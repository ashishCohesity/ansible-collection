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
        kTimeout: _ClassVar[ErrorProto.Type]
        kTableNonExistent: _ClassVar[ErrorProto.Type]
        kInvalidSequencer: _ClassVar[ErrorProto.Type]
        kCASFailure: _ClassVar[ErrorProto.Type]
        kRetry: _ClassVar[ErrorProto.Type]
        kExists: _ClassVar[ErrorProto.Type]
        kNonExistent: _ClassVar[ErrorProto.Type]
        kStale: _ClassVar[ErrorProto.Type]
        kTransportError: _ClassVar[ErrorProto.Type]
        kNotPrimary: _ClassVar[ErrorProto.Type]
        kNotCaughtUp: _ClassVar[ErrorProto.Type]
        kMaybeDeadlocked: _ClassVar[ErrorProto.Type]
        kSeenHigherProposal: _ClassVar[ErrorProto.Type]
        kCrashClient: _ClassVar[ErrorProto.Type]
        kRpcNotImplemented: _ClassVar[ErrorProto.Type]
        kExceedsMaxMessageSize: _ClassVar[ErrorProto.Type]
        kUserTimeout: _ClassVar[ErrorProto.Type]
        kParanoidConsistencyError: _ClassVar[ErrorProto.Type]
        kDifferentBucketsError: _ClassVar[ErrorProto.Type]
        kErrorCount: _ClassVar[ErrorProto.Type]
    kNoError: ErrorProto.Type
    kTimeout: ErrorProto.Type
    kTableNonExistent: ErrorProto.Type
    kInvalidSequencer: ErrorProto.Type
    kCASFailure: ErrorProto.Type
    kRetry: ErrorProto.Type
    kExists: ErrorProto.Type
    kNonExistent: ErrorProto.Type
    kStale: ErrorProto.Type
    kTransportError: ErrorProto.Type
    kNotPrimary: ErrorProto.Type
    kNotCaughtUp: ErrorProto.Type
    kMaybeDeadlocked: ErrorProto.Type
    kSeenHigherProposal: ErrorProto.Type
    kCrashClient: ErrorProto.Type
    kRpcNotImplemented: ErrorProto.Type
    kExceedsMaxMessageSize: ErrorProto.Type
    kUserTimeout: ErrorProto.Type
    kParanoidConsistencyError: ErrorProto.Type
    kDifferentBucketsError: ErrorProto.Type
    kErrorCount: ErrorProto.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ERROR_MSG_FIELD_NUMBER: _ClassVar[int]
    type: ErrorProto.Type
    error_msg: str
    def __init__(self, type: _Optional[_Union[ErrorProto.Type, str]] = ..., error_msg: _Optional[str] = ...) -> None: ...
