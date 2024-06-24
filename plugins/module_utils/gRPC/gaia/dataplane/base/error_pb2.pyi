from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ErrorProto(_message.Message):
    __slots__ = ("type", "error_detail")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNoError: _ClassVar[ErrorProto.Type]
        kInvalid: _ClassVar[ErrorProto.Type]
        kTimeout: _ClassVar[ErrorProto.Type]
        kRetry: _ClassVar[ErrorProto.Type]
        kNotLeader: _ClassVar[ErrorProto.Type]
        kMagnetoError: _ClassVar[ErrorProto.Type]
        kYodaError: _ClassVar[ErrorProto.Type]
        kGrpcError: _ClassVar[ErrorProto.Type]
        kNotFound: _ClassVar[ErrorProto.Type]
        kBridgeError: _ClassVar[ErrorProto.Type]
        kEmblemError: _ClassVar[ErrorProto.Type]
        kTransportError: _ClassVar[ErrorProto.Type]
        kStorageError: _ClassVar[ErrorProto.Type]
        kOutOfSpace: _ClassVar[ErrorProto.Type]
        kNonExistent: _ClassVar[ErrorProto.Type]
    kNoError: ErrorProto.Type
    kInvalid: ErrorProto.Type
    kTimeout: ErrorProto.Type
    kRetry: ErrorProto.Type
    kNotLeader: ErrorProto.Type
    kMagnetoError: ErrorProto.Type
    kYodaError: ErrorProto.Type
    kGrpcError: ErrorProto.Type
    kNotFound: ErrorProto.Type
    kBridgeError: ErrorProto.Type
    kEmblemError: ErrorProto.Type
    kTransportError: ErrorProto.Type
    kStorageError: ErrorProto.Type
    kOutOfSpace: ErrorProto.Type
    kNonExistent: ErrorProto.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ERROR_DETAIL_FIELD_NUMBER: _ClassVar[int]
    type: ErrorProto.Type
    error_detail: str
    def __init__(self, type: _Optional[_Union[ErrorProto.Type, str]] = ..., error_detail: _Optional[str] = ...) -> None: ...
