from apollo.mr.base import histogram_proto_pb2 as _histogram_proto_pb2
from apollo.mr.base import pipeline_pb2 as _pipeline_pb2
from apollo.mr.base import shard_pb2 as _shard_pb2
from open_util.net import protorpc_pb2 as _protorpc_pb2
from util.base import op_clock_pb2 as _op_clock_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RpcVerifierProto(_message.Message):
    __slots__ = ("rx_session_id", "tx_session_id", "master_version", "sender_version")
    RX_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    TX_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    MASTER_VERSION_FIELD_NUMBER: _ClassVar[int]
    SENDER_VERSION_FIELD_NUMBER: _ClassVar[int]
    rx_session_id: int
    tx_session_id: int
    master_version: int
    sender_version: str
    def __init__(self, rx_session_id: _Optional[int] = ..., tx_session_id: _Optional[int] = ..., master_version: _Optional[int] = ..., sender_version: _Optional[str] = ...) -> None: ...

class QueryHardwareConfigArg(_message.Message):
    __slots__ = ("verifier",)
    VERIFIER_FIELD_NUMBER: _ClassVar[int]
    verifier: RpcVerifierProto
    def __init__(self, verifier: _Optional[_Union[RpcVerifierProto, _Mapping]] = ...) -> None: ...

class QueryHardwareConfigResult(_message.Message):
    __slots__ = ("hardware_cfg",)
    HARDWARE_CFG_FIELD_NUMBER: _ClassVar[int]
    hardware_cfg: _shard_pb2.SlaveProto.HardwareConfig
    def __init__(self, hardware_cfg: _Optional[_Union[_shard_pb2.SlaveProto.HardwareConfig, _Mapping]] = ...) -> None: ...

class UpdateResourceUsageArg(_message.Message):
    __slots__ = ("verifier", "num_slave_cpu_threads", "num_slave_disk_threads")
    VERIFIER_FIELD_NUMBER: _ClassVar[int]
    NUM_SLAVE_CPU_THREADS_FIELD_NUMBER: _ClassVar[int]
    NUM_SLAVE_DISK_THREADS_FIELD_NUMBER: _ClassVar[int]
    verifier: RpcVerifierProto
    num_slave_cpu_threads: int
    num_slave_disk_threads: int
    def __init__(self, verifier: _Optional[_Union[RpcVerifierProto, _Mapping]] = ..., num_slave_cpu_threads: _Optional[int] = ..., num_slave_disk_threads: _Optional[int] = ...) -> None: ...

class UpdateResourceUsageResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class QuerySlaveStateArg(_message.Message):
    __slots__ = ("verifier", "shard_id_vec", "backlog_indicator_vec")
    VERIFIER_FIELD_NUMBER: _ClassVar[int]
    SHARD_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    BACKLOG_INDICATOR_VEC_FIELD_NUMBER: _ClassVar[int]
    verifier: RpcVerifierProto
    shard_id_vec: _containers.RepeatedCompositeFieldContainer[_pipeline_pb2.IdProto]
    backlog_indicator_vec: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, verifier: _Optional[_Union[RpcVerifierProto, _Mapping]] = ..., shard_id_vec: _Optional[_Iterable[_Union[_pipeline_pb2.IdProto, _Mapping]]] = ..., backlog_indicator_vec: _Optional[_Iterable[int]] = ...) -> None: ...

class QuerySlaveStateResult(_message.Message):
    __slots__ = ("shard_id_vec", "run_state_vec", "constituent_start_usecs")
    SHARD_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    RUN_STATE_VEC_FIELD_NUMBER: _ClassVar[int]
    CONSTITUENT_START_USECS_FIELD_NUMBER: _ClassVar[int]
    shard_id_vec: _containers.RepeatedCompositeFieldContainer[_pipeline_pb2.IdProto]
    run_state_vec: _containers.RepeatedCompositeFieldContainer[_shard_pb2.ShardProto.RunState]
    constituent_start_usecs: int
    def __init__(self, shard_id_vec: _Optional[_Iterable[_Union[_pipeline_pb2.IdProto, _Mapping]]] = ..., run_state_vec: _Optional[_Iterable[_Union[_shard_pb2.ShardProto.RunState, _Mapping]]] = ..., constituent_start_usecs: _Optional[int] = ...) -> None: ...

