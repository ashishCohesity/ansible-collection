from apache_util.base import error_pb2 as _error_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EntityType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kFile: _ClassVar[EntityType]
    kDirectory: _ClassVar[EntityType]
    kSymLink: _ClassVar[EntityType]
    kReparsePointFile: _ClassVar[EntityType]
    kReparsePointDir: _ClassVar[EntityType]
kFile: EntityType
kDirectory: EntityType
kSymLink: EntityType
kReparsePointFile: EntityType
kReparsePointDir: EntityType

class SmbProxyGetStatusInfoArg(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SmbProxyGetStatusInfoResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class SmbProxyBaseArg(_message.Message):
    __slots__ = ("task_key", "server", "share", "username", "password", "domain_name", "root_dir", "continue_on_error", "skip_metadata_vec", "populate_root_dir", "encryption_enabled", "entity_id", "task_type", "hostname", "kdc")
    TASK_KEY_FIELD_NUMBER: _ClassVar[int]
    SERVER_FIELD_NUMBER: _ClassVar[int]
    SHARE_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    ROOT_DIR_FIELD_NUMBER: _ClassVar[int]
    CONTINUE_ON_ERROR_FIELD_NUMBER: _ClassVar[int]
    SKIP_METADATA_VEC_FIELD_NUMBER: _ClassVar[int]
    POPULATE_ROOT_DIR_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_ENABLED_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    TASK_TYPE_FIELD_NUMBER: _ClassVar[int]
    HOSTNAME_FIELD_NUMBER: _ClassVar[int]
    KDC_FIELD_NUMBER: _ClassVar[int]
    task_key: str
    server: str
    share: str
    username: str
    password: str
    domain_name: str
    root_dir: bytes
    continue_on_error: bool
    skip_metadata_vec: _containers.RepeatedScalarFieldContainer[bytes]
    populate_root_dir: bool
    encryption_enabled: bool
    entity_id: int
    task_type: TaskType.Type
    hostname: str
    kdc: str
    def __init__(self, task_key: _Optional[str] = ..., server: _Optional[str] = ..., share: _Optional[str] = ..., username: _Optional[str] = ..., password: _Optional[str] = ..., domain_name: _Optional[str] = ..., root_dir: _Optional[bytes] = ..., continue_on_error: bool = ..., skip_metadata_vec: _Optional[_Iterable[bytes]] = ..., populate_root_dir: bool = ..., encryption_enabled: bool = ..., entity_id: _Optional[int] = ..., task_type: _Optional[_Union[TaskType.Type, str]] = ..., hostname: _Optional[str] = ..., kdc: _Optional[str] = ...) -> None: ...

class SmbProxyResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class ExtendedAttribute(_message.Message):
    __slots__ = ("name", "value")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    name: str
    value: bytes
    def __init__(self, name: _Optional[str] = ..., value: _Optional[bytes] = ...) -> None: ...

class EntityMetadata(_message.Message):
    __slots__ = ("root_dir", "path", "type", "attributes", "uid", "gid", "change_time_usecs", "modify_time_usecs", "create_time_usecs", "access_time_usecs", "size", "allocation_size", "inode_id", "num_hardlinks", "first_path_to_hardlink", "symlink_target", "symlink_flags", "reparse_point_info", "extended_attributes", "error")
    class EntityType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kFile: _ClassVar[EntityMetadata.EntityType]
        kDirectory: _ClassVar[EntityMetadata.EntityType]
        kSymLink: _ClassVar[EntityMetadata.EntityType]
    kFile: EntityMetadata.EntityType
    kDirectory: EntityMetadata.EntityType
    kSymLink: EntityMetadata.EntityType
    class ReparsePointInfo(_message.Message):
        __slots__ = ("reparse_tag", "symlink_reparse_point_info")
        class SymlinkReparsePointInfo(_message.Message):
            __slots__ = ("substitute_name", "print_name", "is_path_relative")
            SUBSTITUTE_NAME_FIELD_NUMBER: _ClassVar[int]
            PRINT_NAME_FIELD_NUMBER: _ClassVar[int]
            IS_PATH_RELATIVE_FIELD_NUMBER: _ClassVar[int]
            substitute_name: str
            print_name: str
            is_path_relative: bool
            def __init__(self, substitute_name: _Optional[str] = ..., print_name: _Optional[str] = ..., is_path_relative: bool = ...) -> None: ...
        REPARSE_TAG_FIELD_NUMBER: _ClassVar[int]
        SYMLINK_REPARSE_POINT_INFO_FIELD_NUMBER: _ClassVar[int]
        reparse_tag: int
        symlink_reparse_point_info: EntityMetadata.ReparsePointInfo.SymlinkReparsePointInfo
        def __init__(self, reparse_tag: _Optional[int] = ..., symlink_reparse_point_info: _Optional[_Union[EntityMetadata.ReparsePointInfo.SymlinkReparsePointInfo, _Mapping]] = ...) -> None: ...
    ROOT_DIR_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    GID_FIELD_NUMBER: _ClassVar[int]
    CHANGE_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    MODIFY_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    ACCESS_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    ALLOCATION_SIZE_FIELD_NUMBER: _ClassVar[int]
    INODE_ID_FIELD_NUMBER: _ClassVar[int]
    NUM_HARDLINKS_FIELD_NUMBER: _ClassVar[int]
    FIRST_PATH_TO_HARDLINK_FIELD_NUMBER: _ClassVar[int]
    SYMLINK_TARGET_FIELD_NUMBER: _ClassVar[int]
    SYMLINK_FLAGS_FIELD_NUMBER: _ClassVar[int]
    REPARSE_POINT_INFO_FIELD_NUMBER: _ClassVar[int]
    EXTENDED_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    root_dir: bytes
    path: bytes
    type: EntityMetadata.EntityType
    attributes: int
    uid: int
    gid: int
    change_time_usecs: int
    modify_time_usecs: int
    create_time_usecs: int
    access_time_usecs: int
    size: int
    allocation_size: int
    inode_id: int
    num_hardlinks: int
    first_path_to_hardlink: bytes
    symlink_target: bytes
    symlink_flags: int
    reparse_point_info: EntityMetadata.ReparsePointInfo
    extended_attributes: _containers.RepeatedCompositeFieldContainer[ExtendedAttribute]
    error: _error_pb2.ErrorProto
    def __init__(self, root_dir: _Optional[bytes] = ..., path: _Optional[bytes] = ..., type: _Optional[_Union[EntityMetadata.EntityType, str]] = ..., attributes: _Optional[int] = ..., uid: _Optional[int] = ..., gid: _Optional[int] = ..., change_time_usecs: _Optional[int] = ..., modify_time_usecs: _Optional[int] = ..., create_time_usecs: _Optional[int] = ..., access_time_usecs: _Optional[int] = ..., size: _Optional[int] = ..., allocation_size: _Optional[int] = ..., inode_id: _Optional[int] = ..., num_hardlinks: _Optional[int] = ..., first_path_to_hardlink: _Optional[bytes] = ..., symlink_target: _Optional[bytes] = ..., symlink_flags: _Optional[int] = ..., reparse_point_info: _Optional[_Union[EntityMetadata.ReparsePointInfo, _Mapping]] = ..., extended_attributes: _Optional[_Iterable[_Union[ExtendedAttribute, _Mapping]]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class SmbProxyGetRootMetadataArg(_message.Message):
    __slots__ = ("header", "path")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    header: SmbProxyBaseArg
    path: bytes
    def __init__(self, header: _Optional[_Union[SmbProxyBaseArg, _Mapping]] = ..., path: _Optional[bytes] = ...) -> None: ...

class SmbProxyGetRootMetadataResult(_message.Message):
    __slots__ = ("error", "metadata")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    metadata: EntityMetadata
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., metadata: _Optional[_Union[EntityMetadata, _Mapping]] = ...) -> None: ...

class SmbProxyGetNfsComplementMetadataArg(_message.Message):
    __slots__ = ("header", "paths")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    PATHS_FIELD_NUMBER: _ClassVar[int]
    header: SmbProxyBaseArg
    paths: _containers.RepeatedScalarFieldContainer[bytes]
    def __init__(self, header: _Optional[_Union[SmbProxyBaseArg, _Mapping]] = ..., paths: _Optional[_Iterable[bytes]] = ...) -> None: ...

class SmbProxyGetNfsComplementMetadataResult(_message.Message):
    __slots__ = ("error", "nfs_complement_metadata")
    class NfsComplementEntityMetadata(_message.Message):
        __slots__ = ("error", "create_time_usecs", "attributes", "extended_attributes")
        ERROR_FIELD_NUMBER: _ClassVar[int]
        CREATE_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
        ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
        EXTENDED_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
        error: _error_pb2.ErrorProto
        create_time_usecs: int
        attributes: int
        extended_attributes: _containers.RepeatedCompositeFieldContainer[ExtendedAttribute]
        def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., create_time_usecs: _Optional[int] = ..., attributes: _Optional[int] = ..., extended_attributes: _Optional[_Iterable[_Union[ExtendedAttribute, _Mapping]]] = ...) -> None: ...
    ERROR_FIELD_NUMBER: _ClassVar[int]
    NFS_COMPLEMENT_METADATA_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    nfs_complement_metadata: _containers.RepeatedCompositeFieldContainer[SmbProxyGetNfsComplementMetadataResult.NfsComplementEntityMetadata]
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., nfs_complement_metadata: _Optional[_Iterable[_Union[SmbProxyGetNfsComplementMetadataResult.NfsComplementEntityMetadata, _Mapping]]] = ...) -> None: ...

