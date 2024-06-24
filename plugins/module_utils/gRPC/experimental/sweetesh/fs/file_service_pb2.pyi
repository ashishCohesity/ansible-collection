from open_util.net import protorpc_pb2 as _protorpc_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateServiceRequest(_message.Message):
    __slots__ = ("file_name",)
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    file_name: str
    def __init__(self, file_name: _Optional[str] = ...) -> None: ...

class ReadServiceRequest(_message.Message):
    __slots__ = ("file_name", "offset", "len")
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LEN_FIELD_NUMBER: _ClassVar[int]
    file_name: str
    offset: int
    len: int
    def __init__(self, file_name: _Optional[str] = ..., offset: _Optional[int] = ..., len: _Optional[int] = ...) -> None: ...

class WriteServiceRequest(_message.Message):
    __slots__ = ("file_name", "offset", "len", "data")
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LEN_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    file_name: str
    offset: int
    len: int
    data: bytes
    def __init__(self, file_name: _Optional[str] = ..., offset: _Optional[int] = ..., len: _Optional[int] = ..., data: _Optional[bytes] = ...) -> None: ...

class CreateServiceResponse(_message.Message):
    __slots__ = ("error_code",)
    class ServerError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNoError: _ClassVar[CreateServiceResponse.ServerError]
        kAlreadyExists: _ClassVar[CreateServiceResponse.ServerError]
        kUnknownError: _ClassVar[CreateServiceResponse.ServerError]
    kNoError: CreateServiceResponse.ServerError
    kAlreadyExists: CreateServiceResponse.ServerError
    kUnknownError: CreateServiceResponse.ServerError
    ERROR_CODE_FIELD_NUMBER: _ClassVar[int]
    error_code: CreateServiceResponse.ServerError
    def __init__(self, error_code: _Optional[_Union[CreateServiceResponse.ServerError, str]] = ...) -> None: ...

class ReadServiceResponse(_message.Message):
    __slots__ = ("error_code", "data", "eof")
    class ServerError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNoError: _ClassVar[ReadServiceResponse.ServerError]
        kAlreadyExists: _ClassVar[ReadServiceResponse.ServerError]
        kUnknownError: _ClassVar[ReadServiceResponse.ServerError]
    kNoError: ReadServiceResponse.ServerError
    kAlreadyExists: ReadServiceResponse.ServerError
    kUnknownError: ReadServiceResponse.ServerError
    ERROR_CODE_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    EOF_FIELD_NUMBER: _ClassVar[int]
    error_code: ReadServiceResponse.ServerError
    data: bytes
    eof: bool
    def __init__(self, error_code: _Optional[_Union[ReadServiceResponse.ServerError, str]] = ..., data: _Optional[bytes] = ..., eof: bool = ...) -> None: ...

class WriteServiceResponse(_message.Message):
    __slots__ = ("error_code", "data")
    class ServerError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNoError: _ClassVar[WriteServiceResponse.ServerError]
        kAlreadyExists: _ClassVar[WriteServiceResponse.ServerError]
        kUnknownError: _ClassVar[WriteServiceResponse.ServerError]
    kNoError: WriteServiceResponse.ServerError
    kAlreadyExists: WriteServiceResponse.ServerError
    kUnknownError: WriteServiceResponse.ServerError
    ERROR_CODE_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    error_code: WriteServiceResponse.ServerError
    data: bytes
    def __init__(self, error_code: _Optional[_Union[WriteServiceResponse.ServerError, str]] = ..., data: _Optional[bytes] = ...) -> None: ...
