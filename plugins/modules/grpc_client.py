print("Importing modules...")
import grpc
import base64
import json
from ansible.module_utils.basic import AnsibleModule
from google.protobuf.json_format import MessageToDict

print("Importing gRPC modules...")
from ansible_collections.cohesity.dataprotect.plugins.module_utils.gRPC.magneto.agents.stub.agent_param_pb2 import (
    GetAgentInfoArg, GetGFlagSettingsArg, UpdateGFlagSettingsArg, ListFilesArg,
    FetchFilesArg, WriteFileArg, RunDiagnosticsArg
)
print("Imported gRPC agent_param_pb2")

from ansible_collections.cohesity.dataprotect.plugins.module_utils.gRPC.magneto.storage_proxy.stub.rpc_args_pb2 import (
    GetRootMetadataArg, WriteFileDataArg, CreateRestoreFilesArg, ProxyBaseArg
)
print("Imported gRPC rpc_args_pb2")

from ansible_collections.cohesity.dataprotect.plugins.module_utils.gRPC.magneto.storage_proxy.stub.grpc_service_pb2_grpc import GRpcServiceStub
print("Imported gRPC grpc_service_pb2_grpc")

from ansible_collections.cohesity.dataprotect.plugins.module_utils.gRPC.magneto.agents.stub.agent_rpc_pb2_grpc import AgentRpcServiceStub
print("Imported gRPC agent_rpc_pb2_grpc")

from ansible_collections.cohesity.dataprotect.plugins.module_utils.gRPC.magneto.agents.stub.agent_base_pb2 import AgentBaseArg
print("Imported gRPC agent_base_pb2")



class GRPCClient:
    def __init__(self, key_path, cacert_path, cert_path, server_address, server_name_override, stub):
        self.key_path = key_path
        self.cacert_path = cacert_path
        self.cert_path = cert_path
        self.server_address = server_address
        self.server_name_override = server_name_override
        self.channel = self.create_secure_channel()
        self.stub = stub(self.channel)

    def create_secure_channel(self):
        with open(self.cacert_path, 'rb') as f:
            trusted_certs = f.read()
        with open(self.cert_path, 'rb') as f:
            client_cert = f.read()
        with open(self.key_path, 'rb') as f:
            client_key = f.read()

        credentials = grpc.ssl_channel_credentials(
            root_certificates=trusted_certs,
            private_key=client_key,
            certificate_chain=client_cert
        )

        options = (('grpc.ssl_target_name_override', self.server_name_override,),)
        channel = grpc.secure_channel(self.server_address, credentials, options)
        return channel

    def execute_rpc_call(self, service_method, request_data):
        try:
            if service_method == "GetAgentInfo":
                response = self.stub.GetAgentInfo(request_data)
            elif service_method == "GetGFlagSettings":
                response = self.stub.GetGFlagSettings(request_data)
            elif service_method == "ListFiles":
                response = self.stub.ListFiles(request_data)
            elif service_method == "UpdateGFlagSettings":
                response = self.stub.UpdateGFlagSettings(request_data)
            elif service_method == "FetchFiles":
                response = self.stub.FetchFiles(request_data)
            elif service_method == "GetRootMetadata":
                response = self.stub.GetRootMetadata(request_data)
            elif service_method == "WriteFileData":
                response = self.stub.WriteFileData(request_data)
            elif service_method == "CreateRestoreFiles":
                response = self.stub.CreateRestoreFiles(request_data)
            elif service_method == "RunDiagnostics":
                response = self.stub.RunDiagnostics(request_data)
            else:
                raise ValueError("Invalid service method")

            response_dict = MessageToDict(response)
            return response_dict
        except grpc.RpcError as e:
            return {
                'failed': True,
                'msg': f"gRPC call failed with code {e.code()}. Details: {e.details()}"
            }

def decode_data(encoded_name):
    return base64.b64decode(encoded_name).decode("utf-8")


