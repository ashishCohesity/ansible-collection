from bridge.audit_log import audit_log_pb2 as _audit_log_pb2
from bridge.base import error_pb2 as _error_pb2
from bridge.snap_fs import dedup_range_pb2 as _dedup_range_pb2
from bridge.snap_fs import entity_handle_pb2 as _entity_handle_pb2
from bridge.snap_fs import snap_fs_metadata_pb2 as _snap_fs_metadata_pb2
from open_util.net import protorpc_pb2 as _protorpc_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LookupFileHandleArg(_message.Message):
    __slots__ = ("path_in_view", "nfs_mount_path", "cifs_mount_path", "view_info")
    class ViewInfo(_message.Message):
        __slots__ = ("view_box_id", "view_id")
        VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
        VIEW_ID_FIELD_NUMBER: _ClassVar[int]
        view_box_id: int
        view_id: int
        def __init__(self, view_box_id: _Optional[int] = ..., view_id: _Optional[int] = ...) -> None: ...
    PATH_IN_VIEW_FIELD_NUMBER: _ClassVar[int]
    NFS_MOUNT_PATH_FIELD_NUMBER: _ClassVar[int]
    CIFS_MOUNT_PATH_FIELD_NUMBER: _ClassVar[int]
    VIEW_INFO_FIELD_NUMBER: _ClassVar[int]
    path_in_view: str
    nfs_mount_path: str
    cifs_mount_path: str
    view_info: LookupFileHandleArg.ViewInfo
    def __init__(self, path_in_view: _Optional[str] = ..., nfs_mount_path: _Optional[str] = ..., cifs_mount_path: _Optional[str] = ..., view_info: _Optional[_Union[LookupFileHandleArg.ViewInfo, _Mapping]] = ...) -> None: ...

class LookupFileHandleResult(_message.Message):
    __slots__ = ("error", "file_handle", "use_dedup_chunks", "dedup_algo_params", "is_externally_triggered_view")
    class DeDupAlgorithmParams(_message.Message):
        __slots__ = ("min_chunk_size", "max_chunk_size", "fp_algo")
        class ChunkingAlgo(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            CHS_FP_1: _ClassVar[LookupFileHandleResult.DeDupAlgorithmParams.ChunkingAlgo]
        CHS_FP_1: LookupFileHandleResult.DeDupAlgorithmParams.ChunkingAlgo
        MIN_CHUNK_SIZE_FIELD_NUMBER: _ClassVar[int]
        MAX_CHUNK_SIZE_FIELD_NUMBER: _ClassVar[int]
        FP_ALGO_FIELD_NUMBER: _ClassVar[int]
        min_chunk_size: int
        max_chunk_size: int
        fp_algo: LookupFileHandleResult.DeDupAlgorithmParams.ChunkingAlgo
        def __init__(self, min_chunk_size: _Optional[int] = ..., max_chunk_size: _Optional[int] = ..., fp_algo: _Optional[_Union[LookupFileHandleResult.DeDupAlgorithmParams.ChunkingAlgo, str]] = ...) -> None: ...
    ERROR_FIELD_NUMBER: _ClassVar[int]
    FILE_HANDLE_FIELD_NUMBER: _ClassVar[int]
    USE_DEDUP_CHUNKS_FIELD_NUMBER: _ClassVar[int]
    DEDUP_ALGO_PARAMS_FIELD_NUMBER: _ClassVar[int]
    IS_EXTERNALLY_TRIGGERED_VIEW_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    file_handle: bytes
    use_dedup_chunks: bool
    dedup_algo_params: LookupFileHandleResult.DeDupAlgorithmParams
    is_externally_triggered_view: bool
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., file_handle: _Optional[bytes] = ..., use_dedup_chunks: bool = ..., dedup_algo_params: _Optional[_Union[LookupFileHandleResult.DeDupAlgorithmParams, _Mapping]] = ..., is_externally_triggered_view: bool = ...) -> None: ...

