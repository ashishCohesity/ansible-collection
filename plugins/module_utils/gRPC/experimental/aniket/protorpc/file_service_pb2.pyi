from open_util.net import protorpc_pb2 as _protorpc_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

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

class ErrorProto(_message.Message):
    __slots__ = ("type",)
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNoError: _ClassVar[ErrorProto.Type]
        kFileCreateError: _ClassVar[ErrorProto.Type]
        kFileReadError: _ClassVar[ErrorProto.Type]
        kFileWriteError: _ClassVar[ErrorProto.Type]
    kNoError: ErrorProto.Type
    kFileCreateError: ErrorProto.Type
    kFileReadError: ErrorProto.Type
    kFileWriteError: ErrorProto.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    type: ErrorProto.Type
    def __init__(self, type: _Optional[_Union[ErrorProto.Type, str]] = ...) -> None: ...

class FileCreateRequest(_message.Message):
    __slots__ = ("file",)
    FILE_FIELD_NUMBER: _ClassVar[int]
    file: str
    def __init__(self, file: _Optional[str] = ...) -> None: ...

class FileReadRangeRequest(_message.Message):
    __slots__ = ("file", "offset", "length")
    FILE_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    file: str
    offset: int
    length: int
    def __init__(self, file: _Optional[str] = ..., offset: _Optional[int] = ..., length: _Optional[int] = ...) -> None: ...

class FileWriteRangeRequest(_message.Message):
    __slots__ = ("file", "offset", "length", "content")
    FILE_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    file: str
    offset: int
    length: int
    content: bytes
    def __init__(self, file: _Optional[str] = ..., offset: _Optional[int] = ..., length: _Optional[int] = ..., content: _Optional[bytes] = ...) -> None: ...

class FileCreateResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: ErrorProto
    def __init__(self, error: _Optional[_Union[ErrorProto, _Mapping]] = ...) -> None: ...

class FileReadRangeResult(_message.Message):
    __slots__ = ("error", "end", "dataread")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    DATAREAD_FIELD_NUMBER: _ClassVar[int]
    error: ErrorProto
    end: bool
    dataread: bytes
    def __init__(self, error: _Optional[_Union[ErrorProto, _Mapping]] = ..., end: bool = ..., dataread: _Optional[bytes] = ...) -> None: ...

class FileWriteRangeResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: ErrorProto
    def __init__(self, error: _Optional[_Union[ErrorProto, _Mapping]] = ...) -> None: ...
