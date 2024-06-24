from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TestSetup(_message.Message):
    __slots__ = ("scripts_share", "scripts_dir", "mount_drive", "script_backup_4vip", "script_invoke_backup", "restore_default", "tshark_drive", "script_purge_kerberos", "script_create_database", "db_load_data_file", "db_size_in_gb", "db_name_to_create", "db_restore_path", "restore_move")
    SCRIPTS_SHARE_FIELD_NUMBER: _ClassVar[int]
    SCRIPTS_DIR_FIELD_NUMBER: _ClassVar[int]
    MOUNT_DRIVE_FIELD_NUMBER: _ClassVar[int]
    SCRIPT_BACKUP_4VIP_FIELD_NUMBER: _ClassVar[int]
    SCRIPT_INVOKE_BACKUP_FIELD_NUMBER: _ClassVar[int]
    RESTORE_DEFAULT_FIELD_NUMBER: _ClassVar[int]
    TSHARK_DRIVE_FIELD_NUMBER: _ClassVar[int]
    SCRIPT_PURGE_KERBEROS_FIELD_NUMBER: _ClassVar[int]
    SCRIPT_CREATE_DATABASE_FIELD_NUMBER: _ClassVar[int]
    DB_LOAD_DATA_FILE_FIELD_NUMBER: _ClassVar[int]
    DB_SIZE_IN_GB_FIELD_NUMBER: _ClassVar[int]
    DB_NAME_TO_CREATE_FIELD_NUMBER: _ClassVar[int]
    DB_RESTORE_PATH_FIELD_NUMBER: _ClassVar[int]
    RESTORE_MOVE_FIELD_NUMBER: _ClassVar[int]
    scripts_share: str
    scripts_dir: str
    mount_drive: str
    script_backup_4vip: str
    script_invoke_backup: str
    restore_default: str
    tshark_drive: str
    script_purge_kerberos: str
    script_create_database: str
    db_load_data_file: str
    db_size_in_gb: str
    db_name_to_create: str
    db_restore_path: str
    restore_move: str
    def __init__(self, scripts_share: _Optional[str] = ..., scripts_dir: _Optional[str] = ..., mount_drive: _Optional[str] = ..., script_backup_4vip: _Optional[str] = ..., script_invoke_backup: _Optional[str] = ..., restore_default: _Optional[str] = ..., tshark_drive: _Optional[str] = ..., script_purge_kerberos: _Optional[str] = ..., script_create_database: _Optional[str] = ..., db_load_data_file: _Optional[str] = ..., db_size_in_gb: _Optional[str] = ..., db_name_to_create: _Optional[str] = ..., db_restore_path: _Optional[str] = ..., restore_move: _Optional[str] = ...) -> None: ...

class WindowsCredentials(_message.Message):
    __slots__ = ("username", "password")
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    username: str
    password: str
    def __init__(self, username: _Optional[str] = ..., password: _Optional[str] = ...) -> None: ...

class SqlInfo(_message.Message):
    __slots__ = ("username", "password", "mount_drive", "sql_instance", "sql_small_db", "sql_large_db", "sql_mid_db")
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    MOUNT_DRIVE_FIELD_NUMBER: _ClassVar[int]
    SQL_INSTANCE_FIELD_NUMBER: _ClassVar[int]
    SQL_SMALL_DB_FIELD_NUMBER: _ClassVar[int]
    SQL_LARGE_DB_FIELD_NUMBER: _ClassVar[int]
    SQL_MID_DB_FIELD_NUMBER: _ClassVar[int]
    username: str
    password: str
    mount_drive: str
    sql_instance: str
    sql_small_db: str
    sql_large_db: str
    sql_mid_db: str
    def __init__(self, username: _Optional[str] = ..., password: _Optional[str] = ..., mount_drive: _Optional[str] = ..., sql_instance: _Optional[str] = ..., sql_small_db: _Optional[str] = ..., sql_large_db: _Optional[str] = ..., sql_mid_db: _Optional[str] = ...) -> None: ...

class LogCollectorInfo(_message.Message):
    __slots__ = ("target_share", "mount_drive", "sql_logs_path")
    TARGET_SHARE_FIELD_NUMBER: _ClassVar[int]
    MOUNT_DRIVE_FIELD_NUMBER: _ClassVar[int]
    SQL_LOGS_PATH_FIELD_NUMBER: _ClassVar[int]
    target_share: str
    mount_drive: str
    sql_logs_path: str
    def __init__(self, target_share: _Optional[str] = ..., mount_drive: _Optional[str] = ..., sql_logs_path: _Optional[str] = ...) -> None: ...

class SmbHost(_message.Message):
    __slots__ = ("host_type", "host_name", "host_ip")
    class HostType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        WIN2012R2: _ClassVar[SmbHost.HostType]
        WIN2008R2: _ClassVar[SmbHost.HostType]
    WIN2012R2: SmbHost.HostType
    WIN2008R2: SmbHost.HostType
    HOST_TYPE_FIELD_NUMBER: _ClassVar[int]
    HOST_NAME_FIELD_NUMBER: _ClassVar[int]
    HOST_IP_FIELD_NUMBER: _ClassVar[int]
    host_type: SmbHost.HostType
    host_name: str
    host_ip: str
    def __init__(self, host_type: _Optional[_Union[SmbHost.HostType, str]] = ..., host_name: _Optional[str] = ..., host_ip: _Optional[str] = ...) -> None: ...

class SmbTestServers(_message.Message):
    __slots__ = ("test_setup", "windows_credentials", "sql_info", "log_collector_info", "smb_host_vec")
    TEST_SETUP_FIELD_NUMBER: _ClassVar[int]
    WINDOWS_CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    SQL_INFO_FIELD_NUMBER: _ClassVar[int]
    LOG_COLLECTOR_INFO_FIELD_NUMBER: _ClassVar[int]
    SMB_HOST_VEC_FIELD_NUMBER: _ClassVar[int]
    test_setup: TestSetup
    windows_credentials: WindowsCredentials
    sql_info: SqlInfo
    log_collector_info: LogCollectorInfo
    smb_host_vec: _containers.RepeatedCompositeFieldContainer[SmbHost]
    def __init__(self, test_setup: _Optional[_Union[TestSetup, _Mapping]] = ..., windows_credentials: _Optional[_Union[WindowsCredentials, _Mapping]] = ..., sql_info: _Optional[_Union[SqlInfo, _Mapping]] = ..., log_collector_info: _Optional[_Union[LogCollectorInfo, _Mapping]] = ..., smb_host_vec: _Optional[_Iterable[_Union[SmbHost, _Mapping]]] = ...) -> None: ...
