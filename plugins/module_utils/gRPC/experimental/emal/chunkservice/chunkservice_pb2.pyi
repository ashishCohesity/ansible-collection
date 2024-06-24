from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Result(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    OP_SUCCESS: _ClassVar[Result]
    OP_FAILED: _ClassVar[Result]
    OP_EXISTS: _ClassVar[Result]
    OP_NOT_FOUND: _ClassVar[Result]
OP_SUCCESS: Result
OP_FAILED: Result
OP_EXISTS: Result
OP_NOT_FOUND: Result

class CreateFileRequest(_message.Message):
    __slots__ = ("file_name",)
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    file_name: str
    def __init__(self, file_name: _Optional[str] = ...) -> None: ...

class WriteFileRangeRequest(_message.Message):
    __slots__ = ("file_name", "start", "end", "data")
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    START_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    file_name: str
    start: int
    end: int
    data: str
    def __init__(self, file_name: _Optional[str] = ..., start: _Optional[int] = ..., end: _Optional[int] = ..., data: _Optional[str] = ...) -> None: ...

class ReadFileRangeRequest(_message.Message):
    __slots__ = ("file_name", "start", "end")
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    START_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    file_name: str
    start: int
    end: int
    def __init__(self, file_name: _Optional[str] = ..., start: _Optional[int] = ..., end: _Optional[int] = ...) -> None: ...

class Response(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: Result
    def __init__(self, result: _Optional[_Union[Result, str]] = ...) -> None: ...

class ReadResponse(_message.Message):
    __slots__ = ("result", "data")
    RESULT_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    result: Result
    data: str
    def __init__(self, result: _Optional[_Union[Result, str]] = ..., data: _Optional[str] = ...) -> None: ...
