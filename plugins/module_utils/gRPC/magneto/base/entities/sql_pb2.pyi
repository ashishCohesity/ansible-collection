from magneto.api.common import stats_pb2 as _stats_pb2
from magneto.agents.base import agent_pb2 as _agent_pb2
from magneto.base import enums_pb2 as _enums_pb2
from magneto.base import error_pb2 as _error_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SqlId(_message.Message):
    __slots__ = ("instance_id", "database_id", "create_date_msecs", "aag_id", "group_database_id")
    INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    DATABASE_ID_FIELD_NUMBER: _ClassVar[int]
    CREATE_DATE_MSECS_FIELD_NUMBER: _ClassVar[int]
    AAG_ID_FIELD_NUMBER: _ClassVar[int]
    GROUP_DATABASE_ID_FIELD_NUMBER: _ClassVar[int]
    instance_id: bytes
    database_id: int
    create_date_msecs: int
    aag_id: str
    group_database_id: str
    def __init__(self, instance_id: _Optional[bytes] = ..., database_id: _Optional[int] = ..., create_date_msecs: _Optional[int] = ..., aag_id: _Optional[str] = ..., group_database_id: _Optional[str] = ...) -> None: ...

class SqlServerInstanceVersion(_message.Message):
    __slots__ = ("major_version", "minor_version", "build", "revision", "version_string")
    MAJOR_VERSION_FIELD_NUMBER: _ClassVar[int]
    MINOR_VERSION_FIELD_NUMBER: _ClassVar[int]
    BUILD_FIELD_NUMBER: _ClassVar[int]
    REVISION_FIELD_NUMBER: _ClassVar[int]
    VERSION_STRING_FIELD_NUMBER: _ClassVar[int]
    major_version: int
    minor_version: int
    build: int
    revision: int
    version_string: str
    def __init__(self, major_version: _Optional[int] = ..., minor_version: _Optional[int] = ..., build: _Optional[int] = ..., revision: _Optional[int] = ..., version_string: _Optional[str] = ...) -> None: ...

