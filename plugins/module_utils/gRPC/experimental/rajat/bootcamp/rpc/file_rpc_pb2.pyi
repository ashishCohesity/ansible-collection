from experimental.rajat.bootcamp.base import error_pb2 as _error_pb2
from open_util.net import protorpc_pb2 as _protorpc_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateFileReq(_message.Message):
    __slots__ = ("filename",)
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    filename: str
    def __init__(self, filename: _Optional[str] = ...) -> None: ...

class CreateFileResp(_message.Message):
    __slots__ = ("status", "seq_num")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SEQ_NUM_FIELD_NUMBER: _ClassVar[int]
    status: _error_pb2.ErrorProto
    seq_num: int
    def __init__(self, status: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., seq_num: _Optional[int] = ...) -> None: ...

class ReadFileRangeReq(_message.Message):
    __slots__ = ("filename", "offset", "length")
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    filename: str
    offset: int
    length: int
    def __init__(self, filename: _Optional[str] = ..., offset: _Optional[int] = ..., length: _Optional[int] = ...) -> None: ...

class ReadFileRangeResp(_message.Message):
    __slots__ = ("status", "seq_num", "length")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SEQ_NUM_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    status: _error_pb2.ErrorProto
    seq_num: int
    length: int
    def __init__(self, status: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., seq_num: _Optional[int] = ..., length: _Optional[int] = ...) -> None: ...

class WriteFileRangeReq(_message.Message):
    __slots__ = ("filename", "offset", "length")
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    filename: str
    offset: int
    length: int
    def __init__(self, filename: _Optional[str] = ..., offset: _Optional[int] = ..., length: _Optional[int] = ...) -> None: ...

class WriteFileRangeResp(_message.Message):
    __slots__ = ("status", "seq_num", "length")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SEQ_NUM_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    status: _error_pb2.ErrorProto
    seq_num: int
    length: int
    def __init__(self, status: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., seq_num: _Optional[int] = ..., length: _Optional[int] = ...) -> None: ...
