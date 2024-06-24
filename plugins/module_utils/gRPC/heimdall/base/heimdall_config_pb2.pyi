from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class HeimdallConfigProto(_message.Message):
    __slots__ = ("gandalf_master_lock_name", "master_status_url", "lookup_master_url", "cloud_status_page_url")
    GANDALF_MASTER_LOCK_NAME_FIELD_NUMBER: _ClassVar[int]
    MASTER_STATUS_URL_FIELD_NUMBER: _ClassVar[int]
    LOOKUP_MASTER_URL_FIELD_NUMBER: _ClassVar[int]
    CLOUD_STATUS_PAGE_URL_FIELD_NUMBER: _ClassVar[int]
    gandalf_master_lock_name: str
    master_status_url: str
    lookup_master_url: str
    cloud_status_page_url: str
    def __init__(self, gandalf_master_lock_name: _Optional[str] = ..., master_status_url: _Optional[str] = ..., lookup_master_url: _Optional[str] = ..., cloud_status_page_url: _Optional[str] = ...) -> None: ...
