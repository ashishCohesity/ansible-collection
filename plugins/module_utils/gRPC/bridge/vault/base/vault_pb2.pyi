from bridge.vault.base import azure_pb2 as _azure_pb2
from bridge.vault.base import glacier_pb2 as _glacier_pb2
from bridge.vault.base import nas_pb2 as _nas_pb2
from bridge.vault.base import nearline_pb2 as _nearline_pb2
from bridge.vault.base import on_disk_vault_pb2 as _on_disk_vault_pb2
from bridge.vault.base import qstar_pb2 as _qstar_pb2
from bridge.vault.base import s3_pb2 as _s3_pb2
from bridge.vault.base import worm_pb2 as _worm_pb2
from configs import cluster_config_pb2 as _cluster_config_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AdapterAttributes(_message.Message):
    __slots__ = ("max_object_size_bytes", "max_object_part_size_bytes", "max_parts_per_object", "is_streaming_supported", "finalize_with_data", "parallel_upload_per_object", "cloud_spill_upload_block_size", "prepare_for_upload_required", "overwriting_data_supported", "journal_data_before_upload", "allow_finalizing_objects_multiple_times", "supports_object_range_preparation", "supports_objects_caching", "curl_throttling_supported", "copy_object_ranges_supported", "prefix_deletion_supported", "get_data_lock_supported", "versioning_enabled", "validate_md5_checksum_for_uploads", "validate_object_ranges_supported")
    MAX_OBJECT_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    MAX_OBJECT_PART_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    MAX_PARTS_PER_OBJECT_FIELD_NUMBER: _ClassVar[int]
    IS_STREAMING_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    FINALIZE_WITH_DATA_FIELD_NUMBER: _ClassVar[int]
    PARALLEL_UPLOAD_PER_OBJECT_FIELD_NUMBER: _ClassVar[int]
    CLOUD_SPILL_UPLOAD_BLOCK_SIZE_FIELD_NUMBER: _ClassVar[int]
    PREPARE_FOR_UPLOAD_REQUIRED_FIELD_NUMBER: _ClassVar[int]
    OVERWRITING_DATA_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    JOURNAL_DATA_BEFORE_UPLOAD_FIELD_NUMBER: _ClassVar[int]
    ALLOW_FINALIZING_OBJECTS_MULTIPLE_TIMES_FIELD_NUMBER: _ClassVar[int]
    SUPPORTS_OBJECT_RANGE_PREPARATION_FIELD_NUMBER: _ClassVar[int]
    SUPPORTS_OBJECTS_CACHING_FIELD_NUMBER: _ClassVar[int]
    CURL_THROTTLING_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    COPY_OBJECT_RANGES_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    PREFIX_DELETION_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    GET_DATA_LOCK_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    VERSIONING_ENABLED_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_MD5_CHECKSUM_FOR_UPLOADS_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_OBJECT_RANGES_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    max_object_size_bytes: int
    max_object_part_size_bytes: int
    max_parts_per_object: int
    is_streaming_supported: bool
    finalize_with_data: bool
    parallel_upload_per_object: bool
    cloud_spill_upload_block_size: int
    prepare_for_upload_required: bool
    overwriting_data_supported: bool
    journal_data_before_upload: bool
    allow_finalizing_objects_multiple_times: bool
    supports_object_range_preparation: bool
    supports_objects_caching: bool
    curl_throttling_supported: bool
    copy_object_ranges_supported: bool
    prefix_deletion_supported: bool
    get_data_lock_supported: bool
    versioning_enabled: bool
    validate_md5_checksum_for_uploads: bool
    validate_object_ranges_supported: bool
    def __init__(self, max_object_size_bytes: _Optional[int] = ..., max_object_part_size_bytes: _Optional[int] = ..., max_parts_per_object: _Optional[int] = ..., is_streaming_supported: bool = ..., finalize_with_data: bool = ..., parallel_upload_per_object: bool = ..., cloud_spill_upload_block_size: _Optional[int] = ..., prepare_for_upload_required: bool = ..., overwriting_data_supported: bool = ..., journal_data_before_upload: bool = ..., allow_finalizing_objects_multiple_times: bool = ..., supports_object_range_preparation: bool = ..., supports_objects_caching: bool = ..., curl_throttling_supported: bool = ..., copy_object_ranges_supported: bool = ..., prefix_deletion_supported: bool = ..., get_data_lock_supported: bool = ..., versioning_enabled: bool = ..., validate_md5_checksum_for_uploads: bool = ..., validate_object_ranges_supported: bool = ...) -> None: ...

