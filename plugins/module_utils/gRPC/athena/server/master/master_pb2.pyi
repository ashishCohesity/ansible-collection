from athena.base import error_pb2 as _error_pb2
from athena.base import athena_pb2 as _athena_pb2
from configs import system_service_pb2 as _system_service_pb2
from athena.base import kubernetes_pb2 as _kubernetes_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AppInfoProto(_message.Message):
    __slots__ = ("app_uid", "app_version", "meta", "checksum", "app_privileges_list", "container_yaml_spec", "helm_chart_base64enc", "package_file", "single_instance", "desired_state", "desired_version", "force_update_app_instances", "force_terminate_app_instances", "state", "install_time_usecs", "uninstall_time_usecs", "container_images", "error", "pre_packaged_app", "dynamic_resource_percentage", "system_service_name", "vm_json_spec", "virtualization_support_required", "external_ip_required", "instance_size_list", "allow_dynamic_num_replicas", "vm_name_info_list", "additional_networks", "config_maps", "secrets", "installed_locally", "installed_nodes_list", "container_name_image_map", "upgrade_error", "readiness_probe")
    class ContainerImagesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class NetworkInfo(_message.Message):
        __slots__ = ("name", "description", "type")
        class NetworkType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            INTERNAL: _ClassVar[AppInfoProto.NetworkInfo.NetworkType]
            PROVIDER: _ClassVar[AppInfoProto.NetworkInfo.NetworkType]
        INTERNAL: AppInfoProto.NetworkInfo.NetworkType
        PROVIDER: AppInfoProto.NetworkInfo.NetworkType
        NAME_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        name: str
        description: str
        type: AppInfoProto.NetworkInfo.NetworkType
        def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., type: _Optional[_Union[AppInfoProto.NetworkInfo.NetworkType, str]] = ...) -> None: ...
    class ConfigMap(_message.Message):
        __slots__ = ("name", "keys")
        class Key(_message.Message):
            __slots__ = ("name", "required")
            NAME_FIELD_NUMBER: _ClassVar[int]
            REQUIRED_FIELD_NUMBER: _ClassVar[int]
            name: str
            required: bool
            def __init__(self, name: _Optional[str] = ..., required: bool = ...) -> None: ...
        NAME_FIELD_NUMBER: _ClassVar[int]
        KEYS_FIELD_NUMBER: _ClassVar[int]
        name: str
        keys: _containers.RepeatedCompositeFieldContainer[AppInfoProto.ConfigMap.Key]
        def __init__(self, name: _Optional[str] = ..., keys: _Optional[_Iterable[_Union[AppInfoProto.ConfigMap.Key, _Mapping]]] = ...) -> None: ...
    class Secret(_message.Message):
        __slots__ = ("name", "keys")
        class Key(_message.Message):
            __slots__ = ("name", "required")
            NAME_FIELD_NUMBER: _ClassVar[int]
            REQUIRED_FIELD_NUMBER: _ClassVar[int]
            name: str
            required: bool
            def __init__(self, name: _Optional[str] = ..., required: bool = ...) -> None: ...
        NAME_FIELD_NUMBER: _ClassVar[int]
        KEYS_FIELD_NUMBER: _ClassVar[int]
        name: str
        keys: _containers.RepeatedCompositeFieldContainer[AppInfoProto.Secret.Key]
        def __init__(self, name: _Optional[str] = ..., keys: _Optional[_Iterable[_Union[AppInfoProto.Secret.Key, _Mapping]]] = ...) -> None: ...
    class ContainerNameImageMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    APP_UID_FIELD_NUMBER: _ClassVar[int]
    APP_VERSION_FIELD_NUMBER: _ClassVar[int]
    META_FIELD_NUMBER: _ClassVar[int]
    CHECKSUM_FIELD_NUMBER: _ClassVar[int]
    APP_PRIVILEGES_LIST_FIELD_NUMBER: _ClassVar[int]
    CONTAINER_YAML_SPEC_FIELD_NUMBER: _ClassVar[int]
    HELM_CHART_BASE64ENC_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_FILE_FIELD_NUMBER: _ClassVar[int]
    SINGLE_INSTANCE_FIELD_NUMBER: _ClassVar[int]
    DESIRED_STATE_FIELD_NUMBER: _ClassVar[int]
    DESIRED_VERSION_FIELD_NUMBER: _ClassVar[int]
    FORCE_UPDATE_APP_INSTANCES_FIELD_NUMBER: _ClassVar[int]
    FORCE_TERMINATE_APP_INSTANCES_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    INSTALL_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    UNINSTALL_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    CONTAINER_IMAGES_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    PRE_PACKAGED_APP_FIELD_NUMBER: _ClassVar[int]
    DYNAMIC_RESOURCE_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_SERVICE_NAME_FIELD_NUMBER: _ClassVar[int]
    VM_JSON_SPEC_FIELD_NUMBER: _ClassVar[int]
    VIRTUALIZATION_SUPPORT_REQUIRED_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_IP_REQUIRED_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_SIZE_LIST_FIELD_NUMBER: _ClassVar[int]
    ALLOW_DYNAMIC_NUM_REPLICAS_FIELD_NUMBER: _ClassVar[int]
    VM_NAME_INFO_LIST_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_NETWORKS_FIELD_NUMBER: _ClassVar[int]
    CONFIG_MAPS_FIELD_NUMBER: _ClassVar[int]
    SECRETS_FIELD_NUMBER: _ClassVar[int]
    INSTALLED_LOCALLY_FIELD_NUMBER: _ClassVar[int]
    INSTALLED_NODES_LIST_FIELD_NUMBER: _ClassVar[int]
    CONTAINER_NAME_IMAGE_MAP_FIELD_NUMBER: _ClassVar[int]
    UPGRADE_ERROR_FIELD_NUMBER: _ClassVar[int]
    READINESS_PROBE_FIELD_NUMBER: _ClassVar[int]
    app_uid: int
    app_version: int
    meta: _athena_pb2.AppMetaInfoProto
    checksum: bytes
    app_privileges_list: _containers.RepeatedCompositeFieldContainer[_athena_pb2.AppPrivilegesProto]
    container_yaml_spec: bytes
    helm_chart_base64enc: bytes
    package_file: str
    single_instance: bool
    desired_state: _athena_pb2.AppStateProto
    desired_version: int
    force_update_app_instances: bool
    force_terminate_app_instances: bool
    state: _athena_pb2.AppStateProto
    install_time_usecs: int
    uninstall_time_usecs: int
    container_images: _containers.ScalarMap[str, str]
    error: _error_pb2.ErrorProto
    pre_packaged_app: bool
    dynamic_resource_percentage: int
    system_service_name: str
    vm_json_spec: str
    virtualization_support_required: bool
    external_ip_required: bool
    instance_size_list: _containers.RepeatedScalarFieldContainer[str]
    allow_dynamic_num_replicas: bool
    vm_name_info_list: _containers.RepeatedCompositeFieldContainer[_athena_pb2.VmNameInfoProto]
    additional_networks: _containers.RepeatedCompositeFieldContainer[AppInfoProto.NetworkInfo]
    config_maps: _containers.RepeatedCompositeFieldContainer[AppInfoProto.ConfigMap]
    secrets: _containers.RepeatedCompositeFieldContainer[AppInfoProto.Secret]
    installed_locally: bool
    installed_nodes_list: _containers.RepeatedScalarFieldContainer[int]
    container_name_image_map: _containers.ScalarMap[str, str]
    upgrade_error: _error_pb2.ErrorProto
    readiness_probe: AppProbe
    def __init__(self, app_uid: _Optional[int] = ..., app_version: _Optional[int] = ..., meta: _Optional[_Union[_athena_pb2.AppMetaInfoProto, _Mapping]] = ..., checksum: _Optional[bytes] = ..., app_privileges_list: _Optional[_Iterable[_Union[_athena_pb2.AppPrivilegesProto, _Mapping]]] = ..., container_yaml_spec: _Optional[bytes] = ..., helm_chart_base64enc: _Optional[bytes] = ..., package_file: _Optional[str] = ..., single_instance: bool = ..., desired_state: _Optional[_Union[_athena_pb2.AppStateProto, _Mapping]] = ..., desired_version: _Optional[int] = ..., force_update_app_instances: bool = ..., force_terminate_app_instances: bool = ..., state: _Optional[_Union[_athena_pb2.AppStateProto, _Mapping]] = ..., install_time_usecs: _Optional[int] = ..., uninstall_time_usecs: _Optional[int] = ..., container_images: _Optional[_Mapping[str, str]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., pre_packaged_app: bool = ..., dynamic_resource_percentage: _Optional[int] = ..., system_service_name: _Optional[str] = ..., vm_json_spec: _Optional[str] = ..., virtualization_support_required: bool = ..., external_ip_required: bool = ..., instance_size_list: _Optional[_Iterable[str]] = ..., allow_dynamic_num_replicas: bool = ..., vm_name_info_list: _Optional[_Iterable[_Union[_athena_pb2.VmNameInfoProto, _Mapping]]] = ..., additional_networks: _Optional[_Iterable[_Union[AppInfoProto.NetworkInfo, _Mapping]]] = ..., config_maps: _Optional[_Iterable[_Union[AppInfoProto.ConfigMap, _Mapping]]] = ..., secrets: _Optional[_Iterable[_Union[AppInfoProto.Secret, _Mapping]]] = ..., installed_locally: bool = ..., installed_nodes_list: _Optional[_Iterable[int]] = ..., container_name_image_map: _Optional[_Mapping[str, str]] = ..., upgrade_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., readiness_probe: _Optional[_Union[AppProbe, _Mapping]] = ...) -> None: ...

class AppProbe(_message.Message):
    __slots__ = ("http_get", "timeout_seconds", "poll_interval_seconds", "success_threshold", "failure_threshold")
    class HTTPGetAction(_message.Message):
        __slots__ = ("path", "port", "host", "scheme", "http_headers")
        class URIScheme(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            HTTPS: _ClassVar[AppProbe.HTTPGetAction.URIScheme]
            HTTP: _ClassVar[AppProbe.HTTPGetAction.URIScheme]
        HTTPS: AppProbe.HTTPGetAction.URIScheme
        HTTP: AppProbe.HTTPGetAction.URIScheme
        class HttpHeadersEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: str
            def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
        PATH_FIELD_NUMBER: _ClassVar[int]
        PORT_FIELD_NUMBER: _ClassVar[int]
        HOST_FIELD_NUMBER: _ClassVar[int]
        SCHEME_FIELD_NUMBER: _ClassVar[int]
        HTTP_HEADERS_FIELD_NUMBER: _ClassVar[int]
        path: str
        port: int
        host: str
        scheme: AppProbe.HTTPGetAction.URIScheme
        http_headers: _containers.ScalarMap[str, str]
        def __init__(self, path: _Optional[str] = ..., port: _Optional[int] = ..., host: _Optional[str] = ..., scheme: _Optional[_Union[AppProbe.HTTPGetAction.URIScheme, str]] = ..., http_headers: _Optional[_Mapping[str, str]] = ...) -> None: ...
    HTTP_GET_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_SECONDS_FIELD_NUMBER: _ClassVar[int]
    POLL_INTERVAL_SECONDS_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    FAILURE_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    http_get: AppProbe.HTTPGetAction
    timeout_seconds: int
    poll_interval_seconds: int
    success_threshold: int
    failure_threshold: int
    def __init__(self, http_get: _Optional[_Union[AppProbe.HTTPGetAction, _Mapping]] = ..., timeout_seconds: _Optional[int] = ..., poll_interval_seconds: _Optional[int] = ..., success_threshold: _Optional[int] = ..., failure_threshold: _Optional[int] = ...) -> None: ...

class LocalAppRegistryProto(_message.Message):
    __slots__ = ("apps",)
    APPS_FIELD_NUMBER: _ClassVar[int]
    apps: _containers.RepeatedCompositeFieldContainer[AppInfoProto]
    def __init__(self, apps: _Optional[_Iterable[_Union[AppInfoProto, _Mapping]]] = ...) -> None: ...

class InternalSubnetInfoProto(_message.Message):
    __slots__ = ("start_ip_addr", "subnet_size", "allocatable_ip_addr_offset")
    START_IP_ADDR_FIELD_NUMBER: _ClassVar[int]
    SUBNET_SIZE_FIELD_NUMBER: _ClassVar[int]
    ALLOCATABLE_IP_ADDR_OFFSET_FIELD_NUMBER: _ClassVar[int]
    start_ip_addr: str
    subnet_size: int
    allocatable_ip_addr_offset: int
    def __init__(self, start_ip_addr: _Optional[str] = ..., subnet_size: _Optional[int] = ..., allocatable_ip_addr_offset: _Optional[int] = ...) -> None: ...

class ExternalSubnetInfoProto(_message.Message):
    __slots__ = ("vlan_id", "is_ipv6", "apps_ip_map")
    class AppsIpMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    VLAN_ID_FIELD_NUMBER: _ClassVar[int]
    IS_IPV6_FIELD_NUMBER: _ClassVar[int]
    APPS_IP_MAP_FIELD_NUMBER: _ClassVar[int]
    vlan_id: int
    is_ipv6: bool
    apps_ip_map: _containers.ScalarMap[str, str]
    def __init__(self, vlan_id: _Optional[int] = ..., is_ipv6: bool = ..., apps_ip_map: _Optional[_Mapping[str, str]] = ...) -> None: ...

class NetworkInfoProto(_message.Message):
    __slots__ = ("network_type", "axon_network_uuid", "axon_network_access_info", "internal_subnet_info", "axon_subnet_uuid", "external_subnet_info", "ipam_type", "interface_group", "metadata", "axon_provider_net")
    class NetworkType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNotSet: _ClassVar[NetworkInfoProto.NetworkType]
        kInternalNetwork: _ClassVar[NetworkInfoProto.NetworkType]
        kExternalNetwork: _ClassVar[NetworkInfoProto.NetworkType]
        kSystemServiceNetwork: _ClassVar[NetworkInfoProto.NetworkType]
        kK8sSystemPodNetwork: _ClassVar[NetworkInfoProto.NetworkType]
        kBifrostTenantNetwork: _ClassVar[NetworkInfoProto.NetworkType]
        kBifrostHostNetwork: _ClassVar[NetworkInfoProto.NetworkType]
    kNotSet: NetworkInfoProto.NetworkType
    kInternalNetwork: NetworkInfoProto.NetworkType
    kExternalNetwork: NetworkInfoProto.NetworkType
    kSystemServiceNetwork: NetworkInfoProto.NetworkType
    kK8sSystemPodNetwork: NetworkInfoProto.NetworkType
    kBifrostTenantNetwork: NetworkInfoProto.NetworkType
    kBifrostHostNetwork: NetworkInfoProto.NetworkType
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NETWORK_TYPE_FIELD_NUMBER: _ClassVar[int]
    AXON_NETWORK_UUID_FIELD_NUMBER: _ClassVar[int]
    AXON_NETWORK_ACCESS_INFO_FIELD_NUMBER: _ClassVar[int]
    INTERNAL_SUBNET_INFO_FIELD_NUMBER: _ClassVar[int]
    AXON_SUBNET_UUID_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_SUBNET_INFO_FIELD_NUMBER: _ClassVar[int]
    IPAM_TYPE_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_GROUP_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    AXON_PROVIDER_NET_FIELD_NUMBER: _ClassVar[int]
    network_type: NetworkInfoProto.NetworkType
    axon_network_uuid: str
    axon_network_access_info: _athena_pb2.AxonNetworkAccessInfoProto
    internal_subnet_info: InternalSubnetInfoProto
    axon_subnet_uuid: str
    external_subnet_info: ExternalSubnetInfoProto
    ipam_type: str
    interface_group: str
    metadata: _containers.ScalarMap[str, str]
    axon_provider_net: bool
    def __init__(self, network_type: _Optional[_Union[NetworkInfoProto.NetworkType, str]] = ..., axon_network_uuid: _Optional[str] = ..., axon_network_access_info: _Optional[_Union[_athena_pb2.AxonNetworkAccessInfoProto, _Mapping]] = ..., internal_subnet_info: _Optional[_Union[InternalSubnetInfoProto, _Mapping]] = ..., axon_subnet_uuid: _Optional[str] = ..., external_subnet_info: _Optional[_Union[ExternalSubnetInfoProto, _Mapping]] = ..., ipam_type: _Optional[str] = ..., interface_group: _Optional[str] = ..., metadata: _Optional[_Mapping[str, str]] = ..., axon_provider_net: bool = ...) -> None: ...

class NetworkProto(_message.Message):
    __slots__ = ("network_name", "network_info", "namespace_pod_networking_info_map", "network_state")
    class NetworkState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNotSet: _ClassVar[NetworkProto.NetworkState]
        kCreating: _ClassVar[NetworkProto.NetworkState]
        kCreated: _ClassVar[NetworkProto.NetworkState]
        kDeleting: _ClassVar[NetworkProto.NetworkState]
        kDeleted: _ClassVar[NetworkProto.NetworkState]
    kNotSet: NetworkProto.NetworkState
    kCreating: NetworkProto.NetworkState
    kCreated: NetworkProto.NetworkState
    kDeleting: NetworkProto.NetworkState
    kDeleted: NetworkProto.NetworkState
    class PodNetworkingInfoMap(_message.Message):
        __slots__ = ("pod_networking_info_map",)
        class PodNetworkingInfoMapEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: _athena_pb2.PodNetworkingInfoProto
            def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_athena_pb2.PodNetworkingInfoProto, _Mapping]] = ...) -> None: ...
        POD_NETWORKING_INFO_MAP_FIELD_NUMBER: _ClassVar[int]
        pod_networking_info_map: _containers.MessageMap[str, _athena_pb2.PodNetworkingInfoProto]
        def __init__(self, pod_networking_info_map: _Optional[_Mapping[str, _athena_pb2.PodNetworkingInfoProto]] = ...) -> None: ...
    class NamespacePodNetworkingInfoMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: NetworkProto.PodNetworkingInfoMap
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[NetworkProto.PodNetworkingInfoMap, _Mapping]] = ...) -> None: ...
    NETWORK_NAME_FIELD_NUMBER: _ClassVar[int]
    NETWORK_INFO_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_POD_NETWORKING_INFO_MAP_FIELD_NUMBER: _ClassVar[int]
    NETWORK_STATE_FIELD_NUMBER: _ClassVar[int]
    network_name: str
    network_info: NetworkInfoProto
    namespace_pod_networking_info_map: _containers.MessageMap[str, NetworkProto.PodNetworkingInfoMap]
    network_state: NetworkProto.NetworkState
    def __init__(self, network_name: _Optional[str] = ..., network_info: _Optional[_Union[NetworkInfoProto, _Mapping]] = ..., namespace_pod_networking_info_map: _Optional[_Mapping[str, NetworkProto.PodNetworkingInfoMap]] = ..., network_state: _Optional[_Union[NetworkProto.NetworkState, str]] = ...) -> None: ...

