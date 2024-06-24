from stats.base import pulse_pb2 as _pulse_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RemovalState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kDontRemove: _ClassVar[RemovalState]
    kMarkedForRemoval: _ClassVar[RemovalState]
    kOkToRemove: _ClassVar[RemovalState]

class IntentRecordState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kTaskCreated: _ClassVar[IntentRecordState]
    kTaskFinished: _ClassVar[IntentRecordState]
kDontRemove: RemovalState
kMarkedForRemoval: RemovalState
kOkToRemove: RemovalState
kTaskCreated: IntentRecordState
kTaskFinished: IntentRecordState

class TaskPolicy(_message.Message):
    __slots__ = ("weight", "hung_task_timeout_secs", "disable_implicit_finish")
    WEIGHT_FIELD_NUMBER: _ClassVar[int]
    HUNG_TASK_TIMEOUT_SECS_FIELD_NUMBER: _ClassVar[int]
    DISABLE_IMPLICIT_FINISH_FIELD_NUMBER: _ClassVar[int]
    weight: int
    hung_task_timeout_secs: int
    disable_implicit_finish: bool
    def __init__(self, weight: _Optional[int] = ..., hung_task_timeout_secs: _Optional[int] = ..., disable_implicit_finish: bool = ...) -> None: ...

class EventLogs(_message.Message):
    __slots__ = ("event_vec",)
    EVENT_VEC_FIELD_NUMBER: _ClassVar[int]
    event_vec: _containers.RepeatedCompositeFieldContainer[_pulse_pb2.TaskEvent]
    def __init__(self, event_vec: _Optional[_Iterable[_Union[_pulse_pb2.TaskEvent, _Mapping]]] = ...) -> None: ...

class TaskStateProto(_message.Message):
    __slots__ = ("task_path", "progress", "policy", "sub_task_vec")
    TASK_PATH_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_FIELD_NUMBER: _ClassVar[int]
    POLICY_FIELD_NUMBER: _ClassVar[int]
    SUB_TASK_VEC_FIELD_NUMBER: _ClassVar[int]
    task_path: str
    progress: _pulse_pb2.TaskProgress
    policy: TaskPolicy
    sub_task_vec: _containers.RepeatedCompositeFieldContainer[TaskStateProto]
    def __init__(self, task_path: _Optional[str] = ..., progress: _Optional[_Union[_pulse_pb2.TaskProgress, _Mapping]] = ..., policy: _Optional[_Union[TaskPolicy, _Mapping]] = ..., sub_task_vec: _Optional[_Iterable[_Union[TaskStateProto, _Mapping]]] = ...) -> None: ...

class WALRootTaskMetadata(_message.Message):
    __slots__ = ("task_path", "scribe_row_id", "start_time_secs", "end_time_secs", "removal_state", "intent_record_state", "are_logs_in_snapfs", "logs_dir_structure")
    TASK_PATH_FIELD_NUMBER: _ClassVar[int]
    SCRIBE_ROW_ID_FIELD_NUMBER: _ClassVar[int]
    START_TIME_SECS_FIELD_NUMBER: _ClassVar[int]
    END_TIME_SECS_FIELD_NUMBER: _ClassVar[int]
    REMOVAL_STATE_FIELD_NUMBER: _ClassVar[int]
    INTENT_RECORD_STATE_FIELD_NUMBER: _ClassVar[int]
    ARE_LOGS_IN_SNAPFS_FIELD_NUMBER: _ClassVar[int]
    LOGS_DIR_STRUCTURE_FIELD_NUMBER: _ClassVar[int]
    task_path: str
    scribe_row_id: int
    start_time_secs: int
    end_time_secs: int
    removal_state: RemovalState
    intent_record_state: IntentRecordState
    are_logs_in_snapfs: bool
    logs_dir_structure: _pulse_pb2.EventLogsDirStructure
    def __init__(self, task_path: _Optional[str] = ..., scribe_row_id: _Optional[int] = ..., start_time_secs: _Optional[int] = ..., end_time_secs: _Optional[int] = ..., removal_state: _Optional[_Union[RemovalState, str]] = ..., intent_record_state: _Optional[_Union[IntentRecordState, str]] = ..., are_logs_in_snapfs: bool = ..., logs_dir_structure: _Optional[_Union[_pulse_pb2.EventLogsDirStructure, _Mapping]] = ...) -> None: ...

class WALStateProto(_message.Message):
    __slots__ = ("root_task_vec", "saved_id_generator", "pulse_view_info")
    class PulseViewInfo(_message.Message):
        __slots__ = ("pulse_view_name", "suffix_id")
        PULSE_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
        SUFFIX_ID_FIELD_NUMBER: _ClassVar[int]
        pulse_view_name: str
        suffix_id: int
        def __init__(self, pulse_view_name: _Optional[str] = ..., suffix_id: _Optional[int] = ...) -> None: ...
    ROOT_TASK_VEC_FIELD_NUMBER: _ClassVar[int]
    SAVED_ID_GENERATOR_FIELD_NUMBER: _ClassVar[int]
    PULSE_VIEW_INFO_FIELD_NUMBER: _ClassVar[int]
    root_task_vec: _containers.RepeatedCompositeFieldContainer[WALRootTaskMetadata]
    saved_id_generator: int
    pulse_view_info: WALStateProto.PulseViewInfo
    def __init__(self, root_task_vec: _Optional[_Iterable[_Union[WALRootTaskMetadata, _Mapping]]] = ..., saved_id_generator: _Optional[int] = ..., pulse_view_info: _Optional[_Union[WALStateProto.PulseViewInfo, _Mapping]] = ...) -> None: ...
