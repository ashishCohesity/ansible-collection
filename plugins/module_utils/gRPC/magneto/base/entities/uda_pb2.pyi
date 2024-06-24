from magneto.base.entities import agent_pb2 as _agent_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ClusterInfo(_message.Message):
    __slots__ = ("hosts",)
    HOSTS_FIELD_NUMBER: _ClassVar[int]
    hosts: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, hosts: _Optional[_Iterable[str]] = ...) -> None: ...

class ObjectInfo(_message.Message):
    __slots__ = ("is_leaf", "object_type")
    IS_LEAF_FIELD_NUMBER: _ClassVar[int]
    OBJECT_TYPE_FIELD_NUMBER: _ClassVar[int]
    is_leaf: bool
    object_type: str
    def __init__(self, is_leaf: bool = ..., object_type: _Optional[str] = ...) -> None: ...

class Entity(_message.Message):
    __slots__ = ("type", "name", "uuid", "cluster_info", "object_info", "agent_status_vec", "source_type")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kCluster: _ClassVar[Entity.Type]
        kObject: _ClassVar[Entity.Type]
    kCluster: Entity.Type
    kObject: Entity.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_INFO_FIELD_NUMBER: _ClassVar[int]
    OBJECT_INFO_FIELD_NUMBER: _ClassVar[int]
    AGENT_STATUS_VEC_FIELD_NUMBER: _ClassVar[int]
    SOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    type: Entity.Type
    name: str
    uuid: str
    cluster_info: ClusterInfo
    object_info: ObjectInfo
    agent_status_vec: _containers.RepeatedCompositeFieldContainer[_agent_pb2.HostAgentStatus]
    source_type: str
    def __init__(self, type: _Optional[_Union[Entity.Type, str]] = ..., name: _Optional[str] = ..., uuid: _Optional[str] = ..., cluster_info: _Optional[_Union[ClusterInfo, _Mapping]] = ..., object_info: _Optional[_Union[ObjectInfo, _Mapping]] = ..., agent_status_vec: _Optional[_Iterable[_Union[_agent_pb2.HostAgentStatus, _Mapping]]] = ..., source_type: _Optional[str] = ...) -> None: ...
