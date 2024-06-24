from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class LogCheckPointProto(_message.Message):
    __slots__ = ("node_id", "file_name", "start_offset_bytes")
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    START_OFFSET_BYTES_FIELD_NUMBER: _ClassVar[int]
    node_id: int
    file_name: bytes
    start_offset_bytes: int
    def __init__(self, node_id: _Optional[int] = ..., file_name: _Optional[bytes] = ..., start_offset_bytes: _Optional[int] = ...) -> None: ...
