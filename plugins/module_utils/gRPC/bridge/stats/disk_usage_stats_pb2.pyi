from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DiskUsageStatsProto(_message.Message):
    __slots__ = ("view_box_vec", "garbage", "total", "system_usage", "system_capacity")
    class Usage(_message.Message):
        __slots__ = ("unmorphed", "morphed")
        UNMORPHED_FIELD_NUMBER: _ClassVar[int]
        MORPHED_FIELD_NUMBER: _ClassVar[int]
        unmorphed: int
        morphed: int
        def __init__(self, unmorphed: _Optional[int] = ..., morphed: _Optional[int] = ...) -> None: ...
    class ViewBox(_message.Message):
        __slots__ = ("view_box_id", "dedup", "non_dedup", "garbage")
        VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
        DEDUP_FIELD_NUMBER: _ClassVar[int]
        NON_DEDUP_FIELD_NUMBER: _ClassVar[int]
        GARBAGE_FIELD_NUMBER: _ClassVar[int]
        view_box_id: int
        dedup: DiskUsageStatsProto.Usage
        non_dedup: DiskUsageStatsProto.Usage
        garbage: DiskUsageStatsProto.Usage
        def __init__(self, view_box_id: _Optional[int] = ..., dedup: _Optional[_Union[DiskUsageStatsProto.Usage, _Mapping]] = ..., non_dedup: _Optional[_Union[DiskUsageStatsProto.Usage, _Mapping]] = ..., garbage: _Optional[_Union[DiskUsageStatsProto.Usage, _Mapping]] = ...) -> None: ...
    VIEW_BOX_VEC_FIELD_NUMBER: _ClassVar[int]
    GARBAGE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_USAGE_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_CAPACITY_FIELD_NUMBER: _ClassVar[int]
    view_box_vec: _containers.RepeatedCompositeFieldContainer[DiskUsageStatsProto.ViewBox]
    garbage: DiskUsageStatsProto.Usage
    total: DiskUsageStatsProto.Usage
    system_usage: int
    system_capacity: int
    def __init__(self, view_box_vec: _Optional[_Iterable[_Union[DiskUsageStatsProto.ViewBox, _Mapping]]] = ..., garbage: _Optional[_Union[DiskUsageStatsProto.Usage, _Mapping]] = ..., total: _Optional[_Union[DiskUsageStatsProto.Usage, _Mapping]] = ..., system_usage: _Optional[int] = ..., system_capacity: _Optional[int] = ...) -> None: ...
