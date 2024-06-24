from bridge.vault.base import vault_pb2 as _vault_pb2
from configs import cluster_config_pb2 as _cluster_config_pb2
from open_util.net import protorpc_pb2 as _protorpc_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ValidateVaultConfigArg(_message.Message):
    __slots__ = ("vault",)
    VAULT_FIELD_NUMBER: _ClassVar[int]
    vault: _cluster_config_pb2.ClusterConfigProto.Vault
    def __init__(self, vault: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.Vault, _Mapping]] = ...) -> None: ...

class ValidateVaultConfigResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ConnectArg(_message.Message):
    __slots__ = ("vault", "force_connect")
    VAULT_FIELD_NUMBER: _ClassVar[int]
    FORCE_CONNECT_FIELD_NUMBER: _ClassVar[int]
    vault: _cluster_config_pb2.ClusterConfigProto.Vault
    force_connect: bool
    def __init__(self, vault: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.Vault, _Mapping]] = ..., force_connect: bool = ...) -> None: ...

class ConnectResult(_message.Message):
    __slots__ = ("credentials", "attributes")
    CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    credentials: bytes
    attributes: _vault_pb2.AdapterAttributes
    def __init__(self, credentials: _Optional[bytes] = ..., attributes: _Optional[_Union[_vault_pb2.AdapterAttributes, _Mapping]] = ...) -> None: ...

class CreateObjectArg(_message.Message):
    __slots__ = ("vault_id", "object_name", "create_context", "rate_limit_bps", "use_hot_storage_tier")
    VAULT_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    RATE_LIMIT_BPS_FIELD_NUMBER: _ClassVar[int]
    USE_HOT_STORAGE_TIER_FIELD_NUMBER: _ClassVar[int]
    vault_id: int
    object_name: str
    create_context: _vault_pb2.VaultObjectCreateContextProto
    rate_limit_bps: int
    use_hot_storage_tier: bool
    def __init__(self, vault_id: _Optional[int] = ..., object_name: _Optional[str] = ..., create_context: _Optional[_Union[_vault_pb2.VaultObjectCreateContextProto, _Mapping]] = ..., rate_limit_bps: _Optional[int] = ..., use_hot_storage_tier: bool = ...) -> None: ...

class CreateObjectResult(_message.Message):
    __slots__ = ("object_name", "upload_context")
    OBJECT_NAME_FIELD_NUMBER: _ClassVar[int]
    UPLOAD_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    object_name: str
    upload_context: _vault_pb2.VaultUploadContextProto
    def __init__(self, object_name: _Optional[str] = ..., upload_context: _Optional[_Union[_vault_pb2.VaultUploadContextProto, _Mapping]] = ...) -> None: ...

class PrepareForUploadArg(_message.Message):
    __slots__ = ("vault_id", "object_name", "object_offset", "data_size", "part_num", "upload_context")
    VAULT_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_NAME_FIELD_NUMBER: _ClassVar[int]
    OBJECT_OFFSET_FIELD_NUMBER: _ClassVar[int]
    DATA_SIZE_FIELD_NUMBER: _ClassVar[int]
    PART_NUM_FIELD_NUMBER: _ClassVar[int]
    UPLOAD_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    vault_id: int
    object_name: str
    object_offset: int
    data_size: int
    part_num: int
    upload_context: _vault_pb2.VaultUploadContextProto
    def __init__(self, vault_id: _Optional[int] = ..., object_name: _Optional[str] = ..., object_offset: _Optional[int] = ..., data_size: _Optional[int] = ..., part_num: _Optional[int] = ..., upload_context: _Optional[_Union[_vault_pb2.VaultUploadContextProto, _Mapping]] = ...) -> None: ...

class PrepareForUploadResult(_message.Message):
    __slots__ = ("upload_context",)
    UPLOAD_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    upload_context: _vault_pb2.VaultUploadContextProto
    def __init__(self, upload_context: _Optional[_Union[_vault_pb2.VaultUploadContextProto, _Mapping]] = ...) -> None: ...

class UploadArg(_message.Message):
    __slots__ = ("vault_id", "object_name", "object_offset", "data_size", "part_num", "upload_context", "rate_limit_bps")
    VAULT_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_NAME_FIELD_NUMBER: _ClassVar[int]
    OBJECT_OFFSET_FIELD_NUMBER: _ClassVar[int]
    DATA_SIZE_FIELD_NUMBER: _ClassVar[int]
    PART_NUM_FIELD_NUMBER: _ClassVar[int]
    UPLOAD_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    RATE_LIMIT_BPS_FIELD_NUMBER: _ClassVar[int]
    vault_id: int
    object_name: str
    object_offset: int
    data_size: int
    part_num: int
    upload_context: _vault_pb2.VaultUploadContextProto
    rate_limit_bps: int
    def __init__(self, vault_id: _Optional[int] = ..., object_name: _Optional[str] = ..., object_offset: _Optional[int] = ..., data_size: _Optional[int] = ..., part_num: _Optional[int] = ..., upload_context: _Optional[_Union[_vault_pb2.VaultUploadContextProto, _Mapping]] = ..., rate_limit_bps: _Optional[int] = ...) -> None: ...

