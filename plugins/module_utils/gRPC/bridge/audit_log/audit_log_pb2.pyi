from bridge.s3_portal.base import s3_enums_pb2 as _s3_enums_pb2
from bridge.s3_portal.base import s3_error_pb2 as _s3_error_pb2
from bridge.snap_fs import entity_handle_pb2 as _entity_handle_pb2
from bridge.snap_fs import snap_fs_metadata_pb2 as _snap_fs_metadata_pb2
from configs import cluster_config_pb2 as _cluster_config_pb2
from yoda.es import jsonname_pb2 as _jsonname_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UserIdentity(_message.Message):
    __slots__ = ("user_name", "domain_name", "is_guest_session", "is_anonymous_session", "user_id", "user_sid")
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    IS_GUEST_SESSION_FIELD_NUMBER: _ClassVar[int]
    IS_ANONYMOUS_SESSION_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    USER_SID_FIELD_NUMBER: _ClassVar[int]
    user_name: str
    domain_name: str
    is_guest_session: bool
    is_anonymous_session: bool
    user_id: int
    user_sid: _cluster_config_pb2.ClusterConfigProto.SID
    def __init__(self, user_name: _Optional[str] = ..., domain_name: _Optional[str] = ..., is_guest_session: bool = ..., is_anonymous_session: bool = ..., user_id: _Optional[int] = ..., user_sid: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.SID, _Mapping]] = ...) -> None: ...

class AuditRecordId(_message.Message):
    __slots__ = ("session_id", "local_id")
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    LOCAL_ID_FIELD_NUMBER: _ClassVar[int]
    session_id: int
    local_id: int
    def __init__(self, session_id: _Optional[int] = ..., local_id: _Optional[int] = ...) -> None: ...

class FileAttributes(_message.Message):
    __slots__ = ("mode", "user_id", "group_id", "size_bytes", "mtime_usecs", "extended_attributes", "file_access_mask", "creation_time_usecs", "atime_usecs")
    MODE_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    MTIME_USECS_FIELD_NUMBER: _ClassVar[int]
    EXTENDED_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    FILE_ACCESS_MASK_FIELD_NUMBER: _ClassVar[int]
    CREATION_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    ATIME_USECS_FIELD_NUMBER: _ClassVar[int]
    mode: int
    user_id: int
    group_id: int
    size_bytes: int
    mtime_usecs: int
    extended_attributes: _snap_fs_metadata_pb2.InodeMetadataProto.ExtendedAttributes
    file_access_mask: int
    creation_time_usecs: int
    atime_usecs: int
    def __init__(self, mode: _Optional[int] = ..., user_id: _Optional[int] = ..., group_id: _Optional[int] = ..., size_bytes: _Optional[int] = ..., mtime_usecs: _Optional[int] = ..., extended_attributes: _Optional[_Union[_snap_fs_metadata_pb2.InodeMetadataProto.ExtendedAttributes, _Mapping]] = ..., file_access_mask: _Optional[int] = ..., creation_time_usecs: _Optional[int] = ..., atime_usecs: _Optional[int] = ...) -> None: ...

class S3Response(_message.Message):
    __slots__ = ("etag", "upload_id", "part_number")
    ETAG_FIELD_NUMBER: _ClassVar[int]
    UPLOAD_ID_FIELD_NUMBER: _ClassVar[int]
    PART_NUMBER_FIELD_NUMBER: _ClassVar[int]
    etag: str
    upload_id: int
    part_number: int
    def __init__(self, etag: _Optional[str] = ..., upload_id: _Optional[int] = ..., part_number: _Optional[int] = ...) -> None: ...

