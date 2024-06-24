from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EchoNumberStreamArg(_message.Message):
    __slots__ = ("number",)
    NUMBER_FIELD_NUMBER: _ClassVar[int]
    number: int
    def __init__(self, number: _Optional[int] = ...) -> None: ...

class EchoNumberStreamResult(_message.Message):
    __slots__ = ("number",)
    NUMBER_FIELD_NUMBER: _ClassVar[int]
    number: int
    def __init__(self, number: _Optional[int] = ...) -> None: ...

class ClientAndServerTlsConfig(_message.Message):
    __slots__ = ("server_tls_config", "client_tls_config")
    class TlsConfig(_message.Message):
        __slots__ = ("root_certificates", "key_cert_pair_vec")
        class KeyCertPair(_message.Message):
            __slots__ = ("certificate_chain", "encrypted_private_key", "private_key")
            CERTIFICATE_CHAIN_FIELD_NUMBER: _ClassVar[int]
            ENCRYPTED_PRIVATE_KEY_FIELD_NUMBER: _ClassVar[int]
            PRIVATE_KEY_FIELD_NUMBER: _ClassVar[int]
            certificate_chain: bytes
            encrypted_private_key: bytes
            private_key: bytes
            def __init__(self, certificate_chain: _Optional[bytes] = ..., encrypted_private_key: _Optional[bytes] = ..., private_key: _Optional[bytes] = ...) -> None: ...
        ROOT_CERTIFICATES_FIELD_NUMBER: _ClassVar[int]
        KEY_CERT_PAIR_VEC_FIELD_NUMBER: _ClassVar[int]
        root_certificates: bytes
        key_cert_pair_vec: _containers.RepeatedCompositeFieldContainer[ClientAndServerTlsConfig.TlsConfig.KeyCertPair]
        def __init__(self, root_certificates: _Optional[bytes] = ..., key_cert_pair_vec: _Optional[_Iterable[_Union[ClientAndServerTlsConfig.TlsConfig.KeyCertPair, _Mapping]]] = ...) -> None: ...
    SERVER_TLS_CONFIG_FIELD_NUMBER: _ClassVar[int]
    CLIENT_TLS_CONFIG_FIELD_NUMBER: _ClassVar[int]
    server_tls_config: ClientAndServerTlsConfig.TlsConfig
    client_tls_config: ClientAndServerTlsConfig.TlsConfig
    def __init__(self, server_tls_config: _Optional[_Union[ClientAndServerTlsConfig.TlsConfig, _Mapping]] = ..., client_tls_config: _Optional[_Union[ClientAndServerTlsConfig.TlsConfig, _Mapping]] = ...) -> None: ...
