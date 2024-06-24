from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class VlanParams(_message.Message):
    __slots__ = ("vlan_id", "disable_vlan", "interface_name")
    VLAN_ID_FIELD_NUMBER: _ClassVar[int]
    DISABLE_VLAN_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_NAME_FIELD_NUMBER: _ClassVar[int]
    vlan_id: int
    disable_vlan: bool
    interface_name: str
    def __init__(self, vlan_id: _Optional[int] = ..., disable_vlan: bool = ..., interface_name: _Optional[str] = ...) -> None: ...

class OracleRmanBackupType(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kImageCopy: _ClassVar[OracleRmanBackupType.Type]
        kBackupSets: _ClassVar[OracleRmanBackupType.Type]
        kSbt: _ClassVar[OracleRmanBackupType.Type]
    kImageCopy: OracleRmanBackupType.Type
    kBackupSets: OracleRmanBackupType.Type
    kSbt: OracleRmanBackupType.Type
    def __init__(self) -> None: ...

class OracleArchiveLogRetentionType(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kHour: _ClassVar[OracleArchiveLogRetentionType.Type]
        kDay: _ClassVar[OracleArchiveLogRetentionType.Type]
    kHour: OracleArchiveLogRetentionType.Type
    kDay: OracleArchiveLogRetentionType.Type
    def __init__(self) -> None: ...

class OracleVlanInfo(_message.Message):
    __slots__ = ("ip_vec", "gateway", "id", "subnet_ip")
    IP_VEC_FIELD_NUMBER: _ClassVar[int]
    GATEWAY_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    SUBNET_IP_FIELD_NUMBER: _ClassVar[int]
    ip_vec: _containers.RepeatedScalarFieldContainer[str]
    gateway: str
    id: int
    subnet_ip: str
    def __init__(self, ip_vec: _Optional[_Iterable[str]] = ..., gateway: _Optional[str] = ..., id: _Optional[int] = ..., subnet_ip: _Optional[str] = ...) -> None: ...

class OracleSbtHostParams(_message.Message):
    __slots__ = ("sbt_library_path", "view_fs_path", "vip_vec", "vlan_info_vec")
    SBT_LIBRARY_PATH_FIELD_NUMBER: _ClassVar[int]
    VIEW_FS_PATH_FIELD_NUMBER: _ClassVar[int]
    VIP_VEC_FIELD_NUMBER: _ClassVar[int]
    VLAN_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    sbt_library_path: str
    view_fs_path: str
    vip_vec: _containers.RepeatedScalarFieldContainer[str]
    vlan_info_vec: _containers.RepeatedCompositeFieldContainer[OracleVlanInfo]
    def __init__(self, sbt_library_path: _Optional[str] = ..., view_fs_path: _Optional[str] = ..., vip_vec: _Optional[_Iterable[str]] = ..., vlan_info_vec: _Optional[_Iterable[_Union[OracleVlanInfo, _Mapping]]] = ...) -> None: ...

class HostInfo(_message.Message):
    __slots__ = ("host", "num_channels", "portnum", "sbt_host_params")
    HOST_FIELD_NUMBER: _ClassVar[int]
    NUM_CHANNELS_FIELD_NUMBER: _ClassVar[int]
    PORTNUM_FIELD_NUMBER: _ClassVar[int]
    SBT_HOST_PARAMS_FIELD_NUMBER: _ClassVar[int]
    host: str
    num_channels: int
    portnum: int
    sbt_host_params: OracleSbtHostParams
    def __init__(self, host: _Optional[str] = ..., num_channels: _Optional[int] = ..., portnum: _Optional[int] = ..., sbt_host_params: _Optional[_Union[OracleSbtHostParams, _Mapping]] = ...) -> None: ...

class Credentials(_message.Message):
    __slots__ = ("username", "password", "encrypted_password")
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTED_PASSWORD_FIELD_NUMBER: _ClassVar[int]
    username: str
    password: bytes
    encrypted_password: bytes
    def __init__(self, username: _Optional[str] = ..., password: _Optional[bytes] = ..., encrypted_password: _Optional[bytes] = ...) -> None: ...

class OracleDBChannelInfo(_message.Message):
    __slots__ = ("host_info_vec", "max_num_host", "num_channels", "db_uuid", "db_unique_name", "archivelog_keep_days", "enable_dg_primary_backup", "rman_backup_type", "credentials", "archivelog_keep_hours")
    HOST_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    MAX_NUM_HOST_FIELD_NUMBER: _ClassVar[int]
    NUM_CHANNELS_FIELD_NUMBER: _ClassVar[int]
    DB_UUID_FIELD_NUMBER: _ClassVar[int]
    DB_UNIQUE_NAME_FIELD_NUMBER: _ClassVar[int]
    ARCHIVELOG_KEEP_DAYS_FIELD_NUMBER: _ClassVar[int]
    ENABLE_DG_PRIMARY_BACKUP_FIELD_NUMBER: _ClassVar[int]
    RMAN_BACKUP_TYPE_FIELD_NUMBER: _ClassVar[int]
    CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    ARCHIVELOG_KEEP_HOURS_FIELD_NUMBER: _ClassVar[int]
    host_info_vec: _containers.RepeatedCompositeFieldContainer[HostInfo]
    max_num_host: int
    num_channels: int
    db_uuid: str
    db_unique_name: str
    archivelog_keep_days: int
    enable_dg_primary_backup: bool
    rman_backup_type: OracleRmanBackupType.Type
    credentials: Credentials
    archivelog_keep_hours: int
    def __init__(self, host_info_vec: _Optional[_Iterable[_Union[HostInfo, _Mapping]]] = ..., max_num_host: _Optional[int] = ..., num_channels: _Optional[int] = ..., db_uuid: _Optional[str] = ..., db_unique_name: _Optional[str] = ..., archivelog_keep_days: _Optional[int] = ..., enable_dg_primary_backup: bool = ..., rman_backup_type: _Optional[_Union[OracleRmanBackupType.Type, str]] = ..., credentials: _Optional[_Union[Credentials, _Mapping]] = ..., archivelog_keep_hours: _Optional[int] = ...) -> None: ...

class AdditionalOracleDBParams(_message.Message):
    __slots__ = ("app_entity_id", "db_info_channel_vec")
    APP_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    DB_INFO_CHANNEL_VEC_FIELD_NUMBER: _ClassVar[int]
    app_entity_id: int
    db_info_channel_vec: _containers.RepeatedCompositeFieldContainer[OracleDBChannelInfo]
    def __init__(self, app_entity_id: _Optional[int] = ..., db_info_channel_vec: _Optional[_Iterable[_Union[OracleDBChannelInfo, _Mapping]]] = ...) -> None: ...

class EnvBackupParamsProto(_message.Message):
    __slots__ = ("persist_mountpoints", "vlan_params")
    PERSIST_MOUNTPOINTS_FIELD_NUMBER: _ClassVar[int]
    VLAN_PARAMS_FIELD_NUMBER: _ClassVar[int]
    persist_mountpoints: bool
    vlan_params: VlanParams
    def __init__(self, persist_mountpoints: bool = ..., vlan_params: _Optional[_Union[VlanParams, _Mapping]] = ...) -> None: ...

class OracleBackupSourceParamsProto(_message.Message):
    __slots__ = ("additional_oracle_db_params_vec", "persist_mountpoints")
    ADDITIONAL_ORACLE_DB_PARAMS_VEC_FIELD_NUMBER: _ClassVar[int]
    PERSIST_MOUNTPOINTS_FIELD_NUMBER: _ClassVar[int]
    additional_oracle_db_params_vec: _containers.RepeatedCompositeFieldContainer[AdditionalOracleDBParams]
    persist_mountpoints: bool
    def __init__(self, additional_oracle_db_params_vec: _Optional[_Iterable[_Union[AdditionalOracleDBParams, _Mapping]]] = ..., persist_mountpoints: bool = ...) -> None: ...

class SameConfigIrRecoveryOptions(_message.Message):
    __slots__ = ("is_same_config_ir_recovery", "cleanup_original_db_files", "rename_database_asm_directory")
    IS_SAME_CONFIG_IR_RECOVERY_FIELD_NUMBER: _ClassVar[int]
    CLEANUP_ORIGINAL_DB_FILES_FIELD_NUMBER: _ClassVar[int]
    RENAME_DATABASE_ASM_DIRECTORY_FIELD_NUMBER: _ClassVar[int]
    is_same_config_ir_recovery: bool
    cleanup_original_db_files: bool
    rename_database_asm_directory: bool
    def __init__(self, is_same_config_ir_recovery: bool = ..., cleanup_original_db_files: bool = ..., rename_database_asm_directory: bool = ...) -> None: ...
