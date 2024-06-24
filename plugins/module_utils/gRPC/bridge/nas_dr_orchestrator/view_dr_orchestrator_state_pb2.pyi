from bridge.base import error_pb2 as _error_pb2
from bridge.nas_dr_orchestrator import nas_external_pb2 as _nas_external_pb2
from util.base import universal_id_pb2 as _universal_id_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FailoverInfo(_message.Message):
    __slots__ = ("failover_id", "failover_op", "start_time_usecs", "completion_time_usecs", "error")
    FAILOVER_ID_FIELD_NUMBER: _ClassVar[int]
    FAILOVER_OP_FIELD_NUMBER: _ClassVar[int]
    START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    COMPLETION_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    failover_id: _universal_id_pb2.UniversalIdProto
    failover_op: _nas_external_pb2.FailoverOperation
    start_time_usecs: int
    completion_time_usecs: int
    error: _error_pb2.ErrorProto
    def __init__(self, failover_id: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., failover_op: _Optional[_Union[_nas_external_pb2.FailoverOperation, str]] = ..., start_time_usecs: _Optional[int] = ..., completion_time_usecs: _Optional[int] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class ViewDROrchestratorStateProto(_message.Message):
    __slots__ = ("update_intent", "operational_state", "completed_failover_info_vec")
    class UpdateIntent(_message.Message):
        __slots__ = ("failover_id", "planned_failover_params", "unplanned_failover_params", "cancel_params")
        class PlannedFailoverParams(_message.Message):
            __slots__ = ("is_finalized", "set_up_reverse_replication")
            IS_FINALIZED_FIELD_NUMBER: _ClassVar[int]
            SET_UP_REVERSE_REPLICATION_FIELD_NUMBER: _ClassVar[int]
            is_finalized: bool
            set_up_reverse_replication: bool
            def __init__(self, is_finalized: bool = ..., set_up_reverse_replication: bool = ...) -> None: ...
        class UnplannedFailoverParams(_message.Message):
            __slots__ = ("set_up_reverse_replication",)
            SET_UP_REVERSE_REPLICATION_FIELD_NUMBER: _ClassVar[int]
            set_up_reverse_replication: bool
            def __init__(self, set_up_reverse_replication: bool = ...) -> None: ...
        class CancelParams(_message.Message):
            __slots__ = ("failover",)
            FAILOVER_FIELD_NUMBER: _ClassVar[int]
            failover: ViewDROrchestratorStateProto.UpdateIntent.PlannedFailoverParams
            def __init__(self, failover: _Optional[_Union[ViewDROrchestratorStateProto.UpdateIntent.PlannedFailoverParams, _Mapping]] = ...) -> None: ...
        FAILOVER_ID_FIELD_NUMBER: _ClassVar[int]
        PLANNED_FAILOVER_PARAMS_FIELD_NUMBER: _ClassVar[int]
        UNPLANNED_FAILOVER_PARAMS_FIELD_NUMBER: _ClassVar[int]
        CANCEL_PARAMS_FIELD_NUMBER: _ClassVar[int]
        failover_id: _universal_id_pb2.UniversalIdProto
        planned_failover_params: ViewDROrchestratorStateProto.UpdateIntent.PlannedFailoverParams
        unplanned_failover_params: ViewDROrchestratorStateProto.UpdateIntent.UnplannedFailoverParams
        cancel_params: ViewDROrchestratorStateProto.UpdateIntent.CancelParams
        def __init__(self, failover_id: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., planned_failover_params: _Optional[_Union[ViewDROrchestratorStateProto.UpdateIntent.PlannedFailoverParams, _Mapping]] = ..., unplanned_failover_params: _Optional[_Union[ViewDROrchestratorStateProto.UpdateIntent.UnplannedFailoverParams, _Mapping]] = ..., cancel_params: _Optional[_Union[ViewDROrchestratorStateProto.UpdateIntent.CancelParams, _Mapping]] = ...) -> None: ...
    class OngoingFailoverOperationalState(_message.Message):
        __slots__ = ("tx_cancellation_issued", "failover_info", "is_final_sync_replication", "is_final_sync_replication_complete")
        TX_CANCELLATION_ISSUED_FIELD_NUMBER: _ClassVar[int]
        FAILOVER_INFO_FIELD_NUMBER: _ClassVar[int]
        IS_FINAL_SYNC_REPLICATION_FIELD_NUMBER: _ClassVar[int]
        IS_FINAL_SYNC_REPLICATION_COMPLETE_FIELD_NUMBER: _ClassVar[int]
        tx_cancellation_issued: bool
        failover_info: FailoverInfo
        is_final_sync_replication: bool
        is_final_sync_replication_complete: bool
        def __init__(self, tx_cancellation_issued: bool = ..., failover_info: _Optional[_Union[FailoverInfo, _Mapping]] = ..., is_final_sync_replication: bool = ..., is_final_sync_replication_complete: bool = ...) -> None: ...
    UPDATE_INTENT_FIELD_NUMBER: _ClassVar[int]
    OPERATIONAL_STATE_FIELD_NUMBER: _ClassVar[int]
    COMPLETED_FAILOVER_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    update_intent: ViewDROrchestratorStateProto.UpdateIntent
    operational_state: ViewDROrchestratorStateProto.OngoingFailoverOperationalState
    completed_failover_info_vec: _containers.RepeatedCompositeFieldContainer[FailoverInfo]
    def __init__(self, update_intent: _Optional[_Union[ViewDROrchestratorStateProto.UpdateIntent, _Mapping]] = ..., operational_state: _Optional[_Union[ViewDROrchestratorStateProto.OngoingFailoverOperationalState, _Mapping]] = ..., completed_failover_info_vec: _Optional[_Iterable[_Union[FailoverInfo, _Mapping]]] = ...) -> None: ...
