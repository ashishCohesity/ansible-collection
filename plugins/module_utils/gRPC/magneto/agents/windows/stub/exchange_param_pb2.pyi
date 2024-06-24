from magneto.agents.base import error_pb2 as _error_pb2
from magneto.agents.windows.exchange import exchange_pb2 as _exchange_pb2
from magneto.base.entities import exchange_pb2 as _exchange_pb2_1
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetExchangeHierarchyArg(_message.Message):
    __slots__ = ("option_flags", "analyze_dbstatus_from_time_offset_sec", "analyze_dbstatus_to_time_offset_sec")
    class GetExchangeHierarchyOptionFlags(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNone: _ClassVar[GetExchangeHierarchyArg.GetExchangeHierarchyOptionFlags]
        kExcludeRecoveryDB: _ClassVar[GetExchangeHierarchyArg.GetExchangeHierarchyOptionFlags]
    kNone: GetExchangeHierarchyArg.GetExchangeHierarchyOptionFlags
    kExcludeRecoveryDB: GetExchangeHierarchyArg.GetExchangeHierarchyOptionFlags
    OPTION_FLAGS_FIELD_NUMBER: _ClassVar[int]
    ANALYZE_DBSTATUS_FROM_TIME_OFFSET_SEC_FIELD_NUMBER: _ClassVar[int]
    ANALYZE_DBSTATUS_TO_TIME_OFFSET_SEC_FIELD_NUMBER: _ClassVar[int]
    option_flags: int
    analyze_dbstatus_from_time_offset_sec: int
    analyze_dbstatus_to_time_offset_sec: int
    def __init__(self, option_flags: _Optional[int] = ..., analyze_dbstatus_from_time_offset_sec: _Optional[int] = ..., analyze_dbstatus_to_time_offset_sec: _Optional[int] = ...) -> None: ...

class GetExchangeHierarchyResult(_message.Message):
    __slots__ = ("exchange",)
    EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    exchange: _exchange_pb2_1.ExchangeTopology
    def __init__(self, exchange: _Optional[_Union[_exchange_pb2_1.ExchangeTopology, _Mapping]] = ...) -> None: ...

class GetExchangeDatabaseMailboxMetadataArg(_message.Message):
    __slots__ = ("db_guid_vec",)
    DB_GUID_VEC_FIELD_NUMBER: _ClassVar[int]
    db_guid_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, db_guid_vec: _Optional[_Iterable[str]] = ...) -> None: ...

class GetExchangeDatabaseMailboxMetadataResult(_message.Message):
    __slots__ = ("metadata_vec",)
    class MailboxMetadata(_message.Message):
        __slots__ = ("db_guid", "status", "mailbox_manifest")
        DB_GUID_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        MAILBOX_MANIFEST_FIELD_NUMBER: _ClassVar[int]
        db_guid: str
        status: _error_pb2.ErrorProto
        mailbox_manifest: _exchange_pb2_1.ExchangeDatabaseMailboxManifest
        def __init__(self, db_guid: _Optional[str] = ..., status: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., mailbox_manifest: _Optional[_Union[_exchange_pb2_1.ExchangeDatabaseMailboxManifest, _Mapping]] = ...) -> None: ...
    METADATA_VEC_FIELD_NUMBER: _ClassVar[int]
    metadata_vec: _containers.RepeatedCompositeFieldContainer[GetExchangeDatabaseMailboxMetadataResult.MailboxMetadata]
    def __init__(self, metadata_vec: _Optional[_Iterable[_Union[GetExchangeDatabaseMailboxMetadataResult.MailboxMetadata, _Mapping]]] = ...) -> None: ...

