from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class ErrorProto(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNoError: _ClassVar[ErrorProto.Type]
        kTransportError: _ClassVar[ErrorProto.Type]
        kTimeout: _ClassVar[ErrorProto.Type]
        kRetry: _ClassVar[ErrorProto.Type]
        kIncarnationIdMismatch: _ClassVar[ErrorProto.Type]
        kNotMaster: _ClassVar[ErrorProto.Type]
        kClientSessionNotFound: _ClassVar[ErrorProto.Type]
        kStale: _ClassVar[ErrorProto.Type]
        kNonExistent: _ClassVar[ErrorProto.Type]
        kStaleKeepAlive: _ClassVar[ErrorProto.Type]
        kSessionToCloseNotFound: _ClassVar[ErrorProto.Type]
        kNotificationIdAlreadyExists: _ClassVar[ErrorProto.Type]
        kRequestIdNotFound: _ClassVar[ErrorProto.Type]
        kCriticalError: _ClassVar[ErrorProto.Type]
        kClusterIdMismatch: _ClassVar[ErrorProto.Type]
        kMethodError: _ClassVar[ErrorProto.Type]
        kUnauthorized: _ClassVar[ErrorProto.Type]
        kEncryptionRequired: _ClassVar[ErrorProto.Type]
        kAuthenticationError: _ClassVar[ErrorProto.Type]
    kNoError: ErrorProto.Type
    kTransportError: ErrorProto.Type
    kTimeout: ErrorProto.Type
    kRetry: ErrorProto.Type
    kIncarnationIdMismatch: ErrorProto.Type
    kNotMaster: ErrorProto.Type
    kClientSessionNotFound: ErrorProto.Type
    kStale: ErrorProto.Type
    kNonExistent: ErrorProto.Type
    kStaleKeepAlive: ErrorProto.Type
    kSessionToCloseNotFound: ErrorProto.Type
    kNotificationIdAlreadyExists: ErrorProto.Type
    kRequestIdNotFound: ErrorProto.Type
    kCriticalError: ErrorProto.Type
    kClusterIdMismatch: ErrorProto.Type
    kMethodError: ErrorProto.Type
    kUnauthorized: ErrorProto.Type
    kEncryptionRequired: ErrorProto.Type
    kAuthenticationError: ErrorProto.Type
    def __init__(self) -> None: ...