class GetFileStatArg(_message.Message):
    __slots__ = ("file_handle",)
    FILE_HANDLE_FIELD_NUMBER: _ClassVar[int]
    file_handle: bytes
    def __init__(self, file_handle: _Optional[bytes] = ...) -> None: ...

class GetFileStatResult(_message.Message):
    __slots__ = ("error", "metadata")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    metadata: ReadDirResult.EntryMetadata
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., metadata: _Optional[_Union[ReadDirResult.EntryMetadata, _Mapping]] = ...) -> None: ...

class GetFileSizeArg(_message.Message):
    __slots__ = ("file_handle",)
    FILE_HANDLE_FIELD_NUMBER: _ClassVar[int]
    file_handle: bytes
    def __init__(self, file_handle: _Optional[bytes] = ...) -> None: ...

class GetFileSizeResult(_message.Message):
    __slots__ = ("error", "file_size")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    FILE_SIZE_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    file_size: int
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., file_size: _Optional[int] = ...) -> None: ...

class SetFileSizeArg(_message.Message):
    __slots__ = ("file_handle", "file_size")
    FILE_HANDLE_FIELD_NUMBER: _ClassVar[int]
    FILE_SIZE_FIELD_NUMBER: _ClassVar[int]
    file_handle: bytes
    file_size: int
    def __init__(self, file_handle: _Optional[bytes] = ..., file_size: _Optional[int] = ...) -> None: ...

class SetFileSizeResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class ReadArg(_message.Message):
    __slots__ = ("file_handle", "offset", "count")
    FILE_HANDLE_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    file_handle: bytes
    offset: int
    count: int
    def __init__(self, file_handle: _Optional[bytes] = ..., offset: _Optional[int] = ..., count: _Optional[int] = ...) -> None: ...

class ReadResult(_message.Message):
    __slots__ = ("error", "eof", "data")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    EOF_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    eof: bool
    data: bytes
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., eof: bool = ..., data: _Optional[bytes] = ...) -> None: ...

class WriteArg(_message.Message):
    __slots__ = ("file_handle", "dedup_range", "offset", "data")
    FILE_HANDLE_FIELD_NUMBER: _ClassVar[int]
    DEDUP_RANGE_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    file_handle: bytes
    dedup_range: _dedup_range_pb2.DedupRange
    offset: int
    data: bytes
    def __init__(self, file_handle: _Optional[bytes] = ..., dedup_range: _Optional[_Union[_dedup_range_pb2.DedupRange, _Mapping]] = ..., offset: _Optional[int] = ..., data: _Optional[bytes] = ...) -> None: ...

class WriteResult(_message.Message):
    __slots__ = ("error", "missing_range_offset_vec", "missing_range_length_vec")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    MISSING_RANGE_OFFSET_VEC_FIELD_NUMBER: _ClassVar[int]
    MISSING_RANGE_LENGTH_VEC_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    missing_range_offset_vec: _containers.RepeatedScalarFieldContainer[int]
    missing_range_length_vec: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., missing_range_offset_vec: _Optional[_Iterable[int]] = ..., missing_range_length_vec: _Optional[_Iterable[int]] = ...) -> None: ...

class ReadDirArg(_message.Message):
    __slots__ = ("file_handle", "cookie", "max_entries", "read_old_metadata", "read_metadata")
    FILE_HANDLE_FIELD_NUMBER: _ClassVar[int]
    COOKIE_FIELD_NUMBER: _ClassVar[int]
    MAX_ENTRIES_FIELD_NUMBER: _ClassVar[int]
    READ_OLD_METADATA_FIELD_NUMBER: _ClassVar[int]
    READ_METADATA_FIELD_NUMBER: _ClassVar[int]
    file_handle: bytes
    cookie: int
    max_entries: int
    read_old_metadata: bool
    read_metadata: bool
    def __init__(self, file_handle: _Optional[bytes] = ..., cookie: _Optional[int] = ..., max_entries: _Optional[int] = ..., read_old_metadata: bool = ..., read_metadata: bool = ...) -> None: ...

