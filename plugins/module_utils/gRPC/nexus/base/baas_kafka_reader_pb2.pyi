from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class KafkaAirflowBetbStatsEvent(_message.Message):
    __slots__ = ("header", "body")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    header: KafkaEventAirflowHeader
    body: _containers.RepeatedCompositeFieldContainer[BetbUsageStatEvent]
    def __init__(self, header: _Optional[_Union[KafkaEventAirflowHeader, _Mapping]] = ..., body: _Optional[_Iterable[_Union[BetbUsageStatEvent, _Mapping]]] = ...) -> None: ...

class KafkaEventAirflowHeader(_message.Message):
    __slots__ = ("event_type", "task_id", "publish_timestamp")
    EVENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    PUBLISH_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    event_type: str
    task_id: int
    publish_timestamp: int
    def __init__(self, event_type: _Optional[str] = ..., task_id: _Optional[int] = ..., publish_timestamp: _Optional[int] = ...) -> None: ...

class BetbUsageStatEvent(_message.Message):
    __slots__ = ("tenant_id", "region_id", "usage_bytes", "usage_timestamp", "calendar_month_timestamp")
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    REGION_ID_FIELD_NUMBER: _ClassVar[int]
    USAGE_BYTES_FIELD_NUMBER: _ClassVar[int]
    USAGE_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    CALENDAR_MONTH_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    tenant_id: str
    region_id: str
    usage_bytes: int
    usage_timestamp: int
    calendar_month_timestamp: int
    def __init__(self, tenant_id: _Optional[str] = ..., region_id: _Optional[str] = ..., usage_bytes: _Optional[int] = ..., usage_timestamp: _Optional[int] = ..., calendar_month_timestamp: _Optional[int] = ...) -> None: ...

class KafkaAirflowFetbStatsEvent(_message.Message):
    __slots__ = ("header", "body")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    header: KafkaEventAirflowHeader
    body: _containers.RepeatedCompositeFieldContainer[FetbUsageStatEvent]
    def __init__(self, header: _Optional[_Union[KafkaEventAirflowHeader, _Mapping]] = ..., body: _Optional[_Iterable[_Union[FetbUsageStatEvent, _Mapping]]] = ...) -> None: ...

class FetbUsageStatEvent(_message.Message):
    __slots__ = ("tenant_id", "cluster_identifier", "entity_id", "calendar_month_timestamp_secs", "usage_bytes", "usage_timestamp_secs", "protection_env_type", "source_env_type", "aux_entity_id", "network_realm_id", "connector_group_id")
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    CALENDAR_MONTH_TIMESTAMP_SECS_FIELD_NUMBER: _ClassVar[int]
    USAGE_BYTES_FIELD_NUMBER: _ClassVar[int]
    USAGE_TIMESTAMP_SECS_FIELD_NUMBER: _ClassVar[int]
    PROTECTION_ENV_TYPE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_ENV_TYPE_FIELD_NUMBER: _ClassVar[int]
    AUX_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    NETWORK_REALM_ID_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    tenant_id: str
    cluster_identifier: str
    entity_id: int
    calendar_month_timestamp_secs: int
    usage_bytes: int
    usage_timestamp_secs: int
    protection_env_type: int
    source_env_type: int
    aux_entity_id: int
    network_realm_id: int
    connector_group_id: int
    def __init__(self, tenant_id: _Optional[str] = ..., cluster_identifier: _Optional[str] = ..., entity_id: _Optional[int] = ..., calendar_month_timestamp_secs: _Optional[int] = ..., usage_bytes: _Optional[int] = ..., usage_timestamp_secs: _Optional[int] = ..., protection_env_type: _Optional[int] = ..., source_env_type: _Optional[int] = ..., aux_entity_id: _Optional[int] = ..., network_realm_id: _Optional[int] = ..., connector_group_id: _Optional[int] = ...) -> None: ...

class KafkaAirflowM365StatsEvent(_message.Message):
    __slots__ = ("header", "body")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    header: KafkaEventAirflowHeader
    body: _containers.RepeatedCompositeFieldContainer[M365UsageStatEvent]
    def __init__(self, header: _Optional[_Union[KafkaEventAirflowHeader, _Mapping]] = ..., body: _Optional[_Iterable[_Union[M365UsageStatEvent, _Mapping]]] = ...) -> None: ...

class M365UsageStatEvent(_message.Message):
    __slots__ = ("tenant_id", "cluster_identifier", "calendar_month_timestamp_secs", "peak_user_count", "total_protected_users")
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    CALENDAR_MONTH_TIMESTAMP_SECS_FIELD_NUMBER: _ClassVar[int]
    PEAK_USER_COUNT_FIELD_NUMBER: _ClassVar[int]
    TOTAL_PROTECTED_USERS_FIELD_NUMBER: _ClassVar[int]
    tenant_id: str
    cluster_identifier: str
    calendar_month_timestamp_secs: int
    peak_user_count: int
    total_protected_users: int
    def __init__(self, tenant_id: _Optional[str] = ..., cluster_identifier: _Optional[str] = ..., calendar_month_timestamp_secs: _Optional[int] = ..., peak_user_count: _Optional[int] = ..., total_protected_users: _Optional[int] = ...) -> None: ...
