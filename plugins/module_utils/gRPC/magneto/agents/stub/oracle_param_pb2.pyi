from bifrost.server import server_config_pb2 as _server_config_pb2
from magneto.agents.base import agent_pb2 as _agent_pb2
from magneto.agents.base import error_pb2 as _error_pb2
from magneto.agents.base import oracle_pb2 as _oracle_pb2
from magneto.agents.base import oracle_sql_pb2 as _oracle_sql_pb2
from magneto.agents.stub import agent_base_pb2 as _agent_base_pb2
from magneto.api.common import oracle_pb2 as _oracle_pb2_1
from magneto.base import enums_pb2 as _enums_pb2
from magneto.base import magneto_pb2 as _magneto_pb2
from magneto.base import env_params_pb2 as _env_params_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FileType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kDataFile: _ClassVar[FileType]
    kArchivedLogFile: _ClassVar[FileType]
    kBackupPiece: _ClassVar[FileType]
    kPfile: _ClassVar[FileType]
    kRacConfigFile: _ClassVar[FileType]
kDataFile: FileType
kArchivedLogFile: FileType
kBackupPiece: FileType
kPfile: FileType
kRacConfigFile: FileType

class DiscoverDBsArg(_message.Message):
    __slots__ = ("header", "auth_type", "username", "password", "encrypted_password", "host_type", "precheck_enabled", "db_sid_vec")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    AUTH_TYPE_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTED_PASSWORD_FIELD_NUMBER: _ClassVar[int]
    HOST_TYPE_FIELD_NUMBER: _ClassVar[int]
    PRECHECK_ENABLED_FIELD_NUMBER: _ClassVar[int]
    DB_SID_VEC_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    auth_type: _oracle_pb2.AuthType.Type
    username: str
    password: str
    encrypted_password: bytes
    host_type: _agent_pb2.ClusterNetworkingInfo.Resource.Type
    precheck_enabled: bool
    db_sid_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., auth_type: _Optional[_Union[_oracle_pb2.AuthType.Type, str]] = ..., username: _Optional[str] = ..., password: _Optional[str] = ..., encrypted_password: _Optional[bytes] = ..., host_type: _Optional[_Union[_agent_pb2.ClusterNetworkingInfo.Resource.Type, str]] = ..., precheck_enabled: bool = ..., db_sid_vec: _Optional[_Iterable[str]] = ...) -> None: ...

class DiscoverDBsResult(_message.Message):
    __slots__ = ("error", "db_info_vec", "host_precheck_result", "discover_db_precheck_result_vec")
    class DiscoverDBCheck(_message.Message):
        __slots__ = ("db_sid", "db_check_result")
        DB_SID_FIELD_NUMBER: _ClassVar[int]
        DB_CHECK_RESULT_FIELD_NUMBER: _ClassVar[int]
        db_sid: str
        db_check_result: PrecheckResult
        def __init__(self, db_sid: _Optional[str] = ..., db_check_result: _Optional[_Union[PrecheckResult, _Mapping]] = ...) -> None: ...
    ERROR_FIELD_NUMBER: _ClassVar[int]
    DB_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    HOST_PRECHECK_RESULT_FIELD_NUMBER: _ClassVar[int]
    DISCOVER_DB_PRECHECK_RESULT_VEC_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    db_info_vec: _containers.RepeatedCompositeFieldContainer[_oracle_pb2.DatabaseInfoProto]
    host_precheck_result: OracleEnvCheckResult
    discover_db_precheck_result_vec: _containers.RepeatedCompositeFieldContainer[DiscoverDBsResult.DiscoverDBCheck]
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., db_info_vec: _Optional[_Iterable[_Union[_oracle_pb2.DatabaseInfoProto, _Mapping]]] = ..., host_precheck_result: _Optional[_Union[OracleEnvCheckResult, _Mapping]] = ..., discover_db_precheck_result_vec: _Optional[_Iterable[_Union[DiscoverDBsResult.DiscoverDBCheck, _Mapping]]] = ...) -> None: ...

class RemoteMountInfo(_message.Message):
    __slots__ = ("fqdn", "port_num", "remote_mount_point_vec", "oracle_sid")
    FQDN_FIELD_NUMBER: _ClassVar[int]
    PORT_NUM_FIELD_NUMBER: _ClassVar[int]
    REMOTE_MOUNT_POINT_VEC_FIELD_NUMBER: _ClassVar[int]
    ORACLE_SID_FIELD_NUMBER: _ClassVar[int]
    fqdn: str
    port_num: str
    remote_mount_point_vec: _containers.RepeatedScalarFieldContainer[str]
    oracle_sid: str
    def __init__(self, fqdn: _Optional[str] = ..., port_num: _Optional[str] = ..., remote_mount_point_vec: _Optional[_Iterable[str]] = ..., oracle_sid: _Optional[str] = ...) -> None: ...

class BackupDBArg(_message.Message):
    __slots__ = ("header", "db_info", "job_id", "job_run_id", "attempt_number", "backup_type", "mount_path_vec", "remote_mount_info_vec", "archivelog_keep_days", "rman_backup_type", "host_info_vec", "mnmc_use_connect_dsc", "archivelog_base_time", "bifrost_server_config_proto", "archivelog_keep_hours", "skip_archivelog_backup", "log_filler_attempt_num", "dump_rac_config")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    DB_INFO_FIELD_NUMBER: _ClassVar[int]
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    JOB_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    ATTEMPT_NUMBER_FIELD_NUMBER: _ClassVar[int]
    BACKUP_TYPE_FIELD_NUMBER: _ClassVar[int]
    MOUNT_PATH_VEC_FIELD_NUMBER: _ClassVar[int]
    REMOTE_MOUNT_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    ARCHIVELOG_KEEP_DAYS_FIELD_NUMBER: _ClassVar[int]
    RMAN_BACKUP_TYPE_FIELD_NUMBER: _ClassVar[int]
    HOST_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    MNMC_USE_CONNECT_DSC_FIELD_NUMBER: _ClassVar[int]
    ARCHIVELOG_BASE_TIME_FIELD_NUMBER: _ClassVar[int]
    BIFROST_SERVER_CONFIG_PROTO_FIELD_NUMBER: _ClassVar[int]
    ARCHIVELOG_KEEP_HOURS_FIELD_NUMBER: _ClassVar[int]
    SKIP_ARCHIVELOG_BACKUP_FIELD_NUMBER: _ClassVar[int]
    LOG_FILLER_ATTEMPT_NUM_FIELD_NUMBER: _ClassVar[int]
    DUMP_RAC_CONFIG_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    db_info: _oracle_pb2.DatabaseInfoProto
    job_id: int
    job_run_id: int
    attempt_number: int
    backup_type: _enums_pb2.ScheduledBackupType.Type
    mount_path_vec: _containers.RepeatedScalarFieldContainer[str]
    remote_mount_info_vec: _containers.RepeatedCompositeFieldContainer[RemoteMountInfo]
    archivelog_keep_days: int
    rman_backup_type: _env_params_pb2.OracleRmanBackupType.Type
    host_info_vec: _containers.RepeatedCompositeFieldContainer[_env_params_pb2.OracleDBChannelInfo.HostInfo]
    mnmc_use_connect_dsc: bool
    archivelog_base_time: str
    bifrost_server_config_proto: _server_config_pb2.ServerConfigProto
    archivelog_keep_hours: int
    skip_archivelog_backup: bool
    log_filler_attempt_num: int
    dump_rac_config: bool
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., db_info: _Optional[_Union[_oracle_pb2.DatabaseInfoProto, _Mapping]] = ..., job_id: _Optional[int] = ..., job_run_id: _Optional[int] = ..., attempt_number: _Optional[int] = ..., backup_type: _Optional[_Union[_enums_pb2.ScheduledBackupType.Type, str]] = ..., mount_path_vec: _Optional[_Iterable[str]] = ..., remote_mount_info_vec: _Optional[_Iterable[_Union[RemoteMountInfo, _Mapping]]] = ..., archivelog_keep_days: _Optional[int] = ..., rman_backup_type: _Optional[_Union[_env_params_pb2.OracleRmanBackupType.Type, str]] = ..., host_info_vec: _Optional[_Iterable[_Union[_env_params_pb2.OracleDBChannelInfo.HostInfo, _Mapping]]] = ..., mnmc_use_connect_dsc: bool = ..., archivelog_base_time: _Optional[str] = ..., bifrost_server_config_proto: _Optional[_Union[_server_config_pb2.ServerConfigProto, _Mapping]] = ..., archivelog_keep_hours: _Optional[int] = ..., skip_archivelog_backup: bool = ..., log_filler_attempt_num: _Optional[int] = ..., dump_rac_config: bool = ...) -> None: ...

class BackupDBResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class BackupDBProgressArg(_message.Message):
    __slots__ = ("header", "db_info", "job_id", "job_run_id", "attempt_number", "backup_type", "mount_path_vec", "remote_mount_info_vec", "archivelog_keep_days", "rman_backup_type", "host_info_vec", "mnmc_use_connect_dsc", "archivelog_base_time", "bifrost_server_config_proto", "archivelog_keep_hours", "skip_archivelog_backup", "log_filler_attempt_num", "dump_rac_config")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    DB_INFO_FIELD_NUMBER: _ClassVar[int]
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    JOB_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    ATTEMPT_NUMBER_FIELD_NUMBER: _ClassVar[int]
    BACKUP_TYPE_FIELD_NUMBER: _ClassVar[int]
    MOUNT_PATH_VEC_FIELD_NUMBER: _ClassVar[int]
    REMOTE_MOUNT_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    ARCHIVELOG_KEEP_DAYS_FIELD_NUMBER: _ClassVar[int]
    RMAN_BACKUP_TYPE_FIELD_NUMBER: _ClassVar[int]
    HOST_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    MNMC_USE_CONNECT_DSC_FIELD_NUMBER: _ClassVar[int]
    ARCHIVELOG_BASE_TIME_FIELD_NUMBER: _ClassVar[int]
    BIFROST_SERVER_CONFIG_PROTO_FIELD_NUMBER: _ClassVar[int]
    ARCHIVELOG_KEEP_HOURS_FIELD_NUMBER: _ClassVar[int]
    SKIP_ARCHIVELOG_BACKUP_FIELD_NUMBER: _ClassVar[int]
    LOG_FILLER_ATTEMPT_NUM_FIELD_NUMBER: _ClassVar[int]
    DUMP_RAC_CONFIG_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    db_info: _oracle_pb2.DatabaseInfoProto
    job_id: int
    job_run_id: int
    attempt_number: int
    backup_type: _enums_pb2.ScheduledBackupType.Type
    mount_path_vec: _containers.RepeatedScalarFieldContainer[str]
    remote_mount_info_vec: _containers.RepeatedCompositeFieldContainer[RemoteMountInfo]
    archivelog_keep_days: int
    rman_backup_type: _env_params_pb2.OracleRmanBackupType.Type
    host_info_vec: _containers.RepeatedCompositeFieldContainer[_env_params_pb2.OracleDBChannelInfo.HostInfo]
    mnmc_use_connect_dsc: bool
    archivelog_base_time: str
    bifrost_server_config_proto: _server_config_pb2.ServerConfigProto
    archivelog_keep_hours: int
    skip_archivelog_backup: bool
    log_filler_attempt_num: int
    dump_rac_config: bool
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., db_info: _Optional[_Union[_oracle_pb2.DatabaseInfoProto, _Mapping]] = ..., job_id: _Optional[int] = ..., job_run_id: _Optional[int] = ..., attempt_number: _Optional[int] = ..., backup_type: _Optional[_Union[_enums_pb2.ScheduledBackupType.Type, str]] = ..., mount_path_vec: _Optional[_Iterable[str]] = ..., remote_mount_info_vec: _Optional[_Iterable[_Union[RemoteMountInfo, _Mapping]]] = ..., archivelog_keep_days: _Optional[int] = ..., rman_backup_type: _Optional[_Union[_env_params_pb2.OracleRmanBackupType.Type, str]] = ..., host_info_vec: _Optional[_Iterable[_Union[_env_params_pb2.OracleDBChannelInfo.HostInfo, _Mapping]]] = ..., mnmc_use_connect_dsc: bool = ..., archivelog_base_time: _Optional[str] = ..., bifrost_server_config_proto: _Optional[_Union[_server_config_pb2.ServerConfigProto, _Mapping]] = ..., archivelog_keep_hours: _Optional[int] = ..., skip_archivelog_backup: bool = ..., log_filler_attempt_num: _Optional[int] = ..., dump_rac_config: bool = ...) -> None: ...

class BackupDBProgressResult(_message.Message):
    __slots__ = ("error", "backup_completed", "backup_error", "total_bytes_read", "total_bytes_to_be_read", "total_bytes_write", "local_start_time", "local_end_time", "local_time_taken_secs", "incr_merge_percent", "data_files_info", "db_incarnation_info", "timezone_difference", "log_file_info", "backup_set_info", "rman_log_info_vec", "deprecated_archive_logs_info", "thread_info", "rac_config_file")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    BACKUP_COMPLETED_FIELD_NUMBER: _ClassVar[int]
    BACKUP_ERROR_FIELD_NUMBER: _ClassVar[int]
    TOTAL_BYTES_READ_FIELD_NUMBER: _ClassVar[int]
    TOTAL_BYTES_TO_BE_READ_FIELD_NUMBER: _ClassVar[int]
    TOTAL_BYTES_WRITE_FIELD_NUMBER: _ClassVar[int]
    LOCAL_START_TIME_FIELD_NUMBER: _ClassVar[int]
    LOCAL_END_TIME_FIELD_NUMBER: _ClassVar[int]
    LOCAL_TIME_TAKEN_SECS_FIELD_NUMBER: _ClassVar[int]
    INCR_MERGE_PERCENT_FIELD_NUMBER: _ClassVar[int]
    DATA_FILES_INFO_FIELD_NUMBER: _ClassVar[int]
    DB_INCARNATION_INFO_FIELD_NUMBER: _ClassVar[int]
    TIMEZONE_DIFFERENCE_FIELD_NUMBER: _ClassVar[int]
    LOG_FILE_INFO_FIELD_NUMBER: _ClassVar[int]
    BACKUP_SET_INFO_FIELD_NUMBER: _ClassVar[int]
    RMAN_LOG_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    DEPRECATED_ARCHIVE_LOGS_INFO_FIELD_NUMBER: _ClassVar[int]
    THREAD_INFO_FIELD_NUMBER: _ClassVar[int]
    RAC_CONFIG_FILE_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    backup_completed: bool
    backup_error: _error_pb2.ErrorProto
    total_bytes_read: int
    total_bytes_to_be_read: int
    total_bytes_write: int
    local_start_time: str
    local_end_time: str
    local_time_taken_secs: int
    incr_merge_percent: int
    data_files_info: _oracle_sql_pb2.DataFilesInfo
    db_incarnation_info: _oracle_sql_pb2.DatabaseIncarnationInfo
    timezone_difference: int
    log_file_info: _oracle_sql_pb2.LogFileInfo
    backup_set_info: _oracle_sql_pb2.BackupSetInfo
    rman_log_info_vec: _containers.RepeatedScalarFieldContainer[str]
    deprecated_archive_logs_info: _oracle_sql_pb2.ArchiveLogsInfo
    thread_info: _oracle_sql_pb2.ThreadInfo
    rac_config_file: str
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., backup_completed: bool = ..., backup_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., total_bytes_read: _Optional[int] = ..., total_bytes_to_be_read: _Optional[int] = ..., total_bytes_write: _Optional[int] = ..., local_start_time: _Optional[str] = ..., local_end_time: _Optional[str] = ..., local_time_taken_secs: _Optional[int] = ..., incr_merge_percent: _Optional[int] = ..., data_files_info: _Optional[_Union[_oracle_sql_pb2.DataFilesInfo, _Mapping]] = ..., db_incarnation_info: _Optional[_Union[_oracle_sql_pb2.DatabaseIncarnationInfo, _Mapping]] = ..., timezone_difference: _Optional[int] = ..., log_file_info: _Optional[_Union[_oracle_sql_pb2.LogFileInfo, _Mapping]] = ..., backup_set_info: _Optional[_Union[_oracle_sql_pb2.BackupSetInfo, _Mapping]] = ..., rman_log_info_vec: _Optional[_Iterable[str]] = ..., deprecated_archive_logs_info: _Optional[_Union[_oracle_sql_pb2.ArchiveLogsInfo, _Mapping]] = ..., thread_info: _Optional[_Union[_oracle_sql_pb2.ThreadInfo, _Mapping]] = ..., rac_config_file: _Optional[str] = ...) -> None: ...

class CancelDBBackupArg(_message.Message):
    __slots__ = ("header", "db_info", "attempt_number", "restore_cancel", "migrate_db_info", "kill_restore_rman_session", "log_filler_attempt_num")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    DB_INFO_FIELD_NUMBER: _ClassVar[int]
    ATTEMPT_NUMBER_FIELD_NUMBER: _ClassVar[int]
    RESTORE_CANCEL_FIELD_NUMBER: _ClassVar[int]
    MIGRATE_DB_INFO_FIELD_NUMBER: _ClassVar[int]
    KILL_RESTORE_RMAN_SESSION_FIELD_NUMBER: _ClassVar[int]
    LOG_FILLER_ATTEMPT_NUM_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    db_info: _oracle_pb2.DatabaseInfoProto
    attempt_number: int
    restore_cancel: bool
    migrate_db_info: MigrateDBInfo
    kill_restore_rman_session: bool
    log_filler_attempt_num: int
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., db_info: _Optional[_Union[_oracle_pb2.DatabaseInfoProto, _Mapping]] = ..., attempt_number: _Optional[int] = ..., restore_cancel: bool = ..., migrate_db_info: _Optional[_Union[MigrateDBInfo, _Mapping]] = ..., kill_restore_rman_session: bool = ..., log_filler_attempt_num: _Optional[int] = ...) -> None: ...

class CancelDBBackupResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class MountServerArg(_message.Message):
    __slots__ = ("server_addr", "server_path")
    SERVER_ADDR_FIELD_NUMBER: _ClassVar[int]
    SERVER_PATH_FIELD_NUMBER: _ClassVar[int]
    server_addr: str
    server_path: str
    def __init__(self, server_addr: _Optional[str] = ..., server_path: _Optional[str] = ...) -> None: ...

class MountOracleNASArg(_message.Message):
    __slots__ = ("header", "mountpoint_identifier", "server_arg_vec", "vlan_info_vec", "max_mount_point", "db_uuid_vec", "use_nolock", "use_noac", "view_mount_subdir_identifier", "relative_dir_vec", "skip_subnet_match")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    MOUNTPOINT_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    SERVER_ARG_VEC_FIELD_NUMBER: _ClassVar[int]
    VLAN_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    MAX_MOUNT_POINT_FIELD_NUMBER: _ClassVar[int]
    DB_UUID_VEC_FIELD_NUMBER: _ClassVar[int]
    USE_NOLOCK_FIELD_NUMBER: _ClassVar[int]
    USE_NOAC_FIELD_NUMBER: _ClassVar[int]
    VIEW_MOUNT_SUBDIR_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    RELATIVE_DIR_VEC_FIELD_NUMBER: _ClassVar[int]
    SKIP_SUBNET_MATCH_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    mountpoint_identifier: str
    server_arg_vec: _containers.RepeatedCompositeFieldContainer[MountServerArg]
    vlan_info_vec: _containers.RepeatedCompositeFieldContainer[_env_params_pb2.OracleVlanInfo]
    max_mount_point: int
    db_uuid_vec: _containers.RepeatedScalarFieldContainer[str]
    use_nolock: bool
    use_noac: bool
    view_mount_subdir_identifier: str
    relative_dir_vec: _containers.RepeatedScalarFieldContainer[str]
    skip_subnet_match: bool
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., mountpoint_identifier: _Optional[str] = ..., server_arg_vec: _Optional[_Iterable[_Union[MountServerArg, _Mapping]]] = ..., vlan_info_vec: _Optional[_Iterable[_Union[_env_params_pb2.OracleVlanInfo, _Mapping]]] = ..., max_mount_point: _Optional[int] = ..., db_uuid_vec: _Optional[_Iterable[str]] = ..., use_nolock: bool = ..., use_noac: bool = ..., view_mount_subdir_identifier: _Optional[str] = ..., relative_dir_vec: _Optional[_Iterable[str]] = ..., skip_subnet_match: bool = ...) -> None: ...

class MountOracleNASResult(_message.Message):
    __slots__ = ("error", "mount_info_vec")
    class MountInfo(_message.Message):
        __slots__ = ("server_arg", "mount_path", "mount_base_dir")
        SERVER_ARG_FIELD_NUMBER: _ClassVar[int]
        MOUNT_PATH_FIELD_NUMBER: _ClassVar[int]
        MOUNT_BASE_DIR_FIELD_NUMBER: _ClassVar[int]
        server_arg: MountServerArg
        mount_path: str
        mount_base_dir: str
        def __init__(self, server_arg: _Optional[_Union[MountServerArg, _Mapping]] = ..., mount_path: _Optional[str] = ..., mount_base_dir: _Optional[str] = ...) -> None: ...
    ERROR_FIELD_NUMBER: _ClassVar[int]
    MOUNT_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    mount_info_vec: _containers.RepeatedCompositeFieldContainer[MountOracleNASResult.MountInfo]
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., mount_info_vec: _Optional[_Iterable[_Union[MountOracleNASResult.MountInfo, _Mapping]]] = ...) -> None: ...

class UnMountOracleNASArg(_message.Message):
    __slots__ = ("header", "mountpoint_identifier", "view_mount_subdir_identifier", "mountpoint_basedir", "db_uuid_vec", "job_id", "remove_fstab_entry")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    MOUNTPOINT_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    VIEW_MOUNT_SUBDIR_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    MOUNTPOINT_BASEDIR_FIELD_NUMBER: _ClassVar[int]
    DB_UUID_VEC_FIELD_NUMBER: _ClassVar[int]
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    REMOVE_FSTAB_ENTRY_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    mountpoint_identifier: str
    view_mount_subdir_identifier: str
    mountpoint_basedir: str
    db_uuid_vec: _containers.RepeatedScalarFieldContainer[str]
    job_id: int
    remove_fstab_entry: bool
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., mountpoint_identifier: _Optional[str] = ..., view_mount_subdir_identifier: _Optional[str] = ..., mountpoint_basedir: _Optional[str] = ..., db_uuid_vec: _Optional[_Iterable[str]] = ..., job_id: _Optional[int] = ..., remove_fstab_entry: bool = ...) -> None: ...

class GetDBIncarnationInfoArg(_message.Message):
    __slots__ = ("header", "db_info")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    DB_INFO_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    db_info: _oracle_pb2.DatabaseInfoProto
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., db_info: _Optional[_Union[_oracle_pb2.DatabaseInfoProto, _Mapping]] = ...) -> None: ...

class GetDBIncarnationInfoResult(_message.Message):
    __slots__ = ("error", "database_incarnation_info", "timezone_difference")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    DATABASE_INCARNATION_INFO_FIELD_NUMBER: _ClassVar[int]
    TIMEZONE_DIFFERENCE_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    database_incarnation_info: _oracle_sql_pb2.DatabaseIncarnationInfo
    timezone_difference: int
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., database_incarnation_info: _Optional[_Union[_oracle_sql_pb2.DatabaseIncarnationInfo, _Mapping]] = ..., timezone_difference: _Optional[int] = ...) -> None: ...

class FileInfo(_message.Message):
    __slots__ = ("file_path", "file_type", "source_file_path")
    FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    FILE_TYPE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    file_path: str
    file_type: FileType
    source_file_path: str
    def __init__(self, file_path: _Optional[str] = ..., file_type: _Optional[_Union[FileType, str]] = ..., source_file_path: _Optional[str] = ...) -> None: ...

class CatalogArg(_message.Message):
    __slots__ = ("header", "db_info", "file_info_vec", "is_catalog_pattern", "rman_backup_type", "host_info_vec", "bifrost_server_config_proto", "catalog_index")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    DB_INFO_FIELD_NUMBER: _ClassVar[int]
    FILE_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    IS_CATALOG_PATTERN_FIELD_NUMBER: _ClassVar[int]
    RMAN_BACKUP_TYPE_FIELD_NUMBER: _ClassVar[int]
    HOST_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    BIFROST_SERVER_CONFIG_PROTO_FIELD_NUMBER: _ClassVar[int]
    CATALOG_INDEX_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    db_info: _oracle_pb2.DatabaseInfoProto
    file_info_vec: _containers.RepeatedCompositeFieldContainer[FileInfo]
    is_catalog_pattern: bool
    rman_backup_type: _env_params_pb2.OracleRmanBackupType.Type
    host_info_vec: _containers.RepeatedCompositeFieldContainer[_env_params_pb2.OracleDBChannelInfo.HostInfo]
    bifrost_server_config_proto: _server_config_pb2.ServerConfigProto
    catalog_index: int
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., db_info: _Optional[_Union[_oracle_pb2.DatabaseInfoProto, _Mapping]] = ..., file_info_vec: _Optional[_Iterable[_Union[FileInfo, _Mapping]]] = ..., is_catalog_pattern: bool = ..., rman_backup_type: _Optional[_Union[_env_params_pb2.OracleRmanBackupType.Type, str]] = ..., host_info_vec: _Optional[_Iterable[_Union[_env_params_pb2.OracleDBChannelInfo.HostInfo, _Mapping]]] = ..., bifrost_server_config_proto: _Optional[_Union[_server_config_pb2.ServerConfigProto, _Mapping]] = ..., catalog_index: _Optional[int] = ...) -> None: ...

