from magneto.base import enums_pb2 as _enums_pb2
from magneto.base import magneto_pb2 as _magneto_pb2
from magneto.base import env_params_pb2 as _env_params_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ConnectorSessionProto(_message.Message):
    __slots__ = ("type", "connector_params", "vmware_session")
    class VMwareSession(_message.Message):
        __slots__ = ("session_id", "version")
        SESSION_ID_FIELD_NUMBER: _ClassVar[int]
        VERSION_FIELD_NUMBER: _ClassVar[int]
        session_id: str
        version: int
        def __init__(self, session_id: _Optional[str] = ..., version: _Optional[int] = ...) -> None: ...
    TYPE_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    VMWARE_SESSION_FIELD_NUMBER: _ClassVar[int]
    type: _enums_pb2.Environment.Type
    connector_params: _magneto_pb2.ConnectorParams
    vmware_session: ConnectorSessionProto.VMwareSession
    def __init__(self, type: _Optional[_Union[_enums_pb2.Environment.Type, str]] = ..., connector_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ..., vmware_session: _Optional[_Union[ConnectorSessionProto.VMwareSession, _Mapping]] = ...) -> None: ...

class ConnectorSessions(_message.Message):
    __slots__ = ("sessions",)
    SESSIONS_FIELD_NUMBER: _ClassVar[int]
    sessions: _containers.RepeatedCompositeFieldContainer[ConnectorSessionProto]
    def __init__(self, sessions: _Optional[_Iterable[_Union[ConnectorSessionProto, _Mapping]]] = ...) -> None: ...
