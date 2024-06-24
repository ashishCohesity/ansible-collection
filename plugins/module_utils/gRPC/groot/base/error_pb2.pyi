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
        kStale: _ClassVar[ErrorProto.Type]
        kNonExistent: _ClassVar[ErrorProto.Type]
        kRetry: _ClassVar[ErrorProto.Type]
        kNotLeader: _ClassVar[ErrorProto.Type]
        kAlreadyExists: _ClassVar[ErrorProto.Type]
        kInvalid: _ClassVar[ErrorProto.Type]
        kPermissionDenied: _ClassVar[ErrorProto.Type]
        kOutOfSpace: _ClassVar[ErrorProto.Type]
        kCorrupt: _ClassVar[ErrorProto.Type]
        kFsError: _ClassVar[ErrorProto.Type]
        kNotSupported: _ClassVar[ErrorProto.Type]
        kCancelled: _ClassVar[ErrorProto.Type]
        kNotEnoughNodes: _ClassVar[ErrorProto.Type]
        kNotFound: _ClassVar[ErrorProto.Type]
        kUnknownError: _ClassVar[ErrorProto.Type]
        kServiceDisabled: _ClassVar[ErrorProto.Type]
        kForeignKeyViolation: _ClassVar[ErrorProto.Type]
        kGrootShuttingDown: _ClassVar[ErrorProto.Type]
        kNoResult: _ClassVar[ErrorProto.Type]
        kBookKeeperError: _ClassVar[ErrorProto.Type]
    kNoError: ErrorProto.Type
    kTransportError: ErrorProto.Type
    kTimeout: ErrorProto.Type
    kStale: ErrorProto.Type
    kNonExistent: ErrorProto.Type
    kRetry: ErrorProto.Type
    kNotLeader: ErrorProto.Type
    kAlreadyExists: ErrorProto.Type
    kInvalid: ErrorProto.Type
    kPermissionDenied: ErrorProto.Type
    kOutOfSpace: ErrorProto.Type
    kCorrupt: ErrorProto.Type
    kFsError: ErrorProto.Type
    kNotSupported: ErrorProto.Type
    kCancelled: ErrorProto.Type
    kNotEnoughNodes: ErrorProto.Type
    kNotFound: ErrorProto.Type
    kUnknownError: ErrorProto.Type
    kServiceDisabled: ErrorProto.Type
    kForeignKeyViolation: ErrorProto.Type
    kGrootShuttingDown: ErrorProto.Type
    kNoResult: ErrorProto.Type
    kBookKeeperError: ErrorProto.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ERROR_DETAIL_FIELD_NUMBER: _ClassVar[int]
    type: ErrorProto.Type
    error_detail: str
    def __init__(self, type: _Optional[_Union[ErrorProto.Type, str]] = ..., error_detail: _Optional[str] = ...) -> None: ...
