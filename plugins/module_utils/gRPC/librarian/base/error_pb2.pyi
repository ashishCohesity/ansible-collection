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
        kStale: _ClassVar[ErrorProto.Type]
        kNonExistent: _ClassVar[ErrorProto.Type]
        kRetry: _ClassVar[ErrorProto.Type]
        kNotLeader: _ClassVar[ErrorProto.Type]
        kAlreadyExists: _ClassVar[ErrorProto.Type]
        kInvalid: _ClassVar[ErrorProto.Type]
        kPermissionDenied: _ClassVar[ErrorProto.Type]
        kOutOfSpace: _ClassVar[ErrorProto.Type]
        kBadCookie: _ClassVar[ErrorProto.Type]
        kCorrupt: _ClassVar[ErrorProto.Type]
        kFsError: _ClassVar[ErrorProto.Type]
        kNotSupported: _ClassVar[ErrorProto.Type]
        kCanceled: _ClassVar[ErrorProto.Type]
        kNotEnoughNodes: _ClassVar[ErrorProto.Type]
        kIOError: _ClassVar[ErrorProto.Type]
        kUnknownError: _ClassVar[ErrorProto.Type]
        kDeleteExisting: _ClassVar[ErrorProto.Type]
        kReadOnly: _ClassVar[ErrorProto.Type]
        kPending: _ClassVar[ErrorProto.Type]
        kParseError: _ClassVar[ErrorProto.Type]
        kServiceUnavailable: _ClassVar[ErrorProto.Type]
        kNotUpdated: _ClassVar[ErrorProto.Type]
        kAbort: _ClassVar[ErrorProto.Type]
        kStaleSessionId: _ClassVar[ErrorProto.Type]
        kSlaveConfigNotUpdated: _ClassVar[ErrorProto.Type]
        kForceIndex: _ClassVar[ErrorProto.Type]
        kIndexableFieldsChanged: _ClassVar[ErrorProto.Type]
        kBusy: _ClassVar[ErrorProto.Type]
        kLuceneserverInternalError: _ClassVar[ErrorProto.Type]
        kStaleCookie: _ClassVar[ErrorProto.Type]
        kBucketReplicasUnavailable: _ClassVar[ErrorProto.Type]
        kTagOpOnNonExistentDocument: _ClassVar[ErrorProto.Type]
        kTagOpOnNonExistentSnapshot: _ClassVar[ErrorProto.Type]
        kTagOpInvalidArgument: _ClassVar[ErrorProto.Type]
        kLuceneMaxClauseCount: _ClassVar[ErrorProto.Type]
        kReassignmentNotNeeded: _ClassVar[ErrorProto.Type]
        kReassign: _ClassVar[ErrorProto.Type]
        kESDocIdSizeExceeded: _ClassVar[ErrorProto.Type]
        kESBulkRequestSizeExceeded: _ClassVar[ErrorProto.Type]
        kDiskNotFound: _ClassVar[ErrorProto.Type]
        kAwsESError: _ClassVar[ErrorProto.Type]
    kNoError: ErrorProto.Type
    kTransportError: ErrorProto.Type
    kTimeout: ErrorProto.Type
    kStale: ErrorProto.Type
    kNonExistent: ErrorProto.Type
    kRetry: ErrorProto.Type
    kNotLeader: ErrorProto.Type
    kAlreadyExists: ErrorProto.Type
    kInvalid: ErrorProto.Type
    kPermissionDenied: ErrorProto.Type
    kOutOfSpace: ErrorProto.Type
    kBadCookie: ErrorProto.Type
    kCorrupt: ErrorProto.Type
    kFsError: ErrorProto.Type
    kNotSupported: ErrorProto.Type
    kCanceled: ErrorProto.Type
    kNotEnoughNodes: ErrorProto.Type
    kIOError: ErrorProto.Type
    kUnknownError: ErrorProto.Type
    kDeleteExisting: ErrorProto.Type
    kReadOnly: ErrorProto.Type
    kPending: ErrorProto.Type
    kParseError: ErrorProto.Type
    kServiceUnavailable: ErrorProto.Type
    kNotUpdated: ErrorProto.Type
    kAbort: ErrorProto.Type
    kStaleSessionId: ErrorProto.Type
    kSlaveConfigNotUpdated: ErrorProto.Type
    kForceIndex: ErrorProto.Type
    kIndexableFieldsChanged: ErrorProto.Type
    kBusy: ErrorProto.Type
    kLuceneserverInternalError: ErrorProto.Type
    kStaleCookie: ErrorProto.Type
    kBucketReplicasUnavailable: ErrorProto.Type
    kTagOpOnNonExistentDocument: ErrorProto.Type
    kTagOpOnNonExistentSnapshot: ErrorProto.Type
    kTagOpInvalidArgument: ErrorProto.Type
    kLuceneMaxClauseCount: ErrorProto.Type
    kReassignmentNotNeeded: ErrorProto.Type
    kReassign: ErrorProto.Type
    kESDocIdSizeExceeded: ErrorProto.Type
    kESBulkRequestSizeExceeded: ErrorProto.Type
    kDiskNotFound: ErrorProto.Type
    kAwsESError: ErrorProto.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ERROR_DETAIL_FIELD_NUMBER: _ClassVar[int]
    type: ErrorProto.Type
    error_detail: str
    def __init__(self, type: _Optional[_Union[ErrorProto.Type, str]] = ..., error_detail: _Optional[str] = ...) -> None: ...
