from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class DataType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kUnknown: _ClassVar[DataType]
    kIOData: _ClassVar[DataType]
    kDiskSnapshot: _ClassVar[DataType]
    kDiskGrow: _ClassVar[DataType]
    kDiskCollapse: _ClassVar[DataType]
    kDiskClone: _ClassVar[DataType]
    kMigration: _ClassVar[DataType]
    kStorageMigration: _ClassVar[DataType]
kUnknown: DataType
kIOData: DataType
kDiskSnapshot: DataType
kDiskGrow: DataType
kDiskCollapse: DataType
kDiskClone: DataType
kMigration: DataType
kStorageMigration: DataType

class VMwareEntityID(_message.Message):
    __slots__ = ("vm_uuid", "disk_uuid", "vcenter_uuid")
    VM_UUID_FIELD_NUMBER: _ClassVar[int]
    DISK_UUID_FIELD_NUMBER: _ClassVar[int]
    VCENTER_UUID_FIELD_NUMBER: _ClassVar[int]
    vm_uuid: str
    disk_uuid: str
    vcenter_uuid: str
    def __init__(self, vm_uuid: _Optional[str] = ..., disk_uuid: _Optional[str] = ..., vcenter_uuid: _Optional[str] = ...) -> None: ...

class SequenceNumber(_message.Message):
    __slots__ = ("incarnation_id", "io_num")
    INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    IO_NUM_FIELD_NUMBER: _ClassVar[int]
    incarnation_id: int
    io_num: int
    def __init__(self, incarnation_id: _Optional[int] = ..., io_num: _Optional[int] = ...) -> None: ...