class ValidateExchangeDatabaseRestoreArg(_message.Message):
    __slots__ = ("dest_db_name", "option_flags", "source_exchange_org", "source_exchange_major_ver", "source_exchange_minor_ver", "dest_edb_filepath", "dest_log_dirpath", "source_edb_size", "source_log_size", "check_log_start", "db_id", "log_file_prefix")
    class ValidateExchangeDBOptionFlags(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNone: _ClassVar[ValidateExchangeDatabaseRestoreArg.ValidateExchangeDBOptionFlags]
        kRecoveryDB: _ClassVar[ValidateExchangeDatabaseRestoreArg.ValidateExchangeDBOptionFlags]
        kPublicFolderDB: _ClassVar[ValidateExchangeDatabaseRestoreArg.ValidateExchangeDBOptionFlags]
        kCheckLogIntegrity: _ClassVar[ValidateExchangeDatabaseRestoreArg.ValidateExchangeDBOptionFlags]
    kNone: ValidateExchangeDatabaseRestoreArg.ValidateExchangeDBOptionFlags
    kRecoveryDB: ValidateExchangeDatabaseRestoreArg.ValidateExchangeDBOptionFlags
    kPublicFolderDB: ValidateExchangeDatabaseRestoreArg.ValidateExchangeDBOptionFlags
    kCheckLogIntegrity: ValidateExchangeDatabaseRestoreArg.ValidateExchangeDBOptionFlags
    DEST_DB_NAME_FIELD_NUMBER: _ClassVar[int]
    OPTION_FLAGS_FIELD_NUMBER: _ClassVar[int]
    SOURCE_EXCHANGE_ORG_FIELD_NUMBER: _ClassVar[int]
    SOURCE_EXCHANGE_MAJOR_VER_FIELD_NUMBER: _ClassVar[int]
    SOURCE_EXCHANGE_MINOR_VER_FIELD_NUMBER: _ClassVar[int]
    DEST_EDB_FILEPATH_FIELD_NUMBER: _ClassVar[int]
    DEST_LOG_DIRPATH_FIELD_NUMBER: _ClassVar[int]
    SOURCE_EDB_SIZE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_LOG_SIZE_FIELD_NUMBER: _ClassVar[int]
    CHECK_LOG_START_FIELD_NUMBER: _ClassVar[int]
    DB_ID_FIELD_NUMBER: _ClassVar[int]
    LOG_FILE_PREFIX_FIELD_NUMBER: _ClassVar[int]
    dest_db_name: str
    option_flags: int
    source_exchange_org: str
    source_exchange_major_ver: int
    source_exchange_minor_ver: int
    dest_edb_filepath: str
    dest_log_dirpath: str
    source_edb_size: int
    source_log_size: int
    check_log_start: int
    db_id: int
    log_file_prefix: str
    def __init__(self, dest_db_name: _Optional[str] = ..., option_flags: _Optional[int] = ..., source_exchange_org: _Optional[str] = ..., source_exchange_major_ver: _Optional[int] = ..., source_exchange_minor_ver: _Optional[int] = ..., dest_edb_filepath: _Optional[str] = ..., dest_log_dirpath: _Optional[str] = ..., source_edb_size: _Optional[int] = ..., source_log_size: _Optional[int] = ..., check_log_start: _Optional[int] = ..., db_id: _Optional[int] = ..., log_file_prefix: _Optional[str] = ...) -> None: ...

class ValidateExchangeDatabaseRestoreResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CreateExchangeDatabaseArg(_message.Message):
    __slots__ = ("db_name", "option_flags", "dest_edb_filepath", "dest_log_dirpath", "db_id")
    class CreateExchangeDBOptionFlags(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNone: _ClassVar[CreateExchangeDatabaseArg.CreateExchangeDBOptionFlags]
        kRecoveryDB: _ClassVar[CreateExchangeDatabaseArg.CreateExchangeDBOptionFlags]
        kPublicFolderDB: _ClassVar[CreateExchangeDatabaseArg.CreateExchangeDBOptionFlags]
        kAllowFileRestore: _ClassVar[CreateExchangeDatabaseArg.CreateExchangeDBOptionFlags]
        kRestartMSExchangeStoreService: _ClassVar[CreateExchangeDatabaseArg.CreateExchangeDBOptionFlags]
        kMountAfterCreate: _ClassVar[CreateExchangeDatabaseArg.CreateExchangeDBOptionFlags]
        kCircularLogging: _ClassVar[CreateExchangeDatabaseArg.CreateExchangeDBOptionFlags]
        kDisableIndexing: _ClassVar[CreateExchangeDatabaseArg.CreateExchangeDBOptionFlags]
    kNone: CreateExchangeDatabaseArg.CreateExchangeDBOptionFlags
    kRecoveryDB: CreateExchangeDatabaseArg.CreateExchangeDBOptionFlags
    kPublicFolderDB: CreateExchangeDatabaseArg.CreateExchangeDBOptionFlags
    kAllowFileRestore: CreateExchangeDatabaseArg.CreateExchangeDBOptionFlags
    kRestartMSExchangeStoreService: CreateExchangeDatabaseArg.CreateExchangeDBOptionFlags
    kMountAfterCreate: CreateExchangeDatabaseArg.CreateExchangeDBOptionFlags
    kCircularLogging: CreateExchangeDatabaseArg.CreateExchangeDBOptionFlags
    kDisableIndexing: CreateExchangeDatabaseArg.CreateExchangeDBOptionFlags
    DB_NAME_FIELD_NUMBER: _ClassVar[int]
    OPTION_FLAGS_FIELD_NUMBER: _ClassVar[int]
    DEST_EDB_FILEPATH_FIELD_NUMBER: _ClassVar[int]
    DEST_LOG_DIRPATH_FIELD_NUMBER: _ClassVar[int]
    DB_ID_FIELD_NUMBER: _ClassVar[int]
    db_name: str
    option_flags: int
    dest_edb_filepath: str
    dest_log_dirpath: str
    db_id: int
    def __init__(self, db_name: _Optional[str] = ..., option_flags: _Optional[int] = ..., dest_edb_filepath: _Optional[str] = ..., dest_log_dirpath: _Optional[str] = ..., db_id: _Optional[int] = ...) -> None: ...

class CreateExchangeDatabaseResult(_message.Message):
    __slots__ = ("db_guid",)
    DB_GUID_FIELD_NUMBER: _ClassVar[int]
    db_guid: str
    def __init__(self, db_guid: _Optional[str] = ...) -> None: ...

class MountOrUnmountExchangeDatabaseArg(_message.Message):
    __slots__ = ("db_guid", "unmount_db", "option_flags", "src_edb_filepath", "dest_edb_filepath", "dest_log_dirpath", "delete_older_than_log_number", "db_id", "log_file_prefix")
    class MountUnmountOptionFlags(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNone: _ClassVar[MountOrUnmountExchangeDatabaseArg.MountUnmountOptionFlags]
        kEmptyLogPath: _ClassVar[MountOrUnmountExchangeDatabaseArg.MountUnmountOptionFlags]
        kDeleteOldLogs: _ClassVar[MountOrUnmountExchangeDatabaseArg.MountUnmountOptionFlags]
        kRestartISSvc: _ClassVar[MountOrUnmountExchangeDatabaseArg.MountUnmountOptionFlags]
        kPrepareForMount: _ClassVar[MountOrUnmountExchangeDatabaseArg.MountUnmountOptionFlags]
    kNone: MountOrUnmountExchangeDatabaseArg.MountUnmountOptionFlags
    kEmptyLogPath: MountOrUnmountExchangeDatabaseArg.MountUnmountOptionFlags
    kDeleteOldLogs: MountOrUnmountExchangeDatabaseArg.MountUnmountOptionFlags
    kRestartISSvc: MountOrUnmountExchangeDatabaseArg.MountUnmountOptionFlags
    kPrepareForMount: MountOrUnmountExchangeDatabaseArg.MountUnmountOptionFlags
    DB_GUID_FIELD_NUMBER: _ClassVar[int]
    UNMOUNT_DB_FIELD_NUMBER: _ClassVar[int]
    OPTION_FLAGS_FIELD_NUMBER: _ClassVar[int]
    SRC_EDB_FILEPATH_FIELD_NUMBER: _ClassVar[int]
    DEST_EDB_FILEPATH_FIELD_NUMBER: _ClassVar[int]
    DEST_LOG_DIRPATH_FIELD_NUMBER: _ClassVar[int]
    DELETE_OLDER_THAN_LOG_NUMBER_FIELD_NUMBER: _ClassVar[int]
    DB_ID_FIELD_NUMBER: _ClassVar[int]
    LOG_FILE_PREFIX_FIELD_NUMBER: _ClassVar[int]
    db_guid: str
    unmount_db: bool
    option_flags: int
    src_edb_filepath: str
    dest_edb_filepath: str
    dest_log_dirpath: str
    delete_older_than_log_number: int
    db_id: int
    log_file_prefix: str
    def __init__(self, db_guid: _Optional[str] = ..., unmount_db: bool = ..., option_flags: _Optional[int] = ..., src_edb_filepath: _Optional[str] = ..., dest_edb_filepath: _Optional[str] = ..., dest_log_dirpath: _Optional[str] = ..., delete_older_than_log_number: _Optional[int] = ..., db_id: _Optional[int] = ..., log_file_prefix: _Optional[str] = ...) -> None: ...

class MountOrUnmountExchangeDatabaseResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteExchangeDatabaseArg(_message.Message):
    __slots__ = ("db_guid", "option_flags", "db_id")
    class DeleteExchangeDBOptionFlags(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNone: _ClassVar[DeleteExchangeDatabaseArg.DeleteExchangeDBOptionFlags]
        kDeleteFiles: _ClassVar[DeleteExchangeDatabaseArg.DeleteExchangeDBOptionFlags]
    kNone: DeleteExchangeDatabaseArg.DeleteExchangeDBOptionFlags
    kDeleteFiles: DeleteExchangeDatabaseArg.DeleteExchangeDBOptionFlags
    DB_GUID_FIELD_NUMBER: _ClassVar[int]
    OPTION_FLAGS_FIELD_NUMBER: _ClassVar[int]
    DB_ID_FIELD_NUMBER: _ClassVar[int]
    db_guid: str
    option_flags: int
    db_id: int
    def __init__(self, db_guid: _Optional[str] = ..., option_flags: _Optional[int] = ..., db_id: _Optional[int] = ...) -> None: ...

class DeleteExchangeDatabaseResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PlayLogsOnExchangeEDBArg(_message.Message):
    __slots__ = ("edb_filepath", "log_dirpath", "option_flags", "db_id", "log_file_prefix")
    class PlayLogsOnExchangeEDBOptionFlags(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNone: _ClassVar[PlayLogsOnExchangeEDBArg.PlayLogsOnExchangeEDBOptionFlags]
    kNone: PlayLogsOnExchangeEDBArg.PlayLogsOnExchangeEDBOptionFlags
    EDB_FILEPATH_FIELD_NUMBER: _ClassVar[int]
    LOG_DIRPATH_FIELD_NUMBER: _ClassVar[int]
    OPTION_FLAGS_FIELD_NUMBER: _ClassVar[int]
    DB_ID_FIELD_NUMBER: _ClassVar[int]
    LOG_FILE_PREFIX_FIELD_NUMBER: _ClassVar[int]
    edb_filepath: str
    log_dirpath: str
    option_flags: int
    db_id: int
    log_file_prefix: str
    def __init__(self, edb_filepath: _Optional[str] = ..., log_dirpath: _Optional[str] = ..., option_flags: _Optional[int] = ..., db_id: _Optional[int] = ..., log_file_prefix: _Optional[str] = ...) -> None: ...

class PlayLogsOnExchangeEDBResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class MoveExchangeMailboxProcessingArg(_message.Message):
    __slots__ = ("source_db_guid", "dest_db_guid", "retry_queue", "db_id")
    SOURCE_DB_GUID_FIELD_NUMBER: _ClassVar[int]
    DEST_DB_GUID_FIELD_NUMBER: _ClassVar[int]
    RETRY_QUEUE_FIELD_NUMBER: _ClassVar[int]
    DB_ID_FIELD_NUMBER: _ClassVar[int]
    source_db_guid: str
    dest_db_guid: str
    retry_queue: bool
    db_id: int
    def __init__(self, source_db_guid: _Optional[str] = ..., dest_db_guid: _Optional[str] = ..., retry_queue: bool = ..., db_id: _Optional[int] = ...) -> None: ...

class MoveExchangeMailboxProcessingResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PrepareExchangeDBRestoreArg(_message.Message):
    __slots__ = ("prepare_action", "db_guid", "db_name", "option_flags", "src_edb_filepath", "dest_edb_filepath", "dest_log_dirpath", "delete_older_than_log_number", "source_db_guid", "dest_db_guid", "retry_queue", "db_id", "log_file_prefix")
    class PrepareActionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kCreateDB: _ClassVar[PrepareExchangeDBRestoreArg.PrepareActionType]
        kMountDB: _ClassVar[PrepareExchangeDBRestoreArg.PrepareActionType]
        kUnmountDB: _ClassVar[PrepareExchangeDBRestoreArg.PrepareActionType]
        kRestartIS: _ClassVar[PrepareExchangeDBRestoreArg.PrepareActionType]
    kCreateDB: PrepareExchangeDBRestoreArg.PrepareActionType
    kMountDB: PrepareExchangeDBRestoreArg.PrepareActionType
    kUnmountDB: PrepareExchangeDBRestoreArg.PrepareActionType
    kRestartIS: PrepareExchangeDBRestoreArg.PrepareActionType
    class PrepareOptionFlags(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNone: _ClassVar[PrepareExchangeDBRestoreArg.PrepareOptionFlags]
        kRecoveryDB: _ClassVar[PrepareExchangeDBRestoreArg.PrepareOptionFlags]
        kPublicFolderDB: _ClassVar[PrepareExchangeDBRestoreArg.PrepareOptionFlags]
        kAllowFileRestore: _ClassVar[PrepareExchangeDBRestoreArg.PrepareOptionFlags]
        kRestartISSvc: _ClassVar[PrepareExchangeDBRestoreArg.PrepareOptionFlags]
        kMountAfterCreate: _ClassVar[PrepareExchangeDBRestoreArg.PrepareOptionFlags]
        kCircularLogging: _ClassVar[PrepareExchangeDBRestoreArg.PrepareOptionFlags]
        kDisableIndexing: _ClassVar[PrepareExchangeDBRestoreArg.PrepareOptionFlags]
        kDeleteOldLogs: _ClassVar[PrepareExchangeDBRestoreArg.PrepareOptionFlags]
        kEmptyLogPath: _ClassVar[PrepareExchangeDBRestoreArg.PrepareOptionFlags]
        kMoveMailboxProcessing: _ClassVar[PrepareExchangeDBRestoreArg.PrepareOptionFlags]
        kPrepareForMount: _ClassVar[PrepareExchangeDBRestoreArg.PrepareOptionFlags]
    kNone: PrepareExchangeDBRestoreArg.PrepareOptionFlags
    kRecoveryDB: PrepareExchangeDBRestoreArg.PrepareOptionFlags
    kPublicFolderDB: PrepareExchangeDBRestoreArg.PrepareOptionFlags
    kAllowFileRestore: PrepareExchangeDBRestoreArg.PrepareOptionFlags
    kRestartISSvc: PrepareExchangeDBRestoreArg.PrepareOptionFlags
    kMountAfterCreate: PrepareExchangeDBRestoreArg.PrepareOptionFlags
    kCircularLogging: PrepareExchangeDBRestoreArg.PrepareOptionFlags
    kDisableIndexing: PrepareExchangeDBRestoreArg.PrepareOptionFlags
    kDeleteOldLogs: PrepareExchangeDBRestoreArg.PrepareOptionFlags
    kEmptyLogPath: PrepareExchangeDBRestoreArg.PrepareOptionFlags
    kMoveMailboxProcessing: PrepareExchangeDBRestoreArg.PrepareOptionFlags
    kPrepareForMount: PrepareExchangeDBRestoreArg.PrepareOptionFlags
    PREPARE_ACTION_FIELD_NUMBER: _ClassVar[int]
    DB_GUID_FIELD_NUMBER: _ClassVar[int]
    DB_NAME_FIELD_NUMBER: _ClassVar[int]
    OPTION_FLAGS_FIELD_NUMBER: _ClassVar[int]
    SRC_EDB_FILEPATH_FIELD_NUMBER: _ClassVar[int]
    DEST_EDB_FILEPATH_FIELD_NUMBER: _ClassVar[int]
    DEST_LOG_DIRPATH_FIELD_NUMBER: _ClassVar[int]
    DELETE_OLDER_THAN_LOG_NUMBER_FIELD_NUMBER: _ClassVar[int]
    SOURCE_DB_GUID_FIELD_NUMBER: _ClassVar[int]
    DEST_DB_GUID_FIELD_NUMBER: _ClassVar[int]
    RETRY_QUEUE_FIELD_NUMBER: _ClassVar[int]
    DB_ID_FIELD_NUMBER: _ClassVar[int]
    LOG_FILE_PREFIX_FIELD_NUMBER: _ClassVar[int]
    prepare_action: PrepareExchangeDBRestoreArg.PrepareActionType
    db_guid: str
    db_name: str
    option_flags: int
    src_edb_filepath: str
    dest_edb_filepath: str
    dest_log_dirpath: str
    delete_older_than_log_number: int
    source_db_guid: str
    dest_db_guid: str
    retry_queue: bool
    db_id: int
    log_file_prefix: str
    def __init__(self, prepare_action: _Optional[_Union[PrepareExchangeDBRestoreArg.PrepareActionType, str]] = ..., db_guid: _Optional[str] = ..., db_name: _Optional[str] = ..., option_flags: _Optional[int] = ..., src_edb_filepath: _Optional[str] = ..., dest_edb_filepath: _Optional[str] = ..., dest_log_dirpath: _Optional[str] = ..., delete_older_than_log_number: _Optional[int] = ..., source_db_guid: _Optional[str] = ..., dest_db_guid: _Optional[str] = ..., retry_queue: bool = ..., db_id: _Optional[int] = ..., log_file_prefix: _Optional[str] = ...) -> None: ...

class PrepareExchangeDBRestoreResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetJobProgressArg(_message.Message):
    __slots__ = ("task_id", "db_id")
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    DB_ID_FIELD_NUMBER: _ClassVar[int]
    task_id: int
    db_id: int
    def __init__(self, task_id: _Optional[int] = ..., db_id: _Optional[int] = ...) -> None: ...

class GetJobProgressResult(_message.Message):
    __slots__ = ("job_state", "percent_complete")
    class ProgressState(_message.Message):
        __slots__ = ()
        class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kUnknown: _ClassVar[GetJobProgressResult.ProgressState.Type]
            kPending: _ClassVar[GetJobProgressResult.ProgressState.Type]
            kProgress: _ClassVar[GetJobProgressResult.ProgressState.Type]
            kCompleted: _ClassVar[GetJobProgressResult.ProgressState.Type]
        kUnknown: GetJobProgressResult.ProgressState.Type
        kPending: GetJobProgressResult.ProgressState.Type
        kProgress: GetJobProgressResult.ProgressState.Type
        kCompleted: GetJobProgressResult.ProgressState.Type
        def __init__(self) -> None: ...
    JOB_STATE_FIELD_NUMBER: _ClassVar[int]
    PERCENT_COMPLETE_FIELD_NUMBER: _ClassVar[int]
    job_state: GetJobProgressResult.ProgressState.Type
    percent_complete: float
    def __init__(self, job_state: _Optional[_Union[GetJobProgressResult.ProgressState.Type, str]] = ..., percent_complete: _Optional[float] = ...) -> None: ...

class GetJobOutputArg(_message.Message):
    __slots__ = ("task_id", "db_id")
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    DB_ID_FIELD_NUMBER: _ClassVar[int]
    task_id: int
    db_id: int
    def __init__(self, task_id: _Optional[int] = ..., db_id: _Optional[int] = ...) -> None: ...

class GetJobOutputResult(_message.Message):
    __slots__ = ("op_error", "db_guid")
    OP_ERROR_FIELD_NUMBER: _ClassVar[int]
    DB_GUID_FIELD_NUMBER: _ClassVar[int]
    op_error: _error_pb2.ErrorProto
    db_guid: str
    def __init__(self, op_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., db_guid: _Optional[str] = ...) -> None: ...

class CancelJobArg(_message.Message):
    __slots__ = ("task_id", "db_id")
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    DB_ID_FIELD_NUMBER: _ClassVar[int]
    task_id: int
    db_id: int
    def __init__(self, task_id: _Optional[int] = ..., db_id: _Optional[int] = ...) -> None: ...

class CancelJobResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CleanupJobArg(_message.Message):
    __slots__ = ("task_id", "db_id", "cancel")
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    DB_ID_FIELD_NUMBER: _ClassVar[int]
    CANCEL_FIELD_NUMBER: _ClassVar[int]
    task_id: int
    db_id: int
    cancel: bool
    def __init__(self, task_id: _Optional[int] = ..., db_id: _Optional[int] = ..., cancel: bool = ...) -> None: ...

class CleanupJobResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class FolderType(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kEmailMessages: _ClassVar[FolderType.Type]
        kCalendar: _ClassVar[FolderType.Type]
        kContacts: _ClassVar[FolderType.Type]
        kSearch: _ClassVar[FolderType.Type]
        kTasks: _ClassVar[FolderType.Type]
        kFolder: _ClassVar[FolderType.Type]
    kEmailMessages: FolderType.Type
    kCalendar: FolderType.Type
    kContacts: FolderType.Type
    kSearch: FolderType.Type
    kTasks: FolderType.Type
    kFolder: FolderType.Type
    def __init__(self) -> None: ...

class PstConvertFolderConfig(_message.Message):
    __slots__ = ("folder_name", "folder_type")
    FOLDER_NAME_FIELD_NUMBER: _ClassVar[int]
    FOLDER_TYPE_FIELD_NUMBER: _ClassVar[int]
    folder_name: str
    folder_type: FolderType.Type
    def __init__(self, folder_name: _Optional[str] = ..., folder_type: _Optional[_Union[FolderType.Type, str]] = ...) -> None: ...

class EwsToPstConversionParams(_message.Message):
    __slots__ = ("create_pst", "pst_name_prefix", "pst_password", "pst_size_threshold", "option_flags", "encrypted_pst_password")
    class ConvertEwsToPSTOptionFlags(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNone: _ClassVar[EwsToPstConversionParams.ConvertEwsToPSTOptionFlags]
        kContinueOnError: _ClassVar[EwsToPstConversionParams.ConvertEwsToPSTOptionFlags]
    kNone: EwsToPstConversionParams.ConvertEwsToPSTOptionFlags
    kContinueOnError: EwsToPstConversionParams.ConvertEwsToPSTOptionFlags
    CREATE_PST_FIELD_NUMBER: _ClassVar[int]
    PST_NAME_PREFIX_FIELD_NUMBER: _ClassVar[int]
    PST_PASSWORD_FIELD_NUMBER: _ClassVar[int]
    PST_SIZE_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    OPTION_FLAGS_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTED_PST_PASSWORD_FIELD_NUMBER: _ClassVar[int]
    create_pst: bool
    pst_name_prefix: str
    pst_password: str
    pst_size_threshold: int
    option_flags: int
    encrypted_pst_password: str
    def __init__(self, create_pst: bool = ..., pst_name_prefix: _Optional[str] = ..., pst_password: _Optional[str] = ..., pst_size_threshold: _Optional[int] = ..., option_flags: _Optional[int] = ..., encrypted_pst_password: _Optional[str] = ...) -> None: ...

class StartPstConversionArg(_message.Message):
    __slots__ = ("input_dir", "output_dir", "pst_params", "total_items")
    INPUT_DIR_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_DIR_FIELD_NUMBER: _ClassVar[int]
    PST_PARAMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_ITEMS_FIELD_NUMBER: _ClassVar[int]
    input_dir: str
    output_dir: str
    pst_params: EwsToPstConversionParams
    total_items: int
    def __init__(self, input_dir: _Optional[str] = ..., output_dir: _Optional[str] = ..., pst_params: _Optional[_Union[EwsToPstConversionParams, _Mapping]] = ..., total_items: _Optional[int] = ...) -> None: ...

class StartPstConversionResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ConvertEwsToPstStatus(_message.Message):
    __slots__ = ("convert_pst_error", "total_items_count", "converted_items_count", "failed_items_count", "data_size_processed", "data_size_processed_bytes")
    CONVERT_PST_ERROR_FIELD_NUMBER: _ClassVar[int]
    TOTAL_ITEMS_COUNT_FIELD_NUMBER: _ClassVar[int]
    CONVERTED_ITEMS_COUNT_FIELD_NUMBER: _ClassVar[int]
    FAILED_ITEMS_COUNT_FIELD_NUMBER: _ClassVar[int]
    DATA_SIZE_PROCESSED_FIELD_NUMBER: _ClassVar[int]
    DATA_SIZE_PROCESSED_BYTES_FIELD_NUMBER: _ClassVar[int]
    convert_pst_error: _error_pb2.ErrorProto
    total_items_count: int
    converted_items_count: int
    failed_items_count: int
    data_size_processed: int
    data_size_processed_bytes: int
    def __init__(self, convert_pst_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., total_items_count: _Optional[int] = ..., converted_items_count: _Optional[int] = ..., failed_items_count: _Optional[int] = ..., data_size_processed: _Optional[int] = ..., data_size_processed_bytes: _Optional[int] = ...) -> None: ...

class GetPstConversionOutputArg(_message.Message):
    __slots__ = ("task_id",)
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    task_id: int
    def __init__(self, task_id: _Optional[int] = ...) -> None: ...

class GetPstConversionOutputResult(_message.Message):
    __slots__ = ("convert_pst_status",)
    CONVERT_PST_STATUS_FIELD_NUMBER: _ClassVar[int]
    convert_pst_status: ConvertEwsToPstStatus
    def __init__(self, convert_pst_status: _Optional[_Union[ConvertEwsToPstStatus, _Mapping]] = ...) -> None: ...

class CancelPstConversionArg(_message.Message):
    __slots__ = ("task_id",)
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    task_id: int
    def __init__(self, task_id: _Optional[int] = ...) -> None: ...

class CancelPstConversionResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CleanupPstConversionArg(_message.Message):
    __slots__ = ("task_id",)
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    task_id: int
    def __init__(self, task_id: _Optional[int] = ...) -> None: ...

class CleanupPstConversionResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetPstConversionProgressArg(_message.Message):
    __slots__ = ("task_id",)
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    task_id: int
    def __init__(self, task_id: _Optional[int] = ...) -> None: ...

class GetPstConversionProgressResult(_message.Message):
    __slots__ = ("task_state", "last_update_time", "activity_str", "convert_pst_status")
    class TaskProgressState(_message.Message):
        __slots__ = ()
        class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kUnknown: _ClassVar[GetPstConversionProgressResult.TaskProgressState.Type]
            kPending: _ClassVar[GetPstConversionProgressResult.TaskProgressState.Type]
            kProgress: _ClassVar[GetPstConversionProgressResult.TaskProgressState.Type]
            kCompleted: _ClassVar[GetPstConversionProgressResult.TaskProgressState.Type]
        kUnknown: GetPstConversionProgressResult.TaskProgressState.Type
        kPending: GetPstConversionProgressResult.TaskProgressState.Type
        kProgress: GetPstConversionProgressResult.TaskProgressState.Type
        kCompleted: GetPstConversionProgressResult.TaskProgressState.Type
        def __init__(self) -> None: ...
    TASK_STATE_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    ACTIVITY_STR_FIELD_NUMBER: _ClassVar[int]
    CONVERT_PST_STATUS_FIELD_NUMBER: _ClassVar[int]
    task_state: GetPstConversionProgressResult.TaskProgressState.Type
    last_update_time: int
    activity_str: str
    convert_pst_status: ConvertEwsToPstStatus
    def __init__(self, task_state: _Optional[_Union[GetPstConversionProgressResult.TaskProgressState.Type, str]] = ..., last_update_time: _Optional[int] = ..., activity_str: _Optional[str] = ..., convert_pst_status: _Optional[_Union[ConvertEwsToPstStatus, _Mapping]] = ...) -> None: ...

class ExchangeActionType(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kGetExchangeHierarchy: _ClassVar[ExchangeActionType.Type]
        kEDBLogVerify: _ClassVar[ExchangeActionType.Type]
        kGetMailboxMetadata: _ClassVar[ExchangeActionType.Type]
        kValidateExchangeDatabaseRestore: _ClassVar[ExchangeActionType.Type]
        kCreateExchangeDatabase: _ClassVar[ExchangeActionType.Type]
        kMountOrUnmountExchangeDatabase: _ClassVar[ExchangeActionType.Type]
        kDeleteExchangeDatabase: _ClassVar[ExchangeActionType.Type]
        kPlayLogsOnEDB: _ClassVar[ExchangeActionType.Type]
        kMoveMailboxProcessing: _ClassVar[ExchangeActionType.Type]
        kStartPstConversion: _ClassVar[ExchangeActionType.Type]
        kGetPstConversionOutput: _ClassVar[ExchangeActionType.Type]
        kGetPstConversionProgress: _ClassVar[ExchangeActionType.Type]
        kCancelPstConversionTask: _ClassVar[ExchangeActionType.Type]
        kCleanupPstConversionTask: _ClassVar[ExchangeActionType.Type]
        kPrepareExchangeDBRestore: _ClassVar[ExchangeActionType.Type]
        kGetJobProgress: _ClassVar[ExchangeActionType.Type]
        kGetJobOutput: _ClassVar[ExchangeActionType.Type]
        kCancelJob: _ClassVar[ExchangeActionType.Type]
        kCleanupJob: _ClassVar[ExchangeActionType.Type]
    kGetExchangeHierarchy: ExchangeActionType.Type
    kEDBLogVerify: ExchangeActionType.Type
    kGetMailboxMetadata: ExchangeActionType.Type
    kValidateExchangeDatabaseRestore: ExchangeActionType.Type
    kCreateExchangeDatabase: ExchangeActionType.Type
    kMountOrUnmountExchangeDatabase: ExchangeActionType.Type
    kDeleteExchangeDatabase: ExchangeActionType.Type
    kPlayLogsOnEDB: ExchangeActionType.Type
    kMoveMailboxProcessing: ExchangeActionType.Type
    kStartPstConversion: ExchangeActionType.Type
    kGetPstConversionOutput: ExchangeActionType.Type
    kGetPstConversionProgress: ExchangeActionType.Type
    kCancelPstConversionTask: ExchangeActionType.Type
    kCleanupPstConversionTask: ExchangeActionType.Type
    kPrepareExchangeDBRestore: ExchangeActionType.Type
    kGetJobProgress: ExchangeActionType.Type
    kGetJobOutput: ExchangeActionType.Type
    kCancelJob: ExchangeActionType.Type
    kCleanupJob: ExchangeActionType.Type
    def __init__(self) -> None: ...

class ExecuteExchangeActionArg(_message.Message):
    __slots__ = ("action_type", "timeout_sec", "num_retries", "get_entity_arg", "verify_edblog_arg", "get_database_mailbox_arg", "validate_database_restore_arg", "create_database_arg", "mount_or_unmount_database_arg", "delete_database_arg", "play_logs_on_edb_arg", "move_mailbox_processing_arg", "start_pst_conversion_arg", "get_pst_conversion_output_arg", "get_pst_conversion_progress_arg", "cancel_pst_conversion_arg", "cleanup_pst_conversion_arg", "prepare_exchange_db_restore_arg", "get_job_progress_arg", "get_job_output_arg", "cancel_job_arg", "cleanup_job_arg")
    ACTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_SEC_FIELD_NUMBER: _ClassVar[int]
    NUM_RETRIES_FIELD_NUMBER: _ClassVar[int]
    GET_ENTITY_ARG_FIELD_NUMBER: _ClassVar[int]
    VERIFY_EDBLOG_ARG_FIELD_NUMBER: _ClassVar[int]
    GET_DATABASE_MAILBOX_ARG_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_DATABASE_RESTORE_ARG_FIELD_NUMBER: _ClassVar[int]
    CREATE_DATABASE_ARG_FIELD_NUMBER: _ClassVar[int]
    MOUNT_OR_UNMOUNT_DATABASE_ARG_FIELD_NUMBER: _ClassVar[int]
    DELETE_DATABASE_ARG_FIELD_NUMBER: _ClassVar[int]
    PLAY_LOGS_ON_EDB_ARG_FIELD_NUMBER: _ClassVar[int]
    MOVE_MAILBOX_PROCESSING_ARG_FIELD_NUMBER: _ClassVar[int]
    START_PST_CONVERSION_ARG_FIELD_NUMBER: _ClassVar[int]
    GET_PST_CONVERSION_OUTPUT_ARG_FIELD_NUMBER: _ClassVar[int]
    GET_PST_CONVERSION_PROGRESS_ARG_FIELD_NUMBER: _ClassVar[int]
    CANCEL_PST_CONVERSION_ARG_FIELD_NUMBER: _ClassVar[int]
    CLEANUP_PST_CONVERSION_ARG_FIELD_NUMBER: _ClassVar[int]
    PREPARE_EXCHANGE_DB_RESTORE_ARG_FIELD_NUMBER: _ClassVar[int]
    GET_JOB_PROGRESS_ARG_FIELD_NUMBER: _ClassVar[int]
    GET_JOB_OUTPUT_ARG_FIELD_NUMBER: _ClassVar[int]
    CANCEL_JOB_ARG_FIELD_NUMBER: _ClassVar[int]
    CLEANUP_JOB_ARG_FIELD_NUMBER: _ClassVar[int]
    action_type: ExchangeActionType.Type
    timeout_sec: int
    num_retries: int
    get_entity_arg: GetExchangeHierarchyArg
    verify_edblog_arg: _exchange_pb2.ExchangeDBVerifyArg
    get_database_mailbox_arg: GetExchangeDatabaseMailboxMetadataArg
    validate_database_restore_arg: ValidateExchangeDatabaseRestoreArg
    create_database_arg: CreateExchangeDatabaseArg
    mount_or_unmount_database_arg: MountOrUnmountExchangeDatabaseArg
    delete_database_arg: DeleteExchangeDatabaseArg
    play_logs_on_edb_arg: PlayLogsOnExchangeEDBArg
    move_mailbox_processing_arg: MoveExchangeMailboxProcessingArg
    start_pst_conversion_arg: StartPstConversionArg
    get_pst_conversion_output_arg: GetPstConversionOutputArg
    get_pst_conversion_progress_arg: GetPstConversionProgressArg
    cancel_pst_conversion_arg: CancelPstConversionArg
    cleanup_pst_conversion_arg: CleanupPstConversionArg
    prepare_exchange_db_restore_arg: PrepareExchangeDBRestoreArg
    get_job_progress_arg: GetJobProgressArg
    get_job_output_arg: GetJobOutputArg
    cancel_job_arg: CancelJobArg
    cleanup_job_arg: CleanupJobArg
    def __init__(self, action_type: _Optional[_Union[ExchangeActionType.Type, str]] = ..., timeout_sec: _Optional[int] = ..., num_retries: _Optional[int] = ..., get_entity_arg: _Optional[_Union[GetExchangeHierarchyArg, _Mapping]] = ..., verify_edblog_arg: _Optional[_Union[_exchange_pb2.ExchangeDBVerifyArg, _Mapping]] = ..., get_database_mailbox_arg: _Optional[_Union[GetExchangeDatabaseMailboxMetadataArg, _Mapping]] = ..., validate_database_restore_arg: _Optional[_Union[ValidateExchangeDatabaseRestoreArg, _Mapping]] = ..., create_database_arg: _Optional[_Union[CreateExchangeDatabaseArg, _Mapping]] = ..., mount_or_unmount_database_arg: _Optional[_Union[MountOrUnmountExchangeDatabaseArg, _Mapping]] = ..., delete_database_arg: _Optional[_Union[DeleteExchangeDatabaseArg, _Mapping]] = ..., play_logs_on_edb_arg: _Optional[_Union[PlayLogsOnExchangeEDBArg, _Mapping]] = ..., move_mailbox_processing_arg: _Optional[_Union[MoveExchangeMailboxProcessingArg, _Mapping]] = ..., start_pst_conversion_arg: _Optional[_Union[StartPstConversionArg, _Mapping]] = ..., get_pst_conversion_output_arg: _Optional[_Union[GetPstConversionOutputArg, _Mapping]] = ..., get_pst_conversion_progress_arg: _Optional[_Union[GetPstConversionProgressArg, _Mapping]] = ..., cancel_pst_conversion_arg: _Optional[_Union[CancelPstConversionArg, _Mapping]] = ..., cleanup_pst_conversion_arg: _Optional[_Union[CleanupPstConversionArg, _Mapping]] = ..., prepare_exchange_db_restore_arg: _Optional[_Union[PrepareExchangeDBRestoreArg, _Mapping]] = ..., get_job_progress_arg: _Optional[_Union[GetJobProgressArg, _Mapping]] = ..., get_job_output_arg: _Optional[_Union[GetJobOutputArg, _Mapping]] = ..., cancel_job_arg: _Optional[_Union[CancelJobArg, _Mapping]] = ..., cleanup_job_arg: _Optional[_Union[CleanupJobArg, _Mapping]] = ...) -> None: ...

class ExecuteExchangeActionResult(_message.Message):
    __slots__ = ("action_type", "get_entity_result", "verify_edblog_result", "get_database_mailbox_result", "validate_database_restore_result", "create_database_result", "mount_or_unmount_database_result", "delete_database_result", "play_logs_on_edb_result", "move_mailbox_processing_result", "start_pst_conversion_result", "get_pst_conversion_output_result", "get_pst_conversion_progress_result", "cancel_pst_conversion_result", "cleanup_pst_conversion_result", "prepare_exchange_db_restore_result", "get_job_progress_result", "get_job_output_result", "cancel_job_result", "cleanup_job_result")
    ACTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    GET_ENTITY_RESULT_FIELD_NUMBER: _ClassVar[int]
    VERIFY_EDBLOG_RESULT_FIELD_NUMBER: _ClassVar[int]
    GET_DATABASE_MAILBOX_RESULT_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_DATABASE_RESTORE_RESULT_FIELD_NUMBER: _ClassVar[int]
    CREATE_DATABASE_RESULT_FIELD_NUMBER: _ClassVar[int]
    MOUNT_OR_UNMOUNT_DATABASE_RESULT_FIELD_NUMBER: _ClassVar[int]
    DELETE_DATABASE_RESULT_FIELD_NUMBER: _ClassVar[int]
    PLAY_LOGS_ON_EDB_RESULT_FIELD_NUMBER: _ClassVar[int]
    MOVE_MAILBOX_PROCESSING_RESULT_FIELD_NUMBER: _ClassVar[int]
    START_PST_CONVERSION_RESULT_FIELD_NUMBER: _ClassVar[int]
    GET_PST_CONVERSION_OUTPUT_RESULT_FIELD_NUMBER: _ClassVar[int]
    GET_PST_CONVERSION_PROGRESS_RESULT_FIELD_NUMBER: _ClassVar[int]
    CANCEL_PST_CONVERSION_RESULT_FIELD_NUMBER: _ClassVar[int]
    CLEANUP_PST_CONVERSION_RESULT_FIELD_NUMBER: _ClassVar[int]
    PREPARE_EXCHANGE_DB_RESTORE_RESULT_FIELD_NUMBER: _ClassVar[int]
    GET_JOB_PROGRESS_RESULT_FIELD_NUMBER: _ClassVar[int]
    GET_JOB_OUTPUT_RESULT_FIELD_NUMBER: _ClassVar[int]
    CANCEL_JOB_RESULT_FIELD_NUMBER: _ClassVar[int]
    CLEANUP_JOB_RESULT_FIELD_NUMBER: _ClassVar[int]
    action_type: ExchangeActionType.Type
    get_entity_result: GetExchangeHierarchyResult
    verify_edblog_result: _exchange_pb2.ExchangeDBVerifyResult
    get_database_mailbox_result: GetExchangeDatabaseMailboxMetadataResult
    validate_database_restore_result: ValidateExchangeDatabaseRestoreResult
    create_database_result: CreateExchangeDatabaseResult
    mount_or_unmount_database_result: MountOrUnmountExchangeDatabaseResult
    delete_database_result: DeleteExchangeDatabaseResult
    play_logs_on_edb_result: PlayLogsOnExchangeEDBResult
    move_mailbox_processing_result: MoveExchangeMailboxProcessingResult
    start_pst_conversion_result: StartPstConversionResult
    get_pst_conversion_output_result: GetPstConversionOutputResult
    get_pst_conversion_progress_result: GetPstConversionProgressResult
    cancel_pst_conversion_result: CancelPstConversionResult
    cleanup_pst_conversion_result: CleanupPstConversionResult
    prepare_exchange_db_restore_result: PrepareExchangeDBRestoreResult
    get_job_progress_result: GetJobProgressResult
    get_job_output_result: GetJobOutputResult
    cancel_job_result: CancelJobResult
    cleanup_job_result: CleanupJobResult
    def __init__(self, action_type: _Optional[_Union[ExchangeActionType.Type, str]] = ..., get_entity_result: _Optional[_Union[GetExchangeHierarchyResult, _Mapping]] = ..., verify_edblog_result: _Optional[_Union[_exchange_pb2.ExchangeDBVerifyResult, _Mapping]] = ..., get_database_mailbox_result: _Optional[_Union[GetExchangeDatabaseMailboxMetadataResult, _Mapping]] = ..., validate_database_restore_result: _Optional[_Union[ValidateExchangeDatabaseRestoreResult, _Mapping]] = ..., create_database_result: _Optional[_Union[CreateExchangeDatabaseResult, _Mapping]] = ..., mount_or_unmount_database_result: _Optional[_Union[MountOrUnmountExchangeDatabaseResult, _Mapping]] = ..., delete_database_result: _Optional[_Union[DeleteExchangeDatabaseResult, _Mapping]] = ..., play_logs_on_edb_result: _Optional[_Union[PlayLogsOnExchangeEDBResult, _Mapping]] = ..., move_mailbox_processing_result: _Optional[_Union[MoveExchangeMailboxProcessingResult, _Mapping]] = ..., start_pst_conversion_result: _Optional[_Union[StartPstConversionResult, _Mapping]] = ..., get_pst_conversion_output_result: _Optional[_Union[GetPstConversionOutputResult, _Mapping]] = ..., get_pst_conversion_progress_result: _Optional[_Union[GetPstConversionProgressResult, _Mapping]] = ..., cancel_pst_conversion_result: _Optional[_Union[CancelPstConversionResult, _Mapping]] = ..., cleanup_pst_conversion_result: _Optional[_Union[CleanupPstConversionResult, _Mapping]] = ..., prepare_exchange_db_restore_result: _Optional[_Union[PrepareExchangeDBRestoreResult, _Mapping]] = ..., get_job_progress_result: _Optional[_Union[GetJobProgressResult, _Mapping]] = ..., get_job_output_result: _Optional[_Union[GetJobOutputResult, _Mapping]] = ..., cancel_job_result: _Optional[_Union[CancelJobResult, _Mapping]] = ..., cleanup_job_result: _Optional[_Union[CleanupJobResult, _Mapping]] = ...) -> None: ...
