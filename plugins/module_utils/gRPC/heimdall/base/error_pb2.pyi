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
        kRetry: _ClassVar[ErrorProto.Type]
        kTransportError: _ClassVar[ErrorProto.Type]
        kNotLeader: _ClassVar[ErrorProto.Type]
        kInvalid: _ClassVar[ErrorProto.Type]
        kNexusError: _ClassVar[ErrorProto.Type]
        kCloudFleetLaunchError: _ClassVar[ErrorProto.Type]
        kNonExistent: _ClassVar[ErrorProto.Type]
        kTimeout: _ClassVar[ErrorProto.Type]
        kInvalidLogin: _ClassVar[ErrorProto.Type]
        kDuplicate: _ClassVar[ErrorProto.Type]
        kConnectorContextError: _ClassVar[ErrorProto.Type]
        kCloudResourceLimitExceeded: _ClassVar[ErrorProto.Type]
        kAccessDenied: _ClassVar[ErrorProto.Type]
        kNotFound: _ClassVar[ErrorProto.Type]
        kUnknownError: _ClassVar[ErrorProto.Type]
        kInternalError: _ClassVar[ErrorProto.Type]
        kEnvironmentError: _ClassVar[ErrorProto.Type]
        kPending: _ClassVar[ErrorProto.Type]
        kParseError: _ClassVar[ErrorProto.Type]
        kEtcHostError: _ClassVar[ErrorProto.Type]
        kMagnetoError: _ClassVar[ErrorProto.Type]
        kAgentError: _ClassVar[ErrorProto.Type]
        kScriptError: _ClassVar[ErrorProto.Type]
        kRetryExhausted: _ClassVar[ErrorProto.Type]
    kNoError: ErrorProto.Type
    kRetry: ErrorProto.Type
    kTransportError: ErrorProto.Type
    kNotLeader: ErrorProto.Type
    kInvalid: ErrorProto.Type
    kNexusError: ErrorProto.Type
    kCloudFleetLaunchError: ErrorProto.Type
    kNonExistent: ErrorProto.Type
    kTimeout: ErrorProto.Type
    kInvalidLogin: ErrorProto.Type
    kDuplicate: ErrorProto.Type
    kConnectorContextError: ErrorProto.Type
    kCloudResourceLimitExceeded: ErrorProto.Type
    kAccessDenied: ErrorProto.Type
    kNotFound: ErrorProto.Type
    kUnknownError: ErrorProto.Type
    kInternalError: ErrorProto.Type
    kEnvironmentError: ErrorProto.Type
    kPending: ErrorProto.Type
    kParseError: ErrorProto.Type
    kEtcHostError: ErrorProto.Type
    kMagnetoError: ErrorProto.Type
    kAgentError: ErrorProto.Type
    kScriptError: ErrorProto.Type
    kRetryExhausted: ErrorProto.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ERROR_MSG_FIELD_NUMBER: _ClassVar[int]
    type: ErrorProto.Type
    error_msg: str
    def __init__(self, type: _Optional[_Union[ErrorProto.Type, str]] = ..., error_msg: _Optional[str] = ...) -> None: ...
