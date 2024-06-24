from helios.hcm.api.v1 import asset_pb2 as _asset_pb2
from helios.hcm.api.v1 import error_pb2 as _error_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TokenType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kTokenTypeNotSet: _ClassVar[TokenType]
    kTokenTypeUUID: _ClassVar[TokenType]
    kTokenTypeJWT: _ClassVar[TokenType]
kTokenTypeNotSet: TokenType
kTokenTypeUUID: TokenType
kTokenTypeJWT: TokenType

class CertEmbedInfo(_message.Message):
    __slots__ = ("common_name", "organization")
    COMMON_NAME_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_FIELD_NUMBER: _ClassVar[int]
    common_name: str
    organization: str
    def __init__(self, common_name: _Optional[str] = ..., organization: _Optional[str] = ...) -> None: ...

class Certificate(_message.Message):
    __slots__ = ("certificate", "private_key", "passphrase", "is_private", "ca_chain", "cert_arn", "ca_arn")
    CERTIFICATE_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_KEY_FIELD_NUMBER: _ClassVar[int]
    PASSPHRASE_FIELD_NUMBER: _ClassVar[int]
    IS_PRIVATE_FIELD_NUMBER: _ClassVar[int]
    CA_CHAIN_FIELD_NUMBER: _ClassVar[int]
    CERT_ARN_FIELD_NUMBER: _ClassVar[int]
    CA_ARN_FIELD_NUMBER: _ClassVar[int]
    certificate: bytes
    private_key: bytes
    passphrase: bytes
    is_private: bool
    ca_chain: bytes
    cert_arn: str
    ca_arn: str
    def __init__(self, certificate: _Optional[bytes] = ..., private_key: _Optional[bytes] = ..., passphrase: _Optional[bytes] = ..., is_private: bool = ..., ca_chain: _Optional[bytes] = ..., cert_arn: _Optional[str] = ..., ca_arn: _Optional[str] = ...) -> None: ...

class AddCAChainReq(_message.Message):
    __slots__ = ("ca_type", "ca_chain")
    CA_TYPE_FIELD_NUMBER: _ClassVar[int]
    CA_CHAIN_FIELD_NUMBER: _ClassVar[int]
    ca_type: _asset_pb2.CAChainType
    ca_chain: str
    def __init__(self, ca_type: _Optional[_Union[_asset_pb2.CAChainType, str]] = ..., ca_chain: _Optional[str] = ...) -> None: ...

class AddCAChainResp(_message.Message):
    __slots__ = ("error_proto",)
    ERROR_PROTO_FIELD_NUMBER: _ClassVar[int]
    error_proto: _error_pb2.HCMApiError
    def __init__(self, error_proto: _Optional[_Union[_error_pb2.HCMApiError, _Mapping]] = ...) -> None: ...

class CreateDMaaSClusterCertsReq(_message.Message):
    __slots__ = ("cluster_id", "cluster_incarnation_id", "sf_account_id", "valid_for_days", "subscribe_for_renewal", "cert_embed_info", "is_renewal_request")
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    SF_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    VALID_FOR_DAYS_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIBE_FOR_RENEWAL_FIELD_NUMBER: _ClassVar[int]
    CERT_EMBED_INFO_FIELD_NUMBER: _ClassVar[int]
    IS_RENEWAL_REQUEST_FIELD_NUMBER: _ClassVar[int]
    cluster_id: int
    cluster_incarnation_id: int
    sf_account_id: str
    valid_for_days: int
    subscribe_for_renewal: bool
    cert_embed_info: CertEmbedInfo
    is_renewal_request: bool
    def __init__(self, cluster_id: _Optional[int] = ..., cluster_incarnation_id: _Optional[int] = ..., sf_account_id: _Optional[str] = ..., valid_for_days: _Optional[int] = ..., subscribe_for_renewal: bool = ..., cert_embed_info: _Optional[_Union[CertEmbedInfo, _Mapping]] = ..., is_renewal_request: bool = ...) -> None: ...

