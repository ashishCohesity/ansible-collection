from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class MRDataGCStatusProto(_message.Message):
    __slots__ = ("incarnation", "slave_node_id", "software_version")
    INCARNATION_FIELD_NUMBER: _ClassVar[int]
    SLAVE_NODE_ID_FIELD_NUMBER: _ClassVar[int]
    SOFTWARE_VERSION_FIELD_NUMBER: _ClassVar[int]
    incarnation: int
    slave_node_id: int
    software_version: str
    def __init__(self, incarnation: _Optional[int] = ..., slave_node_id: _Optional[int] = ..., software_version: _Optional[str] = ...) -> None: ...
