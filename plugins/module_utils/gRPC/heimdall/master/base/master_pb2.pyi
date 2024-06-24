from heimdall.base import error_pb2 as _error_pb2
from heimdall.master.stub import rpc_service_pb2 as _rpc_service_pb2
from magneto.base import magneto_pb2 as _magneto_pb2
from magneto.base import env_params_pb2 as _env_params_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf.internal import python_message as _python_message
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FleetAgent(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kYodaAgent: _ClassVar[FleetAgent]
    kStorageProxy: _ClassVar[FleetAgent]
    kWindowsAgent: _ClassVar[FleetAgent]

class FleetResourceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kNetwork: _ClassVar[FleetResourceType]
    kCPU: _ClassVar[FleetResourceType]

class UpdateType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kLaunchIntentLogged: _ClassVar[UpdateType]
    kResourceCreated: _ClassVar[UpdateType]
    kResourceDeleted: _ClassVar[UpdateType]
    kRequestAssigned: _ClassVar[UpdateType]
    kRequestReleased: _ClassVar[UpdateType]
    kNewError: _ClassVar[UpdateType]

class DiskPartitionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kStandard: _ClassVar[DiskPartitionType]
    kLVM: _ClassVar[DiskPartitionType]

class FileSystemType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kEXT4: _ClassVar[FileSystemType]
    kXFS: _ClassVar[FileSystemType]
kYodaAgent: FleetAgent
kStorageProxy: FleetAgent
kWindowsAgent: FleetAgent
kNetwork: FleetResourceType
kCPU: FleetResourceType
kLaunchIntentLogged: UpdateType
kResourceCreated: UpdateType
kResourceDeleted: UpdateType
kRequestAssigned: UpdateType
kRequestReleased: UpdateType
kNewError: UpdateType
kStandard: DiskPartitionType
kLVM: DiskPartitionType
kEXT4: FileSystemType
kXFS: FileSystemType

class FleetInfo(_message.Message):
    __slots__ = ("ip_address", "status", "agents_health", "os_type", "id", "environment", "source_entity_id", "request_map", "error", "name", "workflow_type", "create_time_secs", "last_release_time_secs")
    Extensions: _python_message._ExtensionDict
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kLaunchIntentLogged: _ClassVar[FleetInfo.Status]
        kLaunched: _ClassVar[FleetInfo.Status]
        kAddedToClusterConfig: _ClassVar[FleetInfo.Status]
        kAgentsStarted: _ClassVar[FleetInfo.Status]
        kRemovedFromClusterConfig: _ClassVar[FleetInfo.Status]
        kTerminationInProgress: _ClassVar[FleetInfo.Status]
        kTerminated: _ClassVar[FleetInfo.Status]
    kLaunchIntentLogged: FleetInfo.Status
    kLaunched: FleetInfo.Status
    kAddedToClusterConfig: FleetInfo.Status
    kAgentsStarted: FleetInfo.Status
    kRemovedFromClusterConfig: FleetInfo.Status
    kTerminationInProgress: FleetInfo.Status
    kTerminated: FleetInfo.Status
    class AgentsHealthEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _error_pb2.ErrorProto
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...
    class RequestMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: Request
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[Request, _Mapping]] = ...) -> None: ...
    IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    AGENTS_HEALTH_FIELD_NUMBER: _ClassVar[int]
    OS_TYPE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    SOURCE_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    REQUEST_MAP_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_TYPE_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_SECS_FIELD_NUMBER: _ClassVar[int]
    LAST_RELEASE_TIME_SECS_FIELD_NUMBER: _ClassVar[int]
    ip_address: str
    status: FleetInfo.Status
    agents_health: _containers.MessageMap[str, _error_pb2.ErrorProto]
    os_type: _rpc_service_pb2.FleetOSType
    id: str
    environment: _rpc_service_pb2.Environment
    source_entity_id: int
    request_map: _containers.MessageMap[str, Request]
    error: _error_pb2.ErrorProto
    name: str
    workflow_type: _rpc_service_pb2.WorkflowType
    create_time_secs: int
    last_release_time_secs: int
    def __init__(self, ip_address: _Optional[str] = ..., status: _Optional[_Union[FleetInfo.Status, str]] = ..., agents_health: _Optional[_Mapping[str, _error_pb2.ErrorProto]] = ..., os_type: _Optional[_Union[_rpc_service_pb2.FleetOSType, str]] = ..., id: _Optional[str] = ..., environment: _Optional[_Union[_rpc_service_pb2.Environment, str]] = ..., source_entity_id: _Optional[int] = ..., request_map: _Optional[_Mapping[str, Request]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., name: _Optional[str] = ..., workflow_type: _Optional[_Union[_rpc_service_pb2.WorkflowType, str]] = ..., create_time_secs: _Optional[int] = ..., last_release_time_secs: _Optional[int] = ...) -> None: ...

class ResourceInfo(_message.Message):
    __slots__ = ("id", "name", "environment", "source_entity_id", "status", "request_map", "error", "workflow_type", "resource_type", "create_time_secs", "last_release_time_secs", "rigel_info", "fleet_info", "disk_access_info", "disks_info")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kCreateIntentLogged: _ClassVar[ResourceInfo.Status]
        kCreated: _ClassVar[ResourceInfo.Status]
        kDeletionInProgress: _ClassVar[ResourceInfo.Status]
        kDeleted: _ClassVar[ResourceInfo.Status]
        kReleaseInProgress: _ClassVar[ResourceInfo.Status]
        kReleased: _ClassVar[ResourceInfo.Status]
    kCreateIntentLogged: ResourceInfo.Status
    kCreated: ResourceInfo.Status
    kDeletionInProgress: ResourceInfo.Status
    kDeleted: ResourceInfo.Status
    kReleaseInProgress: ResourceInfo.Status
    kReleased: ResourceInfo.Status
    class RequestMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: Request
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[Request, _Mapping]] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    SOURCE_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    REQUEST_MAP_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_TYPE_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_SECS_FIELD_NUMBER: _ClassVar[int]
    LAST_RELEASE_TIME_SECS_FIELD_NUMBER: _ClassVar[int]
    RIGEL_INFO_FIELD_NUMBER: _ClassVar[int]
    FLEET_INFO_FIELD_NUMBER: _ClassVar[int]
    DISK_ACCESS_INFO_FIELD_NUMBER: _ClassVar[int]
    DISKS_INFO_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    environment: _rpc_service_pb2.Environment
    source_entity_id: int
    status: ResourceInfo.Status
    request_map: _containers.MessageMap[str, Request]
    error: _error_pb2.ErrorProto
    workflow_type: _rpc_service_pb2.WorkflowType
    resource_type: _rpc_service_pb2.ResourceType
    create_time_secs: int
    last_release_time_secs: int
    rigel_info: _rpc_service_pb2.RigelInfo
    fleet_info: FleetInfo
    disk_access_info: DiskAccessInfo
    disks_info: DisksInfo
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., environment: _Optional[_Union[_rpc_service_pb2.Environment, str]] = ..., source_entity_id: _Optional[int] = ..., status: _Optional[_Union[ResourceInfo.Status, str]] = ..., request_map: _Optional[_Mapping[str, Request]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., workflow_type: _Optional[_Union[_rpc_service_pb2.WorkflowType, str]] = ..., resource_type: _Optional[_Union[_rpc_service_pb2.ResourceType, str]] = ..., create_time_secs: _Optional[int] = ..., last_release_time_secs: _Optional[int] = ..., rigel_info: _Optional[_Union[_rpc_service_pb2.RigelInfo, _Mapping]] = ..., fleet_info: _Optional[_Union[FleetInfo, _Mapping]] = ..., disk_access_info: _Optional[_Union[DiskAccessInfo, _Mapping]] = ..., disks_info: _Optional[_Union[DisksInfo, _Mapping]] = ...) -> None: ...

