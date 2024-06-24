from qa.lib.cohesityConnector.base import perf_stats_pb2 as _perf_stats_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Result(_message.Message):
    __slots__ = ("result_start_time_usecs", "result_end_time_usecs", "num_objects_backedup", "num_failed_objects_backedup", "num_successful_objects_backedup", "vms_backup_stats", "total_bytes_read_from_source", "total_physical_bytes_written", "total_logical_bytes_written", "magneto_source_stats", "magneto_cluster_stats", "bridge_cluster_stats", "bridge_node_stats", "bridge_viewbox_stats")
    RESULT_START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    RESULT_END_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    NUM_OBJECTS_BACKEDUP_FIELD_NUMBER: _ClassVar[int]
    NUM_FAILED_OBJECTS_BACKEDUP_FIELD_NUMBER: _ClassVar[int]
    NUM_SUCCESSFUL_OBJECTS_BACKEDUP_FIELD_NUMBER: _ClassVar[int]
    VMS_BACKUP_STATS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_BYTES_READ_FROM_SOURCE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_PHYSICAL_BYTES_WRITTEN_FIELD_NUMBER: _ClassVar[int]
    TOTAL_LOGICAL_BYTES_WRITTEN_FIELD_NUMBER: _ClassVar[int]
    MAGNETO_SOURCE_STATS_FIELD_NUMBER: _ClassVar[int]
    MAGNETO_CLUSTER_STATS_FIELD_NUMBER: _ClassVar[int]
    BRIDGE_CLUSTER_STATS_FIELD_NUMBER: _ClassVar[int]
    BRIDGE_NODE_STATS_FIELD_NUMBER: _ClassVar[int]
    BRIDGE_VIEWBOX_STATS_FIELD_NUMBER: _ClassVar[int]
    result_start_time_usecs: int
    result_end_time_usecs: int
    num_objects_backedup: int
    num_failed_objects_backedup: int
    num_successful_objects_backedup: int
    vms_backup_stats: _containers.RepeatedCompositeFieldContainer[_perf_stats_pb2.VMBackupStats]
    total_bytes_read_from_source: int
    total_physical_bytes_written: int
    total_logical_bytes_written: int
    magneto_source_stats: _containers.RepeatedCompositeFieldContainer[_perf_stats_pb2.MagnetoEntityPerfStats]
    magneto_cluster_stats: _perf_stats_pb2.MagnetoEntityPerfStats
    bridge_cluster_stats: _perf_stats_pb2.BridgeEntityPerfStats
    bridge_node_stats: _containers.RepeatedCompositeFieldContainer[_perf_stats_pb2.BridgeEntityPerfStats]
    bridge_viewbox_stats: _containers.RepeatedCompositeFieldContainer[_perf_stats_pb2.BridgeEntityPerfStats]
    def __init__(self, result_start_time_usecs: _Optional[int] = ..., result_end_time_usecs: _Optional[int] = ..., num_objects_backedup: _Optional[int] = ..., num_failed_objects_backedup: _Optional[int] = ..., num_successful_objects_backedup: _Optional[int] = ..., vms_backup_stats: _Optional[_Iterable[_Union[_perf_stats_pb2.VMBackupStats, _Mapping]]] = ..., total_bytes_read_from_source: _Optional[int] = ..., total_physical_bytes_written: _Optional[int] = ..., total_logical_bytes_written: _Optional[int] = ..., magneto_source_stats: _Optional[_Iterable[_Union[_perf_stats_pb2.MagnetoEntityPerfStats, _Mapping]]] = ..., magneto_cluster_stats: _Optional[_Union[_perf_stats_pb2.MagnetoEntityPerfStats, _Mapping]] = ..., bridge_cluster_stats: _Optional[_Union[_perf_stats_pb2.BridgeEntityPerfStats, _Mapping]] = ..., bridge_node_stats: _Optional[_Iterable[_Union[_perf_stats_pb2.BridgeEntityPerfStats, _Mapping]]] = ..., bridge_viewbox_stats: _Optional[_Iterable[_Union[_perf_stats_pb2.BridgeEntityPerfStats, _Mapping]]] = ...) -> None: ...
