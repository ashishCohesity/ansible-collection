from bifrost.server import server_config_pb2 as _server_config_pb2
from magneto.agents.base import error_pb2 as _error_pb2
from magneto.agents.base import agent_pb2 as _agent_pb2
from magneto.agents.stub import agent_base_pb2 as _agent_base_pb2
from magneto.agents.stub import agent_param_pb2 as _agent_param_pb2
from magneto.agents.windows.base import hyperv_pb2 as _hyperv_pb2
from magneto.agents.windows.base import vss_pb2 as _vss_pb2
from magneto.agents.windows.stub import hyperv_param_pb2 as _hyperv_param_pb2
from magneto.agents.windows.sql.base import sql_pb2 as _sql_pb2
from magneto.agents.windows.sql.base import sql_param_pb2 as _sql_param_pb2
from magneto.base.entities import sql_pb2 as _sql_pb2_1
from magneto.base import magneto_pb2 as _magneto_pb2
from magneto.base import env_params_pb2 as _env_params_pb2
from magneto.connectors.sql import sql_pb2 as _sql_pb2_1_1
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ReadBytesFromStreamArg(_message.Message):
    __slots__ = ("header", "stream_id", "offset", "num_bytes")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    STREAM_ID_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    NUM_BYTES_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    stream_id: int
    offset: int
    num_bytes: int
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., stream_id: _Optional[int] = ..., offset: _Optional[int] = ..., num_bytes: _Optional[int] = ...) -> None: ...

class ReadBytesFromStreamResult(_message.Message):
    __slots__ = ("error", "bytes_read", "bytes_buffer", "all_bytes_read", "buffer_has_more_bytes")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    BYTES_READ_FIELD_NUMBER: _ClassVar[int]
    BYTES_BUFFER_FIELD_NUMBER: _ClassVar[int]
    ALL_BYTES_READ_FIELD_NUMBER: _ClassVar[int]
    BUFFER_HAS_MORE_BYTES_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    bytes_read: int
    bytes_buffer: bytes
    all_bytes_read: bool
    buffer_has_more_bytes: bool
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., bytes_read: _Optional[int] = ..., bytes_buffer: _Optional[bytes] = ..., all_bytes_read: bool = ..., buffer_has_more_bytes: bool = ...) -> None: ...

class WriteBytesToStreamArg(_message.Message):
    __slots__ = ("header", "stream_id", "offset", "num_bytes", "bytes_buffer", "all_bytes_written")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    STREAM_ID_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    NUM_BYTES_FIELD_NUMBER: _ClassVar[int]
    BYTES_BUFFER_FIELD_NUMBER: _ClassVar[int]
    ALL_BYTES_WRITTEN_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    stream_id: int
    offset: int
    num_bytes: int
    bytes_buffer: bytes
    all_bytes_written: bool
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., stream_id: _Optional[int] = ..., offset: _Optional[int] = ..., num_bytes: _Optional[int] = ..., bytes_buffer: _Optional[bytes] = ..., all_bytes_written: bool = ...) -> None: ...

class WriteBytesToStreamResult(_message.Message):
    __slots__ = ("error", "bytes_written", "total_bytes_written", "force_commit")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    BYTES_WRITTEN_FIELD_NUMBER: _ClassVar[int]
    TOTAL_BYTES_WRITTEN_FIELD_NUMBER: _ClassVar[int]
    FORCE_COMMIT_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    bytes_written: int
    total_bytes_written: int
    force_commit: bool
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., bytes_written: _Optional[int] = ..., total_bytes_written: _Optional[int] = ..., force_commit: bool = ...) -> None: ...

class CommitBytesFromStreamArg(_message.Message):
    __slots__ = ("header", "stream_id", "offset")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    STREAM_ID_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    stream_id: int
    offset: int
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., stream_id: _Optional[int] = ..., offset: _Optional[int] = ...) -> None: ...

class CommitBytesFromStreamResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class CommitBytesToStreamArg(_message.Message):
    __slots__ = ("header", "stream_id", "offset")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    STREAM_ID_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    stream_id: int
    offset: int
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., stream_id: _Optional[int] = ..., offset: _Optional[int] = ...) -> None: ...

class CommitBytesToStreamResult(_message.Message):
    __slots__ = ("error", "offset")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    offset: int
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., offset: _Optional[int] = ...) -> None: ...

class CloseStreamArg(_message.Message):
    __slots__ = ("header", "stream_id", "sql_id", "stream_uuid", "should_rename", "credentials")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    STREAM_ID_FIELD_NUMBER: _ClassVar[int]
    SQL_ID_FIELD_NUMBER: _ClassVar[int]
    STREAM_UUID_FIELD_NUMBER: _ClassVar[int]
    SHOULD_RENAME_FIELD_NUMBER: _ClassVar[int]
    CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    stream_id: int
    sql_id: _sql_pb2_1.SqlId
    stream_uuid: str
    should_rename: bool
    credentials: _sql_pb2_1_1.Credentials
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., stream_id: _Optional[int] = ..., sql_id: _Optional[_Union[_sql_pb2_1.SqlId, _Mapping]] = ..., stream_uuid: _Optional[str] = ..., should_rename: bool = ..., credentials: _Optional[_Union[_sql_pb2_1_1.Credentials, _Mapping]] = ...) -> None: ...

class CloseStreamResult(_message.Message):
    __slots__ = ("error", "sql_id", "backupset_row_info")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    SQL_ID_FIELD_NUMBER: _ClassVar[int]
    BACKUPSET_ROW_INFO_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    sql_id: _sql_pb2_1.SqlId
    backupset_row_info: _sql_pb2_1_1.BackupSetRowInfo
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., sql_id: _Optional[_Union[_sql_pb2_1.SqlId, _Mapping]] = ..., backupset_row_info: _Optional[_Union[_sql_pb2_1_1.BackupSetRowInfo, _Mapping]] = ...) -> None: ...

class VSSNotifyRestoreCompleteArg(_message.Message):
    __slots__ = ("header", "check_task_id", "snapshot_set_id_DEPRECATED")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    CHECK_TASK_ID_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_SET_ID_DEPRECATED_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    check_task_id: bool
    snapshot_set_id_DEPRECATED: bytes
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., check_task_id: bool = ..., snapshot_set_id_DEPRECATED: _Optional[bytes] = ...) -> None: ...

class VSSNotifyRestoreCompleteResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class VssWriterInfo(_message.Message):
    __slots__ = ("vss_writer_metadata",)
    VSS_WRITER_INFO_FIELD_NUMBER: _ClassVar[int]
    vss_writer_info: _descriptor.FieldDescriptor
    VSS_WRITER_METADATA_FIELD_NUMBER: _ClassVar[int]
    vss_writer_metadata: _vss_pb2.VSSWriterMetadataProto
    def __init__(self, vss_writer_metadata: _Optional[_Union[_vss_pb2.VSSWriterMetadataProto, _Mapping]] = ...) -> None: ...

class DiscoverDatabasesArg(_message.Message):
    __slots__ = ("header", "ignore_system_databases", "credentials")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    IGNORE_SYSTEM_DATABASES_FIELD_NUMBER: _ClassVar[int]
    CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    ignore_system_databases: bool
    credentials: _sql_pb2_1_1.Credentials
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., ignore_system_databases: bool = ..., credentials: _Optional[_Union[_sql_pb2_1_1.Credentials, _Mapping]] = ...) -> None: ...

class DiscoverDatabasesResult(_message.Message):
    __slots__ = ("error", "database_info_vec", "offline_instance_id_vec")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    DATABASE_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    OFFLINE_INSTANCE_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    database_info_vec: _containers.RepeatedCompositeFieldContainer[_sql_pb2.SQLDatabaseInfo]
    offline_instance_id_vec: _containers.RepeatedScalarFieldContainer[bytes]
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., database_info_vec: _Optional[_Iterable[_Union[_sql_pb2.SQLDatabaseInfo, _Mapping]]] = ..., offline_instance_id_vec: _Optional[_Iterable[bytes]] = ...) -> None: ...

