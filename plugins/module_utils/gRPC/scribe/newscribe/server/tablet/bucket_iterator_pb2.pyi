from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class IteratorPositionProto(_message.Message):
    __slots__ = ("is_at_end", "table", "current_db_key")
    IS_AT_END_FIELD_NUMBER: _ClassVar[int]
    TABLE_FIELD_NUMBER: _ClassVar[int]
    CURRENT_DB_KEY_FIELD_NUMBER: _ClassVar[int]
    is_at_end: bool
    table: int
    current_db_key: bytes
    def __init__(self, is_at_end: bool = ..., table: _Optional[int] = ..., current_db_key: _Optional[bytes] = ...) -> None: ...
