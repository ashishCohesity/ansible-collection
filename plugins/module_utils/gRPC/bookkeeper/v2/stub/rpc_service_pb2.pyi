from bookkeeper.v2.base import bookkeeper_v2_pb2 as _bookkeeper_v2_pb2
from bookkeeper.v2.base import bookkeeper_v2_special_groups_pb2 as _bookkeeper_v2_special_groups_pb2
from bookkeeper.v2.base import error_pb2 as _error_pb2
from open_util.net import protorpc_pb2 as _protorpc_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ReserveGroupIdArg(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ReserveGroupIdResult(_message.Message):
    __slots__ = ("group_id",)
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    group_id: int
    def __init__(self, group_id: _Optional[int] = ...) -> None: ...

class GetBookkeeperV2ClusterStatsArg(_message.Message):
    __slots__ = ("entity_name",)
    ENTITY_NAME_FIELD_NUMBER: _ClassVar[int]
    entity_name: str
    def __init__(self, entity_name: _Optional[str] = ...) -> None: ...

class GetBookkeeperV2ClusterStatsResult(_message.Message):
    __slots__ = ("logical_stats", "physical_stats")
    LOGICAL_STATS_FIELD_NUMBER: _ClassVar[int]
    PHYSICAL_STATS_FIELD_NUMBER: _ClassVar[int]
    logical_stats: _bookkeeper_v2_pb2.LogicalStats
    physical_stats: _bookkeeper_v2_pb2.PhysicalStats
    def __init__(self, logical_stats: _Optional[_Union[_bookkeeper_v2_pb2.LogicalStats, _Mapping]] = ..., physical_stats: _Optional[_Union[_bookkeeper_v2_pb2.PhysicalStats, _Mapping]] = ...) -> None: ...

class CreateBookkeeperGroupArg(_message.Message):
    __slots__ = ("opaque_metadata", "group_name", "group_type", "publish_stats", "is_leaf", "actual_write_bytes", "requested_write_bytes", "data_read", "data_written", "bk_v2_grp_id", "parent_grp_id_vec")
    OPAQUE_METADATA_FIELD_NUMBER: _ClassVar[int]
    GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    GROUP_TYPE_FIELD_NUMBER: _ClassVar[int]
    PUBLISH_STATS_FIELD_NUMBER: _ClassVar[int]
    IS_LEAF_FIELD_NUMBER: _ClassVar[int]
    ACTUAL_WRITE_BYTES_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_WRITE_BYTES_FIELD_NUMBER: _ClassVar[int]
    DATA_READ_FIELD_NUMBER: _ClassVar[int]
    DATA_WRITTEN_FIELD_NUMBER: _ClassVar[int]
    BK_V2_GRP_ID_FIELD_NUMBER: _ClassVar[int]
    PARENT_GRP_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    opaque_metadata: bytes
    group_name: str
    group_type: str
    publish_stats: bool
    is_leaf: bool
    actual_write_bytes: int
    requested_write_bytes: int
    data_read: int
    data_written: int
    bk_v2_grp_id: str
    parent_grp_id_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, opaque_metadata: _Optional[bytes] = ..., group_name: _Optional[str] = ..., group_type: _Optional[str] = ..., publish_stats: bool = ..., is_leaf: bool = ..., actual_write_bytes: _Optional[int] = ..., requested_write_bytes: _Optional[int] = ..., data_read: _Optional[int] = ..., data_written: _Optional[int] = ..., bk_v2_grp_id: _Optional[str] = ..., parent_grp_id_vec: _Optional[_Iterable[str]] = ...) -> None: ...

class CreateBookkeeperGroupResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UpdateBookkeeperGroupArg(_message.Message):
    __slots__ = ("opaque_metadata", "group_type", "group_name", "io_stats", "group_metadata_stats", "logical_stats", "physical_stats", "stats_version", "bk_v2_grp_id", "parent_grp_id_vec")
    OPAQUE_METADATA_FIELD_NUMBER: _ClassVar[int]
    GROUP_TYPE_FIELD_NUMBER: _ClassVar[int]
    GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    IO_STATS_FIELD_NUMBER: _ClassVar[int]
    GROUP_METADATA_STATS_FIELD_NUMBER: _ClassVar[int]
    LOGICAL_STATS_FIELD_NUMBER: _ClassVar[int]
    PHYSICAL_STATS_FIELD_NUMBER: _ClassVar[int]
    STATS_VERSION_FIELD_NUMBER: _ClassVar[int]
    BK_V2_GRP_ID_FIELD_NUMBER: _ClassVar[int]
    PARENT_GRP_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    opaque_metadata: bytes
    group_type: str
    group_name: str
    io_stats: _bookkeeper_v2_pb2.IOStats
    group_metadata_stats: _bookkeeper_v2_pb2.GroupMetadataStats
    logical_stats: _bookkeeper_v2_pb2.LogicalStats
    physical_stats: _bookkeeper_v2_pb2.PhysicalStats
    stats_version: str
    bk_v2_grp_id: str
    parent_grp_id_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, opaque_metadata: _Optional[bytes] = ..., group_type: _Optional[str] = ..., group_name: _Optional[str] = ..., io_stats: _Optional[_Union[_bookkeeper_v2_pb2.IOStats, _Mapping]] = ..., group_metadata_stats: _Optional[_Union[_bookkeeper_v2_pb2.GroupMetadataStats, _Mapping]] = ..., logical_stats: _Optional[_Union[_bookkeeper_v2_pb2.LogicalStats, _Mapping]] = ..., physical_stats: _Optional[_Union[_bookkeeper_v2_pb2.PhysicalStats, _Mapping]] = ..., stats_version: _Optional[str] = ..., bk_v2_grp_id: _Optional[str] = ..., parent_grp_id_vec: _Optional[_Iterable[str]] = ...) -> None: ...

class UpdateBookkeeperGroupResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class LookupBookkeeperV2GroupArg(_message.Message):
    __slots__ = ("get_stats", "get_group_info", "get_parent_group_ids", "stats_version", "bk_v2_grp_id")
    GET_STATS_FIELD_NUMBER: _ClassVar[int]
    GET_GROUP_INFO_FIELD_NUMBER: _ClassVar[int]
    GET_PARENT_GROUP_IDS_FIELD_NUMBER: _ClassVar[int]
    STATS_VERSION_FIELD_NUMBER: _ClassVar[int]
    BK_V2_GRP_ID_FIELD_NUMBER: _ClassVar[int]
    get_stats: bool
    get_group_info: bool
    get_parent_group_ids: bool
    stats_version: str
    bk_v2_grp_id: str
    def __init__(self, get_stats: bool = ..., get_group_info: bool = ..., get_parent_group_ids: bool = ..., stats_version: _Optional[str] = ..., bk_v2_grp_id: _Optional[str] = ...) -> None: ...

class LookupBookkeeperV2GroupResult(_message.Message):
    __slots__ = ("error", "io_stats", "group_info", "group_metadata_stats", "parent_group_ids", "opaque_metadata", "scribe_row_version", "logical_stats", "physical_stats", "stats_version")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    IO_STATS_FIELD_NUMBER: _ClassVar[int]
    GROUP_INFO_FIELD_NUMBER: _ClassVar[int]
    GROUP_METADATA_STATS_FIELD_NUMBER: _ClassVar[int]
    PARENT_GROUP_IDS_FIELD_NUMBER: _ClassVar[int]
    OPAQUE_METADATA_FIELD_NUMBER: _ClassVar[int]
    SCRIBE_ROW_VERSION_FIELD_NUMBER: _ClassVar[int]
    LOGICAL_STATS_FIELD_NUMBER: _ClassVar[int]
    PHYSICAL_STATS_FIELD_NUMBER: _ClassVar[int]
    STATS_VERSION_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    io_stats: _bookkeeper_v2_pb2.IOStats
    group_info: _bookkeeper_v2_pb2.GroupInfo
    group_metadata_stats: _bookkeeper_v2_pb2.GroupMetadataStats
    parent_group_ids: _bookkeeper_v2_pb2.ParentGroupIdsProto
    opaque_metadata: str
    scribe_row_version: int
    logical_stats: _bookkeeper_v2_pb2.LogicalStats
    physical_stats: _bookkeeper_v2_pb2.PhysicalStats
    stats_version: str
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., io_stats: _Optional[_Union[_bookkeeper_v2_pb2.IOStats, _Mapping]] = ..., group_info: _Optional[_Union[_bookkeeper_v2_pb2.GroupInfo, _Mapping]] = ..., group_metadata_stats: _Optional[_Union[_bookkeeper_v2_pb2.GroupMetadataStats, _Mapping]] = ..., parent_group_ids: _Optional[_Union[_bookkeeper_v2_pb2.ParentGroupIdsProto, _Mapping]] = ..., opaque_metadata: _Optional[str] = ..., scribe_row_version: _Optional[int] = ..., logical_stats: _Optional[_Union[_bookkeeper_v2_pb2.LogicalStats, _Mapping]] = ..., physical_stats: _Optional[_Union[_bookkeeper_v2_pb2.PhysicalStats, _Mapping]] = ..., stats_version: _Optional[str] = ...) -> None: ...

