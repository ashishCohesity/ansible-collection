from apollo.mr.base import error_pb2 as _error_pb2
from apollo.mr.base import pipeline_pb2 as _pipeline_pb2
from util.base import op_clock_pb2 as _op_clock_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DurationsProto(_message.Message):
    __slots__ = ("min_usecs", "max_usecs", "sum_usecs", "count")
    MIN_USECS_FIELD_NUMBER: _ClassVar[int]
    MAX_USECS_FIELD_NUMBER: _ClassVar[int]
    SUM_USECS_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    min_usecs: int
    max_usecs: int
    sum_usecs: int
    count: int
    def __init__(self, min_usecs: _Optional[int] = ..., max_usecs: _Optional[int] = ..., sum_usecs: _Optional[int] = ..., count: _Optional[int] = ...) -> None: ...

class FragmentStatsProto(_message.Message):
    __slots__ = ("start_time_usecs", "end_time_usecs", "run_times")
    START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    END_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    RUN_TIMES_FIELD_NUMBER: _ClassVar[int]
    start_time_usecs: int
    end_time_usecs: int
    run_times: DurationsProto
    def __init__(self, start_time_usecs: _Optional[int] = ..., end_time_usecs: _Optional[int] = ..., run_times: _Optional[_Union[DurationsProto, _Mapping]] = ...) -> None: ...

