from heimdall.master.stub import rpc_service_pb2 as _rpc_service_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FleetInfoWALEntry(_message.Message):
    __slots__ = ("workflow_type", "status")
    class FleetStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kAcquiring: _ClassVar[FleetInfoWALEntry.FleetStatus]
        kAcquired: _ClassVar[FleetInfoWALEntry.FleetStatus]
        kReleasing: _ClassVar[FleetInfoWALEntry.FleetStatus]
    kAcquiring: FleetInfoWALEntry.FleetStatus
    kAcquired: FleetInfoWALEntry.FleetStatus
    kReleasing: FleetInfoWALEntry.FleetStatus
    WORKFLOW_TYPE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    workflow_type: _rpc_service_pb2.WorkflowType
    status: FleetInfoWALEntry.FleetStatus
    def __init__(self, workflow_type: _Optional[_Union[_rpc_service_pb2.WorkflowType, str]] = ..., status: _Optional[_Union[FleetInfoWALEntry.FleetStatus, str]] = ...) -> None: ...
