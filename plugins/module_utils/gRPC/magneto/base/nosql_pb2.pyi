from atom.base import event_pb2 as _event_pb2
from magneto.base import entity_pb2 as _entity_pb2
from magneto.base import credentials_pb2 as _credentials_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DSESolrInfo(_message.Message):
    __slots__ = ("solr_node_vec", "solr_port")
    SOLR_NODE_VEC_FIELD_NUMBER: _ClassVar[int]
    SOLR_PORT_FIELD_NUMBER: _ClassVar[int]
    solr_node_vec: _containers.RepeatedScalarFieldContainer[str]
    solr_port: int
    def __init__(self, solr_node_vec: _Optional[_Iterable[str]] = ..., solr_port: _Optional[int] = ...) -> None: ...

class CassandraPortInfo(_message.Message):
    __slots__ = ("native_transport_port", "rpc_port", "storage_port", "ssl_storage_port", "jmx_port")
    NATIVE_TRANSPORT_PORT_FIELD_NUMBER: _ClassVar[int]
    RPC_PORT_FIELD_NUMBER: _ClassVar[int]
    STORAGE_PORT_FIELD_NUMBER: _ClassVar[int]
    SSL_STORAGE_PORT_FIELD_NUMBER: _ClassVar[int]
    JMX_PORT_FIELD_NUMBER: _ClassVar[int]
    native_transport_port: int
    rpc_port: int
    storage_port: int
    ssl_storage_port: int
    jmx_port: int
    def __init__(self, native_transport_port: _Optional[int] = ..., rpc_port: _Optional[int] = ..., storage_port: _Optional[int] = ..., ssl_storage_port: _Optional[int] = ..., jmx_port: _Optional[int] = ...) -> None: ...

class CassandraSecurityInfo(_message.Message):
    __slots__ = ("cassandra_authorizer", "cassandra_auth_required", "cassandra_auth_type", "dse_authorization_enabled", "cassandra_client_encryption_enabled", "cassandra_server_encryption_req_client_auth", "cassandra_server_internode_encryption_type", "cassandra_authenticator")
    class CassandraAuthType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PASSWORD: _ClassVar[CassandraSecurityInfo.CassandraAuthType]
        KERBEROS: _ClassVar[CassandraSecurityInfo.CassandraAuthType]
        LDAP: _ClassVar[CassandraSecurityInfo.CassandraAuthType]
    PASSWORD: CassandraSecurityInfo.CassandraAuthType
    KERBEROS: CassandraSecurityInfo.CassandraAuthType
    LDAP: CassandraSecurityInfo.CassandraAuthType
    CASSANDRA_AUTHORIZER_FIELD_NUMBER: _ClassVar[int]
    CASSANDRA_AUTH_REQUIRED_FIELD_NUMBER: _ClassVar[int]
    CASSANDRA_AUTH_TYPE_FIELD_NUMBER: _ClassVar[int]
    DSE_AUTHORIZATION_ENABLED_FIELD_NUMBER: _ClassVar[int]
    CASSANDRA_CLIENT_ENCRYPTION_ENABLED_FIELD_NUMBER: _ClassVar[int]
    CASSANDRA_SERVER_ENCRYPTION_REQ_CLIENT_AUTH_FIELD_NUMBER: _ClassVar[int]
    CASSANDRA_SERVER_INTERNODE_ENCRYPTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    CASSANDRA_AUTHENTICATOR_FIELD_NUMBER: _ClassVar[int]
    cassandra_authorizer: str
    cassandra_auth_required: bool
    cassandra_auth_type: CassandraSecurityInfo.CassandraAuthType
    dse_authorization_enabled: bool
    cassandra_client_encryption_enabled: bool
    cassandra_server_encryption_req_client_auth: bool
    cassandra_server_internode_encryption_type: str
    cassandra_authenticator: str
    def __init__(self, cassandra_authorizer: _Optional[str] = ..., cassandra_auth_required: bool = ..., cassandra_auth_type: _Optional[_Union[CassandraSecurityInfo.CassandraAuthType, str]] = ..., dse_authorization_enabled: bool = ..., cassandra_client_encryption_enabled: bool = ..., cassandra_server_encryption_req_client_auth: bool = ..., cassandra_server_internode_encryption_type: _Optional[str] = ..., cassandra_authenticator: _Optional[str] = ...) -> None: ...

class CassandraDiscoveryParams(_message.Message):
    __slots__ = ("primary_host", "cassandra_config_directory", "is_dse_tiered_storage", "is_dse_authenticator", "dse_config_directory", "ssh_credentials", "is_cassandra_connection_allowed", "is_graph_discovery_enabled", "is_system_ks_discovery_enabled")
    PRIMARY_HOST_FIELD_NUMBER: _ClassVar[int]
    CASSANDRA_CONFIG_DIRECTORY_FIELD_NUMBER: _ClassVar[int]
    IS_DSE_TIERED_STORAGE_FIELD_NUMBER: _ClassVar[int]
    IS_DSE_AUTHENTICATOR_FIELD_NUMBER: _ClassVar[int]
    DSE_CONFIG_DIRECTORY_FIELD_NUMBER: _ClassVar[int]
    SSH_CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    IS_CASSANDRA_CONNECTION_ALLOWED_FIELD_NUMBER: _ClassVar[int]
    IS_GRAPH_DISCOVERY_ENABLED_FIELD_NUMBER: _ClassVar[int]
    IS_SYSTEM_KS_DISCOVERY_ENABLED_FIELD_NUMBER: _ClassVar[int]
    primary_host: str
    cassandra_config_directory: str
    is_dse_tiered_storage: bool
    is_dse_authenticator: bool
    dse_config_directory: str
    ssh_credentials: _credentials_pb2.Credentials
    is_cassandra_connection_allowed: bool
    is_graph_discovery_enabled: bool
    is_system_ks_discovery_enabled: bool
    def __init__(self, primary_host: _Optional[str] = ..., cassandra_config_directory: _Optional[str] = ..., is_dse_tiered_storage: bool = ..., is_dse_authenticator: bool = ..., dse_config_directory: _Optional[str] = ..., ssh_credentials: _Optional[_Union[_credentials_pb2.Credentials, _Mapping]] = ..., is_cassandra_connection_allowed: bool = ..., is_graph_discovery_enabled: bool = ..., is_system_ks_discovery_enabled: bool = ...) -> None: ...

