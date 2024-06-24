from metadata_service.api import api_pb2 as _api_pb2
from metadata_service.base import error_pb2 as _error_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NotifyDetachedNodesArg(_message.Message):
    __slots__ = ("batch_id", "nodes")
    BATCH_ID_FIELD_NUMBER: _ClassVar[int]
    NODES_FIELD_NUMBER: _ClassVar[int]
    batch_id: str
    nodes: _containers.RepeatedCompositeFieldContainer[_api_pb2.NodeProto]
    def __init__(self, batch_id: _Optional[str] = ..., nodes: _Optional[_Iterable[_Union[_api_pb2.NodeProto, _Mapping]]] = ...) -> None: ...

class NotifyDetachedNodesResult(_message.Message):
    __slots__ = ("error", "nodes")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    NODES_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    nodes: _containers.RepeatedCompositeFieldContainer[_api_pb2.NodeProto]
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., nodes: _Optional[_Iterable[_Union[_api_pb2.NodeProto, _Mapping]]] = ...) -> None: ...
