from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AlertTypeProto(_message.Message):
    __slots__ = ("id",)
    class Id(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kTestDiskSpaceUsageHigh: _ClassVar[AlertTypeProto.Id]
        kTestViewBoxSpaceUsageHigh: _ClassVar[AlertTypeProto.Id]
        kTestNodeSpaceUsageHigh: _ClassVar[AlertTypeProto.Id]
        kTestClusterSpaceUsageHigh: _ClassVar[AlertTypeProto.Id]
        kClusterSpaceUsageHigh: _ClassVar[AlertTypeProto.Id]
        kViewBoxSpaceUsageHigh: _ClassVar[AlertTypeProto.Id]
        kNodeFailureIsNotTolerated: _ClassVar[AlertTypeProto.Id]
        kClusterCpuUsageHigh: _ClassVar[AlertTypeProto.Id]
        kClusterMemoryUsageHigh: _ClassVar[AlertTypeProto.Id]
        kDiskAwaitHigh: _ClassVar[AlertTypeProto.Id]
        kPulseTaskProgressHung: _ClassVar[AlertTypeProto.Id]
    kTestDiskSpaceUsageHigh: AlertTypeProto.Id
    kTestViewBoxSpaceUsageHigh: AlertTypeProto.Id
    kTestNodeSpaceUsageHigh: AlertTypeProto.Id
    kTestClusterSpaceUsageHigh: AlertTypeProto.Id
    kClusterSpaceUsageHigh: AlertTypeProto.Id
    kViewBoxSpaceUsageHigh: AlertTypeProto.Id
    kNodeFailureIsNotTolerated: AlertTypeProto.Id
    kClusterCpuUsageHigh: AlertTypeProto.Id
    kClusterMemoryUsageHigh: AlertTypeProto.Id
    kDiskAwaitHigh: AlertTypeProto.Id
    kPulseTaskProgressHung: AlertTypeProto.Id
    ID_FIELD_NUMBER: _ClassVar[int]
    id: AlertTypeProto.Id
    def __init__(self, id: _Optional[_Union[AlertTypeProto.Id, str]] = ...) -> None: ...