class SmbProxyFetchChildrenMetadataArg(_message.Message):
    __slots__ = ("header", "path", "cookie", "fetch_symlink_target", "fetch_acls")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    COOKIE_FIELD_NUMBER: _ClassVar[int]
    FETCH_SYMLINK_TARGET_FIELD_NUMBER: _ClassVar[int]
    FETCH_ACLS_FIELD_NUMBER: _ClassVar[int]
    header: SmbProxyBaseArg
    path: bytes
    cookie: bytes
    fetch_symlink_target: bool
    fetch_acls: bool
    def __init__(self, header: _Optional[_Union[SmbProxyBaseArg, _Mapping]] = ..., path: _Optional[bytes] = ..., cookie: _Optional[bytes] = ..., fetch_symlink_target: bool = ..., fetch_acls: bool = ...) -> None: ...

class SmbProxyFetchChildrenMetadataResult(_message.Message):
    __slots__ = ("error", "parent_dir_error", "children_metadata", "cookie")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    PARENT_DIR_ERROR_FIELD_NUMBER: _ClassVar[int]
    CHILDREN_METADATA_FIELD_NUMBER: _ClassVar[int]
    COOKIE_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    parent_dir_error: _error_pb2.ErrorProto
    children_metadata: _containers.RepeatedCompositeFieldContainer[EntityMetadata]
    cookie: bytes
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., parent_dir_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., children_metadata: _Optional[_Iterable[_Union[EntityMetadata, _Mapping]]] = ..., cookie: _Optional[bytes] = ...) -> None: ...

