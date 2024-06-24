from apollo.mr.base import error_pb2 as _error_pb2
from apollo.mr.base import action_pb2 as _action_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class IdProto(_message.Message):
    __slots__ = ("pipeline", "instance_id", "fragment_id", "shard_id", "fragment_name", "output_type", "output_id", "uuid")
    class OutputType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNone: _ClassVar[IdProto.OutputType]
        kRecord: _ClassVar[IdProto.OutputType]
        kAction: _ClassVar[IdProto.OutputType]
    kNone: IdProto.OutputType
    kRecord: IdProto.OutputType
    kAction: IdProto.OutputType
    PIPELINE_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    FRAGMENT_ID_FIELD_NUMBER: _ClassVar[int]
    SHARD_ID_FIELD_NUMBER: _ClassVar[int]
    FRAGMENT_NAME_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_TYPE_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_ID_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    pipeline: str
    instance_id: int
    fragment_id: int
    shard_id: int
    fragment_name: str
    output_type: IdProto.OutputType
    output_id: int
    uuid: int
    def __init__(self, pipeline: _Optional[str] = ..., instance_id: _Optional[int] = ..., fragment_id: _Optional[int] = ..., shard_id: _Optional[int] = ..., fragment_name: _Optional[str] = ..., output_type: _Optional[_Union[IdProto.OutputType, str]] = ..., output_id: _Optional[int] = ..., uuid: _Optional[int] = ...) -> None: ...

class ScribeScanInfoProto(_message.Message):
    __slots__ = ("bucket_id_vec",)
    BUCKET_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    bucket_id_vec: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, bucket_id_vec: _Optional[_Iterable[int]] = ...) -> None: ...

class FileDescriptorProto(_message.Message):
    __slots__ = ("disk_id", "start_offset", "end_offset", "file_index")
    DISK_ID_FIELD_NUMBER: _ClassVar[int]
    START_OFFSET_FIELD_NUMBER: _ClassVar[int]
    END_OFFSET_FIELD_NUMBER: _ClassVar[int]
    FILE_INDEX_FIELD_NUMBER: _ClassVar[int]
    disk_id: int
    start_offset: int
    end_offset: int
    file_index: int
    def __init__(self, disk_id: _Optional[int] = ..., start_offset: _Optional[int] = ..., end_offset: _Optional[int] = ..., file_index: _Optional[int] = ...) -> None: ...

class ShardedFilesProto(_message.Message):
    __slots__ = ("file_desc_vec",)
    FILE_DESC_VEC_FIELD_NUMBER: _ClassVar[int]
    file_desc_vec: _containers.RepeatedCompositeFieldContainer[FileDescriptorProto]
    def __init__(self, file_desc_vec: _Optional[_Iterable[_Union[FileDescriptorProto, _Mapping]]] = ...) -> None: ...

class RecordSinkProto(_message.Message):
    __slots__ = ("serialized_sharded_output_vec",)
    SERIALIZED_SHARDED_OUTPUT_VEC_FIELD_NUMBER: _ClassVar[int]
    serialized_sharded_output_vec: _containers.RepeatedScalarFieldContainer[bytes]
    def __init__(self, serialized_sharded_output_vec: _Optional[_Iterable[bytes]] = ...) -> None: ...

class RecordSourceProto(_message.Message):
    __slots__ = ("input_vec",)
    class Input(_message.Message):
        __slots__ = ("node_id", "record_output_id", "sharded_input")
        NODE_ID_FIELD_NUMBER: _ClassVar[int]
        RECORD_OUTPUT_ID_FIELD_NUMBER: _ClassVar[int]
        SHARDED_INPUT_FIELD_NUMBER: _ClassVar[int]
        node_id: int
        record_output_id: IdProto
        sharded_input: ShardedFilesProto
        def __init__(self, node_id: _Optional[int] = ..., record_output_id: _Optional[_Union[IdProto, _Mapping]] = ..., sharded_input: _Optional[_Union[ShardedFilesProto, _Mapping]] = ...) -> None: ...
    INPUT_VEC_FIELD_NUMBER: _ClassVar[int]
    input_vec: _containers.RepeatedCompositeFieldContainer[RecordSourceProto.Input]
    def __init__(self, input_vec: _Optional[_Iterable[_Union[RecordSourceProto.Input, _Mapping]]] = ...) -> None: ...