class DiskAccessInfo(_message.Message):
    __slots__ = ("name", "disk_access_id", "private_endpoint_name", "private_endpoint_id", "private_endpoint_fqdn", "private_endpoint_ipv4_address")
    Extensions: _python_message._ExtensionDict
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISK_ACCESS_ID_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_ENDPOINT_NAME_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_ENDPOINT_ID_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_ENDPOINT_FQDN_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_ENDPOINT_IPV4_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    name: str
    disk_access_id: str
    private_endpoint_name: str
    private_endpoint_id: str
    private_endpoint_fqdn: str
    private_endpoint_ipv4_address: str
    def __init__(self, name: _Optional[str] = ..., disk_access_id: _Optional[str] = ..., private_endpoint_name: _Optional[str] = ..., private_endpoint_id: _Optional[str] = ..., private_endpoint_fqdn: _Optional[str] = ..., private_endpoint_ipv4_address: _Optional[str] = ...) -> None: ...

class DisksInfo(_message.Message):
    __slots__ = ("number_of_disks", "size_bytes", "status", "disk_info_vec", "is_resize_required", "last_modified_time_secs")
    Extensions: _python_message._ExtensionDict
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kLaunchIntentLogged: _ClassVar[DisksInfo.Status]
        kLaunched: _ClassVar[DisksInfo.Status]
        kResized: _ClassVar[DisksInfo.Status]
        kAttached: _ClassVar[DisksInfo.Status]
        kMounted: _ClassVar[DisksInfo.Status]
        kReadyToUse: _ClassVar[DisksInfo.Status]
    kLaunchIntentLogged: DisksInfo.Status
    kLaunched: DisksInfo.Status
    kResized: DisksInfo.Status
    kAttached: DisksInfo.Status
    kMounted: DisksInfo.Status
    kReadyToUse: DisksInfo.Status
    class DiskInfo(_message.Message):
        __slots__ = ("disk_id", "device_name", "lun")
        DISK_ID_FIELD_NUMBER: _ClassVar[int]
        DEVICE_NAME_FIELD_NUMBER: _ClassVar[int]
        LUN_FIELD_NUMBER: _ClassVar[int]
        disk_id: str
        device_name: str
        lun: int
        def __init__(self, disk_id: _Optional[str] = ..., device_name: _Optional[str] = ..., lun: _Optional[int] = ...) -> None: ...
    NUMBER_OF_DISKS_FIELD_NUMBER: _ClassVar[int]
    SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    DISK_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    IS_RESIZE_REQUIRED_FIELD_NUMBER: _ClassVar[int]
    LAST_MODIFIED_TIME_SECS_FIELD_NUMBER: _ClassVar[int]
    number_of_disks: int
    size_bytes: int
    status: DisksInfo.Status
    disk_info_vec: _containers.RepeatedCompositeFieldContainer[DisksInfo.DiskInfo]
    is_resize_required: bool
    last_modified_time_secs: int
    def __init__(self, number_of_disks: _Optional[int] = ..., size_bytes: _Optional[int] = ..., status: _Optional[_Union[DisksInfo.Status, str]] = ..., disk_info_vec: _Optional[_Iterable[_Union[DisksInfo.DiskInfo, _Mapping]]] = ..., is_resize_required: bool = ..., last_modified_time_secs: _Optional[int] = ...) -> None: ...

