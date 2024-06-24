from magneto.agents.base import agent_pb2 as _agent_pb2
from magneto.agents.stub import agent_param_pb2 as _agent_param_pb2
from magneto.agents.windows.sql.base import sql_param_pb2 as _sql_param_pb2
from magneto.agents.windows.stub import ad_param_pb2 as _ad_param_pb2
from magneto.agents.windows.stub import exchange_param_pb2 as _exchange_param_pb2
from magneto.base import api_version_pb2 as _api_version_pb2
from magneto.base import credentials_pb2 as _credentials_pb2
from magneto.base.entities import exchange_pb2 as _exchange_pb2
from magneto.base.entities import sql_pb2 as _sql_pb2
from magneto.base import enums_pb2 as _enums_pb2
from magneto.base import error_pb2 as _error_pb2
from magneto.base import permissions_pb2 as _permissions_pb2
from magneto.master.base import master_pb2 as _master_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ExecuteAgentActionArg(_message.Message):
    __slots__ = ("api_request_attr", "env_type", "api_version", "user_info", "task_id", "ad_parent_entity_id", "exchange_action_params", "ad_action_arg", "exchange_action_arg", "get_app_topology_arg", "sql_action_arg", "network_realm_id", "o365_action_arg")
    API_REQUEST_ATTR_FIELD_NUMBER: _ClassVar[int]
    ENV_TYPE_FIELD_NUMBER: _ClassVar[int]
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    USER_INFO_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    AD_PARENT_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    EXCHANGE_ACTION_PARAMS_FIELD_NUMBER: _ClassVar[int]
    AD_ACTION_ARG_FIELD_NUMBER: _ClassVar[int]
    EXCHANGE_ACTION_ARG_FIELD_NUMBER: _ClassVar[int]
    GET_APP_TOPOLOGY_ARG_FIELD_NUMBER: _ClassVar[int]
    SQL_ACTION_ARG_FIELD_NUMBER: _ClassVar[int]
    NETWORK_REALM_ID_FIELD_NUMBER: _ClassVar[int]
    O365_ACTION_ARG_FIELD_NUMBER: _ClassVar[int]
    api_request_attr: _master_pb2.APIRequestAttr
    env_type: _enums_pb2.Environment.Type
    api_version: _api_version_pb2.APIVersion
    user_info: _permissions_pb2.UserInformation
    task_id: int
    ad_parent_entity_id: int
    exchange_action_params: ExchangeActionAdditionalParams
    ad_action_arg: _ad_param_pb2.ExecuteADActionArg
    exchange_action_arg: _exchange_param_pb2.ExecuteExchangeActionArg
    get_app_topology_arg: _agent_param_pb2.GetAppTopologyArg
    sql_action_arg: _sql_param_pb2.ExecuteSQLActionArg
    network_realm_id: int
    o365_action_arg: O365ActionArg
    def __init__(self, api_request_attr: _Optional[_Union[_master_pb2.APIRequestAttr, _Mapping]] = ..., env_type: _Optional[_Union[_enums_pb2.Environment.Type, str]] = ..., api_version: _Optional[_Union[_api_version_pb2.APIVersion, _Mapping]] = ..., user_info: _Optional[_Union[_permissions_pb2.UserInformation, _Mapping]] = ..., task_id: _Optional[int] = ..., ad_parent_entity_id: _Optional[int] = ..., exchange_action_params: _Optional[_Union[ExchangeActionAdditionalParams, _Mapping]] = ..., ad_action_arg: _Optional[_Union[_ad_param_pb2.ExecuteADActionArg, _Mapping]] = ..., exchange_action_arg: _Optional[_Union[_exchange_param_pb2.ExecuteExchangeActionArg, _Mapping]] = ..., get_app_topology_arg: _Optional[_Union[_agent_param_pb2.GetAppTopologyArg, _Mapping]] = ..., sql_action_arg: _Optional[_Union[_sql_param_pb2.ExecuteSQLActionArg, _Mapping]] = ..., network_realm_id: _Optional[int] = ..., o365_action_arg: _Optional[_Union[O365ActionArg, _Mapping]] = ...) -> None: ...