class CreateDMaaSClusterCertsResp(_message.Message):
    __slots__ = ("error_proto", "dmaas_cluster_certificate", "helios_certificate", "topic_name_for_notifications")
    ERROR_PROTO_FIELD_NUMBER: _ClassVar[int]
    DMAAS_CLUSTER_CERTIFICATE_FIELD_NUMBER: _ClassVar[int]
    HELIOS_CERTIFICATE_FIELD_NUMBER: _ClassVar[int]
    TOPIC_NAME_FOR_NOTIFICATIONS_FIELD_NUMBER: _ClassVar[int]
    error_proto: _error_pb2.HCMApiError
    dmaas_cluster_certificate: Certificate
    helios_certificate: Certificate
    topic_name_for_notifications: str
    def __init__(self, error_proto: _Optional[_Union[_error_pb2.HCMApiError, _Mapping]] = ..., dmaas_cluster_certificate: _Optional[_Union[Certificate, _Mapping]] = ..., helios_certificate: _Optional[_Union[Certificate, _Mapping]] = ..., topic_name_for_notifications: _Optional[str] = ...) -> None: ...

class CreateOnPremClusterCertReq(_message.Message):
    __slots__ = ("cluster_id", "cluster_incarnation_id", "sf_account_id", "valid_for_days", "subscribe_for_renewal", "asset_type")
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    SF_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    VALID_FOR_DAYS_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIBE_FOR_RENEWAL_FIELD_NUMBER: _ClassVar[int]
    ASSET_TYPE_FIELD_NUMBER: _ClassVar[int]
    cluster_id: int
    cluster_incarnation_id: int
    sf_account_id: str
    valid_for_days: int
    subscribe_for_renewal: bool
    asset_type: _asset_pb2.AssetType
    def __init__(self, cluster_id: _Optional[int] = ..., cluster_incarnation_id: _Optional[int] = ..., sf_account_id: _Optional[str] = ..., valid_for_days: _Optional[int] = ..., subscribe_for_renewal: bool = ..., asset_type: _Optional[_Union[_asset_pb2.AssetType, str]] = ...) -> None: ...

class CreateOnPremClusterCertResp(_message.Message):
    __slots__ = ("error_proto", "onprem_cluster_certificate", "helios_certificate", "tenant_ca_chain", "topic_name_for_notifications")
    ERROR_PROTO_FIELD_NUMBER: _ClassVar[int]
    ONPREM_CLUSTER_CERTIFICATE_FIELD_NUMBER: _ClassVar[int]
    HELIOS_CERTIFICATE_FIELD_NUMBER: _ClassVar[int]
    TENANT_CA_CHAIN_FIELD_NUMBER: _ClassVar[int]
    TOPIC_NAME_FOR_NOTIFICATIONS_FIELD_NUMBER: _ClassVar[int]
    error_proto: _error_pb2.HCMApiError
    onprem_cluster_certificate: Certificate
    helios_certificate: Certificate
    tenant_ca_chain: Certificate
    topic_name_for_notifications: str
    def __init__(self, error_proto: _Optional[_Union[_error_pb2.HCMApiError, _Mapping]] = ..., onprem_cluster_certificate: _Optional[_Union[Certificate, _Mapping]] = ..., helios_certificate: _Optional[_Union[Certificate, _Mapping]] = ..., tenant_ca_chain: _Optional[_Union[Certificate, _Mapping]] = ..., topic_name_for_notifications: _Optional[str] = ...) -> None: ...

