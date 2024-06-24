from open_util.net import protorpc_pb2 as _protorpc_pb2
from librarian.base import error_pb2 as _error_pb2
from librarian.base import librarian_pb2 as _librarian_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UpdateIndexMigrationTaskStatusArg(_message.Message):
    __slots__ = ("task_id", "index_name", "constituent_id", "error")
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    INDEX_NAME_FIELD_NUMBER: _ClassVar[int]
    CONSTITUENT_ID_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    task_id: int
    index_name: str
    constituent_id: int
    error: _error_pb2.ErrorProto
    def __init__(self, task_id: _Optional[int] = ..., index_name: _Optional[str] = ..., constituent_id: _Optional[int] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class UpdateIndexMigrationTaskStatusResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UpdateBucketInstanceMetadataArg(_message.Message):
    __slots__ = ("index_name", "bucket_id", "bucket_incarnation_id", "task_id", "read_only", "replication_in_progress", "shuffle_keys_cookie", "prune_keys_cookie", "pruning_completed")
    INDEX_NAME_FIELD_NUMBER: _ClassVar[int]
    BUCKET_ID_FIELD_NUMBER: _ClassVar[int]
    BUCKET_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    READ_ONLY_FIELD_NUMBER: _ClassVar[int]
    REPLICATION_IN_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    SHUFFLE_KEYS_COOKIE_FIELD_NUMBER: _ClassVar[int]
    PRUNE_KEYS_COOKIE_FIELD_NUMBER: _ClassVar[int]
    PRUNING_COMPLETED_FIELD_NUMBER: _ClassVar[int]
    index_name: str
    bucket_id: int
    bucket_incarnation_id: int
    task_id: int
    read_only: bool
    replication_in_progress: bool
    shuffle_keys_cookie: bytes
    prune_keys_cookie: bytes
    pruning_completed: bool
    def __init__(self, index_name: _Optional[str] = ..., bucket_id: _Optional[int] = ..., bucket_incarnation_id: _Optional[int] = ..., task_id: _Optional[int] = ..., read_only: bool = ..., replication_in_progress: bool = ..., shuffle_keys_cookie: _Optional[bytes] = ..., prune_keys_cookie: _Optional[bytes] = ..., pruning_completed: bool = ...) -> None: ...

class UpdateBucketInstanceMetadataResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class GetBucketInstanceMetadataArg(_message.Message):
    __slots__ = ("index_name", "bucket_id", "bucket_incarnation_id", "task_id")
    INDEX_NAME_FIELD_NUMBER: _ClassVar[int]
    BUCKET_ID_FIELD_NUMBER: _ClassVar[int]
    BUCKET_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    index_name: str
    bucket_id: int
    bucket_incarnation_id: int
    task_id: int
    def __init__(self, index_name: _Optional[str] = ..., bucket_id: _Optional[int] = ..., bucket_incarnation_id: _Optional[int] = ..., task_id: _Optional[int] = ...) -> None: ...

class GetBucketInstanceMetadataResult(_message.Message):
    __slots__ = ("read_only", "replication_in_progress", "shuffle_keys_cookie", "prune_keys_cookie")
    READ_ONLY_FIELD_NUMBER: _ClassVar[int]
    REPLICATION_IN_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    SHUFFLE_KEYS_COOKIE_FIELD_NUMBER: _ClassVar[int]
    PRUNE_KEYS_COOKIE_FIELD_NUMBER: _ClassVar[int]
    read_only: bool
    replication_in_progress: bool
    shuffle_keys_cookie: bytes
    prune_keys_cookie: bytes
    def __init__(self, read_only: bool = ..., replication_in_progress: bool = ..., shuffle_keys_cookie: _Optional[bytes] = ..., prune_keys_cookie: _Optional[bytes] = ...) -> None: ...

class GetIndicesToPruneArg(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetIndicesToPruneResult(_message.Message):
    __slots__ = ("indices_to_prune",)
    INDICES_TO_PRUNE_FIELD_NUMBER: _ClassVar[int]
    indices_to_prune: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, indices_to_prune: _Optional[_Iterable[str]] = ...) -> None: ...

class SlaveReplicaStatusArg(_message.Message):
    __slots__ = ("index_name", "constituent_id", "replica_state_vec")
    class ReplicaState(_message.Message):
        __slots__ = ("bucket_id", "disk_id", "usable", "error")
        BUCKET_ID_FIELD_NUMBER: _ClassVar[int]
        DISK_ID_FIELD_NUMBER: _ClassVar[int]
        USABLE_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        bucket_id: int
        disk_id: int
        usable: bool
        error: _error_pb2.ErrorProto
        def __init__(self, bucket_id: _Optional[int] = ..., disk_id: _Optional[int] = ..., usable: bool = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...
    INDEX_NAME_FIELD_NUMBER: _ClassVar[int]
    CONSTITUENT_ID_FIELD_NUMBER: _ClassVar[int]
    REPLICA_STATE_VEC_FIELD_NUMBER: _ClassVar[int]
    index_name: str
    constituent_id: int
    replica_state_vec: _containers.RepeatedCompositeFieldContainer[SlaveReplicaStatusArg.ReplicaState]
    def __init__(self, index_name: _Optional[str] = ..., constituent_id: _Optional[int] = ..., replica_state_vec: _Optional[_Iterable[_Union[SlaveReplicaStatusArg.ReplicaState, _Mapping]]] = ...) -> None: ...

class SlaveReplicaStatusResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
