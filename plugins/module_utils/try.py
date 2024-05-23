from cohesity_auth import get__cohesity_auth__token
class ParamsObject:
    def __init__(self, params):
        self.params = params

# Define the parameters
params = {
    "cluster": "10.14.49.14",
    "username": "admin",
    "password": "fr8shst8rt",
    "validate_certs": False,
    "state": "present",
    "create_user": False,
    "native_package": False,
    "operating_system": "Ubuntu",
    "download_location": "",
    "service_user": "cohesityagent",
    "service_group": "cohesityagent",
    "file_based": False,
    "download_uri": "",
    "host": "",
    "upgrade": False,
    "wait_minutes": 30
}

# Create ParamsObject instance
params_obj = ParamsObject(params)

# Call the function with the ParamsObject instance
token = get__cohesity_auth__token(params_obj)

# Now you have the authentication token available in the variable `token`
print("Authentication Token:", token)