class CreateCohesionApplianceCertReq(_message.Message):
    __slots__ = ("cluster_id", "cluster_incarnation_id", "sf_account_id", "appliance_id", "valid_for_days", "is_renewal_request", "subscribe_for_renewal")
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    SF_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    APPLIANCE_ID_FIELD_NUMBER: _ClassVar[int]
    VALID_FOR_DAYS_FIELD_NUMBER: _ClassVar[int]
    IS_RENEWAL_REQUEST_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIBE_FOR_RENEWAL_FIELD_NUMBER: _ClassVar[int]
    cluster_id: int
    cluster_incarnation_id: int
    sf_account_id: str
    appliance_id: str
    valid_for_days: int
    is_renewal_request: bool
    subscribe_for_renewal: bool
    def __init__(self, cluster_id: _Optional[int] = ..., cluster_incarnation_id: _Optional[int] = ..., sf_account_id: _Optional[str] = ..., appliance_id: _Optional[str] = ..., valid_for_days: _Optional[int] = ..., is_renewal_request: bool = ..., subscribe_for_renewal: bool = ...) -> None: ...

class CreateCohesionApplianceCertResp(_message.Message):
    __slots__ = ("error_proto", "cohesion_certificate", "helios_certificate")
    ERROR_PROTO_FIELD_NUMBER: _ClassVar[int]
    COHESION_CERTIFICATE_FIELD_NUMBER: _ClassVar[int]
    HELIOS_CERTIFICATE_FIELD_NUMBER: _ClassVar[int]
    error_proto: _error_pb2.HCMApiError
    cohesion_certificate: Certificate
    helios_certificate: Certificate
    def __init__(self, error_proto: _Optional[_Union[_error_pb2.HCMApiError, _Mapping]] = ..., cohesion_certificate: _Optional[_Union[Certificate, _Mapping]] = ..., helios_certificate: _Optional[_Union[Certificate, _Mapping]] = ...) -> None: ...

class CreateTenantCertReq(_message.Message):
    __slots__ = ("tenant_fqdn", "global_tenant_id", "valid_for_days", "subscribe_for_renewal", "is_renewal_request")
    TENANT_FQDN_FIELD_NUMBER: _ClassVar[int]
    GLOBAL_TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    VALID_FOR_DAYS_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIBE_FOR_RENEWAL_FIELD_NUMBER: _ClassVar[int]
    IS_RENEWAL_REQUEST_FIELD_NUMBER: _ClassVar[int]
    tenant_fqdn: str
    global_tenant_id: str
    valid_for_days: int
    subscribe_for_renewal: bool
    is_renewal_request: bool
    def __init__(self, tenant_fqdn: _Optional[str] = ..., global_tenant_id: _Optional[str] = ..., valid_for_days: _Optional[int] = ..., subscribe_for_renewal: bool = ..., is_renewal_request: bool = ...) -> None: ...

class CreateTenantCertResp(_message.Message):
    __slots__ = ("error_proto", "tenant_certificate", "client_ca_chains", "topic_name_for_notifications")
    ERROR_PROTO_FIELD_NUMBER: _ClassVar[int]
    TENANT_CERTIFICATE_FIELD_NUMBER: _ClassVar[int]
    CLIENT_CA_CHAINS_FIELD_NUMBER: _ClassVar[int]
    TOPIC_NAME_FOR_NOTIFICATIONS_FIELD_NUMBER: _ClassVar[int]
    error_proto: _error_pb2.HCMApiError
    tenant_certificate: Certificate
    client_ca_chains: _containers.RepeatedCompositeFieldContainer[Certificate]
    topic_name_for_notifications: str
    def __init__(self, error_proto: _Optional[_Union[_error_pb2.HCMApiError, _Mapping]] = ..., tenant_certificate: _Optional[_Union[Certificate, _Mapping]] = ..., client_ca_chains: _Optional[_Iterable[_Union[Certificate, _Mapping]]] = ..., topic_name_for_notifications: _Optional[str] = ...) -> None: ...

