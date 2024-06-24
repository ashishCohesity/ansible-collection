from open_util.net import protorpc_pb2 as _protorpc_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ReturnCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kSuccess: _ClassVar[ReturnCode]
    kAlreadyExists: _ClassVar[ReturnCode]
    kDoesNotExist: _ClassVar[ReturnCode]
    kAccessDenied: _ClassVar[ReturnCode]
    kUnknownError: _ClassVar[ReturnCode]
kSuccess: ReturnCode
kAlreadyExists: ReturnCode
kDoesNotExist: ReturnCode
kAccessDenied: ReturnCode
kUnknownError: ReturnCode

class CreateFileRequest(_message.Message):
    __slots__ = ("file_name",)
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    file_name: str
    def __init__(self, file_name: _Optional[str] = ...) -> None: ...

class CreateFileResult(_message.Message):
    __slots__ = ("return_code",)
    RETURN_CODE_FIELD_NUMBER: _ClassVar[int]
    return_code: ReturnCode
    def __init__(self, return_code: _Optional[_Union[ReturnCode, str]] = ...) -> None: ...

class ReadFileRequest(_message.Message):
    __slots__ = ("file_name", "offset", "length")
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    file_name: str
    offset: int
    length: int
    def __init__(self, file_name: _Optional[str] = ..., offset: _Optional[int] = ..., length: _Optional[int] = ...) -> None: ...

class ReadFileResult(_message.Message):
    __slots__ = ("return_code",)
    RETURN_CODE_FIELD_NUMBER: _ClassVar[int]
    return_code: ReturnCode
    def __init__(self, return_code: _Optional[_Union[ReturnCode, str]] = ...) -> None: ...

class WriteFileRequest(_message.Message):
    __slots__ = ("file_name", "offset", "length")
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    file_name: str
    offset: int
    length: int
    def __init__(self, file_name: _Optional[str] = ..., offset: _Optional[int] = ..., length: _Optional[int] = ...) -> None: ...

class WriteFileResult(_message.Message):
    __slots__ = ("return_code",)
    RETURN_CODE_FIELD_NUMBER: _ClassVar[int]
    return_code: ReturnCode
    def __init__(self, return_code: _Optional[_Union[ReturnCode, str]] = ...) -> None: ...
