from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class OnDiskObjectMetadataProto(_message.Message):
    __slots__ = ("object_name", "object_part_size_bytes", "object_size_bytes", "num_object_parts", "is_finalized", "description", "restore_status_call_count", "storage_class", "creation_time_usecs", "ctag")
    OBJECT_NAME_FIELD_NUMBER: _ClassVar[int]
    OBJECT_PART_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    OBJECT_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    NUM_OBJECT_PARTS_FIELD_NUMBER: _ClassVar[int]
    IS_FINALIZED_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    RESTORE_STATUS_CALL_COUNT_FIELD_NUMBER: _ClassVar[int]
    STORAGE_CLASS_FIELD_NUMBER: _ClassVar[int]
    CREATION_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    CTAG_FIELD_NUMBER: _ClassVar[int]
    object_name: str
    object_part_size_bytes: int
    object_size_bytes: int
    num_object_parts: int
    is_finalized: bool
    description: str
    restore_status_call_count: int
    storage_class: str
    creation_time_usecs: int
    ctag: str
    def __init__(self, object_name: _Optional[str] = ..., object_part_size_bytes: _Optional[int] = ..., object_size_bytes: _Optional[int] = ..., num_object_parts: _Optional[int] = ..., is_finalized: bool = ..., description: _Optional[str] = ..., restore_status_call_count: _Optional[int] = ..., storage_class: _Optional[str] = ..., creation_time_usecs: _Optional[int] = ..., ctag: _Optional[str] = ...) -> None: ...
