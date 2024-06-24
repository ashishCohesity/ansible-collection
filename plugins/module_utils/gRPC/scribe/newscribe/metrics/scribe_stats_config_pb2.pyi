from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ScribeStatsConfigProto(_message.Message):
    __slots__ = ("time_to_live_secs", "scribe_table_instance_stats_schema_name", "scribe_table_instance_stats_schema_version", "table_instance_id_attr", "scribe_table_cluster_stats_schema_name", "scribe_table_cluster_stats_schema_version", "table_id_attr", "scribe_server_instance_client_stats_schema_name", "scribe_server_instance_client_stats_schema_version", "scribe_server_instance_scribe_server_client_id_attr", "scribe_server_client_stats_schema_name", "scribe_server_client_stats_schema_version", "scribe_server_client_id_attr", "scribe_server_qos_queue_stats_schema_name", "scribe_server_qos_queue_stats_schema_version", "scribe_server_qos_queue_id_attr")
    TIME_TO_LIVE_SECS_FIELD_NUMBER: _ClassVar[int]
    SCRIBE_TABLE_INSTANCE_STATS_SCHEMA_NAME_FIELD_NUMBER: _ClassVar[int]
    SCRIBE_TABLE_INSTANCE_STATS_SCHEMA_VERSION_FIELD_NUMBER: _ClassVar[int]
    TABLE_INSTANCE_ID_ATTR_FIELD_NUMBER: _ClassVar[int]
    SCRIBE_TABLE_CLUSTER_STATS_SCHEMA_NAME_FIELD_NUMBER: _ClassVar[int]
    SCRIBE_TABLE_CLUSTER_STATS_SCHEMA_VERSION_FIELD_NUMBER: _ClassVar[int]
    TABLE_ID_ATTR_FIELD_NUMBER: _ClassVar[int]
    SCRIBE_SERVER_INSTANCE_CLIENT_STATS_SCHEMA_NAME_FIELD_NUMBER: _ClassVar[int]
    SCRIBE_SERVER_INSTANCE_CLIENT_STATS_SCHEMA_VERSION_FIELD_NUMBER: _ClassVar[int]
    SCRIBE_SERVER_INSTANCE_SCRIBE_SERVER_CLIENT_ID_ATTR_FIELD_NUMBER: _ClassVar[int]
    SCRIBE_SERVER_CLIENT_STATS_SCHEMA_NAME_FIELD_NUMBER: _ClassVar[int]
    SCRIBE_SERVER_CLIENT_STATS_SCHEMA_VERSION_FIELD_NUMBER: _ClassVar[int]
    SCRIBE_SERVER_CLIENT_ID_ATTR_FIELD_NUMBER: _ClassVar[int]
    SCRIBE_SERVER_QOS_QUEUE_STATS_SCHEMA_NAME_FIELD_NUMBER: _ClassVar[int]
    SCRIBE_SERVER_QOS_QUEUE_STATS_SCHEMA_VERSION_FIELD_NUMBER: _ClassVar[int]
    SCRIBE_SERVER_QOS_QUEUE_ID_ATTR_FIELD_NUMBER: _ClassVar[int]
    time_to_live_secs: int
    scribe_table_instance_stats_schema_name: str
    scribe_table_instance_stats_schema_version: int
    table_instance_id_attr: str
    scribe_table_cluster_stats_schema_name: str
    scribe_table_cluster_stats_schema_version: int
    table_id_attr: str
    scribe_server_instance_client_stats_schema_name: str
    scribe_server_instance_client_stats_schema_version: int
    scribe_server_instance_scribe_server_client_id_attr: str
    scribe_server_client_stats_schema_name: str
    scribe_server_client_stats_schema_version: int
    scribe_server_client_id_attr: str
    scribe_server_qos_queue_stats_schema_name: str
    scribe_server_qos_queue_stats_schema_version: int
    scribe_server_qos_queue_id_attr: str
    def __init__(self, time_to_live_secs: _Optional[int] = ..., scribe_table_instance_stats_schema_name: _Optional[str] = ..., scribe_table_instance_stats_schema_version: _Optional[int] = ..., table_instance_id_attr: _Optional[str] = ..., scribe_table_cluster_stats_schema_name: _Optional[str] = ..., scribe_table_cluster_stats_schema_version: _Optional[int] = ..., table_id_attr: _Optional[str] = ..., scribe_server_instance_client_stats_schema_name: _Optional[str] = ..., scribe_server_instance_client_stats_schema_version: _Optional[int] = ..., scribe_server_instance_scribe_server_client_id_attr: _Optional[str] = ..., scribe_server_client_stats_schema_name: _Optional[str] = ..., scribe_server_client_stats_schema_version: _Optional[int] = ..., scribe_server_client_id_attr: _Optional[str] = ..., scribe_server_qos_queue_stats_schema_name: _Optional[str] = ..., scribe_server_qos_queue_stats_schema_version: _Optional[int] = ..., scribe_server_qos_queue_id_attr: _Optional[str] = ...) -> None: ...
