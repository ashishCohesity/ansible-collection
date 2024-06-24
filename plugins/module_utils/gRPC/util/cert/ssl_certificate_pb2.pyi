from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ClientServerCert(_message.Message):
    __slots__ = ("cert_pairs",)
    CERT_PAIRS_FIELD_NUMBER: _ClassVar[int]
    cert_pairs: _containers.RepeatedCompositeFieldContainer[ClientServerCertPair]
    def __init__(self, cert_pairs: _Optional[_Iterable[_Union[ClientServerCertPair, _Mapping]]] = ...) -> None: ...

class ClientServerCertPair(_message.Message):
    __slots__ = ("id", "server_cert", "client_cert")
    ID_FIELD_NUMBER: _ClassVar[int]
    SERVER_CERT_FIELD_NUMBER: _ClassVar[int]
    CLIENT_CERT_FIELD_NUMBER: _ClassVar[int]
    id: str
    server_cert: CertificateProto
    client_cert: CertificateProto
    def __init__(self, id: _Optional[str] = ..., server_cert: _Optional[_Union[CertificateProto, _Mapping]] = ..., client_cert: _Optional[_Union[CertificateProto, _Mapping]] = ...) -> None: ...

class CertificateProto(_message.Message):
    __slots__ = ("certificate", "last_import_time_msecs", "csr", "ca_certificates")
    CERTIFICATE_FIELD_NUMBER: _ClassVar[int]
    LAST_IMPORT_TIME_MSECS_FIELD_NUMBER: _ClassVar[int]
    CSR_FIELD_NUMBER: _ClassVar[int]
    CA_CERTIFICATES_FIELD_NUMBER: _ClassVar[int]
    certificate: bytes
    last_import_time_msecs: int
    csr: Csr
    ca_certificates: bytes
    def __init__(self, certificate: _Optional[bytes] = ..., last_import_time_msecs: _Optional[int] = ..., csr: _Optional[_Union[Csr, _Mapping]] = ..., ca_certificates: _Optional[bytes] = ...) -> None: ...

class SslCertificateProto(_message.Message):
    __slots__ = ("certificate", "private_key", "last_update_time_msecs", "web_server_ca_certificates", "web_client_ca_certificates", "version", "helios_certificate_store", "api_public_key", "api_private_key", "csr_vec")
    class HeliosCertificateStore(_message.Message):
        __slots__ = ("cluster_certificate_path", "cluster_private_key_path", "helios_certificate_path", "cluster_certificate", "cluster_private_key", "helios_certificate")
        CLUSTER_CERTIFICATE_PATH_FIELD_NUMBER: _ClassVar[int]
        CLUSTER_PRIVATE_KEY_PATH_FIELD_NUMBER: _ClassVar[int]
        HELIOS_CERTIFICATE_PATH_FIELD_NUMBER: _ClassVar[int]
        CLUSTER_CERTIFICATE_FIELD_NUMBER: _ClassVar[int]
        CLUSTER_PRIVATE_KEY_FIELD_NUMBER: _ClassVar[int]
        HELIOS_CERTIFICATE_FIELD_NUMBER: _ClassVar[int]
        cluster_certificate_path: str
        cluster_private_key_path: str
        helios_certificate_path: str
        cluster_certificate: str
        cluster_private_key: str
        helios_certificate: str
        def __init__(self, cluster_certificate_path: _Optional[str] = ..., cluster_private_key_path: _Optional[str] = ..., helios_certificate_path: _Optional[str] = ..., cluster_certificate: _Optional[str] = ..., cluster_private_key: _Optional[str] = ..., helios_certificate: _Optional[str] = ...) -> None: ...
    CERTIFICATE_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_KEY_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATE_TIME_MSECS_FIELD_NUMBER: _ClassVar[int]
    WEB_SERVER_CA_CERTIFICATES_FIELD_NUMBER: _ClassVar[int]
    WEB_CLIENT_CA_CERTIFICATES_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    HELIOS_CERTIFICATE_STORE_FIELD_NUMBER: _ClassVar[int]
    API_PUBLIC_KEY_FIELD_NUMBER: _ClassVar[int]
    API_PRIVATE_KEY_FIELD_NUMBER: _ClassVar[int]
    CSR_VEC_FIELD_NUMBER: _ClassVar[int]
    certificate: bytes
    private_key: bytes
    last_update_time_msecs: int
    web_server_ca_certificates: _containers.RepeatedScalarFieldContainer[str]
    web_client_ca_certificates: _containers.RepeatedScalarFieldContainer[str]
    version: int
    helios_certificate_store: SslCertificateProto.HeliosCertificateStore
    api_public_key: bytes
    api_private_key: bytes
    csr_vec: _containers.RepeatedCompositeFieldContainer[Csr]
    def __init__(self, certificate: _Optional[bytes] = ..., private_key: _Optional[bytes] = ..., last_update_time_msecs: _Optional[int] = ..., web_server_ca_certificates: _Optional[_Iterable[str]] = ..., web_client_ca_certificates: _Optional[_Iterable[str]] = ..., version: _Optional[int] = ..., helios_certificate_store: _Optional[_Union[SslCertificateProto.HeliosCertificateStore, _Mapping]] = ..., api_public_key: _Optional[bytes] = ..., api_private_key: _Optional[bytes] = ..., csr_vec: _Optional[_Iterable[_Union[Csr, _Mapping]]] = ...) -> None: ...

