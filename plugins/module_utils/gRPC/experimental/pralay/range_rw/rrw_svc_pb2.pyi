from open_util.net import protorpc_pb2 as _protorpc_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CreateFileReq(_message.Message):
    __slots__ = ("filename",)
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    filename: str
    def __init__(self, filename: _Optional[str] = ...) -> None: ...

class CreateFileResp(_message.Message):
    __slots__ = ("errcode",)
    ERRCODE_FIELD_NUMBER: _ClassVar[int]
    errcode: int
    def __init__(self, errcode: _Optional[int] = ...) -> None: ...

class FileReadReq(_message.Message):
    __slots__ = ("filename", "offset", "len")
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LEN_FIELD_NUMBER: _ClassVar[int]
    filename: str
    offset: int
    len: int
    def __init__(self, filename: _Optional[str] = ..., offset: _Optional[int] = ..., len: _Optional[int] = ...) -> None: ...

class FileReadResp(_message.Message):
    __slots__ = ("errcode", "data", "wr_seq_marker")
    ERRCODE_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    WR_SEQ_MARKER_FIELD_NUMBER: _ClassVar[int]
    errcode: int
    data: bytes
    wr_seq_marker: int
    def __init__(self, errcode: _Optional[int] = ..., data: _Optional[bytes] = ..., wr_seq_marker: _Optional[int] = ...) -> None: ...

class FileWriteReq(_message.Message):
    __slots__ = ("filename", "offset", "data")
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    filename: str
    offset: int
    data: bytes
    def __init__(self, filename: _Optional[str] = ..., offset: _Optional[int] = ..., data: _Optional[bytes] = ...) -> None: ...

class FileWriteResp(_message.Message):
    __slots__ = ("errcode", "len", "wr_seq")
    ERRCODE_FIELD_NUMBER: _ClassVar[int]
    LEN_FIELD_NUMBER: _ClassVar[int]
    WR_SEQ_FIELD_NUMBER: _ClassVar[int]
    errcode: int
    len: int
    wr_seq: int
    def __init__(self, errcode: _Optional[int] = ..., len: _Optional[int] = ..., wr_seq: _Optional[int] = ...) -> None: ...
