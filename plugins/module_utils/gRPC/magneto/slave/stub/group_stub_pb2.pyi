from magneto.connectors.o365 import o365_pb2 as _o365_pb2
from magneto.slave.stub import bridge_updates_pb2 as _bridge_updates_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PrepareGroupBackupUpdateArg(_message.Message):
    __slots__ = ("group_config_file",)
    GROUP_CONFIG_FILE_FIELD_NUMBER: _ClassVar[int]
    group_config_file: _o365_pb2.O365GroupSparseConfig
    def __init__(self, group_config_file: _Optional[_Union[_o365_pb2.O365GroupSparseConfig, _Mapping]] = ...) -> None: ...

class EndBackupUpdateArg(_message.Message):
    __slots__ = ("config_file_written", "is_cleanup_successful")
    CONFIG_FILE_WRITTEN_FIELD_NUMBER: _ClassVar[int]
    IS_CLEANUP_SUCCESSFUL_FIELD_NUMBER: _ClassVar[int]
    config_file_written: bool
    is_cleanup_successful: bool
    def __init__(self, config_file_written: bool = ..., is_cleanup_successful: bool = ...) -> None: ...

class ReadConfigUpdateArg(_message.Message):
    __slots__ = ("group_config_file",)
    GROUP_CONFIG_FILE_FIELD_NUMBER: _ClassVar[int]
    group_config_file: _o365_pb2.O365GroupSparseConfig
    def __init__(self, group_config_file: _Optional[_Union[_o365_pb2.O365GroupSparseConfig, _Mapping]] = ...) -> None: ...

class GroupActionUpdateArg(_message.Message):
    __slots__ = ("type", "prepare_group_backup_update_arg", "end_backup_update_arg", "read_config_update_arg")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kPrepareGroupBackupUpdate: _ClassVar[GroupActionUpdateArg.Type]
        kEndBackupUpdate: _ClassVar[GroupActionUpdateArg.Type]
        kReadConfigUpdate: _ClassVar[GroupActionUpdateArg.Type]
    kPrepareGroupBackupUpdate: GroupActionUpdateArg.Type
    kEndBackupUpdate: GroupActionUpdateArg.Type
    kReadConfigUpdate: GroupActionUpdateArg.Type
    GROUP_ACTION_UPDATE_ARG_FIELD_NUMBER: _ClassVar[int]
    group_action_update_arg: _descriptor.FieldDescriptor
    TYPE_FIELD_NUMBER: _ClassVar[int]
    PREPARE_GROUP_BACKUP_UPDATE_ARG_FIELD_NUMBER: _ClassVar[int]
    END_BACKUP_UPDATE_ARG_FIELD_NUMBER: _ClassVar[int]
    READ_CONFIG_UPDATE_ARG_FIELD_NUMBER: _ClassVar[int]
    type: GroupActionUpdateArg.Type
    prepare_group_backup_update_arg: PrepareGroupBackupUpdateArg
    end_backup_update_arg: EndBackupUpdateArg
    read_config_update_arg: ReadConfigUpdateArg
    def __init__(self, type: _Optional[_Union[GroupActionUpdateArg.Type, str]] = ..., prepare_group_backup_update_arg: _Optional[_Union[PrepareGroupBackupUpdateArg, _Mapping]] = ..., end_backup_update_arg: _Optional[_Union[EndBackupUpdateArg, _Mapping]] = ..., read_config_update_arg: _Optional[_Union[ReadConfigUpdateArg, _Mapping]] = ...) -> None: ...
