import os
import json
from ansible.module_utils.urls import open_url, urllib_error

class InstallError(Exception):
    pass

def raise_cohesity_exception_handler(error):
    raise Exception(f"An error occurred: {error}")

# Configuration parameters
params = {
    "cluster": "10.14.55.222",
    "username": "admin",
    "password": "fr8shst8rt",  # Replace with actual password
    "validate_certs": False,
    "native_package": True,
    "operating_system": "HP-UX",
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
    if "Solaris" in params.get("operating_system"):
        server = params.get("cluster")
        token = get_authentication_token(params)
        parts = params.get("operating_system").split()
        pkgType = parts[-1].lower()
        if pkgType[0] == ('s'):
            pkgType = 'S' + pkgType[1:]
        distribution = parts[-2].split('.')[0]
        pkgType = 'kSolaris' + distribution + pkgType

        uri = (
            "https://"
            + server
            + "/irisservices/api/v1/public/physicalAgents/download"
            + "?hostType=kSolaris&agentType=kJava&solarisPkgType="
            + pkgType
        )
        headers = {
            "Accept": "application/octet-stream",
            "Authorization": "Bearer " + token,
            "user-agent": "cohesity-ansible/v1.2.0",
        }
    elif params.get("operating_system")=="AIX":
        server = params.get("cluster")
        token = get_authentication_token(params)
        uri = (
                "https://"
                + server
                + "/irisservices/api/v1/public/physicalAgents/download"
                + "?hostType=kAix&agentType=kJava"
            )
        headers = {
            "Accept": "application/octet-stream",
            "Authorization": "Bearer " + token,
            "user-agent": "cohesity-ansible/v1.2.0",
        }
    elif params.get("operating_system")=="HP-UX":
        server = params.get("cluster")
        token = get_authentication_token(params)
        uri = (
                "https://"
                + server
                + "/irisservices/api/v1/public/physicalAgents/download"
                + "?hostType=kHPUX"
            )
        headers = {
            "Accept": "application/octet-stream",
            "Authorization": "Bearer " + token,
            "user-agent": "cohesity-ansible/v1.2.0",
        }
    else:
        os_type = "Linux"
        server = params.get("cluster")
        token = get_authentication_token(params)
        package_type = "kScript"
        if params.get("native_package"):
            if params.get("operating_system") in (
                "CentOS",
                "OracleLinux",
                "Rocky"
            ):
                package_type = "kRPM"
            elif params.get("operating_system") == "RedHat":
                package_type = "kPowerPCRPM"
            elif params.get("operating_system") == "SLES":
                package_type = "kSuseRPM"
            elif params.get("operating_system") == "Ubuntu":
                package_type = "kDEB"
        uri = (
            "https://"
            + server
            + "/irisservices/api/v1/public/physicalAgents/download?hostType=k"
            + os_type
            + "&pkgType="
            + package_type
        )
        headers = {
            "Accept": "application/octet-stream",
            "Authorization": "Bearer " + token,
            "user-agent": "cohesity-ansible/v1.2.0",
        }

    agent = open_url(
        url=uri, headers=headers, validate_certs=False, timeout=REQUEST_TIMEOUT
    )
    resp_headers = agent.headers
    if "content-disposition" in resp_headers.keys():
        filename = resp_headers["content-disposition"].split("=")[1]
    else:
        filename = "cohesity-agent-installer"
    filename = params["download_location"] + "/" + filename
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
        raise InstallError(f"Failed to download the Cohesity Agent. Reason: {error_msg['message']}")
    else:
        raise_cohesity_exception_handler(e)
except urllib_error.URLError as e:
    raise_cohesity_exception_handler(e.read())
except Exception as error:
    raise_cohesity_exception_handler(error)
