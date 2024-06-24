from bifrost.stub import magneto_connector_params_pb2 as _magneto_connector_params_pb2
from util.storage import error_pb2 as _error_pb2
from magneto.storage_proxy.stub import rpc_args_pb2 as _rpc_args_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LocalStorageProxyConnectorParams(_message.Message):
    __slots__ = ("ip_addr", "proxy_port", "cluster_id", "cluster_incarnation_id")
    IP_ADDR_FIELD_NUMBER: _ClassVar[int]
    PROXY_PORT_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    ip_addr: str
    proxy_port: int
    cluster_id: int
    cluster_incarnation_id: int
    def __init__(self, ip_addr: _Optional[str] = ..., proxy_port: _Optional[int] = ..., cluster_id: _Optional[int] = ..., cluster_incarnation_id: _Optional[int] = ...) -> None: ...

class StorageProxyArg(_message.Message):
    __slots__ = ("type", "agent_connector_context_params", "local_storage_proxy_connector_params", "forward_request_to_local_storage_proxy", "get_root_metadata_arg", "fetch_children_metadata_arg", "purge_file_handles_arg", "create_restore_files_arg", "write_files_data_arg", "finalize_restore_files_arg", "delete_entity_arg", "mount_nas_share_arg", "unmount_nas_share_arg", "mount_virtual_disk_arg", "unmount_virtual_disk_arg", "rename_entity_arg", "end_backup_arg", "create_symlink_arg", "fetch_file_data_arg", "read_file_dedup_data_arg", "write_file_data_arg", "read_file_brick_arg")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kGetRootMetadata: _ClassVar[StorageProxyArg.Type]
        kFetchChildrenMetadata: _ClassVar[StorageProxyArg.Type]
        kPurgeFileHandles: _ClassVar[StorageProxyArg.Type]
        kCreateRestoreFiles: _ClassVar[StorageProxyArg.Type]
        kWriteFilesData: _ClassVar[StorageProxyArg.Type]
        kFinalizeRestoreFiles: _ClassVar[StorageProxyArg.Type]
        kDeleteEntity: _ClassVar[StorageProxyArg.Type]
        kMountNasShare: _ClassVar[StorageProxyArg.Type]
        kUnmountNasShare: _ClassVar[StorageProxyArg.Type]
        kMountVirtualDisk: _ClassVar[StorageProxyArg.Type]
        kUnmountVirtualDisk: _ClassVar[StorageProxyArg.Type]
        kRenameEntity: _ClassVar[StorageProxyArg.Type]
        kEndBackup: _ClassVar[StorageProxyArg.Type]
        kCreateSymlink: _ClassVar[StorageProxyArg.Type]
        kFetchFileData: _ClassVar[StorageProxyArg.Type]
        kReadFileDedupData: _ClassVar[StorageProxyArg.Type]
        kWriteFileData: _ClassVar[StorageProxyArg.Type]
        kReadFileBrick: _ClassVar[StorageProxyArg.Type]
    kGetRootMetadata: StorageProxyArg.Type
    kFetchChildrenMetadata: StorageProxyArg.Type
    kPurgeFileHandles: StorageProxyArg.Type
    kCreateRestoreFiles: StorageProxyArg.Type
    kWriteFilesData: StorageProxyArg.Type
    kFinalizeRestoreFiles: StorageProxyArg.Type
    kDeleteEntity: StorageProxyArg.Type
    kMountNasShare: StorageProxyArg.Type
    kUnmountNasShare: StorageProxyArg.Type
    kMountVirtualDisk: StorageProxyArg.Type
    kUnmountVirtualDisk: StorageProxyArg.Type
    kRenameEntity: StorageProxyArg.Type
    kEndBackup: StorageProxyArg.Type
    kCreateSymlink: StorageProxyArg.Type
    kFetchFileData: StorageProxyArg.Type
    kReadFileDedupData: StorageProxyArg.Type
    kWriteFileData: StorageProxyArg.Type
    kReadFileBrick: StorageProxyArg.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    AGENT_CONNECTOR_CONTEXT_PARAMS_FIELD_NUMBER: _ClassVar[int]
    LOCAL_STORAGE_PROXY_CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    FORWARD_REQUEST_TO_LOCAL_STORAGE_PROXY_FIELD_NUMBER: _ClassVar[int]
    GET_ROOT_METADATA_ARG_FIELD_NUMBER: _ClassVar[int]
    FETCH_CHILDREN_METADATA_ARG_FIELD_NUMBER: _ClassVar[int]
    PURGE_FILE_HANDLES_ARG_FIELD_NUMBER: _ClassVar[int]
    CREATE_RESTORE_FILES_ARG_FIELD_NUMBER: _ClassVar[int]
    WRITE_FILES_DATA_ARG_FIELD_NUMBER: _ClassVar[int]
    FINALIZE_RESTORE_FILES_ARG_FIELD_NUMBER: _ClassVar[int]
    DELETE_ENTITY_ARG_FIELD_NUMBER: _ClassVar[int]
    MOUNT_NAS_SHARE_ARG_FIELD_NUMBER: _ClassVar[int]
    UNMOUNT_NAS_SHARE_ARG_FIELD_NUMBER: _ClassVar[int]
    MOUNT_VIRTUAL_DISK_ARG_FIELD_NUMBER: _ClassVar[int]
    UNMOUNT_VIRTUAL_DISK_ARG_FIELD_NUMBER: _ClassVar[int]
    RENAME_ENTITY_ARG_FIELD_NUMBER: _ClassVar[int]
    END_BACKUP_ARG_FIELD_NUMBER: _ClassVar[int]
    CREATE_SYMLINK_ARG_FIELD_NUMBER: _ClassVar[int]
    FETCH_FILE_DATA_ARG_FIELD_NUMBER: _ClassVar[int]
    READ_FILE_DEDUP_DATA_ARG_FIELD_NUMBER: _ClassVar[int]
    WRITE_FILE_DATA_ARG_FIELD_NUMBER: _ClassVar[int]
    READ_FILE_BRICK_ARG_FIELD_NUMBER: _ClassVar[int]
    type: StorageProxyArg.Type
    agent_connector_context_params: _magneto_connector_params_pb2.AgentConnectorArg.AgentConnectorContext
    local_storage_proxy_connector_params: LocalStorageProxyConnectorParams
    forward_request_to_local_storage_proxy: bool
    get_root_metadata_arg: _rpc_args_pb2.GetRootMetadataArg
    fetch_children_metadata_arg: _rpc_args_pb2.FetchChildrenMetadataArg
    purge_file_handles_arg: _rpc_args_pb2.PurgeFileHandlesArg
    create_restore_files_arg: _rpc_args_pb2.CreateRestoreFilesArg
    write_files_data_arg: _rpc_args_pb2.WriteFilesDataArg
    finalize_restore_files_arg: _rpc_args_pb2.FinalizeRestoreFilesArg
    delete_entity_arg: _rpc_args_pb2.DeleteEntityArg
    mount_nas_share_arg: _rpc_args_pb2.MountNasShareArg
    unmount_nas_share_arg: _rpc_args_pb2.UnmountNasShareArg
    mount_virtual_disk_arg: _rpc_args_pb2.MountVirtualDiskArg
    unmount_virtual_disk_arg: _rpc_args_pb2.UnmountVirtualDiskArg
    rename_entity_arg: _rpc_args_pb2.RenameEntityArg
    end_backup_arg: _rpc_args_pb2.EndBackupArg
    create_symlink_arg: _rpc_args_pb2.CreateSymlinkArg
    fetch_file_data_arg: _rpc_args_pb2.FetchFileDataArg
    read_file_dedup_data_arg: _rpc_args_pb2.ReadFileDedupDataArg
    write_file_data_arg: _rpc_args_pb2.WriteFileDataArg
    read_file_brick_arg: _rpc_args_pb2.ReadFileBrickArg
    def __init__(self, type: _Optional[_Union[StorageProxyArg.Type, str]] = ..., agent_connector_context_params: _Optional[_Union[_magneto_connector_params_pb2.AgentConnectorArg.AgentConnectorContext, _Mapping]] = ..., local_storage_proxy_connector_params: _Optional[_Union[LocalStorageProxyConnectorParams, _Mapping]] = ..., forward_request_to_local_storage_proxy: bool = ..., get_root_metadata_arg: _Optional[_Union[_rpc_args_pb2.GetRootMetadataArg, _Mapping]] = ..., fetch_children_metadata_arg: _Optional[_Union[_rpc_args_pb2.FetchChildrenMetadataArg, _Mapping]] = ..., purge_file_handles_arg: _Optional[_Union[_rpc_args_pb2.PurgeFileHandlesArg, _Mapping]] = ..., create_restore_files_arg: _Optional[_Union[_rpc_args_pb2.CreateRestoreFilesArg, _Mapping]] = ..., write_files_data_arg: _Optional[_Union[_rpc_args_pb2.WriteFilesDataArg, _Mapping]] = ..., finalize_restore_files_arg: _Optional[_Union[_rpc_args_pb2.FinalizeRestoreFilesArg, _Mapping]] = ..., delete_entity_arg: _Optional[_Union[_rpc_args_pb2.DeleteEntityArg, _Mapping]] = ..., mount_nas_share_arg: _Optional[_Union[_rpc_args_pb2.MountNasShareArg, _Mapping]] = ..., unmount_nas_share_arg: _Optional[_Union[_rpc_args_pb2.UnmountNasShareArg, _Mapping]] = ..., mount_virtual_disk_arg: _Optional[_Union[_rpc_args_pb2.MountVirtualDiskArg, _Mapping]] = ..., unmount_virtual_disk_arg: _Optional[_Union[_rpc_args_pb2.UnmountVirtualDiskArg, _Mapping]] = ..., rename_entity_arg: _Optional[_Union[_rpc_args_pb2.RenameEntityArg, _Mapping]] = ..., end_backup_arg: _Optional[_Union[_rpc_args_pb2.EndBackupArg, _Mapping]] = ..., create_symlink_arg: _Optional[_Union[_rpc_args_pb2.CreateSymlinkArg, _Mapping]] = ..., fetch_file_data_arg: _Optional[_Union[_rpc_args_pb2.FetchFileDataArg, _Mapping]] = ..., read_file_dedup_data_arg: _Optional[_Union[_rpc_args_pb2.ReadFileDedupDataArg, _Mapping]] = ..., write_file_data_arg: _Optional[_Union[_rpc_args_pb2.WriteFileDataArg, _Mapping]] = ..., read_file_brick_arg: _Optional[_Union[_rpc_args_pb2.ReadFileBrickArg, _Mapping]] = ...) -> None: ...

