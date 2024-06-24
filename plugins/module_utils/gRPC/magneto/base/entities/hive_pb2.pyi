from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ClusterInfo(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DatabaseInfo(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class TableInfo(_message.Message):
    __slots__ = ("approx_size_bytes", "table_type", "is_transactional_table", "owner", "created_on")
    class TableType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MANAGED_TABLE: _ClassVar[TableInfo.TableType]
        EXTERNAL_TABLE: _ClassVar[TableInfo.TableType]
        VIRTUAL_VIEW: _ClassVar[TableInfo.TableType]
        INDEX_TABLE: _ClassVar[TableInfo.TableType]
    MANAGED_TABLE: TableInfo.TableType
    EXTERNAL_TABLE: TableInfo.TableType
    VIRTUAL_VIEW: TableInfo.TableType
    INDEX_TABLE: TableInfo.TableType
    APPROX_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    TABLE_TYPE_FIELD_NUMBER: _ClassVar[int]
    IS_TRANSACTIONAL_TABLE_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    CREATED_ON_FIELD_NUMBER: _ClassVar[int]
    approx_size_bytes: int
    table_type: TableInfo.TableType
    is_transactional_table: bool
    owner: str
    created_on: int
    def __init__(self, approx_size_bytes: _Optional[int] = ..., table_type: _Optional[_Union[TableInfo.TableType, str]] = ..., is_transactional_table: bool = ..., owner: _Optional[str] = ..., created_on: _Optional[int] = ...) -> None: ...

class Entity(_message.Message):
    __slots__ = ("type", "name", "uuid", "cluster_info", "database_info", "table_info")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kCluster: _ClassVar[Entity.Type]
        kDatabase: _ClassVar[Entity.Type]
        kTable: _ClassVar[Entity.Type]
    kCluster: Entity.Type
    kDatabase: Entity.Type
    kTable: Entity.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_INFO_FIELD_NUMBER: _ClassVar[int]
    DATABASE_INFO_FIELD_NUMBER: _ClassVar[int]
    TABLE_INFO_FIELD_NUMBER: _ClassVar[int]
    type: Entity.Type
    name: str
    uuid: str
    cluster_info: ClusterInfo
    database_info: DatabaseInfo
    table_info: TableInfo
    def __init__(self, type: _Optional[_Union[Entity.Type, str]] = ..., name: _Optional[str] = ..., uuid: _Optional[str] = ..., cluster_info: _Optional[_Union[ClusterInfo, _Mapping]] = ..., database_info: _Optional[_Union[DatabaseInfo, _Mapping]] = ..., table_info: _Optional[_Union[TableInfo, _Mapping]] = ...) -> None: ...