class CreateRigelCertReq(_message.Message):
    __slots__ = ("rigel_guid", "global_tenant_id", "valid_for_days", "asset_type", "subscribe_for_renewal", "cert_embed_info")
    RIGEL_GUID_FIELD_NUMBER: _ClassVar[int]
    GLOBAL_TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    VALID_FOR_DAYS_FIELD_NUMBER: _ClassVar[int]
    ASSET_TYPE_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIBE_FOR_RENEWAL_FIELD_NUMBER: _ClassVar[int]
    CERT_EMBED_INFO_FIELD_NUMBER: _ClassVar[int]
    rigel_guid: int
    global_tenant_id: str
    valid_for_days: int
    asset_type: _asset_pb2.AssetType
    subscribe_for_renewal: bool
    cert_embed_info: CertEmbedInfo
    def __init__(self, rigel_guid: _Optional[int] = ..., global_tenant_id: _Optional[str] = ..., valid_for_days: _Optional[int] = ..., asset_type: _Optional[_Union[_asset_pb2.AssetType, str]] = ..., subscribe_for_renewal: bool = ..., cert_embed_info: _Optional[_Union[CertEmbedInfo, _Mapping]] = ...) -> None: ...

class CreateRigelCertResp(_message.Message):
    __slots__ = ("error_proto", "rigel_certificate", "helios_certificate", "certificate_version", "tenant_ca_chains", "topic_name_for_notifications")
    ERROR_PROTO_FIELD_NUMBER: _ClassVar[int]
    RIGEL_CERTIFICATE_FIELD_NUMBER: _ClassVar[int]
    HELIOS_CERTIFICATE_FIELD_NUMBER: _ClassVar[int]
    CERTIFICATE_VERSION_FIELD_NUMBER: _ClassVar[int]
    TENANT_CA_CHAINS_FIELD_NUMBER: _ClassVar[int]
    TOPIC_NAME_FOR_NOTIFICATIONS_FIELD_NUMBER: _ClassVar[int]
    error_proto: _error_pb2.HCMApiError
    rigel_certificate: Certificate
    helios_certificate: Certificate
    certificate_version: int
    tenant_ca_chains: _containers.RepeatedCompositeFieldContainer[Certificate]
    topic_name_for_notifications: str
    def __init__(self, error_proto: _Optional[_Union[_error_pb2.HCMApiError, _Mapping]] = ..., rigel_certificate: _Optional[_Union[Certificate, _Mapping]] = ..., helios_certificate: _Optional[_Union[Certificate, _Mapping]] = ..., certificate_version: _Optional[int] = ..., tenant_ca_chains: _Optional[_Iterable[_Union[Certificate, _Mapping]]] = ..., topic_name_for_notifications: _Optional[str] = ...) -> None: ...

class RevokeCertReq(_message.Message):
    __slots__ = ("asset_type", "cluster_id", "cluster_incarnation_id", "sf_account_id", "rigel_guid", "tenant_fqdn", "global_tenant_id", "revoke_all_except")
    ASSET_TYPE_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    SF_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    RIGEL_GUID_FIELD_NUMBER: _ClassVar[int]
    TENANT_FQDN_FIELD_NUMBER: _ClassVar[int]
    GLOBAL_TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    REVOKE_ALL_EXCEPT_FIELD_NUMBER: _ClassVar[int]
    asset_type: _asset_pb2.AssetType
    cluster_id: int
    cluster_incarnation_id: int
    sf_account_id: str
    rigel_guid: int
    tenant_fqdn: str
    global_tenant_id: str
    revoke_all_except: Certificate
    def __init__(self, asset_type: _Optional[_Union[_asset_pb2.AssetType, str]] = ..., cluster_id: _Optional[int] = ..., cluster_incarnation_id: _Optional[int] = ..., sf_account_id: _Optional[str] = ..., rigel_guid: _Optional[int] = ..., tenant_fqdn: _Optional[str] = ..., global_tenant_id: _Optional[str] = ..., revoke_all_except: _Optional[_Union[Certificate, _Mapping]] = ...) -> None: ...

