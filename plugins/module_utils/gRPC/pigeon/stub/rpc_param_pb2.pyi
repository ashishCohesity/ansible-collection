from open_util.net import protorpc_pb2 as _protorpc_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TcpEndpointProto(_message.Message):
    __slots__ = ("ip", "port", "ip_DEPRECATED")
    IP_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    IP_DEPRECATED_FIELD_NUMBER: _ClassVar[int]
    ip: str
    port: int
    ip_DEPRECATED: str
    def __init__(self, ip: _Optional[str] = ..., port: _Optional[int] = ..., ip_DEPRECATED: _Optional[str] = ...) -> None: ...

class QueryRemoteClusterInfoArg(_message.Message):
    __slots__ = ("tx_cluster_id",)
    TX_CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    tx_cluster_id: int
    def __init__(self, tx_cluster_id: _Optional[int] = ...) -> None: ...

class QueryRemoteClusterInfoResult(_message.Message):
    __slots__ = ("cluster_id", "cluster_incarnation_id", "kek_configured", "cluster_version_supports_encryption", "cluster_aes_encryption_mode")
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    KEK_CONFIGURED_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_VERSION_SUPPORTS_ENCRYPTION_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_AES_ENCRYPTION_MODE_FIELD_NUMBER: _ClassVar[int]
    cluster_id: int
    cluster_incarnation_id: int
    kek_configured: bool
    cluster_version_supports_encryption: bool
    cluster_aes_encryption_mode: int
    def __init__(self, cluster_id: _Optional[int] = ..., cluster_incarnation_id: _Optional[int] = ..., kek_configured: bool = ..., cluster_version_supports_encryption: bool = ..., cluster_aes_encryption_mode: _Optional[int] = ...) -> None: ...

class Status(_message.Message):
    __slots__ = ("type", "error_detail")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ERROR_DETAIL_FIELD_NUMBER: _ClassVar[int]
    type: _protorpc_pb2.ProtoRpcStatus.Type
    error_detail: str
    def __init__(self, type: _Optional[_Union[_protorpc_pb2.ProtoRpcStatus.Type, str]] = ..., error_detail: _Optional[str] = ...) -> None: ...

class RemoteRequestArg(_message.Message):
    __slots__ = ("tx_cluster_id", "expected_rx_cluster_id", "expected_rx_cluster_incarnation_id", "rx_tcp_endpt", "data", "payload_encrypted")
    TX_CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_RX_CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_RX_CLUSTER_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    RX_TCP_ENDPT_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_ENCRYPTED_FIELD_NUMBER: _ClassVar[int]
    tx_cluster_id: int
    expected_rx_cluster_id: int
    expected_rx_cluster_incarnation_id: int
    rx_tcp_endpt: TcpEndpointProto
    data: bytes
    payload_encrypted: bool
    def __init__(self, tx_cluster_id: _Optional[int] = ..., expected_rx_cluster_id: _Optional[int] = ..., expected_rx_cluster_incarnation_id: _Optional[int] = ..., rx_tcp_endpt: _Optional[_Union[TcpEndpointProto, _Mapping]] = ..., data: _Optional[bytes] = ..., payload_encrypted: bool = ...) -> None: ...

class RemoteRequestResult(_message.Message):
    __slots__ = ("status", "rx_cluster_details_mismatch", "data")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    RX_CLUSTER_DETAILS_MISMATCH_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    status: Status
    rx_cluster_details_mismatch: bool
    data: bytes
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ..., rx_cluster_details_mismatch: bool = ..., data: _Optional[bytes] = ...) -> None: ...
