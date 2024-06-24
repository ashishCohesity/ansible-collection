from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class InternodeTunnelPayload(_message.Message):
    __slots__ = ("target_endpoint", "payload")
    TARGET_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    target_endpoint: str
    payload: bytes
    def __init__(self, target_endpoint: _Optional[str] = ..., payload: _Optional[bytes] = ...) -> None: ...