class RevokeCertResp(_message.Message):
    __slots__ = ("error_proto", "is_revoked")
    ERROR_PROTO_FIELD_NUMBER: _ClassVar[int]
    IS_REVOKED_FIELD_NUMBER: _ClassVar[int]
    error_proto: _error_pb2.HCMApiError
    is_revoked: bool
    def __init__(self, error_proto: _Optional[_Union[_error_pb2.HCMApiError, _Mapping]] = ..., is_revoked: bool = ...) -> None: ...

class CertStatusReq(_message.Message):
    __slots__ = ("asset_type", "cluster_id", "cluster_incarnation_id", "rigel_guid", "tenant_fqdn", "fetch_certificate", "sf_account_id", "global_tenant_id", "cohesion_appliance_id")
    ASSET_TYPE_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    RIGEL_GUID_FIELD_NUMBER: _ClassVar[int]
    TENANT_FQDN_FIELD_NUMBER: _ClassVar[int]
    FETCH_CERTIFICATE_FIELD_NUMBER: _ClassVar[int]
    SF_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    GLOBAL_TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    COHESION_APPLIANCE_ID_FIELD_NUMBER: _ClassVar[int]
    asset_type: _asset_pb2.AssetType
    cluster_id: int
    cluster_incarnation_id: int
    rigel_guid: int
    tenant_fqdn: str
    fetch_certificate: bool
    sf_account_id: str
    global_tenant_id: str
    cohesion_appliance_id: str
    def __init__(self, asset_type: _Optional[_Union[_asset_pb2.AssetType, str]] = ..., cluster_id: _Optional[int] = ..., cluster_incarnation_id: _Optional[int] = ..., rigel_guid: _Optional[int] = ..., tenant_fqdn: _Optional[str] = ..., fetch_certificate: bool = ..., sf_account_id: _Optional[str] = ..., global_tenant_id: _Optional[str] = ..., cohesion_appliance_id: _Optional[str] = ...) -> None: ...

class CertStatusResp(_message.Message):
    __slots__ = ("error_proto", "is_revoked", "certificate", "version")
    ERROR_PROTO_FIELD_NUMBER: _ClassVar[int]
    IS_REVOKED_FIELD_NUMBER: _ClassVar[int]
    CERTIFICATE_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    error_proto: _error_pb2.HCMApiError
    is_revoked: bool
    certificate: Certificate
    version: int
    def __init__(self, error_proto: _Optional[_Union[_error_pb2.HCMApiError, _Mapping]] = ..., is_revoked: bool = ..., certificate: _Optional[_Union[Certificate, _Mapping]] = ..., version: _Optional[int] = ...) -> None: ...

class FetchCAChainsReq(_message.Message):
    __slots__ = ("asset_type", "cluster_id", "cluster_incarnation_id", "rigel_guid", "tenant_fqdn", "fetch_all_active")
    ASSET_TYPE_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    RIGEL_GUID_FIELD_NUMBER: _ClassVar[int]
    TENANT_FQDN_FIELD_NUMBER: _ClassVar[int]
    FETCH_ALL_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    asset_type: _asset_pb2.AssetType
    cluster_id: int
    cluster_incarnation_id: int
    rigel_guid: int
    tenant_fqdn: str
    fetch_all_active: bool
    def __init__(self, asset_type: _Optional[_Union[_asset_pb2.AssetType, str]] = ..., cluster_id: _Optional[int] = ..., cluster_incarnation_id: _Optional[int] = ..., rigel_guid: _Optional[int] = ..., tenant_fqdn: _Optional[str] = ..., fetch_all_active: bool = ...) -> None: ...

class FetchCAChainsResp(_message.Message):
    __slots__ = ("error_proto", "certificates")
    ERROR_PROTO_FIELD_NUMBER: _ClassVar[int]
    CERTIFICATES_FIELD_NUMBER: _ClassVar[int]
    error_proto: _error_pb2.HCMApiError
    certificates: _containers.RepeatedCompositeFieldContainer[Certificate]
    def __init__(self, error_proto: _Optional[_Union[_error_pb2.HCMApiError, _Mapping]] = ..., certificates: _Optional[_Iterable[_Union[Certificate, _Mapping]]] = ...) -> None: ...

