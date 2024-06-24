from configs import cluster_config_pb2 as _cluster_config_pb2
from bridge.snap_tree import snap_tree_pb2 as _snap_tree_pb2
from bridge.snap_fs import snap_fs_metadata_pb2 as _snap_fs_metadata_pb2
from bridge.view_keeper import view_metadata_pb2 as _view_metadata_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ViewSnapTreeFixerContextDataProto(_message.Message):
    __slots__ = ("cluster_config_proto", "max_view_snaptree_level", "enable_orphan_entity_gc", "enable_lazy_directory_deletion", "enable_s3lc_fixer_pipeline", "s3lc_inode_bucket", "enable_delete_orphan_s3_inodes_with_intents", "create_separate_scanner_for_each_vst_level")
    CLUSTER_CONFIG_PROTO_FIELD_NUMBER: _ClassVar[int]
    MAX_VIEW_SNAPTREE_LEVEL_FIELD_NUMBER: _ClassVar[int]
    ENABLE_ORPHAN_ENTITY_GC_FIELD_NUMBER: _ClassVar[int]
    ENABLE_LAZY_DIRECTORY_DELETION_FIELD_NUMBER: _ClassVar[int]
    ENABLE_S3LC_FIXER_PIPELINE_FIELD_NUMBER: _ClassVar[int]
    S3LC_INODE_BUCKET_FIELD_NUMBER: _ClassVar[int]
    ENABLE_DELETE_ORPHAN_S3_INODES_WITH_INTENTS_FIELD_NUMBER: _ClassVar[int]
    CREATE_SEPARATE_SCANNER_FOR_EACH_VST_LEVEL_FIELD_NUMBER: _ClassVar[int]
    cluster_config_proto: _cluster_config_pb2.ClusterConfigProto
    max_view_snaptree_level: int
    enable_orphan_entity_gc: bool
    enable_lazy_directory_deletion: bool
    enable_s3lc_fixer_pipeline: bool
    s3lc_inode_bucket: int
    enable_delete_orphan_s3_inodes_with_intents: bool
    create_separate_scanner_for_each_vst_level: bool
    def __init__(self, cluster_config_proto: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto, _Mapping]] = ..., max_view_snaptree_level: _Optional[int] = ..., enable_orphan_entity_gc: bool = ..., enable_lazy_directory_deletion: bool = ..., enable_s3lc_fixer_pipeline: bool = ..., s3lc_inode_bucket: _Optional[int] = ..., enable_delete_orphan_s3_inodes_with_intents: bool = ..., create_separate_scanner_for_each_vst_level: bool = ...) -> None: ...

class ViewSnapTreeIntentFixerInfo(_message.Message):
    __slots__ = ("snap_fs_intent", "s3_intent", "snap_fs_intent_id", "s3_empty_dir_deletion")
    class IntentId(_message.Message):
        __slots__ = ("intent_id_high", "intent_id_low")
        INTENT_ID_HIGH_FIELD_NUMBER: _ClassVar[int]
        INTENT_ID_LOW_FIELD_NUMBER: _ClassVar[int]
        intent_id_high: int
        intent_id_low: int
        def __init__(self, intent_id_high: _Optional[int] = ..., intent_id_low: _Optional[int] = ...) -> None: ...
    SNAP_FS_INTENT_FIELD_NUMBER: _ClassVar[int]
    S3_INTENT_FIELD_NUMBER: _ClassVar[int]
    SNAP_FS_INTENT_ID_FIELD_NUMBER: _ClassVar[int]
    S3_EMPTY_DIR_DELETION_FIELD_NUMBER: _ClassVar[int]
    snap_fs_intent: bool
    s3_intent: bool
    snap_fs_intent_id: ViewSnapTreeIntentFixerInfo.IntentId
    s3_empty_dir_deletion: bool
    def __init__(self, snap_fs_intent: bool = ..., s3_intent: bool = ..., snap_fs_intent_id: _Optional[_Union[ViewSnapTreeIntentFixerInfo.IntentId, _Mapping]] = ..., s3_empty_dir_deletion: bool = ...) -> None: ...

class EntityGCInfo(_message.Message):
    __slots__ = ("owner_inode_id", "is_data_fragment")
    OWNER_INODE_ID_FIELD_NUMBER: _ClassVar[int]
    IS_DATA_FRAGMENT_FIELD_NUMBER: _ClassVar[int]
    owner_inode_id: int
    is_data_fragment: bool
    def __init__(self, owner_inode_id: _Optional[int] = ..., is_data_fragment: bool = ...) -> None: ...

class AsyncDeleteInfo(_message.Message):
    __slots__ = ("value_version", "owner_inode_id")
    VALUE_VERSION_FIELD_NUMBER: _ClassVar[int]
    OWNER_INODE_ID_FIELD_NUMBER: _ClassVar[int]
    value_version: _snap_tree_pb2.SnapTreeValueVersionProto
    owner_inode_id: int
    def __init__(self, value_version: _Optional[_Union[_snap_tree_pb2.SnapTreeValueVersionProto, _Mapping]] = ..., owner_inode_id: _Optional[int] = ...) -> None: ...

