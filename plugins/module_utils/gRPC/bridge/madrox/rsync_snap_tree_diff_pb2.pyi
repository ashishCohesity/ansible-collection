from bridge.snap_fs import entity_handle_pb2 as _entity_handle_pb2
from bridge.snap_fs import snap_fs_metadata_pb2 as _snap_fs_metadata_pb2
from bridge.view_keeper import view_metadata_pb2 as _view_metadata_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RsyncInodeMapKeyProto(_message.Message):
    __slots__ = ("inode_entity_handle", "is_missing_entity", "fixed_s3_intent_on_entity", "is_ancestor_dir_sync")
    INODE_ENTITY_HANDLE_FIELD_NUMBER: _ClassVar[int]
    IS_MISSING_ENTITY_FIELD_NUMBER: _ClassVar[int]
    FIXED_S3_INTENT_ON_ENTITY_FIELD_NUMBER: _ClassVar[int]
    IS_ANCESTOR_DIR_SYNC_FIELD_NUMBER: _ClassVar[int]
    inode_entity_handle: _entity_handle_pb2.EntityHandleProto
    is_missing_entity: bool
    fixed_s3_intent_on_entity: bool
    is_ancestor_dir_sync: bool
    def __init__(self, inode_entity_handle: _Optional[_Union[_entity_handle_pb2.EntityHandleProto, _Mapping]] = ..., is_missing_entity: bool = ..., fixed_s3_intent_on_entity: bool = ..., is_ancestor_dir_sync: bool = ...) -> None: ...