class StorageProxyResult(_message.Message):
    __slots__ = ("error", "get_root_metadata_result", "fetch_children_metadata_result", "purge_file_handles_result", "create_restore_files_result", "write_files_data_result", "finalize_restore_files_result", "delete_entity_result", "mount_nas_share_result", "unmount_nas_share_result", "mount_virtual_disk_result", "unmount_virtual_disk_result", "rename_entity_result", "end_backup_result", "create_symlink_result", "fetch_file_data_result", "read_file_dedup_data_result", "write_file_data_result", "read_file_brick_result")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    GET_ROOT_METADATA_RESULT_FIELD_NUMBER: _ClassVar[int]
    FETCH_CHILDREN_METADATA_RESULT_FIELD_NUMBER: _ClassVar[int]
    PURGE_FILE_HANDLES_RESULT_FIELD_NUMBER: _ClassVar[int]
    CREATE_RESTORE_FILES_RESULT_FIELD_NUMBER: _ClassVar[int]
    WRITE_FILES_DATA_RESULT_FIELD_NUMBER: _ClassVar[int]
    FINALIZE_RESTORE_FILES_RESULT_FIELD_NUMBER: _ClassVar[int]
    DELETE_ENTITY_RESULT_FIELD_NUMBER: _ClassVar[int]
    MOUNT_NAS_SHARE_RESULT_FIELD_NUMBER: _ClassVar[int]
    UNMOUNT_NAS_SHARE_RESULT_FIELD_NUMBER: _ClassVar[int]
    MOUNT_VIRTUAL_DISK_RESULT_FIELD_NUMBER: _ClassVar[int]
    UNMOUNT_VIRTUAL_DISK_RESULT_FIELD_NUMBER: _ClassVar[int]
    RENAME_ENTITY_RESULT_FIELD_NUMBER: _ClassVar[int]
    END_BACKUP_RESULT_FIELD_NUMBER: _ClassVar[int]
    CREATE_SYMLINK_RESULT_FIELD_NUMBER: _ClassVar[int]
    FETCH_FILE_DATA_RESULT_FIELD_NUMBER: _ClassVar[int]
    READ_FILE_DEDUP_DATA_RESULT_FIELD_NUMBER: _ClassVar[int]
    WRITE_FILE_DATA_RESULT_FIELD_NUMBER: _ClassVar[int]
    READ_FILE_BRICK_RESULT_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    get_root_metadata_result: _rpc_args_pb2.GetRootMetadataResult
    fetch_children_metadata_result: _rpc_args_pb2.FetchChildrenMetadataResult
    purge_file_handles_result: _rpc_args_pb2.PurgeFileHandlesResult
    create_restore_files_result: _rpc_args_pb2.CreateRestoreFilesResult
    write_files_data_result: _rpc_args_pb2.WriteFilesDataResult
    finalize_restore_files_result: _rpc_args_pb2.FinalizeRestoreFilesResult
    delete_entity_result: _rpc_args_pb2.DeleteEntityResult
    mount_nas_share_result: _rpc_args_pb2.MountNasShareResult
    unmount_nas_share_result: _rpc_args_pb2.UnmountNasShareResult
    mount_virtual_disk_result: _rpc_args_pb2.MountVirtualDiskResult
    unmount_virtual_disk_result: _rpc_args_pb2.UnmountVirtualDiskResult
    rename_entity_result: _rpc_args_pb2.RenameEntityResult
    end_backup_result: _rpc_args_pb2.EndBackupResult
    create_symlink_result: _rpc_args_pb2.CreateSymlinkResult
    fetch_file_data_result: _rpc_args_pb2.FetchFileDataResult
    read_file_dedup_data_result: _rpc_args_pb2.ReadFileDedupDataResult
    write_file_data_result: _rpc_args_pb2.WriteFileDataResult
    read_file_brick_result: _rpc_args_pb2.ReadFileBrickResult
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., get_root_metadata_result: _Optional[_Union[_rpc_args_pb2.GetRootMetadataResult, _Mapping]] = ..., fetch_children_metadata_result: _Optional[_Union[_rpc_args_pb2.FetchChildrenMetadataResult, _Mapping]] = ..., purge_file_handles_result: _Optional[_Union[_rpc_args_pb2.PurgeFileHandlesResult, _Mapping]] = ..., create_restore_files_result: _Optional[_Union[_rpc_args_pb2.CreateRestoreFilesResult, _Mapping]] = ..., write_files_data_result: _Optional[_Union[_rpc_args_pb2.WriteFilesDataResult, _Mapping]] = ..., finalize_restore_files_result: _Optional[_Union[_rpc_args_pb2.FinalizeRestoreFilesResult, _Mapping]] = ..., delete_entity_result: _Optional[_Union[_rpc_args_pb2.DeleteEntityResult, _Mapping]] = ..., mount_nas_share_result: _Optional[_Union[_rpc_args_pb2.MountNasShareResult, _Mapping]] = ..., unmount_nas_share_result: _Optional[_Union[_rpc_args_pb2.UnmountNasShareResult, _Mapping]] = ..., mount_virtual_disk_result: _Optional[_Union[_rpc_args_pb2.MountVirtualDiskResult, _Mapping]] = ..., unmount_virtual_disk_result: _Optional[_Union[_rpc_args_pb2.UnmountVirtualDiskResult, _Mapping]] = ..., rename_entity_result: _Optional[_Union[_rpc_args_pb2.RenameEntityResult, _Mapping]] = ..., end_backup_result: _Optional[_Union[_rpc_args_pb2.EndBackupResult, _Mapping]] = ..., create_symlink_result: _Optional[_Union[_rpc_args_pb2.CreateSymlinkResult, _Mapping]] = ..., fetch_file_data_result: _Optional[_Union[_rpc_args_pb2.FetchFileDataResult, _Mapping]] = ..., read_file_dedup_data_result: _Optional[_Union[_rpc_args_pb2.ReadFileDedupDataResult, _Mapping]] = ..., write_file_data_result: _Optional[_Union[_rpc_args_pb2.WriteFileDataResult, _Mapping]] = ..., read_file_brick_result: _Optional[_Union[_rpc_args_pb2.ReadFileBrickResult, _Mapping]] = ...) -> None: ...
