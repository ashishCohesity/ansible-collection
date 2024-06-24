from bridge.snap_fs import dedup_range_pb2 as _dedup_range_pb2
from magneto.base import enums_pb2 as _enums_pb2
from magneto.base import magneto_pb2 as _magneto_pb2
from magneto.base import env_params_pb2 as _env_params_pb2
from magneto.connectors.vmware import vmware_common_args_pb2 as _vmware_common_args_pb2
from open_util.net import protorpc_pb2 as _protorpc_pb2
from magneto.directory_walker import directory_walker_pb2 as _directory_walker_pb2
from util.storage import error_pb2 as _error_pb2
from yoda.base import volume_info_pb2 as _volume_info_pb2
from util.base import op_clock_pb2 as _op_clock_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MetadataFetcherParams(_message.Message):
    __slots__ = ("root_dir", "populate_root_dir", "fetch_extended_attributes", "continue_on_listxattr_error", "skip_getxattr_vec", "continue_on_error", "force_usec_ts_resolution", "additional_ea_name_vec", "protocol", "ignore_hardlinks", "alternate_full_path", "max_num_concurrent_dir_fetch", "max_num_concurrent_metadata_fetch_per_dir", "filesystem_type", "symlink_follow_nas_target")
    ROOT_DIR_FIELD_NUMBER: _ClassVar[int]
    POPULATE_ROOT_DIR_FIELD_NUMBER: _ClassVar[int]
    FETCH_EXTENDED_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    CONTINUE_ON_LISTXATTR_ERROR_FIELD_NUMBER: _ClassVar[int]
    SKIP_GETXATTR_VEC_FIELD_NUMBER: _ClassVar[int]
    CONTINUE_ON_ERROR_FIELD_NUMBER: _ClassVar[int]
    FORCE_USEC_TS_RESOLUTION_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_EA_NAME_VEC_FIELD_NUMBER: _ClassVar[int]
    PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    IGNORE_HARDLINKS_FIELD_NUMBER: _ClassVar[int]
    ALTERNATE_FULL_PATH_FIELD_NUMBER: _ClassVar[int]
    MAX_NUM_CONCURRENT_DIR_FETCH_FIELD_NUMBER: _ClassVar[int]
    MAX_NUM_CONCURRENT_METADATA_FETCH_PER_DIR_FIELD_NUMBER: _ClassVar[int]
    FILESYSTEM_TYPE_FIELD_NUMBER: _ClassVar[int]
    SYMLINK_FOLLOW_NAS_TARGET_FIELD_NUMBER: _ClassVar[int]
    root_dir: str
    populate_root_dir: bool
    fetch_extended_attributes: bool
    continue_on_listxattr_error: bool
    skip_getxattr_vec: _containers.RepeatedScalarFieldContainer[str]
    continue_on_error: bool
    force_usec_ts_resolution: bool
    additional_ea_name_vec: _containers.RepeatedScalarFieldContainer[str]
    protocol: _enums_pb2.NasProtocol.Type
    ignore_hardlinks: bool
    alternate_full_path: str
    max_num_concurrent_dir_fetch: int
    max_num_concurrent_metadata_fetch_per_dir: int
    filesystem_type: str
    symlink_follow_nas_target: bool
    def __init__(self, root_dir: _Optional[str] = ..., populate_root_dir: bool = ..., fetch_extended_attributes: bool = ..., continue_on_listxattr_error: bool = ..., skip_getxattr_vec: _Optional[_Iterable[str]] = ..., continue_on_error: bool = ..., force_usec_ts_resolution: bool = ..., additional_ea_name_vec: _Optional[_Iterable[str]] = ..., protocol: _Optional[_Union[_enums_pb2.NasProtocol.Type, str]] = ..., ignore_hardlinks: bool = ..., alternate_full_path: _Optional[str] = ..., max_num_concurrent_dir_fetch: _Optional[int] = ..., max_num_concurrent_metadata_fetch_per_dir: _Optional[int] = ..., filesystem_type: _Optional[str] = ..., symlink_follow_nas_target: bool = ...) -> None: ...

class ProxyBaseArg(_message.Message):
    __slots__ = ("task_id", "subtask_id", "work_unit_idx", "entity_key", "mountpoint_identifier", "protocol", "servers", "nas_path", "target_path", "use_soft_mount", "use_read_only", "username", "password", "domain_name", "connection_info", "nfs_encryption_enabled", "bridge_proxy_address")
    class ConnectionInfo(_message.Message):
        __slots__ = ("connector_params", "guest_operation_params", "host_name")
        CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
        GUEST_OPERATION_PARAMS_FIELD_NUMBER: _ClassVar[int]
        HOST_NAME_FIELD_NUMBER: _ClassVar[int]
        connector_params: _magneto_pb2.ConnectorParams
        guest_operation_params: _vmware_common_args_pb2.GuestOperationArg
        host_name: str
        def __init__(self, connector_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ..., guest_operation_params: _Optional[_Union[_vmware_common_args_pb2.GuestOperationArg, _Mapping]] = ..., host_name: _Optional[str] = ...) -> None: ...
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    SUBTASK_ID_FIELD_NUMBER: _ClassVar[int]
    WORK_UNIT_IDX_FIELD_NUMBER: _ClassVar[int]
    ENTITY_KEY_FIELD_NUMBER: _ClassVar[int]
    MOUNTPOINT_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    SERVERS_FIELD_NUMBER: _ClassVar[int]
    NAS_PATH_FIELD_NUMBER: _ClassVar[int]
    TARGET_PATH_FIELD_NUMBER: _ClassVar[int]
    USE_SOFT_MOUNT_FIELD_NUMBER: _ClassVar[int]
    USE_READ_ONLY_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_INFO_FIELD_NUMBER: _ClassVar[int]
    NFS_ENCRYPTION_ENABLED_FIELD_NUMBER: _ClassVar[int]
    BRIDGE_PROXY_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    task_id: int
    subtask_id: int
    work_unit_idx: int
    entity_key: str
    mountpoint_identifier: str
    protocol: _enums_pb2.NasProtocol.Type
    servers: _containers.RepeatedScalarFieldContainer[str]
    nas_path: str
    target_path: str
    use_soft_mount: bool
    use_read_only: bool
    username: str
    password: str
    domain_name: str
    connection_info: ProxyBaseArg.ConnectionInfo
    nfs_encryption_enabled: bool
    bridge_proxy_address: str
    def __init__(self, task_id: _Optional[int] = ..., subtask_id: _Optional[int] = ..., work_unit_idx: _Optional[int] = ..., entity_key: _Optional[str] = ..., mountpoint_identifier: _Optional[str] = ..., protocol: _Optional[_Union[_enums_pb2.NasProtocol.Type, str]] = ..., servers: _Optional[_Iterable[str]] = ..., nas_path: _Optional[str] = ..., target_path: _Optional[str] = ..., use_soft_mount: bool = ..., use_read_only: bool = ..., username: _Optional[str] = ..., password: _Optional[str] = ..., domain_name: _Optional[str] = ..., connection_info: _Optional[_Union[ProxyBaseArg.ConnectionInfo, _Mapping]] = ..., nfs_encryption_enabled: bool = ..., bridge_proxy_address: _Optional[str] = ...) -> None: ...

