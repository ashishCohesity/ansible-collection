from aegis.base import error_pb2 as _error_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ComponentState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kHealthy: _ClassVar[ComponentState]
    kUnhealthy: _ClassVar[ComponentState]
    kIsolated: _ClassVar[ComponentState]
    kMarkedForRemoval: _ClassVar[ComponentState]
kHealthy: ComponentState
kUnhealthy: ComponentState
kIsolated: ComponentState
kMarkedForRemoval: ComponentState

class ComponentIdentifier(_message.Message):
    __slots__ = ("service_scope", "component_type", "component_id", "attribute_vec")
    SERVICE_SCOPE_FIELD_NUMBER: _ClassVar[int]
    COMPONENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    COMPONENT_ID_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTE_VEC_FIELD_NUMBER: _ClassVar[int]
    service_scope: str
    component_type: str
    component_id: str
    attribute_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, service_scope: _Optional[str] = ..., component_type: _Optional[str] = ..., component_id: _Optional[str] = ..., attribute_vec: _Optional[_Iterable[str]] = ...) -> None: ...

class ComponentHealthProto(_message.Message):
    __slots__ = ("id", "state", "reason", "last_transition_timestamp_secs", "recovery_action_vec", "history")
    class RecoveryAction(_message.Message):
        __slots__ = ("action", "start_timestamp_secs", "end_timestamp_secs", "state", "owner", "num_attempts")
        class RecoveryActionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kRestartService: _ClassVar[ComponentHealthProto.RecoveryAction.RecoveryActionType]
            kShutdownService: _ClassVar[ComponentHealthProto.RecoveryAction.RecoveryActionType]
            kRestartNode: _ClassVar[ComponentHealthProto.RecoveryAction.RecoveryActionType]
            kShutdownNode: _ClassVar[ComponentHealthProto.RecoveryAction.RecoveryActionType]
        kRestartService: ComponentHealthProto.RecoveryAction.RecoveryActionType
        kShutdownService: ComponentHealthProto.RecoveryAction.RecoveryActionType
        kRestartNode: ComponentHealthProto.RecoveryAction.RecoveryActionType
        kShutdownNode: ComponentHealthProto.RecoveryAction.RecoveryActionType
        class RecoveryActionState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kInProgress: _ClassVar[ComponentHealthProto.RecoveryAction.RecoveryActionState]
            kCompleted: _ClassVar[ComponentHealthProto.RecoveryAction.RecoveryActionState]
            kNotStarted: _ClassVar[ComponentHealthProto.RecoveryAction.RecoveryActionState]
        kInProgress: ComponentHealthProto.RecoveryAction.RecoveryActionState
        kCompleted: ComponentHealthProto.RecoveryAction.RecoveryActionState
        kNotStarted: ComponentHealthProto.RecoveryAction.RecoveryActionState
        ACTION_FIELD_NUMBER: _ClassVar[int]
        START_TIMESTAMP_SECS_FIELD_NUMBER: _ClassVar[int]
        END_TIMESTAMP_SECS_FIELD_NUMBER: _ClassVar[int]
        STATE_FIELD_NUMBER: _ClassVar[int]
        OWNER_FIELD_NUMBER: _ClassVar[int]
        NUM_ATTEMPTS_FIELD_NUMBER: _ClassVar[int]
        action: ComponentHealthProto.RecoveryAction.RecoveryActionType
        start_timestamp_secs: int
        end_timestamp_secs: int
        state: ComponentHealthProto.RecoveryAction.RecoveryActionState
        owner: str
        num_attempts: int
        def __init__(self, action: _Optional[_Union[ComponentHealthProto.RecoveryAction.RecoveryActionType, str]] = ..., start_timestamp_secs: _Optional[int] = ..., end_timestamp_secs: _Optional[int] = ..., state: _Optional[_Union[ComponentHealthProto.RecoveryAction.RecoveryActionState, str]] = ..., owner: _Optional[str] = ..., num_attempts: _Optional[int] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    LAST_TRANSITION_TIMESTAMP_SECS_FIELD_NUMBER: _ClassVar[int]
    RECOVERY_ACTION_VEC_FIELD_NUMBER: _ClassVar[int]
    HISTORY_FIELD_NUMBER: _ClassVar[int]
    id: ComponentIdentifier
    state: ComponentState
    reason: str
    last_transition_timestamp_secs: int
    recovery_action_vec: _containers.RepeatedCompositeFieldContainer[ComponentHealthProto.RecoveryAction]
    history: _containers.RepeatedCompositeFieldContainer[ComponentStateHistory]
    def __init__(self, id: _Optional[_Union[ComponentIdentifier, _Mapping]] = ..., state: _Optional[_Union[ComponentState, str]] = ..., reason: _Optional[str] = ..., last_transition_timestamp_secs: _Optional[int] = ..., recovery_action_vec: _Optional[_Iterable[_Union[ComponentHealthProto.RecoveryAction, _Mapping]]] = ..., history: _Optional[_Iterable[_Union[ComponentStateHistory, _Mapping]]] = ...) -> None: ...

class HealthMetric(_message.Message):
    __slots__ = ("metric_name", "metric_value", "timestamp_secs")
    METRIC_NAME_FIELD_NUMBER: _ClassVar[int]
    METRIC_VALUE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_SECS_FIELD_NUMBER: _ClassVar[int]
    metric_name: str
    metric_value: str
    timestamp_secs: int
    def __init__(self, metric_name: _Optional[str] = ..., metric_value: _Optional[str] = ..., timestamp_secs: _Optional[int] = ...) -> None: ...

class ComponentStateHistory(_message.Message):
    __slots__ = ("state", "metric_name", "metric_value", "timestamp_secs", "threshold_value", "reason", "rule", "metric_vec")
    STATE_FIELD_NUMBER: _ClassVar[int]
    METRIC_NAME_FIELD_NUMBER: _ClassVar[int]
    METRIC_VALUE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_SECS_FIELD_NUMBER: _ClassVar[int]
    THRESHOLD_VALUE_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    RULE_FIELD_NUMBER: _ClassVar[int]
    METRIC_VEC_FIELD_NUMBER: _ClassVar[int]
    state: ComponentState
    metric_name: str
    metric_value: str
    timestamp_secs: int
    threshold_value: int
    reason: str
    rule: str
    metric_vec: _containers.RepeatedCompositeFieldContainer[HealthMetric]
    def __init__(self, state: _Optional[_Union[ComponentState, str]] = ..., metric_name: _Optional[str] = ..., metric_value: _Optional[str] = ..., timestamp_secs: _Optional[int] = ..., threshold_value: _Optional[int] = ..., reason: _Optional[str] = ..., rule: _Optional[str] = ..., metric_vec: _Optional[_Iterable[_Union[HealthMetric, _Mapping]]] = ...) -> None: ...

class ComponentHealthRegistryProto(_message.Message):
    __slots__ = ("service_scope_map", "ids_in_isolation_vec", "num_components_marked_for_removal")
    class ServiceScope(_message.Message):
        __slots__ = ("component_health_map",)
        class ComponentHealthMapEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: ComponentHealthProto
            def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[ComponentHealthProto, _Mapping]] = ...) -> None: ...
        COMPONENT_HEALTH_MAP_FIELD_NUMBER: _ClassVar[int]
        component_health_map: _containers.MessageMap[str, ComponentHealthProto]
        def __init__(self, component_health_map: _Optional[_Mapping[str, ComponentHealthProto]] = ...) -> None: ...
    class ServiceScopeMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: ComponentHealthRegistryProto.ServiceScope
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[ComponentHealthRegistryProto.ServiceScope, _Mapping]] = ...) -> None: ...
    SERVICE_SCOPE_MAP_FIELD_NUMBER: _ClassVar[int]
    IDS_IN_ISOLATION_VEC_FIELD_NUMBER: _ClassVar[int]
    NUM_COMPONENTS_MARKED_FOR_REMOVAL_FIELD_NUMBER: _ClassVar[int]
    service_scope_map: _containers.MessageMap[str, ComponentHealthRegistryProto.ServiceScope]
    ids_in_isolation_vec: _containers.RepeatedCompositeFieldContainer[ComponentIdentifier]
    num_components_marked_for_removal: int
    def __init__(self, service_scope_map: _Optional[_Mapping[str, ComponentHealthRegistryProto.ServiceScope]] = ..., ids_in_isolation_vec: _Optional[_Iterable[_Union[ComponentIdentifier, _Mapping]]] = ..., num_components_marked_for_removal: _Optional[int] = ...) -> None: ...

