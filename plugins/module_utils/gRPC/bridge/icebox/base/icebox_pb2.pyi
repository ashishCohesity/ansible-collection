from bridge.base import cloud_pb2 as _cloud_pb2
from bridge.base import error_pb2 as _error_pb2
from bridge.blob_store import blob_store_pb2 as _blob_store_pb2
from bridge.snap_fs import entity_handle_pb2 as _entity_handle_pb2
from bridge.snap_fs import snap_fs_metadata_pb2 as _snap_fs_metadata_pb2
from bridge.snap_tree import snap_tree_pb2 as _snap_tree_pb2
from bridge.vault.base import vault_pb2 as _vault_pb2
from bridge.view_keeper import view_metadata_pb2 as _view_metadata_pb2
from configs import cluster_config_pb2 as _cluster_config_pb2
from keychain.base import keychain_pb2 as _keychain_pb2
from magneto.api import worm_pb2 as _worm_pb2
from magneto.base import entity_pb2 as _entity_pb2
from magneto.base import enums_pb2 as _enums_pb2
from magneto.base import magneto_pb2 as _magneto_pb2
from magneto.base import env_params_pb2 as _env_params_pb2
from magneto.base import permissions_pb2 as _permissions_pb2
from magneto.master.base import master_pb2 as _master_pb2
from util.base import cluster_instance_identifier_pb2 as _cluster_instance_identifier_pb2
from util.base import op_clock_pb2 as _op_clock_pb2
from util.base import universal_id_pb2 as _universal_id_pb2
from magneto.directory_walker import directory_walker_pb2 as _directory_walker_pb2
from yoda.db import documents_pb2 as _documents_pb2
from yoda.master.stub import yoda_rpc_args_pb2 as _yoda_rpc_args_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class IceboxJobStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kCreated: _ClassVar[IceboxJobStatus]
    kRunning: _ClassVar[IceboxJobStatus]
    kFinished: _ClassVar[IceboxJobStatus]
    kFailed: _ClassVar[IceboxJobStatus]
    kCanceled: _ClassVar[IceboxJobStatus]
    kCanceling: _ClassVar[IceboxJobStatus]
    kArchivingIndex: _ClassVar[IceboxJobStatus]
    kRestoringIndex: _ClassVar[IceboxJobStatus]
    kPaused: _ClassVar[IceboxJobStatus]
    kPreprocessing: _ClassVar[IceboxJobStatus]
    kArchivingBlobs: _ClassVar[IceboxJobStatus]
    kArchivingInternalFileSystem: _ClassVar[IceboxJobStatus]
    kArchivingViewSnapTrees: _ClassVar[IceboxJobStatus]
    kArchiveObjectFinalizing: _ClassVar[IceboxJobStatus]
    kArchivingMetadata: _ClassVar[IceboxJobStatus]
    kReadingMetadata: _ClassVar[IceboxJobStatus]
    kPostprocessing: _ClassVar[IceboxJobStatus]
    kAborting: _ClassVar[IceboxJobStatus]
    kArchivingDirectArchiveBlobs: _ClassVar[IceboxJobStatus]
    kDownloadSnapTreeObjects: _ClassVar[IceboxJobStatus]
    kIssueDirectArchiveGCReqToApollo: _ClassVar[IceboxJobStatus]
    kCleaningupDirectArchiveObjects: _ClassVar[IceboxJobStatus]
    kIssuedDirectArchiveGCReqToApollo: _ClassVar[IceboxJobStatus]
    kValidating: _ClassVar[IceboxJobStatus]
    kDowntieringData: _ClassVar[IceboxJobStatus]
    kArchivingDataAndMetadata: _ClassVar[IceboxJobStatus]
    kArchivingIndexMetadata: _ClassVar[IceboxJobStatus]
    kStuck: _ClassVar[IceboxJobStatus]
    kSnapTreesDownloaded: _ClassVar[IceboxJobStatus]
    kUptieringCloudDomainData: _ClassVar[IceboxJobStatus]
    kInitiateSnapTreesFetch: _ClassVar[IceboxJobStatus]
    kIssueDomainMigrationRequestsToApollo: _ClassVar[IceboxJobStatus]
    kInitiateTenantFailover: _ClassVar[IceboxJobStatus]
    kRegisterRuns: _ClassVar[IceboxJobStatus]
    kInitiateSnapshotMigration: _ClassVar[IceboxJobStatus]
    kFetchingCloudSnapshots: _ClassVar[IceboxJobStatus]
    kReadyForMagnetoFailover: _ClassVar[IceboxJobStatus]
    kRegisterAppJobMetadata: _ClassVar[IceboxJobStatus]
    kCopyingCohesionData: _ClassVar[IceboxJobStatus]

class FileUploadStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kFileCreated: _ClassVar[FileUploadStatus]
    kFileUploaded: _ClassVar[FileUploadStatus]
    kFileFinalized: _ClassVar[FileUploadStatus]

class RemoteRestoreState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kAppJobMetadataRegistered: _ClassVar[RemoteRestoreState]
    kIndexBuilt: _ClassVar[RemoteRestoreState]

class IceboxJobType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kArchival: _ClassVar[IceboxJobType]
    kRestore: _ClassVar[IceboxJobType]
    kVaultSearch: _ClassVar[IceboxJobType]
    kBatchJob: _ClassVar[IceboxJobType]
    kRestoreIndexAndSnapshot: _ClassVar[IceboxJobType]
    kStubView: _ClassVar[IceboxJobType]
    kFileUpload: _ClassVar[IceboxJobType]
    kDirectArchiveJob: _ClassVar[IceboxJobType]
    kDirectArchiveGCJob: _ClassVar[IceboxJobType]
    kCloudDomainArchiveJob: _ClassVar[IceboxJobType]
    kCloudDomainMigrationJob: _ClassVar[IceboxJobType]
    kCloudDomainRebuildJob: _ClassVar[IceboxJobType]
    kCohesionCopyJob: _ClassVar[IceboxJobType]

class IceboxSnapTreeType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kViewSnapTree: _ClassVar[IceboxSnapTreeType]
    kBlobSnapTree: _ClassVar[IceboxSnapTreeType]
    kS3ObjectSnapTree: _ClassVar[IceboxSnapTreeType]
kCreated: IceboxJobStatus
kRunning: IceboxJobStatus
kFinished: IceboxJobStatus
kFailed: IceboxJobStatus
kCanceled: IceboxJobStatus
kCanceling: IceboxJobStatus
kArchivingIndex: IceboxJobStatus
kRestoringIndex: IceboxJobStatus
kPaused: IceboxJobStatus
kPreprocessing: IceboxJobStatus
kArchivingBlobs: IceboxJobStatus
kArchivingInternalFileSystem: IceboxJobStatus
kArchivingViewSnapTrees: IceboxJobStatus
kArchiveObjectFinalizing: IceboxJobStatus
kArchivingMetadata: IceboxJobStatus
kReadingMetadata: IceboxJobStatus
kPostprocessing: IceboxJobStatus
kAborting: IceboxJobStatus
kArchivingDirectArchiveBlobs: IceboxJobStatus
kDownloadSnapTreeObjects: IceboxJobStatus
kIssueDirectArchiveGCReqToApollo: IceboxJobStatus
kCleaningupDirectArchiveObjects: IceboxJobStatus
kIssuedDirectArchiveGCReqToApollo: IceboxJobStatus
kValidating: IceboxJobStatus
kDowntieringData: IceboxJobStatus
kArchivingDataAndMetadata: IceboxJobStatus
kArchivingIndexMetadata: IceboxJobStatus
kStuck: IceboxJobStatus
kSnapTreesDownloaded: IceboxJobStatus
kUptieringCloudDomainData: IceboxJobStatus
kInitiateSnapTreesFetch: IceboxJobStatus
kIssueDomainMigrationRequestsToApollo: IceboxJobStatus
kInitiateTenantFailover: IceboxJobStatus
kRegisterRuns: IceboxJobStatus
kInitiateSnapshotMigration: IceboxJobStatus
kFetchingCloudSnapshots: IceboxJobStatus
kReadyForMagnetoFailover: IceboxJobStatus
kRegisterAppJobMetadata: IceboxJobStatus
kCopyingCohesionData: IceboxJobStatus
kFileCreated: FileUploadStatus
kFileUploaded: FileUploadStatus
kFileFinalized: FileUploadStatus
kAppJobMetadataRegistered: RemoteRestoreState
kIndexBuilt: RemoteRestoreState
kArchival: IceboxJobType
kRestore: IceboxJobType
kVaultSearch: IceboxJobType
kBatchJob: IceboxJobType
kRestoreIndexAndSnapshot: IceboxJobType
kStubView: IceboxJobType
kFileUpload: IceboxJobType
kDirectArchiveJob: IceboxJobType
kDirectArchiveGCJob: IceboxJobType
kCloudDomainArchiveJob: IceboxJobType
kCloudDomainMigrationJob: IceboxJobType
kCloudDomainRebuildJob: IceboxJobType
kCohesionCopyJob: IceboxJobType
kViewSnapTree: IceboxSnapTreeType
kBlobSnapTree: IceboxSnapTreeType
kS3ObjectSnapTree: IceboxSnapTreeType

class ArchivalObjectMetadataProto(_message.Message):
    __slots__ = ("archive_uid", "object_uid", "version", "cluster_instance_id", "snapshot_time_usecs", "compression_level", "encryption_level", "encryption_config", "random_nonce", "is_index", "job_uid", "job_instance_id", "job_metadata", "expiry_timestamp_usecs", "cluster_name", "job_name", "view_id", "view_name", "object_type", "job_run_metadata", "encrypted_object_metadata_info", "is_view_snap_tree", "version_id")
    class ObjectType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kDataObjectType: _ClassVar[ArchivalObjectMetadataProto.ObjectType]
        kSnapTreeObjectType: _ClassVar[ArchivalObjectMetadataProto.ObjectType]
        kMetadataObjectType: _ClassVar[ArchivalObjectMetadataProto.ObjectType]
        kViewSnapTreeObjectType: _ClassVar[ArchivalObjectMetadataProto.ObjectType]
    kDataObjectType: ArchivalObjectMetadataProto.ObjectType
    kSnapTreeObjectType: ArchivalObjectMetadataProto.ObjectType
    kMetadataObjectType: ArchivalObjectMetadataProto.ObjectType
    kViewSnapTreeObjectType: ArchivalObjectMetadataProto.ObjectType
    class EncryptedObjectMetadataInfo(_message.Message):
        __slots__ = ("size_before_encryption", "size_after_encryption")
        SIZE_BEFORE_ENCRYPTION_FIELD_NUMBER: _ClassVar[int]
        SIZE_AFTER_ENCRYPTION_FIELD_NUMBER: _ClassVar[int]
        size_before_encryption: int
        size_after_encryption: int
        def __init__(self, size_before_encryption: _Optional[int] = ..., size_after_encryption: _Optional[int] = ...) -> None: ...
    ARCHIVE_UID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_UID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    COMPRESSION_LEVEL_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_LEVEL_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    RANDOM_NONCE_FIELD_NUMBER: _ClassVar[int]
    IS_INDEX_FIELD_NUMBER: _ClassVar[int]
    JOB_UID_FIELD_NUMBER: _ClassVar[int]
    JOB_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    JOB_METADATA_FIELD_NUMBER: _ClassVar[int]
    EXPIRY_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_NAME_FIELD_NUMBER: _ClassVar[int]
    JOB_NAME_FIELD_NUMBER: _ClassVar[int]
    VIEW_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    OBJECT_TYPE_FIELD_NUMBER: _ClassVar[int]
    JOB_RUN_METADATA_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTED_OBJECT_METADATA_INFO_FIELD_NUMBER: _ClassVar[int]
    IS_VIEW_SNAP_TREE_FIELD_NUMBER: _ClassVar[int]
    VERSION_ID_FIELD_NUMBER: _ClassVar[int]
    archive_uid: _universal_id_pb2.UniversalIdProto
    object_uid: _universal_id_pb2.UniversalIdProto
    version: int
    cluster_instance_id: _cluster_instance_identifier_pb2.ClusterInstanceIdentifier
    snapshot_time_usecs: int
    compression_level: _cluster_config_pb2.ClusterConfigProto.StoragePolicy.CompressionLevel
    encryption_level: _cluster_config_pb2.ClusterConfigProto.EncryptionLevel
    encryption_config: _cluster_config_pb2.ClusterConfigProto.Vault.EncryptionConfig
    random_nonce: bytes
    is_index: bool
    job_uid: _universal_id_pb2.UniversalIdProto
    job_instance_id: int
    job_metadata: bytes
    expiry_timestamp_usecs: int
    cluster_name: str
    job_name: str
    view_id: int
    view_name: str
    object_type: ArchivalObjectMetadataProto.ObjectType
    job_run_metadata: _master_pb2.BackupRunArchiveMDProto
    encrypted_object_metadata_info: ArchivalObjectMetadataProto.EncryptedObjectMetadataInfo
    is_view_snap_tree: bool
    version_id: str
    def __init__(self, archive_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., object_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., version: _Optional[int] = ..., cluster_instance_id: _Optional[_Union[_cluster_instance_identifier_pb2.ClusterInstanceIdentifier, _Mapping]] = ..., snapshot_time_usecs: _Optional[int] = ..., compression_level: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.StoragePolicy.CompressionLevel, str]] = ..., encryption_level: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.EncryptionLevel, str]] = ..., encryption_config: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.Vault.EncryptionConfig, _Mapping]] = ..., random_nonce: _Optional[bytes] = ..., is_index: bool = ..., job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., job_instance_id: _Optional[int] = ..., job_metadata: _Optional[bytes] = ..., expiry_timestamp_usecs: _Optional[int] = ..., cluster_name: _Optional[str] = ..., job_name: _Optional[str] = ..., view_id: _Optional[int] = ..., view_name: _Optional[str] = ..., object_type: _Optional[_Union[ArchivalObjectMetadataProto.ObjectType, str]] = ..., job_run_metadata: _Optional[_Union[_master_pb2.BackupRunArchiveMDProto, _Mapping]] = ..., encrypted_object_metadata_info: _Optional[_Union[ArchivalObjectMetadataProto.EncryptedObjectMetadataInfo, _Mapping]] = ..., is_view_snap_tree: bool = ..., version_id: _Optional[str] = ...) -> None: ...

class SegmentMetadataProto(_message.Message):
    __slots__ = ("morphed_size_bytes", "unmorphed_size_bytes", "checksum", "is_zero_segment", "num_padding_bytes", "contains_entity_metadata", "is_final_segment", "segment_type", "checksum_after_compression", "checksum_after_encryption")
    class SegmentType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kDataSegment: _ClassVar[SegmentMetadataProto.SegmentType]
        kSnapTreeIndexSegment: _ClassVar[SegmentMetadataProto.SegmentType]
        kZeroSegment: _ClassVar[SegmentMetadataProto.SegmentType]
        kPaddingSegment: _ClassVar[SegmentMetadataProto.SegmentType]
        kFinalSegment: _ClassVar[SegmentMetadataProto.SegmentType]
        kMetadataSegment: _ClassVar[SegmentMetadataProto.SegmentType]
    kDataSegment: SegmentMetadataProto.SegmentType
    kSnapTreeIndexSegment: SegmentMetadataProto.SegmentType
    kZeroSegment: SegmentMetadataProto.SegmentType
    kPaddingSegment: SegmentMetadataProto.SegmentType
    kFinalSegment: SegmentMetadataProto.SegmentType
    kMetadataSegment: SegmentMetadataProto.SegmentType
    MORPHED_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    UNMORPHED_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    CHECKSUM_FIELD_NUMBER: _ClassVar[int]
    IS_ZERO_SEGMENT_FIELD_NUMBER: _ClassVar[int]
    NUM_PADDING_BYTES_FIELD_NUMBER: _ClassVar[int]
    CONTAINS_ENTITY_METADATA_FIELD_NUMBER: _ClassVar[int]
    IS_FINAL_SEGMENT_FIELD_NUMBER: _ClassVar[int]
    SEGMENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    CHECKSUM_AFTER_COMPRESSION_FIELD_NUMBER: _ClassVar[int]
    CHECKSUM_AFTER_ENCRYPTION_FIELD_NUMBER: _ClassVar[int]
    morphed_size_bytes: int
    unmorphed_size_bytes: int
    checksum: int
    is_zero_segment: bool
    num_padding_bytes: int
    contains_entity_metadata: bool
    is_final_segment: bool
    segment_type: SegmentMetadataProto.SegmentType
    checksum_after_compression: int
    checksum_after_encryption: int
    def __init__(self, morphed_size_bytes: _Optional[int] = ..., unmorphed_size_bytes: _Optional[int] = ..., checksum: _Optional[int] = ..., is_zero_segment: bool = ..., num_padding_bytes: _Optional[int] = ..., contains_entity_metadata: bool = ..., is_final_segment: bool = ..., segment_type: _Optional[_Union[SegmentMetadataProto.SegmentType, str]] = ..., checksum_after_compression: _Optional[int] = ..., checksum_after_encryption: _Optional[int] = ...) -> None: ...

class EntityMetadataProto(_message.Message):
    __slots__ = ("entity_id", "file_system_name", "entity_metadata", "logical_size_bytes", "physical_size_bytes", "entity_reference_vec", "status", "error", "end_timestamp_usecs", "entity_dir_relative_path", "index_info", "view_id", "prev_archive_node_id_floor", "view_snap_tree_keys_mapped", "mapped_key_byte_swapped_with_last_byte", "mapped_key_swap_bit_mask", "entity_name", "expiry_timestamp_usecs", "removal_state", "quota_snap_tree_info", "case_insensitive_entity_names", "on_legal_hold", "frontend_size_bytes")
    class EntityReference(_message.Message):
        __slots__ = ("object_uid", "start_offset", "end_offset")
        OBJECT_UID_FIELD_NUMBER: _ClassVar[int]
        START_OFFSET_FIELD_NUMBER: _ClassVar[int]
        END_OFFSET_FIELD_NUMBER: _ClassVar[int]
        object_uid: _universal_id_pb2.UniversalIdProto
        start_offset: int
        end_offset: int
        def __init__(self, object_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., start_offset: _Optional[int] = ..., end_offset: _Optional[int] = ...) -> None: ...
    class ObjectSnapshotDocFileProto(_message.Message):
        __slots__ = ("object_doc", "aux_db", "cfile_index_metadata")
        class AuxDbEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: bytes
            def __init__(self, key: _Optional[str] = ..., value: _Optional[bytes] = ...) -> None: ...
        OBJECT_DOC_FIELD_NUMBER: _ClassVar[int]
        AUX_DB_FIELD_NUMBER: _ClassVar[int]
        CFILE_INDEX_METADATA_FIELD_NUMBER: _ClassVar[int]
        object_doc: _documents_pb2.ObjectSnapshotDocument
        aux_db: _containers.ScalarMap[str, bytes]
        cfile_index_metadata: _yoda_rpc_args_pb2.CrackedFileIndexMetadata
        def __init__(self, object_doc: _Optional[_Union[_documents_pb2.ObjectSnapshotDocument, _Mapping]] = ..., aux_db: _Optional[_Mapping[str, bytes]] = ..., cfile_index_metadata: _Optional[_Union[_yoda_rpc_args_pb2.CrackedFileIndexMetadata, _Mapping]] = ...) -> None: ...
    class IndexInfo(_message.Message):
        __slots__ = ("object_snapshot_doc_file_rel_path", "index_file_rel_path", "index_size_bytes", "fs_name", "index_files_parent_dir_path", "object_doc_file_format_version")
        OBJECT_SNAPSHOT_DOC_FILE_REL_PATH_FIELD_NUMBER: _ClassVar[int]
        INDEX_FILE_REL_PATH_FIELD_NUMBER: _ClassVar[int]
        INDEX_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
        FS_NAME_FIELD_NUMBER: _ClassVar[int]
        INDEX_FILES_PARENT_DIR_PATH_FIELD_NUMBER: _ClassVar[int]
        OBJECT_DOC_FILE_FORMAT_VERSION_FIELD_NUMBER: _ClassVar[int]
        object_snapshot_doc_file_rel_path: str
        index_file_rel_path: str
        index_size_bytes: int
        fs_name: str
        index_files_parent_dir_path: str
        object_doc_file_format_version: int
        def __init__(self, object_snapshot_doc_file_rel_path: _Optional[str] = ..., index_file_rel_path: _Optional[str] = ..., index_size_bytes: _Optional[int] = ..., fs_name: _Optional[str] = ..., index_files_parent_dir_path: _Optional[str] = ..., object_doc_file_format_version: _Optional[int] = ...) -> None: ...
    class QuotaSnapTreeInfo(_message.Message):
        __slots__ = ("backup_unique_id", "backup_dir_name")
        BACKUP_UNIQUE_ID_FIELD_NUMBER: _ClassVar[int]
        BACKUP_DIR_NAME_FIELD_NUMBER: _ClassVar[int]
        backup_unique_id: int
        backup_dir_name: str
        def __init__(self, backup_unique_id: _Optional[int] = ..., backup_dir_name: _Optional[str] = ...) -> None: ...
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    FILE_SYSTEM_NAME_FIELD_NUMBER: _ClassVar[int]
    ENTITY_METADATA_FIELD_NUMBER: _ClassVar[int]
    LOGICAL_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    PHYSICAL_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    ENTITY_REFERENCE_VEC_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    END_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
    ENTITY_DIR_RELATIVE_PATH_FIELD_NUMBER: _ClassVar[int]
    INDEX_INFO_FIELD_NUMBER: _ClassVar[int]
    VIEW_ID_FIELD_NUMBER: _ClassVar[int]
    PREV_ARCHIVE_NODE_ID_FLOOR_FIELD_NUMBER: _ClassVar[int]
    VIEW_SNAP_TREE_KEYS_MAPPED_FIELD_NUMBER: _ClassVar[int]
    MAPPED_KEY_BYTE_SWAPPED_WITH_LAST_BYTE_FIELD_NUMBER: _ClassVar[int]
    MAPPED_KEY_SWAP_BIT_MASK_FIELD_NUMBER: _ClassVar[int]
    ENTITY_NAME_FIELD_NUMBER: _ClassVar[int]
    EXPIRY_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
    REMOVAL_STATE_FIELD_NUMBER: _ClassVar[int]
    QUOTA_SNAP_TREE_INFO_FIELD_NUMBER: _ClassVar[int]
    CASE_INSENSITIVE_ENTITY_NAMES_FIELD_NUMBER: _ClassVar[int]
    ON_LEGAL_HOLD_FIELD_NUMBER: _ClassVar[int]
    FRONTEND_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    entity_id: int
    file_system_name: str
    entity_metadata: bytes
    logical_size_bytes: int
    physical_size_bytes: int
    entity_reference_vec: _containers.RepeatedCompositeFieldContainer[EntityMetadataProto.EntityReference]
    status: IceboxJobStatus
    error: _error_pb2.ErrorProto
    end_timestamp_usecs: int
    entity_dir_relative_path: str
    index_info: EntityMetadataProto.IndexInfo
    view_id: int
    prev_archive_node_id_floor: int
    view_snap_tree_keys_mapped: bool
    mapped_key_byte_swapped_with_last_byte: int
    mapped_key_swap_bit_mask: int
    entity_name: str
    expiry_timestamp_usecs: int
    removal_state: _cluster_config_pb2.ClusterConfigProto.RemovalState
    quota_snap_tree_info: EntityMetadataProto.QuotaSnapTreeInfo
    case_insensitive_entity_names: bool
    on_legal_hold: bool
    frontend_size_bytes: int
    def __init__(self, entity_id: _Optional[int] = ..., file_system_name: _Optional[str] = ..., entity_metadata: _Optional[bytes] = ..., logical_size_bytes: _Optional[int] = ..., physical_size_bytes: _Optional[int] = ..., entity_reference_vec: _Optional[_Iterable[_Union[EntityMetadataProto.EntityReference, _Mapping]]] = ..., status: _Optional[_Union[IceboxJobStatus, str]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., end_timestamp_usecs: _Optional[int] = ..., entity_dir_relative_path: _Optional[str] = ..., index_info: _Optional[_Union[EntityMetadataProto.IndexInfo, _Mapping]] = ..., view_id: _Optional[int] = ..., prev_archive_node_id_floor: _Optional[int] = ..., view_snap_tree_keys_mapped: bool = ..., mapped_key_byte_swapped_with_last_byte: _Optional[int] = ..., mapped_key_swap_bit_mask: _Optional[int] = ..., entity_name: _Optional[str] = ..., expiry_timestamp_usecs: _Optional[int] = ..., removal_state: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.RemovalState, _Mapping]] = ..., quota_snap_tree_info: _Optional[_Union[EntityMetadataProto.QuotaSnapTreeInfo, _Mapping]] = ..., case_insensitive_entity_names: bool = ..., on_legal_hold: bool = ..., frontend_size_bytes: _Optional[int] = ...) -> None: ...