class CassandraConnectParams(_message.Message):
    __slots__ = ("cassandra_discovery_params", "seed_vec", "is_cassandra_jmx_auth_enabled", "cassandra_ports_info", "cassandra_security_info", "cassandra_credentials", "jmx_credentials", "kerberos_sasl_protocol", "kerberos_principal")
    CASSANDRA_DISCOVERY_PARAMS_FIELD_NUMBER: _ClassVar[int]
    SEED_VEC_FIELD_NUMBER: _ClassVar[int]
    IS_CASSANDRA_JMX_AUTH_ENABLED_FIELD_NUMBER: _ClassVar[int]
    CASSANDRA_PORTS_INFO_FIELD_NUMBER: _ClassVar[int]
    CASSANDRA_SECURITY_INFO_FIELD_NUMBER: _ClassVar[int]
    CASSANDRA_CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    JMX_CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    KERBEROS_SASL_PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    KERBEROS_PRINCIPAL_FIELD_NUMBER: _ClassVar[int]
    cassandra_discovery_params: CassandraDiscoveryParams
    seed_vec: _containers.RepeatedScalarFieldContainer[str]
    is_cassandra_jmx_auth_enabled: bool
    cassandra_ports_info: CassandraPortInfo
    cassandra_security_info: CassandraSecurityInfo
    cassandra_credentials: _credentials_pb2.Credentials
    jmx_credentials: _credentials_pb2.Credentials
    kerberos_sasl_protocol: str
    kerberos_principal: str
    def __init__(self, cassandra_discovery_params: _Optional[_Union[CassandraDiscoveryParams, _Mapping]] = ..., seed_vec: _Optional[_Iterable[str]] = ..., is_cassandra_jmx_auth_enabled: bool = ..., cassandra_ports_info: _Optional[_Union[CassandraPortInfo, _Mapping]] = ..., cassandra_security_info: _Optional[_Union[CassandraSecurityInfo, _Mapping]] = ..., cassandra_credentials: _Optional[_Union[_credentials_pb2.Credentials, _Mapping]] = ..., jmx_credentials: _Optional[_Union[_credentials_pb2.Credentials, _Mapping]] = ..., kerberos_sasl_protocol: _Optional[str] = ..., kerberos_principal: _Optional[str] = ...) -> None: ...

class NodeToTieredStorageDirectoriesMap(_message.Message):
    __slots__ = ("cassandra_node_name", "tiered_storage_directories_vec")
    CASSANDRA_NODE_NAME_FIELD_NUMBER: _ClassVar[int]
    TIERED_STORAGE_DIRECTORIES_VEC_FIELD_NUMBER: _ClassVar[int]
    cassandra_node_name: str
    tiered_storage_directories_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, cassandra_node_name: _Optional[str] = ..., tiered_storage_directories_vec: _Optional[_Iterable[str]] = ...) -> None: ...

class CassandraAdditionalParams(_message.Message):
    __slots__ = ("data_center_vec", "cassandra_partitioner", "cassandra_version", "dse_version", "cassandra_classpath_suffix", "dse_solr_info", "tiered_storage_dirs_map", "commit_log_backup_location")
    DATA_CENTER_VEC_FIELD_NUMBER: _ClassVar[int]
    CASSANDRA_PARTITIONER_FIELD_NUMBER: _ClassVar[int]
    CASSANDRA_VERSION_FIELD_NUMBER: _ClassVar[int]
    DSE_VERSION_FIELD_NUMBER: _ClassVar[int]
    CASSANDRA_CLASSPATH_SUFFIX_FIELD_NUMBER: _ClassVar[int]
    DSE_SOLR_INFO_FIELD_NUMBER: _ClassVar[int]
    TIERED_STORAGE_DIRS_MAP_FIELD_NUMBER: _ClassVar[int]
    COMMIT_LOG_BACKUP_LOCATION_FIELD_NUMBER: _ClassVar[int]
    data_center_vec: _containers.RepeatedScalarFieldContainer[str]
    cassandra_partitioner: str
    cassandra_version: str
    dse_version: str
    cassandra_classpath_suffix: str
    dse_solr_info: DSESolrInfo
    tiered_storage_dirs_map: _containers.RepeatedCompositeFieldContainer[NodeToTieredStorageDirectoriesMap]
    commit_log_backup_location: str
    def __init__(self, data_center_vec: _Optional[_Iterable[str]] = ..., cassandra_partitioner: _Optional[str] = ..., cassandra_version: _Optional[str] = ..., dse_version: _Optional[str] = ..., cassandra_classpath_suffix: _Optional[str] = ..., dse_solr_info: _Optional[_Union[DSESolrInfo, _Mapping]] = ..., tiered_storage_dirs_map: _Optional[_Iterable[_Union[NodeToTieredStorageDirectoriesMap, _Mapping]]] = ..., commit_log_backup_location: _Optional[str] = ...) -> None: ...

class MongoDBConnectParams(_message.Message):
    __slots__ = ("seeds", "authenticating_database_name", "requires_ssl", "auth_type", "credentials")
    class MongoDBAuthType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SCRAM: _ClassVar[MongoDBConnectParams.MongoDBAuthType]
        LDAP: _ClassVar[MongoDBConnectParams.MongoDBAuthType]
        NONE: _ClassVar[MongoDBConnectParams.MongoDBAuthType]
        KERBEROS: _ClassVar[MongoDBConnectParams.MongoDBAuthType]
    SCRAM: MongoDBConnectParams.MongoDBAuthType
    LDAP: MongoDBConnectParams.MongoDBAuthType
    NONE: MongoDBConnectParams.MongoDBAuthType
    KERBEROS: MongoDBConnectParams.MongoDBAuthType
    SEEDS_FIELD_NUMBER: _ClassVar[int]
    AUTHENTICATING_DATABASE_NAME_FIELD_NUMBER: _ClassVar[int]
    REQUIRES_SSL_FIELD_NUMBER: _ClassVar[int]
    AUTH_TYPE_FIELD_NUMBER: _ClassVar[int]
    CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    seeds: _containers.RepeatedScalarFieldContainer[str]
    authenticating_database_name: str
    requires_ssl: bool
    auth_type: MongoDBConnectParams.MongoDBAuthType
    credentials: _credentials_pb2.Credentials
    def __init__(self, seeds: _Optional[_Iterable[str]] = ..., authenticating_database_name: _Optional[str] = ..., requires_ssl: bool = ..., auth_type: _Optional[_Union[MongoDBConnectParams.MongoDBAuthType, str]] = ..., credentials: _Optional[_Union[_credentials_pb2.Credentials, _Mapping]] = ...) -> None: ...

class MongoDBAdditionalParams(_message.Message):
    __slots__ = ("use_secondary_for_backup", "secondary_node_tag")
    USE_SECONDARY_FOR_BACKUP_FIELD_NUMBER: _ClassVar[int]
    SECONDARY_NODE_TAG_FIELD_NUMBER: _ClassVar[int]
    use_secondary_for_backup: bool
    secondary_node_tag: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, use_secondary_for_backup: bool = ..., secondary_node_tag: _Optional[_Iterable[str]] = ...) -> None: ...

class CouchbaseConnectParams(_message.Message):
    __slots__ = ("seeds", "requires_ssl", "http_direct_port", "carrier_direct_port", "credentials")
    SEEDS_FIELD_NUMBER: _ClassVar[int]
    REQUIRES_SSL_FIELD_NUMBER: _ClassVar[int]
    HTTP_DIRECT_PORT_FIELD_NUMBER: _ClassVar[int]
    CARRIER_DIRECT_PORT_FIELD_NUMBER: _ClassVar[int]
    CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    seeds: _containers.RepeatedScalarFieldContainer[str]
    requires_ssl: bool
    http_direct_port: int
    carrier_direct_port: int
    credentials: _credentials_pb2.Credentials
    def __init__(self, seeds: _Optional[_Iterable[str]] = ..., requires_ssl: bool = ..., http_direct_port: _Optional[int] = ..., carrier_direct_port: _Optional[int] = ..., credentials: _Optional[_Union[_credentials_pb2.Credentials, _Mapping]] = ...) -> None: ...