class ExecuteSQLStatementsArg(_message.Message):
    __slots__ = ("header", "instance_name", "sql_statement_vec")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_NAME_FIELD_NUMBER: _ClassVar[int]
    SQL_STATEMENT_VEC_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    instance_name: bytes
    sql_statement_vec: _containers.RepeatedScalarFieldContainer[bytes]
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., instance_name: _Optional[bytes] = ..., sql_statement_vec: _Optional[_Iterable[bytes]] = ...) -> None: ...

class ExecuteSQLStatementsResult(_message.Message):
    __slots__ = ("error", "result_vec")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    RESULT_VEC_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    result_vec: _containers.RepeatedCompositeFieldContainer[_sql_param_pb2.SQLResult]
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., result_vec: _Optional[_Iterable[_Union[_sql_param_pb2.SQLResult, _Mapping]]] = ...) -> None: ...

class AbortSQLVDIOperationArg(_message.Message):
    __slots__ = ("header", "sql_id")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    SQL_ID_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    sql_id: _sql_pb2_1.SqlId
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., sql_id: _Optional[_Union[_sql_pb2_1.SqlId, _Mapping]] = ...) -> None: ...

class AbortSQLVDIOperationResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class InitSQLLogBackupArg(_message.Message):
    __slots__ = ("header", "sql_id", "stream", "is_tail_log_backup", "is_copy_only", "enable_checksum", "continue_after_error")
    class Stream(_message.Message):
        __slots__ = ("id", "buffer_size_bytes")
        ID_FIELD_NUMBER: _ClassVar[int]
        BUFFER_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
        id: int
        buffer_size_bytes: int
        def __init__(self, id: _Optional[int] = ..., buffer_size_bytes: _Optional[int] = ...) -> None: ...
    HEADER_FIELD_NUMBER: _ClassVar[int]
    SQL_ID_FIELD_NUMBER: _ClassVar[int]
    STREAM_FIELD_NUMBER: _ClassVar[int]
    IS_TAIL_LOG_BACKUP_FIELD_NUMBER: _ClassVar[int]
    IS_COPY_ONLY_FIELD_NUMBER: _ClassVar[int]
    ENABLE_CHECKSUM_FIELD_NUMBER: _ClassVar[int]
    CONTINUE_AFTER_ERROR_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    sql_id: _sql_pb2_1.SqlId
    stream: InitSQLLogBackupArg.Stream
    is_tail_log_backup: bool
    is_copy_only: bool
    enable_checksum: bool
    continue_after_error: bool
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., sql_id: _Optional[_Union[_sql_pb2_1.SqlId, _Mapping]] = ..., stream: _Optional[_Union[InitSQLLogBackupArg.Stream, _Mapping]] = ..., is_tail_log_backup: bool = ..., is_copy_only: bool = ..., enable_checksum: bool = ..., continue_after_error: bool = ...) -> None: ...

class InitSQLLogBackupResult(_message.Message):
    __slots__ = ("error", "uuid")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    uuid: str
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., uuid: _Optional[str] = ...) -> None: ...

class StartSQLNativeBackupArg(_message.Message):
    __slots__ = ("header", "db_name", "backup_type", "bridge_node_vip_vec", "file_name_vec", "view_name", "tail_log", "copy_only", "use_smb", "with_clause", "enable_checksum", "continue_after_error", "bridge_node_vip_fqdn", "sql_vdi_command_timeout_secs", "sql_vdi_configuration_wait_time_secs", "bifrost_server_config_proto", "stats_container_id", "oio_bytes_per_stream_limit", "oio_count_per_stream_limit", "disable_agent_buffering", "initial_bak_file_size", "credentials", "chunk_size", "global_oio_limit")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    DB_NAME_FIELD_NUMBER: _ClassVar[int]
    BACKUP_TYPE_FIELD_NUMBER: _ClassVar[int]
    BRIDGE_NODE_VIP_VEC_FIELD_NUMBER: _ClassVar[int]
    FILE_NAME_VEC_FIELD_NUMBER: _ClassVar[int]
    VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    TAIL_LOG_FIELD_NUMBER: _ClassVar[int]
    COPY_ONLY_FIELD_NUMBER: _ClassVar[int]
    USE_SMB_FIELD_NUMBER: _ClassVar[int]
    WITH_CLAUSE_FIELD_NUMBER: _ClassVar[int]
    ENABLE_CHECKSUM_FIELD_NUMBER: _ClassVar[int]
    CONTINUE_AFTER_ERROR_FIELD_NUMBER: _ClassVar[int]
    BRIDGE_NODE_VIP_FQDN_FIELD_NUMBER: _ClassVar[int]
    SQL_VDI_COMMAND_TIMEOUT_SECS_FIELD_NUMBER: _ClassVar[int]
    SQL_VDI_CONFIGURATION_WAIT_TIME_SECS_FIELD_NUMBER: _ClassVar[int]
    BIFROST_SERVER_CONFIG_PROTO_FIELD_NUMBER: _ClassVar[int]
    STATS_CONTAINER_ID_FIELD_NUMBER: _ClassVar[int]
    OIO_BYTES_PER_STREAM_LIMIT_FIELD_NUMBER: _ClassVar[int]
    OIO_COUNT_PER_STREAM_LIMIT_FIELD_NUMBER: _ClassVar[int]
    DISABLE_AGENT_BUFFERING_FIELD_NUMBER: _ClassVar[int]
    INITIAL_BAK_FILE_SIZE_FIELD_NUMBER: _ClassVar[int]
    CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    CHUNK_SIZE_FIELD_NUMBER: _ClassVar[int]
    GLOBAL_OIO_LIMIT_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    db_name: _sql_pb2_1_1.DBNameProto
    backup_type: _sql_pb2_1_1.SQLNativeOperationType
    bridge_node_vip_vec: _containers.RepeatedScalarFieldContainer[str]
    file_name_vec: _containers.RepeatedScalarFieldContainer[str]
    view_name: str
    tail_log: bool
    copy_only: bool
    use_smb: bool
    with_clause: str
    enable_checksum: bool
    continue_after_error: bool
    bridge_node_vip_fqdn: str
    sql_vdi_command_timeout_secs: int
    sql_vdi_configuration_wait_time_secs: int
    bifrost_server_config_proto: _server_config_pb2.ServerConfigProto
    stats_container_id: int
    oio_bytes_per_stream_limit: int
    oio_count_per_stream_limit: int
    disable_agent_buffering: bool
    initial_bak_file_size: int
    credentials: _sql_pb2_1_1.Credentials
    chunk_size: int
    global_oio_limit: int
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., db_name: _Optional[_Union[_sql_pb2_1_1.DBNameProto, _Mapping]] = ..., backup_type: _Optional[_Union[_sql_pb2_1_1.SQLNativeOperationType, str]] = ..., bridge_node_vip_vec: _Optional[_Iterable[str]] = ..., file_name_vec: _Optional[_Iterable[str]] = ..., view_name: _Optional[str] = ..., tail_log: bool = ..., copy_only: bool = ..., use_smb: bool = ..., with_clause: _Optional[str] = ..., enable_checksum: bool = ..., continue_after_error: bool = ..., bridge_node_vip_fqdn: _Optional[str] = ..., sql_vdi_command_timeout_secs: _Optional[int] = ..., sql_vdi_configuration_wait_time_secs: _Optional[int] = ..., bifrost_server_config_proto: _Optional[_Union[_server_config_pb2.ServerConfigProto, _Mapping]] = ..., stats_container_id: _Optional[int] = ..., oio_bytes_per_stream_limit: _Optional[int] = ..., oio_count_per_stream_limit: _Optional[int] = ..., disable_agent_buffering: bool = ..., initial_bak_file_size: _Optional[int] = ..., credentials: _Optional[_Union[_sql_pb2_1_1.Credentials, _Mapping]] = ..., chunk_size: _Optional[int] = ..., global_oio_limit: _Optional[int] = ...) -> None: ...

