from bridge.base import cloud_pb2 as _cloud_pb2
from apollo.mr.base import histogram_proto_pb2 as _histogram_proto_pb2
from bookkeeper.base import bookkeeper_pb2 as _bookkeeper_pb2
from bookkeeper.v2.base import bookkeeper_v2_pb2 as _bookkeeper_v2_pb2
from bookkeeper.v2.base import bookkeeper_v2_special_groups_pb2 as _bookkeeper_v2_special_groups_pb2
from bridge.apollo import actions_v2_pb2 as _actions_v2_pb2
from bridge.icebox.master.stub import rpc_service_pb2 as _rpc_service_pb2
from bridge.blob_store import blob_store_pb2 as _blob_store_pb2
from bridge.snap_fs import entity_handle_pb2 as _entity_handle_pb2
from bridge.view_keeper import view_usage_pb2 as _view_usage_pb2
from configs import cluster_config_pb2 as _cluster_config_pb2
from util.base import op_clock_pb2 as _op_clock_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ActionMetadataProto(_message.Message):
    __slots__ = ("view_box_id", "action_utility_score", "chunk_logical_bytes", "owner_blob_id", "priority", "node_id", "view_id")
    VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
    ACTION_UTILITY_SCORE_FIELD_NUMBER: _ClassVar[int]
    CHUNK_LOGICAL_BYTES_FIELD_NUMBER: _ClassVar[int]
    OWNER_BLOB_ID_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_ID_FIELD_NUMBER: _ClassVar[int]
    view_box_id: int
    action_utility_score: int
    chunk_logical_bytes: int
    owner_blob_id: int
    priority: int
    node_id: int
    view_id: int
    def __init__(self, view_box_id: _Optional[int] = ..., action_utility_score: _Optional[int] = ..., chunk_logical_bytes: _Optional[int] = ..., owner_blob_id: _Optional[int] = ..., priority: _Optional[int] = ..., node_id: _Optional[int] = ..., view_id: _Optional[int] = ...) -> None: ...

