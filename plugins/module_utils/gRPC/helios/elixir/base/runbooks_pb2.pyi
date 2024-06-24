from nexus.eagle_agent.base import pipe_data_pb2 as _pipe_data_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RunbooksKafkaMessage(_message.Message):
    __slots__ = ("cluster_identifier", "runbooks_data", "is_unregistered")
    CLUSTER_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    RUNBOOKS_DATA_FIELD_NUMBER: _ClassVar[int]
    IS_UNREGISTERED_FIELD_NUMBER: _ClassVar[int]
    cluster_identifier: _pipe_data_pb2.ClusterIdentifier
    runbooks_data: bytes
    is_unregistered: bool
    def __init__(self, cluster_identifier: _Optional[_Union[_pipe_data_pb2.ClusterIdentifier, _Mapping]] = ..., runbooks_data: _Optional[bytes] = ..., is_unregistered: bool = ...) -> None: ...
