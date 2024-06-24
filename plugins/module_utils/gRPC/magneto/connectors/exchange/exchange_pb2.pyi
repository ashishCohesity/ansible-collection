from magneto.agents.base import agent_pb2 as _agent_pb2
from magneto.base.entities import exchange_pb2 as _exchange_pb2
from magneto.base import error_pb2 as _error_pb2
from magneto.base import magneto_pb2 as _magneto_pb2
from magneto.base import env_params_pb2 as _env_params_pb2
from magneto.connectors.base import common_pb2 as _common_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class VerificationInfo(_message.Message):
    __slots__ = ("exchange",)
    EXCHANGE_VERIFICATION_INFO_FIELD_NUMBER: _ClassVar[int]
    exchange_verification_info: _descriptor.FieldDescriptor
    EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    exchange: _exchange_pb2.ExchangeTopology
    def __init__(self, exchange: _Optional[_Union[_exchange_pb2.ExchangeTopology, _Mapping]] = ...) -> None: ...

class VSSFileDbPreviousSnapshotInfo(_message.Message):
    __slots__ = ("snapshot_set_id", "snapshot_root_path", "relative_snapshot_dir", "backup_info")
    SNAPSHOT_SET_ID_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_ROOT_PATH_FIELD_NUMBER: _ClassVar[int]
    RELATIVE_SNAPSHOT_DIR_FIELD_NUMBER: _ClassVar[int]
    BACKUP_INFO_FIELD_NUMBER: _ClassVar[int]
    snapshot_set_id: bytes
    snapshot_root_path: str
    relative_snapshot_dir: str
    backup_info: DatabaseBackupInfo
    def __init__(self, snapshot_set_id: _Optional[bytes] = ..., snapshot_root_path: _Optional[str] = ..., relative_snapshot_dir: _Optional[str] = ..., backup_info: _Optional[_Union[DatabaseBackupInfo, _Mapping]] = ...) -> None: ...

class DatabaseBackupInfo(_message.Message):
    __slots__ = ("db_guid", "db_name", "standalone", "dag_copy", "dag", "dag_info", "skipped", "skip_reason", "previous_task_id", "error", "warning", "start_time_usecs", "end_time_usecs", "batch_num", "vss_file_prev_snapshot_info", "sub_file_size_mb", "vss_snapshot_db_file_info_vec", "backup_finished_successfully", "log_start_counter", "log_end_counter", "manifest_filename")
    DB_GUID_FIELD_NUMBER: _ClassVar[int]
    DB_NAME_FIELD_NUMBER: _ClassVar[int]
    STANDALONE_FIELD_NUMBER: _ClassVar[int]
    DAG_COPY_FIELD_NUMBER: _ClassVar[int]
    DAG_FIELD_NUMBER: _ClassVar[int]
    DAG_INFO_FIELD_NUMBER: _ClassVar[int]
    SKIPPED_FIELD_NUMBER: _ClassVar[int]
    SKIP_REASON_FIELD_NUMBER: _ClassVar[int]
    PREVIOUS_TASK_ID_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    WARNING_FIELD_NUMBER: _ClassVar[int]
    START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    END_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    BATCH_NUM_FIELD_NUMBER: _ClassVar[int]
    VSS_FILE_PREV_SNAPSHOT_INFO_FIELD_NUMBER: _ClassVar[int]
    SUB_FILE_SIZE_MB_FIELD_NUMBER: _ClassVar[int]
    VSS_SNAPSHOT_DB_FILE_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    BACKUP_FINISHED_SUCCESSFULLY_FIELD_NUMBER: _ClassVar[int]
    LOG_START_COUNTER_FIELD_NUMBER: _ClassVar[int]
    LOG_END_COUNTER_FIELD_NUMBER: _ClassVar[int]
    MANIFEST_FILENAME_FIELD_NUMBER: _ClassVar[int]
    db_guid: str
    db_name: str
    standalone: _exchange_pb2.ExchangeDatabase
    dag_copy: _exchange_pb2.ExchangeDAGDatabaseCopy
    dag: _exchange_pb2.ExchangeDAGDatabase
    dag_info: _exchange_pb2.ExchangeDAGInfo
    skipped: bool
    skip_reason: str
    previous_task_id: int
    error: _error_pb2.ErrorProto
    warning: _error_pb2.ErrorProto
    start_time_usecs: int
    end_time_usecs: int
    batch_num: int
    vss_file_prev_snapshot_info: VSSFileDbPreviousSnapshotInfo
    sub_file_size_mb: int
    vss_snapshot_db_file_info_vec: _containers.RepeatedCompositeFieldContainer[_common_pb2.VSSSnapshotDbFileInfo]
    backup_finished_successfully: bool
    log_start_counter: int
    log_end_counter: int
    manifest_filename: str
    def __init__(self, db_guid: _Optional[str] = ..., db_name: _Optional[str] = ..., standalone: _Optional[_Union[_exchange_pb2.ExchangeDatabase, _Mapping]] = ..., dag_copy: _Optional[_Union[_exchange_pb2.ExchangeDAGDatabaseCopy, _Mapping]] = ..., dag: _Optional[_Union[_exchange_pb2.ExchangeDAGDatabase, _Mapping]] = ..., dag_info: _Optional[_Union[_exchange_pb2.ExchangeDAGInfo, _Mapping]] = ..., skipped: bool = ..., skip_reason: _Optional[str] = ..., previous_task_id: _Optional[int] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., warning: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., start_time_usecs: _Optional[int] = ..., end_time_usecs: _Optional[int] = ..., batch_num: _Optional[int] = ..., vss_file_prev_snapshot_info: _Optional[_Union[VSSFileDbPreviousSnapshotInfo, _Mapping]] = ..., sub_file_size_mb: _Optional[int] = ..., vss_snapshot_db_file_info_vec: _Optional[_Iterable[_Union[_common_pb2.VSSSnapshotDbFileInfo, _Mapping]]] = ..., backup_finished_successfully: bool = ..., log_start_counter: _Optional[int] = ..., log_end_counter: _Optional[int] = ..., manifest_filename: _Optional[str] = ...) -> None: ...