class FileMetadataProto(_message.Message):
    __slots__ = ("entity_dir_path", "relative_file_path", "file_type", "mode", "uid", "gid", "logical_size", "physical_size", "major_device_number", "minor_device_number", "ctime_usecs", "mtime_usecs", "create_verifier", "total_directory_entries", "symlink_data", "parent_ctime_usecs", "parent_mtime_usecs")
    class FileType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kRegularFile: _ClassVar[FileMetadataProto.FileType]
        kDirectory: _ClassVar[FileMetadataProto.FileType]
        kBlockDevice: _ClassVar[FileMetadataProto.FileType]
        kCharacterDevice: _ClassVar[FileMetadataProto.FileType]
        kSymLink: _ClassVar[FileMetadataProto.FileType]
        kSocket: _ClassVar[FileMetadataProto.FileType]
        kPipe: _ClassVar[FileMetadataProto.FileType]
    kRegularFile: FileMetadataProto.FileType
    kDirectory: FileMetadataProto.FileType
    kBlockDevice: FileMetadataProto.FileType
    kCharacterDevice: FileMetadataProto.FileType
    kSymLink: FileMetadataProto.FileType
    kSocket: FileMetadataProto.FileType
    kPipe: FileMetadataProto.FileType
    ENTITY_DIR_PATH_FIELD_NUMBER: _ClassVar[int]
    RELATIVE_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    FILE_TYPE_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    GID_FIELD_NUMBER: _ClassVar[int]
    LOGICAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    PHYSICAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    MAJOR_DEVICE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    MINOR_DEVICE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    CTIME_USECS_FIELD_NUMBER: _ClassVar[int]
    MTIME_USECS_FIELD_NUMBER: _ClassVar[int]
    CREATE_VERIFIER_FIELD_NUMBER: _ClassVar[int]
    TOTAL_DIRECTORY_ENTRIES_FIELD_NUMBER: _ClassVar[int]
    SYMLINK_DATA_FIELD_NUMBER: _ClassVar[int]
    PARENT_CTIME_USECS_FIELD_NUMBER: _ClassVar[int]
    PARENT_MTIME_USECS_FIELD_NUMBER: _ClassVar[int]
    entity_dir_path: str
    relative_file_path: str
    file_type: FileMetadataProto.FileType
    mode: int
    uid: int
    gid: int
    logical_size: int
    physical_size: int
    major_device_number: int
    minor_device_number: int
    ctime_usecs: int
    mtime_usecs: int
    create_verifier: int
    total_directory_entries: int
    symlink_data: str
    parent_ctime_usecs: int
    parent_mtime_usecs: int
    def __init__(self, entity_dir_path: _Optional[str] = ..., relative_file_path: _Optional[str] = ..., file_type: _Optional[_Union[FileMetadataProto.FileType, str]] = ..., mode: _Optional[int] = ..., uid: _Optional[int] = ..., gid: _Optional[int] = ..., logical_size: _Optional[int] = ..., physical_size: _Optional[int] = ..., major_device_number: _Optional[int] = ..., minor_device_number: _Optional[int] = ..., ctime_usecs: _Optional[int] = ..., mtime_usecs: _Optional[int] = ..., create_verifier: _Optional[int] = ..., total_directory_entries: _Optional[int] = ..., symlink_data: _Optional[str] = ..., parent_ctime_usecs: _Optional[int] = ..., parent_mtime_usecs: _Optional[int] = ...) -> None: ...

class ArchiveBlobTaskStats(_message.Message):
    __slots__ = ("num_bytes_changed", "num_total_chunks", "num_new_chunks_uploaded", "num_chunks_used_from_curr_reference")
    NUM_BYTES_CHANGED_FIELD_NUMBER: _ClassVar[int]
    NUM_TOTAL_CHUNKS_FIELD_NUMBER: _ClassVar[int]
    NUM_NEW_CHUNKS_UPLOADED_FIELD_NUMBER: _ClassVar[int]
    NUM_CHUNKS_USED_FROM_CURR_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    num_bytes_changed: int
    num_total_chunks: int
    num_new_chunks_uploaded: int
    num_chunks_used_from_curr_reference: int
    def __init__(self, num_bytes_changed: _Optional[int] = ..., num_total_chunks: _Optional[int] = ..., num_new_chunks_uploaded: _Optional[int] = ..., num_chunks_used_from_curr_reference: _Optional[int] = ...) -> None: ...

class ArchiveViewSnapTreeTaskStats(_message.Message):
    __slots__ = ("total_view_snap_tree_nodes_to_be_archived", "num_view_snap_tree_nodes_processed", "snap_tree_stats_vec")
    class SnapTreeStats(_message.Message):
        __slots__ = ("root_tree_id", "total_view_snap_tree_nodes_to_be_archived", "total_logical_size_to_be_archived")
        ROOT_TREE_ID_FIELD_NUMBER: _ClassVar[int]
        TOTAL_VIEW_SNAP_TREE_NODES_TO_BE_ARCHIVED_FIELD_NUMBER: _ClassVar[int]
        TOTAL_LOGICAL_SIZE_TO_BE_ARCHIVED_FIELD_NUMBER: _ClassVar[int]
        root_tree_id: int
        total_view_snap_tree_nodes_to_be_archived: int
        total_logical_size_to_be_archived: int
        def __init__(self, root_tree_id: _Optional[int] = ..., total_view_snap_tree_nodes_to_be_archived: _Optional[int] = ..., total_logical_size_to_be_archived: _Optional[int] = ...) -> None: ...
    TOTAL_VIEW_SNAP_TREE_NODES_TO_BE_ARCHIVED_FIELD_NUMBER: _ClassVar[int]
    NUM_VIEW_SNAP_TREE_NODES_PROCESSED_FIELD_NUMBER: _ClassVar[int]
    SNAP_TREE_STATS_VEC_FIELD_NUMBER: _ClassVar[int]
    total_view_snap_tree_nodes_to_be_archived: int
    num_view_snap_tree_nodes_processed: int
    snap_tree_stats_vec: _containers.RepeatedCompositeFieldContainer[ArchiveViewSnapTreeTaskStats.SnapTreeStats]
    def __init__(self, total_view_snap_tree_nodes_to_be_archived: _Optional[int] = ..., num_view_snap_tree_nodes_processed: _Optional[int] = ..., snap_tree_stats_vec: _Optional[_Iterable[_Union[ArchiveViewSnapTreeTaskStats.SnapTreeStats, _Mapping]]] = ...) -> None: ...

class ArchiveMetadataProto(_message.Message):
    __slots__ = ("archive_uid", "vault_id", "object_uid_vec", "metadata_object_uid_vec", "logical_archive_size_bytes", "physical_archive_size_bytes", "start_time_usecs", "end_time_usecs", "job_status", "error", "expiry_timestamp_usecs", "progress_monitor_task_path", "entity_metadata_vec", "job_uid", "job_instance_id", "is_view_archive", "version", "snapshot_metadata", "is_reference_archive", "is_retired_reference", "archived_view_inode_id_floor", "view_snap_tree_keys_mapped", "archive_object_metadata_vec", "logical_bytes_processed", "archive_stats", "opclock_vec", "non_finalized_object_name_vec", "snapshot_time_usecs", "job_run_metadata", "entity_mapping_info", "index_info", "view_metadata", "app_job_type", "archive_stub_view_info", "entity_stub_view_info_vec", "original_expiry_timestamp_usecs", "cluster_name", "use_restore_objects_manager", "worm_policy_type", "data_lock_constraints", "on_legal_hold", "is_direct_archive", "is_data_in_native_format", "num_padded_bytes", "archive_entities_in_single_view", "cloud_domain_snap_trees_info", "is_app_notified", "archive_metadata_cloud_location", "cloud_tier_setting", "entity_view_metadata_map", "archive_worm_properties", "is_cad_archive", "software_version", "dummy_data_vec", "is_rpaas_job", "non_finalized_object_vec", "scribe_metadata_id_ceiling", "is_cohesion_copy_job", "is_metadata_full_archive")
    class EntityMappingInfo(_message.Message):
        __slots__ = ("entity_id_map", "registered_source")
        class EntityIdMapEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: int
            value: int
            def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
        ENTITY_ID_MAP_FIELD_NUMBER: _ClassVar[int]
        REGISTERED_SOURCE_FIELD_NUMBER: _ClassVar[int]
        entity_id_map: _containers.ScalarMap[int, int]
        registered_source: _entity_pb2.EntityProto
        def __init__(self, entity_id_map: _Optional[_Mapping[int, int]] = ..., registered_source: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ...) -> None: ...
    class IndexInfo(_message.Message):
        __slots__ = ("fs_name", "index_files_parent_dir_path", "index_size_bytes")
        FS_NAME_FIELD_NUMBER: _ClassVar[int]
        INDEX_FILES_PARENT_DIR_PATH_FIELD_NUMBER: _ClassVar[int]
        INDEX_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
        fs_name: str
        index_files_parent_dir_path: str
        index_size_bytes: int
        def __init__(self, fs_name: _Optional[str] = ..., index_files_parent_dir_path: _Optional[str] = ..., index_size_bytes: _Optional[int] = ...) -> None: ...
    class StubViewInfo(_message.Message):
        __slots__ = ("view_id", "last_access_time_usecs", "entity_id", "local_fs_snap_tree_info_vec", "error", "restore_job_uid", "view_name", "expiry_timestamp_usecs", "uptier_expiry_timestamp_usecs", "creation_timestamp_usecs", "reuse_restored_view_snap_tree_nodes")
        class LocalFsSnapTreeInfo(_message.Message):
            __slots__ = ("fs_name", "tree_id", "root_inode_id")
            FS_NAME_FIELD_NUMBER: _ClassVar[int]
            TREE_ID_FIELD_NUMBER: _ClassVar[int]
            ROOT_INODE_ID_FIELD_NUMBER: _ClassVar[int]
            fs_name: str
            tree_id: int
            root_inode_id: int
            def __init__(self, fs_name: _Optional[str] = ..., tree_id: _Optional[int] = ..., root_inode_id: _Optional[int] = ...) -> None: ...
        VIEW_ID_FIELD_NUMBER: _ClassVar[int]
        LAST_ACCESS_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
        ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
        LOCAL_FS_SNAP_TREE_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        RESTORE_JOB_UID_FIELD_NUMBER: _ClassVar[int]
        VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
        EXPIRY_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
        UPTIER_EXPIRY_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
        CREATION_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
        REUSE_RESTORED_VIEW_SNAP_TREE_NODES_FIELD_NUMBER: _ClassVar[int]
        view_id: int
        last_access_time_usecs: int
        entity_id: int
        local_fs_snap_tree_info_vec: _containers.RepeatedCompositeFieldContainer[ArchiveMetadataProto.StubViewInfo.LocalFsSnapTreeInfo]
        error: _error_pb2.ErrorProto
        restore_job_uid: _universal_id_pb2.UniversalIdProto
        view_name: str
        expiry_timestamp_usecs: int
        uptier_expiry_timestamp_usecs: int
        creation_timestamp_usecs: int
        reuse_restored_view_snap_tree_nodes: bool
        def __init__(self, view_id: _Optional[int] = ..., last_access_time_usecs: _Optional[int] = ..., entity_id: _Optional[int] = ..., local_fs_snap_tree_info_vec: _Optional[_Iterable[_Union[ArchiveMetadataProto.StubViewInfo.LocalFsSnapTreeInfo, _Mapping]]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., restore_job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., view_name: _Optional[str] = ..., expiry_timestamp_usecs: _Optional[int] = ..., uptier_expiry_timestamp_usecs: _Optional[int] = ..., creation_timestamp_usecs: _Optional[int] = ..., reuse_restored_view_snap_tree_nodes: bool = ...) -> None: ...
    class EntityViewMetadataMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _view_metadata_pb2.ViewIdMappingProto
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_view_metadata_pb2.ViewIdMappingProto, _Mapping]] = ...) -> None: ...
    ARCHIVE_UID_FIELD_NUMBER: _ClassVar[int]
    VAULT_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_UID_VEC_FIELD_NUMBER: _ClassVar[int]
    METADATA_OBJECT_UID_VEC_FIELD_NUMBER: _ClassVar[int]
    LOGICAL_ARCHIVE_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    PHYSICAL_ARCHIVE_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    END_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    JOB_STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    EXPIRY_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_MONITOR_TASK_PATH_FIELD_NUMBER: _ClassVar[int]
    ENTITY_METADATA_VEC_FIELD_NUMBER: _ClassVar[int]
    JOB_UID_FIELD_NUMBER: _ClassVar[int]
    JOB_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    IS_VIEW_ARCHIVE_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_METADATA_FIELD_NUMBER: _ClassVar[int]
    IS_REFERENCE_ARCHIVE_FIELD_NUMBER: _ClassVar[int]
    IS_RETIRED_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    ARCHIVED_VIEW_INODE_ID_FLOOR_FIELD_NUMBER: _ClassVar[int]
    VIEW_SNAP_TREE_KEYS_MAPPED_FIELD_NUMBER: _ClassVar[int]
    ARCHIVE_OBJECT_METADATA_VEC_FIELD_NUMBER: _ClassVar[int]
    LOGICAL_BYTES_PROCESSED_FIELD_NUMBER: _ClassVar[int]
    ARCHIVE_STATS_FIELD_NUMBER: _ClassVar[int]
    OPCLOCK_VEC_FIELD_NUMBER: _ClassVar[int]
    NON_FINALIZED_OBJECT_NAME_VEC_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    JOB_RUN_METADATA_FIELD_NUMBER: _ClassVar[int]
    ENTITY_MAPPING_INFO_FIELD_NUMBER: _ClassVar[int]
    INDEX_INFO_FIELD_NUMBER: _ClassVar[int]
    VIEW_METADATA_FIELD_NUMBER: _ClassVar[int]
    APP_JOB_TYPE_FIELD_NUMBER: _ClassVar[int]
    ARCHIVE_STUB_VIEW_INFO_FIELD_NUMBER: _ClassVar[int]
    ENTITY_STUB_VIEW_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    ORIGINAL_EXPIRY_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_NAME_FIELD_NUMBER: _ClassVar[int]
    USE_RESTORE_OBJECTS_MANAGER_FIELD_NUMBER: _ClassVar[int]
    WORM_POLICY_TYPE_FIELD_NUMBER: _ClassVar[int]
    DATA_LOCK_CONSTRAINTS_FIELD_NUMBER: _ClassVar[int]
    ON_LEGAL_HOLD_FIELD_NUMBER: _ClassVar[int]
    IS_DIRECT_ARCHIVE_FIELD_NUMBER: _ClassVar[int]
    IS_DATA_IN_NATIVE_FORMAT_FIELD_NUMBER: _ClassVar[int]
    NUM_PADDED_BYTES_FIELD_NUMBER: _ClassVar[int]
    ARCHIVE_ENTITIES_IN_SINGLE_VIEW_FIELD_NUMBER: _ClassVar[int]
    CLOUD_DOMAIN_SNAP_TREES_INFO_FIELD_NUMBER: _ClassVar[int]
    IS_APP_NOTIFIED_FIELD_NUMBER: _ClassVar[int]
    ARCHIVE_METADATA_CLOUD_LOCATION_FIELD_NUMBER: _ClassVar[int]
    CLOUD_TIER_SETTING_FIELD_NUMBER: _ClassVar[int]
    ENTITY_VIEW_METADATA_MAP_FIELD_NUMBER: _ClassVar[int]
    ARCHIVE_WORM_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    IS_CAD_ARCHIVE_FIELD_NUMBER: _ClassVar[int]
    SOFTWARE_VERSION_FIELD_NUMBER: _ClassVar[int]
    DUMMY_DATA_VEC_FIELD_NUMBER: _ClassVar[int]
    IS_RPAAS_JOB_FIELD_NUMBER: _ClassVar[int]
    NON_FINALIZED_OBJECT_VEC_FIELD_NUMBER: _ClassVar[int]
    SCRIBE_METADATA_ID_CEILING_FIELD_NUMBER: _ClassVar[int]
    IS_COHESION_COPY_JOB_FIELD_NUMBER: _ClassVar[int]
    IS_METADATA_FULL_ARCHIVE_FIELD_NUMBER: _ClassVar[int]
    archive_uid: _universal_id_pb2.UniversalIdProto
    vault_id: int
    object_uid_vec: _containers.RepeatedCompositeFieldContainer[_universal_id_pb2.UniversalIdProto]
    metadata_object_uid_vec: _containers.RepeatedCompositeFieldContainer[_universal_id_pb2.UniversalIdProto]
    logical_archive_size_bytes: int
    physical_archive_size_bytes: int
    start_time_usecs: int
    end_time_usecs: int
    job_status: IceboxJobStatus
    error: _error_pb2.ErrorProto
    expiry_timestamp_usecs: int
    progress_monitor_task_path: str
    entity_metadata_vec: _containers.RepeatedCompositeFieldContainer[EntityMetadataProto]
    job_uid: _universal_id_pb2.UniversalIdProto
    job_instance_id: int
    is_view_archive: bool
    version: int
    snapshot_metadata: ArchiveSnapshotMetadataProto
    is_reference_archive: bool
    is_retired_reference: bool
    archived_view_inode_id_floor: int
    view_snap_tree_keys_mapped: bool
    archive_object_metadata_vec: _containers.RepeatedCompositeFieldContainer[ArchiveObjectScribeMetadataProto]
    logical_bytes_processed: int
    archive_stats: ArchiveBlobTaskStats
    opclock_vec: _containers.RepeatedCompositeFieldContainer[_op_clock_pb2.OpClock]
    non_finalized_object_name_vec: _containers.RepeatedScalarFieldContainer[str]
    snapshot_time_usecs: int
    job_run_metadata: _master_pb2.BackupRunArchiveMDProto
    entity_mapping_info: ArchiveMetadataProto.EntityMappingInfo
    index_info: ArchiveMetadataProto.IndexInfo
    view_metadata: _view_metadata_pb2.ViewIdMappingProto
    app_job_type: _enums_pb2.Environment.Type
    archive_stub_view_info: ArchiveMetadataProto.StubViewInfo
    entity_stub_view_info_vec: _containers.RepeatedCompositeFieldContainer[ArchiveMetadataProto.StubViewInfo]
    original_expiry_timestamp_usecs: int
    cluster_name: str
    use_restore_objects_manager: bool
    worm_policy_type: _worm_pb2.WormRetentionProto.WormPolicyType
    data_lock_constraints: _worm_pb2.DataLockConstraintsProto
    on_legal_hold: bool
    is_direct_archive: bool
    is_data_in_native_format: bool
    num_padded_bytes: int
    archive_entities_in_single_view: bool
    cloud_domain_snap_trees_info: CloudDomainSnapTreesInfoProto
    is_app_notified: bool
    archive_metadata_cloud_location: _cloud_pb2.CloudNodePrefixPtrProto
    cloud_tier_setting: _cluster_config_pb2.ClusterConfigProto.Vault.CloudTierSetting
    entity_view_metadata_map: _containers.MessageMap[int, _view_metadata_pb2.ViewIdMappingProto]
    archive_worm_properties: _worm_pb2.ArchiveWORMProperties
    is_cad_archive: bool
    software_version: str
    dummy_data_vec: _containers.RepeatedScalarFieldContainer[str]
    is_rpaas_job: bool
    non_finalized_object_vec: _containers.RepeatedCompositeFieldContainer[_universal_id_pb2.UniversalIdProto]
    scribe_metadata_id_ceiling: int
    is_cohesion_copy_job: bool
    is_metadata_full_archive: bool
    def __init__(self, archive_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., vault_id: _Optional[int] = ..., object_uid_vec: _Optional[_Iterable[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]]] = ..., metadata_object_uid_vec: _Optional[_Iterable[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]]] = ..., logical_archive_size_bytes: _Optional[int] = ..., physical_archive_size_bytes: _Optional[int] = ..., start_time_usecs: _Optional[int] = ..., end_time_usecs: _Optional[int] = ..., job_status: _Optional[_Union[IceboxJobStatus, str]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., expiry_timestamp_usecs: _Optional[int] = ..., progress_monitor_task_path: _Optional[str] = ..., entity_metadata_vec: _Optional[_Iterable[_Union[EntityMetadataProto, _Mapping]]] = ..., job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., job_instance_id: _Optional[int] = ..., is_view_archive: bool = ..., version: _Optional[int] = ..., snapshot_metadata: _Optional[_Union[ArchiveSnapshotMetadataProto, _Mapping]] = ..., is_reference_archive: bool = ..., is_retired_reference: bool = ..., archived_view_inode_id_floor: _Optional[int] = ..., view_snap_tree_keys_mapped: bool = ..., archive_object_metadata_vec: _Optional[_Iterable[_Union[ArchiveObjectScribeMetadataProto, _Mapping]]] = ..., logical_bytes_processed: _Optional[int] = ..., archive_stats: _Optional[_Union[ArchiveBlobTaskStats, _Mapping]] = ..., opclock_vec: _Optional[_Iterable[_Union[_op_clock_pb2.OpClock, _Mapping]]] = ..., non_finalized_object_name_vec: _Optional[_Iterable[str]] = ..., snapshot_time_usecs: _Optional[int] = ..., job_run_metadata: _Optional[_Union[_master_pb2.BackupRunArchiveMDProto, _Mapping]] = ..., entity_mapping_info: _Optional[_Union[ArchiveMetadataProto.EntityMappingInfo, _Mapping]] = ..., index_info: _Optional[_Union[ArchiveMetadataProto.IndexInfo, _Mapping]] = ..., view_metadata: _Optional[_Union[_view_metadata_pb2.ViewIdMappingProto, _Mapping]] = ..., app_job_type: _Optional[_Union[_enums_pb2.Environment.Type, str]] = ..., archive_stub_view_info: _Optional[_Union[ArchiveMetadataProto.StubViewInfo, _Mapping]] = ..., entity_stub_view_info_vec: _Optional[_Iterable[_Union[ArchiveMetadataProto.StubViewInfo, _Mapping]]] = ..., original_expiry_timestamp_usecs: _Optional[int] = ..., cluster_name: _Optional[str] = ..., use_restore_objects_manager: bool = ..., worm_policy_type: _Optional[_Union[_worm_pb2.WormRetentionProto.WormPolicyType, str]] = ..., data_lock_constraints: _Optional[_Union[_worm_pb2.DataLockConstraintsProto, _Mapping]] = ..., on_legal_hold: bool = ..., is_direct_archive: bool = ..., is_data_in_native_format: bool = ..., num_padded_bytes: _Optional[int] = ..., archive_entities_in_single_view: bool = ..., cloud_domain_snap_trees_info: _Optional[_Union[CloudDomainSnapTreesInfoProto, _Mapping]] = ..., is_app_notified: bool = ..., archive_metadata_cloud_location: _Optional[_Union[_cloud_pb2.CloudNodePrefixPtrProto, _Mapping]] = ..., cloud_tier_setting: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.Vault.CloudTierSetting, _Mapping]] = ..., entity_view_metadata_map: _Optional[_Mapping[int, _view_metadata_pb2.ViewIdMappingProto]] = ..., archive_worm_properties: _Optional[_Union[_worm_pb2.ArchiveWORMProperties, _Mapping]] = ..., is_cad_archive: bool = ..., software_version: _Optional[str] = ..., dummy_data_vec: _Optional[_Iterable[str]] = ..., is_rpaas_job: bool = ..., non_finalized_object_vec: _Optional[_Iterable[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]]] = ..., scribe_metadata_id_ceiling: _Optional[int] = ..., is_cohesion_copy_job: bool = ..., is_metadata_full_archive: bool = ...) -> None: ...

class ArchiveObjectScribeMetadataProto(_message.Message):
    __slots__ = ("object_uid", "object_name", "metadata", "logical_size_bytes", "physical_size_bytes", "start_time_usecs", "end_time_usecs", "modified_time_usecs", "version_id", "worm_retention_time_usecs", "object_type")
    OBJECT_UID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_NAME_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    LOGICAL_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    PHYSICAL_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    END_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    MODIFIED_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    VERSION_ID_FIELD_NUMBER: _ClassVar[int]
    WORM_RETENTION_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    OBJECT_TYPE_FIELD_NUMBER: _ClassVar[int]
    object_uid: _universal_id_pb2.UniversalIdProto
    object_name: bytes
    metadata: ArchivalObjectMetadataProto
    logical_size_bytes: int
    physical_size_bytes: int
    start_time_usecs: int
    end_time_usecs: int
    modified_time_usecs: int
    version_id: str
    worm_retention_time_usecs: int
    object_type: ArchivalObjectMetadataProto.ObjectType
    def __init__(self, object_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., object_name: _Optional[bytes] = ..., metadata: _Optional[_Union[ArchivalObjectMetadataProto, _Mapping]] = ..., logical_size_bytes: _Optional[int] = ..., physical_size_bytes: _Optional[int] = ..., start_time_usecs: _Optional[int] = ..., end_time_usecs: _Optional[int] = ..., modified_time_usecs: _Optional[int] = ..., version_id: _Optional[str] = ..., worm_retention_time_usecs: _Optional[int] = ..., object_type: _Optional[_Union[ArchivalObjectMetadataProto.ObjectType, str]] = ...) -> None: ...

class StubViewInfo(_message.Message):
    __slots__ = ("entity_dir_path", "entity_id", "stub_view_name", "stub_view_id", "internal_view_name", "progress_monitor_task_path", "existing_uptier_expiry_timestamp_usecs")
    ENTITY_DIR_PATH_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    STUB_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    STUB_VIEW_ID_FIELD_NUMBER: _ClassVar[int]
    INTERNAL_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_MONITOR_TASK_PATH_FIELD_NUMBER: _ClassVar[int]
    EXISTING_UPTIER_EXPIRY_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
    entity_dir_path: str
    entity_id: int
    stub_view_name: str
    stub_view_id: int
    internal_view_name: str
    progress_monitor_task_path: str
    existing_uptier_expiry_timestamp_usecs: int
    def __init__(self, entity_dir_path: _Optional[str] = ..., entity_id: _Optional[int] = ..., stub_view_name: _Optional[str] = ..., stub_view_id: _Optional[int] = ..., internal_view_name: _Optional[str] = ..., progress_monitor_task_path: _Optional[str] = ..., existing_uptier_expiry_timestamp_usecs: _Optional[int] = ...) -> None: ...

