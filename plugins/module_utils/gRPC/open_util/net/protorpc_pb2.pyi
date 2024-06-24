from google.protobuf import descriptor_pb2 as _descriptor_pb2
from open_util.base import compression_types_pb2 as _compression_types_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor
DEFAULT_TIMEOUT_MSECS_FIELD_NUMBER: _ClassVar[int]
default_timeout_msecs: _descriptor.FieldDescriptor
DEFAULT_TIMEOUT_EXPONENTIAL_BACKOFF_FIELD_NUMBER: _ClassVar[int]
default_timeout_exponential_backoff: _descriptor.FieldDescriptor
DEFAULT_TIMEOUT_MAX_RETRIES_FIELD_NUMBER: _ClassVar[int]
default_timeout_max_retries: _descriptor.FieldDescriptor
DEFAULT_ENABLE_RETRY_ON_CONNECTION_TERMINATION_FIELD_NUMBER: _ClassVar[int]
default_enable_retry_on_connection_termination: _descriptor.FieldDescriptor
DEFAULT_COMPRESSION_TYPE_FIELD_NUMBER: _ClassVar[int]
default_compression_type: _descriptor.FieldDescriptor
TIMEOUT_MSECS_FIELD_NUMBER: _ClassVar[int]
timeout_msecs: _descriptor.FieldDescriptor
TIMEOUT_EXPONENTIAL_BACKOFF_FIELD_NUMBER: _ClassVar[int]
timeout_exponential_backoff: _descriptor.FieldDescriptor
TIMEOUT_MAX_RETRIES_FIELD_NUMBER: _ClassVar[int]
timeout_max_retries: _descriptor.FieldDescriptor
ENABLE_RETRY_ON_CONNECTION_TERMINATION_FIELD_NUMBER: _ClassVar[int]
enable_retry_on_connection_termination: _descriptor.FieldDescriptor
COMPRESSION_TYPE_FIELD_NUMBER: _ClassVar[int]
compression_type: _descriptor.FieldDescriptor

class ProtoRpcId(_message.Message):
    __slots__ = ("incarnation_id", "request_id", "cluster_id", "constituent_id")
    INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    CONSTITUENT_ID_FIELD_NUMBER: _ClassVar[int]
    incarnation_id: int
    request_id: int
    cluster_id: int
    constituent_id: int
    def __init__(self, incarnation_id: _Optional[int] = ..., request_id: _Optional[int] = ..., cluster_id: _Optional[int] = ..., constituent_id: _Optional[int] = ...) -> None: ...

class IpInfo(_message.Message):
    __slots__ = ("ip", "epoch")
    IP_FIELD_NUMBER: _ClassVar[int]
    EPOCH_FIELD_NUMBER: _ClassVar[int]
    ip: str
    epoch: int
    def __init__(self, ip: _Optional[str] = ..., epoch: _Optional[int] = ...) -> None: ...

class SlicedEncryptionInfo(_message.Message):
    __slots__ = ("sliced_enc_ver", "num_enc_slices", "slice_size")
    SLICED_ENC_VER_FIELD_NUMBER: _ClassVar[int]
    NUM_ENC_SLICES_FIELD_NUMBER: _ClassVar[int]
    SLICE_SIZE_FIELD_NUMBER: _ClassVar[int]
    sliced_enc_ver: int
    num_enc_slices: int
    slice_size: int
    def __init__(self, sliced_enc_ver: _Optional[int] = ..., num_enc_slices: _Optional[int] = ..., slice_size: _Optional[int] = ...) -> None: ...

class ProtoRpcChecksum(_message.Message):
    __slots__ = ("type", "checksum")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kUnknown: _ClassVar[ProtoRpcChecksum.Type]
        kCRC32: _ClassVar[ProtoRpcChecksum.Type]
    kUnknown: ProtoRpcChecksum.Type
    kCRC32: ProtoRpcChecksum.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    CHECKSUM_FIELD_NUMBER: _ClassVar[int]
    type: ProtoRpcChecksum.Type
    checksum: bytes
    def __init__(self, type: _Optional[_Union[ProtoRpcChecksum.Type, str]] = ..., checksum: _Optional[bytes] = ...) -> None: ...