class SnapshotInfo(_message.Message):
    __slots__ = ("database_backup_info_vec", "dag_info", "snapshot_set_id", "status", "discover_exchange_done", "current_batch_num", "vss_backup_writers_vec", "vss_restore_writer", "disable_indexing", "file_cbt_warning", "exchange", "pulse_message_vec")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kCreated: _ClassVar[SnapshotInfo.Status]
        kBackup: _ClassVar[SnapshotInfo.Status]
        kDone: _ClassVar[SnapshotInfo.Status]
    kCreated: SnapshotInfo.Status
    kBackup: SnapshotInfo.Status
    kDone: SnapshotInfo.Status
    EXCHANGE_SNAPSHOT_INFO_FIELD_NUMBER: _ClassVar[int]
    exchange_snapshot_info: _descriptor.FieldDescriptor
    DATABASE_BACKUP_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    DAG_INFO_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_SET_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    DISCOVER_EXCHANGE_DONE_FIELD_NUMBER: _ClassVar[int]
    CURRENT_BATCH_NUM_FIELD_NUMBER: _ClassVar[int]
    VSS_BACKUP_WRITERS_VEC_FIELD_NUMBER: _ClassVar[int]
    VSS_RESTORE_WRITER_FIELD_NUMBER: _ClassVar[int]
    DISABLE_INDEXING_FIELD_NUMBER: _ClassVar[int]
    FILE_CBT_WARNING_FIELD_NUMBER: _ClassVar[int]
    EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    PULSE_MESSAGE_VEC_FIELD_NUMBER: _ClassVar[int]
    database_backup_info_vec: _containers.RepeatedCompositeFieldContainer[DatabaseBackupInfo]
    dag_info: _exchange_pb2.ExchangeDAGInfo
    snapshot_set_id: bytes
    status: SnapshotInfo.Status
    discover_exchange_done: bool
    current_batch_num: int
    vss_backup_writers_vec: _containers.RepeatedScalarFieldContainer[str]
    vss_restore_writer: str
    disable_indexing: bool
    file_cbt_warning: _error_pb2.ErrorProto
    exchange: _exchange_pb2.ExchangeTopology
    pulse_message_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, database_backup_info_vec: _Optional[_Iterable[_Union[DatabaseBackupInfo, _Mapping]]] = ..., dag_info: _Optional[_Union[_exchange_pb2.ExchangeDAGInfo, _Mapping]] = ..., snapshot_set_id: _Optional[bytes] = ..., status: _Optional[_Union[SnapshotInfo.Status, str]] = ..., discover_exchange_done: bool = ..., current_batch_num: _Optional[int] = ..., vss_backup_writers_vec: _Optional[_Iterable[str]] = ..., vss_restore_writer: _Optional[str] = ..., disable_indexing: bool = ..., file_cbt_warning: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., exchange: _Optional[_Union[_exchange_pb2.ExchangeTopology, _Mapping]] = ..., pulse_message_vec: _Optional[_Iterable[str]] = ...) -> None: ...

