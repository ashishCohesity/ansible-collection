from magnus.base import error_pb2 as _error_pb2
from magnus.base import server_pb2 as _server_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RegisterActorArg(_message.Message):
    __slots__ = ("actor", "actor_heartbeat_fail_crash_duration_msecs", "capacity")
    ACTOR_FIELD_NUMBER: _ClassVar[int]
    ACTOR_HEARTBEAT_FAIL_CRASH_DURATION_MSECS_FIELD_NUMBER: _ClassVar[int]
    CAPACITY_FIELD_NUMBER: _ClassVar[int]
    actor: _server_pb2.ActorIncarnationProto
    actor_heartbeat_fail_crash_duration_msecs: int
    capacity: int
    def __init__(self, actor: _Optional[_Union[_server_pb2.ActorIncarnationProto, _Mapping]] = ..., actor_heartbeat_fail_crash_duration_msecs: _Optional[int] = ..., capacity: _Optional[int] = ...) -> None: ...

class RegisterActorResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class FetchIncarnationIdArg(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class FetchIncarnationIdResult(_message.Message):
    __slots__ = ("error", "incarnation_id")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    incarnation_id: int
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., incarnation_id: _Optional[int] = ...) -> None: ...

class ActorToServerHeartbeatArg(_message.Message):
    __slots__ = ("actor",)
    ACTOR_FIELD_NUMBER: _ClassVar[int]
    actor: _server_pb2.ActorIncarnationProto
    def __init__(self, actor: _Optional[_Union[_server_pb2.ActorIncarnationProto, _Mapping]] = ...) -> None: ...

class ActorToServerHeartbeatResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class ActorToServerUpdateArg(_message.Message):
    __slots__ = ("actor", "msg_id", "task_status")
    ACTOR_FIELD_NUMBER: _ClassVar[int]
    MSG_ID_FIELD_NUMBER: _ClassVar[int]
    TASK_STATUS_FIELD_NUMBER: _ClassVar[int]
    actor: _server_pb2.ActorIncarnationProto
    msg_id: int
    task_status: _containers.RepeatedCompositeFieldContainer[_server_pb2.TaskStateProto]
    def __init__(self, actor: _Optional[_Union[_server_pb2.ActorIncarnationProto, _Mapping]] = ..., msg_id: _Optional[int] = ..., task_status: _Optional[_Iterable[_Union[_server_pb2.TaskStateProto, _Mapping]]] = ...) -> None: ...

class ActorToServerUpdateResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class FetchWorkFromServerArg(_message.Message):
    __slots__ = ("actor",)
    ACTOR_FIELD_NUMBER: _ClassVar[int]
    actor: _server_pb2.ActorIncarnationProto
    def __init__(self, actor: _Optional[_Union[_server_pb2.ActorIncarnationProto, _Mapping]] = ...) -> None: ...

class FetchWorkFromServerResult(_message.Message):
    __slots__ = ("error", "active_tasks")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_TASKS_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    active_tasks: _containers.RepeatedCompositeFieldContainer[_server_pb2.TaskStateProto]
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., active_tasks: _Optional[_Iterable[_Union[_server_pb2.TaskStateProto, _Mapping]]] = ...) -> None: ...
