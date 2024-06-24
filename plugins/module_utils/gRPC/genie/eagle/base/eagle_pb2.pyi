from alerts.base import alert_pb2 as _alert_pb2
from configs import cluster_config_pb2 as _cluster_config_pb2
from stats.base import stats_types_pb2 as _stats_types_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DailyStatsKeys(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kUsedCapacityBytes: _ClassVar[DailyStatsKeys]
    kTotalCapacityBytes: _ClassVar[DailyStatsKeys]
    kDedupRatio: _ClassVar[DailyStatsKeys]
    kUsedLogicalCapacityBytes: _ClassVar[DailyStatsKeys]

class NotificationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kClusterInactiveNotificaiton: _ClassVar[NotificationType]
    kClusterWithCriticalAlertsNotification: _ClassVar[NotificationType]

class ClusterType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kCustomerPROD: _ClassVar[ClusterType]
    kCustomerTEST: _ClassVar[ClusterType]
    kPOC: _ClassVar[ClusterType]

class TaskType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kSendNotifClusterAlerts: _ClassVar[TaskType]
    kSendNotifInactiveClusters: _ClassVar[TaskType]

class ClusterStatusType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kClusterActive: _ClassVar[ClusterStatusType]
    kClusterInactive: _ClassVar[ClusterStatusType]
    KClusterNone: _ClassVar[ClusterStatusType]

class FilterType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kGreaterThan: _ClassVar[FilterType]
    kLessThan: _ClassVar[FilterType]
    kEquals: _ClassVar[FilterType]
    kNone: _ClassVar[FilterType]
kUsedCapacityBytes: DailyStatsKeys
kTotalCapacityBytes: DailyStatsKeys
kDedupRatio: DailyStatsKeys
kUsedLogicalCapacityBytes: DailyStatsKeys
kClusterInactiveNotificaiton: NotificationType
kClusterWithCriticalAlertsNotification: NotificationType
kCustomerPROD: ClusterType
kCustomerTEST: ClusterType
kPOC: ClusterType
kSendNotifClusterAlerts: TaskType
kSendNotifInactiveClusters: TaskType
kClusterActive: ClusterStatusType
kClusterInactive: ClusterStatusType
KClusterNone: ClusterStatusType
kGreaterThan: FilterType
kLessThan: FilterType
kEquals: FilterType
kNone: FilterType

class EagleConfigProto(_message.Message):
    __slots__ = ("base_uri", "api_version", "login_uri", "logout_uri", "clusters_uri", "alerts_uri", "cluster_uri", "customer_uri", "customer_clusters_uri", "customers_uri", "cluster_owner_uri", "cluster_firmware_uri", "cluster_config_uri", "cluster_tunnel_uri", "cluster_settings_uri", "cluster_prod_uri", "google_login_uri", "google_redirect_uri", "dashboard_uri", "monitor_alerts_uri", "monitor_anomalies_uri", "playground_software_version_uri", "playground_firmware_version_uri", "playground_dedup_uri", "playground_capacity_uri", "playground_cluster_settings_uri", "cluster_home_uri", "user_clusters_uri", "add_user_clusters_uri", "delete_user_clusters_uri", "cluster_vaults_uri", "reports_base_uri", "production_clusters_summary_report_uri", "nodes_summary_report_uri", "disks_summary_report_uri", "agent_base_uri", "agent_cluster_status_uri", "agent_cluster_firmware_uri", "agent_cluster_stats_uri", "agent_cluster_support_bundle_uri", "agent_audit_report_uri", "agent_cluster_alerts_batch", "agent_iris_data_batch", "agent_stats_data_batch", "agent_smart_ctl_batch", "tricorder_batch_deprecated", "firmware_batch", "agent_cluster_script_data_batch", "agent_stats_change_id_uri", "agent_cluster_healthcheck_data_batch", "agent_cluster_config_data_batch", "agent_janus_heartbeat", "agent_janus_app_metadata", "agent_janus_app_download", "agent_header_field_secret_key", "prod_google_project_id", "prod_google_client_email_address", "deprecated_prod_google_client_private_key", "prod_server_hostname", "prod_google_storage_bucket_name", "sandbox_google_project_id", "sandbox_google_client_email_address", "deprecated_sandbox_google_client_private_key", "sandbox_server_hostname", "sandbox_server_port", "pager_duty_service_key", "sandbox_google_storage_bucket_name", "localhost_hostname", "oauth_google_client_id", "oauth_google_client_secret", "oauth_google_api", "google_api_url", "company_hd", "eagle_group_email_id", "admin_email_id", "google_group_uri", "google_group_member_uri", "eagle_watcher_user_name", "eagle_watcher_password", "google_smtp_host_name", "google_smtp_port_number", "helios_communication_protocol", "helios_prod_eagle_redirect_hostname", "helios_sandbox_eagle_redirect_hostname")
    BASE_URI_FIELD_NUMBER: _ClassVar[int]
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    LOGIN_URI_FIELD_NUMBER: _ClassVar[int]
    LOGOUT_URI_FIELD_NUMBER: _ClassVar[int]
    CLUSTERS_URI_FIELD_NUMBER: _ClassVar[int]
    ALERTS_URI_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_URI_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_URI_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_CLUSTERS_URI_FIELD_NUMBER: _ClassVar[int]
    CUSTOMERS_URI_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_OWNER_URI_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_FIRMWARE_URI_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_CONFIG_URI_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_TUNNEL_URI_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_SETTINGS_URI_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_PROD_URI_FIELD_NUMBER: _ClassVar[int]
    GOOGLE_LOGIN_URI_FIELD_NUMBER: _ClassVar[int]
    GOOGLE_REDIRECT_URI_FIELD_NUMBER: _ClassVar[int]
    DASHBOARD_URI_FIELD_NUMBER: _ClassVar[int]
    MONITOR_ALERTS_URI_FIELD_NUMBER: _ClassVar[int]
    MONITOR_ANOMALIES_URI_FIELD_NUMBER: _ClassVar[int]
    PLAYGROUND_SOFTWARE_VERSION_URI_FIELD_NUMBER: _ClassVar[int]
    PLAYGROUND_FIRMWARE_VERSION_URI_FIELD_NUMBER: _ClassVar[int]
    PLAYGROUND_DEDUP_URI_FIELD_NUMBER: _ClassVar[int]
    PLAYGROUND_CAPACITY_URI_FIELD_NUMBER: _ClassVar[int]
    PLAYGROUND_CLUSTER_SETTINGS_URI_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_HOME_URI_FIELD_NUMBER: _ClassVar[int]
    USER_CLUSTERS_URI_FIELD_NUMBER: _ClassVar[int]
    ADD_USER_CLUSTERS_URI_FIELD_NUMBER: _ClassVar[int]
    DELETE_USER_CLUSTERS_URI_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_VAULTS_URI_FIELD_NUMBER: _ClassVar[int]
    REPORTS_BASE_URI_FIELD_NUMBER: _ClassVar[int]
    PRODUCTION_CLUSTERS_SUMMARY_REPORT_URI_FIELD_NUMBER: _ClassVar[int]
    NODES_SUMMARY_REPORT_URI_FIELD_NUMBER: _ClassVar[int]
    DISKS_SUMMARY_REPORT_URI_FIELD_NUMBER: _ClassVar[int]
    AGENT_BASE_URI_FIELD_NUMBER: _ClassVar[int]
    AGENT_CLUSTER_STATUS_URI_FIELD_NUMBER: _ClassVar[int]
    AGENT_CLUSTER_FIRMWARE_URI_FIELD_NUMBER: _ClassVar[int]
    AGENT_CLUSTER_STATS_URI_FIELD_NUMBER: _ClassVar[int]
    AGENT_CLUSTER_SUPPORT_BUNDLE_URI_FIELD_NUMBER: _ClassVar[int]
    AGENT_AUDIT_REPORT_URI_FIELD_NUMBER: _ClassVar[int]
    AGENT_CLUSTER_ALERTS_BATCH_FIELD_NUMBER: _ClassVar[int]
    AGENT_IRIS_DATA_BATCH_FIELD_NUMBER: _ClassVar[int]
    AGENT_STATS_DATA_BATCH_FIELD_NUMBER: _ClassVar[int]
    AGENT_SMART_CTL_BATCH_FIELD_NUMBER: _ClassVar[int]
    TRICORDER_BATCH_DEPRECATED_FIELD_NUMBER: _ClassVar[int]
    FIRMWARE_BATCH_FIELD_NUMBER: _ClassVar[int]
    AGENT_CLUSTER_SCRIPT_DATA_BATCH_FIELD_NUMBER: _ClassVar[int]
    AGENT_STATS_CHANGE_ID_URI_FIELD_NUMBER: _ClassVar[int]
    AGENT_CLUSTER_HEALTHCHECK_DATA_BATCH_FIELD_NUMBER: _ClassVar[int]
    AGENT_CLUSTER_CONFIG_DATA_BATCH_FIELD_NUMBER: _ClassVar[int]
    AGENT_JANUS_HEARTBEAT_FIELD_NUMBER: _ClassVar[int]
    AGENT_JANUS_APP_METADATA_FIELD_NUMBER: _ClassVar[int]
    AGENT_JANUS_APP_DOWNLOAD_FIELD_NUMBER: _ClassVar[int]
    AGENT_HEADER_FIELD_SECRET_KEY_FIELD_NUMBER: _ClassVar[int]
    PROD_GOOGLE_PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    PROD_GOOGLE_CLIENT_EMAIL_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    DEPRECATED_PROD_GOOGLE_CLIENT_PRIVATE_KEY_FIELD_NUMBER: _ClassVar[int]
    PROD_SERVER_HOSTNAME_FIELD_NUMBER: _ClassVar[int]
    PROD_GOOGLE_STORAGE_BUCKET_NAME_FIELD_NUMBER: _ClassVar[int]
    SANDBOX_GOOGLE_PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    SANDBOX_GOOGLE_CLIENT_EMAIL_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    DEPRECATED_SANDBOX_GOOGLE_CLIENT_PRIVATE_KEY_FIELD_NUMBER: _ClassVar[int]
    SANDBOX_SERVER_HOSTNAME_FIELD_NUMBER: _ClassVar[int]
    SANDBOX_SERVER_PORT_FIELD_NUMBER: _ClassVar[int]
    PAGER_DUTY_SERVICE_KEY_FIELD_NUMBER: _ClassVar[int]
    SANDBOX_GOOGLE_STORAGE_BUCKET_NAME_FIELD_NUMBER: _ClassVar[int]
    LOCALHOST_HOSTNAME_FIELD_NUMBER: _ClassVar[int]
    OAUTH_GOOGLE_CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    OAUTH_GOOGLE_CLIENT_SECRET_FIELD_NUMBER: _ClassVar[int]
    OAUTH_GOOGLE_API_FIELD_NUMBER: _ClassVar[int]
    GOOGLE_API_URL_FIELD_NUMBER: _ClassVar[int]
    COMPANY_HD_FIELD_NUMBER: _ClassVar[int]
    EAGLE_GROUP_EMAIL_ID_FIELD_NUMBER: _ClassVar[int]
    ADMIN_EMAIL_ID_FIELD_NUMBER: _ClassVar[int]
    GOOGLE_GROUP_URI_FIELD_NUMBER: _ClassVar[int]
    GOOGLE_GROUP_MEMBER_URI_FIELD_NUMBER: _ClassVar[int]
    EAGLE_WATCHER_USER_NAME_FIELD_NUMBER: _ClassVar[int]
    EAGLE_WATCHER_PASSWORD_FIELD_NUMBER: _ClassVar[int]
    GOOGLE_SMTP_HOST_NAME_FIELD_NUMBER: _ClassVar[int]
    GOOGLE_SMTP_PORT_NUMBER_FIELD_NUMBER: _ClassVar[int]
    HELIOS_COMMUNICATION_PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    HELIOS_PROD_EAGLE_REDIRECT_HOSTNAME_FIELD_NUMBER: _ClassVar[int]
    HELIOS_SANDBOX_EAGLE_REDIRECT_HOSTNAME_FIELD_NUMBER: _ClassVar[int]
    base_uri: str
    api_version: str
    login_uri: str
    logout_uri: str
    clusters_uri: str
    alerts_uri: str
    cluster_uri: str
    customer_uri: str
    customer_clusters_uri: str
    customers_uri: str
    cluster_owner_uri: str
    cluster_firmware_uri: str
    cluster_config_uri: str
    cluster_tunnel_uri: str
    cluster_settings_uri: str
    cluster_prod_uri: str
    google_login_uri: str
    google_redirect_uri: str
    dashboard_uri: str
    monitor_alerts_uri: str
    monitor_anomalies_uri: str
    playground_software_version_uri: str
    playground_firmware_version_uri: str
    playground_dedup_uri: str
    playground_capacity_uri: str
    playground_cluster_settings_uri: str
    cluster_home_uri: str
    user_clusters_uri: str
    add_user_clusters_uri: str
    delete_user_clusters_uri: str
    cluster_vaults_uri: str
    reports_base_uri: str
    production_clusters_summary_report_uri: str
    nodes_summary_report_uri: str
    disks_summary_report_uri: str
    agent_base_uri: str
    agent_cluster_status_uri: str
    agent_cluster_firmware_uri: str
    agent_cluster_stats_uri: str
    agent_cluster_support_bundle_uri: str
    agent_audit_report_uri: str
    agent_cluster_alerts_batch: str
    agent_iris_data_batch: str
    agent_stats_data_batch: str
    agent_smart_ctl_batch: str
    tricorder_batch_deprecated: str
    firmware_batch: str
    agent_cluster_script_data_batch: str
    agent_stats_change_id_uri: str
    agent_cluster_healthcheck_data_batch: str
    agent_cluster_config_data_batch: str
    agent_janus_heartbeat: str
    agent_janus_app_metadata: str
    agent_janus_app_download: str
    agent_header_field_secret_key: str
    prod_google_project_id: str
    prod_google_client_email_address: str
    deprecated_prod_google_client_private_key: str
    prod_server_hostname: str
    prod_google_storage_bucket_name: str
    sandbox_google_project_id: str
    sandbox_google_client_email_address: str
    deprecated_sandbox_google_client_private_key: str
    sandbox_server_hostname: str
    sandbox_server_port: int
    pager_duty_service_key: str
    sandbox_google_storage_bucket_name: str
    localhost_hostname: str
    oauth_google_client_id: str
    oauth_google_client_secret: str
    oauth_google_api: str
    google_api_url: str
    company_hd: str
    eagle_group_email_id: str
    admin_email_id: str
    google_group_uri: str
    google_group_member_uri: str
    eagle_watcher_user_name: str
    eagle_watcher_password: str
    google_smtp_host_name: str
    google_smtp_port_number: str
    helios_communication_protocol: str
    helios_prod_eagle_redirect_hostname: str
    helios_sandbox_eagle_redirect_hostname: str
    def __init__(self, base_uri: _Optional[str] = ..., api_version: _Optional[str] = ..., login_uri: _Optional[str] = ..., logout_uri: _Optional[str] = ..., clusters_uri: _Optional[str] = ..., alerts_uri: _Optional[str] = ..., cluster_uri: _Optional[str] = ..., customer_uri: _Optional[str] = ..., customer_clusters_uri: _Optional[str] = ..., customers_uri: _Optional[str] = ..., cluster_owner_uri: _Optional[str] = ..., cluster_firmware_uri: _Optional[str] = ..., cluster_config_uri: _Optional[str] = ..., cluster_tunnel_uri: _Optional[str] = ..., cluster_settings_uri: _Optional[str] = ..., cluster_prod_uri: _Optional[str] = ..., google_login_uri: _Optional[str] = ..., google_redirect_uri: _Optional[str] = ..., dashboard_uri: _Optional[str] = ..., monitor_alerts_uri: _Optional[str] = ..., monitor_anomalies_uri: _Optional[str] = ..., playground_software_version_uri: _Optional[str] = ..., playground_firmware_version_uri: _Optional[str] = ..., playground_dedup_uri: _Optional[str] = ..., playground_capacity_uri: _Optional[str] = ..., playground_cluster_settings_uri: _Optional[str] = ..., cluster_home_uri: _Optional[str] = ..., user_clusters_uri: _Optional[str] = ..., add_user_clusters_uri: _Optional[str] = ..., delete_user_clusters_uri: _Optional[str] = ..., cluster_vaults_uri: _Optional[str] = ..., reports_base_uri: _Optional[str] = ..., production_clusters_summary_report_uri: _Optional[str] = ..., nodes_summary_report_uri: _Optional[str] = ..., disks_summary_report_uri: _Optional[str] = ..., agent_base_uri: _Optional[str] = ..., agent_cluster_status_uri: _Optional[str] = ..., agent_cluster_firmware_uri: _Optional[str] = ..., agent_cluster_stats_uri: _Optional[str] = ..., agent_cluster_support_bundle_uri: _Optional[str] = ..., agent_audit_report_uri: _Optional[str] = ..., agent_cluster_alerts_batch: _Optional[str] = ..., agent_iris_data_batch: _Optional[str] = ..., agent_stats_data_batch: _Optional[str] = ..., agent_smart_ctl_batch: _Optional[str] = ..., tricorder_batch_deprecated: _Optional[str] = ..., firmware_batch: _Optional[str] = ..., agent_cluster_script_data_batch: _Optional[str] = ..., agent_stats_change_id_uri: _Optional[str] = ..., agent_cluster_healthcheck_data_batch: _Optional[str] = ..., agent_cluster_config_data_batch: _Optional[str] = ..., agent_janus_heartbeat: _Optional[str] = ..., agent_janus_app_metadata: _Optional[str] = ..., agent_janus_app_download: _Optional[str] = ..., agent_header_field_secret_key: _Optional[str] = ..., prod_google_project_id: _Optional[str] = ..., prod_google_client_email_address: _Optional[str] = ..., deprecated_prod_google_client_private_key: _Optional[str] = ..., prod_server_hostname: _Optional[str] = ..., prod_google_storage_bucket_name: _Optional[str] = ..., sandbox_google_project_id: _Optional[str] = ..., sandbox_google_client_email_address: _Optional[str] = ..., deprecated_sandbox_google_client_private_key: _Optional[str] = ..., sandbox_server_hostname: _Optional[str] = ..., sandbox_server_port: _Optional[int] = ..., pager_duty_service_key: _Optional[str] = ..., sandbox_google_storage_bucket_name: _Optional[str] = ..., localhost_hostname: _Optional[str] = ..., oauth_google_client_id: _Optional[str] = ..., oauth_google_client_secret: _Optional[str] = ..., oauth_google_api: _Optional[str] = ..., google_api_url: _Optional[str] = ..., company_hd: _Optional[str] = ..., eagle_group_email_id: _Optional[str] = ..., admin_email_id: _Optional[str] = ..., google_group_uri: _Optional[str] = ..., google_group_member_uri: _Optional[str] = ..., eagle_watcher_user_name: _Optional[str] = ..., eagle_watcher_password: _Optional[str] = ..., google_smtp_host_name: _Optional[str] = ..., google_smtp_port_number: _Optional[str] = ..., helios_communication_protocol: _Optional[str] = ..., helios_prod_eagle_redirect_hostname: _Optional[str] = ..., helios_sandbox_eagle_redirect_hostname: _Optional[str] = ...) -> None: ...

class AgentAuthKeyProto(_message.Message):
    __slots__ = ("secret_key", "cluster_id", "is_active")
    SECRET_KEY_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    IS_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    secret_key: str
    cluster_id: int
    is_active: bool
    def __init__(self, secret_key: _Optional[str] = ..., cluster_id: _Optional[int] = ..., is_active: bool = ...) -> None: ...

class UserProto(_message.Message):
    __slots__ = ("username", "password", "email_address", "first_name", "last_name", "has_role_admin", "has_role_support_engineer", "created_time_msecs", "last_updated_time_msecs", "phone_num")
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    EMAIL_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
    LAST_NAME_FIELD_NUMBER: _ClassVar[int]
    HAS_ROLE_ADMIN_FIELD_NUMBER: _ClassVar[int]
    HAS_ROLE_SUPPORT_ENGINEER_FIELD_NUMBER: _ClassVar[int]
    CREATED_TIME_MSECS_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATED_TIME_MSECS_FIELD_NUMBER: _ClassVar[int]
    PHONE_NUM_FIELD_NUMBER: _ClassVar[int]
    username: str
    password: str
    email_address: str
    first_name: str
    last_name: str
    has_role_admin: bool
    has_role_support_engineer: bool
    created_time_msecs: int
    last_updated_time_msecs: int
    phone_num: str
    def __init__(self, username: _Optional[str] = ..., password: _Optional[str] = ..., email_address: _Optional[str] = ..., first_name: _Optional[str] = ..., last_name: _Optional[str] = ..., has_role_admin: bool = ..., has_role_support_engineer: bool = ..., created_time_msecs: _Optional[int] = ..., last_updated_time_msecs: _Optional[int] = ..., phone_num: _Optional[str] = ...) -> None: ...

class ClusterProto(_message.Message):
    __slots__ = ("created_time_msecs", "last_updated_time_msecs", "cluster_id", "cluster_incarnation_id", "cluster_name", "num_of_nodes", "num_of_partitions", "num_of_viewboxes", "total_capacity_bytes", "free_capacity_bytes", "used_capacity_bytes", "used_logical_capacity_bytes", "num_of_last_run_jobs", "num_of_running_jobs", "num_of_successful_jobs", "num_of_partially_successful_jobs", "num_of_failed_jobs", "num_of_critical_alerts", "num_of_warning_alerts", "software_version", "internal_cluster", "partition_host_name", "chassis_serial", "system_capacity_bytes", "system_usage_bytes", "num_of_protected_entities", "num_of_unprotected_entities", "health", "is_healthy", "total_vault_usage_bytes", "serialized_gflags", "is_poc_cluster")
    CREATED_TIME_MSECS_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATED_TIME_MSECS_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_NAME_FIELD_NUMBER: _ClassVar[int]
    NUM_OF_NODES_FIELD_NUMBER: _ClassVar[int]
    NUM_OF_PARTITIONS_FIELD_NUMBER: _ClassVar[int]
    NUM_OF_VIEWBOXES_FIELD_NUMBER: _ClassVar[int]
    TOTAL_CAPACITY_BYTES_FIELD_NUMBER: _ClassVar[int]
    FREE_CAPACITY_BYTES_FIELD_NUMBER: _ClassVar[int]
    USED_CAPACITY_BYTES_FIELD_NUMBER: _ClassVar[int]
    USED_LOGICAL_CAPACITY_BYTES_FIELD_NUMBER: _ClassVar[int]
    NUM_OF_LAST_RUN_JOBS_FIELD_NUMBER: _ClassVar[int]
    NUM_OF_RUNNING_JOBS_FIELD_NUMBER: _ClassVar[int]
    NUM_OF_SUCCESSFUL_JOBS_FIELD_NUMBER: _ClassVar[int]
    NUM_OF_PARTIALLY_SUCCESSFUL_JOBS_FIELD_NUMBER: _ClassVar[int]
    NUM_OF_FAILED_JOBS_FIELD_NUMBER: _ClassVar[int]
    NUM_OF_CRITICAL_ALERTS_FIELD_NUMBER: _ClassVar[int]
    NUM_OF_WARNING_ALERTS_FIELD_NUMBER: _ClassVar[int]
    SOFTWARE_VERSION_FIELD_NUMBER: _ClassVar[int]
    INTERNAL_CLUSTER_FIELD_NUMBER: _ClassVar[int]
    PARTITION_HOST_NAME_FIELD_NUMBER: _ClassVar[int]
    CHASSIS_SERIAL_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_CAPACITY_BYTES_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_USAGE_BYTES_FIELD_NUMBER: _ClassVar[int]
    NUM_OF_PROTECTED_ENTITIES_FIELD_NUMBER: _ClassVar[int]
    NUM_OF_UNPROTECTED_ENTITIES_FIELD_NUMBER: _ClassVar[int]
    HEALTH_FIELD_NUMBER: _ClassVar[int]
    IS_HEALTHY_FIELD_NUMBER: _ClassVar[int]
    TOTAL_VAULT_USAGE_BYTES_FIELD_NUMBER: _ClassVar[int]
    SERIALIZED_GFLAGS_FIELD_NUMBER: _ClassVar[int]
    IS_POC_CLUSTER_FIELD_NUMBER: _ClassVar[int]
    created_time_msecs: int
    last_updated_time_msecs: int
    cluster_id: int
    cluster_incarnation_id: int
    cluster_name: str
    num_of_nodes: int
    num_of_partitions: int
    num_of_viewboxes: int
    total_capacity_bytes: int
    free_capacity_bytes: int
    used_capacity_bytes: int
    used_logical_capacity_bytes: int
    num_of_last_run_jobs: int
    num_of_running_jobs: int
    num_of_successful_jobs: int
    num_of_partially_successful_jobs: int
    num_of_failed_jobs: int
    num_of_critical_alerts: int
    num_of_warning_alerts: int
    software_version: str
    internal_cluster: bool
    partition_host_name: str
    chassis_serial: str
    system_capacity_bytes: int
    system_usage_bytes: int
    num_of_protected_entities: int
    num_of_unprotected_entities: int
    health: float
    is_healthy: bool
    total_vault_usage_bytes: int
    serialized_gflags: str
    is_poc_cluster: bool
    def __init__(self, created_time_msecs: _Optional[int] = ..., last_updated_time_msecs: _Optional[int] = ..., cluster_id: _Optional[int] = ..., cluster_incarnation_id: _Optional[int] = ..., cluster_name: _Optional[str] = ..., num_of_nodes: _Optional[int] = ..., num_of_partitions: _Optional[int] = ..., num_of_viewboxes: _Optional[int] = ..., total_capacity_bytes: _Optional[int] = ..., free_capacity_bytes: _Optional[int] = ..., used_capacity_bytes: _Optional[int] = ..., used_logical_capacity_bytes: _Optional[int] = ..., num_of_last_run_jobs: _Optional[int] = ..., num_of_running_jobs: _Optional[int] = ..., num_of_successful_jobs: _Optional[int] = ..., num_of_partially_successful_jobs: _Optional[int] = ..., num_of_failed_jobs: _Optional[int] = ..., num_of_critical_alerts: _Optional[int] = ..., num_of_warning_alerts: _Optional[int] = ..., software_version: _Optional[str] = ..., internal_cluster: bool = ..., partition_host_name: _Optional[str] = ..., chassis_serial: _Optional[str] = ..., system_capacity_bytes: _Optional[int] = ..., system_usage_bytes: _Optional[int] = ..., num_of_protected_entities: _Optional[int] = ..., num_of_unprotected_entities: _Optional[int] = ..., health: _Optional[float] = ..., is_healthy: bool = ..., total_vault_usage_bytes: _Optional[int] = ..., serialized_gflags: _Optional[str] = ..., is_poc_cluster: bool = ...) -> None: ...

class AlertPropertiesProto(_message.Message):
    __slots__ = ("property_vec",)
    PROPERTY_VEC_FIELD_NUMBER: _ClassVar[int]
    property_vec: _containers.RepeatedCompositeFieldContainer[_alert_pb2.AlertProto.Property]
    def __init__(self, property_vec: _Optional[_Iterable[_Union[_alert_pb2.AlertProto.Property, _Mapping]]] = ...) -> None: ...

class AlertProto(_message.Message):
    __slots__ = ("timestamp_usecs", "type", "cluster_id", "incarnation_id", "description", "is_critical", "tie_break_id", "serialized_properties", "severity", "category", "resolution_id", "suppression_id", "deserialized_alert_properties")
    TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    IS_CRITICAL_FIELD_NUMBER: _ClassVar[int]
    TIE_BREAK_ID_FIELD_NUMBER: _ClassVar[int]
    SERIALIZED_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    SEVERITY_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    RESOLUTION_ID_FIELD_NUMBER: _ClassVar[int]
    SUPPRESSION_ID_FIELD_NUMBER: _ClassVar[int]
    DESERIALIZED_ALERT_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    timestamp_usecs: int
    type: int
    cluster_id: int
    incarnation_id: int
    description: str
    is_critical: bool
    tie_break_id: int
    serialized_properties: str
    severity: str
    category: str
    resolution_id: int
    suppression_id: int
    deserialized_alert_properties: AlertPropertiesProto
    def __init__(self, timestamp_usecs: _Optional[int] = ..., type: _Optional[int] = ..., cluster_id: _Optional[int] = ..., incarnation_id: _Optional[int] = ..., description: _Optional[str] = ..., is_critical: bool = ..., tie_break_id: _Optional[int] = ..., serialized_properties: _Optional[str] = ..., severity: _Optional[str] = ..., category: _Optional[str] = ..., resolution_id: _Optional[int] = ..., suppression_id: _Optional[int] = ..., deserialized_alert_properties: _Optional[_Union[AlertPropertiesProto, _Mapping]] = ...) -> None: ...

class AlertSummaryProto(_message.Message):
    __slots__ = ("hardware_alerts", "software_alerts", "backup_alerts", "health")
    HARDWARE_ALERTS_FIELD_NUMBER: _ClassVar[int]
    SOFTWARE_ALERTS_FIELD_NUMBER: _ClassVar[int]
    BACKUP_ALERTS_FIELD_NUMBER: _ClassVar[int]
    HEALTH_FIELD_NUMBER: _ClassVar[int]
    hardware_alerts: AlertCategorySummary
    software_alerts: AlertCategorySummary
    backup_alerts: AlertCategorySummary
    health: int
    def __init__(self, hardware_alerts: _Optional[_Union[AlertCategorySummary, _Mapping]] = ..., software_alerts: _Optional[_Union[AlertCategorySummary, _Mapping]] = ..., backup_alerts: _Optional[_Union[AlertCategorySummary, _Mapping]] = ..., health: _Optional[int] = ...) -> None: ...

class DailyStatProto(_message.Message):
    __slots__ = ("last_updated_time_msecs", "cluster_id", "stat_key", "stat_value")
    LAST_UPDATED_TIME_MSECS_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    STAT_KEY_FIELD_NUMBER: _ClassVar[int]
    STAT_VALUE_FIELD_NUMBER: _ClassVar[int]
    last_updated_time_msecs: int
    cluster_id: int
    stat_key: str
    stat_value: str
    def __init__(self, last_updated_time_msecs: _Optional[int] = ..., cluster_id: _Optional[int] = ..., stat_key: _Optional[str] = ..., stat_value: _Optional[str] = ...) -> None: ...

class AlertCategorySummary(_message.Message):
    __slots__ = ("num_critical_alerts", "num_warning_alerts", "num_info_messages")
    NUM_CRITICAL_ALERTS_FIELD_NUMBER: _ClassVar[int]
    NUM_WARNING_ALERTS_FIELD_NUMBER: _ClassVar[int]
    NUM_INFO_MESSAGES_FIELD_NUMBER: _ClassVar[int]
    num_critical_alerts: int
    num_warning_alerts: int
    num_info_messages: int
    def __init__(self, num_critical_alerts: _Optional[int] = ..., num_warning_alerts: _Optional[int] = ..., num_info_messages: _Optional[int] = ...) -> None: ...

class UserNotifProto(_message.Message):
    __slots__ = ("username", "cluster_id", "alert_id", "email_sent", "email_sent_time_msecs", "sms_sent", "sms_sent_time_msecs", "pager_duty_notif_sent", "pager_duty_notif_sent_time_msecs")
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    ALERT_ID_FIELD_NUMBER: _ClassVar[int]
    EMAIL_SENT_FIELD_NUMBER: _ClassVar[int]
    EMAIL_SENT_TIME_MSECS_FIELD_NUMBER: _ClassVar[int]
    SMS_SENT_FIELD_NUMBER: _ClassVar[int]
    SMS_SENT_TIME_MSECS_FIELD_NUMBER: _ClassVar[int]
    PAGER_DUTY_NOTIF_SENT_FIELD_NUMBER: _ClassVar[int]
    PAGER_DUTY_NOTIF_SENT_TIME_MSECS_FIELD_NUMBER: _ClassVar[int]
    username: str
    cluster_id: int
    alert_id: str
    email_sent: bool
    email_sent_time_msecs: int
    sms_sent: bool
    sms_sent_time_msecs: int
    pager_duty_notif_sent: bool
    pager_duty_notif_sent_time_msecs: int
    def __init__(self, username: _Optional[str] = ..., cluster_id: _Optional[int] = ..., alert_id: _Optional[str] = ..., email_sent: bool = ..., email_sent_time_msecs: _Optional[int] = ..., sms_sent: bool = ..., sms_sent_time_msecs: _Optional[int] = ..., pager_duty_notif_sent: bool = ..., pager_duty_notif_sent_time_msecs: _Optional[int] = ...) -> None: ...

class UserNotifSettingsProto(_message.Message):
    __slots__ = ("username", "rx_notif_disk_offline", "rx_notif_node_down", "rx_notif_job_failed", "rx_notif_inactive_alert")
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    RX_NOTIF_DISK_OFFLINE_FIELD_NUMBER: _ClassVar[int]
    RX_NOTIF_NODE_DOWN_FIELD_NUMBER: _ClassVar[int]
    RX_NOTIF_JOB_FAILED_FIELD_NUMBER: _ClassVar[int]
    RX_NOTIF_INACTIVE_ALERT_FIELD_NUMBER: _ClassVar[int]
    username: str
    rx_notif_disk_offline: bool
    rx_notif_node_down: bool
    rx_notif_job_failed: bool
    rx_notif_inactive_alert: bool
    def __init__(self, username: _Optional[str] = ..., rx_notif_disk_offline: bool = ..., rx_notif_node_down: bool = ..., rx_notif_job_failed: bool = ..., rx_notif_inactive_alert: bool = ...) -> None: ...

class ClusterSettingsProto(_message.Message):
    __slots__ = ("cluster_id", "alert_if_inactive", "alert_on_critical_cluster_alerts", "make_the_cluster_production_cluster_type")
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    ALERT_IF_INACTIVE_FIELD_NUMBER: _ClassVar[int]
    ALERT_ON_CRITICAL_CLUSTER_ALERTS_FIELD_NUMBER: _ClassVar[int]
    MAKE_THE_CLUSTER_PRODUCTION_CLUSTER_TYPE_FIELD_NUMBER: _ClassVar[int]
    cluster_id: int
    alert_if_inactive: bool
    alert_on_critical_cluster_alerts: bool
    make_the_cluster_production_cluster_type: bool
    def __init__(self, cluster_id: _Optional[int] = ..., alert_if_inactive: bool = ..., alert_on_critical_cluster_alerts: bool = ..., make_the_cluster_production_cluster_type: bool = ...) -> None: ...

class StatsEntityAttrsProto(_message.Message):
    __slots__ = ("attribute_vec",)
    ATTRIBUTE_VEC_FIELD_NUMBER: _ClassVar[int]
    attribute_vec: _containers.RepeatedCompositeFieldContainer[_stats_types_pb2.KeyValuePair]
    def __init__(self, attribute_vec: _Optional[_Iterable[_Union[_stats_types_pb2.KeyValuePair, _Mapping]]] = ...) -> None: ...

class StatsEntityMetadataProto(_message.Message):
    __slots__ = ("cluster_id", "incarnation_id", "schema_name", "entity_id", "entity_name", "serialized_entity_attrs")
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_NAME_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    ENTITY_NAME_FIELD_NUMBER: _ClassVar[int]
    SERIALIZED_ENTITY_ATTRS_FIELD_NUMBER: _ClassVar[int]
    cluster_id: int
    incarnation_id: int
    schema_name: str
    entity_id: str
    entity_name: str
    serialized_entity_attrs: str
    def __init__(self, cluster_id: _Optional[int] = ..., incarnation_id: _Optional[int] = ..., schema_name: _Optional[str] = ..., entity_id: _Optional[str] = ..., entity_name: _Optional[str] = ..., serialized_entity_attrs: _Optional[str] = ...) -> None: ...

class StatsEntitiesMetadata(_message.Message):
    __slots__ = ("metadata_vec",)
    METADATA_VEC_FIELD_NUMBER: _ClassVar[int]
    metadata_vec: _containers.RepeatedCompositeFieldContainer[StatsEntityMetadataProto]
    def __init__(self, metadata_vec: _Optional[_Iterable[_Union[StatsEntityMetadataProto, _Mapping]]] = ...) -> None: ...

class StatsEntityMetricDataPoint(_message.Message):
    __slots__ = ("cluster_id", "incarnation_id", "schema_name", "entity_id", "metric_name", "created_time_msecs", "expiry_time_msecs", "metric_value_type", "metric_int64_value", "metric_str_value", "metric_double_value")
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_NAME_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    METRIC_NAME_FIELD_NUMBER: _ClassVar[int]
    CREATED_TIME_MSECS_FIELD_NUMBER: _ClassVar[int]
    EXPIRY_TIME_MSECS_FIELD_NUMBER: _ClassVar[int]
    METRIC_VALUE_TYPE_FIELD_NUMBER: _ClassVar[int]
    METRIC_INT64_VALUE_FIELD_NUMBER: _ClassVar[int]
    METRIC_STR_VALUE_FIELD_NUMBER: _ClassVar[int]
    METRIC_DOUBLE_VALUE_FIELD_NUMBER: _ClassVar[int]
    cluster_id: int
    incarnation_id: int
    schema_name: str
    entity_id: str
    metric_name: str
    created_time_msecs: int
    expiry_time_msecs: int
    metric_value_type: str
    metric_int64_value: int
    metric_str_value: str
    metric_double_value: float
    def __init__(self, cluster_id: _Optional[int] = ..., incarnation_id: _Optional[int] = ..., schema_name: _Optional[str] = ..., entity_id: _Optional[str] = ..., metric_name: _Optional[str] = ..., created_time_msecs: _Optional[int] = ..., expiry_time_msecs: _Optional[int] = ..., metric_value_type: _Optional[str] = ..., metric_int64_value: _Optional[int] = ..., metric_str_value: _Optional[str] = ..., metric_double_value: _Optional[float] = ...) -> None: ...

class AlertCategoryWeights(_message.Message):
    __slots__ = ("weight_node_health", "weight_cluster_health", "weight_disk", "weight_node", "weight_cluster", "weight_archival", "weight_encryption", "weight_backup_restore")
    WEIGHT_NODE_HEALTH_FIELD_NUMBER: _ClassVar[int]
    WEIGHT_CLUSTER_HEALTH_FIELD_NUMBER: _ClassVar[int]
    WEIGHT_DISK_FIELD_NUMBER: _ClassVar[int]
    WEIGHT_NODE_FIELD_NUMBER: _ClassVar[int]
    WEIGHT_CLUSTER_FIELD_NUMBER: _ClassVar[int]
    WEIGHT_ARCHIVAL_FIELD_NUMBER: _ClassVar[int]
    WEIGHT_ENCRYPTION_FIELD_NUMBER: _ClassVar[int]
    WEIGHT_BACKUP_RESTORE_FIELD_NUMBER: _ClassVar[int]
    weight_node_health: float
    weight_cluster_health: float
    weight_disk: float
    weight_node: float
    weight_cluster: float
    weight_archival: float
    weight_encryption: float
    weight_backup_restore: float
    def __init__(self, weight_node_health: _Optional[float] = ..., weight_cluster_health: _Optional[float] = ..., weight_disk: _Optional[float] = ..., weight_node: _Optional[float] = ..., weight_cluster: _Optional[float] = ..., weight_archival: _Optional[float] = ..., weight_encryption: _Optional[float] = ..., weight_backup_restore: _Optional[float] = ...) -> None: ...

class AlertTimeDurationWeights(_message.Message):
    __slots__ = ("weight_same_day", "weight_same_week", "weight_same_month", "weight_expired")
    WEIGHT_SAME_DAY_FIELD_NUMBER: _ClassVar[int]
    WEIGHT_SAME_WEEK_FIELD_NUMBER: _ClassVar[int]
    WEIGHT_SAME_MONTH_FIELD_NUMBER: _ClassVar[int]
    WEIGHT_EXPIRED_FIELD_NUMBER: _ClassVar[int]
    weight_same_day: float
    weight_same_week: float
    weight_same_month: float
    weight_expired: float
    def __init__(self, weight_same_day: _Optional[float] = ..., weight_same_week: _Optional[float] = ..., weight_same_month: _Optional[float] = ..., weight_expired: _Optional[float] = ...) -> None: ...

class CustomerProto(_message.Message):
    __slots__ = ("customer_id", "name", "details", "primary_contact_name", "primary_contact_email", "primary_contact_phone_num", "secondary_contact_name", "secondary_contact_email", "secondary_contact_phone_num")
    CUSTOMER_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_CONTACT_NAME_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_CONTACT_EMAIL_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_CONTACT_PHONE_NUM_FIELD_NUMBER: _ClassVar[int]
    SECONDARY_CONTACT_NAME_FIELD_NUMBER: _ClassVar[int]
    SECONDARY_CONTACT_EMAIL_FIELD_NUMBER: _ClassVar[int]
    SECONDARY_CONTACT_PHONE_NUM_FIELD_NUMBER: _ClassVar[int]
    customer_id: int
    name: str
    details: str
    primary_contact_name: str
    primary_contact_email: str
    primary_contact_phone_num: str
    secondary_contact_name: str
    secondary_contact_email: str
    secondary_contact_phone_num: str
    def __init__(self, customer_id: _Optional[int] = ..., name: _Optional[str] = ..., details: _Optional[str] = ..., primary_contact_name: _Optional[str] = ..., primary_contact_email: _Optional[str] = ..., primary_contact_phone_num: _Optional[str] = ..., secondary_contact_name: _Optional[str] = ..., secondary_contact_email: _Optional[str] = ..., secondary_contact_phone_num: _Optional[str] = ...) -> None: ...

class ClusterOwnerProto(_message.Message):
    __slots__ = ("cluster_id", "customer_id", "cluster_type", "cluster_name", "primary_contact_name", "primary_contact_email", "primary_contact_phone_num", "secondary_contact_name", "secondary_contact_email", "secondary_contact_phone_num")
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_TYPE_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_NAME_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_CONTACT_NAME_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_CONTACT_EMAIL_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_CONTACT_PHONE_NUM_FIELD_NUMBER: _ClassVar[int]
    SECONDARY_CONTACT_NAME_FIELD_NUMBER: _ClassVar[int]
    SECONDARY_CONTACT_EMAIL_FIELD_NUMBER: _ClassVar[int]
    SECONDARY_CONTACT_PHONE_NUM_FIELD_NUMBER: _ClassVar[int]
    cluster_id: int
    customer_id: int
    cluster_type: str
    cluster_name: str
    primary_contact_name: str
    primary_contact_email: str
    primary_contact_phone_num: str
    secondary_contact_name: str
    secondary_contact_email: str
    secondary_contact_phone_num: str
    def __init__(self, cluster_id: _Optional[int] = ..., customer_id: _Optional[int] = ..., cluster_type: _Optional[str] = ..., cluster_name: _Optional[str] = ..., primary_contact_name: _Optional[str] = ..., primary_contact_email: _Optional[str] = ..., primary_contact_phone_num: _Optional[str] = ..., secondary_contact_name: _Optional[str] = ..., secondary_contact_email: _Optional[str] = ..., secondary_contact_phone_num: _Optional[str] = ...) -> None: ...

class CategoryAlertCountResult(_message.Message):
    __slots__ = ("num_node_alerts", "num_cluster_alerts", "num_disk_alerts", "num_encryption_alerts", "num_backupRestore_alerts", "num_nodeHealth_alerts", "num_clusterHealth_alerts", "num_archival_alerts")
    NUM_NODE_ALERTS_FIELD_NUMBER: _ClassVar[int]
    NUM_CLUSTER_ALERTS_FIELD_NUMBER: _ClassVar[int]
    NUM_DISK_ALERTS_FIELD_NUMBER: _ClassVar[int]
    NUM_ENCRYPTION_ALERTS_FIELD_NUMBER: _ClassVar[int]
    NUM_BACKUPRESTORE_ALERTS_FIELD_NUMBER: _ClassVar[int]
    NUM_NODEHEALTH_ALERTS_FIELD_NUMBER: _ClassVar[int]
    NUM_CLUSTERHEALTH_ALERTS_FIELD_NUMBER: _ClassVar[int]
    NUM_ARCHIVAL_ALERTS_FIELD_NUMBER: _ClassVar[int]
    num_node_alerts: int
    num_cluster_alerts: int
    num_disk_alerts: int
    num_encryption_alerts: int
    num_backupRestore_alerts: int
    num_nodeHealth_alerts: int
    num_clusterHealth_alerts: int
    num_archival_alerts: int
    def __init__(self, num_node_alerts: _Optional[int] = ..., num_cluster_alerts: _Optional[int] = ..., num_disk_alerts: _Optional[int] = ..., num_encryption_alerts: _Optional[int] = ..., num_backupRestore_alerts: _Optional[int] = ..., num_nodeHealth_alerts: _Optional[int] = ..., num_clusterHealth_alerts: _Optional[int] = ..., num_archival_alerts: _Optional[int] = ...) -> None: ...

class FirmwareProto(_message.Message):
    __slots__ = ("cluster_id", "node_id", "node_ip", "hardware_type", "hardware_id", "hardware_desc", "hardware_model", "firmware_version")
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    NODE_IP_FIELD_NUMBER: _ClassVar[int]
    HARDWARE_TYPE_FIELD_NUMBER: _ClassVar[int]
    HARDWARE_ID_FIELD_NUMBER: _ClassVar[int]
    HARDWARE_DESC_FIELD_NUMBER: _ClassVar[int]
    HARDWARE_MODEL_FIELD_NUMBER: _ClassVar[int]
    FIRMWARE_VERSION_FIELD_NUMBER: _ClassVar[int]
    cluster_id: int
    node_id: int
    node_ip: str
    hardware_type: str
    hardware_id: str
    hardware_desc: str
    hardware_model: str
    firmware_version: str
    def __init__(self, cluster_id: _Optional[int] = ..., node_id: _Optional[int] = ..., node_ip: _Optional[str] = ..., hardware_type: _Optional[str] = ..., hardware_id: _Optional[str] = ..., hardware_desc: _Optional[str] = ..., hardware_model: _Optional[str] = ..., firmware_version: _Optional[str] = ...) -> None: ...

class ClusterConfigMetadataProto(_message.Message):
    __slots__ = ("cluster_id", "config_file_name", "hash", "last_updated_time_usecs")
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    HASH_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATED_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    cluster_id: int
    config_file_name: str
    hash: str
    last_updated_time_usecs: int
    def __init__(self, cluster_id: _Optional[int] = ..., config_file_name: _Optional[str] = ..., hash: _Optional[str] = ..., last_updated_time_usecs: _Optional[int] = ...) -> None: ...

class ClusterConfigHistoryProto(_message.Message):
    __slots__ = ("cluster_id", "config_file_name", "created_time_usecs")
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    CREATED_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    cluster_id: int
    config_file_name: str
    created_time_usecs: int
    def __init__(self, cluster_id: _Optional[int] = ..., config_file_name: _Optional[str] = ..., created_time_usecs: _Optional[int] = ...) -> None: ...

class TaskPayloadProto(_message.Message):
    __slots__ = ("type", "cluster_alerts", "inactive_clusters")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ALERTS_FIELD_NUMBER: _ClassVar[int]
    INACTIVE_CLUSTERS_FIELD_NUMBER: _ClassVar[int]
    type: TaskType
    cluster_alerts: TaskPayloadClusterAlerts
    inactive_clusters: TaskPayloadInactiveClusters
    def __init__(self, type: _Optional[_Union[TaskType, str]] = ..., cluster_alerts: _Optional[_Union[TaskPayloadClusterAlerts, _Mapping]] = ..., inactive_clusters: _Optional[_Union[TaskPayloadInactiveClusters, _Mapping]] = ...) -> None: ...

class TaskPayloadClusterAlerts(_message.Message):
    __slots__ = ("cluster", "alert_vec")
    CLUSTER_FIELD_NUMBER: _ClassVar[int]
    ALERT_VEC_FIELD_NUMBER: _ClassVar[int]
    cluster: ClusterProto
    alert_vec: _containers.RepeatedCompositeFieldContainer[AlertProto]
    def __init__(self, cluster: _Optional[_Union[ClusterProto, _Mapping]] = ..., alert_vec: _Optional[_Iterable[_Union[AlertProto, _Mapping]]] = ...) -> None: ...

class TaskPayloadInactiveClusters(_message.Message):
    __slots__ = ("cluster_vec",)
    CLUSTER_VEC_FIELD_NUMBER: _ClassVar[int]
    cluster_vec: _containers.RepeatedCompositeFieldContainer[ClusterProto]
    def __init__(self, cluster_vec: _Optional[_Iterable[_Union[ClusterProto, _Mapping]]] = ...) -> None: ...

class CreateCustomerArg(_message.Message):
    __slots__ = ("customer",)
    CUSTOMER_FIELD_NUMBER: _ClassVar[int]
    customer: CustomerProto
    def __init__(self, customer: _Optional[_Union[CustomerProto, _Mapping]] = ...) -> None: ...

class DashboardResult(_message.Message):
    __slots__ = ("num_healthy_clusters", "num_unhealthy_clusters", "num_protected_vms", "logical_capacity_used", "physical_capacity_used", "num_critical_alerts", "num_warning_alerts", "num_active_clusters", "num_inactive_clusters", "avg_de_dup_ratio", "daily_critical_alerts_count_list", "daily_warning_alerts_count_list", "past_days_list", "unhealthy_clusters_vec")
    NUM_HEALTHY_CLUSTERS_FIELD_NUMBER: _ClassVar[int]
    NUM_UNHEALTHY_CLUSTERS_FIELD_NUMBER: _ClassVar[int]
    NUM_PROTECTED_VMS_FIELD_NUMBER: _ClassVar[int]
    LOGICAL_CAPACITY_USED_FIELD_NUMBER: _ClassVar[int]
    PHYSICAL_CAPACITY_USED_FIELD_NUMBER: _ClassVar[int]
    NUM_CRITICAL_ALERTS_FIELD_NUMBER: _ClassVar[int]
    NUM_WARNING_ALERTS_FIELD_NUMBER: _ClassVar[int]
    NUM_ACTIVE_CLUSTERS_FIELD_NUMBER: _ClassVar[int]
    NUM_INACTIVE_CLUSTERS_FIELD_NUMBER: _ClassVar[int]
    AVG_DE_DUP_RATIO_FIELD_NUMBER: _ClassVar[int]
    DAILY_CRITICAL_ALERTS_COUNT_LIST_FIELD_NUMBER: _ClassVar[int]
    DAILY_WARNING_ALERTS_COUNT_LIST_FIELD_NUMBER: _ClassVar[int]
    PAST_DAYS_LIST_FIELD_NUMBER: _ClassVar[int]
    UNHEALTHY_CLUSTERS_VEC_FIELD_NUMBER: _ClassVar[int]
    num_healthy_clusters: int
    num_unhealthy_clusters: int
    num_protected_vms: int
    logical_capacity_used: int
    physical_capacity_used: int
    num_critical_alerts: int
    num_warning_alerts: int
    num_active_clusters: int
    num_inactive_clusters: int
    avg_de_dup_ratio: float
    daily_critical_alerts_count_list: _containers.RepeatedScalarFieldContainer[int]
    daily_warning_alerts_count_list: _containers.RepeatedScalarFieldContainer[int]
    past_days_list: _containers.RepeatedScalarFieldContainer[str]
    unhealthy_clusters_vec: _containers.RepeatedCompositeFieldContainer[ClusterProto]
    def __init__(self, num_healthy_clusters: _Optional[int] = ..., num_unhealthy_clusters: _Optional[int] = ..., num_protected_vms: _Optional[int] = ..., logical_capacity_used: _Optional[int] = ..., physical_capacity_used: _Optional[int] = ..., num_critical_alerts: _Optional[int] = ..., num_warning_alerts: _Optional[int] = ..., num_active_clusters: _Optional[int] = ..., num_inactive_clusters: _Optional[int] = ..., avg_de_dup_ratio: _Optional[float] = ..., daily_critical_alerts_count_list: _Optional[_Iterable[int]] = ..., daily_warning_alerts_count_list: _Optional[_Iterable[int]] = ..., past_days_list: _Optional[_Iterable[str]] = ..., unhealthy_clusters_vec: _Optional[_Iterable[_Union[ClusterProto, _Mapping]]] = ...) -> None: ...

class ApplicationCache(_message.Message):
    __slots__ = ("dashboard_result", "monitor_alerts_result", "active_clusters_vec", "anomalies_result")
    DASHBOARD_RESULT_FIELD_NUMBER: _ClassVar[int]
    MONITOR_ALERTS_RESULT_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_CLUSTERS_VEC_FIELD_NUMBER: _ClassVar[int]
    ANOMALIES_RESULT_FIELD_NUMBER: _ClassVar[int]
    dashboard_result: DashboardResult
    monitor_alerts_result: MonitoringAlertsResult
    active_clusters_vec: _containers.RepeatedCompositeFieldContainer[ClusterProto]
    anomalies_result: AnomalyResult
    def __init__(self, dashboard_result: _Optional[_Union[DashboardResult, _Mapping]] = ..., monitor_alerts_result: _Optional[_Union[MonitoringAlertsResult, _Mapping]] = ..., active_clusters_vec: _Optional[_Iterable[_Union[ClusterProto, _Mapping]]] = ..., anomalies_result: _Optional[_Union[AnomalyResult, _Mapping]] = ...) -> None: ...

class CreateCustomerResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetCustomerResult(_message.Message):
    __slots__ = ("customer",)
    CUSTOMER_FIELD_NUMBER: _ClassVar[int]
    customer: CustomerProto
    def __init__(self, customer: _Optional[_Union[CustomerProto, _Mapping]] = ...) -> None: ...

class RemoveCustomerResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetCustomersResult(_message.Message):
    __slots__ = ("customer_vec",)
    CUSTOMER_VEC_FIELD_NUMBER: _ClassVar[int]
    customer_vec: _containers.RepeatedCompositeFieldContainer[CustomerProto]
    def __init__(self, customer_vec: _Optional[_Iterable[_Union[CustomerProto, _Mapping]]] = ...) -> None: ...

class GetCustomerClustersResult(_message.Message):
    __slots__ = ("cluster_vec",)
    CLUSTER_VEC_FIELD_NUMBER: _ClassVar[int]
    cluster_vec: _containers.RepeatedCompositeFieldContainer[ClusterOwnerProto]
    def __init__(self, cluster_vec: _Optional[_Iterable[_Union[ClusterOwnerProto, _Mapping]]] = ...) -> None: ...

class AddClusterOwnerArg(_message.Message):
    __slots__ = ("owner",)
    OWNER_FIELD_NUMBER: _ClassVar[int]
    owner: ClusterOwnerProto
    def __init__(self, owner: _Optional[_Union[ClusterOwnerProto, _Mapping]] = ...) -> None: ...

class AddClusterOwnerResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetClusterOwnerResult(_message.Message):
    __slots__ = ("owner",)
    OWNER_FIELD_NUMBER: _ClassVar[int]
    owner: ClusterOwnerProto
    def __init__(self, owner: _Optional[_Union[ClusterOwnerProto, _Mapping]] = ...) -> None: ...

class RemoveClusterOwnerResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ClusterInfoProto(_message.Message):
    __slots__ = ("cluster", "customer", "owner", "num_critical_alerts", "num_warning_alerts", "num_anomalies", "alerts_vec", "used_logical_capacity_graph_stats", "used_physcial_capacity_graph_stats", "dedup_graph_stats", "healthy", "last_seven_days", "services_gflags_proto")
    CLUSTER_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    NUM_CRITICAL_ALERTS_FIELD_NUMBER: _ClassVar[int]
    NUM_WARNING_ALERTS_FIELD_NUMBER: _ClassVar[int]
    NUM_ANOMALIES_FIELD_NUMBER: _ClassVar[int]
    ALERTS_VEC_FIELD_NUMBER: _ClassVar[int]
    USED_LOGICAL_CAPACITY_GRAPH_STATS_FIELD_NUMBER: _ClassVar[int]
    USED_PHYSCIAL_CAPACITY_GRAPH_STATS_FIELD_NUMBER: _ClassVar[int]
    DEDUP_GRAPH_STATS_FIELD_NUMBER: _ClassVar[int]
    HEALTHY_FIELD_NUMBER: _ClassVar[int]
    LAST_SEVEN_DAYS_FIELD_NUMBER: _ClassVar[int]
    SERVICES_GFLAGS_PROTO_FIELD_NUMBER: _ClassVar[int]
    cluster: ClusterProto
    customer: CustomerProto
    owner: ClusterOwnerProto
    num_critical_alerts: int
    num_warning_alerts: int
    num_anomalies: int
    alerts_vec: _containers.RepeatedScalarFieldContainer[int]
    used_logical_capacity_graph_stats: _containers.RepeatedScalarFieldContainer[int]
    used_physcial_capacity_graph_stats: _containers.RepeatedScalarFieldContainer[int]
    dedup_graph_stats: _containers.RepeatedScalarFieldContainer[float]
    healthy: bool
    last_seven_days: _containers.RepeatedScalarFieldContainer[str]
    services_gflags_proto: _containers.RepeatedCompositeFieldContainer[GflagProto]
    def __init__(self, cluster: _Optional[_Union[ClusterProto, _Mapping]] = ..., customer: _Optional[_Union[CustomerProto, _Mapping]] = ..., owner: _Optional[_Union[ClusterOwnerProto, _Mapping]] = ..., num_critical_alerts: _Optional[int] = ..., num_warning_alerts: _Optional[int] = ..., num_anomalies: _Optional[int] = ..., alerts_vec: _Optional[_Iterable[int]] = ..., used_logical_capacity_graph_stats: _Optional[_Iterable[int]] = ..., used_physcial_capacity_graph_stats: _Optional[_Iterable[int]] = ..., dedup_graph_stats: _Optional[_Iterable[float]] = ..., healthy: bool = ..., last_seven_days: _Optional[_Iterable[str]] = ..., services_gflags_proto: _Optional[_Iterable[_Union[GflagProto, _Mapping]]] = ...) -> None: ...

class GflagProto(_message.Message):
    __slots__ = ("gflag_service_name", "gflag_name", "gflag_value")
    GFLAG_SERVICE_NAME_FIELD_NUMBER: _ClassVar[int]
    GFLAG_NAME_FIELD_NUMBER: _ClassVar[int]
    GFLAG_VALUE_FIELD_NUMBER: _ClassVar[int]
    gflag_service_name: str
    gflag_name: str
    gflag_value: str
    def __init__(self, gflag_service_name: _Optional[str] = ..., gflag_name: _Optional[str] = ..., gflag_value: _Optional[str] = ...) -> None: ...

class GetClustersResult(_message.Message):
    __slots__ = ("cluster_info_vec",)
    CLUSTER_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    cluster_info_vec: _containers.RepeatedCompositeFieldContainer[ClusterInfoProto]
    def __init__(self, cluster_info_vec: _Optional[_Iterable[_Union[ClusterInfoProto, _Mapping]]] = ...) -> None: ...

class GetClusterResult(_message.Message):
    __slots__ = ("cluster_info",)
    CLUSTER_INFO_FIELD_NUMBER: _ClassVar[int]
    cluster_info: ClusterInfoProto
    def __init__(self, cluster_info: _Optional[_Union[ClusterInfoProto, _Mapping]] = ...) -> None: ...

class GetClusterDashboardResult(_message.Message):
    __slots__ = ("cluster_info",)
    CLUSTER_INFO_FIELD_NUMBER: _ClassVar[int]
    cluster_info: ClusterInfoProto
    def __init__(self, cluster_info: _Optional[_Union[ClusterInfoProto, _Mapping]] = ...) -> None: ...

class GetClusterConfigResult(_message.Message):
    __slots__ = ("config",)
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    config: _cluster_config_pb2.ClusterConfigProto
    def __init__(self, config: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto, _Mapping]] = ...) -> None: ...

