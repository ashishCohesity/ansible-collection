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
        kTransportError: _ClassVar[ErrorProto.Type]
        kTimeout: _ClassVar[ErrorProto.Type]
        kRetry: _ClassVar[ErrorProto.Type]
        kStale: _ClassVar[ErrorProto.Type]
        kNotMaster: _ClassVar[ErrorProto.Type]
        kInvalid: _ClassVar[ErrorProto.Type]
        kCanceled: _ClassVar[ErrorProto.Type]
        kVersionMismatch: _ClassVar[ErrorProto.Type]
        kPermissionDenied: _ClassVar[ErrorProto.Type]
        kNonExistent: _ClassVar[ErrorProto.Type]
        kNotSupported: _ClassVar[ErrorProto.Type]
        kOutOfSpace: _ClassVar[ErrorProto.Type]
        kIOError: _ClassVar[ErrorProto.Type]
        kReadOnlyFS: _ClassVar[ErrorProto.Type]
        kAlreadyExists: _ClassVar[ErrorProto.Type]
        kAppError: _ClassVar[ErrorProto.Type]
        kRejected: _ClassVar[ErrorProto.Type]
        kScribeError: _ClassVar[ErrorProto.Type]
        kDuplicate: _ClassVar[ErrorProto.Type]
        kParseError: _ClassVar[ErrorProto.Type]
    kNoError: ErrorProto.Type
    kTransportError: ErrorProto.Type
    kTimeout: ErrorProto.Type
    kRetry: ErrorProto.Type
    kStale: ErrorProto.Type
    kNotMaster: ErrorProto.Type
    kInvalid: ErrorProto.Type
    kCanceled: ErrorProto.Type
    kVersionMismatch: ErrorProto.Type
    kPermissionDenied: ErrorProto.Type
    kNonExistent: ErrorProto.Type
    kNotSupported: ErrorProto.Type
    kOutOfSpace: ErrorProto.Type
    kIOError: ErrorProto.Type
    kReadOnlyFS: ErrorProto.Type
    kAlreadyExists: ErrorProto.Type
    kAppError: ErrorProto.Type
    kRejected: ErrorProto.Type
    kScribeError: ErrorProto.Type
    kDuplicate: ErrorProto.Type
    kParseError: ErrorProto.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ERROR_DETAIL_FIELD_NUMBER: _ClassVar[int]
    type: ErrorProto.Type
    error_detail: str
    def __init__(self, type: _Optional[_Union[ErrorProto.Type, str]] = ..., error_detail: _Optional[str] = ...) -> None: ...
