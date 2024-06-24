from athena.apps.insight.base import common_pb2 as _common_pb2
from athena.apps.insight.base import directory_walker_pb2 as _directory_walker_pb2
from athena.apps.insight.base import error_pb2 as _error_pb2
from athena.apps.insight.base import task_pb2 as _task_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MinionStateProto(_message.Message):
    __slots__ = ("endpt", "info", "sub_task_spec_vec", "last_heartbeat_time_nsecs")
    ENDPT_FIELD_NUMBER: _ClassVar[int]
    INFO_FIELD_NUMBER: _ClassVar[int]
    SUB_TASK_SPEC_VEC_FIELD_NUMBER: _ClassVar[int]
    LAST_HEARTBEAT_TIME_NSECS_FIELD_NUMBER: _ClassVar[int]
    endpt: _common_pb2.MinionTcpEndpointProto
    info: _common_pb2.MinionInfoProto
    sub_task_spec_vec: _containers.RepeatedCompositeFieldContainer[_task_pb2.SubTaskSpecProto]
    last_heartbeat_time_nsecs: int
    def __init__(self, endpt: _Optional[_Union[_common_pb2.MinionTcpEndpointProto, _Mapping]] = ..., info: _Optional[_Union[_common_pb2.MinionInfoProto, _Mapping]] = ..., sub_task_spec_vec: _Optional[_Iterable[_Union[_task_pb2.SubTaskSpecProto, _Mapping]]] = ..., last_heartbeat_time_nsecs: _Optional[int] = ...) -> None: ...

