from magneto.agents.base import agent_pb2 as _agent_pb2
from magneto.agents.base import oracle_sql_pb2 as _oracle_sql_pb2
from magneto.api.common import oracle_pb2 as _oracle_pb2
from magneto.base.entities import oracle_pb2 as _oracle_pb2_1
from magneto.base import enums_pb2 as _enums_pb2
from magneto.base import env_params_pb2 as _env_params_pb2
from magneto.base import error_pb2 as _error_pb2
from magneto.base import magneto_pb2 as _magneto_pb2
from magneto.base import env_params_pb2 as _env_params_pb2_1
from magneto.base import sub_task_pb2 as _sub_task_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DatabaseBackupInfo(_message.Message):
    __slots__ = ("uuid", "unique_name", "db_name", "db_entity_info", "skip_error", "error", "perform_l0_backup", "backup_set_info", "data_files_info", "previous_data_files_info", "max_fuzzy_scn", "min_checkpoint_scn", "max_checkpoint_time", "db_incarnation_info", "log_file_info", "timezone_difference", "catalog_performed", "relative_db_dir", "backup_view_name", "rman_backup_type", "is_backup_validated", "is_self_sufficient", "self_sufficiency_log_info", "is_log_filler_clone_done", "thread_info", "rac_config_file", "deprecated_archive_logs_info")
    UUID_FIELD_NUMBER: _ClassVar[int]
    UNIQUE_NAME_FIELD_NUMBER: _ClassVar[int]
    DB_NAME_FIELD_NUMBER: _ClassVar[int]
    DB_ENTITY_INFO_FIELD_NUMBER: _ClassVar[int]
    SKIP_ERROR_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    PERFORM_L0_BACKUP_FIELD_NUMBER: _ClassVar[int]
    BACKUP_SET_INFO_FIELD_NUMBER: _ClassVar[int]
    DATA_FILES_INFO_FIELD_NUMBER: _ClassVar[int]
    PREVIOUS_DATA_FILES_INFO_FIELD_NUMBER: _ClassVar[int]
    MAX_FUZZY_SCN_FIELD_NUMBER: _ClassVar[int]
    MIN_CHECKPOINT_SCN_FIELD_NUMBER: _ClassVar[int]
    MAX_CHECKPOINT_TIME_FIELD_NUMBER: _ClassVar[int]
    DB_INCARNATION_INFO_FIELD_NUMBER: _ClassVar[int]
    LOG_FILE_INFO_FIELD_NUMBER: _ClassVar[int]
    TIMEZONE_DIFFERENCE_FIELD_NUMBER: _ClassVar[int]
    CATALOG_PERFORMED_FIELD_NUMBER: _ClassVar[int]
    RELATIVE_DB_DIR_FIELD_NUMBER: _ClassVar[int]
    BACKUP_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    RMAN_BACKUP_TYPE_FIELD_NUMBER: _ClassVar[int]
    IS_BACKUP_VALIDATED_FIELD_NUMBER: _ClassVar[int]
    IS_SELF_SUFFICIENT_FIELD_NUMBER: _ClassVar[int]
    SELF_SUFFICIENCY_LOG_INFO_FIELD_NUMBER: _ClassVar[int]
    IS_LOG_FILLER_CLONE_DONE_FIELD_NUMBER: _ClassVar[int]
    THREAD_INFO_FIELD_NUMBER: _ClassVar[int]
    RAC_CONFIG_FILE_FIELD_NUMBER: _ClassVar[int]
    DEPRECATED_ARCHIVE_LOGS_INFO_FIELD_NUMBER: _ClassVar[int]
    uuid: str
    unique_name: str
    db_name: str
    db_entity_info: _oracle_pb2_1.DBEntityInfo
    skip_error: _error_pb2.ErrorProto
    error: _error_pb2.ErrorProto
    perform_l0_backup: bool
    backup_set_info: _oracle_sql_pb2.BackupSetInfo
    data_files_info: _oracle_sql_pb2.DataFilesInfo
    previous_data_files_info: _oracle_sql_pb2.DataFilesInfo
    max_fuzzy_scn: int
    min_checkpoint_scn: int
    max_checkpoint_time: int
    db_incarnation_info: _oracle_sql_pb2.DatabaseIncarnationInfo
    log_file_info: _oracle_sql_pb2.LogFileInfo
    timezone_difference: int
    catalog_performed: bool
    relative_db_dir: str
    backup_view_name: str
    rman_backup_type: _env_params_pb2_1.OracleRmanBackupType.Type
    is_backup_validated: bool
    is_self_sufficient: bool
    self_sufficiency_log_info: SelfSufficiencyLogInfo
    is_log_filler_clone_done: bool
    thread_info: _oracle_sql_pb2.ThreadInfo
    rac_config_file: str
    deprecated_archive_logs_info: _oracle_sql_pb2.ArchiveLogsInfo
    def __init__(self, uuid: _Optional[str] = ..., unique_name: _Optional[str] = ..., db_name: _Optional[str] = ..., db_entity_info: _Optional[_Union[_oracle_pb2_1.DBEntityInfo, _Mapping]] = ..., skip_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., perform_l0_backup: bool = ..., backup_set_info: _Optional[_Union[_oracle_sql_pb2.BackupSetInfo, _Mapping]] = ..., data_files_info: _Optional[_Union[_oracle_sql_pb2.DataFilesInfo, _Mapping]] = ..., previous_data_files_info: _Optional[_Union[_oracle_sql_pb2.DataFilesInfo, _Mapping]] = ..., max_fuzzy_scn: _Optional[int] = ..., min_checkpoint_scn: _Optional[int] = ..., max_checkpoint_time: _Optional[int] = ..., db_incarnation_info: _Optional[_Union[_oracle_sql_pb2.DatabaseIncarnationInfo, _Mapping]] = ..., log_file_info: _Optional[_Union[_oracle_sql_pb2.LogFileInfo, _Mapping]] = ..., timezone_difference: _Optional[int] = ..., catalog_performed: bool = ..., relative_db_dir: _Optional[str] = ..., backup_view_name: _Optional[str] = ..., rman_backup_type: _Optional[_Union[_env_params_pb2_1.OracleRmanBackupType.Type, str]] = ..., is_backup_validated: bool = ..., is_self_sufficient: bool = ..., self_sufficiency_log_info: _Optional[_Union[SelfSufficiencyLogInfo, _Mapping]] = ..., is_log_filler_clone_done: bool = ..., thread_info: _Optional[_Union[_oracle_sql_pb2.ThreadInfo, _Mapping]] = ..., rac_config_file: _Optional[str] = ..., deprecated_archive_logs_info: _Optional[_Union[_oracle_sql_pb2.ArchiveLogsInfo, _Mapping]] = ...) -> None: ...

