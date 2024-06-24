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
        kLocalGitError: _ClassVar[ErrorProto.Type]
        kGitPushError: _ClassVar[ErrorProto.Type]
        kGitPruneError: _ClassVar[ErrorProto.Type]
        kGitRemoteConnectionError: _ClassVar[ErrorProto.Type]
        kGitRemoteBranchCheckoutError: _ClassVar[ErrorProto.Type]
        kGitRemoteSha1CheckoutError: _ClassVar[ErrorProto.Type]
        kGitRemoteSetupError: _ClassVar[ErrorProto.Type]
    kNoError: ErrorProto.Type
    kGenericError: ErrorProto.Type
    kLocalGitError: ErrorProto.Type
    kGitPushError: ErrorProto.Type
    kGitPruneError: ErrorProto.Type
    kGitRemoteConnectionError: ErrorProto.Type
    kGitRemoteBranchCheckoutError: ErrorProto.Type
    kGitRemoteSha1CheckoutError: ErrorProto.Type
    kGitRemoteSetupError: ErrorProto.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ERROR_MSG_FIELD_NUMBER: _ClassVar[int]
    type: ErrorProto.Type
    error_msg: str
    def __init__(self, type: _Optional[_Union[ErrorProto.Type, str]] = ..., error_msg: _Optional[str] = ...) -> None: ...
