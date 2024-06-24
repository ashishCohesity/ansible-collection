from open_util.net import protorpc_pb2 as _protorpc_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kSuccess: _ClassVar[Status]
    kInvalidOperationError: _ClassVar[Status]
    kFileExistsError: _ClassVar[Status]
    kFileOpenFailedError: _ClassVar[Status]
    kFileReadFailed: _ClassVar[Status]
    kFileReadIncomplete: _ClassVar[Status]
    kFileWriteFailed: _ClassVar[Status]
    kFileWriteIncomplete: _ClassVar[Status]
kSuccess: Status
kInvalidOperationError: Status
kFileExistsError: Status
kFileOpenFailedError: Status
kFileReadFailed: Status
kFileReadIncomplete: Status
kFileWriteFailed: Status
kFileWriteIncomplete: Status

class HelloArg(_message.Message):
    __slots__ = ("hi_message", "sender_name")
    HI_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    SENDER_NAME_FIELD_NUMBER: _ClassVar[int]
    hi_message: str
    sender_name: str
    def __init__(self, hi_message: _Optional[str] = ..., sender_name: _Optional[str] = ...) -> None: ...

class HelloResult(_message.Message):
    __slots__ = ("hi_result",)
    HI_RESULT_FIELD_NUMBER: _ClassVar[int]
    hi_result: str
    def __init__(self, hi_result: _Optional[str] = ...) -> None: ...

class CreateFileArg(_message.Message):
    __slots__ = ("file_name",)
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    file_name: str
    def __init__(self, file_name: _Optional[str] = ...) -> None: ...

class CreateFileResult(_message.Message):
    __slots__ = ("status", "message")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    status: Status
    message: str
    def __init__(self, status: _Optional[_Union[Status, str]] = ..., message: _Optional[str] = ...) -> None: ...

class ReadFileRangeArg(_message.Message):
    __slots__ = ("file_name", "offset", "length")
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    file_name: str
    offset: int
    length: int
    def __init__(self, file_name: _Optional[str] = ..., offset: _Optional[int] = ..., length: _Optional[int] = ...) -> None: ...

class ReadFileRangeResult(_message.Message):
    __slots__ = ("status", "message", "length")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    status: Status
    message: str
    length: int
    def __init__(self, status: _Optional[_Union[Status, str]] = ..., message: _Optional[str] = ..., length: _Optional[int] = ...) -> None: ...

class WriteFileRangeArg(_message.Message):
    __slots__ = ("file_name", "offset", "length")
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    file_name: str
    offset: int
    length: int
    def __init__(self, file_name: _Optional[str] = ..., offset: _Optional[int] = ..., length: _Optional[int] = ...) -> None: ...

class WriteFileRangeResult(_message.Message):
    __slots__ = ("status", "message", "length")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    status: Status
    message: str
    length: int
    def __init__(self, status: _Optional[_Union[Status, str]] = ..., message: _Optional[str] = ..., length: _Optional[int] = ...) -> None: ...