class ReadDirResult(_message.Message):
    __slots__ = ("error", "entry_vec", "cookie", "file_handle")
    class EntryMetadata(_message.Message):
        __slots__ = ("type", "ctime_usecs", "mtime_usecs", "size", "mode", "uid", "gid")
        class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kFile: _ClassVar[ReadDirResult.EntryMetadata.Type]
            kDirectory: _ClassVar[ReadDirResult.EntryMetadata.Type]
            kSymLink: _ClassVar[ReadDirResult.EntryMetadata.Type]
            kOther: _ClassVar[ReadDirResult.EntryMetadata.Type]
        kFile: ReadDirResult.EntryMetadata.Type
        kDirectory: ReadDirResult.EntryMetadata.Type
        kSymLink: ReadDirResult.EntryMetadata.Type
        kOther: ReadDirResult.EntryMetadata.Type
        TYPE_FIELD_NUMBER: _ClassVar[int]
        CTIME_USECS_FIELD_NUMBER: _ClassVar[int]
        MTIME_USECS_FIELD_NUMBER: _ClassVar[int]
        SIZE_FIELD_NUMBER: _ClassVar[int]
        MODE_FIELD_NUMBER: _ClassVar[int]
        UID_FIELD_NUMBER: _ClassVar[int]
        GID_FIELD_NUMBER: _ClassVar[int]
        type: ReadDirResult.EntryMetadata.Type
        ctime_usecs: int
        mtime_usecs: int
        size: int
        mode: int
        uid: int
        gid: int
        def __init__(self, type: _Optional[_Union[ReadDirResult.EntryMetadata.Type, str]] = ..., ctime_usecs: _Optional[int] = ..., mtime_usecs: _Optional[int] = ..., size: _Optional[int] = ..., mode: _Optional[int] = ..., uid: _Optional[int] = ..., gid: _Optional[int] = ...) -> None: ...
    class Entry(_message.Message):
        __slots__ = ("name", "old_metadata", "metadata", "file_handle")
        NAME_FIELD_NUMBER: _ClassVar[int]
        OLD_METADATA_FIELD_NUMBER: _ClassVar[int]
        METADATA_FIELD_NUMBER: _ClassVar[int]
        FILE_HANDLE_FIELD_NUMBER: _ClassVar[int]
        name: bytes
        old_metadata: ReadDirResult.EntryMetadata
        metadata: _snap_fs_metadata_pb2.InodeMetadataProto
        file_handle: _entity_handle_pb2.EntityHandleProto
        def __init__(self, name: _Optional[bytes] = ..., old_metadata: _Optional[_Union[ReadDirResult.EntryMetadata, _Mapping]] = ..., metadata: _Optional[_Union[_snap_fs_metadata_pb2.InodeMetadataProto, _Mapping]] = ..., file_handle: _Optional[_Union[_entity_handle_pb2.EntityHandleProto, _Mapping]] = ...) -> None: ...
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ENTRY_VEC_FIELD_NUMBER: _ClassVar[int]
    COOKIE_FIELD_NUMBER: _ClassVar[int]
    FILE_HANDLE_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    entry_vec: _containers.RepeatedCompositeFieldContainer[ReadDirResult.Entry]
    cookie: int
    file_handle: bytes
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., entry_vec: _Optional[_Iterable[_Union[ReadDirResult.Entry, _Mapping]]] = ..., cookie: _Optional[int] = ..., file_handle: _Optional[bytes] = ...) -> None: ...

class CloneDirectoryArg(_message.Message):
    __slots__ = ("src_dir_name", "target_parent_dir_name", "target_dir_name", "mode", "uid", "gid")
    SRC_DIR_NAME_FIELD_NUMBER: _ClassVar[int]
    TARGET_PARENT_DIR_NAME_FIELD_NUMBER: _ClassVar[int]
    TARGET_DIR_NAME_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    GID_FIELD_NUMBER: _ClassVar[int]
    src_dir_name: str
    target_parent_dir_name: str
    target_dir_name: str
    mode: int
    uid: int
    gid: int
    def __init__(self, src_dir_name: _Optional[str] = ..., target_parent_dir_name: _Optional[str] = ..., target_dir_name: _Optional[str] = ..., mode: _Optional[int] = ..., uid: _Optional[int] = ..., gid: _Optional[int] = ...) -> None: ...

