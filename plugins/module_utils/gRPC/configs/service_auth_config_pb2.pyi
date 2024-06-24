from util.base import universal_id_pb2 as _universal_id_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ServiceAuthConfigProto(_message.Message):
    __slots__ = ("client_component_2_acl_mask_map",)
    class ClientComponent(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kUnknown: _ClassVar[ServiceAuthConfigProto.ClientComponent]
        kOther: _ClassVar[ServiceAuthConfigProto.ClientComponent]
        kTools: _ClassVar[ServiceAuthConfigProto.ClientComponent]
        kBridge: _ClassVar[ServiceAuthConfigProto.ClientComponent]
        kApollo: _ClassVar[ServiceAuthConfigProto.ClientComponent]
        kMagneto: _ClassVar[ServiceAuthConfigProto.ClientComponent]
        kMadrox: _ClassVar[ServiceAuthConfigProto.ClientComponent]
        kIcebox: _ClassVar[ServiceAuthConfigProto.ClientComponent]
        kYoda: _ClassVar[ServiceAuthConfigProto.ClientComponent]
        kAthena: _ClassVar[ServiceAuthConfigProto.ClientComponent]
        kAtomRemote: _ClassVar[ServiceAuthConfigProto.ClientComponent]
    kUnknown: ServiceAuthConfigProto.ClientComponent
    kOther: ServiceAuthConfigProto.ClientComponent
    kTools: ServiceAuthConfigProto.ClientComponent
    kBridge: ServiceAuthConfigProto.ClientComponent
    kApollo: ServiceAuthConfigProto.ClientComponent
    kMagneto: ServiceAuthConfigProto.ClientComponent
    kMadrox: ServiceAuthConfigProto.ClientComponent
    kIcebox: ServiceAuthConfigProto.ClientComponent
    kYoda: ServiceAuthConfigProto.ClientComponent
    kAthena: ServiceAuthConfigProto.ClientComponent
    kAtomRemote: ServiceAuthConfigProto.ClientComponent
    class ACLPermissionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kRead: _ClassVar[ServiceAuthConfigProto.ACLPermissionType]
        kWrite: _ClassVar[ServiceAuthConfigProto.ACLPermissionType]
    kRead: ServiceAuthConfigProto.ACLPermissionType
    kWrite: ServiceAuthConfigProto.ACLPermissionType
    class ClientComponent2AclMaskMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    class ClientID(_message.Message):
        __slots__ = ("id",)
        ID_FIELD_NUMBER: _ClassVar[int]
        id: _universal_id_pb2.UniversalIdProto
        def __init__(self, id: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ...) -> None: ...
    CLIENT_COMPONENT_2_ACL_MASK_MAP_FIELD_NUMBER: _ClassVar[int]
    client_component_2_acl_mask_map: _containers.ScalarMap[int, int]
    def __init__(self, client_component_2_acl_mask_map: _Optional[_Mapping[int, int]] = ...) -> None: ...