class RsyncOperation(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kCreate: _ClassVar[RsyncOperation.Type]
        kMoveForAdd: _ClassVar[RsyncOperation.Type]
        kAddHardLink: _ClassVar[RsyncOperation.Type]
        kMoveForRemove: _ClassVar[RsyncOperation.Type]
        kRemove: _ClassVar[RsyncOperation.Type]
        kUpdateMetadata: _ClassVar[RsyncOperation.Type]
        kRmDir: _ClassVar[RsyncOperation.Type]
    kCreate: RsyncOperation.Type
    kMoveForAdd: RsyncOperation.Type
    kAddHardLink: RsyncOperation.Type
    kMoveForRemove: RsyncOperation.Type
    kRemove: RsyncOperation.Type
    kUpdateMetadata: RsyncOperation.Type
    kRmDir: RsyncOperation.Type
    def __init__(self) -> None: ...

class RsyncInodeMapValueProto(_message.Message):
    __slots__ = ("is_synced", "completed_removals", "metadata_synced", "processed_until_cookie", "processed_until_cookie_verifier", "file_sync_done_bytes", "update_intent", "existing_dst_path", "older_incarnation_entity_id", "num_entries_removed", "num_entries_added", "entity_name", "parent_entity_id", "entity_move_for_add_done", "sync_full_file", "ancestor_dir_divergence_checked_and_fixed", "dir_sync_validation_completed", "missing_entities_created_in_namespace", "processed_until_dir_fragment_index", "num_missing_entities", "new_entity")
    class UpdateIntent(_message.Message):
        __slots__ = ("new_dst_path", "operation", "src_inode_metadata")
        NEW_DST_PATH_FIELD_NUMBER: _ClassVar[int]
        OPERATION_FIELD_NUMBER: _ClassVar[int]
        SRC_INODE_METADATA_FIELD_NUMBER: _ClassVar[int]
        new_dst_path: bytes
        operation: RsyncOperation.Type
        src_inode_metadata: _snap_fs_metadata_pb2.InodeMetadataProto
        def __init__(self, new_dst_path: _Optional[bytes] = ..., operation: _Optional[_Union[RsyncOperation.Type, str]] = ..., src_inode_metadata: _Optional[_Union[_snap_fs_metadata_pb2.InodeMetadataProto, _Mapping]] = ...) -> None: ...
    IS_SYNCED_FIELD_NUMBER: _ClassVar[int]
    COMPLETED_REMOVALS_FIELD_NUMBER: _ClassVar[int]
    METADATA_SYNCED_FIELD_NUMBER: _ClassVar[int]
    PROCESSED_UNTIL_COOKIE_FIELD_NUMBER: _ClassVar[int]
    PROCESSED_UNTIL_COOKIE_VERIFIER_FIELD_NUMBER: _ClassVar[int]
    FILE_SYNC_DONE_BYTES_FIELD_NUMBER: _ClassVar[int]
    UPDATE_INTENT_FIELD_NUMBER: _ClassVar[int]
    EXISTING_DST_PATH_FIELD_NUMBER: _ClassVar[int]
    OLDER_INCARNATION_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    NUM_ENTRIES_REMOVED_FIELD_NUMBER: _ClassVar[int]
    NUM_ENTRIES_ADDED_FIELD_NUMBER: _ClassVar[int]
    ENTITY_NAME_FIELD_NUMBER: _ClassVar[int]
    PARENT_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    ENTITY_MOVE_FOR_ADD_DONE_FIELD_NUMBER: _ClassVar[int]
    SYNC_FULL_FILE_FIELD_NUMBER: _ClassVar[int]
    ANCESTOR_DIR_DIVERGENCE_CHECKED_AND_FIXED_FIELD_NUMBER: _ClassVar[int]
    DIR_SYNC_VALIDATION_COMPLETED_FIELD_NUMBER: _ClassVar[int]
    MISSING_ENTITIES_CREATED_IN_NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    PROCESSED_UNTIL_DIR_FRAGMENT_INDEX_FIELD_NUMBER: _ClassVar[int]
    NUM_MISSING_ENTITIES_FIELD_NUMBER: _ClassVar[int]
    NEW_ENTITY_FIELD_NUMBER: _ClassVar[int]
    is_synced: bool
    completed_removals: bool
    metadata_synced: bool
    processed_until_cookie: int
    processed_until_cookie_verifier: int
    file_sync_done_bytes: int
    update_intent: RsyncInodeMapValueProto.UpdateIntent
    existing_dst_path: bytes
    older_incarnation_entity_id: int
    num_entries_removed: int
    num_entries_added: int
    entity_name: bytes
    parent_entity_id: int
    entity_move_for_add_done: bool
    sync_full_file: bool
    ancestor_dir_divergence_checked_and_fixed: bool
    dir_sync_validation_completed: bool
    missing_entities_created_in_namespace: bool
    processed_until_dir_fragment_index: int
    num_missing_entities: int
    new_entity: bool
    def __init__(self, is_synced: bool = ..., completed_removals: bool = ..., metadata_synced: bool = ..., processed_until_cookie: _Optional[int] = ..., processed_until_cookie_verifier: _Optional[int] = ..., file_sync_done_bytes: _Optional[int] = ..., update_intent: _Optional[_Union[RsyncInodeMapValueProto.UpdateIntent, _Mapping]] = ..., existing_dst_path: _Optional[bytes] = ..., older_incarnation_entity_id: _Optional[int] = ..., num_entries_removed: _Optional[int] = ..., num_entries_added: _Optional[int] = ..., entity_name: _Optional[bytes] = ..., parent_entity_id: _Optional[int] = ..., entity_move_for_add_done: bool = ..., sync_full_file: bool = ..., ancestor_dir_divergence_checked_and_fixed: bool = ..., dir_sync_validation_completed: bool = ..., missing_entities_created_in_namespace: bool = ..., processed_until_dir_fragment_index: _Optional[int] = ..., num_missing_entities: _Optional[int] = ..., new_entity: bool = ...) -> None: ...

class CustomSnapTreeKeyProto(_message.Message):
    __slots__ = ("key_int", "key_str")
    KEY_INT_FIELD_NUMBER: _ClassVar[int]
    KEY_STR_FIELD_NUMBER: _ClassVar[int]
    key_int: int
    key_str: str
    def __init__(self, key_int: _Optional[int] = ..., key_str: _Optional[str] = ...) -> None: ...

class RsyncSnapTreeDiffTransmitOpCheckpoint(_message.Message):
    __slots__ = ("start_time_usecs", "num_incarnations", "num_attempts_allowed", "num_attempts_remaining", "resolved_all_update_intents", "root_info_vec", "curr_root_index", "completed_key_ceiling", "ancestor_s3_intent_fixing_complete", "ancestor_s3_intent_scan_cookie", "missing_inodes_scan_cookie", "custom_snap_tree_info_vec", "curr_custom_snap_tree_idx", "custom_snap_tree_comp_key_ceiling", "progress", "progress_map", "resolved_all_update_intents_usecs", "estimated_logical_bytes_to_transfer", "estimated_changed_entities", "synced_files_logical_size_sum", "finished_due_to_blackout")
    class ShardInfo(_message.Message):
        __slots__ = ("end_key", "completed_key_ceiling")
        END_KEY_FIELD_NUMBER: _ClassVar[int]
        COMPLETED_KEY_CEILING_FIELD_NUMBER: _ClassVar[int]
        end_key: int
        completed_key_ceiling: int
        def __init__(self, end_key: _Optional[int] = ..., completed_key_ceiling: _Optional[int] = ...) -> None: ...
    class RootInfo(_message.Message):
        __slots__ = ("root_name", "search_key_vec", "avg_search_key_coverage", "shard_info_vec", "may_have_s3_intents")
        ROOT_NAME_FIELD_NUMBER: _ClassVar[int]
        SEARCH_KEY_VEC_FIELD_NUMBER: _ClassVar[int]
        AVG_SEARCH_KEY_COVERAGE_FIELD_NUMBER: _ClassVar[int]
        SHARD_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
        MAY_HAVE_S3_INTENTS_FIELD_NUMBER: _ClassVar[int]
        root_name: str
        search_key_vec: _containers.RepeatedScalarFieldContainer[int]
        avg_search_key_coverage: int
        shard_info_vec: _containers.RepeatedCompositeFieldContainer[RsyncSnapTreeDiffTransmitOpCheckpoint.ShardInfo]
        may_have_s3_intents: bool
        def __init__(self, root_name: _Optional[str] = ..., search_key_vec: _Optional[_Iterable[int]] = ..., avg_search_key_coverage: _Optional[int] = ..., shard_info_vec: _Optional[_Iterable[_Union[RsyncSnapTreeDiffTransmitOpCheckpoint.ShardInfo, _Mapping]]] = ..., may_have_s3_intents: bool = ...) -> None: ...
    class SpecialEntryRangeScanCookie(_message.Message):
        __slots__ = ("bucket_id", "scan_start_key")
        BUCKET_ID_FIELD_NUMBER: _ClassVar[int]
        SCAN_START_KEY_FIELD_NUMBER: _ClassVar[int]
        bucket_id: int
        scan_start_key: bytes
        def __init__(self, bucket_id: _Optional[int] = ..., scan_start_key: _Optional[bytes] = ...) -> None: ...
    class CustomSnapTreeInfo(_message.Message):
        __slots__ = ("tree_info",)
        TREE_INFO_FIELD_NUMBER: _ClassVar[int]
        tree_info: _view_metadata_pb2.SnapTreeInfo
        def __init__(self, tree_info: _Optional[_Union[_view_metadata_pb2.SnapTreeInfo, _Mapping]] = ...) -> None: ...
    class CustomSnapTreeStats(_message.Message):
        __slots__ = ("s3object_tree_md_actions_completed",)
        S3OBJECT_TREE_MD_ACTIONS_COMPLETED_FIELD_NUMBER: _ClassVar[int]
        s3object_tree_md_actions_completed: int
        def __init__(self, s3object_tree_md_actions_completed: _Optional[int] = ...) -> None: ...
    class Progress(_message.Message):
        __slots__ = ("logical_bytes_transferred", "physical_bytes_transferred", "metadata_actions_completed", "morphed_physical_bytes_transferred", "num_entities_synced", "num_entries_added", "num_entries_removed", "err_logical_bytes_transferred", "err_physical_bytes_transferred", "logical_bytes_transferred_object_ns", "metadata_actions_completed_object_ns", "custom_snap_tree_stats")
        LOGICAL_BYTES_TRANSFERRED_FIELD_NUMBER: _ClassVar[int]
        PHYSICAL_BYTES_TRANSFERRED_FIELD_NUMBER: _ClassVar[int]
        METADATA_ACTIONS_COMPLETED_FIELD_NUMBER: _ClassVar[int]
        MORPHED_PHYSICAL_BYTES_TRANSFERRED_FIELD_NUMBER: _ClassVar[int]
        NUM_ENTITIES_SYNCED_FIELD_NUMBER: _ClassVar[int]
        NUM_ENTRIES_ADDED_FIELD_NUMBER: _ClassVar[int]
        NUM_ENTRIES_REMOVED_FIELD_NUMBER: _ClassVar[int]
        ERR_LOGICAL_BYTES_TRANSFERRED_FIELD_NUMBER: _ClassVar[int]
        ERR_PHYSICAL_BYTES_TRANSFERRED_FIELD_NUMBER: _ClassVar[int]
        LOGICAL_BYTES_TRANSFERRED_OBJECT_NS_FIELD_NUMBER: _ClassVar[int]
        METADATA_ACTIONS_COMPLETED_OBJECT_NS_FIELD_NUMBER: _ClassVar[int]
        CUSTOM_SNAP_TREE_STATS_FIELD_NUMBER: _ClassVar[int]
        logical_bytes_transferred: int
        physical_bytes_transferred: int
        metadata_actions_completed: int
        morphed_physical_bytes_transferred: int
        num_entities_synced: int
        num_entries_added: int
        num_entries_removed: int
        err_logical_bytes_transferred: int
        err_physical_bytes_transferred: int
        logical_bytes_transferred_object_ns: int
        metadata_actions_completed_object_ns: int
        custom_snap_tree_stats: RsyncSnapTreeDiffTransmitOpCheckpoint.CustomSnapTreeStats
        def __init__(self, logical_bytes_transferred: _Optional[int] = ..., physical_bytes_transferred: _Optional[int] = ..., metadata_actions_completed: _Optional[int] = ..., morphed_physical_bytes_transferred: _Optional[int] = ..., num_entities_synced: _Optional[int] = ..., num_entries_added: _Optional[int] = ..., num_entries_removed: _Optional[int] = ..., err_logical_bytes_transferred: _Optional[int] = ..., err_physical_bytes_transferred: _Optional[int] = ..., logical_bytes_transferred_object_ns: _Optional[int] = ..., metadata_actions_completed_object_ns: _Optional[int] = ..., custom_snap_tree_stats: _Optional[_Union[RsyncSnapTreeDiffTransmitOpCheckpoint.CustomSnapTreeStats, _Mapping]] = ...) -> None: ...
    class ProgressMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: RsyncSnapTreeDiffTransmitOpCheckpoint.Progress
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[RsyncSnapTreeDiffTransmitOpCheckpoint.Progress, _Mapping]] = ...) -> None: ...
    START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    NUM_INCARNATIONS_FIELD_NUMBER: _ClassVar[int]
    NUM_ATTEMPTS_ALLOWED_FIELD_NUMBER: _ClassVar[int]
    NUM_ATTEMPTS_REMAINING_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_ALL_UPDATE_INTENTS_FIELD_NUMBER: _ClassVar[int]
    ROOT_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    CURR_ROOT_INDEX_FIELD_NUMBER: _ClassVar[int]
    COMPLETED_KEY_CEILING_FIELD_NUMBER: _ClassVar[int]
    ANCESTOR_S3_INTENT_FIXING_COMPLETE_FIELD_NUMBER: _ClassVar[int]
    ANCESTOR_S3_INTENT_SCAN_COOKIE_FIELD_NUMBER: _ClassVar[int]
    MISSING_INODES_SCAN_COOKIE_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_SNAP_TREE_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    CURR_CUSTOM_SNAP_TREE_IDX_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_SNAP_TREE_COMP_KEY_CEILING_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_MAP_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_ALL_UPDATE_INTENTS_USECS_FIELD_NUMBER: _ClassVar[int]
    ESTIMATED_LOGICAL_BYTES_TO_TRANSFER_FIELD_NUMBER: _ClassVar[int]
    ESTIMATED_CHANGED_ENTITIES_FIELD_NUMBER: _ClassVar[int]
    SYNCED_FILES_LOGICAL_SIZE_SUM_FIELD_NUMBER: _ClassVar[int]
    FINISHED_DUE_TO_BLACKOUT_FIELD_NUMBER: _ClassVar[int]
    start_time_usecs: int
    num_incarnations: int
    num_attempts_allowed: int
    num_attempts_remaining: int
    resolved_all_update_intents: bool
    root_info_vec: _containers.RepeatedCompositeFieldContainer[RsyncSnapTreeDiffTransmitOpCheckpoint.RootInfo]
    curr_root_index: int
    completed_key_ceiling: int
    ancestor_s3_intent_fixing_complete: bool
    ancestor_s3_intent_scan_cookie: RsyncSnapTreeDiffTransmitOpCheckpoint.SpecialEntryRangeScanCookie
    missing_inodes_scan_cookie: RsyncSnapTreeDiffTransmitOpCheckpoint.SpecialEntryRangeScanCookie
    custom_snap_tree_info_vec: _containers.RepeatedCompositeFieldContainer[RsyncSnapTreeDiffTransmitOpCheckpoint.CustomSnapTreeInfo]
    curr_custom_snap_tree_idx: int
    custom_snap_tree_comp_key_ceiling: CustomSnapTreeKeyProto
    progress: RsyncSnapTreeDiffTransmitOpCheckpoint.Progress
    progress_map: _containers.MessageMap[int, RsyncSnapTreeDiffTransmitOpCheckpoint.Progress]
    resolved_all_update_intents_usecs: int
    estimated_logical_bytes_to_transfer: int
    estimated_changed_entities: int
    synced_files_logical_size_sum: int
    finished_due_to_blackout: bool
    def __init__(self, start_time_usecs: _Optional[int] = ..., num_incarnations: _Optional[int] = ..., num_attempts_allowed: _Optional[int] = ..., num_attempts_remaining: _Optional[int] = ..., resolved_all_update_intents: bool = ..., root_info_vec: _Optional[_Iterable[_Union[RsyncSnapTreeDiffTransmitOpCheckpoint.RootInfo, _Mapping]]] = ..., curr_root_index: _Optional[int] = ..., completed_key_ceiling: _Optional[int] = ..., ancestor_s3_intent_fixing_complete: bool = ..., ancestor_s3_intent_scan_cookie: _Optional[_Union[RsyncSnapTreeDiffTransmitOpCheckpoint.SpecialEntryRangeScanCookie, _Mapping]] = ..., missing_inodes_scan_cookie: _Optional[_Union[RsyncSnapTreeDiffTransmitOpCheckpoint.SpecialEntryRangeScanCookie, _Mapping]] = ..., custom_snap_tree_info_vec: _Optional[_Iterable[_Union[RsyncSnapTreeDiffTransmitOpCheckpoint.CustomSnapTreeInfo, _Mapping]]] = ..., curr_custom_snap_tree_idx: _Optional[int] = ..., custom_snap_tree_comp_key_ceiling: _Optional[_Union[CustomSnapTreeKeyProto, _Mapping]] = ..., progress: _Optional[_Union[RsyncSnapTreeDiffTransmitOpCheckpoint.Progress, _Mapping]] = ..., progress_map: _Optional[_Mapping[int, RsyncSnapTreeDiffTransmitOpCheckpoint.Progress]] = ..., resolved_all_update_intents_usecs: _Optional[int] = ..., estimated_logical_bytes_to_transfer: _Optional[int] = ..., estimated_changed_entities: _Optional[int] = ..., synced_files_logical_size_sum: _Optional[int] = ..., finished_due_to_blackout: bool = ...) -> None: ...
