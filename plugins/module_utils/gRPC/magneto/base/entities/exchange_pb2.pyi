from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LocalTime(_message.Message):
    __slots__ = ("msecs", "offset_minutes")
    MSECS_FIELD_NUMBER: _ClassVar[int]
    OFFSET_MINUTES_FIELD_NUMBER: _ClassVar[int]
    msecs: int
    offset_minutes: int
    def __init__(self, msecs: _Optional[int] = ..., offset_minutes: _Optional[int] = ...) -> None: ...

class ExchangeServerVersion(_message.Message):
    __slots__ = ("major_ver", "minor_ver", "build_ver", "revision_num", "display_version")
    MAJOR_VER_FIELD_NUMBER: _ClassVar[int]
    MINOR_VER_FIELD_NUMBER: _ClassVar[int]
    BUILD_VER_FIELD_NUMBER: _ClassVar[int]
    REVISION_NUM_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_VERSION_FIELD_NUMBER: _ClassVar[int]
    major_ver: int
    minor_ver: int
    build_ver: int
    revision_num: int
    display_version: str
    def __init__(self, major_ver: _Optional[int] = ..., minor_ver: _Optional[int] = ..., build_ver: _Optional[int] = ..., revision_num: _Optional[int] = ..., display_version: _Optional[str] = ...) -> None: ...

class ExchangeServerIdentity(_message.Message):
    __slots__ = ("guid", "name", "fqdn")
    GUID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    FQDN_FIELD_NUMBER: _ClassVar[int]
    guid: str
    name: str
    fqdn: str
    def __init__(self, guid: _Optional[str] = ..., name: _Optional[str] = ..., fqdn: _Optional[str] = ...) -> None: ...

