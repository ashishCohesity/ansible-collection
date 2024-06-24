from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class WorkqueueWorkerTaskData(_message.Message):
    __slots__ = ("incarnation_id", "payload")
    INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    incarnation_id: int
    payload: bytes
    def __init__(self, incarnation_id: _Optional[int] = ..., payload: _Optional[bytes] = ...) -> None: ...
