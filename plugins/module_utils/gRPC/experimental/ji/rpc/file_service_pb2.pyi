from open_util.net import protorpc_pb2 as _protorpc_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateFileRequest(_message.Message):
    __slots__ = ("filename", "len", "offset", "content")
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    LEN_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    filename: str
    len: int
    offset: int
    content: str
    def __init__(self, filename: _Optional[str] = ..., len: _Optional[int] = ..., offset: _Optional[int] = ..., content: _Optional[str] = ...) -> None: ...

class CreateFileResult(_message.Message):
    __slots__ = ("response", "content", "num")
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    NUM_FIELD_NUMBER: _ClassVar[int]
    response: bool
    content: str
    num: int
    def __init__(self, response: bool = ..., content: _Optional[str] = ..., num: _Optional[int] = ...) -> None: ...

class ReadFileRequest(_message.Message):
    __slots__ = ("filename", "len", "offset", "content")
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    LEN_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    filename: str
    len: int
    offset: int
    content: str
    def __init__(self, filename: _Optional[str] = ..., len: _Optional[int] = ..., offset: _Optional[int] = ..., content: _Optional[str] = ...) -> None: ...

class ReadFileResult(_message.Message):
    __slots__ = ("response", "content", "num")
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    NUM_FIELD_NUMBER: _ClassVar[int]
    response: bool
    content: str
    num: int
    def __init__(self, response: bool = ..., content: _Optional[str] = ..., num: _Optional[int] = ...) -> None: ...

class WriteFileRequest(_message.Message):
    __slots__ = ("filename", "len", "offset", "content")
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    LEN_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    filename: str
    len: int
    offset: int
    content: str
    def __init__(self, filename: _Optional[str] = ..., len: _Optional[int] = ..., offset: _Optional[int] = ..., content: _Optional[str] = ...) -> None: ...

class WriteFileResult(_message.Message):
    __slots__ = ("response", "content", "num")
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    NUM_FIELD_NUMBER: _ClassVar[int]
    response: bool
    content: str
    num: int
    def __init__(self, response: bool = ..., content: _Optional[str] = ..., num: _Optional[int] = ...) -> None: ...

class GetLogRequest(_message.Message):
    __slots__ = ("filename",)
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    filename: str
    def __init__(self, filename: _Optional[str] = ...) -> None: ...

class GetLogResult(_message.Message):
    __slots__ = ("LogResult", "success")
    class Log(_message.Message):
        __slots__ = ("success", "service_type", "filename", "position", "offset", "len", "content")
        SUCCESS_FIELD_NUMBER: _ClassVar[int]
        SERVICE_TYPE_FIELD_NUMBER: _ClassVar[int]
        FILENAME_FIELD_NUMBER: _ClassVar[int]
        POSITION_FIELD_NUMBER: _ClassVar[int]
        OFFSET_FIELD_NUMBER: _ClassVar[int]
        LEN_FIELD_NUMBER: _ClassVar[int]
        CONTENT_FIELD_NUMBER: _ClassVar[int]
        success: bool
        service_type: int
        filename: str
        position: int
        offset: int
        len: int
        content: str
        def __init__(self, success: bool = ..., service_type: _Optional[int] = ..., filename: _Optional[str] = ..., position: _Optional[int] = ..., offset: _Optional[int] = ..., len: _Optional[int] = ..., content: _Optional[str] = ...) -> None: ...
    LOGRESULT_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    LogResult: _containers.RepeatedCompositeFieldContainer[GetLogResult.Log]
    success: bool
    def __init__(self, LogResult: _Optional[_Iterable[_Union[GetLogResult.Log, _Mapping]]] = ..., success: bool = ...) -> None: ...
