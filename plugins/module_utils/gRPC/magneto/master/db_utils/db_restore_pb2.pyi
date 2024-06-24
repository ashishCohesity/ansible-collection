from magneto.base import entity_pb2 as _entity_pb2
from magneto.base import enums_pb2 as _enums_pb2
from magneto.base import magneto_pb2 as _magneto_pb2
from magneto.base import env_params_pb2 as _env_params_pb2
from util.base import universal_id_pb2 as _universal_id_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import python_message as _python_message
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DbRestoreSnapshotInfo(_message.Message):
    __slots__ = ("run_start_time_usecs", "job_uid", "job_instance_id", "attempt_num", "task_index", "task_id", "db_index", "full_db_name", "backup_type", "db_server_backup_start_time_msecs", "node_id")
    RUN_START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    JOB_UID_FIELD_NUMBER: _ClassVar[int]
    JOB_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    ATTEMPT_NUM_FIELD_NUMBER: _ClassVar[int]
    TASK_INDEX_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    DB_INDEX_FIELD_NUMBER: _ClassVar[int]
    FULL_DB_NAME_FIELD_NUMBER: _ClassVar[int]
    BACKUP_TYPE_FIELD_NUMBER: _ClassVar[int]
    DB_SERVER_BACKUP_START_TIME_MSECS_FIELD_NUMBER: _ClassVar[int]
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    run_start_time_usecs: int
    job_uid: _universal_id_pb2.UniversalIdProto
    job_instance_id: int
    attempt_num: int
    task_index: int
    task_id: int
    db_index: int
    full_db_name: str
    backup_type: _enums_pb2.ScheduledBackupType.Type
    db_server_backup_start_time_msecs: int
    node_id: int
    def __init__(self, run_start_time_usecs: _Optional[int] = ..., job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., job_instance_id: _Optional[int] = ..., attempt_num: _Optional[int] = ..., task_index: _Optional[int] = ..., task_id: _Optional[int] = ..., db_index: _Optional[int] = ..., full_db_name: _Optional[str] = ..., backup_type: _Optional[_Union[_enums_pb2.ScheduledBackupType.Type, str]] = ..., db_server_backup_start_time_msecs: _Optional[int] = ..., node_id: _Optional[int] = ...) -> None: ...

class DbRestoreNode(_message.Message):
    __slots__ = ("id", "is_root", "snapshot_info", "parent_id", "child_id_vec", "max_child_db_server_backup_start_time_msecs")
    Extensions: _python_message._ExtensionDict
    ID_FIELD_NUMBER: _ClassVar[int]
    IS_ROOT_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_INFO_FIELD_NUMBER: _ClassVar[int]
    PARENT_ID_FIELD_NUMBER: _ClassVar[int]
    CHILD_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    MAX_CHILD_DB_SERVER_BACKUP_START_TIME_MSECS_FIELD_NUMBER: _ClassVar[int]
    id: int
    is_root: bool
    snapshot_info: DbRestoreSnapshotInfo
    parent_id: int
    child_id_vec: _containers.RepeatedScalarFieldContainer[int]
    max_child_db_server_backup_start_time_msecs: int
    def __init__(self, id: _Optional[int] = ..., is_root: bool = ..., snapshot_info: _Optional[_Union[DbRestoreSnapshotInfo, _Mapping]] = ..., parent_id: _Optional[int] = ..., child_id_vec: _Optional[_Iterable[int]] = ..., max_child_db_server_backup_start_time_msecs: _Optional[int] = ...) -> None: ...

class DbRestoreTree(_message.Message):
    __slots__ = ("tree_id", "db_entity", "all_node_vec", "root_node_id")
    TREE_ID_FIELD_NUMBER: _ClassVar[int]
    DB_ENTITY_FIELD_NUMBER: _ClassVar[int]
    ALL_NODE_VEC_FIELD_NUMBER: _ClassVar[int]
    ROOT_NODE_ID_FIELD_NUMBER: _ClassVar[int]
    tree_id: int
    db_entity: _entity_pb2.EntityProto
    all_node_vec: _containers.RepeatedCompositeFieldContainer[DbRestoreNode]
    root_node_id: int
    def __init__(self, tree_id: _Optional[int] = ..., db_entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., all_node_vec: _Optional[_Iterable[_Union[DbRestoreNode, _Mapping]]] = ..., root_node_id: _Optional[int] = ...) -> None: ...

class DbRestorePath(_message.Message):
    __slots__ = ("db_entity", "full_snapshot_node_id", "log_snapshot_node_id_vec")
    DB_ENTITY_FIELD_NUMBER: _ClassVar[int]
    FULL_SNAPSHOT_NODE_ID_FIELD_NUMBER: _ClassVar[int]
    LOG_SNAPSHOT_NODE_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    db_entity: _entity_pb2.EntityProto
    full_snapshot_node_id: int
    log_snapshot_node_id_vec: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, db_entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., full_snapshot_node_id: _Optional[int] = ..., log_snapshot_node_id_vec: _Optional[_Iterable[int]] = ...) -> None: ...

class DbRecoveryPlan(_message.Message):
    __slots__ = ("path_group_vec",)
    class PathGroup(_message.Message):
        __slots__ = ("run_start_time_usecs", "path_vec")
        RUN_START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
        PATH_VEC_FIELD_NUMBER: _ClassVar[int]
        run_start_time_usecs: int
        path_vec: _containers.RepeatedCompositeFieldContainer[DbRestorePath]
        def __init__(self, run_start_time_usecs: _Optional[int] = ..., path_vec: _Optional[_Iterable[_Union[DbRestorePath, _Mapping]]] = ...) -> None: ...
    PATH_GROUP_VEC_FIELD_NUMBER: _ClassVar[int]
    path_group_vec: _containers.RepeatedCompositeFieldContainer[DbRecoveryPlan.PathGroup]
    def __init__(self, path_group_vec: _Optional[_Iterable[_Union[DbRecoveryPlan.PathGroup, _Mapping]]] = ...) -> None: ...
