from open_util.net import protorpc_pb2 as _protorpc_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FileIORequestArg(_message.Message):
    __slots__ = ("request_type", "request")
    class RequestType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CREATE_FILE_OP: _ClassVar[FileIORequestArg.RequestType]
        READ_RANGE_OP: _ClassVar[FileIORequestArg.RequestType]
        WRITE_RANGE_OP: _ClassVar[FileIORequestArg.RequestType]
    CREATE_FILE_OP: FileIORequestArg.RequestType
    READ_RANGE_OP: FileIORequestArg.RequestType
    WRITE_RANGE_OP: FileIORequestArg.RequestType
    class IORequest(_message.Message):
        __slots__ = ("filename", "offset", "length")
        FILENAME_FIELD_NUMBER: _ClassVar[int]
        OFFSET_FIELD_NUMBER: _ClassVar[int]
        LENGTH_FIELD_NUMBER: _ClassVar[int]
        filename: str
        offset: int
        length: int
        def __init__(self, filename: _Optional[str] = ..., offset: _Optional[int] = ..., length: _Optional[int] = ...) -> None: ...
    REQUEST_TYPE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    request_type: FileIORequestArg.RequestType
    request: FileIORequestArg.IORequest
    def __init__(self, request_type: _Optional[_Union[FileIORequestArg.RequestType, str]] = ..., request: _Optional[_Union[FileIORequestArg.IORequest, _Mapping]] = ...) -> None: ...

class FileIORequestResult(_message.Message):
    __slots__ = ("operation_id", "response_status")
    class ResponseCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SUCCESS_OK: _ClassVar[FileIORequestResult.ResponseCode]
        ERR_INVALID_REQUEST: _ClassVar[FileIORequestResult.ResponseCode]
        ERR_INTERNAL_SERVER: _ClassVar[FileIORequestResult.ResponseCode]
        ERR_CACHE_MISS: _ClassVar[FileIORequestResult.ResponseCode]
    SUCCESS_OK: FileIORequestResult.ResponseCode
    ERR_INVALID_REQUEST: FileIORequestResult.ResponseCode
    ERR_INTERNAL_SERVER: FileIORequestResult.ResponseCode
    ERR_CACHE_MISS: FileIORequestResult.ResponseCode
    OPERATION_ID_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STATUS_FIELD_NUMBER: _ClassVar[int]
    operation_id: int
    response_status: FileIORequestResult.ResponseCode
    def __init__(self, operation_id: _Optional[int] = ..., response_status: _Optional[_Union[FileIORequestResult.ResponseCode, str]] = ...) -> None: ...
