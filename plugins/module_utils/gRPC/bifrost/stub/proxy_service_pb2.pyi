from bifrost.base import bifrost_base_pb2 as _bifrost_base_pb2
from bifrost.base import error_pb2 as _error_pb2
from bifrost.portal_proxy import portal_proxy_pb2 as _portal_proxy_pb2
from bifrost.stub import bifrost_debug_params_pb2 as _bifrost_debug_params_pb2
from bifrost.stub import bridge_auth_params_pb2 as _bridge_auth_params_pb2
from bifrost.stub import magneto_connector_params_pb2 as _magneto_connector_params_pb2
from bifrost.stub import storage_proxy_params_pb2 as _storage_proxy_params_pb2
from bifrost.stub import smb_proxy_params_pb2 as _smb_proxy_params_pb2
from bifrost.task import bifrost_task_pb2 as _bifrost_task_pb2
from bridge.base import error_pb2 as _error_pb2_1
from bridge.magneto.base import magneto_actions_pb2 as _magneto_actions_pb2
from open_util.net import protorpc_pb2 as _protorpc_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BifrostCallArg(_message.Message):
    __slots__ = ("tenant_id", "bifrost_constituent_id", "bifrost_session_id", "type", "magneto_connector_arg", "magneto_action_executor_arg", "storage_proxy_arg", "bifrost_schedule_task_arg", "bifrost_debug_arg", "test_number", "get_bifrost_rt_arg", "update_reverse_tunnel_arg", "bridge_auth_arg", "smb_proxy_arg", "proxy_stream_setup_arg", "update_bifrost_connector_group_id_arg")
    class CallType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kMagnetoConnector: _ClassVar[BifrostCallArg.CallType]
        kMagnetoActionExecutor: _ClassVar[BifrostCallArg.CallType]
        kStorageProxy: _ClassVar[BifrostCallArg.CallType]
        kBifrostDebug: _ClassVar[BifrostCallArg.CallType]
        kCurlHttpClientBifrost: _ClassVar[BifrostCallArg.CallType]
        kTest: _ClassVar[BifrostCallArg.CallType]
        kGetBifrostRt: _ClassVar[BifrostCallArg.CallType]
        kUpdateReverseTunnel: _ClassVar[BifrostCallArg.CallType]
        kBridgeAuth: _ClassVar[BifrostCallArg.CallType]
        kSmbProxy: _ClassVar[BifrostCallArg.CallType]
        kSocksProxyStreamSetupRequest: _ClassVar[BifrostCallArg.CallType]
        kUpdateBifrostConnectorGroupId: _ClassVar[BifrostCallArg.CallType]
        kResetBifrost: _ClassVar[BifrostCallArg.CallType]
    kMagnetoConnector: BifrostCallArg.CallType
    kMagnetoActionExecutor: BifrostCallArg.CallType
    kStorageProxy: BifrostCallArg.CallType
    kBifrostDebug: BifrostCallArg.CallType
    kCurlHttpClientBifrost: BifrostCallArg.CallType
    kTest: BifrostCallArg.CallType
    kGetBifrostRt: BifrostCallArg.CallType
    kUpdateReverseTunnel: BifrostCallArg.CallType
    kBridgeAuth: BifrostCallArg.CallType
    kSmbProxy: BifrostCallArg.CallType
    kSocksProxyStreamSetupRequest: BifrostCallArg.CallType
    kUpdateBifrostConnectorGroupId: BifrostCallArg.CallType
    kResetBifrost: BifrostCallArg.CallType
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    BIFROST_CONSTITUENT_ID_FIELD_NUMBER: _ClassVar[int]
    BIFROST_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    MAGNETO_CONNECTOR_ARG_FIELD_NUMBER: _ClassVar[int]
    MAGNETO_ACTION_EXECUTOR_ARG_FIELD_NUMBER: _ClassVar[int]
    STORAGE_PROXY_ARG_FIELD_NUMBER: _ClassVar[int]
    BIFROST_SCHEDULE_TASK_ARG_FIELD_NUMBER: _ClassVar[int]
    BIFROST_DEBUG_ARG_FIELD_NUMBER: _ClassVar[int]
    TEST_NUMBER_FIELD_NUMBER: _ClassVar[int]
    GET_BIFROST_RT_ARG_FIELD_NUMBER: _ClassVar[int]
    UPDATE_REVERSE_TUNNEL_ARG_FIELD_NUMBER: _ClassVar[int]
    BRIDGE_AUTH_ARG_FIELD_NUMBER: _ClassVar[int]
    SMB_PROXY_ARG_FIELD_NUMBER: _ClassVar[int]
    PROXY_STREAM_SETUP_ARG_FIELD_NUMBER: _ClassVar[int]
    UPDATE_BIFROST_CONNECTOR_GROUP_ID_ARG_FIELD_NUMBER: _ClassVar[int]
    tenant_id: str
    bifrost_constituent_id: int
    bifrost_session_id: int
    type: BifrostCallArg.CallType
    magneto_connector_arg: _magneto_connector_params_pb2.MagnetoConnectorArg
    magneto_action_executor_arg: _magneto_actions_pb2.ExecuteActionArg
    storage_proxy_arg: _storage_proxy_params_pb2.StorageProxyArg
    bifrost_schedule_task_arg: _bifrost_task_pb2.BifrostScheduleTaskArg
    bifrost_debug_arg: _bifrost_debug_params_pb2.BifrostDebugArg
    test_number: int
    get_bifrost_rt_arg: GetBifrostRtArg
    update_reverse_tunnel_arg: _bifrost_base_pb2.BifrostRtConfigProto
    bridge_auth_arg: _bridge_auth_params_pb2.BridgeAuthArg
    smb_proxy_arg: _smb_proxy_params_pb2.SmbProxyArg
    proxy_stream_setup_arg: ProxyStreamSetupArg
    update_bifrost_connector_group_id_arg: UpdateBifrostConnectorGroupIdArg
    def __init__(self, tenant_id: _Optional[str] = ..., bifrost_constituent_id: _Optional[int] = ..., bifrost_session_id: _Optional[int] = ..., type: _Optional[_Union[BifrostCallArg.CallType, str]] = ..., magneto_connector_arg: _Optional[_Union[_magneto_connector_params_pb2.MagnetoConnectorArg, _Mapping]] = ..., magneto_action_executor_arg: _Optional[_Union[_magneto_actions_pb2.ExecuteActionArg, _Mapping]] = ..., storage_proxy_arg: _Optional[_Union[_storage_proxy_params_pb2.StorageProxyArg, _Mapping]] = ..., bifrost_schedule_task_arg: _Optional[_Union[_bifrost_task_pb2.BifrostScheduleTaskArg, _Mapping]] = ..., bifrost_debug_arg: _Optional[_Union[_bifrost_debug_params_pb2.BifrostDebugArg, _Mapping]] = ..., test_number: _Optional[int] = ..., get_bifrost_rt_arg: _Optional[_Union[GetBifrostRtArg, _Mapping]] = ..., update_reverse_tunnel_arg: _Optional[_Union[_bifrost_base_pb2.BifrostRtConfigProto, _Mapping]] = ..., bridge_auth_arg: _Optional[_Union[_bridge_auth_params_pb2.BridgeAuthArg, _Mapping]] = ..., smb_proxy_arg: _Optional[_Union[_smb_proxy_params_pb2.SmbProxyArg, _Mapping]] = ..., proxy_stream_setup_arg: _Optional[_Union[ProxyStreamSetupArg, _Mapping]] = ..., update_bifrost_connector_group_id_arg: _Optional[_Union[UpdateBifrostConnectorGroupIdArg, _Mapping]] = ...) -> None: ...

