from nexus.go.pki.ca.grpc.api import error_pb2 as _error_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Algorithm(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UNDEFINED: _ClassVar[Algorithm]
    RSA_3072: _ClassVar[Algorithm]
    RSA_4096: _ClassVar[Algorithm]
    RSA_7680: _ClassVar[Algorithm]
    RSA_15360: _ClassVar[Algorithm]
    ECDSA_256: _ClassVar[Algorithm]
    ECDSA_384: _ClassVar[Algorithm]
    ECDSA_512: _ClassVar[Algorithm]

class PeerType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kMagnetoAgent: _ClassVar[PeerType]
    kMagnetoPlugin: _ClassVar[PeerType]
    kRemoteCluster: _ClassVar[PeerType]
UNDEFINED: Algorithm
RSA_3072: Algorithm
RSA_4096: Algorithm
RSA_7680: Algorithm
RSA_15360: Algorithm
ECDSA_256: Algorithm
ECDSA_384: Algorithm
ECDSA_512: Algorithm
kMagnetoAgent: PeerType
kMagnetoPlugin: PeerType
kRemoteCluster: PeerType

class SubjectInfo(_message.Message):
    __slots__ = ("country", "state", "locality", "organization_name", "organization_unit_name", "email", "serial_number")
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    LOCALITY_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_NAME_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_UNIT_NAME_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    SERIAL_NUMBER_FIELD_NUMBER: _ClassVar[int]
    country: str
    state: str
    locality: str
    organization_name: str
    organization_unit_name: str
    email: str
    serial_number: str
    def __init__(self, country: _Optional[str] = ..., state: _Optional[str] = ..., locality: _Optional[str] = ..., organization_name: _Optional[str] = ..., organization_unit_name: _Optional[str] = ..., email: _Optional[str] = ..., serial_number: _Optional[str] = ...) -> None: ...

class KeyRequest(_message.Message):
    __slots__ = ("algo",)
    ALGO_FIELD_NUMBER: _ClassVar[int]
    algo: Algorithm
    def __init__(self, algo: _Optional[_Union[Algorithm, str]] = ...) -> None: ...

class NewCertArg(_message.Message):
    __slots__ = ("cn", "names", "hosts", "cluster_name", "cluster_id", "additional_fields", "key_params", "expiry", "delegation_enabled", "profile", "tenant_id")
    class AdditionalFieldsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    CN_FIELD_NUMBER: _ClassVar[int]
    NAMES_FIELD_NUMBER: _ClassVar[int]
    HOSTS_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_NAME_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_FIELDS_FIELD_NUMBER: _ClassVar[int]
    KEY_PARAMS_FIELD_NUMBER: _ClassVar[int]
    EXPIRY_FIELD_NUMBER: _ClassVar[int]
    DELEGATION_ENABLED_FIELD_NUMBER: _ClassVar[int]
    PROFILE_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    cn: str
    names: _containers.RepeatedCompositeFieldContainer[SubjectInfo]
    hosts: _containers.RepeatedScalarFieldContainer[str]
    cluster_name: str
    cluster_id: str
    additional_fields: _containers.ScalarMap[str, str]
    key_params: KeyRequest
    expiry: str
    delegation_enabled: bool
    profile: str
    tenant_id: str
    def __init__(self, cn: _Optional[str] = ..., names: _Optional[_Iterable[_Union[SubjectInfo, _Mapping]]] = ..., hosts: _Optional[_Iterable[str]] = ..., cluster_name: _Optional[str] = ..., cluster_id: _Optional[str] = ..., additional_fields: _Optional[_Mapping[str, str]] = ..., key_params: _Optional[_Union[KeyRequest, _Mapping]] = ..., expiry: _Optional[str] = ..., delegation_enabled: bool = ..., profile: _Optional[str] = ..., tenant_id: _Optional[str] = ...) -> None: ...

class SignCsrArg(_message.Message):
    __slots__ = ("csr_req_pem", "tenant_id", "expiry", "san_fields", "additional_fields")
    class AdditionalFieldsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    CSR_REQ_PEM_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    EXPIRY_FIELD_NUMBER: _ClassVar[int]
    SAN_FIELDS_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_FIELDS_FIELD_NUMBER: _ClassVar[int]
    csr_req_pem: str
    tenant_id: str
    expiry: str
    san_fields: _containers.RepeatedScalarFieldContainer[str]
    additional_fields: _containers.ScalarMap[str, str]
    def __init__(self, csr_req_pem: _Optional[str] = ..., tenant_id: _Optional[str] = ..., expiry: _Optional[str] = ..., san_fields: _Optional[_Iterable[str]] = ..., additional_fields: _Optional[_Mapping[str, str]] = ...) -> None: ...

class SignCsrResult(_message.Message):
    __slots__ = ("error", "messages", "certificate_pem", "ca_cert_chain")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    CERTIFICATE_PEM_FIELD_NUMBER: _ClassVar[int]
    CA_CERT_CHAIN_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    messages: _containers.RepeatedScalarFieldContainer[str]
    certificate_pem: str
    ca_cert_chain: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., messages: _Optional[_Iterable[str]] = ..., certificate_pem: _Optional[str] = ..., ca_cert_chain: _Optional[_Iterable[str]] = ...) -> None: ...

