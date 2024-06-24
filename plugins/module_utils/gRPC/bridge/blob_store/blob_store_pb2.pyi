from bridge.base import cloud_pb2 as _cloud_pb2
from bridge.hydra.base import epoch_pb2 as _epoch_pb2
from bridge.vault.base import vault_pb2 as _vault_pb2
from bridge.vault.base import worm_pb2 as _worm_pb2
from configs import cluster_config_pb2 as _cluster_config_pb2
from keychain.base import keychain_pb2 as _keychain_pb2
from open_util.base import aes_encryptor_pb2 as _aes_encryptor_pb2
from util.base import op_clock_pb2 as _op_clock_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CloudChunkIdProto(_message.Message):
    __slots__ = ("sha1", "local_id", "chunk_len")
    SHA1_FIELD_NUMBER: _ClassVar[int]
    LOCAL_ID_FIELD_NUMBER: _ClassVar[int]
    CHUNK_LEN_FIELD_NUMBER: _ClassVar[int]
    sha1: bytes
    local_id: int
    chunk_len: int
    def __init__(self, sha1: _Optional[bytes] = ..., local_id: _Optional[int] = ..., chunk_len: _Optional[int] = ...) -> None: ...

class CloudChunkLocationProto(_message.Message):
    __slots__ = ("cloud_chunk_id", "cloud_object_id", "lease_id")
    CLOUD_CHUNK_ID_FIELD_NUMBER: _ClassVar[int]
    CLOUD_OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    LEASE_ID_FIELD_NUMBER: _ClassVar[int]
    cloud_chunk_id: CloudChunkIdProto
    cloud_object_id: _cloud_pb2.CloudObjectIdProto
    lease_id: int
    def __init__(self, cloud_chunk_id: _Optional[_Union[CloudChunkIdProto, _Mapping]] = ..., cloud_object_id: _Optional[_Union[_cloud_pb2.CloudObjectIdProto, _Mapping]] = ..., lease_id: _Optional[int] = ...) -> None: ...

class BlobMetadataProto(_message.Message):
    __slots__ = ("opclock_vec", "blob_snap_tree_id", "view_box_id", "blob_immutable", "is_stub_blob", "hydra_epochs", "max_issued_epoch_id", "deleted_timestamp_usecs", "storage_policy_override", "minion_snap_tree_root_id", "update_intent", "node_id_floor", "creation_time_usecs", "brick_size", "blur_blob_view_id", "blur_blob_min_entity_id", "blur_blob_root_inode_id", "blur_entry_reservation", "fixed_dedup_chunk_size")
    class UpdateIntent(_message.Message):
        __slots__ = ("hydra_epochs", "under_replicated_clone_target_epoch_info_vec", "under_replicated_clone_source_epoch_info_vec")
        class EpochInfo(_message.Message):
            __slots__ = ("blob_id", "epoch_id_vec")
            BLOB_ID_FIELD_NUMBER: _ClassVar[int]
            EPOCH_ID_VEC_FIELD_NUMBER: _ClassVar[int]
            blob_id: int
            epoch_id_vec: _containers.RepeatedScalarFieldContainer[int]
            def __init__(self, blob_id: _Optional[int] = ..., epoch_id_vec: _Optional[_Iterable[int]] = ...) -> None: ...
        HYDRA_EPOCHS_FIELD_NUMBER: _ClassVar[int]
        UNDER_REPLICATED_CLONE_TARGET_EPOCH_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
        UNDER_REPLICATED_CLONE_SOURCE_EPOCH_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
        hydra_epochs: _containers.RepeatedCompositeFieldContainer[_epoch_pb2.EpochProto]
        under_replicated_clone_target_epoch_info_vec: _containers.RepeatedCompositeFieldContainer[BlobMetadataProto.UpdateIntent.EpochInfo]
        under_replicated_clone_source_epoch_info_vec: _containers.RepeatedCompositeFieldContainer[BlobMetadataProto.UpdateIntent.EpochInfo]
        def __init__(self, hydra_epochs: _Optional[_Iterable[_Union[_epoch_pb2.EpochProto, _Mapping]]] = ..., under_replicated_clone_target_epoch_info_vec: _Optional[_Iterable[_Union[BlobMetadataProto.UpdateIntent.EpochInfo, _Mapping]]] = ..., under_replicated_clone_source_epoch_info_vec: _Optional[_Iterable[_Union[BlobMetadataProto.UpdateIntent.EpochInfo, _Mapping]]] = ...) -> None: ...
    OPCLOCK_VEC_FIELD_NUMBER: _ClassVar[int]
    BLOB_SNAP_TREE_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
    BLOB_IMMUTABLE_FIELD_NUMBER: _ClassVar[int]
    IS_STUB_BLOB_FIELD_NUMBER: _ClassVar[int]
    HYDRA_EPOCHS_FIELD_NUMBER: _ClassVar[int]
    MAX_ISSUED_EPOCH_ID_FIELD_NUMBER: _ClassVar[int]
    DELETED_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
    STORAGE_POLICY_OVERRIDE_FIELD_NUMBER: _ClassVar[int]
    MINION_SNAP_TREE_ROOT_ID_FIELD_NUMBER: _ClassVar[int]
    UPDATE_INTENT_FIELD_NUMBER: _ClassVar[int]
    NODE_ID_FLOOR_FIELD_NUMBER: _ClassVar[int]
    CREATION_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    BRICK_SIZE_FIELD_NUMBER: _ClassVar[int]
    BLUR_BLOB_VIEW_ID_FIELD_NUMBER: _ClassVar[int]
    BLUR_BLOB_MIN_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    BLUR_BLOB_ROOT_INODE_ID_FIELD_NUMBER: _ClassVar[int]
    BLUR_ENTRY_RESERVATION_FIELD_NUMBER: _ClassVar[int]
    FIXED_DEDUP_CHUNK_SIZE_FIELD_NUMBER: _ClassVar[int]
    opclock_vec: _containers.RepeatedCompositeFieldContainer[_op_clock_pb2.OpClock]
    blob_snap_tree_id: int
    view_box_id: int
    blob_immutable: bool
    is_stub_blob: bool
    hydra_epochs: _containers.RepeatedCompositeFieldContainer[_epoch_pb2.EpochProto]
    max_issued_epoch_id: int
    deleted_timestamp_usecs: int
    storage_policy_override: _cluster_config_pb2.ClusterConfigProto.StoragePolicyOverride
    minion_snap_tree_root_id: int
    update_intent: BlobMetadataProto.UpdateIntent
    node_id_floor: int
    creation_time_usecs: int
    brick_size: int
    blur_blob_view_id: int
    blur_blob_min_entity_id: int
    blur_blob_root_inode_id: int
    blur_entry_reservation: int
    fixed_dedup_chunk_size: int
    def __init__(self, opclock_vec: _Optional[_Iterable[_Union[_op_clock_pb2.OpClock, _Mapping]]] = ..., blob_snap_tree_id: _Optional[int] = ..., view_box_id: _Optional[int] = ..., blob_immutable: bool = ..., is_stub_blob: bool = ..., hydra_epochs: _Optional[_Iterable[_Union[_epoch_pb2.EpochProto, _Mapping]]] = ..., max_issued_epoch_id: _Optional[int] = ..., deleted_timestamp_usecs: _Optional[int] = ..., storage_policy_override: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.StoragePolicyOverride, _Mapping]] = ..., minion_snap_tree_root_id: _Optional[int] = ..., update_intent: _Optional[_Union[BlobMetadataProto.UpdateIntent, _Mapping]] = ..., node_id_floor: _Optional[int] = ..., creation_time_usecs: _Optional[int] = ..., brick_size: _Optional[int] = ..., blur_blob_view_id: _Optional[int] = ..., blur_blob_min_entity_id: _Optional[int] = ..., blur_blob_root_inode_id: _Optional[int] = ..., blur_entry_reservation: _Optional[int] = ..., fixed_dedup_chunk_size: _Optional[int] = ...) -> None: ...

class ChunkIdProto(_message.Message):
    __slots__ = ("owner_id", "chunk_len", "dedup", "non_dedup")
    class Dedup(_message.Message):
        __slots__ = ("sha1",)
        SHA1_FIELD_NUMBER: _ClassVar[int]
        sha1: bytes
        def __init__(self, sha1: _Optional[bytes] = ...) -> None: ...
    class NonDedup(_message.Message):
        __slots__ = ("blob_offset", "incarnation")
        BLOB_OFFSET_FIELD_NUMBER: _ClassVar[int]
        INCARNATION_FIELD_NUMBER: _ClassVar[int]
        blob_offset: int
        incarnation: int
        def __init__(self, blob_offset: _Optional[int] = ..., incarnation: _Optional[int] = ...) -> None: ...
    OWNER_ID_FIELD_NUMBER: _ClassVar[int]
    CHUNK_LEN_FIELD_NUMBER: _ClassVar[int]
    DEDUP_FIELD_NUMBER: _ClassVar[int]
    NON_DEDUP_FIELD_NUMBER: _ClassVar[int]
    owner_id: int
    chunk_len: int
    dedup: ChunkIdProto.Dedup
    non_dedup: ChunkIdProto.NonDedup
    def __init__(self, owner_id: _Optional[int] = ..., chunk_len: _Optional[int] = ..., dedup: _Optional[_Union[ChunkIdProto.Dedup, _Mapping]] = ..., non_dedup: _Optional[_Union[ChunkIdProto.NonDedup, _Mapping]] = ...) -> None: ...

