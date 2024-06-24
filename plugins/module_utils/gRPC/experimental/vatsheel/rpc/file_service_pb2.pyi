from open_util.net import protorpc_pb2 as _protorpc_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateFileRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ErrorProto(_message.Message):
    __slots__ = ("type", "error_msg")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNoError: _ClassVar[ErrorProto.Type]
        kInvalid: _ClassVar[ErrorProto.Type]
        kServerError: _ClassVar[ErrorProto.Type]
        kUnknownError: _ClassVar[ErrorProto.Type]
    kNoError: ErrorProto.Type
    kInvalid: ErrorProto.Type
    kServerError: ErrorProto.Type
    kUnknownError: ErrorProto.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ERROR_MSG_FIELD_NUMBER: _ClassVar[int]
    type: ErrorProto.Type
    error_msg: str
    def __init__(self, type: _Optional[_Union[ErrorProto.Type, str]] = ..., error_msg: _Optional[str] = ...) -> None: ...

class CreateFileResponse(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: ErrorProto
    def __init__(self, error: _Optional[_Union[ErrorProto, _Mapping]] = ...) -> None: ...

class ReadFileRangeRequest(_message.Message):
    __slots__ = ("name", "offset", "len")
    NAME_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LEN_FIELD_NUMBER: _ClassVar[int]
    name: str
    offset: int
    len: int
    def __init__(self, name: _Optional[str] = ..., offset: _Optional[int] = ..., len: _Optional[int] = ...) -> None: ...

class ReadFileRangeResponse(_message.Message):
    __slots__ = ("content", "error")
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    content: bytes
    error: ErrorProto
    def __init__(self, content: _Optional[bytes] = ..., error: _Optional[_Union[ErrorProto, _Mapping]] = ...) -> None: ...

class WriteFileRangeRequest(_message.Message):
    __slots__ = ("name", "offset", "len", "content")
    NAME_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LEN_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    name: str
    offset: int
    len: int
    content: bytes
    def __init__(self, name: _Optional[str] = ..., offset: _Optional[int] = ..., len: _Optional[int] = ..., content: _Optional[bytes] = ...) -> None: ...

class WriteFileRangeResponse(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: ErrorProto
    def __init__(self, error: _Optional[_Union[ErrorProto, _Mapping]] = ...) -> None: ...