class SmbProxyConnectionCookie(_message.Message):
    __slots__ = ("creation_time_usecs", "children_fetched")
    CREATION_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    CHILDREN_FETCHED_FIELD_NUMBER: _ClassVar[int]
    creation_time_usecs: int
    children_fetched: int
    def __init__(self, creation_time_usecs: _Optional[int] = ..., children_fetched: _Optional[int] = ...) -> None: ...

class SmbProxyFetchFileDataArg(_message.Message):
    __slots__ = ("header", "file_path", "offset", "size", "cache_handle")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    CACHE_HANDLE_FIELD_NUMBER: _ClassVar[int]
    header: SmbProxyBaseArg
    file_path: bytes
    offset: int
    size: int
    cache_handle: bool
    def __init__(self, header: _Optional[_Union[SmbProxyBaseArg, _Mapping]] = ..., file_path: _Optional[bytes] = ..., offset: _Optional[int] = ..., size: _Optional[int] = ..., cache_handle: bool = ...) -> None: ...

class SmbProxyFetchFileDataResult(_message.Message):
    __slots__ = ("error", "data")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    data: bytes
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., data: _Optional[bytes] = ...) -> None: ...

class SmbProxyWriteFileDataArg(_message.Message):
    __slots__ = ("header", "file_path", "offset", "size", "cache_handle", "data", "is_stubbed")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    CACHE_HANDLE_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    IS_STUBBED_FIELD_NUMBER: _ClassVar[int]
    header: SmbProxyBaseArg
    file_path: bytes
    offset: int
    size: int
    cache_handle: bool
    data: bytes
    is_stubbed: bool
    def __init__(self, header: _Optional[_Union[SmbProxyBaseArg, _Mapping]] = ..., file_path: _Optional[bytes] = ..., offset: _Optional[int] = ..., size: _Optional[int] = ..., cache_handle: bool = ..., data: _Optional[bytes] = ..., is_stubbed: bool = ...) -> None: ...

class SmbProxyWriteFileDataResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class SmbProxyPurgeTaskArg(_message.Message):
    __slots__ = ("header", "task_key")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    TASK_KEY_FIELD_NUMBER: _ClassVar[int]
    header: SmbProxyBaseArg
    task_key: str
    def __init__(self, header: _Optional[_Union[SmbProxyBaseArg, _Mapping]] = ..., task_key: _Optional[str] = ...) -> None: ...

class SmbProxyPurgeTaskResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class SmbProxyCreateEntityArg(_message.Message):
    __slots__ = ("header", "type", "path")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    header: SmbProxyBaseArg
    type: EntityType
    path: bytes
    def __init__(self, header: _Optional[_Union[SmbProxyBaseArg, _Mapping]] = ..., type: _Optional[_Union[EntityType, str]] = ..., path: _Optional[bytes] = ...) -> None: ...

class SmbProxyCreateEntityResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class SmbProxyDeleteEntityArg(_message.Message):
    __slots__ = ("header", "type", "path", "exclusive_access")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    EXCLUSIVE_ACCESS_FIELD_NUMBER: _ClassVar[int]
    header: SmbProxyBaseArg
    type: EntityType
    path: bytes
    exclusive_access: bool
    def __init__(self, header: _Optional[_Union[SmbProxyBaseArg, _Mapping]] = ..., type: _Optional[_Union[EntityType, str]] = ..., path: _Optional[bytes] = ..., exclusive_access: bool = ...) -> None: ...

class SmbProxyDeleteEntityResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class SmbProxyCreateRestoreFilesArg(_message.Message):
    __slots__ = ("header", "alternate_location_path", "entity_metadata_vec", "create_parent_dirs", "overwrite_existing_tmp", "hardlink_tmp_dir_sharding_width", "nas_uptier_task")
    class Entity(_message.Message):
        __slots__ = ("existing_entity_md", "restore_entity_md", "restore_file_handle", "existing_file_handle")
        EXISTING_ENTITY_MD_FIELD_NUMBER: _ClassVar[int]
        RESTORE_ENTITY_MD_FIELD_NUMBER: _ClassVar[int]
        RESTORE_FILE_HANDLE_FIELD_NUMBER: _ClassVar[int]
        EXISTING_FILE_HANDLE_FIELD_NUMBER: _ClassVar[int]
        existing_entity_md: EntityMetadata
        restore_entity_md: EntityMetadata
        restore_file_handle: RestoreFileHandle
        existing_file_handle: RestoreFileHandle
        def __init__(self, existing_entity_md: _Optional[_Union[EntityMetadata, _Mapping]] = ..., restore_entity_md: _Optional[_Union[EntityMetadata, _Mapping]] = ..., restore_file_handle: _Optional[_Union[RestoreFileHandle, _Mapping]] = ..., existing_file_handle: _Optional[_Union[RestoreFileHandle, _Mapping]] = ...) -> None: ...
    HEADER_FIELD_NUMBER: _ClassVar[int]
    ALTERNATE_LOCATION_PATH_FIELD_NUMBER: _ClassVar[int]
    ENTITY_METADATA_VEC_FIELD_NUMBER: _ClassVar[int]
    CREATE_PARENT_DIRS_FIELD_NUMBER: _ClassVar[int]
    OVERWRITE_EXISTING_TMP_FIELD_NUMBER: _ClassVar[int]
    HARDLINK_TMP_DIR_SHARDING_WIDTH_FIELD_NUMBER: _ClassVar[int]
    NAS_UPTIER_TASK_FIELD_NUMBER: _ClassVar[int]
    header: SmbProxyBaseArg
    alternate_location_path: bytes
    entity_metadata_vec: _containers.RepeatedCompositeFieldContainer[SmbProxyCreateRestoreFilesArg.Entity]
    create_parent_dirs: bool
    overwrite_existing_tmp: bool
    hardlink_tmp_dir_sharding_width: int
    nas_uptier_task: bool
    def __init__(self, header: _Optional[_Union[SmbProxyBaseArg, _Mapping]] = ..., alternate_location_path: _Optional[bytes] = ..., entity_metadata_vec: _Optional[_Iterable[_Union[SmbProxyCreateRestoreFilesArg.Entity, _Mapping]]] = ..., create_parent_dirs: bool = ..., overwrite_existing_tmp: bool = ..., hardlink_tmp_dir_sharding_width: _Optional[int] = ..., nas_uptier_task: bool = ...) -> None: ...

class SmbProxyCreateRestoreFilesResult(_message.Message):
    __slots__ = ("error", "entity_result_vec")
    class EntityResult(_message.Message):
        __slots__ = ("error",)
        ERROR_FIELD_NUMBER: _ClassVar[int]
        error: _error_pb2.ErrorProto
        def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ENTITY_RESULT_VEC_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    entity_result_vec: _containers.RepeatedCompositeFieldContainer[SmbProxyCreateRestoreFilesResult.EntityResult]
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., entity_result_vec: _Optional[_Iterable[_Union[SmbProxyCreateRestoreFilesResult.EntityResult, _Mapping]]] = ...) -> None: ...

class RestoreFileHandle(_message.Message):
    __slots__ = ("entity_metadata", "file_path", "tmp_file_path")
    ENTITY_METADATA_FIELD_NUMBER: _ClassVar[int]
    FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    TMP_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    entity_metadata: EntityMetadata
    file_path: bytes
    tmp_file_path: bytes
    def __init__(self, entity_metadata: _Optional[_Union[EntityMetadata, _Mapping]] = ..., file_path: _Optional[bytes] = ..., tmp_file_path: _Optional[bytes] = ...) -> None: ...

