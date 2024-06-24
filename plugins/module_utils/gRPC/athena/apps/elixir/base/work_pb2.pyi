from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class WorkStage(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kStageUnknown: _ClassVar[WorkStage]
    kStagePlanCreation: _ClassVar[WorkStage]
    kStagePlanExecution: _ClassVar[WorkStage]
    kStageCompleted: _ClassVar[WorkStage]
    kStageFetchSnapshots: _ClassVar[WorkStage]
    kStageFetchTargetEntities: _ClassVar[WorkStage]
    kStageRefreshEH: _ClassVar[WorkStage]
    kStageProtectVms: _ClassVar[WorkStage]
    kStageUpdateSpecAfterFailover: _ClassVar[WorkStage]
    kStageUpdateSpecAfterFailback: _ClassVar[WorkStage]
    kStageUpdateRunbookForFailback: _ClassVar[WorkStage]
    kStageInitiateFailover: _ClassVar[WorkStage]
    kStageFinalizeFailoverRx: _ClassVar[WorkStage]
    kStageLinkEntities: _ClassVar[WorkStage]
    kStageFinalizeFailoverTx: _ClassVar[WorkStage]
    kStageResolveEntities: _ClassVar[WorkStage]
    kStageVmwMountNASds: _ClassVar[WorkStage]
    kStageShutdownVMs: _ClassVar[WorkStage]
    kStageVmwRegisterVM: _ClassVar[WorkStage]
    kStageVmwVmotionAndCustomize: _ClassVar[WorkStage]
    kStageVmwUnmountNASds: _ClassVar[WorkStage]
    kStageViewPlanCreation: _ClassVar[WorkStage]
    kStageViewPlanExecution: _ClassVar[WorkStage]
    kStageUpdateSpecAfterViewFailover: _ClassVar[WorkStage]
kStageUnknown: WorkStage
kStagePlanCreation: WorkStage
kStagePlanExecution: WorkStage
kStageCompleted: WorkStage
kStageFetchSnapshots: WorkStage
kStageFetchTargetEntities: WorkStage
kStageRefreshEH: WorkStage
kStageProtectVms: WorkStage
kStageUpdateSpecAfterFailover: WorkStage
kStageUpdateSpecAfterFailback: WorkStage
kStageUpdateRunbookForFailback: WorkStage
kStageInitiateFailover: WorkStage
kStageFinalizeFailoverRx: WorkStage
kStageLinkEntities: WorkStage
kStageFinalizeFailoverTx: WorkStage
kStageResolveEntities: WorkStage
kStageVmwMountNASds: WorkStage
kStageShutdownVMs: WorkStage
kStageVmwRegisterVM: WorkStage
kStageVmwVmotionAndCustomize: WorkStage
kStageVmwUnmountNASds: WorkStage
kStageViewPlanCreation: WorkStage
kStageViewPlanExecution: WorkStage
kStageUpdateSpecAfterViewFailover: WorkStage

class AppSpecWorkProto(_message.Message):
    __slots__ = ("id", "runbook_uid", "run_id", "status", "start_time_msecs", "end_time_msecs", "duration_msecs", "sequence", "action", "total_plans", "is_first_work", "is_last_work", "has_terraform_plan", "is_init_work", "is_last_init_work", "ignore_failure", "execute_on_resume")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kInProgress: _ClassVar[AppSpecWorkProto.Status]
        kCompleted: _ClassVar[AppSpecWorkProto.Status]
        kFailed: _ClassVar[AppSpecWorkProto.Status]
        kCanceled: _ClassVar[AppSpecWorkProto.Status]
        kCanceling: _ClassVar[AppSpecWorkProto.Status]
        kDeleted: _ClassVar[AppSpecWorkProto.Status]
        kDeleting: _ClassVar[AppSpecWorkProto.Status]
    kInProgress: AppSpecWorkProto.Status
    kCompleted: AppSpecWorkProto.Status
    kFailed: AppSpecWorkProto.Status
    kCanceled: AppSpecWorkProto.Status
    kCanceling: AppSpecWorkProto.Status
    kDeleted: AppSpecWorkProto.Status
    kDeleting: AppSpecWorkProto.Status
    class Action(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kApply: _ClassVar[AppSpecWorkProto.Action]
        kDestroy: _ClassVar[AppSpecWorkProto.Action]
    kApply: AppSpecWorkProto.Action
    kDestroy: AppSpecWorkProto.Action
    ID_FIELD_NUMBER: _ClassVar[int]
    RUNBOOK_UID_FIELD_NUMBER: _ClassVar[int]
    RUN_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    START_TIME_MSECS_FIELD_NUMBER: _ClassVar[int]
    END_TIME_MSECS_FIELD_NUMBER: _ClassVar[int]
    DURATION_MSECS_FIELD_NUMBER: _ClassVar[int]
    SEQUENCE_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    TOTAL_PLANS_FIELD_NUMBER: _ClassVar[int]
    IS_FIRST_WORK_FIELD_NUMBER: _ClassVar[int]
    IS_LAST_WORK_FIELD_NUMBER: _ClassVar[int]
    HAS_TERRAFORM_PLAN_FIELD_NUMBER: _ClassVar[int]
    IS_INIT_WORK_FIELD_NUMBER: _ClassVar[int]
    IS_LAST_INIT_WORK_FIELD_NUMBER: _ClassVar[int]
    IGNORE_FAILURE_FIELD_NUMBER: _ClassVar[int]
    EXECUTE_ON_RESUME_FIELD_NUMBER: _ClassVar[int]
    id: int
    runbook_uid: str
    run_id: int
    status: AppSpecWorkProto.Status
    start_time_msecs: int
    end_time_msecs: int
    duration_msecs: int
    sequence: WorkStage
    action: AppSpecWorkProto.Action
    total_plans: int
    is_first_work: bool
    is_last_work: bool
    has_terraform_plan: bool
    is_init_work: bool
    is_last_init_work: bool
    ignore_failure: bool
    execute_on_resume: bool
    def __init__(self, id: _Optional[int] = ..., runbook_uid: _Optional[str] = ..., run_id: _Optional[int] = ..., status: _Optional[_Union[AppSpecWorkProto.Status, str]] = ..., start_time_msecs: _Optional[int] = ..., end_time_msecs: _Optional[int] = ..., duration_msecs: _Optional[int] = ..., sequence: _Optional[_Union[WorkStage, str]] = ..., action: _Optional[_Union[AppSpecWorkProto.Action, str]] = ..., total_plans: _Optional[int] = ..., is_first_work: bool = ..., is_last_work: bool = ..., has_terraform_plan: bool = ..., is_init_work: bool = ..., is_last_init_work: bool = ..., ignore_failure: bool = ..., execute_on_resume: bool = ...) -> None: ...
