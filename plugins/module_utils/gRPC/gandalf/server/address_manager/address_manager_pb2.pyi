from open_util.net import protorpc_pb2 as _protorpc_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GandalfEndpointProto(_message.Message):
    __slots__ = ("endpoint_map",)
    class EndpointMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: str
        def __init__(self, key: _Optional[int] = ..., value: _Optional[str] = ...) -> None: ...
    ENDPOINT_MAP_FIELD_NUMBER: _ClassVar[int]
    endpoint_map: _containers.ScalarMap[int, str]
    def __init__(self, endpoint_map: _Optional[_Mapping[int, str]] = ...) -> None: ...

class FetchIpInfoArg(_message.Message):
    __slots__ = ("cluster_id",)
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    cluster_id: int
    def __init__(self, cluster_id: _Optional[int] = ...) -> None: ...

class FetchIpInfoResult(_message.Message):
    __slots__ = ("endpoint_proto",)
    ENDPOINT_PROTO_FIELD_NUMBER: _ClassVar[int]
    endpoint_proto: GandalfEndpointProto
    def __init__(self, endpoint_proto: _Optional[_Union[GandalfEndpointProto, _Mapping]] = ...) -> None: ...

class PushIpInfoArg(_message.Message):
    __slots__ = ("cluster_id", "endpoint_proto")
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_PROTO_FIELD_NUMBER: _ClassVar[int]
    cluster_id: int
    endpoint_proto: GandalfEndpointProto
    def __init__(self, cluster_id: _Optional[int] = ..., endpoint_proto: _Optional[_Union[GandalfEndpointProto, _Mapping]] = ...) -> None: ...

class PushIpInfoResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ProbeArg(_message.Message):
    __slots__ = ("cluster_id",)
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    cluster_id: int
    def __init__(self, cluster_id: _Optional[int] = ...) -> None: ...

class ProbeResult(_message.Message):
    __slots__ = ("node_id", "gandalf_master_incarnation_id")
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    GANDALF_MASTER_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    node_id: int
    gandalf_master_incarnation_id: int
    def __init__(self, node_id: _Optional[int] = ..., gandalf_master_incarnation_id: _Optional[int] = ...) -> None: ...
