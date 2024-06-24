from open_util.net import protorpc_pb2 as _protorpc_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ErrorProto(_message.Message):
    __slots__ = ("error_type", "error_msg")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNoError: _ClassVar[ErrorProto.Type]
        kFileOpen: _ClassVar[ErrorProto.Type]
        kFileCreate: _ClassVar[ErrorProto.Type]
        kFileNotFound: _ClassVar[ErrorProto.Type]
        kFileExists: _ClassVar[ErrorProto.Type]
        kFileRead: _ClassVar[ErrorProto.Type]
        kFileWrite: _ClassVar[ErrorProto.Type]
        kFileWriteLess: _ClassVar[ErrorProto.Type]
        kRetry: _ClassVar[ErrorProto.Type]
        kTimeout: _ClassVar[ErrorProto.Type]
        kTransport: _ClassVar[ErrorProto.Type]
    kNoError: ErrorProto.Type
    kFileOpen: ErrorProto.Type
    kFileCreate: ErrorProto.Type
    kFileNotFound: ErrorProto.Type
    kFileExists: ErrorProto.Type
    kFileRead: ErrorProto.Type
    kFileWrite: ErrorProto.Type
    kFileWriteLess: ErrorProto.Type
    kRetry: ErrorProto.Type
    kTimeout: ErrorProto.Type
    kTransport: ErrorProto.Type
    ERROR_TYPE_FIELD_NUMBER: _ClassVar[int]
    ERROR_MSG_FIELD_NUMBER: _ClassVar[int]
    error_type: ErrorProto.Type
    error_msg: str
    def __init__(self, error_type: _Optional[_Union[ErrorProto.Type, str]] = ..., error_msg: _Optional[str] = ...) -> None: ...