class GetRootMetadataArg(_message.Message):
    __slots__ = ("proxy_header", "base_arg", "task_key", "fetcher_params", "path", "protocol", "nfs_root_dir_path", "smb_relative_path", "entity_id", "volume_mount_key", "rpc_stats")
    PROXY_HEADER_FIELD_NUMBER: _ClassVar[int]
    BASE_ARG_FIELD_NUMBER: _ClassVar[int]
    TASK_KEY_FIELD_NUMBER: _ClassVar[int]
    FETCHER_PARAMS_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    NFS_ROOT_DIR_PATH_FIELD_NUMBER: _ClassVar[int]
    SMB_RELATIVE_PATH_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    VOLUME_MOUNT_KEY_FIELD_NUMBER: _ClassVar[int]
    RPC_STATS_FIELD_NUMBER: _ClassVar[int]
    proxy_header: bytes
    base_arg: ProxyBaseArg
    task_key: str
    fetcher_params: MetadataFetcherParams
    path: str
    protocol: _enums_pb2.NasProtocol.Type
    nfs_root_dir_path: str
    smb_relative_path: str
    entity_id: int
    volume_mount_key: str
    rpc_stats: RpcStats
    def __init__(self, proxy_header: _Optional[bytes] = ..., base_arg: _Optional[_Union[ProxyBaseArg, _Mapping]] = ..., task_key: _Optional[str] = ..., fetcher_params: _Optional[_Union[MetadataFetcherParams, _Mapping]] = ..., path: _Optional[str] = ..., protocol: _Optional[_Union[_enums_pb2.NasProtocol.Type, str]] = ..., nfs_root_dir_path: _Optional[str] = ..., smb_relative_path: _Optional[str] = ..., entity_id: _Optional[int] = ..., volume_mount_key: _Optional[str] = ..., rpc_stats: _Optional[_Union[RpcStats, _Mapping]] = ...) -> None: ...

class GetRootMetadataResult(_message.Message):
    __slots__ = ("error", "metadata", "rpc_stats")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    RPC_STATS_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    metadata: _directory_walker_pb2.EntityMetadata
    rpc_stats: RpcStats
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., metadata: _Optional[_Union[_directory_walker_pb2.EntityMetadata, _Mapping]] = ..., rpc_stats: _Optional[_Union[RpcStats, _Mapping]] = ...) -> None: ...

class FetchChildrenMetadataArg(_message.Message):
    __slots__ = ("proxy_header", "base_arg", "task_key", "fetcher_params", "metadata", "start_child_loc", "protocol", "entity_id", "cookie", "file_names_only", "volume_mount_key", "rpc_stats")
    PROXY_HEADER_FIELD_NUMBER: _ClassVar[int]
    BASE_ARG_FIELD_NUMBER: _ClassVar[int]
    TASK_KEY_FIELD_NUMBER: _ClassVar[int]
    FETCHER_PARAMS_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    START_CHILD_LOC_FIELD_NUMBER: _ClassVar[int]
    PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    COOKIE_FIELD_NUMBER: _ClassVar[int]
    FILE_NAMES_ONLY_FIELD_NUMBER: _ClassVar[int]
    VOLUME_MOUNT_KEY_FIELD_NUMBER: _ClassVar[int]
    RPC_STATS_FIELD_NUMBER: _ClassVar[int]
    proxy_header: bytes
    base_arg: ProxyBaseArg
    task_key: str
    fetcher_params: MetadataFetcherParams
    metadata: _directory_walker_pb2.EntityMetadata
    start_child_loc: int
    protocol: _enums_pb2.NasProtocol.Type
    entity_id: int
    cookie: bytes
    file_names_only: bool
    volume_mount_key: str
    rpc_stats: RpcStats
    def __init__(self, proxy_header: _Optional[bytes] = ..., base_arg: _Optional[_Union[ProxyBaseArg, _Mapping]] = ..., task_key: _Optional[str] = ..., fetcher_params: _Optional[_Union[MetadataFetcherParams, _Mapping]] = ..., metadata: _Optional[_Union[_directory_walker_pb2.EntityMetadata, _Mapping]] = ..., start_child_loc: _Optional[int] = ..., protocol: _Optional[_Union[_enums_pb2.NasProtocol.Type, str]] = ..., entity_id: _Optional[int] = ..., cookie: _Optional[bytes] = ..., file_names_only: bool = ..., volume_mount_key: _Optional[str] = ..., rpc_stats: _Optional[_Union[RpcStats, _Mapping]] = ...) -> None: ...

class FetchChildrenMetadataResult(_message.Message):
    __slots__ = ("error", "parent_dir_error", "children_metadata", "next_child_loc", "cookie", "rpc_stats")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    PARENT_DIR_ERROR_FIELD_NUMBER: _ClassVar[int]
    CHILDREN_METADATA_FIELD_NUMBER: _ClassVar[int]
    NEXT_CHILD_LOC_FIELD_NUMBER: _ClassVar[int]
    COOKIE_FIELD_NUMBER: _ClassVar[int]
    RPC_STATS_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    parent_dir_error: _error_pb2.ErrorProto
    children_metadata: _containers.RepeatedCompositeFieldContainer[_directory_walker_pb2.EntityMetadata]
    next_child_loc: int
    cookie: bytes
    rpc_stats: RpcStats
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., parent_dir_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., children_metadata: _Optional[_Iterable[_Union[_directory_walker_pb2.EntityMetadata, _Mapping]]] = ..., next_child_loc: _Optional[int] = ..., cookie: _Optional[bytes] = ..., rpc_stats: _Optional[_Union[RpcStats, _Mapping]] = ...) -> None: ...

class FetchFileDataArg(_message.Message):
    __slots__ = ("proxy_header", "base_arg", "task_key", "file_path", "offset", "size", "cache_handle", "protocol", "entity_id", "restore_from_archived_snapshot", "skip_read", "rpc_stats")
    PROXY_HEADER_FIELD_NUMBER: _ClassVar[int]
    BASE_ARG_FIELD_NUMBER: _ClassVar[int]
    TASK_KEY_FIELD_NUMBER: _ClassVar[int]
    FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    CACHE_HANDLE_FIELD_NUMBER: _ClassVar[int]
    PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    RESTORE_FROM_ARCHIVED_SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    SKIP_READ_FIELD_NUMBER: _ClassVar[int]
    RPC_STATS_FIELD_NUMBER: _ClassVar[int]
    proxy_header: bytes
    base_arg: ProxyBaseArg
    task_key: str
    file_path: str
    offset: int
    size: int
    cache_handle: bool
    protocol: _enums_pb2.NasProtocol.Type
    entity_id: int
    restore_from_archived_snapshot: bool
    skip_read: bool
    rpc_stats: RpcStats
    def __init__(self, proxy_header: _Optional[bytes] = ..., base_arg: _Optional[_Union[ProxyBaseArg, _Mapping]] = ..., task_key: _Optional[str] = ..., file_path: _Optional[str] = ..., offset: _Optional[int] = ..., size: _Optional[int] = ..., cache_handle: bool = ..., protocol: _Optional[_Union[_enums_pb2.NasProtocol.Type, str]] = ..., entity_id: _Optional[int] = ..., restore_from_archived_snapshot: bool = ..., skip_read: bool = ..., rpc_stats: _Optional[_Union[RpcStats, _Mapping]] = ...) -> None: ...

