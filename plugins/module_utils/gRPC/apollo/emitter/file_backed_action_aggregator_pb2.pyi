from apollo.base import unique_id_pb2 as _unique_id_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FileBackedActionKeyProto(_message.Message):
    __slots__ = ("int_key",)
    INT_KEY_FIELD_NUMBER: _ClassVar[int]
    int_key: int
    def __init__(self, int_key: _Optional[int] = ...) -> None: ...

class FileBackedActionAggregatorStateProto(_message.Message):
    __slots__ = ("state", "job_id", "deadline_usecs", "sorted_stream_seek_cookie", "disk_id_vec", "num_incarnations", "num_actions_aggregated", "num_actions_processed", "num_consolidated_actions_released", "num_actions_dropped", "num_chunks_dropped", "signature_sha1")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kAggregating: _ClassVar[FileBackedActionAggregatorStateProto.State]
        kFinalizing: _ClassVar[FileBackedActionAggregatorStateProto.State]
        kDraining: _ClassVar[FileBackedActionAggregatorStateProto.State]
        kDeleting: _ClassVar[FileBackedActionAggregatorStateProto.State]
        kFinished: _ClassVar[FileBackedActionAggregatorStateProto.State]
    kAggregating: FileBackedActionAggregatorStateProto.State
    kFinalizing: FileBackedActionAggregatorStateProto.State
    kDraining: FileBackedActionAggregatorStateProto.State
    kDeleting: FileBackedActionAggregatorStateProto.State
    kFinished: FileBackedActionAggregatorStateProto.State
    STATE_FIELD_NUMBER: _ClassVar[int]
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    DEADLINE_USECS_FIELD_NUMBER: _ClassVar[int]
    SORTED_STREAM_SEEK_COOKIE_FIELD_NUMBER: _ClassVar[int]
    DISK_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    NUM_INCARNATIONS_FIELD_NUMBER: _ClassVar[int]
    NUM_ACTIONS_AGGREGATED_FIELD_NUMBER: _ClassVar[int]
    NUM_ACTIONS_PROCESSED_FIELD_NUMBER: _ClassVar[int]
    NUM_CONSOLIDATED_ACTIONS_RELEASED_FIELD_NUMBER: _ClassVar[int]
    NUM_ACTIONS_DROPPED_FIELD_NUMBER: _ClassVar[int]
    NUM_CHUNKS_DROPPED_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_SHA1_FIELD_NUMBER: _ClassVar[int]
    state: FileBackedActionAggregatorStateProto.State
    job_id: _unique_id_pb2.UniqueId
    deadline_usecs: int
    sorted_stream_seek_cookie: bytes
    disk_id_vec: _containers.RepeatedScalarFieldContainer[int]
    num_incarnations: int
    num_actions_aggregated: int
    num_actions_processed: int
    num_consolidated_actions_released: int
    num_actions_dropped: int
    num_chunks_dropped: int
    signature_sha1: str
    def __init__(self, state: _Optional[_Union[FileBackedActionAggregatorStateProto.State, str]] = ..., job_id: _Optional[_Union[_unique_id_pb2.UniqueId, _Mapping]] = ..., deadline_usecs: _Optional[int] = ..., sorted_stream_seek_cookie: _Optional[bytes] = ..., disk_id_vec: _Optional[_Iterable[int]] = ..., num_incarnations: _Optional[int] = ..., num_actions_aggregated: _Optional[int] = ..., num_actions_processed: _Optional[int] = ..., num_consolidated_actions_released: _Optional[int] = ..., num_actions_dropped: _Optional[int] = ..., num_chunks_dropped: _Optional[int] = ..., signature_sha1: _Optional[str] = ...) -> None: ...
