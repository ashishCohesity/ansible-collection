from magneto.base import error_pb2 as _error_pb2
from magneto.base import magneto_pb2 as _magneto_pb2
from magneto.base import env_params_pb2 as _env_params_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class VMStatus(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kDown: _ClassVar[VMStatus.Type]
        kImageLocked: _ClassVar[VMStatus.Type]
        kMigrating: _ClassVar[VMStatus.Type]
        kNotResponding: _ClassVar[VMStatus.Type]
        kPaused: _ClassVar[VMStatus.Type]
        kPoweringDown: _ClassVar[VMStatus.Type]
        kPoweringUp: _ClassVar[VMStatus.Type]
        kRebootInProgress: _ClassVar[VMStatus.Type]
        kRestoringState: _ClassVar[VMStatus.Type]
        kSavingState: _ClassVar[VMStatus.Type]
        kSuspended: _ClassVar[VMStatus.Type]
        kUnassigned: _ClassVar[VMStatus.Type]
        kUnknown: _ClassVar[VMStatus.Type]
        kUp: _ClassVar[VMStatus.Type]
        kWaitForLaunch: _ClassVar[VMStatus.Type]
        kInvalid: _ClassVar[VMStatus.Type]
    kDown: VMStatus.Type
    kImageLocked: VMStatus.Type
    kMigrating: VMStatus.Type
    kNotResponding: VMStatus.Type
    kPaused: VMStatus.Type
    kPoweringDown: VMStatus.Type
    kPoweringUp: VMStatus.Type
    kRebootInProgress: VMStatus.Type
    kRestoringState: VMStatus.Type
    kSavingState: VMStatus.Type
    kSuspended: VMStatus.Type
    kUnassigned: VMStatus.Type
    kUnknown: VMStatus.Type
    kUp: VMStatus.Type
    kWaitForLaunch: VMStatus.Type
    kInvalid: VMStatus.Type
    def __init__(self) -> None: ...

class SnapshotStatus(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kOk: _ClassVar[SnapshotStatus.Type]
        kLocked: _ClassVar[SnapshotStatus.Type]
        kInPreview: _ClassVar[SnapshotStatus.Type]
        kInvalidStatus: _ClassVar[SnapshotStatus.Type]
    kOk: SnapshotStatus.Type
    kLocked: SnapshotStatus.Type
    kInPreview: SnapshotStatus.Type
    kInvalidStatus: SnapshotStatus.Type
    def __init__(self) -> None: ...

class SnapshotType(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kActive: _ClassVar[SnapshotType.Type]
        kPreview: _ClassVar[SnapshotType.Type]
        kRegular: _ClassVar[SnapshotType.Type]
        kStateless: _ClassVar[SnapshotType.Type]
        kInvalidType: _ClassVar[SnapshotType.Type]
    kActive: SnapshotType.Type
    kPreview: SnapshotType.Type
    kRegular: SnapshotType.Type
    kStateless: SnapshotType.Type
    kInvalidType: SnapshotType.Type
    def __init__(self) -> None: ...

class GetKVMHierarchyArg(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetKVMHierarchyResult(_message.Message):
    __slots__ = ("error", "entity_hierarchy")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ENTITY_HIERARCHY_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    entity_hierarchy: _magneto_pb2.EntityHierarchyProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., entity_hierarchy: _Optional[_Union[_magneto_pb2.EntityHierarchyProto, _Mapping]] = ...) -> None: ...

class CreateVMSnapshotArg(_message.Message):
    __slots__ = ("vm_uuid", "snapshot_name", "dc_uuid")
    VM_UUID_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_NAME_FIELD_NUMBER: _ClassVar[int]
    DC_UUID_FIELD_NUMBER: _ClassVar[int]
    vm_uuid: str
    snapshot_name: str
    dc_uuid: str
    def __init__(self, vm_uuid: _Optional[str] = ..., snapshot_name: _Optional[str] = ..., dc_uuid: _Optional[str] = ...) -> None: ...

class CreateVMSnapshotResult(_message.Message):
    __slots__ = ("error", "snapshot_uuid", "snapshot_info")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_UUID_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_INFO_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    snapshot_uuid: str
    snapshot_info: GetSnapshotInfoResult
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., snapshot_uuid: _Optional[str] = ..., snapshot_info: _Optional[_Union[GetSnapshotInfoResult, _Mapping]] = ...) -> None: ...

class GetSnapshotInfoArg(_message.Message):
    __slots__ = ("dc_uuid", "vm_uuid", "snapshot_uuid")
    DC_UUID_FIELD_NUMBER: _ClassVar[int]
    VM_UUID_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_UUID_FIELD_NUMBER: _ClassVar[int]
    dc_uuid: str
    vm_uuid: str
    snapshot_uuid: str
    def __init__(self, dc_uuid: _Optional[str] = ..., vm_uuid: _Optional[str] = ..., snapshot_uuid: _Optional[str] = ...) -> None: ...

class VirtualDiskInfo(_message.Message):
    __slots__ = ("disk_id", "disk_path", "active_disk_path", "dc_id", "disk_config")
    DISK_ID_FIELD_NUMBER: _ClassVar[int]
    DISK_PATH_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_DISK_PATH_FIELD_NUMBER: _ClassVar[int]
    DC_ID_FIELD_NUMBER: _ClassVar[int]
    DISK_CONFIG_FIELD_NUMBER: _ClassVar[int]
    disk_id: str
    disk_path: str
    active_disk_path: str
    dc_id: str
    disk_config: Disk
    def __init__(self, disk_id: _Optional[str] = ..., disk_path: _Optional[str] = ..., active_disk_path: _Optional[str] = ..., dc_id: _Optional[str] = ..., disk_config: _Optional[_Union[Disk, _Mapping]] = ...) -> None: ...

class GetSnapshotInfoResult(_message.Message):
    __slots__ = ("error", "uuid", "cluster_id", "description", "snapshot_status", "snapshot_type", "disk_vec")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_STATUS_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_TYPE_FIELD_NUMBER: _ClassVar[int]
    DISK_VEC_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    uuid: str
    cluster_id: str
    description: str
    snapshot_status: SnapshotStatus.Type
    snapshot_type: SnapshotType.Type
    disk_vec: _containers.RepeatedCompositeFieldContainer[VirtualDiskInfo]
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., uuid: _Optional[str] = ..., cluster_id: _Optional[str] = ..., description: _Optional[str] = ..., snapshot_status: _Optional[_Union[SnapshotStatus.Type, str]] = ..., snapshot_type: _Optional[_Union[SnapshotType.Type, str]] = ..., disk_vec: _Optional[_Iterable[_Union[VirtualDiskInfo, _Mapping]]] = ...) -> None: ...

class VMDiskListArg(_message.Message):
    __slots__ = ("vm_id", "dc_id")
    VM_ID_FIELD_NUMBER: _ClassVar[int]
    DC_ID_FIELD_NUMBER: _ClassVar[int]
    vm_id: str
    dc_id: str
    def __init__(self, vm_id: _Optional[str] = ..., dc_id: _Optional[str] = ...) -> None: ...

class VMDiskListResult(_message.Message):
    __slots__ = ("disk_vec",)
    DISK_VEC_FIELD_NUMBER: _ClassVar[int]
    disk_vec: _containers.RepeatedCompositeFieldContainer[VirtualDiskInfo]
    def __init__(self, disk_vec: _Optional[_Iterable[_Union[VirtualDiskInfo, _Mapping]]] = ...) -> None: ...

class DeleteVMSnapshotArg(_message.Message):
    __slots__ = ("vm_uuid", "snapshot_uuid", "delete_wait_time_usecs")
    VM_UUID_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_UUID_FIELD_NUMBER: _ClassVar[int]
    DELETE_WAIT_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    vm_uuid: str
    snapshot_uuid: str
    delete_wait_time_usecs: int
    def __init__(self, vm_uuid: _Optional[str] = ..., snapshot_uuid: _Optional[str] = ..., delete_wait_time_usecs: _Optional[int] = ...) -> None: ...

class DeleteVMSnapshotResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class Disk(_message.Message):
    __slots__ = ("name", "logical_bytes", "bootable", "read_only", "shareable", "format", "interface", "wipe_after_delete", "active", "sd_id", "description", "id")
    NAME_FIELD_NUMBER: _ClassVar[int]
    LOGICAL_BYTES_FIELD_NUMBER: _ClassVar[int]
    BOOTABLE_FIELD_NUMBER: _ClassVar[int]
    READ_ONLY_FIELD_NUMBER: _ClassVar[int]
    SHAREABLE_FIELD_NUMBER: _ClassVar[int]
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_FIELD_NUMBER: _ClassVar[int]
    WIPE_AFTER_DELETE_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    SD_ID_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    logical_bytes: int
    bootable: bool
    read_only: bool
    shareable: bool
    format: str
    interface: str
    wipe_after_delete: bool
    active: bool
    sd_id: str
    description: str
    id: str
    def __init__(self, name: _Optional[str] = ..., logical_bytes: _Optional[int] = ..., bootable: bool = ..., read_only: bool = ..., shareable: bool = ..., format: _Optional[str] = ..., interface: _Optional[str] = ..., wipe_after_delete: bool = ..., active: bool = ..., sd_id: _Optional[str] = ..., description: _Optional[str] = ..., id: _Optional[str] = ...) -> None: ...

class VMInfo(_message.Message):
    __slots__ = ("vm_name", "description", "vm_id", "cluster_id", "vm_status", "cpu", "memory_bytes", "os", "disk_vec", "nic_vec", "host_info", "dc_id", "custom_emulated_machine", "type", "comment", "memory_policy", "high_availability", "time_zone")
    class CPU(_message.Message):
        __slots__ = ("topology",)
        class Topology(_message.Message):
            __slots__ = ("sockets", "cores", "threads")
            SOCKETS_FIELD_NUMBER: _ClassVar[int]
            CORES_FIELD_NUMBER: _ClassVar[int]
            THREADS_FIELD_NUMBER: _ClassVar[int]
            sockets: int
            cores: int
            threads: int
            def __init__(self, sockets: _Optional[int] = ..., cores: _Optional[int] = ..., threads: _Optional[int] = ...) -> None: ...
        TOPOLOGY_FIELD_NUMBER: _ClassVar[int]
        topology: VMInfo.CPU.Topology
        def __init__(self, topology: _Optional[_Union[VMInfo.CPU.Topology, _Mapping]] = ...) -> None: ...
    class OSInfo(_message.Message):
        __slots__ = ("boot", "type")
        class Boot(_message.Message):
            __slots__ = ("devices",)
            class Devices(_message.Message):
                __slots__ = ("device",)
                DEVICE_FIELD_NUMBER: _ClassVar[int]
                device: _containers.RepeatedScalarFieldContainer[str]
                def __init__(self, device: _Optional[_Iterable[str]] = ...) -> None: ...
            DEVICES_FIELD_NUMBER: _ClassVar[int]
            devices: VMInfo.OSInfo.Boot.Devices
            def __init__(self, devices: _Optional[_Union[VMInfo.OSInfo.Boot.Devices, _Mapping]] = ...) -> None: ...
        BOOT_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        boot: VMInfo.OSInfo.Boot
        type: str
        def __init__(self, boot: _Optional[_Union[VMInfo.OSInfo.Boot, _Mapping]] = ..., type: _Optional[str] = ...) -> None: ...
    class VMNic(_message.Message):
        __slots__ = ("name", "id", "mac_address", "device_vec", "vnic_profile_id", "network_id")
        class Device(_message.Message):
            __slots__ = ("name", "id", "ip_vec")
            NAME_FIELD_NUMBER: _ClassVar[int]
            ID_FIELD_NUMBER: _ClassVar[int]
            IP_VEC_FIELD_NUMBER: _ClassVar[int]
            name: str
            id: str
            ip_vec: _containers.RepeatedScalarFieldContainer[str]
            def __init__(self, name: _Optional[str] = ..., id: _Optional[str] = ..., ip_vec: _Optional[_Iterable[str]] = ...) -> None: ...
        NAME_FIELD_NUMBER: _ClassVar[int]
        ID_FIELD_NUMBER: _ClassVar[int]
        MAC_ADDRESS_FIELD_NUMBER: _ClassVar[int]
        DEVICE_VEC_FIELD_NUMBER: _ClassVar[int]
        VNIC_PROFILE_ID_FIELD_NUMBER: _ClassVar[int]
        NETWORK_ID_FIELD_NUMBER: _ClassVar[int]
        name: str
        id: str
        mac_address: str
        device_vec: _containers.RepeatedCompositeFieldContainer[VMInfo.VMNic.Device]
        vnic_profile_id: str
        network_id: str
        def __init__(self, name: _Optional[str] = ..., id: _Optional[str] = ..., mac_address: _Optional[str] = ..., device_vec: _Optional[_Iterable[_Union[VMInfo.VMNic.Device, _Mapping]]] = ..., vnic_profile_id: _Optional[str] = ..., network_id: _Optional[str] = ...) -> None: ...
    class HostInfo(_message.Message):
        __slots__ = ("host_name", "ip_addr", "host_id")
        HOST_NAME_FIELD_NUMBER: _ClassVar[int]
        IP_ADDR_FIELD_NUMBER: _ClassVar[int]
        HOST_ID_FIELD_NUMBER: _ClassVar[int]
        host_name: str
        ip_addr: str
        host_id: str
        def __init__(self, host_name: _Optional[str] = ..., ip_addr: _Optional[str] = ..., host_id: _Optional[str] = ...) -> None: ...
    class MemoryPolicy(_message.Message):
        __slots__ = ("guaranteed_bytes", "max_bytes")
        GUARANTEED_BYTES_FIELD_NUMBER: _ClassVar[int]
        MAX_BYTES_FIELD_NUMBER: _ClassVar[int]
        guaranteed_bytes: int
        max_bytes: int
        def __init__(self, guaranteed_bytes: _Optional[int] = ..., max_bytes: _Optional[int] = ...) -> None: ...
    class HighAvailability(_message.Message):
        __slots__ = ("enabled", "priority")
        ENABLED_FIELD_NUMBER: _ClassVar[int]
        PRIORITY_FIELD_NUMBER: _ClassVar[int]
        enabled: bool
        priority: int
        def __init__(self, enabled: bool = ..., priority: _Optional[int] = ...) -> None: ...
    VM_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    VM_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    VM_STATUS_FIELD_NUMBER: _ClassVar[int]
    CPU_FIELD_NUMBER: _ClassVar[int]
    MEMORY_BYTES_FIELD_NUMBER: _ClassVar[int]
    OS_FIELD_NUMBER: _ClassVar[int]
    DISK_VEC_FIELD_NUMBER: _ClassVar[int]
    NIC_VEC_FIELD_NUMBER: _ClassVar[int]
    HOST_INFO_FIELD_NUMBER: _ClassVar[int]
    DC_ID_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_EMULATED_MACHINE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    MEMORY_POLICY_FIELD_NUMBER: _ClassVar[int]
    HIGH_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    TIME_ZONE_FIELD_NUMBER: _ClassVar[int]
    vm_name: str
    description: str
    vm_id: str
    cluster_id: str
    vm_status: VMStatus.Type
    cpu: VMInfo.CPU
    memory_bytes: int
    os: VMInfo.OSInfo
    disk_vec: _containers.RepeatedCompositeFieldContainer[Disk]
    nic_vec: _containers.RepeatedCompositeFieldContainer[VMInfo.VMNic]
    host_info: VMInfo.HostInfo
    dc_id: str
    custom_emulated_machine: str
    type: str
    comment: str
    memory_policy: VMInfo.MemoryPolicy
    high_availability: VMInfo.HighAvailability
    time_zone: str
    def __init__(self, vm_name: _Optional[str] = ..., description: _Optional[str] = ..., vm_id: _Optional[str] = ..., cluster_id: _Optional[str] = ..., vm_status: _Optional[_Union[VMStatus.Type, str]] = ..., cpu: _Optional[_Union[VMInfo.CPU, _Mapping]] = ..., memory_bytes: _Optional[int] = ..., os: _Optional[_Union[VMInfo.OSInfo, _Mapping]] = ..., disk_vec: _Optional[_Iterable[_Union[Disk, _Mapping]]] = ..., nic_vec: _Optional[_Iterable[_Union[VMInfo.VMNic, _Mapping]]] = ..., host_info: _Optional[_Union[VMInfo.HostInfo, _Mapping]] = ..., dc_id: _Optional[str] = ..., custom_emulated_machine: _Optional[str] = ..., type: _Optional[str] = ..., comment: _Optional[str] = ..., memory_policy: _Optional[_Union[VMInfo.MemoryPolicy, _Mapping]] = ..., high_availability: _Optional[_Union[VMInfo.HighAvailability, _Mapping]] = ..., time_zone: _Optional[str] = ...) -> None: ...

class VMInfoArg(_message.Message):
    __slots__ = ("vm_uuid",)
    VM_UUID_FIELD_NUMBER: _ClassVar[int]
    vm_uuid: str
    def __init__(self, vm_uuid: _Optional[str] = ...) -> None: ...

class VMInfoResult(_message.Message):
    __slots__ = ("error", "vm_info")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    VM_INFO_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    vm_info: VMInfo
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., vm_info: _Optional[_Union[VMInfo, _Mapping]] = ...) -> None: ...

