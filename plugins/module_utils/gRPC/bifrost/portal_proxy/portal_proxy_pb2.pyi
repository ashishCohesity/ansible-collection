from bifrost.base import bifrost_base_pb2 as _bifrost_base_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SessionProto(_message.Message):
    __slots__ = ("user_ip", "user_port", "user_tenant_id", "destination_port", "destination_ip", "hyx_connector_config")
    USER_IP_FIELD_NUMBER: _ClassVar[int]
    USER_PORT_FIELD_NUMBER: _ClassVar[int]
    USER_TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_PORT_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_IP_FIELD_NUMBER: _ClassVar[int]
    HYX_CONNECTOR_CONFIG_FIELD_NUMBER: _ClassVar[int]
    user_ip: str
    user_port: int
    user_tenant_id: str
    destination_port: str
    destination_ip: str
    hyx_connector_config: _bifrost_base_pb2.HyxConnectorConfigProto
    def __init__(self, user_ip: _Optional[str] = ..., user_port: _Optional[int] = ..., user_tenant_id: _Optional[str] = ..., destination_port: _Optional[str] = ..., destination_ip: _Optional[str] = ..., hyx_connector_config: _Optional[_Union[_bifrost_base_pb2.HyxConnectorConfigProto, _Mapping]] = ...) -> None: ...

class BifrostPortalProxyStreamData(_message.Message):
    __slots__ = ("session_info", "data_size", "data")
    SESSION_INFO_FIELD_NUMBER: _ClassVar[int]
    DATA_SIZE_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    session_info: SessionProto
    data_size: int
    data: bytes
    def __init__(self, session_info: _Optional[_Union[SessionProto, _Mapping]] = ..., data_size: _Optional[int] = ..., data: _Optional[bytes] = ...) -> None: ...
