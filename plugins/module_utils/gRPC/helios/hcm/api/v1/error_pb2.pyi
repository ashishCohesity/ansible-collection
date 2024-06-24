from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ApiErrorType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NotSetApiErrorType: _ClassVar[ApiErrorType]
    AccessDenied: _ClassVar[ApiErrorType]
    CAExpired: _ClassVar[ApiErrorType]
    CAServerUnreachable: _ClassVar[ApiErrorType]
    CertAlreadyExists: _ClassVar[ApiErrorType]
    CertDoesNotExist: _ClassVar[ApiErrorType]
    DocumentStoreUnavailable: _ClassVar[ApiErrorType]
    TokenAlreadyExists: _ClassVar[ApiErrorType]
    TokenAlreadyExpired: _ClassVar[ApiErrorType]
    TokenDoesNotExist: _ClassVar[ApiErrorType]
    TokenInvalidError: _ClassVar[ApiErrorType]
    InvalidRequest: _ClassVar[ApiErrorType]
    InternalError: _ClassVar[ApiErrorType]
    RateLimitExceeded: _ClassVar[ApiErrorType]
NotSetApiErrorType: ApiErrorType
AccessDenied: ApiErrorType
CAExpired: ApiErrorType
CAServerUnreachable: ApiErrorType
CertAlreadyExists: ApiErrorType
CertDoesNotExist: ApiErrorType
DocumentStoreUnavailable: ApiErrorType
TokenAlreadyExists: ApiErrorType
TokenAlreadyExpired: ApiErrorType
TokenDoesNotExist: ApiErrorType
TokenInvalidError: ApiErrorType
InvalidRequest: ApiErrorType
InternalError: ApiErrorType
RateLimitExceeded: ApiErrorType

class HCMApiError(_message.Message):
    __slots__ = ("error_type", "error_msg", "is_retryable")
    ERROR_TYPE_FIELD_NUMBER: _ClassVar[int]
    ERROR_MSG_FIELD_NUMBER: _ClassVar[int]
    IS_RETRYABLE_FIELD_NUMBER: _ClassVar[int]
    error_type: ApiErrorType
    error_msg: str
    is_retryable: bool
    def __init__(self, error_type: _Optional[_Union[ApiErrorType, str]] = ..., error_msg: _Optional[str] = ..., is_retryable: bool = ...) -> None: ...
