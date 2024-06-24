from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ADDomainMode(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kUnknownDomain: _ClassVar[ADDomainMode.Type]
        kWindows2000Domain: _ClassVar[ADDomainMode.Type]
        kWindows2003InterimDomain: _ClassVar[ADDomainMode.Type]
        kWindows2003Domain: _ClassVar[ADDomainMode.Type]
        kWindows2008Domain: _ClassVar[ADDomainMode.Type]
        kWindows2008R2Domain: _ClassVar[ADDomainMode.Type]
        kWindows2012Domain: _ClassVar[ADDomainMode.Type]
        kWindows2012R2Domain: _ClassVar[ADDomainMode.Type]
        kWindows2016Domain: _ClassVar[ADDomainMode.Type]
        kWindows2019Domain: _ClassVar[ADDomainMode.Type]
    kUnknownDomain: ADDomainMode.Type
    kWindows2000Domain: ADDomainMode.Type
    kWindows2003InterimDomain: ADDomainMode.Type
    kWindows2003Domain: ADDomainMode.Type
    kWindows2008Domain: ADDomainMode.Type
    kWindows2008R2Domain: ADDomainMode.Type
    kWindows2012Domain: ADDomainMode.Type
    kWindows2012R2Domain: ADDomainMode.Type
    kWindows2016Domain: ADDomainMode.Type
    kWindows2019Domain: ADDomainMode.Type
    def __init__(self) -> None: ...

class ADForestMode(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kUnknownForest: _ClassVar[ADForestMode.Type]
        kWindows2000Forest: _ClassVar[ADForestMode.Type]
        kWindows2003InterimForest: _ClassVar[ADForestMode.Type]
        kWindows2003Forest: _ClassVar[ADForestMode.Type]
        kWindows2008Forest: _ClassVar[ADForestMode.Type]
        kWindows2008R2Forest: _ClassVar[ADForestMode.Type]
        kWindows2012Forest: _ClassVar[ADForestMode.Type]
        kWindows2012R2Forest: _ClassVar[ADForestMode.Type]
        kWindows2016Forest: _ClassVar[ADForestMode.Type]
        kWindows2019Forest: _ClassVar[ADForestMode.Type]
    kUnknownForest: ADForestMode.Type
    kWindows2000Forest: ADForestMode.Type
    kWindows2003InterimForest: ADForestMode.Type
    kWindows2003Forest: ADForestMode.Type
    kWindows2008Forest: ADForestMode.Type
    kWindows2008R2Forest: ADForestMode.Type
    kWindows2012Forest: ADForestMode.Type
    kWindows2012R2Forest: ADForestMode.Type
    kWindows2016Forest: ADForestMode.Type
    kWindows2019Forest: ADForestMode.Type
    def __init__(self) -> None: ...

class ADDomainIdentity(_message.Message):
    __slots__ = ("object_guid", "dn", "name", "sid")
    OBJECT_GUID_FIELD_NUMBER: _ClassVar[int]
    DN_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SID_FIELD_NUMBER: _ClassVar[int]
    object_guid: str
    dn: str
    name: str
    sid: str
    def __init__(self, object_guid: _Optional[str] = ..., dn: _Optional[str] = ..., name: _Optional[str] = ..., sid: _Optional[str] = ...) -> None: ...

class ADDomain(_message.Message):
    __slots__ = ("id", "domain_mode", "forest_mode", "forest", "netbios_name", "dns_root", "parent_domain", "tombstone_days", "schema_version")
    ID_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_MODE_FIELD_NUMBER: _ClassVar[int]
    FOREST_MODE_FIELD_NUMBER: _ClassVar[int]
    FOREST_FIELD_NUMBER: _ClassVar[int]
    NETBIOS_NAME_FIELD_NUMBER: _ClassVar[int]
    DNS_ROOT_FIELD_NUMBER: _ClassVar[int]
    PARENT_DOMAIN_FIELD_NUMBER: _ClassVar[int]
    TOMBSTONE_DAYS_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_VERSION_FIELD_NUMBER: _ClassVar[int]
    id: ADDomainIdentity
    domain_mode: ADDomainMode.Type
    forest_mode: ADForestMode.Type
    forest: str
    netbios_name: str
    dns_root: str
    parent_domain: str
    tombstone_days: int
    schema_version: int
    def __init__(self, id: _Optional[_Union[ADDomainIdentity, _Mapping]] = ..., domain_mode: _Optional[_Union[ADDomainMode.Type, str]] = ..., forest_mode: _Optional[_Union[ADForestMode.Type, str]] = ..., forest: _Optional[str] = ..., netbios_name: _Optional[str] = ..., dns_root: _Optional[str] = ..., parent_domain: _Optional[str] = ..., tombstone_days: _Optional[int] = ..., schema_version: _Optional[int] = ...) -> None: ...

class ADDatabaseInfo(_message.Message):
    __slots__ = ("name", "db_file_path", "db_file_size_bytes", "log_dir_path", "db_volume_guid", "log_volume_guid", "ldap_port", "ldap_ssl_port")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DB_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    DB_FILE_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    LOG_DIR_PATH_FIELD_NUMBER: _ClassVar[int]
    DB_VOLUME_GUID_FIELD_NUMBER: _ClassVar[int]
    LOG_VOLUME_GUID_FIELD_NUMBER: _ClassVar[int]
    LDAP_PORT_FIELD_NUMBER: _ClassVar[int]
    LDAP_SSL_PORT_FIELD_NUMBER: _ClassVar[int]
    name: str
    db_file_path: str
    db_file_size_bytes: int
    log_dir_path: str
    db_volume_guid: str
    log_volume_guid: str
    ldap_port: int
    ldap_ssl_port: int
    def __init__(self, name: _Optional[str] = ..., db_file_path: _Optional[str] = ..., db_file_size_bytes: _Optional[int] = ..., log_dir_path: _Optional[str] = ..., db_volume_guid: _Optional[str] = ..., log_volume_guid: _Optional[str] = ..., ldap_port: _Optional[int] = ..., ldap_ssl_port: _Optional[int] = ...) -> None: ...

class ADSysvolInfo(_message.Message):
    __slots__ = ("sysvol_folder_path", "sysvol_volume_guid")
    SYSVOL_FOLDER_PATH_FIELD_NUMBER: _ClassVar[int]
    SYSVOL_VOLUME_GUID_FIELD_NUMBER: _ClassVar[int]
    sysvol_folder_path: str
    sysvol_volume_guid: str
    def __init__(self, sysvol_folder_path: _Optional[str] = ..., sysvol_volume_guid: _Optional[str] = ...) -> None: ...

class ADDomainController(_message.Message):
    __slots__ = ("domain", "ntds_db", "adam_db_vec", "host_name", "fsmo_role_vec", "is_global_catalog", "is_read_only", "utcoffsetmin", "vss_backup_writers_vec", "backup_supported", "backup_unsupported_reason_vec", "sysvol_folder")
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    NTDS_DB_FIELD_NUMBER: _ClassVar[int]
    ADAM_DB_VEC_FIELD_NUMBER: _ClassVar[int]
    HOST_NAME_FIELD_NUMBER: _ClassVar[int]
    FSMO_ROLE_VEC_FIELD_NUMBER: _ClassVar[int]
    IS_GLOBAL_CATALOG_FIELD_NUMBER: _ClassVar[int]
    IS_READ_ONLY_FIELD_NUMBER: _ClassVar[int]
    UTCOFFSETMIN_FIELD_NUMBER: _ClassVar[int]
    VSS_BACKUP_WRITERS_VEC_FIELD_NUMBER: _ClassVar[int]
    BACKUP_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    BACKUP_UNSUPPORTED_REASON_VEC_FIELD_NUMBER: _ClassVar[int]
    SYSVOL_FOLDER_FIELD_NUMBER: _ClassVar[int]
    domain: ADDomain
    ntds_db: ADDatabaseInfo
    adam_db_vec: _containers.RepeatedCompositeFieldContainer[ADDatabaseInfo]
    host_name: str
    fsmo_role_vec: _containers.RepeatedScalarFieldContainer[str]
    is_global_catalog: bool
    is_read_only: bool
    utcoffsetmin: int
    vss_backup_writers_vec: _containers.RepeatedScalarFieldContainer[str]
    backup_supported: bool
    backup_unsupported_reason_vec: _containers.RepeatedScalarFieldContainer[str]
    sysvol_folder: ADSysvolInfo
    def __init__(self, domain: _Optional[_Union[ADDomain, _Mapping]] = ..., ntds_db: _Optional[_Union[ADDatabaseInfo, _Mapping]] = ..., adam_db_vec: _Optional[_Iterable[_Union[ADDatabaseInfo, _Mapping]]] = ..., host_name: _Optional[str] = ..., fsmo_role_vec: _Optional[_Iterable[str]] = ..., is_global_catalog: bool = ..., is_read_only: bool = ..., utcoffsetmin: _Optional[int] = ..., vss_backup_writers_vec: _Optional[_Iterable[str]] = ..., backup_supported: bool = ..., backup_unsupported_reason_vec: _Optional[_Iterable[str]] = ..., sysvol_folder: _Optional[_Union[ADSysvolInfo, _Mapping]] = ...) -> None: ...

class Entity(_message.Message):
    __slots__ = ("type", "uuid", "name", "domain_name", "dc", "owner_id")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kRootContainer: _ClassVar[Entity.Type]
        kDomainController: _ClassVar[Entity.Type]
    kRootContainer: Entity.Type
    kDomainController: Entity.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    DC_FIELD_NUMBER: _ClassVar[int]
    OWNER_ID_FIELD_NUMBER: _ClassVar[int]
    type: Entity.Type
    uuid: str
    name: str
    domain_name: str
    dc: ADDomainController
    owner_id: int
    def __init__(self, type: _Optional[_Union[Entity.Type, str]] = ..., uuid: _Optional[str] = ..., name: _Optional[str] = ..., domain_name: _Optional[str] = ..., dc: _Optional[_Union[ADDomainController, _Mapping]] = ..., owner_id: _Optional[int] = ...) -> None: ...
