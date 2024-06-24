from magneto.base import error_pb2 as _error_pb2
from magneto.base import magneto_pb2 as _magneto_pb2
from magneto.base import env_params_pb2 as _env_params_pb2
from nexus.cloud.connectors.aws import rds_params_pb2 as _rds_params_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class OracleRmanSnapshotInfo(_message.Message):
    __slots__ = ("status", "job_instance_id", "attempt_num", "error", "db_info")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kStarted: _ClassVar[OracleRmanSnapshotInfo.Status]
        kDBInfoFetched: _ClassVar[OracleRmanSnapshotInfo.Status]
        kPermitGranted: _ClassVar[OracleRmanSnapshotInfo.Status]
        kCompleted: _ClassVar[OracleRmanSnapshotInfo.Status]
    kStarted: OracleRmanSnapshotInfo.Status
    kDBInfoFetched: OracleRmanSnapshotInfo.Status
    kPermitGranted: OracleRmanSnapshotInfo.Status
    kCompleted: OracleRmanSnapshotInfo.Status
    RDS_ORACLE_RMAN_SNAPSHOT_INFO_FIELD_NUMBER: _ClassVar[int]
    rds_oracle_rman_snapshot_info: _descriptor.FieldDescriptor
    STATUS_FIELD_NUMBER: _ClassVar[int]
    JOB_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    ATTEMPT_NUM_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    DB_INFO_FIELD_NUMBER: _ClassVar[int]
    status: OracleRmanSnapshotInfo.Status
    job_instance_id: int
    attempt_num: int
    error: _error_pb2.ErrorProto
    db_info: _rds_params_pb2.DBInfo
    def __init__(self, status: _Optional[_Union[OracleRmanSnapshotInfo.Status, str]] = ..., job_instance_id: _Optional[int] = ..., attempt_num: _Optional[int] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., db_info: _Optional[_Union[_rds_params_pb2.DBInfo, _Mapping]] = ...) -> None: ...