class StartShardArg(_message.Message):
    __slots__ = ("verifier", "shard_id", "num_shards", "num_output_shards_vec", "resource_cfg", "scribe_scan_info", "record_source", "job_opclock_vec", "job_start_time_usecs", "job_num_nodes", "job_debug_mode", "checkpoint", "payload_size", "backlog_indicator")
    VERIFIER_FIELD_NUMBER: _ClassVar[int]
    SHARD_ID_FIELD_NUMBER: _ClassVar[int]
    NUM_SHARDS_FIELD_NUMBER: _ClassVar[int]
    NUM_OUTPUT_SHARDS_VEC_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_CFG_FIELD_NUMBER: _ClassVar[int]
    SCRIBE_SCAN_INFO_FIELD_NUMBER: _ClassVar[int]
    RECORD_SOURCE_FIELD_NUMBER: _ClassVar[int]
    JOB_OPCLOCK_VEC_FIELD_NUMBER: _ClassVar[int]
    JOB_START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    JOB_NUM_NODES_FIELD_NUMBER: _ClassVar[int]
    JOB_DEBUG_MODE_FIELD_NUMBER: _ClassVar[int]
    CHECKPOINT_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_SIZE_FIELD_NUMBER: _ClassVar[int]
    BACKLOG_INDICATOR_FIELD_NUMBER: _ClassVar[int]
    verifier: RpcVerifierProto
    shard_id: _pipeline_pb2.IdProto
    num_shards: int
    num_output_shards_vec: _containers.RepeatedScalarFieldContainer[int]
    resource_cfg: _shard_pb2.ShardProto.ResourceConfig
    scribe_scan_info: _pipeline_pb2.ScribeScanInfoProto
    record_source: _pipeline_pb2.RecordSourceProto
    job_opclock_vec: _containers.RepeatedCompositeFieldContainer[_op_clock_pb2.OpClock]
    job_start_time_usecs: int
    job_num_nodes: int
    job_debug_mode: bool
    checkpoint: _shard_pb2.ShardCheckpointProto
    payload_size: int
    backlog_indicator: int
    def __init__(self, verifier: _Optional[_Union[RpcVerifierProto, _Mapping]] = ..., shard_id: _Optional[_Union[_pipeline_pb2.IdProto, _Mapping]] = ..., num_shards: _Optional[int] = ..., num_output_shards_vec: _Optional[_Iterable[int]] = ..., resource_cfg: _Optional[_Union[_shard_pb2.ShardProto.ResourceConfig, _Mapping]] = ..., scribe_scan_info: _Optional[_Union[_pipeline_pb2.ScribeScanInfoProto, _Mapping]] = ..., record_source: _Optional[_Union[_pipeline_pb2.RecordSourceProto, _Mapping]] = ..., job_opclock_vec: _Optional[_Iterable[_Union[_op_clock_pb2.OpClock, _Mapping]]] = ..., job_start_time_usecs: _Optional[int] = ..., job_num_nodes: _Optional[int] = ..., job_debug_mode: bool = ..., checkpoint: _Optional[_Union[_shard_pb2.ShardCheckpointProto, _Mapping]] = ..., payload_size: _Optional[int] = ..., backlog_indicator: _Optional[int] = ...) -> None: ...

class StartShardResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GarbageCollectArg(_message.Message):
    __slots__ = ("verifier", "excluded_shard_vec", "excluded_shard_vec_DEPRECATED")
    class Shard(_message.Message):
        __slots__ = ("id", "incarnation_id")
        ID_FIELD_NUMBER: _ClassVar[int]
        INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
        id: _pipeline_pb2.IdProto
        incarnation_id: int
        def __init__(self, id: _Optional[_Union[_pipeline_pb2.IdProto, _Mapping]] = ..., incarnation_id: _Optional[int] = ...) -> None: ...
    VERIFIER_FIELD_NUMBER: _ClassVar[int]
    EXCLUDED_SHARD_VEC_FIELD_NUMBER: _ClassVar[int]
    EXCLUDED_SHARD_VEC_DEPRECATED_FIELD_NUMBER: _ClassVar[int]
    verifier: RpcVerifierProto
    excluded_shard_vec: _containers.RepeatedCompositeFieldContainer[GarbageCollectArg.Shard]
    excluded_shard_vec_DEPRECATED: _containers.RepeatedCompositeFieldContainer[_pipeline_pb2.IdProto]
    def __init__(self, verifier: _Optional[_Union[RpcVerifierProto, _Mapping]] = ..., excluded_shard_vec: _Optional[_Iterable[_Union[GarbageCollectArg.Shard, _Mapping]]] = ..., excluded_shard_vec_DEPRECATED: _Optional[_Iterable[_Union[_pipeline_pb2.IdProto, _Mapping]]] = ...) -> None: ...