class ScribeTableProto(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kChunkMetadata: _ClassVar[ScribeTableProto.Type]
        kChunkFileAccess: _ClassVar[ScribeTableProto.Type]
        kBlobSnaptree: _ClassVar[ScribeTableProto.Type]
        kBlobMetadata: _ClassVar[ScribeTableProto.Type]
        kViewSnaptree: _ClassVar[ScribeTableProto.Type]
        kViewMetadata: _ClassVar[ScribeTableProto.Type]
        kChunkFileMetadata: _ClassVar[ScribeTableProto.Type]
        kSmbSessionMetadata: _ClassVar[ScribeTableProto.Type]
        kSmbEntityMetadata: _ClassVar[ScribeTableProto.Type]
        kIceboxArchiveMetadata: _ClassVar[ScribeTableProto.Type]
        kIceboxChunkLocation: _ClassVar[ScribeTableProto.Type]
        kIceboxSnapTreeNodeLocation: _ClassVar[ScribeTableProto.Type]
        kIceboxRestoredSnapTreeNodeLocation: _ClassVar[ScribeTableProto.Type]
        kIceboxRestoreJobMetadata: _ClassVar[ScribeTableProto.Type]
        kViewUsage: _ClassVar[ScribeTableProto.Type]
        kQuotaSnapTree: _ClassVar[ScribeTableProto.Type]
        kQuotaUsageSnapTree: _ClassVar[ScribeTableProto.Type]
        kChunkRepoMetadata: _ClassVar[ScribeTableProto.Type]
        kAntivirusSnapTree: _ClassVar[ScribeTableProto.Type]
        kIceboxRestoredHardlinks: _ClassVar[ScribeTableProto.Type]
        kBookkeeperMetadata: _ClassVar[ScribeTableProto.Type]
        kDirQuotaSnapTree: _ClassVar[ScribeTableProto.Type]
        kShadowCopySetContext: _ClassVar[ScribeTableProto.Type]
        kNFSv4Metadata: _ClassVar[ScribeTableProto.Type]
        kStatsTimeSeries: _ClassVar[ScribeTableProto.Type]
        kStatsAggrTimeSeries: _ClassVar[ScribeTableProto.Type]
        kStatsEntity: _ClassVar[ScribeTableProto.Type]
        kStatsEntitySchema: _ClassVar[ScribeTableProto.Type]
        kStatsCounters: _ClassVar[ScribeTableProto.Type]
        kStatsContainers: _ClassVar[ScribeTableProto.Type]
        kCloudChunkFileMetadata: _ClassVar[ScribeTableProto.Type]
        kCloudObjectMetadata: _ClassVar[ScribeTableProto.Type]
        kIceboxStubViewMetadata: _ClassVar[ScribeTableProto.Type]
        kChunkFileContainerMetadata: _ClassVar[ScribeTableProto.Type]
        kS3ObjectSnapTree: _ClassVar[ScribeTableProto.Type]
        kBookkeeperV2Groups: _ClassVar[ScribeTableProto.Type]
        kBookkeeperV2Entities: _ClassVar[ScribeTableProto.Type]
        kInvalidArchivedNodes: _ClassVar[ScribeTableProto.Type]
        kInvalidArchivedChunks: _ClassVar[ScribeTableProto.Type]
        kInvalidCloudLocations: _ClassVar[ScribeTableProto.Type]
        kBookkeeperV2Queries: _ClassVar[ScribeTableProto.Type]
        kQueryMrResultData: _ClassVar[ScribeTableProto.Type]
        kApolloMrTestTable_1: _ClassVar[ScribeTableProto.Type]
        kApolloMrTestTable_2: _ClassVar[ScribeTableProto.Type]
        kApolloMrTestTable_3: _ClassVar[ScribeTableProto.Type]
    kChunkMetadata: ScribeTableProto.Type
    kChunkFileAccess: ScribeTableProto.Type
    kBlobSnaptree: ScribeTableProto.Type
    kBlobMetadata: ScribeTableProto.Type
    kViewSnaptree: ScribeTableProto.Type
    kViewMetadata: ScribeTableProto.Type
    kChunkFileMetadata: ScribeTableProto.Type
    kSmbSessionMetadata: ScribeTableProto.Type
    kSmbEntityMetadata: ScribeTableProto.Type
    kIceboxArchiveMetadata: ScribeTableProto.Type
    kIceboxChunkLocation: ScribeTableProto.Type
    kIceboxSnapTreeNodeLocation: ScribeTableProto.Type
    kIceboxRestoredSnapTreeNodeLocation: ScribeTableProto.Type
    kIceboxRestoreJobMetadata: ScribeTableProto.Type
    kViewUsage: ScribeTableProto.Type
    kQuotaSnapTree: ScribeTableProto.Type
    kQuotaUsageSnapTree: ScribeTableProto.Type
    kChunkRepoMetadata: ScribeTableProto.Type
    kAntivirusSnapTree: ScribeTableProto.Type
    kIceboxRestoredHardlinks: ScribeTableProto.Type
    kBookkeeperMetadata: ScribeTableProto.Type
    kDirQuotaSnapTree: ScribeTableProto.Type
    kShadowCopySetContext: ScribeTableProto.Type
    kNFSv4Metadata: ScribeTableProto.Type
    kStatsTimeSeries: ScribeTableProto.Type
    kStatsAggrTimeSeries: ScribeTableProto.Type
    kStatsEntity: ScribeTableProto.Type
    kStatsEntitySchema: ScribeTableProto.Type
    kStatsCounters: ScribeTableProto.Type
    kStatsContainers: ScribeTableProto.Type
    kCloudChunkFileMetadata: ScribeTableProto.Type
    kCloudObjectMetadata: ScribeTableProto.Type
    kIceboxStubViewMetadata: ScribeTableProto.Type
    kChunkFileContainerMetadata: ScribeTableProto.Type
    kS3ObjectSnapTree: ScribeTableProto.Type
    kBookkeeperV2Groups: ScribeTableProto.Type
    kBookkeeperV2Entities: ScribeTableProto.Type
    kInvalidArchivedNodes: ScribeTableProto.Type
    kInvalidArchivedChunks: ScribeTableProto.Type
    kInvalidCloudLocations: ScribeTableProto.Type
    kBookkeeperV2Queries: ScribeTableProto.Type
    kQueryMrResultData: ScribeTableProto.Type
    kApolloMrTestTable_1: ScribeTableProto.Type
    kApolloMrTestTable_2: ScribeTableProto.Type
    kApolloMrTestTable_3: ScribeTableProto.Type
    def __init__(self) -> None: ...

class SnapTreeChildReferenceInfoProto(_message.Message):
    __slots__ = ("child_table", "child_node_id", "parent_info_vec", "raise_fatal_error")
    class ParentInfo(_message.Message):
        __slots__ = ("table", "key", "eh")
        TABLE_FIELD_NUMBER: _ClassVar[int]
        KEY_FIELD_NUMBER: _ClassVar[int]
        EH_FIELD_NUMBER: _ClassVar[int]
        table: ScribeTableProto.Type
        key: int
        eh: _entity_handle_pb2.EntityHandleProto
        def __init__(self, table: _Optional[_Union[ScribeTableProto.Type, str]] = ..., key: _Optional[int] = ..., eh: _Optional[_Union[_entity_handle_pb2.EntityHandleProto, _Mapping]] = ...) -> None: ...
    CHILD_TABLE_FIELD_NUMBER: _ClassVar[int]
    CHILD_NODE_ID_FIELD_NUMBER: _ClassVar[int]
    PARENT_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    RAISE_FATAL_ERROR_FIELD_NUMBER: _ClassVar[int]
    child_table: ScribeTableProto.Type
    child_node_id: int
    parent_info_vec: _containers.RepeatedCompositeFieldContainer[SnapTreeChildReferenceInfoProto.ParentInfo]
    raise_fatal_error: bool
    def __init__(self, child_table: _Optional[_Union[ScribeTableProto.Type, str]] = ..., child_node_id: _Optional[int] = ..., parent_info_vec: _Optional[_Iterable[_Union[SnapTreeChildReferenceInfoProto.ParentInfo, _Mapping]]] = ..., raise_fatal_error: bool = ...) -> None: ...

class ChunkReferenceInfoProto(_message.Message):
    __slots__ = ("chunk_id", "brick_snap_tree_node_id", "raise_fatal_error")
    CHUNK_ID_FIELD_NUMBER: _ClassVar[int]
    BRICK_SNAP_TREE_NODE_ID_FIELD_NUMBER: _ClassVar[int]
    RAISE_FATAL_ERROR_FIELD_NUMBER: _ClassVar[int]
    chunk_id: _blob_store_pb2.ChunkIdProto
    brick_snap_tree_node_id: int
    raise_fatal_error: bool
    def __init__(self, chunk_id: _Optional[_Union[_blob_store_pb2.ChunkIdProto, _Mapping]] = ..., brick_snap_tree_node_id: _Optional[int] = ..., raise_fatal_error: bool = ...) -> None: ...

class InsertDeleteScribeRowProto(_message.Message):
    __slots__ = ("is_delete", "table", "version", "integer_row_key", "string_row_key", "column_data_vec", "insert_retry_count", "set_opclock_vec", "expect_opclock_vec")
    class ColumnData(_message.Message):
        __slots__ = ("integer_key", "string_key", "data", "merge_info")
        class MergeInfo(_message.Message):
            __slots__ = ("protobuf_message_type",)
            PROTOBUF_MESSAGE_TYPE_FIELD_NUMBER: _ClassVar[int]
            protobuf_message_type: str
            def __init__(self, protobuf_message_type: _Optional[str] = ...) -> None: ...
        INTEGER_KEY_FIELD_NUMBER: _ClassVar[int]
        STRING_KEY_FIELD_NUMBER: _ClassVar[int]
        DATA_FIELD_NUMBER: _ClassVar[int]
        MERGE_INFO_FIELD_NUMBER: _ClassVar[int]
        integer_key: int
        string_key: str
        data: bytes
        merge_info: InsertDeleteScribeRowProto.ColumnData.MergeInfo
        def __init__(self, integer_key: _Optional[int] = ..., string_key: _Optional[str] = ..., data: _Optional[bytes] = ..., merge_info: _Optional[_Union[InsertDeleteScribeRowProto.ColumnData.MergeInfo, _Mapping]] = ...) -> None: ...
    IS_DELETE_FIELD_NUMBER: _ClassVar[int]
    TABLE_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    INTEGER_ROW_KEY_FIELD_NUMBER: _ClassVar[int]
    STRING_ROW_KEY_FIELD_NUMBER: _ClassVar[int]
    COLUMN_DATA_VEC_FIELD_NUMBER: _ClassVar[int]
    INSERT_RETRY_COUNT_FIELD_NUMBER: _ClassVar[int]
    SET_OPCLOCK_VEC_FIELD_NUMBER: _ClassVar[int]
    EXPECT_OPCLOCK_VEC_FIELD_NUMBER: _ClassVar[int]
    is_delete: bool
    table: ScribeTableProto.Type
    version: int
    integer_row_key: int
    string_row_key: str
    column_data_vec: _containers.RepeatedCompositeFieldContainer[InsertDeleteScribeRowProto.ColumnData]
    insert_retry_count: int
    set_opclock_vec: _containers.RepeatedCompositeFieldContainer[_op_clock_pb2.OpClock]
    expect_opclock_vec: _containers.RepeatedCompositeFieldContainer[_op_clock_pb2.OpClock]
    def __init__(self, is_delete: bool = ..., table: _Optional[_Union[ScribeTableProto.Type, str]] = ..., version: _Optional[int] = ..., integer_row_key: _Optional[int] = ..., string_row_key: _Optional[str] = ..., column_data_vec: _Optional[_Iterable[_Union[InsertDeleteScribeRowProto.ColumnData, _Mapping]]] = ..., insert_retry_count: _Optional[int] = ..., set_opclock_vec: _Optional[_Iterable[_Union[_op_clock_pb2.OpClock, _Mapping]]] = ..., expect_opclock_vec: _Optional[_Iterable[_Union[_op_clock_pb2.OpClock, _Mapping]]] = ...) -> None: ...

class DeleteRangeScribeRowsProto(_message.Message):
    __slots__ = ("table", "string_range_key", "int64_range_key", "do_single_bucket_delete_range")
    class StringRangeKey(_message.Message):
        __slots__ = ("start_key", "end_key")
        START_KEY_FIELD_NUMBER: _ClassVar[int]
        END_KEY_FIELD_NUMBER: _ClassVar[int]
        start_key: str
        end_key: str
        def __init__(self, start_key: _Optional[str] = ..., end_key: _Optional[str] = ...) -> None: ...
    class Int64RangeKey(_message.Message):
        __slots__ = ("start_key", "end_key")
        START_KEY_FIELD_NUMBER: _ClassVar[int]
        END_KEY_FIELD_NUMBER: _ClassVar[int]
        start_key: int
        end_key: int
        def __init__(self, start_key: _Optional[int] = ..., end_key: _Optional[int] = ...) -> None: ...
    TABLE_FIELD_NUMBER: _ClassVar[int]
    STRING_RANGE_KEY_FIELD_NUMBER: _ClassVar[int]
    INT64_RANGE_KEY_FIELD_NUMBER: _ClassVar[int]
    DO_SINGLE_BUCKET_DELETE_RANGE_FIELD_NUMBER: _ClassVar[int]
    table: ScribeTableProto.Type
    string_range_key: DeleteRangeScribeRowsProto.StringRangeKey
    int64_range_key: DeleteRangeScribeRowsProto.Int64RangeKey
    do_single_bucket_delete_range: bool
    def __init__(self, table: _Optional[_Union[ScribeTableProto.Type, str]] = ..., string_range_key: _Optional[_Union[DeleteRangeScribeRowsProto.StringRangeKey, _Mapping]] = ..., int64_range_key: _Optional[_Union[DeleteRangeScribeRowsProto.Int64RangeKey, _Mapping]] = ..., do_single_bucket_delete_range: bool = ...) -> None: ...

class UpdateViewUsageTableProto(_message.Message):
    __slots__ = ("view_id", "view_usage_proto", "insert_retry_count", "clear_extension_stats", "update_view_usage_field")
    VIEW_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_USAGE_PROTO_FIELD_NUMBER: _ClassVar[int]
    INSERT_RETRY_COUNT_FIELD_NUMBER: _ClassVar[int]
    CLEAR_EXTENSION_STATS_FIELD_NUMBER: _ClassVar[int]
    UPDATE_VIEW_USAGE_FIELD_FIELD_NUMBER: _ClassVar[int]
    view_id: int
    view_usage_proto: _view_usage_pb2.ViewUsageProto
    insert_retry_count: int
    clear_extension_stats: bool
    update_view_usage_field: bool
    def __init__(self, view_id: _Optional[int] = ..., view_usage_proto: _Optional[_Union[_view_usage_pb2.ViewUsageProto, _Mapping]] = ..., insert_retry_count: _Optional[int] = ..., clear_extension_stats: bool = ..., update_view_usage_field: bool = ...) -> None: ...

class AddAcksAndMayBeDeleteViewBoxProto(_message.Message):
    __slots__ = ("view_box_id", "removal_state_version", "acks_to_add")
    VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
    REMOVAL_STATE_VERSION_FIELD_NUMBER: _ClassVar[int]
    ACKS_TO_ADD_FIELD_NUMBER: _ClassVar[int]
    view_box_id: int
    removal_state_version: int
    acks_to_add: int
    def __init__(self, view_box_id: _Optional[int] = ..., removal_state_version: _Optional[int] = ..., acks_to_add: _Optional[int] = ...) -> None: ...

class PublishStatsProto(_message.Message):
    __slots__ = ("schema_name", "entity_key_string", "entity_key_int", "timestamp_usecs", "metric_vec")
    class Metric(_message.Message):
        __slots__ = ("name", "value")
        NAME_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        name: str
        value: int
        def __init__(self, name: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    SCHEMA_NAME_FIELD_NUMBER: _ClassVar[int]
    ENTITY_KEY_STRING_FIELD_NUMBER: _ClassVar[int]
    ENTITY_KEY_INT_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
    METRIC_VEC_FIELD_NUMBER: _ClassVar[int]
    schema_name: str
    entity_key_string: str
    entity_key_int: int
    timestamp_usecs: int
    metric_vec: _containers.RepeatedCompositeFieldContainer[PublishStatsProto.Metric]
    def __init__(self, schema_name: _Optional[str] = ..., entity_key_string: _Optional[str] = ..., entity_key_int: _Optional[int] = ..., timestamp_usecs: _Optional[int] = ..., metric_vec: _Optional[_Iterable[_Union[PublishStatsProto.Metric, _Mapping]]] = ...) -> None: ...

class PublishStorageStatsProto(_message.Message):
    __slots__ = ("publish_stats", "chunk_bytes_morphed_local", "chunk_bytes_morphed_cloud", "viewbox_id", "pipeline_name", "chunk_bytes_physical")
    PUBLISH_STATS_FIELD_NUMBER: _ClassVar[int]
    CHUNK_BYTES_MORPHED_LOCAL_FIELD_NUMBER: _ClassVar[int]
    CHUNK_BYTES_MORPHED_CLOUD_FIELD_NUMBER: _ClassVar[int]
    VIEWBOX_ID_FIELD_NUMBER: _ClassVar[int]
    PIPELINE_NAME_FIELD_NUMBER: _ClassVar[int]
    CHUNK_BYTES_PHYSICAL_FIELD_NUMBER: _ClassVar[int]
    publish_stats: PublishStatsProto
    chunk_bytes_morphed_local: int
    chunk_bytes_morphed_cloud: int
    viewbox_id: int
    pipeline_name: str
    chunk_bytes_physical: int
    def __init__(self, publish_stats: _Optional[_Union[PublishStatsProto, _Mapping]] = ..., chunk_bytes_morphed_local: _Optional[int] = ..., chunk_bytes_morphed_cloud: _Optional[int] = ..., viewbox_id: _Optional[int] = ..., pipeline_name: _Optional[str] = ..., chunk_bytes_physical: _Optional[int] = ...) -> None: ...

class PublishHistogramsProto(_message.Message):
    __slots__ = ("histogram", "entity_name", "histogram_name")
    HISTOGRAM_FIELD_NUMBER: _ClassVar[int]
    ENTITY_NAME_FIELD_NUMBER: _ClassVar[int]
    HISTOGRAM_NAME_FIELD_NUMBER: _ClassVar[int]
    histogram: _histogram_proto_pb2.HistogramProto
    entity_name: str
    histogram_name: str
    def __init__(self, histogram: _Optional[_Union[_histogram_proto_pb2.HistogramProto, _Mapping]] = ..., entity_name: _Optional[str] = ..., histogram_name: _Optional[str] = ...) -> None: ...

class CreateOrUpdateBookkeeperGroupProto(_message.Message):
    __slots__ = ("view_id", "view_name", "bookkeeper_group_id", "group_attributes", "consumer_entity")
    VIEW_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    BOOKKEEPER_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    GROUP_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    CONSUMER_ENTITY_FIELD_NUMBER: _ClassVar[int]
    view_id: int
    view_name: str
    bookkeeper_group_id: int
    group_attributes: _bookkeeper_pb2.GroupAttributesProto
    consumer_entity: _bookkeeper_pb2.ConsumerEntityProto
    def __init__(self, view_id: _Optional[int] = ..., view_name: _Optional[str] = ..., bookkeeper_group_id: _Optional[int] = ..., group_attributes: _Optional[_Union[_bookkeeper_pb2.GroupAttributesProto, _Mapping]] = ..., consumer_entity: _Optional[_Union[_bookkeeper_pb2.ConsumerEntityProto, _Mapping]] = ...) -> None: ...

class PublishBookkeeperGroupStatsProto(_message.Message):
    __slots__ = ("group_id", "group_stats")
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    GROUP_STATS_FIELD_NUMBER: _ClassVar[int]
    group_id: int
    group_stats: _bookkeeper_pb2.GroupStatusProto
    def __init__(self, group_id: _Optional[int] = ..., group_stats: _Optional[_Union[_bookkeeper_pb2.GroupStatusProto, _Mapping]] = ...) -> None: ...

class DeleteBookkeeperGroupProto(_message.Message):
    __slots__ = ("group_id",)
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    group_id: int
    def __init__(self, group_id: _Optional[int] = ...) -> None: ...

class CheckBlobSnapTreeRootRefProto(_message.Message):
    __slots__ = ("blob_snap_tree_root_id", "raise_fatal_error")
    BLOB_SNAP_TREE_ROOT_ID_FIELD_NUMBER: _ClassVar[int]
    RAISE_FATAL_ERROR_FIELD_NUMBER: _ClassVar[int]
    blob_snap_tree_root_id: int
    raise_fatal_error: bool
    def __init__(self, blob_snap_tree_root_id: _Optional[int] = ..., raise_fatal_error: bool = ...) -> None: ...

class AckDiskRemovalProto(_message.Message):
    __slots__ = ("disk_cfg_from_context", "ack")
    DISK_CFG_FROM_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    ACK_FIELD_NUMBER: _ClassVar[int]
    disk_cfg_from_context: _cluster_config_pb2.ClusterConfigProto.Disk
    ack: _cluster_config_pb2.ClusterConfigProto.RemovalState.Ack
    def __init__(self, disk_cfg_from_context: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.Disk, _Mapping]] = ..., ack: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.RemovalState.Ack, str]] = ...) -> None: ...

