from util.base import op_clock_pb2 as _op_clock_pb2
from open_util.net import protorpc_pb2 as _protorpc_pb2
from scribe.base import scribe_pb2 as _scribe_pb2
from scribe.newscribe.server import data_format_pb2 as _data_format_pb2
from scribe.newscribe.stub import server_error_pb2 as _server_error_pb2
from configs import cluster_config_pb2 as _cluster_config_pb2
from scribe.newscribe.base import liveness_pb2 as _liveness_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RpcContext(_message.Message):
    __slots__ = ("bucket", "table", "sender_timestamp_usecs")
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    TABLE_FIELD_NUMBER: _ClassVar[int]
    SENDER_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
    bucket: int
    table: int
    sender_timestamp_usecs: int
    def __init__(self, bucket: _Optional[int] = ..., table: _Optional[int] = ..., sender_timestamp_usecs: _Optional[int] = ...) -> None: ...

class VersionContext(_message.Message):
    __slots__ = ("view_version", "table_md_version", "leader_lock_sequencer")
    VIEW_VERSION_FIELD_NUMBER: _ClassVar[int]
    TABLE_MD_VERSION_FIELD_NUMBER: _ClassVar[int]
    LEADER_LOCK_SEQUENCER_FIELD_NUMBER: _ClassVar[int]
    view_version: int
    table_md_version: int
    leader_lock_sequencer: int
    def __init__(self, view_version: _Optional[int] = ..., table_md_version: _Optional[int] = ..., leader_lock_sequencer: _Optional[int] = ...) -> None: ...

class WriteArg(_message.Message):
    __slots__ = ("rpc_context", "version_context", "params", "arg_creation_timestamp_msecs", "maybe_dump_mem_traces", "history_write")
    class Params(_message.Message):
        __slots__ = ("update", "version", "sequencer", "op_clock_vec", "scribe_qos_params", "writer_writes_unique_data", "expected_opclock_vec", "existing_column_vec", "payload_size", "payload_offset", "clear_existing_sequencer", "reason")
        UPDATE_FIELD_NUMBER: _ClassVar[int]
        VERSION_FIELD_NUMBER: _ClassVar[int]
        SEQUENCER_FIELD_NUMBER: _ClassVar[int]
        OP_CLOCK_VEC_FIELD_NUMBER: _ClassVar[int]
        SCRIBE_QOS_PARAMS_FIELD_NUMBER: _ClassVar[int]
        WRITER_WRITES_UNIQUE_DATA_FIELD_NUMBER: _ClassVar[int]
        EXPECTED_OPCLOCK_VEC_FIELD_NUMBER: _ClassVar[int]
        EXISTING_COLUMN_VEC_FIELD_NUMBER: _ClassVar[int]
        PAYLOAD_SIZE_FIELD_NUMBER: _ClassVar[int]
        PAYLOAD_OFFSET_FIELD_NUMBER: _ClassVar[int]
        CLEAR_EXISTING_SEQUENCER_FIELD_NUMBER: _ClassVar[int]
        REASON_FIELD_NUMBER: _ClassVar[int]
        update: _scribe_pb2.RowData
        version: int
        sequencer: _scribe_pb2.SequencerProto
        op_clock_vec: _containers.RepeatedCompositeFieldContainer[_op_clock_pb2.OpClock]
        scribe_qos_params: _scribe_pb2.ScribeQoSParams
        writer_writes_unique_data: bool
        expected_opclock_vec: _containers.RepeatedCompositeFieldContainer[_op_clock_pb2.OpClock]
        existing_column_vec: _containers.RepeatedCompositeFieldContainer[_scribe_pb2.RowColumnKey]
        payload_size: int
        payload_offset: int
        clear_existing_sequencer: bool
        reason: bytes
        def __init__(self, update: _Optional[_Union[_scribe_pb2.RowData, _Mapping]] = ..., version: _Optional[int] = ..., sequencer: _Optional[_Union[_scribe_pb2.SequencerProto, _Mapping]] = ..., op_clock_vec: _Optional[_Iterable[_Union[_op_clock_pb2.OpClock, _Mapping]]] = ..., scribe_qos_params: _Optional[_Union[_scribe_pb2.ScribeQoSParams, _Mapping]] = ..., writer_writes_unique_data: bool = ..., expected_opclock_vec: _Optional[_Iterable[_Union[_op_clock_pb2.OpClock, _Mapping]]] = ..., existing_column_vec: _Optional[_Iterable[_Union[_scribe_pb2.RowColumnKey, _Mapping]]] = ..., payload_size: _Optional[int] = ..., payload_offset: _Optional[int] = ..., clear_existing_sequencer: bool = ..., reason: _Optional[bytes] = ...) -> None: ...
    RPC_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    VERSION_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    ARG_CREATION_TIMESTAMP_MSECS_FIELD_NUMBER: _ClassVar[int]
    MAYBE_DUMP_MEM_TRACES_FIELD_NUMBER: _ClassVar[int]
    HISTORY_WRITE_FIELD_NUMBER: _ClassVar[int]
    rpc_context: RpcContext
    version_context: VersionContext
    params: WriteArg.Params
    arg_creation_timestamp_msecs: int
    maybe_dump_mem_traces: bool
    history_write: bool
    def __init__(self, rpc_context: _Optional[_Union[RpcContext, _Mapping]] = ..., version_context: _Optional[_Union[VersionContext, _Mapping]] = ..., params: _Optional[_Union[WriteArg.Params, _Mapping]] = ..., arg_creation_timestamp_msecs: _Optional[int] = ..., maybe_dump_mem_traces: bool = ..., history_write: bool = ...) -> None: ...

class WriteResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class BulkWriteArg(_message.Message):
    __slots__ = ("rpc_context", "version_context", "write_params_vec", "arg_creation_timestamp_msecs")
    RPC_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    VERSION_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    WRITE_PARAMS_VEC_FIELD_NUMBER: _ClassVar[int]
    ARG_CREATION_TIMESTAMP_MSECS_FIELD_NUMBER: _ClassVar[int]
    rpc_context: RpcContext
    version_context: VersionContext
    write_params_vec: _containers.RepeatedCompositeFieldContainer[WriteArg.Params]
    arg_creation_timestamp_msecs: int
    def __init__(self, rpc_context: _Optional[_Union[RpcContext, _Mapping]] = ..., version_context: _Optional[_Union[VersionContext, _Mapping]] = ..., write_params_vec: _Optional[_Iterable[_Union[WriteArg.Params, _Mapping]]] = ..., arg_creation_timestamp_msecs: _Optional[int] = ...) -> None: ...

class KeyServerErrorPair(_message.Message):
    __slots__ = ("key", "error")
    KEY_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    key: _scribe_pb2.RowColumnKey
    error: _server_error_pb2.ServerErrorProto.Type
    def __init__(self, key: _Optional[_Union[_scribe_pb2.RowColumnKey, _Mapping]] = ..., error: _Optional[_Union[_server_error_pb2.ServerErrorProto.Type, str]] = ...) -> None: ...

class BulkWriteResult(_message.Message):
    __slots__ = ("key_error_vec",)
    KEY_ERROR_VEC_FIELD_NUMBER: _ClassVar[int]
    key_error_vec: _containers.RepeatedCompositeFieldContainer[KeyServerErrorPair]
    def __init__(self, key_error_vec: _Optional[_Iterable[_Union[KeyServerErrorPair, _Mapping]]] = ...) -> None: ...

class BulkWriteTransactionArg(_message.Message):
    __slots__ = ("bucket_arg_vec", "bulk_rpc_context")
    class BucketArg(_message.Message):
        __slots__ = ("bucket_id", "version_context", "write_params_vec")
        BUCKET_ID_FIELD_NUMBER: _ClassVar[int]
        VERSION_CONTEXT_FIELD_NUMBER: _ClassVar[int]
        WRITE_PARAMS_VEC_FIELD_NUMBER: _ClassVar[int]
        bucket_id: int
        version_context: VersionContext
        write_params_vec: _containers.RepeatedCompositeFieldContainer[WriteArg.Params]
        def __init__(self, bucket_id: _Optional[int] = ..., version_context: _Optional[_Union[VersionContext, _Mapping]] = ..., write_params_vec: _Optional[_Iterable[_Union[WriteArg.Params, _Mapping]]] = ...) -> None: ...
    class BulkRpcContext(_message.Message):
        __slots__ = ("table_id", "sender_timestamp_usecs")
        TABLE_ID_FIELD_NUMBER: _ClassVar[int]
        SENDER_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
        table_id: int
        sender_timestamp_usecs: int
        def __init__(self, table_id: _Optional[int] = ..., sender_timestamp_usecs: _Optional[int] = ...) -> None: ...
    BUCKET_ARG_VEC_FIELD_NUMBER: _ClassVar[int]
    BULK_RPC_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    bucket_arg_vec: _containers.RepeatedCompositeFieldContainer[BulkWriteTransactionArg.BucketArg]
    bulk_rpc_context: BulkWriteTransactionArg.BulkRpcContext
    def __init__(self, bucket_arg_vec: _Optional[_Iterable[_Union[BulkWriteTransactionArg.BucketArg, _Mapping]]] = ..., bulk_rpc_context: _Optional[_Union[BulkWriteTransactionArg.BulkRpcContext, _Mapping]] = ...) -> None: ...

