from bifrost.base import bifrost_base_pb2 as _bifrost_base_pb2
from bifrost.base import rpc_id_pb2 as _rpc_id_pb2
from bifrost.base import error_pb2 as _error_pb2
from bifrost.portal_proxy import portal_proxy_pb2 as _portal_proxy_pb2
from bifrost.stub import capabilities_pb2 as _capabilities_pb2
from bifrost.stub import proxy_service_pb2 as _proxy_service_pb2
from bifrost.task import bifrost_task_pb2 as _bifrost_task_pb2
from configs import cluster_config_pb2 as _cluster_config_pb2
from magneto.base import error_pb2 as _error_pb2_1
from magneto.agents.base import agent_pb2 as _agent_pb2
from magneto.master.stub import stub_pb2 as _stub_pb2
from magneto.slave.stub import bridge_updates_pb2 as _bridge_updates_pb2
from gandalf.base import error_pb2 as _error_pb2_1_1
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ConnectMessage(_message.Message):
    __slots__ = ("tenant_id", "constituent_id", "session_id", "ip_addr", "capability_message", "version", "hyx_connector_config", "is_rigel_mode", "resource_capacity")
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    CONSTITUENT_ID_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    IP_ADDR_FIELD_NUMBER: _ClassVar[int]
    CAPABILITY_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    HYX_CONNECTOR_CONFIG_FIELD_NUMBER: _ClassVar[int]
    IS_RIGEL_MODE_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_CAPACITY_FIELD_NUMBER: _ClassVar[int]
    tenant_id: str
    constituent_id: int
    session_id: int
    ip_addr: str
    capability_message: _capabilities_pb2.CapabilityProto
    version: str
    hyx_connector_config: _bifrost_base_pb2.HyxConnectorConfigProto
    is_rigel_mode: bool
    resource_capacity: _bifrost_base_pb2.BifrostResourceCapacityProto
    def __init__(self, tenant_id: _Optional[str] = ..., constituent_id: _Optional[int] = ..., session_id: _Optional[int] = ..., ip_addr: _Optional[str] = ..., capability_message: _Optional[_Union[_capabilities_pb2.CapabilityProto, _Mapping]] = ..., version: _Optional[str] = ..., hyx_connector_config: _Optional[_Union[_bifrost_base_pb2.HyxConnectorConfigProto, _Mapping]] = ..., is_rigel_mode: bool = ..., resource_capacity: _Optional[_Union[_bifrost_base_pb2.BifrostResourceCapacityProto, _Mapping]] = ...) -> None: ...

class RpcId(_message.Message):
    __slots__ = ("bifrost_broker_session_id", "request_id")
    BIFROST_BROKER_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    bifrost_broker_session_id: int
    request_id: int
    def __init__(self, bifrost_broker_session_id: _Optional[int] = ..., request_id: _Optional[int] = ...) -> None: ...

class BrokerRequest(_message.Message):
    __slots__ = ("rpc_id", "deadline_msecs", "arg")
    RPC_ID_FIELD_NUMBER: _ClassVar[int]
    DEADLINE_MSECS_FIELD_NUMBER: _ClassVar[int]
    ARG_FIELD_NUMBER: _ClassVar[int]
    rpc_id: _rpc_id_pb2.RpcIdProto
    deadline_msecs: int
    arg: _proxy_service_pb2.BifrostCallArg
    def __init__(self, rpc_id: _Optional[_Union[_rpc_id_pb2.RpcIdProto, _Mapping]] = ..., deadline_msecs: _Optional[int] = ..., arg: _Optional[_Union[_proxy_service_pb2.BifrostCallArg, _Mapping]] = ...) -> None: ...

class BifrostResponse(_message.Message):
    __slots__ = ("rpc_id", "result")
    RPC_ID_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    rpc_id: _rpc_id_pb2.RpcIdProto
    result: _proxy_service_pb2.BifrostCallResult
    def __init__(self, rpc_id: _Optional[_Union[_rpc_id_pb2.RpcIdProto, _Mapping]] = ..., result: _Optional[_Union[_proxy_service_pb2.BifrostCallResult, _Mapping]] = ...) -> None: ...

class StreamMessage(_message.Message):
    __slots__ = ("connect", "request", "response")
    CONNECT_FIELD_NUMBER: _ClassVar[int]
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    connect: ConnectMessage
    request: BrokerRequest
    response: BifrostResponse
    def __init__(self, connect: _Optional[_Union[ConnectMessage, _Mapping]] = ..., request: _Optional[_Union[BrokerRequest, _Mapping]] = ..., response: _Optional[_Union[BifrostResponse, _Mapping]] = ...) -> None: ...

