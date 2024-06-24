# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: magneto/master/base/remote_actions.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from magneto.api import worm_pb2 as magneto_dot_api_dot_worm__pb2
from magneto.base import error_pb2 as magneto_dot_base_dot_error__pb2
from magneto.base import entity_pb2 as magneto_dot_base_dot_entity__pb2
from magneto.base import magneto_pb2 as magneto_dot_base_dot_magneto__pb2
try:
  magneto_dot_base_dot_env__params__pb2 = magneto_dot_base_dot_magneto__pb2.magneto_dot_base_dot_env__params__pb2
except AttributeError:
  magneto_dot_base_dot_env__params__pb2 = magneto_dot_base_dot_magneto__pb2.magneto.base.env_params_pb2
from magneto.base import permissions_pb2 as magneto_dot_base_dot_permissions__pb2
from magneto.base import policy_pb2 as magneto_dot_base_dot_policy__pb2
from magneto.master.base import master_pb2 as magneto_dot_master_dot_base_dot_master__pb2
from magneto.master.base import master_cdp_pb2 as magneto_dot_master_dot_base_dot_master__cdp__pb2
from magneto.master.entity_provenance import entity_provenance_pb2 as magneto_dot_master_dot_entity__provenance_dot_entity__provenance__pb2
from magneto.utils import capability_pb2 as magneto_dot_utils_dot_capability__pb2
from util.base import cluster_instance_identifier_pb2 as util_dot_base_dot_cluster__instance__identifier__pb2
from util.base import universal_id_pb2 as util_dot_base_dot_universal__id__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(magneto/master/base/remote_actions.proto\x12\x17\x63ohesity.magneto.master\x1a\x16magneto/api/worm.proto\x1a\x18magneto/base/error.proto\x1a\x19magneto/base/entity.proto\x1a\x1amagneto/base/magneto.proto\x1a\x1emagneto/base/permissions.proto\x1a\x19magneto/base/policy.proto\x1a magneto/master/base/master.proto\x1a$magneto/master/base/master_cdp.proto\x1a\x38magneto/master/entity_provenance/entity_provenance.proto\x1a\x1emagneto/utils/capability.proto\x1a+util/base/cluster_instance_identifier.proto\x1a\x1cutil/base/universal_id.proto\"\x14\n\x12GetCapabilitiesArg\"T\n\x15GetCapabilitiesResult\x12;\n\x10\x63\x61pability_proto\x18\x01 \x01(\x0b\x32!.cohesity.magneto.CapabilityProto\"\xcd\x06\n\x17StartReplicationTaskArg\x12\x1b\n\x13replication_version\x18\x01 \x01(\x05\x12\x39\n\x0fjob_description\x18\x02 \x01(\x0b\x32 .cohesity.magneto.BackupJobProto\x12\x42\n\x11protection_policy\x18\n \x01(\x0b\x32\'.cohesity.magneto.ProtectionPolicyProto\x12,\n\x08task_uid\x18\x03 \x01(\x0b\x32\x1a.cohesity.UniversalIdProto\x12\x46\n\x08run_base\x18\x04 \x01(\x0b\x32\x34.cohesity.magneto.master.BackupJobTaskStateBaseProto\x12\x1d\n\x15snapshot_expiry_usecs\x18\x05 \x01(\x03\x12\x16\n\x0erx_view_box_id\x18\x06 \x01(\x03\x12J\n\x1a\x65ntity_permission_info_vec\x18\x07 \x03(\x0b\x32&.cohesity.magneto.EntityPermissionInfo\x12\x1f\n\x11object_level_copy\x18\x08 \x01(\x08:\x04true\x12V\n\x1a\x65ntity_provenance_edge_vec\x18\t \x03(\x0b\x32\x32.cohesity.magneto.master.EntityProvenanceEdgeProto\x12>\n\x13tx_capability_proto\x18\x0b \x01(\x0b\x32!.cohesity.magneto.CapabilityProto\x12I\n\x10\x62\x61\x63kup_run_state\x18\x0c \x01(\x0b\x32/.cohesity.magneto.master.BackupJobRunStateProto\x12 \n\x18is_out_of_band_copy_task\x18\r \x01(\x08\x12@\n\x10retention_policy\x18\x0e \x01(\x0b\x32&.cohesity.magneto.RetentionPolicyProto\x12\x35\n\x0e\x61pp_entity_vec\x18\x0f \x03(\x0b\x32\x1d.cohesity.magneto.EntityProto\"\x95\x02\n\x1aStartReplicationTaskResult\x12I\n\x10\x62\x61\x63kup_run_state\x18\x01 \x01(\x0b\x32/.cohesity.magneto.master.BackupJobRunStateProto\x12\"\n\x1a\x65xisting_expiry_time_usecs\x18\x02 \x01(\x03\x12V\n\x1e\x65xisting_data_lock_constraints\x18\x03 \x01(\x0b\x32..cohesity.magneto.api.DataLockConstraintsProto\x12\x30\n(display_sub_tasks_status_based_on_parent\x18\x04 \x01(\x08\"\xe6\x02\n\x15\x45ndReplicationTaskArg\x12,\n\x08task_uid\x18\x01 \x01(\x0b\x32\x1a.cohesity.UniversalIdProto\x12I\n\x10\x62\x61\x63kup_run_state\x18\x02 \x01(\x0b\x32/.cohesity.magneto.master.BackupJobRunStateProto\x12+\n\x05\x65rror\x18\x03 \x01(\x0b\x32\x1c.cohesity.magneto.ErrorProto\x12\x1d\n\x15snapshot_expiry_usecs\x18\x04 \x01(\x03\x12\x1a\n\x12legal_hold_enabled\x18\x05 \x01(\x08\x12M\n\x15\x64\x61ta_lock_constraints\x18\x06 \x01(\x0b\x32..cohesity.magneto.api.DataLockConstraintsProto\x12\x1d\n\x15initiated_by_dso_role\x18\x07 \x01(\x08\"\xd4\x01\n\x13\x43\x64pEntityRequestArg\x12\x15\n\tentity_id\x18\x01 \x01(\x03:\x02-1\x12O\n\x18get_cdp_entity_state_arg\x18\x02 \x01(\x0b\x32-.cohesity.magneto.master.GetCdpEntityStateArg\x12U\n\x1bupdate_cdp_entity_state_arg\x18\x03 \x01(\x0b\x32\x30.cohesity.magneto.master.UpdateCdpEntityStateArg\"o\n\x16\x43\x64pEntityRequestResult\x12U\n\x1bget_cdp_entity_state_result\x18\x01 \x01(\x0b\x32\x30.cohesity.magneto.master.GetCdpEntityStateResult\"3\n\x17UpdateCdpEntityStateArg\x12\x18\n\nenable_cdp\x18\x01 \x01(\x08:\x04true\"\\\n\x14GetCdpEntityStateArg\x12&\n\x1einclude_entity_cdp_state_proto\x18\x01 \x01(\x08\x12\x1c\n\x14include_restore_info\x18\x02 \x01(\x08\"\xbe\x02\n\x17GetCdpEntityStateResult\x12L\n\x16\x65ntity_cdp_state_proto\x18\x01 \x01(\x0b\x32,.cohesity.magneto.master.EntityCdpStateProto\x12_\n\x13\x65ntity_restore_info\x18\x02 \x01(\x0b\x32\x42.cohesity.magneto.master.GetCdpEntityStateResult.EntityRestoreInfo\x1at\n\x11\x45ntityRestoreInfo\x12&\n\x17is_waiting_for_snapshot\x18\x01 \x01(\x08:\x05\x66\x61lse\x12\x37\n\thole_info\x18\x02 \x01(\x0b\x32$.cohesity.magneto.master.CDPHoleInfo\"\x96\x03\n\x18RemoteReplicationActions\x12\x43\n\x16rx_cluster_instance_id\x18\x04 \x01(\x0b\x32#.cohesity.ClusterInstanceIdentifier\x12I\n\x14get_capabilities_arg\x18\x03 \x01(\x0b\x32+.cohesity.magneto.master.GetCapabilitiesArg\x12O\n\x15start_replication_arg\x18\x01 \x01(\x0b\x32\x30.cohesity.magneto.master.StartReplicationTaskArg\x12K\n\x13\x65nd_replication_arg\x18\x02 \x01(\x0b\x32..cohesity.magneto.master.EndReplicationTaskArg\x12L\n\x16\x63\x64p_entity_request_arg\x18\x05 \x01(\x0b\x32,.cohesity.magneto.master.CdpEntityRequestArg\"\xdd\x02\n\x1eRemoteReplicationActionsResult\x12O\n\x17get_capabilities_result\x18\x02 \x01(\x0b\x32..cohesity.magneto.master.GetCapabilitiesResult\x12U\n\x18start_replication_result\x18\x03 \x01(\x0b\x32\x33.cohesity.magneto.master.StartReplicationTaskResult\x12R\n\x19\x63\x64p_entity_request_result\x18\x04 \x01(\x0b\x32/.cohesity.magneto.master.CdpEntityRequestResult\x12?\n\x10\x63\x61pability_proto\x18\x01 \x01(\x0b\x32!.cohesity.magneto.CapabilityProtoB\x02\x18\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'magneto.master.base.remote_actions_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_REMOTEREPLICATIONACTIONSRESULT'].fields_by_name['capability_proto']._loaded_options = None
  _globals['_REMOTEREPLICATIONACTIONSRESULT'].fields_by_name['capability_proto']._serialized_options = b'\030\001'
  _globals['_GETCAPABILITIESARG']._serialized_start=470
  _globals['_GETCAPABILITIESARG']._serialized_end=490
  _globals['_GETCAPABILITIESRESULT']._serialized_start=492
  _globals['_GETCAPABILITIESRESULT']._serialized_end=576
  _globals['_STARTREPLICATIONTASKARG']._serialized_start=579
  _globals['_STARTREPLICATIONTASKARG']._serialized_end=1424
  _globals['_STARTREPLICATIONTASKRESULT']._serialized_start=1427
  _globals['_STARTREPLICATIONTASKRESULT']._serialized_end=1704
  _globals['_ENDREPLICATIONTASKARG']._serialized_start=1707
  _globals['_ENDREPLICATIONTASKARG']._serialized_end=2065
  _globals['_CDPENTITYREQUESTARG']._serialized_start=2068
  _globals['_CDPENTITYREQUESTARG']._serialized_end=2280
  _globals['_CDPENTITYREQUESTRESULT']._serialized_start=2282
  _globals['_CDPENTITYREQUESTRESULT']._serialized_end=2393
  _globals['_UPDATECDPENTITYSTATEARG']._serialized_start=2395
  _globals['_UPDATECDPENTITYSTATEARG']._serialized_end=2446
  _globals['_GETCDPENTITYSTATEARG']._serialized_start=2448
  _globals['_GETCDPENTITYSTATEARG']._serialized_end=2540
  _globals['_GETCDPENTITYSTATERESULT']._serialized_start=2543
  _globals['_GETCDPENTITYSTATERESULT']._serialized_end=2861
  _globals['_GETCDPENTITYSTATERESULT_ENTITYRESTOREINFO']._serialized_start=2745
  _globals['_GETCDPENTITYSTATERESULT_ENTITYRESTOREINFO']._serialized_end=2861
  _globals['_REMOTEREPLICATIONACTIONS']._serialized_start=2864
  _globals['_REMOTEREPLICATIONACTIONS']._serialized_end=3270
  _globals['_REMOTEREPLICATIONACTIONSRESULT']._serialized_start=3273
  _globals['_REMOTEREPLICATIONACTIONSRESULT']._serialized_end=3622
# @@protoc_insertion_point(module_scope)
