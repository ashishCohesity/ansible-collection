from apache_util.base import error_pb2 as _error_pb2
from apache_util.smb import smb_proxy_param_pb2 as _smb_proxy_param_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LocalSmbProxyConnectorParams(_message.Message):
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

class SmbProxyArg(_message.Message):
    __slots__ = ("type", "local_smb_proxy_connector_params", "get_root_metadata_arg", "fetch_children_metadata_arg", "purge_task_arg", "create_restore_files_arg", "finalize_restore_files_arg", "create_entity_arg", "delete_entity_arg", "rename_entity_arg", "set_entity_metadata_arg", "create_symlink_arg", "create_hardlink_arg", "fetch_file_data_arg", "write_file_data_arg", "write_files_data_arg", "verify_share_arg", "update_ad_user_password_arg", "get_nfs_complement_metadata_arg")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kGetRootMetadata: _ClassVar[SmbProxyArg.Type]
        kFetchChildrenMetadata: _ClassVar[SmbProxyArg.Type]
        kPurgeTask: _ClassVar[SmbProxyArg.Type]
        kCreateRestoreFiles: _ClassVar[SmbProxyArg.Type]
        kFinalizeRestoreFiles: _ClassVar[SmbProxyArg.Type]
        kCreateEntity: _ClassVar[SmbProxyArg.Type]
        kDeleteEntity: _ClassVar[SmbProxyArg.Type]
        kRenameEntity: _ClassVar[SmbProxyArg.Type]
        kSetEntityMetadata: _ClassVar[SmbProxyArg.Type]
        kCreateSymlink: _ClassVar[SmbProxyArg.Type]
        kCreateHardlink: _ClassVar[SmbProxyArg.Type]
        kFetchFileData: _ClassVar[SmbProxyArg.Type]
        kWriteFileData: _ClassVar[SmbProxyArg.Type]
        kWriteFilesData: _ClassVar[SmbProxyArg.Type]
        kVerifyShare: _ClassVar[SmbProxyArg.Type]
        kUpdateAdUserPassword: _ClassVar[SmbProxyArg.Type]
        kGetNfsComplementMetadata: _ClassVar[SmbProxyArg.Type]
    kGetRootMetadata: SmbProxyArg.Type
    kFetchChildrenMetadata: SmbProxyArg.Type
    kPurgeTask: SmbProxyArg.Type
    kCreateRestoreFiles: SmbProxyArg.Type
    kFinalizeRestoreFiles: SmbProxyArg.Type
    kCreateEntity: SmbProxyArg.Type
    kDeleteEntity: SmbProxyArg.Type
    kRenameEntity: SmbProxyArg.Type
    kSetEntityMetadata: SmbProxyArg.Type
    kCreateSymlink: SmbProxyArg.Type
    kCreateHardlink: SmbProxyArg.Type
    kFetchFileData: SmbProxyArg.Type
    kWriteFileData: SmbProxyArg.Type
    kWriteFilesData: SmbProxyArg.Type
    kVerifyShare: SmbProxyArg.Type
    kUpdateAdUserPassword: SmbProxyArg.Type
    kGetNfsComplementMetadata: SmbProxyArg.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    LOCAL_SMB_PROXY_CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    GET_ROOT_METADATA_ARG_FIELD_NUMBER: _ClassVar[int]
    FETCH_CHILDREN_METADATA_ARG_FIELD_NUMBER: _ClassVar[int]
    PURGE_TASK_ARG_FIELD_NUMBER: _ClassVar[int]
    CREATE_RESTORE_FILES_ARG_FIELD_NUMBER: _ClassVar[int]
    FINALIZE_RESTORE_FILES_ARG_FIELD_NUMBER: _ClassVar[int]
    CREATE_ENTITY_ARG_FIELD_NUMBER: _ClassVar[int]
    DELETE_ENTITY_ARG_FIELD_NUMBER: _ClassVar[int]
    RENAME_ENTITY_ARG_FIELD_NUMBER: _ClassVar[int]
    SET_ENTITY_METADATA_ARG_FIELD_NUMBER: _ClassVar[int]
    CREATE_SYMLINK_ARG_FIELD_NUMBER: _ClassVar[int]
    CREATE_HARDLINK_ARG_FIELD_NUMBER: _ClassVar[int]
    FETCH_FILE_DATA_ARG_FIELD_NUMBER: _ClassVar[int]
    WRITE_FILE_DATA_ARG_FIELD_NUMBER: _ClassVar[int]
    WRITE_FILES_DATA_ARG_FIELD_NUMBER: _ClassVar[int]
    VERIFY_SHARE_ARG_FIELD_NUMBER: _ClassVar[int]
    UPDATE_AD_USER_PASSWORD_ARG_FIELD_NUMBER: _ClassVar[int]
    GET_NFS_COMPLEMENT_METADATA_ARG_FIELD_NUMBER: _ClassVar[int]
    type: SmbProxyArg.Type
    local_smb_proxy_connector_params: LocalSmbProxyConnectorParams
    get_root_metadata_arg: _smb_proxy_param_pb2.SmbProxyGetRootMetadataArg
    fetch_children_metadata_arg: _smb_proxy_param_pb2.SmbProxyFetchChildrenMetadataArg
    purge_task_arg: _smb_proxy_param_pb2.SmbProxyPurgeTaskArg
    create_restore_files_arg: _smb_proxy_param_pb2.SmbProxyCreateRestoreFilesArg
    finalize_restore_files_arg: _smb_proxy_param_pb2.SmbProxyFinalizeRestoreFilesArg
    create_entity_arg: _smb_proxy_param_pb2.SmbProxyCreateEntityArg
    delete_entity_arg: _smb_proxy_param_pb2.SmbProxyDeleteEntityArg
    rename_entity_arg: _smb_proxy_param_pb2.SmbProxyRenameEntityArg
    set_entity_metadata_arg: _smb_proxy_param_pb2.SmbProxySetEntityMetadataArg
    create_symlink_arg: _smb_proxy_param_pb2.SmbProxyCreateSymlinkArg
    create_hardlink_arg: _smb_proxy_param_pb2.SmbProxyCreateHardlinkArg
    fetch_file_data_arg: _smb_proxy_param_pb2.SmbProxyFetchFileDataArg
    write_file_data_arg: _smb_proxy_param_pb2.SmbProxyWriteFileDataArg
    write_files_data_arg: _smb_proxy_param_pb2.SmbProxyWriteFilesDataArg
    verify_share_arg: _smb_proxy_param_pb2.SmbProxyVerifyShareArg
    update_ad_user_password_arg: _smb_proxy_param_pb2.SmbProxyUpdateAdUserPasswordArg
    get_nfs_complement_metadata_arg: _smb_proxy_param_pb2.SmbProxyGetNfsComplementMetadataArg
    def __init__(self, type: _Optional[_Union[SmbProxyArg.Type, str]] = ..., local_smb_proxy_connector_params: _Optional[_Union[LocalSmbProxyConnectorParams, _Mapping]] = ..., get_root_metadata_arg: _Optional[_Union[_smb_proxy_param_pb2.SmbProxyGetRootMetadataArg, _Mapping]] = ..., fetch_children_metadata_arg: _Optional[_Union[_smb_proxy_param_pb2.SmbProxyFetchChildrenMetadataArg, _Mapping]] = ..., purge_task_arg: _Optional[_Union[_smb_proxy_param_pb2.SmbProxyPurgeTaskArg, _Mapping]] = ..., create_restore_files_arg: _Optional[_Union[_smb_proxy_param_pb2.SmbProxyCreateRestoreFilesArg, _Mapping]] = ..., finalize_restore_files_arg: _Optional[_Union[_smb_proxy_param_pb2.SmbProxyFinalizeRestoreFilesArg, _Mapping]] = ..., create_entity_arg: _Optional[_Union[_smb_proxy_param_pb2.SmbProxyCreateEntityArg, _Mapping]] = ..., delete_entity_arg: _Optional[_Union[_smb_proxy_param_pb2.SmbProxyDeleteEntityArg, _Mapping]] = ..., rename_entity_arg: _Optional[_Union[_smb_proxy_param_pb2.SmbProxyRenameEntityArg, _Mapping]] = ..., set_entity_metadata_arg: _Optional[_Union[_smb_proxy_param_pb2.SmbProxySetEntityMetadataArg, _Mapping]] = ..., create_symlink_arg: _Optional[_Union[_smb_proxy_param_pb2.SmbProxyCreateSymlinkArg, _Mapping]] = ..., create_hardlink_arg: _Optional[_Union[_smb_proxy_param_pb2.SmbProxyCreateHardlinkArg, _Mapping]] = ..., fetch_file_data_arg: _Optional[_Union[_smb_proxy_param_pb2.SmbProxyFetchFileDataArg, _Mapping]] = ..., write_file_data_arg: _Optional[_Union[_smb_proxy_param_pb2.SmbProxyWriteFileDataArg, _Mapping]] = ..., write_files_data_arg: _Optional[_Union[_smb_proxy_param_pb2.SmbProxyWriteFilesDataArg, _Mapping]] = ..., verify_share_arg: _Optional[_Union[_smb_proxy_param_pb2.SmbProxyVerifyShareArg, _Mapping]] = ..., update_ad_user_password_arg: _Optional[_Union[_smb_proxy_param_pb2.SmbProxyUpdateAdUserPasswordArg, _Mapping]] = ..., get_nfs_complement_metadata_arg: _Optional[_Union[_smb_proxy_param_pb2.SmbProxyGetNfsComplementMetadataArg, _Mapping]] = ...) -> None: ...

