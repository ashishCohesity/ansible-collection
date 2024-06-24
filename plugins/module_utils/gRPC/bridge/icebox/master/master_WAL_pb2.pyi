from bridge.base import error_pb2 as _error_pb2
from bridge.icebox.base import icebox_pb2 as _icebox_pb2
from bridge.icebox.master.stub import rpc_service_pb2 as _rpc_service_pb2
from bridge.vault.base import vault_pb2 as _vault_pb2
from bridge.vault.base import worm_pb2 as _worm_pb2
from configs import cluster_config_pb2 as _cluster_config_pb2
from magneto.api import worm_pb2 as _worm_pb2_1
from magneto.base import permissions_pb2 as _permissions_pb2
from util.base import op_clock_pb2 as _op_clock_pb2
from util.base import universal_id_pb2 as _universal_id_pb2
from magneto.directory_walker import directory_walker_pb2 as _directory_walker_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ConstituentInfoProto(_message.Message):
    __slots__ = ("constituent_id", "node_id", "session_id", "unavailable_timestamp_usecs")
    CONSTITUENT_ID_FIELD_NUMBER: _ClassVar[int]
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    UNAVAILABLE_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
    constituent_id: int
    node_id: int
    session_id: int
    unavailable_timestamp_usecs: int
    def __init__(self, constituent_id: _Optional[int] = ..., node_id: _Optional[int] = ..., session_id: _Optional[int] = ..., unavailable_timestamp_usecs: _Optional[int] = ...) -> None: ...

class BlobStateProto(_message.Message):
    __slots__ = ("inode_id", "task_id_vec", "all_data_tasks_created", "snap_tree_task_created")
    INODE_ID_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    ALL_DATA_TASKS_CREATED_FIELD_NUMBER: _ClassVar[int]
    SNAP_TREE_TASK_CREATED_FIELD_NUMBER: _ClassVar[int]
    inode_id: int
    task_id_vec: _containers.RepeatedScalarFieldContainer[int]
    all_data_tasks_created: bool
    snap_tree_task_created: bool
    def __init__(self, inode_id: _Optional[int] = ..., task_id_vec: _Optional[_Iterable[int]] = ..., all_data_tasks_created: bool = ..., snap_tree_task_created: bool = ...) -> None: ...

class ViewSnapTreeStateProto(_message.Message):
    __slots__ = ("tree_uid", "root_inode_id", "fs_name", "tree_type", "state", "view_snap_tree_iter_cookie", "blob_info_cookie", "blob_state_vec", "all_blob_archival_tasks_created", "archiving_blobs_context", "blob_archival_task_id_vec", "view_id", "prev_archive_node_id_floor", "entity_id", "fixing_update_intents_context", "fixing_update_intents_enabled", "upload_files_context", "direct_archive_fs_context", "marked_snap_tree_as_immutable", "is_s3_view_snap_tree", "total_num_leaf_nodes_to_be_archived", "total_logical_size_to_be_archived", "sha256_summary_checksum")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kCreated: _ClassVar[ViewSnapTreeStateProto.State]
        kCreatingInternalFiles: _ClassVar[ViewSnapTreeStateProto.State]
        kArchivingBlobs: _ClassVar[ViewSnapTreeStateProto.State]
        kFinished: _ClassVar[ViewSnapTreeStateProto.State]
        kFailed: _ClassVar[ViewSnapTreeStateProto.State]
        kCanceled: _ClassVar[ViewSnapTreeStateProto.State]
        kFixingUpdateIntents: _ClassVar[ViewSnapTreeStateProto.State]
        kUploadingFiles: _ClassVar[ViewSnapTreeStateProto.State]
        kArchivingDirectArchiveBlobs: _ClassVar[ViewSnapTreeStateProto.State]
        kFixingDirectArchiveFsUpdateIntents: _ClassVar[ViewSnapTreeStateProto.State]
        kCloudDomainFixingUpdateIntents: _ClassVar[ViewSnapTreeStateProto.State]
        kCloudDomainArchivingTree: _ClassVar[ViewSnapTreeStateProto.State]
        kCohesionFixingUpdateIntents: _ClassVar[ViewSnapTreeStateProto.State]
        kCopyingCohesionData: _ClassVar[ViewSnapTreeStateProto.State]
    kCreated: ViewSnapTreeStateProto.State
    kCreatingInternalFiles: ViewSnapTreeStateProto.State
    kArchivingBlobs: ViewSnapTreeStateProto.State
    kFinished: ViewSnapTreeStateProto.State
    kFailed: ViewSnapTreeStateProto.State
    kCanceled: ViewSnapTreeStateProto.State
    kFixingUpdateIntents: ViewSnapTreeStateProto.State
    kUploadingFiles: ViewSnapTreeStateProto.State
    kArchivingDirectArchiveBlobs: ViewSnapTreeStateProto.State
    kFixingDirectArchiveFsUpdateIntents: ViewSnapTreeStateProto.State
    kCloudDomainFixingUpdateIntents: ViewSnapTreeStateProto.State
    kCloudDomainArchivingTree: ViewSnapTreeStateProto.State
    kCohesionFixingUpdateIntents: ViewSnapTreeStateProto.State
    kCopyingCohesionData: ViewSnapTreeStateProto.State
    class ArchivingBlobsContextProto(_message.Message):
        __slots__ = ("key_range_info_vec", "blob_info_list_vec")
        class KeyRangeInfo(_message.Message):
            __slots__ = ("min_key", "max_key", "snap_tree_iter_cookie", "blob_info_cookie", "is_range_processed")
            MIN_KEY_FIELD_NUMBER: _ClassVar[int]
            MAX_KEY_FIELD_NUMBER: _ClassVar[int]
            SNAP_TREE_ITER_COOKIE_FIELD_NUMBER: _ClassVar[int]
            BLOB_INFO_COOKIE_FIELD_NUMBER: _ClassVar[int]
            IS_RANGE_PROCESSED_FIELD_NUMBER: _ClassVar[int]
            min_key: int
            max_key: int
            snap_tree_iter_cookie: _icebox_pb2.SnapTreeIterCookieProto
            blob_info_cookie: _icebox_pb2.BlobInfo
            is_range_processed: bool
            def __init__(self, min_key: _Optional[int] = ..., max_key: _Optional[int] = ..., snap_tree_iter_cookie: _Optional[_Union[_icebox_pb2.SnapTreeIterCookieProto, _Mapping]] = ..., blob_info_cookie: _Optional[_Union[_icebox_pb2.BlobInfo, _Mapping]] = ..., is_range_processed: bool = ...) -> None: ...
        class BlobInfoList(_message.Message):
            __slots__ = ("blob_info_vec", "task_size_bytes")
            BLOB_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
            TASK_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
            blob_info_vec: _containers.RepeatedCompositeFieldContainer[_icebox_pb2.BlobInfo]
            task_size_bytes: int
            def __init__(self, blob_info_vec: _Optional[_Iterable[_Union[_icebox_pb2.BlobInfo, _Mapping]]] = ..., task_size_bytes: _Optional[int] = ...) -> None: ...
        KEY_RANGE_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
        BLOB_INFO_LIST_VEC_FIELD_NUMBER: _ClassVar[int]
        key_range_info_vec: _containers.RepeatedCompositeFieldContainer[ViewSnapTreeStateProto.ArchivingBlobsContextProto.KeyRangeInfo]
        blob_info_list_vec: _containers.RepeatedCompositeFieldContainer[ViewSnapTreeStateProto.ArchivingBlobsContextProto.BlobInfoList]
        def __init__(self, key_range_info_vec: _Optional[_Iterable[_Union[ViewSnapTreeStateProto.ArchivingBlobsContextProto.KeyRangeInfo, _Mapping]]] = ..., blob_info_list_vec: _Optional[_Iterable[_Union[ViewSnapTreeStateProto.ArchivingBlobsContextProto.BlobInfoList, _Mapping]]] = ...) -> None: ...
    class FixingUpdateIntentsContextProto(_message.Message):
        __slots__ = ("keys", "prev_key")
        KEYS_FIELD_NUMBER: _ClassVar[int]
        PREV_KEY_FIELD_NUMBER: _ClassVar[int]
        keys: _containers.RepeatedScalarFieldContainer[int]
        prev_key: int
        def __init__(self, keys: _Optional[_Iterable[int]] = ..., prev_key: _Optional[int] = ...) -> None: ...
    class UploadFilesContext(_message.Message):
        __slots__ = ("file_info_vec", "cookie", "fs_scanned", "fs_checkpoint_info", "prev_job_run_fs_checkpoint_info", "stats")
        FILE_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
        COOKIE_FIELD_NUMBER: _ClassVar[int]
        FS_SCANNED_FIELD_NUMBER: _ClassVar[int]
        FS_CHECKPOINT_INFO_FIELD_NUMBER: _ClassVar[int]
        PREV_JOB_RUN_FS_CHECKPOINT_INFO_FIELD_NUMBER: _ClassVar[int]
        STATS_FIELD_NUMBER: _ClassVar[int]
        file_info_vec: _containers.RepeatedCompositeFieldContainer[_icebox_pb2.FileInfoProto]
        cookie: _icebox_pb2.GetFilesToUploadCookieProto
        fs_scanned: bool
        fs_checkpoint_info: _icebox_pb2.FileUploadJobMetadataProto.FSCheckpointInfo
        prev_job_run_fs_checkpoint_info: _icebox_pb2.FileUploadJobMetadataProto.FSCheckpointInfo
        stats: _icebox_pb2.FileUploadJobStats
        def __init__(self, file_info_vec: _Optional[_Iterable[_Union[_icebox_pb2.FileInfoProto, _Mapping]]] = ..., cookie: _Optional[_Union[_icebox_pb2.GetFilesToUploadCookieProto, _Mapping]] = ..., fs_scanned: bool = ..., fs_checkpoint_info: _Optional[_Union[_icebox_pb2.FileUploadJobMetadataProto.FSCheckpointInfo, _Mapping]] = ..., prev_job_run_fs_checkpoint_info: _Optional[_Union[_icebox_pb2.FileUploadJobMetadataProto.FSCheckpointInfo, _Mapping]] = ..., stats: _Optional[_Union[_icebox_pb2.FileUploadJobStats, _Mapping]] = ...) -> None: ...
    class DirectArchiveFSContext(_message.Message):
        __slots__ = ("archive_files_req_vec", "received_all_reqs", "archive_files_id_vec")
        ARCHIVE_FILES_REQ_VEC_FIELD_NUMBER: _ClassVar[int]
        RECEIVED_ALL_REQS_FIELD_NUMBER: _ClassVar[int]
        ARCHIVE_FILES_ID_VEC_FIELD_NUMBER: _ClassVar[int]
        archive_files_req_vec: _containers.RepeatedCompositeFieldContainer[_icebox_pb2.ArchiveFilesRequest]
        received_all_reqs: bool
        archive_files_id_vec: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, archive_files_req_vec: _Optional[_Iterable[_Union[_icebox_pb2.ArchiveFilesRequest, _Mapping]]] = ..., received_all_reqs: bool = ..., archive_files_id_vec: _Optional[_Iterable[str]] = ...) -> None: ...
    TREE_UID_FIELD_NUMBER: _ClassVar[int]
    ROOT_INODE_ID_FIELD_NUMBER: _ClassVar[int]
    FS_NAME_FIELD_NUMBER: _ClassVar[int]
    TREE_TYPE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    VIEW_SNAP_TREE_ITER_COOKIE_FIELD_NUMBER: _ClassVar[int]
    BLOB_INFO_COOKIE_FIELD_NUMBER: _ClassVar[int]
    BLOB_STATE_VEC_FIELD_NUMBER: _ClassVar[int]
    ALL_BLOB_ARCHIVAL_TASKS_CREATED_FIELD_NUMBER: _ClassVar[int]
    ARCHIVING_BLOBS_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    BLOB_ARCHIVAL_TASK_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    VIEW_ID_FIELD_NUMBER: _ClassVar[int]
    PREV_ARCHIVE_NODE_ID_FLOOR_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    FIXING_UPDATE_INTENTS_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    FIXING_UPDATE_INTENTS_ENABLED_FIELD_NUMBER: _ClassVar[int]
    UPLOAD_FILES_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    DIRECT_ARCHIVE_FS_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    MARKED_SNAP_TREE_AS_IMMUTABLE_FIELD_NUMBER: _ClassVar[int]
    IS_S3_VIEW_SNAP_TREE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_NUM_LEAF_NODES_TO_BE_ARCHIVED_FIELD_NUMBER: _ClassVar[int]
    TOTAL_LOGICAL_SIZE_TO_BE_ARCHIVED_FIELD_NUMBER: _ClassVar[int]
    SHA256_SUMMARY_CHECKSUM_FIELD_NUMBER: _ClassVar[int]
    tree_uid: _universal_id_pb2.UniversalIdProto
    root_inode_id: int
    fs_name: str
    tree_type: _icebox_pb2.IceboxSnapTreeType
    state: ViewSnapTreeStateProto.State
    view_snap_tree_iter_cookie: _icebox_pb2.SnapTreeIterCookieProto
    blob_info_cookie: _icebox_pb2.BlobInfo
    blob_state_vec: _containers.RepeatedCompositeFieldContainer[BlobStateProto]
    all_blob_archival_tasks_created: bool
    archiving_blobs_context: ViewSnapTreeStateProto.ArchivingBlobsContextProto
    blob_archival_task_id_vec: _containers.RepeatedScalarFieldContainer[int]
    view_id: int
    prev_archive_node_id_floor: int
    entity_id: int
    fixing_update_intents_context: ViewSnapTreeStateProto.FixingUpdateIntentsContextProto
    fixing_update_intents_enabled: bool
    upload_files_context: ViewSnapTreeStateProto.UploadFilesContext
    direct_archive_fs_context: ViewSnapTreeStateProto.DirectArchiveFSContext
    marked_snap_tree_as_immutable: bool
    is_s3_view_snap_tree: bool
    total_num_leaf_nodes_to_be_archived: int
    total_logical_size_to_be_archived: int
    sha256_summary_checksum: bytes
    def __init__(self, tree_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., root_inode_id: _Optional[int] = ..., fs_name: _Optional[str] = ..., tree_type: _Optional[_Union[_icebox_pb2.IceboxSnapTreeType, str]] = ..., state: _Optional[_Union[ViewSnapTreeStateProto.State, str]] = ..., view_snap_tree_iter_cookie: _Optional[_Union[_icebox_pb2.SnapTreeIterCookieProto, _Mapping]] = ..., blob_info_cookie: _Optional[_Union[_icebox_pb2.BlobInfo, _Mapping]] = ..., blob_state_vec: _Optional[_Iterable[_Union[BlobStateProto, _Mapping]]] = ..., all_blob_archival_tasks_created: bool = ..., archiving_blobs_context: _Optional[_Union[ViewSnapTreeStateProto.ArchivingBlobsContextProto, _Mapping]] = ..., blob_archival_task_id_vec: _Optional[_Iterable[int]] = ..., view_id: _Optional[int] = ..., prev_archive_node_id_floor: _Optional[int] = ..., entity_id: _Optional[int] = ..., fixing_update_intents_context: _Optional[_Union[ViewSnapTreeStateProto.FixingUpdateIntentsContextProto, _Mapping]] = ..., fixing_update_intents_enabled: bool = ..., upload_files_context: _Optional[_Union[ViewSnapTreeStateProto.UploadFilesContext, _Mapping]] = ..., direct_archive_fs_context: _Optional[_Union[ViewSnapTreeStateProto.DirectArchiveFSContext, _Mapping]] = ..., marked_snap_tree_as_immutable: bool = ..., is_s3_view_snap_tree: bool = ..., total_num_leaf_nodes_to_be_archived: _Optional[int] = ..., total_logical_size_to_be_archived: _Optional[int] = ..., sha256_summary_checksum: _Optional[bytes] = ...) -> None: ...

class SearchJobStats(_message.Message):
    __slots__ = ("num_objects_found", "num_ignored_objects", "num_archive_metadata_objects", "num_restorable_archives", "num_failed_objects", "num_decryption_key_unavailable_objects", "num_app_jobs", "num_clusters")
    NUM_OBJECTS_FOUND_FIELD_NUMBER: _ClassVar[int]
    NUM_IGNORED_OBJECTS_FIELD_NUMBER: _ClassVar[int]
    NUM_ARCHIVE_METADATA_OBJECTS_FIELD_NUMBER: _ClassVar[int]
    NUM_RESTORABLE_ARCHIVES_FIELD_NUMBER: _ClassVar[int]
    NUM_FAILED_OBJECTS_FIELD_NUMBER: _ClassVar[int]
    NUM_DECRYPTION_KEY_UNAVAILABLE_OBJECTS_FIELD_NUMBER: _ClassVar[int]
    NUM_APP_JOBS_FIELD_NUMBER: _ClassVar[int]
    NUM_CLUSTERS_FIELD_NUMBER: _ClassVar[int]
    num_objects_found: int
    num_ignored_objects: int
    num_archive_metadata_objects: int
    num_restorable_archives: int
    num_failed_objects: int
    num_decryption_key_unavailable_objects: int
    num_app_jobs: int
    num_clusters: int
    def __init__(self, num_objects_found: _Optional[int] = ..., num_ignored_objects: _Optional[int] = ..., num_archive_metadata_objects: _Optional[int] = ..., num_restorable_archives: _Optional[int] = ..., num_failed_objects: _Optional[int] = ..., num_decryption_key_unavailable_objects: _Optional[int] = ..., num_app_jobs: _Optional[int] = ..., num_clusters: _Optional[int] = ...) -> None: ...

class DomainMigrationJobContextProto(_message.Message):
    __slots__ = ("migration_uid", "vault_id", "user_info", "cloud_domain_config_file", "cloud_domain_details", "cloud_domain_id", "read_pending_archive_metadata_object_vec", "cookie", "vault_scanned", "stats", "prefix", "initiated_restore_jobs", "completed_restore_jobs", "apollo_actions_complete", "list_archive_metadata_issued")
    MIGRATION_UID_FIELD_NUMBER: _ClassVar[int]
    VAULT_ID_FIELD_NUMBER: _ClassVar[int]
    USER_INFO_FIELD_NUMBER: _ClassVar[int]
    CLOUD_DOMAIN_CONFIG_FILE_FIELD_NUMBER: _ClassVar[int]
    CLOUD_DOMAIN_DETAILS_FIELD_NUMBER: _ClassVar[int]
    CLOUD_DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    READ_PENDING_ARCHIVE_METADATA_OBJECT_VEC_FIELD_NUMBER: _ClassVar[int]
    COOKIE_FIELD_NUMBER: _ClassVar[int]
    VAULT_SCANNED_FIELD_NUMBER: _ClassVar[int]
    STATS_FIELD_NUMBER: _ClassVar[int]
    PREFIX_FIELD_NUMBER: _ClassVar[int]
    INITIATED_RESTORE_JOBS_FIELD_NUMBER: _ClassVar[int]
    COMPLETED_RESTORE_JOBS_FIELD_NUMBER: _ClassVar[int]
    APOLLO_ACTIONS_COMPLETE_FIELD_NUMBER: _ClassVar[int]
    LIST_ARCHIVE_METADATA_ISSUED_FIELD_NUMBER: _ClassVar[int]
    migration_uid: str
    vault_id: int
    user_info: _permissions_pb2.UserInformation
    cloud_domain_config_file: str
    cloud_domain_details: _icebox_pb2.CloudDomainAccessInfo
    cloud_domain_id: int
    read_pending_archive_metadata_object_vec: _containers.RepeatedCompositeFieldContainer[_icebox_pb2.ObjectInfoProto]
    cookie: str
    vault_scanned: bool
    stats: SearchJobStats
    prefix: str
    initiated_restore_jobs: _containers.RepeatedCompositeFieldContainer[_universal_id_pb2.UniversalIdProto]
    completed_restore_jobs: _containers.RepeatedCompositeFieldContainer[_universal_id_pb2.UniversalIdProto]
    apollo_actions_complete: bool
    list_archive_metadata_issued: bool
    def __init__(self, migration_uid: _Optional[str] = ..., vault_id: _Optional[int] = ..., user_info: _Optional[_Union[_permissions_pb2.UserInformation, _Mapping]] = ..., cloud_domain_config_file: _Optional[str] = ..., cloud_domain_details: _Optional[_Union[_icebox_pb2.CloudDomainAccessInfo, _Mapping]] = ..., cloud_domain_id: _Optional[int] = ..., read_pending_archive_metadata_object_vec: _Optional[_Iterable[_Union[_icebox_pb2.ObjectInfoProto, _Mapping]]] = ..., cookie: _Optional[str] = ..., vault_scanned: bool = ..., stats: _Optional[_Union[SearchJobStats, _Mapping]] = ..., prefix: _Optional[str] = ..., initiated_restore_jobs: _Optional[_Iterable[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]]] = ..., completed_restore_jobs: _Optional[_Iterable[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]]] = ..., apollo_actions_complete: bool = ..., list_archive_metadata_issued: bool = ...) -> None: ...