class SQLInstanceInfo(_message.Message):
    __slots__ = ("instance_name", "instance_id", "is_online", "version", "edition_info", "level_info", "update_level_info", "build_type_info", "cluster_resource_endpoint_vec", "is_fci_instance", "guid_in_windows_cluster", "default_data_location", "default_log_location", "fci_node_name_vec")
    class Edition(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kEnterpriseEdition: _ClassVar[SQLInstanceInfo.Edition]
        kEnterpriseEditionCoreBasedLicensing: _ClassVar[SQLInstanceInfo.Edition]
        kEnterpriseEvaluationEdition: _ClassVar[SQLInstanceInfo.Edition]
        kBusinessIntelligenceEdition: _ClassVar[SQLInstanceInfo.Edition]
        kDeveloperEdition: _ClassVar[SQLInstanceInfo.Edition]
        kExpressEdition: _ClassVar[SQLInstanceInfo.Edition]
        kExpressEditionWithAdvancedServices: _ClassVar[SQLInstanceInfo.Edition]
        kStandardEdition: _ClassVar[SQLInstanceInfo.Edition]
        kWebEdition: _ClassVar[SQLInstanceInfo.Edition]
        kSQLAzure: _ClassVar[SQLInstanceInfo.Edition]
        kUnknownEdition: _ClassVar[SQLInstanceInfo.Edition]
    kEnterpriseEdition: SQLInstanceInfo.Edition
    kEnterpriseEditionCoreBasedLicensing: SQLInstanceInfo.Edition
    kEnterpriseEvaluationEdition: SQLInstanceInfo.Edition
    kBusinessIntelligenceEdition: SQLInstanceInfo.Edition
    kDeveloperEdition: SQLInstanceInfo.Edition
    kExpressEdition: SQLInstanceInfo.Edition
    kExpressEditionWithAdvancedServices: SQLInstanceInfo.Edition
    kStandardEdition: SQLInstanceInfo.Edition
    kWebEdition: SQLInstanceInfo.Edition
    kSQLAzure: SQLInstanceInfo.Edition
    kUnknownEdition: SQLInstanceInfo.Edition
    class ProductLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kRTM: _ClassVar[SQLInstanceInfo.ProductLevel]
        kSPn: _ClassVar[SQLInstanceInfo.ProductLevel]
        kCTPn: _ClassVar[SQLInstanceInfo.ProductLevel]
        kUnknownProductLevel: _ClassVar[SQLInstanceInfo.ProductLevel]
    kRTM: SQLInstanceInfo.ProductLevel
    kSPn: SQLInstanceInfo.ProductLevel
    kCTPn: SQLInstanceInfo.ProductLevel
    kUnknownProductLevel: SQLInstanceInfo.ProductLevel
    class ProductUpdateLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kCUn: _ClassVar[SQLInstanceInfo.ProductUpdateLevel]
        kUnknownProductUpdateLevel: _ClassVar[SQLInstanceInfo.ProductUpdateLevel]
    kCUn: SQLInstanceInfo.ProductUpdateLevel
    kUnknownProductUpdateLevel: SQLInstanceInfo.ProductUpdateLevel
    class ProductBuildType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kOD: _ClassVar[SQLInstanceInfo.ProductBuildType]
        kGDR: _ClassVar[SQLInstanceInfo.ProductBuildType]
        kUnknownProductBuildType: _ClassVar[SQLInstanceInfo.ProductBuildType]
    kOD: SQLInstanceInfo.ProductBuildType
    kGDR: SQLInstanceInfo.ProductBuildType
    kUnknownProductBuildType: SQLInstanceInfo.ProductBuildType
    class EditionInfo(_message.Message):
        __slots__ = ("edition", "is_64_bit", "edition_string")
        EDITION_FIELD_NUMBER: _ClassVar[int]
        IS_64_BIT_FIELD_NUMBER: _ClassVar[int]
        EDITION_STRING_FIELD_NUMBER: _ClassVar[int]
        edition: SQLInstanceInfo.Edition
        is_64_bit: bool
        edition_string: str
        def __init__(self, edition: _Optional[_Union[SQLInstanceInfo.Edition, str]] = ..., is_64_bit: bool = ..., edition_string: _Optional[str] = ...) -> None: ...
    class ProductLevelInfo(_message.Message):
        __slots__ = ("level", "level_string")
        LEVEL_FIELD_NUMBER: _ClassVar[int]
        LEVEL_STRING_FIELD_NUMBER: _ClassVar[int]
        level: SQLInstanceInfo.ProductLevel
        level_string: str
        def __init__(self, level: _Optional[_Union[SQLInstanceInfo.ProductLevel, str]] = ..., level_string: _Optional[str] = ...) -> None: ...
    class ProductUpdateLevelInfo(_message.Message):
        __slots__ = ("update_level", "update_level_string")
        UPDATE_LEVEL_FIELD_NUMBER: _ClassVar[int]
        UPDATE_LEVEL_STRING_FIELD_NUMBER: _ClassVar[int]
        update_level: SQLInstanceInfo.ProductUpdateLevel
        update_level_string: str
        def __init__(self, update_level: _Optional[_Union[SQLInstanceInfo.ProductUpdateLevel, str]] = ..., update_level_string: _Optional[str] = ...) -> None: ...
    class ProductBuildTypeInfo(_message.Message):
        __slots__ = ("build_type", "build_type_string")
        BUILD_TYPE_FIELD_NUMBER: _ClassVar[int]
        BUILD_TYPE_STRING_FIELD_NUMBER: _ClassVar[int]
        build_type: SQLInstanceInfo.ProductBuildType
        build_type_string: str
        def __init__(self, build_type: _Optional[_Union[SQLInstanceInfo.ProductBuildType, str]] = ..., build_type_string: _Optional[str] = ...) -> None: ...
    INSTANCE_NAME_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    IS_ONLINE_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    EDITION_INFO_FIELD_NUMBER: _ClassVar[int]
    LEVEL_INFO_FIELD_NUMBER: _ClassVar[int]
    UPDATE_LEVEL_INFO_FIELD_NUMBER: _ClassVar[int]
    BUILD_TYPE_INFO_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_RESOURCE_ENDPOINT_VEC_FIELD_NUMBER: _ClassVar[int]
    IS_FCI_INSTANCE_FIELD_NUMBER: _ClassVar[int]
    GUID_IN_WINDOWS_CLUSTER_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_DATA_LOCATION_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_LOG_LOCATION_FIELD_NUMBER: _ClassVar[int]
    FCI_NODE_NAME_VEC_FIELD_NUMBER: _ClassVar[int]
    instance_name: bytes
    instance_id: bytes
    is_online: bool
    version: SqlServerInstanceVersion
    edition_info: SQLInstanceInfo.EditionInfo
    level_info: SQLInstanceInfo.ProductLevelInfo
    update_level_info: SQLInstanceInfo.ProductUpdateLevelInfo
    build_type_info: SQLInstanceInfo.ProductBuildTypeInfo
    cluster_resource_endpoint_vec: _containers.RepeatedCompositeFieldContainer[_agent_pb2.ClusterNetworkingInfo.Endpoint]
    is_fci_instance: bool
    guid_in_windows_cluster: str
    default_data_location: str
    default_log_location: str
    fci_node_name_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, instance_name: _Optional[bytes] = ..., instance_id: _Optional[bytes] = ..., is_online: bool = ..., version: _Optional[_Union[SqlServerInstanceVersion, _Mapping]] = ..., edition_info: _Optional[_Union[SQLInstanceInfo.EditionInfo, _Mapping]] = ..., level_info: _Optional[_Union[SQLInstanceInfo.ProductLevelInfo, _Mapping]] = ..., update_level_info: _Optional[_Union[SQLInstanceInfo.ProductUpdateLevelInfo, _Mapping]] = ..., build_type_info: _Optional[_Union[SQLInstanceInfo.ProductBuildTypeInfo, _Mapping]] = ..., cluster_resource_endpoint_vec: _Optional[_Iterable[_Union[_agent_pb2.ClusterNetworkingInfo.Endpoint, _Mapping]]] = ..., is_fci_instance: bool = ..., guid_in_windows_cluster: _Optional[str] = ..., default_data_location: _Optional[str] = ..., default_log_location: _Optional[str] = ..., fci_node_name_vec: _Optional[_Iterable[str]] = ...) -> None: ...

