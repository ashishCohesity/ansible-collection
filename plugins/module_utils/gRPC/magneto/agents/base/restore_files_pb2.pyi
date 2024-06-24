from magneto.base import error_pb2 as _error_pb2
from magneto.base import magneto_pb2 as _magneto_pb2
from magneto.base import env_params_pb2 as _env_params_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RestoreUtilArg(_message.Message):
    __slots__ = ("task_id", "restored_file_info_vec", "attached_disk_id_vec", "attached_disk_unique_id_vec", "restore_files_preferences", "max_disk_online_wait_time_secs")
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    RESTORED_FILE_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    ATTACHED_DISK_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    ATTACHED_DISK_UNIQUE_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    RESTORE_FILES_PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    MAX_DISK_ONLINE_WAIT_TIME_SECS_FIELD_NUMBER: _ClassVar[int]
    task_id: int
    restored_file_info_vec: _containers.RepeatedCompositeFieldContainer[_magneto_pb2.RestoredFileInfo]
    attached_disk_id_vec: _containers.RepeatedScalarFieldContainer[int]
    attached_disk_unique_id_vec: _containers.RepeatedScalarFieldContainer[str]
    restore_files_preferences: _magneto_pb2.RestoreFilesPreferences
    max_disk_online_wait_time_secs: int
    def __init__(self, task_id: _Optional[int] = ..., restored_file_info_vec: _Optional[_Iterable[_Union[_magneto_pb2.RestoredFileInfo, _Mapping]]] = ..., attached_disk_id_vec: _Optional[_Iterable[int]] = ..., attached_disk_unique_id_vec: _Optional[_Iterable[str]] = ..., restore_files_preferences: _Optional[_Union[_magneto_pb2.RestoreFilesPreferences, _Mapping]] = ..., max_disk_online_wait_time_secs: _Optional[int] = ...) -> None: ...

class RestoreUtilResult(_message.Message):
    __slots__ = ("task_id", "error", "status", "restore_file_result_info_vec")
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    RESTORE_FILE_RESULT_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    task_id: int
    error: _error_pb2.ErrorProto
    status: _magneto_pb2.RestoreFileStatus.Type
    restore_file_result_info_vec: _containers.RepeatedCompositeFieldContainer[_magneto_pb2.RestoreFileResultInfo]
    def __init__(self, task_id: _Optional[int] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., status: _Optional[_Union[_magneto_pb2.RestoreFileStatus.Type, str]] = ..., restore_file_result_info_vec: _Optional[_Iterable[_Union[_magneto_pb2.RestoreFileResultInfo, _Mapping]]] = ...) -> None: ...

class RestoreUtilOnStartState(_message.Message):
    __slots__ = ("pid", "process_name", "admin_privileges_verified")
    PID_FIELD_NUMBER: _ClassVar[int]
    PROCESS_NAME_FIELD_NUMBER: _ClassVar[int]
    ADMIN_PRIVILEGES_VERIFIED_FIELD_NUMBER: _ClassVar[int]
    pid: int
    process_name: str
    admin_privileges_verified: bool
    def __init__(self, pid: _Optional[int] = ..., process_name: _Optional[str] = ..., admin_privileges_verified: bool = ...) -> None: ...