class CloudDomainRebuildJobContextProto(_message.Message):
    __slots__ = ("object_type", "cloud_domain_id", "max_objects_per_list_request", "prefix", "read_pending_object_info_vec", "cookie", "vault_scanned", "stats")
    OBJECT_TYPE_FIELD_NUMBER: _ClassVar[int]
    CLOUD_DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    MAX_OBJECTS_PER_LIST_REQUEST_FIELD_NUMBER: _ClassVar[int]
    PREFIX_FIELD_NUMBER: _ClassVar[int]
    READ_PENDING_OBJECT_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    COOKIE_FIELD_NUMBER: _ClassVar[int]
    VAULT_SCANNED_FIELD_NUMBER: _ClassVar[int]
    STATS_FIELD_NUMBER: _ClassVar[int]
    object_type: _rpc_service_pb2.ScheduleCloudDomainRebuildJobArg.ObjectType
    cloud_domain_id: int
    max_objects_per_list_request: int
    prefix: str
    read_pending_object_info_vec: _containers.RepeatedCompositeFieldContainer[_icebox_pb2.ObjectInfoProto]
    cookie: str
    vault_scanned: bool
    stats: SearchJobStats
    def __init__(self, object_type: _Optional[_Union[_rpc_service_pb2.ScheduleCloudDomainRebuildJobArg.ObjectType, str]] = ..., cloud_domain_id: _Optional[int] = ..., max_objects_per_list_request: _Optional[int] = ..., prefix: _Optional[str] = ..., read_pending_object_info_vec: _Optional[_Iterable[_Union[_icebox_pb2.ObjectInfoProto, _Mapping]]] = ..., cookie: _Optional[str] = ..., vault_scanned: bool = ..., stats: _Optional[_Union[SearchJobStats, _Mapping]] = ...) -> None: ...

class SearchJobContextProto(_message.Message):
    __slots__ = ("search_params", "key_info", "read_pending_object_info_vec", "read_pending_unknown_object_info_vec", "cookie", "vault_scanned", "stats", "max_objects_per_list_request", "list_metadata_objects_only", "cloud_domain_config_file_vec", "cloud_domain_cookie", "accessible_cloud_domains", "remaining_accessible_cloud_domains", "cloud_domain_archive_metadata_objects", "vault_scanned_for_new_format_objects", "is_fortknox_vault")
    class CloudDomainArchiveMetadataObjects(_message.Message):
        __slots__ = ("cloud_domain_config_file", "read_pending_archive_metadata_object_vec", "cookie", "domain_prefix", "is_vault_encryption", "use_uploaded_key", "dek_uid")
        CLOUD_DOMAIN_CONFIG_FILE_FIELD_NUMBER: _ClassVar[int]
        READ_PENDING_ARCHIVE_METADATA_OBJECT_VEC_FIELD_NUMBER: _ClassVar[int]
        COOKIE_FIELD_NUMBER: _ClassVar[int]
        DOMAIN_PREFIX_FIELD_NUMBER: _ClassVar[int]
        IS_VAULT_ENCRYPTION_FIELD_NUMBER: _ClassVar[int]
        USE_UPLOADED_KEY_FIELD_NUMBER: _ClassVar[int]
        DEK_UID_FIELD_NUMBER: _ClassVar[int]
        cloud_domain_config_file: str
        read_pending_archive_metadata_object_vec: _containers.RepeatedCompositeFieldContainer[_icebox_pb2.ObjectInfoProto]
        cookie: str
        domain_prefix: str
        is_vault_encryption: bool
        use_uploaded_key: bool
        dek_uid: _universal_id_pb2.UniversalIdProto
        def __init__(self, cloud_domain_config_file: _Optional[str] = ..., read_pending_archive_metadata_object_vec: _Optional[_Iterable[_Union[_icebox_pb2.ObjectInfoProto, _Mapping]]] = ..., cookie: _Optional[str] = ..., domain_prefix: _Optional[str] = ..., is_vault_encryption: bool = ..., use_uploaded_key: bool = ..., dek_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ...) -> None: ...
    SEARCH_PARAMS_FIELD_NUMBER: _ClassVar[int]
    KEY_INFO_FIELD_NUMBER: _ClassVar[int]
    READ_PENDING_OBJECT_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    READ_PENDING_UNKNOWN_OBJECT_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    COOKIE_FIELD_NUMBER: _ClassVar[int]
    VAULT_SCANNED_FIELD_NUMBER: _ClassVar[int]
    STATS_FIELD_NUMBER: _ClassVar[int]
    MAX_OBJECTS_PER_LIST_REQUEST_FIELD_NUMBER: _ClassVar[int]
    LIST_METADATA_OBJECTS_ONLY_FIELD_NUMBER: _ClassVar[int]
    CLOUD_DOMAIN_CONFIG_FILE_VEC_FIELD_NUMBER: _ClassVar[int]
    CLOUD_DOMAIN_COOKIE_FIELD_NUMBER: _ClassVar[int]
    ACCESSIBLE_CLOUD_DOMAINS_FIELD_NUMBER: _ClassVar[int]
    REMAINING_ACCESSIBLE_CLOUD_DOMAINS_FIELD_NUMBER: _ClassVar[int]
    CLOUD_DOMAIN_ARCHIVE_METADATA_OBJECTS_FIELD_NUMBER: _ClassVar[int]
    VAULT_SCANNED_FOR_NEW_FORMAT_OBJECTS_FIELD_NUMBER: _ClassVar[int]
    IS_FORTKNOX_VAULT_FIELD_NUMBER: _ClassVar[int]
    search_params: _icebox_pb2.VaultSearchParams
    key_info: _containers.RepeatedCompositeFieldContainer[_rpc_service_pb2.VaultEncryptionKeyInfoProto]
    read_pending_object_info_vec: _containers.RepeatedCompositeFieldContainer[_icebox_pb2.ObjectInfoProto]
    read_pending_unknown_object_info_vec: _containers.RepeatedCompositeFieldContainer[_icebox_pb2.ObjectInfoProto]
    cookie: str
    vault_scanned: bool
    stats: SearchJobStats
    max_objects_per_list_request: int
    list_metadata_objects_only: bool
    cloud_domain_config_file_vec: _containers.RepeatedScalarFieldContainer[str]
    cloud_domain_cookie: str
    accessible_cloud_domains: _containers.RepeatedCompositeFieldContainer[_icebox_pb2.CloudDomainAccessInfo]
    remaining_accessible_cloud_domains: _containers.RepeatedCompositeFieldContainer[_icebox_pb2.CloudDomainAccessInfo]
    cloud_domain_archive_metadata_objects: _containers.RepeatedCompositeFieldContainer[SearchJobContextProto.CloudDomainArchiveMetadataObjects]
    vault_scanned_for_new_format_objects: bool
    is_fortknox_vault: bool
    def __init__(self, search_params: _Optional[_Union[_icebox_pb2.VaultSearchParams, _Mapping]] = ..., key_info: _Optional[_Iterable[_Union[_rpc_service_pb2.VaultEncryptionKeyInfoProto, _Mapping]]] = ..., read_pending_object_info_vec: _Optional[_Iterable[_Union[_icebox_pb2.ObjectInfoProto, _Mapping]]] = ..., read_pending_unknown_object_info_vec: _Optional[_Iterable[_Union[_icebox_pb2.ObjectInfoProto, _Mapping]]] = ..., cookie: _Optional[str] = ..., vault_scanned: bool = ..., stats: _Optional[_Union[SearchJobStats, _Mapping]] = ..., max_objects_per_list_request: _Optional[int] = ..., list_metadata_objects_only: bool = ..., cloud_domain_config_file_vec: _Optional[_Iterable[str]] = ..., cloud_domain_cookie: _Optional[str] = ..., accessible_cloud_domains: _Optional[_Iterable[_Union[_icebox_pb2.CloudDomainAccessInfo, _Mapping]]] = ..., remaining_accessible_cloud_domains: _Optional[_Iterable[_Union[_icebox_pb2.CloudDomainAccessInfo, _Mapping]]] = ..., cloud_domain_archive_metadata_objects: _Optional[_Iterable[_Union[SearchJobContextProto.CloudDomainArchiveMetadataObjects, _Mapping]]] = ..., vault_scanned_for_new_format_objects: bool = ..., is_fortknox_vault: bool = ...) -> None: ...

class BatchJobContextProto(_message.Message):
    __slots__ = ("restore_index_batch_job_arg",)
    RESTORE_INDEX_BATCH_JOB_ARG_FIELD_NUMBER: _ClassVar[int]
    restore_index_batch_job_arg: _rpc_service_pb2.ScheduleRestoreIndexAndSnapshotJobsArg
    def __init__(self, restore_index_batch_job_arg: _Optional[_Union[_rpc_service_pb2.ScheduleRestoreIndexAndSnapshotJobsArg, _Mapping]] = ...) -> None: ...

class RestoreIndexJobContextProto(_message.Message):
    __slots__ = ("app_job_uid", "search_job_uid", "viewbox_id", "index_time_range", "restore_snapshot_archive_uid", "restore_snapshot_job_uid", "restore_snapshot_job_error", "restore_snapshot_job_scheduled", "index_view_name", "restore_index_archive_uid_vec", "archive_state_vec", "missing_archive_metadata_object_info_vec", "missing_archive_uid_vec", "app_job_name", "cluster_name", "snapshot_progress_monitor_path", "num_indices_to_restore", "num_indices_restored", "prev_processed_archive_state", "local_app_job_uid", "restore_snapshot_expiry_time_usecs", "latest_expiry_time_usecs", "restore_index_stats", "is_direct_archive", "restore_index_job_uid", "restore_index_job_scheduled", "register_app_metadata_task_creation_index", "register_app_metadata_task_completion_index")
    class ArchiveStateProto(_message.Message):
        __slots__ = ("archive_uid", "version", "prev_archive_uid", "state", "done", "source_index_dir_rel_path", "index_dir_rel_path", "error", "download_index_state", "all_tasks_created", "original_error", "is_cloud_domain_format", "restore_index_job_uid", "restore_index_job_scheduled")
        class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kCreated: _ClassVar[RestoreIndexJobContextProto.ArchiveStateProto.State]
            kRegisteringAppJobMetadata: _ClassVar[RestoreIndexJobContextProto.ArchiveStateProto.State]
            kDownloadingIndex: _ClassVar[RestoreIndexJobContextProto.ArchiveStateProto.State]
            kBuildingIndex: _ClassVar[RestoreIndexJobContextProto.ArchiveStateProto.State]
            kPostProcessing: _ClassVar[RestoreIndexJobContextProto.ArchiveStateProto.State]
            kFinished: _ClassVar[RestoreIndexJobContextProto.ArchiveStateProto.State]
            kFailed: _ClassVar[RestoreIndexJobContextProto.ArchiveStateProto.State]
            kCanceled: _ClassVar[RestoreIndexJobContextProto.ArchiveStateProto.State]
        kCreated: RestoreIndexJobContextProto.ArchiveStateProto.State
        kRegisteringAppJobMetadata: RestoreIndexJobContextProto.ArchiveStateProto.State
        kDownloadingIndex: RestoreIndexJobContextProto.ArchiveStateProto.State
        kBuildingIndex: RestoreIndexJobContextProto.ArchiveStateProto.State
        kPostProcessing: RestoreIndexJobContextProto.ArchiveStateProto.State
        kFinished: RestoreIndexJobContextProto.ArchiveStateProto.State
        kFailed: RestoreIndexJobContextProto.ArchiveStateProto.State
        kCanceled: RestoreIndexJobContextProto.ArchiveStateProto.State
        class DownloadIndexState(_message.Message):
            __slots__ = ("num_total_entities_with_index", "num_entities_have_tasks_created", "num_entities_have_tasks_finished", "next_entity_idx")
            NUM_TOTAL_ENTITIES_WITH_INDEX_FIELD_NUMBER: _ClassVar[int]
            NUM_ENTITIES_HAVE_TASKS_CREATED_FIELD_NUMBER: _ClassVar[int]
            NUM_ENTITIES_HAVE_TASKS_FINISHED_FIELD_NUMBER: _ClassVar[int]
            NEXT_ENTITY_IDX_FIELD_NUMBER: _ClassVar[int]
            num_total_entities_with_index: int
            num_entities_have_tasks_created: int
            num_entities_have_tasks_finished: int
            next_entity_idx: int
            def __init__(self, num_total_entities_with_index: _Optional[int] = ..., num_entities_have_tasks_created: _Optional[int] = ..., num_entities_have_tasks_finished: _Optional[int] = ..., next_entity_idx: _Optional[int] = ...) -> None: ...
        ARCHIVE_UID_FIELD_NUMBER: _ClassVar[int]
        VERSION_FIELD_NUMBER: _ClassVar[int]
        PREV_ARCHIVE_UID_FIELD_NUMBER: _ClassVar[int]
        STATE_FIELD_NUMBER: _ClassVar[int]
        DONE_FIELD_NUMBER: _ClassVar[int]
        SOURCE_INDEX_DIR_REL_PATH_FIELD_NUMBER: _ClassVar[int]
        INDEX_DIR_REL_PATH_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        DOWNLOAD_INDEX_STATE_FIELD_NUMBER: _ClassVar[int]
        ALL_TASKS_CREATED_FIELD_NUMBER: _ClassVar[int]
        ORIGINAL_ERROR_FIELD_NUMBER: _ClassVar[int]
        IS_CLOUD_DOMAIN_FORMAT_FIELD_NUMBER: _ClassVar[int]
        RESTORE_INDEX_JOB_UID_FIELD_NUMBER: _ClassVar[int]
        RESTORE_INDEX_JOB_SCHEDULED_FIELD_NUMBER: _ClassVar[int]
        archive_uid: _universal_id_pb2.UniversalIdProto
        version: int
        prev_archive_uid: _universal_id_pb2.UniversalIdProto
        state: RestoreIndexJobContextProto.ArchiveStateProto.State
        done: bool
        source_index_dir_rel_path: str
        index_dir_rel_path: str
        error: _error_pb2.ErrorProto
        download_index_state: RestoreIndexJobContextProto.ArchiveStateProto.DownloadIndexState
        all_tasks_created: bool
        original_error: _error_pb2.ErrorProto
        is_cloud_domain_format: bool
        restore_index_job_uid: _universal_id_pb2.UniversalIdProto
        restore_index_job_scheduled: bool
        def __init__(self, archive_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., version: _Optional[int] = ..., prev_archive_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., state: _Optional[_Union[RestoreIndexJobContextProto.ArchiveStateProto.State, str]] = ..., done: bool = ..., source_index_dir_rel_path: _Optional[str] = ..., index_dir_rel_path: _Optional[str] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., download_index_state: _Optional[_Union[RestoreIndexJobContextProto.ArchiveStateProto.DownloadIndexState, _Mapping]] = ..., all_tasks_created: bool = ..., original_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., is_cloud_domain_format: bool = ..., restore_index_job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., restore_index_job_scheduled: bool = ...) -> None: ...
    APP_JOB_UID_FIELD_NUMBER: _ClassVar[int]
    SEARCH_JOB_UID_FIELD_NUMBER: _ClassVar[int]
    VIEWBOX_ID_FIELD_NUMBER: _ClassVar[int]
    INDEX_TIME_RANGE_FIELD_NUMBER: _ClassVar[int]
    RESTORE_SNAPSHOT_ARCHIVE_UID_FIELD_NUMBER: _ClassVar[int]
    RESTORE_SNAPSHOT_JOB_UID_FIELD_NUMBER: _ClassVar[int]
    RESTORE_SNAPSHOT_JOB_ERROR_FIELD_NUMBER: _ClassVar[int]
    RESTORE_SNAPSHOT_JOB_SCHEDULED_FIELD_NUMBER: _ClassVar[int]
    INDEX_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    RESTORE_INDEX_ARCHIVE_UID_VEC_FIELD_NUMBER: _ClassVar[int]
    ARCHIVE_STATE_VEC_FIELD_NUMBER: _ClassVar[int]
    MISSING_ARCHIVE_METADATA_OBJECT_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    MISSING_ARCHIVE_UID_VEC_FIELD_NUMBER: _ClassVar[int]
    APP_JOB_NAME_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_NAME_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_PROGRESS_MONITOR_PATH_FIELD_NUMBER: _ClassVar[int]
    NUM_INDICES_TO_RESTORE_FIELD_NUMBER: _ClassVar[int]
    NUM_INDICES_RESTORED_FIELD_NUMBER: _ClassVar[int]
    PREV_PROCESSED_ARCHIVE_STATE_FIELD_NUMBER: _ClassVar[int]
    LOCAL_APP_JOB_UID_FIELD_NUMBER: _ClassVar[int]
    RESTORE_SNAPSHOT_EXPIRY_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    LATEST_EXPIRY_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    RESTORE_INDEX_STATS_FIELD_NUMBER: _ClassVar[int]
    IS_DIRECT_ARCHIVE_FIELD_NUMBER: _ClassVar[int]
    RESTORE_INDEX_JOB_UID_FIELD_NUMBER: _ClassVar[int]
    RESTORE_INDEX_JOB_SCHEDULED_FIELD_NUMBER: _ClassVar[int]
    REGISTER_APP_METADATA_TASK_CREATION_INDEX_FIELD_NUMBER: _ClassVar[int]
    REGISTER_APP_METADATA_TASK_COMPLETION_INDEX_FIELD_NUMBER: _ClassVar[int]
    app_job_uid: _universal_id_pb2.UniversalIdProto
    search_job_uid: _universal_id_pb2.UniversalIdProto
    viewbox_id: int
    index_time_range: _icebox_pb2.TimeRange
    restore_snapshot_archive_uid: _universal_id_pb2.UniversalIdProto
    restore_snapshot_job_uid: _universal_id_pb2.UniversalIdProto
    restore_snapshot_job_error: _error_pb2.ErrorProto
    restore_snapshot_job_scheduled: bool
    index_view_name: str
    restore_index_archive_uid_vec: _containers.RepeatedCompositeFieldContainer[_universal_id_pb2.UniversalIdProto]
    archive_state_vec: _containers.RepeatedCompositeFieldContainer[RestoreIndexJobContextProto.ArchiveStateProto]
    missing_archive_metadata_object_info_vec: _containers.RepeatedCompositeFieldContainer[_icebox_pb2.ObjectInfoProto]
    missing_archive_uid_vec: _containers.RepeatedCompositeFieldContainer[_universal_id_pb2.UniversalIdProto]
    app_job_name: str
    cluster_name: str
    snapshot_progress_monitor_path: str
    num_indices_to_restore: int
    num_indices_restored: int
    prev_processed_archive_state: RestoreIndexJobContextProto.ArchiveStateProto
    local_app_job_uid: _universal_id_pb2.UniversalIdProto
    restore_snapshot_expiry_time_usecs: int
    latest_expiry_time_usecs: int
    restore_index_stats: _icebox_pb2.RestoreIndexStats
    is_direct_archive: bool
    restore_index_job_uid: _universal_id_pb2.UniversalIdProto
    restore_index_job_scheduled: bool
    register_app_metadata_task_creation_index: int
    register_app_metadata_task_completion_index: int
    def __init__(self, app_job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., search_job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., viewbox_id: _Optional[int] = ..., index_time_range: _Optional[_Union[_icebox_pb2.TimeRange, _Mapping]] = ..., restore_snapshot_archive_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., restore_snapshot_job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., restore_snapshot_job_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., restore_snapshot_job_scheduled: bool = ..., index_view_name: _Optional[str] = ..., restore_index_archive_uid_vec: _Optional[_Iterable[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]]] = ..., archive_state_vec: _Optional[_Iterable[_Union[RestoreIndexJobContextProto.ArchiveStateProto, _Mapping]]] = ..., missing_archive_metadata_object_info_vec: _Optional[_Iterable[_Union[_icebox_pb2.ObjectInfoProto, _Mapping]]] = ..., missing_archive_uid_vec: _Optional[_Iterable[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]]] = ..., app_job_name: _Optional[str] = ..., cluster_name: _Optional[str] = ..., snapshot_progress_monitor_path: _Optional[str] = ..., num_indices_to_restore: _Optional[int] = ..., num_indices_restored: _Optional[int] = ..., prev_processed_archive_state: _Optional[_Union[RestoreIndexJobContextProto.ArchiveStateProto, _Mapping]] = ..., local_app_job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., restore_snapshot_expiry_time_usecs: _Optional[int] = ..., latest_expiry_time_usecs: _Optional[int] = ..., restore_index_stats: _Optional[_Union[_icebox_pb2.RestoreIndexStats, _Mapping]] = ..., is_direct_archive: bool = ..., restore_index_job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., restore_index_job_scheduled: bool = ..., register_app_metadata_task_creation_index: _Optional[int] = ..., register_app_metadata_task_completion_index: _Optional[int] = ...) -> None: ...