class ChunkFileContainerMetadataProto(_message.Message):
    __slots__ = ("view_box_id", "opclock_vec", "data_chunk_file_id_vec", "coded_chunk_file_id_vec", "chunk_file_disk_vec", "max_chunk_file_size", "ec_algo", "update_intent", "intent_id_generator", "coded_chunkgroup_vec", "has_dedup_chunks")
    class ECAlgoInfo(_message.Message):
        __slots__ = ("algo", "num_data_stripes", "num_coded_stripes")
        class Algorithm(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kReedSolomon: _ClassVar[ChunkFileContainerMetadataProto.ECAlgoInfo.Algorithm]
            kLRC: _ClassVar[ChunkFileContainerMetadataProto.ECAlgoInfo.Algorithm]
        kReedSolomon: ChunkFileContainerMetadataProto.ECAlgoInfo.Algorithm
        kLRC: ChunkFileContainerMetadataProto.ECAlgoInfo.Algorithm
        ALGO_FIELD_NUMBER: _ClassVar[int]
        NUM_DATA_STRIPES_FIELD_NUMBER: _ClassVar[int]
        NUM_CODED_STRIPES_FIELD_NUMBER: _ClassVar[int]
        algo: ChunkFileContainerMetadataProto.ECAlgoInfo.Algorithm
        num_data_stripes: int
        num_coded_stripes: int
        def __init__(self, algo: _Optional[_Union[ChunkFileContainerMetadataProto.ECAlgoInfo.Algorithm, str]] = ..., num_data_stripes: _Optional[int] = ..., num_coded_stripes: _Optional[int] = ...) -> None: ...
    class UpdateIntent(_message.Message):
        __slots__ = ("intent_id", "coding", "rebuild")
        class CodingIntent(_message.Message):
            __slots__ = ("data_chunk_file_id_vec", "coded_chunk_file_id_vec")
            DATA_CHUNK_FILE_ID_VEC_FIELD_NUMBER: _ClassVar[int]
            CODED_CHUNK_FILE_ID_VEC_FIELD_NUMBER: _ClassVar[int]
            data_chunk_file_id_vec: _containers.RepeatedScalarFieldContainer[int]
            coded_chunk_file_id_vec: _containers.RepeatedScalarFieldContainer[int]
            def __init__(self, data_chunk_file_id_vec: _Optional[_Iterable[int]] = ..., coded_chunk_file_id_vec: _Optional[_Iterable[int]] = ...) -> None: ...
        class RebuildIntent(_message.Message):
            __slots__ = ("stripe_disk_vec",)
            class RebuildMethod(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                kClone: _ClassVar[ChunkFileContainerMetadataProto.UpdateIntent.RebuildIntent.RebuildMethod]
                kRebuild: _ClassVar[ChunkFileContainerMetadataProto.UpdateIntent.RebuildIntent.RebuildMethod]
            kClone: ChunkFileContainerMetadataProto.UpdateIntent.RebuildIntent.RebuildMethod
            kRebuild: ChunkFileContainerMetadataProto.UpdateIntent.RebuildIntent.RebuildMethod
            class StripeDisk(_message.Message):
                __slots__ = ("index", "dest_disk_id", "rebuild_method")
                INDEX_FIELD_NUMBER: _ClassVar[int]
                DEST_DISK_ID_FIELD_NUMBER: _ClassVar[int]
                REBUILD_METHOD_FIELD_NUMBER: _ClassVar[int]
                index: int
                dest_disk_id: int
                rebuild_method: ChunkFileContainerMetadataProto.UpdateIntent.RebuildIntent.RebuildMethod
                def __init__(self, index: _Optional[int] = ..., dest_disk_id: _Optional[int] = ..., rebuild_method: _Optional[_Union[ChunkFileContainerMetadataProto.UpdateIntent.RebuildIntent.RebuildMethod, str]] = ...) -> None: ...
            STRIPE_DISK_VEC_FIELD_NUMBER: _ClassVar[int]
            stripe_disk_vec: _containers.RepeatedCompositeFieldContainer[ChunkFileContainerMetadataProto.UpdateIntent.RebuildIntent.StripeDisk]
            def __init__(self, stripe_disk_vec: _Optional[_Iterable[_Union[ChunkFileContainerMetadataProto.UpdateIntent.RebuildIntent.StripeDisk, _Mapping]]] = ...) -> None: ...
        INTENT_ID_FIELD_NUMBER: _ClassVar[int]
        CODING_FIELD_NUMBER: _ClassVar[int]
        REBUILD_FIELD_NUMBER: _ClassVar[int]
        intent_id: int
        coding: ChunkFileContainerMetadataProto.UpdateIntent.CodingIntent
        rebuild: ChunkFileContainerMetadataProto.UpdateIntent.RebuildIntent
        def __init__(self, intent_id: _Optional[int] = ..., coding: _Optional[_Union[ChunkFileContainerMetadataProto.UpdateIntent.CodingIntent, _Mapping]] = ..., rebuild: _Optional[_Union[ChunkFileContainerMetadataProto.UpdateIntent.RebuildIntent, _Mapping]] = ...) -> None: ...
    class CodedChunkGroup(_message.Message):
        __slots__ = ("offset", "size", "stripe_ec_info_vec")
        class StripeECInfo(_message.Message):
            __slots__ = ("chunk_file_physical_ranges_vec",)
            class ChunkFilePhysicalRange(_message.Message):
                __slots__ = ("data_stripe_offset", "data_stripe_length", "adler32_cksum")
                DATA_STRIPE_OFFSET_FIELD_NUMBER: _ClassVar[int]
                DATA_STRIPE_LENGTH_FIELD_NUMBER: _ClassVar[int]
                ADLER32_CKSUM_FIELD_NUMBER: _ClassVar[int]
                data_stripe_offset: int
                data_stripe_length: int
                adler32_cksum: int
                def __init__(self, data_stripe_offset: _Optional[int] = ..., data_stripe_length: _Optional[int] = ..., adler32_cksum: _Optional[int] = ...) -> None: ...
            CHUNK_FILE_PHYSICAL_RANGES_VEC_FIELD_NUMBER: _ClassVar[int]
            chunk_file_physical_ranges_vec: _containers.RepeatedCompositeFieldContainer[ChunkFileContainerMetadataProto.CodedChunkGroup.StripeECInfo.ChunkFilePhysicalRange]
            def __init__(self, chunk_file_physical_ranges_vec: _Optional[_Iterable[_Union[ChunkFileContainerMetadataProto.CodedChunkGroup.StripeECInfo.ChunkFilePhysicalRange, _Mapping]]] = ...) -> None: ...
        OFFSET_FIELD_NUMBER: _ClassVar[int]
        SIZE_FIELD_NUMBER: _ClassVar[int]
        STRIPE_EC_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
        offset: int
        size: int
        stripe_ec_info_vec: _containers.RepeatedCompositeFieldContainer[ChunkFileContainerMetadataProto.CodedChunkGroup.StripeECInfo]
        def __init__(self, offset: _Optional[int] = ..., size: _Optional[int] = ..., stripe_ec_info_vec: _Optional[_Iterable[_Union[ChunkFileContainerMetadataProto.CodedChunkGroup.StripeECInfo, _Mapping]]] = ...) -> None: ...
    VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
    OPCLOCK_VEC_FIELD_NUMBER: _ClassVar[int]
    DATA_CHUNK_FILE_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    CODED_CHUNK_FILE_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    CHUNK_FILE_DISK_VEC_FIELD_NUMBER: _ClassVar[int]
    MAX_CHUNK_FILE_SIZE_FIELD_NUMBER: _ClassVar[int]
    EC_ALGO_FIELD_NUMBER: _ClassVar[int]
    UPDATE_INTENT_FIELD_NUMBER: _ClassVar[int]
    INTENT_ID_GENERATOR_FIELD_NUMBER: _ClassVar[int]
    CODED_CHUNKGROUP_VEC_FIELD_NUMBER: _ClassVar[int]
    HAS_DEDUP_CHUNKS_FIELD_NUMBER: _ClassVar[int]
    view_box_id: int
    opclock_vec: _containers.RepeatedCompositeFieldContainer[_op_clock_pb2.OpClock]
    data_chunk_file_id_vec: _containers.RepeatedScalarFieldContainer[int]
    coded_chunk_file_id_vec: _containers.RepeatedScalarFieldContainer[int]
    chunk_file_disk_vec: _containers.RepeatedScalarFieldContainer[int]
    max_chunk_file_size: int
    ec_algo: ChunkFileContainerMetadataProto.ECAlgoInfo
    update_intent: ChunkFileContainerMetadataProto.UpdateIntent
    intent_id_generator: int
    coded_chunkgroup_vec: _containers.RepeatedCompositeFieldContainer[ChunkFileContainerMetadataProto.CodedChunkGroup]
    has_dedup_chunks: bool
    def __init__(self, view_box_id: _Optional[int] = ..., opclock_vec: _Optional[_Iterable[_Union[_op_clock_pb2.OpClock, _Mapping]]] = ..., data_chunk_file_id_vec: _Optional[_Iterable[int]] = ..., coded_chunk_file_id_vec: _Optional[_Iterable[int]] = ..., chunk_file_disk_vec: _Optional[_Iterable[int]] = ..., max_chunk_file_size: _Optional[int] = ..., ec_algo: _Optional[_Union[ChunkFileContainerMetadataProto.ECAlgoInfo, _Mapping]] = ..., update_intent: _Optional[_Union[ChunkFileContainerMetadataProto.UpdateIntent, _Mapping]] = ..., intent_id_generator: _Optional[int] = ..., coded_chunkgroup_vec: _Optional[_Iterable[_Union[ChunkFileContainerMetadataProto.CodedChunkGroup, _Mapping]]] = ..., has_dedup_chunks: bool = ...) -> None: ...

class BrickMetadataProto(_message.Message):
    __slots__ = ("opclock_vec", "last_mutation_time_usecs", "last_morph_time_usecs", "owner_blob_id", "snap_tree_leaf_node_id", "stats_container_id", "view_box_id", "extent_vec", "chunk_id_vec", "dedup_override_view_id", "brick_sha1")
    class Extent(_message.Message):
        __slots__ = ("chunk_id", "chunk_id_vec_index", "chunk_offset", "chunk_file_id", "brick_offset", "extent_length", "cloud_location_vec")
        CHUNK_ID_FIELD_NUMBER: _ClassVar[int]
        CHUNK_ID_VEC_INDEX_FIELD_NUMBER: _ClassVar[int]
        CHUNK_OFFSET_FIELD_NUMBER: _ClassVar[int]
        CHUNK_FILE_ID_FIELD_NUMBER: _ClassVar[int]
        BRICK_OFFSET_FIELD_NUMBER: _ClassVar[int]
        EXTENT_LENGTH_FIELD_NUMBER: _ClassVar[int]
        CLOUD_LOCATION_VEC_FIELD_NUMBER: _ClassVar[int]
        chunk_id: ChunkIdProto
        chunk_id_vec_index: int
        chunk_offset: int
        chunk_file_id: int
        brick_offset: int
        extent_length: int
        cloud_location_vec: _containers.RepeatedCompositeFieldContainer[CloudChunkLocationProto]
        def __init__(self, chunk_id: _Optional[_Union[ChunkIdProto, _Mapping]] = ..., chunk_id_vec_index: _Optional[int] = ..., chunk_offset: _Optional[int] = ..., chunk_file_id: _Optional[int] = ..., brick_offset: _Optional[int] = ..., extent_length: _Optional[int] = ..., cloud_location_vec: _Optional[_Iterable[_Union[CloudChunkLocationProto, _Mapping]]] = ...) -> None: ...
    class BrickSha1(_message.Message):
        __slots__ = ("sha1",)
        SHA1_FIELD_NUMBER: _ClassVar[int]
        sha1: bytes
        def __init__(self, sha1: _Optional[bytes] = ...) -> None: ...
    OPCLOCK_VEC_FIELD_NUMBER: _ClassVar[int]
    LAST_MUTATION_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    LAST_MORPH_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    OWNER_BLOB_ID_FIELD_NUMBER: _ClassVar[int]
    SNAP_TREE_LEAF_NODE_ID_FIELD_NUMBER: _ClassVar[int]
    STATS_CONTAINER_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
    EXTENT_VEC_FIELD_NUMBER: _ClassVar[int]
    CHUNK_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    DEDUP_OVERRIDE_VIEW_ID_FIELD_NUMBER: _ClassVar[int]
    BRICK_SHA1_FIELD_NUMBER: _ClassVar[int]
    opclock_vec: _containers.RepeatedCompositeFieldContainer[_op_clock_pb2.OpClock]
    last_mutation_time_usecs: int
    last_morph_time_usecs: int
    owner_blob_id: int
    snap_tree_leaf_node_id: int
    stats_container_id: int
    view_box_id: int
    extent_vec: _containers.RepeatedCompositeFieldContainer[BrickMetadataProto.Extent]
    chunk_id_vec: _containers.RepeatedCompositeFieldContainer[ChunkIdProto]
    dedup_override_view_id: int
    brick_sha1: BrickMetadataProto.BrickSha1
    def __init__(self, opclock_vec: _Optional[_Iterable[_Union[_op_clock_pb2.OpClock, _Mapping]]] = ..., last_mutation_time_usecs: _Optional[int] = ..., last_morph_time_usecs: _Optional[int] = ..., owner_blob_id: _Optional[int] = ..., snap_tree_leaf_node_id: _Optional[int] = ..., stats_container_id: _Optional[int] = ..., view_box_id: _Optional[int] = ..., extent_vec: _Optional[_Iterable[_Union[BrickMetadataProto.Extent, _Mapping]]] = ..., chunk_id_vec: _Optional[_Iterable[_Union[ChunkIdProto, _Mapping]]] = ..., dedup_override_view_id: _Optional[int] = ..., brick_sha1: _Optional[_Union[BrickMetadataProto.BrickSha1, _Mapping]] = ...) -> None: ...

class ChunkMetadataProto(_message.Message):
    __slots__ = ("opclock_vec", "chunk_file_id", "cloud_location_vec", "first_brick_leaf_node_id")
    OPCLOCK_VEC_FIELD_NUMBER: _ClassVar[int]
    CHUNK_FILE_ID_FIELD_NUMBER: _ClassVar[int]
    CLOUD_LOCATION_VEC_FIELD_NUMBER: _ClassVar[int]
    FIRST_BRICK_LEAF_NODE_ID_FIELD_NUMBER: _ClassVar[int]
    opclock_vec: _containers.RepeatedCompositeFieldContainer[_op_clock_pb2.OpClock]
    chunk_file_id: int
    cloud_location_vec: _containers.RepeatedCompositeFieldContainer[CloudChunkLocationProto]
    first_brick_leaf_node_id: int
    def __init__(self, opclock_vec: _Optional[_Iterable[_Union[_op_clock_pb2.OpClock, _Mapping]]] = ..., chunk_file_id: _Optional[int] = ..., cloud_location_vec: _Optional[_Iterable[_Union[CloudChunkLocationProto, _Mapping]]] = ..., first_brick_leaf_node_id: _Optional[int] = ...) -> None: ...

class ChunkFileMetadataProto(_message.Message):
    __slots__ = ()
    class UpdateIntent(_message.Message):
        __slots__ = ("intent_id", "add_or_update_chunks", "delete_chunks", "move_chunk_mapping", "clone_replica", "ec_add_chunks", "shuffle_replica", "coding_intent")
        class AddOrUpdateChunks(_message.Message):
            __slots__ = ("chunk_id_vec", "snap_tree_leaf_node_id_vec")
            CHUNK_ID_VEC_FIELD_NUMBER: _ClassVar[int]
            SNAP_TREE_LEAF_NODE_ID_VEC_FIELD_NUMBER: _ClassVar[int]
            chunk_id_vec: _containers.RepeatedCompositeFieldContainer[ChunkIdProto]
            snap_tree_leaf_node_id_vec: _containers.RepeatedScalarFieldContainer[int]
            def __init__(self, chunk_id_vec: _Optional[_Iterable[_Union[ChunkIdProto, _Mapping]]] = ..., snap_tree_leaf_node_id_vec: _Optional[_Iterable[int]] = ...) -> None: ...
        class DeleteChunks(_message.Message):
            __slots__ = ("chunk_id_vec",)
            CHUNK_ID_VEC_FIELD_NUMBER: _ClassVar[int]
            chunk_id_vec: _containers.RepeatedCompositeFieldContainer[ChunkIdProto]
            def __init__(self, chunk_id_vec: _Optional[_Iterable[_Union[ChunkIdProto, _Mapping]]] = ...) -> None: ...
        class MoveChunkMapping(_message.Message):
            __slots__ = ("chunk_id_vec",)
            CHUNK_ID_VEC_FIELD_NUMBER: _ClassVar[int]
            chunk_id_vec: _containers.RepeatedCompositeFieldContainer[ChunkIdProto]
            def __init__(self, chunk_id_vec: _Optional[_Iterable[_Union[ChunkIdProto, _Mapping]]] = ...) -> None: ...
        class CloneReplica(_message.Message):
            __slots__ = ("source_disk_id",)
            SOURCE_DISK_ID_FIELD_NUMBER: _ClassVar[int]
            source_disk_id: int
            def __init__(self, source_disk_id: _Optional[int] = ...) -> None: ...
        class ECAddChunks(_message.Message):
            __slots__ = ("chunk_id_vec", "chunk_column_vec", "chunkgroup_column_vec", "chunkgroup_id_vec", "committed")
            CHUNK_ID_VEC_FIELD_NUMBER: _ClassVar[int]
            CHUNK_COLUMN_VEC_FIELD_NUMBER: _ClassVar[int]
            CHUNKGROUP_COLUMN_VEC_FIELD_NUMBER: _ClassVar[int]
            CHUNKGROUP_ID_VEC_FIELD_NUMBER: _ClassVar[int]
            COMMITTED_FIELD_NUMBER: _ClassVar[int]
            chunk_id_vec: _containers.RepeatedCompositeFieldContainer[ChunkIdProto]
            chunk_column_vec: _containers.RepeatedCompositeFieldContainer[ChunkFileMetadataProto.ChunkColumn]
            chunkgroup_column_vec: _containers.RepeatedCompositeFieldContainer[ChunkFileMetadataProto.ChunkGroupColumn]
            chunkgroup_id_vec: _containers.RepeatedScalarFieldContainer[int]
            committed: bool
            def __init__(self, chunk_id_vec: _Optional[_Iterable[_Union[ChunkIdProto, _Mapping]]] = ..., chunk_column_vec: _Optional[_Iterable[_Union[ChunkFileMetadataProto.ChunkColumn, _Mapping]]] = ..., chunkgroup_column_vec: _Optional[_Iterable[_Union[ChunkFileMetadataProto.ChunkGroupColumn, _Mapping]]] = ..., chunkgroup_id_vec: _Optional[_Iterable[int]] = ..., committed: bool = ...) -> None: ...
        class ShuffleReplica(_message.Message):
            __slots__ = ("dest_disk_id", "method")
            class ShuffleMethod(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                CLONE: _ClassVar[ChunkFileMetadataProto.UpdateIntent.ShuffleReplica.ShuffleMethod]
                REBUILD: _ClassVar[ChunkFileMetadataProto.UpdateIntent.ShuffleReplica.ShuffleMethod]
            CLONE: ChunkFileMetadataProto.UpdateIntent.ShuffleReplica.ShuffleMethod
            REBUILD: ChunkFileMetadataProto.UpdateIntent.ShuffleReplica.ShuffleMethod
            DEST_DISK_ID_FIELD_NUMBER: _ClassVar[int]
            METHOD_FIELD_NUMBER: _ClassVar[int]
            dest_disk_id: int
            method: ChunkFileMetadataProto.UpdateIntent.ShuffleReplica.ShuffleMethod
            def __init__(self, dest_disk_id: _Optional[int] = ..., method: _Optional[_Union[ChunkFileMetadataProto.UpdateIntent.ShuffleReplica.ShuffleMethod, str]] = ...) -> None: ...
        class CodingIntent(_message.Message):
            __slots__ = ("chunk_file_container_id", "is_coded_chunk_file", "disk_id", "ec_container_info")
            CHUNK_FILE_CONTAINER_ID_FIELD_NUMBER: _ClassVar[int]
            IS_CODED_CHUNK_FILE_FIELD_NUMBER: _ClassVar[int]
            DISK_ID_FIELD_NUMBER: _ClassVar[int]
            EC_CONTAINER_INFO_FIELD_NUMBER: _ClassVar[int]
            chunk_file_container_id: int
            is_coded_chunk_file: bool
            disk_id: int
            ec_container_info: ChunkFileContainerMetadataProto.ECAlgoInfo
            def __init__(self, chunk_file_container_id: _Optional[int] = ..., is_coded_chunk_file: bool = ..., disk_id: _Optional[int] = ..., ec_container_info: _Optional[_Union[ChunkFileContainerMetadataProto.ECAlgoInfo, _Mapping]] = ...) -> None: ...
        INTENT_ID_FIELD_NUMBER: _ClassVar[int]
        ADD_OR_UPDATE_CHUNKS_FIELD_NUMBER: _ClassVar[int]
        DELETE_CHUNKS_FIELD_NUMBER: _ClassVar[int]
        MOVE_CHUNK_MAPPING_FIELD_NUMBER: _ClassVar[int]
        CLONE_REPLICA_FIELD_NUMBER: _ClassVar[int]
        EC_ADD_CHUNKS_FIELD_NUMBER: _ClassVar[int]
        SHUFFLE_REPLICA_FIELD_NUMBER: _ClassVar[int]
        CODING_INTENT_FIELD_NUMBER: _ClassVar[int]
        intent_id: int
        add_or_update_chunks: ChunkFileMetadataProto.UpdateIntent.AddOrUpdateChunks
        delete_chunks: ChunkFileMetadataProto.UpdateIntent.DeleteChunks
        move_chunk_mapping: ChunkFileMetadataProto.UpdateIntent.MoveChunkMapping
        clone_replica: ChunkFileMetadataProto.UpdateIntent.CloneReplica
        ec_add_chunks: ChunkFileMetadataProto.UpdateIntent.ECAddChunks
        shuffle_replica: ChunkFileMetadataProto.UpdateIntent.ShuffleReplica
        coding_intent: ChunkFileMetadataProto.UpdateIntent.CodingIntent
        def __init__(self, intent_id: _Optional[int] = ..., add_or_update_chunks: _Optional[_Union[ChunkFileMetadataProto.UpdateIntent.AddOrUpdateChunks, _Mapping]] = ..., delete_chunks: _Optional[_Union[ChunkFileMetadataProto.UpdateIntent.DeleteChunks, _Mapping]] = ..., move_chunk_mapping: _Optional[_Union[ChunkFileMetadataProto.UpdateIntent.MoveChunkMapping, _Mapping]] = ..., clone_replica: _Optional[_Union[ChunkFileMetadataProto.UpdateIntent.CloneReplica, _Mapping]] = ..., ec_add_chunks: _Optional[_Union[ChunkFileMetadataProto.UpdateIntent.ECAddChunks, _Mapping]] = ..., shuffle_replica: _Optional[_Union[ChunkFileMetadataProto.UpdateIntent.ShuffleReplica, _Mapping]] = ..., coding_intent: _Optional[_Union[ChunkFileMetadataProto.UpdateIntent.CodingIntent, _Mapping]] = ...) -> None: ...
    class UpdateIntentHistoryRecord(_message.Message):
        __slots__ = ("disk_id", "creation_time_usecs", "update_intent")
        DISK_ID_FIELD_NUMBER: _ClassVar[int]
        CREATION_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
        UPDATE_INTENT_FIELD_NUMBER: _ClassVar[int]
        disk_id: int
        creation_time_usecs: int
        update_intent: ChunkFileMetadataProto.UpdateIntent
        def __init__(self, disk_id: _Optional[int] = ..., creation_time_usecs: _Optional[int] = ..., update_intent: _Optional[_Union[ChunkFileMetadataProto.UpdateIntent, _Mapping]] = ...) -> None: ...
    class Replica(_message.Message):
        __slots__ = ("disk_id", "update_intent_vec", "version", "next_write_offset", "changed_chunk_vec", "changed_chunkgroup_vec", "error_info")
        class ChangedChunk(_message.Message):
            __slots__ = ("chunk_id", "chunk_column")
            CHUNK_ID_FIELD_NUMBER: _ClassVar[int]
            CHUNK_COLUMN_FIELD_NUMBER: _ClassVar[int]
            chunk_id: ChunkIdProto
            chunk_column: ChunkFileMetadataProto.ChunkColumn
            def __init__(self, chunk_id: _Optional[_Union[ChunkIdProto, _Mapping]] = ..., chunk_column: _Optional[_Union[ChunkFileMetadataProto.ChunkColumn, _Mapping]] = ...) -> None: ...
        class ChangedChunkGroup(_message.Message):
            __slots__ = ("chunkgroup_id", "chunkgroup_column")
            CHUNKGROUP_ID_FIELD_NUMBER: _ClassVar[int]
            CHUNKGROUP_COLUMN_FIELD_NUMBER: _ClassVar[int]
            chunkgroup_id: int
            chunkgroup_column: ChunkFileMetadataProto.ChunkGroupColumn
            def __init__(self, chunkgroup_id: _Optional[int] = ..., chunkgroup_column: _Optional[_Union[ChunkFileMetadataProto.ChunkGroupColumn, _Mapping]] = ...) -> None: ...
        class ErrorInfo(_message.Message):
            __slots__ = ("reason", "time_stamp_usecs")
            class Reason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                kUnknown: _ClassVar[ChunkFileMetadataProto.Replica.ErrorInfo.Reason]
                kDiskMissing: _ClassVar[ChunkFileMetadataProto.Replica.ErrorInfo.Reason]
                kNonExistent: _ClassVar[ChunkFileMetadataProto.Replica.ErrorInfo.Reason]
                kCorrupted: _ClassVar[ChunkFileMetadataProto.Replica.ErrorInfo.Reason]
                kVersionGoneBack: _ClassVar[ChunkFileMetadataProto.Replica.ErrorInfo.Reason]
                kCloneVersionMismatch: _ClassVar[ChunkFileMetadataProto.Replica.ErrorInfo.Reason]
            kUnknown: ChunkFileMetadataProto.Replica.ErrorInfo.Reason
            kDiskMissing: ChunkFileMetadataProto.Replica.ErrorInfo.Reason
            kNonExistent: ChunkFileMetadataProto.Replica.ErrorInfo.Reason
            kCorrupted: ChunkFileMetadataProto.Replica.ErrorInfo.Reason
            kVersionGoneBack: ChunkFileMetadataProto.Replica.ErrorInfo.Reason
            kCloneVersionMismatch: ChunkFileMetadataProto.Replica.ErrorInfo.Reason
            REASON_FIELD_NUMBER: _ClassVar[int]
            TIME_STAMP_USECS_FIELD_NUMBER: _ClassVar[int]
            reason: ChunkFileMetadataProto.Replica.ErrorInfo.Reason
            time_stamp_usecs: int
            def __init__(self, reason: _Optional[_Union[ChunkFileMetadataProto.Replica.ErrorInfo.Reason, str]] = ..., time_stamp_usecs: _Optional[int] = ...) -> None: ...
        DISK_ID_FIELD_NUMBER: _ClassVar[int]
        UPDATE_INTENT_VEC_FIELD_NUMBER: _ClassVar[int]
        VERSION_FIELD_NUMBER: _ClassVar[int]
        NEXT_WRITE_OFFSET_FIELD_NUMBER: _ClassVar[int]
        CHANGED_CHUNK_VEC_FIELD_NUMBER: _ClassVar[int]
        CHANGED_CHUNKGROUP_VEC_FIELD_NUMBER: _ClassVar[int]
        ERROR_INFO_FIELD_NUMBER: _ClassVar[int]
        disk_id: int
        update_intent_vec: _containers.RepeatedCompositeFieldContainer[ChunkFileMetadataProto.UpdateIntent]
        version: int
        next_write_offset: int
        changed_chunk_vec: _containers.RepeatedCompositeFieldContainer[ChunkFileMetadataProto.Replica.ChangedChunk]
        changed_chunkgroup_vec: _containers.RepeatedCompositeFieldContainer[ChunkFileMetadataProto.Replica.ChangedChunkGroup]
        error_info: ChunkFileMetadataProto.Replica.ErrorInfo
        def __init__(self, disk_id: _Optional[int] = ..., update_intent_vec: _Optional[_Iterable[_Union[ChunkFileMetadataProto.UpdateIntent, _Mapping]]] = ..., version: _Optional[int] = ..., next_write_offset: _Optional[int] = ..., changed_chunk_vec: _Optional[_Iterable[_Union[ChunkFileMetadataProto.Replica.ChangedChunk, _Mapping]]] = ..., changed_chunkgroup_vec: _Optional[_Iterable[_Union[ChunkFileMetadataProto.Replica.ChangedChunkGroup, _Mapping]]] = ..., error_info: _Optional[_Union[ChunkFileMetadataProto.Replica.ErrorInfo, _Mapping]] = ...) -> None: ...
    class MasterColumn(_message.Message):
        __slots__ = ("opclock_vec", "chunk_count", "chunkgroup_count", "owner_blob_id", "owner_view_box_id", "compression_level", "encryption_level", "last_waterfall_time_usecs", "intent_id_generator", "update_intent", "replica_vec", "update_intent_session_id", "version", "morphed_size_hint", "finalize_existing_io_update_intents", "last_update_time_usecs", "ec_container_info", "ec_info", "next_avail_stripe_row", "next_avail_chunkgroup_id", "has_dedup_chunks", "chunk_file_container_id", "is_coded_chunk_file", "cloud_domain_id_vec", "edek_info", "encryption_mode", "update_intent_history_record_vec")
        OPCLOCK_VEC_FIELD_NUMBER: _ClassVar[int]
        CHUNK_COUNT_FIELD_NUMBER: _ClassVar[int]
        CHUNKGROUP_COUNT_FIELD_NUMBER: _ClassVar[int]
        OWNER_BLOB_ID_FIELD_NUMBER: _ClassVar[int]
        OWNER_VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
        COMPRESSION_LEVEL_FIELD_NUMBER: _ClassVar[int]
        ENCRYPTION_LEVEL_FIELD_NUMBER: _ClassVar[int]
        LAST_WATERFALL_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
        INTENT_ID_GENERATOR_FIELD_NUMBER: _ClassVar[int]
        UPDATE_INTENT_FIELD_NUMBER: _ClassVar[int]
        REPLICA_VEC_FIELD_NUMBER: _ClassVar[int]
        UPDATE_INTENT_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
        VERSION_FIELD_NUMBER: _ClassVar[int]
        MORPHED_SIZE_HINT_FIELD_NUMBER: _ClassVar[int]
        FINALIZE_EXISTING_IO_UPDATE_INTENTS_FIELD_NUMBER: _ClassVar[int]
        LAST_UPDATE_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
        EC_CONTAINER_INFO_FIELD_NUMBER: _ClassVar[int]
        EC_INFO_FIELD_NUMBER: _ClassVar[int]
        NEXT_AVAIL_STRIPE_ROW_FIELD_NUMBER: _ClassVar[int]
        NEXT_AVAIL_CHUNKGROUP_ID_FIELD_NUMBER: _ClassVar[int]
        HAS_DEDUP_CHUNKS_FIELD_NUMBER: _ClassVar[int]
        CHUNK_FILE_CONTAINER_ID_FIELD_NUMBER: _ClassVar[int]
        IS_CODED_CHUNK_FILE_FIELD_NUMBER: _ClassVar[int]
        CLOUD_DOMAIN_ID_VEC_FIELD_NUMBER: _ClassVar[int]
        EDEK_INFO_FIELD_NUMBER: _ClassVar[int]
        ENCRYPTION_MODE_FIELD_NUMBER: _ClassVar[int]
        UPDATE_INTENT_HISTORY_RECORD_VEC_FIELD_NUMBER: _ClassVar[int]
        opclock_vec: _containers.RepeatedCompositeFieldContainer[_op_clock_pb2.OpClock]
        chunk_count: int
        chunkgroup_count: int
        owner_blob_id: int
        owner_view_box_id: int
        compression_level: _cluster_config_pb2.ClusterConfigProto.StoragePolicy.CompressionLevel
        encryption_level: _cluster_config_pb2.ClusterConfigProto.EncryptionLevel
        last_waterfall_time_usecs: int
        intent_id_generator: int
        update_intent: ChunkFileMetadataProto.UpdateIntent
        replica_vec: _containers.RepeatedCompositeFieldContainer[ChunkFileMetadataProto.Replica]
        update_intent_session_id: int
        version: int
        morphed_size_hint: int
        finalize_existing_io_update_intents: bool
        last_update_time_usecs: int
        ec_container_info: ChunkFileContainerMetadataProto.ECAlgoInfo
        ec_info: _cluster_config_pb2.ClusterConfigProto.StoragePolicy.ECInfo
        next_avail_stripe_row: int
        next_avail_chunkgroup_id: int
        has_dedup_chunks: bool
        chunk_file_container_id: int
        is_coded_chunk_file: bool
        cloud_domain_id_vec: _containers.RepeatedScalarFieldContainer[int]
        edek_info: _keychain_pb2.EdekProto
        encryption_mode: _aes_encryptor_pb2.AESEncryptorMode
        update_intent_history_record_vec: _containers.RepeatedCompositeFieldContainer[ChunkFileMetadataProto.UpdateIntentHistoryRecord]
        def __init__(self, opclock_vec: _Optional[_Iterable[_Union[_op_clock_pb2.OpClock, _Mapping]]] = ..., chunk_count: _Optional[int] = ..., chunkgroup_count: _Optional[int] = ..., owner_blob_id: _Optional[int] = ..., owner_view_box_id: _Optional[int] = ..., compression_level: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.StoragePolicy.CompressionLevel, str]] = ..., encryption_level: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.EncryptionLevel, str]] = ..., last_waterfall_time_usecs: _Optional[int] = ..., intent_id_generator: _Optional[int] = ..., update_intent: _Optional[_Union[ChunkFileMetadataProto.UpdateIntent, _Mapping]] = ..., replica_vec: _Optional[_Iterable[_Union[ChunkFileMetadataProto.Replica, _Mapping]]] = ..., update_intent_session_id: _Optional[int] = ..., version: _Optional[int] = ..., morphed_size_hint: _Optional[int] = ..., finalize_existing_io_update_intents: bool = ..., last_update_time_usecs: _Optional[int] = ..., ec_container_info: _Optional[_Union[ChunkFileContainerMetadataProto.ECAlgoInfo, _Mapping]] = ..., ec_info: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.StoragePolicy.ECInfo, _Mapping]] = ..., next_avail_stripe_row: _Optional[int] = ..., next_avail_chunkgroup_id: _Optional[int] = ..., has_dedup_chunks: bool = ..., chunk_file_container_id: _Optional[int] = ..., is_coded_chunk_file: bool = ..., cloud_domain_id_vec: _Optional[_Iterable[int]] = ..., edek_info: _Optional[_Union[_keychain_pb2.EdekProto, _Mapping]] = ..., encryption_mode: _Optional[_Union[_aes_encryptor_pb2.AESEncryptorMode, str]] = ..., update_intent_history_record_vec: _Optional[_Iterable[_Union[ChunkFileMetadataProto.UpdateIntentHistoryRecord, _Mapping]]] = ...) -> None: ...
    class ChunkColumn(_message.Message):
        __slots__ = ("snap_tree_leaf_node_id", "offset", "chunkgroup_id", "checksum", "morphed_size", "stripe_col")
        SNAP_TREE_LEAF_NODE_ID_FIELD_NUMBER: _ClassVar[int]
        OFFSET_FIELD_NUMBER: _ClassVar[int]
        CHUNKGROUP_ID_FIELD_NUMBER: _ClassVar[int]
        CHECKSUM_FIELD_NUMBER: _ClassVar[int]
        MORPHED_SIZE_FIELD_NUMBER: _ClassVar[int]
        STRIPE_COL_FIELD_NUMBER: _ClassVar[int]
        snap_tree_leaf_node_id: int
        offset: int
        chunkgroup_id: int
        checksum: int
        morphed_size: int
        stripe_col: int
        def __init__(self, snap_tree_leaf_node_id: _Optional[int] = ..., offset: _Optional[int] = ..., chunkgroup_id: _Optional[int] = ..., checksum: _Optional[int] = ..., morphed_size: _Optional[int] = ..., stripe_col: _Optional[int] = ...) -> None: ...
    class ChunkGroupColumn(_message.Message):
        __slots__ = ("unmorphed_size", "morphed_size", "offset", "checksum", "expansion_area_size", "compressed_size", "stripe_col", "stripe_ec_info", "stripe_row")
        class StripeECInfo(_message.Message):
            __slots__ = ("data_stripe_offset_vec", "data_stripe_length_vec", "data_stripe_adler32_cksum_vec")
            DATA_STRIPE_OFFSET_VEC_FIELD_NUMBER: _ClassVar[int]
            DATA_STRIPE_LENGTH_VEC_FIELD_NUMBER: _ClassVar[int]
            DATA_STRIPE_ADLER32_CKSUM_VEC_FIELD_NUMBER: _ClassVar[int]
            data_stripe_offset_vec: _containers.RepeatedScalarFieldContainer[int]
            data_stripe_length_vec: _containers.RepeatedScalarFieldContainer[int]
            data_stripe_adler32_cksum_vec: _containers.RepeatedScalarFieldContainer[int]
            def __init__(self, data_stripe_offset_vec: _Optional[_Iterable[int]] = ..., data_stripe_length_vec: _Optional[_Iterable[int]] = ..., data_stripe_adler32_cksum_vec: _Optional[_Iterable[int]] = ...) -> None: ...
        UNMORPHED_SIZE_FIELD_NUMBER: _ClassVar[int]
        MORPHED_SIZE_FIELD_NUMBER: _ClassVar[int]
        OFFSET_FIELD_NUMBER: _ClassVar[int]
        CHECKSUM_FIELD_NUMBER: _ClassVar[int]
        EXPANSION_AREA_SIZE_FIELD_NUMBER: _ClassVar[int]
        COMPRESSED_SIZE_FIELD_NUMBER: _ClassVar[int]
        STRIPE_COL_FIELD_NUMBER: _ClassVar[int]
        STRIPE_EC_INFO_FIELD_NUMBER: _ClassVar[int]
        STRIPE_ROW_FIELD_NUMBER: _ClassVar[int]
        unmorphed_size: int
        morphed_size: int
        offset: int
        checksum: int
        expansion_area_size: int
        compressed_size: int
        stripe_col: int
        stripe_ec_info: ChunkFileMetadataProto.ChunkGroupColumn.StripeECInfo
        stripe_row: int
        def __init__(self, unmorphed_size: _Optional[int] = ..., morphed_size: _Optional[int] = ..., offset: _Optional[int] = ..., checksum: _Optional[int] = ..., expansion_area_size: _Optional[int] = ..., compressed_size: _Optional[int] = ..., stripe_col: _Optional[int] = ..., stripe_ec_info: _Optional[_Union[ChunkFileMetadataProto.ChunkGroupColumn.StripeECInfo, _Mapping]] = ..., stripe_row: _Optional[int] = ...) -> None: ...
    def __init__(self) -> None: ...

