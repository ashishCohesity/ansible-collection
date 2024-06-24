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
        kExpectedError: _ClassVar[ErrorProto.Type]
        kTransportError: _ClassVar[ErrorProto.Type]
        kTimeout: _ClassVar[ErrorProto.Type]
        kRetry: _ClassVar[ErrorProto.Type]
        kCancelled: _ClassVar[ErrorProto.Type]
        kNonExistent: _ClassVar[ErrorProto.Type]
        kNotDirectory: _ClassVar[ErrorProto.Type]
        kNameTooLong: _ClassVar[ErrorProto.Type]
        kPermissionDenied: _ClassVar[ErrorProto.Type]
        kInvalid: _ClassVar[ErrorProto.Type]
        kNotSupported: _ClassVar[ErrorProto.Type]
        kBufferTooSmall: _ClassVar[ErrorProto.Type]
        kSizeExceededSystemLimit: _ClassVar[ErrorProto.Type]
        kAttrNonExistent: _ClassVar[ErrorProto.Type]
        kWindowsSystemError: _ClassVar[ErrorProto.Type]
        kStale: _ClassVar[ErrorProto.Type]
        kAlreadyExists: _ClassVar[ErrorProto.Type]
        kClusterMismatchError: _ClassVar[ErrorProto.Type]
        kFsError: _ClassVar[ErrorProto.Type]
        kPathNotCovered: _ClassVar[ErrorProto.Type]
        kFetchChildrenError: _ClassVar[ErrorProto.Type]
        kSkipped: _ClassVar[ErrorProto.Type]
        kVMwareFsError: _ClassVar[ErrorProto.Type]
        kResourceBusy: _ClassVar[ErrorProto.Type]
        kStoppedOnSymlink: _ClassVar[ErrorProto.Type]
        kEOF: _ClassVar[ErrorProto.Type]
        kSharingViolation: _ClassVar[ErrorProto.Type]
        kVosEOF: _ClassVar[ErrorProto.Type]
        kVosFailure: _ClassVar[ErrorProto.Type]
        kVosIgnoreOffset: _ClassVar[ErrorProto.Type]
        kInternalError: _ClassVar[ErrorProto.Type]
    kNoError: ErrorProto.Type
    kExpectedError: ErrorProto.Type
    kTransportError: ErrorProto.Type
    kTimeout: ErrorProto.Type
    kRetry: ErrorProto.Type
    kCancelled: ErrorProto.Type
    kNonExistent: ErrorProto.Type
    kNotDirectory: ErrorProto.Type
    kNameTooLong: ErrorProto.Type
    kPermissionDenied: ErrorProto.Type
    kInvalid: ErrorProto.Type
    kNotSupported: ErrorProto.Type
    kBufferTooSmall: ErrorProto.Type
    kSizeExceededSystemLimit: ErrorProto.Type
    kAttrNonExistent: ErrorProto.Type
    kWindowsSystemError: ErrorProto.Type
    kStale: ErrorProto.Type
    kAlreadyExists: ErrorProto.Type
    kClusterMismatchError: ErrorProto.Type
    kFsError: ErrorProto.Type
    kPathNotCovered: ErrorProto.Type
    kFetchChildrenError: ErrorProto.Type
    kSkipped: ErrorProto.Type
    kVMwareFsError: ErrorProto.Type
    kResourceBusy: ErrorProto.Type
    kStoppedOnSymlink: ErrorProto.Type
    kEOF: ErrorProto.Type
    kSharingViolation: ErrorProto.Type
    kVosEOF: ErrorProto.Type
    kVosFailure: ErrorProto.Type
    kVosIgnoreOffset: ErrorProto.Type
    kInternalError: ErrorProto.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ERROR_DETAIL_FIELD_NUMBER: _ClassVar[int]
    DETAILED_ERROR_MSG_FIELD_NUMBER: _ClassVar[int]
    type: ErrorProto.Type
    error_detail: str
    detailed_error_msg: _message_catalog_pb2.MessageProto
    def __init__(self, type: _Optional[_Union[ErrorProto.Type, str]] = ..., error_detail: _Optional[str] = ..., detailed_error_msg: _Optional[_Union[_message_catalog_pb2.MessageProto, _Mapping]] = ...) -> None: ...
