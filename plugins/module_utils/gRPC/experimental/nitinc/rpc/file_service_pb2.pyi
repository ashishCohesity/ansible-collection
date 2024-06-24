from open_util.net import protorpc_pb2 as _protorpc_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ErrorProto(_message.Message):
    __slots__ = ("type", "error_detail")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNoError: _ClassVar[ErrorProto.Type]
        kInternalError: _ClassVar[ErrorProto.Type]
        kInvalidInput: _ClassVar[ErrorProto.Type]
        kRetryExceeded: _ClassVar[ErrorProto.Type]
    kNoError: ErrorProto.Type
    kInternalError: ErrorProto.Type
    kInvalidInput: ErrorProto.Type
    kRetryExceeded: ErrorProto.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ERROR_DETAIL_FIELD_NUMBER: _ClassVar[int]
    type: ErrorProto.Type
    error_detail: str
    def __init__(self, type: _Optional[_Union[ErrorProto.Type, str]] = ..., error_detail: _Optional[str] = ...) -> None: ...

class FileCreateRequest(_message.Message):
    __slots__ = ("filename",)
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    filename: str
    def __init__(self, filename: _Optional[str] = ...) -> None: ...

class FileReadRequest(_message.Message):
    __slots__ = ("filename", "offset", "len")
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LEN_FIELD_NUMBER: _ClassVar[int]
    filename: str
    offset: int
    len: int
    def __init__(self, filename: _Optional[str] = ..., offset: _Optional[int] = ..., len: _Optional[int] = ...) -> None: ...

class FileWriteRequest(_message.Message):
    __slots__ = ("filename", "offset", "data")
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    filename: str
    offset: int
    data: str
    def __init__(self, filename: _Optional[str] = ..., offset: _Optional[int] = ..., data: _Optional[str] = ...) -> None: ...

class FileCreateResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: ErrorProto
    def __init__(self, error: _Optional[_Union[ErrorProto, _Mapping]] = ...) -> None: ...

class FileReadResult(_message.Message):
    __slots__ = ("data", "error")
    DATA_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    data: str
    error: ErrorProto
    def __init__(self, data: _Optional[str] = ..., error: _Optional[_Union[ErrorProto, _Mapping]] = ...) -> None: ...

class FileWriteResult(_message.Message):
    __slots__ = ("len", "error")
    LEN_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    len: int
    error: ErrorProto
    def __init__(self, len: _Optional[int] = ..., error: _Optional[_Union[ErrorProto, _Mapping]] = ...) -> None: ...
