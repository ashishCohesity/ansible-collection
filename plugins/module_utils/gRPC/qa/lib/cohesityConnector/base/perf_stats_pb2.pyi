from magneto.base import error_pb2 as _error_pb2
from magneto.master.base import enums_pb2 as _enums_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BasePerfStats(_message.Message):
    __slots__ = ("avg", "min", "max", "median")
    AVG_FIELD_NUMBER: _ClassVar[int]
    MIN_FIELD_NUMBER: _ClassVar[int]
    MAX_FIELD_NUMBER: _ClassVar[int]
    MEDIAN_FIELD_NUMBER: _ClassVar[int]
    avg: int
    min: int
    max: int
    median: int
    def __init__(self, avg: _Optional[int] = ..., min: _Optional[int] = ..., max: _Optional[int] = ..., median: _Optional[int] = ...) -> None: ...

class BridgePerfStats(_message.Message):
    __slots__ = ("write_latency_usecs", "write_ios_per_second", "data_written_bytes_per_second", "read_latency_usecs", "read_ios_per_second", "data_read_bytes_per_second", "sequential_ios_per_second", "random_ios_per_second")
    WRITE_LATENCY_USECS_FIELD_NUMBER: _ClassVar[int]
    WRITE_IOS_PER_SECOND_FIELD_NUMBER: _ClassVar[int]
    DATA_WRITTEN_BYTES_PER_SECOND_FIELD_NUMBER: _ClassVar[int]
    READ_LATENCY_USECS_FIELD_NUMBER: _ClassVar[int]
    READ_IOS_PER_SECOND_FIELD_NUMBER: _ClassVar[int]
    DATA_READ_BYTES_PER_SECOND_FIELD_NUMBER: _ClassVar[int]
    SEQUENTIAL_IOS_PER_SECOND_FIELD_NUMBER: _ClassVar[int]
    RANDOM_IOS_PER_SECOND_FIELD_NUMBER: _ClassVar[int]
    write_latency_usecs: BasePerfStats
    write_ios_per_second: BasePerfStats
    data_written_bytes_per_second: BasePerfStats
    read_latency_usecs: BasePerfStats
    read_ios_per_second: BasePerfStats
    data_read_bytes_per_second: BasePerfStats
    sequential_ios_per_second: BasePerfStats
    random_ios_per_second: BasePerfStats
    def __init__(self, write_latency_usecs: _Optional[_Union[BasePerfStats, _Mapping]] = ..., write_ios_per_second: _Optional[_Union[BasePerfStats, _Mapping]] = ..., data_written_bytes_per_second: _Optional[_Union[BasePerfStats, _Mapping]] = ..., read_latency_usecs: _Optional[_Union[BasePerfStats, _Mapping]] = ..., read_ios_per_second: _Optional[_Union[BasePerfStats, _Mapping]] = ..., data_read_bytes_per_second: _Optional[_Union[BasePerfStats, _Mapping]] = ..., sequential_ios_per_second: _Optional[_Union[BasePerfStats, _Mapping]] = ..., random_ios_per_second: _Optional[_Union[BasePerfStats, _Mapping]] = ...) -> None: ...

class BridgeEntityPerfStats(_message.Message):
    __slots__ = ("entity_id", "stats")
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    STATS_FIELD_NUMBER: _ClassVar[int]
    entity_id: int
    stats: BridgePerfStats
    def __init__(self, entity_id: _Optional[int] = ..., stats: _Optional[_Union[BridgePerfStats, _Mapping]] = ...) -> None: ...

class MagnetoEntityPerfStats(_message.Message):
    __slots__ = ("entity_id", "bytes_backedup_per_second")
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    BYTES_BACKEDUP_PER_SECOND_FIELD_NUMBER: _ClassVar[int]
    entity_id: int
    bytes_backedup_per_second: BasePerfStats
    def __init__(self, entity_id: _Optional[int] = ..., bytes_backedup_per_second: _Optional[_Union[BasePerfStats, _Mapping]] = ...) -> None: ...

class VMBackupTaskStats(_message.Message):
    __slots__ = ("task_start_time_usecs", "task_schedule_time_usecs", "backup_time_usecs", "bytes_read_from_source", "logical_bytes_written", "physical_bytes_written", "status", "error")
    TASK_START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    TASK_SCHEDULE_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    BACKUP_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    BYTES_READ_FROM_SOURCE_FIELD_NUMBER: _ClassVar[int]
    LOGICAL_BYTES_WRITTEN_FIELD_NUMBER: _ClassVar[int]
    PHYSICAL_BYTES_WRITTEN_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    task_start_time_usecs: int
    task_schedule_time_usecs: int
    backup_time_usecs: int
    bytes_read_from_source: int
    logical_bytes_written: int
    physical_bytes_written: int
    status: _enums_pb2.BackupJobTaskStatus
    error: _error_pb2.ErrorProto
    def __init__(self, task_start_time_usecs: _Optional[int] = ..., task_schedule_time_usecs: _Optional[int] = ..., backup_time_usecs: _Optional[int] = ..., bytes_read_from_source: _Optional[int] = ..., logical_bytes_written: _Optional[int] = ..., physical_bytes_written: _Optional[int] = ..., status: _Optional[_Union[_enums_pb2.BackupJobTaskStatus, str]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class VMBackupStats(_message.Message):
    __slots__ = ("moref", "backup_task_stats")
    MOREF_FIELD_NUMBER: _ClassVar[int]
    BACKUP_TASK_STATS_FIELD_NUMBER: _ClassVar[int]
    moref: str
    backup_task_stats: _containers.RepeatedCompositeFieldContainer[VMBackupTaskStats]
    def __init__(self, moref: _Optional[str] = ..., backup_task_stats: _Optional[_Iterable[_Union[VMBackupTaskStats, _Mapping]]] = ...) -> None: ...
