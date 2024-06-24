from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SupportServiceVendor(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kNone: _ClassVar[SupportServiceVendor]
    kTeleport: _ClassVar[SupportServiceVendor]
kNone: SupportServiceVendor
kTeleport: SupportServiceVendor

class TeleportConfigProto(_message.Message):
    __slots__ = ("node_proxy_config", "session_recording")
    class AuthenticationService(_message.Message):
        __slots__ = ("cluster_name", "listen_port")
        CLUSTER_NAME_FIELD_NUMBER: _ClassVar[int]
        LISTEN_PORT_FIELD_NUMBER: _ClassVar[int]
        cluster_name: str
        listen_port: int
        def __init__(self, cluster_name: _Optional[str] = ..., listen_port: _Optional[int] = ...) -> None: ...
    class ProxyService(_message.Message):
        __slots__ = ("listen_port", "web_listen_port", "tunnel_listen_port")
        LISTEN_PORT_FIELD_NUMBER: _ClassVar[int]
        WEB_LISTEN_PORT_FIELD_NUMBER: _ClassVar[int]
        TUNNEL_LISTEN_PORT_FIELD_NUMBER: _ClassVar[int]
        listen_port: int
        web_listen_port: int
        tunnel_listen_port: int
        def __init__(self, listen_port: _Optional[int] = ..., web_listen_port: _Optional[int] = ..., tunnel_listen_port: _Optional[int] = ...) -> None: ...
    class NodeProxyConfiguration(_message.Message):
        __slots__ = ("token", "ca_pin", "auth_servers", "auth_service", "proxy_service")
        TOKEN_FIELD_NUMBER: _ClassVar[int]
        CA_PIN_FIELD_NUMBER: _ClassVar[int]
        AUTH_SERVERS_FIELD_NUMBER: _ClassVar[int]
        AUTH_SERVICE_FIELD_NUMBER: _ClassVar[int]
        PROXY_SERVICE_FIELD_NUMBER: _ClassVar[int]
        token: bytes
        ca_pin: str
        auth_servers: _containers.RepeatedScalarFieldContainer[str]
        auth_service: TeleportConfigProto.AuthenticationService
        proxy_service: TeleportConfigProto.ProxyService
        def __init__(self, token: _Optional[bytes] = ..., ca_pin: _Optional[str] = ..., auth_servers: _Optional[_Iterable[str]] = ..., auth_service: _Optional[_Union[TeleportConfigProto.AuthenticationService, _Mapping]] = ..., proxy_service: _Optional[_Union[TeleportConfigProto.ProxyService, _Mapping]] = ...) -> None: ...
    NODE_PROXY_CONFIG_FIELD_NUMBER: _ClassVar[int]
    SESSION_RECORDING_FIELD_NUMBER: _ClassVar[int]
    node_proxy_config: TeleportConfigProto.NodeProxyConfiguration
    session_recording: bool
    def __init__(self, node_proxy_config: _Optional[_Union[TeleportConfigProto.NodeProxyConfiguration, _Mapping]] = ..., session_recording: bool = ...) -> None: ...

class SupportServerV2Config(_message.Message):
    __slots__ = ("vendor", "teleport_config")
    VENDOR_FIELD_NUMBER: _ClassVar[int]
    TELEPORT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    vendor: SupportServiceVendor
    teleport_config: TeleportConfigProto
    def __init__(self, vendor: _Optional[_Union[SupportServiceVendor, str]] = ..., teleport_config: _Optional[_Union[TeleportConfigProto, _Mapping]] = ...) -> None: ...
