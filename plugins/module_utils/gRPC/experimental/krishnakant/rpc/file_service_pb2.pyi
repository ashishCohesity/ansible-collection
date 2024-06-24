from open_util.net import protorpc_pb2 as _protorpc_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ErrorProto(_message.Message):
    __slots__ = ("type", "error_string")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNoError: _ClassVar[ErrorProto.Type]
        kInternalError: _ClassVar[ErrorProto.Type]
        kRetryExceeded: _ClassVar[ErrorProto.Type]
    kNoError: ErrorProto.Type
    kInternalError: ErrorProto.Type
    kRetryExceeded: ErrorProto.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ERROR_STRING_FIELD_NUMBER: _ClassVar[int]
    type: ErrorProto.Type
    error_string: str
    def __init__(self, type: _Optional[_Union[ErrorProto.Type, str]] = ..., error_string: _Optional[str] = ...) -> None: ...

class CreateFileArg(_message.Message):
    __slots__ = ("fname",)
    FNAME_FIELD_NUMBER: _ClassVar[int]
    fname: str
    def __init__(self, fname: _Optional[str] = ...) -> None: ...

class CreateFileResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: ErrorProto
    def __init__(self, error: _Optional[_Union[ErrorProto, _Mapping]] = ...) -> None: ...

class ReadFileArg(_message.Message):
    __slots__ = ("fname", "offset", "length")
    FNAME_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    fname: str
    offset: int
    length: int
    def __init__(self, fname: _Optional[str] = ..., offset: _Optional[int] = ..., length: _Optional[int] = ...) -> None: ...

class ReadFileResult(_message.Message):
    __slots__ = ("seqno", "error")
    SEQNO_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    seqno: int
    error: ErrorProto
    def __init__(self, seqno: _Optional[int] = ..., error: _Optional[_Union[ErrorProto, _Mapping]] = ...) -> None: ...

class WriteFileArg(_message.Message):
    __slots__ = ("fname", "offset")
    FNAME_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    fname: str
    offset: int
    def __init__(self, fname: _Optional[str] = ..., offset: _Optional[int] = ...) -> None: ...

class WriteFileResult(_message.Message):
    __slots__ = ("seqno", "error")
    SEQNO_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    seqno: int
    error: ErrorProto
    def __init__(self, seqno: _Optional[int] = ..., error: _Optional[_Union[ErrorProto, _Mapping]] = ...) -> None: ...