class GetCsrArg(_message.Message):
    __slots__ = ("cert_arg",)
    CERT_ARG_FIELD_NUMBER: _ClassVar[int]
    cert_arg: NewCertArg
    def __init__(self, cert_arg: _Optional[_Union[NewCertArg, _Mapping]] = ...) -> None: ...

class GetCsrResult(_message.Message):
    __slots__ = ("error", "messages", "private_key", "csr_pem")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_KEY_FIELD_NUMBER: _ClassVar[int]
    CSR_PEM_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    messages: _containers.RepeatedScalarFieldContainer[str]
    private_key: str
    csr_pem: str
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., messages: _Optional[_Iterable[str]] = ..., private_key: _Optional[str] = ..., csr_pem: _Optional[str] = ...) -> None: ...

class NewCertResult(_message.Message):
    __slots__ = ("error", "messages", "private_key", "certificate", "ca_cert_chain", "csr")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_KEY_FIELD_NUMBER: _ClassVar[int]
    CERTIFICATE_FIELD_NUMBER: _ClassVar[int]
    CA_CERT_CHAIN_FIELD_NUMBER: _ClassVar[int]
    CSR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    messages: _containers.RepeatedScalarFieldContainer[str]
    private_key: str
    certificate: str
    ca_cert_chain: _containers.RepeatedScalarFieldContainer[str]
    csr: str
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., messages: _Optional[_Iterable[str]] = ..., private_key: _Optional[str] = ..., certificate: _Optional[str] = ..., ca_cert_chain: _Optional[_Iterable[str]] = ..., csr: _Optional[str] = ...) -> None: ...

class DiscoveredCertProperties(_message.Message):
    __slots__ = ("peerType", "additional_metadata")
    class AdditionalMetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    PEERTYPE_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_METADATA_FIELD_NUMBER: _ClassVar[int]
    peerType: PeerType
    additional_metadata: _containers.ScalarMap[str, str]
    def __init__(self, peerType: _Optional[_Union[PeerType, str]] = ..., additional_metadata: _Optional[_Mapping[str, str]] = ...) -> None: ...

class RegisterDiscoveredCertificateArg(_message.Message):
    __slots__ = ("certificate_pem", "cert_properties")
    CERTIFICATE_PEM_FIELD_NUMBER: _ClassVar[int]
    CERT_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    certificate_pem: str
    cert_properties: DiscoveredCertProperties
    def __init__(self, certificate_pem: _Optional[str] = ..., cert_properties: _Optional[_Union[DiscoveredCertProperties, _Mapping]] = ...) -> None: ...

class RegisterDiscoveredCertificateResult(_message.Message):
    __slots__ = ("error", "messages")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    messages: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., messages: _Optional[_Iterable[str]] = ...) -> None: ...
