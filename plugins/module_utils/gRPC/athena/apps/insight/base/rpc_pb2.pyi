from athena.apps.insight.base import common_pb2 as _common_pb2
from athena.apps.insight.base import task_pb2 as _task_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HeartbeatArg(_message.Message):
    __slots__ = ("endpt", "info", "stats")
    ENDPT_FIELD_NUMBER: _ClassVar[int]
    INFO_FIELD_NUMBER: _ClassVar[int]
    STATS_FIELD_NUMBER: _ClassVar[int]
    endpt: _common_pb2.MinionTcpEndpointProto
    info: _common_pb2.MinionInfoProto
    stats: _common_pb2.MinionStatsProto
    def __init__(self, endpt: _Optional[_Union[_common_pb2.MinionTcpEndpointProto, _Mapping]] = ..., info: _Optional[_Union[_common_pb2.MinionInfoProto, _Mapping]] = ..., stats: _Optional[_Union[_common_pb2.MinionStatsProto, _Mapping]] = ...) -> None: ...

class HeartbeatResult(_message.Message):
    __slots__ = ("modified_gflags",)
    class ModifiedGflagsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    MODIFIED_GFLAGS_FIELD_NUMBER: _ClassVar[int]
    modified_gflags: _containers.ScalarMap[str, str]
    def __init__(self, modified_gflags: _Optional[_Mapping[str, str]] = ...) -> None: ...

class ExecuteSubTasksArg(_message.Message):
    __slots__ = ("sub_task_vec", "delete_subtasks")
    class SubTaskArg(_message.Message):
        __slots__ = ("spec", "index_name")
        SPEC_FIELD_NUMBER: _ClassVar[int]
        INDEX_NAME_FIELD_NUMBER: _ClassVar[int]
        spec: _task_pb2.SubTaskSpecProto
        index_name: str
        def __init__(self, spec: _Optional[_Union[_task_pb2.SubTaskSpecProto, _Mapping]] = ..., index_name: _Optional[str] = ...) -> None: ...
    SUB_TASK_VEC_FIELD_NUMBER: _ClassVar[int]
    DELETE_SUBTASKS_FIELD_NUMBER: _ClassVar[int]
    sub_task_vec: _containers.RepeatedCompositeFieldContainer[ExecuteSubTasksArg.SubTaskArg]
    delete_subtasks: bool
    def __init__(self, sub_task_vec: _Optional[_Iterable[_Union[ExecuteSubTasksArg.SubTaskArg, _Mapping]]] = ..., delete_subtasks: bool = ...) -> None: ...

class ExecuteSubTasksResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListSubTasksArg(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetObjectConfigArg(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetObjectConfigResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class NotifyObjectConfigChangeArg(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class NotifyObjectConfigChangeResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