class CloneDirectoryResult(_message.Message):
    __slots__ = ("error", "directory_handle")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    DIRECTORY_HANDLE_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    directory_handle: bytes
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., directory_handle: _Optional[bytes] = ...) -> None: ...

class CreateFileOrDirArg(_message.Message):
    __slots__ = ("parent_dir_name", "entity_name", "mode", "uid", "gid", "create_type", "create_verifier")
    PARENT_DIR_NAME_FIELD_NUMBER: _ClassVar[int]
    ENTITY_NAME_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    GID_FIELD_NUMBER: _ClassVar[int]
    CREATE_TYPE_FIELD_NUMBER: _ClassVar[int]
    CREATE_VERIFIER_FIELD_NUMBER: _ClassVar[int]
    parent_dir_name: str
    entity_name: str
    mode: int
    uid: int
    gid: int
    create_type: int
    create_verifier: int
    def __init__(self, parent_dir_name: _Optional[str] = ..., entity_name: _Optional[str] = ..., mode: _Optional[int] = ..., uid: _Optional[int] = ..., gid: _Optional[int] = ..., create_type: _Optional[int] = ..., create_verifier: _Optional[int] = ...) -> None: ...

class CreateFileOrDirResult(_message.Message):
    __slots__ = ("error", "entity_handle")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ENTITY_HANDLE_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    entity_handle: bytes
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., entity_handle: _Optional[bytes] = ...) -> None: ...

class CreateEntitiesArg(_message.Message):
    __slots__ = ("parent_dir_name", "parent_eh", "entity_vec")
    class Entity(_message.Message):
        __slots__ = ("type", "name", "mode", "uid", "gid", "logical_size", "ctime_usecs", "mtime_usecs", "symlink_data")
        class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kFile: _ClassVar[CreateEntitiesArg.Entity.Type]
            kDirectory: _ClassVar[CreateEntitiesArg.Entity.Type]
            kSymLink: _ClassVar[CreateEntitiesArg.Entity.Type]
        kFile: CreateEntitiesArg.Entity.Type
        kDirectory: CreateEntitiesArg.Entity.Type
        kSymLink: CreateEntitiesArg.Entity.Type
        TYPE_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        MODE_FIELD_NUMBER: _ClassVar[int]
        UID_FIELD_NUMBER: _ClassVar[int]
        GID_FIELD_NUMBER: _ClassVar[int]
        LOGICAL_SIZE_FIELD_NUMBER: _ClassVar[int]
        CTIME_USECS_FIELD_NUMBER: _ClassVar[int]
        MTIME_USECS_FIELD_NUMBER: _ClassVar[int]
        SYMLINK_DATA_FIELD_NUMBER: _ClassVar[int]
        type: CreateEntitiesArg.Entity.Type
        name: str
        mode: int
        uid: int
        gid: int
        logical_size: int
        ctime_usecs: int
        mtime_usecs: int
        symlink_data: str
        def __init__(self, type: _Optional[_Union[CreateEntitiesArg.Entity.Type, str]] = ..., name: _Optional[str] = ..., mode: _Optional[int] = ..., uid: _Optional[int] = ..., gid: _Optional[int] = ..., logical_size: _Optional[int] = ..., ctime_usecs: _Optional[int] = ..., mtime_usecs: _Optional[int] = ..., symlink_data: _Optional[str] = ...) -> None: ...
    PARENT_DIR_NAME_FIELD_NUMBER: _ClassVar[int]
    PARENT_EH_FIELD_NUMBER: _ClassVar[int]
    ENTITY_VEC_FIELD_NUMBER: _ClassVar[int]
    parent_dir_name: str
    parent_eh: bytes
    entity_vec: _containers.RepeatedCompositeFieldContainer[CreateEntitiesArg.Entity]
    def __init__(self, parent_dir_name: _Optional[str] = ..., parent_eh: _Optional[bytes] = ..., entity_vec: _Optional[_Iterable[_Union[CreateEntitiesArg.Entity, _Mapping]]] = ...) -> None: ...