class GetAlertsResult(_message.Message):
    __slots__ = ("alert_vec", "alerts_stats")
    ALERT_VEC_FIELD_NUMBER: _ClassVar[int]
    ALERTS_STATS_FIELD_NUMBER: _ClassVar[int]
    alert_vec: _containers.RepeatedCompositeFieldContainer[AlertProto]
    alerts_stats: AlertSummaryProto
    def __init__(self, alert_vec: _Optional[_Iterable[_Union[AlertProto, _Mapping]]] = ..., alerts_stats: _Optional[_Union[AlertSummaryProto, _Mapping]] = ...) -> None: ...

class GetFirmwareResult(_message.Message):
    __slots__ = ("firmware_vec",)
    FIRMWARE_VEC_FIELD_NUMBER: _ClassVar[int]
    firmware_vec: _containers.RepeatedCompositeFieldContainer[FirmwareProto]
    def __init__(self, firmware_vec: _Optional[_Iterable[_Union[FirmwareProto, _Mapping]]] = ...) -> None: ...

class UpdateClusterSettingsArg(_message.Message):
    __slots__ = ("settings",)
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    settings: ClusterSettingsProto
    def __init__(self, settings: _Optional[_Union[ClusterSettingsProto, _Mapping]] = ...) -> None: ...

class UpdateClusterSettingsResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetClusterSettingsResult(_message.Message):
    __slots__ = ("settings",)
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    settings: ClusterSettingsProto
    def __init__(self, settings: _Optional[_Union[ClusterSettingsProto, _Mapping]] = ...) -> None: ...

class GetVaultsArg(_message.Message):
    __slots__ = ("cluster_id",)
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    cluster_id: int
    def __init__(self, cluster_id: _Optional[int] = ...) -> None: ...

class VaultProto(_message.Message):
    __slots__ = ("id", "name", "type", "morphed_usage_bytes")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    MORPHED_USAGE_BYTES_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    type: str
    morphed_usage_bytes: StatsEntityMetricDataPoint
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., type: _Optional[str] = ..., morphed_usage_bytes: _Optional[_Union[StatsEntityMetricDataPoint, _Mapping]] = ...) -> None: ...

class GetVaultsResult(_message.Message):
    __slots__ = ("vault_vec",)
    VAULT_VEC_FIELD_NUMBER: _ClassVar[int]
    vault_vec: _containers.RepeatedCompositeFieldContainer[VaultProto]
    def __init__(self, vault_vec: _Optional[_Iterable[_Union[VaultProto, _Mapping]]] = ...) -> None: ...

class LogoutResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class MonitoringAlertsRequest(_message.Message):
    __slots__ = ("category", "severity", "filters")
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    SEVERITY_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    category: str
    severity: str
    filters: str
    def __init__(self, category: _Optional[str] = ..., severity: _Optional[str] = ..., filters: _Optional[str] = ...) -> None: ...