class HBaseDiscoveryParams(_message.Message):
    __slots__ = ("host", "hbase_config_directory", "ssh_credentials")
    HOST_FIELD_NUMBER: _ClassVar[int]
    HBASE_CONFIG_DIRECTORY_FIELD_NUMBER: _ClassVar[int]
    SSH_CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    host: str
    hbase_config_directory: str
    ssh_credentials: _credentials_pb2.Credentials
    def __init__(self, host: _Optional[str] = ..., hbase_config_directory: _Optional[str] = ..., ssh_credentials: _Optional[_Union[_credentials_pb2.Credentials, _Mapping]] = ...) -> None: ...

class HBaseConnectParams(_message.Message):
    __slots__ = ("hdfs_entity_id", "hbase_zookeeper_quorum", "hbase_root_data_directory", "configuration", "hbase_principal", "hbase_auth_type")
    class HbaseAuthType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        KERBEROS: _ClassVar[HBaseConnectParams.HbaseAuthType]
        NONE: _ClassVar[HBaseConnectParams.HbaseAuthType]
    KERBEROS: HBaseConnectParams.HbaseAuthType
    NONE: HBaseConnectParams.HbaseAuthType
    class ConfigurationEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    HDFS_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    HBASE_ZOOKEEPER_QUORUM_FIELD_NUMBER: _ClassVar[int]
    HBASE_ROOT_DATA_DIRECTORY_FIELD_NUMBER: _ClassVar[int]
    CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
    HBASE_PRINCIPAL_FIELD_NUMBER: _ClassVar[int]
    HBASE_AUTH_TYPE_FIELD_NUMBER: _ClassVar[int]
    hdfs_entity_id: int
    hbase_zookeeper_quorum: _containers.RepeatedScalarFieldContainer[str]
    hbase_root_data_directory: str
    configuration: _containers.ScalarMap[str, str]
    hbase_principal: str
    hbase_auth_type: HBaseConnectParams.HbaseAuthType
    def __init__(self, hdfs_entity_id: _Optional[int] = ..., hbase_zookeeper_quorum: _Optional[_Iterable[str]] = ..., hbase_root_data_directory: _Optional[str] = ..., configuration: _Optional[_Mapping[str, str]] = ..., hbase_principal: _Optional[str] = ..., hbase_auth_type: _Optional[_Union[HBaseConnectParams.HbaseAuthType, str]] = ...) -> None: ...

class HdfsDiscoveryParams(_message.Message):
    __slots__ = ("host", "hdfs_config_directory", "ssh_credentials")
    HOST_FIELD_NUMBER: _ClassVar[int]
    HDFS_CONFIG_DIRECTORY_FIELD_NUMBER: _ClassVar[int]
    SSH_CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    host: str
    hdfs_config_directory: str
    ssh_credentials: _credentials_pb2.Credentials
    def __init__(self, host: _Optional[str] = ..., hdfs_config_directory: _Optional[str] = ..., ssh_credentials: _Optional[_Union[_credentials_pb2.Credentials, _Mapping]] = ...) -> None: ...

