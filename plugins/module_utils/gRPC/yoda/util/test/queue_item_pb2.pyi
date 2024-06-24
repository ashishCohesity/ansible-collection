from yoda.util import work_item_pb2 as _work_item_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class TestWorkItem(_message.Message):
    __slots__ = ("work",)
    WORK_ITEM_EXT_FIELD_NUMBER: _ClassVar[int]
    work_item_ext: _descriptor.FieldDescriptor
    WORK_FIELD_NUMBER: _ClassVar[int]
    work: str
    def __init__(self, work: _Optional[str] = ...) -> None: ...