class AddEntitiesToBookkeeperGroupArg(_message.Message):
    __slots__ = ("entities", "bk_v2_grp_id")
    ENTITIES_FIELD_NUMBER: _ClassVar[int]
    BK_V2_GRP_ID_FIELD_NUMBER: _ClassVar[int]
    entities: _containers.RepeatedCompositeFieldContainer[_bookkeeper_v2_pb2.BookkeeperEntityProto]
    bk_v2_grp_id: str
    def __init__(self, entities: _Optional[_Iterable[_Union[_bookkeeper_v2_pb2.BookkeeperEntityProto, _Mapping]]] = ..., bk_v2_grp_id: _Optional[str] = ...) -> None: ...

class AddEntitiesToBookkeeperGroupResult(_message.Message):
    __slots__ = ("error", "entities_failed_to_add_vec", "error_vec")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ENTITIES_FAILED_TO_ADD_VEC_FIELD_NUMBER: _ClassVar[int]
    ERROR_VEC_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    entities_failed_to_add_vec: _containers.RepeatedCompositeFieldContainer[_bookkeeper_v2_pb2.BookkeeperEntityProto]
    error_vec: _containers.RepeatedCompositeFieldContainer[_error_pb2.ErrorProto]
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., entities_failed_to_add_vec: _Optional[_Iterable[_Union[_bookkeeper_v2_pb2.BookkeeperEntityProto, _Mapping]]] = ..., error_vec: _Optional[_Iterable[_Union[_error_pb2.ErrorProto, _Mapping]]] = ...) -> None: ...

class DeleteBookkeeperGroupArg(_message.Message):
    __slots__ = ("bk_v2_grp_id", "deleted_timestamp_usecs")
    BK_V2_GRP_ID_FIELD_NUMBER: _ClassVar[int]
    DELETED_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
    bk_v2_grp_id: str
    deleted_timestamp_usecs: int
    def __init__(self, bk_v2_grp_id: _Optional[str] = ..., deleted_timestamp_usecs: _Optional[int] = ...) -> None: ...

class DeleteBookkeeperGroupResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UpdateBkV2BrickBytesLogicalArg(_message.Message):
    __slots__ = ("bk_v2_grp_id", "brick_bytes_logical", "minion_brick_bytes_logical")
    BK_V2_GRP_ID_FIELD_NUMBER: _ClassVar[int]
    BRICK_BYTES_LOGICAL_FIELD_NUMBER: _ClassVar[int]
    MINION_BRICK_BYTES_LOGICAL_FIELD_NUMBER: _ClassVar[int]
    bk_v2_grp_id: str
    brick_bytes_logical: int
    minion_brick_bytes_logical: int
    def __init__(self, bk_v2_grp_id: _Optional[str] = ..., brick_bytes_logical: _Optional[int] = ..., minion_brick_bytes_logical: _Optional[int] = ...) -> None: ...

class UpdateBkV2BrickBytesLogicalResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CreateTenantBookkeeperGroupArg(_message.Message):
    __slots__ = ("tenant_id_str",)
    TENANT_ID_STR_FIELD_NUMBER: _ClassVar[int]
    tenant_id_str: str
    def __init__(self, tenant_id_str: _Optional[str] = ...) -> None: ...

class CreateTenantBookkeeperGroupResult(_message.Message):
    __slots__ = ("tenant_grp_id",)
    TENANT_GRP_ID_FIELD_NUMBER: _ClassVar[int]
    tenant_grp_id: str
    def __init__(self, tenant_grp_id: _Optional[str] = ...) -> None: ...

