# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: magneto/master/base/master_cdp.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from atom.base import atom_pb2 as atom_dot_base_dot_atom__pb2
from magneto.base import common_pb2 as magneto_dot_base_dot_common__pb2
from magneto.base import entity_pb2 as magneto_dot_base_dot_entity__pb2
from magneto.base import enums_pb2 as magneto_dot_base_dot_enums__pb2
from magneto.base import error_pb2 as magneto_dot_base_dot_error__pb2
from magneto.base.entities import vmware_pb2 as magneto_dot_base_dot_entities_dot_vmware__pb2
from magneto.connectors.vmware import vmware_pb2 as magneto_dot_connectors_dot_vmware_dot_vmware__pb2
from util.base import universal_id_pb2 as util_dot_base_dot_universal__id__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$magneto/master/base/master_cdp.proto\x12\x17\x63ohesity.magneto.master\x1a\x14\x61tom/base/atom.proto\x1a\x19magneto/base/common.proto\x1a\x19magneto/base/entity.proto\x1a\x18magneto/base/enums.proto\x1a\x18magneto/base/error.proto\x1a\"magneto/base/entities/vmware.proto\x1a&magneto/connectors/vmware/vmware.proto\x1a\x1cutil/base/universal_id.proto\"\xd5.\n\x13\x45ntityCdpStateProto\x12-\n\x06\x65ntity\x18\x01 \x01(\x0b\x32\x1d.cohesity.magneto.EntityProto\x12+\n\x07job_uid\x18\x02 \x01(\x0b\x32\x1a.cohesity.UniversalIdProto\x12\x16\n\x0eis_cdp_enabled\x18\x03 \x01(\x08\x12\\\n\x12pre_process_status\x18\x04 \x01(\x0b\x32@.cohesity.magneto.master.EntityCdpStateProto.PreProcessingStatus\x12W\n\x11\x63\x64p_filter_status\x18\x05 \x01(\x0b\x32<.cohesity.magneto.master.EntityCdpStateProto.CDPFilterStatus\x12W\n\x11image_backup_info\x18\x06 \x01(\x0b\x32<.cohesity.magneto.master.EntityCdpStateProto.ImageBackupInfo\x12]\n\x14hydration_point_info\x18\x07 \x01(\x0b\x32?.cohesity.magneto.master.EntityCdpStateProto.HydrationPointInfo\x12M\n\x0c\x63\x64p_log_info\x18\x08 \x01(\x0b\x32\x37.cohesity.magneto.master.EntityCdpStateProto.CDPLogInfo\x12N\n\x0cstate_intent\x18\t \x01(\x0b\x32\x38.cohesity.magneto.master.EntityCdpStateProto.StateIntent\x12[\n\x13process_events_info\x18\n \x01(\x0b\x32>.cohesity.magneto.master.EntityCdpStateProto.ProcessEventsInfo\x12*\n\"cluster_compute_resource_entity_id\x18\x0b \x01(\x03\x12@\n\x0b\x63\x64p_version\x18\x0c \x01(\x0e\x32\x1c.cohesity.magneto.CDPVersion:\rkCDPVersionV1\x12M\n\x0clog_run_info\x18\r \x01(\x0b\x32\x37.cohesity.magneto.master.EntityCdpStateProto.LogRunInfo\x12#\n\x14is_replicated_entity\x18\x0e \x01(\x08:\x05\x66\x61lse\x12i\n\x14replication_strategy\x18\x0f \x01(\x0e\x32@.cohesity.magneto.master.EntityCdpStateProto.ReplicationStrategy:\tkPeriodic\x12^\n\x13post_process_status\x18\x10 \x01(\x0b\x32\x41.cohesity.magneto.master.EntityCdpStateProto.PostProcessingStatus\x12J\n\nalert_info\x18\x11 \x01(\x0b\x32\x36.cohesity.magneto.master.EntityCdpStateProto.AlertInfo\x12]\n\x12sync_repl_info_map\x18\x12 \x03(\x0b\x32\x41.cohesity.magneto.master.EntityCdpStateProto.SyncReplInfoMapEntry\x12\x14\n\x0ctx_entity_id\x18\x13 \x01(\x03\x12.\n\ntx_job_uid\x18\x14 \x01(\x0b\x32\x1a.cohesity.UniversalIdProto\x12\x17\n\x08is_stale\x18\x15 \x01(\x08:\x05\x66\x61lse\x12T\n\x0fguardrails_info\x18\x16 \x01(\x0b\x32;.cohesity.magneto.master.EntityCdpStateProto.GuardrailsInfo\x12!\n\x12is_journal_sharded\x18\x17 \x01(\x08:\x05\x66\x61lse\x12\"\n\x13\x61llow_re_enable_cdp\x18\x18 \x01(\x08:\x05\x66\x61lse\x12\x19\n\x11purge_data_events\x18\x19 \x01(\x08\x1a\xea\x01\n\x13PreProcessingStatus\x12U\n\x05state\x18\x01 \x01(\x0e\x32\x46.cohesity.magneto.master.EntityCdpStateProto.PreProcessingStatus.State\x12+\n\x05\x65rror\x18\x02 \x01(\x0b\x32\x1c.cohesity.magneto.ErrorProto\"O\n\x05State\x12\x0c\n\x08kUnknown\x10\x00\x12\x0c\n\x08kStarted\x10\x01\x12\x0f\n\x0bkInProgress\x10\x02\x12\r\n\tkFinished\x10\x03\x12\n\n\x06kError\x10\x04\x1a\xae\x07\n\x0f\x43\x44PFilterStatus\x12`\n\x05state\x18\x01 \x01(\x0e\x32\x42.cohesity.magneto.master.EntityCdpStateProto.CDPFilterStatus.State:\rkNotInstalled\x12\x0f\n\x07version\x18\x02 \x01(\t\x12+\n\x05\x65rror\x18\x03 \x01(\x0b\x32\x1c.cohesity.magneto.ErrorProto\x12g\n\rfilter_issues\x18\x05 \x01(\x0b\x32P.cohesity.magneto.master.EntityCdpStateProto.CDPFilterStatus.FilterIssuesOnHosts\x12\'\n\x1fstorage_policy_attached_offline\x18\x06 \x01(\x08\x12*\n\"last_filter_alert_raised_time_secs\x18\x07 \x01(\x03\x12V\n\x14io_filter_properties\x18\x08 \x01(\x0b\x32\x38.cohesity.magneto.vmware.IoFilterStoragePolicyProperties\x1ap\n\x13\x46ilterIssuesOnHosts\x12\x0e\n\x06\x61\x63tion\x18\x01 \x01(\t\x12I\n\x15host_io_filter_issues\x18\x02 \x03(\x0b\x32*.cohesity.magneto.vmware.IoFilterHostIssue\"\xec\x02\n\x05State\x12\x0c\n\x08kUnknown\x10\x00\x12\x11\n\rkNotInstalled\x10\x01\x12\x1c\n\x18kInstallFilterInProgress\x10\x02\x12\x14\n\x10kFilterInstalled\x10\x08\x12\x1e\n\x1akUninstallFilterInProgress\x10\x07\x12\x1c\n\x18kUpgradeFilterInProgress\x10\n\x12\x18\n\x14kUpgradeFilterFailed\x10\x0b\x12\x1a\n\x16kUninstallFilterFailed\x10\x0c\x12\x1e\n\x1akFilterInstalledIOInactive\x10\x03\x12\x0f\n\x0bkIOInactive\x10\t\x12\x1b\n\x17kIOActivationInProgress\x10\x04\x12\r\n\tkIOActive\x10\x05\x12\x1d\n\x19kIODeactivationInProgress\x10\x06\x12\x1e\n\x1akWaitingForCDPPolicyAttach\x10\rJ\x04\x08\x04\x10\x05\x1a\xa2\x03\n\x0fImageBackupInfo\x12[\n\x05state\x18\x01 \x01(\x0e\x32\x42.cohesity.magneto.master.EntityCdpStateProto.ImageBackupInfo.State:\x08kUnknown\x12\x0f\n\x07\x64\x65tails\x18\x02 \x01(\t\x12\x1b\n\x13last_backup_task_id\x18\x03 \x01(\x03\x12$\n\x1clast_backup_start_time_usecs\x18\x04 \x01(\x03\x12\"\n\x1alast_backup_end_time_usecs\x18\x05 \x01(\x03\x12+\n\x05\x65rror\x18\x06 \x01(\x0b\x32\x1c.cohesity.magneto.ErrorProto\x12\x16\n\x0evmsd_file_path\x18\x07 \x01(\t\x12!\n\x19snapshot_create_time_secs\x18\x08 \x01(\x03\"R\n\x05State\x12\x0c\n\x08kUnknown\x10\x00\x12\x0f\n\x0bkTakeBackup\x10\x01\x12\x0f\n\x0bkInProgress\x10\x02\x12\r\n\tkComplete\x10\x03\x12\n\n\x06kError\x10\x04\x1a\xdf\x02\n\x12HydrationPointInfo\x12^\n\x05state\x18\x01 \x01(\x0e\x32\x45.cohesity.magneto.master.EntityCdpStateProto.HydrationPointInfo.State:\x08kUnknown\x12\x1e\n\x16last_hydration_task_id\x18\x02 \x01(\x03\x12&\n\x1elast_hydration_timestamp_usecs\x18\x03 \x01(\x03\x12\x31\n)last_successful_hydration_timestamp_usecs\x18\x04 \x01(\x03\x12+\n\x05\x65rror\x18\x05 \x01(\x0b\x32\x1c.cohesity.magneto.ErrorProto\"A\n\x05State\x12\x0c\n\x08kUnknown\x10\x00\x12\x0f\n\x0bkInProgress\x10\x01\x12\r\n\tkComplete\x10\x02\x12\n\n\x06kError\x10\x03\x1a\x37\n\nCDPLogInfo\x12\x13\n\x0bview_box_id\x18\x01 \x01(\x03\x12\x14\n\x0clog_view_dir\x18\x02 \x01(\t\x1a\x96\x02\n\x0bStateIntent\x12\x63\n\rfilter_intent\x18\x01 \x01(\x0e\x32\x45.cohesity.magneto.master.EntityCdpStateProto.StateIntent.FilterIntent:\x05kNone\x12\x1a\n\x0btake_backup\x18\x02 \x01(\x08:\x05\x66\x61lse\"\x85\x01\n\x0c\x46ilterIntent\x12\x0c\n\x08kUnknown\x10\x00\x12\r\n\tkIOActive\x10\x01\x12\x0f\n\x0bkIOInactive\x10\x02\x12\x12\n\x0ekInstallFilter\x10\x04\x12\x14\n\x10kUninstallFilter\x10\x05\x12\x12\n\x0ekUpgradeFilter\x10\x06\x12\t\n\x05kNone\x10\x03\x1a\x46\n\x11ProcessEventsInfo\x12\x31\n%latest_processed_migration_time_usecs\x18\x01 \x01(\x03:\x02-1\x1a\xdb\x02\n\nLogRunInfo\x12V\n\x05state\x18\x01 \x01(\x0e\x32=.cohesity.magneto.master.EntityCdpStateProto.LogRunInfo.State:\x08kUnknown\x12$\n\x1clast_log_run_timestamp_usecs\x18\x02 \x01(\x03\x12\'\n\x1flast_applied_io_timestamp_usecs\x18\x04 \x01(\x03\x12\x36\n\x13last_switched_epoch\x18\x05 \x01(\x0b\x32\x19.cohesity.atom.EpochProto\x12+\n\x05\x65rror\x18\x03 \x01(\x0b\x32\x1c.cohesity.magneto.ErrorProto\"A\n\x05State\x12\x0c\n\x08kUnknown\x10\x00\x12\x0f\n\x0bkInProgress\x10\x01\x12\r\n\tkComplete\x10\x02\x12\n\n\x06kError\x10\x03\x1a\x8e\x02\n\x14PostProcessingStatus\x12`\n\x05state\x18\x01 \x01(\x0e\x32G.cohesity.magneto.master.EntityCdpStateProto.PostProcessingStatus.State:\x08kUnknown\x12\x16\n\x0bretry_count\x18\x02 \x01(\x05:\x01\x30\x12+\n\x05\x65rror\x18\x03 \x01(\x0b\x32\x1c.cohesity.magneto.ErrorProto\"O\n\x05State\x12\x0c\n\x08kUnknown\x10\x00\x12\x0c\n\x08kStarted\x10\x01\x12\x0f\n\x0bkInProgress\x10\x02\x12\r\n\tkFinished\x10\x03\x12\n\n\x06kError\x10\x04\x1a\x95\x01\n\tAlertInfo\x12S\n\x04type\x18\x01 \x01(\x0e\x32;.cohesity.magneto.master.EntityCdpStateProto.AlertInfo.Type:\x08kUnknown\x12\x0b\n\x03msg\x18\x02 \x01(\t\"&\n\x04Type\x12\x0c\n\x08kUnknown\x10\x00\x12\x10\n\x0ckCDPDisabled\x10\x01\x1a\xb7\x04\n\x13SyncReplicationInfo\x12_\n\x05state\x18\x01 \x01(\x0e\x32\x46.cohesity.magneto.master.EntityCdpStateProto.SyncReplicationInfo.State:\x08kUnknown\x12+\n\x05\x65rror\x18\x02 \x01(\x0b\x32\x1c.cohesity.magneto.ErrorProto\x12\x19\n\x11remote_cluster_id\x18\x03 \x01(\x03\x12,\n$last_replicated_run_start_time_usecs\x18\x04 \x01(\x03\x12O\n\x1blast_replicated_backup_type\x18\x05 \x01(\x0e\x32*.cohesity.magneto.ScheduledBackupType.Type\x12:\n\x0crx_hole_info\x18\x06 \x01(\x0b\x32$.cohesity.magneto.master.CDPHoleInfo\x12%\n\x1dlast_fetched_state_time_usecs\x18\x07 \x01(\x03\"\x94\x01\n\x05State\x12\x0c\n\x08kUnknown\x10\x00\x12\n\n\x06kStart\x10\x01\x12\x12\n\x0ekSyncReplicate\x10\x02\x12\x17\n\x13kWaitingForSnapshot\x10\x03\x12\x0b\n\x07kSteady\x10\x04\x12\t\n\x05kStop\x10\x05\x12\x13\n\x0fkInitInProgress\x10\x06\x12\x17\n\x13kSnapshotInProgress\x10\x07\x1ax\n\x14SyncReplInfoMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\x03\x12O\n\x05value\x18\x02 \x01(\x0b\x32@.cohesity.magneto.master.EntityCdpStateProto.SyncReplicationInfo:\x02\x38\x01\x1a\xc4\x03\n\x0eGuardrailsInfo\x12\'\n\x1fhydration_skip_start_time_usecs\x18\x01 \x01(\x03\x12\"\n\x1a\x65sx_max_io_throughput_mbps\x18\x02 \x01(\x03\x12\x35\n-last_esx_max_throughput_processing_time_usecs\x18\x03 \x01(\x03\x12\x61\n\x0e\x64isable_intent\x18\x04 \x01(\x0e\x32I.cohesity.magneto.master.EntityCdpStateProto.GuardrailsInfo.DisableIntent\x12$\n\x1clast_cdp_disabled_time_usecs\x18\x05 \x01(\x03\x12#\n\x1b\x63\x64p_disabled_time_usecs_vec\x18\x06 \x03(\x03\x12+\n\x05\x65rror\x18\x07 \x01(\x0b\x32\x1c.cohesity.magneto.ErrorProto\"S\n\rDisableIntent\x12\x0c\n\x08kUnknown\x10\x00\x12\x0f\n\x0bkDisableCDP\x10\x01\x12\x18\n\x14kPermanentDisableCDP\x10\x02\x12\t\n\x05kNone\x10\x03\"/\n\x13ReplicationStrategy\x12\r\n\tkPeriodic\x10\x00\x12\t\n\x05kSync\x10\x01\"G\n\x0b\x43\x44PHoleInfo\x12\x1c\n\x10start_time_usecs\x18\x01 \x01(\x03:\x02-1\x12\x1a\n\x0e\x65nd_time_usecs\x18\x02 \x01(\x03:\x02-1')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'magneto.master.base.master_cdp_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_ENTITYCDPSTATEPROTO_SYNCREPLINFOMAPENTRY']._loaded_options = None
  _globals['_ENTITYCDPSTATEPROTO_SYNCREPLINFOMAPENTRY']._serialized_options = b'8\001'
  _globals['_ENTITYCDPSTATEPROTO']._serialized_start=300
  _globals['_ENTITYCDPSTATEPROTO']._serialized_end=6273
  _globals['_ENTITYCDPSTATEPROTO_PREPROCESSINGSTATUS']._serialized_start=1938
  _globals['_ENTITYCDPSTATEPROTO_PREPROCESSINGSTATUS']._serialized_end=2172
  _globals['_ENTITYCDPSTATEPROTO_PREPROCESSINGSTATUS_STATE']._serialized_start=2093
  _globals['_ENTITYCDPSTATEPROTO_PREPROCESSINGSTATUS_STATE']._serialized_end=2172
  _globals['_ENTITYCDPSTATEPROTO_CDPFILTERSTATUS']._serialized_start=2175
  _globals['_ENTITYCDPSTATEPROTO_CDPFILTERSTATUS']._serialized_end=3117
  _globals['_ENTITYCDPSTATEPROTO_CDPFILTERSTATUS_FILTERISSUESONHOSTS']._serialized_start=2632
  _globals['_ENTITYCDPSTATEPROTO_CDPFILTERSTATUS_FILTERISSUESONHOSTS']._serialized_end=2744
  _globals['_ENTITYCDPSTATEPROTO_CDPFILTERSTATUS_STATE']._serialized_start=2747
  _globals['_ENTITYCDPSTATEPROTO_CDPFILTERSTATUS_STATE']._serialized_end=3111
  _globals['_ENTITYCDPSTATEPROTO_IMAGEBACKUPINFO']._serialized_start=3120
  _globals['_ENTITYCDPSTATEPROTO_IMAGEBACKUPINFO']._serialized_end=3538
  _globals['_ENTITYCDPSTATEPROTO_IMAGEBACKUPINFO_STATE']._serialized_start=3456
  _globals['_ENTITYCDPSTATEPROTO_IMAGEBACKUPINFO_STATE']._serialized_end=3538
  _globals['_ENTITYCDPSTATEPROTO_HYDRATIONPOINTINFO']._serialized_start=3541
  _globals['_ENTITYCDPSTATEPROTO_HYDRATIONPOINTINFO']._serialized_end=3892
  _globals['_ENTITYCDPSTATEPROTO_HYDRATIONPOINTINFO_STATE']._serialized_start=3827
  _globals['_ENTITYCDPSTATEPROTO_HYDRATIONPOINTINFO_STATE']._serialized_end=3892
  _globals['_ENTITYCDPSTATEPROTO_CDPLOGINFO']._serialized_start=3894
  _globals['_ENTITYCDPSTATEPROTO_CDPLOGINFO']._serialized_end=3949
  _globals['_ENTITYCDPSTATEPROTO_STATEINTENT']._serialized_start=3952
  _globals['_ENTITYCDPSTATEPROTO_STATEINTENT']._serialized_end=4230
  _globals['_ENTITYCDPSTATEPROTO_STATEINTENT_FILTERINTENT']._serialized_start=4097
  _globals['_ENTITYCDPSTATEPROTO_STATEINTENT_FILTERINTENT']._serialized_end=4230
  _globals['_ENTITYCDPSTATEPROTO_PROCESSEVENTSINFO']._serialized_start=4232
  _globals['_ENTITYCDPSTATEPROTO_PROCESSEVENTSINFO']._serialized_end=4302
  _globals['_ENTITYCDPSTATEPROTO_LOGRUNINFO']._serialized_start=4305
  _globals['_ENTITYCDPSTATEPROTO_LOGRUNINFO']._serialized_end=4652
  _globals['_ENTITYCDPSTATEPROTO_LOGRUNINFO_STATE']._serialized_start=3827
  _globals['_ENTITYCDPSTATEPROTO_LOGRUNINFO_STATE']._serialized_end=3892
  _globals['_ENTITYCDPSTATEPROTO_POSTPROCESSINGSTATUS']._serialized_start=4655
  _globals['_ENTITYCDPSTATEPROTO_POSTPROCESSINGSTATUS']._serialized_end=4925
  _globals['_ENTITYCDPSTATEPROTO_POSTPROCESSINGSTATUS_STATE']._serialized_start=2093
  _globals['_ENTITYCDPSTATEPROTO_POSTPROCESSINGSTATUS_STATE']._serialized_end=2172
  _globals['_ENTITYCDPSTATEPROTO_ALERTINFO']._serialized_start=4928
  _globals['_ENTITYCDPSTATEPROTO_ALERTINFO']._serialized_end=5077
  _globals['_ENTITYCDPSTATEPROTO_ALERTINFO_TYPE']._serialized_start=5039
  _globals['_ENTITYCDPSTATEPROTO_ALERTINFO_TYPE']._serialized_end=5077
  _globals['_ENTITYCDPSTATEPROTO_SYNCREPLICATIONINFO']._serialized_start=5080
  _globals['_ENTITYCDPSTATEPROTO_SYNCREPLICATIONINFO']._serialized_end=5647
  _globals['_ENTITYCDPSTATEPROTO_SYNCREPLICATIONINFO_STATE']._serialized_start=5499
  _globals['_ENTITYCDPSTATEPROTO_SYNCREPLICATIONINFO_STATE']._serialized_end=5647
  _globals['_ENTITYCDPSTATEPROTO_SYNCREPLINFOMAPENTRY']._serialized_start=5649
  _globals['_ENTITYCDPSTATEPROTO_SYNCREPLINFOMAPENTRY']._serialized_end=5769
  _globals['_ENTITYCDPSTATEPROTO_GUARDRAILSINFO']._serialized_start=5772
  _globals['_ENTITYCDPSTATEPROTO_GUARDRAILSINFO']._serialized_end=6224
  _globals['_ENTITYCDPSTATEPROTO_GUARDRAILSINFO_DISABLEINTENT']._serialized_start=6141
  _globals['_ENTITYCDPSTATEPROTO_GUARDRAILSINFO_DISABLEINTENT']._serialized_end=6224
  _globals['_ENTITYCDPSTATEPROTO_REPLICATIONSTRATEGY']._serialized_start=6226
  _globals['_ENTITYCDPSTATEPROTO_REPLICATIONSTRATEGY']._serialized_end=6273
  _globals['_CDPHOLEINFO']._serialized_start=6275
  _globals['_CDPHOLEINFO']._serialized_end=6346
# @@protoc_insertion_point(module_scope)