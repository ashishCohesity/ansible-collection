from open_util.net import protorpc_pb2 as _protorpc_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

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

class CreateFileRequest(_message.Message):
    __slots__ = ("filename", "client_id", "job_id")
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    filename: str
    client_id: int
    job_id: int
    def __init__(self, filename: _Optional[str] = ..., client_id: _Optional[int] = ..., job_id: _Optional[int] = ...) -> None: ...

class CreateFileResult(_message.Message):
    __slots__ = ("success", "timestamp")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    success: bool
    timestamp: int
    def __init__(self, success: bool = ..., timestamp: _Optional[int] = ...) -> None: ...

class ReadWriteFileRangeRequest(_message.Message):
    __slots__ = ("read", "offset", "size", "filename", "client_id", "job_id")
    READ_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    read: bool
    offset: int
    size: int
    filename: str
    client_id: int
    job_id: int
    def __init__(self, read: bool = ..., offset: _Optional[int] = ..., size: _Optional[int] = ..., filename: _Optional[str] = ..., client_id: _Optional[int] = ..., job_id: _Optional[int] = ...) -> None: ...

class ReadWriteFileRangeResult(_message.Message):
    __slots__ = ("success", "timestamp")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    success: bool
    timestamp: int
    def __init__(self, success: bool = ..., timestamp: _Optional[int] = ...) -> None: ...

class FileLogRequest(_message.Message):
    __slots__ = ("filename", "client_id", "job_id")
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    filename: str
    client_id: int
    job_id: int
    def __init__(self, filename: _Optional[str] = ..., client_id: _Optional[int] = ..., job_id: _Optional[int] = ...) -> None: ...

class FileLogResult(_message.Message):
    __slots__ = ("success", "file_op")
    class FileOp(_message.Message):
        __slots__ = ("read", "create", "success", "timestamp", "filename", "client_id", "job_id", "offset", "size", "data")
        READ_FIELD_NUMBER: _ClassVar[int]
        CREATE_FIELD_NUMBER: _ClassVar[int]
        SUCCESS_FIELD_NUMBER: _ClassVar[int]
        TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
        FILENAME_FIELD_NUMBER: _ClassVar[int]
        CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
        JOB_ID_FIELD_NUMBER: _ClassVar[int]
        OFFSET_FIELD_NUMBER: _ClassVar[int]
        SIZE_FIELD_NUMBER: _ClassVar[int]
        DATA_FIELD_NUMBER: _ClassVar[int]
        read: bool
        create: bool
        success: bool
        timestamp: int
        filename: str
        client_id: int
        job_id: int
        offset: int
        size: int
        data: str
        def __init__(self, read: bool = ..., create: bool = ..., success: bool = ..., timestamp: _Optional[int] = ..., filename: _Optional[str] = ..., client_id: _Optional[int] = ..., job_id: _Optional[int] = ..., offset: _Optional[int] = ..., size: _Optional[int] = ..., data: _Optional[str] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FILE_OP_FIELD_NUMBER: _ClassVar[int]
    success: bool
    file_op: _containers.RepeatedCompositeFieldContainer[FileLogResult.FileOp]
    def __init__(self, success: bool = ..., file_op: _Optional[_Iterable[_Union[FileLogResult.FileOp, _Mapping]]] = ...) -> None: ...
