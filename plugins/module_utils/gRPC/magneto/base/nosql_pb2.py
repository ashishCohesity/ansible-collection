# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: magneto/base/nosql.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from atom.base import event_pb2 as atom_dot_base_dot_event__pb2
from magneto.base import entity_pb2 as magneto_dot_base_dot_entity__pb2
from magneto.base import credentials_pb2 as magneto_dot_base_dot_credentials__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18magneto/base/nosql.proto\x12\x10\x63ohesity.magneto\x1a\x15\x61tom/base/event.proto\x1a\x19magneto/base/entity.proto\x1a\x1emagneto/base/credentials.proto\"7\n\x0b\x44SESolrInfo\x12\x15\n\rsolr_node_vec\x18\x01 \x03(\t\x12\x11\n\tsolr_port\x18\x02 \x01(\r\"\x86\x01\n\x11\x43\x61ssandraPortInfo\x12\x1d\n\x15native_transport_port\x18\x01 \x01(\r\x12\x10\n\x08rpc_port\x18\x02 \x01(\r\x12\x14\n\x0cstorage_port\x18\x03 \x01(\r\x12\x18\n\x10ssl_storage_port\x18\x04 \x01(\r\x12\x10\n\x08jmx_port\x18\x05 \x01(\r\"\xc9\x03\n\x15\x43\x61ssandraSecurityInfo\x12\x1c\n\x14\x63\x61ssandra_authorizer\x18\x01 \x01(\t\x12\x1f\n\x17\x63\x61ssandra_auth_required\x18\x02 \x01(\x08\x12V\n\x13\x63\x61ssandra_auth_type\x18\x03 \x01(\x0e\x32\x39.cohesity.magneto.CassandraSecurityInfo.CassandraAuthType\x12!\n\x19\x64se_authorization_enabled\x18\x04 \x01(\x08\x12+\n#cassandra_client_encryption_enabled\x18\x05 \x01(\x08\x12\x33\n+cassandra_server_encryption_req_client_auth\x18\x07 \x01(\x08\x12\x32\n*cassandra_server_internode_encryption_type\x18\x08 \x01(\t\x12\x1f\n\x17\x63\x61ssandra_authenticator\x18\t \x01(\t\"9\n\x11\x43\x61ssandraAuthType\x12\x0c\n\x08PASSWORD\x10\x01\x12\x0c\n\x08KERBEROS\x10\x02\x12\x08\n\x04LDAP\x10\x03J\x04\x08\x06\x10\x07\"\xe3\x02\n\x18\x43\x61ssandraDiscoveryParams\x12\x14\n\x0cprimary_host\x18\x01 \x01(\t\x12\"\n\x1a\x63\x61ssandra_config_directory\x18\x02 \x01(\t\x12\x1d\n\x15is_dse_tiered_storage\x18\x03 \x01(\x08\x12\x1c\n\x14is_dse_authenticator\x18\x04 \x01(\x08\x12\x1c\n\x14\x64se_config_directory\x18\x05 \x01(\t\x12\x36\n\x0fssh_credentials\x18\x06 \x01(\x0b\x32\x1d.cohesity.magneto.Credentials\x12\'\n\x1fis_cassandra_connection_allowed\x18\x07 \x01(\x08\x12\"\n\x1ais_graph_discovery_enabled\x18\x08 \x01(\x08\x12-\n\x1eis_system_ks_discovery_enabled\x18\t \x01(\x08:\x05\x66\x61lse\"\xe6\x03\n\x16\x43\x61ssandraConnectParams\x12N\n\x1a\x63\x61ssandra_discovery_params\x18\x01 \x01(\x0b\x32*.cohesity.magneto.CassandraDiscoveryParams\x12\x10\n\x08seed_vec\x18\x02 \x03(\t\x12%\n\x1dis_cassandra_jmx_auth_enabled\x18\x03 \x01(\x08\x12\x41\n\x14\x63\x61ssandra_ports_info\x18\x04 \x01(\x0b\x32#.cohesity.magneto.CassandraPortInfo\x12H\n\x17\x63\x61ssandra_security_info\x18\x05 \x01(\x0b\x32\'.cohesity.magneto.CassandraSecurityInfo\x12<\n\x15\x63\x61ssandra_credentials\x18\x06 \x01(\x0b\x32\x1d.cohesity.magneto.Credentials\x12\x36\n\x0fjmx_credentials\x18\x07 \x01(\x0b\x32\x1d.cohesity.magneto.Credentials\x12\x1e\n\x16kerberos_sasl_protocol\x18\x08 \x01(\t\x12\x1a\n\x12kerberos_principal\x18\n \x01(\tJ\x04\x08\t\x10\n\"h\n!NodeToTieredStorageDirectoriesMap\x12\x1b\n\x13\x63\x61ssandra_node_name\x18\x01 \x01(\t\x12&\n\x1etiered_storage_directories_vec\x18\x02 \x03(\t\"\xd7\x02\n\x19\x43\x61ssandraAdditionalParams\x12\x17\n\x0f\x64\x61ta_center_vec\x18\x01 \x03(\t\x12\x1d\n\x15\x63\x61ssandra_partitioner\x18\x02 \x01(\t\x12\x19\n\x11\x63\x61ssandra_version\x18\x03 \x01(\t\x12\x13\n\x0b\x64se_version\x18\x04 \x01(\t\x12\"\n\x1a\x63\x61ssandra_classpath_suffix\x18\x05 \x01(\t\x12\x34\n\rdse_solr_info\x18\x06 \x01(\x0b\x32\x1d.cohesity.magneto.DSESolrInfo\x12T\n\x17tiered_storage_dirs_map\x18\x07 \x03(\x0b\x32\x33.cohesity.magneto.NodeToTieredStorageDirectoriesMap\x12\"\n\x1a\x63ommit_log_backup_location\x18\x08 \x01(\t\"\xa0\x02\n\x14MongoDBConnectParams\x12\r\n\x05seeds\x18\x01 \x03(\t\x12$\n\x1c\x61uthenticating_database_name\x18\x03 \x01(\t\x12\x14\n\x0crequires_ssl\x18\x04 \x01(\x08\x12I\n\tauth_type\x18\x05 \x01(\x0e\x32\x36.cohesity.magneto.MongoDBConnectParams.MongoDBAuthType\x12\x32\n\x0b\x63redentials\x18\x06 \x01(\x0b\x32\x1d.cohesity.magneto.Credentials\">\n\x0fMongoDBAuthType\x12\t\n\x05SCRAM\x10\x01\x12\x08\n\x04LDAP\x10\x02\x12\x08\n\x04NONE\x10\x03\x12\x0c\n\x08KERBEROS\x10\x04\"W\n\x17MongoDBAdditionalParams\x12 \n\x18use_secondary_for_backup\x18\x01 \x01(\x08\x12\x1a\n\x12secondary_node_tag\x18\x02 \x03(\t\"\xa8\x01\n\x16\x43ouchbaseConnectParams\x12\r\n\x05seeds\x18\x01 \x03(\t\x12\x14\n\x0crequires_ssl\x18\x02 \x01(\x08\x12\x18\n\x10http_direct_port\x18\x03 \x01(\x05\x12\x1b\n\x13\x63\x61rrier_direct_port\x18\x04 \x01(\x05\x12\x32\n\x0b\x63redentials\x18\x05 \x01(\x0b\x32\x1d.cohesity.magneto.Credentials\"|\n\x14HBaseDiscoveryParams\x12\x0c\n\x04host\x18\x01 \x01(\t\x12\x1e\n\x16hbase_config_directory\x18\x02 \x01(\t\x12\x36\n\x0fssh_credentials\x18\x03 \x01(\x0b\x32\x1d.cohesity.magneto.Credentials\"\x84\x03\n\x12HBaseConnectParams\x12\x16\n\x0ehdfs_entity_id\x18\x01 \x01(\x03\x12\x1e\n\x16hbase_zookeeper_quorum\x18\x02 \x03(\t\x12!\n\x19hbase_root_data_directory\x18\x03 \x01(\t\x12N\n\rconfiguration\x18\x04 \x03(\x0b\x32\x37.cohesity.magneto.HBaseConnectParams.ConfigurationEntry\x12\x17\n\x0fhbase_principal\x18\x05 \x01(\t\x12K\n\x0fhbase_auth_type\x18\x06 \x01(\x0e\x32\x32.cohesity.magneto.HBaseConnectParams.HbaseAuthType\x1a\x34\n\x12\x43onfigurationEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\'\n\rHbaseAuthType\x12\x0c\n\x08KERBEROS\x10\x01\x12\x08\n\x04NONE\x10\x02\"z\n\x13HdfsDiscoveryParams\x12\x0c\n\x04host\x18\x01 \x01(\t\x12\x1d\n\x15hdfs_config_directory\x18\x02 \x01(\t\x12\x36\n\x0fssh_credentials\x18\x03 \x01(\x0b\x32\x1d.cohesity.magneto.Credentials\"\xd7\x03\n\x11HdfsConnectParams\x12\x10\n\x08namenode\x18\x01 \x01(\t\x12\x0c\n\x04port\x18\x02 \x01(\x05\x12M\n\rconfiguration\x18\x03 \x03(\x0b\x32\x36.cohesity.magneto.HdfsConnectParams.ConfigurationEntry\x12S\n\x13hadoop_distribution\x18\x04 \x01(\x0e\x32\x36.cohesity.magneto.HdfsConnectParams.HadoopDistribution\x12\x16\n\x0ehadoop_version\x18\x05 \x01(\t\x12\x16\n\x0ehdfs_principal\x18\x06 \x01(\t\x12H\n\x0ehdfs_auth_type\x18\x07 \x01(\x0e\x32\x30.cohesity.magneto.HdfsConnectParams.HdfsAuthType\x1a\x34\n\x12\x43onfigurationEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"&\n\x12HadoopDistribution\x12\x07\n\x03\x43\x44H\x10\x01\x12\x07\n\x03HDP\x10\x02\"&\n\x0cHdfsAuthType\x12\x0c\n\x08KERBEROS\x10\x01\x12\x08\n\x04NONE\x10\x02\"z\n\x13HiveDiscoveryParams\x12\x0c\n\x04host\x18\x01 \x01(\t\x12\x1d\n\x15hive_config_directory\x18\x02 \x01(\t\x12\x36\n\x0fssh_credentials\x18\x03 \x01(\x0b\x32\x1d.cohesity.magneto.Credentials\"\xe2\x02\n\x11HiveConnectParams\x12\x16\n\x0ehdfs_entity_id\x18\x01 \x01(\x03\x12\x11\n\tmetastore\x18\x02 \x01(\t\x12\x13\n\x0bthrift_port\x18\x03 \x01(\x05\x12M\n\rconfiguration\x18\x04 \x03(\x0b\x32\x36.cohesity.magneto.HiveConnectParams.ConfigurationEntry\x12\x16\n\x0ehive_principal\x18\x05 \x01(\t\x12H\n\x0ehive_auth_type\x18\x06 \x01(\x0e\x32\x30.cohesity.magneto.HiveConnectParams.HiveAuthType\x1a\x34\n\x12\x43onfigurationEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"&\n\x0cHiveAuthType\x12\x0c\n\x08KERBEROS\x10\x01\x12\x08\n\x04NONE\x10\x02\"\xaf\x03\n\x18\x43\x61ssandraBackupJobParams\x12N\n\x19\x63\x61ssandra_additional_info\x18\x01 \x01(\x0b\x32+.cohesity.magneto.CassandraAdditionalParams\x12 \n\x18selected_data_center_vec\x18\x02 \x03(\t\x12\x1e\n\x16graph_handling_enabled\x18\x03 \x01(\x08\x12%\n\x16is_only_log_backup_job\x18\x04 \x01(\x08:\x05\x66\x61lse\x12 \n\x18retention_period_in_secs\x18\x05 \x01(\x03\x12\x1b\n\x13roles_gflag_enabled\x18\x06 \x01(\x08\x12\"\n\x13is_system_ks_backup\x18\x07 \x01(\x08:\x05\x66\x61lse\x12&\n\x17make_primary_log_backup\x18\x08 \x01(\x08:\x05\x66\x61lse\x12*\n\x1eprevious_job_end_time_in_usecs\x18\t \x01(\x03:\x02-1\x12#\n\x17job_start_time_in_usecs\x18\n \x01(\x03:\x02-1\"d\n\x16MongoDBBackupJobParams\x12J\n\x17mongodb_additional_info\x18\x01 \x01(\x0b\x32).cohesity.magneto.MongoDBAdditionalParams\"\x1a\n\x18\x43ouchbaseBackupJobParams\"X\n\x14HBaseBackupJobParams\x12@\n\x13hdfs_connect_params\x18\x01 \x01(\x0b\x32#.cohesity.magneto.HdfsConnectParams\"Q\n\x13HdfsBackupJobParams\x12\x1c\n\x14hdfs_protect_pattern\x18\x01 \x03(\t\x12\x1c\n\x14hdfs_exclude_pattern\x18\x02 \x03(\t\"W\n\x13HiveBackupJobParams\x12@\n\x13hdfs_connect_params\x18\x01 \x01(\x0b\x32#.cohesity.magneto.HdfsConnectParams\"\xac\x07\n\x14NoSqlBackupJobParams\x12\x13\n\x0b\x63oncurrency\x18\x01 \x01(\x05\x12\"\n\x1a\x62\x61ndwidth_bytes_per_second\x18\x02 \x01(\x03\x12$\n\x1c\x63ompaction_job_interval_secs\x18\x03 \x01(\x03\x12&\n\x1elast_compaction_run_time_usecs\x18\x04 \x01(\x03\x12\x1c\n\x14gc_job_interval_secs\x18\x05 \x01(\x03\x12\x1e\n\x16last_gc_run_time_usecs\x18\x06 \x01(\x03\x12 \n\x18gc_retention_period_days\x18\x07 \x01(\x05\x12O\n\x1b\x63\x61ssandra_backup_job_params\x18\x08 \x01(\x0b\x32*.cohesity.magneto.CassandraBackupJobParams\x12K\n\x19mongodb_backup_job_params\x18\t \x01(\x0b\x32(.cohesity.magneto.MongoDBBackupJobParams\x12O\n\x1b\x63ouchbase_backup_job_params\x18\n \x01(\x0b\x32*.cohesity.magneto.CouchbaseBackupJobParams\x12G\n\x17hbase_backup_job_params\x18\x0b \x01(\x0b\x32&.cohesity.magneto.HBaseBackupJobParams\x12\x45\n\x16hdfs_backup_job_params\x18\x0c \x01(\x0b\x32%.cohesity.magneto.HdfsBackupJobParams\x12\x45\n\x16hive_backup_job_params\x18\r \x01(\x0b\x32%.cohesity.magneto.HiveBackupJobParams\x12)\n!previous_protected_entity_ids_vec\x18\x0e \x03(\x03\x12`\n\x16immediate_ancestor_map\x18\x0f \x03(\x0b\x32@.cohesity.magneto.NoSqlBackupJobParams.ImmediateAncestorMapEntry\x1aZ\n\x19ImmediateAncestorMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\x03\x12,\n\x05value\x18\x02 \x01(\x0b\x32\x1d.cohesity.magneto.EntityProto:\x02\x38\x01\"\xff\x04\n\x19\x43\x61ssandraRecoverJobParams\x12\x0e\n\x06suffix\x18\x01 \x01(\t\x12N\n\x19\x63\x61ssandra_additional_info\x18\x02 \x01(\x0b\x32+.cohesity.magneto.CassandraAdditionalParams\x12 \n\x18selected_data_center_vec\x18\x03 \x03(\t\x12\x1d\n\x15staging_directory_vec\x18\x05 \x03(\t\x12\x1e\n\x16graph_handling_enabled\x18\x06 \x01(\x08\x12\x1d\n\x15log_restore_directory\x18\x07 \x01(\t\x12J\n\x12log_recover_params\x18\x08 \x01(\x0b\x32..cohesity.magneto.CassandraLogRecoverJobParams\x12\x17\n\x0frestart_allowed\x18\t \x01(\x08\x12\x1b\n\x13restart_immediately\x18\n \x01(\x08\x12\x14\n\x0crestart_time\x18\x0b \x01(\x03\x12\x17\n\x0frestart_command\x18\x0c \x01(\t\x12\x19\n\x11is_finalise_phase\x18\r \x01(\x08\x12 \n\x18\x66inalise_restore_task_id\x18\x0e \x01(\x03\x12\x1b\n\x13roles_gflag_enabled\x18\x0f \x01(\x08\x12%\n\x1drestore_roles_and_permissions\x18\x10 \x01(\x08\x12$\n\x15is_system_ks_recovery\x18\x11 \x01(\x08:\x05\x66\x61lse\x12$\n\x15is_live_table_restore\x18\x12 \x01(\x08:\x05\x66\x61lseJ\x04\x08\x04\x10\x05\"\xca\x01\n\x1c\x43\x61ssandraLogRecoverJobParams\x12 \n\x18log_backup_view_box_name\x18\x01 \x01(\t\x12\x1c\n\x14log_backup_view_name\x18\x02 \x01(\t\x12*\n\"start_time_for_log_replay_in_usecs\x18\x03 \x01(\x03\x12(\n end_time_for_log_replay_in_usecs\x18\x04 \x01(\x03\x12\x14\n\x0cobject_names\x18\x05 \x03(\t\")\n\x17MongoDBRecoverJobParams\x12\x0e\n\x06suffix\x18\x01 \x01(\t\"\xb8\x02\n\x19\x43ouchbaseRecoverJobParams\x12\x0e\n\x06suffix\x18\x01 \x01(\t\x12\x17\n\x0f\x61ppendDocuments\x18\x02 \x01(\x08\x12\x17\n\x0f\x64\x64lOnlyRecovery\x18\x03 \x01(\x08\x12\x16\n\x0eoverwriteUsers\x18\x04 \x01(\x08\x12^\n\x15\x64ocuments_filter_type\x18\x05 \x01(\x0e\x32?.cohesity.magneto.CouchbaseRecoverJobParams.DocumentsFilterType\x12\x10\n\x08id_regex\x18\x06 \x01(\t\x12\x19\n\x11\x66ilter_expression\x18\x07 \x01(\t\"4\n\x13\x44ocumentsFilterType\x12\x08\n\x04NONE\x10\x01\x12\x06\n\x02ID\x10\x02\x12\x0b\n\x07\x43ONTENT\x10\x03\"i\n\x15HBaseRecoverJobParams\x12\x0e\n\x06suffix\x18\x01 \x01(\t\x12@\n\x13hdfs_connect_params\x18\x02 \x01(\x0b\x32#.cohesity.magneto.HdfsConnectParams\"l\n\x14HdfsRecoverJobParams\x12\x18\n\x10target_directory\x18\x01 \x01(\t\x12\x1c\n\x14hdfs_recover_pattern\x18\x02 \x03(\t\x12\x1c\n\x14hdfs_exclude_pattern\x18\x03 \x03(\t\"h\n\x14HiveRecoverJobParams\x12\x0e\n\x06suffix\x18\x01 \x01(\t\x12@\n\x13hdfs_connect_params\x18\x02 \x01(\x0b\x32#.cohesity.magneto.HdfsConnectParams\"E\n\x1cNoSqlMirrorRecoveryJobParams\x12%\n\x1dmirror_restore_parent_task_id\x18\x01 \x01(\x03\"\xaa\x05\n\x15NoSqlRecoverJobParams\x12\x13\n\x0b\x63oncurrency\x18\x01 \x01(\x05\x12\"\n\x1a\x62\x61ndwidth_bytes_per_second\x18\x02 \x01(\x03\x12\x11\n\toverwrite\x18\x03 \x01(\x08\x12Q\n\x1c\x63\x61ssandra_recover_job_params\x18\x04 \x01(\x0b\x32+.cohesity.magneto.CassandraRecoverJobParams\x12M\n\x1amongodb_recover_job_params\x18\x05 \x01(\x0b\x32).cohesity.magneto.MongoDBRecoverJobParams\x12Q\n\x1c\x63ouchbase_recover_job_params\x18\x06 \x01(\x0b\x32+.cohesity.magneto.CouchbaseRecoverJobParams\x12I\n\x18hbase_recover_job_params\x18\x07 \x01(\x0b\x32\'.cohesity.magneto.HBaseRecoverJobParams\x12G\n\x17hdfs_recover_job_params\x18\x08 \x01(\x0b\x32&.cohesity.magneto.HdfsRecoverJobParams\x12G\n\x17hive_recover_job_params\x18\t \x01(\x0b\x32&.cohesity.magneto.HiveRecoverJobParams\x12I\n\x11mirror_job_params\x18\n \x01(\x0b\x32..cohesity.magneto.NoSqlMirrorRecoveryJobParams\x12(\n\x19\x63ontinue_restore_on_error\x18\x0b \x01(\x08:\x05\x66\x61lse\"\xe9\x01\n\x12NoSqlRestoreObject\x12\x13\n\x0bobject_uuid\x18\x01 \x01(\t\x12\x0e\n\x06rename\x18\x02 \x01(\t\x12k\n\x1dobject_restore_properties_map\x18\x03 \x03(\x0b\x32\x44.cohesity.magneto.NoSqlRestoreObject.ObjectRestorePropertiesMapEntry\x1a\x41\n\x1fObjectRestorePropertiesMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"L\n\x11\x42\x61\x63kupJobGCParams\x12\x15\n\rbackup_job_id\x18\x01 \x01(\x03\x12 \n\x18gc_retention_period_days\x18\x02 \x01(\x05\"\xa2\x03\n\nNoSqlStats\x12\x39\n\x0f\x63\x61ssandra_stats\x18\x01 \x01(\x0b\x32 .cohesity.magneto.CassandraStats\x12\x39\n\x0f\x63ouchbase_stats\x18\x02 \x01(\x0b\x32 .cohesity.magneto.CouchbaseStats\x12/\n\nhdfs_stats\x18\x03 \x01(\x0b\x32\x1b.cohesity.magneto.HdfsStats\x12\x31\n\x0bhbase_stats\x18\x04 \x01(\x0b\x32\x1c.cohesity.magneto.HbaseStats\x12/\n\nhive_stats\x18\x05 \x01(\x0b\x32\x1b.cohesity.magneto.HiveStats\x12\x35\n\rmongodb_stats\x18\x06 \x01(\x0b\x32\x1e.cohesity.magneto.MongoDBStats\x12\x19\n\x11\x62ytes_transferred\x18\x07 \x01(\x03\x12\x17\n\x0f\x62ytes_protected\x18\x08 \x01(\x03\x12\x1e\n\x16num_protected_entities\x18\t \x01(\x03\"n\n\rPhysicalStats\x12\x15\n\rfiles_created\x18\x01 \x01(\x03\x12\x16\n\x0e\x66iles_modified\x18\x02 \x01(\x03\x12\x15\n\rfiles_deleted\x18\x03 \x01(\x03\x12\x17\n\x0f\x66iles_protected\x18\x04 \x01(\x03\"\x9b\x02\n\x0e\x43\x61ssandraStats\x12\x19\n\x11keyspaces_created\x18\x01 \x01(\x03\x12\x1a\n\x12keyspaces_modified\x18\x02 \x01(\x03\x12\x19\n\x11keyspaces_deleted\x18\x03 \x01(\x03\x12\x16\n\x0etables_created\x18\x04 \x01(\x03\x12\x17\n\x0ftables_modified\x18\x05 \x01(\x03\x12\x16\n\x0etables_deleted\x18\x06 \x01(\x03\x12\x1b\n\x13keyspaces_protected\x18\x07 \x01(\x03\x12\x18\n\x10tables_protected\x18\x08 \x01(\x03\x12\x37\n\x0ephysical_stats\x18\t \x01(\x0b\x32\x1f.cohesity.magneto.PhysicalStats\"w\n\x0e\x43ouchbaseStats\x12\x17\n\x0f\x62uckets_created\x18\x01 \x01(\x03\x12\x18\n\x10\x62uckets_modified\x18\x02 \x01(\x03\x12\x17\n\x0f\x62uckets_deleted\x18\x03 \x01(\x03\x12\x19\n\x11\x62uckets_protected\x18\x04 \x01(\x03\"q\n\tHdfsStats\x12\x17\n\x0fobjects_created\x18\x01 \x01(\x03\x12\x18\n\x10objects_appended\x18\x02 \x01(\x03\x12\x18\n\x10objects_modified\x18\x03 \x01(\x03\x12\x17\n\x0fobjects_deleted\x18\x04 \x01(\x03\"\x9b\x02\n\nHbaseStats\x12\x1a\n\x12namespaces_created\x18\x01 \x01(\x03\x12\x1b\n\x13namespaces_modified\x18\x02 \x01(\x03\x12\x1a\n\x12namespaces_deleted\x18\x03 \x01(\x03\x12\x16\n\x0etables_created\x18\x04 \x01(\x03\x12\x17\n\x0ftables_modified\x18\x05 \x01(\x03\x12\x16\n\x0etables_deleted\x18\x06 \x01(\x03\x12\x1c\n\x14namespaces_protected\x18\x07 \x01(\x03\x12\x18\n\x10tables_protected\x18\x08 \x01(\x03\x12\x37\n\x0ephysical_stats\x18\t \x01(\x0b\x32\x1f.cohesity.magneto.PhysicalStats\"\x89\x03\n\tHiveStats\x12\x19\n\x11\x64\x61tabases_created\x18\x01 \x01(\x03\x12\x1a\n\x12\x64\x61tabases_modified\x18\x02 \x01(\x03\x12\x19\n\x11\x64\x61tabases_deleted\x18\x03 \x01(\x03\x12\x16\n\x0etables_created\x18\x04 \x01(\x03\x12\x17\n\x0ftables_modified\x18\x05 \x01(\x03\x12\x16\n\x0etables_deleted\x18\x06 \x01(\x03\x12\x1a\n\x12partitions_created\x18\x07 \x01(\x03\x12\x1b\n\x13partitions_modified\x18\x08 \x01(\x03\x12\x1a\n\x12partitions_deleted\x18\t \x01(\x03\x12\x1b\n\x13\x64\x61tabases_protected\x18\n \x01(\x03\x12\x18\n\x10tables_protected\x18\x0b \x01(\x03\x12\x1c\n\x14partitions_protected\x18\x0c \x01(\x03\x12\x37\n\x0ephysical_stats\x18\r \x01(\x0b\x32\x1f.cohesity.magneto.PhysicalStats\"\xf4\x01\n\x0cMongoDBStats\x12\x19\n\x11\x64\x61tabases_created\x18\x01 \x01(\x03\x12\x1a\n\x12\x64\x61tabases_modified\x18\x02 \x01(\x03\x12\x19\n\x11\x64\x61tabases_deleted\x18\x03 \x01(\x03\x12\x1b\n\x13\x63ollections_created\x18\x04 \x01(\x03\x12\x1c\n\x14\x63ollections_modified\x18\x05 \x01(\x03\x12\x1b\n\x13\x63ollections_deleted\x18\x06 \x01(\x03\x12\x1b\n\x13\x64\x61tabases_protected\x18\x07 \x01(\x03\x12\x1d\n\x15\x63ollections_protected\x18\x08 \x01(\x03\"\xc7\x01\n\x0cNoSqlLogData\x12\x15\n\rlog_file_name\x18\x01 \x01(\t\x12\x32\n\x10start_seq_number\x18\x03 \x01(\x0b\x32\x18.cohesity.atom.Sequencer\x12\x30\n\x0e\x65nd_seq_number\x18\x04 \x01(\x0b\x32\x18.cohesity.atom.Sequencer\x12\x14\n\x0clog_rollover\x18\x05 \x01(\x08\x12$\n\x15\x63ontains_change_event\x18\x06 \x01(\x08:\x05\x66\x61lse\"F\n\x19NosqlAdditionalStateProto\x12)\n!previous_protected_entity_ids_vec\x18\x01 \x03(\x03')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'magneto.base.nosql_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_HBASECONNECTPARAMS_CONFIGURATIONENTRY']._loaded_options = None
  _globals['_HBASECONNECTPARAMS_CONFIGURATIONENTRY']._serialized_options = b'8\001'
  _globals['_HDFSCONNECTPARAMS_CONFIGURATIONENTRY']._loaded_options = None
  _globals['_HDFSCONNECTPARAMS_CONFIGURATIONENTRY']._serialized_options = b'8\001'
  _globals['_HIVECONNECTPARAMS_CONFIGURATIONENTRY']._loaded_options = None
  _globals['_HIVECONNECTPARAMS_CONFIGURATIONENTRY']._serialized_options = b'8\001'
  _globals['_NOSQLBACKUPJOBPARAMS_IMMEDIATEANCESTORMAPENTRY']._loaded_options = None
  _globals['_NOSQLBACKUPJOBPARAMS_IMMEDIATEANCESTORMAPENTRY']._serialized_options = b'8\001'
  _globals['_NOSQLRESTOREOBJECT_OBJECTRESTOREPROPERTIESMAPENTRY']._loaded_options = None
  _globals['_NOSQLRESTOREOBJECT_OBJECTRESTOREPROPERTIESMAPENTRY']._serialized_options = b'8\001'
  _globals['_DSESOLRINFO']._serialized_start=128
  _globals['_DSESOLRINFO']._serialized_end=183
  _globals['_CASSANDRAPORTINFO']._serialized_start=186
  _globals['_CASSANDRAPORTINFO']._serialized_end=320
  _globals['_CASSANDRASECURITYINFO']._serialized_start=323
  _globals['_CASSANDRASECURITYINFO']._serialized_end=780
  _globals['_CASSANDRASECURITYINFO_CASSANDRAAUTHTYPE']._serialized_start=717
  _globals['_CASSANDRASECURITYINFO_CASSANDRAAUTHTYPE']._serialized_end=774
  _globals['_CASSANDRADISCOVERYPARAMS']._serialized_start=783
  _globals['_CASSANDRADISCOVERYPARAMS']._serialized_end=1138
  _globals['_CASSANDRACONNECTPARAMS']._serialized_start=1141
  _globals['_CASSANDRACONNECTPARAMS']._serialized_end=1627
  _globals['_NODETOTIEREDSTORAGEDIRECTORIESMAP']._serialized_start=1629
  _globals['_NODETOTIEREDSTORAGEDIRECTORIESMAP']._serialized_end=1733
  _globals['_CASSANDRAADDITIONALPARAMS']._serialized_start=1736
  _globals['_CASSANDRAADDITIONALPARAMS']._serialized_end=2079
  _globals['_MONGODBCONNECTPARAMS']._serialized_start=2082
  _globals['_MONGODBCONNECTPARAMS']._serialized_end=2370
  _globals['_MONGODBCONNECTPARAMS_MONGODBAUTHTYPE']._serialized_start=2308
  _globals['_MONGODBCONNECTPARAMS_MONGODBAUTHTYPE']._serialized_end=2370
  _globals['_MONGODBADDITIONALPARAMS']._serialized_start=2372
  _globals['_MONGODBADDITIONALPARAMS']._serialized_end=2459
  _globals['_COUCHBASECONNECTPARAMS']._serialized_start=2462
  _globals['_COUCHBASECONNECTPARAMS']._serialized_end=2630
  _globals['_HBASEDISCOVERYPARAMS']._serialized_start=2632
  _globals['_HBASEDISCOVERYPARAMS']._serialized_end=2756
  _globals['_HBASECONNECTPARAMS']._serialized_start=2759
  _globals['_HBASECONNECTPARAMS']._serialized_end=3147
  _globals['_HBASECONNECTPARAMS_CONFIGURATIONENTRY']._serialized_start=3054
  _globals['_HBASECONNECTPARAMS_CONFIGURATIONENTRY']._serialized_end=3106
  _globals['_HBASECONNECTPARAMS_HBASEAUTHTYPE']._serialized_start=3108
  _globals['_HBASECONNECTPARAMS_HBASEAUTHTYPE']._serialized_end=3147
  _globals['_HDFSDISCOVERYPARAMS']._serialized_start=3149
  _globals['_HDFSDISCOVERYPARAMS']._serialized_end=3271
  _globals['_HDFSCONNECTPARAMS']._serialized_start=3274
  _globals['_HDFSCONNECTPARAMS']._serialized_end=3745
  _globals['_HDFSCONNECTPARAMS_CONFIGURATIONENTRY']._serialized_start=3054
  _globals['_HDFSCONNECTPARAMS_CONFIGURATIONENTRY']._serialized_end=3106
  _globals['_HDFSCONNECTPARAMS_HADOOPDISTRIBUTION']._serialized_start=3667
  _globals['_HDFSCONNECTPARAMS_HADOOPDISTRIBUTION']._serialized_end=3705
  _globals['_HDFSCONNECTPARAMS_HDFSAUTHTYPE']._serialized_start=3707
  _globals['_HDFSCONNECTPARAMS_HDFSAUTHTYPE']._serialized_end=3745
  _globals['_HIVEDISCOVERYPARAMS']._serialized_start=3747
  _globals['_HIVEDISCOVERYPARAMS']._serialized_end=3869
  _globals['_HIVECONNECTPARAMS']._serialized_start=3872
  _globals['_HIVECONNECTPARAMS']._serialized_end=4226
  _globals['_HIVECONNECTPARAMS_CONFIGURATIONENTRY']._serialized_start=3054
  _globals['_HIVECONNECTPARAMS_CONFIGURATIONENTRY']._serialized_end=3106
  _globals['_HIVECONNECTPARAMS_HIVEAUTHTYPE']._serialized_start=4188
  _globals['_HIVECONNECTPARAMS_HIVEAUTHTYPE']._serialized_end=4226
  _globals['_CASSANDRABACKUPJOBPARAMS']._serialized_start=4229
  _globals['_CASSANDRABACKUPJOBPARAMS']._serialized_end=4660
  _globals['_MONGODBBACKUPJOBPARAMS']._serialized_start=4662
  _globals['_MONGODBBACKUPJOBPARAMS']._serialized_end=4762
  _globals['_COUCHBASEBACKUPJOBPARAMS']._serialized_start=4764
  _globals['_COUCHBASEBACKUPJOBPARAMS']._serialized_end=4790
  _globals['_HBASEBACKUPJOBPARAMS']._serialized_start=4792
  _globals['_HBASEBACKUPJOBPARAMS']._serialized_end=4880
  _globals['_HDFSBACKUPJOBPARAMS']._serialized_start=4882
  _globals['_HDFSBACKUPJOBPARAMS']._serialized_end=4963
  _globals['_HIVEBACKUPJOBPARAMS']._serialized_start=4965
  _globals['_HIVEBACKUPJOBPARAMS']._serialized_end=5052
  _globals['_NOSQLBACKUPJOBPARAMS']._serialized_start=5055
  _globals['_NOSQLBACKUPJOBPARAMS']._serialized_end=5995
  _globals['_NOSQLBACKUPJOBPARAMS_IMMEDIATEANCESTORMAPENTRY']._serialized_start=5905
  _globals['_NOSQLBACKUPJOBPARAMS_IMMEDIATEANCESTORMAPENTRY']._serialized_end=5995
  _globals['_CASSANDRARECOVERJOBPARAMS']._serialized_start=5998
  _globals['_CASSANDRARECOVERJOBPARAMS']._serialized_end=6637
  _globals['_CASSANDRALOGRECOVERJOBPARAMS']._serialized_start=6640
  _globals['_CASSANDRALOGRECOVERJOBPARAMS']._serialized_end=6842
  _globals['_MONGODBRECOVERJOBPARAMS']._serialized_start=6844
  _globals['_MONGODBRECOVERJOBPARAMS']._serialized_end=6885
  _globals['_COUCHBASERECOVERJOBPARAMS']._serialized_start=6888
  _globals['_COUCHBASERECOVERJOBPARAMS']._serialized_end=7200
  _globals['_COUCHBASERECOVERJOBPARAMS_DOCUMENTSFILTERTYPE']._serialized_start=7148
  _globals['_COUCHBASERECOVERJOBPARAMS_DOCUMENTSFILTERTYPE']._serialized_end=7200
  _globals['_HBASERECOVERJOBPARAMS']._serialized_start=7202
  _globals['_HBASERECOVERJOBPARAMS']._serialized_end=7307
  _globals['_HDFSRECOVERJOBPARAMS']._serialized_start=7309
  _globals['_HDFSRECOVERJOBPARAMS']._serialized_end=7417
  _globals['_HIVERECOVERJOBPARAMS']._serialized_start=7419
  _globals['_HIVERECOVERJOBPARAMS']._serialized_end=7523
  _globals['_NOSQLMIRRORRECOVERYJOBPARAMS']._serialized_start=7525
  _globals['_NOSQLMIRRORRECOVERYJOBPARAMS']._serialized_end=7594
  _globals['_NOSQLRECOVERJOBPARAMS']._serialized_start=7597
  _globals['_NOSQLRECOVERJOBPARAMS']._serialized_end=8279
  _globals['_NOSQLRESTOREOBJECT']._serialized_start=8282
  _globals['_NOSQLRESTOREOBJECT']._serialized_end=8515
  _globals['_NOSQLRESTOREOBJECT_OBJECTRESTOREPROPERTIESMAPENTRY']._serialized_start=8450
  _globals['_NOSQLRESTOREOBJECT_OBJECTRESTOREPROPERTIESMAPENTRY']._serialized_end=8515
  _globals['_BACKUPJOBGCPARAMS']._serialized_start=8517
  _globals['_BACKUPJOBGCPARAMS']._serialized_end=8593
  _globals['_NOSQLSTATS']._serialized_start=8596
  _globals['_NOSQLSTATS']._serialized_end=9014
  _globals['_PHYSICALSTATS']._serialized_start=9016
  _globals['_PHYSICALSTATS']._serialized_end=9126
  _globals['_CASSANDRASTATS']._serialized_start=9129
  _globals['_CASSANDRASTATS']._serialized_end=9412
  _globals['_COUCHBASESTATS']._serialized_start=9414
  _globals['_COUCHBASESTATS']._serialized_end=9533
  _globals['_HDFSSTATS']._serialized_start=9535
  _globals['_HDFSSTATS']._serialized_end=9648
  _globals['_HBASESTATS']._serialized_start=9651
  _globals['_HBASESTATS']._serialized_end=9934
  _globals['_HIVESTATS']._serialized_start=9937
  _globals['_HIVESTATS']._serialized_end=10330
  _globals['_MONGODBSTATS']._serialized_start=10333
  _globals['_MONGODBSTATS']._serialized_end=10577
  _globals['_NOSQLLOGDATA']._serialized_start=10580
  _globals['_NOSQLLOGDATA']._serialized_end=10779
  _globals['_NOSQLADDITIONALSTATEPROTO']._serialized_start=10781
  _globals['_NOSQLADDITIONALSTATEPROTO']._serialized_end=10851
# @@protoc_insertion_point(module_scope)