class FetchFileDataResult(_message.Message):
    __slots__ = ("error", "data", "rpc_stats")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    RPC_STATS_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    data: bytes
    rpc_stats: RpcStats
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., data: _Optional[bytes] = ..., rpc_stats: _Optional[_Union[RpcStats, _Mapping]] = ...) -> None: ...

class PurgeFileHandlesArg(_message.Message):
    __slots__ = ("proxy_header", "base_arg", "task_key", "entity_id", "rpc_stats")
    PROXY_HEADER_FIELD_NUMBER: _ClassVar[int]
    BASE_ARG_FIELD_NUMBER: _ClassVar[int]
    TASK_KEY_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    RPC_STATS_FIELD_NUMBER: _ClassVar[int]
    proxy_header: bytes
    base_arg: ProxyBaseArg
    task_key: str
    entity_id: int
    rpc_stats: RpcStats
    def __init__(self, proxy_header: _Optional[bytes] = ..., base_arg: _Optional[_Union[ProxyBaseArg, _Mapping]] = ..., task_key: _Optional[str] = ..., entity_id: _Optional[int] = ..., rpc_stats: _Optional[_Union[RpcStats, _Mapping]] = ...) -> None: ...

class PurgeFileHandlesResult(_message.Message):
    __slots__ = ("error", "rpc_stats")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    RPC_STATS_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    rpc_stats: RpcStats
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., rpc_stats: _Optional[_Union[RpcStats, _Mapping]] = ...) -> None: ...

class CreateRestoreFilesArg(_message.Message):
    __slots__ = ("proxy_header", "base_arg", "task_key", "alternate_location_path", "entity_metadata_vec", "create_parent_dirs", "overwrite_existing_tmp", "hardlink_tmp_dir_sharding_width", "protocol", "nas_uptier_task", "overwrite_existing_file", "preserve_attributes", "entity_id", "rpc_stats")
    class Entity(_message.Message):
        __slots__ = ("existing_entity_md", "restore_entity_md", "restore_file_handle", "existing_file_handle")
        EXISTING_ENTITY_MD_FIELD_NUMBER: _ClassVar[int]
        RESTORE_ENTITY_MD_FIELD_NUMBER: _ClassVar[int]
        RESTORE_FILE_HANDLE_FIELD_NUMBER: _ClassVar[int]
        EXISTING_FILE_HANDLE_FIELD_NUMBER: _ClassVar[int]
        existing_entity_md: _directory_walker_pb2.EntityMetadata
        restore_entity_md: _directory_walker_pb2.EntityMetadata
        restore_file_handle: RestoreFileHandle
        existing_file_handle: RestoreFileHandle
        def __init__(self, existing_entity_md: _Optional[_Union[_directory_walker_pb2.EntityMetadata, _Mapping]] = ..., restore_entity_md: _Optional[_Union[_directory_walker_pb2.EntityMetadata, _Mapping]] = ..., restore_file_handle: _Optional[_Union[RestoreFileHandle, _Mapping]] = ..., existing_file_handle: _Optional[_Union[RestoreFileHandle, _Mapping]] = ...) -> None: ...
    PROXY_HEADER_FIELD_NUMBER: _ClassVar[int]
    BASE_ARG_FIELD_NUMBER: _ClassVar[int]
    TASK_KEY_FIELD_NUMBER: _ClassVar[int]
    ALTERNATE_LOCATION_PATH_FIELD_NUMBER: _ClassVar[int]
    ENTITY_METADATA_VEC_FIELD_NUMBER: _ClassVar[int]
    CREATE_PARENT_DIRS_FIELD_NUMBER: _ClassVar[int]
    OVERWRITE_EXISTING_TMP_FIELD_NUMBER: _ClassVar[int]
    HARDLINK_TMP_DIR_SHARDING_WIDTH_FIELD_NUMBER: _ClassVar[int]
    PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    NAS_UPTIER_TASK_FIELD_NUMBER: _ClassVar[int]
    OVERWRITE_EXISTING_FILE_FIELD_NUMBER: _ClassVar[int]
    PRESERVE_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    RPC_STATS_FIELD_NUMBER: _ClassVar[int]
    proxy_header: bytes
    base_arg: ProxyBaseArg
    task_key: str
    alternate_location_path: str
    entity_metadata_vec: _containers.RepeatedCompositeFieldContainer[CreateRestoreFilesArg.Entity]
    create_parent_dirs: bool
    overwrite_existing_tmp: bool
    hardlink_tmp_dir_sharding_width: int
    protocol: _enums_pb2.NasProtocol.Type
    nas_uptier_task: bool
    overwrite_existing_file: bool
    preserve_attributes: bool
    entity_id: int
    rpc_stats: RpcStats
    def __init__(self, proxy_header: _Optional[bytes] = ..., base_arg: _Optional[_Union[ProxyBaseArg, _Mapping]] = ..., task_key: _Optional[str] = ..., alternate_location_path: _Optional[str] = ..., entity_metadata_vec: _Optional[_Iterable[_Union[CreateRestoreFilesArg.Entity, _Mapping]]] = ..., create_parent_dirs: bool = ..., overwrite_existing_tmp: bool = ..., hardlink_tmp_dir_sharding_width: _Optional[int] = ..., protocol: _Optional[_Union[_enums_pb2.NasProtocol.Type, str]] = ..., nas_uptier_task: bool = ..., overwrite_existing_file: bool = ..., preserve_attributes: bool = ..., entity_id: _Optional[int] = ..., rpc_stats: _Optional[_Union[RpcStats, _Mapping]] = ...) -> None: ...

class RestoreFileHandle(_message.Message):
    __slots__ = ("entity_metadata", "file_path", "tmp_file_path", "parallel_restore")
    ENTITY_METADATA_FIELD_NUMBER: _ClassVar[int]
    FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    TMP_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    PARALLEL_RESTORE_FIELD_NUMBER: _ClassVar[int]
    entity_metadata: _directory_walker_pb2.EntityMetadata
    file_path: str
    tmp_file_path: str
    parallel_restore: bool
    def __init__(self, entity_metadata: _Optional[_Union[_directory_walker_pb2.EntityMetadata, _Mapping]] = ..., file_path: _Optional[str] = ..., tmp_file_path: _Optional[str] = ..., parallel_restore: bool = ...) -> None: ...