class SmbProxyWriteFilesDataArg(_message.Message):
    __slots__ = ("header", "alternate_location_path", "entities_vec")
    class Entity(_message.Message):
        __slots__ = ("restore_file_handle", "offset", "data")
        RESTORE_FILE_HANDLE_FIELD_NUMBER: _ClassVar[int]
        OFFSET_FIELD_NUMBER: _ClassVar[int]
        DATA_FIELD_NUMBER: _ClassVar[int]
        restore_file_handle: RestoreFileHandle
        offset: int
        data: bytes
        def __init__(self, restore_file_handle: _Optional[_Union[RestoreFileHandle, _Mapping]] = ..., offset: _Optional[int] = ..., data: _Optional[bytes] = ...) -> None: ...
    HEADER_FIELD_NUMBER: _ClassVar[int]
    ALTERNATE_LOCATION_PATH_FIELD_NUMBER: _ClassVar[int]
    ENTITIES_VEC_FIELD_NUMBER: _ClassVar[int]
    header: SmbProxyBaseArg
    alternate_location_path: bytes
    entities_vec: _containers.RepeatedCompositeFieldContainer[SmbProxyWriteFilesDataArg.Entity]
    def __init__(self, header: _Optional[_Union[SmbProxyBaseArg, _Mapping]] = ..., alternate_location_path: _Optional[bytes] = ..., entities_vec: _Optional[_Iterable[_Union[SmbProxyWriteFilesDataArg.Entity, _Mapping]]] = ...) -> None: ...

class SmbProxyWriteFilesDataResult(_message.Message):
    __slots__ = ("error", "error_vec")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ERROR_VEC_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    error_vec: _containers.RepeatedCompositeFieldContainer[_error_pb2.ErrorProto]
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., error_vec: _Optional[_Iterable[_Union[_error_pb2.ErrorProto, _Mapping]]] = ...) -> None: ...

class SmbProxyFinalizeRestoreFilesArg(_message.Message):
    __slots__ = ("header", "alternate_location_path", "entities_vec", "nas_uptier_task", "nas_uptier_symlink_prefix", "purge_all_file_handles_on_finalize")
    class Entity(_message.Message):
        __slots__ = ("should_commit", "restore_file_handle")
        SHOULD_COMMIT_FIELD_NUMBER: _ClassVar[int]
        RESTORE_FILE_HANDLE_FIELD_NUMBER: _ClassVar[int]
        should_commit: bool
        restore_file_handle: RestoreFileHandle
        def __init__(self, should_commit: bool = ..., restore_file_handle: _Optional[_Union[RestoreFileHandle, _Mapping]] = ...) -> None: ...
    HEADER_FIELD_NUMBER: _ClassVar[int]
    ALTERNATE_LOCATION_PATH_FIELD_NUMBER: _ClassVar[int]
    ENTITIES_VEC_FIELD_NUMBER: _ClassVar[int]
    NAS_UPTIER_TASK_FIELD_NUMBER: _ClassVar[int]
    NAS_UPTIER_SYMLINK_PREFIX_FIELD_NUMBER: _ClassVar[int]
    PURGE_ALL_FILE_HANDLES_ON_FINALIZE_FIELD_NUMBER: _ClassVar[int]
    header: SmbProxyBaseArg
    alternate_location_path: bytes
    entities_vec: _containers.RepeatedCompositeFieldContainer[SmbProxyFinalizeRestoreFilesArg.Entity]
    nas_uptier_task: bool
    nas_uptier_symlink_prefix: str
    purge_all_file_handles_on_finalize: bool
    def __init__(self, header: _Optional[_Union[SmbProxyBaseArg, _Mapping]] = ..., alternate_location_path: _Optional[bytes] = ..., entities_vec: _Optional[_Iterable[_Union[SmbProxyFinalizeRestoreFilesArg.Entity, _Mapping]]] = ..., nas_uptier_task: bool = ..., nas_uptier_symlink_prefix: _Optional[str] = ..., purge_all_file_handles_on_finalize: bool = ...) -> None: ...

class SmbProxyFinalizeRestoreFilesResult(_message.Message):
    __slots__ = ("error", "error_vec")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ERROR_VEC_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    error_vec: _containers.RepeatedCompositeFieldContainer[_error_pb2.ErrorProto]
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., error_vec: _Optional[_Iterable[_Union[_error_pb2.ErrorProto, _Mapping]]] = ...) -> None: ...

