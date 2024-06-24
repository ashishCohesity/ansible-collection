from magneto.slave.stub import bridge_updates_pb2 as _bridge_updates_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PreparePublicFolderBackupUpdateArg(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class EndBackupUpdateArg(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PublicFolderActionUpdateArg(_message.Message):
    __slots__ = ("type", "prepare_public_folder_backup_update_arg", "end_backup_update_arg")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kPreparePublicFolderBackupUpdate: _ClassVar[PublicFolderActionUpdateArg.Type]
        kEndBackupUpdate: _ClassVar[PublicFolderActionUpdateArg.Type]
    kPreparePublicFolderBackupUpdate: PublicFolderActionUpdateArg.Type
    kEndBackupUpdate: PublicFolderActionUpdateArg.Type
    PUBLIC_FOLDER_ACTION_UPDATE_ARG_FIELD_NUMBER: _ClassVar[int]
    public_folder_action_update_arg: _descriptor.FieldDescriptor
    TYPE_FIELD_NUMBER: _ClassVar[int]
    PREPARE_PUBLIC_FOLDER_BACKUP_UPDATE_ARG_FIELD_NUMBER: _ClassVar[int]
    END_BACKUP_UPDATE_ARG_FIELD_NUMBER: _ClassVar[int]
    type: PublicFolderActionUpdateArg.Type
    prepare_public_folder_backup_update_arg: PreparePublicFolderBackupUpdateArg
    end_backup_update_arg: EndBackupUpdateArg
    def __init__(self, type: _Optional[_Union[PublicFolderActionUpdateArg.Type, str]] = ..., prepare_public_folder_backup_update_arg: _Optional[_Union[PreparePublicFolderBackupUpdateArg, _Mapping]] = ..., end_backup_update_arg: _Optional[_Union[EndBackupUpdateArg, _Mapping]] = ...) -> None: ...
