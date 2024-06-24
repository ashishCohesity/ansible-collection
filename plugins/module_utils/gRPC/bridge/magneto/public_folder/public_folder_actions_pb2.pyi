from bridge.magneto.base import magneto_actions_pb2 as _magneto_actions_pb2
from magneto.base.entities import o365_pb2 as _o365_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PreparePublicFolderBackupInfo(_message.Message):
    __slots__ = ("view_cloning_enabled", "should_recursively_clone_dir")
    VIEW_CLONING_ENABLED_FIELD_NUMBER: _ClassVar[int]
    SHOULD_RECURSIVELY_CLONE_DIR_FIELD_NUMBER: _ClassVar[int]
    view_cloning_enabled: bool
    should_recursively_clone_dir: bool
    def __init__(self, view_cloning_enabled: bool = ..., should_recursively_clone_dir: bool = ...) -> None: ...

class EndBackupInfo(_message.Message):
    __slots__ = ("orphaned_directory_vec",)
    ORPHANED_DIRECTORY_VEC_FIELD_NUMBER: _ClassVar[int]
    orphaned_directory_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, orphaned_directory_vec: _Optional[_Iterable[str]] = ...) -> None: ...

class BackupPublicFolderArg(_message.Message):
    __slots__ = ("base", "type", "root_entity", "user_entity", "prepare_public_folder_backup_info", "end_backup_info")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kPreparePublicFolderBackup: _ClassVar[BackupPublicFolderArg.Type]
        kEndBackup: _ClassVar[BackupPublicFolderArg.Type]
    kPreparePublicFolderBackup: BackupPublicFolderArg.Type
    kEndBackup: BackupPublicFolderArg.Type
    BASE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ROOT_ENTITY_FIELD_NUMBER: _ClassVar[int]
    USER_ENTITY_FIELD_NUMBER: _ClassVar[int]
    PREPARE_PUBLIC_FOLDER_BACKUP_INFO_FIELD_NUMBER: _ClassVar[int]
    END_BACKUP_INFO_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_actions_pb2.BackupBaseArg
    type: BackupPublicFolderArg.Type
    root_entity: _o365_pb2.Entity
    user_entity: _o365_pb2.Entity
    prepare_public_folder_backup_info: PreparePublicFolderBackupInfo
    end_backup_info: EndBackupInfo
    def __init__(self, base: _Optional[_Union[_magneto_actions_pb2.BackupBaseArg, _Mapping]] = ..., type: _Optional[_Union[BackupPublicFolderArg.Type, str]] = ..., root_entity: _Optional[_Union[_o365_pb2.Entity, _Mapping]] = ..., user_entity: _Optional[_Union[_o365_pb2.Entity, _Mapping]] = ..., prepare_public_folder_backup_info: _Optional[_Union[PreparePublicFolderBackupInfo, _Mapping]] = ..., end_backup_info: _Optional[_Union[EndBackupInfo, _Mapping]] = ...) -> None: ...

class RestorePublicFolderArg(_message.Message):
    __slots__ = ("base", "type", "src_root_path")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kReadPublicFolderInfo: _ClassVar[RestorePublicFolderArg.Type]
    kReadPublicFolderInfo: RestorePublicFolderArg.Type
    BASE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SRC_ROOT_PATH_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_actions_pb2.RestoreBaseArg
    type: RestorePublicFolderArg.Type
    src_root_path: str
    def __init__(self, base: _Optional[_Union[_magneto_actions_pb2.RestoreBaseArg, _Mapping]] = ..., type: _Optional[_Union[RestorePublicFolderArg.Type, str]] = ..., src_root_path: _Optional[str] = ...) -> None: ...

class PublicFolderActionArg(_message.Message):
    __slots__ = ("task_id", "sub_task_id", "backup_public_folder_arg", "restore_public_folder_arg")
    PUBLIC_FOLDER_ACTION_ARG_FIELD_NUMBER: _ClassVar[int]
    public_folder_action_arg: _descriptor.FieldDescriptor
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    SUB_TASK_ID_FIELD_NUMBER: _ClassVar[int]
    BACKUP_PUBLIC_FOLDER_ARG_FIELD_NUMBER: _ClassVar[int]
    RESTORE_PUBLIC_FOLDER_ARG_FIELD_NUMBER: _ClassVar[int]
    task_id: int
    sub_task_id: int
    backup_public_folder_arg: BackupPublicFolderArg
    restore_public_folder_arg: RestorePublicFolderArg
    def __init__(self, task_id: _Optional[int] = ..., sub_task_id: _Optional[int] = ..., backup_public_folder_arg: _Optional[_Union[BackupPublicFolderArg, _Mapping]] = ..., restore_public_folder_arg: _Optional[_Union[RestorePublicFolderArg, _Mapping]] = ...) -> None: ...
