from bridge.magneto.base import magneto_actions_pb2 as _magneto_actions_pb2
from magneto.base.entities import o365_pb2 as _o365_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PrepareO365BackupInfo(_message.Message):
    __slots__ = ("view_cloning_enabled", "should_recursively_clone_dir", "delete_entire_mailbox_dir", "dir_to_be_renamed", "first_time_view_clone", "forward_upgrade_data_layout", "backward_upgrade_data_layout", "new_mailbox_guid", "skip_data_dir_while_cloning")
    VIEW_CLONING_ENABLED_FIELD_NUMBER: _ClassVar[int]
    SHOULD_RECURSIVELY_CLONE_DIR_FIELD_NUMBER: _ClassVar[int]
    DELETE_ENTIRE_MAILBOX_DIR_FIELD_NUMBER: _ClassVar[int]
    DIR_TO_BE_RENAMED_FIELD_NUMBER: _ClassVar[int]
    FIRST_TIME_VIEW_CLONE_FIELD_NUMBER: _ClassVar[int]
    FORWARD_UPGRADE_DATA_LAYOUT_FIELD_NUMBER: _ClassVar[int]
    BACKWARD_UPGRADE_DATA_LAYOUT_FIELD_NUMBER: _ClassVar[int]
    NEW_MAILBOX_GUID_FIELD_NUMBER: _ClassVar[int]
    SKIP_DATA_DIR_WHILE_CLONING_FIELD_NUMBER: _ClassVar[int]
    view_cloning_enabled: bool
    should_recursively_clone_dir: bool
    delete_entire_mailbox_dir: bool
    dir_to_be_renamed: str
    first_time_view_clone: bool
    forward_upgrade_data_layout: bool
    backward_upgrade_data_layout: bool
    new_mailbox_guid: str
    skip_data_dir_while_cloning: bool
    def __init__(self, view_cloning_enabled: bool = ..., should_recursively_clone_dir: bool = ..., delete_entire_mailbox_dir: bool = ..., dir_to_be_renamed: _Optional[str] = ..., first_time_view_clone: bool = ..., forward_upgrade_data_layout: bool = ..., backward_upgrade_data_layout: bool = ..., new_mailbox_guid: _Optional[str] = ..., skip_data_dir_while_cloning: bool = ...) -> None: ...

class BackupO365Arg(_message.Message):
    __slots__ = ("base", "type", "root_entity", "user_entity", "prepare_o365_backup_info")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kPrepareO365Backup: _ClassVar[BackupO365Arg.Type]
    kPrepareO365Backup: BackupO365Arg.Type
    BASE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ROOT_ENTITY_FIELD_NUMBER: _ClassVar[int]
    USER_ENTITY_FIELD_NUMBER: _ClassVar[int]
    PREPARE_O365_BACKUP_INFO_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_actions_pb2.BackupBaseArg
    type: BackupO365Arg.Type
    root_entity: _o365_pb2.Entity
    user_entity: _o365_pb2.Entity
    prepare_o365_backup_info: PrepareO365BackupInfo
    def __init__(self, base: _Optional[_Union[_magneto_actions_pb2.BackupBaseArg, _Mapping]] = ..., type: _Optional[_Union[BackupO365Arg.Type, str]] = ..., root_entity: _Optional[_Union[_o365_pb2.Entity, _Mapping]] = ..., user_entity: _Optional[_Union[_o365_pb2.Entity, _Mapping]] = ..., prepare_o365_backup_info: _Optional[_Union[PrepareO365BackupInfo, _Mapping]] = ...) -> None: ...

class RestoreO365Arg(_message.Message):
    __slots__ = ("base", "type")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kO365RestoreCloneView: _ClassVar[RestoreO365Arg.Type]
    kO365RestoreCloneView: RestoreO365Arg.Type
    BASE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_actions_pb2.RestoreBaseArg
    type: RestoreO365Arg.Type
    def __init__(self, base: _Optional[_Union[_magneto_actions_pb2.RestoreBaseArg, _Mapping]] = ..., type: _Optional[_Union[RestoreO365Arg.Type, str]] = ...) -> None: ...

class Cancelo365Arg(_message.Message):
    __slots__ = ("respond_after_draining", "dead_slave_constituent_id", "dead_slave_incarnation_id", "task_id")
    RESPOND_AFTER_DRAINING_FIELD_NUMBER: _ClassVar[int]
    DEAD_SLAVE_CONSTITUENT_ID_FIELD_NUMBER: _ClassVar[int]
    DEAD_SLAVE_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    respond_after_draining: bool
    dead_slave_constituent_id: int
    dead_slave_incarnation_id: int
    task_id: int
    def __init__(self, respond_after_draining: bool = ..., dead_slave_constituent_id: _Optional[int] = ..., dead_slave_incarnation_id: _Optional[int] = ..., task_id: _Optional[int] = ...) -> None: ...

class O365ActionArg(_message.Message):
    __slots__ = ("task_id", "sub_task_id", "backup_o365_arg", "restore_o365_arg", "cancel_o365_arg")
    O365_ACTION_ARG_FIELD_NUMBER: _ClassVar[int]
    o365_action_arg: _descriptor.FieldDescriptor
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    SUB_TASK_ID_FIELD_NUMBER: _ClassVar[int]
    BACKUP_O365_ARG_FIELD_NUMBER: _ClassVar[int]
    RESTORE_O365_ARG_FIELD_NUMBER: _ClassVar[int]
    CANCEL_O365_ARG_FIELD_NUMBER: _ClassVar[int]
    task_id: int
    sub_task_id: int
    backup_o365_arg: BackupO365Arg
    restore_o365_arg: RestoreO365Arg
    cancel_o365_arg: Cancelo365Arg
    def __init__(self, task_id: _Optional[int] = ..., sub_task_id: _Optional[int] = ..., backup_o365_arg: _Optional[_Union[BackupO365Arg, _Mapping]] = ..., restore_o365_arg: _Optional[_Union[RestoreO365Arg, _Mapping]] = ..., cancel_o365_arg: _Optional[_Union[Cancelo365Arg, _Mapping]] = ...) -> None: ...
