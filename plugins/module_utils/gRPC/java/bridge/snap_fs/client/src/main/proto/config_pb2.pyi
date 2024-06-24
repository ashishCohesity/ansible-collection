from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CertificateProto(_message.Message):
    __slots__ = ("connection_config_vec",)
    class ConnectionConfig(_message.Message):
        __slots__ = ("cluster_cert", "self_cert", "self_cert_priv_key_encrypted", "tenant_id", "cluster_id", "grpc_server_common_name")
        CLUSTER_CERT_FIELD_NUMBER: _ClassVar[int]
        SELF_CERT_FIELD_NUMBER: _ClassVar[int]
        SELF_CERT_PRIV_KEY_ENCRYPTED_FIELD_NUMBER: _ClassVar[int]
        TENANT_ID_FIELD_NUMBER: _ClassVar[int]
        CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
        GRPC_SERVER_COMMON_NAME_FIELD_NUMBER: _ClassVar[int]
        cluster_cert: str
        self_cert: str
        self_cert_priv_key_encrypted: bytes
        tenant_id: str
        cluster_id: int
        grpc_server_common_name: str
        def __init__(self, cluster_cert: _Optional[str] = ..., self_cert: _Optional[str] = ..., self_cert_priv_key_encrypted: _Optional[bytes] = ..., tenant_id: _Optional[str] = ..., cluster_id: _Optional[int] = ..., grpc_server_common_name: _Optional[str] = ...) -> None: ...
    CONNECTION_CONFIG_VEC_FIELD_NUMBER: _ClassVar[int]
    connection_config_vec: _containers.RepeatedCompositeFieldContainer[CertificateProto.ConnectionConfig]
    def __init__(self, connection_config_vec: _Optional[_Iterable[_Union[CertificateProto.ConnectionConfig, _Mapping]]] = ...) -> None: ...

class EncryptHeader(_message.Message):
    __slots__ = ("iv", "morphed_data_length", "key")
    IV_FIELD_NUMBER: _ClassVar[int]
    MORPHED_DATA_LENGTH_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    iv: bytes
    morphed_data_length: int
    key: bytes
    def __init__(self, iv: _Optional[bytes] = ..., morphed_data_length: _Optional[int] = ..., key: _Optional[bytes] = ...) -> None: ...
