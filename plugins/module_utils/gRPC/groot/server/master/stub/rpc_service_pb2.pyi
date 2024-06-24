from groot.base import error_pb2 as _error_pb2
from groot.base import groot_pb2 as _groot_pb2
from open_util.net import protorpc_pb2 as _protorpc_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetServiceInfoArg(_message.Message):
    __slots__ = ("service_id",)
    SERVICE_ID_FIELD_NUMBER: _ClassVar[int]
    service_id: int
    def __init__(self, service_id: _Optional[int] = ...) -> None: ...

class GetServiceInfoResult(_message.Message):
    __slots__ = ("error", "service_info")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    SERVICE_INFO_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    service_info: _groot_pb2.ServiceInfo
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., service_info: _Optional[_Union[_groot_pb2.ServiceInfo, _Mapping]] = ...) -> None: ...

class UpdateMigrationStatusArg(_message.Message):
    __slots__ = ("task_id", "service_id", "constituent_id", "session_id", "error")
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ID_FIELD_NUMBER: _ClassVar[int]
    CONSTITUENT_ID_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    task_id: int
    service_id: int
    constituent_id: int
    session_id: int
    error: _error_pb2.ErrorProto
    def __init__(self, task_id: _Optional[int] = ..., service_id: _Optional[int] = ..., constituent_id: _Optional[int] = ..., session_id: _Optional[int] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class UpdateMigrationStatusResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class NotifyServiceStateArg(_message.Message):
    __slots__ = ("constituent_id", "session_id", "service_update_vec")
    class ServiceState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kRunning: _ClassVar[NotifyServiceStateArg.ServiceState]
        kDown: _ClassVar[NotifyServiceStateArg.ServiceState]
    kRunning: NotifyServiceStateArg.ServiceState
    kDown: NotifyServiceStateArg.ServiceState
    class ServiceUpdate(_message.Message):
        __slots__ = ("service_id", "epoch_id", "service_state")
        SERVICE_ID_FIELD_NUMBER: _ClassVar[int]
        EPOCH_ID_FIELD_NUMBER: _ClassVar[int]
        SERVICE_STATE_FIELD_NUMBER: _ClassVar[int]
        service_id: int
        epoch_id: int
        service_state: NotifyServiceStateArg.ServiceState
        def __init__(self, service_id: _Optional[int] = ..., epoch_id: _Optional[int] = ..., service_state: _Optional[_Union[NotifyServiceStateArg.ServiceState, str]] = ...) -> None: ...
    CONSTITUENT_ID_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    SERVICE_UPDATE_VEC_FIELD_NUMBER: _ClassVar[int]
    constituent_id: int
    session_id: int
    service_update_vec: _containers.RepeatedCompositeFieldContainer[NotifyServiceStateArg.ServiceUpdate]
    def __init__(self, constituent_id: _Optional[int] = ..., session_id: _Optional[int] = ..., service_update_vec: _Optional[_Iterable[_Union[NotifyServiceStateArg.ServiceUpdate, _Mapping]]] = ...) -> None: ...

class NotifyServiceStateResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...
