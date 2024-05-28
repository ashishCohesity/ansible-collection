import os
import json
from ansible.module_utils.urls import open_url, urllib_error
from urllib import request as urllib_request
from urllib import error as urllib_error
import requests
class InstallError(Exception):
    pass

def raise__cohesity_exception__handler(error, module):
    raise Exception(f"An error occurred: {error}")

# Configuration parameters
params = {
    "cluster": "10.14.55.222",
    "username": "admin",
    "password": "fr8shst8rt",  # Replace with actual password
    "validate_certs": False,
    "native_package": True,
    "operating_system": "RedHat",
    "download_location": "/home/cohesity/work",  # Adjust this path as needed
    "download_uri": ""
}

REQUEST_TIMEOUT = 120

# Function to get authentication token
def get_authentication_token(params):
    server = params.get("cluster")
    username = params.get("username")
    password = params.get("password")

    uri = "https://" + server + "/irisservices/api/v1/public/accessTokens"
    headers = {"Accept": "application/json"}
    payload = {"username": username, "password": password}
    data = json.dumps(payload)
    try:
        response = open_url(
            url=uri,
            data=data,
            headers=headers,
            validate_certs=params.get("validate_certs"),
            timeout=REQUEST_TIMEOUT,
        )
        response_data = json.loads(response.read())
        return response_data["accessToken"]
    except urllib_error.URLError as error:
        raise InstallError(f"Authentication failed: {error}")
    except IOError as error:
        raise InstallError(f"IO Error: {error}")

try:
    server = params.get("cluster")
    path = params.get("download_location")
    if not os.path.exists(path):
        os.makedirs(path)
        print('Path created!')
    token = get_authentication_token(params)
    package_type = "kScript"

    if params.get("native_package"):
        os_type = params.get("operating_system")
        if os_type in ("CentOS", "Rocky", "OracleLinux"):
            package_type = "kRPM"
        elif os_type == "SLES":
            package_type = "kSuseRPM"
        elif os_type == "RedHat":
            package_type = "kPowerPCRPM"
        elif os_type == "Ubuntu":
            package_type = "kDEB"

    if params.get("download_uri"):
        uri = params.get("download_uri")
        headers = {
            "Accept": "application/octet-stream",
            "user-agent": "cohesity-ansible/v1.2.0",
        }
    else:
        uri = (
            f"https://{server}/irisservices/api/v1/public/physicalAgents/download"
            f"?hostType=kLinux&pkgType={package_type}"
        )
        headers = {
            "Accept": "application/octet-stream",
            "Authorization": f"Bearer {token}",
            "user-agent": "cohesity-ansible/v1.2.0",
        }

    print(f"Requesting URI: {uri}")
    req = urllib_request.Request(uri, headers=headers)
    with urllib_request.urlopen(req, timeout=REQUEST_TIMEOUT) as agent:
        resp_headers = agent.headers
        if "content-disposition" in resp_headers:
            filename = resp_headers["content-disposition"].split("=")[1].strip('"')
        else:
            filename = "cohesity-agent-installer"
        
        filepath = os.path.join(path, filename)
        print(f"Saving agent to: {filepath}")
        with open(filepath, "wb") as f:
            f.write(agent.read())
        os.chmod(filepath, 0o755)

except urllib_error.HTTPError as e:
    try:
        error_msg = json.loads(e.read().decode())
        if "message" in error_msg:
            print(f"HTTP Error: {error_msg['message']}")
        else:
            raise__cohesity_exception__handler(e, params)
    except json.JSONDecodeError:
        print(f"HTTP Error: {e.reason}")

except urllib_error.URLError as e:
    raise__cohesity_exception__handler(e, params)

except Exception as error:
    raise__cohesity_exception__handler(error, params)

