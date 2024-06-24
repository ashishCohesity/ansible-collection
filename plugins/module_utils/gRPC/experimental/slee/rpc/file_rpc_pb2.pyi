from open_util.net import protorpc_pb2 as _protorpc_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SayHelloPayload(_message.Message):
    __slots__ = ("question",)
    QUESTION_FIELD_NUMBER: _ClassVar[int]
    question: str
    def __init__(self, question: _Optional[str] = ...) -> None: ...

class SayHelloResult(_message.Message):
    __slots__ = ("answer",)
    ANSWER_FIELD_NUMBER: _ClassVar[int]
    answer: str
    def __init__(self, answer: _Optional[str] = ...) -> None: ...

class CreateFilePayload(_message.Message):
    __slots__ = ("file_path", "size_bytes", "init_string")
    FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    INIT_STRING_FIELD_NUMBER: _ClassVar[int]
    file_path: str
    size_bytes: int
    init_string: str
    def __init__(self, file_path: _Optional[str] = ..., size_bytes: _Optional[int] = ..., init_string: _Optional[str] = ...) -> None: ...

class CreateFileResult(_message.Message):
    __slots__ = ("status", "return_message")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    RETURN_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    status: int
    return_message: str
    def __init__(self, status: _Optional[int] = ..., return_message: _Optional[str] = ...) -> None: ...

class ReadFileRangePayload(_message.Message):
    __slots__ = ("file_path", "offset_bytes", "len_bytes")
    FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    OFFSET_BYTES_FIELD_NUMBER: _ClassVar[int]
    LEN_BYTES_FIELD_NUMBER: _ClassVar[int]
    file_path: str
    offset_bytes: int
    len_bytes: int
    def __init__(self, file_path: _Optional[str] = ..., offset_bytes: _Optional[int] = ..., len_bytes: _Optional[int] = ...) -> None: ...

class ReadFileRangeResult(_message.Message):
    __slots__ = ("status", "data_read", "return_message")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    DATA_READ_FIELD_NUMBER: _ClassVar[int]
    RETURN_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    status: int
    data_read: str
    return_message: str
    def __init__(self, status: _Optional[int] = ..., data_read: _Optional[str] = ..., return_message: _Optional[str] = ...) -> None: ...

class WriteFileRangePayload(_message.Message):
    __slots__ = ("file_path", "offset_bytes", "data_2b_written")
    FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    OFFSET_BYTES_FIELD_NUMBER: _ClassVar[int]
    DATA_2B_WRITTEN_FIELD_NUMBER: _ClassVar[int]
    file_path: str
    offset_bytes: int
    data_2b_written: str
    def __init__(self, file_path: _Optional[str] = ..., offset_bytes: _Optional[int] = ..., data_2b_written: _Optional[str] = ...) -> None: ...

class WriteFileRangeResult(_message.Message):
    __slots__ = ("status", "return_message")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    RETURN_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    status: int
    return_message: str
    def __init__(self, status: _Optional[int] = ..., return_message: _Optional[str] = ...) -> None: ...
