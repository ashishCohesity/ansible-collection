from magneto.base import error_pb2 as _error_pb2
from magneto.v2.entity_manager import entity_external_pb2 as _entity_external_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EntityManagerVersionProto(_message.Message):
    __slots__ = ("version", "api_version")
    VERSION_FIELD_NUMBER: _ClassVar[int]
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    version: int
    api_version: int
    def __init__(self, version: _Optional[int] = ..., api_version: _Optional[int] = ...) -> None: ...

class SourceTaskIdProto(_message.Message):
    __slots__ = ("task_id", "source_primary_key")
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_PRIMARY_KEY_FIELD_NUMBER: _ClassVar[int]
    task_id: int
    source_primary_key: str
    def __init__(self, task_id: _Optional[int] = ..., source_primary_key: _Optional[str] = ...) -> None: ...

class EntityManagerRefreshStateProto(_message.Message):
    __slots__ = ("start_source_refresh_arg", "refresh_task_id", "refresh_status", "pagination_cookie", "last_updated_secs", "error")
    class RefreshStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kWaiting: _ClassVar[EntityManagerRefreshStateProto.RefreshStatus]
        kStarted: _ClassVar[EntityManagerRefreshStateProto.RefreshStatus]
        kRefreshedDAG: _ClassVar[EntityManagerRefreshStateProto.RefreshStatus]
        kFinished: _ClassVar[EntityManagerRefreshStateProto.RefreshStatus]
        kAborted: _ClassVar[EntityManagerRefreshStateProto.RefreshStatus]
    kWaiting: EntityManagerRefreshStateProto.RefreshStatus
    kStarted: EntityManagerRefreshStateProto.RefreshStatus
    kRefreshedDAG: EntityManagerRefreshStateProto.RefreshStatus
    kFinished: EntityManagerRefreshStateProto.RefreshStatus
    kAborted: EntityManagerRefreshStateProto.RefreshStatus
    START_SOURCE_REFRESH_ARG_FIELD_NUMBER: _ClassVar[int]
    REFRESH_TASK_ID_FIELD_NUMBER: _ClassVar[int]
    REFRESH_STATUS_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_COOKIE_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATED_SECS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    start_source_refresh_arg: _entity_external_pb2.StartSourceRefreshArg
    refresh_task_id: SourceTaskIdProto
    refresh_status: EntityManagerRefreshStateProto.RefreshStatus
    pagination_cookie: str
    last_updated_secs: int
    error: _error_pb2.ErrorProto
    def __init__(self, start_source_refresh_arg: _Optional[_Union[_entity_external_pb2.StartSourceRefreshArg, _Mapping]] = ..., refresh_task_id: _Optional[_Union[SourceTaskIdProto, _Mapping]] = ..., refresh_status: _Optional[_Union[EntityManagerRefreshStateProto.RefreshStatus, str]] = ..., pagination_cookie: _Optional[str] = ..., last_updated_secs: _Optional[int] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class EntityManagerUnregisterStateProto(_message.Message):
    __slots__ = ("unregister_arg", "unregister_status", "last_updated_secs", "error")
    class UnregistrationStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNotSet: _ClassVar[EntityManagerUnregisterStateProto.UnregistrationStatus]
        kPending: _ClassVar[EntityManagerUnregisterStateProto.UnregistrationStatus]
        kDetaching: _ClassVar[EntityManagerUnregisterStateProto.UnregistrationStatus]
        kFinished: _ClassVar[EntityManagerUnregisterStateProto.UnregistrationStatus]
    kNotSet: EntityManagerUnregisterStateProto.UnregistrationStatus
    kPending: EntityManagerUnregisterStateProto.UnregistrationStatus
    kDetaching: EntityManagerUnregisterStateProto.UnregistrationStatus
    kFinished: EntityManagerUnregisterStateProto.UnregistrationStatus
    UNREGISTER_ARG_FIELD_NUMBER: _ClassVar[int]
    UNREGISTER_STATUS_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATED_SECS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    unregister_arg: _entity_external_pb2.UnregisterSourceArg
    unregister_status: EntityManagerUnregisterStateProto.UnregistrationStatus
    last_updated_secs: int
    error: _error_pb2.ErrorProto
    def __init__(self, unregister_arg: _Optional[_Union[_entity_external_pb2.UnregisterSourceArg, _Mapping]] = ..., unregister_status: _Optional[_Union[EntityManagerUnregisterStateProto.UnregistrationStatus, str]] = ..., last_updated_secs: _Optional[int] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class WALRecordProto(_message.Message):
    __slots__ = ("entity_manager_version", "refresh_state_vec", "unregister_state_vec")
    ENTITY_MANAGER_VERSION_FIELD_NUMBER: _ClassVar[int]
    REFRESH_STATE_VEC_FIELD_NUMBER: _ClassVar[int]
    UNREGISTER_STATE_VEC_FIELD_NUMBER: _ClassVar[int]
    entity_manager_version: EntityManagerVersionProto
    refresh_state_vec: _containers.RepeatedCompositeFieldContainer[EntityManagerRefreshStateProto]
    unregister_state_vec: _containers.RepeatedCompositeFieldContainer[EntityManagerUnregisterStateProto]
    def __init__(self, entity_manager_version: _Optional[_Union[EntityManagerVersionProto, _Mapping]] = ..., refresh_state_vec: _Optional[_Iterable[_Union[EntityManagerRefreshStateProto, _Mapping]]] = ..., unregister_state_vec: _Optional[_Iterable[_Union[EntityManagerUnregisterStateProto, _Mapping]]] = ...) -> None: ...