class LivenessArg(_message.Message):
    __slots__ = ("connect_arg",)
    CONNECT_ARG_FIELD_NUMBER: _ClassVar[int]
    connect_arg: ConnectMessage
    def __init__(self, connect_arg: _Optional[_Union[ConnectMessage, _Mapping]] = ...) -> None: ...

class LivenessResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class MagnetoArg(_message.Message):
    __slots__ = ("type", "magneto_constituent_id", "action_update_arg", "update_bridge_task_arg", "update_bifrost_task_arg")
    class CallType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kActionUpdate: _ClassVar[MagnetoArg.CallType]
        kUpdateBridgeTask: _ClassVar[MagnetoArg.CallType]
        kUpdateBifrostTask: _ClassVar[MagnetoArg.CallType]
    kActionUpdate: MagnetoArg.CallType
    kUpdateBridgeTask: MagnetoArg.CallType
    kUpdateBifrostTask: MagnetoArg.CallType
    TYPE_FIELD_NUMBER: _ClassVar[int]
    MAGNETO_CONSTITUENT_ID_FIELD_NUMBER: _ClassVar[int]
    ACTION_UPDATE_ARG_FIELD_NUMBER: _ClassVar[int]
    UPDATE_BRIDGE_TASK_ARG_FIELD_NUMBER: _ClassVar[int]
    UPDATE_BIFROST_TASK_ARG_FIELD_NUMBER: _ClassVar[int]
    type: MagnetoArg.CallType
    magneto_constituent_id: int
    action_update_arg: _bridge_updates_pb2.ActionUpdateArg
    update_bridge_task_arg: _stub_pb2.UpdateBridgeTaskArg
    update_bifrost_task_arg: _bifrost_task_pb2.UpdateBifrostTaskArg
    def __init__(self, type: _Optional[_Union[MagnetoArg.CallType, str]] = ..., magneto_constituent_id: _Optional[int] = ..., action_update_arg: _Optional[_Union[_bridge_updates_pb2.ActionUpdateArg, _Mapping]] = ..., update_bridge_task_arg: _Optional[_Union[_stub_pb2.UpdateBridgeTaskArg, _Mapping]] = ..., update_bifrost_task_arg: _Optional[_Union[_bifrost_task_pb2.UpdateBifrostTaskArg, _Mapping]] = ...) -> None: ...

class MagnetoResult(_message.Message):
    __slots__ = ("error", "type", "action_update_response", "update_bridge_task_response", "update_bifrost_task_response")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ACTION_UPDATE_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_BRIDGE_TASK_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_BIFROST_TASK_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2_1.ErrorProto
    type: MagnetoArg.CallType
    action_update_response: _bridge_updates_pb2.ActionUpdateResult
    update_bridge_task_response: _stub_pb2.UpdateBridgeTaskResult
    update_bifrost_task_response: _bifrost_task_pb2.UpdateBifrostTaskResult
    def __init__(self, error: _Optional[_Union[_error_pb2_1.ErrorProto, _Mapping]] = ..., type: _Optional[_Union[MagnetoArg.CallType, str]] = ..., action_update_response: _Optional[_Union[_bridge_updates_pb2.ActionUpdateResult, _Mapping]] = ..., update_bridge_task_response: _Optional[_Union[_stub_pb2.UpdateBridgeTaskResult, _Mapping]] = ..., update_bifrost_task_response: _Optional[_Union[_bifrost_task_pb2.UpdateBifrostTaskResult, _Mapping]] = ...) -> None: ...

class TestResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class GetTenantInfoArg(_message.Message):
    __slots__ = ("tenant_id",)
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    tenant_id: str
    def __init__(self, tenant_id: _Optional[str] = ...) -> None: ...

