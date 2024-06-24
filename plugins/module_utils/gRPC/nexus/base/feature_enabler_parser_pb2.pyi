from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class FeatureEnablerParserOutput(_message.Message):
    __slots__ = ("timestamp_msecs", "prerequisite_feature_list")
    TIMESTAMP_MSECS_FIELD_NUMBER: _ClassVar[int]
    PREREQUISITE_FEATURE_LIST_FIELD_NUMBER: _ClassVar[int]
    timestamp_msecs: int
    prerequisite_feature_list: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, timestamp_msecs: _Optional[int] = ..., prerequisite_feature_list: _Optional[_Iterable[int]] = ...) -> None: ...
