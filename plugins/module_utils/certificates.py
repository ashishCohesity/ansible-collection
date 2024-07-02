import os
import json
from urllib.request import urlopen, Request
from urllib.error import URLError, HTTPError
import ssl

class CohesityCertificates:
    def __init__(self, cluster, username, password):
        self.cluster = cluster
        self.username = username
        self.password = password
        self.base_url = f"https://{cluster}"

    def get_authentication_token(self):
        uri = f"{self.base_url}/irisservices/api/v1/public/accessTokens"
        headers = {"Accept": "application/json", "Content-Type": "application/json"}
        payload = json.dumps({"username": self.username, "password": self.password}).encode('utf-8')

        try:
            response = self._send_request(uri, payload, headers, method='POST')
            response_data = json.loads(response.read().decode('utf-8'))
            return response_data["accessToken"]
        except (URLError, HTTPError, IOError) as error:
            raise InstallError(f"Authentication failed: {error}")

    def generate_new_binary_certificate(self, access_token):
        uri = f"{self.base_url}/v2/cert-manager/binary-cert"
        headers = {
            'Authorization': f'Bearer {access_token}',
            'Content-Type': 'application/json'
        }

        payload = {
            "organization": "organization0",
            "organizationUnit": "organizationUnit6",
            "countryCode": "countryCode8",
            "state": "state8",
            "city": "city4",
            "keyType": "RSA_4096",
            "commonName": "commonName6"
        }

        data = json.dumps(payload).encode('utf-8')

        try:
            response = self._send_request(uri, data, headers, method='POST')
            self._save_certificate(response)
            print("Certificate generated and saved successfully")
        except (URLError, HTTPError, IOError) as error:
            raise InstallError(f"Failed to generate certificate: {error}")

    def init_cohesity_ca(self, access_token):
        uri = f"{self.base_url}/v2/cert-manager/bootstrap-ca"
        headers = {
            'Authorization': f'Bearer {access_token}',
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

        payload = {
            "privateKey": "privateKey8",
            "caChain": [
                "caChain7",
                "caChain8",
                "caChain9"
            ]
        }

        data = json.dumps(payload).encode('utf-8')

        try:
            response = self._send_request(uri, data, headers, method='POST')
            print("Initialization of Cohesity CA successful")
        except (URLError, HTTPError, IOError) as error:
            raise InstallError(f"Failed to initialize Cohesity CA: {error}")

    def generate_ca_certificate(self, access_token):
        uri = f"{self.base_url}/v2/cert-manager/ca-certificate"
        headers = {
            'Authorization': f'Bearer {access_token}',
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

        payload = {
            "commonName": "commonName6",
            "organization": "organization0",
            "country": "country0",
            "locality": "locality4"
        }

        data = json.dumps(payload).encode('utf-8')

        try:
            response = self._send_request(uri, data, headers, method='POST')
            print("Generation of CA certificate successful")
        except (URLError, HTTPError, IOError) as error:
            raise InstallError(f"Failed to generate CA certificate: {error}")

    def get_cohesity_ca_keys(self, access_token):
        uri = f"{self.base_url}/v2/cert-manager/ca-keys"
        headers = {
            'Authorization': f'Bearer {access_token}',
            'Accept': 'application/json'
        }

        try:
            response = self._send_request(uri, headers=headers)
            response_data = response.read().decode('utf-8')
            print("Cohesity CA Keys:")
            print(response_data)  # TODO : Adjust handling
        except (URLError, HTTPError, IOError) as error:
            raise InstallError(f"Failed to get Cohesity CA keys: {error}")

    def get_cohesity_ca_status(self, access_token):
        uri = f"{self.base_url}/v2/cert-manager/ca-status"
        headers = {
            'Authorization': f'Bearer {access_token}',
            'Accept': 'application/json'
        }

        try:
            response = self._send_request(uri, headers=headers)
            response_data = response.read().decode('utf-8')
            print("Cohesity CA Status:")
            print(response_data)  # TODO : Adjust handling
        except (URLError, HTTPError, IOError) as error:
            raise InstallError(f"Failed to get Cohesity CA status: {error}")

    def generate_new_certificate(self, access_token):
        uri = f"{self.base_url}/v2/cert-manager/cert"
        headers = {
            'Authorization': f'Bearer {access_token}',
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

        payload = {
            "organization": "organization0",
            "organizationUnit": "organizationUnit6",
            "countryCode": "countryCode8",
            "state": "state8",
            "city": "city4",
            "keyType": "RSA_4096",
            "commonName": "commonName6"
        }

        data = json.dumps(payload).encode('utf-8')

        try:
            response = self._send_request(uri, data, headers, method='POST')
            print("New certificate generated successfully")
        except (URLError, HTTPError, IOError) as error:
            raise InstallError(f"Failed to generate new certificate: {error}")

    def generate_new_csr(self, access_token):
        uri = f"{self.base_url}/v2/cert-manager/csr"
        headers = {
            'Authorization': f'Bearer {access_token}',
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

        payload = {
            "organization": "organization0",
            "organizationUnit": "organizationUnit6",
            "countryCode": "countryCode8",
            "state": "state8",
            "city": "city4",
            "keyType": "RSA_4096",
            "commonName": "commonName6"
            # Add other optional fields if needed (sanList, emailAddress, duration, tenantId)
        }

        data = json.dumps(payload).encode('utf-8')

        try:
            response = self._send_request(uri, data, headers, method='POST')
            print("New CSR generated successfully")
        except (URLError, HTTPError, IOError) as error:
            raise InstallError(f"Failed to generate new CSR: {error}")

    def sign_csr(self, access_token, csr_pem, expiry="24h", tenant_id=None, san_list=None):
        uri = f"{self.base_url}/v2/cert-manager/sign-csr"
        headers = {
            'Authorization': f'Bearer {access_token}',
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

        payload = {
            "csrPem": csr_pem,
            "expiry": expiry,
            "tenantId": tenant_id,
            "sanList": san_list if san_list else []
        }

        data = json.dumps(payload).encode('utf-8')

        try:
            response = self._send_request(uri, data, headers, method='POST')
            print("CSR signed successfully")
            return response.read().decode('utf-8')
        except (URLError, HTTPError, IOError) as error:
            raise InstallError(f"Failed to sign CSR: {error}")

    def sign_csr_from_file(self, access_token, csr_file_path, expiry="24h", tenant_id=None, san_list=None):
        try:
            with open(csr_file_path, 'r') as file:
                csr_pem = file.read()
                return self.sign_csr(access_token, csr_pem, expiry, tenant_id, san_list)
        except IOError as error:
            raise InstallError(f"Failed to read CSR file: {error}")

    def _send_request(self, uri, data=None, headers={}, method='GET'):
        if data is None:
            data = b''

        context = ssl.SSLContext(ssl.PROTOCOL_TLS)
        request = Request(uri, data=data, headers=headers, method=method)
        return urlopen(request, context=context)

    def _save_certificate(self, response):
        download_path = os.path.join("/home/cohesity/work", 'certificate.bin')
        with open(download_path, 'wb') as file:
            file.write(response.read())

class InstallError(Exception):
    pass

def raise_cohesity_exception_handler(error):
    raise Exception(f"An error occurred: {error}")

def main():
    params = {
        "cluster": "10.14.55.222",
        "username": "admin",
        "password": "fr8shst8rt",
    }

    try:
        cohesity_api = CohesityCertificates(params["cluster"], params["username"], params["password"])
        access_token = cohesity_api.get_authentication_token()
        # cohesity_api.generate_new_binary_certificate(access_token)
        # cohesity_api.init_cohesity_ca(access_token)
        # cohesity_api.generate_ca_certificate(access_token)
        # cohesity_api.get_cohesity_ca_keys(access_token)
        # cohesity_api.get_cohesity_ca_status(access_token)
        cohesity_api.generate_new_certificate(access_token)
        # cohesity_api.generate_new_csr(access_token)

        # # Example usage of sign_csr
        # csr_pem_example = "-----BEGIN CERTIFICATE REQUEST-----\n... Your CSR PEM content here ...\n-----END CERTIFICATE REQUEST-----"
        # signed_cert_response = cohesity_api.sign_csr(access_token, csr_pem=csr_pem_example)
        # print("Signed Certificate Response:", signed_cert_response)

        # # Example usage of sign_csr_from_file
        # signed_cert_response = cohesity_api.sign_csr_from_file(access_token, csr_file_path)
        # print("Signed Certificate Response:", signed_cert_response)
    except InstallError as e:
        raise_cohesity_exception_handler(e)

if __name__ == "__main__":
    main()
