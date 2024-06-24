from configs import cluster_config_pb2 as _cluster_config_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BrickFragmentationContextDataProto(_message.Message):
    __slots__ = ("cluster_config_proto",)
    CLUSTER_CONFIG_PROTO_FIELD_NUMBER: _ClassVar[int]
    cluster_config_proto: _cluster_config_pb2.ClusterConfigProto
    def __init__(self, cluster_config_proto: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto, _Mapping]] = ...) -> None: ...

class BrickFragmentationMapValueProto(_message.Message):
    __slots__ = ("node_id", "stripe_col", "chunk_file_id", "view_box_id")
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    STRIPE_COL_FIELD_NUMBER: _ClassVar[int]
    CHUNK_FILE_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
    node_id: int
    stripe_col: int
    chunk_file_id: int
    view_box_id: int
    def __init__(self, node_id: _Optional[int] = ..., stripe_col: _Optional[int] = ..., chunk_file_id: _Optional[int] = ..., view_box_id: _Optional[int] = ...) -> None: ...
