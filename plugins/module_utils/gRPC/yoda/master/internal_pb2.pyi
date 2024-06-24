from magneto.base import magneto_pb2 as _magneto_pb2
from magneto.base import env_params_pb2 as _env_params_pb2
from yoda.util import work_item_pb2 as _work_item_pb2
from yoda.base import reports_pb2 as _reports_pb2
from yoda.base import yoda_pb2 as _yoda_pb2
from yoda.base import yoda_types_pb2 as _yoda_types_pb2
from yoda.db import documents_pb2 as _documents_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ProcessReportWorkItem(_message.Message):
    __slots__ = ("object_id", "report", "progress_monitor_task_path", "update_volume_mapping_monitor")
    WORK_EXT_FIELD_NUMBER: _ClassVar[int]
    work_ext: _descriptor.FieldDescriptor
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    REPORT_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_MONITOR_TASK_PATH_FIELD_NUMBER: _ClassVar[int]
    UPDATE_VOLUME_MAPPING_MONITOR_FIELD_NUMBER: _ClassVar[int]
    object_id: _magneto_pb2.MagnetoObjectId
    report: _reports_pb2.YodaReport
    progress_monitor_task_path: str
    update_volume_mapping_monitor: bool
    def __init__(self, object_id: _Optional[_Union[_magneto_pb2.MagnetoObjectId, _Mapping]] = ..., report: _Optional[_Union[_reports_pb2.YodaReport, _Mapping]] = ..., progress_monitor_task_path: _Optional[str] = ..., update_volume_mapping_monitor: bool = ...) -> None: ...

class MasterProcessingWorkItem(_message.Message):
    __slots__ = ("done",)
    WORK_EXT_FIELD_NUMBER: _ClassVar[int]
    work_ext: _descriptor.FieldDescriptor
    DONE_FIELD_NUMBER: _ClassVar[int]
    done: bool
    def __init__(self, done: bool = ...) -> None: ...

class UpdateReplicasWorkItem(_message.Message):
    __slots__ = ("object_id", "instance_id", "replica_info", "cluster_partition_id", "expire_all_snapshots")
    WORK_EXT_FIELD_NUMBER: _ClassVar[int]
    work_ext: _descriptor.FieldDescriptor
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    REPLICA_INFO_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_PARTITION_ID_FIELD_NUMBER: _ClassVar[int]
    EXPIRE_ALL_SNAPSHOTS_FIELD_NUMBER: _ClassVar[int]
    object_id: _magneto_pb2.MagnetoObjectId
    instance_id: _yoda_types_pb2.MagnetoInstanceId
    replica_info: _yoda_pb2.SnapshotReplicas
    cluster_partition_id: int
    expire_all_snapshots: bool
    def __init__(self, object_id: _Optional[_Union[_magneto_pb2.MagnetoObjectId, _Mapping]] = ..., instance_id: _Optional[_Union[_yoda_types_pb2.MagnetoInstanceId, _Mapping]] = ..., replica_info: _Optional[_Union[_yoda_pb2.SnapshotReplicas, _Mapping]] = ..., cluster_partition_id: _Optional[int] = ..., expire_all_snapshots: bool = ...) -> None: ...

class UpdateIndexingStatusWorkItem(_message.Message):
    __slots__ = ("object_id", "instance_indexing_status_vec")
    class InstanceIndexingStatus(_message.Message):
        __slots__ = ("instance_id", "indexing_status")
        INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
        INDEXING_STATUS_FIELD_NUMBER: _ClassVar[int]
        instance_id: _yoda_types_pb2.MagnetoInstanceId
        indexing_status: _documents_pb2.ObjectSnapshotDocument.VersionInfo.IndexingStatus
        def __init__(self, instance_id: _Optional[_Union[_yoda_types_pb2.MagnetoInstanceId, _Mapping]] = ..., indexing_status: _Optional[_Union[_documents_pb2.ObjectSnapshotDocument.VersionInfo.IndexingStatus, str]] = ...) -> None: ...
    WORK_EXT_FIELD_NUMBER: _ClassVar[int]
    work_ext: _descriptor.FieldDescriptor
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_INDEXING_STATUS_VEC_FIELD_NUMBER: _ClassVar[int]
    object_id: _magneto_pb2.MagnetoObjectId
    instance_indexing_status_vec: _containers.RepeatedCompositeFieldContainer[UpdateIndexingStatusWorkItem.InstanceIndexingStatus]
    def __init__(self, object_id: _Optional[_Union[_magneto_pb2.MagnetoObjectId, _Mapping]] = ..., instance_indexing_status_vec: _Optional[_Iterable[_Union[UpdateIndexingStatusWorkItem.InstanceIndexingStatus, _Mapping]]] = ...) -> None: ...

class FinishIndexingPulseTaskWorkItem(_message.Message):
    __slots__ = ("object_id", "progress_monitor_task_path", "progress_monitor_msg")
    WORK_EXT_FIELD_NUMBER: _ClassVar[int]
    work_ext: _descriptor.FieldDescriptor
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_MONITOR_TASK_PATH_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_MONITOR_MSG_FIELD_NUMBER: _ClassVar[int]
    object_id: _magneto_pb2.MagnetoObjectId
    progress_monitor_task_path: str
    progress_monitor_msg: str
    def __init__(self, object_id: _Optional[_Union[_magneto_pb2.MagnetoObjectId, _Mapping]] = ..., progress_monitor_task_path: _Optional[str] = ..., progress_monitor_msg: _Optional[str] = ...) -> None: ...

class DispatcherState(_message.Message):
    __slots__ = ("slave_dispatcher_blocked", "block_reason", "blocked_time_usecs", "block_all_item_type")
    SLAVE_DISPATCHER_BLOCKED_FIELD_NUMBER: _ClassVar[int]
    BLOCK_REASON_FIELD_NUMBER: _ClassVar[int]
    BLOCKED_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    BLOCK_ALL_ITEM_TYPE_FIELD_NUMBER: _ClassVar[int]
    slave_dispatcher_blocked: bool
    block_reason: str
    blocked_time_usecs: int
    block_all_item_type: bool
    def __init__(self, slave_dispatcher_blocked: bool = ..., block_reason: _Optional[str] = ..., blocked_time_usecs: _Optional[int] = ..., block_all_item_type: bool = ...) -> None: ...

class ComputeStatsWorkItem(_message.Message):
    __slots__ = ("object_id", "instance_id", "base_instance_id", "stat", "cluster_partition_id")
    WORK_EXT_FIELD_NUMBER: _ClassVar[int]
    work_ext: _descriptor.FieldDescriptor
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    BASE_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    STAT_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_PARTITION_ID_FIELD_NUMBER: _ClassVar[int]
    object_id: _magneto_pb2.MagnetoObjectId
    instance_id: _yoda_types_pb2.MagnetoInstanceId
    base_instance_id: _yoda_types_pb2.MagnetoInstanceId
    stat: _yoda_pb2.IndexingMetadataStats
    cluster_partition_id: int
    def __init__(self, object_id: _Optional[_Union[_magneto_pb2.MagnetoObjectId, _Mapping]] = ..., instance_id: _Optional[_Union[_yoda_types_pb2.MagnetoInstanceId, _Mapping]] = ..., base_instance_id: _Optional[_Union[_yoda_types_pb2.MagnetoInstanceId, _Mapping]] = ..., stat: _Optional[_Union[_yoda_pb2.IndexingMetadataStats, _Mapping]] = ..., cluster_partition_id: _Optional[int] = ...) -> None: ...
