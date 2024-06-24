from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ConstantsProto(_message.Message):
    __slots__ = ("apollo_mr_master_gandalf_key",)
    APOLLO_MR_MASTER_GANDALF_KEY_FIELD_NUMBER: _ClassVar[int]
    apollo_mr_master_gandalf_key: str
    def __init__(self, apollo_mr_master_gandalf_key: _Optional[str] = ...) -> None: ...
