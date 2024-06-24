# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: configs/node_config.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19\x63onfigs/node_config.proto\x12\x10\x63ohesity.configs\"\xac\x99\x01\n\x0fNodeConfigProto\x12)\n\x0c\x64\x61ta_dirpath\x18\x01 \x01(\t:\x13/home/cohesity/data\x12:\n\x10node_id_filepath\x18\x02 \x01(\t: /home/cohesity/data/node_id.json\x12@\n\x13\x63luster_id_filepath\x18\x03 \x01(\t:#/home/cohesity/data/cluster_id.json\x12\x31\n\x10software_dirpath\x18\x04 \x01(\t:\x17/home/cohesity/software\x12\x38\n\x0fgandalf_dirpath\x18\x05 \x01(\t:\x1f/home/cohesity/gandalf_software\x12\x32\n\x1agandalf_constituent_id_key\x18\x06 \x01(\t:\x0e\x63onstituent_id\x12,\n\x17gandalf_metadata_id_key\x18\x07 \x01(\t:\x0bmetadata_id\x12*\n\x12\x63luster_config_key\x18\t \x01(\t:\x0e\x63luster_config\x12<\n\x10packages_dirpath\x18\n \x01(\t:\"/home/cohesity/data/nexus/packages\x12,\n\x13services_gflags_key\x18\x0b \x01(\t:\x0fservices_gflags\x12,\n\x13ssl_certificate_key\x18\x0c \x01(\t:\x0fssl_certificate\x12/\n disk_mounts_parent_relative_path\x18\r \x01(\t:\x05\x64isks\x12*\n\x10\x64isk_config_name\x18\x0e \x01(\t:\x10\x64isk_config.json\x12(\n\x18\x61pollo_dir_relative_path\x18\x0f \x01(\t:\x06\x61pollo\x12<\n\"chunk_repository_dir_relative_path\x18\x10 \x01(\t:\x10\x63hunk_repository\x12&\n\x17hydra_dir_relative_path\x18\x11 \x01(\t:\x05hydra\x12(\n\x18scribe_dir_relative_path\x18\x12 \x01(\t:\x06scribe\x12$\n\x16yoda_dir_relative_path\x18\x13 \x01(\t:\x04yoda\x12\x34\n\x19\x65lasticsearch_config_file\x18\x14 \x01(\t:\x11\x65lasticsearch.yml\x12\x45\n\"elasticsearch_script_relative_path\x18\x15 \x01(\t:\x19\x63rux/bin/elasticsearch.sh\x12G\n#reverse_tunnel_script_relative_path\x18\x16 \x01(\t:\x1a\x63rux/bin/reverse_tunnel.sh\x12(\n\x15gandalf_alerts_id_key\x18\x17 \x01(\t:\talerts_id\x12\x30\n\x13scribe_table_id_key\x18\x18 \x01(\t:\x13scribe_table_id_key\x12\"\n\x0eiris_users_key\x18\x19 \x01(\t:\niris_users\x12\x38\n\x19\x63luster_create_status_key\x18\x1a \x01(\t:\x15\x63luster_create_status\x12W\n+clear_old_mount_points_script_relative_path\x18\x1b \x01(\t:\"crux/bin/clear_old_mount_points.sh\x12Y\n,elasticsearch_kill_busy_script_relative_path\x18\x1c \x01(\t:#crux/bin/elasticsearch_kill_busy.sh\x12\x30\n\x1cyoda_slave_dir_relative_path\x18\x1d \x01(\t:\nyoda_slave\x12\x42\n\x1c\x63luster_has_new_packages_key\x18\x1e \x01(\t:\x1c\x63luster_has_new_packages_key\x12\x42\n\x11hardware_filepath\x18\x1f \x01(\t:\'/home/cohesity/data/nexus/hardware.json\x12*\n\x12mr_metadata_id_key\x18  \x01(\t:\x0emr_metadata_id\x12\x35\n\x1arhino_script_relative_path\x18! \x01(\t:\x11\x63rux/bin/rhino.sh\x12j\n,nearline_adapter_ssl_validator_relative_path\x18\" \x01(\t:4crux/conf/vault/google_ssl_certificate_validator.pem\x12Z\n\x1b\x63luster_bringup_status_path\x18$ \x01(\t:5/home/cohesity/data/nexus/cluster_bringup_status.json\x12\x42\n\x17software_config_dirpath\x18% \x01(\t:!/home/cohesity/software/crux/conf\x12T\n software_platform_config_dirpath\x18& \x01(\t:*/home/cohesity/software/crux/conf/platform\x12>\n\x14software_bin_dirpath\x18\' \x01(\t: /home/cohesity/software/crux/bin\x12L\n\x16\x64isk_location_filepath\x18( \x01(\t:,/home/cohesity/data/nexus/disk_location.json\x12P\n\x18\x66ree_node_alert_filepath\x18) \x01(\t:./home/cohesity/data/nexus/free_node_alert.json\x12J\n\x15memory_limit_filepath\x18* \x01(\t:+/home/cohesity/data/nexus/memory_limit.json\x12Q\n\x1bnotify_disk_change_filepath\x18+ \x01(\t:,/home/cohesity/data/nexus/notify_disk_change\x12I\n\x15nic_port_map_filepath\x18, \x01(\t:*/home/cohesity/data/nexus/nic_portmap.json\x12g\n&node_software_version_history_filepath\x18- \x01(\t:7/home/cohesity/data/nexus/software_version_history.json\x12&\n\x10\x66\x65\x61ture_list_key\x18. \x01(\t:\x0c\x66\x65\x61ture_list\x12\x1e\n\x0f\x61\x64min_user_name\x18/ \x01(\t:\x05\x61\x64min\x12\x14\n\tadmin_rid\x18\x30 \x01(\x05:\x01\x31\x12\"\n\x13\x64\x65\x66\x61ult_domain_name\x18\x31 \x01(\t:\x05LOCAL\x12 \n\x12iris_relative_path\x18\x32 \x01(\t:\x04iris\x12&\n\x15private_key_file_name\x18\x33 \x01(\t:\x07key.pem\x12$\n\rscheduler_key\x18\x34 \x01(\t:\rscheduler_key\x12%\n\x08logs_dir\x18\x35 \x01(\t:\x13/home/cohesity/logs\x12$\n\x0firis_master_key\x18\x36 \x01(\t:\x0biris_master\x12.\n\x1blibrarian_dir_relative_path\x18\x37 \x01(\t:\tlibrarian\x12&\n\x17groot_dir_relative_path\x18\x38 \x01(\t:\x05groot\x12\x32\n\x16scribe_view_config_key\x18\x39 \x01(\t:\x12scribe_view_config\x12i\n\'zero_metadata_fault_tolerance_file_path\x18: \x01(\t:8/home/cohesity/data/zero_metadata_fault_tolerance_marker\x12\x43\n!luceneserver_script_relative_path\x18; \x01(\t:\x18\x63rux/bin/luceneserver.sh\x12/\n\x17\x64\x62_script_relative_path\x18< \x01(\t:\x0e\x63rux/bin/db.sh\x12\x38\n\"reporting_schema_dir_relative_path\x18= \x01(\t:\x0c\x63rux/schema/\x12K\n\x1dinterface_link_state_filepath\x18? \x01(\t:$/home/cohesity/data/nexus/link_state\x12\x42\n\x13\x65\x61gle_agent_dirpath\x18@ \x01(\t:%/home/cohesity/data/nexus/eagle_agent\x12N\n!tricorder_data_dirpath_deprecated\x18\x41 \x01(\t:#/home/cohesity/data/nexus/tricorder\x12j\n\x1c\x61thena_app_downloads_dirpath\x18\x42 \x01(\t:D/home/cohesity/data/athena/mounts/_internal_view_mount/app_downloads\x12N\n\x17network_config_filepath\x18\x44 \x01(\t:-/home/cohesity/data/nexus/network_config.json\x12@\n cached_services_gflags_file_name\x18\x45 \x01(\t:\x16\x63\x61\x63hed_services_gflags\x12+\n\x10helios_agent_key\x18\x46 \x01(\t:\x11helios_agent_data\x12\x39\n\x1coptimus_script_relative_path\x18G \x01(\t:\x13\x63rux/bin/optimus.sh\x12>\n gandalf_antivirus_service_id_key\x18H \x01(\t:\x14\x61ntivirus_service_id\x12*\n\x19\x62ifrost_dir_relative_path\x18I \x01(\t:\x07\x62ifrost\x12k\n&selinux_avc_denials_chkpoint_file_path\x18J \x01(\t:;/home/cohesity/data/nexus/selinux_avc_denials_chkpoint.json\x12U\n\x1enexus_proxy_vip_epoch_filepath\x18K \x01(\t:-/home/cohesity/data/nexus_proxy/vip_epoch.bin\x12W\n\"athena_ephemeral_volumes_base_path\x18L \x01(\t:+/home/cohesity/data/athena/mounts/ephemeral\x12K\n\x1bssl_validator_relative_path\x18M \x01(\t:&crux/conf/connectors/certs/cacerts.pem\x12(\n\x18\x65lrond_dir_relative_path\x18N \x01(\t:\x06\x65lrond\x12\x37\n$nfsshare_mounts_parent_relative_path\x18O \x01(\t:\tnfsshares\x12[\n notify_nfs_mount_change_filepath\x18Q \x01(\t:1/home/cohesity/data/nexus/notify_nfs_mount_change\x12(\n\x18\x62ridge_dir_relative_path\x18R \x01(\t:\x06\x62ridge\x12I\n&bridge_nfs_auth_kerberos_relative_path\x18\x8d\x02 \x01(\t:\x18\x62ridge/nfs/auth/kerberos\x12@\n\'elrond_tracked_io_log_dir_relative_path\x18S \x01(\t:\x0ftracked_io_logs\x12\x33\n elrond_binary_logger_file_prefix\x18T \x01(\t:\tio_traces\x12\x61\n!ntp_freq_error_chkpoint_file_path\x18U \x01(\t:6/home/cohesity/data/nexus/ntp_freq_error_chkpoint.json\x12\x34\n\x17\x65lrond_access_model_key\x18V \x01(\t:\x13\x65lrond_access_model\x12,\n\x1aheimdall_dir_relative_path\x18W \x01(\t:\x08heimdall\x12\x65\n#avc_denial_error_chkpoint_file_path\x18X \x01(\t:8/home/cohesity/data/nexus/avc_denial_error_chkpoint.json\x12\\\n\x1eremote_storage_config_filepath\x18Z \x01(\t:4/home/cohesity/data/nexus/remote_storage_config.json\x12\x1d\n\x10os_util_min_port\x18\x64 \x01(\x05:\x03\x31\x30\x30\x12L\n patch_nodes_script_relative_path\x18\x65 \x01(\t:\"crux/patch/bin/patch_added_node.sh\x12&\n\x17patch_dir_relative_path\x18\x66 \x01(\t:\x05patch\x12\"\n\x0epatch_logs_dir\x18g \x01(\t:\npatch/logs\x12,\n\x14imported_patches_dir\x18h \x01(\t:\x0epatch/imported\x12.\n\x15\x61vailable_patches_dir\x18j \x01(\t:\x0fpatch/available\x12*\n\x13\x61pplied_patches_dir\x18k \x01(\t:\rpatch/applied\x12%\n\rpatch_bin_dir\x18l \x01(\t:\x0e\x63rux/patch/bin\x12#\n\x12\x61\x63tive_patches_dir\x18m \x01(\t:\x07patches\x12\x1a\n\nhotfix_dir\x18n \x01(\t:\x06hotfix\x12(\n\x11patch_configs_dir\x18o \x01(\t:\rpatch/configs\x12;\n\x14teleport_script_path\x18p \x01(\t:\x1d\x63rux/bin/teleport/teleport.py\x12?\n\x1f\x65tl_server_script_relative_path\x18q \x01(\t:\x16\x63rux/bin/etl_server.sh\x12\x45\n!offline_alerts_file_relative_path\x18r \x01(\t:\x1a\x61lerts/offline_alerts.json\x12\x1a\n\x0eiris_http_port\x18P \x01(\x05:\x02\x38\x30\x12\x1d\n\x0firis_https_port\x18\xbb\x03 \x01(\x05:\x03\x34\x34\x33\x12\x19\n\x0bsmbrpc_port\x18\xbd\x03 \x01(\x05:\x03\x34\x34\x35\x12\x1e\n\x0fnfs_sunrpc_port\x18\x81\x10 \x01(\x05:\x04\x32\x30\x34\x39\x12\x16\n\x07s3_port\x18\xb8\x17 \x01(\x05:\x04\x33\x30\x30\x30\x12\x19\n\nswift_port\x18\xb9\x17 \x01(\x05:\x04\x33\x30\x30\x31\x12\x19\n\niscsi_port\x18\xbc\x19 \x01(\x05:\x04\x33\x32\x36\x30\x12\x1a\n\x0bovn_nb_port\x18\xf1\x33 \x01(\x05:\x04\x36\x36\x34\x31\x12\x1a\n\x0bovn_sb_port\x18\xf2\x33 \x01(\x05:\x04\x36\x36\x34\x32\x12\x1f\n\x10ovn_nb_raft_port\x18\xf3\x33 \x01(\x05:\x04\x36\x36\x34\x33\x12\x1f\n\x10ovn_sb_raft_port\x18\xf4\x33 \x01(\x05:\x04\x36\x36\x34\x34\x12 \n\x11spire_server_port\x18\x91? \x01(\x05:\x04\x38\x30\x38\x31\x12$\n\x15spire_federation_port\x18\xfb\x41 \x01(\x05:\x04\x38\x34\x34\x33\x12\"\n\x13\x61thena_flannel_port\x18\xdd@ \x01(\x05:\x04\x38\x32\x38\x35\x12(\n\x19\x61thena_flannel_vxlan_port\x18\x98\x42 \x01(\x05:\x04\x38\x34\x37\x32\x12)\n\x1a\x61thena_flannel2_vxlan_port\x18\x99\x42 \x01(\x05:\x04\x38\x34\x37\x33\x12\x19\n\nsiren_port\x18\x97G \x01(\x05:\x04\x39\x31\x31\x31\x12 \n\x10os_util_max_port\x18\x90N \x01(\x05:\x05\x31\x30\x30\x30\x30\x12\x1b\n\x0b\x62ridge_port\x18\xe7V \x01(\x05:\x05\x31\x31\x31\x31\x31\x12\x1a\n\nhydra_port\x18\xe8V \x01(\x05:\x05\x31\x31\x31\x31\x32\x12\x30\n bridge_insecure_grpc_server_port\x18\xe9V \x01(\x05:\x05\x31\x31\x31\x31\x33\x12\'\n\x17\x62ridge_pigeon_grpc_port\x18\xeaV \x01(\x05:\x05\x31\x31\x31\x31\x34\x12 \n\x10vault_proxy_port\x18\xebV \x01(\x05:\x05\x31\x31\x31\x31\x35\x12!\n\x11\x62ridge_proxy_port\x18\xecV \x01(\x05:\x05\x31\x31\x31\x31\x36\x12.\n\x1e\x62ridge_secure_grpc_server_port\x18\xedV \x01(\x05:\x05\x31\x31\x31\x31\x37\x12\x1b\n\x0bmadrox_port\x18\xcbW \x01(\x05:\x05\x31\x31\x32\x31\x31\x12*\n\x1a\x62ridge_secondary_http_port\x18\xeeV \x01(\x05:\x05\x31\x31\x31\x31\x38\x12\x1e\n\x0enewscribe_port\x18\xbe_ \x01(\x05:\x05\x31\x32\x32\x32\x32\x12#\n\x13newscribe_port_last\x18\x8b` \x01(\x05:\x05\x31\x32\x32\x39\x39\x12\x1d\n\rrtclient_port\x18\xa1` \x01(\x05:\x05\x31\x32\x33\x32\x31\x12\x1b\n\x0bscribe_port\x18\xb9` \x01(\x05:\x05\x31\x32\x33\x34\x35\x12\x1d\n\x0cmagneto_port\x18\xa0\x9c\x01 \x01(\x05:\x05\x32\x30\x30\x30\x30\x12*\n\x19magneto_read_replica_port\x18\xab\x9c\x01 \x01(\x05:\x05\x32\x30\x30\x31\x31\x12-\n\x1cmagneto_api_server_grpc_port\x18\x88\xa4\x01 \x01(\x05:\x05\x32\x31\x30\x30\x30\x12#\n\x12storage_proxy_port\x18\xa1\x9c\x01 \x01(\x05:\x05\x32\x30\x30\x30\x31\x12\x1f\n\x0esmb_proxy_port\x18\xa2\x9c\x01 \x01(\x05:\x05\x32\x30\x30\x30\x32\x12$\n\x13smb_proxy_http_port\x18\xa3\x9c\x01 \x01(\x05:\x05\x32\x30\x30\x30\x33\x12\x1f\n\x0e\x61tom_grpc_port\x18\xa4\x9c\x01 \x01(\x05:\x05\x32\x30\x30\x30\x34\x12\x1a\n\tatom_port\x18\xa5\x9c\x01 \x01(\x05:\x05\x32\x30\x30\x30\x35\x12#\n\x12\x61tom_protorpc_port\x18\xfc\xbe\x01 \x01(\x05:\x05\x32\x34\x34\x34\x34\x12 \n\x0fsmb2_proxy_port\x18\xa6\x9c\x01 \x01(\x05:\x05\x32\x30\x30\x30\x36\x12%\n\x14smb2_proxy_http_port\x18\xa7\x9c\x01 \x01(\x05:\x05\x32\x30\x30\x30\x37\x12\x1f\n\x0ethrottler_port\x18\xa8\x9c\x01 \x01(\x05:\x05\x32\x30\x30\x30\x38\x12\x1f\n\x0enfs_proxy_port\x18\xa9\x9c\x01 \x01(\x05:\x05\x32\x30\x30\x30\x39\x12$\n\x13nfs_proxy_http_port\x18\xaa\x9c\x01 \x01(\x05:\x05\x32\x30\x30\x31\x30\x12\x1c\n\x0b\x61lerts_port\x18\xf7\xa4\x01 \x01(\x05:\x05\x32\x31\x31\x31\x31\x12\x1e\n\rkeychain_port\x18\xf0\xab\x01 \x01(\x05:\x05\x32\x32\x30\x30\x30\x12\x1d\n\x0cgandalf_port\x18\xce\xad\x01 \x01(\x05:\x05\x32\x32\x32\x32\x32\x12\"\n\x11gandalf_grpc_port\x18\xcf\xad\x01 \x01(\x05:\x05\x32\x32\x32\x32\x33\x12\x1c\n\x0bpigeon_port\x18\xa5\xb6\x01 \x01(\x05:\x05\x32\x33\x33\x33\x33\x12\'\n\x16\x62ridge_pigeon_tls_port\x18\xa7\xb6\x01 \x01(\x05:\x05\x32\x33\x33\x33\x35\x12&\n\x15pigeon_alternate_port\x18\xa6\xb6\x01 \x01(\x05:\x05\x32\x33\x33\x33\x34\x12!\n\x10nexus_pprof_port\x18\x9f\xb7\x01 \x01(\x05:\x05\x32\x33\x34\x35\x35\x12\x1b\n\nnexus_port\x18\xa0\xb7\x01 \x01(\x05:\x05\x32\x33\x34\x35\x36\x12!\n\x10nexus_proxy_port\x18\xa1\xb7\x01 \x01(\x05:\x05\x32\x33\x34\x35\x37\x12\"\n\x11nexus_secure_port\x18\xa8\xb7\x01 \x01(\x05:\x05\x32\x33\x34\x36\x34\x12*\n\x19tricorder_port_deprecated\x18\xa2\xb7\x01 \x01(\x05:\x05\x32\x33\x34\x35\x38\x12\x1b\n\nre_ip_port\x18\xa3\xb7\x01 \x01(\x05:\x05\x32\x33\x34\x35\x39\x12!\n\x10\x65\x61gle_agent_port\x18\xa4\xb7\x01 \x01(\x05:\x05\x32\x33\x34\x36\x30\x12\"\n\x11re_ip_socket_port\x18\xa5\xb7\x01 \x01(\x05:\x05\x32\x33\x34\x36\x31\x12#\n\x12mcmetl_server_port\x18\xa6\xb7\x01 \x01(\x05:\x05\x32\x33\x34\x36\x32\x12\x1f\n\x0elicensing_port\x18\xa7\xb7\x01 \x01(\x05:\x05\x32\x33\x34\x36\x33\x12$\n\x13olympus_server_port\x18\xae\xb7\x01 \x01(\x05:\x05\x32\x33\x34\x37\x30\x12 \n\x0firis_proxy_port\x18\xf7\xbf\x01 \x01(\x05:\x05\x32\x34\x35\x36\x37\x12\x1c\n\x0b\x61pollo_port\x18\xe8\xc0\x01 \x01(\x05:\x05\x32\x34\x36\x38\x30\x12!\n\x10\x61pollo_grpc_port\x18\xe9\xc0\x01 \x01(\x05:\x05\x32\x34\x36\x38\x31\x12\x1d\n\x0c\x63ompass_port\x18\xd3\xc7\x01 \x01(\x05:\x05\x32\x35\x35\x35\x35\x12\x1b\n\nstats_port\x18\xde\xc7\x01 \x01(\x05:\x05\x32\x35\x35\x36\x36\x12 \n\x0fpulse_grpc_port\x18\xdf\xc7\x01 \x01(\x05:\x05\x32\x35\x35\x36\x37\x12\x1a\n\tgaia_port\x18\xe9\xc7\x01 \x01(\x05:\x05\x32\x35\x35\x37\x37\x12\x1f\n\x0egaia_grpc_port\x18\xea\xc7\x01 \x01(\x05:\x05\x32\x35\x35\x37\x38\x12\x32\n!athena_kube_scheduler_secure_port\x18\xe2\xc7\x01 \x01(\x05:\x05\x32\x35\x35\x37\x30\x12\x33\n\"athena_kube_controller_secure_port\x18\xe3\xc7\x01 \x01(\x05:\x05\x32\x35\x35\x37\x31\x12/\n\x1e\x61thena_kube_proxy_healthz_port\x18\xe4\xc7\x01 \x01(\x05:\x05\x32\x35\x35\x37\x32\x12/\n\x1e\x61thena_kube_proxy_metrics_port\x18\xe5\xc7\x01 \x01(\x05:\x05\x32\x35\x35\x37\x33\x12,\n\x1b\x61thena_kubelet_healthz_port\x18\xe6\xc7\x01 \x01(\x05:\x05\x32\x35\x35\x37\x34\x12\x33\n\"athena_kube_scheduler_healthz_port\x18\xe7\xc7\x01 \x01(\x05:\x05\x32\x35\x35\x37\x35\x12\'\n\x16nexus_envoy_admin_port\x18\xcd\xc8\x01 \x01(\x05:\x05\x32\x35\x36\x37\x37\x12\x38\n\'nexus_service_identity_outbound_handler\x18\xce\xc8\x01 \x01(\x05:\x05\x32\x35\x36\x37\x38\x12\x37\n&nexus_service_identity_inbound_handler\x18\xcf\xc8\x01 \x01(\x05:\x05\x32\x35\x36\x37\x39\x12$\n\x13statscollector_port\x18\xd0\xc8\x01 \x01(\x05:\x05\x32\x35\x36\x38\x30\x12\x1c\n\x0b\x61thena_port\x18\xd1\xc8\x01 \x01(\x05:\x05\x32\x35\x36\x38\x31\x12,\n\x1b\x61thena_docker_registry_port\x18\xd2\xc8\x01 \x01(\x05:\x05\x32\x35\x36\x38\x32\x12\x1d\n\x0coptimus_port\x18\xd3\xc8\x01 \x01(\x05:\x05\x32\x35\x36\x38\x33\x12\x32\n!athena_proxy_docker_registry_port\x18\xd4\xc8\x01 \x01(\x05:\x05\x32\x35\x36\x38\x34\x12-\n\x1c\x61thena_proxy_api_server_port\x18\xd5\xc8\x01 \x01(\x05:\x05\x32\x35\x36\x38\x35\x12)\n\x18\x61thena_proxy_config_port\x18\xd6\xc8\x01 \x01(\x05:\x05\x32\x35\x36\x38\x36\x12(\n\x17\x61thena_etcd_client_port\x18\xd7\xc8\x01 \x01(\x05:\x05\x32\x35\x36\x38\x37\x12&\n\x15\x61thena_etcd_peer_port\x18\xd8\xc8\x01 \x01(\x05:\x05\x32\x35\x36\x38\x38\x12\x36\n%athena_kubernetes_apiserver_http_port\x18\xd9\xc8\x01 \x01(\x05:\x05\x32\x35\x36\x38\x39\x12-\n\x1c\x61thena_kubelet_cadvisor_port\x18\xda\xc8\x01 \x01(\x05:\x05\x32\x35\x36\x39\x30\x12*\n\x19\x61thena_kubelet_https_port\x18\xdb\xc8\x01 \x01(\x05:\x05\x32\x35\x36\x39\x31\x12$\n\x13\x61thena_coredns_port\x18\xdc\xc8\x01 \x01(\x05:\x05\x32\x35\x36\x39\x32\x12+\n\x1a\x61thena_coredns_health_port\x18\xdd\xc8\x01 \x01(\x05:\x05\x32\x35\x36\x39\x33\x12\"\n\x11\x61thena_proxy_port\x18\xde\xc8\x01 \x01(\x05:\x05\x32\x35\x36\x39\x34\x12+\n\x1a\x61thena_proxy_internal_port\x18\xdf\xc8\x01 \x01(\x05:\x05\x32\x35\x36\x39\x35\x12\x37\n&athena_kubernetes_apiserver_https_port\x18\xe0\xc8\x01 \x01(\x05:\x05\x32\x35\x36\x39\x36\x12%\n\x14\x61thena_watchdog_port\x18\xe1\xc8\x01 \x01(\x05:\x05\x32\x35\x36\x39\x37\x12%\n\x14\x65tl_server_grpc_port\x18\xe2\xc8\x01 \x01(\x05:\x05\x32\x35\x36\x39\x38\x12\x35\n$athena_sys_srvc_docker_registry_port\x18\xe3\xc8\x01 \x01(\x05:\x05\x32\x35\x36\x39\x39\x12\'\n\x16\x65lasticsearch_min_port\x18\xe4\xc8\x01 \x01(\x05:\x05\x32\x35\x37\x30\x30\x12\'\n\x16\x65lasticsearch_max_port\x18\xc8\xc9\x01 \x01(\x05:\x05\x32\x35\x38\x30\x30\x12\x32\n!elasticsearch_node_discovery_port\x18\xc9\xc9\x01 \x01(\x05:\x05\x32\x35\x38\x30\x31\x12\x33\n\"helios_onprem_docker_registry_port\x18\xca\xc9\x01 \x01(\x05:\x05\x32\x35\x38\x30\x32\x12/\n\x1ehelios_onprem_etcd_client_port\x18\xcb\xc9\x01 \x01(\x05:\x05\x32\x35\x38\x30\x33\x12-\n\x1chelios_onprem_etcd_peer_port\x18\xcc\xc9\x01 \x01(\x05:\x05\x32\x35\x38\x30\x34\x12-\n\x1chelios_onprem_iris_http_port\x18\x97\xca\x01 \x01(\x05:\x05\x32\x35\x38\x37\x39\x12.\n\x1dhelios_onprem_iris_https_port\x18\x98\xca\x01 \x01(\x05:\x05\x32\x35\x38\x38\x30\x12\x1b\n\nrhino_port\x18\x8e\xcb\x01 \x01(\x05:\x05\x32\x35\x39\x39\x38\x12\x1a\n\tyoda_port\x18\x8f\xcb\x01 \x01(\x05:\x05\x32\x35\x39\x39\x39\x12\x1f\n\x0elibrarian_port\x18\x90\xcb\x01 \x01(\x05:\x05\x32\x36\x30\x30\x30\x12\"\n\x11luceneserver_port\x18\x91\xcb\x01 \x01(\x05:\x05\x32\x36\x30\x30\x31\x12\x1c\n\x0b\x65lrond_port\x18\x92\xcb\x01 \x01(\x05:\x05\x32\x36\x30\x30\x32\x12\x1e\n\rheimdall_port\x18\xd8\xcc\x01 \x01(\x05:\x05\x32\x36\x32\x30\x30\x12 \n\x0fyoda_agent_port\x18\xa5\xd0\x01 \x01(\x05:\x05\x32\x36\x36\x36\x31\x12%\n\x14yoda_agent_http_port\x18\xa6\xd0\x01 \x01(\x05:\x05\x32\x36\x36\x36\x32\x12$\n\x13opensearch_min_port\x18\xa7\xd0\x01 \x01(\x05:\x05\x32\x36\x36\x36\x33\x12$\n\x13opensearch_max_port\x18\xcc\xd0\x01 \x01(\x05:\x05\x32\x36\x37\x30\x30\x12\x1b\n\ngroot_port\x18\xf7\xd2\x01 \x01(\x05:\x05\x32\x36\x39\x39\x39\x12%\n\x14report_database_port\x18\xdf\xda\x01 \x01(\x05:\x05\x32\x37\x39\x39\x39\x12#\n\x12report_server_port\x18\xc7\xe2\x01 \x01(\x05:\x05\x32\x38\x39\x39\x39\x12!\n\x12node_exporter_port\x18\x8cG \x01(\x05:\x04\x39\x31\x30\x30\x12%\n\x14\x62roker_services_port\x18\xa6\xea\x01 \x01(\x05:\x05\x32\x39\x39\x39\x30\x12$\n\x13\x62roker_bifrost_port\x18\xa7\xea\x01 \x01(\x05:\x05\x32\x39\x39\x39\x31\x12!\n\x10\x62roker_http_port\x18\xa8\xea\x01 \x01(\x05:\x05\x32\x39\x39\x39\x32\x12;\n%socks_server_broker_listen_port_range\x18\x98u \x01(\t:\x0b\x31\x35\x30\x30\x30-17000\x12\x35\n\x1erigel_local_bridge_ports_range\x18\xdc\x88\x01 \x01(\t:\x0b\x31\x37\x35\x30\x30-17600\x12\"\n\x11\x62ifrost_http_port\x18\xaa\xea\x01 \x01(\x05:\x05\x32\x39\x39\x39\x34\x12&\n\x15socks_grpc_proxy_port\x18\xad\xea\x01 \x01(\x05:\x05\x32\x39\x39\x39\x37\x12&\n\x15socks_grpc_agent_port\x18\xae\xea\x01 \x01(\x05:\x05\x32\x39\x39\x39\x38\x12\x1c\n\x0bicebox_port\x18\xaf\xea\x01 \x01(\x05:\x05\x32\x39\x39\x39\x39\x12 \n\x0fpatch_exec_port\x18\xb0\xea\x01 \x01(\x05:\x05\x33\x30\x30\x30\x30\x12!\n\x10testing_min_port\x18\xb1\xea\x01 \x01(\x05:\x05\x33\x30\x30\x30\x31\x12!\n\x10testing_max_port\x18\xf4\xfd\x01 \x01(\x05:\x05\x33\x32\x35\x30\x30\x12#\n\x12\x65phemeral_min_port\x18\xa6\xff\x01 \x01(\x05:\x05\x33\x32\x37\x36\x38\x12#\n\x12\x65phemeral_max_port\x18\xc8\xdc\x03 \x01(\x05:\x05\x36\x31\x30\x30\x30\x12-\n\x1c\x61thena_min_dynamic_node_port\x18\xc9\xdc\x03 \x01(\x05:\x05\x36\x31\x30\x30\x31\x12-\n\x1c\x61thena_max_dynamic_node_port\x18\x98\xf2\x03 \x01(\x05:\x05\x36\x33\x37\x36\x38\x12,\n\x1b\x61thena_min_static_node_port\x18\x99\xf2\x03 \x01(\x05:\x05\x36\x33\x37\x36\x39\x12,\n\x1b\x61thena_max_static_node_port\x18\x80\xf4\x03 \x01(\x05:\x05\x36\x34\x30\x30\x30\x12!\n\x10\x65lixir_http_port\x18\x9a\xf2\x03 \x01(\x05:\x05\x36\x33\x37\x37\x30\x12 \n\x0fvulscanner_port\x18\x9b\xf2\x03 \x01(\x05:\x05\x36\x33\x37\x37\x31\x12\"\n\x11\x62ootstrapper_port\x18\x9c\xf2\x03 \x01(\x05:\x05\x36\x33\x37\x37\x32\x12$\n\x13kube_dashboard_port\x18\x9d\xf2\x03 \x01(\x05:\x05\x36\x33\x37\x37\x33\x12!\n\x10testservice_port\x18\x9e\xf2\x03 \x01(\x05:\x05\x36\x33\x37\x37\x34\x12\x19\n\x08\x64lp_port\x18\x9f\xf2\x03 \x01(\x05:\x05\x36\x33\x37\x37\x35\x12&\n\x15\x65venting_service_port\x18\xa0\xf2\x03 \x01(\x05:\x05\x36\x33\x37\x37\x36\x12 \n\x0fprometheus_port\x18\xa1\xf2\x03 \x01(\x05:\x05\x36\x33\x37\x37\x37\x12\x1b\n\nkafka_port\x18\xa2\xf2\x03 \x01(\x05:\x05\x36\x33\x37\x37\x38\x12\'\n\x16\x61gentinstall_http_port\x18\xa3\xf2\x03 \x01(\x05:\x05\x36\x33\x37\x37\x39\x12!\n\x10imanis_grpc_port\x18\xa4\xf2\x03 \x01(\x05:\x05\x36\x33\x37\x38\x30\x12-\n\x1cimanis_resource_manager_port\x18\xa5\xf2\x03 \x01(\x05:\x05\x36\x33\x37\x38\x31\x12)\n\x18imanis_node_manager_port\x18\xa6\xf2\x03 \x01(\x05:\x05\x36\x33\x37\x38\x32\x12+\n\x1aworkqueue_server_grpc_port\x18\xa7\xf2\x03 \x01(\x05:\x05\x36\x33\x37\x38\x33\x12+\n\x1aworkqueue_server_http_port\x18\xa8\xf2\x03 \x01(\x05:\x05\x36\x33\x37\x38\x34\x12+\n\x1ametadata_service_grpc_port\x18\xa9\xf2\x03 \x01(\x05:\x05\x36\x33\x37\x38\x35\x12\x1f\n\x0e\x61rgus_app_port\x18\xaa\xf2\x03 \x01(\x05:\x05\x36\x33\x37\x38\x36\x12 \n\x0fmagnus_api_port\x18\xab\xf2\x03 \x01(\x05:\x05\x36\x33\x37\x38\x37\x12/\n\x1emagnus_server_grpc_server_port\x18\xac\xf2\x03 \x01(\x05:\x05\x36\x33\x37\x38\x38\x12/\n\x1emagnus_server_http_server_port\x18\xad\xf2\x03 \x01(\x05:\x05\x36\x33\x37\x38\x39\x12.\n\x1dmagnus_actor_http_server_port\x18\xae\xf2\x03 \x01(\x05:\x05\x36\x33\x37\x39\x30\x12\x1d\n\x0cods_app_port\x18\xaf\xf2\x03 \x01(\x05:\x05\x36\x33\x37\x39\x31\x12.\n\x1dsheltered_harbor_control_port\x18\xb0\xf2\x03 \x01(\x05:\x05\x36\x33\x37\x39\x32\x12\x34\n#sheltered_harbor_data_preparer_port\x18\xb1\xf2\x03 \x01(\x05:\x05\x36\x33\x37\x39\x33\x12/\n\x1esheltered_harbor_restorer_port\x18\xb2\xf2\x03 \x01(\x05:\x05\x36\x33\x37\x39\x34\x12\x1e\n\rsftp_app_port\x18\xb3\xf2\x03 \x01(\x05:\x05\x36\x33\x37\x39\x35\x12#\n\x12sftp_rest_app_port\x18\xb4\xf2\x03 \x01(\x05:\x05\x36\x33\x37\x39\x36\x12\x1d\n\x11routing_ospf_port\x18Y \x01(\x05:\x02\x38\x39\x12\x1e\n\x10routing_bgp_port\x18\xb3\x01 \x01(\x05:\x03\x31\x37\x39\x12\x1e\n\x10routing_rip_port\x18\x88\x04 \x01(\x05:\x03\x35\x32\x30\x12\x1b\n\njanus_port\x18\x81\xf4\x03 \x01(\x05:\x05\x36\x34\x30\x30\x31\x12 \n\x0fpushclient_port\x18\x82\xf4\x03 \x01(\x05:\x05\x36\x34\x30\x30\x32\x12\x1b\n\naegis_port\x18\x83\xf4\x03 \x01(\x05:\x05\x36\x34\x30\x30\x33\x12\x36\n%resource_manager_api_server_grpc_port\x18\x85\xf4\x03 \x01(\x05:\x05\x36\x34\x30\x30\x35\x12\x32\n!elasticsearch_system_service_port\x18\x86\xf4\x03 \x01(\x05:\x05\x36\x34\x30\x30\x36\x12<\n+elasticsearch_system_service_transport_port\x18\x87\xf4\x03 \x01(\x05:\x05\x36\x34\x30\x30\x37\x12\x33\n\"bifrost_keychain_client_local_port\x18\xd1\x8c\x01 \x01(\x05:\x05\x31\x38\x30\x30\x31\x12\x30\n\x1f\x62ifrost_stats_client_local_port\x18\xd2\x8c\x01 \x01(\x05:\x05\x31\x38\x30\x30\x32\x12\x34\n#bifrost_throttler_client_local_port\x18\xd3\x8c\x01 \x01(\x05:\x05\x31\x38\x30\x30\x33\x12/\n\x1e\x62ifrost_broker_stub_local_port\x18\xd4\x8c\x01 \x01(\x05:\x05\x31\x38\x30\x30\x34\x12\x31\n bifrost_bridge_pigeon_local_port\x18\xd5\x8c\x01 \x01(\x05:\x05\x31\x38\x30\x30\x35\x12\x31\n bifrost_snapfs_server_local_port\x18\xd6\x8c\x01 \x01(\x05:\x05\x31\x38\x30\x30\x36\x12\x38\n\'bifrost_bridge_secure_snapfs_local_port\x18\xd7\x8c\x01 \x01(\x05:\x05\x31\x38\x30\x30\x37\x12!\n\x10\x63ohesity_ca_port\x18\xd8\xe1\x01 \x01(\x05:\x05\x32\x38\x38\x38\x38\x12-\n\x1c\x63ohesity_ca_grpc_server_port\x18\xd9\xe1\x01 \x01(\x05:\x05\x32\x38\x38\x38\x39\x12\x1e\n\rcohesion_port\x18\xe4\xe1\x01 \x01(\x05:\x05\x32\x38\x39\x30\x30\x12#\n\x12\x63ohesion_grpc_port\x18\xe5\xe1\x01 \x01(\x05:\x05\x32\x38\x39\x30\x31\x12!\n\x10linux_agent_port\x18\xdf\xd4\x03 \x01(\x05:\x05\x35\x39\x39\x39\x39\x12&\n\x15linux_agent_grpc_port\x18\x83\x87\x03 \x01(\x05:\x05\x35\x30\x30\x35\x31\x12/\n#bridge_desirable_chunk_file_size_MB\x18\xcc\x01 \x01(\x05:\x01\x38\x12\x33\n&bridge_desirable_ec_chunk_file_size_MB\x18\xd4\x01 \x01(\x05:\x02\x31\x36\x12.\n\"bridge_desirable_ec_stripe_size_MB\x18\xe5\x01 \x01(\x05:\x01\x34\x12/\n#bridge_estimated_compression_factor\x18\xcd\x01 \x01(\x05:\x01\x32\x12\'\n\x10iris_tenants_key\x18\xce\x01 \x01(\t:\x0ciris_tenants\x12?\n\x1c\x61thena_kubernetes_config_key\x18\xcf\x01 \x01(\t:\x18\x61thena_kubernetes_config\x12%\n\x0f\x61lerts_data_key\x18\xd0\x01 \x01(\t:\x0b\x61lerts_data\x12\x33\n\x12\x62ulletin_board_key\x18\xd1\x01 \x01(\t:\x16generic_bulletin_board\x12#\n\x0epg_db_info_key\x18\xd2\x01 \x01(\t:\npg_db_info\x12\x33\n\x14helios_metadata_view\x18\xd3\x01 \x01(\t:\x14helios_metadata_view\x12\x36\n\x17helios_metadata_dirpath\x18\xd5\x01 \x01(\t:\x14helios_metadata_path\x12\x31\n\x1epostgres_datadir_relative_path\x18\xd6\x01 \x01(\t:\x08postgres\x12K\n alert_policies_change_notify_key\x18\xd7\x01 \x01(\t: alert_policies_change_notify_key\x12\x37\n\x1cgandalf_iris_metadata_id_key\x18\xd8\x01 \x01(\t:\x10iris_metadata_id\x12%\n\x0f\x61xon_config_key\x18\xd9\x01 \x01(\t:\x0b\x61xon_config\x12\x32\n$axon_service_access_interface_prefix\x18\xda\x01 \x01(\t:\x03\x61sa\x12I\n!ssl_certificate_key_magneto_agent\x18\xdb\x01 \x01(\t:\x1dssl_certificate_magneto_agent\x12(\n\x17\x62ifrost_rtuser_username\x18\xdc\x01 \x01(\t:\x06rtuser\x12X\n\x1chealthcheck_results_filepath\x18\xde\x01 \x01(\t:1/home/cohesity/data/support-toolbox/healthchecks/\x12S\n\'bifrost_rtuser_authorized_keys_filepath\x18\xdf\x01 \x01(\t:!/home/rtuser/.ssh/authorized_keys\x12h\n3save_tenant_bifrost_rt_pub_key_script_relative_path\x18\xe0\x01 \x01(\t:*crux/bin/save_tenant_bifrost_rt_pub_key.sh\x12i\n-bifrost_rtuser_sshd_force_command_script_path\x18\xe1\x01 \x01(\t:1/home/rtuser/bifrost_rtuser_sshd_force_command.sh\x12\x1f\n\x0c\x61xon_mac_oui\x18\xe2\x01 \x01(\t:\x08\x34\x34:f4:e7\x12g\n\x1flinux_default_commands_filepath\x18\xe3\x01 \x01(\t:=/home/cohesity/software/crux/conf/linux_default_commands.json\x12]\n\x1elinux_custom_commands_filepath\x18\xe4\x01 \x01(\t:4/home/cohesity/data/nexus/linux_custom_commands.json\x12\x33\n\x16helios_certificate_key\x18\xe6\x01 \x01(\t:\x12helios_certificate\x12S\n\x1c\x63luster_reset_state_filepath\x18\xe7\x01 \x01(\t:,/home/cohesity/data/cluster_reset_state.json\x12_\n\x1f\x63urrent_network_config_filepath\x18\xe8\x01 \x01(\t:5/home/cohesity/data/nexus/current_network_config.yaml\x12_\n\x1fstaging_network_config_filepath\x18\xe9\x01 \x01(\t:5/home/cohesity/data/nexus/staging_network_config.yaml\x12=\n\x1f\x62ifrost_constituent_id_filename\x18\xf6\x01 \x01(\t:\x13\x63onstituent_id.json\x12-\n\x18\x62ifrost_config_file_name\x18\xea\x01 \x01(\t:\nconfig.txt\x12\x32\n\x1a\x62ifrost_rt_config_filename\x18\xf7\x01 \x01(\t:\rrt_config.txt\x12\x33\n\x16tenant_certificate_key\x18\xeb\x01 \x01(\t:\x12tenant_certificate\x12%\n\x0f\x63luster_log_key\x18\xec\x01 \x01(\t:\x0b\x63luster_log\x12)\n\x18icebox_dir_relative_path\x18\xed\x01 \x01(\t:\x06icebox\x12;\n\x1f\x62ifrost_latest_config_file_name\x18\xee\x01 \x01(\t:\x11latest_config.txt\x12\x35\n\x17\x62ifrost_vlan_config_key\x18\xef\x01 \x01(\t:\x13\x62ifrost_vlan_config\x12\x35\n\x17\x62ifrost_ipam_config_key\x18\xf0\x01 \x01(\t:\x13\x62ifrost_ipam_config\x12\x31\n\x15\x62ifrost_vm_config_key\x18\xf1\x01 \x01(\t:\x11\x62ifrost_vm_config\x12\x65\n!system_service_pkg_build_location\x18\xf2\x01 \x01(\t:9/home/cohesity/software/crux/athena/system_services/pkgs/\x12_\n\"system_service_pkg_athena_location\x18\xf3\x01 \x01(\t:2/home/cohesity/data/athena/system_service/package/\x12V\n\x1a\x62ifrost_pkg_build_location\x18\xf4\x01 \x01(\t:1/home/cohesity/software/crux/athena/bifrost/pkgs/\x12Q\n\x1b\x62ifrost_pkg_athena_location\x18\xf5\x01 \x01(\t:+/home/cohesity/data/athena/bifrost/package/\x12-\n\x13system_services_key\x18\xf8\x01 \x01(\t:\x0fsystem_services\x12;\n\x1arigel_transient_config_key\x18\xf9\x01 \x01(\t:\x16rigel_transient_config\x12+\n\x12\x63\x61_trust_store_key\x18\xfa\x01 \x01(\t:\x0e\x63\x61_trust_store\x12+\n\x14utility_app_info_key\x18\xfb\x01 \x01(\t:\x0cutility_apps\x12#\n\x0eocsp_cache_key\x18\xfc\x01 \x01(\t:\nocsp_cache\x12O\n\"ticket_approval_file_relative_path\x18\xfd\x01 \x01(\t:\"crux/bin/ticket_approval_list.json\x12-\n\x13packages_config_key\x18\xfe\x01 \x01(\t:\x0fpackages_config\x12*\n\x0e\x65ncryption_key\x18\xff\x01 \x01(\t:\x11\x65ncryption_config\x12\\\n\x16sql_agent_ca_cert_path\x18\x80\x02 \x01(\t:;/home/cohesity/software/crux/conf/agents/certs/agent_ca.pem\x12\\\n&allow_cluster_destroy_marker_file_path\x18\x81\x02 \x01(\t:+/home/cohesity/allow_cluster_destroy_marker\x12\x62\n\"system_service_json_build_location\x18\x82\x02 \x01(\t:5/home/cohesity/software/crux/conf/system_service.json\x12Z\n\"system_service_json_nexus_location\x18\x83\x02 \x01(\t:-/home/cohesity/data/nexus/system_service.json\x12^\n!system_service_vec_nexus_location\x18\x84\x02 \x01(\t:2/home/cohesity/data/nexus/system_service_vec_proto\x12%\n\x0f\x65tcd_config_key\x18\x85\x02 \x01(\t:\x0b\x65tcd_config\x12\x33\n\x16rigel_connectivity_key\x18\x86\x02 \x01(\t:\x12rigel_connectivity\x12Y\n$node_base_os_version_history_dirpath\x18\x87\x02 \x01(\t:*/home/cohesity/data/nexus/base_os_version/\x12U\n etcd_config_local_proto_filepath\x18\x88\x02 \x01(\t:*/home/cohesity/data/etcd/etcd_config.proto\x12\x35\n\x15nexus_hmac_config_key\x18\x89\x02 \x01(\t:\x15nexus_hmac_config_key\x12!\n\remail_otp_key\x18\x8a\x02 \x01(\t:\temail_otp\x12;\n\x1asfdc_instance_task_ids_key\x18\x8b\x02 \x01(\t:\x16sfdc_instance_task_ids\x12\x38\n\x18\x61udit_log_collection_key\x18\x8c\x02 \x01(\t:\x15\x61udit_log_collections\x12/\n\x16opensearch_config_file\x18\x8e\x02 \x01(\t:\x0eopensearch.yml\x12@\n\x1fopensearch_script_relative_path\x18\x8f\x02 \x01(\t:\x16\x63rux/bin/opensearch.sh\x12\x37\n\x1bopensearch_pemcert_filepath\x18\x90\x02 \x01(\t:\x11keys/cohesity.pem\x12:\n\x1aopensearch_pemkey_filepath\x18\x91\x02 \x01(\t:\x15keys/cohesity-key.pem\x12<\n!opensearch_pemtrustedcas_filepath\x18\x92\x02 \x01(\t:\x10keys/root-ca.pem\x12J\n spire_service_identity_base_path\x18\x93\x02 \x01(\t:\x1f/home/cohesity/data/nexus/spire\x12g\n\"kubelet_memory_limit_in_bytes_path\x18\x94\x02 \x01(\t::/sys/fs/cgroup/memory/kubepods.slice/memory.limit_in_bytes\x12\x61\n#cluster_disaggregate_state_filepath\x18\x95\x02 \x01(\t:3/home/cohesity/data/cluster_disaggregate_state.json\x12\'\n\x10user_tunings_key\x18\x96\x02 \x01(\t:\x0cuser_tunings\x12H\n\x16upgrade_check_dir_path\x18\x97\x02 \x01(\t:\'/home_cohesity_data/nexus/upgrade_check\x12_\n\x19support_tool_box_pkg_path\x18\x98\x02 \x01(\t:;/home_cohesity_data/nexus/upgrade_check/support-toolbox.tgz\x12Z\n\x18support_tool_box_pkg_dir\x18\x99\x02 \x01(\t:7/home_cohesity_data/nexus/upgrade_check/support_toolbox\x12\x1b\n\x0cs3_grpc_port\x18\xba\x17 \x01(\x05:\x04\x33\x30\x30\x32\x12]\n!customer_managed_baseos_file_path\x18\x9b\x02 \x01(\t:1/home/cohesity/data/nexus/customer_managed_baseos\x12H\n\x14\x64\x65s_decrypt_lib_path\x18\x9c\x02 \x01(\t:)/home/cohesity/bin/get_des_decrypted_text\x12/\n\x14tenant_migration_key\x18\x9d\x02 \x01(\t:\x10tenant_migration\x12.\n\x16ssh_key_pair_store_key\x18\x9e\x02 \x01(\t:\rssh_key_store\x12%\n\x0f\x63ohesity_ca_key\x18\x9f\x02 \x01(\t:\x0b\x63ohesity_ca\x12?\n\x1c\x63ohesity_ca_certificates_key\x18\xa0\x02 \x01(\t:\x18\x63ohesity_ca_certificates\x12K\n\"yoda_entity_id_migration_state_key\x18\xa1\x02 \x01(\t:\x1eyoda_entity_id_migration_state\x12-\n\x1a\x63ohesion_dir_relative_path\x18\xa2\x02 \x01(\t:\x08\x63ohesion\x12G\n\x1euser_bootstrap_cohesity_ca_key\x18\xa3\x02 \x01(\t:\x1euser_bootstrap_cohesity_ca_key\x12Y\n\'customer_ca_signed_cluster_certificates\x18\xa4\x02 \x01(\t:\'customer_ca_signed_cluster_certificates\x12K\n rotated_cohesity_ca_certificates\x18\xa5\x02 \x01(\t: rotated_cohesity_ca_certificates\x12\x37\n\x18on_prem_rigel_config_key\x18\xa6\x02 \x01(\t:\x14on_prem_rigel_config\x12\x37\n\x16\x64ownloaded_patches_key\x18\xa7\x02 \x01(\t:\x16\x64ownloaded_patches_key\x12\x31\n\x13patches_history_key\x18\xa8\x02 \x01(\t:\x13patches_history_key\x12\x45\n\x1dpatch_orchestration_state_key\x18\xa9\x02 \x01(\t:\x1dpatch_orchestration_state_key\x12+\n\x12prechecks_data_key\x18\xaa\x02 \x01(\t:\x0eprechecks_data\x12L\n!helios_certificate_encryption_key\x18\xab\x02 \x01(\t: VDCDPTXGDCADVLFBWSGSKMRSPTVQNGYHJ\x04\x08\x08\x10\tJ\x04\x08#\x10$J\x06\x08\x8c.\x10\xf1.J\x06\x08\x90\x35\x10\xf5\x35J\x06\x08\x91N\x10\xf8UJ\x04\x08i\x10jJ\x08\x08\xe5\xc8\x01\x10\xc8\xc9\x01J\x08\x08\xa8\xd0\x01\x10\xcc\xd0\x01J\x07\x08\x99u\x10\xe8\x84\x01J\x08\x08\xdd\x88\x01\x10\xc0\x89\x01J\x08\x08\xe9\x84\x01\x10\xcd\x85\x01J\x08\x08\xb2\xea\x01\x10\xf4\xfd\x01J\x08\x08\xa7\xff\x01\x10\x83\x87\x03J\x08\x08\x84\x87\x03\x10\xdf\xd4\x03J\x08\x08\xca\xdc\x03\x10\x98\xf2\x03J\x08\x08\x84\xf4\x03\x10\x85\xf4\x03J\x08\x08\xb5\xf2\x03\x10\x80\xf4\x03J\x06\x08\xdd\x01\x10\xde\x01\x42\x16\n\x14\x63om.cohesity.configs')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'configs.node_config_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\024com.cohesity.configs'
  _globals['_NODECONFIGPROTO']._serialized_start=49
  _globals['_NODECONFIGPROTO']._serialized_end=19677
# @@protoc_insertion_point(module_scope)
