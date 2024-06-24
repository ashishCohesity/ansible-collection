from bridge.magneto.base import magneto_actions_pb2 as _magneto_actions_pb2
from magneto.base.entities import o365_pb2 as _o365_pb2
from magneto.connectors.o365 import o365_pb2 as _o365_pb2_1
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PrepareTeamsBackupInfo(_message.Message):
    __slots__ = ("view_cloning_enabled", "should_recursively_clone_dir", "skip_channel_site_deletion", "teams_private_channel_site_id_vec")
    VIEW_CLONING_ENABLED_FIELD_NUMBER: _ClassVar[int]
    SHOULD_RECURSIVELY_CLONE_DIR_FIELD_NUMBER: _ClassVar[int]
    SKIP_CHANNEL_SITE_DELETION_FIELD_NUMBER: _ClassVar[int]
    TEAMS_PRIVATE_CHANNEL_SITE_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    view_cloning_enabled: bool
    should_recursively_clone_dir: bool
    skip_channel_site_deletion: bool
    teams_private_channel_site_id_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, view_cloning_enabled: bool = ..., should_recursively_clone_dir: bool = ..., skip_channel_site_deletion: bool = ..., teams_private_channel_site_id_vec: _Optional[_Iterable[str]] = ...) -> None: ...

class EndTeamsBackupInfo(_message.Message):
    __slots__ = ("teams_config", "cleanup_on_failure")
    TEAMS_CONFIG_FIELD_NUMBER: _ClassVar[int]
    CLEANUP_ON_FAILURE_FIELD_NUMBER: _ClassVar[int]
    teams_config: _o365_pb2_1.TeamsSparseConfig
    cleanup_on_failure: bool
    def __init__(self, teams_config: _Optional[_Union[_o365_pb2_1.TeamsSparseConfig, _Mapping]] = ..., cleanup_on_failure: bool = ...) -> None: ...

class BackupTeamsArg(_message.Message):
    __slots__ = ("base", "type", "root_entity", "teams_entity", "prepare_teams_backup_info", "end_teams_backup_info")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kPrepareTeamsBackup: _ClassVar[BackupTeamsArg.Type]
        kEndTeamsBackup: _ClassVar[BackupTeamsArg.Type]
    kPrepareTeamsBackup: BackupTeamsArg.Type
    kEndTeamsBackup: BackupTeamsArg.Type
    BASE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ROOT_ENTITY_FIELD_NUMBER: _ClassVar[int]
    TEAMS_ENTITY_FIELD_NUMBER: _ClassVar[int]
    PREPARE_TEAMS_BACKUP_INFO_FIELD_NUMBER: _ClassVar[int]
    END_TEAMS_BACKUP_INFO_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_actions_pb2.BackupBaseArg
    type: BackupTeamsArg.Type
    root_entity: _o365_pb2.Entity
    teams_entity: _o365_pb2.Entity
    prepare_teams_backup_info: PrepareTeamsBackupInfo
    end_teams_backup_info: EndTeamsBackupInfo
    def __init__(self, base: _Optional[_Union[_magneto_actions_pb2.BackupBaseArg, _Mapping]] = ..., type: _Optional[_Union[BackupTeamsArg.Type, str]] = ..., root_entity: _Optional[_Union[_o365_pb2.Entity, _Mapping]] = ..., teams_entity: _Optional[_Union[_o365_pb2.Entity, _Mapping]] = ..., prepare_teams_backup_info: _Optional[_Union[PrepareTeamsBackupInfo, _Mapping]] = ..., end_teams_backup_info: _Optional[_Union[EndTeamsBackupInfo, _Mapping]] = ...) -> None: ...

class GetTeamsConfig(_message.Message):
    __slots__ = ("config_path",)
    CONFIG_PATH_FIELD_NUMBER: _ClassVar[int]
    config_path: str
    def __init__(self, config_path: _Optional[str] = ...) -> None: ...

class RestoreTeamsArg(_message.Message):
    __slots__ = ("base", "type", "get_teams_config")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kGetTeamsInfo: _ClassVar[RestoreTeamsArg.Type]
    kGetTeamsInfo: RestoreTeamsArg.Type
    BASE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    GET_TEAMS_CONFIG_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_actions_pb2.RestoreBaseArg
    type: RestoreTeamsArg.Type
    get_teams_config: GetTeamsConfig
    def __init__(self, base: _Optional[_Union[_magneto_actions_pb2.RestoreBaseArg, _Mapping]] = ..., type: _Optional[_Union[RestoreTeamsArg.Type, str]] = ..., get_teams_config: _Optional[_Union[GetTeamsConfig, _Mapping]] = ...) -> None: ...

class TeamsActionArg(_message.Message):
    __slots__ = ("task_id", "sub_task_id", "backup_teams_arg", "restore_teams_arg")
    TEAMS_ACTION_ARG_FIELD_NUMBER: _ClassVar[int]
    teams_action_arg: _descriptor.FieldDescriptor
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    SUB_TASK_ID_FIELD_NUMBER: _ClassVar[int]
    BACKUP_TEAMS_ARG_FIELD_NUMBER: _ClassVar[int]
    RESTORE_TEAMS_ARG_FIELD_NUMBER: _ClassVar[int]
    task_id: int
    sub_task_id: int
    backup_teams_arg: BackupTeamsArg
    restore_teams_arg: RestoreTeamsArg
    def __init__(self, task_id: _Optional[int] = ..., sub_task_id: _Optional[int] = ..., backup_teams_arg: _Optional[_Union[BackupTeamsArg, _Mapping]] = ..., restore_teams_arg: _Optional[_Union[RestoreTeamsArg, _Mapping]] = ...) -> None: ...
