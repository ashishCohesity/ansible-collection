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
        kIOError: _ClassVar[ErrorProto.Type]
        kNonExistent: _ClassVar[ErrorProto.Type]
        kEOFError: _ClassVar[ErrorProto.Type]
        kParseError: _ClassVar[ErrorProto.Type]
        kUnknownTag: _ClassVar[ErrorProto.Type]
        kAuthenticationError: _ClassVar[ErrorProto.Type]
        kErrorCount: _ClassVar[ErrorProto.Type]
    kNoError: ErrorProto.Type
    kIOError: ErrorProto.Type
    kNonExistent: ErrorProto.Type
    kEOFError: ErrorProto.Type
    kParseError: ErrorProto.Type
    kUnknownTag: ErrorProto.Type
    kAuthenticationError: ErrorProto.Type
    kErrorCount: ErrorProto.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ERROR_MSG_FIELD_NUMBER: _ClassVar[int]
    type: ErrorProto.Type
    error_msg: str
    def __init__(self, type: _Optional[_Union[ErrorProto.Type, str]] = ..., error_msg: _Optional[str] = ...) -> None: ...