class StartSQLNativeBackupResult(_message.Message):
    __slots__ = ("error", "uuid")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    uuid: str
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., uuid: _Optional[str] = ...) -> None: ...

class StartSQLNativeRestoreArg(_message.Message):
    __slots__ = ("header", "db_name", "original_db_name", "restore_type", "bridge_node_vip_vec", "file_name_vec", "view_name", "restore_time", "with_recovery", "overwrite_alternate_database_if_it_exists", "original_sql_id", "move_file_params", "keep_cdc", "use_smb", "with_clause", "enable_checksum", "continue_after_error", "file_info_vec", "bridge_node_vip_fqdn", "sql_vdi_command_timeout_secs", "sql_vdi_configuration_wait_time_secs", "overwrite", "bifrost_server_config_proto", "original_instance_info", "credentials", "num_log_replays", "is_last_log")
    class MoveFileParam(_message.Message):
        __slots__ = ("logical_file_name", "new_physical_file_path")
        LOGICAL_FILE_NAME_FIELD_NUMBER: _ClassVar[int]
        NEW_PHYSICAL_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
        logical_file_name: str
        new_physical_file_path: str
        def __init__(self, logical_file_name: _Optional[str] = ..., new_physical_file_path: _Optional[str] = ...) -> None: ...
    HEADER_FIELD_NUMBER: _ClassVar[int]
    DB_NAME_FIELD_NUMBER: _ClassVar[int]
    ORIGINAL_DB_NAME_FIELD_NUMBER: _ClassVar[int]
    RESTORE_TYPE_FIELD_NUMBER: _ClassVar[int]
    BRIDGE_NODE_VIP_VEC_FIELD_NUMBER: _ClassVar[int]
    FILE_NAME_VEC_FIELD_NUMBER: _ClassVar[int]
    VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    RESTORE_TIME_FIELD_NUMBER: _ClassVar[int]
    WITH_RECOVERY_FIELD_NUMBER: _ClassVar[int]
    OVERWRITE_ALTERNATE_DATABASE_IF_IT_EXISTS_FIELD_NUMBER: _ClassVar[int]
    ORIGINAL_SQL_ID_FIELD_NUMBER: _ClassVar[int]
    MOVE_FILE_PARAMS_FIELD_NUMBER: _ClassVar[int]
    KEEP_CDC_FIELD_NUMBER: _ClassVar[int]
    USE_SMB_FIELD_NUMBER: _ClassVar[int]
    WITH_CLAUSE_FIELD_NUMBER: _ClassVar[int]
    ENABLE_CHECKSUM_FIELD_NUMBER: _ClassVar[int]
    CONTINUE_AFTER_ERROR_FIELD_NUMBER: _ClassVar[int]
    FILE_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    BRIDGE_NODE_VIP_FQDN_FIELD_NUMBER: _ClassVar[int]
    SQL_VDI_COMMAND_TIMEOUT_SECS_FIELD_NUMBER: _ClassVar[int]
    SQL_VDI_CONFIGURATION_WAIT_TIME_SECS_FIELD_NUMBER: _ClassVar[int]
    OVERWRITE_FIELD_NUMBER: _ClassVar[int]
    BIFROST_SERVER_CONFIG_PROTO_FIELD_NUMBER: _ClassVar[int]
    ORIGINAL_INSTANCE_INFO_FIELD_NUMBER: _ClassVar[int]
    CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    NUM_LOG_REPLAYS_FIELD_NUMBER: _ClassVar[int]
    IS_LAST_LOG_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    db_name: _sql_pb2_1_1.DBNameProto
    original_db_name: _sql_pb2_1_1.DBNameProto
    restore_type: _sql_pb2_1_1.SQLNativeOperationType
    bridge_node_vip_vec: _containers.RepeatedScalarFieldContainer[str]
    file_name_vec: _containers.RepeatedScalarFieldContainer[str]
    view_name: str
    restore_time: _sql_pb2_1_1.LocalTime
    with_recovery: bool
    overwrite_alternate_database_if_it_exists: bool
    original_sql_id: _sql_pb2_1.SqlId
    move_file_params: _containers.RepeatedCompositeFieldContainer[StartSQLNativeRestoreArg.MoveFileParam]
    keep_cdc: bool
    use_smb: bool
    with_clause: str
    enable_checksum: bool
    continue_after_error: bool
    file_info_vec: _containers.RepeatedCompositeFieldContainer[_sql_pb2_1.FileInfo]
    bridge_node_vip_fqdn: str
    sql_vdi_command_timeout_secs: int
    sql_vdi_configuration_wait_time_secs: int
    overwrite: bool
    bifrost_server_config_proto: _server_config_pb2.ServerConfigProto
    original_instance_info: _sql_pb2_1.SQLInstanceInfo
    credentials: _sql_pb2_1_1.Credentials
    num_log_replays: int
    is_last_log: bool
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., db_name: _Optional[_Union[_sql_pb2_1_1.DBNameProto, _Mapping]] = ..., original_db_name: _Optional[_Union[_sql_pb2_1_1.DBNameProto, _Mapping]] = ..., restore_type: _Optional[_Union[_sql_pb2_1_1.SQLNativeOperationType, str]] = ..., bridge_node_vip_vec: _Optional[_Iterable[str]] = ..., file_name_vec: _Optional[_Iterable[str]] = ..., view_name: _Optional[str] = ..., restore_time: _Optional[_Union[_sql_pb2_1_1.LocalTime, _Mapping]] = ..., with_recovery: bool = ..., overwrite_alternate_database_if_it_exists: bool = ..., original_sql_id: _Optional[_Union[_sql_pb2_1.SqlId, _Mapping]] = ..., move_file_params: _Optional[_Iterable[_Union[StartSQLNativeRestoreArg.MoveFileParam, _Mapping]]] = ..., keep_cdc: bool = ..., use_smb: bool = ..., with_clause: _Optional[str] = ..., enable_checksum: bool = ..., continue_after_error: bool = ..., file_info_vec: _Optional[_Iterable[_Union[_sql_pb2_1.FileInfo, _Mapping]]] = ..., bridge_node_vip_fqdn: _Optional[str] = ..., sql_vdi_command_timeout_secs: _Optional[int] = ..., sql_vdi_configuration_wait_time_secs: _Optional[int] = ..., overwrite: bool = ..., bifrost_server_config_proto: _Optional[_Union[_server_config_pb2.ServerConfigProto, _Mapping]] = ..., original_instance_info: _Optional[_Union[_sql_pb2_1.SQLInstanceInfo, _Mapping]] = ..., credentials: _Optional[_Union[_sql_pb2_1_1.Credentials, _Mapping]] = ..., num_log_replays: _Optional[int] = ..., is_last_log: bool = ...) -> None: ...

class StartSQLNativeRestoreResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class AbortSQLNativeOperationArg(_message.Message):
    __slots__ = ("header", "db_name", "credentials", "op_type")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    DB_NAME_FIELD_NUMBER: _ClassVar[int]
    CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    OP_TYPE_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    db_name: _sql_pb2_1_1.DBNameProto
    credentials: _sql_pb2_1_1.Credentials
    op_type: _sql_pb2_1_1.SQLNativeOperationType
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., db_name: _Optional[_Union[_sql_pb2_1_1.DBNameProto, _Mapping]] = ..., credentials: _Optional[_Union[_sql_pb2_1_1.Credentials, _Mapping]] = ..., op_type: _Optional[_Union[_sql_pb2_1_1.SQLNativeOperationType, str]] = ...) -> None: ...

class AbortSQLNativeOperationResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class GetSQLNativeBackupProgressArg(_message.Message):
    __slots__ = ("header", "db_name", "uuid", "credentials", "op_type")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    DB_NAME_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    OP_TYPE_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    db_name: _sql_pb2_1_1.DBNameProto
    uuid: str
    credentials: _sql_pb2_1_1.Credentials
    op_type: _sql_pb2_1_1.SQLNativeOperationType
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., db_name: _Optional[_Union[_sql_pb2_1_1.DBNameProto, _Mapping]] = ..., uuid: _Optional[str] = ..., credentials: _Optional[_Union[_sql_pb2_1_1.Credentials, _Mapping]] = ..., op_type: _Optional[_Union[_sql_pb2_1_1.SQLNativeOperationType, str]] = ...) -> None: ...

class GetSQLNativeBackupProgressResult(_message.Message):
    __slots__ = ("error", "backup_error", "backup_completed", "percentage_backup_completion", "backupset_row_info")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    BACKUP_ERROR_FIELD_NUMBER: _ClassVar[int]
    BACKUP_COMPLETED_FIELD_NUMBER: _ClassVar[int]
    PERCENTAGE_BACKUP_COMPLETION_FIELD_NUMBER: _ClassVar[int]
    BACKUPSET_ROW_INFO_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    backup_error: _error_pb2.ErrorProto
    backup_completed: bool
    percentage_backup_completion: int
    backupset_row_info: _sql_pb2_1_1.BackupSetRowInfo
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., backup_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., backup_completed: bool = ..., percentage_backup_completion: _Optional[int] = ..., backupset_row_info: _Optional[_Union[_sql_pb2_1_1.BackupSetRowInfo, _Mapping]] = ...) -> None: ...

class GetSQLNativeRestoreProgressArg(_message.Message):
    __slots__ = ("header", "db_name", "credentials", "op_type")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    DB_NAME_FIELD_NUMBER: _ClassVar[int]
    CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    OP_TYPE_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    db_name: _sql_pb2_1_1.DBNameProto
    credentials: _sql_pb2_1_1.Credentials
    op_type: _sql_pb2_1_1.SQLNativeOperationType
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., db_name: _Optional[_Union[_sql_pb2_1_1.DBNameProto, _Mapping]] = ..., credentials: _Optional[_Union[_sql_pb2_1_1.Credentials, _Mapping]] = ..., op_type: _Optional[_Union[_sql_pb2_1_1.SQLNativeOperationType, str]] = ...) -> None: ...

class GetSQLNativeRestoreProgressResult(_message.Message):
    __slots__ = ("error", "restore_error", "restore_completed", "percentage_restore_completion", "new_sql_id")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    RESTORE_ERROR_FIELD_NUMBER: _ClassVar[int]
    RESTORE_COMPLETED_FIELD_NUMBER: _ClassVar[int]
    PERCENTAGE_RESTORE_COMPLETION_FIELD_NUMBER: _ClassVar[int]
    NEW_SQL_ID_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    restore_error: _error_pb2.ErrorProto
    restore_completed: bool
    percentage_restore_completion: int
    new_sql_id: _sql_pb2_1.SqlId
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., restore_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., restore_completed: bool = ..., percentage_restore_completion: _Optional[int] = ..., new_sql_id: _Optional[_Union[_sql_pb2_1.SqlId, _Mapping]] = ...) -> None: ...

class CancelSQLNativeOperationArg(_message.Message):
    __slots__ = ("header", "db_name", "credentials", "op_type")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    DB_NAME_FIELD_NUMBER: _ClassVar[int]
    CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    OP_TYPE_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    db_name: _sql_pb2_1_1.DBNameProto
    credentials: _sql_pb2_1_1.Credentials
    op_type: _sql_pb2_1_1.SQLNativeOperationType
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., db_name: _Optional[_Union[_sql_pb2_1_1.DBNameProto, _Mapping]] = ..., credentials: _Optional[_Union[_sql_pb2_1_1.Credentials, _Mapping]] = ..., op_type: _Optional[_Union[_sql_pb2_1_1.SQLNativeOperationType, str]] = ...) -> None: ...

class CancelSQLNativeOperationResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class NotifySQLNativeOperationCompleteArg(_message.Message):
    __slots__ = ("header", "db_name", "credentials", "op_type")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    DB_NAME_FIELD_NUMBER: _ClassVar[int]
    CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    OP_TYPE_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    db_name: _sql_pb2_1_1.DBNameProto
    credentials: _sql_pb2_1_1.Credentials
    op_type: _sql_pb2_1_1.SQLNativeOperationType
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., db_name: _Optional[_Union[_sql_pb2_1_1.DBNameProto, _Mapping]] = ..., credentials: _Optional[_Union[_sql_pb2_1_1.Credentials, _Mapping]] = ..., op_type: _Optional[_Union[_sql_pb2_1_1.SQLNativeOperationType, str]] = ...) -> None: ...

class NotifySQLNativeOperationCompleteResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class VSSRestoreSQLSnapshotArg(_message.Message):
    __slots__ = ("restore_policy",)
    VSS_RESTORE_SQL_SNAPSHOT_ARG_FIELD_NUMBER: _ClassVar[int]
    vss_restore_sql_snapshot_arg: _descriptor.FieldDescriptor
    RESTORE_POLICY_FIELD_NUMBER: _ClassVar[int]
    restore_policy: _sql_pb2.RestorePolicy
    def __init__(self, restore_policy: _Optional[_Union[_sql_pb2.RestorePolicy, _Mapping]] = ...) -> None: ...

class VSSRestoreSQLSnapshotResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class SQLRestoreFromSnapshotResult(_message.Message):
    __slots__ = ("cohesity_mount_to_local_file_path_map", "progress", "snapfs_path_to_target_file_dir_map")
    class CohesityMountToLocalFilePathMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class SnapfsPathToTargetFileDirMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    SQL_RESTORE_FROM_SNAPSHOT_RESULT_FIELD_NUMBER: _ClassVar[int]
    sql_restore_from_snapshot_result: _descriptor.FieldDescriptor
    COHESITY_MOUNT_TO_LOCAL_FILE_PATH_MAP_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_FIELD_NUMBER: _ClassVar[int]
    SNAPFS_PATH_TO_TARGET_FILE_DIR_MAP_FIELD_NUMBER: _ClassVar[int]
    cohesity_mount_to_local_file_path_map: _containers.ScalarMap[str, str]
    progress: _sql_pb2.SQLVSSRestoreProgress
    snapfs_path_to_target_file_dir_map: _containers.ScalarMap[str, str]
    def __init__(self, cohesity_mount_to_local_file_path_map: _Optional[_Mapping[str, str]] = ..., progress: _Optional[_Union[_sql_pb2.SQLVSSRestoreProgress, _Mapping]] = ..., snapfs_path_to_target_file_dir_map: _Optional[_Mapping[str, str]] = ...) -> None: ...

class VSSGetSQLRestoreProgressArg(_message.Message):
    __slots__ = ("header", "snapshot_set_id")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_SET_ID_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    snapshot_set_id: bytes
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., snapshot_set_id: _Optional[bytes] = ...) -> None: ...

class VSSGetSQLRestoreProgressResult(_message.Message):
    __slots__ = ("error", "progress", "user_messages")
    VSS_GET_SQL_RESTORE_PROGRESS_RESULT_FIELD_NUMBER: _ClassVar[int]
    vss_get_sql_restore_progress_result: _descriptor.FieldDescriptor
    ERROR_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_FIELD_NUMBER: _ClassVar[int]
    USER_MESSAGES_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    progress: _sql_pb2.SQLVSSRestoreProgress
    user_messages: _magneto_pb2.UserMessageProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., progress: _Optional[_Union[_sql_pb2.SQLVSSRestoreProgress, _Mapping]] = ..., user_messages: _Optional[_Union[_magneto_pb2.UserMessageProto, _Mapping]] = ...) -> None: ...