class MagnetoExecuteActionResult(_message.Message):
    __slots__ = ("bridge_error", "execute_action_result")
    BRIDGE_ERROR_FIELD_NUMBER: _ClassVar[int]
    EXECUTE_ACTION_RESULT_FIELD_NUMBER: _ClassVar[int]
    bridge_error: _error_pb2_1.ErrorProto
    execute_action_result: _magneto_actions_pb2.ExecuteActionResult
    def __init__(self, bridge_error: _Optional[_Union[_error_pb2_1.ErrorProto, _Mapping]] = ..., execute_action_result: _Optional[_Union[_magneto_actions_pb2.ExecuteActionResult, _Mapping]] = ...) -> None: ...

class BifrostCallResult(_message.Message):
    __slots__ = ("error", "magneto_connector_result", "magneto_action_executor_result", "magneto_execute_action_result", "storage_proxy_result", "bifrost_schedule_task_result", "bifrost_debug_result", "test_number", "bridge_auth_result", "smb_proxy_result", "get_bifrost_rt_result", "dummy_data_vec")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    MAGNETO_CONNECTOR_RESULT_FIELD_NUMBER: _ClassVar[int]
    MAGNETO_ACTION_EXECUTOR_RESULT_FIELD_NUMBER: _ClassVar[int]
    MAGNETO_EXECUTE_ACTION_RESULT_FIELD_NUMBER: _ClassVar[int]
    STORAGE_PROXY_RESULT_FIELD_NUMBER: _ClassVar[int]
    BIFROST_SCHEDULE_TASK_RESULT_FIELD_NUMBER: _ClassVar[int]
    BIFROST_DEBUG_RESULT_FIELD_NUMBER: _ClassVar[int]
    TEST_NUMBER_FIELD_NUMBER: _ClassVar[int]
    BRIDGE_AUTH_RESULT_FIELD_NUMBER: _ClassVar[int]
    SMB_PROXY_RESULT_FIELD_NUMBER: _ClassVar[int]
    GET_BIFROST_RT_RESULT_FIELD_NUMBER: _ClassVar[int]
    DUMMY_DATA_VEC_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    magneto_connector_result: _magneto_connector_params_pb2.MagnetoConnectorResult
    magneto_action_executor_result: _magneto_actions_pb2.ExecuteActionResult
    magneto_execute_action_result: MagnetoExecuteActionResult
    storage_proxy_result: _storage_proxy_params_pb2.StorageProxyResult
    bifrost_schedule_task_result: _bifrost_task_pb2.BifrostScheduleTaskResult
    bifrost_debug_result: _bifrost_debug_params_pb2.BifrostDebugResult
    test_number: int
    bridge_auth_result: _bridge_auth_params_pb2.BridgeAuthResult
    smb_proxy_result: _smb_proxy_params_pb2.SmbProxyResult
    get_bifrost_rt_result: GetBifrostRtResult
    dummy_data_vec: _containers.RepeatedScalarFieldContainer[bytes]
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., magneto_connector_result: _Optional[_Union[_magneto_connector_params_pb2.MagnetoConnectorResult, _Mapping]] = ..., magneto_action_executor_result: _Optional[_Union[_magneto_actions_pb2.ExecuteActionResult, _Mapping]] = ..., magneto_execute_action_result: _Optional[_Union[MagnetoExecuteActionResult, _Mapping]] = ..., storage_proxy_result: _Optional[_Union[_storage_proxy_params_pb2.StorageProxyResult, _Mapping]] = ..., bifrost_schedule_task_result: _Optional[_Union[_bifrost_task_pb2.BifrostScheduleTaskResult, _Mapping]] = ..., bifrost_debug_result: _Optional[_Union[_bifrost_debug_params_pb2.BifrostDebugResult, _Mapping]] = ..., test_number: _Optional[int] = ..., bridge_auth_result: _Optional[_Union[_bridge_auth_params_pb2.BridgeAuthResult, _Mapping]] = ..., smb_proxy_result: _Optional[_Union[_smb_proxy_params_pb2.SmbProxyResult, _Mapping]] = ..., get_bifrost_rt_result: _Optional[_Union[GetBifrostRtResult, _Mapping]] = ..., dummy_data_vec: _Optional[_Iterable[bytes]] = ...) -> None: ...

