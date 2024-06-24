from util.message_catalog import message_catalog_pb2 as _message_catalog_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ErrorProto(_message.Message):
    __slots__ = ("type", "error_detail", "detailed_error_msg")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNoError: _ClassVar[ErrorProto.Type]
        kTransportError: _ClassVar[ErrorProto.Type]
        kTimeout: _ClassVar[ErrorProto.Type]
        kStale: _ClassVar[ErrorProto.Type]
        kNonExistent: _ClassVar[ErrorProto.Type]
        kRetry: _ClassVar[ErrorProto.Type]
        kNotImplemented: _ClassVar[ErrorProto.Type]
        kIOError: _ClassVar[ErrorProto.Type]
        kUnknownError: _ClassVar[ErrorProto.Type]
        kInvalidRequest: _ClassVar[ErrorProto.Type]
        kInternalError: _ClassVar[ErrorProto.Type]
        kKerberosInternal: _ClassVar[ErrorProto.Type]
        kUnknownUser: _ClassVar[ErrorProto.Type]
        kIncorrectPassword: _ClassVar[ErrorProto.Type]
        kAdNotReachable: _ClassVar[ErrorProto.Type]
        kPermissionDenied: _ClassVar[ErrorProto.Type]
        kAlreadyExists: _ClassVar[ErrorProto.Type]
        kInvalid: _ClassVar[ErrorProto.Type]
        kNotSupported: _ClassVar[ErrorProto.Type]
        kMoreProcessingRequired: _ClassVar[ErrorProto.Type]
        kNoAdServices: _ClassVar[ErrorProto.Type]
        kLdapError: _ClassVar[ErrorProto.Type]
        kNoneMapped: _ClassVar[ErrorProto.Type]
        kSomeNotMapped: _ClassVar[ErrorProto.Type]
        kWinbindError: _ClassVar[ErrorProto.Type]
        kLogonFailure: _ClassVar[ErrorProto.Type]
        kCASError: _ClassVar[ErrorProto.Type]
        kSkipped: _ClassVar[ErrorProto.Type]
        kBifrostDisconnected: _ClassVar[ErrorProto.Type]
        kBrokerSocksServerNoFreeListenPorts: _ClassVar[ErrorProto.Type]
        kRejected: _ClassVar[ErrorProto.Type]
        kDuplicate: _ClassVar[ErrorProto.Type]
        kValidBrokerNotFound: _ClassVar[ErrorProto.Type]
        kBifrostNotFound: _ClassVar[ErrorProto.Type]
    kNoError: ErrorProto.Type
    kTransportError: ErrorProto.Type
    kTimeout: ErrorProto.Type
    kStale: ErrorProto.Type
    kNonExistent: ErrorProto.Type
    kRetry: ErrorProto.Type
    kNotImplemented: ErrorProto.Type
    kIOError: ErrorProto.Type
    kUnknownError: ErrorProto.Type
    kInvalidRequest: ErrorProto.Type
    kInternalError: ErrorProto.Type
    kKerberosInternal: ErrorProto.Type
    kUnknownUser: ErrorProto.Type
    kIncorrectPassword: ErrorProto.Type
    kAdNotReachable: ErrorProto.Type
    kPermissionDenied: ErrorProto.Type
    kAlreadyExists: ErrorProto.Type
    kInvalid: ErrorProto.Type
    kNotSupported: ErrorProto.Type
    kMoreProcessingRequired: ErrorProto.Type
    kNoAdServices: ErrorProto.Type
    kLdapError: ErrorProto.Type
    kNoneMapped: ErrorProto.Type
    kSomeNotMapped: ErrorProto.Type
    kWinbindError: ErrorProto.Type
    kLogonFailure: ErrorProto.Type
    kCASError: ErrorProto.Type
    kSkipped: ErrorProto.Type
    kBifrostDisconnected: ErrorProto.Type
    kBrokerSocksServerNoFreeListenPorts: ErrorProto.Type
    kRejected: ErrorProto.Type
    kDuplicate: ErrorProto.Type
    kValidBrokerNotFound: ErrorProto.Type
    kBifrostNotFound: ErrorProto.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ERROR_DETAIL_FIELD_NUMBER: _ClassVar[int]
    DETAILED_ERROR_MSG_FIELD_NUMBER: _ClassVar[int]
    type: ErrorProto.Type
    error_detail: str
    detailed_error_msg: _message_catalog_pb2.MessageProto
    def __init__(self, type: _Optional[_Union[ErrorProto.Type, str]] = ..., error_detail: _Optional[str] = ..., detailed_error_msg: _Optional[_Union[_message_catalog_pb2.MessageProto, _Mapping]] = ...) -> None: ...
