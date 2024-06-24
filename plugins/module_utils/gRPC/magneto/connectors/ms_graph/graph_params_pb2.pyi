from google.protobuf import struct_pb2 as _struct_pb2
from magneto.base import credentials_pb2 as _credentials_pb2
from magneto.base import enums_pb2 as _enums_pb2
from magneto.base.entities import o365_pb2 as _o365_pb2
from magneto.base import error_pb2 as _error_pb2
from magneto.base import magneto_pb2 as _magneto_pb2
from magneto.base import env_params_pb2 as _env_params_pb2
from magneto.connectors.ms_graph import graph_pb2 as _graph_pb2
from magneto.connectors.ms_graph import graph_external_pb2 as _graph_external_pb2
from magneto.connectors.o365 import o365_error_pb2 as _o365_error_pb2
from magneto.connectors.outlook import outlook_pb2 as _outlook_pb2
from magneto.connectors.outlook import outlook_external_pb2 as _outlook_external_pb2
from magneto.master.base import agent_actions_pb2 as _agent_actions_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GraphBaseResult(_message.Message):
    __slots__ = ("request_throttled", "retry_after_delay_in_secs", "throttling_time_usecs", "http_status", "num_api_calls")
    REQUEST_THROTTLED_FIELD_NUMBER: _ClassVar[int]
    RETRY_AFTER_DELAY_IN_SECS_FIELD_NUMBER: _ClassVar[int]
    THROTTLING_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    HTTP_STATUS_FIELD_NUMBER: _ClassVar[int]
    NUM_API_CALLS_FIELD_NUMBER: _ClassVar[int]
    request_throttled: bool
    retry_after_delay_in_secs: int
    throttling_time_usecs: int
    http_status: int
    num_api_calls: int
    def __init__(self, request_throttled: bool = ..., retry_after_delay_in_secs: _Optional[int] = ..., throttling_time_usecs: _Optional[int] = ..., http_status: _Optional[int] = ..., num_api_calls: _Optional[int] = ...) -> None: ...

class GraphBaseArg(_message.Message):
    __slots__ = ("workload_type", "backup_type")
    WORKLOAD_TYPE_FIELD_NUMBER: _ClassVar[int]
    BACKUP_TYPE_FIELD_NUMBER: _ClassVar[int]
    workload_type: _enums_pb2.Environment.Type
    backup_type: _enums_pb2.ScheduledBackupType.Type
    def __init__(self, workload_type: _Optional[_Union[_enums_pb2.Environment.Type, str]] = ..., backup_type: _Optional[_Union[_enums_pb2.ScheduledBackupType.Type, str]] = ...) -> None: ...

class ValidateGraphCredentialsArg(_message.Message):
    __slots__ = ("params", "additional_params", "detailed_report")
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_PARAMS_FIELD_NUMBER: _ClassVar[int]
    DETAILED_REPORT_FIELD_NUMBER: _ClassVar[int]
    params: _magneto_pb2.RegisteredEntityO365Params
    additional_params: _magneto_pb2.AdditionalConnectorParams
    detailed_report: bool
    def __init__(self, params: _Optional[_Union[_magneto_pb2.RegisteredEntityO365Params, _Mapping]] = ..., additional_params: _Optional[_Union[_magneto_pb2.AdditionalConnectorParams, _Mapping]] = ..., detailed_report: bool = ...) -> None: ...

class ValidateGraphCredentialsResult(_message.Message):
    __slots__ = ("graph_base_result", "missing_permissions_vec", "dead_time")
    GRAPH_BASE_RESULT_FIELD_NUMBER: _ClassVar[int]
    MISSING_PERMISSIONS_VEC_FIELD_NUMBER: _ClassVar[int]
    DEAD_TIME_FIELD_NUMBER: _ClassVar[int]
    graph_base_result: GraphBaseResult
    missing_permissions_vec: _containers.RepeatedCompositeFieldContainer[_graph_pb2.AppApiPermissions]
    dead_time: int
    def __init__(self, graph_base_result: _Optional[_Union[GraphBaseResult, _Mapping]] = ..., missing_permissions_vec: _Optional[_Iterable[_Union[_graph_pb2.AppApiPermissions, _Mapping]]] = ..., dead_time: _Optional[int] = ...) -> None: ...

class GetServicePrincipalsArg(_message.Message):
    __slots__ = ("service_principal_id_vec", "app_id", "app_displayname")
    SERVICE_PRINCIPAL_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    APP_DISPLAYNAME_FIELD_NUMBER: _ClassVar[int]
    service_principal_id_vec: _containers.RepeatedScalarFieldContainer[str]
    app_id: str
    app_displayname: str
    def __init__(self, service_principal_id_vec: _Optional[_Iterable[str]] = ..., app_id: _Optional[str] = ..., app_displayname: _Optional[str] = ...) -> None: ...

class GetServicePrincipalsResult(_message.Message):
    __slots__ = ("service_principal_vec", "next_link", "graph_base_result")
    SERVICE_PRINCIPAL_VEC_FIELD_NUMBER: _ClassVar[int]
    NEXT_LINK_FIELD_NUMBER: _ClassVar[int]
    GRAPH_BASE_RESULT_FIELD_NUMBER: _ClassVar[int]
    service_principal_vec: _containers.RepeatedCompositeFieldContainer[_graph_pb2.ServicePrincipal]
    next_link: str
    graph_base_result: GraphBaseResult
    def __init__(self, service_principal_vec: _Optional[_Iterable[_Union[_graph_pb2.ServicePrincipal, _Mapping]]] = ..., next_link: _Optional[str] = ..., graph_base_result: _Optional[_Union[GraphBaseResult, _Mapping]] = ...) -> None: ...

class GetAzureApplicationsArg(_message.Message):
    __slots__ = ("azure_application_vec", "display_name_prefix", "application_tag")
    AZURE_APPLICATION_VEC_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_PREFIX_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_TAG_FIELD_NUMBER: _ClassVar[int]
    azure_application_vec: _containers.RepeatedCompositeFieldContainer[_graph_pb2.AzureActiveDirectoryAppManifest]
    display_name_prefix: str
    application_tag: str
    def __init__(self, azure_application_vec: _Optional[_Iterable[_Union[_graph_pb2.AzureActiveDirectoryAppManifest, _Mapping]]] = ..., display_name_prefix: _Optional[str] = ..., application_tag: _Optional[str] = ...) -> None: ...

class GetAzureApplicationsResult(_message.Message):
    __slots__ = ("azure_application_vec", "next_link", "graph_base_result")
    AZURE_APPLICATION_VEC_FIELD_NUMBER: _ClassVar[int]
    NEXT_LINK_FIELD_NUMBER: _ClassVar[int]
    GRAPH_BASE_RESULT_FIELD_NUMBER: _ClassVar[int]
    azure_application_vec: _containers.RepeatedCompositeFieldContainer[_graph_pb2.AzureActiveDirectoryAppManifest]
    next_link: str
    graph_base_result: GraphBaseResult
    def __init__(self, azure_application_vec: _Optional[_Iterable[_Union[_graph_pb2.AzureActiveDirectoryAppManifest, _Mapping]]] = ..., next_link: _Optional[str] = ..., graph_base_result: _Optional[_Union[GraphBaseResult, _Mapping]] = ...) -> None: ...

class AddAppPasswordCredentialsArg(_message.Message):
    __slots__ = ("azure_application_vec",)
    AZURE_APPLICATION_VEC_FIELD_NUMBER: _ClassVar[int]
    azure_application_vec: _containers.RepeatedCompositeFieldContainer[_graph_pb2.AzureActiveDirectoryAppManifest]
    def __init__(self, azure_application_vec: _Optional[_Iterable[_Union[_graph_pb2.AzureActiveDirectoryAppManifest, _Mapping]]] = ...) -> None: ...

class AddAppPasswordCredentialsResult(_message.Message):
    __slots__ = ("azure_application_vec", "graph_base_result")
    AZURE_APPLICATION_VEC_FIELD_NUMBER: _ClassVar[int]
    GRAPH_BASE_RESULT_FIELD_NUMBER: _ClassVar[int]
    azure_application_vec: _containers.RepeatedCompositeFieldContainer[_graph_pb2.AzureActiveDirectoryAppManifest]
    graph_base_result: GraphBaseResult
    def __init__(self, azure_application_vec: _Optional[_Iterable[_Union[_graph_pb2.AzureActiveDirectoryAppManifest, _Mapping]]] = ..., graph_base_result: _Optional[_Union[GraphBaseResult, _Mapping]] = ...) -> None: ...

class CreateServicePrincipalsArg(_message.Message):
    __slots__ = ("azure_application_vec",)
    AZURE_APPLICATION_VEC_FIELD_NUMBER: _ClassVar[int]
    azure_application_vec: _containers.RepeatedCompositeFieldContainer[_graph_pb2.AzureActiveDirectoryAppManifest]
    def __init__(self, azure_application_vec: _Optional[_Iterable[_Union[_graph_pb2.AzureActiveDirectoryAppManifest, _Mapping]]] = ...) -> None: ...

class CreateServicePrincipalsResult(_message.Message):
    __slots__ = ("service_principal_vec", "graph_base_result")
    SERVICE_PRINCIPAL_VEC_FIELD_NUMBER: _ClassVar[int]
    GRAPH_BASE_RESULT_FIELD_NUMBER: _ClassVar[int]
    service_principal_vec: _containers.RepeatedCompositeFieldContainer[_graph_pb2.ServicePrincipal]
    graph_base_result: GraphBaseResult
    def __init__(self, service_principal_vec: _Optional[_Iterable[_Union[_graph_pb2.ServicePrincipal, _Mapping]]] = ..., graph_base_result: _Optional[_Union[GraphBaseResult, _Mapping]] = ...) -> None: ...

class CreateAzureApplicationsArg(_message.Message):
    __slots__ = ("existing_app_credentials_vec", "display_name_prefix", "display_name", "count", "unique_id", "action_type")
    EXISTING_APP_CREDENTIALS_VEC_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_PREFIX_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    UNIQUE_ID_FIELD_NUMBER: _ClassVar[int]
    ACTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    existing_app_credentials_vec: _containers.RepeatedCompositeFieldContainer[_credentials_pb2.MSGraphAppCredentials]
    display_name_prefix: str
    display_name: str
    count: int
    unique_id: str
    action_type: _agent_actions_pb2.O365ActionType.Type
    def __init__(self, existing_app_credentials_vec: _Optional[_Iterable[_Union[_credentials_pb2.MSGraphAppCredentials, _Mapping]]] = ..., display_name_prefix: _Optional[str] = ..., display_name: _Optional[str] = ..., count: _Optional[int] = ..., unique_id: _Optional[str] = ..., action_type: _Optional[_Union[_agent_actions_pb2.O365ActionType.Type, str]] = ...) -> None: ...

class CreateAzureApplicationsResult(_message.Message):
    __slots__ = ("app_credentials_vec", "graph_base_result")
    APP_CREDENTIALS_VEC_FIELD_NUMBER: _ClassVar[int]
    GRAPH_BASE_RESULT_FIELD_NUMBER: _ClassVar[int]
    app_credentials_vec: _containers.RepeatedCompositeFieldContainer[_credentials_pb2.MSGraphAppCredentials]
    graph_base_result: GraphBaseResult
    def __init__(self, app_credentials_vec: _Optional[_Iterable[_Union[_credentials_pb2.MSGraphAppCredentials, _Mapping]]] = ..., graph_base_result: _Optional[_Union[GraphBaseResult, _Mapping]] = ...) -> None: ...

class AssignAppDelegatedPermissionsArg(_message.Message):
    __slots__ = ("app_permission_vec",)
    APP_PERMISSION_VEC_FIELD_NUMBER: _ClassVar[int]
    app_permission_vec: _containers.RepeatedCompositeFieldContainer[_graph_pb2.OAuth2PermissionGrant]
    def __init__(self, app_permission_vec: _Optional[_Iterable[_Union[_graph_pb2.OAuth2PermissionGrant, _Mapping]]] = ...) -> None: ...

class AssignAppDelegatedPermissionsResult(_message.Message):
    __slots__ = ("graph_base_result",)
    GRAPH_BASE_RESULT_FIELD_NUMBER: _ClassVar[int]
    graph_base_result: GraphBaseResult
    def __init__(self, graph_base_result: _Optional[_Union[GraphBaseResult, _Mapping]] = ...) -> None: ...

class AssignAppRolePermissionsArg(_message.Message):
    __slots__ = ("app_role_vec",)
    APP_ROLE_VEC_FIELD_NUMBER: _ClassVar[int]
    app_role_vec: _containers.RepeatedCompositeFieldContainer[_graph_pb2.AppRoleAssignment]
    def __init__(self, app_role_vec: _Optional[_Iterable[_Union[_graph_pb2.AppRoleAssignment, _Mapping]]] = ...) -> None: ...

class AssignAppRolePermissionsResult(_message.Message):
    __slots__ = ("graph_base_result",)
    GRAPH_BASE_RESULT_FIELD_NUMBER: _ClassVar[int]
    graph_base_result: GraphBaseResult
    def __init__(self, graph_base_result: _Optional[_Union[GraphBaseResult, _Mapping]] = ...) -> None: ...

class RegisterAzureApplicationsArg(_message.Message):
    __slots__ = ("display_name_prefix", "count", "display_name_suffix_counter", "unique_id")
    DISPLAY_NAME_PREFIX_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_SUFFIX_COUNTER_FIELD_NUMBER: _ClassVar[int]
    UNIQUE_ID_FIELD_NUMBER: _ClassVar[int]
    display_name_prefix: str
    count: int
    display_name_suffix_counter: int
    unique_id: str
    def __init__(self, display_name_prefix: _Optional[str] = ..., count: _Optional[int] = ..., display_name_suffix_counter: _Optional[int] = ..., unique_id: _Optional[str] = ...) -> None: ...

class RegisterAzureApplicationsResult(_message.Message):
    __slots__ = ("azure_application_vec", "graph_base_result")
    AZURE_APPLICATION_VEC_FIELD_NUMBER: _ClassVar[int]
    GRAPH_BASE_RESULT_FIELD_NUMBER: _ClassVar[int]
    azure_application_vec: _containers.RepeatedCompositeFieldContainer[_graph_pb2.AzureActiveDirectoryAppManifest]
    graph_base_result: GraphBaseResult
    def __init__(self, azure_application_vec: _Optional[_Iterable[_Union[_graph_pb2.AzureActiveDirectoryAppManifest, _Mapping]]] = ..., graph_base_result: _Optional[_Union[GraphBaseResult, _Mapping]] = ...) -> None: ...

class UpdateAzureApplicationsArg(_message.Message):
    __slots__ = ("azure_application_vec",)
    AZURE_APPLICATION_VEC_FIELD_NUMBER: _ClassVar[int]
    azure_application_vec: _containers.RepeatedCompositeFieldContainer[_graph_pb2.AzureActiveDirectoryAppManifest]
    def __init__(self, azure_application_vec: _Optional[_Iterable[_Union[_graph_pb2.AzureActiveDirectoryAppManifest, _Mapping]]] = ...) -> None: ...

