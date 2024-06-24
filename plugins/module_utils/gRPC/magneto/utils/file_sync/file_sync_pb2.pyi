from magneto.base import error_pb2 as _error_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Range(_message.Message):
    __slots__ = ("start_offset", "size")
    START_OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    start_offset: int
    size: int
    def __init__(self, start_offset: _Optional[int] = ..., size: _Optional[int] = ...) -> None: ...

class FileDiffBatch(_message.Message):
    __slots__ = ("file_range", "diff_range_vec", "total_diff_size_bytes", "status")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kWaiting: _ClassVar[FileDiffBatch.Status]
        kDispatched: _ClassVar[FileDiffBatch.Status]
        kFinished: _ClassVar[FileDiffBatch.Status]
    kWaiting: FileDiffBatch.Status
    kDispatched: FileDiffBatch.Status
    kFinished: FileDiffBatch.Status
    FILE_RANGE_FIELD_NUMBER: _ClassVar[int]
    DIFF_RANGE_VEC_FIELD_NUMBER: _ClassVar[int]
    TOTAL_DIFF_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    file_range: Range
    diff_range_vec: _containers.RepeatedCompositeFieldContainer[Range]
    total_diff_size_bytes: int
    status: FileDiffBatch.Status
    def __init__(self, file_range: _Optional[_Union[Range, _Mapping]] = ..., diff_range_vec: _Optional[_Iterable[_Union[Range, _Mapping]]] = ..., total_diff_size_bytes: _Optional[int] = ..., status: _Optional[_Union[FileDiffBatch.Status, str]] = ...) -> None: ...

class TaskState(_message.Message):
    __slots__ = ("target_snapshot_full_snapfs_file_path", "base_snapshot_full_snapfs_file_path", "synced_offset", "status", "error", "total_logical_size_bytes", "total_physical_size_bytes")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kInProgress: _ClassVar[TaskState.Status]
        kFinished: _ClassVar[TaskState.Status]
        kCancelled: _ClassVar[TaskState.Status]
    kInProgress: TaskState.Status
    kFinished: TaskState.Status
    kCancelled: TaskState.Status
    TARGET_SNAPSHOT_FULL_SNAPFS_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    BASE_SNAPSHOT_FULL_SNAPFS_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    SYNCED_OFFSET_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    TOTAL_LOGICAL_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    TOTAL_PHYSICAL_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    target_snapshot_full_snapfs_file_path: str
    base_snapshot_full_snapfs_file_path: str
    synced_offset: int
    status: TaskState.Status
    error: _error_pb2.ErrorProto
    total_logical_size_bytes: int
    total_physical_size_bytes: int
    def __init__(self, target_snapshot_full_snapfs_file_path: _Optional[str] = ..., base_snapshot_full_snapfs_file_path: _Optional[str] = ..., synced_offset: _Optional[int] = ..., status: _Optional[_Union[TaskState.Status, str]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., total_logical_size_bytes: _Optional[int] = ..., total_physical_size_bytes: _Optional[int] = ...) -> None: ...