class RecordSourceErrorProto(_message.Message):
    __slots__ = ("error_vec",)
    class Error(_message.Message):
        __slots__ = ("record_output_id", "error")
        RECORD_OUTPUT_ID_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        record_output_id: IdProto
        error: _error_pb2.ErrorProto
        def __init__(self, record_output_id: _Optional[_Union[IdProto, _Mapping]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...
    ERROR_VEC_FIELD_NUMBER: _ClassVar[int]
    error_vec: _containers.RepeatedCompositeFieldContainer[RecordSourceErrorProto.Error]
    def __init__(self, error_vec: _Optional[_Iterable[_Union[RecordSourceErrorProto.Error, _Mapping]]] = ...) -> None: ...

class ShardRunnerCheckpointProto(_message.Message):
    __slots__ = ("action_sink_state_vec",)
    class ActionSinkState(_message.Message):
        __slots__ = ("executed_action_count", "action_stats_vec")
        EXECUTED_ACTION_COUNT_FIELD_NUMBER: _ClassVar[int]
        ACTION_STATS_VEC_FIELD_NUMBER: _ClassVar[int]
        executed_action_count: int
        action_stats_vec: _containers.RepeatedCompositeFieldContainer[_action_pb2.ActionStats]
        def __init__(self, executed_action_count: _Optional[int] = ..., action_stats_vec: _Optional[_Iterable[_Union[_action_pb2.ActionStats, _Mapping]]] = ...) -> None: ...
    ACTION_SINK_STATE_VEC_FIELD_NUMBER: _ClassVar[int]
    action_sink_state_vec: _containers.RepeatedCompositeFieldContainer[ShardRunnerCheckpointProto.ActionSinkState]
    def __init__(self, action_sink_state_vec: _Optional[_Iterable[_Union[ShardRunnerCheckpointProto.ActionSinkState, _Mapping]]] = ...) -> None: ...

class CustomInputSourceProto(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CountersProto(_message.Message):
    __slots__ = ("counter_map",)
    class StatType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNone: _ClassVar[CountersProto.StatType]
        kSum: _ClassVar[CountersProto.StatType]
        kLatest: _ClassVar[CountersProto.StatType]
    kNone: CountersProto.StatType
    kSum: CountersProto.StatType
    kLatest: CountersProto.StatType
    class StatUnit(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kCount: _ClassVar[CountersProto.StatUnit]
        kBytes: _ClassVar[CountersProto.StatUnit]
    kCount: CountersProto.StatUnit
    kBytes: CountersProto.StatUnit
    class CounterInfo(_message.Message):
        __slots__ = ("count", "stat_type", "stat_unit")
        COUNT_FIELD_NUMBER: _ClassVar[int]
        STAT_TYPE_FIELD_NUMBER: _ClassVar[int]
        STAT_UNIT_FIELD_NUMBER: _ClassVar[int]
        count: int
        stat_type: CountersProto.StatType
        stat_unit: CountersProto.StatUnit
        def __init__(self, count: _Optional[int] = ..., stat_type: _Optional[_Union[CountersProto.StatType, str]] = ..., stat_unit: _Optional[_Union[CountersProto.StatUnit, str]] = ...) -> None: ...
    class CounterMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: CountersProto.CounterInfo
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[CountersProto.CounterInfo, _Mapping]] = ...) -> None: ...
    COUNTER_MAP_FIELD_NUMBER: _ClassVar[int]
    counter_map: _containers.MessageMap[str, CountersProto.CounterInfo]
    def __init__(self, counter_map: _Optional[_Mapping[str, CountersProto.CounterInfo]] = ...) -> None: ...

class FSStoreInput(_message.Message):
    __slots__ = ("indices",)
    INDICES_FIELD_NUMBER: _ClassVar[int]
    indices: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, indices: _Optional[_Iterable[int]] = ...) -> None: ...