class UpdateAzureApplicationsResult(_message.Message):
    __slots__ = ("graph_base_result",)
    GRAPH_BASE_RESULT_FIELD_NUMBER: _ClassVar[int]
    graph_base_result: GraphBaseResult
    def __init__(self, graph_base_result: _Optional[_Union[GraphBaseResult, _Mapping]] = ...) -> None: ...

class GetAppPermissionGrantsArg(_message.Message):
    __slots__ = ("service_principal_id", "app_id", "app_displayname")
    SERVICE_PRINCIPAL_ID_FIELD_NUMBER: _ClassVar[int]
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    APP_DISPLAYNAME_FIELD_NUMBER: _ClassVar[int]
    service_principal_id: str
    app_id: str
    app_displayname: str
    def __init__(self, service_principal_id: _Optional[str] = ..., app_id: _Optional[str] = ..., app_displayname: _Optional[str] = ...) -> None: ...

class GetAppPermissionGrantsResult(_message.Message):
    __slots__ = ("permission_grant_vec", "graph_base_result")
    PERMISSION_GRANT_VEC_FIELD_NUMBER: _ClassVar[int]
    GRAPH_BASE_RESULT_FIELD_NUMBER: _ClassVar[int]
    permission_grant_vec: _containers.RepeatedCompositeFieldContainer[_graph_pb2.OAuth2PermissionGrant]
    graph_base_result: GraphBaseResult
    def __init__(self, permission_grant_vec: _Optional[_Iterable[_Union[_graph_pb2.OAuth2PermissionGrant, _Mapping]]] = ..., graph_base_result: _Optional[_Union[GraphBaseResult, _Mapping]] = ...) -> None: ...

class GetAppRoleAssignmentsArg(_message.Message):
    __slots__ = ("service_principal_id", "app_id", "app_displayname")
    SERVICE_PRINCIPAL_ID_FIELD_NUMBER: _ClassVar[int]
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    APP_DISPLAYNAME_FIELD_NUMBER: _ClassVar[int]
    service_principal_id: str
    app_id: str
    app_displayname: str
    def __init__(self, service_principal_id: _Optional[str] = ..., app_id: _Optional[str] = ..., app_displayname: _Optional[str] = ...) -> None: ...

class GetAppRoleAssignmentsResult(_message.Message):
    __slots__ = ("app_role_vec", "graph_base_result")
    APP_ROLE_VEC_FIELD_NUMBER: _ClassVar[int]
    GRAPH_BASE_RESULT_FIELD_NUMBER: _ClassVar[int]
    app_role_vec: _containers.RepeatedCompositeFieldContainer[_graph_pb2.AppRoleAssignment]
    graph_base_result: GraphBaseResult
    def __init__(self, app_role_vec: _Optional[_Iterable[_Union[_graph_pb2.AppRoleAssignment, _Mapping]]] = ..., graph_base_result: _Optional[_Union[GraphBaseResult, _Mapping]] = ...) -> None: ...

class GetTokenArg(_message.Message):
    __slots__ = ("scope_DEPRECATED", "ms_graph_credentials")
    SCOPE_DEPRECATED_FIELD_NUMBER: _ClassVar[int]
    MS_GRAPH_CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    scope_DEPRECATED: str
    ms_graph_credentials: _credentials_pb2.MSGraphAppCredentials
    def __init__(self, scope_DEPRECATED: _Optional[str] = ..., ms_graph_credentials: _Optional[_Union[_credentials_pb2.MSGraphAppCredentials, _Mapping]] = ...) -> None: ...

class GetTokenResult(_message.Message):
    __slots__ = ("access_token", "graph_base_result", "token_error", "expiry_time_secs")
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    GRAPH_BASE_RESULT_FIELD_NUMBER: _ClassVar[int]
    TOKEN_ERROR_FIELD_NUMBER: _ClassVar[int]
    EXPIRY_TIME_SECS_FIELD_NUMBER: _ClassVar[int]
    access_token: str
    graph_base_result: GraphBaseResult
    token_error: _graph_pb2.AzureADSecurityTokenServiceError
    expiry_time_secs: int
    def __init__(self, access_token: _Optional[str] = ..., graph_base_result: _Optional[_Union[GraphBaseResult, _Mapping]] = ..., token_error: _Optional[_Union[_graph_pb2.AzureADSecurityTokenServiceError, _Mapping]] = ..., expiry_time_secs: _Optional[int] = ...) -> None: ...

class GetUsersArg(_message.Message):
    __slots__ = ("next_link", "user_id")
    NEXT_LINK_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    next_link: str
    user_id: str
    def __init__(self, next_link: _Optional[str] = ..., user_id: _Optional[str] = ...) -> None: ...

class GenericGetRequestArg(_message.Message):
    __slots__ = ("url", "next_link", "request_headers", "timeout_msecs", "retry_interval_msecs")
    class RequestHeadersEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    URL_FIELD_NUMBER: _ClassVar[int]
    NEXT_LINK_FIELD_NUMBER: _ClassVar[int]
    REQUEST_HEADERS_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_MSECS_FIELD_NUMBER: _ClassVar[int]
    RETRY_INTERVAL_MSECS_FIELD_NUMBER: _ClassVar[int]
    url: str
    next_link: str
    request_headers: _containers.ScalarMap[str, str]
    timeout_msecs: int
    retry_interval_msecs: int
    def __init__(self, url: _Optional[str] = ..., next_link: _Optional[str] = ..., request_headers: _Optional[_Mapping[str, str]] = ..., timeout_msecs: _Optional[int] = ..., retry_interval_msecs: _Optional[int] = ...) -> None: ...

class GetGroupsArg(_message.Message):
    __slots__ = ("next_link", "group_operation", "group_id", "is_security_group", "query_filter", "retry_get_group")
    class GroupOperation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kDefault: _ClassVar[GetGroupsArg.GroupOperation]
        kGroupDetails: _ClassVar[GetGroupsArg.GroupOperation]
    kDefault: GetGroupsArg.GroupOperation
    kGroupDetails: GetGroupsArg.GroupOperation
    NEXT_LINK_FIELD_NUMBER: _ClassVar[int]
    GROUP_OPERATION_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    IS_SECURITY_GROUP_FIELD_NUMBER: _ClassVar[int]
    QUERY_FILTER_FIELD_NUMBER: _ClassVar[int]
    RETRY_GET_GROUP_FIELD_NUMBER: _ClassVar[int]
    next_link: str
    group_operation: GetGroupsArg.GroupOperation
    group_id: str
    is_security_group: bool
    query_filter: str
    retry_get_group: bool
    def __init__(self, next_link: _Optional[str] = ..., group_operation: _Optional[_Union[GetGroupsArg.GroupOperation, str]] = ..., group_id: _Optional[str] = ..., is_security_group: bool = ..., query_filter: _Optional[str] = ..., retry_get_group: bool = ...) -> None: ...

class GetSitesArg(_message.Message):
    __slots__ = ("next_link", "site_operation", "discover_multi_geo_sites", "discoverable_multi_geo_region_codes_vec")
    class SiteOperation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kDefault: _ClassVar[GetSitesArg.SiteOperation]
        kRootSites: _ClassVar[GetSitesArg.SiteOperation]
        kSitesTree: _ClassVar[GetSitesArg.SiteOperation]
    kDefault: GetSitesArg.SiteOperation
    kRootSites: GetSitesArg.SiteOperation
    kSitesTree: GetSitesArg.SiteOperation
    NEXT_LINK_FIELD_NUMBER: _ClassVar[int]
    SITE_OPERATION_FIELD_NUMBER: _ClassVar[int]
    DISCOVER_MULTI_GEO_SITES_FIELD_NUMBER: _ClassVar[int]
    DISCOVERABLE_MULTI_GEO_REGION_CODES_VEC_FIELD_NUMBER: _ClassVar[int]
    next_link: str
    site_operation: GetSitesArg.SiteOperation
    discover_multi_geo_sites: bool
    discoverable_multi_geo_region_codes_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, next_link: _Optional[str] = ..., site_operation: _Optional[_Union[GetSitesArg.SiteOperation, str]] = ..., discover_multi_geo_sites: bool = ..., discoverable_multi_geo_region_codes_vec: _Optional[_Iterable[str]] = ...) -> None: ...

class GetUsersResult(_message.Message):
    __slots__ = ("user_vec", "next_link", "graph_base_result")
    USER_VEC_FIELD_NUMBER: _ClassVar[int]
    NEXT_LINK_FIELD_NUMBER: _ClassVar[int]
    GRAPH_BASE_RESULT_FIELD_NUMBER: _ClassVar[int]
    user_vec: _containers.RepeatedCompositeFieldContainer[_graph_pb2.User]
    next_link: str
    graph_base_result: GraphBaseResult
    def __init__(self, user_vec: _Optional[_Iterable[_Union[_graph_pb2.User, _Mapping]]] = ..., next_link: _Optional[str] = ..., graph_base_result: _Optional[_Union[GraphBaseResult, _Mapping]] = ...) -> None: ...

class GetGroupsResult(_message.Message):
    __slots__ = ("group_vec", "next_link", "graph_base_result")
    GROUP_VEC_FIELD_NUMBER: _ClassVar[int]
    NEXT_LINK_FIELD_NUMBER: _ClassVar[int]
    GRAPH_BASE_RESULT_FIELD_NUMBER: _ClassVar[int]
    group_vec: _containers.RepeatedCompositeFieldContainer[_graph_pb2.Group]
    next_link: str
    graph_base_result: GraphBaseResult
    def __init__(self, group_vec: _Optional[_Iterable[_Union[_graph_pb2.Group, _Mapping]]] = ..., next_link: _Optional[str] = ..., graph_base_result: _Optional[_Union[GraphBaseResult, _Mapping]] = ...) -> None: ...

class GetSitesResult(_message.Message):
    __slots__ = ("site_vec", "next_link", "graph_base_result", "warning_vec", "invalid_site_id_vec")
    SITE_VEC_FIELD_NUMBER: _ClassVar[int]
    NEXT_LINK_FIELD_NUMBER: _ClassVar[int]
    GRAPH_BASE_RESULT_FIELD_NUMBER: _ClassVar[int]
    WARNING_VEC_FIELD_NUMBER: _ClassVar[int]
    INVALID_SITE_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    site_vec: _containers.RepeatedCompositeFieldContainer[_graph_pb2.Site]
    next_link: str
    graph_base_result: GraphBaseResult
    warning_vec: _containers.RepeatedCompositeFieldContainer[_error_pb2.ErrorProto]
    invalid_site_id_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, site_vec: _Optional[_Iterable[_Union[_graph_pb2.Site, _Mapping]]] = ..., next_link: _Optional[str] = ..., graph_base_result: _Optional[_Union[GraphBaseResult, _Mapping]] = ..., warning_vec: _Optional[_Iterable[_Union[_error_pb2.ErrorProto, _Mapping]]] = ..., invalid_site_id_vec: _Optional[_Iterable[str]] = ...) -> None: ...

class GetAllEntitiesArg(_message.Message):
    __slots__ = ("entity_type_vec", "site_discovery_option", "discover_multi_geo_sites", "discoverable_multi_geo_region_codes_vec")
    ENTITY_TYPE_VEC_FIELD_NUMBER: _ClassVar[int]
    SITE_DISCOVERY_OPTION_FIELD_NUMBER: _ClassVar[int]
    DISCOVER_MULTI_GEO_SITES_FIELD_NUMBER: _ClassVar[int]
    DISCOVERABLE_MULTI_GEO_REGION_CODES_VEC_FIELD_NUMBER: _ClassVar[int]
    entity_type_vec: _containers.RepeatedScalarFieldContainer[_graph_pb2.EntityType.Type]
    site_discovery_option: GetSitesArg.SiteOperation
    discover_multi_geo_sites: bool
    discoverable_multi_geo_region_codes_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, entity_type_vec: _Optional[_Iterable[_Union[_graph_pb2.EntityType.Type, str]]] = ..., site_discovery_option: _Optional[_Union[GetSitesArg.SiteOperation, str]] = ..., discover_multi_geo_sites: bool = ..., discoverable_multi_geo_region_codes_vec: _Optional[_Iterable[str]] = ...) -> None: ...

class GetAllEntitiesResult(_message.Message):
    __slots__ = ("users", "groups", "sites", "graph_base_result")
    USERS_FIELD_NUMBER: _ClassVar[int]
    GROUPS_FIELD_NUMBER: _ClassVar[int]
    SITES_FIELD_NUMBER: _ClassVar[int]
    GRAPH_BASE_RESULT_FIELD_NUMBER: _ClassVar[int]
    users: GetUsersResult
    groups: GetGroupsResult
    sites: GetSitesResult
    graph_base_result: GraphBaseResult
    def __init__(self, users: _Optional[_Union[GetUsersResult, _Mapping]] = ..., groups: _Optional[_Union[GetGroupsResult, _Mapping]] = ..., sites: _Optional[_Union[GetSitesResult, _Mapping]] = ..., graph_base_result: _Optional[_Union[GraphBaseResult, _Mapping]] = ...) -> None: ...

class GetEntityDrivesArg(_message.Message):
    __slots__ = ("user_id", "group_id", "site_id", "entity_type", "fetch_default_drive", "fetch_phl_drive")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    SITE_ID_FIELD_NUMBER: _ClassVar[int]
    ENTITY_TYPE_FIELD_NUMBER: _ClassVar[int]
    FETCH_DEFAULT_DRIVE_FIELD_NUMBER: _ClassVar[int]
    FETCH_PHL_DRIVE_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    group_id: str
    site_id: str
    entity_type: _graph_pb2.EntityType.Type
    fetch_default_drive: bool
    fetch_phl_drive: bool
    def __init__(self, user_id: _Optional[str] = ..., group_id: _Optional[str] = ..., site_id: _Optional[str] = ..., entity_type: _Optional[_Union[_graph_pb2.EntityType.Type, str]] = ..., fetch_default_drive: bool = ..., fetch_phl_drive: bool = ...) -> None: ...

class GetEntityDrivesResult(_message.Message):
    __slots__ = ("drive_list", "graph_error", "graph_base_result")
    DRIVE_LIST_FIELD_NUMBER: _ClassVar[int]
    GRAPH_ERROR_FIELD_NUMBER: _ClassVar[int]
    GRAPH_BASE_RESULT_FIELD_NUMBER: _ClassVar[int]
    drive_list: _containers.RepeatedCompositeFieldContainer[_graph_pb2.Drive]
    graph_error: _graph_pb2.GraphError
    graph_base_result: GraphBaseResult
    def __init__(self, drive_list: _Optional[_Iterable[_Union[_graph_pb2.Drive, _Mapping]]] = ..., graph_error: _Optional[_Union[_graph_pb2.GraphError, _Mapping]] = ..., graph_base_result: _Optional[_Union[GraphBaseResult, _Mapping]] = ...) -> None: ...

