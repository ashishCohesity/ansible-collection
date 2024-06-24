from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ErrorProto(_message.Message):
    __slots__ = ("type", "error_msg")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNoError: _ClassVar[ErrorProto.Type]
        kTransportError: _ClassVar[ErrorProto.Type]
        kTimeout: _ClassVar[ErrorProto.Type]
        kRetry: _ClassVar[ErrorProto.Type]
        kCancelled: _ClassVar[ErrorProto.Type]
        kInvalid: _ClassVar[ErrorProto.Type]
        kPending: _ClassVar[ErrorProto.Type]
        kAccessDenied: _ClassVar[ErrorProto.Type]
        kExists: _ClassVar[ErrorProto.Type]
        kNotFound: _ClassVar[ErrorProto.Type]
        kMountFailure: _ClassVar[ErrorProto.Type]
        kReadError: _ClassVar[ErrorProto.Type]
        kIOError: _ClassVar[ErrorProto.Type]
        kOperationNotPermittedError: _ClassVar[ErrorProto.Type]
        kUnknownError: _ClassVar[ErrorProto.Type]
    kNoError: ErrorProto.Type
    kTransportError: ErrorProto.Type
    kTimeout: ErrorProto.Type
    kRetry: ErrorProto.Type
    kCancelled: ErrorProto.Type
    kInvalid: ErrorProto.Type
    kPending: ErrorProto.Type
    kAccessDenied: ErrorProto.Type
    kExists: ErrorProto.Type
    kNotFound: ErrorProto.Type
    kMountFailure: ErrorProto.Type
    kReadError: ErrorProto.Type
    kIOError: ErrorProto.Type
    kOperationNotPermittedError: ErrorProto.Type
    kUnknownError: ErrorProto.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ERROR_MSG_FIELD_NUMBER: _ClassVar[int]
    type: ErrorProto.Type
    error_msg: str
    def __init__(self, type: _Optional[_Union[ErrorProto.Type, str]] = ..., error_msg: _Optional[str] = ...) -> None: ...
