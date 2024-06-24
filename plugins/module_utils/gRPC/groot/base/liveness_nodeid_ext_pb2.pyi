from gandalf.util import liveness_pb2 as _liveness_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class LivenessNodeIdExtension(_message.Message):
    __slots__ = ("node_id",)
    LIVENESS_EXT_FIELD_NUMBER: _ClassVar[int]
    liveness_ext: _descriptor.FieldDescriptor
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    node_id: int
    def __init__(self, node_id: _Optional[int] = ...) -> None: ...
