from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ErrorProto(_message.Message):
    __slots__ = ("error", "error_message")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNoError: _ClassVar[ErrorProto.Type]
        kRetry: _ClassVar[ErrorProto.Type]
        kInvalidRequest: _ClassVar[ErrorProto.Type]
        kInternalServerError: _ClassVar[ErrorProto.Type]
        kFileNotFound: _ClassVar[ErrorProto.Type]
        kServiceUnavailable: _ClassVar[ErrorProto.Type]
    kNoError: ErrorProto.Type
    kRetry: ErrorProto.Type
    kInvalidRequest: ErrorProto.Type
    kInternalServerError: ErrorProto.Type
    kFileNotFound: ErrorProto.Type
    kServiceUnavailable: ErrorProto.Type
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    error: ErrorProto.Type
    error_message: str
    def __init__(self, error: _Optional[_Union[ErrorProto.Type, str]] = ..., error_message: _Optional[str] = ...) -> None: ...
