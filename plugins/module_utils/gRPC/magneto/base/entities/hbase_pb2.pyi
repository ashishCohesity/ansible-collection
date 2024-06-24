from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ClusterInfo(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class NamespaceInfo(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class TableInfo(_message.Message):
    __slots__ = ("approx_size_bytes",)
    APPROX_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    approx_size_bytes: int
    def __init__(self, approx_size_bytes: _Optional[int] = ...) -> None: ...

class Entity(_message.Message):
    __slots__ = ("type", "name", "uuid", "cluster_info", "namespace_info", "table_info")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kCluster: _ClassVar[Entity.Type]
        kNamespace: _ClassVar[Entity.Type]
        kTable: _ClassVar[Entity.Type]
    kCluster: Entity.Type
    kNamespace: Entity.Type
    kTable: Entity.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_INFO_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_INFO_FIELD_NUMBER: _ClassVar[int]
    TABLE_INFO_FIELD_NUMBER: _ClassVar[int]
    type: Entity.Type
    name: str
    uuid: str
    cluster_info: ClusterInfo
    namespace_info: NamespaceInfo
    table_info: TableInfo
    def __init__(self, type: _Optional[_Union[Entity.Type, str]] = ..., name: _Optional[str] = ..., uuid: _Optional[str] = ..., cluster_info: _Optional[_Union[ClusterInfo, _Mapping]] = ..., namespace_info: _Optional[_Union[NamespaceInfo, _Mapping]] = ..., table_info: _Optional[_Union[TableInfo, _Mapping]] = ...) -> None: ...