class GetBifrostRtArg(_message.Message):
    __slots__ = ("should_get_bifrost_rt_status", "should_get_bifrost_rt_conf")
    SHOULD_GET_BIFROST_RT_STATUS_FIELD_NUMBER: _ClassVar[int]
    SHOULD_GET_BIFROST_RT_CONF_FIELD_NUMBER: _ClassVar[int]
    should_get_bifrost_rt_status: bool
    should_get_bifrost_rt_conf: bool
    def __init__(self, should_get_bifrost_rt_status: bool = ..., should_get_bifrost_rt_conf: bool = ...) -> None: ...

class GetBifrostRtResult(_message.Message):
    __slots__ = ("service_status", "does_bifrost_rt_conf_file_exist", "bifrost_rt_conf")
    SERVICE_STATUS_FIELD_NUMBER: _ClassVar[int]
    DOES_BIFROST_RT_CONF_FILE_EXIST_FIELD_NUMBER: _ClassVar[int]
    BIFROST_RT_CONF_FIELD_NUMBER: _ClassVar[int]
    service_status: _bifrost_base_pb2.BifrostRtServiceStatus
    does_bifrost_rt_conf_file_exist: bool
    bifrost_rt_conf: _bifrost_base_pb2.BifrostRtConfigProto
    def __init__(self, service_status: _Optional[_Union[_bifrost_base_pb2.BifrostRtServiceStatus, str]] = ..., does_bifrost_rt_conf_file_exist: bool = ..., bifrost_rt_conf: _Optional[_Union[_bifrost_base_pb2.BifrostRtConfigProto, _Mapping]] = ...) -> None: ...