class CreateEntitiesResult(_message.Message):
    __slots__ = ("error", "entity_handle_vec")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ENTITY_HANDLE_VEC_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    entity_handle_vec: _containers.RepeatedScalarFieldContainer[bytes]
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., entity_handle_vec: _Optional[_Iterable[bytes]] = ...) -> None: ...

class RemoveFileArg(_message.Message):
    __slots__ = ("parent_dir_name", "file_name")
    PARENT_DIR_NAME_FIELD_NUMBER: _ClassVar[int]
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    parent_dir_name: str
    file_name: str
    def __init__(self, parent_dir_name: _Optional[str] = ..., file_name: _Optional[str] = ...) -> None: ...

class RemoveFileResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class RenameArg(_message.Message):
    __slots__ = ("src_parent_dir_name", "src_entity_name", "target_parent_dir_name", "target_entity_name")
    SRC_PARENT_DIR_NAME_FIELD_NUMBER: _ClassVar[int]
    SRC_ENTITY_NAME_FIELD_NUMBER: _ClassVar[int]
    TARGET_PARENT_DIR_NAME_FIELD_NUMBER: _ClassVar[int]
    TARGET_ENTITY_NAME_FIELD_NUMBER: _ClassVar[int]
    src_parent_dir_name: str
    src_entity_name: str
    target_parent_dir_name: str
    target_entity_name: str
    def __init__(self, src_parent_dir_name: _Optional[str] = ..., src_entity_name: _Optional[str] = ..., target_parent_dir_name: _Optional[str] = ..., target_entity_name: _Optional[str] = ...) -> None: ...

class RenameResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class GetInodeMetadataArg(_message.Message):
    __slots__ = ("path",)
    PATH_FIELD_NUMBER: _ClassVar[int]
    path: str
    def __init__(self, path: _Optional[str] = ...) -> None: ...

class GetInodeMetadataResult(_message.Message):
    __slots__ = ("error", "inode_md", "file_handle")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    INODE_MD_FIELD_NUMBER: _ClassVar[int]
    FILE_HANDLE_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    inode_md: _snap_fs_metadata_pb2.InodeMetadataProto
    file_handle: _entity_handle_pb2.EntityHandleProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., inode_md: _Optional[_Union[_snap_fs_metadata_pb2.InodeMetadataProto, _Mapping]] = ..., file_handle: _Optional[_Union[_entity_handle_pb2.EntityHandleProto, _Mapping]] = ...) -> None: ...

class ReportAuditEventArg(_message.Message):
    __slots__ = ("id", "request_type", "ddw_portal_audit_log", "file_handle")
    ID_FIELD_NUMBER: _ClassVar[int]
    REQUEST_TYPE_FIELD_NUMBER: _ClassVar[int]
    DDW_PORTAL_AUDIT_LOG_FIELD_NUMBER: _ClassVar[int]
    FILE_HANDLE_FIELD_NUMBER: _ClassVar[int]
    id: _audit_log_pb2.AuditRecordId
    request_type: _audit_log_pb2.AuditRecord.RequestType
    ddw_portal_audit_log: _audit_log_pb2.DdwPortalAuditLog
    file_handle: bytes
    def __init__(self, id: _Optional[_Union[_audit_log_pb2.AuditRecordId, _Mapping]] = ..., request_type: _Optional[_Union[_audit_log_pb2.AuditRecord.RequestType, str]] = ..., ddw_portal_audit_log: _Optional[_Union[_audit_log_pb2.DdwPortalAuditLog, _Mapping]] = ..., file_handle: _Optional[bytes] = ...) -> None: ...

class ReportAuditEventResult(_message.Message):
    __slots__ = ("error", "id")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    id: _audit_log_pb2.AuditRecordId
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., id: _Optional[_Union[_audit_log_pb2.AuditRecordId, _Mapping]] = ...) -> None: ...
