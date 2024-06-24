from magneto.base.entities import agent_pb2 as _agent_pb2
from magneto.base import error_pb2 as _error_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Entity(_message.Message):
    __slots__ = ("type", "uuid", "cluster_id", "dc_id", "name", "host_address", "description", "network_id", "agent_entity_id", "agent_error", "agent_status")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kOVirtManager: _ClassVar[Entity.Type]
        kStandaloneHost: _ClassVar[Entity.Type]
        kDatacenter: _ClassVar[Entity.Type]
        kCluster: _ClassVar[Entity.Type]
        kHost: _ClassVar[Entity.Type]
        kVirtualMachine: _ClassVar[Entity.Type]
        kNetwork: _ClassVar[Entity.Type]
        kStorageDomain: _ClassVar[Entity.Type]
        kVNicProfile: _ClassVar[Entity.Type]
    kOVirtManager: Entity.Type
    kStandaloneHost: Entity.Type
    kDatacenter: Entity.Type
    kCluster: Entity.Type
    kHost: Entity.Type
    kVirtualMachine: Entity.Type
    kNetwork: Entity.Type
    kStorageDomain: Entity.Type
    kVNicProfile: Entity.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    DC_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    HOST_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    NETWORK_ID_FIELD_NUMBER: _ClassVar[int]
    AGENT_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    AGENT_ERROR_FIELD_NUMBER: _ClassVar[int]
    AGENT_STATUS_FIELD_NUMBER: _ClassVar[int]
    type: Entity.Type
    uuid: str
    cluster_id: str
    dc_id: str
    name: str
    host_address: str
    description: str
    network_id: str
    agent_entity_id: int
    agent_error: _error_pb2.ErrorProto
    agent_status: _agent_pb2.HostAgentStatus
    def __init__(self, type: _Optional[_Union[Entity.Type, str]] = ..., uuid: _Optional[str] = ..., cluster_id: _Optional[str] = ..., dc_id: _Optional[str] = ..., name: _Optional[str] = ..., host_address: _Optional[str] = ..., description: _Optional[str] = ..., network_id: _Optional[str] = ..., agent_entity_id: _Optional[int] = ..., agent_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., agent_status: _Optional[_Union[_agent_pb2.HostAgentStatus, _Mapping]] = ...) -> None: ...
