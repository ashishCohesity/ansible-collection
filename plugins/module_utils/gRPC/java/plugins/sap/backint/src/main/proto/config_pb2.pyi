from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ParamsProto(_message.Message):
    __slots__ = ("cluster_ips", "cluster_port", "view_name", "sap_nfs_mount_path", "sap_nfs_mount_options", "sap_max_read_write_retries", "sap_max_io_size_in_bytes", "sap_max_io_asynchronous_callback_concurrency", "sap_nfs_create_file_permission", "sap_nfs_create_directory_permission", "sap_max_backup_streams", "sap_max_restore_streams", "sap_max_metafiles_read_concurrency", "sap_max_inquire_period_days", "sap_max_ebid_create_retries", "sap_max_logs_directories_retention_count", "database_type", "service_type", "sap_oracle_online_backup_initial_start_time_to_check_switch_log_file_in_seconds", "sap_oracle_online_backup_interval_time_to_check_switch_log_file_in_seconds", "sap_oracle_online_backup_initial_start_time_to_check_backup_finished_in_seconds", "sap_oracle_online_backup_interval_time_to_check_backup_finished_in_seconds", "sap_oracle_online_backup_delay_time_to_start_backup_switch_in_seconds", "sap_oracle_online_backup_delay_time_to_check_backup_progress_in_seconds", "sap_oracle_online_backup_max_switch_wait_time_in_milli_seconds", "sap_oracle_restore_with_user_id", "sap_oracle_restore_with_group_id", "number_of_mounts", "sap_max_num_outstanding_io", "log_dir", "log_level", "os_type", "rpc_timeout_msecs", "write_rpc_timeout_msecs", "rpc_call_concurrency", "rpc_callback_concurrency", "alive_message_interval_msecs", "log_io_stats_interval", "log_outstanding_io_offset_interval_msecs", "catalog_view_name", "enable_immutable_view", "keep_alive_polling_interval_secs", "sap_certificate_config_path", "n_threads_event_loop_group", "n_threads_netty_channel_executor", "log_heap_dump_interval_mins", "log_thread_dump_interval_mins", "backint_protocol_version")
    CLUSTER_IPS_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_PORT_FIELD_NUMBER: _ClassVar[int]
    VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    SAP_NFS_MOUNT_PATH_FIELD_NUMBER: _ClassVar[int]
    SAP_NFS_MOUNT_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    SAP_MAX_READ_WRITE_RETRIES_FIELD_NUMBER: _ClassVar[int]
    SAP_MAX_IO_SIZE_IN_BYTES_FIELD_NUMBER: _ClassVar[int]
    SAP_MAX_IO_ASYNCHRONOUS_CALLBACK_CONCURRENCY_FIELD_NUMBER: _ClassVar[int]
    SAP_NFS_CREATE_FILE_PERMISSION_FIELD_NUMBER: _ClassVar[int]
    SAP_NFS_CREATE_DIRECTORY_PERMISSION_FIELD_NUMBER: _ClassVar[int]
    SAP_MAX_BACKUP_STREAMS_FIELD_NUMBER: _ClassVar[int]
    SAP_MAX_RESTORE_STREAMS_FIELD_NUMBER: _ClassVar[int]
    SAP_MAX_METAFILES_READ_CONCURRENCY_FIELD_NUMBER: _ClassVar[int]
    SAP_MAX_INQUIRE_PERIOD_DAYS_FIELD_NUMBER: _ClassVar[int]
    SAP_MAX_EBID_CREATE_RETRIES_FIELD_NUMBER: _ClassVar[int]
    SAP_MAX_LOGS_DIRECTORIES_RETENTION_COUNT_FIELD_NUMBER: _ClassVar[int]
    DATABASE_TYPE_FIELD_NUMBER: _ClassVar[int]
    SERVICE_TYPE_FIELD_NUMBER: _ClassVar[int]
    SAP_ORACLE_ONLINE_BACKUP_INITIAL_START_TIME_TO_CHECK_SWITCH_LOG_FILE_IN_SECONDS_FIELD_NUMBER: _ClassVar[int]
    SAP_ORACLE_ONLINE_BACKUP_INTERVAL_TIME_TO_CHECK_SWITCH_LOG_FILE_IN_SECONDS_FIELD_NUMBER: _ClassVar[int]
    SAP_ORACLE_ONLINE_BACKUP_INITIAL_START_TIME_TO_CHECK_BACKUP_FINISHED_IN_SECONDS_FIELD_NUMBER: _ClassVar[int]
    SAP_ORACLE_ONLINE_BACKUP_INTERVAL_TIME_TO_CHECK_BACKUP_FINISHED_IN_SECONDS_FIELD_NUMBER: _ClassVar[int]
    SAP_ORACLE_ONLINE_BACKUP_DELAY_TIME_TO_START_BACKUP_SWITCH_IN_SECONDS_FIELD_NUMBER: _ClassVar[int]
    SAP_ORACLE_ONLINE_BACKUP_DELAY_TIME_TO_CHECK_BACKUP_PROGRESS_IN_SECONDS_FIELD_NUMBER: _ClassVar[int]
    SAP_ORACLE_ONLINE_BACKUP_MAX_SWITCH_WAIT_TIME_IN_MILLI_SECONDS_FIELD_NUMBER: _ClassVar[int]
    SAP_ORACLE_RESTORE_WITH_USER_ID_FIELD_NUMBER: _ClassVar[int]
    SAP_ORACLE_RESTORE_WITH_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    NUMBER_OF_MOUNTS_FIELD_NUMBER: _ClassVar[int]
    SAP_MAX_NUM_OUTSTANDING_IO_FIELD_NUMBER: _ClassVar[int]
    LOG_DIR_FIELD_NUMBER: _ClassVar[int]
    LOG_LEVEL_FIELD_NUMBER: _ClassVar[int]
    OS_TYPE_FIELD_NUMBER: _ClassVar[int]
    RPC_TIMEOUT_MSECS_FIELD_NUMBER: _ClassVar[int]
    WRITE_RPC_TIMEOUT_MSECS_FIELD_NUMBER: _ClassVar[int]
    RPC_CALL_CONCURRENCY_FIELD_NUMBER: _ClassVar[int]
    RPC_CALLBACK_CONCURRENCY_FIELD_NUMBER: _ClassVar[int]
    ALIVE_MESSAGE_INTERVAL_MSECS_FIELD_NUMBER: _ClassVar[int]
    LOG_IO_STATS_INTERVAL_FIELD_NUMBER: _ClassVar[int]
    LOG_OUTSTANDING_IO_OFFSET_INTERVAL_MSECS_FIELD_NUMBER: _ClassVar[int]
    CATALOG_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    ENABLE_IMMUTABLE_VIEW_FIELD_NUMBER: _ClassVar[int]
    KEEP_ALIVE_POLLING_INTERVAL_SECS_FIELD_NUMBER: _ClassVar[int]
    SAP_CERTIFICATE_CONFIG_PATH_FIELD_NUMBER: _ClassVar[int]
    N_THREADS_EVENT_LOOP_GROUP_FIELD_NUMBER: _ClassVar[int]
    N_THREADS_NETTY_CHANNEL_EXECUTOR_FIELD_NUMBER: _ClassVar[int]
    LOG_HEAP_DUMP_INTERVAL_MINS_FIELD_NUMBER: _ClassVar[int]
    LOG_THREAD_DUMP_INTERVAL_MINS_FIELD_NUMBER: _ClassVar[int]
    BACKINT_PROTOCOL_VERSION_FIELD_NUMBER: _ClassVar[int]
    cluster_ips: str
    cluster_port: int
    view_name: str
    sap_nfs_mount_path: str
    sap_nfs_mount_options: str
    sap_max_read_write_retries: int
    sap_max_io_size_in_bytes: int
    sap_max_io_asynchronous_callback_concurrency: int
    sap_nfs_create_file_permission: str
    sap_nfs_create_directory_permission: str
    sap_max_backup_streams: int
    sap_max_restore_streams: int
    sap_max_metafiles_read_concurrency: int
    sap_max_inquire_period_days: int
    sap_max_ebid_create_retries: int
    sap_max_logs_directories_retention_count: int
    database_type: str
    service_type: str
    sap_oracle_online_backup_initial_start_time_to_check_switch_log_file_in_seconds: int
    sap_oracle_online_backup_interval_time_to_check_switch_log_file_in_seconds: int
    sap_oracle_online_backup_initial_start_time_to_check_backup_finished_in_seconds: int
    sap_oracle_online_backup_interval_time_to_check_backup_finished_in_seconds: int
    sap_oracle_online_backup_delay_time_to_start_backup_switch_in_seconds: int
    sap_oracle_online_backup_delay_time_to_check_backup_progress_in_seconds: int
    sap_oracle_online_backup_max_switch_wait_time_in_milli_seconds: int
    sap_oracle_restore_with_user_id: int
    sap_oracle_restore_with_group_id: int
    number_of_mounts: int
    sap_max_num_outstanding_io: int
    log_dir: str
    log_level: str
    os_type: str
    rpc_timeout_msecs: int
    write_rpc_timeout_msecs: int
    rpc_call_concurrency: int
    rpc_callback_concurrency: int
    alive_message_interval_msecs: int
    log_io_stats_interval: int
    log_outstanding_io_offset_interval_msecs: int
    catalog_view_name: str
    enable_immutable_view: bool
    keep_alive_polling_interval_secs: int
    sap_certificate_config_path: str
    n_threads_event_loop_group: int
    n_threads_netty_channel_executor: int
    log_heap_dump_interval_mins: int
    log_thread_dump_interval_mins: int
    backint_protocol_version: str
    def __init__(self, cluster_ips: _Optional[str] = ..., cluster_port: _Optional[int] = ..., view_name: _Optional[str] = ..., sap_nfs_mount_path: _Optional[str] = ..., sap_nfs_mount_options: _Optional[str] = ..., sap_max_read_write_retries: _Optional[int] = ..., sap_max_io_size_in_bytes: _Optional[int] = ..., sap_max_io_asynchronous_callback_concurrency: _Optional[int] = ..., sap_nfs_create_file_permission: _Optional[str] = ..., sap_nfs_create_directory_permission: _Optional[str] = ..., sap_max_backup_streams: _Optional[int] = ..., sap_max_restore_streams: _Optional[int] = ..., sap_max_metafiles_read_concurrency: _Optional[int] = ..., sap_max_inquire_period_days: _Optional[int] = ..., sap_max_ebid_create_retries: _Optional[int] = ..., sap_max_logs_directories_retention_count: _Optional[int] = ..., database_type: _Optional[str] = ..., service_type: _Optional[str] = ..., sap_oracle_online_backup_initial_start_time_to_check_switch_log_file_in_seconds: _Optional[int] = ..., sap_oracle_online_backup_interval_time_to_check_switch_log_file_in_seconds: _Optional[int] = ..., sap_oracle_online_backup_initial_start_time_to_check_backup_finished_in_seconds: _Optional[int] = ..., sap_oracle_online_backup_interval_time_to_check_backup_finished_in_seconds: _Optional[int] = ..., sap_oracle_online_backup_delay_time_to_start_backup_switch_in_seconds: _Optional[int] = ..., sap_oracle_online_backup_delay_time_to_check_backup_progress_in_seconds: _Optional[int] = ..., sap_oracle_online_backup_max_switch_wait_time_in_milli_seconds: _Optional[int] = ..., sap_oracle_restore_with_user_id: _Optional[int] = ..., sap_oracle_restore_with_group_id: _Optional[int] = ..., number_of_mounts: _Optional[int] = ..., sap_max_num_outstanding_io: _Optional[int] = ..., log_dir: _Optional[str] = ..., log_level: _Optional[str] = ..., os_type: _Optional[str] = ..., rpc_timeout_msecs: _Optional[int] = ..., write_rpc_timeout_msecs: _Optional[int] = ..., rpc_call_concurrency: _Optional[int] = ..., rpc_callback_concurrency: _Optional[int] = ..., alive_message_interval_msecs: _Optional[int] = ..., log_io_stats_interval: _Optional[int] = ..., log_outstanding_io_offset_interval_msecs: _Optional[int] = ..., catalog_view_name: _Optional[str] = ..., enable_immutable_view: bool = ..., keep_alive_polling_interval_secs: _Optional[int] = ..., sap_certificate_config_path: _Optional[str] = ..., n_threads_event_loop_group: _Optional[int] = ..., n_threads_netty_channel_executor: _Optional[int] = ..., log_heap_dump_interval_mins: _Optional[int] = ..., log_thread_dump_interval_mins: _Optional[int] = ..., backint_protocol_version: _Optional[str] = ...) -> None: ...

