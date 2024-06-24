from open_util.net import protorpc_pb2 as _protorpc_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

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
    __slots__ = ("val", "data", "delay_ms", "send_app_error", "send_app_error_detail", "include_app_error_data", "local_transport", "include_client_cert_info")
    VAL_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    DELAY_MS_FIELD_NUMBER: _ClassVar[int]
    SEND_APP_ERROR_FIELD_NUMBER: _ClassVar[int]
    SEND_APP_ERROR_DETAIL_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_APP_ERROR_DATA_FIELD_NUMBER: _ClassVar[int]
    LOCAL_TRANSPORT_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_CLIENT_CERT_INFO_FIELD_NUMBER: _ClassVar[int]
    val: int
    data: str
    delay_ms: int
    send_app_error: int
    send_app_error_detail: str
    include_app_error_data: bool
    local_transport: bool
    include_client_cert_info: bool
    def __init__(self, val: _Optional[int] = ..., data: _Optional[str] = ..., delay_ms: _Optional[int] = ..., send_app_error: _Optional[int] = ..., send_app_error_detail: _Optional[str] = ..., include_app_error_data: bool = ..., local_transport: bool = ..., include_client_cert_info: bool = ...) -> None: ...

class Proc1Result(_message.Message):
    __slots__ = ("val", "data", "client_cert_info")
    VAL_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    CLIENT_CERT_INFO_FIELD_NUMBER: _ClassVar[int]
    val: int
    data: str
    client_cert_info: str
    def __init__(self, val: _Optional[int] = ..., data: _Optional[str] = ..., client_cert_info: _Optional[str] = ...) -> None: ...

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
    __slots__ = ("terminate", "local_transport", "repeated_msg_vec", "payload_checksum")
    class RepeatedMsg(_message.Message):
        __slots__ = ("id", "data")
        class Id(_message.Message):
            __slots__ = ("id_int", "id_str")
            ID_INT_FIELD_NUMBER: _ClassVar[int]
            ID_STR_FIELD_NUMBER: _ClassVar[int]
            id_int: int
            id_str: bytes
            def __init__(self, id_int: _Optional[int] = ..., id_str: _Optional[bytes] = ...) -> None: ...
        class Data(_message.Message):
            __slots__ = ("id",)
            ID_FIELD_NUMBER: _ClassVar[int]
            id: Proc3Arg.RepeatedMsg.Id
            def __init__(self, id: _Optional[_Union[Proc3Arg.RepeatedMsg.Id, _Mapping]] = ...) -> None: ...
        ID_FIELD_NUMBER: _ClassVar[int]
        DATA_FIELD_NUMBER: _ClassVar[int]
        id: Proc3Arg.RepeatedMsg.Id
        data: Proc3Arg.RepeatedMsg.Data
        def __init__(self, id: _Optional[_Union[Proc3Arg.RepeatedMsg.Id, _Mapping]] = ..., data: _Optional[_Union[Proc3Arg.RepeatedMsg.Data, _Mapping]] = ...) -> None: ...
    TERMINATE_FIELD_NUMBER: _ClassVar[int]
    LOCAL_TRANSPORT_FIELD_NUMBER: _ClassVar[int]
    REPEATED_MSG_VEC_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_CHECKSUM_FIELD_NUMBER: _ClassVar[int]
    terminate: bool
    local_transport: bool
    repeated_msg_vec: _containers.RepeatedCompositeFieldContainer[Proc3Arg.RepeatedMsg]
    payload_checksum: int
    def __init__(self, terminate: bool = ..., local_transport: bool = ..., repeated_msg_vec: _Optional[_Iterable[_Union[Proc3Arg.RepeatedMsg, _Mapping]]] = ..., payload_checksum: _Optional[int] = ...) -> None: ...

class Proc3Result(_message.Message):
    __slots__ = ("terminate", "payload_checksum", "checksum_enabled_gflag_set")
    TERMINATE_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_CHECKSUM_FIELD_NUMBER: _ClassVar[int]
    CHECKSUM_ENABLED_GFLAG_SET_FIELD_NUMBER: _ClassVar[int]
    terminate: bool
    payload_checksum: int
    checksum_enabled_gflag_set: bool
    def __init__(self, terminate: bool = ..., payload_checksum: _Optional[int] = ..., checksum_enabled_gflag_set: bool = ...) -> None: ...
