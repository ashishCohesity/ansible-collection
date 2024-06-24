from magneto.base import error_pb2 as _error_pb2
from magneto.base.entities import aws_pb2 as _aws_pb2
from magneto.base.entities import gcp_pb2 as _gcp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf.internal import python_message as _python_message
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TaskType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kBackup: _ClassVar[TaskType]
    kYoda: _ClassVar[TaskType]
kBackup: TaskType
kYoda: TaskType

class ProxyInfo(_message.Message):
    __slots__ = ("id", "ip", "parent_entity_id", "type", "is_alive", "status", "task_type", "task_id", "launch_time", "launch_time_msecs", "error")
    Extensions: _python_message._ExtensionDict
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kAWS: _ClassVar[ProxyInfo.Type]
        kGCP: _ClassVar[ProxyInfo.Type]
        kBifrost: _ClassVar[ProxyInfo.Type]
    kAWS: ProxyInfo.Type
    kGCP: ProxyInfo.Type
    kBifrost: ProxyInfo.Type
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kLaunchIntentLogged: _ClassVar[ProxyInfo.Status]
        kLaunched: _ClassVar[ProxyInfo.Status]
        kAgentRegistered: _ClassVar[ProxyInfo.Status]
        kStopped: _ClassVar[ProxyInfo.Status]
        kAttachDisksIntentLogged: _ClassVar[ProxyInfo.Status]
        kDisksAttached: _ClassVar[ProxyInfo.Status]
        kTerminating: _ClassVar[ProxyInfo.Status]
        kTerminated: _ClassVar[ProxyInfo.Status]
    kLaunchIntentLogged: ProxyInfo.Status
    kLaunched: ProxyInfo.Status
    kAgentRegistered: ProxyInfo.Status
    kStopped: ProxyInfo.Status
    kAttachDisksIntentLogged: ProxyInfo.Status
    kDisksAttached: ProxyInfo.Status
    kTerminating: ProxyInfo.Status
    kTerminated: ProxyInfo.Status
    ID_FIELD_NUMBER: _ClassVar[int]
    IP_FIELD_NUMBER: _ClassVar[int]
    PARENT_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    IS_ALIVE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TASK_TYPE_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    LAUNCH_TIME_FIELD_NUMBER: _ClassVar[int]
    LAUNCH_TIME_MSECS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    id: str
    ip: str
    parent_entity_id: int
    type: ProxyInfo.Type
    is_alive: bool
    status: ProxyInfo.Status
    task_type: TaskType
    task_id: int
    launch_time: str
    launch_time_msecs: int
    error: _error_pb2.ErrorProto
    def __init__(self, id: _Optional[str] = ..., ip: _Optional[str] = ..., parent_entity_id: _Optional[int] = ..., type: _Optional[_Union[ProxyInfo.Type, str]] = ..., is_alive: bool = ..., status: _Optional[_Union[ProxyInfo.Status, str]] = ..., task_type: _Optional[_Union[TaskType, str]] = ..., task_id: _Optional[int] = ..., launch_time: _Optional[str] = ..., launch_time_msecs: _Optional[int] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class AWSProxyInfo(_message.Message):
    __slots__ = ("region", "availability_zone", "device_name_vec", "volume_size_bytes", "vpc", "subnet", "network_security_group_vec", "proxy_uuid", "is_marketplace_proxy", "is_exclusive_proxy", "instance_type", "instance_type_vec", "disk_to_device_name_map", "custom_tag_vec")
    class DiskToDeviceNameMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    AWS_PROXY_INFO_FIELD_NUMBER: _ClassVar[int]
    aws_proxy_info: _descriptor.FieldDescriptor
    REGION_FIELD_NUMBER: _ClassVar[int]
    AVAILABILITY_ZONE_FIELD_NUMBER: _ClassVar[int]
    DEVICE_NAME_VEC_FIELD_NUMBER: _ClassVar[int]
    VOLUME_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    VPC_FIELD_NUMBER: _ClassVar[int]
    SUBNET_FIELD_NUMBER: _ClassVar[int]
    NETWORK_SECURITY_GROUP_VEC_FIELD_NUMBER: _ClassVar[int]
    PROXY_UUID_FIELD_NUMBER: _ClassVar[int]
    IS_MARKETPLACE_PROXY_FIELD_NUMBER: _ClassVar[int]
    IS_EXCLUSIVE_PROXY_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_TYPE_VEC_FIELD_NUMBER: _ClassVar[int]
    DISK_TO_DEVICE_NAME_MAP_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_TAG_VEC_FIELD_NUMBER: _ClassVar[int]
    region: str
    availability_zone: str
    device_name_vec: _containers.RepeatedScalarFieldContainer[str]
    volume_size_bytes: int
    vpc: str
    subnet: str
    network_security_group_vec: _containers.RepeatedScalarFieldContainer[str]
    proxy_uuid: str
    is_marketplace_proxy: bool
    is_exclusive_proxy: bool
    instance_type: str
    instance_type_vec: _containers.RepeatedScalarFieldContainer[str]
    disk_to_device_name_map: _containers.ScalarMap[str, str]
    custom_tag_vec: _containers.RepeatedCompositeFieldContainer[_aws_pb2.AWSFleetParams.Tag]
    def __init__(self, region: _Optional[str] = ..., availability_zone: _Optional[str] = ..., device_name_vec: _Optional[_Iterable[str]] = ..., volume_size_bytes: _Optional[int] = ..., vpc: _Optional[str] = ..., subnet: _Optional[str] = ..., network_security_group_vec: _Optional[_Iterable[str]] = ..., proxy_uuid: _Optional[str] = ..., is_marketplace_proxy: bool = ..., is_exclusive_proxy: bool = ..., instance_type: _Optional[str] = ..., instance_type_vec: _Optional[_Iterable[str]] = ..., disk_to_device_name_map: _Optional[_Mapping[str, str]] = ..., custom_tag_vec: _Optional[_Iterable[_Union[_aws_pb2.AWSFleetParams.Tag, _Mapping]]] = ...) -> None: ...

class GCPProxyInfo(_message.Message):
    __slots__ = ("region", "zone", "device_name", "vpc_network", "subnet", "proxy_uuid", "project_id", "is_exclusive_proxy", "disk_size_gb", "startup_script", "requested_device_name", "fleet_nw_tag_vec", "service_account_name", "kms_key_name", "use_multiple_subnet", "network_params_vec", "network_param_index")
    GCP_PROXY_INFO_FIELD_NUMBER: _ClassVar[int]
    gcp_proxy_info: _descriptor.FieldDescriptor
    REGION_FIELD_NUMBER: _ClassVar[int]
    ZONE_FIELD_NUMBER: _ClassVar[int]
    DEVICE_NAME_FIELD_NUMBER: _ClassVar[int]
    VPC_NETWORK_FIELD_NUMBER: _ClassVar[int]
    SUBNET_FIELD_NUMBER: _ClassVar[int]
    PROXY_UUID_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    IS_EXCLUSIVE_PROXY_FIELD_NUMBER: _ClassVar[int]
    DISK_SIZE_GB_FIELD_NUMBER: _ClassVar[int]
    STARTUP_SCRIPT_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_DEVICE_NAME_FIELD_NUMBER: _ClassVar[int]
    FLEET_NW_TAG_VEC_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNT_NAME_FIELD_NUMBER: _ClassVar[int]
    KMS_KEY_NAME_FIELD_NUMBER: _ClassVar[int]
    USE_MULTIPLE_SUBNET_FIELD_NUMBER: _ClassVar[int]
    NETWORK_PARAMS_VEC_FIELD_NUMBER: _ClassVar[int]
    NETWORK_PARAM_INDEX_FIELD_NUMBER: _ClassVar[int]
    region: str
    zone: str
    device_name: str
    vpc_network: str
    subnet: str
    proxy_uuid: str
    project_id: str
    is_exclusive_proxy: bool
    disk_size_gb: int
    startup_script: str
    requested_device_name: str
    fleet_nw_tag_vec: _containers.RepeatedScalarFieldContainer[str]
    service_account_name: str
    kms_key_name: str
    use_multiple_subnet: bool
    network_params_vec: _containers.RepeatedCompositeFieldContainer[_gcp_pb2.FleetNetworkParams.NetworkParams]
    network_param_index: int
    def __init__(self, region: _Optional[str] = ..., zone: _Optional[str] = ..., device_name: _Optional[str] = ..., vpc_network: _Optional[str] = ..., subnet: _Optional[str] = ..., proxy_uuid: _Optional[str] = ..., project_id: _Optional[str] = ..., is_exclusive_proxy: bool = ..., disk_size_gb: _Optional[int] = ..., startup_script: _Optional[str] = ..., requested_device_name: _Optional[str] = ..., fleet_nw_tag_vec: _Optional[_Iterable[str]] = ..., service_account_name: _Optional[str] = ..., kms_key_name: _Optional[str] = ..., use_multiple_subnet: bool = ..., network_params_vec: _Optional[_Iterable[_Union[_gcp_pb2.FleetNetworkParams.NetworkParams, _Mapping]]] = ..., network_param_index: _Optional[int] = ...) -> None: ...

class BifrostProxyInfo(_message.Message):
    __slots__ = ("constituent_id", "session_id")
    BIFROST_PROXY_INFO_FIELD_NUMBER: _ClassVar[int]
    bifrost_proxy_info: _descriptor.FieldDescriptor
    CONSTITUENT_ID_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    constituent_id: int
    session_id: int
    def __init__(self, constituent_id: _Optional[int] = ..., session_id: _Optional[int] = ...) -> None: ...

class ProxyStateProto(_message.Message):
    __slots__ = ("proxy_info", "num_device_names_assigned", "total_attached_volume_size_bytes", "available_device_names", "last_access_time_secs")
    PROXY_INFO_FIELD_NUMBER: _ClassVar[int]
    NUM_DEVICE_NAMES_ASSIGNED_FIELD_NUMBER: _ClassVar[int]
    TOTAL_ATTACHED_VOLUME_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    AVAILABLE_DEVICE_NAMES_FIELD_NUMBER: _ClassVar[int]
    LAST_ACCESS_TIME_SECS_FIELD_NUMBER: _ClassVar[int]
    proxy_info: ProxyInfo
    num_device_names_assigned: int
    total_attached_volume_size_bytes: int
    available_device_names: _containers.RepeatedScalarFieldContainer[str]
    last_access_time_secs: int
    def __init__(self, proxy_info: _Optional[_Union[ProxyInfo, _Mapping]] = ..., num_device_names_assigned: _Optional[int] = ..., total_attached_volume_size_bytes: _Optional[int] = ..., available_device_names: _Optional[_Iterable[str]] = ..., last_access_time_secs: _Optional[int] = ...) -> None: ...

class AssignProxyArg(_message.Message):
    __slots__ = ("type", "parent_entity_id", "task_id", "task_type")
    Extensions: _python_message._ExtensionDict
    TYPE_FIELD_NUMBER: _ClassVar[int]
    PARENT_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    TASK_TYPE_FIELD_NUMBER: _ClassVar[int]
    type: ProxyInfo.Type
    parent_entity_id: int
    task_id: int
    task_type: TaskType
    def __init__(self, type: _Optional[_Union[ProxyInfo.Type, str]] = ..., parent_entity_id: _Optional[int] = ..., task_id: _Optional[int] = ..., task_type: _Optional[_Union[TaskType, str]] = ...) -> None: ...

class AssignAWSProxyArg(_message.Message):
    __slots__ = ("region", "vpc", "subnet", "volume_size_bytes", "availability_zone", "assign_marketplace_proxy", "assign_exclusive_proxy", "custom_tag_vec", "instance_type_vec", "network_security_group_vec_deprecated")
    ASSIGN_AWS_PROXY_ARG_FIELD_NUMBER: _ClassVar[int]
    assign_aws_proxy_arg: _descriptor.FieldDescriptor
    REGION_FIELD_NUMBER: _ClassVar[int]
    VPC_FIELD_NUMBER: _ClassVar[int]
    SUBNET_FIELD_NUMBER: _ClassVar[int]
    VOLUME_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    AVAILABILITY_ZONE_FIELD_NUMBER: _ClassVar[int]
    ASSIGN_MARKETPLACE_PROXY_FIELD_NUMBER: _ClassVar[int]
    ASSIGN_EXCLUSIVE_PROXY_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_TAG_VEC_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_TYPE_VEC_FIELD_NUMBER: _ClassVar[int]
    NETWORK_SECURITY_GROUP_VEC_DEPRECATED_FIELD_NUMBER: _ClassVar[int]
    region: str
    vpc: str
    subnet: str
    volume_size_bytes: int
    availability_zone: str
    assign_marketplace_proxy: bool
    assign_exclusive_proxy: bool
    custom_tag_vec: _containers.RepeatedCompositeFieldContainer[_aws_pb2.AWSFleetParams.Tag]
    instance_type_vec: _containers.RepeatedScalarFieldContainer[str]
    network_security_group_vec_deprecated: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, region: _Optional[str] = ..., vpc: _Optional[str] = ..., subnet: _Optional[str] = ..., volume_size_bytes: _Optional[int] = ..., availability_zone: _Optional[str] = ..., assign_marketplace_proxy: bool = ..., assign_exclusive_proxy: bool = ..., custom_tag_vec: _Optional[_Iterable[_Union[_aws_pb2.AWSFleetParams.Tag, _Mapping]]] = ..., instance_type_vec: _Optional[_Iterable[str]] = ..., network_security_group_vec_deprecated: _Optional[_Iterable[str]] = ...) -> None: ...

