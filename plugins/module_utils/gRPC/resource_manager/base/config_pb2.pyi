from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ResourceManagerConfigProto(_message.Message):
    __slots__ = ("request_sequencer_gandalf_key_prefix",)
    REQUEST_SEQUENCER_GANDALF_KEY_PREFIX_FIELD_NUMBER: _ClassVar[int]
    request_sequencer_gandalf_key_prefix: str
    def __init__(self, request_sequencer_gandalf_key_prefix: _Optional[str] = ...) -> None: ...
