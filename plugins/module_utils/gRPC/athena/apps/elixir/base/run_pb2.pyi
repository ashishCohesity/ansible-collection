from util.appspec import appspec_pb2 as _appspec_pb2
from athena.apps.elixir.base import work_pb2 as _work_pb2
from athena.apps.elixir.base import override_pb2 as _override_pb2
from magneto.base import permissions_pb2 as _permissions_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ProgressInfoProto(_message.Message):
    __slots__ = ("resource", "status", "details", "start_time_msecs", "end_time_msecs", "duration_msecs", "target_profile_id", "resource_identifier", "type", "status_message", "group_name", "group_identifier")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kCreated: _ClassVar[ProgressInfoProto.Status]
        kCreating: _ClassVar[ProgressInfoProto.Status]
        kFailed: _ClassVar[ProgressInfoProto.Status]
        kCanceled: _ClassVar[ProgressInfoProto.Status]
        kCanceling: _ClassVar[ProgressInfoProto.Status]
        kDeleted: _ClassVar[ProgressInfoProto.Status]
        kDeleting: _ClassVar[ProgressInfoProto.Status]
        kPending: _ClassVar[ProgressInfoProto.Status]
    kCreated: ProgressInfoProto.Status
    kCreating: ProgressInfoProto.Status
    kFailed: ProgressInfoProto.Status
    kCanceled: ProgressInfoProto.Status
    kCanceling: ProgressInfoProto.Status
    kDeleted: ProgressInfoProto.Status
    kDeleting: ProgressInfoProto.Status
    kPending: ProgressInfoProto.Status
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kInit: _ClassVar[ProgressInfoProto.Type]
        kResource: _ClassVar[ProgressInfoProto.Type]
        kFinal: _ClassVar[ProgressInfoProto.Type]
    kInit: ProgressInfoProto.Type
    kResource: ProgressInfoProto.Type
    kFinal: ProgressInfoProto.Type
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    START_TIME_MSECS_FIELD_NUMBER: _ClassVar[int]
    END_TIME_MSECS_FIELD_NUMBER: _ClassVar[int]
    DURATION_MSECS_FIELD_NUMBER: _ClassVar[int]
    TARGET_PROFILE_ID_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    STATUS_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    GROUP_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    resource: _appspec_pb2.Resource
    status: ProgressInfoProto.Status
    details: str
    start_time_msecs: int
    end_time_msecs: int
    duration_msecs: int
    target_profile_id: str
    resource_identifier: _appspec_pb2.Identifier
    type: ProgressInfoProto.Type
    status_message: str
    group_name: str
    group_identifier: _appspec_pb2.Identifier
    def __init__(self, resource: _Optional[_Union[_appspec_pb2.Resource, _Mapping]] = ..., status: _Optional[_Union[ProgressInfoProto.Status, str]] = ..., details: _Optional[str] = ..., start_time_msecs: _Optional[int] = ..., end_time_msecs: _Optional[int] = ..., duration_msecs: _Optional[int] = ..., target_profile_id: _Optional[str] = ..., resource_identifier: _Optional[_Union[_appspec_pb2.Identifier, _Mapping]] = ..., type: _Optional[_Union[ProgressInfoProto.Type, str]] = ..., status_message: _Optional[str] = ..., group_name: _Optional[str] = ..., group_identifier: _Optional[_Union[_appspec_pb2.Identifier, _Mapping]] = ...) -> None: ...