class ProtoRpcRequestHeader(_message.Message):
    __slots__ = ("service_name", "method_name", "protorpc_id", "client_send_time_usecs", "timeout_msecs", "arg_proto_size", "arg_payload_size", "notification_listen_port", "min_progress_notification_interval_secs", "compression_type", "encryption_key_locator", "sender_ip_info", "auth_token", "sliced_enc_info")
    SERVICE_NAME_FIELD_NUMBER: _ClassVar[int]
    METHOD_NAME_FIELD_NUMBER: _ClassVar[int]
    PROTORPC_ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_SEND_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_MSECS_FIELD_NUMBER: _ClassVar[int]
    ARG_PROTO_SIZE_FIELD_NUMBER: _ClassVar[int]
    ARG_PAYLOAD_SIZE_FIELD_NUMBER: _ClassVar[int]
    NOTIFICATION_LISTEN_PORT_FIELD_NUMBER: _ClassVar[int]
    MIN_PROGRESS_NOTIFICATION_INTERVAL_SECS_FIELD_NUMBER: _ClassVar[int]
    COMPRESSION_TYPE_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_KEY_LOCATOR_FIELD_NUMBER: _ClassVar[int]
    SENDER_IP_INFO_FIELD_NUMBER: _ClassVar[int]
    AUTH_TOKEN_FIELD_NUMBER: _ClassVar[int]
    SLICED_ENC_INFO_FIELD_NUMBER: _ClassVar[int]
    service_name: str
    method_name: str
    protorpc_id: ProtoRpcId
    client_send_time_usecs: int
    timeout_msecs: int
    arg_proto_size: int
    arg_payload_size: int
    notification_listen_port: int
    min_progress_notification_interval_secs: int
    compression_type: _compression_types_pb2.CompressionProto.Type
    encryption_key_locator: bytes
    sender_ip_info: IpInfo
    auth_token: bytes
    sliced_enc_info: SlicedEncryptionInfo
    def __init__(self, service_name: _Optional[str] = ..., method_name: _Optional[str] = ..., protorpc_id: _Optional[_Union[ProtoRpcId, _Mapping]] = ..., client_send_time_usecs: _Optional[int] = ..., timeout_msecs: _Optional[int] = ..., arg_proto_size: _Optional[int] = ..., arg_payload_size: _Optional[int] = ..., notification_listen_port: _Optional[int] = ..., min_progress_notification_interval_secs: _Optional[int] = ..., compression_type: _Optional[_Union[_compression_types_pb2.CompressionProto.Type, str]] = ..., encryption_key_locator: _Optional[bytes] = ..., sender_ip_info: _Optional[_Union[IpInfo, _Mapping]] = ..., auth_token: _Optional[bytes] = ..., sliced_enc_info: _Optional[_Union[SlicedEncryptionInfo, _Mapping]] = ...) -> None: ...

