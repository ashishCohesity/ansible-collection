from bridge.base import request_context_pb2 as _request_context_pb2
from bridge.blob_store import blob_store_pb2 as _blob_store_pb2
from bridge.stats import disk_usage_stats_pb2 as _disk_usage_stats_pb2
from configs import cluster_config_pb2 as _cluster_config_pb2
from keychain.base import keychain_pb2 as _keychain_pb2
from open_util.base import aes_encryptor_pb2 as _aes_encryptor_pb2
from open_util.net import protorpc_pb2 as _protorpc_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ChunkInfo(_message.Message):
    __slots__ = ("chunk_id", "chunk_column", "replica_version", "chunk_offset", "chunk_data_size")
    CHUNK_ID_FIELD_NUMBER: _ClassVar[int]
    CHUNK_COLUMN_FIELD_NUMBER: _ClassVar[int]
    REPLICA_VERSION_FIELD_NUMBER: _ClassVar[int]
    CHUNK_OFFSET_FIELD_NUMBER: _ClassVar[int]
    CHUNK_DATA_SIZE_FIELD_NUMBER: _ClassVar[int]
    chunk_id: _blob_store_pb2.ChunkIdProto
    chunk_column: _blob_store_pb2.ChunkFileMetadataProto.ChunkColumn
    replica_version: int
    chunk_offset: int
    chunk_data_size: int
    def __init__(self, chunk_id: _Optional[_Union[_blob_store_pb2.ChunkIdProto, _Mapping]] = ..., chunk_column: _Optional[_Union[_blob_store_pb2.ChunkFileMetadataProto.ChunkColumn, _Mapping]] = ..., replica_version: _Optional[int] = ..., chunk_offset: _Optional[int] = ..., chunk_data_size: _Optional[int] = ...) -> None: ...

class ChunkGroupInfo(_message.Message):
    __slots__ = ("chunkgroup_id", "chunkgroup_column", "replica_version")
    CHUNKGROUP_ID_FIELD_NUMBER: _ClassVar[int]
    CHUNKGROUP_COLUMN_FIELD_NUMBER: _ClassVar[int]
    REPLICA_VERSION_FIELD_NUMBER: _ClassVar[int]
    chunkgroup_id: int
    chunkgroup_column: _blob_store_pb2.ChunkFileMetadataProto.ChunkGroupColumn
    replica_version: int
    def __init__(self, chunkgroup_id: _Optional[int] = ..., chunkgroup_column: _Optional[_Union[_blob_store_pb2.ChunkFileMetadataProto.ChunkGroupColumn, _Mapping]] = ..., replica_version: _Optional[int] = ...) -> None: ...

class ChunkChange(_message.Message):
    __slots__ = ("chunk_id", "old_chunk_column", "new_chunk_column")
    CHUNK_ID_FIELD_NUMBER: _ClassVar[int]
    OLD_CHUNK_COLUMN_FIELD_NUMBER: _ClassVar[int]
    NEW_CHUNK_COLUMN_FIELD_NUMBER: _ClassVar[int]
    chunk_id: _blob_store_pb2.ChunkIdProto
    old_chunk_column: _blob_store_pb2.ChunkFileMetadataProto.ChunkColumn
    new_chunk_column: _blob_store_pb2.ChunkFileMetadataProto.ChunkColumn
    def __init__(self, chunk_id: _Optional[_Union[_blob_store_pb2.ChunkIdProto, _Mapping]] = ..., old_chunk_column: _Optional[_Union[_blob_store_pb2.ChunkFileMetadataProto.ChunkColumn, _Mapping]] = ..., new_chunk_column: _Optional[_Union[_blob_store_pb2.ChunkFileMetadataProto.ChunkColumn, _Mapping]] = ...) -> None: ...

