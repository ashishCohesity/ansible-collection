from magneto.slave.stub import bridge_updates_pb2 as _bridge_updates_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PrepareO365BackupUpdateArg(_message.Message):
    __slots__ = ("updated_mailbox_guid_path",)
    UPDATED_MAILBOX_GUID_PATH_FIELD_NUMBER: _ClassVar[int]
    updated_mailbox_guid_path: bool
    def __init__(self, updated_mailbox_guid_path: bool = ...) -> None: ...

class O365ActionUpdateArg(_message.Message):
    __slots__ = ("type", "prepare_o365_backup_update_arg")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kPrepareO365BackupUpdate: _ClassVar[O365ActionUpdateArg.Type]
    kPrepareO365BackupUpdate: O365ActionUpdateArg.Type
    O365_ACTION_UPDATE_ARG_FIELD_NUMBER: _ClassVar[int]
    o365_action_update_arg: _descriptor.FieldDescriptor
    TYPE_FIELD_NUMBER: _ClassVar[int]
    PREPARE_O365_BACKUP_UPDATE_ARG_FIELD_NUMBER: _ClassVar[int]
    type: O365ActionUpdateArg.Type
    prepare_o365_backup_update_arg: PrepareO365BackupUpdateArg
    def __init__(self, type: _Optional[_Union[O365ActionUpdateArg.Type, str]] = ..., prepare_o365_backup_update_arg: _Optional[_Union[PrepareO365BackupUpdateArg, _Mapping]] = ...) -> None: ...
