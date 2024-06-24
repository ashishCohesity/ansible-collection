from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class DriveType(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kUserDefaultDrive: _ClassVar[DriveType.Type]
        kPreservationHoldLibrary: _ClassVar[DriveType.Type]
        kUnspecified: _ClassVar[DriveType.Type]
        kSitePreservationHoldLibrary: _ClassVar[DriveType.Type]
    kUserDefaultDrive: DriveType.Type
    kPreservationHoldLibrary: DriveType.Type
    kUnspecified: DriveType.Type
    kSitePreservationHoldLibrary: DriveType.Type
    def __init__(self) -> None: ...
