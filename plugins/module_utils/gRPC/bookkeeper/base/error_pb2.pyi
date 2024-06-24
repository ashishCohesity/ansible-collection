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
        kTransportError: _ClassVar[ErrorProto.Type]
        kTimeout: _ClassVar[ErrorProto.Type]
        kNonExistent: _ClassVar[ErrorProto.Type]
        kRetry: _ClassVar[ErrorProto.Type]
        kNotLeader: _ClassVar[ErrorProto.Type]
        kInvalid: _ClassVar[ErrorProto.Type]
        kBusy: _ClassVar[ErrorProto.Type]
        kErrorCount: _ClassVar[ErrorProto.Type]
    kNoError: ErrorProto.Type
    kTransportError: ErrorProto.Type
    kTimeout: ErrorProto.Type
    kNonExistent: ErrorProto.Type
    kRetry: ErrorProto.Type
    kNotLeader: ErrorProto.Type
    kInvalid: ErrorProto.Type
    kBusy: ErrorProto.Type
    kErrorCount: ErrorProto.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ERROR_DETAIL_FIELD_NUMBER: _ClassVar[int]
    type: ErrorProto.Type
    error_detail: str
    def __init__(self, type: _Optional[_Union[ErrorProto.Type, str]] = ..., error_detail: _Optional[str] = ...) -> None: ...
