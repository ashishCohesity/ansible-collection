from configs import cluster_config_pb2 as _cluster_config_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ViewUsageCleanerContextDataProto(_message.Message):
    __slots__ = ("cluster_config_proto",)
    CLUSTER_CONFIG_PROTO_FIELD_NUMBER: _ClassVar[int]
    cluster_config_proto: _cluster_config_pb2.ClusterConfigProto
    def __init__(self, cluster_config_proto: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto, _Mapping]] = ...) -> None: ...

class ViewUsageCleanerMapKeyProto(_message.Message):
    __slots__ = ("view_id",)
    VIEW_ID_FIELD_NUMBER: _ClassVar[int]
    view_id: int
    def __init__(self, view_id: _Optional[int] = ...) -> None: ...

class ViewUsageCleanerMapValueProto(_message.Message):
    __slots__ = ("in_view_usage", "in_view_metadata", "scribe_row_version", "in_stats")
    IN_VIEW_USAGE_FIELD_NUMBER: _ClassVar[int]
    IN_VIEW_METADATA_FIELD_NUMBER: _ClassVar[int]
    SCRIBE_ROW_VERSION_FIELD_NUMBER: _ClassVar[int]
    IN_STATS_FIELD_NUMBER: _ClassVar[int]
    in_view_usage: bool
    in_view_metadata: bool
    scribe_row_version: int
    in_stats: bool
    def __init__(self, in_view_usage: bool = ..., in_view_metadata: bool = ..., scribe_row_version: _Optional[int] = ..., in_stats: bool = ...) -> None: ...