class AuditRecord(_message.Message):
    __slots__ = ("id", "timestamp_usecs", "entity_handle", "view_name", "view_alias_name", "user_identity", "client_ip", "protocol", "request_type", "mnt_response_status", "nfs_response_status", "smb_response_status", "bridge_response_status", "path", "file_type", "file_attr", "prev_file_attr", "dest_path", "dest_entity_handle", "delete_on_close", "s3_request_type", "s3_response_status", "source_parent_entity_handle", "s3_response", "should_publish_audit_record", "should_log_filer_event_record", "lcm_rule_id", "ddw_portal_audit_log")
    class Protocol(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kSMB: _ClassVar[AuditRecord.Protocol]
        kNFS3: _ClassVar[AuditRecord.Protocol]
        kS3: _ClassVar[AuditRecord.Protocol]
        kSwift: _ClassVar[AuditRecord.Protocol]
        kSnapFS: _ClassVar[AuditRecord.Protocol]
        kDdwPortal: _ClassVar[AuditRecord.Protocol]
    kSMB: AuditRecord.Protocol
    kNFS3: AuditRecord.Protocol
    kS3: AuditRecord.Protocol
    kSwift: AuditRecord.Protocol
    kSnapFS: AuditRecord.Protocol
    kDdwPortal: AuditRecord.Protocol
    class RequestType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kLogOn: _ClassVar[AuditRecord.RequestType]
        kLogOff: _ClassVar[AuditRecord.RequestType]
        kMount: _ClassVar[AuditRecord.RequestType]
        kOpen: _ClassVar[AuditRecord.RequestType]
        kCreate: _ClassVar[AuditRecord.RequestType]
        kClose: _ClassVar[AuditRecord.RequestType]
        kDelete: _ClassVar[AuditRecord.RequestType]
        kRename: _ClassVar[AuditRecord.RequestType]
        kSetAttributes: _ClassVar[AuditRecord.RequestType]
        kCommit: _ClassVar[AuditRecord.RequestType]
        kUmount: _ClassVar[AuditRecord.RequestType]
        kQuarantineThreat: _ClassVar[AuditRecord.RequestType]
        kUnquarantineThreat: _ClassVar[AuditRecord.RequestType]
        kResetThreat: _ClassVar[AuditRecord.RequestType]
        kRead: _ClassVar[AuditRecord.RequestType]
    kLogOn: AuditRecord.RequestType
    kLogOff: AuditRecord.RequestType
    kMount: AuditRecord.RequestType
    kOpen: AuditRecord.RequestType
    kCreate: AuditRecord.RequestType
    kClose: AuditRecord.RequestType
    kDelete: AuditRecord.RequestType
    kRename: AuditRecord.RequestType
    kSetAttributes: AuditRecord.RequestType
    kCommit: AuditRecord.RequestType
    kUmount: AuditRecord.RequestType
    kQuarantineThreat: AuditRecord.RequestType
    kUnquarantineThreat: AuditRecord.RequestType
    kResetThreat: AuditRecord.RequestType
    kRead: AuditRecord.RequestType
    class FileType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kFile: _ClassVar[AuditRecord.FileType]
        kDirectory: _ClassVar[AuditRecord.FileType]
        kBlockDevice: _ClassVar[AuditRecord.FileType]
        kCharacterDevice: _ClassVar[AuditRecord.FileType]
        kSymLink: _ClassVar[AuditRecord.FileType]
        kLink: _ClassVar[AuditRecord.FileType]
        kSocket: _ClassVar[AuditRecord.FileType]
        kPipe: _ClassVar[AuditRecord.FileType]
    kFile: AuditRecord.FileType
    kDirectory: AuditRecord.FileType
    kBlockDevice: AuditRecord.FileType
    kCharacterDevice: AuditRecord.FileType
    kSymLink: AuditRecord.FileType
    kLink: AuditRecord.FileType
    kSocket: AuditRecord.FileType
    kPipe: AuditRecord.FileType
    ID_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
    ENTITY_HANDLE_FIELD_NUMBER: _ClassVar[int]
    VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    VIEW_ALIAS_NAME_FIELD_NUMBER: _ClassVar[int]
    USER_IDENTITY_FIELD_NUMBER: _ClassVar[int]
    CLIENT_IP_FIELD_NUMBER: _ClassVar[int]
    PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    REQUEST_TYPE_FIELD_NUMBER: _ClassVar[int]
    MNT_RESPONSE_STATUS_FIELD_NUMBER: _ClassVar[int]
    NFS_RESPONSE_STATUS_FIELD_NUMBER: _ClassVar[int]
    SMB_RESPONSE_STATUS_FIELD_NUMBER: _ClassVar[int]
    BRIDGE_RESPONSE_STATUS_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    FILE_TYPE_FIELD_NUMBER: _ClassVar[int]
    FILE_ATTR_FIELD_NUMBER: _ClassVar[int]
    PREV_FILE_ATTR_FIELD_NUMBER: _ClassVar[int]
    DEST_PATH_FIELD_NUMBER: _ClassVar[int]
    DEST_ENTITY_HANDLE_FIELD_NUMBER: _ClassVar[int]
    DELETE_ON_CLOSE_FIELD_NUMBER: _ClassVar[int]
    S3_REQUEST_TYPE_FIELD_NUMBER: _ClassVar[int]
    S3_RESPONSE_STATUS_FIELD_NUMBER: _ClassVar[int]
    SOURCE_PARENT_ENTITY_HANDLE_FIELD_NUMBER: _ClassVar[int]
    S3_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    SHOULD_PUBLISH_AUDIT_RECORD_FIELD_NUMBER: _ClassVar[int]
    SHOULD_LOG_FILER_EVENT_RECORD_FIELD_NUMBER: _ClassVar[int]
    LCM_RULE_ID_FIELD_NUMBER: _ClassVar[int]
    DDW_PORTAL_AUDIT_LOG_FIELD_NUMBER: _ClassVar[int]
    id: AuditRecordId
    timestamp_usecs: int
    entity_handle: _entity_handle_pb2.EntityHandleProto
    view_name: str
    view_alias_name: str
    user_identity: UserIdentity
    client_ip: str
    protocol: AuditRecord.Protocol
    request_type: AuditRecord.RequestType
    mnt_response_status: int
    nfs_response_status: int
    smb_response_status: int
    bridge_response_status: int
    path: str
    file_type: AuditRecord.FileType
    file_attr: FileAttributes
    prev_file_attr: FileAttributes
    dest_path: str
    dest_entity_handle: _entity_handle_pb2.EntityHandleProto
    delete_on_close: bool
    s3_request_type: _s3_enums_pb2.Request.Type
    s3_response_status: _s3_error_pb2.S3ErrorProto.Code
    source_parent_entity_handle: _entity_handle_pb2.EntityHandleProto
    s3_response: S3Response
    should_publish_audit_record: bool
    should_log_filer_event_record: bool
    lcm_rule_id: str
    ddw_portal_audit_log: DdwPortalAuditLog
    def __init__(self, id: _Optional[_Union[AuditRecordId, _Mapping]] = ..., timestamp_usecs: _Optional[int] = ..., entity_handle: _Optional[_Union[_entity_handle_pb2.EntityHandleProto, _Mapping]] = ..., view_name: _Optional[str] = ..., view_alias_name: _Optional[str] = ..., user_identity: _Optional[_Union[UserIdentity, _Mapping]] = ..., client_ip: _Optional[str] = ..., protocol: _Optional[_Union[AuditRecord.Protocol, str]] = ..., request_type: _Optional[_Union[AuditRecord.RequestType, str]] = ..., mnt_response_status: _Optional[int] = ..., nfs_response_status: _Optional[int] = ..., smb_response_status: _Optional[int] = ..., bridge_response_status: _Optional[int] = ..., path: _Optional[str] = ..., file_type: _Optional[_Union[AuditRecord.FileType, str]] = ..., file_attr: _Optional[_Union[FileAttributes, _Mapping]] = ..., prev_file_attr: _Optional[_Union[FileAttributes, _Mapping]] = ..., dest_path: _Optional[str] = ..., dest_entity_handle: _Optional[_Union[_entity_handle_pb2.EntityHandleProto, _Mapping]] = ..., delete_on_close: bool = ..., s3_request_type: _Optional[_Union[_s3_enums_pb2.Request.Type, str]] = ..., s3_response_status: _Optional[_Union[_s3_error_pb2.S3ErrorProto.Code, str]] = ..., source_parent_entity_handle: _Optional[_Union[_entity_handle_pb2.EntityHandleProto, _Mapping]] = ..., s3_response: _Optional[_Union[S3Response, _Mapping]] = ..., should_publish_audit_record: bool = ..., should_log_filer_event_record: bool = ..., lcm_rule_id: _Optional[str] = ..., ddw_portal_audit_log: _Optional[_Union[DdwPortalAuditLog, _Mapping]] = ...) -> None: ...

class FormattedAuditRecord(_message.Message):
    __slots__ = ("timestamp", "record_id", "protocol", "client_ip", "user_name", "user_id", "domain_name", "user_sid", "view_name", "view_alias_name", "fsid", "request_type", "result", "entity_type", "entity_path", "entity_inode", "entity_mode", "entity_user_id", "entity_group_id", "entity_modify_timestamp", "entity_access_mask", "destination_entity_path", "destination_entity_inode", "delete_on_close", "smb2_security_descriptor", "security_descriptor", "prev_smb2_security_descriptor", "prev_security_descriptor", "prev_entity_mode", "prev_entity_user_id", "prev_entity_group_id", "inode_size_bytes", "source_parent_entity_inode", "etag", "upload_id", "part_number", "ddw_portal_audit_log", "lcm_rule_name", "entity_creation_timestamp", "entity_access_timestamp")
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    RECORD_ID_FIELD_NUMBER: _ClassVar[int]
    PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    CLIENT_IP_FIELD_NUMBER: _ClassVar[int]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    USER_SID_FIELD_NUMBER: _ClassVar[int]
    VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    VIEW_ALIAS_NAME_FIELD_NUMBER: _ClassVar[int]
    FSID_FIELD_NUMBER: _ClassVar[int]
    REQUEST_TYPE_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    ENTITY_TYPE_FIELD_NUMBER: _ClassVar[int]
    ENTITY_PATH_FIELD_NUMBER: _ClassVar[int]
    ENTITY_INODE_FIELD_NUMBER: _ClassVar[int]
    ENTITY_MODE_FIELD_NUMBER: _ClassVar[int]
    ENTITY_USER_ID_FIELD_NUMBER: _ClassVar[int]
    ENTITY_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    ENTITY_MODIFY_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ACCESS_MASK_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_ENTITY_PATH_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_ENTITY_INODE_FIELD_NUMBER: _ClassVar[int]
    DELETE_ON_CLOSE_FIELD_NUMBER: _ClassVar[int]
    SMB2_SECURITY_DESCRIPTOR_FIELD_NUMBER: _ClassVar[int]
    SECURITY_DESCRIPTOR_FIELD_NUMBER: _ClassVar[int]
    PREV_SMB2_SECURITY_DESCRIPTOR_FIELD_NUMBER: _ClassVar[int]
    PREV_SECURITY_DESCRIPTOR_FIELD_NUMBER: _ClassVar[int]
    PREV_ENTITY_MODE_FIELD_NUMBER: _ClassVar[int]
    PREV_ENTITY_USER_ID_FIELD_NUMBER: _ClassVar[int]
    PREV_ENTITY_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    INODE_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    SOURCE_PARENT_ENTITY_INODE_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    UPLOAD_ID_FIELD_NUMBER: _ClassVar[int]
    PART_NUMBER_FIELD_NUMBER: _ClassVar[int]
    DDW_PORTAL_AUDIT_LOG_FIELD_NUMBER: _ClassVar[int]
    LCM_RULE_NAME_FIELD_NUMBER: _ClassVar[int]
    ENTITY_CREATION_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ACCESS_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    timestamp: str
    record_id: str
    protocol: str
    client_ip: str
    user_name: str
    user_id: int
    domain_name: str
    user_sid: str
    view_name: str
    view_alias_name: str
    fsid: int
    request_type: str
    result: str
    entity_type: str
    entity_path: str
    entity_inode: int
    entity_mode: int
    entity_user_id: int
    entity_group_id: int
    entity_modify_timestamp: str
    entity_access_mask: int
    destination_entity_path: str
    destination_entity_inode: int
    delete_on_close: bool
    smb2_security_descriptor: str
    security_descriptor: FormattedSmb2SecurityDescriptor
    prev_smb2_security_descriptor: str
    prev_security_descriptor: FormattedSmb2SecurityDescriptor
    prev_entity_mode: int
    prev_entity_user_id: int
    prev_entity_group_id: int
    inode_size_bytes: int
    source_parent_entity_inode: int
    etag: str
    upload_id: int
    part_number: int
    ddw_portal_audit_log: FormattedDdwPortalAuditLog
    lcm_rule_name: str
    entity_creation_timestamp: str
    entity_access_timestamp: str
    def __init__(self, timestamp: _Optional[str] = ..., record_id: _Optional[str] = ..., protocol: _Optional[str] = ..., client_ip: _Optional[str] = ..., user_name: _Optional[str] = ..., user_id: _Optional[int] = ..., domain_name: _Optional[str] = ..., user_sid: _Optional[str] = ..., view_name: _Optional[str] = ..., view_alias_name: _Optional[str] = ..., fsid: _Optional[int] = ..., request_type: _Optional[str] = ..., result: _Optional[str] = ..., entity_type: _Optional[str] = ..., entity_path: _Optional[str] = ..., entity_inode: _Optional[int] = ..., entity_mode: _Optional[int] = ..., entity_user_id: _Optional[int] = ..., entity_group_id: _Optional[int] = ..., entity_modify_timestamp: _Optional[str] = ..., entity_access_mask: _Optional[int] = ..., destination_entity_path: _Optional[str] = ..., destination_entity_inode: _Optional[int] = ..., delete_on_close: bool = ..., smb2_security_descriptor: _Optional[str] = ..., security_descriptor: _Optional[_Union[FormattedSmb2SecurityDescriptor, _Mapping]] = ..., prev_smb2_security_descriptor: _Optional[str] = ..., prev_security_descriptor: _Optional[_Union[FormattedSmb2SecurityDescriptor, _Mapping]] = ..., prev_entity_mode: _Optional[int] = ..., prev_entity_user_id: _Optional[int] = ..., prev_entity_group_id: _Optional[int] = ..., inode_size_bytes: _Optional[int] = ..., source_parent_entity_inode: _Optional[int] = ..., etag: _Optional[str] = ..., upload_id: _Optional[int] = ..., part_number: _Optional[int] = ..., ddw_portal_audit_log: _Optional[_Union[FormattedDdwPortalAuditLog, _Mapping]] = ..., lcm_rule_name: _Optional[str] = ..., entity_creation_timestamp: _Optional[str] = ..., entity_access_timestamp: _Optional[str] = ...) -> None: ...

class FormattedACE(_message.Message):
    __slots__ = ("ace_type", "ace_flags", "access_mask", "sid")
    ACE_TYPE_FIELD_NUMBER: _ClassVar[int]
    ACE_FLAGS_FIELD_NUMBER: _ClassVar[int]
    ACCESS_MASK_FIELD_NUMBER: _ClassVar[int]
    SID_FIELD_NUMBER: _ClassVar[int]
    ace_type: int
    ace_flags: int
    access_mask: int
    sid: str
    def __init__(self, ace_type: _Optional[int] = ..., ace_flags: _Optional[int] = ..., access_mask: _Optional[int] = ..., sid: _Optional[str] = ...) -> None: ...

class FormattedSmb2SecurityDescriptor(_message.Message):
    __slots__ = ("control", "owner_sid", "group_sid", "dacls")
    CONTROL_FIELD_NUMBER: _ClassVar[int]
    OWNER_SID_FIELD_NUMBER: _ClassVar[int]
    GROUP_SID_FIELD_NUMBER: _ClassVar[int]
    DACLS_FIELD_NUMBER: _ClassVar[int]
    control: int
    owner_sid: str
    group_sid: str
    dacls: _containers.RepeatedCompositeFieldContainer[FormattedACE]
    def __init__(self, control: _Optional[int] = ..., owner_sid: _Optional[str] = ..., group_sid: _Optional[str] = ..., dacls: _Optional[_Iterable[_Union[FormattedACE, _Mapping]]] = ...) -> None: ...

class DdwPortalAuditLog(_message.Message):
    __slots__ = ("file_name", "start_time", "end_time", "file_size", "read_size", "status", "source_type", "tag")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kInProgress: _ClassVar[DdwPortalAuditLog.Status]
        kSuccess: _ClassVar[DdwPortalAuditLog.Status]
        kFailure: _ClassVar[DdwPortalAuditLog.Status]
    kInProgress: DdwPortalAuditLog.Status
    kSuccess: DdwPortalAuditLog.Status
    kFailure: DdwPortalAuditLog.Status
    class SourceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kGeneral: _ClassVar[DdwPortalAuditLog.SourceType]
        kSBT: _ClassVar[DdwPortalAuditLog.SourceType]
    kGeneral: DdwPortalAuditLog.SourceType
    kSBT: DdwPortalAuditLog.SourceType
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    FILE_SIZE_FIELD_NUMBER: _ClassVar[int]
    READ_SIZE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    TAG_FIELD_NUMBER: _ClassVar[int]
    file_name: str
    start_time: int
    end_time: int
    file_size: int
    read_size: int
    status: DdwPortalAuditLog.Status
    source_type: DdwPortalAuditLog.SourceType
    tag: str
    def __init__(self, file_name: _Optional[str] = ..., start_time: _Optional[int] = ..., end_time: _Optional[int] = ..., file_size: _Optional[int] = ..., read_size: _Optional[int] = ..., status: _Optional[_Union[DdwPortalAuditLog.Status, str]] = ..., source_type: _Optional[_Union[DdwPortalAuditLog.SourceType, str]] = ..., tag: _Optional[str] = ...) -> None: ...

class FormattedDdwPortalAuditLog(_message.Message):
    __slots__ = ("file_name", "start_time", "end_time", "file_size", "read_size", "status", "source_type", "tag")
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    FILE_SIZE_FIELD_NUMBER: _ClassVar[int]
    READ_SIZE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    TAG_FIELD_NUMBER: _ClassVar[int]
    file_name: str
    start_time: int
    end_time: int
    file_size: int
    read_size: int
    status: str
    source_type: str
    tag: str
    def __init__(self, file_name: _Optional[str] = ..., start_time: _Optional[int] = ..., end_time: _Optional[int] = ..., file_size: _Optional[int] = ..., read_size: _Optional[int] = ..., status: _Optional[str] = ..., source_type: _Optional[str] = ..., tag: _Optional[str] = ...) -> None: ...
