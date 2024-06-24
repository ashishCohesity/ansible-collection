from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class StatsConfigProto(_message.Message):
    __slots__ = ("time_to_live_secs", "node_stats_schema_name", "node_stats_schema_version", "cluster_stats_schema_name", "cluster_stats_schema_version", "node_stats_schema_description", "node_stats_schema_help_text", "cluster_stats_schema_description", "cluster_stats_schema_help_text", "disk_stats_schema_name", "disk_stats_schema_version", "disk_stats_schema_description", "disk_stats_schema_help_text", "disk_stats_time_to_live_secs", "node_id_attr", "cluster_id_attr", "disk_id_attr")
    class Metric(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kCpuUsagePct: _ClassVar[StatsConfigProto.Metric]
        kMemoryUsagePct: _ClassVar[StatsConfigProto.Metric]
        kDiskAwaitTimeMsecs: _ClassVar[StatsConfigProto.Metric]
    kCpuUsagePct: StatsConfigProto.Metric
    kMemoryUsagePct: StatsConfigProto.Metric
    kDiskAwaitTimeMsecs: StatsConfigProto.Metric
    TIME_TO_LIVE_SECS_FIELD_NUMBER: _ClassVar[int]
    NODE_STATS_SCHEMA_NAME_FIELD_NUMBER: _ClassVar[int]
    NODE_STATS_SCHEMA_VERSION_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_STATS_SCHEMA_NAME_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_STATS_SCHEMA_VERSION_FIELD_NUMBER: _ClassVar[int]
    NODE_STATS_SCHEMA_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    NODE_STATS_SCHEMA_HELP_TEXT_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_STATS_SCHEMA_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_STATS_SCHEMA_HELP_TEXT_FIELD_NUMBER: _ClassVar[int]
    DISK_STATS_SCHEMA_NAME_FIELD_NUMBER: _ClassVar[int]
    DISK_STATS_SCHEMA_VERSION_FIELD_NUMBER: _ClassVar[int]
    DISK_STATS_SCHEMA_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DISK_STATS_SCHEMA_HELP_TEXT_FIELD_NUMBER: _ClassVar[int]
    DISK_STATS_TIME_TO_LIVE_SECS_FIELD_NUMBER: _ClassVar[int]
    NODE_ID_ATTR_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_ATTR_FIELD_NUMBER: _ClassVar[int]
    DISK_ID_ATTR_FIELD_NUMBER: _ClassVar[int]
    time_to_live_secs: int
    node_stats_schema_name: str
    node_stats_schema_version: int
    cluster_stats_schema_name: str
    cluster_stats_schema_version: int
    node_stats_schema_description: str
    node_stats_schema_help_text: str
    cluster_stats_schema_description: str
    cluster_stats_schema_help_text: str
    disk_stats_schema_name: str
    disk_stats_schema_version: int
    disk_stats_schema_description: str
    disk_stats_schema_help_text: str
    disk_stats_time_to_live_secs: int
    node_id_attr: str
    cluster_id_attr: str
    disk_id_attr: str
    def __init__(self, time_to_live_secs: _Optional[int] = ..., node_stats_schema_name: _Optional[str] = ..., node_stats_schema_version: _Optional[int] = ..., cluster_stats_schema_name: _Optional[str] = ..., cluster_stats_schema_version: _Optional[int] = ..., node_stats_schema_description: _Optional[str] = ..., node_stats_schema_help_text: _Optional[str] = ..., cluster_stats_schema_description: _Optional[str] = ..., cluster_stats_schema_help_text: _Optional[str] = ..., disk_stats_schema_name: _Optional[str] = ..., disk_stats_schema_version: _Optional[int] = ..., disk_stats_schema_description: _Optional[str] = ..., disk_stats_schema_help_text: _Optional[str] = ..., disk_stats_time_to_live_secs: _Optional[int] = ..., node_id_attr: _Optional[str] = ..., cluster_id_attr: _Optional[str] = ..., disk_id_attr: _Optional[str] = ...) -> None: ...
