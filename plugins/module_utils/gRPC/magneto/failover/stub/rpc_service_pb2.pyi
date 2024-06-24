from magneto.api import magneto_external_base_pb2 as _magneto_external_base_pb2
from magneto.base import error_pb2 as _error_pb2
from magneto.failover import failover_state_pb2 as _failover_state_pb2
from open_util.net import protorpc_pb2 as _protorpc_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FetchFailoverCommandArg(_message.Message):
    __slots__ = ("tx_cluster_id", "tx_cluster_incarnation_id", "expected_rx_cluster_id", "expected_rx_cluster_incarnation_id", "is_forwarded", "failover_replication_stats_vec")
    class FailoverReplicationStats(_message.Message):
        __slots__ = ("failover_uid", "replication_stats_vec")
        FAILOVER_UID_FIELD_NUMBER: _ClassVar[int]
        REPLICATION_STATS_VEC_FIELD_NUMBER: _ClassVar[int]
        failover_uid: str
        replication_stats_vec: _containers.RepeatedCompositeFieldContainer[_magneto_external_base_pb2.ReplicationInfoProto]
        def __init__(self, failover_uid: _Optional[str] = ..., replication_stats_vec: _Optional[_Iterable[_Union[_magneto_external_base_pb2.ReplicationInfoProto, _Mapping]]] = ...) -> None: ...
    TX_CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    TX_CLUSTER_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_RX_CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_RX_CLUSTER_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    IS_FORWARDED_FIELD_NUMBER: _ClassVar[int]
    FAILOVER_REPLICATION_STATS_VEC_FIELD_NUMBER: _ClassVar[int]
    tx_cluster_id: int
    tx_cluster_incarnation_id: int
    expected_rx_cluster_id: int
    expected_rx_cluster_incarnation_id: int
    is_forwarded: bool
    failover_replication_stats_vec: _containers.RepeatedCompositeFieldContainer[FetchFailoverCommandArg.FailoverReplicationStats]
    def __init__(self, tx_cluster_id: _Optional[int] = ..., tx_cluster_incarnation_id: _Optional[int] = ..., expected_rx_cluster_id: _Optional[int] = ..., expected_rx_cluster_incarnation_id: _Optional[int] = ..., is_forwarded: bool = ..., failover_replication_stats_vec: _Optional[_Iterable[_Union[FetchFailoverCommandArg.FailoverReplicationStats, _Mapping]]] = ...) -> None: ...

class FetchFailoverCommandResult(_message.Message):
    __slots__ = ("error", "failover_command_arg_vec")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    FAILOVER_COMMAND_ARG_VEC_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    failover_command_arg_vec: _containers.RepeatedCompositeFieldContainer[_failover_state_pb2.FailoverCommandArg]
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., failover_command_arg_vec: _Optional[_Iterable[_Union[_failover_state_pb2.FailoverCommandArg, _Mapping]]] = ...) -> None: ...

class DeliverFailoverCommandResponseArg(_message.Message):
    __slots__ = ("tx_cluster_id", "tx_cluster_incarnation_id", "expected_rx_cluster_id", "expected_rx_cluster_incarnation_id", "failover_command_result_vec", "is_forwarded")
    class Result(_message.Message):
        __slots__ = ("failover_command_arg", "failover_command_result")
        FAILOVER_COMMAND_ARG_FIELD_NUMBER: _ClassVar[int]
        FAILOVER_COMMAND_RESULT_FIELD_NUMBER: _ClassVar[int]
        failover_command_arg: _failover_state_pb2.FailoverCommandArg
        failover_command_result: _failover_state_pb2.FailoverCommandResult
        def __init__(self, failover_command_arg: _Optional[_Union[_failover_state_pb2.FailoverCommandArg, _Mapping]] = ..., failover_command_result: _Optional[_Union[_failover_state_pb2.FailoverCommandResult, _Mapping]] = ...) -> None: ...
    TX_CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    TX_CLUSTER_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_RX_CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_RX_CLUSTER_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    FAILOVER_COMMAND_RESULT_VEC_FIELD_NUMBER: _ClassVar[int]
    IS_FORWARDED_FIELD_NUMBER: _ClassVar[int]
    tx_cluster_id: int
    tx_cluster_incarnation_id: int
    expected_rx_cluster_id: int
    expected_rx_cluster_incarnation_id: int
    failover_command_result_vec: _containers.RepeatedCompositeFieldContainer[DeliverFailoverCommandResponseArg.Result]
    is_forwarded: bool
    def __init__(self, tx_cluster_id: _Optional[int] = ..., tx_cluster_incarnation_id: _Optional[int] = ..., expected_rx_cluster_id: _Optional[int] = ..., expected_rx_cluster_incarnation_id: _Optional[int] = ..., failover_command_result_vec: _Optional[_Iterable[_Union[DeliverFailoverCommandResponseArg.Result, _Mapping]]] = ..., is_forwarded: bool = ...) -> None: ...

class DeliverFailoverCommandResponseResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...