class GetDriveDeltaArg(_message.Message):
    __slots__ = ("drive_id", "delta_link", "max_pages_to_fetch", "fetch_changes_in_pages", "page_size", "prefer_permissions_hierarchial_sharing", "fetch_doc_lib_size_only", "base_arg")
    DRIVE_ID_FIELD_NUMBER: _ClassVar[int]
    DELTA_LINK_FIELD_NUMBER: _ClassVar[int]
    MAX_PAGES_TO_FETCH_FIELD_NUMBER: _ClassVar[int]
    FETCH_CHANGES_IN_PAGES_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PREFER_PERMISSIONS_HIERARCHIAL_SHARING_FIELD_NUMBER: _ClassVar[int]
    FETCH_DOC_LIB_SIZE_ONLY_FIELD_NUMBER: _ClassVar[int]
    BASE_ARG_FIELD_NUMBER: _ClassVar[int]
    drive_id: str
    delta_link: str
    max_pages_to_fetch: int
    fetch_changes_in_pages: bool
    page_size: int
    prefer_permissions_hierarchial_sharing: bool
    fetch_doc_lib_size_only: bool
    base_arg: GraphBaseArg
    def __init__(self, drive_id: _Optional[str] = ..., delta_link: _Optional[str] = ..., max_pages_to_fetch: _Optional[int] = ..., fetch_changes_in_pages: bool = ..., page_size: _Optional[int] = ..., prefer_permissions_hierarchial_sharing: bool = ..., fetch_doc_lib_size_only: bool = ..., base_arg: _Optional[_Union[GraphBaseArg, _Mapping]] = ...) -> None: ...

class GetDriveDeltaResult(_message.Message):
    __slots__ = ("delta_link", "drive_items", "next_link", "o365_error_proto", "graph_base_result")
    DELTA_LINK_FIELD_NUMBER: _ClassVar[int]
    DRIVE_ITEMS_FIELD_NUMBER: _ClassVar[int]
    NEXT_LINK_FIELD_NUMBER: _ClassVar[int]
    O365_ERROR_PROTO_FIELD_NUMBER: _ClassVar[int]
    GRAPH_BASE_RESULT_FIELD_NUMBER: _ClassVar[int]
    delta_link: str
    drive_items: _containers.RepeatedCompositeFieldContainer[_graph_pb2.DriveItem]
    next_link: str
    o365_error_proto: _o365_error_pb2.O365ErrorProto
    graph_base_result: GraphBaseResult
    def __init__(self, delta_link: _Optional[str] = ..., drive_items: _Optional[_Iterable[_Union[_graph_pb2.DriveItem, _Mapping]]] = ..., next_link: _Optional[str] = ..., o365_error_proto: _Optional[_Union[_o365_error_pb2.O365ErrorProto, _Mapping]] = ..., graph_base_result: _Optional[_Union[GraphBaseResult, _Mapping]] = ...) -> None: ...

class GetItemPermissionsArg(_message.Message):
    __slots__ = ("drive_id", "item_id", "drive_item_type", "base_arg")
    DRIVE_ID_FIELD_NUMBER: _ClassVar[int]
    ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    DRIVE_ITEM_TYPE_FIELD_NUMBER: _ClassVar[int]
    BASE_ARG_FIELD_NUMBER: _ClassVar[int]
    drive_id: str
    item_id: str
    drive_item_type: _graph_pb2.DriveItemType.Type
    base_arg: GraphBaseArg
    def __init__(self, drive_id: _Optional[str] = ..., item_id: _Optional[str] = ..., drive_item_type: _Optional[_Union[_graph_pb2.DriveItemType.Type, str]] = ..., base_arg: _Optional[_Union[GraphBaseArg, _Mapping]] = ...) -> None: ...

class GetItemPermissionsResult(_message.Message):
    __slots__ = ("permissions", "graph_base_result", "graph_error")
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    GRAPH_BASE_RESULT_FIELD_NUMBER: _ClassVar[int]
    GRAPH_ERROR_FIELD_NUMBER: _ClassVar[int]
    permissions: _containers.RepeatedCompositeFieldContainer[_graph_pb2.Permissions]
    graph_base_result: GraphBaseResult
    graph_error: _graph_pb2.GraphError
    def __init__(self, permissions: _Optional[_Iterable[_Union[_graph_pb2.Permissions, _Mapping]]] = ..., graph_base_result: _Optional[_Union[GraphBaseResult, _Mapping]] = ..., graph_error: _Optional[_Union[_graph_pb2.GraphError, _Mapping]] = ...) -> None: ...

class GetItemArg(_message.Message):
    __slots__ = ("drive_id", "item_id", "get_only_ctag")
    DRIVE_ID_FIELD_NUMBER: _ClassVar[int]
    ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    GET_ONLY_CTAG_FIELD_NUMBER: _ClassVar[int]
    drive_id: str
    item_id: str
    get_only_ctag: bool
    def __init__(self, drive_id: _Optional[str] = ..., item_id: _Optional[str] = ..., get_only_ctag: bool = ...) -> None: ...

class GetItemResult(_message.Message):
    __slots__ = ("drive_item", "graph_base_result")
    DRIVE_ITEM_FIELD_NUMBER: _ClassVar[int]
    GRAPH_BASE_RESULT_FIELD_NUMBER: _ClassVar[int]
    drive_item: _graph_pb2.DriveItem
    graph_base_result: GraphBaseResult
    def __init__(self, drive_item: _Optional[_Union[_graph_pb2.DriveItem, _Mapping]] = ..., graph_base_result: _Optional[_Union[GraphBaseResult, _Mapping]] = ...) -> None: ...

class GetFileContentPartialArg(_message.Message):
    __slots__ = ("drive_id", "item_id", "offset", "length", "download_url", "size", "base_arg")
    DRIVE_ID_FIELD_NUMBER: _ClassVar[int]
    ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_URL_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    BASE_ARG_FIELD_NUMBER: _ClassVar[int]
    drive_id: str
    item_id: str
    offset: int
    length: int
    download_url: str
    size: int
    base_arg: GraphBaseArg
    def __init__(self, drive_id: _Optional[str] = ..., item_id: _Optional[str] = ..., offset: _Optional[int] = ..., length: _Optional[int] = ..., download_url: _Optional[str] = ..., size: _Optional[int] = ..., base_arg: _Optional[_Union[GraphBaseArg, _Mapping]] = ...) -> None: ...

class GetFileContentPartialResult(_message.Message):
    __slots__ = ("content", "request_throttled", "graph_base_result", "o365_error_proto", "dead_time_info")
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    REQUEST_THROTTLED_FIELD_NUMBER: _ClassVar[int]
    GRAPH_BASE_RESULT_FIELD_NUMBER: _ClassVar[int]
    O365_ERROR_PROTO_FIELD_NUMBER: _ClassVar[int]
    DEAD_TIME_INFO_FIELD_NUMBER: _ClassVar[int]
    content: bytes
    request_throttled: bool
    graph_base_result: GraphBaseResult
    o365_error_proto: _o365_error_pb2.O365ErrorProto
    dead_time_info: _graph_pb2.DeadTimeInfo
    def __init__(self, content: _Optional[bytes] = ..., request_throttled: bool = ..., graph_base_result: _Optional[_Union[GraphBaseResult, _Mapping]] = ..., o365_error_proto: _Optional[_Union[_o365_error_pb2.O365ErrorProto, _Mapping]] = ..., dead_time_info: _Optional[_Union[_graph_pb2.DeadTimeInfo, _Mapping]] = ...) -> None: ...

class GetFileContentArg(_message.Message):
    __slots__ = ("drive_id", "item_id", "size", "base_arg")
    DRIVE_ID_FIELD_NUMBER: _ClassVar[int]
    ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    BASE_ARG_FIELD_NUMBER: _ClassVar[int]
    drive_id: str
    item_id: str
    size: int
    base_arg: GraphBaseArg
    def __init__(self, drive_id: _Optional[str] = ..., item_id: _Optional[str] = ..., size: _Optional[int] = ..., base_arg: _Optional[_Union[GraphBaseArg, _Mapping]] = ...) -> None: ...

class GetFileContentResult(_message.Message):
    __slots__ = ("content", "request_throttled", "graph_base_result", "o365_error_proto", "dead_time_info")
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    REQUEST_THROTTLED_FIELD_NUMBER: _ClassVar[int]
    GRAPH_BASE_RESULT_FIELD_NUMBER: _ClassVar[int]
    O365_ERROR_PROTO_FIELD_NUMBER: _ClassVar[int]
    DEAD_TIME_INFO_FIELD_NUMBER: _ClassVar[int]
    content: bytes
    request_throttled: bool
    graph_base_result: GraphBaseResult
    o365_error_proto: _o365_error_pb2.O365ErrorProto
    dead_time_info: _graph_pb2.DeadTimeInfo
    def __init__(self, content: _Optional[bytes] = ..., request_throttled: bool = ..., graph_base_result: _Optional[_Union[GraphBaseResult, _Mapping]] = ..., o365_error_proto: _Optional[_Union[_o365_error_pb2.O365ErrorProto, _Mapping]] = ..., dead_time_info: _Optional[_Union[_graph_pb2.DeadTimeInfo, _Mapping]] = ...) -> None: ...

class GenericBatchRequestBody(_message.Message):
    __slots__ = ("display_name", "list_info", "description", "odata_type", "membership_type", "members")
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    LIST_INFO_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ODATA_TYPE_FIELD_NUMBER: _ClassVar[int]
    MEMBERSHIP_TYPE_FIELD_NUMBER: _ClassVar[int]
    MEMBERS_FIELD_NUMBER: _ClassVar[int]
    display_name: str
    list_info: _graph_pb2.ListInfo
    description: str
    odata_type: str
    membership_type: str
    members: _containers.RepeatedCompositeFieldContainer[_graph_pb2.ChannelMemberInfo]
    def __init__(self, display_name: _Optional[str] = ..., list_info: _Optional[_Union[_graph_pb2.ListInfo, _Mapping]] = ..., description: _Optional[str] = ..., odata_type: _Optional[str] = ..., membership_type: _Optional[str] = ..., members: _Optional[_Iterable[_Union[_graph_pb2.ChannelMemberInfo, _Mapping]]] = ...) -> None: ...

class GenericBatchRequestHeader(_message.Message):
    __slots__ = ("content_type", "consistency_level")
    CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    CONSISTENCY_LEVEL_FIELD_NUMBER: _ClassVar[int]
    content_type: str
    consistency_level: str
    def __init__(self, content_type: _Optional[str] = ..., consistency_level: _Optional[str] = ...) -> None: ...

class Request(_message.Message):
    __slots__ = ("id", "method", "url", "request_body", "individual_request_header", "depends_on")
    ID_FIELD_NUMBER: _ClassVar[int]
    METHOD_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    REQUEST_BODY_FIELD_NUMBER: _ClassVar[int]
    INDIVIDUAL_REQUEST_HEADER_FIELD_NUMBER: _ClassVar[int]
    DEPENDS_ON_FIELD_NUMBER: _ClassVar[int]
    id: str
    method: str
    url: str
    request_body: GenericBatchRequestBody
    individual_request_header: GenericBatchRequestHeader
    depends_on: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, id: _Optional[str] = ..., method: _Optional[str] = ..., url: _Optional[str] = ..., request_body: _Optional[_Union[GenericBatchRequestBody, _Mapping]] = ..., individual_request_header: _Optional[_Union[GenericBatchRequestHeader, _Mapping]] = ..., depends_on: _Optional[_Iterable[str]] = ...) -> None: ...

class BatchRequest(_message.Message):
    __slots__ = ("request_vec",)
    REQUEST_VEC_FIELD_NUMBER: _ClassVar[int]
    request_vec: _containers.RepeatedCompositeFieldContainer[Request]
    def __init__(self, request_vec: _Optional[_Iterable[_Union[Request, _Mapping]]] = ...) -> None: ...

class ResponseHeaders(_message.Message):
    __slots__ = ("location", "retry_after_in_secs", "throttle_scope", "throttle_reason")
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    RETRY_AFTER_IN_SECS_FIELD_NUMBER: _ClassVar[int]
    THROTTLE_SCOPE_FIELD_NUMBER: _ClassVar[int]
    THROTTLE_REASON_FIELD_NUMBER: _ClassVar[int]
    location: str
    retry_after_in_secs: str
    throttle_scope: str
    throttle_reason: str
    def __init__(self, location: _Optional[str] = ..., retry_after_in_secs: _Optional[str] = ..., throttle_scope: _Optional[str] = ..., throttle_reason: _Optional[str] = ...) -> None: ...

class ResponseBody(_message.Message):
    __slots__ = ("permissions", "size", "parent_reference", "id", "name", "web_url", "display_name", "list_info", "error", "num_members", "membership_type")
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    PARENT_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    WEB_URL_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    LIST_INFO_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    NUM_MEMBERS_FIELD_NUMBER: _ClassVar[int]
    MEMBERSHIP_TYPE_FIELD_NUMBER: _ClassVar[int]
    permissions: _containers.RepeatedCompositeFieldContainer[_graph_pb2.Permissions]
    size: int
    parent_reference: _graph_pb2.ItemReference
    id: str
    name: str
    web_url: str
    display_name: str
    list_info: _graph_pb2.ListInfo
    error: _graph_pb2.GraphError
    num_members: int
    membership_type: str
    def __init__(self, permissions: _Optional[_Iterable[_Union[_graph_pb2.Permissions, _Mapping]]] = ..., size: _Optional[int] = ..., parent_reference: _Optional[_Union[_graph_pb2.ItemReference, _Mapping]] = ..., id: _Optional[str] = ..., name: _Optional[str] = ..., web_url: _Optional[str] = ..., display_name: _Optional[str] = ..., list_info: _Optional[_Union[_graph_pb2.ListInfo, _Mapping]] = ..., error: _Optional[_Union[_graph_pb2.GraphError, _Mapping]] = ..., num_members: _Optional[int] = ..., membership_type: _Optional[str] = ...) -> None: ...

class Response(_message.Message):
    __slots__ = ("id", "status", "headers", "body")
    ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    HEADERS_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    id: str
    status: int
    headers: ResponseHeaders
    body: ResponseBody
    def __init__(self, id: _Optional[str] = ..., status: _Optional[int] = ..., headers: _Optional[_Union[ResponseHeaders, _Mapping]] = ..., body: _Optional[_Union[ResponseBody, _Mapping]] = ...) -> None: ...

class GenericBatchResponse(_message.Message):
    __slots__ = ("id", "status", "headers", "body")
    ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    HEADERS_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    id: str
    status: int
    headers: ResponseHeaders
    body: GenericBatchResponseBody
    def __init__(self, id: _Optional[str] = ..., status: _Optional[int] = ..., headers: _Optional[_Union[ResponseHeaders, _Mapping]] = ..., body: _Optional[_Union[GenericBatchResponseBody, _Mapping]] = ...) -> None: ...

