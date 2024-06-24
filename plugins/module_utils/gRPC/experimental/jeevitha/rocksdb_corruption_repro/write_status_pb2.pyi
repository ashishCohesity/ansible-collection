from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class WriteStatus(_message.Message):
    __slots__ = ("next_key", "num_keys_deleted")
    NEXT_KEY_FIELD_NUMBER: _ClassVar[int]
    NUM_KEYS_DELETED_FIELD_NUMBER: _ClassVar[int]
    next_key: int
    num_keys_deleted: int
    def __init__(self, next_key: _Optional[int] = ..., num_keys_deleted: _Optional[int] = ...) -> None: ...
