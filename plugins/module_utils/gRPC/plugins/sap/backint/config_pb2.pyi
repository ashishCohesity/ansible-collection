from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ParamsProto(_message.Message):
    __slots__ = ("cluster_ips", "cluster_port", "view_name", "io_thread_count", "max_outstanding_io", "max_cached_io", "max_io_size_bytes", "rpc_timeout_msecs", "certificate_config_path", "inquire_period_days", "log_dir", "vlog_level", "metafiles_read_concurrency", "write_rpc_timeout_msecs", "add_back_time_msecs", "bridge_snap_fs_stub_max_retries", "max_backup_streams", "max_restore_streams", "enable_dedup_write", "enable_dedup_read", "enable_bifrost_auth", "initial_create_file_size_in_gb", "enable_read_forwarding", "enable_write_forwarding", "vip_selection_type", "bridge_wan_stub_remote_endpoint_acceptable_failure_threshold", "audit_pipe_latency", "interval_to_audit_pipe_latency", "log_retention_size_mb", "disable_sha1_streams", "sap_hana_enable_error_injection", "inquire_without_pipe_name_match_for_ebid", "restore_without_pipe_name_match_for_ebid", "bridge_wan_stub_remote_endpoint_failure_timeframe_window_msecs", "qos_principal_priority", "enable_clean_up_logs_on_log_backup", "progress_directory_path", "et_log_backup_param_file", "job_id", "is_et_log_backup_enabled_for_db", "use_tcp_proxy", "proxy_port_range")
    class VIPSelectionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kConsistentHash: _ClassVar[ParamsProto.VIPSelectionType]
        kRoundRobin: _ClassVar[ParamsProto.VIPSelectionType]
        kLeastConnections: _ClassVar[ParamsProto.VIPSelectionType]
        kMixedMode: _ClassVar[ParamsProto.VIPSelectionType]
    kConsistentHash: ParamsProto.VIPSelectionType
    kRoundRobin: ParamsProto.VIPSelectionType
    kLeastConnections: ParamsProto.VIPSelectionType
    kMixedMode: ParamsProto.VIPSelectionType
    class Priority(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kCritical: _ClassVar[ParamsProto.Priority]
        kHigh: _ClassVar[ParamsProto.Priority]
        kMedium: _ClassVar[ParamsProto.Priority]
        kLow: _ClassVar[ParamsProto.Priority]
        kNumPriorities: _ClassVar[ParamsProto.Priority]
        kNoPriority: _ClassVar[ParamsProto.Priority]
        kNumPrioritiesUpperLimit: _ClassVar[ParamsProto.Priority]
    kCritical: ParamsProto.Priority
    kHigh: ParamsProto.Priority
    kMedium: ParamsProto.Priority
    kLow: ParamsProto.Priority
    kNumPriorities: ParamsProto.Priority
    kNoPriority: ParamsProto.Priority
    kNumPrioritiesUpperLimit: ParamsProto.Priority
    CLUSTER_IPS_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_PORT_FIELD_NUMBER: _ClassVar[int]
    VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    IO_THREAD_COUNT_FIELD_NUMBER: _ClassVar[int]
    MAX_OUTSTANDING_IO_FIELD_NUMBER: _ClassVar[int]
    MAX_CACHED_IO_FIELD_NUMBER: _ClassVar[int]
    MAX_IO_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    RPC_TIMEOUT_MSECS_FIELD_NUMBER: _ClassVar[int]
    CERTIFICATE_CONFIG_PATH_FIELD_NUMBER: _ClassVar[int]
    INQUIRE_PERIOD_DAYS_FIELD_NUMBER: _ClassVar[int]
    LOG_DIR_FIELD_NUMBER: _ClassVar[int]
    VLOG_LEVEL_FIELD_NUMBER: _ClassVar[int]
    METAFILES_READ_CONCURRENCY_FIELD_NUMBER: _ClassVar[int]
    WRITE_RPC_TIMEOUT_MSECS_FIELD_NUMBER: _ClassVar[int]
    ADD_BACK_TIME_MSECS_FIELD_NUMBER: _ClassVar[int]
    BRIDGE_SNAP_FS_STUB_MAX_RETRIES_FIELD_NUMBER: _ClassVar[int]
    MAX_BACKUP_STREAMS_FIELD_NUMBER: _ClassVar[int]
    MAX_RESTORE_STREAMS_FIELD_NUMBER: _ClassVar[int]
    ENABLE_DEDUP_WRITE_FIELD_NUMBER: _ClassVar[int]
    ENABLE_DEDUP_READ_FIELD_NUMBER: _ClassVar[int]
    ENABLE_BIFROST_AUTH_FIELD_NUMBER: _ClassVar[int]
    INITIAL_CREATE_FILE_SIZE_IN_GB_FIELD_NUMBER: _ClassVar[int]
    ENABLE_READ_FORWARDING_FIELD_NUMBER: _ClassVar[int]
    ENABLE_WRITE_FORWARDING_FIELD_NUMBER: _ClassVar[int]
    VIP_SELECTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    BRIDGE_WAN_STUB_REMOTE_ENDPOINT_ACCEPTABLE_FAILURE_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    AUDIT_PIPE_LATENCY_FIELD_NUMBER: _ClassVar[int]
    INTERVAL_TO_AUDIT_PIPE_LATENCY_FIELD_NUMBER: _ClassVar[int]
    LOG_RETENTION_SIZE_MB_FIELD_NUMBER: _ClassVar[int]
    DISABLE_SHA1_STREAMS_FIELD_NUMBER: _ClassVar[int]
    SAP_HANA_ENABLE_ERROR_INJECTION_FIELD_NUMBER: _ClassVar[int]
    INQUIRE_WITHOUT_PIPE_NAME_MATCH_FOR_EBID_FIELD_NUMBER: _ClassVar[int]
    RESTORE_WITHOUT_PIPE_NAME_MATCH_FOR_EBID_FIELD_NUMBER: _ClassVar[int]
    BRIDGE_WAN_STUB_REMOTE_ENDPOINT_FAILURE_TIMEFRAME_WINDOW_MSECS_FIELD_NUMBER: _ClassVar[int]
    QOS_PRINCIPAL_PRIORITY_FIELD_NUMBER: _ClassVar[int]
    ENABLE_CLEAN_UP_LOGS_ON_LOG_BACKUP_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_DIRECTORY_PATH_FIELD_NUMBER: _ClassVar[int]
    ET_LOG_BACKUP_PARAM_FILE_FIELD_NUMBER: _ClassVar[int]
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    IS_ET_LOG_BACKUP_ENABLED_FOR_DB_FIELD_NUMBER: _ClassVar[int]
    USE_TCP_PROXY_FIELD_NUMBER: _ClassVar[int]
    PROXY_PORT_RANGE_FIELD_NUMBER: _ClassVar[int]
    cluster_ips: str
    cluster_port: int
    view_name: str
    io_thread_count: int
    max_outstanding_io: int
    max_cached_io: int
    max_io_size_bytes: int
    rpc_timeout_msecs: int
    certificate_config_path: str
    inquire_period_days: int
    log_dir: str
    vlog_level: int
    metafiles_read_concurrency: int
    write_rpc_timeout_msecs: int
    add_back_time_msecs: int
    bridge_snap_fs_stub_max_retries: int
    max_backup_streams: int
    max_restore_streams: int
    enable_dedup_write: bool
    enable_dedup_read: bool
    enable_bifrost_auth: bool
    initial_create_file_size_in_gb: int
    enable_read_forwarding: bool
    enable_write_forwarding: bool
    vip_selection_type: ParamsProto.VIPSelectionType
    bridge_wan_stub_remote_endpoint_acceptable_failure_threshold: int
    audit_pipe_latency: bool
    interval_to_audit_pipe_latency: int
    log_retention_size_mb: int
    disable_sha1_streams: bool
    sap_hana_enable_error_injection: bool
    inquire_without_pipe_name_match_for_ebid: bool
    restore_without_pipe_name_match_for_ebid: bool
    bridge_wan_stub_remote_endpoint_failure_timeframe_window_msecs: int
    qos_principal_priority: ParamsProto.Priority
    enable_clean_up_logs_on_log_backup: bool
    progress_directory_path: str
    et_log_backup_param_file: str
    job_id: str
    is_et_log_backup_enabled_for_db: bool
    use_tcp_proxy: bool
    proxy_port_range: str
    def __init__(self, cluster_ips: _Optional[str] = ..., cluster_port: _Optional[int] = ..., view_name: _Optional[str] = ..., io_thread_count: _Optional[int] = ..., max_outstanding_io: _Optional[int] = ..., max_cached_io: _Optional[int] = ..., max_io_size_bytes: _Optional[int] = ..., rpc_timeout_msecs: _Optional[int] = ..., certificate_config_path: _Optional[str] = ..., inquire_period_days: _Optional[int] = ..., log_dir: _Optional[str] = ..., vlog_level: _Optional[int] = ..., metafiles_read_concurrency: _Optional[int] = ..., write_rpc_timeout_msecs: _Optional[int] = ..., add_back_time_msecs: _Optional[int] = ..., bridge_snap_fs_stub_max_retries: _Optional[int] = ..., max_backup_streams: _Optional[int] = ..., max_restore_streams: _Optional[int] = ..., enable_dedup_write: bool = ..., enable_dedup_read: bool = ..., enable_bifrost_auth: bool = ..., initial_create_file_size_in_gb: _Optional[int] = ..., enable_read_forwarding: bool = ..., enable_write_forwarding: bool = ..., vip_selection_type: _Optional[_Union[ParamsProto.VIPSelectionType, str]] = ..., bridge_wan_stub_remote_endpoint_acceptable_failure_threshold: _Optional[int] = ..., audit_pipe_latency: bool = ..., interval_to_audit_pipe_latency: _Optional[int] = ..., log_retention_size_mb: _Optional[int] = ..., disable_sha1_streams: bool = ..., sap_hana_enable_error_injection: bool = ..., inquire_without_pipe_name_match_for_ebid: bool = ..., restore_without_pipe_name_match_for_ebid: bool = ..., bridge_wan_stub_remote_endpoint_failure_timeframe_window_msecs: _Optional[int] = ..., qos_principal_priority: _Optional[_Union[ParamsProto.Priority, str]] = ..., enable_clean_up_logs_on_log_backup: bool = ..., progress_directory_path: _Optional[str] = ..., et_log_backup_param_file: _Optional[str] = ..., job_id: _Optional[str] = ..., is_et_log_backup_enabled_for_db: bool = ..., use_tcp_proxy: bool = ..., proxy_port_range: _Optional[str] = ...) -> None: ...

class DataSourceInfo(_message.Message):
    __slots__ = ("type", "path", "ebid")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kPipe: _ClassVar[DataSourceInfo.Type]
        kFile: _ClassVar[DataSourceInfo.Type]
    kPipe: DataSourceInfo.Type
    kFile: DataSourceInfo.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    EBID_FIELD_NUMBER: _ClassVar[int]
    type: DataSourceInfo.Type
    path: str
    ebid: str
    def __init__(self, type: _Optional[_Union[DataSourceInfo.Type, str]] = ..., path: _Optional[str] = ..., ebid: _Optional[str] = ...) -> None: ...

class MetadataProto(_message.Message):
    __slots__ = ("epoch", "count", "backupid", "sid", "backup_level", "source_info_vec")
    EPOCH_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    BACKUPID_FIELD_NUMBER: _ClassVar[int]
    SID_FIELD_NUMBER: _ClassVar[int]
    BACKUP_LEVEL_FIELD_NUMBER: _ClassVar[int]
    SOURCE_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    epoch: int
    count: int
    backupid: str
    sid: str
    backup_level: str
    source_info_vec: _containers.RepeatedCompositeFieldContainer[DataSourceInfo]
    def __init__(self, epoch: _Optional[int] = ..., count: _Optional[int] = ..., backupid: _Optional[str] = ..., sid: _Optional[str] = ..., backup_level: _Optional[str] = ..., source_info_vec: _Optional[_Iterable[_Union[DataSourceInfo, _Mapping]]] = ...) -> None: ...

class BackintCertificateProto(_message.Message):
    __slots__ = ("connection_config_vec",)
    class ConnectionConfig(_message.Message):
        __slots__ = ("cluster_cert", "self_cert", "self_cert_priv_key_encrypted", "tenant_id", "cluster_id", "grpc_server_common_name")
        CLUSTER_CERT_FIELD_NUMBER: _ClassVar[int]
        SELF_CERT_FIELD_NUMBER: _ClassVar[int]
        SELF_CERT_PRIV_KEY_ENCRYPTED_FIELD_NUMBER: _ClassVar[int]
        TENANT_ID_FIELD_NUMBER: _ClassVar[int]
        CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
        GRPC_SERVER_COMMON_NAME_FIELD_NUMBER: _ClassVar[int]
        cluster_cert: str
        self_cert: str
        self_cert_priv_key_encrypted: bytes
        tenant_id: str
        cluster_id: int
        grpc_server_common_name: str
        def __init__(self, cluster_cert: _Optional[str] = ..., self_cert: _Optional[str] = ..., self_cert_priv_key_encrypted: _Optional[bytes] = ..., tenant_id: _Optional[str] = ..., cluster_id: _Optional[int] = ..., grpc_server_common_name: _Optional[str] = ...) -> None: ...
    CONNECTION_CONFIG_VEC_FIELD_NUMBER: _ClassVar[int]
    connection_config_vec: _containers.RepeatedCompositeFieldContainer[BackintCertificateProto.ConnectionConfig]
    def __init__(self, connection_config_vec: _Optional[_Iterable[_Union[BackintCertificateProto.ConnectionConfig, _Mapping]]] = ...) -> None: ...
