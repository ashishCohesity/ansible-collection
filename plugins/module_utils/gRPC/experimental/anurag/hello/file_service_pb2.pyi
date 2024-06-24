from open_util.net import protorpc_pb2 as _protorpc_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class FileArgs(_message.Message):
    __slots__ = ("file_name", "fd", "offset", "len")
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    FD_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LEN_FIELD_NUMBER: _ClassVar[int]
    file_name: str
    fd: int
    offset: int
    len: int
    def __init__(self, file_name: _Optional[str] = ..., fd: _Optional[int] = ..., offset: _Optional[int] = ..., len: _Optional[int] = ...) -> None: ...

class FileResponse(_message.Message):
    __slots__ = ("file_response", "fd")
    FILE_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    FD_FIELD_NUMBER: _ClassVar[int]
    file_response: int
    fd: int
    def __init__(self, file_response: _Optional[int] = ..., fd: _Optional[int] = ...) -> None: ...