class GenericBatchResponseBody(_message.Message):
    __slots__ = ("size", "parent_reference", "id", "name", "web_url", "display_name", "list_info", "error", "num_members", "membership_type", "sub_site_vec", "next_link", "site_drive_vec", "provisioned_plans", "assigned_plans", "mail", "count", "account_enabled")
    SIZE_FIELD_NUMBER: _ClassVar[int]
    PARENT_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    WEB_URL_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    LIST_INFO_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    NUM_MEMBERS_FIELD_NUMBER: _ClassVar[int]
    MEMBERSHIP_TYPE_FIELD_NUMBER: _ClassVar[int]
    SUB_SITE_VEC_FIELD_NUMBER: _ClassVar[int]
    NEXT_LINK_FIELD_NUMBER: _ClassVar[int]
    SITE_DRIVE_VEC_FIELD_NUMBER: _ClassVar[int]
    PROVISIONED_PLANS_FIELD_NUMBER: _ClassVar[int]
    ASSIGNED_PLANS_FIELD_NUMBER: _ClassVar[int]
    MAIL_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ENABLED_FIELD_NUMBER: _ClassVar[int]
    size: int
    parent_reference: _graph_pb2.ItemReference
    id: str
    name: str
    web_url: str
    display_name: str
    list_info: _graph_pb2.ListInfo
    error: _graph_pb2.GraphError
    num_members: int
    membership_type: str
    sub_site_vec: _containers.RepeatedCompositeFieldContainer[_graph_pb2.Site]
    next_link: str
    site_drive_vec: _containers.RepeatedCompositeFieldContainer[_graph_pb2.SiteDrive]
    provisioned_plans: _containers.RepeatedCompositeFieldContainer[_graph_pb2.ProvisionedPlan]
    assigned_plans: _containers.RepeatedCompositeFieldContainer[_graph_pb2.AssignedPlan]
    mail: str
    count: int
    account_enabled: bool
    def __init__(self, size: _Optional[int] = ..., parent_reference: _Optional[_Union[_graph_pb2.ItemReference, _Mapping]] = ..., id: _Optional[str] = ..., name: _Optional[str] = ..., web_url: _Optional[str] = ..., display_name: _Optional[str] = ..., list_info: _Optional[_Union[_graph_pb2.ListInfo, _Mapping]] = ..., error: _Optional[_Union[_graph_pb2.GraphError, _Mapping]] = ..., num_members: _Optional[int] = ..., membership_type: _Optional[str] = ..., sub_site_vec: _Optional[_Iterable[_Union[_graph_pb2.Site, _Mapping]]] = ..., next_link: _Optional[str] = ..., site_drive_vec: _Optional[_Iterable[_Union[_graph_pb2.SiteDrive, _Mapping]]] = ..., provisioned_plans: _Optional[_Iterable[_Union[_graph_pb2.ProvisionedPlan, _Mapping]]] = ..., assigned_plans: _Optional[_Iterable[_Union[_graph_pb2.AssignedPlan, _Mapping]]] = ..., mail: _Optional[str] = ..., count: _Optional[int] = ..., account_enabled: bool = ...) -> None: ...

class ResponseGetMemberCount(_message.Message):
    __slots__ = ("id", "status", "headers", "body")
    ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    HEADERS_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    id: str
    status: int
    headers: ResponseHeaders
    body: int
    def __init__(self, id: _Optional[str] = ..., status: _Optional[int] = ..., headers: _Optional[_Union[ResponseHeaders, _Mapping]] = ..., body: _Optional[int] = ...) -> None: ...

class ResponseGetSiteDrives(_message.Message):
    __slots__ = ("id", "status", "headers", "body")
    ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    HEADERS_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    id: str
    status: int
    headers: ResponseHeaders
    body: SiteDrivesBatch
    def __init__(self, id: _Optional[str] = ..., status: _Optional[int] = ..., headers: _Optional[_Union[ResponseHeaders, _Mapping]] = ..., body: _Optional[_Union[SiteDrivesBatch, _Mapping]] = ...) -> None: ...

class SiteDrivesBatch(_message.Message):
    __slots__ = ("site_drive_vec", "error")
    SITE_DRIVE_VEC_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    site_drive_vec: _containers.RepeatedCompositeFieldContainer[_graph_pb2.SiteDrive]
    error: _graph_pb2.GraphError
    def __init__(self, site_drive_vec: _Optional[_Iterable[_Union[_graph_pb2.SiteDrive, _Mapping]]] = ..., error: _Optional[_Union[_graph_pb2.GraphError, _Mapping]] = ...) -> None: ...

class BatchRequestResult(_message.Message):
    __slots__ = ("responses", "next_link", "graph_base_result")
    RESPONSES_FIELD_NUMBER: _ClassVar[int]
    NEXT_LINK_FIELD_NUMBER: _ClassVar[int]
    GRAPH_BASE_RESULT_FIELD_NUMBER: _ClassVar[int]
    responses: _containers.RepeatedCompositeFieldContainer[Response]
    next_link: str
    graph_base_result: GraphBaseResult
    def __init__(self, responses: _Optional[_Iterable[_Union[Response, _Mapping]]] = ..., next_link: _Optional[str] = ..., graph_base_result: _Optional[_Union[GraphBaseResult, _Mapping]] = ...) -> None: ...

class GenericBatchRequestResult(_message.Message):
    __slots__ = ("responses", "graph_base_result", "batch_count_response")
    RESPONSES_FIELD_NUMBER: _ClassVar[int]
    GRAPH_BASE_RESULT_FIELD_NUMBER: _ClassVar[int]
    BATCH_COUNT_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    responses: _containers.RepeatedCompositeFieldContainer[GenericBatchResponse]
    graph_base_result: GraphBaseResult
    batch_count_response: GenericBatchGetMemberCountResult
    def __init__(self, responses: _Optional[_Iterable[_Union[GenericBatchResponse, _Mapping]]] = ..., graph_base_result: _Optional[_Union[GraphBaseResult, _Mapping]] = ..., batch_count_response: _Optional[_Union[GenericBatchGetMemberCountResult, _Mapping]] = ...) -> None: ...

class GenericBatchGetMemberCountResult(_message.Message):
    __slots__ = ("responses",)
    RESPONSES_FIELD_NUMBER: _ClassVar[int]
    responses: _containers.RepeatedCompositeFieldContainer[ResponseGetMemberCount]
    def __init__(self, responses: _Optional[_Iterable[_Union[ResponseGetMemberCount, _Mapping]]] = ...) -> None: ...

class GenericBatchGetSiteDrives(_message.Message):
    __slots__ = ("responses",)
    RESPONSES_FIELD_NUMBER: _ClassVar[int]
    responses: _containers.RepeatedCompositeFieldContainer[ResponseGetSiteDrives]
    def __init__(self, responses: _Optional[_Iterable[_Union[ResponseGetSiteDrives, _Mapping]]] = ...) -> None: ...

class BatchRequestArg(_message.Message):
    __slots__ = ("drive_id", "item_id_vec", "method", "request_type", "next_link", "ignore_throttled_requests", "serialize_requests")
    DRIVE_ID_FIELD_NUMBER: _ClassVar[int]
    ITEM_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    METHOD_FIELD_NUMBER: _ClassVar[int]
    REQUEST_TYPE_FIELD_NUMBER: _ClassVar[int]
    NEXT_LINK_FIELD_NUMBER: _ClassVar[int]
    IGNORE_THROTTLED_REQUESTS_FIELD_NUMBER: _ClassVar[int]
    SERIALIZE_REQUESTS_FIELD_NUMBER: _ClassVar[int]
    drive_id: str
    item_id_vec: _containers.RepeatedScalarFieldContainer[str]
    method: str
    request_type: str
    next_link: str
    ignore_throttled_requests: bool
    serialize_requests: bool
    def __init__(self, drive_id: _Optional[str] = ..., item_id_vec: _Optional[_Iterable[str]] = ..., method: _Optional[str] = ..., request_type: _Optional[str] = ..., next_link: _Optional[str] = ..., ignore_throttled_requests: bool = ..., serialize_requests: bool = ...) -> None: ...

class GenericBatchRequestArg(_message.Message):
    __slots__ = ("url_str_vec", "method_str_vec", "tag_id_vec", "request_header_vec", "body_vec", "count", "use_beta_url", "ignore_throttled_requests", "fetch_site_drives", "description")
    URL_STR_VEC_FIELD_NUMBER: _ClassVar[int]
    METHOD_STR_VEC_FIELD_NUMBER: _ClassVar[int]
    TAG_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    REQUEST_HEADER_VEC_FIELD_NUMBER: _ClassVar[int]
    BODY_VEC_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    USE_BETA_URL_FIELD_NUMBER: _ClassVar[int]
    IGNORE_THROTTLED_REQUESTS_FIELD_NUMBER: _ClassVar[int]
    FETCH_SITE_DRIVES_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    url_str_vec: _containers.RepeatedScalarFieldContainer[str]
    method_str_vec: _containers.RepeatedScalarFieldContainer[str]
    tag_id_vec: _containers.RepeatedScalarFieldContainer[str]
    request_header_vec: _containers.RepeatedCompositeFieldContainer[GenericBatchRequestHeader]
    body_vec: _containers.RepeatedCompositeFieldContainer[GenericBatchRequestBody]
    count: bool
    use_beta_url: bool
    ignore_throttled_requests: bool
    fetch_site_drives: bool
    description: str
    def __init__(self, url_str_vec: _Optional[_Iterable[str]] = ..., method_str_vec: _Optional[_Iterable[str]] = ..., tag_id_vec: _Optional[_Iterable[str]] = ..., request_header_vec: _Optional[_Iterable[_Union[GenericBatchRequestHeader, _Mapping]]] = ..., body_vec: _Optional[_Iterable[_Union[GenericBatchRequestBody, _Mapping]]] = ..., count: bool = ..., use_beta_url: bool = ..., ignore_throttled_requests: bool = ..., fetch_site_drives: bool = ..., description: _Optional[str] = ...) -> None: ...

class CreateFolderArg(_message.Message):
    __slots__ = ("drive_id", "parent_item_path", "request_folder_item", "should_create_parents")
    DRIVE_ID_FIELD_NUMBER: _ClassVar[int]
    PARENT_ITEM_PATH_FIELD_NUMBER: _ClassVar[int]
    REQUEST_FOLDER_ITEM_FIELD_NUMBER: _ClassVar[int]
    SHOULD_CREATE_PARENTS_FIELD_NUMBER: _ClassVar[int]
    drive_id: str
    parent_item_path: str
    request_folder_item: _graph_pb2.DriveItem
    should_create_parents: bool
    def __init__(self, drive_id: _Optional[str] = ..., parent_item_path: _Optional[str] = ..., request_folder_item: _Optional[_Union[_graph_pb2.DriveItem, _Mapping]] = ..., should_create_parents: bool = ...) -> None: ...

class CreateFolderResult(_message.Message):
    __slots__ = ("response_folder_item", "graph_base_result", "o365_error_proto")
    RESPONSE_FOLDER_ITEM_FIELD_NUMBER: _ClassVar[int]
    GRAPH_BASE_RESULT_FIELD_NUMBER: _ClassVar[int]
    O365_ERROR_PROTO_FIELD_NUMBER: _ClassVar[int]
    response_folder_item: _graph_pb2.DriveItem
    graph_base_result: GraphBaseResult
    o365_error_proto: _o365_error_pb2.O365ErrorProto
    def __init__(self, response_folder_item: _Optional[_Union[_graph_pb2.DriveItem, _Mapping]] = ..., graph_base_result: _Optional[_Union[GraphBaseResult, _Mapping]] = ..., o365_error_proto: _Optional[_Union[_o365_error_pb2.O365ErrorProto, _Mapping]] = ...) -> None: ...

class CreateGroupArg(_message.Message):
    __slots__ = ("display_name", "description", "mail_enabled", "mail_nickname", "security_enabled", "visibility", "group_type_vec", "users_list", "theme", "membership_rule", "membership_rule_processing_state")
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    MAIL_ENABLED_FIELD_NUMBER: _ClassVar[int]
    MAIL_NICKNAME_FIELD_NUMBER: _ClassVar[int]
    SECURITY_ENABLED_FIELD_NUMBER: _ClassVar[int]
    VISIBILITY_FIELD_NUMBER: _ClassVar[int]
    GROUP_TYPE_VEC_FIELD_NUMBER: _ClassVar[int]
    USERS_LIST_FIELD_NUMBER: _ClassVar[int]
    THEME_FIELD_NUMBER: _ClassVar[int]
    MEMBERSHIP_RULE_FIELD_NUMBER: _ClassVar[int]
    MEMBERSHIP_RULE_PROCESSING_STATE_FIELD_NUMBER: _ClassVar[int]
    display_name: str
    description: str
    mail_enabled: bool
    mail_nickname: str
    security_enabled: bool
    visibility: str
    group_type_vec: _containers.RepeatedScalarFieldContainer[str]
    users_list: _graph_pb2.UsersList
    theme: str
    membership_rule: str
    membership_rule_processing_state: str
    def __init__(self, display_name: _Optional[str] = ..., description: _Optional[str] = ..., mail_enabled: bool = ..., mail_nickname: _Optional[str] = ..., security_enabled: bool = ..., visibility: _Optional[str] = ..., group_type_vec: _Optional[_Iterable[str]] = ..., users_list: _Optional[_Union[_graph_pb2.UsersList, _Mapping]] = ..., theme: _Optional[str] = ..., membership_rule: _Optional[str] = ..., membership_rule_processing_state: _Optional[str] = ...) -> None: ...

class CreateGroupResult(_message.Message):
    __slots__ = ("group", "graph_error", "graph_base_result")
    GROUP_FIELD_NUMBER: _ClassVar[int]
    GRAPH_ERROR_FIELD_NUMBER: _ClassVar[int]
    GRAPH_BASE_RESULT_FIELD_NUMBER: _ClassVar[int]
    group: _graph_pb2.Group
    graph_error: _graph_pb2.GraphError
    graph_base_result: GraphBaseResult
    def __init__(self, group: _Optional[_Union[_graph_pb2.Group, _Mapping]] = ..., graph_error: _Optional[_Union[_graph_pb2.GraphError, _Mapping]] = ..., graph_base_result: _Optional[_Union[GraphBaseResult, _Mapping]] = ...) -> None: ...

class CreateUploadSessionArg(_message.Message):
    __slots__ = ("drive_id", "file_path", "upload_folder_item")
    DRIVE_ID_FIELD_NUMBER: _ClassVar[int]
    FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    UPLOAD_FOLDER_ITEM_FIELD_NUMBER: _ClassVar[int]
    drive_id: str
    file_path: str
    upload_folder_item: _graph_pb2.DriveItem
    def __init__(self, drive_id: _Optional[str] = ..., file_path: _Optional[str] = ..., upload_folder_item: _Optional[_Union[_graph_pb2.DriveItem, _Mapping]] = ...) -> None: ...

class CreateUploadSessionResult(_message.Message):
    __slots__ = ("upload_session", "graph_base_result", "o365_error_proto")
    UPLOAD_SESSION_FIELD_NUMBER: _ClassVar[int]
    GRAPH_BASE_RESULT_FIELD_NUMBER: _ClassVar[int]
    O365_ERROR_PROTO_FIELD_NUMBER: _ClassVar[int]
    upload_session: _graph_pb2.UploadSession
    graph_base_result: GraphBaseResult
    o365_error_proto: _o365_error_pb2.O365ErrorProto
    def __init__(self, upload_session: _Optional[_Union[_graph_pb2.UploadSession, _Mapping]] = ..., graph_base_result: _Optional[_Union[GraphBaseResult, _Mapping]] = ..., o365_error_proto: _Optional[_Union[_o365_error_pb2.O365ErrorProto, _Mapping]] = ...) -> None: ...