class UnCatalogArg(_message.Message):
    __slots__ = ("header", "db_info", "file_info_vec", "is_datafile_pattern", "uncatalog_backuppiece_using_tag", "job_id", "uncatalog_index")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    DB_INFO_FIELD_NUMBER: _ClassVar[int]
    FILE_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    IS_DATAFILE_PATTERN_FIELD_NUMBER: _ClassVar[int]
    UNCATALOG_BACKUPPIECE_USING_TAG_FIELD_NUMBER: _ClassVar[int]
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    UNCATALOG_INDEX_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    db_info: _oracle_pb2.DatabaseInfoProto
    file_info_vec: _containers.RepeatedCompositeFieldContainer[FileInfo]
    is_datafile_pattern: bool
    uncatalog_backuppiece_using_tag: bool
    job_id: int
    uncatalog_index: int
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., db_info: _Optional[_Union[_oracle_pb2.DatabaseInfoProto, _Mapping]] = ..., file_info_vec: _Optional[_Iterable[_Union[FileInfo, _Mapping]]] = ..., is_datafile_pattern: bool = ..., uncatalog_backuppiece_using_tag: bool = ..., job_id: _Optional[int] = ..., uncatalog_index: _Optional[int] = ...) -> None: ...

class RestoreDBConfiguration(_message.Message):
    __slots__ = ("new_db_name", "new_oracle_base", "new_oracle_home", "backup_location", "src_data_file_parent_path_vec", "src_log_file_parent_path_vec", "restore_to_last_node", "data_file_converter_str", "log_file_converter_str", "oracle_db_config", "duplicate_filenames", "newname_clause", "nofilenamecheck", "new_sid_deprecated", "prev_sid", "prev_oracle_base")
    NEW_DB_NAME_FIELD_NUMBER: _ClassVar[int]
    NEW_ORACLE_BASE_FIELD_NUMBER: _ClassVar[int]
    NEW_ORACLE_HOME_FIELD_NUMBER: _ClassVar[int]
    BACKUP_LOCATION_FIELD_NUMBER: _ClassVar[int]
    SRC_DATA_FILE_PARENT_PATH_VEC_FIELD_NUMBER: _ClassVar[int]
    SRC_LOG_FILE_PARENT_PATH_VEC_FIELD_NUMBER: _ClassVar[int]
    RESTORE_TO_LAST_NODE_FIELD_NUMBER: _ClassVar[int]
    DATA_FILE_CONVERTER_STR_FIELD_NUMBER: _ClassVar[int]
    LOG_FILE_CONVERTER_STR_FIELD_NUMBER: _ClassVar[int]
    ORACLE_DB_CONFIG_FIELD_NUMBER: _ClassVar[int]
    DUPLICATE_FILENAMES_FIELD_NUMBER: _ClassVar[int]
    NEWNAME_CLAUSE_FIELD_NUMBER: _ClassVar[int]
    NOFILENAMECHECK_FIELD_NUMBER: _ClassVar[int]
    NEW_SID_DEPRECATED_FIELD_NUMBER: _ClassVar[int]
    PREV_SID_FIELD_NUMBER: _ClassVar[int]
    PREV_ORACLE_BASE_FIELD_NUMBER: _ClassVar[int]
    new_db_name: str
    new_oracle_base: str
    new_oracle_home: str
    backup_location: str
    src_data_file_parent_path_vec: _containers.RepeatedScalarFieldContainer[str]
    src_log_file_parent_path_vec: _containers.RepeatedScalarFieldContainer[str]
    restore_to_last_node: bool
    data_file_converter_str: str
    log_file_converter_str: str
    oracle_db_config: _magneto_pb2.OracleDBConfig
    duplicate_filenames: bool
    newname_clause: str
    nofilenamecheck: bool
    new_sid_deprecated: str
    prev_sid: str
    prev_oracle_base: str
    def __init__(self, new_db_name: _Optional[str] = ..., new_oracle_base: _Optional[str] = ..., new_oracle_home: _Optional[str] = ..., backup_location: _Optional[str] = ..., src_data_file_parent_path_vec: _Optional[_Iterable[str]] = ..., src_log_file_parent_path_vec: _Optional[_Iterable[str]] = ..., restore_to_last_node: bool = ..., data_file_converter_str: _Optional[str] = ..., log_file_converter_str: _Optional[str] = ..., oracle_db_config: _Optional[_Union[_magneto_pb2.OracleDBConfig, _Mapping]] = ..., duplicate_filenames: bool = ..., newname_clause: _Optional[str] = ..., nofilenamecheck: bool = ..., new_sid_deprecated: _Optional[str] = ..., prev_sid: _Optional[str] = ..., prev_oracle_base: _Optional[str] = ...) -> None: ...

class CloneDBInfo(_message.Message):
    __slots__ = ("control_file_backuppiece", "redo_logfile_mapping_vec", "datafile_mapping_vec", "backuppiece_prefix", "spfile_name", "rac_config_file", "backuppiece_vec_deprecated")
    class SourceToTargetEntry(_message.Message):
        __slots__ = ("source_file", "target_file", "group_number", "member_size_mb", "thread_number")
        SOURCE_FILE_FIELD_NUMBER: _ClassVar[int]
        TARGET_FILE_FIELD_NUMBER: _ClassVar[int]
        GROUP_NUMBER_FIELD_NUMBER: _ClassVar[int]
        MEMBER_SIZE_MB_FIELD_NUMBER: _ClassVar[int]
        THREAD_NUMBER_FIELD_NUMBER: _ClassVar[int]
        source_file: str
        target_file: str
        group_number: int
        member_size_mb: int
        thread_number: int
        def __init__(self, source_file: _Optional[str] = ..., target_file: _Optional[str] = ..., group_number: _Optional[int] = ..., member_size_mb: _Optional[int] = ..., thread_number: _Optional[int] = ...) -> None: ...
    CONTROL_FILE_BACKUPPIECE_FIELD_NUMBER: _ClassVar[int]
    REDO_LOGFILE_MAPPING_VEC_FIELD_NUMBER: _ClassVar[int]
    DATAFILE_MAPPING_VEC_FIELD_NUMBER: _ClassVar[int]
    BACKUPPIECE_PREFIX_FIELD_NUMBER: _ClassVar[int]
    SPFILE_NAME_FIELD_NUMBER: _ClassVar[int]
    RAC_CONFIG_FILE_FIELD_NUMBER: _ClassVar[int]
    BACKUPPIECE_VEC_DEPRECATED_FIELD_NUMBER: _ClassVar[int]
    control_file_backuppiece: str
    redo_logfile_mapping_vec: _containers.RepeatedCompositeFieldContainer[CloneDBInfo.SourceToTargetEntry]
    datafile_mapping_vec: _containers.RepeatedCompositeFieldContainer[CloneDBInfo.SourceToTargetEntry]
    backuppiece_prefix: str
    spfile_name: str
    rac_config_file: str
    backuppiece_vec_deprecated: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, control_file_backuppiece: _Optional[str] = ..., redo_logfile_mapping_vec: _Optional[_Iterable[_Union[CloneDBInfo.SourceToTargetEntry, _Mapping]]] = ..., datafile_mapping_vec: _Optional[_Iterable[_Union[CloneDBInfo.SourceToTargetEntry, _Mapping]]] = ..., backuppiece_prefix: _Optional[str] = ..., spfile_name: _Optional[str] = ..., rac_config_file: _Optional[str] = ..., backuppiece_vec_deprecated: _Optional[_Iterable[str]] = ...) -> None: ...

