from athena.base import kubernetes_pb2 as _kubernetes_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StatsListProto(_message.Message):
    __slots__ = ("stats",)
    STATS_FIELD_NUMBER: _ClassVar[int]
    stats: _containers.RepeatedCompositeFieldContainer[StatsProto]
    def __init__(self, stats: _Optional[_Iterable[_Union[StatsProto, _Mapping]]] = ...) -> None: ...

class StatsProto(_message.Message):
    __slots__ = ("cpu_usage", "memory_usage", "io_bytes", "memory_cache", "timestamp_ms")
    CPU_USAGE_FIELD_NUMBER: _ClassVar[int]
    MEMORY_USAGE_FIELD_NUMBER: _ClassVar[int]
    IO_BYTES_FIELD_NUMBER: _ClassVar[int]
    MEMORY_CACHE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_MS_FIELD_NUMBER: _ClassVar[int]
    cpu_usage: int
    memory_usage: int
    io_bytes: int
    memory_cache: int
    timestamp_ms: int
    def __init__(self, cpu_usage: _Optional[int] = ..., memory_usage: _Optional[int] = ..., io_bytes: _Optional[int] = ..., memory_cache: _Optional[int] = ..., timestamp_ms: _Optional[int] = ...) -> None: ...

class AggregateStatsListProto(_message.Message):
    __slots__ = ("stats",)
    STATS_FIELD_NUMBER: _ClassVar[int]
    stats: _containers.RepeatedCompositeFieldContainer[AggregateStatsProto]
    def __init__(self, stats: _Optional[_Iterable[_Union[AggregateStatsProto, _Mapping]]] = ...) -> None: ...

class AggregateStatsProto(_message.Message):
    __slots__ = ("cpu_usage_percent", "memory_usage_bytes", "io_bytes_per_second")
    CPU_USAGE_PERCENT_FIELD_NUMBER: _ClassVar[int]
    MEMORY_USAGE_BYTES_FIELD_NUMBER: _ClassVar[int]
    IO_BYTES_PER_SECOND_FIELD_NUMBER: _ClassVar[int]
    cpu_usage_percent: float
    memory_usage_bytes: int
    io_bytes_per_second: float
    def __init__(self, cpu_usage_percent: _Optional[float] = ..., memory_usage_bytes: _Optional[int] = ..., io_bytes_per_second: _Optional[float] = ...) -> None: ...

class ContainerStatsProto(_message.Message):
    __slots__ = ("pod_info", "stats")
    POD_INFO_FIELD_NUMBER: _ClassVar[int]
    STATS_FIELD_NUMBER: _ClassVar[int]
    pod_info: _kubernetes_pb2.PodProto
    stats: AggregateStatsProto
    def __init__(self, pod_info: _Optional[_Union[_kubernetes_pb2.PodProto, _Mapping]] = ..., stats: _Optional[_Union[AggregateStatsProto, _Mapping]] = ...) -> None: ...