class PutFileContentPartialArg(_message.Message):
    __slots__ = ("upload_url", "offset", "length", "total_length", "content")
    UPLOAD_URL_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    TOTAL_LENGTH_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    upload_url: str
    offset: int
    length: int
    total_length: int
    content: _graph_pb2.FileContent
    def __init__(self, upload_url: _Optional[str] = ..., offset: _Optional[int] = ..., length: _Optional[int] = ..., total_length: _Optional[int] = ..., content: _Optional[_Union[_graph_pb2.FileContent, _Mapping]] = ...) -> None: ...

class PutFileContentPartialResult(_message.Message):
    __slots__ = ("upload_session", "uploaded_drive_item", "graph_base_result", "o365_error_proto")
    UPLOAD_SESSION_FIELD_NUMBER: _ClassVar[int]
    UPLOADED_DRIVE_ITEM_FIELD_NUMBER: _ClassVar[int]
    GRAPH_BASE_RESULT_FIELD_NUMBER: _ClassVar[int]
    O365_ERROR_PROTO_FIELD_NUMBER: _ClassVar[int]
    upload_session: _graph_pb2.UploadSession
    uploaded_drive_item: _graph_pb2.DriveItem
    graph_base_result: GraphBaseResult
    o365_error_proto: _o365_error_pb2.O365ErrorProto
    def __init__(self, upload_session: _Optional[_Union[_graph_pb2.UploadSession, _Mapping]] = ..., uploaded_drive_item: _Optional[_Union[_graph_pb2.DriveItem, _Mapping]] = ..., graph_base_result: _Optional[_Union[GraphBaseResult, _Mapping]] = ..., o365_error_proto: _Optional[_Union[_o365_error_pb2.O365ErrorProto, _Mapping]] = ...) -> None: ...

class PutFileContentArg(_message.Message):
    __slots__ = ("drive_id", "file_path", "content")
    DRIVE_ID_FIELD_NUMBER: _ClassVar[int]
    FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    drive_id: str
    file_path: str
    content: _graph_pb2.FileContent
    def __init__(self, drive_id: _Optional[str] = ..., file_path: _Optional[str] = ..., content: _Optional[_Union[_graph_pb2.FileContent, _Mapping]] = ...) -> None: ...

class PutFileContentResult(_message.Message):
    __slots__ = ("uploaded_drive_item", "graph_base_result", "o365_error_proto")
    UPLOADED_DRIVE_ITEM_FIELD_NUMBER: _ClassVar[int]
    GRAPH_BASE_RESULT_FIELD_NUMBER: _ClassVar[int]
    O365_ERROR_PROTO_FIELD_NUMBER: _ClassVar[int]
    uploaded_drive_item: _graph_pb2.DriveItem
    graph_base_result: GraphBaseResult
    o365_error_proto: _o365_error_pb2.O365ErrorProto
    def __init__(self, uploaded_drive_item: _Optional[_Union[_graph_pb2.DriveItem, _Mapping]] = ..., graph_base_result: _Optional[_Union[GraphBaseResult, _Mapping]] = ..., o365_error_proto: _Optional[_Union[_o365_error_pb2.O365ErrorProto, _Mapping]] = ...) -> None: ...

class GetListsArg(_message.Message):
    __slots__ = ("site_id", "max_pages_to_fetch", "fetch_changes_in_pages", "next_link")
    SITE_ID_FIELD_NUMBER: _ClassVar[int]
    MAX_PAGES_TO_FETCH_FIELD_NUMBER: _ClassVar[int]
    FETCH_CHANGES_IN_PAGES_FIELD_NUMBER: _ClassVar[int]
    NEXT_LINK_FIELD_NUMBER: _ClassVar[int]
    site_id: str
    max_pages_to_fetch: int
    fetch_changes_in_pages: bool
    next_link: str
    def __init__(self, site_id: _Optional[str] = ..., max_pages_to_fetch: _Optional[int] = ..., fetch_changes_in_pages: bool = ..., next_link: _Optional[str] = ...) -> None: ...

class GetListsResult(_message.Message):
    __slots__ = ("site_list_vec", "graph_error", "next_link", "graph_base_result")
    SITE_LIST_VEC_FIELD_NUMBER: _ClassVar[int]
    GRAPH_ERROR_FIELD_NUMBER: _ClassVar[int]
    NEXT_LINK_FIELD_NUMBER: _ClassVar[int]
    GRAPH_BASE_RESULT_FIELD_NUMBER: _ClassVar[int]
    site_list_vec: _containers.RepeatedCompositeFieldContainer[_graph_pb2.List]
    graph_error: _graph_pb2.GraphError
    next_link: str
    graph_base_result: GraphBaseResult
    def __init__(self, site_list_vec: _Optional[_Iterable[_Union[_graph_pb2.List, _Mapping]]] = ..., graph_error: _Optional[_Union[_graph_pb2.GraphError, _Mapping]] = ..., next_link: _Optional[str] = ..., graph_base_result: _Optional[_Union[GraphBaseResult, _Mapping]] = ...) -> None: ...

class GetSiteDrivesArg(_message.Message):
    __slots__ = ("site_id", "include_sites_system_drives", "site_web_url", "fetch_drive_template", "attempt_to_determine_drive_type")
    SITE_ID_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_SITES_SYSTEM_DRIVES_FIELD_NUMBER: _ClassVar[int]
    SITE_WEB_URL_FIELD_NUMBER: _ClassVar[int]
    FETCH_DRIVE_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    ATTEMPT_TO_DETERMINE_DRIVE_TYPE_FIELD_NUMBER: _ClassVar[int]
    site_id: str
    include_sites_system_drives: bool
    site_web_url: str
    fetch_drive_template: bool
    attempt_to_determine_drive_type: bool
    def __init__(self, site_id: _Optional[str] = ..., include_sites_system_drives: bool = ..., site_web_url: _Optional[str] = ..., fetch_drive_template: bool = ..., attempt_to_determine_drive_type: bool = ...) -> None: ...

class GetSiteDrivesResult(_message.Message):
    __slots__ = ("site_drive_vec", "graph_error", "graph_base_result")
    SITE_DRIVE_VEC_FIELD_NUMBER: _ClassVar[int]
    GRAPH_ERROR_FIELD_NUMBER: _ClassVar[int]
    GRAPH_BASE_RESULT_FIELD_NUMBER: _ClassVar[int]
    site_drive_vec: _containers.RepeatedCompositeFieldContainer[_graph_pb2.SiteDrive]
    graph_error: _graph_pb2.GraphError
    graph_base_result: GraphBaseResult
    def __init__(self, site_drive_vec: _Optional[_Iterable[_Union[_graph_pb2.SiteDrive, _Mapping]]] = ..., graph_error: _Optional[_Union[_graph_pb2.GraphError, _Mapping]] = ..., graph_base_result: _Optional[_Union[GraphBaseResult, _Mapping]] = ...) -> None: ...

class CreateSiteListArg(_message.Message):
    __slots__ = ("site_id", "site_list_info_vec")
    class SiteListInfo(_message.Message):
        __slots__ = ("list_template", "list_name")
        LIST_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
        LIST_NAME_FIELD_NUMBER: _ClassVar[int]
        list_template: str
        list_name: str
        def __init__(self, list_template: _Optional[str] = ..., list_name: _Optional[str] = ...) -> None: ...
    SITE_ID_FIELD_NUMBER: _ClassVar[int]
    SITE_LIST_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    site_id: str
    site_list_info_vec: _containers.RepeatedCompositeFieldContainer[CreateSiteListArg.SiteListInfo]
    def __init__(self, site_id: _Optional[str] = ..., site_list_info_vec: _Optional[_Iterable[_Union[CreateSiteListArg.SiteListInfo, _Mapping]]] = ...) -> None: ...

class CreateSiteListResult(_message.Message):
    __slots__ = ("site_list", "graph_error", "graph_base_result")
    SITE_LIST_FIELD_NUMBER: _ClassVar[int]
    GRAPH_ERROR_FIELD_NUMBER: _ClassVar[int]
    GRAPH_BASE_RESULT_FIELD_NUMBER: _ClassVar[int]
    site_list: _containers.RepeatedCompositeFieldContainer[_graph_pb2.List]
    graph_error: _graph_pb2.GraphError
    graph_base_result: GraphBaseResult
    def __init__(self, site_list: _Optional[_Iterable[_Union[_graph_pb2.List, _Mapping]]] = ..., graph_error: _Optional[_Union[_graph_pb2.GraphError, _Mapping]] = ..., graph_base_result: _Optional[_Union[GraphBaseResult, _Mapping]] = ...) -> None: ...

class GetListItemsArg(_message.Message):
    __slots__ = ("site_id", "list_id", "expand_fields", "next_link")
    SITE_ID_FIELD_NUMBER: _ClassVar[int]
    LIST_ID_FIELD_NUMBER: _ClassVar[int]
    EXPAND_FIELDS_FIELD_NUMBER: _ClassVar[int]
    NEXT_LINK_FIELD_NUMBER: _ClassVar[int]
    site_id: str
    list_id: str
    expand_fields: bool
    next_link: str
    def __init__(self, site_id: _Optional[str] = ..., list_id: _Optional[str] = ..., expand_fields: bool = ..., next_link: _Optional[str] = ...) -> None: ...

class GetListItemsResult(_message.Message):
    __slots__ = ("item_list", "graph_error", "graph_base_result", "next_link")
    ITEM_LIST_FIELD_NUMBER: _ClassVar[int]
    GRAPH_ERROR_FIELD_NUMBER: _ClassVar[int]
    GRAPH_BASE_RESULT_FIELD_NUMBER: _ClassVar[int]
    NEXT_LINK_FIELD_NUMBER: _ClassVar[int]
    item_list: _containers.RepeatedCompositeFieldContainer[_graph_pb2.ListItem]
    graph_error: _graph_pb2.GraphError
    graph_base_result: GraphBaseResult
    next_link: str
    def __init__(self, item_list: _Optional[_Iterable[_Union[_graph_pb2.ListItem, _Mapping]]] = ..., graph_error: _Optional[_Union[_graph_pb2.GraphError, _Mapping]] = ..., graph_base_result: _Optional[_Union[GraphBaseResult, _Mapping]] = ..., next_link: _Optional[str] = ...) -> None: ...

class GetMailboxUsageDetailsArg(_message.Message):
    __slots__ = ("report_period",)
    REPORT_PERIOD_FIELD_NUMBER: _ClassVar[int]
    report_period: str
    def __init__(self, report_period: _Optional[str] = ...) -> None: ...

class GetMailboxUsageDetailsResult(_message.Message):
    __slots__ = ("mailbox_usage_content", "graph_base_result")
    MAILBOX_USAGE_CONTENT_FIELD_NUMBER: _ClassVar[int]
    GRAPH_BASE_RESULT_FIELD_NUMBER: _ClassVar[int]
    mailbox_usage_content: bytes
    graph_base_result: GraphBaseResult
    def __init__(self, mailbox_usage_content: _Optional[bytes] = ..., graph_base_result: _Optional[_Union[GraphBaseResult, _Mapping]] = ...) -> None: ...

class GetMailboxSettingsArg(_message.Message):
    __slots__ = ("user_id",)
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    def __init__(self, user_id: _Optional[str] = ...) -> None: ...

class GetMailboxSettingsResult(_message.Message):
    __slots__ = ("settings", "graph_error", "graph_base_result")
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    GRAPH_ERROR_FIELD_NUMBER: _ClassVar[int]
    GRAPH_BASE_RESULT_FIELD_NUMBER: _ClassVar[int]
    settings: _graph_pb2.MailboxSettings
    graph_error: _graph_pb2.GraphError
    graph_base_result: GraphBaseResult
    def __init__(self, settings: _Optional[_Union[_graph_pb2.MailboxSettings, _Mapping]] = ..., graph_error: _Optional[_Union[_graph_pb2.GraphError, _Mapping]] = ..., graph_base_result: _Optional[_Union[GraphBaseResult, _Mapping]] = ...) -> None: ...

