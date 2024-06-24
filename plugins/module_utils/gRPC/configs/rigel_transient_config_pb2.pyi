from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RigelConnectionStatus(_message.Message):
    __slots__ = ("is_connected", "last_connected_timestamp_msecs", "error_message_str", "bifrost_consitutent_id")
    IS_CONNECTED_FIELD_NUMBER: _ClassVar[int]
    LAST_CONNECTED_TIMESTAMP_MSECS_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_STR_FIELD_NUMBER: _ClassVar[int]
    BIFROST_CONSITUTENT_ID_FIELD_NUMBER: _ClassVar[int]
    is_connected: bool
    last_connected_timestamp_msecs: int
    error_message_str: str
    bifrost_consitutent_id: int
    def __init__(self, is_connected: bool = ..., last_connected_timestamp_msecs: _Optional[int] = ..., error_message_str: _Optional[str] = ..., bifrost_consitutent_id: _Optional[int] = ...) -> None: ...

class RigelNode(_message.Message):
    __slots__ = ("rigel_guid", "controlplane_connection_status", "dataplane_connection_status", "dataplane_connection_status_vec")
    RIGEL_GUID_FIELD_NUMBER: _ClassVar[int]
    CONTROLPLANE_CONNECTION_STATUS_FIELD_NUMBER: _ClassVar[int]
    DATAPLANE_CONNECTION_STATUS_FIELD_NUMBER: _ClassVar[int]
    DATAPLANE_CONNECTION_STATUS_VEC_FIELD_NUMBER: _ClassVar[int]
    rigel_guid: int
    controlplane_connection_status: RigelConnectionStatus
    dataplane_connection_status: RigelConnectionStatus
    dataplane_connection_status_vec: _containers.RepeatedCompositeFieldContainer[RigelConnectionStatus]
    def __init__(self, rigel_guid: _Optional[int] = ..., controlplane_connection_status: _Optional[_Union[RigelConnectionStatus, _Mapping]] = ..., dataplane_connection_status: _Optional[_Union[RigelConnectionStatus, _Mapping]] = ..., dataplane_connection_status_vec: _Optional[_Iterable[_Union[RigelConnectionStatus, _Mapping]]] = ...) -> None: ...

class RigelTransientConfig(_message.Message):
    __slots__ = ("rigel_node_vec",)
    RIGEL_NODE_VEC_FIELD_NUMBER: _ClassVar[int]
    rigel_node_vec: _containers.RepeatedCompositeFieldContainer[RigelNode]
    def __init__(self, rigel_node_vec: _Optional[_Iterable[_Union[RigelNode, _Mapping]]] = ...) -> None: ...