class HdfsConnectParams(_message.Message):
    __slots__ = ("namenode", "port", "configuration", "hadoop_distribution", "hadoop_version", "hdfs_principal", "hdfs_auth_type")
    class HadoopDistribution(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CDH: _ClassVar[HdfsConnectParams.HadoopDistribution]
        HDP: _ClassVar[HdfsConnectParams.HadoopDistribution]
    CDH: HdfsConnectParams.HadoopDistribution
    HDP: HdfsConnectParams.HadoopDistribution
    class HdfsAuthType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        KERBEROS: _ClassVar[HdfsConnectParams.HdfsAuthType]
        NONE: _ClassVar[HdfsConnectParams.HdfsAuthType]
    KERBEROS: HdfsConnectParams.HdfsAuthType
    NONE: HdfsConnectParams.HdfsAuthType
    class ConfigurationEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAMENODE_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
    HADOOP_DISTRIBUTION_FIELD_NUMBER: _ClassVar[int]
    HADOOP_VERSION_FIELD_NUMBER: _ClassVar[int]
    HDFS_PRINCIPAL_FIELD_NUMBER: _ClassVar[int]
    HDFS_AUTH_TYPE_FIELD_NUMBER: _ClassVar[int]
    namenode: str
    port: int
    configuration: _containers.ScalarMap[str, str]
    hadoop_distribution: HdfsConnectParams.HadoopDistribution
    hadoop_version: str
    hdfs_principal: str
    hdfs_auth_type: HdfsConnectParams.HdfsAuthType
    def __init__(self, namenode: _Optional[str] = ..., port: _Optional[int] = ..., configuration: _Optional[_Mapping[str, str]] = ..., hadoop_distribution: _Optional[_Union[HdfsConnectParams.HadoopDistribution, str]] = ..., hadoop_version: _Optional[str] = ..., hdfs_principal: _Optional[str] = ..., hdfs_auth_type: _Optional[_Union[HdfsConnectParams.HdfsAuthType, str]] = ...) -> None: ...

class HiveDiscoveryParams(_message.Message):
    __slots__ = ("host", "hive_config_directory", "ssh_credentials")
    HOST_FIELD_NUMBER: _ClassVar[int]
    HIVE_CONFIG_DIRECTORY_FIELD_NUMBER: _ClassVar[int]
    SSH_CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    host: str
    hive_config_directory: str
    ssh_credentials: _credentials_pb2.Credentials
    def __init__(self, host: _Optional[str] = ..., hive_config_directory: _Optional[str] = ..., ssh_credentials: _Optional[_Union[_credentials_pb2.Credentials, _Mapping]] = ...) -> None: ...

class HiveConnectParams(_message.Message):
    __slots__ = ("hdfs_entity_id", "metastore", "thrift_port", "configuration", "hive_principal", "hive_auth_type")
    class HiveAuthType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        KERBEROS: _ClassVar[HiveConnectParams.HiveAuthType]
        NONE: _ClassVar[HiveConnectParams.HiveAuthType]
    KERBEROS: HiveConnectParams.HiveAuthType
    NONE: HiveConnectParams.HiveAuthType
    class ConfigurationEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    HDFS_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    METASTORE_FIELD_NUMBER: _ClassVar[int]
    THRIFT_PORT_FIELD_NUMBER: _ClassVar[int]
    CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
    HIVE_PRINCIPAL_FIELD_NUMBER: _ClassVar[int]
    HIVE_AUTH_TYPE_FIELD_NUMBER: _ClassVar[int]
    hdfs_entity_id: int
    metastore: str
    thrift_port: int
    configuration: _containers.ScalarMap[str, str]
    hive_principal: str
    hive_auth_type: HiveConnectParams.HiveAuthType
    def __init__(self, hdfs_entity_id: _Optional[int] = ..., metastore: _Optional[str] = ..., thrift_port: _Optional[int] = ..., configuration: _Optional[_Mapping[str, str]] = ..., hive_principal: _Optional[str] = ..., hive_auth_type: _Optional[_Union[HiveConnectParams.HiveAuthType, str]] = ...) -> None: ...

class CassandraBackupJobParams(_message.Message):
    __slots__ = ("cassandra_additional_info", "selected_data_center_vec", "graph_handling_enabled", "is_only_log_backup_job", "retention_period_in_secs", "roles_gflag_enabled", "is_system_ks_backup", "make_primary_log_backup", "previous_job_end_time_in_usecs", "job_start_time_in_usecs")
    CASSANDRA_ADDITIONAL_INFO_FIELD_NUMBER: _ClassVar[int]
    SELECTED_DATA_CENTER_VEC_FIELD_NUMBER: _ClassVar[int]
    GRAPH_HANDLING_ENABLED_FIELD_NUMBER: _ClassVar[int]
    IS_ONLY_LOG_BACKUP_JOB_FIELD_NUMBER: _ClassVar[int]
    RETENTION_PERIOD_IN_SECS_FIELD_NUMBER: _ClassVar[int]
    ROLES_GFLAG_ENABLED_FIELD_NUMBER: _ClassVar[int]
    IS_SYSTEM_KS_BACKUP_FIELD_NUMBER: _ClassVar[int]
    MAKE_PRIMARY_LOG_BACKUP_FIELD_NUMBER: _ClassVar[int]
    PREVIOUS_JOB_END_TIME_IN_USECS_FIELD_NUMBER: _ClassVar[int]
    JOB_START_TIME_IN_USECS_FIELD_NUMBER: _ClassVar[int]
    cassandra_additional_info: CassandraAdditionalParams
    selected_data_center_vec: _containers.RepeatedScalarFieldContainer[str]
    graph_handling_enabled: bool
    is_only_log_backup_job: bool
    retention_period_in_secs: int
    roles_gflag_enabled: bool
    is_system_ks_backup: bool
    make_primary_log_backup: bool
    previous_job_end_time_in_usecs: int
    job_start_time_in_usecs: int
    def __init__(self, cassandra_additional_info: _Optional[_Union[CassandraAdditionalParams, _Mapping]] = ..., selected_data_center_vec: _Optional[_Iterable[str]] = ..., graph_handling_enabled: bool = ..., is_only_log_backup_job: bool = ..., retention_period_in_secs: _Optional[int] = ..., roles_gflag_enabled: bool = ..., is_system_ks_backup: bool = ..., make_primary_log_backup: bool = ..., previous_job_end_time_in_usecs: _Optional[int] = ..., job_start_time_in_usecs: _Optional[int] = ...) -> None: ...

class MongoDBBackupJobParams(_message.Message):
    __slots__ = ("mongodb_additional_info",)
    MONGODB_ADDITIONAL_INFO_FIELD_NUMBER: _ClassVar[int]
    mongodb_additional_info: MongoDBAdditionalParams
    def __init__(self, mongodb_additional_info: _Optional[_Union[MongoDBAdditionalParams, _Mapping]] = ...) -> None: ...

class CouchbaseBackupJobParams(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class HBaseBackupJobParams(_message.Message):
    __slots__ = ("hdfs_connect_params",)
    HDFS_CONNECT_PARAMS_FIELD_NUMBER: _ClassVar[int]
    hdfs_connect_params: HdfsConnectParams
    def __init__(self, hdfs_connect_params: _Optional[_Union[HdfsConnectParams, _Mapping]] = ...) -> None: ...

class HdfsBackupJobParams(_message.Message):
    __slots__ = ("hdfs_protect_pattern", "hdfs_exclude_pattern")
    HDFS_PROTECT_PATTERN_FIELD_NUMBER: _ClassVar[int]
    HDFS_EXCLUDE_PATTERN_FIELD_NUMBER: _ClassVar[int]
    hdfs_protect_pattern: _containers.RepeatedScalarFieldContainer[str]
    hdfs_exclude_pattern: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, hdfs_protect_pattern: _Optional[_Iterable[str]] = ..., hdfs_exclude_pattern: _Optional[_Iterable[str]] = ...) -> None: ...

class HiveBackupJobParams(_message.Message):
    __slots__ = ("hdfs_connect_params",)
    HDFS_CONNECT_PARAMS_FIELD_NUMBER: _ClassVar[int]
    hdfs_connect_params: HdfsConnectParams
    def __init__(self, hdfs_connect_params: _Optional[_Union[HdfsConnectParams, _Mapping]] = ...) -> None: ...

class NoSqlBackupJobParams(_message.Message):
    __slots__ = ("concurrency", "bandwidth_bytes_per_second", "compaction_job_interval_secs", "last_compaction_run_time_usecs", "gc_job_interval_secs", "last_gc_run_time_usecs", "gc_retention_period_days", "cassandra_backup_job_params", "mongodb_backup_job_params", "couchbase_backup_job_params", "hbase_backup_job_params", "hdfs_backup_job_params", "hive_backup_job_params", "previous_protected_entity_ids_vec", "immediate_ancestor_map")
    class ImmediateAncestorMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _entity_pb2.EntityProto
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ...) -> None: ...
    CONCURRENCY_FIELD_NUMBER: _ClassVar[int]
    BANDWIDTH_BYTES_PER_SECOND_FIELD_NUMBER: _ClassVar[int]
    COMPACTION_JOB_INTERVAL_SECS_FIELD_NUMBER: _ClassVar[int]
    LAST_COMPACTION_RUN_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    GC_JOB_INTERVAL_SECS_FIELD_NUMBER: _ClassVar[int]
    LAST_GC_RUN_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    GC_RETENTION_PERIOD_DAYS_FIELD_NUMBER: _ClassVar[int]
    CASSANDRA_BACKUP_JOB_PARAMS_FIELD_NUMBER: _ClassVar[int]
    MONGODB_BACKUP_JOB_PARAMS_FIELD_NUMBER: _ClassVar[int]
    COUCHBASE_BACKUP_JOB_PARAMS_FIELD_NUMBER: _ClassVar[int]
    HBASE_BACKUP_JOB_PARAMS_FIELD_NUMBER: _ClassVar[int]
    HDFS_BACKUP_JOB_PARAMS_FIELD_NUMBER: _ClassVar[int]
    HIVE_BACKUP_JOB_PARAMS_FIELD_NUMBER: _ClassVar[int]
    PREVIOUS_PROTECTED_ENTITY_IDS_VEC_FIELD_NUMBER: _ClassVar[int]
    IMMEDIATE_ANCESTOR_MAP_FIELD_NUMBER: _ClassVar[int]
    concurrency: int
    bandwidth_bytes_per_second: int
    compaction_job_interval_secs: int
    last_compaction_run_time_usecs: int
    gc_job_interval_secs: int
    last_gc_run_time_usecs: int
    gc_retention_period_days: int
    cassandra_backup_job_params: CassandraBackupJobParams
    mongodb_backup_job_params: MongoDBBackupJobParams
    couchbase_backup_job_params: CouchbaseBackupJobParams
    hbase_backup_job_params: HBaseBackupJobParams
    hdfs_backup_job_params: HdfsBackupJobParams
    hive_backup_job_params: HiveBackupJobParams
    previous_protected_entity_ids_vec: _containers.RepeatedScalarFieldContainer[int]
    immediate_ancestor_map: _containers.MessageMap[int, _entity_pb2.EntityProto]
    def __init__(self, concurrency: _Optional[int] = ..., bandwidth_bytes_per_second: _Optional[int] = ..., compaction_job_interval_secs: _Optional[int] = ..., last_compaction_run_time_usecs: _Optional[int] = ..., gc_job_interval_secs: _Optional[int] = ..., last_gc_run_time_usecs: _Optional[int] = ..., gc_retention_period_days: _Optional[int] = ..., cassandra_backup_job_params: _Optional[_Union[CassandraBackupJobParams, _Mapping]] = ..., mongodb_backup_job_params: _Optional[_Union[MongoDBBackupJobParams, _Mapping]] = ..., couchbase_backup_job_params: _Optional[_Union[CouchbaseBackupJobParams, _Mapping]] = ..., hbase_backup_job_params: _Optional[_Union[HBaseBackupJobParams, _Mapping]] = ..., hdfs_backup_job_params: _Optional[_Union[HdfsBackupJobParams, _Mapping]] = ..., hive_backup_job_params: _Optional[_Union[HiveBackupJobParams, _Mapping]] = ..., previous_protected_entity_ids_vec: _Optional[_Iterable[int]] = ..., immediate_ancestor_map: _Optional[_Mapping[int, _entity_pb2.EntityProto]] = ...) -> None: ...