class RestoreJobMetadataProto(_message.Message):
    __slots__ = ("restore_job_uid", "archive_uid", "logical_size_bytes", "physical_size_bytes", "start_time_usecs", "end_time_usecs", "job_status", "error", "entity_metadata_vec", "application_name", "target_view_name", "stub_view_info_vec", "entity_internal_view_name_map", "num_files_found", "num_files_restored", "is_uptier_restore_job", "progress_monitor_task_path", "is_download_index_job", "stub_view_info", "restore_object_data_vec", "restored_object_uid_vec", "uptier_job_metadata", "user_info")
    class EntityInternalViewNameMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: str
        def __init__(self, key: _Optional[int] = ..., value: _Optional[str] = ...) -> None: ...
    RESTORE_JOB_UID_FIELD_NUMBER: _ClassVar[int]
    ARCHIVE_UID_FIELD_NUMBER: _ClassVar[int]
    LOGICAL_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    PHYSICAL_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    END_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    JOB_STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ENTITY_METADATA_VEC_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_NAME_FIELD_NUMBER: _ClassVar[int]
    TARGET_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    STUB_VIEW_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    ENTITY_INTERNAL_VIEW_NAME_MAP_FIELD_NUMBER: _ClassVar[int]
    NUM_FILES_FOUND_FIELD_NUMBER: _ClassVar[int]
    NUM_FILES_RESTORED_FIELD_NUMBER: _ClassVar[int]
    IS_UPTIER_RESTORE_JOB_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_MONITOR_TASK_PATH_FIELD_NUMBER: _ClassVar[int]
    IS_DOWNLOAD_INDEX_JOB_FIELD_NUMBER: _ClassVar[int]
    STUB_VIEW_INFO_FIELD_NUMBER: _ClassVar[int]
    RESTORE_OBJECT_DATA_VEC_FIELD_NUMBER: _ClassVar[int]
    RESTORED_OBJECT_UID_VEC_FIELD_NUMBER: _ClassVar[int]
    UPTIER_JOB_METADATA_FIELD_NUMBER: _ClassVar[int]
    USER_INFO_FIELD_NUMBER: _ClassVar[int]
    restore_job_uid: _universal_id_pb2.UniversalIdProto
    archive_uid: _universal_id_pb2.UniversalIdProto
    logical_size_bytes: int
    physical_size_bytes: int
    start_time_usecs: int
    end_time_usecs: int
    job_status: IceboxJobStatus
    error: _error_pb2.ErrorProto
    entity_metadata_vec: _containers.RepeatedCompositeFieldContainer[RestoreJobEntityMetadataProto]
    application_name: str
    target_view_name: str
    stub_view_info_vec: _containers.RepeatedCompositeFieldContainer[StubViewInfo]
    entity_internal_view_name_map: _containers.ScalarMap[int, str]
    num_files_found: int
    num_files_restored: int
    is_uptier_restore_job: bool
    progress_monitor_task_path: str
    is_download_index_job: bool
    stub_view_info: StubViewInfo
    restore_object_data_vec: _containers.RepeatedCompositeFieldContainer[TaskCheckpointInfo.RestoreObjectData]
    restored_object_uid_vec: _containers.RepeatedCompositeFieldContainer[_universal_id_pb2.UniversalIdProto]
    uptier_job_metadata: bytes
    user_info: _permissions_pb2.UserInformation
    def __init__(self, restore_job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., archive_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., logical_size_bytes: _Optional[int] = ..., physical_size_bytes: _Optional[int] = ..., start_time_usecs: _Optional[int] = ..., end_time_usecs: _Optional[int] = ..., job_status: _Optional[_Union[IceboxJobStatus, str]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., entity_metadata_vec: _Optional[_Iterable[_Union[RestoreJobEntityMetadataProto, _Mapping]]] = ..., application_name: _Optional[str] = ..., target_view_name: _Optional[str] = ..., stub_view_info_vec: _Optional[_Iterable[_Union[StubViewInfo, _Mapping]]] = ..., entity_internal_view_name_map: _Optional[_Mapping[int, str]] = ..., num_files_found: _Optional[int] = ..., num_files_restored: _Optional[int] = ..., is_uptier_restore_job: bool = ..., progress_monitor_task_path: _Optional[str] = ..., is_download_index_job: bool = ..., stub_view_info: _Optional[_Union[StubViewInfo, _Mapping]] = ..., restore_object_data_vec: _Optional[_Iterable[_Union[TaskCheckpointInfo.RestoreObjectData, _Mapping]]] = ..., restored_object_uid_vec: _Optional[_Iterable[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]]] = ..., uptier_job_metadata: _Optional[bytes] = ..., user_info: _Optional[_Union[_permissions_pb2.UserInformation, _Mapping]] = ...) -> None: ...

