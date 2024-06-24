from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class EntityHandleProto(_message.Message):
    __slots__ = ("view_id", "root_inode_id", "entity_id")
    VIEW_ID_FIELD_NUMBER: _ClassVar[int]
    ROOT_INODE_ID_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    view_id: int
    root_inode_id: int
    entity_id: int
    def __init__(self, view_id: _Optional[int] = ..., root_inode_id: _Optional[int] = ..., entity_id: _Optional[int] = ...) -> None: ...
