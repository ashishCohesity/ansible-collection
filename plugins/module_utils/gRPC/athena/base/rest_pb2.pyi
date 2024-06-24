from athena.base import athena_pb2 as _athena_pb2
from athena.base import kubernetes_config_pb2 as _kubernetes_config_pb2
from athena.base import kubernetes_pb2 as _kubernetes_pb2
from athena.base import error_pb2 as _error_pb2
from athena.base import athenamount_pb2 as _athenamount_pb2
from athena.server.master import master_pb2 as _master_pb2
from bridge.view_keeper import view_metadata_pb2 as _view_metadata_pb2
from configs import cluster_config_pb2 as _cluster_config_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AthenaRestUrlEndpointsProto(_message.Message):
    __slots__ = ("launch_app_instance", "terminate_app_instance", "pause_app_instance", "resume_app_instance", "upgrade_app_instance", "get_app_instance", "get_all_app_instances", "update_app_instance_settings", "get_all_installed_apps", "install_app", "uninstall_app", "athena_mount", "athena_unmount", "athena_view_validate", "athena_lookup_master", "get_app_privileges", "athena_cleanup_status", "get_iris_access_token", "get_app_settings", "get_pod_uid", "create_volume", "get_volume", "delete_volume", "virtualization_support_required", "replace_app_spec", "validate_protection_source", "allocate_pod_networking_info", "get_pod_networking_info", "release_pod_networking_info", "replace_app_container_image", "update_incarnation_id", "create_bifrost_network", "delete_bifrost_network", "get_all_installed_system_apps", "launch_bifrost_app", "update_bifrost_app", "terminate_bifrost_app", "get_all_networking_info", "launch_system_app", "terminate_system_app", "get_system_app_status", "update_system_service_app_info", "app_view_create", "app_view_get", "app_view_delete", "resources_available", "add_object", "delete_object", "edit_app_config_json", "get_app_config_json", "get_k8s_cluster_config", "get_athena_config")
    LAUNCH_APP_INSTANCE_FIELD_NUMBER: _ClassVar[int]
    TERMINATE_APP_INSTANCE_FIELD_NUMBER: _ClassVar[int]
    PAUSE_APP_INSTANCE_FIELD_NUMBER: _ClassVar[int]
    RESUME_APP_INSTANCE_FIELD_NUMBER: _ClassVar[int]
    UPGRADE_APP_INSTANCE_FIELD_NUMBER: _ClassVar[int]
    GET_APP_INSTANCE_FIELD_NUMBER: _ClassVar[int]
    GET_ALL_APP_INSTANCES_FIELD_NUMBER: _ClassVar[int]
    UPDATE_APP_INSTANCE_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    GET_ALL_INSTALLED_APPS_FIELD_NUMBER: _ClassVar[int]
    INSTALL_APP_FIELD_NUMBER: _ClassVar[int]
    UNINSTALL_APP_FIELD_NUMBER: _ClassVar[int]
    ATHENA_MOUNT_FIELD_NUMBER: _ClassVar[int]
    ATHENA_UNMOUNT_FIELD_NUMBER: _ClassVar[int]
    ATHENA_VIEW_VALIDATE_FIELD_NUMBER: _ClassVar[int]
    ATHENA_LOOKUP_MASTER_FIELD_NUMBER: _ClassVar[int]
    GET_APP_PRIVILEGES_FIELD_NUMBER: _ClassVar[int]
    ATHENA_CLEANUP_STATUS_FIELD_NUMBER: _ClassVar[int]
    GET_IRIS_ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    GET_APP_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    GET_POD_UID_FIELD_NUMBER: _ClassVar[int]
    CREATE_VOLUME_FIELD_NUMBER: _ClassVar[int]
    GET_VOLUME_FIELD_NUMBER: _ClassVar[int]
    DELETE_VOLUME_FIELD_NUMBER: _ClassVar[int]
    VIRTUALIZATION_SUPPORT_REQUIRED_FIELD_NUMBER: _ClassVar[int]
    REPLACE_APP_SPEC_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_PROTECTION_SOURCE_FIELD_NUMBER: _ClassVar[int]
    ALLOCATE_POD_NETWORKING_INFO_FIELD_NUMBER: _ClassVar[int]
    GET_POD_NETWORKING_INFO_FIELD_NUMBER: _ClassVar[int]
    RELEASE_POD_NETWORKING_INFO_FIELD_NUMBER: _ClassVar[int]
    REPLACE_APP_CONTAINER_IMAGE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    CREATE_BIFROST_NETWORK_FIELD_NUMBER: _ClassVar[int]
    DELETE_BIFROST_NETWORK_FIELD_NUMBER: _ClassVar[int]
    GET_ALL_INSTALLED_SYSTEM_APPS_FIELD_NUMBER: _ClassVar[int]
    LAUNCH_BIFROST_APP_FIELD_NUMBER: _ClassVar[int]
    UPDATE_BIFROST_APP_FIELD_NUMBER: _ClassVar[int]
    TERMINATE_BIFROST_APP_FIELD_NUMBER: _ClassVar[int]
    GET_ALL_NETWORKING_INFO_FIELD_NUMBER: _ClassVar[int]
    LAUNCH_SYSTEM_APP_FIELD_NUMBER: _ClassVar[int]
    TERMINATE_SYSTEM_APP_FIELD_NUMBER: _ClassVar[int]
    GET_SYSTEM_APP_STATUS_FIELD_NUMBER: _ClassVar[int]
    UPDATE_SYSTEM_SERVICE_APP_INFO_FIELD_NUMBER: _ClassVar[int]
    APP_VIEW_CREATE_FIELD_NUMBER: _ClassVar[int]
    APP_VIEW_GET_FIELD_NUMBER: _ClassVar[int]
    APP_VIEW_DELETE_FIELD_NUMBER: _ClassVar[int]
    RESOURCES_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    ADD_OBJECT_FIELD_NUMBER: _ClassVar[int]
    DELETE_OBJECT_FIELD_NUMBER: _ClassVar[int]
    EDIT_APP_CONFIG_JSON_FIELD_NUMBER: _ClassVar[int]
    GET_APP_CONFIG_JSON_FIELD_NUMBER: _ClassVar[int]
    GET_K8S_CLUSTER_CONFIG_FIELD_NUMBER: _ClassVar[int]
    GET_ATHENA_CONFIG_FIELD_NUMBER: _ClassVar[int]
    launch_app_instance: str
    terminate_app_instance: str
    pause_app_instance: str
    resume_app_instance: str
    upgrade_app_instance: str
    get_app_instance: str
    get_all_app_instances: str
    update_app_instance_settings: str
    get_all_installed_apps: str
    install_app: str
    uninstall_app: str
    athena_mount: str
    athena_unmount: str
    athena_view_validate: str
    athena_lookup_master: str
    get_app_privileges: str
    athena_cleanup_status: str
    get_iris_access_token: str
    get_app_settings: str
    get_pod_uid: str
    create_volume: str
    get_volume: str
    delete_volume: str
    virtualization_support_required: str
    replace_app_spec: str
    validate_protection_source: str
    allocate_pod_networking_info: str
    get_pod_networking_info: str
    release_pod_networking_info: str
    replace_app_container_image: str
    update_incarnation_id: str
    create_bifrost_network: str
    delete_bifrost_network: str
    get_all_installed_system_apps: str
    launch_bifrost_app: str
    update_bifrost_app: str
    terminate_bifrost_app: str
    get_all_networking_info: str
    launch_system_app: str
    terminate_system_app: str
    get_system_app_status: str
    update_system_service_app_info: str
    app_view_create: str
    app_view_get: str
    app_view_delete: str
    resources_available: str
    add_object: str
    delete_object: str
    edit_app_config_json: str
    get_app_config_json: str
    get_k8s_cluster_config: str
    get_athena_config: str
    def __init__(self, launch_app_instance: _Optional[str] = ..., terminate_app_instance: _Optional[str] = ..., pause_app_instance: _Optional[str] = ..., resume_app_instance: _Optional[str] = ..., upgrade_app_instance: _Optional[str] = ..., get_app_instance: _Optional[str] = ..., get_all_app_instances: _Optional[str] = ..., update_app_instance_settings: _Optional[str] = ..., get_all_installed_apps: _Optional[str] = ..., install_app: _Optional[str] = ..., uninstall_app: _Optional[str] = ..., athena_mount: _Optional[str] = ..., athena_unmount: _Optional[str] = ..., athena_view_validate: _Optional[str] = ..., athena_lookup_master: _Optional[str] = ..., get_app_privileges: _Optional[str] = ..., athena_cleanup_status: _Optional[str] = ..., get_iris_access_token: _Optional[str] = ..., get_app_settings: _Optional[str] = ..., get_pod_uid: _Optional[str] = ..., create_volume: _Optional[str] = ..., get_volume: _Optional[str] = ..., delete_volume: _Optional[str] = ..., virtualization_support_required: _Optional[str] = ..., replace_app_spec: _Optional[str] = ..., validate_protection_source: _Optional[str] = ..., allocate_pod_networking_info: _Optional[str] = ..., get_pod_networking_info: _Optional[str] = ..., release_pod_networking_info: _Optional[str] = ..., replace_app_container_image: _Optional[str] = ..., update_incarnation_id: _Optional[str] = ..., create_bifrost_network: _Optional[str] = ..., delete_bifrost_network: _Optional[str] = ..., get_all_installed_system_apps: _Optional[str] = ..., launch_bifrost_app: _Optional[str] = ..., update_bifrost_app: _Optional[str] = ..., terminate_bifrost_app: _Optional[str] = ..., get_all_networking_info: _Optional[str] = ..., launch_system_app: _Optional[str] = ..., terminate_system_app: _Optional[str] = ..., get_system_app_status: _Optional[str] = ..., update_system_service_app_info: _Optional[str] = ..., app_view_create: _Optional[str] = ..., app_view_get: _Optional[str] = ..., app_view_delete: _Optional[str] = ..., resources_available: _Optional[str] = ..., add_object: _Optional[str] = ..., delete_object: _Optional[str] = ..., edit_app_config_json: _Optional[str] = ..., get_app_config_json: _Optional[str] = ..., get_k8s_cluster_config: _Optional[str] = ..., get_athena_config: _Optional[str] = ...) -> None: ...