class ExecuteAgentActionResult(_message.Message):
    __slots__ = ("error", "env_type", "ad_action_result", "exchange_action_result", "exchange_result", "get_app_topology_result", "sql_action_result", "o365_action_result")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ENV_TYPE_FIELD_NUMBER: _ClassVar[int]
    AD_ACTION_RESULT_FIELD_NUMBER: _ClassVar[int]
    EXCHANGE_ACTION_RESULT_FIELD_NUMBER: _ClassVar[int]
    EXCHANGE_RESULT_FIELD_NUMBER: _ClassVar[int]
    GET_APP_TOPOLOGY_RESULT_FIELD_NUMBER: _ClassVar[int]
    SQL_ACTION_RESULT_FIELD_NUMBER: _ClassVar[int]
    O365_ACTION_RESULT_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    env_type: _enums_pb2.Environment.Type
    ad_action_result: _ad_param_pb2.ExecuteADActionResult
    exchange_action_result: _exchange_param_pb2.ExecuteExchangeActionResult
    exchange_result: ExchangeActionResult
    get_app_topology_result: GetAppTopologyResult
    sql_action_result: _sql_param_pb2.ExecuteSQLActionResult
    o365_action_result: O365ActionResult
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., env_type: _Optional[_Union[_enums_pb2.Environment.Type, str]] = ..., ad_action_result: _Optional[_Union[_ad_param_pb2.ExecuteADActionResult, _Mapping]] = ..., exchange_action_result: _Optional[_Union[_exchange_param_pb2.ExecuteExchangeActionResult, _Mapping]] = ..., exchange_result: _Optional[_Union[ExchangeActionResult, _Mapping]] = ..., get_app_topology_result: _Optional[_Union[GetAppTopologyResult, _Mapping]] = ..., sql_action_result: _Optional[_Union[_sql_param_pb2.ExecuteSQLActionResult, _Mapping]] = ..., o365_action_result: _Optional[_Union[O365ActionResult, _Mapping]] = ...) -> None: ...

class ExchangeActionAdditionalParams(_message.Message):
    __slots__ = ("exchange_endpoint", "exchange_dag_entity_id")
    EXCHANGE_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    EXCHANGE_DAG_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    exchange_endpoint: str
    exchange_dag_entity_id: int
    def __init__(self, exchange_endpoint: _Optional[str] = ..., exchange_dag_entity_id: _Optional[int] = ...) -> None: ...

class ExchangeActionResult(_message.Message):
    __slots__ = ("action_type", "exchange_topology")
    ACTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    EXCHANGE_TOPOLOGY_FIELD_NUMBER: _ClassVar[int]
    action_type: _exchange_param_pb2.ExchangeActionType.Type
    exchange_topology: ExchangeTopology
    def __init__(self, action_type: _Optional[_Union[_exchange_param_pb2.ExchangeActionType.Type, str]] = ..., exchange_topology: _Optional[_Union[ExchangeTopology, _Mapping]] = ...) -> None: ...

class ExchangeTopology(_message.Message):
    __slots__ = ("is_standalone_server", "exchange_dag_info", "exchange_dag_entity_id")
    IS_STANDALONE_SERVER_FIELD_NUMBER: _ClassVar[int]
    EXCHANGE_DAG_INFO_FIELD_NUMBER: _ClassVar[int]
    EXCHANGE_DAG_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    is_standalone_server: bool
    exchange_dag_info: _exchange_pb2.ExchangeDAGInfo
    exchange_dag_entity_id: int
    def __init__(self, is_standalone_server: bool = ..., exchange_dag_info: _Optional[_Union[_exchange_pb2.ExchangeDAGInfo, _Mapping]] = ..., exchange_dag_entity_id: _Optional[int] = ...) -> None: ...

class GetAppTopologyResult(_message.Message):
    __slots__ = ("error", "app_topology_vec")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    APP_TOPOLOGY_VEC_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    app_topology_vec: _containers.RepeatedCompositeFieldContainer[AppTopology]
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., app_topology_vec: _Optional[_Iterable[_Union[AppTopology, _Mapping]]] = ...) -> None: ...

