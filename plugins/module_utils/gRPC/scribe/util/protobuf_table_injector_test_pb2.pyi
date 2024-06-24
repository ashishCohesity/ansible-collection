from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Key(_message.Message):
    __slots__ = ("column_0_key", "column_1_key")
    COLUMN_0_KEY_FIELD_NUMBER: _ClassVar[int]
    COLUMN_1_KEY_FIELD_NUMBER: _ClassVar[int]
    column_0_key: int
    column_1_key: str
    def __init__(self, column_0_key: _Optional[int] = ..., column_1_key: _Optional[str] = ...) -> None: ...

class Column0(_message.Message):
    __slots__ = ("column_0_content",)
    COLUMN_0_CONTENT_FIELD_NUMBER: _ClassVar[int]
    column_0_content: int
    def __init__(self, column_0_content: _Optional[int] = ...) -> None: ...

class Column1(_message.Message):
    __slots__ = ("column_1_content",)
    COLUMN_1_CONTENT_FIELD_NUMBER: _ClassVar[int]
    column_1_content: str
    def __init__(self, column_1_content: _Optional[str] = ...) -> None: ...
