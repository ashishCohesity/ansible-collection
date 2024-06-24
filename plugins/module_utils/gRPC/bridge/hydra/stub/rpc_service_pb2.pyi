from bridge.hydra.base import epoch_pb2 as _epoch_pb2
from configs import cluster_config_pb2 as _cluster_config_pb2
from open_util.net import protorpc_pb2 as _protorpc_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ByteRange(_message.Message):
    __slots__ = ("logical_offset", "write_offset", "write_length", "adler32_cksum", "block_offset", "logical_length", "compression_level", "compressed_length", "inline_payload_offset")
    LOGICAL_OFFSET_FIELD_NUMBER: _ClassVar[int]
    WRITE_OFFSET_FIELD_NUMBER: _ClassVar[int]
    WRITE_LENGTH_FIELD_NUMBER: _ClassVar[int]
    ADLER32_CKSUM_FIELD_NUMBER: _ClassVar[int]
    BLOCK_OFFSET_FIELD_NUMBER: _ClassVar[int]
    LOGICAL_LENGTH_FIELD_NUMBER: _ClassVar[int]
    COMPRESSION_LEVEL_FIELD_NUMBER: _ClassVar[int]
    COMPRESSED_LENGTH_FIELD_NUMBER: _ClassVar[int]
    INLINE_PAYLOAD_OFFSET_FIELD_NUMBER: _ClassVar[int]
    logical_offset: int
    write_offset: int
    write_length: int
    adler32_cksum: int
    block_offset: int
    logical_length: int
    compression_level: _cluster_config_pb2.ClusterConfigProto.StoragePolicy.CompressionLevel
    compressed_length: int
    inline_payload_offset: int
    def __init__(self, logical_offset: _Optional[int] = ..., write_offset: _Optional[int] = ..., write_length: _Optional[int] = ..., adler32_cksum: _Optional[int] = ..., block_offset: _Optional[int] = ..., logical_length: _Optional[int] = ..., compression_level: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.StoragePolicy.CompressionLevel, str]] = ..., compressed_length: _Optional[int] = ..., inline_payload_offset: _Optional[int] = ...) -> None: ...

class MetadataRecord(_message.Message):
    __slots__ = ("sequence_id", "writes", "max_committed_sequence_id", "flushes", "is_random", "stats_container_id", "write_issue_usecs", "qos_principal_id", "view_id")
    class FlushData(_message.Message):
        __slots__ = ("epoch_id", "sequence_id", "blob_offset", "write_length", "flush_finish_usecs")
        EPOCH_ID_FIELD_NUMBER: _ClassVar[int]
        SEQUENCE_ID_FIELD_NUMBER: _ClassVar[int]
        BLOB_OFFSET_FIELD_NUMBER: _ClassVar[int]
        WRITE_LENGTH_FIELD_NUMBER: _ClassVar[int]
        FLUSH_FINISH_USECS_FIELD_NUMBER: _ClassVar[int]
        epoch_id: int
        sequence_id: int
        blob_offset: int
        write_length: int
        flush_finish_usecs: int
        def __init__(self, epoch_id: _Optional[int] = ..., sequence_id: _Optional[int] = ..., blob_offset: _Optional[int] = ..., write_length: _Optional[int] = ..., flush_finish_usecs: _Optional[int] = ...) -> None: ...
    SEQUENCE_ID_FIELD_NUMBER: _ClassVar[int]
    WRITES_FIELD_NUMBER: _ClassVar[int]
    MAX_COMMITTED_SEQUENCE_ID_FIELD_NUMBER: _ClassVar[int]
    FLUSHES_FIELD_NUMBER: _ClassVar[int]
    IS_RANDOM_FIELD_NUMBER: _ClassVar[int]
    STATS_CONTAINER_ID_FIELD_NUMBER: _ClassVar[int]
    WRITE_ISSUE_USECS_FIELD_NUMBER: _ClassVar[int]
    QOS_PRINCIPAL_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_ID_FIELD_NUMBER: _ClassVar[int]
    sequence_id: int
    writes: _containers.RepeatedCompositeFieldContainer[ByteRange]
    max_committed_sequence_id: int
    flushes: _containers.RepeatedCompositeFieldContainer[MetadataRecord.FlushData]
    is_random: bool
    stats_container_id: int
    write_issue_usecs: int
    qos_principal_id: int
    view_id: int
    def __init__(self, sequence_id: _Optional[int] = ..., writes: _Optional[_Iterable[_Union[ByteRange, _Mapping]]] = ..., max_committed_sequence_id: _Optional[int] = ..., flushes: _Optional[_Iterable[_Union[MetadataRecord.FlushData, _Mapping]]] = ..., is_random: bool = ..., stats_container_id: _Optional[int] = ..., write_issue_usecs: _Optional[int] = ..., qos_principal_id: _Optional[int] = ..., view_id: _Optional[int] = ...) -> None: ...