class GarbageCollectResult(_message.Message):
    __slots__ = ("deleted_shard_vec",)
    DELETED_SHARD_VEC_FIELD_NUMBER: _ClassVar[int]
    deleted_shard_vec: _containers.RepeatedCompositeFieldContainer[_pipeline_pb2.IdProto]
    def __init__(self, deleted_shard_vec: _Optional[_Iterable[_Union[_pipeline_pb2.IdProto, _Mapping]]] = ...) -> None: ...

class FetchDataArg(_message.Message):
    __slots__ = ("verifier", "shard_id", "file_desc", "max_payload_size_bytes")
    VERIFIER_FIELD_NUMBER: _ClassVar[int]
    SHARD_ID_FIELD_NUMBER: _ClassVar[int]
    FILE_DESC_FIELD_NUMBER: _ClassVar[int]
    MAX_PAYLOAD_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    verifier: RpcVerifierProto
    shard_id: _pipeline_pb2.IdProto
    file_desc: _pipeline_pb2.FileDescriptorProto
    max_payload_size_bytes: int
    def __init__(self, verifier: _Optional[_Union[RpcVerifierProto, _Mapping]] = ..., shard_id: _Optional[_Union[_pipeline_pb2.IdProto, _Mapping]] = ..., file_desc: _Optional[_Union[_pipeline_pb2.FileDescriptorProto, _Mapping]] = ..., max_payload_size_bytes: _Optional[int] = ...) -> None: ...

class FetchDataResult(_message.Message):
    __slots__ = ("record_offsets_vec", "end_offset")
    RECORD_OFFSETS_VEC_FIELD_NUMBER: _ClassVar[int]
    END_OFFSET_FIELD_NUMBER: _ClassVar[int]
    record_offsets_vec: _containers.RepeatedScalarFieldContainer[int]
    end_offset: int
    def __init__(self, record_offsets_vec: _Optional[_Iterable[int]] = ..., end_offset: _Optional[int] = ...) -> None: ...

class NotifySlaveEventArg(_message.Message):
    __slots__ = ("verifier", "slave_node_id")
    VERIFIER_FIELD_NUMBER: _ClassVar[int]
    SLAVE_NODE_ID_FIELD_NUMBER: _ClassVar[int]
    verifier: RpcVerifierProto
    slave_node_id: int
    def __init__(self, verifier: _Optional[_Union[RpcVerifierProto, _Mapping]] = ..., slave_node_id: _Optional[int] = ...) -> None: ...

class NotifySlaveEventResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SendStatsArg(_message.Message):
    __slots__ = ("verifier", "histogram_vec")
    class Histogram(_message.Message):
        __slots__ = ("entity_name", "name", "histogram_info")
        ENTITY_NAME_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        HISTOGRAM_INFO_FIELD_NUMBER: _ClassVar[int]
        entity_name: str
        name: str
        histogram_info: _histogram_proto_pb2.HistogramProto
        def __init__(self, entity_name: _Optional[str] = ..., name: _Optional[str] = ..., histogram_info: _Optional[_Union[_histogram_proto_pb2.HistogramProto, _Mapping]] = ...) -> None: ...
    VERIFIER_FIELD_NUMBER: _ClassVar[int]
    HISTOGRAM_VEC_FIELD_NUMBER: _ClassVar[int]
    verifier: RpcVerifierProto
    histogram_vec: _containers.RepeatedCompositeFieldContainer[SendStatsArg.Histogram]
    def __init__(self, verifier: _Optional[_Union[RpcVerifierProto, _Mapping]] = ..., histogram_vec: _Optional[_Iterable[_Union[SendStatsArg.Histogram, _Mapping]]] = ...) -> None: ...

class SendStatsResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
