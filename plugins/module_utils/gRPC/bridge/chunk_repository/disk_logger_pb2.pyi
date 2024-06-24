from bridge.chunk_repository.stub import rpc_service_pb2 as _rpc_service_pb2
from bridge.stats import disk_usage_stats_pb2 as _disk_usage_stats_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DiskLoggerRecordProto(_message.Message):
    __slots__ = ("chunk_file_change_vec", "disk_usage_stats_diff", "disk_usage_computation", "background_scrubber_next_cookie", "clear_corruption_bits_info", "dump_inconsistent_chunks_info")
    class UpdateIntent(_message.Message):
        __slots__ = ("intent_id", "chunk_change_vec", "chunkgroup_change_vec")
        INTENT_ID_FIELD_NUMBER: _ClassVar[int]
        CHUNK_CHANGE_VEC_FIELD_NUMBER: _ClassVar[int]
        CHUNKGROUP_CHANGE_VEC_FIELD_NUMBER: _ClassVar[int]
        intent_id: int
        chunk_change_vec: _containers.RepeatedCompositeFieldContainer[_rpc_service_pb2.ChunkChange]
        chunkgroup_change_vec: _containers.RepeatedCompositeFieldContainer[_rpc_service_pb2.ChunkgroupChange]
        def __init__(self, intent_id: _Optional[int] = ..., chunk_change_vec: _Optional[_Iterable[_Union[_rpc_service_pb2.ChunkChange, _Mapping]]] = ..., chunkgroup_change_vec: _Optional[_Iterable[_Union[_rpc_service_pb2.ChunkgroupChange, _Mapping]]] = ...) -> None: ...
    class ChunkFileChange(_message.Message):
        __slots__ = ("chunk_file_id", "version", "update_intent", "finalized_intent_id", "aborted_intent_id", "synced_version", "delete_chunk_file", "is_corrupt", "highest_intent_id_detected", "used_chunk_file_bytes", "max_chunk_file_bytes", "next_available_chunkgroup_id", "override_max_chunk_file_bytes", "version_monotonic", "chunk_file_deletor", "corruption_reason", "stripe_column", "physical_version", "last_read_access_time_secs", "last_write_access_time_secs", "chunk_stripe_type", "max_pin_secs_hint", "view_box_id", "corruption_error_info")
        class ChunkStripeType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kUnknown: _ClassVar[DiskLoggerRecordProto.ChunkFileChange.ChunkStripeType]
            kDataStripe: _ClassVar[DiskLoggerRecordProto.ChunkFileChange.ChunkStripeType]
            kCodedStripe: _ClassVar[DiskLoggerRecordProto.ChunkFileChange.ChunkStripeType]
            kNumStripeTypes: _ClassVar[DiskLoggerRecordProto.ChunkFileChange.ChunkStripeType]
        kUnknown: DiskLoggerRecordProto.ChunkFileChange.ChunkStripeType
        kDataStripe: DiskLoggerRecordProto.ChunkFileChange.ChunkStripeType
        kCodedStripe: DiskLoggerRecordProto.ChunkFileChange.ChunkStripeType
        kNumStripeTypes: DiskLoggerRecordProto.ChunkFileChange.ChunkStripeType
        class CorruptionErrorInfo(_message.Message):
            __slots__ = ("reason", "time_stamp_usecs")
            class Reason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                kNoError: _ClassVar[DiskLoggerRecordProto.ChunkFileChange.CorruptionErrorInfo.Reason]
                kUnknown: _ClassVar[DiskLoggerRecordProto.ChunkFileChange.CorruptionErrorInfo.Reason]
                kStripeColumnMismatch: _ClassVar[DiskLoggerRecordProto.ChunkFileChange.CorruptionErrorInfo.Reason]
                kChunkFileTypeMismatch: _ClassVar[DiskLoggerRecordProto.ChunkFileChange.CorruptionErrorInfo.Reason]
                kReadFailed: _ClassVar[DiskLoggerRecordProto.ChunkFileChange.CorruptionErrorInfo.Reason]
                kChecksumMismatch: _ClassVar[DiskLoggerRecordProto.ChunkFileChange.CorruptionErrorInfo.Reason]
                kUndecryptable: _ClassVar[DiskLoggerRecordProto.ChunkFileChange.CorruptionErrorInfo.Reason]
                kDecryptionSizeMismatch: _ClassVar[DiskLoggerRecordProto.ChunkFileChange.CorruptionErrorInfo.Reason]
                kCantAbort: _ClassVar[DiskLoggerRecordProto.ChunkFileChange.CorruptionErrorInfo.Reason]
                kIntendedChangesFetchFailed: _ClassVar[DiskLoggerRecordProto.ChunkFileChange.CorruptionErrorInfo.Reason]
                kWriteFailed: _ClassVar[DiskLoggerRecordProto.ChunkFileChange.CorruptionErrorInfo.Reason]
                kErrorInjection: _ClassVar[DiskLoggerRecordProto.ChunkFileChange.CorruptionErrorInfo.Reason]
            kNoError: DiskLoggerRecordProto.ChunkFileChange.CorruptionErrorInfo.Reason
            kUnknown: DiskLoggerRecordProto.ChunkFileChange.CorruptionErrorInfo.Reason
            kStripeColumnMismatch: DiskLoggerRecordProto.ChunkFileChange.CorruptionErrorInfo.Reason
            kChunkFileTypeMismatch: DiskLoggerRecordProto.ChunkFileChange.CorruptionErrorInfo.Reason
            kReadFailed: DiskLoggerRecordProto.ChunkFileChange.CorruptionErrorInfo.Reason
            kChecksumMismatch: DiskLoggerRecordProto.ChunkFileChange.CorruptionErrorInfo.Reason
            kUndecryptable: DiskLoggerRecordProto.ChunkFileChange.CorruptionErrorInfo.Reason
            kDecryptionSizeMismatch: DiskLoggerRecordProto.ChunkFileChange.CorruptionErrorInfo.Reason
            kCantAbort: DiskLoggerRecordProto.ChunkFileChange.CorruptionErrorInfo.Reason
            kIntendedChangesFetchFailed: DiskLoggerRecordProto.ChunkFileChange.CorruptionErrorInfo.Reason
            kWriteFailed: DiskLoggerRecordProto.ChunkFileChange.CorruptionErrorInfo.Reason
            kErrorInjection: DiskLoggerRecordProto.ChunkFileChange.CorruptionErrorInfo.Reason
            REASON_FIELD_NUMBER: _ClassVar[int]
            TIME_STAMP_USECS_FIELD_NUMBER: _ClassVar[int]
            reason: DiskLoggerRecordProto.ChunkFileChange.CorruptionErrorInfo.Reason
            time_stamp_usecs: int
            def __init__(self, reason: _Optional[_Union[DiskLoggerRecordProto.ChunkFileChange.CorruptionErrorInfo.Reason, str]] = ..., time_stamp_usecs: _Optional[int] = ...) -> None: ...
        CHUNK_FILE_ID_FIELD_NUMBER: _ClassVar[int]
        VERSION_FIELD_NUMBER: _ClassVar[int]
        UPDATE_INTENT_FIELD_NUMBER: _ClassVar[int]
        FINALIZED_INTENT_ID_FIELD_NUMBER: _ClassVar[int]
        ABORTED_INTENT_ID_FIELD_NUMBER: _ClassVar[int]
        SYNCED_VERSION_FIELD_NUMBER: _ClassVar[int]
        DELETE_CHUNK_FILE_FIELD_NUMBER: _ClassVar[int]
        IS_CORRUPT_FIELD_NUMBER: _ClassVar[int]
        HIGHEST_INTENT_ID_DETECTED_FIELD_NUMBER: _ClassVar[int]
        USED_CHUNK_FILE_BYTES_FIELD_NUMBER: _ClassVar[int]
        MAX_CHUNK_FILE_BYTES_FIELD_NUMBER: _ClassVar[int]
        NEXT_AVAILABLE_CHUNKGROUP_ID_FIELD_NUMBER: _ClassVar[int]
        OVERRIDE_MAX_CHUNK_FILE_BYTES_FIELD_NUMBER: _ClassVar[int]
        VERSION_MONOTONIC_FIELD_NUMBER: _ClassVar[int]
        CHUNK_FILE_DELETOR_FIELD_NUMBER: _ClassVar[int]
        CORRUPTION_REASON_FIELD_NUMBER: _ClassVar[int]
        STRIPE_COLUMN_FIELD_NUMBER: _ClassVar[int]
        PHYSICAL_VERSION_FIELD_NUMBER: _ClassVar[int]
        LAST_READ_ACCESS_TIME_SECS_FIELD_NUMBER: _ClassVar[int]
        LAST_WRITE_ACCESS_TIME_SECS_FIELD_NUMBER: _ClassVar[int]
        CHUNK_STRIPE_TYPE_FIELD_NUMBER: _ClassVar[int]
        MAX_PIN_SECS_HINT_FIELD_NUMBER: _ClassVar[int]
        VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
        CORRUPTION_ERROR_INFO_FIELD_NUMBER: _ClassVar[int]
        chunk_file_id: int
        version: int
        update_intent: DiskLoggerRecordProto.UpdateIntent
        finalized_intent_id: int
        aborted_intent_id: int
        synced_version: int
        delete_chunk_file: bool
        is_corrupt: bool
        highest_intent_id_detected: int
        used_chunk_file_bytes: int
        max_chunk_file_bytes: int
        next_available_chunkgroup_id: int
        override_max_chunk_file_bytes: bool
        version_monotonic: bool
        chunk_file_deletor: str
        corruption_reason: str
        stripe_column: int
        physical_version: int
        last_read_access_time_secs: int
        last_write_access_time_secs: int
        chunk_stripe_type: DiskLoggerRecordProto.ChunkFileChange.ChunkStripeType
        max_pin_secs_hint: int
        view_box_id: int
        corruption_error_info: DiskLoggerRecordProto.ChunkFileChange.CorruptionErrorInfo
        def __init__(self, chunk_file_id: _Optional[int] = ..., version: _Optional[int] = ..., update_intent: _Optional[_Union[DiskLoggerRecordProto.UpdateIntent, _Mapping]] = ..., finalized_intent_id: _Optional[int] = ..., aborted_intent_id: _Optional[int] = ..., synced_version: _Optional[int] = ..., delete_chunk_file: bool = ..., is_corrupt: bool = ..., highest_intent_id_detected: _Optional[int] = ..., used_chunk_file_bytes: _Optional[int] = ..., max_chunk_file_bytes: _Optional[int] = ..., next_available_chunkgroup_id: _Optional[int] = ..., override_max_chunk_file_bytes: bool = ..., version_monotonic: bool = ..., chunk_file_deletor: _Optional[str] = ..., corruption_reason: _Optional[str] = ..., stripe_column: _Optional[int] = ..., physical_version: _Optional[int] = ..., last_read_access_time_secs: _Optional[int] = ..., last_write_access_time_secs: _Optional[int] = ..., chunk_stripe_type: _Optional[_Union[DiskLoggerRecordProto.ChunkFileChange.ChunkStripeType, str]] = ..., max_pin_secs_hint: _Optional[int] = ..., view_box_id: _Optional[int] = ..., corruption_error_info: _Optional[_Union[DiskLoggerRecordProto.ChunkFileChange.CorruptionErrorInfo, _Mapping]] = ...) -> None: ...
    class DiskUsageComputation(_message.Message):
        __slots__ = ("usage_stats_diff", "next_shard", "shard_count")
        USAGE_STATS_DIFF_FIELD_NUMBER: _ClassVar[int]
        NEXT_SHARD_FIELD_NUMBER: _ClassVar[int]
        SHARD_COUNT_FIELD_NUMBER: _ClassVar[int]
        usage_stats_diff: _disk_usage_stats_pb2.DiskUsageStatsProto
        next_shard: int
        shard_count: int
        def __init__(self, usage_stats_diff: _Optional[_Union[_disk_usage_stats_pb2.DiskUsageStatsProto, _Mapping]] = ..., next_shard: _Optional[int] = ..., shard_count: _Optional[int] = ...) -> None: ...
    class ClearCorruptionBitsInfo(_message.Message):
        __slots__ = ("next_shard", "shard_count")
        NEXT_SHARD_FIELD_NUMBER: _ClassVar[int]
        SHARD_COUNT_FIELD_NUMBER: _ClassVar[int]
        next_shard: int
        shard_count: int
        def __init__(self, next_shard: _Optional[int] = ..., shard_count: _Optional[int] = ...) -> None: ...
    class DumpInconsistentChunksInfo(_message.Message):
        __slots__ = ("state", "shard_count")
        class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kNotStarted: _ClassVar[DiskLoggerRecordProto.DumpInconsistentChunksInfo.State]
            kRunning: _ClassVar[DiskLoggerRecordProto.DumpInconsistentChunksInfo.State]
            kFinished: _ClassVar[DiskLoggerRecordProto.DumpInconsistentChunksInfo.State]
        kNotStarted: DiskLoggerRecordProto.DumpInconsistentChunksInfo.State
        kRunning: DiskLoggerRecordProto.DumpInconsistentChunksInfo.State
        kFinished: DiskLoggerRecordProto.DumpInconsistentChunksInfo.State
        STATE_FIELD_NUMBER: _ClassVar[int]
        SHARD_COUNT_FIELD_NUMBER: _ClassVar[int]
        state: DiskLoggerRecordProto.DumpInconsistentChunksInfo.State
        shard_count: int
        def __init__(self, state: _Optional[_Union[DiskLoggerRecordProto.DumpInconsistentChunksInfo.State, str]] = ..., shard_count: _Optional[int] = ...) -> None: ...
    CHUNK_FILE_CHANGE_VEC_FIELD_NUMBER: _ClassVar[int]
    DISK_USAGE_STATS_DIFF_FIELD_NUMBER: _ClassVar[int]
    DISK_USAGE_COMPUTATION_FIELD_NUMBER: _ClassVar[int]
    BACKGROUND_SCRUBBER_NEXT_COOKIE_FIELD_NUMBER: _ClassVar[int]
    CLEAR_CORRUPTION_BITS_INFO_FIELD_NUMBER: _ClassVar[int]
    DUMP_INCONSISTENT_CHUNKS_INFO_FIELD_NUMBER: _ClassVar[int]
    chunk_file_change_vec: _containers.RepeatedCompositeFieldContainer[DiskLoggerRecordProto.ChunkFileChange]
    disk_usage_stats_diff: _disk_usage_stats_pb2.DiskUsageStatsProto
    disk_usage_computation: DiskLoggerRecordProto.DiskUsageComputation
    background_scrubber_next_cookie: bytes
    clear_corruption_bits_info: DiskLoggerRecordProto.ClearCorruptionBitsInfo
    dump_inconsistent_chunks_info: DiskLoggerRecordProto.DumpInconsistentChunksInfo
    def __init__(self, chunk_file_change_vec: _Optional[_Iterable[_Union[DiskLoggerRecordProto.ChunkFileChange, _Mapping]]] = ..., disk_usage_stats_diff: _Optional[_Union[_disk_usage_stats_pb2.DiskUsageStatsProto, _Mapping]] = ..., disk_usage_computation: _Optional[_Union[DiskLoggerRecordProto.DiskUsageComputation, _Mapping]] = ..., background_scrubber_next_cookie: _Optional[bytes] = ..., clear_corruption_bits_info: _Optional[_Union[DiskLoggerRecordProto.ClearCorruptionBitsInfo, _Mapping]] = ..., dump_inconsistent_chunks_info: _Optional[_Union[DiskLoggerRecordProto.DumpInconsistentChunksInfo, _Mapping]] = ...) -> None: ...