class AthenaProxyRestUrlEndpointsProto(_message.Message):
    __slots__ = ("athena_mount", "get_app_settings", "get_iris_manageability_access_token", "volume_api", "protected_source_volume_info", "view_api_prefix", "view_api_suffix_clone", "resources_available", "add_object", "delete_object", "edit_app_config_json", "get_app_config_json")
    ATHENA_MOUNT_FIELD_NUMBER: _ClassVar[int]
    GET_APP_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    GET_IRIS_MANAGEABILITY_ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    VOLUME_API_FIELD_NUMBER: _ClassVar[int]
    PROTECTED_SOURCE_VOLUME_INFO_FIELD_NUMBER: _ClassVar[int]
    VIEW_API_PREFIX_FIELD_NUMBER: _ClassVar[int]
    VIEW_API_SUFFIX_CLONE_FIELD_NUMBER: _ClassVar[int]
    RESOURCES_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    ADD_OBJECT_FIELD_NUMBER: _ClassVar[int]
    DELETE_OBJECT_FIELD_NUMBER: _ClassVar[int]
    EDIT_APP_CONFIG_JSON_FIELD_NUMBER: _ClassVar[int]
    GET_APP_CONFIG_JSON_FIELD_NUMBER: _ClassVar[int]
    athena_mount: str
    get_app_settings: str
    get_iris_manageability_access_token: str
    volume_api: str
    protected_source_volume_info: str
    view_api_prefix: str
    view_api_suffix_clone: str
    resources_available: str
    add_object: str
    delete_object: str
    edit_app_config_json: str
    get_app_config_json: str
    def __init__(self, athena_mount: _Optional[str] = ..., get_app_settings: _Optional[str] = ..., get_iris_manageability_access_token: _Optional[str] = ..., volume_api: _Optional[str] = ..., protected_source_volume_info: _Optional[str] = ..., view_api_prefix: _Optional[str] = ..., view_api_suffix_clone: _Optional[str] = ..., resources_available: _Optional[str] = ..., add_object: _Optional[str] = ..., delete_object: _Optional[str] = ..., edit_app_config_json: _Optional[str] = ..., get_app_config_json: _Optional[str] = ...) -> None: ...

class AthenaProxyInternalRestUrlEndpointsProto(_message.Message):
    __slots__ = ("get_kubelet_mount_points", "cleanup_mount_points", "unmount_vm_volume")
    GET_KUBELET_MOUNT_POINTS_FIELD_NUMBER: _ClassVar[int]
    CLEANUP_MOUNT_POINTS_FIELD_NUMBER: _ClassVar[int]
    UNMOUNT_VM_VOLUME_FIELD_NUMBER: _ClassVar[int]
    get_kubelet_mount_points: str
    cleanup_mount_points: str
    unmount_vm_volume: str
    def __init__(self, get_kubelet_mount_points: _Optional[str] = ..., cleanup_mount_points: _Optional[str] = ..., unmount_vm_volume: _Optional[str] = ...) -> None: ...

class AthenaWatchdogRestUrlEndpointsProto(_message.Message):
    __slots__ = ("athena_heartbeat",)
    ATHENA_HEARTBEAT_FIELD_NUMBER: _ClassVar[int]
    athena_heartbeat: str
    def __init__(self, athena_heartbeat: _Optional[str] = ...) -> None: ...

class RestStatusProto(_message.Message):
    __slots__ = ("error", "error_message")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto.Type
    error_message: str
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto.Type, str]] = ..., error_message: _Optional[str] = ...) -> None: ...

class ValidateAppInstanceViewArg(_message.Message):
    __slots__ = ("athena_mount_proto", "app_instance_authentication_token", "pod_ip_addr", "ignore_view_access_check")
    ATHENA_MOUNT_PROTO_FIELD_NUMBER: _ClassVar[int]
    APP_INSTANCE_AUTHENTICATION_TOKEN_FIELD_NUMBER: _ClassVar[int]
    POD_IP_ADDR_FIELD_NUMBER: _ClassVar[int]
    IGNORE_VIEW_ACCESS_CHECK_FIELD_NUMBER: _ClassVar[int]
    athena_mount_proto: _athenamount_pb2.AthenaMountProto
    app_instance_authentication_token: str
    pod_ip_addr: str
    ignore_view_access_check: bool
    def __init__(self, athena_mount_proto: _Optional[_Union[_athenamount_pb2.AthenaMountProto, _Mapping]] = ..., app_instance_authentication_token: _Optional[str] = ..., pod_ip_addr: _Optional[str] = ..., ignore_view_access_check: bool = ...) -> None: ...

class ValidateAppInstanceViewResult(_message.Message):
    __slots__ = ("status", "view_box", "pod_uid", "view_box_id", "protocol_access_info")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    VIEW_BOX_FIELD_NUMBER: _ClassVar[int]
    POD_UID_FIELD_NUMBER: _ClassVar[int]
    VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
    PROTOCOL_ACCESS_INFO_FIELD_NUMBER: _ClassVar[int]
    status: RestStatusProto
    view_box: str
    pod_uid: str
    view_box_id: int
    protocol_access_info: _view_metadata_pb2.ViewIdMappingProto.ProtocolAccessInfo
    def __init__(self, status: _Optional[_Union[RestStatusProto, _Mapping]] = ..., view_box: _Optional[str] = ..., pod_uid: _Optional[str] = ..., view_box_id: _Optional[int] = ..., protocol_access_info: _Optional[_Union[_view_metadata_pb2.ViewIdMappingProto.ProtocolAccessInfo, _Mapping]] = ...) -> None: ...

class ValidateProtectionSourceArg(_message.Message):
    __slots__ = ("protection_source_id", "app_instance_authentication_token")
    PROTECTION_SOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    APP_INSTANCE_AUTHENTICATION_TOKEN_FIELD_NUMBER: _ClassVar[int]
    protection_source_id: int
    app_instance_authentication_token: str
    def __init__(self, protection_source_id: _Optional[int] = ..., app_instance_authentication_token: _Optional[str] = ...) -> None: ...

