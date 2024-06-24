from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ErrorProto(_message.Message):
    __slots__ = ("type", "detail")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kInvalidEnumValue: _ClassVar[ErrorProto.Type]
        kNoError: _ClassVar[ErrorProto.Type]
        kDirWalkerError: _ClassVar[ErrorProto.Type]
        kDirWalkerFatalError: _ClassVar[ErrorProto.Type]
        kDirectoryDifferError: _ClassVar[ErrorProto.Type]
        kTaskRunnerError: _ClassVar[ErrorProto.Type]
        kMinionError: _ClassVar[ErrorProto.Type]
        kMountError: _ClassVar[ErrorProto.Type]
        kIOError: _ClassVar[ErrorProto.Type]
        kElasticError: _ClassVar[ErrorProto.Type]
        kCanceled: _ClassVar[ErrorProto.Type]
        kValidationError: _ClassVar[ErrorProto.Type]
        kNonExistent: _ClassVar[ErrorProto.Type]
        kApiError: _ClassVar[ErrorProto.Type]
    kInvalidEnumValue: ErrorProto.Type
    kNoError: ErrorProto.Type
    kDirWalkerError: ErrorProto.Type
    kDirWalkerFatalError: ErrorProto.Type
    kDirectoryDifferError: ErrorProto.Type
    kTaskRunnerError: ErrorProto.Type
    kMinionError: ErrorProto.Type
    kMountError: ErrorProto.Type
    kIOError: ErrorProto.Type
    kElasticError: ErrorProto.Type
    kCanceled: ErrorProto.Type
    kValidationError: ErrorProto.Type
    kNonExistent: ErrorProto.Type
    kApiError: ErrorProto.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DETAIL_FIELD_NUMBER: _ClassVar[int]
    type: ErrorProto.Type
    detail: str
    def __init__(self, type: _Optional[_Union[ErrorProto.Type, str]] = ..., detail: _Optional[str] = ...) -> None: ...