class RestoreDBArg(_message.Message):
    __slots__ = ("header", "db_info", "attempt_number", "new_db_conf", "restore_time", "timezone_difference", "incarnation_id", "mount_path_vec", "no_open_mode", "clone_db_info", "backup_job_id", "remote_mount_info_vec", "clone_of_clone_db_info", "granular_restore_info", "shell_environment_vec", "spfile_prefix", "controlfile_prefix", "rman_backup_type", "host_info_vec", "file_info_vec", "granular_clone_completed", "use_smart_clone_workflow", "bifrost_server_config_proto", "skip_clone_nid", "roll_forward_log_path_vec", "attempt_complete_recovery", "roll_forward_time_msecs", "oracle_archive_log_restore_info", "restore_scn", "oracle_recovery_validation_info", "use_scn_for_restore", "stop_active_passive", "restore_as_rac", "same_config_ir_recovery_options")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    DB_INFO_FIELD_NUMBER: _ClassVar[int]
    ATTEMPT_NUMBER_FIELD_NUMBER: _ClassVar[int]
    NEW_DB_CONF_FIELD_NUMBER: _ClassVar[int]
    RESTORE_TIME_FIELD_NUMBER: _ClassVar[int]
    TIMEZONE_DIFFERENCE_FIELD_NUMBER: _ClassVar[int]
    INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    MOUNT_PATH_VEC_FIELD_NUMBER: _ClassVar[int]
    NO_OPEN_MODE_FIELD_NUMBER: _ClassVar[int]
    CLONE_DB_INFO_FIELD_NUMBER: _ClassVar[int]
    BACKUP_JOB_ID_FIELD_NUMBER: _ClassVar[int]
    REMOTE_MOUNT_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    CLONE_OF_CLONE_DB_INFO_FIELD_NUMBER: _ClassVar[int]
    GRANULAR_RESTORE_INFO_FIELD_NUMBER: _ClassVar[int]
    SHELL_ENVIRONMENT_VEC_FIELD_NUMBER: _ClassVar[int]
    SPFILE_PREFIX_FIELD_NUMBER: _ClassVar[int]
    CONTROLFILE_PREFIX_FIELD_NUMBER: _ClassVar[int]
    RMAN_BACKUP_TYPE_FIELD_NUMBER: _ClassVar[int]
    HOST_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    FILE_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    GRANULAR_CLONE_COMPLETED_FIELD_NUMBER: _ClassVar[int]
    USE_SMART_CLONE_WORKFLOW_FIELD_NUMBER: _ClassVar[int]
    BIFROST_SERVER_CONFIG_PROTO_FIELD_NUMBER: _ClassVar[int]
    SKIP_CLONE_NID_FIELD_NUMBER: _ClassVar[int]
    ROLL_FORWARD_LOG_PATH_VEC_FIELD_NUMBER: _ClassVar[int]
    ATTEMPT_COMPLETE_RECOVERY_FIELD_NUMBER: _ClassVar[int]
    ROLL_FORWARD_TIME_MSECS_FIELD_NUMBER: _ClassVar[int]
    ORACLE_ARCHIVE_LOG_RESTORE_INFO_FIELD_NUMBER: _ClassVar[int]
    RESTORE_SCN_FIELD_NUMBER: _ClassVar[int]
    ORACLE_RECOVERY_VALIDATION_INFO_FIELD_NUMBER: _ClassVar[int]
    USE_SCN_FOR_RESTORE_FIELD_NUMBER: _ClassVar[int]
    STOP_ACTIVE_PASSIVE_FIELD_NUMBER: _ClassVar[int]
    RESTORE_AS_RAC_FIELD_NUMBER: _ClassVar[int]
    SAME_CONFIG_IR_RECOVERY_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    db_info: _oracle_pb2.DatabaseInfoProto
    attempt_number: int
    new_db_conf: RestoreDBConfiguration
    restore_time: str
    timezone_difference: int
    incarnation_id: int
    mount_path_vec: _containers.RepeatedScalarFieldContainer[str]
    no_open_mode: bool
    clone_db_info: CloneDBInfo
    backup_job_id: int
    remote_mount_info_vec: _containers.RepeatedCompositeFieldContainer[RemoteMountInfo]
    clone_of_clone_db_info: CloneDBInfo
    granular_restore_info: _magneto_pb2.GranularRestoreInfo
    shell_environment_vec: _containers.RepeatedCompositeFieldContainer[_magneto_pb2.RestoreOracleAppObjectParams.KeyValuePair]
    spfile_prefix: str
    controlfile_prefix: str
    rman_backup_type: _env_params_pb2.OracleRmanBackupType.Type
    host_info_vec: _containers.RepeatedCompositeFieldContainer[_env_params_pb2.OracleDBChannelInfo.HostInfo]
    file_info_vec: _containers.RepeatedCompositeFieldContainer[FileInfo]
    granular_clone_completed: bool
    use_smart_clone_workflow: bool
    bifrost_server_config_proto: _server_config_pb2.ServerConfigProto
    skip_clone_nid: bool
    roll_forward_log_path_vec: _containers.RepeatedScalarFieldContainer[str]
    attempt_complete_recovery: bool
    roll_forward_time_msecs: int
    oracle_archive_log_restore_info: _magneto_pb2.OracleArchiveLogInfo
    restore_scn: int
    oracle_recovery_validation_info: _magneto_pb2.OracleRecoveryValidationInfo
    use_scn_for_restore: bool
    stop_active_passive: bool
    restore_as_rac: bool
    same_config_ir_recovery_options: _oracle_pb2_1.SameConfigIrRecoveryOptions
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., db_info: _Optional[_Union[_oracle_pb2.DatabaseInfoProto, _Mapping]] = ..., attempt_number: _Optional[int] = ..., new_db_conf: _Optional[_Union[RestoreDBConfiguration, _Mapping]] = ..., restore_time: _Optional[str] = ..., timezone_difference: _Optional[int] = ..., incarnation_id: _Optional[int] = ..., mount_path_vec: _Optional[_Iterable[str]] = ..., no_open_mode: bool = ..., clone_db_info: _Optional[_Union[CloneDBInfo, _Mapping]] = ..., backup_job_id: _Optional[int] = ..., remote_mount_info_vec: _Optional[_Iterable[_Union[RemoteMountInfo, _Mapping]]] = ..., clone_of_clone_db_info: _Optional[_Union[CloneDBInfo, _Mapping]] = ..., granular_restore_info: _Optional[_Union[_magneto_pb2.GranularRestoreInfo, _Mapping]] = ..., shell_environment_vec: _Optional[_Iterable[_Union[_magneto_pb2.RestoreOracleAppObjectParams.KeyValuePair, _Mapping]]] = ..., spfile_prefix: _Optional[str] = ..., controlfile_prefix: _Optional[str] = ..., rman_backup_type: _Optional[_Union[_env_params_pb2.OracleRmanBackupType.Type, str]] = ..., host_info_vec: _Optional[_Iterable[_Union[_env_params_pb2.OracleDBChannelInfo.HostInfo, _Mapping]]] = ..., file_info_vec: _Optional[_Iterable[_Union[FileInfo, _Mapping]]] = ..., granular_clone_completed: bool = ..., use_smart_clone_workflow: bool = ..., bifrost_server_config_proto: _Optional[_Union[_server_config_pb2.ServerConfigProto, _Mapping]] = ..., skip_clone_nid: bool = ..., roll_forward_log_path_vec: _Optional[_Iterable[str]] = ..., attempt_complete_recovery: bool = ..., roll_forward_time_msecs: _Optional[int] = ..., oracle_archive_log_restore_info: _Optional[_Union[_magneto_pb2.OracleArchiveLogInfo, _Mapping]] = ..., restore_scn: _Optional[int] = ..., oracle_recovery_validation_info: _Optional[_Union[_magneto_pb2.OracleRecoveryValidationInfo, _Mapping]] = ..., use_scn_for_restore: bool = ..., stop_active_passive: bool = ..., restore_as_rac: bool = ..., same_config_ir_recovery_options: _Optional[_Union[_oracle_pb2_1.SameConfigIrRecoveryOptions, _Mapping]] = ...) -> None: ...

class RestoreDBResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class PostAltRestoreDBArg(_message.Message):
    __slots__ = ("header", "new_db_conf", "no_open_mode", "mount_points_vec", "is_clone_db", "is_clone_view", "shell_environment_vec")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    NEW_DB_CONF_FIELD_NUMBER: _ClassVar[int]
    NO_OPEN_MODE_FIELD_NUMBER: _ClassVar[int]
    MOUNT_POINTS_VEC_FIELD_NUMBER: _ClassVar[int]
    IS_CLONE_DB_FIELD_NUMBER: _ClassVar[int]
    IS_CLONE_VIEW_FIELD_NUMBER: _ClassVar[int]
    SHELL_ENVIRONMENT_VEC_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    new_db_conf: RestoreDBConfiguration
    no_open_mode: bool
    mount_points_vec: _containers.RepeatedScalarFieldContainer[str]
    is_clone_db: bool
    is_clone_view: bool
    shell_environment_vec: _containers.RepeatedCompositeFieldContainer[_magneto_pb2.RestoreOracleAppObjectParams.KeyValuePair]
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., new_db_conf: _Optional[_Union[RestoreDBConfiguration, _Mapping]] = ..., no_open_mode: bool = ..., mount_points_vec: _Optional[_Iterable[str]] = ..., is_clone_db: bool = ..., is_clone_view: bool = ..., shell_environment_vec: _Optional[_Iterable[_Union[_magneto_pb2.RestoreOracleAppObjectParams.KeyValuePair, _Mapping]]] = ...) -> None: ...

class PostAltRestoreDBResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class MigrateDBArg(_message.Message):
    __slots__ = ("header", "migrate_task_id", "migrate_db_info", "target_path_vec", "datafile_name_to_info_map")
    class DatafileInfo(_message.Message):
        __slots__ = ("target_path",)
        TARGET_PATH_FIELD_NUMBER: _ClassVar[int]
        target_path: str
        def __init__(self, target_path: _Optional[str] = ...) -> None: ...
    class DatafileNameToInfoMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: MigrateDBArg.DatafileInfo
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[MigrateDBArg.DatafileInfo, _Mapping]] = ...) -> None: ...
    HEADER_FIELD_NUMBER: _ClassVar[int]
    MIGRATE_TASK_ID_FIELD_NUMBER: _ClassVar[int]
    MIGRATE_DB_INFO_FIELD_NUMBER: _ClassVar[int]
    TARGET_PATH_VEC_FIELD_NUMBER: _ClassVar[int]
    DATAFILE_NAME_TO_INFO_MAP_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    migrate_task_id: int
    migrate_db_info: MigrateDBInfo
    target_path_vec: _containers.RepeatedScalarFieldContainer[str]
    datafile_name_to_info_map: _containers.MessageMap[str, MigrateDBArg.DatafileInfo]
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., migrate_task_id: _Optional[int] = ..., migrate_db_info: _Optional[_Union[MigrateDBInfo, _Mapping]] = ..., target_path_vec: _Optional[_Iterable[str]] = ..., datafile_name_to_info_map: _Optional[_Mapping[str, MigrateDBArg.DatafileInfo]] = ...) -> None: ...

