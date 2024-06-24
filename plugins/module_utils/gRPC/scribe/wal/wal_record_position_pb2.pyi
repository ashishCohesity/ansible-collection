from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class WALScribeRecordPosition(_message.Message):
    __slots__ = ("episode_id", "is_checkpoint", "entity_id", "finalized_checkpoint_episode_id")
    EPISODE_ID_FIELD_NUMBER: _ClassVar[int]
    IS_CHECKPOINT_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    FINALIZED_CHECKPOINT_EPISODE_ID_FIELD_NUMBER: _ClassVar[int]
    episode_id: int
    is_checkpoint: bool
    entity_id: int
    finalized_checkpoint_episode_id: int
    def __init__(self, episode_id: _Optional[int] = ..., is_checkpoint: bool = ..., entity_id: _Optional[int] = ..., finalized_checkpoint_episode_id: _Optional[int] = ...) -> None: ...
