from magneto.api import worm_pb2 as _worm_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RetentionPolicyProto(_message.Message):
    __slots__ = ("num_days_to_keep", "worm_retention", "num_secs_to_keep")
    NUM_DAYS_TO_KEEP_FIELD_NUMBER: _ClassVar[int]
    WORM_RETENTION_FIELD_NUMBER: _ClassVar[int]
    NUM_SECS_TO_KEEP_FIELD_NUMBER: _ClassVar[int]
    num_days_to_keep: int
    worm_retention: _worm_pb2.WormRetentionProto
    num_secs_to_keep: int
    def __init__(self, num_days_to_keep: _Optional[int] = ..., worm_retention: _Optional[_Union[_worm_pb2.WormRetentionProto, _Mapping]] = ..., num_secs_to_keep: _Optional[int] = ...) -> None: ...