class VaultObjectCreateContextProto(_message.Message):
    __slots__ = ("azure_create_context", "s3_create_context", "max_object_part_size_bytes", "is_object_empty", "compute_part_size", "object_logical_size", "can_skip_empty_object_creation", "retention_timestamp_secs", "retention_mode", "reuse_object_version")
    AZURE_CREATE_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    S3_CREATE_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    MAX_OBJECT_PART_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    IS_OBJECT_EMPTY_FIELD_NUMBER: _ClassVar[int]
    COMPUTE_PART_SIZE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_LOGICAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    CAN_SKIP_EMPTY_OBJECT_CREATION_FIELD_NUMBER: _ClassVar[int]
    RETENTION_TIMESTAMP_SECS_FIELD_NUMBER: _ClassVar[int]
    RETENTION_MODE_FIELD_NUMBER: _ClassVar[int]
    REUSE_OBJECT_VERSION_FIELD_NUMBER: _ClassVar[int]
    azure_create_context: _azure_pb2.CreateContext
    s3_create_context: _s3_pb2.CreateContext
    max_object_part_size_bytes: int
    is_object_empty: bool
    compute_part_size: bool
    object_logical_size: int
    can_skip_empty_object_creation: bool
    retention_timestamp_secs: int
    retention_mode: _worm_pb2.RetentionMode.Type
    reuse_object_version: bool
    def __init__(self, azure_create_context: _Optional[_Union[_azure_pb2.CreateContext, _Mapping]] = ..., s3_create_context: _Optional[_Union[_s3_pb2.CreateContext, _Mapping]] = ..., max_object_part_size_bytes: _Optional[int] = ..., is_object_empty: bool = ..., compute_part_size: bool = ..., object_logical_size: _Optional[int] = ..., can_skip_empty_object_creation: bool = ..., retention_timestamp_secs: _Optional[int] = ..., retention_mode: _Optional[_Union[_worm_pb2.RetentionMode.Type, str]] = ..., reuse_object_version: bool = ...) -> None: ...

class VaultUploadContextProto(_message.Message):
    __slots__ = ("nearline_upload_context", "glacier_upload_context", "s3_upload_context", "azure_upload_context", "qstar_upload_context", "nas_upload_context", "object_name", "optimal_part_size", "object_version_id")
    NEARLINE_UPLOAD_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    GLACIER_UPLOAD_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    S3_UPLOAD_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    AZURE_UPLOAD_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    QSTAR_UPLOAD_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    NAS_UPLOAD_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    OBJECT_NAME_FIELD_NUMBER: _ClassVar[int]
    OPTIMAL_PART_SIZE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_VERSION_ID_FIELD_NUMBER: _ClassVar[int]
    nearline_upload_context: _nearline_pb2.UploadContext
    glacier_upload_context: _glacier_pb2.UploadContext
    s3_upload_context: _s3_pb2.UploadContext
    azure_upload_context: _azure_pb2.UploadContext
    qstar_upload_context: _qstar_pb2.UploadContext
    nas_upload_context: _nas_pb2.UploadContext
    object_name: str
    optimal_part_size: int
    object_version_id: str
    def __init__(self, nearline_upload_context: _Optional[_Union[_nearline_pb2.UploadContext, _Mapping]] = ..., glacier_upload_context: _Optional[_Union[_glacier_pb2.UploadContext, _Mapping]] = ..., s3_upload_context: _Optional[_Union[_s3_pb2.UploadContext, _Mapping]] = ..., azure_upload_context: _Optional[_Union[_azure_pb2.UploadContext, _Mapping]] = ..., qstar_upload_context: _Optional[_Union[_qstar_pb2.UploadContext, _Mapping]] = ..., nas_upload_context: _Optional[_Union[_nas_pb2.UploadContext, _Mapping]] = ..., object_name: _Optional[str] = ..., optimal_part_size: _Optional[int] = ..., object_version_id: _Optional[str] = ...) -> None: ...

