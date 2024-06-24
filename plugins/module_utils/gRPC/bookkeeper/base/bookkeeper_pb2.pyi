from bridge.snap_fs import entity_handle_pb2 as _entity_handle_pb2
from util.base import universal_id_pb2 as _universal_id_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ObjectProto(_message.Message):
    __slots__ = ("view_id", "namespace_root_name", "relative_file_path_vec")
    VIEW_ID_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_ROOT_NAME_FIELD_NUMBER: _ClassVar[int]
    RELATIVE_FILE_PATH_VEC_FIELD_NUMBER: _ClassVar[int]
    view_id: int
    namespace_root_name: str
    relative_file_path_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, view_id: _Optional[int] = ..., namespace_root_name: _Optional[str] = ..., relative_file_path_vec: _Optional[_Iterable[str]] = ...) -> None: ...

class ConsumerProto(_message.Message):
    __slots__ = ("type",)
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNone: _ClassVar[ConsumerProto.Type]
        kViews: _ClassVar[ConsumerProto.Type]
        kBackupRuns: _ClassVar[ConsumerProto.Type]
        kReplicationRuns: _ClassVar[ConsumerProto.Type]
        kObjects: _ClassVar[ConsumerProto.Type]
        kDataProtect: _ClassVar[ConsumerProto.Type]
        kDataPlatform: _ClassVar[ConsumerProto.Type]
        kViewProtectionRuns: _ClassVar[ConsumerProto.Type]
    kNone: ConsumerProto.Type
    kViews: ConsumerProto.Type
    kBackupRuns: ConsumerProto.Type
    kReplicationRuns: ConsumerProto.Type
    kObjects: ConsumerProto.Type
    kDataProtect: ConsumerProto.Type
    kDataPlatform: ConsumerProto.Type
    kViewProtectionRuns: ConsumerProto.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    type: ConsumerProto.Type
    def __init__(self, type: _Optional[_Union[ConsumerProto.Type, str]] = ...) -> None: ...

class ConsumerEntityProto(_message.Message):
    __slots__ = ("id", "name")
    class IdProto(_message.Message):
        __slots__ = ("id_int", "id_str", "uid")
        ID_INT_FIELD_NUMBER: _ClassVar[int]
        ID_STR_FIELD_NUMBER: _ClassVar[int]
        UID_FIELD_NUMBER: _ClassVar[int]
        id_int: int
        id_str: str
        uid: _universal_id_pb2.UniversalIdProto
        def __init__(self, id_int: _Optional[int] = ..., id_str: _Optional[str] = ..., uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: ConsumerEntityProto.IdProto
    name: str
    def __init__(self, id: _Optional[_Union[ConsumerEntityProto.IdProto, _Mapping]] = ..., name: _Optional[str] = ...) -> None: ...

class GroupAttributesProto(_message.Message):
    __slots__ = ("tenant_id_deprecated", "storage_domain_id", "consumer", "tenant_info")
    class TenantInfo(_message.Message):
        __slots__ = ("tenant_id_str", "null_tenant")
        TENANT_ID_STR_FIELD_NUMBER: _ClassVar[int]
        NULL_TENANT_FIELD_NUMBER: _ClassVar[int]
        tenant_id_str: str
        null_tenant: bool
        def __init__(self, tenant_id_str: _Optional[str] = ..., null_tenant: bool = ...) -> None: ...
    TENANT_ID_DEPRECATED_FIELD_NUMBER: _ClassVar[int]
    STORAGE_DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    CONSUMER_FIELD_NUMBER: _ClassVar[int]
    TENANT_INFO_FIELD_NUMBER: _ClassVar[int]
    tenant_id_deprecated: str
    storage_domain_id: int
    consumer: ConsumerProto
    tenant_info: GroupAttributesProto.TenantInfo
    def __init__(self, tenant_id_deprecated: _Optional[str] = ..., storage_domain_id: _Optional[int] = ..., consumer: _Optional[_Union[ConsumerProto, _Mapping]] = ..., tenant_info: _Optional[_Union[GroupAttributesProto.TenantInfo, _Mapping]] = ...) -> None: ...

class GroupConfigProto(_message.Message):
    __slots__ = ("stats_cfg", "auto_garbage_collect", "opaque_metadata", "stats_computation_interval_secs", "attributes", "consumer_entity", "old_group_id")
    class StatsConfig(_message.Message):
        __slots__ = ("ttl_secs",)
        TTL_SECS_FIELD_NUMBER: _ClassVar[int]
        ttl_secs: int
        def __init__(self, ttl_secs: _Optional[int] = ...) -> None: ...
    STATS_CFG_FIELD_NUMBER: _ClassVar[int]
    AUTO_GARBAGE_COLLECT_FIELD_NUMBER: _ClassVar[int]
    OPAQUE_METADATA_FIELD_NUMBER: _ClassVar[int]
    STATS_COMPUTATION_INTERVAL_SECS_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    CONSUMER_ENTITY_FIELD_NUMBER: _ClassVar[int]
    OLD_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    stats_cfg: GroupConfigProto.StatsConfig
    auto_garbage_collect: bool
    opaque_metadata: bytes
    stats_computation_interval_secs: int
    attributes: GroupAttributesProto
    consumer_entity: ConsumerEntityProto
    old_group_id: int
    def __init__(self, stats_cfg: _Optional[_Union[GroupConfigProto.StatsConfig, _Mapping]] = ..., auto_garbage_collect: bool = ..., opaque_metadata: _Optional[bytes] = ..., stats_computation_interval_secs: _Optional[int] = ..., attributes: _Optional[_Union[GroupAttributesProto, _Mapping]] = ..., consumer_entity: _Optional[_Union[ConsumerEntityProto, _Mapping]] = ..., old_group_id: _Optional[int] = ...) -> None: ...

class GroupStats(_message.Message):
    __slots__ = ("metric_map", "stats_timestamp_usecs")
    class Stat(_message.Message):
        __slots__ = ("value", "timestamp_usecs")
        VALUE_FIELD_NUMBER: _ClassVar[int]
        TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
        value: int
        timestamp_usecs: int
        def __init__(self, value: _Optional[int] = ..., timestamp_usecs: _Optional[int] = ...) -> None: ...
    class MetricMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: GroupStats.Stat
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[GroupStats.Stat, _Mapping]] = ...) -> None: ...
    METRIC_MAP_FIELD_NUMBER: _ClassVar[int]
    STATS_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
    metric_map: _containers.MessageMap[str, GroupStats.Stat]
    stats_timestamp_usecs: int
    def __init__(self, metric_map: _Optional[_Mapping[str, GroupStats.Stat]] = ..., stats_timestamp_usecs: _Optional[int] = ...) -> None: ...

