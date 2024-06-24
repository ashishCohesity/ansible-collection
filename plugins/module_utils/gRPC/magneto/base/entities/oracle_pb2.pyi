from magneto.api.common import stats_pb2 as _stats_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SessionConfiguration(_message.Message):
    __slots__ = ("sid", "oracle_home", "oracle_base")
    SID_FIELD_NUMBER: _ClassVar[int]
    ORACLE_HOME_FIELD_NUMBER: _ClassVar[int]
    ORACLE_BASE_FIELD_NUMBER: _ClassVar[int]
    sid: str
    oracle_home: str
    oracle_base: str
    def __init__(self, sid: _Optional[str] = ..., oracle_home: _Optional[str] = ..., oracle_base: _Optional[str] = ...) -> None: ...

class Host(_message.Message):
    __slots__ = ("num_cpu", "ip_address_vec", "session_conf_vec", "portnum_vec")
    NUM_CPU_FIELD_NUMBER: _ClassVar[int]
    IP_ADDRESS_VEC_FIELD_NUMBER: _ClassVar[int]
    SESSION_CONF_VEC_FIELD_NUMBER: _ClassVar[int]
    PORTNUM_VEC_FIELD_NUMBER: _ClassVar[int]
    num_cpu: int
    ip_address_vec: _containers.RepeatedScalarFieldContainer[str]
    session_conf_vec: _containers.RepeatedCompositeFieldContainer[SessionConfiguration]
    portnum_vec: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, num_cpu: _Optional[int] = ..., ip_address_vec: _Optional[_Iterable[str]] = ..., session_conf_vec: _Optional[_Iterable[_Union[SessionConfiguration, _Mapping]]] = ..., portnum_vec: _Optional[_Iterable[int]] = ...) -> None: ...

