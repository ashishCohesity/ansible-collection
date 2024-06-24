from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LivenessProto(_message.Message):
    __slots__ = ("ip", "port", "scribe_namespace", "start_usecs", "network_interface_vec")
    class NetworkInterface(_message.Message):
        __slots__ = ("ip", "speed_mbps")
        IP_FIELD_NUMBER: _ClassVar[int]
        SPEED_MBPS_FIELD_NUMBER: _ClassVar[int]
        ip: str
        speed_mbps: int
        def __init__(self, ip: _Optional[str] = ..., speed_mbps: _Optional[int] = ...) -> None: ...
    IP_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    SCRIBE_NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    START_USECS_FIELD_NUMBER: _ClassVar[int]
    NETWORK_INTERFACE_VEC_FIELD_NUMBER: _ClassVar[int]
    ip: str
    port: int
    scribe_namespace: str
    start_usecs: int
    network_interface_vec: _containers.RepeatedCompositeFieldContainer[LivenessProto.NetworkInterface]
    def __init__(self, ip: _Optional[str] = ..., port: _Optional[int] = ..., scribe_namespace: _Optional[str] = ..., start_usecs: _Optional[int] = ..., network_interface_vec: _Optional[_Iterable[_Union[LivenessProto.NetworkInterface, _Mapping]]] = ...) -> None: ...