class CreateRestoreFilesResult(_message.Message):
    __slots__ = ("error", "entity_result_vec", "rpc_stats")
    class EntityResult(_message.Message):
        __slots__ = ("error", "restore_file_handle")
        ERROR_FIELD_NUMBER: _ClassVar[int]
        RESTORE_FILE_HANDLE_FIELD_NUMBER: _ClassVar[int]
        error: _error_pb2.ErrorProto
        restore_file_handle: RestoreFileHandle
        def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., restore_file_handle: _Optional[_Union[RestoreFileHandle, _Mapping]] = ...) -> None: ...
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ENTITY_RESULT_VEC_FIELD_NUMBER: _ClassVar[int]
    RPC_STATS_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    entity_result_vec: _containers.RepeatedCompositeFieldContainer[CreateRestoreFilesResult.EntityResult]
    rpc_stats: RpcStats
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., entity_result_vec: _Optional[_Iterable[_Union[CreateRestoreFilesResult.EntityResult, _Mapping]]] = ..., rpc_stats: _Optional[_Union[RpcStats, _Mapping]] = ...) -> None: ...

class WriteFileDataArg(_message.Message):
    __slots__ = ("proxy_header", "base_arg", "task_key", "file_path", "offset", "size", "cache_handle", "data", "protocol", "is_stubbed", "parallel_restore", "entity_id", "skip_write", "rpc_stats")
    PROXY_HEADER_FIELD_NUMBER: _ClassVar[int]
    BASE_ARG_FIELD_NUMBER: _ClassVar[int]
    TASK_KEY_FIELD_NUMBER: _ClassVar[int]
    FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    CACHE_HANDLE_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    IS_STUBBED_FIELD_NUMBER: _ClassVar[int]
    PARALLEL_RESTORE_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    SKIP_WRITE_FIELD_NUMBER: _ClassVar[int]
    RPC_STATS_FIELD_NUMBER: _ClassVar[int]
    proxy_header: bytes
    base_arg: ProxyBaseArg
    task_key: str
    file_path: str
    offset: int
    size: int
    cache_handle: bool
    data: bytes
    protocol: _enums_pb2.NasProtocol.Type
    is_stubbed: bool
    parallel_restore: bool
    entity_id: int
    skip_write: bool
    rpc_stats: RpcStats
    def __init__(self, proxy_header: _Optional[bytes] = ..., base_arg: _Optional[_Union[ProxyBaseArg, _Mapping]] = ..., task_key: _Optional[str] = ..., file_path: _Optional[str] = ..., offset: _Optional[int] = ..., size: _Optional[int] = ..., cache_handle: bool = ..., data: _Optional[bytes] = ..., protocol: _Optional[_Union[_enums_pb2.NasProtocol.Type, str]] = ..., is_stubbed: bool = ..., parallel_restore: bool = ..., entity_id: _Optional[int] = ..., skip_write: bool = ..., rpc_stats: _Optional[_Union[RpcStats, _Mapping]] = ...) -> None: ...

class WriteFileDataResult(_message.Message):
    __slots__ = ("error", "rpc_stats")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    RPC_STATS_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    rpc_stats: RpcStats
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., rpc_stats: _Optional[_Union[RpcStats, _Mapping]] = ...) -> None: ...

class WriteFilesDataArg(_message.Message):
    __slots__ = ("proxy_header", "base_arg", "task_key", "alternate_location_path", "entities_vec", "protocol", "entity_id", "rpc_stats")
    class Entity(_message.Message):
        __slots__ = ("restore_file_handle", "offset", "data")
        RESTORE_FILE_HANDLE_FIELD_NUMBER: _ClassVar[int]
        OFFSET_FIELD_NUMBER: _ClassVar[int]
        DATA_FIELD_NUMBER: _ClassVar[int]
        restore_file_handle: RestoreFileHandle
        offset: int
        data: bytes
        def __init__(self, restore_file_handle: _Optional[_Union[RestoreFileHandle, _Mapping]] = ..., offset: _Optional[int] = ..., data: _Optional[bytes] = ...) -> None: ...
    PROXY_HEADER_FIELD_NUMBER: _ClassVar[int]
    BASE_ARG_FIELD_NUMBER: _ClassVar[int]
    TASK_KEY_FIELD_NUMBER: _ClassVar[int]
    ALTERNATE_LOCATION_PATH_FIELD_NUMBER: _ClassVar[int]
    ENTITIES_VEC_FIELD_NUMBER: _ClassVar[int]
    PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    RPC_STATS_FIELD_NUMBER: _ClassVar[int]
    proxy_header: bytes
    base_arg: ProxyBaseArg
    task_key: str
    alternate_location_path: str
    entities_vec: _containers.RepeatedCompositeFieldContainer[WriteFilesDataArg.Entity]
    protocol: _enums_pb2.NasProtocol.Type
    entity_id: int
    rpc_stats: RpcStats
    def __init__(self, proxy_header: _Optional[bytes] = ..., base_arg: _Optional[_Union[ProxyBaseArg, _Mapping]] = ..., task_key: _Optional[str] = ..., alternate_location_path: _Optional[str] = ..., entities_vec: _Optional[_Iterable[_Union[WriteFilesDataArg.Entity, _Mapping]]] = ..., protocol: _Optional[_Union[_enums_pb2.NasProtocol.Type, str]] = ..., entity_id: _Optional[int] = ..., rpc_stats: _Optional[_Union[RpcStats, _Mapping]] = ...) -> None: ...

class WriteFilesDataResult(_message.Message):
    __slots__ = ("error", "error_vec", "rpc_stats")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ERROR_VEC_FIELD_NUMBER: _ClassVar[int]
    RPC_STATS_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    error_vec: _containers.RepeatedCompositeFieldContainer[_error_pb2.ErrorProto]
    rpc_stats: RpcStats
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., error_vec: _Optional[_Iterable[_Union[_error_pb2.ErrorProto, _Mapping]]] = ..., rpc_stats: _Optional[_Union[RpcStats, _Mapping]] = ...) -> None: ...

