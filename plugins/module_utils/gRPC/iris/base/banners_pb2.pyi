from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Banner(_message.Message):
    __slots__ = ("version", "banner_id", "content", "description", "created_time_msecs", "last_updated_time_msecs")
    VERSION_FIELD_NUMBER: _ClassVar[int]
    BANNER_ID_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CREATED_TIME_MSECS_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATED_TIME_MSECS_FIELD_NUMBER: _ClassVar[int]
    version: int
    banner_id: str
    content: str
    description: str
    created_time_msecs: int
    last_updated_time_msecs: int
    def __init__(self, version: _Optional[int] = ..., banner_id: _Optional[str] = ..., content: _Optional[str] = ..., description: _Optional[str] = ..., created_time_msecs: _Optional[int] = ..., last_updated_time_msecs: _Optional[int] = ...) -> None: ...