class ReadArchiveMetadataTaskData(_message.Message):
    __slots__ = ("object_info_vec",)
    OBJECT_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    object_info_vec: _containers.RepeatedCompositeFieldContainer[_icebox_pb2.ObjectInfoProto]
    def __init__(self, object_info_vec: _Optional[_Iterable[_Union[_icebox_pb2.ObjectInfoProto, _Mapping]]] = ...) -> None: ...

class ReadArchiveMetadataFromCSRTaskData(_message.Message):
    __slots__ = ("object_info_vec", "domain_prefix", "is_vault_encryption", "use_uploaded_key", "dek_uid")
    OBJECT_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_PREFIX_FIELD_NUMBER: _ClassVar[int]
    IS_VAULT_ENCRYPTION_FIELD_NUMBER: _ClassVar[int]
    USE_UPLOADED_KEY_FIELD_NUMBER: _ClassVar[int]
    DEK_UID_FIELD_NUMBER: _ClassVar[int]
    object_info_vec: _containers.RepeatedCompositeFieldContainer[_icebox_pb2.ObjectInfoProto]
    domain_prefix: str
    is_vault_encryption: bool
    use_uploaded_key: bool
    dek_uid: _universal_id_pb2.UniversalIdProto
    def __init__(self, object_info_vec: _Optional[_Iterable[_Union[_icebox_pb2.ObjectInfoProto, _Mapping]]] = ..., domain_prefix: _Optional[str] = ..., is_vault_encryption: bool = ..., use_uploaded_key: bool = ..., dek_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ...) -> None: ...

class PopulateCloudDomainScribeEntriesTaskData(_message.Message):
    __slots__ = ("object_info_vec",)
    OBJECT_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    object_info_vec: _containers.RepeatedCompositeFieldContainer[_icebox_pb2.ObjectInfoProto]
    def __init__(self, object_info_vec: _Optional[_Iterable[_Union[_icebox_pb2.ObjectInfoProto, _Mapping]]] = ...) -> None: ...

class RestoreJobContext(_message.Message):
    __slots__ = ("found_view_fs", "view_fs_vec", "cookie_view_id", "single_file_restore_entity_id", "parallel_entity_restores_supported", "next_entity_id_to_restore", "all_tasks_created", "parallel_file_restores_supported", "cookie_entity_id", "hydration_duration_usecs", "last_hydration_start_time_usecs", "last_hydration_end_time_usecs", "last_hydration_duration_usecs", "current_view_fs_index")
    class ArchiveObjectRestoreInfo(_message.Message):
        __slots__ = ("archive_object_uid", "object_file_path_vec", "num_data_files", "cookie_object_file_path", "cookie_object_file_offset", "cookie_data_file_index")
        ARCHIVE_OBJECT_UID_FIELD_NUMBER: _ClassVar[int]
        OBJECT_FILE_PATH_VEC_FIELD_NUMBER: _ClassVar[int]
        NUM_DATA_FILES_FIELD_NUMBER: _ClassVar[int]
        COOKIE_OBJECT_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
        COOKIE_OBJECT_FILE_OFFSET_FIELD_NUMBER: _ClassVar[int]
        COOKIE_DATA_FILE_INDEX_FIELD_NUMBER: _ClassVar[int]
        archive_object_uid: _universal_id_pb2.UniversalIdProto
        object_file_path_vec: _containers.RepeatedScalarFieldContainer[str]
        num_data_files: int
        cookie_object_file_path: str
        cookie_object_file_offset: int
        cookie_data_file_index: int
        def __init__(self, archive_object_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., object_file_path_vec: _Optional[_Iterable[str]] = ..., num_data_files: _Optional[int] = ..., cookie_object_file_path: _Optional[str] = ..., cookie_object_file_offset: _Optional[int] = ..., cookie_data_file_index: _Optional[int] = ...) -> None: ...
    class ViewFS(_message.Message):
        __slots__ = ("view_id", "fs_name", "entity_id", "pending_fs_file_vec", "cookie", "fetched_all_files", "is_list_task_active", "parallel_walker_cookie", "archive_object_restore_info_map", "root_dir_path")
        class ArchiveObjectRestoreInfoMapEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: RestoreJobContext.ArchiveObjectRestoreInfo
            def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[RestoreJobContext.ArchiveObjectRestoreInfo, _Mapping]] = ...) -> None: ...
        VIEW_ID_FIELD_NUMBER: _ClassVar[int]
        FS_NAME_FIELD_NUMBER: _ClassVar[int]
        ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
        PENDING_FS_FILE_VEC_FIELD_NUMBER: _ClassVar[int]
        COOKIE_FIELD_NUMBER: _ClassVar[int]
        FETCHED_ALL_FILES_FIELD_NUMBER: _ClassVar[int]
        IS_LIST_TASK_ACTIVE_FIELD_NUMBER: _ClassVar[int]
        PARALLEL_WALKER_COOKIE_FIELD_NUMBER: _ClassVar[int]
        ARCHIVE_OBJECT_RESTORE_INFO_MAP_FIELD_NUMBER: _ClassVar[int]
        ROOT_DIR_PATH_FIELD_NUMBER: _ClassVar[int]
        view_id: int
        fs_name: str
        entity_id: int
        pending_fs_file_vec: _containers.RepeatedCompositeFieldContainer[_icebox_pb2.FSFileProto]
        cookie: str
        fetched_all_files: bool
        is_list_task_active: bool
        parallel_walker_cookie: _icebox_pb2.VaultFSWalkerCookieProto
        archive_object_restore_info_map: _containers.MessageMap[str, RestoreJobContext.ArchiveObjectRestoreInfo]
        root_dir_path: str
        def __init__(self, view_id: _Optional[int] = ..., fs_name: _Optional[str] = ..., entity_id: _Optional[int] = ..., pending_fs_file_vec: _Optional[_Iterable[_Union[_icebox_pb2.FSFileProto, _Mapping]]] = ..., cookie: _Optional[str] = ..., fetched_all_files: bool = ..., is_list_task_active: bool = ..., parallel_walker_cookie: _Optional[_Union[_icebox_pb2.VaultFSWalkerCookieProto, _Mapping]] = ..., archive_object_restore_info_map: _Optional[_Mapping[str, RestoreJobContext.ArchiveObjectRestoreInfo]] = ..., root_dir_path: _Optional[str] = ...) -> None: ...
    FOUND_VIEW_FS_FIELD_NUMBER: _ClassVar[int]
    VIEW_FS_VEC_FIELD_NUMBER: _ClassVar[int]
    COOKIE_VIEW_ID_FIELD_NUMBER: _ClassVar[int]
    SINGLE_FILE_RESTORE_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    PARALLEL_ENTITY_RESTORES_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    NEXT_ENTITY_ID_TO_RESTORE_FIELD_NUMBER: _ClassVar[int]
    ALL_TASKS_CREATED_FIELD_NUMBER: _ClassVar[int]
    PARALLEL_FILE_RESTORES_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    COOKIE_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    HYDRATION_DURATION_USECS_FIELD_NUMBER: _ClassVar[int]
    LAST_HYDRATION_START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    LAST_HYDRATION_END_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    LAST_HYDRATION_DURATION_USECS_FIELD_NUMBER: _ClassVar[int]
    CURRENT_VIEW_FS_INDEX_FIELD_NUMBER: _ClassVar[int]
    found_view_fs: bool
    view_fs_vec: _containers.RepeatedCompositeFieldContainer[RestoreJobContext.ViewFS]
    cookie_view_id: int
    single_file_restore_entity_id: int
    parallel_entity_restores_supported: bool
    next_entity_id_to_restore: int
    all_tasks_created: bool
    parallel_file_restores_supported: bool
    cookie_entity_id: int
    hydration_duration_usecs: int
    last_hydration_start_time_usecs: int
    last_hydration_end_time_usecs: int
    last_hydration_duration_usecs: int
    current_view_fs_index: int
    def __init__(self, found_view_fs: bool = ..., view_fs_vec: _Optional[_Iterable[_Union[RestoreJobContext.ViewFS, _Mapping]]] = ..., cookie_view_id: _Optional[int] = ..., single_file_restore_entity_id: _Optional[int] = ..., parallel_entity_restores_supported: bool = ..., next_entity_id_to_restore: _Optional[int] = ..., all_tasks_created: bool = ..., parallel_file_restores_supported: bool = ..., cookie_entity_id: _Optional[int] = ..., hydration_duration_usecs: _Optional[int] = ..., last_hydration_start_time_usecs: _Optional[int] = ..., last_hydration_end_time_usecs: _Optional[int] = ..., last_hydration_duration_usecs: _Optional[int] = ..., current_view_fs_index: _Optional[int] = ...) -> None: ...

class ArchiveViewSnapTreesContext(_message.Message):
    __slots__ = ("remaining_view_info_vec", "cookie_entity_id")
    class ViewInfo(_message.Message):
        __slots__ = ("view_id", "node_id_floor", "sub_snap_tree_vec", "next_sub_snap_tree_idx", "all_sub_trees_serialized")
        VIEW_ID_FIELD_NUMBER: _ClassVar[int]
        NODE_ID_FLOOR_FIELD_NUMBER: _ClassVar[int]
        SUB_SNAP_TREE_VEC_FIELD_NUMBER: _ClassVar[int]
        NEXT_SUB_SNAP_TREE_IDX_FIELD_NUMBER: _ClassVar[int]
        ALL_SUB_TREES_SERIALIZED_FIELD_NUMBER: _ClassVar[int]
        view_id: int
        node_id_floor: int
        sub_snap_tree_vec: _containers.RepeatedCompositeFieldContainer[SubSnapTree]
        next_sub_snap_tree_idx: int
        all_sub_trees_serialized: bool
        def __init__(self, view_id: _Optional[int] = ..., node_id_floor: _Optional[int] = ..., sub_snap_tree_vec: _Optional[_Iterable[_Union[SubSnapTree, _Mapping]]] = ..., next_sub_snap_tree_idx: _Optional[int] = ..., all_sub_trees_serialized: bool = ...) -> None: ...
    REMAINING_VIEW_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    COOKIE_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    remaining_view_info_vec: _containers.RepeatedCompositeFieldContainer[ArchiveViewSnapTreesContext.ViewInfo]
    cookie_entity_id: int
    def __init__(self, remaining_view_info_vec: _Optional[_Iterable[_Union[ArchiveViewSnapTreesContext.ViewInfo, _Mapping]]] = ..., cookie_entity_id: _Optional[int] = ...) -> None: ...

class SnapTreeKeyRange(_message.Message):
    __slots__ = ("min_key", "max_key", "snap_tree_id", "is_view_snap_tree")
    MIN_KEY_FIELD_NUMBER: _ClassVar[int]
    MAX_KEY_FIELD_NUMBER: _ClassVar[int]
    SNAP_TREE_ID_FIELD_NUMBER: _ClassVar[int]
    IS_VIEW_SNAP_TREE_FIELD_NUMBER: _ClassVar[int]
    min_key: int
    max_key: int
    snap_tree_id: int
    is_view_snap_tree: bool
    def __init__(self, min_key: _Optional[int] = ..., max_key: _Optional[int] = ..., snap_tree_id: _Optional[int] = ..., is_view_snap_tree: bool = ...) -> None: ...

class SubSnapTree(_message.Message):
    __slots__ = ("tree_id", "sub_tree_id", "min_key", "max_key", "is_serialized")
    TREE_ID_FIELD_NUMBER: _ClassVar[int]
    SUB_TREE_ID_FIELD_NUMBER: _ClassVar[int]
    MIN_KEY_FIELD_NUMBER: _ClassVar[int]
    MAX_KEY_FIELD_NUMBER: _ClassVar[int]
    IS_SERIALIZED_FIELD_NUMBER: _ClassVar[int]
    tree_id: int
    sub_tree_id: int
    min_key: int
    max_key: int
    is_serialized: bool
    def __init__(self, tree_id: _Optional[int] = ..., sub_tree_id: _Optional[int] = ..., min_key: _Optional[int] = ..., max_key: _Optional[int] = ..., is_serialized: bool = ...) -> None: ...

class UptierDowntierContext(_message.Message):
    __slots__ = ("stub_view_name", "internal_view_name", "directory_walker_checkpoint_file_path", "num_objects_uptiered", "uptiered_data_size_bytes", "has_active_uptier_task", "all_uptier_tasks_created", "first_uptier_task_completed", "object_info_dir_path_vec", "dir_walker_cookie", "all_downtier_tasks_created")
    STUB_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    INTERNAL_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    DIRECTORY_WALKER_CHECKPOINT_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    NUM_OBJECTS_UPTIERED_FIELD_NUMBER: _ClassVar[int]
    UPTIERED_DATA_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    HAS_ACTIVE_UPTIER_TASK_FIELD_NUMBER: _ClassVar[int]
    ALL_UPTIER_TASKS_CREATED_FIELD_NUMBER: _ClassVar[int]
    FIRST_UPTIER_TASK_COMPLETED_FIELD_NUMBER: _ClassVar[int]
    OBJECT_INFO_DIR_PATH_VEC_FIELD_NUMBER: _ClassVar[int]
    DIR_WALKER_COOKIE_FIELD_NUMBER: _ClassVar[int]
    ALL_DOWNTIER_TASKS_CREATED_FIELD_NUMBER: _ClassVar[int]
    stub_view_name: str
    internal_view_name: str
    directory_walker_checkpoint_file_path: str
    num_objects_uptiered: int
    uptiered_data_size_bytes: int
    has_active_uptier_task: bool
    all_uptier_tasks_created: bool
    first_uptier_task_completed: bool
    object_info_dir_path_vec: _containers.RepeatedScalarFieldContainer[str]
    dir_walker_cookie: _directory_walker_pb2.EntityMetadata
    all_downtier_tasks_created: bool
    def __init__(self, stub_view_name: _Optional[str] = ..., internal_view_name: _Optional[str] = ..., directory_walker_checkpoint_file_path: _Optional[str] = ..., num_objects_uptiered: _Optional[int] = ..., uptiered_data_size_bytes: _Optional[int] = ..., has_active_uptier_task: bool = ..., all_uptier_tasks_created: bool = ..., first_uptier_task_completed: bool = ..., object_info_dir_path_vec: _Optional[_Iterable[str]] = ..., dir_walker_cookie: _Optional[_Union[_directory_walker_pb2.EntityMetadata, _Mapping]] = ..., all_downtier_tasks_created: bool = ...) -> None: ...

class UptierCloudDomainDataContext(_message.Message):
    __slots__ = ("uptier_task_active", "uptiering_done", "last_finished_uptier_task_timestamp_usecs", "num_objects_to_uptier", "num_objects_uptiered")
    UPTIER_TASK_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    UPTIERING_DONE_FIELD_NUMBER: _ClassVar[int]
    LAST_FINISHED_UPTIER_TASK_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
    NUM_OBJECTS_TO_UPTIER_FIELD_NUMBER: _ClassVar[int]
    NUM_OBJECTS_UPTIERED_FIELD_NUMBER: _ClassVar[int]
    uptier_task_active: bool
    uptiering_done: bool
    last_finished_uptier_task_timestamp_usecs: int
    num_objects_to_uptier: int
    num_objects_uptiered: int
    def __init__(self, uptier_task_active: bool = ..., uptiering_done: bool = ..., last_finished_uptier_task_timestamp_usecs: _Optional[int] = ..., num_objects_to_uptier: _Optional[int] = ..., num_objects_uptiered: _Optional[int] = ...) -> None: ...

class RestoreStubSnapTreeContext(_message.Message):
    __slots__ = ("is_restored",)
    IS_RESTORED_FIELD_NUMBER: _ClassVar[int]
    is_restored: bool
    def __init__(self, is_restored: bool = ...) -> None: ...

