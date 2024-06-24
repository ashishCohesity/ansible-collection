from bridge.stats import bridge_stats_config_pb2 as _bridge_stats_config_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DiskStatProto(_message.Message):
    __slots__ = ("disk_id", "is_cloud_disk", "expected_available", "session_id", "sequence_id", "metric_vec")
    class MetricValue(_message.Message):
        __slots__ = ("metric_id", "value")
        METRIC_ID_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        metric_id: _bridge_stats_config_pb2.BridgeStatsConfigProto.Metric
        value: int
        def __init__(self, metric_id: _Optional[_Union[_bridge_stats_config_pb2.BridgeStatsConfigProto.Metric, str]] = ..., value: _Optional[int] = ...) -> None: ...
    DISK_ID_FIELD_NUMBER: _ClassVar[int]
    IS_CLOUD_DISK_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    SEQUENCE_ID_FIELD_NUMBER: _ClassVar[int]
    METRIC_VEC_FIELD_NUMBER: _ClassVar[int]
    disk_id: int
    is_cloud_disk: bool
    expected_available: int
    session_id: int
    sequence_id: int
    metric_vec: _containers.RepeatedCompositeFieldContainer[DiskStatProto.MetricValue]
    def __init__(self, disk_id: _Optional[int] = ..., is_cloud_disk: bool = ..., expected_available: _Optional[int] = ..., session_id: _Optional[int] = ..., sequence_id: _Optional[int] = ..., metric_vec: _Optional[_Iterable[_Union[DiskStatProto.MetricValue, _Mapping]]] = ...) -> None: ...