class ChunkgroupChange(_message.Message):
    __slots__ = ("chunkgroup_id", "old_chunkgroup_column", "new_chunkgroup_column")
    CHUNKGROUP_ID_FIELD_NUMBER: _ClassVar[int]
    OLD_CHUNKGROUP_COLUMN_FIELD_NUMBER: _ClassVar[int]
    NEW_CHUNKGROUP_COLUMN_FIELD_NUMBER: _ClassVar[int]
    chunkgroup_id: int
    old_chunkgroup_column: _blob_store_pb2.ChunkFileMetadataProto.ChunkGroupColumn
    new_chunkgroup_column: _blob_store_pb2.ChunkFileMetadataProto.ChunkGroupColumn
    def __init__(self, chunkgroup_id: _Optional[int] = ..., old_chunkgroup_column: _Optional[_Union[_blob_store_pb2.ChunkFileMetadataProto.ChunkGroupColumn, _Mapping]] = ..., new_chunkgroup_column: _Optional[_Union[_blob_store_pb2.ChunkFileMetadataProto.ChunkGroupColumn, _Mapping]] = ...) -> None: ...

class RemoveChunkFileArg(_message.Message):
    __slots__ = ("chunk_file_id", "replica_disk_id", "intent_id", "diff_usage", "high_priority", "reason")
    class Reason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kReplicaRemoval: _ClassVar[RemoveChunkFileArg.Reason]
        kChunkFileDeletion: _ClassVar[RemoveChunkFileArg.Reason]
    kReplicaRemoval: RemoveChunkFileArg.Reason
    kChunkFileDeletion: RemoveChunkFileArg.Reason
    CHUNK_FILE_ID_FIELD_NUMBER: _ClassVar[int]
    REPLICA_DISK_ID_FIELD_NUMBER: _ClassVar[int]
    INTENT_ID_FIELD_NUMBER: _ClassVar[int]
    DIFF_USAGE_FIELD_NUMBER: _ClassVar[int]
    HIGH_PRIORITY_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    chunk_file_id: int
    replica_disk_id: int
    intent_id: int
    diff_usage: _disk_usage_stats_pb2.DiskUsageStatsProto
    high_priority: bool
    reason: int
    def __init__(self, chunk_file_id: _Optional[int] = ..., replica_disk_id: _Optional[int] = ..., intent_id: _Optional[int] = ..., diff_usage: _Optional[_Union[_disk_usage_stats_pb2.DiskUsageStatsProto, _Mapping]] = ..., high_priority: bool = ..., reason: _Optional[int] = ...) -> None: ...

class RemoveChunkFileResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ReadChunksArg(_message.Message):
    __slots__ = ("chunk_file_id", "replica_disk_id", "lowest_acceptable_replica_version", "compression_level", "encryption_level", "chunk_info_vec", "chunkgroup_info_vec", "qos_principal", "view_box_id", "invoked_from_scrubber", "stripe_column", "is_coded_stripe", "request_context", "edek_info", "expected_encryption_mode")
    CHUNK_FILE_ID_FIELD_NUMBER: _ClassVar[int]
    REPLICA_DISK_ID_FIELD_NUMBER: _ClassVar[int]
    LOWEST_ACCEPTABLE_REPLICA_VERSION_FIELD_NUMBER: _ClassVar[int]
    COMPRESSION_LEVEL_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_LEVEL_FIELD_NUMBER: _ClassVar[int]
    CHUNK_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    CHUNKGROUP_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    QOS_PRINCIPAL_FIELD_NUMBER: _ClassVar[int]
    VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
    INVOKED_FROM_SCRUBBER_FIELD_NUMBER: _ClassVar[int]
    STRIPE_COLUMN_FIELD_NUMBER: _ClassVar[int]
    IS_CODED_STRIPE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    EDEK_INFO_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_ENCRYPTION_MODE_FIELD_NUMBER: _ClassVar[int]
    chunk_file_id: int
    replica_disk_id: int
    lowest_acceptable_replica_version: int
    compression_level: _cluster_config_pb2.ClusterConfigProto.StoragePolicy.CompressionLevel
    encryption_level: _cluster_config_pb2.ClusterConfigProto.EncryptionLevel
    chunk_info_vec: _containers.RepeatedCompositeFieldContainer[ChunkInfo]
    chunkgroup_info_vec: _containers.RepeatedCompositeFieldContainer[ChunkGroupInfo]
    qos_principal: _cluster_config_pb2.ClusterConfigProto.QoSPrincipal
    view_box_id: int
    invoked_from_scrubber: bool
    stripe_column: int
    is_coded_stripe: bool
    request_context: _request_context_pb2.RequestContextProto
    edek_info: _keychain_pb2.EdekProto
    expected_encryption_mode: _aes_encryptor_pb2.AESEncryptorMode
    def __init__(self, chunk_file_id: _Optional[int] = ..., replica_disk_id: _Optional[int] = ..., lowest_acceptable_replica_version: _Optional[int] = ..., compression_level: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.StoragePolicy.CompressionLevel, str]] = ..., encryption_level: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.EncryptionLevel, str]] = ..., chunk_info_vec: _Optional[_Iterable[_Union[ChunkInfo, _Mapping]]] = ..., chunkgroup_info_vec: _Optional[_Iterable[_Union[ChunkGroupInfo, _Mapping]]] = ..., qos_principal: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.QoSPrincipal, _Mapping]] = ..., view_box_id: _Optional[int] = ..., invoked_from_scrubber: bool = ..., stripe_column: _Optional[int] = ..., is_coded_stripe: bool = ..., request_context: _Optional[_Union[_request_context_pb2.RequestContextProto, _Mapping]] = ..., edek_info: _Optional[_Union[_keychain_pb2.EdekProto, _Mapping]] = ..., expected_encryption_mode: _Optional[_Union[_aes_encryptor_pb2.AESEncryptorMode, str]] = ...) -> None: ...

class ReadChunksResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CommonWriteChunks(_message.Message):
    __slots__ = ("chunk_file_id", "replica_vec", "intent_id", "expected_replica_version", "synced_replica_version", "compression_level", "encryption_level", "owner_blob_id", "view_box_id", "qos_principal", "request_context")
    CHUNK_FILE_ID_FIELD_NUMBER: _ClassVar[int]
    REPLICA_VEC_FIELD_NUMBER: _ClassVar[int]
    INTENT_ID_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_REPLICA_VERSION_FIELD_NUMBER: _ClassVar[int]
    SYNCED_REPLICA_VERSION_FIELD_NUMBER: _ClassVar[int]
    COMPRESSION_LEVEL_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_LEVEL_FIELD_NUMBER: _ClassVar[int]
    OWNER_BLOB_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
    QOS_PRINCIPAL_FIELD_NUMBER: _ClassVar[int]
    REQUEST_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    chunk_file_id: int
    replica_vec: _containers.RepeatedScalarFieldContainer[int]
    intent_id: int
    expected_replica_version: int
    synced_replica_version: int
    compression_level: _cluster_config_pb2.ClusterConfigProto.StoragePolicy.CompressionLevel
    encryption_level: _cluster_config_pb2.ClusterConfigProto.EncryptionLevel
    owner_blob_id: int
    view_box_id: int
    qos_principal: _cluster_config_pb2.ClusterConfigProto.QoSPrincipal
    request_context: _request_context_pb2.RequestContextProto
    def __init__(self, chunk_file_id: _Optional[int] = ..., replica_vec: _Optional[_Iterable[int]] = ..., intent_id: _Optional[int] = ..., expected_replica_version: _Optional[int] = ..., synced_replica_version: _Optional[int] = ..., compression_level: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.StoragePolicy.CompressionLevel, str]] = ..., encryption_level: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.EncryptionLevel, str]] = ..., owner_blob_id: _Optional[int] = ..., view_box_id: _Optional[int] = ..., qos_principal: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.QoSPrincipal, _Mapping]] = ..., request_context: _Optional[_Union[_request_context_pb2.RequestContextProto, _Mapping]] = ...) -> None: ...

class PrimaryWriteChunksArg(_message.Message):
    __slots__ = ("common", "chunk_info_vec", "chunkgroup_info_vec", "cached_lowest_finalized_version", "stats_container", "edek_info", "encryption_mode")
    COMMON_FIELD_NUMBER: _ClassVar[int]
    CHUNK_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    CHUNKGROUP_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    CACHED_LOWEST_FINALIZED_VERSION_FIELD_NUMBER: _ClassVar[int]
    STATS_CONTAINER_FIELD_NUMBER: _ClassVar[int]
    EDEK_INFO_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_MODE_FIELD_NUMBER: _ClassVar[int]
    common: CommonWriteChunks
    chunk_info_vec: _containers.RepeatedCompositeFieldContainer[ChunkInfo]
    chunkgroup_info_vec: _containers.RepeatedCompositeFieldContainer[ChunkGroupInfo]
    cached_lowest_finalized_version: int
    stats_container: int
    edek_info: _keychain_pb2.EdekProto
    encryption_mode: _aes_encryptor_pb2.AESEncryptorMode
    def __init__(self, common: _Optional[_Union[CommonWriteChunks, _Mapping]] = ..., chunk_info_vec: _Optional[_Iterable[_Union[ChunkInfo, _Mapping]]] = ..., chunkgroup_info_vec: _Optional[_Iterable[_Union[ChunkGroupInfo, _Mapping]]] = ..., cached_lowest_finalized_version: _Optional[int] = ..., stats_container: _Optional[int] = ..., edek_info: _Optional[_Union[_keychain_pb2.EdekProto, _Mapping]] = ..., encryption_mode: _Optional[_Union[_aes_encryptor_pb2.AESEncryptorMode, str]] = ...) -> None: ...

