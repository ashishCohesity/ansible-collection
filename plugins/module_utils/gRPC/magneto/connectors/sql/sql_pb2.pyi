from magneto.agents.base import agent_pb2 as _agent_pb2
from magneto.agents.windows.base import file_attrs_pb2 as _file_attrs_pb2
from magneto.base.entities import sql_pb2 as _sql_pb2
from magneto.base import common_pb2 as _common_pb2
from magneto.base import entity_pb2 as _entity_pb2
from magneto.base import error_pb2 as _error_pb2
from magneto.base import magneto_pb2 as _magneto_pb2
from magneto.base import env_params_pb2 as _env_params_pb2
from magneto.base import sub_task_pb2 as _sub_task_pb2
from magneto.connectors.base import common_pb2 as _common_pb2_1
from magneto.connectors.vmware import vmware_setup_restore_disks_pb2 as _vmware_setup_restore_disks_pb2
from magneto.master.stub import stub_pb2 as _stub_pb2
from util.base import universal_id_pb2 as _universal_id_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SQLNativeOperationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kNativeFull: _ClassVar[SQLNativeOperationType]
    kNativeDifferential: _ClassVar[SQLNativeOperationType]
    kNativeLog: _ClassVar[SQLNativeOperationType]
    kNativeTailLog: _ClassVar[SQLNativeOperationType]
kNativeFull: SQLNativeOperationType
kNativeDifferential: SQLNativeOperationType
kNativeLog: SQLNativeOperationType
kNativeTailLog: SQLNativeOperationType

class DBNameProto(_message.Message):
    __slots__ = ("instance_name", "database_name")
    INSTANCE_NAME_FIELD_NUMBER: _ClassVar[int]
    DATABASE_NAME_FIELD_NUMBER: _ClassVar[int]
    instance_name: str
    database_name: str
    def __init__(self, instance_name: _Optional[str] = ..., database_name: _Optional[str] = ...) -> None: ...

class LocalTime(_message.Message):
    __slots__ = ("msecs", "offset_minutes")
    MSECS_FIELD_NUMBER: _ClassVar[int]
    OFFSET_MINUTES_FIELD_NUMBER: _ClassVar[int]
    msecs: int
    offset_minutes: int
    def __init__(self, msecs: _Optional[int] = ..., offset_minutes: _Optional[int] = ...) -> None: ...

class StreamInfoProto(_message.Message):
    __slots__ = ("stream_id", "log_file_relative_path", "state", "num_bytes_processed", "stream_uuid")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kUninitialized: _ClassVar[StreamInfoProto.State]
        kOpen: _ClassVar[StreamInfoProto.State]
        kNoMoreData: _ClassVar[StreamInfoProto.State]
        kClosed: _ClassVar[StreamInfoProto.State]
        kAborted: _ClassVar[StreamInfoProto.State]
    kUninitialized: StreamInfoProto.State
    kOpen: StreamInfoProto.State
    kNoMoreData: StreamInfoProto.State
    kClosed: StreamInfoProto.State
    kAborted: StreamInfoProto.State
    STREAM_ID_FIELD_NUMBER: _ClassVar[int]
    LOG_FILE_RELATIVE_PATH_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    NUM_BYTES_PROCESSED_FIELD_NUMBER: _ClassVar[int]
    STREAM_UUID_FIELD_NUMBER: _ClassVar[int]
    stream_id: int
    log_file_relative_path: str
    state: StreamInfoProto.State
    num_bytes_processed: int
    stream_uuid: str
    def __init__(self, stream_id: _Optional[int] = ..., log_file_relative_path: _Optional[str] = ..., state: _Optional[_Union[StreamInfoProto.State, str]] = ..., num_bytes_processed: _Optional[int] = ..., stream_uuid: _Optional[str] = ...) -> None: ...

class NativeBackupInfo(_message.Message):
    __slots__ = ("num_streams", "backup_file_path_vec", "state", "uuid", "backup_type", "base_backup_run_start_time_usecs", "base_backup_run_job_uid", "db_snap_fs_base_backup_dir_name", "base_backup_file_path_vec", "base_backup_file_vec", "base_backup_size", "base_compressed_backup_size", "base_backupset_uuid", "with_clause")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kUninitialized: _ClassVar[NativeBackupInfo.State]
        kStarted: _ClassVar[NativeBackupInfo.State]
        kBackupDone: _ClassVar[NativeBackupInfo.State]
        kNotifyComplete: _ClassVar[NativeBackupInfo.State]
    kUninitialized: NativeBackupInfo.State
    kStarted: NativeBackupInfo.State
    kBackupDone: NativeBackupInfo.State
    kNotifyComplete: NativeBackupInfo.State
    NUM_STREAMS_FIELD_NUMBER: _ClassVar[int]
    BACKUP_FILE_PATH_VEC_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    BACKUP_TYPE_FIELD_NUMBER: _ClassVar[int]
    BASE_BACKUP_RUN_START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    BASE_BACKUP_RUN_JOB_UID_FIELD_NUMBER: _ClassVar[int]
    DB_SNAP_FS_BASE_BACKUP_DIR_NAME_FIELD_NUMBER: _ClassVar[int]
    BASE_BACKUP_FILE_PATH_VEC_FIELD_NUMBER: _ClassVar[int]
    BASE_BACKUP_FILE_VEC_FIELD_NUMBER: _ClassVar[int]
    BASE_BACKUP_SIZE_FIELD_NUMBER: _ClassVar[int]
    BASE_COMPRESSED_BACKUP_SIZE_FIELD_NUMBER: _ClassVar[int]
    BASE_BACKUPSET_UUID_FIELD_NUMBER: _ClassVar[int]
    WITH_CLAUSE_FIELD_NUMBER: _ClassVar[int]
    num_streams: int
    backup_file_path_vec: _containers.RepeatedScalarFieldContainer[str]
    state: NativeBackupInfo.State
    uuid: str
    backup_type: SQLNativeOperationType
    base_backup_run_start_time_usecs: int
    base_backup_run_job_uid: _universal_id_pb2.UniversalIdProto
    db_snap_fs_base_backup_dir_name: str
    base_backup_file_path_vec: _containers.RepeatedScalarFieldContainer[str]
    base_backup_file_vec: _containers.RepeatedCompositeFieldContainer[_sql_pb2.FileInfo]
    base_backup_size: int
    base_compressed_backup_size: int
    base_backupset_uuid: str
    with_clause: str
    def __init__(self, num_streams: _Optional[int] = ..., backup_file_path_vec: _Optional[_Iterable[str]] = ..., state: _Optional[_Union[NativeBackupInfo.State, str]] = ..., uuid: _Optional[str] = ..., backup_type: _Optional[_Union[SQLNativeOperationType, str]] = ..., base_backup_run_start_time_usecs: _Optional[int] = ..., base_backup_run_job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., db_snap_fs_base_backup_dir_name: _Optional[str] = ..., base_backup_file_path_vec: _Optional[_Iterable[str]] = ..., base_backup_file_vec: _Optional[_Iterable[_Union[_sql_pb2.FileInfo, _Mapping]]] = ..., base_backup_size: _Optional[int] = ..., base_compressed_backup_size: _Optional[int] = ..., base_backupset_uuid: _Optional[str] = ..., with_clause: _Optional[str] = ...) -> None: ...

class LSNInfo(_message.Message):
    __slots__ = ("first_lsn", "last_lsn", "database_backup_lsn", "checkpoint_lsn", "fork_point_lsn")
    FIRST_LSN_FIELD_NUMBER: _ClassVar[int]
    LAST_LSN_FIELD_NUMBER: _ClassVar[int]
    DATABASE_BACKUP_LSN_FIELD_NUMBER: _ClassVar[int]
    CHECKPOINT_LSN_FIELD_NUMBER: _ClassVar[int]
    FORK_POINT_LSN_FIELD_NUMBER: _ClassVar[int]
    first_lsn: str
    last_lsn: str
    database_backup_lsn: str
    checkpoint_lsn: str
    fork_point_lsn: str
    def __init__(self, first_lsn: _Optional[str] = ..., last_lsn: _Optional[str] = ..., database_backup_lsn: _Optional[str] = ..., checkpoint_lsn: _Optional[str] = ..., fork_point_lsn: _Optional[str] = ...) -> None: ...

class DatabaseRecoveryStatus(_message.Message):
    __slots__ = ("last_log_backup_lsn", "recovery_fork_guid", "first_recovery_fork_guid", "fork_point_lsn")
    LAST_LOG_BACKUP_LSN_FIELD_NUMBER: _ClassVar[int]
    RECOVERY_FORK_GUID_FIELD_NUMBER: _ClassVar[int]
    FIRST_RECOVERY_FORK_GUID_FIELD_NUMBER: _ClassVar[int]
    FORK_POINT_LSN_FIELD_NUMBER: _ClassVar[int]
    last_log_backup_lsn: str
    recovery_fork_guid: str
    first_recovery_fork_guid: str
    fork_point_lsn: str
    def __init__(self, last_log_backup_lsn: _Optional[str] = ..., recovery_fork_guid: _Optional[str] = ..., first_recovery_fork_guid: _Optional[str] = ..., fork_point_lsn: _Optional[str] = ...) -> None: ...

