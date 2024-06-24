from configs import cluster_config_pb2 as _cluster_config_pb2
from bridge.quota import quota_tree_metadata_pb2 as _quota_tree_metadata_pb2
from bridge.snap_fs import snap_fs_metadata_pb2 as _snap_fs_metadata_pb2
from bridge.snap_tree import snap_tree_pb2 as _snap_tree_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ViewUsageFixerContextDataProto(_message.Message):
    __slots__ = ("cluster_config_proto", "max_view_snaptree_level", "max_dir_quota_snaptree_level")
    CLUSTER_CONFIG_PROTO_FIELD_NUMBER: _ClassVar[int]
    MAX_VIEW_SNAPTREE_LEVEL_FIELD_NUMBER: _ClassVar[int]
    MAX_DIR_QUOTA_SNAPTREE_LEVEL_FIELD_NUMBER: _ClassVar[int]
    cluster_config_proto: _cluster_config_pb2.ClusterConfigProto
    max_view_snaptree_level: int
    max_dir_quota_snaptree_level: int
    def __init__(self, cluster_config_proto: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto, _Mapping]] = ..., max_view_snaptree_level: _Optional[int] = ..., max_dir_quota_snaptree_level: _Optional[int] = ...) -> None: ...

class UserUsageFixerKeyProto(_message.Message):
    __slots__ = ("node_id", "view_id_vec", "mixed_mode_enabled", "usage_quota_snaptree_id", "user_quota_id")
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    MIXED_MODE_ENABLED_FIELD_NUMBER: _ClassVar[int]
    USAGE_QUOTA_SNAPTREE_ID_FIELD_NUMBER: _ClassVar[int]
    USER_QUOTA_ID_FIELD_NUMBER: _ClassVar[int]
    node_id: int
    view_id_vec: _containers.RepeatedScalarFieldContainer[int]
    mixed_mode_enabled: bool
    usage_quota_snaptree_id: int
    user_quota_id: _quota_tree_metadata_pb2.QuotaUID
    def __init__(self, node_id: _Optional[int] = ..., view_id_vec: _Optional[_Iterable[int]] = ..., mixed_mode_enabled: bool = ..., usage_quota_snaptree_id: _Optional[int] = ..., user_quota_id: _Optional[_Union[_quota_tree_metadata_pb2.QuotaUID, _Mapping]] = ...) -> None: ...