class BulkWriteForMigrationArg(_message.Message):
    __slots__ = ("rpc_context", "version_context", "records", "arg_creation_timestamp_msecs")
    RPC_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    VERSION_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    RECORDS_FIELD_NUMBER: _ClassVar[int]
    ARG_CREATION_TIMESTAMP_MSECS_FIELD_NUMBER: _ClassVar[int]
    rpc_context: RpcContext
    version_context: VersionContext
    records: _containers.RepeatedCompositeFieldContainer[WriteArg.Params]
    arg_creation_timestamp_msecs: int
    def __init__(self, rpc_context: _Optional[_Union[RpcContext, _Mapping]] = ..., version_context: _Optional[_Union[VersionContext, _Mapping]] = ..., records: _Optional[_Iterable[_Union[WriteArg.Params, _Mapping]]] = ..., arg_creation_timestamp_msecs: _Optional[int] = ...) -> None: ...

class BulkWriteForMigrationResult(_message.Message):
    __slots__ = ("num_records_persisted", "num_rocksdb_rows_persisted")
    NUM_RECORDS_PERSISTED_FIELD_NUMBER: _ClassVar[int]
    NUM_ROCKSDB_ROWS_PERSISTED_FIELD_NUMBER: _ClassVar[int]
    num_records_persisted: int
    num_rocksdb_rows_persisted: int
    def __init__(self, num_records_persisted: _Optional[int] = ..., num_rocksdb_rows_persisted: _Optional[int] = ...) -> None: ...

class ReadArg(_message.Message):
    __slots__ = ("rpc_context", "version_context", "key", "params", "arg_creation_timestamp_msecs", "maybe_dump_mem_traces")
    class Params(_message.Message):
        __slots__ = ("columns", "sequencer", "op_clock_to_add", "create_tombstone", "scribe_qos_params", "list_only", "clear_existing_sequencer")
        COLUMNS_FIELD_NUMBER: _ClassVar[int]
        SEQUENCER_FIELD_NUMBER: _ClassVar[int]
        OP_CLOCK_TO_ADD_FIELD_NUMBER: _ClassVar[int]
        CREATE_TOMBSTONE_FIELD_NUMBER: _ClassVar[int]
        SCRIBE_QOS_PARAMS_FIELD_NUMBER: _ClassVar[int]
        LIST_ONLY_FIELD_NUMBER: _ClassVar[int]
        CLEAR_EXISTING_SEQUENCER_FIELD_NUMBER: _ClassVar[int]
        columns: _containers.RepeatedCompositeFieldContainer[_scribe_pb2.RowColumnKey]
        sequencer: _scribe_pb2.SequencerProto
        op_clock_to_add: _op_clock_pb2.OpClock
        create_tombstone: bool
        scribe_qos_params: _scribe_pb2.ScribeQoSParams
        list_only: bool
        clear_existing_sequencer: bool
        def __init__(self, columns: _Optional[_Iterable[_Union[_scribe_pb2.RowColumnKey, _Mapping]]] = ..., sequencer: _Optional[_Union[_scribe_pb2.SequencerProto, _Mapping]] = ..., op_clock_to_add: _Optional[_Union[_op_clock_pb2.OpClock, _Mapping]] = ..., create_tombstone: bool = ..., scribe_qos_params: _Optional[_Union[_scribe_pb2.ScribeQoSParams, _Mapping]] = ..., list_only: bool = ..., clear_existing_sequencer: bool = ...) -> None: ...
    RPC_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    VERSION_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    ARG_CREATION_TIMESTAMP_MSECS_FIELD_NUMBER: _ClassVar[int]
    MAYBE_DUMP_MEM_TRACES_FIELD_NUMBER: _ClassVar[int]
    rpc_context: RpcContext
    version_context: VersionContext
    key: _scribe_pb2.RowColumnKey
    params: ReadArg.Params
    arg_creation_timestamp_msecs: int
    maybe_dump_mem_traces: bool
    def __init__(self, rpc_context: _Optional[_Union[RpcContext, _Mapping]] = ..., version_context: _Optional[_Union[VersionContext, _Mapping]] = ..., key: _Optional[_Union[_scribe_pb2.RowColumnKey, _Mapping]] = ..., params: _Optional[_Union[ReadArg.Params, _Mapping]] = ..., arg_creation_timestamp_msecs: _Optional[int] = ..., maybe_dump_mem_traces: bool = ...) -> None: ...