class CassandraRecoverJobParams(_message.Message):
    __slots__ = ("suffix", "cassandra_additional_info", "selected_data_center_vec", "staging_directory_vec", "graph_handling_enabled", "log_restore_directory", "log_recover_params", "restart_allowed", "restart_immediately", "restart_time", "restart_command", "is_finalise_phase", "finalise_restore_task_id", "roles_gflag_enabled", "restore_roles_and_permissions", "is_system_ks_recovery", "is_live_table_restore")
    SUFFIX_FIELD_NUMBER: _ClassVar[int]
    CASSANDRA_ADDITIONAL_INFO_FIELD_NUMBER: _ClassVar[int]
    SELECTED_DATA_CENTER_VEC_FIELD_NUMBER: _ClassVar[int]
    STAGING_DIRECTORY_VEC_FIELD_NUMBER: _ClassVar[int]
    GRAPH_HANDLING_ENABLED_FIELD_NUMBER: _ClassVar[int]
    LOG_RESTORE_DIRECTORY_FIELD_NUMBER: _ClassVar[int]
    LOG_RECOVER_PARAMS_FIELD_NUMBER: _ClassVar[int]
    RESTART_ALLOWED_FIELD_NUMBER: _ClassVar[int]
    RESTART_IMMEDIATELY_FIELD_NUMBER: _ClassVar[int]
    RESTART_TIME_FIELD_NUMBER: _ClassVar[int]
    RESTART_COMMAND_FIELD_NUMBER: _ClassVar[int]
    IS_FINALISE_PHASE_FIELD_NUMBER: _ClassVar[int]
    FINALISE_RESTORE_TASK_ID_FIELD_NUMBER: _ClassVar[int]
    ROLES_GFLAG_ENABLED_FIELD_NUMBER: _ClassVar[int]
    RESTORE_ROLES_AND_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    IS_SYSTEM_KS_RECOVERY_FIELD_NUMBER: _ClassVar[int]
    IS_LIVE_TABLE_RESTORE_FIELD_NUMBER: _ClassVar[int]
    suffix: str
    cassandra_additional_info: CassandraAdditionalParams
    selected_data_center_vec: _containers.RepeatedScalarFieldContainer[str]
    staging_directory_vec: _containers.RepeatedScalarFieldContainer[str]
    graph_handling_enabled: bool
    log_restore_directory: str
    log_recover_params: CassandraLogRecoverJobParams
    restart_allowed: bool
    restart_immediately: bool
    restart_time: int
    restart_command: str
    is_finalise_phase: bool
    finalise_restore_task_id: int
    roles_gflag_enabled: bool
    restore_roles_and_permissions: bool
    is_system_ks_recovery: bool
    is_live_table_restore: bool
    def __init__(self, suffix: _Optional[str] = ..., cassandra_additional_info: _Optional[_Union[CassandraAdditionalParams, _Mapping]] = ..., selected_data_center_vec: _Optional[_Iterable[str]] = ..., staging_directory_vec: _Optional[_Iterable[str]] = ..., graph_handling_enabled: bool = ..., log_restore_directory: _Optional[str] = ..., log_recover_params: _Optional[_Union[CassandraLogRecoverJobParams, _Mapping]] = ..., restart_allowed: bool = ..., restart_immediately: bool = ..., restart_time: _Optional[int] = ..., restart_command: _Optional[str] = ..., is_finalise_phase: bool = ..., finalise_restore_task_id: _Optional[int] = ..., roles_gflag_enabled: bool = ..., restore_roles_and_permissions: bool = ..., is_system_ks_recovery: bool = ..., is_live_table_restore: bool = ...) -> None: ...

class CassandraLogRecoverJobParams(_message.Message):
    __slots__ = ("log_backup_view_box_name", "log_backup_view_name", "start_time_for_log_replay_in_usecs", "end_time_for_log_replay_in_usecs", "object_names")
    LOG_BACKUP_VIEW_BOX_NAME_FIELD_NUMBER: _ClassVar[int]
    LOG_BACKUP_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FOR_LOG_REPLAY_IN_USECS_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FOR_LOG_REPLAY_IN_USECS_FIELD_NUMBER: _ClassVar[int]
    OBJECT_NAMES_FIELD_NUMBER: _ClassVar[int]
    log_backup_view_box_name: str
    log_backup_view_name: str
    start_time_for_log_replay_in_usecs: int
    end_time_for_log_replay_in_usecs: int
    object_names: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, log_backup_view_box_name: _Optional[str] = ..., log_backup_view_name: _Optional[str] = ..., start_time_for_log_replay_in_usecs: _Optional[int] = ..., end_time_for_log_replay_in_usecs: _Optional[int] = ..., object_names: _Optional[_Iterable[str]] = ...) -> None: ...

class MongoDBRecoverJobParams(_message.Message):
    __slots__ = ("suffix",)
    SUFFIX_FIELD_NUMBER: _ClassVar[int]
    suffix: str
    def __init__(self, suffix: _Optional[str] = ...) -> None: ...