class QuerySQLBackupsetTableArg(_message.Message):
    __slots__ = ("header", "database_id_vec", "max_num_rows", "cluster_resource_ip_address", "include_only_standalone_instances", "enable_aag", "backup_type", "differential_base_only", "get_only_backupset_row_info", "discover_database_file_location", "skip_vss_check", "auth_type", "credentials")
    class BackupType(_message.Message):
        __slots__ = ()
        class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kAll: _ClassVar[QuerySQLBackupsetTableArg.BackupType.Type]
            kFull: _ClassVar[QuerySQLBackupsetTableArg.BackupType.Type]
            kLog: _ClassVar[QuerySQLBackupsetTableArg.BackupType.Type]
        kAll: QuerySQLBackupsetTableArg.BackupType.Type
        kFull: QuerySQLBackupsetTableArg.BackupType.Type
        kLog: QuerySQLBackupsetTableArg.BackupType.Type
        def __init__(self) -> None: ...
    HEADER_FIELD_NUMBER: _ClassVar[int]
    DATABASE_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    MAX_NUM_ROWS_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_RESOURCE_IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_ONLY_STANDALONE_INSTANCES_FIELD_NUMBER: _ClassVar[int]
    ENABLE_AAG_FIELD_NUMBER: _ClassVar[int]
    BACKUP_TYPE_FIELD_NUMBER: _ClassVar[int]
    DIFFERENTIAL_BASE_ONLY_FIELD_NUMBER: _ClassVar[int]
    GET_ONLY_BACKUPSET_ROW_INFO_FIELD_NUMBER: _ClassVar[int]
    DISCOVER_DATABASE_FILE_LOCATION_FIELD_NUMBER: _ClassVar[int]
    SKIP_VSS_CHECK_FIELD_NUMBER: _ClassVar[int]
    AUTH_TYPE_FIELD_NUMBER: _ClassVar[int]
    CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    database_id_vec: _containers.RepeatedCompositeFieldContainer[_sql_pb2_1.SqlId]
    max_num_rows: int
    cluster_resource_ip_address: str
    include_only_standalone_instances: bool
    enable_aag: bool
    backup_type: QuerySQLBackupsetTableArg.BackupType.Type
    differential_base_only: bool
    get_only_backupset_row_info: bool
    discover_database_file_location: bool
    skip_vss_check: bool
    auth_type: _sql_pb2.AuthType.Type
    credentials: _sql_pb2_1_1.Credentials
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., database_id_vec: _Optional[_Iterable[_Union[_sql_pb2_1.SqlId, _Mapping]]] = ..., max_num_rows: _Optional[int] = ..., cluster_resource_ip_address: _Optional[str] = ..., include_only_standalone_instances: bool = ..., enable_aag: bool = ..., backup_type: _Optional[_Union[QuerySQLBackupsetTableArg.BackupType.Type, str]] = ..., differential_base_only: bool = ..., get_only_backupset_row_info: bool = ..., discover_database_file_location: bool = ..., skip_vss_check: bool = ..., auth_type: _Optional[_Union[_sql_pb2.AuthType.Type, str]] = ..., credentials: _Optional[_Union[_sql_pb2_1_1.Credentials, _Mapping]] = ...) -> None: ...

class QuerySQLBackupsetTableResult(_message.Message):
    __slots__ = ("error", "database_info_vec", "aag_info_result_vec", "user_info", "user_warning", "sql_instance_vec", "is_utf16")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    DATABASE_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    AAG_INFO_RESULT_VEC_FIELD_NUMBER: _ClassVar[int]
    USER_INFO_FIELD_NUMBER: _ClassVar[int]
    USER_WARNING_FIELD_NUMBER: _ClassVar[int]
    SQL_INSTANCE_VEC_FIELD_NUMBER: _ClassVar[int]
    IS_UTF16_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    database_info_vec: _containers.RepeatedCompositeFieldContainer[_sql_pb2.SQLDatabaseInfo]
    aag_info_result_vec: _containers.RepeatedCompositeFieldContainer[_sql_pb2.AAGInfoResult]
    user_info: str
    user_warning: str
    sql_instance_vec: _containers.RepeatedCompositeFieldContainer[_sql_pb2_1.SQLInstanceInfo]
    is_utf16: bool
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., database_info_vec: _Optional[_Iterable[_Union[_sql_pb2.SQLDatabaseInfo, _Mapping]]] = ..., aag_info_result_vec: _Optional[_Iterable[_Union[_sql_pb2.AAGInfoResult, _Mapping]]] = ..., user_info: _Optional[str] = ..., user_warning: _Optional[str] = ..., sql_instance_vec: _Optional[_Iterable[_Union[_sql_pb2_1.SQLInstanceInfo, _Mapping]]] = ..., is_utf16: bool = ...) -> None: ...

class GetSQLDatabaseFileInfoArg(_message.Message):
    __slots__ = ("header", "db_name_vec")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    DB_NAME_VEC_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    db_name_vec: _containers.RepeatedCompositeFieldContainer[_sql_pb2_1_1.DBNameProto]
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., db_name_vec: _Optional[_Iterable[_Union[_sql_pb2_1_1.DBNameProto, _Mapping]]] = ...) -> None: ...

class GetSQLDatabaseFileInfoResult(_message.Message):
    __slots__ = ("error", "database_to_file_info_vec")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    DATABASE_TO_FILE_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    database_to_file_info_vec: _containers.RepeatedCompositeFieldContainer[_sql_pb2_1_1.DatabaseToFileInfo]
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., database_to_file_info_vec: _Optional[_Iterable[_Union[_sql_pb2_1_1.DatabaseToFileInfo, _Mapping]]] = ...) -> None: ...

class InitSQLLogReplayArg(_message.Message):
    __slots__ = ("header", "sql_id", "stream", "restore_time", "with_recovery", "keep_cdc", "enable_checksum", "continue_after_error", "is_last_log")
    class Stream(_message.Message):
        __slots__ = ("id", "buffer_size_bytes")
        ID_FIELD_NUMBER: _ClassVar[int]
        BUFFER_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
        id: int
        buffer_size_bytes: int
        def __init__(self, id: _Optional[int] = ..., buffer_size_bytes: _Optional[int] = ...) -> None: ...
    HEADER_FIELD_NUMBER: _ClassVar[int]
    SQL_ID_FIELD_NUMBER: _ClassVar[int]
    STREAM_FIELD_NUMBER: _ClassVar[int]
    RESTORE_TIME_FIELD_NUMBER: _ClassVar[int]
    WITH_RECOVERY_FIELD_NUMBER: _ClassVar[int]
    KEEP_CDC_FIELD_NUMBER: _ClassVar[int]
    ENABLE_CHECKSUM_FIELD_NUMBER: _ClassVar[int]
    CONTINUE_AFTER_ERROR_FIELD_NUMBER: _ClassVar[int]
    IS_LAST_LOG_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    sql_id: _sql_pb2_1.SqlId
    stream: InitSQLLogReplayArg.Stream
    restore_time: _sql_pb2_1_1.LocalTime
    with_recovery: bool
    keep_cdc: bool
    enable_checksum: bool
    continue_after_error: bool
    is_last_log: bool
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., sql_id: _Optional[_Union[_sql_pb2_1.SqlId, _Mapping]] = ..., stream: _Optional[_Union[InitSQLLogReplayArg.Stream, _Mapping]] = ..., restore_time: _Optional[_Union[_sql_pb2_1_1.LocalTime, _Mapping]] = ..., with_recovery: bool = ..., keep_cdc: bool = ..., enable_checksum: bool = ..., continue_after_error: bool = ..., is_last_log: bool = ...) -> None: ...

class InitSQLLogReplayResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class HyperVGuestEndpointArg(_message.Message):
    __slots__ = ("hyperv_guest_access_params",)
    BRING_DISKS_ONLINE_ENDPOINT_ARG_FIELD_NUMBER: _ClassVar[int]
    bring_disks_online_endpoint_arg: _descriptor.FieldDescriptor
    RESTORE_FROM_SNAPSHOT_ARG_FIELD_NUMBER: _ClassVar[int]
    restore_from_snapshot_arg: _descriptor.FieldDescriptor
    GET_RESTORE_FROM_SNAPSHOT_PROGRESS_ARG_FIELD_NUMBER: _ClassVar[int]
    get_restore_from_snapshot_progress_arg: _descriptor.FieldDescriptor
    HYPERV_GUEST_ACCESS_PARAMS_FIELD_NUMBER: _ClassVar[int]
    hyperv_guest_access_params: _hyperv_param_pb2.HyperVGuestAccessParams
    def __init__(self, hyperv_guest_access_params: _Optional[_Union[_hyperv_param_pb2.HyperVGuestAccessParams, _Mapping]] = ...) -> None: ...

class HyperVGuestEndpointResult(_message.Message):
    __slots__ = ("hyperv_access_state",)
    RESTORE_FROM_SNAPSHOT_RESULT_FIELD_NUMBER: _ClassVar[int]
    restore_from_snapshot_result: _descriptor.FieldDescriptor
    HYPERV_ACCESS_STATE_FIELD_NUMBER: _ClassVar[int]
    hyperv_access_state: _hyperv_param_pb2.HyperVAccessState
    def __init__(self, hyperv_access_state: _Optional[_Union[_hyperv_param_pb2.HyperVAccessState, _Mapping]] = ...) -> None: ...

class BringHyperVDisksOnlineArg(_message.Message):
    __slots__ = ("virtual_disk_vec",)
    BRING_HYPERV_DISKS_ONLINE_ARG_FIELD_NUMBER: _ClassVar[int]
    bring_hyperv_disks_online_arg: _descriptor.FieldDescriptor
    VIRTUAL_DISK_VEC_FIELD_NUMBER: _ClassVar[int]
    virtual_disk_vec: _containers.RepeatedCompositeFieldContainer[_hyperv_pb2.VirtualDisk]
    def __init__(self, virtual_disk_vec: _Optional[_Iterable[_Union[_hyperv_pb2.VirtualDisk, _Mapping]]] = ...) -> None: ...

class PrepareVSSSnapshotArg(_message.Message):
    __slots__ = ("involve_vss_writers", "excluded_vss_writers", "included_vss_writers", "suppress_included_writer_warnings", "copy_only", "sql_params", "enable_incremental_backup_after_restart", "excluded_unc_substr_deprecated", "hyperv_params", "cluster_resource_ip_address", "preferred_vss_provider", "snapshot_type", "vss_writer_options", "ad_params", "vss_backup_type", "exchange_params")
    class SnapshotType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kVolume: _ClassVar[PrepareVSSSnapshotArg.SnapshotType]
        kFile: _ClassVar[PrepareVSSSnapshotArg.SnapshotType]
        kVolumeNullCBT: _ClassVar[PrepareVSSSnapshotArg.SnapshotType]
    kVolume: PrepareVSSSnapshotArg.SnapshotType
    kFile: PrepareVSSSnapshotArg.SnapshotType
    kVolumeNullCBT: PrepareVSSSnapshotArg.SnapshotType
    class HyperVParams(_message.Message):
        __slots__ = ("vm_id_vec", "allow_downgrade_to_crash_consistent_backup", "skip_shared_vhds", "quiesce")
        VM_ID_VEC_FIELD_NUMBER: _ClassVar[int]
        ALLOW_DOWNGRADE_TO_CRASH_CONSISTENT_BACKUP_FIELD_NUMBER: _ClassVar[int]
        SKIP_SHARED_VHDS_FIELD_NUMBER: _ClassVar[int]
        QUIESCE_FIELD_NUMBER: _ClassVar[int]
        vm_id_vec: _containers.RepeatedScalarFieldContainer[str]
        allow_downgrade_to_crash_consistent_backup: bool
        skip_shared_vhds: bool
        quiesce: bool
        def __init__(self, vm_id_vec: _Optional[_Iterable[str]] = ..., allow_downgrade_to_crash_consistent_backup: bool = ..., skip_shared_vhds: bool = ..., quiesce: bool = ...) -> None: ...
    class VSSWriterAdditionalOption(_message.Message):
        __slots__ = ("vss_writer_name", "backup_select_component_explicit")
        VSS_WRITER_NAME_FIELD_NUMBER: _ClassVar[int]
        BACKUP_SELECT_COMPONENT_EXPLICIT_FIELD_NUMBER: _ClassVar[int]
        vss_writer_name: str
        backup_select_component_explicit: bool
        def __init__(self, vss_writer_name: _Optional[str] = ..., backup_select_component_explicit: bool = ...) -> None: ...
    class ADParams(_message.Message):
        __slots__ = ("populate_ad_topology",)
        POPULATE_AD_TOPOLOGY_FIELD_NUMBER: _ClassVar[int]
        populate_ad_topology: bool
        def __init__(self, populate_ad_topology: bool = ...) -> None: ...
    class ExchangeParams(_message.Message):
        __slots__ = ("db_vec", "skip_filecbt_vss_checkpoint")
        class ExchangeDBParam(_message.Message):
            __slots__ = ("db_guid", "verification_flags", "generate_mailbox_metadata")
            DB_GUID_FIELD_NUMBER: _ClassVar[int]
            VERIFICATION_FLAGS_FIELD_NUMBER: _ClassVar[int]
            GENERATE_MAILBOX_METADATA_FIELD_NUMBER: _ClassVar[int]
            db_guid: str
            verification_flags: int
            generate_mailbox_metadata: bool
            def __init__(self, db_guid: _Optional[str] = ..., verification_flags: _Optional[int] = ..., generate_mailbox_metadata: bool = ...) -> None: ...
        DB_VEC_FIELD_NUMBER: _ClassVar[int]
        SKIP_FILECBT_VSS_CHECKPOINT_FIELD_NUMBER: _ClassVar[int]
        db_vec: _containers.RepeatedCompositeFieldContainer[PrepareVSSSnapshotArg.ExchangeParams.ExchangeDBParam]
        skip_filecbt_vss_checkpoint: bool
        def __init__(self, db_vec: _Optional[_Iterable[_Union[PrepareVSSSnapshotArg.ExchangeParams.ExchangeDBParam, _Mapping]]] = ..., skip_filecbt_vss_checkpoint: bool = ...) -> None: ...
    PREPARE_VSS_SNAPSHOT_ARG_FIELD_NUMBER: _ClassVar[int]
    prepare_vss_snapshot_arg: _descriptor.FieldDescriptor
    INVOLVE_VSS_WRITERS_FIELD_NUMBER: _ClassVar[int]
    EXCLUDED_VSS_WRITERS_FIELD_NUMBER: _ClassVar[int]
    INCLUDED_VSS_WRITERS_FIELD_NUMBER: _ClassVar[int]
    SUPPRESS_INCLUDED_WRITER_WARNINGS_FIELD_NUMBER: _ClassVar[int]
    COPY_ONLY_FIELD_NUMBER: _ClassVar[int]
    SQL_PARAMS_FIELD_NUMBER: _ClassVar[int]
    ENABLE_INCREMENTAL_BACKUP_AFTER_RESTART_FIELD_NUMBER: _ClassVar[int]
    EXCLUDED_UNC_SUBSTR_DEPRECATED_FIELD_NUMBER: _ClassVar[int]
    HYPERV_PARAMS_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_RESOURCE_IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PREFERRED_VSS_PROVIDER_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_TYPE_FIELD_NUMBER: _ClassVar[int]
    VSS_WRITER_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    AD_PARAMS_FIELD_NUMBER: _ClassVar[int]
    VSS_BACKUP_TYPE_FIELD_NUMBER: _ClassVar[int]
    EXCHANGE_PARAMS_FIELD_NUMBER: _ClassVar[int]
    involve_vss_writers: bool
    excluded_vss_writers: _containers.RepeatedScalarFieldContainer[str]
    included_vss_writers: _containers.RepeatedScalarFieldContainer[str]
    suppress_included_writer_warnings: bool
    copy_only: bool
    sql_params: _sql_pb2.SQLParams
    enable_incremental_backup_after_restart: bool
    excluded_unc_substr_deprecated: str
    hyperv_params: PrepareVSSSnapshotArg.HyperVParams
    cluster_resource_ip_address: str
    preferred_vss_provider: _vss_pb2.VSSProviderPropertiesProto.ProviderType
    snapshot_type: PrepareVSSSnapshotArg.SnapshotType
    vss_writer_options: _containers.RepeatedCompositeFieldContainer[PrepareVSSSnapshotArg.VSSWriterAdditionalOption]
    ad_params: PrepareVSSSnapshotArg.ADParams
    vss_backup_type: _vss_pb2.VSSBackupType.Type
    exchange_params: PrepareVSSSnapshotArg.ExchangeParams
    def __init__(self, involve_vss_writers: bool = ..., excluded_vss_writers: _Optional[_Iterable[str]] = ..., included_vss_writers: _Optional[_Iterable[str]] = ..., suppress_included_writer_warnings: bool = ..., copy_only: bool = ..., sql_params: _Optional[_Union[_sql_pb2.SQLParams, _Mapping]] = ..., enable_incremental_backup_after_restart: bool = ..., excluded_unc_substr_deprecated: _Optional[str] = ..., hyperv_params: _Optional[_Union[PrepareVSSSnapshotArg.HyperVParams, _Mapping]] = ..., cluster_resource_ip_address: _Optional[str] = ..., preferred_vss_provider: _Optional[_Union[_vss_pb2.VSSProviderPropertiesProto.ProviderType, str]] = ..., snapshot_type: _Optional[_Union[PrepareVSSSnapshotArg.SnapshotType, str]] = ..., vss_writer_options: _Optional[_Iterable[_Union[PrepareVSSSnapshotArg.VSSWriterAdditionalOption, _Mapping]]] = ..., ad_params: _Optional[_Union[PrepareVSSSnapshotArg.ADParams, _Mapping]] = ..., vss_backup_type: _Optional[_Union[_vss_pb2.VSSBackupType.Type, str]] = ..., exchange_params: _Optional[_Union[PrepareVSSSnapshotArg.ExchangeParams, _Mapping]] = ...) -> None: ...

