from scribe.newscribe.base import view_config_pb2 as _view_config_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ClusterInfo(_message.Message):
    __slots__ = ("racks", "cluster_setting")
    class DiskInfo(_message.Message):
        __slots__ = ("status", "capacity")
        STATUS_FIELD_NUMBER: _ClassVar[int]
        CAPACITY_FIELD_NUMBER: _ClassVar[int]
        status: _view_config_pb2.ViewConfigProto.Constituent.OperationalStatus
        capacity: int
        def __init__(self, status: _Optional[_Union[_view_config_pb2.ViewConfigProto.Constituent.OperationalStatus, str]] = ..., capacity: _Optional[int] = ...) -> None: ...
    class NodeInfo(_message.Message):
        __slots__ = ("status", "disks")
        STATUS_FIELD_NUMBER: _ClassVar[int]
        DISKS_FIELD_NUMBER: _ClassVar[int]
        status: _view_config_pb2.ViewConfigProto.Constituent.OperationalStatus
        disks: _containers.RepeatedCompositeFieldContainer[ClusterInfo.DiskInfo]
        def __init__(self, status: _Optional[_Union[_view_config_pb2.ViewConfigProto.Constituent.OperationalStatus, str]] = ..., disks: _Optional[_Iterable[_Union[ClusterInfo.DiskInfo, _Mapping]]] = ...) -> None: ...
    class ChassisInfo(_message.Message):
        __slots__ = ("status", "nodes")
        STATUS_FIELD_NUMBER: _ClassVar[int]
        NODES_FIELD_NUMBER: _ClassVar[int]
        status: _view_config_pb2.ViewConfigProto.Constituent.OperationalStatus
        nodes: _containers.RepeatedCompositeFieldContainer[ClusterInfo.NodeInfo]
        def __init__(self, status: _Optional[_Union[_view_config_pb2.ViewConfigProto.Constituent.OperationalStatus, str]] = ..., nodes: _Optional[_Iterable[_Union[ClusterInfo.NodeInfo, _Mapping]]] = ...) -> None: ...
    class RackInfo(_message.Message):
        __slots__ = ("status", "chassis_vec")
        STATUS_FIELD_NUMBER: _ClassVar[int]
        CHASSIS_VEC_FIELD_NUMBER: _ClassVar[int]
        status: _view_config_pb2.ViewConfigProto.Constituent.OperationalStatus
        chassis_vec: _containers.RepeatedCompositeFieldContainer[ClusterInfo.ChassisInfo]
        def __init__(self, status: _Optional[_Union[_view_config_pb2.ViewConfigProto.Constituent.OperationalStatus, str]] = ..., chassis_vec: _Optional[_Iterable[_Union[ClusterInfo.ChassisInfo, _Mapping]]] = ...) -> None: ...
    RACKS_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_SETTING_FIELD_NUMBER: _ClassVar[int]
    racks: _containers.RepeatedCompositeFieldContainer[ClusterInfo.RackInfo]
    cluster_setting: _view_config_pb2.ViewConfigProto.ClusterSetting
    def __init__(self, racks: _Optional[_Iterable[_Union[ClusterInfo.RackInfo, _Mapping]]] = ..., cluster_setting: _Optional[_Union[_view_config_pb2.ViewConfigProto.ClusterSetting, _Mapping]] = ...) -> None: ...
