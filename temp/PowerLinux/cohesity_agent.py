#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule
import os
import json
from urllib import request as urllib_request
from urllib.error import HTTPError, URLError

REQUEST_TIMEOUT = 60

def get_cohesity_auth_token(module):
    # Placeholder function to get authentication token
    # Implement this function according to your authentication mechanism
    username = module.params.get("username")
    password = module.params.get("password")
    server = module.params.get("cluster")
    
    # Authentication logic here
    # For example:
    auth_url = f"https://{server}/irisservices/api/v1/public/accessTokens"
    auth_data = json.dumps({"domain": "LOCAL", "username": username, "password": password}).encode()
    auth_headers = {"Content-Type": "application/json"}

    request = urllib_request.Request(auth_url, data=auth_data, headers=auth_headers)
    try:
        response = urllib_request.urlopen(request)
        auth_response = json.loads(response.read())
        return auth_response['accessToken']
    except (HTTPError, URLError) as e:
        module.fail_json(msg="Authentication failed", reason=str(e))

def download_agent(module, path):
    try:
        operating_system = module.params.get("operating_system")
        server = module.params.get("cluster")
        token = get_cohesity_auth_token(module)

        if operating_system == "AIX":
            uri = (
                f"https://{server}/irisservices/api/v1/public/physicalAgents/download"
                "?hostType=kAix&agentType=kJava"
            )
        elif not module.params.get("download_uri"):
            os_type = "Linux"
            package_type = "kScript"
            if module.params.get("native_package"):
                os_map = {
                    "CentOS": "kRPM",
                    "Rocky": "kRPM",
                    "RedHat": "kRPM",
                    "OracleLinux": "kRPM",
                    "SLES": "kSuseRPM",
                    "Ubuntu": "kDEB",
                }
                package_type = os_map.get(operating_system, "kScript")
            
            uri = (
                f"https://{server}/irisservices/api/v1/public/physicalAgents/download?"
                f"hostType=k{os_type}&pkgType={package_type}"
            )
        else:
            uri = module.params.get("download_uri")

        headers = {
            "Accept": "application/octet-stream",
            "Authorization": f"Bearer {token}",
            "user-agent": "cohesity-ansible/v1.2.0",
        }

        agent = urllib_request.urlopen(
            urllib_request.Request(uri, headers=headers), timeout=REQUEST_TIMEOUT
        )
        resp_headers = agent.headers
        filename = (
            resp_headers.get("content-disposition", "attachment=cohesity-agent-installer")
            .split("=")[1]
        )
        filename = os.path.join(path, filename)
        
        with open(filename, "wb") as f:
            f.write(agent.read())
        os.chmod(filename, 0o755)
    except (HTTPError, URLError, OSError) as e:
        module.fail_json(
            msg="Failed to download the Cohesity Agent",
            reason=str(e)
        )

    return filename

def main():
    module_args = dict(
        cluster=dict(type='str', required=True),
        username=dict(type='str', required=True),
        password=dict(type='str', required=True, no_log=True),
        validate_certs=dict(type='bool', default=True),
        state=dict(type='str', default='present'),
        create_user=dict(type='bool', default=False),
        native_package=dict(type='bool', default=False),
        operating_system=dict(type='str', required=True),
        download_uri=dict(type='str', required=False, default=None),
        path=dict(type='str', required=False, default='/tmp')
    )

    result = dict(
        changed=False,
        message=''
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    try:
        filename = download_agent(module, module.params['path'])
        result['changed'] = True
        result['message'] = f'Cohesity agent downloaded to {filename}'
    except Exception as e:
        module.fail_json(msg='Failed to install the Cohesity Agent', reason=str(e))

    module.exit_json(**result)

if __name__ == '__main__':
    main()
