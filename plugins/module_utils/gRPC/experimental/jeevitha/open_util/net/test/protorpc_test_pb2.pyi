from open_util.net import protorpc_pb2 as _protorpc_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ErrorProto(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kNoError: _ClassVar[ErrorProto]
    kRetry: _ClassVar[ErrorProto]
    kTimeout: _ClassVar[ErrorProto]
    kTransportError: _ClassVar[ErrorProto]
    kAppError1: _ClassVar[ErrorProto]
    kAppError2: _ClassVar[ErrorProto]
kNoError: ErrorProto
kRetry: ErrorProto
kTimeout: ErrorProto
kTransportError: ErrorProto
kAppError1: ErrorProto
kAppError2: ErrorProto

class Proc1Arg(_message.Message):
    __slots__ = ("val", "data", "delay_ms", "send_app_error", "send_app_error_detail", "include_app_error_data", "local_transport")
    VAL_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    DELAY_MS_FIELD_NUMBER: _ClassVar[int]
    SEND_APP_ERROR_FIELD_NUMBER: _ClassVar[int]
    SEND_APP_ERROR_DETAIL_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_APP_ERROR_DATA_FIELD_NUMBER: _ClassVar[int]
    LOCAL_TRANSPORT_FIELD_NUMBER: _ClassVar[int]
    val: int
    data: str
    delay_ms: int
    send_app_error: int
    send_app_error_detail: str
    include_app_error_data: bool
    local_transport: bool
    def __init__(self, val: _Optional[int] = ..., data: _Optional[str] = ..., delay_ms: _Optional[int] = ..., send_app_error: _Optional[int] = ..., send_app_error_detail: _Optional[str] = ..., include_app_error_data: bool = ..., local_transport: bool = ...) -> None: ...

class Proc1Result(_message.Message):
    __slots__ = ("val", "data")
    VAL_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    val: int
    data: str
    def __init__(self, val: _Optional[int] = ..., data: _Optional[str] = ...) -> None: ...

class Proc2Arg(_message.Message):
    __slots__ = ("delay_ms", "local_transport")
    DELAY_MS_FIELD_NUMBER: _ClassVar[int]
    LOCAL_TRANSPORT_FIELD_NUMBER: _ClassVar[int]
    delay_ms: int
    local_transport: bool
    def __init__(self, delay_ms: _Optional[int] = ..., local_transport: bool = ...) -> None: ...

class Proc2Result(_message.Message):
    __slots__ = ("delay_str",)
    DELAY_STR_FIELD_NUMBER: _ClassVar[int]
    delay_str: str
    def __init__(self, delay_str: _Optional[str] = ...) -> None: ...

class Proc3Arg(_message.Message):
    __slots__ = ("terminate", "local_transport", "client_send_time")
    TERMINATE_FIELD_NUMBER: _ClassVar[int]
    LOCAL_TRANSPORT_FIELD_NUMBER: _ClassVar[int]
    CLIENT_SEND_TIME_FIELD_NUMBER: _ClassVar[int]
    terminate: bool
    local_transport: bool
    client_send_time: int
    def __init__(self, terminate: bool = ..., local_transport: bool = ..., client_send_time: _Optional[int] = ...) -> None: ...

class Proc3Result(_message.Message):
    __slots__ = ("terminate", "server_resp_time")
    TERMINATE_FIELD_NUMBER: _ClassVar[int]
    SERVER_RESP_TIME_FIELD_NUMBER: _ClassVar[int]
    terminate: bool
    server_resp_time: int
    def __init__(self, terminate: bool = ..., server_resp_time: _Optional[int] = ...) -> None: ...