class DeleteStatsEntityProto(_message.Message):
    __slots__ = ("schema_name", "entity_key_str", "entity_key_int")
    SCHEMA_NAME_FIELD_NUMBER: _ClassVar[int]
    ENTITY_KEY_STR_FIELD_NUMBER: _ClassVar[int]
    ENTITY_KEY_INT_FIELD_NUMBER: _ClassVar[int]
    schema_name: str
    entity_key_str: str
    entity_key_int: int
    def __init__(self, schema_name: _Optional[str] = ..., entity_key_str: _Optional[str] = ..., entity_key_int: _Optional[int] = ...) -> None: ...

class GandalfUpdateStateProto(_message.Message):
    __slots__ = ("key", "data", "version", "is_delete", "retry_on_cas_error")
    KEY_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    IS_DELETE_FIELD_NUMBER: _ClassVar[int]
    RETRY_ON_CAS_ERROR_FIELD_NUMBER: _ClassVar[int]
    key: str
    data: bytes
    version: int
    is_delete: bool
    retry_on_cas_error: bool
    def __init__(self, key: _Optional[str] = ..., data: _Optional[bytes] = ..., version: _Optional[int] = ..., is_delete: bool = ..., retry_on_cas_error: bool = ...) -> None: ...

class FindPathsForEntityHandlesProto(_message.Message):
    __slots__ = ("input_path", "chunk_id", "blob_id_vec", "job_start_time_str", "refd_chunk_info_vec", "missing_entry_name_vec", "missing_fragment_id_vec", "blob_snap_tree_node_id_vec")
    class Eh2PathProto(_message.Message):
        __slots__ = ("eh", "root_inode_path")
        EH_FIELD_NUMBER: _ClassVar[int]
        ROOT_INODE_PATH_FIELD_NUMBER: _ClassVar[int]
        eh: _entity_handle_pb2.EntityHandleProto
        root_inode_path: str
        def __init__(self, eh: _Optional[_Union[_entity_handle_pb2.EntityHandleProto, _Mapping]] = ..., root_inode_path: _Optional[str] = ...) -> None: ...
    class ChunkInfo(_message.Message):
        __slots__ = ("refd_chunk_id", "offset_vec")
        REFD_CHUNK_ID_FIELD_NUMBER: _ClassVar[int]
        OFFSET_VEC_FIELD_NUMBER: _ClassVar[int]
        refd_chunk_id: _blob_store_pb2.ChunkIdProto
        offset_vec: _containers.RepeatedScalarFieldContainer[int]
        def __init__(self, refd_chunk_id: _Optional[_Union[_blob_store_pb2.ChunkIdProto, _Mapping]] = ..., offset_vec: _Optional[_Iterable[int]] = ...) -> None: ...
    INPUT_PATH_FIELD_NUMBER: _ClassVar[int]
    CHUNK_ID_FIELD_NUMBER: _ClassVar[int]
    BLOB_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    JOB_START_TIME_STR_FIELD_NUMBER: _ClassVar[int]
    REFD_CHUNK_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    MISSING_ENTRY_NAME_VEC_FIELD_NUMBER: _ClassVar[int]
    MISSING_FRAGMENT_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    BLOB_SNAP_TREE_NODE_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    input_path: FindPathsForEntityHandlesProto.Eh2PathProto
    chunk_id: _blob_store_pb2.ChunkIdProto
    blob_id_vec: _containers.RepeatedScalarFieldContainer[int]
    job_start_time_str: str
    refd_chunk_info_vec: _containers.RepeatedCompositeFieldContainer[FindPathsForEntityHandlesProto.ChunkInfo]
    missing_entry_name_vec: _containers.RepeatedScalarFieldContainer[str]
    missing_fragment_id_vec: _containers.RepeatedScalarFieldContainer[int]
    blob_snap_tree_node_id_vec: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, input_path: _Optional[_Union[FindPathsForEntityHandlesProto.Eh2PathProto, _Mapping]] = ..., chunk_id: _Optional[_Union[_blob_store_pb2.ChunkIdProto, _Mapping]] = ..., blob_id_vec: _Optional[_Iterable[int]] = ..., job_start_time_str: _Optional[str] = ..., refd_chunk_info_vec: _Optional[_Iterable[_Union[FindPathsForEntityHandlesProto.ChunkInfo, _Mapping]]] = ..., missing_entry_name_vec: _Optional[_Iterable[str]] = ..., missing_fragment_id_vec: _Optional[_Iterable[int]] = ..., blob_snap_tree_node_id_vec: _Optional[_Iterable[int]] = ...) -> None: ...