class SqlServer(_message.Message):
    __slots__ = ("resource", "id", "status", "error", "agent_sw_version_str", "agent_supported_status", "last_agent_info_time_usecs", "is_primary", "sql_instance_vec", "display_messages", "host_settings_check_result_vec", "is_selected_by_default")
    class Status(_message.Message):
        __slots__ = ()
        class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kUnknown: _ClassVar[SqlServer.Status.Type]
            kHealthy: _ClassVar[SqlServer.Status.Type]
            kUnregistered: _ClassVar[SqlServer.Status.Type]
            kUnreachable: _ClassVar[SqlServer.Status.Type]
            kUnHealthy: _ClassVar[SqlServer.Status.Type]
            kError: _ClassVar[SqlServer.Status.Type]
        kUnknown: SqlServer.Status.Type
        kHealthy: SqlServer.Status.Type
        kUnregistered: SqlServer.Status.Type
        kUnreachable: SqlServer.Status.Type
        kUnHealthy: SqlServer.Status.Type
        kError: SqlServer.Status.Type
        def __init__(self) -> None: ...
    class AgentSupportedStatus(_message.Message):
        __slots__ = ()
        class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kSupported: _ClassVar[SqlServer.AgentSupportedStatus.Type]
            kUpgrade: _ClassVar[SqlServer.AgentSupportedStatus.Type]
            kUnsupported: _ClassVar[SqlServer.AgentSupportedStatus.Type]
        kSupported: SqlServer.AgentSupportedStatus.Type
        kUpgrade: SqlServer.AgentSupportedStatus.Type
        kUnsupported: SqlServer.AgentSupportedStatus.Type
        def __init__(self) -> None: ...
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    AGENT_SW_VERSION_STR_FIELD_NUMBER: _ClassVar[int]
    AGENT_SUPPORTED_STATUS_FIELD_NUMBER: _ClassVar[int]
    LAST_AGENT_INFO_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    IS_PRIMARY_FIELD_NUMBER: _ClassVar[int]
    SQL_INSTANCE_VEC_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_MESSAGES_FIELD_NUMBER: _ClassVar[int]
    HOST_SETTINGS_CHECK_RESULT_VEC_FIELD_NUMBER: _ClassVar[int]
    IS_SELECTED_BY_DEFAULT_FIELD_NUMBER: _ClassVar[int]
    resource: _agent_pb2.ClusterNetworkingInfo.Resource
    id: _agent_param_pb2.TopologyNode.NodeID
    status: SqlServer.Status.Type
    error: _error_pb2.ErrorProto
    agent_sw_version_str: str
    agent_supported_status: SqlServer.AgentSupportedStatus.Type
    last_agent_info_time_usecs: int
    is_primary: bool
    sql_instance_vec: _containers.RepeatedCompositeFieldContainer[_sql_pb2.SQLInstanceInfo]
    display_messages: _containers.RepeatedScalarFieldContainer[str]
    host_settings_check_result_vec: _containers.RepeatedCompositeFieldContainer[_agent_pb2.HostSettingsCheckResult]
    is_selected_by_default: bool
    def __init__(self, resource: _Optional[_Union[_agent_pb2.ClusterNetworkingInfo.Resource, _Mapping]] = ..., id: _Optional[_Union[_agent_param_pb2.TopologyNode.NodeID, _Mapping]] = ..., status: _Optional[_Union[SqlServer.Status.Type, str]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., agent_sw_version_str: _Optional[str] = ..., agent_supported_status: _Optional[_Union[SqlServer.AgentSupportedStatus.Type, str]] = ..., last_agent_info_time_usecs: _Optional[int] = ..., is_primary: bool = ..., sql_instance_vec: _Optional[_Iterable[_Union[_sql_pb2.SQLInstanceInfo, _Mapping]]] = ..., display_messages: _Optional[_Iterable[str]] = ..., host_settings_check_result_vec: _Optional[_Iterable[_Union[_agent_pb2.HostSettingsCheckResult, _Mapping]]] = ..., is_selected_by_default: bool = ...) -> None: ...

class SqlAppTopology(_message.Message):
    __slots__ = ("is_standalone_server", "standalone_vec", "fci_cluster_vec", "aag_group_vec")
    class FCICluster(_message.Message):
        __slots__ = ("id", "instance_name", "resource", "fci_node_vec", "is_selected_by_default", "error")
        ID_FIELD_NUMBER: _ClassVar[int]
        INSTANCE_NAME_FIELD_NUMBER: _ClassVar[int]
        RESOURCE_FIELD_NUMBER: _ClassVar[int]
        FCI_NODE_VEC_FIELD_NUMBER: _ClassVar[int]
        IS_SELECTED_BY_DEFAULT_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        id: _agent_param_pb2.TopologyNode.NodeID
        instance_name: str
        resource: _agent_pb2.ClusterNetworkingInfo.Resource
        fci_node_vec: _containers.RepeatedCompositeFieldContainer[SqlServer]
        is_selected_by_default: bool
        error: _error_pb2.ErrorProto
        def __init__(self, id: _Optional[_Union[_agent_param_pb2.TopologyNode.NodeID, _Mapping]] = ..., instance_name: _Optional[str] = ..., resource: _Optional[_Union[_agent_pb2.ClusterNetworkingInfo.Resource, _Mapping]] = ..., fci_node_vec: _Optional[_Iterable[_Union[SqlServer, _Mapping]]] = ..., is_selected_by_default: bool = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...
    class AAGGroup(_message.Message):
        __slots__ = ("id", "group_name", "resource", "aag_node_vec", "aag_fci_cluster_vec", "aag_info")
        ID_FIELD_NUMBER: _ClassVar[int]
        GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
        RESOURCE_FIELD_NUMBER: _ClassVar[int]
        AAG_NODE_VEC_FIELD_NUMBER: _ClassVar[int]
        AAG_FCI_CLUSTER_VEC_FIELD_NUMBER: _ClassVar[int]
        AAG_INFO_FIELD_NUMBER: _ClassVar[int]
        id: _agent_param_pb2.TopologyNode.NodeID
        group_name: str
        resource: _agent_pb2.ClusterNetworkingInfo.Resource
        aag_node_vec: _containers.RepeatedCompositeFieldContainer[SqlServer]
        aag_fci_cluster_vec: _containers.RepeatedCompositeFieldContainer[SqlAppTopology.FCICluster]
        aag_info: _sql_pb2.AAGInfo
        def __init__(self, id: _Optional[_Union[_agent_param_pb2.TopologyNode.NodeID, _Mapping]] = ..., group_name: _Optional[str] = ..., resource: _Optional[_Union[_agent_pb2.ClusterNetworkingInfo.Resource, _Mapping]] = ..., aag_node_vec: _Optional[_Iterable[_Union[SqlServer, _Mapping]]] = ..., aag_fci_cluster_vec: _Optional[_Iterable[_Union[SqlAppTopology.FCICluster, _Mapping]]] = ..., aag_info: _Optional[_Union[_sql_pb2.AAGInfo, _Mapping]] = ...) -> None: ...
    IS_STANDALONE_SERVER_FIELD_NUMBER: _ClassVar[int]
    STANDALONE_VEC_FIELD_NUMBER: _ClassVar[int]
    FCI_CLUSTER_VEC_FIELD_NUMBER: _ClassVar[int]
    AAG_GROUP_VEC_FIELD_NUMBER: _ClassVar[int]
    is_standalone_server: bool
    standalone_vec: _containers.RepeatedCompositeFieldContainer[SqlServer]
    fci_cluster_vec: _containers.RepeatedCompositeFieldContainer[SqlAppTopology.FCICluster]
    aag_group_vec: _containers.RepeatedCompositeFieldContainer[SqlAppTopology.AAGGroup]
    def __init__(self, is_standalone_server: bool = ..., standalone_vec: _Optional[_Iterable[_Union[SqlServer, _Mapping]]] = ..., fci_cluster_vec: _Optional[_Iterable[_Union[SqlAppTopology.FCICluster, _Mapping]]] = ..., aag_group_vec: _Optional[_Iterable[_Union[SqlAppTopology.AAGGroup, _Mapping]]] = ...) -> None: ...

class AppTopology(_message.Message):
    __slots__ = ("error", "env_type", "sql_app_topology")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ENV_TYPE_FIELD_NUMBER: _ClassVar[int]
    SQL_APP_TOPOLOGY_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    env_type: _enums_pb2.Environment.Type
    sql_app_topology: SqlAppTopology
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., env_type: _Optional[_Union[_enums_pb2.Environment.Type, str]] = ..., sql_app_topology: _Optional[_Union[SqlAppTopology, _Mapping]] = ...) -> None: ...

class O365ActionType(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kCreateAzureApplications: _ClassVar[O365ActionType.Type]
        kUpdateAzureApplications: _ClassVar[O365ActionType.Type]
    kCreateAzureApplications: O365ActionType.Type
    kUpdateAzureApplications: O365ActionType.Type
    def __init__(self) -> None: ...

class O365ActionArg(_message.Message):
    __slots__ = ("action_type", "entity_access_info", "count")
    ACTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ACCESS_INFO_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    action_type: O365ActionType.Type
    entity_access_info: _master_pb2.EntityAccessInfo
    count: int
    def __init__(self, action_type: _Optional[_Union[O365ActionType.Type, str]] = ..., entity_access_info: _Optional[_Union[_master_pb2.EntityAccessInfo, _Mapping]] = ..., count: _Optional[int] = ...) -> None: ...

class O365ActionResult(_message.Message):
    __slots__ = ("action_type", "app_credentials_vec")
    ACTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    APP_CREDENTIALS_VEC_FIELD_NUMBER: _ClassVar[int]
    action_type: O365ActionType.Type
    app_credentials_vec: _containers.RepeatedCompositeFieldContainer[_credentials_pb2.MSGraphAppCredentials]
    def __init__(self, action_type: _Optional[_Union[O365ActionType.Type, str]] = ..., app_credentials_vec: _Optional[_Iterable[_Union[_credentials_pb2.MSGraphAppCredentials, _Mapping]]] = ...) -> None: ...
