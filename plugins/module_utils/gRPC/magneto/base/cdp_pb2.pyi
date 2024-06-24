from atom.base import atom_pb2 as _atom_pb2
from atom.base import event_pb2 as _event_pb2
from magneto.base import disk_pb2 as _disk_pb2
from magneto.base import error_pb2 as _error_pb2
from magneto.base import magneto_pb2 as _magneto_pb2
from magneto.base import env_params_pb2 as _env_params_pb2
from magneto.base import sub_task_pb2 as _sub_task_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class VirtualDiskInfo(_message.Message):
    __slots__ = ("file_path", "uuid", "last_seq_number")
    FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    LAST_SEQ_NUMBER_FIELD_NUMBER: _ClassVar[int]
    file_path: str
    uuid: str
    last_seq_number: _event_pb2.Sequencer
    def __init__(self, file_path: _Optional[str] = ..., uuid: _Optional[str] = ..., last_seq_number: _Optional[_Union[_event_pb2.Sequencer, _Mapping]] = ...) -> None: ...

class RestoreInfo(_message.Message):
    __slots__ = ("status", "cdp_restore_params", "virtual_disks", "hydration_info")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kStarted: _ClassVar[RestoreInfo.Status]
        kFilesCloned: _ClassVar[RestoreInfo.Status]
        kFinished: _ClassVar[RestoreInfo.Status]
        kViewCreated: _ClassVar[RestoreInfo.Status]
    kStarted: RestoreInfo.Status
    kFilesCloned: RestoreInfo.Status
    kFinished: RestoreInfo.Status
    kViewCreated: RestoreInfo.Status
    CDP_RESTORE_INFO_FIELD_NUMBER: _ClassVar[int]
    cdp_restore_info: _descriptor.FieldDescriptor
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CDP_RESTORE_PARAMS_FIELD_NUMBER: _ClassVar[int]
    VIRTUAL_DISKS_FIELD_NUMBER: _ClassVar[int]
    HYDRATION_INFO_FIELD_NUMBER: _ClassVar[int]
    status: RestoreInfo.Status
    cdp_restore_params: _magneto_pb2.CDPRestoreParams
    virtual_disks: _containers.RepeatedCompositeFieldContainer[VirtualDiskInfo]
    hydration_info: HydrationInfo
    def __init__(self, status: _Optional[_Union[RestoreInfo.Status, str]] = ..., cdp_restore_params: _Optional[_Union[_magneto_pb2.CDPRestoreParams, _Mapping]] = ..., virtual_disks: _Optional[_Iterable[_Union[VirtualDiskInfo, _Mapping]]] = ..., hydration_info: _Optional[_Union[HydrationInfo, _Mapping]] = ...) -> None: ...