class FinalizeRestoreFilesArg(_message.Message):
    __slots__ = ("proxy_header", "base_arg", "task_key", "alternate_location_path", "entities_vec", "protocol", "nas_uptier_task", "nas_uptier_symlink_prefix", "purge_all_file_handles_on_finalize", "preserve_attributes", "set_attr_only", "entity_id", "restore_entities", "rpc_stats")
    class Entity(_message.Message):
        __slots__ = ("should_commit", "restore_file_handle")
        SHOULD_COMMIT_FIELD_NUMBER: _ClassVar[int]
        RESTORE_FILE_HANDLE_FIELD_NUMBER: _ClassVar[int]
        should_commit: bool
        restore_file_handle: RestoreFileHandle
        def __init__(self, should_commit: bool = ..., restore_file_handle: _Optional[_Union[RestoreFileHandle, _Mapping]] = ...) -> None: ...
    PROXY_HEADER_FIELD_NUMBER: _ClassVar[int]
    BASE_ARG_FIELD_NUMBER: _ClassVar[int]
    TASK_KEY_FIELD_NUMBER: _ClassVar[int]
    ALTERNATE_LOCATION_PATH_FIELD_NUMBER: _ClassVar[int]
    ENTITIES_VEC_FIELD_NUMBER: _ClassVar[int]
    PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    NAS_UPTIER_TASK_FIELD_NUMBER: _ClassVar[int]
    NAS_UPTIER_SYMLINK_PREFIX_FIELD_NUMBER: _ClassVar[int]
    PURGE_ALL_FILE_HANDLES_ON_FINALIZE_FIELD_NUMBER: _ClassVar[int]
    PRESERVE_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    SET_ATTR_ONLY_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    RESTORE_ENTITIES_FIELD_NUMBER: _ClassVar[int]
    RPC_STATS_FIELD_NUMBER: _ClassVar[int]
    proxy_header: bytes
    base_arg: ProxyBaseArg
    task_key: str
    alternate_location_path: str
    entities_vec: _containers.RepeatedCompositeFieldContainer[FinalizeRestoreFilesArg.Entity]
    protocol: _enums_pb2.NasProtocol.Type
    nas_uptier_task: bool
    nas_uptier_symlink_prefix: str
    purge_all_file_handles_on_finalize: bool
    preserve_attributes: bool
    set_attr_only: bool
    entity_id: int
    restore_entities: _magneto_pb2.RestoreFilesPreferences.RestoreEntityType
    rpc_stats: RpcStats
    def __init__(self, proxy_header: _Optional[bytes] = ..., base_arg: _Optional[_Union[ProxyBaseArg, _Mapping]] = ..., task_key: _Optional[str] = ..., alternate_location_path: _Optional[str] = ..., entities_vec: _Optional[_Iterable[_Union[FinalizeRestoreFilesArg.Entity, _Mapping]]] = ..., protocol: _Optional[_Union[_enums_pb2.NasProtocol.Type, str]] = ..., nas_uptier_task: bool = ..., nas_uptier_symlink_prefix: _Optional[str] = ..., purge_all_file_handles_on_finalize: bool = ..., preserve_attributes: bool = ..., set_attr_only: bool = ..., entity_id: _Optional[int] = ..., restore_entities: _Optional[_Union[_magneto_pb2.RestoreFilesPreferences.RestoreEntityType, str]] = ..., rpc_stats: _Optional[_Union[RpcStats, _Mapping]] = ...) -> None: ...

class FinalizeRestoreFilesResult(_message.Message):
    __slots__ = ("error", "error_vec", "rpc_stats")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ERROR_VEC_FIELD_NUMBER: _ClassVar[int]
    RPC_STATS_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    error_vec: _containers.RepeatedCompositeFieldContainer[_error_pb2.ErrorProto]
    rpc_stats: RpcStats
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., error_vec: _Optional[_Iterable[_Union[_error_pb2.ErrorProto, _Mapping]]] = ..., rpc_stats: _Optional[_Union[RpcStats, _Mapping]] = ...) -> None: ...

class DeleteEntityArg(_message.Message):
    __slots__ = ("proxy_header", "base_arg", "task_key", "type", "path", "protocol", "exclusive_access", "entity_id", "rpc_stats")
    PROXY_HEADER_FIELD_NUMBER: _ClassVar[int]
    BASE_ARG_FIELD_NUMBER: _ClassVar[int]
    TASK_KEY_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    EXCLUSIVE_ACCESS_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    RPC_STATS_FIELD_NUMBER: _ClassVar[int]
    proxy_header: bytes
    base_arg: ProxyBaseArg
    task_key: str
    type: _directory_walker_pb2.EntityMetadata.EntityType
    path: str
    protocol: _enums_pb2.NasProtocol.Type
    exclusive_access: bool
    entity_id: int
    rpc_stats: RpcStats
    def __init__(self, proxy_header: _Optional[bytes] = ..., base_arg: _Optional[_Union[ProxyBaseArg, _Mapping]] = ..., task_key: _Optional[str] = ..., type: _Optional[_Union[_directory_walker_pb2.EntityMetadata.EntityType, str]] = ..., path: _Optional[str] = ..., protocol: _Optional[_Union[_enums_pb2.NasProtocol.Type, str]] = ..., exclusive_access: bool = ..., entity_id: _Optional[int] = ..., rpc_stats: _Optional[_Union[RpcStats, _Mapping]] = ...) -> None: ...

class DeleteEntityResult(_message.Message):
    __slots__ = ("error", "rpc_stats")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    RPC_STATS_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    rpc_stats: RpcStats
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., rpc_stats: _Optional[_Union[RpcStats, _Mapping]] = ...) -> None: ...

class MountNasShareArg(_message.Message):
    __slots__ = ("task_key", "remote_nas_path", "mount_identifier", "mount_options", "domain_name", "username", "password", "rpc_stats")
    TASK_KEY_FIELD_NUMBER: _ClassVar[int]
    REMOTE_NAS_PATH_FIELD_NUMBER: _ClassVar[int]
    MOUNT_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    MOUNT_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    RPC_STATS_FIELD_NUMBER: _ClassVar[int]
    task_key: str
    remote_nas_path: str
    mount_identifier: str
    mount_options: str
    domain_name: str
    username: str
    password: str
    rpc_stats: RpcStats
    def __init__(self, task_key: _Optional[str] = ..., remote_nas_path: _Optional[str] = ..., mount_identifier: _Optional[str] = ..., mount_options: _Optional[str] = ..., domain_name: _Optional[str] = ..., username: _Optional[str] = ..., password: _Optional[str] = ..., rpc_stats: _Optional[_Union[RpcStats, _Mapping]] = ...) -> None: ...

class MountNasShareResult(_message.Message):
    __slots__ = ("error", "mountpoint", "mountroot", "rpc_stats")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    MOUNTPOINT_FIELD_NUMBER: _ClassVar[int]
    MOUNTROOT_FIELD_NUMBER: _ClassVar[int]
    RPC_STATS_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    mountpoint: str
    mountroot: str
    rpc_stats: RpcStats
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., mountpoint: _Optional[str] = ..., mountroot: _Optional[str] = ..., rpc_stats: _Optional[_Union[RpcStats, _Mapping]] = ...) -> None: ...

class UnmountNasShareArg(_message.Message):
    __slots__ = ("task_key", "mountpoint", "rpc_stats")
    TASK_KEY_FIELD_NUMBER: _ClassVar[int]
    MOUNTPOINT_FIELD_NUMBER: _ClassVar[int]
    RPC_STATS_FIELD_NUMBER: _ClassVar[int]
    task_key: str
    mountpoint: str
    rpc_stats: RpcStats
    def __init__(self, task_key: _Optional[str] = ..., mountpoint: _Optional[str] = ..., rpc_stats: _Optional[_Union[RpcStats, _Mapping]] = ...) -> None: ...

