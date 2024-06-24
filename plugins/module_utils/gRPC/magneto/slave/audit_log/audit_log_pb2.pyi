from magneto.directory_walker import directory_walker_pb2 as _directory_walker_pb2
from yoda.es import jsonname_pb2 as _jsonname_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AuditRecord(_message.Message):
    __slots__ = ("timestamp_usecs", "request_type", "entity_metadata", "view_name", "dest_path", "remote_share", "job_name", "error_msg")
    class RequestType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kDownTier: _ClassVar[AuditRecord.RequestType]
        kRenameSymlinkTgt: _ClassVar[AuditRecord.RequestType]
        kOrphanDelete: _ClassVar[AuditRecord.RequestType]
        kUpTier: _ClassVar[AuditRecord.RequestType]
    kDownTier: AuditRecord.RequestType
    kRenameSymlinkTgt: AuditRecord.RequestType
    kOrphanDelete: AuditRecord.RequestType
    kUpTier: AuditRecord.RequestType
    TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
    REQUEST_TYPE_FIELD_NUMBER: _ClassVar[int]
    ENTITY_METADATA_FIELD_NUMBER: _ClassVar[int]
    VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    DEST_PATH_FIELD_NUMBER: _ClassVar[int]
    REMOTE_SHARE_FIELD_NUMBER: _ClassVar[int]
    JOB_NAME_FIELD_NUMBER: _ClassVar[int]
    ERROR_MSG_FIELD_NUMBER: _ClassVar[int]
    timestamp_usecs: int
    request_type: AuditRecord.RequestType
    entity_metadata: _directory_walker_pb2.EntityMetadata
    view_name: str
    dest_path: str
    remote_share: str
    job_name: str
    error_msg: str
    def __init__(self, timestamp_usecs: _Optional[int] = ..., request_type: _Optional[_Union[AuditRecord.RequestType, str]] = ..., entity_metadata: _Optional[_Union[_directory_walker_pb2.EntityMetadata, _Mapping]] = ..., view_name: _Optional[str] = ..., dest_path: _Optional[str] = ..., remote_share: _Optional[str] = ..., job_name: _Optional[str] = ..., error_msg: _Optional[str] = ...) -> None: ...

class FormattedAuditRecord(_message.Message):
    __slots__ = ("timestamp", "request_type", "remote_share", "view_name", "entity_path", "entity_modify_timestamp", "entity_access_timestamp", "entity_mode", "entity_user_id", "entity_group_id", "entity_size", "entity_inode", "destination_entity_path", "job_name", "error_msg")
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    REQUEST_TYPE_FIELD_NUMBER: _ClassVar[int]
    REMOTE_SHARE_FIELD_NUMBER: _ClassVar[int]
    VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    ENTITY_PATH_FIELD_NUMBER: _ClassVar[int]
    ENTITY_MODIFY_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ACCESS_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    ENTITY_MODE_FIELD_NUMBER: _ClassVar[int]
    ENTITY_USER_ID_FIELD_NUMBER: _ClassVar[int]
    ENTITY_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    ENTITY_SIZE_FIELD_NUMBER: _ClassVar[int]
    ENTITY_INODE_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_ENTITY_PATH_FIELD_NUMBER: _ClassVar[int]
    JOB_NAME_FIELD_NUMBER: _ClassVar[int]
    ERROR_MSG_FIELD_NUMBER: _ClassVar[int]
    timestamp: str
    request_type: str
    remote_share: str
    view_name: str
    entity_path: str
    entity_modify_timestamp: str
    entity_access_timestamp: str
    entity_mode: int
    entity_user_id: int
    entity_group_id: int
    entity_size: int
    entity_inode: int
    destination_entity_path: str
    job_name: str
    error_msg: str
    def __init__(self, timestamp: _Optional[str] = ..., request_type: _Optional[str] = ..., remote_share: _Optional[str] = ..., view_name: _Optional[str] = ..., entity_path: _Optional[str] = ..., entity_modify_timestamp: _Optional[str] = ..., entity_access_timestamp: _Optional[str] = ..., entity_mode: _Optional[int] = ..., entity_user_id: _Optional[int] = ..., entity_group_id: _Optional[int] = ..., entity_size: _Optional[int] = ..., entity_inode: _Optional[int] = ..., destination_entity_path: _Optional[str] = ..., job_name: _Optional[str] = ..., error_msg: _Optional[str] = ...) -> None: ...
