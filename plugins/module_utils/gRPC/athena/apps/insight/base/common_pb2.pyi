from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HistogramProto(_message.Message):
    __slots__ = ("name", "count", "sum", "sum_of_squares", "min_val", "max_val")
    NAME_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    SUM_FIELD_NUMBER: _ClassVar[int]
    SUM_OF_SQUARES_FIELD_NUMBER: _ClassVar[int]
    MIN_VAL_FIELD_NUMBER: _ClassVar[int]
    MAX_VAL_FIELD_NUMBER: _ClassVar[int]
    name: str
    count: int
    sum: int
    sum_of_squares: int
    min_val: int
    max_val: int
    def __init__(self, name: _Optional[str] = ..., count: _Optional[int] = ..., sum: _Optional[int] = ..., sum_of_squares: _Optional[int] = ..., min_val: _Optional[int] = ..., max_val: _Optional[int] = ...) -> None: ...

class MinionStatsProto(_message.Message):
    __slots__ = ("num_subtasks_total", "num_subtask_errors_total", "histogram_vec")
    NUM_SUBTASKS_TOTAL_FIELD_NUMBER: _ClassVar[int]
    NUM_SUBTASK_ERRORS_TOTAL_FIELD_NUMBER: _ClassVar[int]
    HISTOGRAM_VEC_FIELD_NUMBER: _ClassVar[int]
    num_subtasks_total: int
    num_subtask_errors_total: int
    histogram_vec: _containers.RepeatedCompositeFieldContainer[HistogramProto]
    def __init__(self, num_subtasks_total: _Optional[int] = ..., num_subtask_errors_total: _Optional[int] = ..., histogram_vec: _Optional[_Iterable[_Union[HistogramProto, _Mapping]]] = ...) -> None: ...

class MinionTcpEndpointProto(_message.Message):
    __slots__ = ("ip_addr_str", "grpc_port")
    IP_ADDR_STR_FIELD_NUMBER: _ClassVar[int]
    GRPC_PORT_FIELD_NUMBER: _ClassVar[int]
    ip_addr_str: str
    grpc_port: int
    def __init__(self, ip_addr_str: _Optional[str] = ..., grpc_port: _Optional[int] = ...) -> None: ...

class MinionInfoProto(_message.Message):
    __slots__ = ("uptime_secs", "memory_bytes", "per_slot_memory_bytes")
    UPTIME_SECS_FIELD_NUMBER: _ClassVar[int]
    MEMORY_BYTES_FIELD_NUMBER: _ClassVar[int]
    PER_SLOT_MEMORY_BYTES_FIELD_NUMBER: _ClassVar[int]
    uptime_secs: int
    memory_bytes: int
    per_slot_memory_bytes: int
    def __init__(self, uptime_secs: _Optional[int] = ..., memory_bytes: _Optional[int] = ..., per_slot_memory_bytes: _Optional[int] = ...) -> None: ...

class CounterProto(_message.Message):
    __slots__ = ("description", "num_entities", "num_bytes")
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    NUM_ENTITIES_FIELD_NUMBER: _ClassVar[int]
    NUM_BYTES_FIELD_NUMBER: _ClassVar[int]
    description: str
    num_entities: int
    num_bytes: int
    def __init__(self, description: _Optional[str] = ..., num_entities: _Optional[int] = ..., num_bytes: _Optional[int] = ...) -> None: ...