class GetTenantInfoResult(_message.Message):
    __slots__ = ("vault_config", "cloud_domain_id", "view_box", "cluster_id", "is_gcm_enabled", "deny_embedded_agent_cert")
    VAULT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    CLOUD_DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_BOX_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    IS_GCM_ENABLED_FIELD_NUMBER: _ClassVar[int]
    DENY_EMBEDDED_AGENT_CERT_FIELD_NUMBER: _ClassVar[int]
    vault_config: _cluster_config_pb2.ClusterConfigProto.Vault
    cloud_domain_id: int
    view_box: _cluster_config_pb2.ClusterConfigProto.ViewBox
    cluster_id: int
    is_gcm_enabled: bool
    deny_embedded_agent_cert: bool
    def __init__(self, vault_config: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.Vault, _Mapping]] = ..., cloud_domain_id: _Optional[int] = ..., view_box: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.ViewBox, _Mapping]] = ..., cluster_id: _Optional[int] = ..., is_gcm_enabled: bool = ..., deny_embedded_agent_cert: bool = ...) -> None: ...

class GetVaultCredentialsArg(_message.Message):
    __slots__ = ("vault_id", "tenant_id", "min_required_credential_validity_secs")
    VAULT_ID_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    MIN_REQUIRED_CREDENTIAL_VALIDITY_SECS_FIELD_NUMBER: _ClassVar[int]
    vault_id: int
    tenant_id: str
    min_required_credential_validity_secs: int
    def __init__(self, vault_id: _Optional[int] = ..., tenant_id: _Optional[str] = ..., min_required_credential_validity_secs: _Optional[int] = ...) -> None: ...

class GetVaultCredentialsResult(_message.Message):
    __slots__ = ("vault_credentials",)
    VAULT_CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    vault_credentials: _cluster_config_pb2.ClusterConfigProto.CloudCredentials
    def __init__(self, vault_credentials: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.CloudCredentials, _Mapping]] = ...) -> None: ...

class UpdateGandalfArg(_message.Message):
    __slots__ = ("update_type", "gandalf_key", "tenant_id", "key_data_zcbuf", "gandalf_key_version")
    class UpdateType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kUpdate: _ClassVar[UpdateGandalfArg.UpdateType]
        kDelete: _ClassVar[UpdateGandalfArg.UpdateType]
    kUpdate: UpdateGandalfArg.UpdateType
    kDelete: UpdateGandalfArg.UpdateType
    UPDATE_TYPE_FIELD_NUMBER: _ClassVar[int]
    GANDALF_KEY_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    KEY_DATA_ZCBUF_FIELD_NUMBER: _ClassVar[int]
    GANDALF_KEY_VERSION_FIELD_NUMBER: _ClassVar[int]
    update_type: UpdateGandalfArg.UpdateType
    gandalf_key: str
    tenant_id: str
    key_data_zcbuf: bytes
    gandalf_key_version: int
    def __init__(self, update_type: _Optional[_Union[UpdateGandalfArg.UpdateType, str]] = ..., gandalf_key: _Optional[str] = ..., tenant_id: _Optional[str] = ..., key_data_zcbuf: _Optional[bytes] = ..., gandalf_key_version: _Optional[int] = ...) -> None: ...

class UpdateGandalfResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2_1_1.ErrorProto.Type
    def __init__(self, error: _Optional[_Union[_error_pb2_1_1.ErrorProto.Type, str]] = ...) -> None: ...

class ReadFileFromLocalFsArg(_message.Message):
    __slots__ = ("filepath", "offset", "num_bytes_to_read")
    FILEPATH_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    NUM_BYTES_TO_READ_FIELD_NUMBER: _ClassVar[int]
    filepath: str
    offset: int
    num_bytes_to_read: int
    def __init__(self, filepath: _Optional[str] = ..., offset: _Optional[int] = ..., num_bytes_to_read: _Optional[int] = ...) -> None: ...

class ReadFileFromLocalFsResult(_message.Message):
    __slots__ = ("error", "errnum", "eof", "data")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ERRNUM_FIELD_NUMBER: _ClassVar[int]
    EOF_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    errnum: int
    eof: bool
    data: bytes
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., errnum: _Optional[int] = ..., eof: bool = ..., data: _Optional[bytes] = ...) -> None: ...

class GetClusterEndpointsArg(_message.Message):
    __slots__ = ("min_cluster_config_gandalf_version",)
    MIN_CLUSTER_CONFIG_GANDALF_VERSION_FIELD_NUMBER: _ClassVar[int]
    min_cluster_config_gandalf_version: int
    def __init__(self, min_cluster_config_gandalf_version: _Optional[int] = ...) -> None: ...