class DatabaseRestoreInfo(_message.Message):
    __slots__ = ("db_guid", "db_name", "restore_params", "db_id", "type", "edb_file_info", "log_files_info", "restore_files_info", "is_original_restore", "error", "status", "owner_snapshot_dir_full_path", "restore_disks_task_info_proto", "log_replay_info_vec", "view_name", "snapshot_relative_dir_path")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kStarted: _ClassVar[DatabaseRestoreInfo.Status]
        kValidationStarted: _ClassVar[DatabaseRestoreInfo.Status]
        kValidationDone: _ClassVar[DatabaseRestoreInfo.Status]
        kPrepareForRestoreStarted: _ClassVar[DatabaseRestoreInfo.Status]
        kPrepareForRestoreDone: _ClassVar[DatabaseRestoreInfo.Status]
        kFileCopyDone: _ClassVar[DatabaseRestoreInfo.Status]
        kLogReplayStarted: _ClassVar[DatabaseRestoreInfo.Status]
        kLogReplayDone: _ClassVar[DatabaseRestoreInfo.Status]
        kFinalizeRestoreStarted: _ClassVar[DatabaseRestoreInfo.Status]
        kFinalizeRestoreDone: _ClassVar[DatabaseRestoreInfo.Status]
    kStarted: DatabaseRestoreInfo.Status
    kValidationStarted: DatabaseRestoreInfo.Status
    kValidationDone: DatabaseRestoreInfo.Status
    kPrepareForRestoreStarted: DatabaseRestoreInfo.Status
    kPrepareForRestoreDone: DatabaseRestoreInfo.Status
    kFileCopyDone: DatabaseRestoreInfo.Status
    kLogReplayStarted: DatabaseRestoreInfo.Status
    kLogReplayDone: DatabaseRestoreInfo.Status
    kFinalizeRestoreStarted: DatabaseRestoreInfo.Status
    kFinalizeRestoreDone: DatabaseRestoreInfo.Status
    class EDBFileInfo(_message.Message):
        __slots__ = ("file_path", "db_size_bytes")
        FILE_PATH_FIELD_NUMBER: _ClassVar[int]
        DB_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
        file_path: str
        db_size_bytes: int
        def __init__(self, file_path: _Optional[str] = ..., db_size_bytes: _Optional[int] = ...) -> None: ...
    class LogFilesInfo(_message.Message):
        __slots__ = ("file_prefix", "total_size", "log_start_counter", "log_end_counter", "additional_log_files_vec")
        FILE_PREFIX_FIELD_NUMBER: _ClassVar[int]
        TOTAL_SIZE_FIELD_NUMBER: _ClassVar[int]
        LOG_START_COUNTER_FIELD_NUMBER: _ClassVar[int]
        LOG_END_COUNTER_FIELD_NUMBER: _ClassVar[int]
        ADDITIONAL_LOG_FILES_VEC_FIELD_NUMBER: _ClassVar[int]
        file_prefix: str
        total_size: int
        log_start_counter: int
        log_end_counter: int
        additional_log_files_vec: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, file_prefix: _Optional[str] = ..., total_size: _Optional[int] = ..., log_start_counter: _Optional[int] = ..., log_end_counter: _Optional[int] = ..., additional_log_files_vec: _Optional[_Iterable[str]] = ...) -> None: ...
    class LogReplayInfo(_message.Message):
        __slots__ = ("view_name", "snapshot_relative_dir_path", "restore_disks_task_info_proto")
        VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
        SNAPSHOT_RELATIVE_DIR_PATH_FIELD_NUMBER: _ClassVar[int]
        RESTORE_DISKS_TASK_INFO_PROTO_FIELD_NUMBER: _ClassVar[int]
        view_name: str
        snapshot_relative_dir_path: str
        restore_disks_task_info_proto: _magneto_pb2.SetupRestoreDiskTaskInfoProto
        def __init__(self, view_name: _Optional[str] = ..., snapshot_relative_dir_path: _Optional[str] = ..., restore_disks_task_info_proto: _Optional[_Union[_magneto_pb2.SetupRestoreDiskTaskInfoProto, _Mapping]] = ...) -> None: ...
    DB_GUID_FIELD_NUMBER: _ClassVar[int]
    DB_NAME_FIELD_NUMBER: _ClassVar[int]
    RESTORE_PARAMS_FIELD_NUMBER: _ClassVar[int]
    DB_ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    EDB_FILE_INFO_FIELD_NUMBER: _ClassVar[int]
    LOG_FILES_INFO_FIELD_NUMBER: _ClassVar[int]
    RESTORE_FILES_INFO_FIELD_NUMBER: _ClassVar[int]
    IS_ORIGINAL_RESTORE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    OWNER_SNAPSHOT_DIR_FULL_PATH_FIELD_NUMBER: _ClassVar[int]
    RESTORE_DISKS_TASK_INFO_PROTO_FIELD_NUMBER: _ClassVar[int]
    LOG_REPLAY_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_RELATIVE_DIR_PATH_FIELD_NUMBER: _ClassVar[int]
    db_guid: str
    db_name: str
    restore_params: _magneto_pb2.RestoreExchangeParams
    db_id: int
    type: _exchange_pb2.ExchangeDatabase.ExchangeDatabaseType.Type
    edb_file_info: DatabaseRestoreInfo.EDBFileInfo
    log_files_info: DatabaseRestoreInfo.LogFilesInfo
    restore_files_info: _magneto_pb2.RestoreFilesInfoProto
    is_original_restore: bool
    error: _error_pb2.ErrorProto
    status: DatabaseRestoreInfo.Status
    owner_snapshot_dir_full_path: str
    restore_disks_task_info_proto: _magneto_pb2.SetupRestoreDiskTaskInfoProto
    log_replay_info_vec: _containers.RepeatedCompositeFieldContainer[DatabaseRestoreInfo.LogReplayInfo]
    view_name: str
    snapshot_relative_dir_path: str
    def __init__(self, db_guid: _Optional[str] = ..., db_name: _Optional[str] = ..., restore_params: _Optional[_Union[_magneto_pb2.RestoreExchangeParams, _Mapping]] = ..., db_id: _Optional[int] = ..., type: _Optional[_Union[_exchange_pb2.ExchangeDatabase.ExchangeDatabaseType.Type, str]] = ..., edb_file_info: _Optional[_Union[DatabaseRestoreInfo.EDBFileInfo, _Mapping]] = ..., log_files_info: _Optional[_Union[DatabaseRestoreInfo.LogFilesInfo, _Mapping]] = ..., restore_files_info: _Optional[_Union[_magneto_pb2.RestoreFilesInfoProto, _Mapping]] = ..., is_original_restore: bool = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., status: _Optional[_Union[DatabaseRestoreInfo.Status, str]] = ..., owner_snapshot_dir_full_path: _Optional[str] = ..., restore_disks_task_info_proto: _Optional[_Union[_magneto_pb2.SetupRestoreDiskTaskInfoProto, _Mapping]] = ..., log_replay_info_vec: _Optional[_Iterable[_Union[DatabaseRestoreInfo.LogReplayInfo, _Mapping]]] = ..., view_name: _Optional[str] = ..., snapshot_relative_dir_path: _Optional[str] = ...) -> None: ...

