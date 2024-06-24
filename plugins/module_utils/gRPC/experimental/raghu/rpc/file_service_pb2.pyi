from open_util.net import protorpc_pb2 as _protorpc_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ErrorType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kNoError: _ClassVar[ErrorType]
    kFileNotFound: _ClassVar[ErrorType]
    kTimeoutError: _ClassVar[ErrorType]
    kIOError: _ClassVar[ErrorType]
    kLookupError: _ClassVar[ErrorType]
kNoError: ErrorType
kFileNotFound: ErrorType
kTimeoutError: ErrorType
kIOError: ErrorType
kLookupError: ErrorType

class FileParams(_message.Message):
    __slots__ = ("file_name",)
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    file_name: str
    def __init__(self, file_name: _Optional[str] = ...) -> None: ...

class ReadIOParams(_message.Message):
    __slots__ = ("file_name", "size", "offset")
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    file_name: str
    size: int
    offset: int
    def __init__(self, file_name: _Optional[str] = ..., size: _Optional[int] = ..., offset: _Optional[int] = ...) -> None: ...

class WriteIOParams(_message.Message):
    __slots__ = ("file_name", "size", "offset")
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    file_name: str
    size: int
    offset: int
    def __init__(self, file_name: _Optional[str] = ..., size: _Optional[int] = ..., offset: _Optional[int] = ...) -> None: ...

class ReadFileRangeResponse(_message.Message):
    __slots__ = ("debug_string", "debug_msg")
    DEBUG_STRING_FIELD_NUMBER: _ClassVar[int]
    DEBUG_MSG_FIELD_NUMBER: _ClassVar[int]
    debug_string: ErrorType
    debug_msg: str
    def __init__(self, debug_string: _Optional[_Union[ErrorType, str]] = ..., debug_msg: _Optional[str] = ...) -> None: ...

class WriteFileRangeResponse(_message.Message):
    __slots__ = ("debug_string", "debug_msg")
    DEBUG_STRING_FIELD_NUMBER: _ClassVar[int]
    DEBUG_MSG_FIELD_NUMBER: _ClassVar[int]
    debug_string: ErrorType
    debug_msg: str
    def __init__(self, debug_string: _Optional[_Union[ErrorType, str]] = ..., debug_msg: _Optional[str] = ...) -> None: ...

class FileResParams(_message.Message):
    __slots__ = ("debug_string", "debug_msg")
    DEBUG_STRING_FIELD_NUMBER: _ClassVar[int]
    DEBUG_MSG_FIELD_NUMBER: _ClassVar[int]
    debug_string: ErrorType
    debug_msg: str
    def __init__(self, debug_string: _Optional[_Union[ErrorType, str]] = ..., debug_msg: _Optional[str] = ...) -> None: ...
