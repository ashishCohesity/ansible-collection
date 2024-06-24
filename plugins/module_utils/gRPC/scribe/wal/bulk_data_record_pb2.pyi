from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class BulkDataRecord(_message.Message):
    __slots__ = ("records", "has_more_segments")
    RECORDS_FIELD_NUMBER: _ClassVar[int]
    HAS_MORE_SEGMENTS_FIELD_NUMBER: _ClassVar[int]
    records: _containers.RepeatedScalarFieldContainer[bytes]
    has_more_segments: bool
    def __init__(self, records: _Optional[_Iterable[bytes]] = ..., has_more_segments: bool = ...) -> None: ...
