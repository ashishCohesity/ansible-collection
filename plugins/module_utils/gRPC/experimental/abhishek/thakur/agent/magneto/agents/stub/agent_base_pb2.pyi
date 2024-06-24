from magneto.agents.base import error_pb2 as _error_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AgentBaseArg(_message.Message):
    __slots__ = ("task_id", "client_agent_api_version", "agent_incarnation_id", "cluster_id", "cluster_incarnation_id")
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_AGENT_API_VERSION_FIELD_NUMBER: _ClassVar[int]
    AGENT_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    task_id: int
    client_agent_api_version: int
    agent_incarnation_id: int
    cluster_id: int
    cluster_incarnation_id: int
    def __init__(self, task_id: _Optional[int] = ..., client_agent_api_version: _Optional[int] = ..., agent_incarnation_id: _Optional[int] = ..., cluster_id: _Optional[int] = ..., cluster_incarnation_id: _Optional[int] = ...) -> None: ...

class Result(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...
