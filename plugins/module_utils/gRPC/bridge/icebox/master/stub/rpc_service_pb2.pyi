from bridge.base import error_pb2 as _error_pb2
from bridge.icebox.base import icebox_pb2 as _icebox_pb2
from bridge.vault.base import vault_pb2 as _vault_pb2
from cohesion.base import common_pb2 as _common_pb2
from configs import cluster_config_pb2 as _cluster_config_pb2
from magneto.api import worm_pb2 as _worm_pb2
from magneto.base import enums_pb2 as _enums_pb2
from magneto.base import magneto_pb2 as _magneto_pb2
from magneto.base import env_params_pb2 as _env_params_pb2
from magneto.base import permissions_pb2 as _permissions_pb2
from magneto.master.base import master_pb2 as _master_pb2
from open_util.net import protorpc_pb2 as _protorpc_pb2
from stats.base import stats_types_pb2 as _stats_types_pb2
from util.base import op_clock_pb2 as _op_clock_pb2
from util.base import universal_id_pb2 as _universal_id_pb2
from yoda.base import yoda_types_pb2 as _yoda_types_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EntityParams(_message.Message):
    __slots__ = ("entity_id", "metadata", "file_system_name", "relative_snapshot_dir", "total_size_bytes", "progress_monitor_task_path", "prev_archive_uid", "prev_archive_node_id_floor", "entity_name", "view_name", "backup_type", "is_view_app_owned", "prev_local_snapshot_view_id")
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    FILE_SYSTEM_NAME_FIELD_NUMBER: _ClassVar[int]
    RELATIVE_SNAPSHOT_DIR_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_MONITOR_TASK_PATH_FIELD_NUMBER: _ClassVar[int]
    PREV_ARCHIVE_UID_FIELD_NUMBER: _ClassVar[int]
    PREV_ARCHIVE_NODE_ID_FLOOR_FIELD_NUMBER: _ClassVar[int]
    ENTITY_NAME_FIELD_NUMBER: _ClassVar[int]
    VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    BACKUP_TYPE_FIELD_NUMBER: _ClassVar[int]
    IS_VIEW_APP_OWNED_FIELD_NUMBER: _ClassVar[int]
    PREV_LOCAL_SNAPSHOT_VIEW_ID_FIELD_NUMBER: _ClassVar[int]
    entity_id: int
    metadata: bytes
    file_system_name: str
    relative_snapshot_dir: str
    total_size_bytes: int
    progress_monitor_task_path: str
    prev_archive_uid: _universal_id_pb2.UniversalIdProto
    prev_archive_node_id_floor: int
    entity_name: str
    view_name: str
    backup_type: _enums_pb2.ScheduledBackupType.Type
    is_view_app_owned: bool
    prev_local_snapshot_view_id: int
    def __init__(self, entity_id: _Optional[int] = ..., metadata: _Optional[bytes] = ..., file_system_name: _Optional[str] = ..., relative_snapshot_dir: _Optional[str] = ..., total_size_bytes: _Optional[int] = ..., progress_monitor_task_path: _Optional[str] = ..., prev_archive_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., prev_archive_node_id_floor: _Optional[int] = ..., entity_name: _Optional[str] = ..., view_name: _Optional[str] = ..., backup_type: _Optional[_Union[_enums_pb2.ScheduledBackupType.Type, str]] = ..., is_view_app_owned: bool = ..., prev_local_snapshot_view_id: _Optional[int] = ...) -> None: ...

class ArchivalJobParams(_message.Message):
    __slots__ = ("archive_uid", "application_name", "job_uid", "snapshot_timestamp_usecs", "job_name", "job_instance_id", "job_metadata", "entity_vec", "vault_id", "viewbox_id", "view_name", "expiry_timestamp_usecs", "root_progress_monitor_task_path", "archive_view", "prev_archive_uid", "job_run_metadata", "node_id_floor", "app_job_type", "upload_files_as_is", "archive_now", "worm_policy_type", "data_lock_constraints", "set_legal_hold", "direct_archive_job", "native_format", "cloud_tier_setting", "force_full_traversal_for_frontend_size_info")
    ARCHIVE_UID_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_NAME_FIELD_NUMBER: _ClassVar[int]
    JOB_UID_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
    JOB_NAME_FIELD_NUMBER: _ClassVar[int]
    JOB_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    JOB_METADATA_FIELD_NUMBER: _ClassVar[int]
    ENTITY_VEC_FIELD_NUMBER: _ClassVar[int]
    VAULT_ID_FIELD_NUMBER: _ClassVar[int]
    VIEWBOX_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    EXPIRY_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
    ROOT_PROGRESS_MONITOR_TASK_PATH_FIELD_NUMBER: _ClassVar[int]
    ARCHIVE_VIEW_FIELD_NUMBER: _ClassVar[int]
    PREV_ARCHIVE_UID_FIELD_NUMBER: _ClassVar[int]
    JOB_RUN_METADATA_FIELD_NUMBER: _ClassVar[int]
    NODE_ID_FLOOR_FIELD_NUMBER: _ClassVar[int]
    APP_JOB_TYPE_FIELD_NUMBER: _ClassVar[int]
    UPLOAD_FILES_AS_IS_FIELD_NUMBER: _ClassVar[int]
    ARCHIVE_NOW_FIELD_NUMBER: _ClassVar[int]
    WORM_POLICY_TYPE_FIELD_NUMBER: _ClassVar[int]
    DATA_LOCK_CONSTRAINTS_FIELD_NUMBER: _ClassVar[int]
    SET_LEGAL_HOLD_FIELD_NUMBER: _ClassVar[int]
    DIRECT_ARCHIVE_JOB_FIELD_NUMBER: _ClassVar[int]
    NATIVE_FORMAT_FIELD_NUMBER: _ClassVar[int]
    CLOUD_TIER_SETTING_FIELD_NUMBER: _ClassVar[int]
    FORCE_FULL_TRAVERSAL_FOR_FRONTEND_SIZE_INFO_FIELD_NUMBER: _ClassVar[int]
    archive_uid: _universal_id_pb2.UniversalIdProto
    application_name: str
    job_uid: _universal_id_pb2.UniversalIdProto
    snapshot_timestamp_usecs: int
    job_name: str
    job_instance_id: int
    job_metadata: bytes
    entity_vec: _containers.RepeatedCompositeFieldContainer[EntityParams]
    vault_id: int
    viewbox_id: int
    view_name: str
    expiry_timestamp_usecs: int
    root_progress_monitor_task_path: str
    archive_view: bool
    prev_archive_uid: _universal_id_pb2.UniversalIdProto
    job_run_metadata: _master_pb2.BackupRunArchiveMDProto
    node_id_floor: int
    app_job_type: _enums_pb2.Environment.Type
    upload_files_as_is: bool
    archive_now: bool
    worm_policy_type: _worm_pb2.WormRetentionProto.WormPolicyType
    data_lock_constraints: _worm_pb2.DataLockConstraintsProto
    set_legal_hold: bool
    direct_archive_job: bool
    native_format: bool
    cloud_tier_setting: _cluster_config_pb2.ClusterConfigProto.Vault.CloudTierSetting
    force_full_traversal_for_frontend_size_info: bool
    def __init__(self, archive_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., application_name: _Optional[str] = ..., job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., snapshot_timestamp_usecs: _Optional[int] = ..., job_name: _Optional[str] = ..., job_instance_id: _Optional[int] = ..., job_metadata: _Optional[bytes] = ..., entity_vec: _Optional[_Iterable[_Union[EntityParams, _Mapping]]] = ..., vault_id: _Optional[int] = ..., viewbox_id: _Optional[int] = ..., view_name: _Optional[str] = ..., expiry_timestamp_usecs: _Optional[int] = ..., root_progress_monitor_task_path: _Optional[str] = ..., archive_view: bool = ..., prev_archive_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., job_run_metadata: _Optional[_Union[_master_pb2.BackupRunArchiveMDProto, _Mapping]] = ..., node_id_floor: _Optional[int] = ..., app_job_type: _Optional[_Union[_enums_pb2.Environment.Type, str]] = ..., upload_files_as_is: bool = ..., archive_now: bool = ..., worm_policy_type: _Optional[_Union[_worm_pb2.WormRetentionProto.WormPolicyType, str]] = ..., data_lock_constraints: _Optional[_Union[_worm_pb2.DataLockConstraintsProto, _Mapping]] = ..., set_legal_hold: bool = ..., direct_archive_job: bool = ..., native_format: bool = ..., cloud_tier_setting: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.Vault.CloudTierSetting, _Mapping]] = ..., force_full_traversal_for_frontend_size_info: bool = ...) -> None: ...

class CohesionCopyParams(_message.Message):
    __slots__ = ("storage_handle", "base_storage_handle")
    STORAGE_HANDLE_FIELD_NUMBER: _ClassVar[int]
    BASE_STORAGE_HANDLE_FIELD_NUMBER: _ClassVar[int]
    storage_handle: _common_pb2.BackupStorageHandle
    base_storage_handle: _common_pb2.BackupStorageHandle
    def __init__(self, storage_handle: _Optional[_Union[_common_pb2.BackupStorageHandle, _Mapping]] = ..., base_storage_handle: _Optional[_Union[_common_pb2.BackupStorageHandle, _Mapping]] = ...) -> None: ...

class ScheduleArchivalJobArg(_message.Message):
    __slots__ = ("job_params", "cohesion_copy_job_params")
    JOB_PARAMS_FIELD_NUMBER: _ClassVar[int]
    COHESION_COPY_JOB_PARAMS_FIELD_NUMBER: _ClassVar[int]
    job_params: ArchivalJobParams
    cohesion_copy_job_params: CohesionCopyParams
    def __init__(self, job_params: _Optional[_Union[ArchivalJobParams, _Mapping]] = ..., cohesion_copy_job_params: _Optional[_Union[CohesionCopyParams, _Mapping]] = ...) -> None: ...

class ScheduleArchivalJobResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CancelArchivalJobArg(_message.Message):
    __slots__ = ("archive_uid",)
    ARCHIVE_UID_FIELD_NUMBER: _ClassVar[int]
    archive_uid: _universal_id_pb2.UniversalIdProto
    def __init__(self, archive_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ...) -> None: ...

class CancelArchivalJobResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteArchiveArg(_message.Message):
    __slots__ = ("archive_uid",)
    ARCHIVE_UID_FIELD_NUMBER: _ClassVar[int]
    archive_uid: _universal_id_pb2.UniversalIdProto
    def __init__(self, archive_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ...) -> None: ...

class DeleteArchiveResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ArchiveFilesArg(_message.Message):
    __slots__ = ("archive_uid", "entity_id", "file_range_info", "file_info_vec", "progress_monitor_path")
    class FileRangeInfo(_message.Message):
        __slots__ = ("checkpoint_file_view_box_id", "checkpoint_file_view_name", "checkpoint_file_system_name", "checkpoint_filepath", "start_filepath", "end_filepath")
        CHECKPOINT_FILE_VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
        CHECKPOINT_FILE_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
        CHECKPOINT_FILE_SYSTEM_NAME_FIELD_NUMBER: _ClassVar[int]
        CHECKPOINT_FILEPATH_FIELD_NUMBER: _ClassVar[int]
        START_FILEPATH_FIELD_NUMBER: _ClassVar[int]
        END_FILEPATH_FIELD_NUMBER: _ClassVar[int]
        checkpoint_file_view_box_id: int
        checkpoint_file_view_name: str
        checkpoint_file_system_name: str
        checkpoint_filepath: str
        start_filepath: str
        end_filepath: str
        def __init__(self, checkpoint_file_view_box_id: _Optional[int] = ..., checkpoint_file_view_name: _Optional[str] = ..., checkpoint_file_system_name: _Optional[str] = ..., checkpoint_filepath: _Optional[str] = ..., start_filepath: _Optional[str] = ..., end_filepath: _Optional[str] = ...) -> None: ...
    class FileInfo(_message.Message):
        __slots__ = ("relative_file_path", "logical_size_bytes", "is_first_path_to_hardlink", "has_hardlinks")
        RELATIVE_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
        LOGICAL_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
        IS_FIRST_PATH_TO_HARDLINK_FIELD_NUMBER: _ClassVar[int]
        HAS_HARDLINKS_FIELD_NUMBER: _ClassVar[int]
        relative_file_path: str
        logical_size_bytes: int
        is_first_path_to_hardlink: bool
        has_hardlinks: bool
        def __init__(self, relative_file_path: _Optional[str] = ..., logical_size_bytes: _Optional[int] = ..., is_first_path_to_hardlink: bool = ..., has_hardlinks: bool = ...) -> None: ...
    ARCHIVE_UID_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    FILE_RANGE_INFO_FIELD_NUMBER: _ClassVar[int]
    FILE_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_MONITOR_PATH_FIELD_NUMBER: _ClassVar[int]
    archive_uid: _universal_id_pb2.UniversalIdProto
    entity_id: int
    file_range_info: ArchiveFilesArg.FileRangeInfo
    file_info_vec: _containers.RepeatedCompositeFieldContainer[ArchiveFilesArg.FileInfo]
    progress_monitor_path: str
    def __init__(self, archive_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., entity_id: _Optional[int] = ..., file_range_info: _Optional[_Union[ArchiveFilesArg.FileRangeInfo, _Mapping]] = ..., file_info_vec: _Optional[_Iterable[_Union[ArchiveFilesArg.FileInfo, _Mapping]]] = ..., progress_monitor_path: _Optional[str] = ...) -> None: ...

class ArchiveFilesResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class CloseDirectArchiveJobArg(_message.Message):
    __slots__ = ("archive_uid", "job_run_metadata")
    ARCHIVE_UID_FIELD_NUMBER: _ClassVar[int]
    JOB_RUN_METADATA_FIELD_NUMBER: _ClassVar[int]
    archive_uid: _universal_id_pb2.UniversalIdProto
    job_run_metadata: _master_pb2.BackupRunArchiveMDProto
    def __init__(self, archive_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., job_run_metadata: _Optional[_Union[_master_pb2.BackupRunArchiveMDProto, _Mapping]] = ...) -> None: ...

class CloseDirectArchiveJobResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ReferenceRetireReason(_message.Message):
    __slots__ = ("code", "detail")
    class ReasonCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kRetiredByApollo: _ClassVar[ReferenceRetireReason.ReasonCode]
        kRetiredByUser: _ClassVar[ReferenceRetireReason.ReasonCode]
        kRetiredByIcebox: _ClassVar[ReferenceRetireReason.ReasonCode]
    kRetiredByApollo: ReferenceRetireReason.ReasonCode
    kRetiredByUser: ReferenceRetireReason.ReasonCode
    kRetiredByIcebox: ReferenceRetireReason.ReasonCode
    CODE_FIELD_NUMBER: _ClassVar[int]
    DETAIL_FIELD_NUMBER: _ClassVar[int]
    code: ReferenceRetireReason.ReasonCode
    detail: str
    def __init__(self, code: _Optional[_Union[ReferenceRetireReason.ReasonCode, str]] = ..., detail: _Optional[str] = ...) -> None: ...

class RetireReferenceArg(_message.Message):
    __slots__ = ("archive_uid", "app_job_uid", "vault_id", "reason", "opclock_vec", "epoch_id_info_vec")
    ARCHIVE_UID_FIELD_NUMBER: _ClassVar[int]
    APP_JOB_UID_FIELD_NUMBER: _ClassVar[int]
    VAULT_ID_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    OPCLOCK_VEC_FIELD_NUMBER: _ClassVar[int]
    EPOCH_ID_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    archive_uid: _universal_id_pb2.UniversalIdProto
    app_job_uid: _universal_id_pb2.UniversalIdProto
    vault_id: int
    reason: ReferenceRetireReason
    opclock_vec: _containers.RepeatedCompositeFieldContainer[_op_clock_pb2.OpClock]
    epoch_id_info_vec: _containers.RepeatedCompositeFieldContainer[EpochIdInfo]
    def __init__(self, archive_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., app_job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., vault_id: _Optional[int] = ..., reason: _Optional[_Union[ReferenceRetireReason, _Mapping]] = ..., opclock_vec: _Optional[_Iterable[_Union[_op_clock_pb2.OpClock, _Mapping]]] = ..., epoch_id_info_vec: _Optional[_Iterable[_Union[EpochIdInfo, _Mapping]]] = ...) -> None: ...

class RetireReferenceResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ReportTaskProgressArg(_message.Message):
    __slots__ = ("archive_uid", "error", "checkpoint_info", "bytes_transferred", "constituent_id", "task_id", "job_uid", "list_objects_data", "read_metadata_object_info_vec", "files_to_upload_info", "fs_files_data", "get_blobs_info", "objects_validation_info", "archive_object_restore_info_map", "list_cloud_domains_data", "find_accessible_cloud_domains_data", "list_archive_metadata_objects_data", "read_archive_metadata_info", "slave_session_id", "cohesion_copy_snap_trees_info")
    class ListObjectsData(_message.Message):
        __slots__ = ("object_info_vec", "cookie")
        OBJECT_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
        COOKIE_FIELD_NUMBER: _ClassVar[int]
        object_info_vec: _containers.RepeatedCompositeFieldContainer[_icebox_pb2.ObjectInfoProto]
        cookie: str
        def __init__(self, object_info_vec: _Optional[_Iterable[_Union[_icebox_pb2.ObjectInfoProto, _Mapping]]] = ..., cookie: _Optional[str] = ...) -> None: ...
    class ReadMetadataObjectInfo(_message.Message):
        __slots__ = ("object_name", "object_metadata", "archive_metadata", "error", "decryption_key_unavailable")
        OBJECT_NAME_FIELD_NUMBER: _ClassVar[int]
        OBJECT_METADATA_FIELD_NUMBER: _ClassVar[int]
        ARCHIVE_METADATA_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        DECRYPTION_KEY_UNAVAILABLE_FIELD_NUMBER: _ClassVar[int]
        object_name: str
        object_metadata: _icebox_pb2.ArchivalObjectMetadataProto
        archive_metadata: _icebox_pb2.ArchiveMetadataProto
        error: _error_pb2.ErrorProto
        decryption_key_unavailable: bool
        def __init__(self, object_name: _Optional[str] = ..., object_metadata: _Optional[_Union[_icebox_pb2.ArchivalObjectMetadataProto, _Mapping]] = ..., archive_metadata: _Optional[_Union[_icebox_pb2.ArchiveMetadataProto, _Mapping]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., decryption_key_unavailable: bool = ...) -> None: ...
    class FilesToUploadInfo(_message.Message):
        __slots__ = ("file_info_vec", "cookie", "fs_checkpoint_info")
        FILE_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
        COOKIE_FIELD_NUMBER: _ClassVar[int]
        FS_CHECKPOINT_INFO_FIELD_NUMBER: _ClassVar[int]
        file_info_vec: _containers.RepeatedCompositeFieldContainer[_icebox_pb2.FileInfoProto]
        cookie: _icebox_pb2.GetFilesToUploadCookieProto
        fs_checkpoint_info: _icebox_pb2.FileUploadJobMetadataProto.FSCheckpointInfo
        def __init__(self, file_info_vec: _Optional[_Iterable[_Union[_icebox_pb2.FileInfoProto, _Mapping]]] = ..., cookie: _Optional[_Union[_icebox_pb2.GetFilesToUploadCookieProto, _Mapping]] = ..., fs_checkpoint_info: _Optional[_Union[_icebox_pb2.FileUploadJobMetadataProto.FSCheckpointInfo, _Mapping]] = ...) -> None: ...
    class ListFSFilesData(_message.Message):
        __slots__ = ("file_vec", "cookie", "parallel_walker_cookie")
        FILE_VEC_FIELD_NUMBER: _ClassVar[int]
        COOKIE_FIELD_NUMBER: _ClassVar[int]
        PARALLEL_WALKER_COOKIE_FIELD_NUMBER: _ClassVar[int]
        file_vec: _containers.RepeatedCompositeFieldContainer[_icebox_pb2.FSFileProto]
        cookie: str
        parallel_walker_cookie: _icebox_pb2.VaultFSWalkerCookieProto
        def __init__(self, file_vec: _Optional[_Iterable[_Union[_icebox_pb2.FSFileProto, _Mapping]]] = ..., cookie: _Optional[str] = ..., parallel_walker_cookie: _Optional[_Union[_icebox_pb2.VaultFSWalkerCookieProto, _Mapping]] = ...) -> None: ...
    class GetBlobsInfo(_message.Message):
        __slots__ = ("blob_info_vec", "snap_tree_iter_cookie", "blob_info_cookie", "task_size_bytes")
        BLOB_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
        SNAP_TREE_ITER_COOKIE_FIELD_NUMBER: _ClassVar[int]
        BLOB_INFO_COOKIE_FIELD_NUMBER: _ClassVar[int]
        TASK_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
        blob_info_vec: _containers.RepeatedCompositeFieldContainer[_icebox_pb2.BlobInfo]
        snap_tree_iter_cookie: _icebox_pb2.SnapTreeIterCookieProto
        blob_info_cookie: _icebox_pb2.BlobInfo
        task_size_bytes: int
        def __init__(self, blob_info_vec: _Optional[_Iterable[_Union[_icebox_pb2.BlobInfo, _Mapping]]] = ..., snap_tree_iter_cookie: _Optional[_Union[_icebox_pb2.SnapTreeIterCookieProto, _Mapping]] = ..., blob_info_cookie: _Optional[_Union[_icebox_pb2.BlobInfo, _Mapping]] = ..., task_size_bytes: _Optional[int] = ...) -> None: ...
    class ArchiveObjectRestoreInfoMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _icebox_pb2.ArchiveObjectRestoreInfo
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_icebox_pb2.ArchiveObjectRestoreInfo, _Mapping]] = ...) -> None: ...
    class ListCloudDomainsData(_message.Message):
        __slots__ = ("object_info_vec", "cookie")
        OBJECT_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
        COOKIE_FIELD_NUMBER: _ClassVar[int]
        object_info_vec: _containers.RepeatedScalarFieldContainer[str]
        cookie: str
        def __init__(self, object_info_vec: _Optional[_Iterable[str]] = ..., cookie: _Optional[str] = ...) -> None: ...
    class FindAccessibleCloudDomainsData(_message.Message):
        __slots__ = ("cloud_domain_access_info_vec",)
        CLOUD_DOMAIN_ACCESS_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
        cloud_domain_access_info_vec: _containers.RepeatedCompositeFieldContainer[_icebox_pb2.CloudDomainAccessInfo]
        def __init__(self, cloud_domain_access_info_vec: _Optional[_Iterable[_Union[_icebox_pb2.CloudDomainAccessInfo, _Mapping]]] = ...) -> None: ...
    class ListArchiveMetadataObjectsData(_message.Message):
        __slots__ = ("object_info_vec", "cookie", "cloud_domain_config_file", "prefix")
        OBJECT_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
        COOKIE_FIELD_NUMBER: _ClassVar[int]
        CLOUD_DOMAIN_CONFIG_FILE_FIELD_NUMBER: _ClassVar[int]
        PREFIX_FIELD_NUMBER: _ClassVar[int]
        object_info_vec: _containers.RepeatedCompositeFieldContainer[_icebox_pb2.ObjectInfoProto]
        cookie: str
        cloud_domain_config_file: str
        prefix: str
        def __init__(self, object_info_vec: _Optional[_Iterable[_Union[_icebox_pb2.ObjectInfoProto, _Mapping]]] = ..., cookie: _Optional[str] = ..., cloud_domain_config_file: _Optional[str] = ..., prefix: _Optional[str] = ...) -> None: ...
    class ReadArchiveMetadataFromCSRObjectInfo(_message.Message):
        __slots__ = ("object_name", "archive_metadata", "error")
        OBJECT_NAME_FIELD_NUMBER: _ClassVar[int]
        ARCHIVE_METADATA_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        object_name: str
        archive_metadata: _icebox_pb2.ArchiveMetadataProto
        error: _error_pb2.ErrorProto
        def __init__(self, object_name: _Optional[str] = ..., archive_metadata: _Optional[_Union[_icebox_pb2.ArchiveMetadataProto, _Mapping]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...
    class CohesionCopySnapTreesInfo(_message.Message):
        __slots__ = ("tree_sha256_summary_checksum_map",)
        class TreeSha256SummaryChecksumMapEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: int
            value: str
            def __init__(self, key: _Optional[int] = ..., value: _Optional[str] = ...) -> None: ...
        TREE_SHA256_SUMMARY_CHECKSUM_MAP_FIELD_NUMBER: _ClassVar[int]
        tree_sha256_summary_checksum_map: _containers.ScalarMap[int, str]
        def __init__(self, tree_sha256_summary_checksum_map: _Optional[_Mapping[int, str]] = ...) -> None: ...
    ARCHIVE_UID_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    CHECKPOINT_INFO_FIELD_NUMBER: _ClassVar[int]
    BYTES_TRANSFERRED_FIELD_NUMBER: _ClassVar[int]
    CONSTITUENT_ID_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    JOB_UID_FIELD_NUMBER: _ClassVar[int]
    LIST_OBJECTS_DATA_FIELD_NUMBER: _ClassVar[int]
    READ_METADATA_OBJECT_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    FILES_TO_UPLOAD_INFO_FIELD_NUMBER: _ClassVar[int]
    FS_FILES_DATA_FIELD_NUMBER: _ClassVar[int]
    GET_BLOBS_INFO_FIELD_NUMBER: _ClassVar[int]
    OBJECTS_VALIDATION_INFO_FIELD_NUMBER: _ClassVar[int]
    ARCHIVE_OBJECT_RESTORE_INFO_MAP_FIELD_NUMBER: _ClassVar[int]
    LIST_CLOUD_DOMAINS_DATA_FIELD_NUMBER: _ClassVar[int]
    FIND_ACCESSIBLE_CLOUD_DOMAINS_DATA_FIELD_NUMBER: _ClassVar[int]
    LIST_ARCHIVE_METADATA_OBJECTS_DATA_FIELD_NUMBER: _ClassVar[int]
    READ_ARCHIVE_METADATA_INFO_FIELD_NUMBER: _ClassVar[int]
    SLAVE_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    COHESION_COPY_SNAP_TREES_INFO_FIELD_NUMBER: _ClassVar[int]
    archive_uid: _universal_id_pb2.UniversalIdProto
    error: _error_pb2.ErrorProto
    checkpoint_info: _icebox_pb2.TaskCheckpointInfo
    bytes_transferred: int
    constituent_id: int
    task_id: int
    job_uid: _universal_id_pb2.UniversalIdProto
    list_objects_data: ReportTaskProgressArg.ListObjectsData
    read_metadata_object_info_vec: _containers.RepeatedCompositeFieldContainer[ReportTaskProgressArg.ReadMetadataObjectInfo]
    files_to_upload_info: ReportTaskProgressArg.FilesToUploadInfo
    fs_files_data: ReportTaskProgressArg.ListFSFilesData
    get_blobs_info: ReportTaskProgressArg.GetBlobsInfo
    objects_validation_info: _icebox_pb2.ObjectsValidationInfo
    archive_object_restore_info_map: _containers.MessageMap[str, _icebox_pb2.ArchiveObjectRestoreInfo]
    list_cloud_domains_data: ReportTaskProgressArg.ListCloudDomainsData
    find_accessible_cloud_domains_data: ReportTaskProgressArg.FindAccessibleCloudDomainsData
    list_archive_metadata_objects_data: ReportTaskProgressArg.ListArchiveMetadataObjectsData
    read_archive_metadata_info: _containers.RepeatedCompositeFieldContainer[ReportTaskProgressArg.ReadArchiveMetadataFromCSRObjectInfo]
    slave_session_id: int
    cohesion_copy_snap_trees_info: ReportTaskProgressArg.CohesionCopySnapTreesInfo
    def __init__(self, archive_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., checkpoint_info: _Optional[_Union[_icebox_pb2.TaskCheckpointInfo, _Mapping]] = ..., bytes_transferred: _Optional[int] = ..., constituent_id: _Optional[int] = ..., task_id: _Optional[int] = ..., job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., list_objects_data: _Optional[_Union[ReportTaskProgressArg.ListObjectsData, _Mapping]] = ..., read_metadata_object_info_vec: _Optional[_Iterable[_Union[ReportTaskProgressArg.ReadMetadataObjectInfo, _Mapping]]] = ..., files_to_upload_info: _Optional[_Union[ReportTaskProgressArg.FilesToUploadInfo, _Mapping]] = ..., fs_files_data: _Optional[_Union[ReportTaskProgressArg.ListFSFilesData, _Mapping]] = ..., get_blobs_info: _Optional[_Union[ReportTaskProgressArg.GetBlobsInfo, _Mapping]] = ..., objects_validation_info: _Optional[_Union[_icebox_pb2.ObjectsValidationInfo, _Mapping]] = ..., archive_object_restore_info_map: _Optional[_Mapping[str, _icebox_pb2.ArchiveObjectRestoreInfo]] = ..., list_cloud_domains_data: _Optional[_Union[ReportTaskProgressArg.ListCloudDomainsData, _Mapping]] = ..., find_accessible_cloud_domains_data: _Optional[_Union[ReportTaskProgressArg.FindAccessibleCloudDomainsData, _Mapping]] = ..., list_archive_metadata_objects_data: _Optional[_Union[ReportTaskProgressArg.ListArchiveMetadataObjectsData, _Mapping]] = ..., read_archive_metadata_info: _Optional[_Iterable[_Union[ReportTaskProgressArg.ReadArchiveMetadataFromCSRObjectInfo, _Mapping]]] = ..., slave_session_id: _Optional[int] = ..., cohesion_copy_snap_trees_info: _Optional[_Union[ReportTaskProgressArg.CohesionCopySnapTreesInfo, _Mapping]] = ...) -> None: ...

class ReportTaskProgressResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class ScheduleRestoreJobArg(_message.Message):
    __slots__ = ("restore_job_uid", "application_name", "archive_uid", "viewbox_id", "target_view_name", "restore_entity_vec", "restore_file_system_name", "restore_parent_dir_path", "progress_monitor_task_path", "job_name", "app_job_uid", "app_job_instance_id", "vault_id", "expiry_time_usecs", "file_restore_info_vec", "restore_files_to_stub_view", "vault_restore_params", "app_job_type", "restore_files_to_source", "app_job_restore_task_id", "is_uptier_restore_job", "is_download_index_job", "migration_uid", "glacier_flr_restore_option", "restore_file_path", "file_restore_entity_id", "restore_file_path_vec", "file_restore_entity_name", "uptier_job_metadata", "user_info")
    class FileRestoreInfo(_message.Message):
        __slots__ = ("entity_id", "restore_file_path_vec", "target_view_name", "target_fs_name", "target_dir_path", "object_id", "magneto_instance_id")
        ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
        RESTORE_FILE_PATH_VEC_FIELD_NUMBER: _ClassVar[int]
        TARGET_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
        TARGET_FS_NAME_FIELD_NUMBER: _ClassVar[int]
        TARGET_DIR_PATH_FIELD_NUMBER: _ClassVar[int]
        OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
        MAGNETO_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
        entity_id: int
        restore_file_path_vec: _containers.RepeatedScalarFieldContainer[str]
        target_view_name: str
        target_fs_name: str
        target_dir_path: str
        object_id: _magneto_pb2.MagnetoObjectId
        magneto_instance_id: _yoda_types_pb2.MagnetoInstanceId
        def __init__(self, entity_id: _Optional[int] = ..., restore_file_path_vec: _Optional[_Iterable[str]] = ..., target_view_name: _Optional[str] = ..., target_fs_name: _Optional[str] = ..., target_dir_path: _Optional[str] = ..., object_id: _Optional[_Union[_magneto_pb2.MagnetoObjectId, _Mapping]] = ..., magneto_instance_id: _Optional[_Union[_yoda_types_pb2.MagnetoInstanceId, _Mapping]] = ...) -> None: ...
    RESTORE_JOB_UID_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_NAME_FIELD_NUMBER: _ClassVar[int]
    ARCHIVE_UID_FIELD_NUMBER: _ClassVar[int]
    VIEWBOX_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    RESTORE_ENTITY_VEC_FIELD_NUMBER: _ClassVar[int]
    RESTORE_FILE_SYSTEM_NAME_FIELD_NUMBER: _ClassVar[int]
    RESTORE_PARENT_DIR_PATH_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_MONITOR_TASK_PATH_FIELD_NUMBER: _ClassVar[int]
    JOB_NAME_FIELD_NUMBER: _ClassVar[int]
    APP_JOB_UID_FIELD_NUMBER: _ClassVar[int]
    APP_JOB_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    VAULT_ID_FIELD_NUMBER: _ClassVar[int]
    EXPIRY_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    FILE_RESTORE_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    RESTORE_FILES_TO_STUB_VIEW_FIELD_NUMBER: _ClassVar[int]
    VAULT_RESTORE_PARAMS_FIELD_NUMBER: _ClassVar[int]
    APP_JOB_TYPE_FIELD_NUMBER: _ClassVar[int]
    RESTORE_FILES_TO_SOURCE_FIELD_NUMBER: _ClassVar[int]
    APP_JOB_RESTORE_TASK_ID_FIELD_NUMBER: _ClassVar[int]
    IS_UPTIER_RESTORE_JOB_FIELD_NUMBER: _ClassVar[int]
    IS_DOWNLOAD_INDEX_JOB_FIELD_NUMBER: _ClassVar[int]
    MIGRATION_UID_FIELD_NUMBER: _ClassVar[int]
    GLACIER_FLR_RESTORE_OPTION_FIELD_NUMBER: _ClassVar[int]
    RESTORE_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    FILE_RESTORE_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    RESTORE_FILE_PATH_VEC_FIELD_NUMBER: _ClassVar[int]
    FILE_RESTORE_ENTITY_NAME_FIELD_NUMBER: _ClassVar[int]
    UPTIER_JOB_METADATA_FIELD_NUMBER: _ClassVar[int]
    USER_INFO_FIELD_NUMBER: _ClassVar[int]
    restore_job_uid: _universal_id_pb2.UniversalIdProto
    application_name: str
    archive_uid: _universal_id_pb2.UniversalIdProto
    viewbox_id: int
    target_view_name: str
    restore_entity_vec: _containers.RepeatedCompositeFieldContainer[EntityParams]
    restore_file_system_name: str
    restore_parent_dir_path: str
    progress_monitor_task_path: str
    job_name: str
    app_job_uid: _universal_id_pb2.UniversalIdProto
    app_job_instance_id: int
    vault_id: int
    expiry_time_usecs: int
    file_restore_info_vec: _containers.RepeatedCompositeFieldContainer[ScheduleRestoreJobArg.FileRestoreInfo]
    restore_files_to_stub_view: bool
    vault_restore_params: _vault_pb2.VaultParams.RestoreParams
    app_job_type: _enums_pb2.Environment.Type
    restore_files_to_source: bool
    app_job_restore_task_id: int
    is_uptier_restore_job: bool
    is_download_index_job: bool
    migration_uid: str
    glacier_flr_restore_option: _magneto_pb2.RestoreFilesParams.GlacierFLRRestoreOption
    restore_file_path: str
    file_restore_entity_id: int
    restore_file_path_vec: _containers.RepeatedScalarFieldContainer[str]
    file_restore_entity_name: str
    uptier_job_metadata: bytes
    user_info: _permissions_pb2.UserInformation
    def __init__(self, restore_job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., application_name: _Optional[str] = ..., archive_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., viewbox_id: _Optional[int] = ..., target_view_name: _Optional[str] = ..., restore_entity_vec: _Optional[_Iterable[_Union[EntityParams, _Mapping]]] = ..., restore_file_system_name: _Optional[str] = ..., restore_parent_dir_path: _Optional[str] = ..., progress_monitor_task_path: _Optional[str] = ..., job_name: _Optional[str] = ..., app_job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., app_job_instance_id: _Optional[int] = ..., vault_id: _Optional[int] = ..., expiry_time_usecs: _Optional[int] = ..., file_restore_info_vec: _Optional[_Iterable[_Union[ScheduleRestoreJobArg.FileRestoreInfo, _Mapping]]] = ..., restore_files_to_stub_view: bool = ..., vault_restore_params: _Optional[_Union[_vault_pb2.VaultParams.RestoreParams, _Mapping]] = ..., app_job_type: _Optional[_Union[_enums_pb2.Environment.Type, str]] = ..., restore_files_to_source: bool = ..., app_job_restore_task_id: _Optional[int] = ..., is_uptier_restore_job: bool = ..., is_download_index_job: bool = ..., migration_uid: _Optional[str] = ..., glacier_flr_restore_option: _Optional[_Union[_magneto_pb2.RestoreFilesParams.GlacierFLRRestoreOption, str]] = ..., restore_file_path: _Optional[str] = ..., file_restore_entity_id: _Optional[int] = ..., restore_file_path_vec: _Optional[_Iterable[str]] = ..., file_restore_entity_name: _Optional[str] = ..., uptier_job_metadata: _Optional[bytes] = ..., user_info: _Optional[_Union[_permissions_pb2.UserInformation, _Mapping]] = ...) -> None: ...

class ScheduleRestoreJobResult(_message.Message):
    __slots__ = ("error", "restore_job_uid")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    RESTORE_JOB_UID_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    restore_job_uid: _universal_id_pb2.UniversalIdProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., restore_job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ...) -> None: ...

class CancelRestoreJobArg(_message.Message):
    __slots__ = ("restore_job_uid",)
    RESTORE_JOB_UID_FIELD_NUMBER: _ClassVar[int]
    restore_job_uid: _universal_id_pb2.UniversalIdProto
    def __init__(self, restore_job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ...) -> None: ...

class CancelRestoreJobResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class QueryArchivalJobsArg(_message.Message):
    __slots__ = ("application_name", "archive_uid_vec", "vault_id")
    APPLICATION_NAME_FIELD_NUMBER: _ClassVar[int]
    ARCHIVE_UID_VEC_FIELD_NUMBER: _ClassVar[int]
    VAULT_ID_FIELD_NUMBER: _ClassVar[int]
    application_name: str
    archive_uid_vec: _containers.RepeatedCompositeFieldContainer[_universal_id_pb2.UniversalIdProto]
    vault_id: int
    def __init__(self, application_name: _Optional[str] = ..., archive_uid_vec: _Optional[_Iterable[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]]] = ..., vault_id: _Optional[int] = ...) -> None: ...