class MigrateDBInfo(_message.Message):
    __slots__ = ("db_name", "db_sid", "oracle_home", "uuid", "mountpoint_identifier", "mountpoint_base_dir")
    DB_NAME_FIELD_NUMBER: _ClassVar[int]
    DB_SID_FIELD_NUMBER: _ClassVar[int]
    ORACLE_HOME_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    MOUNTPOINT_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    MOUNTPOINT_BASE_DIR_FIELD_NUMBER: _ClassVar[int]
    db_name: str
    db_sid: str
    oracle_home: str
    uuid: str
    mountpoint_identifier: str
    mountpoint_base_dir: str
    def __init__(self, db_name: _Optional[str] = ..., db_sid: _Optional[str] = ..., oracle_home: _Optional[str] = ..., uuid: _Optional[str] = ..., mountpoint_identifier: _Optional[str] = ..., mountpoint_base_dir: _Optional[str] = ...) -> None: ...

class MigrateDBResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class MigrateDBProgressResult(_message.Message):
    __slots__ = ("error", "is_migrate_completed", "total_bytes_processed", "total_bytes_to_be_processed", "rman_log_info_vec", "migrate_error")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    IS_MIGRATE_COMPLETED_FIELD_NUMBER: _ClassVar[int]
    TOTAL_BYTES_PROCESSED_FIELD_NUMBER: _ClassVar[int]
    TOTAL_BYTES_TO_BE_PROCESSED_FIELD_NUMBER: _ClassVar[int]
    RMAN_LOG_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    MIGRATE_ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    is_migrate_completed: bool
    total_bytes_processed: int
    total_bytes_to_be_processed: int
    rman_log_info_vec: _containers.RepeatedScalarFieldContainer[str]
    migrate_error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., is_migrate_completed: bool = ..., total_bytes_processed: _Optional[int] = ..., total_bytes_to_be_processed: _Optional[int] = ..., rman_log_info_vec: _Optional[_Iterable[str]] = ..., migrate_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class DBRestoreType(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kSingleInstanceOverwrite: _ClassVar[DBRestoreType.Type]
        kSingleInstance: _ClassVar[DBRestoreType.Type]
        kRacOverwrite: _ClassVar[DBRestoreType.Type]
        kAPOverwrite: _ClassVar[DBRestoreType.Type]
    kSingleInstanceOverwrite: DBRestoreType.Type
    kSingleInstance: DBRestoreType.Type
    kRacOverwrite: DBRestoreType.Type
    kAPOverwrite: DBRestoreType.Type
    def __init__(self) -> None: ...

class RestoreDBProgressArg(_message.Message):
    __slots__ = ("header", "db_info", "attempt_number", "new_db_conf", "restore_time", "timezone_difference", "incarnation_id", "mount_path_vec", "remote_mount_info_vec", "no_open_mode", "restore_type", "backup_job_id", "clone_db_info", "clone_of_clone_db_info", "shell_environment_vec", "rman_backup_type", "granular_restore_info", "granular_clone_completed", "use_smart_clone_workflow", "skip_clone_nid", "roll_forward_log_path_vec", "attempt_complete_recovery", "roll_forward_time_msecs", "oracle_archive_log_restore_info", "restore_scn", "oracle_recovery_validation_info", "use_scn_for_restore", "stop_active_passive", "restore_as_rac", "same_config_ir_recovery_options")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    DB_INFO_FIELD_NUMBER: _ClassVar[int]
    ATTEMPT_NUMBER_FIELD_NUMBER: _ClassVar[int]
    NEW_DB_CONF_FIELD_NUMBER: _ClassVar[int]
    RESTORE_TIME_FIELD_NUMBER: _ClassVar[int]
    TIMEZONE_DIFFERENCE_FIELD_NUMBER: _ClassVar[int]
    INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    MOUNT_PATH_VEC_FIELD_NUMBER: _ClassVar[int]
    REMOTE_MOUNT_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    NO_OPEN_MODE_FIELD_NUMBER: _ClassVar[int]
    RESTORE_TYPE_FIELD_NUMBER: _ClassVar[int]
    BACKUP_JOB_ID_FIELD_NUMBER: _ClassVar[int]
    CLONE_DB_INFO_FIELD_NUMBER: _ClassVar[int]
    CLONE_OF_CLONE_DB_INFO_FIELD_NUMBER: _ClassVar[int]
    SHELL_ENVIRONMENT_VEC_FIELD_NUMBER: _ClassVar[int]
    RMAN_BACKUP_TYPE_FIELD_NUMBER: _ClassVar[int]
    GRANULAR_RESTORE_INFO_FIELD_NUMBER: _ClassVar[int]
    GRANULAR_CLONE_COMPLETED_FIELD_NUMBER: _ClassVar[int]
    USE_SMART_CLONE_WORKFLOW_FIELD_NUMBER: _ClassVar[int]
    SKIP_CLONE_NID_FIELD_NUMBER: _ClassVar[int]
    ROLL_FORWARD_LOG_PATH_VEC_FIELD_NUMBER: _ClassVar[int]
    ATTEMPT_COMPLETE_RECOVERY_FIELD_NUMBER: _ClassVar[int]
    ROLL_FORWARD_TIME_MSECS_FIELD_NUMBER: _ClassVar[int]
    ORACLE_ARCHIVE_LOG_RESTORE_INFO_FIELD_NUMBER: _ClassVar[int]
    RESTORE_SCN_FIELD_NUMBER: _ClassVar[int]
    ORACLE_RECOVERY_VALIDATION_INFO_FIELD_NUMBER: _ClassVar[int]
    USE_SCN_FOR_RESTORE_FIELD_NUMBER: _ClassVar[int]
    STOP_ACTIVE_PASSIVE_FIELD_NUMBER: _ClassVar[int]
    RESTORE_AS_RAC_FIELD_NUMBER: _ClassVar[int]
    SAME_CONFIG_IR_RECOVERY_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    db_info: _oracle_pb2.DatabaseInfoProto
    attempt_number: int
    new_db_conf: RestoreDBConfiguration
    restore_time: str
    timezone_difference: int
    incarnation_id: int
    mount_path_vec: _containers.RepeatedScalarFieldContainer[str]
    remote_mount_info_vec: _containers.RepeatedCompositeFieldContainer[RemoteMountInfo]
    no_open_mode: bool
    restore_type: DBRestoreType.Type
    backup_job_id: int
    clone_db_info: CloneDBInfo
    clone_of_clone_db_info: CloneDBInfo
    shell_environment_vec: _containers.RepeatedCompositeFieldContainer[_magneto_pb2.RestoreOracleAppObjectParams.KeyValuePair]
    rman_backup_type: _env_params_pb2.OracleRmanBackupType.Type
    granular_restore_info: _magneto_pb2.GranularRestoreInfo
    granular_clone_completed: bool
    use_smart_clone_workflow: bool
    skip_clone_nid: bool
    roll_forward_log_path_vec: _containers.RepeatedScalarFieldContainer[str]
    attempt_complete_recovery: bool
    roll_forward_time_msecs: int
    oracle_archive_log_restore_info: _magneto_pb2.OracleArchiveLogInfo
    restore_scn: int
    oracle_recovery_validation_info: _magneto_pb2.OracleRecoveryValidationInfo
    use_scn_for_restore: bool
    stop_active_passive: bool
    restore_as_rac: bool
    same_config_ir_recovery_options: _oracle_pb2_1.SameConfigIrRecoveryOptions
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., db_info: _Optional[_Union[_oracle_pb2.DatabaseInfoProto, _Mapping]] = ..., attempt_number: _Optional[int] = ..., new_db_conf: _Optional[_Union[RestoreDBConfiguration, _Mapping]] = ..., restore_time: _Optional[str] = ..., timezone_difference: _Optional[int] = ..., incarnation_id: _Optional[int] = ..., mount_path_vec: _Optional[_Iterable[str]] = ..., remote_mount_info_vec: _Optional[_Iterable[_Union[RemoteMountInfo, _Mapping]]] = ..., no_open_mode: bool = ..., restore_type: _Optional[_Union[DBRestoreType.Type, str]] = ..., backup_job_id: _Optional[int] = ..., clone_db_info: _Optional[_Union[CloneDBInfo, _Mapping]] = ..., clone_of_clone_db_info: _Optional[_Union[CloneDBInfo, _Mapping]] = ..., shell_environment_vec: _Optional[_Iterable[_Union[_magneto_pb2.RestoreOracleAppObjectParams.KeyValuePair, _Mapping]]] = ..., rman_backup_type: _Optional[_Union[_env_params_pb2.OracleRmanBackupType.Type, str]] = ..., granular_restore_info: _Optional[_Union[_magneto_pb2.GranularRestoreInfo, _Mapping]] = ..., granular_clone_completed: bool = ..., use_smart_clone_workflow: bool = ..., skip_clone_nid: bool = ..., roll_forward_log_path_vec: _Optional[_Iterable[str]] = ..., attempt_complete_recovery: bool = ..., roll_forward_time_msecs: _Optional[int] = ..., oracle_archive_log_restore_info: _Optional[_Union[_magneto_pb2.OracleArchiveLogInfo, _Mapping]] = ..., restore_scn: _Optional[int] = ..., oracle_recovery_validation_info: _Optional[_Union[_magneto_pb2.OracleRecoveryValidationInfo, _Mapping]] = ..., use_scn_for_restore: bool = ..., stop_active_passive: bool = ..., restore_as_rac: bool = ..., same_config_ir_recovery_options: _Optional[_Union[_oracle_pb2_1.SameConfigIrRecoveryOptions, _Mapping]] = ...) -> None: ...