class RemovedRanges(_message.Message):
    __slots__ = ("ranges",)
    class Range(_message.Message):
        __slots__ = ("data_file_offset", "length")
        DATA_FILE_OFFSET_FIELD_NUMBER: _ClassVar[int]
        LENGTH_FIELD_NUMBER: _ClassVar[int]
        data_file_offset: int
        length: int
        def __init__(self, data_file_offset: _Optional[int] = ..., length: _Optional[int] = ...) -> None: ...
    RANGES_FIELD_NUMBER: _ClassVar[int]
    ranges: _containers.RepeatedCompositeFieldContainer[RemovedRanges.Range]
    def __init__(self, ranges: _Optional[_Iterable[_Union[RemovedRanges.Range, _Mapping]]] = ...) -> None: ...

class WriteArg(_message.Message):
    __slots__ = ("master_incarnation_id", "blob_id", "epoch_id", "replica_vec", "write_data", "removed_ranges", "roll_forward_write", "view_box_id", "send_request_to_peer", "qos_principal", "metadata_write_offset", "formatted_metadata_record_size", "inline_payload_size", "data_write_offset", "blur_blob_view_id")
    MASTER_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    BLOB_ID_FIELD_NUMBER: _ClassVar[int]
    EPOCH_ID_FIELD_NUMBER: _ClassVar[int]
    REPLICA_VEC_FIELD_NUMBER: _ClassVar[int]
    WRITE_DATA_FIELD_NUMBER: _ClassVar[int]
    REMOVED_RANGES_FIELD_NUMBER: _ClassVar[int]
    ROLL_FORWARD_WRITE_FIELD_NUMBER: _ClassVar[int]
    VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
    SEND_REQUEST_TO_PEER_FIELD_NUMBER: _ClassVar[int]
    QOS_PRINCIPAL_FIELD_NUMBER: _ClassVar[int]
    METADATA_WRITE_OFFSET_FIELD_NUMBER: _ClassVar[int]
    FORMATTED_METADATA_RECORD_SIZE_FIELD_NUMBER: _ClassVar[int]
    INLINE_PAYLOAD_SIZE_FIELD_NUMBER: _ClassVar[int]
    DATA_WRITE_OFFSET_FIELD_NUMBER: _ClassVar[int]
    BLUR_BLOB_VIEW_ID_FIELD_NUMBER: _ClassVar[int]
    master_incarnation_id: int
    blob_id: int
    epoch_id: int
    replica_vec: _containers.RepeatedCompositeFieldContainer[_epoch_pb2.SlaveSelection]
    write_data: MetadataRecord
    removed_ranges: RemovedRanges
    roll_forward_write: bool
    view_box_id: int
    send_request_to_peer: bool
    qos_principal: _cluster_config_pb2.ClusterConfigProto.QoSPrincipal
    metadata_write_offset: int
    formatted_metadata_record_size: int
    inline_payload_size: int
    data_write_offset: int
    blur_blob_view_id: int
    def __init__(self, master_incarnation_id: _Optional[int] = ..., blob_id: _Optional[int] = ..., epoch_id: _Optional[int] = ..., replica_vec: _Optional[_Iterable[_Union[_epoch_pb2.SlaveSelection, _Mapping]]] = ..., write_data: _Optional[_Union[MetadataRecord, _Mapping]] = ..., removed_ranges: _Optional[_Union[RemovedRanges, _Mapping]] = ..., roll_forward_write: bool = ..., view_box_id: _Optional[int] = ..., send_request_to_peer: bool = ..., qos_principal: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.QoSPrincipal, _Mapping]] = ..., metadata_write_offset: _Optional[int] = ..., formatted_metadata_record_size: _Optional[int] = ..., inline_payload_size: _Optional[int] = ..., data_write_offset: _Optional[int] = ..., blur_blob_view_id: _Optional[int] = ...) -> None: ...

