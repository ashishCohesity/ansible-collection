from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class CompressionProto(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kSnappy: _ClassVar[CompressionProto.Type]
        kGZip: _ClassVar[CompressionProto.Type]
        kLZ4: _ClassVar[CompressionProto.Type]
        kZSTD: _ClassVar[CompressionProto.Type]
    kSnappy: CompressionProto.Type
    kGZip: CompressionProto.Type
    kLZ4: CompressionProto.Type
    kZSTD: CompressionProto.Type
    def __init__(self) -> None: ...
