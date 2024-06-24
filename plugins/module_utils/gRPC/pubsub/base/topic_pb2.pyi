from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class TopicProto(_message.Message):
    __slots__ = ("name", "num_shards", "consumer_group_ids", "ttl_usecs")
    NAME_FIELD_NUMBER: _ClassVar[int]
    NUM_SHARDS_FIELD_NUMBER: _ClassVar[int]
    CONSUMER_GROUP_IDS_FIELD_NUMBER: _ClassVar[int]
    TTL_USECS_FIELD_NUMBER: _ClassVar[int]
    name: str
    num_shards: int
    consumer_group_ids: _containers.RepeatedScalarFieldContainer[int]
    ttl_usecs: int
    def __init__(self, name: _Optional[str] = ..., num_shards: _Optional[int] = ..., consumer_group_ids: _Optional[_Iterable[int]] = ..., ttl_usecs: _Optional[int] = ...) -> None: ...