class RestoreDBProgressResult(_message.Message):
    __slots__ = ("error", "restore_completed", "restore_error", "total_bytes_processed", "total_bytes_to_be_processed", "db_info", "rman_log_info_vec")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    RESTORE_COMPLETED_FIELD_NUMBER: _ClassVar[int]
    RESTORE_ERROR_FIELD_NUMBER: _ClassVar[int]
    TOTAL_BYTES_PROCESSED_FIELD_NUMBER: _ClassVar[int]
    TOTAL_BYTES_TO_BE_PROCESSED_FIELD_NUMBER: _ClassVar[int]
    DB_INFO_FIELD_NUMBER: _ClassVar[int]
    RMAN_LOG_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    restore_completed: bool
    restore_error: _error_pb2.ErrorProto
    total_bytes_processed: int
    total_bytes_to_be_processed: int
    db_info: _oracle_pb2.DatabaseInfoProto
    rman_log_info_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., restore_completed: bool = ..., restore_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., total_bytes_processed: _Optional[int] = ..., total_bytes_to_be_processed: _Optional[int] = ..., db_info: _Optional[_Union[_oracle_pb2.DatabaseInfoProto, _Mapping]] = ..., rman_log_info_vec: _Optional[_Iterable[str]] = ...) -> None: ...

class RestoreDBControlFileArg(_message.Message):
    __slots__ = ("header", "db_info", "control_file_path", "restore_type", "shell_environment_vec", "rman_backup_type", "host_info_vec", "bifrost_server_config_proto", "attempt_complete_recovery", "spfile_path", "pfile_path", "pfile_parameter_map", "restore_spfile_or_pfile_info", "stop_active_passive")
    class PfileParameterMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    HEADER_FIELD_NUMBER: _ClassVar[int]
    DB_INFO_FIELD_NUMBER: _ClassVar[int]
    CONTROL_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    RESTORE_TYPE_FIELD_NUMBER: _ClassVar[int]
    SHELL_ENVIRONMENT_VEC_FIELD_NUMBER: _ClassVar[int]
    RMAN_BACKUP_TYPE_FIELD_NUMBER: _ClassVar[int]
    HOST_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    BIFROST_SERVER_CONFIG_PROTO_FIELD_NUMBER: _ClassVar[int]
    ATTEMPT_COMPLETE_RECOVERY_FIELD_NUMBER: _ClassVar[int]
    SPFILE_PATH_FIELD_NUMBER: _ClassVar[int]
    PFILE_PATH_FIELD_NUMBER: _ClassVar[int]
    PFILE_PARAMETER_MAP_FIELD_NUMBER: _ClassVar[int]
    RESTORE_SPFILE_OR_PFILE_INFO_FIELD_NUMBER: _ClassVar[int]
    STOP_ACTIVE_PASSIVE_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    db_info: _oracle_pb2.DatabaseInfoProto
    control_file_path: str
    restore_type: DBRestoreType.Type
    shell_environment_vec: _containers.RepeatedCompositeFieldContainer[_magneto_pb2.RestoreOracleAppObjectParams.KeyValuePair]
    rman_backup_type: _env_params_pb2.OracleRmanBackupType.Type
    host_info_vec: _containers.RepeatedCompositeFieldContainer[_env_params_pb2.OracleDBChannelInfo.HostInfo]
    bifrost_server_config_proto: _server_config_pb2.ServerConfigProto
    attempt_complete_recovery: bool
    spfile_path: str
    pfile_path: str
    pfile_parameter_map: _containers.ScalarMap[str, str]
    restore_spfile_or_pfile_info: _magneto_pb2.RestoreSpfileOrPfileInfo
    stop_active_passive: bool
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., db_info: _Optional[_Union[_oracle_pb2.DatabaseInfoProto, _Mapping]] = ..., control_file_path: _Optional[str] = ..., restore_type: _Optional[_Union[DBRestoreType.Type, str]] = ..., shell_environment_vec: _Optional[_Iterable[_Union[_magneto_pb2.RestoreOracleAppObjectParams.KeyValuePair, _Mapping]]] = ..., rman_backup_type: _Optional[_Union[_env_params_pb2.OracleRmanBackupType.Type, str]] = ..., host_info_vec: _Optional[_Iterable[_Union[_env_params_pb2.OracleDBChannelInfo.HostInfo, _Mapping]]] = ..., bifrost_server_config_proto: _Optional[_Union[_server_config_pb2.ServerConfigProto, _Mapping]] = ..., attempt_complete_recovery: bool = ..., spfile_path: _Optional[str] = ..., pfile_path: _Optional[str] = ..., pfile_parameter_map: _Optional[_Mapping[str, str]] = ..., restore_spfile_or_pfile_info: _Optional[_Union[_magneto_pb2.RestoreSpfileOrPfileInfo, _Mapping]] = ..., stop_active_passive: bool = ...) -> None: ...

class RestoreDBControlFileResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class DBBackupDataFilesArg(_message.Message):
    __slots__ = ("header", "db_info", "job_id", "job_run_id", "attempt_number")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    DB_INFO_FIELD_NUMBER: _ClassVar[int]
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    JOB_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    ATTEMPT_NUMBER_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    db_info: _oracle_pb2.DatabaseInfoProto
    job_id: int
    job_run_id: int
    attempt_number: int
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., db_info: _Optional[_Union[_oracle_pb2.DatabaseInfoProto, _Mapping]] = ..., job_id: _Optional[int] = ..., job_run_id: _Optional[int] = ..., attempt_number: _Optional[int] = ...) -> None: ...

class DBBackupDataFilesResult(_message.Message):
    __slots__ = ("error", "data_files_info", "is_backup_running")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    DATA_FILES_INFO_FIELD_NUMBER: _ClassVar[int]
    IS_BACKUP_RUNNING_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    data_files_info: _oracle_sql_pb2.DataFilesInfo
    is_backup_running: bool
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., data_files_info: _Optional[_Union[_oracle_sql_pb2.DataFilesInfo, _Mapping]] = ..., is_backup_running: bool = ...) -> None: ...

class DropOracleDBsArg(_message.Message):
    __slots__ = ("header", "force_delete", "db_info_vec")
    class DropDBInfo(_message.Message):
        __slots__ = ("oracle_home", "db_sid", "db_name", "mount_point", "is_rac")
        ORACLE_HOME_FIELD_NUMBER: _ClassVar[int]
        DB_SID_FIELD_NUMBER: _ClassVar[int]
        DB_NAME_FIELD_NUMBER: _ClassVar[int]
        MOUNT_POINT_FIELD_NUMBER: _ClassVar[int]
        IS_RAC_FIELD_NUMBER: _ClassVar[int]
        oracle_home: str
        db_sid: str
        db_name: str
        mount_point: str
        is_rac: bool
        def __init__(self, oracle_home: _Optional[str] = ..., db_sid: _Optional[str] = ..., db_name: _Optional[str] = ..., mount_point: _Optional[str] = ..., is_rac: bool = ...) -> None: ...
    HEADER_FIELD_NUMBER: _ClassVar[int]
    FORCE_DELETE_FIELD_NUMBER: _ClassVar[int]
    DB_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    force_delete: bool
    db_info_vec: _containers.RepeatedCompositeFieldContainer[DropOracleDBsArg.DropDBInfo]
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., force_delete: bool = ..., db_info_vec: _Optional[_Iterable[_Union[DropOracleDBsArg.DropDBInfo, _Mapping]]] = ...) -> None: ...

