from open_util.net import protorpc_pb2 as _protorpc_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class HelloRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class HelloResult(_message.Message):
    __slots__ = ("greeting",)
    GREETING_FIELD_NUMBER: _ClassVar[int]
    greeting: str
    def __init__(self, greeting: _Optional[str] = ...) -> None: ...

class CreateFileRequest(_message.Message):
    __slots__ = ("filename",)
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    filename: str
    def __init__(self, filename: _Optional[str] = ...) -> None: ...

class CreateFileResult(_message.Message):
    __slots__ = ("success", "response", "operationid")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    OPERATIONID_FIELD_NUMBER: _ClassVar[int]
    success: bool
    response: str
    operationid: int
    def __init__(self, success: bool = ..., response: _Optional[str] = ..., operationid: _Optional[int] = ...) -> None: ...

class ReadFileRangeRequest(_message.Message):
    __slots__ = ("filename", "offset", "len")
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LEN_FIELD_NUMBER: _ClassVar[int]
    filename: str
    offset: int
    len: int
    def __init__(self, filename: _Optional[str] = ..., offset: _Optional[int] = ..., len: _Optional[int] = ...) -> None: ...

class ReadFileRangeResult(_message.Message):
    __slots__ = ("success", "response", "operationId")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    OPERATIONID_FIELD_NUMBER: _ClassVar[int]
    success: bool
    response: str
    operationId: int
    def __init__(self, success: bool = ..., response: _Optional[str] = ..., operationId: _Optional[int] = ...) -> None: ...

class WriteFileRangeRequest(_message.Message):
    __slots__ = ("filename", "offset", "len")
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LEN_FIELD_NUMBER: _ClassVar[int]
    filename: str
    offset: int
    len: int
    def __init__(self, filename: _Optional[str] = ..., offset: _Optional[int] = ..., len: _Optional[int] = ...) -> None: ...

class WriteFileRangeResult(_message.Message):
    __slots__ = ("success", "response", "operationId")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    OPERATIONID_FIELD_NUMBER: _ClassVar[int]
    success: bool
    response: str
    operationId: int
    def __init__(self, success: bool = ..., response: _Optional[str] = ..., operationId: _Optional[int] = ...) -> None: ...