class CreateClaimTokenReq(_message.Message):
    __slots__ = ("asset_type", "rigel_group_id", "validity_in_hours", "force_create", "account_id")
    ASSET_TYPE_FIELD_NUMBER: _ClassVar[int]
    RIGEL_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    VALIDITY_IN_HOURS_FIELD_NUMBER: _ClassVar[int]
    FORCE_CREATE_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    asset_type: _asset_pb2.AssetType
    rigel_group_id: int
    validity_in_hours: int
    force_create: bool
    account_id: str
    def __init__(self, asset_type: _Optional[_Union[_asset_pb2.AssetType, str]] = ..., rigel_group_id: _Optional[int] = ..., validity_in_hours: _Optional[int] = ..., force_create: bool = ..., account_id: _Optional[str] = ...) -> None: ...

class CreateClaimTokenResp(_message.Message):
    __slots__ = ("error_proto", "token", "issued_timestamp_secs", "expiry_timestamp_secs", "type", "name", "uuid")
    ERROR_PROTO_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    ISSUED_TIMESTAMP_SECS_FIELD_NUMBER: _ClassVar[int]
    EXPIRY_TIMESTAMP_SECS_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    error_proto: _error_pb2.HCMApiError
    token: str
    issued_timestamp_secs: int
    expiry_timestamp_secs: int
    type: TokenType
    name: str
    uuid: str
    def __init__(self, error_proto: _Optional[_Union[_error_pb2.HCMApiError, _Mapping]] = ..., token: _Optional[str] = ..., issued_timestamp_secs: _Optional[int] = ..., expiry_timestamp_secs: _Optional[int] = ..., type: _Optional[_Union[TokenType, str]] = ..., name: _Optional[str] = ..., uuid: _Optional[str] = ...) -> None: ...

class ValidateTokenReq(_message.Message):
    __slots__ = ("token", "type")
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    token: str
    type: TokenType
    def __init__(self, token: _Optional[str] = ..., type: _Optional[_Union[TokenType, str]] = ...) -> None: ...

class ValidateTokenResp(_message.Message):
    __slots__ = ("error_proto", "is_valid", "asset_type", "uuid", "rigel_group_id", "account_id")
    ERROR_PROTO_FIELD_NUMBER: _ClassVar[int]
    IS_VALID_FIELD_NUMBER: _ClassVar[int]
    ASSET_TYPE_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    RIGEL_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    error_proto: _error_pb2.HCMApiError
    is_valid: bool
    asset_type: _asset_pb2.AssetType
    uuid: str
    rigel_group_id: int
    account_id: str
    def __init__(self, error_proto: _Optional[_Union[_error_pb2.HCMApiError, _Mapping]] = ..., is_valid: bool = ..., asset_type: _Optional[_Union[_asset_pb2.AssetType, str]] = ..., uuid: _Optional[str] = ..., rigel_group_id: _Optional[int] = ..., account_id: _Optional[str] = ...) -> None: ...

class FetchRigelTokenReq(_message.Message):
    __slots__ = ("asset_type", "rigel_group_id")
    ASSET_TYPE_FIELD_NUMBER: _ClassVar[int]
    RIGEL_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    asset_type: _asset_pb2.AssetType
    rigel_group_id: int
    def __init__(self, asset_type: _Optional[_Union[_asset_pb2.AssetType, str]] = ..., rigel_group_id: _Optional[int] = ...) -> None: ...

class FetchRigelTokenResp(_message.Message):
    __slots__ = ("error_proto", "token", "expiry_timestamp_secs")
    ERROR_PROTO_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    EXPIRY_TIMESTAMP_SECS_FIELD_NUMBER: _ClassVar[int]
    error_proto: _error_pb2.HCMApiError
    token: str
    expiry_timestamp_secs: int
    def __init__(self, error_proto: _Optional[_Union[_error_pb2.HCMApiError, _Mapping]] = ..., token: _Optional[str] = ..., expiry_timestamp_secs: _Optional[int] = ...) -> None: ...

