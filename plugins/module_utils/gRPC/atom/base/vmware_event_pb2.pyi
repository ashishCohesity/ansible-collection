from atom.base import vmware_pb2 as _vmware_pb2
from atom.base import event_pb2 as _event_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class VMwareDataEvent(_message.Message):
    __slots__ = ("data_type", "start_seq_num", "end_seq_num", "start_time_usecs", "end_time_usecs", "snapshot_id", "disk_capacity", "snapshot_create_time_secs", "is_gap_filler")
    VMWARE_DATA_EVENT_FIELD_NUMBER: _ClassVar[int]
    vmware_data_event: _descriptor.FieldDescriptor
    DATA_TYPE_FIELD_NUMBER: _ClassVar[int]
    START_SEQ_NUM_FIELD_NUMBER: _ClassVar[int]
    END_SEQ_NUM_FIELD_NUMBER: _ClassVar[int]
    START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    END_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_ID_FIELD_NUMBER: _ClassVar[int]
    DISK_CAPACITY_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_CREATE_TIME_SECS_FIELD_NUMBER: _ClassVar[int]
    IS_GAP_FILLER_FIELD_NUMBER: _ClassVar[int]
    data_type: _vmware_pb2.DataType
    start_seq_num: _vmware_pb2.SequenceNumber
    end_seq_num: _vmware_pb2.SequenceNumber
    start_time_usecs: int
    end_time_usecs: int
    snapshot_id: int
    disk_capacity: int
    snapshot_create_time_secs: int
    is_gap_filler: bool
    def __init__(self, data_type: _Optional[_Union[_vmware_pb2.DataType, str]] = ..., start_seq_num: _Optional[_Union[_vmware_pb2.SequenceNumber, _Mapping]] = ..., end_seq_num: _Optional[_Union[_vmware_pb2.SequenceNumber, _Mapping]] = ..., start_time_usecs: _Optional[int] = ..., end_time_usecs: _Optional[int] = ..., snapshot_id: _Optional[int] = ..., disk_capacity: _Optional[int] = ..., snapshot_create_time_secs: _Optional[int] = ..., is_gap_filler: bool = ...) -> None: ...