class SmbProxyCreateSymlinkArg(_message.Message):
    __slots__ = ("header", "path", "target_path", "delete_entity", "entity_type")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    TARGET_PATH_FIELD_NUMBER: _ClassVar[int]
    DELETE_ENTITY_FIELD_NUMBER: _ClassVar[int]
    ENTITY_TYPE_FIELD_NUMBER: _ClassVar[int]
    header: SmbProxyBaseArg
    path: bytes
    target_path: bytes
    delete_entity: bool
    entity_type: EntityType
    def __init__(self, header: _Optional[_Union[SmbProxyBaseArg, _Mapping]] = ..., path: _Optional[bytes] = ..., target_path: _Optional[bytes] = ..., delete_entity: bool = ..., entity_type: _Optional[_Union[EntityType, str]] = ...) -> None: ...

class SmbProxyCreateSymlinkResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class SmbProxyRenameEntityArg(_message.Message):
    __slots__ = ("header", "existing_path", "target_path", "entity_type", "replace_if_exists")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    EXISTING_PATH_FIELD_NUMBER: _ClassVar[int]
    TARGET_PATH_FIELD_NUMBER: _ClassVar[int]
    ENTITY_TYPE_FIELD_NUMBER: _ClassVar[int]
    REPLACE_IF_EXISTS_FIELD_NUMBER: _ClassVar[int]
    header: SmbProxyBaseArg
    existing_path: bytes
    target_path: bytes
    entity_type: EntityType
    replace_if_exists: bool
    def __init__(self, header: _Optional[_Union[SmbProxyBaseArg, _Mapping]] = ..., existing_path: _Optional[bytes] = ..., target_path: _Optional[bytes] = ..., entity_type: _Optional[_Union[EntityType, str]] = ..., replace_if_exists: bool = ...) -> None: ...

class SmbProxyRenameEntityResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class SmbProxyCreateHardlinkArg(_message.Message):
    __slots__ = ("header", "path", "target_path")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    TARGET_PATH_FIELD_NUMBER: _ClassVar[int]
    header: SmbProxyBaseArg
    path: bytes
    target_path: bytes
    def __init__(self, header: _Optional[_Union[SmbProxyBaseArg, _Mapping]] = ..., path: _Optional[bytes] = ..., target_path: _Optional[bytes] = ...) -> None: ...

class SmbProxyCreateHardlinkResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class SmbProxyVerifyShareArg(_message.Message):
    __slots__ = ("header",)
    HEADER_FIELD_NUMBER: _ClassVar[int]
    header: SmbProxyBaseArg
    def __init__(self, header: _Optional[_Union[SmbProxyBaseArg, _Mapping]] = ...) -> None: ...

class SmbProxyVerifyShareResult(_message.Message):
    __slots__ = ("error", "first_working_ip", "logical_size_bytes", "available_size_bytes", "total_allocation_units", "caller_available_allocation_units", "actual_available_allocation_units", "sectors_per_allocation_unit", "bytes_per_sector")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    FIRST_WORKING_IP_FIELD_NUMBER: _ClassVar[int]
    LOGICAL_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    AVAILABLE_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    TOTAL_ALLOCATION_UNITS_FIELD_NUMBER: _ClassVar[int]
    CALLER_AVAILABLE_ALLOCATION_UNITS_FIELD_NUMBER: _ClassVar[int]
    ACTUAL_AVAILABLE_ALLOCATION_UNITS_FIELD_NUMBER: _ClassVar[int]
    SECTORS_PER_ALLOCATION_UNIT_FIELD_NUMBER: _ClassVar[int]
    BYTES_PER_SECTOR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    first_working_ip: str
    logical_size_bytes: int
    available_size_bytes: int
    total_allocation_units: int
    caller_available_allocation_units: int
    actual_available_allocation_units: int
    sectors_per_allocation_unit: int
    bytes_per_sector: int
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., first_working_ip: _Optional[str] = ..., logical_size_bytes: _Optional[int] = ..., available_size_bytes: _Optional[int] = ..., total_allocation_units: _Optional[int] = ..., caller_available_allocation_units: _Optional[int] = ..., actual_available_allocation_units: _Optional[int] = ..., sectors_per_allocation_unit: _Optional[int] = ..., bytes_per_sector: _Optional[int] = ...) -> None: ...

