from bridge.snap_fs import entity_handle_pb2 as _entity_handle_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BookkeeperEntityProto(_message.Message):
    __slots__ = ("view_id", "entity_handle")
    VIEW_ID_FIELD_NUMBER: _ClassVar[int]
    ENTITY_HANDLE_FIELD_NUMBER: _ClassVar[int]
    view_id: int
    entity_handle: _entity_handle_pb2.EntityHandleProto
    def __init__(self, view_id: _Optional[int] = ..., entity_handle: _Optional[_Union[_entity_handle_pb2.EntityHandleProto, _Mapping]] = ...) -> None: ...

class LogicalStats(_message.Message):
    __slots__ = ("inode_bytes_logical", "num_files", "num_dirs", "num_minion_files", "minion_files_usage", "num_mega_files", "mega_files_usage", "num_regular_files", "regular_files_usage", "num_special_inodes", "brick_bytes_logical", "minion_brick_bytes_logical")
    INODE_BYTES_LOGICAL_FIELD_NUMBER: _ClassVar[int]
    NUM_FILES_FIELD_NUMBER: _ClassVar[int]
    NUM_DIRS_FIELD_NUMBER: _ClassVar[int]
    NUM_MINION_FILES_FIELD_NUMBER: _ClassVar[int]
    MINION_FILES_USAGE_FIELD_NUMBER: _ClassVar[int]
    NUM_MEGA_FILES_FIELD_NUMBER: _ClassVar[int]
    MEGA_FILES_USAGE_FIELD_NUMBER: _ClassVar[int]
    NUM_REGULAR_FILES_FIELD_NUMBER: _ClassVar[int]
    REGULAR_FILES_USAGE_FIELD_NUMBER: _ClassVar[int]
    NUM_SPECIAL_INODES_FIELD_NUMBER: _ClassVar[int]
    BRICK_BYTES_LOGICAL_FIELD_NUMBER: _ClassVar[int]
    MINION_BRICK_BYTES_LOGICAL_FIELD_NUMBER: _ClassVar[int]
    inode_bytes_logical: int
    num_files: int
    num_dirs: int
    num_minion_files: int
    minion_files_usage: int
    num_mega_files: int
    mega_files_usage: int
    num_regular_files: int
    regular_files_usage: int
    num_special_inodes: int
    brick_bytes_logical: int
    minion_brick_bytes_logical: int
    def __init__(self, inode_bytes_logical: _Optional[int] = ..., num_files: _Optional[int] = ..., num_dirs: _Optional[int] = ..., num_minion_files: _Optional[int] = ..., minion_files_usage: _Optional[int] = ..., num_mega_files: _Optional[int] = ..., mega_files_usage: _Optional[int] = ..., num_regular_files: _Optional[int] = ..., regular_files_usage: _Optional[int] = ..., num_special_inodes: _Optional[int] = ..., brick_bytes_logical: _Optional[int] = ..., minion_brick_bytes_logical: _Optional[int] = ...) -> None: ...