class SubTaskEnumerationStateProto(_message.Message):
    __slots__ = ("task_id", "listing_file_relative_path", "listing_file_last_sync_offset", "next_sub_task_id", "start_time_nsecs", "state", "end_time_nsecs", "error")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kRunning: _ClassVar[SubTaskEnumerationStateProto.State]
        kFinished: _ClassVar[SubTaskEnumerationStateProto.State]
    kRunning: SubTaskEnumerationStateProto.State
    kFinished: SubTaskEnumerationStateProto.State
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    LISTING_FILE_RELATIVE_PATH_FIELD_NUMBER: _ClassVar[int]
    LISTING_FILE_LAST_SYNC_OFFSET_FIELD_NUMBER: _ClassVar[int]
    NEXT_SUB_TASK_ID_FIELD_NUMBER: _ClassVar[int]
    START_TIME_NSECS_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    END_TIME_NSECS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    task_id: int
    listing_file_relative_path: str
    listing_file_last_sync_offset: int
    next_sub_task_id: int
    start_time_nsecs: int
    state: SubTaskEnumerationStateProto.State
    end_time_nsecs: int
    error: _error_pb2.ErrorProto
    def __init__(self, task_id: _Optional[int] = ..., listing_file_relative_path: _Optional[str] = ..., listing_file_last_sync_offset: _Optional[int] = ..., next_sub_task_id: _Optional[int] = ..., start_time_nsecs: _Optional[int] = ..., state: _Optional[_Union[SubTaskEnumerationStateProto.State, str]] = ..., end_time_nsecs: _Optional[int] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class SubTaskExecutionStateProto(_message.Message):
    __slots__ = ("task_id", "running_subtask_state_vec", "ready_subtask_spec_vec", "listing_file_next_read_offset")
    class SubTaskState(_message.Message):
        __slots__ = ("spec", "state")
        SPEC_FIELD_NUMBER: _ClassVar[int]
        STATE_FIELD_NUMBER: _ClassVar[int]
        spec: _task_pb2.SubTaskSpecProto
        state: _task_pb2.SubTaskStateProto
        def __init__(self, spec: _Optional[_Union[_task_pb2.SubTaskSpecProto, _Mapping]] = ..., state: _Optional[_Union[_task_pb2.SubTaskStateProto, _Mapping]] = ...) -> None: ...
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    RUNNING_SUBTASK_STATE_VEC_FIELD_NUMBER: _ClassVar[int]
    READY_SUBTASK_SPEC_VEC_FIELD_NUMBER: _ClassVar[int]
    LISTING_FILE_NEXT_READ_OFFSET_FIELD_NUMBER: _ClassVar[int]
    task_id: int
    running_subtask_state_vec: _containers.RepeatedCompositeFieldContainer[SubTaskExecutionStateProto.SubTaskState]
    ready_subtask_spec_vec: _containers.RepeatedCompositeFieldContainer[_task_pb2.SubTaskSpecProto]
    listing_file_next_read_offset: int
    def __init__(self, task_id: _Optional[int] = ..., running_subtask_state_vec: _Optional[_Iterable[_Union[SubTaskExecutionStateProto.SubTaskState, _Mapping]]] = ..., ready_subtask_spec_vec: _Optional[_Iterable[_Union[_task_pb2.SubTaskSpecProto, _Mapping]]] = ..., listing_file_next_read_offset: _Optional[int] = ...) -> None: ...

class ActiveTaskStateProto(_message.Message):
    __slots__ = ("task", "directory_walker_state", "directory_differ_state", "sub_task_enumeration_state", "sub_task_execution_state")
    TASK_FIELD_NUMBER: _ClassVar[int]
    DIRECTORY_WALKER_STATE_FIELD_NUMBER: _ClassVar[int]
    DIRECTORY_DIFFER_STATE_FIELD_NUMBER: _ClassVar[int]
    SUB_TASK_ENUMERATION_STATE_FIELD_NUMBER: _ClassVar[int]
    SUB_TASK_EXECUTION_STATE_FIELD_NUMBER: _ClassVar[int]
    task: _task_pb2.TaskProto
    directory_walker_state: _directory_walker_pb2.DirectoryWalkerStateProto
    directory_differ_state: _directory_walker_pb2.DirectoryDifferStateProto
    sub_task_enumeration_state: SubTaskEnumerationStateProto
    sub_task_execution_state: SubTaskExecutionStateProto
    def __init__(self, task: _Optional[_Union[_task_pb2.TaskProto, _Mapping]] = ..., directory_walker_state: _Optional[_Union[_directory_walker_pb2.DirectoryWalkerStateProto, _Mapping]] = ..., directory_differ_state: _Optional[_Union[_directory_walker_pb2.DirectoryDifferStateProto, _Mapping]] = ..., sub_task_enumeration_state: _Optional[_Union[SubTaskEnumerationStateProto, _Mapping]] = ..., sub_task_execution_state: _Optional[_Union[SubTaskExecutionStateProto, _Mapping]] = ...) -> None: ...

class ObjectStateProto(_message.Message):
    __slots__ = ("object", "active_task", "past_task_vec", "last_successful_task_final_state", "index_incarnation", "last_index_healthy_timestamp_nsecs", "non_existent")
    OBJECT_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_TASK_FIELD_NUMBER: _ClassVar[int]
    PAST_TASK_VEC_FIELD_NUMBER: _ClassVar[int]
    LAST_SUCCESSFUL_TASK_FINAL_STATE_FIELD_NUMBER: _ClassVar[int]
    INDEX_INCARNATION_FIELD_NUMBER: _ClassVar[int]
    LAST_INDEX_HEALTHY_TIMESTAMP_NSECS_FIELD_NUMBER: _ClassVar[int]
    NON_EXISTENT_FIELD_NUMBER: _ClassVar[int]
    object: _task_pb2.ObjectProto
    active_task: ActiveTaskStateProto
    past_task_vec: _containers.RepeatedCompositeFieldContainer[_task_pb2.TaskProto]
    last_successful_task_final_state: ActiveTaskStateProto
    index_incarnation: int
    last_index_healthy_timestamp_nsecs: int
    non_existent: bool
    def __init__(self, object: _Optional[_Union[_task_pb2.ObjectProto, _Mapping]] = ..., active_task: _Optional[_Union[ActiveTaskStateProto, _Mapping]] = ..., past_task_vec: _Optional[_Iterable[_Union[_task_pb2.TaskProto, _Mapping]]] = ..., last_successful_task_final_state: _Optional[_Union[ActiveTaskStateProto, _Mapping]] = ..., index_incarnation: _Optional[int] = ..., last_index_healthy_timestamp_nsecs: _Optional[int] = ..., non_existent: bool = ...) -> None: ...

class MasterCheckpointProto(_message.Message):
    __slots__ = ("minion_state_vec", "object_state_vec", "file_filter", "next_object_id", "next_task_id", "total_volumes_map")
    class TotalVolumesMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    MINION_STATE_VEC_FIELD_NUMBER: _ClassVar[int]
    OBJECT_STATE_VEC_FIELD_NUMBER: _ClassVar[int]
    FILE_FILTER_FIELD_NUMBER: _ClassVar[int]
    NEXT_OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    NEXT_TASK_ID_FIELD_NUMBER: _ClassVar[int]
    TOTAL_VOLUMES_MAP_FIELD_NUMBER: _ClassVar[int]
    minion_state_vec: _containers.RepeatedCompositeFieldContainer[MinionStateProto]
    object_state_vec: _containers.RepeatedCompositeFieldContainer[ObjectStateProto]
    file_filter: _task_pb2.FileFilterProto
    next_object_id: int
    next_task_id: int
    total_volumes_map: _containers.ScalarMap[int, int]
    def __init__(self, minion_state_vec: _Optional[_Iterable[_Union[MinionStateProto, _Mapping]]] = ..., object_state_vec: _Optional[_Iterable[_Union[ObjectStateProto, _Mapping]]] = ..., file_filter: _Optional[_Union[_task_pb2.FileFilterProto, _Mapping]] = ..., next_object_id: _Optional[int] = ..., next_task_id: _Optional[int] = ..., total_volumes_map: _Optional[_Mapping[int, int]] = ...) -> None: ...
