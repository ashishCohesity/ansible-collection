from open_util.net import protorpc_pb2 as _protorpc_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ErrorCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ALL_OK: _ClassVar[ErrorCode]
    FILE_ALREADY_EXISTS: _ClassVar[ErrorCode]
    FILE_NOT_FOUND: _ClassVar[ErrorCode]
    FILE_WRITE_LIMIT_ERROR: _ClassVar[ErrorCode]
    FILE_READ_LIMIT_ERROR: _ClassVar[ErrorCode]
ALL_OK: ErrorCode
FILE_ALREADY_EXISTS: ErrorCode
FILE_NOT_FOUND: ErrorCode
FILE_WRITE_LIMIT_ERROR: ErrorCode
FILE_READ_LIMIT_ERROR: ErrorCode

class CreateFileRequest(_message.Message):
    __slots__ = ("fname", "thread_id")
    FNAME_FIELD_NUMBER: _ClassVar[int]
    THREAD_ID_FIELD_NUMBER: _ClassVar[int]
    fname: str
    thread_id: int
    def __init__(self, fname: _Optional[str] = ..., thread_id: _Optional[int] = ...) -> None: ...

class CreateFileResult(_message.Message):
    __slots__ = ("ack_message", "time_stamp", "status")
    ACK_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    TIME_STAMP_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ack_message: str
    time_stamp: int
    status: ErrorCode
    def __init__(self, ack_message: _Optional[str] = ..., time_stamp: _Optional[int] = ..., status: _Optional[_Union[ErrorCode, str]] = ...) -> None: ...

class WriteFileRequest(_message.Message):
    __slots__ = ("fname", "offset", "length", "thread_id")
    FNAME_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    THREAD_ID_FIELD_NUMBER: _ClassVar[int]
    fname: str
    offset: int
    length: int
    thread_id: int
    def __init__(self, fname: _Optional[str] = ..., offset: _Optional[int] = ..., length: _Optional[int] = ..., thread_id: _Optional[int] = ...) -> None: ...

class WriteFileResult(_message.Message):
    __slots__ = ("ack_message", "time_stamp", "status")
    ACK_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    TIME_STAMP_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ack_message: str
    time_stamp: int
    status: ErrorCode
    def __init__(self, ack_message: _Optional[str] = ..., time_stamp: _Optional[int] = ..., status: _Optional[_Union[ErrorCode, str]] = ...) -> None: ...

class ReadFileRequest(_message.Message):
    __slots__ = ("fname", "offset", "length", "thread_id")
    FNAME_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    THREAD_ID_FIELD_NUMBER: _ClassVar[int]
    fname: str
    offset: int
    length: int
    thread_id: int
    def __init__(self, fname: _Optional[str] = ..., offset: _Optional[int] = ..., length: _Optional[int] = ..., thread_id: _Optional[int] = ...) -> None: ...

class ReadFileResult(_message.Message):
    __slots__ = ("ack_message", "time_stamp", "status")
    ACK_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    TIME_STAMP_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ack_message: str
    time_stamp: int
    status: ErrorCode
    def __init__(self, ack_message: _Optional[str] = ..., time_stamp: _Optional[int] = ..., status: _Optional[_Union[ErrorCode, str]] = ...) -> None: ...
