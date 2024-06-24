from siren.base import error_pb2 as _error_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LogLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kUnknown: _ClassVar[LogLevel]
    kInfo: _ClassVar[LogLevel]
    kWarning: _ClassVar[LogLevel]
    kError: _ClassVar[LogLevel]
    kFatal: _ClassVar[LogLevel]
kUnknown: LogLevel
kInfo: LogLevel
kWarning: LogLevel
kError: LogLevel
kFatal: LogLevel

class SirenUrisProto(_message.Message):
    __slots__ = ("base_uri", "api_version", "node_logs_uri", "node_cores_uri", "node_logs_find_uri", "cluster_logs_uri", "cluster_logs_find_uri", "cluster_logs_find_opts_uri", "local_logs_uri", "local_logs_find_uri", "local_logs_find_opts_uri", "remote_page_uri", "cluster_timecapsule_uri", "node_timecapsule_list_uri", "node_timecapsule_uri", "node_timecapsules_delete_uri", "cluster_source_diagnostics_uri", "node_source_diagnostics_uri", "node_source_diagnostics_delete_uri", "cluster_network_capture_uri", "cluster_schedule_timecapsule_uri", "node_siren_uri", "cluster_timecapsule_schedule_delete_uri", "cluster_timecapsule_schedule_add_uri", "node_timecapsule_schedule_delete_uri", "node_timecapsule_bundle_info_add_uri", "node_timecapsule_bundle_info_list_uri", "timecapsule_current_status_uri", "hc_cli_uri", "hc_cli_start_uri", "hc_cli_read_uri", "hc_cli_run_uri", "hc_cli_clusterips_uri", "hc_cli_resultdata_uri", "hc_cli_file_uri", "cluster_forensics_uri", "node_forensics_list_uri", "node_forensics_delete_uri", "node_forensics_uri", "hc_cli_fingerprint_uri", "hc_cli_fixnow_uri", "hc_cli_fixnow_result_uri")
    BASE_URI_FIELD_NUMBER: _ClassVar[int]
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    NODE_LOGS_URI_FIELD_NUMBER: _ClassVar[int]
    NODE_CORES_URI_FIELD_NUMBER: _ClassVar[int]
    NODE_LOGS_FIND_URI_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_LOGS_URI_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_LOGS_FIND_URI_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_LOGS_FIND_OPTS_URI_FIELD_NUMBER: _ClassVar[int]
    LOCAL_LOGS_URI_FIELD_NUMBER: _ClassVar[int]
    LOCAL_LOGS_FIND_URI_FIELD_NUMBER: _ClassVar[int]
    LOCAL_LOGS_FIND_OPTS_URI_FIELD_NUMBER: _ClassVar[int]
    REMOTE_PAGE_URI_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_TIMECAPSULE_URI_FIELD_NUMBER: _ClassVar[int]
    NODE_TIMECAPSULE_LIST_URI_FIELD_NUMBER: _ClassVar[int]
    NODE_TIMECAPSULE_URI_FIELD_NUMBER: _ClassVar[int]
    NODE_TIMECAPSULES_DELETE_URI_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_SOURCE_DIAGNOSTICS_URI_FIELD_NUMBER: _ClassVar[int]
    NODE_SOURCE_DIAGNOSTICS_URI_FIELD_NUMBER: _ClassVar[int]
    NODE_SOURCE_DIAGNOSTICS_DELETE_URI_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_NETWORK_CAPTURE_URI_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_SCHEDULE_TIMECAPSULE_URI_FIELD_NUMBER: _ClassVar[int]
    NODE_SIREN_URI_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_TIMECAPSULE_SCHEDULE_DELETE_URI_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_TIMECAPSULE_SCHEDULE_ADD_URI_FIELD_NUMBER: _ClassVar[int]
    NODE_TIMECAPSULE_SCHEDULE_DELETE_URI_FIELD_NUMBER: _ClassVar[int]
    NODE_TIMECAPSULE_BUNDLE_INFO_ADD_URI_FIELD_NUMBER: _ClassVar[int]
    NODE_TIMECAPSULE_BUNDLE_INFO_LIST_URI_FIELD_NUMBER: _ClassVar[int]
    TIMECAPSULE_CURRENT_STATUS_URI_FIELD_NUMBER: _ClassVar[int]
    HC_CLI_URI_FIELD_NUMBER: _ClassVar[int]
    HC_CLI_START_URI_FIELD_NUMBER: _ClassVar[int]
    HC_CLI_READ_URI_FIELD_NUMBER: _ClassVar[int]
    HC_CLI_RUN_URI_FIELD_NUMBER: _ClassVar[int]
    HC_CLI_CLUSTERIPS_URI_FIELD_NUMBER: _ClassVar[int]
    HC_CLI_RESULTDATA_URI_FIELD_NUMBER: _ClassVar[int]
    HC_CLI_FILE_URI_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_FORENSICS_URI_FIELD_NUMBER: _ClassVar[int]
    NODE_FORENSICS_LIST_URI_FIELD_NUMBER: _ClassVar[int]
    NODE_FORENSICS_DELETE_URI_FIELD_NUMBER: _ClassVar[int]
    NODE_FORENSICS_URI_FIELD_NUMBER: _ClassVar[int]
    HC_CLI_FINGERPRINT_URI_FIELD_NUMBER: _ClassVar[int]
    HC_CLI_FIXNOW_URI_FIELD_NUMBER: _ClassVar[int]
    HC_CLI_FIXNOW_RESULT_URI_FIELD_NUMBER: _ClassVar[int]
    base_uri: str
    api_version: str
    node_logs_uri: str
    node_cores_uri: str
    node_logs_find_uri: str
    cluster_logs_uri: str
    cluster_logs_find_uri: str
    cluster_logs_find_opts_uri: str
    local_logs_uri: str
    local_logs_find_uri: str
    local_logs_find_opts_uri: str
    remote_page_uri: str
    cluster_timecapsule_uri: str
    node_timecapsule_list_uri: str
    node_timecapsule_uri: str
    node_timecapsules_delete_uri: str
    cluster_source_diagnostics_uri: str
    node_source_diagnostics_uri: str
    node_source_diagnostics_delete_uri: str
    cluster_network_capture_uri: str
    cluster_schedule_timecapsule_uri: str
    node_siren_uri: str
    cluster_timecapsule_schedule_delete_uri: str
    cluster_timecapsule_schedule_add_uri: str
    node_timecapsule_schedule_delete_uri: str
    node_timecapsule_bundle_info_add_uri: str
    node_timecapsule_bundle_info_list_uri: str
    timecapsule_current_status_uri: str
    hc_cli_uri: str
    hc_cli_start_uri: str
    hc_cli_read_uri: str
    hc_cli_run_uri: str
    hc_cli_clusterips_uri: str
    hc_cli_resultdata_uri: str
    hc_cli_file_uri: str
    cluster_forensics_uri: str
    node_forensics_list_uri: str
    node_forensics_delete_uri: str
    node_forensics_uri: str
    hc_cli_fingerprint_uri: str
    hc_cli_fixnow_uri: str
    hc_cli_fixnow_result_uri: str
    def __init__(self, base_uri: _Optional[str] = ..., api_version: _Optional[str] = ..., node_logs_uri: _Optional[str] = ..., node_cores_uri: _Optional[str] = ..., node_logs_find_uri: _Optional[str] = ..., cluster_logs_uri: _Optional[str] = ..., cluster_logs_find_uri: _Optional[str] = ..., cluster_logs_find_opts_uri: _Optional[str] = ..., local_logs_uri: _Optional[str] = ..., local_logs_find_uri: _Optional[str] = ..., local_logs_find_opts_uri: _Optional[str] = ..., remote_page_uri: _Optional[str] = ..., cluster_timecapsule_uri: _Optional[str] = ..., node_timecapsule_list_uri: _Optional[str] = ..., node_timecapsule_uri: _Optional[str] = ..., node_timecapsules_delete_uri: _Optional[str] = ..., cluster_source_diagnostics_uri: _Optional[str] = ..., node_source_diagnostics_uri: _Optional[str] = ..., node_source_diagnostics_delete_uri: _Optional[str] = ..., cluster_network_capture_uri: _Optional[str] = ..., cluster_schedule_timecapsule_uri: _Optional[str] = ..., node_siren_uri: _Optional[str] = ..., cluster_timecapsule_schedule_delete_uri: _Optional[str] = ..., cluster_timecapsule_schedule_add_uri: _Optional[str] = ..., node_timecapsule_schedule_delete_uri: _Optional[str] = ..., node_timecapsule_bundle_info_add_uri: _Optional[str] = ..., node_timecapsule_bundle_info_list_uri: _Optional[str] = ..., timecapsule_current_status_uri: _Optional[str] = ..., hc_cli_uri: _Optional[str] = ..., hc_cli_start_uri: _Optional[str] = ..., hc_cli_read_uri: _Optional[str] = ..., hc_cli_run_uri: _Optional[str] = ..., hc_cli_clusterips_uri: _Optional[str] = ..., hc_cli_resultdata_uri: _Optional[str] = ..., hc_cli_file_uri: _Optional[str] = ..., cluster_forensics_uri: _Optional[str] = ..., node_forensics_list_uri: _Optional[str] = ..., node_forensics_delete_uri: _Optional[str] = ..., node_forensics_uri: _Optional[str] = ..., hc_cli_fingerprint_uri: _Optional[str] = ..., hc_cli_fixnow_uri: _Optional[str] = ..., hc_cli_fixnow_result_uri: _Optional[str] = ...) -> None: ...