class DropOracleDBsResult(_message.Message):
    __slots__ = ("error", "db_error_vec")
    class DBError(_message.Message):
        __slots__ = ("db_name", "error")
        DB_NAME_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        db_name: str
        error: _error_pb2.ErrorProto
        def __init__(self, db_name: _Optional[str] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...
    ERROR_FIELD_NUMBER: _ClassVar[int]
    DB_ERROR_VEC_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    db_error_vec: _containers.RepeatedCompositeFieldContainer[DropOracleDBsResult.DBError]
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., db_error_vec: _Optional[_Iterable[_Union[DropOracleDBsResult.DBError, _Mapping]]] = ...) -> None: ...

class DBBackupEnvCheckArg(_message.Message):
    __slots__ = ("backup_args",)
    BACKUP_ARGS_FIELD_NUMBER: _ClassVar[int]
    backup_args: BackupDBArg
    def __init__(self, backup_args: _Optional[_Union[BackupDBArg, _Mapping]] = ...) -> None: ...

class DBRestoreAltEnvCheckArg(_message.Message):
    __slots__ = ("restore_args",)
    RESTORE_ARGS_FIELD_NUMBER: _ClassVar[int]
    restore_args: RestoreDBArg
    def __init__(self, restore_args: _Optional[_Union[RestoreDBArg, _Mapping]] = ...) -> None: ...

class DBRestoreOriginalEnvCheckArg(_message.Message):
    __slots__ = ("db_info", "restore_args", "restore_spfile_or_pfile_info")
    DB_INFO_FIELD_NUMBER: _ClassVar[int]
    RESTORE_ARGS_FIELD_NUMBER: _ClassVar[int]
    RESTORE_SPFILE_OR_PFILE_INFO_FIELD_NUMBER: _ClassVar[int]
    db_info: _oracle_pb2.DatabaseInfoProto
    restore_args: RestoreDBArg
    restore_spfile_or_pfile_info: _magneto_pb2.RestoreSpfileOrPfileInfo
    def __init__(self, db_info: _Optional[_Union[_oracle_pb2.DatabaseInfoProto, _Mapping]] = ..., restore_args: _Optional[_Union[RestoreDBArg, _Mapping]] = ..., restore_spfile_or_pfile_info: _Optional[_Union[_magneto_pb2.RestoreSpfileOrPfileInfo, _Mapping]] = ...) -> None: ...

class DBCloneEnvCheckArg(_message.Message):
    __slots__ = ("restore_args",)
    RESTORE_ARGS_FIELD_NUMBER: _ClassVar[int]
    restore_args: RestoreDBArg
    def __init__(self, restore_args: _Optional[_Union[RestoreDBArg, _Mapping]] = ...) -> None: ...

class DBMigrateEnvCheckArg(_message.Message):
    __slots__ = ("migrate_db_info", "target_path_vec", "is_migrate_completed")
    MIGRATE_DB_INFO_FIELD_NUMBER: _ClassVar[int]
    TARGET_PATH_VEC_FIELD_NUMBER: _ClassVar[int]
    IS_MIGRATE_COMPLETED_FIELD_NUMBER: _ClassVar[int]
    migrate_db_info: MigrateDBInfo
    target_path_vec: _containers.RepeatedScalarFieldContainer[str]
    is_migrate_completed: bool
    def __init__(self, migrate_db_info: _Optional[_Union[MigrateDBInfo, _Mapping]] = ..., target_path_vec: _Optional[_Iterable[str]] = ..., is_migrate_completed: bool = ...) -> None: ...

class OracleEnvCheckArg(_message.Message):
    __slots__ = ("header", "type", "bkp_env_check_arg", "restore_alt_env_check_arg", "restore_orig_env_check_arg", "clone_db_env_check_arg", "migrate_db_env_check_arg")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kEnv: _ClassVar[OracleEnvCheckArg.Type]
        kBackup: _ClassVar[OracleEnvCheckArg.Type]
        kRestoreOverwrite: _ClassVar[OracleEnvCheckArg.Type]
        kRestoreAlt: _ClassVar[OracleEnvCheckArg.Type]
        kClone: _ClassVar[OracleEnvCheckArg.Type]
        kDiscovery: _ClassVar[OracleEnvCheckArg.Type]
        kMigrateDB: _ClassVar[OracleEnvCheckArg.Type]
        kRestoreArchiveLog: _ClassVar[OracleEnvCheckArg.Type]
        kDummyDBValidation: _ClassVar[OracleEnvCheckArg.Type]
    kEnv: OracleEnvCheckArg.Type
    kBackup: OracleEnvCheckArg.Type
    kRestoreOverwrite: OracleEnvCheckArg.Type
    kRestoreAlt: OracleEnvCheckArg.Type
    kClone: OracleEnvCheckArg.Type
    kDiscovery: OracleEnvCheckArg.Type
    kMigrateDB: OracleEnvCheckArg.Type
    kRestoreArchiveLog: OracleEnvCheckArg.Type
    kDummyDBValidation: OracleEnvCheckArg.Type
    HEADER_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    BKP_ENV_CHECK_ARG_FIELD_NUMBER: _ClassVar[int]
    RESTORE_ALT_ENV_CHECK_ARG_FIELD_NUMBER: _ClassVar[int]
    RESTORE_ORIG_ENV_CHECK_ARG_FIELD_NUMBER: _ClassVar[int]
    CLONE_DB_ENV_CHECK_ARG_FIELD_NUMBER: _ClassVar[int]
    MIGRATE_DB_ENV_CHECK_ARG_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    type: OracleEnvCheckArg.Type
    bkp_env_check_arg: DBBackupEnvCheckArg
    restore_alt_env_check_arg: DBRestoreAltEnvCheckArg
    restore_orig_env_check_arg: DBRestoreOriginalEnvCheckArg
    clone_db_env_check_arg: DBCloneEnvCheckArg
    migrate_db_env_check_arg: DBMigrateEnvCheckArg
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., type: _Optional[_Union[OracleEnvCheckArg.Type, str]] = ..., bkp_env_check_arg: _Optional[_Union[DBBackupEnvCheckArg, _Mapping]] = ..., restore_alt_env_check_arg: _Optional[_Union[DBRestoreAltEnvCheckArg, _Mapping]] = ..., restore_orig_env_check_arg: _Optional[_Union[DBRestoreOriginalEnvCheckArg, _Mapping]] = ..., clone_db_env_check_arg: _Optional[_Union[DBCloneEnvCheckArg, _Mapping]] = ..., migrate_db_env_check_arg: _Optional[_Union[DBMigrateEnvCheckArg, _Mapping]] = ...) -> None: ...

class PrecheckResult(_message.Message):
    __slots__ = ("message_type", "message")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kInfo: _ClassVar[PrecheckResult.Type]
        kWarn: _ClassVar[PrecheckResult.Type]
        kError: _ClassVar[PrecheckResult.Type]
    kInfo: PrecheckResult.Type
    kWarn: PrecheckResult.Type
    kError: PrecheckResult.Type
    MESSAGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message_type: PrecheckResult.Type
    message: str
    def __init__(self, message_type: _Optional[_Union[PrecheckResult.Type, str]] = ..., message: _Optional[str] = ...) -> None: ...

class OracleEnvCheckResult(_message.Message):
    __slots__ = ("error", "precheck_result_vec")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    PRECHECK_RESULT_VEC_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    precheck_result_vec: _containers.RepeatedCompositeFieldContainer[PrecheckResult]
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., precheck_result_vec: _Optional[_Iterable[_Union[PrecheckResult, _Mapping]]] = ...) -> None: ...

class DeleteArchivelogArg(_message.Message):
    __slots__ = ("header", "db_info", "rman_backup_type", "archivelog_keep_days", "archivelog_keep_hours", "mount_path_vec")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    DB_INFO_FIELD_NUMBER: _ClassVar[int]
    RMAN_BACKUP_TYPE_FIELD_NUMBER: _ClassVar[int]
    ARCHIVELOG_KEEP_DAYS_FIELD_NUMBER: _ClassVar[int]
    ARCHIVELOG_KEEP_HOURS_FIELD_NUMBER: _ClassVar[int]
    MOUNT_PATH_VEC_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    db_info: _oracle_pb2.DatabaseInfoProto
    rman_backup_type: _env_params_pb2.OracleRmanBackupType.Type
    archivelog_keep_days: int
    archivelog_keep_hours: int
    mount_path_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., db_info: _Optional[_Union[_oracle_pb2.DatabaseInfoProto, _Mapping]] = ..., rman_backup_type: _Optional[_Union[_env_params_pb2.OracleRmanBackupType.Type, str]] = ..., archivelog_keep_days: _Optional[int] = ..., archivelog_keep_hours: _Optional[int] = ..., mount_path_vec: _Optional[_Iterable[str]] = ...) -> None: ...

class DeleteArchivelogResult(_message.Message):
    __slots__ = ("error", "is_finished")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    IS_FINISHED_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    is_finished: bool
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., is_finished: bool = ...) -> None: ...