class StubViewJobContextProto(_message.Message):
    __slots__ = ("stub_view_tasks_created", "view_snap_tree_ranges_created", "prefetch_view_snap_tree_tasks_created", "blob_snap_tree_ranges_created", "prefetch_blob_snap_tree_tasks_created", "prefetch_files_tasks_created", "current_entity_index", "entity_snap_tree_ranges_map", "is_stub_view_prefetching_supported", "entity_blob_snap_tree_data_map", "is_caller_notified", "is_direct_archive_restore_from_archive_tiers_supported", "is_flr_to_source_from_glacier_supported", "entity_state_vec", "reuse_existing_stub_view", "should_create_uptier_downtier_tasks", "last_caller_notification_timestamp_usecs", "should_restore_stub_snap_trees", "restore_stub_snap_trees_tasks_created", "entity_to_stub_view_map", "should_uptier_cloud_domain_data", "uptier_cloud_domain_data_tasks_created", "next_entity_id")
    class SnapTreeRanges(_message.Message):
        __slots__ = ("snap_tree_range_vec", "next_snap_tree_range_index")
        SNAP_TREE_RANGE_VEC_FIELD_NUMBER: _ClassVar[int]
        NEXT_SNAP_TREE_RANGE_INDEX_FIELD_NUMBER: _ClassVar[int]
        snap_tree_range_vec: _containers.RepeatedCompositeFieldContainer[SnapTreeKeyRange]
        next_snap_tree_range_index: int
        def __init__(self, snap_tree_range_vec: _Optional[_Iterable[_Union[SnapTreeKeyRange, _Mapping]]] = ..., next_snap_tree_range_index: _Optional[int] = ...) -> None: ...
    class EntitySnapTreeRangesMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: StubViewJobContextProto.SnapTreeRanges
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[StubViewJobContextProto.SnapTreeRanges, _Mapping]] = ...) -> None: ...
    class BlobSnapTreeIds(_message.Message):
        __slots__ = ("blob_snap_tree_id_vec", "blob_data_ranges_map")
        class BlobDataRangesMapEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: int
            value: _icebox_pb2.BlobDataRanges
            def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_icebox_pb2.BlobDataRanges, _Mapping]] = ...) -> None: ...
        BLOB_SNAP_TREE_ID_VEC_FIELD_NUMBER: _ClassVar[int]
        BLOB_DATA_RANGES_MAP_FIELD_NUMBER: _ClassVar[int]
        blob_snap_tree_id_vec: _containers.RepeatedScalarFieldContainer[int]
        blob_data_ranges_map: _containers.MessageMap[int, _icebox_pb2.BlobDataRanges]
        def __init__(self, blob_snap_tree_id_vec: _Optional[_Iterable[int]] = ..., blob_data_ranges_map: _Optional[_Mapping[int, _icebox_pb2.BlobDataRanges]] = ...) -> None: ...
    class EntityBlobSnapTreeDataMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: StubViewJobContextProto.BlobSnapTreeIds
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[StubViewJobContextProto.BlobSnapTreeIds, _Mapping]] = ...) -> None: ...
    class EntityState(_message.Message):
        __slots__ = ("entity_id", "uptier_downtier_context")
        ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
        UPTIER_DOWNTIER_CONTEXT_FIELD_NUMBER: _ClassVar[int]
        entity_id: int
        uptier_downtier_context: UptierDowntierContext
        def __init__(self, entity_id: _Optional[int] = ..., uptier_downtier_context: _Optional[_Union[UptierDowntierContext, _Mapping]] = ...) -> None: ...
    class StubViewSnapTreesInfo(_message.Message):
        __slots__ = ("view_id", "view_snap_tree_id_vec", "next_snap_tree_index", "uptier_context_vec", "restore_context_vec", "fs_name_vec", "uptier_files_context")
        VIEW_ID_FIELD_NUMBER: _ClassVar[int]
        VIEW_SNAP_TREE_ID_VEC_FIELD_NUMBER: _ClassVar[int]
        NEXT_SNAP_TREE_INDEX_FIELD_NUMBER: _ClassVar[int]
        UPTIER_CONTEXT_VEC_FIELD_NUMBER: _ClassVar[int]
        RESTORE_CONTEXT_VEC_FIELD_NUMBER: _ClassVar[int]
        FS_NAME_VEC_FIELD_NUMBER: _ClassVar[int]
        UPTIER_FILES_CONTEXT_FIELD_NUMBER: _ClassVar[int]
        view_id: int
        view_snap_tree_id_vec: _containers.RepeatedScalarFieldContainer[int]
        next_snap_tree_index: int
        uptier_context_vec: _containers.RepeatedCompositeFieldContainer[UptierCloudDomainDataContext]
        restore_context_vec: _containers.RepeatedCompositeFieldContainer[RestoreStubSnapTreeContext]
        fs_name_vec: _containers.RepeatedScalarFieldContainer[str]
        uptier_files_context: UptierCloudDomainDataContext
        def __init__(self, view_id: _Optional[int] = ..., view_snap_tree_id_vec: _Optional[_Iterable[int]] = ..., next_snap_tree_index: _Optional[int] = ..., uptier_context_vec: _Optional[_Iterable[_Union[UptierCloudDomainDataContext, _Mapping]]] = ..., restore_context_vec: _Optional[_Iterable[_Union[RestoreStubSnapTreeContext, _Mapping]]] = ..., fs_name_vec: _Optional[_Iterable[str]] = ..., uptier_files_context: _Optional[_Union[UptierCloudDomainDataContext, _Mapping]] = ...) -> None: ...
    class EntityToStubViewMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: StubViewJobContextProto.StubViewSnapTreesInfo
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[StubViewJobContextProto.StubViewSnapTreesInfo, _Mapping]] = ...) -> None: ...
    STUB_VIEW_TASKS_CREATED_FIELD_NUMBER: _ClassVar[int]
    VIEW_SNAP_TREE_RANGES_CREATED_FIELD_NUMBER: _ClassVar[int]
    PREFETCH_VIEW_SNAP_TREE_TASKS_CREATED_FIELD_NUMBER: _ClassVar[int]
    BLOB_SNAP_TREE_RANGES_CREATED_FIELD_NUMBER: _ClassVar[int]
    PREFETCH_BLOB_SNAP_TREE_TASKS_CREATED_FIELD_NUMBER: _ClassVar[int]
    PREFETCH_FILES_TASKS_CREATED_FIELD_NUMBER: _ClassVar[int]
    CURRENT_ENTITY_INDEX_FIELD_NUMBER: _ClassVar[int]
    ENTITY_SNAP_TREE_RANGES_MAP_FIELD_NUMBER: _ClassVar[int]
    IS_STUB_VIEW_PREFETCHING_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    ENTITY_BLOB_SNAP_TREE_DATA_MAP_FIELD_NUMBER: _ClassVar[int]
    IS_CALLER_NOTIFIED_FIELD_NUMBER: _ClassVar[int]
    IS_DIRECT_ARCHIVE_RESTORE_FROM_ARCHIVE_TIERS_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    IS_FLR_TO_SOURCE_FROM_GLACIER_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    ENTITY_STATE_VEC_FIELD_NUMBER: _ClassVar[int]
    REUSE_EXISTING_STUB_VIEW_FIELD_NUMBER: _ClassVar[int]
    SHOULD_CREATE_UPTIER_DOWNTIER_TASKS_FIELD_NUMBER: _ClassVar[int]
    LAST_CALLER_NOTIFICATION_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
    SHOULD_RESTORE_STUB_SNAP_TREES_FIELD_NUMBER: _ClassVar[int]
    RESTORE_STUB_SNAP_TREES_TASKS_CREATED_FIELD_NUMBER: _ClassVar[int]
    ENTITY_TO_STUB_VIEW_MAP_FIELD_NUMBER: _ClassVar[int]
    SHOULD_UPTIER_CLOUD_DOMAIN_DATA_FIELD_NUMBER: _ClassVar[int]
    UPTIER_CLOUD_DOMAIN_DATA_TASKS_CREATED_FIELD_NUMBER: _ClassVar[int]
    NEXT_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    stub_view_tasks_created: bool
    view_snap_tree_ranges_created: bool
    prefetch_view_snap_tree_tasks_created: bool
    blob_snap_tree_ranges_created: bool
    prefetch_blob_snap_tree_tasks_created: bool
    prefetch_files_tasks_created: bool
    current_entity_index: int
    entity_snap_tree_ranges_map: _containers.MessageMap[int, StubViewJobContextProto.SnapTreeRanges]
    is_stub_view_prefetching_supported: bool
    entity_blob_snap_tree_data_map: _containers.MessageMap[int, StubViewJobContextProto.BlobSnapTreeIds]
    is_caller_notified: bool
    is_direct_archive_restore_from_archive_tiers_supported: bool
    is_flr_to_source_from_glacier_supported: bool
    entity_state_vec: _containers.RepeatedCompositeFieldContainer[StubViewJobContextProto.EntityState]
    reuse_existing_stub_view: bool
    should_create_uptier_downtier_tasks: bool
    last_caller_notification_timestamp_usecs: int
    should_restore_stub_snap_trees: bool
    restore_stub_snap_trees_tasks_created: bool
    entity_to_stub_view_map: _containers.MessageMap[int, StubViewJobContextProto.StubViewSnapTreesInfo]
    should_uptier_cloud_domain_data: bool
    uptier_cloud_domain_data_tasks_created: bool
    next_entity_id: int
    def __init__(self, stub_view_tasks_created: bool = ..., view_snap_tree_ranges_created: bool = ..., prefetch_view_snap_tree_tasks_created: bool = ..., blob_snap_tree_ranges_created: bool = ..., prefetch_blob_snap_tree_tasks_created: bool = ..., prefetch_files_tasks_created: bool = ..., current_entity_index: _Optional[int] = ..., entity_snap_tree_ranges_map: _Optional[_Mapping[int, StubViewJobContextProto.SnapTreeRanges]] = ..., is_stub_view_prefetching_supported: bool = ..., entity_blob_snap_tree_data_map: _Optional[_Mapping[int, StubViewJobContextProto.BlobSnapTreeIds]] = ..., is_caller_notified: bool = ..., is_direct_archive_restore_from_archive_tiers_supported: bool = ..., is_flr_to_source_from_glacier_supported: bool = ..., entity_state_vec: _Optional[_Iterable[_Union[StubViewJobContextProto.EntityState, _Mapping]]] = ..., reuse_existing_stub_view: bool = ..., should_create_uptier_downtier_tasks: bool = ..., last_caller_notification_timestamp_usecs: _Optional[int] = ..., should_restore_stub_snap_trees: bool = ..., restore_stub_snap_trees_tasks_created: bool = ..., entity_to_stub_view_map: _Optional[_Mapping[int, StubViewJobContextProto.StubViewSnapTreesInfo]] = ..., should_uptier_cloud_domain_data: bool = ..., uptier_cloud_domain_data_tasks_created: bool = ..., next_entity_id: _Optional[int] = ...) -> None: ...

class FSWalkContext(_message.Message):
    __slots__ = ("pending_fs_file_vec", "cookie", "fetched_all_files", "is_list_task_active", "is_cleanup_task_active")
    PENDING_FS_FILE_VEC_FIELD_NUMBER: _ClassVar[int]
    COOKIE_FIELD_NUMBER: _ClassVar[int]
    FETCHED_ALL_FILES_FIELD_NUMBER: _ClassVar[int]
    IS_LIST_TASK_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    IS_CLEANUP_TASK_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    pending_fs_file_vec: _containers.RepeatedCompositeFieldContainer[_icebox_pb2.FSFileProto]
    cookie: str
    fetched_all_files: bool
    is_list_task_active: bool
    is_cleanup_task_active: bool
    def __init__(self, pending_fs_file_vec: _Optional[_Iterable[_Union[_icebox_pb2.FSFileProto, _Mapping]]] = ..., cookie: _Optional[str] = ..., fetched_all_files: bool = ..., is_list_task_active: bool = ..., is_cleanup_task_active: bool = ...) -> None: ...

class DirectArchiveGCJobContext(_message.Message):
    __slots__ = ("app_job_uid", "expired_direct_archive_job_uid_vec", "unexpired_direct_archive_job_uid_vec", "view_name", "fs_name", "next_direct_archive_index", "object_info_vec", "next_object_to_download_index", "is_apollo_req_task_created", "max_snap_tree_height", "action_files_view", "action_files_fs_name", "action_files_relative_dir", "relative_dir_path_vec")
    APP_JOB_UID_FIELD_NUMBER: _ClassVar[int]
    EXPIRED_DIRECT_ARCHIVE_JOB_UID_VEC_FIELD_NUMBER: _ClassVar[int]
    UNEXPIRED_DIRECT_ARCHIVE_JOB_UID_VEC_FIELD_NUMBER: _ClassVar[int]
    VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    FS_NAME_FIELD_NUMBER: _ClassVar[int]
    NEXT_DIRECT_ARCHIVE_INDEX_FIELD_NUMBER: _ClassVar[int]
    OBJECT_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    NEXT_OBJECT_TO_DOWNLOAD_INDEX_FIELD_NUMBER: _ClassVar[int]
    IS_APOLLO_REQ_TASK_CREATED_FIELD_NUMBER: _ClassVar[int]
    MAX_SNAP_TREE_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    ACTION_FILES_VIEW_FIELD_NUMBER: _ClassVar[int]
    ACTION_FILES_FS_NAME_FIELD_NUMBER: _ClassVar[int]
    ACTION_FILES_RELATIVE_DIR_FIELD_NUMBER: _ClassVar[int]
    RELATIVE_DIR_PATH_VEC_FIELD_NUMBER: _ClassVar[int]
    app_job_uid: _universal_id_pb2.UniversalIdProto
    expired_direct_archive_job_uid_vec: _containers.RepeatedCompositeFieldContainer[_universal_id_pb2.UniversalIdProto]
    unexpired_direct_archive_job_uid_vec: _containers.RepeatedCompositeFieldContainer[_universal_id_pb2.UniversalIdProto]
    view_name: str
    fs_name: str
    next_direct_archive_index: int
    object_info_vec: _containers.RepeatedCompositeFieldContainer[_icebox_pb2.ObjectInfoProto]
    next_object_to_download_index: int
    is_apollo_req_task_created: bool
    max_snap_tree_height: int
    action_files_view: str
    action_files_fs_name: str
    action_files_relative_dir: str
    relative_dir_path_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, app_job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., expired_direct_archive_job_uid_vec: _Optional[_Iterable[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]]] = ..., unexpired_direct_archive_job_uid_vec: _Optional[_Iterable[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]]] = ..., view_name: _Optional[str] = ..., fs_name: _Optional[str] = ..., next_direct_archive_index: _Optional[int] = ..., object_info_vec: _Optional[_Iterable[_Union[_icebox_pb2.ObjectInfoProto, _Mapping]]] = ..., next_object_to_download_index: _Optional[int] = ..., is_apollo_req_task_created: bool = ..., max_snap_tree_height: _Optional[int] = ..., action_files_view: _Optional[str] = ..., action_files_fs_name: _Optional[str] = ..., action_files_relative_dir: _Optional[str] = ..., relative_dir_path_vec: _Optional[_Iterable[str]] = ...) -> None: ...

class DirectArchiveJobContext(_message.Message):
    __slots__ = ("internal_view_name", "internal_view_fs", "relative_objects_info_dir", "enable_unified_view", "unified_view_dir_path", "enable_compression", "enable_encryption")
    INTERNAL_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    INTERNAL_VIEW_FS_FIELD_NUMBER: _ClassVar[int]
    RELATIVE_OBJECTS_INFO_DIR_FIELD_NUMBER: _ClassVar[int]
    ENABLE_UNIFIED_VIEW_FIELD_NUMBER: _ClassVar[int]
    UNIFIED_VIEW_DIR_PATH_FIELD_NUMBER: _ClassVar[int]
    ENABLE_COMPRESSION_FIELD_NUMBER: _ClassVar[int]
    ENABLE_ENCRYPTION_FIELD_NUMBER: _ClassVar[int]
    internal_view_name: str
    internal_view_fs: str
    relative_objects_info_dir: str
    enable_unified_view: bool
    unified_view_dir_path: str
    enable_compression: bool
    enable_encryption: bool
    def __init__(self, internal_view_name: _Optional[str] = ..., internal_view_fs: _Optional[str] = ..., relative_objects_info_dir: _Optional[str] = ..., enable_unified_view: bool = ..., unified_view_dir_path: _Optional[str] = ..., enable_compression: bool = ..., enable_encryption: bool = ...) -> None: ...

class ValidateObjectsContext(_message.Message):
    __slots__ = ("referred_archive_uid_vec", "referred_object_uid_vec", "all_tasks_created", "is_lifecycle_policy_task_created", "objects_validation_info")
    REFERRED_ARCHIVE_UID_VEC_FIELD_NUMBER: _ClassVar[int]
    REFERRED_OBJECT_UID_VEC_FIELD_NUMBER: _ClassVar[int]
    ALL_TASKS_CREATED_FIELD_NUMBER: _ClassVar[int]
    IS_LIFECYCLE_POLICY_TASK_CREATED_FIELD_NUMBER: _ClassVar[int]
    OBJECTS_VALIDATION_INFO_FIELD_NUMBER: _ClassVar[int]
    referred_archive_uid_vec: _containers.RepeatedCompositeFieldContainer[_universal_id_pb2.UniversalIdProto]
    referred_object_uid_vec: _containers.RepeatedCompositeFieldContainer[_universal_id_pb2.UniversalIdProto]
    all_tasks_created: bool
    is_lifecycle_policy_task_created: bool
    objects_validation_info: _icebox_pb2.ObjectsValidationInfo
    def __init__(self, referred_archive_uid_vec: _Optional[_Iterable[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]]] = ..., referred_object_uid_vec: _Optional[_Iterable[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]]] = ..., all_tasks_created: bool = ..., is_lifecycle_policy_task_created: bool = ..., objects_validation_info: _Optional[_Union[_icebox_pb2.ObjectsValidationInfo, _Mapping]] = ...) -> None: ...

