from magneto.base import enums_pb2 as _enums_pb2
from magneto.base import policy_pb2 as _policy_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TimeRangeUsecs(_message.Message):
    __slots__ = ("start_time_usecs", "end_time_usecs")
    START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    END_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    start_time_usecs: int
    end_time_usecs: int
    def __init__(self, start_time_usecs: _Optional[int] = ..., end_time_usecs: _Optional[int] = ...) -> None: ...

class TimeWindow(_message.Message):
    __slots__ = ("day", "start_time", "end_time")
    DAY_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    day: _enums_pb2.Day.Type
    start_time: _policy_pb2.Time
    end_time: _policy_pb2.Time
    def __init__(self, day: _Optional[_Union[_enums_pb2.Day.Type, str]] = ..., start_time: _Optional[_Union[_policy_pb2.Time, _Mapping]] = ..., end_time: _Optional[_Union[_policy_pb2.Time, _Mapping]] = ...) -> None: ...

class ScheduleProto(_message.Message):
    __slots__ = ("type", "periodic_time_windows", "time_ranges", "timezone")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kUnknownSchedule: _ClassVar[ScheduleProto.Type]
        kPeriodicTimeWindows: _ClassVar[ScheduleProto.Type]
        kCustomIntervals: _ClassVar[ScheduleProto.Type]
    kUnknownSchedule: ScheduleProto.Type
    kPeriodicTimeWindows: ScheduleProto.Type
    kCustomIntervals: ScheduleProto.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    PERIODIC_TIME_WINDOWS_FIELD_NUMBER: _ClassVar[int]
    TIME_RANGES_FIELD_NUMBER: _ClassVar[int]
    TIMEZONE_FIELD_NUMBER: _ClassVar[int]
    type: ScheduleProto.Type
    periodic_time_windows: _containers.RepeatedCompositeFieldContainer[TimeWindow]
    time_ranges: _containers.RepeatedCompositeFieldContainer[TimeRangeUsecs]
    timezone: str
    def __init__(self, type: _Optional[_Union[ScheduleProto.Type, str]] = ..., periodic_time_windows: _Optional[_Iterable[_Union[TimeWindow, _Mapping]]] = ..., time_ranges: _Optional[_Iterable[_Union[TimeRangeUsecs, _Mapping]]] = ..., timezone: _Optional[str] = ...) -> None: ...