class PrimaryWriteChunksResult(_message.Message):
    __slots__ = ("chunk_info_vec", "chunkgroup_info_vec", "out_of_space_disk_vec")
    CHUNK_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    CHUNKGROUP_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    OUT_OF_SPACE_DISK_VEC_FIELD_NUMBER: _ClassVar[int]
    chunk_info_vec: _containers.RepeatedCompositeFieldContainer[ChunkInfo]
    chunkgroup_info_vec: _containers.RepeatedCompositeFieldContainer[ChunkGroupInfo]
    out_of_space_disk_vec: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, chunk_info_vec: _Optional[_Iterable[_Union[ChunkInfo, _Mapping]]] = ..., chunkgroup_info_vec: _Optional[_Iterable[_Union[ChunkGroupInfo, _Mapping]]] = ..., out_of_space_disk_vec: _Optional[_Iterable[int]] = ...) -> None: ...

class AuxWriteChunksArg(_message.Message):
    __slots__ = ("common", "chunk_change_vec", "chunkgroup_change_vec", "write_region_vec", "forwarding_number", "update_intent_checksum")
    class WriteRegion(_message.Message):
        __slots__ = ("chunk_file_offset", "region_size")
        CHUNK_FILE_OFFSET_FIELD_NUMBER: _ClassVar[int]
        REGION_SIZE_FIELD_NUMBER: _ClassVar[int]
        chunk_file_offset: int
        region_size: int
        def __init__(self, chunk_file_offset: _Optional[int] = ..., region_size: _Optional[int] = ...) -> None: ...
    COMMON_FIELD_NUMBER: _ClassVar[int]
    CHUNK_CHANGE_VEC_FIELD_NUMBER: _ClassVar[int]
    CHUNKGROUP_CHANGE_VEC_FIELD_NUMBER: _ClassVar[int]
    WRITE_REGION_VEC_FIELD_NUMBER: _ClassVar[int]
    FORWARDING_NUMBER_FIELD_NUMBER: _ClassVar[int]
    UPDATE_INTENT_CHECKSUM_FIELD_NUMBER: _ClassVar[int]
    common: CommonWriteChunks
    chunk_change_vec: _containers.RepeatedCompositeFieldContainer[ChunkChange]
    chunkgroup_change_vec: _containers.RepeatedCompositeFieldContainer[ChunkgroupChange]
    write_region_vec: _containers.RepeatedCompositeFieldContainer[AuxWriteChunksArg.WriteRegion]
    forwarding_number: int
    update_intent_checksum: int
    def __init__(self, common: _Optional[_Union[CommonWriteChunks, _Mapping]] = ..., chunk_change_vec: _Optional[_Iterable[_Union[ChunkChange, _Mapping]]] = ..., chunkgroup_change_vec: _Optional[_Iterable[_Union[ChunkgroupChange, _Mapping]]] = ..., write_region_vec: _Optional[_Iterable[_Union[AuxWriteChunksArg.WriteRegion, _Mapping]]] = ..., forwarding_number: _Optional[int] = ..., update_intent_checksum: _Optional[int] = ...) -> None: ...

class AuxWriteChunksResult(_message.Message):
    __slots__ = ("out_of_space_disk_vec",)
    OUT_OF_SPACE_DISK_VEC_FIELD_NUMBER: _ClassVar[int]
    out_of_space_disk_vec: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, out_of_space_disk_vec: _Optional[_Iterable[int]] = ...) -> None: ...

