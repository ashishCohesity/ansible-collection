from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UdaCustomArgument(_message.Message):
    __slots__ = ("value", "encrypted_value")
    VALUE_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTED_VALUE_FIELD_NUMBER: _ClassVar[int]
    value: str
    encrypted_value: bytes
    def __init__(self, value: _Optional[str] = ..., encrypted_value: _Optional[bytes] = ...) -> None: ...

class UdaBackupSourceParamsProto(_message.Message):
    __slots__ = ("excluded_object_ids_vec",)
    EXCLUDED_OBJECT_IDS_VEC_FIELD_NUMBER: _ClassVar[int]
    excluded_object_ids_vec: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, excluded_object_ids_vec: _Optional[_Iterable[int]] = ...) -> None: ...

class EnvBackupParamsProto(_message.Message):
    __slots__ = ("backup_job_arguments_map", "concurrency", "mounts", "full_backup_args", "incremental_backup_args", "log_backup_args")
    class BackupJobArgumentsMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: UdaCustomArgument
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[UdaCustomArgument, _Mapping]] = ...) -> None: ...
    BACKUP_JOB_ARGUMENTS_MAP_FIELD_NUMBER: _ClassVar[int]
    CONCURRENCY_FIELD_NUMBER: _ClassVar[int]
    MOUNTS_FIELD_NUMBER: _ClassVar[int]
    FULL_BACKUP_ARGS_FIELD_NUMBER: _ClassVar[int]
    INCREMENTAL_BACKUP_ARGS_FIELD_NUMBER: _ClassVar[int]
    LOG_BACKUP_ARGS_FIELD_NUMBER: _ClassVar[int]
    backup_job_arguments_map: _containers.MessageMap[str, UdaCustomArgument]
    concurrency: int
    mounts: int
    full_backup_args: str
    incremental_backup_args: str
    log_backup_args: str
    def __init__(self, backup_job_arguments_map: _Optional[_Mapping[str, UdaCustomArgument]] = ..., concurrency: _Optional[int] = ..., mounts: _Optional[int] = ..., full_backup_args: _Optional[str] = ..., incremental_backup_args: _Optional[str] = ..., log_backup_args: _Optional[str] = ...) -> None: ...
