from open_util.net import protorpc_pb2 as _protorpc_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CreateRequest(_message.Message):
    __slots__ = ("file_name",)
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    file_name: str
    def __init__(self, file_name: _Optional[str] = ...) -> None: ...

class CreateResponse(_message.Message):
    __slots__ = ("response", "counter")
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    COUNTER_FIELD_NUMBER: _ClassVar[int]
    response: str
    counter: int
    def __init__(self, response: _Optional[str] = ..., counter: _Optional[int] = ...) -> None: ...

class WriteRequest(_message.Message):
    __slots__ = ("file_name", "content", "offset")
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    file_name: str
    content: str
    offset: int
    def __init__(self, file_name: _Optional[str] = ..., content: _Optional[str] = ..., offset: _Optional[int] = ...) -> None: ...

class WriteResponse(_message.Message):
    __slots__ = ("response", "counter")
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    COUNTER_FIELD_NUMBER: _ClassVar[int]
    response: str
    counter: int
    def __init__(self, response: _Optional[str] = ..., counter: _Optional[int] = ...) -> None: ...

class ReadRequest(_message.Message):
    __slots__ = ("file_name", "len", "offset")
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    LEN_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    file_name: str
    len: int
    offset: int
    def __init__(self, file_name: _Optional[str] = ..., len: _Optional[int] = ..., offset: _Optional[int] = ...) -> None: ...

class ReadResponse(_message.Message):
    __slots__ = ("response", "counter", "content")
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    COUNTER_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    response: str
    counter: int
    content: str
    def __init__(self, response: _Optional[str] = ..., counter: _Optional[int] = ..., content: _Optional[str] = ...) -> None: ...
