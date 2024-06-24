from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class BkClientType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kRest: _ClassVar[BkClientType]
    kGrpc: _ClassVar[BkClientType]
    kRedis: _ClassVar[BkClientType]
kRest: BkClientType
kGrpc: BkClientType
kRedis: BkClientType

class BookkeeperUrisProto(_message.Message):
    __slots__ = ("kub_bk_hostname", "api_version", "base_uri", "status_uri", "copy_tasks_uri", "pg_status_uri", "es_status_uri", "bk_status_uri", "kafka_status_uri", "gflag_config", "app_health", "debug_info_describe_pod", "debug_info_gflags")
    KUB_BK_HOSTNAME_FIELD_NUMBER: _ClassVar[int]
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    BASE_URI_FIELD_NUMBER: _ClassVar[int]
    STATUS_URI_FIELD_NUMBER: _ClassVar[int]
    COPY_TASKS_URI_FIELD_NUMBER: _ClassVar[int]
    PG_STATUS_URI_FIELD_NUMBER: _ClassVar[int]
    ES_STATUS_URI_FIELD_NUMBER: _ClassVar[int]
    BK_STATUS_URI_FIELD_NUMBER: _ClassVar[int]
    KAFKA_STATUS_URI_FIELD_NUMBER: _ClassVar[int]
    GFLAG_CONFIG_FIELD_NUMBER: _ClassVar[int]
    APP_HEALTH_FIELD_NUMBER: _ClassVar[int]
    DEBUG_INFO_DESCRIBE_POD_FIELD_NUMBER: _ClassVar[int]
    DEBUG_INFO_GFLAGS_FIELD_NUMBER: _ClassVar[int]
    kub_bk_hostname: str
    api_version: str
    base_uri: str
    status_uri: str
    copy_tasks_uri: str
    pg_status_uri: str
    es_status_uri: str
    bk_status_uri: str
    kafka_status_uri: str
    gflag_config: str
    app_health: str
    debug_info_describe_pod: str
    debug_info_gflags: str
    def __init__(self, kub_bk_hostname: _Optional[str] = ..., api_version: _Optional[str] = ..., base_uri: _Optional[str] = ..., status_uri: _Optional[str] = ..., copy_tasks_uri: _Optional[str] = ..., pg_status_uri: _Optional[str] = ..., es_status_uri: _Optional[str] = ..., bk_status_uri: _Optional[str] = ..., kafka_status_uri: _Optional[str] = ..., gflag_config: _Optional[str] = ..., app_health: _Optional[str] = ..., debug_info_describe_pod: _Optional[str] = ..., debug_info_gflags: _Optional[str] = ...) -> None: ...