class ProtoRpcStatus(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNoError: _ClassVar[ProtoRpcStatus.Type]
        kTimeout: _ClassVar[ProtoRpcStatus.Type]
        kTransportError: _ClassVar[ProtoRpcStatus.Type]
        kServiceError: _ClassVar[ProtoRpcStatus.Type]
        kMethodError: _ClassVar[ProtoRpcStatus.Type]
        kAppError: _ClassVar[ProtoRpcStatus.Type]
    kNoError: ProtoRpcStatus.Type
    kTimeout: ProtoRpcStatus.Type
    kTransportError: ProtoRpcStatus.Type
    kServiceError: ProtoRpcStatus.Type
    kMethodError: ProtoRpcStatus.Type
    kAppError: ProtoRpcStatus.Type
    class MethodErrorReason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kMethodNotFound: _ClassVar[ProtoRpcStatus.MethodErrorReason]
        kEncryptionKeyNotFound: _ClassVar[ProtoRpcStatus.MethodErrorReason]
    kMethodNotFound: ProtoRpcStatus.MethodErrorReason
    kEncryptionKeyNotFound: ProtoRpcStatus.MethodErrorReason
    def __init__(self) -> None: ...

class ProtoRpcResponseHeader(_message.Message):
    __slots__ = ("status", "protorpc_id", "error_detail", "app_error", "result_proto_size", "result_payload_size", "method_error_reason", "app_exec_time_usecs", "server_recv_time_usecs", "sliced_enc_info")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    PROTORPC_ID_FIELD_NUMBER: _ClassVar[int]
    ERROR_DETAIL_FIELD_NUMBER: _ClassVar[int]
    APP_ERROR_FIELD_NUMBER: _ClassVar[int]
    RESULT_PROTO_SIZE_FIELD_NUMBER: _ClassVar[int]
    RESULT_PAYLOAD_SIZE_FIELD_NUMBER: _ClassVar[int]
    METHOD_ERROR_REASON_FIELD_NUMBER: _ClassVar[int]
    APP_EXEC_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    SERVER_RECV_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    SLICED_ENC_INFO_FIELD_NUMBER: _ClassVar[int]
    status: ProtoRpcStatus.Type
    protorpc_id: ProtoRpcId
    error_detail: str
    app_error: int
    result_proto_size: int
    result_payload_size: int
    method_error_reason: ProtoRpcStatus.MethodErrorReason
    app_exec_time_usecs: int
    server_recv_time_usecs: int
    sliced_enc_info: SlicedEncryptionInfo
    def __init__(self, status: _Optional[_Union[ProtoRpcStatus.Type, str]] = ..., protorpc_id: _Optional[_Union[ProtoRpcId, _Mapping]] = ..., error_detail: _Optional[str] = ..., app_error: _Optional[int] = ..., result_proto_size: _Optional[int] = ..., result_payload_size: _Optional[int] = ..., method_error_reason: _Optional[_Union[ProtoRpcStatus.MethodErrorReason, str]] = ..., app_exec_time_usecs: _Optional[int] = ..., server_recv_time_usecs: _Optional[int] = ..., sliced_enc_info: _Optional[_Union[SlicedEncryptionInfo, _Mapping]] = ...) -> None: ...

class ProtoRpcBinaryLogHeader(_message.Message):
    __slots__ = ("peer_transport_endpoint", "local_transport_endpoint", "server_sequence_id")
    PEER_TRANSPORT_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    LOCAL_TRANSPORT_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    SERVER_SEQUENCE_ID_FIELD_NUMBER: _ClassVar[int]
    peer_transport_endpoint: str
    local_transport_endpoint: str
    server_sequence_id: int
    def __init__(self, peer_transport_endpoint: _Optional[str] = ..., local_transport_endpoint: _Optional[str] = ..., server_sequence_id: _Optional[int] = ...) -> None: ...

class ProtoRpcApiList(_message.Message):
    __slots__ = ("port_vec",)
    class SvcInfo(_message.Message):
        __slots__ = ("svc_full_name", "method_name_vec", "all_methods")
        SVC_FULL_NAME_FIELD_NUMBER: _ClassVar[int]
        METHOD_NAME_VEC_FIELD_NUMBER: _ClassVar[int]
        ALL_METHODS_FIELD_NUMBER: _ClassVar[int]
        svc_full_name: str
        method_name_vec: _containers.RepeatedScalarFieldContainer[str]
        all_methods: bool
        def __init__(self, svc_full_name: _Optional[str] = ..., method_name_vec: _Optional[_Iterable[str]] = ..., all_methods: bool = ...) -> None: ...
    class PortInfo(_message.Message):
        __slots__ = ("server_port", "svc_vec")
        SERVER_PORT_FIELD_NUMBER: _ClassVar[int]
        SVC_VEC_FIELD_NUMBER: _ClassVar[int]
        server_port: int
        svc_vec: _containers.RepeatedCompositeFieldContainer[ProtoRpcApiList.SvcInfo]
        def __init__(self, server_port: _Optional[int] = ..., svc_vec: _Optional[_Iterable[_Union[ProtoRpcApiList.SvcInfo, _Mapping]]] = ...) -> None: ...
    PORT_VEC_FIELD_NUMBER: _ClassVar[int]
    port_vec: _containers.RepeatedCompositeFieldContainer[ProtoRpcApiList.PortInfo]
    def __init__(self, port_vec: _Optional[_Iterable[_Union[ProtoRpcApiList.PortInfo, _Mapping]]] = ...) -> None: ...
