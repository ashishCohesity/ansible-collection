from magneto.slave.stub import bridge_updates_pb2 as _bridge_updates_pb2
from magneto.connectors.o365 import o365_pb2 as _o365_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PrepareTeamsBackupUpdateArg(_message.Message):
    __slots__ = ("teams_config_file", "new_channel_site_id_vec")
    TEAMS_CONFIG_FILE_FIELD_NUMBER: _ClassVar[int]
    NEW_CHANNEL_SITE_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    teams_config_file: _o365_pb2.TeamsSparseConfig
    new_channel_site_id_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, teams_config_file: _Optional[_Union[_o365_pb2.TeamsSparseConfig, _Mapping]] = ..., new_channel_site_id_vec: _Optional[_Iterable[str]] = ...) -> None: ...

class EndTeamsBackupUpdateArg(_message.Message):
    __slots__ = ("config_file_written", "is_cleanup_successful")
    CONFIG_FILE_WRITTEN_FIELD_NUMBER: _ClassVar[int]
    IS_CLEANUP_SUCCESSFUL_FIELD_NUMBER: _ClassVar[int]
    config_file_written: bool
    is_cleanup_successful: bool
    def __init__(self, config_file_written: bool = ..., is_cleanup_successful: bool = ...) -> None: ...

class GetTeamsInfoUpdateArg(_message.Message):
    __slots__ = ("teams_config",)
    TEAMS_CONFIG_FIELD_NUMBER: _ClassVar[int]
    teams_config: _o365_pb2.TeamsSparseConfig
    def __init__(self, teams_config: _Optional[_Union[_o365_pb2.TeamsSparseConfig, _Mapping]] = ...) -> None: ...

class TeamsActionUpdateArg(_message.Message):
    __slots__ = ("type", "prepare_teams_backup_update_arg", "end_teams_backup_update_arg", "get_teams_info_update_arg")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kPrepareTeamsBackupUpdate: _ClassVar[TeamsActionUpdateArg.Type]
        kEndTeamsBackupUpdate: _ClassVar[TeamsActionUpdateArg.Type]
        kGetTeamsInfoUpdate: _ClassVar[TeamsActionUpdateArg.Type]
    kPrepareTeamsBackupUpdate: TeamsActionUpdateArg.Type
    kEndTeamsBackupUpdate: TeamsActionUpdateArg.Type
    kGetTeamsInfoUpdate: TeamsActionUpdateArg.Type
    TEAMS_ACTION_UPDATE_ARG_FIELD_NUMBER: _ClassVar[int]
    teams_action_update_arg: _descriptor.FieldDescriptor
    TYPE_FIELD_NUMBER: _ClassVar[int]
    PREPARE_TEAMS_BACKUP_UPDATE_ARG_FIELD_NUMBER: _ClassVar[int]
    END_TEAMS_BACKUP_UPDATE_ARG_FIELD_NUMBER: _ClassVar[int]
    GET_TEAMS_INFO_UPDATE_ARG_FIELD_NUMBER: _ClassVar[int]
    type: TeamsActionUpdateArg.Type
    prepare_teams_backup_update_arg: PrepareTeamsBackupUpdateArg
    end_teams_backup_update_arg: EndTeamsBackupUpdateArg
    get_teams_info_update_arg: GetTeamsInfoUpdateArg
    def __init__(self, type: _Optional[_Union[TeamsActionUpdateArg.Type, str]] = ..., prepare_teams_backup_update_arg: _Optional[_Union[PrepareTeamsBackupUpdateArg, _Mapping]] = ..., end_teams_backup_update_arg: _Optional[_Union[EndTeamsBackupUpdateArg, _Mapping]] = ..., get_teams_info_update_arg: _Optional[_Union[GetTeamsInfoUpdateArg, _Mapping]] = ...) -> None: ...