class RestoreJobEntityMetadataProto(_message.Message):
    __slots__ = ("entity_id", "status", "error", "start_timestamp_usecs", "end_timestamp_usecs", "logical_size_bytes", "physical_size_bytes", "view_name")
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    START_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
    END_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
    LOGICAL_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    PHYSICAL_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    entity_id: int
    status: IceboxJobStatus
    error: _error_pb2.ErrorProto
    start_timestamp_usecs: int
    end_timestamp_usecs: int
    logical_size_bytes: int
    physical_size_bytes: int
    view_name: str
    def __init__(self, entity_id: _Optional[int] = ..., status: _Optional[_Union[IceboxJobStatus, str]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., start_timestamp_usecs: _Optional[int] = ..., end_timestamp_usecs: _Optional[int] = ..., logical_size_bytes: _Optional[int] = ..., physical_size_bytes: _Optional[int] = ..., view_name: _Optional[str] = ...) -> None: ...

class BlobDataRanges(_message.Message):
    __slots__ = ("range_vec",)
    class BlobRange(_message.Message):
        __slots__ = ("offset", "size")
        OFFSET_FIELD_NUMBER: _ClassVar[int]
        SIZE_FIELD_NUMBER: _ClassVar[int]
        offset: int
        size: int
        def __init__(self, offset: _Optional[int] = ..., size: _Optional[int] = ...) -> None: ...
    RANGE_VEC_FIELD_NUMBER: _ClassVar[int]
    range_vec: _containers.RepeatedCompositeFieldContainer[BlobDataRanges.BlobRange]
    def __init__(self, range_vec: _Optional[_Iterable[_Union[BlobDataRanges.BlobRange, _Mapping]]] = ...) -> None: ...

class ArchiveWORMStats(_message.Message):
    __slots__ = ("num_nodes_visited_for_msr", "num_cloud_chunk_files_retention_extended", "num_csr_objects_retention_extended", "num_data_bytes_rearchived", "num_snap_tree_nodes_rearchived", "num_chunks_rearchived")
    NUM_NODES_VISITED_FOR_MSR_FIELD_NUMBER: _ClassVar[int]
    NUM_CLOUD_CHUNK_FILES_RETENTION_EXTENDED_FIELD_NUMBER: _ClassVar[int]
    NUM_CSR_OBJECTS_RETENTION_EXTENDED_FIELD_NUMBER: _ClassVar[int]
    NUM_DATA_BYTES_REARCHIVED_FIELD_NUMBER: _ClassVar[int]
    NUM_SNAP_TREE_NODES_REARCHIVED_FIELD_NUMBER: _ClassVar[int]
    NUM_CHUNKS_REARCHIVED_FIELD_NUMBER: _ClassVar[int]
    num_nodes_visited_for_msr: int
    num_cloud_chunk_files_retention_extended: int
    num_csr_objects_retention_extended: int
    num_data_bytes_rearchived: int
    num_snap_tree_nodes_rearchived: int
    num_chunks_rearchived: int
    def __init__(self, num_nodes_visited_for_msr: _Optional[int] = ..., num_cloud_chunk_files_retention_extended: _Optional[int] = ..., num_csr_objects_retention_extended: _Optional[int] = ..., num_data_bytes_rearchived: _Optional[int] = ..., num_snap_tree_nodes_rearchived: _Optional[int] = ..., num_chunks_rearchived: _Optional[int] = ...) -> None: ...

class TaskCheckpointInfo(_message.Message):
    __slots__ = ("progress_type", "entity_id", "restore_job_uid", "file_data", "object_data", "restore_object_data_vec", "entity_data", "timestamp_usecs", "latency_usecs", "snap_tree_data", "fs_snap_tree_info_vec", "hardlink_map", "chunk_db_file_info", "referred_object_uid_vec", "task_finished", "referred_archive_uid_vec", "restore_stats", "archive_stats", "range_download_info_vec", "list_objects_data", "read_metadata_object_map", "build_file_index_data", "create_index_files_data", "create_stub_view_data", "get_files_to_upload_data", "upload_files_data", "prefetch_files_data", "quota_snap_tree_info", "hydration_info", "resolved_all_update_intents", "copy_file_info", "blob_data_location_vec", "data_object_vec", "prefetch_snap_tree_nodes_data", "download_snap_tree_object_info", "archive_view_snap_tree_task_stats", "objects_validation_info", "cleanup_da_objects_info", "archive_object_restore_info_map", "num_padded_bytes", "uptier_data_info", "downtier_data_info", "view_snap_tree_info_vec", "fix_update_intents_info", "archive_metadata_cloud_location", "uptier_cloud_domain_data_info", "list_cloud_domains_data", "list_archive_metadata_objects_data", "read_archive_metadata_object_map", "archive_metadata_object_data", "archive_task_worm_stats")
    class ProgressType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kArchivalObjectCreated: _ClassVar[TaskCheckpointInfo.ProgressType]
        kArchivalObjectFinalized: _ClassVar[TaskCheckpointInfo.ProgressType]
        kEntityArchivalStarted: _ClassVar[TaskCheckpointInfo.ProgressType]
        kEntityArchivalFinished: _ClassVar[TaskCheckpointInfo.ProgressType]
        kArchivalTaskProgress: _ClassVar[TaskCheckpointInfo.ProgressType]
        kObjectRestoreStarted: _ClassVar[TaskCheckpointInfo.ProgressType]
        kEntityRestoreStarted: _ClassVar[TaskCheckpointInfo.ProgressType]
        kEntityRestoreFinished: _ClassVar[TaskCheckpointInfo.ProgressType]
        kRestoreTaskProgress: _ClassVar[TaskCheckpointInfo.ProgressType]
        kArchiveTaskComplete: _ClassVar[TaskCheckpointInfo.ProgressType]
        kRestoreTaskComplete: _ClassVar[TaskCheckpointInfo.ProgressType]
        kListObjectsTaskProgress: _ClassVar[TaskCheckpointInfo.ProgressType]
        kListObjectsTaskComplete: _ClassVar[TaskCheckpointInfo.ProgressType]
        kReadMetadataTaskProgress: _ClassVar[TaskCheckpointInfo.ProgressType]
        kReadMetadataTaskComplete: _ClassVar[TaskCheckpointInfo.ProgressType]
        kBuildIndexTaskProgress: _ClassVar[TaskCheckpointInfo.ProgressType]
        kBuildIndexTaskComplete: _ClassVar[TaskCheckpointInfo.ProgressType]
        kMasterWorkerTaskComplete: _ClassVar[TaskCheckpointInfo.ProgressType]
        kTaskProgress: _ClassVar[TaskCheckpointInfo.ProgressType]
        kTaskComplete: _ClassVar[TaskCheckpointInfo.ProgressType]
        kArchivalObjectAborted: _ClassVar[TaskCheckpointInfo.ProgressType]
        kSkippedObjectFinalization: _ClassVar[TaskCheckpointInfo.ProgressType]
        kListCloudDomainsTaskProgress: _ClassVar[TaskCheckpointInfo.ProgressType]
        kListCloudDomainsTaskComplete: _ClassVar[TaskCheckpointInfo.ProgressType]
        kFindAccessibleCloudDomainsTaskProgress: _ClassVar[TaskCheckpointInfo.ProgressType]
        kFindAccessibleCloudDomainsTaskComplete: _ClassVar[TaskCheckpointInfo.ProgressType]
        kListArchiveMetadataObjectsTaskProgress: _ClassVar[TaskCheckpointInfo.ProgressType]
        kListArchiveMetadataObjectsTaskComplete: _ClassVar[TaskCheckpointInfo.ProgressType]
        kReadArchiveMetadataFromCSRTaskProgress: _ClassVar[TaskCheckpointInfo.ProgressType]
        kReadArchiveMetadataFromCSRTaskComplete: _ClassVar[TaskCheckpointInfo.ProgressType]
        kSetWORMObjectRetentionTaskProgress: _ClassVar[TaskCheckpointInfo.ProgressType]
        kSetWORMObjectRetentionTaskComplete: _ClassVar[TaskCheckpointInfo.ProgressType]
        kPopulateCloudDomainEntriesInScribeComplete: _ClassVar[TaskCheckpointInfo.ProgressType]
    kArchivalObjectCreated: TaskCheckpointInfo.ProgressType
    kArchivalObjectFinalized: TaskCheckpointInfo.ProgressType
    kEntityArchivalStarted: TaskCheckpointInfo.ProgressType
    kEntityArchivalFinished: TaskCheckpointInfo.ProgressType
    kArchivalTaskProgress: TaskCheckpointInfo.ProgressType
    kObjectRestoreStarted: TaskCheckpointInfo.ProgressType
    kEntityRestoreStarted: TaskCheckpointInfo.ProgressType
    kEntityRestoreFinished: TaskCheckpointInfo.ProgressType
    kRestoreTaskProgress: TaskCheckpointInfo.ProgressType
    kArchiveTaskComplete: TaskCheckpointInfo.ProgressType
    kRestoreTaskComplete: TaskCheckpointInfo.ProgressType
    kListObjectsTaskProgress: TaskCheckpointInfo.ProgressType
    kListObjectsTaskComplete: TaskCheckpointInfo.ProgressType
    kReadMetadataTaskProgress: TaskCheckpointInfo.ProgressType
    kReadMetadataTaskComplete: TaskCheckpointInfo.ProgressType
    kBuildIndexTaskProgress: TaskCheckpointInfo.ProgressType
    kBuildIndexTaskComplete: TaskCheckpointInfo.ProgressType
    kMasterWorkerTaskComplete: TaskCheckpointInfo.ProgressType
    kTaskProgress: TaskCheckpointInfo.ProgressType
    kTaskComplete: TaskCheckpointInfo.ProgressType
    kArchivalObjectAborted: TaskCheckpointInfo.ProgressType
    kSkippedObjectFinalization: TaskCheckpointInfo.ProgressType
    kListCloudDomainsTaskProgress: TaskCheckpointInfo.ProgressType
    kListCloudDomainsTaskComplete: TaskCheckpointInfo.ProgressType
    kFindAccessibleCloudDomainsTaskProgress: TaskCheckpointInfo.ProgressType
    kFindAccessibleCloudDomainsTaskComplete: TaskCheckpointInfo.ProgressType
    kListArchiveMetadataObjectsTaskProgress: TaskCheckpointInfo.ProgressType
    kListArchiveMetadataObjectsTaskComplete: TaskCheckpointInfo.ProgressType
    kReadArchiveMetadataFromCSRTaskProgress: TaskCheckpointInfo.ProgressType
    kReadArchiveMetadataFromCSRTaskComplete: TaskCheckpointInfo.ProgressType
    kSetWORMObjectRetentionTaskProgress: TaskCheckpointInfo.ProgressType
    kSetWORMObjectRetentionTaskComplete: TaskCheckpointInfo.ProgressType
    kPopulateCloudDomainEntriesInScribeComplete: TaskCheckpointInfo.ProgressType
    class BlobObjectRange(_message.Message):
        __slots__ = ("range", "offset")
        RANGE_FIELD_NUMBER: _ClassVar[int]
        OFFSET_FIELD_NUMBER: _ClassVar[int]
        range: _cloud_pb2.ArchiveDataRange
        offset: int
        def __init__(self, range: _Optional[_Union[_cloud_pb2.ArchiveDataRange, _Mapping]] = ..., offset: _Optional[int] = ...) -> None: ...
    class FileData(_message.Message):
        __slots__ = ("fs_name", "file_name", "file_offset", "file_metadata", "inode_id", "blob_snap_tree_id", "blob_restore_in_progress", "blob_object_range_vec", "fs_entry_index", "max_restore_blob_portion_size_bytes", "end_offset", "blob_info_vec_index", "brick_size", "last_validated_blob_info_idx")
        FS_NAME_FIELD_NUMBER: _ClassVar[int]
        FILE_NAME_FIELD_NUMBER: _ClassVar[int]
        FILE_OFFSET_FIELD_NUMBER: _ClassVar[int]
        FILE_METADATA_FIELD_NUMBER: _ClassVar[int]
        INODE_ID_FIELD_NUMBER: _ClassVar[int]
        BLOB_SNAP_TREE_ID_FIELD_NUMBER: _ClassVar[int]
        BLOB_RESTORE_IN_PROGRESS_FIELD_NUMBER: _ClassVar[int]
        BLOB_OBJECT_RANGE_VEC_FIELD_NUMBER: _ClassVar[int]
        FS_ENTRY_INDEX_FIELD_NUMBER: _ClassVar[int]
        MAX_RESTORE_BLOB_PORTION_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
        END_OFFSET_FIELD_NUMBER: _ClassVar[int]
        BLOB_INFO_VEC_INDEX_FIELD_NUMBER: _ClassVar[int]
        BRICK_SIZE_FIELD_NUMBER: _ClassVar[int]
        LAST_VALIDATED_BLOB_INFO_IDX_FIELD_NUMBER: _ClassVar[int]
        fs_name: str
        file_name: str
        file_offset: int
        file_metadata: FileMetadataProto
        inode_id: int
        blob_snap_tree_id: int
        blob_restore_in_progress: bool
        blob_object_range_vec: _containers.RepeatedCompositeFieldContainer[TaskCheckpointInfo.BlobObjectRange]
        fs_entry_index: int
        max_restore_blob_portion_size_bytes: int
        end_offset: int
        blob_info_vec_index: int
        brick_size: int
        last_validated_blob_info_idx: int
        def __init__(self, fs_name: _Optional[str] = ..., file_name: _Optional[str] = ..., file_offset: _Optional[int] = ..., file_metadata: _Optional[_Union[FileMetadataProto, _Mapping]] = ..., inode_id: _Optional[int] = ..., blob_snap_tree_id: _Optional[int] = ..., blob_restore_in_progress: bool = ..., blob_object_range_vec: _Optional[_Iterable[_Union[TaskCheckpointInfo.BlobObjectRange, _Mapping]]] = ..., fs_entry_index: _Optional[int] = ..., max_restore_blob_portion_size_bytes: _Optional[int] = ..., end_offset: _Optional[int] = ..., blob_info_vec_index: _Optional[int] = ..., brick_size: _Optional[int] = ..., last_validated_blob_info_idx: _Optional[int] = ...) -> None: ...
    class JournalInfo(_message.Message):
        __slots__ = ("journal_view_name", "journal_fs_name", "journal_file_rel_path", "journal_file_size_bytes", "num_bytes_read", "finalize_object_after_part")
        JOURNAL_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
        JOURNAL_FS_NAME_FIELD_NUMBER: _ClassVar[int]
        JOURNAL_FILE_REL_PATH_FIELD_NUMBER: _ClassVar[int]
        JOURNAL_FILE_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
        NUM_BYTES_READ_FIELD_NUMBER: _ClassVar[int]
        FINALIZE_OBJECT_AFTER_PART_FIELD_NUMBER: _ClassVar[int]
        journal_view_name: str
        journal_fs_name: str
        journal_file_rel_path: str
        journal_file_size_bytes: int
        num_bytes_read: int
        finalize_object_after_part: bool
        def __init__(self, journal_view_name: _Optional[str] = ..., journal_fs_name: _Optional[str] = ..., journal_file_rel_path: _Optional[str] = ..., journal_file_size_bytes: _Optional[int] = ..., num_bytes_read: _Optional[int] = ..., finalize_object_after_part: bool = ...) -> None: ...
    class ObjectData(_message.Message):
        __slots__ = ("object_uid", "name", "offset", "upload_context", "download_context", "archival_object_metadata", "last_part_num", "num_bytes_read", "num_bytes_written", "chunks_to_finalize_vec", "blob_object_range_map", "segment_start_offset_vec", "journal_info", "finalize_in_progress", "object_part_size", "skipped_finalization", "creation_time_usecs", "finalization_time_usecs", "object_version_id")
        class BlobObjectRangeMapEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: int
            value: _cloud_pb2.ArchiveDataRange
            def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_cloud_pb2.ArchiveDataRange, _Mapping]] = ...) -> None: ...
        OBJECT_UID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        OFFSET_FIELD_NUMBER: _ClassVar[int]
        UPLOAD_CONTEXT_FIELD_NUMBER: _ClassVar[int]
        DOWNLOAD_CONTEXT_FIELD_NUMBER: _ClassVar[int]
        ARCHIVAL_OBJECT_METADATA_FIELD_NUMBER: _ClassVar[int]
        LAST_PART_NUM_FIELD_NUMBER: _ClassVar[int]
        NUM_BYTES_READ_FIELD_NUMBER: _ClassVar[int]
        NUM_BYTES_WRITTEN_FIELD_NUMBER: _ClassVar[int]
        CHUNKS_TO_FINALIZE_VEC_FIELD_NUMBER: _ClassVar[int]
        BLOB_OBJECT_RANGE_MAP_FIELD_NUMBER: _ClassVar[int]
        SEGMENT_START_OFFSET_VEC_FIELD_NUMBER: _ClassVar[int]
        JOURNAL_INFO_FIELD_NUMBER: _ClassVar[int]
        FINALIZE_IN_PROGRESS_FIELD_NUMBER: _ClassVar[int]
        OBJECT_PART_SIZE_FIELD_NUMBER: _ClassVar[int]
        SKIPPED_FINALIZATION_FIELD_NUMBER: _ClassVar[int]
        CREATION_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
        FINALIZATION_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
        OBJECT_VERSION_ID_FIELD_NUMBER: _ClassVar[int]
        object_uid: _universal_id_pb2.UniversalIdProto
        name: bytes
        offset: int
        upload_context: _vault_pb2.VaultUploadContextProto
        download_context: _vault_pb2.VaultDownloadContextProto
        archival_object_metadata: ArchivalObjectMetadataProto
        last_part_num: int
        num_bytes_read: int
        num_bytes_written: int
        chunks_to_finalize_vec: _containers.RepeatedCompositeFieldContainer[IceboxChunkIdProto]
        blob_object_range_map: _containers.MessageMap[int, _cloud_pb2.ArchiveDataRange]
        segment_start_offset_vec: _containers.RepeatedScalarFieldContainer[int]
        journal_info: TaskCheckpointInfo.JournalInfo
        finalize_in_progress: bool
        object_part_size: int
        skipped_finalization: bool
        creation_time_usecs: int
        finalization_time_usecs: int
        object_version_id: str
        def __init__(self, object_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., name: _Optional[bytes] = ..., offset: _Optional[int] = ..., upload_context: _Optional[_Union[_vault_pb2.VaultUploadContextProto, _Mapping]] = ..., download_context: _Optional[_Union[_vault_pb2.VaultDownloadContextProto, _Mapping]] = ..., archival_object_metadata: _Optional[_Union[ArchivalObjectMetadataProto, _Mapping]] = ..., last_part_num: _Optional[int] = ..., num_bytes_read: _Optional[int] = ..., num_bytes_written: _Optional[int] = ..., chunks_to_finalize_vec: _Optional[_Iterable[_Union[IceboxChunkIdProto, _Mapping]]] = ..., blob_object_range_map: _Optional[_Mapping[int, _cloud_pb2.ArchiveDataRange]] = ..., segment_start_offset_vec: _Optional[_Iterable[int]] = ..., journal_info: _Optional[_Union[TaskCheckpointInfo.JournalInfo, _Mapping]] = ..., finalize_in_progress: bool = ..., object_part_size: _Optional[int] = ..., skipped_finalization: bool = ..., creation_time_usecs: _Optional[int] = ..., finalization_time_usecs: _Optional[int] = ..., object_version_id: _Optional[str] = ...) -> None: ...
    class RestoreObjectData(_message.Message):
        __slots__ = ("object_uid", "download_context", "ready_for_download")
        OBJECT_UID_FIELD_NUMBER: _ClassVar[int]
        DOWNLOAD_CONTEXT_FIELD_NUMBER: _ClassVar[int]
        READY_FOR_DOWNLOAD_FIELD_NUMBER: _ClassVar[int]
        object_uid: _universal_id_pb2.UniversalIdProto
        download_context: _vault_pb2.VaultDownloadContextProto
        ready_for_download: bool
        def __init__(self, object_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., download_context: _Optional[_Union[_vault_pb2.VaultDownloadContextProto, _Mapping]] = ..., ready_for_download: bool = ...) -> None: ...
    class EntityData(_message.Message):
        __slots__ = ("num_bytes_read", "num_bytes_written")
        NUM_BYTES_READ_FIELD_NUMBER: _ClassVar[int]
        NUM_BYTES_WRITTEN_FIELD_NUMBER: _ClassVar[int]
        num_bytes_read: int
        num_bytes_written: int
        def __init__(self, num_bytes_read: _Optional[int] = ..., num_bytes_written: _Optional[int] = ...) -> None: ...
    class SnapTreeData(_message.Message):
        __slots__ = ("view_fs_root_inode_id", "blob_snap_tree_uid", "cookie")
        VIEW_FS_ROOT_INODE_ID_FIELD_NUMBER: _ClassVar[int]
        BLOB_SNAP_TREE_UID_FIELD_NUMBER: _ClassVar[int]
        COOKIE_FIELD_NUMBER: _ClassVar[int]
        view_fs_root_inode_id: int
        blob_snap_tree_uid: _universal_id_pb2.UniversalIdProto
        cookie: SnapTreeIterCookieProto
        def __init__(self, view_fs_root_inode_id: _Optional[int] = ..., blob_snap_tree_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., cookie: _Optional[_Union[SnapTreeIterCookieProto, _Mapping]] = ...) -> None: ...
    class HardlinkData(_message.Message):
        __slots__ = ("local_inode_id", "expected_num_links")
        LOCAL_INODE_ID_FIELD_NUMBER: _ClassVar[int]
        EXPECTED_NUM_LINKS_FIELD_NUMBER: _ClassVar[int]
        local_inode_id: int
        expected_num_links: int
        def __init__(self, local_inode_id: _Optional[int] = ..., expected_num_links: _Optional[int] = ...) -> None: ...
    class HardlinkMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: TaskCheckpointInfo.HardlinkData
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[TaskCheckpointInfo.HardlinkData, _Mapping]] = ...) -> None: ...
    class ChunkDBFileInfo(_message.Message):
        __slots__ = ("file_path", "file_size", "file_rel_path")
        FILE_PATH_FIELD_NUMBER: _ClassVar[int]
        FILE_SIZE_FIELD_NUMBER: _ClassVar[int]
        FILE_REL_PATH_FIELD_NUMBER: _ClassVar[int]
        file_path: str
        file_size: int
        file_rel_path: str
        def __init__(self, file_path: _Optional[str] = ..., file_size: _Optional[int] = ..., file_rel_path: _Optional[str] = ...) -> None: ...
    class RestoreStats(_message.Message):
        __slots__ = ("num_bytes_downloaded", "num_bytes_consumed", "num_bytes_written", "num_logical_bytes_restored", "num_files_found")
        NUM_BYTES_DOWNLOADED_FIELD_NUMBER: _ClassVar[int]
        NUM_BYTES_CONSUMED_FIELD_NUMBER: _ClassVar[int]
        NUM_BYTES_WRITTEN_FIELD_NUMBER: _ClassVar[int]
        NUM_LOGICAL_BYTES_RESTORED_FIELD_NUMBER: _ClassVar[int]
        NUM_FILES_FOUND_FIELD_NUMBER: _ClassVar[int]
        num_bytes_downloaded: int
        num_bytes_consumed: int
        num_bytes_written: int
        num_logical_bytes_restored: int
        num_files_found: int
        def __init__(self, num_bytes_downloaded: _Optional[int] = ..., num_bytes_consumed: _Optional[int] = ..., num_bytes_written: _Optional[int] = ..., num_logical_bytes_restored: _Optional[int] = ..., num_files_found: _Optional[int] = ...) -> None: ...
    class ListObjectsData(_message.Message):
        __slots__ = ("initiated", "context")
        INITIATED_FIELD_NUMBER: _ClassVar[int]
        CONTEXT_FIELD_NUMBER: _ClassVar[int]
        initiated: bool
        context: _vault_pb2.VaultListObjectsContextProto
        def __init__(self, initiated: bool = ..., context: _Optional[_Union[_vault_pb2.VaultListObjectsContextProto, _Mapping]] = ...) -> None: ...
    class ReadMetadataObjectInfo(_message.Message):
        __slots__ = ("returned_object_metadata", "returned_archive_metadata", "decryption_key_unavailable", "failed")
        RETURNED_OBJECT_METADATA_FIELD_NUMBER: _ClassVar[int]
        RETURNED_ARCHIVE_METADATA_FIELD_NUMBER: _ClassVar[int]
        DECRYPTION_KEY_UNAVAILABLE_FIELD_NUMBER: _ClassVar[int]
        FAILED_FIELD_NUMBER: _ClassVar[int]
        returned_object_metadata: bool
        returned_archive_metadata: bool
        decryption_key_unavailable: bool
        failed: bool
        def __init__(self, returned_object_metadata: bool = ..., returned_archive_metadata: bool = ..., decryption_key_unavailable: bool = ..., failed: bool = ...) -> None: ...
    class ReadMetadataObjectMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: TaskCheckpointInfo.ReadMetadataObjectInfo
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[TaskCheckpointInfo.ReadMetadataObjectInfo, _Mapping]] = ...) -> None: ...
    class EntityFileIndexCommonInfo(_message.Message):
        __slots__ = ("entity_id", "index_file_path", "index_file_offset", "finished", "error", "is_handle_released", "skipped_indexing", "last_progress_timestamp_usecs")
        ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
        INDEX_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
        INDEX_FILE_OFFSET_FIELD_NUMBER: _ClassVar[int]
        FINISHED_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        IS_HANDLE_RELEASED_FIELD_NUMBER: _ClassVar[int]
        SKIPPED_INDEXING_FIELD_NUMBER: _ClassVar[int]
        LAST_PROGRESS_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
        entity_id: int
        index_file_path: str
        index_file_offset: int
        finished: bool
        error: _error_pb2.ErrorProto
        is_handle_released: bool
        skipped_indexing: bool
        last_progress_timestamp_usecs: int
        def __init__(self, entity_id: _Optional[int] = ..., index_file_path: _Optional[str] = ..., index_file_offset: _Optional[int] = ..., finished: bool = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., is_handle_released: bool = ..., skipped_indexing: bool = ..., last_progress_timestamp_usecs: _Optional[int] = ...) -> None: ...
    class BuildEntityFileIndexInfo(_message.Message):
        __slots__ = ("index_state", "yoda_handle", "object_snapshot_doc_file_path", "entity_index_info", "object_doc", "object_doc_file_proto", "cookie")
        INDEX_STATE_FIELD_NUMBER: _ClassVar[int]
        YODA_HANDLE_FIELD_NUMBER: _ClassVar[int]
        OBJECT_SNAPSHOT_DOC_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
        ENTITY_INDEX_INFO_FIELD_NUMBER: _ClassVar[int]
        OBJECT_DOC_FIELD_NUMBER: _ClassVar[int]
        OBJECT_DOC_FILE_PROTO_FIELD_NUMBER: _ClassVar[int]
        COOKIE_FIELD_NUMBER: _ClassVar[int]
        index_state: TaskCheckpointInfo.EntityFileIndexCommonInfo
        yoda_handle: _yoda_rpc_args_pb2.PutCrackedFileIndexHandle
        object_snapshot_doc_file_path: str
        entity_index_info: EntityMetadataProto.IndexInfo
        object_doc: _documents_pb2.ObjectSnapshotDocument
        object_doc_file_proto: EntityMetadataProto.ObjectSnapshotDocFileProto
        cookie: bytes
        def __init__(self, index_state: _Optional[_Union[TaskCheckpointInfo.EntityFileIndexCommonInfo, _Mapping]] = ..., yoda_handle: _Optional[_Union[_yoda_rpc_args_pb2.PutCrackedFileIndexHandle, _Mapping]] = ..., object_snapshot_doc_file_path: _Optional[str] = ..., entity_index_info: _Optional[_Union[EntityMetadataProto.IndexInfo, _Mapping]] = ..., object_doc: _Optional[_Union[_documents_pb2.ObjectSnapshotDocument, _Mapping]] = ..., object_doc_file_proto: _Optional[_Union[EntityMetadataProto.ObjectSnapshotDocFileProto, _Mapping]] = ..., cookie: _Optional[bytes] = ...) -> None: ...
    class BuildFileIndexData(_message.Message):
        __slots__ = ("archive_uid", "build_entity_file_index_info_map")
        class BuildEntityFileIndexInfoMapEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: int
            value: TaskCheckpointInfo.BuildEntityFileIndexInfo
            def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[TaskCheckpointInfo.BuildEntityFileIndexInfo, _Mapping]] = ...) -> None: ...
        ARCHIVE_UID_FIELD_NUMBER: _ClassVar[int]
        BUILD_ENTITY_FILE_INDEX_INFO_MAP_FIELD_NUMBER: _ClassVar[int]
        archive_uid: _universal_id_pb2.UniversalIdProto
        build_entity_file_index_info_map: _containers.MessageMap[int, TaskCheckpointInfo.BuildEntityFileIndexInfo]
        def __init__(self, archive_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., build_entity_file_index_info_map: _Optional[_Mapping[int, TaskCheckpointInfo.BuildEntityFileIndexInfo]] = ...) -> None: ...
    class CreateEntityIndexFilesInfo(_message.Message):
        __slots__ = ("index_state", "yoda_handle", "object_doc", "cookie", "entity_index_info", "object_doc_file_proto")
        INDEX_STATE_FIELD_NUMBER: _ClassVar[int]
        YODA_HANDLE_FIELD_NUMBER: _ClassVar[int]
        OBJECT_DOC_FIELD_NUMBER: _ClassVar[int]
        COOKIE_FIELD_NUMBER: _ClassVar[int]
        ENTITY_INDEX_INFO_FIELD_NUMBER: _ClassVar[int]
        OBJECT_DOC_FILE_PROTO_FIELD_NUMBER: _ClassVar[int]
        index_state: TaskCheckpointInfo.EntityFileIndexCommonInfo
        yoda_handle: _yoda_rpc_args_pb2.CrackedFileIndexHandle
        object_doc: _documents_pb2.ObjectSnapshotDocument
        cookie: bytes
        entity_index_info: EntityMetadataProto.IndexInfo
        object_doc_file_proto: EntityMetadataProto.ObjectSnapshotDocFileProto
        def __init__(self, index_state: _Optional[_Union[TaskCheckpointInfo.EntityFileIndexCommonInfo, _Mapping]] = ..., yoda_handle: _Optional[_Union[_yoda_rpc_args_pb2.CrackedFileIndexHandle, _Mapping]] = ..., object_doc: _Optional[_Union[_documents_pb2.ObjectSnapshotDocument, _Mapping]] = ..., cookie: _Optional[bytes] = ..., entity_index_info: _Optional[_Union[EntityMetadataProto.IndexInfo, _Mapping]] = ..., object_doc_file_proto: _Optional[_Union[EntityMetadataProto.ObjectSnapshotDocFileProto, _Mapping]] = ...) -> None: ...
    class CreateIndexFilesData(_message.Message):
        __slots__ = ("create_entity_index_file_info_map", "archive_index_info", "indexing_start_time_usecs")
        class CreateEntityIndexFileInfoMapEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: int
            value: TaskCheckpointInfo.CreateEntityIndexFilesInfo
            def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[TaskCheckpointInfo.CreateEntityIndexFilesInfo, _Mapping]] = ...) -> None: ...
        CREATE_ENTITY_INDEX_FILE_INFO_MAP_FIELD_NUMBER: _ClassVar[int]
        ARCHIVE_INDEX_INFO_FIELD_NUMBER: _ClassVar[int]
        INDEXING_START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
        create_entity_index_file_info_map: _containers.MessageMap[int, TaskCheckpointInfo.CreateEntityIndexFilesInfo]
        archive_index_info: ArchiveMetadataProto.IndexInfo
        indexing_start_time_usecs: int
        def __init__(self, create_entity_index_file_info_map: _Optional[_Mapping[int, TaskCheckpointInfo.CreateEntityIndexFilesInfo]] = ..., archive_index_info: _Optional[_Union[ArchiveMetadataProto.IndexInfo, _Mapping]] = ..., indexing_start_time_usecs: _Optional[int] = ...) -> None: ...
    class CreateStubViewData(_message.Message):
        __slots__ = ("stub_view_name", "stub_view_id", "existing_uptier_expiry_timestamp_usecs")
        STUB_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
        STUB_VIEW_ID_FIELD_NUMBER: _ClassVar[int]
        EXISTING_UPTIER_EXPIRY_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
        stub_view_name: str
        stub_view_id: int
        existing_uptier_expiry_timestamp_usecs: int
        def __init__(self, stub_view_name: _Optional[str] = ..., stub_view_id: _Optional[int] = ..., existing_uptier_expiry_timestamp_usecs: _Optional[int] = ...) -> None: ...
    class UploadFileInfo(_message.Message):
        __slots__ = ("file_info", "upload_context", "latest_uploaded_part_num", "in_progress_part_num_vec", "error", "status")
        FILE_INFO_FIELD_NUMBER: _ClassVar[int]
        UPLOAD_CONTEXT_FIELD_NUMBER: _ClassVar[int]
        LATEST_UPLOADED_PART_NUM_FIELD_NUMBER: _ClassVar[int]
        IN_PROGRESS_PART_NUM_VEC_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        file_info: FileInfoProto
        upload_context: _vault_pb2.VaultUploadContextProto
        latest_uploaded_part_num: int
        in_progress_part_num_vec: _containers.RepeatedScalarFieldContainer[int]
        error: _error_pb2.ErrorProto
        status: FileUploadStatus
        def __init__(self, file_info: _Optional[_Union[FileInfoProto, _Mapping]] = ..., upload_context: _Optional[_Union[_vault_pb2.VaultUploadContextProto, _Mapping]] = ..., latest_uploaded_part_num: _Optional[int] = ..., in_progress_part_num_vec: _Optional[_Iterable[int]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., status: _Optional[_Union[FileUploadStatus, str]] = ...) -> None: ...
    class GetFilesToUploadData(_message.Message):
        __slots__ = ("curr_checkpoint_file_rel_path", "prev_checkpoint_file_rel_path", "skipped_checkpoint_file_rel_path")
        CURR_CHECKPOINT_FILE_REL_PATH_FIELD_NUMBER: _ClassVar[int]
        PREV_CHECKPOINT_FILE_REL_PATH_FIELD_NUMBER: _ClassVar[int]
        SKIPPED_CHECKPOINT_FILE_REL_PATH_FIELD_NUMBER: _ClassVar[int]
        curr_checkpoint_file_rel_path: str
        prev_checkpoint_file_rel_path: str
        skipped_checkpoint_file_rel_path: str
        def __init__(self, curr_checkpoint_file_rel_path: _Optional[str] = ..., prev_checkpoint_file_rel_path: _Optional[str] = ..., skipped_checkpoint_file_rel_path: _Optional[str] = ...) -> None: ...
    class UploadFilesData(_message.Message):
        __slots__ = ("upload_file_info_vec",)
        UPLOAD_FILE_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
        upload_file_info_vec: _containers.RepeatedCompositeFieldContainer[TaskCheckpointInfo.UploadFileInfo]
        def __init__(self, upload_file_info_vec: _Optional[_Iterable[_Union[TaskCheckpointInfo.UploadFileInfo, _Mapping]]] = ...) -> None: ...
    class PrefetchFilesData(_message.Message):
        __slots__ = ("prefetch_file_path", "file_offset")
        PREFETCH_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
        FILE_OFFSET_FIELD_NUMBER: _ClassVar[int]
        prefetch_file_path: str
        file_offset: int
        def __init__(self, prefetch_file_path: _Optional[str] = ..., file_offset: _Optional[int] = ...) -> None: ...
    class HydrationInfo(_message.Message):
        __slots__ = ("start_time_usecs", "end_time_usecs")
        START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
        END_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
        start_time_usecs: int
        end_time_usecs: int
        def __init__(self, start_time_usecs: _Optional[int] = ..., end_time_usecs: _Optional[int] = ...) -> None: ...
    class CopyFilePartInfo(_message.Message):
        __slots__ = ("part_num", "offset", "size", "uploaded", "upload_context")
        PART_NUM_FIELD_NUMBER: _ClassVar[int]
        OFFSET_FIELD_NUMBER: _ClassVar[int]
        SIZE_FIELD_NUMBER: _ClassVar[int]
        UPLOADED_FIELD_NUMBER: _ClassVar[int]
        UPLOAD_CONTEXT_FIELD_NUMBER: _ClassVar[int]
        part_num: int
        offset: int
        size: int
        uploaded: bool
        upload_context: _vault_pb2.VaultUploadContextProto
        def __init__(self, part_num: _Optional[int] = ..., offset: _Optional[int] = ..., size: _Optional[int] = ..., uploaded: bool = ..., upload_context: _Optional[_Union[_vault_pb2.VaultUploadContextProto, _Mapping]] = ...) -> None: ...
    class CopyFileInfo(_message.Message):
        __slots__ = ("file_index", "object_name", "part_size", "upload_context", "part_vec", "finalized_object_name", "logical_size", "num_bytes_written", "num_bytes_read", "objects_info_file_name", "action_file_next_offset", "morphed_info", "is_batch_action_record_created")
        FILE_INDEX_FIELD_NUMBER: _ClassVar[int]
        OBJECT_NAME_FIELD_NUMBER: _ClassVar[int]
        PART_SIZE_FIELD_NUMBER: _ClassVar[int]
        UPLOAD_CONTEXT_FIELD_NUMBER: _ClassVar[int]
        PART_VEC_FIELD_NUMBER: _ClassVar[int]
        FINALIZED_OBJECT_NAME_FIELD_NUMBER: _ClassVar[int]
        LOGICAL_SIZE_FIELD_NUMBER: _ClassVar[int]
        NUM_BYTES_WRITTEN_FIELD_NUMBER: _ClassVar[int]
        NUM_BYTES_READ_FIELD_NUMBER: _ClassVar[int]
        OBJECTS_INFO_FILE_NAME_FIELD_NUMBER: _ClassVar[int]
        ACTION_FILE_NEXT_OFFSET_FIELD_NUMBER: _ClassVar[int]
        MORPHED_INFO_FIELD_NUMBER: _ClassVar[int]
        IS_BATCH_ACTION_RECORD_CREATED_FIELD_NUMBER: _ClassVar[int]
        file_index: int
        object_name: str
        part_size: int
        upload_context: _vault_pb2.VaultUploadContextProto
        part_vec: _containers.RepeatedCompositeFieldContainer[TaskCheckpointInfo.CopyFilePartInfo]
        finalized_object_name: str
        logical_size: int
        num_bytes_written: int
        num_bytes_read: int
        objects_info_file_name: str
        action_file_next_offset: int
        morphed_info: _cloud_pb2.ArchivedLocation.MorphedInfo
        is_batch_action_record_created: bool
        def __init__(self, file_index: _Optional[int] = ..., object_name: _Optional[str] = ..., part_size: _Optional[int] = ..., upload_context: _Optional[_Union[_vault_pb2.VaultUploadContextProto, _Mapping]] = ..., part_vec: _Optional[_Iterable[_Union[TaskCheckpointInfo.CopyFilePartInfo, _Mapping]]] = ..., finalized_object_name: _Optional[str] = ..., logical_size: _Optional[int] = ..., num_bytes_written: _Optional[int] = ..., num_bytes_read: _Optional[int] = ..., objects_info_file_name: _Optional[str] = ..., action_file_next_offset: _Optional[int] = ..., morphed_info: _Optional[_Union[_cloud_pb2.ArchivedLocation.MorphedInfo, _Mapping]] = ..., is_batch_action_record_created: bool = ...) -> None: ...
    class PrefetchSnapTreeNodesData(_message.Message):
        __slots__ = ("blob_snap_tree_id_vec", "blob_data_ranges_map")
        class BlobDataRangesMapEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: int
            value: BlobDataRanges
            def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[BlobDataRanges, _Mapping]] = ...) -> None: ...
        BLOB_SNAP_TREE_ID_VEC_FIELD_NUMBER: _ClassVar[int]
        BLOB_DATA_RANGES_MAP_FIELD_NUMBER: _ClassVar[int]
        blob_snap_tree_id_vec: _containers.RepeatedScalarFieldContainer[int]
        blob_data_ranges_map: _containers.MessageMap[int, BlobDataRanges]
        def __init__(self, blob_snap_tree_id_vec: _Optional[_Iterable[int]] = ..., blob_data_ranges_map: _Optional[_Mapping[int, BlobDataRanges]] = ...) -> None: ...
    class DownloadSnapTreeObjectInfo(_message.Message):
        __slots__ = ("object_index", "next_offset", "uptiering_done")
        OBJECT_INDEX_FIELD_NUMBER: _ClassVar[int]
        NEXT_OFFSET_FIELD_NUMBER: _ClassVar[int]
        UPTIERING_DONE_FIELD_NUMBER: _ClassVar[int]
        object_index: int
        next_offset: int
        uptiering_done: bool
        def __init__(self, object_index: _Optional[int] = ..., next_offset: _Optional[int] = ..., uptiering_done: bool = ...) -> None: ...
    class CleanupDirectArchiveObjectsInfo(_message.Message):
        __slots__ = ("current_file_index", "curr_file_offset", "num_objects_deleted", "num_bytes_deleted")
        CURRENT_FILE_INDEX_FIELD_NUMBER: _ClassVar[int]
        CURR_FILE_OFFSET_FIELD_NUMBER: _ClassVar[int]
        NUM_OBJECTS_DELETED_FIELD_NUMBER: _ClassVar[int]
        NUM_BYTES_DELETED_FIELD_NUMBER: _ClassVar[int]
        current_file_index: int
        curr_file_offset: int
        num_objects_deleted: int
        num_bytes_deleted: int
        def __init__(self, current_file_index: _Optional[int] = ..., curr_file_offset: _Optional[int] = ..., num_objects_deleted: _Optional[int] = ..., num_bytes_deleted: _Optional[int] = ...) -> None: ...
    class ArchiveObjectRestoreInfoMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: ArchiveObjectRestoreInfo
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[ArchiveObjectRestoreInfo, _Mapping]] = ...) -> None: ...
    class UptierDataInfo(_message.Message):
        __slots__ = ("object_info_file_id_gen", "object_info_file_vec", "uptier_status_vec", "dir_walker_cookie", "is_directory_walking_done", "num_objects_to_uptier", "total_objects_size_bytes", "logical_bytes_uptiered")
        OBJECT_INFO_FILE_ID_GEN_FIELD_NUMBER: _ClassVar[int]
        OBJECT_INFO_FILE_VEC_FIELD_NUMBER: _ClassVar[int]
        UPTIER_STATUS_VEC_FIELD_NUMBER: _ClassVar[int]
        DIR_WALKER_COOKIE_FIELD_NUMBER: _ClassVar[int]
        IS_DIRECTORY_WALKING_DONE_FIELD_NUMBER: _ClassVar[int]
        NUM_OBJECTS_TO_UPTIER_FIELD_NUMBER: _ClassVar[int]
        TOTAL_OBJECTS_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
        LOGICAL_BYTES_UPTIERED_FIELD_NUMBER: _ClassVar[int]
        object_info_file_id_gen: int
        object_info_file_vec: _containers.RepeatedScalarFieldContainer[str]
        uptier_status_vec: _containers.RepeatedScalarFieldContainer[bool]
        dir_walker_cookie: _directory_walker_pb2.EntityMetadata
        is_directory_walking_done: bool
        num_objects_to_uptier: int
        total_objects_size_bytes: int
        logical_bytes_uptiered: int
        def __init__(self, object_info_file_id_gen: _Optional[int] = ..., object_info_file_vec: _Optional[_Iterable[str]] = ..., uptier_status_vec: _Optional[_Iterable[bool]] = ..., dir_walker_cookie: _Optional[_Union[_directory_walker_pb2.EntityMetadata, _Mapping]] = ..., is_directory_walking_done: bool = ..., num_objects_to_uptier: _Optional[int] = ..., total_objects_size_bytes: _Optional[int] = ..., logical_bytes_uptiered: _Optional[int] = ...) -> None: ...
    class DowntierDataInfo(_message.Message):
        __slots__ = ("cur_dir_index", "view_id", "root_inode_id", "dir_entity_id", "file_info_vec", "is_downtiering_finished", "num_objects_downtiered", "total_objects_size_bytes")
        class FileInfo(_message.Message):
            __slots__ = ("file_name", "entity_id", "is_downtiered")
            FILE_NAME_FIELD_NUMBER: _ClassVar[int]
            ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
            IS_DOWNTIERED_FIELD_NUMBER: _ClassVar[int]
            file_name: str
            entity_id: int
            is_downtiered: bool
            def __init__(self, file_name: _Optional[str] = ..., entity_id: _Optional[int] = ..., is_downtiered: bool = ...) -> None: ...
        CUR_DIR_INDEX_FIELD_NUMBER: _ClassVar[int]
        VIEW_ID_FIELD_NUMBER: _ClassVar[int]
        ROOT_INODE_ID_FIELD_NUMBER: _ClassVar[int]
        DIR_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
        FILE_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
        IS_DOWNTIERING_FINISHED_FIELD_NUMBER: _ClassVar[int]
        NUM_OBJECTS_DOWNTIERED_FIELD_NUMBER: _ClassVar[int]
        TOTAL_OBJECTS_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
        cur_dir_index: int
        view_id: int
        root_inode_id: int
        dir_entity_id: int
        file_info_vec: _containers.RepeatedCompositeFieldContainer[TaskCheckpointInfo.DowntierDataInfo.FileInfo]
        is_downtiering_finished: bool
        num_objects_downtiered: int
        total_objects_size_bytes: int
        def __init__(self, cur_dir_index: _Optional[int] = ..., view_id: _Optional[int] = ..., root_inode_id: _Optional[int] = ..., dir_entity_id: _Optional[int] = ..., file_info_vec: _Optional[_Iterable[_Union[TaskCheckpointInfo.DowntierDataInfo.FileInfo, _Mapping]]] = ..., is_downtiering_finished: bool = ..., num_objects_downtiered: _Optional[int] = ..., total_objects_size_bytes: _Optional[int] = ...) -> None: ...
    class FixUpdateIntentsInfo(_message.Message):
        __slots__ = ("index_to_tree_info_map", "is_validation_pass")
        class SnapTreeInfo(_message.Message):
            __slots__ = ("cookie", "traversal_done", "has_update_intents")
            COOKIE_FIELD_NUMBER: _ClassVar[int]
            TRAVERSAL_DONE_FIELD_NUMBER: _ClassVar[int]
            HAS_UPDATE_INTENTS_FIELD_NUMBER: _ClassVar[int]
            cookie: _snap_tree_pb2.SnapTreeTraversalCookieProto
            traversal_done: bool
            has_update_intents: bool
            def __init__(self, cookie: _Optional[_Union[_snap_tree_pb2.SnapTreeTraversalCookieProto, _Mapping]] = ..., traversal_done: bool = ..., has_update_intents: bool = ...) -> None: ...
        class IndexToTreeInfoMapEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: int
            value: TaskCheckpointInfo.FixUpdateIntentsInfo.SnapTreeInfo
            def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[TaskCheckpointInfo.FixUpdateIntentsInfo.SnapTreeInfo, _Mapping]] = ...) -> None: ...
        INDEX_TO_TREE_INFO_MAP_FIELD_NUMBER: _ClassVar[int]
        IS_VALIDATION_PASS_FIELD_NUMBER: _ClassVar[int]
        index_to_tree_info_map: _containers.MessageMap[int, TaskCheckpointInfo.FixUpdateIntentsInfo.SnapTreeInfo]
        is_validation_pass: bool
        def __init__(self, index_to_tree_info_map: _Optional[_Mapping[int, TaskCheckpointInfo.FixUpdateIntentsInfo.SnapTreeInfo]] = ..., is_validation_pass: bool = ...) -> None: ...
    class UptierCloudDomainDataInfo(_message.Message):
        __slots__ = ("index_to_vst_info_map", "tree_id_to_bst_info_map", "uptiering_done", "dir_walker_cookie", "is_directory_walking_done")
        class ViewSnapTreeInfo(_message.Message):
            __slots__ = ("cookie", "traversal_done", "uptiered", "num_objects_to_uptier", "num_objects_uptiered")
            COOKIE_FIELD_NUMBER: _ClassVar[int]
            TRAVERSAL_DONE_FIELD_NUMBER: _ClassVar[int]
            UPTIERED_FIELD_NUMBER: _ClassVar[int]
            NUM_OBJECTS_TO_UPTIER_FIELD_NUMBER: _ClassVar[int]
            NUM_OBJECTS_UPTIERED_FIELD_NUMBER: _ClassVar[int]
            cookie: _snap_tree_pb2.SnapTreeTraversalCookieProto
            traversal_done: bool
            uptiered: bool
            num_objects_to_uptier: int
            num_objects_uptiered: int
            def __init__(self, cookie: _Optional[_Union[_snap_tree_pb2.SnapTreeTraversalCookieProto, _Mapping]] = ..., traversal_done: bool = ..., uptiered: bool = ..., num_objects_to_uptier: _Optional[int] = ..., num_objects_uptiered: _Optional[int] = ...) -> None: ...
        class IndexToVstInfoMapEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: int
            value: TaskCheckpointInfo.UptierCloudDomainDataInfo.ViewSnapTreeInfo
            def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[TaskCheckpointInfo.UptierCloudDomainDataInfo.ViewSnapTreeInfo, _Mapping]] = ...) -> None: ...
        class BlobSnapTreeInfo(_message.Message):
            __slots__ = ("view_snap_tree_index", "cookie")
            VIEW_SNAP_TREE_INDEX_FIELD_NUMBER: _ClassVar[int]
            COOKIE_FIELD_NUMBER: _ClassVar[int]
            view_snap_tree_index: int
            cookie: _snap_tree_pb2.SnapTreeTraversalCookieProto
            def __init__(self, view_snap_tree_index: _Optional[int] = ..., cookie: _Optional[_Union[_snap_tree_pb2.SnapTreeTraversalCookieProto, _Mapping]] = ...) -> None: ...
        class TreeIdToBstInfoMapEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: int
            value: TaskCheckpointInfo.UptierCloudDomainDataInfo.BlobSnapTreeInfo
            def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[TaskCheckpointInfo.UptierCloudDomainDataInfo.BlobSnapTreeInfo, _Mapping]] = ...) -> None: ...
        INDEX_TO_VST_INFO_MAP_FIELD_NUMBER: _ClassVar[int]
        TREE_ID_TO_BST_INFO_MAP_FIELD_NUMBER: _ClassVar[int]
        UPTIERING_DONE_FIELD_NUMBER: _ClassVar[int]
        DIR_WALKER_COOKIE_FIELD_NUMBER: _ClassVar[int]
        IS_DIRECTORY_WALKING_DONE_FIELD_NUMBER: _ClassVar[int]
        index_to_vst_info_map: _containers.MessageMap[int, TaskCheckpointInfo.UptierCloudDomainDataInfo.ViewSnapTreeInfo]
        tree_id_to_bst_info_map: _containers.MessageMap[int, TaskCheckpointInfo.UptierCloudDomainDataInfo.BlobSnapTreeInfo]
        uptiering_done: bool
        dir_walker_cookie: _directory_walker_pb2.EntityMetadata
        is_directory_walking_done: bool
        def __init__(self, index_to_vst_info_map: _Optional[_Mapping[int, TaskCheckpointInfo.UptierCloudDomainDataInfo.ViewSnapTreeInfo]] = ..., tree_id_to_bst_info_map: _Optional[_Mapping[int, TaskCheckpointInfo.UptierCloudDomainDataInfo.BlobSnapTreeInfo]] = ..., uptiering_done: bool = ..., dir_walker_cookie: _Optional[_Union[_directory_walker_pb2.EntityMetadata, _Mapping]] = ..., is_directory_walking_done: bool = ...) -> None: ...
    class ListCloudDomainsData(_message.Message):
        __slots__ = ("initiated", "context")
        INITIATED_FIELD_NUMBER: _ClassVar[int]
        CONTEXT_FIELD_NUMBER: _ClassVar[int]
        initiated: bool
        context: _vault_pb2.VaultListObjectsContextProto
        def __init__(self, initiated: bool = ..., context: _Optional[_Union[_vault_pb2.VaultListObjectsContextProto, _Mapping]] = ...) -> None: ...
    class ListArchiveMetadataObjectsData(_message.Message):
        __slots__ = ("initiated", "context")
        INITIATED_FIELD_NUMBER: _ClassVar[int]
        CONTEXT_FIELD_NUMBER: _ClassVar[int]
        initiated: bool
        context: _vault_pb2.VaultListObjectsContextProto
        def __init__(self, initiated: bool = ..., context: _Optional[_Union[_vault_pb2.VaultListObjectsContextProto, _Mapping]] = ...) -> None: ...
    class ReadArchiveMetadataObjectInfo(_message.Message):
        __slots__ = ("returned_archive_metadata", "failed")
        RETURNED_ARCHIVE_METADATA_FIELD_NUMBER: _ClassVar[int]
        FAILED_FIELD_NUMBER: _ClassVar[int]
        returned_archive_metadata: bool
        failed: bool
        def __init__(self, returned_archive_metadata: bool = ..., failed: bool = ...) -> None: ...
    class ReadArchiveMetadataObjectMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: TaskCheckpointInfo.ReadArchiveMetadataObjectInfo
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[TaskCheckpointInfo.ReadArchiveMetadataObjectInfo, _Mapping]] = ...) -> None: ...
    class ArchiveMetadataObjectData(_message.Message):
        __slots__ = ("offset",)
        OFFSET_FIELD_NUMBER: _ClassVar[int]
        offset: int
        def __init__(self, offset: _Optional[int] = ...) -> None: ...
    PROGRESS_TYPE_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    RESTORE_JOB_UID_FIELD_NUMBER: _ClassVar[int]
    FILE_DATA_FIELD_NUMBER: _ClassVar[int]
    OBJECT_DATA_FIELD_NUMBER: _ClassVar[int]
    RESTORE_OBJECT_DATA_VEC_FIELD_NUMBER: _ClassVar[int]
    ENTITY_DATA_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
    LATENCY_USECS_FIELD_NUMBER: _ClassVar[int]
    SNAP_TREE_DATA_FIELD_NUMBER: _ClassVar[int]
    FS_SNAP_TREE_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    HARDLINK_MAP_FIELD_NUMBER: _ClassVar[int]
    CHUNK_DB_FILE_INFO_FIELD_NUMBER: _ClassVar[int]
    REFERRED_OBJECT_UID_VEC_FIELD_NUMBER: _ClassVar[int]
    TASK_FINISHED_FIELD_NUMBER: _ClassVar[int]
    REFERRED_ARCHIVE_UID_VEC_FIELD_NUMBER: _ClassVar[int]
    RESTORE_STATS_FIELD_NUMBER: _ClassVar[int]
    ARCHIVE_STATS_FIELD_NUMBER: _ClassVar[int]
    RANGE_DOWNLOAD_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    LIST_OBJECTS_DATA_FIELD_NUMBER: _ClassVar[int]
    READ_METADATA_OBJECT_MAP_FIELD_NUMBER: _ClassVar[int]
    BUILD_FILE_INDEX_DATA_FIELD_NUMBER: _ClassVar[int]
    CREATE_INDEX_FILES_DATA_FIELD_NUMBER: _ClassVar[int]
    CREATE_STUB_VIEW_DATA_FIELD_NUMBER: _ClassVar[int]
    GET_FILES_TO_UPLOAD_DATA_FIELD_NUMBER: _ClassVar[int]
    UPLOAD_FILES_DATA_FIELD_NUMBER: _ClassVar[int]
    PREFETCH_FILES_DATA_FIELD_NUMBER: _ClassVar[int]
    QUOTA_SNAP_TREE_INFO_FIELD_NUMBER: _ClassVar[int]
    HYDRATION_INFO_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_ALL_UPDATE_INTENTS_FIELD_NUMBER: _ClassVar[int]
    COPY_FILE_INFO_FIELD_NUMBER: _ClassVar[int]
    BLOB_DATA_LOCATION_VEC_FIELD_NUMBER: _ClassVar[int]
    DATA_OBJECT_VEC_FIELD_NUMBER: _ClassVar[int]
    PREFETCH_SNAP_TREE_NODES_DATA_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_SNAP_TREE_OBJECT_INFO_FIELD_NUMBER: _ClassVar[int]
    ARCHIVE_VIEW_SNAP_TREE_TASK_STATS_FIELD_NUMBER: _ClassVar[int]
    OBJECTS_VALIDATION_INFO_FIELD_NUMBER: _ClassVar[int]
    CLEANUP_DA_OBJECTS_INFO_FIELD_NUMBER: _ClassVar[int]
    ARCHIVE_OBJECT_RESTORE_INFO_MAP_FIELD_NUMBER: _ClassVar[int]
    NUM_PADDED_BYTES_FIELD_NUMBER: _ClassVar[int]
    UPTIER_DATA_INFO_FIELD_NUMBER: _ClassVar[int]
    DOWNTIER_DATA_INFO_FIELD_NUMBER: _ClassVar[int]
    VIEW_SNAP_TREE_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    FIX_UPDATE_INTENTS_INFO_FIELD_NUMBER: _ClassVar[int]
    ARCHIVE_METADATA_CLOUD_LOCATION_FIELD_NUMBER: _ClassVar[int]
    UPTIER_CLOUD_DOMAIN_DATA_INFO_FIELD_NUMBER: _ClassVar[int]
    LIST_CLOUD_DOMAINS_DATA_FIELD_NUMBER: _ClassVar[int]
    LIST_ARCHIVE_METADATA_OBJECTS_DATA_FIELD_NUMBER: _ClassVar[int]
    READ_ARCHIVE_METADATA_OBJECT_MAP_FIELD_NUMBER: _ClassVar[int]
    ARCHIVE_METADATA_OBJECT_DATA_FIELD_NUMBER: _ClassVar[int]
    ARCHIVE_TASK_WORM_STATS_FIELD_NUMBER: _ClassVar[int]
    progress_type: TaskCheckpointInfo.ProgressType
    entity_id: int
    restore_job_uid: _universal_id_pb2.UniversalIdProto
    file_data: TaskCheckpointInfo.FileData
    object_data: TaskCheckpointInfo.ObjectData
    restore_object_data_vec: _containers.RepeatedCompositeFieldContainer[TaskCheckpointInfo.RestoreObjectData]
    entity_data: TaskCheckpointInfo.EntityData
    timestamp_usecs: int
    latency_usecs: int
    snap_tree_data: TaskCheckpointInfo.SnapTreeData
    fs_snap_tree_info_vec: _containers.RepeatedCompositeFieldContainer[ArchiveSnapshotMetadataProto.SnapTreeInfo]
    hardlink_map: _containers.MessageMap[int, TaskCheckpointInfo.HardlinkData]
    chunk_db_file_info: TaskCheckpointInfo.ChunkDBFileInfo
    referred_object_uid_vec: _containers.RepeatedCompositeFieldContainer[_universal_id_pb2.UniversalIdProto]
    task_finished: bool
    referred_archive_uid_vec: _containers.RepeatedCompositeFieldContainer[_universal_id_pb2.UniversalIdProto]
    restore_stats: TaskCheckpointInfo.RestoreStats
    archive_stats: ArchiveBlobTaskStats
    range_download_info_vec: _containers.RepeatedCompositeFieldContainer[RangeDownloadInfoProto]
    list_objects_data: TaskCheckpointInfo.ListObjectsData
    read_metadata_object_map: _containers.MessageMap[str, TaskCheckpointInfo.ReadMetadataObjectInfo]
    build_file_index_data: TaskCheckpointInfo.BuildFileIndexData
    create_index_files_data: TaskCheckpointInfo.CreateIndexFilesData
    create_stub_view_data: TaskCheckpointInfo.CreateStubViewData
    get_files_to_upload_data: TaskCheckpointInfo.GetFilesToUploadData
    upload_files_data: TaskCheckpointInfo.UploadFilesData
    prefetch_files_data: TaskCheckpointInfo.PrefetchFilesData
    quota_snap_tree_info: EntityMetadataProto.QuotaSnapTreeInfo
    hydration_info: TaskCheckpointInfo.HydrationInfo
    resolved_all_update_intents: bool
    copy_file_info: TaskCheckpointInfo.CopyFileInfo
    blob_data_location_vec: _containers.RepeatedCompositeFieldContainer[_cloud_pb2.ArchiveDataRange]
    data_object_vec: _containers.RepeatedCompositeFieldContainer[_cloud_pb2.ArchivedObject]
    prefetch_snap_tree_nodes_data: TaskCheckpointInfo.PrefetchSnapTreeNodesData
    download_snap_tree_object_info: TaskCheckpointInfo.DownloadSnapTreeObjectInfo
    archive_view_snap_tree_task_stats: ArchiveViewSnapTreeTaskStats
    objects_validation_info: ObjectsValidationInfo
    cleanup_da_objects_info: TaskCheckpointInfo.CleanupDirectArchiveObjectsInfo
    archive_object_restore_info_map: _containers.MessageMap[str, ArchiveObjectRestoreInfo]
    num_padded_bytes: int
    uptier_data_info: TaskCheckpointInfo.UptierDataInfo
    downtier_data_info: TaskCheckpointInfo.DowntierDataInfo
    view_snap_tree_info_vec: _containers.RepeatedCompositeFieldContainer[CloudDomainSnapTreesInfoProto.ViewSnapTreeInfo]
    fix_update_intents_info: TaskCheckpointInfo.FixUpdateIntentsInfo
    archive_metadata_cloud_location: _cloud_pb2.CloudNodePrefixPtrProto
    uptier_cloud_domain_data_info: TaskCheckpointInfo.UptierCloudDomainDataInfo
    list_cloud_domains_data: TaskCheckpointInfo.ListCloudDomainsData
    list_archive_metadata_objects_data: TaskCheckpointInfo.ListArchiveMetadataObjectsData
    read_archive_metadata_object_map: _containers.MessageMap[str, TaskCheckpointInfo.ReadArchiveMetadataObjectInfo]
    archive_metadata_object_data: TaskCheckpointInfo.ArchiveMetadataObjectData
    archive_task_worm_stats: ArchiveWORMStats
    def __init__(self, progress_type: _Optional[_Union[TaskCheckpointInfo.ProgressType, str]] = ..., entity_id: _Optional[int] = ..., restore_job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., file_data: _Optional[_Union[TaskCheckpointInfo.FileData, _Mapping]] = ..., object_data: _Optional[_Union[TaskCheckpointInfo.ObjectData, _Mapping]] = ..., restore_object_data_vec: _Optional[_Iterable[_Union[TaskCheckpointInfo.RestoreObjectData, _Mapping]]] = ..., entity_data: _Optional[_Union[TaskCheckpointInfo.EntityData, _Mapping]] = ..., timestamp_usecs: _Optional[int] = ..., latency_usecs: _Optional[int] = ..., snap_tree_data: _Optional[_Union[TaskCheckpointInfo.SnapTreeData, _Mapping]] = ..., fs_snap_tree_info_vec: _Optional[_Iterable[_Union[ArchiveSnapshotMetadataProto.SnapTreeInfo, _Mapping]]] = ..., hardlink_map: _Optional[_Mapping[int, TaskCheckpointInfo.HardlinkData]] = ..., chunk_db_file_info: _Optional[_Union[TaskCheckpointInfo.ChunkDBFileInfo, _Mapping]] = ..., referred_object_uid_vec: _Optional[_Iterable[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]]] = ..., task_finished: bool = ..., referred_archive_uid_vec: _Optional[_Iterable[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]]] = ..., restore_stats: _Optional[_Union[TaskCheckpointInfo.RestoreStats, _Mapping]] = ..., archive_stats: _Optional[_Union[ArchiveBlobTaskStats, _Mapping]] = ..., range_download_info_vec: _Optional[_Iterable[_Union[RangeDownloadInfoProto, _Mapping]]] = ..., list_objects_data: _Optional[_Union[TaskCheckpointInfo.ListObjectsData, _Mapping]] = ..., read_metadata_object_map: _Optional[_Mapping[str, TaskCheckpointInfo.ReadMetadataObjectInfo]] = ..., build_file_index_data: _Optional[_Union[TaskCheckpointInfo.BuildFileIndexData, _Mapping]] = ..., create_index_files_data: _Optional[_Union[TaskCheckpointInfo.CreateIndexFilesData, _Mapping]] = ..., create_stub_view_data: _Optional[_Union[TaskCheckpointInfo.CreateStubViewData, _Mapping]] = ..., get_files_to_upload_data: _Optional[_Union[TaskCheckpointInfo.GetFilesToUploadData, _Mapping]] = ..., upload_files_data: _Optional[_Union[TaskCheckpointInfo.UploadFilesData, _Mapping]] = ..., prefetch_files_data: _Optional[_Union[TaskCheckpointInfo.PrefetchFilesData, _Mapping]] = ..., quota_snap_tree_info: _Optional[_Union[EntityMetadataProto.QuotaSnapTreeInfo, _Mapping]] = ..., hydration_info: _Optional[_Union[TaskCheckpointInfo.HydrationInfo, _Mapping]] = ..., resolved_all_update_intents: bool = ..., copy_file_info: _Optional[_Union[TaskCheckpointInfo.CopyFileInfo, _Mapping]] = ..., blob_data_location_vec: _Optional[_Iterable[_Union[_cloud_pb2.ArchiveDataRange, _Mapping]]] = ..., data_object_vec: _Optional[_Iterable[_Union[_cloud_pb2.ArchivedObject, _Mapping]]] = ..., prefetch_snap_tree_nodes_data: _Optional[_Union[TaskCheckpointInfo.PrefetchSnapTreeNodesData, _Mapping]] = ..., download_snap_tree_object_info: _Optional[_Union[TaskCheckpointInfo.DownloadSnapTreeObjectInfo, _Mapping]] = ..., archive_view_snap_tree_task_stats: _Optional[_Union[ArchiveViewSnapTreeTaskStats, _Mapping]] = ..., objects_validation_info: _Optional[_Union[ObjectsValidationInfo, _Mapping]] = ..., cleanup_da_objects_info: _Optional[_Union[TaskCheckpointInfo.CleanupDirectArchiveObjectsInfo, _Mapping]] = ..., archive_object_restore_info_map: _Optional[_Mapping[str, ArchiveObjectRestoreInfo]] = ..., num_padded_bytes: _Optional[int] = ..., uptier_data_info: _Optional[_Union[TaskCheckpointInfo.UptierDataInfo, _Mapping]] = ..., downtier_data_info: _Optional[_Union[TaskCheckpointInfo.DowntierDataInfo, _Mapping]] = ..., view_snap_tree_info_vec: _Optional[_Iterable[_Union[CloudDomainSnapTreesInfoProto.ViewSnapTreeInfo, _Mapping]]] = ..., fix_update_intents_info: _Optional[_Union[TaskCheckpointInfo.FixUpdateIntentsInfo, _Mapping]] = ..., archive_metadata_cloud_location: _Optional[_Union[_cloud_pb2.CloudNodePrefixPtrProto, _Mapping]] = ..., uptier_cloud_domain_data_info: _Optional[_Union[TaskCheckpointInfo.UptierCloudDomainDataInfo, _Mapping]] = ..., list_cloud_domains_data: _Optional[_Union[TaskCheckpointInfo.ListCloudDomainsData, _Mapping]] = ..., list_archive_metadata_objects_data: _Optional[_Union[TaskCheckpointInfo.ListArchiveMetadataObjectsData, _Mapping]] = ..., read_archive_metadata_object_map: _Optional[_Mapping[str, TaskCheckpointInfo.ReadArchiveMetadataObjectInfo]] = ..., archive_metadata_object_data: _Optional[_Union[TaskCheckpointInfo.ArchiveMetadataObjectData, _Mapping]] = ..., archive_task_worm_stats: _Optional[_Union[ArchiveWORMStats, _Mapping]] = ...) -> None: ...

