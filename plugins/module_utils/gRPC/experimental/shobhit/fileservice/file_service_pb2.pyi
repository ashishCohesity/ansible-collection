from open_util.net import protorpc_pb2 as _protorpc_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FileRequest(_message.Message):
    __slots__ = ("filepath", "readwrite")
    class ReadWriteRequest(_message.Message):
        __slots__ = ("offset", "len", "data")
        OFFSET_FIELD_NUMBER: _ClassVar[int]
        LEN_FIELD_NUMBER: _ClassVar[int]
        DATA_FIELD_NUMBER: _ClassVar[int]
        offset: int
        len: int
        data: bytes
        def __init__(self, offset: _Optional[int] = ..., len: _Optional[int] = ..., data: _Optional[bytes] = ...) -> None: ...
    FILEPATH_FIELD_NUMBER: _ClassVar[int]
    READWRITE_FIELD_NUMBER: _ClassVar[int]
    filepath: str
    readwrite: FileRequest.ReadWriteRequest
    def __init__(self, filepath: _Optional[str] = ..., readwrite: _Optional[_Union[FileRequest.ReadWriteRequest, _Mapping]] = ...) -> None: ...

class FileResponse(_message.Message):
    __slots__ = ("error", "readwrite")
    class ErrorCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kAlreadyExist: _ClassVar[FileResponse.ErrorCode]
        kAccessDenied: _ClassVar[FileResponse.ErrorCode]
        kPermissionDenied: _ClassVar[FileResponse.ErrorCode]
        kUnknownError: _ClassVar[FileResponse.ErrorCode]
        kBadRequestError: _ClassVar[FileResponse.ErrorCode]
    kAlreadyExist: FileResponse.ErrorCode
    kAccessDenied: FileResponse.ErrorCode
    kPermissionDenied: FileResponse.ErrorCode
    kUnknownError: FileResponse.ErrorCode
    kBadRequestError: FileResponse.ErrorCode
    class ReadWriteResponse(_message.Message):
        __slots__ = ("data",)
        DATA_FIELD_NUMBER: _ClassVar[int]
        data: bytes
        def __init__(self, data: _Optional[bytes] = ...) -> None: ...
    ERROR_FIELD_NUMBER: _ClassVar[int]
    READWRITE_FIELD_NUMBER: _ClassVar[int]
    error: FileResponse.ErrorCode
    readwrite: FileResponse.ReadWriteResponse
    def __init__(self, error: _Optional[_Union[FileResponse.ErrorCode, str]] = ..., readwrite: _Optional[_Union[FileResponse.ReadWriteResponse, _Mapping]] = ...) -> None: ...
