from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class RpcIdProto(_message.Message):
    __slots__ = ("bifrost_broker_session_id", "request_id")
    BIFROST_BROKER_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    bifrost_broker_session_id: int
    request_id: int
    def __init__(self, bifrost_broker_session_id: _Optional[int] = ..., request_id: _Optional[int] = ...) -> None: ...
