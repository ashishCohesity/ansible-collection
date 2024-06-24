from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ShardingStateProto(_message.Message):
    __slots__ = ("stats_sharding_state_key", "ordered_live_stats_shards")
    class Constituent(_message.Message):
        __slots__ = ("constituent_id", "node_id", "endpoint_str")
        CONSTITUENT_ID_FIELD_NUMBER: _ClassVar[int]
        NODE_ID_FIELD_NUMBER: _ClassVar[int]
        ENDPOINT_STR_FIELD_NUMBER: _ClassVar[int]
        constituent_id: int
        node_id: int
        endpoint_str: str
        def __init__(self, constituent_id: _Optional[int] = ..., node_id: _Optional[int] = ..., endpoint_str: _Optional[str] = ...) -> None: ...
    STATS_SHARDING_STATE_KEY_FIELD_NUMBER: _ClassVar[int]
    ORDERED_LIVE_STATS_SHARDS_FIELD_NUMBER: _ClassVar[int]
    stats_sharding_state_key: str
    ordered_live_stats_shards: _containers.RepeatedCompositeFieldContainer[ShardingStateProto.Constituent]
    def __init__(self, stats_sharding_state_key: _Optional[str] = ..., ordered_live_stats_shards: _Optional[_Iterable[_Union[ShardingStateProto.Constituent, _Mapping]]] = ...) -> None: ...