class FetchChunkFileInfoArg(_message.Message):
    __slots__ = ("chunk_file_id", "replica_disk_id", "intent_id", "synced_replica_version", "stripe_col", "skip_intent_id_check", "is_coded_stripe")
    CHUNK_FILE_ID_FIELD_NUMBER: _ClassVar[int]
    REPLICA_DISK_ID_FIELD_NUMBER: _ClassVar[int]
    INTENT_ID_FIELD_NUMBER: _ClassVar[int]
    SYNCED_REPLICA_VERSION_FIELD_NUMBER: _ClassVar[int]
    STRIPE_COL_FIELD_NUMBER: _ClassVar[int]
    SKIP_INTENT_ID_CHECK_FIELD_NUMBER: _ClassVar[int]
    IS_CODED_STRIPE_FIELD_NUMBER: _ClassVar[int]
    chunk_file_id: int
    replica_disk_id: int
    intent_id: int
    synced_replica_version: int
    stripe_col: int
    skip_intent_id_check: bool
    is_coded_stripe: bool
    def __init__(self, chunk_file_id: _Optional[int] = ..., replica_disk_id: _Optional[int] = ..., intent_id: _Optional[int] = ..., synced_replica_version: _Optional[int] = ..., stripe_col: _Optional[int] = ..., skip_intent_id_check: bool = ..., is_coded_stripe: bool = ...) -> None: ...

class FetchChunkFileInfoResult(_message.Message):
    __slots__ = ("replica_version", "replica_corrupt", "chunk_info_vec", "chunkgroup_info_vec", "corrupt_time_stamp_usecs", "corrupt_reason")
    REPLICA_VERSION_FIELD_NUMBER: _ClassVar[int]
    REPLICA_CORRUPT_FIELD_NUMBER: _ClassVar[int]
    CHUNK_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    CHUNKGROUP_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    CORRUPT_TIME_STAMP_USECS_FIELD_NUMBER: _ClassVar[int]
    CORRUPT_REASON_FIELD_NUMBER: _ClassVar[int]
    replica_version: int
    replica_corrupt: bool
    chunk_info_vec: _containers.RepeatedCompositeFieldContainer[ChunkInfo]
    chunkgroup_info_vec: _containers.RepeatedCompositeFieldContainer[ChunkGroupInfo]
    corrupt_time_stamp_usecs: int
    corrupt_reason: int
    def __init__(self, replica_version: _Optional[int] = ..., replica_corrupt: bool = ..., chunk_info_vec: _Optional[_Iterable[_Union[ChunkInfo, _Mapping]]] = ..., chunkgroup_info_vec: _Optional[_Iterable[_Union[ChunkGroupInfo, _Mapping]]] = ..., corrupt_time_stamp_usecs: _Optional[int] = ..., corrupt_reason: _Optional[int] = ...) -> None: ...

class ListChunkFilesArg(_message.Message):
    __slots__ = ("cookie", "replica_disk_id", "ignore_corrupted_chunk_files")
    COOKIE_FIELD_NUMBER: _ClassVar[int]
    REPLICA_DISK_ID_FIELD_NUMBER: _ClassVar[int]
    IGNORE_CORRUPTED_CHUNK_FILES_FIELD_NUMBER: _ClassVar[int]
    cookie: bytes
    replica_disk_id: int
    ignore_corrupted_chunk_files: bool
    def __init__(self, cookie: _Optional[bytes] = ..., replica_disk_id: _Optional[int] = ..., ignore_corrupted_chunk_files: bool = ...) -> None: ...

class ListChunkFilesResult(_message.Message):
    __slots__ = ("chunk_file_id_vec", "next_cookie")
    CHUNK_FILE_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    NEXT_COOKIE_FIELD_NUMBER: _ClassVar[int]
    chunk_file_id_vec: _containers.RepeatedScalarFieldContainer[int]
    next_cookie: bytes
    def __init__(self, chunk_file_id_vec: _Optional[_Iterable[int]] = ..., next_cookie: _Optional[bytes] = ...) -> None: ...

