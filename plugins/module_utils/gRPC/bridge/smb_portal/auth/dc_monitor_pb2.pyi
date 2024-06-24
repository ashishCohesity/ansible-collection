from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ReachableDcProto(_message.Message):
    __slots__ = ("last_update_time_usecs", "domain_map")
    class DomainInfo(_message.Message):
        __slots__ = ("primary_fqdn", "reachable_dc_vec")
        class DcEndpoint(_message.Message):
            __slots__ = ("dc_fqdn", "ldap_port", "status")
            class DcStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                kReachable: _ClassVar[ReachableDcProto.DomainInfo.DcEndpoint.DcStatus]
                kIncompatible: _ClassVar[ReachableDcProto.DomainInfo.DcEndpoint.DcStatus]
                kFlapping: _ClassVar[ReachableDcProto.DomainInfo.DcEndpoint.DcStatus]
                kClockSkew: _ClassVar[ReachableDcProto.DomainInfo.DcEndpoint.DcStatus]
            kReachable: ReachableDcProto.DomainInfo.DcEndpoint.DcStatus
            kIncompatible: ReachableDcProto.DomainInfo.DcEndpoint.DcStatus
            kFlapping: ReachableDcProto.DomainInfo.DcEndpoint.DcStatus
            kClockSkew: ReachableDcProto.DomainInfo.DcEndpoint.DcStatus
            DC_FQDN_FIELD_NUMBER: _ClassVar[int]
            LDAP_PORT_FIELD_NUMBER: _ClassVar[int]
            STATUS_FIELD_NUMBER: _ClassVar[int]
            dc_fqdn: str
            ldap_port: int
            status: ReachableDcProto.DomainInfo.DcEndpoint.DcStatus
            def __init__(self, dc_fqdn: _Optional[str] = ..., ldap_port: _Optional[int] = ..., status: _Optional[_Union[ReachableDcProto.DomainInfo.DcEndpoint.DcStatus, str]] = ...) -> None: ...
        PRIMARY_FQDN_FIELD_NUMBER: _ClassVar[int]
        REACHABLE_DC_VEC_FIELD_NUMBER: _ClassVar[int]
        primary_fqdn: str
        reachable_dc_vec: _containers.RepeatedCompositeFieldContainer[ReachableDcProto.DomainInfo.DcEndpoint]
        def __init__(self, primary_fqdn: _Optional[str] = ..., reachable_dc_vec: _Optional[_Iterable[_Union[ReachableDcProto.DomainInfo.DcEndpoint, _Mapping]]] = ...) -> None: ...
    class DomainMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: ReachableDcProto.DomainInfo
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[ReachableDcProto.DomainInfo, _Mapping]] = ...) -> None: ...
    LAST_UPDATE_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_MAP_FIELD_NUMBER: _ClassVar[int]
    last_update_time_usecs: int
    domain_map: _containers.MessageMap[str, ReachableDcProto.DomainInfo]
    def __init__(self, last_update_time_usecs: _Optional[int] = ..., domain_map: _Optional[_Mapping[str, ReachableDcProto.DomainInfo]] = ...) -> None: ...

class DcMonitorLockDataProto(_message.Message):
    __slots__ = ("update_map",)
    class LastUpdateInfo(_message.Message):
        __slots__ = ("primary_fqdn", "update_time_usecs", "is_background_check", "cluster_config_version", "is_frequent_check_needed")
        PRIMARY_FQDN_FIELD_NUMBER: _ClassVar[int]
        UPDATE_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
        IS_BACKGROUND_CHECK_FIELD_NUMBER: _ClassVar[int]
        CLUSTER_CONFIG_VERSION_FIELD_NUMBER: _ClassVar[int]
        IS_FREQUENT_CHECK_NEEDED_FIELD_NUMBER: _ClassVar[int]
        primary_fqdn: str
        update_time_usecs: int
        is_background_check: bool
        cluster_config_version: int
        is_frequent_check_needed: bool
        def __init__(self, primary_fqdn: _Optional[str] = ..., update_time_usecs: _Optional[int] = ..., is_background_check: bool = ..., cluster_config_version: _Optional[int] = ..., is_frequent_check_needed: bool = ...) -> None: ...
    class UpdateMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: DcMonitorLockDataProto.LastUpdateInfo
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[DcMonitorLockDataProto.LastUpdateInfo, _Mapping]] = ...) -> None: ...
    UPDATE_MAP_FIELD_NUMBER: _ClassVar[int]
    update_map: _containers.MessageMap[str, DcMonitorLockDataProto.LastUpdateInfo]
    def __init__(self, update_map: _Optional[_Mapping[str, DcMonitorLockDataProto.LastUpdateInfo]] = ...) -> None: ...