class LookupTenantBookkeeperGroupArg(_message.Message):
    __slots__ = ("tenant_id_str",)
    TENANT_ID_STR_FIELD_NUMBER: _ClassVar[int]
    tenant_id_str: str
    def __init__(self, tenant_id_str: _Optional[str] = ...) -> None: ...

class LookupTenantBookkeeperGroupResult(_message.Message):
    __slots__ = ("tenant_grp_id",)
    TENANT_GRP_ID_FIELD_NUMBER: _ClassVar[int]
    tenant_grp_id: str
    def __init__(self, tenant_grp_id: _Optional[str] = ...) -> None: ...

class GetAllObjectStatsArg(_message.Message):
    __slots__ = ("pagination_cookie",)
    PAGINATION_COOKIE_FIELD_NUMBER: _ClassVar[int]
    pagination_cookie: str
    def __init__(self, pagination_cookie: _Optional[str] = ...) -> None: ...

class GetAllObjectStatsResult(_message.Message):
    __slots__ = ("pagination_cookie", "group_info_vec")
    class GroupInfo(_message.Message):
        __slots__ = ("logical_stats", "physical_stats", "bk_v2_grp_id")
        LOGICAL_STATS_FIELD_NUMBER: _ClassVar[int]
        PHYSICAL_STATS_FIELD_NUMBER: _ClassVar[int]
        BK_V2_GRP_ID_FIELD_NUMBER: _ClassVar[int]
        logical_stats: _bookkeeper_v2_pb2.LogicalStats
        physical_stats: _bookkeeper_v2_pb2.PhysicalStats
        bk_v2_grp_id: str
        def __init__(self, logical_stats: _Optional[_Union[_bookkeeper_v2_pb2.LogicalStats, _Mapping]] = ..., physical_stats: _Optional[_Union[_bookkeeper_v2_pb2.PhysicalStats, _Mapping]] = ..., bk_v2_grp_id: _Optional[str] = ...) -> None: ...
    PAGINATION_COOKIE_FIELD_NUMBER: _ClassVar[int]
    GROUP_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    pagination_cookie: str
    group_info_vec: _containers.RepeatedCompositeFieldContainer[GetAllObjectStatsResult.GroupInfo]
    def __init__(self, pagination_cookie: _Optional[str] = ..., group_info_vec: _Optional[_Iterable[_Union[GetAllObjectStatsResult.GroupInfo, _Mapping]]] = ...) -> None: ...

class GetBookkeeperV2GroupStatsArg(_message.Message):
    __slots__ = ("bk_v2_grp_id",)
    BK_V2_GRP_ID_FIELD_NUMBER: _ClassVar[int]
    bk_v2_grp_id: str
    def __init__(self, bk_v2_grp_id: _Optional[str] = ...) -> None: ...

class GetBookkeeperV2GroupStatsResult(_message.Message):
    __slots__ = ("logical_stats", "physical_stats")
    LOGICAL_STATS_FIELD_NUMBER: _ClassVar[int]
    PHYSICAL_STATS_FIELD_NUMBER: _ClassVar[int]
    logical_stats: _bookkeeper_v2_pb2.LogicalStats
    physical_stats: _bookkeeper_v2_pb2.PhysicalStats
    def __init__(self, logical_stats: _Optional[_Union[_bookkeeper_v2_pb2.LogicalStats, _Mapping]] = ..., physical_stats: _Optional[_Union[_bookkeeper_v2_pb2.PhysicalStats, _Mapping]] = ...) -> None: ...

class GetStorageDomainStatsArg(_message.Message):
    __slots__ = ("storage_domain_id", "entity_name")
    STORAGE_DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    ENTITY_NAME_FIELD_NUMBER: _ClassVar[int]
    storage_domain_id: int
    entity_name: str
    def __init__(self, storage_domain_id: _Optional[int] = ..., entity_name: _Optional[str] = ...) -> None: ...

class GetStorageDomainStatsResult(_message.Message):
    __slots__ = ("logical_stats", "physical_stats")
    LOGICAL_STATS_FIELD_NUMBER: _ClassVar[int]
    PHYSICAL_STATS_FIELD_NUMBER: _ClassVar[int]
    logical_stats: _bookkeeper_v2_pb2.LogicalStats
    physical_stats: _bookkeeper_v2_pb2.PhysicalStats
    def __init__(self, logical_stats: _Optional[_Union[_bookkeeper_v2_pb2.LogicalStats, _Mapping]] = ..., physical_stats: _Optional[_Union[_bookkeeper_v2_pb2.PhysicalStats, _Mapping]] = ...) -> None: ...

