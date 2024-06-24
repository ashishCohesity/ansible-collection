from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class MagnetoInstanceId(_message.Message):
    __slots__ = ("job_instance_id", "job_start_time_usecs", "attempt_num")
    JOB_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    JOB_START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    ATTEMPT_NUM_FIELD_NUMBER: _ClassVar[int]
    job_instance_id: int
    job_start_time_usecs: int
    attempt_num: int
    def __init__(self, job_instance_id: _Optional[int] = ..., job_start_time_usecs: _Optional[int] = ..., attempt_num: _Optional[int] = ...) -> None: ...

class DiskPartitionType(_message.Message):
    __slots__ = ()
    class PartitionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNoPartition: _ClassVar[DiskPartitionType.PartitionType]
        kMBRPartition: _ClassVar[DiskPartitionType.PartitionType]
        kGPTPartition: _ClassVar[DiskPartitionType.PartitionType]
        kSGIPartition: _ClassVar[DiskPartitionType.PartitionType]
        kSUNPartition: _ClassVar[DiskPartitionType.PartitionType]
    kNoPartition: DiskPartitionType.PartitionType
    kMBRPartition: DiskPartitionType.PartitionType
    kGPTPartition: DiskPartitionType.PartitionType
    kSGIPartition: DiskPartitionType.PartitionType
    kSUNPartition: DiskPartitionType.PartitionType
    def __init__(self) -> None: ...
