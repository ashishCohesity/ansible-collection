from apollo.mr.base import histogram_proto_pb2 as _histogram_proto_pb2
from configs import cluster_config_pb2 as _cluster_config_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class InodeStatsContextDataProto(_message.Message):
    __slots__ = ("cluster_config_proto", "max_view_snaptree_level", "extension_vec", "apollo_mr_enable_apollo_binary_logging")
    CLUSTER_CONFIG_PROTO_FIELD_NUMBER: _ClassVar[int]
    MAX_VIEW_SNAPTREE_LEVEL_FIELD_NUMBER: _ClassVar[int]
    EXTENSION_VEC_FIELD_NUMBER: _ClassVar[int]
    APOLLO_MR_ENABLE_APOLLO_BINARY_LOGGING_FIELD_NUMBER: _ClassVar[int]
    cluster_config_proto: _cluster_config_pb2.ClusterConfigProto
    max_view_snaptree_level: int
    extension_vec: _containers.RepeatedScalarFieldContainer[str]
    apollo_mr_enable_apollo_binary_logging: bool
    def __init__(self, cluster_config_proto: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto, _Mapping]] = ..., max_view_snaptree_level: _Optional[int] = ..., extension_vec: _Optional[_Iterable[str]] = ..., apollo_mr_enable_apollo_binary_logging: bool = ...) -> None: ...

class InodeStatsKeyProto(_message.Message):
    __slots__ = ("node_id", "inode_id", "view_id", "view_box_id")
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    INODE_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
    node_id: int
    inode_id: int
    view_id: int
    view_box_id: int
    def __init__(self, node_id: _Optional[int] = ..., inode_id: _Optional[int] = ..., view_id: _Optional[int] = ..., view_box_id: _Optional[int] = ...) -> None: ...

class InodeStatsValueProto(_message.Message):
    __slots__ = ("view_id_vec", "child_node_id", "inode_id", "logical_size", "extension", "view_box_id")
    VIEW_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    CHILD_NODE_ID_FIELD_NUMBER: _ClassVar[int]
    INODE_ID_FIELD_NUMBER: _ClassVar[int]
    LOGICAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    EXTENSION_FIELD_NUMBER: _ClassVar[int]
    VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
    view_id_vec: _containers.RepeatedScalarFieldContainer[int]
    child_node_id: int
    inode_id: int
    logical_size: int
    extension: str
    view_box_id: int
    def __init__(self, view_id_vec: _Optional[_Iterable[int]] = ..., child_node_id: _Optional[int] = ..., inode_id: _Optional[int] = ..., logical_size: _Optional[int] = ..., extension: _Optional[str] = ..., view_box_id: _Optional[int] = ...) -> None: ...

class InodeInfoProto(_message.Message):
    __slots__ = ("viewbox_id", "physical_size")
    VIEWBOX_ID_FIELD_NUMBER: _ClassVar[int]
    PHYSICAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    viewbox_id: int
    physical_size: int
    def __init__(self, viewbox_id: _Optional[int] = ..., physical_size: _Optional[int] = ...) -> None: ...

class ViewBoxLogicalStatsProto(_message.Message):
    __slots__ = ("cumulative_logical_size", "mega_file_inode_stats", "total_inode_stats", "num_directories")
    CUMULATIVE_LOGICAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    MEGA_FILE_INODE_STATS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_INODE_STATS_FIELD_NUMBER: _ClassVar[int]
    NUM_DIRECTORIES_FIELD_NUMBER: _ClassVar[int]
    cumulative_logical_size: int
    mega_file_inode_stats: _histogram_proto_pb2.HistogramProto
    total_inode_stats: _histogram_proto_pb2.HistogramProto
    num_directories: int
    def __init__(self, cumulative_logical_size: _Optional[int] = ..., mega_file_inode_stats: _Optional[_Union[_histogram_proto_pb2.HistogramProto, _Mapping]] = ..., total_inode_stats: _Optional[_Union[_histogram_proto_pb2.HistogramProto, _Mapping]] = ..., num_directories: _Optional[int] = ...) -> None: ...