class ChunkFileAccessStateProto(_message.Message):
    __slots__ = ("last_access_time_usecs", "is_read", "is_random")
    LAST_ACCESS_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    IS_READ_FIELD_NUMBER: _ClassVar[int]
    IS_RANDOM_FIELD_NUMBER: _ClassVar[int]
    last_access_time_usecs: int
    is_read: bool
    is_random: bool
    def __init__(self, last_access_time_usecs: _Optional[int] = ..., is_read: bool = ..., is_random: bool = ...) -> None: ...

class PinnedChunkFileAccessStateProto(_message.Message):
    __slots__ = ("pinned_view_entry_vec", "last_update_time_secs")
    class PinnedViewEntry(_message.Message):
        __slots__ = ("view_id", "last_access_time_secs")
        VIEW_ID_FIELD_NUMBER: _ClassVar[int]
        LAST_ACCESS_TIME_SECS_FIELD_NUMBER: _ClassVar[int]
        view_id: int
        last_access_time_secs: int
        def __init__(self, view_id: _Optional[int] = ..., last_access_time_secs: _Optional[int] = ...) -> None: ...
    PINNED_VIEW_ENTRY_VEC_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATE_TIME_SECS_FIELD_NUMBER: _ClassVar[int]
    pinned_view_entry_vec: _containers.RepeatedCompositeFieldContainer[PinnedChunkFileAccessStateProto.PinnedViewEntry]
    last_update_time_secs: int
    def __init__(self, pinned_view_entry_vec: _Optional[_Iterable[_Union[PinnedChunkFileAccessStateProto.PinnedViewEntry, _Mapping]]] = ..., last_update_time_secs: _Optional[int] = ...) -> None: ...

