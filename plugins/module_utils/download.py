import os
import json
from ansible.module_utils.urls import open_url, urllib_error

class InstallError(Exception):
    pass

def raise__cohesity_exception__handler(error, module):
    raise Exception(f"An error occurred: {error}")

# Configuration parameters
params = {
    "cluster": "10.14.49.14",
    "username": "admin",
    "password": "fr8shst8rt",  # Replace with actual password
    "validate_certs": False,
    "native_package": False,
    "operating_system": "Ubuntu",
    "download_location": "/home/cohesity/ansible-collection/plugins/module_utils",  # Adjust this path as needed
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

# Main code to download the agent
try:
    server = params.get("cluster")
    path = params.get("download_location")
    token = get_authentication_token(params)
    # print(token)
    package_type = "kScript"
    if params.get("native_package"):
        if params.get("operating_system") in ("CentOS", "Rocky", "RedHat", "OracleLinux"):
            package_type = "kRPM"
        elif params.get("operating_system") == "SLES":
            package_type = "kSuseRPM"
        elif params.get("operating_system") == "Ubuntu":
            package_type = "kDEB"

    if params.get("download_uri"):
        uri = params.get("download_uri")
        headers = {
            "Accept": "application/octet-stream",
            "user-agent": "cohesity-ansible/v1.2.0",
        }
    else:
        uri = (
            "https://" + server +
            "/irisservices/api/v1/public/physicalAgents/download?hostType=kLinux&pkgType=" + package_type
        )
        headers = {
            "Accept": "application/octet-stream",
            "Authorization": "Bearer " + token,
            "user-agent": "cohesity-ansible/v1.2.0",
        }
    # print(headers)
    agent = open_url(
            url=uri, headers=headers, validate_certs=False, timeout=REQUEST_TIMEOUT
        )
    resp_headers = agent.headers
    # print(resp_headers)
    if "content-disposition" in resp_headers.keys():
        filename = resp_headers["content-disposition"].split("=")[1]
    else:
        filename = "cohesity-agent-installer"
    
    filename = path + "/" + filename
    try:
        with open(filename, "wb") as f:
            f.write(agent.read())
        os.chmod(filename, 0o755)
    except Exception as e:
        raise InstallError(e)
    finally:
        f.close()
    
except urllib_error.HTTPError as e:
    error_msg = json.loads(e.read())
    if "message" in error_msg:
        print(f"HTTP Error: {error_msg['message']}")
    else:
        raise__cohesity_exception__handler(e, params)
except urllib_error.URLError as e:
    raise__cohesity_exception__handler(e.read(), params)
except Exception as error:
    raise__cohesity_exception__handler(error, params)