class GetClusterEndpointsResult(_message.Message):
    __slots__ = ("cluster_config_gandalf_version", "endpoint_type", "cluster_endpoints")
    class EndpointType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kUnknown: _ClassVar[GetClusterEndpointsResult.EndpointType]
        kPrimaryIfaceVips: _ClassVar[GetClusterEndpointsResult.EndpointType]
        kStaticNodeIps: _ClassVar[GetClusterEndpointsResult.EndpointType]
    kUnknown: GetClusterEndpointsResult.EndpointType
    kPrimaryIfaceVips: GetClusterEndpointsResult.EndpointType
    kStaticNodeIps: GetClusterEndpointsResult.EndpointType
    CLUSTER_CONFIG_GANDALF_VERSION_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_TYPE_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ENDPOINTS_FIELD_NUMBER: _ClassVar[int]
    cluster_config_gandalf_version: int
    endpoint_type: GetClusterEndpointsResult.EndpointType
    cluster_endpoints: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, cluster_config_gandalf_version: _Optional[int] = ..., endpoint_type: _Optional[_Union[GetClusterEndpointsResult.EndpointType, str]] = ..., cluster_endpoints: _Optional[_Iterable[str]] = ...) -> None: ...

class GetConnectorCertificatesArg(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetConnectorCertificatesResult(_message.Message):
    __slots__ = ("certificates",)
    class Cert(_message.Message):
        __slots__ = ("pem_root_certs", "pem_private_key", "pem_cert_chain", "cert_type")
        PEM_ROOT_CERTS_FIELD_NUMBER: _ClassVar[int]
        PEM_PRIVATE_KEY_FIELD_NUMBER: _ClassVar[int]
        PEM_CERT_CHAIN_FIELD_NUMBER: _ClassVar[int]
        CERT_TYPE_FIELD_NUMBER: _ClassVar[int]
        pem_root_certs: bytes
        pem_private_key: bytes
        pem_cert_chain: bytes
        cert_type: _agent_pb2.AgentCertificateInformation.CertType
        def __init__(self, pem_root_certs: _Optional[bytes] = ..., pem_private_key: _Optional[bytes] = ..., pem_cert_chain: _Optional[bytes] = ..., cert_type: _Optional[_Union[_agent_pb2.AgentCertificateInformation.CertType, str]] = ...) -> None: ...
    CERTIFICATES_FIELD_NUMBER: _ClassVar[int]
    certificates: _containers.RepeatedCompositeFieldContainer[GetConnectorCertificatesResult.Cert]
    def __init__(self, certificates: _Optional[_Iterable[_Union[GetConnectorCertificatesResult.Cert, _Mapping]]] = ...) -> None: ...

class BifrostRequest(_message.Message):
    __slots__ = ("type", "liveness_arg", "magneto_arg", "get_tenant_info_arg", "get_vault_credentials_arg", "update_gandalf_arg", "read_file_from_local_fs_arg", "get_cluster_endpoints_arg", "get_connector_certificates_arg")
    class CallType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kLivenessPing: _ClassVar[BifrostRequest.CallType]
        kMagneto: _ClassVar[BifrostRequest.CallType]
        kTest: _ClassVar[BifrostRequest.CallType]
        kGetTenantInfo: _ClassVar[BifrostRequest.CallType]
        kGetVaultCredentials: _ClassVar[BifrostRequest.CallType]
        kUpdateGandalf: _ClassVar[BifrostRequest.CallType]
        kReadFileFromLocalFs: _ClassVar[BifrostRequest.CallType]
        kGetClusterEndpoints: _ClassVar[BifrostRequest.CallType]
        kGetConnectorCertificates: _ClassVar[BifrostRequest.CallType]
    kLivenessPing: BifrostRequest.CallType
    kMagneto: BifrostRequest.CallType
    kTest: BifrostRequest.CallType
    kGetTenantInfo: BifrostRequest.CallType
    kGetVaultCredentials: BifrostRequest.CallType
    kUpdateGandalf: BifrostRequest.CallType
    kReadFileFromLocalFs: BifrostRequest.CallType
    kGetClusterEndpoints: BifrostRequest.CallType
    kGetConnectorCertificates: BifrostRequest.CallType
    TYPE_FIELD_NUMBER: _ClassVar[int]
    LIVENESS_ARG_FIELD_NUMBER: _ClassVar[int]
    MAGNETO_ARG_FIELD_NUMBER: _ClassVar[int]
    GET_TENANT_INFO_ARG_FIELD_NUMBER: _ClassVar[int]
    GET_VAULT_CREDENTIALS_ARG_FIELD_NUMBER: _ClassVar[int]
    UPDATE_GANDALF_ARG_FIELD_NUMBER: _ClassVar[int]
    READ_FILE_FROM_LOCAL_FS_ARG_FIELD_NUMBER: _ClassVar[int]
    GET_CLUSTER_ENDPOINTS_ARG_FIELD_NUMBER: _ClassVar[int]
    GET_CONNECTOR_CERTIFICATES_ARG_FIELD_NUMBER: _ClassVar[int]
    type: BifrostRequest.CallType
    liveness_arg: LivenessArg
    magneto_arg: MagnetoArg
    get_tenant_info_arg: GetTenantInfoArg
    get_vault_credentials_arg: GetVaultCredentialsArg
    update_gandalf_arg: UpdateGandalfArg
    read_file_from_local_fs_arg: ReadFileFromLocalFsArg
    get_cluster_endpoints_arg: GetClusterEndpointsArg
    get_connector_certificates_arg: GetConnectorCertificatesArg
    def __init__(self, type: _Optional[_Union[BifrostRequest.CallType, str]] = ..., liveness_arg: _Optional[_Union[LivenessArg, _Mapping]] = ..., magneto_arg: _Optional[_Union[MagnetoArg, _Mapping]] = ..., get_tenant_info_arg: _Optional[_Union[GetTenantInfoArg, _Mapping]] = ..., get_vault_credentials_arg: _Optional[_Union[GetVaultCredentialsArg, _Mapping]] = ..., update_gandalf_arg: _Optional[_Union[UpdateGandalfArg, _Mapping]] = ..., read_file_from_local_fs_arg: _Optional[_Union[ReadFileFromLocalFsArg, _Mapping]] = ..., get_cluster_endpoints_arg: _Optional[_Union[GetClusterEndpointsArg, _Mapping]] = ..., get_connector_certificates_arg: _Optional[_Union[GetConnectorCertificatesArg, _Mapping]] = ...) -> None: ...

class BrokerResponse(_message.Message):
    __slots__ = ("error", "type", "liveness_response", "magneto_result", "test_result", "get_tenant_info_result", "get_vault_credentials_result", "update_gandalf_result", "read_file_from_local_fs_result", "get_cluster_endpoints_result", "get_connector_certificates_result")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    LIVENESS_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    MAGNETO_RESULT_FIELD_NUMBER: _ClassVar[int]
    TEST_RESULT_FIELD_NUMBER: _ClassVar[int]
    GET_TENANT_INFO_RESULT_FIELD_NUMBER: _ClassVar[int]
    GET_VAULT_CREDENTIALS_RESULT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_GANDALF_RESULT_FIELD_NUMBER: _ClassVar[int]
    READ_FILE_FROM_LOCAL_FS_RESULT_FIELD_NUMBER: _ClassVar[int]
    GET_CLUSTER_ENDPOINTS_RESULT_FIELD_NUMBER: _ClassVar[int]
    GET_CONNECTOR_CERTIFICATES_RESULT_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    type: BifrostRequest.CallType
    liveness_response: LivenessResponse
    magneto_result: MagnetoResult
    test_result: TestResult
    get_tenant_info_result: GetTenantInfoResult
    get_vault_credentials_result: GetVaultCredentialsResult
    update_gandalf_result: UpdateGandalfResult
    read_file_from_local_fs_result: ReadFileFromLocalFsResult
    get_cluster_endpoints_result: GetClusterEndpointsResult
    get_connector_certificates_result: GetConnectorCertificatesResult
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., type: _Optional[_Union[BifrostRequest.CallType, str]] = ..., liveness_response: _Optional[_Union[LivenessResponse, _Mapping]] = ..., magneto_result: _Optional[_Union[MagnetoResult, _Mapping]] = ..., test_result: _Optional[_Union[TestResult, _Mapping]] = ..., get_tenant_info_result: _Optional[_Union[GetTenantInfoResult, _Mapping]] = ..., get_vault_credentials_result: _Optional[_Union[GetVaultCredentialsResult, _Mapping]] = ..., update_gandalf_result: _Optional[_Union[UpdateGandalfResult, _Mapping]] = ..., read_file_from_local_fs_result: _Optional[_Union[ReadFileFromLocalFsResult, _Mapping]] = ..., get_cluster_endpoints_result: _Optional[_Union[GetClusterEndpointsResult, _Mapping]] = ..., get_connector_certificates_result: _Optional[_Union[GetConnectorCertificatesResult, _Mapping]] = ...) -> None: ...
