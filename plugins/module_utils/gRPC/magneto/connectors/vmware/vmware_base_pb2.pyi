from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class FileType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kOther: _ClassVar[FileType]
    kVMX: _ClassVar[FileType]
    kNVRAM: _ClassVar[FileType]
kOther: FileType
kVMX: FileType
kNVRAM: FileType
