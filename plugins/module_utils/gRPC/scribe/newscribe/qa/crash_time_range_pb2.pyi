from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CrashTimeRangeProto(_message.Message):
    __slots__ = ("crash_after_msecs", "crash_before_msecs")
    CRASH_AFTER_MSECS_FIELD_NUMBER: _ClassVar[int]
    CRASH_BEFORE_MSECS_FIELD_NUMBER: _ClassVar[int]
    crash_after_msecs: int
    crash_before_msecs: int
    def __init__(self, crash_after_msecs: _Optional[int] = ..., crash_before_msecs: _Optional[int] = ...) -> None: ...