class IceboxChunkIdProto(_message.Message):
    __slots__ = ("vault_id", "sha1", "chunk_len", "cluster_instance_id", "dedup_domain")
    VAULT_ID_FIELD_NUMBER: _ClassVar[int]
    SHA1_FIELD_NUMBER: _ClassVar[int]
    CHUNK_LEN_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    DEDUP_DOMAIN_FIELD_NUMBER: _ClassVar[int]
    vault_id: int
    sha1: bytes
    chunk_len: int
    cluster_instance_id: _cluster_instance_identifier_pb2.ClusterInstanceIdentifier
    dedup_domain: int
    def __init__(self, vault_id: _Optional[int] = ..., sha1: _Optional[bytes] = ..., chunk_len: _Optional[int] = ..., cluster_instance_id: _Optional[_Union[_cluster_instance_identifier_pb2.ClusterInstanceIdentifier, _Mapping]] = ..., dedup_domain: _Optional[int] = ...) -> None: ...

class IceboxExtentProto(_message.Message):
    __slots__ = ("chunk_id", "chunk_offset", "blob_offset", "extent_len", "contains_data", "chunk_data_location")
    CHUNK_ID_FIELD_NUMBER: _ClassVar[int]
    CHUNK_OFFSET_FIELD_NUMBER: _ClassVar[int]
    BLOB_OFFSET_FIELD_NUMBER: _ClassVar[int]
    EXTENT_LEN_FIELD_NUMBER: _ClassVar[int]
    CONTAINS_DATA_FIELD_NUMBER: _ClassVar[int]
    CHUNK_DATA_LOCATION_FIELD_NUMBER: _ClassVar[int]
    chunk_id: IceboxChunkIdProto
    chunk_offset: int
    blob_offset: int
    extent_len: int
    contains_data: bool
    chunk_data_location: _cloud_pb2.ArchiveChunkPtrProto
    def __init__(self, chunk_id: _Optional[_Union[IceboxChunkIdProto, _Mapping]] = ..., chunk_offset: _Optional[int] = ..., blob_offset: _Optional[int] = ..., extent_len: _Optional[int] = ..., contains_data: bool = ..., chunk_data_location: _Optional[_Union[_cloud_pb2.ArchiveChunkPtrProto, _Mapping]] = ...) -> None: ...

class IceboxChunkLocationProto(_message.Message):
    __slots__ = ("location_vec", "last_access_timestamp_usecs", "update_intent_vec", "opclock_vec")
    class Location(_message.Message):
        __slots__ = ("owner_archive_uid", "data_pointer")
        OWNER_ARCHIVE_UID_FIELD_NUMBER: _ClassVar[int]
        DATA_POINTER_FIELD_NUMBER: _ClassVar[int]
        owner_archive_uid: _universal_id_pb2.UniversalIdProto
        data_pointer: _cloud_pb2.ArchiveChunkPtrProto
        def __init__(self, owner_archive_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., data_pointer: _Optional[_Union[_cloud_pb2.ArchiveChunkPtrProto, _Mapping]] = ...) -> None: ...
    class UpdateIntent(_message.Message):
        __slots__ = ("location", "task_id", "object_part_num")
        LOCATION_FIELD_NUMBER: _ClassVar[int]
        TASK_ID_FIELD_NUMBER: _ClassVar[int]
        OBJECT_PART_NUM_FIELD_NUMBER: _ClassVar[int]
        location: IceboxChunkLocationProto.Location
        task_id: int
        object_part_num: int
        def __init__(self, location: _Optional[_Union[IceboxChunkLocationProto.Location, _Mapping]] = ..., task_id: _Optional[int] = ..., object_part_num: _Optional[int] = ...) -> None: ...
    LOCATION_VEC_FIELD_NUMBER: _ClassVar[int]
    LAST_ACCESS_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
    UPDATE_INTENT_VEC_FIELD_NUMBER: _ClassVar[int]
    OPCLOCK_VEC_FIELD_NUMBER: _ClassVar[int]
    location_vec: _containers.RepeatedCompositeFieldContainer[IceboxChunkLocationProto.Location]
    last_access_timestamp_usecs: int
    update_intent_vec: _containers.RepeatedCompositeFieldContainer[IceboxChunkLocationProto.UpdateIntent]
    opclock_vec: _containers.RepeatedCompositeFieldContainer[_op_clock_pb2.OpClock]
    def __init__(self, location_vec: _Optional[_Iterable[_Union[IceboxChunkLocationProto.Location, _Mapping]]] = ..., last_access_timestamp_usecs: _Optional[int] = ..., update_intent_vec: _Optional[_Iterable[_Union[IceboxChunkLocationProto.UpdateIntent, _Mapping]]] = ..., opclock_vec: _Optional[_Iterable[_Union[_op_clock_pb2.OpClock, _Mapping]]] = ...) -> None: ...

class IceboxChunkDBFileRecordProto(_message.Message):
    __slots__ = ("entry_vec",)
    class ChunkDBFileEntry(_message.Message):
        __slots__ = ("sha1", "chunk_len", "data_pointer")
        SHA1_FIELD_NUMBER: _ClassVar[int]
        CHUNK_LEN_FIELD_NUMBER: _ClassVar[int]
        DATA_POINTER_FIELD_NUMBER: _ClassVar[int]
        sha1: bytes
        chunk_len: int
        data_pointer: _cloud_pb2.ArchiveChunkPtrProto
        def __init__(self, sha1: _Optional[bytes] = ..., chunk_len: _Optional[int] = ..., data_pointer: _Optional[_Union[_cloud_pb2.ArchiveChunkPtrProto, _Mapping]] = ...) -> None: ...
    ENTRY_VEC_FIELD_NUMBER: _ClassVar[int]
    entry_vec: _containers.RepeatedCompositeFieldContainer[IceboxChunkDBFileRecordProto.ChunkDBFileEntry]
    def __init__(self, entry_vec: _Optional[_Iterable[_Union[IceboxChunkDBFileRecordProto.ChunkDBFileEntry, _Mapping]]] = ...) -> None: ...

