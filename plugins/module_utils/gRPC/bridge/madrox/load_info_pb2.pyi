from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class LoadInfo(_message.Message):
    __slots__ = ("transmit_rid_load", "receive_rid_load", "transmit_unit_load", "receive_unit_load", "transmit_unit_load_smoothed", "receive_unit_load_smoothed", "external_io_load_smoothed", "external_metadata_load_smoothed", "forwarded_load_smoothed", "bridge_io_semaphore_utilization_smoothed", "bridge_metadata_semaphore_utilization_smoothed", "bridge_admctl_external_io_threshold", "bridge_admctl_external_metadata_threshold", "bridge_admctl_forwarded_io_threshold", "bridge_admctl_forwarded_metadata_threshold")
    TRANSMIT_RID_LOAD_FIELD_NUMBER: _ClassVar[int]
    RECEIVE_RID_LOAD_FIELD_NUMBER: _ClassVar[int]
    TRANSMIT_UNIT_LOAD_FIELD_NUMBER: _ClassVar[int]
    RECEIVE_UNIT_LOAD_FIELD_NUMBER: _ClassVar[int]
    TRANSMIT_UNIT_LOAD_SMOOTHED_FIELD_NUMBER: _ClassVar[int]
    RECEIVE_UNIT_LOAD_SMOOTHED_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_IO_LOAD_SMOOTHED_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_METADATA_LOAD_SMOOTHED_FIELD_NUMBER: _ClassVar[int]
    FORWARDED_LOAD_SMOOTHED_FIELD_NUMBER: _ClassVar[int]
    BRIDGE_IO_SEMAPHORE_UTILIZATION_SMOOTHED_FIELD_NUMBER: _ClassVar[int]
    BRIDGE_METADATA_SEMAPHORE_UTILIZATION_SMOOTHED_FIELD_NUMBER: _ClassVar[int]
    BRIDGE_ADMCTL_EXTERNAL_IO_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    BRIDGE_ADMCTL_EXTERNAL_METADATA_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    BRIDGE_ADMCTL_FORWARDED_IO_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    BRIDGE_ADMCTL_FORWARDED_METADATA_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    transmit_rid_load: int
    receive_rid_load: int
    transmit_unit_load: float
    receive_unit_load: float
    transmit_unit_load_smoothed: float
    receive_unit_load_smoothed: float
    external_io_load_smoothed: float
    external_metadata_load_smoothed: float
    forwarded_load_smoothed: float
    bridge_io_semaphore_utilization_smoothed: float
    bridge_metadata_semaphore_utilization_smoothed: float
    bridge_admctl_external_io_threshold: int
    bridge_admctl_external_metadata_threshold: int
    bridge_admctl_forwarded_io_threshold: int
    bridge_admctl_forwarded_metadata_threshold: int
    def __init__(self, transmit_rid_load: _Optional[int] = ..., receive_rid_load: _Optional[int] = ..., transmit_unit_load: _Optional[float] = ..., receive_unit_load: _Optional[float] = ..., transmit_unit_load_smoothed: _Optional[float] = ..., receive_unit_load_smoothed: _Optional[float] = ..., external_io_load_smoothed: _Optional[float] = ..., external_metadata_load_smoothed: _Optional[float] = ..., forwarded_load_smoothed: _Optional[float] = ..., bridge_io_semaphore_utilization_smoothed: _Optional[float] = ..., bridge_metadata_semaphore_utilization_smoothed: _Optional[float] = ..., bridge_admctl_external_io_threshold: _Optional[int] = ..., bridge_admctl_external_metadata_threshold: _Optional[int] = ..., bridge_admctl_forwarded_io_threshold: _Optional[int] = ..., bridge_admctl_forwarded_metadata_threshold: _Optional[int] = ...) -> None: ...
