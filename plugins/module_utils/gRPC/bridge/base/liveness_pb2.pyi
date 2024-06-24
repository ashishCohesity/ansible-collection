from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LivenessProto(_message.Message):
    __slots__ = ("ip", "network_interface_vec", "port", "node_id", "hydra_port", "bridge_namespace", "bridge_disk_namespace", "publishes_disk_liveness", "bridge_proxy_namespace", "bridge_proxy_port")
    class NetworkInterface(_message.Message):
        __slots__ = ("ip", "speed_mbps")
        IP_FIELD_NUMBER: _ClassVar[int]
        SPEED_MBPS_FIELD_NUMBER: _ClassVar[int]
        ip: str
        speed_mbps: int
        def __init__(self, ip: _Optional[str] = ..., speed_mbps: _Optional[int] = ...) -> None: ...
    IP_FIELD_NUMBER: _ClassVar[int]
    NETWORK_INTERFACE_VEC_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    HYDRA_PORT_FIELD_NUMBER: _ClassVar[int]
    BRIDGE_NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    BRIDGE_DISK_NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    PUBLISHES_DISK_LIVENESS_FIELD_NUMBER: _ClassVar[int]
    BRIDGE_PROXY_NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    BRIDGE_PROXY_PORT_FIELD_NUMBER: _ClassVar[int]
    ip: str
    network_interface_vec: _containers.RepeatedCompositeFieldContainer[LivenessProto.NetworkInterface]
    port: int
    node_id: int
    hydra_port: int
    bridge_namespace: str
    bridge_disk_namespace: str
    publishes_disk_liveness: bool
    bridge_proxy_namespace: str
    bridge_proxy_port: int
    def __init__(self, ip: _Optional[str] = ..., network_interface_vec: _Optional[_Iterable[_Union[LivenessProto.NetworkInterface, _Mapping]]] = ..., port: _Optional[int] = ..., node_id: _Optional[int] = ..., hydra_port: _Optional[int] = ..., bridge_namespace: _Optional[str] = ..., bridge_disk_namespace: _Optional[str] = ..., publishes_disk_liveness: bool = ..., bridge_proxy_namespace: _Optional[str] = ..., bridge_proxy_port: _Optional[int] = ...) -> None: ...
