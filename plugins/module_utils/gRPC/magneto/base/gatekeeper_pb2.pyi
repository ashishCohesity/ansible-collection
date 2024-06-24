from magneto.base import entity_pb2 as _entity_pb2
from magneto.base import enums_pb2 as _enums_pb2
from magneto.base import proxy_pb2 as _proxy_pb2
from magneto.resource_providers import resource_pb2 as _resource_pb2
from resource_manager.base import logical_timestamp_pb2 as _logical_timestamp_pb2
from util.base import universal_id_pb2 as _universal_id_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ResourceProto(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kBridge: _ClassVar[ResourceProto.Type]
    kBridge: ResourceProto.Type
    def __init__(self) -> None: ...

class ResourceProperty(_message.Message):
    __slots__ = ("type",)
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kFibreChannel: _ClassVar[ResourceProperty.Type]
    kFibreChannel: ResourceProperty.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    type: ResourceProperty.Type
    def __init__(self, type: _Optional[_Union[ResourceProperty.Type, str]] = ...) -> None: ...

class ResourceConstraint(_message.Message):
    __slots__ = ("type", "property_vec", "schedule_sub_tasks_on_separate_resources")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    PROPERTY_VEC_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_SUB_TASKS_ON_SEPARATE_RESOURCES_FIELD_NUMBER: _ClassVar[int]
    type: ResourceProto.Type
    property_vec: _containers.RepeatedCompositeFieldContainer[ResourceProperty]
    schedule_sub_tasks_on_separate_resources: bool
    def __init__(self, type: _Optional[_Union[ResourceProto.Type, str]] = ..., property_vec: _Optional[_Iterable[_Union[ResourceProperty, _Mapping]]] = ..., schedule_sub_tasks_on_separate_resources: bool = ...) -> None: ...

class O365Resource(_message.Message):
    __slots__ = ("type", "parent_entity_id", "affinity_constituent_id")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kApplication: _ClassVar[O365Resource.Type]
        kPowerShell: _ClassVar[O365Resource.Type]
    kApplication: O365Resource.Type
    kPowerShell: O365Resource.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    PARENT_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    AFFINITY_CONSTITUENT_ID_FIELD_NUMBER: _ClassVar[int]
    type: O365Resource.Type
    parent_entity_id: int
    affinity_constituent_id: int
    def __init__(self, type: _Optional[_Union[O365Resource.Type, str]] = ..., parent_entity_id: _Optional[int] = ..., affinity_constituent_id: _Optional[int] = ...) -> None: ...

class Task(_message.Message):
    __slots__ = ("task_id", "sub_task_id", "version", "entities", "proxy_info_vec", "entities_to_lock", "entities_to_lock_shared_mode", "assign_bridge", "assign_control_path_slot", "assign_proxy_arg", "partition_id", "task_uid", "resource_constraint_vec", "target_type", "weight_percent", "o365_permit_requests", "parent_task_id", "resource_requests")
    class ResourceRequest(_message.Message):
        __slots__ = ("entity", "usage_requested", "resource_type")
        ENTITY_FIELD_NUMBER: _ClassVar[int]
        USAGE_REQUESTED_FIELD_NUMBER: _ClassVar[int]
        RESOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
        entity: _entity_pb2.EntityProto
        usage_requested: int
        resource_type: _resource_pb2.ResourceProto.Type
        def __init__(self, entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., usage_requested: _Optional[int] = ..., resource_type: _Optional[_Union[_resource_pb2.ResourceProto.Type, str]] = ...) -> None: ...
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    SUB_TASK_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    ENTITIES_FIELD_NUMBER: _ClassVar[int]
    PROXY_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    ENTITIES_TO_LOCK_FIELD_NUMBER: _ClassVar[int]
    ENTITIES_TO_LOCK_SHARED_MODE_FIELD_NUMBER: _ClassVar[int]
    ASSIGN_BRIDGE_FIELD_NUMBER: _ClassVar[int]
    ASSIGN_CONTROL_PATH_SLOT_FIELD_NUMBER: _ClassVar[int]
    ASSIGN_PROXY_ARG_FIELD_NUMBER: _ClassVar[int]
    PARTITION_ID_FIELD_NUMBER: _ClassVar[int]
    TASK_UID_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_CONSTRAINT_VEC_FIELD_NUMBER: _ClassVar[int]
    TARGET_TYPE_FIELD_NUMBER: _ClassVar[int]
    WEIGHT_PERCENT_FIELD_NUMBER: _ClassVar[int]
    O365_PERMIT_REQUESTS_FIELD_NUMBER: _ClassVar[int]
    PARENT_TASK_ID_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_REQUESTS_FIELD_NUMBER: _ClassVar[int]
    task_id: int
    sub_task_id: int
    version: int
    entities: _containers.RepeatedCompositeFieldContainer[_entity_pb2.EntityProto]
    proxy_info_vec: _containers.RepeatedCompositeFieldContainer[_proxy_pb2.ProxyInfo]
    entities_to_lock: _containers.RepeatedCompositeFieldContainer[_entity_pb2.EntityProto]
    entities_to_lock_shared_mode: _containers.RepeatedCompositeFieldContainer[_entity_pb2.EntityProto]
    assign_bridge: bool
    assign_control_path_slot: bool
    assign_proxy_arg: _proxy_pb2.AssignProxyArg
    partition_id: int
    task_uid: _universal_id_pb2.UniversalIdProto
    resource_constraint_vec: _containers.RepeatedCompositeFieldContainer[ResourceConstraint]
    target_type: _enums_pb2.TargetType.Type
    weight_percent: int
    o365_permit_requests: _containers.RepeatedCompositeFieldContainer[O365Resource]
    parent_task_id: int
    resource_requests: _containers.RepeatedCompositeFieldContainer[Task.ResourceRequest]
    def __init__(self, task_id: _Optional[int] = ..., sub_task_id: _Optional[int] = ..., version: _Optional[int] = ..., entities: _Optional[_Iterable[_Union[_entity_pb2.EntityProto, _Mapping]]] = ..., proxy_info_vec: _Optional[_Iterable[_Union[_proxy_pb2.ProxyInfo, _Mapping]]] = ..., entities_to_lock: _Optional[_Iterable[_Union[_entity_pb2.EntityProto, _Mapping]]] = ..., entities_to_lock_shared_mode: _Optional[_Iterable[_Union[_entity_pb2.EntityProto, _Mapping]]] = ..., assign_bridge: bool = ..., assign_control_path_slot: bool = ..., assign_proxy_arg: _Optional[_Union[_proxy_pb2.AssignProxyArg, _Mapping]] = ..., partition_id: _Optional[int] = ..., task_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., resource_constraint_vec: _Optional[_Iterable[_Union[ResourceConstraint, _Mapping]]] = ..., target_type: _Optional[_Union[_enums_pb2.TargetType.Type, str]] = ..., weight_percent: _Optional[int] = ..., o365_permit_requests: _Optional[_Iterable[_Union[O365Resource, _Mapping]]] = ..., parent_task_id: _Optional[int] = ..., resource_requests: _Optional[_Iterable[_Union[Task.ResourceRequest, _Mapping]]] = ...) -> None: ...

class TaskState(_message.Message):
    __slots__ = ("status", "is_parent_token", "is_token_free", "constituent_id", "proxy_info", "target_type", "permitted_timestamp_usecs", "release_timestamp_usecs", "unlocked_entities", "o365_grants", "latest_logical_timestamp")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kRequested: _ClassVar[TaskState.Status]
        kPermitted: _ClassVar[TaskState.Status]
        kReleased: _ClassVar[TaskState.Status]
    kRequested: TaskState.Status
    kPermitted: TaskState.Status
    kReleased: TaskState.Status
    class O365Grant(_message.Message):
        __slots__ = ("request_info", "application", "is_parent_token", "is_token_free", "constituent_id")
        REQUEST_INFO_FIELD_NUMBER: _ClassVar[int]
        APPLICATION_FIELD_NUMBER: _ClassVar[int]
        IS_PARENT_TOKEN_FIELD_NUMBER: _ClassVar[int]
        IS_TOKEN_FREE_FIELD_NUMBER: _ClassVar[int]
        CONSTITUENT_ID_FIELD_NUMBER: _ClassVar[int]
        request_info: O365Resource
        application: str
        is_parent_token: bool
        is_token_free: bool
        constituent_id: int
        def __init__(self, request_info: _Optional[_Union[O365Resource, _Mapping]] = ..., application: _Optional[str] = ..., is_parent_token: bool = ..., is_token_free: bool = ..., constituent_id: _Optional[int] = ...) -> None: ...
    STATUS_FIELD_NUMBER: _ClassVar[int]
    IS_PARENT_TOKEN_FIELD_NUMBER: _ClassVar[int]
    IS_TOKEN_FREE_FIELD_NUMBER: _ClassVar[int]
    CONSTITUENT_ID_FIELD_NUMBER: _ClassVar[int]
    PROXY_INFO_FIELD_NUMBER: _ClassVar[int]
    TARGET_TYPE_FIELD_NUMBER: _ClassVar[int]
    PERMITTED_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
    RELEASE_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
    UNLOCKED_ENTITIES_FIELD_NUMBER: _ClassVar[int]
    O365_GRANTS_FIELD_NUMBER: _ClassVar[int]
    LATEST_LOGICAL_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    status: TaskState.Status
    is_parent_token: _containers.RepeatedScalarFieldContainer[bool]
    is_token_free: _containers.RepeatedScalarFieldContainer[bool]
    constituent_id: int
    proxy_info: _proxy_pb2.ProxyInfo
    target_type: _enums_pb2.TargetType.Type
    permitted_timestamp_usecs: int
    release_timestamp_usecs: int
    unlocked_entities: _containers.RepeatedCompositeFieldContainer[_entity_pb2.EntityProto]
    o365_grants: _containers.RepeatedCompositeFieldContainer[TaskState.O365Grant]
    latest_logical_timestamp: _logical_timestamp_pb2.LogicalTimestamp
    def __init__(self, status: _Optional[_Union[TaskState.Status, str]] = ..., is_parent_token: _Optional[_Iterable[bool]] = ..., is_token_free: _Optional[_Iterable[bool]] = ..., constituent_id: _Optional[int] = ..., proxy_info: _Optional[_Union[_proxy_pb2.ProxyInfo, _Mapping]] = ..., target_type: _Optional[_Union[_enums_pb2.TargetType.Type, str]] = ..., permitted_timestamp_usecs: _Optional[int] = ..., release_timestamp_usecs: _Optional[int] = ..., unlocked_entities: _Optional[_Iterable[_Union[_entity_pb2.EntityProto, _Mapping]]] = ..., o365_grants: _Optional[_Iterable[_Union[TaskState.O365Grant, _Mapping]]] = ..., latest_logical_timestamp: _Optional[_Union[_logical_timestamp_pb2.LogicalTimestamp, _Mapping]] = ...) -> None: ...
