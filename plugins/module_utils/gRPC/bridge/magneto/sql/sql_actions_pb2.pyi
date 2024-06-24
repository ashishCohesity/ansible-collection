from bridge.magneto.base import magneto_actions_pb2 as _magneto_actions_pb2
from magneto.base.entities import sql_pb2 as _sql_pb2
from magneto.base import entity_pb2 as _entity_pb2
from magneto.base import enums_pb2 as _enums_pb2
from magneto.base import magneto_pb2 as _magneto_pb2
from magneto.base import env_params_pb2 as _env_params_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AgentInfo(_message.Message):
    __slots__ = ("connector_params", "agent_version", "agent_incarnation_id")
    CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    AGENT_VERSION_FIELD_NUMBER: _ClassVar[int]
    AGENT_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    connector_params: _magneto_pb2.ConnectorParams
    agent_version: int
    agent_incarnation_id: int
    def __init__(self, connector_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ..., agent_version: _Optional[int] = ..., agent_incarnation_id: _Optional[int] = ...) -> None: ...

class StreamIOParams(_message.Message):
    __slots__ = ("stream_id", "stream_offset", "stream_data_length")
    STREAM_ID_FIELD_NUMBER: _ClassVar[int]
    STREAM_OFFSET_FIELD_NUMBER: _ClassVar[int]
    STREAM_DATA_LENGTH_FIELD_NUMBER: _ClassVar[int]
    stream_id: int
    stream_offset: int
    stream_data_length: int
    def __init__(self, stream_id: _Optional[int] = ..., stream_offset: _Optional[int] = ..., stream_data_length: _Optional[int] = ...) -> None: ...

class MigrateHostViewArg(_message.Message):
    __slots__ = ("job_id", "job_instance_id", "attempt_num", "view_box_id", "source_view_name", "dest_view_name", "dest_snapshot_dir", "qos_principal_name")
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    JOB_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    ATTEMPT_NUM_FIELD_NUMBER: _ClassVar[int]
    VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    DEST_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    DEST_SNAPSHOT_DIR_FIELD_NUMBER: _ClassVar[int]
    QOS_PRINCIPAL_NAME_FIELD_NUMBER: _ClassVar[int]
    job_id: int
    job_instance_id: int
    attempt_num: int
    view_box_id: int
    source_view_name: str
    dest_view_name: str
    dest_snapshot_dir: str
    qos_principal_name: str
    def __init__(self, job_id: _Optional[int] = ..., job_instance_id: _Optional[int] = ..., attempt_num: _Optional[int] = ..., view_box_id: _Optional[int] = ..., source_view_name: _Optional[str] = ..., dest_view_name: _Optional[str] = ..., dest_snapshot_dir: _Optional[str] = ..., qos_principal_name: _Optional[str] = ...) -> None: ...

class PopulateNativeRestoreViewArg(_message.Message):
    __slots__ = ("view_box_id", "src_view_name", "dest_view_name", "src_snapshot_dir", "backup_file_name_vec", "view_whitelist_ip_addr_str_vec")
    VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
    SRC_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    DEST_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    SRC_SNAPSHOT_DIR_FIELD_NUMBER: _ClassVar[int]
    BACKUP_FILE_NAME_VEC_FIELD_NUMBER: _ClassVar[int]
    VIEW_WHITELIST_IP_ADDR_STR_VEC_FIELD_NUMBER: _ClassVar[int]
    view_box_id: int
    src_view_name: str
    dest_view_name: str
    src_snapshot_dir: str
    backup_file_name_vec: _containers.RepeatedScalarFieldContainer[str]
    view_whitelist_ip_addr_str_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, view_box_id: _Optional[int] = ..., src_view_name: _Optional[str] = ..., dest_view_name: _Optional[str] = ..., src_snapshot_dir: _Optional[str] = ..., backup_file_name_vec: _Optional[_Iterable[str]] = ..., view_whitelist_ip_addr_str_vec: _Optional[_Iterable[str]] = ...) -> None: ...

