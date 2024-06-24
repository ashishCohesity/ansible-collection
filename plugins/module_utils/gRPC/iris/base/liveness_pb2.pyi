from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class LivenessProto(_message.Message):
    __slots__ = ("node_id", "ip", "port", "Iris_namespace")
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    IP_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    IRIS_NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    node_id: int
    ip: str
    port: int
    Iris_namespace: str
    def __init__(self, node_id: _Optional[int] = ..., ip: _Optional[str] = ..., port: _Optional[int] = ..., Iris_namespace: _Optional[str] = ...) -> None: ...
