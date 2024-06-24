from bridge.base import cloud_pb2 as _cloud_pb2
from bridge.base import error_pb2 as _error_pb2
from bridge.snap_fs import entity_handle_pb2 as _entity_handle_pb2
from bridge.snap_fs import snap_fs_metadata_pb2 as _snap_fs_metadata_pb2
from bridge.snap_tree import snap_tree_pb2 as _snap_tree_pb2
from bridge.icebox.base import icebox_pb2 as _icebox_pb2
from bridge.icebox.master.stub import rpc_service_pb2 as _rpc_service_pb2
from bridge.vault.base import vault_pb2 as _vault_pb2
from bridge.vault.base import worm_pb2 as _worm_pb2
from cohesion.base import common_pb2 as _common_pb2
from magneto.base import magneto_pb2 as _magneto_pb2
from magneto.base import env_params_pb2 as _env_params_pb2
from open_util.net import protorpc_pb2 as _protorpc_pb2
from util.base import universal_id_pb2 as _universal_id_pb2
from yoda.base import yoda_types_pb2 as _yoda_types_pb2
from magneto.directory_walker import directory_walker_pb2 as _directory_walker_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateArchivalViewArg(_message.Message):
    __slots__ = ("archive_uid", "job_params", "target_view_name")
    ARCHIVE_UID_FIELD_NUMBER: _ClassVar[int]
    JOB_PARAMS_FIELD_NUMBER: _ClassVar[int]
    TARGET_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    archive_uid: _universal_id_pb2.UniversalIdProto
    job_params: _rpc_service_pb2.ArchivalJobParams
    target_view_name: str
    def __init__(self, archive_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., job_params: _Optional[_Union[_rpc_service_pb2.ArchivalJobParams, _Mapping]] = ..., target_view_name: _Optional[str] = ...) -> None: ...

class CreateArchivalViewResult(_message.Message):
    __slots__ = ("view_id", "view_size_bytes")
    VIEW_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    view_id: int
    view_size_bytes: int
    def __init__(self, view_id: _Optional[int] = ..., view_size_bytes: _Optional[int] = ...) -> None: ...

class CloneDirectoriesArg(_message.Message):
    __slots__ = ("view_box_id", "src_view_name", "dst_view_name", "create_dst_view", "clone_dir_param_vec")
    class CloneDirectoryParams(_message.Message):
        __slots__ = ("view_fs_name", "src_relative_dir_path", "dst_relative_dir_path")
        VIEW_FS_NAME_FIELD_NUMBER: _ClassVar[int]
        SRC_RELATIVE_DIR_PATH_FIELD_NUMBER: _ClassVar[int]
        DST_RELATIVE_DIR_PATH_FIELD_NUMBER: _ClassVar[int]
        view_fs_name: str
        src_relative_dir_path: str
        dst_relative_dir_path: str
        def __init__(self, view_fs_name: _Optional[str] = ..., src_relative_dir_path: _Optional[str] = ..., dst_relative_dir_path: _Optional[str] = ...) -> None: ...
    VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
    SRC_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    DST_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_DST_VIEW_FIELD_NUMBER: _ClassVar[int]
    CLONE_DIR_PARAM_VEC_FIELD_NUMBER: _ClassVar[int]
    view_box_id: int
    src_view_name: str
    dst_view_name: str
    create_dst_view: bool
    clone_dir_param_vec: _containers.RepeatedCompositeFieldContainer[CloneDirectoriesArg.CloneDirectoryParams]
    def __init__(self, view_box_id: _Optional[int] = ..., src_view_name: _Optional[str] = ..., dst_view_name: _Optional[str] = ..., create_dst_view: bool = ..., clone_dir_param_vec: _Optional[_Iterable[_Union[CloneDirectoriesArg.CloneDirectoryParams, _Mapping]]] = ...) -> None: ...

class CloneDirectoriesResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class ScheduleArchivalTaskArg(_message.Message):
    __slots__ = ("job_params", "checkpoint_info", "index_file_path", "index_progress_monitor_task_path")
    JOB_PARAMS_FIELD_NUMBER: _ClassVar[int]
    CHECKPOINT_INFO_FIELD_NUMBER: _ClassVar[int]
    INDEX_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    INDEX_PROGRESS_MONITOR_TASK_PATH_FIELD_NUMBER: _ClassVar[int]
    job_params: _rpc_service_pb2.ArchivalJobParams
    checkpoint_info: _icebox_pb2.TaskCheckpointInfo
    index_file_path: str
    index_progress_monitor_task_path: str
    def __init__(self, job_params: _Optional[_Union[_rpc_service_pb2.ArchivalJobParams, _Mapping]] = ..., checkpoint_info: _Optional[_Union[_icebox_pb2.TaskCheckpointInfo, _Mapping]] = ..., index_file_path: _Optional[str] = ..., index_progress_monitor_task_path: _Optional[str] = ...) -> None: ...

class ScheduleArchivalTaskResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ArchiveArg(_message.Message):
    __slots__ = ("archive_uid", "task_id", "view_box_id", "cloud_domain_id", "snap_tree_info_vec", "epoch_id", "app_job_uid", "total_view_snap_tree_nodes_to_be_archived", "skip_progress_reporting", "root_progress_monitor_path", "max_sub_trees_in_parallel", "acquire_pins_and_locks", "archive_all_snap_tree_nodes", "enable_fetb_calculation", "worm_params", "is_view_snap_tree", "calculate_frontend_size_info_for_existing_incrementals")
    class SnapTreeInfo(_message.Message):
        __slots__ = ("root_tree_id", "sub_tree_root_tree_id", "sub_tree_root_node_id", "view_id", "view_snap_tree_id", "tree_type", "total_view_snap_tree_nodes_to_be_archived", "total_logical_size_to_be_archived", "progress_monitor_task_path")
        ROOT_TREE_ID_FIELD_NUMBER: _ClassVar[int]
        SUB_TREE_ROOT_TREE_ID_FIELD_NUMBER: _ClassVar[int]
        SUB_TREE_ROOT_NODE_ID_FIELD_NUMBER: _ClassVar[int]
        VIEW_ID_FIELD_NUMBER: _ClassVar[int]
        VIEW_SNAP_TREE_ID_FIELD_NUMBER: _ClassVar[int]
        TREE_TYPE_FIELD_NUMBER: _ClassVar[int]
        TOTAL_VIEW_SNAP_TREE_NODES_TO_BE_ARCHIVED_FIELD_NUMBER: _ClassVar[int]
        TOTAL_LOGICAL_SIZE_TO_BE_ARCHIVED_FIELD_NUMBER: _ClassVar[int]
        PROGRESS_MONITOR_TASK_PATH_FIELD_NUMBER: _ClassVar[int]
        root_tree_id: int
        sub_tree_root_tree_id: int
        sub_tree_root_node_id: int
        view_id: int
        view_snap_tree_id: int
        tree_type: _icebox_pb2.IceboxSnapTreeType
        total_view_snap_tree_nodes_to_be_archived: int
        total_logical_size_to_be_archived: int
        progress_monitor_task_path: str
        def __init__(self, root_tree_id: _Optional[int] = ..., sub_tree_root_tree_id: _Optional[int] = ..., sub_tree_root_node_id: _Optional[int] = ..., view_id: _Optional[int] = ..., view_snap_tree_id: _Optional[int] = ..., tree_type: _Optional[_Union[_icebox_pb2.IceboxSnapTreeType, str]] = ..., total_view_snap_tree_nodes_to_be_archived: _Optional[int] = ..., total_logical_size_to_be_archived: _Optional[int] = ..., progress_monitor_task_path: _Optional[str] = ...) -> None: ...
    ARCHIVE_UID_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
    CLOUD_DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    SNAP_TREE_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    EPOCH_ID_FIELD_NUMBER: _ClassVar[int]
    APP_JOB_UID_FIELD_NUMBER: _ClassVar[int]
    TOTAL_VIEW_SNAP_TREE_NODES_TO_BE_ARCHIVED_FIELD_NUMBER: _ClassVar[int]
    SKIP_PROGRESS_REPORTING_FIELD_NUMBER: _ClassVar[int]
    ROOT_PROGRESS_MONITOR_PATH_FIELD_NUMBER: _ClassVar[int]
    MAX_SUB_TREES_IN_PARALLEL_FIELD_NUMBER: _ClassVar[int]
    ACQUIRE_PINS_AND_LOCKS_FIELD_NUMBER: _ClassVar[int]
    ARCHIVE_ALL_SNAP_TREE_NODES_FIELD_NUMBER: _ClassVar[int]
    ENABLE_FETB_CALCULATION_FIELD_NUMBER: _ClassVar[int]
    WORM_PARAMS_FIELD_NUMBER: _ClassVar[int]
    IS_VIEW_SNAP_TREE_FIELD_NUMBER: _ClassVar[int]
    CALCULATE_FRONTEND_SIZE_INFO_FOR_EXISTING_INCREMENTALS_FIELD_NUMBER: _ClassVar[int]
    archive_uid: _universal_id_pb2.UniversalIdProto
    task_id: int
    view_box_id: int
    cloud_domain_id: int
    snap_tree_info_vec: _containers.RepeatedCompositeFieldContainer[ArchiveArg.SnapTreeInfo]
    epoch_id: int
    app_job_uid: _universal_id_pb2.UniversalIdProto
    total_view_snap_tree_nodes_to_be_archived: int
    skip_progress_reporting: bool
    root_progress_monitor_path: str
    max_sub_trees_in_parallel: int
    acquire_pins_and_locks: bool
    archive_all_snap_tree_nodes: bool
    enable_fetb_calculation: bool
    worm_params: _worm_pb2.WORMParams
    is_view_snap_tree: bool
    calculate_frontend_size_info_for_existing_incrementals: bool
    def __init__(self, archive_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., task_id: _Optional[int] = ..., view_box_id: _Optional[int] = ..., cloud_domain_id: _Optional[int] = ..., snap_tree_info_vec: _Optional[_Iterable[_Union[ArchiveArg.SnapTreeInfo, _Mapping]]] = ..., epoch_id: _Optional[int] = ..., app_job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., total_view_snap_tree_nodes_to_be_archived: _Optional[int] = ..., skip_progress_reporting: bool = ..., root_progress_monitor_path: _Optional[str] = ..., max_sub_trees_in_parallel: _Optional[int] = ..., acquire_pins_and_locks: bool = ..., archive_all_snap_tree_nodes: bool = ..., enable_fetb_calculation: bool = ..., worm_params: _Optional[_Union[_worm_pb2.WORMParams, _Mapping]] = ..., is_view_snap_tree: bool = ..., calculate_frontend_size_info_for_existing_incrementals: bool = ...) -> None: ...

class ArchiveResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ArchiveBlobsArg(_message.Message):
    __slots__ = ("archive_uid", "task_id", "job_params", "view_id", "prev_full_archive_uid", "prev_archive_uid", "node_id_floor", "root_inode_id", "blob_info_vec", "reference_snapshot", "dedup_enabled", "checkpoint_info", "progress_monitor_task_path", "archival_object_type", "flush_data_journal", "archive_version", "use_node_id_floor_to_determine_incremental_archives", "enabled_feature_vec", "direct_archive_enabled", "use_forever_incremental_archive_format")
    ARCHIVE_UID_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    JOB_PARAMS_FIELD_NUMBER: _ClassVar[int]
    VIEW_ID_FIELD_NUMBER: _ClassVar[int]
    PREV_FULL_ARCHIVE_UID_FIELD_NUMBER: _ClassVar[int]
    PREV_ARCHIVE_UID_FIELD_NUMBER: _ClassVar[int]
    NODE_ID_FLOOR_FIELD_NUMBER: _ClassVar[int]
    ROOT_INODE_ID_FIELD_NUMBER: _ClassVar[int]
    BLOB_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    DEDUP_ENABLED_FIELD_NUMBER: _ClassVar[int]
    CHECKPOINT_INFO_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_MONITOR_TASK_PATH_FIELD_NUMBER: _ClassVar[int]
    ARCHIVAL_OBJECT_TYPE_FIELD_NUMBER: _ClassVar[int]
    FLUSH_DATA_JOURNAL_FIELD_NUMBER: _ClassVar[int]
    ARCHIVE_VERSION_FIELD_NUMBER: _ClassVar[int]
    USE_NODE_ID_FLOOR_TO_DETERMINE_INCREMENTAL_ARCHIVES_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FEATURE_VEC_FIELD_NUMBER: _ClassVar[int]
    DIRECT_ARCHIVE_ENABLED_FIELD_NUMBER: _ClassVar[int]
    USE_FOREVER_INCREMENTAL_ARCHIVE_FORMAT_FIELD_NUMBER: _ClassVar[int]
    archive_uid: _universal_id_pb2.UniversalIdProto
    task_id: int
    job_params: _rpc_service_pb2.ArchivalJobParams
    view_id: int
    prev_full_archive_uid: _universal_id_pb2.UniversalIdProto
    prev_archive_uid: _universal_id_pb2.UniversalIdProto
    node_id_floor: int
    root_inode_id: int
    blob_info_vec: _containers.RepeatedCompositeFieldContainer[_icebox_pb2.BlobInfo]
    reference_snapshot: bool
    dedup_enabled: bool
    checkpoint_info: _icebox_pb2.TaskCheckpointInfo
    progress_monitor_task_path: str
    archival_object_type: _icebox_pb2.ArchivalObjectMetadataProto.ObjectType
    flush_data_journal: bool
    archive_version: int
    use_node_id_floor_to_determine_incremental_archives: bool
    enabled_feature_vec: _containers.RepeatedScalarFieldContainer[int]
    direct_archive_enabled: bool
    use_forever_incremental_archive_format: bool
    def __init__(self, archive_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., task_id: _Optional[int] = ..., job_params: _Optional[_Union[_rpc_service_pb2.ArchivalJobParams, _Mapping]] = ..., view_id: _Optional[int] = ..., prev_full_archive_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., prev_archive_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., node_id_floor: _Optional[int] = ..., root_inode_id: _Optional[int] = ..., blob_info_vec: _Optional[_Iterable[_Union[_icebox_pb2.BlobInfo, _Mapping]]] = ..., reference_snapshot: bool = ..., dedup_enabled: bool = ..., checkpoint_info: _Optional[_Union[_icebox_pb2.TaskCheckpointInfo, _Mapping]] = ..., progress_monitor_task_path: _Optional[str] = ..., archival_object_type: _Optional[_Union[_icebox_pb2.ArchivalObjectMetadataProto.ObjectType, str]] = ..., flush_data_journal: bool = ..., archive_version: _Optional[int] = ..., use_node_id_floor_to_determine_incremental_archives: bool = ..., enabled_feature_vec: _Optional[_Iterable[int]] = ..., direct_archive_enabled: bool = ..., use_forever_incremental_archive_format: bool = ...) -> None: ...

class ArchiveBlobsResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ArchiveSnapTreesArg(_message.Message):
    __slots__ = ("archive_uid", "base_archive_uid", "task_id", "job_params", "view_id", "snap_tree_type", "blob_info_vec", "node_id_floor", "checkpoint_info", "progress_monitor_task_path", "prev_base_archive_uid", "archival_object_type", "archive_version", "root_inode_id", "archive_now", "use_node_id_floor_to_determine_incremental_archives", "enabled_feature_vec", "direct_archive_enabled", "native_format", "report_missing_files", "repair_missing_files", "app_job_name", "entity_name")
    class SnapTreeType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kViewSnapTree: _ClassVar[ArchiveSnapTreesArg.SnapTreeType]
        kBlobSnapTree: _ClassVar[ArchiveSnapTreesArg.SnapTreeType]
    kViewSnapTree: ArchiveSnapTreesArg.SnapTreeType
    kBlobSnapTree: ArchiveSnapTreesArg.SnapTreeType
    ARCHIVE_UID_FIELD_NUMBER: _ClassVar[int]
    BASE_ARCHIVE_UID_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    JOB_PARAMS_FIELD_NUMBER: _ClassVar[int]
    VIEW_ID_FIELD_NUMBER: _ClassVar[int]
    SNAP_TREE_TYPE_FIELD_NUMBER: _ClassVar[int]
    BLOB_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    NODE_ID_FLOOR_FIELD_NUMBER: _ClassVar[int]
    CHECKPOINT_INFO_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_MONITOR_TASK_PATH_FIELD_NUMBER: _ClassVar[int]
    PREV_BASE_ARCHIVE_UID_FIELD_NUMBER: _ClassVar[int]
    ARCHIVAL_OBJECT_TYPE_FIELD_NUMBER: _ClassVar[int]
    ARCHIVE_VERSION_FIELD_NUMBER: _ClassVar[int]
    ROOT_INODE_ID_FIELD_NUMBER: _ClassVar[int]
    ARCHIVE_NOW_FIELD_NUMBER: _ClassVar[int]
    USE_NODE_ID_FLOOR_TO_DETERMINE_INCREMENTAL_ARCHIVES_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FEATURE_VEC_FIELD_NUMBER: _ClassVar[int]
    DIRECT_ARCHIVE_ENABLED_FIELD_NUMBER: _ClassVar[int]
    NATIVE_FORMAT_FIELD_NUMBER: _ClassVar[int]
    REPORT_MISSING_FILES_FIELD_NUMBER: _ClassVar[int]
    REPAIR_MISSING_FILES_FIELD_NUMBER: _ClassVar[int]
    APP_JOB_NAME_FIELD_NUMBER: _ClassVar[int]
    ENTITY_NAME_FIELD_NUMBER: _ClassVar[int]
    archive_uid: _universal_id_pb2.UniversalIdProto
    base_archive_uid: _universal_id_pb2.UniversalIdProto
    task_id: int
    job_params: _rpc_service_pb2.ArchivalJobParams
    view_id: int
    snap_tree_type: ArchiveSnapTreesArg.SnapTreeType
    blob_info_vec: _containers.RepeatedCompositeFieldContainer[_icebox_pb2.BlobInfo]
    node_id_floor: int
    checkpoint_info: _icebox_pb2.TaskCheckpointInfo
    progress_monitor_task_path: str
    prev_base_archive_uid: _universal_id_pb2.UniversalIdProto
    archival_object_type: _icebox_pb2.ArchivalObjectMetadataProto.ObjectType
    archive_version: int
    root_inode_id: int
    archive_now: bool
    use_node_id_floor_to_determine_incremental_archives: bool
    enabled_feature_vec: _containers.RepeatedScalarFieldContainer[int]
    direct_archive_enabled: bool
    native_format: bool
    report_missing_files: bool
    repair_missing_files: bool
    app_job_name: str
    entity_name: str
    def __init__(self, archive_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., base_archive_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., task_id: _Optional[int] = ..., job_params: _Optional[_Union[_rpc_service_pb2.ArchivalJobParams, _Mapping]] = ..., view_id: _Optional[int] = ..., snap_tree_type: _Optional[_Union[ArchiveSnapTreesArg.SnapTreeType, str]] = ..., blob_info_vec: _Optional[_Iterable[_Union[_icebox_pb2.BlobInfo, _Mapping]]] = ..., node_id_floor: _Optional[int] = ..., checkpoint_info: _Optional[_Union[_icebox_pb2.TaskCheckpointInfo, _Mapping]] = ..., progress_monitor_task_path: _Optional[str] = ..., prev_base_archive_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., archival_object_type: _Optional[_Union[_icebox_pb2.ArchivalObjectMetadataProto.ObjectType, str]] = ..., archive_version: _Optional[int] = ..., root_inode_id: _Optional[int] = ..., archive_now: bool = ..., use_node_id_floor_to_determine_incremental_archives: bool = ..., enabled_feature_vec: _Optional[_Iterable[int]] = ..., direct_archive_enabled: bool = ..., native_format: bool = ..., report_missing_files: bool = ..., repair_missing_files: bool = ..., app_job_name: _Optional[str] = ..., entity_name: _Optional[str] = ...) -> None: ...

class ArchiveSnapTreesResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class FinalizeArchiveObjectsArg(_message.Message):
    __slots__ = ("archive_uid", "task_id", "vault_id", "abort_objects", "object_data_vec", "checkpoint_info")
    ARCHIVE_UID_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    VAULT_ID_FIELD_NUMBER: _ClassVar[int]
    ABORT_OBJECTS_FIELD_NUMBER: _ClassVar[int]
    OBJECT_DATA_VEC_FIELD_NUMBER: _ClassVar[int]
    CHECKPOINT_INFO_FIELD_NUMBER: _ClassVar[int]
    archive_uid: _universal_id_pb2.UniversalIdProto
    task_id: int
    vault_id: int
    abort_objects: bool
    object_data_vec: _containers.RepeatedCompositeFieldContainer[_icebox_pb2.TaskCheckpointInfo.ObjectData]
    checkpoint_info: _icebox_pb2.TaskCheckpointInfo
    def __init__(self, archive_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., task_id: _Optional[int] = ..., vault_id: _Optional[int] = ..., abort_objects: bool = ..., object_data_vec: _Optional[_Iterable[_Union[_icebox_pb2.TaskCheckpointInfo.ObjectData, _Mapping]]] = ..., checkpoint_info: _Optional[_Union[_icebox_pb2.TaskCheckpointInfo, _Mapping]] = ...) -> None: ...

class FinalizeArchiveObjectsResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ArchiveMetadataArg(_message.Message):
    __slots__ = ("archive_uid", "task_id", "job_params", "archive_metadata", "checkpoint_info", "archival_object_type", "archive_version", "enabled_feature_vec")
    ARCHIVE_UID_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    JOB_PARAMS_FIELD_NUMBER: _ClassVar[int]
    ARCHIVE_METADATA_FIELD_NUMBER: _ClassVar[int]
    CHECKPOINT_INFO_FIELD_NUMBER: _ClassVar[int]
    ARCHIVAL_OBJECT_TYPE_FIELD_NUMBER: _ClassVar[int]
    ARCHIVE_VERSION_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FEATURE_VEC_FIELD_NUMBER: _ClassVar[int]
    archive_uid: _universal_id_pb2.UniversalIdProto
    task_id: int
    job_params: _rpc_service_pb2.ArchivalJobParams
    archive_metadata: _icebox_pb2.ArchiveMetadataProto
    checkpoint_info: _icebox_pb2.TaskCheckpointInfo
    archival_object_type: _icebox_pb2.ArchivalObjectMetadataProto.ObjectType
    archive_version: int
    enabled_feature_vec: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, archive_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., task_id: _Optional[int] = ..., job_params: _Optional[_Union[_rpc_service_pb2.ArchivalJobParams, _Mapping]] = ..., archive_metadata: _Optional[_Union[_icebox_pb2.ArchiveMetadataProto, _Mapping]] = ..., checkpoint_info: _Optional[_Union[_icebox_pb2.TaskCheckpointInfo, _Mapping]] = ..., archival_object_type: _Optional[_Union[_icebox_pb2.ArchivalObjectMetadataProto.ObjectType, str]] = ..., archive_version: _Optional[int] = ..., enabled_feature_vec: _Optional[_Iterable[int]] = ...) -> None: ...

class ArchiveMetadataResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ArchiveMetadataToCloudDomainArg(_message.Message):
    __slots__ = ("archive_uid", "task_id", "cloud_domain_id", "archive_metadata", "app_job_uid", "worm_params")
    ARCHIVE_UID_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    CLOUD_DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    ARCHIVE_METADATA_FIELD_NUMBER: _ClassVar[int]
    APP_JOB_UID_FIELD_NUMBER: _ClassVar[int]
    WORM_PARAMS_FIELD_NUMBER: _ClassVar[int]
    archive_uid: _universal_id_pb2.UniversalIdProto
    task_id: int
    cloud_domain_id: int
    archive_metadata: _icebox_pb2.ArchiveMetadataProto
    app_job_uid: _universal_id_pb2.UniversalIdProto
    worm_params: _worm_pb2.WORMParams
    def __init__(self, archive_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., task_id: _Optional[int] = ..., cloud_domain_id: _Optional[int] = ..., archive_metadata: _Optional[_Union[_icebox_pb2.ArchiveMetadataProto, _Mapping]] = ..., app_job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., worm_params: _Optional[_Union[_worm_pb2.WORMParams, _Mapping]] = ...) -> None: ...

class ArchiveMetadataToCloudDomainResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ScheduleRestoreTaskArg(_message.Message):
    __slots__ = ("archive_uid", "vault_id", "restore_job_uid", "viewbox_id", "target_view_name", "entity_vec", "entity_metadata_vec", "checkpoint_info", "object_metadata_vec", "root_progress_monitor_task_path", "create_target_view", "index_file_path", "index_progress_monitor_task_path", "app_job_uid")
    ARCHIVE_UID_FIELD_NUMBER: _ClassVar[int]
    VAULT_ID_FIELD_NUMBER: _ClassVar[int]
    RESTORE_JOB_UID_FIELD_NUMBER: _ClassVar[int]
    VIEWBOX_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    ENTITY_VEC_FIELD_NUMBER: _ClassVar[int]
    ENTITY_METADATA_VEC_FIELD_NUMBER: _ClassVar[int]
    CHECKPOINT_INFO_FIELD_NUMBER: _ClassVar[int]
    OBJECT_METADATA_VEC_FIELD_NUMBER: _ClassVar[int]
    ROOT_PROGRESS_MONITOR_TASK_PATH_FIELD_NUMBER: _ClassVar[int]
    CREATE_TARGET_VIEW_FIELD_NUMBER: _ClassVar[int]
    INDEX_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    INDEX_PROGRESS_MONITOR_TASK_PATH_FIELD_NUMBER: _ClassVar[int]
    APP_JOB_UID_FIELD_NUMBER: _ClassVar[int]
    archive_uid: _universal_id_pb2.UniversalIdProto
    vault_id: int
    restore_job_uid: _universal_id_pb2.UniversalIdProto
    viewbox_id: int
    target_view_name: str
    entity_vec: _containers.RepeatedCompositeFieldContainer[_rpc_service_pb2.EntityParams]
    entity_metadata_vec: _containers.RepeatedCompositeFieldContainer[_icebox_pb2.EntityMetadataProto]
    checkpoint_info: _icebox_pb2.TaskCheckpointInfo
    object_metadata_vec: _containers.RepeatedCompositeFieldContainer[_icebox_pb2.ArchiveObjectScribeMetadataProto]
    root_progress_monitor_task_path: str
    create_target_view: bool
    index_file_path: str
    index_progress_monitor_task_path: str
    app_job_uid: _universal_id_pb2.UniversalIdProto
    def __init__(self, archive_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., vault_id: _Optional[int] = ..., restore_job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., viewbox_id: _Optional[int] = ..., target_view_name: _Optional[str] = ..., entity_vec: _Optional[_Iterable[_Union[_rpc_service_pb2.EntityParams, _Mapping]]] = ..., entity_metadata_vec: _Optional[_Iterable[_Union[_icebox_pb2.EntityMetadataProto, _Mapping]]] = ..., checkpoint_info: _Optional[_Union[_icebox_pb2.TaskCheckpointInfo, _Mapping]] = ..., object_metadata_vec: _Optional[_Iterable[_Union[_icebox_pb2.ArchiveObjectScribeMetadataProto, _Mapping]]] = ..., root_progress_monitor_task_path: _Optional[str] = ..., create_target_view: bool = ..., index_file_path: _Optional[str] = ..., index_progress_monitor_task_path: _Optional[str] = ..., app_job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ...) -> None: ...

class ScheduleRestoreTaskResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RestoreFilesArg(_message.Message):
    __slots__ = ("archive_uid", "vault_id", "restore_job_uid", "task_id", "viewbox_id", "target_view_name", "checkpoint_info", "archive_metadata", "root_progress_monitor_task_path", "fs_entry_vec", "vault_params", "enabled_feature_vec", "restore_directory_contents", "app_job_uid", "pruned_archive_metadata")
    class FSEntry(_message.Message):
        __slots__ = ("fs_name", "src_path", "dst_path", "progress_monitor_task_path", "view_id")
        FS_NAME_FIELD_NUMBER: _ClassVar[int]
        SRC_PATH_FIELD_NUMBER: _ClassVar[int]
        DST_PATH_FIELD_NUMBER: _ClassVar[int]
        PROGRESS_MONITOR_TASK_PATH_FIELD_NUMBER: _ClassVar[int]
        VIEW_ID_FIELD_NUMBER: _ClassVar[int]
        fs_name: str
        src_path: str
        dst_path: str
        progress_monitor_task_path: str
        view_id: int
        def __init__(self, fs_name: _Optional[str] = ..., src_path: _Optional[str] = ..., dst_path: _Optional[str] = ..., progress_monitor_task_path: _Optional[str] = ..., view_id: _Optional[int] = ...) -> None: ...
    ARCHIVE_UID_FIELD_NUMBER: _ClassVar[int]
    VAULT_ID_FIELD_NUMBER: _ClassVar[int]
    RESTORE_JOB_UID_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    VIEWBOX_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    CHECKPOINT_INFO_FIELD_NUMBER: _ClassVar[int]
    ARCHIVE_METADATA_FIELD_NUMBER: _ClassVar[int]
    ROOT_PROGRESS_MONITOR_TASK_PATH_FIELD_NUMBER: _ClassVar[int]
    FS_ENTRY_VEC_FIELD_NUMBER: _ClassVar[int]
    VAULT_PARAMS_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FEATURE_VEC_FIELD_NUMBER: _ClassVar[int]
    RESTORE_DIRECTORY_CONTENTS_FIELD_NUMBER: _ClassVar[int]
    APP_JOB_UID_FIELD_NUMBER: _ClassVar[int]
    PRUNED_ARCHIVE_METADATA_FIELD_NUMBER: _ClassVar[int]
    archive_uid: _universal_id_pb2.UniversalIdProto
    vault_id: int
    restore_job_uid: _universal_id_pb2.UniversalIdProto
    task_id: int
    viewbox_id: int
    target_view_name: str
    checkpoint_info: _icebox_pb2.TaskCheckpointInfo
    archive_metadata: _icebox_pb2.ArchiveMetadataProto
    root_progress_monitor_task_path: str
    fs_entry_vec: _containers.RepeatedCompositeFieldContainer[RestoreFilesArg.FSEntry]
    vault_params: _vault_pb2.VaultParams
    enabled_feature_vec: _containers.RepeatedScalarFieldContainer[int]
    restore_directory_contents: bool
    app_job_uid: _universal_id_pb2.UniversalIdProto
    pruned_archive_metadata: _icebox_pb2.ArchiveMetadataProto
    def __init__(self, archive_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., vault_id: _Optional[int] = ..., restore_job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., task_id: _Optional[int] = ..., viewbox_id: _Optional[int] = ..., target_view_name: _Optional[str] = ..., checkpoint_info: _Optional[_Union[_icebox_pb2.TaskCheckpointInfo, _Mapping]] = ..., archive_metadata: _Optional[_Union[_icebox_pb2.ArchiveMetadataProto, _Mapping]] = ..., root_progress_monitor_task_path: _Optional[str] = ..., fs_entry_vec: _Optional[_Iterable[_Union[RestoreFilesArg.FSEntry, _Mapping]]] = ..., vault_params: _Optional[_Union[_vault_pb2.VaultParams, _Mapping]] = ..., enabled_feature_vec: _Optional[_Iterable[int]] = ..., restore_directory_contents: bool = ..., app_job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., pruned_archive_metadata: _Optional[_Union[_icebox_pb2.ArchiveMetadataProto, _Mapping]] = ...) -> None: ...

class RestoreFilesResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CancelArchivalTaskArg(_message.Message):
    __slots__ = ("archive_uid", "task_id")
    ARCHIVE_UID_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    archive_uid: _universal_id_pb2.UniversalIdProto
    task_id: int
    def __init__(self, archive_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., task_id: _Optional[int] = ...) -> None: ...

class CancelArchivalTaskResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class CancelRestoreTaskArg(_message.Message):
    __slots__ = ("restore_job_uid", "task_id")
    RESTORE_JOB_UID_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    restore_job_uid: _universal_id_pb2.UniversalIdProto
    task_id: int
    def __init__(self, restore_job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., task_id: _Optional[int] = ...) -> None: ...

class CancelRestoreTaskResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class CancelTaskArg(_message.Message):
    __slots__ = ("job_uid", "task_id")
    JOB_UID_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    job_uid: _universal_id_pb2.UniversalIdProto
    task_id: int
    def __init__(self, job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., task_id: _Optional[int] = ...) -> None: ...

class CancelTaskResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SetWORMObjectRetentionArg(_message.Message):
    __slots__ = ("job_uid", "task_id", "data_lock_timestamp_usecs", "vault_id", "object_metadata_vec", "object_uid_vec", "task_expiry_timestamp_usecs")
    JOB_UID_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    DATA_LOCK_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
    VAULT_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_METADATA_VEC_FIELD_NUMBER: _ClassVar[int]
    OBJECT_UID_VEC_FIELD_NUMBER: _ClassVar[int]
    TASK_EXPIRY_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
    job_uid: _universal_id_pb2.UniversalIdProto
    task_id: int
    data_lock_timestamp_usecs: int
    vault_id: int
    object_metadata_vec: _containers.RepeatedCompositeFieldContainer[_icebox_pb2.ArchiveObjectScribeMetadataProto]
    object_uid_vec: _containers.RepeatedCompositeFieldContainer[_universal_id_pb2.UniversalIdProto]
    task_expiry_timestamp_usecs: int
    def __init__(self, job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., task_id: _Optional[int] = ..., data_lock_timestamp_usecs: _Optional[int] = ..., vault_id: _Optional[int] = ..., object_metadata_vec: _Optional[_Iterable[_Union[_icebox_pb2.ArchiveObjectScribeMetadataProto, _Mapping]]] = ..., object_uid_vec: _Optional[_Iterable[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]]] = ..., task_expiry_timestamp_usecs: _Optional[int] = ...) -> None: ...

class SetWORMObjectRetentionResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class ListObjectsArg(_message.Message):
    __slots__ = ("job_uid", "task_id", "vault_id", "search_params", "max_objects", "cookie", "list_metadata_objects_only", "prefix", "checkpoint_info")
    JOB_UID_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    VAULT_ID_FIELD_NUMBER: _ClassVar[int]
    SEARCH_PARAMS_FIELD_NUMBER: _ClassVar[int]
    MAX_OBJECTS_FIELD_NUMBER: _ClassVar[int]
    COOKIE_FIELD_NUMBER: _ClassVar[int]
    LIST_METADATA_OBJECTS_ONLY_FIELD_NUMBER: _ClassVar[int]
    PREFIX_FIELD_NUMBER: _ClassVar[int]
    CHECKPOINT_INFO_FIELD_NUMBER: _ClassVar[int]
    job_uid: _universal_id_pb2.UniversalIdProto
    task_id: int
    vault_id: int
    search_params: _icebox_pb2.VaultSearchParams
    max_objects: int
    cookie: str
    list_metadata_objects_only: bool
    prefix: str
    checkpoint_info: _icebox_pb2.TaskCheckpointInfo
    def __init__(self, job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., task_id: _Optional[int] = ..., vault_id: _Optional[int] = ..., search_params: _Optional[_Union[_icebox_pb2.VaultSearchParams, _Mapping]] = ..., max_objects: _Optional[int] = ..., cookie: _Optional[str] = ..., list_metadata_objects_only: bool = ..., prefix: _Optional[str] = ..., checkpoint_info: _Optional[_Union[_icebox_pb2.TaskCheckpointInfo, _Mapping]] = ...) -> None: ...

class ListObjectsResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListCloudDomainsArg(_message.Message):
    __slots__ = ("job_uid", "task_id", "vault_id", "cookie", "checkpoint_info")
    JOB_UID_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    VAULT_ID_FIELD_NUMBER: _ClassVar[int]
    COOKIE_FIELD_NUMBER: _ClassVar[int]
    CHECKPOINT_INFO_FIELD_NUMBER: _ClassVar[int]
    job_uid: _universal_id_pb2.UniversalIdProto
    task_id: int
    vault_id: int
    cookie: str
    checkpoint_info: _icebox_pb2.TaskCheckpointInfo
    def __init__(self, job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., task_id: _Optional[int] = ..., vault_id: _Optional[int] = ..., cookie: _Optional[str] = ..., checkpoint_info: _Optional[_Union[_icebox_pb2.TaskCheckpointInfo, _Mapping]] = ...) -> None: ...

class ListCloudDomainsResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class FindAccessibleCloudDomainsArg(_message.Message):
    __slots__ = ("job_uid", "task_id", "vault_id", "object_vec", "checkpoint_info")
    JOB_UID_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    VAULT_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_VEC_FIELD_NUMBER: _ClassVar[int]
    CHECKPOINT_INFO_FIELD_NUMBER: _ClassVar[int]
    job_uid: _universal_id_pb2.UniversalIdProto
    task_id: int
    vault_id: int
    object_vec: _containers.RepeatedScalarFieldContainer[str]
    checkpoint_info: _icebox_pb2.TaskCheckpointInfo
    def __init__(self, job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., task_id: _Optional[int] = ..., vault_id: _Optional[int] = ..., object_vec: _Optional[_Iterable[str]] = ..., checkpoint_info: _Optional[_Union[_icebox_pb2.TaskCheckpointInfo, _Mapping]] = ...) -> None: ...

class FindAccessibleCloudDomainsResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListArchiveMetadataObjectsArg(_message.Message):
    __slots__ = ("job_uid", "task_id", "vault_id", "domain_prefix", "search_params", "max_objects", "cookie", "checkpoint_info")
    JOB_UID_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    VAULT_ID_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_PREFIX_FIELD_NUMBER: _ClassVar[int]
    SEARCH_PARAMS_FIELD_NUMBER: _ClassVar[int]
    MAX_OBJECTS_FIELD_NUMBER: _ClassVar[int]
    COOKIE_FIELD_NUMBER: _ClassVar[int]
    CHECKPOINT_INFO_FIELD_NUMBER: _ClassVar[int]
    job_uid: _universal_id_pb2.UniversalIdProto
    task_id: int
    vault_id: int
    domain_prefix: str
    search_params: _icebox_pb2.VaultSearchParams
    max_objects: int
    cookie: str
    checkpoint_info: _icebox_pb2.TaskCheckpointInfo
    def __init__(self, job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., task_id: _Optional[int] = ..., vault_id: _Optional[int] = ..., domain_prefix: _Optional[str] = ..., search_params: _Optional[_Union[_icebox_pb2.VaultSearchParams, _Mapping]] = ..., max_objects: _Optional[int] = ..., cookie: _Optional[str] = ..., checkpoint_info: _Optional[_Union[_icebox_pb2.TaskCheckpointInfo, _Mapping]] = ...) -> None: ...

class ListArchiveMetadataObjectsResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ReadArchiveMetadataFromCSRArg(_message.Message):
    __slots__ = ("job_uid", "task_id", "cloud_domain_id", "domain_prefix", "is_vault_encryption", "use_uploaded_key", "dek_uid", "object_info_vec", "search_params", "checkpoint_info")
    JOB_UID_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    CLOUD_DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_PREFIX_FIELD_NUMBER: _ClassVar[int]
    IS_VAULT_ENCRYPTION_FIELD_NUMBER: _ClassVar[int]
    USE_UPLOADED_KEY_FIELD_NUMBER: _ClassVar[int]
    DEK_UID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    SEARCH_PARAMS_FIELD_NUMBER: _ClassVar[int]
    CHECKPOINT_INFO_FIELD_NUMBER: _ClassVar[int]
    job_uid: _universal_id_pb2.UniversalIdProto
    task_id: int
    cloud_domain_id: int
    domain_prefix: str
    is_vault_encryption: bool
    use_uploaded_key: bool
    dek_uid: _universal_id_pb2.UniversalIdProto
    object_info_vec: _containers.RepeatedCompositeFieldContainer[_icebox_pb2.ObjectInfoProto]
    search_params: _icebox_pb2.VaultSearchParams
    checkpoint_info: _icebox_pb2.TaskCheckpointInfo
    def __init__(self, job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., task_id: _Optional[int] = ..., cloud_domain_id: _Optional[int] = ..., domain_prefix: _Optional[str] = ..., is_vault_encryption: bool = ..., use_uploaded_key: bool = ..., dek_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., object_info_vec: _Optional[_Iterable[_Union[_icebox_pb2.ObjectInfoProto, _Mapping]]] = ..., search_params: _Optional[_Union[_icebox_pb2.VaultSearchParams, _Mapping]] = ..., checkpoint_info: _Optional[_Union[_icebox_pb2.TaskCheckpointInfo, _Mapping]] = ...) -> None: ...

class ReadArchiveMetadataFromCSRResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ReadMetadataArg(_message.Message):
    __slots__ = ("job_uid", "task_id", "vault_id", "read_object_metadata_only", "object_info_vec", "checkpoint_info")
    JOB_UID_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    VAULT_ID_FIELD_NUMBER: _ClassVar[int]
    READ_OBJECT_METADATA_ONLY_FIELD_NUMBER: _ClassVar[int]
    OBJECT_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    CHECKPOINT_INFO_FIELD_NUMBER: _ClassVar[int]
    job_uid: _universal_id_pb2.UniversalIdProto
    task_id: int
    vault_id: int
    read_object_metadata_only: bool
    object_info_vec: _containers.RepeatedCompositeFieldContainer[_icebox_pb2.ObjectInfoProto]
    checkpoint_info: _icebox_pb2.TaskCheckpointInfo
    def __init__(self, job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., task_id: _Optional[int] = ..., vault_id: _Optional[int] = ..., read_object_metadata_only: bool = ..., object_info_vec: _Optional[_Iterable[_Union[_icebox_pb2.ObjectInfoProto, _Mapping]]] = ..., checkpoint_info: _Optional[_Union[_icebox_pb2.TaskCheckpointInfo, _Mapping]] = ...) -> None: ...

class ReadMetadataResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class IndexEntityInfo(_message.Message):
    __slots__ = ("magneto_object_id", "magneto_instance_id")
    MAGNETO_OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    MAGNETO_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    magneto_object_id: _magneto_pb2.MagnetoObjectId
    magneto_instance_id: _yoda_types_pb2.MagnetoInstanceId
    def __init__(self, magneto_object_id: _Optional[_Union[_magneto_pb2.MagnetoObjectId, _Mapping]] = ..., magneto_instance_id: _Optional[_Union[_yoda_types_pb2.MagnetoInstanceId, _Mapping]] = ...) -> None: ...

class CreateIndexFilesArg(_message.Message):
    __slots__ = ("archive_uid", "task_id", "viewbox_id", "view_id", "job_params", "checkpoint_info", "entity_id", "entity_info_map")
    class EntityInfoMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: IndexEntityInfo
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[IndexEntityInfo, _Mapping]] = ...) -> None: ...
    ARCHIVE_UID_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    VIEWBOX_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_ID_FIELD_NUMBER: _ClassVar[int]
    JOB_PARAMS_FIELD_NUMBER: _ClassVar[int]
    CHECKPOINT_INFO_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    ENTITY_INFO_MAP_FIELD_NUMBER: _ClassVar[int]
    archive_uid: _universal_id_pb2.UniversalIdProto
    task_id: int
    viewbox_id: int
    view_id: int
    job_params: _rpc_service_pb2.ArchivalJobParams
    checkpoint_info: _icebox_pb2.TaskCheckpointInfo
    entity_id: int
    entity_info_map: _containers.MessageMap[int, IndexEntityInfo]
    def __init__(self, archive_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., task_id: _Optional[int] = ..., viewbox_id: _Optional[int] = ..., view_id: _Optional[int] = ..., job_params: _Optional[_Union[_rpc_service_pb2.ArchivalJobParams, _Mapping]] = ..., checkpoint_info: _Optional[_Union[_icebox_pb2.TaskCheckpointInfo, _Mapping]] = ..., entity_id: _Optional[int] = ..., entity_info_map: _Optional[_Mapping[int, IndexEntityInfo]] = ...) -> None: ...

class CreateIndexFilesResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class BuildFileIndexArg(_message.Message):
    __slots__ = ("job_uid", "task_id", "archive_uid", "viewbox_id", "view_name", "fs_name", "index_dir_path", "checkpoint_info", "entity_id")
    JOB_UID_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    ARCHIVE_UID_FIELD_NUMBER: _ClassVar[int]
    VIEWBOX_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    FS_NAME_FIELD_NUMBER: _ClassVar[int]
    INDEX_DIR_PATH_FIELD_NUMBER: _ClassVar[int]
    CHECKPOINT_INFO_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    job_uid: _universal_id_pb2.UniversalIdProto
    task_id: int
    archive_uid: _universal_id_pb2.UniversalIdProto
    viewbox_id: int
    view_name: str
    fs_name: str
    index_dir_path: str
    checkpoint_info: _icebox_pb2.TaskCheckpointInfo
    entity_id: int
    def __init__(self, job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., task_id: _Optional[int] = ..., archive_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., viewbox_id: _Optional[int] = ..., view_name: _Optional[str] = ..., fs_name: _Optional[str] = ..., index_dir_path: _Optional[str] = ..., checkpoint_info: _Optional[_Union[_icebox_pb2.TaskCheckpointInfo, _Mapping]] = ..., entity_id: _Optional[int] = ...) -> None: ...

class BuildFileIndexResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CreateStubEntityViewArg(_message.Message):
    __slots__ = ("job_uid", "task_id", "archive_uid", "entity_id", "vault_id", "viewbox_id", "archive_job_type", "checkpoint_info", "vault_params", "enabled_feature_vec", "reuse_existing_stub_view", "is_download_index_job")
    JOB_UID_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    ARCHIVE_UID_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    VAULT_ID_FIELD_NUMBER: _ClassVar[int]
    VIEWBOX_ID_FIELD_NUMBER: _ClassVar[int]
    ARCHIVE_JOB_TYPE_FIELD_NUMBER: _ClassVar[int]
    CHECKPOINT_INFO_FIELD_NUMBER: _ClassVar[int]
    VAULT_PARAMS_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FEATURE_VEC_FIELD_NUMBER: _ClassVar[int]
    REUSE_EXISTING_STUB_VIEW_FIELD_NUMBER: _ClassVar[int]
    IS_DOWNLOAD_INDEX_JOB_FIELD_NUMBER: _ClassVar[int]
    job_uid: _universal_id_pb2.UniversalIdProto
    task_id: int
    archive_uid: _universal_id_pb2.UniversalIdProto
    entity_id: int
    vault_id: int
    viewbox_id: int
    archive_job_type: _icebox_pb2.IceboxJobType
    checkpoint_info: _icebox_pb2.TaskCheckpointInfo
    vault_params: _vault_pb2.VaultParams
    enabled_feature_vec: _containers.RepeatedScalarFieldContainer[int]
    reuse_existing_stub_view: bool
    is_download_index_job: bool
    def __init__(self, job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., task_id: _Optional[int] = ..., archive_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., entity_id: _Optional[int] = ..., vault_id: _Optional[int] = ..., viewbox_id: _Optional[int] = ..., archive_job_type: _Optional[_Union[_icebox_pb2.IceboxJobType, str]] = ..., checkpoint_info: _Optional[_Union[_icebox_pb2.TaskCheckpointInfo, _Mapping]] = ..., vault_params: _Optional[_Union[_vault_pb2.VaultParams, _Mapping]] = ..., enabled_feature_vec: _Optional[_Iterable[int]] = ..., reuse_existing_stub_view: bool = ..., is_download_index_job: bool = ...) -> None: ...

class CreateStubEntityViewResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PrefetchFilesArg(_message.Message):
    __slots__ = ("job_uid", "task_id", "archive_uid", "entity_id", "vault_id", "viewbox_id", "stub_view_info", "file_restore_info", "progress_monitor_task_path", "checkpoint_info", "prefetch_file_path_vec")
    JOB_UID_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    ARCHIVE_UID_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    VAULT_ID_FIELD_NUMBER: _ClassVar[int]
    VIEWBOX_ID_FIELD_NUMBER: _ClassVar[int]
    STUB_VIEW_INFO_FIELD_NUMBER: _ClassVar[int]
    FILE_RESTORE_INFO_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_MONITOR_TASK_PATH_FIELD_NUMBER: _ClassVar[int]
    CHECKPOINT_INFO_FIELD_NUMBER: _ClassVar[int]
    PREFETCH_FILE_PATH_VEC_FIELD_NUMBER: _ClassVar[int]
    job_uid: _universal_id_pb2.UniversalIdProto
    task_id: int
    archive_uid: _universal_id_pb2.UniversalIdProto
    entity_id: int
    vault_id: int
    viewbox_id: int
    stub_view_info: _icebox_pb2.StubViewInfo
    file_restore_info: _rpc_service_pb2.ScheduleRestoreJobArg.FileRestoreInfo
    progress_monitor_task_path: str
    checkpoint_info: _icebox_pb2.TaskCheckpointInfo
    prefetch_file_path_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., task_id: _Optional[int] = ..., archive_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., entity_id: _Optional[int] = ..., vault_id: _Optional[int] = ..., viewbox_id: _Optional[int] = ..., stub_view_info: _Optional[_Union[_icebox_pb2.StubViewInfo, _Mapping]] = ..., file_restore_info: _Optional[_Union[_rpc_service_pb2.ScheduleRestoreJobArg.FileRestoreInfo, _Mapping]] = ..., progress_monitor_task_path: _Optional[str] = ..., checkpoint_info: _Optional[_Union[_icebox_pb2.TaskCheckpointInfo, _Mapping]] = ..., prefetch_file_path_vec: _Optional[_Iterable[str]] = ...) -> None: ...

class PrefetchFilesResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PrefetchSnapTreeNodesArg(_message.Message):
    __slots__ = ("job_uid", "task_id", "archive_uid", "entity_id", "vault_id", "viewbox_id", "stub_view_info", "file_restore_info", "snap_tree_id", "snap_tree_min_key_id", "snap_tree_max_key_id", "is_view_snap_tree", "blob_data_ranges", "progress_monitor_task_path", "checkpoint_info", "enabled_feature_vec")
    JOB_UID_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    ARCHIVE_UID_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    VAULT_ID_FIELD_NUMBER: _ClassVar[int]
    VIEWBOX_ID_FIELD_NUMBER: _ClassVar[int]
    STUB_VIEW_INFO_FIELD_NUMBER: _ClassVar[int]
    FILE_RESTORE_INFO_FIELD_NUMBER: _ClassVar[int]
    SNAP_TREE_ID_FIELD_NUMBER: _ClassVar[int]
    SNAP_TREE_MIN_KEY_ID_FIELD_NUMBER: _ClassVar[int]
    SNAP_TREE_MAX_KEY_ID_FIELD_NUMBER: _ClassVar[int]
    IS_VIEW_SNAP_TREE_FIELD_NUMBER: _ClassVar[int]
    BLOB_DATA_RANGES_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_MONITOR_TASK_PATH_FIELD_NUMBER: _ClassVar[int]
    CHECKPOINT_INFO_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FEATURE_VEC_FIELD_NUMBER: _ClassVar[int]
    job_uid: _universal_id_pb2.UniversalIdProto
    task_id: int
    archive_uid: _universal_id_pb2.UniversalIdProto
    entity_id: int
    vault_id: int
    viewbox_id: int
    stub_view_info: _icebox_pb2.StubViewInfo
    file_restore_info: _rpc_service_pb2.ScheduleRestoreJobArg.FileRestoreInfo
    snap_tree_id: int
    snap_tree_min_key_id: int
    snap_tree_max_key_id: int
    is_view_snap_tree: bool
    blob_data_ranges: _icebox_pb2.BlobDataRanges
    progress_monitor_task_path: str
    checkpoint_info: _icebox_pb2.TaskCheckpointInfo
    enabled_feature_vec: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., task_id: _Optional[int] = ..., archive_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., entity_id: _Optional[int] = ..., vault_id: _Optional[int] = ..., viewbox_id: _Optional[int] = ..., stub_view_info: _Optional[_Union[_icebox_pb2.StubViewInfo, _Mapping]] = ..., file_restore_info: _Optional[_Union[_rpc_service_pb2.ScheduleRestoreJobArg.FileRestoreInfo, _Mapping]] = ..., snap_tree_id: _Optional[int] = ..., snap_tree_min_key_id: _Optional[int] = ..., snap_tree_max_key_id: _Optional[int] = ..., is_view_snap_tree: bool = ..., blob_data_ranges: _Optional[_Union[_icebox_pb2.BlobDataRanges, _Mapping]] = ..., progress_monitor_task_path: _Optional[str] = ..., checkpoint_info: _Optional[_Union[_icebox_pb2.TaskCheckpointInfo, _Mapping]] = ..., enabled_feature_vec: _Optional[_Iterable[int]] = ...) -> None: ...

class PrefetchSnapTreeNodesResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RestoreStubSnapTreesArg(_message.Message):
    __slots__ = ("job_uid", "task_id", "archive_uid", "cloud_domain_id", "stub_snap_tree_info_vec", "checkpoint_info", "app_job_uid", "viewbox_id", "is_domain_migration_job")
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
    JOB_UID_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    ARCHIVE_UID_FIELD_NUMBER: _ClassVar[int]
    CLOUD_DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    STUB_SNAP_TREE_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    CHECKPOINT_INFO_FIELD_NUMBER: _ClassVar[int]
    APP_JOB_UID_FIELD_NUMBER: _ClassVar[int]
    VIEWBOX_ID_FIELD_NUMBER: _ClassVar[int]
    IS_DOMAIN_MIGRATION_JOB_FIELD_NUMBER: _ClassVar[int]
    job_uid: _universal_id_pb2.UniversalIdProto
    task_id: int
    archive_uid: _universal_id_pb2.UniversalIdProto
    cloud_domain_id: int
    stub_snap_tree_info_vec: _containers.RepeatedCompositeFieldContainer[RestoreStubSnapTreesArg.StubSnapTreeInfo]
    checkpoint_info: _icebox_pb2.TaskCheckpointInfo
    app_job_uid: _universal_id_pb2.UniversalIdProto
    viewbox_id: int
    is_domain_migration_job: bool
    def __init__(self, job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., task_id: _Optional[int] = ..., archive_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., cloud_domain_id: _Optional[int] = ..., stub_snap_tree_info_vec: _Optional[_Iterable[_Union[RestoreStubSnapTreesArg.StubSnapTreeInfo, _Mapping]]] = ..., checkpoint_info: _Optional[_Union[_icebox_pb2.TaskCheckpointInfo, _Mapping]] = ..., app_job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., viewbox_id: _Optional[int] = ..., is_domain_migration_job: bool = ...) -> None: ...

class RestoreStubSnapTreesResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class FixViewSnapTreeUpdateIntentsArg(_message.Message):
    __slots__ = ("archive_uid", "task_id", "view_id", "tree_uid", "root_inode_id", "min_key", "max_key", "checkpoint_info", "base_archive_uid", "node_id_floor", "use_node_id_floor_to_determine_incremental_archives")
    ARCHIVE_UID_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_ID_FIELD_NUMBER: _ClassVar[int]
    TREE_UID_FIELD_NUMBER: _ClassVar[int]
    ROOT_INODE_ID_FIELD_NUMBER: _ClassVar[int]
    MIN_KEY_FIELD_NUMBER: _ClassVar[int]
    MAX_KEY_FIELD_NUMBER: _ClassVar[int]
    CHECKPOINT_INFO_FIELD_NUMBER: _ClassVar[int]
    BASE_ARCHIVE_UID_FIELD_NUMBER: _ClassVar[int]
    NODE_ID_FLOOR_FIELD_NUMBER: _ClassVar[int]
    USE_NODE_ID_FLOOR_TO_DETERMINE_INCREMENTAL_ARCHIVES_FIELD_NUMBER: _ClassVar[int]
    archive_uid: _universal_id_pb2.UniversalIdProto
    task_id: int
    view_id: int
    tree_uid: _universal_id_pb2.UniversalIdProto
    root_inode_id: int
    min_key: int
    max_key: int
    checkpoint_info: _icebox_pb2.TaskCheckpointInfo
    base_archive_uid: _universal_id_pb2.UniversalIdProto
    node_id_floor: int
    use_node_id_floor_to_determine_incremental_archives: bool
    def __init__(self, archive_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., task_id: _Optional[int] = ..., view_id: _Optional[int] = ..., tree_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., root_inode_id: _Optional[int] = ..., min_key: _Optional[int] = ..., max_key: _Optional[int] = ..., checkpoint_info: _Optional[_Union[_icebox_pb2.TaskCheckpointInfo, _Mapping]] = ..., base_archive_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., node_id_floor: _Optional[int] = ..., use_node_id_floor_to_determine_incremental_archives: bool = ...) -> None: ...

class FixViewSnapTreeUpdateIntentsResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class FixSnapTreesUpdateIntentsArg(_message.Message):
    __slots__ = ("archive_uid", "task_id", "cloud_domain_id", "tree_info_vec", "checkpoint_info", "skip_progress_reporting", "max_sub_trees_in_parallel", "acquire_pins_and_locks", "is_cohesion_copy_job")
    class ViewSnapTreeInfo(_message.Message):
        __slots__ = ("tree_id", "root_inode_id", "view_id", "is_s3_view_snap_tree")
        TREE_ID_FIELD_NUMBER: _ClassVar[int]
        ROOT_INODE_ID_FIELD_NUMBER: _ClassVar[int]
        VIEW_ID_FIELD_NUMBER: _ClassVar[int]
        IS_S3_VIEW_SNAP_TREE_FIELD_NUMBER: _ClassVar[int]
        tree_id: int
        root_inode_id: int
        view_id: int
        is_s3_view_snap_tree: bool
        def __init__(self, tree_id: _Optional[int] = ..., root_inode_id: _Optional[int] = ..., view_id: _Optional[int] = ..., is_s3_view_snap_tree: bool = ...) -> None: ...
    ARCHIVE_UID_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    CLOUD_DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    TREE_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    CHECKPOINT_INFO_FIELD_NUMBER: _ClassVar[int]
    SKIP_PROGRESS_REPORTING_FIELD_NUMBER: _ClassVar[int]
    MAX_SUB_TREES_IN_PARALLEL_FIELD_NUMBER: _ClassVar[int]
    ACQUIRE_PINS_AND_LOCKS_FIELD_NUMBER: _ClassVar[int]
    IS_COHESION_COPY_JOB_FIELD_NUMBER: _ClassVar[int]
    archive_uid: _universal_id_pb2.UniversalIdProto
    task_id: int
    cloud_domain_id: int
    tree_info_vec: _containers.RepeatedCompositeFieldContainer[FixSnapTreesUpdateIntentsArg.ViewSnapTreeInfo]
    checkpoint_info: _icebox_pb2.TaskCheckpointInfo
    skip_progress_reporting: bool
    max_sub_trees_in_parallel: int
    acquire_pins_and_locks: bool
    is_cohesion_copy_job: bool
    def __init__(self, archive_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., task_id: _Optional[int] = ..., cloud_domain_id: _Optional[int] = ..., tree_info_vec: _Optional[_Iterable[_Union[FixSnapTreesUpdateIntentsArg.ViewSnapTreeInfo, _Mapping]]] = ..., checkpoint_info: _Optional[_Union[_icebox_pb2.TaskCheckpointInfo, _Mapping]] = ..., skip_progress_reporting: bool = ..., max_sub_trees_in_parallel: _Optional[int] = ..., acquire_pins_and_locks: bool = ..., is_cohesion_copy_job: bool = ...) -> None: ...

class FixSnapTreesUpdateIntentsResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class FixUpdateIntentsStatsArg(_message.Message):
    __slots__ = ("archive_uid", "task_id")
    ARCHIVE_UID_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    archive_uid: _universal_id_pb2.UniversalIdProto
    task_id: int
    def __init__(self, archive_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., task_id: _Optional[int] = ...) -> None: ...

class FixUpdateIntentsStatsResult(_message.Message):
    __slots__ = ("total_num_nodes",)
    TOTAL_NUM_NODES_FIELD_NUMBER: _ClassVar[int]
    total_num_nodes: int
    def __init__(self, total_num_nodes: _Optional[int] = ...) -> None: ...

class GetFilesToUploadArg(_message.Message):
    __slots__ = ("job_uid", "task_id", "view_id", "fs_name", "root_dir", "prev_job_run_fs_checkpoint_info", "cookie", "max_files", "checkpoint_info")
    JOB_UID_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_ID_FIELD_NUMBER: _ClassVar[int]
    FS_NAME_FIELD_NUMBER: _ClassVar[int]
    ROOT_DIR_FIELD_NUMBER: _ClassVar[int]
    PREV_JOB_RUN_FS_CHECKPOINT_INFO_FIELD_NUMBER: _ClassVar[int]
    COOKIE_FIELD_NUMBER: _ClassVar[int]
    MAX_FILES_FIELD_NUMBER: _ClassVar[int]
    CHECKPOINT_INFO_FIELD_NUMBER: _ClassVar[int]
    job_uid: _universal_id_pb2.UniversalIdProto
    task_id: int
    view_id: int
    fs_name: str
    root_dir: str
    prev_job_run_fs_checkpoint_info: _icebox_pb2.FileUploadJobMetadataProto.FSCheckpointInfo
    cookie: _icebox_pb2.GetFilesToUploadCookieProto
    max_files: int
    checkpoint_info: _icebox_pb2.TaskCheckpointInfo
    def __init__(self, job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., task_id: _Optional[int] = ..., view_id: _Optional[int] = ..., fs_name: _Optional[str] = ..., root_dir: _Optional[str] = ..., prev_job_run_fs_checkpoint_info: _Optional[_Union[_icebox_pb2.FileUploadJobMetadataProto.FSCheckpointInfo, _Mapping]] = ..., cookie: _Optional[_Union[_icebox_pb2.GetFilesToUploadCookieProto, _Mapping]] = ..., max_files: _Optional[int] = ..., checkpoint_info: _Optional[_Union[_icebox_pb2.TaskCheckpointInfo, _Mapping]] = ...) -> None: ...

class GetFilesToUploadResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UploadFilesArg(_message.Message):
    __slots__ = ("job_uid", "task_id", "vault_id", "viewbox_id", "view_name", "fs_name", "file_info_vec", "checkpoint_info")
    JOB_UID_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    VAULT_ID_FIELD_NUMBER: _ClassVar[int]
    VIEWBOX_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    FS_NAME_FIELD_NUMBER: _ClassVar[int]
    FILE_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    CHECKPOINT_INFO_FIELD_NUMBER: _ClassVar[int]
    job_uid: _universal_id_pb2.UniversalIdProto
    task_id: int
    vault_id: int
    viewbox_id: int
    view_name: str
    fs_name: str
    file_info_vec: _containers.RepeatedCompositeFieldContainer[_icebox_pb2.FileInfoProto]
    checkpoint_info: _icebox_pb2.TaskCheckpointInfo
    def __init__(self, job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., task_id: _Optional[int] = ..., vault_id: _Optional[int] = ..., viewbox_id: _Optional[int] = ..., view_name: _Optional[str] = ..., fs_name: _Optional[str] = ..., file_info_vec: _Optional[_Iterable[_Union[_icebox_pb2.FileInfoProto, _Mapping]]] = ..., checkpoint_info: _Optional[_Union[_icebox_pb2.TaskCheckpointInfo, _Mapping]] = ...) -> None: ...

class UploadFilesResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class BackupQuotaSnapTreeArg(_message.Message):
    __slots__ = ("archive_uid", "task_id", "view_id", "viewbox_id", "entity_id", "checkpoint_info")
    ARCHIVE_UID_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_ID_FIELD_NUMBER: _ClassVar[int]
    VIEWBOX_ID_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    CHECKPOINT_INFO_FIELD_NUMBER: _ClassVar[int]
    archive_uid: _universal_id_pb2.UniversalIdProto
    task_id: int
    view_id: int
    viewbox_id: int
    entity_id: int
    checkpoint_info: _icebox_pb2.TaskCheckpointInfo
    def __init__(self, archive_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., task_id: _Optional[int] = ..., view_id: _Optional[int] = ..., viewbox_id: _Optional[int] = ..., entity_id: _Optional[int] = ..., checkpoint_info: _Optional[_Union[_icebox_pb2.TaskCheckpointInfo, _Mapping]] = ...) -> None: ...

class BackupQuotaSnapTreeResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CleanupPreparedRangesArg(_message.Message):
    __slots__ = ("vault_id", "object_uid_vec", "restore_job_uid", "restore_objects_manager_used")
    VAULT_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_UID_VEC_FIELD_NUMBER: _ClassVar[int]
    RESTORE_JOB_UID_FIELD_NUMBER: _ClassVar[int]
    RESTORE_OBJECTS_MANAGER_USED_FIELD_NUMBER: _ClassVar[int]
    vault_id: int
    object_uid_vec: _containers.RepeatedCompositeFieldContainer[_universal_id_pb2.UniversalIdProto]
    restore_job_uid: _universal_id_pb2.UniversalIdProto
    restore_objects_manager_used: bool
    def __init__(self, vault_id: _Optional[int] = ..., object_uid_vec: _Optional[_Iterable[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]]] = ..., restore_job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., restore_objects_manager_used: bool = ...) -> None: ...

class CleanupPreparedRangesResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PrepareArchiveObjectsArg(_message.Message):
    __slots__ = ("archive_uid", "vault_id", "restore_job_uid", "task_id", "vault_params", "enabled_feature_vec", "checkpoint_info")
    ARCHIVE_UID_FIELD_NUMBER: _ClassVar[int]
    VAULT_ID_FIELD_NUMBER: _ClassVar[int]
    RESTORE_JOB_UID_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    VAULT_PARAMS_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FEATURE_VEC_FIELD_NUMBER: _ClassVar[int]
    CHECKPOINT_INFO_FIELD_NUMBER: _ClassVar[int]
    archive_uid: _universal_id_pb2.UniversalIdProto
    vault_id: int
    restore_job_uid: _universal_id_pb2.UniversalIdProto
    task_id: int
    vault_params: _vault_pb2.VaultParams
    enabled_feature_vec: _containers.RepeatedScalarFieldContainer[int]
    checkpoint_info: _icebox_pb2.TaskCheckpointInfo
    def __init__(self, archive_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., vault_id: _Optional[int] = ..., restore_job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., task_id: _Optional[int] = ..., vault_params: _Optional[_Union[_vault_pb2.VaultParams, _Mapping]] = ..., enabled_feature_vec: _Optional[_Iterable[int]] = ..., checkpoint_info: _Optional[_Union[_icebox_pb2.TaskCheckpointInfo, _Mapping]] = ...) -> None: ...

class PrepareArchiveObjectsResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListVaultFSFilesArg(_message.Message):
    __slots__ = ("job_uid", "task_id", "vault_id", "archive_uid", "archived_view_id", "archived_view_fs_name", "archived_view_fs_path", "max_files", "cookie", "checkpoint_info", "enabled_feature_vec", "vault_params", "set_archive_object_uid", "parallel_walker_cookie", "object_files_viewbox_id", "object_files_view_name", "object_files_fs_name", "object_files_dir_path")
    JOB_UID_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    VAULT_ID_FIELD_NUMBER: _ClassVar[int]
    ARCHIVE_UID_FIELD_NUMBER: _ClassVar[int]
    ARCHIVED_VIEW_ID_FIELD_NUMBER: _ClassVar[int]
    ARCHIVED_VIEW_FS_NAME_FIELD_NUMBER: _ClassVar[int]
    ARCHIVED_VIEW_FS_PATH_FIELD_NUMBER: _ClassVar[int]
    MAX_FILES_FIELD_NUMBER: _ClassVar[int]
    COOKIE_FIELD_NUMBER: _ClassVar[int]
    CHECKPOINT_INFO_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FEATURE_VEC_FIELD_NUMBER: _ClassVar[int]
    VAULT_PARAMS_FIELD_NUMBER: _ClassVar[int]
    SET_ARCHIVE_OBJECT_UID_FIELD_NUMBER: _ClassVar[int]
    PARALLEL_WALKER_COOKIE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_FILES_VIEWBOX_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_FILES_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    OBJECT_FILES_FS_NAME_FIELD_NUMBER: _ClassVar[int]
    OBJECT_FILES_DIR_PATH_FIELD_NUMBER: _ClassVar[int]
    job_uid: _universal_id_pb2.UniversalIdProto
    task_id: int
    vault_id: int
    archive_uid: _universal_id_pb2.UniversalIdProto
    archived_view_id: int
    archived_view_fs_name: str
    archived_view_fs_path: str
    max_files: int
    cookie: str
    checkpoint_info: _icebox_pb2.TaskCheckpointInfo
    enabled_feature_vec: _containers.RepeatedScalarFieldContainer[int]
    vault_params: _vault_pb2.VaultParams
    set_archive_object_uid: bool
    parallel_walker_cookie: _icebox_pb2.VaultFSWalkerCookieProto
    object_files_viewbox_id: int
    object_files_view_name: str
    object_files_fs_name: str
    object_files_dir_path: str
    def __init__(self, job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., task_id: _Optional[int] = ..., vault_id: _Optional[int] = ..., archive_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., archived_view_id: _Optional[int] = ..., archived_view_fs_name: _Optional[str] = ..., archived_view_fs_path: _Optional[str] = ..., max_files: _Optional[int] = ..., cookie: _Optional[str] = ..., checkpoint_info: _Optional[_Union[_icebox_pb2.TaskCheckpointInfo, _Mapping]] = ..., enabled_feature_vec: _Optional[_Iterable[int]] = ..., vault_params: _Optional[_Union[_vault_pb2.VaultParams, _Mapping]] = ..., set_archive_object_uid: bool = ..., parallel_walker_cookie: _Optional[_Union[_icebox_pb2.VaultFSWalkerCookieProto, _Mapping]] = ..., object_files_viewbox_id: _Optional[int] = ..., object_files_view_name: _Optional[str] = ..., object_files_fs_name: _Optional[str] = ..., object_files_dir_path: _Optional[str] = ...) -> None: ...

class ListVaultFSFilesResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DumpVaultSnapTreeArg(_message.Message):
    __slots__ = ("vault_id", "archive_uid", "restore_job_uid", "task_id", "tree_uid", "root_node_location", "dump_file_path")
    VAULT_ID_FIELD_NUMBER: _ClassVar[int]
    ARCHIVE_UID_FIELD_NUMBER: _ClassVar[int]
    RESTORE_JOB_UID_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    TREE_UID_FIELD_NUMBER: _ClassVar[int]
    ROOT_NODE_LOCATION_FIELD_NUMBER: _ClassVar[int]
    DUMP_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    vault_id: int
    archive_uid: _universal_id_pb2.UniversalIdProto
    restore_job_uid: _universal_id_pb2.UniversalIdProto
    task_id: int
    tree_uid: _universal_id_pb2.UniversalIdProto
    root_node_location: _cloud_pb2.ArchiveSnapTreeNodePtrProto
    dump_file_path: str
    def __init__(self, vault_id: _Optional[int] = ..., archive_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., restore_job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., task_id: _Optional[int] = ..., tree_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., root_node_location: _Optional[_Union[_cloud_pb2.ArchiveSnapTreeNodePtrProto, _Mapping]] = ..., dump_file_path: _Optional[str] = ...) -> None: ...

class DumpVaultSnapTreeResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class CopyFilesArg(_message.Message):
    __slots__ = ("archive_uid", "app_job_uid", "job_run_id", "vault_id", "task_id", "viewbox_id", "full_metadata_archive_uid", "view_id", "root_inode_id", "file_inode_vec", "relative_file_path_vec", "checkpoint_info", "enabled_feature_vec", "da_internal_view_name", "da_internal_view_objects_info_dir", "unified_view_dir_path", "enable_compression", "enable_encryption", "skip_progress_and_record", "tree_id", "owner_tree_id", "node_id")
    ARCHIVE_UID_FIELD_NUMBER: _ClassVar[int]
    APP_JOB_UID_FIELD_NUMBER: _ClassVar[int]
    JOB_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    VAULT_ID_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    VIEWBOX_ID_FIELD_NUMBER: _ClassVar[int]
    FULL_METADATA_ARCHIVE_UID_FIELD_NUMBER: _ClassVar[int]
    VIEW_ID_FIELD_NUMBER: _ClassVar[int]
    ROOT_INODE_ID_FIELD_NUMBER: _ClassVar[int]
    FILE_INODE_VEC_FIELD_NUMBER: _ClassVar[int]
    RELATIVE_FILE_PATH_VEC_FIELD_NUMBER: _ClassVar[int]
    CHECKPOINT_INFO_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FEATURE_VEC_FIELD_NUMBER: _ClassVar[int]
    DA_INTERNAL_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    DA_INTERNAL_VIEW_OBJECTS_INFO_DIR_FIELD_NUMBER: _ClassVar[int]
    UNIFIED_VIEW_DIR_PATH_FIELD_NUMBER: _ClassVar[int]
    ENABLE_COMPRESSION_FIELD_NUMBER: _ClassVar[int]
    ENABLE_ENCRYPTION_FIELD_NUMBER: _ClassVar[int]
    SKIP_PROGRESS_AND_RECORD_FIELD_NUMBER: _ClassVar[int]
    TREE_ID_FIELD_NUMBER: _ClassVar[int]
    OWNER_TREE_ID_FIELD_NUMBER: _ClassVar[int]
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    archive_uid: _universal_id_pb2.UniversalIdProto
    app_job_uid: _universal_id_pb2.UniversalIdProto
    job_run_id: int
    vault_id: int
    task_id: int
    viewbox_id: int
    full_metadata_archive_uid: _universal_id_pb2.UniversalIdProto
    view_id: int
    root_inode_id: int
    file_inode_vec: _containers.RepeatedScalarFieldContainer[int]
    relative_file_path_vec: _containers.RepeatedScalarFieldContainer[str]
    checkpoint_info: _icebox_pb2.TaskCheckpointInfo
    enabled_feature_vec: _containers.RepeatedScalarFieldContainer[int]
    da_internal_view_name: str
    da_internal_view_objects_info_dir: str
    unified_view_dir_path: str
    enable_compression: bool
    enable_encryption: bool
    skip_progress_and_record: bool
    tree_id: int
    owner_tree_id: int
    node_id: int
    def __init__(self, archive_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., app_job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., job_run_id: _Optional[int] = ..., vault_id: _Optional[int] = ..., task_id: _Optional[int] = ..., viewbox_id: _Optional[int] = ..., full_metadata_archive_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., view_id: _Optional[int] = ..., root_inode_id: _Optional[int] = ..., file_inode_vec: _Optional[_Iterable[int]] = ..., relative_file_path_vec: _Optional[_Iterable[str]] = ..., checkpoint_info: _Optional[_Union[_icebox_pb2.TaskCheckpointInfo, _Mapping]] = ..., enabled_feature_vec: _Optional[_Iterable[int]] = ..., da_internal_view_name: _Optional[str] = ..., da_internal_view_objects_info_dir: _Optional[str] = ..., unified_view_dir_path: _Optional[str] = ..., enable_compression: bool = ..., enable_encryption: bool = ..., skip_progress_and_record: bool = ..., tree_id: _Optional[int] = ..., owner_tree_id: _Optional[int] = ..., node_id: _Optional[int] = ...) -> None: ...

class CopyFilesResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CleanupDirectArchiveObjectsArg(_message.Message):
    __slots__ = ("job_uid", "task_id", "vault_id", "viewbox_id", "view_name", "fs_name", "relative_dir_path", "actions_file_vec", "checkpoint_info", "is_direct_archive_gc_job", "app_job_uid")
    JOB_UID_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    VAULT_ID_FIELD_NUMBER: _ClassVar[int]
    VIEWBOX_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    FS_NAME_FIELD_NUMBER: _ClassVar[int]
    RELATIVE_DIR_PATH_FIELD_NUMBER: _ClassVar[int]
    ACTIONS_FILE_VEC_FIELD_NUMBER: _ClassVar[int]
    CHECKPOINT_INFO_FIELD_NUMBER: _ClassVar[int]
    IS_DIRECT_ARCHIVE_GC_JOB_FIELD_NUMBER: _ClassVar[int]
    APP_JOB_UID_FIELD_NUMBER: _ClassVar[int]
    job_uid: _universal_id_pb2.UniversalIdProto
    task_id: int
    vault_id: int
    viewbox_id: int
    view_name: str
    fs_name: str
    relative_dir_path: str
    actions_file_vec: _containers.RepeatedScalarFieldContainer[str]
    checkpoint_info: _icebox_pb2.TaskCheckpointInfo
    is_direct_archive_gc_job: bool
    app_job_uid: _universal_id_pb2.UniversalIdProto
    def __init__(self, job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., task_id: _Optional[int] = ..., vault_id: _Optional[int] = ..., viewbox_id: _Optional[int] = ..., view_name: _Optional[str] = ..., fs_name: _Optional[str] = ..., relative_dir_path: _Optional[str] = ..., actions_file_vec: _Optional[_Iterable[str]] = ..., checkpoint_info: _Optional[_Union[_icebox_pb2.TaskCheckpointInfo, _Mapping]] = ..., is_direct_archive_gc_job: bool = ..., app_job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ...) -> None: ...

class CleanupDirectArchiveObjectsResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DownloadSnapTreeObjectsArg(_message.Message):
    __slots__ = ("job_uid", "task_id", "vault_id", "viewbox_id", "view_name", "fs_name", "object_vec", "checkpoint_info")
    JOB_UID_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    VAULT_ID_FIELD_NUMBER: _ClassVar[int]
    VIEWBOX_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    FS_NAME_FIELD_NUMBER: _ClassVar[int]
    OBJECT_VEC_FIELD_NUMBER: _ClassVar[int]
    CHECKPOINT_INFO_FIELD_NUMBER: _ClassVar[int]
    job_uid: _universal_id_pb2.UniversalIdProto
    task_id: int
    vault_id: int
    viewbox_id: int
    view_name: str
    fs_name: str
    object_vec: _containers.RepeatedCompositeFieldContainer[_icebox_pb2.ObjectInfoProto]
    checkpoint_info: _icebox_pb2.TaskCheckpointInfo
    def __init__(self, job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., task_id: _Optional[int] = ..., vault_id: _Optional[int] = ..., viewbox_id: _Optional[int] = ..., view_name: _Optional[str] = ..., fs_name: _Optional[str] = ..., object_vec: _Optional[_Iterable[_Union[_icebox_pb2.ObjectInfoProto, _Mapping]]] = ..., checkpoint_info: _Optional[_Union[_icebox_pb2.TaskCheckpointInfo, _Mapping]] = ...) -> None: ...

class DownloadSnapTreeObjectsResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetBlobsInfoArg(_message.Message):
    __slots__ = ("task_id", "view_id", "tree_uid", "root_inode_id", "job_uid", "node_id_floor", "base_archive_uid", "parent_archive_uid_vec", "should_flush_blob_journal_data", "min_key", "max_key", "snap_tree_iter_cookie", "blob_info_cookie", "log_skipped_nodes")
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_ID_FIELD_NUMBER: _ClassVar[int]
    TREE_UID_FIELD_NUMBER: _ClassVar[int]
    ROOT_INODE_ID_FIELD_NUMBER: _ClassVar[int]
    JOB_UID_FIELD_NUMBER: _ClassVar[int]
    NODE_ID_FLOOR_FIELD_NUMBER: _ClassVar[int]
    BASE_ARCHIVE_UID_FIELD_NUMBER: _ClassVar[int]
    PARENT_ARCHIVE_UID_VEC_FIELD_NUMBER: _ClassVar[int]
    SHOULD_FLUSH_BLOB_JOURNAL_DATA_FIELD_NUMBER: _ClassVar[int]
    MIN_KEY_FIELD_NUMBER: _ClassVar[int]
    MAX_KEY_FIELD_NUMBER: _ClassVar[int]
    SNAP_TREE_ITER_COOKIE_FIELD_NUMBER: _ClassVar[int]
    BLOB_INFO_COOKIE_FIELD_NUMBER: _ClassVar[int]
    LOG_SKIPPED_NODES_FIELD_NUMBER: _ClassVar[int]
    task_id: int
    view_id: int
    tree_uid: _universal_id_pb2.UniversalIdProto
    root_inode_id: int
    job_uid: _universal_id_pb2.UniversalIdProto
    node_id_floor: int
    base_archive_uid: _universal_id_pb2.UniversalIdProto
    parent_archive_uid_vec: _containers.RepeatedCompositeFieldContainer[_universal_id_pb2.UniversalIdProto]
    should_flush_blob_journal_data: bool
    min_key: int
    max_key: int
    snap_tree_iter_cookie: _icebox_pb2.SnapTreeIterCookieProto
    blob_info_cookie: _icebox_pb2.BlobInfo
    log_skipped_nodes: bool
    def __init__(self, task_id: _Optional[int] = ..., view_id: _Optional[int] = ..., tree_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., root_inode_id: _Optional[int] = ..., job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., node_id_floor: _Optional[int] = ..., base_archive_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., parent_archive_uid_vec: _Optional[_Iterable[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]]] = ..., should_flush_blob_journal_data: bool = ..., min_key: _Optional[int] = ..., max_key: _Optional[int] = ..., snap_tree_iter_cookie: _Optional[_Union[_icebox_pb2.SnapTreeIterCookieProto, _Mapping]] = ..., blob_info_cookie: _Optional[_Union[_icebox_pb2.BlobInfo, _Mapping]] = ..., log_skipped_nodes: bool = ...) -> None: ...

class GetBlobsInfoResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListViewFSFilesArg(_message.Message):
    __slots__ = ("job_uid", "task_id", "viewbox_id", "view_name", "view_fs_name", "relative_dir_path", "max_files", "cookie", "checkpoint_info", "action_file_dir_vec", "non_existent_fs_root_expected")
    JOB_UID_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    VIEWBOX_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    VIEW_FS_NAME_FIELD_NUMBER: _ClassVar[int]
    RELATIVE_DIR_PATH_FIELD_NUMBER: _ClassVar[int]
    MAX_FILES_FIELD_NUMBER: _ClassVar[int]
    COOKIE_FIELD_NUMBER: _ClassVar[int]
    CHECKPOINT_INFO_FIELD_NUMBER: _ClassVar[int]
    ACTION_FILE_DIR_VEC_FIELD_NUMBER: _ClassVar[int]
    NON_EXISTENT_FS_ROOT_EXPECTED_FIELD_NUMBER: _ClassVar[int]
    job_uid: _universal_id_pb2.UniversalIdProto
    task_id: int
    viewbox_id: int
    view_name: str
    view_fs_name: str
    relative_dir_path: str
    max_files: int
    cookie: str
    checkpoint_info: _icebox_pb2.TaskCheckpointInfo
    action_file_dir_vec: _containers.RepeatedScalarFieldContainer[str]
    non_existent_fs_root_expected: bool
    def __init__(self, job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., task_id: _Optional[int] = ..., viewbox_id: _Optional[int] = ..., view_name: _Optional[str] = ..., view_fs_name: _Optional[str] = ..., relative_dir_path: _Optional[str] = ..., max_files: _Optional[int] = ..., cookie: _Optional[str] = ..., checkpoint_info: _Optional[_Union[_icebox_pb2.TaskCheckpointInfo, _Mapping]] = ..., action_file_dir_vec: _Optional[_Iterable[str]] = ..., non_existent_fs_root_expected: bool = ...) -> None: ...

class ListViewFSFilesResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ValidateObjectsArg(_message.Message):
    __slots__ = ("job_uid", "task_id", "vault_id", "object_uid_vec", "actions", "checkpoint_info")
    JOB_UID_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    VAULT_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_UID_VEC_FIELD_NUMBER: _ClassVar[int]
    ACTIONS_FIELD_NUMBER: _ClassVar[int]
    CHECKPOINT_INFO_FIELD_NUMBER: _ClassVar[int]
    job_uid: _universal_id_pb2.UniversalIdProto
    task_id: int
    vault_id: int
    object_uid_vec: _containers.RepeatedCompositeFieldContainer[_universal_id_pb2.UniversalIdProto]
    actions: _icebox_pb2.ObjectsValidationActions
    checkpoint_info: _icebox_pb2.TaskCheckpointInfo
    def __init__(self, job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., task_id: _Optional[int] = ..., vault_id: _Optional[int] = ..., object_uid_vec: _Optional[_Iterable[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]]] = ..., actions: _Optional[_Union[_icebox_pb2.ObjectsValidationActions, _Mapping]] = ..., checkpoint_info: _Optional[_Union[_icebox_pb2.TaskCheckpointInfo, _Mapping]] = ...) -> None: ...

class ValidateObjectsResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class EvictObjectsFromVaultCacheArg(_message.Message):
    __slots__ = ("job_uid", "task_id", "vault_id", "object_uid_vec")
    JOB_UID_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    VAULT_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_UID_VEC_FIELD_NUMBER: _ClassVar[int]
    job_uid: _universal_id_pb2.UniversalIdProto
    task_id: int
    vault_id: int
    object_uid_vec: _containers.RepeatedCompositeFieldContainer[_universal_id_pb2.UniversalIdProto]
    def __init__(self, job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., task_id: _Optional[int] = ..., vault_id: _Optional[int] = ..., object_uid_vec: _Optional[_Iterable[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]]] = ...) -> None: ...

class EvictObjectsFromVaultCacheResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UptierDataArg(_message.Message):
    __slots__ = ("job_uid", "task_id", "vault_id", "archive_uid", "archival_job_type", "view_box_id", "stub_view_name", "stub_view_fs_name", "internal_view_name", "internal_view_fs_name", "dw_checkpoint_file_path", "object_info_dir_path", "dir_walker_cookie", "approx_data_size_bytes", "max_files_to_uptier", "checkpoint_info", "file_restore_info")
    JOB_UID_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    VAULT_ID_FIELD_NUMBER: _ClassVar[int]
    ARCHIVE_UID_FIELD_NUMBER: _ClassVar[int]
    ARCHIVAL_JOB_TYPE_FIELD_NUMBER: _ClassVar[int]
    VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
    STUB_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    STUB_VIEW_FS_NAME_FIELD_NUMBER: _ClassVar[int]
    INTERNAL_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    INTERNAL_VIEW_FS_NAME_FIELD_NUMBER: _ClassVar[int]
    DW_CHECKPOINT_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    OBJECT_INFO_DIR_PATH_FIELD_NUMBER: _ClassVar[int]
    DIR_WALKER_COOKIE_FIELD_NUMBER: _ClassVar[int]
    APPROX_DATA_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    MAX_FILES_TO_UPTIER_FIELD_NUMBER: _ClassVar[int]
    CHECKPOINT_INFO_FIELD_NUMBER: _ClassVar[int]
    FILE_RESTORE_INFO_FIELD_NUMBER: _ClassVar[int]
    job_uid: _universal_id_pb2.UniversalIdProto
    task_id: int
    vault_id: int
    archive_uid: _universal_id_pb2.UniversalIdProto
    archival_job_type: _icebox_pb2.IceboxJobType
    view_box_id: int
    stub_view_name: str
    stub_view_fs_name: str
    internal_view_name: str
    internal_view_fs_name: str
    dw_checkpoint_file_path: str
    object_info_dir_path: str
    dir_walker_cookie: _directory_walker_pb2.EntityMetadata
    approx_data_size_bytes: int
    max_files_to_uptier: int
    checkpoint_info: _icebox_pb2.TaskCheckpointInfo
    file_restore_info: _rpc_service_pb2.ScheduleRestoreJobArg.FileRestoreInfo
    def __init__(self, job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., task_id: _Optional[int] = ..., vault_id: _Optional[int] = ..., archive_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., archival_job_type: _Optional[_Union[_icebox_pb2.IceboxJobType, str]] = ..., view_box_id: _Optional[int] = ..., stub_view_name: _Optional[str] = ..., stub_view_fs_name: _Optional[str] = ..., internal_view_name: _Optional[str] = ..., internal_view_fs_name: _Optional[str] = ..., dw_checkpoint_file_path: _Optional[str] = ..., object_info_dir_path: _Optional[str] = ..., dir_walker_cookie: _Optional[_Union[_directory_walker_pb2.EntityMetadata, _Mapping]] = ..., approx_data_size_bytes: _Optional[int] = ..., max_files_to_uptier: _Optional[int] = ..., checkpoint_info: _Optional[_Union[_icebox_pb2.TaskCheckpointInfo, _Mapping]] = ..., file_restore_info: _Optional[_Union[_rpc_service_pb2.ScheduleRestoreJobArg.FileRestoreInfo, _Mapping]] = ...) -> None: ...

class UptierDataResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DowntierDataArg(_message.Message):
    __slots__ = ("job_uid", "task_id", "vault_id", "archive_uid", "view_box_id", "internal_view_name", "internal_view_fs_name", "object_info_dir_path_vec", "checkpoint_info", "archival_job_type")
    JOB_UID_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    VAULT_ID_FIELD_NUMBER: _ClassVar[int]
    ARCHIVE_UID_FIELD_NUMBER: _ClassVar[int]
    VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
    INTERNAL_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    INTERNAL_VIEW_FS_NAME_FIELD_NUMBER: _ClassVar[int]
    OBJECT_INFO_DIR_PATH_VEC_FIELD_NUMBER: _ClassVar[int]
    CHECKPOINT_INFO_FIELD_NUMBER: _ClassVar[int]
    ARCHIVAL_JOB_TYPE_FIELD_NUMBER: _ClassVar[int]
    job_uid: _universal_id_pb2.UniversalIdProto
    task_id: int
    vault_id: int
    archive_uid: _universal_id_pb2.UniversalIdProto
    view_box_id: int
    internal_view_name: str
    internal_view_fs_name: str
    object_info_dir_path_vec: _containers.RepeatedScalarFieldContainer[str]
    checkpoint_info: _icebox_pb2.TaskCheckpointInfo
    archival_job_type: _icebox_pb2.IceboxJobType
    def __init__(self, job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., task_id: _Optional[int] = ..., vault_id: _Optional[int] = ..., archive_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., view_box_id: _Optional[int] = ..., internal_view_name: _Optional[str] = ..., internal_view_fs_name: _Optional[str] = ..., object_info_dir_path_vec: _Optional[_Iterable[str]] = ..., checkpoint_info: _Optional[_Union[_icebox_pb2.TaskCheckpointInfo, _Mapping]] = ..., archival_job_type: _Optional[_Union[_icebox_pb2.IceboxJobType, str]] = ...) -> None: ...

class DowntierDataResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetSnapTreeKeyRangesArg(_message.Message):
    __slots__ = ("tree_uid_vec", "max_desired_key_ranges", "is_view_snap_tree")
    TREE_UID_VEC_FIELD_NUMBER: _ClassVar[int]
    MAX_DESIRED_KEY_RANGES_FIELD_NUMBER: _ClassVar[int]
    IS_VIEW_SNAP_TREE_FIELD_NUMBER: _ClassVar[int]
    tree_uid_vec: _containers.RepeatedCompositeFieldContainer[_universal_id_pb2.UniversalIdProto]
    max_desired_key_ranges: int
    is_view_snap_tree: bool
    def __init__(self, tree_uid_vec: _Optional[_Iterable[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]]] = ..., max_desired_key_ranges: _Optional[int] = ..., is_view_snap_tree: bool = ...) -> None: ...

class GetSnapTreeKeyRangesResult(_message.Message):
    __slots__ = ("snap_tree_key_ranges_map",)
    class SnapTreeKeyRanges(_message.Message):
        __slots__ = ("snap_tree_key_range_vec",)
        class SnapTreeKeyRange(_message.Message):
            __slots__ = ("min_key", "max_key")
            MIN_KEY_FIELD_NUMBER: _ClassVar[int]
            MAX_KEY_FIELD_NUMBER: _ClassVar[int]
            min_key: int
            max_key: int
            def __init__(self, min_key: _Optional[int] = ..., max_key: _Optional[int] = ...) -> None: ...
        SNAP_TREE_KEY_RANGE_VEC_FIELD_NUMBER: _ClassVar[int]
        snap_tree_key_range_vec: _containers.RepeatedCompositeFieldContainer[GetSnapTreeKeyRangesResult.SnapTreeKeyRanges.SnapTreeKeyRange]
        def __init__(self, snap_tree_key_range_vec: _Optional[_Iterable[_Union[GetSnapTreeKeyRangesResult.SnapTreeKeyRanges.SnapTreeKeyRange, _Mapping]]] = ...) -> None: ...
    class SnapTreeKeyRangesMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: GetSnapTreeKeyRangesResult.SnapTreeKeyRanges
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[GetSnapTreeKeyRangesResult.SnapTreeKeyRanges, _Mapping]] = ...) -> None: ...
    SNAP_TREE_KEY_RANGES_MAP_FIELD_NUMBER: _ClassVar[int]
    snap_tree_key_ranges_map: _containers.MessageMap[str, GetSnapTreeKeyRangesResult.SnapTreeKeyRanges]
    def __init__(self, snap_tree_key_ranges_map: _Optional[_Mapping[str, GetSnapTreeKeyRangesResult.SnapTreeKeyRanges]] = ...) -> None: ...

class CreateStubViewArg(_message.Message):
    __slots__ = ("archive_uid", "entity_id", "viewbox_id", "application_name", "expiry_timestamp_usecs", "is_download_index_job")
    ARCHIVE_UID_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    VIEWBOX_ID_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_NAME_FIELD_NUMBER: _ClassVar[int]
    EXPIRY_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
    IS_DOWNLOAD_INDEX_JOB_FIELD_NUMBER: _ClassVar[int]
    archive_uid: _universal_id_pb2.UniversalIdProto
    entity_id: int
    viewbox_id: int
    application_name: str
    expiry_timestamp_usecs: int
    is_download_index_job: bool
    def __init__(self, archive_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., entity_id: _Optional[int] = ..., viewbox_id: _Optional[int] = ..., application_name: _Optional[str] = ..., expiry_timestamp_usecs: _Optional[int] = ..., is_download_index_job: bool = ...) -> None: ...

class CreateStubViewResult(_message.Message):
    __slots__ = ("view_id", "view_name", "file_system_name", "entity_dir_relative_path")
    VIEW_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    FILE_SYSTEM_NAME_FIELD_NUMBER: _ClassVar[int]
    ENTITY_DIR_RELATIVE_PATH_FIELD_NUMBER: _ClassVar[int]
    view_id: int
    view_name: str
    file_system_name: str
    entity_dir_relative_path: str
    def __init__(self, view_id: _Optional[int] = ..., view_name: _Optional[str] = ..., file_system_name: _Optional[str] = ..., entity_dir_relative_path: _Optional[str] = ...) -> None: ...