class ChunkFileDeleteProto(_message.Message):
    __slots__ = ("chunk_file_id", "chunk_file_opclock_vec", "scribe_row_version", "raise_fatal_error")
    CHUNK_FILE_ID_FIELD_NUMBER: _ClassVar[int]
    CHUNK_FILE_OPCLOCK_VEC_FIELD_NUMBER: _ClassVar[int]
    SCRIBE_ROW_VERSION_FIELD_NUMBER: _ClassVar[int]
    RAISE_FATAL_ERROR_FIELD_NUMBER: _ClassVar[int]
    chunk_file_id: int
    chunk_file_opclock_vec: _containers.RepeatedCompositeFieldContainer[_op_clock_pb2.OpClock]
    scribe_row_version: int
    raise_fatal_error: bool
    def __init__(self, chunk_file_id: _Optional[int] = ..., chunk_file_opclock_vec: _Optional[_Iterable[_Union[_op_clock_pb2.OpClock, _Mapping]]] = ..., scribe_row_version: _Optional[int] = ..., raise_fatal_error: bool = ...) -> None: ...

class CheckStaleDanglingChunkProto(_message.Message):
    __slots__ = ("chunk_id", "chunk_file_id_refd_by_chunk", "raise_fatal_error")
    CHUNK_ID_FIELD_NUMBER: _ClassVar[int]
    CHUNK_FILE_ID_REFD_BY_CHUNK_FIELD_NUMBER: _ClassVar[int]
    RAISE_FATAL_ERROR_FIELD_NUMBER: _ClassVar[int]
    chunk_id: _blob_store_pb2.ChunkIdProto
    chunk_file_id_refd_by_chunk: int
    raise_fatal_error: bool
    def __init__(self, chunk_id: _Optional[_Union[_blob_store_pb2.ChunkIdProto, _Mapping]] = ..., chunk_file_id_refd_by_chunk: _Optional[int] = ..., raise_fatal_error: bool = ...) -> None: ...

class UpdateChunkFileAccessTableProto(_message.Message):
    __slots__ = ("chunk_file_id", "pinned_access_state_proto", "scribe_row_version")
    CHUNK_FILE_ID_FIELD_NUMBER: _ClassVar[int]
    PINNED_ACCESS_STATE_PROTO_FIELD_NUMBER: _ClassVar[int]
    SCRIBE_ROW_VERSION_FIELD_NUMBER: _ClassVar[int]
    chunk_file_id: int
    pinned_access_state_proto: _blob_store_pb2.PinnedChunkFileAccessStateProto
    scribe_row_version: int
    def __init__(self, chunk_file_id: _Optional[int] = ..., pinned_access_state_proto: _Optional[_Union[_blob_store_pb2.PinnedChunkFileAccessStateProto, _Mapping]] = ..., scribe_row_version: _Optional[int] = ...) -> None: ...

class OrionDanglingChildValidationProto(_message.Message):
    __slots__ = ("cloud_object_id", "validate_local_nodes_absence_vec", "local_minion_brick_node_to_parents_map")
    class CloudNodePtrProtoVec(_message.Message):
        __slots__ = ("ptr_vec",)
        PTR_VEC_FIELD_NUMBER: _ClassVar[int]
        ptr_vec: _containers.RepeatedCompositeFieldContainer[_cloud_pb2.CloudNodePtrProto]
        def __init__(self, ptr_vec: _Optional[_Iterable[_Union[_cloud_pb2.CloudNodePtrProto, _Mapping]]] = ...) -> None: ...
    class LocalMinionBrickNodeToParentsMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: OrionDanglingChildValidationProto.CloudNodePtrProtoVec
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[OrionDanglingChildValidationProto.CloudNodePtrProtoVec, _Mapping]] = ...) -> None: ...
    CLOUD_OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_LOCAL_NODES_ABSENCE_VEC_FIELD_NUMBER: _ClassVar[int]
    LOCAL_MINION_BRICK_NODE_TO_PARENTS_MAP_FIELD_NUMBER: _ClassVar[int]
    cloud_object_id: _cloud_pb2.CloudObjectIdProto
    validate_local_nodes_absence_vec: _containers.RepeatedScalarFieldContainer[int]
    local_minion_brick_node_to_parents_map: _containers.MessageMap[int, OrionDanglingChildValidationProto.CloudNodePtrProtoVec]
    def __init__(self, cloud_object_id: _Optional[_Union[_cloud_pb2.CloudObjectIdProto, _Mapping]] = ..., validate_local_nodes_absence_vec: _Optional[_Iterable[int]] = ..., local_minion_brick_node_to_parents_map: _Optional[_Mapping[int, OrionDanglingChildValidationProto.CloudNodePtrProtoVec]] = ...) -> None: ...

class ValidateBrickOwnedChunkMappingProto(_message.Message):
    __slots__ = ("chunk_id", "brick_snap_tree_node_id", "brick_chunk_file_id", "actual_chunk_file_id", "brick_scribe_row_version", "raise_fatal_error")
    CHUNK_ID_FIELD_NUMBER: _ClassVar[int]
    BRICK_SNAP_TREE_NODE_ID_FIELD_NUMBER: _ClassVar[int]
    BRICK_CHUNK_FILE_ID_FIELD_NUMBER: _ClassVar[int]
    ACTUAL_CHUNK_FILE_ID_FIELD_NUMBER: _ClassVar[int]
    BRICK_SCRIBE_ROW_VERSION_FIELD_NUMBER: _ClassVar[int]
    RAISE_FATAL_ERROR_FIELD_NUMBER: _ClassVar[int]
    chunk_id: _blob_store_pb2.ChunkIdProto
    brick_snap_tree_node_id: int
    brick_chunk_file_id: int
    actual_chunk_file_id: int
    brick_scribe_row_version: int
    raise_fatal_error: bool
    def __init__(self, chunk_id: _Optional[_Union[_blob_store_pb2.ChunkIdProto, _Mapping]] = ..., brick_snap_tree_node_id: _Optional[int] = ..., brick_chunk_file_id: _Optional[int] = ..., actual_chunk_file_id: _Optional[int] = ..., brick_scribe_row_version: _Optional[int] = ..., raise_fatal_error: bool = ...) -> None: ...

class BookkeeperV2GroupStatsProto(_message.Message):
    __slots__ = ("logical_stats", "physical_stats", "group_metadata_stats", "io_stats", "stats_version", "bk_v2_group_id")
    LOGICAL_STATS_FIELD_NUMBER: _ClassVar[int]
    PHYSICAL_STATS_FIELD_NUMBER: _ClassVar[int]
    GROUP_METADATA_STATS_FIELD_NUMBER: _ClassVar[int]
    IO_STATS_FIELD_NUMBER: _ClassVar[int]
    STATS_VERSION_FIELD_NUMBER: _ClassVar[int]
    BK_V2_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    logical_stats: _bookkeeper_v2_pb2.LogicalStats
    physical_stats: _bookkeeper_v2_pb2.PhysicalStats
    group_metadata_stats: _bookkeeper_v2_pb2.GroupMetadataStats
    io_stats: _bookkeeper_v2_pb2.IOStats
    stats_version: str
    bk_v2_group_id: str
    def __init__(self, logical_stats: _Optional[_Union[_bookkeeper_v2_pb2.LogicalStats, _Mapping]] = ..., physical_stats: _Optional[_Union[_bookkeeper_v2_pb2.PhysicalStats, _Mapping]] = ..., group_metadata_stats: _Optional[_Union[_bookkeeper_v2_pb2.GroupMetadataStats, _Mapping]] = ..., io_stats: _Optional[_Union[_bookkeeper_v2_pb2.IOStats, _Mapping]] = ..., stats_version: _Optional[str] = ..., bk_v2_group_id: _Optional[str] = ...) -> None: ...

class DeleteBookkeeperV2EntityProto(_message.Message):
    __slots__ = ("bk_v2_entity_proto", "scribe_row_version", "bk_v2_entity_deleted_timestamp")
    BK_V2_ENTITY_PROTO_FIELD_NUMBER: _ClassVar[int]
    SCRIBE_ROW_VERSION_FIELD_NUMBER: _ClassVar[int]
    BK_V2_ENTITY_DELETED_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    bk_v2_entity_proto: _bookkeeper_v2_pb2.BookkeeperEntityProto
    scribe_row_version: int
    bk_v2_entity_deleted_timestamp: int
    def __init__(self, bk_v2_entity_proto: _Optional[_Union[_bookkeeper_v2_pb2.BookkeeperEntityProto, _Mapping]] = ..., scribe_row_version: _Optional[int] = ..., bk_v2_entity_deleted_timestamp: _Optional[int] = ...) -> None: ...

class BookkeeperV2QueryKeyValProto(_message.Message):
    __slots__ = ("result_data", "input_arg_as_key", "last_updated_timestamp", "batch_size", "is_query_completed")
    RESULT_DATA_FIELD_NUMBER: _ClassVar[int]
    INPUT_ARG_AS_KEY_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATED_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    BATCH_SIZE_FIELD_NUMBER: _ClassVar[int]
    IS_QUERY_COMPLETED_FIELD_NUMBER: _ClassVar[int]
    result_data: str
    input_arg_as_key: str
    last_updated_timestamp: int
    batch_size: int
    is_query_completed: bool
    def __init__(self, result_data: _Optional[str] = ..., input_arg_as_key: _Optional[str] = ..., last_updated_timestamp: _Optional[int] = ..., batch_size: _Optional[int] = ..., is_query_completed: bool = ...) -> None: ...