class AppSpecRun(_message.Message):
    __slots__ = ("id", "runbook_uid", "status", "appspec_json", "start_time_msecs", "end_time_msecs", "duration_secs", "target_profile_id_vec", "resource_progress_vec", "status_message", "last_run_stage", "last_delete_stage", "failover_type", "type", "target_details", "failover_options", "continue_on_error", "last_group_processed", "snapshot_override_vec", "dependency_vec", "user_info")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kInProgress: _ClassVar[AppSpecRun.Status]
        kCompleted: _ClassVar[AppSpecRun.Status]
        kFailed: _ClassVar[AppSpecRun.Status]
        kCanceled: _ClassVar[AppSpecRun.Status]
        kCanceling: _ClassVar[AppSpecRun.Status]
        kDeleted: _ClassVar[AppSpecRun.Status]
        kDeleting: _ClassVar[AppSpecRun.Status]
    kInProgress: AppSpecRun.Status
    kCompleted: AppSpecRun.Status
    kFailed: AppSpecRun.Status
    kCanceled: AppSpecRun.Status
    kCanceling: AppSpecRun.Status
    kDeleted: AppSpecRun.Status
    kDeleting: AppSpecRun.Status
    class FailoverType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kTest: _ClassVar[AppSpecRun.FailoverType]
        kActual: _ClassVar[AppSpecRun.FailoverType]
    kTest: AppSpecRun.FailoverType
    kActual: AppSpecRun.FailoverType
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kFailoverRun: _ClassVar[AppSpecRun.Type]
        kPreFailbackRun: _ClassVar[AppSpecRun.Type]
        kFailbackRun: _ClassVar[AppSpecRun.Type]
        kTestDevRun: _ClassVar[AppSpecRun.Type]
    kFailoverRun: AppSpecRun.Type
    kPreFailbackRun: AppSpecRun.Type
    kFailbackRun: AppSpecRun.Type
    kTestDevRun: AppSpecRun.Type
    ID_FIELD_NUMBER: _ClassVar[int]
    RUNBOOK_UID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    APPSPEC_JSON_FIELD_NUMBER: _ClassVar[int]
    START_TIME_MSECS_FIELD_NUMBER: _ClassVar[int]
    END_TIME_MSECS_FIELD_NUMBER: _ClassVar[int]
    DURATION_SECS_FIELD_NUMBER: _ClassVar[int]
    TARGET_PROFILE_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_PROGRESS_VEC_FIELD_NUMBER: _ClassVar[int]
    STATUS_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    LAST_RUN_STAGE_FIELD_NUMBER: _ClassVar[int]
    LAST_DELETE_STAGE_FIELD_NUMBER: _ClassVar[int]
    FAILOVER_TYPE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    TARGET_DETAILS_FIELD_NUMBER: _ClassVar[int]
    FAILOVER_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    CONTINUE_ON_ERROR_FIELD_NUMBER: _ClassVar[int]
    LAST_GROUP_PROCESSED_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_OVERRIDE_VEC_FIELD_NUMBER: _ClassVar[int]
    DEPENDENCY_VEC_FIELD_NUMBER: _ClassVar[int]
    USER_INFO_FIELD_NUMBER: _ClassVar[int]
    id: int
    runbook_uid: str
    status: AppSpecRun.Status
    appspec_json: str
    start_time_msecs: int
    end_time_msecs: int
    duration_secs: int
    target_profile_id_vec: _containers.RepeatedScalarFieldContainer[str]
    resource_progress_vec: _containers.RepeatedCompositeFieldContainer[ProgressInfoProto]
    status_message: str
    last_run_stage: _work_pb2.WorkStage
    last_delete_stage: _work_pb2.WorkStage
    failover_type: AppSpecRun.FailoverType
    type: AppSpecRun.Type
    target_details: TargetDetails
    failover_options: FailoverOptions
    continue_on_error: bool
    last_group_processed: str
    snapshot_override_vec: _containers.RepeatedCompositeFieldContainer[_override_pb2.SnapshotOverrideProto]
    dependency_vec: _containers.RepeatedScalarFieldContainer[str]
    user_info: _permissions_pb2.UserInformation
    def __init__(self, id: _Optional[int] = ..., runbook_uid: _Optional[str] = ..., status: _Optional[_Union[AppSpecRun.Status, str]] = ..., appspec_json: _Optional[str] = ..., start_time_msecs: _Optional[int] = ..., end_time_msecs: _Optional[int] = ..., duration_secs: _Optional[int] = ..., target_profile_id_vec: _Optional[_Iterable[str]] = ..., resource_progress_vec: _Optional[_Iterable[_Union[ProgressInfoProto, _Mapping]]] = ..., status_message: _Optional[str] = ..., last_run_stage: _Optional[_Union[_work_pb2.WorkStage, str]] = ..., last_delete_stage: _Optional[_Union[_work_pb2.WorkStage, str]] = ..., failover_type: _Optional[_Union[AppSpecRun.FailoverType, str]] = ..., type: _Optional[_Union[AppSpecRun.Type, str]] = ..., target_details: _Optional[_Union[TargetDetails, _Mapping]] = ..., failover_options: _Optional[_Union[FailoverOptions, _Mapping]] = ..., continue_on_error: bool = ..., last_group_processed: _Optional[str] = ..., snapshot_override_vec: _Optional[_Iterable[_Union[_override_pb2.SnapshotOverrideProto, _Mapping]]] = ..., dependency_vec: _Optional[_Iterable[str]] = ..., user_info: _Optional[_Union[_permissions_pb2.UserInformation, _Mapping]] = ...) -> None: ...