class QueriedAlertProto(_message.Message):
    __slots__ = ("cluster_id", "cluster_name", "alert_description", "alert_category", "alert_serverity", "alert_count")
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_NAME_FIELD_NUMBER: _ClassVar[int]
    ALERT_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ALERT_CATEGORY_FIELD_NUMBER: _ClassVar[int]
    ALERT_SERVERITY_FIELD_NUMBER: _ClassVar[int]
    ALERT_COUNT_FIELD_NUMBER: _ClassVar[int]
    cluster_id: int
    cluster_name: str
    alert_description: str
    alert_category: str
    alert_serverity: str
    alert_count: int
    def __init__(self, cluster_id: _Optional[int] = ..., cluster_name: _Optional[str] = ..., alert_description: _Optional[str] = ..., alert_category: _Optional[str] = ..., alert_serverity: _Optional[str] = ..., alert_count: _Optional[int] = ...) -> None: ...

class MonitoringAlertsResult(_message.Message):
    __slots__ = ("alerts_list", "category_alert_count_list", "num_critical_alerts", "num_warnings")
    ALERTS_LIST_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_ALERT_COUNT_LIST_FIELD_NUMBER: _ClassVar[int]
    NUM_CRITICAL_ALERTS_FIELD_NUMBER: _ClassVar[int]
    NUM_WARNINGS_FIELD_NUMBER: _ClassVar[int]
    alerts_list: _containers.RepeatedCompositeFieldContainer[QueriedAlertProto]
    category_alert_count_list: CategoryAlertCountResult
    num_critical_alerts: int
    num_warnings: int
    def __init__(self, alerts_list: _Optional[_Iterable[_Union[QueriedAlertProto, _Mapping]]] = ..., category_alert_count_list: _Optional[_Union[CategoryAlertCountResult, _Mapping]] = ..., num_critical_alerts: _Optional[int] = ..., num_warnings: _Optional[int] = ...) -> None: ...