class BkV2ViewGroupCreatorProto(_message.Message):
    __slots__ = ("view_id", "view_name")
    VIEW_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    view_id: int
    view_name: str
    def __init__(self, view_id: _Optional[int] = ..., view_name: _Optional[str] = ...) -> None: ...

class UpdateBrickBytesLogicalProto(_message.Message):
    __slots__ = ("bk_v2_grp_id", "brick_bytes_logical", "minion_brick_bytes_logical")
    BK_V2_GRP_ID_FIELD_NUMBER: _ClassVar[int]
    BRICK_BYTES_LOGICAL_FIELD_NUMBER: _ClassVar[int]
    MINION_BRICK_BYTES_LOGICAL_FIELD_NUMBER: _ClassVar[int]
    bk_v2_grp_id: str
    brick_bytes_logical: int
    minion_brick_bytes_logical: int
    def __init__(self, bk_v2_grp_id: _Optional[str] = ..., brick_bytes_logical: _Optional[int] = ..., minion_brick_bytes_logical: _Optional[int] = ...) -> None: ...

class MiscActionProto(_message.Message):
    __slots__ = ("type", "job_opclock_vec", "check_snaptree_dangling_ref", "check_chunk_dangling_ref", "insert_delete_scribe_row", "publish_stats", "ack_disk_removal", "publish_histograms", "add_acks_and_may_be_delete_view_box", "update_view_usage_table", "publish_storage_stats", "check_blob_snap_tree_root_ref", "create_or_update_bookkeeper_group", "publish_bookkeeper_group_stats", "delete_bookkeeper_group", "delete_stats_entity", "gandalf_update_state", "find_paths_for_entity_handles", "chunk_file_delete", "chunk_stale_dangling_ref", "icebox_retire_reference_archive_arg", "update_chunk_file_access_table", "orion_dangling_child_validation", "delete_range_scribe_rows", "validate_brick_owned_chunk_mapping", "bookkeeper_v2_group_stats", "bk_v2_delete_entity_proto", "create_bk_v2_grp_for_ext_views", "update_bk_v2_brick_bytes_logical", "bookkeeper_v2_query_result", "bkpr_v2_special_entity_proto")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kCheckSnapTreeDanglingRef: _ClassVar[MiscActionProto.Type]
        kCheckChunkDanglingRef: _ClassVar[MiscActionProto.Type]
        kInsertDeleteScribeRow: _ClassVar[MiscActionProto.Type]
        kPublishStats: _ClassVar[MiscActionProto.Type]
        kAckDiskRemoval: _ClassVar[MiscActionProto.Type]
        kPublishHistograms: _ClassVar[MiscActionProto.Type]
        kAddAcksAndMayBeDeleteViewBox: _ClassVar[MiscActionProto.Type]
        kUpdateViewUsageTable: _ClassVar[MiscActionProto.Type]
        kPublishStorageStats: _ClassVar[MiscActionProto.Type]
        kCheckBlobSnapTreeRootRef: _ClassVar[MiscActionProto.Type]
        kCreateOrUpdateBookkeeperGroup: _ClassVar[MiscActionProto.Type]
        kPublishBookkeeperGroupStats: _ClassVar[MiscActionProto.Type]
        kDeleteBookkeeperGroup: _ClassVar[MiscActionProto.Type]
        kDeleteStatsEntity: _ClassVar[MiscActionProto.Type]
        kUpdateGandalf: _ClassVar[MiscActionProto.Type]
        kFindPathsForEntityHandles: _ClassVar[MiscActionProto.Type]
        kChunkFileDelete: _ClassVar[MiscActionProto.Type]
        kCheckStaleChunkDanglingRef: _ClassVar[MiscActionProto.Type]
        kIceboxRetireReferenceArchive: _ClassVar[MiscActionProto.Type]
        kUpdateChunkFileAccessTable: _ClassVar[MiscActionProto.Type]
        kIceboxOrionDanglingChildValidation: _ClassVar[MiscActionProto.Type]
        kDeleteRangeScribeRows: _ClassVar[MiscActionProto.Type]
        kValidateBrickOwnedChunkMapping: _ClassVar[MiscActionProto.Type]
        kPublishBookkeeperV2GroupStats: _ClassVar[MiscActionProto.Type]
        kDeleteBookkeeperV2Entities: _ClassVar[MiscActionProto.Type]
        kCreateBookkeeperV2GroupForViews: _ClassVar[MiscActionProto.Type]
        kUpdateBkV2BrickBytesLogical: _ClassVar[MiscActionProto.Type]
        kPublishBookkeeperV2QueryResult: _ClassVar[MiscActionProto.Type]
        kUpdateBkV2SpecialGroups: _ClassVar[MiscActionProto.Type]
    kCheckSnapTreeDanglingRef: MiscActionProto.Type
    kCheckChunkDanglingRef: MiscActionProto.Type
    kInsertDeleteScribeRow: MiscActionProto.Type
    kPublishStats: MiscActionProto.Type
    kAckDiskRemoval: MiscActionProto.Type
    kPublishHistograms: MiscActionProto.Type
    kAddAcksAndMayBeDeleteViewBox: MiscActionProto.Type
    kUpdateViewUsageTable: MiscActionProto.Type
    kPublishStorageStats: MiscActionProto.Type
    kCheckBlobSnapTreeRootRef: MiscActionProto.Type
    kCreateOrUpdateBookkeeperGroup: MiscActionProto.Type
    kPublishBookkeeperGroupStats: MiscActionProto.Type
    kDeleteBookkeeperGroup: MiscActionProto.Type
    kDeleteStatsEntity: MiscActionProto.Type
    kUpdateGandalf: MiscActionProto.Type
    kFindPathsForEntityHandles: MiscActionProto.Type
    kChunkFileDelete: MiscActionProto.Type
    kCheckStaleChunkDanglingRef: MiscActionProto.Type
    kIceboxRetireReferenceArchive: MiscActionProto.Type
    kUpdateChunkFileAccessTable: MiscActionProto.Type
    kIceboxOrionDanglingChildValidation: MiscActionProto.Type
    kDeleteRangeScribeRows: MiscActionProto.Type
    kValidateBrickOwnedChunkMapping: MiscActionProto.Type
    kPublishBookkeeperV2GroupStats: MiscActionProto.Type
    kDeleteBookkeeperV2Entities: MiscActionProto.Type
    kCreateBookkeeperV2GroupForViews: MiscActionProto.Type
    kUpdateBkV2BrickBytesLogical: MiscActionProto.Type
    kPublishBookkeeperV2QueryResult: MiscActionProto.Type
    kUpdateBkV2SpecialGroups: MiscActionProto.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    JOB_OPCLOCK_VEC_FIELD_NUMBER: _ClassVar[int]
    CHECK_SNAPTREE_DANGLING_REF_FIELD_NUMBER: _ClassVar[int]
    CHECK_CHUNK_DANGLING_REF_FIELD_NUMBER: _ClassVar[int]
    INSERT_DELETE_SCRIBE_ROW_FIELD_NUMBER: _ClassVar[int]
    PUBLISH_STATS_FIELD_NUMBER: _ClassVar[int]
    ACK_DISK_REMOVAL_FIELD_NUMBER: _ClassVar[int]
    PUBLISH_HISTOGRAMS_FIELD_NUMBER: _ClassVar[int]
    ADD_ACKS_AND_MAY_BE_DELETE_VIEW_BOX_FIELD_NUMBER: _ClassVar[int]
    UPDATE_VIEW_USAGE_TABLE_FIELD_NUMBER: _ClassVar[int]
    PUBLISH_STORAGE_STATS_FIELD_NUMBER: _ClassVar[int]
    CHECK_BLOB_SNAP_TREE_ROOT_REF_FIELD_NUMBER: _ClassVar[int]
    CREATE_OR_UPDATE_BOOKKEEPER_GROUP_FIELD_NUMBER: _ClassVar[int]
    PUBLISH_BOOKKEEPER_GROUP_STATS_FIELD_NUMBER: _ClassVar[int]
    DELETE_BOOKKEEPER_GROUP_FIELD_NUMBER: _ClassVar[int]
    DELETE_STATS_ENTITY_FIELD_NUMBER: _ClassVar[int]
    GANDALF_UPDATE_STATE_FIELD_NUMBER: _ClassVar[int]
    FIND_PATHS_FOR_ENTITY_HANDLES_FIELD_NUMBER: _ClassVar[int]
    CHUNK_FILE_DELETE_FIELD_NUMBER: _ClassVar[int]
    CHUNK_STALE_DANGLING_REF_FIELD_NUMBER: _ClassVar[int]
    ICEBOX_RETIRE_REFERENCE_ARCHIVE_ARG_FIELD_NUMBER: _ClassVar[int]
    UPDATE_CHUNK_FILE_ACCESS_TABLE_FIELD_NUMBER: _ClassVar[int]
    ORION_DANGLING_CHILD_VALIDATION_FIELD_NUMBER: _ClassVar[int]
    DELETE_RANGE_SCRIBE_ROWS_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_BRICK_OWNED_CHUNK_MAPPING_FIELD_NUMBER: _ClassVar[int]
    BOOKKEEPER_V2_GROUP_STATS_FIELD_NUMBER: _ClassVar[int]
    BK_V2_DELETE_ENTITY_PROTO_FIELD_NUMBER: _ClassVar[int]
    CREATE_BK_V2_GRP_FOR_EXT_VIEWS_FIELD_NUMBER: _ClassVar[int]
    UPDATE_BK_V2_BRICK_BYTES_LOGICAL_FIELD_NUMBER: _ClassVar[int]
    BOOKKEEPER_V2_QUERY_RESULT_FIELD_NUMBER: _ClassVar[int]
    BKPR_V2_SPECIAL_ENTITY_PROTO_FIELD_NUMBER: _ClassVar[int]
    type: MiscActionProto.Type
    job_opclock_vec: _containers.RepeatedCompositeFieldContainer[_op_clock_pb2.OpClock]
    check_snaptree_dangling_ref: SnapTreeChildReferenceInfoProto
    check_chunk_dangling_ref: ChunkReferenceInfoProto
    insert_delete_scribe_row: InsertDeleteScribeRowProto
    publish_stats: PublishStatsProto
    ack_disk_removal: AckDiskRemovalProto
    publish_histograms: _containers.RepeatedCompositeFieldContainer[PublishHistogramsProto]
    add_acks_and_may_be_delete_view_box: AddAcksAndMayBeDeleteViewBoxProto
    update_view_usage_table: UpdateViewUsageTableProto
    publish_storage_stats: PublishStorageStatsProto
    check_blob_snap_tree_root_ref: CheckBlobSnapTreeRootRefProto
    create_or_update_bookkeeper_group: CreateOrUpdateBookkeeperGroupProto
    publish_bookkeeper_group_stats: PublishBookkeeperGroupStatsProto
    delete_bookkeeper_group: DeleteBookkeeperGroupProto
    delete_stats_entity: DeleteStatsEntityProto
    gandalf_update_state: GandalfUpdateStateProto
    find_paths_for_entity_handles: FindPathsForEntityHandlesProto
    chunk_file_delete: ChunkFileDeleteProto
    chunk_stale_dangling_ref: CheckStaleDanglingChunkProto
    icebox_retire_reference_archive_arg: _rpc_service_pb2.RetireReferenceArg
    update_chunk_file_access_table: UpdateChunkFileAccessTableProto
    orion_dangling_child_validation: OrionDanglingChildValidationProto
    delete_range_scribe_rows: DeleteRangeScribeRowsProto
    validate_brick_owned_chunk_mapping: ValidateBrickOwnedChunkMappingProto
    bookkeeper_v2_group_stats: BookkeeperV2GroupStatsProto
    bk_v2_delete_entity_proto: DeleteBookkeeperV2EntityProto
    create_bk_v2_grp_for_ext_views: BkV2ViewGroupCreatorProto
    update_bk_v2_brick_bytes_logical: UpdateBrickBytesLogicalProto
    bookkeeper_v2_query_result: BookkeeperV2QueryKeyValProto
    bkpr_v2_special_entity_proto: _bookkeeper_v2_special_groups_pb2.BookkeeperV2SpecialEntityProto
    def __init__(self, type: _Optional[_Union[MiscActionProto.Type, str]] = ..., job_opclock_vec: _Optional[_Iterable[_Union[_op_clock_pb2.OpClock, _Mapping]]] = ..., check_snaptree_dangling_ref: _Optional[_Union[SnapTreeChildReferenceInfoProto, _Mapping]] = ..., check_chunk_dangling_ref: _Optional[_Union[ChunkReferenceInfoProto, _Mapping]] = ..., insert_delete_scribe_row: _Optional[_Union[InsertDeleteScribeRowProto, _Mapping]] = ..., publish_stats: _Optional[_Union[PublishStatsProto, _Mapping]] = ..., ack_disk_removal: _Optional[_Union[AckDiskRemovalProto, _Mapping]] = ..., publish_histograms: _Optional[_Iterable[_Union[PublishHistogramsProto, _Mapping]]] = ..., add_acks_and_may_be_delete_view_box: _Optional[_Union[AddAcksAndMayBeDeleteViewBoxProto, _Mapping]] = ..., update_view_usage_table: _Optional[_Union[UpdateViewUsageTableProto, _Mapping]] = ..., publish_storage_stats: _Optional[_Union[PublishStorageStatsProto, _Mapping]] = ..., check_blob_snap_tree_root_ref: _Optional[_Union[CheckBlobSnapTreeRootRefProto, _Mapping]] = ..., create_or_update_bookkeeper_group: _Optional[_Union[CreateOrUpdateBookkeeperGroupProto, _Mapping]] = ..., publish_bookkeeper_group_stats: _Optional[_Union[PublishBookkeeperGroupStatsProto, _Mapping]] = ..., delete_bookkeeper_group: _Optional[_Union[DeleteBookkeeperGroupProto, _Mapping]] = ..., delete_stats_entity: _Optional[_Union[DeleteStatsEntityProto, _Mapping]] = ..., gandalf_update_state: _Optional[_Union[GandalfUpdateStateProto, _Mapping]] = ..., find_paths_for_entity_handles: _Optional[_Union[FindPathsForEntityHandlesProto, _Mapping]] = ..., chunk_file_delete: _Optional[_Union[ChunkFileDeleteProto, _Mapping]] = ..., chunk_stale_dangling_ref: _Optional[_Union[CheckStaleDanglingChunkProto, _Mapping]] = ..., icebox_retire_reference_archive_arg: _Optional[_Union[_rpc_service_pb2.RetireReferenceArg, _Mapping]] = ..., update_chunk_file_access_table: _Optional[_Union[UpdateChunkFileAccessTableProto, _Mapping]] = ..., orion_dangling_child_validation: _Optional[_Union[OrionDanglingChildValidationProto, _Mapping]] = ..., delete_range_scribe_rows: _Optional[_Union[DeleteRangeScribeRowsProto, _Mapping]] = ..., validate_brick_owned_chunk_mapping: _Optional[_Union[ValidateBrickOwnedChunkMappingProto, _Mapping]] = ..., bookkeeper_v2_group_stats: _Optional[_Union[BookkeeperV2GroupStatsProto, _Mapping]] = ..., bk_v2_delete_entity_proto: _Optional[_Union[DeleteBookkeeperV2EntityProto, _Mapping]] = ..., create_bk_v2_grp_for_ext_views: _Optional[_Union[BkV2ViewGroupCreatorProto, _Mapping]] = ..., update_bk_v2_brick_bytes_logical: _Optional[_Union[UpdateBrickBytesLogicalProto, _Mapping]] = ..., bookkeeper_v2_query_result: _Optional[_Union[BookkeeperV2QueryKeyValProto, _Mapping]] = ..., bkpr_v2_special_entity_proto: _Optional[_Union[_bookkeeper_v2_special_groups_pb2.BookkeeperV2SpecialEntityProto, _Mapping]] = ...) -> None: ...