class VerificationInfo(_message.Message):
    __slots__ = ("database_info_vec", "query_oracle_warning", "query_oracle_info", "host_summary")
    ORACLE_VERIFICATION_INFO_FIELD_NUMBER: _ClassVar[int]
    oracle_verification_info: _descriptor.FieldDescriptor
    DATABASE_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    QUERY_ORACLE_WARNING_FIELD_NUMBER: _ClassVar[int]
    QUERY_ORACLE_INFO_FIELD_NUMBER: _ClassVar[int]
    HOST_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    database_info_vec: _containers.RepeatedCompositeFieldContainer[DatabaseBackupInfo]
    query_oracle_warning: _error_pb2.ErrorProto
    query_oracle_info: str
    host_summary: _agent_pb2.HostInfoSummary
    def __init__(self, database_info_vec: _Optional[_Iterable[_Union[DatabaseBackupInfo, _Mapping]]] = ..., query_oracle_warning: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., query_oracle_info: _Optional[str] = ..., host_summary: _Optional[_Union[_agent_pb2.HostInfoSummary, _Mapping]] = ...) -> None: ...

class EntityInfo(_message.Message):
    __slots__ = ("host_id", "view_name", "view_id", "database_info_vec", "whitelisted_host_ip_vec", "view_fs_path")
    class DatabaseInfo(_message.Message):
        __slots__ = ("db_id", "relative_db_dir")
        DB_ID_FIELD_NUMBER: _ClassVar[int]
        RELATIVE_DB_DIR_FIELD_NUMBER: _ClassVar[int]
        db_id: str
        relative_db_dir: str
        def __init__(self, db_id: _Optional[str] = ..., relative_db_dir: _Optional[str] = ...) -> None: ...
    HOST_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    VIEW_ID_FIELD_NUMBER: _ClassVar[int]
    DATABASE_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    WHITELISTED_HOST_IP_VEC_FIELD_NUMBER: _ClassVar[int]
    VIEW_FS_PATH_FIELD_NUMBER: _ClassVar[int]
    host_id: int
    view_name: str
    view_id: int
    database_info_vec: _containers.RepeatedCompositeFieldContainer[EntityInfo.DatabaseInfo]
    whitelisted_host_ip_vec: _containers.RepeatedScalarFieldContainer[str]
    view_fs_path: str
    def __init__(self, host_id: _Optional[int] = ..., view_name: _Optional[str] = ..., view_id: _Optional[int] = ..., database_info_vec: _Optional[_Iterable[_Union[EntityInfo.DatabaseInfo, _Mapping]]] = ..., whitelisted_host_ip_vec: _Optional[_Iterable[str]] = ..., view_fs_path: _Optional[str] = ...) -> None: ...

class OracleDBHostsInfo(_message.Message):
    __slots__ = ("ip_addr_vec", "index_vec")
    IP_ADDR_VEC_FIELD_NUMBER: _ClassVar[int]
    INDEX_VEC_FIELD_NUMBER: _ClassVar[int]
    ip_addr_vec: _containers.RepeatedScalarFieldContainer[str]
    index_vec: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, ip_addr_vec: _Optional[_Iterable[str]] = ..., index_vec: _Optional[_Iterable[int]] = ...) -> None: ...

class OracleHostMountInfo(_message.Message):
    __slots__ = ("mount_points_vec", "num_cpu")
    MOUNT_POINTS_VEC_FIELD_NUMBER: _ClassVar[int]
    NUM_CPU_FIELD_NUMBER: _ClassVar[int]
    mount_points_vec: _containers.RepeatedScalarFieldContainer[str]
    num_cpu: int
    def __init__(self, mount_points_vec: _Optional[_Iterable[str]] = ..., num_cpu: _Optional[int] = ...) -> None: ...