class ValidateProtectionSourceResult(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: RestStatusProto
    def __init__(self, status: _Optional[_Union[RestStatusProto, _Mapping]] = ...) -> None: ...

class RestAppInfoProto(_message.Message):
    __slots__ = ("app_uid", "app_version", "meta", "app_privileges_list", "state", "install_time_usecs", "uninstall_time_usecs", "state_detail", "external_ip_required", "external_network_info_list", "instance_size_list", "vm_name_info_list", "readiness_probe")
    APP_UID_FIELD_NUMBER: _ClassVar[int]
    APP_VERSION_FIELD_NUMBER: _ClassVar[int]
    META_FIELD_NUMBER: _ClassVar[int]
    APP_PRIVILEGES_LIST_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    INSTALL_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    UNINSTALL_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    STATE_DETAIL_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_IP_REQUIRED_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_NETWORK_INFO_LIST_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_SIZE_LIST_FIELD_NUMBER: _ClassVar[int]
    VM_NAME_INFO_LIST_FIELD_NUMBER: _ClassVar[int]
    READINESS_PROBE_FIELD_NUMBER: _ClassVar[int]
    app_uid: int
    app_version: int
    meta: _athena_pb2.AppMetaInfoProto
    app_privileges_list: _containers.RepeatedCompositeFieldContainer[_athena_pb2.AppPrivilegesProto]
    state: _athena_pb2.AppStateProto
    install_time_usecs: int
    uninstall_time_usecs: int
    state_detail: str
    external_ip_required: bool
    external_network_info_list: _containers.RepeatedCompositeFieldContainer[_athena_pb2.ExternalNetworkInfoProto]
    instance_size_list: _containers.RepeatedScalarFieldContainer[str]
    vm_name_info_list: _containers.RepeatedCompositeFieldContainer[_athena_pb2.VmNameInfoProto]
    readiness_probe: _master_pb2.AppProbe
    def __init__(self, app_uid: _Optional[int] = ..., app_version: _Optional[int] = ..., meta: _Optional[_Union[_athena_pb2.AppMetaInfoProto, _Mapping]] = ..., app_privileges_list: _Optional[_Iterable[_Union[_athena_pb2.AppPrivilegesProto, _Mapping]]] = ..., state: _Optional[_Union[_athena_pb2.AppStateProto, _Mapping]] = ..., install_time_usecs: _Optional[int] = ..., uninstall_time_usecs: _Optional[int] = ..., state_detail: _Optional[str] = ..., external_ip_required: bool = ..., external_network_info_list: _Optional[_Iterable[_Union[_athena_pb2.ExternalNetworkInfoProto, _Mapping]]] = ..., instance_size_list: _Optional[_Iterable[str]] = ..., vm_name_info_list: _Optional[_Iterable[_Union[_athena_pb2.VmNameInfoProto, _Mapping]]] = ..., readiness_probe: _Optional[_Union[_master_pb2.AppProbe, _Mapping]] = ...) -> None: ...

class RestAppInstanceStateProto(_message.Message):
    __slots__ = ("value",)
    class Value(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNotSet: _ClassVar[RestAppInstanceStateProto.Value]
        kInitializing: _ClassVar[RestAppInstanceStateProto.Value]
        kRunning: _ClassVar[RestAppInstanceStateProto.Value]
        kPausing: _ClassVar[RestAppInstanceStateProto.Value]
        kPaused: _ClassVar[RestAppInstanceStateProto.Value]
        kTerminating: _ClassVar[RestAppInstanceStateProto.Value]
        kTerminated: _ClassVar[RestAppInstanceStateProto.Value]
        kFailed: _ClassVar[RestAppInstanceStateProto.Value]
        kUnschedulable: _ClassVar[RestAppInstanceStateProto.Value]
        kNotHealthy: _ClassVar[RestAppInstanceStateProto.Value]
    kNotSet: RestAppInstanceStateProto.Value
    kInitializing: RestAppInstanceStateProto.Value
    kRunning: RestAppInstanceStateProto.Value
    kPausing: RestAppInstanceStateProto.Value
    kPaused: RestAppInstanceStateProto.Value
    kTerminating: RestAppInstanceStateProto.Value
    kTerminated: RestAppInstanceStateProto.Value
    kFailed: RestAppInstanceStateProto.Value
    kUnschedulable: RestAppInstanceStateProto.Value
    kNotHealthy: RestAppInstanceStateProto.Value
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: RestAppInstanceStateProto.Value
    def __init__(self, value: _Optional[_Union[RestAppInstanceStateProto.Value, str]] = ...) -> None: ...

class FailureReason(_message.Message):
    __slots__ = ("code", "summary", "detail")
    CODE_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    DETAIL_FIELD_NUMBER: _ClassVar[int]
    code: str
    summary: str
    detail: str
    def __init__(self, code: _Optional[str] = ..., summary: _Optional[str] = ..., detail: _Optional[str] = ...) -> None: ...

class RestAppInstanceProto(_message.Message):
    __slots__ = ("app_instance_id", "app_uid", "app_version", "app_name", "operational_state", "operational_state_detail", "health_status", "health_detail", "view_name", "node_port", "settings", "creation_uid", "description", "created_time_usecs", "duration_usecs", "app_access_token", "user", "app_instance_resources", "https_ui", "vm_groups_info", "ssh_key_info", "volume_health_status", "volume_health_detail", "dev_version", "external_network_info", "namespace_name", "instance_size", "tenant_id", "additional_networks", "ui_cluster_ip_svc_addr", "ui_cluster_ip_svc_port", "exposed_node_port_info", "deployment_parameters", "upgradable_newer_version_present", "events_list", "failure_reasons")
    class User(_message.Message):
        __slots__ = ("domain", "user_name")
        DOMAIN_FIELD_NUMBER: _ClassVar[int]
        USER_NAME_FIELD_NUMBER: _ClassVar[int]
        domain: str
        user_name: str
        def __init__(self, domain: _Optional[str] = ..., user_name: _Optional[str] = ...) -> None: ...
    class NetworkInfo(_message.Message):
        __slots__ = ("external_network_info", "name", "id")
        EXTERNAL_NETWORK_INFO_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        ID_FIELD_NUMBER: _ClassVar[int]
        external_network_info: _athena_pb2.ExternalNetworkInfoProto
        name: str
        id: str
        def __init__(self, external_network_info: _Optional[_Union[_athena_pb2.ExternalNetworkInfoProto, _Mapping]] = ..., name: _Optional[str] = ..., id: _Optional[str] = ...) -> None: ...
    APP_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    APP_UID_FIELD_NUMBER: _ClassVar[int]
    APP_VERSION_FIELD_NUMBER: _ClassVar[int]
    APP_NAME_FIELD_NUMBER: _ClassVar[int]
    OPERATIONAL_STATE_FIELD_NUMBER: _ClassVar[int]
    OPERATIONAL_STATE_DETAIL_FIELD_NUMBER: _ClassVar[int]
    HEALTH_STATUS_FIELD_NUMBER: _ClassVar[int]
    HEALTH_DETAIL_FIELD_NUMBER: _ClassVar[int]
    VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    NODE_PORT_FIELD_NUMBER: _ClassVar[int]
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    CREATION_UID_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CREATED_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    DURATION_USECS_FIELD_NUMBER: _ClassVar[int]
    APP_ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    APP_INSTANCE_RESOURCES_FIELD_NUMBER: _ClassVar[int]
    HTTPS_UI_FIELD_NUMBER: _ClassVar[int]
    VM_GROUPS_INFO_FIELD_NUMBER: _ClassVar[int]
    SSH_KEY_INFO_FIELD_NUMBER: _ClassVar[int]
    VOLUME_HEALTH_STATUS_FIELD_NUMBER: _ClassVar[int]
    VOLUME_HEALTH_DETAIL_FIELD_NUMBER: _ClassVar[int]
    DEV_VERSION_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_NETWORK_INFO_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_NAME_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_SIZE_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_NETWORKS_FIELD_NUMBER: _ClassVar[int]
    UI_CLUSTER_IP_SVC_ADDR_FIELD_NUMBER: _ClassVar[int]
    UI_CLUSTER_IP_SVC_PORT_FIELD_NUMBER: _ClassVar[int]
    EXPOSED_NODE_PORT_INFO_FIELD_NUMBER: _ClassVar[int]
    DEPLOYMENT_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    UPGRADABLE_NEWER_VERSION_PRESENT_FIELD_NUMBER: _ClassVar[int]
    EVENTS_LIST_FIELD_NUMBER: _ClassVar[int]
    FAILURE_REASONS_FIELD_NUMBER: _ClassVar[int]
    app_instance_id: int
    app_uid: int
    app_version: int
    app_name: str
    operational_state: RestAppInstanceStateProto
    operational_state_detail: str
    health_status: _athena_pb2.HealthStatusProto
    health_detail: str
    view_name: str
    node_port: int
    settings: _athena_pb2.AppInstanceSettingsProto
    creation_uid: str
    description: str
    created_time_usecs: int
    duration_usecs: int
    app_access_token: str
    user: RestAppInstanceProto.User
    app_instance_resources: _athena_pb2.AppInstanceResourcesProto
    https_ui: bool
    vm_groups_info: _containers.RepeatedCompositeFieldContainer[_athena_pb2.VMGroupProto]
    ssh_key_info: _athena_pb2.UserSshKeyInfo
    volume_health_status: _athena_pb2.HealthStatusProto
    volume_health_detail: str
    dev_version: str
    external_network_info: _athena_pb2.ExternalNetworkInfoProto
    namespace_name: str
    instance_size: str
    tenant_id: str
    additional_networks: _containers.RepeatedCompositeFieldContainer[RestAppInstanceProto.NetworkInfo]
    ui_cluster_ip_svc_addr: str
    ui_cluster_ip_svc_port: int
    exposed_node_port_info: _containers.RepeatedCompositeFieldContainer[_athena_pb2.NodePortInfoProto]
    deployment_parameters: str
    upgradable_newer_version_present: bool
    events_list: _kubernetes_pb2.EventListProto
    failure_reasons: _containers.RepeatedCompositeFieldContainer[FailureReason]
    def __init__(self, app_instance_id: _Optional[int] = ..., app_uid: _Optional[int] = ..., app_version: _Optional[int] = ..., app_name: _Optional[str] = ..., operational_state: _Optional[_Union[RestAppInstanceStateProto, _Mapping]] = ..., operational_state_detail: _Optional[str] = ..., health_status: _Optional[_Union[_athena_pb2.HealthStatusProto, _Mapping]] = ..., health_detail: _Optional[str] = ..., view_name: _Optional[str] = ..., node_port: _Optional[int] = ..., settings: _Optional[_Union[_athena_pb2.AppInstanceSettingsProto, _Mapping]] = ..., creation_uid: _Optional[str] = ..., description: _Optional[str] = ..., created_time_usecs: _Optional[int] = ..., duration_usecs: _Optional[int] = ..., app_access_token: _Optional[str] = ..., user: _Optional[_Union[RestAppInstanceProto.User, _Mapping]] = ..., app_instance_resources: _Optional[_Union[_athena_pb2.AppInstanceResourcesProto, _Mapping]] = ..., https_ui: bool = ..., vm_groups_info: _Optional[_Iterable[_Union[_athena_pb2.VMGroupProto, _Mapping]]] = ..., ssh_key_info: _Optional[_Union[_athena_pb2.UserSshKeyInfo, _Mapping]] = ..., volume_health_status: _Optional[_Union[_athena_pb2.HealthStatusProto, _Mapping]] = ..., volume_health_detail: _Optional[str] = ..., dev_version: _Optional[str] = ..., external_network_info: _Optional[_Union[_athena_pb2.ExternalNetworkInfoProto, _Mapping]] = ..., namespace_name: _Optional[str] = ..., instance_size: _Optional[str] = ..., tenant_id: _Optional[str] = ..., additional_networks: _Optional[_Iterable[_Union[RestAppInstanceProto.NetworkInfo, _Mapping]]] = ..., ui_cluster_ip_svc_addr: _Optional[str] = ..., ui_cluster_ip_svc_port: _Optional[int] = ..., exposed_node_port_info: _Optional[_Iterable[_Union[_athena_pb2.NodePortInfoProto, _Mapping]]] = ..., deployment_parameters: _Optional[str] = ..., upgradable_newer_version_present: bool = ..., events_list: _Optional[_Union[_kubernetes_pb2.EventListProto, _Mapping]] = ..., failure_reasons: _Optional[_Iterable[_Union[FailureReason, _Mapping]]] = ...) -> None: ...

class InstallAppArg(_message.Message):
    __slots__ = ("app_uid", "app_version", "app_package_file", "force_update", "pre_packaged_app")
    APP_UID_FIELD_NUMBER: _ClassVar[int]
    APP_VERSION_FIELD_NUMBER: _ClassVar[int]
    APP_PACKAGE_FILE_FIELD_NUMBER: _ClassVar[int]
    FORCE_UPDATE_FIELD_NUMBER: _ClassVar[int]
    PRE_PACKAGED_APP_FIELD_NUMBER: _ClassVar[int]
    app_uid: int
    app_version: int
    app_package_file: str
    force_update: bool
    pre_packaged_app: bool
    def __init__(self, app_uid: _Optional[int] = ..., app_version: _Optional[int] = ..., app_package_file: _Optional[str] = ..., force_update: bool = ..., pre_packaged_app: bool = ...) -> None: ...

class InstallAppResult(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: RestStatusProto
    def __init__(self, status: _Optional[_Union[RestStatusProto, _Mapping]] = ...) -> None: ...

class UninstallAppArg(_message.Message):
    __slots__ = ("app_uid", "app_version", "force_uninstall")
    APP_UID_FIELD_NUMBER: _ClassVar[int]
    APP_VERSION_FIELD_NUMBER: _ClassVar[int]
    FORCE_UNINSTALL_FIELD_NUMBER: _ClassVar[int]
    app_uid: int
    app_version: int
    force_uninstall: bool
    def __init__(self, app_uid: _Optional[int] = ..., app_version: _Optional[int] = ..., force_uninstall: bool = ...) -> None: ...

class UninstallAppResult(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: RestStatusProto
    def __init__(self, status: _Optional[_Union[RestStatusProto, _Mapping]] = ...) -> None: ...

class GetAllInstalledAppsResult(_message.Message):
    __slots__ = ("status", "apps")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    APPS_FIELD_NUMBER: _ClassVar[int]
    status: RestStatusProto
    apps: _containers.RepeatedCompositeFieldContainer[RestAppInfoProto]
    def __init__(self, status: _Optional[_Union[RestStatusProto, _Mapping]] = ..., apps: _Optional[_Iterable[_Union[RestAppInfoProto, _Mapping]]] = ...) -> None: ...

class LaunchAppInstanceArg(_message.Message):
    __slots__ = ("app_uid", "app_version", "settings", "creation_uid", "description", "user_info", "external_network_info", "instance_size", "bifrost_config", "tenant_id", "additional_networks", "deployment_parameters")
    class NetworkInfo(_message.Message):
        __slots__ = ("external_network_info", "name", "id")
        EXTERNAL_NETWORK_INFO_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        ID_FIELD_NUMBER: _ClassVar[int]
        external_network_info: _athena_pb2.ExternalNetworkInfoProto
        name: str
        id: str
        def __init__(self, external_network_info: _Optional[_Union[_athena_pb2.ExternalNetworkInfoProto, _Mapping]] = ..., name: _Optional[str] = ..., id: _Optional[str] = ...) -> None: ...
    APP_UID_FIELD_NUMBER: _ClassVar[int]
    APP_VERSION_FIELD_NUMBER: _ClassVar[int]
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    CREATION_UID_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    USER_INFO_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_NETWORK_INFO_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_SIZE_FIELD_NUMBER: _ClassVar[int]
    BIFROST_CONFIG_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_NETWORKS_FIELD_NUMBER: _ClassVar[int]
    DEPLOYMENT_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    app_uid: int
    app_version: int
    settings: _athena_pb2.AppInstanceSettingsProto
    creation_uid: str
    description: str
    user_info: _athena_pb2.UserInformation
    external_network_info: _athena_pb2.ExternalNetworkInfoProto
    instance_size: str
    bifrost_config: _athena_pb2.BifrostConfig
    tenant_id: str
    additional_networks: _containers.RepeatedCompositeFieldContainer[LaunchAppInstanceArg.NetworkInfo]
    deployment_parameters: str
    def __init__(self, app_uid: _Optional[int] = ..., app_version: _Optional[int] = ..., settings: _Optional[_Union[_athena_pb2.AppInstanceSettingsProto, _Mapping]] = ..., creation_uid: _Optional[str] = ..., description: _Optional[str] = ..., user_info: _Optional[_Union[_athena_pb2.UserInformation, _Mapping]] = ..., external_network_info: _Optional[_Union[_athena_pb2.ExternalNetworkInfoProto, _Mapping]] = ..., instance_size: _Optional[str] = ..., bifrost_config: _Optional[_Union[_athena_pb2.BifrostConfig, _Mapping]] = ..., tenant_id: _Optional[str] = ..., additional_networks: _Optional[_Iterable[_Union[LaunchAppInstanceArg.NetworkInfo, _Mapping]]] = ..., deployment_parameters: _Optional[str] = ...) -> None: ...

class LaunchAppInstanceResult(_message.Message):
    __slots__ = ("status", "app_instance_id")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    APP_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    status: RestStatusProto
    app_instance_id: int
    def __init__(self, status: _Optional[_Union[RestStatusProto, _Mapping]] = ..., app_instance_id: _Optional[int] = ...) -> None: ...

class UpdateAppInstanceSettingsArg(_message.Message):
    __slots__ = ("app_instance_id", "settings", "description")
    APP_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    app_instance_id: int
    settings: _athena_pb2.AppInstanceSettingsProto
    description: str
    def __init__(self, app_instance_id: _Optional[int] = ..., settings: _Optional[_Union[_athena_pb2.AppInstanceSettingsProto, _Mapping]] = ..., description: _Optional[str] = ...) -> None: ...

class UpdateAppInstanceSettingsResult(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: RestStatusProto
    def __init__(self, status: _Optional[_Union[RestStatusProto, _Mapping]] = ...) -> None: ...

class TerminateAppInstanceArg(_message.Message):
    __slots__ = ("app_instance_id",)
    APP_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    app_instance_id: int
    def __init__(self, app_instance_id: _Optional[int] = ...) -> None: ...

class TerminateAppInstanceResult(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: RestStatusProto
    def __init__(self, status: _Optional[_Union[RestStatusProto, _Mapping]] = ...) -> None: ...

class PauseAppInstanceArg(_message.Message):
    __slots__ = ("app_instance_id",)
    APP_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    app_instance_id: int
    def __init__(self, app_instance_id: _Optional[int] = ...) -> None: ...

class PauseAppInstanceResult(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: RestStatusProto
    def __init__(self, status: _Optional[_Union[RestStatusProto, _Mapping]] = ...) -> None: ...

class ResumeAppInstanceArg(_message.Message):
    __slots__ = ("app_instance_id",)
    APP_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    app_instance_id: int
    def __init__(self, app_instance_id: _Optional[int] = ...) -> None: ...

class ResumeAppInstanceResult(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: RestStatusProto
    def __init__(self, status: _Optional[_Union[RestStatusProto, _Mapping]] = ...) -> None: ...

class UpgradeAppInstanceArg(_message.Message):
    __slots__ = ("app_instance_id", "deployment_parameters")
    APP_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    DEPLOYMENT_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    app_instance_id: int
    deployment_parameters: str
    def __init__(self, app_instance_id: _Optional[int] = ..., deployment_parameters: _Optional[str] = ...) -> None: ...

class UpgradeAppInstanceResult(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: RestStatusProto
    def __init__(self, status: _Optional[_Union[RestStatusProto, _Mapping]] = ...) -> None: ...

class GetAppInstanceArg(_message.Message):
    __slots__ = ("app_instance_id", "app_instance_authentication_token")
    APP_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    APP_INSTANCE_AUTHENTICATION_TOKEN_FIELD_NUMBER: _ClassVar[int]
    app_instance_id: int
    app_instance_authentication_token: str
    def __init__(self, app_instance_id: _Optional[int] = ..., app_instance_authentication_token: _Optional[str] = ...) -> None: ...

class GetAppInstanceResult(_message.Message):
    __slots__ = ("status", "app_instance")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    APP_INSTANCE_FIELD_NUMBER: _ClassVar[int]
    status: RestStatusProto
    app_instance: RestAppInstanceProto
    def __init__(self, status: _Optional[_Union[RestStatusProto, _Mapping]] = ..., app_instance: _Optional[_Union[RestAppInstanceProto, _Mapping]] = ...) -> None: ...

class GetAllAppInstancesArg(_message.Message):
    __slots__ = ("user_info", "show_system_app")
    USER_INFO_FIELD_NUMBER: _ClassVar[int]
    SHOW_SYSTEM_APP_FIELD_NUMBER: _ClassVar[int]
    user_info: _athena_pb2.UserInformation
    show_system_app: bool
    def __init__(self, user_info: _Optional[_Union[_athena_pb2.UserInformation, _Mapping]] = ..., show_system_app: bool = ...) -> None: ...

class GetAllAppInstancesResult(_message.Message):
    __slots__ = ("status", "app_instance")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    APP_INSTANCE_FIELD_NUMBER: _ClassVar[int]
    status: RestStatusProto
    app_instance: _containers.RepeatedCompositeFieldContainer[RestAppInstanceProto]
    def __init__(self, status: _Optional[_Union[RestStatusProto, _Mapping]] = ..., app_instance: _Optional[_Iterable[_Union[RestAppInstanceProto, _Mapping]]] = ...) -> None: ...

class LookupMasterResult(_message.Message):
    __slots__ = ("status", "ip", "port")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    IP_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    status: RestStatusProto
    ip: str
    port: int
    def __init__(self, status: _Optional[_Union[RestStatusProto, _Mapping]] = ..., ip: _Optional[str] = ..., port: _Optional[int] = ...) -> None: ...

class GetAppSettingsArg(_message.Message):
    __slots__ = ("app_instance_authentication_token",)
    APP_INSTANCE_AUTHENTICATION_TOKEN_FIELD_NUMBER: _ClassVar[int]
    app_instance_authentication_token: str
    def __init__(self, app_instance_authentication_token: _Optional[str] = ...) -> None: ...

class GetAppSettingsResult(_message.Message):
    __slots__ = ("status", "user", "app_instance_settings")
    class User(_message.Message):
        __slots__ = ("domain", "user_name")
        DOMAIN_FIELD_NUMBER: _ClassVar[int]
        USER_NAME_FIELD_NUMBER: _ClassVar[int]
        domain: str
        user_name: str
        def __init__(self, domain: _Optional[str] = ..., user_name: _Optional[str] = ...) -> None: ...
    STATUS_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    APP_INSTANCE_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    status: RestStatusProto
    user: GetAppSettingsResult.User
    app_instance_settings: _athena_pb2.AppInstanceSettingsProto
    def __init__(self, status: _Optional[_Union[RestStatusProto, _Mapping]] = ..., user: _Optional[_Union[GetAppSettingsResult.User, _Mapping]] = ..., app_instance_settings: _Optional[_Union[_athena_pb2.AppInstanceSettingsProto, _Mapping]] = ...) -> None: ...

class CleanupStatusResult(_message.Message):
    __slots__ = ("status", "last_cleaned_incarnation_id")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    LAST_CLEANED_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    status: RestStatusProto
    last_cleaned_incarnation_id: int
    def __init__(self, status: _Optional[_Union[RestStatusProto, _Mapping]] = ..., last_cleaned_incarnation_id: _Optional[int] = ...) -> None: ...

class GetIrisAccessTokenArg(_message.Message):
    __slots__ = ("app_instance_token", "user_sid", "user_tenant_id", "user_name", "user_domain")
    APP_INSTANCE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    USER_SID_FIELD_NUMBER: _ClassVar[int]
    USER_TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    USER_DOMAIN_FIELD_NUMBER: _ClassVar[int]
    app_instance_token: _athena_pb2.AppInstanceTokenProto
    user_sid: str
    user_tenant_id: str
    user_name: str
    user_domain: str
    def __init__(self, app_instance_token: _Optional[_Union[_athena_pb2.AppInstanceTokenProto, _Mapping]] = ..., user_sid: _Optional[str] = ..., user_tenant_id: _Optional[str] = ..., user_name: _Optional[str] = ..., user_domain: _Optional[str] = ...) -> None: ...

class GetIrisAccessTokenResult(_message.Message):
    __slots__ = ("error_code", "error_msg", "iris_access_token", "token_type")
    ERROR_CODE_FIELD_NUMBER: _ClassVar[int]
    ERROR_MSG_FIELD_NUMBER: _ClassVar[int]
    IRIS_ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    TOKEN_TYPE_FIELD_NUMBER: _ClassVar[int]
    error_code: int
    error_msg: str
    iris_access_token: str
    token_type: str
    def __init__(self, error_code: _Optional[int] = ..., error_msg: _Optional[str] = ..., iris_access_token: _Optional[str] = ..., token_type: _Optional[str] = ...) -> None: ...

class GetPodUidArg(_message.Message):
    __slots__ = ("app_instance_authentication_token", "pod_ip_addr")
    APP_INSTANCE_AUTHENTICATION_TOKEN_FIELD_NUMBER: _ClassVar[int]
    POD_IP_ADDR_FIELD_NUMBER: _ClassVar[int]
    app_instance_authentication_token: str
    pod_ip_addr: str
    def __init__(self, app_instance_authentication_token: _Optional[str] = ..., pod_ip_addr: _Optional[str] = ...) -> None: ...

class GetPodUidResult(_message.Message):
    __slots__ = ("status", "pod_uid")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    POD_UID_FIELD_NUMBER: _ClassVar[int]
    status: RestStatusProto
    pod_uid: str
    def __init__(self, status: _Optional[_Union[RestStatusProto, _Mapping]] = ..., pod_uid: _Optional[str] = ...) -> None: ...

class GetKubeletMountPointsResult(_message.Message):
    __slots__ = ("status", "mount_point_info")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MOUNT_POINT_INFO_FIELD_NUMBER: _ClassVar[int]
    status: RestStatusProto
    mount_point_info: _containers.RepeatedCompositeFieldContainer[_athena_pb2.MountPointInfoProto]
    def __init__(self, status: _Optional[_Union[RestStatusProto, _Mapping]] = ..., mount_point_info: _Optional[_Iterable[_Union[_athena_pb2.MountPointInfoProto, _Mapping]]] = ...) -> None: ...

class CleanupMountPointsArg(_message.Message):
    __slots__ = ("mount_point_info",)
    MOUNT_POINT_INFO_FIELD_NUMBER: _ClassVar[int]
    mount_point_info: _containers.RepeatedCompositeFieldContainer[_athena_pb2.MountPointInfoProto]
    def __init__(self, mount_point_info: _Optional[_Iterable[_Union[_athena_pb2.MountPointInfoProto, _Mapping]]] = ...) -> None: ...

class CleanupMountPointsResult(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: RestStatusProto
    def __init__(self, status: _Optional[_Union[RestStatusProto, _Mapping]] = ...) -> None: ...

class UnmountVmVolumeArg(_message.Message):
    __slots__ = ("mount_point_info",)
    MOUNT_POINT_INFO_FIELD_NUMBER: _ClassVar[int]
    mount_point_info: _athena_pb2.MountPointInfoProto
    def __init__(self, mount_point_info: _Optional[_Union[_athena_pb2.MountPointInfoProto, _Mapping]] = ...) -> None: ...

class UnmountVmVolumeResult(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: RestStatusProto
    def __init__(self, status: _Optional[_Union[RestStatusProto, _Mapping]] = ...) -> None: ...

class AthenaHeartbeatArg(_message.Message):
    __slots__ = ("timestamp_msecs",)
    TIMESTAMP_MSECS_FIELD_NUMBER: _ClassVar[int]
    timestamp_msecs: int
    def __init__(self, timestamp_msecs: _Optional[int] = ...) -> None: ...

class AthenaHeartbeatResult(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: RestStatusProto
    def __init__(self, status: _Optional[_Union[RestStatusProto, _Mapping]] = ...) -> None: ...

class CreateVolumeArg(_message.Message):
    __slots__ = ("volume_name", "target_view", "app_instance_id", "app_instance_authentication_token", "volume_type", "volume_capacity_bytes", "volume_claim_ref", "volume_claim_ref_namespace", "disk_image_nfs_path", "app_disk_image_name", "disk_type", "sysprep_operations", "user_ssh_key_info", "swap_mountpoint", "create_kubernetes_persistent_volume", "is_storage_provisioner_volume", "retry_on_failure")
    class VolumeType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNotSet: _ClassVar[CreateVolumeArg.VolumeType]
        kNfs: _ClassVar[CreateVolumeArg.VolumeType]
        kIscsi: _ClassVar[CreateVolumeArg.VolumeType]
    kNotSet: CreateVolumeArg.VolumeType
    kNfs: CreateVolumeArg.VolumeType
    kIscsi: CreateVolumeArg.VolumeType
    class DiskType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kDiskTypeNotSet: _ClassVar[CreateVolumeArg.DiskType]
        kBoot: _ClassVar[CreateVolumeArg.DiskType]
        kData: _ClassVar[CreateVolumeArg.DiskType]
    kDiskTypeNotSet: CreateVolumeArg.DiskType
    kBoot: CreateVolumeArg.DiskType
    kData: CreateVolumeArg.DiskType
    class SysprepOperationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kOperNotSet: _ClassVar[CreateVolumeArg.SysprepOperationType]
        kAddUserSshKey: _ClassVar[CreateVolumeArg.SysprepOperationType]
        kAddSwapMountPoint: _ClassVar[CreateVolumeArg.SysprepOperationType]
        kAddVirtioDriver: _ClassVar[CreateVolumeArg.SysprepOperationType]
    kOperNotSet: CreateVolumeArg.SysprepOperationType
    kAddUserSshKey: CreateVolumeArg.SysprepOperationType
    kAddSwapMountPoint: CreateVolumeArg.SysprepOperationType
    kAddVirtioDriver: CreateVolumeArg.SysprepOperationType
    VOLUME_NAME_FIELD_NUMBER: _ClassVar[int]
    TARGET_VIEW_FIELD_NUMBER: _ClassVar[int]
    APP_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    APP_INSTANCE_AUTHENTICATION_TOKEN_FIELD_NUMBER: _ClassVar[int]
    VOLUME_TYPE_FIELD_NUMBER: _ClassVar[int]
    VOLUME_CAPACITY_BYTES_FIELD_NUMBER: _ClassVar[int]
    VOLUME_CLAIM_REF_FIELD_NUMBER: _ClassVar[int]
    VOLUME_CLAIM_REF_NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    DISK_IMAGE_NFS_PATH_FIELD_NUMBER: _ClassVar[int]
    APP_DISK_IMAGE_NAME_FIELD_NUMBER: _ClassVar[int]
    DISK_TYPE_FIELD_NUMBER: _ClassVar[int]
    SYSPREP_OPERATIONS_FIELD_NUMBER: _ClassVar[int]
    USER_SSH_KEY_INFO_FIELD_NUMBER: _ClassVar[int]
    SWAP_MOUNTPOINT_FIELD_NUMBER: _ClassVar[int]
    CREATE_KUBERNETES_PERSISTENT_VOLUME_FIELD_NUMBER: _ClassVar[int]
    IS_STORAGE_PROVISIONER_VOLUME_FIELD_NUMBER: _ClassVar[int]
    RETRY_ON_FAILURE_FIELD_NUMBER: _ClassVar[int]
    volume_name: str
    target_view: str
    app_instance_id: int
    app_instance_authentication_token: str
    volume_type: CreateVolumeArg.VolumeType
    volume_capacity_bytes: int
    volume_claim_ref: str
    volume_claim_ref_namespace: str
    disk_image_nfs_path: str
    app_disk_image_name: str
    disk_type: CreateVolumeArg.DiskType
    sysprep_operations: _containers.RepeatedScalarFieldContainer[CreateVolumeArg.SysprepOperationType]
    user_ssh_key_info: _containers.RepeatedCompositeFieldContainer[_athena_pb2.UserSshKeyInfo]
    swap_mountpoint: str
    create_kubernetes_persistent_volume: bool
    is_storage_provisioner_volume: bool
    retry_on_failure: bool
    def __init__(self, volume_name: _Optional[str] = ..., target_view: _Optional[str] = ..., app_instance_id: _Optional[int] = ..., app_instance_authentication_token: _Optional[str] = ..., volume_type: _Optional[_Union[CreateVolumeArg.VolumeType, str]] = ..., volume_capacity_bytes: _Optional[int] = ..., volume_claim_ref: _Optional[str] = ..., volume_claim_ref_namespace: _Optional[str] = ..., disk_image_nfs_path: _Optional[str] = ..., app_disk_image_name: _Optional[str] = ..., disk_type: _Optional[_Union[CreateVolumeArg.DiskType, str]] = ..., sysprep_operations: _Optional[_Iterable[_Union[CreateVolumeArg.SysprepOperationType, str]]] = ..., user_ssh_key_info: _Optional[_Iterable[_Union[_athena_pb2.UserSshKeyInfo, _Mapping]]] = ..., swap_mountpoint: _Optional[str] = ..., create_kubernetes_persistent_volume: bool = ..., is_storage_provisioner_volume: bool = ..., retry_on_failure: bool = ...) -> None: ...

class CreateVolumeResult(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: RestStatusProto
    def __init__(self, status: _Optional[_Union[RestStatusProto, _Mapping]] = ...) -> None: ...

class GetVolumeArg(_message.Message):
    __slots__ = ("volume_name", "app_instance_id", "app_instance_authentication_token", "app_instance_namespace")
    VOLUME_NAME_FIELD_NUMBER: _ClassVar[int]
    APP_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    APP_INSTANCE_AUTHENTICATION_TOKEN_FIELD_NUMBER: _ClassVar[int]
    APP_INSTANCE_NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    volume_name: str
    app_instance_id: int
    app_instance_authentication_token: str
    app_instance_namespace: str
    def __init__(self, volume_name: _Optional[str] = ..., app_instance_id: _Optional[int] = ..., app_instance_authentication_token: _Optional[str] = ..., app_instance_namespace: _Optional[str] = ...) -> None: ...

class GetVolumeResult(_message.Message):
    __slots__ = ("status", "volume_info")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    VOLUME_INFO_FIELD_NUMBER: _ClassVar[int]
    status: RestStatusProto
    volume_info: _athena_pb2.VolumeInfoProto
    def __init__(self, status: _Optional[_Union[RestStatusProto, _Mapping]] = ..., volume_info: _Optional[_Union[_athena_pb2.VolumeInfoProto, _Mapping]] = ...) -> None: ...

class DeleteVolumeArg(_message.Message):
    __slots__ = ("volume_name", "app_instance_id", "app_instance_authentication_token", "app_instance_namespace")
    VOLUME_NAME_FIELD_NUMBER: _ClassVar[int]
    APP_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    APP_INSTANCE_AUTHENTICATION_TOKEN_FIELD_NUMBER: _ClassVar[int]
    APP_INSTANCE_NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    volume_name: str
    app_instance_id: int
    app_instance_authentication_token: str
    app_instance_namespace: str
    def __init__(self, volume_name: _Optional[str] = ..., app_instance_id: _Optional[int] = ..., app_instance_authentication_token: _Optional[str] = ..., app_instance_namespace: _Optional[str] = ...) -> None: ...

class DeleteVolumeResult(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: RestStatusProto
    def __init__(self, status: _Optional[_Union[RestStatusProto, _Mapping]] = ...) -> None: ...

class AppViewCreateArg(_message.Message):
    __slots__ = ("request_id", "app_instance_authentication_token", "app_instance_id", "app_instance_namespace", "view_box_id", "view_type", "retry_on_failure", "view_name", "source_view_name", "pod_uid")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNotSet: _ClassVar[AppViewCreateArg.Type]
        kClone: _ClassVar[AppViewCreateArg.Type]
    kNotSet: AppViewCreateArg.Type
    kClone: AppViewCreateArg.Type
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    APP_INSTANCE_AUTHENTICATION_TOKEN_FIELD_NUMBER: _ClassVar[int]
    APP_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    APP_INSTANCE_NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_TYPE_FIELD_NUMBER: _ClassVar[int]
    RETRY_ON_FAILURE_FIELD_NUMBER: _ClassVar[int]
    VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    SOURCE_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    POD_UID_FIELD_NUMBER: _ClassVar[int]
    request_id: str
    app_instance_authentication_token: str
    app_instance_id: int
    app_instance_namespace: str
    view_box_id: int
    view_type: AppViewCreateArg.Type
    retry_on_failure: bool
    view_name: str
    source_view_name: str
    pod_uid: str
    def __init__(self, request_id: _Optional[str] = ..., app_instance_authentication_token: _Optional[str] = ..., app_instance_id: _Optional[int] = ..., app_instance_namespace: _Optional[str] = ..., view_box_id: _Optional[int] = ..., view_type: _Optional[_Union[AppViewCreateArg.Type, str]] = ..., retry_on_failure: bool = ..., view_name: _Optional[str] = ..., source_view_name: _Optional[str] = ..., pod_uid: _Optional[str] = ...) -> None: ...

class AppViewCreateResult(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: RestStatusProto
    def __init__(self, status: _Optional[_Union[RestStatusProto, _Mapping]] = ...) -> None: ...

class AppViewGetArg(_message.Message):
    __slots__ = ("request_id", "app_instance_authentication_token", "app_instance_id", "app_instance_namespace", "view_box_id", "view_name", "source_view_name", "pod_uid")
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    APP_INSTANCE_AUTHENTICATION_TOKEN_FIELD_NUMBER: _ClassVar[int]
    APP_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    APP_INSTANCE_NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    SOURCE_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    POD_UID_FIELD_NUMBER: _ClassVar[int]
    request_id: str
    app_instance_authentication_token: str
    app_instance_id: int
    app_instance_namespace: str
    view_box_id: int
    view_name: str
    source_view_name: str
    pod_uid: str
    def __init__(self, request_id: _Optional[str] = ..., app_instance_authentication_token: _Optional[str] = ..., app_instance_id: _Optional[int] = ..., app_instance_namespace: _Optional[str] = ..., view_box_id: _Optional[int] = ..., view_name: _Optional[str] = ..., source_view_name: _Optional[str] = ..., pod_uid: _Optional[str] = ...) -> None: ...

class AppViewGetResult(_message.Message):
    __slots__ = ("status", "app_view_info")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    APP_VIEW_INFO_FIELD_NUMBER: _ClassVar[int]
    status: RestStatusProto
    app_view_info: _athena_pb2.AppViewInfoProto
    def __init__(self, status: _Optional[_Union[RestStatusProto, _Mapping]] = ..., app_view_info: _Optional[_Union[_athena_pb2.AppViewInfoProto, _Mapping]] = ...) -> None: ...

class AppViewDeleteArg(_message.Message):
    __slots__ = ("request_id", "app_instance_authentication_token", "app_instance_id", "app_instance_namespace", "view_box_id", "view_name", "source_view_name", "pod_uid")
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    APP_INSTANCE_AUTHENTICATION_TOKEN_FIELD_NUMBER: _ClassVar[int]
    APP_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    APP_INSTANCE_NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    SOURCE_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    POD_UID_FIELD_NUMBER: _ClassVar[int]
    request_id: str
    app_instance_authentication_token: str
    app_instance_id: int
    app_instance_namespace: str
    view_box_id: int
    view_name: str
    source_view_name: str
    pod_uid: str
    def __init__(self, request_id: _Optional[str] = ..., app_instance_authentication_token: _Optional[str] = ..., app_instance_id: _Optional[int] = ..., app_instance_namespace: _Optional[str] = ..., view_box_id: _Optional[int] = ..., view_name: _Optional[str] = ..., source_view_name: _Optional[str] = ..., pod_uid: _Optional[str] = ...) -> None: ...

class AppViewDeleteResult(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: RestStatusProto
    def __init__(self, status: _Optional[_Union[RestStatusProto, _Mapping]] = ...) -> None: ...

class ValidateVirtualizationSupportResult(_message.Message):
    __slots__ = ("status", "virtualization_support_required")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    VIRTUALIZATION_SUPPORT_REQUIRED_FIELD_NUMBER: _ClassVar[int]
    status: RestStatusProto
    virtualization_support_required: bool
    def __init__(self, status: _Optional[_Union[RestStatusProto, _Mapping]] = ..., virtualization_support_required: bool = ...) -> None: ...

class ReplaceAppSpecArg(_message.Message):
    __slots__ = ("container_app_spec_path", "vm_app_spec_path", "app_uid", "app_version")
    CONTAINER_APP_SPEC_PATH_FIELD_NUMBER: _ClassVar[int]
    VM_APP_SPEC_PATH_FIELD_NUMBER: _ClassVar[int]
    APP_UID_FIELD_NUMBER: _ClassVar[int]
    APP_VERSION_FIELD_NUMBER: _ClassVar[int]
    container_app_spec_path: str
    vm_app_spec_path: str
    app_uid: int
    app_version: int
    def __init__(self, container_app_spec_path: _Optional[str] = ..., vm_app_spec_path: _Optional[str] = ..., app_uid: _Optional[int] = ..., app_version: _Optional[int] = ...) -> None: ...

class ReplaceAppSpecResult(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: RestStatusProto
    def __init__(self, status: _Optional[_Union[RestStatusProto, _Mapping]] = ...) -> None: ...

class ReplaceAppContainerImageArg(_message.Message):
    __slots__ = ("app_uid", "app_version", "container_image_path")
    APP_UID_FIELD_NUMBER: _ClassVar[int]
    APP_VERSION_FIELD_NUMBER: _ClassVar[int]
    CONTAINER_IMAGE_PATH_FIELD_NUMBER: _ClassVar[int]
    app_uid: int
    app_version: int
    container_image_path: str
    def __init__(self, app_uid: _Optional[int] = ..., app_version: _Optional[int] = ..., container_image_path: _Optional[str] = ...) -> None: ...

class ReplaceAppContainerImageResult(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: RestStatusProto
    def __init__(self, status: _Optional[_Union[RestStatusProto, _Mapping]] = ...) -> None: ...

class AllocatePodNetworkingInfoArg(_message.Message):
    __slots__ = ("key",)
    KEY_FIELD_NUMBER: _ClassVar[int]
    key: _athena_pb2.PodNetworkingKeyProto
    def __init__(self, key: _Optional[_Union[_athena_pb2.PodNetworkingKeyProto, _Mapping]] = ...) -> None: ...

class AllocatePodNetworkingInfoResult(_message.Message):
    __slots__ = ("status", "pod_networking_info", "axon_network_access_info")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    POD_NETWORKING_INFO_FIELD_NUMBER: _ClassVar[int]
    AXON_NETWORK_ACCESS_INFO_FIELD_NUMBER: _ClassVar[int]
    status: RestStatusProto
    pod_networking_info: _athena_pb2.PodNetworkingInfoProto
    axon_network_access_info: _athena_pb2.AxonNetworkAccessInfoProto
    def __init__(self, status: _Optional[_Union[RestStatusProto, _Mapping]] = ..., pod_networking_info: _Optional[_Union[_athena_pb2.PodNetworkingInfoProto, _Mapping]] = ..., axon_network_access_info: _Optional[_Union[_athena_pb2.AxonNetworkAccessInfoProto, _Mapping]] = ...) -> None: ...

class GetPodNetworkingInfoArg(_message.Message):
    __slots__ = ("key",)
    KEY_FIELD_NUMBER: _ClassVar[int]
    key: _athena_pb2.PodNetworkingKeyProto
    def __init__(self, key: _Optional[_Union[_athena_pb2.PodNetworkingKeyProto, _Mapping]] = ...) -> None: ...

class GetPodNetworkingInfoResult(_message.Message):
    __slots__ = ("status", "pod_networking_info", "axon_network_access_info")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    POD_NETWORKING_INFO_FIELD_NUMBER: _ClassVar[int]
    AXON_NETWORK_ACCESS_INFO_FIELD_NUMBER: _ClassVar[int]
    status: RestStatusProto
    pod_networking_info: _athena_pb2.PodNetworkingInfoProto
    axon_network_access_info: _athena_pb2.AxonNetworkAccessInfoProto
    def __init__(self, status: _Optional[_Union[RestStatusProto, _Mapping]] = ..., pod_networking_info: _Optional[_Union[_athena_pb2.PodNetworkingInfoProto, _Mapping]] = ..., axon_network_access_info: _Optional[_Union[_athena_pb2.AxonNetworkAccessInfoProto, _Mapping]] = ...) -> None: ...

class ReleasePodNetworkingInfoArg(_message.Message):
    __slots__ = ("key",)
    KEY_FIELD_NUMBER: _ClassVar[int]
    key: _athena_pb2.PodNetworkingKeyProto
    def __init__(self, key: _Optional[_Union[_athena_pb2.PodNetworkingKeyProto, _Mapping]] = ...) -> None: ...

class ReleasePodNetworkingInfoResult(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: RestStatusProto
    def __init__(self, status: _Optional[_Union[RestStatusProto, _Mapping]] = ...) -> None: ...

class UpdateIncarnationIdArg(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UpdateIncarnationIdResult(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: RestStatusProto
    def __init__(self, status: _Optional[_Union[RestStatusProto, _Mapping]] = ...) -> None: ...

class CreateBifrostNetworkArg(_message.Message):
    __slots__ = ("tenant_id", "vlan_id", "host_iface_group", "network_name", "cni_type", "cni_ver", "ipam_type", "ipam_params", "access_info")
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    VLAN_ID_FIELD_NUMBER: _ClassVar[int]
    HOST_IFACE_GROUP_FIELD_NUMBER: _ClassVar[int]
    NETWORK_NAME_FIELD_NUMBER: _ClassVar[int]
    CNI_TYPE_FIELD_NUMBER: _ClassVar[int]
    CNI_VER_FIELD_NUMBER: _ClassVar[int]
    IPAM_TYPE_FIELD_NUMBER: _ClassVar[int]
    IPAM_PARAMS_FIELD_NUMBER: _ClassVar[int]
    ACCESS_INFO_FIELD_NUMBER: _ClassVar[int]
    tenant_id: str
    vlan_id: int
    host_iface_group: str
    network_name: str
    cni_type: str
    cni_ver: str
    ipam_type: str
    ipam_params: str
    access_info: _athena_pb2.AxonNetworkAccessInfoProto
    def __init__(self, tenant_id: _Optional[str] = ..., vlan_id: _Optional[int] = ..., host_iface_group: _Optional[str] = ..., network_name: _Optional[str] = ..., cni_type: _Optional[str] = ..., cni_ver: _Optional[str] = ..., ipam_type: _Optional[str] = ..., ipam_params: _Optional[str] = ..., access_info: _Optional[_Union[_athena_pb2.AxonNetworkAccessInfoProto, _Mapping]] = ...) -> None: ...

class CreateBifrostNetworkResult(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: RestStatusProto
    def __init__(self, status: _Optional[_Union[RestStatusProto, _Mapping]] = ...) -> None: ...

class DeleteBifrostNetworkArg(_message.Message):
    __slots__ = ("tenant_id", "vlan_id", "host_iface_group", "network_name")
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    VLAN_ID_FIELD_NUMBER: _ClassVar[int]
    HOST_IFACE_GROUP_FIELD_NUMBER: _ClassVar[int]
    NETWORK_NAME_FIELD_NUMBER: _ClassVar[int]
    tenant_id: str
    vlan_id: int
    host_iface_group: str
    network_name: str
    def __init__(self, tenant_id: _Optional[str] = ..., vlan_id: _Optional[int] = ..., host_iface_group: _Optional[str] = ..., network_name: _Optional[str] = ...) -> None: ...

class DeleteBifrostNetworkResult(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: RestStatusProto
    def __init__(self, status: _Optional[_Union[RestStatusProto, _Mapping]] = ...) -> None: ...

class GetAllNetworkingInfoArg(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetAllNetworkingInfoResult(_message.Message):
    __slots__ = ("status", "network_protos")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    NETWORK_PROTOS_FIELD_NUMBER: _ClassVar[int]
    status: RestStatusProto
    network_protos: _containers.RepeatedCompositeFieldContainer[_master_pb2.NetworkProto]
    def __init__(self, status: _Optional[_Union[RestStatusProto, _Mapping]] = ..., network_protos: _Optional[_Iterable[_Union[_master_pb2.NetworkProto, _Mapping]]] = ...) -> None: ...

class TerminateBifrostAppInstanceArg(_message.Message):
    __slots__ = ("tenant_id",)
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    tenant_id: str
    def __init__(self, tenant_id: _Optional[str] = ...) -> None: ...

class LaunchSystemAppInstanceArg(_message.Message):
    __slots__ = ("sys_app_uid", "launch_params")
    SYS_APP_UID_FIELD_NUMBER: _ClassVar[int]
    LAUNCH_PARAMS_FIELD_NUMBER: _ClassVar[int]
    sys_app_uid: int
    launch_params: str
    def __init__(self, sys_app_uid: _Optional[int] = ..., launch_params: _Optional[str] = ...) -> None: ...

class LaunchSystemAppInstanceResult(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: RestStatusProto
    def __init__(self, status: _Optional[_Union[RestStatusProto, _Mapping]] = ...) -> None: ...

class TerminateSystemAppInstanceArg(_message.Message):
    __slots__ = ("sys_app_uid",)
    SYS_APP_UID_FIELD_NUMBER: _ClassVar[int]
    sys_app_uid: int
    def __init__(self, sys_app_uid: _Optional[int] = ...) -> None: ...

class TerminateSystemAppInstanceResult(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: RestStatusProto
    def __init__(self, status: _Optional[_Union[RestStatusProto, _Mapping]] = ...) -> None: ...

class GetSystemAppStatusArg(_message.Message):
    __slots__ = ("sys_app_uid",)
    SYS_APP_UID_FIELD_NUMBER: _ClassVar[int]
    sys_app_uid: int
    def __init__(self, sys_app_uid: _Optional[int] = ...) -> None: ...

class GetSystemAppStatusResult(_message.Message):
    __slots__ = ("status", "app_status", "node_pod_status_vec", "pod_status_vec")
    class NodePodStatus(_message.Message):
        __slots__ = ("node_id", "node_ip", "pids")
        NODE_ID_FIELD_NUMBER: _ClassVar[int]
        NODE_IP_FIELD_NUMBER: _ClassVar[int]
        PIDS_FIELD_NUMBER: _ClassVar[int]
        node_id: int
        node_ip: str
        pids: _containers.RepeatedScalarFieldContainer[int]
        def __init__(self, node_id: _Optional[int] = ..., node_ip: _Optional[str] = ..., pids: _Optional[_Iterable[int]] = ...) -> None: ...
    class PodStatus(_message.Message):
        __slots__ = ("pod_uid", "pod_ip", "host_ip")
        POD_UID_FIELD_NUMBER: _ClassVar[int]
        POD_IP_FIELD_NUMBER: _ClassVar[int]
        HOST_IP_FIELD_NUMBER: _ClassVar[int]
        pod_uid: str
        pod_ip: str
        host_ip: str
        def __init__(self, pod_uid: _Optional[str] = ..., pod_ip: _Optional[str] = ..., host_ip: _Optional[str] = ...) -> None: ...
    STATUS_FIELD_NUMBER: _ClassVar[int]
    APP_STATUS_FIELD_NUMBER: _ClassVar[int]
    NODE_POD_STATUS_VEC_FIELD_NUMBER: _ClassVar[int]
    POD_STATUS_VEC_FIELD_NUMBER: _ClassVar[int]
    status: RestStatusProto
    app_status: RestAppInstanceStateProto
    node_pod_status_vec: _containers.RepeatedCompositeFieldContainer[GetSystemAppStatusResult.NodePodStatus]
    pod_status_vec: _containers.RepeatedCompositeFieldContainer[GetSystemAppStatusResult.PodStatus]
    def __init__(self, status: _Optional[_Union[RestStatusProto, _Mapping]] = ..., app_status: _Optional[_Union[RestAppInstanceStateProto, _Mapping]] = ..., node_pod_status_vec: _Optional[_Iterable[_Union[GetSystemAppStatusResult.NodePodStatus, _Mapping]]] = ..., pod_status_vec: _Optional[_Iterable[_Union[GetSystemAppStatusResult.PodStatus, _Mapping]]] = ...) -> None: ...

class AthenaMasterUpdateAppInfoArg(_message.Message):
    __slots__ = ("app_info",)
    APP_INFO_FIELD_NUMBER: _ClassVar[int]
    app_info: _master_pb2.AppInfoProto
    def __init__(self, app_info: _Optional[_Union[_master_pb2.AppInfoProto, _Mapping]] = ...) -> None: ...

class AthenaMasterUpdateAppInfoResult(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: RestStatusProto
    def __init__(self, status: _Optional[_Union[RestStatusProto, _Mapping]] = ...) -> None: ...

class ResourcesAvailableArg(_message.Message):
    __slots__ = ("app_instance_token",)
    APP_INSTANCE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    app_instance_token: _athena_pb2.AppInstanceTokenProto
    def __init__(self, app_instance_token: _Optional[_Union[_athena_pb2.AppInstanceTokenProto, _Mapping]] = ...) -> None: ...

class ResourcesAvailableResult(_message.Message):
    __slots__ = ("status", "resources_available")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    RESOURCES_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    status: RestStatusProto
    resources_available: ResourcesAvailableProto
    def __init__(self, status: _Optional[_Union[RestStatusProto, _Mapping]] = ..., resources_available: _Optional[_Union[ResourcesAvailableProto, _Mapping]] = ...) -> None: ...

class ResourcesAvailableProto(_message.Message):
    __slots__ = ("limits_available", "requests_available")
    LIMITS_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    REQUESTS_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    limits_available: CpuMemoryProto
    requests_available: CpuMemoryProto
    def __init__(self, limits_available: _Optional[_Union[CpuMemoryProto, _Mapping]] = ..., requests_available: _Optional[_Union[CpuMemoryProto, _Mapping]] = ...) -> None: ...

class CpuMemoryProto(_message.Message):
    __slots__ = ("memory", "cpu")
    MEMORY_FIELD_NUMBER: _ClassVar[int]
    CPU_FIELD_NUMBER: _ClassVar[int]
    memory: str
    cpu: str
    def __init__(self, memory: _Optional[str] = ..., cpu: _Optional[str] = ...) -> None: ...

class AddObjectArg(_message.Message):
    __slots__ = ("yaml_data", "app_instance_token")
    YAML_DATA_FIELD_NUMBER: _ClassVar[int]
    APP_INSTANCE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    yaml_data: bytes
    app_instance_token: _athena_pb2.AppInstanceTokenProto
    def __init__(self, yaml_data: _Optional[bytes] = ..., app_instance_token: _Optional[_Union[_athena_pb2.AppInstanceTokenProto, _Mapping]] = ...) -> None: ...

class AddObjectResult(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: RestStatusProto
    def __init__(self, status: _Optional[_Union[RestStatusProto, _Mapping]] = ...) -> None: ...

class DeleteObjectArg(_message.Message):
    __slots__ = ("object_kind", "object_name", "app_instance_token")
    OBJECT_KIND_FIELD_NUMBER: _ClassVar[int]
    OBJECT_NAME_FIELD_NUMBER: _ClassVar[int]
    APP_INSTANCE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    object_kind: str
    object_name: str
    app_instance_token: _athena_pb2.AppInstanceTokenProto
    def __init__(self, object_kind: _Optional[str] = ..., object_name: _Optional[str] = ..., app_instance_token: _Optional[_Union[_athena_pb2.AppInstanceTokenProto, _Mapping]] = ...) -> None: ...

class DeleteObjectResult(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: RestStatusProto
    def __init__(self, status: _Optional[_Union[RestStatusProto, _Mapping]] = ...) -> None: ...

class EditAppConfigJsonArg(_message.Message):
    __slots__ = ("app_config_json_data", "app_uid", "app_version")
    APP_CONFIG_JSON_DATA_FIELD_NUMBER: _ClassVar[int]
    APP_UID_FIELD_NUMBER: _ClassVar[int]
    APP_VERSION_FIELD_NUMBER: _ClassVar[int]
    app_config_json_data: str
    app_uid: int
    app_version: int
    def __init__(self, app_config_json_data: _Optional[str] = ..., app_uid: _Optional[int] = ..., app_version: _Optional[int] = ...) -> None: ...

class EditAppConfigJsonResult(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: RestStatusProto
    def __init__(self, status: _Optional[_Union[RestStatusProto, _Mapping]] = ...) -> None: ...

class GetAppConfigJsonArg(_message.Message):
    __slots__ = ("app_uid", "app_version")
    APP_UID_FIELD_NUMBER: _ClassVar[int]
    APP_VERSION_FIELD_NUMBER: _ClassVar[int]
    app_uid: int
    app_version: int
    def __init__(self, app_uid: _Optional[int] = ..., app_version: _Optional[int] = ...) -> None: ...

class GetAppConfigJsonResult(_message.Message):
    __slots__ = ("app_config_json_data", "status")
    APP_CONFIG_JSON_DATA_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    app_config_json_data: str
    status: RestStatusProto
    def __init__(self, app_config_json_data: _Optional[str] = ..., status: _Optional[_Union[RestStatusProto, _Mapping]] = ...) -> None: ...

class GetK8SClusterConfigResult(_message.Message):
    __slots__ = ("k8s_config", "status")
    K8S_CONFIG_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    k8s_config: _kubernetes_config_pb2.KubernetesConfigProto
    status: RestStatusProto
    def __init__(self, k8s_config: _Optional[_Union[_kubernetes_config_pb2.KubernetesConfigProto, _Mapping]] = ..., status: _Optional[_Union[RestStatusProto, _Mapping]] = ...) -> None: ...

class GetAthenaConfigResult(_message.Message):
    __slots__ = ("athena_config", "status")
    ATHENA_CONFIG_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    athena_config: _cluster_config_pb2.ClusterConfigProto.AthenaConfig
    status: RestStatusProto
    def __init__(self, athena_config: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.AthenaConfig, _Mapping]] = ..., status: _Optional[_Union[RestStatusProto, _Mapping]] = ...) -> None: ...
