from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class GrootConfigProto(_message.Message):
    __slots__ = ("gandalf_master_lock_name", "database_service_id", "master_status_url", "database_info_url", "lookup_master_url", "magneto_fullsync_url")
    GANDALF_MASTER_LOCK_NAME_FIELD_NUMBER: _ClassVar[int]
    DATABASE_SERVICE_ID_FIELD_NUMBER: _ClassVar[int]
    MASTER_STATUS_URL_FIELD_NUMBER: _ClassVar[int]
    DATABASE_INFO_URL_FIELD_NUMBER: _ClassVar[int]
    LOOKUP_MASTER_URL_FIELD_NUMBER: _ClassVar[int]
    MAGNETO_FULLSYNC_URL_FIELD_NUMBER: _ClassVar[int]
    gandalf_master_lock_name: str
    database_service_id: int
    master_status_url: str
    database_info_url: str
    lookup_master_url: str
    magneto_fullsync_url: str
    def __init__(self, gandalf_master_lock_name: _Optional[str] = ..., database_service_id: _Optional[int] = ..., master_status_url: _Optional[str] = ..., database_info_url: _Optional[str] = ..., lookup_master_url: _Optional[str] = ..., magneto_fullsync_url: _Optional[str] = ...) -> None: ...
