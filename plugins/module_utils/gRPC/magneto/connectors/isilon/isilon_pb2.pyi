from magneto.base import magneto_pb2 as _magneto_pb2
from magneto.base import env_params_pb2 as _env_params_pb2
from magneto.connectors.file import file_pb2 as _file_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SnapshotInfo(_message.Message):
    __slots__ = ("id", "creation_time_usecs", "expire_time_usecs", "changelist_state", "changelist_job_id", "pagination_resume_token", "changelist_deleted", "skip_configure_nfs_exports", "changelist_creation_final_progress", "uses_ifs_root_for_snapshot")
    class ChangelistState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNotStarted: _ClassVar[SnapshotInfo.ChangelistState]
        kCreateRequestSent: _ClassVar[SnapshotInfo.ChangelistState]
        kCreated: _ClassVar[SnapshotInfo.ChangelistState]
        kFullyIngested: _ClassVar[SnapshotInfo.ChangelistState]
    kNotStarted: SnapshotInfo.ChangelistState
    kCreateRequestSent: SnapshotInfo.ChangelistState
    kCreated: SnapshotInfo.ChangelistState
    kFullyIngested: SnapshotInfo.ChangelistState
    ISILON_SNAPSHOT_INFO_FIELD_NUMBER: _ClassVar[int]
    isilon_snapshot_info: _descriptor.FieldDescriptor
    ID_FIELD_NUMBER: _ClassVar[int]
    CREATION_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    EXPIRE_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    CHANGELIST_STATE_FIELD_NUMBER: _ClassVar[int]
    CHANGELIST_JOB_ID_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_RESUME_TOKEN_FIELD_NUMBER: _ClassVar[int]
    CHANGELIST_DELETED_FIELD_NUMBER: _ClassVar[int]
    SKIP_CONFIGURE_NFS_EXPORTS_FIELD_NUMBER: _ClassVar[int]
    CHANGELIST_CREATION_FINAL_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    USES_IFS_ROOT_FOR_SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    id: int
    creation_time_usecs: int
    expire_time_usecs: int
    changelist_state: SnapshotInfo.ChangelistState
    changelist_job_id: int
    pagination_resume_token: str
    changelist_deleted: bool
    skip_configure_nfs_exports: bool
    changelist_creation_final_progress: str
    uses_ifs_root_for_snapshot: bool
    def __init__(self, id: _Optional[int] = ..., creation_time_usecs: _Optional[int] = ..., expire_time_usecs: _Optional[int] = ..., changelist_state: _Optional[_Union[SnapshotInfo.ChangelistState, str]] = ..., changelist_job_id: _Optional[int] = ..., pagination_resume_token: _Optional[str] = ..., changelist_deleted: bool = ..., skip_configure_nfs_exports: bool = ..., changelist_creation_final_progress: _Optional[str] = ..., uses_ifs_root_for_snapshot: bool = ...) -> None: ...

class ChangeEntry(_message.Message):
    __slots__ = ("lin",)
    ISILON_ENTRY_FIELD_NUMBER: _ClassVar[int]
    isilon_entry: _descriptor.FieldDescriptor
    LIN_FIELD_NUMBER: _ClassVar[int]
    lin: int
    def __init__(self, lin: _Optional[int] = ...) -> None: ...

class SnapChangeInfoCache(_message.Message):
    __slots__ = ("deleted_lin_map",)
    class DeletedLinMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: str
        def __init__(self, key: _Optional[int] = ..., value: _Optional[str] = ...) -> None: ...
    ISILON_SNAP_CHANGE_INFO_CACHE_FIELD_NUMBER: _ClassVar[int]
    isilon_snap_change_info_cache: _descriptor.FieldDescriptor
    DELETED_LIN_MAP_FIELD_NUMBER: _ClassVar[int]
    deleted_lin_map: _containers.ScalarMap[int, str]
    def __init__(self, deleted_lin_map: _Optional[_Mapping[int, str]] = ...) -> None: ...