class ReadResult(_message.Message):
    __slots__ = ("row",)
    ROW_FIELD_NUMBER: _ClassVar[int]
    row: _scribe_pb2.ReadRowResult
    def __init__(self, row: _Optional[_Union[_scribe_pb2.ReadRowResult, _Mapping]] = ...) -> None: ...

class RangeScanArg(_message.Message):
    __slots__ = ("row_range", "rpc_context", "version_context", "params", "cookie", "sender_constituent_id", "response_size_limit_hint_bytes", "maybe_dump_mem_traces", "response_num_rows_limit", "is_throttled_range_scan", "bucket_incarnation")
    class Params(_message.Message):
        __slots__ = ("columns", "range_scan_consistency", "range_scan_row_payload_size_threshold_bytes", "is_sorted", "capacity_per_column_per_batch", "client_name")
        COLUMNS_FIELD_NUMBER: _ClassVar[int]
        RANGE_SCAN_CONSISTENCY_FIELD_NUMBER: _ClassVar[int]
        RANGE_SCAN_ROW_PAYLOAD_SIZE_THRESHOLD_BYTES_FIELD_NUMBER: _ClassVar[int]
        IS_SORTED_FIELD_NUMBER: _ClassVar[int]
        CAPACITY_PER_COLUMN_PER_BATCH_FIELD_NUMBER: _ClassVar[int]
        CLIENT_NAME_FIELD_NUMBER: _ClassVar[int]
        columns: _containers.RepeatedCompositeFieldContainer[_scribe_pb2.RowColumnKey]
        range_scan_consistency: _scribe_pb2.RangeScanConsistency
        range_scan_row_payload_size_threshold_bytes: int
        is_sorted: bool
        capacity_per_column_per_batch: int
        client_name: str
        def __init__(self, columns: _Optional[_Iterable[_Union[_scribe_pb2.RowColumnKey, _Mapping]]] = ..., range_scan_consistency: _Optional[_Union[_scribe_pb2.RangeScanConsistency, str]] = ..., range_scan_row_payload_size_threshold_bytes: _Optional[int] = ..., is_sorted: bool = ..., capacity_per_column_per_batch: _Optional[int] = ..., client_name: _Optional[str] = ...) -> None: ...
    ROW_RANGE_FIELD_NUMBER: _ClassVar[int]
    RPC_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    VERSION_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    COOKIE_FIELD_NUMBER: _ClassVar[int]
    SENDER_CONSTITUENT_ID_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_SIZE_LIMIT_HINT_BYTES_FIELD_NUMBER: _ClassVar[int]
    MAYBE_DUMP_MEM_TRACES_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_NUM_ROWS_LIMIT_FIELD_NUMBER: _ClassVar[int]
    IS_THROTTLED_RANGE_SCAN_FIELD_NUMBER: _ClassVar[int]
    BUCKET_INCARNATION_FIELD_NUMBER: _ClassVar[int]
    row_range: _scribe_pb2.RowRange
    rpc_context: RpcContext
    version_context: VersionContext
    params: RangeScanArg.Params
    cookie: _scribe_pb2.RowColumnKey
    sender_constituent_id: int
    response_size_limit_hint_bytes: int
    maybe_dump_mem_traces: bool
    response_num_rows_limit: int
    is_throttled_range_scan: bool
    bucket_incarnation: int
    def __init__(self, row_range: _Optional[_Union[_scribe_pb2.RowRange, _Mapping]] = ..., rpc_context: _Optional[_Union[RpcContext, _Mapping]] = ..., version_context: _Optional[_Union[VersionContext, _Mapping]] = ..., params: _Optional[_Union[RangeScanArg.Params, _Mapping]] = ..., cookie: _Optional[_Union[_scribe_pb2.RowColumnKey, _Mapping]] = ..., sender_constituent_id: _Optional[int] = ..., response_size_limit_hint_bytes: _Optional[int] = ..., maybe_dump_mem_traces: bool = ..., response_num_rows_limit: _Optional[int] = ..., is_throttled_range_scan: bool = ..., bucket_incarnation: _Optional[int] = ...) -> None: ...

