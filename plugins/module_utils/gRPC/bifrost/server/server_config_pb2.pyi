from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ServerConfigProto(_message.Message):
    __slots__ = ("connection_config_vec",)
    class ConnectionConfig(_message.Message):
        __slots__ = ("vip_vec", "host_name", "broker_port", "bridge_port", "bridge_secure_port", "cluster_cert", "self_cert", "self_cert_private_key", "self_cert_priv_key_encrypted", "tenant_id", "network_realm_id", "cluster_id", "is_reverse_tunnel_enabled", "grpc_server_common_name")
        VIP_VEC_FIELD_NUMBER: _ClassVar[int]
        HOST_NAME_FIELD_NUMBER: _ClassVar[int]
        BROKER_PORT_FIELD_NUMBER: _ClassVar[int]
        BRIDGE_PORT_FIELD_NUMBER: _ClassVar[int]
        BRIDGE_SECURE_PORT_FIELD_NUMBER: _ClassVar[int]
        CLUSTER_CERT_FIELD_NUMBER: _ClassVar[int]
        SELF_CERT_FIELD_NUMBER: _ClassVar[int]
        SELF_CERT_PRIVATE_KEY_FIELD_NUMBER: _ClassVar[int]
        SELF_CERT_PRIV_KEY_ENCRYPTED_FIELD_NUMBER: _ClassVar[int]
        TENANT_ID_FIELD_NUMBER: _ClassVar[int]
        NETWORK_REALM_ID_FIELD_NUMBER: _ClassVar[int]
        CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
        IS_REVERSE_TUNNEL_ENABLED_FIELD_NUMBER: _ClassVar[int]
        GRPC_SERVER_COMMON_NAME_FIELD_NUMBER: _ClassVar[int]
        vip_vec: _containers.RepeatedScalarFieldContainer[str]
        host_name: str
        broker_port: int
        bridge_port: int
        bridge_secure_port: int
        cluster_cert: str
        self_cert: str
        self_cert_private_key: bytes
        self_cert_priv_key_encrypted: bytes
        tenant_id: str
        network_realm_id: int
        cluster_id: int
        is_reverse_tunnel_enabled: bool
        grpc_server_common_name: str
        def __init__(self, vip_vec: _Optional[_Iterable[str]] = ..., host_name: _Optional[str] = ..., broker_port: _Optional[int] = ..., bridge_port: _Optional[int] = ..., bridge_secure_port: _Optional[int] = ..., cluster_cert: _Optional[str] = ..., self_cert: _Optional[str] = ..., self_cert_private_key: _Optional[bytes] = ..., self_cert_priv_key_encrypted: _Optional[bytes] = ..., tenant_id: _Optional[str] = ..., network_realm_id: _Optional[int] = ..., cluster_id: _Optional[int] = ..., is_reverse_tunnel_enabled: bool = ..., grpc_server_common_name: _Optional[str] = ...) -> None: ...
    CONNECTION_CONFIG_VEC_FIELD_NUMBER: _ClassVar[int]
    connection_config_vec: _containers.RepeatedCompositeFieldContainer[ServerConfigProto.ConnectionConfig]
    def __init__(self, connection_config_vec: _Optional[_Iterable[_Union[ServerConfigProto.ConnectionConfig, _Mapping]]] = ...) -> None: ...
