from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StatsCollectionInfo(_message.Message):
    __slots__ = ("start_collection_usecs", "end_collection_usecs", "slider_length", "slider_length_minutes")
    START_COLLECTION_USECS_FIELD_NUMBER: _ClassVar[int]
    END_COLLECTION_USECS_FIELD_NUMBER: _ClassVar[int]
    SLIDER_LENGTH_FIELD_NUMBER: _ClassVar[int]
    SLIDER_LENGTH_MINUTES_FIELD_NUMBER: _ClassVar[int]
    start_collection_usecs: int
    end_collection_usecs: int
    slider_length: int
    slider_length_minutes: int
    def __init__(self, start_collection_usecs: _Optional[int] = ..., end_collection_usecs: _Optional[int] = ..., slider_length: _Optional[int] = ..., slider_length_minutes: _Optional[int] = ...) -> None: ...

class StatsBatchObject(_message.Message):
    __slots__ = ("stats_data", "stats_collection_state")
    STATS_DATA_FIELD_NUMBER: _ClassVar[int]
    STATS_COLLECTION_STATE_FIELD_NUMBER: _ClassVar[int]
    stats_data: bytes
    stats_collection_state: StatsCollectionInfo
    def __init__(self, stats_data: _Optional[bytes] = ..., stats_collection_state: _Optional[_Union[StatsCollectionInfo, _Mapping]] = ...) -> None: ...
