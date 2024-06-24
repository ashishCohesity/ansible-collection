from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BlurUsageStatsProto(_message.Message):
    __slots__ = ("node_id", "num_blobs", "view_usage_vec", "view_box_usage_vec", "disk_usage_vec")
    class BlurViewUsageStatsProto(_message.Message):
        __slots__ = ("view_id", "usage_bytes", "num_epochs")
        VIEW_ID_FIELD_NUMBER: _ClassVar[int]
        USAGE_BYTES_FIELD_NUMBER: _ClassVar[int]
        NUM_EPOCHS_FIELD_NUMBER: _ClassVar[int]
        view_id: int
        usage_bytes: int
        num_epochs: int
        def __init__(self, view_id: _Optional[int] = ..., usage_bytes: _Optional[int] = ..., num_epochs: _Optional[int] = ...) -> None: ...
    class BlurViewBoxUsageStatsProto(_message.Message):
        __slots__ = ("view_box_id", "used_bytes", "num_epochs")
        VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
        USED_BYTES_FIELD_NUMBER: _ClassVar[int]
        NUM_EPOCHS_FIELD_NUMBER: _ClassVar[int]
        view_box_id: int
        used_bytes: int
        num_epochs: int
        def __init__(self, view_box_id: _Optional[int] = ..., used_bytes: _Optional[int] = ..., num_epochs: _Optional[int] = ...) -> None: ...
    class BlurDiskUsageStatsProto(_message.Message):
        __slots__ = ("disk_id", "usage_bytes", "num_epochs")
        DISK_ID_FIELD_NUMBER: _ClassVar[int]
        USAGE_BYTES_FIELD_NUMBER: _ClassVar[int]
        NUM_EPOCHS_FIELD_NUMBER: _ClassVar[int]
        disk_id: int
        usage_bytes: int
        num_epochs: int
        def __init__(self, disk_id: _Optional[int] = ..., usage_bytes: _Optional[int] = ..., num_epochs: _Optional[int] = ...) -> None: ...
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    NUM_BLOBS_FIELD_NUMBER: _ClassVar[int]
    VIEW_USAGE_VEC_FIELD_NUMBER: _ClassVar[int]
    VIEW_BOX_USAGE_VEC_FIELD_NUMBER: _ClassVar[int]
    DISK_USAGE_VEC_FIELD_NUMBER: _ClassVar[int]
    node_id: int
    num_blobs: int
    view_usage_vec: _containers.RepeatedCompositeFieldContainer[BlurUsageStatsProto.BlurViewUsageStatsProto]
    view_box_usage_vec: _containers.RepeatedCompositeFieldContainer[BlurUsageStatsProto.BlurViewBoxUsageStatsProto]
    disk_usage_vec: _containers.RepeatedCompositeFieldContainer[BlurUsageStatsProto.BlurDiskUsageStatsProto]
    def __init__(self, node_id: _Optional[int] = ..., num_blobs: _Optional[int] = ..., view_usage_vec: _Optional[_Iterable[_Union[BlurUsageStatsProto.BlurViewUsageStatsProto, _Mapping]]] = ..., view_box_usage_vec: _Optional[_Iterable[_Union[BlurUsageStatsProto.BlurViewBoxUsageStatsProto, _Mapping]]] = ..., disk_usage_vec: _Optional[_Iterable[_Union[BlurUsageStatsProto.BlurDiskUsageStatsProto, _Mapping]]] = ...) -> None: ...