class AppInstanceSpecProto(_message.Message):
    __slots__ = ("app_instance_id", "app_uid", "desired_app_version", "app_name", "desired_state", "created_time_usecs", "settings", "creation_uid", "description", "user_info", "external_network_info", "is_system_app", "revert_state", "bifrost_config", "delta_yaml", "desired_update_id", "instance_size", "additional_networks", "config_maps", "secrets", "tenant_id", "deployment_parameters")
    class NetworkInfo(_message.Message):
        __slots__ = ("external_network_info", "name", "id")
        EXTERNAL_NETWORK_INFO_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        ID_FIELD_NUMBER: _ClassVar[int]
        external_network_info: _athena_pb2.ExternalNetworkInfoProto
        name: str
        id: str
        def __init__(self, external_network_info: _Optional[_Union[_athena_pb2.ExternalNetworkInfoProto, _Mapping]] = ..., name: _Optional[str] = ..., id: _Optional[str] = ...) -> None: ...
    class ConfigMap(_message.Message):
        __slots__ = ("name", "data")
        class DataEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: str
            def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
        NAME_FIELD_NUMBER: _ClassVar[int]
        DATA_FIELD_NUMBER: _ClassVar[int]
        name: str
        data: _containers.ScalarMap[str, str]
        def __init__(self, name: _Optional[str] = ..., data: _Optional[_Mapping[str, str]] = ...) -> None: ...
    class Secret(_message.Message):
        __slots__ = ("name", "data")
        class DataEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: str
            def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
        NAME_FIELD_NUMBER: _ClassVar[int]
        DATA_FIELD_NUMBER: _ClassVar[int]
        name: str
        data: _containers.ScalarMap[str, str]
        def __init__(self, name: _Optional[str] = ..., data: _Optional[_Mapping[str, str]] = ...) -> None: ...
    APP_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    APP_UID_FIELD_NUMBER: _ClassVar[int]
    DESIRED_APP_VERSION_FIELD_NUMBER: _ClassVar[int]
    APP_NAME_FIELD_NUMBER: _ClassVar[int]
    DESIRED_STATE_FIELD_NUMBER: _ClassVar[int]
    CREATED_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    CREATION_UID_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    USER_INFO_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_NETWORK_INFO_FIELD_NUMBER: _ClassVar[int]
    IS_SYSTEM_APP_FIELD_NUMBER: _ClassVar[int]
    REVERT_STATE_FIELD_NUMBER: _ClassVar[int]
    BIFROST_CONFIG_FIELD_NUMBER: _ClassVar[int]
    DELTA_YAML_FIELD_NUMBER: _ClassVar[int]
    DESIRED_UPDATE_ID_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_SIZE_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_NETWORKS_FIELD_NUMBER: _ClassVar[int]
    CONFIG_MAPS_FIELD_NUMBER: _ClassVar[int]
    SECRETS_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    DEPLOYMENT_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    app_instance_id: int
    app_uid: int
    desired_app_version: int
    app_name: str
    desired_state: _athena_pb2.AppInstanceStateProto
    created_time_usecs: int
    settings: _athena_pb2.AppInstanceSettingsProto
    creation_uid: str
    description: str
    user_info: _athena_pb2.UserInformation
    external_network_info: _athena_pb2.ExternalNetworkInfoProto
    is_system_app: bool
    revert_state: _athena_pb2.AppInstanceStateProto
    bifrost_config: _athena_pb2.BifrostConfig
    delta_yaml: bytes
    desired_update_id: int
    instance_size: str
    additional_networks: _containers.RepeatedCompositeFieldContainer[AppInstanceSpecProto.NetworkInfo]
    config_maps: _containers.RepeatedCompositeFieldContainer[AppInstanceSpecProto.ConfigMap]
    secrets: _containers.RepeatedCompositeFieldContainer[AppInstanceSpecProto.Secret]
    tenant_id: str
    deployment_parameters: str
    def __init__(self, app_instance_id: _Optional[int] = ..., app_uid: _Optional[int] = ..., desired_app_version: _Optional[int] = ..., app_name: _Optional[str] = ..., desired_state: _Optional[_Union[_athena_pb2.AppInstanceStateProto, _Mapping]] = ..., created_time_usecs: _Optional[int] = ..., settings: _Optional[_Union[_athena_pb2.AppInstanceSettingsProto, _Mapping]] = ..., creation_uid: _Optional[str] = ..., description: _Optional[str] = ..., user_info: _Optional[_Union[_athena_pb2.UserInformation, _Mapping]] = ..., external_network_info: _Optional[_Union[_athena_pb2.ExternalNetworkInfoProto, _Mapping]] = ..., is_system_app: bool = ..., revert_state: _Optional[_Union[_athena_pb2.AppInstanceStateProto, _Mapping]] = ..., bifrost_config: _Optional[_Union[_athena_pb2.BifrostConfig, _Mapping]] = ..., delta_yaml: _Optional[bytes] = ..., desired_update_id: _Optional[int] = ..., instance_size: _Optional[str] = ..., additional_networks: _Optional[_Iterable[_Union[AppInstanceSpecProto.NetworkInfo, _Mapping]]] = ..., config_maps: _Optional[_Iterable[_Union[AppInstanceSpecProto.ConfigMap, _Mapping]]] = ..., secrets: _Optional[_Iterable[_Union[AppInstanceSpecProto.Secret, _Mapping]]] = ..., tenant_id: _Optional[str] = ..., deployment_parameters: _Optional[str] = ...) -> None: ...