class AssignGCPProxyArg(_message.Message):
    __slots__ = ("region", "zone", "vpc_network", "vpc_subnetwork", "project_id", "assign_exclusive_proxy", "disk_size_gb", "startup_script", "requested_device_name", "fleet_nw_tag_vec", "service_account_name", "kms_key_name", "use_multiple_subnet", "network_params_vec")
    ASSIGN_GCP_PROXY_ARG_FIELD_NUMBER: _ClassVar[int]
    assign_gcp_proxy_arg: _descriptor.FieldDescriptor
    REGION_FIELD_NUMBER: _ClassVar[int]
    ZONE_FIELD_NUMBER: _ClassVar[int]
    VPC_NETWORK_FIELD_NUMBER: _ClassVar[int]
    VPC_SUBNETWORK_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    ASSIGN_EXCLUSIVE_PROXY_FIELD_NUMBER: _ClassVar[int]
    DISK_SIZE_GB_FIELD_NUMBER: _ClassVar[int]
    STARTUP_SCRIPT_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_DEVICE_NAME_FIELD_NUMBER: _ClassVar[int]
    FLEET_NW_TAG_VEC_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNT_NAME_FIELD_NUMBER: _ClassVar[int]
    KMS_KEY_NAME_FIELD_NUMBER: _ClassVar[int]
    USE_MULTIPLE_SUBNET_FIELD_NUMBER: _ClassVar[int]
    NETWORK_PARAMS_VEC_FIELD_NUMBER: _ClassVar[int]
    region: str
    zone: str
    vpc_network: str
    vpc_subnetwork: str
    project_id: str
    assign_exclusive_proxy: bool
    disk_size_gb: int
    startup_script: str
    requested_device_name: str
    fleet_nw_tag_vec: _containers.RepeatedScalarFieldContainer[str]
    service_account_name: str
    kms_key_name: str
    use_multiple_subnet: bool
    network_params_vec: _containers.RepeatedCompositeFieldContainer[_gcp_pb2.FleetNetworkParams.NetworkParams]
    def __init__(self, region: _Optional[str] = ..., zone: _Optional[str] = ..., vpc_network: _Optional[str] = ..., vpc_subnetwork: _Optional[str] = ..., project_id: _Optional[str] = ..., assign_exclusive_proxy: bool = ..., disk_size_gb: _Optional[int] = ..., startup_script: _Optional[str] = ..., requested_device_name: _Optional[str] = ..., fleet_nw_tag_vec: _Optional[_Iterable[str]] = ..., service_account_name: _Optional[str] = ..., kms_key_name: _Optional[str] = ..., use_multiple_subnet: bool = ..., network_params_vec: _Optional[_Iterable[_Union[_gcp_pb2.FleetNetworkParams.NetworkParams, _Mapping]]] = ...) -> None: ...

