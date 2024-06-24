from configs import cluster_config_pb2 as _cluster_config_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ChunkFileCloudSpillerContextDataProto(_message.Message):
    __slots__ = ("cluster_config_proto", "max_num_chunk_file_to_spill", "previous_tier_name", "previous_tier_overflow_bytes", "candidate_cloud_spill_viewbox_vec", "viewbox_overflow_info_vec", "viewbox_coldness_threshold_vec")
    class ViewBoxOverflowInfo(_message.Message):
        __slots__ = ("viewbox_id", "overflow_bytes")
        VIEWBOX_ID_FIELD_NUMBER: _ClassVar[int]
        OVERFLOW_BYTES_FIELD_NUMBER: _ClassVar[int]
        viewbox_id: int
        overflow_bytes: int
        def __init__(self, viewbox_id: _Optional[int] = ..., overflow_bytes: _Optional[int] = ...) -> None: ...
    class ViewBoxColdnessThresholdInfo(_message.Message):
        __slots__ = ("viewbox_id", "coldness_threshold_secs")
        VIEWBOX_ID_FIELD_NUMBER: _ClassVar[int]
        COLDNESS_THRESHOLD_SECS_FIELD_NUMBER: _ClassVar[int]
        viewbox_id: int
        coldness_threshold_secs: int
        def __init__(self, viewbox_id: _Optional[int] = ..., coldness_threshold_secs: _Optional[int] = ...) -> None: ...
    CLUSTER_CONFIG_PROTO_FIELD_NUMBER: _ClassVar[int]
    MAX_NUM_CHUNK_FILE_TO_SPILL_FIELD_NUMBER: _ClassVar[int]
    PREVIOUS_TIER_NAME_FIELD_NUMBER: _ClassVar[int]
    PREVIOUS_TIER_OVERFLOW_BYTES_FIELD_NUMBER: _ClassVar[int]
    CANDIDATE_CLOUD_SPILL_VIEWBOX_VEC_FIELD_NUMBER: _ClassVar[int]
    VIEWBOX_OVERFLOW_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    VIEWBOX_COLDNESS_THRESHOLD_VEC_FIELD_NUMBER: _ClassVar[int]
    cluster_config_proto: _cluster_config_pb2.ClusterConfigProto
    max_num_chunk_file_to_spill: int
    previous_tier_name: str
    previous_tier_overflow_bytes: int
    candidate_cloud_spill_viewbox_vec: _containers.RepeatedScalarFieldContainer[int]
    viewbox_overflow_info_vec: _containers.RepeatedCompositeFieldContainer[ChunkFileCloudSpillerContextDataProto.ViewBoxOverflowInfo]
    viewbox_coldness_threshold_vec: _containers.RepeatedCompositeFieldContainer[ChunkFileCloudSpillerContextDataProto.ViewBoxColdnessThresholdInfo]
    def __init__(self, cluster_config_proto: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto, _Mapping]] = ..., max_num_chunk_file_to_spill: _Optional[int] = ..., previous_tier_name: _Optional[str] = ..., previous_tier_overflow_bytes: _Optional[int] = ..., candidate_cloud_spill_viewbox_vec: _Optional[_Iterable[int]] = ..., viewbox_overflow_info_vec: _Optional[_Iterable[_Union[ChunkFileCloudSpillerContextDataProto.ViewBoxOverflowInfo, _Mapping]]] = ..., viewbox_coldness_threshold_vec: _Optional[_Iterable[_Union[ChunkFileCloudSpillerContextDataProto.ViewBoxColdnessThresholdInfo, _Mapping]]] = ...) -> None: ...

class ChunkFileCloudSpillerProto(_message.Message):
    __slots__ = ("coldness_secs", "chunk_file_id", "view_box_id", "owner_blob_id", "scribe_row_version", "current_compression_level", "current_encryption_level", "chunk_file_morphed_size", "is_erasure_coded", "has_viewbox_downtier_threshold")
    COLDNESS_SECS_FIELD_NUMBER: _ClassVar[int]
    CHUNK_FILE_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
    OWNER_BLOB_ID_FIELD_NUMBER: _ClassVar[int]
    SCRIBE_ROW_VERSION_FIELD_NUMBER: _ClassVar[int]
    CURRENT_COMPRESSION_LEVEL_FIELD_NUMBER: _ClassVar[int]
    CURRENT_ENCRYPTION_LEVEL_FIELD_NUMBER: _ClassVar[int]
    CHUNK_FILE_MORPHED_SIZE_FIELD_NUMBER: _ClassVar[int]
    IS_ERASURE_CODED_FIELD_NUMBER: _ClassVar[int]
    HAS_VIEWBOX_DOWNTIER_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    coldness_secs: int
    chunk_file_id: int
    view_box_id: int
    owner_blob_id: int
    scribe_row_version: int
    current_compression_level: _cluster_config_pb2.ClusterConfigProto.StoragePolicy.CompressionLevel
    current_encryption_level: _cluster_config_pb2.ClusterConfigProto.EncryptionLevel
    chunk_file_morphed_size: int
    is_erasure_coded: bool
    has_viewbox_downtier_threshold: bool
    def __init__(self, coldness_secs: _Optional[int] = ..., chunk_file_id: _Optional[int] = ..., view_box_id: _Optional[int] = ..., owner_blob_id: _Optional[int] = ..., scribe_row_version: _Optional[int] = ..., current_compression_level: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.StoragePolicy.CompressionLevel, str]] = ..., current_encryption_level: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.EncryptionLevel, str]] = ..., chunk_file_morphed_size: _Optional[int] = ..., is_erasure_coded: bool = ..., has_viewbox_downtier_threshold: bool = ...) -> None: ...