class IceboxSnapTreeNodeProto(_message.Message):
    __slots__ = ("tree_uid", "node_uid", "key_child_ptr_vec", "leaf_level_distance", "payload_size", "data_ptr", "blob_snap_tree_location_vec", "blob_data_location_vec", "original_snap_tree_node")
    class KeyChildPointer(_message.Message):
        __slots__ = ("key_int", "key_str", "child_ptr_tree_uid", "child_ptr_node_uid", "child_ptr")
        KEY_INT_FIELD_NUMBER: _ClassVar[int]
        KEY_STR_FIELD_NUMBER: _ClassVar[int]
        CHILD_PTR_TREE_UID_FIELD_NUMBER: _ClassVar[int]
        CHILD_PTR_NODE_UID_FIELD_NUMBER: _ClassVar[int]
        CHILD_PTR_FIELD_NUMBER: _ClassVar[int]
        key_int: int
        key_str: bytes
        child_ptr_tree_uid: _universal_id_pb2.UniversalIdProto
        child_ptr_node_uid: _universal_id_pb2.UniversalIdProto
        child_ptr: _cloud_pb2.ArchiveSnapTreeNodePtrProto
        def __init__(self, key_int: _Optional[int] = ..., key_str: _Optional[bytes] = ..., child_ptr_tree_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., child_ptr_node_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., child_ptr: _Optional[_Union[_cloud_pb2.ArchiveSnapTreeNodePtrProto, _Mapping]] = ...) -> None: ...
    TREE_UID_FIELD_NUMBER: _ClassVar[int]
    NODE_UID_FIELD_NUMBER: _ClassVar[int]
    KEY_CHILD_PTR_VEC_FIELD_NUMBER: _ClassVar[int]
    LEAF_LEVEL_DISTANCE_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_SIZE_FIELD_NUMBER: _ClassVar[int]
    DATA_PTR_FIELD_NUMBER: _ClassVar[int]
    BLOB_SNAP_TREE_LOCATION_VEC_FIELD_NUMBER: _ClassVar[int]
    BLOB_DATA_LOCATION_VEC_FIELD_NUMBER: _ClassVar[int]
    ORIGINAL_SNAP_TREE_NODE_FIELD_NUMBER: _ClassVar[int]
    tree_uid: _universal_id_pb2.UniversalIdProto
    node_uid: _universal_id_pb2.UniversalIdProto
    key_child_ptr_vec: _containers.RepeatedCompositeFieldContainer[IceboxSnapTreeNodeProto.KeyChildPointer]
    leaf_level_distance: int
    payload_size: int
    data_ptr: _cloud_pb2.ArchiveSnapTreeNodePtrProto
    blob_snap_tree_location_vec: _containers.RepeatedCompositeFieldContainer[_cloud_pb2.ArchiveDataRange]
    blob_data_location_vec: _containers.RepeatedCompositeFieldContainer[_cloud_pb2.ArchiveDataRange]
    original_snap_tree_node: _snap_tree_pb2.SnapTreeNodeProto
    def __init__(self, tree_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., node_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., key_child_ptr_vec: _Optional[_Iterable[_Union[IceboxSnapTreeNodeProto.KeyChildPointer, _Mapping]]] = ..., leaf_level_distance: _Optional[int] = ..., payload_size: _Optional[int] = ..., data_ptr: _Optional[_Union[_cloud_pb2.ArchiveSnapTreeNodePtrProto, _Mapping]] = ..., blob_snap_tree_location_vec: _Optional[_Iterable[_Union[_cloud_pb2.ArchiveDataRange, _Mapping]]] = ..., blob_data_location_vec: _Optional[_Iterable[_Union[_cloud_pb2.ArchiveDataRange, _Mapping]]] = ..., original_snap_tree_node: _Optional[_Union[_snap_tree_pb2.SnapTreeNodeProto, _Mapping]] = ...) -> None: ...

class ArchiveBrickMetadataProto(_message.Message):
    __slots__ = ("brick_metadata", "archive_chunk_ptr_vec")
    BRICK_METADATA_FIELD_NUMBER: _ClassVar[int]
    ARCHIVE_CHUNK_PTR_VEC_FIELD_NUMBER: _ClassVar[int]
    brick_metadata: _blob_store_pb2.BrickMetadataProto
    archive_chunk_ptr_vec: _containers.RepeatedCompositeFieldContainer[_cloud_pb2.ArchiveChunkPtrProto]
    def __init__(self, brick_metadata: _Optional[_Union[_blob_store_pb2.BrickMetadataProto, _Mapping]] = ..., archive_chunk_ptr_vec: _Optional[_Iterable[_Union[_cloud_pb2.ArchiveChunkPtrProto, _Mapping]]] = ...) -> None: ...

class IceboxSnapTreeNodeId(_message.Message):
    __slots__ = ("node_id", "cluster_instance_id", "blob_snap_tree_id", "brick_num", "node_ptr")
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    BLOB_SNAP_TREE_ID_FIELD_NUMBER: _ClassVar[int]
    BRICK_NUM_FIELD_NUMBER: _ClassVar[int]
    NODE_PTR_FIELD_NUMBER: _ClassVar[int]
    node_id: int
    cluster_instance_id: _cluster_instance_identifier_pb2.ClusterInstanceIdentifier
    blob_snap_tree_id: int
    brick_num: int
    node_ptr: _cloud_pb2.ArchiveSnapTreeNodePtrProto
    def __init__(self, node_id: _Optional[int] = ..., cluster_instance_id: _Optional[_Union[_cluster_instance_identifier_pb2.ClusterInstanceIdentifier, _Mapping]] = ..., blob_snap_tree_id: _Optional[int] = ..., brick_num: _Optional[int] = ..., node_ptr: _Optional[_Union[_cloud_pb2.ArchiveSnapTreeNodePtrProto, _Mapping]] = ...) -> None: ...

class IceboxSnapTreeNodeLocation(_message.Message):
    __slots__ = ("base_archive_uid", "data_ptr", "node_ptr", "blob_snap_tree_location_vec", "blob_data_location_vec", "archive_uid", "location_owner_id", "location_owner_eh")
    BASE_ARCHIVE_UID_FIELD_NUMBER: _ClassVar[int]
    DATA_PTR_FIELD_NUMBER: _ClassVar[int]
    NODE_PTR_FIELD_NUMBER: _ClassVar[int]
    BLOB_SNAP_TREE_LOCATION_VEC_FIELD_NUMBER: _ClassVar[int]
    BLOB_DATA_LOCATION_VEC_FIELD_NUMBER: _ClassVar[int]
    ARCHIVE_UID_FIELD_NUMBER: _ClassVar[int]
    LOCATION_OWNER_ID_FIELD_NUMBER: _ClassVar[int]
    LOCATION_OWNER_EH_FIELD_NUMBER: _ClassVar[int]
    base_archive_uid: _universal_id_pb2.UniversalIdProto
    data_ptr: _cloud_pb2.ArchiveSnapTreeNodePtrProto
    node_ptr: _cloud_pb2.ArchiveSnapTreeNodePtrProto
    blob_snap_tree_location_vec: _containers.RepeatedCompositeFieldContainer[_cloud_pb2.ArchiveDataRange]
    blob_data_location_vec: _containers.RepeatedCompositeFieldContainer[_cloud_pb2.ArchiveDataRange]
    archive_uid: _universal_id_pb2.UniversalIdProto
    location_owner_id: int
    location_owner_eh: _entity_handle_pb2.EntityHandleProto
    def __init__(self, base_archive_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., data_ptr: _Optional[_Union[_cloud_pb2.ArchiveSnapTreeNodePtrProto, _Mapping]] = ..., node_ptr: _Optional[_Union[_cloud_pb2.ArchiveSnapTreeNodePtrProto, _Mapping]] = ..., blob_snap_tree_location_vec: _Optional[_Iterable[_Union[_cloud_pb2.ArchiveDataRange, _Mapping]]] = ..., blob_data_location_vec: _Optional[_Iterable[_Union[_cloud_pb2.ArchiveDataRange, _Mapping]]] = ..., archive_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., location_owner_id: _Optional[int] = ..., location_owner_eh: _Optional[_Union[_entity_handle_pb2.EntityHandleProto, _Mapping]] = ...) -> None: ...

class IceboxSnapTreeNodeMetadataProto(_message.Message):
    __slots__ = ("location_vec", "opclock_vec")
    LOCATION_VEC_FIELD_NUMBER: _ClassVar[int]
    OPCLOCK_VEC_FIELD_NUMBER: _ClassVar[int]
    location_vec: _containers.RepeatedCompositeFieldContainer[IceboxSnapTreeNodeLocation]
    opclock_vec: _containers.RepeatedCompositeFieldContainer[_op_clock_pb2.OpClock]
    def __init__(self, location_vec: _Optional[_Iterable[_Union[IceboxSnapTreeNodeLocation, _Mapping]]] = ..., opclock_vec: _Optional[_Iterable[_Union[_op_clock_pb2.OpClock, _Mapping]]] = ...) -> None: ...

class IceboxRestoredNodeMetadataProto(_message.Message):
    __slots__ = ("node_vec", "opclock_vec")
    class RestoredNode(_message.Message):
        __slots__ = ("restore_job_uid", "icebox_snap_tree_node", "view_snap_tree_value", "blob_snap_tree_value")
        RESTORE_JOB_UID_FIELD_NUMBER: _ClassVar[int]
        ICEBOX_SNAP_TREE_NODE_FIELD_NUMBER: _ClassVar[int]
        VIEW_SNAP_TREE_VALUE_FIELD_NUMBER: _ClassVar[int]
        BLOB_SNAP_TREE_VALUE_FIELD_NUMBER: _ClassVar[int]
        restore_job_uid: _universal_id_pb2.UniversalIdProto
        icebox_snap_tree_node: IceboxSnapTreeNodeProto
        view_snap_tree_value: _snap_fs_metadata_pb2.ViewSnapTreeValueProto
        blob_snap_tree_value: _blob_store_pb2.BrickMetadataProto
        def __init__(self, restore_job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., icebox_snap_tree_node: _Optional[_Union[IceboxSnapTreeNodeProto, _Mapping]] = ..., view_snap_tree_value: _Optional[_Union[_snap_fs_metadata_pb2.ViewSnapTreeValueProto, _Mapping]] = ..., blob_snap_tree_value: _Optional[_Union[_blob_store_pb2.BrickMetadataProto, _Mapping]] = ...) -> None: ...
    NODE_VEC_FIELD_NUMBER: _ClassVar[int]
    OPCLOCK_VEC_FIELD_NUMBER: _ClassVar[int]
    node_vec: _containers.RepeatedCompositeFieldContainer[IceboxRestoredNodeMetadataProto.RestoredNode]
    opclock_vec: _containers.RepeatedCompositeFieldContainer[_op_clock_pb2.OpClock]
    def __init__(self, node_vec: _Optional[_Iterable[_Union[IceboxRestoredNodeMetadataProto.RestoredNode, _Mapping]]] = ..., opclock_vec: _Optional[_Iterable[_Union[_op_clock_pb2.OpClock, _Mapping]]] = ...) -> None: ...

class CloudDomainSnapTreesInfoProto(_message.Message):
    __slots__ = ("cloud_domain_id", "view_snap_tree_info_vec")
    class ViewSnapTreeInfo(_message.Message):
        __slots__ = ("view_snap_tree_id", "view_id", "fs_name", "root_node_cloud_location", "root_inode_id", "root_leaf_level_distance", "max_bst_leaf_level_distance", "total_num_leaf_nodes_archived", "frontend_size_bytes")
        VIEW_SNAP_TREE_ID_FIELD_NUMBER: _ClassVar[int]
        VIEW_ID_FIELD_NUMBER: _ClassVar[int]
        FS_NAME_FIELD_NUMBER: _ClassVar[int]
        ROOT_NODE_CLOUD_LOCATION_FIELD_NUMBER: _ClassVar[int]
        ROOT_INODE_ID_FIELD_NUMBER: _ClassVar[int]
        ROOT_LEAF_LEVEL_DISTANCE_FIELD_NUMBER: _ClassVar[int]
        MAX_BST_LEAF_LEVEL_DISTANCE_FIELD_NUMBER: _ClassVar[int]
        TOTAL_NUM_LEAF_NODES_ARCHIVED_FIELD_NUMBER: _ClassVar[int]
        FRONTEND_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
        view_snap_tree_id: int
        view_id: int
        fs_name: str
        root_node_cloud_location: _cloud_pb2.CloudNodePtrProto
        root_inode_id: int
        root_leaf_level_distance: int
        max_bst_leaf_level_distance: int
        total_num_leaf_nodes_archived: int
        frontend_size_bytes: int
        def __init__(self, view_snap_tree_id: _Optional[int] = ..., view_id: _Optional[int] = ..., fs_name: _Optional[str] = ..., root_node_cloud_location: _Optional[_Union[_cloud_pb2.CloudNodePtrProto, _Mapping]] = ..., root_inode_id: _Optional[int] = ..., root_leaf_level_distance: _Optional[int] = ..., max_bst_leaf_level_distance: _Optional[int] = ..., total_num_leaf_nodes_archived: _Optional[int] = ..., frontend_size_bytes: _Optional[int] = ...) -> None: ...
    CLOUD_DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_SNAP_TREE_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    cloud_domain_id: int
    view_snap_tree_info_vec: _containers.RepeatedCompositeFieldContainer[CloudDomainSnapTreesInfoProto.ViewSnapTreeInfo]
    def __init__(self, cloud_domain_id: _Optional[int] = ..., view_snap_tree_info_vec: _Optional[_Iterable[_Union[CloudDomainSnapTreesInfoProto.ViewSnapTreeInfo, _Mapping]]] = ...) -> None: ...

class ArchiveSnapshotMetadataProto(_message.Message):
    __slots__ = ("fs_snap_tree_info_vec", "base_archive_uid", "parent_archive_uid_vec", "referred_object_uid_vec", "brick_size", "is_base", "prev_base_archive_uid", "referred_archive_uid_vec", "prev_archive_uid", "node_id_floor", "base_archive_metadata_object_name", "parent_archive_metadata_object_name_vec", "referred_archive_metadata_object_name_vec", "prev_archive_metadata_object_name")
    class SnapTreeInfo(_message.Message):
        __slots__ = ("fs_name", "tree_uid", "root_inode_id", "root_node_location", "snap_tree_location_vec", "view_id", "snap_tree_root_lld")
        FS_NAME_FIELD_NUMBER: _ClassVar[int]
        TREE_UID_FIELD_NUMBER: _ClassVar[int]
        ROOT_INODE_ID_FIELD_NUMBER: _ClassVar[int]
        ROOT_NODE_LOCATION_FIELD_NUMBER: _ClassVar[int]
        SNAP_TREE_LOCATION_VEC_FIELD_NUMBER: _ClassVar[int]
        VIEW_ID_FIELD_NUMBER: _ClassVar[int]
        SNAP_TREE_ROOT_LLD_FIELD_NUMBER: _ClassVar[int]
        fs_name: str
        tree_uid: _universal_id_pb2.UniversalIdProto
        root_inode_id: int
        root_node_location: _cloud_pb2.ArchiveSnapTreeNodePtrProto
        snap_tree_location_vec: _containers.RepeatedCompositeFieldContainer[_cloud_pb2.ArchiveDataRange]
        view_id: int
        snap_tree_root_lld: int
        def __init__(self, fs_name: _Optional[str] = ..., tree_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., root_inode_id: _Optional[int] = ..., root_node_location: _Optional[_Union[_cloud_pb2.ArchiveSnapTreeNodePtrProto, _Mapping]] = ..., snap_tree_location_vec: _Optional[_Iterable[_Union[_cloud_pb2.ArchiveDataRange, _Mapping]]] = ..., view_id: _Optional[int] = ..., snap_tree_root_lld: _Optional[int] = ...) -> None: ...
    FS_SNAP_TREE_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    BASE_ARCHIVE_UID_FIELD_NUMBER: _ClassVar[int]
    PARENT_ARCHIVE_UID_VEC_FIELD_NUMBER: _ClassVar[int]
    REFERRED_OBJECT_UID_VEC_FIELD_NUMBER: _ClassVar[int]
    BRICK_SIZE_FIELD_NUMBER: _ClassVar[int]
    IS_BASE_FIELD_NUMBER: _ClassVar[int]
    PREV_BASE_ARCHIVE_UID_FIELD_NUMBER: _ClassVar[int]
    REFERRED_ARCHIVE_UID_VEC_FIELD_NUMBER: _ClassVar[int]
    PREV_ARCHIVE_UID_FIELD_NUMBER: _ClassVar[int]
    NODE_ID_FLOOR_FIELD_NUMBER: _ClassVar[int]
    BASE_ARCHIVE_METADATA_OBJECT_NAME_FIELD_NUMBER: _ClassVar[int]
    PARENT_ARCHIVE_METADATA_OBJECT_NAME_VEC_FIELD_NUMBER: _ClassVar[int]
    REFERRED_ARCHIVE_METADATA_OBJECT_NAME_VEC_FIELD_NUMBER: _ClassVar[int]
    PREV_ARCHIVE_METADATA_OBJECT_NAME_FIELD_NUMBER: _ClassVar[int]
    fs_snap_tree_info_vec: _containers.RepeatedCompositeFieldContainer[ArchiveSnapshotMetadataProto.SnapTreeInfo]
    base_archive_uid: _universal_id_pb2.UniversalIdProto
    parent_archive_uid_vec: _containers.RepeatedCompositeFieldContainer[_universal_id_pb2.UniversalIdProto]
    referred_object_uid_vec: _containers.RepeatedCompositeFieldContainer[_universal_id_pb2.UniversalIdProto]
    brick_size: int
    is_base: bool
    prev_base_archive_uid: _universal_id_pb2.UniversalIdProto
    referred_archive_uid_vec: _containers.RepeatedCompositeFieldContainer[_universal_id_pb2.UniversalIdProto]
    prev_archive_uid: _universal_id_pb2.UniversalIdProto
    node_id_floor: int
    base_archive_metadata_object_name: str
    parent_archive_metadata_object_name_vec: _containers.RepeatedScalarFieldContainer[str]
    referred_archive_metadata_object_name_vec: _containers.RepeatedScalarFieldContainer[str]
    prev_archive_metadata_object_name: str
    def __init__(self, fs_snap_tree_info_vec: _Optional[_Iterable[_Union[ArchiveSnapshotMetadataProto.SnapTreeInfo, _Mapping]]] = ..., base_archive_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., parent_archive_uid_vec: _Optional[_Iterable[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]]] = ..., referred_object_uid_vec: _Optional[_Iterable[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]]] = ..., brick_size: _Optional[int] = ..., is_base: bool = ..., prev_base_archive_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., referred_archive_uid_vec: _Optional[_Iterable[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]]] = ..., prev_archive_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., node_id_floor: _Optional[int] = ..., base_archive_metadata_object_name: _Optional[str] = ..., parent_archive_metadata_object_name_vec: _Optional[_Iterable[str]] = ..., referred_archive_metadata_object_name_vec: _Optional[_Iterable[str]] = ..., prev_archive_metadata_object_name: _Optional[str] = ...) -> None: ...

class ArchiveMetadataSliceProto(_message.Message):
    __slots__ = ("total_serialized_metadata_size", "offset", "slice_size", "is_final_slice")
    TOTAL_SERIALIZED_METADATA_SIZE_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SLICE_SIZE_FIELD_NUMBER: _ClassVar[int]
    IS_FINAL_SLICE_FIELD_NUMBER: _ClassVar[int]
    total_serialized_metadata_size: int
    offset: int
    slice_size: int
    is_final_slice: bool
    def __init__(self, total_serialized_metadata_size: _Optional[int] = ..., offset: _Optional[int] = ..., slice_size: _Optional[int] = ..., is_final_slice: bool = ...) -> None: ...

class BlobInfo(_message.Message):
    __slots__ = ("inode_id", "blob_snap_tree_uid", "snap_tree_node_uid", "blob_logical_size", "offset", "size", "is_minion", "relative_file_path")
    INODE_ID_FIELD_NUMBER: _ClassVar[int]
    BLOB_SNAP_TREE_UID_FIELD_NUMBER: _ClassVar[int]
    SNAP_TREE_NODE_UID_FIELD_NUMBER: _ClassVar[int]
    BLOB_LOGICAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    IS_MINION_FIELD_NUMBER: _ClassVar[int]
    RELATIVE_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    inode_id: int
    blob_snap_tree_uid: _universal_id_pb2.UniversalIdProto
    snap_tree_node_uid: _universal_id_pb2.UniversalIdProto
    blob_logical_size: int
    offset: int
    size: int
    is_minion: bool
    relative_file_path: str
    def __init__(self, inode_id: _Optional[int] = ..., blob_snap_tree_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., snap_tree_node_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., blob_logical_size: _Optional[int] = ..., offset: _Optional[int] = ..., size: _Optional[int] = ..., is_minion: bool = ..., relative_file_path: _Optional[str] = ...) -> None: ...

class SnapTreeIterCookieProto(_message.Message):
    __slots__ = ("int_key", "str_key", "cookie_tree_uid", "cookie_node_uid", "last_processed_tree_uid", "last_processed_node_uid")
    INT_KEY_FIELD_NUMBER: _ClassVar[int]
    STR_KEY_FIELD_NUMBER: _ClassVar[int]
    COOKIE_TREE_UID_FIELD_NUMBER: _ClassVar[int]
    COOKIE_NODE_UID_FIELD_NUMBER: _ClassVar[int]
    LAST_PROCESSED_TREE_UID_FIELD_NUMBER: _ClassVar[int]
    LAST_PROCESSED_NODE_UID_FIELD_NUMBER: _ClassVar[int]
    int_key: int
    str_key: str
    cookie_tree_uid: _universal_id_pb2.UniversalIdProto
    cookie_node_uid: _universal_id_pb2.UniversalIdProto
    last_processed_tree_uid: _universal_id_pb2.UniversalIdProto
    last_processed_node_uid: _universal_id_pb2.UniversalIdProto
    def __init__(self, int_key: _Optional[int] = ..., str_key: _Optional[str] = ..., cookie_tree_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., cookie_node_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., last_processed_tree_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., last_processed_node_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ...) -> None: ...

class TimeRange(_message.Message):
    __slots__ = ("start_time_usecs", "end_time_usecs")
    START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    END_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    start_time_usecs: int
    end_time_usecs: int
    def __init__(self, start_time_usecs: _Optional[int] = ..., end_time_usecs: _Optional[int] = ...) -> None: ...

class VaultSearchParams(_message.Message):
    __slots__ = ("start_time_usecs", "end_time_usecs", "cluster_name", "app_job_name", "object_name", "cluster_id", "app_job_uid_vec")
    START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    END_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_NAME_FIELD_NUMBER: _ClassVar[int]
    APP_JOB_NAME_FIELD_NUMBER: _ClassVar[int]
    OBJECT_NAME_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    APP_JOB_UID_VEC_FIELD_NUMBER: _ClassVar[int]
    start_time_usecs: int
    end_time_usecs: int
    cluster_name: str
    app_job_name: str
    object_name: str
    cluster_id: int
    app_job_uid_vec: _containers.RepeatedCompositeFieldContainer[_universal_id_pb2.UniversalIdProto]
    def __init__(self, start_time_usecs: _Optional[int] = ..., end_time_usecs: _Optional[int] = ..., cluster_name: _Optional[str] = ..., app_job_name: _Optional[str] = ..., object_name: _Optional[str] = ..., cluster_id: _Optional[int] = ..., app_job_uid_vec: _Optional[_Iterable[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]]] = ...) -> None: ...

