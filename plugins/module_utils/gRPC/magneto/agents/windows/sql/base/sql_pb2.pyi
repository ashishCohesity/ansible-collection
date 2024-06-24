from magneto.agents.base import agent_pb2 as _agent_pb2
from magneto.agents.base import error_pb2 as _error_pb2
from magneto.agents.stub import agent_param_pb2 as _agent_param_pb2
from magneto.agents.windows.base import vss_pb2 as _vss_pb2
from magneto.base.entities import sql_pb2 as _sql_pb2
from magneto.connectors.sql import sql_pb2 as _sql_pb2_1
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AuthType(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kAdBased: _ClassVar[AuthType.Type]
        kDbBased: _ClassVar[AuthType.Type]
    kAdBased: AuthType.Type
    kDbBased: AuthType.Type
    def __init__(self) -> None: ...

class SQLDatabaseInfo(_message.Message):
    __slots__ = ("id", "instance_name", "database_name", "backupset_row_info_vec", "recovery_model", "state", "state_description", "is_available_for_vss_backup", "ldf_size_bytes", "total_size_bytes", "create_date", "file_vec", "file_vec_error", "vdi_snapshot_metadata", "database_recovery_status", "database_owner", "file_group_info_vec", "compatibility_level", "read_only", "is_database_cloned", "is_fci_database", "has_files_on_external_storage", "usage_size_bytes", "auth_type", "username", "password", "encrypted_password", "is_encrypted")
    ID_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_NAME_FIELD_NUMBER: _ClassVar[int]
    DATABASE_NAME_FIELD_NUMBER: _ClassVar[int]
    BACKUPSET_ROW_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    RECOVERY_MODEL_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    STATE_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    IS_AVAILABLE_FOR_VSS_BACKUP_FIELD_NUMBER: _ClassVar[int]
    LDF_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    CREATE_DATE_FIELD_NUMBER: _ClassVar[int]
    FILE_VEC_FIELD_NUMBER: _ClassVar[int]
    FILE_VEC_ERROR_FIELD_NUMBER: _ClassVar[int]
    VDI_SNAPSHOT_METADATA_FIELD_NUMBER: _ClassVar[int]
    DATABASE_RECOVERY_STATUS_FIELD_NUMBER: _ClassVar[int]
    DATABASE_OWNER_FIELD_NUMBER: _ClassVar[int]
    FILE_GROUP_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    COMPATIBILITY_LEVEL_FIELD_NUMBER: _ClassVar[int]
    READ_ONLY_FIELD_NUMBER: _ClassVar[int]
    IS_DATABASE_CLONED_FIELD_NUMBER: _ClassVar[int]
    IS_FCI_DATABASE_FIELD_NUMBER: _ClassVar[int]
    HAS_FILES_ON_EXTERNAL_STORAGE_FIELD_NUMBER: _ClassVar[int]
    USAGE_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    AUTH_TYPE_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTED_PASSWORD_FIELD_NUMBER: _ClassVar[int]
    IS_ENCRYPTED_FIELD_NUMBER: _ClassVar[int]
    id: _sql_pb2.SqlId
    instance_name: bytes
    database_name: bytes
    backupset_row_info_vec: _containers.RepeatedCompositeFieldContainer[_sql_pb2_1.BackupSetRowInfo]
    recovery_model: _sql_pb2.RecoveryModel.Type
    state: _sql_pb2.SQLDatabaseState.Type
    state_description: str
    is_available_for_vss_backup: bool
    ldf_size_bytes: int
    total_size_bytes: int
    create_date: str
    file_vec: _containers.RepeatedCompositeFieldContainer[_sql_pb2_1.SQLDatabaseFileInfo]
    file_vec_error: _error_pb2.ErrorProto
    vdi_snapshot_metadata: bytes
    database_recovery_status: _sql_pb2_1.DatabaseRecoveryStatus
    database_owner: str
    file_group_info_vec: _containers.RepeatedCompositeFieldContainer[_sql_pb2.SQLDatabaseFileGroupInfo]
    compatibility_level: int
    read_only: bool
    is_database_cloned: bool
    is_fci_database: bool
    has_files_on_external_storage: bool
    usage_size_bytes: int
    auth_type: AuthType.Type
    username: str
    password: str
    encrypted_password: bytes
    is_encrypted: bool
    def __init__(self, id: _Optional[_Union[_sql_pb2.SqlId, _Mapping]] = ..., instance_name: _Optional[bytes] = ..., database_name: _Optional[bytes] = ..., backupset_row_info_vec: _Optional[_Iterable[_Union[_sql_pb2_1.BackupSetRowInfo, _Mapping]]] = ..., recovery_model: _Optional[_Union[_sql_pb2.RecoveryModel.Type, str]] = ..., state: _Optional[_Union[_sql_pb2.SQLDatabaseState.Type, str]] = ..., state_description: _Optional[str] = ..., is_available_for_vss_backup: bool = ..., ldf_size_bytes: _Optional[int] = ..., total_size_bytes: _Optional[int] = ..., create_date: _Optional[str] = ..., file_vec: _Optional[_Iterable[_Union[_sql_pb2_1.SQLDatabaseFileInfo, _Mapping]]] = ..., file_vec_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., vdi_snapshot_metadata: _Optional[bytes] = ..., database_recovery_status: _Optional[_Union[_sql_pb2_1.DatabaseRecoveryStatus, _Mapping]] = ..., database_owner: _Optional[str] = ..., file_group_info_vec: _Optional[_Iterable[_Union[_sql_pb2.SQLDatabaseFileGroupInfo, _Mapping]]] = ..., compatibility_level: _Optional[int] = ..., read_only: bool = ..., is_database_cloned: bool = ..., is_fci_database: bool = ..., has_files_on_external_storage: bool = ..., usage_size_bytes: _Optional[int] = ..., auth_type: _Optional[_Union[AuthType.Type, str]] = ..., username: _Optional[str] = ..., password: _Optional[str] = ..., encrypted_password: _Optional[bytes] = ..., is_encrypted: bool = ...) -> None: ...

class DatabaseRestoreSpec(_message.Message):
    __slots__ = ("sql_id", "instance_name", "database_name", "resolve_db_name_conflict", "grant_full_control_to_these_users", "use_vdi_snapshot", "with_recovery", "no_file_copy", "keep_cdc", "is_pit_restore")
    SQL_ID_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_NAME_FIELD_NUMBER: _ClassVar[int]
    DATABASE_NAME_FIELD_NUMBER: _ClassVar[int]
    RESOLVE_DB_NAME_CONFLICT_FIELD_NUMBER: _ClassVar[int]
    GRANT_FULL_CONTROL_TO_THESE_USERS_FIELD_NUMBER: _ClassVar[int]
    USE_VDI_SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    WITH_RECOVERY_FIELD_NUMBER: _ClassVar[int]
    NO_FILE_COPY_FIELD_NUMBER: _ClassVar[int]
    KEEP_CDC_FIELD_NUMBER: _ClassVar[int]
    IS_PIT_RESTORE_FIELD_NUMBER: _ClassVar[int]
    sql_id: _sql_pb2.SqlId
    instance_name: str
    database_name: str
    resolve_db_name_conflict: bool
    grant_full_control_to_these_users: _containers.RepeatedScalarFieldContainer[str]
    use_vdi_snapshot: bool
    with_recovery: bool
    no_file_copy: bool
    keep_cdc: bool
    is_pit_restore: bool
    def __init__(self, sql_id: _Optional[_Union[_sql_pb2.SqlId, _Mapping]] = ..., instance_name: _Optional[str] = ..., database_name: _Optional[str] = ..., resolve_db_name_conflict: bool = ..., grant_full_control_to_these_users: _Optional[_Iterable[str]] = ..., use_vdi_snapshot: bool = ..., with_recovery: bool = ..., no_file_copy: bool = ..., keep_cdc: bool = ..., is_pit_restore: bool = ...) -> None: ...

class SQLFileCopyInstructionFilter(_message.Message):
    __slots__ = ("db_file_type_vec",)
    DB_FILE_COPY_INSTRUCTION_FIELD_NUMBER: _ClassVar[int]
    db_file_copy_instruction: _descriptor.FieldDescriptor
    DB_FILE_TYPE_VEC_FIELD_NUMBER: _ClassVar[int]
    db_file_type_vec: _containers.RepeatedScalarFieldContainer[_sql_pb2_1.DBFileType.Type]
    def __init__(self, db_file_type_vec: _Optional[_Iterable[_Union[_sql_pb2_1.DBFileType.Type, str]]] = ...) -> None: ...

class RestorePolicy(_message.Message):
    __slots__ = ("database_vec", "all_databases_with_recovery", "attach_deprecated", "vdi_snapshot")
    class Database(_message.Message):
        __slots__ = ("database_spec", "copy_instruction_vec", "with_recovery", "db_restore_overwrite_policy")
        DATABASE_SPEC_FIELD_NUMBER: _ClassVar[int]
        COPY_INSTRUCTION_VEC_FIELD_NUMBER: _ClassVar[int]
        WITH_RECOVERY_FIELD_NUMBER: _ClassVar[int]
        DB_RESTORE_OVERWRITE_POLICY_FIELD_NUMBER: _ClassVar[int]
        database_spec: DatabaseRestoreSpec
        copy_instruction_vec: _containers.RepeatedCompositeFieldContainer[_vss_pb2.VSSFileCopyInstruction]
        with_recovery: bool
        db_restore_overwrite_policy: _sql_pb2.DBRestoreOverwritePolicy.Type
        def __init__(self, database_spec: _Optional[_Union[DatabaseRestoreSpec, _Mapping]] = ..., copy_instruction_vec: _Optional[_Iterable[_Union[_vss_pb2.VSSFileCopyInstruction, _Mapping]]] = ..., with_recovery: bool = ..., db_restore_overwrite_policy: _Optional[_Union[_sql_pb2.DBRestoreOverwritePolicy.Type, str]] = ...) -> None: ...
    DATABASE_VEC_FIELD_NUMBER: _ClassVar[int]
    ALL_DATABASES_WITH_RECOVERY_FIELD_NUMBER: _ClassVar[int]
    ATTACH_DEPRECATED_FIELD_NUMBER: _ClassVar[int]
    VDI_SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    database_vec: _containers.RepeatedCompositeFieldContainer[RestorePolicy.Database]
    all_databases_with_recovery: bool
    attach_deprecated: bool
    vdi_snapshot: bool
    def __init__(self, database_vec: _Optional[_Iterable[_Union[RestorePolicy.Database, _Mapping]]] = ..., all_databases_with_recovery: bool = ..., attach_deprecated: bool = ..., vdi_snapshot: bool = ...) -> None: ...

class SQLVSSRestoreProgress(_message.Message):
    __slots__ = ("database_vec", "finished", "restore_error")
    class Database(_message.Message):
        __slots__ = ("sql_id", "database_name", "original_sql_id", "num_files", "num_files_processed", "num_bytes", "num_bytes_processed", "finished")
        SQL_ID_FIELD_NUMBER: _ClassVar[int]
        DATABASE_NAME_FIELD_NUMBER: _ClassVar[int]
        ORIGINAL_SQL_ID_FIELD_NUMBER: _ClassVar[int]
        NUM_FILES_FIELD_NUMBER: _ClassVar[int]
        NUM_FILES_PROCESSED_FIELD_NUMBER: _ClassVar[int]
        NUM_BYTES_FIELD_NUMBER: _ClassVar[int]
        NUM_BYTES_PROCESSED_FIELD_NUMBER: _ClassVar[int]
        FINISHED_FIELD_NUMBER: _ClassVar[int]
        sql_id: _sql_pb2.SqlId
        database_name: str
        original_sql_id: _sql_pb2.SqlId
        num_files: int
        num_files_processed: int
        num_bytes: int
        num_bytes_processed: int
        finished: bool
        def __init__(self, sql_id: _Optional[_Union[_sql_pb2.SqlId, _Mapping]] = ..., database_name: _Optional[str] = ..., original_sql_id: _Optional[_Union[_sql_pb2.SqlId, _Mapping]] = ..., num_files: _Optional[int] = ..., num_files_processed: _Optional[int] = ..., num_bytes: _Optional[int] = ..., num_bytes_processed: _Optional[int] = ..., finished: bool = ...) -> None: ...
    DATABASE_VEC_FIELD_NUMBER: _ClassVar[int]
    FINISHED_FIELD_NUMBER: _ClassVar[int]
    RESTORE_ERROR_FIELD_NUMBER: _ClassVar[int]
    database_vec: _containers.RepeatedCompositeFieldContainer[SQLVSSRestoreProgress.Database]
    finished: bool
    restore_error: _error_pb2.ErrorProto
    def __init__(self, database_vec: _Optional[_Iterable[_Union[SQLVSSRestoreProgress.Database, _Mapping]]] = ..., finished: bool = ..., restore_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class SQLParams(_message.Message):
    __slots__ = ("populate_sql_info", "database_id_vec", "track_file_cbt", "use_vdi_snapshot")
    POPULATE_SQL_INFO_FIELD_NUMBER: _ClassVar[int]
    DATABASE_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    TRACK_FILE_CBT_FIELD_NUMBER: _ClassVar[int]
    USE_VDI_SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    populate_sql_info: bool
    database_id_vec: _containers.RepeatedCompositeFieldContainer[_sql_pb2.SqlId]
    track_file_cbt: bool
    use_vdi_snapshot: bool
    def __init__(self, populate_sql_info: bool = ..., database_id_vec: _Optional[_Iterable[_Union[_sql_pb2.SqlId, _Mapping]]] = ..., track_file_cbt: bool = ..., use_vdi_snapshot: bool = ...) -> None: ...

class VSSBackupInfo(_message.Message):
    __slots__ = ("db_info_vec", "sql_instance_vec")
    VSS_BACKUP_INFO_FIELD_NUMBER: _ClassVar[int]
    vss_backup_info: _descriptor.FieldDescriptor
    DB_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    SQL_INSTANCE_VEC_FIELD_NUMBER: _ClassVar[int]
    db_info_vec: _containers.RepeatedCompositeFieldContainer[SQLDatabaseInfo]
    sql_instance_vec: _containers.RepeatedCompositeFieldContainer[_sql_pb2.SQLInstanceInfo]
    def __init__(self, db_info_vec: _Optional[_Iterable[_Union[SQLDatabaseInfo, _Mapping]]] = ..., sql_instance_vec: _Optional[_Iterable[_Union[_sql_pb2.SQLInstanceInfo, _Mapping]]] = ...) -> None: ...

class AAGInfoResult(_message.Message):
    __slots__ = ("aag_info", "error")
    AAG_INFO_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    aag_info: _sql_pb2.AAGInfo
    error: _error_pb2.ErrorProto
    def __init__(self, aag_info: _Optional[_Union[_sql_pb2.AAGInfo, _Mapping]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class SQLFileInfoFromVSSSnapshot(_message.Message):
    __slots__ = ("full_filepath", "filename", "snapshot_path", "snapshot_file_size_bytes")
    FULL_FILEPATH_FIELD_NUMBER: _ClassVar[int]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_PATH_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_FILE_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    full_filepath: bytes
    filename: bytes
    snapshot_path: str
    snapshot_file_size_bytes: int
    def __init__(self, full_filepath: _Optional[bytes] = ..., filename: _Optional[bytes] = ..., snapshot_path: _Optional[str] = ..., snapshot_file_size_bytes: _Optional[int] = ...) -> None: ...

class SQLAppFileInfo(_message.Message):
    __slots__ = ("xxx_db_info_deprecated", "database_vec")
    class DatabaseAppFileInfo(_message.Message):
        __slots__ = ("db_info", "file_snapshot_info_vec")
        DB_INFO_FIELD_NUMBER: _ClassVar[int]
        FILE_SNAPSHOT_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
        db_info: SQLDatabaseInfo
        file_snapshot_info_vec: _containers.RepeatedCompositeFieldContainer[SQLFileInfoFromVSSSnapshot]
        def __init__(self, db_info: _Optional[_Union[SQLDatabaseInfo, _Mapping]] = ..., file_snapshot_info_vec: _Optional[_Iterable[_Union[SQLFileInfoFromVSSSnapshot, _Mapping]]] = ...) -> None: ...
    APP_FILE_INFO_FIELD_NUMBER: _ClassVar[int]
    app_file_info: _descriptor.FieldDescriptor
    XXX_DB_INFO_DEPRECATED_FIELD_NUMBER: _ClassVar[int]
    DATABASE_VEC_FIELD_NUMBER: _ClassVar[int]
    xxx_db_info_deprecated: _containers.RepeatedCompositeFieldContainer[SQLDatabaseInfo]
    database_vec: _containers.RepeatedCompositeFieldContainer[SQLAppFileInfo.DatabaseAppFileInfo]
    def __init__(self, xxx_db_info_deprecated: _Optional[_Iterable[_Union[SQLDatabaseInfo, _Mapping]]] = ..., database_vec: _Optional[_Iterable[_Union[SQLAppFileInfo.DatabaseAppFileInfo, _Mapping]]] = ...) -> None: ...

class SQLTopologyNode(_message.Message):
    __slots__ = ("sql_instance_vec", "aag_info")
    SQL_TOPOLOGY_NODE_FIELD_NUMBER: _ClassVar[int]
    sql_topology_node: _descriptor.FieldDescriptor
    SQL_INSTANCE_VEC_FIELD_NUMBER: _ClassVar[int]
    AAG_INFO_FIELD_NUMBER: _ClassVar[int]
    sql_instance_vec: _containers.RepeatedCompositeFieldContainer[_sql_pb2.SQLInstanceInfo]
    aag_info: _sql_pb2.AAGInfo
    def __init__(self, sql_instance_vec: _Optional[_Iterable[_Union[_sql_pb2.SQLInstanceInfo, _Mapping]]] = ..., aag_info: _Optional[_Union[_sql_pb2.AAGInfo, _Mapping]] = ...) -> None: ...

class GetSQLTopologyArg(_message.Message):
    __slots__ = ("include_databases", "allow_fqdn_generation")
    GET_SQL_TOPOLOGY_ARG_FIELD_NUMBER: _ClassVar[int]
    get_sql_topology_arg: _descriptor.FieldDescriptor
    INCLUDE_DATABASES_FIELD_NUMBER: _ClassVar[int]
    ALLOW_FQDN_GENERATION_FIELD_NUMBER: _ClassVar[int]
    include_databases: bool
    allow_fqdn_generation: bool
    def __init__(self, include_databases: bool = ..., allow_fqdn_generation: bool = ...) -> None: ...
