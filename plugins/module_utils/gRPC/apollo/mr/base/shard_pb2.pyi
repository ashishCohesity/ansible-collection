from apollo.mr.base import error_pb2 as _error_pb2
from apollo.mr.base import pipeline_pb2 as _pipeline_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SlaveProto(_message.Message):
    __slots__ = ("node_id", "session_id", "hardware_cfg")
    class HardwareConfig(_message.Message):
        __slots__ = ("available_memory_bytes", "num_cores", "reserved_disk_id_vec", "per_slot_memory_bytes")
        AVAILABLE_MEMORY_BYTES_FIELD_NUMBER: _ClassVar[int]
        NUM_CORES_FIELD_NUMBER: _ClassVar[int]
        RESERVED_DISK_ID_VEC_FIELD_NUMBER: _ClassVar[int]
        PER_SLOT_MEMORY_BYTES_FIELD_NUMBER: _ClassVar[int]
        available_memory_bytes: int
        num_cores: int
        reserved_disk_id_vec: _containers.RepeatedScalarFieldContainer[int]
        per_slot_memory_bytes: int
        def __init__(self, available_memory_bytes: _Optional[int] = ..., num_cores: _Optional[int] = ..., reserved_disk_id_vec: _Optional[_Iterable[int]] = ..., per_slot_memory_bytes: _Optional[int] = ...) -> None: ...
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    HARDWARE_CFG_FIELD_NUMBER: _ClassVar[int]
    node_id: int
    session_id: int
    hardware_cfg: SlaveProto.HardwareConfig
    def __init__(self, node_id: _Optional[int] = ..., session_id: _Optional[int] = ..., hardware_cfg: _Optional[_Union[SlaveProto.HardwareConfig, _Mapping]] = ...) -> None: ...

class ShardCheckpointProto(_message.Message):
    __slots__ = ("incarnation_id", "serialized_checkpoint")
    INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    SERIALIZED_CHECKPOINT_FIELD_NUMBER: _ClassVar[int]
    incarnation_id: int
    serialized_checkpoint: bytes
    def __init__(self, incarnation_id: _Optional[int] = ..., serialized_checkpoint: _Optional[bytes] = ...) -> None: ...

class ShardProto(_message.Message):
    __slots__ = ("id", "state", "start_time_usecs", "slave_node_id", "resource_cfg", "run_state")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kRunning: _ClassVar[ShardProto.State]
        kFinished: _ClassVar[ShardProto.State]
    kRunning: ShardProto.State
    kFinished: ShardProto.State
    class ResourceConfig(_message.Message):
        __slots__ = ("num_memory_slots", "disk_id_vec", "num_reserved_slots")
        NUM_MEMORY_SLOTS_FIELD_NUMBER: _ClassVar[int]
        DISK_ID_VEC_FIELD_NUMBER: _ClassVar[int]
        NUM_RESERVED_SLOTS_FIELD_NUMBER: _ClassVar[int]
        num_memory_slots: int
        disk_id_vec: _containers.RepeatedScalarFieldContainer[int]
        num_reserved_slots: int
        def __init__(self, num_memory_slots: _Optional[int] = ..., disk_id_vec: _Optional[_Iterable[int]] = ..., num_reserved_slots: _Optional[int] = ...) -> None: ...
    class RunState(_message.Message):
        __slots__ = ("counters", "error", "start_time_usecs", "end_time_usecs", "record_output_id_vec", "record_output_index_vec", "record_source_error", "checkpoint")
        COUNTERS_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
        END_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
        RECORD_OUTPUT_ID_VEC_FIELD_NUMBER: _ClassVar[int]
        RECORD_OUTPUT_INDEX_VEC_FIELD_NUMBER: _ClassVar[int]
        RECORD_SOURCE_ERROR_FIELD_NUMBER: _ClassVar[int]
        CHECKPOINT_FIELD_NUMBER: _ClassVar[int]
        counters: _pipeline_pb2.CountersProto
        error: _error_pb2.ErrorProto
        start_time_usecs: int
        end_time_usecs: int
        record_output_id_vec: _containers.RepeatedCompositeFieldContainer[_pipeline_pb2.IdProto]
        record_output_index_vec: _containers.RepeatedCompositeFieldContainer[_pipeline_pb2.RecordSinkProto]
        record_source_error: _pipeline_pb2.RecordSourceErrorProto
        checkpoint: ShardCheckpointProto
        def __init__(self, counters: _Optional[_Union[_pipeline_pb2.CountersProto, _Mapping]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., start_time_usecs: _Optional[int] = ..., end_time_usecs: _Optional[int] = ..., record_output_id_vec: _Optional[_Iterable[_Union[_pipeline_pb2.IdProto, _Mapping]]] = ..., record_output_index_vec: _Optional[_Iterable[_Union[_pipeline_pb2.RecordSinkProto, _Mapping]]] = ..., record_source_error: _Optional[_Union[_pipeline_pb2.RecordSourceErrorProto, _Mapping]] = ..., checkpoint: _Optional[_Union[ShardCheckpointProto, _Mapping]] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    SLAVE_NODE_ID_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_CFG_FIELD_NUMBER: _ClassVar[int]
    RUN_STATE_FIELD_NUMBER: _ClassVar[int]
    id: _pipeline_pb2.IdProto
    state: ShardProto.State
    start_time_usecs: int
    slave_node_id: int
    resource_cfg: ShardProto.ResourceConfig
    run_state: ShardProto.RunState
    def __init__(self, id: _Optional[_Union[_pipeline_pb2.IdProto, _Mapping]] = ..., state: _Optional[_Union[ShardProto.State, str]] = ..., start_time_usecs: _Optional[int] = ..., slave_node_id: _Optional[int] = ..., resource_cfg: _Optional[_Union[ShardProto.ResourceConfig, _Mapping]] = ..., run_state: _Optional[_Union[ShardProto.RunState, _Mapping]] = ...) -> None: ...