class PhysicalStats(_message.Message):
    __slots__ = ("local_stats", "cloud_stats", "brick_bytes_logical")
    class Metric(_message.Message):
        __slots__ = ("attributed_physical_bytes", "attributed_morphed_bytes", "attributed_logical_bytes", "ideal_resiliency_overhead_bytes", "unique_attributed_physical_bytes", "unique_attributed_morphed_bytes", "unique_attributed_logical_bytes")
        ATTRIBUTED_PHYSICAL_BYTES_FIELD_NUMBER: _ClassVar[int]
        ATTRIBUTED_MORPHED_BYTES_FIELD_NUMBER: _ClassVar[int]
        ATTRIBUTED_LOGICAL_BYTES_FIELD_NUMBER: _ClassVar[int]
        IDEAL_RESILIENCY_OVERHEAD_BYTES_FIELD_NUMBER: _ClassVar[int]
        UNIQUE_ATTRIBUTED_PHYSICAL_BYTES_FIELD_NUMBER: _ClassVar[int]
        UNIQUE_ATTRIBUTED_MORPHED_BYTES_FIELD_NUMBER: _ClassVar[int]
        UNIQUE_ATTRIBUTED_LOGICAL_BYTES_FIELD_NUMBER: _ClassVar[int]
        attributed_physical_bytes: float
        attributed_morphed_bytes: float
        attributed_logical_bytes: float
        ideal_resiliency_overhead_bytes: float
        unique_attributed_physical_bytes: float
        unique_attributed_morphed_bytes: float
        unique_attributed_logical_bytes: float
        def __init__(self, attributed_physical_bytes: _Optional[float] = ..., attributed_morphed_bytes: _Optional[float] = ..., attributed_logical_bytes: _Optional[float] = ..., ideal_resiliency_overhead_bytes: _Optional[float] = ..., unique_attributed_physical_bytes: _Optional[float] = ..., unique_attributed_morphed_bytes: _Optional[float] = ..., unique_attributed_logical_bytes: _Optional[float] = ...) -> None: ...
    LOCAL_STATS_FIELD_NUMBER: _ClassVar[int]
    CLOUD_STATS_FIELD_NUMBER: _ClassVar[int]
    BRICK_BYTES_LOGICAL_FIELD_NUMBER: _ClassVar[int]
    local_stats: PhysicalStats.Metric
    cloud_stats: PhysicalStats.Metric
    brick_bytes_logical: int
    def __init__(self, local_stats: _Optional[_Union[PhysicalStats.Metric, _Mapping]] = ..., cloud_stats: _Optional[_Union[PhysicalStats.Metric, _Mapping]] = ..., brick_bytes_logical: _Optional[int] = ...) -> None: ...

class IOStats(_message.Message):
    __slots__ = ("actual_write_bytes", "requested_write_bytes", "data_read", "data_written")
    ACTUAL_WRITE_BYTES_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_WRITE_BYTES_FIELD_NUMBER: _ClassVar[int]
    DATA_READ_FIELD_NUMBER: _ClassVar[int]
    DATA_WRITTEN_FIELD_NUMBER: _ClassVar[int]
    actual_write_bytes: int
    requested_write_bytes: int
    data_read: int
    data_written: int
    def __init__(self, actual_write_bytes: _Optional[int] = ..., requested_write_bytes: _Optional[int] = ..., data_read: _Optional[int] = ..., data_written: _Optional[int] = ...) -> None: ...

class GroupInfo(_message.Message):
    __slots__ = ("is_leaf", "group_name", "type", "marked_for_deletion", "publish_stats", "bk_v2_grp_id", "deleted_timestamp_usecs")
    IS_LEAF_FIELD_NUMBER: _ClassVar[int]
    GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    MARKED_FOR_DELETION_FIELD_NUMBER: _ClassVar[int]
    PUBLISH_STATS_FIELD_NUMBER: _ClassVar[int]
    BK_V2_GRP_ID_FIELD_NUMBER: _ClassVar[int]
    DELETED_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
    is_leaf: bool
    group_name: str
    type: str
    marked_for_deletion: bool
    publish_stats: bool
    bk_v2_grp_id: str
    deleted_timestamp_usecs: int
    def __init__(self, is_leaf: bool = ..., group_name: _Optional[str] = ..., type: _Optional[str] = ..., marked_for_deletion: bool = ..., publish_stats: bool = ..., bk_v2_grp_id: _Optional[str] = ..., deleted_timestamp_usecs: _Optional[int] = ...) -> None: ...

class GroupMetadataStats(_message.Message):
    __slots__ = ("num_entities", "num_leaf_objects")
    NUM_ENTITIES_FIELD_NUMBER: _ClassVar[int]
    NUM_LEAF_OBJECTS_FIELD_NUMBER: _ClassVar[int]
    num_entities: int
    num_leaf_objects: int
    def __init__(self, num_entities: _Optional[int] = ..., num_leaf_objects: _Optional[int] = ...) -> None: ...

class ParentGroupIdsProto(_message.Message):
    __slots__ = ("parent_grp_id_vec",)
    PARENT_GRP_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    parent_grp_id_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, parent_grp_id_vec: _Optional[_Iterable[str]] = ...) -> None: ...