class ViewSnapTreeFixerProto(_message.Message):
    __slots__ = ("entity_id", "node_id", "fix_intent_info", "entity_info", "parent_node_id", "view_id", "root_inode_id", "namespace_fixing_disabled", "orphan_entities_deletion_disabled", "op_in_progress", "value_version_count", "view_creation_time_usecs", "async_delete_info", "num_garbage_data_fragments", "num_garbage_dir_embedded_data_fragments", "is_root_inode_id", "mapped_from_view_usage_table", "num_orphan_entities", "num_orphan_fragments", "is_internal", "update_view_usage_table", "is_s3_view_with_empty_dir_deletion", "publish_gc_stats")
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    FIX_INTENT_INFO_FIELD_NUMBER: _ClassVar[int]
    ENTITY_INFO_FIELD_NUMBER: _ClassVar[int]
    PARENT_NODE_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_ID_FIELD_NUMBER: _ClassVar[int]
    ROOT_INODE_ID_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIXING_DISABLED_FIELD_NUMBER: _ClassVar[int]
    ORPHAN_ENTITIES_DELETION_DISABLED_FIELD_NUMBER: _ClassVar[int]
    OP_IN_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    VALUE_VERSION_COUNT_FIELD_NUMBER: _ClassVar[int]
    VIEW_CREATION_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    ASYNC_DELETE_INFO_FIELD_NUMBER: _ClassVar[int]
    NUM_GARBAGE_DATA_FRAGMENTS_FIELD_NUMBER: _ClassVar[int]
    NUM_GARBAGE_DIR_EMBEDDED_DATA_FRAGMENTS_FIELD_NUMBER: _ClassVar[int]
    IS_ROOT_INODE_ID_FIELD_NUMBER: _ClassVar[int]
    MAPPED_FROM_VIEW_USAGE_TABLE_FIELD_NUMBER: _ClassVar[int]
    NUM_ORPHAN_ENTITIES_FIELD_NUMBER: _ClassVar[int]
    NUM_ORPHAN_FRAGMENTS_FIELD_NUMBER: _ClassVar[int]
    IS_INTERNAL_FIELD_NUMBER: _ClassVar[int]
    UPDATE_VIEW_USAGE_TABLE_FIELD_NUMBER: _ClassVar[int]
    IS_S3_VIEW_WITH_EMPTY_DIR_DELETION_FIELD_NUMBER: _ClassVar[int]
    PUBLISH_GC_STATS_FIELD_NUMBER: _ClassVar[int]
    entity_id: int
    node_id: int
    fix_intent_info: ViewSnapTreeIntentFixerInfo
    entity_info: EntityGCInfo
    parent_node_id: int
    view_id: int
    root_inode_id: int
    namespace_fixing_disabled: bool
    orphan_entities_deletion_disabled: bool
    op_in_progress: bool
    value_version_count: int
    view_creation_time_usecs: int
    async_delete_info: AsyncDeleteInfo
    num_garbage_data_fragments: int
    num_garbage_dir_embedded_data_fragments: int
    is_root_inode_id: int
    mapped_from_view_usage_table: bool
    num_orphan_entities: int
    num_orphan_fragments: int
    is_internal: int
    update_view_usage_table: bool
    is_s3_view_with_empty_dir_deletion: bool
    publish_gc_stats: bool
    def __init__(self, entity_id: _Optional[int] = ..., node_id: _Optional[int] = ..., fix_intent_info: _Optional[_Union[ViewSnapTreeIntentFixerInfo, _Mapping]] = ..., entity_info: _Optional[_Union[EntityGCInfo, _Mapping]] = ..., parent_node_id: _Optional[int] = ..., view_id: _Optional[int] = ..., root_inode_id: _Optional[int] = ..., namespace_fixing_disabled: bool = ..., orphan_entities_deletion_disabled: bool = ..., op_in_progress: bool = ..., value_version_count: _Optional[int] = ..., view_creation_time_usecs: _Optional[int] = ..., async_delete_info: _Optional[_Union[AsyncDeleteInfo, _Mapping]] = ..., num_garbage_data_fragments: _Optional[int] = ..., num_garbage_dir_embedded_data_fragments: _Optional[int] = ..., is_root_inode_id: _Optional[int] = ..., mapped_from_view_usage_table: bool = ..., num_orphan_entities: _Optional[int] = ..., num_orphan_fragments: _Optional[int] = ..., is_internal: _Optional[int] = ..., update_view_usage_table: bool = ..., is_s3_view_with_empty_dir_deletion: bool = ..., publish_gc_stats: bool = ...) -> None: ...

class S3LifeCycleFixerKeyProto(_message.Message):
    __slots__ = ("view_id", "inode_bucket_id", "node_id")
    VIEW_ID_FIELD_NUMBER: _ClassVar[int]
    INODE_BUCKET_ID_FIELD_NUMBER: _ClassVar[int]
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    view_id: int
    inode_bucket_id: int
    node_id: int
    def __init__(self, view_id: _Optional[int] = ..., inode_bucket_id: _Optional[int] = ..., node_id: _Optional[int] = ...) -> None: ...

class S3LifeCycleFixerValueProto(_message.Message):
    __slots__ = ("view_id_vec", "child_node_id_vec", "inode_metadata", "view_id_mapping")
    VIEW_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    CHILD_NODE_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    INODE_METADATA_FIELD_NUMBER: _ClassVar[int]
    VIEW_ID_MAPPING_FIELD_NUMBER: _ClassVar[int]
    view_id_vec: _containers.RepeatedScalarFieldContainer[int]
    child_node_id_vec: _containers.RepeatedScalarFieldContainer[int]
    inode_metadata: _snap_fs_metadata_pb2.InodeMetadataProto
    view_id_mapping: _view_metadata_pb2.ViewIdMappingProto
    def __init__(self, view_id_vec: _Optional[_Iterable[int]] = ..., child_node_id_vec: _Optional[_Iterable[int]] = ..., inode_metadata: _Optional[_Union[_snap_fs_metadata_pb2.InodeMetadataProto, _Mapping]] = ..., view_id_mapping: _Optional[_Union[_view_metadata_pb2.ViewIdMappingProto, _Mapping]] = ...) -> None: ...