class JobCommonInfo(_message.Message):
    __slots__ = ("job_uid", "job_name", "vault_id", "start_time_usecs", "end_time_usecs", "job_status", "error")
    JOB_UID_FIELD_NUMBER: _ClassVar[int]
    JOB_NAME_FIELD_NUMBER: _ClassVar[int]
    VAULT_ID_FIELD_NUMBER: _ClassVar[int]
    START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    END_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    JOB_STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    job_uid: _universal_id_pb2.UniversalIdProto
    job_name: str
    vault_id: int
    start_time_usecs: int
    end_time_usecs: int
    job_status: IceboxJobStatus
    error: _error_pb2.ErrorProto
    def __init__(self, job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., job_name: _Optional[str] = ..., vault_id: _Optional[int] = ..., start_time_usecs: _Optional[int] = ..., end_time_usecs: _Optional[int] = ..., job_status: _Optional[_Union[IceboxJobStatus, str]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class SearchJobMetadataKey(_message.Message):
    __slots__ = ("search_job_uid", "app_job_uid")
    SEARCH_JOB_UID_FIELD_NUMBER: _ClassVar[int]
    APP_JOB_UID_FIELD_NUMBER: _ClassVar[int]
    search_job_uid: _universal_id_pb2.UniversalIdProto
    app_job_uid: _universal_id_pb2.UniversalIdProto
    def __init__(self, search_job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., app_job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ...) -> None: ...

class SearchJobMetadataProto(_message.Message):
    __slots__ = ("common_info", "search_params", "app_job_uid_vec", "num_bytes_downloaded", "app_job_info")
    class AppJobRunInfo(_message.Message):
        __slots__ = ("app_job_instance_id", "archive_uid", "snapshot_timestamp_usecs", "archive_version", "full_metadata_available", "expiry_timestamp_usecs", "index_size_bytes", "job_run_type")
        APP_JOB_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
        ARCHIVE_UID_FIELD_NUMBER: _ClassVar[int]
        SNAPSHOT_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
        ARCHIVE_VERSION_FIELD_NUMBER: _ClassVar[int]
        FULL_METADATA_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
        EXPIRY_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
        INDEX_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
        JOB_RUN_TYPE_FIELD_NUMBER: _ClassVar[int]
        app_job_instance_id: int
        archive_uid: _universal_id_pb2.UniversalIdProto
        snapshot_timestamp_usecs: int
        archive_version: int
        full_metadata_available: bool
        expiry_timestamp_usecs: int
        index_size_bytes: int
        job_run_type: _enums_pb2.ScheduledBackupType.Type
        def __init__(self, app_job_instance_id: _Optional[int] = ..., archive_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., snapshot_timestamp_usecs: _Optional[int] = ..., archive_version: _Optional[int] = ..., full_metadata_available: bool = ..., expiry_timestamp_usecs: _Optional[int] = ..., index_size_bytes: _Optional[int] = ..., job_run_type: _Optional[_Union[_enums_pb2.ScheduledBackupType.Type, str]] = ...) -> None: ...
    class AppJobInfo(_message.Message):
        __slots__ = ("app_job_uid", "app_job_name", "cluster_name", "app_job_instance_info_vec", "app_job_type")
        APP_JOB_UID_FIELD_NUMBER: _ClassVar[int]
        APP_JOB_NAME_FIELD_NUMBER: _ClassVar[int]
        CLUSTER_NAME_FIELD_NUMBER: _ClassVar[int]
        APP_JOB_INSTANCE_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
        APP_JOB_TYPE_FIELD_NUMBER: _ClassVar[int]
        app_job_uid: _universal_id_pb2.UniversalIdProto
        app_job_name: str
        cluster_name: str
        app_job_instance_info_vec: _containers.RepeatedCompositeFieldContainer[SearchJobMetadataProto.AppJobRunInfo]
        app_job_type: _enums_pb2.Environment.Type
        def __init__(self, app_job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., app_job_name: _Optional[str] = ..., cluster_name: _Optional[str] = ..., app_job_instance_info_vec: _Optional[_Iterable[_Union[SearchJobMetadataProto.AppJobRunInfo, _Mapping]]] = ..., app_job_type: _Optional[_Union[_enums_pb2.Environment.Type, str]] = ...) -> None: ...
    COMMON_INFO_FIELD_NUMBER: _ClassVar[int]
    SEARCH_PARAMS_FIELD_NUMBER: _ClassVar[int]
    APP_JOB_UID_VEC_FIELD_NUMBER: _ClassVar[int]
    NUM_BYTES_DOWNLOADED_FIELD_NUMBER: _ClassVar[int]
    APP_JOB_INFO_FIELD_NUMBER: _ClassVar[int]
    common_info: JobCommonInfo
    search_params: VaultSearchParams
    app_job_uid_vec: _containers.RepeatedCompositeFieldContainer[_universal_id_pb2.UniversalIdProto]
    num_bytes_downloaded: int
    app_job_info: SearchJobMetadataProto.AppJobInfo
    def __init__(self, common_info: _Optional[_Union[JobCommonInfo, _Mapping]] = ..., search_params: _Optional[_Union[VaultSearchParams, _Mapping]] = ..., app_job_uid_vec: _Optional[_Iterable[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]]] = ..., num_bytes_downloaded: _Optional[int] = ..., app_job_info: _Optional[_Union[SearchJobMetadataProto.AppJobInfo, _Mapping]] = ...) -> None: ...

class DomainMigrationJobMetadataProto(_message.Message):
    __slots__ = ("common_info", "is_cad", "app_job_uid_vec", "num_bytes_downloaded", "cloud_domain_id", "is_migration_ready")
    COMMON_INFO_FIELD_NUMBER: _ClassVar[int]
    IS_CAD_FIELD_NUMBER: _ClassVar[int]
    APP_JOB_UID_VEC_FIELD_NUMBER: _ClassVar[int]
    NUM_BYTES_DOWNLOADED_FIELD_NUMBER: _ClassVar[int]
    CLOUD_DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    IS_MIGRATION_READY_FIELD_NUMBER: _ClassVar[int]
    common_info: JobCommonInfo
    is_cad: bool
    app_job_uid_vec: _containers.RepeatedCompositeFieldContainer[_universal_id_pb2.UniversalIdProto]
    num_bytes_downloaded: int
    cloud_domain_id: int
    is_migration_ready: bool
    def __init__(self, common_info: _Optional[_Union[JobCommonInfo, _Mapping]] = ..., is_cad: bool = ..., app_job_uid_vec: _Optional[_Iterable[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]]] = ..., num_bytes_downloaded: _Optional[int] = ..., cloud_domain_id: _Optional[int] = ..., is_migration_ready: bool = ...) -> None: ...

class SearchResultArchiveMetadataProto(_message.Message):
    __slots__ = ("job_uid_vec", "archive_metadata_proto", "archive_object_metadata_vec", "job_run_metadata")
    JOB_UID_VEC_FIELD_NUMBER: _ClassVar[int]
    ARCHIVE_METADATA_PROTO_FIELD_NUMBER: _ClassVar[int]
    ARCHIVE_OBJECT_METADATA_VEC_FIELD_NUMBER: _ClassVar[int]
    JOB_RUN_METADATA_FIELD_NUMBER: _ClassVar[int]
    job_uid_vec: _containers.RepeatedCompositeFieldContainer[_universal_id_pb2.UniversalIdProto]
    archive_metadata_proto: ArchiveMetadataProto
    archive_object_metadata_vec: _containers.RepeatedCompositeFieldContainer[ArchiveObjectScribeMetadataProto]
    job_run_metadata: _master_pb2.BackupRunArchiveMDProto
    def __init__(self, job_uid_vec: _Optional[_Iterable[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]]] = ..., archive_metadata_proto: _Optional[_Union[ArchiveMetadataProto, _Mapping]] = ..., archive_object_metadata_vec: _Optional[_Iterable[_Union[ArchiveObjectScribeMetadataProto, _Mapping]]] = ..., job_run_metadata: _Optional[_Union[_master_pb2.BackupRunArchiveMDProto, _Mapping]] = ...) -> None: ...

class SearchResultCloudDomainProto(_message.Message):
    __slots__ = ("cloud_domain_info", "dek_uid", "vault_kms")
    class CloudDomainInfo(_message.Message):
        __slots__ = ("external_target_name", "storage_domain_name", "cluster_id", "name", "cloud_domain_id")
        EXTERNAL_TARGET_NAME_FIELD_NUMBER: _ClassVar[int]
        STORAGE_DOMAIN_NAME_FIELD_NUMBER: _ClassVar[int]
        CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        CLOUD_DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
        external_target_name: str
        storage_domain_name: str
        cluster_id: int
        name: str
        cloud_domain_id: int
        def __init__(self, external_target_name: _Optional[str] = ..., storage_domain_name: _Optional[str] = ..., cluster_id: _Optional[int] = ..., name: _Optional[str] = ..., cloud_domain_id: _Optional[int] = ...) -> None: ...
    CLOUD_DOMAIN_INFO_FIELD_NUMBER: _ClassVar[int]
    DEK_UID_FIELD_NUMBER: _ClassVar[int]
    VAULT_KMS_FIELD_NUMBER: _ClassVar[int]
    cloud_domain_info: SearchResultCloudDomainProto.CloudDomainInfo
    dek_uid: _universal_id_pb2.UniversalIdProto
    vault_kms: bool
    def __init__(self, cloud_domain_info: _Optional[_Union[SearchResultCloudDomainProto.CloudDomainInfo, _Mapping]] = ..., dek_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., vault_kms: bool = ...) -> None: ...

class StubViewMetadataKey(_message.Message):
    __slots__ = ("archive_uid", "entity_id", "viewbox_id")
    ARCHIVE_UID_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    VIEWBOX_ID_FIELD_NUMBER: _ClassVar[int]
    archive_uid: _universal_id_pb2.UniversalIdProto
    entity_id: int
    viewbox_id: int
    def __init__(self, archive_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., entity_id: _Optional[int] = ..., viewbox_id: _Optional[int] = ...) -> None: ...

class StubViewMetadataProto(_message.Message):
    __slots__ = ("stub_view_info",)
    STUB_VIEW_INFO_FIELD_NUMBER: _ClassVar[int]
    stub_view_info: ArchiveMetadataProto.StubViewInfo
    def __init__(self, stub_view_info: _Optional[_Union[ArchiveMetadataProto.StubViewInfo, _Mapping]] = ...) -> None: ...

class RestoreIndexStats(_message.Message):
    __slots__ = ("archive_count", "job_run_registration_success_count", "job_run_registration_failure_count", "index_files_not_present_count", "download_index_success_count", "download_index_failure_count", "build_index_success_count", "build_index_failure_count")
    ARCHIVE_COUNT_FIELD_NUMBER: _ClassVar[int]
    JOB_RUN_REGISTRATION_SUCCESS_COUNT_FIELD_NUMBER: _ClassVar[int]
    JOB_RUN_REGISTRATION_FAILURE_COUNT_FIELD_NUMBER: _ClassVar[int]
    INDEX_FILES_NOT_PRESENT_COUNT_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_INDEX_SUCCESS_COUNT_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_INDEX_FAILURE_COUNT_FIELD_NUMBER: _ClassVar[int]
    BUILD_INDEX_SUCCESS_COUNT_FIELD_NUMBER: _ClassVar[int]
    BUILD_INDEX_FAILURE_COUNT_FIELD_NUMBER: _ClassVar[int]
    archive_count: int
    job_run_registration_success_count: int
    job_run_registration_failure_count: int
    index_files_not_present_count: int
    download_index_success_count: int
    download_index_failure_count: int
    build_index_success_count: int
    build_index_failure_count: int
    def __init__(self, archive_count: _Optional[int] = ..., job_run_registration_success_count: _Optional[int] = ..., job_run_registration_failure_count: _Optional[int] = ..., index_files_not_present_count: _Optional[int] = ..., download_index_success_count: _Optional[int] = ..., download_index_failure_count: _Optional[int] = ..., build_index_success_count: _Optional[int] = ..., build_index_failure_count: _Optional[int] = ...) -> None: ...

class ObjectInfoProto(_message.Message):
    __slots__ = ("name", "description", "size", "object_id", "object_type", "cluster_id", "cluster_incarnation_id", "application_job_id", "application_job_instance_id", "archive_id", "creation_timestamp_usecs", "object_name_version", "expired")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_TYPE_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_JOB_ID_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_JOB_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    ARCHIVE_ID_FIELD_NUMBER: _ClassVar[int]
    CREATION_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
    OBJECT_NAME_VERSION_FIELD_NUMBER: _ClassVar[int]
    EXPIRED_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    size: int
    object_id: int
    object_type: ArchivalObjectMetadataProto.ObjectType
    cluster_id: int
    cluster_incarnation_id: int
    application_job_id: int
    application_job_instance_id: int
    archive_id: int
    creation_timestamp_usecs: int
    object_name_version: int
    expired: bool
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., size: _Optional[int] = ..., object_id: _Optional[int] = ..., object_type: _Optional[_Union[ArchivalObjectMetadataProto.ObjectType, str]] = ..., cluster_id: _Optional[int] = ..., cluster_incarnation_id: _Optional[int] = ..., application_job_id: _Optional[int] = ..., application_job_instance_id: _Optional[int] = ..., archive_id: _Optional[int] = ..., creation_timestamp_usecs: _Optional[int] = ..., object_name_version: _Optional[int] = ..., expired: bool = ...) -> None: ...

class FileInfoProto(_message.Message):
    __slots__ = ("inode_id", "rel_file_path", "size")
    INODE_ID_FIELD_NUMBER: _ClassVar[int]
    REL_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    inode_id: int
    rel_file_path: str
    size: int
    def __init__(self, inode_id: _Optional[int] = ..., rel_file_path: _Optional[str] = ..., size: _Optional[int] = ...) -> None: ...

class GetFilesToUploadCookieProto(_message.Message):
    __slots__ = ("last_diffed_entity", "get_files_to_upload_data")
    LAST_DIFFED_ENTITY_FIELD_NUMBER: _ClassVar[int]
    GET_FILES_TO_UPLOAD_DATA_FIELD_NUMBER: _ClassVar[int]
    last_diffed_entity: _directory_walker_pb2.EntityMetadata
    get_files_to_upload_data: TaskCheckpointInfo.GetFilesToUploadData
    def __init__(self, last_diffed_entity: _Optional[_Union[_directory_walker_pb2.EntityMetadata, _Mapping]] = ..., get_files_to_upload_data: _Optional[_Union[TaskCheckpointInfo.GetFilesToUploadData, _Mapping]] = ...) -> None: ...

class FileUploadJobMetadataProto(_message.Message):
    __slots__ = ("fs_checkpoint_info_vec", "stats")
    class FSCheckpointInfo(_message.Message):
        __slots__ = ("view_id", "fs_name", "checkpoint_file_rel_path", "skipped_checkpoint_file_rel_path")
        VIEW_ID_FIELD_NUMBER: _ClassVar[int]
        FS_NAME_FIELD_NUMBER: _ClassVar[int]
        CHECKPOINT_FILE_REL_PATH_FIELD_NUMBER: _ClassVar[int]
        SKIPPED_CHECKPOINT_FILE_REL_PATH_FIELD_NUMBER: _ClassVar[int]
        view_id: int
        fs_name: str
        checkpoint_file_rel_path: str
        skipped_checkpoint_file_rel_path: str
        def __init__(self, view_id: _Optional[int] = ..., fs_name: _Optional[str] = ..., checkpoint_file_rel_path: _Optional[str] = ..., skipped_checkpoint_file_rel_path: _Optional[str] = ...) -> None: ...
    FS_CHECKPOINT_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    STATS_FIELD_NUMBER: _ClassVar[int]
    fs_checkpoint_info_vec: _containers.RepeatedCompositeFieldContainer[FileUploadJobMetadataProto.FSCheckpointInfo]
    stats: FileUploadJobStats
    def __init__(self, fs_checkpoint_info_vec: _Optional[_Iterable[_Union[FileUploadJobMetadataProto.FSCheckpointInfo, _Mapping]]] = ..., stats: _Optional[_Union[FileUploadJobStats, _Mapping]] = ...) -> None: ...

class FileUploadJobStats(_message.Message):
    __slots__ = ("num_files", "upload_size_bytes", "failed_upload_count")
    NUM_FILES_FIELD_NUMBER: _ClassVar[int]
    UPLOAD_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    FAILED_UPLOAD_COUNT_FIELD_NUMBER: _ClassVar[int]
    num_files: int
    upload_size_bytes: int
    failed_upload_count: int
    def __init__(self, num_files: _Optional[int] = ..., upload_size_bytes: _Optional[int] = ..., failed_upload_count: _Optional[int] = ...) -> None: ...

class IceboxJobMetadataProto(_message.Message):
    __slots__ = ("job_type", "opclock_vec", "common_info", "file_upload_job_metadata")
    JOB_TYPE_FIELD_NUMBER: _ClassVar[int]
    OPCLOCK_VEC_FIELD_NUMBER: _ClassVar[int]
    COMMON_INFO_FIELD_NUMBER: _ClassVar[int]
    FILE_UPLOAD_JOB_METADATA_FIELD_NUMBER: _ClassVar[int]
    job_type: IceboxJobType
    opclock_vec: _containers.RepeatedCompositeFieldContainer[_op_clock_pb2.OpClock]
    common_info: JobCommonInfo
    file_upload_job_metadata: FileUploadJobMetadataProto
    def __init__(self, job_type: _Optional[_Union[IceboxJobType, str]] = ..., opclock_vec: _Optional[_Iterable[_Union[_op_clock_pb2.OpClock, _Mapping]]] = ..., common_info: _Optional[_Union[JobCommonInfo, _Mapping]] = ..., file_upload_job_metadata: _Optional[_Union[FileUploadJobMetadataProto, _Mapping]] = ...) -> None: ...

class RangeDownloadInfoProto(_message.Message):
    __slots__ = ("range", "initiate_time_usecs", "expiry_time_usecs", "download_context", "available_time_usecs", "non_existent", "initiate_completed", "object_size", "task_id_vec", "is_expedited_restore")
    RANGE_FIELD_NUMBER: _ClassVar[int]
    INITIATE_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    EXPIRY_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    AVAILABLE_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    NON_EXISTENT_FIELD_NUMBER: _ClassVar[int]
    INITIATE_COMPLETED_FIELD_NUMBER: _ClassVar[int]
    OBJECT_SIZE_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    IS_EXPEDITED_RESTORE_FIELD_NUMBER: _ClassVar[int]
    range: _cloud_pb2.ArchiveDataRange
    initiate_time_usecs: int
    expiry_time_usecs: int
    download_context: _vault_pb2.VaultDownloadContextProto
    available_time_usecs: int
    non_existent: bool
    initiate_completed: bool
    object_size: int
    task_id_vec: _containers.RepeatedCompositeFieldContainer[PrepareRangesTaskIdProto]
    is_expedited_restore: bool
    def __init__(self, range: _Optional[_Union[_cloud_pb2.ArchiveDataRange, _Mapping]] = ..., initiate_time_usecs: _Optional[int] = ..., expiry_time_usecs: _Optional[int] = ..., download_context: _Optional[_Union[_vault_pb2.VaultDownloadContextProto, _Mapping]] = ..., available_time_usecs: _Optional[int] = ..., non_existent: bool = ..., initiate_completed: bool = ..., object_size: _Optional[int] = ..., task_id_vec: _Optional[_Iterable[_Union[PrepareRangesTaskIdProto, _Mapping]]] = ..., is_expedited_restore: bool = ...) -> None: ...

class PrepareRangesTaskIdProto(_message.Message):
    __slots__ = ("job_uid", "batch_id")
    JOB_UID_FIELD_NUMBER: _ClassVar[int]
    BATCH_ID_FIELD_NUMBER: _ClassVar[int]
    job_uid: _universal_id_pb2.UniversalIdProto
    batch_id: str
    def __init__(self, job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., batch_id: _Optional[str] = ...) -> None: ...

class ObjectNameUIDProto(_message.Message):
    __slots__ = ("object_uid", "object_name")
    OBJECT_UID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_NAME_FIELD_NUMBER: _ClassVar[int]
    object_uid: _universal_id_pb2.UniversalIdProto
    object_name: str
    def __init__(self, object_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., object_name: _Optional[str] = ...) -> None: ...

class PreparedObjectKeyProto(_message.Message):
    __slots__ = ("object_uid", "object_id", "sequence_num")
    OBJECT_UID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    SEQUENCE_NUM_FIELD_NUMBER: _ClassVar[int]
    object_uid: _universal_id_pb2.UniversalIdProto
    object_id: ObjectIdProto
    sequence_num: int
    def __init__(self, object_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., object_id: _Optional[_Union[ObjectIdProto, _Mapping]] = ..., sequence_num: _Optional[int] = ...) -> None: ...

class ObjectIdProto(_message.Message):
    __slots__ = ("object_name", "vault_id")
    OBJECT_NAME_FIELD_NUMBER: _ClassVar[int]
    VAULT_ID_FIELD_NUMBER: _ClassVar[int]
    object_name: str
    vault_id: int
    def __init__(self, object_name: _Optional[str] = ..., vault_id: _Optional[int] = ...) -> None: ...

class PreparedObjectProto(_message.Message):
    __slots__ = ("object_name", "next_sequence_num", "object_range_info_vec", "opclock_vec")
    class ObjectRangeInfo(_message.Message):
        __slots__ = ("offset", "size", "sequence_num", "download_context", "initiate_timestamp_usecs", "expiry_timestamp_usecs", "available_timestamp_usecs", "task_id_vec", "is_expedited_restore")
        OFFSET_FIELD_NUMBER: _ClassVar[int]
        SIZE_FIELD_NUMBER: _ClassVar[int]
        SEQUENCE_NUM_FIELD_NUMBER: _ClassVar[int]
        DOWNLOAD_CONTEXT_FIELD_NUMBER: _ClassVar[int]
        INITIATE_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
        EXPIRY_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
        AVAILABLE_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
        TASK_ID_VEC_FIELD_NUMBER: _ClassVar[int]
        IS_EXPEDITED_RESTORE_FIELD_NUMBER: _ClassVar[int]
        offset: int
        size: int
        sequence_num: int
        download_context: _vault_pb2.VaultDownloadContextProto
        initiate_timestamp_usecs: int
        expiry_timestamp_usecs: int
        available_timestamp_usecs: int
        task_id_vec: _containers.RepeatedCompositeFieldContainer[PrepareRangesTaskIdProto]
        is_expedited_restore: bool
        def __init__(self, offset: _Optional[int] = ..., size: _Optional[int] = ..., sequence_num: _Optional[int] = ..., download_context: _Optional[_Union[_vault_pb2.VaultDownloadContextProto, _Mapping]] = ..., initiate_timestamp_usecs: _Optional[int] = ..., expiry_timestamp_usecs: _Optional[int] = ..., available_timestamp_usecs: _Optional[int] = ..., task_id_vec: _Optional[_Iterable[_Union[PrepareRangesTaskIdProto, _Mapping]]] = ..., is_expedited_restore: bool = ...) -> None: ...
    OBJECT_NAME_FIELD_NUMBER: _ClassVar[int]
    NEXT_SEQUENCE_NUM_FIELD_NUMBER: _ClassVar[int]
    OBJECT_RANGE_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    OPCLOCK_VEC_FIELD_NUMBER: _ClassVar[int]
    object_name: str
    next_sequence_num: int
    object_range_info_vec: _containers.RepeatedCompositeFieldContainer[PreparedObjectProto.ObjectRangeInfo]
    opclock_vec: _containers.RepeatedCompositeFieldContainer[_op_clock_pb2.OpClock]
    def __init__(self, object_name: _Optional[str] = ..., next_sequence_num: _Optional[int] = ..., object_range_info_vec: _Optional[_Iterable[_Union[PreparedObjectProto.ObjectRangeInfo, _Mapping]]] = ..., opclock_vec: _Optional[_Iterable[_Union[_op_clock_pb2.OpClock, _Mapping]]] = ...) -> None: ...

class ObjectPreparationState(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class FSFileProto(_message.Message):
    __slots__ = ("rel_file_path", "file_size", "archive_object_uid", "offset")
    REL_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    FILE_SIZE_FIELD_NUMBER: _ClassVar[int]
    ARCHIVE_OBJECT_UID_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    rel_file_path: str
    file_size: int
    archive_object_uid: _universal_id_pb2.UniversalIdProto
    offset: int
    def __init__(self, rel_file_path: _Optional[str] = ..., file_size: _Optional[int] = ..., archive_object_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., offset: _Optional[int] = ...) -> None: ...

class VaultFSWalkerCookieProto(_message.Message):
    __slots__ = ("curr_working_dir_path", "last_processed_entry", "read_dir_cookie", "all_entries_processed_at_curr_level", "range_vec")
    class FSWalkerRange(_message.Message):
        __slots__ = ("range_root_dir", "last_processed_file_path", "can_split_range", "exhausted", "skip_directory_walking")
        RANGE_ROOT_DIR_FIELD_NUMBER: _ClassVar[int]
        LAST_PROCESSED_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
        CAN_SPLIT_RANGE_FIELD_NUMBER: _ClassVar[int]
        EXHAUSTED_FIELD_NUMBER: _ClassVar[int]
        SKIP_DIRECTORY_WALKING_FIELD_NUMBER: _ClassVar[int]
        range_root_dir: str
        last_processed_file_path: str
        can_split_range: bool
        exhausted: bool
        skip_directory_walking: bool
        def __init__(self, range_root_dir: _Optional[str] = ..., last_processed_file_path: _Optional[str] = ..., can_split_range: bool = ..., exhausted: bool = ..., skip_directory_walking: bool = ...) -> None: ...
    CURR_WORKING_DIR_PATH_FIELD_NUMBER: _ClassVar[int]
    LAST_PROCESSED_ENTRY_FIELD_NUMBER: _ClassVar[int]
    READ_DIR_COOKIE_FIELD_NUMBER: _ClassVar[int]
    ALL_ENTRIES_PROCESSED_AT_CURR_LEVEL_FIELD_NUMBER: _ClassVar[int]
    RANGE_VEC_FIELD_NUMBER: _ClassVar[int]
    curr_working_dir_path: str
    last_processed_entry: str
    read_dir_cookie: int
    all_entries_processed_at_curr_level: bool
    range_vec: _containers.RepeatedCompositeFieldContainer[VaultFSWalkerCookieProto.FSWalkerRange]
    def __init__(self, curr_working_dir_path: _Optional[str] = ..., last_processed_entry: _Optional[str] = ..., read_dir_cookie: _Optional[int] = ..., all_entries_processed_at_curr_level: bool = ..., range_vec: _Optional[_Iterable[_Union[VaultFSWalkerCookieProto.FSWalkerRange, _Mapping]]] = ...) -> None: ...

class ArchiveObjectRestoreInfo(_message.Message):
    __slots__ = ("archive_object_uid", "object_file_path", "num_data_files", "object_file_offset")
    ARCHIVE_OBJECT_UID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    NUM_DATA_FILES_FIELD_NUMBER: _ClassVar[int]
    OBJECT_FILE_OFFSET_FIELD_NUMBER: _ClassVar[int]
    archive_object_uid: _universal_id_pb2.UniversalIdProto
    object_file_path: str
    num_data_files: int
    object_file_offset: int
    def __init__(self, archive_object_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., object_file_path: _Optional[str] = ..., num_data_files: _Optional[int] = ..., object_file_offset: _Optional[int] = ...) -> None: ...

class RestoredHardlinkKeyProto(_message.Message):
    __slots__ = ("restore_job_uid", "view_id", "fs_name", "inode_id")
    RESTORE_JOB_UID_FIELD_NUMBER: _ClassVar[int]
    VIEW_ID_FIELD_NUMBER: _ClassVar[int]
    FS_NAME_FIELD_NUMBER: _ClassVar[int]
    INODE_ID_FIELD_NUMBER: _ClassVar[int]
    restore_job_uid: _universal_id_pb2.UniversalIdProto
    view_id: int
    fs_name: str
    inode_id: int
    def __init__(self, restore_job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., view_id: _Optional[int] = ..., fs_name: _Optional[str] = ..., inode_id: _Optional[int] = ...) -> None: ...

class RestoredHardlinkValueProto(_message.Message):
    __slots__ = ("local_inode_id", "task_id", "opclock_vec")
    LOCAL_INODE_ID_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    OPCLOCK_VEC_FIELD_NUMBER: _ClassVar[int]
    local_inode_id: int
    task_id: int
    opclock_vec: _containers.RepeatedCompositeFieldContainer[_op_clock_pb2.OpClock]
    def __init__(self, local_inode_id: _Optional[int] = ..., task_id: _Optional[int] = ..., opclock_vec: _Optional[_Iterable[_Union[_op_clock_pb2.OpClock, _Mapping]]] = ...) -> None: ...

class ArchiveFilesRequest(_message.Message):
    __slots__ = ("request_id", "progress_monitor_path", "blob_info_vec")
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_MONITOR_PATH_FIELD_NUMBER: _ClassVar[int]
    BLOB_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    request_id: str
    progress_monitor_path: str
    blob_info_vec: _containers.RepeatedCompositeFieldContainer[BlobInfo]
    def __init__(self, request_id: _Optional[str] = ..., progress_monitor_path: _Optional[str] = ..., blob_info_vec: _Optional[_Iterable[_Union[BlobInfo, _Mapping]]] = ...) -> None: ...

class DirectArchiveObjectProto(_message.Message):
    __slots__ = ("inode_metadata", "upload_context", "morphed_objects_info", "object_name_vec")
    class MorphedObjectsInfo(_message.Message):
        __slots__ = ("start_index", "batch_size", "object_name_prefix")
        START_INDEX_FIELD_NUMBER: _ClassVar[int]
        BATCH_SIZE_FIELD_NUMBER: _ClassVar[int]
        OBJECT_NAME_PREFIX_FIELD_NUMBER: _ClassVar[int]
        start_index: int
        batch_size: int
        object_name_prefix: str
        def __init__(self, start_index: _Optional[int] = ..., batch_size: _Optional[int] = ..., object_name_prefix: _Optional[str] = ...) -> None: ...
    INODE_METADATA_FIELD_NUMBER: _ClassVar[int]
    UPLOAD_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    MORPHED_OBJECTS_INFO_FIELD_NUMBER: _ClassVar[int]
    OBJECT_NAME_VEC_FIELD_NUMBER: _ClassVar[int]
    inode_metadata: _snap_fs_metadata_pb2.InodeMetadataProto
    upload_context: _vault_pb2.VaultUploadContextProto
    morphed_objects_info: DirectArchiveObjectProto.MorphedObjectsInfo
    object_name_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, inode_metadata: _Optional[_Union[_snap_fs_metadata_pb2.InodeMetadataProto, _Mapping]] = ..., upload_context: _Optional[_Union[_vault_pb2.VaultUploadContextProto, _Mapping]] = ..., morphed_objects_info: _Optional[_Union[DirectArchiveObjectProto.MorphedObjectsInfo, _Mapping]] = ..., object_name_vec: _Optional[_Iterable[str]] = ...) -> None: ...

