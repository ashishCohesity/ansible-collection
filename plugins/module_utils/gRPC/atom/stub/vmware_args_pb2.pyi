from atom.base import vmware_pb2 as _vmware_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class VMwareData(_message.Message):
    __slots__ = ("io_vec",)
    class IO(_message.Message):
        __slots__ = ("timestamp", "sequence_num", "offset", "data", "data_type", "snapshot_id", "disk_capacity", "snapshot_create_time_secs")
        TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
        SEQUENCE_NUM_FIELD_NUMBER: _ClassVar[int]
        OFFSET_FIELD_NUMBER: _ClassVar[int]
        DATA_FIELD_NUMBER: _ClassVar[int]
        DATA_TYPE_FIELD_NUMBER: _ClassVar[int]
        SNAPSHOT_ID_FIELD_NUMBER: _ClassVar[int]
        DISK_CAPACITY_FIELD_NUMBER: _ClassVar[int]
        SNAPSHOT_CREATE_TIME_SECS_FIELD_NUMBER: _ClassVar[int]
        timestamp: int
        sequence_num: _vmware_pb2.SequenceNumber
        offset: int
        data: bytes
        data_type: _vmware_pb2.DataType
        snapshot_id: int
        disk_capacity: int
        snapshot_create_time_secs: int
        def __init__(self, timestamp: _Optional[int] = ..., sequence_num: _Optional[_Union[_vmware_pb2.SequenceNumber, _Mapping]] = ..., offset: _Optional[int] = ..., data: _Optional[bytes] = ..., data_type: _Optional[_Union[_vmware_pb2.DataType, str]] = ..., snapshot_id: _Optional[int] = ..., disk_capacity: _Optional[int] = ..., snapshot_create_time_secs: _Optional[int] = ...) -> None: ...
    IO_VEC_FIELD_NUMBER: _ClassVar[int]
    io_vec: _containers.RepeatedCompositeFieldContainer[VMwareData.IO]
    def __init__(self, io_vec: _Optional[_Iterable[_Union[VMwareData.IO, _Mapping]]] = ...) -> None: ...
