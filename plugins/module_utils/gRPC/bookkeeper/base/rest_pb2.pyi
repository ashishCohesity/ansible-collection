from apollo.mr.base import utils_pb2 as _utils_pb2
from bookkeeper.base import error_pb2 as _error_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GroupFilterProto(_message.Message):
    __slots__ = ("tenant_id_vec", "storage_domain_id_vec", "consumer", "null_tenant")
    class ConsumerProto(_message.Message):
        __slots__ = ("type",)
        class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kNone: _ClassVar[GroupFilterProto.ConsumerProto.Type]
            kViews: _ClassVar[GroupFilterProto.ConsumerProto.Type]
            kBackupRuns: _ClassVar[GroupFilterProto.ConsumerProto.Type]
            kReplicationRuns: _ClassVar[GroupFilterProto.ConsumerProto.Type]
            kObjects: _ClassVar[GroupFilterProto.ConsumerProto.Type]
            kDataProtect: _ClassVar[GroupFilterProto.ConsumerProto.Type]
            kDataPlatform: _ClassVar[GroupFilterProto.ConsumerProto.Type]
            kViewProtectionRuns: _ClassVar[GroupFilterProto.ConsumerProto.Type]
        kNone: GroupFilterProto.ConsumerProto.Type
        kViews: GroupFilterProto.ConsumerProto.Type
        kBackupRuns: GroupFilterProto.ConsumerProto.Type
        kReplicationRuns: GroupFilterProto.ConsumerProto.Type
        kObjects: GroupFilterProto.ConsumerProto.Type
        kDataProtect: GroupFilterProto.ConsumerProto.Type
        kDataPlatform: GroupFilterProto.ConsumerProto.Type
        kViewProtectionRuns: GroupFilterProto.ConsumerProto.Type
        TYPE_FIELD_NUMBER: _ClassVar[int]
        type: GroupFilterProto.ConsumerProto.Type
        def __init__(self, type: _Optional[_Union[GroupFilterProto.ConsumerProto.Type, str]] = ...) -> None: ...
    TENANT_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    STORAGE_DOMAIN_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    CONSUMER_FIELD_NUMBER: _ClassVar[int]
    NULL_TENANT_FIELD_NUMBER: _ClassVar[int]
    tenant_id_vec: _containers.RepeatedScalarFieldContainer[str]
    storage_domain_id_vec: _containers.RepeatedScalarFieldContainer[int]
    consumer: GroupFilterProto.ConsumerProto
    null_tenant: bool
    def __init__(self, tenant_id_vec: _Optional[_Iterable[str]] = ..., storage_domain_id_vec: _Optional[_Iterable[int]] = ..., consumer: _Optional[_Union[GroupFilterProto.ConsumerProto, _Mapping]] = ..., null_tenant: bool = ...) -> None: ...

class GroupInformationProto(_message.Message):
    __slots__ = ("id", "name", "attributes", "stats_entity_id_str", "metric_vec", "stats_timestamp_usecs")
    class GroupAttributesProto(_message.Message):
        __slots__ = ("tenant_id_deprecated", "storage_domain_id", "consumer", "tenant_info")
        class TenantInfo(_message.Message):
            __slots__ = ("tenant_id_str", "null_tenant")
            TENANT_ID_STR_FIELD_NUMBER: _ClassVar[int]
            NULL_TENANT_FIELD_NUMBER: _ClassVar[int]
            tenant_id_str: str
            null_tenant: bool
            def __init__(self, tenant_id_str: _Optional[str] = ..., null_tenant: bool = ...) -> None: ...
        TENANT_ID_DEPRECATED_FIELD_NUMBER: _ClassVar[int]
        STORAGE_DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
        CONSUMER_FIELD_NUMBER: _ClassVar[int]
        TENANT_INFO_FIELD_NUMBER: _ClassVar[int]
        tenant_id_deprecated: str
        storage_domain_id: int
        consumer: GroupFilterProto.ConsumerProto
        tenant_info: GroupInformationProto.GroupAttributesProto.TenantInfo
        def __init__(self, tenant_id_deprecated: _Optional[str] = ..., storage_domain_id: _Optional[int] = ..., consumer: _Optional[_Union[GroupFilterProto.ConsumerProto, _Mapping]] = ..., tenant_info: _Optional[_Union[GroupInformationProto.GroupAttributesProto.TenantInfo, _Mapping]] = ...) -> None: ...
    class Metric(_message.Message):
        __slots__ = ("name", "value", "time_stamp_usecs")
        NAME_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        TIME_STAMP_USECS_FIELD_NUMBER: _ClassVar[int]
        name: str
        value: int
        time_stamp_usecs: int
        def __init__(self, name: _Optional[str] = ..., value: _Optional[int] = ..., time_stamp_usecs: _Optional[int] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    STATS_ENTITY_ID_STR_FIELD_NUMBER: _ClassVar[int]
    METRIC_VEC_FIELD_NUMBER: _ClassVar[int]
    STATS_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    attributes: GroupInformationProto.GroupAttributesProto
    stats_entity_id_str: str
    metric_vec: _containers.RepeatedCompositeFieldContainer[GroupInformationProto.Metric]
    stats_timestamp_usecs: int
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., attributes: _Optional[_Union[GroupInformationProto.GroupAttributesProto, _Mapping]] = ..., stats_entity_id_str: _Optional[str] = ..., metric_vec: _Optional[_Iterable[_Union[GroupInformationProto.Metric, _Mapping]]] = ..., stats_timestamp_usecs: _Optional[int] = ...) -> None: ...

