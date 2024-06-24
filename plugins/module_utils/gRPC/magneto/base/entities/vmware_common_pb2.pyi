from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class MORef(_message.Message):
    __slots__ = ("item", "type")
    ITEM_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    item: str
    type: str
    def __init__(self, item: _Optional[str] = ..., type: _Optional[str] = ...) -> None: ...
