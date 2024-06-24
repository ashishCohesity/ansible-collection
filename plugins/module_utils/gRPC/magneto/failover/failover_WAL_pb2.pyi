from magneto.failover import failover_state_pb2 as _failover_state_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class WALRecordProto(_message.Message):
    __slots__ = ("failover_service_version", "failover_state_vec", "add_or_update_failover_state", "delete_failover_state")
    FAILOVER_SERVICE_VERSION_FIELD_NUMBER: _ClassVar[int]
    FAILOVER_STATE_VEC_FIELD_NUMBER: _ClassVar[int]
    ADD_OR_UPDATE_FAILOVER_STATE_FIELD_NUMBER: _ClassVar[int]
    DELETE_FAILOVER_STATE_FIELD_NUMBER: _ClassVar[int]
    failover_service_version: _failover_state_pb2.FailoverVersionProto
    failover_state_vec: _containers.RepeatedCompositeFieldContainer[_failover_state_pb2.FailoverStateProto]
    add_or_update_failover_state: _failover_state_pb2.FailoverStateProto
    delete_failover_state: str
    def __init__(self, failover_service_version: _Optional[_Union[_failover_state_pb2.FailoverVersionProto, _Mapping]] = ..., failover_state_vec: _Optional[_Iterable[_Union[_failover_state_pb2.FailoverStateProto, _Mapping]]] = ..., add_or_update_failover_state: _Optional[_Union[_failover_state_pb2.FailoverStateProto, _Mapping]] = ..., delete_failover_state: _Optional[str] = ...) -> None: ...
