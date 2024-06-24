from magneto.base import enums_pb2 as _enums_pb2
from magneto.base import error_pb2 as _error_pb2
from magneto.base import magneto_pb2 as _magneto_pb2
from magneto.base import env_params_pb2 as _env_params_pb2
from magneto.object_graph import base_pb2 as _base_pb2
from util.base import universal_id_pb2 as _universal_id_pb2
from magneto.api import magneto_external_pb2 as _magneto_external_pb2
from magneto.api import magneto_external_base_pb2 as _magneto_external_base_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ProtectClonesArgs(_message.Message):
    __slots__ = ("task_uid",)
    TASK_UID_FIELD_NUMBER: _ClassVar[int]
    task_uid: _universal_id_pb2.UniversalIdProto
    def __init__(self, task_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ...) -> None: ...

class ProtectClonesResults(_message.Message):
    __slots__ = ("result_vec",)
    class Result(_message.Message):
        __slots__ = ("clone_entity_uid", "view_clone_name", "relative_path", "status")
        CLONE_ENTITY_UID_FIELD_NUMBER: _ClassVar[int]
        VIEW_CLONE_NAME_FIELD_NUMBER: _ClassVar[int]
        RELATIVE_PATH_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        clone_entity_uid: _universal_id_pb2.UniversalIdProto
        view_clone_name: str
        relative_path: str
        status: _error_pb2.ErrorProto
        def __init__(self, clone_entity_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., view_clone_name: _Optional[str] = ..., relative_path: _Optional[str] = ..., status: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...
    RESULT_VEC_FIELD_NUMBER: _ClassVar[int]
    result_vec: _containers.RepeatedCompositeFieldContainer[ProtectClonesResults.Result]
    def __init__(self, result_vec: _Optional[_Iterable[_Union[ProtectClonesResults.Result, _Mapping]]] = ...) -> None: ...

class ProtectClonesTaskDetails(_message.Message):
    __slots__ = ("clone_entity_uid_vec", "view_params", "pre_script", "post_script")
    CLONE_ENTITY_UID_VEC_FIELD_NUMBER: _ClassVar[int]
    VIEW_PARAMS_FIELD_NUMBER: _ClassVar[int]
    PRE_SCRIPT_FIELD_NUMBER: _ClassVar[int]
    POST_SCRIPT_FIELD_NUMBER: _ClassVar[int]
    clone_entity_uid_vec: _containers.RepeatedCompositeFieldContainer[_universal_id_pb2.UniversalIdProto]
    view_params: _magneto_external_pb2.ViewParamsProto
    pre_script: _magneto_external_base_pb2.RemoteScriptProto
    post_script: _magneto_external_base_pb2.RemoteScriptProto
    def __init__(self, clone_entity_uid_vec: _Optional[_Iterable[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]]] = ..., view_params: _Optional[_Union[_magneto_external_pb2.ViewParamsProto, _Mapping]] = ..., pre_script: _Optional[_Union[_magneto_external_base_pb2.RemoteScriptProto, _Mapping]] = ..., post_script: _Optional[_Union[_magneto_external_base_pb2.RemoteScriptProto, _Mapping]] = ...) -> None: ...