class TargetDetails(_message.Message):
    __slots__ = ("replication_targets", "target_vec", "target_profile_vec")
    REPLICATION_TARGETS_FIELD_NUMBER: _ClassVar[int]
    TARGET_VEC_FIELD_NUMBER: _ClassVar[int]
    TARGET_PROFILE_VEC_FIELD_NUMBER: _ClassVar[int]
    replication_targets: _containers.RepeatedCompositeFieldContainer[_appspec_pb2.RemoteCluster]
    target_vec: _containers.RepeatedCompositeFieldContainer[_appspec_pb2.Target]
    target_profile_vec: _containers.RepeatedCompositeFieldContainer[_appspec_pb2.TargetProfile]
    def __init__(self, replication_targets: _Optional[_Iterable[_Union[_appspec_pb2.RemoteCluster, _Mapping]]] = ..., target_vec: _Optional[_Iterable[_Union[_appspec_pb2.Target, _Mapping]]] = ..., target_profile_vec: _Optional[_Iterable[_Union[_appspec_pb2.TargetProfile, _Mapping]]] = ...) -> None: ...

class FailoverOptions(_message.Message):
    __slots__ = ("shut_primary_vms", "protect_vms", "view_dr_action_options")
    SHUT_PRIMARY_VMS_FIELD_NUMBER: _ClassVar[int]
    PROTECT_VMS_FIELD_NUMBER: _ClassVar[int]
    VIEW_DR_ACTION_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    shut_primary_vms: bool
    protect_vms: bool
    view_dr_action_options: ViewDRActionOptions
    def __init__(self, shut_primary_vms: bool = ..., protect_vms: bool = ..., view_dr_action_options: _Optional[_Union[ViewDRActionOptions, _Mapping]] = ...) -> None: ...

class ViewDRActionOptions(_message.Message):
    __slots__ = ("failover_action", "set_up_reverse_replication", "view_ids")
    class FailoverAction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kUnplannedFailover: _ClassVar[ViewDRActionOptions.FailoverAction]
        kPreparePlannedFailover: _ClassVar[ViewDRActionOptions.FailoverAction]
        kFinalisePlannedFailover: _ClassVar[ViewDRActionOptions.FailoverAction]
        kCancelFailover: _ClassVar[ViewDRActionOptions.FailoverAction]
    kUnplannedFailover: ViewDRActionOptions.FailoverAction
    kPreparePlannedFailover: ViewDRActionOptions.FailoverAction
    kFinalisePlannedFailover: ViewDRActionOptions.FailoverAction
    kCancelFailover: ViewDRActionOptions.FailoverAction
    FAILOVER_ACTION_FIELD_NUMBER: _ClassVar[int]
    SET_UP_REVERSE_REPLICATION_FIELD_NUMBER: _ClassVar[int]
    VIEW_IDS_FIELD_NUMBER: _ClassVar[int]
    failover_action: ViewDRActionOptions.FailoverAction
    set_up_reverse_replication: bool
    view_ids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, failover_action: _Optional[_Union[ViewDRActionOptions.FailoverAction, str]] = ..., set_up_reverse_replication: bool = ..., view_ids: _Optional[_Iterable[int]] = ...) -> None: ...