class PublishComponentsHealthArg(_message.Message):
    __slots__ = ("component_health_vec",)
    class PublishComponentHealth(_message.Message):
        __slots__ = ("id", "source_id", "metric_vec")
        ID_FIELD_NUMBER: _ClassVar[int]
        SOURCE_ID_FIELD_NUMBER: _ClassVar[int]
        METRIC_VEC_FIELD_NUMBER: _ClassVar[int]
        id: ComponentIdentifier
        source_id: str
        metric_vec: _containers.RepeatedCompositeFieldContainer[HealthMetric]
        def __init__(self, id: _Optional[_Union[ComponentIdentifier, _Mapping]] = ..., source_id: _Optional[str] = ..., metric_vec: _Optional[_Iterable[_Union[HealthMetric, _Mapping]]] = ...) -> None: ...
    COMPONENT_HEALTH_VEC_FIELD_NUMBER: _ClassVar[int]
    component_health_vec: _containers.RepeatedCompositeFieldContainer[PublishComponentsHealthArg.PublishComponentHealth]
    def __init__(self, component_health_vec: _Optional[_Iterable[_Union[PublishComponentsHealthArg.PublishComponentHealth, _Mapping]]] = ...) -> None: ...

class PublishComponentsHealthResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class SubscribeComponentsHealthArg(_message.Message):
    __slots__ = ("id_vec",)
    ID_VEC_FIELD_NUMBER: _ClassVar[int]
    id_vec: _containers.RepeatedCompositeFieldContainer[ComponentIdentifier]
    def __init__(self, id_vec: _Optional[_Iterable[_Union[ComponentIdentifier, _Mapping]]] = ...) -> None: ...