class ObjectsValidationActions(_message.Message):
    __slots__ = ("check_objects_in_archive_tier", "check_missing_objects", "check_lifecycle_policy")
    CHECK_OBJECTS_IN_ARCHIVE_TIER_FIELD_NUMBER: _ClassVar[int]
    CHECK_MISSING_OBJECTS_FIELD_NUMBER: _ClassVar[int]
    CHECK_LIFECYCLE_POLICY_FIELD_NUMBER: _ClassVar[int]
    check_objects_in_archive_tier: bool
    check_missing_objects: bool
    check_lifecycle_policy: bool
    def __init__(self, check_objects_in_archive_tier: bool = ..., check_missing_objects: bool = ..., check_lifecycle_policy: bool = ...) -> None: ...

class ObjectsValidationInfo(_message.Message):
    __slots__ = ("archive_tier_object_uid_vec", "missing_object_uid_vec", "corrupt_object_uid_vec", "is_lifecycle_policy_enabled", "storage_class")
    ARCHIVE_TIER_OBJECT_UID_VEC_FIELD_NUMBER: _ClassVar[int]
    MISSING_OBJECT_UID_VEC_FIELD_NUMBER: _ClassVar[int]
    CORRUPT_OBJECT_UID_VEC_FIELD_NUMBER: _ClassVar[int]
    IS_LIFECYCLE_POLICY_ENABLED_FIELD_NUMBER: _ClassVar[int]
    STORAGE_CLASS_FIELD_NUMBER: _ClassVar[int]
    archive_tier_object_uid_vec: _containers.RepeatedCompositeFieldContainer[_universal_id_pb2.UniversalIdProto]
    missing_object_uid_vec: _containers.RepeatedCompositeFieldContainer[_universal_id_pb2.UniversalIdProto]
    corrupt_object_uid_vec: _containers.RepeatedCompositeFieldContainer[_universal_id_pb2.UniversalIdProto]
    is_lifecycle_policy_enabled: bool
    storage_class: str
    def __init__(self, archive_tier_object_uid_vec: _Optional[_Iterable[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]]] = ..., missing_object_uid_vec: _Optional[_Iterable[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]]] = ..., corrupt_object_uid_vec: _Optional[_Iterable[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]]] = ..., is_lifecycle_policy_enabled: bool = ..., storage_class: _Optional[str] = ...) -> None: ...

class ObjectDataFileInfo(_message.Message):
    __slots__ = ("data_file_vec",)
    DATA_FILE_VEC_FIELD_NUMBER: _ClassVar[int]
    data_file_vec: _containers.RepeatedCompositeFieldContainer[FSFileProto]
    def __init__(self, data_file_vec: _Optional[_Iterable[_Union[FSFileProto, _Mapping]]] = ...) -> None: ...

class RestoreObjectMetadataProto(_message.Message):
    __slots__ = ("data_size", "data_checksum", "download_context", "eof")
    DATA_SIZE_FIELD_NUMBER: _ClassVar[int]
    DATA_CHECKSUM_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    EOF_FIELD_NUMBER: _ClassVar[int]
    data_size: int
    data_checksum: int
    download_context: _vault_pb2.VaultDownloadContextProto
    eof: bool
    def __init__(self, data_size: _Optional[int] = ..., data_checksum: _Optional[int] = ..., download_context: _Optional[_Union[_vault_pb2.VaultDownloadContextProto, _Mapping]] = ..., eof: bool = ...) -> None: ...

class StubViewStatsKey(_message.Message):
    __slots__ = ("stub_view_id",)
    STUB_VIEW_ID_FIELD_NUMBER: _ClassVar[int]
    stub_view_id: int
    def __init__(self, stub_view_id: _Optional[int] = ...) -> None: ...

class StubViewStatsProto(_message.Message):
    __slots__ = ("stub_view_id", "logical_bytes_downloaded", "opclock_vec")
    STUB_VIEW_ID_FIELD_NUMBER: _ClassVar[int]
    LOGICAL_BYTES_DOWNLOADED_FIELD_NUMBER: _ClassVar[int]
    OPCLOCK_VEC_FIELD_NUMBER: _ClassVar[int]
    stub_view_id: int
    logical_bytes_downloaded: int
    opclock_vec: _containers.RepeatedCompositeFieldContainer[_op_clock_pb2.OpClock]
    def __init__(self, stub_view_id: _Optional[int] = ..., logical_bytes_downloaded: _Optional[int] = ..., opclock_vec: _Optional[_Iterable[_Union[_op_clock_pb2.OpClock, _Mapping]]] = ...) -> None: ...

class CloudDomainRestoredNodeKey(_message.Message):
    __slots__ = ("domain_id", "node_ptr", "view_id", "viewbox_id")
    DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    NODE_PTR_FIELD_NUMBER: _ClassVar[int]
    VIEW_ID_FIELD_NUMBER: _ClassVar[int]
    VIEWBOX_ID_FIELD_NUMBER: _ClassVar[int]
    domain_id: int
    node_ptr: _cloud_pb2.CloudNodePtrProto
    view_id: int
    viewbox_id: int
    def __init__(self, domain_id: _Optional[int] = ..., node_ptr: _Optional[_Union[_cloud_pb2.CloudNodePtrProto, _Mapping]] = ..., view_id: _Optional[int] = ..., viewbox_id: _Optional[int] = ...) -> None: ...

class CloudDomainRestoredNodeValue(_message.Message):
    __slots__ = ("tree_id", "node_id", "restored_sub_tree", "touched_timestamp_usecs")
    TREE_ID_FIELD_NUMBER: _ClassVar[int]
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    RESTORED_SUB_TREE_FIELD_NUMBER: _ClassVar[int]
    TOUCHED_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
    tree_id: int
    node_id: int
    restored_sub_tree: bool
    touched_timestamp_usecs: int
    def __init__(self, tree_id: _Optional[int] = ..., node_id: _Optional[int] = ..., restored_sub_tree: bool = ..., touched_timestamp_usecs: _Optional[int] = ...) -> None: ...

class IceboxConfigProto(_message.Message):
    __slots__ = ("ideal_segment_size_MB", "icebox_master_key", "icebox_stats_uri", "icebox_features_key", "icebox_base_uri", "validate_vault_config_uri", "add_update_vault_uri", "get_vaults_uri", "delete_vault_uri", "query_archive_media_info_uri", "get_vault_encryption_key_info_uri", "schedule_vault_search_job_uri", "get_vault_search_jobs_uri", "cancel_job_uri", "query_vault_search_job_uri", "upload_vault_encryption_keys_info_uri", "schedule_restore_index_and_snapshot_jobs_uri", "query_restore_index_and_snapshot_jobs_uri", "add_update_icebox_properties_uri", "get_icebox_properties_uri", "schedule_cloud_domain_migration_job_uri", "cancel_cloud_domain_migration_job_uri", "query_cloud_domain_migration_job_uri", "fetch_cloud_snapshot_uri", "initiate_cloud_domain_migration_uri", "get_or_create_cloud_domain_uri", "fetch_uptier_data_size_uri", "schedule_cloud_domain_rebuild_job_uri", "schedule_restore_job_uri", "query_restore_jobs_uri")
    IDEAL_SEGMENT_SIZE_MB_FIELD_NUMBER: _ClassVar[int]
    ICEBOX_MASTER_KEY_FIELD_NUMBER: _ClassVar[int]
    ICEBOX_STATS_URI_FIELD_NUMBER: _ClassVar[int]
    ICEBOX_FEATURES_KEY_FIELD_NUMBER: _ClassVar[int]
    ICEBOX_BASE_URI_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_VAULT_CONFIG_URI_FIELD_NUMBER: _ClassVar[int]
    ADD_UPDATE_VAULT_URI_FIELD_NUMBER: _ClassVar[int]
    GET_VAULTS_URI_FIELD_NUMBER: _ClassVar[int]
    DELETE_VAULT_URI_FIELD_NUMBER: _ClassVar[int]
    QUERY_ARCHIVE_MEDIA_INFO_URI_FIELD_NUMBER: _ClassVar[int]
    GET_VAULT_ENCRYPTION_KEY_INFO_URI_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_VAULT_SEARCH_JOB_URI_FIELD_NUMBER: _ClassVar[int]
    GET_VAULT_SEARCH_JOBS_URI_FIELD_NUMBER: _ClassVar[int]
    CANCEL_JOB_URI_FIELD_NUMBER: _ClassVar[int]
    QUERY_VAULT_SEARCH_JOB_URI_FIELD_NUMBER: _ClassVar[int]
    UPLOAD_VAULT_ENCRYPTION_KEYS_INFO_URI_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_RESTORE_INDEX_AND_SNAPSHOT_JOBS_URI_FIELD_NUMBER: _ClassVar[int]
    QUERY_RESTORE_INDEX_AND_SNAPSHOT_JOBS_URI_FIELD_NUMBER: _ClassVar[int]
    ADD_UPDATE_ICEBOX_PROPERTIES_URI_FIELD_NUMBER: _ClassVar[int]
    GET_ICEBOX_PROPERTIES_URI_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_CLOUD_DOMAIN_MIGRATION_JOB_URI_FIELD_NUMBER: _ClassVar[int]
    CANCEL_CLOUD_DOMAIN_MIGRATION_JOB_URI_FIELD_NUMBER: _ClassVar[int]
    QUERY_CLOUD_DOMAIN_MIGRATION_JOB_URI_FIELD_NUMBER: _ClassVar[int]
    FETCH_CLOUD_SNAPSHOT_URI_FIELD_NUMBER: _ClassVar[int]
    INITIATE_CLOUD_DOMAIN_MIGRATION_URI_FIELD_NUMBER: _ClassVar[int]
    GET_OR_CREATE_CLOUD_DOMAIN_URI_FIELD_NUMBER: _ClassVar[int]
    FETCH_UPTIER_DATA_SIZE_URI_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_CLOUD_DOMAIN_REBUILD_JOB_URI_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_RESTORE_JOB_URI_FIELD_NUMBER: _ClassVar[int]
    QUERY_RESTORE_JOBS_URI_FIELD_NUMBER: _ClassVar[int]
    ideal_segment_size_MB: int
    icebox_master_key: str
    icebox_stats_uri: str
    icebox_features_key: str
    icebox_base_uri: str
    validate_vault_config_uri: str
    add_update_vault_uri: str
    get_vaults_uri: str
    delete_vault_uri: str
    query_archive_media_info_uri: str
    get_vault_encryption_key_info_uri: str
    schedule_vault_search_job_uri: str
    get_vault_search_jobs_uri: str
    cancel_job_uri: str
    query_vault_search_job_uri: str
    upload_vault_encryption_keys_info_uri: str
    schedule_restore_index_and_snapshot_jobs_uri: str
    query_restore_index_and_snapshot_jobs_uri: str
    add_update_icebox_properties_uri: str
    get_icebox_properties_uri: str
    schedule_cloud_domain_migration_job_uri: str
    cancel_cloud_domain_migration_job_uri: str
    query_cloud_domain_migration_job_uri: str
    fetch_cloud_snapshot_uri: str
    initiate_cloud_domain_migration_uri: str
    get_or_create_cloud_domain_uri: str
    fetch_uptier_data_size_uri: str
    schedule_cloud_domain_rebuild_job_uri: str
    schedule_restore_job_uri: str
    query_restore_jobs_uri: str
    def __init__(self, ideal_segment_size_MB: _Optional[int] = ..., icebox_master_key: _Optional[str] = ..., icebox_stats_uri: _Optional[str] = ..., icebox_features_key: _Optional[str] = ..., icebox_base_uri: _Optional[str] = ..., validate_vault_config_uri: _Optional[str] = ..., add_update_vault_uri: _Optional[str] = ..., get_vaults_uri: _Optional[str] = ..., delete_vault_uri: _Optional[str] = ..., query_archive_media_info_uri: _Optional[str] = ..., get_vault_encryption_key_info_uri: _Optional[str] = ..., schedule_vault_search_job_uri: _Optional[str] = ..., get_vault_search_jobs_uri: _Optional[str] = ..., cancel_job_uri: _Optional[str] = ..., query_vault_search_job_uri: _Optional[str] = ..., upload_vault_encryption_keys_info_uri: _Optional[str] = ..., schedule_restore_index_and_snapshot_jobs_uri: _Optional[str] = ..., query_restore_index_and_snapshot_jobs_uri: _Optional[str] = ..., add_update_icebox_properties_uri: _Optional[str] = ..., get_icebox_properties_uri: _Optional[str] = ..., schedule_cloud_domain_migration_job_uri: _Optional[str] = ..., cancel_cloud_domain_migration_job_uri: _Optional[str] = ..., query_cloud_domain_migration_job_uri: _Optional[str] = ..., fetch_cloud_snapshot_uri: _Optional[str] = ..., initiate_cloud_domain_migration_uri: _Optional[str] = ..., get_or_create_cloud_domain_uri: _Optional[str] = ..., fetch_uptier_data_size_uri: _Optional[str] = ..., schedule_cloud_domain_rebuild_job_uri: _Optional[str] = ..., schedule_restore_job_uri: _Optional[str] = ..., query_restore_jobs_uri: _Optional[str] = ...) -> None: ...

class CloudDomainConfig(_message.Message):
    __slots__ = ("cluster_name", "vault_name", "viewbox_name", "prefix")
    CLUSTER_NAME_FIELD_NUMBER: _ClassVar[int]
    VAULT_NAME_FIELD_NUMBER: _ClassVar[int]
    VIEWBOX_NAME_FIELD_NUMBER: _ClassVar[int]
    PREFIX_FIELD_NUMBER: _ClassVar[int]
    cluster_name: str
    vault_name: str
    viewbox_name: str
    prefix: str
    def __init__(self, cluster_name: _Optional[str] = ..., vault_name: _Optional[str] = ..., viewbox_name: _Optional[str] = ..., prefix: _Optional[str] = ...) -> None: ...

class CloudDomainConfigFileContent(_message.Message):
    __slots__ = ("cloud_domain_config", "edek")
    CLOUD_DOMAIN_CONFIG_FIELD_NUMBER: _ClassVar[int]
    EDEK_FIELD_NUMBER: _ClassVar[int]
    cloud_domain_config: bytes
    edek: _keychain_pb2.EdekProto
    def __init__(self, cloud_domain_config: _Optional[bytes] = ..., edek: _Optional[_Union[_keychain_pb2.EdekProto, _Mapping]] = ...) -> None: ...

class CloudDomainConfigVersionedFileContent(_message.Message):
    __slots__ = ("version", "cloud_domain_config", "edek")
    VERSION_FIELD_NUMBER: _ClassVar[int]
    CLOUD_DOMAIN_CONFIG_FIELD_NUMBER: _ClassVar[int]
    EDEK_FIELD_NUMBER: _ClassVar[int]
    version: int
    cloud_domain_config: bytes
    edek: _keychain_pb2.EdekProto
    def __init__(self, version: _Optional[int] = ..., cloud_domain_config: _Optional[bytes] = ..., edek: _Optional[_Union[_keychain_pb2.EdekProto, _Mapping]] = ...) -> None: ...

class CloudDomainAccessInfo(_message.Message):
    __slots__ = ("cloud_domain_config", "dek_uid", "is_vault_kms", "prefix", "cloud_domain_scanned")
    CLOUD_DOMAIN_CONFIG_FIELD_NUMBER: _ClassVar[int]
    DEK_UID_FIELD_NUMBER: _ClassVar[int]
    IS_VAULT_KMS_FIELD_NUMBER: _ClassVar[int]
    PREFIX_FIELD_NUMBER: _ClassVar[int]
    CLOUD_DOMAIN_SCANNED_FIELD_NUMBER: _ClassVar[int]
    cloud_domain_config: CloudDomainConfig
    dek_uid: _universal_id_pb2.UniversalIdProto
    is_vault_kms: bool
    prefix: str
    cloud_domain_scanned: bool
    def __init__(self, cloud_domain_config: _Optional[_Union[CloudDomainConfig, _Mapping]] = ..., dek_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., is_vault_kms: bool = ..., prefix: _Optional[str] = ..., cloud_domain_scanned: bool = ...) -> None: ...

class CustomSnapTreeRootNames(_message.Message):
    __slots__ = ("s3object_snap_tree_root_name",)
    S3OBJECT_SNAP_TREE_ROOT_NAME_FIELD_NUMBER: _ClassVar[int]
    s3object_snap_tree_root_name: str
    def __init__(self, s3object_snap_tree_root_name: _Optional[str] = ...) -> None: ...

class WorkloadTag(_message.Message):
    __slots__ = ("app_job_uid", "source_type", "entity_id")
    APP_JOB_UID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    app_job_uid: _universal_id_pb2.UniversalIdProto
    source_type: _enums_pb2.Environment.Type
    entity_id: int
    def __init__(self, app_job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., source_type: _Optional[_Union[_enums_pb2.Environment.Type, str]] = ..., entity_id: _Optional[int] = ...) -> None: ...

class InvalidCloudLocationProto(_message.Message):
    __slots__ = ("cloud_node_location", "cloud_chunk_location")
    class CloudSnapTreeNodeLocation(_message.Message):
        __slots__ = ("domain_id", "cloud_node_ptr", "tree_type")
        DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
        CLOUD_NODE_PTR_FIELD_NUMBER: _ClassVar[int]
        TREE_TYPE_FIELD_NUMBER: _ClassVar[int]
        domain_id: int
        cloud_node_ptr: _cloud_pb2.CloudNodePtrProto
        tree_type: IceboxSnapTreeType
        def __init__(self, domain_id: _Optional[int] = ..., cloud_node_ptr: _Optional[_Union[_cloud_pb2.CloudNodePtrProto, _Mapping]] = ..., tree_type: _Optional[_Union[IceboxSnapTreeType, str]] = ...) -> None: ...
    CLOUD_NODE_LOCATION_FIELD_NUMBER: _ClassVar[int]
    CLOUD_CHUNK_LOCATION_FIELD_NUMBER: _ClassVar[int]
    cloud_node_location: InvalidCloudLocationProto.CloudSnapTreeNodeLocation
    cloud_chunk_location: _blob_store_pb2.CloudChunkLocationProto
    def __init__(self, cloud_node_location: _Optional[_Union[InvalidCloudLocationProto.CloudSnapTreeNodeLocation, _Mapping]] = ..., cloud_chunk_location: _Optional[_Union[_blob_store_pb2.CloudChunkLocationProto, _Mapping]] = ...) -> None: ...

class InvalidCloudLocationValueProto(_message.Message):
    __slots__ = ("opclock_vec",)
    OPCLOCK_VEC_FIELD_NUMBER: _ClassVar[int]
    opclock_vec: _containers.RepeatedCompositeFieldContainer[_op_clock_pb2.OpClock]
    def __init__(self, opclock_vec: _Optional[_Iterable[_Union[_op_clock_pb2.OpClock, _Mapping]]] = ...) -> None: ...

class InvalidArchivedNodeKeyProto(_message.Message):
    __slots__ = ("cloud_domain_id", "view_id", "vst_node_info", "bst_node_info")
    class VSTNodeInfo(_message.Message):
        __slots__ = ("root_id", "node_id", "key")
        ROOT_ID_FIELD_NUMBER: _ClassVar[int]
        NODE_ID_FIELD_NUMBER: _ClassVar[int]
        KEY_FIELD_NUMBER: _ClassVar[int]
        root_id: int
        node_id: int
        key: int
        def __init__(self, root_id: _Optional[int] = ..., node_id: _Optional[int] = ..., key: _Optional[int] = ...) -> None: ...
    class BSTNodeInfo(_message.Message):
        __slots__ = ("root_id", "node_id", "key")
        ROOT_ID_FIELD_NUMBER: _ClassVar[int]
        NODE_ID_FIELD_NUMBER: _ClassVar[int]
        KEY_FIELD_NUMBER: _ClassVar[int]
        root_id: int
        node_id: int
        key: int
        def __init__(self, root_id: _Optional[int] = ..., node_id: _Optional[int] = ..., key: _Optional[int] = ...) -> None: ...
    CLOUD_DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_ID_FIELD_NUMBER: _ClassVar[int]
    VST_NODE_INFO_FIELD_NUMBER: _ClassVar[int]
    BST_NODE_INFO_FIELD_NUMBER: _ClassVar[int]
    cloud_domain_id: int
    view_id: int
    vst_node_info: InvalidArchivedNodeKeyProto.VSTNodeInfo
    bst_node_info: InvalidArchivedNodeKeyProto.BSTNodeInfo
    def __init__(self, cloud_domain_id: _Optional[int] = ..., view_id: _Optional[int] = ..., vst_node_info: _Optional[_Union[InvalidArchivedNodeKeyProto.VSTNodeInfo, _Mapping]] = ..., bst_node_info: _Optional[_Union[InvalidArchivedNodeKeyProto.BSTNodeInfo, _Mapping]] = ...) -> None: ...

class InvalidArchivedNodeValueProto(_message.Message):
    __slots__ = ("opclock_vec", "view_info")
    class ViewInfo(_message.Message):
        __slots__ = ("view_id", "root_snap_tree_id", "root_inode_id", "view_name", "root_inode_path")
        VIEW_ID_FIELD_NUMBER: _ClassVar[int]
        ROOT_SNAP_TREE_ID_FIELD_NUMBER: _ClassVar[int]
        ROOT_INODE_ID_FIELD_NUMBER: _ClassVar[int]
        VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
        ROOT_INODE_PATH_FIELD_NUMBER: _ClassVar[int]
        view_id: int
        root_snap_tree_id: int
        root_inode_id: int
        view_name: str
        root_inode_path: str
        def __init__(self, view_id: _Optional[int] = ..., root_snap_tree_id: _Optional[int] = ..., root_inode_id: _Optional[int] = ..., view_name: _Optional[str] = ..., root_inode_path: _Optional[str] = ...) -> None: ...
    OPCLOCK_VEC_FIELD_NUMBER: _ClassVar[int]
    VIEW_INFO_FIELD_NUMBER: _ClassVar[int]
    opclock_vec: _containers.RepeatedCompositeFieldContainer[_op_clock_pb2.OpClock]
    view_info: InvalidArchivedNodeValueProto.ViewInfo
    def __init__(self, opclock_vec: _Optional[_Iterable[_Union[_op_clock_pb2.OpClock, _Mapping]]] = ..., view_info: _Optional[_Union[InvalidArchivedNodeValueProto.ViewInfo, _Mapping]] = ...) -> None: ...

class InvalidArchivedChunkKeyProto(_message.Message):
    __slots__ = ("cloud_domain_id", "chunk_id")
    CLOUD_DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    CHUNK_ID_FIELD_NUMBER: _ClassVar[int]
    cloud_domain_id: int
    chunk_id: _blob_store_pb2.ChunkIdProto
    def __init__(self, cloud_domain_id: _Optional[int] = ..., chunk_id: _Optional[_Union[_blob_store_pb2.ChunkIdProto, _Mapping]] = ...) -> None: ...

class InvalidArchivedChunkValueProto(_message.Message):
    __slots__ = ("opclock_vec",)
    OPCLOCK_VEC_FIELD_NUMBER: _ClassVar[int]
    opclock_vec: _containers.RepeatedCompositeFieldContainer[_op_clock_pb2.OpClock]
    def __init__(self, opclock_vec: _Optional[_Iterable[_Union[_op_clock_pb2.OpClock, _Mapping]]] = ...) -> None: ...