class WriteResult(_message.Message):
    __slots__ = ("read_only_disk_vec", "missing_disk_vec")
    class ReadOnlyDisk(_message.Message):
        __slots__ = ("disk_id", "disk_version", "avoid_access")
        DISK_ID_FIELD_NUMBER: _ClassVar[int]
        DISK_VERSION_FIELD_NUMBER: _ClassVar[int]
        AVOID_ACCESS_FIELD_NUMBER: _ClassVar[int]
        disk_id: int
        disk_version: int
        avoid_access: int
        def __init__(self, disk_id: _Optional[int] = ..., disk_version: _Optional[int] = ..., avoid_access: _Optional[int] = ...) -> None: ...
    class MissingDisk(_message.Message):
        __slots__ = ("disk_id", "disk_version")
        DISK_ID_FIELD_NUMBER: _ClassVar[int]
        DISK_VERSION_FIELD_NUMBER: _ClassVar[int]
        disk_id: int
        disk_version: int
        def __init__(self, disk_id: _Optional[int] = ..., disk_version: _Optional[int] = ...) -> None: ...
    READ_ONLY_DISK_VEC_FIELD_NUMBER: _ClassVar[int]
    MISSING_DISK_VEC_FIELD_NUMBER: _ClassVar[int]
    read_only_disk_vec: _containers.RepeatedCompositeFieldContainer[WriteResult.ReadOnlyDisk]
    missing_disk_vec: _containers.RepeatedCompositeFieldContainer[WriteResult.MissingDisk]
    def __init__(self, read_only_disk_vec: _Optional[_Iterable[_Union[WriteResult.ReadOnlyDisk, _Mapping]]] = ..., missing_disk_vec: _Optional[_Iterable[_Union[WriteResult.MissingDisk, _Mapping]]] = ...) -> None: ...

class ReadArg(_message.Message):
    __slots__ = ("blob_id", "epoch_id", "disk_id", "byte_ranges", "view_box_id", "trim_to_logical_range", "should_decrypt", "qos_principal", "is_canonical_epoch")
    BLOB_ID_FIELD_NUMBER: _ClassVar[int]
    EPOCH_ID_FIELD_NUMBER: _ClassVar[int]
    DISK_ID_FIELD_NUMBER: _ClassVar[int]
    BYTE_RANGES_FIELD_NUMBER: _ClassVar[int]
    VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
    TRIM_TO_LOGICAL_RANGE_FIELD_NUMBER: _ClassVar[int]
    SHOULD_DECRYPT_FIELD_NUMBER: _ClassVar[int]
    QOS_PRINCIPAL_FIELD_NUMBER: _ClassVar[int]
    IS_CANONICAL_EPOCH_FIELD_NUMBER: _ClassVar[int]
    blob_id: int
    epoch_id: int
    disk_id: int
    byte_ranges: _containers.RepeatedCompositeFieldContainer[ByteRange]
    view_box_id: int
    trim_to_logical_range: bool
    should_decrypt: bool
    qos_principal: _cluster_config_pb2.ClusterConfigProto.QoSPrincipal
    is_canonical_epoch: bool
    def __init__(self, blob_id: _Optional[int] = ..., epoch_id: _Optional[int] = ..., disk_id: _Optional[int] = ..., byte_ranges: _Optional[_Iterable[_Union[ByteRange, _Mapping]]] = ..., view_box_id: _Optional[int] = ..., trim_to_logical_range: bool = ..., should_decrypt: bool = ..., qos_principal: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.QoSPrincipal, _Mapping]] = ..., is_canonical_epoch: bool = ...) -> None: ...

class ReadResult(_message.Message):
    __slots__ = ("has_data", "available_ranges", "disk_version")
    HAS_DATA_FIELD_NUMBER: _ClassVar[int]
    AVAILABLE_RANGES_FIELD_NUMBER: _ClassVar[int]
    DISK_VERSION_FIELD_NUMBER: _ClassVar[int]
    has_data: bool
    available_ranges: _containers.RepeatedCompositeFieldContainer[ByteRange]
    disk_version: int
    def __init__(self, has_data: bool = ..., available_ranges: _Optional[_Iterable[_Union[ByteRange, _Mapping]]] = ..., disk_version: _Optional[int] = ...) -> None: ...

