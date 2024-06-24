from atom.base import event_pb2 as _event_pb2
from magneto.base import magneto_pb2 as _magneto_pb2
from magneto.base import env_params_pb2 as _env_params_pb2
from magneto.base import sub_task_pb2 as _sub_task_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LogApplyRestoreParams(_message.Message):
    __slots__ = ("restore_time_usecs", "virtual_disk_vec", "backup_to_standby_disk_uuid_map")
    class BackupToStandbyDiskUuidMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    RESTORE_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    VIRTUAL_DISK_VEC_FIELD_NUMBER: _ClassVar[int]
    BACKUP_TO_STANDBY_DISK_UUID_MAP_FIELD_NUMBER: _ClassVar[int]
    restore_time_usecs: int
    virtual_disk_vec: _containers.RepeatedCompositeFieldContainer[_magneto_pb2.VirtualDiskHydrationInfo]
    backup_to_standby_disk_uuid_map: _containers.ScalarMap[str, str]
    def __init__(self, restore_time_usecs: _Optional[int] = ..., virtual_disk_vec: _Optional[_Iterable[_Union[_magneto_pb2.VirtualDiskHydrationInfo, _Mapping]]] = ..., backup_to_standby_disk_uuid_map: _Optional[_Mapping[str, str]] = ...) -> None: ...

class LogApplyRestoreSubTaskInfo(_message.Message):
    __slots__ = ("applied_log_index", "last_applied_sequence_number")
    LOG_APPLY_RESTORE_SUB_TASK_INFO_FIELD_NUMBER: _ClassVar[int]
    log_apply_restore_sub_task_info: _descriptor.FieldDescriptor
    APPLIED_LOG_INDEX_FIELD_NUMBER: _ClassVar[int]
    LAST_APPLIED_SEQUENCE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    applied_log_index: int
    last_applied_sequence_number: _event_pb2.Sequencer
    def __init__(self, applied_log_index: _Optional[int] = ..., last_applied_sequence_number: _Optional[_Union[_event_pb2.Sequencer, _Mapping]] = ...) -> None: ...

class ReHydrateVMRestoreParams(_message.Message):
    __slots__ = ("rehydrate_full_backup", "is_cdp_rehydration", "backup_to_standby_disk_uuid_map", "latest_cdp_standby_hydration_params", "latest_cdp_backup_hydration_params")
    class BackupToStandbyDiskUuidMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    REHYDRATE_FULL_BACKUP_FIELD_NUMBER: _ClassVar[int]
    IS_CDP_REHYDRATION_FIELD_NUMBER: _ClassVar[int]
    BACKUP_TO_STANDBY_DISK_UUID_MAP_FIELD_NUMBER: _ClassVar[int]
    LATEST_CDP_STANDBY_HYDRATION_PARAMS_FIELD_NUMBER: _ClassVar[int]
    LATEST_CDP_BACKUP_HYDRATION_PARAMS_FIELD_NUMBER: _ClassVar[int]
    rehydrate_full_backup: bool
    is_cdp_rehydration: bool
    backup_to_standby_disk_uuid_map: _containers.ScalarMap[str, str]
    latest_cdp_standby_hydration_params: _magneto_pb2.CDPRestoreParams
    latest_cdp_backup_hydration_params: _magneto_pb2.CDPRestoreParams
    def __init__(self, rehydrate_full_backup: bool = ..., is_cdp_rehydration: bool = ..., backup_to_standby_disk_uuid_map: _Optional[_Mapping[str, str]] = ..., latest_cdp_standby_hydration_params: _Optional[_Union[_magneto_pb2.CDPRestoreParams, _Mapping]] = ..., latest_cdp_backup_hydration_params: _Optional[_Union[_magneto_pb2.CDPRestoreParams, _Mapping]] = ...) -> None: ...
