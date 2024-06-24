from apollo.base import unique_id_pb2 as _unique_id_pb2
from open_util.net import protorpc_pb2 as _protorpc_pb2
from util.base import op_clock_pb2 as _op_clock_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TaskStatus(_message.Message):
    __slots__ = ("type", "data")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNotStarted: _ClassVar[TaskStatus.Type]
        kInitializing: _ClassVar[TaskStatus.Type]
        kInitialized: _ClassVar[TaskStatus.Type]
        kWaitingForMapper: _ClassVar[TaskStatus.Type]
        kFetchingData: _ClassVar[TaskStatus.Type]
        kSortingData: _ClassVar[TaskStatus.Type]
        kWaitingForRunSlot: _ClassVar[TaskStatus.Type]
        kRunning: _ClassVar[TaskStatus.Type]
        kFinished: _ClassVar[TaskStatus.Type]
        kScribeBucketMismatch: _ClassVar[TaskStatus.Type]
        kMasterVersionMismatch: _ClassVar[TaskStatus.Type]
        kError: _ClassVar[TaskStatus.Type]
        kStatusTypeCount: _ClassVar[TaskStatus.Type]
    kNotStarted: TaskStatus.Type
    kInitializing: TaskStatus.Type
    kInitialized: TaskStatus.Type
    kWaitingForMapper: TaskStatus.Type
    kFetchingData: TaskStatus.Type
    kSortingData: TaskStatus.Type
    kWaitingForRunSlot: TaskStatus.Type
    kRunning: TaskStatus.Type
    kFinished: TaskStatus.Type
    kScribeBucketMismatch: TaskStatus.Type
    kMasterVersionMismatch: TaskStatus.Type
    kError: TaskStatus.Type
    kStatusTypeCount: TaskStatus.Type
    class Data(_message.Message):
        __slots__ = ("num_records_for_reducer_shard", "master_known_version")
        NUM_RECORDS_FOR_REDUCER_SHARD_FIELD_NUMBER: _ClassVar[int]
        MASTER_KNOWN_VERSION_FIELD_NUMBER: _ClassVar[int]
        num_records_for_reducer_shard: _containers.RepeatedScalarFieldContainer[int]
        master_known_version: int
        def __init__(self, num_records_for_reducer_shard: _Optional[_Iterable[int]] = ..., master_known_version: _Optional[int] = ...) -> None: ...
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    type: TaskStatus.Type
    data: TaskStatus.Data
    def __init__(self, type: _Optional[_Union[TaskStatus.Type, str]] = ..., data: _Optional[_Union[TaskStatus.Data, _Mapping]] = ...) -> None: ...