class GetBookkeeperV2TenantStatsArg(_message.Message):
    __slots__ = ("tenant_id_str",)
    TENANT_ID_STR_FIELD_NUMBER: _ClassVar[int]
    tenant_id_str: str
    def __init__(self, tenant_id_str: _Optional[str] = ...) -> None: ...

class GetBookkeeperV2TenantStatsResult(_message.Message):
    __slots__ = ("logical_stats", "physical_stats")
    LOGICAL_STATS_FIELD_NUMBER: _ClassVar[int]
    PHYSICAL_STATS_FIELD_NUMBER: _ClassVar[int]
    logical_stats: _bookkeeper_v2_pb2.LogicalStats
    physical_stats: _bookkeeper_v2_pb2.PhysicalStats
    def __init__(self, logical_stats: _Optional[_Union[_bookkeeper_v2_pb2.LogicalStats, _Mapping]] = ..., physical_stats: _Optional[_Union[_bookkeeper_v2_pb2.PhysicalStats, _Mapping]] = ...) -> None: ...

class BookkeeperV2QueryStatsArg(_message.Message):
    __slots__ = ("query_type", "input_blob")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kQueryTopN: _ClassVar[BookkeeperV2QueryStatsArg.Type]
    kQueryTopN: BookkeeperV2QueryStatsArg.Type
    QUERY_TYPE_FIELD_NUMBER: _ClassVar[int]
    INPUT_BLOB_FIELD_NUMBER: _ClassVar[int]
    query_type: BookkeeperV2QueryStatsArg.Type
    input_blob: bytes
    def __init__(self, query_type: _Optional[_Union[BookkeeperV2QueryStatsArg.Type, str]] = ..., input_blob: _Optional[bytes] = ...) -> None: ...

class BookkeeperV2QueryStatsResult(_message.Message):
    __slots__ = ("error", "output_blob")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_BLOB_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    output_blob: bytes
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., output_blob: _Optional[bytes] = ...) -> None: ...

class MetricInfo(_message.Message):
    __slots__ = ("metric_info_val",)
    class MetricInfoEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kInodeBytesLogical: _ClassVar[MetricInfo.MetricInfoEnum]
        kBrickBytesLogical: _ClassVar[MetricInfo.MetricInfoEnum]
        kDataWritten: _ClassVar[MetricInfo.MetricInfoEnum]
        kDataRead: _ClassVar[MetricInfo.MetricInfoEnum]
    kInodeBytesLogical: MetricInfo.MetricInfoEnum
    kBrickBytesLogical: MetricInfo.MetricInfoEnum
    kDataWritten: MetricInfo.MetricInfoEnum
    kDataRead: MetricInfo.MetricInfoEnum
    METRIC_INFO_VAL_FIELD_NUMBER: _ClassVar[int]
    metric_info_val: MetricInfo.MetricInfoEnum
    def __init__(self, metric_info_val: _Optional[_Union[MetricInfo.MetricInfoEnum, str]] = ...) -> None: ...

class BookkeeperV2QueryTopNArg(_message.Message):
    __slots__ = ("top_n", "group_type", "metric_info", "parent_group_id", "parent_group_type")
    TOP_N_FIELD_NUMBER: _ClassVar[int]
    GROUP_TYPE_FIELD_NUMBER: _ClassVar[int]
    METRIC_INFO_FIELD_NUMBER: _ClassVar[int]
    PARENT_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    PARENT_GROUP_TYPE_FIELD_NUMBER: _ClassVar[int]
    top_n: int
    group_type: str
    metric_info: MetricInfo
    parent_group_id: str
    parent_group_type: str
    def __init__(self, top_n: _Optional[int] = ..., group_type: _Optional[str] = ..., metric_info: _Optional[_Union[MetricInfo, _Mapping]] = ..., parent_group_id: _Optional[str] = ..., parent_group_type: _Optional[str] = ...) -> None: ...

