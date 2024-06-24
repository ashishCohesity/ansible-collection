from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GcpCredentials(_message.Message):
    __slots__ = ("project_id", "client_email_address", "encrypted_client_private_key", "type", "private_key_id", "client_id", "auth_uri", "token_uri", "auth_provider_x509_cert_url", "client_x509_cert_url")
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_EMAIL_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTED_CLIENT_PRIVATE_KEY_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_KEY_ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    AUTH_URI_FIELD_NUMBER: _ClassVar[int]
    TOKEN_URI_FIELD_NUMBER: _ClassVar[int]
    AUTH_PROVIDER_X509_CERT_URL_FIELD_NUMBER: _ClassVar[int]
    CLIENT_X509_CERT_URL_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    client_email_address: str
    encrypted_client_private_key: bytes
    type: str
    private_key_id: str
    client_id: str
    auth_uri: str
    token_uri: str
    auth_provider_x509_cert_url: str
    client_x509_cert_url: str
    def __init__(self, project_id: _Optional[str] = ..., client_email_address: _Optional[str] = ..., encrypted_client_private_key: _Optional[bytes] = ..., type: _Optional[str] = ..., private_key_id: _Optional[str] = ..., client_id: _Optional[str] = ..., auth_uri: _Optional[str] = ..., token_uri: _Optional[str] = ..., auth_provider_x509_cert_url: _Optional[str] = ..., client_x509_cert_url: _Optional[str] = ...) -> None: ...

class Credentials(_message.Message):
    __slots__ = ("gcp_credentials",)
    GCP_CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    gcp_credentials: GcpCredentials
    def __init__(self, gcp_credentials: _Optional[_Union[GcpCredentials, _Mapping]] = ...) -> None: ...
