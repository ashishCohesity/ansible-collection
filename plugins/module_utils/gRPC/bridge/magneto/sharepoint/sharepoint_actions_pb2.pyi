from bridge.magneto.base import magneto_actions_pb2 as _magneto_actions_pb2
from magneto.base.entities import o365_pb2 as _o365_pb2
from magneto.connectors.ms_graph import graph_pb2 as _graph_pb2
from magneto.connectors.o365 import o365_pb2 as _o365_pb2_1
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SitesPreparationInfo(_message.Message):
    __slots__ = ("site_entity_vec",)
    SITE_ENTITY_VEC_FIELD_NUMBER: _ClassVar[int]
    site_entity_vec: _containers.RepeatedCompositeFieldContainer[_graph_pb2.Site]
    def __init__(self, site_entity_vec: _Optional[_Iterable[_Union[_graph_pb2.Site, _Mapping]]] = ...) -> None: ...

class PrepareSharepointBackupInfo(_message.Message):
    __slots__ = ("view_cloning_enabled", "should_recursively_clone_dir", "delete_entire_mailbox_dir", "dir_to_be_renamed", "first_time_view_clone", "skip_directory_cloning", "skip_drive_deletion", "site_one_drive_vec", "create_template_dir", "template_directory_name", "sharepoint_config_absent")
    VIEW_CLONING_ENABLED_FIELD_NUMBER: _ClassVar[int]
    SHOULD_RECURSIVELY_CLONE_DIR_FIELD_NUMBER: _ClassVar[int]
    DELETE_ENTIRE_MAILBOX_DIR_FIELD_NUMBER: _ClassVar[int]
    DIR_TO_BE_RENAMED_FIELD_NUMBER: _ClassVar[int]
    FIRST_TIME_VIEW_CLONE_FIELD_NUMBER: _ClassVar[int]
    SKIP_DIRECTORY_CLONING_FIELD_NUMBER: _ClassVar[int]
    SKIP_DRIVE_DELETION_FIELD_NUMBER: _ClassVar[int]
    SITE_ONE_DRIVE_VEC_FIELD_NUMBER: _ClassVar[int]
    CREATE_TEMPLATE_DIR_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_DIRECTORY_NAME_FIELD_NUMBER: _ClassVar[int]
    SHAREPOINT_CONFIG_ABSENT_FIELD_NUMBER: _ClassVar[int]
    view_cloning_enabled: bool
    should_recursively_clone_dir: bool
    delete_entire_mailbox_dir: bool
    dir_to_be_renamed: str
    first_time_view_clone: bool
    skip_directory_cloning: bool
    skip_drive_deletion: bool
    site_one_drive_vec: _containers.RepeatedScalarFieldContainer[str]
    create_template_dir: bool
    template_directory_name: str
    sharepoint_config_absent: bool
    def __init__(self, view_cloning_enabled: bool = ..., should_recursively_clone_dir: bool = ..., delete_entire_mailbox_dir: bool = ..., dir_to_be_renamed: _Optional[str] = ..., first_time_view_clone: bool = ..., skip_directory_cloning: bool = ..., skip_drive_deletion: bool = ..., site_one_drive_vec: _Optional[_Iterable[str]] = ..., create_template_dir: bool = ..., template_directory_name: _Optional[str] = ..., sharepoint_config_absent: bool = ...) -> None: ...

class SetupListsInfo(_message.Message):
    __slots__ = ("list_vec",)
    LIST_VEC_FIELD_NUMBER: _ClassVar[int]
    list_vec: _containers.RepeatedCompositeFieldContainer[_graph_pb2.List]
    def __init__(self, list_vec: _Optional[_Iterable[_Union[_graph_pb2.List, _Mapping]]] = ...) -> None: ...

class BackupListsInfo(_message.Message):
    __slots__ = ("site_id", "list_id")
    SITE_ID_FIELD_NUMBER: _ClassVar[int]
    LIST_ID_FIELD_NUMBER: _ClassVar[int]
    site_id: str
    list_id: str
    def __init__(self, site_id: _Optional[str] = ..., list_id: _Optional[str] = ...) -> None: ...

