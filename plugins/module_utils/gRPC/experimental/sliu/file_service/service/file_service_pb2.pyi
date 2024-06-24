from open_util.net import protorpc_pb2 as _protorpc_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CreateFileRequest(_message.Message):
    __slots__ = ("file_name",)
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    file_name: str
    def __init__(self, file_name: _Optional[str] = ...) -> None: ...

class ReadFileRangeRequest(_message.Message):
    __slots__ = ("file_name", "offset", "length")
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    file_name: str
    offset: int
    length: int
    def __init__(self, file_name: _Optional[str] = ..., offset: _Optional[int] = ..., length: _Optional[int] = ...) -> None: ...

class WriteFileRangeRequest(_message.Message):
    __slots__ = ("file_name", "offset", "data")
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    file_name: str
    offset: int
    data: str
    def __init__(self, file_name: _Optional[str] = ..., offset: _Optional[int] = ..., data: _Optional[str] = ...) -> None: ...

class FileOpResponse(_message.Message):
    __slots__ = ("ret_code", "op_order", "data", "error_msg")
    RET_CODE_FIELD_NUMBER: _ClassVar[int]
    OP_ORDER_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    ERROR_MSG_FIELD_NUMBER: _ClassVar[int]
    ret_code: int
    op_order: int
    data: str
    error_msg: str
    def __init__(self, ret_code: _Optional[int] = ..., op_order: _Optional[int] = ..., data: _Optional[str] = ..., error_msg: _Optional[str] = ...) -> None: ...

class EmptyMessage(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