class UnmountNasShareResult(_message.Message):
    __slots__ = ("error", "rpc_stats")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    RPC_STATS_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    rpc_stats: RpcStats
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., rpc_stats: _Optional[_Union[RpcStats, _Mapping]] = ...) -> None: ...

class MountVirtualDiskArg(_message.Message):
    __slots__ = ("task_id", "vm_disk_path", "volume_info", "backup_type", "rpc_stats")
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    VM_DISK_PATH_FIELD_NUMBER: _ClassVar[int]
    VOLUME_INFO_FIELD_NUMBER: _ClassVar[int]
    BACKUP_TYPE_FIELD_NUMBER: _ClassVar[int]
    RPC_STATS_FIELD_NUMBER: _ClassVar[int]
    task_id: int
    vm_disk_path: str
    volume_info: _volume_info_pb2.VolumeInfo
    backup_type: _enums_pb2.Environment.Type
    rpc_stats: RpcStats
    def __init__(self, task_id: _Optional[int] = ..., vm_disk_path: _Optional[str] = ..., volume_info: _Optional[_Union[_volume_info_pb2.VolumeInfo, _Mapping]] = ..., backup_type: _Optional[_Union[_enums_pb2.Environment.Type, str]] = ..., rpc_stats: _Optional[_Union[RpcStats, _Mapping]] = ...) -> None: ...

class MountVirtualDiskResult(_message.Message):
    __slots__ = ("error", "mountpoint", "fs_uuid", "rpc_stats")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    MOUNTPOINT_FIELD_NUMBER: _ClassVar[int]
    FS_UUID_FIELD_NUMBER: _ClassVar[int]
    RPC_STATS_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    mountpoint: str
    fs_uuid: str
    rpc_stats: RpcStats
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., mountpoint: _Optional[str] = ..., fs_uuid: _Optional[str] = ..., rpc_stats: _Optional[_Union[RpcStats, _Mapping]] = ...) -> None: ...

class UnmountVirtualDiskArg(_message.Message):
    __slots__ = ("task_key", "mountpoint", "rpc_stats")
    TASK_KEY_FIELD_NUMBER: _ClassVar[int]
    MOUNTPOINT_FIELD_NUMBER: _ClassVar[int]
    RPC_STATS_FIELD_NUMBER: _ClassVar[int]
    task_key: str
    mountpoint: str
    rpc_stats: RpcStats
    def __init__(self, task_key: _Optional[str] = ..., mountpoint: _Optional[str] = ..., rpc_stats: _Optional[_Union[RpcStats, _Mapping]] = ...) -> None: ...

class UnmountVirtualDiskResult(_message.Message):
    __slots__ = ("error", "mountpoint", "rpc_stats")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    MOUNTPOINT_FIELD_NUMBER: _ClassVar[int]
    RPC_STATS_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    mountpoint: str
    rpc_stats: RpcStats
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., mountpoint: _Optional[str] = ..., rpc_stats: _Optional[_Union[RpcStats, _Mapping]] = ...) -> None: ...

class DedupDataArg(_message.Message):
    __slots__ = ("data_region", "missing_dedup_range", "chunking_args")
    class DataRegion(_message.Message):
        __slots__ = ("offset", "length")
        OFFSET_FIELD_NUMBER: _ClassVar[int]
        LENGTH_FIELD_NUMBER: _ClassVar[int]
        offset: int
        length: int
        def __init__(self, offset: _Optional[int] = ..., length: _Optional[int] = ...) -> None: ...
    class ChunkingArgs(_message.Message):
        __slots__ = ("min_dedup_chunk_size", "max_dedup_chunk_size", "non_dedup_chunk_size")
        MIN_DEDUP_CHUNK_SIZE_FIELD_NUMBER: _ClassVar[int]
        MAX_DEDUP_CHUNK_SIZE_FIELD_NUMBER: _ClassVar[int]
        NON_DEDUP_CHUNK_SIZE_FIELD_NUMBER: _ClassVar[int]
        min_dedup_chunk_size: int
        max_dedup_chunk_size: int
        non_dedup_chunk_size: int
        def __init__(self, min_dedup_chunk_size: _Optional[int] = ..., max_dedup_chunk_size: _Optional[int] = ..., non_dedup_chunk_size: _Optional[int] = ...) -> None: ...
    DATA_REGION_FIELD_NUMBER: _ClassVar[int]
    MISSING_DEDUP_RANGE_FIELD_NUMBER: _ClassVar[int]
    CHUNKING_ARGS_FIELD_NUMBER: _ClassVar[int]
    data_region: DedupDataArg.DataRegion
    missing_dedup_range: _dedup_range_pb2.DedupRange
    chunking_args: DedupDataArg.ChunkingArgs
    def __init__(self, data_region: _Optional[_Union[DedupDataArg.DataRegion, _Mapping]] = ..., missing_dedup_range: _Optional[_Union[_dedup_range_pb2.DedupRange, _Mapping]] = ..., chunking_args: _Optional[_Union[DedupDataArg.ChunkingArgs, _Mapping]] = ...) -> None: ...

class brick(_message.Message):
    __slots__ = ("offset", "length", "sha1", "data", "brick_sha1")
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    SHA1_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    BRICK_SHA1_FIELD_NUMBER: _ClassVar[int]
    offset: int
    length: int
    sha1: str
    data: bytes
    brick_sha1: bytes
    def __init__(self, offset: _Optional[int] = ..., length: _Optional[int] = ..., sha1: _Optional[str] = ..., data: _Optional[bytes] = ..., brick_sha1: _Optional[bytes] = ...) -> None: ...

class DedupDataResult(_message.Message):
    __slots__ = ("dedup_range", "data", "eof", "io_latency_usecs", "dedup_compute_time_usecs", "num_cache_hits", "num_cache_misses")
    DEDUP_RANGE_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    EOF_FIELD_NUMBER: _ClassVar[int]
    IO_LATENCY_USECS_FIELD_NUMBER: _ClassVar[int]
    DEDUP_COMPUTE_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    NUM_CACHE_HITS_FIELD_NUMBER: _ClassVar[int]
    NUM_CACHE_MISSES_FIELD_NUMBER: _ClassVar[int]
    dedup_range: _dedup_range_pb2.DedupRange
    data: bytes
    eof: bool
    io_latency_usecs: int
    dedup_compute_time_usecs: int
    num_cache_hits: int
    num_cache_misses: int
    def __init__(self, dedup_range: _Optional[_Union[_dedup_range_pb2.DedupRange, _Mapping]] = ..., data: _Optional[bytes] = ..., eof: bool = ..., io_latency_usecs: _Optional[int] = ..., dedup_compute_time_usecs: _Optional[int] = ..., num_cache_hits: _Optional[int] = ..., num_cache_misses: _Optional[int] = ...) -> None: ...

