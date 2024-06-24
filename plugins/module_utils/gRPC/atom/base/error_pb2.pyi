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
        kRetry: _ClassVar[ErrorProto.Type]
        kTransportError: _ClassVar[ErrorProto.Type]
        kTimeout: _ClassVar[ErrorProto.Type]
        kNonExistent: _ClassVar[ErrorProto.Type]
        kInvalidRequest: _ClassVar[ErrorProto.Type]
        kAlreadyExists: _ClassVar[ErrorProto.Type]
        kBridgeError: _ClassVar[ErrorProto.Type]
        kNotReady: _ClassVar[ErrorProto.Type]
        kDeleted: _ClassVar[ErrorProto.Type]
        kOutOfMemory: _ClassVar[ErrorProto.Type]
        kInvalidLog: _ClassVar[ErrorProto.Type]
        kInvalid: _ClassVar[ErrorProto.Type]
        kUnknown: _ClassVar[ErrorProto.Type]
        kScribeError: _ClassVar[ErrorProto.Type]
        kInvalidEndTime: _ClassVar[ErrorProto.Type]
        kRejected: _ClassVar[ErrorProto.Type]
        kEncryptionKeyNotFound: _ClassVar[ErrorProto.Type]
        kCanceled: _ClassVar[ErrorProto.Type]
        kNotCurrent: _ClassVar[ErrorProto.Type]
        kEpochSwitchInProgress: _ClassVar[ErrorProto.Type]
        kCDPDisabled: _ClassVar[ErrorProto.Type]
        kPermissionDenied: _ClassVar[ErrorProto.Type]
    kNoError: ErrorProto.Type
    kRetry: ErrorProto.Type
    kTransportError: ErrorProto.Type
    kTimeout: ErrorProto.Type
    kNonExistent: ErrorProto.Type
    kInvalidRequest: ErrorProto.Type
    kAlreadyExists: ErrorProto.Type
    kBridgeError: ErrorProto.Type
    kNotReady: ErrorProto.Type
    kDeleted: ErrorProto.Type
    kOutOfMemory: ErrorProto.Type
    kInvalidLog: ErrorProto.Type
    kInvalid: ErrorProto.Type
    kUnknown: ErrorProto.Type
    kScribeError: ErrorProto.Type
    kInvalidEndTime: ErrorProto.Type
    kRejected: ErrorProto.Type
    kEncryptionKeyNotFound: ErrorProto.Type
    kCanceled: ErrorProto.Type
    kNotCurrent: ErrorProto.Type
    kEpochSwitchInProgress: ErrorProto.Type
    kCDPDisabled: ErrorProto.Type
    kPermissionDenied: ErrorProto.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ERROR_MSG_FIELD_NUMBER: _ClassVar[int]
    type: ErrorProto.Type
    error_msg: str
    def __init__(self, type: _Optional[_Union[ErrorProto.Type, str]] = ..., error_msg: _Optional[str] = ...) -> None: ...
