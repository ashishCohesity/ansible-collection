from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TimestampDurationTestCases(_message.Message):
    __slots__ = ("epoch", "epoch2", "mintime", "maxtime", "timeval1", "timeval2", "timeval3", "timeval4", "timeval5", "timeval6", "timeval7", "timeval8", "zero_duration", "min_duration", "max_duration", "duration1", "duration2", "duration3", "duration4", "duration5")
    EPOCH_FIELD_NUMBER: _ClassVar[int]
    EPOCH2_FIELD_NUMBER: _ClassVar[int]
    MINTIME_FIELD_NUMBER: _ClassVar[int]
    MAXTIME_FIELD_NUMBER: _ClassVar[int]
    TIMEVAL1_FIELD_NUMBER: _ClassVar[int]
    TIMEVAL2_FIELD_NUMBER: _ClassVar[int]
    TIMEVAL3_FIELD_NUMBER: _ClassVar[int]
    TIMEVAL4_FIELD_NUMBER: _ClassVar[int]
    TIMEVAL5_FIELD_NUMBER: _ClassVar[int]
    TIMEVAL6_FIELD_NUMBER: _ClassVar[int]
    TIMEVAL7_FIELD_NUMBER: _ClassVar[int]
    TIMEVAL8_FIELD_NUMBER: _ClassVar[int]
    ZERO_DURATION_FIELD_NUMBER: _ClassVar[int]
    MIN_DURATION_FIELD_NUMBER: _ClassVar[int]
    MAX_DURATION_FIELD_NUMBER: _ClassVar[int]
    DURATION1_FIELD_NUMBER: _ClassVar[int]
    DURATION2_FIELD_NUMBER: _ClassVar[int]
    DURATION3_FIELD_NUMBER: _ClassVar[int]
    DURATION4_FIELD_NUMBER: _ClassVar[int]
    DURATION5_FIELD_NUMBER: _ClassVar[int]
    epoch: TimeStampType
    epoch2: TimeStampType
    mintime: TimeStampType
    maxtime: TimeStampType
    timeval1: TimeStampType
    timeval2: TimeStampType
    timeval3: TimeStampType
    timeval4: TimeStampType
    timeval5: TimeStampType
    timeval6: TimeStampType
    timeval7: TimeStampType
    timeval8: _timestamp_pb2.Timestamp
    zero_duration: DurationType
    min_duration: DurationType
    max_duration: DurationType
    duration1: DurationType
    duration2: DurationType
    duration3: DurationType
    duration4: DurationType
    duration5: _duration_pb2.Duration
    def __init__(self, epoch: _Optional[_Union[TimeStampType, _Mapping]] = ..., epoch2: _Optional[_Union[TimeStampType, _Mapping]] = ..., mintime: _Optional[_Union[TimeStampType, _Mapping]] = ..., maxtime: _Optional[_Union[TimeStampType, _Mapping]] = ..., timeval1: _Optional[_Union[TimeStampType, _Mapping]] = ..., timeval2: _Optional[_Union[TimeStampType, _Mapping]] = ..., timeval3: _Optional[_Union[TimeStampType, _Mapping]] = ..., timeval4: _Optional[_Union[TimeStampType, _Mapping]] = ..., timeval5: _Optional[_Union[TimeStampType, _Mapping]] = ..., timeval6: _Optional[_Union[TimeStampType, _Mapping]] = ..., timeval7: _Optional[_Union[TimeStampType, _Mapping]] = ..., timeval8: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., zero_duration: _Optional[_Union[DurationType, _Mapping]] = ..., min_duration: _Optional[_Union[DurationType, _Mapping]] = ..., max_duration: _Optional[_Union[DurationType, _Mapping]] = ..., duration1: _Optional[_Union[DurationType, _Mapping]] = ..., duration2: _Optional[_Union[DurationType, _Mapping]] = ..., duration3: _Optional[_Union[DurationType, _Mapping]] = ..., duration4: _Optional[_Union[DurationType, _Mapping]] = ..., duration5: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...

class TimeStampType(_message.Message):
    __slots__ = ("timestamp",)
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    timestamp: _timestamp_pb2.Timestamp
    def __init__(self, timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class DurationType(_message.Message):
    __slots__ = ("duration",)
    DURATION_FIELD_NUMBER: _ClassVar[int]
    duration: _duration_pb2.Duration
    def __init__(self, duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...

class TimestampDuration(_message.Message):
    __slots__ = ("ts", "dur", "rep_ts")
    TS_FIELD_NUMBER: _ClassVar[int]
    DUR_FIELD_NUMBER: _ClassVar[int]
    REP_TS_FIELD_NUMBER: _ClassVar[int]
    ts: _timestamp_pb2.Timestamp
    dur: _duration_pb2.Duration
    rep_ts: _containers.RepeatedCompositeFieldContainer[_timestamp_pb2.Timestamp]
    def __init__(self, ts: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., dur: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., rep_ts: _Optional[_Iterable[_Union[_timestamp_pb2.Timestamp, _Mapping]]] = ...) -> None: ...
