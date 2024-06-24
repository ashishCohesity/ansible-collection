from magneto.agents.base import agent_pb2 as _agent_pb2
from magneto.agents.base import error_pb2 as _error_pb2
from magneto.agents.windows.base import vss_pb2 as _vss_pb2
from magneto.base.entities import exchange_pb2 as _exchange_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ExchangeDBVerifyArg(_message.Message):
    __slots__ = ("db_guid", "db_name", "edb_file_path", "log_dir_path", "log_prefix", "verification_flags")
    class ExchangeDBVerificationOptionFlags(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNone: _ClassVar[ExchangeDBVerifyArg.ExchangeDBVerificationOptionFlags]
        kHeader: _ClassVar[ExchangeDBVerifyArg.ExchangeDBVerificationOptionFlags]
        kEnumerateLogFiles: _ClassVar[ExchangeDBVerifyArg.ExchangeDBVerificationOptionFlags]
    kNone: ExchangeDBVerifyArg.ExchangeDBVerificationOptionFlags
    kHeader: ExchangeDBVerifyArg.ExchangeDBVerificationOptionFlags
    kEnumerateLogFiles: ExchangeDBVerifyArg.ExchangeDBVerificationOptionFlags
    DB_GUID_FIELD_NUMBER: _ClassVar[int]
    DB_NAME_FIELD_NUMBER: _ClassVar[int]
    EDB_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    LOG_DIR_PATH_FIELD_NUMBER: _ClassVar[int]
    LOG_PREFIX_FIELD_NUMBER: _ClassVar[int]
    VERIFICATION_FLAGS_FIELD_NUMBER: _ClassVar[int]
    db_guid: str
    db_name: str
    edb_file_path: str
    log_dir_path: str
    log_prefix: str
    verification_flags: int
    def __init__(self, db_guid: _Optional[str] = ..., db_name: _Optional[str] = ..., edb_file_path: _Optional[str] = ..., log_dir_path: _Optional[str] = ..., log_prefix: _Optional[str] = ..., verification_flags: _Optional[int] = ...) -> None: ...

class ExchangeDBVerifyResult(_message.Message):
    __slots__ = ("edb_state_str", "edb_checksum", "edb_signature", "edb_logsignature", "edb_log_required_start", "edb_log_required_end", "edb_log_commited_start", "edb_log_commited_end", "edb_log_recovering", "edb_log_consistent", "checkpoint_log", "edb_create_date", "chk_circular_logging", "log_dir_lgeneration_start", "log_dir_lgeneration_end", "log_file_name_start", "log_file_name_end", "logdir_lgeneration_start_date", "logdir_lgeneration_end_date", "log_file_count")
    EDB_STATE_STR_FIELD_NUMBER: _ClassVar[int]
    EDB_CHECKSUM_FIELD_NUMBER: _ClassVar[int]
    EDB_SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    EDB_LOGSIGNATURE_FIELD_NUMBER: _ClassVar[int]
    EDB_LOG_REQUIRED_START_FIELD_NUMBER: _ClassVar[int]
    EDB_LOG_REQUIRED_END_FIELD_NUMBER: _ClassVar[int]
    EDB_LOG_COMMITED_START_FIELD_NUMBER: _ClassVar[int]
    EDB_LOG_COMMITED_END_FIELD_NUMBER: _ClassVar[int]
    EDB_LOG_RECOVERING_FIELD_NUMBER: _ClassVar[int]
    EDB_LOG_CONSISTENT_FIELD_NUMBER: _ClassVar[int]
    CHECKPOINT_LOG_FIELD_NUMBER: _ClassVar[int]
    EDB_CREATE_DATE_FIELD_NUMBER: _ClassVar[int]
    CHK_CIRCULAR_LOGGING_FIELD_NUMBER: _ClassVar[int]
    LOG_DIR_LGENERATION_START_FIELD_NUMBER: _ClassVar[int]
    LOG_DIR_LGENERATION_END_FIELD_NUMBER: _ClassVar[int]
    LOG_FILE_NAME_START_FIELD_NUMBER: _ClassVar[int]
    LOG_FILE_NAME_END_FIELD_NUMBER: _ClassVar[int]
    LOGDIR_LGENERATION_START_DATE_FIELD_NUMBER: _ClassVar[int]
    LOGDIR_LGENERATION_END_DATE_FIELD_NUMBER: _ClassVar[int]
    LOG_FILE_COUNT_FIELD_NUMBER: _ClassVar[int]
    edb_state_str: str
    edb_checksum: int
    edb_signature: int
    edb_logsignature: int
    edb_log_required_start: int
    edb_log_required_end: int
    edb_log_commited_start: int
    edb_log_commited_end: int
    edb_log_recovering: int
    edb_log_consistent: int
    checkpoint_log: int
    edb_create_date: _exchange_pb2.LocalTime
    chk_circular_logging: bool
    log_dir_lgeneration_start: int
    log_dir_lgeneration_end: int
    log_file_name_start: str
    log_file_name_end: str
    logdir_lgeneration_start_date: _exchange_pb2.LocalTime
    logdir_lgeneration_end_date: _exchange_pb2.LocalTime
    log_file_count: int
    def __init__(self, edb_state_str: _Optional[str] = ..., edb_checksum: _Optional[int] = ..., edb_signature: _Optional[int] = ..., edb_logsignature: _Optional[int] = ..., edb_log_required_start: _Optional[int] = ..., edb_log_required_end: _Optional[int] = ..., edb_log_commited_start: _Optional[int] = ..., edb_log_commited_end: _Optional[int] = ..., edb_log_recovering: _Optional[int] = ..., edb_log_consistent: _Optional[int] = ..., checkpoint_log: _Optional[int] = ..., edb_create_date: _Optional[_Union[_exchange_pb2.LocalTime, _Mapping]] = ..., chk_circular_logging: bool = ..., log_dir_lgeneration_start: _Optional[int] = ..., log_dir_lgeneration_end: _Optional[int] = ..., log_file_name_start: _Optional[str] = ..., log_file_name_end: _Optional[str] = ..., logdir_lgeneration_start_date: _Optional[_Union[_exchange_pb2.LocalTime, _Mapping]] = ..., logdir_lgeneration_end_date: _Optional[_Union[_exchange_pb2.LocalTime, _Mapping]] = ..., log_file_count: _Optional[int] = ...) -> None: ...

class ExchangeVSSBackupInfo(_message.Message):
    __slots__ = ("vss_backup_type", "db_backup_status_vec")
    class ExchangeDBVSSBackupStatus(_message.Message):
        __slots__ = ("db_guid", "db_name", "status", "log_file_prefix", "edb_file_vss_symlink_path", "log_dir_vss_symlink_path", "edb_file_size_bytes", "chk_file_size_bytes", "db_verify_result", "mailbox_manifest_status", "mailbox_manifest", "log_dir_extra_file_vec")
        DB_GUID_FIELD_NUMBER: _ClassVar[int]
        DB_NAME_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        LOG_FILE_PREFIX_FIELD_NUMBER: _ClassVar[int]
        EDB_FILE_VSS_SYMLINK_PATH_FIELD_NUMBER: _ClassVar[int]
        LOG_DIR_VSS_SYMLINK_PATH_FIELD_NUMBER: _ClassVar[int]
        EDB_FILE_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
        CHK_FILE_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
        DB_VERIFY_RESULT_FIELD_NUMBER: _ClassVar[int]
        MAILBOX_MANIFEST_STATUS_FIELD_NUMBER: _ClassVar[int]
        MAILBOX_MANIFEST_FIELD_NUMBER: _ClassVar[int]
        LOG_DIR_EXTRA_FILE_VEC_FIELD_NUMBER: _ClassVar[int]
        db_guid: str
        db_name: str
        status: _error_pb2.ErrorProto
        log_file_prefix: str
        edb_file_vss_symlink_path: str
        log_dir_vss_symlink_path: str
        edb_file_size_bytes: int
        chk_file_size_bytes: int
        db_verify_result: ExchangeDBVerifyResult
        mailbox_manifest_status: _error_pb2.ErrorProto
        mailbox_manifest: _exchange_pb2.ExchangeDatabaseMailboxManifest
        log_dir_extra_file_vec: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, db_guid: _Optional[str] = ..., db_name: _Optional[str] = ..., status: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., log_file_prefix: _Optional[str] = ..., edb_file_vss_symlink_path: _Optional[str] = ..., log_dir_vss_symlink_path: _Optional[str] = ..., edb_file_size_bytes: _Optional[int] = ..., chk_file_size_bytes: _Optional[int] = ..., db_verify_result: _Optional[_Union[ExchangeDBVerifyResult, _Mapping]] = ..., mailbox_manifest_status: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., mailbox_manifest: _Optional[_Union[_exchange_pb2.ExchangeDatabaseMailboxManifest, _Mapping]] = ..., log_dir_extra_file_vec: _Optional[_Iterable[str]] = ...) -> None: ...
    EXCHANGE_BACKUP_INFO_FIELD_NUMBER: _ClassVar[int]
    exchange_backup_info: _descriptor.FieldDescriptor
    VSS_BACKUP_TYPE_FIELD_NUMBER: _ClassVar[int]
    DB_BACKUP_STATUS_VEC_FIELD_NUMBER: _ClassVar[int]
    vss_backup_type: _vss_pb2.VSSBackupType.Type
    db_backup_status_vec: _containers.RepeatedCompositeFieldContainer[ExchangeVSSBackupInfo.ExchangeDBVSSBackupStatus]
    def __init__(self, vss_backup_type: _Optional[_Union[_vss_pb2.VSSBackupType.Type, str]] = ..., db_backup_status_vec: _Optional[_Iterable[_Union[ExchangeVSSBackupInfo.ExchangeDBVSSBackupStatus, _Mapping]]] = ...) -> None: ...

class ExchangeAppFileInfo(_message.Message):
    __slots__ = ("exchange_vssinfo",)
    APP_FILE_INFO_FIELD_NUMBER: _ClassVar[int]
    app_file_info: _descriptor.FieldDescriptor
    EXCHANGE_VSSINFO_FIELD_NUMBER: _ClassVar[int]
    exchange_vssinfo: ExchangeVSSBackupInfo
    def __init__(self, exchange_vssinfo: _Optional[_Union[ExchangeVSSBackupInfo, _Mapping]] = ...) -> None: ...
