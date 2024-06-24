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
        kGenericError: _ClassVar[ErrorProto.Type]
        kRemoteConnectionError: _ClassVar[ErrorProto.Type]
        kBuildError: _ClassVar[ErrorProto.Type]
        kArtifactDownloadError: _ClassVar[ErrorProto.Type]
    kNoError: ErrorProto.Type
    kGenericError: ErrorProto.Type
    kRemoteConnectionError: ErrorProto.Type
    kBuildError: ErrorProto.Type
    kArtifactDownloadError: ErrorProto.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ERROR_MSG_FIELD_NUMBER: _ClassVar[int]
    type: ErrorProto.Type
    error_msg: str
    def __init__(self, type: _Optional[_Union[ErrorProto.Type, str]] = ..., error_msg: _Optional[str] = ...) -> None: ...
