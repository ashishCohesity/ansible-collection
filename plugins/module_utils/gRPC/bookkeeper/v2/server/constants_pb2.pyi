from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ConstantsProto(_message.Message):
    __slots__ = ("bookkeeper_v2_group_id_gandalf_key",)
    BOOKKEEPER_V2_GROUP_ID_GANDALF_KEY_FIELD_NUMBER: _ClassVar[int]
    bookkeeper_v2_group_id_gandalf_key: str
    def __init__(self, bookkeeper_v2_group_id_gandalf_key: _Optional[str] = ...) -> None: ...
