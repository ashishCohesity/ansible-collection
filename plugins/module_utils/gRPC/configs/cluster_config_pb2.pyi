from configs import cluster_network_pb2 as _cluster_network_pb2
from configs import node_config_pb2 as _node_config_pb2
from configs import node_network_pb2 as _node_network_pb2
from configs import support_service_config_pb2 as _support_service_config_pb2
from util.base import op_clock_pb2 as _op_clock_pb2
from util.base import universal_id_pb2 as _universal_id_pb2
from open_util.base import aes_encryptor_pb2 as _aes_encryptor_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ClusterConfigProto(_message.Message):
    __slots__ = ("cluster_id", "cluster_incarnation_id", "cluster_name", "deprecated_subnet", "internal_subnet", "client_subnet_whitelist", "storage_tier_vec", "scribe_storage_tier_vec", "sequential_io_preference_index", "sequential_storage_tier_vec", "random_storage_tier_vec", "tier_shuffle_threshold_pct", "min_tier_shuffle_util_pct", "disk_vec", "rack_vec", "chassis_vec", "node_vec", "cluster_partition_vec", "view_box_vec", "bulletin_board", "scribe_table_names", "ntp_server_vec", "ntp_settings", "bonding_mode", "smtp_server", "support_server", "support_server_v2", "support_server_v2_config", "apollo_storage_tier_index", "apollo_storage_tier_vec", "apollo_wal_storage_tier_index", "apollo_wal_storage_tier_vec", "yoda_storage_tier_vec", "hydra_storage_tier_vec", "hydra_downtier_storage_tier_vec", "librarian_storage_tier_vec", "groot_storage_tier_index", "groot_storage_tier_vec", "athena_storage_tier_vec", "athena_slower_storage_tier_vec", "eagle_agent_storage_tier_vec", "cloud_chunk_repo_storage_tier_vec", "alert_notification_email_list", "ipmi_config", "nfs_export_path_list", "halo_config", "eagle_config", "kms_server_vec", "obfuscate_cryptsoft_client_key", "internal_kms_gandalf_key", "encryption_key_rotation_period_secs", "cluster_level_encryption_enabled", "older_kms_id", "cluster_level_encryption_kms_id", "qos_principal_map", "qos_mapping_vec", "apollo_throttling_schedule", "remote_cluster_vec", "archival_domain_vec", "vault_vec", "qos_principal_workload_vec", "default_qos_principal_names", "initial_qos_principal_weights", "initial_qos_principal_names", "initial_qos_principal_workload_names", "deprecated_dns_server_vec", "domain_name_vec", "deprecated_gateway", "active_directory_config", "winbind_krb5_locator_plugin_enabled", "ldap_config", "is_documentation_local", "snmp_config", "newscribe_enabled", "mtu", "fips_mode_enabled", "eula_config", "license_state", "proxy_server_vec", "cluster_ssh_public_key", "authorized_ssh_public_key_vec", "disable_ssh_password_authentication", "icebox_properties", "fault_tolerance", "metadata_fault_tolerance_factor", "topic_to_metadata_map", "consumer_group_ids", "filer_audit_logging_config", "cluster_audit_logging_config", "tiering_audit_logging_config", "timezone", "remote_log_servers_info", "topic_to_remote_log_servers_map", "language_locale", "zone_vec", "cluster_network_vec", "data_journal_compression_level", "deprecated_static_route_vec", "turbo_mode", "authentication_type", "aws_proxy_info_vec", "multi_tenancy_enabled", "tenant_viewbox_sharing_enabled", "tenant_deletion_info_vec", "yoda_cfiledb_use_librarian", "yoda_cfileindex_librarian_migration_status", "mcm_config", "firewall_profile_vec", "cluster_subnet_vec", "athena_config", "antivirus_config", "license_server_claimed", "idp_configuration", "stig_mode_enabled", "interface_group_vec", "tls_cert_config", "next_chunk_repo_wal_incarnation", "domain_sid", "google_analytics_enabled", "local_auth_domain_name", "metadata_info", "helios_views", "banner_enabled", "local_groups_enabled", "virbr0_ip", "keystone_config_vec", "swift_config_vec", "proxy_vm_ip", "license_start_time", "is_manual_license", "feature_flags", "ip_preference", "disabled_cipher_list", "object_store_disabled_cipher_list", "magneto_adapter_status", "nis_config", "client_netgroup_whitelist", "node_ip_adding_in_progress", "migratable_disk_vec", "support_user", "cloud_bandwidth_limits", "cluster_size", "smb_multichannel_enabled", "rigel_config", "rigel_config_vec", "route_rigel_snap_fs_traffic_through_broker", "cloud_dataplane_info", "banner", "alert_audit_logging_config", "dataprotection_audit_logging_config", "use_heimdall", "deprecated_node_group_vec", "network_config", "amqp_target_config", "ntp_server_auth_keys_vec", "kerberos_config", "flash_blade_registration_vec", "enable_patches_download", "internal_bifrost_enabled", "security_config", "description", "test_mode", "fleet_instance_ip_vec", "security_mode_enabled", "node_access", "is_any_active_bifrost_tenant", "root_certifying_authority", "allow_cluster_destroy_on_api_request", "bridge_enable_secure_view_access", "is_gandalf_secure_mode", "is_dmaas", "root_user", "ui_config", "active_cluster_ca_cert_id", "target_cluster_ca_cert_id", "current_ca_id_value", "certifying_authority_to_id_map", "is_cluster_mfa_enabled", "mfa_methods", "nfs_portal_honor_protocol_access_for_cluster_ips", "nfs_portal_honor_kdisabled_for_cluster_ips", "nfs_portal_honor_external_views_access_for_cluster_ips", "nfs_portal_disable_protocol_access_check", "smb_portal_disable_protocol_access_check", "enforce_nfs_access_checks_for_s3_views_for_cluster_ips", "helios_onprem_config", "is_internode_protorpc_encryption_enabled", "hardware_encryption_enabled", "disaggregated_metadata_disk_enabled", "disaggregated_storage_fencing_enabled", "max_chunk_file_id_to_check_for_bloat", "es_use_system_services", "yoda_es_migration_to_opensearch_status", "yoda_es_migration_status", "yoda_pxg_es_data_migration_status", "s3_portal_honor_object_store_access_enable_flag", "iris_api_backup_data_acl", "updated_realm_info_connector_params_pre_68", "split_key_enabled", "operation_state_map", "cluster_aes_encryption_mode_deprecated", "cluster_ssh_encrypted_priv_key", "cluster_active_ssh_private_key_md5sum", "cluster_target_ssh_private_key_md5sum", "last_rotated_ssh_key_timestamp", "cluster_target_enc_ssh_priv_key", "cluster_target_ssh_public_key", "apollo_binary_logging_config", "expose_tracking_view", "list_tracking_view_ui", "airgap_config", "ssh_config", "service_identity", "last_scribe_exclusive_disk_switch_usecs", "cluster_aes_encryption", "abac_config", "virtual_hosting_domain_vec", "cohesion_config", "cluster_snapshot_policy", "patch_download_in_progress", "use_default_agent_ports", "attempt_agent_ports_upgrade")
    class ProtocolAccessLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kDisabled: _ClassVar[ClusterConfigProto.ProtocolAccessLevel]
        kReadOnly: _ClassVar[ClusterConfigProto.ProtocolAccessLevel]
        kReadWrite: _ClassVar[ClusterConfigProto.ProtocolAccessLevel]
    kDisabled: ClusterConfigProto.ProtocolAccessLevel
    kReadOnly: ClusterConfigProto.ProtocolAccessLevel
    kReadWrite: ClusterConfigProto.ProtocolAccessLevel
    class IpAddressFamily(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        Unknown: _ClassVar[ClusterConfigProto.IpAddressFamily]
        IPv4: _ClassVar[ClusterConfigProto.IpAddressFamily]
        IPv6: _ClassVar[ClusterConfigProto.IpAddressFamily]
    Unknown: ClusterConfigProto.IpAddressFamily
    IPv4: ClusterConfigProto.IpAddressFamily
    IPv6: ClusterConfigProto.IpAddressFamily
    class EncryptionLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kEncryptionNone: _ClassVar[ClusterConfigProto.EncryptionLevel]
        kEncryptionWeak: _ClassVar[ClusterConfigProto.EncryptionLevel]
        kEncryptionStrong: _ClassVar[ClusterConfigProto.EncryptionLevel]
    kEncryptionNone: ClusterConfigProto.EncryptionLevel
    kEncryptionWeak: ClusterConfigProto.EncryptionLevel
    kEncryptionStrong: ClusterConfigProto.EncryptionLevel
    class InterfaceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kInterfaceTypePhysical: _ClassVar[ClusterConfigProto.InterfaceType]
        kInterfaceTypeBond: _ClassVar[ClusterConfigProto.InterfaceType]
        kInterfaceTypeVlan: _ClassVar[ClusterConfigProto.InterfaceType]
        kInterfaceTypeIpmi: _ClassVar[ClusterConfigProto.InterfaceType]
        kInterfaceTypeBridge: _ClassVar[ClusterConfigProto.InterfaceType]
    kInterfaceTypePhysical: ClusterConfigProto.InterfaceType
    kInterfaceTypeBond: ClusterConfigProto.InterfaceType
    kInterfaceTypeVlan: ClusterConfigProto.InterfaceType
    kInterfaceTypeIpmi: ClusterConfigProto.InterfaceType
    kInterfaceTypeBridge: ClusterConfigProto.InterfaceType
    class FirewallId(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kFirewallIdUndefined: _ClassVar[ClusterConfigProto.FirewallId]
        kFirewallIdPrimary: _ClassVar[ClusterConfigProto.FirewallId]
        kFirewallIdAdmin: _ClassVar[ClusterConfigProto.FirewallId]
        kFirewallIdData: _ClassVar[ClusterConfigProto.FirewallId]
        kFirewallIdExternalData: _ClassVar[ClusterConfigProto.FirewallId]
        kFirewallIdInternalData: _ClassVar[ClusterConfigProto.FirewallId]
        kFirewallIdReplication: _ClassVar[ClusterConfigProto.FirewallId]
        kFirewallIdArchive: _ClassVar[ClusterConfigProto.FirewallId]
        kFirewallIdAthena: _ClassVar[ClusterConfigProto.FirewallId]
        kFirewallIdInterComm: _ClassVar[ClusterConfigProto.FirewallId]
        kFirewallIdExternalComm: _ClassVar[ClusterConfigProto.FirewallId]
        kFirewallIdCustomerDefinedStart: _ClassVar[ClusterConfigProto.FirewallId]
    kFirewallIdUndefined: ClusterConfigProto.FirewallId
    kFirewallIdPrimary: ClusterConfigProto.FirewallId
    kFirewallIdAdmin: ClusterConfigProto.FirewallId
    kFirewallIdData: ClusterConfigProto.FirewallId
    kFirewallIdExternalData: ClusterConfigProto.FirewallId
    kFirewallIdInternalData: ClusterConfigProto.FirewallId
    kFirewallIdReplication: ClusterConfigProto.FirewallId
    kFirewallIdArchive: ClusterConfigProto.FirewallId
    kFirewallIdAthena: ClusterConfigProto.FirewallId
    kFirewallIdInterComm: ClusterConfigProto.FirewallId
    kFirewallIdExternalComm: ClusterConfigProto.FirewallId
    kFirewallIdCustomerDefinedStart: ClusterConfigProto.FirewallId
    class InterfaceRole(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kInterfaceRolePrimary: _ClassVar[ClusterConfigProto.InterfaceRole]
        kInterfaceRoleSecondary: _ClassVar[ClusterConfigProto.InterfaceRole]
    kInterfaceRolePrimary: ClusterConfigProto.InterfaceRole
    kInterfaceRoleSecondary: ClusterConfigProto.InterfaceRole
    class ReservedProductModel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kReservedProductModelUnknown: _ClassVar[ClusterConfigProto.ReservedProductModel]
        kReservedProductModelVirtualEditionBifrost: _ClassVar[ClusterConfigProto.ReservedProductModel]
        kReservedProductModelFake: _ClassVar[ClusterConfigProto.ReservedProductModel]
        kReservedProductModelAll: _ClassVar[ClusterConfigProto.ReservedProductModel]
        kReservedProductModelC2301: _ClassVar[ClusterConfigProto.ReservedProductModel]
        kReservedProductModelR740X: _ClassVar[ClusterConfigProto.ReservedProductModel]
    kReservedProductModelUnknown: ClusterConfigProto.ReservedProductModel
    kReservedProductModelVirtualEditionBifrost: ClusterConfigProto.ReservedProductModel
    kReservedProductModelFake: ClusterConfigProto.ReservedProductModel
    kReservedProductModelAll: ClusterConfigProto.ReservedProductModel
    kReservedProductModelC2301: ClusterConfigProto.ReservedProductModel
    kReservedProductModelR740X: ClusterConfigProto.ReservedProductModel
    class ProductModel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kProductModelUnknown: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelC2100: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelC2300: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelC2500: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelC2510: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelC3000: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelUcsC240H4: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelMicrocloud: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelProliantGen9: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelC2105: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelC2305: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelC2505: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelC2515: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelC3500: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelC10000H: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelC2301: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelC2605: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelR740X: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelUcsC240H10: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelProliantDl380Gen10H4: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelProliantDl380Gen10H8: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelUcsC240M5H4: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelUcsC240M5H10: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelApolloR2200Gen10H8: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelApolloR2200Gen10H12: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelUcsS3260M5: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelApollo4510Gen10: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelPowerEdgeR740XdH4: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelPowerEdgeR740XdH8: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelC4300: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelC4500: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelC4600: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelUcsC220M5H8: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelUcsC220M5H12: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelC2700: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelC2705: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelC6015: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelC6025: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelC6035: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelApollo4510Gen10H14: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelPowerEdgeC6420H8: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelPowerEdgeC6420H12: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelPowerEdgeR640: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelCX8100: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelC6045: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelC6020: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelC6030: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelC6040: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelCX8200: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelCX8300: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelCX8105: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelCX8205: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelCX8305: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelR1208WF: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelC4100: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelAuriga: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelUcsC220M5SN: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelProliantDl360Gen10RoboH8: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelAppNode: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelPrimergyRx2540M5H8: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelUcsC220M5RoboH8: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelUcsC220M5RoboH4: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelProliantDl360Gen10RoboH4: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelC4000: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelCX8405: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelC6055: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelPrimergyRx2540M5H4: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelPowerEdgeR640RoboH4: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelPowerEdgeR640RoboH8: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelProliantDl360Gen10SN3: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelUcsS3260M5H14: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelUcsC220M5H4: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelProliantDl360Gen10SN6: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelR2208WFN7: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelC4000AppNode: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelProliantDl360Gen10SN7: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelApollo4200Gen10H16: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelApollo4200Gen10H4: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelApollo4200Gen10H8: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelApollo4200Gen10H12: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelApolloR2200Gen10H4: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelSuperServer1029UTN12RVN7: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelUcsS3260M5H16: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelThinkSystemSR650H4: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelThinkSystemSR650H8: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelUcsC220M5SN8: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelC4700: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelUcsC240M5H8: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelUcsC240M5H12: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelUcsC240M5H14: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelUcsC240M5H16: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelSupermicro6029PE1CR12L: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelApollo4510Gen10H12: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelProliantDl380Gen10H12: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelC5016: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelC5026: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelC5036: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelC5056: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelC5066: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelProliantDl380Gen10H14: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelProliantDl380Gen10SN3: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelProliantDl360Gen10RoboH14: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelProliantDl360Gen10RoboH18: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelUcsX210CM6SN15: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelProliantDl360Gen10H4: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelProliantDl360Gen10H8: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelProliantDl360Gen10H12: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelC5000PXG2: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelProliantDl360Gen10PlusSN15: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelPowerEdgeR740XdH12: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelPowerEdgeR740XdH16: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelC5000AppNode: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelUcsC240M6H4: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelUcsC240M6H8: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelUcsC240M6H12: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelUcsC240M6H18: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelThinkSystemSR645H8: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelThinkSystemSR645H12: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelProliantDl360Gen10PlusSN3: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelProliantDl360Gen10PlusSN7: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelUcsC220M6SN7: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelUcsC220M6SN15: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelProliantDl380Gen10PlusH4: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelProliantDl380Gen10PlusH8: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelProliantDl380Gen10PlusH12: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelProliantDl380Gen10PlusH14: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelGeneralStorageNode: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelDenseStorageNode: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelAllFlashNode: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelRoboNode: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelVirtualCluster: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelVirtualRoboEsx: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelGcp: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelAws: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelAzure: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelVirtualRoboHyperv: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelVirtualRoboVirtualBox: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelVirtualEditionCluster8TBEsx: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelVirtualEditionCluster16TBEsx: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelVirtualEditionKvm: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelVirtualEditionAhv: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelVirtualEditionBifrost: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelVirtualRoboAhv: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelVirtualRoboKvm: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelTenantVE: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelRigelVE: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelHeliosOnPremEsx: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelRigelAWS: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelRigelHyperv: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelBifrostHyperv: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelVirtualEditionClusterHyperv: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelHeliosOnPremKvm: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelGcpNextGen: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelRigelAzure: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelAWSNgceLarge: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelCohesionSmall: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelCohesionMedium: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelCohesionLarge: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelFake: _ClassVar[ClusterConfigProto.ProductModel]
        kProductModelAll: _ClassVar[ClusterConfigProto.ProductModel]
    kProductModelUnknown: ClusterConfigProto.ProductModel
    kProductModelC2100: ClusterConfigProto.ProductModel
    kProductModelC2300: ClusterConfigProto.ProductModel
    kProductModelC2500: ClusterConfigProto.ProductModel
    kProductModelC2510: ClusterConfigProto.ProductModel
    kProductModelC3000: ClusterConfigProto.ProductModel
    kProductModelUcsC240H4: ClusterConfigProto.ProductModel
    kProductModelMicrocloud: ClusterConfigProto.ProductModel
    kProductModelProliantGen9: ClusterConfigProto.ProductModel
    kProductModelC2105: ClusterConfigProto.ProductModel
    kProductModelC2305: ClusterConfigProto.ProductModel
    kProductModelC2505: ClusterConfigProto.ProductModel
    kProductModelC2515: ClusterConfigProto.ProductModel
    kProductModelC3500: ClusterConfigProto.ProductModel
    kProductModelC10000H: ClusterConfigProto.ProductModel
    kProductModelC2301: ClusterConfigProto.ProductModel
    kProductModelC2605: ClusterConfigProto.ProductModel
    kProductModelR740X: ClusterConfigProto.ProductModel
    kProductModelUcsC240H10: ClusterConfigProto.ProductModel
    kProductModelProliantDl380Gen10H4: ClusterConfigProto.ProductModel
    kProductModelProliantDl380Gen10H8: ClusterConfigProto.ProductModel
    kProductModelUcsC240M5H4: ClusterConfigProto.ProductModel
    kProductModelUcsC240M5H10: ClusterConfigProto.ProductModel
    kProductModelApolloR2200Gen10H8: ClusterConfigProto.ProductModel
    kProductModelApolloR2200Gen10H12: ClusterConfigProto.ProductModel
    kProductModelUcsS3260M5: ClusterConfigProto.ProductModel
    kProductModelApollo4510Gen10: ClusterConfigProto.ProductModel
    kProductModelPowerEdgeR740XdH4: ClusterConfigProto.ProductModel
    kProductModelPowerEdgeR740XdH8: ClusterConfigProto.ProductModel
    kProductModelC4300: ClusterConfigProto.ProductModel
    kProductModelC4500: ClusterConfigProto.ProductModel
    kProductModelC4600: ClusterConfigProto.ProductModel
    kProductModelUcsC220M5H8: ClusterConfigProto.ProductModel
    kProductModelUcsC220M5H12: ClusterConfigProto.ProductModel
    kProductModelC2700: ClusterConfigProto.ProductModel
    kProductModelC2705: ClusterConfigProto.ProductModel
    kProductModelC6015: ClusterConfigProto.ProductModel
    kProductModelC6025: ClusterConfigProto.ProductModel
    kProductModelC6035: ClusterConfigProto.ProductModel
    kProductModelApollo4510Gen10H14: ClusterConfigProto.ProductModel
    kProductModelPowerEdgeC6420H8: ClusterConfigProto.ProductModel
    kProductModelPowerEdgeC6420H12: ClusterConfigProto.ProductModel
    kProductModelPowerEdgeR640: ClusterConfigProto.ProductModel
    kProductModelCX8100: ClusterConfigProto.ProductModel
    kProductModelC6045: ClusterConfigProto.ProductModel
    kProductModelC6020: ClusterConfigProto.ProductModel
    kProductModelC6030: ClusterConfigProto.ProductModel
    kProductModelC6040: ClusterConfigProto.ProductModel
    kProductModelCX8200: ClusterConfigProto.ProductModel
    kProductModelCX8300: ClusterConfigProto.ProductModel
    kProductModelCX8105: ClusterConfigProto.ProductModel
    kProductModelCX8205: ClusterConfigProto.ProductModel
    kProductModelCX8305: ClusterConfigProto.ProductModel
    kProductModelR1208WF: ClusterConfigProto.ProductModel
    kProductModelC4100: ClusterConfigProto.ProductModel
    kProductModelAuriga: ClusterConfigProto.ProductModel
    kProductModelUcsC220M5SN: ClusterConfigProto.ProductModel
    kProductModelProliantDl360Gen10RoboH8: ClusterConfigProto.ProductModel
    kProductModelAppNode: ClusterConfigProto.ProductModel
    kProductModelPrimergyRx2540M5H8: ClusterConfigProto.ProductModel
    kProductModelUcsC220M5RoboH8: ClusterConfigProto.ProductModel
    kProductModelUcsC220M5RoboH4: ClusterConfigProto.ProductModel
    kProductModelProliantDl360Gen10RoboH4: ClusterConfigProto.ProductModel
    kProductModelC4000: ClusterConfigProto.ProductModel
    kProductModelCX8405: ClusterConfigProto.ProductModel
    kProductModelC6055: ClusterConfigProto.ProductModel
    kProductModelPrimergyRx2540M5H4: ClusterConfigProto.ProductModel
    kProductModelPowerEdgeR640RoboH4: ClusterConfigProto.ProductModel
    kProductModelPowerEdgeR640RoboH8: ClusterConfigProto.ProductModel
    kProductModelProliantDl360Gen10SN3: ClusterConfigProto.ProductModel
    kProductModelUcsS3260M5H14: ClusterConfigProto.ProductModel
    kProductModelUcsC220M5H4: ClusterConfigProto.ProductModel
    kProductModelProliantDl360Gen10SN6: ClusterConfigProto.ProductModel
    kProductModelR2208WFN7: ClusterConfigProto.ProductModel
    kProductModelC4000AppNode: ClusterConfigProto.ProductModel
    kProductModelProliantDl360Gen10SN7: ClusterConfigProto.ProductModel
    kProductModelApollo4200Gen10H16: ClusterConfigProto.ProductModel
    kProductModelApollo4200Gen10H4: ClusterConfigProto.ProductModel
    kProductModelApollo4200Gen10H8: ClusterConfigProto.ProductModel
    kProductModelApollo4200Gen10H12: ClusterConfigProto.ProductModel
    kProductModelApolloR2200Gen10H4: ClusterConfigProto.ProductModel
    kProductModelSuperServer1029UTN12RVN7: ClusterConfigProto.ProductModel
    kProductModelUcsS3260M5H16: ClusterConfigProto.ProductModel
    kProductModelThinkSystemSR650H4: ClusterConfigProto.ProductModel
    kProductModelThinkSystemSR650H8: ClusterConfigProto.ProductModel
    kProductModelUcsC220M5SN8: ClusterConfigProto.ProductModel
    kProductModelC4700: ClusterConfigProto.ProductModel
    kProductModelUcsC240M5H8: ClusterConfigProto.ProductModel
    kProductModelUcsC240M5H12: ClusterConfigProto.ProductModel
    kProductModelUcsC240M5H14: ClusterConfigProto.ProductModel
    kProductModelUcsC240M5H16: ClusterConfigProto.ProductModel
    kProductModelSupermicro6029PE1CR12L: ClusterConfigProto.ProductModel
    kProductModelApollo4510Gen10H12: ClusterConfigProto.ProductModel
    kProductModelProliantDl380Gen10H12: ClusterConfigProto.ProductModel
    kProductModelC5016: ClusterConfigProto.ProductModel
    kProductModelC5026: ClusterConfigProto.ProductModel
    kProductModelC5036: ClusterConfigProto.ProductModel
    kProductModelC5056: ClusterConfigProto.ProductModel
    kProductModelC5066: ClusterConfigProto.ProductModel
    kProductModelProliantDl380Gen10H14: ClusterConfigProto.ProductModel
    kProductModelProliantDl380Gen10SN3: ClusterConfigProto.ProductModel
    kProductModelProliantDl360Gen10RoboH14: ClusterConfigProto.ProductModel
    kProductModelProliantDl360Gen10RoboH18: ClusterConfigProto.ProductModel
    kProductModelUcsX210CM6SN15: ClusterConfigProto.ProductModel
    kProductModelProliantDl360Gen10H4: ClusterConfigProto.ProductModel
    kProductModelProliantDl360Gen10H8: ClusterConfigProto.ProductModel
    kProductModelProliantDl360Gen10H12: ClusterConfigProto.ProductModel
    kProductModelC5000PXG2: ClusterConfigProto.ProductModel
    kProductModelProliantDl360Gen10PlusSN15: ClusterConfigProto.ProductModel
    kProductModelPowerEdgeR740XdH12: ClusterConfigProto.ProductModel
    kProductModelPowerEdgeR740XdH16: ClusterConfigProto.ProductModel
    kProductModelC5000AppNode: ClusterConfigProto.ProductModel
    kProductModelUcsC240M6H4: ClusterConfigProto.ProductModel
    kProductModelUcsC240M6H8: ClusterConfigProto.ProductModel
    kProductModelUcsC240M6H12: ClusterConfigProto.ProductModel
    kProductModelUcsC240M6H18: ClusterConfigProto.ProductModel
    kProductModelThinkSystemSR645H8: ClusterConfigProto.ProductModel
    kProductModelThinkSystemSR645H12: ClusterConfigProto.ProductModel
    kProductModelProliantDl360Gen10PlusSN3: ClusterConfigProto.ProductModel
    kProductModelProliantDl360Gen10PlusSN7: ClusterConfigProto.ProductModel
    kProductModelUcsC220M6SN7: ClusterConfigProto.ProductModel
    kProductModelUcsC220M6SN15: ClusterConfigProto.ProductModel
    kProductModelProliantDl380Gen10PlusH4: ClusterConfigProto.ProductModel
    kProductModelProliantDl380Gen10PlusH8: ClusterConfigProto.ProductModel
    kProductModelProliantDl380Gen10PlusH12: ClusterConfigProto.ProductModel
    kProductModelProliantDl380Gen10PlusH14: ClusterConfigProto.ProductModel
    kProductModelGeneralStorageNode: ClusterConfigProto.ProductModel
    kProductModelDenseStorageNode: ClusterConfigProto.ProductModel
    kProductModelAllFlashNode: ClusterConfigProto.ProductModel
    kProductModelRoboNode: ClusterConfigProto.ProductModel
    kProductModelVirtualCluster: ClusterConfigProto.ProductModel
    kProductModelVirtualRoboEsx: ClusterConfigProto.ProductModel
    kProductModelGcp: ClusterConfigProto.ProductModel
    kProductModelAws: ClusterConfigProto.ProductModel
    kProductModelAzure: ClusterConfigProto.ProductModel
    kProductModelVirtualRoboHyperv: ClusterConfigProto.ProductModel
    kProductModelVirtualRoboVirtualBox: ClusterConfigProto.ProductModel
    kProductModelVirtualEditionCluster8TBEsx: ClusterConfigProto.ProductModel
    kProductModelVirtualEditionCluster16TBEsx: ClusterConfigProto.ProductModel
    kProductModelVirtualEditionKvm: ClusterConfigProto.ProductModel
    kProductModelVirtualEditionAhv: ClusterConfigProto.ProductModel
    kProductModelVirtualEditionBifrost: ClusterConfigProto.ProductModel
    kProductModelVirtualRoboAhv: ClusterConfigProto.ProductModel
    kProductModelVirtualRoboKvm: ClusterConfigProto.ProductModel
    kProductModelTenantVE: ClusterConfigProto.ProductModel
    kProductModelRigelVE: ClusterConfigProto.ProductModel
    kProductModelHeliosOnPremEsx: ClusterConfigProto.ProductModel
    kProductModelRigelAWS: ClusterConfigProto.ProductModel
    kProductModelRigelHyperv: ClusterConfigProto.ProductModel
    kProductModelBifrostHyperv: ClusterConfigProto.ProductModel
    kProductModelVirtualEditionClusterHyperv: ClusterConfigProto.ProductModel
    kProductModelHeliosOnPremKvm: ClusterConfigProto.ProductModel
    kProductModelGcpNextGen: ClusterConfigProto.ProductModel
    kProductModelRigelAzure: ClusterConfigProto.ProductModel
    kProductModelAWSNgceLarge: ClusterConfigProto.ProductModel
    kProductModelCohesionSmall: ClusterConfigProto.ProductModel
    kProductModelCohesionMedium: ClusterConfigProto.ProductModel
    kProductModelCohesionLarge: ClusterConfigProto.ProductModel
    kProductModelFake: ClusterConfigProto.ProductModel
    kProductModelAll: ClusterConfigProto.ProductModel
    class ClusterSize(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kSmall: _ClassVar[ClusterConfigProto.ClusterSize]
        kMedium: _ClassVar[ClusterConfigProto.ClusterSize]
        kLarge: _ClassVar[ClusterConfigProto.ClusterSize]
        kXLarge: _ClassVar[ClusterConfigProto.ClusterSize]
        kNextGen: _ClassVar[ClusterConfigProto.ClusterSize]
    kSmall: ClusterConfigProto.ClusterSize
    kMedium: ClusterConfigProto.ClusterSize
    kLarge: ClusterConfigProto.ClusterSize
    kXLarge: ClusterConfigProto.ClusterSize
    kNextGen: ClusterConfigProto.ClusterSize
    class BondingMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kActiveBackup: _ClassVar[ClusterConfigProto.BondingMode]
        k802_3ad: _ClassVar[ClusterConfigProto.BondingMode]
    kActiveBackup: ClusterConfigProto.BondingMode
    k802_3ad: ClusterConfigProto.BondingMode
    class XmitHashPolicy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kXmitHashLayer2: _ClassVar[ClusterConfigProto.XmitHashPolicy]
        kXmitHashLayer3Plus4: _ClassVar[ClusterConfigProto.XmitHashPolicy]
        kXmitHashLayer2Plus3: _ClassVar[ClusterConfigProto.XmitHashPolicy]
    kXmitHashLayer2: ClusterConfigProto.XmitHashPolicy
    kXmitHashLayer3Plus4: ClusterConfigProto.XmitHashPolicy
    kXmitHashLayer2Plus3: ClusterConfigProto.XmitHashPolicy
    class LacpRate(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kLacpRateSlow: _ClassVar[ClusterConfigProto.LacpRate]
        kLacpRateFast: _ClassVar[ClusterConfigProto.LacpRate]
    kLacpRateSlow: ClusterConfigProto.LacpRate
    kLacpRateFast: ClusterConfigProto.LacpRate
    class OwnershipContext(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kOwnershipContextLocal: _ClassVar[ClusterConfigProto.OwnershipContext]
        kOwnershipContextFortKnox: _ClassVar[ClusterConfigProto.OwnershipContext]
    kOwnershipContextLocal: ClusterConfigProto.OwnershipContext
    kOwnershipContextFortKnox: ClusterConfigProto.OwnershipContext
    class ShareType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kCIFS: _ClassVar[ClusterConfigProto.ShareType]
        kNFS: _ClassVar[ClusterConfigProto.ShareType]
    kCIFS: ClusterConfigProto.ShareType
    kNFS: ClusterConfigProto.ShareType
    class NfsVersionNumber(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNfsVersionNumberNone: _ClassVar[ClusterConfigProto.NfsVersionNumber]
        kNfsVersionNumber3: _ClassVar[ClusterConfigProto.NfsVersionNumber]
        kNfsVersionNumber4: _ClassVar[ClusterConfigProto.NfsVersionNumber]
        kNfsVersionNumber4_0: _ClassVar[ClusterConfigProto.NfsVersionNumber]
        kNfsVersionNumber4_1: _ClassVar[ClusterConfigProto.NfsVersionNumber]
        kNfsVersionNumber4_2: _ClassVar[ClusterConfigProto.NfsVersionNumber]
    kNfsVersionNumberNone: ClusterConfigProto.NfsVersionNumber
    kNfsVersionNumber3: ClusterConfigProto.NfsVersionNumber
    kNfsVersionNumber4: ClusterConfigProto.NfsVersionNumber
    kNfsVersionNumber4_0: ClusterConfigProto.NfsVersionNumber
    kNfsVersionNumber4_1: ClusterConfigProto.NfsVersionNumber
    kNfsVersionNumber4_2: ClusterConfigProto.NfsVersionNumber
    class NfsSecurityType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNfsSecurityTypeDefault: _ClassVar[ClusterConfigProto.NfsSecurityType]
        kNfsSecurityTypeNone: _ClassVar[ClusterConfigProto.NfsSecurityType]
        kNfsSecurityTypeSys: _ClassVar[ClusterConfigProto.NfsSecurityType]
        kNfsSecurityTypeKRB5: _ClassVar[ClusterConfigProto.NfsSecurityType]
        kNfsSecurityTypeKRB5I: _ClassVar[ClusterConfigProto.NfsSecurityType]
        kNfsSecurityTypeKRB5P: _ClassVar[ClusterConfigProto.NfsSecurityType]
    kNfsSecurityTypeDefault: ClusterConfigProto.NfsSecurityType
    kNfsSecurityTypeNone: ClusterConfigProto.NfsSecurityType
    kNfsSecurityTypeSys: ClusterConfigProto.NfsSecurityType
    kNfsSecurityTypeKRB5: ClusterConfigProto.NfsSecurityType
    kNfsSecurityTypeKRB5I: ClusterConfigProto.NfsSecurityType
    kNfsSecurityTypeKRB5P: ClusterConfigProto.NfsSecurityType
    class SnmpVersion(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kSnmpV2: _ClassVar[ClusterConfigProto.SnmpVersion]
        kSnmpV3: _ClassVar[ClusterConfigProto.SnmpVersion]
    kSnmpV2: ClusterConfigProto.SnmpVersion
    kSnmpV3: ClusterConfigProto.SnmpVersion
    class AuthType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kPasswordOnly: _ClassVar[ClusterConfigProto.AuthType]
        kCertificateOnly: _ClassVar[ClusterConfigProto.AuthType]
        kPasswordAndCertificate: _ClassVar[ClusterConfigProto.AuthType]
    kPasswordOnly: ClusterConfigProto.AuthType
    kCertificateOnly: ClusterConfigProto.AuthType
    kPasswordAndCertificate: ClusterConfigProto.AuthType
    class LibrarianMigrationStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kLibrarianMigrationNotStarted: _ClassVar[ClusterConfigProto.LibrarianMigrationStatus]
        kLibrarianMigrationStarted: _ClassVar[ClusterConfigProto.LibrarianMigrationStatus]
        kLibrarianMigrationFinished: _ClassVar[ClusterConfigProto.LibrarianMigrationStatus]
    kLibrarianMigrationNotStarted: ClusterConfigProto.LibrarianMigrationStatus
    kLibrarianMigrationStarted: ClusterConfigProto.LibrarianMigrationStatus
    kLibrarianMigrationFinished: ClusterConfigProto.LibrarianMigrationStatus
    class FirewallProfileType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kFirewallProfileTypePredefined: _ClassVar[ClusterConfigProto.FirewallProfileType]
        kFirewallProfileTypeUserDefined: _ClassVar[ClusterConfigProto.FirewallProfileType]
    kFirewallProfileTypePredefined: ClusterConfigProto.FirewallProfileType
    kFirewallProfileTypeUserDefined: ClusterConfigProto.FirewallProfileType
    class InterfaceGroupType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kInterfaceGroupTypeBond: _ClassVar[ClusterConfigProto.InterfaceGroupType]
        kInterfaceGroupTypeLoopback: _ClassVar[ClusterConfigProto.InterfaceGroupType]
    kInterfaceGroupTypeBond: ClusterConfigProto.InterfaceGroupType
    kInterfaceGroupTypeLoopback: ClusterConfigProto.InterfaceGroupType
    class supportTokenVersion(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        unknownToken: _ClassVar[ClusterConfigProto.supportTokenVersion]
        ecdsaKey: _ClassVar[ClusterConfigProto.supportTokenVersion]
        encryptedEcdsaKey: _ClassVar[ClusterConfigProto.supportTokenVersion]
    unknownToken: ClusterConfigProto.supportTokenVersion
    ecdsaKey: ClusterConfigProto.supportTokenVersion
    encryptedEcdsaKey: ClusterConfigProto.supportTokenVersion
    class supportUser2FAMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        No2FAPasswordOnly: _ClassVar[ClusterConfigProto.supportUser2FAMode]
        PasswordAndTOTP: _ClassVar[ClusterConfigProto.supportUser2FAMode]
        PasswordAndEmail: _ClassVar[ClusterConfigProto.supportUser2FAMode]
    No2FAPasswordOnly: ClusterConfigProto.supportUser2FAMode
    PasswordAndTOTP: ClusterConfigProto.supportUser2FAMode
    PasswordAndEmail: ClusterConfigProto.supportUser2FAMode
    class sudoAccessMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SudoAccessDisabled: _ClassVar[ClusterConfigProto.sudoAccessMode]
        SudoAccessEnabledUntilSupportChannelExpiry: _ClassVar[ClusterConfigProto.sudoAccessMode]
        SudoAccessTemporaryEnabled: _ClassVar[ClusterConfigProto.sudoAccessMode]
    SudoAccessDisabled: ClusterConfigProto.sudoAccessMode
    SudoAccessEnabledUntilSupportChannelExpiry: ClusterConfigProto.sudoAccessMode
    SudoAccessTemporaryEnabled: ClusterConfigProto.sudoAccessMode
    class ESMigrationStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kESMigrationNotStarted: _ClassVar[ClusterConfigProto.ESMigrationStatus]
        kESMigrationStarted: _ClassVar[ClusterConfigProto.ESMigrationStatus]
        kESMigrationFinished: _ClassVar[ClusterConfigProto.ESMigrationStatus]
    kESMigrationNotStarted: ClusterConfigProto.ESMigrationStatus
    kESMigrationStarted: ClusterConfigProto.ESMigrationStatus
    kESMigrationFinished: ClusterConfigProto.ESMigrationStatus
    class PXGESMigrationStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kPXGESMigrationNotStarted: _ClassVar[ClusterConfigProto.PXGESMigrationStatus]
        kPXGESMigrationStarted: _ClassVar[ClusterConfigProto.PXGESMigrationStatus]
        kPXGESMigrationFinished: _ClassVar[ClusterConfigProto.PXGESMigrationStatus]
    kPXGESMigrationNotStarted: ClusterConfigProto.PXGESMigrationStatus
    kPXGESMigrationStarted: ClusterConfigProto.PXGESMigrationStatus
    kPXGESMigrationFinished: ClusterConfigProto.PXGESMigrationStatus
    class IrisAPIBackupDataACL(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kAllowNone: _ClassVar[ClusterConfigProto.IrisAPIBackupDataACL]
        KAllowClone: _ClassVar[ClusterConfigProto.IrisAPIBackupDataACL]
    kAllowNone: ClusterConfigProto.IrisAPIBackupDataACL
    KAllowClone: ClusterConfigProto.IrisAPIBackupDataACL
    class Subnet(_message.Message):
        __slots__ = ("ip", "netmask_bits", "netmask_ip4", "description", "gateway", "id", "component", "nfs_root_squash", "nfs_access", "smb_access", "nfs_all_squash", "s3_access")
        class Component(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            unknown: _ClassVar[ClusterConfigProto.Subnet.Component]
            nexus: _ClassVar[ClusterConfigProto.Subnet.Component]
            athena: _ClassVar[ClusterConfigProto.Subnet.Component]
        unknown: ClusterConfigProto.Subnet.Component
        nexus: ClusterConfigProto.Subnet.Component
        athena: ClusterConfigProto.Subnet.Component
        IP_FIELD_NUMBER: _ClassVar[int]
        NETMASK_BITS_FIELD_NUMBER: _ClassVar[int]
        NETMASK_IP4_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        GATEWAY_FIELD_NUMBER: _ClassVar[int]
        ID_FIELD_NUMBER: _ClassVar[int]
        COMPONENT_FIELD_NUMBER: _ClassVar[int]
        NFS_ROOT_SQUASH_FIELD_NUMBER: _ClassVar[int]
        NFS_ACCESS_FIELD_NUMBER: _ClassVar[int]
        SMB_ACCESS_FIELD_NUMBER: _ClassVar[int]
        NFS_ALL_SQUASH_FIELD_NUMBER: _ClassVar[int]
        S3_ACCESS_FIELD_NUMBER: _ClassVar[int]
        ip: str
        netmask_bits: int
        netmask_ip4: str
        description: str
        gateway: str
        id: int
        component: ClusterConfigProto.Subnet.Component
        nfs_root_squash: bool
        nfs_access: ClusterConfigProto.ProtocolAccessLevel
        smb_access: ClusterConfigProto.ProtocolAccessLevel
        nfs_all_squash: bool
        s3_access: ClusterConfigProto.ProtocolAccessLevel
        def __init__(self, ip: _Optional[str] = ..., netmask_bits: _Optional[int] = ..., netmask_ip4: _Optional[str] = ..., description: _Optional[str] = ..., gateway: _Optional[str] = ..., id: _Optional[int] = ..., component: _Optional[_Union[ClusterConfigProto.Subnet.Component, str]] = ..., nfs_root_squash: bool = ..., nfs_access: _Optional[_Union[ClusterConfigProto.ProtocolAccessLevel, str]] = ..., smb_access: _Optional[_Union[ClusterConfigProto.ProtocolAccessLevel, str]] = ..., nfs_all_squash: bool = ..., s3_access: _Optional[_Union[ClusterConfigProto.ProtocolAccessLevel, str]] = ...) -> None: ...
    class IpConfig(_message.Message):
        __slots__ = ("ip", "subnet", "gateway", "uses_dhcp")
        IP_FIELD_NUMBER: _ClassVar[int]
        SUBNET_FIELD_NUMBER: _ClassVar[int]
        GATEWAY_FIELD_NUMBER: _ClassVar[int]
        USES_DHCP_FIELD_NUMBER: _ClassVar[int]
        ip: str
        subnet: ClusterConfigProto.Subnet
        gateway: str
        uses_dhcp: bool
        def __init__(self, ip: _Optional[str] = ..., subnet: _Optional[_Union[ClusterConfigProto.Subnet, _Mapping]] = ..., gateway: _Optional[str] = ..., uses_dhcp: bool = ...) -> None: ...
    class NetworkInterface(_message.Message):
        __slots__ = ("id", "deprecated_subnet", "deprecated_ip", "deprecated_gateway", "mtu", "is_default_route", "bonding_mode", "interface_name", "interface_type", "firewall_profile_vec", "route_vec", "subnet_id", "speed_mbps", "interface_group_id_vec", "ip_config_vec", "interface_role")
        ID_FIELD_NUMBER: _ClassVar[int]
        DEPRECATED_SUBNET_FIELD_NUMBER: _ClassVar[int]
        DEPRECATED_IP_FIELD_NUMBER: _ClassVar[int]
        DEPRECATED_GATEWAY_FIELD_NUMBER: _ClassVar[int]
        MTU_FIELD_NUMBER: _ClassVar[int]
        IS_DEFAULT_ROUTE_FIELD_NUMBER: _ClassVar[int]
        BONDING_MODE_FIELD_NUMBER: _ClassVar[int]
        INTERFACE_NAME_FIELD_NUMBER: _ClassVar[int]
        INTERFACE_TYPE_FIELD_NUMBER: _ClassVar[int]
        FIREWALL_PROFILE_VEC_FIELD_NUMBER: _ClassVar[int]
        ROUTE_VEC_FIELD_NUMBER: _ClassVar[int]
        SUBNET_ID_FIELD_NUMBER: _ClassVar[int]
        SPEED_MBPS_FIELD_NUMBER: _ClassVar[int]
        INTERFACE_GROUP_ID_VEC_FIELD_NUMBER: _ClassVar[int]
        IP_CONFIG_VEC_FIELD_NUMBER: _ClassVar[int]
        INTERFACE_ROLE_FIELD_NUMBER: _ClassVar[int]
        id: int
        deprecated_subnet: ClusterConfigProto.Subnet
        deprecated_ip: str
        deprecated_gateway: str
        mtu: int
        is_default_route: bool
        bonding_mode: int
        interface_name: str
        interface_type: ClusterConfigProto.InterfaceType
        firewall_profile_vec: _containers.RepeatedScalarFieldContainer[int]
        route_vec: _containers.RepeatedScalarFieldContainer[int]
        subnet_id: int
        speed_mbps: int
        interface_group_id_vec: _containers.RepeatedScalarFieldContainer[int]
        ip_config_vec: _containers.RepeatedCompositeFieldContainer[ClusterConfigProto.IpConfig]
        interface_role: ClusterConfigProto.InterfaceRole
        def __init__(self, id: _Optional[int] = ..., deprecated_subnet: _Optional[_Union[ClusterConfigProto.Subnet, _Mapping]] = ..., deprecated_ip: _Optional[str] = ..., deprecated_gateway: _Optional[str] = ..., mtu: _Optional[int] = ..., is_default_route: bool = ..., bonding_mode: _Optional[int] = ..., interface_name: _Optional[str] = ..., interface_type: _Optional[_Union[ClusterConfigProto.InterfaceType, str]] = ..., firewall_profile_vec: _Optional[_Iterable[int]] = ..., route_vec: _Optional[_Iterable[int]] = ..., subnet_id: _Optional[int] = ..., speed_mbps: _Optional[int] = ..., interface_group_id_vec: _Optional[_Iterable[int]] = ..., ip_config_vec: _Optional[_Iterable[_Union[ClusterConfigProto.IpConfig, _Mapping]]] = ..., interface_role: _Optional[_Union[ClusterConfigProto.InterfaceRole, str]] = ...) -> None: ...
    class FibreChannelPort(_message.Message):
        __slots__ = ("wwpn", "wwnn", "port_number", "port_type", "connection_mode", "port_status", "data_rate")
        WWPN_FIELD_NUMBER: _ClassVar[int]
        WWNN_FIELD_NUMBER: _ClassVar[int]
        PORT_NUMBER_FIELD_NUMBER: _ClassVar[int]
        PORT_TYPE_FIELD_NUMBER: _ClassVar[int]
        CONNECTION_MODE_FIELD_NUMBER: _ClassVar[int]
        PORT_STATUS_FIELD_NUMBER: _ClassVar[int]
        DATA_RATE_FIELD_NUMBER: _ClassVar[int]
        wwpn: str
        wwnn: str
        port_number: str
        port_type: str
        connection_mode: str
        port_status: str
        data_rate: str
        def __init__(self, wwpn: _Optional[str] = ..., wwnn: _Optional[str] = ..., port_number: _Optional[str] = ..., port_type: _Optional[str] = ..., connection_mode: _Optional[str] = ..., port_status: _Optional[str] = ..., data_rate: _Optional[str] = ...) -> None: ...
    class StorageTier(_message.Message):
        __slots__ = ("name", "self_fault_tolerant", "all_nodes_reachable", "min_encryption_level", "hardware_encryption_level", "down_waterfall_threshold_pct", "admission_control_threshold", "tier_rebalance_delay_secs", "content_modification_allowed", "min_compression_level", "hardware_encryption_capability", "write_uptier_num_access_threshold", "read_uptier_num_access_threshold", "disks_in_vaults", "disk_bandwidth_MBps", "downtier_target_tier", "allow_double_encryption")
        NAME_FIELD_NUMBER: _ClassVar[int]
        SELF_FAULT_TOLERANT_FIELD_NUMBER: _ClassVar[int]
        ALL_NODES_REACHABLE_FIELD_NUMBER: _ClassVar[int]
        MIN_ENCRYPTION_LEVEL_FIELD_NUMBER: _ClassVar[int]
        HARDWARE_ENCRYPTION_LEVEL_FIELD_NUMBER: _ClassVar[int]
        DOWN_WATERFALL_THRESHOLD_PCT_FIELD_NUMBER: _ClassVar[int]
        ADMISSION_CONTROL_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
        TIER_REBALANCE_DELAY_SECS_FIELD_NUMBER: _ClassVar[int]
        CONTENT_MODIFICATION_ALLOWED_FIELD_NUMBER: _ClassVar[int]
        MIN_COMPRESSION_LEVEL_FIELD_NUMBER: _ClassVar[int]
        HARDWARE_ENCRYPTION_CAPABILITY_FIELD_NUMBER: _ClassVar[int]
        WRITE_UPTIER_NUM_ACCESS_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
        READ_UPTIER_NUM_ACCESS_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
        DISKS_IN_VAULTS_FIELD_NUMBER: _ClassVar[int]
        DISK_BANDWIDTH_MBPS_FIELD_NUMBER: _ClassVar[int]
        DOWNTIER_TARGET_TIER_FIELD_NUMBER: _ClassVar[int]
        ALLOW_DOUBLE_ENCRYPTION_FIELD_NUMBER: _ClassVar[int]
        name: str
        self_fault_tolerant: bool
        all_nodes_reachable: bool
        min_encryption_level: ClusterConfigProto.EncryptionLevel
        hardware_encryption_level: ClusterConfigProto.EncryptionLevel
        down_waterfall_threshold_pct: int
        admission_control_threshold: int
        tier_rebalance_delay_secs: int
        content_modification_allowed: bool
        min_compression_level: ClusterConfigProto.StoragePolicy.CompressionLevel
        hardware_encryption_capability: ClusterConfigProto.EncryptionLevel
        write_uptier_num_access_threshold: int
        read_uptier_num_access_threshold: int
        disks_in_vaults: bool
        disk_bandwidth_MBps: int
        downtier_target_tier: str
        allow_double_encryption: bool
        def __init__(self, name: _Optional[str] = ..., self_fault_tolerant: bool = ..., all_nodes_reachable: bool = ..., min_encryption_level: _Optional[_Union[ClusterConfigProto.EncryptionLevel, str]] = ..., hardware_encryption_level: _Optional[_Union[ClusterConfigProto.EncryptionLevel, str]] = ..., down_waterfall_threshold_pct: _Optional[int] = ..., admission_control_threshold: _Optional[int] = ..., tier_rebalance_delay_secs: _Optional[int] = ..., content_modification_allowed: bool = ..., min_compression_level: _Optional[_Union[ClusterConfigProto.StoragePolicy.CompressionLevel, str]] = ..., hardware_encryption_capability: _Optional[_Union[ClusterConfigProto.EncryptionLevel, str]] = ..., write_uptier_num_access_threshold: _Optional[int] = ..., read_uptier_num_access_threshold: _Optional[int] = ..., disks_in_vaults: bool = ..., disk_bandwidth_MBps: _Optional[int] = ..., downtier_target_tier: _Optional[str] = ..., allow_double_encryption: bool = ...) -> None: ...
    class RemovalState(_message.Message):
        __slots__ = ("version", "status", "reasons_vec", "stop_writes_barrier", "ack")
        class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kDontRemove: _ClassVar[ClusterConfigProto.RemovalState.Status]
            kMarkedForRemoval: _ClassVar[ClusterConfigProto.RemovalState.Status]
            kOkToRemove: _ClassVar[ClusterConfigProto.RemovalState.Status]
        kDontRemove: ClusterConfigProto.RemovalState.Status
        kMarkedForRemoval: ClusterConfigProto.RemovalState.Status
        kOkToRemove: ClusterConfigProto.RemovalState.Status
        class Ack(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kUnknown: _ClassVar[ClusterConfigProto.RemovalState.Ack]
            kScribe: _ClassVar[ClusterConfigProto.RemovalState.Ack]
            kApollo: _ClassVar[ClusterConfigProto.RemovalState.Ack]
            kGandalf: _ClassVar[ClusterConfigProto.RemovalState.Ack]
            kYoda: _ClassVar[ClusterConfigProto.RemovalState.Ack]
            kMagneto: _ClassVar[ClusterConfigProto.RemovalState.Ack]
            kHydra: _ClassVar[ClusterConfigProto.RemovalState.Ack]
            kLibrarian: _ClassVar[ClusterConfigProto.RemovalState.Ack]
            kChunkRepository: _ClassVar[ClusterConfigProto.RemovalState.Ack]
            kAthena: _ClassVar[ClusterConfigProto.RemovalState.Ack]
            kGroot: _ClassVar[ClusterConfigProto.RemovalState.Ack]
            kAll: _ClassVar[ClusterConfigProto.RemovalState.Ack]
        kUnknown: ClusterConfigProto.RemovalState.Ack
        kScribe: ClusterConfigProto.RemovalState.Ack
        kApollo: ClusterConfigProto.RemovalState.Ack
        kGandalf: ClusterConfigProto.RemovalState.Ack
        kYoda: ClusterConfigProto.RemovalState.Ack
        kMagneto: ClusterConfigProto.RemovalState.Ack
        kHydra: ClusterConfigProto.RemovalState.Ack
        kLibrarian: ClusterConfigProto.RemovalState.Ack
        kChunkRepository: ClusterConfigProto.RemovalState.Ack
        kAthena: ClusterConfigProto.RemovalState.Ack
        kGroot: ClusterConfigProto.RemovalState.Ack
        kAll: ClusterConfigProto.RemovalState.Ack
        class Reason(_message.Message):
            __slots__ = ("type", "timestamp_msecs", "message")
            class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                kUnknown: _ClassVar[ClusterConfigProto.RemovalState.Reason.Type]
                kAutoHealthCheck: _ClassVar[ClusterConfigProto.RemovalState.Reason.Type]
                kUserGracefulRemoval: _ClassVar[ClusterConfigProto.RemovalState.Reason.Type]
                kUserAvoidAccess: _ClassVar[ClusterConfigProto.RemovalState.Reason.Type]
                kUserGracefulNodeRemoval: _ClassVar[ClusterConfigProto.RemovalState.Reason.Type]
                kUserRemoveDownNode: _ClassVar[ClusterConfigProto.RemovalState.Reason.Type]
                kBridgeDataUnavailable: _ClassVar[ClusterConfigProto.RemovalState.Reason.Type]
            kUnknown: ClusterConfigProto.RemovalState.Reason.Type
            kAutoHealthCheck: ClusterConfigProto.RemovalState.Reason.Type
            kUserGracefulRemoval: ClusterConfigProto.RemovalState.Reason.Type
            kUserAvoidAccess: ClusterConfigProto.RemovalState.Reason.Type
            kUserGracefulNodeRemoval: ClusterConfigProto.RemovalState.Reason.Type
            kUserRemoveDownNode: ClusterConfigProto.RemovalState.Reason.Type
            kBridgeDataUnavailable: ClusterConfigProto.RemovalState.Reason.Type
            TYPE_FIELD_NUMBER: _ClassVar[int]
            TIMESTAMP_MSECS_FIELD_NUMBER: _ClassVar[int]
            MESSAGE_FIELD_NUMBER: _ClassVar[int]
            type: ClusterConfigProto.RemovalState.Reason.Type
            timestamp_msecs: int
            message: str
            def __init__(self, type: _Optional[_Union[ClusterConfigProto.RemovalState.Reason.Type, str]] = ..., timestamp_msecs: _Optional[int] = ..., message: _Optional[str] = ...) -> None: ...
        VERSION_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        REASONS_VEC_FIELD_NUMBER: _ClassVar[int]
        STOP_WRITES_BARRIER_FIELD_NUMBER: _ClassVar[int]
        ACK_FIELD_NUMBER: _ClassVar[int]
        version: int
        status: ClusterConfigProto.RemovalState.Status
        reasons_vec: _containers.RepeatedCompositeFieldContainer[ClusterConfigProto.RemovalState.Reason]
        stop_writes_barrier: int
        ack: int
        def __init__(self, version: _Optional[int] = ..., status: _Optional[_Union[ClusterConfigProto.RemovalState.Status, str]] = ..., reasons_vec: _Optional[_Iterable[_Union[ClusterConfigProto.RemovalState.Reason, _Mapping]]] = ..., stop_writes_barrier: _Optional[int] = ..., ack: _Optional[int] = ...) -> None: ...
    class Disk(_message.Message):
        __slots__ = ("id", "tier", "location", "current_node_id", "last_node_id", "offline", "max_capacity_bytes", "usable_capacity_bytes", "removal_state", "access_method", "reservation_vec", "serial_number", "kms_uid", "encryption_state", "encrypted_disk_encryption_key", "previous_encrypted_disk_encryption_key", "previous_kms_uid", "admin_offline", "current_chunk_repository_wal_location", "desired_chunk_repository_wal_location", "chunk_repo_wal_incarnation", "disk_exclusive_for_component", "self_fault_tolerant", "all_nodes_reachable")
        class Component(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kUnknown: _ClassVar[ClusterConfigProto.Disk.Component]
            kApollo: _ClassVar[ClusterConfigProto.Disk.Component]
            kScribe: _ClassVar[ClusterConfigProto.Disk.Component]
            kHydra: _ClassVar[ClusterConfigProto.Disk.Component]
            kYoda: _ClassVar[ClusterConfigProto.Disk.Component]
            kLibrarian: _ClassVar[ClusterConfigProto.Disk.Component]
            kGroot: _ClassVar[ClusterConfigProto.Disk.Component]
            kAthena: _ClassVar[ClusterConfigProto.Disk.Component]
            kEagleAgent: _ClassVar[ClusterConfigProto.Disk.Component]
            kChunkRepo: _ClassVar[ClusterConfigProto.Disk.Component]
            kCloudChunkRepo: _ClassVar[ClusterConfigProto.Disk.Component]
        kUnknown: ClusterConfigProto.Disk.Component
        kApollo: ClusterConfigProto.Disk.Component
        kScribe: ClusterConfigProto.Disk.Component
        kHydra: ClusterConfigProto.Disk.Component
        kYoda: ClusterConfigProto.Disk.Component
        kLibrarian: ClusterConfigProto.Disk.Component
        kGroot: ClusterConfigProto.Disk.Component
        kAthena: ClusterConfigProto.Disk.Component
        kEagleAgent: ClusterConfigProto.Disk.Component
        kChunkRepo: ClusterConfigProto.Disk.Component
        kCloudChunkRepo: ClusterConfigProto.Disk.Component
        class ChunkRepoWALLocation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kHomePartition: _ClassVar[ClusterConfigProto.Disk.ChunkRepoWALLocation]
            kDisk: _ClassVar[ClusterConfigProto.Disk.ChunkRepoWALLocation]
            kScribeWAL: _ClassVar[ClusterConfigProto.Disk.ChunkRepoWALLocation]
            kScribeTable: _ClassVar[ClusterConfigProto.Disk.ChunkRepoWALLocation]
        kHomePartition: ClusterConfigProto.Disk.ChunkRepoWALLocation
        kDisk: ClusterConfigProto.Disk.ChunkRepoWALLocation
        kScribeWAL: ClusterConfigProto.Disk.ChunkRepoWALLocation
        kScribeTable: ClusterConfigProto.Disk.ChunkRepoWALLocation
        class AccessMethod(_message.Message):
            __slots__ = ("mount_path", "mount_protocol", "pending_unmount_nodes", "fenced_off_nodes", "migration_timestamp_secs", "vault_id")
            class MountProtocol(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                kLocal: _ClassVar[ClusterConfigProto.Disk.AccessMethod.MountProtocol]
                kNFS: _ClassVar[ClusterConfigProto.Disk.AccessMethod.MountProtocol]
            kLocal: ClusterConfigProto.Disk.AccessMethod.MountProtocol
            kNFS: ClusterConfigProto.Disk.AccessMethod.MountProtocol
            MOUNT_PATH_FIELD_NUMBER: _ClassVar[int]
            MOUNT_PROTOCOL_FIELD_NUMBER: _ClassVar[int]
            PENDING_UNMOUNT_NODES_FIELD_NUMBER: _ClassVar[int]
            FENCED_OFF_NODES_FIELD_NUMBER: _ClassVar[int]
            MIGRATION_TIMESTAMP_SECS_FIELD_NUMBER: _ClassVar[int]
            VAULT_ID_FIELD_NUMBER: _ClassVar[int]
            mount_path: str
            mount_protocol: int
            pending_unmount_nodes: _containers.RepeatedScalarFieldContainer[int]
            fenced_off_nodes: _containers.RepeatedScalarFieldContainer[int]
            migration_timestamp_secs: int
            vault_id: int
            def __init__(self, mount_path: _Optional[str] = ..., mount_protocol: _Optional[int] = ..., pending_unmount_nodes: _Optional[_Iterable[int]] = ..., fenced_off_nodes: _Optional[_Iterable[int]] = ..., migration_timestamp_secs: _Optional[int] = ..., vault_id: _Optional[int] = ...) -> None: ...
        class Reservation(_message.Message):
            __slots__ = ("component", "reserved_bytes", "near_full")
            COMPONENT_FIELD_NUMBER: _ClassVar[int]
            RESERVED_BYTES_FIELD_NUMBER: _ClassVar[int]
            NEAR_FULL_FIELD_NUMBER: _ClassVar[int]
            component: ClusterConfigProto.Disk.Component
            reserved_bytes: int
            near_full: bool
            def __init__(self, component: _Optional[_Union[ClusterConfigProto.Disk.Component, str]] = ..., reserved_bytes: _Optional[int] = ..., near_full: bool = ...) -> None: ...
        ID_FIELD_NUMBER: _ClassVar[int]
        TIER_FIELD_NUMBER: _ClassVar[int]
        LOCATION_FIELD_NUMBER: _ClassVar[int]
        CURRENT_NODE_ID_FIELD_NUMBER: _ClassVar[int]
        LAST_NODE_ID_FIELD_NUMBER: _ClassVar[int]
        OFFLINE_FIELD_NUMBER: _ClassVar[int]
        MAX_CAPACITY_BYTES_FIELD_NUMBER: _ClassVar[int]
        USABLE_CAPACITY_BYTES_FIELD_NUMBER: _ClassVar[int]
        REMOVAL_STATE_FIELD_NUMBER: _ClassVar[int]
        ACCESS_METHOD_FIELD_NUMBER: _ClassVar[int]
        RESERVATION_VEC_FIELD_NUMBER: _ClassVar[int]
        SERIAL_NUMBER_FIELD_NUMBER: _ClassVar[int]
        KMS_UID_FIELD_NUMBER: _ClassVar[int]
        ENCRYPTION_STATE_FIELD_NUMBER: _ClassVar[int]
        ENCRYPTED_DISK_ENCRYPTION_KEY_FIELD_NUMBER: _ClassVar[int]
        PREVIOUS_ENCRYPTED_DISK_ENCRYPTION_KEY_FIELD_NUMBER: _ClassVar[int]
        PREVIOUS_KMS_UID_FIELD_NUMBER: _ClassVar[int]
        ADMIN_OFFLINE_FIELD_NUMBER: _ClassVar[int]
        CURRENT_CHUNK_REPOSITORY_WAL_LOCATION_FIELD_NUMBER: _ClassVar[int]
        DESIRED_CHUNK_REPOSITORY_WAL_LOCATION_FIELD_NUMBER: _ClassVar[int]
        CHUNK_REPO_WAL_INCARNATION_FIELD_NUMBER: _ClassVar[int]
        DISK_EXCLUSIVE_FOR_COMPONENT_FIELD_NUMBER: _ClassVar[int]
        SELF_FAULT_TOLERANT_FIELD_NUMBER: _ClassVar[int]
        ALL_NODES_REACHABLE_FIELD_NUMBER: _ClassVar[int]
        id: int
        tier: str
        location: bytes
        current_node_id: int
        last_node_id: int
        offline: bool
        max_capacity_bytes: int
        usable_capacity_bytes: int
        removal_state: ClusterConfigProto.RemovalState
        access_method: ClusterConfigProto.Disk.AccessMethod
        reservation_vec: _containers.RepeatedCompositeFieldContainer[ClusterConfigProto.Disk.Reservation]
        serial_number: str
        kms_uid: bytes
        encryption_state: int
        encrypted_disk_encryption_key: bytes
        previous_encrypted_disk_encryption_key: bytes
        previous_kms_uid: bytes
        admin_offline: bool
        current_chunk_repository_wal_location: ClusterConfigProto.Disk.ChunkRepoWALLocation
        desired_chunk_repository_wal_location: ClusterConfigProto.Disk.ChunkRepoWALLocation
        chunk_repo_wal_incarnation: int
        disk_exclusive_for_component: ClusterConfigProto.Disk.Component
        self_fault_tolerant: bool
        all_nodes_reachable: bool
        def __init__(self, id: _Optional[int] = ..., tier: _Optional[str] = ..., location: _Optional[bytes] = ..., current_node_id: _Optional[int] = ..., last_node_id: _Optional[int] = ..., offline: bool = ..., max_capacity_bytes: _Optional[int] = ..., usable_capacity_bytes: _Optional[int] = ..., removal_state: _Optional[_Union[ClusterConfigProto.RemovalState, _Mapping]] = ..., access_method: _Optional[_Union[ClusterConfigProto.Disk.AccessMethod, _Mapping]] = ..., reservation_vec: _Optional[_Iterable[_Union[ClusterConfigProto.Disk.Reservation, _Mapping]]] = ..., serial_number: _Optional[str] = ..., kms_uid: _Optional[bytes] = ..., encryption_state: _Optional[int] = ..., encrypted_disk_encryption_key: _Optional[bytes] = ..., previous_encrypted_disk_encryption_key: _Optional[bytes] = ..., previous_kms_uid: _Optional[bytes] = ..., admin_offline: bool = ..., current_chunk_repository_wal_location: _Optional[_Union[ClusterConfigProto.Disk.ChunkRepoWALLocation, str]] = ..., desired_chunk_repository_wal_location: _Optional[_Union[ClusterConfigProto.Disk.ChunkRepoWALLocation, str]] = ..., chunk_repo_wal_incarnation: _Optional[int] = ..., disk_exclusive_for_component: _Optional[_Union[ClusterConfigProto.Disk.Component, str]] = ..., self_fault_tolerant: bool = ..., all_nodes_reachable: bool = ...) -> None: ...
    class Rack(_message.Message):
        __slots__ = ("name", "id", "location")
        NAME_FIELD_NUMBER: _ClassVar[int]
        ID_FIELD_NUMBER: _ClassVar[int]
        LOCATION_FIELD_NUMBER: _ClassVar[int]
        name: str
        id: int
        location: bytes
        def __init__(self, name: _Optional[str] = ..., id: _Optional[int] = ..., location: _Optional[bytes] = ...) -> None: ...
    class Chassis(_message.Message):
        __slots__ = ("serial", "id", "rack_id", "location", "hardware_model", "chassis_node_base", "name")
        SERIAL_FIELD_NUMBER: _ClassVar[int]
        ID_FIELD_NUMBER: _ClassVar[int]
        RACK_ID_FIELD_NUMBER: _ClassVar[int]
        LOCATION_FIELD_NUMBER: _ClassVar[int]
        HARDWARE_MODEL_FIELD_NUMBER: _ClassVar[int]
        CHASSIS_NODE_BASE_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        serial: str
        id: int
        rack_id: int
        location: bytes
        hardware_model: str
        chassis_node_base: int
        name: str
        def __init__(self, serial: _Optional[str] = ..., id: _Optional[int] = ..., rack_id: _Optional[int] = ..., location: _Optional[bytes] = ..., hardware_model: _Optional[str] = ..., chassis_node_base: _Optional[int] = ..., name: _Optional[str] = ...) -> None: ...
    class Node(_message.Message):
        __slots__ = ("id", "cluster_partition_id", "cluster_sub_partition_id", "chassis_id", "location", "removal_state", "remove_from_cluster", "ip", "uses_dhcp", "bridge_constituent_id", "bridge_proxy_constituent_id", "storage_proxy_constituent_id", "icebox_constituent_id", "magneto_constituent_id", "atom_constituent_id", "software_version", "node_incarnation_id", "ipmi_ip", "remote_vip", "hardware_model", "link_local_ip", "serial_number", "cluster_node_index", "slot_number", "node_interface_vec", "node_config_proto", "is_restart_services_done", "initiator_iqn", "product_model", "uuid", "system_disk_vec", "hydra_default_disk_id", "hostname", "ipmi_user", "ipmi_network", "total_memory_bytes", "total_cpu_millicores", "apps_reserved_cpu_pct", "apps_reserved_memory_pct", "node_fc_port_vec", "cohesity_serial_number", "in_maintenance_mode", "base_os_version", "active_ca_cert_id", "target_ca_cert_id", "active_node_cert_id", "active_ca_cert_ids", "secured_shell_enabled", "append_cluster_ca_with_rootca", "started_secure_https_rest_server", "started_limited_expansion_handlers_server", "switched_nexus_clients_to_be_secure", "upgrade_checks_status", "upgrade_checks_error", "node_target_ssh_private_key_md5sum", "node_active_ssh_private_key_md5sum", "is_upgrade_in_progress", "restart_go_services_after_upgrade", "upgrade_transaction_id")
        class UpgradeChecksStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kDefault: _ClassVar[ClusterConfigProto.Node.UpgradeChecksStatus]
            kRequested: _ClassVar[ClusterConfigProto.Node.UpgradeChecksStatus]
            kRunning: _ClassVar[ClusterConfigProto.Node.UpgradeChecksStatus]
            kCompleted: _ClassVar[ClusterConfigProto.Node.UpgradeChecksStatus]
        kDefault: ClusterConfigProto.Node.UpgradeChecksStatus
        kRequested: ClusterConfigProto.Node.UpgradeChecksStatus
        kRunning: ClusterConfigProto.Node.UpgradeChecksStatus
        kCompleted: ClusterConfigProto.Node.UpgradeChecksStatus
        class SystemDiskFsUuid(_message.Message):
            __slots__ = ("boot_uuid", "root_uuid", "spare_uuid")
            BOOT_UUID_FIELD_NUMBER: _ClassVar[int]
            ROOT_UUID_FIELD_NUMBER: _ClassVar[int]
            SPARE_UUID_FIELD_NUMBER: _ClassVar[int]
            boot_uuid: str
            root_uuid: str
            spare_uuid: str
            def __init__(self, boot_uuid: _Optional[str] = ..., root_uuid: _Optional[str] = ..., spare_uuid: _Optional[str] = ...) -> None: ...
        class SystemDisk(_message.Message):
            __slots__ = ("id", "location", "current_node_id", "offline", "device_path", "serial_number", "disk_type")
            ID_FIELD_NUMBER: _ClassVar[int]
            LOCATION_FIELD_NUMBER: _ClassVar[int]
            CURRENT_NODE_ID_FIELD_NUMBER: _ClassVar[int]
            OFFLINE_FIELD_NUMBER: _ClassVar[int]
            DEVICE_PATH_FIELD_NUMBER: _ClassVar[int]
            SERIAL_NUMBER_FIELD_NUMBER: _ClassVar[int]
            DISK_TYPE_FIELD_NUMBER: _ClassVar[int]
            id: int
            location: str
            current_node_id: int
            offline: bool
            device_path: str
            serial_number: str
            disk_type: str
            def __init__(self, id: _Optional[int] = ..., location: _Optional[str] = ..., current_node_id: _Optional[int] = ..., offline: bool = ..., device_path: _Optional[str] = ..., serial_number: _Optional[str] = ..., disk_type: _Optional[str] = ...) -> None: ...
        class IpmiUser(_message.Message):
            __slots__ = ("username", "password")
            USERNAME_FIELD_NUMBER: _ClassVar[int]
            PASSWORD_FIELD_NUMBER: _ClassVar[int]
            username: str
            password: bytes
            def __init__(self, username: _Optional[str] = ..., password: _Optional[bytes] = ...) -> None: ...
        class IpmiNetwork(_message.Message):
            __slots__ = ("subnet", "gateway")
            SUBNET_FIELD_NUMBER: _ClassVar[int]
            GATEWAY_FIELD_NUMBER: _ClassVar[int]
            subnet: ClusterConfigProto.Subnet
            gateway: str
            def __init__(self, subnet: _Optional[_Union[ClusterConfigProto.Subnet, _Mapping]] = ..., gateway: _Optional[str] = ...) -> None: ...
        ID_FIELD_NUMBER: _ClassVar[int]
        CLUSTER_PARTITION_ID_FIELD_NUMBER: _ClassVar[int]
        CLUSTER_SUB_PARTITION_ID_FIELD_NUMBER: _ClassVar[int]
        CHASSIS_ID_FIELD_NUMBER: _ClassVar[int]
        LOCATION_FIELD_NUMBER: _ClassVar[int]
        REMOVAL_STATE_FIELD_NUMBER: _ClassVar[int]
        REMOVE_FROM_CLUSTER_FIELD_NUMBER: _ClassVar[int]
        IP_FIELD_NUMBER: _ClassVar[int]
        USES_DHCP_FIELD_NUMBER: _ClassVar[int]
        BRIDGE_CONSTITUENT_ID_FIELD_NUMBER: _ClassVar[int]
        BRIDGE_PROXY_CONSTITUENT_ID_FIELD_NUMBER: _ClassVar[int]
        STORAGE_PROXY_CONSTITUENT_ID_FIELD_NUMBER: _ClassVar[int]
        ICEBOX_CONSTITUENT_ID_FIELD_NUMBER: _ClassVar[int]
        MAGNETO_CONSTITUENT_ID_FIELD_NUMBER: _ClassVar[int]
        ATOM_CONSTITUENT_ID_FIELD_NUMBER: _ClassVar[int]
        SOFTWARE_VERSION_FIELD_NUMBER: _ClassVar[int]
        NODE_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
        IPMI_IP_FIELD_NUMBER: _ClassVar[int]
        REMOTE_VIP_FIELD_NUMBER: _ClassVar[int]
        HARDWARE_MODEL_FIELD_NUMBER: _ClassVar[int]
        LINK_LOCAL_IP_FIELD_NUMBER: _ClassVar[int]
        SERIAL_NUMBER_FIELD_NUMBER: _ClassVar[int]
        CLUSTER_NODE_INDEX_FIELD_NUMBER: _ClassVar[int]
        SLOT_NUMBER_FIELD_NUMBER: _ClassVar[int]
        NODE_INTERFACE_VEC_FIELD_NUMBER: _ClassVar[int]
        NODE_CONFIG_PROTO_FIELD_NUMBER: _ClassVar[int]
        IS_RESTART_SERVICES_DONE_FIELD_NUMBER: _ClassVar[int]
        INITIATOR_IQN_FIELD_NUMBER: _ClassVar[int]
        PRODUCT_MODEL_FIELD_NUMBER: _ClassVar[int]
        UUID_FIELD_NUMBER: _ClassVar[int]
        SYSTEM_DISK_VEC_FIELD_NUMBER: _ClassVar[int]
        HYDRA_DEFAULT_DISK_ID_FIELD_NUMBER: _ClassVar[int]
        HOSTNAME_FIELD_NUMBER: _ClassVar[int]
        IPMI_USER_FIELD_NUMBER: _ClassVar[int]
        IPMI_NETWORK_FIELD_NUMBER: _ClassVar[int]
        TOTAL_MEMORY_BYTES_FIELD_NUMBER: _ClassVar[int]
        TOTAL_CPU_MILLICORES_FIELD_NUMBER: _ClassVar[int]
        APPS_RESERVED_CPU_PCT_FIELD_NUMBER: _ClassVar[int]
        APPS_RESERVED_MEMORY_PCT_FIELD_NUMBER: _ClassVar[int]
        NODE_FC_PORT_VEC_FIELD_NUMBER: _ClassVar[int]
        COHESITY_SERIAL_NUMBER_FIELD_NUMBER: _ClassVar[int]
        IN_MAINTENANCE_MODE_FIELD_NUMBER: _ClassVar[int]
        BASE_OS_VERSION_FIELD_NUMBER: _ClassVar[int]
        ACTIVE_CA_CERT_ID_FIELD_NUMBER: _ClassVar[int]
        TARGET_CA_CERT_ID_FIELD_NUMBER: _ClassVar[int]
        ACTIVE_NODE_CERT_ID_FIELD_NUMBER: _ClassVar[int]
        ACTIVE_CA_CERT_IDS_FIELD_NUMBER: _ClassVar[int]
        SECURED_SHELL_ENABLED_FIELD_NUMBER: _ClassVar[int]
        APPEND_CLUSTER_CA_WITH_ROOTCA_FIELD_NUMBER: _ClassVar[int]
        STARTED_SECURE_HTTPS_REST_SERVER_FIELD_NUMBER: _ClassVar[int]
        STARTED_LIMITED_EXPANSION_HANDLERS_SERVER_FIELD_NUMBER: _ClassVar[int]
        SWITCHED_NEXUS_CLIENTS_TO_BE_SECURE_FIELD_NUMBER: _ClassVar[int]
        UPGRADE_CHECKS_STATUS_FIELD_NUMBER: _ClassVar[int]
        UPGRADE_CHECKS_ERROR_FIELD_NUMBER: _ClassVar[int]
        NODE_TARGET_SSH_PRIVATE_KEY_MD5SUM_FIELD_NUMBER: _ClassVar[int]
        NODE_ACTIVE_SSH_PRIVATE_KEY_MD5SUM_FIELD_NUMBER: _ClassVar[int]
        IS_UPGRADE_IN_PROGRESS_FIELD_NUMBER: _ClassVar[int]
        RESTART_GO_SERVICES_AFTER_UPGRADE_FIELD_NUMBER: _ClassVar[int]
        UPGRADE_TRANSACTION_ID_FIELD_NUMBER: _ClassVar[int]
        id: int
        cluster_partition_id: int
        cluster_sub_partition_id: int
        chassis_id: int
        location: bytes
        removal_state: ClusterConfigProto.RemovalState
        remove_from_cluster: bool
        ip: str
        uses_dhcp: bool
        bridge_constituent_id: int
        bridge_proxy_constituent_id: int
        storage_proxy_constituent_id: int
        icebox_constituent_id: int
        magneto_constituent_id: int
        atom_constituent_id: int
        software_version: str
        node_incarnation_id: int
        ipmi_ip: str
        remote_vip: str
        hardware_model: str
        link_local_ip: str
        serial_number: str
        cluster_node_index: int
        slot_number: int
        node_interface_vec: _containers.RepeatedCompositeFieldContainer[ClusterConfigProto.NetworkInterface]
        node_config_proto: _node_config_pb2.NodeConfigProto
        is_restart_services_done: bool
        initiator_iqn: str
        product_model: ClusterConfigProto.ProductModel
        uuid: ClusterConfigProto.Node.SystemDiskFsUuid
        system_disk_vec: _containers.RepeatedCompositeFieldContainer[ClusterConfigProto.Node.SystemDisk]
        hydra_default_disk_id: int
        hostname: str
        ipmi_user: ClusterConfigProto.Node.IpmiUser
        ipmi_network: ClusterConfigProto.Node.IpmiNetwork
        total_memory_bytes: int
        total_cpu_millicores: int
        apps_reserved_cpu_pct: int
        apps_reserved_memory_pct: int
        node_fc_port_vec: _containers.RepeatedCompositeFieldContainer[ClusterConfigProto.FibreChannelPort]
        cohesity_serial_number: str
        in_maintenance_mode: bool
        base_os_version: int
        active_ca_cert_id: int
        target_ca_cert_id: int
        active_node_cert_id: int
        active_ca_cert_ids: _containers.RepeatedScalarFieldContainer[int]
        secured_shell_enabled: bool
        append_cluster_ca_with_rootca: bool
        started_secure_https_rest_server: bool
        started_limited_expansion_handlers_server: bool
        switched_nexus_clients_to_be_secure: bool
        upgrade_checks_status: ClusterConfigProto.Node.UpgradeChecksStatus
        upgrade_checks_error: str
        node_target_ssh_private_key_md5sum: str
        node_active_ssh_private_key_md5sum: str
        is_upgrade_in_progress: bool
        restart_go_services_after_upgrade: bool
        upgrade_transaction_id: int
        def __init__(self, id: _Optional[int] = ..., cluster_partition_id: _Optional[int] = ..., cluster_sub_partition_id: _Optional[int] = ..., chassis_id: _Optional[int] = ..., location: _Optional[bytes] = ..., removal_state: _Optional[_Union[ClusterConfigProto.RemovalState, _Mapping]] = ..., remove_from_cluster: bool = ..., ip: _Optional[str] = ..., uses_dhcp: bool = ..., bridge_constituent_id: _Optional[int] = ..., bridge_proxy_constituent_id: _Optional[int] = ..., storage_proxy_constituent_id: _Optional[int] = ..., icebox_constituent_id: _Optional[int] = ..., magneto_constituent_id: _Optional[int] = ..., atom_constituent_id: _Optional[int] = ..., software_version: _Optional[str] = ..., node_incarnation_id: _Optional[int] = ..., ipmi_ip: _Optional[str] = ..., remote_vip: _Optional[str] = ..., hardware_model: _Optional[str] = ..., link_local_ip: _Optional[str] = ..., serial_number: _Optional[str] = ..., cluster_node_index: _Optional[int] = ..., slot_number: _Optional[int] = ..., node_interface_vec: _Optional[_Iterable[_Union[ClusterConfigProto.NetworkInterface, _Mapping]]] = ..., node_config_proto: _Optional[_Union[_node_config_pb2.NodeConfigProto, _Mapping]] = ..., is_restart_services_done: bool = ..., initiator_iqn: _Optional[str] = ..., product_model: _Optional[_Union[ClusterConfigProto.ProductModel, str]] = ..., uuid: _Optional[_Union[ClusterConfigProto.Node.SystemDiskFsUuid, _Mapping]] = ..., system_disk_vec: _Optional[_Iterable[_Union[ClusterConfigProto.Node.SystemDisk, _Mapping]]] = ..., hydra_default_disk_id: _Optional[int] = ..., hostname: _Optional[str] = ..., ipmi_user: _Optional[_Union[ClusterConfigProto.Node.IpmiUser, _Mapping]] = ..., ipmi_network: _Optional[_Union[ClusterConfigProto.Node.IpmiNetwork, _Mapping]] = ..., total_memory_bytes: _Optional[int] = ..., total_cpu_millicores: _Optional[int] = ..., apps_reserved_cpu_pct: _Optional[int] = ..., apps_reserved_memory_pct: _Optional[int] = ..., node_fc_port_vec: _Optional[_Iterable[_Union[ClusterConfigProto.FibreChannelPort, _Mapping]]] = ..., cohesity_serial_number: _Optional[str] = ..., in_maintenance_mode: bool = ..., base_os_version: _Optional[int] = ..., active_ca_cert_id: _Optional[int] = ..., target_ca_cert_id: _Optional[int] = ..., active_node_cert_id: _Optional[int] = ..., active_ca_cert_ids: _Optional[_Iterable[int]] = ..., secured_shell_enabled: bool = ..., append_cluster_ca_with_rootca: bool = ..., started_secure_https_rest_server: bool = ..., started_limited_expansion_handlers_server: bool = ..., switched_nexus_clients_to_be_secure: bool = ..., upgrade_checks_status: _Optional[_Union[ClusterConfigProto.Node.UpgradeChecksStatus, str]] = ..., upgrade_checks_error: _Optional[str] = ..., node_target_ssh_private_key_md5sum: _Optional[str] = ..., node_active_ssh_private_key_md5sum: _Optional[str] = ..., is_upgrade_in_progress: bool = ..., restart_go_services_after_upgrade: bool = ..., upgrade_transaction_id: _Optional[int] = ...) -> None: ...
    class ClusterSubPartition(_message.Message):
        __slots__ = ("name", "id", "virtual_ip_vec", "magneto_enabled")
        NAME_FIELD_NUMBER: _ClassVar[int]
        ID_FIELD_NUMBER: _ClassVar[int]
        VIRTUAL_IP_VEC_FIELD_NUMBER: _ClassVar[int]
        MAGNETO_ENABLED_FIELD_NUMBER: _ClassVar[int]
        name: str
        id: int
        virtual_ip_vec: _containers.RepeatedScalarFieldContainer[str]
        magneto_enabled: bool
        def __init__(self, name: _Optional[str] = ..., id: _Optional[int] = ..., virtual_ip_vec: _Optional[_Iterable[str]] = ..., magneto_enabled: bool = ...) -> None: ...
    class ClusterPartition(_message.Message):
        __slots__ = ("name", "id", "removal_state", "virtual_ip_vec", "host_name", "cluster_sub_partition_vec", "vlan_ip_vec", "partition_vips_disabled")
        NAME_FIELD_NUMBER: _ClassVar[int]
        ID_FIELD_NUMBER: _ClassVar[int]
        REMOVAL_STATE_FIELD_NUMBER: _ClassVar[int]
        VIRTUAL_IP_VEC_FIELD_NUMBER: _ClassVar[int]
        HOST_NAME_FIELD_NUMBER: _ClassVar[int]
        CLUSTER_SUB_PARTITION_VEC_FIELD_NUMBER: _ClassVar[int]
        VLAN_IP_VEC_FIELD_NUMBER: _ClassVar[int]
        PARTITION_VIPS_DISABLED_FIELD_NUMBER: _ClassVar[int]
        name: str
        id: int
        removal_state: ClusterConfigProto.RemovalState
        virtual_ip_vec: _containers.RepeatedScalarFieldContainer[str]
        host_name: str
        cluster_sub_partition_vec: _containers.RepeatedCompositeFieldContainer[ClusterConfigProto.ClusterSubPartition]
        vlan_ip_vec: _containers.RepeatedScalarFieldContainer[str]
        partition_vips_disabled: bool
        def __init__(self, name: _Optional[str] = ..., id: _Optional[int] = ..., removal_state: _Optional[_Union[ClusterConfigProto.RemovalState, _Mapping]] = ..., virtual_ip_vec: _Optional[_Iterable[str]] = ..., host_name: _Optional[str] = ..., cluster_sub_partition_vec: _Optional[_Iterable[_Union[ClusterConfigProto.ClusterSubPartition, _Mapping]]] = ..., vlan_ip_vec: _Optional[_Iterable[str]] = ..., partition_vips_disabled: bool = ...) -> None: ...
    class StoragePolicy(_message.Message):
        __slots__ = ("deduplicate", "compression_level", "deduplicate_compress_delay_secs", "min_dedup_chunk_size", "max_dedup_chunk_size", "non_dedup_chunk_size", "encryption_level", "replica_count", "ec_info", "erasure_code_delay_secs", "down_waterfall_threshold_secs", "defrag_chunk_file_threshold_pct", "defrag_chunk_file_delay_secs", "cloud_spill_vault_id", "inline_compress", "inline_deduplicate", "chunkgroup_size", "erasure_coded_chunkgroup_size", "fault_tolerance", "fault_tolerance_factor", "app_marker_detection", "fixed_offset_deduplicate", "fixed_dedup_chunk_size")
        class CompressionLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kCompressionNone: _ClassVar[ClusterConfigProto.StoragePolicy.CompressionLevel]
            kCompressionLow: _ClassVar[ClusterConfigProto.StoragePolicy.CompressionLevel]
            kCompressionHigh: _ClassVar[ClusterConfigProto.StoragePolicy.CompressionLevel]
            kCompressionSnappy: _ClassVar[ClusterConfigProto.StoragePolicy.CompressionLevel]
            kCompressionGZip: _ClassVar[ClusterConfigProto.StoragePolicy.CompressionLevel]
            kCompressionLZ4: _ClassVar[ClusterConfigProto.StoragePolicy.CompressionLevel]
            kCompressionZSTDLow: _ClassVar[ClusterConfigProto.StoragePolicy.CompressionLevel]
            kCompressionZSTDHigh: _ClassVar[ClusterConfigProto.StoragePolicy.CompressionLevel]
        kCompressionNone: ClusterConfigProto.StoragePolicy.CompressionLevel
        kCompressionLow: ClusterConfigProto.StoragePolicy.CompressionLevel
        kCompressionHigh: ClusterConfigProto.StoragePolicy.CompressionLevel
        kCompressionSnappy: ClusterConfigProto.StoragePolicy.CompressionLevel
        kCompressionGZip: ClusterConfigProto.StoragePolicy.CompressionLevel
        kCompressionLZ4: ClusterConfigProto.StoragePolicy.CompressionLevel
        kCompressionZSTDLow: ClusterConfigProto.StoragePolicy.CompressionLevel
        kCompressionZSTDHigh: ClusterConfigProto.StoragePolicy.CompressionLevel
        class ECInfo(_message.Message):
            __slots__ = ("ec_algo", "num_data_stripes", "num_coded_stripes", "use_container")
            class ECAlgo(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                REED_SOLOMON: _ClassVar[ClusterConfigProto.StoragePolicy.ECInfo.ECAlgo]
                LRC: _ClassVar[ClusterConfigProto.StoragePolicy.ECInfo.ECAlgo]
            REED_SOLOMON: ClusterConfigProto.StoragePolicy.ECInfo.ECAlgo
            LRC: ClusterConfigProto.StoragePolicy.ECInfo.ECAlgo
            EC_ALGO_FIELD_NUMBER: _ClassVar[int]
            NUM_DATA_STRIPES_FIELD_NUMBER: _ClassVar[int]
            NUM_CODED_STRIPES_FIELD_NUMBER: _ClassVar[int]
            USE_CONTAINER_FIELD_NUMBER: _ClassVar[int]
            ec_algo: ClusterConfigProto.StoragePolicy.ECInfo.ECAlgo
            num_data_stripes: int
            num_coded_stripes: int
            use_container: bool
            def __init__(self, ec_algo: _Optional[_Union[ClusterConfigProto.StoragePolicy.ECInfo.ECAlgo, str]] = ..., num_data_stripes: _Optional[int] = ..., num_coded_stripes: _Optional[int] = ..., use_container: bool = ...) -> None: ...
        DEDUPLICATE_FIELD_NUMBER: _ClassVar[int]
        COMPRESSION_LEVEL_FIELD_NUMBER: _ClassVar[int]
        DEDUPLICATE_COMPRESS_DELAY_SECS_FIELD_NUMBER: _ClassVar[int]
        MIN_DEDUP_CHUNK_SIZE_FIELD_NUMBER: _ClassVar[int]
        MAX_DEDUP_CHUNK_SIZE_FIELD_NUMBER: _ClassVar[int]
        NON_DEDUP_CHUNK_SIZE_FIELD_NUMBER: _ClassVar[int]
        ENCRYPTION_LEVEL_FIELD_NUMBER: _ClassVar[int]
        REPLICA_COUNT_FIELD_NUMBER: _ClassVar[int]
        EC_INFO_FIELD_NUMBER: _ClassVar[int]
        ERASURE_CODE_DELAY_SECS_FIELD_NUMBER: _ClassVar[int]
        DOWN_WATERFALL_THRESHOLD_SECS_FIELD_NUMBER: _ClassVar[int]
        DEFRAG_CHUNK_FILE_THRESHOLD_PCT_FIELD_NUMBER: _ClassVar[int]
        DEFRAG_CHUNK_FILE_DELAY_SECS_FIELD_NUMBER: _ClassVar[int]
        CLOUD_SPILL_VAULT_ID_FIELD_NUMBER: _ClassVar[int]
        INLINE_COMPRESS_FIELD_NUMBER: _ClassVar[int]
        INLINE_DEDUPLICATE_FIELD_NUMBER: _ClassVar[int]
        CHUNKGROUP_SIZE_FIELD_NUMBER: _ClassVar[int]
        ERASURE_CODED_CHUNKGROUP_SIZE_FIELD_NUMBER: _ClassVar[int]
        FAULT_TOLERANCE_FIELD_NUMBER: _ClassVar[int]
        FAULT_TOLERANCE_FACTOR_FIELD_NUMBER: _ClassVar[int]
        APP_MARKER_DETECTION_FIELD_NUMBER: _ClassVar[int]
        FIXED_OFFSET_DEDUPLICATE_FIELD_NUMBER: _ClassVar[int]
        FIXED_DEDUP_CHUNK_SIZE_FIELD_NUMBER: _ClassVar[int]
        deduplicate: bool
        compression_level: ClusterConfigProto.StoragePolicy.CompressionLevel
        deduplicate_compress_delay_secs: int
        min_dedup_chunk_size: int
        max_dedup_chunk_size: int
        non_dedup_chunk_size: int
        encryption_level: ClusterConfigProto.EncryptionLevel
        replica_count: int
        ec_info: ClusterConfigProto.StoragePolicy.ECInfo
        erasure_code_delay_secs: int
        down_waterfall_threshold_secs: _containers.RepeatedScalarFieldContainer[int]
        defrag_chunk_file_threshold_pct: int
        defrag_chunk_file_delay_secs: int
        cloud_spill_vault_id: int
        inline_compress: bool
        inline_deduplicate: bool
        chunkgroup_size: int
        erasure_coded_chunkgroup_size: int
        fault_tolerance: ClusterConfigProto.FaultToleranceStrictness
        fault_tolerance_factor: int
        app_marker_detection: bool
        fixed_offset_deduplicate: bool
        fixed_dedup_chunk_size: int
        def __init__(self, deduplicate: bool = ..., compression_level: _Optional[_Union[ClusterConfigProto.StoragePolicy.CompressionLevel, str]] = ..., deduplicate_compress_delay_secs: _Optional[int] = ..., min_dedup_chunk_size: _Optional[int] = ..., max_dedup_chunk_size: _Optional[int] = ..., non_dedup_chunk_size: _Optional[int] = ..., encryption_level: _Optional[_Union[ClusterConfigProto.EncryptionLevel, str]] = ..., replica_count: _Optional[int] = ..., ec_info: _Optional[_Union[ClusterConfigProto.StoragePolicy.ECInfo, _Mapping]] = ..., erasure_code_delay_secs: _Optional[int] = ..., down_waterfall_threshold_secs: _Optional[_Iterable[int]] = ..., defrag_chunk_file_threshold_pct: _Optional[int] = ..., defrag_chunk_file_delay_secs: _Optional[int] = ..., cloud_spill_vault_id: _Optional[int] = ..., inline_compress: bool = ..., inline_deduplicate: bool = ..., chunkgroup_size: _Optional[int] = ..., erasure_coded_chunkgroup_size: _Optional[int] = ..., fault_tolerance: _Optional[_Union[ClusterConfigProto.FaultToleranceStrictness, _Mapping]] = ..., fault_tolerance_factor: _Optional[int] = ..., app_marker_detection: bool = ..., fixed_offset_deduplicate: bool = ..., fixed_dedup_chunk_size: _Optional[int] = ...) -> None: ...
    class StoragePolicyOverride(_message.Message):
        __slots__ = ("disable_inline_dedup_and_compression", "disable_dedup")
        DISABLE_INLINE_DEDUP_AND_COMPRESSION_FIELD_NUMBER: _ClassVar[int]
        DISABLE_DEDUP_FIELD_NUMBER: _ClassVar[int]
        disable_inline_dedup_and_compression: bool
        disable_dedup: bool
        def __init__(self, disable_inline_dedup_and_compression: bool = ..., disable_dedup: bool = ...) -> None: ...
    class QuotaPolicy(_message.Message):
        __slots__ = ("hard_limit_bytes", "alert_limit_bytes", "alert_threshold_percentage")
        HARD_LIMIT_BYTES_FIELD_NUMBER: _ClassVar[int]
        ALERT_LIMIT_BYTES_FIELD_NUMBER: _ClassVar[int]
        ALERT_THRESHOLD_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
        hard_limit_bytes: int
        alert_limit_bytes: int
        alert_threshold_percentage: int
        def __init__(self, hard_limit_bytes: _Optional[int] = ..., alert_limit_bytes: _Optional[int] = ..., alert_threshold_percentage: _Optional[int] = ...) -> None: ...
    class ViewBox(_message.Message):
        __slots__ = ("name", "id", "storage_policy", "cluster_partition_id", "removal_state", "client_subnet_whitelist", "opclock_vec", "brick_size", "updated_brick_size", "yoda_internal", "treat_file_sync_as_data_sync", "kms_uid", "encrypted_data_encryption_key", "physical_quota", "default_view_quota_policy", "default_user_quota_policy", "s3_buckets_allowed", "audit_log_internal", "ad_domain_dns_name", "is_default_mmc_share", "tenant_id_vec", "ldap_provider_id", "athena_internal", "down_waterfall_threshold_pct", "helios_internal", "direct_archive_enabled", "nis_domain_name_vec", "kms_server_id", "dek_rotation_enabled", "fixed_dek_key_id", "current_dek_key_id", "cloud_domain_id", "kerberos_realm_name", "aux_view_box_vec", "icebox_internal", "apollo_internal", "checksum_algorithm")
        class ChecksumAlgorithm(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kSha1: _ClassVar[ClusterConfigProto.ViewBox.ChecksumAlgorithm]
            kSha256: _ClassVar[ClusterConfigProto.ViewBox.ChecksumAlgorithm]
        kSha1: ClusterConfigProto.ViewBox.ChecksumAlgorithm
        kSha256: ClusterConfigProto.ViewBox.ChecksumAlgorithm
        class AuxiliaryViewBoxInfo(_message.Message):
            __slots__ = ("view_box_id", "type")
            class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                kMetadataViewBox: _ClassVar[ClusterConfigProto.ViewBox.AuxiliaryViewBoxInfo.Type]
            kMetadataViewBox: ClusterConfigProto.ViewBox.AuxiliaryViewBoxInfo.Type
            VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
            TYPE_FIELD_NUMBER: _ClassVar[int]
            view_box_id: int
            type: ClusterConfigProto.ViewBox.AuxiliaryViewBoxInfo.Type
            def __init__(self, view_box_id: _Optional[int] = ..., type: _Optional[_Union[ClusterConfigProto.ViewBox.AuxiliaryViewBoxInfo.Type, str]] = ...) -> None: ...
        NAME_FIELD_NUMBER: _ClassVar[int]
        ID_FIELD_NUMBER: _ClassVar[int]
        STORAGE_POLICY_FIELD_NUMBER: _ClassVar[int]
        CLUSTER_PARTITION_ID_FIELD_NUMBER: _ClassVar[int]
        REMOVAL_STATE_FIELD_NUMBER: _ClassVar[int]
        CLIENT_SUBNET_WHITELIST_FIELD_NUMBER: _ClassVar[int]
        OPCLOCK_VEC_FIELD_NUMBER: _ClassVar[int]
        BRICK_SIZE_FIELD_NUMBER: _ClassVar[int]
        UPDATED_BRICK_SIZE_FIELD_NUMBER: _ClassVar[int]
        YODA_INTERNAL_FIELD_NUMBER: _ClassVar[int]
        TREAT_FILE_SYNC_AS_DATA_SYNC_FIELD_NUMBER: _ClassVar[int]
        KMS_UID_FIELD_NUMBER: _ClassVar[int]
        ENCRYPTED_DATA_ENCRYPTION_KEY_FIELD_NUMBER: _ClassVar[int]
        PHYSICAL_QUOTA_FIELD_NUMBER: _ClassVar[int]
        DEFAULT_VIEW_QUOTA_POLICY_FIELD_NUMBER: _ClassVar[int]
        DEFAULT_USER_QUOTA_POLICY_FIELD_NUMBER: _ClassVar[int]
        S3_BUCKETS_ALLOWED_FIELD_NUMBER: _ClassVar[int]
        AUDIT_LOG_INTERNAL_FIELD_NUMBER: _ClassVar[int]
        AD_DOMAIN_DNS_NAME_FIELD_NUMBER: _ClassVar[int]
        IS_DEFAULT_MMC_SHARE_FIELD_NUMBER: _ClassVar[int]
        TENANT_ID_VEC_FIELD_NUMBER: _ClassVar[int]
        LDAP_PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
        ATHENA_INTERNAL_FIELD_NUMBER: _ClassVar[int]
        DOWN_WATERFALL_THRESHOLD_PCT_FIELD_NUMBER: _ClassVar[int]
        HELIOS_INTERNAL_FIELD_NUMBER: _ClassVar[int]
        DIRECT_ARCHIVE_ENABLED_FIELD_NUMBER: _ClassVar[int]
        NIS_DOMAIN_NAME_VEC_FIELD_NUMBER: _ClassVar[int]
        KMS_SERVER_ID_FIELD_NUMBER: _ClassVar[int]
        DEK_ROTATION_ENABLED_FIELD_NUMBER: _ClassVar[int]
        FIXED_DEK_KEY_ID_FIELD_NUMBER: _ClassVar[int]
        CURRENT_DEK_KEY_ID_FIELD_NUMBER: _ClassVar[int]
        CLOUD_DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
        KERBEROS_REALM_NAME_FIELD_NUMBER: _ClassVar[int]
        AUX_VIEW_BOX_VEC_FIELD_NUMBER: _ClassVar[int]
        ICEBOX_INTERNAL_FIELD_NUMBER: _ClassVar[int]
        APOLLO_INTERNAL_FIELD_NUMBER: _ClassVar[int]
        CHECKSUM_ALGORITHM_FIELD_NUMBER: _ClassVar[int]
        name: str
        id: int
        storage_policy: ClusterConfigProto.StoragePolicy
        cluster_partition_id: int
        removal_state: ClusterConfigProto.RemovalState
        client_subnet_whitelist: _containers.RepeatedCompositeFieldContainer[ClusterConfigProto.Subnet]
        opclock_vec: _containers.RepeatedCompositeFieldContainer[_op_clock_pb2.OpClock]
        brick_size: int
        updated_brick_size: int
        yoda_internal: bool
        treat_file_sync_as_data_sync: bool
        kms_uid: bytes
        encrypted_data_encryption_key: bytes
        physical_quota: ClusterConfigProto.QuotaPolicy
        default_view_quota_policy: ClusterConfigProto.QuotaPolicy
        default_user_quota_policy: ClusterConfigProto.QuotaPolicy
        s3_buckets_allowed: bool
        audit_log_internal: bool
        ad_domain_dns_name: str
        is_default_mmc_share: bool
        tenant_id_vec: _containers.RepeatedScalarFieldContainer[str]
        ldap_provider_id: int
        athena_internal: bool
        down_waterfall_threshold_pct: int
        helios_internal: bool
        direct_archive_enabled: bool
        nis_domain_name_vec: _containers.RepeatedScalarFieldContainer[str]
        kms_server_id: int
        dek_rotation_enabled: bool
        fixed_dek_key_id: int
        current_dek_key_id: int
        cloud_domain_id: int
        kerberos_realm_name: str
        aux_view_box_vec: _containers.RepeatedCompositeFieldContainer[ClusterConfigProto.ViewBox.AuxiliaryViewBoxInfo]
        icebox_internal: bool
        apollo_internal: bool
        checksum_algorithm: ClusterConfigProto.ViewBox.ChecksumAlgorithm
        def __init__(self, name: _Optional[str] = ..., id: _Optional[int] = ..., storage_policy: _Optional[_Union[ClusterConfigProto.StoragePolicy, _Mapping]] = ..., cluster_partition_id: _Optional[int] = ..., removal_state: _Optional[_Union[ClusterConfigProto.RemovalState, _Mapping]] = ..., client_subnet_whitelist: _Optional[_Iterable[_Union[ClusterConfigProto.Subnet, _Mapping]]] = ..., opclock_vec: _Optional[_Iterable[_Union[_op_clock_pb2.OpClock, _Mapping]]] = ..., brick_size: _Optional[int] = ..., updated_brick_size: _Optional[int] = ..., yoda_internal: bool = ..., treat_file_sync_as_data_sync: bool = ..., kms_uid: _Optional[bytes] = ..., encrypted_data_encryption_key: _Optional[bytes] = ..., physical_quota: _Optional[_Union[ClusterConfigProto.QuotaPolicy, _Mapping]] = ..., default_view_quota_policy: _Optional[_Union[ClusterConfigProto.QuotaPolicy, _Mapping]] = ..., default_user_quota_policy: _Optional[_Union[ClusterConfigProto.QuotaPolicy, _Mapping]] = ..., s3_buckets_allowed: bool = ..., audit_log_internal: bool = ..., ad_domain_dns_name: _Optional[str] = ..., is_default_mmc_share: bool = ..., tenant_id_vec: _Optional[_Iterable[str]] = ..., ldap_provider_id: _Optional[int] = ..., athena_internal: bool = ..., down_waterfall_threshold_pct: _Optional[int] = ..., helios_internal: bool = ..., direct_archive_enabled: bool = ..., nis_domain_name_vec: _Optional[_Iterable[str]] = ..., kms_server_id: _Optional[int] = ..., dek_rotation_enabled: bool = ..., fixed_dek_key_id: _Optional[int] = ..., current_dek_key_id: _Optional[int] = ..., cloud_domain_id: _Optional[int] = ..., kerberos_realm_name: _Optional[str] = ..., aux_view_box_vec: _Optional[_Iterable[_Union[ClusterConfigProto.ViewBox.AuxiliaryViewBoxInfo, _Mapping]]] = ..., icebox_internal: bool = ..., apollo_internal: bool = ..., checksum_algorithm: _Optional[_Union[ClusterConfigProto.ViewBox.ChecksumAlgorithm, str]] = ...) -> None: ...
    class Bulletin(_message.Message):
        __slots__ = ("cluster_target_software_version", "service_state", "current_operation", "operation_start_time_secs", "software_package_url", "software_package_checksum", "ignore_sw_incompatibility", "is_parallel_upgrade", "agent_auto_upgrade_requested", "cluster_target_base_os_version", "is_upgrade_cancel_requested", "is_cluster_migration_pending", "upgrade_checks_req_state", "upgrade_req_hc_data", "cluster_current_software_version", "is_upgrade_aborted", "upgrade_failure_error_string", "cluster_target_upgrade_transaction_id")
        class ServiceName(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            invalid: _ClassVar[ClusterConfigProto.Bulletin.ServiceName]
            apollo: _ClassVar[ClusterConfigProto.Bulletin.ServiceName]
            bridge: _ClassVar[ClusterConfigProto.Bulletin.ServiceName]
            genie: _ClassVar[ClusterConfigProto.Bulletin.ServiceName]
            genie_gofer: _ClassVar[ClusterConfigProto.Bulletin.ServiceName]
            magneto: _ClassVar[ClusterConfigProto.Bulletin.ServiceName]
            iris: _ClassVar[ClusterConfigProto.Bulletin.ServiceName]
            iris_proxy: _ClassVar[ClusterConfigProto.Bulletin.ServiceName]
            newscribe: _ClassVar[ClusterConfigProto.Bulletin.ServiceName]
            stats: _ClassVar[ClusterConfigProto.Bulletin.ServiceName]
            yoda: _ClassVar[ClusterConfigProto.Bulletin.ServiceName]
            alerts: _ClassVar[ClusterConfigProto.Bulletin.ServiceName]
            keychain: _ClassVar[ClusterConfigProto.Bulletin.ServiceName]
            logwatcher: _ClassVar[ClusterConfigProto.Bulletin.ServiceName]
            statscollector: _ClassVar[ClusterConfigProto.Bulletin.ServiceName]
            gandalf: _ClassVar[ClusterConfigProto.Bulletin.ServiceName]
            nexus: _ClassVar[ClusterConfigProto.Bulletin.ServiceName]
            nexus_proxy: _ClassVar[ClusterConfigProto.Bulletin.ServiceName]
            storage_proxy: _ClassVar[ClusterConfigProto.Bulletin.ServiceName]
            tricorder: _ClassVar[ClusterConfigProto.Bulletin.ServiceName]
            rtclient: _ClassVar[ClusterConfigProto.Bulletin.ServiceName]
            vault_proxy: _ClassVar[ClusterConfigProto.Bulletin.ServiceName]
            smb_proxy: _ClassVar[ClusterConfigProto.Bulletin.ServiceName]
            bridge_proxy: _ClassVar[ClusterConfigProto.Bulletin.ServiceName]
            librarian: _ClassVar[ClusterConfigProto.Bulletin.ServiceName]
            groot: _ClassVar[ClusterConfigProto.Bulletin.ServiceName]
            eagle_agent: _ClassVar[ClusterConfigProto.Bulletin.ServiceName]
            athena: _ClassVar[ClusterConfigProto.Bulletin.ServiceName]
            bifrost_broker: _ClassVar[ClusterConfigProto.Bulletin.ServiceName]
            elixir: _ClassVar[ClusterConfigProto.Bulletin.ServiceName]
            vulscan: _ClassVar[ClusterConfigProto.Bulletin.ServiceName]
            postgres: _ClassVar[ClusterConfigProto.Bulletin.ServiceName]
            atom: _ClassVar[ClusterConfigProto.Bulletin.ServiceName]
            yoda_agent: _ClassVar[ClusterConfigProto.Bulletin.ServiceName]
            smb2_proxy: _ClassVar[ClusterConfigProto.Bulletin.ServiceName]
            throttler: _ClassVar[ClusterConfigProto.Bulletin.ServiceName]
            kafka: _ClassVar[ClusterConfigProto.Bulletin.ServiceName]
            eventing: _ClassVar[ClusterConfigProto.Bulletin.ServiceName]
            agentinstall: _ClassVar[ClusterConfigProto.Bulletin.ServiceName]
            imanis: _ClassVar[ClusterConfigProto.Bulletin.ServiceName]
            elrond: _ClassVar[ClusterConfigProto.Bulletin.ServiceName]
            heimdall: _ClassVar[ClusterConfigProto.Bulletin.ServiceName]
            bifrost: _ClassVar[ClusterConfigProto.Bulletin.ServiceName]
            icebox: _ClassVar[ClusterConfigProto.Bulletin.ServiceName]
            node_exporter: _ClassVar[ClusterConfigProto.Bulletin.ServiceName]
            compass: _ClassVar[ClusterConfigProto.Bulletin.ServiceName]
            patch: _ClassVar[ClusterConfigProto.Bulletin.ServiceName]
            etl_server: _ClassVar[ClusterConfigProto.Bulletin.ServiceName]
            upgrader: _ClassVar[ClusterConfigProto.Bulletin.ServiceName]
            testservice: _ClassVar[ClusterConfigProto.Bulletin.ServiceName]
            os: _ClassVar[ClusterConfigProto.Bulletin.ServiceName]
            janus: _ClassVar[ClusterConfigProto.Bulletin.ServiceName]
            hc_cli: _ClassVar[ClusterConfigProto.Bulletin.ServiceName]
            dlp: _ClassVar[ClusterConfigProto.Bulletin.ServiceName]
            pushprox_client: _ClassVar[ClusterConfigProto.Bulletin.ServiceName]
            pushclient: _ClassVar[ClusterConfigProto.Bulletin.ServiceName]
            aegis: _ClassVar[ClusterConfigProto.Bulletin.ServiceName]
            nfs_proxy: _ClassVar[ClusterConfigProto.Bulletin.ServiceName]
            elixir_workerservice: _ClassVar[ClusterConfigProto.Bulletin.ServiceName]
            argus_app: _ClassVar[ClusterConfigProto.Bulletin.ServiceName]
            metadataservice: _ClassVar[ClusterConfigProto.Bulletin.ServiceName]
            spire_server: _ClassVar[ClusterConfigProto.Bulletin.ServiceName]
            spire_agent: _ClassVar[ClusterConfigProto.Bulletin.ServiceName]
            workqueueserver: _ClassVar[ClusterConfigProto.Bulletin.ServiceName]
            elasticsearch: _ClassVar[ClusterConfigProto.Bulletin.ServiceName]
            licensing: _ClassVar[ClusterConfigProto.Bulletin.ServiceName]
            axon: _ClassVar[ClusterConfigProto.Bulletin.ServiceName]
            magnus: _ClassVar[ClusterConfigProto.Bulletin.ServiceName]
            ods_app: _ClassVar[ClusterConfigProto.Bulletin.ServiceName]
            sheltered_harbor_app: _ClassVar[ClusterConfigProto.Bulletin.ServiceName]
            sheltered_harbor_uda: _ClassVar[ClusterConfigProto.Bulletin.ServiceName]
            coredns: _ClassVar[ClusterConfigProto.Bulletin.ServiceName]
            cohesity_ca: _ClassVar[ClusterConfigProto.Bulletin.ServiceName]
            metrics_server: _ClassVar[ClusterConfigProto.Bulletin.ServiceName]
            infraoperator: _ClassVar[ClusterConfigProto.Bulletin.ServiceName]
            marketplaceoperator: _ClassVar[ClusterConfigProto.Bulletin.ServiceName]
            cohesion: _ClassVar[ClusterConfigProto.Bulletin.ServiceName]
            spire_app: _ClassVar[ClusterConfigProto.Bulletin.ServiceName]
            gaia: _ClassVar[ClusterConfigProto.Bulletin.ServiceName]
            sftp_ui_app: _ClassVar[ClusterConfigProto.Bulletin.ServiceName]
        invalid: ClusterConfigProto.Bulletin.ServiceName
        apollo: ClusterConfigProto.Bulletin.ServiceName
        bridge: ClusterConfigProto.Bulletin.ServiceName
        genie: ClusterConfigProto.Bulletin.ServiceName
        genie_gofer: ClusterConfigProto.Bulletin.ServiceName
        magneto: ClusterConfigProto.Bulletin.ServiceName
        iris: ClusterConfigProto.Bulletin.ServiceName
        iris_proxy: ClusterConfigProto.Bulletin.ServiceName
        newscribe: ClusterConfigProto.Bulletin.ServiceName
        stats: ClusterConfigProto.Bulletin.ServiceName
        yoda: ClusterConfigProto.Bulletin.ServiceName
        alerts: ClusterConfigProto.Bulletin.ServiceName
        keychain: ClusterConfigProto.Bulletin.ServiceName
        logwatcher: ClusterConfigProto.Bulletin.ServiceName
        statscollector: ClusterConfigProto.Bulletin.ServiceName
        gandalf: ClusterConfigProto.Bulletin.ServiceName
        nexus: ClusterConfigProto.Bulletin.ServiceName
        nexus_proxy: ClusterConfigProto.Bulletin.ServiceName
        storage_proxy: ClusterConfigProto.Bulletin.ServiceName
        tricorder: ClusterConfigProto.Bulletin.ServiceName
        rtclient: ClusterConfigProto.Bulletin.ServiceName
        vault_proxy: ClusterConfigProto.Bulletin.ServiceName
        smb_proxy: ClusterConfigProto.Bulletin.ServiceName
        bridge_proxy: ClusterConfigProto.Bulletin.ServiceName
        librarian: ClusterConfigProto.Bulletin.ServiceName
        groot: ClusterConfigProto.Bulletin.ServiceName
        eagle_agent: ClusterConfigProto.Bulletin.ServiceName
        athena: ClusterConfigProto.Bulletin.ServiceName
        bifrost_broker: ClusterConfigProto.Bulletin.ServiceName
        elixir: ClusterConfigProto.Bulletin.ServiceName
        vulscan: ClusterConfigProto.Bulletin.ServiceName
        postgres: ClusterConfigProto.Bulletin.ServiceName
        atom: ClusterConfigProto.Bulletin.ServiceName
        yoda_agent: ClusterConfigProto.Bulletin.ServiceName
        smb2_proxy: ClusterConfigProto.Bulletin.ServiceName
        throttler: ClusterConfigProto.Bulletin.ServiceName
        kafka: ClusterConfigProto.Bulletin.ServiceName
        eventing: ClusterConfigProto.Bulletin.ServiceName
        agentinstall: ClusterConfigProto.Bulletin.ServiceName
        imanis: ClusterConfigProto.Bulletin.ServiceName
        elrond: ClusterConfigProto.Bulletin.ServiceName
        heimdall: ClusterConfigProto.Bulletin.ServiceName
        bifrost: ClusterConfigProto.Bulletin.ServiceName
        icebox: ClusterConfigProto.Bulletin.ServiceName
        node_exporter: ClusterConfigProto.Bulletin.ServiceName
        compass: ClusterConfigProto.Bulletin.ServiceName
        patch: ClusterConfigProto.Bulletin.ServiceName
        etl_server: ClusterConfigProto.Bulletin.ServiceName
        upgrader: ClusterConfigProto.Bulletin.ServiceName
        testservice: ClusterConfigProto.Bulletin.ServiceName
        os: ClusterConfigProto.Bulletin.ServiceName
        janus: ClusterConfigProto.Bulletin.ServiceName
        hc_cli: ClusterConfigProto.Bulletin.ServiceName
        dlp: ClusterConfigProto.Bulletin.ServiceName
        pushprox_client: ClusterConfigProto.Bulletin.ServiceName
        pushclient: ClusterConfigProto.Bulletin.ServiceName
        aegis: ClusterConfigProto.Bulletin.ServiceName
        nfs_proxy: ClusterConfigProto.Bulletin.ServiceName
        elixir_workerservice: ClusterConfigProto.Bulletin.ServiceName
        argus_app: ClusterConfigProto.Bulletin.ServiceName
        metadataservice: ClusterConfigProto.Bulletin.ServiceName
        spire_server: ClusterConfigProto.Bulletin.ServiceName
        spire_agent: ClusterConfigProto.Bulletin.ServiceName
        workqueueserver: ClusterConfigProto.Bulletin.ServiceName
        elasticsearch: ClusterConfigProto.Bulletin.ServiceName
        licensing: ClusterConfigProto.Bulletin.ServiceName
        axon: ClusterConfigProto.Bulletin.ServiceName
        magnus: ClusterConfigProto.Bulletin.ServiceName
        ods_app: ClusterConfigProto.Bulletin.ServiceName
        sheltered_harbor_app: ClusterConfigProto.Bulletin.ServiceName
        sheltered_harbor_uda: ClusterConfigProto.Bulletin.ServiceName
        coredns: ClusterConfigProto.Bulletin.ServiceName
        cohesity_ca: ClusterConfigProto.Bulletin.ServiceName
        metrics_server: ClusterConfigProto.Bulletin.ServiceName
        infraoperator: ClusterConfigProto.Bulletin.ServiceName
        marketplaceoperator: ClusterConfigProto.Bulletin.ServiceName
        cohesion: ClusterConfigProto.Bulletin.ServiceName
        spire_app: ClusterConfigProto.Bulletin.ServiceName
        gaia: ClusterConfigProto.Bulletin.ServiceName
        sftp_ui_app: ClusterConfigProto.Bulletin.ServiceName
        class Operation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kNone: _ClassVar[ClusterConfigProto.Bulletin.Operation]
            kDestroy: _ClassVar[ClusterConfigProto.Bulletin.Operation]
            kUpgrade: _ClassVar[ClusterConfigProto.Bulletin.Operation]
            kClean: _ClassVar[ClusterConfigProto.Bulletin.Operation]
            kRemoveNode: _ClassVar[ClusterConfigProto.Bulletin.Operation]
            kRestartServices: _ClassVar[ClusterConfigProto.Bulletin.Operation]
            kRestartSystemServices: _ClassVar[ClusterConfigProto.Bulletin.Operation]
            kUpgradeBaseos: _ClassVar[ClusterConfigProto.Bulletin.Operation]
            kClusterExpand: _ClassVar[ClusterConfigProto.Bulletin.Operation]
            kRunUpgradeChecks: _ClassVar[ClusterConfigProto.Bulletin.Operation]
        kNone: ClusterConfigProto.Bulletin.Operation
        kDestroy: ClusterConfigProto.Bulletin.Operation
        kUpgrade: ClusterConfigProto.Bulletin.Operation
        kClean: ClusterConfigProto.Bulletin.Operation
        kRemoveNode: ClusterConfigProto.Bulletin.Operation
        kRestartServices: ClusterConfigProto.Bulletin.Operation
        kRestartSystemServices: ClusterConfigProto.Bulletin.Operation
        kUpgradeBaseos: ClusterConfigProto.Bulletin.Operation
        kClusterExpand: ClusterConfigProto.Bulletin.Operation
        kRunUpgradeChecks: ClusterConfigProto.Bulletin.Operation
        class UpgradeChecksPhase(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kUpgradeChecksPre: _ClassVar[ClusterConfigProto.Bulletin.UpgradeChecksPhase]
            kUpgradeChecksDuring: _ClassVar[ClusterConfigProto.Bulletin.UpgradeChecksPhase]
            kUpgradeChecksPost: _ClassVar[ClusterConfigProto.Bulletin.UpgradeChecksPhase]
        kUpgradeChecksPre: ClusterConfigProto.Bulletin.UpgradeChecksPhase
        kUpgradeChecksDuring: ClusterConfigProto.Bulletin.UpgradeChecksPhase
        kUpgradeChecksPost: ClusterConfigProto.Bulletin.UpgradeChecksPhase
        class ServicesState(_message.Message):
            __slots__ = ("stop_cluster", "stopped_service_vec_deprecated", "restart_service_vec_deprecated", "stopped_services_vec", "restart_services_vec", "license_disabled", "athena_enabled_services_vec", "athena_paused_services_vec", "ignore_dependent_services", "restart_as_system_services_vec")
            STOP_CLUSTER_FIELD_NUMBER: _ClassVar[int]
            STOPPED_SERVICE_VEC_DEPRECATED_FIELD_NUMBER: _ClassVar[int]
            RESTART_SERVICE_VEC_DEPRECATED_FIELD_NUMBER: _ClassVar[int]
            STOPPED_SERVICES_VEC_FIELD_NUMBER: _ClassVar[int]
            RESTART_SERVICES_VEC_FIELD_NUMBER: _ClassVar[int]
            LICENSE_DISABLED_FIELD_NUMBER: _ClassVar[int]
            ATHENA_ENABLED_SERVICES_VEC_FIELD_NUMBER: _ClassVar[int]
            ATHENA_PAUSED_SERVICES_VEC_FIELD_NUMBER: _ClassVar[int]
            IGNORE_DEPENDENT_SERVICES_FIELD_NUMBER: _ClassVar[int]
            RESTART_AS_SYSTEM_SERVICES_VEC_FIELD_NUMBER: _ClassVar[int]
            stop_cluster: bool
            stopped_service_vec_deprecated: int
            restart_service_vec_deprecated: int
            stopped_services_vec: _containers.RepeatedScalarFieldContainer[ClusterConfigProto.Bulletin.ServiceName]
            restart_services_vec: _containers.RepeatedScalarFieldContainer[ClusterConfigProto.Bulletin.ServiceName]
            license_disabled: bool
            athena_enabled_services_vec: _containers.RepeatedScalarFieldContainer[ClusterConfigProto.Bulletin.ServiceName]
            athena_paused_services_vec: _containers.RepeatedScalarFieldContainer[ClusterConfigProto.Bulletin.ServiceName]
            ignore_dependent_services: bool
            restart_as_system_services_vec: _containers.RepeatedScalarFieldContainer[ClusterConfigProto.Bulletin.ServiceName]
            def __init__(self, stop_cluster: bool = ..., stopped_service_vec_deprecated: _Optional[int] = ..., restart_service_vec_deprecated: _Optional[int] = ..., stopped_services_vec: _Optional[_Iterable[_Union[ClusterConfigProto.Bulletin.ServiceName, str]]] = ..., restart_services_vec: _Optional[_Iterable[_Union[ClusterConfigProto.Bulletin.ServiceName, str]]] = ..., license_disabled: bool = ..., athena_enabled_services_vec: _Optional[_Iterable[_Union[ClusterConfigProto.Bulletin.ServiceName, str]]] = ..., athena_paused_services_vec: _Optional[_Iterable[_Union[ClusterConfigProto.Bulletin.ServiceName, str]]] = ..., ignore_dependent_services: bool = ..., restart_as_system_services_vec: _Optional[_Iterable[_Union[ClusterConfigProto.Bulletin.ServiceName, str]]] = ...) -> None: ...
        class UpgradeChecksReqPhaseInfo(_message.Message):
            __slots__ = ("execution_phase", "start_time_secs", "finish_time_secs", "is_run_success", "instance_failure_reason")
            EXECUTION_PHASE_FIELD_NUMBER: _ClassVar[int]
            START_TIME_SECS_FIELD_NUMBER: _ClassVar[int]
            FINISH_TIME_SECS_FIELD_NUMBER: _ClassVar[int]
            IS_RUN_SUCCESS_FIELD_NUMBER: _ClassVar[int]
            INSTANCE_FAILURE_REASON_FIELD_NUMBER: _ClassVar[int]
            execution_phase: ClusterConfigProto.Bulletin.UpgradeChecksPhase
            start_time_secs: int
            finish_time_secs: int
            is_run_success: bool
            instance_failure_reason: str
            def __init__(self, execution_phase: _Optional[_Union[ClusterConfigProto.Bulletin.UpgradeChecksPhase, str]] = ..., start_time_secs: _Optional[int] = ..., finish_time_secs: _Optional[int] = ..., is_run_success: bool = ..., instance_failure_reason: _Optional[str] = ...) -> None: ...
        class UpgradeChecksReqInfo(_message.Message):
            __slots__ = ("instance_id", "phase_info_vec", "healthcheck_skip_test_ids", "healthcheck_skip_node_ids", "force_validate_health_checks")
            INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
            PHASE_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
            HEALTHCHECK_SKIP_TEST_IDS_FIELD_NUMBER: _ClassVar[int]
            HEALTHCHECK_SKIP_NODE_IDS_FIELD_NUMBER: _ClassVar[int]
            FORCE_VALIDATE_HEALTH_CHECKS_FIELD_NUMBER: _ClassVar[int]
            instance_id: int
            phase_info_vec: _containers.RepeatedCompositeFieldContainer[ClusterConfigProto.Bulletin.UpgradeChecksReqPhaseInfo]
            healthcheck_skip_test_ids: str
            healthcheck_skip_node_ids: str
            force_validate_health_checks: bool
            def __init__(self, instance_id: _Optional[int] = ..., phase_info_vec: _Optional[_Iterable[_Union[ClusterConfigProto.Bulletin.UpgradeChecksReqPhaseInfo, _Mapping]]] = ..., healthcheck_skip_test_ids: _Optional[str] = ..., healthcheck_skip_node_ids: _Optional[str] = ..., force_validate_health_checks: bool = ...) -> None: ...
        class UpgradeChecksReqState(_message.Message):
            __slots__ = ("execution_phase", "active_instance", "completed_instances_vec")
            EXECUTION_PHASE_FIELD_NUMBER: _ClassVar[int]
            ACTIVE_INSTANCE_FIELD_NUMBER: _ClassVar[int]
            COMPLETED_INSTANCES_VEC_FIELD_NUMBER: _ClassVar[int]
            execution_phase: ClusterConfigProto.Bulletin.UpgradeChecksPhase
            active_instance: ClusterConfigProto.Bulletin.UpgradeChecksReqInfo
            completed_instances_vec: _containers.RepeatedCompositeFieldContainer[ClusterConfigProto.Bulletin.UpgradeChecksReqInfo]
            def __init__(self, execution_phase: _Optional[_Union[ClusterConfigProto.Bulletin.UpgradeChecksPhase, str]] = ..., active_instance: _Optional[_Union[ClusterConfigProto.Bulletin.UpgradeChecksReqInfo, _Mapping]] = ..., completed_instances_vec: _Optional[_Iterable[_Union[ClusterConfigProto.Bulletin.UpgradeChecksReqInfo, _Mapping]]] = ...) -> None: ...
        CLUSTER_TARGET_SOFTWARE_VERSION_FIELD_NUMBER: _ClassVar[int]
        SERVICE_STATE_FIELD_NUMBER: _ClassVar[int]
        CURRENT_OPERATION_FIELD_NUMBER: _ClassVar[int]
        OPERATION_START_TIME_SECS_FIELD_NUMBER: _ClassVar[int]
        SOFTWARE_PACKAGE_URL_FIELD_NUMBER: _ClassVar[int]
        SOFTWARE_PACKAGE_CHECKSUM_FIELD_NUMBER: _ClassVar[int]
        IGNORE_SW_INCOMPATIBILITY_FIELD_NUMBER: _ClassVar[int]
        IS_PARALLEL_UPGRADE_FIELD_NUMBER: _ClassVar[int]
        AGENT_AUTO_UPGRADE_REQUESTED_FIELD_NUMBER: _ClassVar[int]
        CLUSTER_TARGET_BASE_OS_VERSION_FIELD_NUMBER: _ClassVar[int]
        IS_UPGRADE_CANCEL_REQUESTED_FIELD_NUMBER: _ClassVar[int]
        IS_CLUSTER_MIGRATION_PENDING_FIELD_NUMBER: _ClassVar[int]
        UPGRADE_CHECKS_REQ_STATE_FIELD_NUMBER: _ClassVar[int]
        UPGRADE_REQ_HC_DATA_FIELD_NUMBER: _ClassVar[int]
        CLUSTER_CURRENT_SOFTWARE_VERSION_FIELD_NUMBER: _ClassVar[int]
        IS_UPGRADE_ABORTED_FIELD_NUMBER: _ClassVar[int]
        UPGRADE_FAILURE_ERROR_STRING_FIELD_NUMBER: _ClassVar[int]
        CLUSTER_TARGET_UPGRADE_TRANSACTION_ID_FIELD_NUMBER: _ClassVar[int]
        cluster_target_software_version: str
        service_state: ClusterConfigProto.Bulletin.ServicesState
        current_operation: ClusterConfigProto.Bulletin.Operation
        operation_start_time_secs: int
        software_package_url: str
        software_package_checksum: str
        ignore_sw_incompatibility: bool
        is_parallel_upgrade: bool
        agent_auto_upgrade_requested: bool
        cluster_target_base_os_version: int
        is_upgrade_cancel_requested: bool
        is_cluster_migration_pending: bool
        upgrade_checks_req_state: ClusterConfigProto.Bulletin.UpgradeChecksReqState
        upgrade_req_hc_data: ClusterConfigProto.Bulletin.UpgradeChecksReqInfo
        cluster_current_software_version: str
        is_upgrade_aborted: bool
        upgrade_failure_error_string: str
        cluster_target_upgrade_transaction_id: int
        def __init__(self, cluster_target_software_version: _Optional[str] = ..., service_state: _Optional[_Union[ClusterConfigProto.Bulletin.ServicesState, _Mapping]] = ..., current_operation: _Optional[_Union[ClusterConfigProto.Bulletin.Operation, str]] = ..., operation_start_time_secs: _Optional[int] = ..., software_package_url: _Optional[str] = ..., software_package_checksum: _Optional[str] = ..., ignore_sw_incompatibility: bool = ..., is_parallel_upgrade: bool = ..., agent_auto_upgrade_requested: bool = ..., cluster_target_base_os_version: _Optional[int] = ..., is_upgrade_cancel_requested: bool = ..., is_cluster_migration_pending: bool = ..., upgrade_checks_req_state: _Optional[_Union[ClusterConfigProto.Bulletin.UpgradeChecksReqState, _Mapping]] = ..., upgrade_req_hc_data: _Optional[_Union[ClusterConfigProto.Bulletin.UpgradeChecksReqInfo, _Mapping]] = ..., cluster_current_software_version: _Optional[str] = ..., is_upgrade_aborted: bool = ..., upgrade_failure_error_string: _Optional[str] = ..., cluster_target_upgrade_transaction_id: _Optional[int] = ...) -> None: ...
    class ScribeTableNames(_message.Message):
        __slots__ = ("view_snap_tree", "blob_snap_tree", "view_metadata", "blob_metadata", "canonical_blob_metadata", "chunk_metadata", "chunk_file_metadata", "chunk_file_container_metadata", "chunk_file_access", "alerts_metadata", "alerts_data", "scribe_wal_filesystem", "stats_data", "yoda_object_data", "alerts_resolutions", "alerts_rules", "analytics_mapper_info", "analytics_reducer_info", "analytics_map_reduce_info", "analytics_map_reduce_instances", "pulse_data", "smb_session_metadata", "icebox_archive_metadata", "icebox_archive_object_metadata", "smb_entity_metadata", "icebox_restore_job_metadata", "pubsub_data", "view_usage", "quota_snap_tree", "icebox_snap_tree_node_location_map", "icebox_chunk_location_map", "icebox_restored_snap_tree_nodes_map", "cluster_audit_records", "filer_audit_records", "tiering_audit_records", "icebox_search_job_metadata", "icebox_search_result_archive_metadata", "magneto_sub_task_state", "magneto_slave_op_data", "view_indices", "icebox_job_metadata", "magneto_snapshot_state", "iris_scheduler_data", "yoda_thread_progress_info", "user_quota_usage_snap_tree", "iris_user_data", "rsync_inode_map", "iris_tenant_data", "magneto_changelogs", "chunk_repo_metadata", "stats_counters_containers", "icebox_prepared_objects_metadata", "icebox_restored_hardlinks", "logical_unit_metadata", "antivirus_snap_tree", "lock_entity_metadata", "yoda_indexing_metadata_stats", "iris_banner_data", "bookkeeper_metadata", "shadow_copy_set_context", "stats_entity_schema", "stats_entity", "stats_timeseries_data", "dir_quota_snap_tree", "stats_counters", "nfs4_metadata", "shadow_copy_set_metadata", "magneto_run_store", "apollo_report", "iris_certificate_data", "stats_alert_policies", "stats_containers", "filer_metadata", "atom_node_alloc_data", "atom_protection_object_metadata", "uptier_entity_metadata", "atom_protection_object_events", "atom_protection_object_event_cleanup", "atom_protection_object_misc_data", "stats_aggregation_timeseries", "icebox_archive_chunk_file_metadata", "elrond_prediction_model", "nas_dr_failover_state", "bridge_swift_account", "view_template", "scribe_megastore", "cloud_chunk_file_metadata", "hyx_connector_metadata", "network_realm_metadata", "icebox_stub_view_stats", "cloud_object_metadata", "icebox_cloud_domain_restored_nodes", "yoda_tag_updates", "icebox_stub_view_metadata", "yoda_tags", "iris_session_data", "librarian_index_info_store", "workqueue_worker_task_store", "s3object_snap_tree", "workqueue_server_task_state_store", "workqueue_server_worker_state_store", "iris_user_login_time_data", "agent_config_data", "bookkeeper_v2_groups", "bookkeeper_v2_entities", "o365_teams_channels_data", "bookkeeper_v2_tenants_groups", "atom_protection_object_epochs", "invalid_cloud_locations", "bookkeeper_v2_query", "invalid_archived_nodes", "invalid_archived_chunks", "critical_debug_info_table", "apollo_bkpr_v2_query_pipeline_mr_state", "magneto_entity_id_mapping_table", "cohesity_ca_certificates_table", "yoda_tenant_migration_import_table", "magneto_tenant_migration_import_table")
        VIEW_SNAP_TREE_FIELD_NUMBER: _ClassVar[int]
        BLOB_SNAP_TREE_FIELD_NUMBER: _ClassVar[int]
        VIEW_METADATA_FIELD_NUMBER: _ClassVar[int]
        BLOB_METADATA_FIELD_NUMBER: _ClassVar[int]
        CANONICAL_BLOB_METADATA_FIELD_NUMBER: _ClassVar[int]
        CHUNK_METADATA_FIELD_NUMBER: _ClassVar[int]
        CHUNK_FILE_METADATA_FIELD_NUMBER: _ClassVar[int]
        CHUNK_FILE_CONTAINER_METADATA_FIELD_NUMBER: _ClassVar[int]
        CHUNK_FILE_ACCESS_FIELD_NUMBER: _ClassVar[int]
        ALERTS_METADATA_FIELD_NUMBER: _ClassVar[int]
        ALERTS_DATA_FIELD_NUMBER: _ClassVar[int]
        SCRIBE_WAL_FILESYSTEM_FIELD_NUMBER: _ClassVar[int]
        STATS_DATA_FIELD_NUMBER: _ClassVar[int]
        YODA_OBJECT_DATA_FIELD_NUMBER: _ClassVar[int]
        ALERTS_RESOLUTIONS_FIELD_NUMBER: _ClassVar[int]
        ALERTS_RULES_FIELD_NUMBER: _ClassVar[int]
        ANALYTICS_MAPPER_INFO_FIELD_NUMBER: _ClassVar[int]
        ANALYTICS_REDUCER_INFO_FIELD_NUMBER: _ClassVar[int]
        ANALYTICS_MAP_REDUCE_INFO_FIELD_NUMBER: _ClassVar[int]
        ANALYTICS_MAP_REDUCE_INSTANCES_FIELD_NUMBER: _ClassVar[int]
        PULSE_DATA_FIELD_NUMBER: _ClassVar[int]
        SMB_SESSION_METADATA_FIELD_NUMBER: _ClassVar[int]
        ICEBOX_ARCHIVE_METADATA_FIELD_NUMBER: _ClassVar[int]
        ICEBOX_ARCHIVE_OBJECT_METADATA_FIELD_NUMBER: _ClassVar[int]
        SMB_ENTITY_METADATA_FIELD_NUMBER: _ClassVar[int]
        ICEBOX_RESTORE_JOB_METADATA_FIELD_NUMBER: _ClassVar[int]
        PUBSUB_DATA_FIELD_NUMBER: _ClassVar[int]
        VIEW_USAGE_FIELD_NUMBER: _ClassVar[int]
        QUOTA_SNAP_TREE_FIELD_NUMBER: _ClassVar[int]
        ICEBOX_SNAP_TREE_NODE_LOCATION_MAP_FIELD_NUMBER: _ClassVar[int]
        ICEBOX_CHUNK_LOCATION_MAP_FIELD_NUMBER: _ClassVar[int]
        ICEBOX_RESTORED_SNAP_TREE_NODES_MAP_FIELD_NUMBER: _ClassVar[int]
        CLUSTER_AUDIT_RECORDS_FIELD_NUMBER: _ClassVar[int]
        FILER_AUDIT_RECORDS_FIELD_NUMBER: _ClassVar[int]
        TIERING_AUDIT_RECORDS_FIELD_NUMBER: _ClassVar[int]
        ICEBOX_SEARCH_JOB_METADATA_FIELD_NUMBER: _ClassVar[int]
        ICEBOX_SEARCH_RESULT_ARCHIVE_METADATA_FIELD_NUMBER: _ClassVar[int]
        MAGNETO_SUB_TASK_STATE_FIELD_NUMBER: _ClassVar[int]
        MAGNETO_SLAVE_OP_DATA_FIELD_NUMBER: _ClassVar[int]
        VIEW_INDICES_FIELD_NUMBER: _ClassVar[int]
        ICEBOX_JOB_METADATA_FIELD_NUMBER: _ClassVar[int]
        MAGNETO_SNAPSHOT_STATE_FIELD_NUMBER: _ClassVar[int]
        IRIS_SCHEDULER_DATA_FIELD_NUMBER: _ClassVar[int]
        YODA_THREAD_PROGRESS_INFO_FIELD_NUMBER: _ClassVar[int]
        USER_QUOTA_USAGE_SNAP_TREE_FIELD_NUMBER: _ClassVar[int]
        IRIS_USER_DATA_FIELD_NUMBER: _ClassVar[int]
        RSYNC_INODE_MAP_FIELD_NUMBER: _ClassVar[int]
        IRIS_TENANT_DATA_FIELD_NUMBER: _ClassVar[int]
        MAGNETO_CHANGELOGS_FIELD_NUMBER: _ClassVar[int]
        CHUNK_REPO_METADATA_FIELD_NUMBER: _ClassVar[int]
        STATS_COUNTERS_CONTAINERS_FIELD_NUMBER: _ClassVar[int]
        ICEBOX_PREPARED_OBJECTS_METADATA_FIELD_NUMBER: _ClassVar[int]
        ICEBOX_RESTORED_HARDLINKS_FIELD_NUMBER: _ClassVar[int]
        LOGICAL_UNIT_METADATA_FIELD_NUMBER: _ClassVar[int]
        ANTIVIRUS_SNAP_TREE_FIELD_NUMBER: _ClassVar[int]
        LOCK_ENTITY_METADATA_FIELD_NUMBER: _ClassVar[int]
        YODA_INDEXING_METADATA_STATS_FIELD_NUMBER: _ClassVar[int]
        IRIS_BANNER_DATA_FIELD_NUMBER: _ClassVar[int]
        BOOKKEEPER_METADATA_FIELD_NUMBER: _ClassVar[int]
        SHADOW_COPY_SET_CONTEXT_FIELD_NUMBER: _ClassVar[int]
        STATS_ENTITY_SCHEMA_FIELD_NUMBER: _ClassVar[int]
        STATS_ENTITY_FIELD_NUMBER: _ClassVar[int]
        STATS_TIMESERIES_DATA_FIELD_NUMBER: _ClassVar[int]
        DIR_QUOTA_SNAP_TREE_FIELD_NUMBER: _ClassVar[int]
        STATS_COUNTERS_FIELD_NUMBER: _ClassVar[int]
        NFS4_METADATA_FIELD_NUMBER: _ClassVar[int]
        SHADOW_COPY_SET_METADATA_FIELD_NUMBER: _ClassVar[int]
        MAGNETO_RUN_STORE_FIELD_NUMBER: _ClassVar[int]
        APOLLO_REPORT_FIELD_NUMBER: _ClassVar[int]
        IRIS_CERTIFICATE_DATA_FIELD_NUMBER: _ClassVar[int]
        STATS_ALERT_POLICIES_FIELD_NUMBER: _ClassVar[int]
        STATS_CONTAINERS_FIELD_NUMBER: _ClassVar[int]
        FILER_METADATA_FIELD_NUMBER: _ClassVar[int]
        ATOM_NODE_ALLOC_DATA_FIELD_NUMBER: _ClassVar[int]
        ATOM_PROTECTION_OBJECT_METADATA_FIELD_NUMBER: _ClassVar[int]
        UPTIER_ENTITY_METADATA_FIELD_NUMBER: _ClassVar[int]
        ATOM_PROTECTION_OBJECT_EVENTS_FIELD_NUMBER: _ClassVar[int]
        ATOM_PROTECTION_OBJECT_EVENT_CLEANUP_FIELD_NUMBER: _ClassVar[int]
        ATOM_PROTECTION_OBJECT_MISC_DATA_FIELD_NUMBER: _ClassVar[int]
        STATS_AGGREGATION_TIMESERIES_FIELD_NUMBER: _ClassVar[int]
        ICEBOX_ARCHIVE_CHUNK_FILE_METADATA_FIELD_NUMBER: _ClassVar[int]
        ELROND_PREDICTION_MODEL_FIELD_NUMBER: _ClassVar[int]
        NAS_DR_FAILOVER_STATE_FIELD_NUMBER: _ClassVar[int]
        BRIDGE_SWIFT_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
        VIEW_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
        SCRIBE_MEGASTORE_FIELD_NUMBER: _ClassVar[int]
        CLOUD_CHUNK_FILE_METADATA_FIELD_NUMBER: _ClassVar[int]
        HYX_CONNECTOR_METADATA_FIELD_NUMBER: _ClassVar[int]
        NETWORK_REALM_METADATA_FIELD_NUMBER: _ClassVar[int]
        ICEBOX_STUB_VIEW_STATS_FIELD_NUMBER: _ClassVar[int]
        CLOUD_OBJECT_METADATA_FIELD_NUMBER: _ClassVar[int]
        ICEBOX_CLOUD_DOMAIN_RESTORED_NODES_FIELD_NUMBER: _ClassVar[int]
        YODA_TAG_UPDATES_FIELD_NUMBER: _ClassVar[int]
        ICEBOX_STUB_VIEW_METADATA_FIELD_NUMBER: _ClassVar[int]
        YODA_TAGS_FIELD_NUMBER: _ClassVar[int]
        IRIS_SESSION_DATA_FIELD_NUMBER: _ClassVar[int]
        LIBRARIAN_INDEX_INFO_STORE_FIELD_NUMBER: _ClassVar[int]
        WORKQUEUE_WORKER_TASK_STORE_FIELD_NUMBER: _ClassVar[int]
        S3OBJECT_SNAP_TREE_FIELD_NUMBER: _ClassVar[int]
        WORKQUEUE_SERVER_TASK_STATE_STORE_FIELD_NUMBER: _ClassVar[int]
        WORKQUEUE_SERVER_WORKER_STATE_STORE_FIELD_NUMBER: _ClassVar[int]
        IRIS_USER_LOGIN_TIME_DATA_FIELD_NUMBER: _ClassVar[int]
        AGENT_CONFIG_DATA_FIELD_NUMBER: _ClassVar[int]
        BOOKKEEPER_V2_GROUPS_FIELD_NUMBER: _ClassVar[int]
        BOOKKEEPER_V2_ENTITIES_FIELD_NUMBER: _ClassVar[int]
        O365_TEAMS_CHANNELS_DATA_FIELD_NUMBER: _ClassVar[int]
        BOOKKEEPER_V2_TENANTS_GROUPS_FIELD_NUMBER: _ClassVar[int]
        ATOM_PROTECTION_OBJECT_EPOCHS_FIELD_NUMBER: _ClassVar[int]
        INVALID_CLOUD_LOCATIONS_FIELD_NUMBER: _ClassVar[int]
        BOOKKEEPER_V2_QUERY_FIELD_NUMBER: _ClassVar[int]
        INVALID_ARCHIVED_NODES_FIELD_NUMBER: _ClassVar[int]
        INVALID_ARCHIVED_CHUNKS_FIELD_NUMBER: _ClassVar[int]
        CRITICAL_DEBUG_INFO_TABLE_FIELD_NUMBER: _ClassVar[int]
        APOLLO_BKPR_V2_QUERY_PIPELINE_MR_STATE_FIELD_NUMBER: _ClassVar[int]
        MAGNETO_ENTITY_ID_MAPPING_TABLE_FIELD_NUMBER: _ClassVar[int]
        COHESITY_CA_CERTIFICATES_TABLE_FIELD_NUMBER: _ClassVar[int]
        YODA_TENANT_MIGRATION_IMPORT_TABLE_FIELD_NUMBER: _ClassVar[int]
        MAGNETO_TENANT_MIGRATION_IMPORT_TABLE_FIELD_NUMBER: _ClassVar[int]
        view_snap_tree: str
        blob_snap_tree: str
        view_metadata: str
        blob_metadata: str
        canonical_blob_metadata: str
        chunk_metadata: str
        chunk_file_metadata: str
        chunk_file_container_metadata: str
        chunk_file_access: str
        alerts_metadata: str
        alerts_data: str
        scribe_wal_filesystem: str
        stats_data: str
        yoda_object_data: str
        alerts_resolutions: str
        alerts_rules: str
        analytics_mapper_info: str
        analytics_reducer_info: str
        analytics_map_reduce_info: str
        analytics_map_reduce_instances: str
        pulse_data: str
        smb_session_metadata: str
        icebox_archive_metadata: str
        icebox_archive_object_metadata: str
        smb_entity_metadata: str
        icebox_restore_job_metadata: str
        pubsub_data: str
        view_usage: str
        quota_snap_tree: str
        icebox_snap_tree_node_location_map: str
        icebox_chunk_location_map: str
        icebox_restored_snap_tree_nodes_map: str
        cluster_audit_records: str
        filer_audit_records: str
        tiering_audit_records: str
        icebox_search_job_metadata: str
        icebox_search_result_archive_metadata: str
        magneto_sub_task_state: str
        magneto_slave_op_data: str
        view_indices: str
        icebox_job_metadata: str
        magneto_snapshot_state: str
        iris_scheduler_data: str
        yoda_thread_progress_info: str
        user_quota_usage_snap_tree: str
        iris_user_data: str
        rsync_inode_map: str
        iris_tenant_data: str
        magneto_changelogs: str
        chunk_repo_metadata: str
        stats_counters_containers: str
        icebox_prepared_objects_metadata: str
        icebox_restored_hardlinks: str
        logical_unit_metadata: str
        antivirus_snap_tree: str
        lock_entity_metadata: str
        yoda_indexing_metadata_stats: str
        iris_banner_data: str
        bookkeeper_metadata: str
        shadow_copy_set_context: str
        stats_entity_schema: str
        stats_entity: str
        stats_timeseries_data: str
        dir_quota_snap_tree: str
        stats_counters: str
        nfs4_metadata: str
        shadow_copy_set_metadata: str
        magneto_run_store: str
        apollo_report: str
        iris_certificate_data: str
        stats_alert_policies: str
        stats_containers: str
        filer_metadata: str
        atom_node_alloc_data: str
        atom_protection_object_metadata: str
        uptier_entity_metadata: str
        atom_protection_object_events: str
        atom_protection_object_event_cleanup: str
        atom_protection_object_misc_data: str
        stats_aggregation_timeseries: str
        icebox_archive_chunk_file_metadata: str
        elrond_prediction_model: str
        nas_dr_failover_state: str
        bridge_swift_account: str
        view_template: str
        scribe_megastore: str
        cloud_chunk_file_metadata: str
        hyx_connector_metadata: str
        network_realm_metadata: str
        icebox_stub_view_stats: str
        cloud_object_metadata: str
        icebox_cloud_domain_restored_nodes: str
        yoda_tag_updates: str
        icebox_stub_view_metadata: str
        yoda_tags: str
        iris_session_data: str
        librarian_index_info_store: str
        workqueue_worker_task_store: str
        s3object_snap_tree: str
        workqueue_server_task_state_store: str
        workqueue_server_worker_state_store: str
        iris_user_login_time_data: str
        agent_config_data: str
        bookkeeper_v2_groups: str
        bookkeeper_v2_entities: str
        o365_teams_channels_data: str
        bookkeeper_v2_tenants_groups: str
        atom_protection_object_epochs: str
        invalid_cloud_locations: str
        bookkeeper_v2_query: str
        invalid_archived_nodes: str
        invalid_archived_chunks: str
        critical_debug_info_table: str
        apollo_bkpr_v2_query_pipeline_mr_state: str
        magneto_entity_id_mapping_table: str
        cohesity_ca_certificates_table: str
        yoda_tenant_migration_import_table: str
        magneto_tenant_migration_import_table: str
        def __init__(self, view_snap_tree: _Optional[str] = ..., blob_snap_tree: _Optional[str] = ..., view_metadata: _Optional[str] = ..., blob_metadata: _Optional[str] = ..., canonical_blob_metadata: _Optional[str] = ..., chunk_metadata: _Optional[str] = ..., chunk_file_metadata: _Optional[str] = ..., chunk_file_container_metadata: _Optional[str] = ..., chunk_file_access: _Optional[str] = ..., alerts_metadata: _Optional[str] = ..., alerts_data: _Optional[str] = ..., scribe_wal_filesystem: _Optional[str] = ..., stats_data: _Optional[str] = ..., yoda_object_data: _Optional[str] = ..., alerts_resolutions: _Optional[str] = ..., alerts_rules: _Optional[str] = ..., analytics_mapper_info: _Optional[str] = ..., analytics_reducer_info: _Optional[str] = ..., analytics_map_reduce_info: _Optional[str] = ..., analytics_map_reduce_instances: _Optional[str] = ..., pulse_data: _Optional[str] = ..., smb_session_metadata: _Optional[str] = ..., icebox_archive_metadata: _Optional[str] = ..., icebox_archive_object_metadata: _Optional[str] = ..., smb_entity_metadata: _Optional[str] = ..., icebox_restore_job_metadata: _Optional[str] = ..., pubsub_data: _Optional[str] = ..., view_usage: _Optional[str] = ..., quota_snap_tree: _Optional[str] = ..., icebox_snap_tree_node_location_map: _Optional[str] = ..., icebox_chunk_location_map: _Optional[str] = ..., icebox_restored_snap_tree_nodes_map: _Optional[str] = ..., cluster_audit_records: _Optional[str] = ..., filer_audit_records: _Optional[str] = ..., tiering_audit_records: _Optional[str] = ..., icebox_search_job_metadata: _Optional[str] = ..., icebox_search_result_archive_metadata: _Optional[str] = ..., magneto_sub_task_state: _Optional[str] = ..., magneto_slave_op_data: _Optional[str] = ..., view_indices: _Optional[str] = ..., icebox_job_metadata: _Optional[str] = ..., magneto_snapshot_state: _Optional[str] = ..., iris_scheduler_data: _Optional[str] = ..., yoda_thread_progress_info: _Optional[str] = ..., user_quota_usage_snap_tree: _Optional[str] = ..., iris_user_data: _Optional[str] = ..., rsync_inode_map: _Optional[str] = ..., iris_tenant_data: _Optional[str] = ..., magneto_changelogs: _Optional[str] = ..., chunk_repo_metadata: _Optional[str] = ..., stats_counters_containers: _Optional[str] = ..., icebox_prepared_objects_metadata: _Optional[str] = ..., icebox_restored_hardlinks: _Optional[str] = ..., logical_unit_metadata: _Optional[str] = ..., antivirus_snap_tree: _Optional[str] = ..., lock_entity_metadata: _Optional[str] = ..., yoda_indexing_metadata_stats: _Optional[str] = ..., iris_banner_data: _Optional[str] = ..., bookkeeper_metadata: _Optional[str] = ..., shadow_copy_set_context: _Optional[str] = ..., stats_entity_schema: _Optional[str] = ..., stats_entity: _Optional[str] = ..., stats_timeseries_data: _Optional[str] = ..., dir_quota_snap_tree: _Optional[str] = ..., stats_counters: _Optional[str] = ..., nfs4_metadata: _Optional[str] = ..., shadow_copy_set_metadata: _Optional[str] = ..., magneto_run_store: _Optional[str] = ..., apollo_report: _Optional[str] = ..., iris_certificate_data: _Optional[str] = ..., stats_alert_policies: _Optional[str] = ..., stats_containers: _Optional[str] = ..., filer_metadata: _Optional[str] = ..., atom_node_alloc_data: _Optional[str] = ..., atom_protection_object_metadata: _Optional[str] = ..., uptier_entity_metadata: _Optional[str] = ..., atom_protection_object_events: _Optional[str] = ..., atom_protection_object_event_cleanup: _Optional[str] = ..., atom_protection_object_misc_data: _Optional[str] = ..., stats_aggregation_timeseries: _Optional[str] = ..., icebox_archive_chunk_file_metadata: _Optional[str] = ..., elrond_prediction_model: _Optional[str] = ..., nas_dr_failover_state: _Optional[str] = ..., bridge_swift_account: _Optional[str] = ..., view_template: _Optional[str] = ..., scribe_megastore: _Optional[str] = ..., cloud_chunk_file_metadata: _Optional[str] = ..., hyx_connector_metadata: _Optional[str] = ..., network_realm_metadata: _Optional[str] = ..., icebox_stub_view_stats: _Optional[str] = ..., cloud_object_metadata: _Optional[str] = ..., icebox_cloud_domain_restored_nodes: _Optional[str] = ..., yoda_tag_updates: _Optional[str] = ..., icebox_stub_view_metadata: _Optional[str] = ..., yoda_tags: _Optional[str] = ..., iris_session_data: _Optional[str] = ..., librarian_index_info_store: _Optional[str] = ..., workqueue_worker_task_store: _Optional[str] = ..., s3object_snap_tree: _Optional[str] = ..., workqueue_server_task_state_store: _Optional[str] = ..., workqueue_server_worker_state_store: _Optional[str] = ..., iris_user_login_time_data: _Optional[str] = ..., agent_config_data: _Optional[str] = ..., bookkeeper_v2_groups: _Optional[str] = ..., bookkeeper_v2_entities: _Optional[str] = ..., o365_teams_channels_data: _Optional[str] = ..., bookkeeper_v2_tenants_groups: _Optional[str] = ..., atom_protection_object_epochs: _Optional[str] = ..., invalid_cloud_locations: _Optional[str] = ..., bookkeeper_v2_query: _Optional[str] = ..., invalid_archived_nodes: _Optional[str] = ..., invalid_archived_chunks: _Optional[str] = ..., critical_debug_info_table: _Optional[str] = ..., apollo_bkpr_v2_query_pipeline_mr_state: _Optional[str] = ..., magneto_entity_id_mapping_table: _Optional[str] = ..., cohesity_ca_certificates_table: _Optional[str] = ..., yoda_tenant_migration_import_table: _Optional[str] = ..., magneto_tenant_migration_import_table: _Optional[str] = ...) -> None: ...
    class NTPSettings(_message.Message):
        __slots__ = ("disable_master_slave_scheme", "ntp_authentication_enabled", "master_auth_info", "enable_master_slave_athentication")
        DISABLE_MASTER_SLAVE_SCHEME_FIELD_NUMBER: _ClassVar[int]
        NTP_AUTHENTICATION_ENABLED_FIELD_NUMBER: _ClassVar[int]
        MASTER_AUTH_INFO_FIELD_NUMBER: _ClassVar[int]
        ENABLE_MASTER_SLAVE_ATHENTICATION_FIELD_NUMBER: _ClassVar[int]
        disable_master_slave_scheme: bool
        ntp_authentication_enabled: bool
        master_auth_info: ClusterConfigProto.NTPAuthKeyInfo
        enable_master_slave_athentication: bool
        def __init__(self, disable_master_slave_scheme: bool = ..., ntp_authentication_enabled: bool = ..., master_auth_info: _Optional[_Union[ClusterConfigProto.NTPAuthKeyInfo, _Mapping]] = ..., enable_master_slave_athentication: bool = ...) -> None: ...
    class SmtpServer(_message.Message):
        __slots__ = ("server", "port", "username", "password", "use_smtps", "disable_smtp", "sender_email_address", "domain_name")
        SERVER_FIELD_NUMBER: _ClassVar[int]
        PORT_FIELD_NUMBER: _ClassVar[int]
        USERNAME_FIELD_NUMBER: _ClassVar[int]
        PASSWORD_FIELD_NUMBER: _ClassVar[int]
        USE_SMTPS_FIELD_NUMBER: _ClassVar[int]
        DISABLE_SMTP_FIELD_NUMBER: _ClassVar[int]
        SENDER_EMAIL_ADDRESS_FIELD_NUMBER: _ClassVar[int]
        DOMAIN_NAME_FIELD_NUMBER: _ClassVar[int]
        server: str
        port: int
        username: str
        password: bytes
        use_smtps: bool
        disable_smtp: bool
        sender_email_address: str
        domain_name: str
        def __init__(self, server: _Optional[str] = ..., port: _Optional[int] = ..., username: _Optional[str] = ..., password: _Optional[bytes] = ..., use_smtps: bool = ..., disable_smtp: bool = ..., sender_email_address: _Optional[str] = ..., domain_name: _Optional[str] = ...) -> None: ...
    class SupportServer(_message.Message):
        __slots__ = ("reverse_tunnel_hostname", "reverse_tunnel_username", "reverse_tunnel_key", "enable_reverse_tunnel", "reverse_tunnel_port", "end_timestamp_msecs", "authorized_users")
        class AuthorizedUser(_message.Message):
            __slots__ = ("name", "public_ssh_key", "added_timestamp_msecs")
            NAME_FIELD_NUMBER: _ClassVar[int]
            PUBLIC_SSH_KEY_FIELD_NUMBER: _ClassVar[int]
            ADDED_TIMESTAMP_MSECS_FIELD_NUMBER: _ClassVar[int]
            name: str
            public_ssh_key: str
            added_timestamp_msecs: int
            def __init__(self, name: _Optional[str] = ..., public_ssh_key: _Optional[str] = ..., added_timestamp_msecs: _Optional[int] = ...) -> None: ...
        REVERSE_TUNNEL_HOSTNAME_FIELD_NUMBER: _ClassVar[int]
        REVERSE_TUNNEL_USERNAME_FIELD_NUMBER: _ClassVar[int]
        REVERSE_TUNNEL_KEY_FIELD_NUMBER: _ClassVar[int]
        ENABLE_REVERSE_TUNNEL_FIELD_NUMBER: _ClassVar[int]
        REVERSE_TUNNEL_PORT_FIELD_NUMBER: _ClassVar[int]
        END_TIMESTAMP_MSECS_FIELD_NUMBER: _ClassVar[int]
        AUTHORIZED_USERS_FIELD_NUMBER: _ClassVar[int]
        reverse_tunnel_hostname: str
        reverse_tunnel_username: str
        reverse_tunnel_key: bytes
        enable_reverse_tunnel: bool
        reverse_tunnel_port: int
        end_timestamp_msecs: int
        authorized_users: _containers.RepeatedCompositeFieldContainer[ClusterConfigProto.SupportServer.AuthorizedUser]
        def __init__(self, reverse_tunnel_hostname: _Optional[str] = ..., reverse_tunnel_username: _Optional[str] = ..., reverse_tunnel_key: _Optional[bytes] = ..., enable_reverse_tunnel: bool = ..., reverse_tunnel_port: _Optional[int] = ..., end_timestamp_msecs: _Optional[int] = ..., authorized_users: _Optional[_Iterable[_Union[ClusterConfigProto.SupportServer.AuthorizedUser, _Mapping]]] = ...) -> None: ...
    class IpmiConfig(_message.Message):
        __slots__ = ("subnet", "username", "password", "ipmi_gateway")
        SUBNET_FIELD_NUMBER: _ClassVar[int]
        USERNAME_FIELD_NUMBER: _ClassVar[int]
        PASSWORD_FIELD_NUMBER: _ClassVar[int]
        IPMI_GATEWAY_FIELD_NUMBER: _ClassVar[int]
        subnet: ClusterConfigProto.Subnet
        username: str
        password: bytes
        ipmi_gateway: str
        def __init__(self, subnet: _Optional[_Union[ClusterConfigProto.Subnet, _Mapping]] = ..., username: _Optional[str] = ..., password: _Optional[bytes] = ..., ipmi_gateway: _Optional[str] = ...) -> None: ...
    class HaloConfig(_message.Message):
        __slots__ = ("auth_key", "enable_automatic_polling", "automatic_pkg_download")
        AUTH_KEY_FIELD_NUMBER: _ClassVar[int]
        ENABLE_AUTOMATIC_POLLING_FIELD_NUMBER: _ClassVar[int]
        AUTOMATIC_PKG_DOWNLOAD_FIELD_NUMBER: _ClassVar[int]
        auth_key: str
        enable_automatic_polling: bool
        automatic_pkg_download: bool
        def __init__(self, auth_key: _Optional[str] = ..., enable_automatic_polling: bool = ..., automatic_pkg_download: bool = ...) -> None: ...
    class EagleConfig(_message.Message):
        __slots__ = ("auth_key", "disable_agent")
        AUTH_KEY_FIELD_NUMBER: _ClassVar[int]
        DISABLE_AGENT_FIELD_NUMBER: _ClassVar[int]
        auth_key: str
        disable_agent: bool
        def __init__(self, auth_key: _Optional[str] = ..., disable_agent: bool = ...) -> None: ...
    class KMSConfig(_message.Message):
        __slots__ = ("type", "version", "name", "aws", "cryptsoft_kms", "azure_kms", "id", "removal_state", "uploaded_key_id", "usage_type", "ownership_context")
        class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kInternalKMS: _ClassVar[ClusterConfigProto.KMSConfig.Type]
            kAwsKMS: _ClassVar[ClusterConfigProto.KMSConfig.Type]
            kCryptsoftKMS: _ClassVar[ClusterConfigProto.KMSConfig.Type]
            kAzureKMS: _ClassVar[ClusterConfigProto.KMSConfig.Type]
        kInternalKMS: ClusterConfigProto.KMSConfig.Type
        kAwsKMS: ClusterConfigProto.KMSConfig.Type
        kCryptsoftKMS: ClusterConfigProto.KMSConfig.Type
        kAzureKMS: ClusterConfigProto.KMSConfig.Type
        class UsageType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kArchival: _ClassVar[ClusterConfigProto.KMSConfig.UsageType]
            kRpaasArchival: _ClassVar[ClusterConfigProto.KMSConfig.UsageType]
        kArchival: ClusterConfigProto.KMSConfig.UsageType
        kRpaasArchival: ClusterConfigProto.KMSConfig.UsageType
        class Aws(_message.Message):
            __slots__ = ("amazon", "cmk_arn", "cmk_key_id", "cmk_alias", "verify_ssl", "ca_certificate_path", "ca_certificate")
            AMAZON_FIELD_NUMBER: _ClassVar[int]
            CMK_ARN_FIELD_NUMBER: _ClassVar[int]
            CMK_KEY_ID_FIELD_NUMBER: _ClassVar[int]
            CMK_ALIAS_FIELD_NUMBER: _ClassVar[int]
            VERIFY_SSL_FIELD_NUMBER: _ClassVar[int]
            CA_CERTIFICATE_PATH_FIELD_NUMBER: _ClassVar[int]
            CA_CERTIFICATE_FIELD_NUMBER: _ClassVar[int]
            amazon: ClusterConfigProto.CloudCredentials.Amazon
            cmk_arn: bytes
            cmk_key_id: bytes
            cmk_alias: bytes
            verify_ssl: bool
            ca_certificate_path: bytes
            ca_certificate: str
            def __init__(self, amazon: _Optional[_Union[ClusterConfigProto.CloudCredentials.Amazon, _Mapping]] = ..., cmk_arn: _Optional[bytes] = ..., cmk_key_id: _Optional[bytes] = ..., cmk_alias: _Optional[bytes] = ..., verify_ssl: bool = ..., ca_certificate_path: _Optional[bytes] = ..., ca_certificate: _Optional[str] = ...) -> None: ...
        class CryptsoftKMS(_message.Message):
            __slots__ = ("ip", "port", "client_certificate", "client_key", "ca_trusted_certificate", "kmip_protocol", "io_timeout", "encrypted_client_key", "additional_address_vec", "obfuscated_encrypted_client_key")
            IP_FIELD_NUMBER: _ClassVar[int]
            PORT_FIELD_NUMBER: _ClassVar[int]
            CLIENT_CERTIFICATE_FIELD_NUMBER: _ClassVar[int]
            CLIENT_KEY_FIELD_NUMBER: _ClassVar[int]
            CA_TRUSTED_CERTIFICATE_FIELD_NUMBER: _ClassVar[int]
            KMIP_PROTOCOL_FIELD_NUMBER: _ClassVar[int]
            IO_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
            ENCRYPTED_CLIENT_KEY_FIELD_NUMBER: _ClassVar[int]
            ADDITIONAL_ADDRESS_VEC_FIELD_NUMBER: _ClassVar[int]
            OBFUSCATED_ENCRYPTED_CLIENT_KEY_FIELD_NUMBER: _ClassVar[int]
            ip: str
            port: int
            client_certificate: str
            client_key: str
            ca_trusted_certificate: str
            kmip_protocol: str
            io_timeout: int
            encrypted_client_key: bytes
            additional_address_vec: _containers.RepeatedScalarFieldContainer[str]
            obfuscated_encrypted_client_key: bytes
            def __init__(self, ip: _Optional[str] = ..., port: _Optional[int] = ..., client_certificate: _Optional[str] = ..., client_key: _Optional[str] = ..., ca_trusted_certificate: _Optional[str] = ..., kmip_protocol: _Optional[str] = ..., io_timeout: _Optional[int] = ..., encrypted_client_key: _Optional[bytes] = ..., additional_address_vec: _Optional[_Iterable[str]] = ..., obfuscated_encrypted_client_key: _Optional[bytes] = ...) -> None: ...
        class Azure(_message.Message):
            __slots__ = ("owner", "cohesity_keyvault", "customer_keyvault")
            class VaultOwner(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                kCohesityManaged: _ClassVar[ClusterConfigProto.KMSConfig.Azure.VaultOwner]
                kCustomerManaged: _ClassVar[ClusterConfigProto.KMSConfig.Azure.VaultOwner]
            kCohesityManaged: ClusterConfigProto.KMSConfig.Azure.VaultOwner
            kCustomerManaged: ClusterConfigProto.KMSConfig.Azure.VaultOwner
            class KeyVault(_message.Message):
                __slots__ = ("microsoft", "keyvault_url", "key_name", "customer_secret_name")
                MICROSOFT_FIELD_NUMBER: _ClassVar[int]
                KEYVAULT_URL_FIELD_NUMBER: _ClassVar[int]
                KEY_NAME_FIELD_NUMBER: _ClassVar[int]
                CUSTOMER_SECRET_NAME_FIELD_NUMBER: _ClassVar[int]
                microsoft: ClusterConfigProto.CloudCredentials.Microsoft
                keyvault_url: str
                key_name: str
                customer_secret_name: str
                def __init__(self, microsoft: _Optional[_Union[ClusterConfigProto.CloudCredentials.Microsoft, _Mapping]] = ..., keyvault_url: _Optional[str] = ..., key_name: _Optional[str] = ..., customer_secret_name: _Optional[str] = ...) -> None: ...
            OWNER_FIELD_NUMBER: _ClassVar[int]
            COHESITY_KEYVAULT_FIELD_NUMBER: _ClassVar[int]
            CUSTOMER_KEYVAULT_FIELD_NUMBER: _ClassVar[int]
            owner: ClusterConfigProto.KMSConfig.Azure.VaultOwner
            cohesity_keyvault: ClusterConfigProto.KMSConfig.Azure.KeyVault
            customer_keyvault: ClusterConfigProto.KMSConfig.Azure.KeyVault
            def __init__(self, owner: _Optional[_Union[ClusterConfigProto.KMSConfig.Azure.VaultOwner, str]] = ..., cohesity_keyvault: _Optional[_Union[ClusterConfigProto.KMSConfig.Azure.KeyVault, _Mapping]] = ..., customer_keyvault: _Optional[_Union[ClusterConfigProto.KMSConfig.Azure.KeyVault, _Mapping]] = ...) -> None: ...
        TYPE_FIELD_NUMBER: _ClassVar[int]
        VERSION_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        AWS_FIELD_NUMBER: _ClassVar[int]
        CRYPTSOFT_KMS_FIELD_NUMBER: _ClassVar[int]
        AZURE_KMS_FIELD_NUMBER: _ClassVar[int]
        ID_FIELD_NUMBER: _ClassVar[int]
        REMOVAL_STATE_FIELD_NUMBER: _ClassVar[int]
        UPLOADED_KEY_ID_FIELD_NUMBER: _ClassVar[int]
        USAGE_TYPE_FIELD_NUMBER: _ClassVar[int]
        OWNERSHIP_CONTEXT_FIELD_NUMBER: _ClassVar[int]
        type: ClusterConfigProto.KMSConfig.Type
        version: int
        name: str
        aws: ClusterConfigProto.KMSConfig.Aws
        cryptsoft_kms: ClusterConfigProto.KMSConfig.CryptsoftKMS
        azure_kms: ClusterConfigProto.KMSConfig.Azure
        id: int
        removal_state: ClusterConfigProto.RemovalState
        uploaded_key_id: int
        usage_type: ClusterConfigProto.KMSConfig.UsageType
        ownership_context: ClusterConfigProto.OwnershipContext
        def __init__(self, type: _Optional[_Union[ClusterConfigProto.KMSConfig.Type, str]] = ..., version: _Optional[int] = ..., name: _Optional[str] = ..., aws: _Optional[_Union[ClusterConfigProto.KMSConfig.Aws, _Mapping]] = ..., cryptsoft_kms: _Optional[_Union[ClusterConfigProto.KMSConfig.CryptsoftKMS, _Mapping]] = ..., azure_kms: _Optional[_Union[ClusterConfigProto.KMSConfig.Azure, _Mapping]] = ..., id: _Optional[int] = ..., removal_state: _Optional[_Union[ClusterConfigProto.RemovalState, _Mapping]] = ..., uploaded_key_id: _Optional[int] = ..., usage_type: _Optional[_Union[ClusterConfigProto.KMSConfig.UsageType, str]] = ..., ownership_context: _Optional[_Union[ClusterConfigProto.OwnershipContext, str]] = ...) -> None: ...
    class QoSPrincipal(_message.Message):
        __slots__ = ("id", "name", "priority", "weight", "random_write_ssd_pct", "seq_write_ssd_pct", "read_ahead_enabled", "tiering_enabled", "min_requests_executing", "is_external", "workload_type", "max_data_fragment_size", "max_non_minion_data_fragment_size", "max_minion_reserve_size", "view_snap_tree_min_fanout", "view_snap_tree_fanout_min_max_ratio", "use_data_journaling", "always_use_ssd", "random_write_hydra_pct", "seq_write_hydra_pct", "inline_dedup_threshold", "app_marker_detection", "journal_downtier_enabled", "num_prefetch_level", "prefetch_threshold_num_files_in_dir", "write_io_size_seq_tier_threshold", "qos_queue_slot_scaling_factor", "should_populate_wcc_attribute", "seq_tier_min_io_size", "force_ec_inline_stripe_size", "use_faa_for_read_ahead", "use_all_tiers", "hydra_max_seq_io_size")
        class Priority(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kCritical: _ClassVar[ClusterConfigProto.QoSPrincipal.Priority]
            kHigh: _ClassVar[ClusterConfigProto.QoSPrincipal.Priority]
            kMedium: _ClassVar[ClusterConfigProto.QoSPrincipal.Priority]
            kLow: _ClassVar[ClusterConfigProto.QoSPrincipal.Priority]
            kNumPriorities: _ClassVar[ClusterConfigProto.QoSPrincipal.Priority]
            kNoPriority: _ClassVar[ClusterConfigProto.QoSPrincipal.Priority]
            kNumPrioritiesUpperLimit: _ClassVar[ClusterConfigProto.QoSPrincipal.Priority]
        kCritical: ClusterConfigProto.QoSPrincipal.Priority
        kHigh: ClusterConfigProto.QoSPrincipal.Priority
        kMedium: ClusterConfigProto.QoSPrincipal.Priority
        kLow: ClusterConfigProto.QoSPrincipal.Priority
        kNumPriorities: ClusterConfigProto.QoSPrincipal.Priority
        kNoPriority: ClusterConfigProto.QoSPrincipal.Priority
        kNumPrioritiesUpperLimit: ClusterConfigProto.QoSPrincipal.Priority
        class Workload(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kNoWorkload: _ClassVar[ClusterConfigProto.QoSPrincipal.Workload]
            kBackup: _ClassVar[ClusterConfigProto.QoSPrincipal.Workload]
            kTestAndDev: _ClassVar[ClusterConfigProto.QoSPrincipal.Workload]
            kYoda: _ClassVar[ClusterConfigProto.QoSPrincipal.Workload]
            kMadrox: _ClassVar[ClusterConfigProto.QoSPrincipal.Workload]
            kFiler: _ClassVar[ClusterConfigProto.QoSPrincipal.Workload]
        kNoWorkload: ClusterConfigProto.QoSPrincipal.Workload
        kBackup: ClusterConfigProto.QoSPrincipal.Workload
        kTestAndDev: ClusterConfigProto.QoSPrincipal.Workload
        kYoda: ClusterConfigProto.QoSPrincipal.Workload
        kMadrox: ClusterConfigProto.QoSPrincipal.Workload
        kFiler: ClusterConfigProto.QoSPrincipal.Workload
        class AppMarkerType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kNone: _ClassVar[ClusterConfigProto.QoSPrincipal.AppMarkerType]
            kCommvault: _ClassVar[ClusterConfigProto.QoSPrincipal.AppMarkerType]
        kNone: ClusterConfigProto.QoSPrincipal.AppMarkerType
        kCommvault: ClusterConfigProto.QoSPrincipal.AppMarkerType
        ID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        PRIORITY_FIELD_NUMBER: _ClassVar[int]
        WEIGHT_FIELD_NUMBER: _ClassVar[int]
        RANDOM_WRITE_SSD_PCT_FIELD_NUMBER: _ClassVar[int]
        SEQ_WRITE_SSD_PCT_FIELD_NUMBER: _ClassVar[int]
        READ_AHEAD_ENABLED_FIELD_NUMBER: _ClassVar[int]
        TIERING_ENABLED_FIELD_NUMBER: _ClassVar[int]
        MIN_REQUESTS_EXECUTING_FIELD_NUMBER: _ClassVar[int]
        IS_EXTERNAL_FIELD_NUMBER: _ClassVar[int]
        WORKLOAD_TYPE_FIELD_NUMBER: _ClassVar[int]
        MAX_DATA_FRAGMENT_SIZE_FIELD_NUMBER: _ClassVar[int]
        MAX_NON_MINION_DATA_FRAGMENT_SIZE_FIELD_NUMBER: _ClassVar[int]
        MAX_MINION_RESERVE_SIZE_FIELD_NUMBER: _ClassVar[int]
        VIEW_SNAP_TREE_MIN_FANOUT_FIELD_NUMBER: _ClassVar[int]
        VIEW_SNAP_TREE_FANOUT_MIN_MAX_RATIO_FIELD_NUMBER: _ClassVar[int]
        USE_DATA_JOURNALING_FIELD_NUMBER: _ClassVar[int]
        ALWAYS_USE_SSD_FIELD_NUMBER: _ClassVar[int]
        RANDOM_WRITE_HYDRA_PCT_FIELD_NUMBER: _ClassVar[int]
        SEQ_WRITE_HYDRA_PCT_FIELD_NUMBER: _ClassVar[int]
        INLINE_DEDUP_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
        APP_MARKER_DETECTION_FIELD_NUMBER: _ClassVar[int]
        JOURNAL_DOWNTIER_ENABLED_FIELD_NUMBER: _ClassVar[int]
        NUM_PREFETCH_LEVEL_FIELD_NUMBER: _ClassVar[int]
        PREFETCH_THRESHOLD_NUM_FILES_IN_DIR_FIELD_NUMBER: _ClassVar[int]
        WRITE_IO_SIZE_SEQ_TIER_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
        QOS_QUEUE_SLOT_SCALING_FACTOR_FIELD_NUMBER: _ClassVar[int]
        SHOULD_POPULATE_WCC_ATTRIBUTE_FIELD_NUMBER: _ClassVar[int]
        SEQ_TIER_MIN_IO_SIZE_FIELD_NUMBER: _ClassVar[int]
        FORCE_EC_INLINE_STRIPE_SIZE_FIELD_NUMBER: _ClassVar[int]
        USE_FAA_FOR_READ_AHEAD_FIELD_NUMBER: _ClassVar[int]
        USE_ALL_TIERS_FIELD_NUMBER: _ClassVar[int]
        HYDRA_MAX_SEQ_IO_SIZE_FIELD_NUMBER: _ClassVar[int]
        id: int
        name: str
        priority: ClusterConfigProto.QoSPrincipal.Priority
        weight: int
        random_write_ssd_pct: int
        seq_write_ssd_pct: int
        read_ahead_enabled: bool
        tiering_enabled: bool
        min_requests_executing: int
        is_external: bool
        workload_type: str
        max_data_fragment_size: int
        max_non_minion_data_fragment_size: int
        max_minion_reserve_size: int
        view_snap_tree_min_fanout: int
        view_snap_tree_fanout_min_max_ratio: int
        use_data_journaling: bool
        always_use_ssd: bool
        random_write_hydra_pct: int
        seq_write_hydra_pct: int
        inline_dedup_threshold: int
        app_marker_detection: ClusterConfigProto.QoSPrincipal.AppMarkerType
        journal_downtier_enabled: bool
        num_prefetch_level: int
        prefetch_threshold_num_files_in_dir: int
        write_io_size_seq_tier_threshold: int
        qos_queue_slot_scaling_factor: int
        should_populate_wcc_attribute: bool
        seq_tier_min_io_size: int
        force_ec_inline_stripe_size: int
        use_faa_for_read_ahead: bool
        use_all_tiers: bool
        hydra_max_seq_io_size: int
        def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., priority: _Optional[_Union[ClusterConfigProto.QoSPrincipal.Priority, str]] = ..., weight: _Optional[int] = ..., random_write_ssd_pct: _Optional[int] = ..., seq_write_ssd_pct: _Optional[int] = ..., read_ahead_enabled: bool = ..., tiering_enabled: bool = ..., min_requests_executing: _Optional[int] = ..., is_external: bool = ..., workload_type: _Optional[str] = ..., max_data_fragment_size: _Optional[int] = ..., max_non_minion_data_fragment_size: _Optional[int] = ..., max_minion_reserve_size: _Optional[int] = ..., view_snap_tree_min_fanout: _Optional[int] = ..., view_snap_tree_fanout_min_max_ratio: _Optional[int] = ..., use_data_journaling: bool = ..., always_use_ssd: bool = ..., random_write_hydra_pct: _Optional[int] = ..., seq_write_hydra_pct: _Optional[int] = ..., inline_dedup_threshold: _Optional[int] = ..., app_marker_detection: _Optional[_Union[ClusterConfigProto.QoSPrincipal.AppMarkerType, str]] = ..., journal_downtier_enabled: bool = ..., num_prefetch_level: _Optional[int] = ..., prefetch_threshold_num_files_in_dir: _Optional[int] = ..., write_io_size_seq_tier_threshold: _Optional[int] = ..., qos_queue_slot_scaling_factor: _Optional[int] = ..., should_populate_wcc_attribute: bool = ..., seq_tier_min_io_size: _Optional[int] = ..., force_ec_inline_stripe_size: _Optional[int] = ..., use_faa_for_read_ahead: bool = ..., use_all_tiers: bool = ..., hydra_max_seq_io_size: _Optional[int] = ...) -> None: ...
    class QosPrincipalMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: ClusterConfigProto.QoSPrincipal
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[ClusterConfigProto.QoSPrincipal, _Mapping]] = ...) -> None: ...
    class Component(_message.Message):
        __slots__ = ()
        class QoSComponent(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kUnknown: _ClassVar[ClusterConfigProto.Component.QoSComponent]
            kMagneto: _ClassVar[ClusterConfigProto.Component.QoSComponent]
            kYoda: _ClassVar[ClusterConfigProto.Component.QoSComponent]
            kMadrox: _ClassVar[ClusterConfigProto.Component.QoSComponent]
            kApollo: _ClassVar[ClusterConfigProto.Component.QoSComponent]
            kIcebox: _ClassVar[ClusterConfigProto.Component.QoSComponent]
            kUser: _ClassVar[ClusterConfigProto.Component.QoSComponent]
            kAthena: _ClassVar[ClusterConfigProto.Component.QoSComponent]
            kAthenaApp: _ClassVar[ClusterConfigProto.Component.QoSComponent]
            kBridgeInternal: _ClassVar[ClusterConfigProto.Component.QoSComponent]
            kMagnetoFileBased: _ClassVar[ClusterConfigProto.Component.QoSComponent]
            kEagleAgent: _ClassVar[ClusterConfigProto.Component.QoSComponent]
            kGaia: _ClassVar[ClusterConfigProto.Component.QoSComponent]
        kUnknown: ClusterConfigProto.Component.QoSComponent
        kMagneto: ClusterConfigProto.Component.QoSComponent
        kYoda: ClusterConfigProto.Component.QoSComponent
        kMadrox: ClusterConfigProto.Component.QoSComponent
        kApollo: ClusterConfigProto.Component.QoSComponent
        kIcebox: ClusterConfigProto.Component.QoSComponent
        kUser: ClusterConfigProto.Component.QoSComponent
        kAthena: ClusterConfigProto.Component.QoSComponent
        kAthenaApp: ClusterConfigProto.Component.QoSComponent
        kBridgeInternal: ClusterConfigProto.Component.QoSComponent
        kMagnetoFileBased: ClusterConfigProto.Component.QoSComponent
        kEagleAgent: ClusterConfigProto.Component.QoSComponent
        kGaia: ClusterConfigProto.Component.QoSComponent
        def __init__(self) -> None: ...
    class QoSMapping(_message.Message):
        __slots__ = ("qos_context", "principal_id")
        class QoSContext(_message.Message):
            __slots__ = ("type", "priority", "view_box_id", "view_id", "component")
            class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                kHydra: _ClassVar[ClusterConfigProto.QoSMapping.QoSContext.Type]
                kMagneto: _ClassVar[ClusterConfigProto.QoSMapping.QoSContext.Type]
                kSystem: _ClassVar[ClusterConfigProto.QoSMapping.QoSContext.Type]
                kUser: _ClassVar[ClusterConfigProto.QoSMapping.QoSContext.Type]
                kYoda: _ClassVar[ClusterConfigProto.QoSMapping.QoSContext.Type]
                kCloud: _ClassVar[ClusterConfigProto.QoSMapping.QoSContext.Type]
                kGaia: _ClassVar[ClusterConfigProto.QoSMapping.QoSContext.Type]
            kHydra: ClusterConfigProto.QoSMapping.QoSContext.Type
            kMagneto: ClusterConfigProto.QoSMapping.QoSContext.Type
            kSystem: ClusterConfigProto.QoSMapping.QoSContext.Type
            kUser: ClusterConfigProto.QoSMapping.QoSContext.Type
            kYoda: ClusterConfigProto.QoSMapping.QoSContext.Type
            kCloud: ClusterConfigProto.QoSMapping.QoSContext.Type
            kGaia: ClusterConfigProto.QoSMapping.QoSContext.Type
            TYPE_FIELD_NUMBER: _ClassVar[int]
            PRIORITY_FIELD_NUMBER: _ClassVar[int]
            VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
            VIEW_ID_FIELD_NUMBER: _ClassVar[int]
            COMPONENT_FIELD_NUMBER: _ClassVar[int]
            type: ClusterConfigProto.QoSMapping.QoSContext.Type
            priority: ClusterConfigProto.QoSPrincipal.Priority
            view_box_id: int
            view_id: int
            component: ClusterConfigProto.Component.QoSComponent
            def __init__(self, type: _Optional[_Union[ClusterConfigProto.QoSMapping.QoSContext.Type, str]] = ..., priority: _Optional[_Union[ClusterConfigProto.QoSPrincipal.Priority, str]] = ..., view_box_id: _Optional[int] = ..., view_id: _Optional[int] = ..., component: _Optional[_Union[ClusterConfigProto.Component.QoSComponent, str]] = ...) -> None: ...
        QOS_CONTEXT_FIELD_NUMBER: _ClassVar[int]
        PRINCIPAL_ID_FIELD_NUMBER: _ClassVar[int]
        qos_context: ClusterConfigProto.QoSMapping.QoSContext
        principal_id: int
        def __init__(self, qos_context: _Optional[_Union[ClusterConfigProto.QoSMapping.QoSContext, _Mapping]] = ..., principal_id: _Optional[int] = ...) -> None: ...
    class BandwidthChangeWindow(_message.Message):
        __slots__ = ("day_of_week_vec", "from_hour", "from_minutes", "to_hour", "to_minutes", "rate_limit_bytes_per_sec", "is_all_day", "io_rate")
        DAY_OF_WEEK_VEC_FIELD_NUMBER: _ClassVar[int]
        FROM_HOUR_FIELD_NUMBER: _ClassVar[int]
        FROM_MINUTES_FIELD_NUMBER: _ClassVar[int]
        TO_HOUR_FIELD_NUMBER: _ClassVar[int]
        TO_MINUTES_FIELD_NUMBER: _ClassVar[int]
        RATE_LIMIT_BYTES_PER_SEC_FIELD_NUMBER: _ClassVar[int]
        IS_ALL_DAY_FIELD_NUMBER: _ClassVar[int]
        IO_RATE_FIELD_NUMBER: _ClassVar[int]
        day_of_week_vec: _containers.RepeatedScalarFieldContainer[int]
        from_hour: int
        from_minutes: int
        to_hour: int
        to_minutes: int
        rate_limit_bytes_per_sec: int
        is_all_day: bool
        io_rate: ClusterConfigProto.BandwidthLimit.BackgroundIORate
        def __init__(self, day_of_week_vec: _Optional[_Iterable[int]] = ..., from_hour: _Optional[int] = ..., from_minutes: _Optional[int] = ..., to_hour: _Optional[int] = ..., to_minutes: _Optional[int] = ..., rate_limit_bytes_per_sec: _Optional[int] = ..., is_all_day: bool = ..., io_rate: _Optional[_Union[ClusterConfigProto.BandwidthLimit.BackgroundIORate, str]] = ...) -> None: ...
    class BandwidthLimit(_message.Message):
        __slots__ = ("rate_limit_bytes_per_sec", "bw_change_windows_vec", "timezone", "io_rate")
        class BackgroundIORate(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kHigh: _ClassVar[ClusterConfigProto.BandwidthLimit.BackgroundIORate]
            kMedium: _ClassVar[ClusterConfigProto.BandwidthLimit.BackgroundIORate]
            kLow: _ClassVar[ClusterConfigProto.BandwidthLimit.BackgroundIORate]
            kNoActivity: _ClassVar[ClusterConfigProto.BandwidthLimit.BackgroundIORate]
        kHigh: ClusterConfigProto.BandwidthLimit.BackgroundIORate
        kMedium: ClusterConfigProto.BandwidthLimit.BackgroundIORate
        kLow: ClusterConfigProto.BandwidthLimit.BackgroundIORate
        kNoActivity: ClusterConfigProto.BandwidthLimit.BackgroundIORate
        RATE_LIMIT_BYTES_PER_SEC_FIELD_NUMBER: _ClassVar[int]
        BW_CHANGE_WINDOWS_VEC_FIELD_NUMBER: _ClassVar[int]
        TIMEZONE_FIELD_NUMBER: _ClassVar[int]
        IO_RATE_FIELD_NUMBER: _ClassVar[int]
        rate_limit_bytes_per_sec: int
        bw_change_windows_vec: _containers.RepeatedCompositeFieldContainer[ClusterConfigProto.BandwidthChangeWindow]
        timezone: str
        io_rate: ClusterConfigProto.BandwidthLimit.BackgroundIORate
        def __init__(self, rate_limit_bytes_per_sec: _Optional[int] = ..., bw_change_windows_vec: _Optional[_Iterable[_Union[ClusterConfigProto.BandwidthChangeWindow, _Mapping]]] = ..., timezone: _Optional[str] = ..., io_rate: _Optional[_Union[ClusterConfigProto.BandwidthLimit.BackgroundIORate, str]] = ...) -> None: ...
    class BandwidthLimits(_message.Message):
        __slots__ = ("upload_bw_limit", "download_bw_limit")
        UPLOAD_BW_LIMIT_FIELD_NUMBER: _ClassVar[int]
        DOWNLOAD_BW_LIMIT_FIELD_NUMBER: _ClassVar[int]
        upload_bw_limit: ClusterConfigProto.BandwidthLimit
        download_bw_limit: ClusterConfigProto.BandwidthLimit
        def __init__(self, upload_bw_limit: _Optional[_Union[ClusterConfigProto.BandwidthLimit, _Mapping]] = ..., download_bw_limit: _Optional[_Union[ClusterConfigProto.BandwidthLimit, _Mapping]] = ...) -> None: ...
    class RemoteCluster(_message.Message):
        __slots__ = ("name", "cluster_id", "cluster_incarnation_id", "is_stale", "proxy_endpt_vec", "rate_limit_bytes_per_second", "all_endpoints_reachable", "view_box_map", "user_name", "encrypted_password", "network_interface_id_vec", "cluster_endpoints", "compression_enabled", "key_encryption_key", "bw_limit", "vlan_id", "purpose_replication", "purpose_remote_access", "remote_access_credentials", "tenant_id", "remote_tenant_id", "vlan_interface_name", "interface_group_id", "interface_group", "auto_registration", "auto_sync_remote", "use_bifrost_broker_channel", "is_odp_pairing", "multi_tenancy_enabled", "tenant_viewbox_sharing_enabled", "cluster_aes_encryption_mode", "tls_enabled")
        class ProxyEndpt(_message.Message):
            __slots__ = ("ip", "port", "iris_port")
            IP_FIELD_NUMBER: _ClassVar[int]
            PORT_FIELD_NUMBER: _ClassVar[int]
            IRIS_PORT_FIELD_NUMBER: _ClassVar[int]
            ip: str
            port: int
            iris_port: int
            def __init__(self, ip: _Optional[str] = ..., port: _Optional[int] = ..., iris_port: _Optional[int] = ...) -> None: ...
        class RemoteViewBox(_message.Message):
            __slots__ = ("view_box_id", "view_box_name")
            VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
            VIEW_BOX_NAME_FIELD_NUMBER: _ClassVar[int]
            view_box_id: int
            view_box_name: str
            def __init__(self, view_box_id: _Optional[int] = ..., view_box_name: _Optional[str] = ...) -> None: ...
        class ViewBoxMapEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: int
            value: ClusterConfigProto.RemoteCluster.RemoteViewBox
            def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[ClusterConfigProto.RemoteCluster.RemoteViewBox, _Mapping]] = ...) -> None: ...
        class IrisCredentials(_message.Message):
            __slots__ = ("user_name", "user_domain", "encrypted_password")
            USER_NAME_FIELD_NUMBER: _ClassVar[int]
            USER_DOMAIN_FIELD_NUMBER: _ClassVar[int]
            ENCRYPTED_PASSWORD_FIELD_NUMBER: _ClassVar[int]
            user_name: str
            user_domain: str
            encrypted_password: bytes
            def __init__(self, user_name: _Optional[str] = ..., user_domain: _Optional[str] = ..., encrypted_password: _Optional[bytes] = ...) -> None: ...
        NAME_FIELD_NUMBER: _ClassVar[int]
        CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
        CLUSTER_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
        IS_STALE_FIELD_NUMBER: _ClassVar[int]
        PROXY_ENDPT_VEC_FIELD_NUMBER: _ClassVar[int]
        RATE_LIMIT_BYTES_PER_SECOND_FIELD_NUMBER: _ClassVar[int]
        ALL_ENDPOINTS_REACHABLE_FIELD_NUMBER: _ClassVar[int]
        VIEW_BOX_MAP_FIELD_NUMBER: _ClassVar[int]
        USER_NAME_FIELD_NUMBER: _ClassVar[int]
        ENCRYPTED_PASSWORD_FIELD_NUMBER: _ClassVar[int]
        NETWORK_INTERFACE_ID_VEC_FIELD_NUMBER: _ClassVar[int]
        CLUSTER_ENDPOINTS_FIELD_NUMBER: _ClassVar[int]
        COMPRESSION_ENABLED_FIELD_NUMBER: _ClassVar[int]
        KEY_ENCRYPTION_KEY_FIELD_NUMBER: _ClassVar[int]
        BW_LIMIT_FIELD_NUMBER: _ClassVar[int]
        VLAN_ID_FIELD_NUMBER: _ClassVar[int]
        PURPOSE_REPLICATION_FIELD_NUMBER: _ClassVar[int]
        PURPOSE_REMOTE_ACCESS_FIELD_NUMBER: _ClassVar[int]
        REMOTE_ACCESS_CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
        TENANT_ID_FIELD_NUMBER: _ClassVar[int]
        REMOTE_TENANT_ID_FIELD_NUMBER: _ClassVar[int]
        VLAN_INTERFACE_NAME_FIELD_NUMBER: _ClassVar[int]
        INTERFACE_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
        INTERFACE_GROUP_FIELD_NUMBER: _ClassVar[int]
        AUTO_REGISTRATION_FIELD_NUMBER: _ClassVar[int]
        AUTO_SYNC_REMOTE_FIELD_NUMBER: _ClassVar[int]
        USE_BIFROST_BROKER_CHANNEL_FIELD_NUMBER: _ClassVar[int]
        IS_ODP_PAIRING_FIELD_NUMBER: _ClassVar[int]
        MULTI_TENANCY_ENABLED_FIELD_NUMBER: _ClassVar[int]
        TENANT_VIEWBOX_SHARING_ENABLED_FIELD_NUMBER: _ClassVar[int]
        CLUSTER_AES_ENCRYPTION_MODE_FIELD_NUMBER: _ClassVar[int]
        TLS_ENABLED_FIELD_NUMBER: _ClassVar[int]
        name: str
        cluster_id: int
        cluster_incarnation_id: int
        is_stale: bool
        proxy_endpt_vec: _containers.RepeatedCompositeFieldContainer[ClusterConfigProto.RemoteCluster.ProxyEndpt]
        rate_limit_bytes_per_second: int
        all_endpoints_reachable: bool
        view_box_map: _containers.MessageMap[int, ClusterConfigProto.RemoteCluster.RemoteViewBox]
        user_name: str
        encrypted_password: bytes
        network_interface_id_vec: _containers.RepeatedScalarFieldContainer[int]
        cluster_endpoints: _containers.RepeatedScalarFieldContainer[str]
        compression_enabled: bool
        key_encryption_key: bytes
        bw_limit: ClusterConfigProto.BandwidthLimit
        vlan_id: int
        purpose_replication: bool
        purpose_remote_access: bool
        remote_access_credentials: ClusterConfigProto.RemoteCluster.IrisCredentials
        tenant_id: str
        remote_tenant_id: str
        vlan_interface_name: str
        interface_group_id: int
        interface_group: str
        auto_registration: bool
        auto_sync_remote: bool
        use_bifrost_broker_channel: bool
        is_odp_pairing: bool
        multi_tenancy_enabled: bool
        tenant_viewbox_sharing_enabled: bool
        cluster_aes_encryption_mode: int
        tls_enabled: bool
        def __init__(self, name: _Optional[str] = ..., cluster_id: _Optional[int] = ..., cluster_incarnation_id: _Optional[int] = ..., is_stale: bool = ..., proxy_endpt_vec: _Optional[_Iterable[_Union[ClusterConfigProto.RemoteCluster.ProxyEndpt, _Mapping]]] = ..., rate_limit_bytes_per_second: _Optional[int] = ..., all_endpoints_reachable: bool = ..., view_box_map: _Optional[_Mapping[int, ClusterConfigProto.RemoteCluster.RemoteViewBox]] = ..., user_name: _Optional[str] = ..., encrypted_password: _Optional[bytes] = ..., network_interface_id_vec: _Optional[_Iterable[int]] = ..., cluster_endpoints: _Optional[_Iterable[str]] = ..., compression_enabled: bool = ..., key_encryption_key: _Optional[bytes] = ..., bw_limit: _Optional[_Union[ClusterConfigProto.BandwidthLimit, _Mapping]] = ..., vlan_id: _Optional[int] = ..., purpose_replication: bool = ..., purpose_remote_access: bool = ..., remote_access_credentials: _Optional[_Union[ClusterConfigProto.RemoteCluster.IrisCredentials, _Mapping]] = ..., tenant_id: _Optional[str] = ..., remote_tenant_id: _Optional[str] = ..., vlan_interface_name: _Optional[str] = ..., interface_group_id: _Optional[int] = ..., interface_group: _Optional[str] = ..., auto_registration: bool = ..., auto_sync_remote: bool = ..., use_bifrost_broker_channel: bool = ..., is_odp_pairing: bool = ..., multi_tenancy_enabled: bool = ..., tenant_viewbox_sharing_enabled: bool = ..., cluster_aes_encryption_mode: _Optional[int] = ..., tls_enabled: bool = ...) -> None: ...
    class CloudCredentials(_message.Message):
        __slots__ = ("type", "google", "amazon", "microsoft", "session_credentials_expiry_time_usecs")
        class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kGoogle: _ClassVar[ClusterConfigProto.CloudCredentials.Type]
            kAmazon: _ClassVar[ClusterConfigProto.CloudCredentials.Type]
            kMicrosoft: _ClassVar[ClusterConfigProto.CloudCredentials.Type]
        kGoogle: ClusterConfigProto.CloudCredentials.Type
        kAmazon: ClusterConfigProto.CloudCredentials.Type
        kMicrosoft: ClusterConfigProto.CloudCredentials.Type
        class AwsAuthMethod(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kUseIAMUser: _ClassVar[ClusterConfigProto.CloudCredentials.AwsAuthMethod]
            kUseIAMRole: _ClassVar[ClusterConfigProto.CloudCredentials.AwsAuthMethod]
            kUseSTS: _ClassVar[ClusterConfigProto.CloudCredentials.AwsAuthMethod]
            kUseHelios: _ClassVar[ClusterConfigProto.CloudCredentials.AwsAuthMethod]
            kUseInstanceProfile: _ClassVar[ClusterConfigProto.CloudCredentials.AwsAuthMethod]
        kUseIAMUser: ClusterConfigProto.CloudCredentials.AwsAuthMethod
        kUseIAMRole: ClusterConfigProto.CloudCredentials.AwsAuthMethod
        kUseSTS: ClusterConfigProto.CloudCredentials.AwsAuthMethod
        kUseHelios: ClusterConfigProto.CloudCredentials.AwsAuthMethod
        kUseInstanceProfile: ClusterConfigProto.CloudCredentials.AwsAuthMethod
        class Google(_message.Message):
            __slots__ = ("project_id", "client_email_address", "encrypted_client_private_key")
            PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
            CLIENT_EMAIL_ADDRESS_FIELD_NUMBER: _ClassVar[int]
            ENCRYPTED_CLIENT_PRIVATE_KEY_FIELD_NUMBER: _ClassVar[int]
            project_id: str
            client_email_address: str
            encrypted_client_private_key: bytes
            def __init__(self, project_id: _Optional[str] = ..., client_email_address: _Optional[str] = ..., encrypted_client_private_key: _Optional[bytes] = ...) -> None: ...
        class Amazon(_message.Message):
            __slots__ = ("auth_method", "access_key_id", "encrypted_secret_access_key", "credential_endpoint", "encrypted_credential_blob", "region", "hostname", "use_https", "signature_version", "s3_acceleration_enabled", "c2s_cap_server_info", "iam_role_arn", "iam_role_arn_vec", "iam_role_arn_read_only_access", "assume_role_session_creds", "bucket_owner_account_id")
            class C2SCapServerInfo(_message.Message):
                __slots__ = ("agency", "mission", "role", "encrypted_password", "base_url", "gandalf_certificate_key")
                AGENCY_FIELD_NUMBER: _ClassVar[int]
                MISSION_FIELD_NUMBER: _ClassVar[int]
                ROLE_FIELD_NUMBER: _ClassVar[int]
                ENCRYPTED_PASSWORD_FIELD_NUMBER: _ClassVar[int]
                BASE_URL_FIELD_NUMBER: _ClassVar[int]
                GANDALF_CERTIFICATE_KEY_FIELD_NUMBER: _ClassVar[int]
                agency: str
                mission: str
                role: str
                encrypted_password: bytes
                base_url: str
                gandalf_certificate_key: str
                def __init__(self, agency: _Optional[str] = ..., mission: _Optional[str] = ..., role: _Optional[str] = ..., encrypted_password: _Optional[bytes] = ..., base_url: _Optional[str] = ..., gandalf_certificate_key: _Optional[str] = ...) -> None: ...
            class AssumeRoleSessionCredentials(_message.Message):
                __slots__ = ("access_key_id", "encrypted_secret_access_key", "session_token")
                ACCESS_KEY_ID_FIELD_NUMBER: _ClassVar[int]
                ENCRYPTED_SECRET_ACCESS_KEY_FIELD_NUMBER: _ClassVar[int]
                SESSION_TOKEN_FIELD_NUMBER: _ClassVar[int]
                access_key_id: str
                encrypted_secret_access_key: bytes
                session_token: bytes
                def __init__(self, access_key_id: _Optional[str] = ..., encrypted_secret_access_key: _Optional[bytes] = ..., session_token: _Optional[bytes] = ...) -> None: ...
            AUTH_METHOD_FIELD_NUMBER: _ClassVar[int]
            ACCESS_KEY_ID_FIELD_NUMBER: _ClassVar[int]
            ENCRYPTED_SECRET_ACCESS_KEY_FIELD_NUMBER: _ClassVar[int]
            CREDENTIAL_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
            ENCRYPTED_CREDENTIAL_BLOB_FIELD_NUMBER: _ClassVar[int]
            REGION_FIELD_NUMBER: _ClassVar[int]
            HOSTNAME_FIELD_NUMBER: _ClassVar[int]
            USE_HTTPS_FIELD_NUMBER: _ClassVar[int]
            SIGNATURE_VERSION_FIELD_NUMBER: _ClassVar[int]
            S3_ACCELERATION_ENABLED_FIELD_NUMBER: _ClassVar[int]
            C2S_CAP_SERVER_INFO_FIELD_NUMBER: _ClassVar[int]
            IAM_ROLE_ARN_FIELD_NUMBER: _ClassVar[int]
            IAM_ROLE_ARN_VEC_FIELD_NUMBER: _ClassVar[int]
            IAM_ROLE_ARN_READ_ONLY_ACCESS_FIELD_NUMBER: _ClassVar[int]
            ASSUME_ROLE_SESSION_CREDS_FIELD_NUMBER: _ClassVar[int]
            BUCKET_OWNER_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
            auth_method: ClusterConfigProto.CloudCredentials.AwsAuthMethod
            access_key_id: str
            encrypted_secret_access_key: bytes
            credential_endpoint: str
            encrypted_credential_blob: bytes
            region: str
            hostname: str
            use_https: bool
            signature_version: int
            s3_acceleration_enabled: bool
            c2s_cap_server_info: ClusterConfigProto.CloudCredentials.Amazon.C2SCapServerInfo
            iam_role_arn: str
            iam_role_arn_vec: _containers.RepeatedScalarFieldContainer[str]
            iam_role_arn_read_only_access: str
            assume_role_session_creds: ClusterConfigProto.CloudCredentials.Amazon.AssumeRoleSessionCredentials
            bucket_owner_account_id: str
            def __init__(self, auth_method: _Optional[_Union[ClusterConfigProto.CloudCredentials.AwsAuthMethod, str]] = ..., access_key_id: _Optional[str] = ..., encrypted_secret_access_key: _Optional[bytes] = ..., credential_endpoint: _Optional[str] = ..., encrypted_credential_blob: _Optional[bytes] = ..., region: _Optional[str] = ..., hostname: _Optional[str] = ..., use_https: bool = ..., signature_version: _Optional[int] = ..., s3_acceleration_enabled: bool = ..., c2s_cap_server_info: _Optional[_Union[ClusterConfigProto.CloudCredentials.Amazon.C2SCapServerInfo, _Mapping]] = ..., iam_role_arn: _Optional[str] = ..., iam_role_arn_vec: _Optional[_Iterable[str]] = ..., iam_role_arn_read_only_access: _Optional[str] = ..., assume_role_session_creds: _Optional[_Union[ClusterConfigProto.CloudCredentials.Amazon.AssumeRoleSessionCredentials, _Mapping]] = ..., bucket_owner_account_id: _Optional[str] = ...) -> None: ...
        class Microsoft(_message.Message):
            __slots__ = ("storage_account_name", "encrypted_storage_access_key", "encrypted_sas_url", "azure_stack_region", "azure_stack_hub_domain_name", "lambda_function_app_name", "encrypted_lambda_function_app_deployment_key", "resource_group", "subscription_id", "application_id", "encrypted_application_key", "tenant_id", "client_id", "encrypted_client_secret", "auth_method", "encrypted_sas_token", "region")
            class MicrosoftAuthMethod(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                kAzureAuthNone: _ClassVar[ClusterConfigProto.CloudCredentials.Microsoft.MicrosoftAuthMethod]
                kAzureClientSecret: _ClassVar[ClusterConfigProto.CloudCredentials.Microsoft.MicrosoftAuthMethod]
                kAzureManagedIdentity: _ClassVar[ClusterConfigProto.CloudCredentials.Microsoft.MicrosoftAuthMethod]
                kUseHelios: _ClassVar[ClusterConfigProto.CloudCredentials.Microsoft.MicrosoftAuthMethod]
            kAzureAuthNone: ClusterConfigProto.CloudCredentials.Microsoft.MicrosoftAuthMethod
            kAzureClientSecret: ClusterConfigProto.CloudCredentials.Microsoft.MicrosoftAuthMethod
            kAzureManagedIdentity: ClusterConfigProto.CloudCredentials.Microsoft.MicrosoftAuthMethod
            kUseHelios: ClusterConfigProto.CloudCredentials.Microsoft.MicrosoftAuthMethod
            STORAGE_ACCOUNT_NAME_FIELD_NUMBER: _ClassVar[int]
            ENCRYPTED_STORAGE_ACCESS_KEY_FIELD_NUMBER: _ClassVar[int]
            ENCRYPTED_SAS_URL_FIELD_NUMBER: _ClassVar[int]
            AZURE_STACK_REGION_FIELD_NUMBER: _ClassVar[int]
            AZURE_STACK_HUB_DOMAIN_NAME_FIELD_NUMBER: _ClassVar[int]
            LAMBDA_FUNCTION_APP_NAME_FIELD_NUMBER: _ClassVar[int]
            ENCRYPTED_LAMBDA_FUNCTION_APP_DEPLOYMENT_KEY_FIELD_NUMBER: _ClassVar[int]
            RESOURCE_GROUP_FIELD_NUMBER: _ClassVar[int]
            SUBSCRIPTION_ID_FIELD_NUMBER: _ClassVar[int]
            APPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
            ENCRYPTED_APPLICATION_KEY_FIELD_NUMBER: _ClassVar[int]
            TENANT_ID_FIELD_NUMBER: _ClassVar[int]
            CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
            ENCRYPTED_CLIENT_SECRET_FIELD_NUMBER: _ClassVar[int]
            AUTH_METHOD_FIELD_NUMBER: _ClassVar[int]
            ENCRYPTED_SAS_TOKEN_FIELD_NUMBER: _ClassVar[int]
            REGION_FIELD_NUMBER: _ClassVar[int]
            storage_account_name: str
            encrypted_storage_access_key: bytes
            encrypted_sas_url: bytes
            azure_stack_region: str
            azure_stack_hub_domain_name: str
            lambda_function_app_name: str
            encrypted_lambda_function_app_deployment_key: bytes
            resource_group: str
            subscription_id: str
            application_id: str
            encrypted_application_key: bytes
            tenant_id: str
            client_id: str
            encrypted_client_secret: bytes
            auth_method: ClusterConfigProto.CloudCredentials.Microsoft.MicrosoftAuthMethod
            encrypted_sas_token: str
            region: str
            def __init__(self, storage_account_name: _Optional[str] = ..., encrypted_storage_access_key: _Optional[bytes] = ..., encrypted_sas_url: _Optional[bytes] = ..., azure_stack_region: _Optional[str] = ..., azure_stack_hub_domain_name: _Optional[str] = ..., lambda_function_app_name: _Optional[str] = ..., encrypted_lambda_function_app_deployment_key: _Optional[bytes] = ..., resource_group: _Optional[str] = ..., subscription_id: _Optional[str] = ..., application_id: _Optional[str] = ..., encrypted_application_key: _Optional[bytes] = ..., tenant_id: _Optional[str] = ..., client_id: _Optional[str] = ..., encrypted_client_secret: _Optional[bytes] = ..., auth_method: _Optional[_Union[ClusterConfigProto.CloudCredentials.Microsoft.MicrosoftAuthMethod, str]] = ..., encrypted_sas_token: _Optional[str] = ..., region: _Optional[str] = ...) -> None: ...
        TYPE_FIELD_NUMBER: _ClassVar[int]
        GOOGLE_FIELD_NUMBER: _ClassVar[int]
        AMAZON_FIELD_NUMBER: _ClassVar[int]
        MICROSOFT_FIELD_NUMBER: _ClassVar[int]
        SESSION_CREDENTIALS_EXPIRY_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
        type: ClusterConfigProto.CloudCredentials.Type
        google: ClusterConfigProto.CloudCredentials.Google
        amazon: ClusterConfigProto.CloudCredentials.Amazon
        microsoft: ClusterConfigProto.CloudCredentials.Microsoft
        session_credentials_expiry_time_usecs: int
        def __init__(self, type: _Optional[_Union[ClusterConfigProto.CloudCredentials.Type, str]] = ..., google: _Optional[_Union[ClusterConfigProto.CloudCredentials.Google, _Mapping]] = ..., amazon: _Optional[_Union[ClusterConfigProto.CloudCredentials.Amazon, _Mapping]] = ..., microsoft: _Optional[_Union[ClusterConfigProto.CloudCredentials.Microsoft, _Mapping]] = ..., session_credentials_expiry_time_usecs: _Optional[int] = ...) -> None: ...
    class MediaServerCredentials(_message.Message):
        __slots__ = ("type", "qstar")
        class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kQStar: _ClassVar[ClusterConfigProto.MediaServerCredentials.Type]
        kQStar: ClusterConfigProto.MediaServerCredentials.Type
        class QStar(_message.Message):
            __slots__ = ("user_name", "encrypted_password", "host", "port", "use_https", "share_type")
            USER_NAME_FIELD_NUMBER: _ClassVar[int]
            ENCRYPTED_PASSWORD_FIELD_NUMBER: _ClassVar[int]
            HOST_FIELD_NUMBER: _ClassVar[int]
            PORT_FIELD_NUMBER: _ClassVar[int]
            USE_HTTPS_FIELD_NUMBER: _ClassVar[int]
            SHARE_TYPE_FIELD_NUMBER: _ClassVar[int]
            user_name: str
            encrypted_password: bytes
            host: str
            port: int
            use_https: bool
            share_type: ClusterConfigProto.ShareType
            def __init__(self, user_name: _Optional[str] = ..., encrypted_password: _Optional[bytes] = ..., host: _Optional[str] = ..., port: _Optional[int] = ..., use_https: bool = ..., share_type: _Optional[_Union[ClusterConfigProto.ShareType, str]] = ...) -> None: ...
        TYPE_FIELD_NUMBER: _ClassVar[int]
        QSTAR_FIELD_NUMBER: _ClassVar[int]
        type: ClusterConfigProto.MediaServerCredentials.Type
        qstar: ClusterConfigProto.MediaServerCredentials.QStar
        def __init__(self, type: _Optional[_Union[ClusterConfigProto.MediaServerCredentials.Type, str]] = ..., qstar: _Optional[_Union[ClusterConfigProto.MediaServerCredentials.QStar, _Mapping]] = ...) -> None: ...
    class NASServerCredentials(_message.Message):
        __slots__ = ("host", "mount_path", "share_type", "user_name", "encrypted_password", "nfs_version_number", "nfs_security_type", "kerberos_realm_name")
        HOST_FIELD_NUMBER: _ClassVar[int]
        MOUNT_PATH_FIELD_NUMBER: _ClassVar[int]
        SHARE_TYPE_FIELD_NUMBER: _ClassVar[int]
        USER_NAME_FIELD_NUMBER: _ClassVar[int]
        ENCRYPTED_PASSWORD_FIELD_NUMBER: _ClassVar[int]
        NFS_VERSION_NUMBER_FIELD_NUMBER: _ClassVar[int]
        NFS_SECURITY_TYPE_FIELD_NUMBER: _ClassVar[int]
        KERBEROS_REALM_NAME_FIELD_NUMBER: _ClassVar[int]
        host: str
        mount_path: str
        share_type: ClusterConfigProto.ShareType
        user_name: str
        encrypted_password: bytes
        nfs_version_number: ClusterConfigProto.NfsVersionNumber
        nfs_security_type: ClusterConfigProto.NfsSecurityType
        kerberos_realm_name: str
        def __init__(self, host: _Optional[str] = ..., mount_path: _Optional[str] = ..., share_type: _Optional[_Union[ClusterConfigProto.ShareType, str]] = ..., user_name: _Optional[str] = ..., encrypted_password: _Optional[bytes] = ..., nfs_version_number: _Optional[_Union[ClusterConfigProto.NfsVersionNumber, str]] = ..., nfs_security_type: _Optional[_Union[ClusterConfigProto.NfsSecurityType, str]] = ..., kerberos_realm_name: _Optional[str] = ...) -> None: ...
    class ArchivalDomain(_message.Message):
        __slots__ = ("domain_uid", "is_cluster_owner")
        DOMAIN_UID_FIELD_NUMBER: _ClassVar[int]
        IS_CLUSTER_OWNER_FIELD_NUMBER: _ClassVar[int]
        domain_uid: _universal_id_pb2.UniversalIdProto
        is_cluster_owner: bool
        def __init__(self, domain_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., is_cluster_owner: bool = ...) -> None: ...
    class Vault(_message.Message):
        __slots__ = ("id", "uid", "global_uuid", "name", "description", "type", "self_fault_tolerant", "config", "removal_state", "force_delete", "delete_vault_error_message", "usage_type", "dedup_enabled", "incremental_archives_enabled", "full_archive_interval_days", "key_file_download_time_usecs", "create_time_usecs", "customer_managing_encryption_keys", "key_file_download_user", "update_time_usecs", "compression_level", "encryption_level", "encryption_config", "random_nonce", "bw_limits", "uploaded_dek_uid_vec", "domain_uid", "cad_config", "cloud_domain_vec", "tenant_id_vec", "version", "forever_incremental_archives_enabled", "on_prem_vault_info", "pending_vault_setup_ngce", "is_remote_vault", "remote_vault_info", "is_worm_capable", "is_worm_bucket_policy_set", "ownership_context", "worm_lock_in_compliance_mode", "is_data_in_remote_env", "credentials_encrypted_using_keychain")
        class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kNearline: _ClassVar[ClusterConfigProto.Vault.Type]
            kGlacier: _ClassVar[ClusterConfigProto.Vault.Type]
            kS3: _ClassVar[ClusterConfigProto.Vault.Type]
            kAzureStandard: _ClassVar[ClusterConfigProto.Vault.Type]
            kS3Compatible: _ClassVar[ClusterConfigProto.Vault.Type]
            kQStarTape: _ClassVar[ClusterConfigProto.Vault.Type]
            kGoogleStandard: _ClassVar[ClusterConfigProto.Vault.Type]
            kGoogleDRA: _ClassVar[ClusterConfigProto.Vault.Type]
            kAmazonS3StandardIA: _ClassVar[ClusterConfigProto.Vault.Type]
            kS3Gov: _ClassVar[ClusterConfigProto.Vault.Type]
            kNAS: _ClassVar[ClusterConfigProto.Vault.Type]
            kColdline: _ClassVar[ClusterConfigProto.Vault.Type]
            kAzureGovCloud: _ClassVar[ClusterConfigProto.Vault.Type]
            kAzureArchive: _ClassVar[ClusterConfigProto.Vault.Type]
            kAzure: _ClassVar[ClusterConfigProto.Vault.Type]
            kGoogle: _ClassVar[ClusterConfigProto.Vault.Type]
            kAmazon: _ClassVar[ClusterConfigProto.Vault.Type]
            kOracle: _ClassVar[ClusterConfigProto.Vault.Type]
            kOracleTierStandard: _ClassVar[ClusterConfigProto.Vault.Type]
            kOracleTierArchive: _ClassVar[ClusterConfigProto.Vault.Type]
            kAmazonC2S: _ClassVar[ClusterConfigProto.Vault.Type]
            kAzureStackCommercial: _ClassVar[ClusterConfigProto.Vault.Type]
            kAzureStackADFS: _ClassVar[ClusterConfigProto.Vault.Type]
        kNearline: ClusterConfigProto.Vault.Type
        kGlacier: ClusterConfigProto.Vault.Type
        kS3: ClusterConfigProto.Vault.Type
        kAzureStandard: ClusterConfigProto.Vault.Type
        kS3Compatible: ClusterConfigProto.Vault.Type
        kQStarTape: ClusterConfigProto.Vault.Type
        kGoogleStandard: ClusterConfigProto.Vault.Type
        kGoogleDRA: ClusterConfigProto.Vault.Type
        kAmazonS3StandardIA: ClusterConfigProto.Vault.Type
        kS3Gov: ClusterConfigProto.Vault.Type
        kNAS: ClusterConfigProto.Vault.Type
        kColdline: ClusterConfigProto.Vault.Type
        kAzureGovCloud: ClusterConfigProto.Vault.Type
        kAzureArchive: ClusterConfigProto.Vault.Type
        kAzure: ClusterConfigProto.Vault.Type
        kGoogle: ClusterConfigProto.Vault.Type
        kAmazon: ClusterConfigProto.Vault.Type
        kOracle: ClusterConfigProto.Vault.Type
        kOracleTierStandard: ClusterConfigProto.Vault.Type
        kOracleTierArchive: ClusterConfigProto.Vault.Type
        kAmazonC2S: ClusterConfigProto.Vault.Type
        kAzureStackCommercial: ClusterConfigProto.Vault.Type
        kAzureStackADFS: ClusterConfigProto.Vault.Type
        class UsageType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kArchival: _ClassVar[ClusterConfigProto.Vault.UsageType]
            kCloudSpill: _ClassVar[ClusterConfigProto.Vault.UsageType]
            kRpaasArchival: _ClassVar[ClusterConfigProto.Vault.UsageType]
        kArchival: ClusterConfigProto.Vault.UsageType
        kCloudSpill: ClusterConfigProto.Vault.UsageType
        kRpaasArchival: ClusterConfigProto.Vault.UsageType
        class CloudVaultConfig(_message.Message):
            __slots__ = ("credentials", "name", "is_on_prem", "cloud_properties")
            CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
            NAME_FIELD_NUMBER: _ClassVar[int]
            IS_ON_PREM_FIELD_NUMBER: _ClassVar[int]
            CLOUD_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
            credentials: ClusterConfigProto.CloudCredentials
            name: str
            is_on_prem: bool
            cloud_properties: ClusterConfigProto.Vault.CloudProperties
            def __init__(self, credentials: _Optional[_Union[ClusterConfigProto.CloudCredentials, _Mapping]] = ..., name: _Optional[str] = ..., is_on_prem: bool = ..., cloud_properties: _Optional[_Union[ClusterConfigProto.Vault.CloudProperties, _Mapping]] = ...) -> None: ...
        class CloudProperties(_message.Message):
            __slots__ = ("azure_properties", "google_properties", "amazon_properties", "oracle_properties", "s3_compatible_properties")
            class AzureProperties(_message.Message):
                __slots__ = ("tier_type", "enable_lambda_based_gc", "lambda_function_version", "worm_enabled")
                class TierType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                    __slots__ = ()
                    kAzureTierHot: _ClassVar[ClusterConfigProto.Vault.CloudProperties.AzureProperties.TierType]
                    kAzureTierCool: _ClassVar[ClusterConfigProto.Vault.CloudProperties.AzureProperties.TierType]
                    kAzureTierArchive: _ClassVar[ClusterConfigProto.Vault.CloudProperties.AzureProperties.TierType]
                kAzureTierHot: ClusterConfigProto.Vault.CloudProperties.AzureProperties.TierType
                kAzureTierCool: ClusterConfigProto.Vault.CloudProperties.AzureProperties.TierType
                kAzureTierArchive: ClusterConfigProto.Vault.CloudProperties.AzureProperties.TierType
                TIER_TYPE_FIELD_NUMBER: _ClassVar[int]
                ENABLE_LAMBDA_BASED_GC_FIELD_NUMBER: _ClassVar[int]
                LAMBDA_FUNCTION_VERSION_FIELD_NUMBER: _ClassVar[int]
                WORM_ENABLED_FIELD_NUMBER: _ClassVar[int]
                tier_type: ClusterConfigProto.Vault.CloudProperties.AzureProperties.TierType
                enable_lambda_based_gc: bool
                lambda_function_version: int
                worm_enabled: bool
                def __init__(self, tier_type: _Optional[_Union[ClusterConfigProto.Vault.CloudProperties.AzureProperties.TierType, str]] = ..., enable_lambda_based_gc: bool = ..., lambda_function_version: _Optional[int] = ..., worm_enabled: bool = ...) -> None: ...
            class GoogleProperties(_message.Message):
                __slots__ = ("tier_type",)
                class TierType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                    __slots__ = ()
                    kGoogleStandard: _ClassVar[ClusterConfigProto.Vault.CloudProperties.GoogleProperties.TierType]
                    kGoogleNearline: _ClassVar[ClusterConfigProto.Vault.CloudProperties.GoogleProperties.TierType]
                    kGoogleColdline: _ClassVar[ClusterConfigProto.Vault.CloudProperties.GoogleProperties.TierType]
                    kGoogleRegional: _ClassVar[ClusterConfigProto.Vault.CloudProperties.GoogleProperties.TierType]
                    kGoogleMultiRegional: _ClassVar[ClusterConfigProto.Vault.CloudProperties.GoogleProperties.TierType]
                kGoogleStandard: ClusterConfigProto.Vault.CloudProperties.GoogleProperties.TierType
                kGoogleNearline: ClusterConfigProto.Vault.CloudProperties.GoogleProperties.TierType
                kGoogleColdline: ClusterConfigProto.Vault.CloudProperties.GoogleProperties.TierType
                kGoogleRegional: ClusterConfigProto.Vault.CloudProperties.GoogleProperties.TierType
                kGoogleMultiRegional: ClusterConfigProto.Vault.CloudProperties.GoogleProperties.TierType
                TIER_TYPE_FIELD_NUMBER: _ClassVar[int]
                tier_type: ClusterConfigProto.Vault.CloudProperties.GoogleProperties.TierType
                def __init__(self, tier_type: _Optional[_Union[ClusterConfigProto.Vault.CloudProperties.GoogleProperties.TierType, str]] = ...) -> None: ...
            class AmazonProperties(_message.Message):
                __slots__ = ("tier_type", "enable_lambda_based_gc", "lambda_function_version")
                class TierType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                    __slots__ = ()
                    kNone: _ClassVar[ClusterConfigProto.Vault.CloudProperties.AmazonProperties.TierType]
                    kAmazonS3Standard: _ClassVar[ClusterConfigProto.Vault.CloudProperties.AmazonProperties.TierType]
                    kAmazonS3StandardIA: _ClassVar[ClusterConfigProto.Vault.CloudProperties.AmazonProperties.TierType]
                    kAmazonGlacier: _ClassVar[ClusterConfigProto.Vault.CloudProperties.AmazonProperties.TierType]
                    kAmazonS3OneZoneIA: _ClassVar[ClusterConfigProto.Vault.CloudProperties.AmazonProperties.TierType]
                    kAmazonS3IntelligentTiering: _ClassVar[ClusterConfigProto.Vault.CloudProperties.AmazonProperties.TierType]
                    kAmazonS3Glacier: _ClassVar[ClusterConfigProto.Vault.CloudProperties.AmazonProperties.TierType]
                    kAmazonS3GlacierDeepArchive: _ClassVar[ClusterConfigProto.Vault.CloudProperties.AmazonProperties.TierType]
                    kAmazonS3GlacierIR: _ClassVar[ClusterConfigProto.Vault.CloudProperties.AmazonProperties.TierType]
                kNone: ClusterConfigProto.Vault.CloudProperties.AmazonProperties.TierType
                kAmazonS3Standard: ClusterConfigProto.Vault.CloudProperties.AmazonProperties.TierType
                kAmazonS3StandardIA: ClusterConfigProto.Vault.CloudProperties.AmazonProperties.TierType
                kAmazonGlacier: ClusterConfigProto.Vault.CloudProperties.AmazonProperties.TierType
                kAmazonS3OneZoneIA: ClusterConfigProto.Vault.CloudProperties.AmazonProperties.TierType
                kAmazonS3IntelligentTiering: ClusterConfigProto.Vault.CloudProperties.AmazonProperties.TierType
                kAmazonS3Glacier: ClusterConfigProto.Vault.CloudProperties.AmazonProperties.TierType
                kAmazonS3GlacierDeepArchive: ClusterConfigProto.Vault.CloudProperties.AmazonProperties.TierType
                kAmazonS3GlacierIR: ClusterConfigProto.Vault.CloudProperties.AmazonProperties.TierType
                TIER_TYPE_FIELD_NUMBER: _ClassVar[int]
                ENABLE_LAMBDA_BASED_GC_FIELD_NUMBER: _ClassVar[int]
                LAMBDA_FUNCTION_VERSION_FIELD_NUMBER: _ClassVar[int]
                tier_type: ClusterConfigProto.Vault.CloudProperties.AmazonProperties.TierType
                enable_lambda_based_gc: bool
                lambda_function_version: int
                def __init__(self, tier_type: _Optional[_Union[ClusterConfigProto.Vault.CloudProperties.AmazonProperties.TierType, str]] = ..., enable_lambda_based_gc: bool = ..., lambda_function_version: _Optional[int] = ...) -> None: ...
            class OracleProperties(_message.Message):
                __slots__ = ("tier_type", "tenant")
                class TierType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                    __slots__ = ()
                    kOracleTierStandard: _ClassVar[ClusterConfigProto.Vault.CloudProperties.OracleProperties.TierType]
                    kOracleTierArchive: _ClassVar[ClusterConfigProto.Vault.CloudProperties.OracleProperties.TierType]
                kOracleTierStandard: ClusterConfigProto.Vault.CloudProperties.OracleProperties.TierType
                kOracleTierArchive: ClusterConfigProto.Vault.CloudProperties.OracleProperties.TierType
                TIER_TYPE_FIELD_NUMBER: _ClassVar[int]
                TENANT_FIELD_NUMBER: _ClassVar[int]
                tier_type: ClusterConfigProto.Vault.CloudProperties.OracleProperties.TierType
                tenant: str
                def __init__(self, tier_type: _Optional[_Union[ClusterConfigProto.Vault.CloudProperties.OracleProperties.TierType, str]] = ..., tenant: _Optional[str] = ...) -> None: ...
            class S3CompatibleProperties(_message.Message):
                __slots__ = ("tier_type",)
                class TierType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                    __slots__ = ()
                    kS3CompatibleStandard: _ClassVar[ClusterConfigProto.Vault.CloudProperties.S3CompatibleProperties.TierType]
                    kS3CompatibleTape: _ClassVar[ClusterConfigProto.Vault.CloudProperties.S3CompatibleProperties.TierType]
                kS3CompatibleStandard: ClusterConfigProto.Vault.CloudProperties.S3CompatibleProperties.TierType
                kS3CompatibleTape: ClusterConfigProto.Vault.CloudProperties.S3CompatibleProperties.TierType
                TIER_TYPE_FIELD_NUMBER: _ClassVar[int]
                tier_type: ClusterConfigProto.Vault.CloudProperties.S3CompatibleProperties.TierType
                def __init__(self, tier_type: _Optional[_Union[ClusterConfigProto.Vault.CloudProperties.S3CompatibleProperties.TierType, str]] = ...) -> None: ...
            AZURE_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
            GOOGLE_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
            AMAZON_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
            ORACLE_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
            S3_COMPATIBLE_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
            azure_properties: ClusterConfigProto.Vault.CloudProperties.AzureProperties
            google_properties: ClusterConfigProto.Vault.CloudProperties.GoogleProperties
            amazon_properties: ClusterConfigProto.Vault.CloudProperties.AmazonProperties
            oracle_properties: ClusterConfigProto.Vault.CloudProperties.OracleProperties
            s3_compatible_properties: ClusterConfigProto.Vault.CloudProperties.S3CompatibleProperties
            def __init__(self, azure_properties: _Optional[_Union[ClusterConfigProto.Vault.CloudProperties.AzureProperties, _Mapping]] = ..., google_properties: _Optional[_Union[ClusterConfigProto.Vault.CloudProperties.GoogleProperties, _Mapping]] = ..., amazon_properties: _Optional[_Union[ClusterConfigProto.Vault.CloudProperties.AmazonProperties, _Mapping]] = ..., oracle_properties: _Optional[_Union[ClusterConfigProto.Vault.CloudProperties.OracleProperties, _Mapping]] = ..., s3_compatible_properties: _Optional[_Union[ClusterConfigProto.Vault.CloudProperties.S3CompatibleProperties, _Mapping]] = ...) -> None: ...
        class CloudTierType(_message.Message):
            __slots__ = ("cloud_type", "cloud_properties")
            CLOUD_TYPE_FIELD_NUMBER: _ClassVar[int]
            CLOUD_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
            cloud_type: ClusterConfigProto.Vault.Type
            cloud_properties: ClusterConfigProto.Vault.CloudProperties
            def __init__(self, cloud_type: _Optional[_Union[ClusterConfigProto.Vault.Type, str]] = ..., cloud_properties: _Optional[_Union[ClusterConfigProto.Vault.CloudProperties, _Mapping]] = ...) -> None: ...
        class CloudTierInfo(_message.Message):
            __slots__ = ("target_tier_type", "num_secs_to_move_after", "honor_tier_info")
            TARGET_TIER_TYPE_FIELD_NUMBER: _ClassVar[int]
            NUM_SECS_TO_MOVE_AFTER_FIELD_NUMBER: _ClassVar[int]
            HONOR_TIER_INFO_FIELD_NUMBER: _ClassVar[int]
            target_tier_type: ClusterConfigProto.Vault.CloudTierType
            num_secs_to_move_after: int
            honor_tier_info: bool
            def __init__(self, target_tier_type: _Optional[_Union[ClusterConfigProto.Vault.CloudTierType, _Mapping]] = ..., num_secs_to_move_after: _Optional[int] = ..., honor_tier_info: bool = ...) -> None: ...
        class CloudTierSetting(_message.Message):
            __slots__ = ("tier_info_vec",)
            TIER_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
            tier_info_vec: _containers.RepeatedCompositeFieldContainer[ClusterConfigProto.Vault.CloudTierInfo]
            def __init__(self, tier_info_vec: _Optional[_Iterable[_Union[ClusterConfigProto.Vault.CloudTierInfo, _Mapping]]] = ...) -> None: ...
        class TapeVaultConfig(_message.Message):
            __slots__ = ("credentials", "volume_name_vec")
            CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
            VOLUME_NAME_VEC_FIELD_NUMBER: _ClassVar[int]
            credentials: ClusterConfigProto.MediaServerCredentials
            volume_name_vec: _containers.RepeatedScalarFieldContainer[str]
            def __init__(self, credentials: _Optional[_Union[ClusterConfigProto.MediaServerCredentials, _Mapping]] = ..., volume_name_vec: _Optional[_Iterable[str]] = ...) -> None: ...
        class NASVaultConfig(_message.Message):
            __slots__ = ("credentials",)
            CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
            credentials: ClusterConfigProto.NASServerCredentials
            def __init__(self, credentials: _Optional[_Union[ClusterConfigProto.NASServerCredentials, _Mapping]] = ...) -> None: ...
        class Config(_message.Message):
            __slots__ = ("cloud_vault_config", "tape_vault_config", "nas_vault_config")
            CLOUD_VAULT_CONFIG_FIELD_NUMBER: _ClassVar[int]
            TAPE_VAULT_CONFIG_FIELD_NUMBER: _ClassVar[int]
            NAS_VAULT_CONFIG_FIELD_NUMBER: _ClassVar[int]
            cloud_vault_config: ClusterConfigProto.Vault.CloudVaultConfig
            tape_vault_config: ClusterConfigProto.Vault.TapeVaultConfig
            nas_vault_config: ClusterConfigProto.Vault.NASVaultConfig
            def __init__(self, cloud_vault_config: _Optional[_Union[ClusterConfigProto.Vault.CloudVaultConfig, _Mapping]] = ..., tape_vault_config: _Optional[_Union[ClusterConfigProto.Vault.TapeVaultConfig, _Mapping]] = ..., nas_vault_config: _Optional[_Union[ClusterConfigProto.Vault.NASVaultConfig, _Mapping]] = ...) -> None: ...
        class EncryptionConfig(_message.Message):
            __slots__ = ("encrypted_data_encryption_key", "encryption_key_rotation_period_hours", "dek_uid", "kek_uid", "kms_server_id", "dek_rotation_enabled", "fixed_dek_key_id", "current_dek_key_id", "edek_info")
            class EdekProto(_message.Message):
                __slots__ = ("key_id", "edek", "gcm_edek")
                KEY_ID_FIELD_NUMBER: _ClassVar[int]
                EDEK_FIELD_NUMBER: _ClassVar[int]
                GCM_EDEK_FIELD_NUMBER: _ClassVar[int]
                key_id: int
                edek: bytes
                gcm_edek: bytes
                def __init__(self, key_id: _Optional[int] = ..., edek: _Optional[bytes] = ..., gcm_edek: _Optional[bytes] = ...) -> None: ...
            ENCRYPTED_DATA_ENCRYPTION_KEY_FIELD_NUMBER: _ClassVar[int]
            ENCRYPTION_KEY_ROTATION_PERIOD_HOURS_FIELD_NUMBER: _ClassVar[int]
            DEK_UID_FIELD_NUMBER: _ClassVar[int]
            KEK_UID_FIELD_NUMBER: _ClassVar[int]
            KMS_SERVER_ID_FIELD_NUMBER: _ClassVar[int]
            DEK_ROTATION_ENABLED_FIELD_NUMBER: _ClassVar[int]
            FIXED_DEK_KEY_ID_FIELD_NUMBER: _ClassVar[int]
            CURRENT_DEK_KEY_ID_FIELD_NUMBER: _ClassVar[int]
            EDEK_INFO_FIELD_NUMBER: _ClassVar[int]
            encrypted_data_encryption_key: bytes
            encryption_key_rotation_period_hours: int
            dek_uid: _universal_id_pb2.UniversalIdProto
            kek_uid: _universal_id_pb2.UniversalIdProto
            kms_server_id: int
            dek_rotation_enabled: bool
            fixed_dek_key_id: int
            current_dek_key_id: int
            edek_info: ClusterConfigProto.Vault.EncryptionConfig.EdekProto
            def __init__(self, encrypted_data_encryption_key: _Optional[bytes] = ..., encryption_key_rotation_period_hours: _Optional[int] = ..., dek_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., kek_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., kms_server_id: _Optional[int] = ..., dek_rotation_enabled: bool = ..., fixed_dek_key_id: _Optional[int] = ..., current_dek_key_id: _Optional[int] = ..., edek_info: _Optional[_Union[ClusterConfigProto.Vault.EncryptionConfig.EdekProto, _Mapping]] = ...) -> None: ...
        class ChecksumType(_message.Message):
            __slots__ = ()
            class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                kNone: _ClassVar[ClusterConfigProto.Vault.ChecksumType.Type]
                kMD5: _ClassVar[ClusterConfigProto.Vault.ChecksumType.Type]
                kSha256: _ClassVar[ClusterConfigProto.Vault.ChecksumType.Type]
                kSha256Tree: _ClassVar[ClusterConfigProto.Vault.ChecksumType.Type]
            kNone: ClusterConfigProto.Vault.ChecksumType.Type
            kMD5: ClusterConfigProto.Vault.ChecksumType.Type
            kSha256: ClusterConfigProto.Vault.ChecksumType.Type
            kSha256Tree: ClusterConfigProto.Vault.ChecksumType.Type
            def __init__(self) -> None: ...
        class CADConfig(_message.Message):
            __slots__ = ("domain_namespace", "physical_quota")
            DOMAIN_NAMESPACE_FIELD_NUMBER: _ClassVar[int]
            PHYSICAL_QUOTA_FIELD_NUMBER: _ClassVar[int]
            domain_namespace: str
            physical_quota: ClusterConfigProto.QuotaPolicy
            def __init__(self, domain_namespace: _Optional[str] = ..., physical_quota: _Optional[_Union[ClusterConfigProto.QuotaPolicy, _Mapping]] = ...) -> None: ...
        class CloudDomainEncryptionDetails(_message.Message):
            __slots__ = ("is_encrypted", "dek_uid", "use_vault_kms")
            IS_ENCRYPTED_FIELD_NUMBER: _ClassVar[int]
            DEK_UID_FIELD_NUMBER: _ClassVar[int]
            USE_VAULT_KMS_FIELD_NUMBER: _ClassVar[int]
            is_encrypted: bool
            dek_uid: _universal_id_pb2.UniversalIdProto
            use_vault_kms: bool
            def __init__(self, is_encrypted: bool = ..., dek_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., use_vault_kms: bool = ...) -> None: ...
        class CloudDomain(_message.Message):
            __slots__ = ("domain_id", "view_box_id", "domain_namespace", "read_write_mode", "encryption_details", "cluster_id", "cluster_incarnation_id", "migration_complete", "removal_state", "rebuilt_csr_scribe_table", "rebuilt_ccfm_scribe_table", "version")
            DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
            VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
            DOMAIN_NAMESPACE_FIELD_NUMBER: _ClassVar[int]
            READ_WRITE_MODE_FIELD_NUMBER: _ClassVar[int]
            ENCRYPTION_DETAILS_FIELD_NUMBER: _ClassVar[int]
            CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
            CLUSTER_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
            MIGRATION_COMPLETE_FIELD_NUMBER: _ClassVar[int]
            REMOVAL_STATE_FIELD_NUMBER: _ClassVar[int]
            REBUILT_CSR_SCRIBE_TABLE_FIELD_NUMBER: _ClassVar[int]
            REBUILT_CCFM_SCRIBE_TABLE_FIELD_NUMBER: _ClassVar[int]
            VERSION_FIELD_NUMBER: _ClassVar[int]
            domain_id: int
            view_box_id: int
            domain_namespace: str
            read_write_mode: bool
            encryption_details: ClusterConfigProto.Vault.CloudDomainEncryptionDetails
            cluster_id: int
            cluster_incarnation_id: int
            migration_complete: bool
            removal_state: ClusterConfigProto.RemovalState
            rebuilt_csr_scribe_table: bool
            rebuilt_ccfm_scribe_table: bool
            version: int
            def __init__(self, domain_id: _Optional[int] = ..., view_box_id: _Optional[int] = ..., domain_namespace: _Optional[str] = ..., read_write_mode: bool = ..., encryption_details: _Optional[_Union[ClusterConfigProto.Vault.CloudDomainEncryptionDetails, _Mapping]] = ..., cluster_id: _Optional[int] = ..., cluster_incarnation_id: _Optional[int] = ..., migration_complete: bool = ..., removal_state: _Optional[_Union[ClusterConfigProto.RemovalState, _Mapping]] = ..., rebuilt_csr_scribe_table: bool = ..., rebuilt_ccfm_scribe_table: bool = ..., version: _Optional[int] = ...) -> None: ...
        class OnPremVaultInfo(_message.Message):
            __slots__ = ("is_aws_snowball", "is_azure_databox", "is_google_transfer_appliance")
            IS_AWS_SNOWBALL_FIELD_NUMBER: _ClassVar[int]
            IS_AZURE_DATABOX_FIELD_NUMBER: _ClassVar[int]
            IS_GOOGLE_TRANSFER_APPLIANCE_FIELD_NUMBER: _ClassVar[int]
            is_aws_snowball: bool
            is_azure_databox: bool
            is_google_transfer_appliance: bool
            def __init__(self, is_aws_snowball: bool = ..., is_azure_databox: bool = ..., is_google_transfer_appliance: bool = ...) -> None: ...
        class RemoteVaultInfo(_message.Message):
            __slots__ = ("cluster_id", "vault_id", "remote_cloud_domain_vec", "rigel_guid")
            class RemoteCloudDomain(_message.Message):
                __slots__ = ("local_domain_id", "remote_domain_id", "viewbox_id")
                LOCAL_DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
                REMOTE_DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
                VIEWBOX_ID_FIELD_NUMBER: _ClassVar[int]
                local_domain_id: int
                remote_domain_id: int
                viewbox_id: int
                def __init__(self, local_domain_id: _Optional[int] = ..., remote_domain_id: _Optional[int] = ..., viewbox_id: _Optional[int] = ...) -> None: ...
            CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
            VAULT_ID_FIELD_NUMBER: _ClassVar[int]
            REMOTE_CLOUD_DOMAIN_VEC_FIELD_NUMBER: _ClassVar[int]
            RIGEL_GUID_FIELD_NUMBER: _ClassVar[int]
            cluster_id: int
            vault_id: int
            remote_cloud_domain_vec: _containers.RepeatedCompositeFieldContainer[ClusterConfigProto.Vault.RemoteVaultInfo.RemoteCloudDomain]
            rigel_guid: int
            def __init__(self, cluster_id: _Optional[int] = ..., vault_id: _Optional[int] = ..., remote_cloud_domain_vec: _Optional[_Iterable[_Union[ClusterConfigProto.Vault.RemoteVaultInfo.RemoteCloudDomain, _Mapping]]] = ..., rigel_guid: _Optional[int] = ...) -> None: ...
        ID_FIELD_NUMBER: _ClassVar[int]
        UID_FIELD_NUMBER: _ClassVar[int]
        GLOBAL_UUID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        SELF_FAULT_TOLERANT_FIELD_NUMBER: _ClassVar[int]
        CONFIG_FIELD_NUMBER: _ClassVar[int]
        REMOVAL_STATE_FIELD_NUMBER: _ClassVar[int]
        FORCE_DELETE_FIELD_NUMBER: _ClassVar[int]
        DELETE_VAULT_ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
        USAGE_TYPE_FIELD_NUMBER: _ClassVar[int]
        DEDUP_ENABLED_FIELD_NUMBER: _ClassVar[int]
        INCREMENTAL_ARCHIVES_ENABLED_FIELD_NUMBER: _ClassVar[int]
        FULL_ARCHIVE_INTERVAL_DAYS_FIELD_NUMBER: _ClassVar[int]
        KEY_FILE_DOWNLOAD_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
        CREATE_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
        CUSTOMER_MANAGING_ENCRYPTION_KEYS_FIELD_NUMBER: _ClassVar[int]
        KEY_FILE_DOWNLOAD_USER_FIELD_NUMBER: _ClassVar[int]
        UPDATE_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
        COMPRESSION_LEVEL_FIELD_NUMBER: _ClassVar[int]
        ENCRYPTION_LEVEL_FIELD_NUMBER: _ClassVar[int]
        ENCRYPTION_CONFIG_FIELD_NUMBER: _ClassVar[int]
        RANDOM_NONCE_FIELD_NUMBER: _ClassVar[int]
        BW_LIMITS_FIELD_NUMBER: _ClassVar[int]
        UPLOADED_DEK_UID_VEC_FIELD_NUMBER: _ClassVar[int]
        DOMAIN_UID_FIELD_NUMBER: _ClassVar[int]
        CAD_CONFIG_FIELD_NUMBER: _ClassVar[int]
        CLOUD_DOMAIN_VEC_FIELD_NUMBER: _ClassVar[int]
        TENANT_ID_VEC_FIELD_NUMBER: _ClassVar[int]
        VERSION_FIELD_NUMBER: _ClassVar[int]
        FOREVER_INCREMENTAL_ARCHIVES_ENABLED_FIELD_NUMBER: _ClassVar[int]
        ON_PREM_VAULT_INFO_FIELD_NUMBER: _ClassVar[int]
        PENDING_VAULT_SETUP_NGCE_FIELD_NUMBER: _ClassVar[int]
        IS_REMOTE_VAULT_FIELD_NUMBER: _ClassVar[int]
        REMOTE_VAULT_INFO_FIELD_NUMBER: _ClassVar[int]
        IS_WORM_CAPABLE_FIELD_NUMBER: _ClassVar[int]
        IS_WORM_BUCKET_POLICY_SET_FIELD_NUMBER: _ClassVar[int]
        OWNERSHIP_CONTEXT_FIELD_NUMBER: _ClassVar[int]
        WORM_LOCK_IN_COMPLIANCE_MODE_FIELD_NUMBER: _ClassVar[int]
        IS_DATA_IN_REMOTE_ENV_FIELD_NUMBER: _ClassVar[int]
        CREDENTIALS_ENCRYPTED_USING_KEYCHAIN_FIELD_NUMBER: _ClassVar[int]
        id: int
        uid: _universal_id_pb2.UniversalIdProto
        global_uuid: str
        name: str
        description: str
        type: ClusterConfigProto.Vault.Type
        self_fault_tolerant: bool
        config: ClusterConfigProto.Vault.Config
        removal_state: ClusterConfigProto.RemovalState
        force_delete: bool
        delete_vault_error_message: str
        usage_type: ClusterConfigProto.Vault.UsageType
        dedup_enabled: bool
        incremental_archives_enabled: bool
        full_archive_interval_days: float
        key_file_download_time_usecs: int
        create_time_usecs: int
        customer_managing_encryption_keys: bool
        key_file_download_user: str
        update_time_usecs: int
        compression_level: ClusterConfigProto.StoragePolicy.CompressionLevel
        encryption_level: ClusterConfigProto.EncryptionLevel
        encryption_config: ClusterConfigProto.Vault.EncryptionConfig
        random_nonce: bytes
        bw_limits: ClusterConfigProto.BandwidthLimits
        uploaded_dek_uid_vec: _containers.RepeatedCompositeFieldContainer[_universal_id_pb2.UniversalIdProto]
        domain_uid: _universal_id_pb2.UniversalIdProto
        cad_config: ClusterConfigProto.Vault.CADConfig
        cloud_domain_vec: _containers.RepeatedCompositeFieldContainer[ClusterConfigProto.Vault.CloudDomain]
        tenant_id_vec: _containers.RepeatedScalarFieldContainer[str]
        version: int
        forever_incremental_archives_enabled: bool
        on_prem_vault_info: ClusterConfigProto.Vault.OnPremVaultInfo
        pending_vault_setup_ngce: bool
        is_remote_vault: bool
        remote_vault_info: ClusterConfigProto.Vault.RemoteVaultInfo
        is_worm_capable: bool
        is_worm_bucket_policy_set: bool
        ownership_context: ClusterConfigProto.OwnershipContext
        worm_lock_in_compliance_mode: bool
        is_data_in_remote_env: bool
        credentials_encrypted_using_keychain: bool
        def __init__(self, id: _Optional[int] = ..., uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., global_uuid: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., type: _Optional[_Union[ClusterConfigProto.Vault.Type, str]] = ..., self_fault_tolerant: bool = ..., config: _Optional[_Union[ClusterConfigProto.Vault.Config, _Mapping]] = ..., removal_state: _Optional[_Union[ClusterConfigProto.RemovalState, _Mapping]] = ..., force_delete: bool = ..., delete_vault_error_message: _Optional[str] = ..., usage_type: _Optional[_Union[ClusterConfigProto.Vault.UsageType, str]] = ..., dedup_enabled: bool = ..., incremental_archives_enabled: bool = ..., full_archive_interval_days: _Optional[float] = ..., key_file_download_time_usecs: _Optional[int] = ..., create_time_usecs: _Optional[int] = ..., customer_managing_encryption_keys: bool = ..., key_file_download_user: _Optional[str] = ..., update_time_usecs: _Optional[int] = ..., compression_level: _Optional[_Union[ClusterConfigProto.StoragePolicy.CompressionLevel, str]] = ..., encryption_level: _Optional[_Union[ClusterConfigProto.EncryptionLevel, str]] = ..., encryption_config: _Optional[_Union[ClusterConfigProto.Vault.EncryptionConfig, _Mapping]] = ..., random_nonce: _Optional[bytes] = ..., bw_limits: _Optional[_Union[ClusterConfigProto.BandwidthLimits, _Mapping]] = ..., uploaded_dek_uid_vec: _Optional[_Iterable[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]]] = ..., domain_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., cad_config: _Optional[_Union[ClusterConfigProto.Vault.CADConfig, _Mapping]] = ..., cloud_domain_vec: _Optional[_Iterable[_Union[ClusterConfigProto.Vault.CloudDomain, _Mapping]]] = ..., tenant_id_vec: _Optional[_Iterable[str]] = ..., version: _Optional[int] = ..., forever_incremental_archives_enabled: bool = ..., on_prem_vault_info: _Optional[_Union[ClusterConfigProto.Vault.OnPremVaultInfo, _Mapping]] = ..., pending_vault_setup_ngce: bool = ..., is_remote_vault: bool = ..., remote_vault_info: _Optional[_Union[ClusterConfigProto.Vault.RemoteVaultInfo, _Mapping]] = ..., is_worm_capable: bool = ..., is_worm_bucket_policy_set: bool = ..., ownership_context: _Optional[_Union[ClusterConfigProto.OwnershipContext, str]] = ..., worm_lock_in_compliance_mode: bool = ..., is_data_in_remote_env: bool = ..., credentials_encrypted_using_keychain: bool = ...) -> None: ...
    class QoSPrincipalWorkload(_message.Message):
        __slots__ = ("name",)
        NAME_FIELD_NUMBER: _ClassVar[int]
        name: str
        def __init__(self, name: _Optional[str] = ...) -> None: ...
    class DefaultQoSPrincipalNames(_message.Message):
        __slots__ = ("critical", "high", "medium", "low")
        CRITICAL_FIELD_NUMBER: _ClassVar[int]
        HIGH_FIELD_NUMBER: _ClassVar[int]
        MEDIUM_FIELD_NUMBER: _ClassVar[int]
        LOW_FIELD_NUMBER: _ClassVar[int]
        critical: str
        high: str
        medium: str
        low: str
        def __init__(self, critical: _Optional[str] = ..., high: _Optional[str] = ..., medium: _Optional[str] = ..., low: _Optional[str] = ...) -> None: ...
    class InitialQoSPrincipalWeights(_message.Message):
        __slots__ = ("default_weight", "system", "yoda", "magneto", "backup", "user_low", "test_dev", "madrox", "filer", "hydra_low", "hydra_high", "cloud_low", "cloud_medium", "cloud_high", "cloud_critical")
        DEFAULT_WEIGHT_FIELD_NUMBER: _ClassVar[int]
        SYSTEM_FIELD_NUMBER: _ClassVar[int]
        YODA_FIELD_NUMBER: _ClassVar[int]
        MAGNETO_FIELD_NUMBER: _ClassVar[int]
        BACKUP_FIELD_NUMBER: _ClassVar[int]
        USER_LOW_FIELD_NUMBER: _ClassVar[int]
        TEST_DEV_FIELD_NUMBER: _ClassVar[int]
        MADROX_FIELD_NUMBER: _ClassVar[int]
        FILER_FIELD_NUMBER: _ClassVar[int]
        HYDRA_LOW_FIELD_NUMBER: _ClassVar[int]
        HYDRA_HIGH_FIELD_NUMBER: _ClassVar[int]
        CLOUD_LOW_FIELD_NUMBER: _ClassVar[int]
        CLOUD_MEDIUM_FIELD_NUMBER: _ClassVar[int]
        CLOUD_HIGH_FIELD_NUMBER: _ClassVar[int]
        CLOUD_CRITICAL_FIELD_NUMBER: _ClassVar[int]
        default_weight: int
        system: int
        yoda: int
        magneto: int
        backup: int
        user_low: int
        test_dev: int
        madrox: int
        filer: int
        hydra_low: int
        hydra_high: int
        cloud_low: int
        cloud_medium: int
        cloud_high: int
        cloud_critical: int
        def __init__(self, default_weight: _Optional[int] = ..., system: _Optional[int] = ..., yoda: _Optional[int] = ..., magneto: _Optional[int] = ..., backup: _Optional[int] = ..., user_low: _Optional[int] = ..., test_dev: _Optional[int] = ..., madrox: _Optional[int] = ..., filer: _Optional[int] = ..., hydra_low: _Optional[int] = ..., hydra_high: _Optional[int] = ..., cloud_low: _Optional[int] = ..., cloud_medium: _Optional[int] = ..., cloud_high: _Optional[int] = ..., cloud_critical: _Optional[int] = ...) -> None: ...
    class InitialQoSPrincipalNames(_message.Message):
        __slots__ = ("backup_high", "backup_low", "test_dev_high", "test_dev_low", "yoda_high", "yoda_low", "magneto_high", "magneto_low", "magneto_ssd", "system_critical", "system_high", "system_low", "user_low", "madrox_low", "madrox_high", "filer_low", "filer_high", "hydra_low", "hydra_high", "backup_ssd", "backup_commvault", "hydra_sequential_dump", "restore_high", "restore_low", "backup_all", "cloud_low", "cloud_medium", "cloud_high", "cloud_critical")
        BACKUP_HIGH_FIELD_NUMBER: _ClassVar[int]
        BACKUP_LOW_FIELD_NUMBER: _ClassVar[int]
        TEST_DEV_HIGH_FIELD_NUMBER: _ClassVar[int]
        TEST_DEV_LOW_FIELD_NUMBER: _ClassVar[int]
        YODA_HIGH_FIELD_NUMBER: _ClassVar[int]
        YODA_LOW_FIELD_NUMBER: _ClassVar[int]
        MAGNETO_HIGH_FIELD_NUMBER: _ClassVar[int]
        MAGNETO_LOW_FIELD_NUMBER: _ClassVar[int]
        MAGNETO_SSD_FIELD_NUMBER: _ClassVar[int]
        SYSTEM_CRITICAL_FIELD_NUMBER: _ClassVar[int]
        SYSTEM_HIGH_FIELD_NUMBER: _ClassVar[int]
        SYSTEM_LOW_FIELD_NUMBER: _ClassVar[int]
        USER_LOW_FIELD_NUMBER: _ClassVar[int]
        MADROX_LOW_FIELD_NUMBER: _ClassVar[int]
        MADROX_HIGH_FIELD_NUMBER: _ClassVar[int]
        FILER_LOW_FIELD_NUMBER: _ClassVar[int]
        FILER_HIGH_FIELD_NUMBER: _ClassVar[int]
        HYDRA_LOW_FIELD_NUMBER: _ClassVar[int]
        HYDRA_HIGH_FIELD_NUMBER: _ClassVar[int]
        BACKUP_SSD_FIELD_NUMBER: _ClassVar[int]
        BACKUP_COMMVAULT_FIELD_NUMBER: _ClassVar[int]
        HYDRA_SEQUENTIAL_DUMP_FIELD_NUMBER: _ClassVar[int]
        RESTORE_HIGH_FIELD_NUMBER: _ClassVar[int]
        RESTORE_LOW_FIELD_NUMBER: _ClassVar[int]
        BACKUP_ALL_FIELD_NUMBER: _ClassVar[int]
        CLOUD_LOW_FIELD_NUMBER: _ClassVar[int]
        CLOUD_MEDIUM_FIELD_NUMBER: _ClassVar[int]
        CLOUD_HIGH_FIELD_NUMBER: _ClassVar[int]
        CLOUD_CRITICAL_FIELD_NUMBER: _ClassVar[int]
        backup_high: str
        backup_low: str
        test_dev_high: str
        test_dev_low: str
        yoda_high: str
        yoda_low: str
        magneto_high: str
        magneto_low: str
        magneto_ssd: str
        system_critical: str
        system_high: str
        system_low: str
        user_low: str
        madrox_low: str
        madrox_high: str
        filer_low: str
        filer_high: str
        hydra_low: str
        hydra_high: str
        backup_ssd: str
        backup_commvault: str
        hydra_sequential_dump: str
        restore_high: str
        restore_low: str
        backup_all: str
        cloud_low: str
        cloud_medium: str
        cloud_high: str
        cloud_critical: str
        def __init__(self, backup_high: _Optional[str] = ..., backup_low: _Optional[str] = ..., test_dev_high: _Optional[str] = ..., test_dev_low: _Optional[str] = ..., yoda_high: _Optional[str] = ..., yoda_low: _Optional[str] = ..., magneto_high: _Optional[str] = ..., magneto_low: _Optional[str] = ..., magneto_ssd: _Optional[str] = ..., system_critical: _Optional[str] = ..., system_high: _Optional[str] = ..., system_low: _Optional[str] = ..., user_low: _Optional[str] = ..., madrox_low: _Optional[str] = ..., madrox_high: _Optional[str] = ..., filer_low: _Optional[str] = ..., filer_high: _Optional[str] = ..., hydra_low: _Optional[str] = ..., hydra_high: _Optional[str] = ..., backup_ssd: _Optional[str] = ..., backup_commvault: _Optional[str] = ..., hydra_sequential_dump: _Optional[str] = ..., restore_high: _Optional[str] = ..., restore_low: _Optional[str] = ..., backup_all: _Optional[str] = ..., cloud_low: _Optional[str] = ..., cloud_medium: _Optional[str] = ..., cloud_high: _Optional[str] = ..., cloud_critical: _Optional[str] = ...) -> None: ...
    class InitialQoSPrincipalWorkloadNames(_message.Message):
        __slots__ = ("backup", "test_dev", "yoda", "madrox", "filer")
        BACKUP_FIELD_NUMBER: _ClassVar[int]
        TEST_DEV_FIELD_NUMBER: _ClassVar[int]
        YODA_FIELD_NUMBER: _ClassVar[int]
        MADROX_FIELD_NUMBER: _ClassVar[int]
        FILER_FIELD_NUMBER: _ClassVar[int]
        backup: str
        test_dev: str
        yoda: str
        madrox: str
        filer: str
        def __init__(self, backup: _Optional[str] = ..., test_dev: _Optional[str] = ..., yoda: _Optional[str] = ..., madrox: _Optional[str] = ..., filer: _Optional[str] = ...) -> None: ...
    class SmbGUID(_message.Message):
        __slots__ = ("data1", "data2", "data3", "data4")
        DATA1_FIELD_NUMBER: _ClassVar[int]
        DATA2_FIELD_NUMBER: _ClassVar[int]
        DATA3_FIELD_NUMBER: _ClassVar[int]
        DATA4_FIELD_NUMBER: _ClassVar[int]
        data1: int
        data2: int
        data3: int
        data4: int
        def __init__(self, data1: _Optional[int] = ..., data2: _Optional[int] = ..., data3: _Optional[int] = ..., data4: _Optional[int] = ...) -> None: ...
    class SID(_message.Message):
        __slots__ = ("revision_level", "identifier_authority", "sub_authority")
        REVISION_LEVEL_FIELD_NUMBER: _ClassVar[int]
        IDENTIFIER_AUTHORITY_FIELD_NUMBER: _ClassVar[int]
        SUB_AUTHORITY_FIELD_NUMBER: _ClassVar[int]
        revision_level: int
        identifier_authority: bytes
        sub_authority: _containers.RepeatedScalarFieldContainer[int]
        def __init__(self, revision_level: _Optional[int] = ..., identifier_authority: _Optional[bytes] = ..., sub_authority: _Optional[_Iterable[int]] = ...) -> None: ...
    class ActiveDirectoryConfig(_message.Message):
        __slots__ = ("enabled", "provider_vec", "disable_smb_auth", "cross_realm_path_map")
        class IdMappingInfo(_message.Message):
            __slots__ = ("type", "centrify_zone_path", "centrify_zone_description", "centrify_schema", "fixed_uid", "fixed_gid", "custom_uid_attr_name", "custom_gid_attr_name")
            class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                kRid: _ClassVar[ClusterConfigProto.ActiveDirectoryConfig.IdMappingInfo.Type]
                kRfc2307: _ClassVar[ClusterConfigProto.ActiveDirectoryConfig.IdMappingInfo.Type]
                kSfu30: _ClassVar[ClusterConfigProto.ActiveDirectoryConfig.IdMappingInfo.Type]
                kCentrify: _ClassVar[ClusterConfigProto.ActiveDirectoryConfig.IdMappingInfo.Type]
                kFixed: _ClassVar[ClusterConfigProto.ActiveDirectoryConfig.IdMappingInfo.Type]
                kCustomAttributes: _ClassVar[ClusterConfigProto.ActiveDirectoryConfig.IdMappingInfo.Type]
                kLdapProvider: _ClassVar[ClusterConfigProto.ActiveDirectoryConfig.IdMappingInfo.Type]
                kNisProvider: _ClassVar[ClusterConfigProto.ActiveDirectoryConfig.IdMappingInfo.Type]
            kRid: ClusterConfigProto.ActiveDirectoryConfig.IdMappingInfo.Type
            kRfc2307: ClusterConfigProto.ActiveDirectoryConfig.IdMappingInfo.Type
            kSfu30: ClusterConfigProto.ActiveDirectoryConfig.IdMappingInfo.Type
            kCentrify: ClusterConfigProto.ActiveDirectoryConfig.IdMappingInfo.Type
            kFixed: ClusterConfigProto.ActiveDirectoryConfig.IdMappingInfo.Type
            kCustomAttributes: ClusterConfigProto.ActiveDirectoryConfig.IdMappingInfo.Type
            kLdapProvider: ClusterConfigProto.ActiveDirectoryConfig.IdMappingInfo.Type
            kNisProvider: ClusterConfigProto.ActiveDirectoryConfig.IdMappingInfo.Type
            class CentrifySchema(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                kCentrifyDynamicSchema_1_0: _ClassVar[ClusterConfigProto.ActiveDirectoryConfig.IdMappingInfo.CentrifySchema]
                kCentrifyDynamicSchema_2_0: _ClassVar[ClusterConfigProto.ActiveDirectoryConfig.IdMappingInfo.CentrifySchema]
                kCentrifySfu_3_0: _ClassVar[ClusterConfigProto.ActiveDirectoryConfig.IdMappingInfo.CentrifySchema]
                kCentrifySfu_4_0: _ClassVar[ClusterConfigProto.ActiveDirectoryConfig.IdMappingInfo.CentrifySchema]
                kCentrifyCdcRfc2307: _ClassVar[ClusterConfigProto.ActiveDirectoryConfig.IdMappingInfo.CentrifySchema]
                kCentrifyDynamicSchema_3_0: _ClassVar[ClusterConfigProto.ActiveDirectoryConfig.IdMappingInfo.CentrifySchema]
                kCentrifyCdcRfc2307_2: _ClassVar[ClusterConfigProto.ActiveDirectoryConfig.IdMappingInfo.CentrifySchema]
                kCentrifyDynamicSchema_5_0: _ClassVar[ClusterConfigProto.ActiveDirectoryConfig.IdMappingInfo.CentrifySchema]
                kCentrifyCdcRfc2307_3: _ClassVar[ClusterConfigProto.ActiveDirectoryConfig.IdMappingInfo.CentrifySchema]
                kCentrifySfu_3_0_V5: _ClassVar[ClusterConfigProto.ActiveDirectoryConfig.IdMappingInfo.CentrifySchema]
            kCentrifyDynamicSchema_1_0: ClusterConfigProto.ActiveDirectoryConfig.IdMappingInfo.CentrifySchema
            kCentrifyDynamicSchema_2_0: ClusterConfigProto.ActiveDirectoryConfig.IdMappingInfo.CentrifySchema
            kCentrifySfu_3_0: ClusterConfigProto.ActiveDirectoryConfig.IdMappingInfo.CentrifySchema
            kCentrifySfu_4_0: ClusterConfigProto.ActiveDirectoryConfig.IdMappingInfo.CentrifySchema
            kCentrifyCdcRfc2307: ClusterConfigProto.ActiveDirectoryConfig.IdMappingInfo.CentrifySchema
            kCentrifyDynamicSchema_3_0: ClusterConfigProto.ActiveDirectoryConfig.IdMappingInfo.CentrifySchema
            kCentrifyCdcRfc2307_2: ClusterConfigProto.ActiveDirectoryConfig.IdMappingInfo.CentrifySchema
            kCentrifyDynamicSchema_5_0: ClusterConfigProto.ActiveDirectoryConfig.IdMappingInfo.CentrifySchema
            kCentrifyCdcRfc2307_3: ClusterConfigProto.ActiveDirectoryConfig.IdMappingInfo.CentrifySchema
            kCentrifySfu_3_0_V5: ClusterConfigProto.ActiveDirectoryConfig.IdMappingInfo.CentrifySchema
            TYPE_FIELD_NUMBER: _ClassVar[int]
            CENTRIFY_ZONE_PATH_FIELD_NUMBER: _ClassVar[int]
            CENTRIFY_ZONE_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
            CENTRIFY_SCHEMA_FIELD_NUMBER: _ClassVar[int]
            FIXED_UID_FIELD_NUMBER: _ClassVar[int]
            FIXED_GID_FIELD_NUMBER: _ClassVar[int]
            CUSTOM_UID_ATTR_NAME_FIELD_NUMBER: _ClassVar[int]
            CUSTOM_GID_ATTR_NAME_FIELD_NUMBER: _ClassVar[int]
            type: ClusterConfigProto.ActiveDirectoryConfig.IdMappingInfo.Type
            centrify_zone_path: str
            centrify_zone_description: str
            centrify_schema: ClusterConfigProto.ActiveDirectoryConfig.IdMappingInfo.CentrifySchema
            fixed_uid: int
            fixed_gid: int
            custom_uid_attr_name: str
            custom_gid_attr_name: str
            def __init__(self, type: _Optional[_Union[ClusterConfigProto.ActiveDirectoryConfig.IdMappingInfo.Type, str]] = ..., centrify_zone_path: _Optional[str] = ..., centrify_zone_description: _Optional[str] = ..., centrify_schema: _Optional[_Union[ClusterConfigProto.ActiveDirectoryConfig.IdMappingInfo.CentrifySchema, str]] = ..., fixed_uid: _Optional[int] = ..., fixed_gid: _Optional[int] = ..., custom_uid_attr_name: _Optional[str] = ..., custom_gid_attr_name: _Optional[str] = ...) -> None: ...
        class PreferredDomainControllers(_message.Message):
            __slots__ = ("server_vec", "ldap_port")
            SERVER_VEC_FIELD_NUMBER: _ClassVar[int]
            LDAP_PORT_FIELD_NUMBER: _ClassVar[int]
            server_vec: _containers.RepeatedScalarFieldContainer[str]
            ldap_port: int
            def __init__(self, server_vec: _Optional[_Iterable[str]] = ..., ldap_port: _Optional[int] = ...) -> None: ...
        class BlacklistedDomainControllers(_message.Message):
            __slots__ = ("server_vec",)
            SERVER_VEC_FIELD_NUMBER: _ClassVar[int]
            server_vec: _containers.RepeatedScalarFieldContainer[str]
            def __init__(self, server_vec: _Optional[_Iterable[str]] = ...) -> None: ...
        class ActiveDirectoryProvider(_message.Message):
            __slots__ = ("id", "domain_name", "ad_server_vec", "kerberos_server_name", "dns_domain_name", "guid", "root_sid", "ldap_root_dn", "machine_account_names", "ldap_urls", "ou_name", "id_mapping_info", "fallback_id_mapping_info", "unix_root_sid", "disabled_trusted_domain_vec", "tenant_id_vec", "preferred_dc_map", "ldap_provider_id", "trusted_domain_discovery_disabled", "deprecated_account_to_dnshostname_map", "deprecated_account_to_encryptiontype_map", "nis_provider_domain_name", "network_realm_id", "transitive_ad_trust_level_limit", "ldap_bind_user_name", "encrypted_ldap_bind_password", "only_use_user_enabled_domains", "enabled_trusted_domain_vec", "machine_accounts_map", "blacklisted_dc_map")
            class PreferredDcMapEntry(_message.Message):
                __slots__ = ("key", "value")
                KEY_FIELD_NUMBER: _ClassVar[int]
                VALUE_FIELD_NUMBER: _ClassVar[int]
                key: str
                value: ClusterConfigProto.ActiveDirectoryConfig.PreferredDomainControllers
                def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[ClusterConfigProto.ActiveDirectoryConfig.PreferredDomainControllers, _Mapping]] = ...) -> None: ...
            class DeprecatedAccountToDnshostnameMapEntry(_message.Message):
                __slots__ = ("key", "value")
                KEY_FIELD_NUMBER: _ClassVar[int]
                VALUE_FIELD_NUMBER: _ClassVar[int]
                key: str
                value: str
                def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
            class DeprecatedAccountToEncryptiontypeMapEntry(_message.Message):
                __slots__ = ("key", "value")
                KEY_FIELD_NUMBER: _ClassVar[int]
                VALUE_FIELD_NUMBER: _ClassVar[int]
                key: str
                value: int
                def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
            class MachineAccountProto(_message.Message):
                __slots__ = ("name", "enctype", "dns_hostname", "spn_vec")
                NAME_FIELD_NUMBER: _ClassVar[int]
                ENCTYPE_FIELD_NUMBER: _ClassVar[int]
                DNS_HOSTNAME_FIELD_NUMBER: _ClassVar[int]
                SPN_VEC_FIELD_NUMBER: _ClassVar[int]
                name: str
                enctype: int
                dns_hostname: str
                spn_vec: _containers.RepeatedScalarFieldContainer[str]
                def __init__(self, name: _Optional[str] = ..., enctype: _Optional[int] = ..., dns_hostname: _Optional[str] = ..., spn_vec: _Optional[_Iterable[str]] = ...) -> None: ...
            class MachineAccountsMapEntry(_message.Message):
                __slots__ = ("key", "value")
                KEY_FIELD_NUMBER: _ClassVar[int]
                VALUE_FIELD_NUMBER: _ClassVar[int]
                key: str
                value: ClusterConfigProto.ActiveDirectoryConfig.ActiveDirectoryProvider.MachineAccountProto
                def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[ClusterConfigProto.ActiveDirectoryConfig.ActiveDirectoryProvider.MachineAccountProto, _Mapping]] = ...) -> None: ...
            class BlacklistedDcMapEntry(_message.Message):
                __slots__ = ("key", "value")
                KEY_FIELD_NUMBER: _ClassVar[int]
                VALUE_FIELD_NUMBER: _ClassVar[int]
                key: str
                value: ClusterConfigProto.ActiveDirectoryConfig.BlacklistedDomainControllers
                def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[ClusterConfigProto.ActiveDirectoryConfig.BlacklistedDomainControllers, _Mapping]] = ...) -> None: ...
            ID_FIELD_NUMBER: _ClassVar[int]
            DOMAIN_NAME_FIELD_NUMBER: _ClassVar[int]
            AD_SERVER_VEC_FIELD_NUMBER: _ClassVar[int]
            KERBEROS_SERVER_NAME_FIELD_NUMBER: _ClassVar[int]
            DNS_DOMAIN_NAME_FIELD_NUMBER: _ClassVar[int]
            GUID_FIELD_NUMBER: _ClassVar[int]
            ROOT_SID_FIELD_NUMBER: _ClassVar[int]
            LDAP_ROOT_DN_FIELD_NUMBER: _ClassVar[int]
            MACHINE_ACCOUNT_NAMES_FIELD_NUMBER: _ClassVar[int]
            LDAP_URLS_FIELD_NUMBER: _ClassVar[int]
            OU_NAME_FIELD_NUMBER: _ClassVar[int]
            ID_MAPPING_INFO_FIELD_NUMBER: _ClassVar[int]
            FALLBACK_ID_MAPPING_INFO_FIELD_NUMBER: _ClassVar[int]
            UNIX_ROOT_SID_FIELD_NUMBER: _ClassVar[int]
            DISABLED_TRUSTED_DOMAIN_VEC_FIELD_NUMBER: _ClassVar[int]
            TENANT_ID_VEC_FIELD_NUMBER: _ClassVar[int]
            PREFERRED_DC_MAP_FIELD_NUMBER: _ClassVar[int]
            LDAP_PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
            TRUSTED_DOMAIN_DISCOVERY_DISABLED_FIELD_NUMBER: _ClassVar[int]
            DEPRECATED_ACCOUNT_TO_DNSHOSTNAME_MAP_FIELD_NUMBER: _ClassVar[int]
            DEPRECATED_ACCOUNT_TO_ENCRYPTIONTYPE_MAP_FIELD_NUMBER: _ClassVar[int]
            NIS_PROVIDER_DOMAIN_NAME_FIELD_NUMBER: _ClassVar[int]
            NETWORK_REALM_ID_FIELD_NUMBER: _ClassVar[int]
            TRANSITIVE_AD_TRUST_LEVEL_LIMIT_FIELD_NUMBER: _ClassVar[int]
            LDAP_BIND_USER_NAME_FIELD_NUMBER: _ClassVar[int]
            ENCRYPTED_LDAP_BIND_PASSWORD_FIELD_NUMBER: _ClassVar[int]
            ONLY_USE_USER_ENABLED_DOMAINS_FIELD_NUMBER: _ClassVar[int]
            ENABLED_TRUSTED_DOMAIN_VEC_FIELD_NUMBER: _ClassVar[int]
            MACHINE_ACCOUNTS_MAP_FIELD_NUMBER: _ClassVar[int]
            BLACKLISTED_DC_MAP_FIELD_NUMBER: _ClassVar[int]
            id: int
            domain_name: str
            ad_server_vec: _containers.RepeatedScalarFieldContainer[str]
            kerberos_server_name: str
            dns_domain_name: str
            guid: ClusterConfigProto.SmbGUID
            root_sid: ClusterConfigProto.SID
            ldap_root_dn: str
            machine_account_names: _containers.RepeatedScalarFieldContainer[str]
            ldap_urls: _containers.RepeatedScalarFieldContainer[str]
            ou_name: str
            id_mapping_info: ClusterConfigProto.ActiveDirectoryConfig.IdMappingInfo
            fallback_id_mapping_info: ClusterConfigProto.ActiveDirectoryConfig.IdMappingInfo
            unix_root_sid: ClusterConfigProto.SID
            disabled_trusted_domain_vec: _containers.RepeatedScalarFieldContainer[str]
            tenant_id_vec: _containers.RepeatedScalarFieldContainer[str]
            preferred_dc_map: _containers.MessageMap[str, ClusterConfigProto.ActiveDirectoryConfig.PreferredDomainControllers]
            ldap_provider_id: int
            trusted_domain_discovery_disabled: bool
            deprecated_account_to_dnshostname_map: _containers.ScalarMap[str, str]
            deprecated_account_to_encryptiontype_map: _containers.ScalarMap[str, int]
            nis_provider_domain_name: str
            network_realm_id: int
            transitive_ad_trust_level_limit: int
            ldap_bind_user_name: str
            encrypted_ldap_bind_password: bytes
            only_use_user_enabled_domains: bool
            enabled_trusted_domain_vec: _containers.RepeatedScalarFieldContainer[str]
            machine_accounts_map: _containers.MessageMap[str, ClusterConfigProto.ActiveDirectoryConfig.ActiveDirectoryProvider.MachineAccountProto]
            blacklisted_dc_map: _containers.MessageMap[str, ClusterConfigProto.ActiveDirectoryConfig.BlacklistedDomainControllers]
            def __init__(self, id: _Optional[int] = ..., domain_name: _Optional[str] = ..., ad_server_vec: _Optional[_Iterable[str]] = ..., kerberos_server_name: _Optional[str] = ..., dns_domain_name: _Optional[str] = ..., guid: _Optional[_Union[ClusterConfigProto.SmbGUID, _Mapping]] = ..., root_sid: _Optional[_Union[ClusterConfigProto.SID, _Mapping]] = ..., ldap_root_dn: _Optional[str] = ..., machine_account_names: _Optional[_Iterable[str]] = ..., ldap_urls: _Optional[_Iterable[str]] = ..., ou_name: _Optional[str] = ..., id_mapping_info: _Optional[_Union[ClusterConfigProto.ActiveDirectoryConfig.IdMappingInfo, _Mapping]] = ..., fallback_id_mapping_info: _Optional[_Union[ClusterConfigProto.ActiveDirectoryConfig.IdMappingInfo, _Mapping]] = ..., unix_root_sid: _Optional[_Union[ClusterConfigProto.SID, _Mapping]] = ..., disabled_trusted_domain_vec: _Optional[_Iterable[str]] = ..., tenant_id_vec: _Optional[_Iterable[str]] = ..., preferred_dc_map: _Optional[_Mapping[str, ClusterConfigProto.ActiveDirectoryConfig.PreferredDomainControllers]] = ..., ldap_provider_id: _Optional[int] = ..., trusted_domain_discovery_disabled: bool = ..., deprecated_account_to_dnshostname_map: _Optional[_Mapping[str, str]] = ..., deprecated_account_to_encryptiontype_map: _Optional[_Mapping[str, int]] = ..., nis_provider_domain_name: _Optional[str] = ..., network_realm_id: _Optional[int] = ..., transitive_ad_trust_level_limit: _Optional[int] = ..., ldap_bind_user_name: _Optional[str] = ..., encrypted_ldap_bind_password: _Optional[bytes] = ..., only_use_user_enabled_domains: bool = ..., enabled_trusted_domain_vec: _Optional[_Iterable[str]] = ..., machine_accounts_map: _Optional[_Mapping[str, ClusterConfigProto.ActiveDirectoryConfig.ActiveDirectoryProvider.MachineAccountProto]] = ..., blacklisted_dc_map: _Optional[_Mapping[str, ClusterConfigProto.ActiveDirectoryConfig.BlacklistedDomainControllers]] = ...) -> None: ...
        class CrossRealmPath(_message.Message):
            __slots__ = ("cluster_domain", "inter_domain")
            CLUSTER_DOMAIN_FIELD_NUMBER: _ClassVar[int]
            INTER_DOMAIN_FIELD_NUMBER: _ClassVar[int]
            cluster_domain: str
            inter_domain: str
            def __init__(self, cluster_domain: _Optional[str] = ..., inter_domain: _Optional[str] = ...) -> None: ...
        class CrossRealmPathVec(_message.Message):
            __slots__ = ("path_vec",)
            PATH_VEC_FIELD_NUMBER: _ClassVar[int]
            path_vec: _containers.RepeatedCompositeFieldContainer[ClusterConfigProto.ActiveDirectoryConfig.CrossRealmPath]
            def __init__(self, path_vec: _Optional[_Iterable[_Union[ClusterConfigProto.ActiveDirectoryConfig.CrossRealmPath, _Mapping]]] = ...) -> None: ...
        class CrossRealmPathMapEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: ClusterConfigProto.ActiveDirectoryConfig.CrossRealmPathVec
            def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[ClusterConfigProto.ActiveDirectoryConfig.CrossRealmPathVec, _Mapping]] = ...) -> None: ...
        ENABLED_FIELD_NUMBER: _ClassVar[int]
        PROVIDER_VEC_FIELD_NUMBER: _ClassVar[int]
        DISABLE_SMB_AUTH_FIELD_NUMBER: _ClassVar[int]
        CROSS_REALM_PATH_MAP_FIELD_NUMBER: _ClassVar[int]
        enabled: bool
        provider_vec: _containers.RepeatedCompositeFieldContainer[ClusterConfigProto.ActiveDirectoryConfig.ActiveDirectoryProvider]
        disable_smb_auth: bool
        cross_realm_path_map: _containers.MessageMap[str, ClusterConfigProto.ActiveDirectoryConfig.CrossRealmPathVec]
        def __init__(self, enabled: bool = ..., provider_vec: _Optional[_Iterable[_Union[ClusterConfigProto.ActiveDirectoryConfig.ActiveDirectoryProvider, _Mapping]]] = ..., disable_smb_auth: bool = ..., cross_realm_path_map: _Optional[_Mapping[str, ClusterConfigProto.ActiveDirectoryConfig.CrossRealmPathVec]] = ...) -> None: ...
    class LdapConfig(_message.Message):
        __slots__ = ("enabled", "provider_vec")
        class LdapProvider(_message.Message):
            __slots__ = ("id", "name", "preferred_ldap_server_vec", "ldap_domain_name", "ldap_port", "auth_level", "bind_user_dn", "encrypted_bind_user_password", "bind_user_password", "base_dn", "use_ssl", "tenant_id_vec", "network_realm_id", "common_name_attribute_name", "gid_attr_name", "uid_attr_name", "member_of_attribute_name", "user_name_attribute_name", "group_object_class_name", "user_object_class_name")
            class AuthLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                kAnonymous: _ClassVar[ClusterConfigProto.LdapConfig.LdapProvider.AuthLevel]
                kSimple: _ClassVar[ClusterConfigProto.LdapConfig.LdapProvider.AuthLevel]
                kSasl: _ClassVar[ClusterConfigProto.LdapConfig.LdapProvider.AuthLevel]
            kAnonymous: ClusterConfigProto.LdapConfig.LdapProvider.AuthLevel
            kSimple: ClusterConfigProto.LdapConfig.LdapProvider.AuthLevel
            kSasl: ClusterConfigProto.LdapConfig.LdapProvider.AuthLevel
            ID_FIELD_NUMBER: _ClassVar[int]
            NAME_FIELD_NUMBER: _ClassVar[int]
            PREFERRED_LDAP_SERVER_VEC_FIELD_NUMBER: _ClassVar[int]
            LDAP_DOMAIN_NAME_FIELD_NUMBER: _ClassVar[int]
            LDAP_PORT_FIELD_NUMBER: _ClassVar[int]
            AUTH_LEVEL_FIELD_NUMBER: _ClassVar[int]
            BIND_USER_DN_FIELD_NUMBER: _ClassVar[int]
            ENCRYPTED_BIND_USER_PASSWORD_FIELD_NUMBER: _ClassVar[int]
            BIND_USER_PASSWORD_FIELD_NUMBER: _ClassVar[int]
            BASE_DN_FIELD_NUMBER: _ClassVar[int]
            USE_SSL_FIELD_NUMBER: _ClassVar[int]
            TENANT_ID_VEC_FIELD_NUMBER: _ClassVar[int]
            NETWORK_REALM_ID_FIELD_NUMBER: _ClassVar[int]
            COMMON_NAME_ATTRIBUTE_NAME_FIELD_NUMBER: _ClassVar[int]
            GID_ATTR_NAME_FIELD_NUMBER: _ClassVar[int]
            UID_ATTR_NAME_FIELD_NUMBER: _ClassVar[int]
            MEMBER_OF_ATTRIBUTE_NAME_FIELD_NUMBER: _ClassVar[int]
            USER_NAME_ATTRIBUTE_NAME_FIELD_NUMBER: _ClassVar[int]
            GROUP_OBJECT_CLASS_NAME_FIELD_NUMBER: _ClassVar[int]
            USER_OBJECT_CLASS_NAME_FIELD_NUMBER: _ClassVar[int]
            id: int
            name: str
            preferred_ldap_server_vec: _containers.RepeatedScalarFieldContainer[str]
            ldap_domain_name: str
            ldap_port: int
            auth_level: ClusterConfigProto.LdapConfig.LdapProvider.AuthLevel
            bind_user_dn: str
            encrypted_bind_user_password: bytes
            bind_user_password: bytes
            base_dn: str
            use_ssl: bool
            tenant_id_vec: _containers.RepeatedScalarFieldContainer[str]
            network_realm_id: int
            common_name_attribute_name: str
            gid_attr_name: str
            uid_attr_name: str
            member_of_attribute_name: str
            user_name_attribute_name: str
            group_object_class_name: str
            user_object_class_name: str
            def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., preferred_ldap_server_vec: _Optional[_Iterable[str]] = ..., ldap_domain_name: _Optional[str] = ..., ldap_port: _Optional[int] = ..., auth_level: _Optional[_Union[ClusterConfigProto.LdapConfig.LdapProvider.AuthLevel, str]] = ..., bind_user_dn: _Optional[str] = ..., encrypted_bind_user_password: _Optional[bytes] = ..., bind_user_password: _Optional[bytes] = ..., base_dn: _Optional[str] = ..., use_ssl: bool = ..., tenant_id_vec: _Optional[_Iterable[str]] = ..., network_realm_id: _Optional[int] = ..., common_name_attribute_name: _Optional[str] = ..., gid_attr_name: _Optional[str] = ..., uid_attr_name: _Optional[str] = ..., member_of_attribute_name: _Optional[str] = ..., user_name_attribute_name: _Optional[str] = ..., group_object_class_name: _Optional[str] = ..., user_object_class_name: _Optional[str] = ...) -> None: ...
        ENABLED_FIELD_NUMBER: _ClassVar[int]
        PROVIDER_VEC_FIELD_NUMBER: _ClassVar[int]
        enabled: bool
        provider_vec: _containers.RepeatedCompositeFieldContainer[ClusterConfigProto.LdapConfig.LdapProvider]
        def __init__(self, enabled: bool = ..., provider_vec: _Optional[_Iterable[_Union[ClusterConfigProto.LdapConfig.LdapProvider, _Mapping]]] = ...) -> None: ...
    class SnmpConfig(_message.Message):
        __slots__ = ("version", "server", "agent_port", "trap_port", "read_user", "write_user", "trap_user", "operation", "vip", "sys_info")
        class SnmpV3AuthProtocol(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kAuthMD5: _ClassVar[ClusterConfigProto.SnmpConfig.SnmpV3AuthProtocol]
            kAuthSHA: _ClassVar[ClusterConfigProto.SnmpConfig.SnmpV3AuthProtocol]
        kAuthMD5: ClusterConfigProto.SnmpConfig.SnmpV3AuthProtocol
        kAuthSHA: ClusterConfigProto.SnmpConfig.SnmpV3AuthProtocol
        class SnmpV3PrivProtocol(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kPrivDES: _ClassVar[ClusterConfigProto.SnmpConfig.SnmpV3PrivProtocol]
            kPrivAES: _ClassVar[ClusterConfigProto.SnmpConfig.SnmpV3PrivProtocol]
        kPrivDES: ClusterConfigProto.SnmpConfig.SnmpV3PrivProtocol
        kPrivAES: ClusterConfigProto.SnmpConfig.SnmpV3PrivProtocol
        class SnmpV3SecurityLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kNoAuthNoPriv: _ClassVar[ClusterConfigProto.SnmpConfig.SnmpV3SecurityLevel]
            kAuthNoPriv: _ClassVar[ClusterConfigProto.SnmpConfig.SnmpV3SecurityLevel]
            kAuthPriv: _ClassVar[ClusterConfigProto.SnmpConfig.SnmpV3SecurityLevel]
        kNoAuthNoPriv: ClusterConfigProto.SnmpConfig.SnmpV3SecurityLevel
        kAuthNoPriv: ClusterConfigProto.SnmpConfig.SnmpV3SecurityLevel
        kAuthPriv: ClusterConfigProto.SnmpConfig.SnmpV3SecurityLevel
        class SnmpUserType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kReadUser: _ClassVar[ClusterConfigProto.SnmpConfig.SnmpUserType]
            kReadWriteUser: _ClassVar[ClusterConfigProto.SnmpConfig.SnmpUserType]
            kTrapUser: _ClassVar[ClusterConfigProto.SnmpConfig.SnmpUserType]
        kReadUser: ClusterConfigProto.SnmpConfig.SnmpUserType
        kReadWriteUser: ClusterConfigProto.SnmpConfig.SnmpUserType
        kTrapUser: ClusterConfigProto.SnmpConfig.SnmpUserType
        class SnmpOperationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kOperationEnable: _ClassVar[ClusterConfigProto.SnmpConfig.SnmpOperationType]
            kOperationDisable: _ClassVar[ClusterConfigProto.SnmpConfig.SnmpOperationType]
        kOperationEnable: ClusterConfigProto.SnmpConfig.SnmpOperationType
        kOperationDisable: ClusterConfigProto.SnmpConfig.SnmpOperationType
        class SnmpUser(_message.Message):
            __slots__ = ("username", "auth_protocol", "deprecated_auth_password", "priv_protocol", "deprecated_priv_password", "engine_id", "security_level", "context_name", "encrypted_auth_password", "encrypted_priv_password")
            USERNAME_FIELD_NUMBER: _ClassVar[int]
            AUTH_PROTOCOL_FIELD_NUMBER: _ClassVar[int]
            DEPRECATED_AUTH_PASSWORD_FIELD_NUMBER: _ClassVar[int]
            PRIV_PROTOCOL_FIELD_NUMBER: _ClassVar[int]
            DEPRECATED_PRIV_PASSWORD_FIELD_NUMBER: _ClassVar[int]
            ENGINE_ID_FIELD_NUMBER: _ClassVar[int]
            SECURITY_LEVEL_FIELD_NUMBER: _ClassVar[int]
            CONTEXT_NAME_FIELD_NUMBER: _ClassVar[int]
            ENCRYPTED_AUTH_PASSWORD_FIELD_NUMBER: _ClassVar[int]
            ENCRYPTED_PRIV_PASSWORD_FIELD_NUMBER: _ClassVar[int]
            username: str
            auth_protocol: ClusterConfigProto.SnmpConfig.SnmpV3AuthProtocol
            deprecated_auth_password: str
            priv_protocol: ClusterConfigProto.SnmpConfig.SnmpV3PrivProtocol
            deprecated_priv_password: str
            engine_id: str
            security_level: ClusterConfigProto.SnmpConfig.SnmpV3SecurityLevel
            context_name: str
            encrypted_auth_password: bytes
            encrypted_priv_password: bytes
            def __init__(self, username: _Optional[str] = ..., auth_protocol: _Optional[_Union[ClusterConfigProto.SnmpConfig.SnmpV3AuthProtocol, str]] = ..., deprecated_auth_password: _Optional[str] = ..., priv_protocol: _Optional[_Union[ClusterConfigProto.SnmpConfig.SnmpV3PrivProtocol, str]] = ..., deprecated_priv_password: _Optional[str] = ..., engine_id: _Optional[str] = ..., security_level: _Optional[_Union[ClusterConfigProto.SnmpConfig.SnmpV3SecurityLevel, str]] = ..., context_name: _Optional[str] = ..., encrypted_auth_password: _Optional[bytes] = ..., encrypted_priv_password: _Optional[bytes] = ...) -> None: ...
        class SnmpSysInfo(_message.Message):
            __slots__ = ("sys_location", "sys_contact", "sys_name", "sys_descr", "sys_object_id", "engine_id_type")
            SYS_LOCATION_FIELD_NUMBER: _ClassVar[int]
            SYS_CONTACT_FIELD_NUMBER: _ClassVar[int]
            SYS_NAME_FIELD_NUMBER: _ClassVar[int]
            SYS_DESCR_FIELD_NUMBER: _ClassVar[int]
            SYS_OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
            ENGINE_ID_TYPE_FIELD_NUMBER: _ClassVar[int]
            sys_location: str
            sys_contact: str
            sys_name: str
            sys_descr: str
            sys_object_id: str
            engine_id_type: int
            def __init__(self, sys_location: _Optional[str] = ..., sys_contact: _Optional[str] = ..., sys_name: _Optional[str] = ..., sys_descr: _Optional[str] = ..., sys_object_id: _Optional[str] = ..., engine_id_type: _Optional[int] = ...) -> None: ...
        VERSION_FIELD_NUMBER: _ClassVar[int]
        SERVER_FIELD_NUMBER: _ClassVar[int]
        AGENT_PORT_FIELD_NUMBER: _ClassVar[int]
        TRAP_PORT_FIELD_NUMBER: _ClassVar[int]
        READ_USER_FIELD_NUMBER: _ClassVar[int]
        WRITE_USER_FIELD_NUMBER: _ClassVar[int]
        TRAP_USER_FIELD_NUMBER: _ClassVar[int]
        OPERATION_FIELD_NUMBER: _ClassVar[int]
        VIP_FIELD_NUMBER: _ClassVar[int]
        SYS_INFO_FIELD_NUMBER: _ClassVar[int]
        version: ClusterConfigProto.SnmpVersion
        server: str
        agent_port: int
        trap_port: int
        read_user: ClusterConfigProto.SnmpConfig.SnmpUser
        write_user: ClusterConfigProto.SnmpConfig.SnmpUser
        trap_user: ClusterConfigProto.SnmpConfig.SnmpUser
        operation: ClusterConfigProto.SnmpConfig.SnmpOperationType
        vip: str
        sys_info: ClusterConfigProto.SnmpConfig.SnmpSysInfo
        def __init__(self, version: _Optional[_Union[ClusterConfigProto.SnmpVersion, str]] = ..., server: _Optional[str] = ..., agent_port: _Optional[int] = ..., trap_port: _Optional[int] = ..., read_user: _Optional[_Union[ClusterConfigProto.SnmpConfig.SnmpUser, _Mapping]] = ..., write_user: _Optional[_Union[ClusterConfigProto.SnmpConfig.SnmpUser, _Mapping]] = ..., trap_user: _Optional[_Union[ClusterConfigProto.SnmpConfig.SnmpUser, _Mapping]] = ..., operation: _Optional[_Union[ClusterConfigProto.SnmpConfig.SnmpOperationType, str]] = ..., vip: _Optional[str] = ..., sys_info: _Optional[_Union[ClusterConfigProto.SnmpConfig.SnmpSysInfo, _Mapping]] = ...) -> None: ...
    class EulaConfig(_message.Message):
        __slots__ = ("signed_time", "signed_by_user", "signed_version", "license_key")
        SIGNED_TIME_FIELD_NUMBER: _ClassVar[int]
        SIGNED_BY_USER_FIELD_NUMBER: _ClassVar[int]
        SIGNED_VERSION_FIELD_NUMBER: _ClassVar[int]
        LICENSE_KEY_FIELD_NUMBER: _ClassVar[int]
        signed_time: int
        signed_by_user: str
        signed_version: int
        license_key: str
        def __init__(self, signed_time: _Optional[int] = ..., signed_by_user: _Optional[str] = ..., signed_version: _Optional[int] = ..., license_key: _Optional[str] = ...) -> None: ...
    class LicenseState(_message.Message):
        __slots__ = ("state", "failed_attempts")
        class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kInProgressNewCluster: _ClassVar[ClusterConfigProto.LicenseState.State]
            kInProgressOldCluster: _ClassVar[ClusterConfigProto.LicenseState.State]
            kClaimed: _ClassVar[ClusterConfigProto.LicenseState.State]
            kSkipped: _ClassVar[ClusterConfigProto.LicenseState.State]
            kStarted: _ClassVar[ClusterConfigProto.LicenseState.State]
        kInProgressNewCluster: ClusterConfigProto.LicenseState.State
        kInProgressOldCluster: ClusterConfigProto.LicenseState.State
        kClaimed: ClusterConfigProto.LicenseState.State
        kSkipped: ClusterConfigProto.LicenseState.State
        kStarted: ClusterConfigProto.LicenseState.State
        STATE_FIELD_NUMBER: _ClassVar[int]
        FAILED_ATTEMPTS_FIELD_NUMBER: _ClassVar[int]
        state: ClusterConfigProto.LicenseState.State
        failed_attempts: int
        def __init__(self, state: _Optional[_Union[ClusterConfigProto.LicenseState.State, str]] = ..., failed_attempts: _Optional[int] = ...) -> None: ...
    class ProxyServerConfig(_message.Message):
        __slots__ = ("name", "ip", "port", "username", "encrypted_password", "encryption_type", "type", "scheme_vec", "services_type_list", "is_disabled")
        class EncryptionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kDes: _ClassVar[ClusterConfigProto.ProxyServerConfig.EncryptionType]
            kAes: _ClassVar[ClusterConfigProto.ProxyServerConfig.EncryptionType]
        kDes: ClusterConfigProto.ProxyServerConfig.EncryptionType
        kAes: ClusterConfigProto.ProxyServerConfig.EncryptionType
        class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kAll: _ClassVar[ClusterConfigProto.ProxyServerConfig.Type]
            kManagement: _ClassVar[ClusterConfigProto.ProxyServerConfig.Type]
            kData: _ClassVar[ClusterConfigProto.ProxyServerConfig.Type]
            kHelios: _ClassVar[ClusterConfigProto.ProxyServerConfig.Type]
            kExternalTarget: _ClassVar[ClusterConfigProto.ProxyServerConfig.Type]
            kCloudTiering: _ClassVar[ClusterConfigProto.ProxyServerConfig.Type]
        kAll: ClusterConfigProto.ProxyServerConfig.Type
        kManagement: ClusterConfigProto.ProxyServerConfig.Type
        kData: ClusterConfigProto.ProxyServerConfig.Type
        kHelios: ClusterConfigProto.ProxyServerConfig.Type
        kExternalTarget: ClusterConfigProto.ProxyServerConfig.Type
        kCloudTiering: ClusterConfigProto.ProxyServerConfig.Type
        class Scheme(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kHttp: _ClassVar[ClusterConfigProto.ProxyServerConfig.Scheme]
            kHttps: _ClassVar[ClusterConfigProto.ProxyServerConfig.Scheme]
        kHttp: ClusterConfigProto.ProxyServerConfig.Scheme
        kHttps: ClusterConfigProto.ProxyServerConfig.Scheme
        NAME_FIELD_NUMBER: _ClassVar[int]
        IP_FIELD_NUMBER: _ClassVar[int]
        PORT_FIELD_NUMBER: _ClassVar[int]
        USERNAME_FIELD_NUMBER: _ClassVar[int]
        ENCRYPTED_PASSWORD_FIELD_NUMBER: _ClassVar[int]
        ENCRYPTION_TYPE_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        SCHEME_VEC_FIELD_NUMBER: _ClassVar[int]
        SERVICES_TYPE_LIST_FIELD_NUMBER: _ClassVar[int]
        IS_DISABLED_FIELD_NUMBER: _ClassVar[int]
        name: str
        ip: str
        port: int
        username: str
        encrypted_password: bytes
        encryption_type: ClusterConfigProto.ProxyServerConfig.EncryptionType
        type: ClusterConfigProto.ProxyServerConfig.Type
        scheme_vec: int
        services_type_list: _containers.RepeatedScalarFieldContainer[ClusterConfigProto.ProxyServerConfig.Type]
        is_disabled: bool
        def __init__(self, name: _Optional[str] = ..., ip: _Optional[str] = ..., port: _Optional[int] = ..., username: _Optional[str] = ..., encrypted_password: _Optional[bytes] = ..., encryption_type: _Optional[_Union[ClusterConfigProto.ProxyServerConfig.EncryptionType, str]] = ..., type: _Optional[_Union[ClusterConfigProto.ProxyServerConfig.Type, str]] = ..., scheme_vec: _Optional[int] = ..., services_type_list: _Optional[_Iterable[_Union[ClusterConfigProto.ProxyServerConfig.Type, str]]] = ..., is_disabled: bool = ...) -> None: ...
    class IceboxProperties(_message.Message):
        __slots__ = ("desired_chunk_utilization_percentage_for_reference", "chunk_utilization_examine_duration_hours", "ideal_segment_size_MB", "global_bw_limits", "non_reference_chunk_utilization_examine_duration_hours", "cloud_domain_version")
        DESIRED_CHUNK_UTILIZATION_PERCENTAGE_FOR_REFERENCE_FIELD_NUMBER: _ClassVar[int]
        CHUNK_UTILIZATION_EXAMINE_DURATION_HOURS_FIELD_NUMBER: _ClassVar[int]
        IDEAL_SEGMENT_SIZE_MB_FIELD_NUMBER: _ClassVar[int]
        GLOBAL_BW_LIMITS_FIELD_NUMBER: _ClassVar[int]
        NON_REFERENCE_CHUNK_UTILIZATION_EXAMINE_DURATION_HOURS_FIELD_NUMBER: _ClassVar[int]
        CLOUD_DOMAIN_VERSION_FIELD_NUMBER: _ClassVar[int]
        desired_chunk_utilization_percentage_for_reference: int
        chunk_utilization_examine_duration_hours: int
        ideal_segment_size_MB: int
        global_bw_limits: ClusterConfigProto.BandwidthLimits
        non_reference_chunk_utilization_examine_duration_hours: int
        cloud_domain_version: int
        def __init__(self, desired_chunk_utilization_percentage_for_reference: _Optional[int] = ..., chunk_utilization_examine_duration_hours: _Optional[int] = ..., ideal_segment_size_MB: _Optional[int] = ..., global_bw_limits: _Optional[_Union[ClusterConfigProto.BandwidthLimits, _Mapping]] = ..., non_reference_chunk_utilization_examine_duration_hours: _Optional[int] = ..., cloud_domain_version: _Optional[int] = ...) -> None: ...
    class FaultToleranceStrictness(_message.Message):
        __slots__ = ("level",)
        class Level(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kNode: _ClassVar[ClusterConfigProto.FaultToleranceStrictness.Level]
            kChassis: _ClassVar[ClusterConfigProto.FaultToleranceStrictness.Level]
            kRack: _ClassVar[ClusterConfigProto.FaultToleranceStrictness.Level]
            kDataCenter: _ClassVar[ClusterConfigProto.FaultToleranceStrictness.Level]
        kNode: ClusterConfigProto.FaultToleranceStrictness.Level
        kChassis: ClusterConfigProto.FaultToleranceStrictness.Level
        kRack: ClusterConfigProto.FaultToleranceStrictness.Level
        kDataCenter: ClusterConfigProto.FaultToleranceStrictness.Level
        LEVEL_FIELD_NUMBER: _ClassVar[int]
        level: ClusterConfigProto.FaultToleranceStrictness.Level
        def __init__(self, level: _Optional[_Union[ClusterConfigProto.FaultToleranceStrictness.Level, str]] = ...) -> None: ...
    class TopicMetadata(_message.Message):
        __slots__ = ("consumer_groups", "record_retention_period_usecs")
        class ConsumerGroups(_message.Message):
            __slots__ = ("id_vec",)
            ID_VEC_FIELD_NUMBER: _ClassVar[int]
            id_vec: _containers.RepeatedScalarFieldContainer[int]
            def __init__(self, id_vec: _Optional[_Iterable[int]] = ...) -> None: ...
        CONSUMER_GROUPS_FIELD_NUMBER: _ClassVar[int]
        RECORD_RETENTION_PERIOD_USECS_FIELD_NUMBER: _ClassVar[int]
        consumer_groups: ClusterConfigProto.TopicMetadata.ConsumerGroups
        record_retention_period_usecs: int
        def __init__(self, consumer_groups: _Optional[_Union[ClusterConfigProto.TopicMetadata.ConsumerGroups, _Mapping]] = ..., record_retention_period_usecs: _Optional[int] = ...) -> None: ...
    class TopicToMetadataMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: ClusterConfigProto.TopicMetadata
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[ClusterConfigProto.TopicMetadata, _Mapping]] = ...) -> None: ...
    class ConsumerGroupIds(_message.Message):
        __slots__ = ("yoda_id", "helios_id", "on_prem_helios_id", "groot_id", "yoda_cluster_logs_id")
        YODA_ID_FIELD_NUMBER: _ClassVar[int]
        HELIOS_ID_FIELD_NUMBER: _ClassVar[int]
        ON_PREM_HELIOS_ID_FIELD_NUMBER: _ClassVar[int]
        GROOT_ID_FIELD_NUMBER: _ClassVar[int]
        YODA_CLUSTER_LOGS_ID_FIELD_NUMBER: _ClassVar[int]
        yoda_id: int
        helios_id: int
        on_prem_helios_id: int
        groot_id: int
        yoda_cluster_logs_id: int
        def __init__(self, yoda_id: _Optional[int] = ..., helios_id: _Optional[int] = ..., on_prem_helios_id: _Optional[int] = ..., groot_id: _Optional[int] = ..., yoda_cluster_logs_id: _Optional[int] = ...) -> None: ...
    class AuditLoggingConfig(_message.Message):
        __slots__ = ("audit_logging_enabled", "retention_period_days", "view_box_name", "view_name", "audit_tag", "verbose_audit", "inherit_from_view")
        AUDIT_LOGGING_ENABLED_FIELD_NUMBER: _ClassVar[int]
        RETENTION_PERIOD_DAYS_FIELD_NUMBER: _ClassVar[int]
        VIEW_BOX_NAME_FIELD_NUMBER: _ClassVar[int]
        VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
        AUDIT_TAG_FIELD_NUMBER: _ClassVar[int]
        VERBOSE_AUDIT_FIELD_NUMBER: _ClassVar[int]
        INHERIT_FROM_VIEW_FIELD_NUMBER: _ClassVar[int]
        audit_logging_enabled: bool
        retention_period_days: int
        view_box_name: str
        view_name: str
        audit_tag: str
        verbose_audit: bool
        inherit_from_view: bool
        def __init__(self, audit_logging_enabled: bool = ..., retention_period_days: _Optional[int] = ..., view_box_name: _Optional[str] = ..., view_name: _Optional[str] = ..., audit_tag: _Optional[str] = ..., verbose_audit: bool = ..., inherit_from_view: bool = ...) -> None: ...
    class RemoteLogServerConfig(_message.Message):
        __slots__ = ("server_name", "server_ip", "port", "protocol", "enabled", "id", "facility_vec", "programename_vec", "msg_pattern_vec", "rawmsg_pattern_vec", "is_tls_enabled", "ca_certificate", "token_id")
        class Protocol(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kUDP: _ClassVar[ClusterConfigProto.RemoteLogServerConfig.Protocol]
            kTCP: _ClassVar[ClusterConfigProto.RemoteLogServerConfig.Protocol]
        kUDP: ClusterConfigProto.RemoteLogServerConfig.Protocol
        kTCP: ClusterConfigProto.RemoteLogServerConfig.Protocol
        SERVER_NAME_FIELD_NUMBER: _ClassVar[int]
        SERVER_IP_FIELD_NUMBER: _ClassVar[int]
        PORT_FIELD_NUMBER: _ClassVar[int]
        PROTOCOL_FIELD_NUMBER: _ClassVar[int]
        ENABLED_FIELD_NUMBER: _ClassVar[int]
        ID_FIELD_NUMBER: _ClassVar[int]
        FACILITY_VEC_FIELD_NUMBER: _ClassVar[int]
        PROGRAMENAME_VEC_FIELD_NUMBER: _ClassVar[int]
        MSG_PATTERN_VEC_FIELD_NUMBER: _ClassVar[int]
        RAWMSG_PATTERN_VEC_FIELD_NUMBER: _ClassVar[int]
        IS_TLS_ENABLED_FIELD_NUMBER: _ClassVar[int]
        CA_CERTIFICATE_FIELD_NUMBER: _ClassVar[int]
        TOKEN_ID_FIELD_NUMBER: _ClassVar[int]
        server_name: str
        server_ip: str
        port: int
        protocol: ClusterConfigProto.RemoteLogServerConfig.Protocol
        enabled: bool
        id: int
        facility_vec: _containers.RepeatedScalarFieldContainer[str]
        programename_vec: _containers.RepeatedScalarFieldContainer[str]
        msg_pattern_vec: _containers.RepeatedScalarFieldContainer[str]
        rawmsg_pattern_vec: _containers.RepeatedScalarFieldContainer[str]
        is_tls_enabled: bool
        ca_certificate: str
        token_id: str
        def __init__(self, server_name: _Optional[str] = ..., server_ip: _Optional[str] = ..., port: _Optional[int] = ..., protocol: _Optional[_Union[ClusterConfigProto.RemoteLogServerConfig.Protocol, str]] = ..., enabled: bool = ..., id: _Optional[int] = ..., facility_vec: _Optional[_Iterable[str]] = ..., programename_vec: _Optional[_Iterable[str]] = ..., msg_pattern_vec: _Optional[_Iterable[str]] = ..., rawmsg_pattern_vec: _Optional[_Iterable[str]] = ..., is_tls_enabled: bool = ..., ca_certificate: _Optional[str] = ..., token_id: _Optional[str] = ...) -> None: ...
    class RemoteLogServerInfo(_message.Message):
        __slots__ = ("remote_log_server_vec", "version")
        REMOTE_LOG_SERVER_VEC_FIELD_NUMBER: _ClassVar[int]
        VERSION_FIELD_NUMBER: _ClassVar[int]
        remote_log_server_vec: _containers.RepeatedCompositeFieldContainer[ClusterConfigProto.RemoteLogServerConfig]
        version: int
        def __init__(self, remote_log_server_vec: _Optional[_Iterable[_Union[ClusterConfigProto.RemoteLogServerConfig, _Mapping]]] = ..., version: _Optional[int] = ...) -> None: ...
    class RemoteLogServers(_message.Message):
        __slots__ = ("remote_log_servers",)
        REMOTE_LOG_SERVERS_FIELD_NUMBER: _ClassVar[int]
        remote_log_servers: _containers.RepeatedCompositeFieldContainer[ClusterConfigProto.RemoteLogServerConfig]
        def __init__(self, remote_log_servers: _Optional[_Iterable[_Union[ClusterConfigProto.RemoteLogServerConfig, _Mapping]]] = ...) -> None: ...
    class TopicToRemoteLogServersMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: ClusterConfigProto.RemoteLogServers
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[ClusterConfigProto.RemoteLogServers, _Mapping]] = ...) -> None: ...
    class NetworkZone(_message.Message):
        __slots__ = ("zone_name", "vip_group", "description", "gateway", "subnet_id", "static_route_vec", "tenant_id", "vip_policy_type", "fqdn", "conn_policy")
        class VipAssignmentPolicy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kLeastVipsPerNode: _ClassVar[ClusterConfigProto.NetworkZone.VipAssignmentPolicy]
            kHighPerformanceNode: _ClassVar[ClusterConfigProto.NetworkZone.VipAssignmentPolicy]
            kHighStorageNodes: _ClassVar[ClusterConfigProto.NetworkZone.VipAssignmentPolicy]
        kLeastVipsPerNode: ClusterConfigProto.NetworkZone.VipAssignmentPolicy
        kHighPerformanceNode: ClusterConfigProto.NetworkZone.VipAssignmentPolicy
        kHighStorageNodes: ClusterConfigProto.NetworkZone.VipAssignmentPolicy
        class ConnPolicy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kRoundRobin: _ClassVar[ClusterConfigProto.NetworkZone.ConnPolicy]
            kCpuLoad: _ClassVar[ClusterConfigProto.NetworkZone.ConnPolicy]
            kConnCount: _ClassVar[ClusterConfigProto.NetworkZone.ConnPolicy]
            kThroughput: _ClassVar[ClusterConfigProto.NetworkZone.ConnPolicy]
        kRoundRobin: ClusterConfigProto.NetworkZone.ConnPolicy
        kCpuLoad: ClusterConfigProto.NetworkZone.ConnPolicy
        kConnCount: ClusterConfigProto.NetworkZone.ConnPolicy
        kThroughput: ClusterConfigProto.NetworkZone.ConnPolicy
        ZONE_NAME_FIELD_NUMBER: _ClassVar[int]
        VIP_GROUP_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        GATEWAY_FIELD_NUMBER: _ClassVar[int]
        SUBNET_ID_FIELD_NUMBER: _ClassVar[int]
        STATIC_ROUTE_VEC_FIELD_NUMBER: _ClassVar[int]
        TENANT_ID_FIELD_NUMBER: _ClassVar[int]
        VIP_POLICY_TYPE_FIELD_NUMBER: _ClassVar[int]
        FQDN_FIELD_NUMBER: _ClassVar[int]
        CONN_POLICY_FIELD_NUMBER: _ClassVar[int]
        zone_name: str
        vip_group: _containers.RepeatedScalarFieldContainer[str]
        description: str
        gateway: str
        subnet_id: int
        static_route_vec: _containers.RepeatedScalarFieldContainer[int]
        tenant_id: str
        vip_policy_type: ClusterConfigProto.NetworkZone.VipAssignmentPolicy
        fqdn: str
        conn_policy: ClusterConfigProto.NetworkZone.ConnPolicy
        def __init__(self, zone_name: _Optional[str] = ..., vip_group: _Optional[_Iterable[str]] = ..., description: _Optional[str] = ..., gateway: _Optional[str] = ..., subnet_id: _Optional[int] = ..., static_route_vec: _Optional[_Iterable[int]] = ..., tenant_id: _Optional[str] = ..., vip_policy_type: _Optional[_Union[ClusterConfigProto.NetworkZone.VipAssignmentPolicy, str]] = ..., fqdn: _Optional[str] = ..., conn_policy: _Optional[_Union[ClusterConfigProto.NetworkZone.ConnPolicy, str]] = ...) -> None: ...
    class BondingOpts(_message.Message):
        __slots__ = ("mode", "xmit_hash_policy", "lacp_rate")
        MODE_FIELD_NUMBER: _ClassVar[int]
        XMIT_HASH_POLICY_FIELD_NUMBER: _ClassVar[int]
        LACP_RATE_FIELD_NUMBER: _ClassVar[int]
        mode: ClusterConfigProto.BondingMode
        xmit_hash_policy: ClusterConfigProto.XmitHashPolicy
        lacp_rate: ClusterConfigProto.LacpRate
        def __init__(self, mode: _Optional[_Union[ClusterConfigProto.BondingMode, str]] = ..., xmit_hash_policy: _Optional[_Union[ClusterConfigProto.XmitHashPolicy, str]] = ..., lacp_rate: _Optional[_Union[ClusterConfigProto.LacpRate, str]] = ...) -> None: ...
    class NetworkParams(_message.Message):
        __slots__ = ("mtu", "bonding_mode", "bonding_opts")
        MTU_FIELD_NUMBER: _ClassVar[int]
        BONDING_MODE_FIELD_NUMBER: _ClassVar[int]
        BONDING_OPTS_FIELD_NUMBER: _ClassVar[int]
        mtu: int
        bonding_mode: int
        bonding_opts: ClusterConfigProto.BondingOpts
        def __init__(self, mtu: _Optional[int] = ..., bonding_mode: _Optional[int] = ..., bonding_opts: _Optional[_Union[ClusterConfigProto.BondingOpts, _Mapping]] = ...) -> None: ...
    class IpPool(_message.Message):
        __slots__ = ("name", "ip_vec")
        NAME_FIELD_NUMBER: _ClassVar[int]
        IP_VEC_FIELD_NUMBER: _ClassVar[int]
        name: str
        ip_vec: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, name: _Optional[str] = ..., ip_vec: _Optional[_Iterable[str]] = ...) -> None: ...
    class VipFollowers(_message.Message):
        __slots__ = ("vip", "ip_vec")
        VIP_FIELD_NUMBER: _ClassVar[int]
        IP_VEC_FIELD_NUMBER: _ClassVar[int]
        vip: str
        ip_vec: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, vip: _Optional[str] = ..., ip_vec: _Optional[_Iterable[str]] = ...) -> None: ...
    class Vlan(_message.Message):
        __slots__ = ("vlan_tag", "gateway", "subnet", "ip_vec", "description", "hostname", "tenant_id", "interface_name", "vlan_name", "rt_table_id", "static_route_vec", "firewall_profile_vec", "mtu", "subnet_id", "interface_group_id", "interface_group", "all_tenant_access", "partial_vips_mode", "node_ip_assignment", "subnet_vec", "gateway_vec", "apps_ip_vec", "apps_ip_vec_in_use", "ip_pool_vec", "vip_followers", "zone_name_to_zone_config", "ecmp_enabled")
        class NodeIpAssignmentEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: int
            value: str
            def __init__(self, key: _Optional[int] = ..., value: _Optional[str] = ...) -> None: ...
        class DnsZoneDelegationConfig(_message.Message):
            __slots__ = ("server_vip_vec", "dns_server_all_vips", "resolved_vip_vec")
            SERVER_VIP_VEC_FIELD_NUMBER: _ClassVar[int]
            DNS_SERVER_ALL_VIPS_FIELD_NUMBER: _ClassVar[int]
            RESOLVED_VIP_VEC_FIELD_NUMBER: _ClassVar[int]
            server_vip_vec: _containers.RepeatedScalarFieldContainer[str]
            dns_server_all_vips: bool
            resolved_vip_vec: _containers.RepeatedScalarFieldContainer[str]
            def __init__(self, server_vip_vec: _Optional[_Iterable[str]] = ..., dns_server_all_vips: bool = ..., resolved_vip_vec: _Optional[_Iterable[str]] = ...) -> None: ...
        class ZoneNameToZoneConfigEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: ClusterConfigProto.Vlan.DnsZoneDelegationConfig
            def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[ClusterConfigProto.Vlan.DnsZoneDelegationConfig, _Mapping]] = ...) -> None: ...
        VLAN_TAG_FIELD_NUMBER: _ClassVar[int]
        GATEWAY_FIELD_NUMBER: _ClassVar[int]
        SUBNET_FIELD_NUMBER: _ClassVar[int]
        IP_VEC_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        HOSTNAME_FIELD_NUMBER: _ClassVar[int]
        TENANT_ID_FIELD_NUMBER: _ClassVar[int]
        INTERFACE_NAME_FIELD_NUMBER: _ClassVar[int]
        VLAN_NAME_FIELD_NUMBER: _ClassVar[int]
        RT_TABLE_ID_FIELD_NUMBER: _ClassVar[int]
        STATIC_ROUTE_VEC_FIELD_NUMBER: _ClassVar[int]
        FIREWALL_PROFILE_VEC_FIELD_NUMBER: _ClassVar[int]
        MTU_FIELD_NUMBER: _ClassVar[int]
        SUBNET_ID_FIELD_NUMBER: _ClassVar[int]
        INTERFACE_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
        INTERFACE_GROUP_FIELD_NUMBER: _ClassVar[int]
        ALL_TENANT_ACCESS_FIELD_NUMBER: _ClassVar[int]
        PARTIAL_VIPS_MODE_FIELD_NUMBER: _ClassVar[int]
        NODE_IP_ASSIGNMENT_FIELD_NUMBER: _ClassVar[int]
        SUBNET_VEC_FIELD_NUMBER: _ClassVar[int]
        GATEWAY_VEC_FIELD_NUMBER: _ClassVar[int]
        APPS_IP_VEC_FIELD_NUMBER: _ClassVar[int]
        APPS_IP_VEC_IN_USE_FIELD_NUMBER: _ClassVar[int]
        IP_POOL_VEC_FIELD_NUMBER: _ClassVar[int]
        VIP_FOLLOWERS_FIELD_NUMBER: _ClassVar[int]
        ZONE_NAME_TO_ZONE_CONFIG_FIELD_NUMBER: _ClassVar[int]
        ECMP_ENABLED_FIELD_NUMBER: _ClassVar[int]
        vlan_tag: int
        gateway: str
        subnet: ClusterConfigProto.Subnet
        ip_vec: _containers.RepeatedScalarFieldContainer[str]
        description: str
        hostname: str
        tenant_id: str
        interface_name: str
        vlan_name: str
        rt_table_id: int
        static_route_vec: _containers.RepeatedScalarFieldContainer[int]
        firewall_profile_vec: _containers.RepeatedScalarFieldContainer[int]
        mtu: int
        subnet_id: int
        interface_group_id: int
        interface_group: str
        all_tenant_access: bool
        partial_vips_mode: bool
        node_ip_assignment: _containers.ScalarMap[int, str]
        subnet_vec: _containers.RepeatedCompositeFieldContainer[ClusterConfigProto.Subnet]
        gateway_vec: _containers.RepeatedScalarFieldContainer[str]
        apps_ip_vec: _containers.RepeatedScalarFieldContainer[str]
        apps_ip_vec_in_use: bool
        ip_pool_vec: _containers.RepeatedCompositeFieldContainer[ClusterConfigProto.IpPool]
        vip_followers: _containers.RepeatedCompositeFieldContainer[ClusterConfigProto.VipFollowers]
        zone_name_to_zone_config: _containers.MessageMap[str, ClusterConfigProto.Vlan.DnsZoneDelegationConfig]
        ecmp_enabled: bool
        def __init__(self, vlan_tag: _Optional[int] = ..., gateway: _Optional[str] = ..., subnet: _Optional[_Union[ClusterConfigProto.Subnet, _Mapping]] = ..., ip_vec: _Optional[_Iterable[str]] = ..., description: _Optional[str] = ..., hostname: _Optional[str] = ..., tenant_id: _Optional[str] = ..., interface_name: _Optional[str] = ..., vlan_name: _Optional[str] = ..., rt_table_id: _Optional[int] = ..., static_route_vec: _Optional[_Iterable[int]] = ..., firewall_profile_vec: _Optional[_Iterable[int]] = ..., mtu: _Optional[int] = ..., subnet_id: _Optional[int] = ..., interface_group_id: _Optional[int] = ..., interface_group: _Optional[str] = ..., all_tenant_access: bool = ..., partial_vips_mode: bool = ..., node_ip_assignment: _Optional[_Mapping[int, str]] = ..., subnet_vec: _Optional[_Iterable[_Union[ClusterConfigProto.Subnet, _Mapping]]] = ..., gateway_vec: _Optional[_Iterable[str]] = ..., apps_ip_vec: _Optional[_Iterable[str]] = ..., apps_ip_vec_in_use: bool = ..., ip_pool_vec: _Optional[_Iterable[_Union[ClusterConfigProto.IpPool, _Mapping]]] = ..., vip_followers: _Optional[_Iterable[_Union[ClusterConfigProto.VipFollowers, _Mapping]]] = ..., zone_name_to_zone_config: _Optional[_Mapping[str, ClusterConfigProto.Vlan.DnsZoneDelegationConfig]] = ..., ecmp_enabled: bool = ...) -> None: ...
    class StaticRoute(_message.Message):
        __slots__ = ("dest_subnet", "deprecated_vlan_id", "interface_id_vec", "description", "next_hop", "deprecated_interface_name", "id", "interface_group_id", "interface_group", "mtu")
        DEST_SUBNET_FIELD_NUMBER: _ClassVar[int]
        DEPRECATED_VLAN_ID_FIELD_NUMBER: _ClassVar[int]
        INTERFACE_ID_VEC_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        NEXT_HOP_FIELD_NUMBER: _ClassVar[int]
        DEPRECATED_INTERFACE_NAME_FIELD_NUMBER: _ClassVar[int]
        ID_FIELD_NUMBER: _ClassVar[int]
        INTERFACE_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
        INTERFACE_GROUP_FIELD_NUMBER: _ClassVar[int]
        MTU_FIELD_NUMBER: _ClassVar[int]
        dest_subnet: ClusterConfigProto.Subnet
        deprecated_vlan_id: int
        interface_id_vec: _containers.RepeatedScalarFieldContainer[int]
        description: str
        next_hop: str
        deprecated_interface_name: str
        id: int
        interface_group_id: int
        interface_group: str
        mtu: int
        def __init__(self, dest_subnet: _Optional[_Union[ClusterConfigProto.Subnet, _Mapping]] = ..., deprecated_vlan_id: _Optional[int] = ..., interface_id_vec: _Optional[_Iterable[int]] = ..., description: _Optional[str] = ..., next_hop: _Optional[str] = ..., deprecated_interface_name: _Optional[str] = ..., id: _Optional[int] = ..., interface_group_id: _Optional[int] = ..., interface_group: _Optional[str] = ..., mtu: _Optional[int] = ...) -> None: ...
    class AWSProxyInfo(_message.Message):
        __slots__ = ("region_name", "port", "ip_vec")
        REGION_NAME_FIELD_NUMBER: _ClassVar[int]
        PORT_FIELD_NUMBER: _ClassVar[int]
        IP_VEC_FIELD_NUMBER: _ClassVar[int]
        region_name: str
        port: int
        ip_vec: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, region_name: _Optional[str] = ..., port: _Optional[int] = ..., ip_vec: _Optional[_Iterable[str]] = ...) -> None: ...
    class TenantDeletionInfo(_message.Message):
        __slots__ = ("tenant_id", "view_box_id_vec", "removal_state")
        TENANT_ID_FIELD_NUMBER: _ClassVar[int]
        VIEW_BOX_ID_VEC_FIELD_NUMBER: _ClassVar[int]
        REMOVAL_STATE_FIELD_NUMBER: _ClassVar[int]
        tenant_id: str
        view_box_id_vec: _containers.RepeatedScalarFieldContainer[int]
        removal_state: ClusterConfigProto.RemovalState
        def __init__(self, tenant_id: _Optional[str] = ..., view_box_id_vec: _Optional[_Iterable[int]] = ..., removal_state: _Optional[_Union[ClusterConfigProto.RemovalState, _Mapping]] = ...) -> None: ...
    class FirewallProfile(_message.Message):
        __slots__ = ("id", "type", "name")
        ID_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        id: int
        type: ClusterConfigProto.FirewallProfileType
        name: str
        def __init__(self, id: _Optional[int] = ..., type: _Optional[_Union[ClusterConfigProto.FirewallProfileType, str]] = ..., name: _Optional[str] = ...) -> None: ...
    class AthenaConfig(_message.Message):
        __slots__ = ("view_box_name", "internal_view_name", "kubernetes_subnet_id_deprecated", "marketplace_apps_mode", "reserved_cpu_millicores", "reserved_memory_pct", "overcommit_memory_pct", "incarnation_id", "allow_external_traffic", "vm_ip", "allow_unrestricted_view_access", "kubernetes_cluster_system_services_ip_range", "kubernetes_cluster_system_services_ip6_range", "has_reenabled_with_axon_networking", "system_service_memory_mb", "system_service_cpu_milli_cores", "apps_mode", "allow_change_app_mode", "is_athena_subnet_clash", "flannel_config", "has_switched_to_flannel_networking")
        class AppsMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kUnknown: _ClassVar[ClusterConfigProto.AthenaConfig.AppsMode]
            kDisabled: _ClassVar[ClusterConfigProto.AthenaConfig.AppsMode]
            kBareMetal: _ClassVar[ClusterConfigProto.AthenaConfig.AppsMode]
            kVMOnly: _ClassVar[ClusterConfigProto.AthenaConfig.AppsMode]
        kUnknown: ClusterConfigProto.AthenaConfig.AppsMode
        kDisabled: ClusterConfigProto.AthenaConfig.AppsMode
        kBareMetal: ClusterConfigProto.AthenaConfig.AppsMode
        kVMOnly: ClusterConfigProto.AthenaConfig.AppsMode
        class FlannelConfig(_message.Message):
            __slots__ = ("backend",)
            class Backend(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                UNKNOWN: _ClassVar[ClusterConfigProto.AthenaConfig.FlannelConfig.Backend]
                VXLAN: _ClassVar[ClusterConfigProto.AthenaConfig.FlannelConfig.Backend]
                WIRE_GUARD: _ClassVar[ClusterConfigProto.AthenaConfig.FlannelConfig.Backend]
                HOST_GW: _ClassVar[ClusterConfigProto.AthenaConfig.FlannelConfig.Backend]
            UNKNOWN: ClusterConfigProto.AthenaConfig.FlannelConfig.Backend
            VXLAN: ClusterConfigProto.AthenaConfig.FlannelConfig.Backend
            WIRE_GUARD: ClusterConfigProto.AthenaConfig.FlannelConfig.Backend
            HOST_GW: ClusterConfigProto.AthenaConfig.FlannelConfig.Backend
            BACKEND_FIELD_NUMBER: _ClassVar[int]
            backend: ClusterConfigProto.AthenaConfig.FlannelConfig.Backend
            def __init__(self, backend: _Optional[_Union[ClusterConfigProto.AthenaConfig.FlannelConfig.Backend, str]] = ...) -> None: ...
        VIEW_BOX_NAME_FIELD_NUMBER: _ClassVar[int]
        INTERNAL_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
        KUBERNETES_SUBNET_ID_DEPRECATED_FIELD_NUMBER: _ClassVar[int]
        MARKETPLACE_APPS_MODE_FIELD_NUMBER: _ClassVar[int]
        RESERVED_CPU_MILLICORES_FIELD_NUMBER: _ClassVar[int]
        RESERVED_MEMORY_PCT_FIELD_NUMBER: _ClassVar[int]
        OVERCOMMIT_MEMORY_PCT_FIELD_NUMBER: _ClassVar[int]
        INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
        ALLOW_EXTERNAL_TRAFFIC_FIELD_NUMBER: _ClassVar[int]
        VM_IP_FIELD_NUMBER: _ClassVar[int]
        ALLOW_UNRESTRICTED_VIEW_ACCESS_FIELD_NUMBER: _ClassVar[int]
        KUBERNETES_CLUSTER_SYSTEM_SERVICES_IP_RANGE_FIELD_NUMBER: _ClassVar[int]
        KUBERNETES_CLUSTER_SYSTEM_SERVICES_IP6_RANGE_FIELD_NUMBER: _ClassVar[int]
        HAS_REENABLED_WITH_AXON_NETWORKING_FIELD_NUMBER: _ClassVar[int]
        SYSTEM_SERVICE_MEMORY_MB_FIELD_NUMBER: _ClassVar[int]
        SYSTEM_SERVICE_CPU_MILLI_CORES_FIELD_NUMBER: _ClassVar[int]
        APPS_MODE_FIELD_NUMBER: _ClassVar[int]
        ALLOW_CHANGE_APP_MODE_FIELD_NUMBER: _ClassVar[int]
        IS_ATHENA_SUBNET_CLASH_FIELD_NUMBER: _ClassVar[int]
        FLANNEL_CONFIG_FIELD_NUMBER: _ClassVar[int]
        HAS_SWITCHED_TO_FLANNEL_NETWORKING_FIELD_NUMBER: _ClassVar[int]
        view_box_name: str
        internal_view_name: str
        kubernetes_subnet_id_deprecated: int
        marketplace_apps_mode: ClusterConfigProto.AthenaConfig.AppsMode
        reserved_cpu_millicores: int
        reserved_memory_pct: int
        overcommit_memory_pct: int
        incarnation_id: int
        allow_external_traffic: bool
        vm_ip: str
        allow_unrestricted_view_access: bool
        kubernetes_cluster_system_services_ip_range: str
        kubernetes_cluster_system_services_ip6_range: str
        has_reenabled_with_axon_networking: bool
        system_service_memory_mb: int
        system_service_cpu_milli_cores: int
        apps_mode: ClusterConfigProto.AthenaConfig.AppsMode
        allow_change_app_mode: bool
        is_athena_subnet_clash: bool
        flannel_config: ClusterConfigProto.AthenaConfig.FlannelConfig
        has_switched_to_flannel_networking: bool
        def __init__(self, view_box_name: _Optional[str] = ..., internal_view_name: _Optional[str] = ..., kubernetes_subnet_id_deprecated: _Optional[int] = ..., marketplace_apps_mode: _Optional[_Union[ClusterConfigProto.AthenaConfig.AppsMode, str]] = ..., reserved_cpu_millicores: _Optional[int] = ..., reserved_memory_pct: _Optional[int] = ..., overcommit_memory_pct: _Optional[int] = ..., incarnation_id: _Optional[int] = ..., allow_external_traffic: bool = ..., vm_ip: _Optional[str] = ..., allow_unrestricted_view_access: bool = ..., kubernetes_cluster_system_services_ip_range: _Optional[str] = ..., kubernetes_cluster_system_services_ip6_range: _Optional[str] = ..., has_reenabled_with_axon_networking: bool = ..., system_service_memory_mb: _Optional[int] = ..., system_service_cpu_milli_cores: _Optional[int] = ..., apps_mode: _Optional[_Union[ClusterConfigProto.AthenaConfig.AppsMode, str]] = ..., allow_change_app_mode: bool = ..., is_athena_subnet_clash: bool = ..., flannel_config: _Optional[_Union[ClusterConfigProto.AthenaConfig.FlannelConfig, _Mapping]] = ..., has_switched_to_flannel_networking: bool = ...) -> None: ...
    class AntivirusConfig(_message.Message):
        __slots__ = ("antivirus_service_group_map", "default_antivirus_service_group_id", "last_antivirus_service_group_id", "last_antivirus_service_id")
        class AntivirusServiceConfig(_message.Message):
            __slots__ = ("id", "enabled", "icap_uri", "description", "tag", "tag_id")
            ID_FIELD_NUMBER: _ClassVar[int]
            ENABLED_FIELD_NUMBER: _ClassVar[int]
            ICAP_URI_FIELD_NUMBER: _ClassVar[int]
            DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
            TAG_FIELD_NUMBER: _ClassVar[int]
            TAG_ID_FIELD_NUMBER: _ClassVar[int]
            id: int
            enabled: bool
            icap_uri: str
            description: str
            tag: str
            tag_id: int
            def __init__(self, id: _Optional[int] = ..., enabled: bool = ..., icap_uri: _Optional[str] = ..., description: _Optional[str] = ..., tag: _Optional[str] = ..., tag_id: _Optional[int] = ...) -> None: ...
        class AntivirusServices(_message.Message):
            __slots__ = ("id", "name", "description", "antivirus_service_map", "internal")
            class AntivirusServiceMapEntry(_message.Message):
                __slots__ = ("key", "value")
                KEY_FIELD_NUMBER: _ClassVar[int]
                VALUE_FIELD_NUMBER: _ClassVar[int]
                key: int
                value: ClusterConfigProto.AntivirusConfig.AntivirusServiceConfig
                def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[ClusterConfigProto.AntivirusConfig.AntivirusServiceConfig, _Mapping]] = ...) -> None: ...
            ID_FIELD_NUMBER: _ClassVar[int]
            NAME_FIELD_NUMBER: _ClassVar[int]
            DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
            ANTIVIRUS_SERVICE_MAP_FIELD_NUMBER: _ClassVar[int]
            INTERNAL_FIELD_NUMBER: _ClassVar[int]
            id: int
            name: str
            description: str
            antivirus_service_map: _containers.MessageMap[int, ClusterConfigProto.AntivirusConfig.AntivirusServiceConfig]
            internal: bool
            def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., antivirus_service_map: _Optional[_Mapping[int, ClusterConfigProto.AntivirusConfig.AntivirusServiceConfig]] = ..., internal: bool = ...) -> None: ...
        class AntivirusServiceGroupMapEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: int
            value: ClusterConfigProto.AntivirusConfig.AntivirusServices
            def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[ClusterConfigProto.AntivirusConfig.AntivirusServices, _Mapping]] = ...) -> None: ...
        ANTIVIRUS_SERVICE_GROUP_MAP_FIELD_NUMBER: _ClassVar[int]
        DEFAULT_ANTIVIRUS_SERVICE_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
        LAST_ANTIVIRUS_SERVICE_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
        LAST_ANTIVIRUS_SERVICE_ID_FIELD_NUMBER: _ClassVar[int]
        antivirus_service_group_map: _containers.MessageMap[int, ClusterConfigProto.AntivirusConfig.AntivirusServices]
        default_antivirus_service_group_id: int
        last_antivirus_service_group_id: int
        last_antivirus_service_id: int
        def __init__(self, antivirus_service_group_map: _Optional[_Mapping[int, ClusterConfigProto.AntivirusConfig.AntivirusServices]] = ..., default_antivirus_service_group_id: _Optional[int] = ..., last_antivirus_service_group_id: _Optional[int] = ..., last_antivirus_service_id: _Optional[int] = ...) -> None: ...
    class ProductModelInterfaceTuple(_message.Message):
        __slots__ = ("product_model", "interface_name")
        PRODUCT_MODEL_FIELD_NUMBER: _ClassVar[int]
        INTERFACE_NAME_FIELD_NUMBER: _ClassVar[int]
        product_model: ClusterConfigProto.ProductModel
        interface_name: str
        def __init__(self, product_model: _Optional[_Union[ClusterConfigProto.ProductModel, str]] = ..., interface_name: _Optional[str] = ...) -> None: ...
    class NodeInterfacePair(_message.Message):
        __slots__ = ("node_id_vec", "interface_name")
        NODE_ID_VEC_FIELD_NUMBER: _ClassVar[int]
        INTERFACE_NAME_FIELD_NUMBER: _ClassVar[int]
        node_id_vec: _containers.RepeatedScalarFieldContainer[int]
        interface_name: str
        def __init__(self, node_id_vec: _Optional[_Iterable[int]] = ..., interface_name: _Optional[str] = ...) -> None: ...
    class InterfaceGroup(_message.Message):
        __slots__ = ("id", "name", "model_interface_vec", "networkParams", "node_interface_pairs", "group_type")
        ID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        MODEL_INTERFACE_VEC_FIELD_NUMBER: _ClassVar[int]
        NETWORKPARAMS_FIELD_NUMBER: _ClassVar[int]
        NODE_INTERFACE_PAIRS_FIELD_NUMBER: _ClassVar[int]
        GROUP_TYPE_FIELD_NUMBER: _ClassVar[int]
        id: int
        name: str
        model_interface_vec: _containers.RepeatedCompositeFieldContainer[ClusterConfigProto.ProductModelInterfaceTuple]
        networkParams: ClusterConfigProto.NetworkParams
        node_interface_pairs: _containers.RepeatedCompositeFieldContainer[ClusterConfigProto.NodeInterfacePair]
        group_type: ClusterConfigProto.InterfaceGroupType
        def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., model_interface_vec: _Optional[_Iterable[_Union[ClusterConfigProto.ProductModelInterfaceTuple, _Mapping]]] = ..., networkParams: _Optional[_Union[ClusterConfigProto.NetworkParams, _Mapping]] = ..., node_interface_pairs: _Optional[_Iterable[_Union[ClusterConfigProto.NodeInterfacePair, _Mapping]]] = ..., group_type: _Optional[_Union[ClusterConfigProto.InterfaceGroupType, str]] = ...) -> None: ...
    class TLSCertConfig(_message.Message):
        __slots__ = ("encrypted_private_key", "certificate")
        ENCRYPTED_PRIVATE_KEY_FIELD_NUMBER: _ClassVar[int]
        CERTIFICATE_FIELD_NUMBER: _ClassVar[int]
        encrypted_private_key: bytes
        certificate: bytes
        def __init__(self, encrypted_private_key: _Optional[bytes] = ..., certificate: _Optional[bytes] = ...) -> None: ...
    class MetadataInfo(_message.Message):
        __slots__ = ("cluster_capacity_bytes",)
        CLUSTER_CAPACITY_BYTES_FIELD_NUMBER: _ClassVar[int]
        cluster_capacity_bytes: int
        def __init__(self, cluster_capacity_bytes: _Optional[int] = ...) -> None: ...
    class HeliosViewsProto(_message.Message):
        __slots__ = ("internal_helios_view_box_name", "helios_snapshots_diff_view_name")
        INTERNAL_HELIOS_VIEW_BOX_NAME_FIELD_NUMBER: _ClassVar[int]
        HELIOS_SNAPSHOTS_DIFF_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
        internal_helios_view_box_name: str
        helios_snapshots_diff_view_name: str
        def __init__(self, internal_helios_view_box_name: _Optional[str] = ..., helios_snapshots_diff_view_name: _Optional[str] = ...) -> None: ...
    class KeystoneConfig(_message.Message):
        __slots__ = ("id", "name", "www_authenticate_uri", "auth_url", "admin_domain_id", "admin_domain_name", "admin_username", "admin_encrypted_password", "project_domain_id", "project_domain_name", "project_name", "domain_name")
        ID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        WWW_AUTHENTICATE_URI_FIELD_NUMBER: _ClassVar[int]
        AUTH_URL_FIELD_NUMBER: _ClassVar[int]
        ADMIN_DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
        ADMIN_DOMAIN_NAME_FIELD_NUMBER: _ClassVar[int]
        ADMIN_USERNAME_FIELD_NUMBER: _ClassVar[int]
        ADMIN_ENCRYPTED_PASSWORD_FIELD_NUMBER: _ClassVar[int]
        PROJECT_DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
        PROJECT_DOMAIN_NAME_FIELD_NUMBER: _ClassVar[int]
        PROJECT_NAME_FIELD_NUMBER: _ClassVar[int]
        DOMAIN_NAME_FIELD_NUMBER: _ClassVar[int]
        id: int
        name: str
        www_authenticate_uri: str
        auth_url: str
        admin_domain_id: str
        admin_domain_name: str
        admin_username: str
        admin_encrypted_password: bytes
        project_domain_id: str
        project_domain_name: str
        project_name: str
        domain_name: str
        def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., www_authenticate_uri: _Optional[str] = ..., auth_url: _Optional[str] = ..., admin_domain_id: _Optional[str] = ..., admin_domain_name: _Optional[str] = ..., admin_username: _Optional[str] = ..., admin_encrypted_password: _Optional[bytes] = ..., project_domain_id: _Optional[str] = ..., project_domain_name: _Optional[str] = ..., project_name: _Optional[str] = ..., domain_name: _Optional[str] = ...) -> None: ...
    class SwiftConfig(_message.Message):
        __slots__ = ("tenant_id", "keystone_config_id", "reseller_prefix_vec", "reseller_admin_roles_vec", "operator_roles_vec", "service_roles_vec", "account_roles_map", "delay_auth_decision")
        class AccountRoles(_message.Message):
            __slots__ = ("operator_roles_vec", "service_roles_vec")
            OPERATOR_ROLES_VEC_FIELD_NUMBER: _ClassVar[int]
            SERVICE_ROLES_VEC_FIELD_NUMBER: _ClassVar[int]
            operator_roles_vec: _containers.RepeatedScalarFieldContainer[str]
            service_roles_vec: _containers.RepeatedScalarFieldContainer[str]
            def __init__(self, operator_roles_vec: _Optional[_Iterable[str]] = ..., service_roles_vec: _Optional[_Iterable[str]] = ...) -> None: ...
        class AccountRolesMapEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: ClusterConfigProto.SwiftConfig.AccountRoles
            def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[ClusterConfigProto.SwiftConfig.AccountRoles, _Mapping]] = ...) -> None: ...
        TENANT_ID_FIELD_NUMBER: _ClassVar[int]
        KEYSTONE_CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
        RESELLER_PREFIX_VEC_FIELD_NUMBER: _ClassVar[int]
        RESELLER_ADMIN_ROLES_VEC_FIELD_NUMBER: _ClassVar[int]
        OPERATOR_ROLES_VEC_FIELD_NUMBER: _ClassVar[int]
        SERVICE_ROLES_VEC_FIELD_NUMBER: _ClassVar[int]
        ACCOUNT_ROLES_MAP_FIELD_NUMBER: _ClassVar[int]
        DELAY_AUTH_DECISION_FIELD_NUMBER: _ClassVar[int]
        tenant_id: str
        keystone_config_id: int
        reseller_prefix_vec: _containers.RepeatedScalarFieldContainer[str]
        reseller_admin_roles_vec: _containers.RepeatedScalarFieldContainer[str]
        operator_roles_vec: _containers.RepeatedScalarFieldContainer[str]
        service_roles_vec: _containers.RepeatedScalarFieldContainer[str]
        account_roles_map: _containers.MessageMap[str, ClusterConfigProto.SwiftConfig.AccountRoles]
        delay_auth_decision: bool
        def __init__(self, tenant_id: _Optional[str] = ..., keystone_config_id: _Optional[int] = ..., reseller_prefix_vec: _Optional[_Iterable[str]] = ..., reseller_admin_roles_vec: _Optional[_Iterable[str]] = ..., operator_roles_vec: _Optional[_Iterable[str]] = ..., service_roles_vec: _Optional[_Iterable[str]] = ..., account_roles_map: _Optional[_Mapping[str, ClusterConfigProto.SwiftConfig.AccountRoles]] = ..., delay_auth_decision: bool = ...) -> None: ...
    class FeatureFlags(_message.Message):
        __slots__ = ("scribe_enable_heterogenous_cluster_support", "madrox_case_sensitivity_alteration_support")
        SCRIBE_ENABLE_HETEROGENOUS_CLUSTER_SUPPORT_FIELD_NUMBER: _ClassVar[int]
        MADROX_CASE_SENSITIVITY_ALTERATION_SUPPORT_FIELD_NUMBER: _ClassVar[int]
        scribe_enable_heterogenous_cluster_support: bool
        madrox_case_sensitivity_alteration_support: bool
        def __init__(self, scribe_enable_heterogenous_cluster_support: bool = ..., madrox_case_sensitivity_alteration_support: bool = ...) -> None: ...
    class MagnetoAdapterStatus(_message.Message):
        __slots__ = ("not_in_bridge_adapter_mask",)
        class Adapter(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kUnknown: _ClassVar[ClusterConfigProto.MagnetoAdapterStatus.Adapter]
            kOracle: _ClassVar[ClusterConfigProto.MagnetoAdapterStatus.Adapter]
            kAppFile: _ClassVar[ClusterConfigProto.MagnetoAdapterStatus.Adapter]
            kAgent: _ClassVar[ClusterConfigProto.MagnetoAdapterStatus.Adapter]
            kSAN: _ClassVar[ClusterConfigProto.MagnetoAdapterStatus.Adapter]
            kSQL: _ClassVar[ClusterConfigProto.MagnetoAdapterStatus.Adapter]
            kFile: _ClassVar[ClusterConfigProto.MagnetoAdapterStatus.Adapter]
            kPhysical: _ClassVar[ClusterConfigProto.MagnetoAdapterStatus.Adapter]
            kSharePoint: _ClassVar[ClusterConfigProto.MagnetoAdapterStatus.Adapter]
            kO365: _ClassVar[ClusterConfigProto.MagnetoAdapterStatus.Adapter]
            kOneDrive: _ClassVar[ClusterConfigProto.MagnetoAdapterStatus.Adapter]
            kOutlook: _ClassVar[ClusterConfigProto.MagnetoAdapterStatus.Adapter]
            kKVM: _ClassVar[ClusterConfigProto.MagnetoAdapterStatus.Adapter]
            kAcropolis: _ClassVar[ClusterConfigProto.MagnetoAdapterStatus.Adapter]
            kHyperV: _ClassVar[ClusterConfigProto.MagnetoAdapterStatus.Adapter]
            kVMWare: _ClassVar[ClusterConfigProto.MagnetoAdapterStatus.Adapter]
            kView: _ClassVar[ClusterConfigProto.MagnetoAdapterStatus.Adapter]
            kCloud: _ClassVar[ClusterConfigProto.MagnetoAdapterStatus.Adapter]
            kAWS: _ClassVar[ClusterConfigProto.MagnetoAdapterStatus.Adapter]
            kGCP: _ClassVar[ClusterConfigProto.MagnetoAdapterStatus.Adapter]
            kAzure: _ClassVar[ClusterConfigProto.MagnetoAdapterStatus.Adapter]
            kAll: _ClassVar[ClusterConfigProto.MagnetoAdapterStatus.Adapter]
        kUnknown: ClusterConfigProto.MagnetoAdapterStatus.Adapter
        kOracle: ClusterConfigProto.MagnetoAdapterStatus.Adapter
        kAppFile: ClusterConfigProto.MagnetoAdapterStatus.Adapter
        kAgent: ClusterConfigProto.MagnetoAdapterStatus.Adapter
        kSAN: ClusterConfigProto.MagnetoAdapterStatus.Adapter
        kSQL: ClusterConfigProto.MagnetoAdapterStatus.Adapter
        kFile: ClusterConfigProto.MagnetoAdapterStatus.Adapter
        kPhysical: ClusterConfigProto.MagnetoAdapterStatus.Adapter
        kSharePoint: ClusterConfigProto.MagnetoAdapterStatus.Adapter
        kO365: ClusterConfigProto.MagnetoAdapterStatus.Adapter
        kOneDrive: ClusterConfigProto.MagnetoAdapterStatus.Adapter
        kOutlook: ClusterConfigProto.MagnetoAdapterStatus.Adapter
        kKVM: ClusterConfigProto.MagnetoAdapterStatus.Adapter
        kAcropolis: ClusterConfigProto.MagnetoAdapterStatus.Adapter
        kHyperV: ClusterConfigProto.MagnetoAdapterStatus.Adapter
        kVMWare: ClusterConfigProto.MagnetoAdapterStatus.Adapter
        kView: ClusterConfigProto.MagnetoAdapterStatus.Adapter
        kCloud: ClusterConfigProto.MagnetoAdapterStatus.Adapter
        kAWS: ClusterConfigProto.MagnetoAdapterStatus.Adapter
        kGCP: ClusterConfigProto.MagnetoAdapterStatus.Adapter
        kAzure: ClusterConfigProto.MagnetoAdapterStatus.Adapter
        kAll: ClusterConfigProto.MagnetoAdapterStatus.Adapter
        NOT_IN_BRIDGE_ADAPTER_MASK_FIELD_NUMBER: _ClassVar[int]
        not_in_bridge_adapter_mask: int
        def __init__(self, not_in_bridge_adapter_mask: _Optional[int] = ...) -> None: ...
    class NisConfig(_message.Message):
        __slots__ = ("nis_domain_provider_map",)
        class NisProvider(_message.Message):
            __slots__ = ("domain_name", "master_server_hostname", "slave_servers_hostname_vec", "tenant_id_vec")
            DOMAIN_NAME_FIELD_NUMBER: _ClassVar[int]
            MASTER_SERVER_HOSTNAME_FIELD_NUMBER: _ClassVar[int]
            SLAVE_SERVERS_HOSTNAME_VEC_FIELD_NUMBER: _ClassVar[int]
            TENANT_ID_VEC_FIELD_NUMBER: _ClassVar[int]
            domain_name: str
            master_server_hostname: str
            slave_servers_hostname_vec: _containers.RepeatedScalarFieldContainer[str]
            tenant_id_vec: _containers.RepeatedScalarFieldContainer[str]
            def __init__(self, domain_name: _Optional[str] = ..., master_server_hostname: _Optional[str] = ..., slave_servers_hostname_vec: _Optional[_Iterable[str]] = ..., tenant_id_vec: _Optional[_Iterable[str]] = ...) -> None: ...
        class NisDomainProviderMapEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: ClusterConfigProto.NisConfig.NisProvider
            def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[ClusterConfigProto.NisConfig.NisProvider, _Mapping]] = ...) -> None: ...
        NIS_DOMAIN_PROVIDER_MAP_FIELD_NUMBER: _ClassVar[int]
        nis_domain_provider_map: _containers.MessageMap[str, ClusterConfigProto.NisConfig.NisProvider]
        def __init__(self, nis_domain_provider_map: _Optional[_Mapping[str, ClusterConfigProto.NisConfig.NisProvider]] = ...) -> None: ...
    class NISNetgroup(_message.Message):
        __slots__ = ("domain_name", "netgroup_name", "nfs_access", "nfs_root_squash", "nfs_all_squash")
        DOMAIN_NAME_FIELD_NUMBER: _ClassVar[int]
        NETGROUP_NAME_FIELD_NUMBER: _ClassVar[int]
        NFS_ACCESS_FIELD_NUMBER: _ClassVar[int]
        NFS_ROOT_SQUASH_FIELD_NUMBER: _ClassVar[int]
        NFS_ALL_SQUASH_FIELD_NUMBER: _ClassVar[int]
        domain_name: str
        netgroup_name: str
        nfs_access: ClusterConfigProto.ProtocolAccessLevel
        nfs_root_squash: bool
        nfs_all_squash: bool
        def __init__(self, domain_name: _Optional[str] = ..., netgroup_name: _Optional[str] = ..., nfs_access: _Optional[_Union[ClusterConfigProto.ProtocolAccessLevel, str]] = ..., nfs_root_squash: bool = ..., nfs_all_squash: bool = ...) -> None: ...
    class SupportUser(_message.Message):
        __slots__ = ("token", "public_key", "bash_access_valid_until", "sudo_access_valid_until", "password", "is_password_set", "is_sudo_access_enabled", "token_version", "last_password_updated_timestamp_sec", "is_password_converted", "two_fa_mode", "deprecated_totp_secret_key", "deprecated_totp_qr_code_url", "two_fa_email_id", "totp_secret_key", "totp_qr_code_url", "is_sudo_access_life_cycle_migrated", "sudo_access_end_timestamp_msecs", "sudo_access_mode", "can_token_be_encrypted_in_cluster_config", "cluster_ssh_support_user_public_key", "ssh_encrypted_support_user_private_key", "cluster_active_support_user_ssh_private_key_md5sum", "cluster_support_user_target_enc_ssh_priv_key", "cluster_support_user_target_ssh_public_key")
        TOKEN_FIELD_NUMBER: _ClassVar[int]
        PUBLIC_KEY_FIELD_NUMBER: _ClassVar[int]
        BASH_ACCESS_VALID_UNTIL_FIELD_NUMBER: _ClassVar[int]
        SUDO_ACCESS_VALID_UNTIL_FIELD_NUMBER: _ClassVar[int]
        PASSWORD_FIELD_NUMBER: _ClassVar[int]
        IS_PASSWORD_SET_FIELD_NUMBER: _ClassVar[int]
        IS_SUDO_ACCESS_ENABLED_FIELD_NUMBER: _ClassVar[int]
        TOKEN_VERSION_FIELD_NUMBER: _ClassVar[int]
        LAST_PASSWORD_UPDATED_TIMESTAMP_SEC_FIELD_NUMBER: _ClassVar[int]
        IS_PASSWORD_CONVERTED_FIELD_NUMBER: _ClassVar[int]
        TWO_FA_MODE_FIELD_NUMBER: _ClassVar[int]
        DEPRECATED_TOTP_SECRET_KEY_FIELD_NUMBER: _ClassVar[int]
        DEPRECATED_TOTP_QR_CODE_URL_FIELD_NUMBER: _ClassVar[int]
        TWO_FA_EMAIL_ID_FIELD_NUMBER: _ClassVar[int]
        TOTP_SECRET_KEY_FIELD_NUMBER: _ClassVar[int]
        TOTP_QR_CODE_URL_FIELD_NUMBER: _ClassVar[int]
        IS_SUDO_ACCESS_LIFE_CYCLE_MIGRATED_FIELD_NUMBER: _ClassVar[int]
        SUDO_ACCESS_END_TIMESTAMP_MSECS_FIELD_NUMBER: _ClassVar[int]
        SUDO_ACCESS_MODE_FIELD_NUMBER: _ClassVar[int]
        CAN_TOKEN_BE_ENCRYPTED_IN_CLUSTER_CONFIG_FIELD_NUMBER: _ClassVar[int]
        CLUSTER_SSH_SUPPORT_USER_PUBLIC_KEY_FIELD_NUMBER: _ClassVar[int]
        SSH_ENCRYPTED_SUPPORT_USER_PRIVATE_KEY_FIELD_NUMBER: _ClassVar[int]
        CLUSTER_ACTIVE_SUPPORT_USER_SSH_PRIVATE_KEY_MD5SUM_FIELD_NUMBER: _ClassVar[int]
        CLUSTER_SUPPORT_USER_TARGET_ENC_SSH_PRIV_KEY_FIELD_NUMBER: _ClassVar[int]
        CLUSTER_SUPPORT_USER_TARGET_SSH_PUBLIC_KEY_FIELD_NUMBER: _ClassVar[int]
        token: str
        public_key: str
        bash_access_valid_until: int
        sudo_access_valid_until: int
        password: bytes
        is_password_set: bool
        is_sudo_access_enabled: bool
        token_version: ClusterConfigProto.supportTokenVersion
        last_password_updated_timestamp_sec: int
        is_password_converted: bool
        two_fa_mode: ClusterConfigProto.supportUser2FAMode
        deprecated_totp_secret_key: str
        deprecated_totp_qr_code_url: str
        two_fa_email_id: str
        totp_secret_key: bytes
        totp_qr_code_url: bytes
        is_sudo_access_life_cycle_migrated: bool
        sudo_access_end_timestamp_msecs: int
        sudo_access_mode: ClusterConfigProto.sudoAccessMode
        can_token_be_encrypted_in_cluster_config: bool
        cluster_ssh_support_user_public_key: str
        ssh_encrypted_support_user_private_key: bytes
        cluster_active_support_user_ssh_private_key_md5sum: str
        cluster_support_user_target_enc_ssh_priv_key: bytes
        cluster_support_user_target_ssh_public_key: str
        def __init__(self, token: _Optional[str] = ..., public_key: _Optional[str] = ..., bash_access_valid_until: _Optional[int] = ..., sudo_access_valid_until: _Optional[int] = ..., password: _Optional[bytes] = ..., is_password_set: bool = ..., is_sudo_access_enabled: bool = ..., token_version: _Optional[_Union[ClusterConfigProto.supportTokenVersion, str]] = ..., last_password_updated_timestamp_sec: _Optional[int] = ..., is_password_converted: bool = ..., two_fa_mode: _Optional[_Union[ClusterConfigProto.supportUser2FAMode, str]] = ..., deprecated_totp_secret_key: _Optional[str] = ..., deprecated_totp_qr_code_url: _Optional[str] = ..., two_fa_email_id: _Optional[str] = ..., totp_secret_key: _Optional[bytes] = ..., totp_qr_code_url: _Optional[bytes] = ..., is_sudo_access_life_cycle_migrated: bool = ..., sudo_access_end_timestamp_msecs: _Optional[int] = ..., sudo_access_mode: _Optional[_Union[ClusterConfigProto.sudoAccessMode, str]] = ..., can_token_be_encrypted_in_cluster_config: bool = ..., cluster_ssh_support_user_public_key: _Optional[str] = ..., ssh_encrypted_support_user_private_key: _Optional[bytes] = ..., cluster_active_support_user_ssh_private_key_md5sum: _Optional[str] = ..., cluster_support_user_target_enc_ssh_priv_key: _Optional[bytes] = ..., cluster_support_user_target_ssh_public_key: _Optional[str] = ...) -> None: ...
    class CloudBandwidthLimits(_message.Message):
        __slots__ = ("global_bw_limits",)
        GLOBAL_BW_LIMITS_FIELD_NUMBER: _ClassVar[int]
        global_bw_limits: ClusterConfigProto.BandwidthLimits
        def __init__(self, global_bw_limits: _Optional[_Union[ClusterConfigProto.BandwidthLimits, _Mapping]] = ...) -> None: ...
    class RigelConfig(_message.Message):
        __slots__ = ("control_plane_endpoint", "claim_token", "control_plane_data_endpoint", "data_plane_endpoint", "rigel_node_vec", "rt_server_endpoint", "tenant_id", "rigel_connection_id", "rigel_connector_group_id", "last_group_id_update_version", "use_case", "is_gcm_enabled", "deny_embedded_agent_cert", "dataplane_vip_vec")
        class UseCase(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kBaaS: _ClassVar[ClusterConfigProto.RigelConfig.UseCase]
            kDRaaSFailover: _ClassVar[ClusterConfigProto.RigelConfig.UseCase]
        kBaaS: ClusterConfigProto.RigelConfig.UseCase
        kDRaaSFailover: ClusterConfigProto.RigelConfig.UseCase
        class RigelConnectionStatus(_message.Message):
            __slots__ = ("is_connected", "last_connected_timestamp_msecs", "deprecated_error_message", "error_message_str")
            IS_CONNECTED_FIELD_NUMBER: _ClassVar[int]
            LAST_CONNECTED_TIMESTAMP_MSECS_FIELD_NUMBER: _ClassVar[int]
            DEPRECATED_ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
            ERROR_MESSAGE_STR_FIELD_NUMBER: _ClassVar[int]
            is_connected: bool
            last_connected_timestamp_msecs: int
            deprecated_error_message: int
            error_message_str: str
            def __init__(self, is_connected: bool = ..., last_connected_timestamp_msecs: _Optional[int] = ..., deprecated_error_message: _Optional[int] = ..., error_message_str: _Optional[str] = ...) -> None: ...
        class RigelNode(_message.Message):
            __slots__ = ("rigel_guid", "rigel_claim_status", "controlplane_connection_status", "dataplane_connection_status", "node_id")
            class RigelClaimInfo(_message.Message):
                __slots__ = ("status", "error_message")
                class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                    __slots__ = ()
                    kClaimNotDone: _ClassVar[ClusterConfigProto.RigelConfig.RigelNode.RigelClaimInfo.Status]
                    kClaimInProgress: _ClassVar[ClusterConfigProto.RigelConfig.RigelNode.RigelClaimInfo.Status]
                    kClaimSuccess: _ClassVar[ClusterConfigProto.RigelConfig.RigelNode.RigelClaimInfo.Status]
                    kClaimFailed: _ClassVar[ClusterConfigProto.RigelConfig.RigelNode.RigelClaimInfo.Status]
                kClaimNotDone: ClusterConfigProto.RigelConfig.RigelNode.RigelClaimInfo.Status
                kClaimInProgress: ClusterConfigProto.RigelConfig.RigelNode.RigelClaimInfo.Status
                kClaimSuccess: ClusterConfigProto.RigelConfig.RigelNode.RigelClaimInfo.Status
                kClaimFailed: ClusterConfigProto.RigelConfig.RigelNode.RigelClaimInfo.Status
                STATUS_FIELD_NUMBER: _ClassVar[int]
                ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
                status: ClusterConfigProto.RigelConfig.RigelNode.RigelClaimInfo.Status
                error_message: str
                def __init__(self, status: _Optional[_Union[ClusterConfigProto.RigelConfig.RigelNode.RigelClaimInfo.Status, str]] = ..., error_message: _Optional[str] = ...) -> None: ...
            RIGEL_GUID_FIELD_NUMBER: _ClassVar[int]
            RIGEL_CLAIM_STATUS_FIELD_NUMBER: _ClassVar[int]
            CONTROLPLANE_CONNECTION_STATUS_FIELD_NUMBER: _ClassVar[int]
            DATAPLANE_CONNECTION_STATUS_FIELD_NUMBER: _ClassVar[int]
            NODE_ID_FIELD_NUMBER: _ClassVar[int]
            rigel_guid: int
            rigel_claim_status: ClusterConfigProto.RigelConfig.RigelNode.RigelClaimInfo
            controlplane_connection_status: ClusterConfigProto.RigelConfig.RigelConnectionStatus
            dataplane_connection_status: ClusterConfigProto.RigelConfig.RigelConnectionStatus
            node_id: int
            def __init__(self, rigel_guid: _Optional[int] = ..., rigel_claim_status: _Optional[_Union[ClusterConfigProto.RigelConfig.RigelNode.RigelClaimInfo, _Mapping]] = ..., controlplane_connection_status: _Optional[_Union[ClusterConfigProto.RigelConfig.RigelConnectionStatus, _Mapping]] = ..., dataplane_connection_status: _Optional[_Union[ClusterConfigProto.RigelConfig.RigelConnectionStatus, _Mapping]] = ..., node_id: _Optional[int] = ...) -> None: ...
        class LastGroupIdUpdateVersion(_message.Message):
            __slots__ = ("version", "cluster_id")
            VERSION_FIELD_NUMBER: _ClassVar[int]
            CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
            version: int
            cluster_id: int
            def __init__(self, version: _Optional[int] = ..., cluster_id: _Optional[int] = ...) -> None: ...
        CONTROL_PLANE_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
        CLAIM_TOKEN_FIELD_NUMBER: _ClassVar[int]
        CONTROL_PLANE_DATA_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
        DATA_PLANE_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
        RIGEL_NODE_VEC_FIELD_NUMBER: _ClassVar[int]
        RT_SERVER_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
        TENANT_ID_FIELD_NUMBER: _ClassVar[int]
        RIGEL_CONNECTION_ID_FIELD_NUMBER: _ClassVar[int]
        RIGEL_CONNECTOR_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
        LAST_GROUP_ID_UPDATE_VERSION_FIELD_NUMBER: _ClassVar[int]
        USE_CASE_FIELD_NUMBER: _ClassVar[int]
        IS_GCM_ENABLED_FIELD_NUMBER: _ClassVar[int]
        DENY_EMBEDDED_AGENT_CERT_FIELD_NUMBER: _ClassVar[int]
        DATAPLANE_VIP_VEC_FIELD_NUMBER: _ClassVar[int]
        control_plane_endpoint: str
        claim_token: str
        control_plane_data_endpoint: str
        data_plane_endpoint: str
        rigel_node_vec: _containers.RepeatedCompositeFieldContainer[ClusterConfigProto.RigelConfig.RigelNode]
        rt_server_endpoint: str
        tenant_id: str
        rigel_connection_id: int
        rigel_connector_group_id: int
        last_group_id_update_version: ClusterConfigProto.RigelConfig.LastGroupIdUpdateVersion
        use_case: ClusterConfigProto.RigelConfig.UseCase
        is_gcm_enabled: bool
        deny_embedded_agent_cert: bool
        dataplane_vip_vec: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, control_plane_endpoint: _Optional[str] = ..., claim_token: _Optional[str] = ..., control_plane_data_endpoint: _Optional[str] = ..., data_plane_endpoint: _Optional[str] = ..., rigel_node_vec: _Optional[_Iterable[_Union[ClusterConfigProto.RigelConfig.RigelNode, _Mapping]]] = ..., rt_server_endpoint: _Optional[str] = ..., tenant_id: _Optional[str] = ..., rigel_connection_id: _Optional[int] = ..., rigel_connector_group_id: _Optional[int] = ..., last_group_id_update_version: _Optional[_Union[ClusterConfigProto.RigelConfig.LastGroupIdUpdateVersion, _Mapping]] = ..., use_case: _Optional[_Union[ClusterConfigProto.RigelConfig.UseCase, str]] = ..., is_gcm_enabled: bool = ..., deny_embedded_agent_cert: bool = ..., dataplane_vip_vec: _Optional[_Iterable[str]] = ...) -> None: ...
    class CloudNetworkParams(_message.Message):
        __slots__ = ("aws_network_params", "azure_network_params")
        class AWSNetworkParams(_message.Message):
            __slots__ = ("region", "vpc_id", "subnet_id", "security_group_id")
            REGION_FIELD_NUMBER: _ClassVar[int]
            VPC_ID_FIELD_NUMBER: _ClassVar[int]
            SUBNET_ID_FIELD_NUMBER: _ClassVar[int]
            SECURITY_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
            region: str
            vpc_id: str
            subnet_id: str
            security_group_id: str
            def __init__(self, region: _Optional[str] = ..., vpc_id: _Optional[str] = ..., subnet_id: _Optional[str] = ..., security_group_id: _Optional[str] = ...) -> None: ...
        class AzureNetworkParams(_message.Message):
            __slots__ = ("region", "vnet_name", "subnet_name", "application_security_group_name", "proximity_placement_group_name", "availability_set_name", "resource_group_name")
            REGION_FIELD_NUMBER: _ClassVar[int]
            VNET_NAME_FIELD_NUMBER: _ClassVar[int]
            SUBNET_NAME_FIELD_NUMBER: _ClassVar[int]
            APPLICATION_SECURITY_GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
            PROXIMITY_PLACEMENT_GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
            AVAILABILITY_SET_NAME_FIELD_NUMBER: _ClassVar[int]
            RESOURCE_GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
            region: str
            vnet_name: str
            subnet_name: str
            application_security_group_name: str
            proximity_placement_group_name: str
            availability_set_name: str
            resource_group_name: str
            def __init__(self, region: _Optional[str] = ..., vnet_name: _Optional[str] = ..., subnet_name: _Optional[str] = ..., application_security_group_name: _Optional[str] = ..., proximity_placement_group_name: _Optional[str] = ..., availability_set_name: _Optional[str] = ..., resource_group_name: _Optional[str] = ...) -> None: ...
        AWS_NETWORK_PARAMS_FIELD_NUMBER: _ClassVar[int]
        AZURE_NETWORK_PARAMS_FIELD_NUMBER: _ClassVar[int]
        aws_network_params: ClusterConfigProto.CloudNetworkParams.AWSNetworkParams
        azure_network_params: ClusterConfigProto.CloudNetworkParams.AzureNetworkParams
        def __init__(self, aws_network_params: _Optional[_Union[ClusterConfigProto.CloudNetworkParams.AWSNetworkParams, _Mapping]] = ..., azure_network_params: _Optional[_Union[ClusterConfigProto.CloudNetworkParams.AzureNetworkParams, _Mapping]] = ...) -> None: ...
    class CloudDataplaneInfo(_message.Message):
        __slots__ = ("aws_cloud_dataplane_info", "azure_cloud_dataplane_info", "cloud_network_params")
        class AWSCloudDataplaneInfo(_message.Message):
            __slots__ = ("iam_role",)
            IAM_ROLE_FIELD_NUMBER: _ClassVar[int]
            iam_role: str
            def __init__(self, iam_role: _Optional[str] = ...) -> None: ...
        class AzureCloudDataplaneInfo(_message.Message):
            __slots__ = ("client_id",)
            CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
            client_id: str
            def __init__(self, client_id: _Optional[str] = ...) -> None: ...
        AWS_CLOUD_DATAPLANE_INFO_FIELD_NUMBER: _ClassVar[int]
        AZURE_CLOUD_DATAPLANE_INFO_FIELD_NUMBER: _ClassVar[int]
        CLOUD_NETWORK_PARAMS_FIELD_NUMBER: _ClassVar[int]
        aws_cloud_dataplane_info: ClusterConfigProto.CloudDataplaneInfo.AWSCloudDataplaneInfo
        azure_cloud_dataplane_info: ClusterConfigProto.CloudDataplaneInfo.AzureCloudDataplaneInfo
        cloud_network_params: ClusterConfigProto.CloudNetworkParams
        def __init__(self, aws_cloud_dataplane_info: _Optional[_Union[ClusterConfigProto.CloudDataplaneInfo.AWSCloudDataplaneInfo, _Mapping]] = ..., azure_cloud_dataplane_info: _Optional[_Union[ClusterConfigProto.CloudDataplaneInfo.AzureCloudDataplaneInfo, _Mapping]] = ..., cloud_network_params: _Optional[_Union[ClusterConfigProto.CloudNetworkParams, _Mapping]] = ...) -> None: ...
    class AMQPTargetConfig(_message.Message):
        __slots__ = ("server_ip", "username", "password", "virtual_host", "exchange", "filer_id", "certificate")
        SERVER_IP_FIELD_NUMBER: _ClassVar[int]
        USERNAME_FIELD_NUMBER: _ClassVar[int]
        PASSWORD_FIELD_NUMBER: _ClassVar[int]
        VIRTUAL_HOST_FIELD_NUMBER: _ClassVar[int]
        EXCHANGE_FIELD_NUMBER: _ClassVar[int]
        FILER_ID_FIELD_NUMBER: _ClassVar[int]
        CERTIFICATE_FIELD_NUMBER: _ClassVar[int]
        server_ip: str
        username: str
        password: str
        virtual_host: str
        exchange: str
        filer_id: int
        certificate: str
        def __init__(self, server_ip: _Optional[str] = ..., username: _Optional[str] = ..., password: _Optional[str] = ..., virtual_host: _Optional[str] = ..., exchange: _Optional[str] = ..., filer_id: _Optional[int] = ..., certificate: _Optional[str] = ...) -> None: ...
    class NTPAuthKeyInfo(_message.Message):
        __slots__ = ("ntp_server_auth_key_id", "ntp_server_auth_key_value", "ntp_server")
        NTP_SERVER_AUTH_KEY_ID_FIELD_NUMBER: _ClassVar[int]
        NTP_SERVER_AUTH_KEY_VALUE_FIELD_NUMBER: _ClassVar[int]
        NTP_SERVER_FIELD_NUMBER: _ClassVar[int]
        ntp_server_auth_key_id: int
        ntp_server_auth_key_value: str
        ntp_server: str
        def __init__(self, ntp_server_auth_key_id: _Optional[int] = ..., ntp_server_auth_key_value: _Optional[str] = ..., ntp_server: _Optional[str] = ...) -> None: ...
    class KerberosConfig(_message.Message):
        __slots__ = ("kerberos_provider_map",)
        class KerberosProvider(_message.Message):
            __slots__ = ("kerberos_realm_name", "kerberos_admin_server", "kdc_server_vec", "tenant_id_vec", "ldap_provider_id", "id", "host_alias_vec")
            KERBEROS_REALM_NAME_FIELD_NUMBER: _ClassVar[int]
            KERBEROS_ADMIN_SERVER_FIELD_NUMBER: _ClassVar[int]
            KDC_SERVER_VEC_FIELD_NUMBER: _ClassVar[int]
            TENANT_ID_VEC_FIELD_NUMBER: _ClassVar[int]
            LDAP_PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
            ID_FIELD_NUMBER: _ClassVar[int]
            HOST_ALIAS_VEC_FIELD_NUMBER: _ClassVar[int]
            kerberos_realm_name: str
            kerberos_admin_server: str
            kdc_server_vec: _containers.RepeatedScalarFieldContainer[str]
            tenant_id_vec: _containers.RepeatedScalarFieldContainer[str]
            ldap_provider_id: int
            id: int
            host_alias_vec: _containers.RepeatedScalarFieldContainer[str]
            def __init__(self, kerberos_realm_name: _Optional[str] = ..., kerberos_admin_server: _Optional[str] = ..., kdc_server_vec: _Optional[_Iterable[str]] = ..., tenant_id_vec: _Optional[_Iterable[str]] = ..., ldap_provider_id: _Optional[int] = ..., id: _Optional[int] = ..., host_alias_vec: _Optional[_Iterable[str]] = ...) -> None: ...
        class KerberosProviderMapEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: ClusterConfigProto.KerberosConfig.KerberosProvider
            def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[ClusterConfigProto.KerberosConfig.KerberosProvider, _Mapping]] = ...) -> None: ...
        KERBEROS_PROVIDER_MAP_FIELD_NUMBER: _ClassVar[int]
        kerberos_provider_map: _containers.MessageMap[str, ClusterConfigProto.KerberosConfig.KerberosProvider]
        def __init__(self, kerberos_provider_map: _Optional[_Mapping[str, ClusterConfigProto.KerberosConfig.KerberosProvider]] = ...) -> None: ...
    class PureFlashbladeInfo(_message.Message):
        __slots__ = ("management_address", "api_token", "flashblade_id", "assigned_capacity_bytes", "is_dedicated_mode", "id", "assigned_data_vips_vec", "total_capacity_bytes", "software_version")
        MANAGEMENT_ADDRESS_FIELD_NUMBER: _ClassVar[int]
        API_TOKEN_FIELD_NUMBER: _ClassVar[int]
        FLASHBLADE_ID_FIELD_NUMBER: _ClassVar[int]
        ASSIGNED_CAPACITY_BYTES_FIELD_NUMBER: _ClassVar[int]
        IS_DEDICATED_MODE_FIELD_NUMBER: _ClassVar[int]
        ID_FIELD_NUMBER: _ClassVar[int]
        ASSIGNED_DATA_VIPS_VEC_FIELD_NUMBER: _ClassVar[int]
        TOTAL_CAPACITY_BYTES_FIELD_NUMBER: _ClassVar[int]
        SOFTWARE_VERSION_FIELD_NUMBER: _ClassVar[int]
        management_address: str
        api_token: str
        flashblade_id: str
        assigned_capacity_bytes: int
        is_dedicated_mode: bool
        id: int
        assigned_data_vips_vec: _containers.RepeatedScalarFieldContainer[str]
        total_capacity_bytes: int
        software_version: str
        def __init__(self, management_address: _Optional[str] = ..., api_token: _Optional[str] = ..., flashblade_id: _Optional[str] = ..., assigned_capacity_bytes: _Optional[int] = ..., is_dedicated_mode: bool = ..., id: _Optional[int] = ..., assigned_data_vips_vec: _Optional[_Iterable[str]] = ..., total_capacity_bytes: _Optional[int] = ..., software_version: _Optional[str] = ...) -> None: ...
    class SecurityConfig(_message.Message):
        __slots__ = ("password_strength", "password_reuse", "password_lifetime", "data_classification", "session_configuration", "certificate_based_auth", "account_lockout", "access_token_validity_mins", "ui_inactivity_timeout_msecs")
        class PasswordStrength(_message.Message):
            __slots__ = ("min_length", "include_upper_letter", "include_lower_letter", "include_number", "include_special_char")
            MIN_LENGTH_FIELD_NUMBER: _ClassVar[int]
            INCLUDE_UPPER_LETTER_FIELD_NUMBER: _ClassVar[int]
            INCLUDE_LOWER_LETTER_FIELD_NUMBER: _ClassVar[int]
            INCLUDE_NUMBER_FIELD_NUMBER: _ClassVar[int]
            INCLUDE_SPECIAL_CHAR_FIELD_NUMBER: _ClassVar[int]
            min_length: int
            include_upper_letter: bool
            include_lower_letter: bool
            include_number: bool
            include_special_char: bool
            def __init__(self, min_length: _Optional[int] = ..., include_upper_letter: bool = ..., include_lower_letter: bool = ..., include_number: bool = ..., include_special_char: bool = ...) -> None: ...
        class PasswordReuse(_message.Message):
            __slots__ = ("num_disallowed_old_passwords", "num_different_chars")
            NUM_DISALLOWED_OLD_PASSWORDS_FIELD_NUMBER: _ClassVar[int]
            NUM_DIFFERENT_CHARS_FIELD_NUMBER: _ClassVar[int]
            num_disallowed_old_passwords: int
            num_different_chars: int
            def __init__(self, num_disallowed_old_passwords: _Optional[int] = ..., num_different_chars: _Optional[int] = ...) -> None: ...
        class PasswordLifetime(_message.Message):
            __slots__ = ("min_lifetime_days", "max_lifetime_days")
            MIN_LIFETIME_DAYS_FIELD_NUMBER: _ClassVar[int]
            MAX_LIFETIME_DAYS_FIELD_NUMBER: _ClassVar[int]
            min_lifetime_days: int
            max_lifetime_days: int
            def __init__(self, min_lifetime_days: _Optional[int] = ..., max_lifetime_days: _Optional[int] = ...) -> None: ...
        class AccountLockout(_message.Message):
            __slots__ = ("max_failed_login_attempts", "failed_login_lock_time_duration_mins", "inactivity_time_days")
            MAX_FAILED_LOGIN_ATTEMPTS_FIELD_NUMBER: _ClassVar[int]
            FAILED_LOGIN_LOCK_TIME_DURATION_MINS_FIELD_NUMBER: _ClassVar[int]
            INACTIVITY_TIME_DAYS_FIELD_NUMBER: _ClassVar[int]
            max_failed_login_attempts: int
            failed_login_lock_time_duration_mins: int
            inactivity_time_days: int
            def __init__(self, max_failed_login_attempts: _Optional[int] = ..., failed_login_lock_time_duration_mins: _Optional[int] = ..., inactivity_time_days: _Optional[int] = ...) -> None: ...
        class DataClassification(_message.Message):
            __slots__ = ("is_data_classified", "classified_data_message", "unclassified_data_message")
            IS_DATA_CLASSIFIED_FIELD_NUMBER: _ClassVar[int]
            CLASSIFIED_DATA_MESSAGE_FIELD_NUMBER: _ClassVar[int]
            UNCLASSIFIED_DATA_MESSAGE_FIELD_NUMBER: _ClassVar[int]
            is_data_classified: bool
            classified_data_message: str
            unclassified_data_message: str
            def __init__(self, is_data_classified: bool = ..., classified_data_message: _Optional[str] = ..., unclassified_data_message: _Optional[str] = ...) -> None: ...
        class SessionConfiguration(_message.Message):
            __slots__ = ("absolute_timeout", "inactivity_timeout", "limit_sessions", "sessions_per_user", "system_wide_sessions")
            ABSOLUTE_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
            INACTIVITY_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
            LIMIT_SESSIONS_FIELD_NUMBER: _ClassVar[int]
            SESSIONS_PER_USER_FIELD_NUMBER: _ClassVar[int]
            SYSTEM_WIDE_SESSIONS_FIELD_NUMBER: _ClassVar[int]
            absolute_timeout: int
            inactivity_timeout: int
            limit_sessions: bool
            sessions_per_user: int
            system_wide_sessions: int
            def __init__(self, absolute_timeout: _Optional[int] = ..., inactivity_timeout: _Optional[int] = ..., limit_sessions: bool = ..., sessions_per_user: _Optional[int] = ..., system_wide_sessions: _Optional[int] = ...) -> None: ...
        class CertificateBasedAuth(_message.Message):
            __slots__ = ("enable_mapping_based_authentication", "certificate_mapping", "ad_mapping")
            class MappingFields(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                commonName: _ClassVar[ClusterConfigProto.SecurityConfig.CertificateBasedAuth.MappingFields]
                emailAddress: _ClassVar[ClusterConfigProto.SecurityConfig.CertificateBasedAuth.MappingFields]
                userPrincipalName: _ClassVar[ClusterConfigProto.SecurityConfig.CertificateBasedAuth.MappingFields]
                samAccountName: _ClassVar[ClusterConfigProto.SecurityConfig.CertificateBasedAuth.MappingFields]
            commonName: ClusterConfigProto.SecurityConfig.CertificateBasedAuth.MappingFields
            emailAddress: ClusterConfigProto.SecurityConfig.CertificateBasedAuth.MappingFields
            userPrincipalName: ClusterConfigProto.SecurityConfig.CertificateBasedAuth.MappingFields
            samAccountName: ClusterConfigProto.SecurityConfig.CertificateBasedAuth.MappingFields
            ENABLE_MAPPING_BASED_AUTHENTICATION_FIELD_NUMBER: _ClassVar[int]
            CERTIFICATE_MAPPING_FIELD_NUMBER: _ClassVar[int]
            AD_MAPPING_FIELD_NUMBER: _ClassVar[int]
            enable_mapping_based_authentication: bool
            certificate_mapping: ClusterConfigProto.SecurityConfig.CertificateBasedAuth.MappingFields
            ad_mapping: ClusterConfigProto.SecurityConfig.CertificateBasedAuth.MappingFields
            def __init__(self, enable_mapping_based_authentication: bool = ..., certificate_mapping: _Optional[_Union[ClusterConfigProto.SecurityConfig.CertificateBasedAuth.MappingFields, str]] = ..., ad_mapping: _Optional[_Union[ClusterConfigProto.SecurityConfig.CertificateBasedAuth.MappingFields, str]] = ...) -> None: ...
        PASSWORD_STRENGTH_FIELD_NUMBER: _ClassVar[int]
        PASSWORD_REUSE_FIELD_NUMBER: _ClassVar[int]
        PASSWORD_LIFETIME_FIELD_NUMBER: _ClassVar[int]
        DATA_CLASSIFICATION_FIELD_NUMBER: _ClassVar[int]
        SESSION_CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
        CERTIFICATE_BASED_AUTH_FIELD_NUMBER: _ClassVar[int]
        ACCOUNT_LOCKOUT_FIELD_NUMBER: _ClassVar[int]
        ACCESS_TOKEN_VALIDITY_MINS_FIELD_NUMBER: _ClassVar[int]
        UI_INACTIVITY_TIMEOUT_MSECS_FIELD_NUMBER: _ClassVar[int]
        password_strength: ClusterConfigProto.SecurityConfig.PasswordStrength
        password_reuse: ClusterConfigProto.SecurityConfig.PasswordReuse
        password_lifetime: ClusterConfigProto.SecurityConfig.PasswordLifetime
        data_classification: ClusterConfigProto.SecurityConfig.DataClassification
        session_configuration: ClusterConfigProto.SecurityConfig.SessionConfiguration
        certificate_based_auth: ClusterConfigProto.SecurityConfig.CertificateBasedAuth
        account_lockout: ClusterConfigProto.SecurityConfig.AccountLockout
        access_token_validity_mins: int
        ui_inactivity_timeout_msecs: int
        def __init__(self, password_strength: _Optional[_Union[ClusterConfigProto.SecurityConfig.PasswordStrength, _Mapping]] = ..., password_reuse: _Optional[_Union[ClusterConfigProto.SecurityConfig.PasswordReuse, _Mapping]] = ..., password_lifetime: _Optional[_Union[ClusterConfigProto.SecurityConfig.PasswordLifetime, _Mapping]] = ..., data_classification: _Optional[_Union[ClusterConfigProto.SecurityConfig.DataClassification, _Mapping]] = ..., session_configuration: _Optional[_Union[ClusterConfigProto.SecurityConfig.SessionConfiguration, _Mapping]] = ..., certificate_based_auth: _Optional[_Union[ClusterConfigProto.SecurityConfig.CertificateBasedAuth, _Mapping]] = ..., account_lockout: _Optional[_Union[ClusterConfigProto.SecurityConfig.AccountLockout, _Mapping]] = ..., access_token_validity_mins: _Optional[int] = ..., ui_inactivity_timeout_msecs: _Optional[int] = ...) -> None: ...
    class NodeAccess(_message.Message):
        __slots__ = ("tsh_access_enabled", "ssh_access_enabled", "end_timestamp_msecs", "opaque_data", "ssh_port", "secure_shell_enabled", "secure_shell_disabled_until_msecs")
        TSH_ACCESS_ENABLED_FIELD_NUMBER: _ClassVar[int]
        SSH_ACCESS_ENABLED_FIELD_NUMBER: _ClassVar[int]
        END_TIMESTAMP_MSECS_FIELD_NUMBER: _ClassVar[int]
        OPAQUE_DATA_FIELD_NUMBER: _ClassVar[int]
        SSH_PORT_FIELD_NUMBER: _ClassVar[int]
        SECURE_SHELL_ENABLED_FIELD_NUMBER: _ClassVar[int]
        SECURE_SHELL_DISABLED_UNTIL_MSECS_FIELD_NUMBER: _ClassVar[int]
        tsh_access_enabled: bool
        ssh_access_enabled: bool
        end_timestamp_msecs: int
        opaque_data: str
        ssh_port: int
        secure_shell_enabled: bool
        secure_shell_disabled_until_msecs: int
        def __init__(self, tsh_access_enabled: bool = ..., ssh_access_enabled: bool = ..., end_timestamp_msecs: _Optional[int] = ..., opaque_data: _Optional[str] = ..., ssh_port: _Optional[int] = ..., secure_shell_enabled: bool = ..., secure_shell_disabled_until_msecs: _Optional[int] = ...) -> None: ...
    class RootCertifyingAuthority(_message.Message):
        __slots__ = ("root_certificate", "encrypted_root_key", "root_ca_id")
        ROOT_CERTIFICATE_FIELD_NUMBER: _ClassVar[int]
        ENCRYPTED_ROOT_KEY_FIELD_NUMBER: _ClassVar[int]
        ROOT_CA_ID_FIELD_NUMBER: _ClassVar[int]
        root_certificate: bytes
        encrypted_root_key: bytes
        root_ca_id: int
        def __init__(self, root_certificate: _Optional[bytes] = ..., encrypted_root_key: _Optional[bytes] = ..., root_ca_id: _Optional[int] = ...) -> None: ...
    class RootUser(_message.Message):
        __slots__ = ("password", "is_password_set", "is_password_converted")
        PASSWORD_FIELD_NUMBER: _ClassVar[int]
        IS_PASSWORD_SET_FIELD_NUMBER: _ClassVar[int]
        IS_PASSWORD_CONVERTED_FIELD_NUMBER: _ClassVar[int]
        password: bytes
        is_password_set: bool
        is_password_converted: bool
        def __init__(self, password: _Optional[bytes] = ..., is_password_set: bool = ..., is_password_converted: bool = ...) -> None: ...
    class CertifyingAuthorityToIdMap(_message.Message):
        __slots__ = ("ca_hash_key", "ca_id_value")
        CA_HASH_KEY_FIELD_NUMBER: _ClassVar[int]
        CA_ID_VALUE_FIELD_NUMBER: _ClassVar[int]
        ca_hash_key: str
        ca_id_value: int
        def __init__(self, ca_hash_key: _Optional[str] = ..., ca_id_value: _Optional[int] = ...) -> None: ...
    class HeliosOnpremConfig(_message.Message):
        __slots__ = ("kubernetes_config",)
        class KubernetesConfig(_message.Message):
            __slots__ = ("kubernetes_subnet_cidr", "pod_subnet_cidr", "service_subnet_cidr")
            KUBERNETES_SUBNET_CIDR_FIELD_NUMBER: _ClassVar[int]
            POD_SUBNET_CIDR_FIELD_NUMBER: _ClassVar[int]
            SERVICE_SUBNET_CIDR_FIELD_NUMBER: _ClassVar[int]
            kubernetes_subnet_cidr: str
            pod_subnet_cidr: str
            service_subnet_cidr: str
            def __init__(self, kubernetes_subnet_cidr: _Optional[str] = ..., pod_subnet_cidr: _Optional[str] = ..., service_subnet_cidr: _Optional[str] = ...) -> None: ...
        KUBERNETES_CONFIG_FIELD_NUMBER: _ClassVar[int]
        kubernetes_config: ClusterConfigProto.HeliosOnpremConfig.KubernetesConfig
        def __init__(self, kubernetes_config: _Optional[_Union[ClusterConfigProto.HeliosOnpremConfig.KubernetesConfig, _Mapping]] = ...) -> None: ...
    class OperationState(_message.Message):
        __slots__ = ("id", "type", "status", "percentage_completion", "time_remaining_seconds", "events", "nodesOperationStatus")
        class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kCreate: _ClassVar[ClusterConfigProto.OperationState.Type]
            kDestroy: _ClassVar[ClusterConfigProto.OperationState.Type]
            kNodeAddition: _ClassVar[ClusterConfigProto.OperationState.Type]
            kUpgrade: _ClassVar[ClusterConfigProto.OperationState.Type]
            kUploadPackageByUrl: _ClassVar[ClusterConfigProto.OperationState.Type]
            kUploadPackageAndUpgrade: _ClassVar[ClusterConfigProto.OperationState.Type]
            kNodeRemoval: _ClassVar[ClusterConfigProto.OperationState.Type]
            kPackageRemoval: _ClassVar[ClusterConfigProto.OperationState.Type]
        kCreate: ClusterConfigProto.OperationState.Type
        kDestroy: ClusterConfigProto.OperationState.Type
        kNodeAddition: ClusterConfigProto.OperationState.Type
        kUpgrade: ClusterConfigProto.OperationState.Type
        kUploadPackageByUrl: ClusterConfigProto.OperationState.Type
        kUploadPackageAndUpgrade: ClusterConfigProto.OperationState.Type
        kNodeRemoval: ClusterConfigProto.OperationState.Type
        kPackageRemoval: ClusterConfigProto.OperationState.Type
        class OperationStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kSuccess: _ClassVar[ClusterConfigProto.OperationState.OperationStatus]
            kFailed: _ClassVar[ClusterConfigProto.OperationState.OperationStatus]
            kInProgress: _ClassVar[ClusterConfigProto.OperationState.OperationStatus]
        kSuccess: ClusterConfigProto.OperationState.OperationStatus
        kFailed: ClusterConfigProto.OperationState.OperationStatus
        kInProgress: ClusterConfigProto.OperationState.OperationStatus
        class Event(_message.Message):
            __slots__ = ("severity", "message", "timestamp")
            class Severity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                kInfo: _ClassVar[ClusterConfigProto.OperationState.Event.Severity]
                kWarning: _ClassVar[ClusterConfigProto.OperationState.Event.Severity]
                kError: _ClassVar[ClusterConfigProto.OperationState.Event.Severity]
            kInfo: ClusterConfigProto.OperationState.Event.Severity
            kWarning: ClusterConfigProto.OperationState.Event.Severity
            kError: ClusterConfigProto.OperationState.Event.Severity
            SEVERITY_FIELD_NUMBER: _ClassVar[int]
            MESSAGE_FIELD_NUMBER: _ClassVar[int]
            TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
            severity: ClusterConfigProto.OperationState.Event.Severity
            message: str
            timestamp: int
            def __init__(self, severity: _Optional[_Union[ClusterConfigProto.OperationState.Event.Severity, str]] = ..., message: _Optional[str] = ..., timestamp: _Optional[int] = ...) -> None: ...
        class NodeOperationStatus(_message.Message):
            __slots__ = ("id", "ip", "percentage_completion", "time_remaining_seconds", "status", "events")
            ID_FIELD_NUMBER: _ClassVar[int]
            IP_FIELD_NUMBER: _ClassVar[int]
            PERCENTAGE_COMPLETION_FIELD_NUMBER: _ClassVar[int]
            TIME_REMAINING_SECONDS_FIELD_NUMBER: _ClassVar[int]
            STATUS_FIELD_NUMBER: _ClassVar[int]
            EVENTS_FIELD_NUMBER: _ClassVar[int]
            id: int
            ip: str
            percentage_completion: int
            time_remaining_seconds: int
            status: ClusterConfigProto.OperationState.OperationStatus
            events: _containers.RepeatedCompositeFieldContainer[ClusterConfigProto.OperationState.Event]
            def __init__(self, id: _Optional[int] = ..., ip: _Optional[str] = ..., percentage_completion: _Optional[int] = ..., time_remaining_seconds: _Optional[int] = ..., status: _Optional[_Union[ClusterConfigProto.OperationState.OperationStatus, str]] = ..., events: _Optional[_Iterable[_Union[ClusterConfigProto.OperationState.Event, _Mapping]]] = ...) -> None: ...
        ID_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        PERCENTAGE_COMPLETION_FIELD_NUMBER: _ClassVar[int]
        TIME_REMAINING_SECONDS_FIELD_NUMBER: _ClassVar[int]
        EVENTS_FIELD_NUMBER: _ClassVar[int]
        NODESOPERATIONSTATUS_FIELD_NUMBER: _ClassVar[int]
        id: str
        type: ClusterConfigProto.OperationState.Type
        status: ClusterConfigProto.OperationState.OperationStatus
        percentage_completion: int
        time_remaining_seconds: int
        events: _containers.RepeatedCompositeFieldContainer[ClusterConfigProto.OperationState.Event]
        nodesOperationStatus: _containers.RepeatedCompositeFieldContainer[ClusterConfigProto.OperationState.NodeOperationStatus]
        def __init__(self, id: _Optional[str] = ..., type: _Optional[_Union[ClusterConfigProto.OperationState.Type, str]] = ..., status: _Optional[_Union[ClusterConfigProto.OperationState.OperationStatus, str]] = ..., percentage_completion: _Optional[int] = ..., time_remaining_seconds: _Optional[int] = ..., events: _Optional[_Iterable[_Union[ClusterConfigProto.OperationState.Event, _Mapping]]] = ..., nodesOperationStatus: _Optional[_Iterable[_Union[ClusterConfigProto.OperationState.NodeOperationStatus, _Mapping]]] = ...) -> None: ...
    class OperationStateMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: ClusterConfigProto.OperationState
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[ClusterConfigProto.OperationState, _Mapping]] = ...) -> None: ...
    class ApolloBinaryLoggingConfig(_message.Message):
        __slots__ = ("view_box_name", "view_name")
        VIEW_BOX_NAME_FIELD_NUMBER: _ClassVar[int]
        VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
        view_box_name: str
        view_name: str
        def __init__(self, view_box_name: _Optional[str] = ..., view_name: _Optional[str] = ...) -> None: ...
    class AirgapConfig(_message.Message):
        __slots__ = ("airgap_status", "exception_port_and_ip", "exception_profiles")
        class AirgapStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kDisable: _ClassVar[ClusterConfigProto.AirgapConfig.AirgapStatus]
            kEnable: _ClassVar[ClusterConfigProto.AirgapConfig.AirgapStatus]
        kDisable: ClusterConfigProto.AirgapConfig.AirgapStatus
        kEnable: ClusterConfigProto.AirgapConfig.AirgapStatus
        class AirgapPortAndIpConfig(_message.Message):
            __slots__ = ("exception_port", "exception_ip_address")
            EXCEPTION_PORT_FIELD_NUMBER: _ClassVar[int]
            EXCEPTION_IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
            exception_port: str
            exception_ip_address: str
            def __init__(self, exception_port: _Optional[str] = ..., exception_ip_address: _Optional[str] = ...) -> None: ...
        AIRGAP_STATUS_FIELD_NUMBER: _ClassVar[int]
        EXCEPTION_PORT_AND_IP_FIELD_NUMBER: _ClassVar[int]
        EXCEPTION_PROFILES_FIELD_NUMBER: _ClassVar[int]
        airgap_status: ClusterConfigProto.AirgapConfig.AirgapStatus
        exception_port_and_ip: _containers.RepeatedCompositeFieldContainer[ClusterConfigProto.AirgapConfig.AirgapPortAndIpConfig]
        exception_profiles: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, airgap_status: _Optional[_Union[ClusterConfigProto.AirgapConfig.AirgapStatus, str]] = ..., exception_port_and_ip: _Optional[_Iterable[_Union[ClusterConfigProto.AirgapConfig.AirgapPortAndIpConfig, _Mapping]]] = ..., exception_profiles: _Optional[_Iterable[str]] = ...) -> None: ...
    class SshConfig(_message.Message):
        __slots__ = ("timeout_in_mins",)
        TIMEOUT_IN_MINS_FIELD_NUMBER: _ClassVar[int]
        timeout_in_mins: int
        def __init__(self, timeout_in_mins: _Optional[int] = ...) -> None: ...
    class ServiceIdentity(_message.Message):
        __slots__ = ("global_enabled", "disabled_ports_vec", "have_all_nodes_upgraded_to_supported_release")
        GLOBAL_ENABLED_FIELD_NUMBER: _ClassVar[int]
        DISABLED_PORTS_VEC_FIELD_NUMBER: _ClassVar[int]
        HAVE_ALL_NODES_UPGRADED_TO_SUPPORTED_RELEASE_FIELD_NUMBER: _ClassVar[int]
        global_enabled: bool
        disabled_ports_vec: _containers.RepeatedScalarFieldContainer[int]
        have_all_nodes_upgraded_to_supported_release: bool
        def __init__(self, global_enabled: bool = ..., disabled_ports_vec: _Optional[_Iterable[int]] = ..., have_all_nodes_upgraded_to_supported_release: bool = ...) -> None: ...
    class ClusterAESEncryption(_message.Message):
        __slots__ = ("encryption_mode", "encryption_mode_change_timestamp_msecs", "max_supported_encryption_mode")
        ENCRYPTION_MODE_FIELD_NUMBER: _ClassVar[int]
        ENCRYPTION_MODE_CHANGE_TIMESTAMP_MSECS_FIELD_NUMBER: _ClassVar[int]
        MAX_SUPPORTED_ENCRYPTION_MODE_FIELD_NUMBER: _ClassVar[int]
        encryption_mode: _aes_encryptor_pb2.AESEncryptorMode
        encryption_mode_change_timestamp_msecs: int
        max_supported_encryption_mode: int
        def __init__(self, encryption_mode: _Optional[_Union[_aes_encryptor_pb2.AESEncryptorMode, str]] = ..., encryption_mode_change_timestamp_msecs: _Optional[int] = ..., max_supported_encryption_mode: _Optional[int] = ...) -> None: ...
    class AbacConfig(_message.Message):
        __slots__ = ("abac_server_map",)
        class AbacServer(_message.Message):
            __slots__ = ("id", "host", "port", "certificate", "key", "ca_certificate_store", "base_path")
            ID_FIELD_NUMBER: _ClassVar[int]
            HOST_FIELD_NUMBER: _ClassVar[int]
            PORT_FIELD_NUMBER: _ClassVar[int]
            CERTIFICATE_FIELD_NUMBER: _ClassVar[int]
            KEY_FIELD_NUMBER: _ClassVar[int]
            CA_CERTIFICATE_STORE_FIELD_NUMBER: _ClassVar[int]
            BASE_PATH_FIELD_NUMBER: _ClassVar[int]
            id: int
            host: str
            port: int
            certificate: str
            key: bytes
            ca_certificate_store: str
            base_path: str
            def __init__(self, id: _Optional[int] = ..., host: _Optional[str] = ..., port: _Optional[int] = ..., certificate: _Optional[str] = ..., key: _Optional[bytes] = ..., ca_certificate_store: _Optional[str] = ..., base_path: _Optional[str] = ...) -> None: ...
        class AbacServerMapEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: ClusterConfigProto.AbacConfig.AbacServer
            def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[ClusterConfigProto.AbacConfig.AbacServer, _Mapping]] = ...) -> None: ...
        ABAC_SERVER_MAP_FIELD_NUMBER: _ClassVar[int]
        abac_server_map: _containers.MessageMap[str, ClusterConfigProto.AbacConfig.AbacServer]
        def __init__(self, abac_server_map: _Optional[_Mapping[str, ClusterConfigProto.AbacConfig.AbacServer]] = ...) -> None: ...
    class CohesionConfig(_message.Message):
        __slots__ = ("activation_string", "client_certificate", "encrypted_private_key", "appliance_id", "sqs_queue_url", "storage_endpoint_url")
        ACTIVATION_STRING_FIELD_NUMBER: _ClassVar[int]
        CLIENT_CERTIFICATE_FIELD_NUMBER: _ClassVar[int]
        ENCRYPTED_PRIVATE_KEY_FIELD_NUMBER: _ClassVar[int]
        APPLIANCE_ID_FIELD_NUMBER: _ClassVar[int]
        SQS_QUEUE_URL_FIELD_NUMBER: _ClassVar[int]
        STORAGE_ENDPOINT_URL_FIELD_NUMBER: _ClassVar[int]
        activation_string: str
        client_certificate: bytes
        encrypted_private_key: bytes
        appliance_id: str
        sqs_queue_url: str
        storage_endpoint_url: str
        def __init__(self, activation_string: _Optional[str] = ..., client_certificate: _Optional[bytes] = ..., encrypted_private_key: _Optional[bytes] = ..., appliance_id: _Optional[str] = ..., sqs_queue_url: _Optional[str] = ..., storage_endpoint_url: _Optional[str] = ...) -> None: ...
    class ClusterSnapshotPolicy(_message.Message):
        __slots__ = ("schedule_policy", "retention_policy")
        SCHEDULE_POLICY_FIELD_NUMBER: _ClassVar[int]
        RETENTION_POLICY_FIELD_NUMBER: _ClassVar[int]
        schedule_policy: ClusterConfigProto.SchedulePolicy
        retention_policy: ClusterConfigProto.RetentionPolicy
        def __init__(self, schedule_policy: _Optional[_Union[ClusterConfigProto.SchedulePolicy, _Mapping]] = ..., retention_policy: _Optional[_Union[ClusterConfigProto.RetentionPolicy, _Mapping]] = ...) -> None: ...
    class SchedulePolicy(_message.Message):
        __slots__ = ("day_of_week_vec", "day_of_month_vec", "hour", "minute", "timezone", "suspended")
        class DayOfWeek(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kSunday: _ClassVar[ClusterConfigProto.SchedulePolicy.DayOfWeek]
            kMonday: _ClassVar[ClusterConfigProto.SchedulePolicy.DayOfWeek]
            kTuesday: _ClassVar[ClusterConfigProto.SchedulePolicy.DayOfWeek]
            kWednesday: _ClassVar[ClusterConfigProto.SchedulePolicy.DayOfWeek]
            kThursday: _ClassVar[ClusterConfigProto.SchedulePolicy.DayOfWeek]
            kFriday: _ClassVar[ClusterConfigProto.SchedulePolicy.DayOfWeek]
            kSaturday: _ClassVar[ClusterConfigProto.SchedulePolicy.DayOfWeek]
        kSunday: ClusterConfigProto.SchedulePolicy.DayOfWeek
        kMonday: ClusterConfigProto.SchedulePolicy.DayOfWeek
        kTuesday: ClusterConfigProto.SchedulePolicy.DayOfWeek
        kWednesday: ClusterConfigProto.SchedulePolicy.DayOfWeek
        kThursday: ClusterConfigProto.SchedulePolicy.DayOfWeek
        kFriday: ClusterConfigProto.SchedulePolicy.DayOfWeek
        kSaturday: ClusterConfigProto.SchedulePolicy.DayOfWeek
        DAY_OF_WEEK_VEC_FIELD_NUMBER: _ClassVar[int]
        DAY_OF_MONTH_VEC_FIELD_NUMBER: _ClassVar[int]
        HOUR_FIELD_NUMBER: _ClassVar[int]
        MINUTE_FIELD_NUMBER: _ClassVar[int]
        TIMEZONE_FIELD_NUMBER: _ClassVar[int]
        SUSPENDED_FIELD_NUMBER: _ClassVar[int]
        day_of_week_vec: _containers.RepeatedScalarFieldContainer[ClusterConfigProto.SchedulePolicy.DayOfWeek]
        day_of_month_vec: _containers.RepeatedScalarFieldContainer[int]
        hour: int
        minute: int
        timezone: str
        suspended: bool
        def __init__(self, day_of_week_vec: _Optional[_Iterable[_Union[ClusterConfigProto.SchedulePolicy.DayOfWeek, str]]] = ..., day_of_month_vec: _Optional[_Iterable[int]] = ..., hour: _Optional[int] = ..., minute: _Optional[int] = ..., timezone: _Optional[str] = ..., suspended: bool = ...) -> None: ...
    class RetentionPolicy(_message.Message):
        __slots__ = ("num_days_to_keep", "num_versions_to_keep", "suspended")
        NUM_DAYS_TO_KEEP_FIELD_NUMBER: _ClassVar[int]
        NUM_VERSIONS_TO_KEEP_FIELD_NUMBER: _ClassVar[int]
        SUSPENDED_FIELD_NUMBER: _ClassVar[int]
        num_days_to_keep: int
        num_versions_to_keep: int
        suspended: bool
        def __init__(self, num_days_to_keep: _Optional[int] = ..., num_versions_to_keep: _Optional[int] = ..., suspended: bool = ...) -> None: ...
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_NAME_FIELD_NUMBER: _ClassVar[int]
    DEPRECATED_SUBNET_FIELD_NUMBER: _ClassVar[int]
    INTERNAL_SUBNET_FIELD_NUMBER: _ClassVar[int]
    CLIENT_SUBNET_WHITELIST_FIELD_NUMBER: _ClassVar[int]
    STORAGE_TIER_VEC_FIELD_NUMBER: _ClassVar[int]
    SCRIBE_STORAGE_TIER_VEC_FIELD_NUMBER: _ClassVar[int]
    SEQUENTIAL_IO_PREFERENCE_INDEX_FIELD_NUMBER: _ClassVar[int]
    SEQUENTIAL_STORAGE_TIER_VEC_FIELD_NUMBER: _ClassVar[int]
    RANDOM_STORAGE_TIER_VEC_FIELD_NUMBER: _ClassVar[int]
    TIER_SHUFFLE_THRESHOLD_PCT_FIELD_NUMBER: _ClassVar[int]
    MIN_TIER_SHUFFLE_UTIL_PCT_FIELD_NUMBER: _ClassVar[int]
    DISK_VEC_FIELD_NUMBER: _ClassVar[int]
    RACK_VEC_FIELD_NUMBER: _ClassVar[int]
    CHASSIS_VEC_FIELD_NUMBER: _ClassVar[int]
    NODE_VEC_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_PARTITION_VEC_FIELD_NUMBER: _ClassVar[int]
    VIEW_BOX_VEC_FIELD_NUMBER: _ClassVar[int]
    BULLETIN_BOARD_FIELD_NUMBER: _ClassVar[int]
    SCRIBE_TABLE_NAMES_FIELD_NUMBER: _ClassVar[int]
    NTP_SERVER_VEC_FIELD_NUMBER: _ClassVar[int]
    NTP_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    BONDING_MODE_FIELD_NUMBER: _ClassVar[int]
    SMTP_SERVER_FIELD_NUMBER: _ClassVar[int]
    SUPPORT_SERVER_FIELD_NUMBER: _ClassVar[int]
    SUPPORT_SERVER_V2_FIELD_NUMBER: _ClassVar[int]
    SUPPORT_SERVER_V2_CONFIG_FIELD_NUMBER: _ClassVar[int]
    APOLLO_STORAGE_TIER_INDEX_FIELD_NUMBER: _ClassVar[int]
    APOLLO_STORAGE_TIER_VEC_FIELD_NUMBER: _ClassVar[int]
    APOLLO_WAL_STORAGE_TIER_INDEX_FIELD_NUMBER: _ClassVar[int]
    APOLLO_WAL_STORAGE_TIER_VEC_FIELD_NUMBER: _ClassVar[int]
    YODA_STORAGE_TIER_VEC_FIELD_NUMBER: _ClassVar[int]
    HYDRA_STORAGE_TIER_VEC_FIELD_NUMBER: _ClassVar[int]
    HYDRA_DOWNTIER_STORAGE_TIER_VEC_FIELD_NUMBER: _ClassVar[int]
    LIBRARIAN_STORAGE_TIER_VEC_FIELD_NUMBER: _ClassVar[int]
    GROOT_STORAGE_TIER_INDEX_FIELD_NUMBER: _ClassVar[int]
    GROOT_STORAGE_TIER_VEC_FIELD_NUMBER: _ClassVar[int]
    ATHENA_STORAGE_TIER_VEC_FIELD_NUMBER: _ClassVar[int]
    ATHENA_SLOWER_STORAGE_TIER_VEC_FIELD_NUMBER: _ClassVar[int]
    EAGLE_AGENT_STORAGE_TIER_VEC_FIELD_NUMBER: _ClassVar[int]
    CLOUD_CHUNK_REPO_STORAGE_TIER_VEC_FIELD_NUMBER: _ClassVar[int]
    ALERT_NOTIFICATION_EMAIL_LIST_FIELD_NUMBER: _ClassVar[int]
    IPMI_CONFIG_FIELD_NUMBER: _ClassVar[int]
    NFS_EXPORT_PATH_LIST_FIELD_NUMBER: _ClassVar[int]
    HALO_CONFIG_FIELD_NUMBER: _ClassVar[int]
    EAGLE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    KMS_SERVER_VEC_FIELD_NUMBER: _ClassVar[int]
    OBFUSCATE_CRYPTSOFT_CLIENT_KEY_FIELD_NUMBER: _ClassVar[int]
    INTERNAL_KMS_GANDALF_KEY_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_KEY_ROTATION_PERIOD_SECS_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_LEVEL_ENCRYPTION_ENABLED_FIELD_NUMBER: _ClassVar[int]
    OLDER_KMS_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_LEVEL_ENCRYPTION_KMS_ID_FIELD_NUMBER: _ClassVar[int]
    QOS_PRINCIPAL_MAP_FIELD_NUMBER: _ClassVar[int]
    QOS_MAPPING_VEC_FIELD_NUMBER: _ClassVar[int]
    APOLLO_THROTTLING_SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    REMOTE_CLUSTER_VEC_FIELD_NUMBER: _ClassVar[int]
    ARCHIVAL_DOMAIN_VEC_FIELD_NUMBER: _ClassVar[int]
    VAULT_VEC_FIELD_NUMBER: _ClassVar[int]
    QOS_PRINCIPAL_WORKLOAD_VEC_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_QOS_PRINCIPAL_NAMES_FIELD_NUMBER: _ClassVar[int]
    INITIAL_QOS_PRINCIPAL_WEIGHTS_FIELD_NUMBER: _ClassVar[int]
    INITIAL_QOS_PRINCIPAL_NAMES_FIELD_NUMBER: _ClassVar[int]
    INITIAL_QOS_PRINCIPAL_WORKLOAD_NAMES_FIELD_NUMBER: _ClassVar[int]
    DEPRECATED_DNS_SERVER_VEC_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_NAME_VEC_FIELD_NUMBER: _ClassVar[int]
    DEPRECATED_GATEWAY_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_DIRECTORY_CONFIG_FIELD_NUMBER: _ClassVar[int]
    WINBIND_KRB5_LOCATOR_PLUGIN_ENABLED_FIELD_NUMBER: _ClassVar[int]
    LDAP_CONFIG_FIELD_NUMBER: _ClassVar[int]
    IS_DOCUMENTATION_LOCAL_FIELD_NUMBER: _ClassVar[int]
    SNMP_CONFIG_FIELD_NUMBER: _ClassVar[int]
    NEWSCRIBE_ENABLED_FIELD_NUMBER: _ClassVar[int]
    MTU_FIELD_NUMBER: _ClassVar[int]
    FIPS_MODE_ENABLED_FIELD_NUMBER: _ClassVar[int]
    EULA_CONFIG_FIELD_NUMBER: _ClassVar[int]
    LICENSE_STATE_FIELD_NUMBER: _ClassVar[int]
    PROXY_SERVER_VEC_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_SSH_PUBLIC_KEY_FIELD_NUMBER: _ClassVar[int]
    AUTHORIZED_SSH_PUBLIC_KEY_VEC_FIELD_NUMBER: _ClassVar[int]
    DISABLE_SSH_PASSWORD_AUTHENTICATION_FIELD_NUMBER: _ClassVar[int]
    ICEBOX_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    FAULT_TOLERANCE_FIELD_NUMBER: _ClassVar[int]
    METADATA_FAULT_TOLERANCE_FACTOR_FIELD_NUMBER: _ClassVar[int]
    TOPIC_TO_METADATA_MAP_FIELD_NUMBER: _ClassVar[int]
    CONSUMER_GROUP_IDS_FIELD_NUMBER: _ClassVar[int]
    FILER_AUDIT_LOGGING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_AUDIT_LOGGING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    TIERING_AUDIT_LOGGING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    TIMEZONE_FIELD_NUMBER: _ClassVar[int]
    REMOTE_LOG_SERVERS_INFO_FIELD_NUMBER: _ClassVar[int]
    TOPIC_TO_REMOTE_LOG_SERVERS_MAP_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_LOCALE_FIELD_NUMBER: _ClassVar[int]
    ZONE_VEC_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_NETWORK_VEC_FIELD_NUMBER: _ClassVar[int]
    DATA_JOURNAL_COMPRESSION_LEVEL_FIELD_NUMBER: _ClassVar[int]
    DEPRECATED_STATIC_ROUTE_VEC_FIELD_NUMBER: _ClassVar[int]
    TURBO_MODE_FIELD_NUMBER: _ClassVar[int]
    AUTHENTICATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    AWS_PROXY_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    MULTI_TENANCY_ENABLED_FIELD_NUMBER: _ClassVar[int]
    TENANT_VIEWBOX_SHARING_ENABLED_FIELD_NUMBER: _ClassVar[int]
    TENANT_DELETION_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    YODA_CFILEDB_USE_LIBRARIAN_FIELD_NUMBER: _ClassVar[int]
    YODA_CFILEINDEX_LIBRARIAN_MIGRATION_STATUS_FIELD_NUMBER: _ClassVar[int]
    MCM_CONFIG_FIELD_NUMBER: _ClassVar[int]
    FIREWALL_PROFILE_VEC_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_SUBNET_VEC_FIELD_NUMBER: _ClassVar[int]
    ATHENA_CONFIG_FIELD_NUMBER: _ClassVar[int]
    ANTIVIRUS_CONFIG_FIELD_NUMBER: _ClassVar[int]
    LICENSE_SERVER_CLAIMED_FIELD_NUMBER: _ClassVar[int]
    IDP_CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
    STIG_MODE_ENABLED_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_GROUP_VEC_FIELD_NUMBER: _ClassVar[int]
    TLS_CERT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    NEXT_CHUNK_REPO_WAL_INCARNATION_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_SID_FIELD_NUMBER: _ClassVar[int]
    GOOGLE_ANALYTICS_ENABLED_FIELD_NUMBER: _ClassVar[int]
    LOCAL_AUTH_DOMAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    METADATA_INFO_FIELD_NUMBER: _ClassVar[int]
    HELIOS_VIEWS_FIELD_NUMBER: _ClassVar[int]
    BANNER_ENABLED_FIELD_NUMBER: _ClassVar[int]
    LOCAL_GROUPS_ENABLED_FIELD_NUMBER: _ClassVar[int]
    VIRBR0_IP_FIELD_NUMBER: _ClassVar[int]
    KEYSTONE_CONFIG_VEC_FIELD_NUMBER: _ClassVar[int]
    SWIFT_CONFIG_VEC_FIELD_NUMBER: _ClassVar[int]
    PROXY_VM_IP_FIELD_NUMBER: _ClassVar[int]
    LICENSE_START_TIME_FIELD_NUMBER: _ClassVar[int]
    IS_MANUAL_LICENSE_FIELD_NUMBER: _ClassVar[int]
    FEATURE_FLAGS_FIELD_NUMBER: _ClassVar[int]
    IP_PREFERENCE_FIELD_NUMBER: _ClassVar[int]
    DISABLED_CIPHER_LIST_FIELD_NUMBER: _ClassVar[int]
    OBJECT_STORE_DISABLED_CIPHER_LIST_FIELD_NUMBER: _ClassVar[int]
    MAGNETO_ADAPTER_STATUS_FIELD_NUMBER: _ClassVar[int]
    NIS_CONFIG_FIELD_NUMBER: _ClassVar[int]
    CLIENT_NETGROUP_WHITELIST_FIELD_NUMBER: _ClassVar[int]
    NODE_IP_ADDING_IN_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    MIGRATABLE_DISK_VEC_FIELD_NUMBER: _ClassVar[int]
    SUPPORT_USER_FIELD_NUMBER: _ClassVar[int]
    CLOUD_BANDWIDTH_LIMITS_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_SIZE_FIELD_NUMBER: _ClassVar[int]
    SMB_MULTICHANNEL_ENABLED_FIELD_NUMBER: _ClassVar[int]
    RIGEL_CONFIG_FIELD_NUMBER: _ClassVar[int]
    RIGEL_CONFIG_VEC_FIELD_NUMBER: _ClassVar[int]
    ROUTE_RIGEL_SNAP_FS_TRAFFIC_THROUGH_BROKER_FIELD_NUMBER: _ClassVar[int]
    CLOUD_DATAPLANE_INFO_FIELD_NUMBER: _ClassVar[int]
    BANNER_FIELD_NUMBER: _ClassVar[int]
    ALERT_AUDIT_LOGGING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    DATAPROTECTION_AUDIT_LOGGING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    USE_HEIMDALL_FIELD_NUMBER: _ClassVar[int]
    DEPRECATED_NODE_GROUP_VEC_FIELD_NUMBER: _ClassVar[int]
    NETWORK_CONFIG_FIELD_NUMBER: _ClassVar[int]
    AMQP_TARGET_CONFIG_FIELD_NUMBER: _ClassVar[int]
    NTP_SERVER_AUTH_KEYS_VEC_FIELD_NUMBER: _ClassVar[int]
    KERBEROS_CONFIG_FIELD_NUMBER: _ClassVar[int]
    FLASH_BLADE_REGISTRATION_VEC_FIELD_NUMBER: _ClassVar[int]
    ENABLE_PATCHES_DOWNLOAD_FIELD_NUMBER: _ClassVar[int]
    INTERNAL_BIFROST_ENABLED_FIELD_NUMBER: _ClassVar[int]
    SECURITY_CONFIG_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TEST_MODE_FIELD_NUMBER: _ClassVar[int]
    FLEET_INSTANCE_IP_VEC_FIELD_NUMBER: _ClassVar[int]
    SECURITY_MODE_ENABLED_FIELD_NUMBER: _ClassVar[int]
    NODE_ACCESS_FIELD_NUMBER: _ClassVar[int]
    IS_ANY_ACTIVE_BIFROST_TENANT_FIELD_NUMBER: _ClassVar[int]
    ROOT_CERTIFYING_AUTHORITY_FIELD_NUMBER: _ClassVar[int]
    ALLOW_CLUSTER_DESTROY_ON_API_REQUEST_FIELD_NUMBER: _ClassVar[int]
    BRIDGE_ENABLE_SECURE_VIEW_ACCESS_FIELD_NUMBER: _ClassVar[int]
    IS_GANDALF_SECURE_MODE_FIELD_NUMBER: _ClassVar[int]
    IS_DMAAS_FIELD_NUMBER: _ClassVar[int]
    ROOT_USER_FIELD_NUMBER: _ClassVar[int]
    UI_CONFIG_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_CLUSTER_CA_CERT_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_CLUSTER_CA_CERT_ID_FIELD_NUMBER: _ClassVar[int]
    CURRENT_CA_ID_VALUE_FIELD_NUMBER: _ClassVar[int]
    CERTIFYING_AUTHORITY_TO_ID_MAP_FIELD_NUMBER: _ClassVar[int]
    IS_CLUSTER_MFA_ENABLED_FIELD_NUMBER: _ClassVar[int]
    MFA_METHODS_FIELD_NUMBER: _ClassVar[int]
    NFS_PORTAL_HONOR_PROTOCOL_ACCESS_FOR_CLUSTER_IPS_FIELD_NUMBER: _ClassVar[int]
    NFS_PORTAL_HONOR_KDISABLED_FOR_CLUSTER_IPS_FIELD_NUMBER: _ClassVar[int]
    NFS_PORTAL_HONOR_EXTERNAL_VIEWS_ACCESS_FOR_CLUSTER_IPS_FIELD_NUMBER: _ClassVar[int]
    NFS_PORTAL_DISABLE_PROTOCOL_ACCESS_CHECK_FIELD_NUMBER: _ClassVar[int]
    SMB_PORTAL_DISABLE_PROTOCOL_ACCESS_CHECK_FIELD_NUMBER: _ClassVar[int]
    ENFORCE_NFS_ACCESS_CHECKS_FOR_S3_VIEWS_FOR_CLUSTER_IPS_FIELD_NUMBER: _ClassVar[int]
    HELIOS_ONPREM_CONFIG_FIELD_NUMBER: _ClassVar[int]
    IS_INTERNODE_PROTORPC_ENCRYPTION_ENABLED_FIELD_NUMBER: _ClassVar[int]
    HARDWARE_ENCRYPTION_ENABLED_FIELD_NUMBER: _ClassVar[int]
    DISAGGREGATED_METADATA_DISK_ENABLED_FIELD_NUMBER: _ClassVar[int]
    DISAGGREGATED_STORAGE_FENCING_ENABLED_FIELD_NUMBER: _ClassVar[int]
    MAX_CHUNK_FILE_ID_TO_CHECK_FOR_BLOAT_FIELD_NUMBER: _ClassVar[int]
    ES_USE_SYSTEM_SERVICES_FIELD_NUMBER: _ClassVar[int]
    YODA_ES_MIGRATION_TO_OPENSEARCH_STATUS_FIELD_NUMBER: _ClassVar[int]
    YODA_ES_MIGRATION_STATUS_FIELD_NUMBER: _ClassVar[int]
    YODA_PXG_ES_DATA_MIGRATION_STATUS_FIELD_NUMBER: _ClassVar[int]
    S3_PORTAL_HONOR_OBJECT_STORE_ACCESS_ENABLE_FLAG_FIELD_NUMBER: _ClassVar[int]
    IRIS_API_BACKUP_DATA_ACL_FIELD_NUMBER: _ClassVar[int]
    UPDATED_REALM_INFO_CONNECTOR_PARAMS_PRE_68_FIELD_NUMBER: _ClassVar[int]
    SPLIT_KEY_ENABLED_FIELD_NUMBER: _ClassVar[int]
    OPERATION_STATE_MAP_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_AES_ENCRYPTION_MODE_DEPRECATED_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_SSH_ENCRYPTED_PRIV_KEY_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ACTIVE_SSH_PRIVATE_KEY_MD5SUM_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_TARGET_SSH_PRIVATE_KEY_MD5SUM_FIELD_NUMBER: _ClassVar[int]
    LAST_ROTATED_SSH_KEY_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_TARGET_ENC_SSH_PRIV_KEY_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_TARGET_SSH_PUBLIC_KEY_FIELD_NUMBER: _ClassVar[int]
    APOLLO_BINARY_LOGGING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    EXPOSE_TRACKING_VIEW_FIELD_NUMBER: _ClassVar[int]
    LIST_TRACKING_VIEW_UI_FIELD_NUMBER: _ClassVar[int]
    AIRGAP_CONFIG_FIELD_NUMBER: _ClassVar[int]
    SSH_CONFIG_FIELD_NUMBER: _ClassVar[int]
    SERVICE_IDENTITY_FIELD_NUMBER: _ClassVar[int]
    LAST_SCRIBE_EXCLUSIVE_DISK_SWITCH_USECS_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_AES_ENCRYPTION_FIELD_NUMBER: _ClassVar[int]
    ABAC_CONFIG_FIELD_NUMBER: _ClassVar[int]
    VIRTUAL_HOSTING_DOMAIN_VEC_FIELD_NUMBER: _ClassVar[int]
    COHESION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_SNAPSHOT_POLICY_FIELD_NUMBER: _ClassVar[int]
    PATCH_DOWNLOAD_IN_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    USE_DEFAULT_AGENT_PORTS_FIELD_NUMBER: _ClassVar[int]
    ATTEMPT_AGENT_PORTS_UPGRADE_FIELD_NUMBER: _ClassVar[int]
    cluster_id: int
    cluster_incarnation_id: int
    cluster_name: str
    deprecated_subnet: ClusterConfigProto.Subnet
    internal_subnet: ClusterConfigProto.Subnet
    client_subnet_whitelist: _containers.RepeatedCompositeFieldContainer[ClusterConfigProto.Subnet]
    storage_tier_vec: _containers.RepeatedCompositeFieldContainer[ClusterConfigProto.StorageTier]
    scribe_storage_tier_vec: _containers.RepeatedScalarFieldContainer[int]
    sequential_io_preference_index: int
    sequential_storage_tier_vec: _containers.RepeatedScalarFieldContainer[int]
    random_storage_tier_vec: _containers.RepeatedScalarFieldContainer[int]
    tier_shuffle_threshold_pct: int
    min_tier_shuffle_util_pct: int
    disk_vec: _containers.RepeatedCompositeFieldContainer[ClusterConfigProto.Disk]
    rack_vec: _containers.RepeatedCompositeFieldContainer[ClusterConfigProto.Rack]
    chassis_vec: _containers.RepeatedCompositeFieldContainer[ClusterConfigProto.Chassis]
    node_vec: _containers.RepeatedCompositeFieldContainer[ClusterConfigProto.Node]
    cluster_partition_vec: _containers.RepeatedCompositeFieldContainer[ClusterConfigProto.ClusterPartition]
    view_box_vec: _containers.RepeatedCompositeFieldContainer[ClusterConfigProto.ViewBox]
    bulletin_board: ClusterConfigProto.Bulletin
    scribe_table_names: ClusterConfigProto.ScribeTableNames
    ntp_server_vec: _containers.RepeatedScalarFieldContainer[str]
    ntp_settings: ClusterConfigProto.NTPSettings
    bonding_mode: ClusterConfigProto.BondingMode
    smtp_server: ClusterConfigProto.SmtpServer
    support_server: ClusterConfigProto.SupportServer
    support_server_v2: ClusterConfigProto.SupportServer
    support_server_v2_config: _containers.RepeatedCompositeFieldContainer[_support_service_config_pb2.SupportServerV2Config]
    apollo_storage_tier_index: int
    apollo_storage_tier_vec: _containers.RepeatedScalarFieldContainer[int]
    apollo_wal_storage_tier_index: int
    apollo_wal_storage_tier_vec: _containers.RepeatedScalarFieldContainer[int]
    yoda_storage_tier_vec: _containers.RepeatedScalarFieldContainer[int]
    hydra_storage_tier_vec: _containers.RepeatedScalarFieldContainer[int]
    hydra_downtier_storage_tier_vec: _containers.RepeatedScalarFieldContainer[int]
    librarian_storage_tier_vec: _containers.RepeatedScalarFieldContainer[int]
    groot_storage_tier_index: int
    groot_storage_tier_vec: _containers.RepeatedScalarFieldContainer[int]
    athena_storage_tier_vec: _containers.RepeatedScalarFieldContainer[int]
    athena_slower_storage_tier_vec: _containers.RepeatedScalarFieldContainer[int]
    eagle_agent_storage_tier_vec: _containers.RepeatedScalarFieldContainer[int]
    cloud_chunk_repo_storage_tier_vec: _containers.RepeatedScalarFieldContainer[int]
    alert_notification_email_list: _containers.RepeatedScalarFieldContainer[str]
    ipmi_config: ClusterConfigProto.IpmiConfig
    nfs_export_path_list: _containers.RepeatedScalarFieldContainer[str]
    halo_config: ClusterConfigProto.HaloConfig
    eagle_config: ClusterConfigProto.EagleConfig
    kms_server_vec: _containers.RepeatedCompositeFieldContainer[ClusterConfigProto.KMSConfig]
    obfuscate_cryptsoft_client_key: bool
    internal_kms_gandalf_key: str
    encryption_key_rotation_period_secs: int
    cluster_level_encryption_enabled: bool
    older_kms_id: int
    cluster_level_encryption_kms_id: int
    qos_principal_map: _containers.MessageMap[int, ClusterConfigProto.QoSPrincipal]
    qos_mapping_vec: _containers.RepeatedCompositeFieldContainer[ClusterConfigProto.QoSMapping]
    apollo_throttling_schedule: ClusterConfigProto.BandwidthLimit
    remote_cluster_vec: _containers.RepeatedCompositeFieldContainer[ClusterConfigProto.RemoteCluster]
    archival_domain_vec: _containers.RepeatedCompositeFieldContainer[ClusterConfigProto.ArchivalDomain]
    vault_vec: _containers.RepeatedCompositeFieldContainer[ClusterConfigProto.Vault]
    qos_principal_workload_vec: _containers.RepeatedCompositeFieldContainer[ClusterConfigProto.QoSPrincipalWorkload]
    default_qos_principal_names: ClusterConfigProto.DefaultQoSPrincipalNames
    initial_qos_principal_weights: ClusterConfigProto.InitialQoSPrincipalWeights
    initial_qos_principal_names: ClusterConfigProto.InitialQoSPrincipalNames
    initial_qos_principal_workload_names: ClusterConfigProto.InitialQoSPrincipalWorkloadNames
    deprecated_dns_server_vec: _containers.RepeatedScalarFieldContainer[str]
    domain_name_vec: _containers.RepeatedScalarFieldContainer[str]
    deprecated_gateway: str
    active_directory_config: ClusterConfigProto.ActiveDirectoryConfig
    winbind_krb5_locator_plugin_enabled: bool
    ldap_config: ClusterConfigProto.LdapConfig
    is_documentation_local: bool
    snmp_config: ClusterConfigProto.SnmpConfig
    newscribe_enabled: bool
    mtu: int
    fips_mode_enabled: bool
    eula_config: ClusterConfigProto.EulaConfig
    license_state: ClusterConfigProto.LicenseState
    proxy_server_vec: _containers.RepeatedCompositeFieldContainer[ClusterConfigProto.ProxyServerConfig]
    cluster_ssh_public_key: str
    authorized_ssh_public_key_vec: _containers.RepeatedScalarFieldContainer[str]
    disable_ssh_password_authentication: bool
    icebox_properties: ClusterConfigProto.IceboxProperties
    fault_tolerance: ClusterConfigProto.FaultToleranceStrictness
    metadata_fault_tolerance_factor: int
    topic_to_metadata_map: _containers.MessageMap[str, ClusterConfigProto.TopicMetadata]
    consumer_group_ids: ClusterConfigProto.ConsumerGroupIds
    filer_audit_logging_config: ClusterConfigProto.AuditLoggingConfig
    cluster_audit_logging_config: ClusterConfigProto.AuditLoggingConfig
    tiering_audit_logging_config: ClusterConfigProto.AuditLoggingConfig
    timezone: str
    remote_log_servers_info: ClusterConfigProto.RemoteLogServerInfo
    topic_to_remote_log_servers_map: _containers.MessageMap[str, ClusterConfigProto.RemoteLogServers]
    language_locale: str
    zone_vec: _containers.RepeatedCompositeFieldContainer[ClusterConfigProto.NetworkZone]
    cluster_network_vec: _containers.RepeatedCompositeFieldContainer[ClusterConfigProto.Vlan]
    data_journal_compression_level: ClusterConfigProto.StoragePolicy.CompressionLevel
    deprecated_static_route_vec: _containers.RepeatedCompositeFieldContainer[ClusterConfigProto.StaticRoute]
    turbo_mode: bool
    authentication_type: ClusterConfigProto.AuthType
    aws_proxy_info_vec: _containers.RepeatedCompositeFieldContainer[ClusterConfigProto.AWSProxyInfo]
    multi_tenancy_enabled: bool
    tenant_viewbox_sharing_enabled: bool
    tenant_deletion_info_vec: _containers.RepeatedCompositeFieldContainer[ClusterConfigProto.TenantDeletionInfo]
    yoda_cfiledb_use_librarian: bool
    yoda_cfileindex_librarian_migration_status: ClusterConfigProto.LibrarianMigrationStatus
    mcm_config: MultiClusterManagerConfig
    firewall_profile_vec: _containers.RepeatedCompositeFieldContainer[ClusterConfigProto.FirewallProfile]
    cluster_subnet_vec: _containers.RepeatedCompositeFieldContainer[ClusterConfigProto.Subnet]
    athena_config: ClusterConfigProto.AthenaConfig
    antivirus_config: ClusterConfigProto.AntivirusConfig
    license_server_claimed: bool
    idp_configuration: IdpConfiguration
    stig_mode_enabled: bool
    interface_group_vec: _containers.RepeatedCompositeFieldContainer[ClusterConfigProto.InterfaceGroup]
    tls_cert_config: ClusterConfigProto.TLSCertConfig
    next_chunk_repo_wal_incarnation: int
    domain_sid: ClusterConfigProto.SID
    google_analytics_enabled: bool
    local_auth_domain_name: str
    metadata_info: ClusterConfigProto.MetadataInfo
    helios_views: ClusterConfigProto.HeliosViewsProto
    banner_enabled: bool
    local_groups_enabled: bool
    virbr0_ip: str
    keystone_config_vec: _containers.RepeatedCompositeFieldContainer[ClusterConfigProto.KeystoneConfig]
    swift_config_vec: _containers.RepeatedCompositeFieldContainer[ClusterConfigProto.SwiftConfig]
    proxy_vm_ip: str
    license_start_time: int
    is_manual_license: bool
    feature_flags: ClusterConfigProto.FeatureFlags
    ip_preference: ClusterConfigProto.IpAddressFamily
    disabled_cipher_list: _containers.RepeatedScalarFieldContainer[str]
    object_store_disabled_cipher_list: _containers.RepeatedScalarFieldContainer[str]
    magneto_adapter_status: ClusterConfigProto.MagnetoAdapterStatus
    nis_config: ClusterConfigProto.NisConfig
    client_netgroup_whitelist: _containers.RepeatedCompositeFieldContainer[ClusterConfigProto.NISNetgroup]
    node_ip_adding_in_progress: _containers.RepeatedScalarFieldContainer[str]
    migratable_disk_vec: _containers.RepeatedCompositeFieldContainer[ClusterConfigProto.Disk]
    support_user: ClusterConfigProto.SupportUser
    cloud_bandwidth_limits: ClusterConfigProto.CloudBandwidthLimits
    cluster_size: ClusterConfigProto.ClusterSize
    smb_multichannel_enabled: bool
    rigel_config: ClusterConfigProto.RigelConfig
    rigel_config_vec: _containers.RepeatedCompositeFieldContainer[ClusterConfigProto.RigelConfig]
    route_rigel_snap_fs_traffic_through_broker: bool
    cloud_dataplane_info: ClusterConfigProto.CloudDataplaneInfo
    banner: str
    alert_audit_logging_config: ClusterConfigProto.AuditLoggingConfig
    dataprotection_audit_logging_config: ClusterConfigProto.AuditLoggingConfig
    use_heimdall: bool
    deprecated_node_group_vec: _containers.RepeatedCompositeFieldContainer[_node_network_pb2.NodeGroup]
    network_config: _cluster_network_pb2.ClusterNetworkProto
    amqp_target_config: ClusterConfigProto.AMQPTargetConfig
    ntp_server_auth_keys_vec: _containers.RepeatedCompositeFieldContainer[ClusterConfigProto.NTPAuthKeyInfo]
    kerberos_config: ClusterConfigProto.KerberosConfig
    flash_blade_registration_vec: _containers.RepeatedCompositeFieldContainer[ClusterConfigProto.PureFlashbladeInfo]
    enable_patches_download: bool
    internal_bifrost_enabled: bool
    security_config: ClusterConfigProto.SecurityConfig
    description: str
    test_mode: bool
    fleet_instance_ip_vec: _containers.RepeatedScalarFieldContainer[str]
    security_mode_enabled: bool
    node_access: ClusterConfigProto.NodeAccess
    is_any_active_bifrost_tenant: bool
    root_certifying_authority: ClusterConfigProto.RootCertifyingAuthority
    allow_cluster_destroy_on_api_request: bool
    bridge_enable_secure_view_access: bool
    is_gandalf_secure_mode: bool
    is_dmaas: bool
    root_user: ClusterConfigProto.RootUser
    ui_config: str
    active_cluster_ca_cert_id: int
    target_cluster_ca_cert_id: int
    current_ca_id_value: int
    certifying_authority_to_id_map: _containers.RepeatedCompositeFieldContainer[ClusterConfigProto.CertifyingAuthorityToIdMap]
    is_cluster_mfa_enabled: bool
    mfa_methods: _containers.RepeatedScalarFieldContainer[str]
    nfs_portal_honor_protocol_access_for_cluster_ips: bool
    nfs_portal_honor_kdisabled_for_cluster_ips: bool
    nfs_portal_honor_external_views_access_for_cluster_ips: bool
    nfs_portal_disable_protocol_access_check: bool
    smb_portal_disable_protocol_access_check: bool
    enforce_nfs_access_checks_for_s3_views_for_cluster_ips: bool
    helios_onprem_config: ClusterConfigProto.HeliosOnpremConfig
    is_internode_protorpc_encryption_enabled: bool
    hardware_encryption_enabled: bool
    disaggregated_metadata_disk_enabled: bool
    disaggregated_storage_fencing_enabled: bool
    max_chunk_file_id_to_check_for_bloat: int
    es_use_system_services: bool
    yoda_es_migration_to_opensearch_status: ClusterConfigProto.ESMigrationStatus
    yoda_es_migration_status: ClusterConfigProto.ESMigrationStatus
    yoda_pxg_es_data_migration_status: ClusterConfigProto.PXGESMigrationStatus
    s3_portal_honor_object_store_access_enable_flag: bool
    iris_api_backup_data_acl: ClusterConfigProto.IrisAPIBackupDataACL
    updated_realm_info_connector_params_pre_68: bool
    split_key_enabled: bool
    operation_state_map: _containers.MessageMap[str, ClusterConfigProto.OperationState]
    cluster_aes_encryption_mode_deprecated: _aes_encryptor_pb2.AESEncryptorMode
    cluster_ssh_encrypted_priv_key: bytes
    cluster_active_ssh_private_key_md5sum: str
    cluster_target_ssh_private_key_md5sum: str
    last_rotated_ssh_key_timestamp: str
    cluster_target_enc_ssh_priv_key: bytes
    cluster_target_ssh_public_key: str
    apollo_binary_logging_config: ClusterConfigProto.ApolloBinaryLoggingConfig
    expose_tracking_view: bool
    list_tracking_view_ui: bool
    airgap_config: ClusterConfigProto.AirgapConfig
    ssh_config: ClusterConfigProto.SshConfig
    service_identity: ClusterConfigProto.ServiceIdentity
    last_scribe_exclusive_disk_switch_usecs: int
    cluster_aes_encryption: ClusterConfigProto.ClusterAESEncryption
    abac_config: ClusterConfigProto.AbacConfig
    virtual_hosting_domain_vec: _containers.RepeatedScalarFieldContainer[str]
    cohesion_config: ClusterConfigProto.CohesionConfig
    cluster_snapshot_policy: ClusterConfigProto.ClusterSnapshotPolicy
    patch_download_in_progress: bool
    use_default_agent_ports: bool
    attempt_agent_ports_upgrade: bool
    def __init__(self, cluster_id: _Optional[int] = ..., cluster_incarnation_id: _Optional[int] = ..., cluster_name: _Optional[str] = ..., deprecated_subnet: _Optional[_Union[ClusterConfigProto.Subnet, _Mapping]] = ..., internal_subnet: _Optional[_Union[ClusterConfigProto.Subnet, _Mapping]] = ..., client_subnet_whitelist: _Optional[_Iterable[_Union[ClusterConfigProto.Subnet, _Mapping]]] = ..., storage_tier_vec: _Optional[_Iterable[_Union[ClusterConfigProto.StorageTier, _Mapping]]] = ..., scribe_storage_tier_vec: _Optional[_Iterable[int]] = ..., sequential_io_preference_index: _Optional[int] = ..., sequential_storage_tier_vec: _Optional[_Iterable[int]] = ..., random_storage_tier_vec: _Optional[_Iterable[int]] = ..., tier_shuffle_threshold_pct: _Optional[int] = ..., min_tier_shuffle_util_pct: _Optional[int] = ..., disk_vec: _Optional[_Iterable[_Union[ClusterConfigProto.Disk, _Mapping]]] = ..., rack_vec: _Optional[_Iterable[_Union[ClusterConfigProto.Rack, _Mapping]]] = ..., chassis_vec: _Optional[_Iterable[_Union[ClusterConfigProto.Chassis, _Mapping]]] = ..., node_vec: _Optional[_Iterable[_Union[ClusterConfigProto.Node, _Mapping]]] = ..., cluster_partition_vec: _Optional[_Iterable[_Union[ClusterConfigProto.ClusterPartition, _Mapping]]] = ..., view_box_vec: _Optional[_Iterable[_Union[ClusterConfigProto.ViewBox, _Mapping]]] = ..., bulletin_board: _Optional[_Union[ClusterConfigProto.Bulletin, _Mapping]] = ..., scribe_table_names: _Optional[_Union[ClusterConfigProto.ScribeTableNames, _Mapping]] = ..., ntp_server_vec: _Optional[_Iterable[str]] = ..., ntp_settings: _Optional[_Union[ClusterConfigProto.NTPSettings, _Mapping]] = ..., bonding_mode: _Optional[_Union[ClusterConfigProto.BondingMode, str]] = ..., smtp_server: _Optional[_Union[ClusterConfigProto.SmtpServer, _Mapping]] = ..., support_server: _Optional[_Union[ClusterConfigProto.SupportServer, _Mapping]] = ..., support_server_v2: _Optional[_Union[ClusterConfigProto.SupportServer, _Mapping]] = ..., support_server_v2_config: _Optional[_Iterable[_Union[_support_service_config_pb2.SupportServerV2Config, _Mapping]]] = ..., apollo_storage_tier_index: _Optional[int] = ..., apollo_storage_tier_vec: _Optional[_Iterable[int]] = ..., apollo_wal_storage_tier_index: _Optional[int] = ..., apollo_wal_storage_tier_vec: _Optional[_Iterable[int]] = ..., yoda_storage_tier_vec: _Optional[_Iterable[int]] = ..., hydra_storage_tier_vec: _Optional[_Iterable[int]] = ..., hydra_downtier_storage_tier_vec: _Optional[_Iterable[int]] = ..., librarian_storage_tier_vec: _Optional[_Iterable[int]] = ..., groot_storage_tier_index: _Optional[int] = ..., groot_storage_tier_vec: _Optional[_Iterable[int]] = ..., athena_storage_tier_vec: _Optional[_Iterable[int]] = ..., athena_slower_storage_tier_vec: _Optional[_Iterable[int]] = ..., eagle_agent_storage_tier_vec: _Optional[_Iterable[int]] = ..., cloud_chunk_repo_storage_tier_vec: _Optional[_Iterable[int]] = ..., alert_notification_email_list: _Optional[_Iterable[str]] = ..., ipmi_config: _Optional[_Union[ClusterConfigProto.IpmiConfig, _Mapping]] = ..., nfs_export_path_list: _Optional[_Iterable[str]] = ..., halo_config: _Optional[_Union[ClusterConfigProto.HaloConfig, _Mapping]] = ..., eagle_config: _Optional[_Union[ClusterConfigProto.EagleConfig, _Mapping]] = ..., kms_server_vec: _Optional[_Iterable[_Union[ClusterConfigProto.KMSConfig, _Mapping]]] = ..., obfuscate_cryptsoft_client_key: bool = ..., internal_kms_gandalf_key: _Optional[str] = ..., encryption_key_rotation_period_secs: _Optional[int] = ..., cluster_level_encryption_enabled: bool = ..., older_kms_id: _Optional[int] = ..., cluster_level_encryption_kms_id: _Optional[int] = ..., qos_principal_map: _Optional[_Mapping[int, ClusterConfigProto.QoSPrincipal]] = ..., qos_mapping_vec: _Optional[_Iterable[_Union[ClusterConfigProto.QoSMapping, _Mapping]]] = ..., apollo_throttling_schedule: _Optional[_Union[ClusterConfigProto.BandwidthLimit, _Mapping]] = ..., remote_cluster_vec: _Optional[_Iterable[_Union[ClusterConfigProto.RemoteCluster, _Mapping]]] = ..., archival_domain_vec: _Optional[_Iterable[_Union[ClusterConfigProto.ArchivalDomain, _Mapping]]] = ..., vault_vec: _Optional[_Iterable[_Union[ClusterConfigProto.Vault, _Mapping]]] = ..., qos_principal_workload_vec: _Optional[_Iterable[_Union[ClusterConfigProto.QoSPrincipalWorkload, _Mapping]]] = ..., default_qos_principal_names: _Optional[_Union[ClusterConfigProto.DefaultQoSPrincipalNames, _Mapping]] = ..., initial_qos_principal_weights: _Optional[_Union[ClusterConfigProto.InitialQoSPrincipalWeights, _Mapping]] = ..., initial_qos_principal_names: _Optional[_Union[ClusterConfigProto.InitialQoSPrincipalNames, _Mapping]] = ..., initial_qos_principal_workload_names: _Optional[_Union[ClusterConfigProto.InitialQoSPrincipalWorkloadNames, _Mapping]] = ..., deprecated_dns_server_vec: _Optional[_Iterable[str]] = ..., domain_name_vec: _Optional[_Iterable[str]] = ..., deprecated_gateway: _Optional[str] = ..., active_directory_config: _Optional[_Union[ClusterConfigProto.ActiveDirectoryConfig, _Mapping]] = ..., winbind_krb5_locator_plugin_enabled: bool = ..., ldap_config: _Optional[_Union[ClusterConfigProto.LdapConfig, _Mapping]] = ..., is_documentation_local: bool = ..., snmp_config: _Optional[_Union[ClusterConfigProto.SnmpConfig, _Mapping]] = ..., newscribe_enabled: bool = ..., mtu: _Optional[int] = ..., fips_mode_enabled: bool = ..., eula_config: _Optional[_Union[ClusterConfigProto.EulaConfig, _Mapping]] = ..., license_state: _Optional[_Union[ClusterConfigProto.LicenseState, _Mapping]] = ..., proxy_server_vec: _Optional[_Iterable[_Union[ClusterConfigProto.ProxyServerConfig, _Mapping]]] = ..., cluster_ssh_public_key: _Optional[str] = ..., authorized_ssh_public_key_vec: _Optional[_Iterable[str]] = ..., disable_ssh_password_authentication: bool = ..., icebox_properties: _Optional[_Union[ClusterConfigProto.IceboxProperties, _Mapping]] = ..., fault_tolerance: _Optional[_Union[ClusterConfigProto.FaultToleranceStrictness, _Mapping]] = ..., metadata_fault_tolerance_factor: _Optional[int] = ..., topic_to_metadata_map: _Optional[_Mapping[str, ClusterConfigProto.TopicMetadata]] = ..., consumer_group_ids: _Optional[_Union[ClusterConfigProto.ConsumerGroupIds, _Mapping]] = ..., filer_audit_logging_config: _Optional[_Union[ClusterConfigProto.AuditLoggingConfig, _Mapping]] = ..., cluster_audit_logging_config: _Optional[_Union[ClusterConfigProto.AuditLoggingConfig, _Mapping]] = ..., tiering_audit_logging_config: _Optional[_Union[ClusterConfigProto.AuditLoggingConfig, _Mapping]] = ..., timezone: _Optional[str] = ..., remote_log_servers_info: _Optional[_Union[ClusterConfigProto.RemoteLogServerInfo, _Mapping]] = ..., topic_to_remote_log_servers_map: _Optional[_Mapping[str, ClusterConfigProto.RemoteLogServers]] = ..., language_locale: _Optional[str] = ..., zone_vec: _Optional[_Iterable[_Union[ClusterConfigProto.NetworkZone, _Mapping]]] = ..., cluster_network_vec: _Optional[_Iterable[_Union[ClusterConfigProto.Vlan, _Mapping]]] = ..., data_journal_compression_level: _Optional[_Union[ClusterConfigProto.StoragePolicy.CompressionLevel, str]] = ..., deprecated_static_route_vec: _Optional[_Iterable[_Union[ClusterConfigProto.StaticRoute, _Mapping]]] = ..., turbo_mode: bool = ..., authentication_type: _Optional[_Union[ClusterConfigProto.AuthType, str]] = ..., aws_proxy_info_vec: _Optional[_Iterable[_Union[ClusterConfigProto.AWSProxyInfo, _Mapping]]] = ..., multi_tenancy_enabled: bool = ..., tenant_viewbox_sharing_enabled: bool = ..., tenant_deletion_info_vec: _Optional[_Iterable[_Union[ClusterConfigProto.TenantDeletionInfo, _Mapping]]] = ..., yoda_cfiledb_use_librarian: bool = ..., yoda_cfileindex_librarian_migration_status: _Optional[_Union[ClusterConfigProto.LibrarianMigrationStatus, str]] = ..., mcm_config: _Optional[_Union[MultiClusterManagerConfig, _Mapping]] = ..., firewall_profile_vec: _Optional[_Iterable[_Union[ClusterConfigProto.FirewallProfile, _Mapping]]] = ..., cluster_subnet_vec: _Optional[_Iterable[_Union[ClusterConfigProto.Subnet, _Mapping]]] = ..., athena_config: _Optional[_Union[ClusterConfigProto.AthenaConfig, _Mapping]] = ..., antivirus_config: _Optional[_Union[ClusterConfigProto.AntivirusConfig, _Mapping]] = ..., license_server_claimed: bool = ..., idp_configuration: _Optional[_Union[IdpConfiguration, _Mapping]] = ..., stig_mode_enabled: bool = ..., interface_group_vec: _Optional[_Iterable[_Union[ClusterConfigProto.InterfaceGroup, _Mapping]]] = ..., tls_cert_config: _Optional[_Union[ClusterConfigProto.TLSCertConfig, _Mapping]] = ..., next_chunk_repo_wal_incarnation: _Optional[int] = ..., domain_sid: _Optional[_Union[ClusterConfigProto.SID, _Mapping]] = ..., google_analytics_enabled: bool = ..., local_auth_domain_name: _Optional[str] = ..., metadata_info: _Optional[_Union[ClusterConfigProto.MetadataInfo, _Mapping]] = ..., helios_views: _Optional[_Union[ClusterConfigProto.HeliosViewsProto, _Mapping]] = ..., banner_enabled: bool = ..., local_groups_enabled: bool = ..., virbr0_ip: _Optional[str] = ..., keystone_config_vec: _Optional[_Iterable[_Union[ClusterConfigProto.KeystoneConfig, _Mapping]]] = ..., swift_config_vec: _Optional[_Iterable[_Union[ClusterConfigProto.SwiftConfig, _Mapping]]] = ..., proxy_vm_ip: _Optional[str] = ..., license_start_time: _Optional[int] = ..., is_manual_license: bool = ..., feature_flags: _Optional[_Union[ClusterConfigProto.FeatureFlags, _Mapping]] = ..., ip_preference: _Optional[_Union[ClusterConfigProto.IpAddressFamily, str]] = ..., disabled_cipher_list: _Optional[_Iterable[str]] = ..., object_store_disabled_cipher_list: _Optional[_Iterable[str]] = ..., magneto_adapter_status: _Optional[_Union[ClusterConfigProto.MagnetoAdapterStatus, _Mapping]] = ..., nis_config: _Optional[_Union[ClusterConfigProto.NisConfig, _Mapping]] = ..., client_netgroup_whitelist: _Optional[_Iterable[_Union[ClusterConfigProto.NISNetgroup, _Mapping]]] = ..., node_ip_adding_in_progress: _Optional[_Iterable[str]] = ..., migratable_disk_vec: _Optional[_Iterable[_Union[ClusterConfigProto.Disk, _Mapping]]] = ..., support_user: _Optional[_Union[ClusterConfigProto.SupportUser, _Mapping]] = ..., cloud_bandwidth_limits: _Optional[_Union[ClusterConfigProto.CloudBandwidthLimits, _Mapping]] = ..., cluster_size: _Optional[_Union[ClusterConfigProto.ClusterSize, str]] = ..., smb_multichannel_enabled: bool = ..., rigel_config: _Optional[_Union[ClusterConfigProto.RigelConfig, _Mapping]] = ..., rigel_config_vec: _Optional[_Iterable[_Union[ClusterConfigProto.RigelConfig, _Mapping]]] = ..., route_rigel_snap_fs_traffic_through_broker: bool = ..., cloud_dataplane_info: _Optional[_Union[ClusterConfigProto.CloudDataplaneInfo, _Mapping]] = ..., banner: _Optional[str] = ..., alert_audit_logging_config: _Optional[_Union[ClusterConfigProto.AuditLoggingConfig, _Mapping]] = ..., dataprotection_audit_logging_config: _Optional[_Union[ClusterConfigProto.AuditLoggingConfig, _Mapping]] = ..., use_heimdall: bool = ..., deprecated_node_group_vec: _Optional[_Iterable[_Union[_node_network_pb2.NodeGroup, _Mapping]]] = ..., network_config: _Optional[_Union[_cluster_network_pb2.ClusterNetworkProto, _Mapping]] = ..., amqp_target_config: _Optional[_Union[ClusterConfigProto.AMQPTargetConfig, _Mapping]] = ..., ntp_server_auth_keys_vec: _Optional[_Iterable[_Union[ClusterConfigProto.NTPAuthKeyInfo, _Mapping]]] = ..., kerberos_config: _Optional[_Union[ClusterConfigProto.KerberosConfig, _Mapping]] = ..., flash_blade_registration_vec: _Optional[_Iterable[_Union[ClusterConfigProto.PureFlashbladeInfo, _Mapping]]] = ..., enable_patches_download: bool = ..., internal_bifrost_enabled: bool = ..., security_config: _Optional[_Union[ClusterConfigProto.SecurityConfig, _Mapping]] = ..., description: _Optional[str] = ..., test_mode: bool = ..., fleet_instance_ip_vec: _Optional[_Iterable[str]] = ..., security_mode_enabled: bool = ..., node_access: _Optional[_Union[ClusterConfigProto.NodeAccess, _Mapping]] = ..., is_any_active_bifrost_tenant: bool = ..., root_certifying_authority: _Optional[_Union[ClusterConfigProto.RootCertifyingAuthority, _Mapping]] = ..., allow_cluster_destroy_on_api_request: bool = ..., bridge_enable_secure_view_access: bool = ..., is_gandalf_secure_mode: bool = ..., is_dmaas: bool = ..., root_user: _Optional[_Union[ClusterConfigProto.RootUser, _Mapping]] = ..., ui_config: _Optional[str] = ..., active_cluster_ca_cert_id: _Optional[int] = ..., target_cluster_ca_cert_id: _Optional[int] = ..., current_ca_id_value: _Optional[int] = ..., certifying_authority_to_id_map: _Optional[_Iterable[_Union[ClusterConfigProto.CertifyingAuthorityToIdMap, _Mapping]]] = ..., is_cluster_mfa_enabled: bool = ..., mfa_methods: _Optional[_Iterable[str]] = ..., nfs_portal_honor_protocol_access_for_cluster_ips: bool = ..., nfs_portal_honor_kdisabled_for_cluster_ips: bool = ..., nfs_portal_honor_external_views_access_for_cluster_ips: bool = ..., nfs_portal_disable_protocol_access_check: bool = ..., smb_portal_disable_protocol_access_check: bool = ..., enforce_nfs_access_checks_for_s3_views_for_cluster_ips: bool = ..., helios_onprem_config: _Optional[_Union[ClusterConfigProto.HeliosOnpremConfig, _Mapping]] = ..., is_internode_protorpc_encryption_enabled: bool = ..., hardware_encryption_enabled: bool = ..., disaggregated_metadata_disk_enabled: bool = ..., disaggregated_storage_fencing_enabled: bool = ..., max_chunk_file_id_to_check_for_bloat: _Optional[int] = ..., es_use_system_services: bool = ..., yoda_es_migration_to_opensearch_status: _Optional[_Union[ClusterConfigProto.ESMigrationStatus, str]] = ..., yoda_es_migration_status: _Optional[_Union[ClusterConfigProto.ESMigrationStatus, str]] = ..., yoda_pxg_es_data_migration_status: _Optional[_Union[ClusterConfigProto.PXGESMigrationStatus, str]] = ..., s3_portal_honor_object_store_access_enable_flag: bool = ..., iris_api_backup_data_acl: _Optional[_Union[ClusterConfigProto.IrisAPIBackupDataACL, str]] = ..., updated_realm_info_connector_params_pre_68: bool = ..., split_key_enabled: bool = ..., operation_state_map: _Optional[_Mapping[str, ClusterConfigProto.OperationState]] = ..., cluster_aes_encryption_mode_deprecated: _Optional[_Union[_aes_encryptor_pb2.AESEncryptorMode, str]] = ..., cluster_ssh_encrypted_priv_key: _Optional[bytes] = ..., cluster_active_ssh_private_key_md5sum: _Optional[str] = ..., cluster_target_ssh_private_key_md5sum: _Optional[str] = ..., last_rotated_ssh_key_timestamp: _Optional[str] = ..., cluster_target_enc_ssh_priv_key: _Optional[bytes] = ..., cluster_target_ssh_public_key: _Optional[str] = ..., apollo_binary_logging_config: _Optional[_Union[ClusterConfigProto.ApolloBinaryLoggingConfig, _Mapping]] = ..., expose_tracking_view: bool = ..., list_tracking_view_ui: bool = ..., airgap_config: _Optional[_Union[ClusterConfigProto.AirgapConfig, _Mapping]] = ..., ssh_config: _Optional[_Union[ClusterConfigProto.SshConfig, _Mapping]] = ..., service_identity: _Optional[_Union[ClusterConfigProto.ServiceIdentity, _Mapping]] = ..., last_scribe_exclusive_disk_switch_usecs: _Optional[int] = ..., cluster_aes_encryption: _Optional[_Union[ClusterConfigProto.ClusterAESEncryption, _Mapping]] = ..., abac_config: _Optional[_Union[ClusterConfigProto.AbacConfig, _Mapping]] = ..., virtual_hosting_domain_vec: _Optional[_Iterable[str]] = ..., cohesion_config: _Optional[_Union[ClusterConfigProto.CohesionConfig, _Mapping]] = ..., cluster_snapshot_policy: _Optional[_Union[ClusterConfigProto.ClusterSnapshotPolicy, _Mapping]] = ..., patch_download_in_progress: bool = ..., use_default_agent_ports: bool = ..., attempt_agent_ports_upgrade: bool = ...) -> None: ...

class MultiClusterManagerConfig(_message.Message):
    __slots__ = ("registration_status", "mcm_connection_status", "enable_mcm", "mcm_read_only", "registration_error", "redirect_url", "mcm_url", "mcm_data_url", "is_app_mode", "license_only", "sso_url", "client_id")
    class RegistrationStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kRegistrationNotDone: _ClassVar[MultiClusterManagerConfig.RegistrationStatus]
        kRegistrationInProgress: _ClassVar[MultiClusterManagerConfig.RegistrationStatus]
        kRegistrationCompleted: _ClassVar[MultiClusterManagerConfig.RegistrationStatus]
    kRegistrationNotDone: MultiClusterManagerConfig.RegistrationStatus
    kRegistrationInProgress: MultiClusterManagerConfig.RegistrationStatus
    kRegistrationCompleted: MultiClusterManagerConfig.RegistrationStatus
    class ConnectionStatus(_message.Message):
        __slots__ = ("connected_to_mcm", "error_message")
        CONNECTED_TO_MCM_FIELD_NUMBER: _ClassVar[int]
        ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
        connected_to_mcm: bool
        error_message: str
        def __init__(self, connected_to_mcm: bool = ..., error_message: _Optional[str] = ...) -> None: ...
    REGISTRATION_STATUS_FIELD_NUMBER: _ClassVar[int]
    MCM_CONNECTION_STATUS_FIELD_NUMBER: _ClassVar[int]
    ENABLE_MCM_FIELD_NUMBER: _ClassVar[int]
    MCM_READ_ONLY_FIELD_NUMBER: _ClassVar[int]
    REGISTRATION_ERROR_FIELD_NUMBER: _ClassVar[int]
    REDIRECT_URL_FIELD_NUMBER: _ClassVar[int]
    MCM_URL_FIELD_NUMBER: _ClassVar[int]
    MCM_DATA_URL_FIELD_NUMBER: _ClassVar[int]
    IS_APP_MODE_FIELD_NUMBER: _ClassVar[int]
    LICENSE_ONLY_FIELD_NUMBER: _ClassVar[int]
    SSO_URL_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    registration_status: MultiClusterManagerConfig.RegistrationStatus
    mcm_connection_status: MultiClusterManagerConfig.ConnectionStatus
    enable_mcm: bool
    mcm_read_only: bool
    registration_error: str
    redirect_url: str
    mcm_url: str
    mcm_data_url: str
    is_app_mode: bool
    license_only: bool
    sso_url: str
    client_id: str
    def __init__(self, registration_status: _Optional[_Union[MultiClusterManagerConfig.RegistrationStatus, str]] = ..., mcm_connection_status: _Optional[_Union[MultiClusterManagerConfig.ConnectionStatus, _Mapping]] = ..., enable_mcm: bool = ..., mcm_read_only: bool = ..., registration_error: _Optional[str] = ..., redirect_url: _Optional[str] = ..., mcm_url: _Optional[str] = ..., mcm_data_url: _Optional[str] = ..., is_app_mode: bool = ..., license_only: bool = ..., sso_url: _Optional[str] = ..., client_id: _Optional[str] = ...) -> None: ...

class IdpConfiguration(_message.Message):
    __slots__ = ("idp_service_vec", "version", "last_idp_id", "open_id_service_vec", "oauth_service_vec")
    IDP_SERVICE_VEC_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    LAST_IDP_ID_FIELD_NUMBER: _ClassVar[int]
    OPEN_ID_SERVICE_VEC_FIELD_NUMBER: _ClassVar[int]
    OAUTH_SERVICE_VEC_FIELD_NUMBER: _ClassVar[int]
    idp_service_vec: _containers.RepeatedCompositeFieldContainer[IdpService]
    version: int
    last_idp_id: int
    open_id_service_vec: _containers.RepeatedCompositeFieldContainer[OpenIdService]
    oauth_service_vec: _containers.RepeatedCompositeFieldContainer[OAuthService]
    def __init__(self, idp_service_vec: _Optional[_Iterable[_Union[IdpService, _Mapping]]] = ..., version: _Optional[int] = ..., last_idp_id: _Optional[int] = ..., open_id_service_vec: _Optional[_Iterable[_Union[OpenIdService, _Mapping]]] = ..., oauth_service_vec: _Optional[_Iterable[_Union[OAuthService, _Mapping]]] = ...) -> None: ...

class IdpService(_message.Message):
    __slots__ = ("id", "name", "tenant_id", "sso_url", "issuer_id", "certificate", "certificate_filename", "allow_jit_provisioning", "saml_attribute_name", "allow_local_authentication", "enable", "role_vec", "sign_request", "domain")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    SSO_URL_FIELD_NUMBER: _ClassVar[int]
    ISSUER_ID_FIELD_NUMBER: _ClassVar[int]
    CERTIFICATE_FIELD_NUMBER: _ClassVar[int]
    CERTIFICATE_FILENAME_FIELD_NUMBER: _ClassVar[int]
    ALLOW_JIT_PROVISIONING_FIELD_NUMBER: _ClassVar[int]
    SAML_ATTRIBUTE_NAME_FIELD_NUMBER: _ClassVar[int]
    ALLOW_LOCAL_AUTHENTICATION_FIELD_NUMBER: _ClassVar[int]
    ENABLE_FIELD_NUMBER: _ClassVar[int]
    ROLE_VEC_FIELD_NUMBER: _ClassVar[int]
    SIGN_REQUEST_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    tenant_id: str
    sso_url: str
    issuer_id: str
    certificate: str
    certificate_filename: str
    allow_jit_provisioning: bool
    saml_attribute_name: str
    allow_local_authentication: bool
    enable: bool
    role_vec: _containers.RepeatedScalarFieldContainer[str]
    sign_request: bool
    domain: str
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., tenant_id: _Optional[str] = ..., sso_url: _Optional[str] = ..., issuer_id: _Optional[str] = ..., certificate: _Optional[str] = ..., certificate_filename: _Optional[str] = ..., allow_jit_provisioning: bool = ..., saml_attribute_name: _Optional[str] = ..., allow_local_authentication: bool = ..., enable: bool = ..., role_vec: _Optional[_Iterable[str]] = ..., sign_request: bool = ..., domain: _Optional[str] = ...) -> None: ...

class OpenIdService(_message.Message):
    __slots__ = ("id", "tenant_id", "public_key_url", "polling_frequency_mins", "last_modified_timestamp_usecs", "enable", "domain", "audience_ids")
    ID_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_KEY_URL_FIELD_NUMBER: _ClassVar[int]
    POLLING_FREQUENCY_MINS_FIELD_NUMBER: _ClassVar[int]
    LAST_MODIFIED_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
    ENABLE_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    AUDIENCE_IDS_FIELD_NUMBER: _ClassVar[int]
    id: int
    tenant_id: str
    public_key_url: str
    polling_frequency_mins: int
    last_modified_timestamp_usecs: int
    enable: bool
    domain: str
    audience_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, id: _Optional[int] = ..., tenant_id: _Optional[str] = ..., public_key_url: _Optional[str] = ..., polling_frequency_mins: _Optional[int] = ..., last_modified_timestamp_usecs: _Optional[int] = ..., enable: bool = ..., domain: _Optional[str] = ..., audience_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class OAuthService(_message.Message):
    __slots__ = ("id", "tenant_id", "public_key_url", "polling_frequency_mins", "last_modified_timestamp_usecs", "enable", "domain", "audience_vec")
    ID_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_KEY_URL_FIELD_NUMBER: _ClassVar[int]
    POLLING_FREQUENCY_MINS_FIELD_NUMBER: _ClassVar[int]
    LAST_MODIFIED_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
    ENABLE_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    AUDIENCE_VEC_FIELD_NUMBER: _ClassVar[int]
    id: int
    tenant_id: str
    public_key_url: str
    polling_frequency_mins: int
    last_modified_timestamp_usecs: int
    enable: bool
    domain: str
    audience_vec: _containers.RepeatedCompositeFieldContainer[OAuthAudience]
    def __init__(self, id: _Optional[int] = ..., tenant_id: _Optional[str] = ..., public_key_url: _Optional[str] = ..., polling_frequency_mins: _Optional[int] = ..., last_modified_timestamp_usecs: _Optional[int] = ..., enable: bool = ..., domain: _Optional[str] = ..., audience_vec: _Optional[_Iterable[_Union[OAuthAudience, _Mapping]]] = ...) -> None: ...

class OAuthAudience(_message.Message):
    __slots__ = ("audience_id", "client_id_vec")
    AUDIENCE_ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    audience_id: str
    client_id_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, audience_id: _Optional[str] = ..., client_id_vec: _Optional[_Iterable[str]] = ...) -> None: ...

class Locale(_message.Message):
    __slots__ = ("k_en_us", "k_ja_jp", "k_zh_cn")
    K_EN_US_FIELD_NUMBER: _ClassVar[int]
    K_JA_JP_FIELD_NUMBER: _ClassVar[int]
    K_ZH_CN_FIELD_NUMBER: _ClassVar[int]
    k_en_us: str
    k_ja_jp: str
    k_zh_cn: str
    def __init__(self, k_en_us: _Optional[str] = ..., k_ja_jp: _Optional[str] = ..., k_zh_cn: _Optional[str] = ...) -> None: ...

class TenantMigrationInfo(_message.Message):
    __slots__ = ()
    class Service(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kUnknownService: _ClassVar[TenantMigrationInfo.Service]
        kMagneto: _ClassVar[TenantMigrationInfo.Service]
        kIcebox: _ClassVar[TenantMigrationInfo.Service]
        kYoda: _ClassVar[TenantMigrationInfo.Service]
        kIris: _ClassVar[TenantMigrationInfo.Service]
    kUnknownService: TenantMigrationInfo.Service
    kMagneto: TenantMigrationInfo.Service
    kIcebox: TenantMigrationInfo.Service
    kYoda: TenantMigrationInfo.Service
    kIris: TenantMigrationInfo.Service
    class Action(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kUnknownAction: _ClassVar[TenantMigrationInfo.Action]
        kExport: _ClassVar[TenantMigrationInfo.Action]
        kImport: _ClassVar[TenantMigrationInfo.Action]
        kImportMetadata: _ClassVar[TenantMigrationInfo.Action]
        kPreCheck: _ClassVar[TenantMigrationInfo.Action]
        kQuiesce: _ClassVar[TenantMigrationInfo.Action]
        kUnquiesce: _ClassVar[TenantMigrationInfo.Action]
        kMigrateMetadata: _ClassVar[TenantMigrationInfo.Action]
        kMigrateData: _ClassVar[TenantMigrationInfo.Action]
        kPurgeTenantData: _ClassVar[TenantMigrationInfo.Action]
        kExportMetadataForValidation: _ClassVar[TenantMigrationInfo.Action]
        kImportMetadataForValidation: _ClassVar[TenantMigrationInfo.Action]
        kValidateMetadata: _ClassVar[TenantMigrationInfo.Action]
    kUnknownAction: TenantMigrationInfo.Action
    kExport: TenantMigrationInfo.Action
    kImport: TenantMigrationInfo.Action
    kImportMetadata: TenantMigrationInfo.Action
    kPreCheck: TenantMigrationInfo.Action
    kQuiesce: TenantMigrationInfo.Action
    kUnquiesce: TenantMigrationInfo.Action
    kMigrateMetadata: TenantMigrationInfo.Action
    kMigrateData: TenantMigrationInfo.Action
    kPurgeTenantData: TenantMigrationInfo.Action
    kExportMetadataForValidation: TenantMigrationInfo.Action
    kImportMetadataForValidation: TenantMigrationInfo.Action
    kValidateMetadata: TenantMigrationInfo.Action
    class SupportedServicesInfo(_message.Message):
        __slots__ = ("services",)
        class ServiceInfo(_message.Message):
            __slots__ = ("service_type", "actions_supported")
            SERVICE_TYPE_FIELD_NUMBER: _ClassVar[int]
            ACTIONS_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
            service_type: TenantMigrationInfo.Service
            actions_supported: _containers.RepeatedScalarFieldContainer[TenantMigrationInfo.Action]
            def __init__(self, service_type: _Optional[_Union[TenantMigrationInfo.Service, str]] = ..., actions_supported: _Optional[_Iterable[_Union[TenantMigrationInfo.Action, str]]] = ...) -> None: ...
        SERVICES_FIELD_NUMBER: _ClassVar[int]
        services: _containers.RepeatedCompositeFieldContainer[TenantMigrationInfo.SupportedServicesInfo.ServiceInfo]
        def __init__(self, services: _Optional[_Iterable[_Union[TenantMigrationInfo.SupportedServicesInfo.ServiceInfo, _Mapping]]] = ...) -> None: ...
    def __init__(self) -> None: ...