class ReadFileDedupDataArg(_message.Message):
    __slots__ = ("proxy_header", "task_key", "file_path", "cache_handle", "dedup_data_arg", "file_size_bytes", "rpc_stats")
    PROXY_HEADER_FIELD_NUMBER: _ClassVar[int]
    TASK_KEY_FIELD_NUMBER: _ClassVar[int]
    FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    CACHE_HANDLE_FIELD_NUMBER: _ClassVar[int]
    DEDUP_DATA_ARG_FIELD_NUMBER: _ClassVar[int]
    FILE_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    RPC_STATS_FIELD_NUMBER: _ClassVar[int]
    proxy_header: bytes
    task_key: str
    file_path: str
    cache_handle: bool
    dedup_data_arg: DedupDataArg
    file_size_bytes: int
    rpc_stats: RpcStats
    def __init__(self, proxy_header: _Optional[bytes] = ..., task_key: _Optional[str] = ..., file_path: _Optional[str] = ..., cache_handle: bool = ..., dedup_data_arg: _Optional[_Union[DedupDataArg, _Mapping]] = ..., file_size_bytes: _Optional[int] = ..., rpc_stats: _Optional[_Union[RpcStats, _Mapping]] = ...) -> None: ...

class ReadFileDedupDataResult(_message.Message):
    __slots__ = ("error", "dedup_data_result", "rpc_stats")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    DEDUP_DATA_RESULT_FIELD_NUMBER: _ClassVar[int]
    RPC_STATS_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    dedup_data_result: DedupDataResult
    rpc_stats: RpcStats
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., dedup_data_result: _Optional[_Union[DedupDataResult, _Mapping]] = ..., rpc_stats: _Optional[_Union[RpcStats, _Mapping]] = ...) -> None: ...

class ReadFileBrickArg(_message.Message):
    __slots__ = ("proxy_header", "task_key", "file_path", "file_size_bytes", "brick_data_arg", "contiguous_len", "for_testing_burst_read", "rpc_stats")
    PROXY_HEADER_FIELD_NUMBER: _ClassVar[int]
    TASK_KEY_FIELD_NUMBER: _ClassVar[int]
    FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    FILE_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    BRICK_DATA_ARG_FIELD_NUMBER: _ClassVar[int]
    CONTIGUOUS_LEN_FIELD_NUMBER: _ClassVar[int]
    FOR_TESTING_BURST_READ_FIELD_NUMBER: _ClassVar[int]
    RPC_STATS_FIELD_NUMBER: _ClassVar[int]
    proxy_header: bytes
    task_key: str
    file_path: str
    file_size_bytes: int
    brick_data_arg: _containers.RepeatedCompositeFieldContainer[brick]
    contiguous_len: int
    for_testing_burst_read: bool
    rpc_stats: RpcStats
    def __init__(self, proxy_header: _Optional[bytes] = ..., task_key: _Optional[str] = ..., file_path: _Optional[str] = ..., file_size_bytes: _Optional[int] = ..., brick_data_arg: _Optional[_Iterable[_Union[brick, _Mapping]]] = ..., contiguous_len: _Optional[int] = ..., for_testing_burst_read: bool = ..., rpc_stats: _Optional[_Union[RpcStats, _Mapping]] = ...) -> None: ...

class ReadFileBrickResult(_message.Message):
    __slots__ = ("error", "brick_data_result", "rpc_stats")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    BRICK_DATA_RESULT_FIELD_NUMBER: _ClassVar[int]
    RPC_STATS_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    brick_data_result: _containers.RepeatedCompositeFieldContainer[brick]
    rpc_stats: RpcStats
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., brick_data_result: _Optional[_Iterable[_Union[brick, _Mapping]]] = ..., rpc_stats: _Optional[_Union[RpcStats, _Mapping]] = ...) -> None: ...

class RenameEntityArg(_message.Message):
    __slots__ = ("proxy_header", "base_arg", "task_key", "existing_path", "target_path", "entity_type", "replace_if_exists", "protocol", "entity_id", "rpc_stats")
    PROXY_HEADER_FIELD_NUMBER: _ClassVar[int]
    BASE_ARG_FIELD_NUMBER: _ClassVar[int]
    TASK_KEY_FIELD_NUMBER: _ClassVar[int]
    EXISTING_PATH_FIELD_NUMBER: _ClassVar[int]
    TARGET_PATH_FIELD_NUMBER: _ClassVar[int]
    ENTITY_TYPE_FIELD_NUMBER: _ClassVar[int]
    REPLACE_IF_EXISTS_FIELD_NUMBER: _ClassVar[int]
    PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    RPC_STATS_FIELD_NUMBER: _ClassVar[int]
    proxy_header: bytes
    base_arg: ProxyBaseArg
    task_key: str
    existing_path: str
    target_path: str
    entity_type: _directory_walker_pb2.EntityMetadata.EntityType
    replace_if_exists: bool
    protocol: _enums_pb2.NasProtocol.Type
    entity_id: int
    rpc_stats: RpcStats
    def __init__(self, proxy_header: _Optional[bytes] = ..., base_arg: _Optional[_Union[ProxyBaseArg, _Mapping]] = ..., task_key: _Optional[str] = ..., existing_path: _Optional[str] = ..., target_path: _Optional[str] = ..., entity_type: _Optional[_Union[_directory_walker_pb2.EntityMetadata.EntityType, str]] = ..., replace_if_exists: bool = ..., protocol: _Optional[_Union[_enums_pb2.NasProtocol.Type, str]] = ..., entity_id: _Optional[int] = ..., rpc_stats: _Optional[_Union[RpcStats, _Mapping]] = ...) -> None: ...

class RenameEntityResult(_message.Message):
    __slots__ = ("error", "rpc_stats")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    RPC_STATS_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    rpc_stats: RpcStats
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., rpc_stats: _Optional[_Union[RpcStats, _Mapping]] = ...) -> None: ...

class EndBackupArg(_message.Message):
    __slots__ = ("proxy_header", "task_key", "rpc_stats")
    PROXY_HEADER_FIELD_NUMBER: _ClassVar[int]
    TASK_KEY_FIELD_NUMBER: _ClassVar[int]
    RPC_STATS_FIELD_NUMBER: _ClassVar[int]
    proxy_header: bytes
    task_key: str
    rpc_stats: RpcStats
    def __init__(self, proxy_header: _Optional[bytes] = ..., task_key: _Optional[str] = ..., rpc_stats: _Optional[_Union[RpcStats, _Mapping]] = ...) -> None: ...

class EndBackupResult(_message.Message):
    __slots__ = ("error", "rpc_stats")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    RPC_STATS_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    rpc_stats: RpcStats
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., rpc_stats: _Optional[_Union[RpcStats, _Mapping]] = ...) -> None: ...