class CouchbaseRecoverJobParams(_message.Message):
    __slots__ = ("suffix", "appendDocuments", "ddlOnlyRecovery", "overwriteUsers", "documents_filter_type", "id_regex", "filter_expression")
    class DocumentsFilterType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NONE: _ClassVar[CouchbaseRecoverJobParams.DocumentsFilterType]
        ID: _ClassVar[CouchbaseRecoverJobParams.DocumentsFilterType]
        CONTENT: _ClassVar[CouchbaseRecoverJobParams.DocumentsFilterType]
    NONE: CouchbaseRecoverJobParams.DocumentsFilterType
    ID: CouchbaseRecoverJobParams.DocumentsFilterType
    CONTENT: CouchbaseRecoverJobParams.DocumentsFilterType
    SUFFIX_FIELD_NUMBER: _ClassVar[int]
    APPENDDOCUMENTS_FIELD_NUMBER: _ClassVar[int]
    DDLONLYRECOVERY_FIELD_NUMBER: _ClassVar[int]
    OVERWRITEUSERS_FIELD_NUMBER: _ClassVar[int]
    DOCUMENTS_FILTER_TYPE_FIELD_NUMBER: _ClassVar[int]
    ID_REGEX_FIELD_NUMBER: _ClassVar[int]
    FILTER_EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    suffix: str
    appendDocuments: bool
    ddlOnlyRecovery: bool
    overwriteUsers: bool
    documents_filter_type: CouchbaseRecoverJobParams.DocumentsFilterType
    id_regex: str
    filter_expression: str
    def __init__(self, suffix: _Optional[str] = ..., appendDocuments: bool = ..., ddlOnlyRecovery: bool = ..., overwriteUsers: bool = ..., documents_filter_type: _Optional[_Union[CouchbaseRecoverJobParams.DocumentsFilterType, str]] = ..., id_regex: _Optional[str] = ..., filter_expression: _Optional[str] = ...) -> None: ...

class HBaseRecoverJobParams(_message.Message):
    __slots__ = ("suffix", "hdfs_connect_params")
    SUFFIX_FIELD_NUMBER: _ClassVar[int]
    HDFS_CONNECT_PARAMS_FIELD_NUMBER: _ClassVar[int]
    suffix: str
    hdfs_connect_params: HdfsConnectParams
    def __init__(self, suffix: _Optional[str] = ..., hdfs_connect_params: _Optional[_Union[HdfsConnectParams, _Mapping]] = ...) -> None: ...

class HdfsRecoverJobParams(_message.Message):
    __slots__ = ("target_directory", "hdfs_recover_pattern", "hdfs_exclude_pattern")
    TARGET_DIRECTORY_FIELD_NUMBER: _ClassVar[int]
    HDFS_RECOVER_PATTERN_FIELD_NUMBER: _ClassVar[int]
    HDFS_EXCLUDE_PATTERN_FIELD_NUMBER: _ClassVar[int]
    target_directory: str
    hdfs_recover_pattern: _containers.RepeatedScalarFieldContainer[str]
    hdfs_exclude_pattern: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, target_directory: _Optional[str] = ..., hdfs_recover_pattern: _Optional[_Iterable[str]] = ..., hdfs_exclude_pattern: _Optional[_Iterable[str]] = ...) -> None: ...

class HiveRecoverJobParams(_message.Message):
    __slots__ = ("suffix", "hdfs_connect_params")
    SUFFIX_FIELD_NUMBER: _ClassVar[int]
    HDFS_CONNECT_PARAMS_FIELD_NUMBER: _ClassVar[int]
    suffix: str
    hdfs_connect_params: HdfsConnectParams
    def __init__(self, suffix: _Optional[str] = ..., hdfs_connect_params: _Optional[_Union[HdfsConnectParams, _Mapping]] = ...) -> None: ...

class NoSqlMirrorRecoveryJobParams(_message.Message):
    __slots__ = ("mirror_restore_parent_task_id",)
    MIRROR_RESTORE_PARENT_TASK_ID_FIELD_NUMBER: _ClassVar[int]
    mirror_restore_parent_task_id: int
    def __init__(self, mirror_restore_parent_task_id: _Optional[int] = ...) -> None: ...

class NoSqlRecoverJobParams(_message.Message):
    __slots__ = ("concurrency", "bandwidth_bytes_per_second", "overwrite", "cassandra_recover_job_params", "mongodb_recover_job_params", "couchbase_recover_job_params", "hbase_recover_job_params", "hdfs_recover_job_params", "hive_recover_job_params", "mirror_job_params", "continue_restore_on_error")
    CONCURRENCY_FIELD_NUMBER: _ClassVar[int]
    BANDWIDTH_BYTES_PER_SECOND_FIELD_NUMBER: _ClassVar[int]
    OVERWRITE_FIELD_NUMBER: _ClassVar[int]
    CASSANDRA_RECOVER_JOB_PARAMS_FIELD_NUMBER: _ClassVar[int]
    MONGODB_RECOVER_JOB_PARAMS_FIELD_NUMBER: _ClassVar[int]
    COUCHBASE_RECOVER_JOB_PARAMS_FIELD_NUMBER: _ClassVar[int]
    HBASE_RECOVER_JOB_PARAMS_FIELD_NUMBER: _ClassVar[int]
    HDFS_RECOVER_JOB_PARAMS_FIELD_NUMBER: _ClassVar[int]
    HIVE_RECOVER_JOB_PARAMS_FIELD_NUMBER: _ClassVar[int]
    MIRROR_JOB_PARAMS_FIELD_NUMBER: _ClassVar[int]
    CONTINUE_RESTORE_ON_ERROR_FIELD_NUMBER: _ClassVar[int]
    concurrency: int
    bandwidth_bytes_per_second: int
    overwrite: bool
    cassandra_recover_job_params: CassandraRecoverJobParams
    mongodb_recover_job_params: MongoDBRecoverJobParams
    couchbase_recover_job_params: CouchbaseRecoverJobParams
    hbase_recover_job_params: HBaseRecoverJobParams
    hdfs_recover_job_params: HdfsRecoverJobParams
    hive_recover_job_params: HiveRecoverJobParams
    mirror_job_params: NoSqlMirrorRecoveryJobParams
    continue_restore_on_error: bool
    def __init__(self, concurrency: _Optional[int] = ..., bandwidth_bytes_per_second: _Optional[int] = ..., overwrite: bool = ..., cassandra_recover_job_params: _Optional[_Union[CassandraRecoverJobParams, _Mapping]] = ..., mongodb_recover_job_params: _Optional[_Union[MongoDBRecoverJobParams, _Mapping]] = ..., couchbase_recover_job_params: _Optional[_Union[CouchbaseRecoverJobParams, _Mapping]] = ..., hbase_recover_job_params: _Optional[_Union[HBaseRecoverJobParams, _Mapping]] = ..., hdfs_recover_job_params: _Optional[_Union[HdfsRecoverJobParams, _Mapping]] = ..., hive_recover_job_params: _Optional[_Union[HiveRecoverJobParams, _Mapping]] = ..., mirror_job_params: _Optional[_Union[NoSqlMirrorRecoveryJobParams, _Mapping]] = ..., continue_restore_on_error: bool = ...) -> None: ...

