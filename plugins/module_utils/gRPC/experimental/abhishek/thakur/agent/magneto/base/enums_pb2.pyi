from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class HostEnv(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kLinux: _ClassVar[HostEnv.Type]
        kVOS: _ClassVar[HostEnv.Type]
    kLinux: HostEnv.Type
    kVOS: HostEnv.Type
    def __init__(self) -> None: ...