class DeleteBkV2EntityProto(_message.Message):
    __slots__ = ("marked_for_deletion", "deleted_timestamp_usecs")
    MARKED_FOR_DELETION_FIELD_NUMBER: _ClassVar[int]
    DELETED_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
    marked_for_deletion: bool
    deleted_timestamp_usecs: int
    def __init__(self, marked_for_deletion: bool = ..., deleted_timestamp_usecs: _Optional[int] = ...) -> None: ...

class BookkeeperV2StatsInfoProto(_message.Message):
    __slots__ = ("leaf_group_stats_version", "parent_group_stats_version")
    LEAF_GROUP_STATS_VERSION_FIELD_NUMBER: _ClassVar[int]
    PARENT_GROUP_STATS_VERSION_FIELD_NUMBER: _ClassVar[int]
    leaf_group_stats_version: str
    parent_group_stats_version: str
    def __init__(self, leaf_group_stats_version: _Optional[str] = ..., parent_group_stats_version: _Optional[str] = ...) -> None: ...

class BkV2PipelineInput(_message.Message):
    __slots__ = ("input_blob", "predicate_type")
    class PredicateType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kQueryTopN: _ClassVar[BkV2PipelineInput.PredicateType]
        kScanAllObjects: _ClassVar[BkV2PipelineInput.PredicateType]
    kQueryTopN: BkV2PipelineInput.PredicateType
    kScanAllObjects: BkV2PipelineInput.PredicateType
    INPUT_BLOB_FIELD_NUMBER: _ClassVar[int]
    PREDICATE_TYPE_FIELD_NUMBER: _ClassVar[int]
    input_blob: str
    predicate_type: BkV2PipelineInput.PredicateType
    def __init__(self, input_blob: _Optional[str] = ..., predicate_type: _Optional[_Union[BkV2PipelineInput.PredicateType, str]] = ...) -> None: ...

class GroupStats(_message.Message):
    __slots__ = ("group_metadata_stats", "io_stats", "logical_stats", "physical_stats", "group_info")
    GROUP_METADATA_STATS_FIELD_NUMBER: _ClassVar[int]
    IO_STATS_FIELD_NUMBER: _ClassVar[int]
    LOGICAL_STATS_FIELD_NUMBER: _ClassVar[int]
    PHYSICAL_STATS_FIELD_NUMBER: _ClassVar[int]
    GROUP_INFO_FIELD_NUMBER: _ClassVar[int]
    group_metadata_stats: GroupMetadataStats
    io_stats: IOStats
    logical_stats: LogicalStats
    physical_stats: PhysicalStats
    group_info: GroupInfo
    def __init__(self, group_metadata_stats: _Optional[_Union[GroupMetadataStats, _Mapping]] = ..., io_stats: _Optional[_Union[IOStats, _Mapping]] = ..., logical_stats: _Optional[_Union[LogicalStats, _Mapping]] = ..., physical_stats: _Optional[_Union[PhysicalStats, _Mapping]] = ..., group_info: _Optional[_Union[GroupInfo, _Mapping]] = ...) -> None: ...

