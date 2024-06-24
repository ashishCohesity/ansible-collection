from bookkeeper.v2.base import bookkeeper_v2_pb2 as _bookkeeper_v2_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BookkeeperV2SpecialEntityProto(_message.Message):
    __slots__ = ("cluster_id", "storage_domain_id", "entity_name", "group_id", "last_updated_timestamp_usecs", "logical_stats", "physical_stats", "group_creation_timestamp_usecs")
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    STORAGE_DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    ENTITY_NAME_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATED_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
    LOGICAL_STATS_FIELD_NUMBER: _ClassVar[int]
    PHYSICAL_STATS_FIELD_NUMBER: _ClassVar[int]
    GROUP_CREATION_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
    cluster_id: int
    storage_domain_id: int
    entity_name: str
    group_id: int
    last_updated_timestamp_usecs: int
    logical_stats: _bookkeeper_v2_pb2.LogicalStats
    physical_stats: _bookkeeper_v2_pb2.PhysicalStats
    group_creation_timestamp_usecs: int
    def __init__(self, cluster_id: _Optional[int] = ..., storage_domain_id: _Optional[int] = ..., entity_name: _Optional[str] = ..., group_id: _Optional[int] = ..., last_updated_timestamp_usecs: _Optional[int] = ..., logical_stats: _Optional[_Union[_bookkeeper_v2_pb2.LogicalStats, _Mapping]] = ..., physical_stats: _Optional[_Union[_bookkeeper_v2_pb2.PhysicalStats, _Mapping]] = ..., group_creation_timestamp_usecs: _Optional[int] = ...) -> None: ...
