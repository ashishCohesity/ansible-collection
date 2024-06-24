from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TableMetadataProto(_message.Message):
    __slots__ = ("tables", "tablets", "next_id", "migration_trigger_table_metadata_version", "scribe_tables_to_be_created_in_high_mem_usage_tablet", "scribe_low_mem_usage_tablet_ready", "last_table_migration_completion_ts", "scribe_history_tablet_ready")
    class Table(_message.Message):
        __slots__ = ("table_id", "table_name", "tablet_id", "target_tablet_id", "custom_hashing_scheme", "history_table", "block_reason")
        class HashingScheme(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kDefaultHashingScheme: _ClassVar[TableMetadataProto.Table.HashingScheme]
            kStatsTimeseriesPrefixHashingScheme: _ClassVar[TableMetadataProto.Table.HashingScheme]
            kStatsEntityPrefixHashingScheme: _ClassVar[TableMetadataProto.Table.HashingScheme]
            kStatsSchemaPrefixHashingScheme: _ClassVar[TableMetadataProto.Table.HashingScheme]
            kTestTablePrefixHashingScheme: _ClassVar[TableMetadataProto.Table.HashingScheme]
            kHistoryTablePrefixHashingScheme: _ClassVar[TableMetadataProto.Table.HashingScheme]
        kDefaultHashingScheme: TableMetadataProto.Table.HashingScheme
        kStatsTimeseriesPrefixHashingScheme: TableMetadataProto.Table.HashingScheme
        kStatsEntityPrefixHashingScheme: TableMetadataProto.Table.HashingScheme
        kStatsSchemaPrefixHashingScheme: TableMetadataProto.Table.HashingScheme
        kTestTablePrefixHashingScheme: TableMetadataProto.Table.HashingScheme
        kHistoryTablePrefixHashingScheme: TableMetadataProto.Table.HashingScheme
        class TableNameToHashingScheme(_message.Message):
            __slots__ = ("stats_timeseries_data", "stats_entity_meta", "stats_entity_schema", "bulk_write_test_0")
            STATS_TIMESERIES_DATA_FIELD_NUMBER: _ClassVar[int]
            STATS_ENTITY_META_FIELD_NUMBER: _ClassVar[int]
            STATS_ENTITY_SCHEMA_FIELD_NUMBER: _ClassVar[int]
            BULK_WRITE_TEST_0_FIELD_NUMBER: _ClassVar[int]
            stats_timeseries_data: TableMetadataProto.Table.HashingScheme
            stats_entity_meta: TableMetadataProto.Table.HashingScheme
            stats_entity_schema: TableMetadataProto.Table.HashingScheme
            bulk_write_test_0: TableMetadataProto.Table.HashingScheme
            def __init__(self, stats_timeseries_data: _Optional[_Union[TableMetadataProto.Table.HashingScheme, str]] = ..., stats_entity_meta: _Optional[_Union[TableMetadataProto.Table.HashingScheme, str]] = ..., stats_entity_schema: _Optional[_Union[TableMetadataProto.Table.HashingScheme, str]] = ..., bulk_write_test_0: _Optional[_Union[TableMetadataProto.Table.HashingScheme, str]] = ...) -> None: ...
        TABLE_ID_FIELD_NUMBER: _ClassVar[int]
        TABLE_NAME_FIELD_NUMBER: _ClassVar[int]
        TABLET_ID_FIELD_NUMBER: _ClassVar[int]
        TARGET_TABLET_ID_FIELD_NUMBER: _ClassVar[int]
        CUSTOM_HASHING_SCHEME_FIELD_NUMBER: _ClassVar[int]
        HISTORY_TABLE_FIELD_NUMBER: _ClassVar[int]
        BLOCK_REASON_FIELD_NUMBER: _ClassVar[int]
        table_id: int
        table_name: bytes
        tablet_id: int
        target_tablet_id: int
        custom_hashing_scheme: TableMetadataProto.Table.HashingScheme
        history_table: bool
        block_reason: str
        def __init__(self, table_id: _Optional[int] = ..., table_name: _Optional[bytes] = ..., tablet_id: _Optional[int] = ..., target_tablet_id: _Optional[int] = ..., custom_hashing_scheme: _Optional[_Union[TableMetadataProto.Table.HashingScheme, str]] = ..., history_table: bool = ..., block_reason: _Optional[str] = ...) -> None: ...
    class Tablet(_message.Message):
        __slots__ = ("id", "encryption_key", "low_mem_usage_setting", "store_row_history")
        ID_FIELD_NUMBER: _ClassVar[int]
        ENCRYPTION_KEY_FIELD_NUMBER: _ClassVar[int]
        LOW_MEM_USAGE_SETTING_FIELD_NUMBER: _ClassVar[int]
        STORE_ROW_HISTORY_FIELD_NUMBER: _ClassVar[int]
        id: int
        encryption_key: bytes
        low_mem_usage_setting: bool
        store_row_history: bool
        def __init__(self, id: _Optional[int] = ..., encryption_key: _Optional[bytes] = ..., low_mem_usage_setting: bool = ..., store_row_history: bool = ...) -> None: ...
    TABLES_FIELD_NUMBER: _ClassVar[int]
    TABLETS_FIELD_NUMBER: _ClassVar[int]
    NEXT_ID_FIELD_NUMBER: _ClassVar[int]
    MIGRATION_TRIGGER_TABLE_METADATA_VERSION_FIELD_NUMBER: _ClassVar[int]
    SCRIBE_TABLES_TO_BE_CREATED_IN_HIGH_MEM_USAGE_TABLET_FIELD_NUMBER: _ClassVar[int]
    SCRIBE_LOW_MEM_USAGE_TABLET_READY_FIELD_NUMBER: _ClassVar[int]
    LAST_TABLE_MIGRATION_COMPLETION_TS_FIELD_NUMBER: _ClassVar[int]
    SCRIBE_HISTORY_TABLET_READY_FIELD_NUMBER: _ClassVar[int]
    tables: _containers.RepeatedCompositeFieldContainer[TableMetadataProto.Table]
    tablets: _containers.RepeatedCompositeFieldContainer[TableMetadataProto.Tablet]
    next_id: int
    migration_trigger_table_metadata_version: int
    scribe_tables_to_be_created_in_high_mem_usage_tablet: str
    scribe_low_mem_usage_tablet_ready: bool
    last_table_migration_completion_ts: int
    scribe_history_tablet_ready: bool
    def __init__(self, tables: _Optional[_Iterable[_Union[TableMetadataProto.Table, _Mapping]]] = ..., tablets: _Optional[_Iterable[_Union[TableMetadataProto.Tablet, _Mapping]]] = ..., next_id: _Optional[int] = ..., migration_trigger_table_metadata_version: _Optional[int] = ..., scribe_tables_to_be_created_in_high_mem_usage_tablet: _Optional[str] = ..., scribe_low_mem_usage_tablet_ready: bool = ..., last_table_migration_completion_ts: _Optional[int] = ..., scribe_history_tablet_ready: bool = ...) -> None: ...
