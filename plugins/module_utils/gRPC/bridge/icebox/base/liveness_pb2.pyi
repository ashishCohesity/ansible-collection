from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LivenessProto(_message.Message):
    __slots__ = ("ip", "port", "node_id", "network_interface_vec", "icebox_namespace")
    class NetworkInterface(_message.Message):
        __slots__ = ("ip", "speed_mbps")
        IP_FIELD_NUMBER: _ClassVar[int]
        SPEED_MBPS_FIELD_NUMBER: _ClassVar[int]
        ip: str
        speed_mbps: int
        def __init__(self, ip: _Optional[str] = ..., speed_mbps: _Optional[int] = ...) -> None: ...
    IP_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    NETWORK_INTERFACE_VEC_FIELD_NUMBER: _ClassVar[int]
    ICEBOX_NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    ip: str
    port: int
    node_id: int
    network_interface_vec: _containers.RepeatedCompositeFieldContainer[LivenessProto.NetworkInterface]
    icebox_namespace: str
    def __init__(self, ip: _Optional[str] = ..., port: _Optional[int] = ..., node_id: _Optional[int] = ..., network_interface_vec: _Optional[_Iterable[_Union[LivenessProto.NetworkInterface, _Mapping]]] = ..., icebox_namespace: _Optional[str] = ...) -> None: ...