class UploadResult(_message.Message):
    __slots__ = ("upload_context",)
    UPLOAD_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    upload_context: _vault_pb2.VaultUploadContextProto
    def __init__(self, upload_context: _Optional[_Union[_vault_pb2.VaultUploadContextProto, _Mapping]] = ...) -> None: ...

class ResumeUploadArg(_message.Message):
    __slots__ = ("vault_id", "object_name", "upload_context")
    VAULT_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_NAME_FIELD_NUMBER: _ClassVar[int]
    UPLOAD_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    vault_id: int
    object_name: str
    upload_context: _vault_pb2.VaultUploadContextProto
    def __init__(self, vault_id: _Optional[int] = ..., object_name: _Optional[str] = ..., upload_context: _Optional[_Union[_vault_pb2.VaultUploadContextProto, _Mapping]] = ...) -> None: ...

class ResumeUploadResult(_message.Message):
    __slots__ = ("upload_context", "is_object_finalized", "object_size_bytes", "object_name")
    UPLOAD_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    IS_OBJECT_FINALIZED_FIELD_NUMBER: _ClassVar[int]
    OBJECT_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    OBJECT_NAME_FIELD_NUMBER: _ClassVar[int]
    upload_context: _vault_pb2.VaultUploadContextProto
    is_object_finalized: bool
    object_size_bytes: int
    object_name: str
    def __init__(self, upload_context: _Optional[_Union[_vault_pb2.VaultUploadContextProto, _Mapping]] = ..., is_object_finalized: bool = ..., object_size_bytes: _Optional[int] = ..., object_name: _Optional[str] = ...) -> None: ...

class AbortUploadArg(_message.Message):
    __slots__ = ("vault_id", "object_name", "upload_context")
    VAULT_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_NAME_FIELD_NUMBER: _ClassVar[int]
    UPLOAD_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    vault_id: int
    object_name: str
    upload_context: _vault_pb2.VaultUploadContextProto
    def __init__(self, vault_id: _Optional[int] = ..., object_name: _Optional[str] = ..., upload_context: _Optional[_Union[_vault_pb2.VaultUploadContextProto, _Mapping]] = ...) -> None: ...

class AbortUploadResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class FinalizeObjectArg(_message.Message):
    __slots__ = ("vault_id", "object_name", "object_offset", "data_size", "upload_context")
    VAULT_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_NAME_FIELD_NUMBER: _ClassVar[int]
    OBJECT_OFFSET_FIELD_NUMBER: _ClassVar[int]
    DATA_SIZE_FIELD_NUMBER: _ClassVar[int]
    UPLOAD_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    vault_id: int
    object_name: str
    object_offset: int
    data_size: int
    upload_context: _vault_pb2.VaultUploadContextProto
    def __init__(self, vault_id: _Optional[int] = ..., object_name: _Optional[str] = ..., object_offset: _Optional[int] = ..., data_size: _Optional[int] = ..., upload_context: _Optional[_Union[_vault_pb2.VaultUploadContextProto, _Mapping]] = ...) -> None: ...

class FinalizeObjectResult(_message.Message):
    __slots__ = ("object_name",)
    OBJECT_NAME_FIELD_NUMBER: _ClassVar[int]
    object_name: str
    def __init__(self, object_name: _Optional[str] = ...) -> None: ...

class DeleteObjectArg(_message.Message):
    __slots__ = ("vault_id", "object_name")
    VAULT_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_NAME_FIELD_NUMBER: _ClassVar[int]
    vault_id: int
    object_name: str
    def __init__(self, vault_id: _Optional[int] = ..., object_name: _Optional[str] = ...) -> None: ...

class DeleteObjectResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteObjectsArg(_message.Message):
    __slots__ = ("vault_id", "object_name_vec")
    VAULT_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_NAME_VEC_FIELD_NUMBER: _ClassVar[int]
    vault_id: int
    object_name_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, vault_id: _Optional[int] = ..., object_name_vec: _Optional[_Iterable[str]] = ...) -> None: ...

class DeleteObjectsResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class InitiateRestoreArg(_message.Message):
    __slots__ = ("vault_id", "object_name", "offset", "size", "task_id", "restore_params")
    VAULT_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_NAME_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    RESTORE_PARAMS_FIELD_NUMBER: _ClassVar[int]
    vault_id: int
    object_name: str
    offset: int
    size: int
    task_id: str
    restore_params: _vault_pb2.VaultParams.RestoreParams
    def __init__(self, vault_id: _Optional[int] = ..., object_name: _Optional[str] = ..., offset: _Optional[int] = ..., size: _Optional[int] = ..., task_id: _Optional[str] = ..., restore_params: _Optional[_Union[_vault_pb2.VaultParams.RestoreParams, _Mapping]] = ...) -> None: ...

class InitiateRestoreResult(_message.Message):
    __slots__ = ("download_context",)
    DOWNLOAD_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    download_context: _vault_pb2.VaultDownloadContextProto
    def __init__(self, download_context: _Optional[_Union[_vault_pb2.VaultDownloadContextProto, _Mapping]] = ...) -> None: ...

class CheckInitiateRestoreStatusArg(_message.Message):
    __slots__ = ("vault_id", "object_name", "download_context")
    VAULT_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_NAME_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    vault_id: int
    object_name: str
    download_context: _vault_pb2.VaultDownloadContextProto
    def __init__(self, vault_id: _Optional[int] = ..., object_name: _Optional[str] = ..., download_context: _Optional[_Union[_vault_pb2.VaultDownloadContextProto, _Mapping]] = ...) -> None: ...

class CheckInitiateRestoreStatusResult(_message.Message):
    __slots__ = ("is_ready",)
    IS_READY_FIELD_NUMBER: _ClassVar[int]
    is_ready: bool
    def __init__(self, is_ready: bool = ...) -> None: ...

class DownloadObjectPartArg(_message.Message):
    __slots__ = ("vault_id", "object_name", "download_context", "start_offset", "num_bytes_to_download", "rate_limit_bps")
    VAULT_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_NAME_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    START_OFFSET_FIELD_NUMBER: _ClassVar[int]
    NUM_BYTES_TO_DOWNLOAD_FIELD_NUMBER: _ClassVar[int]
    RATE_LIMIT_BPS_FIELD_NUMBER: _ClassVar[int]
    vault_id: int
    object_name: str
    download_context: _vault_pb2.VaultDownloadContextProto
    start_offset: int
    num_bytes_to_download: int
    rate_limit_bps: int
    def __init__(self, vault_id: _Optional[int] = ..., object_name: _Optional[str] = ..., download_context: _Optional[_Union[_vault_pb2.VaultDownloadContextProto, _Mapping]] = ..., start_offset: _Optional[int] = ..., num_bytes_to_download: _Optional[int] = ..., rate_limit_bps: _Optional[int] = ...) -> None: ...

class DownloadObjectPartResult(_message.Message):
    __slots__ = ("download_context", "eof")
    DOWNLOAD_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    EOF_FIELD_NUMBER: _ClassVar[int]
    download_context: _vault_pb2.VaultDownloadContextProto
    eof: bool
    def __init__(self, download_context: _Optional[_Union[_vault_pb2.VaultDownloadContextProto, _Mapping]] = ..., eof: bool = ...) -> None: ...

class InitiateListObjectsArg(_message.Message):
    __slots__ = ("vault_id", "params")
    VAULT_ID_FIELD_NUMBER: _ClassVar[int]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    vault_id: int
    params: _vault_pb2.VaultListObjectsContextProto.Params
    def __init__(self, vault_id: _Optional[int] = ..., params: _Optional[_Union[_vault_pb2.VaultListObjectsContextProto.Params, _Mapping]] = ...) -> None: ...

class InitiateListObjectsResult(_message.Message):
    __slots__ = ("list_context", "check_status")
    LIST_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    CHECK_STATUS_FIELD_NUMBER: _ClassVar[int]
    list_context: _vault_pb2.VaultListObjectsContextProto
    check_status: bool
    def __init__(self, list_context: _Optional[_Union[_vault_pb2.VaultListObjectsContextProto, _Mapping]] = ..., check_status: bool = ...) -> None: ...

class CheckInitiateListObjectsStatusArg(_message.Message):
    __slots__ = ("vault_id", "list_context")
    VAULT_ID_FIELD_NUMBER: _ClassVar[int]
    LIST_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    vault_id: int
    list_context: _vault_pb2.VaultListObjectsContextProto
    def __init__(self, vault_id: _Optional[int] = ..., list_context: _Optional[_Union[_vault_pb2.VaultListObjectsContextProto, _Mapping]] = ...) -> None: ...