class LogData(_message.Message):
    __slots__ = ("node_ip", "service_name", "log_level", "timestamp_secs", "thread_id", "filename", "line_num", "msg", "dedup_timestamp_vec", "dedup_count", "dedup_node_ip_vec", "source")
    NODE_IP_FIELD_NUMBER: _ClassVar[int]
    SERVICE_NAME_FIELD_NUMBER: _ClassVar[int]
    LOG_LEVEL_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_SECS_FIELD_NUMBER: _ClassVar[int]
    THREAD_ID_FIELD_NUMBER: _ClassVar[int]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    LINE_NUM_FIELD_NUMBER: _ClassVar[int]
    MSG_FIELD_NUMBER: _ClassVar[int]
    DEDUP_TIMESTAMP_VEC_FIELD_NUMBER: _ClassVar[int]
    DEDUP_COUNT_FIELD_NUMBER: _ClassVar[int]
    DEDUP_NODE_IP_VEC_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    node_ip: str
    service_name: str
    log_level: LogLevel
    timestamp_secs: int
    thread_id: int
    filename: str
    line_num: int
    msg: str
    dedup_timestamp_vec: _containers.RepeatedScalarFieldContainer[int]
    dedup_count: int
    dedup_node_ip_vec: _containers.RepeatedScalarFieldContainer[str]
    source: str
    def __init__(self, node_ip: _Optional[str] = ..., service_name: _Optional[str] = ..., log_level: _Optional[_Union[LogLevel, str]] = ..., timestamp_secs: _Optional[int] = ..., thread_id: _Optional[int] = ..., filename: _Optional[str] = ..., line_num: _Optional[int] = ..., msg: _Optional[str] = ..., dedup_timestamp_vec: _Optional[_Iterable[int]] = ..., dedup_count: _Optional[int] = ..., dedup_node_ip_vec: _Optional[_Iterable[str]] = ..., source: _Optional[str] = ...) -> None: ...

