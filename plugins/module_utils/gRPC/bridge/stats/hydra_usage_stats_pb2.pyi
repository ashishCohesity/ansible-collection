from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HydraUsageStatsProto(_message.Message):
    __slots__ = ("node_id", "num_blobs", "disk_usage_vec", "view_box_usage_vec")
    class HydraDiskUsageStatsProto(_message.Message):
        __slots__ = ("disk_id", "usage_bytes", "capacity_bytes", "num_epochs")
        DISK_ID_FIELD_NUMBER: _ClassVar[int]
        USAGE_BYTES_FIELD_NUMBER: _ClassVar[int]
        CAPACITY_BYTES_FIELD_NUMBER: _ClassVar[int]
        NUM_EPOCHS_FIELD_NUMBER: _ClassVar[int]
        disk_id: int
        usage_bytes: int
        capacity_bytes: int
        num_epochs: int
        def __init__(self, disk_id: _Optional[int] = ..., usage_bytes: _Optional[int] = ..., capacity_bytes: _Optional[int] = ..., num_epochs: _Optional[int] = ...) -> None: ...
    class HydraViewBoxUsageStatsProto(_message.Message):
        __slots__ = ("view_box_id", "used_bytes", "num_epochs")
        VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
        USED_BYTES_FIELD_NUMBER: _ClassVar[int]
        NUM_EPOCHS_FIELD_NUMBER: _ClassVar[int]
        view_box_id: int
        used_bytes: int
        num_epochs: int
        def __init__(self, view_box_id: _Optional[int] = ..., used_bytes: _Optional[int] = ..., num_epochs: _Optional[int] = ...) -> None: ...
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    NUM_BLOBS_FIELD_NUMBER: _ClassVar[int]
    DISK_USAGE_VEC_FIELD_NUMBER: _ClassVar[int]
    VIEW_BOX_USAGE_VEC_FIELD_NUMBER: _ClassVar[int]
    node_id: int
    num_blobs: int
    disk_usage_vec: _containers.RepeatedCompositeFieldContainer[HydraUsageStatsProto.HydraDiskUsageStatsProto]
    view_box_usage_vec: _containers.RepeatedCompositeFieldContainer[HydraUsageStatsProto.HydraViewBoxUsageStatsProto]
    def __init__(self, node_id: _Optional[int] = ..., num_blobs: _Optional[int] = ..., disk_usage_vec: _Optional[_Iterable[_Union[HydraUsageStatsProto.HydraDiskUsageStatsProto, _Mapping]]] = ..., view_box_usage_vec: _Optional[_Iterable[_Union[HydraUsageStatsProto.HydraViewBoxUsageStatsProto, _Mapping]]] = ...) -> None: ...