class PrepareVSSSnapshotResult(_message.Message):
    __slots__ = ("component_info",)
    PREPARE_VSS_SNAPSHOT_RESULT_FIELD_NUMBER: _ClassVar[int]
    prepare_vss_snapshot_result: _descriptor.FieldDescriptor
    COMPONENT_INFO_FIELD_NUMBER: _ClassVar[int]
    component_info: _vss_pb2.VSSWriterComponentInfo
    def __init__(self, component_info: _Optional[_Union[_vss_pb2.VSSWriterComponentInfo, _Mapping]] = ...) -> None: ...

class FinalizeVSSSnapshotMetadataResult(_message.Message):
    __slots__ = ("component_info",)
    FINALIZE_VSS_SNAPSHOT_METADATA_RESULT_FIELD_NUMBER: _ClassVar[int]
    finalize_vss_snapshot_metadata_result: _descriptor.FieldDescriptor
    COMPONENT_INFO_FIELD_NUMBER: _ClassVar[int]
    component_info: _vss_pb2.VSSWriterComponentInfo
    def __init__(self, component_info: _Optional[_Union[_vss_pb2.VSSWriterComponentInfo, _Mapping]] = ...) -> None: ...

class NotifyVSSBackupCompleteResult(_message.Message):
    __slots__ = ("component_info",)
    NOTIFY_VSS_BACKUP_COMPLETE_RESULT_FIELD_NUMBER: _ClassVar[int]
    notify_vss_backup_complete_result: _descriptor.FieldDescriptor
    COMPONENT_INFO_FIELD_NUMBER: _ClassVar[int]
    component_info: _vss_pb2.VSSWriterComponentInfo
    def __init__(self, component_info: _Optional[_Union[_vss_pb2.VSSWriterComponentInfo, _Mapping]] = ...) -> None: ...

class RevertAndAttachSQLArg(_message.Message):
    __slots__ = ("header", "server_snapshot_info", "database_vec", "mount_volume_info_vec", "mounted_volumes_are_crash_consistent", "restore_app_files_arg")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    SERVER_SNAPSHOT_INFO_FIELD_NUMBER: _ClassVar[int]
    DATABASE_VEC_FIELD_NUMBER: _ClassVar[int]
    MOUNT_VOLUME_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    MOUNTED_VOLUMES_ARE_CRASH_CONSISTENT_FIELD_NUMBER: _ClassVar[int]
    RESTORE_APP_FILES_ARG_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    server_snapshot_info: _agent_pb2.ServerSnapshotInfo
    database_vec: _containers.RepeatedCompositeFieldContainer[_sql_pb2.DatabaseRestoreSpec]
    mount_volume_info_vec: _containers.RepeatedCompositeFieldContainer[_agent_pb2.MountVolumeInfo]
    mounted_volumes_are_crash_consistent: bool
    restore_app_files_arg: _agent_param_pb2.RestoreAppFilesArg
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., server_snapshot_info: _Optional[_Union[_agent_pb2.ServerSnapshotInfo, _Mapping]] = ..., database_vec: _Optional[_Iterable[_Union[_sql_pb2.DatabaseRestoreSpec, _Mapping]]] = ..., mount_volume_info_vec: _Optional[_Iterable[_Union[_agent_pb2.MountVolumeInfo, _Mapping]]] = ..., mounted_volumes_are_crash_consistent: bool = ..., restore_app_files_arg: _Optional[_Union[_agent_param_pb2.RestoreAppFilesArg, _Mapping]] = ...) -> None: ...

class RevertAndAttachSQLResult(_message.Message):
    __slots__ = ("error", "sql_id_vec", "volume_guid_to_error_map", "database_error_vec", "attached_db_info_vec")
    class VolumeGuidToErrorMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _error_pb2.ErrorProto
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...
    class DatabaseError(_message.Message):
        __slots__ = ("sql_id", "error")
        SQL_ID_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        sql_id: _sql_pb2_1.SqlId
        error: _error_pb2.ErrorProto
        def __init__(self, sql_id: _Optional[_Union[_sql_pb2_1.SqlId, _Mapping]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...
    ERROR_FIELD_NUMBER: _ClassVar[int]
    SQL_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    VOLUME_GUID_TO_ERROR_MAP_FIELD_NUMBER: _ClassVar[int]
    DATABASE_ERROR_VEC_FIELD_NUMBER: _ClassVar[int]
    ATTACHED_DB_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    sql_id_vec: _containers.RepeatedCompositeFieldContainer[_sql_pb2_1.SqlId]
    volume_guid_to_error_map: _containers.MessageMap[str, _error_pb2.ErrorProto]
    database_error_vec: _containers.RepeatedCompositeFieldContainer[RevertAndAttachSQLResult.DatabaseError]
    attached_db_info_vec: _containers.RepeatedCompositeFieldContainer[_sql_pb2_1_1.AttachedDbInfo]
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., sql_id_vec: _Optional[_Iterable[_Union[_sql_pb2_1.SqlId, _Mapping]]] = ..., volume_guid_to_error_map: _Optional[_Mapping[str, _error_pb2.ErrorProto]] = ..., database_error_vec: _Optional[_Iterable[_Union[RevertAndAttachSQLResult.DatabaseError, _Mapping]]] = ..., attached_db_info_vec: _Optional[_Iterable[_Union[_sql_pb2_1_1.AttachedDbInfo, _Mapping]]] = ...) -> None: ...

class DetachSQLDatabasesArg(_message.Message):
    __slots__ = ("header", "sql_id_vec", "db_name_vec", "smb_path_vec", "kill_connections")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    SQL_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    DB_NAME_VEC_FIELD_NUMBER: _ClassVar[int]
    SMB_PATH_VEC_FIELD_NUMBER: _ClassVar[int]
    KILL_CONNECTIONS_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    sql_id_vec: _containers.RepeatedCompositeFieldContainer[_sql_pb2_1.SqlId]
    db_name_vec: _containers.RepeatedCompositeFieldContainer[_sql_pb2_1_1.DBNameProto]
    smb_path_vec: _containers.RepeatedScalarFieldContainer[str]
    kill_connections: bool
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., sql_id_vec: _Optional[_Iterable[_Union[_sql_pb2_1.SqlId, _Mapping]]] = ..., db_name_vec: _Optional[_Iterable[_Union[_sql_pb2_1_1.DBNameProto, _Mapping]]] = ..., smb_path_vec: _Optional[_Iterable[str]] = ..., kill_connections: bool = ...) -> None: ...

