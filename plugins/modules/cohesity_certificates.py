#!/usr/bin/python
from ansible.module_utils.basic import AnsibleModule
import os
import json
from urllib.request import urlopen, Request
from urllib.error import URLError, HTTPError
import ssl


class CohesityCertificates:
    def __init__(self, params):
        self.cluster = params.get("cluster")
        self.username = params.get("username")
        self.password = params.get("password")
        self.base_url = f"https://{self.cluster}"
        self.download_location = params.get("download_location")  # Default download location
        self.host_ip = params.get("host_ip")

    def get_authentication_token(self):
        uri = f"{self.base_url}/irisservices/api/v1/public/accessTokens"
        headers = {"Accept": "application/json", "Content-Type": "application/json"}
        payload = json.dumps(
            {"username": self.username, "password": self.password}
        ).encode("utf-8")

        try:
            response = self._send_request(uri, payload, headers, method="POST")
            response_data = json.loads(response.read().decode("utf-8"))
            return response_data["accessToken"]
        except (URLError, HTTPError, IOError) as error:
            raise AnsibleError(f"Authentication failed: {error}")

    def generate_new_certificate(self, access_token):
        uri = f"{self.base_url}/v2/cert-manager/cert"
        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        }

        payload = {
            "organization": "organization0",
            "organizationUnit": "organizationUnit6",
            "countryCode": "countryCode8",
            "state": "state8",
            "city": "city4",
            "keyType": "RSA_4096",
            "commonName": "commonName6",
        }

        data = json.dumps(payload).encode("utf-8")

        try:
            response = self._send_request(uri, data, headers, method="POST")
            return response.read().decode("utf-8")
        except (URLError, HTTPError, IOError) as error:
            raise AnsibleError(f"Failed to generate new certificate: {error}")

    def get_cohesityca_agent_certificates(self, access_token):
        uri = f"{self.base_url}/v2/cert-manager/binary-cert"
        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        }

        payload = {
             "organization": "organization",
            "organizationUnit": "organizationUnit",
            "countryCode": "countryCode",
            "state": "state",
            "city": "city",
            "commonName": "Agent (gRPC server)",
            "sanList": ["Agent (gRPC server)", self.host_ip]
        }

        data = json.dumps(payload).encode("utf-8")
        response = None

        try:
            response = self._send_request(uri, data, headers, method="POST")
            self._save_cert(response)
            return "CohesityCA agent certificates obtained and saved successfully"
        except (URLError, HTTPError, IOError) as error:
            error_message = f"Failed to get CohesityCA agent certificates: {str(error)}"
            if hasattr(error, 'code'):
                error_message += f" (HTTP Error Code: {error.code})"
            if hasattr(error, 'reason'):
                error_message += f" (Reason: {error.reason})"
            if response is not None:
                error_message += f" (Response: {response.status}, {response.reason})"
                try:
                    response_content = response.read().decode()
                    error_message += f" (Response Content: {response_content})"
                except Exception as read_error:
                    error_message += f" (Failed to read response content: {read_error})"
            raise AnsibleError(error_message)


    def _send_request(self, uri, data=None, headers={}, method="GET"):
        if data is None:
            data = b""

        context = ssl.SSLContext(ssl.PROTOCOL_TLS)
        request = Request(uri, data=data, headers=headers, method=method)
        return urlopen(request, context=context)

    def _save_cert(self, response):
        try:
            with open(self.download_location, "wb") as file:
                file.write(response.read())
        except IOError as e:
            error_message = (
                f"Failed to save certificate to {self.download_location}: {e.strerror} "
                f"(Error Code: {e.errno}, Error Message: {e})"
            )
            raise AnsibleError(error_message)


class AnsibleError(Exception):
    pass


def main():
    module_args = dict(
        cluster=dict(type="str", required=True),
        username=dict(type="str", required=True),
        password=dict(type="str", required=True, no_log=True),
        get_agent_certificates=dict(type="bool", required=False, default=False),
        download_location=dict(
            type="str", required=False, default="/tmp/"
        ),
        host_ip=dict(type="str", required=True),
    )

    result = dict(
        changed=False,
        message="",
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    params = module.params

    try:
        cohesity_api = CohesityCertificates(params)
        access_token = cohesity_api.get_authentication_token()
        result["access_token"] = access_token

        if params["get_agent_certificates"]:
            message = cohesity_api.get_cohesityca_agent_certificates(access_token)
            result["message"] = message
        else:
            result["message"] = (
                "No action specified. Use 'get_agent_certificates: true' to obtain CohesityCA agent certificates."
            )

        module.exit_json(**result)

    except AnsibleError as e:
        module.fail_json(msg=str(e))


if __name__ == "__main__":
    main()
