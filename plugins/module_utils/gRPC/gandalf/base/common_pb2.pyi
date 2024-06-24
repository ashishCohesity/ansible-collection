from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ConstituentStatsProto(_message.Message):
    __slots__ = ("constituent_id", "last_known_session_id", "last_up_time_usecs", "last_down_time_usecs", "total_up_time_secs_5_min", "total_up_count_5_min", "total_up_time_secs_1_hour", "total_up_count_1_hour", "total_up_time_secs_1_day", "total_up_count_1_day", "total_up_time_secs_1_week", "total_up_count_1_week")
    CONSTITUENT_ID_FIELD_NUMBER: _ClassVar[int]
    LAST_KNOWN_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    LAST_UP_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    LAST_DOWN_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_UP_TIME_SECS_5_MIN_FIELD_NUMBER: _ClassVar[int]
    TOTAL_UP_COUNT_5_MIN_FIELD_NUMBER: _ClassVar[int]
    TOTAL_UP_TIME_SECS_1_HOUR_FIELD_NUMBER: _ClassVar[int]
    TOTAL_UP_COUNT_1_HOUR_FIELD_NUMBER: _ClassVar[int]
    TOTAL_UP_TIME_SECS_1_DAY_FIELD_NUMBER: _ClassVar[int]
    TOTAL_UP_COUNT_1_DAY_FIELD_NUMBER: _ClassVar[int]
    TOTAL_UP_TIME_SECS_1_WEEK_FIELD_NUMBER: _ClassVar[int]
    TOTAL_UP_COUNT_1_WEEK_FIELD_NUMBER: _ClassVar[int]
    constituent_id: int
    last_known_session_id: int
    last_up_time_usecs: int
    last_down_time_usecs: int
    total_up_time_secs_5_min: float
    total_up_count_5_min: float
    total_up_time_secs_1_hour: float
    total_up_count_1_hour: float
    total_up_time_secs_1_day: float
    total_up_count_1_day: float
    total_up_time_secs_1_week: float
    total_up_count_1_week: float
    def __init__(self, constituent_id: _Optional[int] = ..., last_known_session_id: _Optional[int] = ..., last_up_time_usecs: _Optional[int] = ..., last_down_time_usecs: _Optional[int] = ..., total_up_time_secs_5_min: _Optional[float] = ..., total_up_count_5_min: _Optional[float] = ..., total_up_time_secs_1_hour: _Optional[float] = ..., total_up_count_1_hour: _Optional[float] = ..., total_up_time_secs_1_day: _Optional[float] = ..., total_up_count_1_day: _Optional[float] = ..., total_up_time_secs_1_week: _Optional[float] = ..., total_up_count_1_week: _Optional[float] = ...) -> None: ...

class TransformKeyOperation(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kUnknown: _ClassVar[TransformKeyOperation.Type]
        kSetGreaterThanOrEqualTo: _ClassVar[TransformKeyOperation.Type]
        kThrowNotImplementedError: _ClassVar[TransformKeyOperation.Type]
    kUnknown: TransformKeyOperation.Type
    kSetGreaterThanOrEqualTo: TransformKeyOperation.Type
    kThrowNotImplementedError: TransformKeyOperation.Type
    def __init__(self) -> None: ...

class LockPriority(_message.Message):
    __slots__ = ()
    class PriorityType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNoPriority: _ClassVar[LockPriority.PriorityType]
        kLowPriority: _ClassVar[LockPriority.PriorityType]
        kMediumPriority: _ClassVar[LockPriority.PriorityType]
        kHighPriority: _ClassVar[LockPriority.PriorityType]
    kNoPriority: LockPriority.PriorityType
    kLowPriority: LockPriority.PriorityType
    kMediumPriority: LockPriority.PriorityType
    kHighPriority: LockPriority.PriorityType
    def __init__(self) -> None: ...