class LogsFindOpts(_message.Message):
    __slots__ = ("node_ip_vec", "service_name_vec", "log_level", "start_time_secs", "end_time_secs", "limit", "directory", "max_dedup_timestamps", "dedup_time_window_secs", "keyword_vec", "stdouterr", "timeout_secs")
    NODE_IP_VEC_FIELD_NUMBER: _ClassVar[int]
    SERVICE_NAME_VEC_FIELD_NUMBER: _ClassVar[int]
    LOG_LEVEL_FIELD_NUMBER: _ClassVar[int]
    START_TIME_SECS_FIELD_NUMBER: _ClassVar[int]
    END_TIME_SECS_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    DIRECTORY_FIELD_NUMBER: _ClassVar[int]
    MAX_DEDUP_TIMESTAMPS_FIELD_NUMBER: _ClassVar[int]
    DEDUP_TIME_WINDOW_SECS_FIELD_NUMBER: _ClassVar[int]
    KEYWORD_VEC_FIELD_NUMBER: _ClassVar[int]
    STDOUTERR_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_SECS_FIELD_NUMBER: _ClassVar[int]
    node_ip_vec: _containers.RepeatedScalarFieldContainer[str]
    service_name_vec: _containers.RepeatedScalarFieldContainer[str]
    log_level: LogLevel
    start_time_secs: int
    end_time_secs: int
    limit: int
    directory: str
    max_dedup_timestamps: int
    dedup_time_window_secs: int
    keyword_vec: _containers.RepeatedScalarFieldContainer[str]
    stdouterr: bool
    timeout_secs: int
    def __init__(self, node_ip_vec: _Optional[_Iterable[str]] = ..., service_name_vec: _Optional[_Iterable[str]] = ..., log_level: _Optional[_Union[LogLevel, str]] = ..., start_time_secs: _Optional[int] = ..., end_time_secs: _Optional[int] = ..., limit: _Optional[int] = ..., directory: _Optional[str] = ..., max_dedup_timestamps: _Optional[int] = ..., dedup_time_window_secs: _Optional[int] = ..., keyword_vec: _Optional[_Iterable[str]] = ..., stdouterr: bool = ..., timeout_secs: _Optional[int] = ...) -> None: ...