class ReplicateChunkFileArg(_message.Message):
    __slots__ = ("chunk_file_id", "src_disk_id", "target_disk_id", "intent_id", "replica_version", "is_best_effort", "chunk_info_vec", "chunkgroup_info_vec", "diff_usage", "higher_on_disk_version_ok", "stripe_column", "is_coded_stripe", "request_context", "view_box_id")
    CHUNK_FILE_ID_FIELD_NUMBER: _ClassVar[int]
    SRC_DISK_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_DISK_ID_FIELD_NUMBER: _ClassVar[int]
    INTENT_ID_FIELD_NUMBER: _ClassVar[int]
    REPLICA_VERSION_FIELD_NUMBER: _ClassVar[int]
    IS_BEST_EFFORT_FIELD_NUMBER: _ClassVar[int]
    CHUNK_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    CHUNKGROUP_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    DIFF_USAGE_FIELD_NUMBER: _ClassVar[int]
    HIGHER_ON_DISK_VERSION_OK_FIELD_NUMBER: _ClassVar[int]
    STRIPE_COLUMN_FIELD_NUMBER: _ClassVar[int]
    IS_CODED_STRIPE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
    chunk_file_id: int
    src_disk_id: int
    target_disk_id: int
    intent_id: int
    replica_version: int
    is_best_effort: bool
    chunk_info_vec: _containers.RepeatedCompositeFieldContainer[ChunkInfo]
    chunkgroup_info_vec: _containers.RepeatedCompositeFieldContainer[ChunkGroupInfo]
    diff_usage: _disk_usage_stats_pb2.DiskUsageStatsProto
    higher_on_disk_version_ok: bool
    stripe_column: int
    is_coded_stripe: bool
    request_context: _request_context_pb2.RequestContextProto
    view_box_id: int
    def __init__(self, chunk_file_id: _Optional[int] = ..., src_disk_id: _Optional[int] = ..., target_disk_id: _Optional[int] = ..., intent_id: _Optional[int] = ..., replica_version: _Optional[int] = ..., is_best_effort: bool = ..., chunk_info_vec: _Optional[_Iterable[_Union[ChunkInfo, _Mapping]]] = ..., chunkgroup_info_vec: _Optional[_Iterable[_Union[ChunkGroupInfo, _Mapping]]] = ..., diff_usage: _Optional[_Union[_disk_usage_stats_pb2.DiskUsageStatsProto, _Mapping]] = ..., higher_on_disk_version_ok: bool = ..., stripe_column: _Optional[int] = ..., is_coded_stripe: bool = ..., request_context: _Optional[_Union[_request_context_pb2.RequestContextProto, _Mapping]] = ..., view_box_id: _Optional[int] = ...) -> None: ...

class ReplicateChunkFileResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ReadMorphedDataArg(_message.Message):
    __slots__ = ("chunk_file_id", "disk_id", "replica_version", "is_best_effort", "chunk_info_vec", "chunkgroup_info_vec", "prefetch_only", "higher_on_disk_version_ok", "stripe_column", "is_coded_stripe", "is_for_replication", "request_context", "view_box_id", "read_corrupt_chunk_file")
    CHUNK_FILE_ID_FIELD_NUMBER: _ClassVar[int]
    DISK_ID_FIELD_NUMBER: _ClassVar[int]
    REPLICA_VERSION_FIELD_NUMBER: _ClassVar[int]
    IS_BEST_EFFORT_FIELD_NUMBER: _ClassVar[int]
    CHUNK_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    CHUNKGROUP_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    PREFETCH_ONLY_FIELD_NUMBER: _ClassVar[int]
    HIGHER_ON_DISK_VERSION_OK_FIELD_NUMBER: _ClassVar[int]
    STRIPE_COLUMN_FIELD_NUMBER: _ClassVar[int]
    IS_CODED_STRIPE_FIELD_NUMBER: _ClassVar[int]
    IS_FOR_REPLICATION_FIELD_NUMBER: _ClassVar[int]
    REQUEST_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
    READ_CORRUPT_CHUNK_FILE_FIELD_NUMBER: _ClassVar[int]
    chunk_file_id: int
    disk_id: int
    replica_version: int
    is_best_effort: bool
    chunk_info_vec: _containers.RepeatedCompositeFieldContainer[ChunkInfo]
    chunkgroup_info_vec: _containers.RepeatedCompositeFieldContainer[ChunkGroupInfo]
    prefetch_only: bool
    higher_on_disk_version_ok: bool
    stripe_column: int
    is_coded_stripe: bool
    is_for_replication: bool
    request_context: _request_context_pb2.RequestContextProto
    view_box_id: int
    read_corrupt_chunk_file: bool
    def __init__(self, chunk_file_id: _Optional[int] = ..., disk_id: _Optional[int] = ..., replica_version: _Optional[int] = ..., is_best_effort: bool = ..., chunk_info_vec: _Optional[_Iterable[_Union[ChunkInfo, _Mapping]]] = ..., chunkgroup_info_vec: _Optional[_Iterable[_Union[ChunkGroupInfo, _Mapping]]] = ..., prefetch_only: bool = ..., higher_on_disk_version_ok: bool = ..., stripe_column: _Optional[int] = ..., is_coded_stripe: bool = ..., is_for_replication: bool = ..., request_context: _Optional[_Union[_request_context_pb2.RequestContextProto, _Mapping]] = ..., view_box_id: _Optional[int] = ..., read_corrupt_chunk_file: bool = ...) -> None: ...