class ClonePreviousBackupFilesArg(_message.Message):
    __slots__ = ("job_id", "job_instance_id", "root_path", "relative_snapshot_dir", "relative_prev_snapshot_dir", "backup_file_name_vec")
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    JOB_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    ROOT_PATH_FIELD_NUMBER: _ClassVar[int]
    RELATIVE_SNAPSHOT_DIR_FIELD_NUMBER: _ClassVar[int]
    RELATIVE_PREV_SNAPSHOT_DIR_FIELD_NUMBER: _ClassVar[int]
    BACKUP_FILE_NAME_VEC_FIELD_NUMBER: _ClassVar[int]
    job_id: int
    job_instance_id: int
    root_path: str
    relative_snapshot_dir: str
    relative_prev_snapshot_dir: str
    backup_file_name_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, job_id: _Optional[int] = ..., job_instance_id: _Optional[int] = ..., root_path: _Optional[str] = ..., relative_snapshot_dir: _Optional[str] = ..., relative_prev_snapshot_dir: _Optional[str] = ..., backup_file_name_vec: _Optional[_Iterable[str]] = ...) -> None: ...

class SqlLogBackupArg(_message.Message):
    __slots__ = ("type", "database_id", "view_box_id", "view_name", "qos_principal_name", "job_id", "job_instance_id", "attempt_num", "root_entity", "source_entity", "file_name", "io_params", "stats_container_id", "root_path", "relative_snapshot_dir", "database_name", "cluster_id", "cluster_incarnation_id")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kPrepareLogBackup: _ClassVar[SqlLogBackupArg.Type]
        kReadData: _ClassVar[SqlLogBackupArg.Type]
        kEndLogBackup: _ClassVar[SqlLogBackupArg.Type]
    kPrepareLogBackup: SqlLogBackupArg.Type
    kReadData: SqlLogBackupArg.Type
    kEndLogBackup: SqlLogBackupArg.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DATABASE_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    QOS_PRINCIPAL_NAME_FIELD_NUMBER: _ClassVar[int]
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    JOB_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    ATTEMPT_NUM_FIELD_NUMBER: _ClassVar[int]
    ROOT_ENTITY_FIELD_NUMBER: _ClassVar[int]
    SOURCE_ENTITY_FIELD_NUMBER: _ClassVar[int]
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    IO_PARAMS_FIELD_NUMBER: _ClassVar[int]
    STATS_CONTAINER_ID_FIELD_NUMBER: _ClassVar[int]
    ROOT_PATH_FIELD_NUMBER: _ClassVar[int]
    RELATIVE_SNAPSHOT_DIR_FIELD_NUMBER: _ClassVar[int]
    DATABASE_NAME_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    type: SqlLogBackupArg.Type
    database_id: _sql_pb2.SqlId
    view_box_id: int
    view_name: str
    qos_principal_name: str
    job_id: int
    job_instance_id: int
    attempt_num: int
    root_entity: _entity_pb2.EntityProto
    source_entity: _entity_pb2.EntityProto
    file_name: str
    io_params: StreamIOParams
    stats_container_id: int
    root_path: str
    relative_snapshot_dir: str
    database_name: str
    cluster_id: int
    cluster_incarnation_id: int
    def __init__(self, type: _Optional[_Union[SqlLogBackupArg.Type, str]] = ..., database_id: _Optional[_Union[_sql_pb2.SqlId, _Mapping]] = ..., view_box_id: _Optional[int] = ..., view_name: _Optional[str] = ..., qos_principal_name: _Optional[str] = ..., job_id: _Optional[int] = ..., job_instance_id: _Optional[int] = ..., attempt_num: _Optional[int] = ..., root_entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., source_entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., file_name: _Optional[str] = ..., io_params: _Optional[_Union[StreamIOParams, _Mapping]] = ..., stats_container_id: _Optional[int] = ..., root_path: _Optional[str] = ..., relative_snapshot_dir: _Optional[str] = ..., database_name: _Optional[str] = ..., cluster_id: _Optional[int] = ..., cluster_incarnation_id: _Optional[int] = ...) -> None: ...

class WriteSqlDataArg(_message.Message):
    __slots__ = ("io_params",)
    IO_PARAMS_FIELD_NUMBER: _ClassVar[int]
    io_params: StreamIOParams
    def __init__(self, io_params: _Optional[_Union[StreamIOParams, _Mapping]] = ...) -> None: ...

class CancelStreamIOArg(_message.Message):
    __slots__ = ("stream_id_vec",)
    STREAM_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    stream_id_vec: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, stream_id_vec: _Optional[_Iterable[int]] = ...) -> None: ...