class AgentClusterStatusArg(_message.Message):
    __slots__ = ("cluster", "alert_vec", "cluster_config")
    CLUSTER_FIELD_NUMBER: _ClassVar[int]
    ALERT_VEC_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_CONFIG_FIELD_NUMBER: _ClassVar[int]
    cluster: ClusterProto
    alert_vec: _containers.RepeatedCompositeFieldContainer[AlertProto]
    cluster_config: _cluster_config_pb2.ClusterConfigProto
    def __init__(self, cluster: _Optional[_Union[ClusterProto, _Mapping]] = ..., alert_vec: _Optional[_Iterable[_Union[AlertProto, _Mapping]]] = ..., cluster_config: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto, _Mapping]] = ...) -> None: ...

class AgentClusterStatusResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AgentClusterFirmwareInfoArg(_message.Message):
    __slots__ = ("firmware_vec",)
    FIRMWARE_VEC_FIELD_NUMBER: _ClassVar[int]
    firmware_vec: _containers.RepeatedCompositeFieldContainer[FirmwareProto]
    def __init__(self, firmware_vec: _Optional[_Iterable[_Union[FirmwareProto, _Mapping]]] = ...) -> None: ...

class AgentClusterFirmwareInfoResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AgentClusterStatsArg(_message.Message):
    __slots__ = ("entity_metadata_vec", "entity_data_point_vec")
    ENTITY_METADATA_VEC_FIELD_NUMBER: _ClassVar[int]
    ENTITY_DATA_POINT_VEC_FIELD_NUMBER: _ClassVar[int]
    entity_metadata_vec: _containers.RepeatedCompositeFieldContainer[StatsEntityMetadataProto]
    entity_data_point_vec: _containers.RepeatedCompositeFieldContainer[StatsEntityMetricDataPoint]
    def __init__(self, entity_metadata_vec: _Optional[_Iterable[_Union[StatsEntityMetadataProto, _Mapping]]] = ..., entity_data_point_vec: _Optional[_Iterable[_Union[StatsEntityMetricDataPoint, _Mapping]]] = ...) -> None: ...

class AgentClusterStatsResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AgentClusterSupportBundleResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AgentAlertsBatchResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AgentHealthcheckDataBatchResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AnomalyResult(_message.Message):
    __slots__ = ("cluster_firmware_anomaly_vec", "cluster_software_anomaly_vec", "cluster_capacity_anomaly_vec", "cluster_dedup_anomaly_vec", "num_firmware_anomalies", "num_software_anomalies", "num_capacity_anomalies", "num_de_dup_anomalies", "num_anomalies", "software_version", "firmware_model", "firmware_version", "capacity_percentage", "dedup_percentage")
    CLUSTER_FIRMWARE_ANOMALY_VEC_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_SOFTWARE_ANOMALY_VEC_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_CAPACITY_ANOMALY_VEC_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_DEDUP_ANOMALY_VEC_FIELD_NUMBER: _ClassVar[int]
    NUM_FIRMWARE_ANOMALIES_FIELD_NUMBER: _ClassVar[int]
    NUM_SOFTWARE_ANOMALIES_FIELD_NUMBER: _ClassVar[int]
    NUM_CAPACITY_ANOMALIES_FIELD_NUMBER: _ClassVar[int]
    NUM_DE_DUP_ANOMALIES_FIELD_NUMBER: _ClassVar[int]
    NUM_ANOMALIES_FIELD_NUMBER: _ClassVar[int]
    SOFTWARE_VERSION_FIELD_NUMBER: _ClassVar[int]
    FIRMWARE_MODEL_FIELD_NUMBER: _ClassVar[int]
    FIRMWARE_VERSION_FIELD_NUMBER: _ClassVar[int]
    CAPACITY_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    DEDUP_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    cluster_firmware_anomaly_vec: _containers.RepeatedCompositeFieldContainer[ClusterFirmwareAnomaliesProto]
    cluster_software_anomaly_vec: _containers.RepeatedCompositeFieldContainer[ClusterProto]
    cluster_capacity_anomaly_vec: _containers.RepeatedCompositeFieldContainer[ClusterProto]
    cluster_dedup_anomaly_vec: _containers.RepeatedCompositeFieldContainer[ClusterProto]
    num_firmware_anomalies: int
    num_software_anomalies: int
    num_capacity_anomalies: int
    num_de_dup_anomalies: int
    num_anomalies: int
    software_version: str
    firmware_model: str
    firmware_version: str
    capacity_percentage: str
    dedup_percentage: str
    def __init__(self, cluster_firmware_anomaly_vec: _Optional[_Iterable[_Union[ClusterFirmwareAnomaliesProto, _Mapping]]] = ..., cluster_software_anomaly_vec: _Optional[_Iterable[_Union[ClusterProto, _Mapping]]] = ..., cluster_capacity_anomaly_vec: _Optional[_Iterable[_Union[ClusterProto, _Mapping]]] = ..., cluster_dedup_anomaly_vec: _Optional[_Iterable[_Union[ClusterProto, _Mapping]]] = ..., num_firmware_anomalies: _Optional[int] = ..., num_software_anomalies: _Optional[int] = ..., num_capacity_anomalies: _Optional[int] = ..., num_de_dup_anomalies: _Optional[int] = ..., num_anomalies: _Optional[int] = ..., software_version: _Optional[str] = ..., firmware_model: _Optional[str] = ..., firmware_version: _Optional[str] = ..., capacity_percentage: _Optional[str] = ..., dedup_percentage: _Optional[str] = ...) -> None: ...

