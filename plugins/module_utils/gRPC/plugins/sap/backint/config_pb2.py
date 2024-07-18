# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: plugins/sap/backint/config.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n plugins/sap/backint/config.proto\x12\x1c\x63ohesity.plugins.sap.backint\"\xba\r\n\x0bParamsProto\x12\x13\n\x0b\x63luster_ips\x18\x01 \x01(\t\x12\x14\n\x0c\x63luster_port\x18\x02 \x01(\x05\x12\x11\n\tview_name\x18\x03 \x01(\t\x12\x17\n\x0fio_thread_count\x18\x04 \x01(\x05\x12\x1a\n\x12max_outstanding_io\x18\x05 \x01(\x05\x12\x15\n\rmax_cached_io\x18\x06 \x01(\x05\x12\x19\n\x11max_io_size_bytes\x18\x07 \x01(\x05\x12\x19\n\x11rpc_timeout_msecs\x18\x08 \x01(\x05\x12\x1f\n\x17\x63\x65rtificate_config_path\x18\t \x01(\t\x12\x1b\n\x13inquire_period_days\x18\n \x01(\x05\x12\x0f\n\x07log_dir\x18\x0b \x01(\t\x12\x12\n\nvlog_level\x18\x0c \x01(\x05\x12\"\n\x1ametafiles_read_concurrency\x18\r \x01(\x05\x12\x1f\n\x17write_rpc_timeout_msecs\x18\x0e \x01(\x05\x12\x1b\n\x13\x61\x64\x64_back_time_msecs\x18\x0f \x01(\x03\x12\'\n\x1f\x62ridge_snap_fs_stub_max_retries\x18\x10 \x01(\x05\x12\x1a\n\x12max_backup_streams\x18\x11 \x01(\x05\x12\x1b\n\x13max_restore_streams\x18\x12 \x01(\x05\x12\x1a\n\x12\x65nable_dedup_write\x18\x13 \x01(\x08\x12\x19\n\x11\x65nable_dedup_read\x18\x14 \x01(\x08\x12\x1b\n\x13\x65nable_bifrost_auth\x18\x15 \x01(\x08\x12&\n\x1einitial_create_file_size_in_gb\x18\x16 \x01(\x03\x12\x1e\n\x16\x65nable_read_forwarding\x18\x17 \x01(\x08\x12\x1f\n\x17\x65nable_write_forwarding\x18\x18 \x01(\x08\x12V\n\x12vip_selection_type\x18\x19 \x01(\x0e\x32:.cohesity.plugins.sap.backint.ParamsProto.VIPSelectionType\x12\x44\n<bridge_wan_stub_remote_endpoint_acceptable_failure_threshold\x18\x1a \x01(\x05\x12\x1a\n\x12\x61udit_pipe_latency\x18\x1b \x01(\x08\x12&\n\x1einterval_to_audit_pipe_latency\x18\x1c \x01(\x05\x12\x1d\n\x15log_retention_size_mb\x18\x1d \x01(\x05\x12\x1c\n\x14\x64isable_sha1_streams\x18\x1e \x01(\x08\x12\'\n\x1fsap_hana_enable_error_injection\x18\x1f \x01(\x08\x12\x30\n(inquire_without_pipe_name_match_for_ebid\x18  \x01(\x08\x12\x30\n(restore_without_pipe_name_match_for_ebid\x18! \x01(\x08\x12\x46\n>bridge_wan_stub_remote_endpoint_failure_timeframe_window_msecs\x18\" \x01(\x05\x12R\n\x16qos_principal_priority\x18# \x01(\x0e\x32\x32.cohesity.plugins.sap.backint.ParamsProto.Priority\x12*\n\"enable_clean_up_logs_on_log_backup\x18$ \x01(\x08\x12\x1f\n\x17progress_directory_path\x18% \x01(\t\x12 \n\x18\x65t_log_backup_param_file\x18\x36 \x01(\t\x12\x0e\n\x06job_id\x18\x37 \x01(\t\x12.\n\x1fis_et_log_backup_enabled_for_db\x18\x38 \x01(\x08:\x05\x66\x61lse\x12\x15\n\ruse_tcp_proxy\x18\x39 \x01(\x08\x12\x18\n\x10proxy_port_range\x18: \x01(\t\"_\n\x10VIPSelectionType\x12\x13\n\x0fkConsistentHash\x10\x01\x12\x0f\n\x0bkRoundRobin\x10\x02\x12\x15\n\x11kLeastConnections\x10\x03\x12\x0e\n\nkMixedMode\x10\x04\"~\n\x08Priority\x12\r\n\tkCritical\x10\x00\x12\t\n\x05kHigh\x10\x01\x12\x0b\n\x07kMedium\x10\x02\x12\x08\n\x04kLow\x10\x03\x12\x12\n\x0ekNumPriorities\x10\x04\x12\x0f\n\x0bkNoPriority\x10\x05\x12\x1c\n\x18kNumPrioritiesUpperLimit\x10@\"\x8b\x01\n\x0e\x44\x61taSourceInfo\x12?\n\x04type\x18\x01 \x01(\x0e\x32\x31.cohesity.plugins.sap.backint.DataSourceInfo.Type\x12\x0c\n\x04path\x18\x02 \x01(\t\x12\x0c\n\x04\x65\x62id\x18\x03 \x01(\t\"\x1c\n\x04Type\x12\t\n\x05kPipe\x10\x01\x12\t\n\x05kFile\x10\x02\"\xa9\x01\n\rMetadataProto\x12\r\n\x05\x65poch\x18\x01 \x01(\x04\x12\r\n\x05\x63ount\x18\x02 \x01(\r\x12\x10\n\x08\x62\x61\x63kupid\x18\x03 \x01(\t\x12\x0b\n\x03sid\x18\x04 \x01(\t\x12\x14\n\x0c\x62\x61\x63kup_level\x18\x05 \x01(\t\x12\x45\n\x0fsource_info_vec\x18\x06 \x03(\x0b\x32,.cohesity.plugins.sap.backint.DataSourceInfo\"\xc5\x02\n\x17\x42\x61\x63kintCertificateProto\x12\x65\n\x15\x63onnection_config_vec\x18\x01 \x03(\x0b\x32\x46.cohesity.plugins.sap.backint.BackintCertificateProto.ConnectionConfig\x1a\xc2\x01\n\x10\x43onnectionConfig\x12\x14\n\x0c\x63luster_cert\x18\x01 \x01(\t\x12\x11\n\tself_cert\x18\x02 \x01(\t\x12$\n\x1cself_cert_priv_key_encrypted\x18\x03 \x01(\x0c\x12\x11\n\ttenant_id\x18\x04 \x01(\t\x12\x16\n\ncluster_id\x18\x05 \x01(\x03:\x02-1\x12\x34\n\x17grpc_server_common_name\x18\x06 \x01(\t:\x13\x43ohesity Inc ServerB\"\n com.cohesity.plugins.sap.backint')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'plugins.sap.backint.config_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n com.cohesity.plugins.sap.backint'
  _globals['_PARAMSPROTO']._serialized_start=67
  _globals['_PARAMSPROTO']._serialized_end=1789
  _globals['_PARAMSPROTO_VIPSELECTIONTYPE']._serialized_start=1566
  _globals['_PARAMSPROTO_VIPSELECTIONTYPE']._serialized_end=1661
  _globals['_PARAMSPROTO_PRIORITY']._serialized_start=1663
  _globals['_PARAMSPROTO_PRIORITY']._serialized_end=1789
  _globals['_DATASOURCEINFO']._serialized_start=1792
  _globals['_DATASOURCEINFO']._serialized_end=1931
  _globals['_DATASOURCEINFO_TYPE']._serialized_start=1903
  _globals['_DATASOURCEINFO_TYPE']._serialized_end=1931
  _globals['_METADATAPROTO']._serialized_start=1934
  _globals['_METADATAPROTO']._serialized_end=2103
  _globals['_BACKINTCERTIFICATEPROTO']._serialized_start=2106
  _globals['_BACKINTCERTIFICATEPROTO']._serialized_end=2431
  _globals['_BACKINTCERTIFICATEPROTO_CONNECTIONCONFIG']._serialized_start=2237
  _globals['_BACKINTCERTIFICATEPROTO_CONNECTIONCONFIG']._serialized_end=2431
# @@protoc_insertion_point(module_scope)