class NoSqlRestoreObject(_message.Message):
    __slots__ = ("object_uuid", "rename", "object_restore_properties_map")
    class ObjectRestorePropertiesMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    OBJECT_UUID_FIELD_NUMBER: _ClassVar[int]
    RENAME_FIELD_NUMBER: _ClassVar[int]
    OBJECT_RESTORE_PROPERTIES_MAP_FIELD_NUMBER: _ClassVar[int]
    object_uuid: str
    rename: str
    object_restore_properties_map: _containers.ScalarMap[str, str]
    def __init__(self, object_uuid: _Optional[str] = ..., rename: _Optional[str] = ..., object_restore_properties_map: _Optional[_Mapping[str, str]] = ...) -> None: ...

class BackupJobGCParams(_message.Message):
    __slots__ = ("backup_job_id", "gc_retention_period_days")
    BACKUP_JOB_ID_FIELD_NUMBER: _ClassVar[int]
    GC_RETENTION_PERIOD_DAYS_FIELD_NUMBER: _ClassVar[int]
    backup_job_id: int
    gc_retention_period_days: int
    def __init__(self, backup_job_id: _Optional[int] = ..., gc_retention_period_days: _Optional[int] = ...) -> None: ...

class NoSqlStats(_message.Message):
    __slots__ = ("cassandra_stats", "couchbase_stats", "hdfs_stats", "hbase_stats", "hive_stats", "mongodb_stats", "bytes_transferred", "bytes_protected", "num_protected_entities")
    CASSANDRA_STATS_FIELD_NUMBER: _ClassVar[int]
    COUCHBASE_STATS_FIELD_NUMBER: _ClassVar[int]
    HDFS_STATS_FIELD_NUMBER: _ClassVar[int]
    HBASE_STATS_FIELD_NUMBER: _ClassVar[int]
    HIVE_STATS_FIELD_NUMBER: _ClassVar[int]
    MONGODB_STATS_FIELD_NUMBER: _ClassVar[int]
    BYTES_TRANSFERRED_FIELD_NUMBER: _ClassVar[int]
    BYTES_PROTECTED_FIELD_NUMBER: _ClassVar[int]
    NUM_PROTECTED_ENTITIES_FIELD_NUMBER: _ClassVar[int]
    cassandra_stats: CassandraStats
    couchbase_stats: CouchbaseStats
    hdfs_stats: HdfsStats
    hbase_stats: HbaseStats
    hive_stats: HiveStats
    mongodb_stats: MongoDBStats
    bytes_transferred: int
    bytes_protected: int
    num_protected_entities: int
    def __init__(self, cassandra_stats: _Optional[_Union[CassandraStats, _Mapping]] = ..., couchbase_stats: _Optional[_Union[CouchbaseStats, _Mapping]] = ..., hdfs_stats: _Optional[_Union[HdfsStats, _Mapping]] = ..., hbase_stats: _Optional[_Union[HbaseStats, _Mapping]] = ..., hive_stats: _Optional[_Union[HiveStats, _Mapping]] = ..., mongodb_stats: _Optional[_Union[MongoDBStats, _Mapping]] = ..., bytes_transferred: _Optional[int] = ..., bytes_protected: _Optional[int] = ..., num_protected_entities: _Optional[int] = ...) -> None: ...

class PhysicalStats(_message.Message):
    __slots__ = ("files_created", "files_modified", "files_deleted", "files_protected")
    FILES_CREATED_FIELD_NUMBER: _ClassVar[int]
    FILES_MODIFIED_FIELD_NUMBER: _ClassVar[int]
    FILES_DELETED_FIELD_NUMBER: _ClassVar[int]
    FILES_PROTECTED_FIELD_NUMBER: _ClassVar[int]
    files_created: int
    files_modified: int
    files_deleted: int
    files_protected: int
    def __init__(self, files_created: _Optional[int] = ..., files_modified: _Optional[int] = ..., files_deleted: _Optional[int] = ..., files_protected: _Optional[int] = ...) -> None: ...

class CassandraStats(_message.Message):
    __slots__ = ("keyspaces_created", "keyspaces_modified", "keyspaces_deleted", "tables_created", "tables_modified", "tables_deleted", "keyspaces_protected", "tables_protected", "physical_stats")
    KEYSPACES_CREATED_FIELD_NUMBER: _ClassVar[int]
    KEYSPACES_MODIFIED_FIELD_NUMBER: _ClassVar[int]
    KEYSPACES_DELETED_FIELD_NUMBER: _ClassVar[int]
    TABLES_CREATED_FIELD_NUMBER: _ClassVar[int]
    TABLES_MODIFIED_FIELD_NUMBER: _ClassVar[int]
    TABLES_DELETED_FIELD_NUMBER: _ClassVar[int]
    KEYSPACES_PROTECTED_FIELD_NUMBER: _ClassVar[int]
    TABLES_PROTECTED_FIELD_NUMBER: _ClassVar[int]
    PHYSICAL_STATS_FIELD_NUMBER: _ClassVar[int]
    keyspaces_created: int
    keyspaces_modified: int
    keyspaces_deleted: int
    tables_created: int
    tables_modified: int
    tables_deleted: int
    keyspaces_protected: int
    tables_protected: int
    physical_stats: PhysicalStats
    def __init__(self, keyspaces_created: _Optional[int] = ..., keyspaces_modified: _Optional[int] = ..., keyspaces_deleted: _Optional[int] = ..., tables_created: _Optional[int] = ..., tables_modified: _Optional[int] = ..., tables_deleted: _Optional[int] = ..., keyspaces_protected: _Optional[int] = ..., tables_protected: _Optional[int] = ..., physical_stats: _Optional[_Union[PhysicalStats, _Mapping]] = ...) -> None: ...

class CouchbaseStats(_message.Message):
    __slots__ = ("buckets_created", "buckets_modified", "buckets_deleted", "buckets_protected")
    BUCKETS_CREATED_FIELD_NUMBER: _ClassVar[int]
    BUCKETS_MODIFIED_FIELD_NUMBER: _ClassVar[int]
    BUCKETS_DELETED_FIELD_NUMBER: _ClassVar[int]
    BUCKETS_PROTECTED_FIELD_NUMBER: _ClassVar[int]
    buckets_created: int
    buckets_modified: int
    buckets_deleted: int
    buckets_protected: int
    def __init__(self, buckets_created: _Optional[int] = ..., buckets_modified: _Optional[int] = ..., buckets_deleted: _Optional[int] = ..., buckets_protected: _Optional[int] = ...) -> None: ...

class HdfsStats(_message.Message):
    __slots__ = ("objects_created", "objects_appended", "objects_modified", "objects_deleted")
    OBJECTS_CREATED_FIELD_NUMBER: _ClassVar[int]
    OBJECTS_APPENDED_FIELD_NUMBER: _ClassVar[int]
    OBJECTS_MODIFIED_FIELD_NUMBER: _ClassVar[int]
    OBJECTS_DELETED_FIELD_NUMBER: _ClassVar[int]
    objects_created: int
    objects_appended: int
    objects_modified: int
    objects_deleted: int
    def __init__(self, objects_created: _Optional[int] = ..., objects_appended: _Optional[int] = ..., objects_modified: _Optional[int] = ..., objects_deleted: _Optional[int] = ...) -> None: ...

