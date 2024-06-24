from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ClusterInfo(_message.Message):
    __slots__ = ("seeds",)
    SEEDS_FIELD_NUMBER: _ClassVar[int]
    seeds: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, seeds: _Optional[_Iterable[str]] = ...) -> None: ...

class DatabaseInfo(_message.Message):
    __slots__ = ("size_bytes",)
    SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    size_bytes: int
    def __init__(self, size_bytes: _Optional[int] = ...) -> None: ...

class CollectionInfo(_message.Message):
    __slots__ = ("size_bytes", "is_mongo_view", "is_capped_collection", "is_timeseries_collection")
    SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    IS_MONGO_VIEW_FIELD_NUMBER: _ClassVar[int]
    IS_CAPPED_COLLECTION_FIELD_NUMBER: _ClassVar[int]
    IS_TIMESERIES_COLLECTION_FIELD_NUMBER: _ClassVar[int]
    size_bytes: int
    is_mongo_view: bool
    is_capped_collection: bool
    is_timeseries_collection: bool
    def __init__(self, size_bytes: _Optional[int] = ..., is_mongo_view: bool = ..., is_capped_collection: bool = ..., is_timeseries_collection: bool = ...) -> None: ...

class Entity(_message.Message):
    __slots__ = ("type", "name", "uuid", "cluster_info", "database_info", "collection_info")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kCluster: _ClassVar[Entity.Type]
        kDatabase: _ClassVar[Entity.Type]
        kCollection: _ClassVar[Entity.Type]
    kCluster: Entity.Type
    kDatabase: Entity.Type
    kCollection: Entity.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_INFO_FIELD_NUMBER: _ClassVar[int]
    DATABASE_INFO_FIELD_NUMBER: _ClassVar[int]
    COLLECTION_INFO_FIELD_NUMBER: _ClassVar[int]
    type: Entity.Type
    name: str
    uuid: str
    cluster_info: ClusterInfo
    database_info: DatabaseInfo
    collection_info: CollectionInfo
    def __init__(self, type: _Optional[_Union[Entity.Type, str]] = ..., name: _Optional[str] = ..., uuid: _Optional[str] = ..., cluster_info: _Optional[_Union[ClusterInfo, _Mapping]] = ..., database_info: _Optional[_Union[DatabaseInfo, _Mapping]] = ..., collection_info: _Optional[_Union[CollectionInfo, _Mapping]] = ...) -> None: ...
