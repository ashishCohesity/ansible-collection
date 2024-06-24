from util.message_catalog import message_catalog_pb2 as _message_catalog_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ErrorProto(_message.Message):
    __slots__ = ("type", "error_msg", "retryable", "detailed_error_msg")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNoError: _ClassVar[ErrorProto.Type]
        kClusterMismatchError: _ClassVar[ErrorProto.Type]
        kFsError: _ClassVar[ErrorProto.Type]
        kWindowsSystemError: _ClassVar[ErrorProto.Type]
        kDuplicate: _ClassVar[ErrorProto.Type]
        kVDIError: _ClassVar[ErrorProto.Type]
        kSQLError: _ClassVar[ErrorProto.Type]
        kStreamError: _ClassVar[ErrorProto.Type]
        kVSSError: _ClassVar[ErrorProto.Type]
        kTransportError: _ClassVar[ErrorProto.Type]
        kTimeout: _ClassVar[ErrorProto.Type]
        kRetry: _ClassVar[ErrorProto.Type]
        kInvalid: _ClassVar[ErrorProto.Type]
        kParseError: _ClassVar[ErrorProto.Type]
        kServiceUnavailable: _ClassVar[ErrorProto.Type]
        kAccessDenied: _ClassVar[ErrorProto.Type]
        kNotFound: _ClassVar[ErrorProto.Type]
        kIOError: _ClassVar[ErrorProto.Type]
        kOperationNotPermittedError: _ClassVar[ErrorProto.Type]
        kUnexpectedState: _ClassVar[ErrorProto.Type]
        kTaskMismatchError: _ClassVar[ErrorProto.Type]
        kInsufficientResources: _ClassVar[ErrorProto.Type]
        kHyperVCmdError: _ClassVar[ErrorProto.Type]
        kCancelled: _ClassVar[ErrorProto.Type]
        kNotImplemented: _ClassVar[ErrorProto.Type]
        kHyperVCmdExceptionThrown: _ClassVar[ErrorProto.Type]
        kOracleCmdError: _ClassVar[ErrorProto.Type]
        kSysCallError: _ClassVar[ErrorProto.Type]
        kNotSupported: _ClassVar[ErrorProto.Type]
        kScriptNotFound: _ClassVar[ErrorProto.Type]
        kPowershellExceptionThrown: _ClassVar[ErrorProto.Type]
        kPowershellError: _ClassVar[ErrorProto.Type]
        kExists: _ClassVar[ErrorProto.Type]
        kSQL: _ClassVar[ErrorProto.Type]
        kWindowsCOMError: _ClassVar[ErrorProto.Type]
        kRemoteSnapFSError: _ClassVar[ErrorProto.Type]
        kWindowsSMBError: _ClassVar[ErrorProto.Type]
        kPstConverterLibError: _ClassVar[ErrorProto.Type]
        kPstConverterLibMsgError: _ClassVar[ErrorProto.Type]
        kShellError: _ClassVar[ErrorProto.Type]
        kWarning: _ClassVar[ErrorProto.Type]
    kNoError: ErrorProto.Type
    kClusterMismatchError: ErrorProto.Type
    kFsError: ErrorProto.Type
    kWindowsSystemError: ErrorProto.Type
    kDuplicate: ErrorProto.Type
    kVDIError: ErrorProto.Type
    kSQLError: ErrorProto.Type
    kStreamError: ErrorProto.Type
    kVSSError: ErrorProto.Type
    kTransportError: ErrorProto.Type
    kTimeout: ErrorProto.Type
    kRetry: ErrorProto.Type
    kInvalid: ErrorProto.Type
    kParseError: ErrorProto.Type
    kServiceUnavailable: ErrorProto.Type
    kAccessDenied: ErrorProto.Type
    kNotFound: ErrorProto.Type
    kIOError: ErrorProto.Type
    kOperationNotPermittedError: ErrorProto.Type
    kUnexpectedState: ErrorProto.Type
    kTaskMismatchError: ErrorProto.Type
    kInsufficientResources: ErrorProto.Type
    kHyperVCmdError: ErrorProto.Type
    kCancelled: ErrorProto.Type
    kNotImplemented: ErrorProto.Type
    kHyperVCmdExceptionThrown: ErrorProto.Type
    kOracleCmdError: ErrorProto.Type
    kSysCallError: ErrorProto.Type
    kNotSupported: ErrorProto.Type
    kScriptNotFound: ErrorProto.Type
    kPowershellExceptionThrown: ErrorProto.Type
    kPowershellError: ErrorProto.Type
    kExists: ErrorProto.Type
    kSQL: ErrorProto.Type
    kWindowsCOMError: ErrorProto.Type
    kRemoteSnapFSError: ErrorProto.Type
    kWindowsSMBError: ErrorProto.Type
    kPstConverterLibError: ErrorProto.Type
    kPstConverterLibMsgError: ErrorProto.Type
    kShellError: ErrorProto.Type
    kWarning: ErrorProto.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ERROR_MSG_FIELD_NUMBER: _ClassVar[int]
    RETRYABLE_FIELD_NUMBER: _ClassVar[int]
    DETAILED_ERROR_MSG_FIELD_NUMBER: _ClassVar[int]
    type: ErrorProto.Type
    error_msg: str
    retryable: bool
    detailed_error_msg: _message_catalog_pb2.MessageProto
    def __init__(self, type: _Optional[_Union[ErrorProto.Type, str]] = ..., error_msg: _Optional[str] = ..., retryable: bool = ..., detailed_error_msg: _Optional[_Union[_message_catalog_pb2.MessageProto, _Mapping]] = ...) -> None: ...