class QueryArchivalJobsResult(_message.Message):
    __slots__ = ("archival_job_state_vec",)
    ARCHIVAL_JOB_STATE_VEC_FIELD_NUMBER: _ClassVar[int]
    archival_job_state_vec: _containers.RepeatedCompositeFieldContainer[ArchivalJobStateProto]
    def __init__(self, archival_job_state_vec: _Optional[_Iterable[_Union[ArchivalJobStateProto, _Mapping]]] = ...) -> None: ...

class QueryRestoreJobsArg(_message.Message):
    __slots__ = ("application_name", "restore_job_uid_vec", "user_info")
    APPLICATION_NAME_FIELD_NUMBER: _ClassVar[int]
    RESTORE_JOB_UID_VEC_FIELD_NUMBER: _ClassVar[int]
    USER_INFO_FIELD_NUMBER: _ClassVar[int]
    application_name: str
    restore_job_uid_vec: _containers.RepeatedCompositeFieldContainer[_universal_id_pb2.UniversalIdProto]
    user_info: _permissions_pb2.UserInformation
    def __init__(self, application_name: _Optional[str] = ..., restore_job_uid_vec: _Optional[_Iterable[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]]] = ..., user_info: _Optional[_Union[_permissions_pb2.UserInformation, _Mapping]] = ...) -> None: ...

class QueryRestoreJobsResult(_message.Message):
    __slots__ = ("restore_job_state_vec", "error")
    RESTORE_JOB_STATE_VEC_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    restore_job_state_vec: _containers.RepeatedCompositeFieldContainer[RestoreJobStateProto]
    error: _error_pb2.ErrorProto
    def __init__(self, restore_job_state_vec: _Optional[_Iterable[_Union[RestoreJobStateProto, _Mapping]]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class ArchivalJobStateProto(_message.Message):
    __slots__ = ("archive_uid", "status", "error", "application_name", "start_timestamp_usecs", "end_timestamp_usecs", "logical_size_bytes", "num_logical_bytes_transferred", "num_physical_bytes_transferred", "entity_state_vec", "progress_monitor_task_path", "user_action_required_msg", "avg_logical_transfer_rate_bps", "is_incremental_archive", "is_reference_archive", "expiry_timestamp_usecs", "app_job_uid", "app_job_instance_id", "snapshot_time_usecs", "is_app_notified", "is_cloud_domain_archive", "archive_worm_properties", "is_cad_archive", "reset_attempt_num")
    ARCHIVE_UID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_NAME_FIELD_NUMBER: _ClassVar[int]
    START_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
    END_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
    LOGICAL_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    NUM_LOGICAL_BYTES_TRANSFERRED_FIELD_NUMBER: _ClassVar[int]
    NUM_PHYSICAL_BYTES_TRANSFERRED_FIELD_NUMBER: _ClassVar[int]
    ENTITY_STATE_VEC_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_MONITOR_TASK_PATH_FIELD_NUMBER: _ClassVar[int]
    USER_ACTION_REQUIRED_MSG_FIELD_NUMBER: _ClassVar[int]
    AVG_LOGICAL_TRANSFER_RATE_BPS_FIELD_NUMBER: _ClassVar[int]
    IS_INCREMENTAL_ARCHIVE_FIELD_NUMBER: _ClassVar[int]
    IS_REFERENCE_ARCHIVE_FIELD_NUMBER: _ClassVar[int]
    EXPIRY_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
    APP_JOB_UID_FIELD_NUMBER: _ClassVar[int]
    APP_JOB_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    IS_APP_NOTIFIED_FIELD_NUMBER: _ClassVar[int]
    IS_CLOUD_DOMAIN_ARCHIVE_FIELD_NUMBER: _ClassVar[int]
    ARCHIVE_WORM_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    IS_CAD_ARCHIVE_FIELD_NUMBER: _ClassVar[int]
    RESET_ATTEMPT_NUM_FIELD_NUMBER: _ClassVar[int]
    archive_uid: _universal_id_pb2.UniversalIdProto
    status: _icebox_pb2.IceboxJobStatus
    error: _error_pb2.ErrorProto
    application_name: str
    start_timestamp_usecs: int
    end_timestamp_usecs: int
    logical_size_bytes: int
    num_logical_bytes_transferred: int
    num_physical_bytes_transferred: int
    entity_state_vec: _containers.RepeatedCompositeFieldContainer[ArchivalEntityStateProto]
    progress_monitor_task_path: str
    user_action_required_msg: str
    avg_logical_transfer_rate_bps: int
    is_incremental_archive: bool
    is_reference_archive: bool
    expiry_timestamp_usecs: int
    app_job_uid: _universal_id_pb2.UniversalIdProto
    app_job_instance_id: int
    snapshot_time_usecs: int
    is_app_notified: bool
    is_cloud_domain_archive: bool
    archive_worm_properties: _worm_pb2.ArchiveWORMProperties
    is_cad_archive: bool
    reset_attempt_num: int
    def __init__(self, archive_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., status: _Optional[_Union[_icebox_pb2.IceboxJobStatus, str]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., application_name: _Optional[str] = ..., start_timestamp_usecs: _Optional[int] = ..., end_timestamp_usecs: _Optional[int] = ..., logical_size_bytes: _Optional[int] = ..., num_logical_bytes_transferred: _Optional[int] = ..., num_physical_bytes_transferred: _Optional[int] = ..., entity_state_vec: _Optional[_Iterable[_Union[ArchivalEntityStateProto, _Mapping]]] = ..., progress_monitor_task_path: _Optional[str] = ..., user_action_required_msg: _Optional[str] = ..., avg_logical_transfer_rate_bps: _Optional[int] = ..., is_incremental_archive: bool = ..., is_reference_archive: bool = ..., expiry_timestamp_usecs: _Optional[int] = ..., app_job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., app_job_instance_id: _Optional[int] = ..., snapshot_time_usecs: _Optional[int] = ..., is_app_notified: bool = ..., is_cloud_domain_archive: bool = ..., archive_worm_properties: _Optional[_Union[_worm_pb2.ArchiveWORMProperties, _Mapping]] = ..., is_cad_archive: bool = ..., reset_attempt_num: _Optional[int] = ...) -> None: ...

class RestoreJobStateProto(_message.Message):
    __slots__ = ("restore_job_uid", "archive_uid", "status", "error", "application_name", "start_timestamp_usecs", "end_timestamp_usecs", "logical_size_bytes", "num_logical_bytes_transferred", "num_physical_bytes_transferred", "job_metadata", "entity_state_vec", "progress_monitor_task_path", "target_view_name", "are_entities_in_single_view", "earliest_entity_expiry_timestamp_usecs", "user_action_required_msg", "avg_logical_transfer_rate_bps", "restore_to_alternate_cluster_params", "stub_view_info_vec", "is_uptier_restore_job", "migration_uid", "stub_view_info", "uptier_job_metadata")
    class RestoreToAlternateClusterParams(_message.Message):
        __slots__ = ("job_run_metadata", "viewbox_id", "entity_id_map")
        class EntityIdMapEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: int
            value: int
            def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
        JOB_RUN_METADATA_FIELD_NUMBER: _ClassVar[int]
        VIEWBOX_ID_FIELD_NUMBER: _ClassVar[int]
        ENTITY_ID_MAP_FIELD_NUMBER: _ClassVar[int]
        job_run_metadata: _master_pb2.BackupRunArchiveMDProto
        viewbox_id: int
        entity_id_map: _containers.ScalarMap[int, int]
        def __init__(self, job_run_metadata: _Optional[_Union[_master_pb2.BackupRunArchiveMDProto, _Mapping]] = ..., viewbox_id: _Optional[int] = ..., entity_id_map: _Optional[_Mapping[int, int]] = ...) -> None: ...
    RESTORE_JOB_UID_FIELD_NUMBER: _ClassVar[int]
    ARCHIVE_UID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_NAME_FIELD_NUMBER: _ClassVar[int]
    START_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
    END_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
    LOGICAL_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    NUM_LOGICAL_BYTES_TRANSFERRED_FIELD_NUMBER: _ClassVar[int]
    NUM_PHYSICAL_BYTES_TRANSFERRED_FIELD_NUMBER: _ClassVar[int]
    JOB_METADATA_FIELD_NUMBER: _ClassVar[int]
    ENTITY_STATE_VEC_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_MONITOR_TASK_PATH_FIELD_NUMBER: _ClassVar[int]
    TARGET_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    ARE_ENTITIES_IN_SINGLE_VIEW_FIELD_NUMBER: _ClassVar[int]
    EARLIEST_ENTITY_EXPIRY_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
    USER_ACTION_REQUIRED_MSG_FIELD_NUMBER: _ClassVar[int]
    AVG_LOGICAL_TRANSFER_RATE_BPS_FIELD_NUMBER: _ClassVar[int]
    RESTORE_TO_ALTERNATE_CLUSTER_PARAMS_FIELD_NUMBER: _ClassVar[int]
    STUB_VIEW_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    IS_UPTIER_RESTORE_JOB_FIELD_NUMBER: _ClassVar[int]
    MIGRATION_UID_FIELD_NUMBER: _ClassVar[int]
    STUB_VIEW_INFO_FIELD_NUMBER: _ClassVar[int]
    UPTIER_JOB_METADATA_FIELD_NUMBER: _ClassVar[int]
    restore_job_uid: _universal_id_pb2.UniversalIdProto
    archive_uid: _universal_id_pb2.UniversalIdProto
    status: _icebox_pb2.IceboxJobStatus
    error: _error_pb2.ErrorProto
    application_name: str
    start_timestamp_usecs: int
    end_timestamp_usecs: int
    logical_size_bytes: int
    num_logical_bytes_transferred: int
    num_physical_bytes_transferred: int
    job_metadata: bytes
    entity_state_vec: _containers.RepeatedCompositeFieldContainer[RestoreEntityStateProto]
    progress_monitor_task_path: str
    target_view_name: str
    are_entities_in_single_view: bool
    earliest_entity_expiry_timestamp_usecs: int
    user_action_required_msg: str
    avg_logical_transfer_rate_bps: int
    restore_to_alternate_cluster_params: RestoreJobStateProto.RestoreToAlternateClusterParams
    stub_view_info_vec: _containers.RepeatedCompositeFieldContainer[_icebox_pb2.StubViewInfo]
    is_uptier_restore_job: bool
    migration_uid: str
    stub_view_info: _icebox_pb2.StubViewInfo
    uptier_job_metadata: bytes
    def __init__(self, restore_job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., archive_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., status: _Optional[_Union[_icebox_pb2.IceboxJobStatus, str]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., application_name: _Optional[str] = ..., start_timestamp_usecs: _Optional[int] = ..., end_timestamp_usecs: _Optional[int] = ..., logical_size_bytes: _Optional[int] = ..., num_logical_bytes_transferred: _Optional[int] = ..., num_physical_bytes_transferred: _Optional[int] = ..., job_metadata: _Optional[bytes] = ..., entity_state_vec: _Optional[_Iterable[_Union[RestoreEntityStateProto, _Mapping]]] = ..., progress_monitor_task_path: _Optional[str] = ..., target_view_name: _Optional[str] = ..., are_entities_in_single_view: bool = ..., earliest_entity_expiry_timestamp_usecs: _Optional[int] = ..., user_action_required_msg: _Optional[str] = ..., avg_logical_transfer_rate_bps: _Optional[int] = ..., restore_to_alternate_cluster_params: _Optional[_Union[RestoreJobStateProto.RestoreToAlternateClusterParams, _Mapping]] = ..., stub_view_info_vec: _Optional[_Iterable[_Union[_icebox_pb2.StubViewInfo, _Mapping]]] = ..., is_uptier_restore_job: bool = ..., migration_uid: _Optional[str] = ..., stub_view_info: _Optional[_Union[_icebox_pb2.StubViewInfo, _Mapping]] = ..., uptier_job_metadata: _Optional[bytes] = ...) -> None: ...

class ArchivalEntityStateProto(_message.Message):
    __slots__ = ("entity_params", "status", "error", "start_timestamp_usecs", "end_timestamp_usecs", "logical_size_bytes", "num_logical_bytes_transferred", "num_physical_bytes_transferred", "frontend_size_bytes")
    ENTITY_PARAMS_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    START_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
    END_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
    LOGICAL_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    NUM_LOGICAL_BYTES_TRANSFERRED_FIELD_NUMBER: _ClassVar[int]
    NUM_PHYSICAL_BYTES_TRANSFERRED_FIELD_NUMBER: _ClassVar[int]
    FRONTEND_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    entity_params: EntityParams
    status: _icebox_pb2.IceboxJobStatus
    error: _error_pb2.ErrorProto
    start_timestamp_usecs: int
    end_timestamp_usecs: int
    logical_size_bytes: int
    num_logical_bytes_transferred: int
    num_physical_bytes_transferred: int
    frontend_size_bytes: int
    def __init__(self, entity_params: _Optional[_Union[EntityParams, _Mapping]] = ..., status: _Optional[_Union[_icebox_pb2.IceboxJobStatus, str]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., start_timestamp_usecs: _Optional[int] = ..., end_timestamp_usecs: _Optional[int] = ..., logical_size_bytes: _Optional[int] = ..., num_logical_bytes_transferred: _Optional[int] = ..., num_physical_bytes_transferred: _Optional[int] = ..., frontend_size_bytes: _Optional[int] = ...) -> None: ...

class RestoreEntityStateProto(_message.Message):
    __slots__ = ("entity_params", "status", "error", "start_timestamp_usecs", "end_timestamp_usecs", "logical_size_bytes", "num_logical_bytes_transferred", "num_physical_bytes_transferred", "expiry_timestamp_usecs", "uptier_expiry_timestamp_usecs")
    ENTITY_PARAMS_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    START_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
    END_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
    LOGICAL_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    NUM_LOGICAL_BYTES_TRANSFERRED_FIELD_NUMBER: _ClassVar[int]
    NUM_PHYSICAL_BYTES_TRANSFERRED_FIELD_NUMBER: _ClassVar[int]
    EXPIRY_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
    UPTIER_EXPIRY_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
    entity_params: EntityParams
    status: _icebox_pb2.IceboxJobStatus
    error: _error_pb2.ErrorProto
    start_timestamp_usecs: int
    end_timestamp_usecs: int
    logical_size_bytes: int
    num_logical_bytes_transferred: int
    num_physical_bytes_transferred: int
    expiry_timestamp_usecs: int
    uptier_expiry_timestamp_usecs: int
    def __init__(self, entity_params: _Optional[_Union[EntityParams, _Mapping]] = ..., status: _Optional[_Union[_icebox_pb2.IceboxJobStatus, str]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., start_timestamp_usecs: _Optional[int] = ..., end_timestamp_usecs: _Optional[int] = ..., logical_size_bytes: _Optional[int] = ..., num_logical_bytes_transferred: _Optional[int] = ..., num_physical_bytes_transferred: _Optional[int] = ..., expiry_timestamp_usecs: _Optional[int] = ..., uptier_expiry_timestamp_usecs: _Optional[int] = ...) -> None: ...

class ValidateVaultConfigArg(_message.Message):
    __slots__ = ("vault",)
    VAULT_FIELD_NUMBER: _ClassVar[int]
    vault: _cluster_config_pb2.ClusterConfigProto.Vault
    def __init__(self, vault: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.Vault, _Mapping]] = ...) -> None: ...

class ValidateVaultConfigResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class AddOrUpdateVaultArg(_message.Message):
    __slots__ = ("vault", "validate_credentials", "is_update", "vault_ext_info", "is_password_encrypted", "cluster_config_version", "is_viewbox_associated", "viewbox_name")
    VAULT_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    IS_UPDATE_FIELD_NUMBER: _ClassVar[int]
    VAULT_EXT_INFO_FIELD_NUMBER: _ClassVar[int]
    IS_PASSWORD_ENCRYPTED_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_CONFIG_VERSION_FIELD_NUMBER: _ClassVar[int]
    IS_VIEWBOX_ASSOCIATED_FIELD_NUMBER: _ClassVar[int]
    VIEWBOX_NAME_FIELD_NUMBER: _ClassVar[int]
    vault: _cluster_config_pb2.ClusterConfigProto.Vault
    validate_credentials: bool
    is_update: bool
    vault_ext_info: _vault_pb2.VaultExtInfo
    is_password_encrypted: bool
    cluster_config_version: int
    is_viewbox_associated: bool
    viewbox_name: str
    def __init__(self, vault: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.Vault, _Mapping]] = ..., validate_credentials: bool = ..., is_update: bool = ..., vault_ext_info: _Optional[_Union[_vault_pb2.VaultExtInfo, _Mapping]] = ..., is_password_encrypted: bool = ..., cluster_config_version: _Optional[int] = ..., is_viewbox_associated: bool = ..., viewbox_name: _Optional[str] = ...) -> None: ...

class AddOrUpdateVaultResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class GetVaultsArg(_message.Message):
    __slots__ = ("id", "uid", "global_uuid", "include_marked_for_removal", "encryption_passphrase")
    ID_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    GLOBAL_UUID_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_MARKED_FOR_REMOVAL_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_PASSPHRASE_FIELD_NUMBER: _ClassVar[int]
    id: int
    uid: _universal_id_pb2.UniversalIdProto
    global_uuid: str
    include_marked_for_removal: bool
    encryption_passphrase: str
    def __init__(self, id: _Optional[int] = ..., uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., global_uuid: _Optional[str] = ..., include_marked_for_removal: bool = ..., encryption_passphrase: _Optional[str] = ...) -> None: ...

class GetVaultsResult(_message.Message):
    __slots__ = ("vault_vec", "error")
    VAULT_VEC_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    vault_vec: _containers.RepeatedCompositeFieldContainer[_cluster_config_pb2.ClusterConfigProto.Vault]
    error: _error_pb2.ErrorProto
    def __init__(self, vault_vec: _Optional[_Iterable[_Union[_cluster_config_pb2.ClusterConfigProto.Vault, _Mapping]]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class AddOrUpdateIceboxPropertiesArg(_message.Message):
    __slots__ = ("icebox_properties",)
    ICEBOX_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    icebox_properties: _cluster_config_pb2.ClusterConfigProto.IceboxProperties
    def __init__(self, icebox_properties: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.IceboxProperties, _Mapping]] = ...) -> None: ...

class AddOrUpdateIceboxPropertiesResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class GetIceboxPropertiesArg(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetIceboxPropertiesResult(_message.Message):
    __slots__ = ("error", "icebox_properties")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ICEBOX_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    icebox_properties: _cluster_config_pb2.ClusterConfigProto.IceboxProperties
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., icebox_properties: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.IceboxProperties, _Mapping]] = ...) -> None: ...

