from configs import cluster_config_pb2 as _cluster_config_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ChunkFileValidatorContextDataProto(_message.Message):
    __slots__ = ("cluster_config_proto", "num_scan_shards_per_node")
    CLUSTER_CONFIG_PROTO_FIELD_NUMBER: _ClassVar[int]
    NUM_SCAN_SHARDS_PER_NODE_FIELD_NUMBER: _ClassVar[int]
    cluster_config_proto: _cluster_config_pb2.ClusterConfigProto
    num_scan_shards_per_node: int
    def __init__(self, cluster_config_proto: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto, _Mapping]] = ..., num_scan_shards_per_node: _Optional[int] = ...) -> None: ...

class ChunkFileValidatorMapKeyProto(_message.Message):
    __slots__ = ("chunk_file_id",)
    CHUNK_FILE_ID_FIELD_NUMBER: _ClassVar[int]
    chunk_file_id: int
    def __init__(self, chunk_file_id: _Optional[int] = ...) -> None: ...

class ChunkFileValidatorMapValueProto(_message.Message):
    __slots__ = ("disk_ids", "chunk_count", "scribe_scan", "owner_blob_id", "view_box_id", "is_in_cloud_tier")
    DISK_IDS_FIELD_NUMBER: _ClassVar[int]
    CHUNK_COUNT_FIELD_NUMBER: _ClassVar[int]
    SCRIBE_SCAN_FIELD_NUMBER: _ClassVar[int]
    OWNER_BLOB_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
    IS_IN_CLOUD_TIER_FIELD_NUMBER: _ClassVar[int]
    disk_ids: _containers.RepeatedScalarFieldContainer[int]
    chunk_count: int
    scribe_scan: bool
    owner_blob_id: int
    view_box_id: int
    is_in_cloud_tier: bool
    def __init__(self, disk_ids: _Optional[_Iterable[int]] = ..., chunk_count: _Optional[int] = ..., scribe_scan: bool = ..., owner_blob_id: _Optional[int] = ..., view_box_id: _Optional[int] = ..., is_in_cloud_tier: bool = ...) -> None: ...