class SnapshotInfo(_message.Message):
    __slots__ = ("status", "database_info_vec", "job_instance_id", "attempt_num", "previous_entity_info", "current_entity_info", "backup_job_db_vec", "backup_all_dbs_in_job", "backup_all_dbs_in_run", "mount_points_vec", "sub_tasks_vec", "error", "discovery_done", "host_to_mount_info_map", "db_to_hosts_info_map", "lock_db_entities", "parallel_log_backup_enabled", "dbconfig_in_liveview", "host_ip_addr")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kStarted: _ClassVar[SnapshotInfo.Status]
        kViewCreated: _ClassVar[SnapshotInfo.Status]
        kDbsDiscovered: _ClassVar[SnapshotInfo.Status]
        kSetupDirsFinished: _ClassVar[SnapshotInfo.Status]
        kViewMounted: _ClassVar[SnapshotInfo.Status]
        kSubTaskCreated: _ClassVar[SnapshotInfo.Status]
        kDataFileCopyDone: _ClassVar[SnapshotInfo.Status]
        kLogGapInfoFetched: _ClassVar[SnapshotInfo.Status]
        kSubTasksFinished: _ClassVar[SnapshotInfo.Status]
        kViewCloned: _ClassVar[SnapshotInfo.Status]
        kFilesDeleted: _ClassVar[SnapshotInfo.Status]
    kStarted: SnapshotInfo.Status
    kViewCreated: SnapshotInfo.Status
    kDbsDiscovered: SnapshotInfo.Status
    kSetupDirsFinished: SnapshotInfo.Status
    kViewMounted: SnapshotInfo.Status
    kSubTaskCreated: SnapshotInfo.Status
    kDataFileCopyDone: SnapshotInfo.Status
    kLogGapInfoFetched: SnapshotInfo.Status
    kSubTasksFinished: SnapshotInfo.Status
    kViewCloned: SnapshotInfo.Status
    kFilesDeleted: SnapshotInfo.Status
    class DatabaseInfo(_message.Message):
        __slots__ = ("current_backup_info", "previous_backup_info")
        CURRENT_BACKUP_INFO_FIELD_NUMBER: _ClassVar[int]
        PREVIOUS_BACKUP_INFO_FIELD_NUMBER: _ClassVar[int]
        current_backup_info: DatabaseBackupInfo
        previous_backup_info: DatabaseBackupInfo
        def __init__(self, current_backup_info: _Optional[_Union[DatabaseBackupInfo, _Mapping]] = ..., previous_backup_info: _Optional[_Union[DatabaseBackupInfo, _Mapping]] = ...) -> None: ...
    class HostToMountInfoMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: OracleHostMountInfo
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[OracleHostMountInfo, _Mapping]] = ...) -> None: ...
    class DbToHostsInfoMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: OracleDBHostsInfo
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[OracleDBHostsInfo, _Mapping]] = ...) -> None: ...
    ORACLE_SNAPSHOT_INFO_FIELD_NUMBER: _ClassVar[int]
    oracle_snapshot_info: _descriptor.FieldDescriptor
    STATUS_FIELD_NUMBER: _ClassVar[int]
    DATABASE_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    JOB_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    ATTEMPT_NUM_FIELD_NUMBER: _ClassVar[int]
    PREVIOUS_ENTITY_INFO_FIELD_NUMBER: _ClassVar[int]
    CURRENT_ENTITY_INFO_FIELD_NUMBER: _ClassVar[int]
    BACKUP_JOB_DB_VEC_FIELD_NUMBER: _ClassVar[int]
    BACKUP_ALL_DBS_IN_JOB_FIELD_NUMBER: _ClassVar[int]
    BACKUP_ALL_DBS_IN_RUN_FIELD_NUMBER: _ClassVar[int]
    MOUNT_POINTS_VEC_FIELD_NUMBER: _ClassVar[int]
    SUB_TASKS_VEC_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    DISCOVERY_DONE_FIELD_NUMBER: _ClassVar[int]
    HOST_TO_MOUNT_INFO_MAP_FIELD_NUMBER: _ClassVar[int]
    DB_TO_HOSTS_INFO_MAP_FIELD_NUMBER: _ClassVar[int]
    LOCK_DB_ENTITIES_FIELD_NUMBER: _ClassVar[int]
    PARALLEL_LOG_BACKUP_ENABLED_FIELD_NUMBER: _ClassVar[int]
    DBCONFIG_IN_LIVEVIEW_FIELD_NUMBER: _ClassVar[int]
    HOST_IP_ADDR_FIELD_NUMBER: _ClassVar[int]
    status: SnapshotInfo.Status
    database_info_vec: _containers.RepeatedCompositeFieldContainer[SnapshotInfo.DatabaseInfo]
    job_instance_id: int
    attempt_num: int
    previous_entity_info: EntityInfo
    current_entity_info: EntityInfo
    backup_job_db_vec: _containers.RepeatedScalarFieldContainer[str]
    backup_all_dbs_in_job: bool
    backup_all_dbs_in_run: bool
    mount_points_vec: _containers.RepeatedScalarFieldContainer[str]
    sub_tasks_vec: _containers.RepeatedCompositeFieldContainer[_sub_task_pb2.SubTaskInfo]
    error: _error_pb2.ErrorProto
    discovery_done: bool
    host_to_mount_info_map: _containers.MessageMap[str, OracleHostMountInfo]
    db_to_hosts_info_map: _containers.MessageMap[str, OracleDBHostsInfo]
    lock_db_entities: bool
    parallel_log_backup_enabled: bool
    dbconfig_in_liveview: bool
    host_ip_addr: str
    def __init__(self, status: _Optional[_Union[SnapshotInfo.Status, str]] = ..., database_info_vec: _Optional[_Iterable[_Union[SnapshotInfo.DatabaseInfo, _Mapping]]] = ..., job_instance_id: _Optional[int] = ..., attempt_num: _Optional[int] = ..., previous_entity_info: _Optional[_Union[EntityInfo, _Mapping]] = ..., current_entity_info: _Optional[_Union[EntityInfo, _Mapping]] = ..., backup_job_db_vec: _Optional[_Iterable[str]] = ..., backup_all_dbs_in_job: bool = ..., backup_all_dbs_in_run: bool = ..., mount_points_vec: _Optional[_Iterable[str]] = ..., sub_tasks_vec: _Optional[_Iterable[_Union[_sub_task_pb2.SubTaskInfo, _Mapping]]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., discovery_done: bool = ..., host_to_mount_info_map: _Optional[_Mapping[str, OracleHostMountInfo]] = ..., db_to_hosts_info_map: _Optional[_Mapping[str, OracleDBHostsInfo]] = ..., lock_db_entities: bool = ..., parallel_log_backup_enabled: bool = ..., dbconfig_in_liveview: bool = ..., host_ip_addr: _Optional[str] = ...) -> None: ...

class OracleSubTaskInfo(_message.Message):
    __slots__ = ("database_idx", "permit_granted", "start_time_usecs", "end_time_usecs", "progress_monitor_path")
    ORACLE_SUB_TASK_INFO_FIELD_NUMBER: _ClassVar[int]
    oracle_sub_task_info: _descriptor.FieldDescriptor
    DATABASE_IDX_FIELD_NUMBER: _ClassVar[int]
    PERMIT_GRANTED_FIELD_NUMBER: _ClassVar[int]
    START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    END_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_MONITOR_PATH_FIELD_NUMBER: _ClassVar[int]
    database_idx: int
    permit_granted: bool
    start_time_usecs: int
    end_time_usecs: int
    progress_monitor_path: str
    def __init__(self, database_idx: _Optional[int] = ..., permit_granted: bool = ..., start_time_usecs: _Optional[int] = ..., end_time_usecs: _Optional[int] = ..., progress_monitor_path: _Optional[str] = ...) -> None: ...

class OracleAdditionalRunInfo(_message.Message):
    __slots__ = ("entity_info_vec",)
    ORACLE_ADDITIONAL_RUN_INFO_FIELD_NUMBER: _ClassVar[int]
    oracle_additional_run_info: _descriptor.FieldDescriptor
    ENTITY_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    entity_info_vec: _containers.RepeatedCompositeFieldContainer[EntityInfo]
    def __init__(self, entity_info_vec: _Optional[_Iterable[_Union[EntityInfo, _Mapping]]] = ...) -> None: ...

class DBMetaInfo(_message.Message):
    __slots__ = ("first_scn", "last_scn", "reset_logs_id")
    FIRST_SCN_FIELD_NUMBER: _ClassVar[int]
    LAST_SCN_FIELD_NUMBER: _ClassVar[int]
    RESET_LOGS_ID_FIELD_NUMBER: _ClassVar[int]
    first_scn: int
    last_scn: int
    reset_logs_id: int
    def __init__(self, first_scn: _Optional[int] = ..., last_scn: _Optional[int] = ..., reset_logs_id: _Optional[int] = ...) -> None: ...

class DatabaseRestoreInfo(_message.Message):
    __slots__ = ("db_backup_info", "backup_view_name", "backup_run_id", "relative_path", "backup_type", "clone_done", "catalog_done", "uncatalog_done", "run_meta_info_vec", "copy_datafile", "copy_controlfile", "db_reset_logs_id")
    DB_BACKUP_INFO_FIELD_NUMBER: _ClassVar[int]
    BACKUP_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    BACKUP_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    RELATIVE_PATH_FIELD_NUMBER: _ClassVar[int]
    BACKUP_TYPE_FIELD_NUMBER: _ClassVar[int]
    CLONE_DONE_FIELD_NUMBER: _ClassVar[int]
    CATALOG_DONE_FIELD_NUMBER: _ClassVar[int]
    UNCATALOG_DONE_FIELD_NUMBER: _ClassVar[int]
    RUN_META_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    COPY_DATAFILE_FIELD_NUMBER: _ClassVar[int]
    COPY_CONTROLFILE_FIELD_NUMBER: _ClassVar[int]
    DB_RESET_LOGS_ID_FIELD_NUMBER: _ClassVar[int]
    db_backup_info: DatabaseBackupInfo
    backup_view_name: str
    backup_run_id: int
    relative_path: str
    backup_type: _enums_pb2.ScheduledBackupType.Type
    clone_done: bool
    catalog_done: bool
    uncatalog_done: bool
    run_meta_info_vec: _containers.RepeatedCompositeFieldContainer[DBMetaInfo]
    copy_datafile: bool
    copy_controlfile: bool
    db_reset_logs_id: int
    def __init__(self, db_backup_info: _Optional[_Union[DatabaseBackupInfo, _Mapping]] = ..., backup_view_name: _Optional[str] = ..., backup_run_id: _Optional[int] = ..., relative_path: _Optional[str] = ..., backup_type: _Optional[_Union[_enums_pb2.ScheduledBackupType.Type, str]] = ..., clone_done: bool = ..., catalog_done: bool = ..., uncatalog_done: bool = ..., run_meta_info_vec: _Optional[_Iterable[_Union[DBMetaInfo, _Mapping]]] = ..., copy_datafile: bool = ..., copy_controlfile: bool = ..., db_reset_logs_id: _Optional[int] = ...) -> None: ...

class RestoreInfo(_message.Message):
    __slots__ = ("restore_task_state", "restore_time", "timezone_difference", "alternate_location_params", "db_restore_info_vec", "error", "no_open_mode", "backup_job_id", "destroy_clone_task_info", "migrate_clone_task_info", "is_migration_subtask", "cloned_db_info_vec", "restore_proto_version", "host_to_mount_info_map", "db_to_hosts_info_map", "oracle_target_params", "cloned_data_file_info_map", "oracle_clone_app_view_params_vec", "lock_db_entities", "oracle_restore_to_same_host", "shell_environment_vec", "granular_restore_info", "granular_clone_completed", "skip_clone_nid", "roll_forward_log_path_vec", "attempt_complete_recovery", "roll_forward_time_msecs", "oracle_archive_log_restore_info", "restore_scn", "oracle_recovery_validation_info", "restore_spfile_or_pfile_info", "use_scn_for_restore", "stop_active_passive", "same_config_ir_recovery_options", "restore_as_rac", "incarnation_id", "mount_points_vec", "control_file", "control_file_backup_run_id", "host_ip_addr", "catalog_index")
    class RestoreTaskState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kStarted: _ClassVar[RestoreInfo.RestoreTaskState]
        kBackupFilesCloned: _ClassVar[RestoreInfo.RestoreTaskState]
        kViewMounted: _ClassVar[RestoreInfo.RestoreTaskState]
        kRestorePrecheckInProgress: _ClassVar[RestoreInfo.RestoreTaskState]
        kControlFileRestored: _ClassVar[RestoreInfo.RestoreTaskState]
        kCatalogDone: _ClassVar[RestoreInfo.RestoreTaskState]
        kRestoreDBDone: _ClassVar[RestoreInfo.RestoreTaskState]
        kPostAltRestoreDBDone: _ClassVar[RestoreInfo.RestoreTaskState]
        kUnCatalogDone: _ClassVar[RestoreInfo.RestoreTaskState]
        kViewUnmounted: _ClassVar[RestoreInfo.RestoreTaskState]
        kRestoreLogsCopied: _ClassVar[RestoreInfo.RestoreTaskState]
        kFinished: _ClassVar[RestoreInfo.RestoreTaskState]
        kDBConfigFetched: _ClassVar[RestoreInfo.RestoreTaskState]
    kStarted: RestoreInfo.RestoreTaskState
    kBackupFilesCloned: RestoreInfo.RestoreTaskState
    kViewMounted: RestoreInfo.RestoreTaskState
    kRestorePrecheckInProgress: RestoreInfo.RestoreTaskState
    kControlFileRestored: RestoreInfo.RestoreTaskState
    kCatalogDone: RestoreInfo.RestoreTaskState
    kRestoreDBDone: RestoreInfo.RestoreTaskState
    kPostAltRestoreDBDone: RestoreInfo.RestoreTaskState
    kUnCatalogDone: RestoreInfo.RestoreTaskState
    kViewUnmounted: RestoreInfo.RestoreTaskState
    kRestoreLogsCopied: RestoreInfo.RestoreTaskState
    kFinished: RestoreInfo.RestoreTaskState
    kDBConfigFetched: RestoreInfo.RestoreTaskState
    class HostToMountInfoMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: OracleHostMountInfo
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[OracleHostMountInfo, _Mapping]] = ...) -> None: ...
    class DbToHostsInfoMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: OracleDBHostsInfo
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[OracleDBHostsInfo, _Mapping]] = ...) -> None: ...
    class ClonedDataFileInfoMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ORACLE_RESTORE_INFO_FIELD_NUMBER: _ClassVar[int]
    oracle_restore_info: _descriptor.FieldDescriptor
    RESTORE_TASK_STATE_FIELD_NUMBER: _ClassVar[int]
    RESTORE_TIME_FIELD_NUMBER: _ClassVar[int]
    TIMEZONE_DIFFERENCE_FIELD_NUMBER: _ClassVar[int]
    ALTERNATE_LOCATION_PARAMS_FIELD_NUMBER: _ClassVar[int]
    DB_RESTORE_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    NO_OPEN_MODE_FIELD_NUMBER: _ClassVar[int]
    BACKUP_JOB_ID_FIELD_NUMBER: _ClassVar[int]
    DESTROY_CLONE_TASK_INFO_FIELD_NUMBER: _ClassVar[int]
    MIGRATE_CLONE_TASK_INFO_FIELD_NUMBER: _ClassVar[int]
    IS_MIGRATION_SUBTASK_FIELD_NUMBER: _ClassVar[int]
    CLONED_DB_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    RESTORE_PROTO_VERSION_FIELD_NUMBER: _ClassVar[int]
    HOST_TO_MOUNT_INFO_MAP_FIELD_NUMBER: _ClassVar[int]
    DB_TO_HOSTS_INFO_MAP_FIELD_NUMBER: _ClassVar[int]
    ORACLE_TARGET_PARAMS_FIELD_NUMBER: _ClassVar[int]
    CLONED_DATA_FILE_INFO_MAP_FIELD_NUMBER: _ClassVar[int]
    ORACLE_CLONE_APP_VIEW_PARAMS_VEC_FIELD_NUMBER: _ClassVar[int]
    LOCK_DB_ENTITIES_FIELD_NUMBER: _ClassVar[int]
    ORACLE_RESTORE_TO_SAME_HOST_FIELD_NUMBER: _ClassVar[int]
    SHELL_ENVIRONMENT_VEC_FIELD_NUMBER: _ClassVar[int]
    GRANULAR_RESTORE_INFO_FIELD_NUMBER: _ClassVar[int]
    GRANULAR_CLONE_COMPLETED_FIELD_NUMBER: _ClassVar[int]
    SKIP_CLONE_NID_FIELD_NUMBER: _ClassVar[int]
    ROLL_FORWARD_LOG_PATH_VEC_FIELD_NUMBER: _ClassVar[int]
    ATTEMPT_COMPLETE_RECOVERY_FIELD_NUMBER: _ClassVar[int]
    ROLL_FORWARD_TIME_MSECS_FIELD_NUMBER: _ClassVar[int]
    ORACLE_ARCHIVE_LOG_RESTORE_INFO_FIELD_NUMBER: _ClassVar[int]
    RESTORE_SCN_FIELD_NUMBER: _ClassVar[int]
    ORACLE_RECOVERY_VALIDATION_INFO_FIELD_NUMBER: _ClassVar[int]
    RESTORE_SPFILE_OR_PFILE_INFO_FIELD_NUMBER: _ClassVar[int]
    USE_SCN_FOR_RESTORE_FIELD_NUMBER: _ClassVar[int]
    STOP_ACTIVE_PASSIVE_FIELD_NUMBER: _ClassVar[int]
    SAME_CONFIG_IR_RECOVERY_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    RESTORE_AS_RAC_FIELD_NUMBER: _ClassVar[int]
    INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    MOUNT_POINTS_VEC_FIELD_NUMBER: _ClassVar[int]
    CONTROL_FILE_FIELD_NUMBER: _ClassVar[int]
    CONTROL_FILE_BACKUP_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    HOST_IP_ADDR_FIELD_NUMBER: _ClassVar[int]
    CATALOG_INDEX_FIELD_NUMBER: _ClassVar[int]
    restore_task_state: RestoreInfo.RestoreTaskState
    restore_time: str
    timezone_difference: int
    alternate_location_params: _magneto_pb2.RestoreOracleAppObjectParams.AlternateLocationParams
    db_restore_info_vec: _containers.RepeatedCompositeFieldContainer[DatabaseRestoreInfo]
    error: _error_pb2.ErrorProto
    no_open_mode: bool
    backup_job_id: int
    destroy_clone_task_info: DestroyCloneTaskInfo
    migrate_clone_task_info: MigrateOracleCloneTaskInfo
    is_migration_subtask: bool
    cloned_db_info_vec: _containers.RepeatedCompositeFieldContainer[ClonedDBInfo]
    restore_proto_version: int
    host_to_mount_info_map: _containers.MessageMap[str, OracleHostMountInfo]
    db_to_hosts_info_map: _containers.MessageMap[str, OracleDBHostsInfo]
    oracle_target_params: _env_params_pb2_1.OracleSourceParams
    cloned_data_file_info_map: _containers.ScalarMap[str, str]
    oracle_clone_app_view_params_vec: _containers.RepeatedCompositeFieldContainer[_magneto_pb2.CloneAppViewParams]
    lock_db_entities: bool
    oracle_restore_to_same_host: bool
    shell_environment_vec: _containers.RepeatedCompositeFieldContainer[_magneto_pb2.RestoreOracleAppObjectParams.KeyValuePair]
    granular_restore_info: _magneto_pb2.GranularRestoreInfo
    granular_clone_completed: bool
    skip_clone_nid: bool
    roll_forward_log_path_vec: _containers.RepeatedScalarFieldContainer[str]
    attempt_complete_recovery: bool
    roll_forward_time_msecs: int
    oracle_archive_log_restore_info: _magneto_pb2.OracleArchiveLogInfo
    restore_scn: int
    oracle_recovery_validation_info: _magneto_pb2.OracleRecoveryValidationInfo
    restore_spfile_or_pfile_info: _magneto_pb2.RestoreSpfileOrPfileInfo
    use_scn_for_restore: bool
    stop_active_passive: bool
    same_config_ir_recovery_options: _oracle_pb2.SameConfigIrRecoveryOptions
    restore_as_rac: bool
    incarnation_id: int
    mount_points_vec: _containers.RepeatedScalarFieldContainer[str]
    control_file: str
    control_file_backup_run_id: int
    host_ip_addr: str
    catalog_index: int
    def __init__(self, restore_task_state: _Optional[_Union[RestoreInfo.RestoreTaskState, str]] = ..., restore_time: _Optional[str] = ..., timezone_difference: _Optional[int] = ..., alternate_location_params: _Optional[_Union[_magneto_pb2.RestoreOracleAppObjectParams.AlternateLocationParams, _Mapping]] = ..., db_restore_info_vec: _Optional[_Iterable[_Union[DatabaseRestoreInfo, _Mapping]]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., no_open_mode: bool = ..., backup_job_id: _Optional[int] = ..., destroy_clone_task_info: _Optional[_Union[DestroyCloneTaskInfo, _Mapping]] = ..., migrate_clone_task_info: _Optional[_Union[MigrateOracleCloneTaskInfo, _Mapping]] = ..., is_migration_subtask: bool = ..., cloned_db_info_vec: _Optional[_Iterable[_Union[ClonedDBInfo, _Mapping]]] = ..., restore_proto_version: _Optional[int] = ..., host_to_mount_info_map: _Optional[_Mapping[str, OracleHostMountInfo]] = ..., db_to_hosts_info_map: _Optional[_Mapping[str, OracleDBHostsInfo]] = ..., oracle_target_params: _Optional[_Union[_env_params_pb2_1.OracleSourceParams, _Mapping]] = ..., cloned_data_file_info_map: _Optional[_Mapping[str, str]] = ..., oracle_clone_app_view_params_vec: _Optional[_Iterable[_Union[_magneto_pb2.CloneAppViewParams, _Mapping]]] = ..., lock_db_entities: bool = ..., oracle_restore_to_same_host: bool = ..., shell_environment_vec: _Optional[_Iterable[_Union[_magneto_pb2.RestoreOracleAppObjectParams.KeyValuePair, _Mapping]]] = ..., granular_restore_info: _Optional[_Union[_magneto_pb2.GranularRestoreInfo, _Mapping]] = ..., granular_clone_completed: bool = ..., skip_clone_nid: bool = ..., roll_forward_log_path_vec: _Optional[_Iterable[str]] = ..., attempt_complete_recovery: bool = ..., roll_forward_time_msecs: _Optional[int] = ..., oracle_archive_log_restore_info: _Optional[_Union[_magneto_pb2.OracleArchiveLogInfo, _Mapping]] = ..., restore_scn: _Optional[int] = ..., oracle_recovery_validation_info: _Optional[_Union[_magneto_pb2.OracleRecoveryValidationInfo, _Mapping]] = ..., restore_spfile_or_pfile_info: _Optional[_Union[_magneto_pb2.RestoreSpfileOrPfileInfo, _Mapping]] = ..., use_scn_for_restore: bool = ..., stop_active_passive: bool = ..., same_config_ir_recovery_options: _Optional[_Union[_oracle_pb2.SameConfigIrRecoveryOptions, _Mapping]] = ..., restore_as_rac: bool = ..., incarnation_id: _Optional[int] = ..., mount_points_vec: _Optional[_Iterable[str]] = ..., control_file: _Optional[str] = ..., control_file_backup_run_id: _Optional[int] = ..., host_ip_addr: _Optional[str] = ..., catalog_index: _Optional[int] = ...) -> None: ...

class ClonedDBInfo(_message.Message):
    __slots__ = ("db_name", "db_sid", "oracle_home", "db_entity_info", "uuid", "dropped_successfully", "error")
    DB_NAME_FIELD_NUMBER: _ClassVar[int]
    DB_SID_FIELD_NUMBER: _ClassVar[int]
    ORACLE_HOME_FIELD_NUMBER: _ClassVar[int]
    DB_ENTITY_INFO_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    DROPPED_SUCCESSFULLY_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    db_name: str
    db_sid: str
    oracle_home: str
    db_entity_info: _oracle_pb2_1.DBEntityInfo
    uuid: str
    dropped_successfully: bool
    error: _error_pb2.ErrorProto
    def __init__(self, db_name: _Optional[str] = ..., db_sid: _Optional[str] = ..., oracle_home: _Optional[str] = ..., db_entity_info: _Optional[_Union[_oracle_pb2_1.DBEntityInfo, _Mapping]] = ..., uuid: _Optional[str] = ..., dropped_successfully: bool = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class DestroyCloneTaskInfo(_message.Message):
    __slots__ = ("host_identifier", "mountpoint_identifier", "mountpoint_basedir", "view_name", "destroy_task_state", "cloned_db_info_vec", "view_mount_subdir_identifier", "remote_host_identifiers_vec")
    class DestroyTaskState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kStarted: _ClassVar[DestroyCloneTaskInfo.DestroyTaskState]
        kDropDBsDone: _ClassVar[DestroyCloneTaskInfo.DestroyTaskState]
        kViewUnmounted: _ClassVar[DestroyCloneTaskInfo.DestroyTaskState]
    kStarted: DestroyCloneTaskInfo.DestroyTaskState
    kDropDBsDone: DestroyCloneTaskInfo.DestroyTaskState
    kViewUnmounted: DestroyCloneTaskInfo.DestroyTaskState
    ORACLE_DESTROY_CLONE_APP_TASK_INFO_FIELD_NUMBER: _ClassVar[int]
    oracle_destroy_clone_app_task_info: _descriptor.FieldDescriptor
    HOST_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    MOUNTPOINT_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    MOUNTPOINT_BASEDIR_FIELD_NUMBER: _ClassVar[int]
    VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    DESTROY_TASK_STATE_FIELD_NUMBER: _ClassVar[int]
    CLONED_DB_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    VIEW_MOUNT_SUBDIR_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    REMOTE_HOST_IDENTIFIERS_VEC_FIELD_NUMBER: _ClassVar[int]
    host_identifier: str
    mountpoint_identifier: str
    mountpoint_basedir: str
    view_name: str
    destroy_task_state: DestroyCloneTaskInfo.DestroyTaskState
    cloned_db_info_vec: _containers.RepeatedCompositeFieldContainer[ClonedDBInfo]
    view_mount_subdir_identifier: str
    remote_host_identifiers_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, host_identifier: _Optional[str] = ..., mountpoint_identifier: _Optional[str] = ..., mountpoint_basedir: _Optional[str] = ..., view_name: _Optional[str] = ..., destroy_task_state: _Optional[_Union[DestroyCloneTaskInfo.DestroyTaskState, str]] = ..., cloned_db_info_vec: _Optional[_Iterable[_Union[ClonedDBInfo, _Mapping]]] = ..., view_mount_subdir_identifier: _Optional[str] = ..., remote_host_identifiers_vec: _Optional[_Iterable[str]] = ...) -> None: ...

class MigrateOracleCloneTaskInfo(_message.Message):
    __slots__ = ("error", "migrate_clone_task_state", "migrate_clone_params")
    class MigrateCloneTaskState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kStarted: _ClassVar[MigrateOracleCloneTaskInfo.MigrateCloneTaskState]
        kPrecheckDone: _ClassVar[MigrateOracleCloneTaskInfo.MigrateCloneTaskState]
        kDBMigrateDone: _ClassVar[MigrateOracleCloneTaskInfo.MigrateCloneTaskState]
        kViewUnmounted: _ClassVar[MigrateOracleCloneTaskInfo.MigrateCloneTaskState]
    kStarted: MigrateOracleCloneTaskInfo.MigrateCloneTaskState
    kPrecheckDone: MigrateOracleCloneTaskInfo.MigrateCloneTaskState
    kDBMigrateDone: MigrateOracleCloneTaskInfo.MigrateCloneTaskState
    kViewUnmounted: MigrateOracleCloneTaskInfo.MigrateCloneTaskState
    ERROR_FIELD_NUMBER: _ClassVar[int]
    MIGRATE_CLONE_TASK_STATE_FIELD_NUMBER: _ClassVar[int]
    MIGRATE_CLONE_PARAMS_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    migrate_clone_task_state: MigrateOracleCloneTaskInfo.MigrateCloneTaskState
    migrate_clone_params: _magneto_pb2.MigrateOracleCloneParams
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., migrate_clone_task_state: _Optional[_Union[MigrateOracleCloneTaskInfo.MigrateCloneTaskState, str]] = ..., migrate_clone_params: _Optional[_Union[_magneto_pb2.MigrateOracleCloneParams, _Mapping]] = ...) -> None: ...

class SelfSufficiencyLogInfo(_message.Message):
    __slots__ = ("clone_logs_info_vec", "archivelog_base_time", "error")
    class CloneLogsInfo(_message.Message):
        __slots__ = ("view_name", "relative_db_dir", "run_start_time_usecs")
        VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
        RELATIVE_DB_DIR_FIELD_NUMBER: _ClassVar[int]
        RUN_START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
        view_name: str
        relative_db_dir: str
        run_start_time_usecs: int
        def __init__(self, view_name: _Optional[str] = ..., relative_db_dir: _Optional[str] = ..., run_start_time_usecs: _Optional[int] = ...) -> None: ...
    CLONE_LOGS_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    ARCHIVELOG_BASE_TIME_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    clone_logs_info_vec: _containers.RepeatedCompositeFieldContainer[SelfSufficiencyLogInfo.CloneLogsInfo]
    archivelog_base_time: str
    error: _error_pb2.ErrorProto
    def __init__(self, clone_logs_info_vec: _Optional[_Iterable[_Union[SelfSufficiencyLogInfo.CloneLogsInfo, _Mapping]]] = ..., archivelog_base_time: _Optional[str] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...