class BackupSetRowInfo(_message.Message):
    __slots__ = ("backup_set_id", "backup_set_uuid", "backup_start_date", "backup_finish_date", "lsn_info", "first_recovery_fork_guid", "last_recovery_fork_guid", "is_post_backup", "backup_size", "user_name", "name", "is_copy_only", "compressed_backup_size", "base_backupset_uuid")
    BACKUP_SET_ID_FIELD_NUMBER: _ClassVar[int]
    BACKUP_SET_UUID_FIELD_NUMBER: _ClassVar[int]
    BACKUP_START_DATE_FIELD_NUMBER: _ClassVar[int]
    BACKUP_FINISH_DATE_FIELD_NUMBER: _ClassVar[int]
    LSN_INFO_FIELD_NUMBER: _ClassVar[int]
    FIRST_RECOVERY_FORK_GUID_FIELD_NUMBER: _ClassVar[int]
    LAST_RECOVERY_FORK_GUID_FIELD_NUMBER: _ClassVar[int]
    IS_POST_BACKUP_FIELD_NUMBER: _ClassVar[int]
    BACKUP_SIZE_FIELD_NUMBER: _ClassVar[int]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    IS_COPY_ONLY_FIELD_NUMBER: _ClassVar[int]
    COMPRESSED_BACKUP_SIZE_FIELD_NUMBER: _ClassVar[int]
    BASE_BACKUPSET_UUID_FIELD_NUMBER: _ClassVar[int]
    backup_set_id: int
    backup_set_uuid: bytes
    backup_start_date: LocalTime
    backup_finish_date: LocalTime
    lsn_info: LSNInfo
    first_recovery_fork_guid: bytes
    last_recovery_fork_guid: bytes
    is_post_backup: bool
    backup_size: int
    user_name: bytes
    name: bytes
    is_copy_only: bytes
    compressed_backup_size: int
    base_backupset_uuid: bytes
    def __init__(self, backup_set_id: _Optional[int] = ..., backup_set_uuid: _Optional[bytes] = ..., backup_start_date: _Optional[_Union[LocalTime, _Mapping]] = ..., backup_finish_date: _Optional[_Union[LocalTime, _Mapping]] = ..., lsn_info: _Optional[_Union[LSNInfo, _Mapping]] = ..., first_recovery_fork_guid: _Optional[bytes] = ..., last_recovery_fork_guid: _Optional[bytes] = ..., is_post_backup: bool = ..., backup_size: _Optional[int] = ..., user_name: _Optional[bytes] = ..., name: _Optional[bytes] = ..., is_copy_only: _Optional[bytes] = ..., compressed_backup_size: _Optional[int] = ..., base_backupset_uuid: _Optional[bytes] = ...) -> None: ...

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
    __slots__ = ("sql_id", "instance_name", "database_name", "sql_server_db_state", "is_user_scheduled", "is_available_for_vss_backup", "skipped", "skip_reason", "stream_info", "previous_task_id", "previous_full_backup_task_id", "backupset_row_info", "recovery_model", "compatibility_level_vec", "ldf_size_bytes", "backup_size_exponential_moving_average", "total_size_bytes", "error", "warning", "create_date", "vss_snapshot_db_file_info_vec", "vss_file_prev_snapshot_info", "sub_file_size_mb", "is_vdi_snapshot_based_vss_backup", "start_time_usecs", "end_time_usecs", "backup_finished_successfully", "batch_num", "database_recovery_status", "database_owner", "file_group_info_vec", "compatibility_level", "file_vec", "prev_log_backup_error", "native_backup_info", "db_snap_fs_backup_dir_name", "read_only", "is_database_cloned", "is_fci_database", "has_files_on_external_storage", "is_excluded", "usage_size_bytes", "is_encrypted", "index", "selected_sql_id_for_backup", "retry_attempt_for_incomplete_log_backup", "aag_group_id", "group_database_id")
    SQL_ID_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_NAME_FIELD_NUMBER: _ClassVar[int]
    DATABASE_NAME_FIELD_NUMBER: _ClassVar[int]
    SQL_SERVER_DB_STATE_FIELD_NUMBER: _ClassVar[int]
    IS_USER_SCHEDULED_FIELD_NUMBER: _ClassVar[int]
    IS_AVAILABLE_FOR_VSS_BACKUP_FIELD_NUMBER: _ClassVar[int]
    SKIPPED_FIELD_NUMBER: _ClassVar[int]
    SKIP_REASON_FIELD_NUMBER: _ClassVar[int]
    STREAM_INFO_FIELD_NUMBER: _ClassVar[int]
    PREVIOUS_TASK_ID_FIELD_NUMBER: _ClassVar[int]
    PREVIOUS_FULL_BACKUP_TASK_ID_FIELD_NUMBER: _ClassVar[int]
    BACKUPSET_ROW_INFO_FIELD_NUMBER: _ClassVar[int]
    RECOVERY_MODEL_FIELD_NUMBER: _ClassVar[int]
    COMPATIBILITY_LEVEL_VEC_FIELD_NUMBER: _ClassVar[int]
    LDF_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    BACKUP_SIZE_EXPONENTIAL_MOVING_AVERAGE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    WARNING_FIELD_NUMBER: _ClassVar[int]
    CREATE_DATE_FIELD_NUMBER: _ClassVar[int]
    VSS_SNAPSHOT_DB_FILE_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    VSS_FILE_PREV_SNAPSHOT_INFO_FIELD_NUMBER: _ClassVar[int]
    SUB_FILE_SIZE_MB_FIELD_NUMBER: _ClassVar[int]
    IS_VDI_SNAPSHOT_BASED_VSS_BACKUP_FIELD_NUMBER: _ClassVar[int]
    START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    END_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    BACKUP_FINISHED_SUCCESSFULLY_FIELD_NUMBER: _ClassVar[int]
    BATCH_NUM_FIELD_NUMBER: _ClassVar[int]
    DATABASE_RECOVERY_STATUS_FIELD_NUMBER: _ClassVar[int]
    DATABASE_OWNER_FIELD_NUMBER: _ClassVar[int]
    FILE_GROUP_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    COMPATIBILITY_LEVEL_FIELD_NUMBER: _ClassVar[int]
    FILE_VEC_FIELD_NUMBER: _ClassVar[int]
    PREV_LOG_BACKUP_ERROR_FIELD_NUMBER: _ClassVar[int]
    NATIVE_BACKUP_INFO_FIELD_NUMBER: _ClassVar[int]
    DB_SNAP_FS_BACKUP_DIR_NAME_FIELD_NUMBER: _ClassVar[int]
    READ_ONLY_FIELD_NUMBER: _ClassVar[int]
    IS_DATABASE_CLONED_FIELD_NUMBER: _ClassVar[int]
    IS_FCI_DATABASE_FIELD_NUMBER: _ClassVar[int]
    HAS_FILES_ON_EXTERNAL_STORAGE_FIELD_NUMBER: _ClassVar[int]
    IS_EXCLUDED_FIELD_NUMBER: _ClassVar[int]
    USAGE_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    IS_ENCRYPTED_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    SELECTED_SQL_ID_FOR_BACKUP_FIELD_NUMBER: _ClassVar[int]
    RETRY_ATTEMPT_FOR_INCOMPLETE_LOG_BACKUP_FIELD_NUMBER: _ClassVar[int]
    AAG_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    GROUP_DATABASE_ID_FIELD_NUMBER: _ClassVar[int]
    sql_id: _sql_pb2.SqlId
    instance_name: str
    database_name: str
    sql_server_db_state: _sql_pb2.SQLDatabaseState.Type
    is_user_scheduled: bool
    is_available_for_vss_backup: bool
    skipped: bool
    skip_reason: str
    stream_info: StreamInfoProto
    previous_task_id: int
    previous_full_backup_task_id: int
    backupset_row_info: BackupSetRowInfo
    recovery_model: _sql_pb2.RecoveryModel.Type
    compatibility_level_vec: _containers.RepeatedScalarFieldContainer[int]
    ldf_size_bytes: int
    backup_size_exponential_moving_average: int
    total_size_bytes: int
    error: _error_pb2.ErrorProto
    warning: _error_pb2.ErrorProto
    create_date: str
    vss_snapshot_db_file_info_vec: _containers.RepeatedCompositeFieldContainer[_common_pb2_1.VSSSnapshotDbFileInfo]
    vss_file_prev_snapshot_info: VSSFileDbPreviousSnapshotInfo
    sub_file_size_mb: int
    is_vdi_snapshot_based_vss_backup: bool
    start_time_usecs: int
    end_time_usecs: int
    backup_finished_successfully: bool
    batch_num: int
    database_recovery_status: DatabaseRecoveryStatus
    database_owner: str
    file_group_info_vec: _containers.RepeatedCompositeFieldContainer[_sql_pb2.SQLDatabaseFileGroupInfo]
    compatibility_level: int
    file_vec: _containers.RepeatedCompositeFieldContainer[_sql_pb2.FileInfo]
    prev_log_backup_error: _error_pb2.ErrorProto
    native_backup_info: NativeBackupInfo
    db_snap_fs_backup_dir_name: str
    read_only: bool
    is_database_cloned: bool
    is_fci_database: bool
    has_files_on_external_storage: bool
    is_excluded: bool
    usage_size_bytes: int
    is_encrypted: bool
    index: int
    selected_sql_id_for_backup: _sql_pb2.SqlId
    retry_attempt_for_incomplete_log_backup: int
    aag_group_id: str
    group_database_id: str
    def __init__(self, sql_id: _Optional[_Union[_sql_pb2.SqlId, _Mapping]] = ..., instance_name: _Optional[str] = ..., database_name: _Optional[str] = ..., sql_server_db_state: _Optional[_Union[_sql_pb2.SQLDatabaseState.Type, str]] = ..., is_user_scheduled: bool = ..., is_available_for_vss_backup: bool = ..., skipped: bool = ..., skip_reason: _Optional[str] = ..., stream_info: _Optional[_Union[StreamInfoProto, _Mapping]] = ..., previous_task_id: _Optional[int] = ..., previous_full_backup_task_id: _Optional[int] = ..., backupset_row_info: _Optional[_Union[BackupSetRowInfo, _Mapping]] = ..., recovery_model: _Optional[_Union[_sql_pb2.RecoveryModel.Type, str]] = ..., compatibility_level_vec: _Optional[_Iterable[int]] = ..., ldf_size_bytes: _Optional[int] = ..., backup_size_exponential_moving_average: _Optional[int] = ..., total_size_bytes: _Optional[int] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., warning: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., create_date: _Optional[str] = ..., vss_snapshot_db_file_info_vec: _Optional[_Iterable[_Union[_common_pb2_1.VSSSnapshotDbFileInfo, _Mapping]]] = ..., vss_file_prev_snapshot_info: _Optional[_Union[VSSFileDbPreviousSnapshotInfo, _Mapping]] = ..., sub_file_size_mb: _Optional[int] = ..., is_vdi_snapshot_based_vss_backup: bool = ..., start_time_usecs: _Optional[int] = ..., end_time_usecs: _Optional[int] = ..., backup_finished_successfully: bool = ..., batch_num: _Optional[int] = ..., database_recovery_status: _Optional[_Union[DatabaseRecoveryStatus, _Mapping]] = ..., database_owner: _Optional[str] = ..., file_group_info_vec: _Optional[_Iterable[_Union[_sql_pb2.SQLDatabaseFileGroupInfo, _Mapping]]] = ..., compatibility_level: _Optional[int] = ..., file_vec: _Optional[_Iterable[_Union[_sql_pb2.FileInfo, _Mapping]]] = ..., prev_log_backup_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., native_backup_info: _Optional[_Union[NativeBackupInfo, _Mapping]] = ..., db_snap_fs_backup_dir_name: _Optional[str] = ..., read_only: bool = ..., is_database_cloned: bool = ..., is_fci_database: bool = ..., has_files_on_external_storage: bool = ..., is_excluded: bool = ..., usage_size_bytes: _Optional[int] = ..., is_encrypted: bool = ..., index: _Optional[int] = ..., selected_sql_id_for_backup: _Optional[_Union[_sql_pb2.SqlId, _Mapping]] = ..., retry_attempt_for_incomplete_log_backup: _Optional[int] = ..., aag_group_id: _Optional[str] = ..., group_database_id: _Optional[str] = ...) -> None: ...

