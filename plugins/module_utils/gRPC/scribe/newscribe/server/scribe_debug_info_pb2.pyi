from scribe.newscribe.base import view_config_pb2 as _view_config_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BucketDebugInfo(_message.Message):
    __slots__ = ("bucket_id", "position_in_current_view", "position_in_target_view", "is_operational", "is_leader", "last_known_leader_lock_sequencer", "is_caughtup", "catchup_duration_usecs", "is_last_catchup_quick", "is_catchup_in_progress", "is_migration_in_progress", "compression", "num_range_scan_token_waiters")
    BUCKET_ID_FIELD_NUMBER: _ClassVar[int]
    POSITION_IN_CURRENT_VIEW_FIELD_NUMBER: _ClassVar[int]
    POSITION_IN_TARGET_VIEW_FIELD_NUMBER: _ClassVar[int]
    IS_OPERATIONAL_FIELD_NUMBER: _ClassVar[int]
    IS_LEADER_FIELD_NUMBER: _ClassVar[int]
    LAST_KNOWN_LEADER_LOCK_SEQUENCER_FIELD_NUMBER: _ClassVar[int]
    IS_CAUGHTUP_FIELD_NUMBER: _ClassVar[int]
    CATCHUP_DURATION_USECS_FIELD_NUMBER: _ClassVar[int]
    IS_LAST_CATCHUP_QUICK_FIELD_NUMBER: _ClassVar[int]
    IS_CATCHUP_IN_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    IS_MIGRATION_IN_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    COMPRESSION_FIELD_NUMBER: _ClassVar[int]
    NUM_RANGE_SCAN_TOKEN_WAITERS_FIELD_NUMBER: _ClassVar[int]
    bucket_id: int
    position_in_current_view: int
    position_in_target_view: int
    is_operational: bool
    is_leader: bool
    last_known_leader_lock_sequencer: int
    is_caughtup: bool
    catchup_duration_usecs: int
    is_last_catchup_quick: bool
    is_catchup_in_progress: bool
    is_migration_in_progress: bool
    compression: _view_config_pb2.ViewConfigProto.CompressionType
    num_range_scan_token_waiters: int
    def __init__(self, bucket_id: _Optional[int] = ..., position_in_current_view: _Optional[int] = ..., position_in_target_view: _Optional[int] = ..., is_operational: bool = ..., is_leader: bool = ..., last_known_leader_lock_sequencer: _Optional[int] = ..., is_caughtup: bool = ..., catchup_duration_usecs: _Optional[int] = ..., is_last_catchup_quick: bool = ..., is_catchup_in_progress: bool = ..., is_migration_in_progress: bool = ..., compression: _Optional[_Union[_view_config_pb2.ViewConfigProto.CompressionType, str]] = ..., num_range_scan_token_waiters: _Optional[int] = ...) -> None: ...

class TabletDebugInfo(_message.Message):
    __slots__ = ("tablet_id", "low_mem_usage_setting")
    TABLET_ID_FIELD_NUMBER: _ClassVar[int]
    LOW_MEM_USAGE_SETTING_FIELD_NUMBER: _ClassVar[int]
    tablet_id: int
    low_mem_usage_setting: bool
    def __init__(self, tablet_id: _Optional[int] = ..., low_mem_usage_setting: bool = ...) -> None: ...

class ScribeInstanceDebugInfo(_message.Message):
    __slots__ = ("constituent_id", "disk_id", "db_size", "total_compaction_size", "bucket_vec", "tablet_vec")
    CONSTITUENT_ID_FIELD_NUMBER: _ClassVar[int]
    DISK_ID_FIELD_NUMBER: _ClassVar[int]
    DB_SIZE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_COMPACTION_SIZE_FIELD_NUMBER: _ClassVar[int]
    BUCKET_VEC_FIELD_NUMBER: _ClassVar[int]
    TABLET_VEC_FIELD_NUMBER: _ClassVar[int]
    constituent_id: int
    disk_id: int
    db_size: int
    total_compaction_size: int
    bucket_vec: _containers.RepeatedCompositeFieldContainer[BucketDebugInfo]
    tablet_vec: _containers.RepeatedCompositeFieldContainer[TabletDebugInfo]
    def __init__(self, constituent_id: _Optional[int] = ..., disk_id: _Optional[int] = ..., db_size: _Optional[int] = ..., total_compaction_size: _Optional[int] = ..., bucket_vec: _Optional[_Iterable[_Union[BucketDebugInfo, _Mapping]]] = ..., tablet_vec: _Optional[_Iterable[_Union[TabletDebugInfo, _Mapping]]] = ...) -> None: ...

class ScribeLivenessInfo(_message.Message):
    __slots__ = ("instance_vec",)
    class InstanceLivenessStatus(_message.Message):
        __slots__ = ("constituent_id", "node_id", "disk_id", "is_alive")
        CONSTITUENT_ID_FIELD_NUMBER: _ClassVar[int]
        NODE_ID_FIELD_NUMBER: _ClassVar[int]
        DISK_ID_FIELD_NUMBER: _ClassVar[int]
        IS_ALIVE_FIELD_NUMBER: _ClassVar[int]
        constituent_id: int
        node_id: int
        disk_id: int
        is_alive: bool
        def __init__(self, constituent_id: _Optional[int] = ..., node_id: _Optional[int] = ..., disk_id: _Optional[int] = ..., is_alive: bool = ...) -> None: ...
    INSTANCE_VEC_FIELD_NUMBER: _ClassVar[int]
    instance_vec: _containers.RepeatedCompositeFieldContainer[ScribeLivenessInfo.InstanceLivenessStatus]
    def __init__(self, instance_vec: _Optional[_Iterable[_Union[ScribeLivenessInfo.InstanceLivenessStatus, _Mapping]]] = ...) -> None: ...

class ScribeDebugInfo(_message.Message):
    __slots__ = ("node_id", "node_incarnation_id", "start_time_usecs", "scribe_instance_vec", "liveness_info")
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    NODE_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    SCRIBE_INSTANCE_VEC_FIELD_NUMBER: _ClassVar[int]
    LIVENESS_INFO_FIELD_NUMBER: _ClassVar[int]
    node_id: int
    node_incarnation_id: int
    start_time_usecs: int
    scribe_instance_vec: _containers.RepeatedCompositeFieldContainer[ScribeInstanceDebugInfo]
    liveness_info: ScribeLivenessInfo
    def __init__(self, node_id: _Optional[int] = ..., node_incarnation_id: _Optional[int] = ..., start_time_usecs: _Optional[int] = ..., scribe_instance_vec: _Optional[_Iterable[_Union[ScribeInstanceDebugInfo, _Mapping]]] = ..., liveness_info: _Optional[_Union[ScribeLivenessInfo, _Mapping]] = ...) -> None: ...
