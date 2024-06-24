from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SchedulerStateProto(_message.Message):
    __slots__ = ("algorithms_run_info",)
    class AlgorithmRunInfo(_message.Message):
        __slots__ = ("last_start_time_secs", "last_end_time_secs", "num_scheduled_times", "num_finished_times")
        LAST_START_TIME_SECS_FIELD_NUMBER: _ClassVar[int]
        LAST_END_TIME_SECS_FIELD_NUMBER: _ClassVar[int]
        NUM_SCHEDULED_TIMES_FIELD_NUMBER: _ClassVar[int]
        NUM_FINISHED_TIMES_FIELD_NUMBER: _ClassVar[int]
        last_start_time_secs: int
        last_end_time_secs: int
        num_scheduled_times: int
        num_finished_times: int
        def __init__(self, last_start_time_secs: _Optional[int] = ..., last_end_time_secs: _Optional[int] = ..., num_scheduled_times: _Optional[int] = ..., num_finished_times: _Optional[int] = ...) -> None: ...
    ALGORITHMS_RUN_INFO_FIELD_NUMBER: _ClassVar[int]
    algorithms_run_info: _containers.RepeatedCompositeFieldContainer[SchedulerStateProto.AlgorithmRunInfo]
    def __init__(self, algorithms_run_info: _Optional[_Iterable[_Union[SchedulerStateProto.AlgorithmRunInfo, _Mapping]]] = ...) -> None: ...
