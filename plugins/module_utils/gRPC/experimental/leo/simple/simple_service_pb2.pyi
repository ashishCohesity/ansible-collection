from open_util.net import protorpc_pb2 as _protorpc_pb2
from util.base import op_clock_pb2 as _op_clock_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ErrorProto(_message.Message):
    __slots__ = ("err_code", "err_detail")
    class ErrCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNoError: _ClassVar[ErrorProto.ErrCode]
        kInvalidFileName: _ClassVar[ErrorProto.ErrCode]
        kNonExistantFile: _ClassVar[ErrorProto.ErrCode]
        kIOError: _ClassVar[ErrorProto.ErrCode]
        kInvalidArgument: _ClassVar[ErrorProto.ErrCode]
        kEOFReached: _ClassVar[ErrorProto.ErrCode]
    kNoError: ErrorProto.ErrCode
    kInvalidFileName: ErrorProto.ErrCode
    kNonExistantFile: ErrorProto.ErrCode
    kIOError: ErrorProto.ErrCode
    kInvalidArgument: ErrorProto.ErrCode
    kEOFReached: ErrorProto.ErrCode
    ERR_CODE_FIELD_NUMBER: _ClassVar[int]
    ERR_DETAIL_FIELD_NUMBER: _ClassVar[int]
    err_code: ErrorProto.ErrCode
    err_detail: str
    def __init__(self, err_code: _Optional[_Union[ErrorProto.ErrCode, str]] = ..., err_detail: _Optional[str] = ...) -> None: ...

class CreateFileArg(_message.Message):
    __slots__ = ("filename",)
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    filename: str
    def __init__(self, filename: _Optional[str] = ...) -> None: ...

class CreateFileResult(_message.Message):
    __slots__ = ("created", "err_proto")
    CREATED_FIELD_NUMBER: _ClassVar[int]
    ERR_PROTO_FIELD_NUMBER: _ClassVar[int]
    created: bool
    err_proto: ErrorProto
    def __init__(self, created: bool = ..., err_proto: _Optional[_Union[ErrorProto, _Mapping]] = ...) -> None: ...

class ReadFileRangeArg(_message.Message):
    __slots__ = ("filename", "offset", "length", "bufoffset", "bufmaxlen")
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    BUFOFFSET_FIELD_NUMBER: _ClassVar[int]
    BUFMAXLEN_FIELD_NUMBER: _ClassVar[int]
    filename: str
    offset: int
    length: int
    bufoffset: int
    bufmaxlen: int
    def __init__(self, filename: _Optional[str] = ..., offset: _Optional[int] = ..., length: _Optional[int] = ..., bufoffset: _Optional[int] = ..., bufmaxlen: _Optional[int] = ...) -> None: ...

class ReadFileRangeResult(_message.Message):
    __slots__ = ("numbytes", "err_proto")
    NUMBYTES_FIELD_NUMBER: _ClassVar[int]
    ERR_PROTO_FIELD_NUMBER: _ClassVar[int]
    numbytes: int
    err_proto: ErrorProto
    def __init__(self, numbytes: _Optional[int] = ..., err_proto: _Optional[_Union[ErrorProto, _Mapping]] = ...) -> None: ...

class WriteFileRangeArg(_message.Message):
    __slots__ = ("filename", "offset", "length", "bufoffset")
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    BUFOFFSET_FIELD_NUMBER: _ClassVar[int]
    filename: str
    offset: int
    length: int
    bufoffset: int
    def __init__(self, filename: _Optional[str] = ..., offset: _Optional[int] = ..., length: _Optional[int] = ..., bufoffset: _Optional[int] = ...) -> None: ...

class WriteFileRangeResult(_message.Message):
    __slots__ = ("numbytes", "err_proto")
    NUMBYTES_FIELD_NUMBER: _ClassVar[int]
    ERR_PROTO_FIELD_NUMBER: _ClassVar[int]
    numbytes: int
    err_proto: ErrorProto
    def __init__(self, numbytes: _Optional[int] = ..., err_proto: _Optional[_Union[ErrorProto, _Mapping]] = ...) -> None: ...
