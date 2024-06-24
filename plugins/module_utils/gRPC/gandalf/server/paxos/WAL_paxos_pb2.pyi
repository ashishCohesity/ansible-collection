from open_util.net import protorpc_pb2 as _protorpc_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class OpHeader(_message.Message):
    __slots__ = ("is_checkpoint", "record_length")
    IS_CHECKPOINT_FIELD_NUMBER: _ClassVar[int]
    RECORD_LENGTH_FIELD_NUMBER: _ClassVar[int]
    is_checkpoint: bool
    record_length: int
    def __init__(self, is_checkpoint: bool = ..., record_length: _Optional[int] = ...) -> None: ...