class GetStorageDomainStorageStatsArg(_message.Message):
    __slots__ = ("query_filter", "max_count", "pagination_cookie")
    QUERY_FILTER_FIELD_NUMBER: _ClassVar[int]
    MAX_COUNT_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_COOKIE_FIELD_NUMBER: _ClassVar[int]
    query_filter: GroupFilterProto
    max_count: int
    pagination_cookie: str
    def __init__(self, query_filter: _Optional[_Union[GroupFilterProto, _Mapping]] = ..., max_count: _Optional[int] = ..., pagination_cookie: _Optional[str] = ...) -> None: ...

class GetStorageDomainStorageStatsResult(_message.Message):
    __slots__ = ("error", "storage_domain_info_vec", "pagination_cookie")
    class StorageDomainInfo(_message.Message):
        __slots__ = ("id", "name", "group_info")
        ID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        GROUP_INFO_FIELD_NUMBER: _ClassVar[int]
        id: int
        name: str
        group_info: GroupInformationProto
        def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., group_info: _Optional[_Union[GroupInformationProto, _Mapping]] = ...) -> None: ...
    ERROR_FIELD_NUMBER: _ClassVar[int]
    STORAGE_DOMAIN_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_COOKIE_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    storage_domain_info_vec: _containers.RepeatedCompositeFieldContainer[GetStorageDomainStorageStatsResult.StorageDomainInfo]
    pagination_cookie: str
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., storage_domain_info_vec: _Optional[_Iterable[_Union[GetStorageDomainStorageStatsResult.StorageDomainInfo, _Mapping]]] = ..., pagination_cookie: _Optional[str] = ...) -> None: ...

class GetTenantStorageStatsArg(_message.Message):
    __slots__ = ("query_filter", "max_count", "pagination_cookie")
    QUERY_FILTER_FIELD_NUMBER: _ClassVar[int]
    MAX_COUNT_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_COOKIE_FIELD_NUMBER: _ClassVar[int]
    query_filter: GroupFilterProto
    max_count: int
    pagination_cookie: str
    def __init__(self, query_filter: _Optional[_Union[GroupFilterProto, _Mapping]] = ..., max_count: _Optional[int] = ..., pagination_cookie: _Optional[str] = ...) -> None: ...

class GetTenantStorageStatsResult(_message.Message):
    __slots__ = ("error", "tenant_info_vec", "pagination_cookie")
    class TenantInfo(_message.Message):
        __slots__ = ("id", "name", "group_info", "null_tenant")
        ID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        GROUP_INFO_FIELD_NUMBER: _ClassVar[int]
        NULL_TENANT_FIELD_NUMBER: _ClassVar[int]
        id: str
        name: str
        group_info: GroupInformationProto
        null_tenant: bool
        def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., group_info: _Optional[_Union[GroupInformationProto, _Mapping]] = ..., null_tenant: bool = ...) -> None: ...
    ERROR_FIELD_NUMBER: _ClassVar[int]
    TENANT_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_COOKIE_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    tenant_info_vec: _containers.RepeatedCompositeFieldContainer[GetTenantStorageStatsResult.TenantInfo]
    pagination_cookie: str
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., tenant_info_vec: _Optional[_Iterable[_Union[GetTenantStorageStatsResult.TenantInfo, _Mapping]]] = ..., pagination_cookie: _Optional[str] = ...) -> None: ...