class GetProxyEndUserInfoArg(_message.Message):
    __slots__ = ("port",)
    PORT_FIELD_NUMBER: _ClassVar[int]
    port: int
    def __init__(self, port: _Optional[int] = ...) -> None: ...

class GetProxyEndUserInfoResult(_message.Message):
    __slots__ = ("error", "session_proto")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    SESSION_PROTO_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    session_proto: _portal_proxy_pb2.SessionProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., session_proto: _Optional[_Union[_portal_proxy_pb2.SessionProto, _Mapping]] = ...) -> None: ...

class ProxyStreamSetupArg(_message.Message):
    __slots__ = ("stream_id_str", "target_host_endpoint")
    STREAM_ID_STR_FIELD_NUMBER: _ClassVar[int]
    TARGET_HOST_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    stream_id_str: str
    target_host_endpoint: str
    def __init__(self, stream_id_str: _Optional[str] = ..., target_host_endpoint: _Optional[str] = ...) -> None: ...

class UpdateBifrostConnectorGroupIdArg(_message.Message):
    __slots__ = ("connector_id", "connection_id", "connector_group_id", "update_version")
    class UpdateVersion(_message.Message):
        __slots__ = ("version", "cluster_id")
        VERSION_FIELD_NUMBER: _ClassVar[int]
        CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
        version: int
        cluster_id: int
        def __init__(self, version: _Optional[int] = ..., cluster_id: _Optional[int] = ...) -> None: ...
    CONNECTOR_ID_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_ID_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    UPDATE_VERSION_FIELD_NUMBER: _ClassVar[int]
    connector_id: int
    connection_id: int
    connector_group_id: int
    update_version: UpdateBifrostConnectorGroupIdArg.UpdateVersion
    def __init__(self, connector_id: _Optional[int] = ..., connection_id: _Optional[int] = ..., connector_group_id: _Optional[int] = ..., update_version: _Optional[_Union[UpdateBifrostConnectorGroupIdArg.UpdateVersion, _Mapping]] = ...) -> None: ...

class BrokerListenForSocksArg(_message.Message):
    __slots__ = ("tenant_id", "network_realm_id", "target_host_endpoint", "bifrost_constituent_id", "connector_group_id")
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    NETWORK_REALM_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_HOST_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    BIFROST_CONSTITUENT_ID_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    tenant_id: str
    network_realm_id: int
    target_host_endpoint: str
    bifrost_constituent_id: int
    connector_group_id: int
    def __init__(self, tenant_id: _Optional[str] = ..., network_realm_id: _Optional[int] = ..., target_host_endpoint: _Optional[str] = ..., bifrost_constituent_id: _Optional[int] = ..., connector_group_id: _Optional[int] = ...) -> None: ...

