from open_util.net import protorpc_pb2 as _protorpc_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FileOpRsp(_message.Message):
    __slots__ = ("status", "sequence", "data")
    class StatusCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SUCCESS: _ClassVar[FileOpRsp.StatusCode]
        FILE_NON_EXIST: _ClassVar[FileOpRsp.StatusCode]
        INVALID_OFFSET: _ClassVar[FileOpRsp.StatusCode]
        INVALID_LEN: _ClassVar[FileOpRsp.StatusCode]
        INTERNAL_ERROR: _ClassVar[FileOpRsp.StatusCode]
    SUCCESS: FileOpRsp.StatusCode
    FILE_NON_EXIST: FileOpRsp.StatusCode
    INVALID_OFFSET: FileOpRsp.StatusCode
    INVALID_LEN: FileOpRsp.StatusCode
    INTERNAL_ERROR: FileOpRsp.StatusCode
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SEQUENCE_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    status: FileOpRsp.StatusCode
    sequence: int
    data: bytes
    def __init__(self, status: _Optional[_Union[FileOpRsp.StatusCode, str]] = ..., sequence: _Optional[int] = ..., data: _Optional[bytes] = ...) -> None: ...

class FileOpReq(_message.Message):
    __slots__ = ("name", "offset", "len", "data")
    NAME_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LEN_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    name: str
    offset: int
    len: int
    data: bytes
    def __init__(self, name: _Optional[str] = ..., offset: _Optional[int] = ..., len: _Optional[int] = ..., data: _Optional[bytes] = ...) -> None: ...