class SubscribeComponentsHealthResult(_message.Message):
    __slots__ = ("error", "component_health_vec")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    COMPONENT_HEALTH_VEC_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    component_health_vec: _containers.RepeatedCompositeFieldContainer[ComponentHealthProto]
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., component_health_vec: _Optional[_Iterable[_Union[ComponentHealthProto, _Mapping]]] = ...) -> None: ...

class UnsubscribeComponentsHealthArg(_message.Message):
    __slots__ = ("id_vec",)
    ID_VEC_FIELD_NUMBER: _ClassVar[int]
    id_vec: _containers.RepeatedCompositeFieldContainer[ComponentIdentifier]
    def __init__(self, id_vec: _Optional[_Iterable[_Union[ComponentIdentifier, _Mapping]]] = ...) -> None: ...

class GetComponentsHealthArg(_message.Message):
    __slots__ = ("id_vec",)
    ID_VEC_FIELD_NUMBER: _ClassVar[int]
    id_vec: _containers.RepeatedCompositeFieldContainer[ComponentIdentifier]
    def __init__(self, id_vec: _Optional[_Iterable[_Union[ComponentIdentifier, _Mapping]]] = ...) -> None: ...

class GetComponentsHealthResult(_message.Message):
    __slots__ = ("component_health_vec", "error")
    COMPONENT_HEALTH_VEC_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    component_health_vec: _containers.RepeatedCompositeFieldContainer[ComponentHealthProto]
    error: _error_pb2.ErrorProto
    def __init__(self, component_health_vec: _Optional[_Iterable[_Union[ComponentHealthProto, _Mapping]]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class AegisConfigProto(_message.Message):
    __slots__ = ("aegis_master_key", "component_health_registry_key")
    AEGIS_MASTER_KEY_FIELD_NUMBER: _ClassVar[int]
    COMPONENT_HEALTH_REGISTRY_KEY_FIELD_NUMBER: _ClassVar[int]
    aegis_master_key: str
    component_health_registry_key: str
    def __init__(self, aegis_master_key: _Optional[str] = ..., component_health_registry_key: _Optional[str] = ...) -> None: ...
