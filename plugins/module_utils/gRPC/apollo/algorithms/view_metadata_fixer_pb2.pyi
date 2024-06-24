from configs import cluster_config_pb2 as _cluster_config_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ViewMetadataFixerContextDataProto(_message.Message):
    __slots__ = ("cluster_config_proto",)
    CLUSTER_CONFIG_PROTO_FIELD_NUMBER: _ClassVar[int]
    cluster_config_proto: _cluster_config_pb2.ClusterConfigProto
    def __init__(self, cluster_config_proto: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto, _Mapping]] = ...) -> None: ...

class ViewMetadataFixerMapKeyProto(_message.Message):
    __slots__ = ("view_id",)
    VIEW_ID_FIELD_NUMBER: _ClassVar[int]
    view_id: int
    def __init__(self, view_id: _Optional[int] = ...) -> None: ...

class ViewIdInfo(_message.Message):
    __slots__ = ("op_in_progress", "view_box_id", "update_intent_present")
    OP_IN_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
    UPDATE_INTENT_PRESENT_FIELD_NUMBER: _ClassVar[int]
    op_in_progress: bool
    view_box_id: int
    update_intent_present: bool
    def __init__(self, op_in_progress: bool = ..., view_box_id: _Optional[int] = ..., update_intent_present: bool = ...) -> None: ...

class ViewNameInfo(_message.Message):
    __slots__ = ("view_name", "op_in_progress")
    VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    OP_IN_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    view_name: bytes
    op_in_progress: bool
    def __init__(self, view_name: _Optional[bytes] = ..., op_in_progress: bool = ...) -> None: ...

class ViewMetadataFixerMapValueProto(_message.Message):
    __slots__ = ("view_name_info", "view_id_info")
    VIEW_NAME_INFO_FIELD_NUMBER: _ClassVar[int]
    VIEW_ID_INFO_FIELD_NUMBER: _ClassVar[int]
    view_name_info: ViewNameInfo
    view_id_info: ViewIdInfo
    def __init__(self, view_name_info: _Optional[_Union[ViewNameInfo, _Mapping]] = ..., view_id_info: _Optional[_Union[ViewIdInfo, _Mapping]] = ...) -> None: ...

class ViewMetadataFixerRunningResultProto(_message.Message):
    __slots__ = ("view_name_info", "view_id_info", "num_aliases", "op_in_progress")
    VIEW_NAME_INFO_FIELD_NUMBER: _ClassVar[int]
    VIEW_ID_INFO_FIELD_NUMBER: _ClassVar[int]
    NUM_ALIASES_FIELD_NUMBER: _ClassVar[int]
    OP_IN_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    view_name_info: ViewNameInfo
    view_id_info: ViewIdInfo
    num_aliases: int
    op_in_progress: bool
    def __init__(self, view_name_info: _Optional[_Union[ViewNameInfo, _Mapping]] = ..., view_id_info: _Optional[_Union[ViewIdInfo, _Mapping]] = ..., num_aliases: _Optional[int] = ..., op_in_progress: bool = ...) -> None: ...
