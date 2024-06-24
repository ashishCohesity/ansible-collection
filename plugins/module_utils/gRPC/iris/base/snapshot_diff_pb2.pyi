from yoda.master.stub import yoda_rpc_args_pb2 as _yoda_rpc_args_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SnapshotDiff(_message.Message):
    __slots__ = ("job_id", "entity_id", "base_job_instance_id", "base_job_start_time_usecs", "job_instance_id", "job_start_time_usecs", "cfile_handle", "status", "filelist", "expiry_timestamp_secs", "range_start", "range_end", "cookie_list", "key", "max_idx")
    class SnapshotDiffStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kRunning: _ClassVar[SnapshotDiff.SnapshotDiffStatus]
        kCompleted: _ClassVar[SnapshotDiff.SnapshotDiffStatus]
        kError: _ClassVar[SnapshotDiff.SnapshotDiffStatus]
    kRunning: SnapshotDiff.SnapshotDiffStatus
    kCompleted: SnapshotDiff.SnapshotDiffStatus
    kError: SnapshotDiff.SnapshotDiffStatus
    class FileOperation(_message.Message):
        __slots__ = ("filename", "operation")
        FILENAME_FIELD_NUMBER: _ClassVar[int]
        OPERATION_FIELD_NUMBER: _ClassVar[int]
        filename: str
        operation: str
        def __init__(self, filename: _Optional[str] = ..., operation: _Optional[str] = ...) -> None: ...
    class CookieDetails(_message.Message):
        __slots__ = ("cookie", "start_index")
        COOKIE_FIELD_NUMBER: _ClassVar[int]
        START_INDEX_FIELD_NUMBER: _ClassVar[int]
        cookie: bytes
        start_index: int
        def __init__(self, cookie: _Optional[bytes] = ..., start_index: _Optional[int] = ...) -> None: ...
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    BASE_JOB_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    BASE_JOB_START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    JOB_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    JOB_START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    CFILE_HANDLE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    FILELIST_FIELD_NUMBER: _ClassVar[int]
    EXPIRY_TIMESTAMP_SECS_FIELD_NUMBER: _ClassVar[int]
    RANGE_START_FIELD_NUMBER: _ClassVar[int]
    RANGE_END_FIELD_NUMBER: _ClassVar[int]
    COOKIE_LIST_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    MAX_IDX_FIELD_NUMBER: _ClassVar[int]
    job_id: int
    entity_id: int
    base_job_instance_id: int
    base_job_start_time_usecs: int
    job_instance_id: int
    job_start_time_usecs: int
    cfile_handle: _yoda_rpc_args_pb2.CrackedFileIndexHandle
    status: SnapshotDiff.SnapshotDiffStatus
    filelist: _containers.RepeatedCompositeFieldContainer[SnapshotDiff.FileOperation]
    expiry_timestamp_secs: int
    range_start: int
    range_end: int
    cookie_list: _containers.RepeatedCompositeFieldContainer[SnapshotDiff.CookieDetails]
    key: str
    max_idx: int
    def __init__(self, job_id: _Optional[int] = ..., entity_id: _Optional[int] = ..., base_job_instance_id: _Optional[int] = ..., base_job_start_time_usecs: _Optional[int] = ..., job_instance_id: _Optional[int] = ..., job_start_time_usecs: _Optional[int] = ..., cfile_handle: _Optional[_Union[_yoda_rpc_args_pb2.CrackedFileIndexHandle, _Mapping]] = ..., status: _Optional[_Union[SnapshotDiff.SnapshotDiffStatus, str]] = ..., filelist: _Optional[_Iterable[_Union[SnapshotDiff.FileOperation, _Mapping]]] = ..., expiry_timestamp_secs: _Optional[int] = ..., range_start: _Optional[int] = ..., range_end: _Optional[int] = ..., cookie_list: _Optional[_Iterable[_Union[SnapshotDiff.CookieDetails, _Mapping]]] = ..., key: _Optional[str] = ..., max_idx: _Optional[int] = ...) -> None: ...

class SnapshotDiffList(_message.Message):
    __slots__ = ("snapshot_diffs",)
    SNAPSHOT_DIFFS_FIELD_NUMBER: _ClassVar[int]
    snapshot_diffs: _containers.RepeatedCompositeFieldContainer[SnapshotDiff]
    def __init__(self, snapshot_diffs: _Optional[_Iterable[_Union[SnapshotDiff, _Mapping]]] = ...) -> None: ...