class JobProto(_message.Message):
    __slots__ = ("id", "state", "start_time_usecs", "deadline_usecs", "num_nodes", "serialized_context_data", "debug_mode", "job_opclock_vec", "fragment_counters", "fragment_stats", "urgency", "input_fragment_num_shards", "incarnation_id_gen", "end_time_usecs", "error", "fragment_names", "pipeline_input_data", "request_id")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kRunning: _ClassVar[JobProto.State]
        kFinished: _ClassVar[JobProto.State]
    kRunning: JobProto.State
    kFinished: JobProto.State
    class FragmentCountersEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _pipeline_pb2.CountersProto
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_pipeline_pb2.CountersProto, _Mapping]] = ...) -> None: ...
    class FragmentStatsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: FragmentStatsProto
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[FragmentStatsProto, _Mapping]] = ...) -> None: ...
    class InputFragmentNumShardsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    class FragmentNamesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: str
        def __init__(self, key: _Optional[int] = ..., value: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    DEADLINE_USECS_FIELD_NUMBER: _ClassVar[int]
    NUM_NODES_FIELD_NUMBER: _ClassVar[int]
    SERIALIZED_CONTEXT_DATA_FIELD_NUMBER: _ClassVar[int]
    DEBUG_MODE_FIELD_NUMBER: _ClassVar[int]
    JOB_OPCLOCK_VEC_FIELD_NUMBER: _ClassVar[int]
    FRAGMENT_COUNTERS_FIELD_NUMBER: _ClassVar[int]
    FRAGMENT_STATS_FIELD_NUMBER: _ClassVar[int]
    URGENCY_FIELD_NUMBER: _ClassVar[int]
    INPUT_FRAGMENT_NUM_SHARDS_FIELD_NUMBER: _ClassVar[int]
    INCARNATION_ID_GEN_FIELD_NUMBER: _ClassVar[int]
    END_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    FRAGMENT_NAMES_FIELD_NUMBER: _ClassVar[int]
    PIPELINE_INPUT_DATA_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    id: _pipeline_pb2.IdProto
    state: JobProto.State
    start_time_usecs: int
    deadline_usecs: int
    num_nodes: int
    serialized_context_data: bytes
    debug_mode: bool
    job_opclock_vec: _containers.RepeatedCompositeFieldContainer[_op_clock_pb2.OpClock]
    fragment_counters: _containers.MessageMap[int, _pipeline_pb2.CountersProto]
    fragment_stats: _containers.MessageMap[int, FragmentStatsProto]
    urgency: int
    input_fragment_num_shards: _containers.ScalarMap[int, int]
    incarnation_id_gen: int
    end_time_usecs: int
    error: _error_pb2.ErrorProto
    fragment_names: _containers.ScalarMap[int, str]
    pipeline_input_data: bytes
    request_id: int
    def __init__(self, id: _Optional[_Union[_pipeline_pb2.IdProto, _Mapping]] = ..., state: _Optional[_Union[JobProto.State, str]] = ..., start_time_usecs: _Optional[int] = ..., deadline_usecs: _Optional[int] = ..., num_nodes: _Optional[int] = ..., serialized_context_data: _Optional[bytes] = ..., debug_mode: bool = ..., job_opclock_vec: _Optional[_Iterable[_Union[_op_clock_pb2.OpClock, _Mapping]]] = ..., fragment_counters: _Optional[_Mapping[int, _pipeline_pb2.CountersProto]] = ..., fragment_stats: _Optional[_Mapping[int, FragmentStatsProto]] = ..., urgency: _Optional[int] = ..., input_fragment_num_shards: _Optional[_Mapping[int, int]] = ..., incarnation_id_gen: _Optional[int] = ..., end_time_usecs: _Optional[int] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., fragment_names: _Optional[_Mapping[int, str]] = ..., pipeline_input_data: _Optional[bytes] = ..., request_id: _Optional[int] = ...) -> None: ...

class JobHistoryProto(_message.Message):
    __slots__ = ("run_history_vec",)
    class RunHistory(_message.Message):
        __slots__ = ("pipeline", "last_start_time_usecs", "last_end_time_usecs", "next_instance_id", "past_job_vec", "backlog_indicator")
        PIPELINE_FIELD_NUMBER: _ClassVar[int]
        LAST_START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
        LAST_END_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
        NEXT_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
        PAST_JOB_VEC_FIELD_NUMBER: _ClassVar[int]
        BACKLOG_INDICATOR_FIELD_NUMBER: _ClassVar[int]
        pipeline: str
        last_start_time_usecs: int
        last_end_time_usecs: int
        next_instance_id: int
        past_job_vec: _containers.RepeatedCompositeFieldContainer[JobProto]
        backlog_indicator: int
        def __init__(self, pipeline: _Optional[str] = ..., last_start_time_usecs: _Optional[int] = ..., last_end_time_usecs: _Optional[int] = ..., next_instance_id: _Optional[int] = ..., past_job_vec: _Optional[_Iterable[_Union[JobProto, _Mapping]]] = ..., backlog_indicator: _Optional[int] = ...) -> None: ...
    RUN_HISTORY_VEC_FIELD_NUMBER: _ClassVar[int]
    run_history_vec: _containers.RepeatedCompositeFieldContainer[JobHistoryProto.RunHistory]
    def __init__(self, run_history_vec: _Optional[_Iterable[_Union[JobHistoryProto.RunHistory, _Mapping]]] = ...) -> None: ...

class ScheduleJobRequestProto(_message.Message):
    __slots__ = ("pipeline_name", "request_id", "pipeline_input", "urgency", "enqueue_time_usecs")
    PIPELINE_NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    PIPELINE_INPUT_FIELD_NUMBER: _ClassVar[int]
    URGENCY_FIELD_NUMBER: _ClassVar[int]
    ENQUEUE_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    pipeline_name: str
    request_id: int
    pipeline_input: bytes
    urgency: int
    enqueue_time_usecs: int
    def __init__(self, pipeline_name: _Optional[str] = ..., request_id: _Optional[int] = ..., pipeline_input: _Optional[bytes] = ..., urgency: _Optional[int] = ..., enqueue_time_usecs: _Optional[int] = ...) -> None: ...

class ThrottlingState(_message.Message):
    __slots__ = ("backlog_start_usecs",)
    BACKLOG_START_USECS_FIELD_NUMBER: _ClassVar[int]
    backlog_start_usecs: int
    def __init__(self, backlog_start_usecs: _Optional[int] = ...) -> None: ...