class CloneArg(_message.Message):
    __slots__ = ("blob_id", "epoch_id", "disk_id", "new_blob_id_vec", "view_box_id", "blur_blob_view_id", "canonical_blob_id")
    BLOB_ID_FIELD_NUMBER: _ClassVar[int]
    EPOCH_ID_FIELD_NUMBER: _ClassVar[int]
    DISK_ID_FIELD_NUMBER: _ClassVar[int]
    NEW_BLOB_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
    BLUR_BLOB_VIEW_ID_FIELD_NUMBER: _ClassVar[int]
    CANONICAL_BLOB_ID_FIELD_NUMBER: _ClassVar[int]
    blob_id: int
    epoch_id: int
    disk_id: int
    new_blob_id_vec: _containers.RepeatedScalarFieldContainer[int]
    view_box_id: int
    blur_blob_view_id: int
    canonical_blob_id: int
    def __init__(self, blob_id: _Optional[int] = ..., epoch_id: _Optional[int] = ..., disk_id: _Optional[int] = ..., new_blob_id_vec: _Optional[_Iterable[int]] = ..., view_box_id: _Optional[int] = ..., blur_blob_view_id: _Optional[int] = ..., canonical_blob_id: _Optional[int] = ...) -> None: ...

class CloneResult(_message.Message):
    __slots__ = ("disk_version", "canonical_blob_id")
    DISK_VERSION_FIELD_NUMBER: _ClassVar[int]
    CANONICAL_BLOB_ID_FIELD_NUMBER: _ClassVar[int]
    disk_version: int
    canonical_blob_id: int
    def __init__(self, disk_version: _Optional[int] = ..., canonical_blob_id: _Optional[int] = ...) -> None: ...

class RemoveEpochArg(_message.Message):
    __slots__ = ("blob_id", "epoch_id", "disk_id", "blur_blob_view_id", "is_canonical_epoch", "force")
    BLOB_ID_FIELD_NUMBER: _ClassVar[int]
    EPOCH_ID_FIELD_NUMBER: _ClassVar[int]
    DISK_ID_FIELD_NUMBER: _ClassVar[int]
    BLUR_BLOB_VIEW_ID_FIELD_NUMBER: _ClassVar[int]
    IS_CANONICAL_EPOCH_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    blob_id: int
    epoch_id: int
    disk_id: int
    blur_blob_view_id: int
    is_canonical_epoch: bool
    force: bool
    def __init__(self, blob_id: _Optional[int] = ..., epoch_id: _Optional[int] = ..., disk_id: _Optional[int] = ..., blur_blob_view_id: _Optional[int] = ..., is_canonical_epoch: bool = ..., force: bool = ...) -> None: ...

class RemoveEpochResult(_message.Message):
    __slots__ = ("disk_version",)
    DISK_VERSION_FIELD_NUMBER: _ClassVar[int]
    disk_version: int
    def __init__(self, disk_version: _Optional[int] = ...) -> None: ...

class RemoveRangesArg(_message.Message):
    __slots__ = ("blob_id", "epoch_id", "replica_vec", "removed_ranges", "view_box_id", "blur_blob_view_id")
    BLOB_ID_FIELD_NUMBER: _ClassVar[int]
    EPOCH_ID_FIELD_NUMBER: _ClassVar[int]
    REPLICA_VEC_FIELD_NUMBER: _ClassVar[int]
    REMOVED_RANGES_FIELD_NUMBER: _ClassVar[int]
    VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
    BLUR_BLOB_VIEW_ID_FIELD_NUMBER: _ClassVar[int]
    blob_id: int
    epoch_id: int
    replica_vec: _containers.RepeatedCompositeFieldContainer[_epoch_pb2.SlaveSelection]
    removed_ranges: RemovedRanges
    view_box_id: int
    blur_blob_view_id: int
    def __init__(self, blob_id: _Optional[int] = ..., epoch_id: _Optional[int] = ..., replica_vec: _Optional[_Iterable[_Union[_epoch_pb2.SlaveSelection, _Mapping]]] = ..., removed_ranges: _Optional[_Union[RemovedRanges, _Mapping]] = ..., view_box_id: _Optional[int] = ..., blur_blob_view_id: _Optional[int] = ...) -> None: ...

class RemoveRangesResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ReadIndexArg(_message.Message):
    __slots__ = ("blob_id", "epoch_id", "disk_id", "is_canonical_blob", "cookie")
    BLOB_ID_FIELD_NUMBER: _ClassVar[int]
    EPOCH_ID_FIELD_NUMBER: _ClassVar[int]
    DISK_ID_FIELD_NUMBER: _ClassVar[int]
    IS_CANONICAL_BLOB_FIELD_NUMBER: _ClassVar[int]
    COOKIE_FIELD_NUMBER: _ClassVar[int]
    blob_id: int
    epoch_id: int
    disk_id: int
    is_canonical_blob: bool
    cookie: bytes
    def __init__(self, blob_id: _Optional[int] = ..., epoch_id: _Optional[int] = ..., disk_id: _Optional[int] = ..., is_canonical_blob: bool = ..., cookie: _Optional[bytes] = ...) -> None: ...

class ReadIndexResult(_message.Message):
    __slots__ = ("entries", "cookie", "disk_version")
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    COOKIE_FIELD_NUMBER: _ClassVar[int]
    DISK_VERSION_FIELD_NUMBER: _ClassVar[int]
    entries: _containers.RepeatedCompositeFieldContainer[MetadataRecord]
    cookie: bytes
    disk_version: int
    def __init__(self, entries: _Optional[_Iterable[_Union[MetadataRecord, _Mapping]]] = ..., cookie: _Optional[bytes] = ..., disk_version: _Optional[int] = ...) -> None: ...

class HydraUsageInfo(_message.Message):
    __slots__ = ("node_id", "disk_id", "is_default_disk", "bridge_constituent_id", "session_id", "sequence_id", "num_active_epochs", "num_active_metadata_epochs", "capacity_bytes", "used_bytes", "metadata_used_bytes", "num_fds", "read_avg_size", "read_avg_oio", "write_avg_size", "write_avg_oio", "healthy")
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    DISK_ID_FIELD_NUMBER: _ClassVar[int]
    IS_DEFAULT_DISK_FIELD_NUMBER: _ClassVar[int]
    BRIDGE_CONSTITUENT_ID_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    SEQUENCE_ID_FIELD_NUMBER: _ClassVar[int]
    NUM_ACTIVE_EPOCHS_FIELD_NUMBER: _ClassVar[int]
    NUM_ACTIVE_METADATA_EPOCHS_FIELD_NUMBER: _ClassVar[int]
    CAPACITY_BYTES_FIELD_NUMBER: _ClassVar[int]
    USED_BYTES_FIELD_NUMBER: _ClassVar[int]
    METADATA_USED_BYTES_FIELD_NUMBER: _ClassVar[int]
    NUM_FDS_FIELD_NUMBER: _ClassVar[int]
    READ_AVG_SIZE_FIELD_NUMBER: _ClassVar[int]
    READ_AVG_OIO_FIELD_NUMBER: _ClassVar[int]
    WRITE_AVG_SIZE_FIELD_NUMBER: _ClassVar[int]
    WRITE_AVG_OIO_FIELD_NUMBER: _ClassVar[int]
    HEALTHY_FIELD_NUMBER: _ClassVar[int]
    node_id: int
    disk_id: int
    is_default_disk: bool
    bridge_constituent_id: int
    session_id: int
    sequence_id: int
    num_active_epochs: int
    num_active_metadata_epochs: int
    capacity_bytes: int
    used_bytes: int
    metadata_used_bytes: int
    num_fds: int
    read_avg_size: int
    read_avg_oio: float
    write_avg_size: int
    write_avg_oio: float
    healthy: bool
    def __init__(self, node_id: _Optional[int] = ..., disk_id: _Optional[int] = ..., is_default_disk: bool = ..., bridge_constituent_id: _Optional[int] = ..., session_id: _Optional[int] = ..., sequence_id: _Optional[int] = ..., num_active_epochs: _Optional[int] = ..., num_active_metadata_epochs: _Optional[int] = ..., capacity_bytes: _Optional[int] = ..., used_bytes: _Optional[int] = ..., metadata_used_bytes: _Optional[int] = ..., num_fds: _Optional[int] = ..., read_avg_size: _Optional[int] = ..., read_avg_oio: _Optional[float] = ..., write_avg_size: _Optional[int] = ..., write_avg_oio: _Optional[float] = ..., healthy: bool = ...) -> None: ...

