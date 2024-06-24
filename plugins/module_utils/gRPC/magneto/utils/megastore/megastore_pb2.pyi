from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class MegastoreMetaData(_message.Message):
    __slots__ = ("num_rows",)
    NUM_ROWS_FIELD_NUMBER: _ClassVar[int]
    num_rows: int
    def __init__(self, num_rows: _Optional[int] = ...) -> None: ...
