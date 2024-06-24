from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class IrisAuthConstants(_message.Message):
    __slots__ = ("shared_secret_key", "pass_phrase_format")
    SHARED_SECRET_KEY_FIELD_NUMBER: _ClassVar[int]
    PASS_PHRASE_FORMAT_FIELD_NUMBER: _ClassVar[int]
    shared_secret_key: str
    pass_phrase_format: str
    def __init__(self, shared_secret_key: _Optional[str] = ..., pass_phrase_format: _Optional[str] = ...) -> None: ...
