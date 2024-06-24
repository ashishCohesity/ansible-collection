from open_util.net import protorpc_pb2 as _protorpc_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FSErrorProto(_message.Message):
    __slots__ = ()
    class ErrorCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kSuccess: _ClassVar[FSErrorProto.ErrorCode]
        kError: _ClassVar[FSErrorProto.ErrorCode]
    kSuccess: FSErrorProto.ErrorCode
    kError: FSErrorProto.ErrorCode
    def __init__(self) -> None: ...

class FSError(_message.Message):
    __slots__ = ("error_code", "error_msg")
    ERROR_CODE_FIELD_NUMBER: _ClassVar[int]
    ERROR_MSG_FIELD_NUMBER: _ClassVar[int]
    error_code: FSErrorProto.ErrorCode
    error_msg: str
    def __init__(self, error_code: _Optional[_Union[FSErrorProto.ErrorCode, str]] = ..., error_msg: _Optional[str] = ...) -> None: ...

class FSCreateFileArg(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class FSCreateFileResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: FSError
    def __init__(self, error: _Optional[_Union[FSError, _Mapping]] = ...) -> None: ...

class FSReadFileRangeArg(_message.Message):
    __slots__ = ("name", "offset", "length")
    NAME_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    name: str
    offset: int
    length: int
    def __init__(self, name: _Optional[str] = ..., offset: _Optional[int] = ..., length: _Optional[int] = ...) -> None: ...

class FSReadFileRangeResult(_message.Message):
    __slots__ = ("error", "data")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    error: FSError
    data: str
    def __init__(self, error: _Optional[_Union[FSError, _Mapping]] = ..., data: _Optional[str] = ...) -> None: ...

class FSWriteFileRangeArg(_message.Message):
    __slots__ = ("name", "offset", "length", "data")
    NAME_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    name: str
    offset: int
    length: int
    data: str
    def __init__(self, name: _Optional[str] = ..., offset: _Optional[int] = ..., length: _Optional[int] = ..., data: _Optional[str] = ...) -> None: ...

class FSWriteFileRangeResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: FSError
    def __init__(self, error: _Optional[_Union[FSError, _Mapping]] = ...) -> None: ...