def run_module():
    module_args = dict(
        rpc=dict(type='str', required=True, choices=[
            "getAgentInfo", "listFiles", "getGFlagSettings", "updateGFlagSettings",
            "FetchFiles", "getRootMetadata", "writeFileData",
            "createRestoreFiles", "runDiagnostics"
        ]),
        key_path=dict(type='str', required=True),
        cacert_path=dict(type='str', required=True),
        cert_path=dict(type='str', required=True),
        server_address=dict(type='str', required=True),
        server_name_override=dict(type='str', required=True),
    )

    result = dict(
        changed=False,
        response=dict()
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    rpc = module.params['rpc']
    key_path = module.params['key_path']
    cacert_path = module.params['cacert_path']
    cert_path = module.params['cert_path']
    server_address = module.params['server_address']
    server_name_override = module.params['server_name_override']

    if rpc in ["getAgentInfo", "listFiles", "getGFlagSettings", "updateGFlagSettings", "FetchFiles", "runDiagnostics"]:
        grpc_client = GRPCClient(key_path, cacert_path, cert_path, server_address, server_name_override, AgentRpcServiceStub)
    else:
        grpc_client = GRPCClient(key_path, cacert_path, cert_path, server_address, server_name_override, GRpcServiceStub)

    request_data = None
    service_method = rpc
    if rpc == "getAgentInfo":
        request_data = GetAgentInfoArg(
            header=AgentBaseArg(
                task_id=-1,
                client_agent_api_version=-1,
                agent_incarnation_id=-1,
                cluster_id=-1,
                cluster_incarnation_id=-1
            ),
            perform_cluster_detection=True,
            populate_subnet_for_all_cluster_nodes=False,
            vlan_hostname_tag=""
        )
    elif rpc == "getGFlagSettings":
        request_data = GetGFlagSettingsArg(
            header=AgentBaseArg(
                task_id=-1,
                client_agent_api_version=-1,
                agent_incarnation_id=-1,
                cluster_id=-1,
                cluster_incarnation_id=-1
            )
        )
    elif rpc == "listFiles":
        request_data = ListFilesArg(
            header=AgentBaseArg(
                task_id=-1,
                client_agent_api_version=-1,
                agent_incarnation_id=-1,
                cluster_id=-1,
                cluster_incarnation_id=-1
            )
        )
    elif rpc == "updateGFlagSettings":
        request_data = UpdateGFlagSettingsArg(
            header=AgentBaseArg(
                task_id=-1,
                client_agent_api_version=-1,
                agent_incarnation_id=-1,
                cluster_id=-1,
                cluster_incarnation_id=-1
            ),
        )
    elif rpc == "FetchFiles":
        encoded_file_names = [
            "L2hvbWUvY29oZXNpdHlhZ2VudC9jb2hlc2l0eWFnZW50L2RhdGEvbG9ncy9saW51eF9hZ2VudF9leGVjLnBhcmVudC5sb2NhbGhvc3QubG9jYWxkb21haW4uY29oZXNpdHlhZ2VudC5sb2cuSU5GTy4yMDI0MDYxNC0wOTQ3MjUuMTU3NDMyMg=="
        ]
        decoded_file_names = [decode_data(name) for name in encoded_file_names]
        request_data = FetchFilesArg(
            header=AgentBaseArg(
                task_id=-1,
                client_agent_api_version=-1,
                agent_incarnation_id=-1,
                cluster_id=-1,
                cluster_incarnation_id=-1
            ),
            file_name_vec=[name.encode("utf-8") for name in decoded_file_names],
            offset_bytes=0,
            limit_size_bytes=-1,
        )
    elif rpc == "getRootMetadata":
        request_data = GetRootMetadataArg()
    elif rpc == "writeFileData":
        request_data = WriteFileArg(
            header=AgentBaseArg(
                task_id=-1,
                client_agent_api_version=-1,
                agent_incarnation_id=-1,
                cluster_id=-1,
                cluster_incarnation_id=-1
            )
        )
    elif rpc == "createRestoreFiles":
        request_data = CreateRestoreFilesArg(
            header=AgentBaseArg(
                task_id=-1,
                client_agent_api_version=-1,
                agent_incarnation_id=-1,
                cluster_id=-1,
                cluster_incarnation_id=-1
            )
        )
    elif rpc == "runDiagnostics":
        request_data = RunDiagnosticsArg(
            header=AgentBaseArg(
                task_id=-1,
                client_agent_api_version=-1,
                agent_incarnation_id=-1,
                cluster_id=-1,
                cluster_incarnation_id=-1
            ),
            offset_bytes=0,
            limit_size_bytes=-1,
            create_tarball=True,
            local_alarm_call=False,
            get_all_logs=False
        )

    response_dict = grpc_client.execute_rpc_call(service_method, request_data)

    if rpc == "FetchFiles":
        for file in response_dict.get('fileVec', []):
            file['originalFileName'] = decode_data(file['originalFileName'])

    result['response'] = response_dict

    if module.check_mode:
        module.exit_json(**result)

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()