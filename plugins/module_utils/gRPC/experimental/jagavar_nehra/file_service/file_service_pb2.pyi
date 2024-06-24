from open_util.net import protorpc_pb2 as _protorpc_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CreateRequest(_message.Message):
    __slots__ = ("filename",)
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    filename: str
    def __init__(self, filename: _Optional[str] = ...) -> None: ...

class CreateResult(_message.Message):
    __slots__ = ("success",)
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    def __init__(self, success: bool = ...) -> None: ...

class ReadRequest(_message.Message):
    __slots__ = ("filename", "offset", "len")
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LEN_FIELD_NUMBER: _ClassVar[int]
    filename: str
    offset: int
    len: int
    def __init__(self, filename: _Optional[str] = ..., offset: _Optional[int] = ..., len: _Optional[int] = ...) -> None: ...

class ReadResult(_message.Message):
    __slots__ = ("success", "seq_id")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    SEQ_ID_FIELD_NUMBER: _ClassVar[int]
    success: bool
    seq_id: int
    def __init__(self, success: bool = ..., seq_id: _Optional[int] = ...) -> None: ...

class WriteRequest(_message.Message):
    __slots__ = ("filename", "offset")
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    filename: str
    offset: int
    def __init__(self, filename: _Optional[str] = ..., offset: _Optional[int] = ...) -> None: ...

class WriteResult(_message.Message):
    __slots__ = ("success", "seq_id")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    SEQ_ID_FIELD_NUMBER: _ClassVar[int]
    success: bool
    seq_id: int
    def __init__(self, success: bool = ..., seq_id: _Optional[int] = ...) -> None: ...
