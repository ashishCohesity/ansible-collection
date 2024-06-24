from magneto.api import magneto_external_base_pb2 as _magneto_external_base_pb2
from magneto.base import error_pb2 as _error_pb2
from util.base import universal_id_pb2 as _universal_id_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AddOrUpdateJobArg(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AddOrUpdateJobResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RemoveJobArg(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RemoveJobResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AddOrUpdateProtectionSpecArg(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AddOrUpdateProtectionSpecResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RemoveProtectionSpecArg(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RemoveProtectionSpecResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AddOrUpdatePolicyArg(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AddOrUpdatePolicyResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RemovePolicyArg(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RemovePolicyResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CancelTasksArg(_message.Message):
    __slots__ = ("base", "run_uid", "task_uid_vec")
    BASE_FIELD_NUMBER: _ClassVar[int]
    RUN_UID_FIELD_NUMBER: _ClassVar[int]
    TASK_UID_VEC_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ArgumentBase
    run_uid: _universal_id_pb2.UniversalIdProto
    task_uid_vec: _containers.RepeatedCompositeFieldContainer[_universal_id_pb2.UniversalIdProto]
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ArgumentBase, _Mapping]] = ..., run_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., task_uid_vec: _Optional[_Iterable[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]]] = ...) -> None: ...

class CancelTasksResult(_message.Message):
    __slots__ = ("base", "run_cancelation_result", "task_cancelation_result_vec")
    class Result(_message.Message):
        __slots__ = ("uid", "error")
        UID_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        uid: _universal_id_pb2.UniversalIdProto
        error: _error_pb2.ErrorProto
        def __init__(self, uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...
    BASE_FIELD_NUMBER: _ClassVar[int]
    RUN_CANCELATION_RESULT_FIELD_NUMBER: _ClassVar[int]
    TASK_CANCELATION_RESULT_VEC_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ResultBase
    run_cancelation_result: CancelTasksResult.Result
    task_cancelation_result_vec: _containers.RepeatedCompositeFieldContainer[CancelTasksResult.Result]
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ResultBase, _Mapping]] = ..., run_cancelation_result: _Optional[_Union[CancelTasksResult.Result, _Mapping]] = ..., task_cancelation_result_vec: _Optional[_Iterable[_Union[CancelTasksResult.Result, _Mapping]]] = ...) -> None: ...

class PauseTasksArg(_message.Message):
    __slots__ = ("base", "run_uid", "task_uid_vec")
    BASE_FIELD_NUMBER: _ClassVar[int]
    RUN_UID_FIELD_NUMBER: _ClassVar[int]
    TASK_UID_VEC_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ArgumentBase
    run_uid: _universal_id_pb2.UniversalIdProto
    task_uid_vec: _containers.RepeatedCompositeFieldContainer[_universal_id_pb2.UniversalIdProto]
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ArgumentBase, _Mapping]] = ..., run_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., task_uid_vec: _Optional[_Iterable[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]]] = ...) -> None: ...

class PauseTasksResult(_message.Message):
    __slots__ = ("base", "run_pause_result", "task_pause_result_vec")
    class Result(_message.Message):
        __slots__ = ("task_uid", "error")
        TASK_UID_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        task_uid: _universal_id_pb2.UniversalIdProto
        error: _error_pb2.ErrorProto
        def __init__(self, task_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...
    BASE_FIELD_NUMBER: _ClassVar[int]
    RUN_PAUSE_RESULT_FIELD_NUMBER: _ClassVar[int]
    TASK_PAUSE_RESULT_VEC_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ResultBase
    run_pause_result: PauseTasksResult.Result
    task_pause_result_vec: _containers.RepeatedCompositeFieldContainer[PauseTasksResult.Result]
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ResultBase, _Mapping]] = ..., run_pause_result: _Optional[_Union[PauseTasksResult.Result, _Mapping]] = ..., task_pause_result_vec: _Optional[_Iterable[_Union[PauseTasksResult.Result, _Mapping]]] = ...) -> None: ...

class ResumeTasksArg(_message.Message):
    __slots__ = ("base", "run_uid", "task_uid_vec")
    BASE_FIELD_NUMBER: _ClassVar[int]
    RUN_UID_FIELD_NUMBER: _ClassVar[int]
    TASK_UID_VEC_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ArgumentBase
    run_uid: _universal_id_pb2.UniversalIdProto
    task_uid_vec: _containers.RepeatedCompositeFieldContainer[_universal_id_pb2.UniversalIdProto]
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ArgumentBase, _Mapping]] = ..., run_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., task_uid_vec: _Optional[_Iterable[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]]] = ...) -> None: ...

class ResumeTasksResult(_message.Message):
    __slots__ = ("base", "run_cancelation_result", "task_cancelation_result_vec")
    class Result(_message.Message):
        __slots__ = ("task_uid", "error")
        TASK_UID_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        task_uid: _universal_id_pb2.UniversalIdProto
        error: _error_pb2.ErrorProto
        def __init__(self, task_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...
    BASE_FIELD_NUMBER: _ClassVar[int]
    RUN_CANCELATION_RESULT_FIELD_NUMBER: _ClassVar[int]
    TASK_CANCELATION_RESULT_VEC_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ResultBase
    run_cancelation_result: ResumeTasksResult.Result
    task_cancelation_result_vec: _containers.RepeatedCompositeFieldContainer[ResumeTasksResult.Result]
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ResultBase, _Mapping]] = ..., run_cancelation_result: _Optional[_Union[ResumeTasksResult.Result, _Mapping]] = ..., task_cancelation_result_vec: _Optional[_Iterable[_Union[ResumeTasksResult.Result, _Mapping]]] = ...) -> None: ...