class AssignBifrostProxyArg(_message.Message):
    __slots__ = ("tenant_id", "network_realm_id", "connector_group_id", "resource_request_vec")
    class ResourceRequest(_message.Message):
        __slots__ = ("resource_type", "usage_requested")
        RESOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
        USAGE_REQUESTED_FIELD_NUMBER: _ClassVar[int]
        resource_type: str
        usage_requested: float
        def __init__(self, resource_type: _Optional[str] = ..., usage_requested: _Optional[float] = ...) -> None: ...
    ASSIGN_BIFROST_PROXY_ARG_FIELD_NUMBER: _ClassVar[int]
    assign_bifrost_proxy_arg: _descriptor.FieldDescriptor
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    NETWORK_REALM_ID_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_REQUEST_VEC_FIELD_NUMBER: _ClassVar[int]
    tenant_id: str
    network_realm_id: int
    connector_group_id: int
    resource_request_vec: _containers.RepeatedCompositeFieldContainer[AssignBifrostProxyArg.ResourceRequest]
    def __init__(self, tenant_id: _Optional[str] = ..., network_realm_id: _Optional[int] = ..., connector_group_id: _Optional[int] = ..., resource_request_vec: _Optional[_Iterable[_Union[AssignBifrostProxyArg.ResourceRequest, _Mapping]]] = ...) -> None: ...
