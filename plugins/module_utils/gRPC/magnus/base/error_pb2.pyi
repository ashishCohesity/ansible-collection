from magnus.api.protoc_gen_openapiv2.options import annotations_pb2 as _annotations_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ErrorProto(_message.Message):
    __slots__ = ("type", "error_message")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNoError: _ClassVar[ErrorProto.Type]
        kExists: _ClassVar[ErrorProto.Type]
        kNonExistent: _ClassVar[ErrorProto.Type]
        kInvalid: _ClassVar[ErrorProto.Type]
        kCanceled: _ClassVar[ErrorProto.Type]
        kTimeout: _ClassVar[ErrorProto.Type]
        kTransportError: _ClassVar[ErrorProto.Type]
        kGrpcError: _ClassVar[ErrorProto.Type]
        kRetry: _ClassVar[ErrorProto.Type]
        kMagnetoError: _ClassVar[ErrorProto.Type]
    kNoError: ErrorProto.Type
    kExists: ErrorProto.Type
    kNonExistent: ErrorProto.Type
    kInvalid: ErrorProto.Type
    kCanceled: ErrorProto.Type
    kTimeout: ErrorProto.Type
    kTransportError: ErrorProto.Type
    kGrpcError: ErrorProto.Type
    kRetry: ErrorProto.Type
    kMagnetoError: ErrorProto.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    type: ErrorProto.Type
    error_message: str
    def __init__(self, type: _Optional[_Union[ErrorProto.Type, str]] = ..., error_message: _Optional[str] = ...) -> None: ...