class Action(_message.Message):
    __slots__ = ("type", "metadata", "bridge_action", "misc_action")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kBridgeAction: _ClassVar[Action.Type]
        kMiscAction: _ClassVar[Action.Type]
    kBridgeAction: Action.Type
    kMiscAction: Action.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    BRIDGE_ACTION_FIELD_NUMBER: _ClassVar[int]
    MISC_ACTION_FIELD_NUMBER: _ClassVar[int]
    type: Action.Type
    metadata: ActionMetadataProto
    bridge_action: _actions_v2_pb2.ActionProto
    misc_action: MiscActionProto
    def __init__(self, type: _Optional[_Union[Action.Type, str]] = ..., metadata: _Optional[_Union[ActionMetadataProto, _Mapping]] = ..., bridge_action: _Optional[_Union[_actions_v2_pb2.ActionProto, _Mapping]] = ..., misc_action: _Optional[_Union[MiscActionProto, _Mapping]] = ...) -> None: ...

class ActionStats(_message.Message):
    __slots__ = ("type", "value", "error_count_map", "subtype_count_map")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ViewSnapTreeNodesDeleted: _ClassVar[ActionStats.Type]
        BlobSnapTreeNodesDeleted: _ClassVar[ActionStats.Type]
        NumChunksDeleted: _ClassVar[ActionStats.Type]
        ChunkDeletedBytesMorphed: _ClassVar[ActionStats.Type]
        NumChunkFilesDeleted: _ClassVar[ActionStats.Type]
        NumChunkFilesMigrated: _ClassVar[ActionStats.Type]
        ReclaimedBytesPhysical: _ClassVar[ActionStats.Type]
        NumChunkFilesEncoded: _ClassVar[ActionStats.Type]
        NumChunkFilesCompressed: _ClassVar[ActionStats.Type]
        QuotaSnapTreeNodesDeleted: _ClassVar[ActionStats.Type]
        QuotaUsageSnapTreeNodesDeleted: _ClassVar[ActionStats.Type]
        ViewSnapTreeInvalidRefcount: _ClassVar[ActionStats.Type]
        BlobSnapTreeInvalidRefcount: _ClassVar[ActionStats.Type]
        QuotaSnapTreeInvalidRefcount: _ClassVar[ActionStats.Type]
        QuotaUsageSnapTreeInvalidRefcount: _ClassVar[ActionStats.Type]
        NumScribeRowsAdded: _ClassVar[ActionStats.Type]
        NumScribeRowsDeleted: _ClassVar[ActionStats.Type]
        NumChunkFilesFixed: _ClassVar[ActionStats.Type]
        NumStatsPublished: _ClassVar[ActionStats.Type]
        MigratedBytesPhysical: _ClassVar[ActionStats.Type]
        MinionBlobBytesFreed: _ClassVar[ActionStats.Type]
        NumSnapTreeNodesDeduped: _ClassVar[ActionStats.Type]
        NumCanonicalSnapTreeNodes: _ClassVar[ActionStats.Type]
        NumUserEntriesFixed: _ClassVar[ActionStats.Type]
        NumUserEntriesFailedToFix: _ClassVar[ActionStats.Type]
        NumUserEntriesDeleted: _ClassVar[ActionStats.Type]
        NumUserEntriesFailedToDelete: _ClassVar[ActionStats.Type]
        NumChunkFilesRebalanced: _ClassVar[ActionStats.Type]
        RebalancedBytesMorphed: _ClassVar[ActionStats.Type]
        NumChunkFilesCloudSpilled: _ClassVar[ActionStats.Type]
        CloudSpilledBytesMorphed: _ClassVar[ActionStats.Type]
        NumSmbEntitiesCleanupExecuted: _ClassVar[ActionStats.Type]
        NumViewsDeleted: _ClassVar[ActionStats.Type]
        NumViewsFixed: _ClassVar[ActionStats.Type]
        NumViewBoxesDeleted: _ClassVar[ActionStats.Type]
        NumEntitiesFixed: _ClassVar[ActionStats.Type]
        NumEntitiesFailedToFix: _ClassVar[ActionStats.Type]
        AntivirusSnapTreeInvalidRefcount: _ClassVar[ActionStats.Type]
        AntivirusSnapTreeNodesDeleted: _ClassVar[ActionStats.Type]
        ViewUsageTableUpdated: _ClassVar[ActionStats.Type]
        NumIceboxChunkLocationsFixed: _ClassVar[ActionStats.Type]
        NumIceboxArchivesRetired: _ClassVar[ActionStats.Type]
        NumBookkeeperGroupsUpdated: _ClassVar[ActionStats.Type]
        NumBookkeeperGroupsStatsPublished: _ClassVar[ActionStats.Type]
        NumBookkeeperGroupsDeleted: _ClassVar[ActionStats.Type]
        NumDirEntriesFixed: _ClassVar[ActionStats.Type]
        NumDirEntriesFailedToFix: _ClassVar[ActionStats.Type]
        NumOrphanEntitiesGarbageCollected: _ClassVar[ActionStats.Type]
        NumShadowCopySetContextCleaned: _ClassVar[ActionStats.Type]
        NumIceboxDirectArchiveFilesGCed: _ClassVar[ActionStats.Type]
        NumNFSv4MetadataObjectsCleaned: _ClassVar[ActionStats.Type]
        NumNFSv4Errors: _ClassVar[ActionStats.Type]
        NumIceboxSnapTreeArchivedNodeLocationsCleaned: _ClassVar[ActionStats.Type]
        NumStatsEntitiesDeleted: _ClassVar[ActionStats.Type]
        NumGandalfKeysUpdated: _ClassVar[ActionStats.Type]
        NumGarbageFragmentsDeleted: _ClassVar[ActionStats.Type]
        NumBricksDeduped: _ClassVar[ActionStats.Type]
        NumFilesDeleted: _ClassVar[ActionStats.Type]
        NumMegaFilesDeleted: _ClassVar[ActionStats.Type]
        NumDirsDeleted: _ClassVar[ActionStats.Type]
        NumFileFragmentsDeleted: _ClassVar[ActionStats.Type]
        NumMegachunkCreated: _ClassVar[ActionStats.Type]
        NumExtentsDedupped: _ClassVar[ActionStats.Type]
        NumNonEmptyChunkFilesDeleted: _ClassVar[ActionStats.Type]
        NumChunkFilesEncodedToContainer: _ClassVar[ActionStats.Type]
        NumContainersCreated: _ClassVar[ActionStats.Type]
        NumCloudChunkFilesFixed: _ClassVar[ActionStats.Type]
        NumCloudChunksDeleted: _ClassVar[ActionStats.Type]
        NumCloudNodesDeleted: _ClassVar[ActionStats.Type]
        ChunkFileAccessTableUpdated: _ClassVar[ActionStats.Type]
        NumChunkFilePinSecsUpdated: _ClassVar[ActionStats.Type]
        NumIceboxStubViewsDeleted: _ClassVar[ActionStats.Type]
        NumCloudChunkFilesLCMed: _ClassVar[ActionStats.Type]
        NumGarbageChunksMigrated: _ClassVar[ActionStats.Type]
        NumGarbageChunksWithMigrateErrors: _ClassVar[ActionStats.Type]
        NumDeleteScribeRangeIssued: _ClassVar[ActionStats.Type]
        NumContainersFixed: _ClassVar[ActionStats.Type]
        NumContainersDeleted: _ClassVar[ActionStats.Type]
        NumS3ObjectsTimestampVecFixed: _ClassVar[ActionStats.Type]
        NumS3ObjectsFailedToFixTimestampVec: _ClassVar[ActionStats.Type]
        NumS3EntitiesLifecycled: _ClassVar[ActionStats.Type]
        LogicalBytesS3EntitiesLifecycled: _ClassVar[ActionStats.Type]
        NumS3EntitiesFailedToLifecycle: _ClassVar[ActionStats.Type]
        NumChunksDeletedKCASErrors: _ClassVar[ActionStats.Type]
        NumChunkFilesWithCASError: _ClassVar[ActionStats.Type]
        CASErrorNumChunksMigrated: _ClassVar[ActionStats.Type]
        CASErrorMigratedBytesPhysical: _ClassVar[ActionStats.Type]
        NumBridgeAssignmentsFailed: _ClassVar[ActionStats.Type]
        S3ObjectSnapTreeInvalidRefcount: _ClassVar[ActionStats.Type]
        S3ObjectSnapTreeNodesDeleted: _ClassVar[ActionStats.Type]
        ValidateBrickOwnedChunkMappingNumBricksFixed: _ClassVar[ActionStats.Type]
        ValidateBrickOwnedChunkMappingNumBricksSkipped: _ClassVar[ActionStats.Type]
        ValidateBrickOwnedChunkMappingNumBricksAccurate: _ClassVar[ActionStats.Type]
        ValidateBrickOwnedChunkMappingNumBrickUpdateErrors: _ClassVar[ActionStats.Type]
        ValidateBrickOwnedChunkMappingNumExistingActiveOpClocks: _ClassVar[ActionStats.Type]
        ValidateBrickOwnedChunkMappingNumChunkFileIdsSet: _ClassVar[ActionStats.Type]
        ValidateBrickOwnedChunkMappingNumChunkFileIdsCleared: _ClassVar[ActionStats.Type]
        NumCloudChunkFileValidationsProcessed: _ClassVar[ActionStats.Type]
        NumMissingCloudChunkFiles: _ClassVar[ActionStats.Type]
        NumIceboxCSRObjectsValidated: _ClassVar[ActionStats.Type]
        NumArchiveMetadataDeleted: _ClassVar[ActionStats.Type]
        NumChunksDeletedKNonExistentErrors: _ClassVar[ActionStats.Type]
        NumBookkeeperV2AggregatedGroups: _ClassVar[ActionStats.Type]
        NumIceboxMissingCSRNodes: _ClassVar[ActionStats.Type]
        NumMissingCloudChunks: _ClassVar[ActionStats.Type]
        NumCorruptCloudChunks: _ClassVar[ActionStats.Type]
        NumS3ObjectVersionsLifecycled: _ClassVar[ActionStats.Type]
        LogicalBytesS3ObjectVersionsLifecycled: _ClassVar[ActionStats.Type]
        NumS3IncompleteMultipartUploadsLifecycled: _ClassVar[ActionStats.Type]
        LogicalBytesS3IncompleteMultipartUploadsLifecycled: _ClassVar[ActionStats.Type]
        NumBookkeeperV2EntitiesDeleted: _ClassVar[ActionStats.Type]
        NumBookkeeperV2ExternalViewGroupsAssigned: _ClassVar[ActionStats.Type]
        NumBkV2GrpsBrickBytesLogicalUpdated: _ClassVar[ActionStats.Type]
        NumUptieredCloudChunkFilesDowntiered: _ClassVar[ActionStats.Type]
        NumIceboxUndeletedCSRNodes: _ClassVar[ActionStats.Type]
        NumBkV2SpecialGroupsStatsUpdated: _ClassVar[ActionStats.Type]
        DirQuotaSnapTreeInvalidRefcount: _ClassVar[ActionStats.Type]
        DirQuotaSnapTreeNodesDeleted: _ClassVar[ActionStats.Type]
        FilerLcmNumFilesDeleted: _ClassVar[ActionStats.Type]
        FilerLcmNumBytesRemoved: _ClassVar[ActionStats.Type]
        FilerLcmNumDirectoriesRemoved: _ClassVar[ActionStats.Type]
        FilerLcmNumEntitesFailedToDelete: _ClassVar[ActionStats.Type]
    ViewSnapTreeNodesDeleted: ActionStats.Type
    BlobSnapTreeNodesDeleted: ActionStats.Type
    NumChunksDeleted: ActionStats.Type
    ChunkDeletedBytesMorphed: ActionStats.Type
    NumChunkFilesDeleted: ActionStats.Type
    NumChunkFilesMigrated: ActionStats.Type
    ReclaimedBytesPhysical: ActionStats.Type
    NumChunkFilesEncoded: ActionStats.Type
    NumChunkFilesCompressed: ActionStats.Type
    QuotaSnapTreeNodesDeleted: ActionStats.Type
    QuotaUsageSnapTreeNodesDeleted: ActionStats.Type
    ViewSnapTreeInvalidRefcount: ActionStats.Type
    BlobSnapTreeInvalidRefcount: ActionStats.Type
    QuotaSnapTreeInvalidRefcount: ActionStats.Type
    QuotaUsageSnapTreeInvalidRefcount: ActionStats.Type
    NumScribeRowsAdded: ActionStats.Type
    NumScribeRowsDeleted: ActionStats.Type
    NumChunkFilesFixed: ActionStats.Type
    NumStatsPublished: ActionStats.Type
    MigratedBytesPhysical: ActionStats.Type
    MinionBlobBytesFreed: ActionStats.Type
    NumSnapTreeNodesDeduped: ActionStats.Type
    NumCanonicalSnapTreeNodes: ActionStats.Type
    NumUserEntriesFixed: ActionStats.Type
    NumUserEntriesFailedToFix: ActionStats.Type
    NumUserEntriesDeleted: ActionStats.Type
    NumUserEntriesFailedToDelete: ActionStats.Type
    NumChunkFilesRebalanced: ActionStats.Type
    RebalancedBytesMorphed: ActionStats.Type
    NumChunkFilesCloudSpilled: ActionStats.Type
    CloudSpilledBytesMorphed: ActionStats.Type
    NumSmbEntitiesCleanupExecuted: ActionStats.Type
    NumViewsDeleted: ActionStats.Type
    NumViewsFixed: ActionStats.Type
    NumViewBoxesDeleted: ActionStats.Type
    NumEntitiesFixed: ActionStats.Type
    NumEntitiesFailedToFix: ActionStats.Type
    AntivirusSnapTreeInvalidRefcount: ActionStats.Type
    AntivirusSnapTreeNodesDeleted: ActionStats.Type
    ViewUsageTableUpdated: ActionStats.Type
    NumIceboxChunkLocationsFixed: ActionStats.Type
    NumIceboxArchivesRetired: ActionStats.Type
    NumBookkeeperGroupsUpdated: ActionStats.Type
    NumBookkeeperGroupsStatsPublished: ActionStats.Type
    NumBookkeeperGroupsDeleted: ActionStats.Type
    NumDirEntriesFixed: ActionStats.Type
    NumDirEntriesFailedToFix: ActionStats.Type
    NumOrphanEntitiesGarbageCollected: ActionStats.Type
    NumShadowCopySetContextCleaned: ActionStats.Type
    NumIceboxDirectArchiveFilesGCed: ActionStats.Type
    NumNFSv4MetadataObjectsCleaned: ActionStats.Type
    NumNFSv4Errors: ActionStats.Type
    NumIceboxSnapTreeArchivedNodeLocationsCleaned: ActionStats.Type
    NumStatsEntitiesDeleted: ActionStats.Type
    NumGandalfKeysUpdated: ActionStats.Type
    NumGarbageFragmentsDeleted: ActionStats.Type
    NumBricksDeduped: ActionStats.Type
    NumFilesDeleted: ActionStats.Type
    NumMegaFilesDeleted: ActionStats.Type
    NumDirsDeleted: ActionStats.Type
    NumFileFragmentsDeleted: ActionStats.Type
    NumMegachunkCreated: ActionStats.Type
    NumExtentsDedupped: ActionStats.Type
    NumNonEmptyChunkFilesDeleted: ActionStats.Type
    NumChunkFilesEncodedToContainer: ActionStats.Type
    NumContainersCreated: ActionStats.Type
    NumCloudChunkFilesFixed: ActionStats.Type
    NumCloudChunksDeleted: ActionStats.Type
    NumCloudNodesDeleted: ActionStats.Type
    ChunkFileAccessTableUpdated: ActionStats.Type
    NumChunkFilePinSecsUpdated: ActionStats.Type
    NumIceboxStubViewsDeleted: ActionStats.Type
    NumCloudChunkFilesLCMed: ActionStats.Type
    NumGarbageChunksMigrated: ActionStats.Type
    NumGarbageChunksWithMigrateErrors: ActionStats.Type
    NumDeleteScribeRangeIssued: ActionStats.Type
    NumContainersFixed: ActionStats.Type
    NumContainersDeleted: ActionStats.Type
    NumS3ObjectsTimestampVecFixed: ActionStats.Type
    NumS3ObjectsFailedToFixTimestampVec: ActionStats.Type
    NumS3EntitiesLifecycled: ActionStats.Type
    LogicalBytesS3EntitiesLifecycled: ActionStats.Type
    NumS3EntitiesFailedToLifecycle: ActionStats.Type
    NumChunksDeletedKCASErrors: ActionStats.Type
    NumChunkFilesWithCASError: ActionStats.Type
    CASErrorNumChunksMigrated: ActionStats.Type
    CASErrorMigratedBytesPhysical: ActionStats.Type
    NumBridgeAssignmentsFailed: ActionStats.Type
    S3ObjectSnapTreeInvalidRefcount: ActionStats.Type
    S3ObjectSnapTreeNodesDeleted: ActionStats.Type
    ValidateBrickOwnedChunkMappingNumBricksFixed: ActionStats.Type
    ValidateBrickOwnedChunkMappingNumBricksSkipped: ActionStats.Type
    ValidateBrickOwnedChunkMappingNumBricksAccurate: ActionStats.Type
    ValidateBrickOwnedChunkMappingNumBrickUpdateErrors: ActionStats.Type
    ValidateBrickOwnedChunkMappingNumExistingActiveOpClocks: ActionStats.Type
    ValidateBrickOwnedChunkMappingNumChunkFileIdsSet: ActionStats.Type
    ValidateBrickOwnedChunkMappingNumChunkFileIdsCleared: ActionStats.Type
    NumCloudChunkFileValidationsProcessed: ActionStats.Type
    NumMissingCloudChunkFiles: ActionStats.Type
    NumIceboxCSRObjectsValidated: ActionStats.Type
    NumArchiveMetadataDeleted: ActionStats.Type
    NumChunksDeletedKNonExistentErrors: ActionStats.Type
    NumBookkeeperV2AggregatedGroups: ActionStats.Type
    NumIceboxMissingCSRNodes: ActionStats.Type
    NumMissingCloudChunks: ActionStats.Type
    NumCorruptCloudChunks: ActionStats.Type
    NumS3ObjectVersionsLifecycled: ActionStats.Type
    LogicalBytesS3ObjectVersionsLifecycled: ActionStats.Type
    NumS3IncompleteMultipartUploadsLifecycled: ActionStats.Type
    LogicalBytesS3IncompleteMultipartUploadsLifecycled: ActionStats.Type
    NumBookkeeperV2EntitiesDeleted: ActionStats.Type
    NumBookkeeperV2ExternalViewGroupsAssigned: ActionStats.Type
    NumBkV2GrpsBrickBytesLogicalUpdated: ActionStats.Type
    NumUptieredCloudChunkFilesDowntiered: ActionStats.Type
    NumIceboxUndeletedCSRNodes: ActionStats.Type
    NumBkV2SpecialGroupsStatsUpdated: ActionStats.Type
    DirQuotaSnapTreeInvalidRefcount: ActionStats.Type
    DirQuotaSnapTreeNodesDeleted: ActionStats.Type
    FilerLcmNumFilesDeleted: ActionStats.Type
    FilerLcmNumBytesRemoved: ActionStats.Type
    FilerLcmNumDirectoriesRemoved: ActionStats.Type
    FilerLcmNumEntitesFailedToDelete: ActionStats.Type
    class ErrorOffset(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kBridgeError: _ClassVar[ActionStats.ErrorOffset]
        kScribeError: _ClassVar[ActionStats.ErrorOffset]
        kGandalfError: _ClassVar[ActionStats.ErrorOffset]
        kStatsError: _ClassVar[ActionStats.ErrorOffset]
        kBookkeeperError: _ClassVar[ActionStats.ErrorOffset]
        kBookkeeperV2Error: _ClassVar[ActionStats.ErrorOffset]
        kOtherError: _ClassVar[ActionStats.ErrorOffset]
    kBridgeError: ActionStats.ErrorOffset
    kScribeError: ActionStats.ErrorOffset
    kGandalfError: ActionStats.ErrorOffset
    kStatsError: ActionStats.ErrorOffset
    kBookkeeperError: ActionStats.ErrorOffset
    kBookkeeperV2Error: ActionStats.ErrorOffset
    kOtherError: ActionStats.ErrorOffset
    class ErrorCountMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    class SubtypeCountMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    TYPE_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    ERROR_COUNT_MAP_FIELD_NUMBER: _ClassVar[int]
    SUBTYPE_COUNT_MAP_FIELD_NUMBER: _ClassVar[int]
    type: ActionStats.Type
    value: int
    error_count_map: _containers.ScalarMap[int, int]
    subtype_count_map: _containers.ScalarMap[str, int]
    def __init__(self, type: _Optional[_Union[ActionStats.Type, str]] = ..., value: _Optional[int] = ..., error_count_map: _Optional[_Mapping[int, int]] = ..., subtype_count_map: _Optional[_Mapping[str, int]] = ...) -> None: ...
