from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AdTrustAdjacencyListProto(_message.Message):
    __slots__ = ("gandalf_key", "member_domain_map", "primary_domain_map")
    class TrustDirection(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kDisabled: _ClassVar[AdTrustAdjacencyListProto.TrustDirection]
        kInbound: _ClassVar[AdTrustAdjacencyListProto.TrustDirection]
        kOutgoing: _ClassVar[AdTrustAdjacencyListProto.TrustDirection]
        kBidirectional: _ClassVar[AdTrustAdjacencyListProto.TrustDirection]
    kDisabled: AdTrustAdjacencyListProto.TrustDirection
    kInbound: AdTrustAdjacencyListProto.TrustDirection
    kOutgoing: AdTrustAdjacencyListProto.TrustDirection
    kBidirectional: AdTrustAdjacencyListProto.TrustDirection
    class TrustType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kDownLevel: _ClassVar[AdTrustAdjacencyListProto.TrustType]
        kUpLevel: _ClassVar[AdTrustAdjacencyListProto.TrustType]
        kMIT: _ClassVar[AdTrustAdjacencyListProto.TrustType]
        kDCE: _ClassVar[AdTrustAdjacencyListProto.TrustType]
    kDownLevel: AdTrustAdjacencyListProto.TrustType
    kUpLevel: AdTrustAdjacencyListProto.TrustType
    kMIT: AdTrustAdjacencyListProto.TrustType
    kDCE: AdTrustAdjacencyListProto.TrustType
    class NeighborInfo(_message.Message):
        __slots__ = ("fqdn", "trust_direction", "trust_type", "trust_attributes")
        FQDN_FIELD_NUMBER: _ClassVar[int]
        TRUST_DIRECTION_FIELD_NUMBER: _ClassVar[int]
        TRUST_TYPE_FIELD_NUMBER: _ClassVar[int]
        TRUST_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
        fqdn: str
        trust_direction: AdTrustAdjacencyListProto.TrustDirection
        trust_type: AdTrustAdjacencyListProto.TrustType
        trust_attributes: int
        def __init__(self, fqdn: _Optional[str] = ..., trust_direction: _Optional[_Union[AdTrustAdjacencyListProto.TrustDirection, str]] = ..., trust_type: _Optional[_Union[AdTrustAdjacencyListProto.TrustType, str]] = ..., trust_attributes: _Optional[int] = ...) -> None: ...
    class MemberDomain(_message.Message):
        __slots__ = ("netbios", "distinguished_name", "sid", "error_count", "neighbor_info_vec")
        NETBIOS_FIELD_NUMBER: _ClassVar[int]
        DISTINGUISHED_NAME_FIELD_NUMBER: _ClassVar[int]
        SID_FIELD_NUMBER: _ClassVar[int]
        ERROR_COUNT_FIELD_NUMBER: _ClassVar[int]
        NEIGHBOR_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
        netbios: str
        distinguished_name: str
        sid: str
        error_count: int
        neighbor_info_vec: _containers.RepeatedCompositeFieldContainer[AdTrustAdjacencyListProto.NeighborInfo]
        def __init__(self, netbios: _Optional[str] = ..., distinguished_name: _Optional[str] = ..., sid: _Optional[str] = ..., error_count: _Optional[int] = ..., neighbor_info_vec: _Optional[_Iterable[_Union[AdTrustAdjacencyListProto.NeighborInfo, _Mapping]]] = ...) -> None: ...
    class MemberDomainMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: AdTrustAdjacencyListProto.MemberDomain
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[AdTrustAdjacencyListProto.MemberDomain, _Mapping]] = ...) -> None: ...
    class PrimaryDomain(_message.Message):
        __slots__ = ("update_time_secs", "tenant_id_vec")
        UPDATE_TIME_SECS_FIELD_NUMBER: _ClassVar[int]
        TENANT_ID_VEC_FIELD_NUMBER: _ClassVar[int]
        update_time_secs: int
        tenant_id_vec: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, update_time_secs: _Optional[int] = ..., tenant_id_vec: _Optional[_Iterable[str]] = ...) -> None: ...
    class PrimaryDomainMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: AdTrustAdjacencyListProto.PrimaryDomain
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[AdTrustAdjacencyListProto.PrimaryDomain, _Mapping]] = ...) -> None: ...
    GANDALF_KEY_FIELD_NUMBER: _ClassVar[int]
    MEMBER_DOMAIN_MAP_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_DOMAIN_MAP_FIELD_NUMBER: _ClassVar[int]
    gandalf_key: str
    member_domain_map: _containers.MessageMap[str, AdTrustAdjacencyListProto.MemberDomain]
    primary_domain_map: _containers.MessageMap[str, AdTrustAdjacencyListProto.PrimaryDomain]
    def __init__(self, gandalf_key: _Optional[str] = ..., member_domain_map: _Optional[_Mapping[str, AdTrustAdjacencyListProto.MemberDomain]] = ..., primary_domain_map: _Optional[_Mapping[str, AdTrustAdjacencyListProto.PrimaryDomain]] = ...) -> None: ...