class ViewUsageFixerProto(_message.Message):
    __slots__ = ("user_usage_bytes", "view_id_vec", "usage_quota_snaptree_id", "include_in_view_logical_usage", "root_name", "mixed_mode_enabled", "is_internal", "num_directories", "num_regular_files", "regular_files_usage_bytes", "num_scribe_files", "scribe_files_usage_bytes", "num_minion_files", "minion_files_usage_bytes", "num_mega_files", "mega_files_usage_bytes", "num_data_fragments", "data_fragments_scribe_usage_bytes", "num_special_inodes", "user_id", "extended_attributes", "child_node_id", "user_quota_id", "user_quota_usage_version", "parent_node_id", "dir_quota_snaptree_id", "dir_quota_ids", "dir_usage_bytes", "dir_quota_usage_version", "is_walk_pending", "is_tombstone", "quota_usage_snap_tree_node_id", "file_size_distribution_map")
    class FileSizeDistributionMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    USER_USAGE_BYTES_FIELD_NUMBER: _ClassVar[int]
    VIEW_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    USAGE_QUOTA_SNAPTREE_ID_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_IN_VIEW_LOGICAL_USAGE_FIELD_NUMBER: _ClassVar[int]
    ROOT_NAME_FIELD_NUMBER: _ClassVar[int]
    MIXED_MODE_ENABLED_FIELD_NUMBER: _ClassVar[int]
    IS_INTERNAL_FIELD_NUMBER: _ClassVar[int]
    NUM_DIRECTORIES_FIELD_NUMBER: _ClassVar[int]
    NUM_REGULAR_FILES_FIELD_NUMBER: _ClassVar[int]
    REGULAR_FILES_USAGE_BYTES_FIELD_NUMBER: _ClassVar[int]
    NUM_SCRIBE_FILES_FIELD_NUMBER: _ClassVar[int]
    SCRIBE_FILES_USAGE_BYTES_FIELD_NUMBER: _ClassVar[int]
    NUM_MINION_FILES_FIELD_NUMBER: _ClassVar[int]
    MINION_FILES_USAGE_BYTES_FIELD_NUMBER: _ClassVar[int]
    NUM_MEGA_FILES_FIELD_NUMBER: _ClassVar[int]
    MEGA_FILES_USAGE_BYTES_FIELD_NUMBER: _ClassVar[int]
    NUM_DATA_FRAGMENTS_FIELD_NUMBER: _ClassVar[int]
    DATA_FRAGMENTS_SCRIBE_USAGE_BYTES_FIELD_NUMBER: _ClassVar[int]
    NUM_SPECIAL_INODES_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    EXTENDED_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    CHILD_NODE_ID_FIELD_NUMBER: _ClassVar[int]
    USER_QUOTA_ID_FIELD_NUMBER: _ClassVar[int]
    USER_QUOTA_USAGE_VERSION_FIELD_NUMBER: _ClassVar[int]
    PARENT_NODE_ID_FIELD_NUMBER: _ClassVar[int]
    DIR_QUOTA_SNAPTREE_ID_FIELD_NUMBER: _ClassVar[int]
    DIR_QUOTA_IDS_FIELD_NUMBER: _ClassVar[int]
    DIR_USAGE_BYTES_FIELD_NUMBER: _ClassVar[int]
    DIR_QUOTA_USAGE_VERSION_FIELD_NUMBER: _ClassVar[int]
    IS_WALK_PENDING_FIELD_NUMBER: _ClassVar[int]
    IS_TOMBSTONE_FIELD_NUMBER: _ClassVar[int]
    QUOTA_USAGE_SNAP_TREE_NODE_ID_FIELD_NUMBER: _ClassVar[int]
    FILE_SIZE_DISTRIBUTION_MAP_FIELD_NUMBER: _ClassVar[int]
    user_usage_bytes: int
    view_id_vec: _containers.RepeatedScalarFieldContainer[int]
    usage_quota_snaptree_id: int
    include_in_view_logical_usage: bool
    root_name: str
    mixed_mode_enabled: bool
    is_internal: bool
    num_directories: int
    num_regular_files: int
    regular_files_usage_bytes: int
    num_scribe_files: int
    scribe_files_usage_bytes: int
    num_minion_files: int
    minion_files_usage_bytes: int
    num_mega_files: int
    mega_files_usage_bytes: int
    num_data_fragments: int
    data_fragments_scribe_usage_bytes: int
    num_special_inodes: int
    user_id: int
    extended_attributes: _snap_fs_metadata_pb2.InodeMetadataProto.ExtendedAttributes
    child_node_id: int
    user_quota_id: _quota_tree_metadata_pb2.QuotaUID
    user_quota_usage_version: _snap_tree_pb2.SnapTreeValueVersionProto
    parent_node_id: int
    dir_quota_snaptree_id: int
    dir_quota_ids: _containers.RepeatedScalarFieldContainer[int]
    dir_usage_bytes: int
    dir_quota_usage_version: _snap_tree_pb2.SnapTreeValueVersionProto
    is_walk_pending: bool
    is_tombstone: bool
    quota_usage_snap_tree_node_id: int
    file_size_distribution_map: _containers.ScalarMap[str, int]
    def __init__(self, user_usage_bytes: _Optional[int] = ..., view_id_vec: _Optional[_Iterable[int]] = ..., usage_quota_snaptree_id: _Optional[int] = ..., include_in_view_logical_usage: bool = ..., root_name: _Optional[str] = ..., mixed_mode_enabled: bool = ..., is_internal: bool = ..., num_directories: _Optional[int] = ..., num_regular_files: _Optional[int] = ..., regular_files_usage_bytes: _Optional[int] = ..., num_scribe_files: _Optional[int] = ..., scribe_files_usage_bytes: _Optional[int] = ..., num_minion_files: _Optional[int] = ..., minion_files_usage_bytes: _Optional[int] = ..., num_mega_files: _Optional[int] = ..., mega_files_usage_bytes: _Optional[int] = ..., num_data_fragments: _Optional[int] = ..., data_fragments_scribe_usage_bytes: _Optional[int] = ..., num_special_inodes: _Optional[int] = ..., user_id: _Optional[int] = ..., extended_attributes: _Optional[_Union[_snap_fs_metadata_pb2.InodeMetadataProto.ExtendedAttributes, _Mapping]] = ..., child_node_id: _Optional[int] = ..., user_quota_id: _Optional[_Union[_quota_tree_metadata_pb2.QuotaUID, _Mapping]] = ..., user_quota_usage_version: _Optional[_Union[_snap_tree_pb2.SnapTreeValueVersionProto, _Mapping]] = ..., parent_node_id: _Optional[int] = ..., dir_quota_snaptree_id: _Optional[int] = ..., dir_quota_ids: _Optional[_Iterable[int]] = ..., dir_usage_bytes: _Optional[int] = ..., dir_quota_usage_version: _Optional[_Union[_snap_tree_pb2.SnapTreeValueVersionProto, _Mapping]] = ..., is_walk_pending: bool = ..., is_tombstone: bool = ..., quota_usage_snap_tree_node_id: _Optional[int] = ..., file_size_distribution_map: _Optional[_Mapping[str, int]] = ...) -> None: ...

class DirUsageFixerKeyProto(_message.Message):
    __slots__ = ("node_id", "view_id_vec", "dir_quota_snaptree_id", "dir_quota_id")
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    DIR_QUOTA_SNAPTREE_ID_FIELD_NUMBER: _ClassVar[int]
    DIR_QUOTA_ID_FIELD_NUMBER: _ClassVar[int]
    node_id: int
    view_id_vec: _containers.RepeatedScalarFieldContainer[int]
    dir_quota_snaptree_id: int
    dir_quota_id: int
    def __init__(self, node_id: _Optional[int] = ..., view_id_vec: _Optional[_Iterable[int]] = ..., dir_quota_snaptree_id: _Optional[int] = ..., dir_quota_id: _Optional[int] = ...) -> None: ...
