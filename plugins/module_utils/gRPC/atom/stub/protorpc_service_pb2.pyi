from atom.base import atom_pb2 as _atom_pb2
from atom.base import entity_pb2 as _entity_pb2
from atom.base import event_pb2 as _event_pb2
from atom.stub import rpc_service_args_pb2 as _rpc_service_args_pb2
from open_util.net import protorpc_pb2 as _protorpc_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ReplicateEventsArg(_message.Message):
    __slots__ = ("entity_id", "data_event_vec")
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    DATA_EVENT_VEC_FIELD_NUMBER: _ClassVar[int]
    entity_id: _entity_pb2.EntityID
    data_event_vec: _containers.RepeatedCompositeFieldContainer[_event_pb2.DataEvent]
    def __init__(self, entity_id: _Optional[_Union[_entity_pb2.EntityID, _Mapping]] = ..., data_event_vec: _Optional[_Iterable[_Union[_event_pb2.DataEvent, _Mapping]]] = ...) -> None: ...

class ReplicateEventsResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
