from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ViewSnaptreeIntentFixerLeafStateDataProto(_message.Message):
    __slots__ = ("entity_id", "snap_fs_intent", "s3_intent")
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    SNAP_FS_INTENT_FIELD_NUMBER: _ClassVar[int]
    S3_INTENT_FIELD_NUMBER: _ClassVar[int]
    entity_id: int
    snap_fs_intent: bool
    s3_intent: bool
    def __init__(self, entity_id: _Optional[int] = ..., snap_fs_intent: bool = ..., s3_intent: bool = ...) -> None: ...