class ProtectClonesTaskState(_message.Message):
    __slots__ = ("state", "intermediate_state", "accumulated_result")
    class TaskState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kFetchTaskDetails: _ClassVar[ProtectClonesTaskState.TaskState]
        kBatchClones: _ClassVar[ProtectClonesTaskState.TaskState]
        kBatchSnapshot: _ClassVar[ProtectClonesTaskState.TaskState]
        kUpdateGraphTaskNode: _ClassVar[ProtectClonesTaskState.TaskState]
        kDone: _ClassVar[ProtectClonesTaskState.TaskState]
    kFetchTaskDetails: ProtectClonesTaskState.TaskState
    kBatchClones: ProtectClonesTaskState.TaskState
    kBatchSnapshot: ProtectClonesTaskState.TaskState
    kUpdateGraphTaskNode: ProtectClonesTaskState.TaskState
    kDone: ProtectClonesTaskState.TaskState
    class ProtectClonesSubTask(_message.Message):
        __slots__ = ("subtasks",)
        class SubTask(_message.Message):
            __slots__ = ("name", "arg")
            NAME_FIELD_NUMBER: _ClassVar[int]
            ARG_FIELD_NUMBER: _ClassVar[int]
            name: str
            arg: CloneBatchSnapshotArgs
            def __init__(self, name: _Optional[str] = ..., arg: _Optional[_Union[CloneBatchSnapshotArgs, _Mapping]] = ...) -> None: ...
        SUBTASKS_FIELD_NUMBER: _ClassVar[int]
        subtasks: _containers.RepeatedCompositeFieldContainer[ProtectClonesTaskState.ProtectClonesSubTask.SubTask]
        def __init__(self, subtasks: _Optional[_Iterable[_Union[ProtectClonesTaskState.ProtectClonesSubTask.SubTask, _Mapping]]] = ...) -> None: ...
    class IntermediateState(_message.Message):
        __slots__ = ("task_details", "pending_subtasks")
        TASK_DETAILS_FIELD_NUMBER: _ClassVar[int]
        PENDING_SUBTASKS_FIELD_NUMBER: _ClassVar[int]
        task_details: ProtectClonesTaskDetails
        pending_subtasks: ProtectClonesTaskState.ProtectClonesSubTask
        def __init__(self, task_details: _Optional[_Union[ProtectClonesTaskDetails, _Mapping]] = ..., pending_subtasks: _Optional[_Union[ProtectClonesTaskState.ProtectClonesSubTask, _Mapping]] = ...) -> None: ...
    STATE_FIELD_NUMBER: _ClassVar[int]
    INTERMEDIATE_STATE_FIELD_NUMBER: _ClassVar[int]
    ACCUMULATED_RESULT_FIELD_NUMBER: _ClassVar[int]
    state: ProtectClonesTaskState.TaskState
    intermediate_state: ProtectClonesTaskState.IntermediateState
    accumulated_result: _containers.RepeatedCompositeFieldContainer[ProtectClonesResults.Result]
    def __init__(self, state: _Optional[_Union[ProtectClonesTaskState.TaskState, str]] = ..., intermediate_state: _Optional[_Union[ProtectClonesTaskState.IntermediateState, _Mapping]] = ..., accumulated_result: _Optional[_Iterable[_Union[ProtectClonesResults.Result, _Mapping]]] = ...) -> None: ...

class CloneBatchSnapshotArgs(_message.Message):
    __slots__ = ("task_uid", "host_uid", "clone_args", "requires_host_snapshot", "env_type", "progress_monitor_path_prefix")
    TASK_UID_FIELD_NUMBER: _ClassVar[int]
    HOST_UID_FIELD_NUMBER: _ClassVar[int]
    CLONE_ARGS_FIELD_NUMBER: _ClassVar[int]
    REQUIRES_HOST_SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    ENV_TYPE_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_MONITOR_PATH_PREFIX_FIELD_NUMBER: _ClassVar[int]
    task_uid: _universal_id_pb2.UniversalIdProto
    host_uid: _universal_id_pb2.UniversalIdProto
    clone_args: ProtectClonesTaskDetails
    requires_host_snapshot: bool
    env_type: _enums_pb2.Environment.Type
    progress_monitor_path_prefix: str
    def __init__(self, task_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., host_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., clone_args: _Optional[_Union[ProtectClonesTaskDetails, _Mapping]] = ..., requires_host_snapshot: bool = ..., env_type: _Optional[_Union[_enums_pb2.Environment.Type, str]] = ..., progress_monitor_path_prefix: _Optional[str] = ...) -> None: ...

