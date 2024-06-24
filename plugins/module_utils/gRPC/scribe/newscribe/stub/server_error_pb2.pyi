from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ServerErrorProto(_message.Message):
    __slots__ = ("type", "error_msg")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNoError: _ClassVar[ServerErrorProto.Type]
        kTimeout: _ClassVar[ServerErrorProto.Type]
        kTableNonExistent: _ClassVar[ServerErrorProto.Type]
        kInvalidSequencer: _ClassVar[ServerErrorProto.Type]
        kCASFailure: _ClassVar[ServerErrorProto.Type]
        kRetry: _ClassVar[ServerErrorProto.Type]
        kTransportError: _ClassVar[ServerErrorProto.Type]
        kNotLeader: _ClassVar[ServerErrorProto.Type]
        kNotCaughtup: _ClassVar[ServerErrorProto.Type]
        kSenderNotLeader: _ClassVar[ServerErrorProto.Type]
        kCrashClient: _ClassVar[ServerErrorProto.Type]
        kInvalidBucket: _ClassVar[ServerErrorProto.Type]
        kReplicaNotCaughtup: _ClassVar[ServerErrorProto.Type]
        kLeaderInstanceStale: _ClassVar[ServerErrorProto.Type]
        kBucketDbLocked: _ClassVar[ServerErrorProto.Type]
        kTxLeaderLockSequencerStale: _ClassVar[ServerErrorProto.Type]
        kRxLeaderLockSequencerStale: _ClassVar[ServerErrorProto.Type]
        kViewVersionMismatch: _ClassVar[ServerErrorProto.Type]
        kTableMdVersionMismatch: _ClassVar[ServerErrorProto.Type]
        kUnavailable: _ClassVar[ServerErrorProto.Type]
        kBucketNotHosted: _ClassVar[ServerErrorProto.Type]
        kStaleRequest: _ClassVar[ServerErrorProto.Type]
        kInjectedFailure: _ClassVar[ServerErrorProto.Type]
        kOpIncomplete: _ClassVar[ServerErrorProto.Type]
        kInsufficientSpace: _ClassVar[ServerErrorProto.Type]
        kBucketLockTryAcquireFailed: _ClassVar[ServerErrorProto.Type]
        kExceedsMaxMessageSize: _ClassVar[ServerErrorProto.Type]
        kUnrecoverableDataFileError: _ClassVar[ServerErrorProto.Type]
        kTabletStateNotCurrent: _ClassVar[ServerErrorProto.Type]
        kParanoidConsistencyError: _ClassVar[ServerErrorProto.Type]
        kBucketsOnDifferentConstituents: _ClassVar[ServerErrorProto.Type]
        kFeatureNotReady: _ClassVar[ServerErrorProto.Type]
        kLeader: _ClassVar[ServerErrorProto.Type]
        kErrorCount: _ClassVar[ServerErrorProto.Type]
    kNoError: ServerErrorProto.Type
    kTimeout: ServerErrorProto.Type
    kTableNonExistent: ServerErrorProto.Type
    kInvalidSequencer: ServerErrorProto.Type
    kCASFailure: ServerErrorProto.Type
    kRetry: ServerErrorProto.Type
    kTransportError: ServerErrorProto.Type
    kNotLeader: ServerErrorProto.Type
    kNotCaughtup: ServerErrorProto.Type
    kSenderNotLeader: ServerErrorProto.Type
    kCrashClient: ServerErrorProto.Type
    kInvalidBucket: ServerErrorProto.Type
    kReplicaNotCaughtup: ServerErrorProto.Type
    kLeaderInstanceStale: ServerErrorProto.Type
    kBucketDbLocked: ServerErrorProto.Type
    kTxLeaderLockSequencerStale: ServerErrorProto.Type
    kRxLeaderLockSequencerStale: ServerErrorProto.Type
    kViewVersionMismatch: ServerErrorProto.Type
    kTableMdVersionMismatch: ServerErrorProto.Type
    kUnavailable: ServerErrorProto.Type
    kBucketNotHosted: ServerErrorProto.Type
    kStaleRequest: ServerErrorProto.Type
    kInjectedFailure: ServerErrorProto.Type
    kOpIncomplete: ServerErrorProto.Type
    kInsufficientSpace: ServerErrorProto.Type
    kBucketLockTryAcquireFailed: ServerErrorProto.Type
    kExceedsMaxMessageSize: ServerErrorProto.Type
    kUnrecoverableDataFileError: ServerErrorProto.Type
    kTabletStateNotCurrent: ServerErrorProto.Type
    kParanoidConsistencyError: ServerErrorProto.Type
    kBucketsOnDifferentConstituents: ServerErrorProto.Type
    kFeatureNotReady: ServerErrorProto.Type
    kLeader: ServerErrorProto.Type
    kErrorCount: ServerErrorProto.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ERROR_MSG_FIELD_NUMBER: _ClassVar[int]
    type: ServerErrorProto.Type
    error_msg: str
    def __init__(self, type: _Optional[_Union[ServerErrorProto.Type, str]] = ..., error_msg: _Optional[str] = ...) -> None: ...