class ExchangeDAGIdentity(_message.Message):
    __slots__ = ("guid", "name")
    GUID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    guid: str
    name: str
    def __init__(self, guid: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class ExchangeServerInfo(_message.Message):
    __slots__ = ("id", "role", "version", "default_data_dir_path", "backup_supported", "backup_unsupported_reason_vec", "utc_offsetmin", "vss_backup_writers_vec", "vss_restore_writer", "organization_dn")
    class ExchangeServerRole(_message.Message):
        __slots__ = ()
        class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kUnknown: _ClassVar[ExchangeServerInfo.ExchangeServerRole.Type]
            kMailBox: _ClassVar[ExchangeServerInfo.ExchangeServerRole.Type]
            kNonMailBox: _ClassVar[ExchangeServerInfo.ExchangeServerRole.Type]
        kUnknown: ExchangeServerInfo.ExchangeServerRole.Type
        kMailBox: ExchangeServerInfo.ExchangeServerRole.Type
        kNonMailBox: ExchangeServerInfo.ExchangeServerRole.Type
        def __init__(self) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_DATA_DIR_PATH_FIELD_NUMBER: _ClassVar[int]
    BACKUP_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    BACKUP_UNSUPPORTED_REASON_VEC_FIELD_NUMBER: _ClassVar[int]
    UTC_OFFSETMIN_FIELD_NUMBER: _ClassVar[int]
    VSS_BACKUP_WRITERS_VEC_FIELD_NUMBER: _ClassVar[int]
    VSS_RESTORE_WRITER_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_DN_FIELD_NUMBER: _ClassVar[int]
    id: ExchangeServerIdentity
    role: ExchangeServerInfo.ExchangeServerRole.Type
    version: ExchangeServerVersion
    default_data_dir_path: str
    backup_supported: bool
    backup_unsupported_reason_vec: _containers.RepeatedScalarFieldContainer[str]
    utc_offsetmin: int
    vss_backup_writers_vec: _containers.RepeatedScalarFieldContainer[str]
    vss_restore_writer: str
    organization_dn: str
    def __init__(self, id: _Optional[_Union[ExchangeServerIdentity, _Mapping]] = ..., role: _Optional[_Union[ExchangeServerInfo.ExchangeServerRole.Type, str]] = ..., version: _Optional[_Union[ExchangeServerVersion, _Mapping]] = ..., default_data_dir_path: _Optional[str] = ..., backup_supported: bool = ..., backup_unsupported_reason_vec: _Optional[_Iterable[str]] = ..., utc_offsetmin: _Optional[int] = ..., vss_backup_writers_vec: _Optional[_Iterable[str]] = ..., vss_restore_writer: _Optional[str] = ..., organization_dn: _Optional[str] = ...) -> None: ...

class ExchangeDatabaseIdentity(_message.Message):
    __slots__ = ("guid", "name")
    GUID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    guid: str
    name: str
    def __init__(self, guid: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class ExchangeEDBInfo(_message.Message):
    __slots__ = ("file_path", "volume", "db_size_bytes", "file_size_bytes", "schema_version", "file_system")
    FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    VOLUME_FIELD_NUMBER: _ClassVar[int]
    DB_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    FILE_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_VERSION_FIELD_NUMBER: _ClassVar[int]
    FILE_SYSTEM_FIELD_NUMBER: _ClassVar[int]
    file_path: str
    volume: str
    db_size_bytes: int
    file_size_bytes: int
    schema_version: str
    file_system: str
    def __init__(self, file_path: _Optional[str] = ..., volume: _Optional[str] = ..., db_size_bytes: _Optional[int] = ..., file_size_bytes: _Optional[int] = ..., schema_version: _Optional[str] = ..., file_system: _Optional[str] = ...) -> None: ...

class ExchangeLogInfo(_message.Message):
    __slots__ = ("file_prefix", "folder_path", "volume", "checkpoint_file_name", "circular_logging", "single_log_size", "total_size", "file_system")
    FILE_PREFIX_FIELD_NUMBER: _ClassVar[int]
    FOLDER_PATH_FIELD_NUMBER: _ClassVar[int]
    VOLUME_FIELD_NUMBER: _ClassVar[int]
    CHECKPOINT_FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    CIRCULAR_LOGGING_FIELD_NUMBER: _ClassVar[int]
    SINGLE_LOG_SIZE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    FILE_SYSTEM_FIELD_NUMBER: _ClassVar[int]
    file_prefix: str
    folder_path: str
    volume: str
    checkpoint_file_name: str
    circular_logging: bool
    single_log_size: int
    total_size: int
    file_system: str
    def __init__(self, file_prefix: _Optional[str] = ..., folder_path: _Optional[str] = ..., volume: _Optional[str] = ..., checkpoint_file_name: _Optional[str] = ..., circular_logging: bool = ..., single_log_size: _Optional[int] = ..., total_size: _Optional[int] = ..., file_system: _Optional[str] = ...) -> None: ...

class ExchangeDatabaseBackupTimes(_message.Message):
    __slots__ = ("last_full_backup_date", "last_copy_backup_date", "last_incremental_backup_date", "last_differential_backup_date")
    LAST_FULL_BACKUP_DATE_FIELD_NUMBER: _ClassVar[int]
    LAST_COPY_BACKUP_DATE_FIELD_NUMBER: _ClassVar[int]
    LAST_INCREMENTAL_BACKUP_DATE_FIELD_NUMBER: _ClassVar[int]
    LAST_DIFFERENTIAL_BACKUP_DATE_FIELD_NUMBER: _ClassVar[int]
    last_full_backup_date: LocalTime
    last_copy_backup_date: LocalTime
    last_incremental_backup_date: LocalTime
    last_differential_backup_date: LocalTime
    def __init__(self, last_full_backup_date: _Optional[_Union[LocalTime, _Mapping]] = ..., last_copy_backup_date: _Optional[_Union[LocalTime, _Mapping]] = ..., last_incremental_backup_date: _Optional[_Union[LocalTime, _Mapping]] = ..., last_differential_backup_date: _Optional[_Union[LocalTime, _Mapping]] = ...) -> None: ...

class DatabaseCopyError(_message.Message):
    __slots__ = ("event_id", "error_message", "suspend_comment")
    EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    SUSPEND_COMMENT_FIELD_NUMBER: _ClassVar[int]
    event_id: int
    error_message: str
    suspend_comment: str
    def __init__(self, event_id: _Optional[int] = ..., error_message: _Optional[str] = ..., suspend_comment: _Optional[str] = ...) -> None: ...

class ExchangeDatabase(_message.Message):
    __slots__ = ("id", "type", "state", "master_type", "edb", "log", "backup_times", "created_date", "recovery", "backup_supported", "backup_unsupported_reason_vec", "full_backup_only", "replay_lag_hours", "backup_in_progress", "online_maintenance_in_progress", "content_index_state")
    class ExchangeDatabaseType(_message.Message):
        __slots__ = ()
        class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kUnknown: _ClassVar[ExchangeDatabase.ExchangeDatabaseType.Type]
            kMailbox: _ClassVar[ExchangeDatabase.ExchangeDatabaseType.Type]
            kPublicFolder: _ClassVar[ExchangeDatabase.ExchangeDatabaseType.Type]
        kUnknown: ExchangeDatabase.ExchangeDatabaseType.Type
        kMailbox: ExchangeDatabase.ExchangeDatabaseType.Type
        kPublicFolder: ExchangeDatabase.ExchangeDatabaseType.Type
        def __init__(self) -> None: ...
    class ExchangeDatabaseState(_message.Message):
        __slots__ = ()
        class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kUnknown: _ClassVar[ExchangeDatabase.ExchangeDatabaseState.Type]
            kMounted: _ClassVar[ExchangeDatabase.ExchangeDatabaseState.Type]
            kError: _ClassVar[ExchangeDatabase.ExchangeDatabaseState.Type]
        kUnknown: ExchangeDatabase.ExchangeDatabaseState.Type
        kMounted: ExchangeDatabase.ExchangeDatabaseState.Type
        kError: ExchangeDatabase.ExchangeDatabaseState.Type
        def __init__(self) -> None: ...
    class DatabaseMasterType(_message.Message):
        __slots__ = ()
        class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kServer: _ClassVar[ExchangeDatabase.DatabaseMasterType.Type]
            kDAG: _ClassVar[ExchangeDatabase.DatabaseMasterType.Type]
            kUnknown: _ClassVar[ExchangeDatabase.DatabaseMasterType.Type]
        kServer: ExchangeDatabase.DatabaseMasterType.Type
        kDAG: ExchangeDatabase.DatabaseMasterType.Type
        kUnknown: ExchangeDatabase.DatabaseMasterType.Type
        def __init__(self) -> None: ...
    class DatabaseContentIndexState(_message.Message):
        __slots__ = ()
        class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kUnknown: _ClassVar[ExchangeDatabase.DatabaseContentIndexState.Type]
            kHealthy: _ClassVar[ExchangeDatabase.DatabaseContentIndexState.Type]
            kCrawling: _ClassVar[ExchangeDatabase.DatabaseContentIndexState.Type]
            kFailed: _ClassVar[ExchangeDatabase.DatabaseContentIndexState.Type]
            kSeeding: _ClassVar[ExchangeDatabase.DatabaseContentIndexState.Type]
            kFailedAndSuspended: _ClassVar[ExchangeDatabase.DatabaseContentIndexState.Type]
            kSuspended: _ClassVar[ExchangeDatabase.DatabaseContentIndexState.Type]
            kDisabled: _ClassVar[ExchangeDatabase.DatabaseContentIndexState.Type]
            kAutoSuspended: _ClassVar[ExchangeDatabase.DatabaseContentIndexState.Type]
            kHealthyAndUpgrading: _ClassVar[ExchangeDatabase.DatabaseContentIndexState.Type]
            kDiskUnavailable: _ClassVar[ExchangeDatabase.DatabaseContentIndexState.Type]
            kNotApplicable: _ClassVar[ExchangeDatabase.DatabaseContentIndexState.Type]
        kUnknown: ExchangeDatabase.DatabaseContentIndexState.Type
        kHealthy: ExchangeDatabase.DatabaseContentIndexState.Type
        kCrawling: ExchangeDatabase.DatabaseContentIndexState.Type
        kFailed: ExchangeDatabase.DatabaseContentIndexState.Type
        kSeeding: ExchangeDatabase.DatabaseContentIndexState.Type
        kFailedAndSuspended: ExchangeDatabase.DatabaseContentIndexState.Type
        kSuspended: ExchangeDatabase.DatabaseContentIndexState.Type
        kDisabled: ExchangeDatabase.DatabaseContentIndexState.Type
        kAutoSuspended: ExchangeDatabase.DatabaseContentIndexState.Type
        kHealthyAndUpgrading: ExchangeDatabase.DatabaseContentIndexState.Type
        kDiskUnavailable: ExchangeDatabase.DatabaseContentIndexState.Type
        kNotApplicable: ExchangeDatabase.DatabaseContentIndexState.Type
        def __init__(self) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    MASTER_TYPE_FIELD_NUMBER: _ClassVar[int]
    EDB_FIELD_NUMBER: _ClassVar[int]
    LOG_FIELD_NUMBER: _ClassVar[int]
    BACKUP_TIMES_FIELD_NUMBER: _ClassVar[int]
    CREATED_DATE_FIELD_NUMBER: _ClassVar[int]
    RECOVERY_FIELD_NUMBER: _ClassVar[int]
    BACKUP_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    BACKUP_UNSUPPORTED_REASON_VEC_FIELD_NUMBER: _ClassVar[int]
    FULL_BACKUP_ONLY_FIELD_NUMBER: _ClassVar[int]
    REPLAY_LAG_HOURS_FIELD_NUMBER: _ClassVar[int]
    BACKUP_IN_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    ONLINE_MAINTENANCE_IN_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    CONTENT_INDEX_STATE_FIELD_NUMBER: _ClassVar[int]
    id: ExchangeDatabaseIdentity
    type: ExchangeDatabase.ExchangeDatabaseType.Type
    state: ExchangeDatabase.ExchangeDatabaseState.Type
    master_type: ExchangeDatabase.DatabaseMasterType.Type
    edb: ExchangeEDBInfo
    log: ExchangeLogInfo
    backup_times: ExchangeDatabaseBackupTimes
    created_date: LocalTime
    recovery: bool
    backup_supported: bool
    backup_unsupported_reason_vec: _containers.RepeatedScalarFieldContainer[str]
    full_backup_only: bool
    replay_lag_hours: int
    backup_in_progress: bool
    online_maintenance_in_progress: bool
    content_index_state: ExchangeDatabase.DatabaseContentIndexState.Type
    def __init__(self, id: _Optional[_Union[ExchangeDatabaseIdentity, _Mapping]] = ..., type: _Optional[_Union[ExchangeDatabase.ExchangeDatabaseType.Type, str]] = ..., state: _Optional[_Union[ExchangeDatabase.ExchangeDatabaseState.Type, str]] = ..., master_type: _Optional[_Union[ExchangeDatabase.DatabaseMasterType.Type, str]] = ..., edb: _Optional[_Union[ExchangeEDBInfo, _Mapping]] = ..., log: _Optional[_Union[ExchangeLogInfo, _Mapping]] = ..., backup_times: _Optional[_Union[ExchangeDatabaseBackupTimes, _Mapping]] = ..., created_date: _Optional[_Union[LocalTime, _Mapping]] = ..., recovery: bool = ..., backup_supported: bool = ..., backup_unsupported_reason_vec: _Optional[_Iterable[str]] = ..., full_backup_only: bool = ..., replay_lag_hours: _Optional[int] = ..., backup_in_progress: bool = ..., online_maintenance_in_progress: bool = ..., content_index_state: _Optional[_Union[ExchangeDatabase.DatabaseContentIndexState.Type, str]] = ...) -> None: ...

class ExchangeDAGDatabaseCopy(_message.Message):
    __slots__ = ("db", "copy_guid", "active_copy", "activation_preference", "max_log_to_replay", "max_log_to_copy", "copy_status", "copy_error")
    class DatabaseCopyStatus(_message.Message):
        __slots__ = ()
        class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kUnknown: _ClassVar[ExchangeDAGDatabaseCopy.DatabaseCopyStatus.Type]
            kFailed: _ClassVar[ExchangeDAGDatabaseCopy.DatabaseCopyStatus.Type]
            kSeeding: _ClassVar[ExchangeDAGDatabaseCopy.DatabaseCopyStatus.Type]
            kSuspended: _ClassVar[ExchangeDAGDatabaseCopy.DatabaseCopyStatus.Type]
            kHealthy: _ClassVar[ExchangeDAGDatabaseCopy.DatabaseCopyStatus.Type]
            kServiceDown: _ClassVar[ExchangeDAGDatabaseCopy.DatabaseCopyStatus.Type]
            kInitializing: _ClassVar[ExchangeDAGDatabaseCopy.DatabaseCopyStatus.Type]
            kResynchronizing: _ClassVar[ExchangeDAGDatabaseCopy.DatabaseCopyStatus.Type]
            kMounted: _ClassVar[ExchangeDAGDatabaseCopy.DatabaseCopyStatus.Type]
            kDismounted: _ClassVar[ExchangeDAGDatabaseCopy.DatabaseCopyStatus.Type]
            kMounting: _ClassVar[ExchangeDAGDatabaseCopy.DatabaseCopyStatus.Type]
            kDismounting: _ClassVar[ExchangeDAGDatabaseCopy.DatabaseCopyStatus.Type]
            kDisconnectedAndHealthy: _ClassVar[ExchangeDAGDatabaseCopy.DatabaseCopyStatus.Type]
            kFailedAndSuspended: _ClassVar[ExchangeDAGDatabaseCopy.DatabaseCopyStatus.Type]
            kDisconnectedAndResynchronizing: _ClassVar[ExchangeDAGDatabaseCopy.DatabaseCopyStatus.Type]
            kNonExchangeReplication: _ClassVar[ExchangeDAGDatabaseCopy.DatabaseCopyStatus.Type]
            kSeedingSource: _ClassVar[ExchangeDAGDatabaseCopy.DatabaseCopyStatus.Type]
            kMisconfigured: _ClassVar[ExchangeDAGDatabaseCopy.DatabaseCopyStatus.Type]
        kUnknown: ExchangeDAGDatabaseCopy.DatabaseCopyStatus.Type
        kFailed: ExchangeDAGDatabaseCopy.DatabaseCopyStatus.Type
        kSeeding: ExchangeDAGDatabaseCopy.DatabaseCopyStatus.Type
        kSuspended: ExchangeDAGDatabaseCopy.DatabaseCopyStatus.Type
        kHealthy: ExchangeDAGDatabaseCopy.DatabaseCopyStatus.Type
        kServiceDown: ExchangeDAGDatabaseCopy.DatabaseCopyStatus.Type
        kInitializing: ExchangeDAGDatabaseCopy.DatabaseCopyStatus.Type
        kResynchronizing: ExchangeDAGDatabaseCopy.DatabaseCopyStatus.Type
        kMounted: ExchangeDAGDatabaseCopy.DatabaseCopyStatus.Type
        kDismounted: ExchangeDAGDatabaseCopy.DatabaseCopyStatus.Type
        kMounting: ExchangeDAGDatabaseCopy.DatabaseCopyStatus.Type
        kDismounting: ExchangeDAGDatabaseCopy.DatabaseCopyStatus.Type
        kDisconnectedAndHealthy: ExchangeDAGDatabaseCopy.DatabaseCopyStatus.Type
        kFailedAndSuspended: ExchangeDAGDatabaseCopy.DatabaseCopyStatus.Type
        kDisconnectedAndResynchronizing: ExchangeDAGDatabaseCopy.DatabaseCopyStatus.Type
        kNonExchangeReplication: ExchangeDAGDatabaseCopy.DatabaseCopyStatus.Type
        kSeedingSource: ExchangeDAGDatabaseCopy.DatabaseCopyStatus.Type
        kMisconfigured: ExchangeDAGDatabaseCopy.DatabaseCopyStatus.Type
        def __init__(self) -> None: ...
    DB_FIELD_NUMBER: _ClassVar[int]
    COPY_GUID_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_COPY_FIELD_NUMBER: _ClassVar[int]
    ACTIVATION_PREFERENCE_FIELD_NUMBER: _ClassVar[int]
    MAX_LOG_TO_REPLAY_FIELD_NUMBER: _ClassVar[int]
    MAX_LOG_TO_COPY_FIELD_NUMBER: _ClassVar[int]
    COPY_STATUS_FIELD_NUMBER: _ClassVar[int]
    COPY_ERROR_FIELD_NUMBER: _ClassVar[int]
    db: ExchangeDatabase
    copy_guid: str
    active_copy: bool
    activation_preference: int
    max_log_to_replay: int
    max_log_to_copy: int
    copy_status: ExchangeDAGDatabaseCopy.DatabaseCopyStatus.Type
    copy_error: DatabaseCopyError
    def __init__(self, db: _Optional[_Union[ExchangeDatabase, _Mapping]] = ..., copy_guid: _Optional[str] = ..., active_copy: bool = ..., activation_preference: _Optional[int] = ..., max_log_to_replay: _Optional[int] = ..., max_log_to_copy: _Optional[int] = ..., copy_status: _Optional[_Union[ExchangeDAGDatabaseCopy.DatabaseCopyStatus.Type, str]] = ..., copy_error: _Optional[_Union[DatabaseCopyError, _Mapping]] = ...) -> None: ...

class ExchangeServerNode(_message.Message):
    __slots__ = ("type", "serverinfo")
    class ExchangeServerNodeType(_message.Message):
        __slots__ = ()
        class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kUnsupported: _ClassVar[ExchangeServerNode.ExchangeServerNodeType.Type]
            kStandalone: _ClassVar[ExchangeServerNode.ExchangeServerNodeType.Type]
            kDAG: _ClassVar[ExchangeServerNode.ExchangeServerNodeType.Type]
        kUnsupported: ExchangeServerNode.ExchangeServerNodeType.Type
        kStandalone: ExchangeServerNode.ExchangeServerNodeType.Type
        kDAG: ExchangeServerNode.ExchangeServerNodeType.Type
        def __init__(self) -> None: ...
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SERVERINFO_FIELD_NUMBER: _ClassVar[int]
    type: ExchangeServerNode.ExchangeServerNodeType.Type
    serverinfo: ExchangeServerInfo
    def __init__(self, type: _Optional[_Union[ExchangeServerNode.ExchangeServerNodeType.Type, str]] = ..., serverinfo: _Optional[_Union[ExchangeServerInfo, _Mapping]] = ...) -> None: ...

class ExchangeServerDAGNode(_message.Message):
    __slots__ = ("server", "deleted", "operational", "maintenance", "primaryactivemanager", "other_dag_server_id_vec")
    SERVER_FIELD_NUMBER: _ClassVar[int]
    DELETED_FIELD_NUMBER: _ClassVar[int]
    OPERATIONAL_FIELD_NUMBER: _ClassVar[int]
    MAINTENANCE_FIELD_NUMBER: _ClassVar[int]
    PRIMARYACTIVEMANAGER_FIELD_NUMBER: _ClassVar[int]
    OTHER_DAG_SERVER_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    server: ExchangeServerNode
    deleted: bool
    operational: bool
    maintenance: bool
    primaryactivemanager: bool
    other_dag_server_id_vec: _containers.RepeatedCompositeFieldContainer[ExchangeServerIdentity]
    def __init__(self, server: _Optional[_Union[ExchangeServerNode, _Mapping]] = ..., deleted: bool = ..., operational: bool = ..., maintenance: bool = ..., primaryactivemanager: bool = ..., other_dag_server_id_vec: _Optional[_Iterable[_Union[ExchangeServerIdentity, _Mapping]]] = ...) -> None: ...

class ExchangeDAG(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: ExchangeDAGIdentity
    def __init__(self, id: _Optional[_Union[ExchangeDAGIdentity, _Mapping]] = ...) -> None: ...

class ExchangeTopology(_message.Message):
    __slots__ = ("dag", "standalone_server", "dag_node", "dag_db_copy_vec", "standalone_db_vec")
    DAG_FIELD_NUMBER: _ClassVar[int]
    STANDALONE_SERVER_FIELD_NUMBER: _ClassVar[int]
    DAG_NODE_FIELD_NUMBER: _ClassVar[int]
    DAG_DB_COPY_VEC_FIELD_NUMBER: _ClassVar[int]
    STANDALONE_DB_VEC_FIELD_NUMBER: _ClassVar[int]
    dag: ExchangeDAG
    standalone_server: ExchangeServerNode
    dag_node: ExchangeServerDAGNode
    dag_db_copy_vec: _containers.RepeatedCompositeFieldContainer[ExchangeDAGDatabaseCopy]
    standalone_db_vec: _containers.RepeatedCompositeFieldContainer[ExchangeDatabase]
    def __init__(self, dag: _Optional[_Union[ExchangeDAG, _Mapping]] = ..., standalone_server: _Optional[_Union[ExchangeServerNode, _Mapping]] = ..., dag_node: _Optional[_Union[ExchangeServerDAGNode, _Mapping]] = ..., dag_db_copy_vec: _Optional[_Iterable[_Union[ExchangeDAGDatabaseCopy, _Mapping]]] = ..., standalone_db_vec: _Optional[_Iterable[_Union[ExchangeDatabase, _Mapping]]] = ...) -> None: ...

class ExchangeServer(_message.Message):
    __slots__ = ("status", "agent_supported_status", "last_agent_info_time_usecs", "id", "exchange_id", "owner_id")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kUnknown: _ClassVar[ExchangeServer.Type]
        kHealthy: _ClassVar[ExchangeServer.Type]
        kUnregistered: _ClassVar[ExchangeServer.Type]
        kUnreachable: _ClassVar[ExchangeServer.Type]
        kUnHealthy: _ClassVar[ExchangeServer.Type]
        kDetached: _ClassVar[ExchangeServer.Type]
    kUnknown: ExchangeServer.Type
    kHealthy: ExchangeServer.Type
    kUnregistered: ExchangeServer.Type
    kUnreachable: ExchangeServer.Type
    kUnHealthy: ExchangeServer.Type
    kDetached: ExchangeServer.Type
    class AgentSupportedStatus(_message.Message):
        __slots__ = ()
        class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kSupported: _ClassVar[ExchangeServer.AgentSupportedStatus.Type]
            kUpgrade: _ClassVar[ExchangeServer.AgentSupportedStatus.Type]
            kUnsupported: _ClassVar[ExchangeServer.AgentSupportedStatus.Type]
        kSupported: ExchangeServer.AgentSupportedStatus.Type
        kUpgrade: ExchangeServer.AgentSupportedStatus.Type
        kUnsupported: ExchangeServer.AgentSupportedStatus.Type
        def __init__(self) -> None: ...
    STATUS_FIELD_NUMBER: _ClassVar[int]
    AGENT_SUPPORTED_STATUS_FIELD_NUMBER: _ClassVar[int]
    LAST_AGENT_INFO_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    EXCHANGE_ID_FIELD_NUMBER: _ClassVar[int]
    OWNER_ID_FIELD_NUMBER: _ClassVar[int]
    status: ExchangeServer.Type
    agent_supported_status: ExchangeServer.AgentSupportedStatus.Type
    last_agent_info_time_usecs: int
    id: ExchangeServerIdentity
    exchange_id: int
    owner_id: int
    def __init__(self, status: _Optional[_Union[ExchangeServer.Type, str]] = ..., agent_supported_status: _Optional[_Union[ExchangeServer.AgentSupportedStatus.Type, str]] = ..., last_agent_info_time_usecs: _Optional[int] = ..., id: _Optional[_Union[ExchangeServerIdentity, _Mapping]] = ..., exchange_id: _Optional[int] = ..., owner_id: _Optional[int] = ...) -> None: ...

class ExchangeDatabaseCopyInfo(_message.Message):
    __slots__ = ("status", "id", "db_guid", "entity_id", "exchange_id", "owner_id", "is_active", "is_backup_supported", "backup_unsupported_reason_vec", "creation_date", "activation_preference_number", "server_id", "total_size_in_bytes", "replay_lag_hours", "is_dag_db_copy")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    DB_GUID_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    EXCHANGE_ID_FIELD_NUMBER: _ClassVar[int]
    OWNER_ID_FIELD_NUMBER: _ClassVar[int]
    IS_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    IS_BACKUP_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    BACKUP_UNSUPPORTED_REASON_VEC_FIELD_NUMBER: _ClassVar[int]
    CREATION_DATE_FIELD_NUMBER: _ClassVar[int]
    ACTIVATION_PREFERENCE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    SERVER_ID_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SIZE_IN_BYTES_FIELD_NUMBER: _ClassVar[int]
    REPLAY_LAG_HOURS_FIELD_NUMBER: _ClassVar[int]
    IS_DAG_DB_COPY_FIELD_NUMBER: _ClassVar[int]
    status: ExchangeDatabase.ExchangeDatabaseState.Type
    id: ExchangeDatabaseIdentity
    db_guid: str
    entity_id: int
    exchange_id: int
    owner_id: int
    is_active: bool
    is_backup_supported: bool
    backup_unsupported_reason_vec: _containers.RepeatedScalarFieldContainer[str]
    creation_date: LocalTime
    activation_preference_number: int
    server_id: ExchangeServerIdentity
    total_size_in_bytes: int
    replay_lag_hours: int
    is_dag_db_copy: bool
    def __init__(self, status: _Optional[_Union[ExchangeDatabase.ExchangeDatabaseState.Type, str]] = ..., id: _Optional[_Union[ExchangeDatabaseIdentity, _Mapping]] = ..., db_guid: _Optional[str] = ..., entity_id: _Optional[int] = ..., exchange_id: _Optional[int] = ..., owner_id: _Optional[int] = ..., is_active: bool = ..., is_backup_supported: bool = ..., backup_unsupported_reason_vec: _Optional[_Iterable[str]] = ..., creation_date: _Optional[_Union[LocalTime, _Mapping]] = ..., activation_preference_number: _Optional[int] = ..., server_id: _Optional[_Union[ExchangeServerIdentity, _Mapping]] = ..., total_size_in_bytes: _Optional[int] = ..., replay_lag_hours: _Optional[int] = ..., is_dag_db_copy: bool = ...) -> None: ...

class ExchangeDAGDatabase(_message.Message):
    __slots__ = ("id", "db_copy_info_vec")
    ID_FIELD_NUMBER: _ClassVar[int]
    DB_COPY_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    id: ExchangeDatabaseIdentity
    db_copy_info_vec: _containers.RepeatedCompositeFieldContainer[ExchangeDatabaseCopyInfo]
    def __init__(self, id: _Optional[_Union[ExchangeDatabaseIdentity, _Mapping]] = ..., db_copy_info_vec: _Optional[_Iterable[_Union[ExchangeDatabaseCopyInfo, _Mapping]]] = ...) -> None: ...

class ExchangeDAGBackupPreference(_message.Message):
    __slots__ = ("preference", "passive_preference", "passive_preference_server_guid_vec")
    class DAGBackupPreference(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kPassiveOnly: _ClassVar[ExchangeDAGBackupPreference.DAGBackupPreference]
        kActivePassive: _ClassVar[ExchangeDAGBackupPreference.DAGBackupPreference]
    kPassiveOnly: ExchangeDAGBackupPreference.DAGBackupPreference
    kActivePassive: ExchangeDAGBackupPreference.DAGBackupPreference
    class PassivePreference(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kReverseActivationOrder: _ClassVar[ExchangeDAGBackupPreference.PassivePreference]
        kUserSpecified: _ClassVar[ExchangeDAGBackupPreference.PassivePreference]
    kReverseActivationOrder: ExchangeDAGBackupPreference.PassivePreference
    kUserSpecified: ExchangeDAGBackupPreference.PassivePreference
    PREFERENCE_FIELD_NUMBER: _ClassVar[int]
    PASSIVE_PREFERENCE_FIELD_NUMBER: _ClassVar[int]
    PASSIVE_PREFERENCE_SERVER_GUID_VEC_FIELD_NUMBER: _ClassVar[int]
    preference: ExchangeDAGBackupPreference.DAGBackupPreference
    passive_preference: ExchangeDAGBackupPreference.PassivePreference
    passive_preference_server_guid_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, preference: _Optional[_Union[ExchangeDAGBackupPreference.DAGBackupPreference, str]] = ..., passive_preference: _Optional[_Union[ExchangeDAGBackupPreference.PassivePreference, str]] = ..., passive_preference_server_guid_vec: _Optional[_Iterable[str]] = ...) -> None: ...

class ExchangeDAGInfo(_message.Message):
    __slots__ = ("id", "server_vec", "backup_preference")
    ID_FIELD_NUMBER: _ClassVar[int]
    SERVER_VEC_FIELD_NUMBER: _ClassVar[int]
    BACKUP_PREFERENCE_FIELD_NUMBER: _ClassVar[int]
    id: ExchangeDAGIdentity
    server_vec: _containers.RepeatedCompositeFieldContainer[ExchangeServer]
    backup_preference: ExchangeDAGBackupPreference
    def __init__(self, id: _Optional[_Union[ExchangeDAGIdentity, _Mapping]] = ..., server_vec: _Optional[_Iterable[_Union[ExchangeServer, _Mapping]]] = ..., backup_preference: _Optional[_Union[ExchangeDAGBackupPreference, _Mapping]] = ...) -> None: ...

class Entity(_message.Message):
    __slots__ = ("type", "uuid", "name", "owner_id", "exchange", "standalone_database", "dag_database_copy", "dag_info", "dag_database")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kRootContainer: _ClassVar[Entity.Type]
        kDAGRootContainer: _ClassVar[Entity.Type]
        kExchangeNode: _ClassVar[Entity.Type]
        kExchangeDAGDatabaseCopy: _ClassVar[Entity.Type]
        kExchangeStandaloneDatabase: _ClassVar[Entity.Type]
        kExchangeDAG: _ClassVar[Entity.Type]
        kExchangeDAGDatabase: _ClassVar[Entity.Type]
    kRootContainer: Entity.Type
    kDAGRootContainer: Entity.Type
    kExchangeNode: Entity.Type
    kExchangeDAGDatabaseCopy: Entity.Type
    kExchangeStandaloneDatabase: Entity.Type
    kExchangeDAG: Entity.Type
    kExchangeDAGDatabase: Entity.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    OWNER_ID_FIELD_NUMBER: _ClassVar[int]
    EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    STANDALONE_DATABASE_FIELD_NUMBER: _ClassVar[int]
    DAG_DATABASE_COPY_FIELD_NUMBER: _ClassVar[int]
    DAG_INFO_FIELD_NUMBER: _ClassVar[int]
    DAG_DATABASE_FIELD_NUMBER: _ClassVar[int]
    type: Entity.Type
    uuid: str
    name: str
    owner_id: int
    exchange: ExchangeTopology
    standalone_database: ExchangeDatabase
    dag_database_copy: ExchangeDAGDatabaseCopy
    dag_info: ExchangeDAGInfo
    dag_database: ExchangeDAGDatabase
    def __init__(self, type: _Optional[_Union[Entity.Type, str]] = ..., uuid: _Optional[str] = ..., name: _Optional[str] = ..., owner_id: _Optional[int] = ..., exchange: _Optional[_Union[ExchangeTopology, _Mapping]] = ..., standalone_database: _Optional[_Union[ExchangeDatabase, _Mapping]] = ..., dag_database_copy: _Optional[_Union[ExchangeDAGDatabaseCopy, _Mapping]] = ..., dag_info: _Optional[_Union[ExchangeDAGInfo, _Mapping]] = ..., dag_database: _Optional[_Union[ExchangeDAGDatabase, _Mapping]] = ...) -> None: ...

class ExchangeDatabaseMailboxManifest(_message.Message):
    __slots__ = ("type", "file_path", "capacity")
    class ExchangeManifestType(_message.Message):
        __slots__ = ()
        class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kNone: _ClassVar[ExchangeDatabaseMailboxManifest.ExchangeManifestType.Type]
            kCSV: _ClassVar[ExchangeDatabaseMailboxManifest.ExchangeManifestType.Type]
        kNone: ExchangeDatabaseMailboxManifest.ExchangeManifestType.Type
        kCSV: ExchangeDatabaseMailboxManifest.ExchangeManifestType.Type
        def __init__(self) -> None: ...
    TYPE_FIELD_NUMBER: _ClassVar[int]
    FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    CAPACITY_FIELD_NUMBER: _ClassVar[int]
    type: ExchangeDatabaseMailboxManifest.ExchangeManifestType.Type
    file_path: str
    capacity: int
    def __init__(self, type: _Optional[_Union[ExchangeDatabaseMailboxManifest.ExchangeManifestType.Type, str]] = ..., file_path: _Optional[str] = ..., capacity: _Optional[int] = ...) -> None: ...
