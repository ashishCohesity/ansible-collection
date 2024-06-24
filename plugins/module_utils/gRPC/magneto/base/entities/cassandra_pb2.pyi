from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ClusterInfo(_message.Message):
    __slots__ = ("primary_host", "seed_vec")
    PRIMARY_HOST_FIELD_NUMBER: _ClassVar[int]
    SEED_VEC_FIELD_NUMBER: _ClassVar[int]
    primary_host: str
    seed_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, primary_host: _Optional[str] = ..., seed_vec: _Optional[_Iterable[str]] = ...) -> None: ...

class GraphKeyspaceInfo(_message.Message):
    __slots__ = ("associated_keyspace_vec",)
    ASSOCIATED_KEYSPACE_VEC_FIELD_NUMBER: _ClassVar[int]
    associated_keyspace_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, associated_keyspace_vec: _Optional[_Iterable[str]] = ...) -> None: ...

class KeyspaceInfo(_message.Message):
    __slots__ = ("children_count", "replication_strategy", "dc_list", "keyspace_type", "graph_info")
    class ReplicationStrategy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kSimple: _ClassVar[KeyspaceInfo.ReplicationStrategy]
        kNetwork: _ClassVar[KeyspaceInfo.ReplicationStrategy]
        kUnsupported: _ClassVar[KeyspaceInfo.ReplicationStrategy]
    kSimple: KeyspaceInfo.ReplicationStrategy
    kNetwork: KeyspaceInfo.ReplicationStrategy
    kUnsupported: KeyspaceInfo.ReplicationStrategy
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kRegular: _ClassVar[KeyspaceInfo.Type]
        kGraph: _ClassVar[KeyspaceInfo.Type]
        kSystem: _ClassVar[KeyspaceInfo.Type]
    kRegular: KeyspaceInfo.Type
    kGraph: KeyspaceInfo.Type
    kSystem: KeyspaceInfo.Type
    CHILDREN_COUNT_FIELD_NUMBER: _ClassVar[int]
    REPLICATION_STRATEGY_FIELD_NUMBER: _ClassVar[int]
    DC_LIST_FIELD_NUMBER: _ClassVar[int]
    KEYSPACE_TYPE_FIELD_NUMBER: _ClassVar[int]
    GRAPH_INFO_FIELD_NUMBER: _ClassVar[int]
    children_count: int
    replication_strategy: KeyspaceInfo.ReplicationStrategy
    dc_list: _containers.RepeatedScalarFieldContainer[str]
    keyspace_type: KeyspaceInfo.Type
    graph_info: GraphKeyspaceInfo
    def __init__(self, children_count: _Optional[int] = ..., replication_strategy: _Optional[_Union[KeyspaceInfo.ReplicationStrategy, str]] = ..., dc_list: _Optional[_Iterable[str]] = ..., keyspace_type: _Optional[_Union[KeyspaceInfo.Type, str]] = ..., graph_info: _Optional[_Union[GraphKeyspaceInfo, _Mapping]] = ...) -> None: ...

class TableInfo(_message.Message):
    __slots__ = ("table_type",)
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kRegular: _ClassVar[TableInfo.Type]
        kGraph: _ClassVar[TableInfo.Type]
        kSystem: _ClassVar[TableInfo.Type]
    kRegular: TableInfo.Type
    kGraph: TableInfo.Type
    kSystem: TableInfo.Type
    TABLE_TYPE_FIELD_NUMBER: _ClassVar[int]
    table_type: TableInfo.Type
    def __init__(self, table_type: _Optional[_Union[TableInfo.Type, str]] = ...) -> None: ...

class Entity(_message.Message):
    __slots__ = ("type", "name", "uuid", "cluster_info", "keyspace_info", "table_info")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kCluster: _ClassVar[Entity.Type]
        kKeyspace: _ClassVar[Entity.Type]
        kTable: _ClassVar[Entity.Type]
    kCluster: Entity.Type
    kKeyspace: Entity.Type
    kTable: Entity.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_INFO_FIELD_NUMBER: _ClassVar[int]
    KEYSPACE_INFO_FIELD_NUMBER: _ClassVar[int]
    TABLE_INFO_FIELD_NUMBER: _ClassVar[int]
    type: Entity.Type
    name: str
    uuid: str
    cluster_info: ClusterInfo
    keyspace_info: KeyspaceInfo
    table_info: TableInfo
    def __init__(self, type: _Optional[_Union[Entity.Type, str]] = ..., name: _Optional[str] = ..., uuid: _Optional[str] = ..., cluster_info: _Optional[_Union[ClusterInfo, _Mapping]] = ..., keyspace_info: _Optional[_Union[KeyspaceInfo, _Mapping]] = ..., table_info: _Optional[_Union[TableInfo, _Mapping]] = ...) -> None: ...
