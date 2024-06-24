from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class LivenessProto(_message.Message):
    __slots__ = ("ip", "port", "storage_proxy_namespace", "storage_proxy_fleet_namespace")
    IP_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    STORAGE_PROXY_NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    STORAGE_PROXY_FLEET_NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    ip: str
    port: int
    storage_proxy_namespace: str
    storage_proxy_fleet_namespace: str
    def __init__(self, ip: _Optional[str] = ..., port: _Optional[int] = ..., storage_proxy_namespace: _Optional[str] = ..., storage_proxy_fleet_namespace: _Optional[str] = ...) -> None: ...
