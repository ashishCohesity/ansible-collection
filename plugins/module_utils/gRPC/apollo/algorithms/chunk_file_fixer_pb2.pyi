from configs import cluster_config_pb2 as _cluster_config_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ChunkFileFixerContextDataProto(_message.Message):
    __slots__ = ("cluster_config_proto", "num_constituents")
    CLUSTER_CONFIG_PROTO_FIELD_NUMBER: _ClassVar[int]
    NUM_CONSTITUENTS_FIELD_NUMBER: _ClassVar[int]
    cluster_config_proto: _cluster_config_pb2.ClusterConfigProto
    num_constituents: int
    def __init__(self, cluster_config_proto: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto, _Mapping]] = ..., num_constituents: _Optional[int] = ...) -> None: ...