class VaultDownloadContextProto(_message.Message):
    __slots__ = ("nearline_download_context", "glacier_download_context", "azure_download_context", "qstar_download_context", "nas_download_context", "s3_download_context", "on_disk_vault_download_context", "object_version_id")
    NEARLINE_DOWNLOAD_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    GLACIER_DOWNLOAD_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    AZURE_DOWNLOAD_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    QSTAR_DOWNLOAD_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    NAS_DOWNLOAD_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    S3_DOWNLOAD_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    ON_DISK_VAULT_DOWNLOAD_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    OBJECT_VERSION_ID_FIELD_NUMBER: _ClassVar[int]
    nearline_download_context: _nearline_pb2.DownloadContext
    glacier_download_context: _glacier_pb2.DownloadContext
    azure_download_context: _azure_pb2.DownloadContext
    qstar_download_context: _qstar_pb2.DownloadContext
    nas_download_context: _nas_pb2.DownloadContext
    s3_download_context: _s3_pb2.DownloadContext
    on_disk_vault_download_context: _on_disk_vault_pb2.DownloadContext
    object_version_id: str
    def __init__(self, nearline_download_context: _Optional[_Union[_nearline_pb2.DownloadContext, _Mapping]] = ..., glacier_download_context: _Optional[_Union[_glacier_pb2.DownloadContext, _Mapping]] = ..., azure_download_context: _Optional[_Union[_azure_pb2.DownloadContext, _Mapping]] = ..., qstar_download_context: _Optional[_Union[_qstar_pb2.DownloadContext, _Mapping]] = ..., nas_download_context: _Optional[_Union[_nas_pb2.DownloadContext, _Mapping]] = ..., s3_download_context: _Optional[_Union[_s3_pb2.DownloadContext, _Mapping]] = ..., on_disk_vault_download_context: _Optional[_Union[_on_disk_vault_pb2.DownloadContext, _Mapping]] = ..., object_version_id: _Optional[str] = ...) -> None: ...

class VaultListObjectsContextProto(_message.Message):
    __slots__ = ("params", "cookie", "glacier_list_objects_context")
    class Params(_message.Message):
        __slots__ = ("prefix", "cookie", "max_objects", "start_time_usecs", "end_time_usecs", "is_prefix_directory", "starts_after_key", "delimiter")
        PREFIX_FIELD_NUMBER: _ClassVar[int]
        COOKIE_FIELD_NUMBER: _ClassVar[int]
        MAX_OBJECTS_FIELD_NUMBER: _ClassVar[int]
        START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
        END_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
        IS_PREFIX_DIRECTORY_FIELD_NUMBER: _ClassVar[int]
        STARTS_AFTER_KEY_FIELD_NUMBER: _ClassVar[int]
        DELIMITER_FIELD_NUMBER: _ClassVar[int]
        prefix: str
        cookie: str
        max_objects: int
        start_time_usecs: int
        end_time_usecs: int
        is_prefix_directory: bool
        starts_after_key: str
        delimiter: str
        def __init__(self, prefix: _Optional[str] = ..., cookie: _Optional[str] = ..., max_objects: _Optional[int] = ..., start_time_usecs: _Optional[int] = ..., end_time_usecs: _Optional[int] = ..., is_prefix_directory: bool = ..., starts_after_key: _Optional[str] = ..., delimiter: _Optional[str] = ...) -> None: ...
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    COOKIE_FIELD_NUMBER: _ClassVar[int]
    GLACIER_LIST_OBJECTS_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    params: VaultListObjectsContextProto.Params
    cookie: str
    glacier_list_objects_context: _glacier_pb2.ListObjectsContext
    def __init__(self, params: _Optional[_Union[VaultListObjectsContextProto.Params, _Mapping]] = ..., cookie: _Optional[str] = ..., glacier_list_objects_context: _Optional[_Union[_glacier_pb2.ListObjectsContext, _Mapping]] = ...) -> None: ...

class MediaInfoData(_message.Message):
    __slots__ = ("barcode", "location", "is_online")
    BARCODE_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    IS_ONLINE_FIELD_NUMBER: _ClassVar[int]
    barcode: str
    location: str
    is_online: bool
    def __init__(self, barcode: _Optional[str] = ..., location: _Optional[str] = ..., is_online: bool = ...) -> None: ...