class BrokerListenForSocksResult(_message.Message):
    __slots__ = ("error", "listen_port")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    LISTEN_PORT_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    listen_port: int
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., listen_port: _Optional[int] = ...) -> None: ...

class CreateNetworkRealmArg(_message.Message):
    __slots__ = ("network_realm",)
    NETWORK_REALM_FIELD_NUMBER: _ClassVar[int]
    network_realm: _bifrost_base_pb2.NetworkRealm
    def __init__(self, network_realm: _Optional[_Union[_bifrost_base_pb2.NetworkRealm, _Mapping]] = ...) -> None: ...

class CreateNetworkRealmResult(_message.Message):
    __slots__ = ("error", "realm_id", "network_realm")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    REALM_ID_FIELD_NUMBER: _ClassVar[int]
    NETWORK_REALM_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    realm_id: int
    network_realm: _bifrost_base_pb2.NetworkRealm
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., realm_id: _Optional[int] = ..., network_realm: _Optional[_Union[_bifrost_base_pb2.NetworkRealm, _Mapping]] = ...) -> None: ...

class UpdateNetworkRealmArg(_message.Message):
    __slots__ = ("network_realm", "scribe_version")
    NETWORK_REALM_FIELD_NUMBER: _ClassVar[int]
    SCRIBE_VERSION_FIELD_NUMBER: _ClassVar[int]
    network_realm: _bifrost_base_pb2.NetworkRealm
    scribe_version: int
    def __init__(self, network_realm: _Optional[_Union[_bifrost_base_pb2.NetworkRealm, _Mapping]] = ..., scribe_version: _Optional[int] = ...) -> None: ...

class UpdateNetworkRealmResult(_message.Message):
    __slots__ = ("error", "network_realm")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    NETWORK_REALM_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    network_realm: _bifrost_base_pb2.NetworkRealm
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., network_realm: _Optional[_Union[_bifrost_base_pb2.NetworkRealm, _Mapping]] = ...) -> None: ...

class GetNetworkRealmsArg(_message.Message):
    __slots__ = ("realm_id_vec", "include_deleted")
    REALM_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_DELETED_FIELD_NUMBER: _ClassVar[int]
    realm_id_vec: _containers.RepeatedScalarFieldContainer[int]
    include_deleted: bool
    def __init__(self, realm_id_vec: _Optional[_Iterable[int]] = ..., include_deleted: bool = ...) -> None: ...

class GetNetworkRealmsResult(_message.Message):
    __slots__ = ("error", "network_realm_vec", "scribe_version_vec")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    NETWORK_REALM_VEC_FIELD_NUMBER: _ClassVar[int]
    SCRIBE_VERSION_VEC_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    network_realm_vec: _containers.RepeatedCompositeFieldContainer[_bifrost_base_pb2.NetworkRealm]
    scribe_version_vec: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., network_realm_vec: _Optional[_Iterable[_Union[_bifrost_base_pb2.NetworkRealm, _Mapping]]] = ..., scribe_version_vec: _Optional[_Iterable[int]] = ...) -> None: ...

class DeleteNetworkRealmArg(_message.Message):
    __slots__ = ("realm_id",)
    REALM_ID_FIELD_NUMBER: _ClassVar[int]
    realm_id: int
    def __init__(self, realm_id: _Optional[int] = ...) -> None: ...

class DeleteNetworkRealmResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class CreateHyxConnectorArg(_message.Message):
    __slots__ = ("connector_config", "tenant_id")
    CONNECTOR_CONFIG_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    connector_config: _bifrost_base_pb2.HyxConnectorConfigProto
    tenant_id: str
    def __init__(self, connector_config: _Optional[_Union[_bifrost_base_pb2.HyxConnectorConfigProto, _Mapping]] = ..., tenant_id: _Optional[str] = ...) -> None: ...