class CloneBatchSnapshotResult(_message.Message):
    __slots__ = ("accumulated_result",)
    ACCUMULATED_RESULT_FIELD_NUMBER: _ClassVar[int]
    accumulated_result: ProtectClonesResults
    def __init__(self, accumulated_result: _Optional[_Union[ProtectClonesResults, _Mapping]] = ...) -> None: ...

class CloneViewBatchState(_message.Message):
    __slots__ = ("args", "result")
    class CloneViewBatchArgs(_message.Message):
        __slots__ = ("src_view_name", "tgt_view_name", "clone_info_vec")
        class CloneInfo(_message.Message):
            __slots__ = ("clone_uid", "relative_path")
            CLONE_UID_FIELD_NUMBER: _ClassVar[int]
            RELATIVE_PATH_FIELD_NUMBER: _ClassVar[int]
            clone_uid: _universal_id_pb2.UniversalIdProto
            relative_path: str
            def __init__(self, clone_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., relative_path: _Optional[str] = ...) -> None: ...
        SRC_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
        TGT_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
        CLONE_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
        src_view_name: str
        tgt_view_name: str
        clone_info_vec: _containers.RepeatedCompositeFieldContainer[CloneViewBatchState.CloneViewBatchArgs.CloneInfo]
        def __init__(self, src_view_name: _Optional[str] = ..., tgt_view_name: _Optional[str] = ..., clone_info_vec: _Optional[_Iterable[_Union[CloneViewBatchState.CloneViewBatchArgs.CloneInfo, _Mapping]]] = ...) -> None: ...
    class CloneViewBatchResults(_message.Message):
        __slots__ = ("status", "snapshot_time_usecs")
        STATUS_FIELD_NUMBER: _ClassVar[int]
        SNAPSHOT_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
        status: _error_pb2.ErrorProto
        snapshot_time_usecs: int
        def __init__(self, status: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., snapshot_time_usecs: _Optional[int] = ...) -> None: ...
    ARGS_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    args: CloneViewBatchState.CloneViewBatchArgs
    result: CloneViewBatchState.CloneViewBatchResults
    def __init__(self, args: _Optional[_Union[CloneViewBatchState.CloneViewBatchArgs, _Mapping]] = ..., result: _Optional[_Union[CloneViewBatchState.CloneViewBatchResults, _Mapping]] = ...) -> None: ...

