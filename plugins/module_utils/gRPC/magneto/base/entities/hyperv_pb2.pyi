from magneto.base.entities import agent_pb2 as _agent_pb2
from magneto.base import enums_pb2 as _enums_pb2
from magneto.base import error_pb2 as _error_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SupportedBackupType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kRctBackup: _ClassVar[SupportedBackupType]
    kVssBackup: _ClassVar[SupportedBackupType]
kRctBackup: SupportedBackupType
kVssBackup: SupportedBackupType

class DatastoreInfo(_message.Message):
    __slots__ = ("datastore_type", "capacity", "free_space", "mount_point_vec", "highly_available")
    class DatastoreType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kFileShare: _ClassVar[DatastoreInfo.DatastoreType]
        kVolume: _ClassVar[DatastoreInfo.DatastoreType]
    kFileShare: DatastoreInfo.DatastoreType
    kVolume: DatastoreInfo.DatastoreType
    DATASTORE_TYPE_FIELD_NUMBER: _ClassVar[int]
    CAPACITY_FIELD_NUMBER: _ClassVar[int]
    FREE_SPACE_FIELD_NUMBER: _ClassVar[int]
    MOUNT_POINT_VEC_FIELD_NUMBER: _ClassVar[int]
    HIGHLY_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    datastore_type: DatastoreInfo.DatastoreType
    capacity: int
    free_space: int
    mount_point_vec: _containers.RepeatedScalarFieldContainer[str]
    highly_available: bool
    def __init__(self, datastore_type: _Optional[_Union[DatastoreInfo.DatastoreType, str]] = ..., capacity: _Optional[int] = ..., free_space: _Optional[int] = ..., mount_point_vec: _Optional[_Iterable[str]] = ..., highly_available: bool = ...) -> None: ...

class VirtualDiskBasicInfo(_message.Message):
    __slots__ = ("location", "vol_id", "vol_name", "unit_number", "controller_bus_number", "controller_type")
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    VOL_ID_FIELD_NUMBER: _ClassVar[int]
    VOL_NAME_FIELD_NUMBER: _ClassVar[int]
    UNIT_NUMBER_FIELD_NUMBER: _ClassVar[int]
    CONTROLLER_BUS_NUMBER_FIELD_NUMBER: _ClassVar[int]
    CONTROLLER_TYPE_FIELD_NUMBER: _ClassVar[int]
    location: str
    vol_id: str
    vol_name: str
    unit_number: int
    controller_bus_number: int
    controller_type: str
    def __init__(self, location: _Optional[str] = ..., vol_id: _Optional[str] = ..., vol_name: _Optional[str] = ..., unit_number: _Optional[int] = ..., controller_bus_number: _Optional[int] = ..., controller_type: _Optional[str] = ...) -> None: ...

class VirtualMachineInfo(_message.Message):
    __slots__ = ("version", "generation", "backup_status", "backup_type", "highly_available", "computer_name", "host_type", "os_name", "tag", "ip_address_vec", "virtual_disk_info_vec", "checkpoints", "physical_size_in_bytes")
    class VMBackupStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kSupported: _ClassVar[VirtualMachineInfo.VMBackupStatus]
        kUnsupportedConfig: _ClassVar[VirtualMachineInfo.VMBackupStatus]
        kMissing: _ClassVar[VirtualMachineInfo.VMBackupStatus]
    kSupported: VirtualMachineInfo.VMBackupStatus
    kUnsupportedConfig: VirtualMachineInfo.VMBackupStatus
    kMissing: VirtualMachineInfo.VMBackupStatus
    VERSION_FIELD_NUMBER: _ClassVar[int]
    GENERATION_FIELD_NUMBER: _ClassVar[int]
    BACKUP_STATUS_FIELD_NUMBER: _ClassVar[int]
    BACKUP_TYPE_FIELD_NUMBER: _ClassVar[int]
    HIGHLY_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    COMPUTER_NAME_FIELD_NUMBER: _ClassVar[int]
    HOST_TYPE_FIELD_NUMBER: _ClassVar[int]
    OS_NAME_FIELD_NUMBER: _ClassVar[int]
    TAG_FIELD_NUMBER: _ClassVar[int]
    IP_ADDRESS_VEC_FIELD_NUMBER: _ClassVar[int]
    VIRTUAL_DISK_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    CHECKPOINTS_FIELD_NUMBER: _ClassVar[int]
    PHYSICAL_SIZE_IN_BYTES_FIELD_NUMBER: _ClassVar[int]
    version: str
    generation: int
    backup_status: VirtualMachineInfo.VMBackupStatus
    backup_type: SupportedBackupType
    highly_available: bool
    computer_name: str
    host_type: _enums_pb2.HostEnv.Type
    os_name: str
    tag: str
    ip_address_vec: _containers.RepeatedScalarFieldContainer[str]
    virtual_disk_info_vec: _containers.RepeatedCompositeFieldContainer[VirtualDiskBasicInfo]
    checkpoints: int
    physical_size_in_bytes: int
    def __init__(self, version: _Optional[str] = ..., generation: _Optional[int] = ..., backup_status: _Optional[_Union[VirtualMachineInfo.VMBackupStatus, str]] = ..., backup_type: _Optional[_Union[SupportedBackupType, str]] = ..., highly_available: bool = ..., computer_name: _Optional[str] = ..., host_type: _Optional[_Union[_enums_pb2.HostEnv.Type, str]] = ..., os_name: _Optional[str] = ..., tag: _Optional[str] = ..., ip_address_vec: _Optional[_Iterable[str]] = ..., virtual_disk_info_vec: _Optional[_Iterable[_Union[VirtualDiskBasicInfo, _Mapping]]] = ..., checkpoints: _Optional[int] = ..., physical_size_in_bytes: _Optional[int] = ...) -> None: ...