class DeleteStubViewArg(_message.Message):
    __slots__ = ("archive_uid", "entity_id", "stub_view_id", "scribe_version", "force_delete", "viewbox_id")
    ARCHIVE_UID_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    STUB_VIEW_ID_FIELD_NUMBER: _ClassVar[int]
    SCRIBE_VERSION_FIELD_NUMBER: _ClassVar[int]
    FORCE_DELETE_FIELD_NUMBER: _ClassVar[int]
    VIEWBOX_ID_FIELD_NUMBER: _ClassVar[int]
    archive_uid: _universal_id_pb2.UniversalIdProto
    entity_id: int
    stub_view_id: int
    scribe_version: int
    force_delete: bool
    viewbox_id: int
    def __init__(self, archive_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., entity_id: _Optional[int] = ..., stub_view_id: _Optional[int] = ..., scribe_version: _Optional[int] = ..., force_delete: bool = ..., viewbox_id: _Optional[int] = ...) -> None: ...

class DeleteStubViewResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CrashSlaveArg(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CrashSlaveResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UptierCloudDomainDataArg(_message.Message):
    __slots__ = ("job_uid", "task_id", "archive_uid", "cloud_domain_id", "tree_info_vec", "view_box_id", "stub_view_name", "stub_view_fs_name", "internal_view_name", "internal_view_fs_name", "dw_checkpoint_file_path", "file_restore_info", "checkpoint_info", "epoch_id", "app_job_uid")
    class ViewSnapTreeInfo(_message.Message):
        __slots__ = ("tree_id", "view_id", "root_inode_id")
        TREE_ID_FIELD_NUMBER: _ClassVar[int]
        VIEW_ID_FIELD_NUMBER: _ClassVar[int]
        ROOT_INODE_ID_FIELD_NUMBER: _ClassVar[int]
        tree_id: int
        view_id: int
        root_inode_id: int
        def __init__(self, tree_id: _Optional[int] = ..., view_id: _Optional[int] = ..., root_inode_id: _Optional[int] = ...) -> None: ...
    JOB_UID_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    ARCHIVE_UID_FIELD_NUMBER: _ClassVar[int]
    CLOUD_DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    TREE_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
    STUB_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    STUB_VIEW_FS_NAME_FIELD_NUMBER: _ClassVar[int]
    INTERNAL_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    INTERNAL_VIEW_FS_NAME_FIELD_NUMBER: _ClassVar[int]
    DW_CHECKPOINT_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    FILE_RESTORE_INFO_FIELD_NUMBER: _ClassVar[int]
    CHECKPOINT_INFO_FIELD_NUMBER: _ClassVar[int]
    EPOCH_ID_FIELD_NUMBER: _ClassVar[int]
    APP_JOB_UID_FIELD_NUMBER: _ClassVar[int]
    job_uid: _universal_id_pb2.UniversalIdProto
    task_id: int
    archive_uid: _universal_id_pb2.UniversalIdProto
    cloud_domain_id: int
    tree_info_vec: _containers.RepeatedCompositeFieldContainer[UptierCloudDomainDataArg.ViewSnapTreeInfo]
    view_box_id: int
    stub_view_name: str
    stub_view_fs_name: str
    internal_view_name: str
    internal_view_fs_name: str
    dw_checkpoint_file_path: str
    file_restore_info: _rpc_service_pb2.ScheduleRestoreJobArg.FileRestoreInfo
    checkpoint_info: _icebox_pb2.TaskCheckpointInfo
    epoch_id: int
    app_job_uid: _universal_id_pb2.UniversalIdProto
    def __init__(self, job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., task_id: _Optional[int] = ..., archive_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., cloud_domain_id: _Optional[int] = ..., tree_info_vec: _Optional[_Iterable[_Union[UptierCloudDomainDataArg.ViewSnapTreeInfo, _Mapping]]] = ..., view_box_id: _Optional[int] = ..., stub_view_name: _Optional[str] = ..., stub_view_fs_name: _Optional[str] = ..., internal_view_name: _Optional[str] = ..., internal_view_fs_name: _Optional[str] = ..., dw_checkpoint_file_path: _Optional[str] = ..., file_restore_info: _Optional[_Union[_rpc_service_pb2.ScheduleRestoreJobArg.FileRestoreInfo, _Mapping]] = ..., checkpoint_info: _Optional[_Union[_icebox_pb2.TaskCheckpointInfo, _Mapping]] = ..., epoch_id: _Optional[int] = ..., app_job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ...) -> None: ...

class UptierCloudDomainDataResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class FindMissingFilesArg(_message.Message):
    __slots__ = ("backup_view_id", "view_id", "file_path_to_examine", "print_missing_files_output_path_prefix", "print_non_missing_files_output_path_prefix")
    BACKUP_VIEW_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_ID_FIELD_NUMBER: _ClassVar[int]
    FILE_PATH_TO_EXAMINE_FIELD_NUMBER: _ClassVar[int]
    PRINT_MISSING_FILES_OUTPUT_PATH_PREFIX_FIELD_NUMBER: _ClassVar[int]
    PRINT_NON_MISSING_FILES_OUTPUT_PATH_PREFIX_FIELD_NUMBER: _ClassVar[int]
    backup_view_id: int
    view_id: int
    file_path_to_examine: str
    print_missing_files_output_path_prefix: str
    print_non_missing_files_output_path_prefix: str
    def __init__(self, backup_view_id: _Optional[int] = ..., view_id: _Optional[int] = ..., file_path_to_examine: _Optional[str] = ..., print_missing_files_output_path_prefix: _Optional[str] = ..., print_non_missing_files_output_path_prefix: _Optional[str] = ...) -> None: ...

class FindMissingFilesResult(_message.Message):
    __slots__ = ("file_archive_status",)
    class FileArchiveStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNonExistent: _ClassVar[FindMissingFilesResult.FileArchiveStatus]
        kNotArchived: _ClassVar[FindMissingFilesResult.FileArchiveStatus]
        kArchived: _ClassVar[FindMissingFilesResult.FileArchiveStatus]
    kNonExistent: FindMissingFilesResult.FileArchiveStatus
    kNotArchived: FindMissingFilesResult.FileArchiveStatus
    kArchived: FindMissingFilesResult.FileArchiveStatus
    FILE_ARCHIVE_STATUS_FIELD_NUMBER: _ClassVar[int]
    file_archive_status: FindMissingFilesResult.FileArchiveStatus
    def __init__(self, file_archive_status: _Optional[_Union[FindMissingFilesResult.FileArchiveStatus, str]] = ...) -> None: ...

class PopulateCloudDomainEntriesInScribeArg(_message.Message):
    __slots__ = ("job_uid", "task_id", "cloud_domain_id", "object_type", "object_name_vec")
    JOB_UID_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    CLOUD_DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_TYPE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_NAME_VEC_FIELD_NUMBER: _ClassVar[int]
    job_uid: _universal_id_pb2.UniversalIdProto
    task_id: int
    cloud_domain_id: int
    object_type: _rpc_service_pb2.ScheduleCloudDomainRebuildJobArg.ObjectType
    object_name_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., task_id: _Optional[int] = ..., cloud_domain_id: _Optional[int] = ..., object_type: _Optional[_Union[_rpc_service_pb2.ScheduleCloudDomainRebuildJobArg.ObjectType, str]] = ..., object_name_vec: _Optional[_Iterable[str]] = ...) -> None: ...

class PopulateCloudDomainEntriesInScribeResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class RecoverFileDataArg(_message.Message):
    __slots__ = ("entity_handle", "inode_metadata", "offset", "size")
    ENTITY_HANDLE_FIELD_NUMBER: _ClassVar[int]
    INODE_METADATA_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    entity_handle: _entity_handle_pb2.EntityHandleProto
    inode_metadata: _snap_fs_metadata_pb2.InodeMetadataProto
    offset: int
    size: int
    def __init__(self, entity_handle: _Optional[_Union[_entity_handle_pb2.EntityHandleProto, _Mapping]] = ..., inode_metadata: _Optional[_Union[_snap_fs_metadata_pb2.InodeMetadataProto, _Mapping]] = ..., offset: _Optional[int] = ..., size: _Optional[int] = ...) -> None: ...

class RecoverFileDataResult(_message.Message):
    __slots__ = ("is_eof", "data")
    IS_EOF_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    is_eof: bool
    data: bytes
    def __init__(self, is_eof: bool = ..., data: _Optional[bytes] = ...) -> None: ...

class CheckArchivesInSameChainArg(_message.Message):
    __slots__ = ("archive_uid1", "archive_uid2")
    ARCHIVE_UID1_FIELD_NUMBER: _ClassVar[int]
    ARCHIVE_UID2_FIELD_NUMBER: _ClassVar[int]
    archive_uid1: _universal_id_pb2.UniversalIdProto
    archive_uid2: _universal_id_pb2.UniversalIdProto
    def __init__(self, archive_uid1: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., archive_uid2: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ...) -> None: ...

class CheckArchivesInSameChainResult(_message.Message):
    __slots__ = ("can_dedup",)
    CAN_DEDUP_FIELD_NUMBER: _ClassVar[int]
    can_dedup: bool
    def __init__(self, can_dedup: bool = ...) -> None: ...

class RecoverStubSnapTreeNodeArg(_message.Message):
    __slots__ = ("root_tree_id", "tree_id", "node_id", "int_key", "str_key", "tree_type", "stub_node_proto")
    ROOT_TREE_ID_FIELD_NUMBER: _ClassVar[int]
    TREE_ID_FIELD_NUMBER: _ClassVar[int]
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    INT_KEY_FIELD_NUMBER: _ClassVar[int]
    STR_KEY_FIELD_NUMBER: _ClassVar[int]
    TREE_TYPE_FIELD_NUMBER: _ClassVar[int]
    STUB_NODE_PROTO_FIELD_NUMBER: _ClassVar[int]
    root_tree_id: int
    tree_id: int
    node_id: int
    int_key: int
    str_key: str
    tree_type: _icebox_pb2.IceboxSnapTreeType
    stub_node_proto: _snap_tree_pb2.SnapTreeNodeProto
    def __init__(self, root_tree_id: _Optional[int] = ..., tree_id: _Optional[int] = ..., node_id: _Optional[int] = ..., int_key: _Optional[int] = ..., str_key: _Optional[str] = ..., tree_type: _Optional[_Union[_icebox_pb2.IceboxSnapTreeType, str]] = ..., stub_node_proto: _Optional[_Union[_snap_tree_pb2.SnapTreeNodeProto, _Mapping]] = ...) -> None: ...

class RecoverStubSnapTreeNodeResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class FixChunkLocationsArg(_message.Message):
    __slots__ = ("chunk_id_vec",)
    CHUNK_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    chunk_id_vec: _containers.RepeatedCompositeFieldContainer[_icebox_pb2.IceboxChunkIdProto]
    def __init__(self, chunk_id_vec: _Optional[_Iterable[_Union[_icebox_pb2.IceboxChunkIdProto, _Mapping]]] = ...) -> None: ...

class FixChunkLocationsResult(_message.Message):
    __slots__ = ("error_vec",)
    ERROR_VEC_FIELD_NUMBER: _ClassVar[int]
    error_vec: _containers.RepeatedCompositeFieldContainer[_error_pb2.ErrorProto]
    def __init__(self, error_vec: _Optional[_Iterable[_Union[_error_pb2.ErrorProto, _Mapping]]] = ...) -> None: ...

class CopySnapTreesArg(_message.Message):
    __slots__ = ("archive_uid", "task_id", "view_box_id", "storage_handle", "view_id", "base_storage_handle", "base_view_id", "snap_tree_info_vec")
    class SnapTreeInfo(_message.Message):
        __slots__ = ("root_snap_tree_id", "tree_type", "root_name")
        ROOT_SNAP_TREE_ID_FIELD_NUMBER: _ClassVar[int]
        TREE_TYPE_FIELD_NUMBER: _ClassVar[int]
        ROOT_NAME_FIELD_NUMBER: _ClassVar[int]
        root_snap_tree_id: int
        tree_type: _icebox_pb2.IceboxSnapTreeType
        root_name: str
        def __init__(self, root_snap_tree_id: _Optional[int] = ..., tree_type: _Optional[_Union[_icebox_pb2.IceboxSnapTreeType, str]] = ..., root_name: _Optional[str] = ...) -> None: ...
    ARCHIVE_UID_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
    STORAGE_HANDLE_FIELD_NUMBER: _ClassVar[int]
    VIEW_ID_FIELD_NUMBER: _ClassVar[int]
    BASE_STORAGE_HANDLE_FIELD_NUMBER: _ClassVar[int]
    BASE_VIEW_ID_FIELD_NUMBER: _ClassVar[int]
    SNAP_TREE_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    archive_uid: _universal_id_pb2.UniversalIdProto
    task_id: int
    view_box_id: int
    storage_handle: _common_pb2.BackupStorageHandle
    view_id: int
    base_storage_handle: _common_pb2.BackupStorageHandle
    base_view_id: int
    snap_tree_info_vec: _containers.RepeatedCompositeFieldContainer[CopySnapTreesArg.SnapTreeInfo]
    def __init__(self, archive_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., task_id: _Optional[int] = ..., view_box_id: _Optional[int] = ..., storage_handle: _Optional[_Union[_common_pb2.BackupStorageHandle, _Mapping]] = ..., view_id: _Optional[int] = ..., base_storage_handle: _Optional[_Union[_common_pb2.BackupStorageHandle, _Mapping]] = ..., base_view_id: _Optional[int] = ..., snap_tree_info_vec: _Optional[_Iterable[_Union[CopySnapTreesArg.SnapTreeInfo, _Mapping]]] = ...) -> None: ...

class CopySnapTreesResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
