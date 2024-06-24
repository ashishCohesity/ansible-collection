from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UserTuningProto(_message.Message):
    __slots__ = ("mode", "state", "reason", "start_time_usecs", "end_time_usecs", "gflags_vec", "default_apollo_common_gflags", "default_apollo_chunk_gc_gflags", "default_apollo_metadata_gc_glags", "default_apollo_aggressive_node_disk_removal_gflags", "default_apollo_aggressive_tier_rebalancer_gflags", "default_apollo_aggressive_ec_gflags")
    class Mode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kApolloNoMode: _ClassVar[UserTuningProto.Mode]
        kApolloChunkGCAggressive: _ClassVar[UserTuningProto.Mode]
        kApolloMetadataGCAggressive: _ClassVar[UserTuningProto.Mode]
        kApolloNodeDiskRemovalAggressive: _ClassVar[UserTuningProto.Mode]
        kApolloTierRebalancerAggressive: _ClassVar[UserTuningProto.Mode]
        kApolloECAggressive: _ClassVar[UserTuningProto.Mode]
    kApolloNoMode: UserTuningProto.Mode
    kApolloChunkGCAggressive: UserTuningProto.Mode
    kApolloMetadataGCAggressive: UserTuningProto.Mode
    kApolloNodeDiskRemovalAggressive: UserTuningProto.Mode
    kApolloTierRebalancerAggressive: UserTuningProto.Mode
    kApolloECAggressive: UserTuningProto.Mode
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kUnSet: _ClassVar[UserTuningProto.Status]
        kSetInProgress: _ClassVar[UserTuningProto.Status]
        kSet: _ClassVar[UserTuningProto.Status]
    kUnSet: UserTuningProto.Status
    kSetInProgress: UserTuningProto.Status
    kSet: UserTuningProto.Status
    class Gflag(_message.Message):
        __slots__ = ("name", "service_name", "old_value", "old_reason", "new_value")
        NAME_FIELD_NUMBER: _ClassVar[int]
        SERVICE_NAME_FIELD_NUMBER: _ClassVar[int]
        OLD_VALUE_FIELD_NUMBER: _ClassVar[int]
        OLD_REASON_FIELD_NUMBER: _ClassVar[int]
        NEW_VALUE_FIELD_NUMBER: _ClassVar[int]
        name: str
        service_name: str
        old_value: str
        old_reason: str
        new_value: str
        def __init__(self, name: _Optional[str] = ..., service_name: _Optional[str] = ..., old_value: _Optional[str] = ..., old_reason: _Optional[str] = ..., new_value: _Optional[str] = ...) -> None: ...
    MODE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    END_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    GFLAGS_VEC_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_APOLLO_COMMON_GFLAGS_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_APOLLO_CHUNK_GC_GFLAGS_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_APOLLO_METADATA_GC_GLAGS_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_APOLLO_AGGRESSIVE_NODE_DISK_REMOVAL_GFLAGS_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_APOLLO_AGGRESSIVE_TIER_REBALANCER_GFLAGS_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_APOLLO_AGGRESSIVE_EC_GFLAGS_FIELD_NUMBER: _ClassVar[int]
    mode: UserTuningProto.Mode
    state: UserTuningProto.Status
    reason: str
    start_time_usecs: int
    end_time_usecs: int
    gflags_vec: _containers.RepeatedCompositeFieldContainer[UserTuningProto.Gflag]
    default_apollo_common_gflags: str
    default_apollo_chunk_gc_gflags: str
    default_apollo_metadata_gc_glags: str
    default_apollo_aggressive_node_disk_removal_gflags: str
    default_apollo_aggressive_tier_rebalancer_gflags: str
    default_apollo_aggressive_ec_gflags: str
    def __init__(self, mode: _Optional[_Union[UserTuningProto.Mode, str]] = ..., state: _Optional[_Union[UserTuningProto.Status, str]] = ..., reason: _Optional[str] = ..., start_time_usecs: _Optional[int] = ..., end_time_usecs: _Optional[int] = ..., gflags_vec: _Optional[_Iterable[_Union[UserTuningProto.Gflag, _Mapping]]] = ..., default_apollo_common_gflags: _Optional[str] = ..., default_apollo_chunk_gc_gflags: _Optional[str] = ..., default_apollo_metadata_gc_glags: _Optional[str] = ..., default_apollo_aggressive_node_disk_removal_gflags: _Optional[str] = ..., default_apollo_aggressive_tier_rebalancer_gflags: _Optional[str] = ..., default_apollo_aggressive_ec_gflags: _Optional[str] = ...) -> None: ...