class ObjectFileBlockInfo(_message.Message):
    __slots__ = ("offset", "size", "media_info")
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    MEDIA_INFO_FIELD_NUMBER: _ClassVar[int]
    offset: int
    size: int
    media_info: MediaInfoData
    def __init__(self, offset: _Optional[int] = ..., size: _Optional[int] = ..., media_info: _Optional[_Union[MediaInfoData, _Mapping]] = ...) -> None: ...

class VaultObjectInfo(_message.Message):
    __slots__ = ("name", "description", "size", "storage_class", "archive_tier", "s3_restore_status", "cloud_tier_type", "last_modified_epoch", "version_id", "ctag")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    STORAGE_CLASS_FIELD_NUMBER: _ClassVar[int]
    ARCHIVE_TIER_FIELD_NUMBER: _ClassVar[int]
    S3_RESTORE_STATUS_FIELD_NUMBER: _ClassVar[int]
    CLOUD_TIER_TYPE_FIELD_NUMBER: _ClassVar[int]
    LAST_MODIFIED_EPOCH_FIELD_NUMBER: _ClassVar[int]
    VERSION_ID_FIELD_NUMBER: _ClassVar[int]
    CTAG_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    size: int
    storage_class: str
    archive_tier: bool
    s3_restore_status: _s3_pb2.DownloadContext
    cloud_tier_type: _cluster_config_pb2.ClusterConfigProto.Vault.CloudTierType
    last_modified_epoch: int
    version_id: str
    ctag: str
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., size: _Optional[int] = ..., storage_class: _Optional[str] = ..., archive_tier: bool = ..., s3_restore_status: _Optional[_Union[_s3_pb2.DownloadContext, _Mapping]] = ..., cloud_tier_type: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.Vault.CloudTierType, _Mapping]] = ..., last_modified_epoch: _Optional[int] = ..., version_id: _Optional[str] = ..., ctag: _Optional[str] = ...) -> None: ...

class LifecyclePolicyInfo(_message.Message):
    __slots__ = ("name", "lifecycle_enabled", "downtier_days", "deletion_days", "expiration_enabled")
    NAME_FIELD_NUMBER: _ClassVar[int]
    LIFECYCLE_ENABLED_FIELD_NUMBER: _ClassVar[int]
    DOWNTIER_DAYS_FIELD_NUMBER: _ClassVar[int]
    DELETION_DAYS_FIELD_NUMBER: _ClassVar[int]
    EXPIRATION_ENABLED_FIELD_NUMBER: _ClassVar[int]
    name: str
    lifecycle_enabled: bool
    downtier_days: int
    deletion_days: int
    expiration_enabled: bool
    def __init__(self, name: _Optional[str] = ..., lifecycle_enabled: bool = ..., downtier_days: _Optional[int] = ..., deletion_days: _Optional[int] = ..., expiration_enabled: bool = ...) -> None: ...

class VaultExtInfo(_message.Message):
    __slots__ = ("certs_data", "private_endpoint_fqdn", "private_endpoint_ipv4_address")
    class CertsData(_message.Message):
        __slots__ = ("ca_trusted_cert_pem", "client_cert_pem", "client_cert_private_key_pem", "create_timestamp_usec")
        CA_TRUSTED_CERT_PEM_FIELD_NUMBER: _ClassVar[int]
        CLIENT_CERT_PEM_FIELD_NUMBER: _ClassVar[int]
        CLIENT_CERT_PRIVATE_KEY_PEM_FIELD_NUMBER: _ClassVar[int]
        CREATE_TIMESTAMP_USEC_FIELD_NUMBER: _ClassVar[int]
        ca_trusted_cert_pem: bytes
        client_cert_pem: str
        client_cert_private_key_pem: str
        create_timestamp_usec: int
        def __init__(self, ca_trusted_cert_pem: _Optional[bytes] = ..., client_cert_pem: _Optional[str] = ..., client_cert_private_key_pem: _Optional[str] = ..., create_timestamp_usec: _Optional[int] = ...) -> None: ...
    CERTS_DATA_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_ENDPOINT_FQDN_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_ENDPOINT_IPV4_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    certs_data: VaultExtInfo.CertsData
    private_endpoint_fqdn: str
    private_endpoint_ipv4_address: str
    def __init__(self, certs_data: _Optional[_Union[VaultExtInfo.CertsData, _Mapping]] = ..., private_endpoint_fqdn: _Optional[str] = ..., private_endpoint_ipv4_address: _Optional[str] = ...) -> None: ...

