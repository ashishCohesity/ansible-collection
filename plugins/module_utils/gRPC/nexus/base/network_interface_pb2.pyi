from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NetworkInterfaceProto(_message.Message):
    __slots__ = ("gandalf_key", "node_interface_states_vec")
    class NodeNetworkInterfacesState(_message.Message):
        __slots__ = ("node_id", "interface_state_vec")
        class NetworkInterfaceState(_message.Message):
            __slots__ = ("interface_name", "interface_state")
            class InterfaceState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                kStateUnknown: _ClassVar[NetworkInterfaceProto.NodeNetworkInterfacesState.NetworkInterfaceState.InterfaceState]
                kStateUp: _ClassVar[NetworkInterfaceProto.NodeNetworkInterfacesState.NetworkInterfaceState.InterfaceState]
                kStateDown: _ClassVar[NetworkInterfaceProto.NodeNetworkInterfacesState.NetworkInterfaceState.InterfaceState]
            kStateUnknown: NetworkInterfaceProto.NodeNetworkInterfacesState.NetworkInterfaceState.InterfaceState
            kStateUp: NetworkInterfaceProto.NodeNetworkInterfacesState.NetworkInterfaceState.InterfaceState
            kStateDown: NetworkInterfaceProto.NodeNetworkInterfacesState.NetworkInterfaceState.InterfaceState
            INTERFACE_NAME_FIELD_NUMBER: _ClassVar[int]
            INTERFACE_STATE_FIELD_NUMBER: _ClassVar[int]
            interface_name: str
            interface_state: NetworkInterfaceProto.NodeNetworkInterfacesState.NetworkInterfaceState.InterfaceState
            def __init__(self, interface_name: _Optional[str] = ..., interface_state: _Optional[_Union[NetworkInterfaceProto.NodeNetworkInterfacesState.NetworkInterfaceState.InterfaceState, str]] = ...) -> None: ...
        NODE_ID_FIELD_NUMBER: _ClassVar[int]
        INTERFACE_STATE_VEC_FIELD_NUMBER: _ClassVar[int]
        node_id: int
        interface_state_vec: _containers.RepeatedCompositeFieldContainer[NetworkInterfaceProto.NodeNetworkInterfacesState.NetworkInterfaceState]
        def __init__(self, node_id: _Optional[int] = ..., interface_state_vec: _Optional[_Iterable[_Union[NetworkInterfaceProto.NodeNetworkInterfacesState.NetworkInterfaceState, _Mapping]]] = ...) -> None: ...
    GANDALF_KEY_FIELD_NUMBER: _ClassVar[int]
    NODE_INTERFACE_STATES_VEC_FIELD_NUMBER: _ClassVar[int]
    gandalf_key: str
    node_interface_states_vec: _containers.RepeatedCompositeFieldContainer[NetworkInterfaceProto.NodeNetworkInterfacesState]
    def __init__(self, gandalf_key: _Optional[str] = ..., node_interface_states_vec: _Optional[_Iterable[_Union[NetworkInterfaceProto.NodeNetworkInterfacesState, _Mapping]]] = ...) -> None: ...
