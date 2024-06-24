from bookkeeper.base import bookkeeper_pb2 as _bookkeeper_pb2
from bookkeeper.base import error_pb2 as _error_pb2
from open_util.net import protorpc_pb2 as _protorpc_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ReserveGroupIdArg(_message.Message):
    __slots__ = ("attributes",)
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    attributes: _bookkeeper_pb2.GroupAttributesProto
    def __init__(self, attributes: _Optional[_Union[_bookkeeper_pb2.GroupAttributesProto, _Mapping]] = ...) -> None: ...

class ReserveGroupIdResult(_message.Message):
    __slots__ = ("group_id",)
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    group_id: int
    def __init__(self, group_id: _Optional[int] = ...) -> None: ...

class CreateOrUpdateGroupArg(_message.Message):
    __slots__ = ("config", "group_id")
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    config: _bookkeeper_pb2.GroupConfigProto
    group_id: int
    def __init__(self, config: _Optional[_Union[_bookkeeper_pb2.GroupConfigProto, _Mapping]] = ..., group_id: _Optional[int] = ...) -> None: ...

class CreateOrUpdateGroupResult(_message.Message):
    __slots__ = ("group_id",)
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    group_id: int
    def __init__(self, group_id: _Optional[int] = ...) -> None: ...

class RetrieveGroupArg(_message.Message):
    __slots__ = ("group_id",)
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    group_id: int
    def __init__(self, group_id: _Optional[int] = ...) -> None: ...

class RetrieveGroupResult(_message.Message):
    __slots__ = ("config",)
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    config: _bookkeeper_pb2.GroupConfigProto
    def __init__(self, config: _Optional[_Union[_bookkeeper_pb2.GroupConfigProto, _Mapping]] = ...) -> None: ...

class DeleteGroupArg(_message.Message):
    __slots__ = ("group_id",)
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    group_id: int
    def __init__(self, group_id: _Optional[int] = ...) -> None: ...

class DeleteGroupResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AddObjectsToGroupArg(_message.Message):
    __slots__ = ("group_id", "objects_vec", "view_name_vec")
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECTS_VEC_FIELD_NUMBER: _ClassVar[int]
    VIEW_NAME_VEC_FIELD_NUMBER: _ClassVar[int]
    group_id: int
    objects_vec: _containers.RepeatedCompositeFieldContainer[_bookkeeper_pb2.ObjectProto]
    view_name_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, group_id: _Optional[int] = ..., objects_vec: _Optional[_Iterable[_Union[_bookkeeper_pb2.ObjectProto, _Mapping]]] = ..., view_name_vec: _Optional[_Iterable[str]] = ...) -> None: ...

class AddObjectsToGroupResult(_message.Message):
    __slots__ = ("error_view_name_vec",)
    ERROR_VIEW_NAME_VEC_FIELD_NUMBER: _ClassVar[int]
    error_view_name_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, error_view_name_vec: _Optional[_Iterable[str]] = ...) -> None: ...

class DeleteObjectsOrSubGroupsFromGroupArg(_message.Message):
    __slots__ = ("group_id", "objects_vec", "sub_groups_vec")
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECTS_VEC_FIELD_NUMBER: _ClassVar[int]
    SUB_GROUPS_VEC_FIELD_NUMBER: _ClassVar[int]
    group_id: int
    objects_vec: _containers.RepeatedCompositeFieldContainer[_bookkeeper_pb2.ObjectProto]
    sub_groups_vec: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, group_id: _Optional[int] = ..., objects_vec: _Optional[_Iterable[_Union[_bookkeeper_pb2.ObjectProto, _Mapping]]] = ..., sub_groups_vec: _Optional[_Iterable[int]] = ...) -> None: ...

class DeleteObjectsOrSubGroupsFromGroupResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PublishGroupStatsArg(_message.Message):
    __slots__ = ("group_id", "group_status", "attributes")
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    GROUP_STATUS_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    group_id: int
    group_status: _bookkeeper_pb2.GroupStatusProto
    attributes: _bookkeeper_pb2.GroupAttributesProto
    def __init__(self, group_id: _Optional[int] = ..., group_status: _Optional[_Union[_bookkeeper_pb2.GroupStatusProto, _Mapping]] = ..., attributes: _Optional[_Union[_bookkeeper_pb2.GroupAttributesProto, _Mapping]] = ...) -> None: ...

class PublishGroupStatsResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetStorageStatsArg(_message.Message):
    __slots__ = ("is_base_group", "query_filter", "resource", "max_count", "pagination_cookie")
    class ResourceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNone: _ClassVar[GetStorageStatsArg.ResourceType]
        kTenant: _ClassVar[GetStorageStatsArg.ResourceType]
        kStorageDomain: _ClassVar[GetStorageStatsArg.ResourceType]
        kConsumer: _ClassVar[GetStorageStatsArg.ResourceType]
        kView: _ClassVar[GetStorageStatsArg.ResourceType]
        kJob: _ClassVar[GetStorageStatsArg.ResourceType]
    kNone: GetStorageStatsArg.ResourceType
    kTenant: GetStorageStatsArg.ResourceType
    kStorageDomain: GetStorageStatsArg.ResourceType
    kConsumer: GetStorageStatsArg.ResourceType
    kView: GetStorageStatsArg.ResourceType
    kJob: GetStorageStatsArg.ResourceType
    class GroupFilterProto(_message.Message):
        __slots__ = ("tenant_id_vec", "storage_domain_id_vec", "consumer", "null_tenant")
        TENANT_ID_VEC_FIELD_NUMBER: _ClassVar[int]
        STORAGE_DOMAIN_ID_VEC_FIELD_NUMBER: _ClassVar[int]
        CONSUMER_FIELD_NUMBER: _ClassVar[int]
        NULL_TENANT_FIELD_NUMBER: _ClassVar[int]
        tenant_id_vec: _containers.RepeatedScalarFieldContainer[str]
        storage_domain_id_vec: _containers.RepeatedScalarFieldContainer[int]
        consumer: _bookkeeper_pb2.ConsumerProto
        null_tenant: bool
        def __init__(self, tenant_id_vec: _Optional[_Iterable[str]] = ..., storage_domain_id_vec: _Optional[_Iterable[int]] = ..., consumer: _Optional[_Union[_bookkeeper_pb2.ConsumerProto, _Mapping]] = ..., null_tenant: bool = ...) -> None: ...
    IS_BASE_GROUP_FIELD_NUMBER: _ClassVar[int]
    QUERY_FILTER_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    MAX_COUNT_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_COOKIE_FIELD_NUMBER: _ClassVar[int]
    is_base_group: bool
    query_filter: GetStorageStatsArg.GroupFilterProto
    resource: GetStorageStatsArg.ResourceType
    max_count: int
    pagination_cookie: str
    def __init__(self, is_base_group: bool = ..., query_filter: _Optional[_Union[GetStorageStatsArg.GroupFilterProto, _Mapping]] = ..., resource: _Optional[_Union[GetStorageStatsArg.ResourceType, str]] = ..., max_count: _Optional[int] = ..., pagination_cookie: _Optional[str] = ...) -> None: ...

class GetStorageStatsResult(_message.Message):
    __slots__ = ("error", "group_info_vec", "pagination_cookie")
    class GroupInfo(_message.Message):
        __slots__ = ("group_id", "config", "status")
        GROUP_ID_FIELD_NUMBER: _ClassVar[int]
        CONFIG_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        group_id: int
        config: _bookkeeper_pb2.GroupConfigProto
        status: _bookkeeper_pb2.GroupStatusProto
        def __init__(self, group_id: _Optional[int] = ..., config: _Optional[_Union[_bookkeeper_pb2.GroupConfigProto, _Mapping]] = ..., status: _Optional[_Union[_bookkeeper_pb2.GroupStatusProto, _Mapping]] = ...) -> None: ...
    ERROR_FIELD_NUMBER: _ClassVar[int]
    GROUP_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_COOKIE_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    group_info_vec: _containers.RepeatedCompositeFieldContainer[GetStorageStatsResult.GroupInfo]
    pagination_cookie: str
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., group_info_vec: _Optional[_Iterable[_Union[GetStorageStatsResult.GroupInfo, _Mapping]]] = ..., pagination_cookie: _Optional[str] = ...) -> None: ...
