from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ErrorProto(_message.Message):
    __slots__ = ("type", "error_detail")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNoError: _ClassVar[ErrorProto.Type]
        kNonExistent: _ClassVar[ErrorProto.Type]
        kNameTooLong: _ClassVar[ErrorProto.Type]
        kPermissionDenied: _ClassVar[ErrorProto.Type]
        kInvalid: _ClassVar[ErrorProto.Type]
        kNotSupported: _ClassVar[ErrorProto.Type]
        kBufferTooSmall: _ClassVar[ErrorProto.Type]
        kSizeExceededSystemLimit: _ClassVar[ErrorProto.Type]
        kAttrNonExistent: _ClassVar[ErrorProto.Type]
        kFsError: _ClassVar[ErrorProto.Type]
        kEOF: _ClassVar[ErrorProto.Type]
        kVosEOF: _ClassVar[ErrorProto.Type]
        kVosFailure: _ClassVar[ErrorProto.Type]
        kVosIgnoreOffset: _ClassVar[ErrorProto.Type]
    kNoError: ErrorProto.Type
    kNonExistent: ErrorProto.Type
    kNameTooLong: ErrorProto.Type
    kPermissionDenied: ErrorProto.Type
    kInvalid: ErrorProto.Type
    kNotSupported: ErrorProto.Type
    kBufferTooSmall: ErrorProto.Type
    kSizeExceededSystemLimit: ErrorProto.Type
    kAttrNonExistent: ErrorProto.Type
    kFsError: ErrorProto.Type
    kEOF: ErrorProto.Type
    kVosEOF: ErrorProto.Type
    kVosFailure: ErrorProto.Type
    kVosIgnoreOffset: ErrorProto.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ERROR_DETAIL_FIELD_NUMBER: _ClassVar[int]
    type: ErrorProto.Type
    error_detail: str
    def __init__(self, type: _Optional[_Union[ErrorProto.Type, str]] = ..., error_detail: _Optional[str] = ...) -> None: ...