class DetachSQLDatabasesResult(_message.Message):
    __slots__ = ("error", "database_error_vec")
    class DatabaseError(_message.Message):
        __slots__ = ("sql_id", "error")
        SQL_ID_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        sql_id: _sql_pb2_1.SqlId
        error: _error_pb2.ErrorProto
        def __init__(self, sql_id: _Optional[_Union[_sql_pb2_1.SqlId, _Mapping]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...
    ERROR_FIELD_NUMBER: _ClassVar[int]
    DATABASE_ERROR_VEC_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    database_error_vec: _containers.RepeatedCompositeFieldContainer[DetachSQLDatabasesResult.DatabaseError]
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., database_error_vec: _Optional[_Iterable[_Union[DetachSQLDatabasesResult.DatabaseError, _Mapping]]] = ...) -> None: ...

class MountNASOnWindowsArg(_message.Message):
    __slots__ = ("use_default_credentials",)
    WINDOWS_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    windows_settings: _descriptor.FieldDescriptor
    USE_DEFAULT_CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    use_default_credentials: bool
    def __init__(self, use_default_credentials: bool = ...) -> None: ...

class MountVirtualVolumeOnWindowsArg(_message.Message):
    __slots__ = ("try_to_assign_drive_letter", "try_to_change_volume_serial_number")
    WINDOWS_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    windows_settings: _descriptor.FieldDescriptor
    TRY_TO_ASSIGN_DRIVE_LETTER_FIELD_NUMBER: _ClassVar[int]
    TRY_TO_CHANGE_VOLUME_SERIAL_NUMBER_FIELD_NUMBER: _ClassVar[int]
    try_to_assign_drive_letter: bool
    try_to_change_volume_serial_number: bool
    def __init__(self, try_to_assign_drive_letter: bool = ..., try_to_change_volume_serial_number: bool = ...) -> None: ...

class FetchVolumeInfoVssArg(_message.Message):
    __slots__ = ("excluded_unc_substr_deprecated",)
    FETCH_VOLUME_INFO_ARG_FIELD_NUMBER: _ClassVar[int]
    fetch_volume_info_arg: _descriptor.FieldDescriptor
    EXCLUDED_UNC_SUBSTR_DEPRECATED_FIELD_NUMBER: _ClassVar[int]
    excluded_unc_substr_deprecated: str
    def __init__(self, excluded_unc_substr_deprecated: _Optional[str] = ...) -> None: ...

class UpdateJobInfoArg(_message.Message):
    __slots__ = ("header", "clusterid_jobid", "gcstate")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    CLUSTERID_JOBID_FIELD_NUMBER: _ClassVar[int]
    GCSTATE_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    clusterid_jobid: str
    gcstate: _agent_param_pb2.GCType.gcAction
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., clusterid_jobid: _Optional[str] = ..., gcstate: _Optional[_Union[_agent_param_pb2.GCType.gcAction, str]] = ...) -> None: ...

class UpdateJobInfoResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class GetWindowsHostInfoArg(_message.Message):
    __slots__ = ("include_cbt_info",)
    GET_HOST_INFO_ARG_FIELD_NUMBER: _ClassVar[int]
    get_host_info_arg: _descriptor.FieldDescriptor
    INCLUDE_CBT_INFO_FIELD_NUMBER: _ClassVar[int]
    include_cbt_info: bool
    def __init__(self, include_cbt_info: bool = ...) -> None: ...

class GetWindowsHostInfoResult(_message.Message):
    __slots__ = ("vol_cbt_info", "file_cbt_info")
    GET_HOST_INFO_RESULT_FIELD_NUMBER: _ClassVar[int]
    get_host_info_result: _descriptor.FieldDescriptor
    VOL_CBT_INFO_FIELD_NUMBER: _ClassVar[int]
    FILE_CBT_INFO_FIELD_NUMBER: _ClassVar[int]
    vol_cbt_info: _agent_pb2.CbtInfo
    file_cbt_info: _agent_pb2.CbtInfo
    def __init__(self, vol_cbt_info: _Optional[_Union[_agent_pb2.CbtInfo, _Mapping]] = ..., file_cbt_info: _Optional[_Union[_agent_pb2.CbtInfo, _Mapping]] = ...) -> None: ...

class VMwareUnmountVirtualVolumeArg(_message.Message):
    __slots__ = ("disk_unique_id_vec", "mount_point_vec")
    VMWARE_UNMOUNT_VIRTUAL_VOLUME_ARG_FIELD_NUMBER: _ClassVar[int]
    vmware_unmount_virtual_volume_arg: _descriptor.FieldDescriptor
    DISK_UNIQUE_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    MOUNT_POINT_VEC_FIELD_NUMBER: _ClassVar[int]
    disk_unique_id_vec: _containers.RepeatedScalarFieldContainer[str]
    mount_point_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, disk_unique_id_vec: _Optional[_Iterable[str]] = ..., mount_point_vec: _Optional[_Iterable[str]] = ...) -> None: ...

class BringVMwareDisksOnlineArg(_message.Message):
    __slots__ = ("additional_ldm_vol_restore_processing",)
    BRING_VMWARE_DISKS_ONLINE_ARG_FIELD_NUMBER: _ClassVar[int]
    bring_vmware_disks_online_arg: _descriptor.FieldDescriptor
    ADDITIONAL_LDM_VOL_RESTORE_PROCESSING_FIELD_NUMBER: _ClassVar[int]
    additional_ldm_vol_restore_processing: bool
    def __init__(self, additional_ldm_vol_restore_processing: bool = ...) -> None: ...

class CbtDriverInfo(_message.Message):
    __slots__ = ("vol_cbt_info", "file_cbt_info")
    CBT_DRIVER_INFO_FIELD_NUMBER: _ClassVar[int]
    cbt_driver_info: _descriptor.FieldDescriptor
    VOL_CBT_INFO_FIELD_NUMBER: _ClassVar[int]
    FILE_CBT_INFO_FIELD_NUMBER: _ClassVar[int]
    vol_cbt_info: _agent_pb2.CbtInfo
    file_cbt_info: _agent_pb2.CbtInfo
    def __init__(self, vol_cbt_info: _Optional[_Union[_agent_pb2.CbtInfo, _Mapping]] = ..., file_cbt_info: _Optional[_Union[_agent_pb2.CbtInfo, _Mapping]] = ...) -> None: ...
