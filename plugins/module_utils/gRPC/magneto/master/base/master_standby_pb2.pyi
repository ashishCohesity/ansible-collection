from magneto.base import cdp_pb2 as _cdp_pb2
from magneto.base import entity_pb2 as _entity_pb2
from magneto.base import error_pb2 as _error_pb2
from magneto.base import magneto_pb2 as _magneto_pb2
from magneto.base import env_params_pb2 as _env_params_pb2
from util.base import universal_id_pb2 as _universal_id_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StandbyStateProto(_message.Message):
    __slots__ = ("entity_id", "job_uid", "standby_entity_id", "standby_resource_info", "type", "standby_state", "last_successful_backup_run_start_time_usecs", "multi_stage_restore_task_id")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kVMwareCDP: _ClassVar[StandbyStateProto.Type]
        kVMwareVADP: _ClassVar[StandbyStateProto.Type]
    kVMwareCDP: StandbyStateProto.Type
    kVMwareVADP: StandbyStateProto.Type
    class StandbyResourceInfo(_message.Message):
        __slots__ = ("parent_entity_id",)
        PARENT_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
        parent_entity_id: int
        def __init__(self, parent_entity_id: _Optional[int] = ...) -> None: ...
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    JOB_UID_FIELD_NUMBER: _ClassVar[int]
    STANDBY_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    STANDBY_RESOURCE_INFO_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    STANDBY_STATE_FIELD_NUMBER: _ClassVar[int]
    LAST_SUCCESSFUL_BACKUP_RUN_START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    MULTI_STAGE_RESTORE_TASK_ID_FIELD_NUMBER: _ClassVar[int]
    entity_id: int
    job_uid: _universal_id_pb2.UniversalIdProto
    standby_entity_id: int
    standby_resource_info: StandbyStateProto.StandbyResourceInfo
    type: StandbyStateProto.Type
    standby_state: StandbyState
    last_successful_backup_run_start_time_usecs: int
    multi_stage_restore_task_id: int
    def __init__(self, entity_id: _Optional[int] = ..., job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., standby_entity_id: _Optional[int] = ..., standby_resource_info: _Optional[_Union[StandbyStateProto.StandbyResourceInfo, _Mapping]] = ..., type: _Optional[_Union[StandbyStateProto.Type, str]] = ..., standby_state: _Optional[_Union[StandbyState, _Mapping]] = ..., last_successful_backup_run_start_time_usecs: _Optional[int] = ..., multi_stage_restore_task_id: _Optional[int] = ...) -> None: ...

class ErrorInfo(_message.Message):
    __slots__ = ("error", "error_count_since_last_success", "last_update_time_usecs")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ERROR_COUNT_SINCE_LAST_SUCCESS_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATE_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    error_count_since_last_success: int
    last_update_time_usecs: int
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., error_count_since_last_success: _Optional[int] = ..., last_update_time_usecs: _Optional[int] = ...) -> None: ...