class CreateHyxConnectorResult(_message.Message):
    __slots__ = ("error", "connector_config")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_CONFIG_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    connector_config: _bifrost_base_pb2.HyxConnectorConfigProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., connector_config: _Optional[_Union[_bifrost_base_pb2.HyxConnectorConfigProto, _Mapping]] = ...) -> None: ...

class UpdateHyxConnectorArg(_message.Message):
    __slots__ = ("connector_config", "tenant_id")
    CONNECTOR_CONFIG_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    connector_config: _bifrost_base_pb2.HyxConnectorConfigProto
    tenant_id: str
    def __init__(self, connector_config: _Optional[_Union[_bifrost_base_pb2.HyxConnectorConfigProto, _Mapping]] = ..., tenant_id: _Optional[str] = ...) -> None: ...

class UpdateHyxConnectorResult(_message.Message):
    __slots__ = ("error", "connector_config")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_CONFIG_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    connector_config: _bifrost_base_pb2.HyxConnectorConfigProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., connector_config: _Optional[_Union[_bifrost_base_pb2.HyxConnectorConfigProto, _Mapping]] = ...) -> None: ...

class GetHyxConnectorsArg(_message.Message):
    __slots__ = ("hyx_connector_id_vec", "realm_id", "tenant_id")
    HYX_CONNECTOR_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    REALM_ID_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    hyx_connector_id_vec: _containers.RepeatedScalarFieldContainer[int]
    realm_id: int
    tenant_id: str
    def __init__(self, hyx_connector_id_vec: _Optional[_Iterable[int]] = ..., realm_id: _Optional[int] = ..., tenant_id: _Optional[str] = ...) -> None: ...

class GetHyxConnectorsResult(_message.Message):
    __slots__ = ("error", "connector_config_vec")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_CONFIG_VEC_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    connector_config_vec: _containers.RepeatedCompositeFieldContainer[_bifrost_base_pb2.HyxConnectorConfigProto]
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., connector_config_vec: _Optional[_Iterable[_Union[_bifrost_base_pb2.HyxConnectorConfigProto, _Mapping]]] = ...) -> None: ...

class DeleteHyxConnectorArg(_message.Message):
    __slots__ = ("hyx_connector_id", "tenant_id")
    HYX_CONNECTOR_ID_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    hyx_connector_id: int
    tenant_id: str
    def __init__(self, hyx_connector_id: _Optional[int] = ..., tenant_id: _Optional[str] = ...) -> None: ...

class DeleteHyxConnectorResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class BringUpConnectorArg(_message.Message):
    __slots__ = ("realm_id",)
    REALM_ID_FIELD_NUMBER: _ClassVar[int]
    realm_id: int
    def __init__(self, realm_id: _Optional[int] = ...) -> None: ...

class BringUpConnectorResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class UpdateBifrostReverseTunnelArg(_message.Message):
    __slots__ = ("bifrost_server_id", "rt_config")
    BIFROST_SERVER_ID_FIELD_NUMBER: _ClassVar[int]
    RT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    bifrost_server_id: _bifrost_base_pb2.BifrostServerIdProto
    rt_config: _bifrost_base_pb2.BifrostRtConfigProto
    def __init__(self, bifrost_server_id: _Optional[_Union[_bifrost_base_pb2.BifrostServerIdProto, _Mapping]] = ..., rt_config: _Optional[_Union[_bifrost_base_pb2.BifrostRtConfigProto, _Mapping]] = ...) -> None: ...

class UpdateBifrostReverseTunnelResult(_message.Message):
    __slots__ = ("error", "service_status", "bifrost_rt_conf")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    SERVICE_STATUS_FIELD_NUMBER: _ClassVar[int]
    BIFROST_RT_CONF_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    service_status: _bifrost_base_pb2.BifrostRtServiceStatus
    bifrost_rt_conf: _bifrost_base_pb2.BifrostRtConfigProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., service_status: _Optional[_Union[_bifrost_base_pb2.BifrostRtServiceStatus, str]] = ..., bifrost_rt_conf: _Optional[_Union[_bifrost_base_pb2.BifrostRtConfigProto, _Mapping]] = ...) -> None: ...