class ClusterFirmwareAnomaliesProto(_message.Message):
    __slots__ = ("cluster_id", "firmware_proto_vec")
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    FIRMWARE_PROTO_VEC_FIELD_NUMBER: _ClassVar[int]
    cluster_id: int
    firmware_proto_vec: _containers.RepeatedCompositeFieldContainer[FirmwareProto]
    def __init__(self, cluster_id: _Optional[int] = ..., firmware_proto_vec: _Optional[_Iterable[_Union[FirmwareProto, _Mapping]]] = ...) -> None: ...

class PlaygroundSoftwareVersionRequest(_message.Message):
    __slots__ = ("type_clusters", "filter_type", "software_version")
    TYPE_CLUSTERS_FIELD_NUMBER: _ClassVar[int]
    FILTER_TYPE_FIELD_NUMBER: _ClassVar[int]
    SOFTWARE_VERSION_FIELD_NUMBER: _ClassVar[int]
    type_clusters: ClusterStatusType
    filter_type: FilterType
    software_version: str
    def __init__(self, type_clusters: _Optional[_Union[ClusterStatusType, str]] = ..., filter_type: _Optional[_Union[FilterType, str]] = ..., software_version: _Optional[str] = ...) -> None: ...

class PlaygroundFirmwareVersionRequest(_message.Message):
    __slots__ = ("type_clusters", "firmware_key", "firmware_value")
    TYPE_CLUSTERS_FIELD_NUMBER: _ClassVar[int]
    FIRMWARE_KEY_FIELD_NUMBER: _ClassVar[int]
    FIRMWARE_VALUE_FIELD_NUMBER: _ClassVar[int]
    type_clusters: ClusterStatusType
    firmware_key: str
    firmware_value: str
    def __init__(self, type_clusters: _Optional[_Union[ClusterStatusType, str]] = ..., firmware_key: _Optional[str] = ..., firmware_value: _Optional[str] = ...) -> None: ...