class TagAttributes(_message.Message):
    __slots__ = ("entity_id", "uuid", "name", "custom_property_name")
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_PROPERTY_NAME_FIELD_NUMBER: _ClassVar[int]
    entity_id: int
    uuid: str
    name: str
    custom_property_name: str
    def __init__(self, entity_id: _Optional[int] = ..., uuid: _Optional[str] = ..., name: _Optional[str] = ..., custom_property_name: _Optional[str] = ...) -> None: ...

class Entity(_message.Message):
    __slots__ = ("type", "uuid", "hyperv_uuid", "name", "agent_error", "agent_status_vec", "cluster_name", "domain_name", "description", "datastore_info", "vm_info", "version", "build_number", "backup_type", "tag_attributes_vec")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kSCVMMServer: _ClassVar[Entity.Type]
        kStandaloneHost: _ClassVar[Entity.Type]
        kStandaloneCluster: _ClassVar[Entity.Type]
        kHostGroup: _ClassVar[Entity.Type]
        kHypervHost: _ClassVar[Entity.Type]
        kHostCluster: _ClassVar[Entity.Type]
        kVirtualMachine: _ClassVar[Entity.Type]
        kNetwork: _ClassVar[Entity.Type]
        kDatastore: _ClassVar[Entity.Type]
        kTag: _ClassVar[Entity.Type]
        kCustomProperty: _ClassVar[Entity.Type]
    kSCVMMServer: Entity.Type
    kStandaloneHost: Entity.Type
    kStandaloneCluster: Entity.Type
    kHostGroup: Entity.Type
    kHypervHost: Entity.Type
    kHostCluster: Entity.Type
    kVirtualMachine: Entity.Type
    kNetwork: Entity.Type
    kDatastore: Entity.Type
    kTag: Entity.Type
    kCustomProperty: Entity.Type
    class WindowsVersion(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kWindows2012R2: _ClassVar[Entity.WindowsVersion]
        kWindows2016: _ClassVar[Entity.WindowsVersion]
        kUnsupported: _ClassVar[Entity.WindowsVersion]
    kWindows2012R2: Entity.WindowsVersion
    kWindows2016: Entity.WindowsVersion
    kUnsupported: Entity.WindowsVersion
    TYPE_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    HYPERV_UUID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    AGENT_ERROR_FIELD_NUMBER: _ClassVar[int]
    AGENT_STATUS_VEC_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_NAME_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DATASTORE_INFO_FIELD_NUMBER: _ClassVar[int]
    VM_INFO_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    BUILD_NUMBER_FIELD_NUMBER: _ClassVar[int]
    BACKUP_TYPE_FIELD_NUMBER: _ClassVar[int]
    TAG_ATTRIBUTES_VEC_FIELD_NUMBER: _ClassVar[int]
    type: Entity.Type
    uuid: str
    hyperv_uuid: str
    name: str
    agent_error: _error_pb2.ErrorProto
    agent_status_vec: _containers.RepeatedCompositeFieldContainer[_agent_pb2.HostAgentStatus]
    cluster_name: str
    domain_name: str
    description: str
    datastore_info: DatastoreInfo
    vm_info: VirtualMachineInfo
    version: Entity.WindowsVersion
    build_number: str
    backup_type: SupportedBackupType
    tag_attributes_vec: _containers.RepeatedCompositeFieldContainer[TagAttributes]
    def __init__(self, type: _Optional[_Union[Entity.Type, str]] = ..., uuid: _Optional[str] = ..., hyperv_uuid: _Optional[str] = ..., name: _Optional[str] = ..., agent_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., agent_status_vec: _Optional[_Iterable[_Union[_agent_pb2.HostAgentStatus, _Mapping]]] = ..., cluster_name: _Optional[str] = ..., domain_name: _Optional[str] = ..., description: _Optional[str] = ..., datastore_info: _Optional[_Union[DatastoreInfo, _Mapping]] = ..., vm_info: _Optional[_Union[VirtualMachineInfo, _Mapping]] = ..., version: _Optional[_Union[Entity.WindowsVersion, str]] = ..., build_number: _Optional[str] = ..., backup_type: _Optional[_Union[SupportedBackupType, str]] = ..., tag_attributes_vec: _Optional[_Iterable[_Union[TagAttributes, _Mapping]]] = ...) -> None: ...