class QueryArchiveMediaInfoArg(_message.Message):
    __slots__ = ("archive_uid", "entity_id_vec", "restore_uid")
    ARCHIVE_UID_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    RESTORE_UID_FIELD_NUMBER: _ClassVar[int]
    archive_uid: _universal_id_pb2.UniversalIdProto
    entity_id_vec: _containers.RepeatedScalarFieldContainer[int]
    restore_uid: _universal_id_pb2.UniversalIdProto
    def __init__(self, archive_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., entity_id_vec: _Optional[_Iterable[int]] = ..., restore_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ...) -> None: ...

class QueryArchiveMediaInfoResult(_message.Message):
    __slots__ = ("media_info_vec", "error")
    MEDIA_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    media_info_vec: _containers.RepeatedCompositeFieldContainer[MediaInfoProto]
    error: _error_pb2.ErrorProto
    def __init__(self, media_info_vec: _Optional[_Iterable[_Union[MediaInfoProto, _Mapping]]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class MediaInfoProto(_message.Message):
    __slots__ = ("barcode", "online", "location")
    BARCODE_FIELD_NUMBER: _ClassVar[int]
    ONLINE_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    barcode: str
    online: bool
    location: str
    def __init__(self, barcode: _Optional[str] = ..., online: bool = ..., location: _Optional[str] = ...) -> None: ...

class DeleteVaultArg(_message.Message):
    __slots__ = ("id", "remove_all_archives", "force_delete", "retry")
    ID_FIELD_NUMBER: _ClassVar[int]
    REMOVE_ALL_ARCHIVES_FIELD_NUMBER: _ClassVar[int]
    FORCE_DELETE_FIELD_NUMBER: _ClassVar[int]
    RETRY_FIELD_NUMBER: _ClassVar[int]
    id: int
    remove_all_archives: bool
    force_delete: bool
    retry: bool
    def __init__(self, id: _Optional[int] = ..., remove_all_archives: bool = ..., force_delete: bool = ..., retry: bool = ...) -> None: ...

class DeleteVaultResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class VaultEncryptionKeyInfoProto(_message.Message):
    __slots__ = ("cluster_name", "key_uid", "encryption_key_data", "vault_id", "vault_name")
    CLUSTER_NAME_FIELD_NUMBER: _ClassVar[int]
    KEY_UID_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_KEY_DATA_FIELD_NUMBER: _ClassVar[int]
    VAULT_ID_FIELD_NUMBER: _ClassVar[int]
    VAULT_NAME_FIELD_NUMBER: _ClassVar[int]
    cluster_name: str
    key_uid: _universal_id_pb2.UniversalIdProto
    encryption_key_data: str
    vault_id: int
    vault_name: str
    def __init__(self, cluster_name: _Optional[str] = ..., key_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., encryption_key_data: _Optional[str] = ..., vault_id: _Optional[int] = ..., vault_name: _Optional[str] = ...) -> None: ...

class GetVaultEncryptionKeyInfoArg(_message.Message):
    __slots__ = ("vault_id",)
    VAULT_ID_FIELD_NUMBER: _ClassVar[int]
    vault_id: int
    def __init__(self, vault_id: _Optional[int] = ...) -> None: ...

class GetVaultEncryptionKeyInfoResult(_message.Message):
    __slots__ = ("error", "info")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    INFO_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    info: VaultEncryptionKeyInfoProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., info: _Optional[_Union[VaultEncryptionKeyInfoProto, _Mapping]] = ...) -> None: ...

class UploadVaultEncryptionKeysInfoArg(_message.Message):
    __slots__ = ("vault_id", "key_info_vec")
    VAULT_ID_FIELD_NUMBER: _ClassVar[int]
    KEY_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    vault_id: int
    key_info_vec: _containers.RepeatedCompositeFieldContainer[VaultEncryptionKeyInfoProto]
    def __init__(self, vault_id: _Optional[int] = ..., key_info_vec: _Optional[_Iterable[_Union[VaultEncryptionKeyInfoProto, _Mapping]]] = ...) -> None: ...

class UploadVaultEncryptionKeysInfoResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class ScheduleCloudDomainMigrationJobArg(_message.Message):
    __slots__ = ("migration_uid", "vault_id", "is_cad_mode", "viewbox_id", "cloud_domain_id", "user_info", "prefix")
    MIGRATION_UID_FIELD_NUMBER: _ClassVar[int]
    VAULT_ID_FIELD_NUMBER: _ClassVar[int]
    IS_CAD_MODE_FIELD_NUMBER: _ClassVar[int]
    VIEWBOX_ID_FIELD_NUMBER: _ClassVar[int]
    CLOUD_DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    USER_INFO_FIELD_NUMBER: _ClassVar[int]
    PREFIX_FIELD_NUMBER: _ClassVar[int]
    migration_uid: str
    vault_id: int
    is_cad_mode: bool
    viewbox_id: int
    cloud_domain_id: int
    user_info: _permissions_pb2.UserInformation
    prefix: str
    def __init__(self, migration_uid: _Optional[str] = ..., vault_id: _Optional[int] = ..., is_cad_mode: bool = ..., viewbox_id: _Optional[int] = ..., cloud_domain_id: _Optional[int] = ..., user_info: _Optional[_Union[_permissions_pb2.UserInformation, _Mapping]] = ..., prefix: _Optional[str] = ...) -> None: ...

class ScheduleCloudDomainMigrationJobResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class CancelCloudDomainMigrationJobArg(_message.Message):
    __slots__ = ("migration_uid",)
    MIGRATION_UID_FIELD_NUMBER: _ClassVar[int]
    migration_uid: str
    def __init__(self, migration_uid: _Optional[str] = ...) -> None: ...

class CancelCloudDomainMigrationJobResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class QueryCloudDomainMigrationJobArg(_message.Message):
    __slots__ = ("migration_uid",)
    MIGRATION_UID_FIELD_NUMBER: _ClassVar[int]
    migration_uid: str
    def __init__(self, migration_uid: _Optional[str] = ...) -> None: ...

class QueryCloudDomainMigrationJobResult(_message.Message):
    __slots__ = ("error", "domain_migration_job_status")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_MIGRATION_JOB_STATUS_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    domain_migration_job_status: _icebox_pb2.DomainMigrationJobMetadataProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., domain_migration_job_status: _Optional[_Union[_icebox_pb2.DomainMigrationJobMetadataProto, _Mapping]] = ...) -> None: ...

class FetchCloudSnapshotArg(_message.Message):
    __slots__ = ("migration_uid", "archive_uid")
    MIGRATION_UID_FIELD_NUMBER: _ClassVar[int]
    ARCHIVE_UID_FIELD_NUMBER: _ClassVar[int]
    migration_uid: str
    archive_uid: _universal_id_pb2.UniversalIdProto
    def __init__(self, migration_uid: _Optional[str] = ..., archive_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ...) -> None: ...

class FetchCloudSnapshotResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class InitiateDomainMigrationDoneArg(_message.Message):
    __slots__ = ("migration_uid",)
    MIGRATION_UID_FIELD_NUMBER: _ClassVar[int]
    migration_uid: str
    def __init__(self, migration_uid: _Optional[str] = ...) -> None: ...

class InitiateDomainMigrationDoneResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class ScheduleCloudDomainRebuildJobArg(_message.Message):
    __slots__ = ("domain_rebuild_job_name", "object_type", "cloud_domain_id")
    class ObjectType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kSnapTreeObjectType: _ClassVar[ScheduleCloudDomainRebuildJobArg.ObjectType]
        kChunkFileObjectType: _ClassVar[ScheduleCloudDomainRebuildJobArg.ObjectType]
    kSnapTreeObjectType: ScheduleCloudDomainRebuildJobArg.ObjectType
    kChunkFileObjectType: ScheduleCloudDomainRebuildJobArg.ObjectType
    DOMAIN_REBUILD_JOB_NAME_FIELD_NUMBER: _ClassVar[int]
    OBJECT_TYPE_FIELD_NUMBER: _ClassVar[int]
    CLOUD_DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    domain_rebuild_job_name: str
    object_type: ScheduleCloudDomainRebuildJobArg.ObjectType
    cloud_domain_id: int
    def __init__(self, domain_rebuild_job_name: _Optional[str] = ..., object_type: _Optional[_Union[ScheduleCloudDomainRebuildJobArg.ObjectType, str]] = ..., cloud_domain_id: _Optional[int] = ...) -> None: ...

class ScheduleCloudDomainRebuildJobResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class ScheduleVaultSearchJobArg(_message.Message):
    __slots__ = ("search_job_name", "vault_id", "application_name", "search_params", "key_info", "pulse_attribute_vec", "user_info")
    SEARCH_JOB_NAME_FIELD_NUMBER: _ClassVar[int]
    VAULT_ID_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_NAME_FIELD_NUMBER: _ClassVar[int]
    SEARCH_PARAMS_FIELD_NUMBER: _ClassVar[int]
    KEY_INFO_FIELD_NUMBER: _ClassVar[int]
    PULSE_ATTRIBUTE_VEC_FIELD_NUMBER: _ClassVar[int]
    USER_INFO_FIELD_NUMBER: _ClassVar[int]
    search_job_name: str
    vault_id: int
    application_name: str
    search_params: _icebox_pb2.VaultSearchParams
    key_info: _containers.RepeatedCompositeFieldContainer[VaultEncryptionKeyInfoProto]
    pulse_attribute_vec: _containers.RepeatedCompositeFieldContainer[_stats_types_pb2.KeyValuePair]
    user_info: _permissions_pb2.UserInformation
    def __init__(self, search_job_name: _Optional[str] = ..., vault_id: _Optional[int] = ..., application_name: _Optional[str] = ..., search_params: _Optional[_Union[_icebox_pb2.VaultSearchParams, _Mapping]] = ..., key_info: _Optional[_Iterable[_Union[VaultEncryptionKeyInfoProto, _Mapping]]] = ..., pulse_attribute_vec: _Optional[_Iterable[_Union[_stats_types_pb2.KeyValuePair, _Mapping]]] = ..., user_info: _Optional[_Union[_permissions_pb2.UserInformation, _Mapping]] = ...) -> None: ...

class ScheduleVaultSearchJobResult(_message.Message):
    __slots__ = ("error", "search_job_uid")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    SEARCH_JOB_UID_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    search_job_uid: _universal_id_pb2.UniversalIdProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., search_job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ...) -> None: ...

class RestoreIndexAndSnapshotInfo(_message.Message):
    __slots__ = ("app_job_uid", "index_time_range", "archive_uid", "viewbox_id")
    APP_JOB_UID_FIELD_NUMBER: _ClassVar[int]
    INDEX_TIME_RANGE_FIELD_NUMBER: _ClassVar[int]
    ARCHIVE_UID_FIELD_NUMBER: _ClassVar[int]
    VIEWBOX_ID_FIELD_NUMBER: _ClassVar[int]
    app_job_uid: _universal_id_pb2.UniversalIdProto
    index_time_range: _icebox_pb2.TimeRange
    archive_uid: _universal_id_pb2.UniversalIdProto
    viewbox_id: int
    def __init__(self, app_job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., index_time_range: _Optional[_Union[_icebox_pb2.TimeRange, _Mapping]] = ..., archive_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., viewbox_id: _Optional[int] = ...) -> None: ...

class ScheduleRestoreIndexAndSnapshotJobsArg(_message.Message):
    __slots__ = ("name", "vault_id", "search_job_uid", "info_vec", "application_name", "vault_restore_params", "user_info")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VAULT_ID_FIELD_NUMBER: _ClassVar[int]
    SEARCH_JOB_UID_FIELD_NUMBER: _ClassVar[int]
    INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_NAME_FIELD_NUMBER: _ClassVar[int]
    VAULT_RESTORE_PARAMS_FIELD_NUMBER: _ClassVar[int]
    USER_INFO_FIELD_NUMBER: _ClassVar[int]
    name: str
    vault_id: int
    search_job_uid: _universal_id_pb2.UniversalIdProto
    info_vec: _containers.RepeatedCompositeFieldContainer[RestoreIndexAndSnapshotInfo]
    application_name: str
    vault_restore_params: _vault_pb2.VaultParams.RestoreParams
    user_info: _permissions_pb2.UserInformation
    def __init__(self, name: _Optional[str] = ..., vault_id: _Optional[int] = ..., search_job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., info_vec: _Optional[_Iterable[_Union[RestoreIndexAndSnapshotInfo, _Mapping]]] = ..., application_name: _Optional[str] = ..., vault_restore_params: _Optional[_Union[_vault_pb2.VaultParams.RestoreParams, _Mapping]] = ..., user_info: _Optional[_Union[_permissions_pb2.UserInformation, _Mapping]] = ...) -> None: ...

class ScheduleRestoreIndexAndSnapshotJobsResult(_message.Message):
    __slots__ = ("error", "job_uid")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    JOB_UID_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    job_uid: _universal_id_pb2.UniversalIdProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ...) -> None: ...

class CancelJobArg(_message.Message):
    __slots__ = ("job_uid",)
    JOB_UID_FIELD_NUMBER: _ClassVar[int]
    job_uid: _universal_id_pb2.UniversalIdProto
    def __init__(self, job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ...) -> None: ...

class CancelJobResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class GetVaultSearchJobsArg(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetVaultSearchJobsResult(_message.Message):
    __slots__ = ("error", "search_job_info_vec")
    class VaultSearchJobInfo(_message.Message):
        __slots__ = ("search_job_name", "search_job_uid", "job_status", "error", "start_time_usecs", "end_time_usecs", "vault_id", "vault_name", "num_app_jobs", "num_clusters", "user_info")
        SEARCH_JOB_NAME_FIELD_NUMBER: _ClassVar[int]
        SEARCH_JOB_UID_FIELD_NUMBER: _ClassVar[int]
        JOB_STATUS_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
        END_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
        VAULT_ID_FIELD_NUMBER: _ClassVar[int]
        VAULT_NAME_FIELD_NUMBER: _ClassVar[int]
        NUM_APP_JOBS_FIELD_NUMBER: _ClassVar[int]
        NUM_CLUSTERS_FIELD_NUMBER: _ClassVar[int]
        USER_INFO_FIELD_NUMBER: _ClassVar[int]
        search_job_name: str
        search_job_uid: _universal_id_pb2.UniversalIdProto
        job_status: _icebox_pb2.IceboxJobStatus
        error: _error_pb2.ErrorProto
        start_time_usecs: int
        end_time_usecs: int
        vault_id: int
        vault_name: str
        num_app_jobs: int
        num_clusters: int
        user_info: _permissions_pb2.UserInformation
        def __init__(self, search_job_name: _Optional[str] = ..., search_job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., job_status: _Optional[_Union[_icebox_pb2.IceboxJobStatus, str]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., start_time_usecs: _Optional[int] = ..., end_time_usecs: _Optional[int] = ..., vault_id: _Optional[int] = ..., vault_name: _Optional[str] = ..., num_app_jobs: _Optional[int] = ..., num_clusters: _Optional[int] = ..., user_info: _Optional[_Union[_permissions_pb2.UserInformation, _Mapping]] = ...) -> None: ...
    ERROR_FIELD_NUMBER: _ClassVar[int]
    SEARCH_JOB_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    search_job_info_vec: _containers.RepeatedCompositeFieldContainer[GetVaultSearchJobsResult.VaultSearchJobInfo]
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., search_job_info_vec: _Optional[_Iterable[_Union[GetVaultSearchJobsResult.VaultSearchJobInfo, _Mapping]]] = ...) -> None: ...

class QueryVaultSearchJobArg(_message.Message):
    __slots__ = ("search_job_uid", "max_app_job_count", "cluster_name", "cookie")
    SEARCH_JOB_UID_FIELD_NUMBER: _ClassVar[int]
    MAX_APP_JOB_COUNT_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_NAME_FIELD_NUMBER: _ClassVar[int]
    COOKIE_FIELD_NUMBER: _ClassVar[int]
    search_job_uid: _universal_id_pb2.UniversalIdProto
    max_app_job_count: int
    cluster_name: str
    cookie: str
    def __init__(self, search_job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., max_app_job_count: _Optional[int] = ..., cluster_name: _Optional[str] = ..., cookie: _Optional[str] = ...) -> None: ...

class QueryVaultSearchJobResult(_message.Message):
    __slots__ = ("error", "search_job_uid", "app_job_info_vec", "cookie", "status", "vault_id", "vault_name", "search_params", "job_error", "num_app_jobs", "num_clusters", "num_cloud_domains", "user_info")
    class QueryVaultSearchCookie(_message.Message):
        __slots__ = ("last_app_job_uid",)
        LAST_APP_JOB_UID_FIELD_NUMBER: _ClassVar[int]
        last_app_job_uid: _universal_id_pb2.UniversalIdProto
        def __init__(self, last_app_job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ...) -> None: ...
    ERROR_FIELD_NUMBER: _ClassVar[int]
    SEARCH_JOB_UID_FIELD_NUMBER: _ClassVar[int]
    APP_JOB_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    COOKIE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    VAULT_ID_FIELD_NUMBER: _ClassVar[int]
    VAULT_NAME_FIELD_NUMBER: _ClassVar[int]
    SEARCH_PARAMS_FIELD_NUMBER: _ClassVar[int]
    JOB_ERROR_FIELD_NUMBER: _ClassVar[int]
    NUM_APP_JOBS_FIELD_NUMBER: _ClassVar[int]
    NUM_CLUSTERS_FIELD_NUMBER: _ClassVar[int]
    NUM_CLOUD_DOMAINS_FIELD_NUMBER: _ClassVar[int]
    USER_INFO_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    search_job_uid: _universal_id_pb2.UniversalIdProto
    app_job_info_vec: _containers.RepeatedCompositeFieldContainer[_icebox_pb2.SearchJobMetadataProto.AppJobInfo]
    cookie: str
    status: _icebox_pb2.IceboxJobStatus
    vault_id: int
    vault_name: str
    search_params: _icebox_pb2.VaultSearchParams
    job_error: _error_pb2.ErrorProto
    num_app_jobs: int
    num_clusters: int
    num_cloud_domains: int
    user_info: _permissions_pb2.UserInformation
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., search_job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., app_job_info_vec: _Optional[_Iterable[_Union[_icebox_pb2.SearchJobMetadataProto.AppJobInfo, _Mapping]]] = ..., cookie: _Optional[str] = ..., status: _Optional[_Union[_icebox_pb2.IceboxJobStatus, str]] = ..., vault_id: _Optional[int] = ..., vault_name: _Optional[str] = ..., search_params: _Optional[_Union[_icebox_pb2.VaultSearchParams, _Mapping]] = ..., job_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., num_app_jobs: _Optional[int] = ..., num_clusters: _Optional[int] = ..., num_cloud_domains: _Optional[int] = ..., user_info: _Optional[_Union[_permissions_pb2.UserInformation, _Mapping]] = ...) -> None: ...