class RangeScanResult(_message.Message):
    __slots__ = ("rows", "unresolved_rows", "may_have_inconsistent_rows", "range_scan_next_cookie", "bucket_incarnation")
    ROWS_FIELD_NUMBER: _ClassVar[int]
    UNRESOLVED_ROWS_FIELD_NUMBER: _ClassVar[int]
    MAY_HAVE_INCONSISTENT_ROWS_FIELD_NUMBER: _ClassVar[int]
    RANGE_SCAN_NEXT_COOKIE_FIELD_NUMBER: _ClassVar[int]
    BUCKET_INCARNATION_FIELD_NUMBER: _ClassVar[int]
    rows: _containers.RepeatedCompositeFieldContainer[_scribe_pb2.ReadRowResult]
    unresolved_rows: _containers.RepeatedCompositeFieldContainer[_scribe_pb2.RowColumnKey]
    may_have_inconsistent_rows: bool
    range_scan_next_cookie: _scribe_pb2.RowColumnKey
    bucket_incarnation: int
    def __init__(self, rows: _Optional[_Iterable[_Union[_scribe_pb2.ReadRowResult, _Mapping]]] = ..., unresolved_rows: _Optional[_Iterable[_Union[_scribe_pb2.RowColumnKey, _Mapping]]] = ..., may_have_inconsistent_rows: bool = ..., range_scan_next_cookie: _Optional[_Union[_scribe_pb2.RowColumnKey, _Mapping]] = ..., bucket_incarnation: _Optional[int] = ...) -> None: ...

class HistoryReadArg(_message.Message):
    __slots__ = ("row_range", "params", "response_num_rows_limit")
    class Params(_message.Message):
        __slots__ = ("columns",)
        COLUMNS_FIELD_NUMBER: _ClassVar[int]
        columns: _containers.RepeatedCompositeFieldContainer[_scribe_pb2.RowColumnKey]
        def __init__(self, columns: _Optional[_Iterable[_Union[_scribe_pb2.RowColumnKey, _Mapping]]] = ...) -> None: ...
    ROW_RANGE_FIELD_NUMBER: _ClassVar[int]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_NUM_ROWS_LIMIT_FIELD_NUMBER: _ClassVar[int]
    row_range: _scribe_pb2.RowRange
    params: HistoryReadArg.Params
    response_num_rows_limit: int
    def __init__(self, row_range: _Optional[_Union[_scribe_pb2.RowRange, _Mapping]] = ..., params: _Optional[_Union[HistoryReadArg.Params, _Mapping]] = ..., response_num_rows_limit: _Optional[int] = ...) -> None: ...

class GetDebugInfoArg(_message.Message):
    __slots__ = ("rpc_context", "version_context", "key")
    RPC_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    VERSION_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    rpc_context: RpcContext
    version_context: VersionContext
    key: _scribe_pb2.RowColumnKey
    def __init__(self, rpc_context: _Optional[_Union[RpcContext, _Mapping]] = ..., version_context: _Optional[_Union[VersionContext, _Mapping]] = ..., key: _Optional[_Union[_scribe_pb2.RowColumnKey, _Mapping]] = ...) -> None: ...

