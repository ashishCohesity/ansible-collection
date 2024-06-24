from open_util.net import protorpc_pb2 as _protorpc_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class FileRequest(_message.Message):
    __slots__ = ("file_name", "file_desc", "num_bytes_rw", "offset")
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    FILE_DESC_FIELD_NUMBER: _ClassVar[int]
    NUM_BYTES_RW_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    file_name: str
    file_desc: int
    num_bytes_rw: int
    offset: int
    def __init__(self, file_name: _Optional[str] = ..., file_desc: _Optional[int] = ..., num_bytes_rw: _Optional[int] = ..., offset: _Optional[int] = ...) -> None: ...

class FileResponse(_message.Message):
    __slots__ = ("file_name", "file_desc", "num_bytes_rw", "offset")
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    FILE_DESC_FIELD_NUMBER: _ClassVar[int]
    NUM_BYTES_RW_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    file_name: str
    file_desc: int
    num_bytes_rw: int
    offset: int
    def __init__(self, file_name: _Optional[str] = ..., file_desc: _Optional[int] = ..., num_bytes_rw: _Optional[int] = ..., offset: _Optional[int] = ...) -> None: ...