class PlaygroundDeDupRequest(_message.Message):
    __slots__ = ("type_clusters", "filter_type", "de_dup_ratio")
    TYPE_CLUSTERS_FIELD_NUMBER: _ClassVar[int]
    FILTER_TYPE_FIELD_NUMBER: _ClassVar[int]
    DE_DUP_RATIO_FIELD_NUMBER: _ClassVar[int]
    type_clusters: ClusterStatusType
    filter_type: FilterType
    de_dup_ratio: str
    def __init__(self, type_clusters: _Optional[_Union[ClusterStatusType, str]] = ..., filter_type: _Optional[_Union[FilterType, str]] = ..., de_dup_ratio: _Optional[str] = ...) -> None: ...

class PlaygroundCapacityRequest(_message.Message):
    __slots__ = ("type_clusters", "filter_type", "capacity")
    TYPE_CLUSTERS_FIELD_NUMBER: _ClassVar[int]
    FILTER_TYPE_FIELD_NUMBER: _ClassVar[int]
    CAPACITY_FIELD_NUMBER: _ClassVar[int]
    type_clusters: ClusterStatusType
    filter_type: FilterType
    capacity: str
    def __init__(self, type_clusters: _Optional[_Union[ClusterStatusType, str]] = ..., filter_type: _Optional[_Union[FilterType, str]] = ..., capacity: _Optional[str] = ...) -> None: ...

class PlaygroundClusterSettingsRequest(_message.Message):
    __slots__ = ("notification_type", "is_active")
    NOTIFICATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    IS_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    notification_type: NotificationType
    is_active: bool
    def __init__(self, notification_type: _Optional[_Union[NotificationType, str]] = ..., is_active: bool = ...) -> None: ...

class GetPlaygroundResult(_message.Message):
    __slots__ = ("matched_clusters",)
    MATCHED_CLUSTERS_FIELD_NUMBER: _ClassVar[int]
    matched_clusters: _containers.RepeatedCompositeFieldContainer[ClusterProto]
    def __init__(self, matched_clusters: _Optional[_Iterable[_Union[ClusterProto, _Mapping]]] = ...) -> None: ...

class UserCluster(_message.Message):
    __slots__ = ("user_name", "cluster_id")
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    user_name: str
    cluster_id: int
    def __init__(self, user_name: _Optional[str] = ..., cluster_id: _Optional[int] = ...) -> None: ...

class AddUserClusterRequest(_message.Message):
    __slots__ = ("cluster_id",)
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    cluster_id: str
    def __init__(self, cluster_id: _Optional[str] = ...) -> None: ...

class UserClustersResult(_message.Message):
    __slots__ = ("user_clusters_vec",)
    USER_CLUSTERS_VEC_FIELD_NUMBER: _ClassVar[int]
    user_clusters_vec: _containers.RepeatedCompositeFieldContainer[ClusterProto]
    def __init__(self, user_clusters_vec: _Optional[_Iterable[_Union[ClusterProto, _Mapping]]] = ...) -> None: ...