class StandbyState(_message.Message):
    __slots__ = ("state", "error", "standby_vm_info", "last_update_time_usecs", "state_intent", "create_vm_info", "log_apply_info", "rehydrate_info", "standby_restore_info")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kInit: _ClassVar[StandbyState.State]
        kVMCreationInProgress: _ClassVar[StandbyState.State]
        kVMCreated: _ClassVar[StandbyState.State]
        kLogStreamingInProgress: _ClassVar[StandbyState.State]
        kReHydrationInProgress: _ClassVar[StandbyState.State]
        kSteady: _ClassVar[StandbyState.State]
        kDisabled: _ClassVar[StandbyState.State]
        kRestoreComplete: _ClassVar[StandbyState.State]
        kReHydrationRequired_DEPRECATED: _ClassVar[StandbyState.State]
    kInit: StandbyState.State
    kVMCreationInProgress: StandbyState.State
    kVMCreated: StandbyState.State
    kLogStreamingInProgress: StandbyState.State
    kReHydrationInProgress: StandbyState.State
    kSteady: StandbyState.State
    kDisabled: StandbyState.State
    kRestoreComplete: StandbyState.State
    kReHydrationRequired_DEPRECATED: StandbyState.State
    class StandbyVMInfo(_message.Message):
        __slots__ = ("cdp_virtual_disk_vec", "standby_time_usecs", "standby_entity", "guest_id", "backup_to_standby_disk_uuid_map")
        class BackupToStandbyDiskUuidMapEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: str
            def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
        CDP_VIRTUAL_DISK_VEC_FIELD_NUMBER: _ClassVar[int]
        STANDBY_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
        STANDBY_ENTITY_FIELD_NUMBER: _ClassVar[int]
        GUEST_ID_FIELD_NUMBER: _ClassVar[int]
        BACKUP_TO_STANDBY_DISK_UUID_MAP_FIELD_NUMBER: _ClassVar[int]
        cdp_virtual_disk_vec: _containers.RepeatedCompositeFieldContainer[_cdp_pb2.VirtualDiskInfo]
        standby_time_usecs: int
        standby_entity: _entity_pb2.EntityProto
        guest_id: str
        backup_to_standby_disk_uuid_map: _containers.ScalarMap[str, str]
        def __init__(self, cdp_virtual_disk_vec: _Optional[_Iterable[_Union[_cdp_pb2.VirtualDiskInfo, _Mapping]]] = ..., standby_time_usecs: _Optional[int] = ..., standby_entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., guest_id: _Optional[str] = ..., backup_to_standby_disk_uuid_map: _Optional[_Mapping[str, str]] = ...) -> None: ...
    class StateIntent(_message.Message):
        __slots__ = ("standby_intent", "cancel_standby")
        class StandbyIntent(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kNone: _ClassVar[StandbyState.StateIntent.StandbyIntent]
            kPauseStandby: _ClassVar[StandbyState.StateIntent.StandbyIntent]
            kDisableStandby: _ClassVar[StandbyState.StateIntent.StandbyIntent]
            kRestoreRequested: _ClassVar[StandbyState.StateIntent.StandbyIntent]
        kNone: StandbyState.StateIntent.StandbyIntent
        kPauseStandby: StandbyState.StateIntent.StandbyIntent
        kDisableStandby: StandbyState.StateIntent.StandbyIntent
        kRestoreRequested: StandbyState.StateIntent.StandbyIntent
        STANDBY_INTENT_FIELD_NUMBER: _ClassVar[int]
        CANCEL_STANDBY_FIELD_NUMBER: _ClassVar[int]
        standby_intent: StandbyState.StateIntent.StandbyIntent
        cancel_standby: bool
        def __init__(self, standby_intent: _Optional[_Union[StandbyState.StateIntent.StandbyIntent, str]] = ..., cancel_standby: bool = ...) -> None: ...
    class CreateVMInfo(_message.Message):
        __slots__ = ("error_info", "task_id")
        ERROR_INFO_FIELD_NUMBER: _ClassVar[int]
        TASK_ID_FIELD_NUMBER: _ClassVar[int]
        error_info: ErrorInfo
        task_id: int
        def __init__(self, error_info: _Optional[_Union[ErrorInfo, _Mapping]] = ..., task_id: _Optional[int] = ...) -> None: ...
    class LogApplyInfo(_message.Message):
        __slots__ = ("error_info", "task_id")
        ERROR_INFO_FIELD_NUMBER: _ClassVar[int]
        TASK_ID_FIELD_NUMBER: _ClassVar[int]
        error_info: ErrorInfo
        task_id: int
        def __init__(self, error_info: _Optional[_Union[ErrorInfo, _Mapping]] = ..., task_id: _Optional[int] = ...) -> None: ...
    class RehydrateInfo(_message.Message):
        __slots__ = ("error_info", "task_id")
        ERROR_INFO_FIELD_NUMBER: _ClassVar[int]
        TASK_ID_FIELD_NUMBER: _ClassVar[int]
        error_info: ErrorInfo
        task_id: int
        def __init__(self, error_info: _Optional[_Union[ErrorInfo, _Mapping]] = ..., task_id: _Optional[int] = ...) -> None: ...
    class StandbyRestoreInfo(_message.Message):
        __slots__ = ("owner_restore_task_id", "restore_point_in_time_usecs", "log_apply_task_id", "rehydration_task_id", "error")
        OWNER_RESTORE_TASK_ID_FIELD_NUMBER: _ClassVar[int]
        RESTORE_POINT_IN_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
        LOG_APPLY_TASK_ID_FIELD_NUMBER: _ClassVar[int]
        REHYDRATION_TASK_ID_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        owner_restore_task_id: int
        restore_point_in_time_usecs: int
        log_apply_task_id: int
        rehydration_task_id: int
        error: _error_pb2.ErrorProto
        def __init__(self, owner_restore_task_id: _Optional[int] = ..., restore_point_in_time_usecs: _Optional[int] = ..., log_apply_task_id: _Optional[int] = ..., rehydration_task_id: _Optional[int] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...
    STATE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    STANDBY_VM_INFO_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATE_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    STATE_INTENT_FIELD_NUMBER: _ClassVar[int]
    CREATE_VM_INFO_FIELD_NUMBER: _ClassVar[int]
    LOG_APPLY_INFO_FIELD_NUMBER: _ClassVar[int]
    REHYDRATE_INFO_FIELD_NUMBER: _ClassVar[int]
    STANDBY_RESTORE_INFO_FIELD_NUMBER: _ClassVar[int]
    state: StandbyState.State
    error: _error_pb2.ErrorProto
    standby_vm_info: StandbyState.StandbyVMInfo
    last_update_time_usecs: int
    state_intent: StandbyState.StateIntent
    create_vm_info: StandbyState.CreateVMInfo
    log_apply_info: StandbyState.LogApplyInfo
    rehydrate_info: StandbyState.RehydrateInfo
    standby_restore_info: StandbyState.StandbyRestoreInfo
    def __init__(self, state: _Optional[_Union[StandbyState.State, str]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., standby_vm_info: _Optional[_Union[StandbyState.StandbyVMInfo, _Mapping]] = ..., last_update_time_usecs: _Optional[int] = ..., state_intent: _Optional[_Union[StandbyState.StateIntent, _Mapping]] = ..., create_vm_info: _Optional[_Union[StandbyState.CreateVMInfo, _Mapping]] = ..., log_apply_info: _Optional[_Union[StandbyState.LogApplyInfo, _Mapping]] = ..., rehydrate_info: _Optional[_Union[StandbyState.RehydrateInfo, _Mapping]] = ..., standby_restore_info: _Optional[_Union[StandbyState.StandbyRestoreInfo, _Mapping]] = ...) -> None: ...
