from open_util.net import protorpc_pb2 as _protorpc_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CreateFileRequest(_message.Message):
    __slots__ = ("filename",)
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    filename: str
    def __init__(self, filename: _Optional[str] = ...) -> None: ...

class CreateFileResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: bool
    def __init__(self, error: bool = ...) -> None: ...

class ReadFileRequest(_message.Message):
    __slots__ = ("filename", "len", "offset")
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    LEN_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    filename: str
    len: int
    offset: int
    def __init__(self, filename: _Optional[str] = ..., len: _Optional[int] = ..., offset: _Optional[int] = ...) -> None: ...

class ReadFileResult(_message.Message):
    __slots__ = ("error", "data", "eof")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    EOF_FIELD_NUMBER: _ClassVar[int]
    error: bool
    data: bytes
    eof: bool
    def __init__(self, error: bool = ..., data: _Optional[bytes] = ..., eof: bool = ...) -> None: ...

class WriteFileRequest(_message.Message):
    __slots__ = ("filename", "content", "offset")
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    filename: str
    content: bytes
    offset: int
    def __init__(self, filename: _Optional[str] = ..., content: _Optional[bytes] = ..., offset: _Optional[int] = ...) -> None: ...

class WriteFileResult(_message.Message):
    __slots__ = ("error", "seq_id")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    SEQ_ID_FIELD_NUMBER: _ClassVar[int]
    error: bool
    seq_id: int
    def __init__(self, error: bool = ..., seq_id: _Optional[int] = ...) -> None: ...