class GroupStatusProto(_message.Message):
    __slots__ = ("last_scan_start_time_usecs", "stats", "create_time_usecs", "last_update_time_usecs")
    LAST_SCAN_START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    STATS_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATE_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    last_scan_start_time_usecs: int
    stats: GroupStats
    create_time_usecs: int
    last_update_time_usecs: int
    def __init__(self, last_scan_start_time_usecs: _Optional[int] = ..., stats: _Optional[_Union[GroupStats, _Mapping]] = ..., create_time_usecs: _Optional[int] = ..., last_update_time_usecs: _Optional[int] = ...) -> None: ...

class EnclosingGroupsProto(_message.Message):
    __slots__ = ("group_ids",)
    GROUP_IDS_FIELD_NUMBER: _ClassVar[int]
    group_ids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, group_ids: _Optional[_Iterable[int]] = ...) -> None: ...

class EntityHandlesProto(_message.Message):
    __slots__ = ("entity_handle_vec",)
    ENTITY_HANDLE_VEC_FIELD_NUMBER: _ClassVar[int]
    entity_handle_vec: _containers.RepeatedCompositeFieldContainer[_entity_handle_pb2.EntityHandleProto]
    def __init__(self, entity_handle_vec: _Optional[_Iterable[_Union[_entity_handle_pb2.EntityHandleProto, _Mapping]]] = ...) -> None: ...

class ConstantsProto(_message.Message):
    __slots__ = ("group_config_column_name", "group_status_column_name", "enclosing_groups_column_name", "entity_handles_column_name", "max_group_depth")
    GROUP_CONFIG_COLUMN_NAME_FIELD_NUMBER: _ClassVar[int]
    GROUP_STATUS_COLUMN_NAME_FIELD_NUMBER: _ClassVar[int]
    ENCLOSING_GROUPS_COLUMN_NAME_FIELD_NUMBER: _ClassVar[int]
    ENTITY_HANDLES_COLUMN_NAME_FIELD_NUMBER: _ClassVar[int]
    MAX_GROUP_DEPTH_FIELD_NUMBER: _ClassVar[int]
    group_config_column_name: str
    group_status_column_name: str
    enclosing_groups_column_name: str
    entity_handles_column_name: str
    max_group_depth: int
    def __init__(self, group_config_column_name: _Optional[str] = ..., group_status_column_name: _Optional[str] = ..., enclosing_groups_column_name: _Optional[str] = ..., entity_handles_column_name: _Optional[str] = ..., max_group_depth: _Optional[int] = ...) -> None: ...

class GroupSet(_message.Message):
    __slots__ = ("type",)
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kBase: _ClassVar[GroupSet.Type]
        kTenantStorageDomain: _ClassVar[GroupSet.Type]
        kStorageDomain: _ClassVar[GroupSet.Type]
        kTenant: _ClassVar[GroupSet.Type]
        kTenantConsumerStorageDomain: _ClassVar[GroupSet.Type]
        kTenantConsumer: _ClassVar[GroupSet.Type]
        kConsumerStorageDomain: _ClassVar[GroupSet.Type]
        kConsumer: _ClassVar[GroupSet.Type]
        kDataProtect: _ClassVar[GroupSet.Type]
        kNumGroupSetTypes: _ClassVar[GroupSet.Type]
    kBase: GroupSet.Type
    kTenantStorageDomain: GroupSet.Type
    kStorageDomain: GroupSet.Type
    kTenant: GroupSet.Type
    kTenantConsumerStorageDomain: GroupSet.Type
    kTenantConsumer: GroupSet.Type
    kConsumerStorageDomain: GroupSet.Type
    kConsumer: GroupSet.Type
    kDataProtect: GroupSet.Type
    kNumGroupSetTypes: GroupSet.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    type: GroupSet.Type
    def __init__(self, type: _Optional[_Union[GroupSet.Type, str]] = ...) -> None: ...