class GetSharepointUsageDetailsArg(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetSharepointUsageDetailsResult(_message.Message):
    __slots__ = ("sharepoint_usage_content", "graph_base_result")
    SHAREPOINT_USAGE_CONTENT_FIELD_NUMBER: _ClassVar[int]
    GRAPH_BASE_RESULT_FIELD_NUMBER: _ClassVar[int]
    sharepoint_usage_content: bytes
    graph_base_result: GraphBaseResult
    def __init__(self, sharepoint_usage_content: _Optional[bytes] = ..., graph_base_result: _Optional[_Union[GraphBaseResult, _Mapping]] = ...) -> None: ...

class GetSiteInfoArg(_message.Message):
    __slots__ = ("site_relative_web_url", "sharepoint_domain_name", "site_id")
    SITE_RELATIVE_WEB_URL_FIELD_NUMBER: _ClassVar[int]
    SHAREPOINT_DOMAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    SITE_ID_FIELD_NUMBER: _ClassVar[int]
    site_relative_web_url: str
    sharepoint_domain_name: str
    site_id: str
    def __init__(self, site_relative_web_url: _Optional[str] = ..., sharepoint_domain_name: _Optional[str] = ..., site_id: _Optional[str] = ...) -> None: ...

class GetSiteInfoResult(_message.Message):
    __slots__ = ("site", "graph_base_result")
    SITE_FIELD_NUMBER: _ClassVar[int]
    GRAPH_BASE_RESULT_FIELD_NUMBER: _ClassVar[int]
    site: _graph_pb2.Site
    graph_base_result: GraphBaseResult
    def __init__(self, site: _Optional[_Union[_graph_pb2.Site, _Mapping]] = ..., graph_base_result: _Optional[_Union[GraphBaseResult, _Mapping]] = ...) -> None: ...

class GetSubSitesArg(_message.Message):
    __slots__ = ("site_id", "next_link", "site_web_url", "sharepoint_domain_name", "display_name")
    SITE_ID_FIELD_NUMBER: _ClassVar[int]
    NEXT_LINK_FIELD_NUMBER: _ClassVar[int]
    SITE_WEB_URL_FIELD_NUMBER: _ClassVar[int]
    SHAREPOINT_DOMAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    site_id: str
    next_link: str
    site_web_url: str
    sharepoint_domain_name: str
    display_name: str
    def __init__(self, site_id: _Optional[str] = ..., next_link: _Optional[str] = ..., site_web_url: _Optional[str] = ..., sharepoint_domain_name: _Optional[str] = ..., display_name: _Optional[str] = ...) -> None: ...

class GetSubSitesResult(_message.Message):
    __slots__ = ("sub_site", "next_link", "graph_base_result")
    SUB_SITE_FIELD_NUMBER: _ClassVar[int]
    NEXT_LINK_FIELD_NUMBER: _ClassVar[int]
    GRAPH_BASE_RESULT_FIELD_NUMBER: _ClassVar[int]
    sub_site: _containers.RepeatedCompositeFieldContainer[_graph_pb2.Site]
    next_link: str
    graph_base_result: GraphBaseResult
    def __init__(self, sub_site: _Optional[_Iterable[_Union[_graph_pb2.Site, _Mapping]]] = ..., next_link: _Optional[str] = ..., graph_base_result: _Optional[_Union[GraphBaseResult, _Mapping]] = ...) -> None: ...

class GetBatchSubSitesArg(_message.Message):
    __slots__ = ("sub_site_request_vec",)
    SUB_SITE_REQUEST_VEC_FIELD_NUMBER: _ClassVar[int]
    sub_site_request_vec: _containers.RepeatedCompositeFieldContainer[GetSubSitesArg]
    def __init__(self, sub_site_request_vec: _Optional[_Iterable[_Union[GetSubSitesArg, _Mapping]]] = ...) -> None: ...

class GetBatchSubSitesResult(_message.Message):
    __slots__ = ("site_vec", "invalid_site_id_vec", "warning_vec", "throttled_site_id_vec", "retry_delay_in_secs", "graph_base_result")
    class SubSiteResult(_message.Message):
        __slots__ = ("site_id", "sub_site_vec")
        SITE_ID_FIELD_NUMBER: _ClassVar[int]
        SUB_SITE_VEC_FIELD_NUMBER: _ClassVar[int]
        site_id: str
        sub_site_vec: _containers.RepeatedCompositeFieldContainer[_graph_pb2.Site]
        def __init__(self, site_id: _Optional[str] = ..., sub_site_vec: _Optional[_Iterable[_Union[_graph_pb2.Site, _Mapping]]] = ...) -> None: ...
    SITE_VEC_FIELD_NUMBER: _ClassVar[int]
    INVALID_SITE_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    WARNING_VEC_FIELD_NUMBER: _ClassVar[int]
    THROTTLED_SITE_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    RETRY_DELAY_IN_SECS_FIELD_NUMBER: _ClassVar[int]
    GRAPH_BASE_RESULT_FIELD_NUMBER: _ClassVar[int]
    site_vec: _containers.RepeatedCompositeFieldContainer[GetBatchSubSitesResult.SubSiteResult]
    invalid_site_id_vec: _containers.RepeatedScalarFieldContainer[str]
    warning_vec: _containers.RepeatedScalarFieldContainer[str]
    throttled_site_id_vec: _containers.RepeatedScalarFieldContainer[str]
    retry_delay_in_secs: int
    graph_base_result: GraphBaseResult
    def __init__(self, site_vec: _Optional[_Iterable[_Union[GetBatchSubSitesResult.SubSiteResult, _Mapping]]] = ..., invalid_site_id_vec: _Optional[_Iterable[str]] = ..., warning_vec: _Optional[_Iterable[str]] = ..., throttled_site_id_vec: _Optional[_Iterable[str]] = ..., retry_delay_in_secs: _Optional[int] = ..., graph_base_result: _Optional[_Union[GraphBaseResult, _Mapping]] = ...) -> None: ...

class RestorePermissionsArg(_message.Message):
    __slots__ = ("drive_id", "drive_item_id", "recipient_vec", "message_content", "require_sign_in", "send_invitation", "role_vec")
    DRIVE_ID_FIELD_NUMBER: _ClassVar[int]
    DRIVE_ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    RECIPIENT_VEC_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_CONTENT_FIELD_NUMBER: _ClassVar[int]
    REQUIRE_SIGN_IN_FIELD_NUMBER: _ClassVar[int]
    SEND_INVITATION_FIELD_NUMBER: _ClassVar[int]
    ROLE_VEC_FIELD_NUMBER: _ClassVar[int]
    drive_id: str
    drive_item_id: str
    recipient_vec: _containers.RepeatedCompositeFieldContainer[_graph_pb2.Recipients]
    message_content: str
    require_sign_in: bool
    send_invitation: bool
    role_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, drive_id: _Optional[str] = ..., drive_item_id: _Optional[str] = ..., recipient_vec: _Optional[_Iterable[_Union[_graph_pb2.Recipients, _Mapping]]] = ..., message_content: _Optional[str] = ..., require_sign_in: bool = ..., send_invitation: bool = ..., role_vec: _Optional[_Iterable[str]] = ...) -> None: ...

class RestorePermissionsResult(_message.Message):
    __slots__ = ("graph_base_result", "graph_error")
    GRAPH_BASE_RESULT_FIELD_NUMBER: _ClassVar[int]
    GRAPH_ERROR_FIELD_NUMBER: _ClassVar[int]
    graph_base_result: GraphBaseResult
    graph_error: _graph_pb2.GraphError
    def __init__(self, graph_base_result: _Optional[_Union[GraphBaseResult, _Mapping]] = ..., graph_error: _Optional[_Union[_graph_pb2.GraphError, _Mapping]] = ...) -> None: ...

class DeletePermissionArg(_message.Message):
    __slots__ = ("drive_id", "drive_item_id", "permission_id")
    DRIVE_ID_FIELD_NUMBER: _ClassVar[int]
    DRIVE_ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    PERMISSION_ID_FIELD_NUMBER: _ClassVar[int]
    drive_id: str
    drive_item_id: str
    permission_id: str
    def __init__(self, drive_id: _Optional[str] = ..., drive_item_id: _Optional[str] = ..., permission_id: _Optional[str] = ...) -> None: ...

class DeletePermissionResult(_message.Message):
    __slots__ = ("graph_base_result",)
    GRAPH_BASE_RESULT_FIELD_NUMBER: _ClassVar[int]
    graph_base_result: GraphBaseResult
    def __init__(self, graph_base_result: _Optional[_Union[GraphBaseResult, _Mapping]] = ...) -> None: ...

class GetGroupOwnersArg(_message.Message):
    __slots__ = ("group_id", "retry_get_owners")
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    RETRY_GET_OWNERS_FIELD_NUMBER: _ClassVar[int]
    group_id: str
    retry_get_owners: bool
    def __init__(self, group_id: _Optional[str] = ..., retry_get_owners: bool = ...) -> None: ...

class GetGroupOwnersResult(_message.Message):
    __slots__ = ("owner_vec", "graph_base_result")
    OWNER_VEC_FIELD_NUMBER: _ClassVar[int]
    GRAPH_BASE_RESULT_FIELD_NUMBER: _ClassVar[int]
    owner_vec: _containers.RepeatedCompositeFieldContainer[_graph_pb2.User]
    graph_base_result: GraphBaseResult
    def __init__(self, owner_vec: _Optional[_Iterable[_Union[_graph_pb2.User, _Mapping]]] = ..., graph_base_result: _Optional[_Union[GraphBaseResult, _Mapping]] = ...) -> None: ...

class GetGroupMembersArg(_message.Message):
    __slots__ = ("group_id", "next_link", "expected_members_id_vec")
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    NEXT_LINK_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_MEMBERS_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    group_id: str
    next_link: str
    expected_members_id_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, group_id: _Optional[str] = ..., next_link: _Optional[str] = ..., expected_members_id_vec: _Optional[_Iterable[str]] = ...) -> None: ...

class GetGroupMembersResult(_message.Message):
    __slots__ = ("members_vec", "graph_base_result", "next_link")
    MEMBERS_VEC_FIELD_NUMBER: _ClassVar[int]
    GRAPH_BASE_RESULT_FIELD_NUMBER: _ClassVar[int]
    NEXT_LINK_FIELD_NUMBER: _ClassVar[int]
    members_vec: _containers.RepeatedCompositeFieldContainer[_graph_pb2.User]
    graph_base_result: GraphBaseResult
    next_link: str
    def __init__(self, members_vec: _Optional[_Iterable[_Union[_graph_pb2.User, _Mapping]]] = ..., graph_base_result: _Optional[_Union[GraphBaseResult, _Mapping]] = ..., next_link: _Optional[str] = ...) -> None: ...

class GetSubscribedSkusArg(_message.Message):
    __slots__ = ("next_link",)
    NEXT_LINK_FIELD_NUMBER: _ClassVar[int]
    next_link: str
    def __init__(self, next_link: _Optional[str] = ...) -> None: ...

class GetSubscribedSkusResult(_message.Message):
    __slots__ = ("sku_vec", "next_link", "graph_base_result")
    SKU_VEC_FIELD_NUMBER: _ClassVar[int]
    NEXT_LINK_FIELD_NUMBER: _ClassVar[int]
    GRAPH_BASE_RESULT_FIELD_NUMBER: _ClassVar[int]
    sku_vec: _containers.RepeatedCompositeFieldContainer[_graph_pb2.SubscribedSku]
    next_link: str
    graph_base_result: GraphBaseResult
    def __init__(self, sku_vec: _Optional[_Iterable[_Union[_graph_pb2.SubscribedSku, _Mapping]]] = ..., next_link: _Optional[str] = ..., graph_base_result: _Optional[_Union[GraphBaseResult, _Mapping]] = ...) -> None: ...

class GetDriveInfoResult(_message.Message):
    __slots__ = ("content",)
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    content: bytes
    def __init__(self, content: _Optional[bytes] = ...) -> None: ...

class GetGroupDeltaArg(_message.Message):
    __slots__ = ("group_id", "next_link")
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    NEXT_LINK_FIELD_NUMBER: _ClassVar[int]
    group_id: str
    next_link: str
    def __init__(self, group_id: _Optional[str] = ..., next_link: _Optional[str] = ...) -> None: ...

class GetGroupDeltaResult(_message.Message):
    __slots__ = ("delta_link", "group_vec", "next_link", "o365_error_proto", "graph_base_result")
    DELTA_LINK_FIELD_NUMBER: _ClassVar[int]
    GROUP_VEC_FIELD_NUMBER: _ClassVar[int]
    NEXT_LINK_FIELD_NUMBER: _ClassVar[int]
    O365_ERROR_PROTO_FIELD_NUMBER: _ClassVar[int]
    GRAPH_BASE_RESULT_FIELD_NUMBER: _ClassVar[int]
    delta_link: str
    group_vec: _containers.RepeatedCompositeFieldContainer[_graph_pb2.Group]
    next_link: str
    o365_error_proto: _o365_error_pb2.O365ErrorProto
    graph_base_result: GraphBaseResult
    def __init__(self, delta_link: _Optional[str] = ..., group_vec: _Optional[_Iterable[_Union[_graph_pb2.Group, _Mapping]]] = ..., next_link: _Optional[str] = ..., o365_error_proto: _Optional[_Union[_o365_error_pb2.O365ErrorProto, _Mapping]] = ..., graph_base_result: _Optional[_Union[GraphBaseResult, _Mapping]] = ...) -> None: ...

class AddUsersToGroupArg(_message.Message):
    __slots__ = ("group_id", "users_list")
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    USERS_LIST_FIELD_NUMBER: _ClassVar[int]
    group_id: str
    users_list: _graph_pb2.UsersList
    def __init__(self, group_id: _Optional[str] = ..., users_list: _Optional[_Union[_graph_pb2.UsersList, _Mapping]] = ...) -> None: ...

class AddUsersToGroupResult(_message.Message):
    __slots__ = ("graph_base_result", "graph_error")
    GRAPH_BASE_RESULT_FIELD_NUMBER: _ClassVar[int]
    GRAPH_ERROR_FIELD_NUMBER: _ClassVar[int]
    graph_base_result: GraphBaseResult
    graph_error: _graph_pb2.GraphError
    def __init__(self, graph_base_result: _Optional[_Union[GraphBaseResult, _Mapping]] = ..., graph_error: _Optional[_Union[_graph_pb2.GraphError, _Mapping]] = ...) -> None: ...

class CreateTeamChannelsArg(_message.Message):
    __slots__ = ("team_id", "public_channel_info_vec", "private_channel_info_vec")
    class PublicChannelInfo(_message.Message):
        __slots__ = ("display_name", "description")
        DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        display_name: str
        description: str
        def __init__(self, display_name: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...
    class PrivateChannelInfo(_message.Message):
        __slots__ = ("display_name", "description", "members", "owners")
        DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        MEMBERS_FIELD_NUMBER: _ClassVar[int]
        OWNERS_FIELD_NUMBER: _ClassVar[int]
        display_name: str
        description: str
        members: _containers.RepeatedScalarFieldContainer[str]
        owners: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, display_name: _Optional[str] = ..., description: _Optional[str] = ..., members: _Optional[_Iterable[str]] = ..., owners: _Optional[_Iterable[str]] = ...) -> None: ...
    TEAM_ID_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_CHANNEL_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_CHANNEL_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    team_id: str
    public_channel_info_vec: _containers.RepeatedCompositeFieldContainer[CreateTeamChannelsArg.PublicChannelInfo]
    private_channel_info_vec: _containers.RepeatedCompositeFieldContainer[CreateTeamChannelsArg.PrivateChannelInfo]
    def __init__(self, team_id: _Optional[str] = ..., public_channel_info_vec: _Optional[_Iterable[_Union[CreateTeamChannelsArg.PublicChannelInfo, _Mapping]]] = ..., private_channel_info_vec: _Optional[_Iterable[_Union[CreateTeamChannelsArg.PrivateChannelInfo, _Mapping]]] = ...) -> None: ...

class CreateTeamChannelsResult(_message.Message):
    __slots__ = ("created_channels_list", "graph_error", "graph_base_result")
    CREATED_CHANNELS_LIST_FIELD_NUMBER: _ClassVar[int]
    GRAPH_ERROR_FIELD_NUMBER: _ClassVar[int]
    GRAPH_BASE_RESULT_FIELD_NUMBER: _ClassVar[int]
    created_channels_list: _containers.RepeatedCompositeFieldContainer[_graph_pb2.Channel]
    graph_error: _graph_pb2.GraphError
    graph_base_result: GraphBaseResult
    def __init__(self, created_channels_list: _Optional[_Iterable[_Union[_graph_pb2.Channel, _Mapping]]] = ..., graph_error: _Optional[_Union[_graph_pb2.GraphError, _Mapping]] = ..., graph_base_result: _Optional[_Union[GraphBaseResult, _Mapping]] = ...) -> None: ...

class GetGroupSiteArg(_message.Message):
    __slots__ = ("group_id", "retry_get_site")
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    RETRY_GET_SITE_FIELD_NUMBER: _ClassVar[int]
    group_id: str
    retry_get_site: bool
    def __init__(self, group_id: _Optional[str] = ..., retry_get_site: bool = ...) -> None: ...

class GetGroupSiteResult(_message.Message):
    __slots__ = ("teams_site", "graph_base_result", "graph_error")
    TEAMS_SITE_FIELD_NUMBER: _ClassVar[int]
    GRAPH_BASE_RESULT_FIELD_NUMBER: _ClassVar[int]
    GRAPH_ERROR_FIELD_NUMBER: _ClassVar[int]
    teams_site: _graph_pb2.Site
    graph_base_result: GraphBaseResult
    graph_error: _graph_pb2.GraphError
    def __init__(self, teams_site: _Optional[_Union[_graph_pb2.Site, _Mapping]] = ..., graph_base_result: _Optional[_Union[GraphBaseResult, _Mapping]] = ..., graph_error: _Optional[_Union[_graph_pb2.GraphError, _Mapping]] = ...) -> None: ...

class GetTeamsChannelsArg(_message.Message):
    __slots__ = ("teams_id", "verify_channels_id_vec")
    TEAMS_ID_FIELD_NUMBER: _ClassVar[int]
    VERIFY_CHANNELS_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    teams_id: str
    verify_channels_id_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, teams_id: _Optional[str] = ..., verify_channels_id_vec: _Optional[_Iterable[str]] = ...) -> None: ...

