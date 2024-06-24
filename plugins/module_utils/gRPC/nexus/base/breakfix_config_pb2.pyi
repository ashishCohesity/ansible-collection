from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UUID(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: str
    def __init__(self, value: _Optional[str] = ...) -> None: ...

class BreakfixNode(_message.Message):
    __slots__ = ("cluster_id", "rack_id", "chassis_id", "node_id")
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    RACK_ID_FIELD_NUMBER: _ClassVar[int]
    CHASSIS_ID_FIELD_NUMBER: _ClassVar[int]
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    cluster_id: str
    rack_id: str
    chassis_id: str
    node_id: int
    def __init__(self, cluster_id: _Optional[str] = ..., rack_id: _Optional[str] = ..., chassis_id: _Optional[str] = ..., node_id: _Optional[int] = ...) -> None: ...

class BreakfixTask(_message.Message):
    __slots__ = ("task_id", "task_type", "task_status")
    class TaskType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNone: _ClassVar[BreakfixTask.TaskType]
        kReplacement: _ClassVar[BreakfixTask.TaskType]
        kRollback: _ClassVar[BreakfixTask.TaskType]
        kLocate: _ClassVar[BreakfixTask.TaskType]
    kNone: BreakfixTask.TaskType
    kReplacement: BreakfixTask.TaskType
    kRollback: BreakfixTask.TaskType
    kLocate: BreakfixTask.TaskType
    class TaskStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kUndefined: _ClassVar[BreakfixTask.TaskStatus]
        kRunning: _ClassVar[BreakfixTask.TaskStatus]
        kSuspended: _ClassVar[BreakfixTask.TaskStatus]
        kCompleted: _ClassVar[BreakfixTask.TaskStatus]
        kFailed: _ClassVar[BreakfixTask.TaskStatus]
    kUndefined: BreakfixTask.TaskStatus
    kRunning: BreakfixTask.TaskStatus
    kSuspended: BreakfixTask.TaskStatus
    kCompleted: BreakfixTask.TaskStatus
    kFailed: BreakfixTask.TaskStatus
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    TASK_TYPE_FIELD_NUMBER: _ClassVar[int]
    TASK_STATUS_FIELD_NUMBER: _ClassVar[int]
    task_id: UUID
    task_type: BreakfixTask.TaskType
    task_status: BreakfixTask.TaskStatus
    def __init__(self, task_id: _Optional[_Union[UUID, _Mapping]] = ..., task_type: _Optional[_Union[BreakfixTask.TaskType, str]] = ..., task_status: _Optional[_Union[BreakfixTask.TaskStatus, str]] = ...) -> None: ...

class BreakfixFru(_message.Message):
    __slots__ = ("fru_type", "fru_id")
    class FruType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNone: _ClassVar[BreakfixFru.FruType]
        kDisk: _ClassVar[BreakfixFru.FruType]
        kFan: _ClassVar[BreakfixFru.FruType]
    kNone: BreakfixFru.FruType
    kDisk: BreakfixFru.FruType
    kFan: BreakfixFru.FruType
    FRU_TYPE_FIELD_NUMBER: _ClassVar[int]
    FRU_ID_FIELD_NUMBER: _ClassVar[int]
    fru_type: BreakfixFru.FruType
    fru_id: str
    def __init__(self, fru_type: _Optional[_Union[BreakfixFru.FruType, str]] = ..., fru_id: _Optional[str] = ...) -> None: ...

class FruReplacementConfigProto(_message.Message):
    __slots__ = ("gandalf_key", "fru_replacement_config")
    GANDALF_KEY_FIELD_NUMBER: _ClassVar[int]
    FRU_REPLACEMENT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    gandalf_key: str
    fru_replacement_config: _containers.RepeatedCompositeFieldContainer[FruReplacementConfig]
    def __init__(self, gandalf_key: _Optional[str] = ..., fru_replacement_config: _Optional[_Iterable[_Union[FruReplacementConfig, _Mapping]]] = ...) -> None: ...

class FruReplacementConfig(_message.Message):
    __slots__ = ("node", "task", "fru", "step_id", "step_state")
    class StepState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kUndefined: _ClassVar[FruReplacementConfig.StepState]
        kCompleted: _ClassVar[FruReplacementConfig.StepState]
        kRunning: _ClassVar[FruReplacementConfig.StepState]
        kSuspended: _ClassVar[FruReplacementConfig.StepState]
        kFailed: _ClassVar[FruReplacementConfig.StepState]
    kUndefined: FruReplacementConfig.StepState
    kCompleted: FruReplacementConfig.StepState
    kRunning: FruReplacementConfig.StepState
    kSuspended: FruReplacementConfig.StepState
    kFailed: FruReplacementConfig.StepState
    NODE_FIELD_NUMBER: _ClassVar[int]
    TASK_FIELD_NUMBER: _ClassVar[int]
    FRU_FIELD_NUMBER: _ClassVar[int]
    STEP_ID_FIELD_NUMBER: _ClassVar[int]
    STEP_STATE_FIELD_NUMBER: _ClassVar[int]
    node: BreakfixNode
    task: BreakfixTask
    fru: BreakfixFru
    step_id: int
    step_state: FruReplacementConfig.StepState
    def __init__(self, node: _Optional[_Union[BreakfixNode, _Mapping]] = ..., task: _Optional[_Union[BreakfixTask, _Mapping]] = ..., fru: _Optional[_Union[BreakfixFru, _Mapping]] = ..., step_id: _Optional[int] = ..., step_state: _Optional[_Union[FruReplacementConfig.StepState, str]] = ...) -> None: ...

class FruLocateConfigProto(_message.Message):
    __slots__ = ("fru_locate_config",)
    FRU_LOCATE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    fru_locate_config: _containers.RepeatedCompositeFieldContainer[FruLocateConfig]
    def __init__(self, fru_locate_config: _Optional[_Iterable[_Union[FruLocateConfig, _Mapping]]] = ...) -> None: ...

class FruLocateConfig(_message.Message):
    __slots__ = ("node", "task", "fru")
    NODE_FIELD_NUMBER: _ClassVar[int]
    TASK_FIELD_NUMBER: _ClassVar[int]
    FRU_FIELD_NUMBER: _ClassVar[int]
    node: BreakfixNode
    task: BreakfixTask
    fru: BreakfixFru
    def __init__(self, node: _Optional[_Union[BreakfixNode, _Mapping]] = ..., task: _Optional[_Union[BreakfixTask, _Mapping]] = ..., fru: _Optional[_Union[BreakfixFru, _Mapping]] = ...) -> None: ...

class FruReplacementProcedureStep(_message.Message):
    __slots__ = ("id", "title", "description", "eta", "step_type", "run_on_local")
    class StepType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kUndefined: _ClassVar[FruReplacementProcedureStep.StepType]
        kAuto: _ClassVar[FruReplacementProcedureStep.StepType]
        kManual: _ClassVar[FruReplacementProcedureStep.StepType]
    kUndefined: FruReplacementProcedureStep.StepType
    kAuto: FruReplacementProcedureStep.StepType
    kManual: FruReplacementProcedureStep.StepType
    ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ETA_FIELD_NUMBER: _ClassVar[int]
    STEP_TYPE_FIELD_NUMBER: _ClassVar[int]
    RUN_ON_LOCAL_FIELD_NUMBER: _ClassVar[int]
    id: int
    title: str
    description: str
    eta: int
    step_type: FruReplacementProcedureStep.StepType
    run_on_local: bool
    def __init__(self, id: _Optional[int] = ..., title: _Optional[str] = ..., description: _Optional[str] = ..., eta: _Optional[int] = ..., step_type: _Optional[_Union[FruReplacementProcedureStep.StepType, str]] = ..., run_on_local: bool = ...) -> None: ...

class FruReplacementProcedure(_message.Message):
    __slots__ = ("task_id", "fru", "fru_replacement_procedure_step")
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    FRU_FIELD_NUMBER: _ClassVar[int]
    FRU_REPLACEMENT_PROCEDURE_STEP_FIELD_NUMBER: _ClassVar[int]
    task_id: str
    fru: BreakfixFru
    fru_replacement_procedure_step: _containers.RepeatedCompositeFieldContainer[FruReplacementProcedureStep]
    def __init__(self, task_id: _Optional[str] = ..., fru: _Optional[_Union[BreakfixFru, _Mapping]] = ..., fru_replacement_procedure_step: _Optional[_Iterable[_Union[FruReplacementProcedureStep, _Mapping]]] = ...) -> None: ...

class FruReplacementProcedureList(_message.Message):
    __slots__ = ("fru_replacement_procedure",)
    FRU_REPLACEMENT_PROCEDURE_FIELD_NUMBER: _ClassVar[int]
    fru_replacement_procedure: _containers.RepeatedCompositeFieldContainer[FruReplacementProcedure]
    def __init__(self, fru_replacement_procedure: _Optional[_Iterable[_Union[FruReplacementProcedure, _Mapping]]] = ...) -> None: ...
