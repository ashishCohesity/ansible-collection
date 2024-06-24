from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FirewallProto(_message.Message):
    __slots__ = ("gandalf_key", "ipset_vec", "profile_vec", "attachment_vec", "initialized", "flags", "version")
    class Ipset(_message.Message):
        __slots__ = ("id", "name", "subnet_vec", "description")
        ID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        SUBNET_VEC_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        id: int
        name: str
        subnet_vec: _containers.RepeatedScalarFieldContainer[str]
        description: str
        def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., subnet_vec: _Optional[_Iterable[str]] = ..., description: _Optional[str] = ...) -> None: ...
    class Profile(_message.Message):
        __slots__ = ("id", "name", "service_vec", "port_protocol_vec", "direction_vec")
        class Service(_message.Message):
            __slots__ = ("id", "name", "port_vec")
            class Port(_message.Message):
                __slots__ = ("protocol", "number")
                class Protocol(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                    __slots__ = ()
                    udp: _ClassVar[FirewallProto.Profile.Service.Port.Protocol]
                    tcp: _ClassVar[FirewallProto.Profile.Service.Port.Protocol]
                    icmp: _ClassVar[FirewallProto.Profile.Service.Port.Protocol]
                    icmpv6: _ClassVar[FirewallProto.Profile.Service.Port.Protocol]
                udp: FirewallProto.Profile.Service.Port.Protocol
                tcp: FirewallProto.Profile.Service.Port.Protocol
                icmp: FirewallProto.Profile.Service.Port.Protocol
                icmpv6: FirewallProto.Profile.Service.Port.Protocol
                PROTOCOL_FIELD_NUMBER: _ClassVar[int]
                NUMBER_FIELD_NUMBER: _ClassVar[int]
                protocol: FirewallProto.Profile.Service.Port.Protocol
                number: int
                def __init__(self, protocol: _Optional[_Union[FirewallProto.Profile.Service.Port.Protocol, str]] = ..., number: _Optional[int] = ...) -> None: ...
            ID_FIELD_NUMBER: _ClassVar[int]
            NAME_FIELD_NUMBER: _ClassVar[int]
            PORT_VEC_FIELD_NUMBER: _ClassVar[int]
            id: int
            name: str
            port_vec: _containers.RepeatedCompositeFieldContainer[FirewallProto.Profile.Service.Port]
            def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., port_vec: _Optional[_Iterable[_Union[FirewallProto.Profile.Service.Port, _Mapping]]] = ...) -> None: ...
        ID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        SERVICE_VEC_FIELD_NUMBER: _ClassVar[int]
        PORT_PROTOCOL_VEC_FIELD_NUMBER: _ClassVar[int]
        DIRECTION_VEC_FIELD_NUMBER: _ClassVar[int]
        id: int
        name: str
        service_vec: _containers.RepeatedCompositeFieldContainer[FirewallProto.Profile.Service]
        port_protocol_vec: _containers.RepeatedScalarFieldContainer[str]
        direction_vec: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., service_vec: _Optional[_Iterable[_Union[FirewallProto.Profile.Service, _Mapping]]] = ..., port_protocol_vec: _Optional[_Iterable[str]] = ..., direction_vec: _Optional[_Iterable[str]] = ...) -> None: ...
    class Attachment(_message.Message):
        __slots__ = ("profile_name", "ipset_name_vec", "interface_name_vec", "action", "name", "description", "interface_group_id_vec", "interface_group_vec")
        class Action(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            Accept: _ClassVar[FirewallProto.Attachment.Action]
            Drop: _ClassVar[FirewallProto.Attachment.Action]
            Reject: _ClassVar[FirewallProto.Attachment.Action]
            Return: _ClassVar[FirewallProto.Attachment.Action]
        Accept: FirewallProto.Attachment.Action
        Drop: FirewallProto.Attachment.Action
        Reject: FirewallProto.Attachment.Action
        Return: FirewallProto.Attachment.Action
        PROFILE_NAME_FIELD_NUMBER: _ClassVar[int]
        IPSET_NAME_VEC_FIELD_NUMBER: _ClassVar[int]
        INTERFACE_NAME_VEC_FIELD_NUMBER: _ClassVar[int]
        ACTION_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        INTERFACE_GROUP_ID_VEC_FIELD_NUMBER: _ClassVar[int]
        INTERFACE_GROUP_VEC_FIELD_NUMBER: _ClassVar[int]
        profile_name: str
        ipset_name_vec: _containers.RepeatedScalarFieldContainer[str]
        interface_name_vec: _containers.RepeatedScalarFieldContainer[str]
        action: FirewallProto.Attachment.Action
        name: str
        description: str
        interface_group_id_vec: _containers.RepeatedScalarFieldContainer[int]
        interface_group_vec: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, profile_name: _Optional[str] = ..., ipset_name_vec: _Optional[_Iterable[str]] = ..., interface_name_vec: _Optional[_Iterable[str]] = ..., action: _Optional[_Union[FirewallProto.Attachment.Action, str]] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., interface_group_id_vec: _Optional[_Iterable[int]] = ..., interface_group_vec: _Optional[_Iterable[str]] = ...) -> None: ...
    class Flags(_message.Message):
        __slots__ = ("athena_allow_pod_external_traffic",)
        ATHENA_ALLOW_POD_EXTERNAL_TRAFFIC_FIELD_NUMBER: _ClassVar[int]
        athena_allow_pod_external_traffic: bool
        def __init__(self, athena_allow_pod_external_traffic: bool = ...) -> None: ...
    GANDALF_KEY_FIELD_NUMBER: _ClassVar[int]
    IPSET_VEC_FIELD_NUMBER: _ClassVar[int]
    PROFILE_VEC_FIELD_NUMBER: _ClassVar[int]
    ATTACHMENT_VEC_FIELD_NUMBER: _ClassVar[int]
    INITIALIZED_FIELD_NUMBER: _ClassVar[int]
    FLAGS_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    gandalf_key: str
    ipset_vec: _containers.RepeatedCompositeFieldContainer[FirewallProto.Ipset]
    profile_vec: _containers.RepeatedCompositeFieldContainer[FirewallProto.Profile]
    attachment_vec: _containers.RepeatedCompositeFieldContainer[FirewallProto.Attachment]
    initialized: bool
    flags: FirewallProto.Flags
    version: int
    def __init__(self, gandalf_key: _Optional[str] = ..., ipset_vec: _Optional[_Iterable[_Union[FirewallProto.Ipset, _Mapping]]] = ..., profile_vec: _Optional[_Iterable[_Union[FirewallProto.Profile, _Mapping]]] = ..., attachment_vec: _Optional[_Iterable[_Union[FirewallProto.Attachment, _Mapping]]] = ..., initialized: bool = ..., flags: _Optional[_Union[FirewallProto.Flags, _Mapping]] = ..., version: _Optional[int] = ...) -> None: ...
