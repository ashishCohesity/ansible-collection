from configs import cluster_config_pb2 as _cluster_config_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ViewBoxDeleterContextDataProto(_message.Message):
    __slots__ = ("cluster_config_proto",)
    CLUSTER_CONFIG_PROTO_FIELD_NUMBER: _ClassVar[int]
    cluster_config_proto: _cluster_config_pb2.ClusterConfigProto
    def __init__(self, cluster_config_proto: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto, _Mapping]] = ...) -> None: ...

class ViewBoxDeleterMapKeyProto(_message.Message):
    __slots__ = ("view_box_id",)
    VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
    view_box_id: int
    def __init__(self, view_box_id: _Optional[int] = ...) -> None: ...

class ViewBoxDeleterMapValueProto(_message.Message):
    __slots__ = ("is_referenced",)
    IS_REFERENCED_FIELD_NUMBER: _ClassVar[int]
    is_referenced: bool
    def __init__(self, is_referenced: bool = ...) -> None: ...
