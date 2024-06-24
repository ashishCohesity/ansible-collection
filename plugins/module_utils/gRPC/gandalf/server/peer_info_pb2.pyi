from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PeerInfoProto(_message.Message):
    __slots__ = ("node_id", "ip_addr_str", "port", "liveness_namespace")
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    IP_ADDR_STR_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    LIVENESS_NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    node_id: int
    ip_addr_str: str
    port: int
    liveness_namespace: str
    def __init__(self, node_id: _Optional[int] = ..., ip_addr_str: _Optional[str] = ..., port: _Optional[int] = ..., liveness_namespace: _Optional[str] = ...) -> None: ...