class RecoveryModel(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kSimpleRecoveryModel: _ClassVar[RecoveryModel.Type]
        kFullRecoveryModel: _ClassVar[RecoveryModel.Type]
        kBulkLoggedRecoveryModel: _ClassVar[RecoveryModel.Type]
    kSimpleRecoveryModel: RecoveryModel.Type
    kFullRecoveryModel: RecoveryModel.Type
    kBulkLoggedRecoveryModel: RecoveryModel.Type
    def __init__(self) -> None: ...

class SQLDatabaseState(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kOnline: _ClassVar[SQLDatabaseState.Type]
        kRestoring: _ClassVar[SQLDatabaseState.Type]
        kRecovering: _ClassVar[SQLDatabaseState.Type]
        kRecoveryPending: _ClassVar[SQLDatabaseState.Type]
        kSuspect: _ClassVar[SQLDatabaseState.Type]
        kEmergency: _ClassVar[SQLDatabaseState.Type]
        kOffline: _ClassVar[SQLDatabaseState.Type]
        kCopying: _ClassVar[SQLDatabaseState.Type]
        kOfflineSecondary: _ClassVar[SQLDatabaseState.Type]
    kOnline: SQLDatabaseState.Type
    kRestoring: SQLDatabaseState.Type
    kRecovering: SQLDatabaseState.Type
    kRecoveryPending: SQLDatabaseState.Type
    kSuspect: SQLDatabaseState.Type
    kEmergency: SQLDatabaseState.Type
    kOffline: SQLDatabaseState.Type
    kCopying: SQLDatabaseState.Type
    kOfflineSecondary: SQLDatabaseState.Type
    def __init__(self) -> None: ...

class AAGReplicaInfo(_message.Message):
    __slots__ = ("host_entity_id", "windows_host_name", "replica_id", "group_id", "replica_server_name", "availability_mode", "create_date_msecs", "modify_date_msecs", "backup_priority", "primary_role_allow_connections", "secondary_role_allow_connections", "is_local", "role", "operational_state", "synchronization_health", "db_info_vec", "wsfc_node_id")
    class Mode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kAsync: _ClassVar[AAGReplicaInfo.Mode]
        kSync: _ClassVar[AAGReplicaInfo.Mode]
    kAsync: AAGReplicaInfo.Mode
    kSync: AAGReplicaInfo.Mode
    class AllowedConnectionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNone: _ClassVar[AAGReplicaInfo.AllowedConnectionType]
        kReadOnly: _ClassVar[AAGReplicaInfo.AllowedConnectionType]
        kAll: _ClassVar[AAGReplicaInfo.AllowedConnectionType]
        kReadWrite: _ClassVar[AAGReplicaInfo.AllowedConnectionType]
    kNone: AAGReplicaInfo.AllowedConnectionType
    kReadOnly: AAGReplicaInfo.AllowedConnectionType
    kAll: AAGReplicaInfo.AllowedConnectionType
    kReadWrite: AAGReplicaInfo.AllowedConnectionType
    class Role(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kResolving: _ClassVar[AAGReplicaInfo.Role]
        kPrimary: _ClassVar[AAGReplicaInfo.Role]
        kSecondary: _ClassVar[AAGReplicaInfo.Role]
    kResolving: AAGReplicaInfo.Role
    kPrimary: AAGReplicaInfo.Role
    kSecondary: AAGReplicaInfo.Role
    class OperationalState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kPendingFailover: _ClassVar[AAGReplicaInfo.OperationalState]
        kPending: _ClassVar[AAGReplicaInfo.OperationalState]
        kOnline: _ClassVar[AAGReplicaInfo.OperationalState]
        kOffline: _ClassVar[AAGReplicaInfo.OperationalState]
        kFailed: _ClassVar[AAGReplicaInfo.OperationalState]
        kFailedNoQuorum: _ClassVar[AAGReplicaInfo.OperationalState]
        kNull: _ClassVar[AAGReplicaInfo.OperationalState]
    kPendingFailover: AAGReplicaInfo.OperationalState
    kPending: AAGReplicaInfo.OperationalState
    kOnline: AAGReplicaInfo.OperationalState
    kOffline: AAGReplicaInfo.OperationalState
    kFailed: AAGReplicaInfo.OperationalState
    kFailedNoQuorum: AAGReplicaInfo.OperationalState
    kNull: AAGReplicaInfo.OperationalState
    class SynchronizationHealth(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNotHealthy: _ClassVar[AAGReplicaInfo.SynchronizationHealth]
        kPartiallyHealthy: _ClassVar[AAGReplicaInfo.SynchronizationHealth]
        kHealthy: _ClassVar[AAGReplicaInfo.SynchronizationHealth]
    kNotHealthy: AAGReplicaInfo.SynchronizationHealth
    kPartiallyHealthy: AAGReplicaInfo.SynchronizationHealth
    kHealthy: AAGReplicaInfo.SynchronizationHealth
    class DbInfo(_message.Message):
        __slots__ = ("entity_id", "sql_id", "database_name")
        ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
        SQL_ID_FIELD_NUMBER: _ClassVar[int]
        DATABASE_NAME_FIELD_NUMBER: _ClassVar[int]
        entity_id: int
        sql_id: SqlId
        database_name: str
        def __init__(self, entity_id: _Optional[int] = ..., sql_id: _Optional[_Union[SqlId, _Mapping]] = ..., database_name: _Optional[str] = ...) -> None: ...
    HOST_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    WINDOWS_HOST_NAME_FIELD_NUMBER: _ClassVar[int]
    REPLICA_ID_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    REPLICA_SERVER_NAME_FIELD_NUMBER: _ClassVar[int]
    AVAILABILITY_MODE_FIELD_NUMBER: _ClassVar[int]
    CREATE_DATE_MSECS_FIELD_NUMBER: _ClassVar[int]
    MODIFY_DATE_MSECS_FIELD_NUMBER: _ClassVar[int]
    BACKUP_PRIORITY_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_ROLE_ALLOW_CONNECTIONS_FIELD_NUMBER: _ClassVar[int]
    SECONDARY_ROLE_ALLOW_CONNECTIONS_FIELD_NUMBER: _ClassVar[int]
    IS_LOCAL_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    OPERATIONAL_STATE_FIELD_NUMBER: _ClassVar[int]
    SYNCHRONIZATION_HEALTH_FIELD_NUMBER: _ClassVar[int]
    DB_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    WSFC_NODE_ID_FIELD_NUMBER: _ClassVar[int]
    host_entity_id: int
    windows_host_name: str
    replica_id: str
    group_id: str
    replica_server_name: str
    availability_mode: AAGReplicaInfo.Mode
    create_date_msecs: int
    modify_date_msecs: int
    backup_priority: int
    primary_role_allow_connections: AAGReplicaInfo.AllowedConnectionType
    secondary_role_allow_connections: AAGReplicaInfo.AllowedConnectionType
    is_local: bool
    role: AAGReplicaInfo.Role
    operational_state: AAGReplicaInfo.OperationalState
    synchronization_health: AAGReplicaInfo.SynchronizationHealth
    db_info_vec: _containers.RepeatedCompositeFieldContainer[AAGReplicaInfo.DbInfo]
    wsfc_node_id: str
    def __init__(self, host_entity_id: _Optional[int] = ..., windows_host_name: _Optional[str] = ..., replica_id: _Optional[str] = ..., group_id: _Optional[str] = ..., replica_server_name: _Optional[str] = ..., availability_mode: _Optional[_Union[AAGReplicaInfo.Mode, str]] = ..., create_date_msecs: _Optional[int] = ..., modify_date_msecs: _Optional[int] = ..., backup_priority: _Optional[int] = ..., primary_role_allow_connections: _Optional[_Union[AAGReplicaInfo.AllowedConnectionType, str]] = ..., secondary_role_allow_connections: _Optional[_Union[AAGReplicaInfo.AllowedConnectionType, str]] = ..., is_local: bool = ..., role: _Optional[_Union[AAGReplicaInfo.Role, str]] = ..., operational_state: _Optional[_Union[AAGReplicaInfo.OperationalState, str]] = ..., synchronization_health: _Optional[_Union[AAGReplicaInfo.SynchronizationHealth, str]] = ..., db_info_vec: _Optional[_Iterable[_Union[AAGReplicaInfo.DbInfo, _Mapping]]] = ..., wsfc_node_id: _Optional[str] = ...) -> None: ...

class AAGDbInfo(_message.Message):
    __slots__ = ("group_database_id", "database_name")
    GROUP_DATABASE_ID_FIELD_NUMBER: _ClassVar[int]
    DATABASE_NAME_FIELD_NUMBER: _ClassVar[int]
    group_database_id: str
    database_name: str
    def __init__(self, group_database_id: _Optional[str] = ..., database_name: _Optional[str] = ...) -> None: ...

class AAGBackupPreference(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kPrimaryReplicaOnly: _ClassVar[AAGBackupPreference.Type]
        kSecondaryReplicaOnly: _ClassVar[AAGBackupPreference.Type]
        kPreferSecondaryReplica: _ClassVar[AAGBackupPreference.Type]
        kAnyReplica: _ClassVar[AAGBackupPreference.Type]
    kPrimaryReplicaOnly: AAGBackupPreference.Type
    kSecondaryReplicaOnly: AAGBackupPreference.Type
    kPreferSecondaryReplica: AAGBackupPreference.Type
    kAnyReplica: AAGBackupPreference.Type
    def __init__(self) -> None: ...

class AAGInfo(_message.Message):
    __slots__ = ("group_id", "name", "automated_backup_preference", "db_info_vec", "replica_vec", "error", "host_type")
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    AUTOMATED_BACKUP_PREFERENCE_FIELD_NUMBER: _ClassVar[int]
    DB_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    REPLICA_VEC_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    HOST_TYPE_FIELD_NUMBER: _ClassVar[int]
    group_id: str
    name: str
    automated_backup_preference: AAGBackupPreference.Type
    db_info_vec: _containers.RepeatedCompositeFieldContainer[AAGDbInfo]
    replica_vec: _containers.RepeatedCompositeFieldContainer[AAGReplicaInfo]
    error: _error_pb2.ErrorProto
    host_type: _enums_pb2.HostEnv.Type
    def __init__(self, group_id: _Optional[str] = ..., name: _Optional[str] = ..., automated_backup_preference: _Optional[_Union[AAGBackupPreference.Type, str]] = ..., db_info_vec: _Optional[_Iterable[_Union[AAGDbInfo, _Mapping]]] = ..., replica_vec: _Optional[_Iterable[_Union[AAGReplicaInfo, _Mapping]]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., host_type: _Optional[_Union[_enums_pb2.HostEnv.Type, str]] = ...) -> None: ...

class Entity(_message.Message):
    __slots__ = ("type", "sql_id", "owner_id", "instance_name", "sql_instance_info", "database_name", "recovery_model", "create_date", "sql_server_db_state", "is_available_for_vss_backup", "is_system_db", "db_aag_entity_id", "db_aag_name", "db_file_info_vec", "total_size_bytes", "aag_info", "sql_instance_version", "db_owner_username", "db_file_group_info_vec", "db_compatibility_level", "read_only", "is_fci", "is_database_cloned", "front_end_size_info", "is_encrypted", "aag_db_copy_info_vec", "is_aag_first_class_citizen")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kInstance: _ClassVar[Entity.Type]
        kDatabase: _ClassVar[Entity.Type]
        kAAG: _ClassVar[Entity.Type]
        kAAGRootContainer: _ClassVar[Entity.Type]
        kRootContainer: _ClassVar[Entity.Type]
        kAAGDatabase: _ClassVar[Entity.Type]
    kInstance: Entity.Type
    kDatabase: Entity.Type
    kAAG: Entity.Type
    kAAGRootContainer: Entity.Type
    kRootContainer: Entity.Type
    kAAGDatabase: Entity.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SQL_ID_FIELD_NUMBER: _ClassVar[int]
    OWNER_ID_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_NAME_FIELD_NUMBER: _ClassVar[int]
    SQL_INSTANCE_INFO_FIELD_NUMBER: _ClassVar[int]
    DATABASE_NAME_FIELD_NUMBER: _ClassVar[int]
    RECOVERY_MODEL_FIELD_NUMBER: _ClassVar[int]
    CREATE_DATE_FIELD_NUMBER: _ClassVar[int]
    SQL_SERVER_DB_STATE_FIELD_NUMBER: _ClassVar[int]
    IS_AVAILABLE_FOR_VSS_BACKUP_FIELD_NUMBER: _ClassVar[int]
    IS_SYSTEM_DB_FIELD_NUMBER: _ClassVar[int]
    DB_AAG_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    DB_AAG_NAME_FIELD_NUMBER: _ClassVar[int]
    DB_FILE_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    AAG_INFO_FIELD_NUMBER: _ClassVar[int]
    SQL_INSTANCE_VERSION_FIELD_NUMBER: _ClassVar[int]
    DB_OWNER_USERNAME_FIELD_NUMBER: _ClassVar[int]
    DB_FILE_GROUP_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    DB_COMPATIBILITY_LEVEL_FIELD_NUMBER: _ClassVar[int]
    READ_ONLY_FIELD_NUMBER: _ClassVar[int]
    IS_FCI_FIELD_NUMBER: _ClassVar[int]
    IS_DATABASE_CLONED_FIELD_NUMBER: _ClassVar[int]
    FRONT_END_SIZE_INFO_FIELD_NUMBER: _ClassVar[int]
    IS_ENCRYPTED_FIELD_NUMBER: _ClassVar[int]
    AAG_DB_COPY_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    IS_AAG_FIRST_CLASS_CITIZEN_FIELD_NUMBER: _ClassVar[int]
    type: Entity.Type
    sql_id: SqlId
    owner_id: int
    instance_name: str
    sql_instance_info: SQLInstanceInfo
    database_name: str
    recovery_model: RecoveryModel.Type
    create_date: str
    sql_server_db_state: SQLDatabaseState.Type
    is_available_for_vss_backup: bool
    is_system_db: bool
    db_aag_entity_id: int
    db_aag_name: str
    db_file_info_vec: _containers.RepeatedCompositeFieldContainer[FileInfo]
    total_size_bytes: int
    aag_info: AAGInfo
    sql_instance_version: SqlServerInstanceVersion
    db_owner_username: str
    db_file_group_info_vec: _containers.RepeatedCompositeFieldContainer[SQLDatabaseFileGroupInfo]
    db_compatibility_level: int
    read_only: bool
    is_fci: bool
    is_database_cloned: bool
    front_end_size_info: _stats_pb2.SizeInfo
    is_encrypted: bool
    aag_db_copy_info_vec: _containers.RepeatedCompositeFieldContainer[AAGDatabaseCopyInfo]
    is_aag_first_class_citizen: bool
    def __init__(self, type: _Optional[_Union[Entity.Type, str]] = ..., sql_id: _Optional[_Union[SqlId, _Mapping]] = ..., owner_id: _Optional[int] = ..., instance_name: _Optional[str] = ..., sql_instance_info: _Optional[_Union[SQLInstanceInfo, _Mapping]] = ..., database_name: _Optional[str] = ..., recovery_model: _Optional[_Union[RecoveryModel.Type, str]] = ..., create_date: _Optional[str] = ..., sql_server_db_state: _Optional[_Union[SQLDatabaseState.Type, str]] = ..., is_available_for_vss_backup: bool = ..., is_system_db: bool = ..., db_aag_entity_id: _Optional[int] = ..., db_aag_name: _Optional[str] = ..., db_file_info_vec: _Optional[_Iterable[_Union[FileInfo, _Mapping]]] = ..., total_size_bytes: _Optional[int] = ..., aag_info: _Optional[_Union[AAGInfo, _Mapping]] = ..., sql_instance_version: _Optional[_Union[SqlServerInstanceVersion, _Mapping]] = ..., db_owner_username: _Optional[str] = ..., db_file_group_info_vec: _Optional[_Iterable[_Union[SQLDatabaseFileGroupInfo, _Mapping]]] = ..., db_compatibility_level: _Optional[int] = ..., read_only: bool = ..., is_fci: bool = ..., is_database_cloned: bool = ..., front_end_size_info: _Optional[_Union[_stats_pb2.SizeInfo, _Mapping]] = ..., is_encrypted: bool = ..., aag_db_copy_info_vec: _Optional[_Iterable[_Union[AAGDatabaseCopyInfo, _Mapping]]] = ..., is_aag_first_class_citizen: bool = ...) -> None: ...

class DBRestoreOverwritePolicy(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kFailIfExists: _ClassVar[DBRestoreOverwritePolicy.Type]
        kOverwrite: _ClassVar[DBRestoreOverwritePolicy.Type]
    kFailIfExists: DBRestoreOverwritePolicy.Type
    kOverwrite: DBRestoreOverwritePolicy.Type
    def __init__(self) -> None: ...

class FileInfo(_message.Message):
    __slots__ = ("full_path", "size_bytes", "type", "logical_name", "is_primary_database_file", "is_on_external_storage")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kRows: _ClassVar[FileInfo.Type]
        kLog: _ClassVar[FileInfo.Type]
        kFileStream: _ClassVar[FileInfo.Type]
        kNotSupportedType: _ClassVar[FileInfo.Type]
        kFullText: _ClassVar[FileInfo.Type]
    kRows: FileInfo.Type
    kLog: FileInfo.Type
    kFileStream: FileInfo.Type
    kNotSupportedType: FileInfo.Type
    kFullText: FileInfo.Type
    FULL_PATH_FIELD_NUMBER: _ClassVar[int]
    SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    LOGICAL_NAME_FIELD_NUMBER: _ClassVar[int]
    IS_PRIMARY_DATABASE_FILE_FIELD_NUMBER: _ClassVar[int]
    IS_ON_EXTERNAL_STORAGE_FIELD_NUMBER: _ClassVar[int]
    full_path: str
    size_bytes: int
    type: FileInfo.Type
    logical_name: str
    is_primary_database_file: bool
    is_on_external_storage: bool
    def __init__(self, full_path: _Optional[str] = ..., size_bytes: _Optional[int] = ..., type: _Optional[_Union[FileInfo.Type, str]] = ..., logical_name: _Optional[str] = ..., is_primary_database_file: bool = ..., is_on_external_storage: bool = ...) -> None: ...

class SQLDatabaseFileGroupInfo(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class AdvancedSettings(_message.Message):
    __slots__ = ("missing_db_backup_status", "report_all_non_autoprotect_db_errors", "offline_restoring_db_backup_status", "cloned_db_backup_status", "db_backup_if_not_online_status", "read_only_db_backup_status")
    class ErrorType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kError: _ClassVar[AdvancedSettings.ErrorType]
        kWarn: _ClassVar[AdvancedSettings.ErrorType]
        kIgnore: _ClassVar[AdvancedSettings.ErrorType]
    kError: AdvancedSettings.ErrorType
    kWarn: AdvancedSettings.ErrorType
    kIgnore: AdvancedSettings.ErrorType
    MISSING_DB_BACKUP_STATUS_FIELD_NUMBER: _ClassVar[int]
    REPORT_ALL_NON_AUTOPROTECT_DB_ERRORS_FIELD_NUMBER: _ClassVar[int]
    OFFLINE_RESTORING_DB_BACKUP_STATUS_FIELD_NUMBER: _ClassVar[int]
    CLONED_DB_BACKUP_STATUS_FIELD_NUMBER: _ClassVar[int]
    DB_BACKUP_IF_NOT_ONLINE_STATUS_FIELD_NUMBER: _ClassVar[int]
    READ_ONLY_DB_BACKUP_STATUS_FIELD_NUMBER: _ClassVar[int]
    missing_db_backup_status: AdvancedSettings.ErrorType
    report_all_non_autoprotect_db_errors: AdvancedSettings.ErrorType
    offline_restoring_db_backup_status: AdvancedSettings.ErrorType
    cloned_db_backup_status: AdvancedSettings.ErrorType
    db_backup_if_not_online_status: AdvancedSettings.ErrorType
    read_only_db_backup_status: AdvancedSettings.ErrorType
    def __init__(self, missing_db_backup_status: _Optional[_Union[AdvancedSettings.ErrorType, str]] = ..., report_all_non_autoprotect_db_errors: _Optional[_Union[AdvancedSettings.ErrorType, str]] = ..., offline_restoring_db_backup_status: _Optional[_Union[AdvancedSettings.ErrorType, str]] = ..., cloned_db_backup_status: _Optional[_Union[AdvancedSettings.ErrorType, str]] = ..., db_backup_if_not_online_status: _Optional[_Union[AdvancedSettings.ErrorType, str]] = ..., read_only_db_backup_status: _Optional[_Union[AdvancedSettings.ErrorType, str]] = ...) -> None: ...

class AAGDatabaseCopyInfo(_message.Message):
    __slots__ = ("database_name", "instance_name", "sql_id", "host_entity_id")
    DATABASE_NAME_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_NAME_FIELD_NUMBER: _ClassVar[int]
    SQL_ID_FIELD_NUMBER: _ClassVar[int]
    HOST_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    database_name: str
    instance_name: str
    sql_id: SqlId
    host_entity_id: int
    def __init__(self, database_name: _Optional[str] = ..., instance_name: _Optional[str] = ..., sql_id: _Optional[_Union[SqlId, _Mapping]] = ..., host_entity_id: _Optional[int] = ...) -> None: ...