class SmbProxyUpdateAdUserPasswordArg(_message.Message):
    __slots__ = ("domain_controller", "user_name", "old_password", "new_password")
    DOMAIN_CONTROLLER_FIELD_NUMBER: _ClassVar[int]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    OLD_PASSWORD_FIELD_NUMBER: _ClassVar[int]
    NEW_PASSWORD_FIELD_NUMBER: _ClassVar[int]
    domain_controller: str
    user_name: str
    old_password: str
    new_password: str
    def __init__(self, domain_controller: _Optional[str] = ..., user_name: _Optional[str] = ..., old_password: _Optional[str] = ..., new_password: _Optional[str] = ...) -> None: ...

class SmbProxyUpdateAdUserPasswordResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class SmbProxySetEntityMetadataArg(_message.Message):
    __slots__ = ("header", "metadata", "set_file_info", "set_acl_info")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    SET_FILE_INFO_FIELD_NUMBER: _ClassVar[int]
    SET_ACL_INFO_FIELD_NUMBER: _ClassVar[int]
    header: SmbProxyBaseArg
    metadata: EntityMetadata
    set_file_info: bool
    set_acl_info: bool
    def __init__(self, header: _Optional[_Union[SmbProxyBaseArg, _Mapping]] = ..., metadata: _Optional[_Union[EntityMetadata, _Mapping]] = ..., set_file_info: bool = ..., set_acl_info: bool = ...) -> None: ...

class SmbProxySetEntityMetadataResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class SmbProxyThrottleResourceUsageArg(_message.Message):
    __slots__ = ("source_utilization_map", "entity_to_source_map")
    class CurrentResourceInfo(_message.Message):
        __slots__ = ("cpu_usage_pct", "cpu_fetched_time_usecs")
        CPU_USAGE_PCT_FIELD_NUMBER: _ClassVar[int]
        CPU_FETCHED_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
        cpu_usage_pct: int
        cpu_fetched_time_usecs: int
        def __init__(self, cpu_usage_pct: _Optional[int] = ..., cpu_fetched_time_usecs: _Optional[int] = ...) -> None: ...
    class SourceUtilizationMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: SmbProxyThrottleResourceUsageArg.CurrentResourceInfo
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[SmbProxyThrottleResourceUsageArg.CurrentResourceInfo, _Mapping]] = ...) -> None: ...
    class EntityToSourceMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: str
        def __init__(self, key: _Optional[int] = ..., value: _Optional[str] = ...) -> None: ...
    SOURCE_UTILIZATION_MAP_FIELD_NUMBER: _ClassVar[int]
    ENTITY_TO_SOURCE_MAP_FIELD_NUMBER: _ClassVar[int]
    source_utilization_map: _containers.MessageMap[str, SmbProxyThrottleResourceUsageArg.CurrentResourceInfo]
    entity_to_source_map: _containers.ScalarMap[int, str]
    def __init__(self, source_utilization_map: _Optional[_Mapping[str, SmbProxyThrottleResourceUsageArg.CurrentResourceInfo]] = ..., entity_to_source_map: _Optional[_Mapping[int, str]] = ...) -> None: ...

class SmbProxyThrottleResourceUsageResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class TaskType(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kMdRegular: _ClassVar[TaskType.Type]
        kMdStreamer: _ClassVar[TaskType.Type]
        kDataTransfer: _ClassVar[TaskType.Type]
        kOther: _ClassVar[TaskType.Type]
        kQStarAdapter: _ClassVar[TaskType.Type]
    kMdRegular: TaskType.Type
    kMdStreamer: TaskType.Type
    kDataTransfer: TaskType.Type
    kOther: TaskType.Type
    kQStarAdapter: TaskType.Type
    def __init__(self) -> None: ...
