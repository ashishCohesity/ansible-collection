from nexus.eagle_agent.base import pipe_data_pb2 as _pipe_data_pb2
from magneto.api import enum_wrappers_pb2 as _enum_wrappers_pb2
from helios.base import fortknox_pb2 as _fortknox_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UnregisterType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    KCluster: _ClassVar[UnregisterType]

class Capability(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kList: _ClassVar[Capability]
    kRead: _ClassVar[Capability]
    kWrite: _ClassVar[Capability]
    kDelete: _ClassVar[Capability]

class CredCapability(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kNone: _ClassVar[CredCapability]
    kReadPriv: _ClassVar[CredCapability]
    kWritePriv: _ClassVar[CredCapability]
    kListPriv: _ClassVar[CredCapability]
KCluster: UnregisterType
kList: Capability
kRead: Capability
kWrite: Capability
kDelete: Capability
kNone: CredCapability
kReadPriv: CredCapability
kWritePriv: CredCapability
kListPriv: CredCapability

class SendMagnetoStateArg(_message.Message):
    __slots__ = ("cluster_id", "magneto_state_object_batch", "is_last_batch", "is_compressed", "latest_magneto_change_info", "is_chunked", "chunk_envelope")
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    MAGNETO_STATE_OBJECT_BATCH_FIELD_NUMBER: _ClassVar[int]
    IS_LAST_BATCH_FIELD_NUMBER: _ClassVar[int]
    IS_COMPRESSED_FIELD_NUMBER: _ClassVar[int]
    LATEST_MAGNETO_CHANGE_INFO_FIELD_NUMBER: _ClassVar[int]
    IS_CHUNKED_FIELD_NUMBER: _ClassVar[int]
    CHUNK_ENVELOPE_FIELD_NUMBER: _ClassVar[int]
    cluster_id: _pipe_data_pb2.ClusterIdentifier
    magneto_state_object_batch: bytes
    is_last_batch: bool
    is_compressed: bool
    latest_magneto_change_info: bytes
    is_chunked: bool
    chunk_envelope: ChunkEnvelopeProto
    def __init__(self, cluster_id: _Optional[_Union[_pipe_data_pb2.ClusterIdentifier, _Mapping]] = ..., magneto_state_object_batch: _Optional[bytes] = ..., is_last_batch: bool = ..., is_compressed: bool = ..., latest_magneto_change_info: _Optional[bytes] = ..., is_chunked: bool = ..., chunk_envelope: _Optional[_Union[ChunkEnvelopeProto, _Mapping]] = ...) -> None: ...

class SendMagnetoStateResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ChunkEnvelopeProto(_message.Message):
    __slots__ = ("cluster_id", "unique_id", "total_chunks_count")
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    UNIQUE_ID_FIELD_NUMBER: _ClassVar[int]
    TOTAL_CHUNKS_COUNT_FIELD_NUMBER: _ClassVar[int]
    cluster_id: _pipe_data_pb2.ClusterIdentifier
    unique_id: str
    total_chunks_count: int
    def __init__(self, cluster_id: _Optional[_Union[_pipe_data_pb2.ClusterIdentifier, _Mapping]] = ..., unique_id: _Optional[str] = ..., total_chunks_count: _Optional[int] = ...) -> None: ...

class ChunkProto(_message.Message):
    __slots__ = ("chunk_envelope", "sequence_number", "data")
    CHUNK_ENVELOPE_FIELD_NUMBER: _ClassVar[int]
    SEQUENCE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    chunk_envelope: ChunkEnvelopeProto
    sequence_number: int
    data: bytes
    def __init__(self, chunk_envelope: _Optional[_Union[ChunkEnvelopeProto, _Mapping]] = ..., sequence_number: _Optional[int] = ..., data: _Optional[bytes] = ...) -> None: ...

class ChunkUploadResult(_message.Message):
    __slots__ = ("message", "status")
    class ChunkUploadStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kFailed: _ClassVar[ChunkUploadResult.ChunkUploadStatus]
        kSuccess: _ClassVar[ChunkUploadResult.ChunkUploadStatus]
        kRejected: _ClassVar[ChunkUploadResult.ChunkUploadStatus]
    kFailed: ChunkUploadResult.ChunkUploadStatus
    kSuccess: ChunkUploadResult.ChunkUploadStatus
    kRejected: ChunkUploadResult.ChunkUploadStatus
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    message: str
    status: ChunkUploadResult.ChunkUploadStatus
    def __init__(self, message: _Optional[str] = ..., status: _Optional[_Union[ChunkUploadResult.ChunkUploadStatus, str]] = ...) -> None: ...

class GetMagnetoStateCookieArg(_message.Message):
    __slots__ = ("cluster_id",)
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    cluster_id: _pipe_data_pb2.ClusterIdentifier
    def __init__(self, cluster_id: _Optional[_Union[_pipe_data_pb2.ClusterIdentifier, _Mapping]] = ...) -> None: ...

class GetMagnetoStateCookieResult(_message.Message):
    __slots__ = ("cookie",)
    COOKIE_FIELD_NUMBER: _ClassVar[int]
    cookie: bytes
    def __init__(self, cookie: _Optional[bytes] = ...) -> None: ...

class UploadAuditReportArg(_message.Message):
    __slots__ = ("cluster_id", "audit_report")
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    AUDIT_REPORT_FIELD_NUMBER: _ClassVar[int]
    cluster_id: _pipe_data_pb2.ClusterIdentifier
    audit_report: bytes
    def __init__(self, cluster_id: _Optional[_Union[_pipe_data_pb2.ClusterIdentifier, _Mapping]] = ..., audit_report: _Optional[bytes] = ...) -> None: ...

class UploadAuditReportResult(_message.Message):
    __slots__ = ("license_bytes",)
    LICENSE_BYTES_FIELD_NUMBER: _ClassVar[int]
    license_bytes: bytes
    def __init__(self, license_bytes: _Optional[bytes] = ...) -> None: ...

class SendIndexingStatsArg(_message.Message):
    __slots__ = ("cluster_id", "indexing_stats")
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    INDEXING_STATS_FIELD_NUMBER: _ClassVar[int]
    cluster_id: _pipe_data_pb2.ClusterIdentifier
    indexing_stats: bytes
    def __init__(self, cluster_id: _Optional[_Union[_pipe_data_pb2.ClusterIdentifier, _Mapping]] = ..., indexing_stats: _Optional[bytes] = ...) -> None: ...

class SendIndexingStatsResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SendTagUpdatesArg(_message.Message):
    __slots__ = ("cluster_id", "tag_updates", "is_compressed")
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    TAG_UPDATES_FIELD_NUMBER: _ClassVar[int]
    IS_COMPRESSED_FIELD_NUMBER: _ClassVar[int]
    cluster_id: _pipe_data_pb2.ClusterIdentifier
    tag_updates: bytes
    is_compressed: bool
    def __init__(self, cluster_id: _Optional[_Union[_pipe_data_pb2.ClusterIdentifier, _Mapping]] = ..., tag_updates: _Optional[bytes] = ..., is_compressed: bool = ...) -> None: ...

class SendTagUpdatesResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SendVulscanMetadataArg(_message.Message):
    __slots__ = ("cluster_identifier", "vulscan_metadata")
    CLUSTER_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    VULSCAN_METADATA_FIELD_NUMBER: _ClassVar[int]
    cluster_identifier: _pipe_data_pb2.ClusterIdentifier
    vulscan_metadata: bytes
    def __init__(self, cluster_identifier: _Optional[_Union[_pipe_data_pb2.ClusterIdentifier, _Mapping]] = ..., vulscan_metadata: _Optional[bytes] = ...) -> None: ...

class SendVulscanMetadataResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SendDataClassificationUpdatesArg(_message.Message):
    __slots__ = ("cluster_identifier", "data_classification_updates")
    CLUSTER_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    DATA_CLASSIFICATION_UPDATES_FIELD_NUMBER: _ClassVar[int]
    cluster_identifier: _pipe_data_pb2.ClusterIdentifier
    data_classification_updates: bytes
    def __init__(self, cluster_identifier: _Optional[_Union[_pipe_data_pb2.ClusterIdentifier, _Mapping]] = ..., data_classification_updates: _Optional[bytes] = ...) -> None: ...

class SendDataClassificationUpdatesResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UnregisterClusterLicensingArg(_message.Message):
    __slots__ = ("identifier",)
    IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    identifier: _pipe_data_pb2.ClusterIdentifier
    def __init__(self, identifier: _Optional[_Union[_pipe_data_pb2.ClusterIdentifier, _Mapping]] = ...) -> None: ...

class UnregisterClusterLicensingResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UnregisterArg(_message.Message):
    __slots__ = ("type", "identifier")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    type: UnregisterType
    identifier: _pipe_data_pb2.ClusterIdentifier
    def __init__(self, type: _Optional[_Union[UnregisterType, str]] = ..., identifier: _Optional[_Union[_pipe_data_pb2.ClusterIdentifier, _Mapping]] = ...) -> None: ...

class UnregisterResult(_message.Message):
    __slots__ = ("status_code", "msg")
    STATUS_CODE_FIELD_NUMBER: _ClassVar[int]
    MSG_FIELD_NUMBER: _ClassVar[int]
    status_code: int
    msg: str
    def __init__(self, status_code: _Optional[int] = ..., msg: _Optional[str] = ...) -> None: ...

class SetRigelMaintenanceModeArg(_message.Message):
    __slots__ = ("identifier", "maintenance_mode")
    IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    MAINTENANCE_MODE_FIELD_NUMBER: _ClassVar[int]
    identifier: _pipe_data_pb2.ClusterIdentifier
    maintenance_mode: bool
    def __init__(self, identifier: _Optional[_Union[_pipe_data_pb2.ClusterIdentifier, _Mapping]] = ..., maintenance_mode: bool = ...) -> None: ...

class SetRigelMaintenanceModeResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UpdateClusterTenantArgs(_message.Message):
    __slots__ = ("clusterIdentifier", "tenant")
    CLUSTERIDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    TENANT_FIELD_NUMBER: _ClassVar[int]
    clusterIdentifier: _pipe_data_pb2.ClusterIdentifier
    tenant: _pipe_data_pb2.TenantInfo
    def __init__(self, clusterIdentifier: _Optional[_Union[_pipe_data_pb2.ClusterIdentifier, _Mapping]] = ..., tenant: _Optional[_Union[_pipe_data_pb2.TenantInfo, _Mapping]] = ...) -> None: ...

class UpdateClusterTenantResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UpdateClusterMultiTenancyInfoArgs(_message.Message):
    __slots__ = ("clusterIdentifier", "organizations_enabled", "organizations_storage_domain_sharing_enabled")
    CLUSTERIDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATIONS_ENABLED_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATIONS_STORAGE_DOMAIN_SHARING_ENABLED_FIELD_NUMBER: _ClassVar[int]
    clusterIdentifier: _pipe_data_pb2.ClusterIdentifier
    organizations_enabled: bool
    organizations_storage_domain_sharing_enabled: bool
    def __init__(self, clusterIdentifier: _Optional[_Union[_pipe_data_pb2.ClusterIdentifier, _Mapping]] = ..., organizations_enabled: bool = ..., organizations_storage_domain_sharing_enabled: bool = ...) -> None: ...

class UpdateClusterMultiTenancyInfoResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UpdateTenantAssignmentArgs(_message.Message):
    __slots__ = ("clusterIdentifier", "local_tenant_id", "properties")
    class AssignedProperty(_message.Message):
        __slots__ = ("property_ids", "property_type")
        class PropertyType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            KPolicy: _ClassVar[UpdateTenantAssignmentArgs.AssignedProperty.PropertyType]
        KPolicy: UpdateTenantAssignmentArgs.AssignedProperty.PropertyType
        PROPERTY_IDS_FIELD_NUMBER: _ClassVar[int]
        PROPERTY_TYPE_FIELD_NUMBER: _ClassVar[int]
        property_ids: _containers.RepeatedScalarFieldContainer[str]
        property_type: UpdateTenantAssignmentArgs.AssignedProperty.PropertyType
        def __init__(self, property_ids: _Optional[_Iterable[str]] = ..., property_type: _Optional[_Union[UpdateTenantAssignmentArgs.AssignedProperty.PropertyType, str]] = ...) -> None: ...
    CLUSTERIDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    LOCAL_TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    clusterIdentifier: _pipe_data_pb2.ClusterIdentifier
    local_tenant_id: str
    properties: _containers.RepeatedCompositeFieldContainer[UpdateTenantAssignmentArgs.AssignedProperty]
    def __init__(self, clusterIdentifier: _Optional[_Union[_pipe_data_pb2.ClusterIdentifier, _Mapping]] = ..., local_tenant_id: _Optional[str] = ..., properties: _Optional[_Iterable[_Union[UpdateTenantAssignmentArgs.AssignedProperty, _Mapping]]] = ...) -> None: ...

class UpdateTenantAssignmentResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CleanupUnregisteredClustersArg(_message.Message):
    __slots__ = ("clusterIdentifiers",)
    CLUSTERIDENTIFIERS_FIELD_NUMBER: _ClassVar[int]
    clusterIdentifiers: _containers.RepeatedCompositeFieldContainer[_pipe_data_pb2.ClusterIdentifier]
    def __init__(self, clusterIdentifiers: _Optional[_Iterable[_Union[_pipe_data_pb2.ClusterIdentifier, _Mapping]]] = ...) -> None: ...

class CleanupUnregisteredClustersResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UpdateObjectProtectionRunNowArg(_message.Message):
    __slots__ = ("clusterIdentifier", "run_label", "request_start_time_usecs", "objects")
    class ObjectProtectionRunNowObjects(_message.Message):
        __slots__ = ("entity_id", "protection_id", "protection_env_type", "is_cad_run", "backup_type", "tenant_id")
        ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
        PROTECTION_ID_FIELD_NUMBER: _ClassVar[int]
        PROTECTION_ENV_TYPE_FIELD_NUMBER: _ClassVar[int]
        IS_CAD_RUN_FIELD_NUMBER: _ClassVar[int]
        BACKUP_TYPE_FIELD_NUMBER: _ClassVar[int]
        TENANT_ID_FIELD_NUMBER: _ClassVar[int]
        entity_id: int
        protection_id: int
        protection_env_type: _enum_wrappers_pb2.EnvironmentProto
        is_cad_run: bool
        backup_type: _enum_wrappers_pb2.MagnetoBackupType
        tenant_id: str
        def __init__(self, entity_id: _Optional[int] = ..., protection_id: _Optional[int] = ..., protection_env_type: _Optional[_Union[_enum_wrappers_pb2.EnvironmentProto, _Mapping]] = ..., is_cad_run: bool = ..., backup_type: _Optional[_Union[_enum_wrappers_pb2.MagnetoBackupType, _Mapping]] = ..., tenant_id: _Optional[str] = ...) -> None: ...
    CLUSTERIDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    RUN_LABEL_FIELD_NUMBER: _ClassVar[int]
    REQUEST_START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    OBJECTS_FIELD_NUMBER: _ClassVar[int]
    clusterIdentifier: _pipe_data_pb2.ClusterIdentifier
    run_label: str
    request_start_time_usecs: int
    objects: _containers.RepeatedCompositeFieldContainer[UpdateObjectProtectionRunNowArg.ObjectProtectionRunNowObjects]
    def __init__(self, clusterIdentifier: _Optional[_Union[_pipe_data_pb2.ClusterIdentifier, _Mapping]] = ..., run_label: _Optional[str] = ..., request_start_time_usecs: _Optional[int] = ..., objects: _Optional[_Iterable[_Union[UpdateObjectProtectionRunNowArg.ObjectProtectionRunNowObjects, _Mapping]]] = ...) -> None: ...

class UpdateObjectProtectionRunNowResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AuthenticateAwsRoleRequest(_message.Message):
    __slots__ = ("cluster_id", "aws_role")
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    AWS_ROLE_FIELD_NUMBER: _ClassVar[int]
    cluster_id: _pipe_data_pb2.ClusterIdentifier
    aws_role: str
    def __init__(self, cluster_id: _Optional[_Union[_pipe_data_pb2.ClusterIdentifier, _Mapping]] = ..., aws_role: _Optional[str] = ...) -> None: ...

class AuthenticateAwsRoleResult(_message.Message):
    __slots__ = ("aws_role", "aws_access_key_id", "aws_access_secret", "aws_token", "aws_provider_name", "expiry_timestamp", "capability", "prefixes")
    AWS_ROLE_FIELD_NUMBER: _ClassVar[int]
    AWS_ACCESS_KEY_ID_FIELD_NUMBER: _ClassVar[int]
    AWS_ACCESS_SECRET_FIELD_NUMBER: _ClassVar[int]
    AWS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    AWS_PROVIDER_NAME_FIELD_NUMBER: _ClassVar[int]
    EXPIRY_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    CAPABILITY_FIELD_NUMBER: _ClassVar[int]
    PREFIXES_FIELD_NUMBER: _ClassVar[int]
    aws_role: str
    aws_access_key_id: str
    aws_access_secret: str
    aws_token: str
    aws_provider_name: str
    expiry_timestamp: int
    capability: CredCapability
    prefixes: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, aws_role: _Optional[str] = ..., aws_access_key_id: _Optional[str] = ..., aws_access_secret: _Optional[str] = ..., aws_token: _Optional[str] = ..., aws_provider_name: _Optional[str] = ..., expiry_timestamp: _Optional[int] = ..., capability: _Optional[_Union[CredCapability, str]] = ..., prefixes: _Optional[_Iterable[str]] = ...) -> None: ...

class GetRigelS3EndpointArg(_message.Message):
    __slots__ = ("identifier", "connection_id")
    IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_ID_FIELD_NUMBER: _ClassVar[int]
    identifier: _pipe_data_pb2.ClusterIdentifier
    connection_id: int
    def __init__(self, identifier: _Optional[_Union[_pipe_data_pb2.ClusterIdentifier, _Mapping]] = ..., connection_id: _Optional[int] = ...) -> None: ...

class GetRigelS3EndpointResult(_message.Message):
    __slots__ = ("endpoint", "region")
    ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    endpoint: str
    region: str
    def __init__(self, endpoint: _Optional[str] = ..., region: _Optional[str] = ...) -> None: ...

class BringUpRigelArg(_message.Message):
    __slots__ = ("identifier", "connection_id")
    IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_ID_FIELD_NUMBER: _ClassVar[int]
    identifier: _pipe_data_pb2.ClusterIdentifier
    connection_id: int
    def __init__(self, identifier: _Optional[_Union[_pipe_data_pb2.ClusterIdentifier, _Mapping]] = ..., connection_id: _Optional[int] = ...) -> None: ...

class BringUpRigelResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetRpaasS3CredentialsRequest(_message.Message):
    __slots__ = ("identifier", "vault_id", "capabilities", "restore_task_id", "search_job_id", "job_id", "capability", "prefix")
    IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    VAULT_ID_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    RESTORE_TASK_ID_FIELD_NUMBER: _ClassVar[int]
    SEARCH_JOB_ID_FIELD_NUMBER: _ClassVar[int]
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    CAPABILITY_FIELD_NUMBER: _ClassVar[int]
    PREFIX_FIELD_NUMBER: _ClassVar[int]
    identifier: _pipe_data_pb2.ClusterIdentifier
    vault_id: int
    capabilities: _containers.RepeatedScalarFieldContainer[Capability]
    restore_task_id: str
    search_job_id: str
    job_id: str
    capability: CredCapability
    prefix: str
    def __init__(self, identifier: _Optional[_Union[_pipe_data_pb2.ClusterIdentifier, _Mapping]] = ..., vault_id: _Optional[int] = ..., capabilities: _Optional[_Iterable[_Union[Capability, str]]] = ..., restore_task_id: _Optional[str] = ..., search_job_id: _Optional[str] = ..., job_id: _Optional[str] = ..., capability: _Optional[_Union[CredCapability, str]] = ..., prefix: _Optional[str] = ...) -> None: ...

class GetRpaasS3CredentialsResponse(_message.Message):
    __slots__ = ("credentials", "error")
    CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    credentials: AuthenticateAwsRoleResult
    error: ErrorResponse
    def __init__(self, credentials: _Optional[_Union[AuthenticateAwsRoleResult, _Mapping]] = ..., error: _Optional[_Union[ErrorResponse, _Mapping]] = ...) -> None: ...

class ErrorResponse(_message.Message):
    __slots__ = ("error_code", "description")
    ERROR_CODE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    error_code: int
    description: str
    def __init__(self, error_code: _Optional[int] = ..., description: _Optional[str] = ...) -> None: ...

class GetRpaasKmsCredentialsRequest(_message.Message):
    __slots__ = ("identifier", "vault_id")
    IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    VAULT_ID_FIELD_NUMBER: _ClassVar[int]
    identifier: _pipe_data_pb2.ClusterIdentifier
    vault_id: int
    def __init__(self, identifier: _Optional[_Union[_pipe_data_pb2.ClusterIdentifier, _Mapping]] = ..., vault_id: _Optional[int] = ...) -> None: ...

class GetRpaasKmsCredentialsResponse(_message.Message):
    __slots__ = ("credentials", "error")
    CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    credentials: AuthenticateAwsRoleResult
    error: ErrorResponse
    def __init__(self, credentials: _Optional[_Union[AuthenticateAwsRoleResult, _Mapping]] = ..., error: _Optional[_Union[ErrorResponse, _Mapping]] = ...) -> None: ...

class RenewCertificatesArg(_message.Message):
    __slots__ = ("identifier", "certificate_type", "current_cert_version", "current_cert_public_key")
    class CertificateType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        KRigel: _ClassVar[RenewCertificatesArg.CertificateType]
        KCluster: _ClassVar[RenewCertificatesArg.CertificateType]
        KTenant: _ClassVar[RenewCertificatesArg.CertificateType]
        kOnPremCluster: _ClassVar[RenewCertificatesArg.CertificateType]
    KRigel: RenewCertificatesArg.CertificateType
    KCluster: RenewCertificatesArg.CertificateType
    KTenant: RenewCertificatesArg.CertificateType
    kOnPremCluster: RenewCertificatesArg.CertificateType
    IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    CERTIFICATE_TYPE_FIELD_NUMBER: _ClassVar[int]
    CURRENT_CERT_VERSION_FIELD_NUMBER: _ClassVar[int]
    CURRENT_CERT_PUBLIC_KEY_FIELD_NUMBER: _ClassVar[int]
    identifier: _pipe_data_pb2.ClusterIdentifier
    certificate_type: RenewCertificatesArg.CertificateType
    current_cert_version: int
    current_cert_public_key: str
    def __init__(self, identifier: _Optional[_Union[_pipe_data_pb2.ClusterIdentifier, _Mapping]] = ..., certificate_type: _Optional[_Union[RenewCertificatesArg.CertificateType, str]] = ..., current_cert_version: _Optional[int] = ..., current_cert_public_key: _Optional[str] = ...) -> None: ...

class RenewCertificatesResult(_message.Message):
    __slots__ = ("certificate", "error")
    class Certificate(_message.Message):
        __slots__ = ("certificate", "private_key", "ca_chain")
        CERTIFICATE_FIELD_NUMBER: _ClassVar[int]
        PRIVATE_KEY_FIELD_NUMBER: _ClassVar[int]
        CA_CHAIN_FIELD_NUMBER: _ClassVar[int]
        certificate: str
        private_key: str
        ca_chain: str
        def __init__(self, certificate: _Optional[str] = ..., private_key: _Optional[str] = ..., ca_chain: _Optional[str] = ...) -> None: ...
    CERTIFICATE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    certificate: RenewCertificatesResult.Certificate
    error: ErrorResponse
    def __init__(self, certificate: _Optional[_Union[RenewCertificatesResult.Certificate, _Mapping]] = ..., error: _Optional[_Union[ErrorResponse, _Mapping]] = ...) -> None: ...

class NotifyRenewRigelCertDoneArg(_message.Message):
    __slots__ = ("identifier",)
    IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    identifier: _pipe_data_pb2.ClusterIdentifier
    def __init__(self, identifier: _Optional[_Union[_pipe_data_pb2.ClusterIdentifier, _Mapping]] = ...) -> None: ...

class NotifyRenewRigelCertDoneResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: ErrorResponse
    def __init__(self, error: _Optional[_Union[ErrorResponse, _Mapping]] = ...) -> None: ...

class NotifyRenewCertDoneArg(_message.Message):
    __slots__ = ("identifier", "certificate_type", "current_cert_public_key")
    class CertificateType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        KRigel: _ClassVar[NotifyRenewCertDoneArg.CertificateType]
        KCluster: _ClassVar[NotifyRenewCertDoneArg.CertificateType]
        KTenant: _ClassVar[NotifyRenewCertDoneArg.CertificateType]
    KRigel: NotifyRenewCertDoneArg.CertificateType
    KCluster: NotifyRenewCertDoneArg.CertificateType
    KTenant: NotifyRenewCertDoneArg.CertificateType
    IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    CERTIFICATE_TYPE_FIELD_NUMBER: _ClassVar[int]
    CURRENT_CERT_PUBLIC_KEY_FIELD_NUMBER: _ClassVar[int]
    identifier: _pipe_data_pb2.ClusterIdentifier
    certificate_type: NotifyRenewCertDoneArg.CertificateType
    current_cert_public_key: str
    def __init__(self, identifier: _Optional[_Union[_pipe_data_pb2.ClusterIdentifier, _Mapping]] = ..., certificate_type: _Optional[_Union[NotifyRenewCertDoneArg.CertificateType, str]] = ..., current_cert_public_key: _Optional[str] = ...) -> None: ...

class NotifyRenewCertDoneResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: ErrorResponse
    def __init__(self, error: _Optional[_Union[ErrorResponse, _Mapping]] = ...) -> None: ...

class CreateAgentCertArg(_message.Message):
    __slots__ = ("identifier", "ValidForDays", "agentGuid")
    IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    VALIDFORDAYS_FIELD_NUMBER: _ClassVar[int]
    AGENTGUID_FIELD_NUMBER: _ClassVar[int]
    identifier: _pipe_data_pb2.ClusterIdentifier
    ValidForDays: int
    agentGuid: str
    def __init__(self, identifier: _Optional[_Union[_pipe_data_pb2.ClusterIdentifier, _Mapping]] = ..., ValidForDays: _Optional[int] = ..., agentGuid: _Optional[str] = ...) -> None: ...

class CreateAgentCertResult(_message.Message):
    __slots__ = ("certificate", "error")
    class Certificate(_message.Message):
        __slots__ = ("self_cert", "private_key", "ca_chain")
        SELF_CERT_FIELD_NUMBER: _ClassVar[int]
        PRIVATE_KEY_FIELD_NUMBER: _ClassVar[int]
        CA_CHAIN_FIELD_NUMBER: _ClassVar[int]
        self_cert: str
        private_key: str
        ca_chain: str
        def __init__(self, self_cert: _Optional[str] = ..., private_key: _Optional[str] = ..., ca_chain: _Optional[str] = ...) -> None: ...
    CERTIFICATE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    certificate: CreateAgentCertResult.Certificate
    error: ErrorResponse
    def __init__(self, certificate: _Optional[_Union[CreateAgentCertResult.Certificate, _Mapping]] = ..., error: _Optional[_Union[ErrorResponse, _Mapping]] = ...) -> None: ...