class GetDebugInfoResult(_message.Message):
    __slots__ = ("debug_info", "key", "replica_info_vec", "bucket", "table")
    class ReplicaInfo(_message.Message):
        __slots__ = ("constituent_id", "row_md")
        CONSTITUENT_ID_FIELD_NUMBER: _ClassVar[int]
        ROW_MD_FIELD_NUMBER: _ClassVar[int]
        constituent_id: int
        row_md: _data_format_pb2.ScribeRowMD
        def __init__(self, constituent_id: _Optional[int] = ..., row_md: _Optional[_Union[_data_format_pb2.ScribeRowMD, _Mapping]] = ...) -> None: ...
    DEBUG_INFO_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    REPLICA_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    TABLE_FIELD_NUMBER: _ClassVar[int]
    debug_info: bytes
    key: _scribe_pb2.RowColumnKey
    replica_info_vec: _containers.RepeatedCompositeFieldContainer[GetDebugInfoResult.ReplicaInfo]
    bucket: int
    table: int
    def __init__(self, debug_info: _Optional[bytes] = ..., key: _Optional[_Union[_scribe_pb2.RowColumnKey, _Mapping]] = ..., replica_info_vec: _Optional[_Iterable[_Union[GetDebugInfoResult.ReplicaInfo, _Mapping]]] = ..., bucket: _Optional[int] = ..., table: _Optional[int] = ...) -> None: ...

class GetConstituentForKeysArg(_message.Message):
    __slots__ = ("keys",)
    KEYS_FIELD_NUMBER: _ClassVar[int]
    keys: _containers.RepeatedCompositeFieldContainer[_scribe_pb2.RowColumnKey]
    def __init__(self, keys: _Optional[_Iterable[_Union[_scribe_pb2.RowColumnKey, _Mapping]]] = ...) -> None: ...

class ConstituentForKey(_message.Message):
    __slots__ = ("key", "constituent_id", "bucket_id")
    KEY_FIELD_NUMBER: _ClassVar[int]
    CONSTITUENT_ID_FIELD_NUMBER: _ClassVar[int]
    BUCKET_ID_FIELD_NUMBER: _ClassVar[int]
    key: _scribe_pb2.RowColumnKey
    constituent_id: int
    bucket_id: int
    def __init__(self, key: _Optional[_Union[_scribe_pb2.RowColumnKey, _Mapping]] = ..., constituent_id: _Optional[int] = ..., bucket_id: _Optional[int] = ...) -> None: ...

class GetConstituentForKeysResult(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: _containers.RepeatedCompositeFieldContainer[ConstituentForKey]
    def __init__(self, result: _Optional[_Iterable[_Union[ConstituentForKey, _Mapping]]] = ...) -> None: ...

class GetTableInfoInBucketArg(_message.Message):
    __slots__ = ("rpc_context", "version_context")
    RPC_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    VERSION_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    rpc_context: RpcContext
    version_context: VersionContext
    def __init__(self, rpc_context: _Optional[_Union[RpcContext, _Mapping]] = ..., version_context: _Optional[_Union[VersionContext, _Mapping]] = ...) -> None: ...

class GetTableInfoInBucketResult(_message.Message):
    __slots__ = ("approximate_size_in_bytes",)
    APPROXIMATE_SIZE_IN_BYTES_FIELD_NUMBER: _ClassVar[int]
    approximate_size_in_bytes: int
    def __init__(self, approximate_size_in_bytes: _Optional[int] = ...) -> None: ...

class DeleteTableArg(_message.Message):
    __slots__ = ("table_name",)
    TABLE_NAME_FIELD_NUMBER: _ClassVar[int]
    table_name: bytes
    def __init__(self, table_name: _Optional[bytes] = ...) -> None: ...

class DeleteTableResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ShuffleBucketsForTestArg(_message.Message):
    __slots__ = ("shuffle_type",)
    class ShuffleType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kFakeGracefulRemoval: _ClassVar[ShuffleBucketsForTestArg.ShuffleType]
        kFakeForceRemoval: _ClassVar[ShuffleBucketsForTestArg.ShuffleType]
        kReshuffleBuckets: _ClassVar[ShuffleBucketsForTestArg.ShuffleType]
        kFakeRFSwitch: _ClassVar[ShuffleBucketsForTestArg.ShuffleType]
        kFakePlacementModeSwitch: _ClassVar[ShuffleBucketsForTestArg.ShuffleType]
    kFakeGracefulRemoval: ShuffleBucketsForTestArg.ShuffleType
    kFakeForceRemoval: ShuffleBucketsForTestArg.ShuffleType
    kReshuffleBuckets: ShuffleBucketsForTestArg.ShuffleType
    kFakeRFSwitch: ShuffleBucketsForTestArg.ShuffleType
    kFakePlacementModeSwitch: ShuffleBucketsForTestArg.ShuffleType
    SHUFFLE_TYPE_FIELD_NUMBER: _ClassVar[int]
    shuffle_type: ShuffleBucketsForTestArg.ShuffleType
    def __init__(self, shuffle_type: _Optional[_Union[ShuffleBucketsForTestArg.ShuffleType, str]] = ...) -> None: ...

class ShuffleBucketsForTestResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetClusterCapacityArg(_message.Message):
    __slots__ = ("force_homogenous_mode", "removed_node_id", "removed_disk_id", "metadata_fault_tolerance", "metadata_fault_tolerance_factor")
    FORCE_HOMOGENOUS_MODE_FIELD_NUMBER: _ClassVar[int]
    REMOVED_NODE_ID_FIELD_NUMBER: _ClassVar[int]
    REMOVED_DISK_ID_FIELD_NUMBER: _ClassVar[int]
    METADATA_FAULT_TOLERANCE_FIELD_NUMBER: _ClassVar[int]
    METADATA_FAULT_TOLERANCE_FACTOR_FIELD_NUMBER: _ClassVar[int]
    force_homogenous_mode: bool
    removed_node_id: int
    removed_disk_id: int
    metadata_fault_tolerance: _cluster_config_pb2.ClusterConfigProto.FaultToleranceStrictness
    metadata_fault_tolerance_factor: int
    def __init__(self, force_homogenous_mode: bool = ..., removed_node_id: _Optional[int] = ..., removed_disk_id: _Optional[int] = ..., metadata_fault_tolerance: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.FaultToleranceStrictness, _Mapping]] = ..., metadata_fault_tolerance_factor: _Optional[int] = ...) -> None: ...

