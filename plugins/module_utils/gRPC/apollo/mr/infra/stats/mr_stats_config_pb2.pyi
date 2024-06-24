from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class UsageMetricsProto(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kBrickBytesLogical: _ClassVar[UsageMetricsProto.Type]
        kChunkBytesLogical: _ClassVar[UsageMetricsProto.Type]
        kChunkBytesMorphed: _ClassVar[UsageMetricsProto.Type]
        kChunkBytesPhysical: _ClassVar[UsageMetricsProto.Type]
        kStorageConsumedBytes: _ClassVar[UsageMetricsProto.Type]
        kCapacityBytes: _ClassVar[UsageMetricsProto.Type]
        kLocalTierResiliencyOverheadBytes: _ClassVar[UsageMetricsProto.Type]
        kLocalTierChunkBytesMorphed: _ClassVar[UsageMetricsProto.Type]
        kLogicalSizeBytes: _ClassVar[UsageMetricsProto.Type]
        kNumFiles: _ClassVar[UsageMetricsProto.Type]
        kNumDirectories: _ClassVar[UsageMetricsProto.Type]
        kUniqueChunkBytesPhysical: _ClassVar[UsageMetricsProto.Type]
        kCloudChunkBytesMorphed: _ClassVar[UsageMetricsProto.Type]
        kLocalChunkBytesMorphed: _ClassVar[UsageMetricsProto.Type]
        kCloudStorageConsumedBytes: _ClassVar[UsageMetricsProto.Type]
        kLocalStorageConsumedBytes: _ClassVar[UsageMetricsProto.Type]
        kInodeBytesLogical: _ClassVar[UsageMetricsProto.Type]
        kLocalUniqueChunkBytesMorphed: _ClassVar[UsageMetricsProto.Type]
    kBrickBytesLogical: UsageMetricsProto.Type
    kChunkBytesLogical: UsageMetricsProto.Type
    kChunkBytesMorphed: UsageMetricsProto.Type
    kChunkBytesPhysical: UsageMetricsProto.Type
    kStorageConsumedBytes: UsageMetricsProto.Type
    kCapacityBytes: UsageMetricsProto.Type
    kLocalTierResiliencyOverheadBytes: UsageMetricsProto.Type
    kLocalTierChunkBytesMorphed: UsageMetricsProto.Type
    kLogicalSizeBytes: UsageMetricsProto.Type
    kNumFiles: UsageMetricsProto.Type
    kNumDirectories: UsageMetricsProto.Type
    kUniqueChunkBytesPhysical: UsageMetricsProto.Type
    kCloudChunkBytesMorphed: UsageMetricsProto.Type
    kLocalChunkBytesMorphed: UsageMetricsProto.Type
    kCloudStorageConsumedBytes: UsageMetricsProto.Type
    kLocalStorageConsumedBytes: UsageMetricsProto.Type
    kInodeBytesLogical: UsageMetricsProto.Type
    kLocalUniqueChunkBytesMorphed: UsageMetricsProto.Type
    def __init__(self) -> None: ...

class StatsSchemaProto(_message.Message):
    __slots__ = ("schema_name", "metric_name", "int_entity_id", "str_entity_id")
    SCHEMA_NAME_FIELD_NUMBER: _ClassVar[int]
    METRIC_NAME_FIELD_NUMBER: _ClassVar[int]
    INT_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    STR_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    schema_name: str
    metric_name: str
    int_entity_id: int
    str_entity_id: str
    def __init__(self, schema_name: _Optional[str] = ..., metric_name: _Optional[str] = ..., int_entity_id: _Optional[int] = ..., str_entity_id: _Optional[str] = ...) -> None: ...

class SchemaNamesProto(_message.Message):
    __slots__ = ("apollo_cluster_stats_schema_name", "apollo_storage_domain_stats_schema_name", "bookkeeper_stats_schema_name")
    APOLLO_CLUSTER_STATS_SCHEMA_NAME_FIELD_NUMBER: _ClassVar[int]
    APOLLO_STORAGE_DOMAIN_STATS_SCHEMA_NAME_FIELD_NUMBER: _ClassVar[int]
    BOOKKEEPER_STATS_SCHEMA_NAME_FIELD_NUMBER: _ClassVar[int]
    apollo_cluster_stats_schema_name: str
    apollo_storage_domain_stats_schema_name: str
    bookkeeper_stats_schema_name: str
    def __init__(self, apollo_cluster_stats_schema_name: _Optional[str] = ..., apollo_storage_domain_stats_schema_name: _Optional[str] = ..., bookkeeper_stats_schema_name: _Optional[str] = ...) -> None: ...