class TaskStateProto(_message.Message):
    __slots__ = ("task_id", "state", "type", "task_data", "hydration_start_time_usecs", "hydration_end_time_usecs", "is_allotted_on_extra_slot", "task_priority", "crashing_constituent_id_vec")
    class TaskType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kPreprocessJob: _ClassVar[TaskStateProto.TaskType]
        kCreateJobMetadataFiles: _ClassVar[TaskStateProto.TaskType]
        kCreateIndexFiles: _ClassVar[TaskStateProto.TaskType]
        kArchiveBlobs: _ClassVar[TaskStateProto.TaskType]
        kArchiveBlobSnapTrees: _ClassVar[TaskStateProto.TaskType]
        kArchiveViewSnapTrees: _ClassVar[TaskStateProto.TaskType]
        kArchiveMetadata: _ClassVar[TaskStateProto.TaskType]
        kRestoreMetadata: _ClassVar[TaskStateProto.TaskType]
        kRestoreViewSnapTree: _ClassVar[TaskStateProto.TaskType]
        kRestoreBlobs: _ClassVar[TaskStateProto.TaskType]
        kRestoreDirectories: _ClassVar[TaskStateProto.TaskType]
        kFinalizeArchiveObjects: _ClassVar[TaskStateProto.TaskType]
        kListObjects: _ClassVar[TaskStateProto.TaskType]
        kReadObjectsMetadata: _ClassVar[TaskStateProto.TaskType]
        kRegisterAppJobMetadata: _ClassVar[TaskStateProto.TaskType]
        kBuildIndex: _ClassVar[TaskStateProto.TaskType]
        kPostprocessRestoredIndex: _ClassVar[TaskStateProto.TaskType]
        kPostprocessJob: _ClassVar[TaskStateProto.TaskType]
        kFixUpdateIntents: _ClassVar[TaskStateProto.TaskType]
        kCreateStubView: _ClassVar[TaskStateProto.TaskType]
        kGetFilesToUpload: _ClassVar[TaskStateProto.TaskType]
        kUploadFiles: _ClassVar[TaskStateProto.TaskType]
        kPrefetchFiles: _ClassVar[TaskStateProto.TaskType]
        kBackupQuotaSnapTree: _ClassVar[TaskStateProto.TaskType]
        kRestoreQuotaSnapTree: _ClassVar[TaskStateProto.TaskType]
        kListVaultFSFiles: _ClassVar[TaskStateProto.TaskType]
        kPrepareArchiveObjects: _ClassVar[TaskStateProto.TaskType]
        kArchiveDirectArchiveBlobs: _ClassVar[TaskStateProto.TaskType]
        kGetBlobsInfo: _ClassVar[TaskStateProto.TaskType]
        kPrefetchViewSnapTree: _ClassVar[TaskStateProto.TaskType]
        kDownloadSnapTreeObjects: _ClassVar[TaskStateProto.TaskType]
        kIssueDirectArchiveGCReqToApollo: _ClassVar[TaskStateProto.TaskType]
        kListViewFSFiles: _ClassVar[TaskStateProto.TaskType]
        kCleanupObjects: _ClassVar[TaskStateProto.TaskType]
        kValidateObjects: _ClassVar[TaskStateProto.TaskType]
        kEvictObjectsFromVaultCache: _ClassVar[TaskStateProto.TaskType]
        kPrefetchBlobSnapTree: _ClassVar[TaskStateProto.TaskType]
        kUptierArchiveObjects: _ClassVar[TaskStateProto.TaskType]
        kDowntierArchiveObjects: _ClassVar[TaskStateProto.TaskType]
        kCrashSlave: _ClassVar[TaskStateProto.TaskType]
        kCloudDomainArchiveTrees: _ClassVar[TaskStateProto.TaskType]
        kCloudDomainFixUpdateIntents: _ClassVar[TaskStateProto.TaskType]
        kRestoreStubSnapTrees: _ClassVar[TaskStateProto.TaskType]
        kUptierCloudDomainData: _ClassVar[TaskStateProto.TaskType]
        kListCloudDomains: _ClassVar[TaskStateProto.TaskType]
        kFindAccessibleCloudDomains: _ClassVar[TaskStateProto.TaskType]
        kListArchiveMetadataObjects: _ClassVar[TaskStateProto.TaskType]
        kReadArchiveMetadataObjectsFromCSR: _ClassVar[TaskStateProto.TaskType]
        kIssueDomainMigrationRequestsToApollo: _ClassVar[TaskStateProto.TaskType]
        kInitiateTenantFailover: _ClassVar[TaskStateProto.TaskType]
        kRegisterRuns: _ClassVar[TaskStateProto.TaskType]
        kInitiateSnapshotMigration: _ClassVar[TaskStateProto.TaskType]
        kSetWORMRetentionOnObjects: _ClassVar[TaskStateProto.TaskType]
        kPopulateCloudDomainScribeEntries: _ClassVar[TaskStateProto.TaskType]
        kCohesionCopyData: _ClassVar[TaskStateProto.TaskType]
        kCohesionFixUpdateIntents: _ClassVar[TaskStateProto.TaskType]
    kPreprocessJob: TaskStateProto.TaskType
    kCreateJobMetadataFiles: TaskStateProto.TaskType
    kCreateIndexFiles: TaskStateProto.TaskType
    kArchiveBlobs: TaskStateProto.TaskType
    kArchiveBlobSnapTrees: TaskStateProto.TaskType
    kArchiveViewSnapTrees: TaskStateProto.TaskType
    kArchiveMetadata: TaskStateProto.TaskType
    kRestoreMetadata: TaskStateProto.TaskType
    kRestoreViewSnapTree: TaskStateProto.TaskType
    kRestoreBlobs: TaskStateProto.TaskType
    kRestoreDirectories: TaskStateProto.TaskType
    kFinalizeArchiveObjects: TaskStateProto.TaskType
    kListObjects: TaskStateProto.TaskType
    kReadObjectsMetadata: TaskStateProto.TaskType
    kRegisterAppJobMetadata: TaskStateProto.TaskType
    kBuildIndex: TaskStateProto.TaskType
    kPostprocessRestoredIndex: TaskStateProto.TaskType
    kPostprocessJob: TaskStateProto.TaskType
    kFixUpdateIntents: TaskStateProto.TaskType
    kCreateStubView: TaskStateProto.TaskType
    kGetFilesToUpload: TaskStateProto.TaskType
    kUploadFiles: TaskStateProto.TaskType
    kPrefetchFiles: TaskStateProto.TaskType
    kBackupQuotaSnapTree: TaskStateProto.TaskType
    kRestoreQuotaSnapTree: TaskStateProto.TaskType
    kListVaultFSFiles: TaskStateProto.TaskType
    kPrepareArchiveObjects: TaskStateProto.TaskType
    kArchiveDirectArchiveBlobs: TaskStateProto.TaskType
    kGetBlobsInfo: TaskStateProto.TaskType
    kPrefetchViewSnapTree: TaskStateProto.TaskType
    kDownloadSnapTreeObjects: TaskStateProto.TaskType
    kIssueDirectArchiveGCReqToApollo: TaskStateProto.TaskType
    kListViewFSFiles: TaskStateProto.TaskType
    kCleanupObjects: TaskStateProto.TaskType
    kValidateObjects: TaskStateProto.TaskType
    kEvictObjectsFromVaultCache: TaskStateProto.TaskType
    kPrefetchBlobSnapTree: TaskStateProto.TaskType
    kUptierArchiveObjects: TaskStateProto.TaskType
    kDowntierArchiveObjects: TaskStateProto.TaskType
    kCrashSlave: TaskStateProto.TaskType
    kCloudDomainArchiveTrees: TaskStateProto.TaskType
    kCloudDomainFixUpdateIntents: TaskStateProto.TaskType
    kRestoreStubSnapTrees: TaskStateProto.TaskType
    kUptierCloudDomainData: TaskStateProto.TaskType
    kListCloudDomains: TaskStateProto.TaskType
    kFindAccessibleCloudDomains: TaskStateProto.TaskType
    kListArchiveMetadataObjects: TaskStateProto.TaskType
    kReadArchiveMetadataObjectsFromCSR: TaskStateProto.TaskType
    kIssueDomainMigrationRequestsToApollo: TaskStateProto.TaskType
    kInitiateTenantFailover: TaskStateProto.TaskType
    kRegisterRuns: TaskStateProto.TaskType
    kInitiateSnapshotMigration: TaskStateProto.TaskType
    kSetWORMRetentionOnObjects: TaskStateProto.TaskType
    kPopulateCloudDomainScribeEntries: TaskStateProto.TaskType
    kCohesionCopyData: TaskStateProto.TaskType
    kCohesionFixUpdateIntents: TaskStateProto.TaskType
    class TaskPriority(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kLow: _ClassVar[TaskStateProto.TaskPriority]
        kMedium: _ClassVar[TaskStateProto.TaskPriority]
        kHigh: _ClassVar[TaskStateProto.TaskPriority]
    kLow: TaskStateProto.TaskPriority
    kMedium: TaskStateProto.TaskPriority
    kHigh: TaskStateProto.TaskPriority
    class RegisterAppJobMetadataTaskContextProto(_message.Message):
        __slots__ = ("archive_uid",)
        ARCHIVE_UID_FIELD_NUMBER: _ClassVar[int]
        archive_uid: _universal_id_pb2.UniversalIdProto
        def __init__(self, archive_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ...) -> None: ...
    class RestoreDirectoriesTaskContextProto(_message.Message):
        __slots__ = ("archive_uid", "target_view_name", "file_system_name", "source_rel_path", "dest_rel_path", "create_view", "lookup_search_archive_metadata", "source_view_id", "source_rel_path_vec", "archive_object_uid_vec")
        ARCHIVE_UID_FIELD_NUMBER: _ClassVar[int]
        TARGET_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
        FILE_SYSTEM_NAME_FIELD_NUMBER: _ClassVar[int]
        SOURCE_REL_PATH_FIELD_NUMBER: _ClassVar[int]
        DEST_REL_PATH_FIELD_NUMBER: _ClassVar[int]
        CREATE_VIEW_FIELD_NUMBER: _ClassVar[int]
        LOOKUP_SEARCH_ARCHIVE_METADATA_FIELD_NUMBER: _ClassVar[int]
        SOURCE_VIEW_ID_FIELD_NUMBER: _ClassVar[int]
        SOURCE_REL_PATH_VEC_FIELD_NUMBER: _ClassVar[int]
        ARCHIVE_OBJECT_UID_VEC_FIELD_NUMBER: _ClassVar[int]
        archive_uid: _universal_id_pb2.UniversalIdProto
        target_view_name: str
        file_system_name: str
        source_rel_path: str
        dest_rel_path: str
        create_view: bool
        lookup_search_archive_metadata: bool
        source_view_id: int
        source_rel_path_vec: _containers.RepeatedScalarFieldContainer[str]
        archive_object_uid_vec: _containers.RepeatedCompositeFieldContainer[_universal_id_pb2.UniversalIdProto]
        def __init__(self, archive_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., target_view_name: _Optional[str] = ..., file_system_name: _Optional[str] = ..., source_rel_path: _Optional[str] = ..., dest_rel_path: _Optional[str] = ..., create_view: bool = ..., lookup_search_archive_metadata: bool = ..., source_view_id: _Optional[int] = ..., source_rel_path_vec: _Optional[_Iterable[str]] = ..., archive_object_uid_vec: _Optional[_Iterable[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]]] = ...) -> None: ...
    class BuildIndexTaskContextProto(_message.Message):
        __slots__ = ("archive_uid", "index_view_name", "file_system_name", "index_dir_rel_path")
        ARCHIVE_UID_FIELD_NUMBER: _ClassVar[int]
        INDEX_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
        FILE_SYSTEM_NAME_FIELD_NUMBER: _ClassVar[int]
        INDEX_DIR_REL_PATH_FIELD_NUMBER: _ClassVar[int]
        archive_uid: _universal_id_pb2.UniversalIdProto
        index_view_name: str
        file_system_name: str
        index_dir_rel_path: str
        def __init__(self, archive_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., index_view_name: _Optional[str] = ..., file_system_name: _Optional[str] = ..., index_dir_rel_path: _Optional[str] = ...) -> None: ...
    class FinalizeArchiveObjectsContextProto(_message.Message):
        __slots__ = ("object_data_vec", "abort_objects")
        OBJECT_DATA_VEC_FIELD_NUMBER: _ClassVar[int]
        ABORT_OBJECTS_FIELD_NUMBER: _ClassVar[int]
        object_data_vec: _containers.RepeatedCompositeFieldContainer[_icebox_pb2.TaskCheckpointInfo.ObjectData]
        abort_objects: bool
        def __init__(self, object_data_vec: _Optional[_Iterable[_Union[_icebox_pb2.TaskCheckpointInfo.ObjectData, _Mapping]]] = ..., abort_objects: bool = ...) -> None: ...
    class PostprocessRestoredIndexContextProto(_message.Message):
        __slots__ = ("archive_uid",)
        ARCHIVE_UID_FIELD_NUMBER: _ClassVar[int]
        archive_uid: _universal_id_pb2.UniversalIdProto
        def __init__(self, archive_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ...) -> None: ...
    class FixUpdateIntentsContextProto(_message.Message):
        __slots__ = ("min_key", "max_key")
        MIN_KEY_FIELD_NUMBER: _ClassVar[int]
        MAX_KEY_FIELD_NUMBER: _ClassVar[int]
        min_key: int
        max_key: int
        def __init__(self, min_key: _Optional[int] = ..., max_key: _Optional[int] = ...) -> None: ...
    class GetFilesToUploadContextProto(_message.Message):
        __slots__ = ("max_files_per_request", "cookie")
        MAX_FILES_PER_REQUEST_FIELD_NUMBER: _ClassVar[int]
        COOKIE_FIELD_NUMBER: _ClassVar[int]
        max_files_per_request: int
        cookie: _icebox_pb2.GetFilesToUploadCookieProto
        def __init__(self, max_files_per_request: _Optional[int] = ..., cookie: _Optional[_Union[_icebox_pb2.GetFilesToUploadCookieProto, _Mapping]] = ...) -> None: ...
    class UploadFilesContextProto(_message.Message):
        __slots__ = ("file_info_vec",)
        FILE_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
        file_info_vec: _containers.RepeatedCompositeFieldContainer[_icebox_pb2.FileInfoProto]
        def __init__(self, file_info_vec: _Optional[_Iterable[_Union[_icebox_pb2.FileInfoProto, _Mapping]]] = ...) -> None: ...
    class StubViewContextProto(_message.Message):
        __slots__ = ("entity_id", "snap_tree_range", "blob_data_ranges")
        ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
        SNAP_TREE_RANGE_FIELD_NUMBER: _ClassVar[int]
        BLOB_DATA_RANGES_FIELD_NUMBER: _ClassVar[int]
        entity_id: int
        snap_tree_range: SnapTreeKeyRange
        blob_data_ranges: _icebox_pb2.BlobDataRanges
        def __init__(self, entity_id: _Optional[int] = ..., snap_tree_range: _Optional[_Union[SnapTreeKeyRange, _Mapping]] = ..., blob_data_ranges: _Optional[_Union[_icebox_pb2.BlobDataRanges, _Mapping]] = ...) -> None: ...
    class UptierDataContextProto(_message.Message):
        __slots__ = ("entity_id", "internal_view_name", "dir_walker_cookie", "dir_walker_checkpoint_file_path", "object_info_dir_path", "approx_num_bytes_to_uptier", "max_files_to_uptier")
        ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
        INTERNAL_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
        DIR_WALKER_COOKIE_FIELD_NUMBER: _ClassVar[int]
        DIR_WALKER_CHECKPOINT_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
        OBJECT_INFO_DIR_PATH_FIELD_NUMBER: _ClassVar[int]
        APPROX_NUM_BYTES_TO_UPTIER_FIELD_NUMBER: _ClassVar[int]
        MAX_FILES_TO_UPTIER_FIELD_NUMBER: _ClassVar[int]
        entity_id: int
        internal_view_name: str
        dir_walker_cookie: _directory_walker_pb2.EntityMetadata
        dir_walker_checkpoint_file_path: str
        object_info_dir_path: str
        approx_num_bytes_to_uptier: int
        max_files_to_uptier: int
        def __init__(self, entity_id: _Optional[int] = ..., internal_view_name: _Optional[str] = ..., dir_walker_cookie: _Optional[_Union[_directory_walker_pb2.EntityMetadata, _Mapping]] = ..., dir_walker_checkpoint_file_path: _Optional[str] = ..., object_info_dir_path: _Optional[str] = ..., approx_num_bytes_to_uptier: _Optional[int] = ..., max_files_to_uptier: _Optional[int] = ...) -> None: ...
    class DowntierDataContextProto(_message.Message):
        __slots__ = ("internal_view_name", "object_info_dir_path_vec")
        INTERNAL_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
        OBJECT_INFO_DIR_PATH_VEC_FIELD_NUMBER: _ClassVar[int]
        internal_view_name: str
        object_info_dir_path_vec: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, internal_view_name: _Optional[str] = ..., object_info_dir_path_vec: _Optional[_Iterable[str]] = ...) -> None: ...
    class RestoreStubSnapTreesContextProto(_message.Message):
        __slots__ = ("stub_snap_tree_info_vec",)
        class StubSnapTreeInfo(_message.Message):
            __slots__ = ("snap_tree_id", "view_id", "entity_id", "tree_type", "root_name")
            SNAP_TREE_ID_FIELD_NUMBER: _ClassVar[int]
            VIEW_ID_FIELD_NUMBER: _ClassVar[int]
            ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
            TREE_TYPE_FIELD_NUMBER: _ClassVar[int]
            ROOT_NAME_FIELD_NUMBER: _ClassVar[int]
            snap_tree_id: int
            view_id: int
            entity_id: int
            tree_type: _icebox_pb2.IceboxSnapTreeType
            root_name: str
            def __init__(self, snap_tree_id: _Optional[int] = ..., view_id: _Optional[int] = ..., entity_id: _Optional[int] = ..., tree_type: _Optional[_Union[_icebox_pb2.IceboxSnapTreeType, str]] = ..., root_name: _Optional[str] = ...) -> None: ...
        STUB_SNAP_TREE_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
        stub_snap_tree_info_vec: _containers.RepeatedCompositeFieldContainer[TaskStateProto.RestoreStubSnapTreesContextProto.StubSnapTreeInfo]
        def __init__(self, stub_snap_tree_info_vec: _Optional[_Iterable[_Union[TaskStateProto.RestoreStubSnapTreesContextProto.StubSnapTreeInfo, _Mapping]]] = ...) -> None: ...
    class UptierCloudDomainFilesContextProto(_message.Message):
        __slots__ = ("file_restore_info", "stub_view_name", "internal_view_name", "dw_checkpoint_file_path")
        FILE_RESTORE_INFO_FIELD_NUMBER: _ClassVar[int]
        STUB_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
        INTERNAL_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
        DW_CHECKPOINT_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
        file_restore_info: _rpc_service_pb2.ScheduleRestoreJobArg.FileRestoreInfo
        stub_view_name: str
        internal_view_name: str
        dw_checkpoint_file_path: str
        def __init__(self, file_restore_info: _Optional[_Union[_rpc_service_pb2.ScheduleRestoreJobArg.FileRestoreInfo, _Mapping]] = ..., stub_view_name: _Optional[str] = ..., internal_view_name: _Optional[str] = ..., dw_checkpoint_file_path: _Optional[str] = ...) -> None: ...
    class ListVaultFSFilesContextProto(_message.Message):
        __slots__ = ("view_id", "fs_name", "set_archive_object_uid", "object_files_view_name", "object_files_fs_name", "object_files_dir_path", "root_dir_path")
        VIEW_ID_FIELD_NUMBER: _ClassVar[int]
        FS_NAME_FIELD_NUMBER: _ClassVar[int]
        SET_ARCHIVE_OBJECT_UID_FIELD_NUMBER: _ClassVar[int]
        OBJECT_FILES_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
        OBJECT_FILES_FS_NAME_FIELD_NUMBER: _ClassVar[int]
        OBJECT_FILES_DIR_PATH_FIELD_NUMBER: _ClassVar[int]
        ROOT_DIR_PATH_FIELD_NUMBER: _ClassVar[int]
        view_id: int
        fs_name: str
        set_archive_object_uid: bool
        object_files_view_name: str
        object_files_fs_name: str
        object_files_dir_path: str
        root_dir_path: str
        def __init__(self, view_id: _Optional[int] = ..., fs_name: _Optional[str] = ..., set_archive_object_uid: bool = ..., object_files_view_name: _Optional[str] = ..., object_files_fs_name: _Optional[str] = ..., object_files_dir_path: _Optional[str] = ..., root_dir_path: _Optional[str] = ...) -> None: ...
    class GetBlobsInfoContextProto(_message.Message):
        __slots__ = ("min_key", "max_key", "snap_tree_iter_cookie", "blob_info_cookie")
        MIN_KEY_FIELD_NUMBER: _ClassVar[int]
        MAX_KEY_FIELD_NUMBER: _ClassVar[int]
        SNAP_TREE_ITER_COOKIE_FIELD_NUMBER: _ClassVar[int]
        BLOB_INFO_COOKIE_FIELD_NUMBER: _ClassVar[int]
        min_key: int
        max_key: int
        snap_tree_iter_cookie: _icebox_pb2.SnapTreeIterCookieProto
        blob_info_cookie: _icebox_pb2.BlobInfo
        def __init__(self, min_key: _Optional[int] = ..., max_key: _Optional[int] = ..., snap_tree_iter_cookie: _Optional[_Union[_icebox_pb2.SnapTreeIterCookieProto, _Mapping]] = ..., blob_info_cookie: _Optional[_Union[_icebox_pb2.BlobInfo, _Mapping]] = ...) -> None: ...
    class DownloadSnapTreeObjectsContextProto(_message.Message):
        __slots__ = ("start_index", "end_index")
        START_INDEX_FIELD_NUMBER: _ClassVar[int]
        END_INDEX_FIELD_NUMBER: _ClassVar[int]
        start_index: int
        end_index: int
        def __init__(self, start_index: _Optional[int] = ..., end_index: _Optional[int] = ...) -> None: ...
    class CleanupObjectsContextProto(_message.Message):
        __slots__ = ("actions_file_vec",)
        ACTIONS_FILE_VEC_FIELD_NUMBER: _ClassVar[int]
        actions_file_vec: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, actions_file_vec: _Optional[_Iterable[str]] = ...) -> None: ...
    class ValidateObjectsContextProto(_message.Message):
        __slots__ = ("object_uid_vec", "actions")
        OBJECT_UID_VEC_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        object_uid_vec: _containers.RepeatedCompositeFieldContainer[_universal_id_pb2.UniversalIdProto]
        actions: _icebox_pb2.ObjectsValidationActions
        def __init__(self, object_uid_vec: _Optional[_Iterable[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]]] = ..., actions: _Optional[_Union[_icebox_pb2.ObjectsValidationActions, _Mapping]] = ...) -> None: ...
    class EvictObjectsContext(_message.Message):
        __slots__ = ("archive_object_uid_vec",)
        ARCHIVE_OBJECT_UID_VEC_FIELD_NUMBER: _ClassVar[int]
        archive_object_uid_vec: _containers.RepeatedCompositeFieldContainer[_universal_id_pb2.UniversalIdProto]
        def __init__(self, archive_object_uid_vec: _Optional[_Iterable[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]]] = ...) -> None: ...
    class TaskData(_message.Message):
        __slots__ = ("view_snap_tree_uid", "view_snap_tree_uid_vec", "size", "create_timestamp_usecs", "start_timestamp_usecs", "end_timestamp_usecs", "pause_timestamp_usecs", "last_stuck_timestamp_usecs", "total_wait_time_usecs", "constituent_id", "blob_info_vec", "checkpoint_info", "archive_object_metadata", "error", "current_logical_size_bytes", "current_physical_size_bytes", "parent_task_id_vec", "blob_count", "finalize_archive_objects_context", "read_archive_metadata_task_data", "register_app_job_metadata_context", "restore_dirs_context", "build_index_context", "archive_view_snap_trees_info", "postprocess_restored_index_context", "fix_update_intents_context", "get_files_to_upload_context", "upload_files_context", "stub_view_context", "vault_fs_files_context", "schedule_timestamp_usecs", "get_blobs_info_context", "download_objects_context", "cleanup_objects_context", "validate_objects_context", "evict_objects_context", "current_view_snap_tree_nodes", "uptier_data_context", "downtier_data_context", "restore_stub_snap_trees_context", "list_archive_metadata_task_data", "read_archive_metadata_from_csr_task_data", "uptier_cloud_domain_files_context", "populate_cloud_domain_scribe_entries_task_data")
        VIEW_SNAP_TREE_UID_FIELD_NUMBER: _ClassVar[int]
        VIEW_SNAP_TREE_UID_VEC_FIELD_NUMBER: _ClassVar[int]
        SIZE_FIELD_NUMBER: _ClassVar[int]
        CREATE_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
        START_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
        END_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
        PAUSE_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
        LAST_STUCK_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
        TOTAL_WAIT_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
        CONSTITUENT_ID_FIELD_NUMBER: _ClassVar[int]
        BLOB_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
        CHECKPOINT_INFO_FIELD_NUMBER: _ClassVar[int]
        ARCHIVE_OBJECT_METADATA_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        CURRENT_LOGICAL_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
        CURRENT_PHYSICAL_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
        PARENT_TASK_ID_VEC_FIELD_NUMBER: _ClassVar[int]
        BLOB_COUNT_FIELD_NUMBER: _ClassVar[int]
        FINALIZE_ARCHIVE_OBJECTS_CONTEXT_FIELD_NUMBER: _ClassVar[int]
        READ_ARCHIVE_METADATA_TASK_DATA_FIELD_NUMBER: _ClassVar[int]
        REGISTER_APP_JOB_METADATA_CONTEXT_FIELD_NUMBER: _ClassVar[int]
        RESTORE_DIRS_CONTEXT_FIELD_NUMBER: _ClassVar[int]
        BUILD_INDEX_CONTEXT_FIELD_NUMBER: _ClassVar[int]
        ARCHIVE_VIEW_SNAP_TREES_INFO_FIELD_NUMBER: _ClassVar[int]
        POSTPROCESS_RESTORED_INDEX_CONTEXT_FIELD_NUMBER: _ClassVar[int]
        FIX_UPDATE_INTENTS_CONTEXT_FIELD_NUMBER: _ClassVar[int]
        GET_FILES_TO_UPLOAD_CONTEXT_FIELD_NUMBER: _ClassVar[int]
        UPLOAD_FILES_CONTEXT_FIELD_NUMBER: _ClassVar[int]
        STUB_VIEW_CONTEXT_FIELD_NUMBER: _ClassVar[int]
        VAULT_FS_FILES_CONTEXT_FIELD_NUMBER: _ClassVar[int]
        SCHEDULE_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
        GET_BLOBS_INFO_CONTEXT_FIELD_NUMBER: _ClassVar[int]
        DOWNLOAD_OBJECTS_CONTEXT_FIELD_NUMBER: _ClassVar[int]
        CLEANUP_OBJECTS_CONTEXT_FIELD_NUMBER: _ClassVar[int]
        VALIDATE_OBJECTS_CONTEXT_FIELD_NUMBER: _ClassVar[int]
        EVICT_OBJECTS_CONTEXT_FIELD_NUMBER: _ClassVar[int]
        CURRENT_VIEW_SNAP_TREE_NODES_FIELD_NUMBER: _ClassVar[int]
        UPTIER_DATA_CONTEXT_FIELD_NUMBER: _ClassVar[int]
        DOWNTIER_DATA_CONTEXT_FIELD_NUMBER: _ClassVar[int]
        RESTORE_STUB_SNAP_TREES_CONTEXT_FIELD_NUMBER: _ClassVar[int]
        LIST_ARCHIVE_METADATA_TASK_DATA_FIELD_NUMBER: _ClassVar[int]
        READ_ARCHIVE_METADATA_FROM_CSR_TASK_DATA_FIELD_NUMBER: _ClassVar[int]
        UPTIER_CLOUD_DOMAIN_FILES_CONTEXT_FIELD_NUMBER: _ClassVar[int]
        POPULATE_CLOUD_DOMAIN_SCRIBE_ENTRIES_TASK_DATA_FIELD_NUMBER: _ClassVar[int]
        view_snap_tree_uid: _universal_id_pb2.UniversalIdProto
        view_snap_tree_uid_vec: _containers.RepeatedCompositeFieldContainer[_universal_id_pb2.UniversalIdProto]
        size: int
        create_timestamp_usecs: int
        start_timestamp_usecs: int
        end_timestamp_usecs: int
        pause_timestamp_usecs: int
        last_stuck_timestamp_usecs: int
        total_wait_time_usecs: int
        constituent_id: int
        blob_info_vec: _containers.RepeatedCompositeFieldContainer[_icebox_pb2.BlobInfo]
        checkpoint_info: _icebox_pb2.TaskCheckpointInfo
        archive_object_metadata: _icebox_pb2.ArchiveObjectScribeMetadataProto
        error: _error_pb2.ErrorProto
        current_logical_size_bytes: int
        current_physical_size_bytes: int
        parent_task_id_vec: _containers.RepeatedScalarFieldContainer[int]
        blob_count: int
        finalize_archive_objects_context: TaskStateProto.FinalizeArchiveObjectsContextProto
        read_archive_metadata_task_data: ReadArchiveMetadataTaskData
        register_app_job_metadata_context: TaskStateProto.RegisterAppJobMetadataTaskContextProto
        restore_dirs_context: TaskStateProto.RestoreDirectoriesTaskContextProto
        build_index_context: TaskStateProto.BuildIndexTaskContextProto
        archive_view_snap_trees_info: ArchiveViewSnapTreesContext.ViewInfo
        postprocess_restored_index_context: TaskStateProto.PostprocessRestoredIndexContextProto
        fix_update_intents_context: TaskStateProto.FixUpdateIntentsContextProto
        get_files_to_upload_context: TaskStateProto.GetFilesToUploadContextProto
        upload_files_context: TaskStateProto.UploadFilesContextProto
        stub_view_context: TaskStateProto.StubViewContextProto
        vault_fs_files_context: TaskStateProto.ListVaultFSFilesContextProto
        schedule_timestamp_usecs: int
        get_blobs_info_context: TaskStateProto.GetBlobsInfoContextProto
        download_objects_context: TaskStateProto.DownloadSnapTreeObjectsContextProto
        cleanup_objects_context: TaskStateProto.CleanupObjectsContextProto
        validate_objects_context: TaskStateProto.ValidateObjectsContextProto
        evict_objects_context: TaskStateProto.EvictObjectsContext
        current_view_snap_tree_nodes: int
        uptier_data_context: TaskStateProto.UptierDataContextProto
        downtier_data_context: TaskStateProto.DowntierDataContextProto
        restore_stub_snap_trees_context: TaskStateProto.RestoreStubSnapTreesContextProto
        list_archive_metadata_task_data: _icebox_pb2.CloudDomainAccessInfo
        read_archive_metadata_from_csr_task_data: ReadArchiveMetadataFromCSRTaskData
        uptier_cloud_domain_files_context: TaskStateProto.UptierCloudDomainFilesContextProto
        populate_cloud_domain_scribe_entries_task_data: PopulateCloudDomainScribeEntriesTaskData
        def __init__(self, view_snap_tree_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., view_snap_tree_uid_vec: _Optional[_Iterable[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]]] = ..., size: _Optional[int] = ..., create_timestamp_usecs: _Optional[int] = ..., start_timestamp_usecs: _Optional[int] = ..., end_timestamp_usecs: _Optional[int] = ..., pause_timestamp_usecs: _Optional[int] = ..., last_stuck_timestamp_usecs: _Optional[int] = ..., total_wait_time_usecs: _Optional[int] = ..., constituent_id: _Optional[int] = ..., blob_info_vec: _Optional[_Iterable[_Union[_icebox_pb2.BlobInfo, _Mapping]]] = ..., checkpoint_info: _Optional[_Union[_icebox_pb2.TaskCheckpointInfo, _Mapping]] = ..., archive_object_metadata: _Optional[_Union[_icebox_pb2.ArchiveObjectScribeMetadataProto, _Mapping]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., current_logical_size_bytes: _Optional[int] = ..., current_physical_size_bytes: _Optional[int] = ..., parent_task_id_vec: _Optional[_Iterable[int]] = ..., blob_count: _Optional[int] = ..., finalize_archive_objects_context: _Optional[_Union[TaskStateProto.FinalizeArchiveObjectsContextProto, _Mapping]] = ..., read_archive_metadata_task_data: _Optional[_Union[ReadArchiveMetadataTaskData, _Mapping]] = ..., register_app_job_metadata_context: _Optional[_Union[TaskStateProto.RegisterAppJobMetadataTaskContextProto, _Mapping]] = ..., restore_dirs_context: _Optional[_Union[TaskStateProto.RestoreDirectoriesTaskContextProto, _Mapping]] = ..., build_index_context: _Optional[_Union[TaskStateProto.BuildIndexTaskContextProto, _Mapping]] = ..., archive_view_snap_trees_info: _Optional[_Union[ArchiveViewSnapTreesContext.ViewInfo, _Mapping]] = ..., postprocess_restored_index_context: _Optional[_Union[TaskStateProto.PostprocessRestoredIndexContextProto, _Mapping]] = ..., fix_update_intents_context: _Optional[_Union[TaskStateProto.FixUpdateIntentsContextProto, _Mapping]] = ..., get_files_to_upload_context: _Optional[_Union[TaskStateProto.GetFilesToUploadContextProto, _Mapping]] = ..., upload_files_context: _Optional[_Union[TaskStateProto.UploadFilesContextProto, _Mapping]] = ..., stub_view_context: _Optional[_Union[TaskStateProto.StubViewContextProto, _Mapping]] = ..., vault_fs_files_context: _Optional[_Union[TaskStateProto.ListVaultFSFilesContextProto, _Mapping]] = ..., schedule_timestamp_usecs: _Optional[int] = ..., get_blobs_info_context: _Optional[_Union[TaskStateProto.GetBlobsInfoContextProto, _Mapping]] = ..., download_objects_context: _Optional[_Union[TaskStateProto.DownloadSnapTreeObjectsContextProto, _Mapping]] = ..., cleanup_objects_context: _Optional[_Union[TaskStateProto.CleanupObjectsContextProto, _Mapping]] = ..., validate_objects_context: _Optional[_Union[TaskStateProto.ValidateObjectsContextProto, _Mapping]] = ..., evict_objects_context: _Optional[_Union[TaskStateProto.EvictObjectsContext, _Mapping]] = ..., current_view_snap_tree_nodes: _Optional[int] = ..., uptier_data_context: _Optional[_Union[TaskStateProto.UptierDataContextProto, _Mapping]] = ..., downtier_data_context: _Optional[_Union[TaskStateProto.DowntierDataContextProto, _Mapping]] = ..., restore_stub_snap_trees_context: _Optional[_Union[TaskStateProto.RestoreStubSnapTreesContextProto, _Mapping]] = ..., list_archive_metadata_task_data: _Optional[_Union[_icebox_pb2.CloudDomainAccessInfo, _Mapping]] = ..., read_archive_metadata_from_csr_task_data: _Optional[_Union[ReadArchiveMetadataFromCSRTaskData, _Mapping]] = ..., uptier_cloud_domain_files_context: _Optional[_Union[TaskStateProto.UptierCloudDomainFilesContextProto, _Mapping]] = ..., populate_cloud_domain_scribe_entries_task_data: _Optional[_Union[PopulateCloudDomainScribeEntriesTaskData, _Mapping]] = ...) -> None: ...
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    TASK_DATA_FIELD_NUMBER: _ClassVar[int]
    HYDRATION_START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    HYDRATION_END_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    IS_ALLOTTED_ON_EXTRA_SLOT_FIELD_NUMBER: _ClassVar[int]
    TASK_PRIORITY_FIELD_NUMBER: _ClassVar[int]
    CRASHING_CONSTITUENT_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    task_id: int
    state: _icebox_pb2.IceboxJobStatus
    type: TaskStateProto.TaskType
    task_data: TaskStateProto.TaskData
    hydration_start_time_usecs: int
    hydration_end_time_usecs: int
    is_allotted_on_extra_slot: bool
    task_priority: TaskStateProto.TaskPriority
    crashing_constituent_id_vec: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, task_id: _Optional[int] = ..., state: _Optional[_Union[_icebox_pb2.IceboxJobStatus, str]] = ..., type: _Optional[_Union[TaskStateProto.TaskType, str]] = ..., task_data: _Optional[_Union[TaskStateProto.TaskData, _Mapping]] = ..., hydration_start_time_usecs: _Optional[int] = ..., hydration_end_time_usecs: _Optional[int] = ..., is_allotted_on_extra_slot: bool = ..., task_priority: _Optional[_Union[TaskStateProto.TaskPriority, str]] = ..., crashing_constituent_id_vec: _Optional[_Iterable[int]] = ...) -> None: ...