class AppInstanceStatusProto(_message.Message):
    __slots__ = ("app_instance_id", "operational_state", "operational_state_detail", "health_status", "health_detail", "app_instance_name", "view_name", "static_volume_list", "node_port_list", "ui_node_port", "kubernetes_object_list", "modified_time_usecs", "operational_app_version", "kubernetes_cleanup_job", "app_instance_tokens", "allocated_resources", "user_name", "user_domain", "total_pod_count", "replica_count_list", "unhealthy_alert_time_usecs", "first_healthy_time_usecs", "service_nodeport_map", "reconciliation_done", "vm_disk_info_map", "iscsi_target_view_name", "vm_groups_info", "user_ssh_key_info_map", "dynamic_volume_list", "use_pvc_for_dynamic_volumes", "volume_health_status", "volume_health_detail", "total_run_time_usecs", "internal_network_info_DEPRECATED", "pod_networking_info_map_DEPRECATED", "network_name", "additional_network_names", "app_resource_pool", "resources_limits", "operational_update_id", "dynamic_update_needed", "ui_cluster_ip_svc_name", "upgrade_completion_check_count", "dynamic_update_in_progress", "events", "readiness_status", "readiness_change_counter", "deployment_type", "compute_objects_map", "failure_reasons")
    class DeploymentType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kAthenaYaml: _ClassVar[AppInstanceStatusProto.DeploymentType]
        kHelmChart: _ClassVar[AppInstanceStatusProto.DeploymentType]
    kAthenaYaml: AppInstanceStatusProto.DeploymentType
    kHelmChart: AppInstanceStatusProto.DeploymentType
    class AllocatedResources(_message.Message):
        __slots__ = ("cpu", "memory")
        CPU_FIELD_NUMBER: _ClassVar[int]
        MEMORY_FIELD_NUMBER: _ClassVar[int]
        cpu: int
        memory: int
        def __init__(self, cpu: _Optional[int] = ..., memory: _Optional[int] = ...) -> None: ...
    class ReplicaCount(_message.Message):
        __slots__ = ("object_kind", "object_name", "replica_count")
        OBJECT_KIND_FIELD_NUMBER: _ClassVar[int]
        OBJECT_NAME_FIELD_NUMBER: _ClassVar[int]
        REPLICA_COUNT_FIELD_NUMBER: _ClassVar[int]
        object_kind: str
        object_name: str
        replica_count: int
        def __init__(self, object_kind: _Optional[str] = ..., object_name: _Optional[str] = ..., replica_count: _Optional[int] = ...) -> None: ...
    class ServiceNodePorts(_message.Message):
        __slots__ = ("nodeport_map", "nodeport_info_map")
        class NodeportMapEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: int
            value: int
            def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
        class NodeportInfoMapEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: int
            value: _athena_pb2.NodePortInfoProto
            def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_athena_pb2.NodePortInfoProto, _Mapping]] = ...) -> None: ...
        NODEPORT_MAP_FIELD_NUMBER: _ClassVar[int]
        NODEPORT_INFO_MAP_FIELD_NUMBER: _ClassVar[int]
        nodeport_map: _containers.ScalarMap[int, int]
        nodeport_info_map: _containers.MessageMap[int, _athena_pb2.NodePortInfoProto]
        def __init__(self, nodeport_map: _Optional[_Mapping[int, int]] = ..., nodeport_info_map: _Optional[_Mapping[int, _athena_pb2.NodePortInfoProto]] = ...) -> None: ...
    class ServiceNodeportMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: AppInstanceStatusProto.ServiceNodePorts
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[AppInstanceStatusProto.ServiceNodePorts, _Mapping]] = ...) -> None: ...
    class VmDiskInfoMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _athena_pb2.VMDiskInfoProto
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_athena_pb2.VMDiskInfoProto, _Mapping]] = ...) -> None: ...
    class UserSshKeyInfoMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _athena_pb2.UserSshKeyInfo
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_athena_pb2.UserSshKeyInfo, _Mapping]] = ...) -> None: ...
    class PodNetworkingInfoMapDEPRECATEDEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _athena_pb2.PodNetworkingInfoProto
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_athena_pb2.PodNetworkingInfoProto, _Mapping]] = ...) -> None: ...
    class KubernetesObject(_message.Message):
        __slots__ = ("kind", "name", "apigroup", "apiversion")
        KIND_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        APIGROUP_FIELD_NUMBER: _ClassVar[int]
        APIVERSION_FIELD_NUMBER: _ClassVar[int]
        kind: str
        name: str
        apigroup: str
        apiversion: str
        def __init__(self, kind: _Optional[str] = ..., name: _Optional[str] = ..., apigroup: _Optional[str] = ..., apiversion: _Optional[str] = ...) -> None: ...
    class KubernetesObjectList(_message.Message):
        __slots__ = ("kubernetes_object_list",)
        KUBERNETES_OBJECT_LIST_FIELD_NUMBER: _ClassVar[int]
        kubernetes_object_list: _containers.RepeatedCompositeFieldContainer[AppInstanceStatusProto.KubernetesObject]
        def __init__(self, kubernetes_object_list: _Optional[_Iterable[_Union[AppInstanceStatusProto.KubernetesObject, _Mapping]]] = ...) -> None: ...
    class ComputeObjectsMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: AppInstanceStatusProto.KubernetesObjectList
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[AppInstanceStatusProto.KubernetesObjectList, _Mapping]] = ...) -> None: ...
    class FailureReason(_message.Message):
        __slots__ = ("code", "summary", "detail")
        CODE_FIELD_NUMBER: _ClassVar[int]
        SUMMARY_FIELD_NUMBER: _ClassVar[int]
        DETAIL_FIELD_NUMBER: _ClassVar[int]
        code: str
        summary: str
        detail: str
        def __init__(self, code: _Optional[str] = ..., summary: _Optional[str] = ..., detail: _Optional[str] = ...) -> None: ...
    APP_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    OPERATIONAL_STATE_FIELD_NUMBER: _ClassVar[int]
    OPERATIONAL_STATE_DETAIL_FIELD_NUMBER: _ClassVar[int]
    HEALTH_STATUS_FIELD_NUMBER: _ClassVar[int]
    HEALTH_DETAIL_FIELD_NUMBER: _ClassVar[int]
    APP_INSTANCE_NAME_FIELD_NUMBER: _ClassVar[int]
    VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    STATIC_VOLUME_LIST_FIELD_NUMBER: _ClassVar[int]
    NODE_PORT_LIST_FIELD_NUMBER: _ClassVar[int]
    UI_NODE_PORT_FIELD_NUMBER: _ClassVar[int]
    KUBERNETES_OBJECT_LIST_FIELD_NUMBER: _ClassVar[int]
    MODIFIED_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    OPERATIONAL_APP_VERSION_FIELD_NUMBER: _ClassVar[int]
    KUBERNETES_CLEANUP_JOB_FIELD_NUMBER: _ClassVar[int]
    APP_INSTANCE_TOKENS_FIELD_NUMBER: _ClassVar[int]
    ALLOCATED_RESOURCES_FIELD_NUMBER: _ClassVar[int]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    USER_DOMAIN_FIELD_NUMBER: _ClassVar[int]
    TOTAL_POD_COUNT_FIELD_NUMBER: _ClassVar[int]
    REPLICA_COUNT_LIST_FIELD_NUMBER: _ClassVar[int]
    UNHEALTHY_ALERT_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    FIRST_HEALTHY_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    SERVICE_NODEPORT_MAP_FIELD_NUMBER: _ClassVar[int]
    RECONCILIATION_DONE_FIELD_NUMBER: _ClassVar[int]
    VM_DISK_INFO_MAP_FIELD_NUMBER: _ClassVar[int]
    ISCSI_TARGET_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    VM_GROUPS_INFO_FIELD_NUMBER: _ClassVar[int]
    USER_SSH_KEY_INFO_MAP_FIELD_NUMBER: _ClassVar[int]
    DYNAMIC_VOLUME_LIST_FIELD_NUMBER: _ClassVar[int]
    USE_PVC_FOR_DYNAMIC_VOLUMES_FIELD_NUMBER: _ClassVar[int]
    VOLUME_HEALTH_STATUS_FIELD_NUMBER: _ClassVar[int]
    VOLUME_HEALTH_DETAIL_FIELD_NUMBER: _ClassVar[int]
    TOTAL_RUN_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    INTERNAL_NETWORK_INFO_DEPRECATED_FIELD_NUMBER: _ClassVar[int]
    POD_NETWORKING_INFO_MAP_DEPRECATED_FIELD_NUMBER: _ClassVar[int]
    NETWORK_NAME_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_NETWORK_NAMES_FIELD_NUMBER: _ClassVar[int]
    APP_RESOURCE_POOL_FIELD_NUMBER: _ClassVar[int]
    RESOURCES_LIMITS_FIELD_NUMBER: _ClassVar[int]
    OPERATIONAL_UPDATE_ID_FIELD_NUMBER: _ClassVar[int]
    DYNAMIC_UPDATE_NEEDED_FIELD_NUMBER: _ClassVar[int]
    UI_CLUSTER_IP_SVC_NAME_FIELD_NUMBER: _ClassVar[int]
    UPGRADE_COMPLETION_CHECK_COUNT_FIELD_NUMBER: _ClassVar[int]
    DYNAMIC_UPDATE_IN_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    READINESS_STATUS_FIELD_NUMBER: _ClassVar[int]
    READINESS_CHANGE_COUNTER_FIELD_NUMBER: _ClassVar[int]
    DEPLOYMENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    COMPUTE_OBJECTS_MAP_FIELD_NUMBER: _ClassVar[int]
    FAILURE_REASONS_FIELD_NUMBER: _ClassVar[int]
    app_instance_id: int
    operational_state: _athena_pb2.AppInstanceStateProto
    operational_state_detail: str
    health_status: _athena_pb2.HealthStatusProto
    health_detail: str
    app_instance_name: str
    view_name: str
    static_volume_list: _containers.RepeatedScalarFieldContainer[str]
    node_port_list: _containers.RepeatedScalarFieldContainer[int]
    ui_node_port: int
    kubernetes_object_list: _containers.RepeatedScalarFieldContainer[str]
    modified_time_usecs: int
    operational_app_version: int
    kubernetes_cleanup_job: str
    app_instance_tokens: _containers.RepeatedCompositeFieldContainer[_athena_pb2.AppInstanceTokenProto]
    allocated_resources: AppInstanceStatusProto.AllocatedResources
    user_name: str
    user_domain: str
    total_pod_count: int
    replica_count_list: _containers.RepeatedCompositeFieldContainer[AppInstanceStatusProto.ReplicaCount]
    unhealthy_alert_time_usecs: int
    first_healthy_time_usecs: int
    service_nodeport_map: _containers.MessageMap[str, AppInstanceStatusProto.ServiceNodePorts]
    reconciliation_done: bool
    vm_disk_info_map: _containers.MessageMap[str, _athena_pb2.VMDiskInfoProto]
    iscsi_target_view_name: str
    vm_groups_info: _containers.RepeatedCompositeFieldContainer[_athena_pb2.VMGroupProto]
    user_ssh_key_info_map: _containers.MessageMap[str, _athena_pb2.UserSshKeyInfo]
    dynamic_volume_list: _containers.RepeatedScalarFieldContainer[str]
    use_pvc_for_dynamic_volumes: bool
    volume_health_status: _athena_pb2.HealthStatusProto
    volume_health_detail: str
    total_run_time_usecs: int
    internal_network_info_DEPRECATED: NetworkInfoProto
    pod_networking_info_map_DEPRECATED: _containers.MessageMap[str, _athena_pb2.PodNetworkingInfoProto]
    network_name: str
    additional_network_names: _containers.RepeatedScalarFieldContainer[str]
    app_resource_pool: _system_service_pb2.ResourcePool
    resources_limits: AppInstanceStatusProto.AllocatedResources
    operational_update_id: int
    dynamic_update_needed: bool
    ui_cluster_ip_svc_name: str
    upgrade_completion_check_count: int
    dynamic_update_in_progress: bool
    events: _containers.RepeatedCompositeFieldContainer[_kubernetes_pb2.EventInfoProto]
    readiness_status: _athena_pb2.HealthStatusProto
    readiness_change_counter: int
    deployment_type: AppInstanceStatusProto.DeploymentType
    compute_objects_map: _containers.MessageMap[int, AppInstanceStatusProto.KubernetesObjectList]
    failure_reasons: _containers.RepeatedCompositeFieldContainer[AppInstanceStatusProto.FailureReason]
    def __init__(self, app_instance_id: _Optional[int] = ..., operational_state: _Optional[_Union[_athena_pb2.AppInstanceStateProto, _Mapping]] = ..., operational_state_detail: _Optional[str] = ..., health_status: _Optional[_Union[_athena_pb2.HealthStatusProto, _Mapping]] = ..., health_detail: _Optional[str] = ..., app_instance_name: _Optional[str] = ..., view_name: _Optional[str] = ..., static_volume_list: _Optional[_Iterable[str]] = ..., node_port_list: _Optional[_Iterable[int]] = ..., ui_node_port: _Optional[int] = ..., kubernetes_object_list: _Optional[_Iterable[str]] = ..., modified_time_usecs: _Optional[int] = ..., operational_app_version: _Optional[int] = ..., kubernetes_cleanup_job: _Optional[str] = ..., app_instance_tokens: _Optional[_Iterable[_Union[_athena_pb2.AppInstanceTokenProto, _Mapping]]] = ..., allocated_resources: _Optional[_Union[AppInstanceStatusProto.AllocatedResources, _Mapping]] = ..., user_name: _Optional[str] = ..., user_domain: _Optional[str] = ..., total_pod_count: _Optional[int] = ..., replica_count_list: _Optional[_Iterable[_Union[AppInstanceStatusProto.ReplicaCount, _Mapping]]] = ..., unhealthy_alert_time_usecs: _Optional[int] = ..., first_healthy_time_usecs: _Optional[int] = ..., service_nodeport_map: _Optional[_Mapping[str, AppInstanceStatusProto.ServiceNodePorts]] = ..., reconciliation_done: bool = ..., vm_disk_info_map: _Optional[_Mapping[str, _athena_pb2.VMDiskInfoProto]] = ..., iscsi_target_view_name: _Optional[str] = ..., vm_groups_info: _Optional[_Iterable[_Union[_athena_pb2.VMGroupProto, _Mapping]]] = ..., user_ssh_key_info_map: _Optional[_Mapping[str, _athena_pb2.UserSshKeyInfo]] = ..., dynamic_volume_list: _Optional[_Iterable[str]] = ..., use_pvc_for_dynamic_volumes: bool = ..., volume_health_status: _Optional[_Union[_athena_pb2.HealthStatusProto, _Mapping]] = ..., volume_health_detail: _Optional[str] = ..., total_run_time_usecs: _Optional[int] = ..., internal_network_info_DEPRECATED: _Optional[_Union[NetworkInfoProto, _Mapping]] = ..., pod_networking_info_map_DEPRECATED: _Optional[_Mapping[str, _athena_pb2.PodNetworkingInfoProto]] = ..., network_name: _Optional[str] = ..., additional_network_names: _Optional[_Iterable[str]] = ..., app_resource_pool: _Optional[_Union[_system_service_pb2.ResourcePool, str]] = ..., resources_limits: _Optional[_Union[AppInstanceStatusProto.AllocatedResources, _Mapping]] = ..., operational_update_id: _Optional[int] = ..., dynamic_update_needed: bool = ..., ui_cluster_ip_svc_name: _Optional[str] = ..., upgrade_completion_check_count: _Optional[int] = ..., dynamic_update_in_progress: bool = ..., events: _Optional[_Iterable[_Union[_kubernetes_pb2.EventInfoProto, _Mapping]]] = ..., readiness_status: _Optional[_Union[_athena_pb2.HealthStatusProto, _Mapping]] = ..., readiness_change_counter: _Optional[int] = ..., deployment_type: _Optional[_Union[AppInstanceStatusProto.DeploymentType, str]] = ..., compute_objects_map: _Optional[_Mapping[int, AppInstanceStatusProto.KubernetesObjectList]] = ..., failure_reasons: _Optional[_Iterable[_Union[AppInstanceStatusProto.FailureReason, _Mapping]]] = ...) -> None: ...