class VSSDatabaseRestoreInfo(_message.Message):
    __slots__ = ("snapshot_set_id", "server_snapshot_info", "owner_snapshot_dir_full_path", "server_snapshot_info_file_name", "common_host_dir_name", "is_common_host_dir_cloned_under_db_snapshots", "server_snapshot_serialized_fetch_info", "database_vec")
    SNAPSHOT_SET_ID_FIELD_NUMBER: _ClassVar[int]
    SERVER_SNAPSHOT_INFO_FIELD_NUMBER: _ClassVar[int]
    OWNER_SNAPSHOT_DIR_FULL_PATH_FIELD_NUMBER: _ClassVar[int]
    SERVER_SNAPSHOT_INFO_FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    COMMON_HOST_DIR_NAME_FIELD_NUMBER: _ClassVar[int]
    IS_COMMON_HOST_DIR_CLONED_UNDER_DB_SNAPSHOTS_FIELD_NUMBER: _ClassVar[int]
    SERVER_SNAPSHOT_SERIALIZED_FETCH_INFO_FIELD_NUMBER: _ClassVar[int]
    DATABASE_VEC_FIELD_NUMBER: _ClassVar[int]
    snapshot_set_id: bytes
    server_snapshot_info: _agent_pb2.ServerSnapshotInfo
    owner_snapshot_dir_full_path: str
    server_snapshot_info_file_name: str
    common_host_dir_name: str
    is_common_host_dir_cloned_under_db_snapshots: bool
    server_snapshot_serialized_fetch_info: _agent_pb2.ServerSnapshotSerializedFetchInfo
    database_vec: _containers.RepeatedCompositeFieldContainer[DatabaseRestoreInfo]
    def __init__(self, snapshot_set_id: _Optional[bytes] = ..., server_snapshot_info: _Optional[_Union[_agent_pb2.ServerSnapshotInfo, _Mapping]] = ..., owner_snapshot_dir_full_path: _Optional[str] = ..., server_snapshot_info_file_name: _Optional[str] = ..., common_host_dir_name: _Optional[str] = ..., is_common_host_dir_cloned_under_db_snapshots: bool = ..., server_snapshot_serialized_fetch_info: _Optional[_Union[_agent_pb2.ServerSnapshotSerializedFetchInfo, _Mapping]] = ..., database_vec: _Optional[_Iterable[_Union[DatabaseRestoreInfo, _Mapping]]] = ...) -> None: ...

