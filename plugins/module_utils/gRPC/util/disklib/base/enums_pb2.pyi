from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class DiskFormat(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kVMDK: _ClassVar[DiskFormat.Type]
        kVHD: _ClassVar[DiskFormat.Type]
        kVHDx: _ClassVar[DiskFormat.Type]
        kRaw: _ClassVar[DiskFormat.Type]
        kUnknown: _ClassVar[DiskFormat.Type]
    kVMDK: DiskFormat.Type
    kVHD: DiskFormat.Type
    kVHDx: DiskFormat.Type
    kRaw: DiskFormat.Type
    kUnknown: DiskFormat.Type
    def __init__(self) -> None: ...

class VirtualHardDiskType(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kFixed: _ClassVar[VirtualHardDiskType.Type]
        kDynamic: _ClassVar[VirtualHardDiskType.Type]
        kDifferencing: _ClassVar[VirtualHardDiskType.Type]
    kFixed: VirtualHardDiskType.Type
    kDynamic: VirtualHardDiskType.Type
    kDifferencing: VirtualHardDiskType.Type
    def __init__(self) -> None: ...