class MorphParams(_message.Message):
    __slots__ = ()
    class Reason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kUpTiering: _ClassVar[MorphParams.Reason]
        kDownTiering: _ClassVar[MorphParams.Reason]
        kDiskBalancing: _ClassVar[MorphParams.Reason]
        kCompression: _ClassVar[MorphParams.Reason]
        kUncompression: _ClassVar[MorphParams.Reason]
        kDefrag: _ClassVar[MorphParams.Reason]
        kForce: _ClassVar[MorphParams.Reason]
        kCloudSpill: _ClassVar[MorphParams.Reason]
        kForceDownTiering: _ClassVar[MorphParams.Reason]
        kRecovery: _ClassVar[MorphParams.Reason]
    kUpTiering: MorphParams.Reason
    kDownTiering: MorphParams.Reason
    kDiskBalancing: MorphParams.Reason
    kCompression: MorphParams.Reason
    kUncompression: MorphParams.Reason
    kDefrag: MorphParams.Reason
    kForce: MorphParams.Reason
    kCloudSpill: MorphParams.Reason
    kForceDownTiering: MorphParams.Reason
    kRecovery: MorphParams.Reason
    def __init__(self) -> None: ...

class CloudChunkFileScribeMetadataProto(_message.Message):
    __slots__ = ("opclock_vec", "chunk_file_version", "chunk_count", "morphed_data_size", "creation_time_usecs", "external_write_permission_expiry_time_usecs", "last_update_time_usecs", "intent_id_generator", "update_intent_session_id", "update_intent", "touch_time_usecs", "update_intent_history_record_vec", "tiering_epoch_id", "tier_info_vec", "morphed_data_offset", "lease_proto_vec", "last_file_existence_validation_usecs", "last_chunk_existence_validation_usecs", "last_chunk_data_validation_usecs", "minimum_retention_timestamp_secs", "retention_mode", "versioned_object_id", "encryption_level", "encryption_mode", "worm_retention_extendability_info")
    class UpdateIntent(_message.Message):
        __slots__ = ("intent_id", "creation_time_usecs", "write_chunks", "add_chunk_mappings", "delete_chunks", "downtier_chunk_file", "uptier_chunk_file")
        class WriteChunks(_message.Message):
            __slots__ = ("cloud_object_written", "written_time_usecs", "edek_info", "compression_level", "morphed_data_size", "chunk_info_vec", "chunk_group_info_vec", "morphed_data_offset")
            class ChunkInfo(_message.Message):
                __slots__ = ("cloud_chunk_id", "local_chunk_id", "snap_tree_leaf_node_id", "blob_snap_tree_id", "chunk_column")
                CLOUD_CHUNK_ID_FIELD_NUMBER: _ClassVar[int]
                LOCAL_CHUNK_ID_FIELD_NUMBER: _ClassVar[int]
                SNAP_TREE_LEAF_NODE_ID_FIELD_NUMBER: _ClassVar[int]
                BLOB_SNAP_TREE_ID_FIELD_NUMBER: _ClassVar[int]
                CHUNK_COLUMN_FIELD_NUMBER: _ClassVar[int]
                cloud_chunk_id: CloudChunkIdProto
                local_chunk_id: ChunkIdProto
                snap_tree_leaf_node_id: int
                blob_snap_tree_id: int
                chunk_column: ChunkFileMetadataProto.ChunkColumn
                def __init__(self, cloud_chunk_id: _Optional[_Union[CloudChunkIdProto, _Mapping]] = ..., local_chunk_id: _Optional[_Union[ChunkIdProto, _Mapping]] = ..., snap_tree_leaf_node_id: _Optional[int] = ..., blob_snap_tree_id: _Optional[int] = ..., chunk_column: _Optional[_Union[ChunkFileMetadataProto.ChunkColumn, _Mapping]] = ...) -> None: ...
            class ChunkGroupInfo(_message.Message):
                __slots__ = ("chunkgroup_id", "chunkgroup_column")
                CHUNKGROUP_ID_FIELD_NUMBER: _ClassVar[int]
                CHUNKGROUP_COLUMN_FIELD_NUMBER: _ClassVar[int]
                chunkgroup_id: int
                chunkgroup_column: ChunkFileMetadataProto.ChunkGroupColumn
                def __init__(self, chunkgroup_id: _Optional[int] = ..., chunkgroup_column: _Optional[_Union[ChunkFileMetadataProto.ChunkGroupColumn, _Mapping]] = ...) -> None: ...
            CLOUD_OBJECT_WRITTEN_FIELD_NUMBER: _ClassVar[int]
            WRITTEN_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
            EDEK_INFO_FIELD_NUMBER: _ClassVar[int]
            COMPRESSION_LEVEL_FIELD_NUMBER: _ClassVar[int]
            MORPHED_DATA_SIZE_FIELD_NUMBER: _ClassVar[int]
            CHUNK_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
            CHUNK_GROUP_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
            MORPHED_DATA_OFFSET_FIELD_NUMBER: _ClassVar[int]
            cloud_object_written: bool
            written_time_usecs: int
            edek_info: _keychain_pb2.EdekProto
            compression_level: _cluster_config_pb2.ClusterConfigProto.StoragePolicy.CompressionLevel
            morphed_data_size: int
            chunk_info_vec: _containers.RepeatedCompositeFieldContainer[CloudChunkFileScribeMetadataProto.UpdateIntent.WriteChunks.ChunkInfo]
            chunk_group_info_vec: _containers.RepeatedCompositeFieldContainer[CloudChunkFileScribeMetadataProto.UpdateIntent.WriteChunks.ChunkGroupInfo]
            morphed_data_offset: int
            def __init__(self, cloud_object_written: bool = ..., written_time_usecs: _Optional[int] = ..., edek_info: _Optional[_Union[_keychain_pb2.EdekProto, _Mapping]] = ..., compression_level: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.StoragePolicy.CompressionLevel, str]] = ..., morphed_data_size: _Optional[int] = ..., chunk_info_vec: _Optional[_Iterable[_Union[CloudChunkFileScribeMetadataProto.UpdateIntent.WriteChunks.ChunkInfo, _Mapping]]] = ..., chunk_group_info_vec: _Optional[_Iterable[_Union[CloudChunkFileScribeMetadataProto.UpdateIntent.WriteChunks.ChunkGroupInfo, _Mapping]]] = ..., morphed_data_offset: _Optional[int] = ...) -> None: ...
        class AddChunkMappings(_message.Message):
            __slots__ = ("total_chunk_count", "morphed_data_size", "cloud_chunk_id_vec", "view_box_id")
            TOTAL_CHUNK_COUNT_FIELD_NUMBER: _ClassVar[int]
            MORPHED_DATA_SIZE_FIELD_NUMBER: _ClassVar[int]
            CLOUD_CHUNK_ID_VEC_FIELD_NUMBER: _ClassVar[int]
            VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
            total_chunk_count: int
            morphed_data_size: int
            cloud_chunk_id_vec: _containers.RepeatedCompositeFieldContainer[CloudChunkIdProto]
            view_box_id: int
            def __init__(self, total_chunk_count: _Optional[int] = ..., morphed_data_size: _Optional[int] = ..., cloud_chunk_id_vec: _Optional[_Iterable[_Union[CloudChunkIdProto, _Mapping]]] = ..., view_box_id: _Optional[int] = ...) -> None: ...
        class DeleteChunks(_message.Message):
            __slots__ = ("chunk_info_vec", "can_delete_cloud_object", "new_cloud_object_info", "new_cloud_object_encryption_mode")
            class ChunkInfo(_message.Message):
                __slots__ = ("cloud_chunk_id", "local_chunk_id")
                CLOUD_CHUNK_ID_FIELD_NUMBER: _ClassVar[int]
                LOCAL_CHUNK_ID_FIELD_NUMBER: _ClassVar[int]
                cloud_chunk_id: CloudChunkIdProto
                local_chunk_id: ChunkIdProto
                def __init__(self, cloud_chunk_id: _Optional[_Union[CloudChunkIdProto, _Mapping]] = ..., local_chunk_id: _Optional[_Union[ChunkIdProto, _Mapping]] = ...) -> None: ...
            class CloudObjectInfo(_message.Message):
                __slots__ = ("chunk_count", "morphed_data_size", "morphed_data_offset")
                CHUNK_COUNT_FIELD_NUMBER: _ClassVar[int]
                MORPHED_DATA_SIZE_FIELD_NUMBER: _ClassVar[int]
                MORPHED_DATA_OFFSET_FIELD_NUMBER: _ClassVar[int]
                chunk_count: int
                morphed_data_size: int
                morphed_data_offset: int
                def __init__(self, chunk_count: _Optional[int] = ..., morphed_data_size: _Optional[int] = ..., morphed_data_offset: _Optional[int] = ...) -> None: ...
            CHUNK_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
            CAN_DELETE_CLOUD_OBJECT_FIELD_NUMBER: _ClassVar[int]
            NEW_CLOUD_OBJECT_INFO_FIELD_NUMBER: _ClassVar[int]
            NEW_CLOUD_OBJECT_ENCRYPTION_MODE_FIELD_NUMBER: _ClassVar[int]
            chunk_info_vec: _containers.RepeatedCompositeFieldContainer[CloudChunkFileScribeMetadataProto.UpdateIntent.DeleteChunks.ChunkInfo]
            can_delete_cloud_object: bool
            new_cloud_object_info: CloudChunkFileScribeMetadataProto.UpdateIntent.DeleteChunks.CloudObjectInfo
            new_cloud_object_encryption_mode: _aes_encryptor_pb2.AESEncryptorMode
            def __init__(self, chunk_info_vec: _Optional[_Iterable[_Union[CloudChunkFileScribeMetadataProto.UpdateIntent.DeleteChunks.ChunkInfo, _Mapping]]] = ..., can_delete_cloud_object: bool = ..., new_cloud_object_info: _Optional[_Union[CloudChunkFileScribeMetadataProto.UpdateIntent.DeleteChunks.CloudObjectInfo, _Mapping]] = ..., new_cloud_object_encryption_mode: _Optional[_Union[_aes_encryptor_pb2.AESEncryptorMode, str]] = ...) -> None: ...
        class DowntierChunkFile(_message.Message):
            __slots__ = ("target_tier_type",)
            TARGET_TIER_TYPE_FIELD_NUMBER: _ClassVar[int]
            target_tier_type: _cluster_config_pb2.ClusterConfigProto.Vault.CloudTierType
            def __init__(self, target_tier_type: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.Vault.CloudTierType, _Mapping]] = ...) -> None: ...
        class UptierChunkFile(_message.Message):
            __slots__ = ("target_tier_type", "expected_expiry_time_usecs", "uptier_context")
            TARGET_TIER_TYPE_FIELD_NUMBER: _ClassVar[int]
            EXPECTED_EXPIRY_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
            UPTIER_CONTEXT_FIELD_NUMBER: _ClassVar[int]
            target_tier_type: _cluster_config_pb2.ClusterConfigProto.Vault.CloudTierType
            expected_expiry_time_usecs: int
            uptier_context: _vault_pb2.VaultUptierContextProto
            def __init__(self, target_tier_type: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.Vault.CloudTierType, _Mapping]] = ..., expected_expiry_time_usecs: _Optional[int] = ..., uptier_context: _Optional[_Union[_vault_pb2.VaultUptierContextProto, _Mapping]] = ...) -> None: ...
        INTENT_ID_FIELD_NUMBER: _ClassVar[int]
        CREATION_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
        WRITE_CHUNKS_FIELD_NUMBER: _ClassVar[int]
        ADD_CHUNK_MAPPINGS_FIELD_NUMBER: _ClassVar[int]
        DELETE_CHUNKS_FIELD_NUMBER: _ClassVar[int]
        DOWNTIER_CHUNK_FILE_FIELD_NUMBER: _ClassVar[int]
        UPTIER_CHUNK_FILE_FIELD_NUMBER: _ClassVar[int]
        intent_id: int
        creation_time_usecs: int
        write_chunks: CloudChunkFileScribeMetadataProto.UpdateIntent.WriteChunks
        add_chunk_mappings: CloudChunkFileScribeMetadataProto.UpdateIntent.AddChunkMappings
        delete_chunks: CloudChunkFileScribeMetadataProto.UpdateIntent.DeleteChunks
        downtier_chunk_file: CloudChunkFileScribeMetadataProto.UpdateIntent.DowntierChunkFile
        uptier_chunk_file: CloudChunkFileScribeMetadataProto.UpdateIntent.UptierChunkFile
        def __init__(self, intent_id: _Optional[int] = ..., creation_time_usecs: _Optional[int] = ..., write_chunks: _Optional[_Union[CloudChunkFileScribeMetadataProto.UpdateIntent.WriteChunks, _Mapping]] = ..., add_chunk_mappings: _Optional[_Union[CloudChunkFileScribeMetadataProto.UpdateIntent.AddChunkMappings, _Mapping]] = ..., delete_chunks: _Optional[_Union[CloudChunkFileScribeMetadataProto.UpdateIntent.DeleteChunks, _Mapping]] = ..., downtier_chunk_file: _Optional[_Union[CloudChunkFileScribeMetadataProto.UpdateIntent.DowntierChunkFile, _Mapping]] = ..., uptier_chunk_file: _Optional[_Union[CloudChunkFileScribeMetadataProto.UpdateIntent.UptierChunkFile, _Mapping]] = ...) -> None: ...
    class CloudTierInfo(_message.Message):
        __slots__ = ("tier", "expiry_time_usecs", "is_uptiered_copy")
        TIER_FIELD_NUMBER: _ClassVar[int]
        EXPIRY_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
        IS_UPTIERED_COPY_FIELD_NUMBER: _ClassVar[int]
        tier: _cluster_config_pb2.ClusterConfigProto.Vault.CloudTierType
        expiry_time_usecs: int
        is_uptiered_copy: bool
        def __init__(self, tier: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.Vault.CloudTierType, _Mapping]] = ..., expiry_time_usecs: _Optional[int] = ..., is_uptiered_copy: bool = ...) -> None: ...
    OPCLOCK_VEC_FIELD_NUMBER: _ClassVar[int]
    CHUNK_FILE_VERSION_FIELD_NUMBER: _ClassVar[int]
    CHUNK_COUNT_FIELD_NUMBER: _ClassVar[int]
    MORPHED_DATA_SIZE_FIELD_NUMBER: _ClassVar[int]
    CREATION_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_WRITE_PERMISSION_EXPIRY_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATE_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    INTENT_ID_GENERATOR_FIELD_NUMBER: _ClassVar[int]
    UPDATE_INTENT_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    UPDATE_INTENT_FIELD_NUMBER: _ClassVar[int]
    TOUCH_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    UPDATE_INTENT_HISTORY_RECORD_VEC_FIELD_NUMBER: _ClassVar[int]
    TIERING_EPOCH_ID_FIELD_NUMBER: _ClassVar[int]
    TIER_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    MORPHED_DATA_OFFSET_FIELD_NUMBER: _ClassVar[int]
    LEASE_PROTO_VEC_FIELD_NUMBER: _ClassVar[int]
    LAST_FILE_EXISTENCE_VALIDATION_USECS_FIELD_NUMBER: _ClassVar[int]
    LAST_CHUNK_EXISTENCE_VALIDATION_USECS_FIELD_NUMBER: _ClassVar[int]
    LAST_CHUNK_DATA_VALIDATION_USECS_FIELD_NUMBER: _ClassVar[int]
    MINIMUM_RETENTION_TIMESTAMP_SECS_FIELD_NUMBER: _ClassVar[int]
    RETENTION_MODE_FIELD_NUMBER: _ClassVar[int]
    VERSIONED_OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_LEVEL_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_MODE_FIELD_NUMBER: _ClassVar[int]
    WORM_RETENTION_EXTENDABILITY_INFO_FIELD_NUMBER: _ClassVar[int]
    opclock_vec: _containers.RepeatedCompositeFieldContainer[_op_clock_pb2.OpClock]
    chunk_file_version: int
    chunk_count: int
    morphed_data_size: int
    creation_time_usecs: int
    external_write_permission_expiry_time_usecs: int
    last_update_time_usecs: int
    intent_id_generator: int
    update_intent_session_id: int
    update_intent: CloudChunkFileScribeMetadataProto.UpdateIntent
    touch_time_usecs: int
    update_intent_history_record_vec: _containers.RepeatedCompositeFieldContainer[CloudChunkFileScribeMetadataProto.UpdateIntent]
    tiering_epoch_id: int
    tier_info_vec: _containers.RepeatedCompositeFieldContainer[CloudChunkFileScribeMetadataProto.CloudTierInfo]
    morphed_data_offset: int
    lease_proto_vec: _containers.RepeatedCompositeFieldContainer[_cloud_pb2.LeaseProto]
    last_file_existence_validation_usecs: int
    last_chunk_existence_validation_usecs: int
    last_chunk_data_validation_usecs: int
    minimum_retention_timestamp_secs: int
    retention_mode: _worm_pb2.RetentionMode.Type
    versioned_object_id: str
    encryption_level: _cluster_config_pb2.ClusterConfigProto.EncryptionLevel
    encryption_mode: _aes_encryptor_pb2.AESEncryptorMode
    worm_retention_extendability_info: _worm_pb2.WORMRetentionExtendabilityInfo
    def __init__(self, opclock_vec: _Optional[_Iterable[_Union[_op_clock_pb2.OpClock, _Mapping]]] = ..., chunk_file_version: _Optional[int] = ..., chunk_count: _Optional[int] = ..., morphed_data_size: _Optional[int] = ..., creation_time_usecs: _Optional[int] = ..., external_write_permission_expiry_time_usecs: _Optional[int] = ..., last_update_time_usecs: _Optional[int] = ..., intent_id_generator: _Optional[int] = ..., update_intent_session_id: _Optional[int] = ..., update_intent: _Optional[_Union[CloudChunkFileScribeMetadataProto.UpdateIntent, _Mapping]] = ..., touch_time_usecs: _Optional[int] = ..., update_intent_history_record_vec: _Optional[_Iterable[_Union[CloudChunkFileScribeMetadataProto.UpdateIntent, _Mapping]]] = ..., tiering_epoch_id: _Optional[int] = ..., tier_info_vec: _Optional[_Iterable[_Union[CloudChunkFileScribeMetadataProto.CloudTierInfo, _Mapping]]] = ..., morphed_data_offset: _Optional[int] = ..., lease_proto_vec: _Optional[_Iterable[_Union[_cloud_pb2.LeaseProto, _Mapping]]] = ..., last_file_existence_validation_usecs: _Optional[int] = ..., last_chunk_existence_validation_usecs: _Optional[int] = ..., last_chunk_data_validation_usecs: _Optional[int] = ..., minimum_retention_timestamp_secs: _Optional[int] = ..., retention_mode: _Optional[_Union[_worm_pb2.RetentionMode.Type, str]] = ..., versioned_object_id: _Optional[str] = ..., encryption_level: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.EncryptionLevel, str]] = ..., encryption_mode: _Optional[_Union[_aes_encryptor_pb2.AESEncryptorMode, str]] = ..., worm_retention_extendability_info: _Optional[_Union[_worm_pb2.WORMRetentionExtendabilityInfo, _Mapping]] = ...) -> None: ...

class ConstantsProto(_message.Message):
    __slots__ = ("pinned_chunk_file_state_column_name",)
    PINNED_CHUNK_FILE_STATE_COLUMN_NAME_FIELD_NUMBER: _ClassVar[int]
    pinned_chunk_file_state_column_name: str
    def __init__(self, pinned_chunk_file_state_column_name: _Optional[str] = ...) -> None: ...