class RestoreInfo(_message.Message):
    __slots__ = ("vss_database_restore_info", "restore_disks_task_info_proto", "log_replay_info_vec", "mount_point", "whitelist_restore_view_for_all", "exchange_node_restore_info")
    class LogReplayInfo(_message.Message):
        __slots__ = ("view_name", "snapshot_relative_dir_path", "restore_disks_task_info_proto")
        VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
        SNAPSHOT_RELATIVE_DIR_PATH_FIELD_NUMBER: _ClassVar[int]
        RESTORE_DISKS_TASK_INFO_PROTO_FIELD_NUMBER: _ClassVar[int]
        view_name: str
        snapshot_relative_dir_path: str
        restore_disks_task_info_proto: _magneto_pb2.SetupRestoreDiskTaskInfoProto
        def __init__(self, view_name: _Optional[str] = ..., snapshot_relative_dir_path: _Optional[str] = ..., restore_disks_task_info_proto: _Optional[_Union[_magneto_pb2.SetupRestoreDiskTaskInfoProto, _Mapping]] = ...) -> None: ...
    class ExchangeNodeRestoreInfo(_message.Message):
        __slots__ = ("status", "database_vec")
        class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kStarted: _ClassVar[RestoreInfo.ExchangeNodeRestoreInfo.Status]
            kPermitGranted: _ClassVar[RestoreInfo.ExchangeNodeRestoreInfo.Status]
            kDBRecoveryStarted: _ClassVar[RestoreInfo.ExchangeNodeRestoreInfo.Status]
            kDBRecoveryDone: _ClassVar[RestoreInfo.ExchangeNodeRestoreInfo.Status]
            kRestoreDone: _ClassVar[RestoreInfo.ExchangeNodeRestoreInfo.Status]
        kStarted: RestoreInfo.ExchangeNodeRestoreInfo.Status
        kPermitGranted: RestoreInfo.ExchangeNodeRestoreInfo.Status
        kDBRecoveryStarted: RestoreInfo.ExchangeNodeRestoreInfo.Status
        kDBRecoveryDone: RestoreInfo.ExchangeNodeRestoreInfo.Status
        kRestoreDone: RestoreInfo.ExchangeNodeRestoreInfo.Status
        STATUS_FIELD_NUMBER: _ClassVar[int]
        DATABASE_VEC_FIELD_NUMBER: _ClassVar[int]
        status: RestoreInfo.ExchangeNodeRestoreInfo.Status
        database_vec: _containers.RepeatedCompositeFieldContainer[DatabaseRestoreInfo]
        def __init__(self, status: _Optional[_Union[RestoreInfo.ExchangeNodeRestoreInfo.Status, str]] = ..., database_vec: _Optional[_Iterable[_Union[DatabaseRestoreInfo, _Mapping]]] = ...) -> None: ...
    EXCHANGE_RESTORE_INFO_FIELD_NUMBER: _ClassVar[int]
    exchange_restore_info: _descriptor.FieldDescriptor
    VSS_DATABASE_RESTORE_INFO_FIELD_NUMBER: _ClassVar[int]
    RESTORE_DISKS_TASK_INFO_PROTO_FIELD_NUMBER: _ClassVar[int]
    LOG_REPLAY_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    MOUNT_POINT_FIELD_NUMBER: _ClassVar[int]
    WHITELIST_RESTORE_VIEW_FOR_ALL_FIELD_NUMBER: _ClassVar[int]
    EXCHANGE_NODE_RESTORE_INFO_FIELD_NUMBER: _ClassVar[int]
    vss_database_restore_info: VSSDatabaseRestoreInfo
    restore_disks_task_info_proto: _magneto_pb2.SetupRestoreDiskTaskInfoProto
    log_replay_info_vec: _containers.RepeatedCompositeFieldContainer[RestoreInfo.LogReplayInfo]
    mount_point: str
    whitelist_restore_view_for_all: bool
    exchange_node_restore_info: RestoreInfo.ExchangeNodeRestoreInfo
    def __init__(self, vss_database_restore_info: _Optional[_Union[VSSDatabaseRestoreInfo, _Mapping]] = ..., restore_disks_task_info_proto: _Optional[_Union[_magneto_pb2.SetupRestoreDiskTaskInfoProto, _Mapping]] = ..., log_replay_info_vec: _Optional[_Iterable[_Union[RestoreInfo.LogReplayInfo, _Mapping]]] = ..., mount_point: _Optional[str] = ..., whitelist_restore_view_for_all: bool = ..., exchange_node_restore_info: _Optional[_Union[RestoreInfo.ExchangeNodeRestoreInfo, _Mapping]] = ...) -> None: ...

class DestroyTaskInfo(_message.Message):
    __slots__ = ("restore_disks_task_info_proto",)
    EXCHANGE_DESTROY_APP_TASK_INFO_FIELD_NUMBER: _ClassVar[int]
    exchange_destroy_app_task_info: _descriptor.FieldDescriptor
    RESTORE_DISKS_TASK_INFO_PROTO_FIELD_NUMBER: _ClassVar[int]
    restore_disks_task_info_proto: _magneto_pb2.SetupRestoreDiskTaskInfoProto
    def __init__(self, restore_disks_task_info_proto: _Optional[_Union[_magneto_pb2.SetupRestoreDiskTaskInfoProto, _Mapping]] = ...) -> None: ...
