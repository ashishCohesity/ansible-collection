from bridge.magneto.base import magneto_actions_pb2 as _magneto_actions_pb2
from magneto.base import magneto_pb2 as _magneto_pb2
from magneto.base import env_params_pb2 as _env_params_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ApplyLogFilesToDiskArg(_message.Message):
    __slots__ = ("dst_parent_dir_path", "disk_logs", "end_timestamp_usecs", "cdp_perform_two_pass_logs_read")
    DST_PARENT_DIR_PATH_FIELD_NUMBER: _ClassVar[int]
    DISK_LOGS_FIELD_NUMBER: _ClassVar[int]
    END_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
    CDP_PERFORM_TWO_PASS_LOGS_READ_FIELD_NUMBER: _ClassVar[int]
    dst_parent_dir_path: str
    disk_logs: _magneto_pb2.CdpHydrationParams.DiskLog
    end_timestamp_usecs: int
    cdp_perform_two_pass_logs_read: bool
    def __init__(self, dst_parent_dir_path: _Optional[str] = ..., disk_logs: _Optional[_Union[_magneto_pb2.CdpHydrationParams.DiskLog, _Mapping]] = ..., end_timestamp_usecs: _Optional[int] = ..., cdp_perform_two_pass_logs_read: bool = ...) -> None: ...

class CDPActionArg(_message.Message):
    __slots__ = ("task_id", "is_using_bifrost", "type", "apply_log_files_to_disk_arg", "stats_container_id", "cancel_task_arg")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kApplyLogFilesToDisk: _ClassVar[CDPActionArg.Type]
        kCancel: _ClassVar[CDPActionArg.Type]
    kApplyLogFilesToDisk: CDPActionArg.Type
    kCancel: CDPActionArg.Type
    CDP_ACTION_ARG_FIELD_NUMBER: _ClassVar[int]
    cdp_action_arg: _descriptor.FieldDescriptor
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    IS_USING_BIFROST_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    APPLY_LOG_FILES_TO_DISK_ARG_FIELD_NUMBER: _ClassVar[int]
    STATS_CONTAINER_ID_FIELD_NUMBER: _ClassVar[int]
    CANCEL_TASK_ARG_FIELD_NUMBER: _ClassVar[int]
    task_id: int
    is_using_bifrost: bool
    type: CDPActionArg.Type
    apply_log_files_to_disk_arg: ApplyLogFilesToDiskArg
    stats_container_id: int
    cancel_task_arg: _magneto_actions_pb2.CancelTaskArg
    def __init__(self, task_id: _Optional[int] = ..., is_using_bifrost: bool = ..., type: _Optional[_Union[CDPActionArg.Type, str]] = ..., apply_log_files_to_disk_arg: _Optional[_Union[ApplyLogFilesToDiskArg, _Mapping]] = ..., stats_container_id: _Optional[int] = ..., cancel_task_arg: _Optional[_Union[_magneto_actions_pb2.CancelTaskArg, _Mapping]] = ...) -> None: ...