class SqlLogReplayArg(_message.Message):
    __slots__ = ("type", "source_env_type", "database_id", "view_box_id", "view_name", "source_view_name", "file_path", "target_dir_name", "io_params", "root_path", "cluster_id", "cluster_incarnation_id")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kPrepareLogReplay: _ClassVar[SqlLogReplayArg.Type]
        kWriteData: _ClassVar[SqlLogReplayArg.Type]
        kEndLogReplay: _ClassVar[SqlLogReplayArg.Type]
        kDeleteView: _ClassVar[SqlLogReplayArg.Type]
    kPrepareLogReplay: SqlLogReplayArg.Type
    kWriteData: SqlLogReplayArg.Type
    kEndLogReplay: SqlLogReplayArg.Type
    kDeleteView: SqlLogReplayArg.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_ENV_TYPE_FIELD_NUMBER: _ClassVar[int]
    DATABASE_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    SOURCE_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    TARGET_DIR_NAME_FIELD_NUMBER: _ClassVar[int]
    IO_PARAMS_FIELD_NUMBER: _ClassVar[int]
    ROOT_PATH_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    type: SqlLogReplayArg.Type
    source_env_type: _enums_pb2.Environment.Type
    database_id: _sql_pb2.SqlId
    view_box_id: int
    view_name: str
    source_view_name: str
    file_path: str
    target_dir_name: str
    io_params: StreamIOParams
    root_path: str
    cluster_id: int
    cluster_incarnation_id: int
    def __init__(self, type: _Optional[_Union[SqlLogReplayArg.Type, str]] = ..., source_env_type: _Optional[_Union[_enums_pb2.Environment.Type, str]] = ..., database_id: _Optional[_Union[_sql_pb2.SqlId, _Mapping]] = ..., view_box_id: _Optional[int] = ..., view_name: _Optional[str] = ..., source_view_name: _Optional[str] = ..., file_path: _Optional[str] = ..., target_dir_name: _Optional[str] = ..., io_params: _Optional[_Union[StreamIOParams, _Mapping]] = ..., root_path: _Optional[str] = ..., cluster_id: _Optional[int] = ..., cluster_incarnation_id: _Optional[int] = ...) -> None: ...

class SqlActionArg(_message.Message):
    __slots__ = ("task_id", "agent_info", "sql_log_backup_arg", "write_sql_data_arg", "cancel_stream_io_arg", "sql_log_replay_arg", "migrate_host_view_arg", "populate_native_restore_view_arg", "clone_previous_backup_files_arg")
    SQL_ACTION_ARG_FIELD_NUMBER: _ClassVar[int]
    sql_action_arg: _descriptor.FieldDescriptor
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    AGENT_INFO_FIELD_NUMBER: _ClassVar[int]
    SQL_LOG_BACKUP_ARG_FIELD_NUMBER: _ClassVar[int]
    WRITE_SQL_DATA_ARG_FIELD_NUMBER: _ClassVar[int]
    CANCEL_STREAM_IO_ARG_FIELD_NUMBER: _ClassVar[int]
    SQL_LOG_REPLAY_ARG_FIELD_NUMBER: _ClassVar[int]
    MIGRATE_HOST_VIEW_ARG_FIELD_NUMBER: _ClassVar[int]
    POPULATE_NATIVE_RESTORE_VIEW_ARG_FIELD_NUMBER: _ClassVar[int]
    CLONE_PREVIOUS_BACKUP_FILES_ARG_FIELD_NUMBER: _ClassVar[int]
    task_id: int
    agent_info: AgentInfo
    sql_log_backup_arg: SqlLogBackupArg
    write_sql_data_arg: WriteSqlDataArg
    cancel_stream_io_arg: CancelStreamIOArg
    sql_log_replay_arg: SqlLogReplayArg
    migrate_host_view_arg: MigrateHostViewArg
    populate_native_restore_view_arg: PopulateNativeRestoreViewArg
    clone_previous_backup_files_arg: ClonePreviousBackupFilesArg
    def __init__(self, task_id: _Optional[int] = ..., agent_info: _Optional[_Union[AgentInfo, _Mapping]] = ..., sql_log_backup_arg: _Optional[_Union[SqlLogBackupArg, _Mapping]] = ..., write_sql_data_arg: _Optional[_Union[WriteSqlDataArg, _Mapping]] = ..., cancel_stream_io_arg: _Optional[_Union[CancelStreamIOArg, _Mapping]] = ..., sql_log_replay_arg: _Optional[_Union[SqlLogReplayArg, _Mapping]] = ..., migrate_host_view_arg: _Optional[_Union[MigrateHostViewArg, _Mapping]] = ..., populate_native_restore_view_arg: _Optional[_Union[PopulateNativeRestoreViewArg, _Mapping]] = ..., clone_previous_backup_files_arg: _Optional[_Union[ClonePreviousBackupFilesArg, _Mapping]] = ...) -> None: ...
