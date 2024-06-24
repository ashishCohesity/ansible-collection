from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class MonitoringCookie(_message.Message):
    __slots__ = ("object_name",)
    OBJECT_NAME_FIELD_NUMBER: _ClassVar[int]
    object_name: str
    def __init__(self, object_name: _Optional[str] = ...) -> None: ...

class ColdTierCookie(_message.Message):
    __slots__ = ("last_object_creation_secs", "is_restore_initiated")
    LAST_OBJECT_CREATION_SECS_FIELD_NUMBER: _ClassVar[int]
    IS_RESTORE_INITIATED_FIELD_NUMBER: _ClassVar[int]
    last_object_creation_secs: int
    is_restore_initiated: bool
    def __init__(self, last_object_creation_secs: _Optional[int] = ..., is_restore_initiated: bool = ...) -> None: ...

class WormCookie(_message.Message):
    __slots__ = ("object_version_id", "retention_period_secs")
    OBJECT_VERSION_ID_FIELD_NUMBER: _ClassVar[int]
    RETENTION_PERIOD_SECS_FIELD_NUMBER: _ClassVar[int]
    object_version_id: str
    retention_period_secs: int
    def __init__(self, object_version_id: _Optional[str] = ..., retention_period_secs: _Optional[int] = ...) -> None: ...
