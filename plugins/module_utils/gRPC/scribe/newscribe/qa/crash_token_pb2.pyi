from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CrashTokenProto(_message.Message):
    __slots__ = ("node_id", "node_incarnation_id", "view_config_version")
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    NODE_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_CONFIG_VERSION_FIELD_NUMBER: _ClassVar[int]
    node_id: int
    node_incarnation_id: int
    view_config_version: int
    def __init__(self, node_id: _Optional[int] = ..., node_incarnation_id: _Optional[int] = ..., view_config_version: _Optional[int] = ...) -> None: ...