class GetClusterCapacityResult(_message.Message):
    __slots__ = ("cluster_capacity_bytes",)
    CLUSTER_CAPACITY_BYTES_FIELD_NUMBER: _ClassVar[int]
    cluster_capacity_bytes: int
    def __init__(self, cluster_capacity_bytes: _Optional[int] = ...) -> None: ...

class GetBucketLeaderArg(_message.Message):
    __slots__ = ("bucket",)
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    bucket: int
    def __init__(self, bucket: _Optional[int] = ...) -> None: ...

class GetBucketLeaderResult(_message.Message):
    __slots__ = ("constituent_id", "lock_sequencer", "ip_address", "port", "network_interface_vec")
    CONSTITUENT_ID_FIELD_NUMBER: _ClassVar[int]
    LOCK_SEQUENCER_FIELD_NUMBER: _ClassVar[int]
    IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    NETWORK_INTERFACE_VEC_FIELD_NUMBER: _ClassVar[int]
    constituent_id: int
    lock_sequencer: int
    ip_address: str
    port: int
    network_interface_vec: _containers.RepeatedCompositeFieldContainer[_liveness_pb2.LivenessProto.NetworkInterface]
    def __init__(self, constituent_id: _Optional[int] = ..., lock_sequencer: _Optional[int] = ..., ip_address: _Optional[str] = ..., port: _Optional[int] = ..., network_interface_vec: _Optional[_Iterable[_Union[_liveness_pb2.LivenessProto.NetworkInterface, _Mapping]]] = ...) -> None: ...

class GetShuffleProgressArg(_message.Message):
    __slots__ = ("disk_id_vec", "node_id_vec")
    DISK_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    NODE_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    disk_id_vec: _containers.RepeatedScalarFieldContainer[int]
    node_id_vec: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, disk_id_vec: _Optional[_Iterable[int]] = ..., node_id_vec: _Optional[_Iterable[int]] = ...) -> None: ...