class HydrationInfo(_message.Message):
    __slots__ = ("status", "sub_tasks_vec", "hydration_time_usecs", "error")
    class TaskStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kStarted: _ClassVar[HydrationInfo.TaskStatus]
        kPermitGranted: _ClassVar[HydrationInfo.TaskStatus]
        kBackupFilesCloned: _ClassVar[HydrationInfo.TaskStatus]
        kSubTasksCreated: _ClassVar[HydrationInfo.TaskStatus]
        kSubTasksDone: _ClassVar[HydrationInfo.TaskStatus]
    kStarted: HydrationInfo.TaskStatus
    kPermitGranted: HydrationInfo.TaskStatus
    kBackupFilesCloned: HydrationInfo.TaskStatus
    kSubTasksCreated: HydrationInfo.TaskStatus
    kSubTasksDone: HydrationInfo.TaskStatus
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SUB_TASKS_VEC_FIELD_NUMBER: _ClassVar[int]
    HYDRATION_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    status: HydrationInfo.TaskStatus
    sub_tasks_vec: _containers.RepeatedCompositeFieldContainer[_sub_task_pb2.SubTaskInfo]
    hydration_time_usecs: int
    error: _error_pb2.ErrorProto
    def __init__(self, status: _Optional[_Union[HydrationInfo.TaskStatus, str]] = ..., sub_tasks_vec: _Optional[_Iterable[_Union[_sub_task_pb2.SubTaskInfo, _Mapping]]] = ..., hydration_time_usecs: _Optional[int] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class CDPSubTaskInfo(_message.Message):
    __slots__ = ("hydrated_disk_idx", "start_time_usecs", "end_time_usecs", "progress_monitor_path", "last_applied_seq_num", "total_bytes_read_from_source")
    CDP_SUB_TASK_INFO_FIELD_NUMBER: _ClassVar[int]
    cdp_sub_task_info: _descriptor.FieldDescriptor
    HYDRATED_DISK_IDX_FIELD_NUMBER: _ClassVar[int]
    START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    END_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_MONITOR_PATH_FIELD_NUMBER: _ClassVar[int]
    LAST_APPLIED_SEQ_NUM_FIELD_NUMBER: _ClassVar[int]
    TOTAL_BYTES_READ_FROM_SOURCE_FIELD_NUMBER: _ClassVar[int]
    hydrated_disk_idx: int
    start_time_usecs: int
    end_time_usecs: int
    progress_monitor_path: str
    last_applied_seq_num: _event_pb2.Sequencer
    total_bytes_read_from_source: int
    def __init__(self, hydrated_disk_idx: _Optional[int] = ..., start_time_usecs: _Optional[int] = ..., end_time_usecs: _Optional[int] = ..., progress_monitor_path: _Optional[str] = ..., last_applied_seq_num: _Optional[_Union[_event_pb2.Sequencer, _Mapping]] = ..., total_bytes_read_from_source: _Optional[int] = ...) -> None: ...

class SnapshotInfo(_message.Message):
    __slots__ = ("hydration_status", "hydrated_disks_vec", "hydration_time_usecs", "hydration_info", "epoch_vec", "max_hydration_time_usecs")
    class HydrationStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kStarted: _ClassVar[SnapshotInfo.HydrationStatus]
        kPermitGranted: _ClassVar[SnapshotInfo.HydrationStatus]
        kBackupFilesCloned: _ClassVar[SnapshotInfo.HydrationStatus]
        kLogsCloned: _ClassVar[SnapshotInfo.HydrationStatus]
        kHydrationFinished: _ClassVar[SnapshotInfo.HydrationStatus]
        kLogsRemoved: _ClassVar[SnapshotInfo.HydrationStatus]
        kFinished: _ClassVar[SnapshotInfo.HydrationStatus]
    kStarted: SnapshotInfo.HydrationStatus
    kPermitGranted: SnapshotInfo.HydrationStatus
    kBackupFilesCloned: SnapshotInfo.HydrationStatus
    kLogsCloned: SnapshotInfo.HydrationStatus
    kHydrationFinished: SnapshotInfo.HydrationStatus
    kLogsRemoved: SnapshotInfo.HydrationStatus
    kFinished: SnapshotInfo.HydrationStatus
    class VirtualDisk(_message.Message):
        __slots__ = ("file_name", "uuid", "applied_log_file_vec", "last_seq_number", "is_deleted", "data_events_vec", "total_bytes_read_from_source")
        CDP_VIRTUAL_DISK_FIELD_NUMBER: _ClassVar[int]
        cdp_virtual_disk: _descriptor.FieldDescriptor
        FILE_NAME_FIELD_NUMBER: _ClassVar[int]
        UUID_FIELD_NUMBER: _ClassVar[int]
        APPLIED_LOG_FILE_VEC_FIELD_NUMBER: _ClassVar[int]
        LAST_SEQ_NUMBER_FIELD_NUMBER: _ClassVar[int]
        IS_DELETED_FIELD_NUMBER: _ClassVar[int]
        DATA_EVENTS_VEC_FIELD_NUMBER: _ClassVar[int]
        TOTAL_BYTES_READ_FROM_SOURCE_FIELD_NUMBER: _ClassVar[int]
        file_name: str
        uuid: str
        applied_log_file_vec: _containers.RepeatedScalarFieldContainer[str]
        last_seq_number: _event_pb2.Sequencer
        is_deleted: bool
        data_events_vec: _containers.RepeatedCompositeFieldContainer[_event_pb2.DataEvent]
        total_bytes_read_from_source: int
        def __init__(self, file_name: _Optional[str] = ..., uuid: _Optional[str] = ..., applied_log_file_vec: _Optional[_Iterable[str]] = ..., last_seq_number: _Optional[_Union[_event_pb2.Sequencer, _Mapping]] = ..., is_deleted: bool = ..., data_events_vec: _Optional[_Iterable[_Union[_event_pb2.DataEvent, _Mapping]]] = ..., total_bytes_read_from_source: _Optional[int] = ...) -> None: ...
    CDP_SNAPSHOT_INFO_FIELD_NUMBER: _ClassVar[int]
    cdp_snapshot_info: _descriptor.FieldDescriptor
    HYDRATION_STATUS_FIELD_NUMBER: _ClassVar[int]
    HYDRATED_DISKS_VEC_FIELD_NUMBER: _ClassVar[int]
    HYDRATION_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    HYDRATION_INFO_FIELD_NUMBER: _ClassVar[int]
    EPOCH_VEC_FIELD_NUMBER: _ClassVar[int]
    MAX_HYDRATION_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    hydration_status: SnapshotInfo.HydrationStatus
    hydrated_disks_vec: _containers.RepeatedCompositeFieldContainer[SnapshotInfo.VirtualDisk]
    hydration_time_usecs: int
    hydration_info: HydrationInfo
    epoch_vec: _containers.RepeatedCompositeFieldContainer[_atom_pb2.EpochProto]
    max_hydration_time_usecs: int
    def __init__(self, hydration_status: _Optional[_Union[SnapshotInfo.HydrationStatus, str]] = ..., hydrated_disks_vec: _Optional[_Iterable[_Union[SnapshotInfo.VirtualDisk, _Mapping]]] = ..., hydration_time_usecs: _Optional[int] = ..., hydration_info: _Optional[_Union[HydrationInfo, _Mapping]] = ..., epoch_vec: _Optional[_Iterable[_Union[_atom_pb2.EpochProto, _Mapping]]] = ..., max_hydration_time_usecs: _Optional[int] = ...) -> None: ...
