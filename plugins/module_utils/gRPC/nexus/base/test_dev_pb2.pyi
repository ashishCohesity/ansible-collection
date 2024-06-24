from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class VMConfig(_message.Message):
    __slots__ = ("vm_uuid", "vm_name", "memory", "vcpus", "interface_name", "mac_addr", "host_id", "vm_state", "magneto_view_name", "volume_name", "migrating_hostIP", "lunID", "vm_creation_time", "vm_ip", "target_name", "storage", "vnc_port", "websocket_port", "host_name", "host_ip", "interfaces_cnt", "completion_percentage", "vm_create_error")
    class VMState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kCreating: _ClassVar[VMConfig.VMState]
        kCreated: _ClassVar[VMConfig.VMState]
        kRunning: _ClassVar[VMConfig.VMState]
        kStopped: _ClassVar[VMConfig.VMState]
        kPaused: _ClassVar[VMConfig.VMState]
        kRemoving: _ClassVar[VMConfig.VMState]
        kMigrating: _ClassVar[VMConfig.VMState]
        kMigrated: _ClassVar[VMConfig.VMState]
        kConverting: _ClassVar[VMConfig.VMState]
        kConverted: _ClassVar[VMConfig.VMState]
        kFailed: _ClassVar[VMConfig.VMState]
    kCreating: VMConfig.VMState
    kCreated: VMConfig.VMState
    kRunning: VMConfig.VMState
    kStopped: VMConfig.VMState
    kPaused: VMConfig.VMState
    kRemoving: VMConfig.VMState
    kMigrating: VMConfig.VMState
    kMigrated: VMConfig.VMState
    kConverting: VMConfig.VMState
    kConverted: VMConfig.VMState
    kFailed: VMConfig.VMState
    VM_UUID_FIELD_NUMBER: _ClassVar[int]
    VM_NAME_FIELD_NUMBER: _ClassVar[int]
    MEMORY_FIELD_NUMBER: _ClassVar[int]
    VCPUS_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_NAME_FIELD_NUMBER: _ClassVar[int]
    MAC_ADDR_FIELD_NUMBER: _ClassVar[int]
    HOST_ID_FIELD_NUMBER: _ClassVar[int]
    VM_STATE_FIELD_NUMBER: _ClassVar[int]
    MAGNETO_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    VOLUME_NAME_FIELD_NUMBER: _ClassVar[int]
    MIGRATING_HOSTIP_FIELD_NUMBER: _ClassVar[int]
    LUNID_FIELD_NUMBER: _ClassVar[int]
    VM_CREATION_TIME_FIELD_NUMBER: _ClassVar[int]
    VM_IP_FIELD_NUMBER: _ClassVar[int]
    TARGET_NAME_FIELD_NUMBER: _ClassVar[int]
    STORAGE_FIELD_NUMBER: _ClassVar[int]
    VNC_PORT_FIELD_NUMBER: _ClassVar[int]
    WEBSOCKET_PORT_FIELD_NUMBER: _ClassVar[int]
    HOST_NAME_FIELD_NUMBER: _ClassVar[int]
    HOST_IP_FIELD_NUMBER: _ClassVar[int]
    INTERFACES_CNT_FIELD_NUMBER: _ClassVar[int]
    COMPLETION_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    VM_CREATE_ERROR_FIELD_NUMBER: _ClassVar[int]
    vm_uuid: str
    vm_name: str
    memory: int
    vcpus: int
    interface_name: str
    mac_addr: _containers.RepeatedScalarFieldContainer[str]
    host_id: str
    vm_state: VMConfig.VMState
    magneto_view_name: str
    volume_name: _containers.RepeatedScalarFieldContainer[str]
    migrating_hostIP: str
    lunID: _containers.RepeatedScalarFieldContainer[str]
    vm_creation_time: int
    vm_ip: str
    target_name: _containers.RepeatedScalarFieldContainer[str]
    storage: int
    vnc_port: int
    websocket_port: int
    host_name: str
    host_ip: str
    interfaces_cnt: int
    completion_percentage: float
    vm_create_error: str
    def __init__(self, vm_uuid: _Optional[str] = ..., vm_name: _Optional[str] = ..., memory: _Optional[int] = ..., vcpus: _Optional[int] = ..., interface_name: _Optional[str] = ..., mac_addr: _Optional[_Iterable[str]] = ..., host_id: _Optional[str] = ..., vm_state: _Optional[_Union[VMConfig.VMState, str]] = ..., magneto_view_name: _Optional[str] = ..., volume_name: _Optional[_Iterable[str]] = ..., migrating_hostIP: _Optional[str] = ..., lunID: _Optional[_Iterable[str]] = ..., vm_creation_time: _Optional[int] = ..., vm_ip: _Optional[str] = ..., target_name: _Optional[_Iterable[str]] = ..., storage: _Optional[int] = ..., vnc_port: _Optional[int] = ..., websocket_port: _Optional[int] = ..., host_name: _Optional[str] = ..., host_ip: _Optional[str] = ..., interfaces_cnt: _Optional[int] = ..., completion_percentage: _Optional[float] = ..., vm_create_error: _Optional[str] = ...) -> None: ...

class VmHostCapacity(_message.Message):
    __slots__ = ("host_id", "host_memory")
    class HostMemUsage(_message.Message):
        __slots__ = ("allocated_mem", "used_mem", "reserved_mem")
        ALLOCATED_MEM_FIELD_NUMBER: _ClassVar[int]
        USED_MEM_FIELD_NUMBER: _ClassVar[int]
        RESERVED_MEM_FIELD_NUMBER: _ClassVar[int]
        allocated_mem: int
        used_mem: int
        reserved_mem: int
        def __init__(self, allocated_mem: _Optional[int] = ..., used_mem: _Optional[int] = ..., reserved_mem: _Optional[int] = ...) -> None: ...
    HOST_ID_FIELD_NUMBER: _ClassVar[int]
    HOST_MEMORY_FIELD_NUMBER: _ClassVar[int]
    host_id: str
    host_memory: VmHostCapacity.HostMemUsage
    def __init__(self, host_id: _Optional[str] = ..., host_memory: _Optional[_Union[VmHostCapacity.HostMemUsage, _Mapping]] = ...) -> None: ...

class HostCapacityStore(_message.Message):
    __slots__ = ("gandalf_key", "host_capacity")
    GANDALF_KEY_FIELD_NUMBER: _ClassVar[int]
    HOST_CAPACITY_FIELD_NUMBER: _ClassVar[int]
    gandalf_key: str
    host_capacity: _containers.RepeatedCompositeFieldContainer[VmHostCapacity]
    def __init__(self, gandalf_key: _Optional[str] = ..., host_capacity: _Optional[_Iterable[_Union[VmHostCapacity, _Mapping]]] = ...) -> None: ...
