from bookkeeper.v2.base import bookkeeper_v2_pb2 as _bookkeeper_v2_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ViewUsageProto(_message.Message):
    __slots__ = ("usage_bytes", "namespace_usage_map", "view_stats_proto", "extension_stats_map", "async_delete_stats", "file_size_distribution_map", "orphan_entity_stats", "physical_stats", "filer_lcm_stats")
    class NameSpaceUsageProto(_message.Message):
        __slots__ = ("num_directories", "num_regular_files", "regular_files_usage_bytes", "num_scribe_files", "scribe_files_usage_bytes", "num_minion_files", "minion_files_usage_bytes", "num_mega_files", "mega_files_usage_bytes", "num_data_fragments", "data_fragments_scribe_usage_bytes", "num_special_inodes", "is_relevant_namespace")
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
        IS_RELEVANT_NAMESPACE_FIELD_NUMBER: _ClassVar[int]
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
        is_relevant_namespace: bool
        def __init__(self, num_directories: _Optional[int] = ..., num_regular_files: _Optional[int] = ..., regular_files_usage_bytes: _Optional[int] = ..., num_scribe_files: _Optional[int] = ..., scribe_files_usage_bytes: _Optional[int] = ..., num_minion_files: _Optional[int] = ..., minion_files_usage_bytes: _Optional[int] = ..., num_mega_files: _Optional[int] = ..., mega_files_usage_bytes: _Optional[int] = ..., num_data_fragments: _Optional[int] = ..., data_fragments_scribe_usage_bytes: _Optional[int] = ..., num_special_inodes: _Optional[int] = ..., is_relevant_namespace: bool = ...) -> None: ...
    class NamespaceUsageMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: ViewUsageProto.NameSpaceUsageProto
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[ViewUsageProto.NameSpaceUsageProto, _Mapping]] = ...) -> None: ...
    class ViewStatsProto(_message.Message):
        __slots__ = ("chunk_physical_bytes", "chunk_logical_bytes", "chunk_morphed_bytes", "inode_logical_bytes", "brick_bytes_logical", "unique_chunk_bytes_logical", "unique_chunk_bytes_physical", "unique_chunk_bytes_morphed", "unique_chunk_bytes_morphed_local", "unique_chunk_bytes_morphed_cloud", "unique_chunk_bytes_physical_cloud", "unique_chunk_bytes_physical_local")
        CHUNK_PHYSICAL_BYTES_FIELD_NUMBER: _ClassVar[int]
        CHUNK_LOGICAL_BYTES_FIELD_NUMBER: _ClassVar[int]
        CHUNK_MORPHED_BYTES_FIELD_NUMBER: _ClassVar[int]
        INODE_LOGICAL_BYTES_FIELD_NUMBER: _ClassVar[int]
        BRICK_BYTES_LOGICAL_FIELD_NUMBER: _ClassVar[int]
        UNIQUE_CHUNK_BYTES_LOGICAL_FIELD_NUMBER: _ClassVar[int]
        UNIQUE_CHUNK_BYTES_PHYSICAL_FIELD_NUMBER: _ClassVar[int]
        UNIQUE_CHUNK_BYTES_MORPHED_FIELD_NUMBER: _ClassVar[int]
        UNIQUE_CHUNK_BYTES_MORPHED_LOCAL_FIELD_NUMBER: _ClassVar[int]
        UNIQUE_CHUNK_BYTES_MORPHED_CLOUD_FIELD_NUMBER: _ClassVar[int]
        UNIQUE_CHUNK_BYTES_PHYSICAL_CLOUD_FIELD_NUMBER: _ClassVar[int]
        UNIQUE_CHUNK_BYTES_PHYSICAL_LOCAL_FIELD_NUMBER: _ClassVar[int]
        chunk_physical_bytes: int
        chunk_logical_bytes: int
        chunk_morphed_bytes: int
        inode_logical_bytes: int
        brick_bytes_logical: int
        unique_chunk_bytes_logical: int
        unique_chunk_bytes_physical: int
        unique_chunk_bytes_morphed: int
        unique_chunk_bytes_morphed_local: int
        unique_chunk_bytes_morphed_cloud: int
        unique_chunk_bytes_physical_cloud: int
        unique_chunk_bytes_physical_local: int
        def __init__(self, chunk_physical_bytes: _Optional[int] = ..., chunk_logical_bytes: _Optional[int] = ..., chunk_morphed_bytes: _Optional[int] = ..., inode_logical_bytes: _Optional[int] = ..., brick_bytes_logical: _Optional[int] = ..., unique_chunk_bytes_logical: _Optional[int] = ..., unique_chunk_bytes_physical: _Optional[int] = ..., unique_chunk_bytes_morphed: _Optional[int] = ..., unique_chunk_bytes_morphed_local: _Optional[int] = ..., unique_chunk_bytes_morphed_cloud: _Optional[int] = ..., unique_chunk_bytes_physical_cloud: _Optional[int] = ..., unique_chunk_bytes_physical_local: _Optional[int] = ...) -> None: ...
    class ExtensionStatsProto(_message.Message):
        __slots__ = ("logical_bytes", "num_files")
        LOGICAL_BYTES_FIELD_NUMBER: _ClassVar[int]
        NUM_FILES_FIELD_NUMBER: _ClassVar[int]
        logical_bytes: int
        num_files: int
        def __init__(self, logical_bytes: _Optional[int] = ..., num_files: _Optional[int] = ...) -> None: ...
    class ExtensionStatsMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: ViewUsageProto.ExtensionStatsProto
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[ViewUsageProto.ExtensionStatsProto, _Mapping]] = ...) -> None: ...
    class AsyncDeleteStats(_message.Message):
        __slots__ = ("num_garbage_data_fragments", "num_garbage_dir_embedded_data_fragments", "last_update_timestamp_usecs")
        NUM_GARBAGE_DATA_FRAGMENTS_FIELD_NUMBER: _ClassVar[int]
        NUM_GARBAGE_DIR_EMBEDDED_DATA_FRAGMENTS_FIELD_NUMBER: _ClassVar[int]
        LAST_UPDATE_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
        num_garbage_data_fragments: int
        num_garbage_dir_embedded_data_fragments: int
        last_update_timestamp_usecs: int
        def __init__(self, num_garbage_data_fragments: _Optional[int] = ..., num_garbage_dir_embedded_data_fragments: _Optional[int] = ..., last_update_timestamp_usecs: _Optional[int] = ...) -> None: ...
    class FileSizeDistributionMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    class OrphanEntityStats(_message.Message):
        __slots__ = ("num_orphan_fragments", "num_orphan_entities", "last_update_timestamp_usecs")
        NUM_ORPHAN_FRAGMENTS_FIELD_NUMBER: _ClassVar[int]
        NUM_ORPHAN_ENTITIES_FIELD_NUMBER: _ClassVar[int]
        LAST_UPDATE_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
        num_orphan_fragments: int
        num_orphan_entities: int
        last_update_timestamp_usecs: int
        def __init__(self, num_orphan_fragments: _Optional[int] = ..., num_orphan_entities: _Optional[int] = ..., last_update_timestamp_usecs: _Optional[int] = ...) -> None: ...
    class FilerLcmStats(_message.Message):
        __slots__ = ("number_of_lcm_qualifying_files", "number_of_lcm_qualifying_directories", "number_of_lcm_actions_needed", "last_update_timestamp_usecs")
        NUMBER_OF_LCM_QUALIFYING_FILES_FIELD_NUMBER: _ClassVar[int]
        NUMBER_OF_LCM_QUALIFYING_DIRECTORIES_FIELD_NUMBER: _ClassVar[int]
        NUMBER_OF_LCM_ACTIONS_NEEDED_FIELD_NUMBER: _ClassVar[int]
        LAST_UPDATE_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
        number_of_lcm_qualifying_files: int
        number_of_lcm_qualifying_directories: int
        number_of_lcm_actions_needed: int
        last_update_timestamp_usecs: int
        def __init__(self, number_of_lcm_qualifying_files: _Optional[int] = ..., number_of_lcm_qualifying_directories: _Optional[int] = ..., number_of_lcm_actions_needed: _Optional[int] = ..., last_update_timestamp_usecs: _Optional[int] = ...) -> None: ...
    USAGE_BYTES_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_USAGE_MAP_FIELD_NUMBER: _ClassVar[int]
    VIEW_STATS_PROTO_FIELD_NUMBER: _ClassVar[int]
    EXTENSION_STATS_MAP_FIELD_NUMBER: _ClassVar[int]
    ASYNC_DELETE_STATS_FIELD_NUMBER: _ClassVar[int]
    FILE_SIZE_DISTRIBUTION_MAP_FIELD_NUMBER: _ClassVar[int]
    ORPHAN_ENTITY_STATS_FIELD_NUMBER: _ClassVar[int]
    PHYSICAL_STATS_FIELD_NUMBER: _ClassVar[int]
    FILER_LCM_STATS_FIELD_NUMBER: _ClassVar[int]
    usage_bytes: int
    namespace_usage_map: _containers.MessageMap[str, ViewUsageProto.NameSpaceUsageProto]
    view_stats_proto: ViewUsageProto.ViewStatsProto
    extension_stats_map: _containers.MessageMap[str, ViewUsageProto.ExtensionStatsProto]
    async_delete_stats: ViewUsageProto.AsyncDeleteStats
    file_size_distribution_map: _containers.ScalarMap[str, int]
    orphan_entity_stats: ViewUsageProto.OrphanEntityStats
    physical_stats: _bookkeeper_v2_pb2.PhysicalStats
    filer_lcm_stats: ViewUsageProto.FilerLcmStats
    def __init__(self, usage_bytes: _Optional[int] = ..., namespace_usage_map: _Optional[_Mapping[str, ViewUsageProto.NameSpaceUsageProto]] = ..., view_stats_proto: _Optional[_Union[ViewUsageProto.ViewStatsProto, _Mapping]] = ..., extension_stats_map: _Optional[_Mapping[str, ViewUsageProto.ExtensionStatsProto]] = ..., async_delete_stats: _Optional[_Union[ViewUsageProto.AsyncDeleteStats, _Mapping]] = ..., file_size_distribution_map: _Optional[_Mapping[str, int]] = ..., orphan_entity_stats: _Optional[_Union[ViewUsageProto.OrphanEntityStats, _Mapping]] = ..., physical_stats: _Optional[_Union[_bookkeeper_v2_pb2.PhysicalStats, _Mapping]] = ..., filer_lcm_stats: _Optional[_Union[ViewUsageProto.FilerLcmStats, _Mapping]] = ...) -> None: ...
