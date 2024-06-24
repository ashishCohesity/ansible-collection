from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SqlDbSnapshotInfo(_message.Message):
    __slots__ = ("run_start_time_usecs", "attempt_num", "task_index", "db_index")
    RUN_START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    ATTEMPT_NUM_FIELD_NUMBER: _ClassVar[int]
    TASK_INDEX_FIELD_NUMBER: _ClassVar[int]
    DB_INDEX_FIELD_NUMBER: _ClassVar[int]
    run_start_time_usecs: int
    attempt_num: int
    task_index: int
    db_index: int
    def __init__(self, run_start_time_usecs: _Optional[int] = ..., attempt_num: _Optional[int] = ..., task_index: _Optional[int] = ..., db_index: _Optional[int] = ...) -> None: ...

class SqlDbRestoreNode(_message.Message):
    __slots__ = ("id", "is_root", "backup_type", "snapshot_info", "parent_id", "child_vec", "child_id_vec")
    ID_FIELD_NUMBER: _ClassVar[int]
    IS_ROOT_FIELD_NUMBER: _ClassVar[int]
    BACKUP_TYPE_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_INFO_FIELD_NUMBER: _ClassVar[int]
    PARENT_ID_FIELD_NUMBER: _ClassVar[int]
    CHILD_VEC_FIELD_NUMBER: _ClassVar[int]
    CHILD_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    id: int
    is_root: bool
    backup_type: int
    snapshot_info: SqlDbSnapshotInfo
    parent_id: int
    child_vec: _containers.RepeatedCompositeFieldContainer[SqlDbRestoreNode]
    child_id_vec: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, id: _Optional[int] = ..., is_root: bool = ..., backup_type: _Optional[int] = ..., snapshot_info: _Optional[_Union[SqlDbSnapshotInfo, _Mapping]] = ..., parent_id: _Optional[int] = ..., child_vec: _Optional[_Iterable[_Union[SqlDbRestoreNode, _Mapping]]] = ..., child_id_vec: _Optional[_Iterable[int]] = ...) -> None: ...

class SqlDbRestoreTree(_message.Message):
    __slots__ = ("all_node_vec", "root")
    ALL_NODE_VEC_FIELD_NUMBER: _ClassVar[int]
    ROOT_FIELD_NUMBER: _ClassVar[int]
    all_node_vec: _containers.RepeatedCompositeFieldContainer[SqlDbRestoreNode]
    root: SqlDbRestoreNode
    def __init__(self, all_node_vec: _Optional[_Iterable[_Union[SqlDbRestoreNode, _Mapping]]] = ..., root: _Optional[_Union[SqlDbRestoreNode, _Mapping]] = ...) -> None: ...