class ReadMorphedDataResult(_message.Message):
    __slots__ = ("corrupt_chunk_id_vec", "corrupt_chunkgroup_id_vec")
    CORRUPT_CHUNK_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    CORRUPT_CHUNKGROUP_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    corrupt_chunk_id_vec: _containers.RepeatedCompositeFieldContainer[_blob_store_pb2.ChunkIdProto]
    corrupt_chunkgroup_id_vec: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, corrupt_chunk_id_vec: _Optional[_Iterable[_Union[_blob_store_pb2.ChunkIdProto, _Mapping]]] = ..., corrupt_chunkgroup_id_vec: _Optional[_Iterable[int]] = ...) -> None: ...

class AdjustDiskUsageArg(_message.Message):
    __slots__ = ("chunk_file_id", "disk_id", "diff_usage")
    CHUNK_FILE_ID_FIELD_NUMBER: _ClassVar[int]
    DISK_ID_FIELD_NUMBER: _ClassVar[int]
    DIFF_USAGE_FIELD_NUMBER: _ClassVar[int]
    chunk_file_id: int
    disk_id: int
    diff_usage: _disk_usage_stats_pb2.DiskUsageStatsProto
    def __init__(self, chunk_file_id: _Optional[int] = ..., disk_id: _Optional[int] = ..., diff_usage: _Optional[_Union[_disk_usage_stats_pb2.DiskUsageStatsProto, _Mapping]] = ...) -> None: ...

class AdjustDiskUsageResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ClearChunkFileCorruptFlagArg(_message.Message):
    __slots__ = ("chunk_file_id", "disk_id")
    CHUNK_FILE_ID_FIELD_NUMBER: _ClassVar[int]
    DISK_ID_FIELD_NUMBER: _ClassVar[int]
    chunk_file_id: int
    disk_id: int
    def __init__(self, chunk_file_id: _Optional[int] = ..., disk_id: _Optional[int] = ...) -> None: ...

class ClearChunkFileCorruptFlagResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetChunkFileCountArg(_message.Message):
    __slots__ = ("disk_id",)
    DISK_ID_FIELD_NUMBER: _ClassVar[int]
    disk_id: int
    def __init__(self, disk_id: _Optional[int] = ...) -> None: ...

class GetChunkFileCountResult(_message.Message):
    __slots__ = ("chunk_file_count",)
    CHUNK_FILE_COUNT_FIELD_NUMBER: _ClassVar[int]
    chunk_file_count: int
    def __init__(self, chunk_file_count: _Optional[int] = ...) -> None: ...