class WORMStats(_message.Message):
    __slots__ = ("num_nodes_visited_for_msr", "num_cloud_chunk_files_retention_extended", "num_csr_objects_retention_extended", "num_data_bytes_rearchived", "num_snap_tree_nodes_rearchived")
    NUM_NODES_VISITED_FOR_MSR_FIELD_NUMBER: _ClassVar[int]
    NUM_CLOUD_CHUNK_FILES_RETENTION_EXTENDED_FIELD_NUMBER: _ClassVar[int]
    NUM_CSR_OBJECTS_RETENTION_EXTENDED_FIELD_NUMBER: _ClassVar[int]
    NUM_DATA_BYTES_REARCHIVED_FIELD_NUMBER: _ClassVar[int]
    NUM_SNAP_TREE_NODES_REARCHIVED_FIELD_NUMBER: _ClassVar[int]
    num_nodes_visited_for_msr: int
    num_cloud_chunk_files_retention_extended: int
    num_csr_objects_retention_extended: int
    num_data_bytes_rearchived: int
    num_snap_tree_nodes_rearchived: int
    def __init__(self, num_nodes_visited_for_msr: _Optional[int] = ..., num_cloud_chunk_files_retention_extended: _Optional[int] = ..., num_csr_objects_retention_extended: _Optional[int] = ..., num_data_bytes_rearchived: _Optional[int] = ..., num_snap_tree_nodes_rearchived: _Optional[int] = ...) -> None: ...

