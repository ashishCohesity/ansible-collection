from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ErrorProto(_message.Message):
    __slots__ = ("type", "error_msg")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNoError: _ClassVar[ErrorProto.Type]
        kTimeout: _ClassVar[ErrorProto.Type]
        kRetry: _ClassVar[ErrorProto.Type]
        kNotMaster: _ClassVar[ErrorProto.Type]
        kInvalidRequest: _ClassVar[ErrorProto.Type]
        kNonExistent: _ClassVar[ErrorProto.Type]
        kAlreadyExists: _ClassVar[ErrorProto.Type]
        kTransportError: _ClassVar[ErrorProto.Type]
        kInternalError: _ClassVar[ErrorProto.Type]
        kErrorCount: _ClassVar[ErrorProto.Type]
        kStale: _ClassVar[ErrorProto.Type]
    kNoError: ErrorProto.Type
    kTimeout: ErrorProto.Type
    kRetry: ErrorProto.Type
    kNotMaster: ErrorProto.Type
    kInvalidRequest: ErrorProto.Type
    kNonExistent: ErrorProto.Type
    kAlreadyExists: ErrorProto.Type
    kTransportError: ErrorProto.Type
    kInternalError: ErrorProto.Type
    kErrorCount: ErrorProto.Type
    kStale: ErrorProto.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ERROR_MSG_FIELD_NUMBER: _ClassVar[int]
    type: ErrorProto.Type
    error_msg: str
    def __init__(self, type: _Optional[_Union[ErrorProto.Type, str]] = ..., error_msg: _Optional[str] = ...) -> None: ...