class SmbProxyResult(_message.Message):
    __slots__ = ("error", "get_root_metadata_result", "fetch_children_metadata_result", "purge_task_result", "create_restore_files_result", "finalize_restore_files_result", "create_entity_result", "delete_entity_result", "rename_entity_result", "set_entity_metadata_result", "create_symlink_result", "create_hardlink_result", "fetch_file_data_result", "write_file_data_result", "write_files_data_result", "verify_share_result", "update_ad_user_password_result", "get_nfs_complement_metadata_result")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    GET_ROOT_METADATA_RESULT_FIELD_NUMBER: _ClassVar[int]
    FETCH_CHILDREN_METADATA_RESULT_FIELD_NUMBER: _ClassVar[int]
    PURGE_TASK_RESULT_FIELD_NUMBER: _ClassVar[int]
    CREATE_RESTORE_FILES_RESULT_FIELD_NUMBER: _ClassVar[int]
    FINALIZE_RESTORE_FILES_RESULT_FIELD_NUMBER: _ClassVar[int]
    CREATE_ENTITY_RESULT_FIELD_NUMBER: _ClassVar[int]
    DELETE_ENTITY_RESULT_FIELD_NUMBER: _ClassVar[int]
    RENAME_ENTITY_RESULT_FIELD_NUMBER: _ClassVar[int]
    SET_ENTITY_METADATA_RESULT_FIELD_NUMBER: _ClassVar[int]
    CREATE_SYMLINK_RESULT_FIELD_NUMBER: _ClassVar[int]
    CREATE_HARDLINK_RESULT_FIELD_NUMBER: _ClassVar[int]
    FETCH_FILE_DATA_RESULT_FIELD_NUMBER: _ClassVar[int]
    WRITE_FILE_DATA_RESULT_FIELD_NUMBER: _ClassVar[int]
    WRITE_FILES_DATA_RESULT_FIELD_NUMBER: _ClassVar[int]
    VERIFY_SHARE_RESULT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_AD_USER_PASSWORD_RESULT_FIELD_NUMBER: _ClassVar[int]
    GET_NFS_COMPLEMENT_METADATA_RESULT_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    get_root_metadata_result: _smb_proxy_param_pb2.SmbProxyGetRootMetadataResult
    fetch_children_metadata_result: _smb_proxy_param_pb2.SmbProxyFetchChildrenMetadataResult
    purge_task_result: _smb_proxy_param_pb2.SmbProxyPurgeTaskResult
    create_restore_files_result: _smb_proxy_param_pb2.SmbProxyCreateRestoreFilesResult
    finalize_restore_files_result: _smb_proxy_param_pb2.SmbProxyFinalizeRestoreFilesResult
    create_entity_result: _smb_proxy_param_pb2.SmbProxyCreateEntityResult
    delete_entity_result: _smb_proxy_param_pb2.SmbProxyDeleteEntityResult
    rename_entity_result: _smb_proxy_param_pb2.SmbProxyRenameEntityResult
    set_entity_metadata_result: _smb_proxy_param_pb2.SmbProxySetEntityMetadataResult
    create_symlink_result: _smb_proxy_param_pb2.SmbProxyCreateSymlinkResult
    create_hardlink_result: _smb_proxy_param_pb2.SmbProxyCreateHardlinkResult
    fetch_file_data_result: _smb_proxy_param_pb2.SmbProxyFetchFileDataResult
    write_file_data_result: _smb_proxy_param_pb2.SmbProxyWriteFileDataResult
    write_files_data_result: _smb_proxy_param_pb2.SmbProxyWriteFilesDataResult
    verify_share_result: _smb_proxy_param_pb2.SmbProxyVerifyShareResult
    update_ad_user_password_result: _smb_proxy_param_pb2.SmbProxyUpdateAdUserPasswordResult
    get_nfs_complement_metadata_result: _smb_proxy_param_pb2.SmbProxyGetNfsComplementMetadataResult
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., get_root_metadata_result: _Optional[_Union[_smb_proxy_param_pb2.SmbProxyGetRootMetadataResult, _Mapping]] = ..., fetch_children_metadata_result: _Optional[_Union[_smb_proxy_param_pb2.SmbProxyFetchChildrenMetadataResult, _Mapping]] = ..., purge_task_result: _Optional[_Union[_smb_proxy_param_pb2.SmbProxyPurgeTaskResult, _Mapping]] = ..., create_restore_files_result: _Optional[_Union[_smb_proxy_param_pb2.SmbProxyCreateRestoreFilesResult, _Mapping]] = ..., finalize_restore_files_result: _Optional[_Union[_smb_proxy_param_pb2.SmbProxyFinalizeRestoreFilesResult, _Mapping]] = ..., create_entity_result: _Optional[_Union[_smb_proxy_param_pb2.SmbProxyCreateEntityResult, _Mapping]] = ..., delete_entity_result: _Optional[_Union[_smb_proxy_param_pb2.SmbProxyDeleteEntityResult, _Mapping]] = ..., rename_entity_result: _Optional[_Union[_smb_proxy_param_pb2.SmbProxyRenameEntityResult, _Mapping]] = ..., set_entity_metadata_result: _Optional[_Union[_smb_proxy_param_pb2.SmbProxySetEntityMetadataResult, _Mapping]] = ..., create_symlink_result: _Optional[_Union[_smb_proxy_param_pb2.SmbProxyCreateSymlinkResult, _Mapping]] = ..., create_hardlink_result: _Optional[_Union[_smb_proxy_param_pb2.SmbProxyCreateHardlinkResult, _Mapping]] = ..., fetch_file_data_result: _Optional[_Union[_smb_proxy_param_pb2.SmbProxyFetchFileDataResult, _Mapping]] = ..., write_file_data_result: _Optional[_Union[_smb_proxy_param_pb2.SmbProxyWriteFileDataResult, _Mapping]] = ..., write_files_data_result: _Optional[_Union[_smb_proxy_param_pb2.SmbProxyWriteFilesDataResult, _Mapping]] = ..., verify_share_result: _Optional[_Union[_smb_proxy_param_pb2.SmbProxyVerifyShareResult, _Mapping]] = ..., update_ad_user_password_result: _Optional[_Union[_smb_proxy_param_pb2.SmbProxyUpdateAdUserPasswordResult, _Mapping]] = ..., get_nfs_complement_metadata_result: _Optional[_Union[_smb_proxy_param_pb2.SmbProxyGetNfsComplementMetadataResult, _Mapping]] = ...) -> None: ...
