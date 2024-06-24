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

class BucketInfo(_message.Message):
    __slots__ = ("document_count", "bucket_type")
    DOCUMENT_COUNT_FIELD_NUMBER: _ClassVar[int]
    BUCKET_TYPE_FIELD_NUMBER: _ClassVar[int]
    document_count: int
    bucket_type: str
    def __init__(self, document_count: _Optional[int] = ..., bucket_type: _Optional[str] = ...) -> None: ...

class Entity(_message.Message):
    __slots__ = ("type", "name", "uuid", "cluster_info", "bucket_info")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kCluster: _ClassVar[Entity.Type]
        kBucket: _ClassVar[Entity.Type]
    kCluster: Entity.Type
    kBucket: Entity.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_INFO_FIELD_NUMBER: _ClassVar[int]
    BUCKET_INFO_FIELD_NUMBER: _ClassVar[int]
    type: Entity.Type
    name: str
    uuid: str
    cluster_info: ClusterInfo
    bucket_info: BucketInfo
    def __init__(self, type: _Optional[_Union[Entity.Type, str]] = ..., name: _Optional[str] = ..., uuid: _Optional[str] = ..., cluster_info: _Optional[_Union[ClusterInfo, _Mapping]] = ..., bucket_info: _Optional[_Union[BucketInfo, _Mapping]] = ...) -> None: ...