class ConstantsProto(_message.Message):
    __slots__ = ("group_metadata", "parent_group_ids", "logical_stats_1", "logical_stats_2", "physical_stats_1", "physical_stats_2", "io_stats", "group_info", "group_metadata_stats", "group_id", "stats_ptr_1", "stats_ptr_2", "bookkeeper_v2_group_stats_info_key", "query_status", "last_updated_timestamp", "query_result", "parent_grp_id_prefix", "tenant_grp_id_prefix", "leaf_grp_id_prefix", "delete_info", "external_view_grp_id_prefix", "result_batch_size", "bookkeeper_v2_query_pipeline_mr_result_column", "bookkeeper_v2_query_pipeline_mr_result_key")
    class QueryStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kPipelineScheduled: _ClassVar[ConstantsProto.QueryStatus]
        kPipelineInProgress: _ClassVar[ConstantsProto.QueryStatus]
        kQueryCompleted: _ClassVar[ConstantsProto.QueryStatus]
        kDefault: _ClassVar[ConstantsProto.QueryStatus]
    kPipelineScheduled: ConstantsProto.QueryStatus
    kPipelineInProgress: ConstantsProto.QueryStatus
    kQueryCompleted: ConstantsProto.QueryStatus
    kDefault: ConstantsProto.QueryStatus
    GROUP_METADATA_FIELD_NUMBER: _ClassVar[int]
    PARENT_GROUP_IDS_FIELD_NUMBER: _ClassVar[int]
    LOGICAL_STATS_1_FIELD_NUMBER: _ClassVar[int]
    LOGICAL_STATS_2_FIELD_NUMBER: _ClassVar[int]
    PHYSICAL_STATS_1_FIELD_NUMBER: _ClassVar[int]
    PHYSICAL_STATS_2_FIELD_NUMBER: _ClassVar[int]
    IO_STATS_FIELD_NUMBER: _ClassVar[int]
    GROUP_INFO_FIELD_NUMBER: _ClassVar[int]
    GROUP_METADATA_STATS_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    STATS_PTR_1_FIELD_NUMBER: _ClassVar[int]
    STATS_PTR_2_FIELD_NUMBER: _ClassVar[int]
    BOOKKEEPER_V2_GROUP_STATS_INFO_KEY_FIELD_NUMBER: _ClassVar[int]
    QUERY_STATUS_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATED_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    QUERY_RESULT_FIELD_NUMBER: _ClassVar[int]
    PARENT_GRP_ID_PREFIX_FIELD_NUMBER: _ClassVar[int]
    TENANT_GRP_ID_PREFIX_FIELD_NUMBER: _ClassVar[int]
    LEAF_GRP_ID_PREFIX_FIELD_NUMBER: _ClassVar[int]
    DELETE_INFO_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_VIEW_GRP_ID_PREFIX_FIELD_NUMBER: _ClassVar[int]
    RESULT_BATCH_SIZE_FIELD_NUMBER: _ClassVar[int]
    BOOKKEEPER_V2_QUERY_PIPELINE_MR_RESULT_COLUMN_FIELD_NUMBER: _ClassVar[int]
    BOOKKEEPER_V2_QUERY_PIPELINE_MR_RESULT_KEY_FIELD_NUMBER: _ClassVar[int]
    group_metadata: str
    parent_group_ids: str
    logical_stats_1: str
    logical_stats_2: str
    physical_stats_1: str
    physical_stats_2: str
    io_stats: str
    group_info: str
    group_metadata_stats: str
    group_id: str
    stats_ptr_1: str
    stats_ptr_2: str
    bookkeeper_v2_group_stats_info_key: str
    query_status: str
    last_updated_timestamp: str
    query_result: str
    parent_grp_id_prefix: str
    tenant_grp_id_prefix: str
    leaf_grp_id_prefix: str
    delete_info: str
    external_view_grp_id_prefix: str
    result_batch_size: str
    bookkeeper_v2_query_pipeline_mr_result_column: str
    bookkeeper_v2_query_pipeline_mr_result_key: str
    def __init__(self, group_metadata: _Optional[str] = ..., parent_group_ids: _Optional[str] = ..., logical_stats_1: _Optional[str] = ..., logical_stats_2: _Optional[str] = ..., physical_stats_1: _Optional[str] = ..., physical_stats_2: _Optional[str] = ..., io_stats: _Optional[str] = ..., group_info: _Optional[str] = ..., group_metadata_stats: _Optional[str] = ..., group_id: _Optional[str] = ..., stats_ptr_1: _Optional[str] = ..., stats_ptr_2: _Optional[str] = ..., bookkeeper_v2_group_stats_info_key: _Optional[str] = ..., query_status: _Optional[str] = ..., last_updated_timestamp: _Optional[str] = ..., query_result: _Optional[str] = ..., parent_grp_id_prefix: _Optional[str] = ..., tenant_grp_id_prefix: _Optional[str] = ..., leaf_grp_id_prefix: _Optional[str] = ..., delete_info: _Optional[str] = ..., external_view_grp_id_prefix: _Optional[str] = ..., result_batch_size: _Optional[str] = ..., bookkeeper_v2_query_pipeline_mr_result_column: _Optional[str] = ..., bookkeeper_v2_query_pipeline_mr_result_key: _Optional[str] = ...) -> None: ...
