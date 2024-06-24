from magneto.base import enums_pb2 as _enums_pb2
from magneto.base import error_pb2 as _error_pb2
from magneto.master.base import enums_pb2 as _enums_pb2_1
from magneto.master.base import master_pb2 as _master_pb2
from util.base import universal_id_pb2 as _universal_id_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BackupJobRunMetadataProto(_message.Message):
    __slots__ = ("job_uid", "job_instance_id", "status", "start_time_usecs", "end_time_usecs", "backup_type", "scribe_key_vec", "metadata_pruned", "metadata_deleted_timestamp_usecs", "error")
    JOB_UID_FIELD_NUMBER: _ClassVar[int]
    JOB_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    END_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    BACKUP_TYPE_FIELD_NUMBER: _ClassVar[int]
    SCRIBE_KEY_VEC_FIELD_NUMBER: _ClassVar[int]
    METADATA_PRUNED_FIELD_NUMBER: _ClassVar[int]
    METADATA_DELETED_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    job_uid: _universal_id_pb2.UniversalIdProto
    job_instance_id: int
    status: _enums_pb2_1.BackupJobTaskStatus
    start_time_usecs: int
    end_time_usecs: int
    backup_type: _enums_pb2.ScheduledBackupType.Type
    scribe_key_vec: _containers.RepeatedScalarFieldContainer[str]
    metadata_pruned: bool
    metadata_deleted_timestamp_usecs: int
    error: _error_pb2.ErrorProto
    def __init__(self, job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., job_instance_id: _Optional[int] = ..., status: _Optional[_Union[_enums_pb2_1.BackupJobTaskStatus, str]] = ..., start_time_usecs: _Optional[int] = ..., end_time_usecs: _Optional[int] = ..., backup_type: _Optional[_Union[_enums_pb2.ScheduledBackupType.Type, str]] = ..., scribe_key_vec: _Optional[_Iterable[str]] = ..., metadata_pruned: bool = ..., metadata_deleted_timestamp_usecs: _Optional[int] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class CopyRunShellProto(_message.Message):
    __slots__ = ("job_uid", "run_start_time_usecs", "copy_run_start_time_usecs", "is_out_of_band_run", "status", "serialized_proto_size")
    JOB_UID_FIELD_NUMBER: _ClassVar[int]
    RUN_START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    COPY_RUN_START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    IS_OUT_OF_BAND_RUN_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SERIALIZED_PROTO_SIZE_FIELD_NUMBER: _ClassVar[int]
    job_uid: _universal_id_pb2.UniversalIdProto
    run_start_time_usecs: int
    copy_run_start_time_usecs: int
    is_out_of_band_run: bool
    status: _master_pb2.CopyBackupRunStateProto.Status
    serialized_proto_size: int
    def __init__(self, job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., run_start_time_usecs: _Optional[int] = ..., copy_run_start_time_usecs: _Optional[int] = ..., is_out_of_band_run: bool = ..., status: _Optional[_Union[_master_pb2.CopyBackupRunStateProto.Status, str]] = ..., serialized_proto_size: _Optional[int] = ...) -> None: ...