class Request(_message.Message):
    __slots__ = ("id", "workflow_type", "acquire_timestamp_secs", "requested_resource_type", "requested_resources_map")
    ID_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_TYPE_FIELD_NUMBER: _ClassVar[int]
    ACQUIRE_TIMESTAMP_SECS_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_RESOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_RESOURCES_MAP_FIELD_NUMBER: _ClassVar[int]
    id: str
    workflow_type: _rpc_service_pb2.WorkflowType
    acquire_timestamp_secs: int
    requested_resource_type: _rpc_service_pb2.ResourceType
    requested_resources_map: _rpc_service_pb2.ResourceWeightMap
    def __init__(self, id: _Optional[str] = ..., workflow_type: _Optional[_Union[_rpc_service_pb2.WorkflowType, str]] = ..., acquire_timestamp_secs: _Optional[int] = ..., requested_resource_type: _Optional[_Union[_rpc_service_pb2.ResourceType, str]] = ..., requested_resources_map: _Optional[_Union[_rpc_service_pb2.ResourceWeightMap, _Mapping]] = ...) -> None: ...

class ListOfString(_message.Message):
    __slots__ = ("values",)
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, values: _Optional[_Iterable[str]] = ...) -> None: ...

class HeimdallConnectorParams(_message.Message):
    __slots__ = ("connector_params",)
    Extensions: _python_message._ExtensionDict
    CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    connector_params: _magneto_pb2.ConnectorParams
    def __init__(self, connector_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ...) -> None: ...

class OSToAMIMap(_message.Message):
    __slots__ = ("os_to_ami_map",)
    class OsToAmiMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    OS_TO_AMI_MAP_FIELD_NUMBER: _ClassVar[int]
    os_to_ami_map: _containers.ScalarMap[str, str]
    def __init__(self, os_to_ami_map: _Optional[_Mapping[str, str]] = ...) -> None: ...

class HeimdallConfig(_message.Message):
    __slots__ = ("workflow_weight_map", "resource_name_vec")
    class WorkflowWeightMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _rpc_service_pb2.ResourceWeightMap
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_rpc_service_pb2.ResourceWeightMap, _Mapping]] = ...) -> None: ...
    WORKFLOW_WEIGHT_MAP_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_NAME_VEC_FIELD_NUMBER: _ClassVar[int]
    workflow_weight_map: _containers.MessageMap[str, _rpc_service_pb2.ResourceWeightMap]
    resource_name_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, workflow_weight_map: _Optional[_Mapping[str, _rpc_service_pb2.ResourceWeightMap]] = ..., resource_name_vec: _Optional[_Iterable[str]] = ...) -> None: ...

class CloudzMapKey(_message.Message):
    __slots__ = ("source_entity_id", "region", "environment", "workflow_type")
    SOURCE_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_TYPE_FIELD_NUMBER: _ClassVar[int]
    source_entity_id: int
    region: str
    environment: _rpc_service_pb2.Environment
    workflow_type: _rpc_service_pb2.WorkflowType
    def __init__(self, source_entity_id: _Optional[int] = ..., region: _Optional[str] = ..., environment: _Optional[_Union[_rpc_service_pb2.Environment, str]] = ..., workflow_type: _Optional[_Union[_rpc_service_pb2.WorkflowType, str]] = ...) -> None: ...
