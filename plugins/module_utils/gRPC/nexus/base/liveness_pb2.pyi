from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class LivenessProto(_message.Message):
    __slots__ = ("ip", "nexus_port", "nexus_proxy_port", "nexus_namespace", "node_id", "down_interface_names")
    IP_FIELD_NUMBER: _ClassVar[int]
    NEXUS_PORT_FIELD_NUMBER: _ClassVar[int]
    NEXUS_PROXY_PORT_FIELD_NUMBER: _ClassVar[int]
    NEXUS_NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    DOWN_INTERFACE_NAMES_FIELD_NUMBER: _ClassVar[int]
    ip: str
    nexus_port: int
    nexus_proxy_port: int
    nexus_namespace: str
    node_id: int
    down_interface_names: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, ip: _Optional[str] = ..., nexus_port: _Optional[int] = ..., nexus_proxy_port: _Optional[int] = ..., nexus_namespace: _Optional[str] = ..., node_id: _Optional[int] = ..., down_interface_names: _Optional[_Iterable[str]] = ...) -> None: ...
