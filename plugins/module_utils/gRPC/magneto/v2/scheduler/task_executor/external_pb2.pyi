from magneto.api import magneto_external_base_pb2 as _magneto_external_base_pb2
from magneto.base import error_pb2 as _error_pb2
from util.base import universal_id_pb2 as _universal_id_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BackupTaskSpecProto(_message.Message):
    __slots__ = ("task_uid", "run_uid")
    TASK_UID_FIELD_NUMBER: _ClassVar[int]
    RUN_UID_FIELD_NUMBER: _ClassVar[int]
    task_uid: _universal_id_pb2.UniversalIdProto
    run_uid: _universal_id_pb2.UniversalIdProto
    def __init__(self, task_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., run_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ...) -> None: ...

class StartBackupTasksArg(_message.Message):
    __slots__ = ("base", "task_spec_vec")
    BASE_FIELD_NUMBER: _ClassVar[int]
    TASK_SPEC_VEC_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ArgumentBase
    task_spec_vec: _containers.RepeatedCompositeFieldContainer[BackupTaskSpecProto]
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ArgumentBase, _Mapping]] = ..., task_spec_vec: _Optional[_Iterable[_Union[BackupTaskSpecProto, _Mapping]]] = ...) -> None: ...

class StartBackupTasksResult(_message.Message):
    __slots__ = ("base", "result_vec")
    class Result(_message.Message):
        __slots__ = ("task_uid", "error", "status")
        TASK_UID_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        task_uid: _universal_id_pb2.UniversalIdProto
        error: _error_pb2.ErrorProto
        status: TaskStatusProto
        def __init__(self, task_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., status: _Optional[_Union[TaskStatusProto, _Mapping]] = ...) -> None: ...
    BASE_FIELD_NUMBER: _ClassVar[int]
    RESULT_VEC_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ResultBase
    result_vec: _containers.RepeatedCompositeFieldContainer[StartBackupTasksResult.Result]
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ResultBase, _Mapping]] = ..., result_vec: _Optional[_Iterable[_Union[StartBackupTasksResult.Result, _Mapping]]] = ...) -> None: ...

class CancelTasksArg(_message.Message):
    __slots__ = ("base", "task_uid_vec", "graceful_cancelation_deadline_timestamp_usecs")
    BASE_FIELD_NUMBER: _ClassVar[int]
    TASK_UID_VEC_FIELD_NUMBER: _ClassVar[int]
    GRACEFUL_CANCELATION_DEADLINE_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ArgumentBase
    task_uid_vec: _containers.RepeatedCompositeFieldContainer[_universal_id_pb2.UniversalIdProto]
    graceful_cancelation_deadline_timestamp_usecs: int
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ArgumentBase, _Mapping]] = ..., task_uid_vec: _Optional[_Iterable[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]]] = ..., graceful_cancelation_deadline_timestamp_usecs: _Optional[int] = ...) -> None: ...

class CancelTasksResult(_message.Message):
    __slots__ = ("base", "result_vec")
    class Result(_message.Message):
        __slots__ = ("task_uid", "error")
        TASK_UID_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        task_uid: _universal_id_pb2.UniversalIdProto
        error: _error_pb2.ErrorProto
        def __init__(self, task_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...
    BASE_FIELD_NUMBER: _ClassVar[int]
    RESULT_VEC_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ResultBase
    result_vec: _containers.RepeatedCompositeFieldContainer[CancelTasksResult.Result]
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ResultBase, _Mapping]] = ..., result_vec: _Optional[_Iterable[_Union[CancelTasksResult.Result, _Mapping]]] = ...) -> None: ...

class PauseTasksArg(_message.Message):
    __slots__ = ("base", "task_uid_vec")
    BASE_FIELD_NUMBER: _ClassVar[int]
    TASK_UID_VEC_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ArgumentBase
    task_uid_vec: _containers.RepeatedCompositeFieldContainer[_universal_id_pb2.UniversalIdProto]
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ArgumentBase, _Mapping]] = ..., task_uid_vec: _Optional[_Iterable[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]]] = ...) -> None: ...

class PauseTasksResult(_message.Message):
    __slots__ = ("base", "result_vec")
    class Result(_message.Message):
        __slots__ = ("task_uid", "error")
        TASK_UID_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        task_uid: _universal_id_pb2.UniversalIdProto
        error: _error_pb2.ErrorProto
        def __init__(self, task_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...
    BASE_FIELD_NUMBER: _ClassVar[int]
    RESULT_VEC_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ResultBase
    result_vec: _containers.RepeatedCompositeFieldContainer[PauseTasksResult.Result]
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ResultBase, _Mapping]] = ..., result_vec: _Optional[_Iterable[_Union[PauseTasksResult.Result, _Mapping]]] = ...) -> None: ...

class PollTasksArg(_message.Message):
    __slots__ = ("base", "task_uid_vec")
    BASE_FIELD_NUMBER: _ClassVar[int]
    TASK_UID_VEC_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ArgumentBase
    task_uid_vec: _containers.RepeatedCompositeFieldContainer[_universal_id_pb2.UniversalIdProto]
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ArgumentBase, _Mapping]] = ..., task_uid_vec: _Optional[_Iterable[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]]] = ...) -> None: ...

class BackupTaskStatusProto(_message.Message):
    __slots__ = ("type", "error")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kRunning: _ClassVar[BackupTaskStatusProto.Type]
        kPausing: _ClassVar[BackupTaskStatusProto.Type]
        kPaused: _ClassVar[BackupTaskStatusProto.Type]
        kCanceling: _ClassVar[BackupTaskStatusProto.Type]
        kFinished: _ClassVar[BackupTaskStatusProto.Type]
    kRunning: BackupTaskStatusProto.Type
    kPausing: BackupTaskStatusProto.Type
    kPaused: BackupTaskStatusProto.Type
    kCanceling: BackupTaskStatusProto.Type
    kFinished: BackupTaskStatusProto.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    type: BackupTaskStatusProto.Type
    error: _error_pb2.ErrorProto
    def __init__(self, type: _Optional[_Union[BackupTaskStatusProto.Type, str]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class TaskStatusProto(_message.Message):
    __slots__ = ("backup_params",)
    BACKUP_PARAMS_FIELD_NUMBER: _ClassVar[int]
    backup_params: BackupTaskStatusProto
    def __init__(self, backup_params: _Optional[_Union[BackupTaskStatusProto, _Mapping]] = ...) -> None: ...

class PollTasksResult(_message.Message):
    __slots__ = ("base", "task_status_vec")
    class Status(_message.Message):
        __slots__ = ("uid", "error", "status")
        UID_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        uid: _universal_id_pb2.UniversalIdProto
        error: _error_pb2.ErrorProto
        status: TaskStatusProto
        def __init__(self, uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., status: _Optional[_Union[TaskStatusProto, _Mapping]] = ...) -> None: ...
    BASE_FIELD_NUMBER: _ClassVar[int]
    TASK_STATUS_VEC_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ResultBase
    task_status_vec: _containers.RepeatedCompositeFieldContainer[PollTasksResult.Status]
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ResultBase, _Mapping]] = ..., task_status_vec: _Optional[_Iterable[_Union[PollTasksResult.Status, _Mapping]]] = ...) -> None: ...