class JobStateProto(_message.Message):
    __slots__ = ("job_uid", "archival_job_arg", "restore_job_arg", "archive_metadata", "checkpoint_info", "constituent_info", "removal_state", "job_status", "error", "archive_object_scribe_metadata", "end_timestamp_usecs", "archive_uid", "app_notification_pending", "expiry_timestamp_usecs", "restore_job_metadata", "pause_timestamp_usecs", "total_wait_time_usecs", "view_snap_tree_state_vec", "task_state_vec", "archive_object_metadata_vec", "checkpoint_object_metadata_vec", "task_id_gen", "create_timestamp_usecs", "view_id", "version", "dedup_enabled", "progress_monitor_root_path", "job_start_op_clock", "vault_type", "prev_archive_node_id_floor", "archive_type_reason", "last_progress_time_usecs", "job_type", "search_job_context", "job_name", "vault_id", "flush_data_journal_at_master", "viewbox_id", "batch_job_context", "restore_index_job_context", "parent_job_uid", "restoring_to_alternate_cluster", "application_name", "start_timestamp_usecs", "restore_job_context", "entity_metadata", "archive_view_snap_trees_context", "entity_internal_view_name_map", "stats", "stub_view_job_context", "view_name", "earliest_entity_expiry_time_usecs", "full_archive_for_nfoi", "being_finalized_object_uid_vec", "vault_params", "enabled_feature_vec", "use_node_id_floor_to_determine_incremental_archives", "da_gc_job_context", "da_job_context", "fs_walk_context", "validate_objects_context", "num_da_objects_deleted", "num_padded_bytes", "epoch_id", "reset_job_info", "full_for_missing_files_report_mode", "full_for_missing_files_repair_mode", "is_forever_incremental_archive", "domain_migration_job_context", "job_status_finish_times_map", "archive_worm_properties", "should_validate", "task_id_to_num_chunks_yet_to_be_finalized_map", "user_info", "stuck_timestamp_usecs", "job_priority", "unusable_non_finalized_object_data_vec", "enable_fetb_calculation", "domain_rebuild_job_context", "worm_object_lock_requested", "is_rpaas_job", "worm_retention_timestamp_usecs", "target_worm_retention_timestamp_usecs", "worm_retention_mode", "base_view_id", "cloud_tier_type", "archive_worm_stats", "restore_object_data_vec", "restored_object_uid_vec", "force_full_traversal_for_frontend_size_info", "worm_stats")
    class JobPriority(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kLow: _ClassVar[JobStateProto.JobPriority]
        kMedium: _ClassVar[JobStateProto.JobPriority]
        kHigh: _ClassVar[JobStateProto.JobPriority]
    kLow: JobStateProto.JobPriority
    kMedium: JobStateProto.JobPriority
    kHigh: JobStateProto.JobPriority
    class EntityInternalViewNameMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: str
        def __init__(self, key: _Optional[int] = ..., value: _Optional[str] = ...) -> None: ...
    class Stats(_message.Message):
        __slots__ = ("logical_size_bytes", "physical_size_bytes", "num_files_found", "total_view_snap_tree_nodes_to_be_archived", "num_files_restored", "num_view_snap_tree_nodes", "num_da_files_archived", "num_logical_bytes_uptiered")
        LOGICAL_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
        PHYSICAL_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
        NUM_FILES_FOUND_FIELD_NUMBER: _ClassVar[int]
        TOTAL_VIEW_SNAP_TREE_NODES_TO_BE_ARCHIVED_FIELD_NUMBER: _ClassVar[int]
        NUM_FILES_RESTORED_FIELD_NUMBER: _ClassVar[int]
        NUM_VIEW_SNAP_TREE_NODES_FIELD_NUMBER: _ClassVar[int]
        NUM_DA_FILES_ARCHIVED_FIELD_NUMBER: _ClassVar[int]
        NUM_LOGICAL_BYTES_UPTIERED_FIELD_NUMBER: _ClassVar[int]
        logical_size_bytes: int
        physical_size_bytes: int
        num_files_found: int
        total_view_snap_tree_nodes_to_be_archived: int
        num_files_restored: int
        num_view_snap_tree_nodes: int
        num_da_files_archived: int
        num_logical_bytes_uptiered: int
        def __init__(self, logical_size_bytes: _Optional[int] = ..., physical_size_bytes: _Optional[int] = ..., num_files_found: _Optional[int] = ..., total_view_snap_tree_nodes_to_be_archived: _Optional[int] = ..., num_files_restored: _Optional[int] = ..., num_view_snap_tree_nodes: _Optional[int] = ..., num_da_files_archived: _Optional[int] = ..., num_logical_bytes_uptiered: _Optional[int] = ...) -> None: ...
    class ResetJobInfo(_message.Message):
        __slots__ = ("attempt_num", "is_reset_pending", "prev_job_status")
        ATTEMPT_NUM_FIELD_NUMBER: _ClassVar[int]
        IS_RESET_PENDING_FIELD_NUMBER: _ClassVar[int]
        PREV_JOB_STATUS_FIELD_NUMBER: _ClassVar[int]
        attempt_num: int
        is_reset_pending: bool
        prev_job_status: _icebox_pb2.IceboxJobStatus
        def __init__(self, attempt_num: _Optional[int] = ..., is_reset_pending: bool = ..., prev_job_status: _Optional[_Union[_icebox_pb2.IceboxJobStatus, str]] = ...) -> None: ...
    class JobStatusFinishTimesMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    class TaskIdToNumChunksYetToBeFinalizedMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    JOB_UID_FIELD_NUMBER: _ClassVar[int]
    ARCHIVAL_JOB_ARG_FIELD_NUMBER: _ClassVar[int]
    RESTORE_JOB_ARG_FIELD_NUMBER: _ClassVar[int]
    ARCHIVE_METADATA_FIELD_NUMBER: _ClassVar[int]
    CHECKPOINT_INFO_FIELD_NUMBER: _ClassVar[int]
    CONSTITUENT_INFO_FIELD_NUMBER: _ClassVar[int]
    REMOVAL_STATE_FIELD_NUMBER: _ClassVar[int]
    JOB_STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ARCHIVE_OBJECT_SCRIBE_METADATA_FIELD_NUMBER: _ClassVar[int]
    END_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
    ARCHIVE_UID_FIELD_NUMBER: _ClassVar[int]
    APP_NOTIFICATION_PENDING_FIELD_NUMBER: _ClassVar[int]
    EXPIRY_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
    RESTORE_JOB_METADATA_FIELD_NUMBER: _ClassVar[int]
    PAUSE_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_WAIT_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    VIEW_SNAP_TREE_STATE_VEC_FIELD_NUMBER: _ClassVar[int]
    TASK_STATE_VEC_FIELD_NUMBER: _ClassVar[int]
    ARCHIVE_OBJECT_METADATA_VEC_FIELD_NUMBER: _ClassVar[int]
    CHECKPOINT_OBJECT_METADATA_VEC_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_GEN_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
    VIEW_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    DEDUP_ENABLED_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_MONITOR_ROOT_PATH_FIELD_NUMBER: _ClassVar[int]
    JOB_START_OP_CLOCK_FIELD_NUMBER: _ClassVar[int]
    VAULT_TYPE_FIELD_NUMBER: _ClassVar[int]
    PREV_ARCHIVE_NODE_ID_FLOOR_FIELD_NUMBER: _ClassVar[int]
    ARCHIVE_TYPE_REASON_FIELD_NUMBER: _ClassVar[int]
    LAST_PROGRESS_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    JOB_TYPE_FIELD_NUMBER: _ClassVar[int]
    SEARCH_JOB_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    JOB_NAME_FIELD_NUMBER: _ClassVar[int]
    VAULT_ID_FIELD_NUMBER: _ClassVar[int]
    FLUSH_DATA_JOURNAL_AT_MASTER_FIELD_NUMBER: _ClassVar[int]
    VIEWBOX_ID_FIELD_NUMBER: _ClassVar[int]
    BATCH_JOB_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    RESTORE_INDEX_JOB_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    PARENT_JOB_UID_FIELD_NUMBER: _ClassVar[int]
    RESTORING_TO_ALTERNATE_CLUSTER_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_NAME_FIELD_NUMBER: _ClassVar[int]
    START_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
    RESTORE_JOB_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    ENTITY_METADATA_FIELD_NUMBER: _ClassVar[int]
    ARCHIVE_VIEW_SNAP_TREES_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    ENTITY_INTERNAL_VIEW_NAME_MAP_FIELD_NUMBER: _ClassVar[int]
    STATS_FIELD_NUMBER: _ClassVar[int]
    STUB_VIEW_JOB_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    EARLIEST_ENTITY_EXPIRY_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    FULL_ARCHIVE_FOR_NFOI_FIELD_NUMBER: _ClassVar[int]
    BEING_FINALIZED_OBJECT_UID_VEC_FIELD_NUMBER: _ClassVar[int]
    VAULT_PARAMS_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FEATURE_VEC_FIELD_NUMBER: _ClassVar[int]
    USE_NODE_ID_FLOOR_TO_DETERMINE_INCREMENTAL_ARCHIVES_FIELD_NUMBER: _ClassVar[int]
    DA_GC_JOB_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    DA_JOB_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    FS_WALK_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_OBJECTS_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    NUM_DA_OBJECTS_DELETED_FIELD_NUMBER: _ClassVar[int]
    NUM_PADDED_BYTES_FIELD_NUMBER: _ClassVar[int]
    EPOCH_ID_FIELD_NUMBER: _ClassVar[int]
    RESET_JOB_INFO_FIELD_NUMBER: _ClassVar[int]
    FULL_FOR_MISSING_FILES_REPORT_MODE_FIELD_NUMBER: _ClassVar[int]
    FULL_FOR_MISSING_FILES_REPAIR_MODE_FIELD_NUMBER: _ClassVar[int]
    IS_FOREVER_INCREMENTAL_ARCHIVE_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_MIGRATION_JOB_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    JOB_STATUS_FINISH_TIMES_MAP_FIELD_NUMBER: _ClassVar[int]
    ARCHIVE_WORM_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    SHOULD_VALIDATE_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_TO_NUM_CHUNKS_YET_TO_BE_FINALIZED_MAP_FIELD_NUMBER: _ClassVar[int]
    USER_INFO_FIELD_NUMBER: _ClassVar[int]
    STUCK_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
    JOB_PRIORITY_FIELD_NUMBER: _ClassVar[int]
    UNUSABLE_NON_FINALIZED_OBJECT_DATA_VEC_FIELD_NUMBER: _ClassVar[int]
    ENABLE_FETB_CALCULATION_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_REBUILD_JOB_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    WORM_OBJECT_LOCK_REQUESTED_FIELD_NUMBER: _ClassVar[int]
    IS_RPAAS_JOB_FIELD_NUMBER: _ClassVar[int]
    WORM_RETENTION_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
    TARGET_WORM_RETENTION_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
    WORM_RETENTION_MODE_FIELD_NUMBER: _ClassVar[int]
    BASE_VIEW_ID_FIELD_NUMBER: _ClassVar[int]
    CLOUD_TIER_TYPE_FIELD_NUMBER: _ClassVar[int]
    ARCHIVE_WORM_STATS_FIELD_NUMBER: _ClassVar[int]
    RESTORE_OBJECT_DATA_VEC_FIELD_NUMBER: _ClassVar[int]
    RESTORED_OBJECT_UID_VEC_FIELD_NUMBER: _ClassVar[int]
    FORCE_FULL_TRAVERSAL_FOR_FRONTEND_SIZE_INFO_FIELD_NUMBER: _ClassVar[int]
    WORM_STATS_FIELD_NUMBER: _ClassVar[int]
    job_uid: _universal_id_pb2.UniversalIdProto
    archival_job_arg: _rpc_service_pb2.ScheduleArchivalJobArg
    restore_job_arg: _rpc_service_pb2.ScheduleRestoreJobArg
    archive_metadata: _icebox_pb2.ArchiveMetadataProto
    checkpoint_info: _icebox_pb2.TaskCheckpointInfo
    constituent_info: ConstituentInfoProto
    removal_state: _cluster_config_pb2.ClusterConfigProto.RemovalState
    job_status: _icebox_pb2.IceboxJobStatus
    error: _error_pb2.ErrorProto
    archive_object_scribe_metadata: _icebox_pb2.ArchiveObjectScribeMetadataProto
    end_timestamp_usecs: int
    archive_uid: _universal_id_pb2.UniversalIdProto
    app_notification_pending: bool
    expiry_timestamp_usecs: int
    restore_job_metadata: _icebox_pb2.RestoreJobMetadataProto
    pause_timestamp_usecs: int
    total_wait_time_usecs: int
    view_snap_tree_state_vec: _containers.RepeatedCompositeFieldContainer[ViewSnapTreeStateProto]
    task_state_vec: _containers.RepeatedCompositeFieldContainer[TaskStateProto]
    archive_object_metadata_vec: _containers.RepeatedCompositeFieldContainer[_icebox_pb2.ArchiveObjectScribeMetadataProto]
    checkpoint_object_metadata_vec: _containers.RepeatedCompositeFieldContainer[_icebox_pb2.TaskCheckpointInfo.ObjectData]
    task_id_gen: int
    create_timestamp_usecs: int
    view_id: int
    version: int
    dedup_enabled: bool
    progress_monitor_root_path: str
    job_start_op_clock: _op_clock_pb2.OpClock
    vault_type: _cluster_config_pb2.ClusterConfigProto.Vault.Type
    prev_archive_node_id_floor: int
    archive_type_reason: str
    last_progress_time_usecs: int
    job_type: _icebox_pb2.IceboxJobType
    search_job_context: SearchJobContextProto
    job_name: str
    vault_id: int
    flush_data_journal_at_master: bool
    viewbox_id: int
    batch_job_context: BatchJobContextProto
    restore_index_job_context: RestoreIndexJobContextProto
    parent_job_uid: _universal_id_pb2.UniversalIdProto
    restoring_to_alternate_cluster: bool
    application_name: str
    start_timestamp_usecs: int
    restore_job_context: RestoreJobContext
    entity_metadata: _icebox_pb2.EntityMetadataProto
    archive_view_snap_trees_context: ArchiveViewSnapTreesContext
    entity_internal_view_name_map: _containers.ScalarMap[int, str]
    stats: JobStateProto.Stats
    stub_view_job_context: StubViewJobContextProto
    view_name: str
    earliest_entity_expiry_time_usecs: int
    full_archive_for_nfoi: bool
    being_finalized_object_uid_vec: _containers.RepeatedCompositeFieldContainer[_universal_id_pb2.UniversalIdProto]
    vault_params: _vault_pb2.VaultParams
    enabled_feature_vec: _containers.RepeatedScalarFieldContainer[int]
    use_node_id_floor_to_determine_incremental_archives: bool
    da_gc_job_context: DirectArchiveGCJobContext
    da_job_context: DirectArchiveJobContext
    fs_walk_context: FSWalkContext
    validate_objects_context: ValidateObjectsContext
    num_da_objects_deleted: int
    num_padded_bytes: int
    epoch_id: int
    reset_job_info: JobStateProto.ResetJobInfo
    full_for_missing_files_report_mode: bool
    full_for_missing_files_repair_mode: bool
    is_forever_incremental_archive: bool
    domain_migration_job_context: DomainMigrationJobContextProto
    job_status_finish_times_map: _containers.ScalarMap[str, int]
    archive_worm_properties: _worm_pb2_1.ArchiveWORMProperties
    should_validate: bool
    task_id_to_num_chunks_yet_to_be_finalized_map: _containers.ScalarMap[int, int]
    user_info: _permissions_pb2.UserInformation
    stuck_timestamp_usecs: int
    job_priority: JobStateProto.JobPriority
    unusable_non_finalized_object_data_vec: _containers.RepeatedCompositeFieldContainer[_icebox_pb2.TaskCheckpointInfo.ObjectData]
    enable_fetb_calculation: bool
    domain_rebuild_job_context: CloudDomainRebuildJobContextProto
    worm_object_lock_requested: bool
    is_rpaas_job: bool
    worm_retention_timestamp_usecs: int
    target_worm_retention_timestamp_usecs: int
    worm_retention_mode: _worm_pb2.RetentionMode.Type
    base_view_id: int
    cloud_tier_type: _cluster_config_pb2.ClusterConfigProto.Vault.CloudTierType
    archive_worm_stats: _icebox_pb2.ArchiveWORMStats
    restore_object_data_vec: _containers.RepeatedCompositeFieldContainer[_icebox_pb2.TaskCheckpointInfo.RestoreObjectData]
    restored_object_uid_vec: _containers.RepeatedCompositeFieldContainer[_universal_id_pb2.UniversalIdProto]
    force_full_traversal_for_frontend_size_info: bool
    worm_stats: WORMStats
    def __init__(self, job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., archival_job_arg: _Optional[_Union[_rpc_service_pb2.ScheduleArchivalJobArg, _Mapping]] = ..., restore_job_arg: _Optional[_Union[_rpc_service_pb2.ScheduleRestoreJobArg, _Mapping]] = ..., archive_metadata: _Optional[_Union[_icebox_pb2.ArchiveMetadataProto, _Mapping]] = ..., checkpoint_info: _Optional[_Union[_icebox_pb2.TaskCheckpointInfo, _Mapping]] = ..., constituent_info: _Optional[_Union[ConstituentInfoProto, _Mapping]] = ..., removal_state: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.RemovalState, _Mapping]] = ..., job_status: _Optional[_Union[_icebox_pb2.IceboxJobStatus, str]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., archive_object_scribe_metadata: _Optional[_Union[_icebox_pb2.ArchiveObjectScribeMetadataProto, _Mapping]] = ..., end_timestamp_usecs: _Optional[int] = ..., archive_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., app_notification_pending: bool = ..., expiry_timestamp_usecs: _Optional[int] = ..., restore_job_metadata: _Optional[_Union[_icebox_pb2.RestoreJobMetadataProto, _Mapping]] = ..., pause_timestamp_usecs: _Optional[int] = ..., total_wait_time_usecs: _Optional[int] = ..., view_snap_tree_state_vec: _Optional[_Iterable[_Union[ViewSnapTreeStateProto, _Mapping]]] = ..., task_state_vec: _Optional[_Iterable[_Union[TaskStateProto, _Mapping]]] = ..., archive_object_metadata_vec: _Optional[_Iterable[_Union[_icebox_pb2.ArchiveObjectScribeMetadataProto, _Mapping]]] = ..., checkpoint_object_metadata_vec: _Optional[_Iterable[_Union[_icebox_pb2.TaskCheckpointInfo.ObjectData, _Mapping]]] = ..., task_id_gen: _Optional[int] = ..., create_timestamp_usecs: _Optional[int] = ..., view_id: _Optional[int] = ..., version: _Optional[int] = ..., dedup_enabled: bool = ..., progress_monitor_root_path: _Optional[str] = ..., job_start_op_clock: _Optional[_Union[_op_clock_pb2.OpClock, _Mapping]] = ..., vault_type: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.Vault.Type, str]] = ..., prev_archive_node_id_floor: _Optional[int] = ..., archive_type_reason: _Optional[str] = ..., last_progress_time_usecs: _Optional[int] = ..., job_type: _Optional[_Union[_icebox_pb2.IceboxJobType, str]] = ..., search_job_context: _Optional[_Union[SearchJobContextProto, _Mapping]] = ..., job_name: _Optional[str] = ..., vault_id: _Optional[int] = ..., flush_data_journal_at_master: bool = ..., viewbox_id: _Optional[int] = ..., batch_job_context: _Optional[_Union[BatchJobContextProto, _Mapping]] = ..., restore_index_job_context: _Optional[_Union[RestoreIndexJobContextProto, _Mapping]] = ..., parent_job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., restoring_to_alternate_cluster: bool = ..., application_name: _Optional[str] = ..., start_timestamp_usecs: _Optional[int] = ..., restore_job_context: _Optional[_Union[RestoreJobContext, _Mapping]] = ..., entity_metadata: _Optional[_Union[_icebox_pb2.EntityMetadataProto, _Mapping]] = ..., archive_view_snap_trees_context: _Optional[_Union[ArchiveViewSnapTreesContext, _Mapping]] = ..., entity_internal_view_name_map: _Optional[_Mapping[int, str]] = ..., stats: _Optional[_Union[JobStateProto.Stats, _Mapping]] = ..., stub_view_job_context: _Optional[_Union[StubViewJobContextProto, _Mapping]] = ..., view_name: _Optional[str] = ..., earliest_entity_expiry_time_usecs: _Optional[int] = ..., full_archive_for_nfoi: bool = ..., being_finalized_object_uid_vec: _Optional[_Iterable[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]]] = ..., vault_params: _Optional[_Union[_vault_pb2.VaultParams, _Mapping]] = ..., enabled_feature_vec: _Optional[_Iterable[int]] = ..., use_node_id_floor_to_determine_incremental_archives: bool = ..., da_gc_job_context: _Optional[_Union[DirectArchiveGCJobContext, _Mapping]] = ..., da_job_context: _Optional[_Union[DirectArchiveJobContext, _Mapping]] = ..., fs_walk_context: _Optional[_Union[FSWalkContext, _Mapping]] = ..., validate_objects_context: _Optional[_Union[ValidateObjectsContext, _Mapping]] = ..., num_da_objects_deleted: _Optional[int] = ..., num_padded_bytes: _Optional[int] = ..., epoch_id: _Optional[int] = ..., reset_job_info: _Optional[_Union[JobStateProto.ResetJobInfo, _Mapping]] = ..., full_for_missing_files_report_mode: bool = ..., full_for_missing_files_repair_mode: bool = ..., is_forever_incremental_archive: bool = ..., domain_migration_job_context: _Optional[_Union[DomainMigrationJobContextProto, _Mapping]] = ..., job_status_finish_times_map: _Optional[_Mapping[str, int]] = ..., archive_worm_properties: _Optional[_Union[_worm_pb2_1.ArchiveWORMProperties, _Mapping]] = ..., should_validate: bool = ..., task_id_to_num_chunks_yet_to_be_finalized_map: _Optional[_Mapping[int, int]] = ..., user_info: _Optional[_Union[_permissions_pb2.UserInformation, _Mapping]] = ..., stuck_timestamp_usecs: _Optional[int] = ..., job_priority: _Optional[_Union[JobStateProto.JobPriority, str]] = ..., unusable_non_finalized_object_data_vec: _Optional[_Iterable[_Union[_icebox_pb2.TaskCheckpointInfo.ObjectData, _Mapping]]] = ..., enable_fetb_calculation: bool = ..., domain_rebuild_job_context: _Optional[_Union[CloudDomainRebuildJobContextProto, _Mapping]] = ..., worm_object_lock_requested: bool = ..., is_rpaas_job: bool = ..., worm_retention_timestamp_usecs: _Optional[int] = ..., target_worm_retention_timestamp_usecs: _Optional[int] = ..., worm_retention_mode: _Optional[_Union[_worm_pb2.RetentionMode.Type, str]] = ..., base_view_id: _Optional[int] = ..., cloud_tier_type: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.Vault.CloudTierType, _Mapping]] = ..., archive_worm_stats: _Optional[_Union[_icebox_pb2.ArchiveWORMStats, _Mapping]] = ..., restore_object_data_vec: _Optional[_Iterable[_Union[_icebox_pb2.TaskCheckpointInfo.RestoreObjectData, _Mapping]]] = ..., restored_object_uid_vec: _Optional[_Iterable[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]]] = ..., force_full_traversal_for_frontend_size_info: bool = ..., worm_stats: _Optional[_Union[WORMStats, _Mapping]] = ...) -> None: ...

class EntityRestoreIdProto(_message.Message):
    __slots__ = ("viewbox_id", "archive_uid", "entity_id")
    VIEWBOX_ID_FIELD_NUMBER: _ClassVar[int]
    ARCHIVE_UID_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    viewbox_id: int
    archive_uid: _universal_id_pb2.UniversalIdProto
    entity_id: int
    def __init__(self, viewbox_id: _Optional[int] = ..., archive_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., entity_id: _Optional[int] = ...) -> None: ...

class EntityRestoreStateProto(_message.Message):
    __slots__ = ("id", "status", "removal_state", "restore_job_uid", "referring_restore_job_vec", "expiry_timestamp_usecs", "end_timestamp_usecs", "file_system_name", "is_view_fs_entity")
    ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    REMOVAL_STATE_FIELD_NUMBER: _ClassVar[int]
    RESTORE_JOB_UID_FIELD_NUMBER: _ClassVar[int]
    REFERRING_RESTORE_JOB_VEC_FIELD_NUMBER: _ClassVar[int]
    EXPIRY_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
    END_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
    FILE_SYSTEM_NAME_FIELD_NUMBER: _ClassVar[int]
    IS_VIEW_FS_ENTITY_FIELD_NUMBER: _ClassVar[int]
    id: EntityRestoreIdProto
    status: _icebox_pb2.IceboxJobStatus
    removal_state: _cluster_config_pb2.ClusterConfigProto.RemovalState
    restore_job_uid: _universal_id_pb2.UniversalIdProto
    referring_restore_job_vec: _containers.RepeatedCompositeFieldContainer[_universal_id_pb2.UniversalIdProto]
    expiry_timestamp_usecs: int
    end_timestamp_usecs: int
    file_system_name: str
    is_view_fs_entity: bool
    def __init__(self, id: _Optional[_Union[EntityRestoreIdProto, _Mapping]] = ..., status: _Optional[_Union[_icebox_pb2.IceboxJobStatus, str]] = ..., removal_state: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.RemovalState, _Mapping]] = ..., restore_job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., referring_restore_job_vec: _Optional[_Iterable[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]]] = ..., expiry_timestamp_usecs: _Optional[int] = ..., end_timestamp_usecs: _Optional[int] = ..., file_system_name: _Optional[str] = ..., is_view_fs_entity: bool = ...) -> None: ...