class ClusterUsageInfo(_message.Message):
    __slots__ = ("node_info",)
    NODE_INFO_FIELD_NUMBER: _ClassVar[int]
    node_info: _containers.RepeatedCompositeFieldContainer[HydraUsageInfo]
    def __init__(self, node_info: _Optional[_Iterable[_Union[HydraUsageInfo, _Mapping]]] = ...) -> None: ...

class GetUsageResult(_message.Message):
    __slots__ = ("cluster_usage",)
    CLUSTER_USAGE_FIELD_NUMBER: _ClassVar[int]
    cluster_usage: ClusterUsageInfo
    def __init__(self, cluster_usage: _Optional[_Union[ClusterUsageInfo, _Mapping]] = ...) -> None: ...

class GetUsageArg(_message.Message):
    __slots__ = ("cluster_usage",)
    CLUSTER_USAGE_FIELD_NUMBER: _ClassVar[int]
    cluster_usage: ClusterUsageInfo
    def __init__(self, cluster_usage: _Optional[_Union[ClusterUsageInfo, _Mapping]] = ...) -> None: ...

class CheckValidEpochArg(_message.Message):
    __slots__ = ("blob_id", "epoch_id")
    BLOB_ID_FIELD_NUMBER: _ClassVar[int]
    EPOCH_ID_FIELD_NUMBER: _ClassVar[int]
    blob_id: int
    epoch_id: int
    def __init__(self, blob_id: _Optional[int] = ..., epoch_id: _Optional[int] = ...) -> None: ...

class CheckValidEpochResult(_message.Message):
    __slots__ = ("validity",)
    class EpochValidity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kValid: _ClassVar[CheckValidEpochResult.EpochValidity]
        kInvalid: _ClassVar[CheckValidEpochResult.EpochValidity]
        kUnknown: _ClassVar[CheckValidEpochResult.EpochValidity]
    kValid: CheckValidEpochResult.EpochValidity
    kInvalid: CheckValidEpochResult.EpochValidity
    kUnknown: CheckValidEpochResult.EpochValidity
    VALIDITY_FIELD_NUMBER: _ClassVar[int]
    validity: CheckValidEpochResult.EpochValidity
    def __init__(self, validity: _Optional[_Union[CheckValidEpochResult.EpochValidity, str]] = ...) -> None: ...

class ReplicateEpochArg(_message.Message):
    __slots__ = ("blob_id", "epoch_id", "src_disk_id", "dst_disk_id", "dst_disk_tier", "check_free_space", "view_box_id", "blur_blob_view_id")
    class DiskTier(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kSSD: _ClassVar[ReplicateEpochArg.DiskTier]
        kHDD: _ClassVar[ReplicateEpochArg.DiskTier]
    kSSD: ReplicateEpochArg.DiskTier
    kHDD: ReplicateEpochArg.DiskTier
    BLOB_ID_FIELD_NUMBER: _ClassVar[int]
    EPOCH_ID_FIELD_NUMBER: _ClassVar[int]
    SRC_DISK_ID_FIELD_NUMBER: _ClassVar[int]
    DST_DISK_ID_FIELD_NUMBER: _ClassVar[int]
    DST_DISK_TIER_FIELD_NUMBER: _ClassVar[int]
    CHECK_FREE_SPACE_FIELD_NUMBER: _ClassVar[int]
    VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
    BLUR_BLOB_VIEW_ID_FIELD_NUMBER: _ClassVar[int]
    blob_id: int
    epoch_id: int
    src_disk_id: int
    dst_disk_id: int
    dst_disk_tier: ReplicateEpochArg.DiskTier
    check_free_space: bool
    view_box_id: int
    blur_blob_view_id: int
    def __init__(self, blob_id: _Optional[int] = ..., epoch_id: _Optional[int] = ..., src_disk_id: _Optional[int] = ..., dst_disk_id: _Optional[int] = ..., dst_disk_tier: _Optional[_Union[ReplicateEpochArg.DiskTier, str]] = ..., check_free_space: bool = ..., view_box_id: _Optional[int] = ..., blur_blob_view_id: _Optional[int] = ...) -> None: ...

class ReplicateEpochResult(_message.Message):
    __slots__ = ("disk_id", "replicated_bytes")
    DISK_ID_FIELD_NUMBER: _ClassVar[int]
    REPLICATED_BYTES_FIELD_NUMBER: _ClassVar[int]
    disk_id: int
    replicated_bytes: int
    def __init__(self, disk_id: _Optional[int] = ..., replicated_bytes: _Optional[int] = ...) -> None: ...
