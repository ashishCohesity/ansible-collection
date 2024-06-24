from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RigelConnectivityProto(_message.Message):
    __slots__ = ("gandalf_key", "node_endpoint_state_vec")
    class NodeEndpointState(_message.Message):
        __slots__ = ("node_id", "endpoint_connection_state_vec", "GatewayReachability", "DNSServerReachability", "NTPServerReachability", "check_time_usecs")
        class ConnectivityState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kStateUnknown: _ClassVar[RigelConnectivityProto.NodeEndpointState.ConnectivityState]
            kStateOk: _ClassVar[RigelConnectivityProto.NodeEndpointState.ConnectivityState]
            kStateFail: _ClassVar[RigelConnectivityProto.NodeEndpointState.ConnectivityState]
            kStateInProgress: _ClassVar[RigelConnectivityProto.NodeEndpointState.ConnectivityState]
        kStateUnknown: RigelConnectivityProto.NodeEndpointState.ConnectivityState
        kStateOk: RigelConnectivityProto.NodeEndpointState.ConnectivityState
        kStateFail: RigelConnectivityProto.NodeEndpointState.ConnectivityState
        kStateInProgress: RigelConnectivityProto.NodeEndpointState.ConnectivityState
        class EndpointConnStatus(_message.Message):
            __slots__ = ("endpoint_name", "endpoint_port", "check_result_vec")
            class CheckResult(_message.Message):
                __slots__ = ("check_name", "connectivity_state", "error_message")
                CHECK_NAME_FIELD_NUMBER: _ClassVar[int]
                CONNECTIVITY_STATE_FIELD_NUMBER: _ClassVar[int]
                ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
                check_name: str
                connectivity_state: RigelConnectivityProto.NodeEndpointState.ConnectivityState
                error_message: str
                def __init__(self, check_name: _Optional[str] = ..., connectivity_state: _Optional[_Union[RigelConnectivityProto.NodeEndpointState.ConnectivityState, str]] = ..., error_message: _Optional[str] = ...) -> None: ...
            ENDPOINT_NAME_FIELD_NUMBER: _ClassVar[int]
            ENDPOINT_PORT_FIELD_NUMBER: _ClassVar[int]
            CHECK_RESULT_VEC_FIELD_NUMBER: _ClassVar[int]
            endpoint_name: str
            endpoint_port: str
            check_result_vec: _containers.RepeatedCompositeFieldContainer[RigelConnectivityProto.NodeEndpointState.EndpointConnStatus.CheckResult]
            def __init__(self, endpoint_name: _Optional[str] = ..., endpoint_port: _Optional[str] = ..., check_result_vec: _Optional[_Iterable[_Union[RigelConnectivityProto.NodeEndpointState.EndpointConnStatus.CheckResult, _Mapping]]] = ...) -> None: ...
        NODE_ID_FIELD_NUMBER: _ClassVar[int]
        ENDPOINT_CONNECTION_STATE_VEC_FIELD_NUMBER: _ClassVar[int]
        GATEWAYREACHABILITY_FIELD_NUMBER: _ClassVar[int]
        DNSSERVERREACHABILITY_FIELD_NUMBER: _ClassVar[int]
        NTPSERVERREACHABILITY_FIELD_NUMBER: _ClassVar[int]
        CHECK_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
        node_id: int
        endpoint_connection_state_vec: _containers.RepeatedCompositeFieldContainer[RigelConnectivityProto.NodeEndpointState.EndpointConnStatus]
        GatewayReachability: RigelConnectivityProto.NodeEndpointState.EndpointConnStatus
        DNSServerReachability: RigelConnectivityProto.NodeEndpointState.EndpointConnStatus
        NTPServerReachability: RigelConnectivityProto.NodeEndpointState.EndpointConnStatus
        check_time_usecs: int
        def __init__(self, node_id: _Optional[int] = ..., endpoint_connection_state_vec: _Optional[_Iterable[_Union[RigelConnectivityProto.NodeEndpointState.EndpointConnStatus, _Mapping]]] = ..., GatewayReachability: _Optional[_Union[RigelConnectivityProto.NodeEndpointState.EndpointConnStatus, _Mapping]] = ..., DNSServerReachability: _Optional[_Union[RigelConnectivityProto.NodeEndpointState.EndpointConnStatus, _Mapping]] = ..., NTPServerReachability: _Optional[_Union[RigelConnectivityProto.NodeEndpointState.EndpointConnStatus, _Mapping]] = ..., check_time_usecs: _Optional[int] = ...) -> None: ...
    GANDALF_KEY_FIELD_NUMBER: _ClassVar[int]
    NODE_ENDPOINT_STATE_VEC_FIELD_NUMBER: _ClassVar[int]
    gandalf_key: str
    node_endpoint_state_vec: _containers.RepeatedCompositeFieldContainer[RigelConnectivityProto.NodeEndpointState]
    def __init__(self, gandalf_key: _Optional[str] = ..., node_endpoint_state_vec: _Optional[_Iterable[_Union[RigelConnectivityProto.NodeEndpointState, _Mapping]]] = ...) -> None: ...