class RestoreIndexAndSnapshotJobStatus(_message.Message):
    __slots__ = ("job_uid", "app_job_info", "restore_snapshot_info", "index_time_range", "index_progress_monitor_task_path", "index_job_status", "index_job_error", "search_job_uid", "parent_job_uid", "app_job_type", "start_timestamp_usecs", "end_timestamp_usecs", "latest_expiry_time_usecs", "user_info", "vault_id", "vault_name")
    class AppJobInfo(_message.Message):
        __slots__ = ("app_job_uid", "app_job_name", "cluster_name", "local_app_job_uid")
        APP_JOB_UID_FIELD_NUMBER: _ClassVar[int]
        APP_JOB_NAME_FIELD_NUMBER: _ClassVar[int]
        CLUSTER_NAME_FIELD_NUMBER: _ClassVar[int]
        LOCAL_APP_JOB_UID_FIELD_NUMBER: _ClassVar[int]
        app_job_uid: _universal_id_pb2.UniversalIdProto
        app_job_name: str
        cluster_name: str
        local_app_job_uid: _universal_id_pb2.UniversalIdProto
        def __init__(self, app_job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., app_job_name: _Optional[str] = ..., cluster_name: _Optional[str] = ..., local_app_job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ...) -> None: ...
    class RestoreSnapshotInfo(_message.Message):
        __slots__ = ("archive_uid", "app_job_instance_id", "snapshot_timestamp_usecs", "job_uid", "progress_monitor_task_path", "job_status", "error", "expiry_time_usecs", "start_timestamp_usecs", "end_timestamp_usecs")
        ARCHIVE_UID_FIELD_NUMBER: _ClassVar[int]
        APP_JOB_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
        SNAPSHOT_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
        JOB_UID_FIELD_NUMBER: _ClassVar[int]
        PROGRESS_MONITOR_TASK_PATH_FIELD_NUMBER: _ClassVar[int]
        JOB_STATUS_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        EXPIRY_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
        START_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
        END_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
        archive_uid: _universal_id_pb2.UniversalIdProto
        app_job_instance_id: int
        snapshot_timestamp_usecs: int
        job_uid: _universal_id_pb2.UniversalIdProto
        progress_monitor_task_path: str
        job_status: _icebox_pb2.IceboxJobStatus
        error: _error_pb2.ErrorProto
        expiry_time_usecs: int
        start_timestamp_usecs: int
        end_timestamp_usecs: int
        def __init__(self, archive_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., app_job_instance_id: _Optional[int] = ..., snapshot_timestamp_usecs: _Optional[int] = ..., job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., progress_monitor_task_path: _Optional[str] = ..., job_status: _Optional[_Union[_icebox_pb2.IceboxJobStatus, str]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., expiry_time_usecs: _Optional[int] = ..., start_timestamp_usecs: _Optional[int] = ..., end_timestamp_usecs: _Optional[int] = ...) -> None: ...
    JOB_UID_FIELD_NUMBER: _ClassVar[int]
    APP_JOB_INFO_FIELD_NUMBER: _ClassVar[int]
    RESTORE_SNAPSHOT_INFO_FIELD_NUMBER: _ClassVar[int]
    INDEX_TIME_RANGE_FIELD_NUMBER: _ClassVar[int]
    INDEX_PROGRESS_MONITOR_TASK_PATH_FIELD_NUMBER: _ClassVar[int]
    INDEX_JOB_STATUS_FIELD_NUMBER: _ClassVar[int]
    INDEX_JOB_ERROR_FIELD_NUMBER: _ClassVar[int]
    SEARCH_JOB_UID_FIELD_NUMBER: _ClassVar[int]
    PARENT_JOB_UID_FIELD_NUMBER: _ClassVar[int]
    APP_JOB_TYPE_FIELD_NUMBER: _ClassVar[int]
    START_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
    END_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
    LATEST_EXPIRY_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    USER_INFO_FIELD_NUMBER: _ClassVar[int]
    VAULT_ID_FIELD_NUMBER: _ClassVar[int]
    VAULT_NAME_FIELD_NUMBER: _ClassVar[int]
    job_uid: _universal_id_pb2.UniversalIdProto
    app_job_info: RestoreIndexAndSnapshotJobStatus.AppJobInfo
    restore_snapshot_info: RestoreIndexAndSnapshotJobStatus.RestoreSnapshotInfo
    index_time_range: _icebox_pb2.TimeRange
    index_progress_monitor_task_path: str
    index_job_status: _icebox_pb2.IceboxJobStatus
    index_job_error: _error_pb2.ErrorProto
    search_job_uid: _universal_id_pb2.UniversalIdProto
    parent_job_uid: _universal_id_pb2.UniversalIdProto
    app_job_type: _enums_pb2.Environment.Type
    start_timestamp_usecs: int
    end_timestamp_usecs: int
    latest_expiry_time_usecs: int
    user_info: _permissions_pb2.UserInformation
    vault_id: int
    vault_name: str
    def __init__(self, job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., app_job_info: _Optional[_Union[RestoreIndexAndSnapshotJobStatus.AppJobInfo, _Mapping]] = ..., restore_snapshot_info: _Optional[_Union[RestoreIndexAndSnapshotJobStatus.RestoreSnapshotInfo, _Mapping]] = ..., index_time_range: _Optional[_Union[_icebox_pb2.TimeRange, _Mapping]] = ..., index_progress_monitor_task_path: _Optional[str] = ..., index_job_status: _Optional[_Union[_icebox_pb2.IceboxJobStatus, str]] = ..., index_job_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., search_job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., parent_job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., app_job_type: _Optional[_Union[_enums_pb2.Environment.Type, str]] = ..., start_timestamp_usecs: _Optional[int] = ..., end_timestamp_usecs: _Optional[int] = ..., latest_expiry_time_usecs: _Optional[int] = ..., user_info: _Optional[_Union[_permissions_pb2.UserInformation, _Mapping]] = ..., vault_id: _Optional[int] = ..., vault_name: _Optional[str] = ...) -> None: ...

class QueryRestoreIndexAndSnapshotJobsArg(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class QueryRestoreIndexAndSnapshotJobsResult(_message.Message):
    __slots__ = ("error", "job_status_vec")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    JOB_STATUS_VEC_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    job_status_vec: _containers.RepeatedCompositeFieldContainer[RestoreIndexAndSnapshotJobStatus]
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., job_status_vec: _Optional[_Iterable[_Union[RestoreIndexAndSnapshotJobStatus, _Mapping]]] = ...) -> None: ...

class NotifyArchivalScheduleRemovedArg(_message.Message):
    __slots__ = ("app_name", "job_uid", "vault_id")
    APP_NAME_FIELD_NUMBER: _ClassVar[int]
    JOB_UID_FIELD_NUMBER: _ClassVar[int]
    VAULT_ID_FIELD_NUMBER: _ClassVar[int]
    app_name: str
    job_uid: _universal_id_pb2.UniversalIdProto
    vault_id: int
    def __init__(self, app_name: _Optional[str] = ..., job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., vault_id: _Optional[int] = ...) -> None: ...

class NotifyArchivalScheduleRemovedResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UpdateExpiryTimeArg(_message.Message):
    __slots__ = ("archive_uid", "expiry_time_usecs", "entity_expiry_time_map", "legal_hold_action", "entity_legal_hold_map", "is_marked_for_removal")
    class LegalHoldAction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kReleaseLegalHold: _ClassVar[UpdateExpiryTimeArg.LegalHoldAction]
        kSetLegalHold: _ClassVar[UpdateExpiryTimeArg.LegalHoldAction]
    kReleaseLegalHold: UpdateExpiryTimeArg.LegalHoldAction
    kSetLegalHold: UpdateExpiryTimeArg.LegalHoldAction
    class EntityExpiryTimeMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    class EntityLegalHoldMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: bool
        def __init__(self, key: _Optional[int] = ..., value: bool = ...) -> None: ...
    ARCHIVE_UID_FIELD_NUMBER: _ClassVar[int]
    EXPIRY_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    ENTITY_EXPIRY_TIME_MAP_FIELD_NUMBER: _ClassVar[int]
    LEGAL_HOLD_ACTION_FIELD_NUMBER: _ClassVar[int]
    ENTITY_LEGAL_HOLD_MAP_FIELD_NUMBER: _ClassVar[int]
    IS_MARKED_FOR_REMOVAL_FIELD_NUMBER: _ClassVar[int]
    archive_uid: _universal_id_pb2.UniversalIdProto
    expiry_time_usecs: int
    entity_expiry_time_map: _containers.ScalarMap[int, int]
    legal_hold_action: UpdateExpiryTimeArg.LegalHoldAction
    entity_legal_hold_map: _containers.ScalarMap[int, bool]
    is_marked_for_removal: bool
    def __init__(self, archive_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., expiry_time_usecs: _Optional[int] = ..., entity_expiry_time_map: _Optional[_Mapping[int, int]] = ..., legal_hold_action: _Optional[_Union[UpdateExpiryTimeArg.LegalHoldAction, str]] = ..., entity_legal_hold_map: _Optional[_Mapping[int, bool]] = ..., is_marked_for_removal: bool = ...) -> None: ...

class UpdateExpiryTimeResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ExtendRestoreJobExpiryTimeArg(_message.Message):
    __slots__ = ("archive_uid",)
    ARCHIVE_UID_FIELD_NUMBER: _ClassVar[int]
    archive_uid: _universal_id_pb2.UniversalIdProto
    def __init__(self, archive_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ...) -> None: ...

class ExtendRestoreJobExpiryTimeResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UpdateLegalHoldArg(_message.Message):
    __slots__ = ("archive_uid", "legal_hold_action", "entity_legal_hold_map")
    class LegalHoldAction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kReleaseLegalHold: _ClassVar[UpdateLegalHoldArg.LegalHoldAction]
        kSetLegalHold: _ClassVar[UpdateLegalHoldArg.LegalHoldAction]
    kReleaseLegalHold: UpdateLegalHoldArg.LegalHoldAction
    kSetLegalHold: UpdateLegalHoldArg.LegalHoldAction
    class EntityLegalHoldMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: bool
        def __init__(self, key: _Optional[int] = ..., value: bool = ...) -> None: ...
    ARCHIVE_UID_FIELD_NUMBER: _ClassVar[int]
    LEGAL_HOLD_ACTION_FIELD_NUMBER: _ClassVar[int]
    ENTITY_LEGAL_HOLD_MAP_FIELD_NUMBER: _ClassVar[int]
    archive_uid: _universal_id_pb2.UniversalIdProto
    legal_hold_action: UpdateLegalHoldArg.LegalHoldAction
    entity_legal_hold_map: _containers.ScalarMap[int, bool]
    def __init__(self, archive_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., legal_hold_action: _Optional[_Union[UpdateLegalHoldArg.LegalHoldAction, str]] = ..., entity_legal_hold_map: _Optional[_Mapping[int, bool]] = ...) -> None: ...

class UpdateLegalHoldResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteArchiveMetadataArg(_message.Message):
    __slots__ = ("archive_uid", "scribe_version")
    ARCHIVE_UID_FIELD_NUMBER: _ClassVar[int]
    SCRIBE_VERSION_FIELD_NUMBER: _ClassVar[int]
    archive_uid: _universal_id_pb2.UniversalIdProto
    scribe_version: int
    def __init__(self, archive_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., scribe_version: _Optional[int] = ...) -> None: ...

class DeleteArchiveMetadataResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class TaskInfo(_message.Message):
    __slots__ = ("job_uid", "task_id", "vault_id", "job_type", "operation_id")
    JOB_UID_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    VAULT_ID_FIELD_NUMBER: _ClassVar[int]
    JOB_TYPE_FIELD_NUMBER: _ClassVar[int]
    OPERATION_ID_FIELD_NUMBER: _ClassVar[int]
    job_uid: _universal_id_pb2.UniversalIdProto
    task_id: int
    vault_id: int
    job_type: _icebox_pb2.IceboxJobType
    operation_id: int
    def __init__(self, job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., task_id: _Optional[int] = ..., vault_id: _Optional[int] = ..., job_type: _Optional[_Union[_icebox_pb2.IceboxJobType, str]] = ..., operation_id: _Optional[int] = ...) -> None: ...

class GetAllowedBandwidthArg(_message.Message):
    __slots__ = ("task_vec", "slave_session_id")
    TASK_VEC_FIELD_NUMBER: _ClassVar[int]
    SLAVE_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    task_vec: _containers.RepeatedCompositeFieldContainer[TaskInfo]
    slave_session_id: int
    def __init__(self, task_vec: _Optional[_Iterable[_Union[TaskInfo, _Mapping]]] = ..., slave_session_id: _Optional[int] = ...) -> None: ...

class BandwidthLimit(_message.Message):
    __slots__ = ("task", "rate_limit_bytes_per_msec")
    TASK_FIELD_NUMBER: _ClassVar[int]
    RATE_LIMIT_BYTES_PER_MSEC_FIELD_NUMBER: _ClassVar[int]
    task: TaskInfo
    rate_limit_bytes_per_msec: int
    def __init__(self, task: _Optional[_Union[TaskInfo, _Mapping]] = ..., rate_limit_bytes_per_msec: _Optional[int] = ...) -> None: ...

class GetAllowedBandwidthResult(_message.Message):
    __slots__ = ("bandwidth_limits_vec", "bandwidth_limits_map_deprecated")
    class BandwidthLimitsMapDeprecatedEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    BANDWIDTH_LIMITS_VEC_FIELD_NUMBER: _ClassVar[int]
    BANDWIDTH_LIMITS_MAP_DEPRECATED_FIELD_NUMBER: _ClassVar[int]
    bandwidth_limits_vec: _containers.RepeatedCompositeFieldContainer[BandwidthLimit]
    bandwidth_limits_map_deprecated: _containers.ScalarMap[str, int]
    def __init__(self, bandwidth_limits_vec: _Optional[_Iterable[_Union[BandwidthLimit, _Mapping]]] = ..., bandwidth_limits_map_deprecated: _Optional[_Mapping[str, int]] = ...) -> None: ...

class CleanupDirectArchiveObjectsArg(_message.Message):
    __slots__ = ("da_gc_job_uid", "relative_dir_path_vec", "error")
    DA_GC_JOB_UID_FIELD_NUMBER: _ClassVar[int]
    RELATIVE_DIR_PATH_VEC_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    da_gc_job_uid: _universal_id_pb2.UniversalIdProto
    relative_dir_path_vec: _containers.RepeatedScalarFieldContainer[str]
    error: _error_pb2.ErrorProto
    def __init__(self, da_gc_job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., relative_dir_path_vec: _Optional[_Iterable[str]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class CleanupDirectArchiveObjectsResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ReportNodeConnectivityArg(_message.Message):
    __slots__ = ("node_id", "constituent_id", "vault_connection_info_vec")
    class VaultConnectionInfo(_message.Message):
        __slots__ = ("vault_id", "timestamp_usecs", "error")
        VAULT_ID_FIELD_NUMBER: _ClassVar[int]
        TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        vault_id: int
        timestamp_usecs: int
        error: _error_pb2.ErrorProto
        def __init__(self, vault_id: _Optional[int] = ..., timestamp_usecs: _Optional[int] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    CONSTITUENT_ID_FIELD_NUMBER: _ClassVar[int]
    VAULT_CONNECTION_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    node_id: int
    constituent_id: int
    vault_connection_info_vec: _containers.RepeatedCompositeFieldContainer[ReportNodeConnectivityArg.VaultConnectionInfo]
    def __init__(self, node_id: _Optional[int] = ..., constituent_id: _Optional[int] = ..., vault_connection_info_vec: _Optional[_Iterable[_Union[ReportNodeConnectivityArg.VaultConnectionInfo, _Mapping]]] = ...) -> None: ...

class ReportNodeConnectivityResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetOrCreateCloudDomainArg(_message.Message):
    __slots__ = ("vault_id", "view_box_id", "viewbox_name")
    VAULT_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
    VIEWBOX_NAME_FIELD_NUMBER: _ClassVar[int]
    vault_id: int
    view_box_id: int
    viewbox_name: str
    def __init__(self, vault_id: _Optional[int] = ..., view_box_id: _Optional[int] = ..., viewbox_name: _Optional[str] = ...) -> None: ...

class GetOrCreateCloudDomainResult(_message.Message):
    __slots__ = ("error", "cloud_domain_id", "view_box_id")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    CLOUD_DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    cloud_domain_id: int
    view_box_id: int
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., cloud_domain_id: _Optional[int] = ..., view_box_id: _Optional[int] = ...) -> None: ...

class DeleteCloudDomainArg(_message.Message):
    __slots__ = ("cloud_domain_id",)
    CLOUD_DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    cloud_domain_id: int
    def __init__(self, cloud_domain_id: _Optional[int] = ...) -> None: ...

class DeleteCloudDomainResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class GetEpochIdsArg(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class EpochIdInfo(_message.Message):
    __slots__ = ("domain_id", "app_job_uid", "vault_id", "epoch_id")
    DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    APP_JOB_UID_FIELD_NUMBER: _ClassVar[int]
    VAULT_ID_FIELD_NUMBER: _ClassVar[int]
    EPOCH_ID_FIELD_NUMBER: _ClassVar[int]
    domain_id: int
    app_job_uid: _universal_id_pb2.UniversalIdProto
    vault_id: int
    epoch_id: int
    def __init__(self, domain_id: _Optional[int] = ..., app_job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., vault_id: _Optional[int] = ..., epoch_id: _Optional[int] = ...) -> None: ...

class GetEpochIdsResult(_message.Message):
    __slots__ = ("error", "epoch_id_info_vec")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    EPOCH_ID_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    epoch_id_info_vec: _containers.RepeatedCompositeFieldContainer[EpochIdInfo]
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., epoch_id_info_vec: _Optional[_Iterable[_Union[EpochIdInfo, _Mapping]]] = ...) -> None: ...

class QueryAppJobsInfoArg(_message.Message):
    __slots__ = ("app_job_vault_vec",)
    class AppJobVaultIdentifier(_message.Message):
        __slots__ = ("app_job_uid", "vault_id")
        APP_JOB_UID_FIELD_NUMBER: _ClassVar[int]
        VAULT_ID_FIELD_NUMBER: _ClassVar[int]
        app_job_uid: _universal_id_pb2.UniversalIdProto
        vault_id: int
        def __init__(self, app_job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., vault_id: _Optional[int] = ...) -> None: ...
    APP_JOB_VAULT_VEC_FIELD_NUMBER: _ClassVar[int]
    app_job_vault_vec: _containers.RepeatedCompositeFieldContainer[QueryAppJobsInfoArg.AppJobVaultIdentifier]
    def __init__(self, app_job_vault_vec: _Optional[_Iterable[_Union[QueryAppJobsInfoArg.AppJobVaultIdentifier, _Mapping]]] = ...) -> None: ...

class QueryAppJobsInfoResult(_message.Message):
    __slots__ = ("app_job_info_vec",)
    class AppJobInfoProto(_message.Message):
        __slots__ = ("app_job_uid", "vault_id", "latest_archive_uid", "last_attempted_archive_uid", "last_attempted_archive_status", "latest_archive_now_archive_uid", "forced_full_archive_for_nfoi", "last_da_gc_job_completion_time_usecs", "is_marked_for_removal", "forced_full_for_missing_files_report_mode", "forced_full_for_missing_files_repair_mode")
        APP_JOB_UID_FIELD_NUMBER: _ClassVar[int]
        VAULT_ID_FIELD_NUMBER: _ClassVar[int]
        LATEST_ARCHIVE_UID_FIELD_NUMBER: _ClassVar[int]
        LAST_ATTEMPTED_ARCHIVE_UID_FIELD_NUMBER: _ClassVar[int]
        LAST_ATTEMPTED_ARCHIVE_STATUS_FIELD_NUMBER: _ClassVar[int]
        LATEST_ARCHIVE_NOW_ARCHIVE_UID_FIELD_NUMBER: _ClassVar[int]
        FORCED_FULL_ARCHIVE_FOR_NFOI_FIELD_NUMBER: _ClassVar[int]
        LAST_DA_GC_JOB_COMPLETION_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
        IS_MARKED_FOR_REMOVAL_FIELD_NUMBER: _ClassVar[int]
        FORCED_FULL_FOR_MISSING_FILES_REPORT_MODE_FIELD_NUMBER: _ClassVar[int]
        FORCED_FULL_FOR_MISSING_FILES_REPAIR_MODE_FIELD_NUMBER: _ClassVar[int]
        app_job_uid: _universal_id_pb2.UniversalIdProto
        vault_id: int
        latest_archive_uid: _universal_id_pb2.UniversalIdProto
        last_attempted_archive_uid: _universal_id_pb2.UniversalIdProto
        last_attempted_archive_status: _icebox_pb2.IceboxJobStatus
        latest_archive_now_archive_uid: _universal_id_pb2.UniversalIdProto
        forced_full_archive_for_nfoi: bool
        last_da_gc_job_completion_time_usecs: int
        is_marked_for_removal: bool
        forced_full_for_missing_files_report_mode: bool
        forced_full_for_missing_files_repair_mode: bool
        def __init__(self, app_job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., vault_id: _Optional[int] = ..., latest_archive_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., last_attempted_archive_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., last_attempted_archive_status: _Optional[_Union[_icebox_pb2.IceboxJobStatus, str]] = ..., latest_archive_now_archive_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., forced_full_archive_for_nfoi: bool = ..., last_da_gc_job_completion_time_usecs: _Optional[int] = ..., is_marked_for_removal: bool = ..., forced_full_for_missing_files_report_mode: bool = ..., forced_full_for_missing_files_repair_mode: bool = ...) -> None: ...
    APP_JOB_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    app_job_info_vec: _containers.RepeatedCompositeFieldContainer[QueryAppJobsInfoResult.AppJobInfoProto]
    def __init__(self, app_job_info_vec: _Optional[_Iterable[_Union[QueryAppJobsInfoResult.AppJobInfoProto, _Mapping]]] = ...) -> None: ...

class GetJobGCStateArg(_message.Message):
    __slots__ = ("archive_uid_vec",)
    ARCHIVE_UID_VEC_FIELD_NUMBER: _ClassVar[int]
    archive_uid_vec: _containers.RepeatedCompositeFieldContainer[_universal_id_pb2.UniversalIdProto]
    def __init__(self, archive_uid_vec: _Optional[_Iterable[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]]] = ...) -> None: ...

class GetJobGCStateResult(_message.Message):
    __slots__ = ("job_gc_state_vec",)
    class JobGCStateProto(_message.Message):
        __slots__ = ("archive_uid", "job_uid", "vault_id", "expiry_timestamp_usecs", "app_job_uid", "start_timestamp_usecs", "end_timestamp_usecs", "job_status", "removal_state", "error", "logical_size_bytes", "physical_size_bytes", "data_removal_state", "is_data_removed", "data_removal_timestamp_usecs", "archive_worm_stats")
        ARCHIVE_UID_FIELD_NUMBER: _ClassVar[int]
        JOB_UID_FIELD_NUMBER: _ClassVar[int]
        VAULT_ID_FIELD_NUMBER: _ClassVar[int]
        EXPIRY_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
        APP_JOB_UID_FIELD_NUMBER: _ClassVar[int]
        START_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
        END_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
        JOB_STATUS_FIELD_NUMBER: _ClassVar[int]
        REMOVAL_STATE_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        LOGICAL_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
        PHYSICAL_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
        DATA_REMOVAL_STATE_FIELD_NUMBER: _ClassVar[int]
        IS_DATA_REMOVED_FIELD_NUMBER: _ClassVar[int]
        DATA_REMOVAL_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
        ARCHIVE_WORM_STATS_FIELD_NUMBER: _ClassVar[int]
        archive_uid: _universal_id_pb2.UniversalIdProto
        job_uid: _universal_id_pb2.UniversalIdProto
        vault_id: int
        expiry_timestamp_usecs: int
        app_job_uid: _universal_id_pb2.UniversalIdProto
        start_timestamp_usecs: int
        end_timestamp_usecs: int
        job_status: _icebox_pb2.IceboxJobStatus
        removal_state: _cluster_config_pb2.ClusterConfigProto.RemovalState
        error: _error_pb2.ErrorProto
        logical_size_bytes: int
        physical_size_bytes: int
        data_removal_state: _cluster_config_pb2.ClusterConfigProto.RemovalState
        is_data_removed: bool
        data_removal_timestamp_usecs: int
        archive_worm_stats: _icebox_pb2.ArchiveWORMStats
        def __init__(self, archive_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., vault_id: _Optional[int] = ..., expiry_timestamp_usecs: _Optional[int] = ..., app_job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., start_timestamp_usecs: _Optional[int] = ..., end_timestamp_usecs: _Optional[int] = ..., job_status: _Optional[_Union[_icebox_pb2.IceboxJobStatus, str]] = ..., removal_state: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.RemovalState, _Mapping]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., logical_size_bytes: _Optional[int] = ..., physical_size_bytes: _Optional[int] = ..., data_removal_state: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.RemovalState, _Mapping]] = ..., is_data_removed: bool = ..., data_removal_timestamp_usecs: _Optional[int] = ..., archive_worm_stats: _Optional[_Union[_icebox_pb2.ArchiveWORMStats, _Mapping]] = ...) -> None: ...
    JOB_GC_STATE_VEC_FIELD_NUMBER: _ClassVar[int]
    job_gc_state_vec: _containers.RepeatedCompositeFieldContainer[GetJobGCStateResult.JobGCStateProto]
    def __init__(self, job_gc_state_vec: _Optional[_Iterable[_Union[GetJobGCStateResult.JobGCStateProto, _Mapping]]] = ...) -> None: ...

class FetchUptierDataSizeArg(_message.Message):
    __slots__ = ("archive_uid",)
    ARCHIVE_UID_FIELD_NUMBER: _ClassVar[int]
    archive_uid: _universal_id_pb2.UniversalIdProto
    def __init__(self, archive_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ...) -> None: ...

class FetchUptierDataSizeResult(_message.Message):
    __slots__ = ("error", "data_size_bytes")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    DATA_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    data_size_bytes: int
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., data_size_bytes: _Optional[int] = ...) -> None: ...

class UpdateIceboxUsageStatsArg(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UpdateIceboxUsageStatsResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class CheckGflagSettingsArg(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CheckGflagSettingsResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...