class GetConsumerStorageStatsArg(_message.Message):
    __slots__ = ("query_filter", "max_count", "pagination_cookie")
    QUERY_FILTER_FIELD_NUMBER: _ClassVar[int]
    MAX_COUNT_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_COOKIE_FIELD_NUMBER: _ClassVar[int]
    query_filter: GroupFilterProto
    max_count: int
    pagination_cookie: str
    def __init__(self, query_filter: _Optional[_Union[GroupFilterProto, _Mapping]] = ..., max_count: _Optional[int] = ..., pagination_cookie: _Optional[str] = ...) -> None: ...

class GetConsumerStorageStatsResult(_message.Message):
    __slots__ = ("error", "consumer_info_vec", "pagination_cookie")
    class ConsumerInfo(_message.Message):
        __slots__ = ("group_info",)
        GROUP_INFO_FIELD_NUMBER: _ClassVar[int]
        group_info: GroupInformationProto
        def __init__(self, group_info: _Optional[_Union[GroupInformationProto, _Mapping]] = ...) -> None: ...
    ERROR_FIELD_NUMBER: _ClassVar[int]
    CONSUMER_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_COOKIE_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    consumer_info_vec: _containers.RepeatedCompositeFieldContainer[GetConsumerStorageStatsResult.ConsumerInfo]
    pagination_cookie: str
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., consumer_info_vec: _Optional[_Iterable[_Union[GetConsumerStorageStatsResult.ConsumerInfo, _Mapping]]] = ..., pagination_cookie: _Optional[str] = ...) -> None: ...

class GetJobStorageStatsArg(_message.Message):
    __slots__ = ("query_filter", "pagination_cookie", "max_count")
    QUERY_FILTER_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_COOKIE_FIELD_NUMBER: _ClassVar[int]
    MAX_COUNT_FIELD_NUMBER: _ClassVar[int]
    query_filter: GroupFilterProto
    pagination_cookie: str
    max_count: int
    def __init__(self, query_filter: _Optional[_Union[GroupFilterProto, _Mapping]] = ..., pagination_cookie: _Optional[str] = ..., max_count: _Optional[int] = ...) -> None: ...

class GetJobStorageStatsResult(_message.Message):
    __slots__ = ("error", "job_info_vec", "pagination_cookie")
    class GroupInfo(_message.Message):
        __slots__ = ("id", "name", "group_info")
        ID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        GROUP_INFO_FIELD_NUMBER: _ClassVar[int]
        id: _utils_pb2.ObjectUidProto
        name: str
        group_info: GroupInformationProto
        def __init__(self, id: _Optional[_Union[_utils_pb2.ObjectUidProto, _Mapping]] = ..., name: _Optional[str] = ..., group_info: _Optional[_Union[GroupInformationProto, _Mapping]] = ...) -> None: ...
    ERROR_FIELD_NUMBER: _ClassVar[int]
    JOB_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_COOKIE_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    job_info_vec: _containers.RepeatedCompositeFieldContainer[GetJobStorageStatsResult.GroupInfo]
    pagination_cookie: str
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., job_info_vec: _Optional[_Iterable[_Union[GetJobStorageStatsResult.GroupInfo, _Mapping]]] = ..., pagination_cookie: _Optional[str] = ...) -> None: ...

class GetViewStorageStatsArg(_message.Message):
    __slots__ = ("query_filter", "max_count", "pagination_cookie")
    QUERY_FILTER_FIELD_NUMBER: _ClassVar[int]
    MAX_COUNT_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_COOKIE_FIELD_NUMBER: _ClassVar[int]
    query_filter: GroupFilterProto
    max_count: int
    pagination_cookie: str
    def __init__(self, query_filter: _Optional[_Union[GroupFilterProto, _Mapping]] = ..., max_count: _Optional[int] = ..., pagination_cookie: _Optional[str] = ...) -> None: ...

class GetViewStorageStatsResult(_message.Message):
    __slots__ = ("error", "view_info_vec", "pagination_cookie")
    class ViewInfo(_message.Message):
        __slots__ = ("id", "name", "group_info")
        ID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        GROUP_INFO_FIELD_NUMBER: _ClassVar[int]
        id: int
        name: str
        group_info: GroupInformationProto
        def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., group_info: _Optional[_Union[GroupInformationProto, _Mapping]] = ...) -> None: ...
    ERROR_FIELD_NUMBER: _ClassVar[int]
    VIEW_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_COOKIE_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    view_info_vec: _containers.RepeatedCompositeFieldContainer[GetViewStorageStatsResult.ViewInfo]
    pagination_cookie: str
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., view_info_vec: _Optional[_Iterable[_Union[GetViewStorageStatsResult.ViewInfo, _Mapping]]] = ..., pagination_cookie: _Optional[str] = ...) -> None: ...