class NodeLogsFindArg(_message.Message):
    __slots__ = ("opts",)
    OPTS_FIELD_NUMBER: _ClassVar[int]
    opts: LogsFindOpts
    def __init__(self, opts: _Optional[_Union[LogsFindOpts, _Mapping]] = ...) -> None: ...

class NodeLogsFindResult(_message.Message):
    __slots__ = ("error", "log_data_vec", "node_ip")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    LOG_DATA_VEC_FIELD_NUMBER: _ClassVar[int]
    NODE_IP_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    log_data_vec: _containers.RepeatedCompositeFieldContainer[LogData]
    node_ip: str
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., log_data_vec: _Optional[_Iterable[_Union[LogData, _Mapping]]] = ..., node_ip: _Optional[str] = ...) -> None: ...

class ClusterLogsFindArg(_message.Message):
    __slots__ = ("opts",)
    OPTS_FIELD_NUMBER: _ClassVar[int]
    opts: LogsFindOpts
    def __init__(self, opts: _Optional[_Union[LogsFindOpts, _Mapping]] = ...) -> None: ...

class ClusterLogsFindResult(_message.Message):
    __slots__ = ("error_vec", "log_data_vec")
    ERROR_VEC_FIELD_NUMBER: _ClassVar[int]
    LOG_DATA_VEC_FIELD_NUMBER: _ClassVar[int]
    error_vec: _containers.RepeatedCompositeFieldContainer[_error_pb2.ErrorProto]
    log_data_vec: _containers.RepeatedCompositeFieldContainer[LogData]
    def __init__(self, error_vec: _Optional[_Iterable[_Union[_error_pb2.ErrorProto, _Mapping]]] = ..., log_data_vec: _Optional[_Iterable[_Union[LogData, _Mapping]]] = ...) -> None: ...