class VaultParams(_message.Message):
    __slots__ = ("restore_params",)
    class RestoreParams(_message.Message):
        __slots__ = ("glacier", "allow_marked_for_removal")
        class Glacier(_message.Message):
            __slots__ = ("retrieval_type",)
            class RetrievalType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                kStandard: _ClassVar[VaultParams.RestoreParams.Glacier.RetrievalType]
                kBulk: _ClassVar[VaultParams.RestoreParams.Glacier.RetrievalType]
                kExpedited: _ClassVar[VaultParams.RestoreParams.Glacier.RetrievalType]
            kStandard: VaultParams.RestoreParams.Glacier.RetrievalType
            kBulk: VaultParams.RestoreParams.Glacier.RetrievalType
            kExpedited: VaultParams.RestoreParams.Glacier.RetrievalType
            RETRIEVAL_TYPE_FIELD_NUMBER: _ClassVar[int]
            retrieval_type: VaultParams.RestoreParams.Glacier.RetrievalType
            def __init__(self, retrieval_type: _Optional[_Union[VaultParams.RestoreParams.Glacier.RetrievalType, str]] = ...) -> None: ...
        GLACIER_FIELD_NUMBER: _ClassVar[int]
        ALLOW_MARKED_FOR_REMOVAL_FIELD_NUMBER: _ClassVar[int]
        glacier: VaultParams.RestoreParams.Glacier
        allow_marked_for_removal: bool
        def __init__(self, glacier: _Optional[_Union[VaultParams.RestoreParams.Glacier, _Mapping]] = ..., allow_marked_for_removal: bool = ...) -> None: ...
    RESTORE_PARAMS_FIELD_NUMBER: _ClassVar[int]
    restore_params: VaultParams.RestoreParams
    def __init__(self, restore_params: _Optional[_Union[VaultParams.RestoreParams, _Mapping]] = ...) -> None: ...

class VaultUptierContextProto(_message.Message):
    __slots__ = ("s3_uptier_context", "on_disk_vault_uptier_context", "azure_uptier_context")
    S3_UPTIER_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    ON_DISK_VAULT_UPTIER_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    AZURE_UPTIER_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    s3_uptier_context: _s3_pb2.DownloadContext
    on_disk_vault_uptier_context: _on_disk_vault_pb2.DownloadContext
    azure_uptier_context: _azure_pb2.DownloadContext
    def __init__(self, s3_uptier_context: _Optional[_Union[_s3_pb2.DownloadContext, _Mapping]] = ..., on_disk_vault_uptier_context: _Optional[_Union[_on_disk_vault_pb2.DownloadContext, _Mapping]] = ..., azure_uptier_context: _Optional[_Union[_azure_pb2.DownloadContext, _Mapping]] = ...) -> None: ...

class DataLockPolicyInfo(_message.Message):
    __slots__ = ("datalock_enabled", "retention_days", "retention_years", "retention_secs", "bucket_worm_lock_enabled")
    DATALOCK_ENABLED_FIELD_NUMBER: _ClassVar[int]
    RETENTION_DAYS_FIELD_NUMBER: _ClassVar[int]
    RETENTION_YEARS_FIELD_NUMBER: _ClassVar[int]
    RETENTION_SECS_FIELD_NUMBER: _ClassVar[int]
    BUCKET_WORM_LOCK_ENABLED_FIELD_NUMBER: _ClassVar[int]
    datalock_enabled: bool
    retention_days: int
    retention_years: int
    retention_secs: int
    bucket_worm_lock_enabled: bool
    def __init__(self, datalock_enabled: bool = ..., retention_days: _Optional[int] = ..., retention_years: _Optional[int] = ..., retention_secs: _Optional[int] = ..., bucket_worm_lock_enabled: bool = ...) -> None: ...