class BookkeeperV2QueryTopNResult(_message.Message):
    __slots__ = ("group_stats_vec",)
    GROUP_STATS_VEC_FIELD_NUMBER: _ClassVar[int]
    group_stats_vec: _containers.RepeatedCompositeFieldContainer[_bookkeeper_v2_pb2.GroupStats]
    def __init__(self, group_stats_vec: _Optional[_Iterable[_Union[_bookkeeper_v2_pb2.GroupStats, _Mapping]]] = ...) -> None: ...

class BookkeeperV2ScanStatsArg(_message.Message):
    __slots__ = ("query_type", "input_blob")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kGetAllTenantObjects: _ClassVar[BookkeeperV2ScanStatsArg.Type]
    kGetAllTenantObjects: BookkeeperV2ScanStatsArg.Type
    QUERY_TYPE_FIELD_NUMBER: _ClassVar[int]
    INPUT_BLOB_FIELD_NUMBER: _ClassVar[int]
    query_type: BookkeeperV2ScanStatsArg.Type
    input_blob: bytes
    def __init__(self, query_type: _Optional[_Union[BookkeeperV2ScanStatsArg.Type, str]] = ..., input_blob: _Optional[bytes] = ...) -> None: ...

class BookkeeperV2ScanStatsResult(_message.Message):
    __slots__ = ("error", "output_blob")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_BLOB_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    output_blob: bytes
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., output_blob: _Optional[bytes] = ...) -> None: ...

class ScanBookkeeperV2ObjectsArg(_message.Message):
    __slots__ = ("cursor", "target_group_type", "parent_group_id", "parent_group_type")
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    TARGET_GROUP_TYPE_FIELD_NUMBER: _ClassVar[int]
    PARENT_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    PARENT_GROUP_TYPE_FIELD_NUMBER: _ClassVar[int]
    cursor: str
    target_group_type: str
    parent_group_id: str
    parent_group_type: str
    def __init__(self, cursor: _Optional[str] = ..., target_group_type: _Optional[str] = ..., parent_group_id: _Optional[str] = ..., parent_group_type: _Optional[str] = ...) -> None: ...

class ScanBookkeeperV2ObjectsResult(_message.Message):
    __slots__ = ("group_stats_vec", "cursor")
    GROUP_STATS_VEC_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    group_stats_vec: _containers.RepeatedCompositeFieldContainer[_bookkeeper_v2_pb2.GroupStats]
    cursor: str
    def __init__(self, group_stats_vec: _Optional[_Iterable[_Union[_bookkeeper_v2_pb2.GroupStats, _Mapping]]] = ..., cursor: _Optional[str] = ...) -> None: ...

class UpdateSpecialGroupStatsArg(_message.Message):
    __slots__ = ("bkpr_v2_special_entity_proto",)
    BKPR_V2_SPECIAL_ENTITY_PROTO_FIELD_NUMBER: _ClassVar[int]
    bkpr_v2_special_entity_proto: _bookkeeper_v2_special_groups_pb2.BookkeeperV2SpecialEntityProto
    def __init__(self, bkpr_v2_special_entity_proto: _Optional[_Union[_bookkeeper_v2_special_groups_pb2.BookkeeperV2SpecialEntityProto, _Mapping]] = ...) -> None: ...

class UpdateSpecialGroupStatsResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetStorageDomainSpecialGroupsArg(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetStorageDomainSpecialGroupsResult(_message.Message):
    __slots__ = ("spl_grp_info_vec",)
    class SdSplGroupInfo(_message.Message):
        __slots__ = ("storage_domain_id", "entity_name", "group_id")
        STORAGE_DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
        ENTITY_NAME_FIELD_NUMBER: _ClassVar[int]
        GROUP_ID_FIELD_NUMBER: _ClassVar[int]
        storage_domain_id: int
        entity_name: str
        group_id: str
        def __init__(self, storage_domain_id: _Optional[int] = ..., entity_name: _Optional[str] = ..., group_id: _Optional[str] = ...) -> None: ...
    SPL_GRP_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    spl_grp_info_vec: _containers.RepeatedCompositeFieldContainer[GetStorageDomainSpecialGroupsResult.SdSplGroupInfo]
    def __init__(self, spl_grp_info_vec: _Optional[_Iterable[_Union[GetStorageDomainSpecialGroupsResult.SdSplGroupInfo, _Mapping]]] = ...) -> None: ...