class GetTeamsChannelsResult(_message.Message):
    __slots__ = ("channel_vec", "graph_base_result", "graph_error")
    CHANNEL_VEC_FIELD_NUMBER: _ClassVar[int]
    GRAPH_BASE_RESULT_FIELD_NUMBER: _ClassVar[int]
    GRAPH_ERROR_FIELD_NUMBER: _ClassVar[int]
    channel_vec: _containers.RepeatedCompositeFieldContainer[_graph_pb2.Channel]
    graph_base_result: GraphBaseResult
    graph_error: _graph_pb2.GraphError
    def __init__(self, channel_vec: _Optional[_Iterable[_Union[_graph_pb2.Channel, _Mapping]]] = ..., graph_base_result: _Optional[_Union[GraphBaseResult, _Mapping]] = ..., graph_error: _Optional[_Union[_graph_pb2.GraphError, _Mapping]] = ...) -> None: ...

class GetTeamsChannelDriveArg(_message.Message):
    __slots__ = ("teams_id", "channel_id", "site_id")
    TEAMS_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    SITE_ID_FIELD_NUMBER: _ClassVar[int]
    teams_id: str
    channel_id: str
    site_id: str
    def __init__(self, teams_id: _Optional[str] = ..., channel_id: _Optional[str] = ..., site_id: _Optional[str] = ...) -> None: ...

class GetTeamsChannelDriveResult(_message.Message):
    __slots__ = ("channel_drive", "site", "graph_base_result", "graph_error")
    CHANNEL_DRIVE_FIELD_NUMBER: _ClassVar[int]
    SITE_FIELD_NUMBER: _ClassVar[int]
    GRAPH_BASE_RESULT_FIELD_NUMBER: _ClassVar[int]
    GRAPH_ERROR_FIELD_NUMBER: _ClassVar[int]
    channel_drive: _graph_pb2.SiteDrive
    site: _graph_pb2.Site
    graph_base_result: GraphBaseResult
    graph_error: _graph_pb2.GraphError
    def __init__(self, channel_drive: _Optional[_Union[_graph_pb2.SiteDrive, _Mapping]] = ..., site: _Optional[_Union[_graph_pb2.Site, _Mapping]] = ..., graph_base_result: _Optional[_Union[GraphBaseResult, _Mapping]] = ..., graph_error: _Optional[_Union[_graph_pb2.GraphError, _Mapping]] = ...) -> None: ...

class GetTeamArg(_message.Message):
    __slots__ = ("teams_id",)
    TEAMS_ID_FIELD_NUMBER: _ClassVar[int]
    teams_id: str
    def __init__(self, teams_id: _Optional[str] = ...) -> None: ...

class GetTeamResult(_message.Message):
    __slots__ = ("team", "graph_base_result", "graph_error")
    TEAM_FIELD_NUMBER: _ClassVar[int]
    GRAPH_BASE_RESULT_FIELD_NUMBER: _ClassVar[int]
    GRAPH_ERROR_FIELD_NUMBER: _ClassVar[int]
    team: _graph_pb2.Team
    graph_base_result: GraphBaseResult
    graph_error: _graph_pb2.GraphError
    def __init__(self, team: _Optional[_Union[_graph_pb2.Team, _Mapping]] = ..., graph_base_result: _Optional[_Union[GraphBaseResult, _Mapping]] = ..., graph_error: _Optional[_Union[_graph_pb2.GraphError, _Mapping]] = ...) -> None: ...

class GetChannelSiteArg(_message.Message):
    __slots__ = ("teams_id", "channel_id", "retry_get_channel_site")
    TEAMS_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    RETRY_GET_CHANNEL_SITE_FIELD_NUMBER: _ClassVar[int]
    teams_id: str
    channel_id: str
    retry_get_channel_site: bool
    def __init__(self, teams_id: _Optional[str] = ..., channel_id: _Optional[str] = ..., retry_get_channel_site: bool = ...) -> None: ...

class GetChannelSiteResult(_message.Message):
    __slots__ = ("site", "graph_base_result", "graph_error", "channel_folder_name")
    SITE_FIELD_NUMBER: _ClassVar[int]
    GRAPH_BASE_RESULT_FIELD_NUMBER: _ClassVar[int]
    GRAPH_ERROR_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_FOLDER_NAME_FIELD_NUMBER: _ClassVar[int]
    site: _graph_pb2.Site
    graph_base_result: GraphBaseResult
    graph_error: _graph_pb2.GraphError
    channel_folder_name: str
    def __init__(self, site: _Optional[_Union[_graph_pb2.Site, _Mapping]] = ..., graph_base_result: _Optional[_Union[GraphBaseResult, _Mapping]] = ..., graph_error: _Optional[_Union[_graph_pb2.GraphError, _Mapping]] = ..., channel_folder_name: _Optional[str] = ...) -> None: ...

class UpdateTeamChannelArg(_message.Message):
    __slots__ = ("team_id", "channel_id", "add_member_info", "delete_member_info", "update_member_info", "channel_display_name", "channel_description", "update_tab_info_vec", "add_tab_info_vec", "skip_add_update_tab_errors", "moderation_settings")
    class AddMemberInfo(_message.Message):
        __slots__ = ("user_id", "role")
        USER_ID_FIELD_NUMBER: _ClassVar[int]
        ROLE_FIELD_NUMBER: _ClassVar[int]
        user_id: str
        role: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, user_id: _Optional[str] = ..., role: _Optional[_Iterable[str]] = ...) -> None: ...
    class DeleteMemberInfo(_message.Message):
        __slots__ = ("member_id",)
        MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
        member_id: str
        def __init__(self, member_id: _Optional[str] = ...) -> None: ...
    class UpdateMemberInfo(_message.Message):
        __slots__ = ("member_id", "role")
        MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
        ROLE_FIELD_NUMBER: _ClassVar[int]
        member_id: str
        role: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, member_id: _Optional[str] = ..., role: _Optional[_Iterable[str]] = ...) -> None: ...
    class UpdateTabInfo(_message.Message):
        __slots__ = ("tab_id", "tab")
        TAB_ID_FIELD_NUMBER: _ClassVar[int]
        TAB_FIELD_NUMBER: _ClassVar[int]
        tab_id: str
        tab: _graph_pb2.ChannelTabInfo
        def __init__(self, tab_id: _Optional[str] = ..., tab: _Optional[_Union[_graph_pb2.ChannelTabInfo, _Mapping]] = ...) -> None: ...
    class AddTabInfo(_message.Message):
        __slots__ = ("tab",)
        TAB_FIELD_NUMBER: _ClassVar[int]
        tab: _graph_pb2.ChannelTabInfo
        def __init__(self, tab: _Optional[_Union[_graph_pb2.ChannelTabInfo, _Mapping]] = ...) -> None: ...
    TEAM_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    ADD_MEMBER_INFO_FIELD_NUMBER: _ClassVar[int]
    DELETE_MEMBER_INFO_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MEMBER_INFO_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TAB_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    ADD_TAB_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    SKIP_ADD_UPDATE_TAB_ERRORS_FIELD_NUMBER: _ClassVar[int]
    MODERATION_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    team_id: str
    channel_id: str
    add_member_info: UpdateTeamChannelArg.AddMemberInfo
    delete_member_info: UpdateTeamChannelArg.DeleteMemberInfo
    update_member_info: UpdateTeamChannelArg.UpdateMemberInfo
    channel_display_name: str
    channel_description: str
    update_tab_info_vec: _containers.RepeatedCompositeFieldContainer[UpdateTeamChannelArg.UpdateTabInfo]
    add_tab_info_vec: _containers.RepeatedCompositeFieldContainer[UpdateTeamChannelArg.AddTabInfo]
    skip_add_update_tab_errors: bool
    moderation_settings: _graph_pb2.ChannelModerationSettings
    def __init__(self, team_id: _Optional[str] = ..., channel_id: _Optional[str] = ..., add_member_info: _Optional[_Union[UpdateTeamChannelArg.AddMemberInfo, _Mapping]] = ..., delete_member_info: _Optional[_Union[UpdateTeamChannelArg.DeleteMemberInfo, _Mapping]] = ..., update_member_info: _Optional[_Union[UpdateTeamChannelArg.UpdateMemberInfo, _Mapping]] = ..., channel_display_name: _Optional[str] = ..., channel_description: _Optional[str] = ..., update_tab_info_vec: _Optional[_Iterable[_Union[UpdateTeamChannelArg.UpdateTabInfo, _Mapping]]] = ..., add_tab_info_vec: _Optional[_Iterable[_Union[UpdateTeamChannelArg.AddTabInfo, _Mapping]]] = ..., skip_add_update_tab_errors: bool = ..., moderation_settings: _Optional[_Union[_graph_pb2.ChannelModerationSettings, _Mapping]] = ...) -> None: ...

class UpdateTeamChannelRequestBody(_message.Message):
    __slots__ = ("odata_type", "roles", "user")
    ODATA_TYPE_FIELD_NUMBER: _ClassVar[int]
    ROLES_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    odata_type: str
    roles: _containers.RepeatedScalarFieldContainer[str]
    user: str
    def __init__(self, odata_type: _Optional[str] = ..., roles: _Optional[_Iterable[str]] = ..., user: _Optional[str] = ...) -> None: ...