class CreateSymlinkArg(_message.Message):
    __slots__ = ("proxy_header", "base_arg", "task_key", "path", "target_path", "delete_entity", "protocol", "entity_id", "rpc_stats")
    PROXY_HEADER_FIELD_NUMBER: _ClassVar[int]
    BASE_ARG_FIELD_NUMBER: _ClassVar[int]
    TASK_KEY_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    TARGET_PATH_FIELD_NUMBER: _ClassVar[int]
    DELETE_ENTITY_FIELD_NUMBER: _ClassVar[int]
    PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    RPC_STATS_FIELD_NUMBER: _ClassVar[int]
    proxy_header: bytes
    base_arg: ProxyBaseArg
    task_key: str
    path: str
    target_path: str
    delete_entity: bool
    protocol: _enums_pb2.NasProtocol.Type
    entity_id: int
    rpc_stats: RpcStats
    def __init__(self, proxy_header: _Optional[bytes] = ..., base_arg: _Optional[_Union[ProxyBaseArg, _Mapping]] = ..., task_key: _Optional[str] = ..., path: _Optional[str] = ..., target_path: _Optional[str] = ..., delete_entity: bool = ..., protocol: _Optional[_Union[_enums_pb2.NasProtocol.Type, str]] = ..., entity_id: _Optional[int] = ..., rpc_stats: _Optional[_Union[RpcStats, _Mapping]] = ...) -> None: ...

class CreateSymlinkResult(_message.Message):
    __slots__ = ("error", "rpc_stats")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    RPC_STATS_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    rpc_stats: RpcStats
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., rpc_stats: _Optional[_Union[RpcStats, _Mapping]] = ...) -> None: ...

class EndRestoreArg(_message.Message):
    __slots__ = ("task_key", "base_arg", "rpc_stats")
    TASK_KEY_FIELD_NUMBER: _ClassVar[int]
    BASE_ARG_FIELD_NUMBER: _ClassVar[int]
    RPC_STATS_FIELD_NUMBER: _ClassVar[int]
    task_key: str
    base_arg: ProxyBaseArg
    rpc_stats: RpcStats
    def __init__(self, task_key: _Optional[str] = ..., base_arg: _Optional[_Union[ProxyBaseArg, _Mapping]] = ..., rpc_stats: _Optional[_Union[RpcStats, _Mapping]] = ...) -> None: ...

class EndRestoreResult(_message.Message):
    __slots__ = ("error", "rpc_stats")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    RPC_STATS_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    rpc_stats: RpcStats
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., rpc_stats: _Optional[_Union[RpcStats, _Mapping]] = ...) -> None: ...

class ExecuteActionArg(_message.Message):
    __slots__ = ("action", "op_clock", "base_arg", "create_restore_files_arg", "rpc_stats")
    class Action(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kCreateRestoreFile: _ClassVar[ExecuteActionArg.Action]
    kCreateRestoreFile: ExecuteActionArg.Action
    ACTION_FIELD_NUMBER: _ClassVar[int]
    OP_CLOCK_FIELD_NUMBER: _ClassVar[int]
    BASE_ARG_FIELD_NUMBER: _ClassVar[int]
    CREATE_RESTORE_FILES_ARG_FIELD_NUMBER: _ClassVar[int]
    RPC_STATS_FIELD_NUMBER: _ClassVar[int]
    action: ExecuteActionArg.Action
    op_clock: _op_clock_pb2.OpClock
    base_arg: ProxyBaseArg
    create_restore_files_arg: CreateRestoreFilesArg
    rpc_stats: RpcStats
    def __init__(self, action: _Optional[_Union[ExecuteActionArg.Action, str]] = ..., op_clock: _Optional[_Union[_op_clock_pb2.OpClock, _Mapping]] = ..., base_arg: _Optional[_Union[ProxyBaseArg, _Mapping]] = ..., create_restore_files_arg: _Optional[_Union[CreateRestoreFilesArg, _Mapping]] = ..., rpc_stats: _Optional[_Union[RpcStats, _Mapping]] = ...) -> None: ...

class ExecuteActionResult(_message.Message):
    __slots__ = ("error", "rpc_stats")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    RPC_STATS_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    rpc_stats: RpcStats
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., rpc_stats: _Optional[_Union[RpcStats, _Mapping]] = ...) -> None: ...

class ThrottleResourceUsageArg(_message.Message):
    __slots__ = ("source_utilization_map", "entity_to_source_map", "protocol", "rpc_stats")
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
        value: ThrottleResourceUsageArg.CurrentResourceInfo
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[ThrottleResourceUsageArg.CurrentResourceInfo, _Mapping]] = ...) -> None: ...
    class EntityToSourceMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: str
        def __init__(self, key: _Optional[int] = ..., value: _Optional[str] = ...) -> None: ...
    SOURCE_UTILIZATION_MAP_FIELD_NUMBER: _ClassVar[int]
    ENTITY_TO_SOURCE_MAP_FIELD_NUMBER: _ClassVar[int]
    PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    RPC_STATS_FIELD_NUMBER: _ClassVar[int]
    source_utilization_map: _containers.MessageMap[str, ThrottleResourceUsageArg.CurrentResourceInfo]
    entity_to_source_map: _containers.ScalarMap[int, str]
    protocol: _enums_pb2.NasProtocol.Type
    rpc_stats: RpcStats
    def __init__(self, source_utilization_map: _Optional[_Mapping[str, ThrottleResourceUsageArg.CurrentResourceInfo]] = ..., entity_to_source_map: _Optional[_Mapping[int, str]] = ..., protocol: _Optional[_Union[_enums_pb2.NasProtocol.Type, str]] = ..., rpc_stats: _Optional[_Union[RpcStats, _Mapping]] = ...) -> None: ...

class ThrottleResourceUsageResult(_message.Message):
    __slots__ = ("error", "rpc_stats")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    RPC_STATS_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    rpc_stats: RpcStats
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., rpc_stats: _Optional[_Union[RpcStats, _Mapping]] = ...) -> None: ...

class Nfsv41ReaddirCookie(_message.Message):
    __slots__ = ("readdir_cookie", "cookie_verifier", "fh")
    READDIR_COOKIE_FIELD_NUMBER: _ClassVar[int]
    COOKIE_VERIFIER_FIELD_NUMBER: _ClassVar[int]
    FH_FIELD_NUMBER: _ClassVar[int]
    readdir_cookie: int
    cookie_verifier: bytes
    fh: bytes
    def __init__(self, readdir_cookie: _Optional[int] = ..., cookie_verifier: _Optional[bytes] = ..., fh: _Optional[bytes] = ...) -> None: ...

class RpcStats(_message.Message):
    __slots__ = ("cluster_start_time_usecs", "cluster_end_time_usecs", "agent_start_time_usecs", "agent_end_time_usecs")
    CLUSTER_START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_END_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    AGENT_START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    AGENT_END_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    cluster_start_time_usecs: int
    cluster_end_time_usecs: int
    agent_start_time_usecs: int
    agent_end_time_usecs: int
    def __init__(self, cluster_start_time_usecs: _Optional[int] = ..., cluster_end_time_usecs: _Optional[int] = ..., agent_start_time_usecs: _Optional[int] = ..., agent_end_time_usecs: _Optional[int] = ...) -> None: ...
