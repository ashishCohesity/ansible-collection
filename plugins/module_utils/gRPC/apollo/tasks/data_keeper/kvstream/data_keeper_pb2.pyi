from apollo.base import unique_id_pb2 as _unique_id_pb2
from apollo.stub import apollo_pb2 as _apollo_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MapperTaskBucketStateProto(_message.Message):
    __slots__ = ("mapper_task_id", "reducer_shard_id", "scribe_table_id", "bucket_id", "data_file_relative_path", "disk_id", "num_records")
    MAPPER_TASK_ID_FIELD_NUMBER: _ClassVar[int]
    REDUCER_SHARD_ID_FIELD_NUMBER: _ClassVar[int]
    SCRIBE_TABLE_ID_FIELD_NUMBER: _ClassVar[int]
    BUCKET_ID_FIELD_NUMBER: _ClassVar[int]
    DATA_FILE_RELATIVE_PATH_FIELD_NUMBER: _ClassVar[int]
    DISK_ID_FIELD_NUMBER: _ClassVar[int]
    NUM_RECORDS_FIELD_NUMBER: _ClassVar[int]
    mapper_task_id: _unique_id_pb2.UniqueId
    reducer_shard_id: int
    scribe_table_id: int
    bucket_id: int
    data_file_relative_path: str
    disk_id: int
    num_records: int
    def __init__(self, mapper_task_id: _Optional[_Union[_unique_id_pb2.UniqueId, _Mapping]] = ..., reducer_shard_id: _Optional[int] = ..., scribe_table_id: _Optional[int] = ..., bucket_id: _Optional[int] = ..., data_file_relative_path: _Optional[str] = ..., disk_id: _Optional[int] = ..., num_records: _Optional[int] = ...) -> None: ...

class TaskStateProto(_message.Message):
    __slots__ = ("task_info", "mapper_bucket_state_vec")
    TASK_INFO_FIELD_NUMBER: _ClassVar[int]
    MAPPER_BUCKET_STATE_VEC_FIELD_NUMBER: _ClassVar[int]
    task_info: _apollo_pb2.TaskInfo
    mapper_bucket_state_vec: _containers.RepeatedCompositeFieldContainer[MapperTaskBucketStateProto]
    def __init__(self, task_info: _Optional[_Union[_apollo_pb2.TaskInfo, _Mapping]] = ..., mapper_bucket_state_vec: _Optional[_Iterable[_Union[MapperTaskBucketStateProto, _Mapping]]] = ...) -> None: ...

class WALRecordProto(_message.Message):
    __slots__ = ("signature_sha1", "task_state_vec", "open_map_streams", "finalize_map_stream", "purge_task_id")
    class OpenMapOutputStreams(_message.Message):
        __slots__ = ("task_id", "bucket_state_vec")
        TASK_ID_FIELD_NUMBER: _ClassVar[int]
        BUCKET_STATE_VEC_FIELD_NUMBER: _ClassVar[int]
        task_id: _unique_id_pb2.UniqueId
        bucket_state_vec: _containers.RepeatedCompositeFieldContainer[MapperTaskBucketStateProto]
        def __init__(self, task_id: _Optional[_Union[_unique_id_pb2.UniqueId, _Mapping]] = ..., bucket_state_vec: _Optional[_Iterable[_Union[MapperTaskBucketStateProto, _Mapping]]] = ...) -> None: ...
    SIGNATURE_SHA1_FIELD_NUMBER: _ClassVar[int]
    TASK_STATE_VEC_FIELD_NUMBER: _ClassVar[int]
    OPEN_MAP_STREAMS_FIELD_NUMBER: _ClassVar[int]
    FINALIZE_MAP_STREAM_FIELD_NUMBER: _ClassVar[int]
    PURGE_TASK_ID_FIELD_NUMBER: _ClassVar[int]
    signature_sha1: str
    task_state_vec: _containers.RepeatedCompositeFieldContainer[TaskStateProto]
    open_map_streams: WALRecordProto.OpenMapOutputStreams
    finalize_map_stream: MapperTaskBucketStateProto
    purge_task_id: _unique_id_pb2.UniqueId
    def __init__(self, signature_sha1: _Optional[str] = ..., task_state_vec: _Optional[_Iterable[_Union[TaskStateProto, _Mapping]]] = ..., open_map_streams: _Optional[_Union[WALRecordProto.OpenMapOutputStreams, _Mapping]] = ..., finalize_map_stream: _Optional[_Union[MapperTaskBucketStateProto, _Mapping]] = ..., purge_task_id: _Optional[_Union[_unique_id_pb2.UniqueId, _Mapping]] = ...) -> None: ...