class HbaseStats(_message.Message):
    __slots__ = ("namespaces_created", "namespaces_modified", "namespaces_deleted", "tables_created", "tables_modified", "tables_deleted", "namespaces_protected", "tables_protected", "physical_stats")
    NAMESPACES_CREATED_FIELD_NUMBER: _ClassVar[int]
    NAMESPACES_MODIFIED_FIELD_NUMBER: _ClassVar[int]
    NAMESPACES_DELETED_FIELD_NUMBER: _ClassVar[int]
    TABLES_CREATED_FIELD_NUMBER: _ClassVar[int]
    TABLES_MODIFIED_FIELD_NUMBER: _ClassVar[int]
    TABLES_DELETED_FIELD_NUMBER: _ClassVar[int]
    NAMESPACES_PROTECTED_FIELD_NUMBER: _ClassVar[int]
    TABLES_PROTECTED_FIELD_NUMBER: _ClassVar[int]
    PHYSICAL_STATS_FIELD_NUMBER: _ClassVar[int]
    namespaces_created: int
    namespaces_modified: int
    namespaces_deleted: int
    tables_created: int
    tables_modified: int
    tables_deleted: int
    namespaces_protected: int
    tables_protected: int
    physical_stats: PhysicalStats
    def __init__(self, namespaces_created: _Optional[int] = ..., namespaces_modified: _Optional[int] = ..., namespaces_deleted: _Optional[int] = ..., tables_created: _Optional[int] = ..., tables_modified: _Optional[int] = ..., tables_deleted: _Optional[int] = ..., namespaces_protected: _Optional[int] = ..., tables_protected: _Optional[int] = ..., physical_stats: _Optional[_Union[PhysicalStats, _Mapping]] = ...) -> None: ...

class HiveStats(_message.Message):
    __slots__ = ("databases_created", "databases_modified", "databases_deleted", "tables_created", "tables_modified", "tables_deleted", "partitions_created", "partitions_modified", "partitions_deleted", "databases_protected", "tables_protected", "partitions_protected", "physical_stats")
    DATABASES_CREATED_FIELD_NUMBER: _ClassVar[int]
    DATABASES_MODIFIED_FIELD_NUMBER: _ClassVar[int]
    DATABASES_DELETED_FIELD_NUMBER: _ClassVar[int]
    TABLES_CREATED_FIELD_NUMBER: _ClassVar[int]
    TABLES_MODIFIED_FIELD_NUMBER: _ClassVar[int]
    TABLES_DELETED_FIELD_NUMBER: _ClassVar[int]
    PARTITIONS_CREATED_FIELD_NUMBER: _ClassVar[int]
    PARTITIONS_MODIFIED_FIELD_NUMBER: _ClassVar[int]
    PARTITIONS_DELETED_FIELD_NUMBER: _ClassVar[int]
    DATABASES_PROTECTED_FIELD_NUMBER: _ClassVar[int]
    TABLES_PROTECTED_FIELD_NUMBER: _ClassVar[int]
    PARTITIONS_PROTECTED_FIELD_NUMBER: _ClassVar[int]
    PHYSICAL_STATS_FIELD_NUMBER: _ClassVar[int]
    databases_created: int
    databases_modified: int
    databases_deleted: int
    tables_created: int
    tables_modified: int
    tables_deleted: int
    partitions_created: int
    partitions_modified: int
    partitions_deleted: int
    databases_protected: int
    tables_protected: int
    partitions_protected: int
    physical_stats: PhysicalStats
    def __init__(self, databases_created: _Optional[int] = ..., databases_modified: _Optional[int] = ..., databases_deleted: _Optional[int] = ..., tables_created: _Optional[int] = ..., tables_modified: _Optional[int] = ..., tables_deleted: _Optional[int] = ..., partitions_created: _Optional[int] = ..., partitions_modified: _Optional[int] = ..., partitions_deleted: _Optional[int] = ..., databases_protected: _Optional[int] = ..., tables_protected: _Optional[int] = ..., partitions_protected: _Optional[int] = ..., physical_stats: _Optional[_Union[PhysicalStats, _Mapping]] = ...) -> None: ...

class MongoDBStats(_message.Message):
    __slots__ = ("databases_created", "databases_modified", "databases_deleted", "collections_created", "collections_modified", "collections_deleted", "databases_protected", "collections_protected")
    DATABASES_CREATED_FIELD_NUMBER: _ClassVar[int]
    DATABASES_MODIFIED_FIELD_NUMBER: _ClassVar[int]
    DATABASES_DELETED_FIELD_NUMBER: _ClassVar[int]
    COLLECTIONS_CREATED_FIELD_NUMBER: _ClassVar[int]
    COLLECTIONS_MODIFIED_FIELD_NUMBER: _ClassVar[int]
    COLLECTIONS_DELETED_FIELD_NUMBER: _ClassVar[int]
    DATABASES_PROTECTED_FIELD_NUMBER: _ClassVar[int]
    COLLECTIONS_PROTECTED_FIELD_NUMBER: _ClassVar[int]
    databases_created: int
    databases_modified: int
    databases_deleted: int
    collections_created: int
    collections_modified: int
    collections_deleted: int
    databases_protected: int
    collections_protected: int
    def __init__(self, databases_created: _Optional[int] = ..., databases_modified: _Optional[int] = ..., databases_deleted: _Optional[int] = ..., collections_created: _Optional[int] = ..., collections_modified: _Optional[int] = ..., collections_deleted: _Optional[int] = ..., databases_protected: _Optional[int] = ..., collections_protected: _Optional[int] = ...) -> None: ...

class NoSqlLogData(_message.Message):
    __slots__ = ("log_file_name", "start_seq_number", "end_seq_number", "log_rollover", "contains_change_event")
    LOG_FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    START_SEQ_NUMBER_FIELD_NUMBER: _ClassVar[int]
    END_SEQ_NUMBER_FIELD_NUMBER: _ClassVar[int]
    LOG_ROLLOVER_FIELD_NUMBER: _ClassVar[int]
    CONTAINS_CHANGE_EVENT_FIELD_NUMBER: _ClassVar[int]
    log_file_name: str
    start_seq_number: _event_pb2.Sequencer
    end_seq_number: _event_pb2.Sequencer
    log_rollover: bool
    contains_change_event: bool
    def __init__(self, log_file_name: _Optional[str] = ..., start_seq_number: _Optional[_Union[_event_pb2.Sequencer, _Mapping]] = ..., end_seq_number: _Optional[_Union[_event_pb2.Sequencer, _Mapping]] = ..., log_rollover: bool = ..., contains_change_event: bool = ...) -> None: ...

class NosqlAdditionalStateProto(_message.Message):
    __slots__ = ("previous_protected_entity_ids_vec",)
    PREVIOUS_PROTECTED_ENTITY_IDS_VEC_FIELD_NUMBER: _ClassVar[int]
    previous_protected_entity_ids_vec: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, previous_protected_entity_ids_vec: _Optional[_Iterable[int]] = ...) -> None: ...
