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
        kNotMaster: _ClassVar[ErrorProto.Type]
        kScribeError: _ClassVar[ErrorProto.Type]
        kInvalidRequest: _ClassVar[ErrorProto.Type]
        kMasterUnknown: _ClassVar[ErrorProto.Type]
        kPartial: _ClassVar[ErrorProto.Type]
        kGandalfError: _ClassVar[ErrorProto.Type]
        kIpmiNotReachable: _ClassVar[ErrorProto.Type]
        kNodeUnknown: _ClassVar[ErrorProto.Type]
        kConnError: _ClassVar[ErrorProto.Type]
        kUserNotFound: _ClassVar[ErrorProto.Type]
        kInvalidCredentials: _ClassVar[ErrorProto.Type]
        kClusterNotFound: _ClassVar[ErrorProto.Type]
        kAlreadyExists: _ClassVar[ErrorProto.Type]
        kNotifNotFound: _ClassVar[ErrorProto.Type]
        kEntityNotFound: _ClassVar[ErrorProto.Type]
        kInvalidResponse: _ClassVar[ErrorProto.Type]
        kInternalServerError: _ClassVar[ErrorProto.Type]
    kNoError: ErrorProto.Type
    kRetry: ErrorProto.Type
    kNotMaster: ErrorProto.Type
    kScribeError: ErrorProto.Type
    kInvalidRequest: ErrorProto.Type
    kMasterUnknown: ErrorProto.Type
    kPartial: ErrorProto.Type
    kGandalfError: ErrorProto.Type
    kIpmiNotReachable: ErrorProto.Type
    kNodeUnknown: ErrorProto.Type
    kConnError: ErrorProto.Type
    kUserNotFound: ErrorProto.Type
    kInvalidCredentials: ErrorProto.Type
    kClusterNotFound: ErrorProto.Type
    kAlreadyExists: ErrorProto.Type
    kNotifNotFound: ErrorProto.Type
    kEntityNotFound: ErrorProto.Type
    kInvalidResponse: ErrorProto.Type
    kInternalServerError: ErrorProto.Type
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    error: ErrorProto.Type
    error_message: str
    def __init__(self, error: _Optional[_Union[ErrorProto.Type, str]] = ..., error_message: _Optional[str] = ...) -> None: ...
