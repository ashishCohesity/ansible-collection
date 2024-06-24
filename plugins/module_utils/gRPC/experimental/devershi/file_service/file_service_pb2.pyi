from open_util.net import protorpc_pb2 as _protorpc_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ErrorType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kUnowknError: _ClassVar[ErrorType]
    kInternalError: _ClassVar[ErrorType]
    kOutOfRangeError: _ClassVar[ErrorType]
    kInvalidRequestError: _ClassVar[ErrorType]
    kNoError: _ClassVar[ErrorType]
    kFileAlreadyExists: _ClassVar[ErrorType]
    kFileDoesNotExists: _ClassVar[ErrorType]

class OpType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kUnknownOp: _ClassVar[OpType]
    kRead: _ClassVar[OpType]
    kCreate: _ClassVar[OpType]
    kWrite: _ClassVar[OpType]
kUnowknError: ErrorType
kInternalError: ErrorType
kOutOfRangeError: ErrorType
kInvalidRequestError: ErrorType
kNoError: ErrorType
kFileAlreadyExists: ErrorType
kFileDoesNotExists: ErrorType
kUnknownOp: OpType
kRead: OpType
kCreate: OpType
kWrite: OpType

class CreateFileRequest(_message.Message):
    __slots__ = ("file_name",)
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    file_name: str
    def __init__(self, file_name: _Optional[str] = ...) -> None: ...

class ReadFileBlockRequest(_message.Message):
    __slots__ = ("file_name", "offset", "block_size")
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    BLOCK_SIZE_FIELD_NUMBER: _ClassVar[int]
    file_name: str
    offset: int
    block_size: int
    def __init__(self, file_name: _Optional[str] = ..., offset: _Optional[int] = ..., block_size: _Optional[int] = ...) -> None: ...

class WriteFileBlockRequest(_message.Message):
    __slots__ = ("file_name", "offset", "data")
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    file_name: str
    offset: int
    data: str
    def __init__(self, file_name: _Optional[str] = ..., offset: _Optional[int] = ..., data: _Optional[str] = ...) -> None: ...

class FileOpResponse(_message.Message):
    __slots__ = ("err_code", "op_type", "data", "error_msg")
    ERR_CODE_FIELD_NUMBER: _ClassVar[int]
    OP_TYPE_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    ERROR_MSG_FIELD_NUMBER: _ClassVar[int]
    err_code: ErrorType
    op_type: OpType
    data: str
    error_msg: str
    def __init__(self, err_code: _Optional[_Union[ErrorType, str]] = ..., op_type: _Optional[_Union[OpType, str]] = ..., data: _Optional[str] = ..., error_msg: _Optional[str] = ...) -> None: ...