class JobGCStateProto(_message.Message):
    __slots__ = ("archive_uid", "job_uid", "vault_id", "expiry_timestamp_usecs", "app_job_uid", "start_timestamp_usecs", "end_timestamp_usecs", "job_status", "is_reference_archive", "is_retired_reference", "removal_state", "error", "logical_size_bytes", "physical_size_bytes", "is_retire_reference_in_progress", "app_job_instance_id", "retired_reference_op_clock", "job_start_op_clock", "is_base", "base_archive_uid", "prev_archive_uid", "prev_base_archive_uid", "referred_archive_uid_vec", "node_id_floor", "reference_retire_reason", "reference_retire_timestamp_usecs", "archive_type_reason", "reference_chunk_usage_pct", "version", "job_type", "job_name", "owned_by_remote_cluster", "restore_index_job_context", "parent_job_uid", "search_job_stats", "remote_restore_state", "viewbox_id", "archive_now", "earliest_entity_expiry_time_usecs", "snapshot_timestamp_usecs", "stub_view_info_vec", "to_be_removed_stub_view_id_vec", "worm_policy_type", "data_lock_constraints", "on_legal_hold", "enabled_feature_vec", "create_timestamp_usecs", "hydration_duration_usecs", "data_removal_state", "num_files_found", "is_data_removed", "num_da_objects_deleted", "num_files_restored", "stub_view_uptiering_downtiering_done", "app_job_restore_task_id", "epoch_id", "is_uptier_restore_job", "is_expired_by_vault_removal", "job_status_finish_times_map", "data_removal_timestamp_usecs", "archive_worm_properties", "last_validation_timestamp_usecs", "is_rpaas_job", "cloud_domain_id", "archive_worm_stats", "is_forever_incremental_archive", "user_info", "worm_stats")
    class RestoreIndexJobContext(_message.Message):
        __slots__ = ("search_job_uid", "app_job_name", "cluster_name", "index_time_range", "restore_snapshot_archive_uid", "restore_snapshot_job_uid", "restore_snapshot_job_error", "snapshot_job_progress_monitor_path", "index_job_progress_monitor_path", "local_app_job_uid", "restore_snapshot_expiry_time_usecs", "latest_expiry_time_usecs", "restore_index_stats", "is_direct_archive")
        SEARCH_JOB_UID_FIELD_NUMBER: _ClassVar[int]
        APP_JOB_NAME_FIELD_NUMBER: _ClassVar[int]
        CLUSTER_NAME_FIELD_NUMBER: _ClassVar[int]
        INDEX_TIME_RANGE_FIELD_NUMBER: _ClassVar[int]
        RESTORE_SNAPSHOT_ARCHIVE_UID_FIELD_NUMBER: _ClassVar[int]
        RESTORE_SNAPSHOT_JOB_UID_FIELD_NUMBER: _ClassVar[int]
        RESTORE_SNAPSHOT_JOB_ERROR_FIELD_NUMBER: _ClassVar[int]
        SNAPSHOT_JOB_PROGRESS_MONITOR_PATH_FIELD_NUMBER: _ClassVar[int]
        INDEX_JOB_PROGRESS_MONITOR_PATH_FIELD_NUMBER: _ClassVar[int]
        LOCAL_APP_JOB_UID_FIELD_NUMBER: _ClassVar[int]
        RESTORE_SNAPSHOT_EXPIRY_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
        LATEST_EXPIRY_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
        RESTORE_INDEX_STATS_FIELD_NUMBER: _ClassVar[int]
        IS_DIRECT_ARCHIVE_FIELD_NUMBER: _ClassVar[int]
        search_job_uid: _universal_id_pb2.UniversalIdProto
        app_job_name: str
        cluster_name: str
        index_time_range: _icebox_pb2.TimeRange
        restore_snapshot_archive_uid: _universal_id_pb2.UniversalIdProto
        restore_snapshot_job_uid: _universal_id_pb2.UniversalIdProto
        restore_snapshot_job_error: _error_pb2.ErrorProto
        snapshot_job_progress_monitor_path: str
        index_job_progress_monitor_path: str
        local_app_job_uid: _universal_id_pb2.UniversalIdProto
        restore_snapshot_expiry_time_usecs: int
        latest_expiry_time_usecs: int
        restore_index_stats: _icebox_pb2.RestoreIndexStats
        is_direct_archive: bool
        def __init__(self, search_job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., app_job_name: _Optional[str] = ..., cluster_name: _Optional[str] = ..., index_time_range: _Optional[_Union[_icebox_pb2.TimeRange, _Mapping]] = ..., restore_snapshot_archive_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., restore_snapshot_job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., restore_snapshot_job_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., snapshot_job_progress_monitor_path: _Optional[str] = ..., index_job_progress_monitor_path: _Optional[str] = ..., local_app_job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., restore_snapshot_expiry_time_usecs: _Optional[int] = ..., latest_expiry_time_usecs: _Optional[int] = ..., restore_index_stats: _Optional[_Union[_icebox_pb2.RestoreIndexStats, _Mapping]] = ..., is_direct_archive: bool = ...) -> None: ...
    class JobStatusFinishTimesMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    ARCHIVE_UID_FIELD_NUMBER: _ClassVar[int]
    JOB_UID_FIELD_NUMBER: _ClassVar[int]
    VAULT_ID_FIELD_NUMBER: _ClassVar[int]
    EXPIRY_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
    APP_JOB_UID_FIELD_NUMBER: _ClassVar[int]
    START_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
    END_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
    JOB_STATUS_FIELD_NUMBER: _ClassVar[int]
    IS_REFERENCE_ARCHIVE_FIELD_NUMBER: _ClassVar[int]
    IS_RETIRED_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    REMOVAL_STATE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    LOGICAL_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    PHYSICAL_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    IS_RETIRE_REFERENCE_IN_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    APP_JOB_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    RETIRED_REFERENCE_OP_CLOCK_FIELD_NUMBER: _ClassVar[int]
    JOB_START_OP_CLOCK_FIELD_NUMBER: _ClassVar[int]
    IS_BASE_FIELD_NUMBER: _ClassVar[int]
    BASE_ARCHIVE_UID_FIELD_NUMBER: _ClassVar[int]
    PREV_ARCHIVE_UID_FIELD_NUMBER: _ClassVar[int]
    PREV_BASE_ARCHIVE_UID_FIELD_NUMBER: _ClassVar[int]
    REFERRED_ARCHIVE_UID_VEC_FIELD_NUMBER: _ClassVar[int]
    NODE_ID_FLOOR_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_RETIRE_REASON_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_RETIRE_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
    ARCHIVE_TYPE_REASON_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_CHUNK_USAGE_PCT_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    JOB_TYPE_FIELD_NUMBER: _ClassVar[int]
    JOB_NAME_FIELD_NUMBER: _ClassVar[int]
    OWNED_BY_REMOTE_CLUSTER_FIELD_NUMBER: _ClassVar[int]
    RESTORE_INDEX_JOB_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    PARENT_JOB_UID_FIELD_NUMBER: _ClassVar[int]
    SEARCH_JOB_STATS_FIELD_NUMBER: _ClassVar[int]
    REMOTE_RESTORE_STATE_FIELD_NUMBER: _ClassVar[int]
    VIEWBOX_ID_FIELD_NUMBER: _ClassVar[int]
    ARCHIVE_NOW_FIELD_NUMBER: _ClassVar[int]
    EARLIEST_ENTITY_EXPIRY_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
    STUB_VIEW_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    TO_BE_REMOVED_STUB_VIEW_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    WORM_POLICY_TYPE_FIELD_NUMBER: _ClassVar[int]
    DATA_LOCK_CONSTRAINTS_FIELD_NUMBER: _ClassVar[int]
    ON_LEGAL_HOLD_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FEATURE_VEC_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
    HYDRATION_DURATION_USECS_FIELD_NUMBER: _ClassVar[int]
    DATA_REMOVAL_STATE_FIELD_NUMBER: _ClassVar[int]
    NUM_FILES_FOUND_FIELD_NUMBER: _ClassVar[int]
    IS_DATA_REMOVED_FIELD_NUMBER: _ClassVar[int]
    NUM_DA_OBJECTS_DELETED_FIELD_NUMBER: _ClassVar[int]
    NUM_FILES_RESTORED_FIELD_NUMBER: _ClassVar[int]
    STUB_VIEW_UPTIERING_DOWNTIERING_DONE_FIELD_NUMBER: _ClassVar[int]
    APP_JOB_RESTORE_TASK_ID_FIELD_NUMBER: _ClassVar[int]
    EPOCH_ID_FIELD_NUMBER: _ClassVar[int]
    IS_UPTIER_RESTORE_JOB_FIELD_NUMBER: _ClassVar[int]
    IS_EXPIRED_BY_VAULT_REMOVAL_FIELD_NUMBER: _ClassVar[int]
    JOB_STATUS_FINISH_TIMES_MAP_FIELD_NUMBER: _ClassVar[int]
    DATA_REMOVAL_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
    ARCHIVE_WORM_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    LAST_VALIDATION_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
    IS_RPAAS_JOB_FIELD_NUMBER: _ClassVar[int]
    CLOUD_DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    ARCHIVE_WORM_STATS_FIELD_NUMBER: _ClassVar[int]
    IS_FOREVER_INCREMENTAL_ARCHIVE_FIELD_NUMBER: _ClassVar[int]
    USER_INFO_FIELD_NUMBER: _ClassVar[int]
    WORM_STATS_FIELD_NUMBER: _ClassVar[int]
    archive_uid: _universal_id_pb2.UniversalIdProto
    job_uid: _universal_id_pb2.UniversalIdProto
    vault_id: int
    expiry_timestamp_usecs: int
    app_job_uid: _universal_id_pb2.UniversalIdProto
    start_timestamp_usecs: int
    end_timestamp_usecs: int
    job_status: _icebox_pb2.IceboxJobStatus
    is_reference_archive: bool
    is_retired_reference: bool
    removal_state: _cluster_config_pb2.ClusterConfigProto.RemovalState
    error: _error_pb2.ErrorProto
    logical_size_bytes: int
    physical_size_bytes: int
    is_retire_reference_in_progress: bool
    app_job_instance_id: int
    retired_reference_op_clock: _op_clock_pb2.OpClock
    job_start_op_clock: _op_clock_pb2.OpClock
    is_base: bool
    base_archive_uid: _universal_id_pb2.UniversalIdProto
    prev_archive_uid: _universal_id_pb2.UniversalIdProto
    prev_base_archive_uid: _universal_id_pb2.UniversalIdProto
    referred_archive_uid_vec: _containers.RepeatedCompositeFieldContainer[_universal_id_pb2.UniversalIdProto]
    node_id_floor: int
    reference_retire_reason: _rpc_service_pb2.ReferenceRetireReason
    reference_retire_timestamp_usecs: int
    archive_type_reason: str
    reference_chunk_usage_pct: int
    version: int
    job_type: _icebox_pb2.IceboxJobType
    job_name: str
    owned_by_remote_cluster: bool
    restore_index_job_context: JobGCStateProto.RestoreIndexJobContext
    parent_job_uid: _universal_id_pb2.UniversalIdProto
    search_job_stats: SearchJobStats
    remote_restore_state: _icebox_pb2.RemoteRestoreState
    viewbox_id: int
    archive_now: bool
    earliest_entity_expiry_time_usecs: int
    snapshot_timestamp_usecs: int
    stub_view_info_vec: _containers.RepeatedCompositeFieldContainer[_icebox_pb2.StubViewInfo]
    to_be_removed_stub_view_id_vec: _containers.RepeatedScalarFieldContainer[int]
    worm_policy_type: _worm_pb2_1.WormRetentionProto.WormPolicyType
    data_lock_constraints: _worm_pb2_1.DataLockConstraintsProto
    on_legal_hold: bool
    enabled_feature_vec: _containers.RepeatedScalarFieldContainer[int]
    create_timestamp_usecs: int
    hydration_duration_usecs: int
    data_removal_state: _cluster_config_pb2.ClusterConfigProto.RemovalState
    num_files_found: int
    is_data_removed: bool
    num_da_objects_deleted: int
    num_files_restored: int
    stub_view_uptiering_downtiering_done: bool
    app_job_restore_task_id: int
    epoch_id: int
    is_uptier_restore_job: bool
    is_expired_by_vault_removal: bool
    job_status_finish_times_map: _containers.ScalarMap[str, int]
    data_removal_timestamp_usecs: int
    archive_worm_properties: _worm_pb2_1.ArchiveWORMProperties
    last_validation_timestamp_usecs: int
    is_rpaas_job: bool
    cloud_domain_id: int
    archive_worm_stats: _icebox_pb2.ArchiveWORMStats
    is_forever_incremental_archive: bool
    user_info: _permissions_pb2.UserInformation
    worm_stats: WORMStats
    def __init__(self, archive_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., vault_id: _Optional[int] = ..., expiry_timestamp_usecs: _Optional[int] = ..., app_job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., start_timestamp_usecs: _Optional[int] = ..., end_timestamp_usecs: _Optional[int] = ..., job_status: _Optional[_Union[_icebox_pb2.IceboxJobStatus, str]] = ..., is_reference_archive: bool = ..., is_retired_reference: bool = ..., removal_state: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.RemovalState, _Mapping]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., logical_size_bytes: _Optional[int] = ..., physical_size_bytes: _Optional[int] = ..., is_retire_reference_in_progress: bool = ..., app_job_instance_id: _Optional[int] = ..., retired_reference_op_clock: _Optional[_Union[_op_clock_pb2.OpClock, _Mapping]] = ..., job_start_op_clock: _Optional[_Union[_op_clock_pb2.OpClock, _Mapping]] = ..., is_base: bool = ..., base_archive_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., prev_archive_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., prev_base_archive_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., referred_archive_uid_vec: _Optional[_Iterable[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]]] = ..., node_id_floor: _Optional[int] = ..., reference_retire_reason: _Optional[_Union[_rpc_service_pb2.ReferenceRetireReason, _Mapping]] = ..., reference_retire_timestamp_usecs: _Optional[int] = ..., archive_type_reason: _Optional[str] = ..., reference_chunk_usage_pct: _Optional[int] = ..., version: _Optional[int] = ..., job_type: _Optional[_Union[_icebox_pb2.IceboxJobType, str]] = ..., job_name: _Optional[str] = ..., owned_by_remote_cluster: bool = ..., restore_index_job_context: _Optional[_Union[JobGCStateProto.RestoreIndexJobContext, _Mapping]] = ..., parent_job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., search_job_stats: _Optional[_Union[SearchJobStats, _Mapping]] = ..., remote_restore_state: _Optional[_Union[_icebox_pb2.RemoteRestoreState, str]] = ..., viewbox_id: _Optional[int] = ..., archive_now: bool = ..., earliest_entity_expiry_time_usecs: _Optional[int] = ..., snapshot_timestamp_usecs: _Optional[int] = ..., stub_view_info_vec: _Optional[_Iterable[_Union[_icebox_pb2.StubViewInfo, _Mapping]]] = ..., to_be_removed_stub_view_id_vec: _Optional[_Iterable[int]] = ..., worm_policy_type: _Optional[_Union[_worm_pb2_1.WormRetentionProto.WormPolicyType, str]] = ..., data_lock_constraints: _Optional[_Union[_worm_pb2_1.DataLockConstraintsProto, _Mapping]] = ..., on_legal_hold: bool = ..., enabled_feature_vec: _Optional[_Iterable[int]] = ..., create_timestamp_usecs: _Optional[int] = ..., hydration_duration_usecs: _Optional[int] = ..., data_removal_state: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.RemovalState, _Mapping]] = ..., num_files_found: _Optional[int] = ..., is_data_removed: bool = ..., num_da_objects_deleted: _Optional[int] = ..., num_files_restored: _Optional[int] = ..., stub_view_uptiering_downtiering_done: bool = ..., app_job_restore_task_id: _Optional[int] = ..., epoch_id: _Optional[int] = ..., is_uptier_restore_job: bool = ..., is_expired_by_vault_removal: bool = ..., job_status_finish_times_map: _Optional[_Mapping[str, int]] = ..., data_removal_timestamp_usecs: _Optional[int] = ..., archive_worm_properties: _Optional[_Union[_worm_pb2_1.ArchiveWORMProperties, _Mapping]] = ..., last_validation_timestamp_usecs: _Optional[int] = ..., is_rpaas_job: bool = ..., cloud_domain_id: _Optional[int] = ..., archive_worm_stats: _Optional[_Union[_icebox_pb2.ArchiveWORMStats, _Mapping]] = ..., is_forever_incremental_archive: bool = ..., user_info: _Optional[_Union[_permissions_pb2.UserInformation, _Mapping]] = ..., worm_stats: _Optional[_Union[WORMStats, _Mapping]] = ...) -> None: ...

class AppJobInfoProto(_message.Message):
    __slots__ = ("app_job_uid", "vault_id", "latest_archive_uid", "last_attempted_archive_uid", "last_attempted_archive_status", "latest_archive_now_archive_uid", "forced_full_archive_for_nfoi", "last_da_gc_job_completion_time_usecs", "is_marked_for_removal", "next_epoch_id", "latest_contiguous_completed_epoch_id", "highest_completed_epoch_id", "forced_full_for_missing_files_report_mode", "forced_full_for_missing_files_repair_mode", "last_da_gc_job_creation_time_usecs")
    APP_JOB_UID_FIELD_NUMBER: _ClassVar[int]
    VAULT_ID_FIELD_NUMBER: _ClassVar[int]
    LATEST_ARCHIVE_UID_FIELD_NUMBER: _ClassVar[int]
    LAST_ATTEMPTED_ARCHIVE_UID_FIELD_NUMBER: _ClassVar[int]
    LAST_ATTEMPTED_ARCHIVE_STATUS_FIELD_NUMBER: _ClassVar[int]
    LATEST_ARCHIVE_NOW_ARCHIVE_UID_FIELD_NUMBER: _ClassVar[int]
    FORCED_FULL_ARCHIVE_FOR_NFOI_FIELD_NUMBER: _ClassVar[int]
    LAST_DA_GC_JOB_COMPLETION_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    IS_MARKED_FOR_REMOVAL_FIELD_NUMBER: _ClassVar[int]
    NEXT_EPOCH_ID_FIELD_NUMBER: _ClassVar[int]
    LATEST_CONTIGUOUS_COMPLETED_EPOCH_ID_FIELD_NUMBER: _ClassVar[int]
    HIGHEST_COMPLETED_EPOCH_ID_FIELD_NUMBER: _ClassVar[int]
    FORCED_FULL_FOR_MISSING_FILES_REPORT_MODE_FIELD_NUMBER: _ClassVar[int]
    FORCED_FULL_FOR_MISSING_FILES_REPAIR_MODE_FIELD_NUMBER: _ClassVar[int]
    LAST_DA_GC_JOB_CREATION_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    app_job_uid: _universal_id_pb2.UniversalIdProto
    vault_id: int
    latest_archive_uid: _universal_id_pb2.UniversalIdProto
    last_attempted_archive_uid: _universal_id_pb2.UniversalIdProto
    last_attempted_archive_status: _icebox_pb2.IceboxJobStatus
    latest_archive_now_archive_uid: _universal_id_pb2.UniversalIdProto
    forced_full_archive_for_nfoi: bool
    last_da_gc_job_completion_time_usecs: int
    is_marked_for_removal: bool
    next_epoch_id: int
    latest_contiguous_completed_epoch_id: int
    highest_completed_epoch_id: int
    forced_full_for_missing_files_report_mode: bool
    forced_full_for_missing_files_repair_mode: bool
    last_da_gc_job_creation_time_usecs: int
    def __init__(self, app_job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., vault_id: _Optional[int] = ..., latest_archive_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., last_attempted_archive_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., last_attempted_archive_status: _Optional[_Union[_icebox_pb2.IceboxJobStatus, str]] = ..., latest_archive_now_archive_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., forced_full_archive_for_nfoi: bool = ..., last_da_gc_job_completion_time_usecs: _Optional[int] = ..., is_marked_for_removal: bool = ..., next_epoch_id: _Optional[int] = ..., latest_contiguous_completed_epoch_id: _Optional[int] = ..., highest_completed_epoch_id: _Optional[int] = ..., forced_full_for_missing_files_report_mode: bool = ..., forced_full_for_missing_files_repair_mode: bool = ..., last_da_gc_job_creation_time_usecs: _Optional[int] = ...) -> None: ...

class CloudDomainInfoProto(_message.Message):
    __slots__ = ("domain_id", "next_epoch_id", "latest_contiguous_completed_epoch_id", "highest_completed_epoch_id")
    DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    NEXT_EPOCH_ID_FIELD_NUMBER: _ClassVar[int]
    LATEST_CONTIGUOUS_COMPLETED_EPOCH_ID_FIELD_NUMBER: _ClassVar[int]
    HIGHEST_COMPLETED_EPOCH_ID_FIELD_NUMBER: _ClassVar[int]
    domain_id: int
    next_epoch_id: int
    latest_contiguous_completed_epoch_id: int
    highest_completed_epoch_id: int
    def __init__(self, domain_id: _Optional[int] = ..., next_epoch_id: _Optional[int] = ..., latest_contiguous_completed_epoch_id: _Optional[int] = ..., highest_completed_epoch_id: _Optional[int] = ...) -> None: ...

class MasterWALRecordProto(_message.Message):
    __slots__ = ("job_state_vec", "entity_restore_state_vec", "job_gc_state_vec", "latest_app_job_info_vec", "latest_cloud_domain_info_vec")
    JOB_STATE_VEC_FIELD_NUMBER: _ClassVar[int]
    ENTITY_RESTORE_STATE_VEC_FIELD_NUMBER: _ClassVar[int]
    JOB_GC_STATE_VEC_FIELD_NUMBER: _ClassVar[int]
    LATEST_APP_JOB_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    LATEST_CLOUD_DOMAIN_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    job_state_vec: _containers.RepeatedCompositeFieldContainer[JobStateProto]
    entity_restore_state_vec: _containers.RepeatedCompositeFieldContainer[EntityRestoreStateProto]
    job_gc_state_vec: _containers.RepeatedCompositeFieldContainer[JobGCStateProto]
    latest_app_job_info_vec: _containers.RepeatedCompositeFieldContainer[AppJobInfoProto]
    latest_cloud_domain_info_vec: _containers.RepeatedCompositeFieldContainer[CloudDomainInfoProto]
    def __init__(self, job_state_vec: _Optional[_Iterable[_Union[JobStateProto, _Mapping]]] = ..., entity_restore_state_vec: _Optional[_Iterable[_Union[EntityRestoreStateProto, _Mapping]]] = ..., job_gc_state_vec: _Optional[_Iterable[_Union[JobGCStateProto, _Mapping]]] = ..., latest_app_job_info_vec: _Optional[_Iterable[_Union[AppJobInfoProto, _Mapping]]] = ..., latest_cloud_domain_info_vec: _Optional[_Iterable[_Union[CloudDomainInfoProto, _Mapping]]] = ...) -> None: ...