class GetShuffleProgressResult(_message.Message):
    __slots__ = ("disk_shuffle_stat_vec", "is_shuffling", "shuffle_start_time_usecs")
    class DiskShuffleStat(_message.Message):
        __slots__ = ("disk_id", "constituent_id", "node_id", "num_buckets_at_shuffle_start", "num_buckets_hosted_now", "error")
        class Error(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kNoError: _ClassVar[GetShuffleProgressResult.DiskShuffleStat.Error]
            kNotFound: _ClassVar[GetShuffleProgressResult.DiskShuffleStat.Error]
        kNoError: GetShuffleProgressResult.DiskShuffleStat.Error
        kNotFound: GetShuffleProgressResult.DiskShuffleStat.Error
        DISK_ID_FIELD_NUMBER: _ClassVar[int]
        CONSTITUENT_ID_FIELD_NUMBER: _ClassVar[int]
        NODE_ID_FIELD_NUMBER: _ClassVar[int]
        NUM_BUCKETS_AT_SHUFFLE_START_FIELD_NUMBER: _ClassVar[int]
        NUM_BUCKETS_HOSTED_NOW_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        disk_id: int
        constituent_id: int
        node_id: int
        num_buckets_at_shuffle_start: int
        num_buckets_hosted_now: int
        error: GetShuffleProgressResult.DiskShuffleStat.Error
        def __init__(self, disk_id: _Optional[int] = ..., constituent_id: _Optional[int] = ..., node_id: _Optional[int] = ..., num_buckets_at_shuffle_start: _Optional[int] = ..., num_buckets_hosted_now: _Optional[int] = ..., error: _Optional[_Union[GetShuffleProgressResult.DiskShuffleStat.Error, str]] = ...) -> None: ...
    DISK_SHUFFLE_STAT_VEC_FIELD_NUMBER: _ClassVar[int]
    IS_SHUFFLING_FIELD_NUMBER: _ClassVar[int]
    SHUFFLE_START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    disk_shuffle_stat_vec: _containers.RepeatedCompositeFieldContainer[GetShuffleProgressResult.DiskShuffleStat]
    is_shuffling: bool
    shuffle_start_time_usecs: int
    def __init__(self, disk_shuffle_stat_vec: _Optional[_Iterable[_Union[GetShuffleProgressResult.DiskShuffleStat, _Mapping]]] = ..., is_shuffling: bool = ..., shuffle_start_time_usecs: _Optional[int] = ...) -> None: ...

class DeleteRangeArg(_message.Message):
    __slots__ = ("row_range", "rpc_context", "version_context", "sender_constituent_id", "maybe_dump_mem_traces", "cookie", "arg_creation_timestamp_msecs", "client_name")
    ROW_RANGE_FIELD_NUMBER: _ClassVar[int]
    RPC_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    VERSION_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    SENDER_CONSTITUENT_ID_FIELD_NUMBER: _ClassVar[int]
    MAYBE_DUMP_MEM_TRACES_FIELD_NUMBER: _ClassVar[int]
    COOKIE_FIELD_NUMBER: _ClassVar[int]
    ARG_CREATION_TIMESTAMP_MSECS_FIELD_NUMBER: _ClassVar[int]
    CLIENT_NAME_FIELD_NUMBER: _ClassVar[int]
    row_range: _scribe_pb2.RowRange
    rpc_context: RpcContext
    version_context: VersionContext
    sender_constituent_id: int
    maybe_dump_mem_traces: bool
    cookie: _scribe_pb2.RowColumnKey
    arg_creation_timestamp_msecs: int
    client_name: str
    def __init__(self, row_range: _Optional[_Union[_scribe_pb2.RowRange, _Mapping]] = ..., rpc_context: _Optional[_Union[RpcContext, _Mapping]] = ..., version_context: _Optional[_Union[VersionContext, _Mapping]] = ..., sender_constituent_id: _Optional[int] = ..., maybe_dump_mem_traces: bool = ..., cookie: _Optional[_Union[_scribe_pb2.RowColumnKey, _Mapping]] = ..., arg_creation_timestamp_msecs: _Optional[int] = ..., client_name: _Optional[str] = ...) -> None: ...

class DeleteRangeResult(_message.Message):
    __slots__ = ("range_scan_next_cookie",)
    RANGE_SCAN_NEXT_COOKIE_FIELD_NUMBER: _ClassVar[int]
    range_scan_next_cookie: _scribe_pb2.RowColumnKey
    def __init__(self, range_scan_next_cookie: _Optional[_Union[_scribe_pb2.RowColumnKey, _Mapping]] = ...) -> None: ...