class DGEntityInfo(_message.Message):
    __slots__ = ("role", "type")
    class Role(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kPrimary: _ClassVar[DGEntityInfo.Role]
        kStandby: _ClassVar[DGEntityInfo.Role]
    kPrimary: DGEntityInfo.Role
    kStandby: DGEntityInfo.Role
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kPhysical: _ClassVar[DGEntityInfo.Type]
        kLogical: _ClassVar[DGEntityInfo.Type]
        kSnapshot: _ClassVar[DGEntityInfo.Type]
    kPhysical: DGEntityInfo.Type
    kLogical: DGEntityInfo.Type
    kSnapshot: DGEntityInfo.Type
    ROLE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    role: DGEntityInfo.Role
    type: DGEntityInfo.Type
    def __init__(self, role: _Optional[_Union[DGEntityInfo.Role, str]] = ..., type: _Optional[_Union[DGEntityInfo.Type, str]] = ...) -> None: ...

class PDBEntityInfo(_message.Message):
    __slots__ = ("name", "db_id", "size_bytes", "open_mode")
    class OpenMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kMounted: _ClassVar[PDBEntityInfo.OpenMode]
        kReadWrite: _ClassVar[PDBEntityInfo.OpenMode]
        kReadOnly: _ClassVar[PDBEntityInfo.OpenMode]
        kMigrate: _ClassVar[PDBEntityInfo.OpenMode]
    kMounted: PDBEntityInfo.OpenMode
    kReadWrite: PDBEntityInfo.OpenMode
    kReadOnly: PDBEntityInfo.OpenMode
    kMigrate: PDBEntityInfo.OpenMode
    NAME_FIELD_NUMBER: _ClassVar[int]
    DB_ID_FIELD_NUMBER: _ClassVar[int]
    SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    OPEN_MODE_FIELD_NUMBER: _ClassVar[int]
    name: str
    db_id: str
    size_bytes: int
    open_mode: PDBEntityInfo.OpenMode
    def __init__(self, name: _Optional[str] = ..., db_id: _Optional[str] = ..., size_bytes: _Optional[int] = ..., open_mode: _Optional[_Union[PDBEntityInfo.OpenMode, str]] = ...) -> None: ...

class CDBEntityInfo(_message.Message):
    __slots__ = ("pdb_entity_info_vec",)
    PDB_ENTITY_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    pdb_entity_info_vec: _containers.RepeatedCompositeFieldContainer[PDBEntityInfo]
    def __init__(self, pdb_entity_info_vec: _Optional[_Iterable[_Union[PDBEntityInfo, _Mapping]]] = ...) -> None: ...

class DBEntityInfo(_message.Message):
    __slots__ = ("size_bytes", "archivelog_enabled", "bct_enabled", "host_vec", "version", "db_type", "sga_target_size", "shared_pool_size", "temp_files_count", "fra_size", "db_unique_name", "dg_entity_info", "db_domain", "cdb_entity_info", "pdb_entity_info", "tde_encrypted_ts_count", "open_mode", "compatibility", "max_datafiles", "max_log_history", "max_instances", "max_logfiles", "max_logmembers", "character_set", "db_edition", "tempfile_info_vec", "spfile_path")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kSingleInstance: _ClassVar[DBEntityInfo.Type]
        kRACDatabase: _ClassVar[DBEntityInfo.Type]
    kSingleInstance: DBEntityInfo.Type
    kRACDatabase: DBEntityInfo.Type
    class OpenMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kReadWrite: _ClassVar[DBEntityInfo.OpenMode]
        kReadOnlyApply: _ClassVar[DBEntityInfo.OpenMode]
        kReadOnly: _ClassVar[DBEntityInfo.OpenMode]
        kMounted: _ClassVar[DBEntityInfo.OpenMode]
    kReadWrite: DBEntityInfo.OpenMode
    kReadOnlyApply: DBEntityInfo.OpenMode
    kReadOnly: DBEntityInfo.OpenMode
    kMounted: DBEntityInfo.OpenMode
    class Edition(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kEnterprise: _ClassVar[DBEntityInfo.Edition]
        kStandard: _ClassVar[DBEntityInfo.Edition]
        kExpress: _ClassVar[DBEntityInfo.Edition]
        kPersonal: _ClassVar[DBEntityInfo.Edition]
    kEnterprise: DBEntityInfo.Edition
    kStandard: DBEntityInfo.Edition
    kExpress: DBEntityInfo.Edition
    kPersonal: DBEntityInfo.Edition
    class TempfileInfoRow(_message.Message):
        __slots__ = ("tempfile_number", "status", "path", "create_size_bytes", "tablespace_name", "container_name")
        class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kOffline: _ClassVar[DBEntityInfo.TempfileInfoRow.Status]
            kOnline: _ClassVar[DBEntityInfo.TempfileInfoRow.Status]
        kOffline: DBEntityInfo.TempfileInfoRow.Status
        kOnline: DBEntityInfo.TempfileInfoRow.Status
        TEMPFILE_NUMBER_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        PATH_FIELD_NUMBER: _ClassVar[int]
        CREATE_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
        TABLESPACE_NAME_FIELD_NUMBER: _ClassVar[int]
        CONTAINER_NAME_FIELD_NUMBER: _ClassVar[int]
        tempfile_number: int
        status: DBEntityInfo.TempfileInfoRow.Status
        path: str
        create_size_bytes: int
        tablespace_name: str
        container_name: str
        def __init__(self, tempfile_number: _Optional[int] = ..., status: _Optional[_Union[DBEntityInfo.TempfileInfoRow.Status, str]] = ..., path: _Optional[str] = ..., create_size_bytes: _Optional[int] = ..., tablespace_name: _Optional[str] = ..., container_name: _Optional[str] = ...) -> None: ...
    SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    ARCHIVELOG_ENABLED_FIELD_NUMBER: _ClassVar[int]
    BCT_ENABLED_FIELD_NUMBER: _ClassVar[int]
    HOST_VEC_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    DB_TYPE_FIELD_NUMBER: _ClassVar[int]
    SGA_TARGET_SIZE_FIELD_NUMBER: _ClassVar[int]
    SHARED_POOL_SIZE_FIELD_NUMBER: _ClassVar[int]
    TEMP_FILES_COUNT_FIELD_NUMBER: _ClassVar[int]
    FRA_SIZE_FIELD_NUMBER: _ClassVar[int]
    DB_UNIQUE_NAME_FIELD_NUMBER: _ClassVar[int]
    DG_ENTITY_INFO_FIELD_NUMBER: _ClassVar[int]
    DB_DOMAIN_FIELD_NUMBER: _ClassVar[int]
    CDB_ENTITY_INFO_FIELD_NUMBER: _ClassVar[int]
    PDB_ENTITY_INFO_FIELD_NUMBER: _ClassVar[int]
    TDE_ENCRYPTED_TS_COUNT_FIELD_NUMBER: _ClassVar[int]
    OPEN_MODE_FIELD_NUMBER: _ClassVar[int]
    COMPATIBILITY_FIELD_NUMBER: _ClassVar[int]
    MAX_DATAFILES_FIELD_NUMBER: _ClassVar[int]
    MAX_LOG_HISTORY_FIELD_NUMBER: _ClassVar[int]
    MAX_INSTANCES_FIELD_NUMBER: _ClassVar[int]
    MAX_LOGFILES_FIELD_NUMBER: _ClassVar[int]
    MAX_LOGMEMBERS_FIELD_NUMBER: _ClassVar[int]
    CHARACTER_SET_FIELD_NUMBER: _ClassVar[int]
    DB_EDITION_FIELD_NUMBER: _ClassVar[int]
    TEMPFILE_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    SPFILE_PATH_FIELD_NUMBER: _ClassVar[int]
    size_bytes: int
    archivelog_enabled: bool
    bct_enabled: bool
    host_vec: _containers.RepeatedCompositeFieldContainer[Host]
    version: str
    db_type: DBEntityInfo.Type
    sga_target_size: str
    shared_pool_size: str
    temp_files_count: int
    fra_size: int
    db_unique_name: str
    dg_entity_info: DGEntityInfo
    db_domain: str
    cdb_entity_info: CDBEntityInfo
    pdb_entity_info: PDBEntityInfo
    tde_encrypted_ts_count: int
    open_mode: DBEntityInfo.OpenMode
    compatibility: str
    max_datafiles: int
    max_log_history: int
    max_instances: int
    max_logfiles: int
    max_logmembers: int
    character_set: str
    db_edition: DBEntityInfo.Edition
    tempfile_info_vec: _containers.RepeatedCompositeFieldContainer[DBEntityInfo.TempfileInfoRow]
    spfile_path: str
    def __init__(self, size_bytes: _Optional[int] = ..., archivelog_enabled: bool = ..., bct_enabled: bool = ..., host_vec: _Optional[_Iterable[_Union[Host, _Mapping]]] = ..., version: _Optional[str] = ..., db_type: _Optional[_Union[DBEntityInfo.Type, str]] = ..., sga_target_size: _Optional[str] = ..., shared_pool_size: _Optional[str] = ..., temp_files_count: _Optional[int] = ..., fra_size: _Optional[int] = ..., db_unique_name: _Optional[str] = ..., dg_entity_info: _Optional[_Union[DGEntityInfo, _Mapping]] = ..., db_domain: _Optional[str] = ..., cdb_entity_info: _Optional[_Union[CDBEntityInfo, _Mapping]] = ..., pdb_entity_info: _Optional[_Union[PDBEntityInfo, _Mapping]] = ..., tde_encrypted_ts_count: _Optional[int] = ..., open_mode: _Optional[_Union[DBEntityInfo.OpenMode, str]] = ..., compatibility: _Optional[str] = ..., max_datafiles: _Optional[int] = ..., max_log_history: _Optional[int] = ..., max_instances: _Optional[int] = ..., max_logfiles: _Optional[int] = ..., max_logmembers: _Optional[int] = ..., character_set: _Optional[str] = ..., db_edition: _Optional[_Union[DBEntityInfo.Edition, str]] = ..., tempfile_info_vec: _Optional[_Iterable[_Union[DBEntityInfo.TempfileInfoRow, _Mapping]]] = ..., spfile_path: _Optional[str] = ...) -> None: ...

class Entity(_message.Message):
    __slots__ = ("type", "uuid", "name", "db_entity_info", "description", "owner_id", "front_end_size_info")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kRACRootContainer: _ClassVar[Entity.Type]
        kRootContainer: _ClassVar[Entity.Type]
        kHost: _ClassVar[Entity.Type]
        kDatabase: _ClassVar[Entity.Type]
        kTableSpace: _ClassVar[Entity.Type]
        kTable: _ClassVar[Entity.Type]
        kPDB: _ClassVar[Entity.Type]
    kRACRootContainer: Entity.Type
    kRootContainer: Entity.Type
    kHost: Entity.Type
    kDatabase: Entity.Type
    kTableSpace: Entity.Type
    kTable: Entity.Type
    kPDB: Entity.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DB_ENTITY_INFO_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    OWNER_ID_FIELD_NUMBER: _ClassVar[int]
    FRONT_END_SIZE_INFO_FIELD_NUMBER: _ClassVar[int]
    type: Entity.Type
    uuid: str
    name: str
    db_entity_info: DBEntityInfo
    description: str
    owner_id: int
    front_end_size_info: _stats_pb2.SizeInfo
    def __init__(self, type: _Optional[_Union[Entity.Type, str]] = ..., uuid: _Optional[str] = ..., name: _Optional[str] = ..., db_entity_info: _Optional[_Union[DBEntityInfo, _Mapping]] = ..., description: _Optional[str] = ..., owner_id: _Optional[int] = ..., front_end_size_info: _Optional[_Union[_stats_pb2.SizeInfo, _Mapping]] = ...) -> None: ...
