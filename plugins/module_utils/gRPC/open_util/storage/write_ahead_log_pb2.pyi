from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class WriteAheadLogRecord(_message.Message):
    __slots__ = ("logical_timestamp", "last_logical_timestamp", "saved_last_delta_logical_timestamp", "payload_size", "morphed_payload_size")
    LOGICAL_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    LAST_LOGICAL_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    SAVED_LAST_DELTA_LOGICAL_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_SIZE_FIELD_NUMBER: _ClassVar[int]
    MORPHED_PAYLOAD_SIZE_FIELD_NUMBER: _ClassVar[int]
    logical_timestamp: int
    last_logical_timestamp: int
    saved_last_delta_logical_timestamp: int
    payload_size: int
    morphed_payload_size: int
    def __init__(self, logical_timestamp: _Optional[int] = ..., last_logical_timestamp: _Optional[int] = ..., saved_last_delta_logical_timestamp: _Optional[int] = ..., payload_size: _Optional[int] = ..., morphed_payload_size: _Optional[int] = ...) -> None: ...