class CreateAgentCertReq(_message.Message):
    __slots__ = ("global_tenant_id", "valid_for_days", "additional_fields")
    class AdditionalFieldsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    GLOBAL_TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    VALID_FOR_DAYS_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_FIELDS_FIELD_NUMBER: _ClassVar[int]
    global_tenant_id: str
    valid_for_days: int
    additional_fields: _containers.ScalarMap[str, str]
    def __init__(self, global_tenant_id: _Optional[str] = ..., valid_for_days: _Optional[int] = ..., additional_fields: _Optional[_Mapping[str, str]] = ...) -> None: ...

class CreateAgentCertResp(_message.Message):
    __slots__ = ("error_proto", "agent_certificate", "tenant_ca_chains")
    ERROR_PROTO_FIELD_NUMBER: _ClassVar[int]
    AGENT_CERTIFICATE_FIELD_NUMBER: _ClassVar[int]
    TENANT_CA_CHAINS_FIELD_NUMBER: _ClassVar[int]
    error_proto: _error_pb2.HCMApiError
    agent_certificate: Certificate
    tenant_ca_chains: _containers.RepeatedCompositeFieldContainer[Certificate]
    def __init__(self, error_proto: _Optional[_Union[_error_pb2.HCMApiError, _Mapping]] = ..., agent_certificate: _Optional[_Union[Certificate, _Mapping]] = ..., tenant_ca_chains: _Optional[_Iterable[_Union[Certificate, _Mapping]]] = ...) -> None: ...

class ListTokensReq(_message.Message):
    __slots__ = ("sf_account_id", "type", "asset_types")
    SF_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ASSET_TYPES_FIELD_NUMBER: _ClassVar[int]
    sf_account_id: str
    type: TokenType
    asset_types: _containers.RepeatedScalarFieldContainer[_asset_pb2.AssetType]
    def __init__(self, sf_account_id: _Optional[str] = ..., type: _Optional[_Union[TokenType, str]] = ..., asset_types: _Optional[_Iterable[_Union[_asset_pb2.AssetType, str]]] = ...) -> None: ...

class ClaimTokenMetadata(_message.Message):
    __slots__ = ("token_name", "uuid")
    TOKEN_NAME_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    token_name: str
    uuid: str
    def __init__(self, token_name: _Optional[str] = ..., uuid: _Optional[str] = ...) -> None: ...

class ListTokensResp(_message.Message):
    __slots__ = ("error_proto", "tokens")
    ERROR_PROTO_FIELD_NUMBER: _ClassVar[int]
    TOKENS_FIELD_NUMBER: _ClassVar[int]
    error_proto: _error_pb2.HCMApiError
    tokens: _containers.RepeatedCompositeFieldContainer[ClaimTokenMetadata]
    def __init__(self, error_proto: _Optional[_Union[_error_pb2.HCMApiError, _Mapping]] = ..., tokens: _Optional[_Iterable[_Union[ClaimTokenMetadata, _Mapping]]] = ...) -> None: ...

class RevokeTokenReq(_message.Message):
    __slots__ = ("sf_account_id", "uuid", "type")
    SF_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    sf_account_id: str
    uuid: str
    type: TokenType
    def __init__(self, sf_account_id: _Optional[str] = ..., uuid: _Optional[str] = ..., type: _Optional[_Union[TokenType, str]] = ...) -> None: ...

class RevokeTokenResp(_message.Message):
    __slots__ = ("error_proto",)
    ERROR_PROTO_FIELD_NUMBER: _ClassVar[int]
    error_proto: _error_pb2.HCMApiError
    def __init__(self, error_proto: _Optional[_Union[_error_pb2.HCMApiError, _Mapping]] = ...) -> None: ...