class CloneBatchSnapshotTaskState(_message.Message):
    __slots__ = ("state", "progress_monitor_sub_task_path", "intermediate_state", "accumulated_result")
    class TaskState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kPreExecuteScripts: _ClassVar[CloneBatchSnapshotTaskState.TaskState]
        kPreSnapshot: _ClassVar[CloneBatchSnapshotTaskState.TaskState]
        kSnapshot: _ClassVar[CloneBatchSnapshotTaskState.TaskState]
        kBatchClones: _ClassVar[CloneBatchSnapshotTaskState.TaskState]
        kCloneView: _ClassVar[CloneBatchSnapshotTaskState.TaskState]
        kPostSnapshot: _ClassVar[CloneBatchSnapshotTaskState.TaskState]
        kQueryDatabase: _ClassVar[CloneBatchSnapshotTaskState.TaskState]
        kUpdateGraph: _ClassVar[CloneBatchSnapshotTaskState.TaskState]
        kPostExecuteScripts: _ClassVar[CloneBatchSnapshotTaskState.TaskState]
        kNotifyYoda: _ClassVar[CloneBatchSnapshotTaskState.TaskState]
        kDone: _ClassVar[CloneBatchSnapshotTaskState.TaskState]
    kPreExecuteScripts: CloneBatchSnapshotTaskState.TaskState
    kPreSnapshot: CloneBatchSnapshotTaskState.TaskState
    kSnapshot: CloneBatchSnapshotTaskState.TaskState
    kBatchClones: CloneBatchSnapshotTaskState.TaskState
    kCloneView: CloneBatchSnapshotTaskState.TaskState
    kPostSnapshot: CloneBatchSnapshotTaskState.TaskState
    kQueryDatabase: CloneBatchSnapshotTaskState.TaskState
    kUpdateGraph: CloneBatchSnapshotTaskState.TaskState
    kPostExecuteScripts: CloneBatchSnapshotTaskState.TaskState
    kNotifyYoda: CloneBatchSnapshotTaskState.TaskState
    kDone: CloneBatchSnapshotTaskState.TaskState
    class IntermediateState(_message.Message):
        __slots__ = ("pre_snapshot_script_status", "pre_snapshot_state", "snapshot_state", "clone_view_batch_state_vec", "post_snapshot_state", "post_backup_script_status", "metadata_state")
        PRE_SNAPSHOT_SCRIPT_STATUS_FIELD_NUMBER: _ClassVar[int]
        PRE_SNAPSHOT_STATE_FIELD_NUMBER: _ClassVar[int]
        SNAPSHOT_STATE_FIELD_NUMBER: _ClassVar[int]
        CLONE_VIEW_BATCH_STATE_VEC_FIELD_NUMBER: _ClassVar[int]
        POST_SNAPSHOT_STATE_FIELD_NUMBER: _ClassVar[int]
        POST_BACKUP_SCRIPT_STATUS_FIELD_NUMBER: _ClassVar[int]
        METADATA_STATE_FIELD_NUMBER: _ClassVar[int]
        pre_snapshot_script_status: _magneto_pb2.ScriptExecutionStatus
        pre_snapshot_state: _base_pb2.PreSnapshotResultProto
        snapshot_state: _base_pb2.SnapshotResultProto
        clone_view_batch_state_vec: _containers.RepeatedCompositeFieldContainer[CloneViewBatchState]
        post_snapshot_state: _base_pb2.PostSnapshotResultProto
        post_backup_script_status: _magneto_pb2.ScriptExecutionStatus
        metadata_state: _base_pb2.DatabaseMetadataProto
        def __init__(self, pre_snapshot_script_status: _Optional[_Union[_magneto_pb2.ScriptExecutionStatus, _Mapping]] = ..., pre_snapshot_state: _Optional[_Union[_base_pb2.PreSnapshotResultProto, _Mapping]] = ..., snapshot_state: _Optional[_Union[_base_pb2.SnapshotResultProto, _Mapping]] = ..., clone_view_batch_state_vec: _Optional[_Iterable[_Union[CloneViewBatchState, _Mapping]]] = ..., post_snapshot_state: _Optional[_Union[_base_pb2.PostSnapshotResultProto, _Mapping]] = ..., post_backup_script_status: _Optional[_Union[_magneto_pb2.ScriptExecutionStatus, _Mapping]] = ..., metadata_state: _Optional[_Union[_base_pb2.DatabaseMetadataProto, _Mapping]] = ...) -> None: ...
    STATE_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_MONITOR_SUB_TASK_PATH_FIELD_NUMBER: _ClassVar[int]
    INTERMEDIATE_STATE_FIELD_NUMBER: _ClassVar[int]
    ACCUMULATED_RESULT_FIELD_NUMBER: _ClassVar[int]
    state: CloneBatchSnapshotTaskState.TaskState
    progress_monitor_sub_task_path: str
    intermediate_state: CloneBatchSnapshotTaskState.IntermediateState
    accumulated_result: CloneBatchSnapshotResult
    def __init__(self, state: _Optional[_Union[CloneBatchSnapshotTaskState.TaskState, str]] = ..., progress_monitor_sub_task_path: _Optional[str] = ..., intermediate_state: _Optional[_Union[CloneBatchSnapshotTaskState.IntermediateState, _Mapping]] = ..., accumulated_result: _Optional[_Union[CloneBatchSnapshotResult, _Mapping]] = ...) -> None: ...