class JobInfo(_message.Message):
    __slots__ = ("id", "num_mappers", "num_reducers", "opclock_vec", "algorithm_list", "start_time_sec", "mapper_bucket_assignments", "priority")
    class Priority(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kLowPriority: _ClassVar[JobInfo.Priority]
        kHighPriority: _ClassVar[JobInfo.Priority]
    kLowPriority: JobInfo.Priority
    kHighPriority: JobInfo.Priority
    class AlgorithmInfo(_message.Message):
        __slots__ = ("algorithm_id", "algorithm_specific_data")
        ALGORITHM_ID_FIELD_NUMBER: _ClassVar[int]
        ALGORITHM_SPECIFIC_DATA_FIELD_NUMBER: _ClassVar[int]
        algorithm_id: int
        algorithm_specific_data: bytes
        def __init__(self, algorithm_id: _Optional[int] = ..., algorithm_specific_data: _Optional[bytes] = ...) -> None: ...
    class MapperScribeLocality(_message.Message):
        __slots__ = ("buckets", "ideal_node_id")
        BUCKETS_FIELD_NUMBER: _ClassVar[int]
        IDEAL_NODE_ID_FIELD_NUMBER: _ClassVar[int]
        buckets: _containers.RepeatedScalarFieldContainer[int]
        ideal_node_id: int
        def __init__(self, buckets: _Optional[_Iterable[int]] = ..., ideal_node_id: _Optional[int] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    NUM_MAPPERS_FIELD_NUMBER: _ClassVar[int]
    NUM_REDUCERS_FIELD_NUMBER: _ClassVar[int]
    OPCLOCK_VEC_FIELD_NUMBER: _ClassVar[int]
    ALGORITHM_LIST_FIELD_NUMBER: _ClassVar[int]
    START_TIME_SEC_FIELD_NUMBER: _ClassVar[int]
    MAPPER_BUCKET_ASSIGNMENTS_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    id: _unique_id_pb2.UniqueId
    num_mappers: int
    num_reducers: int
    opclock_vec: _containers.RepeatedCompositeFieldContainer[_op_clock_pb2.OpClock]
    algorithm_list: _containers.RepeatedCompositeFieldContainer[JobInfo.AlgorithmInfo]
    start_time_sec: int
    mapper_bucket_assignments: _containers.RepeatedCompositeFieldContainer[JobInfo.MapperScribeLocality]
    priority: JobInfo.Priority
    def __init__(self, id: _Optional[_Union[_unique_id_pb2.UniqueId, _Mapping]] = ..., num_mappers: _Optional[int] = ..., num_reducers: _Optional[int] = ..., opclock_vec: _Optional[_Iterable[_Union[_op_clock_pb2.OpClock, _Mapping]]] = ..., algorithm_list: _Optional[_Iterable[_Union[JobInfo.AlgorithmInfo, _Mapping]]] = ..., start_time_sec: _Optional[int] = ..., mapper_bucket_assignments: _Optional[_Iterable[_Union[JobInfo.MapperScribeLocality, _Mapping]]] = ..., priority: _Optional[_Union[JobInfo.Priority, str]] = ...) -> None: ...

class TaskInfo(_message.Message):
    __slots__ = ("task_id", "is_mapper", "job", "shard")
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    IS_MAPPER_FIELD_NUMBER: _ClassVar[int]
    JOB_FIELD_NUMBER: _ClassVar[int]
    SHARD_FIELD_NUMBER: _ClassVar[int]
    task_id: _unique_id_pb2.UniqueId
    is_mapper: bool
    job: JobInfo
    shard: int
    def __init__(self, task_id: _Optional[_Union[_unique_id_pb2.UniqueId, _Mapping]] = ..., is_mapper: bool = ..., job: _Optional[_Union[JobInfo, _Mapping]] = ..., shard: _Optional[int] = ...) -> None: ...

class MapperInfoForReduce(_message.Message):
    __slots__ = ("task_info", "task_status", "session_id")
    TASK_INFO_FIELD_NUMBER: _ClassVar[int]
    TASK_STATUS_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    task_info: TaskInfo
    task_status: TaskStatus
    session_id: int
    def __init__(self, task_info: _Optional[_Union[TaskInfo, _Mapping]] = ..., task_status: _Optional[_Union[TaskStatus, _Mapping]] = ..., session_id: _Optional[int] = ...) -> None: ...

class ReducerInfoForReduce(_message.Message):
    __slots__ = ("task_info", "session_id", "node_id", "task_cancelled")
    TASK_INFO_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    TASK_CANCELLED_FIELD_NUMBER: _ClassVar[int]
    task_info: TaskInfo
    session_id: int
    node_id: int
    task_cancelled: bool
    def __init__(self, task_info: _Optional[_Union[TaskInfo, _Mapping]] = ..., session_id: _Optional[int] = ..., node_id: _Optional[int] = ..., task_cancelled: bool = ...) -> None: ...

class StartTaskArg(_message.Message):
    __slots__ = ("rx_session_id", "task_info", "mapper_info", "master_version")
    RX_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    TASK_INFO_FIELD_NUMBER: _ClassVar[int]
    MAPPER_INFO_FIELD_NUMBER: _ClassVar[int]
    MASTER_VERSION_FIELD_NUMBER: _ClassVar[int]
    rx_session_id: int
    task_info: TaskInfo
    mapper_info: _containers.RepeatedCompositeFieldContainer[MapperInfoForReduce]
    master_version: int
    def __init__(self, rx_session_id: _Optional[int] = ..., task_info: _Optional[_Union[TaskInfo, _Mapping]] = ..., mapper_info: _Optional[_Iterable[_Union[MapperInfoForReduce, _Mapping]]] = ..., master_version: _Optional[int] = ...) -> None: ...

class StartTaskResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ProbeArg(_message.Message):
    __slots__ = ("rx_session_id", "master_version")
    RX_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    MASTER_VERSION_FIELD_NUMBER: _ClassVar[int]
    rx_session_id: int
    master_version: int
    def __init__(self, rx_session_id: _Optional[int] = ..., master_version: _Optional[int] = ...) -> None: ...

class ProbeResult(_message.Message):
    __slots__ = ("task_state", "task_status")
    TASK_STATE_FIELD_NUMBER: _ClassVar[int]
    TASK_STATUS_FIELD_NUMBER: _ClassVar[int]
    task_state: _containers.RepeatedCompositeFieldContainer[TaskInfo]
    task_status: _containers.RepeatedCompositeFieldContainer[TaskStatus]
    def __init__(self, task_state: _Optional[_Iterable[_Union[TaskInfo, _Mapping]]] = ..., task_status: _Optional[_Iterable[_Union[TaskStatus, _Mapping]]] = ...) -> None: ...

class NotifyMapperStatusForReduceArg(_message.Message):
    __slots__ = ("rx_session_id", "mapper_info", "master_version")
    RX_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    MAPPER_INFO_FIELD_NUMBER: _ClassVar[int]
    MASTER_VERSION_FIELD_NUMBER: _ClassVar[int]
    rx_session_id: int
    mapper_info: _containers.RepeatedCompositeFieldContainer[MapperInfoForReduce]
    master_version: int
    def __init__(self, rx_session_id: _Optional[int] = ..., mapper_info: _Optional[_Iterable[_Union[MapperInfoForReduce, _Mapping]]] = ..., master_version: _Optional[int] = ...) -> None: ...

class NotifyMapperStatusForReduceResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class EndTaskArg(_message.Message):
    __slots__ = ("rx_session_id", "task_id", "master_version")
    RX_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    MASTER_VERSION_FIELD_NUMBER: _ClassVar[int]
    rx_session_id: int
    task_id: _unique_id_pb2.UniqueId
    master_version: int
    def __init__(self, rx_session_id: _Optional[int] = ..., task_id: _Optional[_Union[_unique_id_pb2.UniqueId, _Mapping]] = ..., master_version: _Optional[int] = ...) -> None: ...

class EndTaskResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class NotifyTaskStatusArg(_message.Message):
    __slots__ = ("rx_session_id", "task_id", "task_status")
    RX_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    TASK_STATUS_FIELD_NUMBER: _ClassVar[int]
    rx_session_id: int
    task_id: _containers.RepeatedCompositeFieldContainer[_unique_id_pb2.UniqueId]
    task_status: _containers.RepeatedCompositeFieldContainer[TaskStatus]
    def __init__(self, rx_session_id: _Optional[int] = ..., task_id: _Optional[_Iterable[_Union[_unique_id_pb2.UniqueId, _Mapping]]] = ..., task_status: _Optional[_Iterable[_Union[TaskStatus, _Mapping]]] = ...) -> None: ...

class NotifyTaskStatusResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class FetchMapOutputArg(_message.Message):
    __slots__ = ("rx_session_id", "map_task_id", "job_id", "reduce_shard", "data_offset", "total_batches_fetched")
    RX_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    MAP_TASK_ID_FIELD_NUMBER: _ClassVar[int]
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    REDUCE_SHARD_FIELD_NUMBER: _ClassVar[int]
    DATA_OFFSET_FIELD_NUMBER: _ClassVar[int]
    TOTAL_BATCHES_FETCHED_FIELD_NUMBER: _ClassVar[int]
    rx_session_id: int
    map_task_id: _unique_id_pb2.UniqueId
    job_id: _unique_id_pb2.UniqueId
    reduce_shard: int
    data_offset: int
    total_batches_fetched: int
    def __init__(self, rx_session_id: _Optional[int] = ..., map_task_id: _Optional[_Union[_unique_id_pb2.UniqueId, _Mapping]] = ..., job_id: _Optional[_Union[_unique_id_pb2.UniqueId, _Mapping]] = ..., reduce_shard: _Optional[int] = ..., data_offset: _Optional[int] = ..., total_batches_fetched: _Optional[int] = ...) -> None: ...

class FetchMapOutputResult(_message.Message):
    __slots__ = ("next_data_offset", "batch_offsets")
    NEXT_DATA_OFFSET_FIELD_NUMBER: _ClassVar[int]
    BATCH_OFFSETS_FIELD_NUMBER: _ClassVar[int]
    next_data_offset: int
    batch_offsets: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, next_data_offset: _Optional[int] = ..., batch_offsets: _Optional[_Iterable[int]] = ...) -> None: ...

class NotifyReducerStatusForReduceArg(_message.Message):
    __slots__ = ("rx_session_id", "reducer_info", "master_version")
    RX_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    REDUCER_INFO_FIELD_NUMBER: _ClassVar[int]
    MASTER_VERSION_FIELD_NUMBER: _ClassVar[int]
    rx_session_id: int
    reducer_info: _containers.RepeatedCompositeFieldContainer[ReducerInfoForReduce]
    master_version: int
    def __init__(self, rx_session_id: _Optional[int] = ..., reducer_info: _Optional[_Iterable[_Union[ReducerInfoForReduce, _Mapping]]] = ..., master_version: _Optional[int] = ...) -> None: ...

class NotifyReducerStatusForReduceResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class EmitActionArg(_message.Message):
    __slots__ = ("rx_session_id", "job_id", "compression_mode", "num_serialized_actions")
    class CompressionMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNone: _ClassVar[EmitActionArg.CompressionMode]
        kGzip: _ClassVar[EmitActionArg.CompressionMode]
        kSnappy: _ClassVar[EmitActionArg.CompressionMode]
    kNone: EmitActionArg.CompressionMode
    kGzip: EmitActionArg.CompressionMode
    kSnappy: EmitActionArg.CompressionMode
    RX_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    COMPRESSION_MODE_FIELD_NUMBER: _ClassVar[int]
    NUM_SERIALIZED_ACTIONS_FIELD_NUMBER: _ClassVar[int]
    rx_session_id: int
    job_id: _unique_id_pb2.UniqueId
    compression_mode: EmitActionArg.CompressionMode
    num_serialized_actions: int
    def __init__(self, rx_session_id: _Optional[int] = ..., job_id: _Optional[_Union[_unique_id_pb2.UniqueId, _Mapping]] = ..., compression_mode: _Optional[_Union[EmitActionArg.CompressionMode, str]] = ..., num_serialized_actions: _Optional[int] = ...) -> None: ...

class EmitActionResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class JobEndNotificationArg(_message.Message):
    __slots__ = ("rx_session_id", "job_id", "master_version")
    RX_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    MASTER_VERSION_FIELD_NUMBER: _ClassVar[int]
    rx_session_id: int
    job_id: _unique_id_pb2.UniqueId
    master_version: int
    def __init__(self, rx_session_id: _Optional[int] = ..., job_id: _Optional[_Union[_unique_id_pb2.UniqueId, _Mapping]] = ..., master_version: _Optional[int] = ...) -> None: ...

class JobEndNotificationResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
