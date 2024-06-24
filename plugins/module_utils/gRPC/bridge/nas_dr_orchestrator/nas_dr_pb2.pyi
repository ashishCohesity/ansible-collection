from bridge.base import error_pb2 as _error_pb2
from bridge.nas_dr_orchestrator import nas_external_pb2 as _nas_external_pb2
from bridge.nas_dr_orchestrator import view_dr_orchestrator_state_pb2 as _view_dr_orchestrator_state_pb2
from magneto.api import magneto_external_base_pb2 as _magneto_external_base_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PerformDROperationArg(_message.Message):
    __slots__ = ("view_id", "failover_op_type", "is_forwarded", "set_up_reverse_replication")
    VIEW_ID_FIELD_NUMBER: _ClassVar[int]
    FAILOVER_OP_TYPE_FIELD_NUMBER: _ClassVar[int]
    IS_FORWARDED_FIELD_NUMBER: _ClassVar[int]
    SET_UP_REVERSE_REPLICATION_FIELD_NUMBER: _ClassVar[int]
    view_id: int
    failover_op_type: _nas_external_pb2.FailoverOperation
    is_forwarded: bool
    set_up_reverse_replication: bool
    def __init__(self, view_id: _Optional[int] = ..., failover_op_type: _Optional[_Union[_nas_external_pb2.FailoverOperation, str]] = ..., is_forwarded: bool = ..., set_up_reverse_replication: bool = ...) -> None: ...

class PerformDROperationResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class GetAllowedFailoverOpsArg(_message.Message):
    __slots__ = ("view_id", "is_forwarded")
    VIEW_ID_FIELD_NUMBER: _ClassVar[int]
    IS_FORWARDED_FIELD_NUMBER: _ClassVar[int]
    view_id: int
    is_forwarded: bool
    def __init__(self, view_id: _Optional[int] = ..., is_forwarded: bool = ...) -> None: ...

class GetAllowedFailoverOpsResult(_message.Message):
    __slots__ = ("error", "allowed_failover_ops_vec")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_FAILOVER_OPS_VEC_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    allowed_failover_ops_vec: _containers.RepeatedScalarFieldContainer[_nas_external_pb2.FailoverOperation]
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., allowed_failover_ops_vec: _Optional[_Iterable[_Union[_nas_external_pb2.FailoverOperation, str]]] = ...) -> None: ...

class GetDRStatusArg(_message.Message):
    __slots__ = ("view_id", "is_forwarded")
    VIEW_ID_FIELD_NUMBER: _ClassVar[int]
    IS_FORWARDED_FIELD_NUMBER: _ClassVar[int]
    view_id: int
    is_forwarded: bool
    def __init__(self, view_id: _Optional[int] = ..., is_forwarded: bool = ...) -> None: ...

class GetDRStatusResult(_message.Message):
    __slots__ = ("error", "in_progress_failover_stats", "completed_failover_stats_vec")
    class FailoverStats(_message.Message):
        __slots__ = ("failover_info", "replication_stats")
        class ReplicationStats(_message.Message):
            __slots__ = ("is_final_sync", "repl_stats_vec")
            IS_FINAL_SYNC_FIELD_NUMBER: _ClassVar[int]
            REPL_STATS_VEC_FIELD_NUMBER: _ClassVar[int]
            is_final_sync: bool
            repl_stats_vec: _containers.RepeatedCompositeFieldContainer[_magneto_external_base_pb2.ReplicationInfoProto]
            def __init__(self, is_final_sync: bool = ..., repl_stats_vec: _Optional[_Iterable[_Union[_magneto_external_base_pb2.ReplicationInfoProto, _Mapping]]] = ...) -> None: ...
        FAILOVER_INFO_FIELD_NUMBER: _ClassVar[int]
        REPLICATION_STATS_FIELD_NUMBER: _ClassVar[int]
        failover_info: _view_dr_orchestrator_state_pb2.FailoverInfo
        replication_stats: GetDRStatusResult.FailoverStats.ReplicationStats
        def __init__(self, failover_info: _Optional[_Union[_view_dr_orchestrator_state_pb2.FailoverInfo, _Mapping]] = ..., replication_stats: _Optional[_Union[GetDRStatusResult.FailoverStats.ReplicationStats, _Mapping]] = ...) -> None: ...
    ERROR_FIELD_NUMBER: _ClassVar[int]
    IN_PROGRESS_FAILOVER_STATS_FIELD_NUMBER: _ClassVar[int]
    COMPLETED_FAILOVER_STATS_VEC_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    in_progress_failover_stats: GetDRStatusResult.FailoverStats
    completed_failover_stats_vec: _containers.RepeatedCompositeFieldContainer[GetDRStatusResult.FailoverStats]
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., in_progress_failover_stats: _Optional[_Union[GetDRStatusResult.FailoverStats, _Mapping]] = ..., completed_failover_stats_vec: _Optional[_Iterable[_Union[GetDRStatusResult.FailoverStats, _Mapping]]] = ...) -> None: ...

class LookupOrUpdateTrackingViewArg(_message.Message):
    __slots__ = ("repl_event_name", "repl_notify_cb_params", "is_forwarded")
    class ReplNotifyCbParams(_message.Message):
        __slots__ = ("entity_chain_id", "app_handler_context")
        class AppHandlerContextEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: str
            def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
        ENTITY_CHAIN_ID_FIELD_NUMBER: _ClassVar[int]
        APP_HANDLER_CONTEXT_FIELD_NUMBER: _ClassVar[int]
        entity_chain_id: str
        app_handler_context: _containers.ScalarMap[str, str]
        def __init__(self, entity_chain_id: _Optional[str] = ..., app_handler_context: _Optional[_Mapping[str, str]] = ...) -> None: ...
    REPL_EVENT_NAME_FIELD_NUMBER: _ClassVar[int]
    REPL_NOTIFY_CB_PARAMS_FIELD_NUMBER: _ClassVar[int]
    IS_FORWARDED_FIELD_NUMBER: _ClassVar[int]
    repl_event_name: _nas_external_pb2.ReplEventName
    repl_notify_cb_params: LookupOrUpdateTrackingViewArg.ReplNotifyCbParams
    is_forwarded: bool
    def __init__(self, repl_event_name: _Optional[_Union[_nas_external_pb2.ReplEventName, str]] = ..., repl_notify_cb_params: _Optional[_Union[LookupOrUpdateTrackingViewArg.ReplNotifyCbParams, _Mapping]] = ..., is_forwarded: bool = ...) -> None: ...

class LookupOrUpdateTrackingViewResult(_message.Message):
    __slots__ = ("error", "view_id")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    VIEW_ID_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    view_id: int
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., view_id: _Optional[int] = ...) -> None: ...

class GetTrackingViewIdArg(_message.Message):
    __slots__ = ("view_uid", "is_forwarded")
    VIEW_UID_FIELD_NUMBER: _ClassVar[int]
    IS_FORWARDED_FIELD_NUMBER: _ClassVar[int]
    view_uid: str
    is_forwarded: bool
    def __init__(self, view_uid: _Optional[str] = ..., is_forwarded: bool = ...) -> None: ...

class GetTrackingViewIdResult(_message.Message):
    __slots__ = ("error", "tracking_view_id")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    TRACKING_VIEW_ID_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    tracking_view_id: int
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., tracking_view_id: _Optional[int] = ...) -> None: ...
