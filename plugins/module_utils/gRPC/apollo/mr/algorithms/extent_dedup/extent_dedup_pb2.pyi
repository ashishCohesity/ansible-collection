from bridge.apollo import actions_v2_pb2 as _actions_v2_pb2
from bridge.blob_store import blob_store_pb2 as _blob_store_pb2
from configs import cluster_config_pb2 as _cluster_config_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BrickCombineKey(_message.Message):
    __slots__ = ("blob_id", "brick_bucket")
    BLOB_ID_FIELD_NUMBER: _ClassVar[int]
    BRICK_BUCKET_FIELD_NUMBER: _ClassVar[int]
    blob_id: int
    brick_bucket: int
    def __init__(self, blob_id: _Optional[int] = ..., brick_bucket: _Optional[int] = ...) -> None: ...

class BrickInfo(_message.Message):
    __slots__ = ("brick_id", "blob_id", "extent_vec")
    BRICK_ID_FIELD_NUMBER: _ClassVar[int]
    BLOB_ID_FIELD_NUMBER: _ClassVar[int]
    EXTENT_VEC_FIELD_NUMBER: _ClassVar[int]
    brick_id: int
    blob_id: int
    extent_vec: _containers.RepeatedCompositeFieldContainer[_blob_store_pb2.BrickMetadataProto.Extent]
    def __init__(self, brick_id: _Optional[int] = ..., blob_id: _Optional[int] = ..., extent_vec: _Optional[_Iterable[_Union[_blob_store_pb2.BrickMetadataProto.Extent, _Mapping]]] = ...) -> None: ...

class BrickCombineReducerValue(_message.Message):
    __slots__ = ("brick_info_vec",)
    BRICK_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    brick_info_vec: _containers.RepeatedCompositeFieldContainer[BrickInfo]
    def __init__(self, brick_info_vec: _Optional[_Iterable[_Union[BrickInfo, _Mapping]]] = ...) -> None: ...

class ExtentCommonSequenceKey(_message.Message):
    __slots__ = ("dedup_chunk_vec",)
    DEDUP_CHUNK_VEC_FIELD_NUMBER: _ClassVar[int]
    dedup_chunk_vec: _containers.RepeatedCompositeFieldContainer[_actions_v2_pb2.ConvertToMegachunkAction.DedupChunkInfo]
    def __init__(self, dedup_chunk_vec: _Optional[_Iterable[_Union[_actions_v2_pb2.ConvertToMegachunkAction.DedupChunkInfo, _Mapping]]] = ...) -> None: ...

class ExtentCommonSequenceValue(_message.Message):
    __slots__ = ("position_info",)
    POSITION_INFO_FIELD_NUMBER: _ClassVar[int]
    position_info: _actions_v2_pb2.ConvertToMegachunkAction.BlobPositionInfo
    def __init__(self, position_info: _Optional[_Union[_actions_v2_pb2.ConvertToMegachunkAction.BlobPositionInfo, _Mapping]] = ...) -> None: ...

class ExtentDedupContextDataProto(_message.Message):
    __slots__ = ("cluster_config_proto", "apollo_mr_extent_dedup_brick_bucket_size", "apollo_mr_extent_dedup_minumum_common_appearance_count", "apollo_mr_extent_dedup_desired_megachunk_length")
    CLUSTER_CONFIG_PROTO_FIELD_NUMBER: _ClassVar[int]
    APOLLO_MR_EXTENT_DEDUP_BRICK_BUCKET_SIZE_FIELD_NUMBER: _ClassVar[int]
    APOLLO_MR_EXTENT_DEDUP_MINUMUM_COMMON_APPEARANCE_COUNT_FIELD_NUMBER: _ClassVar[int]
    APOLLO_MR_EXTENT_DEDUP_DESIRED_MEGACHUNK_LENGTH_FIELD_NUMBER: _ClassVar[int]
    cluster_config_proto: _cluster_config_pb2.ClusterConfigProto
    apollo_mr_extent_dedup_brick_bucket_size: int
    apollo_mr_extent_dedup_minumum_common_appearance_count: int
    apollo_mr_extent_dedup_desired_megachunk_length: int
    def __init__(self, cluster_config_proto: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto, _Mapping]] = ..., apollo_mr_extent_dedup_brick_bucket_size: _Optional[int] = ..., apollo_mr_extent_dedup_minumum_common_appearance_count: _Optional[int] = ..., apollo_mr_extent_dedup_desired_megachunk_length: _Optional[int] = ...) -> None: ...
