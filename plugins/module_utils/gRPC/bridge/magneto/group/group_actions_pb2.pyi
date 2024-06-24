from bridge.magneto.base import magneto_actions_pb2 as _magneto_actions_pb2
from magneto.base.entities import o365_pb2 as _o365_pb2
from magneto.connectors.o365 import o365_pb2 as _o365_pb2_1
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PrepareGroupBackupInfo(_message.Message):
    __slots__ = ("should_recursively_clone_dir", "create_group_mailbox_dir")
    SHOULD_RECURSIVELY_CLONE_DIR_FIELD_NUMBER: _ClassVar[int]
    CREATE_GROUP_MAILBOX_DIR_FIELD_NUMBER: _ClassVar[int]
    should_recursively_clone_dir: bool
    create_group_mailbox_dir: bool
    def __init__(self, should_recursively_clone_dir: bool = ..., create_group_mailbox_dir: bool = ...) -> None: ...

class EndBackupInfo(_message.Message):
    __slots__ = ("group_config", "write_config_file", "cleanup_on_failure")
    GROUP_CONFIG_FIELD_NUMBER: _ClassVar[int]
    WRITE_CONFIG_FILE_FIELD_NUMBER: _ClassVar[int]
    CLEANUP_ON_FAILURE_FIELD_NUMBER: _ClassVar[int]
    group_config: _o365_pb2_1.O365GroupSparseConfig
    write_config_file: bool
    cleanup_on_failure: bool
    def __init__(self, group_config: _Optional[_Union[_o365_pb2_1.O365GroupSparseConfig, _Mapping]] = ..., write_config_file: bool = ..., cleanup_on_failure: bool = ...) -> None: ...

class BackupGroupArg(_message.Message):
    __slots__ = ("base", "type", "root_entity", "group_entity", "prepare_group_backup_info", "end_backup_info")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kPrepareGroupBackup: _ClassVar[BackupGroupArg.Type]
        kEndGroupBackup: _ClassVar[BackupGroupArg.Type]
    kPrepareGroupBackup: BackupGroupArg.Type
    kEndGroupBackup: BackupGroupArg.Type
    BASE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ROOT_ENTITY_FIELD_NUMBER: _ClassVar[int]
    GROUP_ENTITY_FIELD_NUMBER: _ClassVar[int]
    PREPARE_GROUP_BACKUP_INFO_FIELD_NUMBER: _ClassVar[int]
    END_BACKUP_INFO_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_actions_pb2.BackupBaseArg
    type: BackupGroupArg.Type
    root_entity: _o365_pb2.Entity
    group_entity: _o365_pb2.Entity
    prepare_group_backup_info: PrepareGroupBackupInfo
    end_backup_info: EndBackupInfo
    def __init__(self, base: _Optional[_Union[_magneto_actions_pb2.BackupBaseArg, _Mapping]] = ..., type: _Optional[_Union[BackupGroupArg.Type, str]] = ..., root_entity: _Optional[_Union[_o365_pb2.Entity, _Mapping]] = ..., group_entity: _Optional[_Union[_o365_pb2.Entity, _Mapping]] = ..., prepare_group_backup_info: _Optional[_Union[PrepareGroupBackupInfo, _Mapping]] = ..., end_backup_info: _Optional[_Union[EndBackupInfo, _Mapping]] = ...) -> None: ...

class ReadConfigInfo(_message.Message):
    __slots__ = ("config_path",)
    CONFIG_PATH_FIELD_NUMBER: _ClassVar[int]
    config_path: str
    def __init__(self, config_path: _Optional[str] = ...) -> None: ...

class RestoreGroupArg(_message.Message):
    __slots__ = ("base", "type", "read_config_info")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kReadConfig: _ClassVar[RestoreGroupArg.Type]
    kReadConfig: RestoreGroupArg.Type
    BASE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    READ_CONFIG_INFO_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_actions_pb2.RestoreBaseArg
    type: RestoreGroupArg.Type
    read_config_info: ReadConfigInfo
    def __init__(self, base: _Optional[_Union[_magneto_actions_pb2.RestoreBaseArg, _Mapping]] = ..., type: _Optional[_Union[RestoreGroupArg.Type, str]] = ..., read_config_info: _Optional[_Union[ReadConfigInfo, _Mapping]] = ...) -> None: ...

class GroupActionArg(_message.Message):
    __slots__ = ("task_id", "sub_task_id", "backup_group_arg", "restore_group_arg")
    GROUP_ACTION_ARG_FIELD_NUMBER: _ClassVar[int]
    group_action_arg: _descriptor.FieldDescriptor
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    SUB_TASK_ID_FIELD_NUMBER: _ClassVar[int]
    BACKUP_GROUP_ARG_FIELD_NUMBER: _ClassVar[int]
    RESTORE_GROUP_ARG_FIELD_NUMBER: _ClassVar[int]
    task_id: int
    sub_task_id: int
    backup_group_arg: BackupGroupArg
    restore_group_arg: RestoreGroupArg
    def __init__(self, task_id: _Optional[int] = ..., sub_task_id: _Optional[int] = ..., backup_group_arg: _Optional[_Union[BackupGroupArg, _Mapping]] = ..., restore_group_arg: _Optional[_Union[RestoreGroupArg, _Mapping]] = ...) -> None: ...
