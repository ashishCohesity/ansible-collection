from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class LivenessProto(_message.Message):
    __slots__ = ("ip", "port", "node_id", "grpc_port")
    IP_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    GRPC_PORT_FIELD_NUMBER: _ClassVar[int]
    ip: str
    port: int
    node_id: int
    grpc_port: int
    def __init__(self, ip: _Optional[str] = ..., port: _Optional[int] = ..., node_id: _Optional[int] = ..., grpc_port: _Optional[int] = ...) -> None: ...
