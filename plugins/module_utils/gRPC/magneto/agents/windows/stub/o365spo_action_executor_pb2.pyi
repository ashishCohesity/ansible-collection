from magneto.agents.windows.o365spo import o365spo_pb2 as _o365spo_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class O365SPOActionType(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kVerifyO365SPOConnectivity: _ClassVar[O365SPOActionType.Type]
        kBackupSite: _ClassVar[O365SPOActionType.Type]
        kRestoreSite: _ClassVar[O365SPOActionType.Type]
        kGetProgress: _ClassVar[O365SPOActionType.Type]
        kGetBackupSiteOutput: _ClassVar[O365SPOActionType.Type]
        kGetRestoreSiteOutput: _ClassVar[O365SPOActionType.Type]
        kDeleteSite: _ClassVar[O365SPOActionType.Type]
        kCleanUp: _ClassVar[O365SPOActionType.Type]
        kCancelTask: _ClassVar[O365SPOActionType.Type]
        kGetVerifyConnOutput: _ClassVar[O365SPOActionType.Type]
    kVerifyO365SPOConnectivity: O365SPOActionType.Type
    kBackupSite: O365SPOActionType.Type
    kRestoreSite: O365SPOActionType.Type
    kGetProgress: O365SPOActionType.Type
    kGetBackupSiteOutput: O365SPOActionType.Type
    kGetRestoreSiteOutput: O365SPOActionType.Type
    kDeleteSite: O365SPOActionType.Type
    kCleanUp: O365SPOActionType.Type
    kCancelTask: O365SPOActionType.Type
    kGetVerifyConnOutput: O365SPOActionType.Type
    def __init__(self) -> None: ...

class ExecuteO365SPOActionArg(_message.Message):
    __slots__ = ("action_type", "timeout_sec", "num_retries", "verify_connectivity_arg", "backup_site_arg", "restore_site_arg", "get_progress_arg", "get_backup_output_arg", "get_restore_output_arg", "delete_site_arg", "cleanup_arg", "cancel_task_arg", "get_verifyconn_output_arg")
    ACTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_SEC_FIELD_NUMBER: _ClassVar[int]
    NUM_RETRIES_FIELD_NUMBER: _ClassVar[int]
    VERIFY_CONNECTIVITY_ARG_FIELD_NUMBER: _ClassVar[int]
    BACKUP_SITE_ARG_FIELD_NUMBER: _ClassVar[int]
    RESTORE_SITE_ARG_FIELD_NUMBER: _ClassVar[int]
    GET_PROGRESS_ARG_FIELD_NUMBER: _ClassVar[int]
    GET_BACKUP_OUTPUT_ARG_FIELD_NUMBER: _ClassVar[int]
    GET_RESTORE_OUTPUT_ARG_FIELD_NUMBER: _ClassVar[int]
    DELETE_SITE_ARG_FIELD_NUMBER: _ClassVar[int]
    CLEANUP_ARG_FIELD_NUMBER: _ClassVar[int]
    CANCEL_TASK_ARG_FIELD_NUMBER: _ClassVar[int]
    GET_VERIFYCONN_OUTPUT_ARG_FIELD_NUMBER: _ClassVar[int]
    action_type: O365SPOActionType.Type
    timeout_sec: int
    num_retries: int
    verify_connectivity_arg: _o365spo_pb2.VerifyConnectivityArg
    backup_site_arg: _o365spo_pb2.BackupSiteArg
    restore_site_arg: _o365spo_pb2.RestoreSiteArg
    get_progress_arg: _o365spo_pb2.GetProgressArg
    get_backup_output_arg: _o365spo_pb2.GetBackupSiteOutputArg
    get_restore_output_arg: _o365spo_pb2.GetRestoreSiteOutputArg
    delete_site_arg: _o365spo_pb2.DeleteSiteArg
    cleanup_arg: _o365spo_pb2.CleanupArg
    cancel_task_arg: _o365spo_pb2.CancelTaskArg
    get_verifyconn_output_arg: _o365spo_pb2.GetVerifyConnOutputArg
    def __init__(self, action_type: _Optional[_Union[O365SPOActionType.Type, str]] = ..., timeout_sec: _Optional[int] = ..., num_retries: _Optional[int] = ..., verify_connectivity_arg: _Optional[_Union[_o365spo_pb2.VerifyConnectivityArg, _Mapping]] = ..., backup_site_arg: _Optional[_Union[_o365spo_pb2.BackupSiteArg, _Mapping]] = ..., restore_site_arg: _Optional[_Union[_o365spo_pb2.RestoreSiteArg, _Mapping]] = ..., get_progress_arg: _Optional[_Union[_o365spo_pb2.GetProgressArg, _Mapping]] = ..., get_backup_output_arg: _Optional[_Union[_o365spo_pb2.GetBackupSiteOutputArg, _Mapping]] = ..., get_restore_output_arg: _Optional[_Union[_o365spo_pb2.GetRestoreSiteOutputArg, _Mapping]] = ..., delete_site_arg: _Optional[_Union[_o365spo_pb2.DeleteSiteArg, _Mapping]] = ..., cleanup_arg: _Optional[_Union[_o365spo_pb2.CleanupArg, _Mapping]] = ..., cancel_task_arg: _Optional[_Union[_o365spo_pb2.CancelTaskArg, _Mapping]] = ..., get_verifyconn_output_arg: _Optional[_Union[_o365spo_pb2.GetVerifyConnOutputArg, _Mapping]] = ...) -> None: ...

class ExecuteO365SPOActionResult(_message.Message):
    __slots__ = ("action_type", "verify_connectivity_result", "backup_site_result", "restore_site_result", "get_progress_result", "get_backup_output_result", "get_restore_output_result", "delete_site_result", "cleanup_result", "cancel_task_result", "get_verifyconn_output_result")
    ACTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    VERIFY_CONNECTIVITY_RESULT_FIELD_NUMBER: _ClassVar[int]
    BACKUP_SITE_RESULT_FIELD_NUMBER: _ClassVar[int]
    RESTORE_SITE_RESULT_FIELD_NUMBER: _ClassVar[int]
    GET_PROGRESS_RESULT_FIELD_NUMBER: _ClassVar[int]
    GET_BACKUP_OUTPUT_RESULT_FIELD_NUMBER: _ClassVar[int]
    GET_RESTORE_OUTPUT_RESULT_FIELD_NUMBER: _ClassVar[int]
    DELETE_SITE_RESULT_FIELD_NUMBER: _ClassVar[int]
    CLEANUP_RESULT_FIELD_NUMBER: _ClassVar[int]
    CANCEL_TASK_RESULT_FIELD_NUMBER: _ClassVar[int]
    GET_VERIFYCONN_OUTPUT_RESULT_FIELD_NUMBER: _ClassVar[int]
    action_type: O365SPOActionType.Type
    verify_connectivity_result: _o365spo_pb2.VerifyConnectivityResult
    backup_site_result: _o365spo_pb2.BackupSiteResult
    restore_site_result: _o365spo_pb2.RestoreSiteResult
    get_progress_result: _o365spo_pb2.GetProgressResult
    get_backup_output_result: _o365spo_pb2.GetBackupSiteOutputResult
    get_restore_output_result: _o365spo_pb2.GetRestoreSiteOutputResult
    delete_site_result: _o365spo_pb2.DeleteSiteResult
    cleanup_result: _o365spo_pb2.CleanupResult
    cancel_task_result: _o365spo_pb2.CancelTaskResult
    get_verifyconn_output_result: _o365spo_pb2.GetVerifyConnResult
    def __init__(self, action_type: _Optional[_Union[O365SPOActionType.Type, str]] = ..., verify_connectivity_result: _Optional[_Union[_o365spo_pb2.VerifyConnectivityResult, _Mapping]] = ..., backup_site_result: _Optional[_Union[_o365spo_pb2.BackupSiteResult, _Mapping]] = ..., restore_site_result: _Optional[_Union[_o365spo_pb2.RestoreSiteResult, _Mapping]] = ..., get_progress_result: _Optional[_Union[_o365spo_pb2.GetProgressResult, _Mapping]] = ..., get_backup_output_result: _Optional[_Union[_o365spo_pb2.GetBackupSiteOutputResult, _Mapping]] = ..., get_restore_output_result: _Optional[_Union[_o365spo_pb2.GetRestoreSiteOutputResult, _Mapping]] = ..., delete_site_result: _Optional[_Union[_o365spo_pb2.DeleteSiteResult, _Mapping]] = ..., cleanup_result: _Optional[_Union[_o365spo_pb2.CleanupResult, _Mapping]] = ..., cancel_task_result: _Optional[_Union[_o365spo_pb2.CancelTaskResult, _Mapping]] = ..., get_verifyconn_output_result: _Optional[_Union[_o365spo_pb2.GetVerifyConnResult, _Mapping]] = ...) -> None: ...