class CheckInitiateListObjectsStatusResult(_message.Message):
    __slots__ = ("list_context", "is_ready")
    LIST_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    IS_READY_FIELD_NUMBER: _ClassVar[int]
    list_context: _vault_pb2.VaultListObjectsContextProto
    is_ready: bool
    def __init__(self, list_context: _Optional[_Union[_vault_pb2.VaultListObjectsContextProto, _Mapping]] = ..., is_ready: bool = ...) -> None: ...

class ListObjectsArg(_message.Message):
    __slots__ = ("vault_id", "list_context")
    VAULT_ID_FIELD_NUMBER: _ClassVar[int]
    LIST_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    vault_id: int
    list_context: _vault_pb2.VaultListObjectsContextProto
    def __init__(self, vault_id: _Optional[int] = ..., list_context: _Optional[_Union[_vault_pb2.VaultListObjectsContextProto, _Mapping]] = ...) -> None: ...

class ListObjectsResult(_message.Message):
    __slots__ = ("list_context", "object_info_vec")
    LIST_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    OBJECT_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    list_context: _vault_pb2.VaultListObjectsContextProto
    object_info_vec: _containers.RepeatedCompositeFieldContainer[_vault_pb2.VaultObjectInfo]
    def __init__(self, list_context: _Optional[_Union[_vault_pb2.VaultListObjectsContextProto, _Mapping]] = ..., object_info_vec: _Optional[_Iterable[_Union[_vault_pb2.VaultObjectInfo, _Mapping]]] = ...) -> None: ...

class GetMediaInfoForArchiveObjectArg(_message.Message):
    __slots__ = ("vault_id", "object_name")
    VAULT_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_NAME_FIELD_NUMBER: _ClassVar[int]
    vault_id: int
    object_name: str
    def __init__(self, vault_id: _Optional[int] = ..., object_name: _Optional[str] = ...) -> None: ...

class GetMediaInfoForArchiveObjectResult(_message.Message):
    __slots__ = ("media_info_vec",)
    MEDIA_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    media_info_vec: _containers.RepeatedCompositeFieldContainer[_vault_pb2.MediaInfoData]
    def __init__(self, media_info_vec: _Optional[_Iterable[_Union[_vault_pb2.MediaInfoData, _Mapping]]] = ...) -> None: ...

class CleanupRestoreObjectArg(_message.Message):
    __slots__ = ("vault_id", "object_name", "download_context")
    VAULT_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_NAME_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    vault_id: int
    object_name: str
    download_context: _vault_pb2.VaultDownloadContextProto
    def __init__(self, vault_id: _Optional[int] = ..., object_name: _Optional[str] = ..., download_context: _Optional[_Union[_vault_pb2.VaultDownloadContextProto, _Mapping]] = ...) -> None: ...

class CleanupRestoreObjectResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetObjectMetadataArg(_message.Message):
    __slots__ = ("vault_id", "object_name")
    VAULT_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_NAME_FIELD_NUMBER: _ClassVar[int]
    vault_id: int
    object_name: str
    def __init__(self, vault_id: _Optional[int] = ..., object_name: _Optional[str] = ...) -> None: ...

class GetObjectMetadataResult(_message.Message):
    __slots__ = ("object_info",)
    OBJECT_INFO_FIELD_NUMBER: _ClassVar[int]
    object_info: _vault_pb2.VaultObjectInfo
    def __init__(self, object_info: _Optional[_Union[_vault_pb2.VaultObjectInfo, _Mapping]] = ...) -> None: ...

class GetLifecyclePolicyInfoArg(_message.Message):
    __slots__ = ("vault_id",)
    VAULT_ID_FIELD_NUMBER: _ClassVar[int]
    vault_id: int
    def __init__(self, vault_id: _Optional[int] = ...) -> None: ...

class GetLifecyclePolicyInfoResult(_message.Message):
    __slots__ = ("lifecycle_policy_info",)
    LIFECYCLE_POLICY_INFO_FIELD_NUMBER: _ClassVar[int]
    lifecycle_policy_info: _vault_pb2.LifecyclePolicyInfo
    def __init__(self, lifecycle_policy_info: _Optional[_Union[_vault_pb2.LifecyclePolicyInfo, _Mapping]] = ...) -> None: ...

class CheckVaultUsageArg(_message.Message):
    __slots__ = ("vault_id",)
    VAULT_ID_FIELD_NUMBER: _ClassVar[int]
    vault_id: int
    def __init__(self, vault_id: _Optional[int] = ...) -> None: ...

class CheckVaultUsageResult(_message.Message):
    __slots__ = ("is_full",)
    IS_FULL_FIELD_NUMBER: _ClassVar[int]
    is_full: bool
    def __init__(self, is_full: bool = ...) -> None: ...