class ExtendedDatabaseBackupInfo(_message.Message):
    __slots__ = ("sql_id", "file_vec")
    SQL_ID_FIELD_NUMBER: _ClassVar[int]
    FILE_VEC_FIELD_NUMBER: _ClassVar[int]
    sql_id: _sql_pb2.SqlId
    file_vec: _containers.RepeatedCompositeFieldContainer[_sql_pb2.FileInfo]
    def __init__(self, sql_id: _Optional[_Union[_sql_pb2.SqlId, _Mapping]] = ..., file_vec: _Optional[_Iterable[_Union[_sql_pb2.FileInfo, _Mapping]]] = ...) -> None: ...

class AAGBackupInfo(_message.Message):
    __slots__ = ("aag_entity_proto", "backup_replica", "warnings", "error")
    AAG_ENTITY_PROTO_FIELD_NUMBER: _ClassVar[int]
    BACKUP_REPLICA_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    aag_entity_proto: _entity_pb2.EntityProto
    backup_replica: _sql_pb2.AAGReplicaInfo
    warnings: _containers.RepeatedScalarFieldContainer[str]
    error: _error_pb2.ErrorProto
    def __init__(self, aag_entity_proto: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., backup_replica: _Optional[_Union[_sql_pb2.AAGReplicaInfo, _Mapping]] = ..., warnings: _Optional[_Iterable[str]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class UpdateSqlLogBackupTaskResult(_message.Message):
    __slots__ = ("databases_with_logchain_holes", "databases_to_skip_for_logchain_holes", "databases_with_aag_relationship_error")
    class AAGRelationshipErrorInfo(_message.Message):
        __slots__ = ("sql_id", "error_message")
        SQL_ID_FIELD_NUMBER: _ClassVar[int]
        ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
        sql_id: _sql_pb2.SqlId
        error_message: str
        def __init__(self, sql_id: _Optional[_Union[_sql_pb2.SqlId, _Mapping]] = ..., error_message: _Optional[str] = ...) -> None: ...
    UPDATE_SQL_LOG_BACKUP_TASK_RESULT_FIELD_NUMBER: _ClassVar[int]
    update_sql_log_backup_task_result: _descriptor.FieldDescriptor
    DATABASES_WITH_LOGCHAIN_HOLES_FIELD_NUMBER: _ClassVar[int]
    DATABASES_TO_SKIP_FOR_LOGCHAIN_HOLES_FIELD_NUMBER: _ClassVar[int]
    DATABASES_WITH_AAG_RELATIONSHIP_ERROR_FIELD_NUMBER: _ClassVar[int]
    databases_with_logchain_holes: _containers.RepeatedCompositeFieldContainer[_sql_pb2.SqlId]
    databases_to_skip_for_logchain_holes: _containers.RepeatedCompositeFieldContainer[_sql_pb2.SqlId]
    databases_with_aag_relationship_error: _containers.RepeatedCompositeFieldContainer[UpdateSqlLogBackupTaskResult.AAGRelationshipErrorInfo]
    def __init__(self, databases_with_logchain_holes: _Optional[_Iterable[_Union[_sql_pb2.SqlId, _Mapping]]] = ..., databases_to_skip_for_logchain_holes: _Optional[_Iterable[_Union[_sql_pb2.SqlId, _Mapping]]] = ..., databases_with_aag_relationship_error: _Optional[_Iterable[_Union[UpdateSqlLogBackupTaskResult.AAGRelationshipErrorInfo, _Mapping]]] = ...) -> None: ...

class UpdateSqlDbLevelBackupTaskResult(_message.Message):
    __slots__ = ("databases_with_locking_conflicts", "databases_with_differential_base")
    class DifferentialBaseInfo(_message.Message):
        __slots__ = ("sql_id", "run_start_time_usecs", "job_uid", "backup_dir", "backup_file_path_vec", "backup_file_vec", "backup_size", "compressed_backup_size", "base_backupset_uuid")
        SQL_ID_FIELD_NUMBER: _ClassVar[int]
        RUN_START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
        JOB_UID_FIELD_NUMBER: _ClassVar[int]
        BACKUP_DIR_FIELD_NUMBER: _ClassVar[int]
        BACKUP_FILE_PATH_VEC_FIELD_NUMBER: _ClassVar[int]
        BACKUP_FILE_VEC_FIELD_NUMBER: _ClassVar[int]
        BACKUP_SIZE_FIELD_NUMBER: _ClassVar[int]
        COMPRESSED_BACKUP_SIZE_FIELD_NUMBER: _ClassVar[int]
        BASE_BACKUPSET_UUID_FIELD_NUMBER: _ClassVar[int]
        sql_id: _sql_pb2.SqlId
        run_start_time_usecs: int
        job_uid: _universal_id_pb2.UniversalIdProto
        backup_dir: str
        backup_file_path_vec: _containers.RepeatedScalarFieldContainer[str]
        backup_file_vec: _containers.RepeatedCompositeFieldContainer[_sql_pb2.FileInfo]
        backup_size: int
        compressed_backup_size: int
        base_backupset_uuid: str
        def __init__(self, sql_id: _Optional[_Union[_sql_pb2.SqlId, _Mapping]] = ..., run_start_time_usecs: _Optional[int] = ..., job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., backup_dir: _Optional[str] = ..., backup_file_path_vec: _Optional[_Iterable[str]] = ..., backup_file_vec: _Optional[_Iterable[_Union[_sql_pb2.FileInfo, _Mapping]]] = ..., backup_size: _Optional[int] = ..., compressed_backup_size: _Optional[int] = ..., base_backupset_uuid: _Optional[str] = ...) -> None: ...
    UPDATE_SQL_DB_LEVEL_BACKUP_TASK_RESULT_FIELD_NUMBER: _ClassVar[int]
    update_sql_db_level_backup_task_result: _descriptor.FieldDescriptor
    DATABASES_WITH_LOCKING_CONFLICTS_FIELD_NUMBER: _ClassVar[int]
    DATABASES_WITH_DIFFERENTIAL_BASE_FIELD_NUMBER: _ClassVar[int]
    databases_with_locking_conflicts: _containers.RepeatedCompositeFieldContainer[_sql_pb2.SqlId]
    databases_with_differential_base: _containers.RepeatedCompositeFieldContainer[UpdateSqlDbLevelBackupTaskResult.DifferentialBaseInfo]
    def __init__(self, databases_with_locking_conflicts: _Optional[_Iterable[_Union[_sql_pb2.SqlId, _Mapping]]] = ..., databases_with_differential_base: _Optional[_Iterable[_Union[UpdateSqlDbLevelBackupTaskResult.DifferentialBaseInfo, _Mapping]]] = ...) -> None: ...

class SnapshotInfo(_message.Message):
    __slots__ = ("database_backup_info_vec", "aag_info_vec", "snapshot_set_id", "is_tail_log_backup", "status", "sub_task_status", "error", "warnings", "query_sql_warning", "db_mismatch_warning", "query_sql_info", "agent_info", "aag_backup_info_vec", "sub_task_vec", "instances_to_backup_vec", "discover_dbs_done", "sql_instance_vec", "current_batch_num", "pending_log_backup_prev_snapshot_dir", "advanced_settings", "use_task_progress_monitor_for_db_progress")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kCreated: _ClassVar[SnapshotInfo.Status]
        kBackup: _ClassVar[SnapshotInfo.Status]
        kDone: _ClassVar[SnapshotInfo.Status]
    kCreated: SnapshotInfo.Status
    kBackup: SnapshotInfo.Status
    kDone: SnapshotInfo.Status
    class SubTaskStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kSubTasksCreated: _ClassVar[SnapshotInfo.SubTaskStatus]
        kSubTasksFinished: _ClassVar[SnapshotInfo.SubTaskStatus]
    kSubTasksCreated: SnapshotInfo.SubTaskStatus
    kSubTasksFinished: SnapshotInfo.SubTaskStatus
    SQL_SNAPSHOT_INFO_FIELD_NUMBER: _ClassVar[int]
    sql_snapshot_info: _descriptor.FieldDescriptor
    DATABASE_BACKUP_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    AAG_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_SET_ID_FIELD_NUMBER: _ClassVar[int]
    IS_TAIL_LOG_BACKUP_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SUB_TASK_STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    QUERY_SQL_WARNING_FIELD_NUMBER: _ClassVar[int]
    DB_MISMATCH_WARNING_FIELD_NUMBER: _ClassVar[int]
    QUERY_SQL_INFO_FIELD_NUMBER: _ClassVar[int]
    AGENT_INFO_FIELD_NUMBER: _ClassVar[int]
    AAG_BACKUP_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    SUB_TASK_VEC_FIELD_NUMBER: _ClassVar[int]
    INSTANCES_TO_BACKUP_VEC_FIELD_NUMBER: _ClassVar[int]
    DISCOVER_DBS_DONE_FIELD_NUMBER: _ClassVar[int]
    SQL_INSTANCE_VEC_FIELD_NUMBER: _ClassVar[int]
    CURRENT_BATCH_NUM_FIELD_NUMBER: _ClassVar[int]
    PENDING_LOG_BACKUP_PREV_SNAPSHOT_DIR_FIELD_NUMBER: _ClassVar[int]
    ADVANCED_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    USE_TASK_PROGRESS_MONITOR_FOR_DB_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    database_backup_info_vec: _containers.RepeatedCompositeFieldContainer[DatabaseBackupInfo]
    aag_info_vec: _containers.RepeatedCompositeFieldContainer[_sql_pb2.AAGInfo]
    snapshot_set_id: bytes
    is_tail_log_backup: bool
    status: SnapshotInfo.Status
    sub_task_status: SnapshotInfo.SubTaskStatus
    error: _error_pb2.ErrorProto
    warnings: _containers.RepeatedCompositeFieldContainer[_error_pb2.ErrorProto]
    query_sql_warning: _error_pb2.ErrorProto
    db_mismatch_warning: _error_pb2.ErrorProto
    query_sql_info: str
    agent_info: _agent_pb2.AgentInfoProto
    aag_backup_info_vec: _containers.RepeatedCompositeFieldContainer[AAGBackupInfo]
    sub_task_vec: _containers.RepeatedCompositeFieldContainer[_sub_task_pb2.SubTaskInfo]
    instances_to_backup_vec: _containers.RepeatedCompositeFieldContainer[_sql_pb2.SqlId]
    discover_dbs_done: bool
    sql_instance_vec: _containers.RepeatedCompositeFieldContainer[_sql_pb2.SQLInstanceInfo]
    current_batch_num: int
    pending_log_backup_prev_snapshot_dir: str
    advanced_settings: _sql_pb2.AdvancedSettings
    use_task_progress_monitor_for_db_progress: bool
    def __init__(self, database_backup_info_vec: _Optional[_Iterable[_Union[DatabaseBackupInfo, _Mapping]]] = ..., aag_info_vec: _Optional[_Iterable[_Union[_sql_pb2.AAGInfo, _Mapping]]] = ..., snapshot_set_id: _Optional[bytes] = ..., is_tail_log_backup: bool = ..., status: _Optional[_Union[SnapshotInfo.Status, str]] = ..., sub_task_status: _Optional[_Union[SnapshotInfo.SubTaskStatus, str]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., warnings: _Optional[_Iterable[_Union[_error_pb2.ErrorProto, _Mapping]]] = ..., query_sql_warning: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., db_mismatch_warning: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., query_sql_info: _Optional[str] = ..., agent_info: _Optional[_Union[_agent_pb2.AgentInfoProto, _Mapping]] = ..., aag_backup_info_vec: _Optional[_Iterable[_Union[AAGBackupInfo, _Mapping]]] = ..., sub_task_vec: _Optional[_Iterable[_Union[_sub_task_pb2.SubTaskInfo, _Mapping]]] = ..., instances_to_backup_vec: _Optional[_Iterable[_Union[_sql_pb2.SqlId, _Mapping]]] = ..., discover_dbs_done: bool = ..., sql_instance_vec: _Optional[_Iterable[_Union[_sql_pb2.SQLInstanceInfo, _Mapping]]] = ..., current_batch_num: _Optional[int] = ..., pending_log_backup_prev_snapshot_dir: _Optional[str] = ..., advanced_settings: _Optional[_Union[_sql_pb2.AdvancedSettings, _Mapping]] = ..., use_task_progress_monitor_for_db_progress: bool = ...) -> None: ...

class SnapshotDelta(_message.Message):
    __slots__ = ("delta_database_backup_info_vec",)
    SQL_SNAPSHOT_DELTA_FIELD_NUMBER: _ClassVar[int]
    sql_snapshot_delta: _descriptor.FieldDescriptor
    DELTA_DATABASE_BACKUP_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    delta_database_backup_info_vec: _containers.RepeatedCompositeFieldContainer[DatabaseBackupInfo]
    def __init__(self, delta_database_backup_info_vec: _Optional[_Iterable[_Union[DatabaseBackupInfo, _Mapping]]] = ...) -> None: ...

class SqlSubTaskInfo(_message.Message):
    __slots__ = ("db_info_vec", "bridge_node_vip_vec")
    class DbInfo(_message.Message):
        __slots__ = ("snapshot_db_index",)
        SNAPSHOT_DB_INDEX_FIELD_NUMBER: _ClassVar[int]
        snapshot_db_index: int
        def __init__(self, snapshot_db_index: _Optional[int] = ...) -> None: ...
    SQL_SUB_TASK_INFO_FIELD_NUMBER: _ClassVar[int]
    sql_sub_task_info: _descriptor.FieldDescriptor
    DB_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    BRIDGE_NODE_VIP_VEC_FIELD_NUMBER: _ClassVar[int]
    db_info_vec: _containers.RepeatedCompositeFieldContainer[SqlSubTaskInfo.DbInfo]
    bridge_node_vip_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, db_info_vec: _Optional[_Iterable[_Union[SqlSubTaskInfo.DbInfo, _Mapping]]] = ..., bridge_node_vip_vec: _Optional[_Iterable[str]] = ...) -> None: ...

class LogBackupSubTaskScribeInfo(_message.Message):
    __slots__ = ("db_info_map",)
    class DbInfo(_message.Message):
        __slots__ = ("stream_info", "backupset_row_info", "error", "backup_finished_successfully", "end_time_usecs", "start_time_usecs")
        STREAM_INFO_FIELD_NUMBER: _ClassVar[int]
        BACKUPSET_ROW_INFO_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        BACKUP_FINISHED_SUCCESSFULLY_FIELD_NUMBER: _ClassVar[int]
        END_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
        START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
        stream_info: StreamInfoProto
        backupset_row_info: BackupSetRowInfo
        error: _error_pb2.ErrorProto
        backup_finished_successfully: bool
        end_time_usecs: int
        start_time_usecs: int
        def __init__(self, stream_info: _Optional[_Union[StreamInfoProto, _Mapping]] = ..., backupset_row_info: _Optional[_Union[BackupSetRowInfo, _Mapping]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., backup_finished_successfully: bool = ..., end_time_usecs: _Optional[int] = ..., start_time_usecs: _Optional[int] = ...) -> None: ...
    class DbInfoMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: LogBackupSubTaskScribeInfo.DbInfo
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[LogBackupSubTaskScribeInfo.DbInfo, _Mapping]] = ...) -> None: ...
    LOG_BACKUP_SUB_TASK_SCRIBE_INFO_FIELD_NUMBER: _ClassVar[int]
    log_backup_sub_task_scribe_info: _descriptor.FieldDescriptor
    DB_INFO_MAP_FIELD_NUMBER: _ClassVar[int]
    db_info_map: _containers.MessageMap[int, LogBackupSubTaskScribeInfo.DbInfo]
    def __init__(self, db_info_map: _Optional[_Mapping[int, LogBackupSubTaskScribeInfo.DbInfo]] = ...) -> None: ...

class VerificationInfo(_message.Message):
    __slots__ = ("database_backup_info_vec", "aag_info_vec", "query_sql_warning", "query_sql_info", "host_summary", "instance_info_vec")
    SQL_VERIFICATION_INFO_FIELD_NUMBER: _ClassVar[int]
    sql_verification_info: _descriptor.FieldDescriptor
    DATABASE_BACKUP_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    AAG_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    QUERY_SQL_WARNING_FIELD_NUMBER: _ClassVar[int]
    QUERY_SQL_INFO_FIELD_NUMBER: _ClassVar[int]
    HOST_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    database_backup_info_vec: _containers.RepeatedCompositeFieldContainer[DatabaseBackupInfo]
    aag_info_vec: _containers.RepeatedCompositeFieldContainer[_sql_pb2.AAGInfo]
    query_sql_warning: _error_pb2.ErrorProto
    query_sql_info: str
    host_summary: _agent_pb2.HostInfoSummary
    instance_info_vec: _containers.RepeatedCompositeFieldContainer[_sql_pb2.SQLInstanceInfo]
    def __init__(self, database_backup_info_vec: _Optional[_Iterable[_Union[DatabaseBackupInfo, _Mapping]]] = ..., aag_info_vec: _Optional[_Iterable[_Union[_sql_pb2.AAGInfo, _Mapping]]] = ..., query_sql_warning: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., query_sql_info: _Optional[str] = ..., host_summary: _Optional[_Union[_agent_pb2.HostInfoSummary, _Mapping]] = ..., instance_info_vec: _Optional[_Iterable[_Union[_sql_pb2.SQLInstanceInfo, _Mapping]]] = ...) -> None: ...

class AttachedDbInfo(_message.Message):
    __slots__ = ("sql_id", "original_sql_id", "cloned_db_name", "detached_successfully", "error")
    SQL_ID_FIELD_NUMBER: _ClassVar[int]
    ORIGINAL_SQL_ID_FIELD_NUMBER: _ClassVar[int]
    CLONED_DB_NAME_FIELD_NUMBER: _ClassVar[int]
    DETACHED_SUCCESSFULLY_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    sql_id: _sql_pb2.SqlId
    original_sql_id: _sql_pb2.SqlId
    cloned_db_name: DBNameProto
    detached_successfully: bool
    error: _error_pb2.ErrorProto
    def __init__(self, sql_id: _Optional[_Union[_sql_pb2.SqlId, _Mapping]] = ..., original_sql_id: _Optional[_Union[_sql_pb2.SqlId, _Mapping]] = ..., cloned_db_name: _Optional[_Union[DBNameProto, _Mapping]] = ..., detached_successfully: bool = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class ParallelRestoreStateInfo(_message.Message):
    __slots__ = ("status", "snapfs_path_to_target_file_dir_map", "error")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNotStarted: _ClassVar[ParallelRestoreStateInfo.Status]
        kPreDataCopyDone: _ClassVar[ParallelRestoreStateInfo.Status]
        kDataCopyDone: _ClassVar[ParallelRestoreStateInfo.Status]
        kPostDataCopyDone: _ClassVar[ParallelRestoreStateInfo.Status]
    kNotStarted: ParallelRestoreStateInfo.Status
    kPreDataCopyDone: ParallelRestoreStateInfo.Status
    kDataCopyDone: ParallelRestoreStateInfo.Status
    kPostDataCopyDone: ParallelRestoreStateInfo.Status
    class SnapfsPathToTargetFileDirMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SNAPFS_PATH_TO_TARGET_FILE_DIR_MAP_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    status: ParallelRestoreStateInfo.Status
    snapfs_path_to_target_file_dir_map: _containers.ScalarMap[str, str]
    error: _error_pb2.ErrorProto
    def __init__(self, status: _Optional[_Union[ParallelRestoreStateInfo.Status, str]] = ..., snapfs_path_to_target_file_dir_map: _Optional[_Mapping[str, str]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class MultiStageRestoreInfo(_message.Message):
    __slots__ = ("action", "perform_data_sync", "perform_finalize", "state")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kMultiStageNone: _ClassVar[MultiStageRestoreInfo.State]
        kMetadataSyncDone: _ClassVar[MultiStageRestoreInfo.State]
        kApplyChangesAreasDone: _ClassVar[MultiStageRestoreInfo.State]
        kFinalizeDone: _ClassVar[MultiStageRestoreInfo.State]
        kMultiStageFinished: _ClassVar[MultiStageRestoreInfo.State]
    kMultiStageNone: MultiStageRestoreInfo.State
    kMetadataSyncDone: MultiStageRestoreInfo.State
    kApplyChangesAreasDone: MultiStageRestoreInfo.State
    kFinalizeDone: MultiStageRestoreInfo.State
    kMultiStageFinished: MultiStageRestoreInfo.State
    ACTION_FIELD_NUMBER: _ClassVar[int]
    PERFORM_DATA_SYNC_FIELD_NUMBER: _ClassVar[int]
    PERFORM_FINALIZE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    action: _magneto_pb2.SqlMultiStageRestoreAction
    perform_data_sync: bool
    perform_finalize: bool
    state: MultiStageRestoreInfo.State
    def __init__(self, action: _Optional[_Union[_magneto_pb2.SqlMultiStageRestoreAction, _Mapping]] = ..., perform_data_sync: bool = ..., perform_finalize: bool = ..., state: _Optional[_Union[MultiStageRestoreInfo.State, str]] = ...) -> None: ...

class DatabaseRestoreInfo(_message.Message):
    __slots__ = ("sql_id", "database_name", "original_sql_id", "new_database_name", "instance_name", "target_database_name_proto", "backupset_row_info", "with_recovery", "is_alternate_instance", "use_vdi_snapshot", "num_bytes_to_process", "num_bytes_processed", "num_files", "num_files_processed", "finished", "total_backup_file_size_bytes", "data_file_destination", "log_file_destination", "secondary_data_file_destination", "secondary_data_file_destination_vec", "db_restore_overwrite_policy", "has_filestream_data", "keep_cdc", "native_restore_info", "differential_native_restore_info", "enable_checksum", "continue_after_error", "should_skip", "num_log_replays")
    class NativeRestoreInfo(_message.Message):
        __slots__ = ("state", "error", "overwrite", "db_snap_fs_backup_dir_name", "backup_file_path_vec", "file_vec", "snapshot_relative_dir_path", "with_clause", "source_view_name", "backup_size", "compressed_backup_size")
        class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kUninitialized: _ClassVar[DatabaseRestoreInfo.NativeRestoreInfo.State]
            kStarted: _ClassVar[DatabaseRestoreInfo.NativeRestoreInfo.State]
            kRestoreDone: _ClassVar[DatabaseRestoreInfo.NativeRestoreInfo.State]
            kNotifyComplete: _ClassVar[DatabaseRestoreInfo.NativeRestoreInfo.State]
        kUninitialized: DatabaseRestoreInfo.NativeRestoreInfo.State
        kStarted: DatabaseRestoreInfo.NativeRestoreInfo.State
        kRestoreDone: DatabaseRestoreInfo.NativeRestoreInfo.State
        kNotifyComplete: DatabaseRestoreInfo.NativeRestoreInfo.State
        STATE_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        OVERWRITE_FIELD_NUMBER: _ClassVar[int]
        DB_SNAP_FS_BACKUP_DIR_NAME_FIELD_NUMBER: _ClassVar[int]
        BACKUP_FILE_PATH_VEC_FIELD_NUMBER: _ClassVar[int]
        FILE_VEC_FIELD_NUMBER: _ClassVar[int]
        SNAPSHOT_RELATIVE_DIR_PATH_FIELD_NUMBER: _ClassVar[int]
        WITH_CLAUSE_FIELD_NUMBER: _ClassVar[int]
        SOURCE_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
        BACKUP_SIZE_FIELD_NUMBER: _ClassVar[int]
        COMPRESSED_BACKUP_SIZE_FIELD_NUMBER: _ClassVar[int]
        state: DatabaseRestoreInfo.NativeRestoreInfo.State
        error: _error_pb2.ErrorProto
        overwrite: bool
        db_snap_fs_backup_dir_name: str
        backup_file_path_vec: _containers.RepeatedScalarFieldContainer[str]
        file_vec: _containers.RepeatedCompositeFieldContainer[_sql_pb2.FileInfo]
        snapshot_relative_dir_path: str
        with_clause: str
        source_view_name: str
        backup_size: int
        compressed_backup_size: int
        def __init__(self, state: _Optional[_Union[DatabaseRestoreInfo.NativeRestoreInfo.State, str]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., overwrite: bool = ..., db_snap_fs_backup_dir_name: _Optional[str] = ..., backup_file_path_vec: _Optional[_Iterable[str]] = ..., file_vec: _Optional[_Iterable[_Union[_sql_pb2.FileInfo, _Mapping]]] = ..., snapshot_relative_dir_path: _Optional[str] = ..., with_clause: _Optional[str] = ..., source_view_name: _Optional[str] = ..., backup_size: _Optional[int] = ..., compressed_backup_size: _Optional[int] = ...) -> None: ...
    SQL_ID_FIELD_NUMBER: _ClassVar[int]
    DATABASE_NAME_FIELD_NUMBER: _ClassVar[int]
    ORIGINAL_SQL_ID_FIELD_NUMBER: _ClassVar[int]
    NEW_DATABASE_NAME_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_NAME_FIELD_NUMBER: _ClassVar[int]
    TARGET_DATABASE_NAME_PROTO_FIELD_NUMBER: _ClassVar[int]
    BACKUPSET_ROW_INFO_FIELD_NUMBER: _ClassVar[int]
    WITH_RECOVERY_FIELD_NUMBER: _ClassVar[int]
    IS_ALTERNATE_INSTANCE_FIELD_NUMBER: _ClassVar[int]
    USE_VDI_SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    NUM_BYTES_TO_PROCESS_FIELD_NUMBER: _ClassVar[int]
    NUM_BYTES_PROCESSED_FIELD_NUMBER: _ClassVar[int]
    NUM_FILES_FIELD_NUMBER: _ClassVar[int]
    NUM_FILES_PROCESSED_FIELD_NUMBER: _ClassVar[int]
    FINISHED_FIELD_NUMBER: _ClassVar[int]
    TOTAL_BACKUP_FILE_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    DATA_FILE_DESTINATION_FIELD_NUMBER: _ClassVar[int]
    LOG_FILE_DESTINATION_FIELD_NUMBER: _ClassVar[int]
    SECONDARY_DATA_FILE_DESTINATION_FIELD_NUMBER: _ClassVar[int]
    SECONDARY_DATA_FILE_DESTINATION_VEC_FIELD_NUMBER: _ClassVar[int]
    DB_RESTORE_OVERWRITE_POLICY_FIELD_NUMBER: _ClassVar[int]
    HAS_FILESTREAM_DATA_FIELD_NUMBER: _ClassVar[int]
    KEEP_CDC_FIELD_NUMBER: _ClassVar[int]
    NATIVE_RESTORE_INFO_FIELD_NUMBER: _ClassVar[int]
    DIFFERENTIAL_NATIVE_RESTORE_INFO_FIELD_NUMBER: _ClassVar[int]
    ENABLE_CHECKSUM_FIELD_NUMBER: _ClassVar[int]
    CONTINUE_AFTER_ERROR_FIELD_NUMBER: _ClassVar[int]
    SHOULD_SKIP_FIELD_NUMBER: _ClassVar[int]
    NUM_LOG_REPLAYS_FIELD_NUMBER: _ClassVar[int]
    sql_id: _sql_pb2.SqlId
    database_name: str
    original_sql_id: _sql_pb2.SqlId
    new_database_name: str
    instance_name: str
    target_database_name_proto: DBNameProto
    backupset_row_info: BackupSetRowInfo
    with_recovery: bool
    is_alternate_instance: bool
    use_vdi_snapshot: bool
    num_bytes_to_process: int
    num_bytes_processed: int
    num_files: int
    num_files_processed: int
    finished: bool
    total_backup_file_size_bytes: int
    data_file_destination: str
    log_file_destination: str
    secondary_data_file_destination: str
    secondary_data_file_destination_vec: _containers.RepeatedCompositeFieldContainer[_common_pb2.FilesToDirectoryMapping]
    db_restore_overwrite_policy: _sql_pb2.DBRestoreOverwritePolicy.Type
    has_filestream_data: bool
    keep_cdc: bool
    native_restore_info: DatabaseRestoreInfo.NativeRestoreInfo
    differential_native_restore_info: DatabaseRestoreInfo.NativeRestoreInfo
    enable_checksum: bool
    continue_after_error: bool
    should_skip: bool
    num_log_replays: int
    def __init__(self, sql_id: _Optional[_Union[_sql_pb2.SqlId, _Mapping]] = ..., database_name: _Optional[str] = ..., original_sql_id: _Optional[_Union[_sql_pb2.SqlId, _Mapping]] = ..., new_database_name: _Optional[str] = ..., instance_name: _Optional[str] = ..., target_database_name_proto: _Optional[_Union[DBNameProto, _Mapping]] = ..., backupset_row_info: _Optional[_Union[BackupSetRowInfo, _Mapping]] = ..., with_recovery: bool = ..., is_alternate_instance: bool = ..., use_vdi_snapshot: bool = ..., num_bytes_to_process: _Optional[int] = ..., num_bytes_processed: _Optional[int] = ..., num_files: _Optional[int] = ..., num_files_processed: _Optional[int] = ..., finished: bool = ..., total_backup_file_size_bytes: _Optional[int] = ..., data_file_destination: _Optional[str] = ..., log_file_destination: _Optional[str] = ..., secondary_data_file_destination: _Optional[str] = ..., secondary_data_file_destination_vec: _Optional[_Iterable[_Union[_common_pb2.FilesToDirectoryMapping, _Mapping]]] = ..., db_restore_overwrite_policy: _Optional[_Union[_sql_pb2.DBRestoreOverwritePolicy.Type, str]] = ..., has_filestream_data: bool = ..., keep_cdc: bool = ..., native_restore_info: _Optional[_Union[DatabaseRestoreInfo.NativeRestoreInfo, _Mapping]] = ..., differential_native_restore_info: _Optional[_Union[DatabaseRestoreInfo.NativeRestoreInfo, _Mapping]] = ..., enable_checksum: bool = ..., continue_after_error: bool = ..., should_skip: bool = ..., num_log_replays: _Optional[int] = ...) -> None: ...

class VSSDatabaseRestoreInfo(_message.Message):
    __slots__ = ("snapshot_set_id", "server_snapshot_info", "owner_snapshot_dir_full_path", "server_snapshot_info_file_name", "common_host_dir_name", "is_common_host_dir_cloned_under_db_snapshots", "server_snapshot_serialized_fetch_info", "database_vec", "all_databases_with_recovery", "state", "start_time_usecs", "num_bytes_processed", "num_bytes_to_process", "error", "copy_attach", "attached_db_info_vec", "cohesity_mount_to_local_file_path_map", "multi_stage_restore_info", "apply_changed_areas_task_info", "user_messages", "restore_files_info", "parallel_restore_state_info")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kCreated: _ClassVar[VSSDatabaseRestoreInfo.State]
        kPreprocessed: _ClassVar[VSSDatabaseRestoreInfo.State]
        kInProgress: _ClassVar[VSSDatabaseRestoreInfo.State]
        kNoMoreData: _ClassVar[VSSDatabaseRestoreInfo.State]
        kDone: _ClassVar[VSSDatabaseRestoreInfo.State]
        kCancelled: _ClassVar[VSSDatabaseRestoreInfo.State]
    kCreated: VSSDatabaseRestoreInfo.State
    kPreprocessed: VSSDatabaseRestoreInfo.State
    kInProgress: VSSDatabaseRestoreInfo.State
    kNoMoreData: VSSDatabaseRestoreInfo.State
    kDone: VSSDatabaseRestoreInfo.State
    kCancelled: VSSDatabaseRestoreInfo.State
    class CohesityMountToLocalFilePathMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    SNAPSHOT_SET_ID_FIELD_NUMBER: _ClassVar[int]
    SERVER_SNAPSHOT_INFO_FIELD_NUMBER: _ClassVar[int]
    OWNER_SNAPSHOT_DIR_FULL_PATH_FIELD_NUMBER: _ClassVar[int]
    SERVER_SNAPSHOT_INFO_FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    COMMON_HOST_DIR_NAME_FIELD_NUMBER: _ClassVar[int]
    IS_COMMON_HOST_DIR_CLONED_UNDER_DB_SNAPSHOTS_FIELD_NUMBER: _ClassVar[int]
    SERVER_SNAPSHOT_SERIALIZED_FETCH_INFO_FIELD_NUMBER: _ClassVar[int]
    DATABASE_VEC_FIELD_NUMBER: _ClassVar[int]
    ALL_DATABASES_WITH_RECOVERY_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    NUM_BYTES_PROCESSED_FIELD_NUMBER: _ClassVar[int]
    NUM_BYTES_TO_PROCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    COPY_ATTACH_FIELD_NUMBER: _ClassVar[int]
    ATTACHED_DB_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    COHESITY_MOUNT_TO_LOCAL_FILE_PATH_MAP_FIELD_NUMBER: _ClassVar[int]
    MULTI_STAGE_RESTORE_INFO_FIELD_NUMBER: _ClassVar[int]
    APPLY_CHANGED_AREAS_TASK_INFO_FIELD_NUMBER: _ClassVar[int]
    USER_MESSAGES_FIELD_NUMBER: _ClassVar[int]
    RESTORE_FILES_INFO_FIELD_NUMBER: _ClassVar[int]
    PARALLEL_RESTORE_STATE_INFO_FIELD_NUMBER: _ClassVar[int]
    snapshot_set_id: bytes
    server_snapshot_info: _agent_pb2.ServerSnapshotInfo
    owner_snapshot_dir_full_path: str
    server_snapshot_info_file_name: str
    common_host_dir_name: str
    is_common_host_dir_cloned_under_db_snapshots: bool
    server_snapshot_serialized_fetch_info: _agent_pb2.ServerSnapshotSerializedFetchInfo
    database_vec: _containers.RepeatedCompositeFieldContainer[DatabaseRestoreInfo]
    all_databases_with_recovery: bool
    state: VSSDatabaseRestoreInfo.State
    start_time_usecs: int
    num_bytes_processed: int
    num_bytes_to_process: int
    error: _error_pb2.ErrorProto
    copy_attach: bool
    attached_db_info_vec: _containers.RepeatedCompositeFieldContainer[AttachedDbInfo]
    cohesity_mount_to_local_file_path_map: _containers.ScalarMap[str, str]
    multi_stage_restore_info: MultiStageRestoreInfo
    apply_changed_areas_task_info: _common_pb2_1.ApplyChangedAreasTaskInfo
    user_messages: _magneto_pb2.UserMessageProto
    restore_files_info: _magneto_pb2.RestoreFilesInfoProto
    parallel_restore_state_info: ParallelRestoreStateInfo
    def __init__(self, snapshot_set_id: _Optional[bytes] = ..., server_snapshot_info: _Optional[_Union[_agent_pb2.ServerSnapshotInfo, _Mapping]] = ..., owner_snapshot_dir_full_path: _Optional[str] = ..., server_snapshot_info_file_name: _Optional[str] = ..., common_host_dir_name: _Optional[str] = ..., is_common_host_dir_cloned_under_db_snapshots: bool = ..., server_snapshot_serialized_fetch_info: _Optional[_Union[_agent_pb2.ServerSnapshotSerializedFetchInfo, _Mapping]] = ..., database_vec: _Optional[_Iterable[_Union[DatabaseRestoreInfo, _Mapping]]] = ..., all_databases_with_recovery: bool = ..., state: _Optional[_Union[VSSDatabaseRestoreInfo.State, str]] = ..., start_time_usecs: _Optional[int] = ..., num_bytes_processed: _Optional[int] = ..., num_bytes_to_process: _Optional[int] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., copy_attach: bool = ..., attached_db_info_vec: _Optional[_Iterable[_Union[AttachedDbInfo, _Mapping]]] = ..., cohesity_mount_to_local_file_path_map: _Optional[_Mapping[str, str]] = ..., multi_stage_restore_info: _Optional[_Union[MultiStageRestoreInfo, _Mapping]] = ..., apply_changed_areas_task_info: _Optional[_Union[_common_pb2_1.ApplyChangedAreasTaskInfo, _Mapping]] = ..., user_messages: _Optional[_Union[_magneto_pb2.UserMessageProto, _Mapping]] = ..., restore_files_info: _Optional[_Union[_magneto_pb2.RestoreFilesInfoProto, _Mapping]] = ..., parallel_restore_state_info: _Optional[_Union[ParallelRestoreStateInfo, _Mapping]] = ...) -> None: ...

class NativeDatabaseRestoreInfo(_message.Message):
    __slots__ = ("database_vec", "error", "original_instance_info_vec")
    DATABASE_VEC_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ORIGINAL_INSTANCE_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    database_vec: _containers.RepeatedCompositeFieldContainer[DatabaseRestoreInfo]
    error: _error_pb2.ErrorProto
    original_instance_info_vec: _containers.RepeatedCompositeFieldContainer[_sql_pb2.SQLInstanceInfo]
    def __init__(self, database_vec: _Optional[_Iterable[_Union[DatabaseRestoreInfo, _Mapping]]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., original_instance_info_vec: _Optional[_Iterable[_Union[_sql_pb2.SQLInstanceInfo, _Mapping]]] = ...) -> None: ...

class VSSRestoreInfoProto(_message.Message):
    __slots__ = ("restore_from_local_snapshot", "database_restore_info", "restore_disks_task_info_proto", "restore_from_file_based_backup", "restore_disks_task_info_DEPRECATED")
    RESTORE_FROM_LOCAL_SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    DATABASE_RESTORE_INFO_FIELD_NUMBER: _ClassVar[int]
    RESTORE_DISKS_TASK_INFO_PROTO_FIELD_NUMBER: _ClassVar[int]
    RESTORE_FROM_FILE_BASED_BACKUP_FIELD_NUMBER: _ClassVar[int]
    RESTORE_DISKS_TASK_INFO_DEPRECATED_FIELD_NUMBER: _ClassVar[int]
    restore_from_local_snapshot: bool
    database_restore_info: VSSDatabaseRestoreInfo
    restore_disks_task_info_proto: _magneto_pb2.SetupRestoreDiskTaskInfoProto
    restore_from_file_based_backup: bool
    restore_disks_task_info_DEPRECATED: _vmware_setup_restore_disks_pb2.SetupRestoreDiskTaskInfo
    def __init__(self, restore_from_local_snapshot: bool = ..., database_restore_info: _Optional[_Union[VSSDatabaseRestoreInfo, _Mapping]] = ..., restore_disks_task_info_proto: _Optional[_Union[_magneto_pb2.SetupRestoreDiskTaskInfoProto, _Mapping]] = ..., restore_from_file_based_backup: bool = ..., restore_disks_task_info_DEPRECATED: _Optional[_Union[_vmware_setup_restore_disks_pb2.SetupRestoreDiskTaskInfo, _Mapping]] = ...) -> None: ...

class DatabaseLogReplayInfo(_message.Message):
    __slots__ = ("sql_id", "database_name", "target_database_name_proto", "log_replay_info_vec", "redo_start_lsn", "redo_start_fork_guid", "starting_log_index", "compatibility_level_vec", "with_recovery", "attached_db_info", "keep_cdc", "enable_checksum", "continue_after_error")
    class LogReplayInfo(_message.Message):
        __slots__ = ("backupset_row_info", "stream_info", "total_backup_size_bytes", "error", "source_view_name", "snapshot_files_cloned", "target_dir_name", "run_start_time_usecs", "native_restore_info")
        BACKUPSET_ROW_INFO_FIELD_NUMBER: _ClassVar[int]
        STREAM_INFO_FIELD_NUMBER: _ClassVar[int]
        TOTAL_BACKUP_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        SOURCE_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
        SNAPSHOT_FILES_CLONED_FIELD_NUMBER: _ClassVar[int]
        TARGET_DIR_NAME_FIELD_NUMBER: _ClassVar[int]
        RUN_START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
        NATIVE_RESTORE_INFO_FIELD_NUMBER: _ClassVar[int]
        backupset_row_info: BackupSetRowInfo
        stream_info: StreamInfoProto
        total_backup_size_bytes: int
        error: _error_pb2.ErrorProto
        source_view_name: str
        snapshot_files_cloned: bool
        target_dir_name: str
        run_start_time_usecs: int
        native_restore_info: DatabaseRestoreInfo.NativeRestoreInfo
        def __init__(self, backupset_row_info: _Optional[_Union[BackupSetRowInfo, _Mapping]] = ..., stream_info: _Optional[_Union[StreamInfoProto, _Mapping]] = ..., total_backup_size_bytes: _Optional[int] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., source_view_name: _Optional[str] = ..., snapshot_files_cloned: bool = ..., target_dir_name: _Optional[str] = ..., run_start_time_usecs: _Optional[int] = ..., native_restore_info: _Optional[_Union[DatabaseRestoreInfo.NativeRestoreInfo, _Mapping]] = ...) -> None: ...
    SQL_ID_FIELD_NUMBER: _ClassVar[int]
    DATABASE_NAME_FIELD_NUMBER: _ClassVar[int]
    TARGET_DATABASE_NAME_PROTO_FIELD_NUMBER: _ClassVar[int]
    LOG_REPLAY_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    REDO_START_LSN_FIELD_NUMBER: _ClassVar[int]
    REDO_START_FORK_GUID_FIELD_NUMBER: _ClassVar[int]
    STARTING_LOG_INDEX_FIELD_NUMBER: _ClassVar[int]
    COMPATIBILITY_LEVEL_VEC_FIELD_NUMBER: _ClassVar[int]
    WITH_RECOVERY_FIELD_NUMBER: _ClassVar[int]
    ATTACHED_DB_INFO_FIELD_NUMBER: _ClassVar[int]
    KEEP_CDC_FIELD_NUMBER: _ClassVar[int]
    ENABLE_CHECKSUM_FIELD_NUMBER: _ClassVar[int]
    CONTINUE_AFTER_ERROR_FIELD_NUMBER: _ClassVar[int]
    sql_id: _sql_pb2.SqlId
    database_name: str
    target_database_name_proto: DBNameProto
    log_replay_info_vec: _containers.RepeatedCompositeFieldContainer[DatabaseLogReplayInfo.LogReplayInfo]
    redo_start_lsn: str
    redo_start_fork_guid: str
    starting_log_index: int
    compatibility_level_vec: _containers.RepeatedScalarFieldContainer[int]
    with_recovery: bool
    attached_db_info: AttachedDbInfo
    keep_cdc: bool
    enable_checksum: bool
    continue_after_error: bool
    def __init__(self, sql_id: _Optional[_Union[_sql_pb2.SqlId, _Mapping]] = ..., database_name: _Optional[str] = ..., target_database_name_proto: _Optional[_Union[DBNameProto, _Mapping]] = ..., log_replay_info_vec: _Optional[_Iterable[_Union[DatabaseLogReplayInfo.LogReplayInfo, _Mapping]]] = ..., redo_start_lsn: _Optional[str] = ..., redo_start_fork_guid: _Optional[str] = ..., starting_log_index: _Optional[int] = ..., compatibility_level_vec: _Optional[_Iterable[int]] = ..., with_recovery: bool = ..., attached_db_info: _Optional[_Union[AttachedDbInfo, _Mapping]] = ..., keep_cdc: bool = ..., enable_checksum: bool = ..., continue_after_error: bool = ...) -> None: ...

class RestoreSqlFromNativeBackupInfo(_message.Message):
    __slots__ = ("state",)
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kCreated: _ClassVar[RestoreSqlFromNativeBackupInfo.State]
        kRestore: _ClassVar[RestoreSqlFromNativeBackupInfo.State]
        kLogReplay: _ClassVar[RestoreSqlFromNativeBackupInfo.State]
        kSanityCheck: _ClassVar[RestoreSqlFromNativeBackupInfo.State]
        kViewDelete: _ClassVar[RestoreSqlFromNativeBackupInfo.State]
        kDone: _ClassVar[RestoreSqlFromNativeBackupInfo.State]
        kCloneBackupFiles: _ClassVar[RestoreSqlFromNativeBackupInfo.State]
        kCloneDifferentialBackupFiles: _ClassVar[RestoreSqlFromNativeBackupInfo.State]
    kCreated: RestoreSqlFromNativeBackupInfo.State
    kRestore: RestoreSqlFromNativeBackupInfo.State
    kLogReplay: RestoreSqlFromNativeBackupInfo.State
    kSanityCheck: RestoreSqlFromNativeBackupInfo.State
    kViewDelete: RestoreSqlFromNativeBackupInfo.State
    kDone: RestoreSqlFromNativeBackupInfo.State
    kCloneBackupFiles: RestoreSqlFromNativeBackupInfo.State
    kCloneDifferentialBackupFiles: RestoreSqlFromNativeBackupInfo.State
    STATE_FIELD_NUMBER: _ClassVar[int]
    state: RestoreSqlFromNativeBackupInfo.State
    def __init__(self, state: _Optional[_Union[RestoreSqlFromNativeBackupInfo.State, str]] = ...) -> None: ...

class RestoreSqlFromNASInfo(_message.Message):
    __slots__ = ("state",)
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kCreated: _ClassVar[RestoreSqlFromNASInfo.State]
        kVSSRestore: _ClassVar[RestoreSqlFromNASInfo.State]
        kLogReplay: _ClassVar[RestoreSqlFromNASInfo.State]
        kSanityCheck: _ClassVar[RestoreSqlFromNASInfo.State]
        kDone: _ClassVar[RestoreSqlFromNASInfo.State]
    kCreated: RestoreSqlFromNASInfo.State
    kVSSRestore: RestoreSqlFromNASInfo.State
    kLogReplay: RestoreSqlFromNASInfo.State
    kSanityCheck: RestoreSqlFromNASInfo.State
    kDone: RestoreSqlFromNASInfo.State
    STATE_FIELD_NUMBER: _ClassVar[int]
    state: RestoreSqlFromNASInfo.State
    def __init__(self, state: _Optional[_Union[RestoreSqlFromNASInfo.State, str]] = ...) -> None: ...

class RestoreSqlFromSourceInfo(_message.Message):
    __slots__ = ("state", "snapshot_deletion_error")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kCreated: _ClassVar[RestoreSqlFromSourceInfo.State]
        kVSSRestore: _ClassVar[RestoreSqlFromSourceInfo.State]
        kDeleteVSSSnapshot: _ClassVar[RestoreSqlFromSourceInfo.State]
        kLogReplay: _ClassVar[RestoreSqlFromSourceInfo.State]
        kSanityCheck: _ClassVar[RestoreSqlFromSourceInfo.State]
        kDone: _ClassVar[RestoreSqlFromSourceInfo.State]
    kCreated: RestoreSqlFromSourceInfo.State
    kVSSRestore: RestoreSqlFromSourceInfo.State
    kDeleteVSSSnapshot: RestoreSqlFromSourceInfo.State
    kLogReplay: RestoreSqlFromSourceInfo.State
    kSanityCheck: RestoreSqlFromSourceInfo.State
    kDone: RestoreSqlFromSourceInfo.State
    STATE_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_DELETION_ERROR_FIELD_NUMBER: _ClassVar[int]
    state: RestoreSqlFromSourceInfo.State
    snapshot_deletion_error: _error_pb2.ErrorProto
    def __init__(self, state: _Optional[_Union[RestoreSqlFromSourceInfo.State, str]] = ..., snapshot_deletion_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class SQLDatabaseFileInfo(_message.Message):
    __slots__ = ("file_id", "type", "type_description", "name", "physical_name", "relative_filename", "snapshot_path", "xxx_state_deprecated", "size_bytes", "file_attributes", "database_id", "state", "state_description", "redo_start_lsn", "redo_start_fork_guid", "is_on_external_storage")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kOnline: _ClassVar[SQLDatabaseFileInfo.State]
        kRestoring: _ClassVar[SQLDatabaseFileInfo.State]
        kRecovering: _ClassVar[SQLDatabaseFileInfo.State]
        kRecoveryPending: _ClassVar[SQLDatabaseFileInfo.State]
        kSuspect: _ClassVar[SQLDatabaseFileInfo.State]
        kNotSupportedState: _ClassVar[SQLDatabaseFileInfo.State]
        kOffline: _ClassVar[SQLDatabaseFileInfo.State]
        kDefunct: _ClassVar[SQLDatabaseFileInfo.State]
    kOnline: SQLDatabaseFileInfo.State
    kRestoring: SQLDatabaseFileInfo.State
    kRecovering: SQLDatabaseFileInfo.State
    kRecoveryPending: SQLDatabaseFileInfo.State
    kSuspect: SQLDatabaseFileInfo.State
    kNotSupportedState: SQLDatabaseFileInfo.State
    kOffline: SQLDatabaseFileInfo.State
    kDefunct: SQLDatabaseFileInfo.State
    FILE_ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    TYPE_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PHYSICAL_NAME_FIELD_NUMBER: _ClassVar[int]
    RELATIVE_FILENAME_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_PATH_FIELD_NUMBER: _ClassVar[int]
    XXX_STATE_DEPRECATED_FIELD_NUMBER: _ClassVar[int]
    SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    FILE_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    DATABASE_ID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    STATE_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    REDO_START_LSN_FIELD_NUMBER: _ClassVar[int]
    REDO_START_FORK_GUID_FIELD_NUMBER: _ClassVar[int]
    IS_ON_EXTERNAL_STORAGE_FIELD_NUMBER: _ClassVar[int]
    file_id: int
    type: _sql_pb2.FileInfo.Type
    type_description: str
    name: bytes
    physical_name: bytes
    relative_filename: bytes
    snapshot_path: str
    xxx_state_deprecated: SQLDatabaseFileInfo.State
    size_bytes: int
    file_attributes: _file_attrs_pb2.FileAttributes
    database_id: int
    state: SQLDatabaseFileInfo.State
    state_description: str
    redo_start_lsn: str
    redo_start_fork_guid: str
    is_on_external_storage: bool
    def __init__(self, file_id: _Optional[int] = ..., type: _Optional[_Union[_sql_pb2.FileInfo.Type, str]] = ..., type_description: _Optional[str] = ..., name: _Optional[bytes] = ..., physical_name: _Optional[bytes] = ..., relative_filename: _Optional[bytes] = ..., snapshot_path: _Optional[str] = ..., xxx_state_deprecated: _Optional[_Union[SQLDatabaseFileInfo.State, str]] = ..., size_bytes: _Optional[int] = ..., file_attributes: _Optional[_Union[_file_attrs_pb2.FileAttributes, _Mapping]] = ..., database_id: _Optional[int] = ..., state: _Optional[_Union[SQLDatabaseFileInfo.State, str]] = ..., state_description: _Optional[str] = ..., redo_start_lsn: _Optional[str] = ..., redo_start_fork_guid: _Optional[str] = ..., is_on_external_storage: bool = ...) -> None: ...

class DatabaseToFileInfo(_message.Message):
    __slots__ = ("sql_id", "db_name", "file_info_vec")
    SQL_ID_FIELD_NUMBER: _ClassVar[int]
    DB_NAME_FIELD_NUMBER: _ClassVar[int]
    FILE_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    sql_id: _sql_pb2.SqlId
    db_name: DBNameProto
    file_info_vec: _containers.RepeatedCompositeFieldContainer[SQLDatabaseFileInfo]
    def __init__(self, sql_id: _Optional[_Union[_sql_pb2.SqlId, _Mapping]] = ..., db_name: _Optional[_Union[DBNameProto, _Mapping]] = ..., file_info_vec: _Optional[_Iterable[_Union[SQLDatabaseFileInfo, _Mapping]]] = ...) -> None: ...

class RestoreInfo(_message.Message):
    __slots__ = ("restore_time", "restore_sql_from_nas", "restore_sql_from_source", "vss_restore_info", "database_log_replay_info_vec", "agent_info", "restore_sql_from_native_backup", "native_database_restore_info", "database_to_file_info_vec", "should_skip_vss_restore", "replay_entire_last_log")
    SQL_RESTORE_INFO_FIELD_NUMBER: _ClassVar[int]
    sql_restore_info: _descriptor.FieldDescriptor
    RESTORE_TIME_FIELD_NUMBER: _ClassVar[int]
    RESTORE_SQL_FROM_NAS_FIELD_NUMBER: _ClassVar[int]
    RESTORE_SQL_FROM_SOURCE_FIELD_NUMBER: _ClassVar[int]
    VSS_RESTORE_INFO_FIELD_NUMBER: _ClassVar[int]
    DATABASE_LOG_REPLAY_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    AGENT_INFO_FIELD_NUMBER: _ClassVar[int]
    RESTORE_SQL_FROM_NATIVE_BACKUP_FIELD_NUMBER: _ClassVar[int]
    NATIVE_DATABASE_RESTORE_INFO_FIELD_NUMBER: _ClassVar[int]
    DATABASE_TO_FILE_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    SHOULD_SKIP_VSS_RESTORE_FIELD_NUMBER: _ClassVar[int]
    REPLAY_ENTIRE_LAST_LOG_FIELD_NUMBER: _ClassVar[int]
    restore_time: LocalTime
    restore_sql_from_nas: RestoreSqlFromNASInfo
    restore_sql_from_source: RestoreSqlFromSourceInfo
    vss_restore_info: VSSRestoreInfoProto
    database_log_replay_info_vec: _containers.RepeatedCompositeFieldContainer[DatabaseLogReplayInfo]
    agent_info: _agent_pb2.AgentInfoProto
    restore_sql_from_native_backup: RestoreSqlFromNativeBackupInfo
    native_database_restore_info: NativeDatabaseRestoreInfo
    database_to_file_info_vec: _containers.RepeatedCompositeFieldContainer[DatabaseToFileInfo]
    should_skip_vss_restore: bool
    replay_entire_last_log: bool
    def __init__(self, restore_time: _Optional[_Union[LocalTime, _Mapping]] = ..., restore_sql_from_nas: _Optional[_Union[RestoreSqlFromNASInfo, _Mapping]] = ..., restore_sql_from_source: _Optional[_Union[RestoreSqlFromSourceInfo, _Mapping]] = ..., vss_restore_info: _Optional[_Union[VSSRestoreInfoProto, _Mapping]] = ..., database_log_replay_info_vec: _Optional[_Iterable[_Union[DatabaseLogReplayInfo, _Mapping]]] = ..., agent_info: _Optional[_Union[_agent_pb2.AgentInfoProto, _Mapping]] = ..., restore_sql_from_native_backup: _Optional[_Union[RestoreSqlFromNativeBackupInfo, _Mapping]] = ..., native_database_restore_info: _Optional[_Union[NativeDatabaseRestoreInfo, _Mapping]] = ..., database_to_file_info_vec: _Optional[_Iterable[_Union[DatabaseToFileInfo, _Mapping]]] = ..., should_skip_vss_restore: bool = ..., replay_entire_last_log: bool = ...) -> None: ...

class DestroyCloneTaskInfo(_message.Message):
    __slots__ = ("attached_db_info_vec", "restore_disks_task_info_proto", "is_file_based_restore")
    SQL_DESTROY_CLONE_APP_TASK_INFO_FIELD_NUMBER: _ClassVar[int]
    sql_destroy_clone_app_task_info: _descriptor.FieldDescriptor
    ATTACHED_DB_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    RESTORE_DISKS_TASK_INFO_PROTO_FIELD_NUMBER: _ClassVar[int]
    IS_FILE_BASED_RESTORE_FIELD_NUMBER: _ClassVar[int]
    attached_db_info_vec: _containers.RepeatedCompositeFieldContainer[AttachedDbInfo]
    restore_disks_task_info_proto: _magneto_pb2.SetupRestoreDiskTaskInfoProto
    is_file_based_restore: bool
    def __init__(self, attached_db_info_vec: _Optional[_Iterable[_Union[AttachedDbInfo, _Mapping]]] = ..., restore_disks_task_info_proto: _Optional[_Union[_magneto_pb2.SetupRestoreDiskTaskInfoProto, _Mapping]] = ..., is_file_based_restore: bool = ...) -> None: ...

class DBFileType(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kPrimaryData: _ClassVar[DBFileType.Type]
        kLog: _ClassVar[DBFileType.Type]
        kSecondaryData: _ClassVar[DBFileType.Type]
        kFileStream: _ClassVar[DBFileType.Type]
    kPrimaryData: DBFileType.Type
    kLog: DBFileType.Type
    kSecondaryData: DBFileType.Type
    kFileStream: DBFileType.Type
    def __init__(self) -> None: ...

class Credentials(_message.Message):
    __slots__ = ("username", "password", "encrypted_password")
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTED_PASSWORD_FIELD_NUMBER: _ClassVar[int]
    username: str
    password: str
    encrypted_password: bytes
    def __init__(self, username: _Optional[str] = ..., password: _Optional[str] = ..., encrypted_password: _Optional[bytes] = ...) -> None: ...