class UpdateTeamChannelResult(_message.Message):
    __slots__ = ("id", "user_id", "display_name", "graph_base_result", "added_tab_vec", "updated_tab_vec")
    class ChannelTabInfoError(_message.Message):
        __slots__ = ("tab", "error")
        TAB_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        tab: _graph_pb2.ChannelTabInfo
        error: _error_pb2.ErrorProto
        def __init__(self, tab: _Optional[_Union[_graph_pb2.ChannelTabInfo, _Mapping]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    GRAPH_BASE_RESULT_FIELD_NUMBER: _ClassVar[int]
    ADDED_TAB_VEC_FIELD_NUMBER: _ClassVar[int]
    UPDATED_TAB_VEC_FIELD_NUMBER: _ClassVar[int]
    id: str
    user_id: str
    display_name: str
    graph_base_result: GraphBaseResult
    added_tab_vec: _containers.RepeatedCompositeFieldContainer[UpdateTeamChannelResult.ChannelTabInfoError]
    updated_tab_vec: _containers.RepeatedCompositeFieldContainer[UpdateTeamChannelResult.ChannelTabInfoError]
    def __init__(self, id: _Optional[str] = ..., user_id: _Optional[str] = ..., display_name: _Optional[str] = ..., graph_base_result: _Optional[_Union[GraphBaseResult, _Mapping]] = ..., added_tab_vec: _Optional[_Iterable[_Union[UpdateTeamChannelResult.ChannelTabInfoError, _Mapping]]] = ..., updated_tab_vec: _Optional[_Iterable[_Union[UpdateTeamChannelResult.ChannelTabInfoError, _Mapping]]] = ...) -> None: ...

class CreateTeamArg(_message.Message):
    __slots__ = ("team", "group_id", "skip_teams_site_intialization")
    TEAM_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    SKIP_TEAMS_SITE_INTIALIZATION_FIELD_NUMBER: _ClassVar[int]
    team: _graph_pb2.Team
    group_id: str
    skip_teams_site_intialization: bool
    def __init__(self, team: _Optional[_Union[_graph_pb2.Team, _Mapping]] = ..., group_id: _Optional[str] = ..., skip_teams_site_intialization: bool = ...) -> None: ...

class CreateTeamResult(_message.Message):
    __slots__ = ("team", "graph_base_result", "success_init_teams_site")
    TEAM_FIELD_NUMBER: _ClassVar[int]
    GRAPH_BASE_RESULT_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_INIT_TEAMS_SITE_FIELD_NUMBER: _ClassVar[int]
    team: _graph_pb2.Team
    graph_base_result: GraphBaseResult
    success_init_teams_site: bool
    def __init__(self, team: _Optional[_Union[_graph_pb2.Team, _Mapping]] = ..., graph_base_result: _Optional[_Union[GraphBaseResult, _Mapping]] = ..., success_init_teams_site: bool = ...) -> None: ...

class ChannelMembers(_message.Message):
    __slots__ = ("num_members", "channel_member_vec", "next_link")
    NUM_MEMBERS_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_MEMBER_VEC_FIELD_NUMBER: _ClassVar[int]
    NEXT_LINK_FIELD_NUMBER: _ClassVar[int]
    num_members: int
    channel_member_vec: _containers.RepeatedCompositeFieldContainer[_graph_pb2.ChannelMemberInfo]
    next_link: str
    def __init__(self, num_members: _Optional[int] = ..., channel_member_vec: _Optional[_Iterable[_Union[_graph_pb2.ChannelMemberInfo, _Mapping]]] = ..., next_link: _Optional[str] = ...) -> None: ...

class ChannelTabs(_message.Message):
    __slots__ = ("num_tabs", "channel_tabs_vec", "next_link")
    NUM_TABS_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_TABS_VEC_FIELD_NUMBER: _ClassVar[int]
    NEXT_LINK_FIELD_NUMBER: _ClassVar[int]
    num_tabs: int
    channel_tabs_vec: _containers.RepeatedCompositeFieldContainer[_graph_pb2.ChannelTabInfo]
    next_link: str
    def __init__(self, num_tabs: _Optional[int] = ..., channel_tabs_vec: _Optional[_Iterable[_Union[_graph_pb2.ChannelTabInfo, _Mapping]]] = ..., next_link: _Optional[str] = ...) -> None: ...

class GetChannelInfoArg(_message.Message):
    __slots__ = ("get_members", "get_tabs", "teams_id", "channel_id", "next_link")
    GET_MEMBERS_FIELD_NUMBER: _ClassVar[int]
    GET_TABS_FIELD_NUMBER: _ClassVar[int]
    TEAMS_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    NEXT_LINK_FIELD_NUMBER: _ClassVar[int]
    get_members: bool
    get_tabs: bool
    teams_id: str
    channel_id: str
    next_link: str
    def __init__(self, get_members: bool = ..., get_tabs: bool = ..., teams_id: _Optional[str] = ..., channel_id: _Optional[str] = ..., next_link: _Optional[str] = ...) -> None: ...

class GetChannelInfoResult(_message.Message):
    __slots__ = ("num_members", "channel_member_vec", "num_tabs", "channel_tabs_vec", "graph_base_result", "fetch_members_error", "fetch_tabs_error")
    NUM_MEMBERS_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_MEMBER_VEC_FIELD_NUMBER: _ClassVar[int]
    NUM_TABS_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_TABS_VEC_FIELD_NUMBER: _ClassVar[int]
    GRAPH_BASE_RESULT_FIELD_NUMBER: _ClassVar[int]
    FETCH_MEMBERS_ERROR_FIELD_NUMBER: _ClassVar[int]
    FETCH_TABS_ERROR_FIELD_NUMBER: _ClassVar[int]
    num_members: int
    channel_member_vec: _containers.RepeatedCompositeFieldContainer[_graph_pb2.ChannelMemberInfo]
    num_tabs: int
    channel_tabs_vec: _containers.RepeatedCompositeFieldContainer[_graph_pb2.ChannelTabInfo]
    graph_base_result: GraphBaseResult
    fetch_members_error: bool
    fetch_tabs_error: bool
    def __init__(self, num_members: _Optional[int] = ..., channel_member_vec: _Optional[_Iterable[_Union[_graph_pb2.ChannelMemberInfo, _Mapping]]] = ..., num_tabs: _Optional[int] = ..., channel_tabs_vec: _Optional[_Iterable[_Union[_graph_pb2.ChannelTabInfo, _Mapping]]] = ..., graph_base_result: _Optional[_Union[GraphBaseResult, _Mapping]] = ..., fetch_members_error: bool = ..., fetch_tabs_error: bool = ...) -> None: ...

class UpdateGroupArg(_message.Message):
    __slots__ = ("group", "should_update_group_users", "only_update_group_users")
    GROUP_FIELD_NUMBER: _ClassVar[int]
    SHOULD_UPDATE_GROUP_USERS_FIELD_NUMBER: _ClassVar[int]
    ONLY_UPDATE_GROUP_USERS_FIELD_NUMBER: _ClassVar[int]
    group: _graph_pb2.Group
    should_update_group_users: bool
    only_update_group_users: bool
    def __init__(self, group: _Optional[_Union[_graph_pb2.Group, _Mapping]] = ..., should_update_group_users: bool = ..., only_update_group_users: bool = ...) -> None: ...

class UpdateGroupResult(_message.Message):
    __slots__ = ("group", "graph_base_result", "graph_error")
    GROUP_FIELD_NUMBER: _ClassVar[int]
    GRAPH_BASE_RESULT_FIELD_NUMBER: _ClassVar[int]
    GRAPH_ERROR_FIELD_NUMBER: _ClassVar[int]
    group: _graph_pb2.Group
    graph_base_result: GraphBaseResult
    graph_error: _graph_pb2.GraphError
    def __init__(self, group: _Optional[_Union[_graph_pb2.Group, _Mapping]] = ..., graph_base_result: _Optional[_Union[GraphBaseResult, _Mapping]] = ..., graph_error: _Optional[_Union[_graph_pb2.GraphError, _Mapping]] = ...) -> None: ...

class UpdateTeamArg(_message.Message):
    __slots__ = ("team",)
    TEAM_FIELD_NUMBER: _ClassVar[int]
    team: _graph_pb2.Team
    def __init__(self, team: _Optional[_Union[_graph_pb2.Team, _Mapping]] = ...) -> None: ...

class UpdateTeamResult(_message.Message):
    __slots__ = ("graph_base_result", "graph_error")
    GRAPH_BASE_RESULT_FIELD_NUMBER: _ClassVar[int]
    GRAPH_ERROR_FIELD_NUMBER: _ClassVar[int]
    graph_base_result: GraphBaseResult
    graph_error: _graph_pb2.GraphError
    def __init__(self, graph_base_result: _Optional[_Union[GraphBaseResult, _Mapping]] = ..., graph_error: _Optional[_Union[_graph_pb2.GraphError, _Mapping]] = ...) -> None: ...

class GetGroupUsageDetailsArg(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetGroupUsageDetailsResult(_message.Message):
    __slots__ = ("group_usage_content", "graph_base_result")
    GROUP_USAGE_CONTENT_FIELD_NUMBER: _ClassVar[int]
    GRAPH_BASE_RESULT_FIELD_NUMBER: _ClassVar[int]
    group_usage_content: bytes
    graph_base_result: GraphBaseResult
    def __init__(self, group_usage_content: _Optional[bytes] = ..., graph_base_result: _Optional[_Union[GraphBaseResult, _Mapping]] = ...) -> None: ...

class OperationError(_message.Message):
    __slots__ = ("code", "message")
    CODE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    code: str
    message: str
    def __init__(self, code: _Optional[str] = ..., message: _Optional[str] = ...) -> None: ...

class GetTeamsAsyncOperationResult(_message.Message):
    __slots__ = ("id", "operation_type", "created_date_time", "status", "last_action_date_time", "attempts_count", "target_resource_id", "target_resource_location", "error", "graph_base_result")
    ID_FIELD_NUMBER: _ClassVar[int]
    OPERATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    CREATED_DATE_TIME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    LAST_ACTION_DATE_TIME_FIELD_NUMBER: _ClassVar[int]
    ATTEMPTS_COUNT_FIELD_NUMBER: _ClassVar[int]
    TARGET_RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_RESOURCE_LOCATION_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    GRAPH_BASE_RESULT_FIELD_NUMBER: _ClassVar[int]
    id: str
    operation_type: str
    created_date_time: str
    status: str
    last_action_date_time: str
    attempts_count: int
    target_resource_id: str
    target_resource_location: str
    error: OperationError
    graph_base_result: GraphBaseResult
    def __init__(self, id: _Optional[str] = ..., operation_type: _Optional[str] = ..., created_date_time: _Optional[str] = ..., status: _Optional[str] = ..., last_action_date_time: _Optional[str] = ..., attempts_count: _Optional[int] = ..., target_resource_id: _Optional[str] = ..., target_resource_location: _Optional[str] = ..., error: _Optional[_Union[OperationError, _Mapping]] = ..., graph_base_result: _Optional[_Union[GraphBaseResult, _Mapping]] = ...) -> None: ...

class GetSharepointHostNameArg(_message.Message):
    __slots__ = ("fetch_root_site_collections",)
    FETCH_ROOT_SITE_COLLECTIONS_FIELD_NUMBER: _ClassVar[int]
    fetch_root_site_collections: bool
    def __init__(self, fetch_root_site_collections: bool = ...) -> None: ...

class GetSharepointHostNameResult(_message.Message):
    __slots__ = ("hostname", "graph_error", "graph_base_result", "data_location_code_to_hostname_map")
    class DataLocationCodeToHostnameMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    HOSTNAME_FIELD_NUMBER: _ClassVar[int]
    GRAPH_ERROR_FIELD_NUMBER: _ClassVar[int]
    GRAPH_BASE_RESULT_FIELD_NUMBER: _ClassVar[int]
    DATA_LOCATION_CODE_TO_HOSTNAME_MAP_FIELD_NUMBER: _ClassVar[int]
    hostname: str
    graph_error: _graph_pb2.GraphError
    graph_base_result: GraphBaseResult
    data_location_code_to_hostname_map: _containers.ScalarMap[str, str]
    def __init__(self, hostname: _Optional[str] = ..., graph_error: _Optional[_Union[_graph_pb2.GraphError, _Mapping]] = ..., graph_base_result: _Optional[_Union[GraphBaseResult, _Mapping]] = ..., data_location_code_to_hostname_map: _Optional[_Mapping[str, str]] = ...) -> None: ...

class DeleteM365GroupArg(_message.Message):
    __slots__ = ("group_id",)
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    group_id: str
    def __init__(self, group_id: _Optional[str] = ...) -> None: ...

class DeleteM365GroupResult(_message.Message):
    __slots__ = ("graph_base_result",)
    GRAPH_BASE_RESULT_FIELD_NUMBER: _ClassVar[int]
    graph_base_result: GraphBaseResult
    def __init__(self, graph_base_result: _Optional[_Union[GraphBaseResult, _Mapping]] = ...) -> None: ...

class GetValidGroupOwnerArg(_message.Message):
    __slots__ = ("group_id", "retry_get_owners")
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    RETRY_GET_OWNERS_FIELD_NUMBER: _ClassVar[int]
    group_id: str
    retry_get_owners: bool
    def __init__(self, group_id: _Optional[str] = ..., retry_get_owners: bool = ...) -> None: ...

class GetValidGroupOwnerResult(_message.Message):
    __slots__ = ("valid_group_owner_smtp", "valid_group_owner_upn", "group_owners_id_vec", "group_owners_name_vec", "graph_error")
    VALID_GROUP_OWNER_SMTP_FIELD_NUMBER: _ClassVar[int]
    VALID_GROUP_OWNER_UPN_FIELD_NUMBER: _ClassVar[int]
    GROUP_OWNERS_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    GROUP_OWNERS_NAME_VEC_FIELD_NUMBER: _ClassVar[int]
    GRAPH_ERROR_FIELD_NUMBER: _ClassVar[int]
    valid_group_owner_smtp: str
    valid_group_owner_upn: str
    group_owners_id_vec: _containers.RepeatedScalarFieldContainer[str]
    group_owners_name_vec: _containers.RepeatedScalarFieldContainer[str]
    graph_error: _graph_pb2.GraphError
    def __init__(self, valid_group_owner_smtp: _Optional[str] = ..., valid_group_owner_upn: _Optional[str] = ..., group_owners_id_vec: _Optional[_Iterable[str]] = ..., group_owners_name_vec: _Optional[_Iterable[str]] = ..., graph_error: _Optional[_Union[_graph_pb2.GraphError, _Mapping]] = ...) -> None: ...

class GetListMessagesArg(_message.Message):
    __slots__ = ("user_id", "parent_folder", "max_pages_to_fetch", "fetch_changes_in_pages", "next_link", "is_fetch_limited_fields")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    PARENT_FOLDER_FIELD_NUMBER: _ClassVar[int]
    MAX_PAGES_TO_FETCH_FIELD_NUMBER: _ClassVar[int]
    FETCH_CHANGES_IN_PAGES_FIELD_NUMBER: _ClassVar[int]
    NEXT_LINK_FIELD_NUMBER: _ClassVar[int]
    IS_FETCH_LIMITED_FIELDS_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    parent_folder: str
    max_pages_to_fetch: int
    fetch_changes_in_pages: bool
    next_link: str
    is_fetch_limited_fields: bool
    def __init__(self, user_id: _Optional[str] = ..., parent_folder: _Optional[str] = ..., max_pages_to_fetch: _Optional[int] = ..., fetch_changes_in_pages: bool = ..., next_link: _Optional[str] = ..., is_fetch_limited_fields: bool = ...) -> None: ...

class GetListMessagesResult(_message.Message):
    __slots__ = ("message_list_vec", "graph_error", "next_link", "graph_base_result")
    MESSAGE_LIST_VEC_FIELD_NUMBER: _ClassVar[int]
    GRAPH_ERROR_FIELD_NUMBER: _ClassVar[int]
    NEXT_LINK_FIELD_NUMBER: _ClassVar[int]
    GRAPH_BASE_RESULT_FIELD_NUMBER: _ClassVar[int]
    message_list_vec: _containers.RepeatedCompositeFieldContainer[_graph_pb2.EmailItem]
    graph_error: _graph_pb2.GraphError
    next_link: str
    graph_base_result: GraphBaseResult
    def __init__(self, message_list_vec: _Optional[_Iterable[_Union[_graph_pb2.EmailItem, _Mapping]]] = ..., graph_error: _Optional[_Union[_graph_pb2.GraphError, _Mapping]] = ..., next_link: _Optional[str] = ..., graph_base_result: _Optional[_Union[GraphBaseResult, _Mapping]] = ...) -> None: ...

class GetMessageArg(_message.Message):
    __slots__ = ("user_id", "message_id", "parent_folder", "is_fetch_limited_fields")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    PARENT_FOLDER_FIELD_NUMBER: _ClassVar[int]
    IS_FETCH_LIMITED_FIELDS_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    message_id: str
    parent_folder: str
    is_fetch_limited_fields: bool
    def __init__(self, user_id: _Optional[str] = ..., message_id: _Optional[str] = ..., parent_folder: _Optional[str] = ..., is_fetch_limited_fields: bool = ...) -> None: ...

class GetMessageResult(_message.Message):
    __slots__ = ("message", "graph_error", "graph_base_result")
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    GRAPH_ERROR_FIELD_NUMBER: _ClassVar[int]
    GRAPH_BASE_RESULT_FIELD_NUMBER: _ClassVar[int]
    message: _graph_pb2.EmailItem
    graph_error: _graph_pb2.GraphError
    graph_base_result: GraphBaseResult
    def __init__(self, message: _Optional[_Union[_graph_pb2.EmailItem, _Mapping]] = ..., graph_error: _Optional[_Union[_graph_pb2.GraphError, _Mapping]] = ..., graph_base_result: _Optional[_Union[GraphBaseResult, _Mapping]] = ...) -> None: ...

class GetChatMessagesArg(_message.Message):
    __slots__ = ("team_id", "user_id", "time_range", "next_link")
    class TimeRange(_message.Message):
        __slots__ = ("inclusive_lower_bound_millis", "exclusive_upper_bound_millis")
        INCLUSIVE_LOWER_BOUND_MILLIS_FIELD_NUMBER: _ClassVar[int]
        EXCLUSIVE_UPPER_BOUND_MILLIS_FIELD_NUMBER: _ClassVar[int]
        inclusive_lower_bound_millis: int
        exclusive_upper_bound_millis: int
        def __init__(self, inclusive_lower_bound_millis: _Optional[int] = ..., exclusive_upper_bound_millis: _Optional[int] = ...) -> None: ...
    TEAM_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    TIME_RANGE_FIELD_NUMBER: _ClassVar[int]
    NEXT_LINK_FIELD_NUMBER: _ClassVar[int]
    team_id: str
    user_id: str
    time_range: GetChatMessagesArg.TimeRange
    next_link: str
    def __init__(self, team_id: _Optional[str] = ..., user_id: _Optional[str] = ..., time_range: _Optional[_Union[GetChatMessagesArg.TimeRange, _Mapping]] = ..., next_link: _Optional[str] = ...) -> None: ...

class GetChatMessagesResult(_message.Message):
    __slots__ = ("messages", "next_link", "graph_error", "graph_base_result")
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    NEXT_LINK_FIELD_NUMBER: _ClassVar[int]
    GRAPH_ERROR_FIELD_NUMBER: _ClassVar[int]
    GRAPH_BASE_RESULT_FIELD_NUMBER: _ClassVar[int]
    messages: _containers.RepeatedCompositeFieldContainer[_struct_pb2.Struct]
    next_link: str
    graph_error: _graph_pb2.GraphError
    graph_base_result: GraphBaseResult
    def __init__(self, messages: _Optional[_Iterable[_Union[_struct_pb2.Struct, _Mapping]]] = ..., next_link: _Optional[str] = ..., graph_error: _Optional[_Union[_graph_pb2.GraphError, _Mapping]] = ..., graph_base_result: _Optional[_Union[GraphBaseResult, _Mapping]] = ...) -> None: ...

class GetChatInfoArg(_message.Message):
    __slots__ = ("chat_id", "user_id")
    CHAT_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    chat_id: str
    user_id: str
    def __init__(self, chat_id: _Optional[str] = ..., user_id: _Optional[str] = ...) -> None: ...

class GetChatInfoResult(_message.Message):
    __slots__ = ("chat", "graph_error", "graph_base_result")
    CHAT_FIELD_NUMBER: _ClassVar[int]
    GRAPH_ERROR_FIELD_NUMBER: _ClassVar[int]
    GRAPH_BASE_RESULT_FIELD_NUMBER: _ClassVar[int]
    chat: _graph_pb2.Chat
    graph_error: _graph_pb2.GraphError
    graph_base_result: GraphBaseResult
    def __init__(self, chat: _Optional[_Union[_graph_pb2.Chat, _Mapping]] = ..., graph_error: _Optional[_Union[_graph_pb2.GraphError, _Mapping]] = ..., graph_base_result: _Optional[_Union[GraphBaseResult, _Mapping]] = ...) -> None: ...
