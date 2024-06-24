from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ErrorProto(_message.Message):
    __slots__ = ("type", "detail")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNoError: _ClassVar[ErrorProto.Type]
        kTransportError: _ClassVar[ErrorProto.Type]
        kTimeout: _ClassVar[ErrorProto.Type]
        kRetry: _ClassVar[ErrorProto.Type]
        kInvalid: _ClassVar[ErrorProto.Type]
        kCASError: _ClassVar[ErrorProto.Type]
        kNonExistent: _ClassVar[ErrorProto.Type]
        kExists: _ClassVar[ErrorProto.Type]
        kTransactionAborted: _ClassVar[ErrorProto.Type]
        kTransactionAlreadyClosed: _ClassVar[ErrorProto.Type]
        kNoTransaction: _ClassVar[ErrorProto.Type]
        kCreateTransaction: _ClassVar[ErrorProto.Type]
        kNotImplemented: _ClassVar[ErrorProto.Type]
        kProcessDBResults: _ClassVar[ErrorProto.Type]
        kNullPropertyValue: _ClassVar[ErrorProto.Type]
        kNodeOrEdgeVersionMismatch: _ClassVar[ErrorProto.Type]
        kDBError: _ClassVar[ErrorProto.Type]
        kAttachmentError: _ClassVar[ErrorProto.Type]
        kBusy: _ClassVar[ErrorProto.Type]
        kIOError: _ClassVar[ErrorProto.Type]
    kNoError: ErrorProto.Type
    kTransportError: ErrorProto.Type
    kTimeout: ErrorProto.Type
    kRetry: ErrorProto.Type
    kInvalid: ErrorProto.Type
    kCASError: ErrorProto.Type
    kNonExistent: ErrorProto.Type
    kExists: ErrorProto.Type
    kTransactionAborted: ErrorProto.Type
    kTransactionAlreadyClosed: ErrorProto.Type
    kNoTransaction: ErrorProto.Type
    kCreateTransaction: ErrorProto.Type
    kNotImplemented: ErrorProto.Type
    kProcessDBResults: ErrorProto.Type
    kNullPropertyValue: ErrorProto.Type
    kNodeOrEdgeVersionMismatch: ErrorProto.Type
    kDBError: ErrorProto.Type
    kAttachmentError: ErrorProto.Type
    kBusy: ErrorProto.Type
    kIOError: ErrorProto.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DETAIL_FIELD_NUMBER: _ClassVar[int]
    type: ErrorProto.Type
    detail: str
    def __init__(self, type: _Optional[_Union[ErrorProto.Type, str]] = ..., detail: _Optional[str] = ...) -> None: ...
