from magneto.base import enums_pb2 as _enums_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NGTEnableStatus(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kUnknown: _ClassVar[NGTEnableStatus.Type]
        kEnabled: _ClassVar[NGTEnableStatus.Type]
        kDisabled: _ClassVar[NGTEnableStatus.Type]
    kUnknown: NGTEnableStatus.Type
    kEnabled: NGTEnableStatus.Type
    kDisabled: NGTEnableStatus.Type
    def __init__(self) -> None: ...

class NGTInstallStatus(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kUnknown: _ClassVar[NGTInstallStatus.Type]
        kInstalled: _ClassVar[NGTInstallStatus.Type]
        kUninstalled: _ClassVar[NGTInstallStatus.Type]
    kUnknown: NGTInstallStatus.Type
    kInstalled: NGTInstallStatus.Type
    kUninstalled: NGTInstallStatus.Type
    def __init__(self) -> None: ...

class NGTCapability(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kUnknown: _ClassVar[NGTCapability.Type]
        kSelfServiceRestore: _ClassVar[NGTCapability.Type]
        kVssSnapshot: _ClassVar[NGTCapability.Type]
    kUnknown: NGTCapability.Type
    kSelfServiceRestore: NGTCapability.Type
    kVssSnapshot: NGTCapability.Type
    def __init__(self) -> None: ...

class NGTInfo(_message.Message):
    __slots__ = ("install_status", "enable_status", "enabled_capability_vec", "version", "reachable")
    INSTALL_STATUS_FIELD_NUMBER: _ClassVar[int]
    ENABLE_STATUS_FIELD_NUMBER: _ClassVar[int]
    ENABLED_CAPABILITY_VEC_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    REACHABLE_FIELD_NUMBER: _ClassVar[int]
    install_status: NGTInstallStatus.Type
    enable_status: NGTEnableStatus.Type
    enabled_capability_vec: _containers.RepeatedScalarFieldContainer[NGTCapability.Type]
    version: str
    reachable: bool
    def __init__(self, install_status: _Optional[_Union[NGTInstallStatus.Type, str]] = ..., enable_status: _Optional[_Union[NGTEnableStatus.Type, str]] = ..., enabled_capability_vec: _Optional[_Iterable[_Union[NGTCapability.Type, str]]] = ..., version: _Optional[str] = ..., reachable: bool = ...) -> None: ...

class VirtualDiskConfig(_message.Message):
    __slots__ = ("disk_size_bytes", "uuid", "device_index", "device_bus")
    DISK_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_INDEX_FIELD_NUMBER: _ClassVar[int]
    DEVICE_BUS_FIELD_NUMBER: _ClassVar[int]
    disk_size_bytes: int
    uuid: str
    device_index: int
    device_bus: str
    def __init__(self, disk_size_bytes: _Optional[int] = ..., uuid: _Optional[str] = ..., device_index: _Optional[int] = ..., device_bus: _Optional[str] = ...) -> None: ...

class Entity(_message.Message):
    __slots__ = ("type", "uuid", "cluster_uuid", "name", "description", "is_agent_vm", "host_type", "version", "ngt_info", "management_server", "hypervisor_vm_uuid", "running_on_ndfs", "non_ndfs_details", "virtual_disk_config_vec")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kPrismCentral: _ClassVar[Entity.Type]
        kStandaloneCluster: _ClassVar[Entity.Type]
        kOtherHypervisorCluster: _ClassVar[Entity.Type]
        kCluster: _ClassVar[Entity.Type]
        kHost: _ClassVar[Entity.Type]
        kVirtualMachine: _ClassVar[Entity.Type]
        kNetwork: _ClassVar[Entity.Type]
        kStorageContainer: _ClassVar[Entity.Type]
        kGenericStandaloneCluster: _ClassVar[Entity.Type]
    kPrismCentral: Entity.Type
    kStandaloneCluster: Entity.Type
    kOtherHypervisorCluster: Entity.Type
    kCluster: Entity.Type
    kHost: Entity.Type
    kVirtualMachine: Entity.Type
    kNetwork: Entity.Type
    kStorageContainer: Entity.Type
    kGenericStandaloneCluster: Entity.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_UUID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    IS_AGENT_VM_FIELD_NUMBER: _ClassVar[int]
    HOST_TYPE_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    NGT_INFO_FIELD_NUMBER: _ClassVar[int]
    MANAGEMENT_SERVER_FIELD_NUMBER: _ClassVar[int]
    HYPERVISOR_VM_UUID_FIELD_NUMBER: _ClassVar[int]
    RUNNING_ON_NDFS_FIELD_NUMBER: _ClassVar[int]
    NON_NDFS_DETAILS_FIELD_NUMBER: _ClassVar[int]
    VIRTUAL_DISK_CONFIG_VEC_FIELD_NUMBER: _ClassVar[int]
    type: Entity.Type
    uuid: str
    cluster_uuid: str
    name: str
    description: str
    is_agent_vm: bool
    host_type: _enums_pb2.HostEnv.Type
    version: str
    ngt_info: NGTInfo
    management_server: ManagementServer
    hypervisor_vm_uuid: str
    running_on_ndfs: bool
    non_ndfs_details: str
    virtual_disk_config_vec: _containers.RepeatedCompositeFieldContainer[VirtualDiskConfig]
    def __init__(self, type: _Optional[_Union[Entity.Type, str]] = ..., uuid: _Optional[str] = ..., cluster_uuid: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., is_agent_vm: bool = ..., host_type: _Optional[_Union[_enums_pb2.HostEnv.Type, str]] = ..., version: _Optional[str] = ..., ngt_info: _Optional[_Union[NGTInfo, _Mapping]] = ..., management_server: _Optional[_Union[ManagementServer, _Mapping]] = ..., hypervisor_vm_uuid: _Optional[str] = ..., running_on_ndfs: bool = ..., non_ndfs_details: _Optional[str] = ..., virtual_disk_config_vec: _Optional[_Iterable[_Union[VirtualDiskConfig, _Mapping]]] = ...) -> None: ...

class ManagementServer(_message.Message):
    __slots__ = ("type", "ip_address")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kVCenter: _ClassVar[ManagementServer.Type]
        kUnknown: _ClassVar[ManagementServer.Type]
    kVCenter: ManagementServer.Type
    kUnknown: ManagementServer.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    type: ManagementServer.Type
    ip_address: str
    def __init__(self, type: _Optional[_Union[ManagementServer.Type, str]] = ..., ip_address: _Optional[str] = ...) -> None: ...
