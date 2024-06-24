from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ServerConstantsProto(_message.Message):
    __slots__ = ("gandalf_counter_key",)
    GANDALF_COUNTER_KEY_FIELD_NUMBER: _ClassVar[int]
    gandalf_counter_key: str
    def __init__(self, gandalf_counter_key: _Optional[str] = ...) -> None: ...