class WriteRawArg(_message.Message):
    __slots__ = ("chunk_file_id", "disk_id", "intent_id", "owner_blob_id", "view_box_id", "offset", "unmorphed_data_size", "morphed_data_size", "dedup_chunks", "morphed", "qos_principal", "version", "stripe_column", "is_coded_stripe", "request_context")
    CHUNK_FILE_ID_FIELD_NUMBER: _ClassVar[int]
    DISK_ID_FIELD_NUMBER: _ClassVar[int]
    INTENT_ID_FIELD_NUMBER: _ClassVar[int]
    OWNER_BLOB_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    UNMORPHED_DATA_SIZE_FIELD_NUMBER: _ClassVar[int]
    MORPHED_DATA_SIZE_FIELD_NUMBER: _ClassVar[int]
    DEDUP_CHUNKS_FIELD_NUMBER: _ClassVar[int]
    MORPHED_FIELD_NUMBER: _ClassVar[int]
    QOS_PRINCIPAL_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    STRIPE_COLUMN_FIELD_NUMBER: _ClassVar[int]
    IS_CODED_STRIPE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    chunk_file_id: int
    disk_id: int
    intent_id: int
    owner_blob_id: int
    view_box_id: int
    offset: int
    unmorphed_data_size: int
    morphed_data_size: int
    dedup_chunks: bool
    morphed: bool
    qos_principal: _cluster_config_pb2.ClusterConfigProto.QoSPrincipal
    version: int
    stripe_column: int
    is_coded_stripe: bool
    request_context: _request_context_pb2.RequestContextProto
    def __init__(self, chunk_file_id: _Optional[int] = ..., disk_id: _Optional[int] = ..., intent_id: _Optional[int] = ..., owner_blob_id: _Optional[int] = ..., view_box_id: _Optional[int] = ..., offset: _Optional[int] = ..., unmorphed_data_size: _Optional[int] = ..., morphed_data_size: _Optional[int] = ..., dedup_chunks: bool = ..., morphed: bool = ..., qos_principal: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.QoSPrincipal, _Mapping]] = ..., version: _Optional[int] = ..., stripe_column: _Optional[int] = ..., is_coded_stripe: bool = ..., request_context: _Optional[_Union[_request_context_pb2.RequestContextProto, _Mapping]] = ...) -> None: ...

class WriteRawResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class TruncateChunkFileArg(_message.Message):
    __slots__ = ("chunk_file_id", "disk_id", "qos_principal", "request_context")
    CHUNK_FILE_ID_FIELD_NUMBER: _ClassVar[int]
    DISK_ID_FIELD_NUMBER: _ClassVar[int]
    QOS_PRINCIPAL_FIELD_NUMBER: _ClassVar[int]
    REQUEST_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    chunk_file_id: int
    disk_id: int
    qos_principal: _cluster_config_pb2.ClusterConfigProto.QoSPrincipal
    request_context: _request_context_pb2.RequestContextProto
    def __init__(self, chunk_file_id: _Optional[int] = ..., disk_id: _Optional[int] = ..., qos_principal: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.QoSPrincipal, _Mapping]] = ..., request_context: _Optional[_Union[_request_context_pb2.RequestContextProto, _Mapping]] = ...) -> None: ...

class TruncateChunkFileResult(_message.Message):
    __slots__ = ("num_bytes_truncated",)
    NUM_BYTES_TRUNCATED_FIELD_NUMBER: _ClassVar[int]
    num_bytes_truncated: int
    def __init__(self, num_bytes_truncated: _Optional[int] = ...) -> None: ...

class SetChunkFileUsageHintArg(_message.Message):
    __slots__ = ("chunk_file_id", "disk_id", "intent_id", "usage")
    CHUNK_FILE_ID_FIELD_NUMBER: _ClassVar[int]
    DISK_ID_FIELD_NUMBER: _ClassVar[int]
    INTENT_ID_FIELD_NUMBER: _ClassVar[int]
    USAGE_FIELD_NUMBER: _ClassVar[int]
    chunk_file_id: int
    disk_id: int
    intent_id: int
    usage: _disk_usage_stats_pb2.DiskUsageStatsProto
    def __init__(self, chunk_file_id: _Optional[int] = ..., disk_id: _Optional[int] = ..., intent_id: _Optional[int] = ..., usage: _Optional[_Union[_disk_usage_stats_pb2.DiskUsageStatsProto, _Mapping]] = ...) -> None: ...

class SetChunkFileUsageHintResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ScrubChunkFileArg(_message.Message):
    __slots__ = ("chunk_file_id", "disk_id", "only_scrub_corrupt_chunk_file")
    CHUNK_FILE_ID_FIELD_NUMBER: _ClassVar[int]
    DISK_ID_FIELD_NUMBER: _ClassVar[int]
    ONLY_SCRUB_CORRUPT_CHUNK_FILE_FIELD_NUMBER: _ClassVar[int]
    chunk_file_id: int
    disk_id: int
    only_scrub_corrupt_chunk_file: bool
    def __init__(self, chunk_file_id: _Optional[int] = ..., disk_id: _Optional[int] = ..., only_scrub_corrupt_chunk_file: bool = ...) -> None: ...

class ScrubChunkFileResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