class Csr(_message.Message):
    __slots__ = ("id", "key_type", "key_size_bits", "common_name", "organization", "organization_unit", "country_code", "state", "city", "dns_names", "host_ips", "email_address", "service_name", "encrypted_private_key", "public_key", "csr", "creationTimeUsecs")
    class Algorithm(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        rsa: _ClassVar[Csr.Algorithm]
        ecdsa: _ClassVar[Csr.Algorithm]
    rsa: Csr.Algorithm
    ecdsa: Csr.Algorithm
    class Service(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        iris: _ClassVar[Csr.Service]
    iris: Csr.Service
    ID_FIELD_NUMBER: _ClassVar[int]
    KEY_TYPE_FIELD_NUMBER: _ClassVar[int]
    KEY_SIZE_BITS_FIELD_NUMBER: _ClassVar[int]
    COMMON_NAME_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_UNIT_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    CITY_FIELD_NUMBER: _ClassVar[int]
    DNS_NAMES_FIELD_NUMBER: _ClassVar[int]
    HOST_IPS_FIELD_NUMBER: _ClassVar[int]
    EMAIL_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    SERVICE_NAME_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTED_PRIVATE_KEY_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_KEY_FIELD_NUMBER: _ClassVar[int]
    CSR_FIELD_NUMBER: _ClassVar[int]
    CREATIONTIMEUSECS_FIELD_NUMBER: _ClassVar[int]
    id: str
    key_type: Csr.Algorithm
    key_size_bits: int
    common_name: str
    organization: str
    organization_unit: str
    country_code: str
    state: str
    city: str
    dns_names: _containers.RepeatedScalarFieldContainer[str]
    host_ips: _containers.RepeatedScalarFieldContainer[str]
    email_address: str
    service_name: Csr.Service
    encrypted_private_key: str
    public_key: str
    csr: str
    creationTimeUsecs: int
    def __init__(self, id: _Optional[str] = ..., key_type: _Optional[_Union[Csr.Algorithm, str]] = ..., key_size_bits: _Optional[int] = ..., common_name: _Optional[str] = ..., organization: _Optional[str] = ..., organization_unit: _Optional[str] = ..., country_code: _Optional[str] = ..., state: _Optional[str] = ..., city: _Optional[str] = ..., dns_names: _Optional[_Iterable[str]] = ..., host_ips: _Optional[_Iterable[str]] = ..., email_address: _Optional[str] = ..., service_name: _Optional[_Union[Csr.Service, str]] = ..., encrypted_private_key: _Optional[str] = ..., public_key: _Optional[str] = ..., csr: _Optional[str] = ..., creationTimeUsecs: _Optional[int] = ...) -> None: ...

class AgentCertificate(_message.Message):
    __slots__ = ("certificate", "encrypted_private_key", "id", "additional_ca_to_trust")
    CERTIFICATE_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTED_PRIVATE_KEY_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_CA_TO_TRUST_FIELD_NUMBER: _ClassVar[int]
    certificate: bytes
    encrypted_private_key: bytes
    id: str
    additional_ca_to_trust: bytes
    def __init__(self, certificate: _Optional[bytes] = ..., encrypted_private_key: _Optional[bytes] = ..., id: _Optional[str] = ..., additional_ca_to_trust: _Optional[bytes] = ...) -> None: ...
