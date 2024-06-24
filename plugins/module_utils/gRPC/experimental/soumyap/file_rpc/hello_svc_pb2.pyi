from open_util.net import protorpc_pb2 as _protorpc_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HelloRequest(_message.Message):
    __slots__ = ("hmsg",)
    HMSG_FIELD_NUMBER: _ClassVar[int]
    hmsg: str
    def __init__(self, hmsg: _Optional[str] = ...) -> None: ...

class HelloResponse(_message.Message):
    __slots__ = ("hmsg_rsp",)
    HMSG_RSP_FIELD_NUMBER: _ClassVar[int]
    hmsg_rsp: str
    def __init__(self, hmsg_rsp: _Optional[str] = ...) -> None: ...

class CreateFileRequest(_message.Message):
    __slots__ = ("filename", "type")
    class FileType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        RDONLY: _ClassVar[CreateFileRequest.FileType]
        RDWR: _ClassVar[CreateFileRequest.FileType]
        WRONLY: _ClassVar[CreateFileRequest.FileType]
        EXE: _ClassVar[CreateFileRequest.FileType]
    RDONLY: CreateFileRequest.FileType
    RDWR: CreateFileRequest.FileType
    WRONLY: CreateFileRequest.FileType
    EXE: CreateFileRequest.FileType
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    filename: str
    type: CreateFileRequest.FileType
    def __init__(self, filename: _Optional[str] = ..., type: _Optional[_Union[CreateFileRequest.FileType, str]] = ...) -> None: ...

class CreateFileResponse(_message.Message):
    __slots__ = ("status", "sys_errno")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        FILE_CREATE_DONE: _ClassVar[CreateFileResponse.Status]
        FILE_REG_EXISTS: _ClassVar[CreateFileResponse.Status]
        FILE_NONREG_EXISTS: _ClassVar[CreateFileResponse.Status]
        FILE_CREATE_FAILED: _ClassVar[CreateFileResponse.Status]
    FILE_CREATE_DONE: CreateFileResponse.Status
    FILE_REG_EXISTS: CreateFileResponse.Status
    FILE_NONREG_EXISTS: CreateFileResponse.Status
    FILE_CREATE_FAILED: CreateFileResponse.Status
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SYS_ERRNO_FIELD_NUMBER: _ClassVar[int]
    status: CreateFileResponse.Status
    sys_errno: int
    def __init__(self, status: _Optional[_Union[CreateFileResponse.Status, str]] = ..., sys_errno: _Optional[int] = ...) -> None: ...

class WriteFileRequest(_message.Message):
    __slots__ = ("filename", "offset", "len", "data")
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LEN_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    filename: str
    offset: int
    len: int
    data: bytes
    def __init__(self, filename: _Optional[str] = ..., offset: _Optional[int] = ..., len: _Optional[int] = ..., data: _Optional[bytes] = ...) -> None: ...

class ReadFileRequest(_message.Message):
    __slots__ = ("filename", "offset", "len")
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LEN_FIELD_NUMBER: _ClassVar[int]
    filename: str
    offset: int
    len: int
    def __init__(self, filename: _Optional[str] = ..., offset: _Optional[int] = ..., len: _Optional[int] = ...) -> None: ...

class WriteFileResponse(_message.Message):
    __slots__ = ("status", "sys_errno")
    class WriteFileRsp_Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        FILE_WRITE_DONE: _ClassVar[WriteFileResponse.WriteFileRsp_Status]
        FILE_RDONLY: _ClassVar[WriteFileResponse.WriteFileRsp_Status]
        FILE_WRITE_FAILED: _ClassVar[WriteFileResponse.WriteFileRsp_Status]
    FILE_WRITE_DONE: WriteFileResponse.WriteFileRsp_Status
    FILE_RDONLY: WriteFileResponse.WriteFileRsp_Status
    FILE_WRITE_FAILED: WriteFileResponse.WriteFileRsp_Status
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SYS_ERRNO_FIELD_NUMBER: _ClassVar[int]
    status: WriteFileResponse.WriteFileRsp_Status
    sys_errno: int
    def __init__(self, status: _Optional[_Union[WriteFileResponse.WriteFileRsp_Status, str]] = ..., sys_errno: _Optional[int] = ...) -> None: ...

class ReadFileResponse(_message.Message):
    __slots__ = ("status", "sys_errno", "data_len", "data")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        FILE_READ_DONE: _ClassVar[ReadFileResponse.Status]
        FILE_WRONLY: _ClassVar[ReadFileResponse.Status]
        FILE_RD_FAILED: _ClassVar[ReadFileResponse.Status]
    FILE_READ_DONE: ReadFileResponse.Status
    FILE_WRONLY: ReadFileResponse.Status
    FILE_RD_FAILED: ReadFileResponse.Status
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SYS_ERRNO_FIELD_NUMBER: _ClassVar[int]
    DATA_LEN_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    status: ReadFileResponse.Status
    sys_errno: int
    data_len: int
    data: bytes
    def __init__(self, status: _Optional[_Union[ReadFileResponse.Status, str]] = ..., sys_errno: _Optional[int] = ..., data_len: _Optional[int] = ..., data: _Optional[bytes] = ...) -> None: ...
