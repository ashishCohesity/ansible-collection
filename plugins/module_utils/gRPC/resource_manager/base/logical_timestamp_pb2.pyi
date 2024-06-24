from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class LogicalTimestamp(_message.Message):
    __slots__ = ("request_sequencer", "operation_id")
    REQUEST_SEQUENCER_FIELD_NUMBER: _ClassVar[int]
    OPERATION_ID_FIELD_NUMBER: _ClassVar[int]
    request_sequencer: int
    operation_id: int
    def __init__(self, request_sequencer: _Optional[int] = ..., operation_id: _Optional[int] = ...) -> None: ...