class OVirtConfigArg(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class OVirtConfigResult(_message.Message):
    __slots__ = ("name", "version")
    class Version(_message.Message):
        __slots__ = ("major_version", "minor_version", "build_version")
        MAJOR_VERSION_FIELD_NUMBER: _ClassVar[int]
        MINOR_VERSION_FIELD_NUMBER: _ClassVar[int]
        BUILD_VERSION_FIELD_NUMBER: _ClassVar[int]
        major_version: str
        minor_version: str
        build_version: str
        def __init__(self, major_version: _Optional[str] = ..., minor_version: _Optional[str] = ..., build_version: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    name: str
    version: OVirtConfigResult.Version
    def __init__(self, name: _Optional[str] = ..., version: _Optional[_Union[OVirtConfigResult.Version, _Mapping]] = ...) -> None: ...

class CreateVMResult(_message.Message):
    __slots__ = ("error", "vm_id", "disk_path_vec", "host_ip")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    VM_ID_FIELD_NUMBER: _ClassVar[int]
    DISK_PATH_VEC_FIELD_NUMBER: _ClassVar[int]
    HOST_IP_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    vm_id: str
    disk_path_vec: _containers.RepeatedScalarFieldContainer[str]
    host_ip: str
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., vm_id: _Optional[str] = ..., disk_path_vec: _Optional[_Iterable[str]] = ..., host_ip: _Optional[str] = ...) -> None: ...

class RenameVMArg(_message.Message):
    __slots__ = ("vm_id", "vm_name", "vm_description")
    VM_ID_FIELD_NUMBER: _ClassVar[int]
    VM_NAME_FIELD_NUMBER: _ClassVar[int]
    VM_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    vm_id: str
    vm_name: str
    vm_description: str
    def __init__(self, vm_id: _Optional[str] = ..., vm_name: _Optional[str] = ..., vm_description: _Optional[str] = ...) -> None: ...

class PowerStateArg(_message.Message):
    __slots__ = ("vm_id", "power_on")
    VM_ID_FIELD_NUMBER: _ClassVar[int]
    POWER_ON_FIELD_NUMBER: _ClassVar[int]
    vm_id: str
    power_on: bool
    def __init__(self, vm_id: _Optional[str] = ..., power_on: bool = ...) -> None: ...

class PowerStateResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...
