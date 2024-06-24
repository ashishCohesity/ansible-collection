from magneto.connectors.ms_graph import graph_pb2 as _graph_pb2
from magneto.connectors.o365 import o365_pb2 as _o365_pb2
from magneto.slave.stub import bridge_updates_pb2 as _bridge_updates_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PrepareSharepointBackupUpdateArg(_message.Message):
    __slots__ = ("sharepoint_config_file", "new_drive_vec")
    SHAREPOINT_CONFIG_FILE_FIELD_NUMBER: _ClassVar[int]
    NEW_DRIVE_VEC_FIELD_NUMBER: _ClassVar[int]
    sharepoint_config_file: _o365_pb2.SharepointSparseConfig
    new_drive_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, sharepoint_config_file: _Optional[_Union[_o365_pb2.SharepointSparseConfig, _Mapping]] = ..., new_drive_vec: _Optional[_Iterable[str]] = ...) -> None: ...

class SetupListsInfoUpdateArg(_message.Message):
    __slots__ = ("list_vec_to_backup",)
    LIST_VEC_TO_BACKUP_FIELD_NUMBER: _ClassVar[int]
    list_vec_to_backup: _containers.RepeatedCompositeFieldContainer[_graph_pb2.List]
    def __init__(self, list_vec_to_backup: _Optional[_Iterable[_Union[_graph_pb2.List, _Mapping]]] = ...) -> None: ...

class BackupListsUpdateArg(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class EndListsBackupUpdateArg(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class EndListsSubTaskUpdateArg(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class EndBackupUpdateArg(_message.Message):
    __slots__ = ("config_file_written", "is_cleanup_successful")
    CONFIG_FILE_WRITTEN_FIELD_NUMBER: _ClassVar[int]
    IS_CLEANUP_SUCCESSFUL_FIELD_NUMBER: _ClassVar[int]
    config_file_written: bool
    is_cleanup_successful: bool
    def __init__(self, config_file_written: bool = ..., is_cleanup_successful: bool = ...) -> None: ...

class SiteInfoUpdateArg(_message.Message):
    __slots__ = ("sharepoint_config",)
    SHAREPOINT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    sharepoint_config: _o365_pb2.SharepointSparseConfig
    def __init__(self, sharepoint_config: _Optional[_Union[_o365_pb2.SharepointSparseConfig, _Mapping]] = ...) -> None: ...

class SharepointActionUpdateArg(_message.Message):
    __slots__ = ("type", "prepare_sharepoint_backup_update_arg", "setup_lists_info_update_arg", "backup_lists_update_arg", "end_lists_backup_update_arg", "end_lists_sub_task_update_arg", "end_backup_update_arg", "site_info_update_arg")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kPrepareSharepointBackupUpdate: _ClassVar[SharepointActionUpdateArg.Type]
        kSetupListsInfoUpdate: _ClassVar[SharepointActionUpdateArg.Type]
        kBackupListsUpdate: _ClassVar[SharepointActionUpdateArg.Type]
        kEndListsBackupUpdate: _ClassVar[SharepointActionUpdateArg.Type]
        kEndListsSubTaskUpdate: _ClassVar[SharepointActionUpdateArg.Type]
        kEndBackupUpdate: _ClassVar[SharepointActionUpdateArg.Type]
        kSiteInfoUpdate: _ClassVar[SharepointActionUpdateArg.Type]
    kPrepareSharepointBackupUpdate: SharepointActionUpdateArg.Type
    kSetupListsInfoUpdate: SharepointActionUpdateArg.Type
    kBackupListsUpdate: SharepointActionUpdateArg.Type
    kEndListsBackupUpdate: SharepointActionUpdateArg.Type
    kEndListsSubTaskUpdate: SharepointActionUpdateArg.Type
    kEndBackupUpdate: SharepointActionUpdateArg.Type
    kSiteInfoUpdate: SharepointActionUpdateArg.Type
    SHAREPOINT_ACTION_UPDATE_ARG_FIELD_NUMBER: _ClassVar[int]
    sharepoint_action_update_arg: _descriptor.FieldDescriptor
    TYPE_FIELD_NUMBER: _ClassVar[int]
    PREPARE_SHAREPOINT_BACKUP_UPDATE_ARG_FIELD_NUMBER: _ClassVar[int]
    SETUP_LISTS_INFO_UPDATE_ARG_FIELD_NUMBER: _ClassVar[int]
    BACKUP_LISTS_UPDATE_ARG_FIELD_NUMBER: _ClassVar[int]
    END_LISTS_BACKUP_UPDATE_ARG_FIELD_NUMBER: _ClassVar[int]
    END_LISTS_SUB_TASK_UPDATE_ARG_FIELD_NUMBER: _ClassVar[int]
    END_BACKUP_UPDATE_ARG_FIELD_NUMBER: _ClassVar[int]
    SITE_INFO_UPDATE_ARG_FIELD_NUMBER: _ClassVar[int]
    type: SharepointActionUpdateArg.Type
    prepare_sharepoint_backup_update_arg: PrepareSharepointBackupUpdateArg
    setup_lists_info_update_arg: SetupListsInfoUpdateArg
    backup_lists_update_arg: BackupListsUpdateArg
    end_lists_backup_update_arg: EndListsBackupUpdateArg
    end_lists_sub_task_update_arg: EndListsSubTaskUpdateArg
    end_backup_update_arg: EndBackupUpdateArg
    site_info_update_arg: SiteInfoUpdateArg
    def __init__(self, type: _Optional[_Union[SharepointActionUpdateArg.Type, str]] = ..., prepare_sharepoint_backup_update_arg: _Optional[_Union[PrepareSharepointBackupUpdateArg, _Mapping]] = ..., setup_lists_info_update_arg: _Optional[_Union[SetupListsInfoUpdateArg, _Mapping]] = ..., backup_lists_update_arg: _Optional[_Union[BackupListsUpdateArg, _Mapping]] = ..., end_lists_backup_update_arg: _Optional[_Union[EndListsBackupUpdateArg, _Mapping]] = ..., end_lists_sub_task_update_arg: _Optional[_Union[EndListsSubTaskUpdateArg, _Mapping]] = ..., end_backup_update_arg: _Optional[_Union[EndBackupUpdateArg, _Mapping]] = ..., site_info_update_arg: _Optional[_Union[SiteInfoUpdateArg, _Mapping]] = ...) -> None: ...
