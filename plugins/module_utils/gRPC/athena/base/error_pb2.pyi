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
        kInvalid: _ClassVar[ErrorProto.Type]
        kTimeout: _ClassVar[ErrorProto.Type]
        kPermissionDenied: _ClassVar[ErrorProto.Type]
        kNonExistent: _ClassVar[ErrorProto.Type]
        kAlreadyExists: _ClassVar[ErrorProto.Type]
        kValidationError: _ClassVar[ErrorProto.Type]
        kUnschedulable: _ClassVar[ErrorProto.Type]
        kNotMaster: _ClassVar[ErrorProto.Type]
        kConflict: _ClassVar[ErrorProto.Type]
        kUnsupported: _ClassVar[ErrorProto.Type]
        kIncorrectAppsMode: _ClassVar[ErrorProto.Type]
        kBusy: _ClassVar[ErrorProto.Type]
        kMasterNotInit: _ClassVar[ErrorProto.Type]
        kTransportError: _ClassVar[ErrorProto.Type]
        kRetry: _ClassVar[ErrorProto.Type]
        kInternalError: _ClassVar[ErrorProto.Type]
        kMethodError: _ClassVar[ErrorProto.Type]
        kInProgress: _ClassVar[ErrorProto.Type]
        kErrorCount: _ClassVar[ErrorProto.Type]
    kNoError: ErrorProto.Type
    kInvalid: ErrorProto.Type
    kTimeout: ErrorProto.Type
    kPermissionDenied: ErrorProto.Type
    kNonExistent: ErrorProto.Type
    kAlreadyExists: ErrorProto.Type
    kValidationError: ErrorProto.Type
    kUnschedulable: ErrorProto.Type
    kNotMaster: ErrorProto.Type
    kConflict: ErrorProto.Type
    kUnsupported: ErrorProto.Type
    kIncorrectAppsMode: ErrorProto.Type
    kBusy: ErrorProto.Type
    kMasterNotInit: ErrorProto.Type
    kTransportError: ErrorProto.Type
    kRetry: ErrorProto.Type
    kInternalError: ErrorProto.Type
    kMethodError: ErrorProto.Type
    kInProgress: ErrorProto.Type
    kErrorCount: ErrorProto.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ERROR_MSG_FIELD_NUMBER: _ClassVar[int]
    type: ErrorProto.Type
    error_msg: str
    def __init__(self, type: _Optional[_Union[ErrorProto.Type, str]] = ..., error_msg: _Optional[str] = ...) -> None: ...
