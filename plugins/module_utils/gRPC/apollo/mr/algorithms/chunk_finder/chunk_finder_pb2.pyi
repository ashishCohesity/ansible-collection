from configs import cluster_config_pb2 as _cluster_config_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ChunkFinderContextDataProto(_message.Message):
    __slots__ = ("cluster_config_proto", "is_orphan_chunk_references_mode")
    CLUSTER_CONFIG_PROTO_FIELD_NUMBER: _ClassVar[int]
    IS_ORPHAN_CHUNK_REFERENCES_MODE_FIELD_NUMBER: _ClassVar[int]
    cluster_config_proto: _cluster_config_pb2.ClusterConfigProto
    is_orphan_chunk_references_mode: bool
    def __init__(self, cluster_config_proto: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto, _Mapping]] = ..., is_orphan_chunk_references_mode: bool = ...) -> None: ...

class ChunkFinderValueProto(_message.Message):
    __slots__ = ("blob_snap_tree_node_id", "chunk_file_id", "chunk_column_snap_tree_leaf_node_id", "is_present_in_cm")
    BLOB_SNAP_TREE_NODE_ID_FIELD_NUMBER: _ClassVar[int]
    CHUNK_FILE_ID_FIELD_NUMBER: _ClassVar[int]
    CHUNK_COLUMN_SNAP_TREE_LEAF_NODE_ID_FIELD_NUMBER: _ClassVar[int]
    IS_PRESENT_IN_CM_FIELD_NUMBER: _ClassVar[int]
    blob_snap_tree_node_id: int
    chunk_file_id: int
    chunk_column_snap_tree_leaf_node_id: int
    is_present_in_cm: bool
    def __init__(self, blob_snap_tree_node_id: _Optional[int] = ..., chunk_file_id: _Optional[int] = ..., chunk_column_snap_tree_leaf_node_id: _Optional[int] = ..., is_present_in_cm: bool = ...) -> None: ...
