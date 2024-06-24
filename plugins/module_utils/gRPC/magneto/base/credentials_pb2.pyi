from magneto.base import enums_pb2 as _enums_pb2
from nexus.cloud.base import credentials_pb2 as _credentials_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NasMountCredentials(_message.Message):
    __slots__ = ("protocol", "username", "password", "encrypted_password", "domain_name", "kdc")
    PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTED_PASSWORD_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    KDC_FIELD_NUMBER: _ClassVar[int]
    protocol: _enums_pb2.NasProtocol.Type
    username: str
    password: str
    encrypted_password: bytes
    domain_name: str
    kdc: str
    def __init__(self, protocol: _Optional[_Union[_enums_pb2.NasProtocol.Type, str]] = ..., username: _Optional[str] = ..., password: _Optional[str] = ..., encrypted_password: _Optional[bytes] = ..., domain_name: _Optional[str] = ..., kdc: _Optional[str] = ...) -> None: ...

class SSLVerification(_message.Message):
    __slots__ = ("enabled", "ca_certificate", "server_sha256_key")
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    CA_CERTIFICATE_FIELD_NUMBER: _ClassVar[int]
    SERVER_SHA256_KEY_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    ca_certificate: str
    server_sha256_key: bytes
    def __init__(self, enabled: bool = ..., ca_certificate: _Optional[str] = ..., server_sha256_key: _Optional[bytes] = ...) -> None: ...

class MSGraphAppCredentials(_message.Message):
    __slots__ = ("client_id", "scope", "client_secret", "grant_type", "encrypted_client_secret", "scope_token_map", "use_outlook_ews_oauth", "display_name", "scope_client_id_map", "cohesity_created", "is_selected")
    class ScopeTokenMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class ScopeClientIdMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    CLIENT_SECRET_FIELD_NUMBER: _ClassVar[int]
    GRANT_TYPE_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTED_CLIENT_SECRET_FIELD_NUMBER: _ClassVar[int]
    SCOPE_TOKEN_MAP_FIELD_NUMBER: _ClassVar[int]
    USE_OUTLOOK_EWS_OAUTH_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    SCOPE_CLIENT_ID_MAP_FIELD_NUMBER: _ClassVar[int]
    COHESITY_CREATED_FIELD_NUMBER: _ClassVar[int]
    IS_SELECTED_FIELD_NUMBER: _ClassVar[int]
    client_id: str
    scope: str
    client_secret: str
    grant_type: str
    encrypted_client_secret: bytes
    scope_token_map: _containers.ScalarMap[str, str]
    use_outlook_ews_oauth: bool
    display_name: str
    scope_client_id_map: _containers.ScalarMap[str, str]
    cohesity_created: bool
    is_selected: bool
    def __init__(self, client_id: _Optional[str] = ..., scope: _Optional[str] = ..., client_secret: _Optional[str] = ..., grant_type: _Optional[str] = ..., encrypted_client_secret: _Optional[bytes] = ..., scope_token_map: _Optional[_Mapping[str, str]] = ..., use_outlook_ews_oauth: bool = ..., display_name: _Optional[str] = ..., scope_client_id_map: _Optional[_Mapping[str, str]] = ..., cohesity_created: bool = ..., is_selected: bool = ...) -> None: ...

class ServiceAccountCredentials(_message.Message):
    __slots__ = ("username", "password", "encrypted_password")
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTED_PASSWORD_FIELD_NUMBER: _ClassVar[int]
    username: str
    password: str
    encrypted_password: bytes
    def __init__(self, username: _Optional[str] = ..., password: _Optional[str] = ..., encrypted_password: _Optional[bytes] = ...) -> None: ...

class CertificateBasedAuthenticationCredentials(_message.Message):
    __slots__ = ("username", "private_key", "passphrase")
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_KEY_FIELD_NUMBER: _ClassVar[int]
    PASSPHRASE_FIELD_NUMBER: _ClassVar[int]
    username: str
    private_key: str
    passphrase: str
    def __init__(self, username: _Optional[str] = ..., private_key: _Optional[str] = ..., passphrase: _Optional[str] = ...) -> None: ...

class Credentials(_message.Message):
    __slots__ = ("username", "password", "encrypted_password", "token", "encrypted_token", "cloud_credentials", "nas_mount_credentials", "ssl_verification", "ms_graph_credentials_vec", "service_account_credentials_vec", "cert_credentials", "validated")
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTED_PASSWORD_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTED_TOKEN_FIELD_NUMBER: _ClassVar[int]
    CLOUD_CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    NAS_MOUNT_CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    SSL_VERIFICATION_FIELD_NUMBER: _ClassVar[int]
    MS_GRAPH_CREDENTIALS_VEC_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNT_CREDENTIALS_VEC_FIELD_NUMBER: _ClassVar[int]
    CERT_CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    VALIDATED_FIELD_NUMBER: _ClassVar[int]
    username: str
    password: str
    encrypted_password: bytes
    token: str
    encrypted_token: bytes
    cloud_credentials: _credentials_pb2.Credentials
    nas_mount_credentials: NasMountCredentials
    ssl_verification: SSLVerification
    ms_graph_credentials_vec: _containers.RepeatedCompositeFieldContainer[MSGraphAppCredentials]
    service_account_credentials_vec: _containers.RepeatedCompositeFieldContainer[ServiceAccountCredentials]
    cert_credentials: CertificateBasedAuthenticationCredentials
    validated: bool
    def __init__(self, username: _Optional[str] = ..., password: _Optional[str] = ..., encrypted_password: _Optional[bytes] = ..., token: _Optional[str] = ..., encrypted_token: _Optional[bytes] = ..., cloud_credentials: _Optional[_Union[_credentials_pb2.Credentials, _Mapping]] = ..., nas_mount_credentials: _Optional[_Union[NasMountCredentials, _Mapping]] = ..., ssl_verification: _Optional[_Union[SSLVerification, _Mapping]] = ..., ms_graph_credentials_vec: _Optional[_Iterable[_Union[MSGraphAppCredentials, _Mapping]]] = ..., service_account_credentials_vec: _Optional[_Iterable[_Union[ServiceAccountCredentials, _Mapping]]] = ..., cert_credentials: _Optional[_Union[CertificateBasedAuthenticationCredentials, _Mapping]] = ..., validated: bool = ...) -> None: ...

class AppCredentials(_message.Message):
    __slots__ = ("env_type", "credentials")
    ENV_TYPE_FIELD_NUMBER: _ClassVar[int]
    CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    env_type: _enums_pb2.Environment.Type
    credentials: Credentials
    def __init__(self, env_type: _Optional[_Union[_enums_pb2.Environment.Type, str]] = ..., credentials: _Optional[_Union[Credentials, _Mapping]] = ...) -> None: ...