class EndListsSubTaskInfo(_message.Message):
    __slots__ = ("site_id",)
    SITE_ID_FIELD_NUMBER: _ClassVar[int]
    site_id: str
    def __init__(self, site_id: _Optional[str] = ...) -> None: ...

class EndListsBackupInfo(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class EndBackupInfo(_message.Message):
    __slots__ = ("sharepoint_config", "write_config_file", "cleanup_on_failure", "is_full_backup")
    SHAREPOINT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    WRITE_CONFIG_FILE_FIELD_NUMBER: _ClassVar[int]
    CLEANUP_ON_FAILURE_FIELD_NUMBER: _ClassVar[int]
    IS_FULL_BACKUP_FIELD_NUMBER: _ClassVar[int]
    sharepoint_config: _o365_pb2_1.SharepointSparseConfig
    write_config_file: bool
    cleanup_on_failure: bool
    is_full_backup: bool
    def __init__(self, sharepoint_config: _Optional[_Union[_o365_pb2_1.SharepointSparseConfig, _Mapping]] = ..., write_config_file: bool = ..., cleanup_on_failure: bool = ..., is_full_backup: bool = ...) -> None: ...

class BackupSharepointArg(_message.Message):
    __slots__ = ("base", "type", "root_entity", "user_entity", "prepare_sharepoint_backup_info", "setup_lists_info", "backup_lists_info", "end_lists_backup_info", "end_lists_sub_task_info", "sites_preparation_info", "end_backup_info", "site_id")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kPrepareSharepointBackup: _ClassVar[BackupSharepointArg.Type]
        kSetupListsInfo: _ClassVar[BackupSharepointArg.Type]
        kBackupLists: _ClassVar[BackupSharepointArg.Type]
        kEndListsBackup: _ClassVar[BackupSharepointArg.Type]
        kEndListsSubTask: _ClassVar[BackupSharepointArg.Type]
        kPrepareSitesInfo: _ClassVar[BackupSharepointArg.Type]
        kEndBackup: _ClassVar[BackupSharepointArg.Type]
    kPrepareSharepointBackup: BackupSharepointArg.Type
    kSetupListsInfo: BackupSharepointArg.Type
    kBackupLists: BackupSharepointArg.Type
    kEndListsBackup: BackupSharepointArg.Type
    kEndListsSubTask: BackupSharepointArg.Type
    kPrepareSitesInfo: BackupSharepointArg.Type
    kEndBackup: BackupSharepointArg.Type
    BASE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ROOT_ENTITY_FIELD_NUMBER: _ClassVar[int]
    USER_ENTITY_FIELD_NUMBER: _ClassVar[int]
    PREPARE_SHAREPOINT_BACKUP_INFO_FIELD_NUMBER: _ClassVar[int]
    SETUP_LISTS_INFO_FIELD_NUMBER: _ClassVar[int]
    BACKUP_LISTS_INFO_FIELD_NUMBER: _ClassVar[int]
    END_LISTS_BACKUP_INFO_FIELD_NUMBER: _ClassVar[int]
    END_LISTS_SUB_TASK_INFO_FIELD_NUMBER: _ClassVar[int]
    SITES_PREPARATION_INFO_FIELD_NUMBER: _ClassVar[int]
    END_BACKUP_INFO_FIELD_NUMBER: _ClassVar[int]
    SITE_ID_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_actions_pb2.BackupBaseArg
    type: BackupSharepointArg.Type
    root_entity: _o365_pb2.Entity
    user_entity: _o365_pb2.Entity
    prepare_sharepoint_backup_info: PrepareSharepointBackupInfo
    setup_lists_info: SetupListsInfo
    backup_lists_info: BackupListsInfo
    end_lists_backup_info: EndListsBackupInfo
    end_lists_sub_task_info: EndListsSubTaskInfo
    sites_preparation_info: SitesPreparationInfo
    end_backup_info: EndBackupInfo
    site_id: str
    def __init__(self, base: _Optional[_Union[_magneto_actions_pb2.BackupBaseArg, _Mapping]] = ..., type: _Optional[_Union[BackupSharepointArg.Type, str]] = ..., root_entity: _Optional[_Union[_o365_pb2.Entity, _Mapping]] = ..., user_entity: _Optional[_Union[_o365_pb2.Entity, _Mapping]] = ..., prepare_sharepoint_backup_info: _Optional[_Union[PrepareSharepointBackupInfo, _Mapping]] = ..., setup_lists_info: _Optional[_Union[SetupListsInfo, _Mapping]] = ..., backup_lists_info: _Optional[_Union[BackupListsInfo, _Mapping]] = ..., end_lists_backup_info: _Optional[_Union[EndListsBackupInfo, _Mapping]] = ..., end_lists_sub_task_info: _Optional[_Union[EndListsSubTaskInfo, _Mapping]] = ..., sites_preparation_info: _Optional[_Union[SitesPreparationInfo, _Mapping]] = ..., end_backup_info: _Optional[_Union[EndBackupInfo, _Mapping]] = ..., site_id: _Optional[str] = ...) -> None: ...

class RestoreSharepointArg(_message.Message):
    __slots__ = ("base", "type", "src_root_path", "site_info")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kSharepointRestoreCloneView: _ClassVar[RestoreSharepointArg.Type]
        kGetSiteDriveInfo: _ClassVar[RestoreSharepointArg.Type]
    kSharepointRestoreCloneView: RestoreSharepointArg.Type
    kGetSiteDriveInfo: RestoreSharepointArg.Type
    BASE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SRC_ROOT_PATH_FIELD_NUMBER: _ClassVar[int]
    SITE_INFO_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_actions_pb2.RestoreBaseArg
    type: RestoreSharepointArg.Type
    src_root_path: str
    site_info: SiteInfo
    def __init__(self, base: _Optional[_Union[_magneto_actions_pb2.RestoreBaseArg, _Mapping]] = ..., type: _Optional[_Union[RestoreSharepointArg.Type, str]] = ..., src_root_path: _Optional[str] = ..., site_info: _Optional[_Union[SiteInfo, _Mapping]] = ...) -> None: ...

class SiteInfo(_message.Message):
    __slots__ = ("src_relative_path", "site_entity")
    SRC_RELATIVE_PATH_FIELD_NUMBER: _ClassVar[int]
    SITE_ENTITY_FIELD_NUMBER: _ClassVar[int]
    src_relative_path: str
    site_entity: _o365_pb2.Entity
    def __init__(self, src_relative_path: _Optional[str] = ..., site_entity: _Optional[_Union[_o365_pb2.Entity, _Mapping]] = ...) -> None: ...

class SharepointActionArg(_message.Message):
    __slots__ = ("task_id", "sub_task_id", "backup_sharepoint_arg", "restore_sharepoint_arg")
    SHAREPOINT_ACTION_ARG_FIELD_NUMBER: _ClassVar[int]
    sharepoint_action_arg: _descriptor.FieldDescriptor
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    SUB_TASK_ID_FIELD_NUMBER: _ClassVar[int]
    BACKUP_SHAREPOINT_ARG_FIELD_NUMBER: _ClassVar[int]
    RESTORE_SHAREPOINT_ARG_FIELD_NUMBER: _ClassVar[int]
    task_id: int
    sub_task_id: int
    backup_sharepoint_arg: BackupSharepointArg
    restore_sharepoint_arg: RestoreSharepointArg
    def __init__(self, task_id: _Optional[int] = ..., sub_task_id: _Optional[int] = ..., backup_sharepoint_arg: _Optional[_Union[BackupSharepointArg, _Mapping]] = ..., restore_sharepoint_arg: _Optional[_Union[RestoreSharepointArg, _Mapping]] = ...) -> None: ...