class DataSourceInfo(_message.Message):
    __slots__ = ("type", "path", "ebid", "uid", "gid", "permissions", "is_parent", "snapshot_view_name")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kPipe: _ClassVar[DataSourceInfo.Type]
        kFile: _ClassVar[DataSourceInfo.Type]
        kDirectory: _ClassVar[DataSourceInfo.Type]
        kSpecialFile: _ClassVar[DataSourceInfo.Type]
    kPipe: DataSourceInfo.Type
    kFile: DataSourceInfo.Type
    kDirectory: DataSourceInfo.Type
    kSpecialFile: DataSourceInfo.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    EBID_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    GID_FIELD_NUMBER: _ClassVar[int]
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    IS_PARENT_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    type: DataSourceInfo.Type
    path: str
    ebid: str
    uid: int
    gid: int
    permissions: str
    is_parent: bool
    snapshot_view_name: str
    def __init__(self, type: _Optional[_Union[DataSourceInfo.Type, str]] = ..., path: _Optional[str] = ..., ebid: _Optional[str] = ..., uid: _Optional[int] = ..., gid: _Optional[int] = ..., permissions: _Optional[str] = ..., is_parent: bool = ..., snapshot_view_name: _Optional[str] = ...) -> None: ...

class MetadataProto(_message.Message):
    __slots__ = ("epoch", "count", "backupid", "sid", "backup_level", "source_info_vec", "backup_type")
    EPOCH_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    BACKUPID_FIELD_NUMBER: _ClassVar[int]
    SID_FIELD_NUMBER: _ClassVar[int]
    BACKUP_LEVEL_FIELD_NUMBER: _ClassVar[int]
    SOURCE_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    BACKUP_TYPE_FIELD_NUMBER: _ClassVar[int]
    epoch: int
    count: int
    backupid: str
    sid: str
    backup_level: str
    source_info_vec: _containers.RepeatedCompositeFieldContainer[DataSourceInfo]
    backup_type: str
    def __init__(self, epoch: _Optional[int] = ..., count: _Optional[int] = ..., backupid: _Optional[str] = ..., sid: _Optional[str] = ..., backup_level: _Optional[str] = ..., source_info_vec: _Optional[_Iterable[_Union[DataSourceInfo, _Mapping]]] = ..., backup_type: _Optional[str] = ...) -> None: ...
