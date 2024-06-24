from scribe.base import scribe_pb2 as _scribe_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RowMD(_message.Message):
    __slots__ = ()
    class Base(_message.Message):
        __slots__ = ("version", "sequencer", "tombstone", "is_integral_key", "timestamp_usecs", "num_columns")
        VERSION_FIELD_NUMBER: _ClassVar[int]
        SEQUENCER_FIELD_NUMBER: _ClassVar[int]
        TOMBSTONE_FIELD_NUMBER: _ClassVar[int]
        IS_INTEGRAL_KEY_FIELD_NUMBER: _ClassVar[int]
        TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
        NUM_COLUMNS_FIELD_NUMBER: _ClassVar[int]
        version: int
        sequencer: _scribe_pb2.SequencerProto
        tombstone: bool
        is_integral_key: bool
        timestamp_usecs: int
        num_columns: int
        def __init__(self, version: _Optional[int] = ..., sequencer: _Optional[_Union[_scribe_pb2.SequencerProto, _Mapping]] = ..., tombstone: bool = ..., is_integral_key: bool = ..., timestamp_usecs: _Optional[int] = ..., num_columns: _Optional[int] = ...) -> None: ...
    def __init__(self) -> None: ...