class ClusterLogsFindOptsResult(_message.Message):
    __slots__ = ("error", "opts", "dedup_across_nodes", "linkify")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    OPTS_FIELD_NUMBER: _ClassVar[int]
    DEDUP_ACROSS_NODES_FIELD_NUMBER: _ClassVar[int]
    LINKIFY_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    opts: LogsFindOpts
    dedup_across_nodes: bool
    linkify: bool
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., opts: _Optional[_Union[LogsFindOpts, _Mapping]] = ..., dedup_across_nodes: bool = ..., linkify: bool = ...) -> None: ...

class LocalLogsFindArg(_message.Message):
    __slots__ = ("opts",)
    OPTS_FIELD_NUMBER: _ClassVar[int]
    opts: LogsFindOpts
    def __init__(self, opts: _Optional[_Union[LogsFindOpts, _Mapping]] = ...) -> None: ...

class LocalLogsFindResult(_message.Message):
    __slots__ = ("error", "log_data_vec")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    LOG_DATA_VEC_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    log_data_vec: _containers.RepeatedCompositeFieldContainer[LogData]
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., log_data_vec: _Optional[_Iterable[_Union[LogData, _Mapping]]] = ...) -> None: ...

class LocalLogsFindOptsResult(_message.Message):
    __slots__ = ("error", "opts", "log_dir_info_vec", "linkify")
    class LogDirInfo(_message.Message):
        __slots__ = ("directory", "node_ip_vec", "service_name_vec")
        DIRECTORY_FIELD_NUMBER: _ClassVar[int]
        NODE_IP_VEC_FIELD_NUMBER: _ClassVar[int]
        SERVICE_NAME_VEC_FIELD_NUMBER: _ClassVar[int]
        directory: str
        node_ip_vec: _containers.RepeatedScalarFieldContainer[str]
        service_name_vec: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, directory: _Optional[str] = ..., node_ip_vec: _Optional[_Iterable[str]] = ..., service_name_vec: _Optional[_Iterable[str]] = ...) -> None: ...
    ERROR_FIELD_NUMBER: _ClassVar[int]
    OPTS_FIELD_NUMBER: _ClassVar[int]
    LOG_DIR_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    LINKIFY_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    opts: LogsFindOpts
    log_dir_info_vec: _containers.RepeatedCompositeFieldContainer[LocalLogsFindOptsResult.LogDirInfo]
    linkify: bool
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., opts: _Optional[_Union[LogsFindOpts, _Mapping]] = ..., log_dir_info_vec: _Optional[_Iterable[_Union[LocalLogsFindOptsResult.LogDirInfo, _Mapping]]] = ..., linkify: bool = ...) -> None: ...

class NodeSourceDiagnosticsDeleteArg(_message.Message):
    __slots__ = ("source_diagnostics_id",)
    SOURCE_DIAGNOSTICS_ID_FIELD_NUMBER: _ClassVar[int]
    source_diagnostics_id: str
    def __init__(self, source_diagnostics_id: _Optional[str] = ...) -> None: ...

class NodeTimecapsuleDeleteArg(_message.Message):
    __slots__ = ("timecapsule_id", "node_ip")
    TIMECAPSULE_ID_FIELD_NUMBER: _ClassVar[int]
    NODE_IP_FIELD_NUMBER: _ClassVar[int]
    timecapsule_id: str
    node_ip: str
    def __init__(self, timecapsule_id: _Optional[str] = ..., node_ip: _Optional[str] = ...) -> None: ...

class NodeForensicsDeleteArg(_message.Message):
    __slots__ = ("forensics_report_id", "node_ip")
    FORENSICS_REPORT_ID_FIELD_NUMBER: _ClassVar[int]
    NODE_IP_FIELD_NUMBER: _ClassVar[int]
    forensics_report_id: str
    node_ip: str
    def __init__(self, forensics_report_id: _Optional[str] = ..., node_ip: _Optional[str] = ...) -> None: ...
