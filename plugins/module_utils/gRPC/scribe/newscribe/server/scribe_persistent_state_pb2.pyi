from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LastRestartReasonProto(_message.Message):
    __slots__ = ("restart_reason", "reason_string", "last_shutdown_time_msec")
    class RestartReason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kFaultInjectionRandom: _ClassVar[LastRestartReasonProto.RestartReason]
        kFaultInjectionCrashSite: _ClassVar[LastRestartReasonProto.RestartReason]
        kUnrecoverableRocksdbDataFileError: _ClassVar[LastRestartReasonProto.RestartReason]
        kUnrecoverableScribeDataFileError: _ClassVar[LastRestartReasonProto.RestartReason]
        kDiskOutOfSpaceError: _ClassVar[LastRestartReasonProto.RestartReason]
        kShutdownInProgress: _ClassVar[LastRestartReasonProto.RestartReason]
        kDeadlockDetected: _ClassVar[LastRestartReasonProto.RestartReason]
        kCompactionTooLarge: _ClassVar[LastRestartReasonProto.RestartReason]
        kColumnFamilyDropped: _ClassVar[LastRestartReasonProto.RestartReason]
        kMemoryLimitCrossed: _ClassVar[LastRestartReasonProto.RestartReason]
        kPathNotFound: _ClassVar[LastRestartReasonProto.RestartReason]
        kManualCompactionPaused: _ClassVar[LastRestartReasonProto.RestartReason]
        kIsTimedOut: _ClassVar[LastRestartReasonProto.RestartReason]
        kViewVersionMismatch: _ClassVar[LastRestartReasonProto.RestartReason]
        kTableMdVersionMismatch: _ClassVar[LastRestartReasonProto.RestartReason]
    kFaultInjectionRandom: LastRestartReasonProto.RestartReason
    kFaultInjectionCrashSite: LastRestartReasonProto.RestartReason
    kUnrecoverableRocksdbDataFileError: LastRestartReasonProto.RestartReason
    kUnrecoverableScribeDataFileError: LastRestartReasonProto.RestartReason
    kDiskOutOfSpaceError: LastRestartReasonProto.RestartReason
    kShutdownInProgress: LastRestartReasonProto.RestartReason
    kDeadlockDetected: LastRestartReasonProto.RestartReason
    kCompactionTooLarge: LastRestartReasonProto.RestartReason
    kColumnFamilyDropped: LastRestartReasonProto.RestartReason
    kMemoryLimitCrossed: LastRestartReasonProto.RestartReason
    kPathNotFound: LastRestartReasonProto.RestartReason
    kManualCompactionPaused: LastRestartReasonProto.RestartReason
    kIsTimedOut: LastRestartReasonProto.RestartReason
    kViewVersionMismatch: LastRestartReasonProto.RestartReason
    kTableMdVersionMismatch: LastRestartReasonProto.RestartReason
    RESTART_REASON_FIELD_NUMBER: _ClassVar[int]
    REASON_STRING_FIELD_NUMBER: _ClassVar[int]
    LAST_SHUTDOWN_TIME_MSEC_FIELD_NUMBER: _ClassVar[int]
    restart_reason: LastRestartReasonProto.RestartReason
    reason_string: str
    last_shutdown_time_msec: int
    def __init__(self, restart_reason: _Optional[_Union[LastRestartReasonProto.RestartReason, str]] = ..., reason_string: _Optional[str] = ..., last_shutdown_time_msec: _Optional[int] = ...) -> None: ...

class LastManualCompactionStateProto(_message.Message):
    __slots__ = ("completed_bucket_index", "compaction_in_progress")
    COMPLETED_BUCKET_INDEX_FIELD_NUMBER: _ClassVar[int]
    COMPACTION_IN_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    completed_bucket_index: int
    compaction_in_progress: bool
    def __init__(self, completed_bucket_index: _Optional[int] = ..., compaction_in_progress: bool = ...) -> None: ...

class AegisCorruptionInfo(_message.Message):
    __slots__ = ("aegis_score", "time_of_last_corruption_secs", "time_of_last_score_update_secs")
    AEGIS_SCORE_FIELD_NUMBER: _ClassVar[int]
    TIME_OF_LAST_CORRUPTION_SECS_FIELD_NUMBER: _ClassVar[int]
    TIME_OF_LAST_SCORE_UPDATE_SECS_FIELD_NUMBER: _ClassVar[int]
    aegis_score: int
    time_of_last_corruption_secs: int
    time_of_last_score_update_secs: int
    def __init__(self, aegis_score: _Optional[int] = ..., time_of_last_corruption_secs: _Optional[int] = ..., time_of_last_score_update_secs: _Optional[int] = ...) -> None: ...
