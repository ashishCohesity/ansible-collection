from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CertKeyPair(_message.Message):
    __slots__ = ("pem_private_key", "pem_cert_chain")
    PEM_PRIVATE_KEY_FIELD_NUMBER: _ClassVar[int]
    PEM_CERT_CHAIN_FIELD_NUMBER: _ClassVar[int]
    pem_private_key: bytes
    pem_cert_chain: _containers.RepeatedScalarFieldContainer[bytes]
    def __init__(self, pem_private_key: _Optional[bytes] = ..., pem_cert_chain: _Optional[_Iterable[bytes]] = ...) -> None: ...

class CSR(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UseCase(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kUnknown: _ClassVar[UseCase.Type]
        kMagneto: _ClassVar[UseCase.Type]
        kReplication: _ClassVar[UseCase.Type]
        kConnectorsInBifrost: _ClassVar[UseCase.Type]
        kDdwPortal: _ClassVar[UseCase.Type]
    kUnknown: UseCase.Type
    kMagneto: UseCase.Type
    kReplication: UseCase.Type
    kConnectorsInBifrost: UseCase.Type
    kDdwPortal: UseCase.Type
    def __init__(self) -> None: ...

class CertificateUseCaseMappingProto(_message.Message):
    __slots__ = ("services", "certificate")
    SERVICES_FIELD_NUMBER: _ClassVar[int]
    CERTIFICATE_FIELD_NUMBER: _ClassVar[int]
    services: _containers.RepeatedScalarFieldContainer[UseCase.Type]
    certificate: CertKeyPair
    def __init__(self, services: _Optional[_Iterable[_Union[UseCase.Type, str]]] = ..., certificate: _Optional[_Union[CertKeyPair, _Mapping]] = ...) -> None: ...

class TrustedRootUseCaseMappingProto(_message.Message):
    __slots__ = ("services", "pem_root_cert")
    SERVICES_FIELD_NUMBER: _ClassVar[int]
    PEM_ROOT_CERT_FIELD_NUMBER: _ClassVar[int]
    services: _containers.RepeatedScalarFieldContainer[UseCase.Type]
    pem_root_cert: bytes
    def __init__(self, services: _Optional[_Iterable[_Union[UseCase.Type, str]]] = ..., pem_root_cert: _Optional[bytes] = ...) -> None: ...

class CsrUseCaseMappingProto(_message.Message):
    __slots__ = ("services", "csr")
    SERVICES_FIELD_NUMBER: _ClassVar[int]
    CSR_FIELD_NUMBER: _ClassVar[int]
    services: _containers.RepeatedScalarFieldContainer[UseCase.Type]
    csr: CSR
    def __init__(self, services: _Optional[_Iterable[_Union[UseCase.Type, str]]] = ..., csr: _Optional[_Union[CSR, _Mapping]] = ...) -> None: ...

class TenantPKIProto(_message.Message):
    __slots__ = ("certificates", "csrs", "trust_roots")
    CERTIFICATES_FIELD_NUMBER: _ClassVar[int]
    CSRS_FIELD_NUMBER: _ClassVar[int]
    TRUST_ROOTS_FIELD_NUMBER: _ClassVar[int]
    certificates: _containers.RepeatedCompositeFieldContainer[CertificateUseCaseMappingProto]
    csrs: _containers.RepeatedCompositeFieldContainer[CsrUseCaseMappingProto]
    trust_roots: _containers.RepeatedCompositeFieldContainer[TrustedRootUseCaseMappingProto]
    def __init__(self, certificates: _Optional[_Iterable[_Union[CertificateUseCaseMappingProto, _Mapping]]] = ..., csrs: _Optional[_Iterable[_Union[CsrUseCaseMappingProto, _Mapping]]] = ..., trust_roots: _Optional[_Iterable[_Union[TrustedRootUseCaseMappingProto, _Mapping]]] = ...) -> None: ...

class RemoteClusterTrustRootsProto(_message.Message):
    __slots__ = ("pem_root_certs",)
    PEM_ROOT_CERTS_FIELD_NUMBER: _ClassVar[int]
    pem_root_certs: _containers.RepeatedScalarFieldContainer[bytes]
    def __init__(self, pem_root_certs: _Optional[_Iterable[bytes]] = ...) -> None: ...

class ClusterCertificatesProto(_message.Message):
    __slots__ = ("gandalf_key", "user_uploaded_certficates_gandalf_key", "cluster_certificates", "cluster_trust_roots", "cluster_csrs", "tenant_pki", "remote_cluster_trust_roots", "newer_cohesity_ca_certificates")
    class TenantPkiEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: TenantPKIProto
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[TenantPKIProto, _Mapping]] = ...) -> None: ...
    class RemoteClusterTrustRootsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: RemoteClusterTrustRootsProto
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[RemoteClusterTrustRootsProto, _Mapping]] = ...) -> None: ...
    GANDALF_KEY_FIELD_NUMBER: _ClassVar[int]
    USER_UPLOADED_CERTFICATES_GANDALF_KEY_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_CERTIFICATES_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_TRUST_ROOTS_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_CSRS_FIELD_NUMBER: _ClassVar[int]
    TENANT_PKI_FIELD_NUMBER: _ClassVar[int]
    REMOTE_CLUSTER_TRUST_ROOTS_FIELD_NUMBER: _ClassVar[int]
    NEWER_COHESITY_CA_CERTIFICATES_FIELD_NUMBER: _ClassVar[int]
    gandalf_key: str
    user_uploaded_certficates_gandalf_key: str
    cluster_certificates: _containers.RepeatedCompositeFieldContainer[CertificateUseCaseMappingProto]
    cluster_trust_roots: _containers.RepeatedCompositeFieldContainer[TrustedRootUseCaseMappingProto]
    cluster_csrs: _containers.RepeatedCompositeFieldContainer[CsrUseCaseMappingProto]
    tenant_pki: _containers.MessageMap[str, TenantPKIProto]
    remote_cluster_trust_roots: _containers.MessageMap[int, RemoteClusterTrustRootsProto]
    newer_cohesity_ca_certificates: _containers.RepeatedCompositeFieldContainer[ClusterCertificatesProto]
    def __init__(self, gandalf_key: _Optional[str] = ..., user_uploaded_certficates_gandalf_key: _Optional[str] = ..., cluster_certificates: _Optional[_Iterable[_Union[CertificateUseCaseMappingProto, _Mapping]]] = ..., cluster_trust_roots: _Optional[_Iterable[_Union[TrustedRootUseCaseMappingProto, _Mapping]]] = ..., cluster_csrs: _Optional[_Iterable[_Union[CsrUseCaseMappingProto, _Mapping]]] = ..., tenant_pki: _Optional[_Mapping[str, TenantPKIProto]] = ..., remote_cluster_trust_roots: _Optional[_Mapping[int, RemoteClusterTrustRootsProto]] = ..., newer_cohesity_ca_certificates: _Optional[_Iterable[_Union[ClusterCertificatesProto, _Mapping]]] = ...) -> None: ...
