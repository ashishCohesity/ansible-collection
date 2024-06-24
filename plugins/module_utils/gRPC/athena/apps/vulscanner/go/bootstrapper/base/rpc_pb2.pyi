from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PrepareVolumeRequest(_message.Message):
    __slots__ = ("image_file_path", "username", "ssh_key", "swap_mountpoint", "convert_image_raw")
    IMAGE_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    SSH_KEY_FIELD_NUMBER: _ClassVar[int]
    SWAP_MOUNTPOINT_FIELD_NUMBER: _ClassVar[int]
    CONVERT_IMAGE_RAW_FIELD_NUMBER: _ClassVar[int]
    image_file_path: str
    username: str
    ssh_key: bytes
    swap_mountpoint: str
    convert_image_raw: bool
    def __init__(self, image_file_path: _Optional[str] = ..., username: _Optional[str] = ..., ssh_key: _Optional[bytes] = ..., swap_mountpoint: _Optional[str] = ..., convert_image_raw: bool = ...) -> None: ...

class PrepareVolumeResult(_message.Message):
    __slots__ = ("is_invalid_request", "error")
    IS_INVALID_REQUEST_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    is_invalid_request: bool
    error: PrepareError
    def __init__(self, is_invalid_request: bool = ..., error: _Optional[_Union[PrepareError, _Mapping]] = ...) -> None: ...

class PrepareError(_message.Message):
    __slots__ = ("error_code", "details")
    class Error(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        INVALID_IMAGE_PATH: _ClassVar[PrepareError.Error]
        INVALID_USERNAME: _ClassVar[PrepareError.Error]
        INVALID_SSH_KEY: _ClassVar[PrepareError.Error]
        INVALID_SWAP_MOUNTPOINT: _ClassVar[PrepareError.Error]
        NO_TRANSFORMATION_ARGUMENT_PRESENT: _ClassVar[PrepareError.Error]
        TIMEOUT: _ClassVar[PrepareError.Error]
        INTERNAL_ERROR: _ClassVar[PrepareError.Error]
    INVALID_IMAGE_PATH: PrepareError.Error
    INVALID_USERNAME: PrepareError.Error
    INVALID_SSH_KEY: PrepareError.Error
    INVALID_SWAP_MOUNTPOINT: PrepareError.Error
    NO_TRANSFORMATION_ARGUMENT_PRESENT: PrepareError.Error
    TIMEOUT: PrepareError.Error
    INTERNAL_ERROR: PrepareError.Error
    ERROR_CODE_FIELD_NUMBER: _ClassVar[int]
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    error_code: PrepareError.Error
    details: str
    def __init__(self, error_code: _Optional[_Union[PrepareError.Error, str]] = ..., details: _Optional[str] = ...) -> None: ...

class GetStatusRequest(_message.Message):
    __slots__ = ("image_file_path",)
    IMAGE_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    image_file_path: str
    def __init__(self, image_file_path: _Optional[str] = ...) -> None: ...

class GetStatusResult(_message.Message):
    __slots__ = ("status", "error")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        COMPLETED: _ClassVar[GetStatusResult.Status]
        FAILED: _ClassVar[GetStatusResult.Status]
        RUNNING: _ClassVar[GetStatusResult.Status]
        NOT_STARTED: _ClassVar[GetStatusResult.Status]
    COMPLETED: GetStatusResult.Status
    FAILED: GetStatusResult.Status
    RUNNING: GetStatusResult.Status
    NOT_STARTED: GetStatusResult.Status
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    status: GetStatusResult.Status
    error: PrepareError
    def __init__(self, status: _Optional[_Union[GetStatusResult.Status, str]] = ..., error: _Optional[_Union[PrepareError, _Mapping]] = ...) -> None: ...

class DeleteStatusRequest(_message.Message):
    __slots__ = ("image_file_path",)
    IMAGE_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    image_file_path: str
    def __init__(self, image_file_path: _Optional[str] = ...) -> None: ...

class DeleteStatusResult(_message.Message):
    __slots__ = ("response",)
    class Response(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        COMPLETED: _ClassVar[DeleteStatusResult.Response]
        PREPARE_RUNNING: _ClassVar[DeleteStatusResult.Response]
    COMPLETED: DeleteStatusResult.Response
    PREPARE_RUNNING: DeleteStatusResult.Response
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    response: DeleteStatusResult.Response
    def __init__(self, response: _Optional[_Union[DeleteStatusResult.Response, str]] = ...) -> None: ...
