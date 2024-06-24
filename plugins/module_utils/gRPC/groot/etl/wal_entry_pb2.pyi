from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EtlWALEntry(_message.Message):
    __slots__ = ("cluster_etl_state", "stats_etl_state", "magneto_etl_state")
    class ClusterEtlState(_message.Message):
        __slots__ = ("last_update_time_secs",)
        LAST_UPDATE_TIME_SECS_FIELD_NUMBER: _ClassVar[int]
        last_update_time_secs: int
        def __init__(self, last_update_time_secs: _Optional[int] = ...) -> None: ...
    class StatsEtlState(_message.Message):
        __slots__ = ("last_io_performance_stats_fetch_time_secs", "last_resource_usage_stats_fetch_time_secs", "last_storage_usage_stats_fetch_time_secs")
        LAST_IO_PERFORMANCE_STATS_FETCH_TIME_SECS_FIELD_NUMBER: _ClassVar[int]
        LAST_RESOURCE_USAGE_STATS_FETCH_TIME_SECS_FIELD_NUMBER: _ClassVar[int]
        LAST_STORAGE_USAGE_STATS_FETCH_TIME_SECS_FIELD_NUMBER: _ClassVar[int]
        last_io_performance_stats_fetch_time_secs: int
        last_resource_usage_stats_fetch_time_secs: int
        last_storage_usage_stats_fetch_time_secs: int
        def __init__(self, last_io_performance_stats_fetch_time_secs: _Optional[int] = ..., last_resource_usage_stats_fetch_time_secs: _Optional[int] = ..., last_storage_usage_stats_fetch_time_secs: _Optional[int] = ...) -> None: ...
    class MagnetoEtlState(_message.Message):
        __slots__ = ("last_run_start_time_map", "last_restored_objects_update_time_secs", "last_data_fetch_time_secs", "should_trigger_fullsync")
        class LastRunStartTimeMapEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: int
            value: int
            def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
        LAST_RUN_START_TIME_MAP_FIELD_NUMBER: _ClassVar[int]
        LAST_RESTORED_OBJECTS_UPDATE_TIME_SECS_FIELD_NUMBER: _ClassVar[int]
        LAST_DATA_FETCH_TIME_SECS_FIELD_NUMBER: _ClassVar[int]
        SHOULD_TRIGGER_FULLSYNC_FIELD_NUMBER: _ClassVar[int]
        last_run_start_time_map: _containers.ScalarMap[int, int]
        last_restored_objects_update_time_secs: int
        last_data_fetch_time_secs: int
        should_trigger_fullsync: bool
        def __init__(self, last_run_start_time_map: _Optional[_Mapping[int, int]] = ..., last_restored_objects_update_time_secs: _Optional[int] = ..., last_data_fetch_time_secs: _Optional[int] = ..., should_trigger_fullsync: bool = ...) -> None: ...
    CLUSTER_ETL_STATE_FIELD_NUMBER: _ClassVar[int]
    STATS_ETL_STATE_FIELD_NUMBER: _ClassVar[int]
    MAGNETO_ETL_STATE_FIELD_NUMBER: _ClassVar[int]
    cluster_etl_state: EtlWALEntry.ClusterEtlState
    stats_etl_state: EtlWALEntry.StatsEtlState
    magneto_etl_state: EtlWALEntry.MagnetoEtlState
    def __init__(self, cluster_etl_state: _Optional[_Union[EtlWALEntry.ClusterEtlState, _Mapping]] = ..., stats_etl_state: _Optional[_Union[EtlWALEntry.StatsEtlState, _Mapping]] = ..., magneto_etl_state: _Optional[_Union[EtlWALEntry.MagnetoEtlState, _Mapping]] = ...) -> None: ...
