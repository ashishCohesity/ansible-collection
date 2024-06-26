# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bridge/madrox/master_WAL.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from bridge.base import error_pb2 as bridge_dot_base_dot_error__pb2
from bridge.madrox import master_replication_state_pb2 as bridge_dot_madrox_dot_master__replication__state__pb2
from bridge.madrox import master_state_pb2 as bridge_dot_madrox_dot_master__state__pb2
from util.base import universal_id_pb2 as util_dot_base_dot_universal__id__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1e\x62ridge/madrox/master_WAL.proto\x12\x16\x63ohesity.bridge.madrox\x1a\x17\x62ridge/base/error.proto\x1a,bridge/madrox/master_replication_state.proto\x1a bridge/madrox/master_state.proto\x1a\x1cutil/base/universal_id.proto\"\x92 \n\x14MasterWALRecordProto\x12R\n\x15replication_state_vec\x18\x01 \x03(\x0b\x32\x33.cohesity.bridge.madrox.MasterReplicationStateProto\x12\x39\n\x15rid_mark_for_deletion\x18\x02 \x01(\x0b\x32\x1a.cohesity.UniversalIdProto\x12.\n\nrid_delete\x18\x03 \x01(\x0b\x32\x1a.cohesity.UniversalIdProto\x12_\n\x15mark_for_cancellation\x18\x04 \x01(\x0b\x32@.cohesity.bridge.madrox.MasterWALRecordProto.MarkForCancellation\x12.\n\nrid_cancel\x18\x05 \x01(\x0b\x32\x1a.cohesity.UniversalIdProto\x12;\n\x17rid_completion_notified\x18\x06 \x01(\x0b\x32\x1a.cohesity.UniversalIdProto\x12[\n\x13pin_unpin_ancestors\x18\x07 \x01(\x0b\x32>.cohesity.bridge.madrox.MasterWALRecordProto.PinUnpinAncestors\x12\\\n\x13handshake_completed\x18\x08 \x01(\x0b\x32?.cohesity.bridge.madrox.MasterWALRecordProto.HandshakeCompleted\x12T\n\x0fprogress_report\x18\t \x01(\x0b\x32;.cohesity.bridge.madrox.MasterWALRecordProto.ProgressReport\x12N\n\x0c\x61ssign_slave\x18\n \x01(\x0b\x32\x38.cohesity.bridge.madrox.MasterWALRecordProto.AssignSlave\x12^\n\x14\x63omplete_replication\x18\x0b \x01(\x0b\x32@.cohesity.bridge.madrox.MasterWALRecordProto.CompleteReplication\x12=\n\x19rid_marked_for_expiration\x18\x0c \x01(\x0b\x32\x1a.cohesity.UniversalIdProto\x12-\n%application_job_marked_for_expiration\x18\r \x01(\x03\x12\x1f\n\x17\x61pplication_job_expired\x18\x0e \x01(\x03\x12N\n*rid_backup_or_restore_quota_data_completed\x18\x0f \x01(\x0b\x32\x1a.cohesity.UniversalIdProto\x12O\n\x17remote_cluster_info_vec\x18\x10 \x03(\x0b\x32..cohesity.bridge.madrox.RemoteClusterInfoProto\x12T\n\x1c\x61\x64\x64_or_update_remote_cluster\x18\x11 \x01(\x0b\x32..cohesity.bridge.madrox.RemoteClusterInfoProto\x12M\n\x15\x64\x65lete_remote_cluster\x18\x12 \x01(\x0b\x32..cohesity.bridge.madrox.RemoteClusterInfoProto\x12\x62\n\x17\x61\x64\x64_app_handler_context\x18\x13 \x01(\x0b\x32\x41.cohesity.bridge.madrox.MasterWALRecordProto.AddAppHandlerContext\x12Q\n\x0emark_for_pause\x18\x14 \x01(\x0b\x32\x39.cohesity.bridge.madrox.MasterWALRecordProto.MarkForPause\x12-\n\trid_pause\x18\x15 \x01(\x0b\x32\x1a.cohesity.UniversalIdProto\x12U\n\x10mark_for_unpause\x18\x16 \x01(\x0b\x32;.cohesity.bridge.madrox.MasterWALRecordProto.MarkForUnpause\x1aN\n\x13MarkForCancellation\x12\'\n\x03rid\x18\x01 \x02(\x0b\x32\x1a.cohesity.UniversalIdProto\x12\x0e\n\x06reason\x18\x02 \x01(\t\x1a\xbb\x01\n\x11PinUnpinAncestors\x12\x32\n\x0ereplication_id\x18\x01 \x02(\x0b\x32\x1a.cohesity.UniversalIdProto\x12\x34\n\x10\x61ncestor_rid_vec\x18\x02 \x03(\x0b\x32\x1a.cohesity.UniversalIdProto\x12\x13\n\x0bperform_pin\x18\x03 \x01(\x08\x12\'\n\x1funpin_for_completion_DEPRECATED\x18\x04 \x01(\x08\x1a\xe9\x05\n\x12HandshakeCompleted\x12\x32\n\x0ereplication_id\x18\x01 \x02(\x0b\x32\x1a.cohesity.UniversalIdProto\x12\x65\n\x14replication_protocol\x18\x02 \x02(\x0e\x32G.cohesity.bridge.madrox.MasterReplicationStateProto.ReplicationProtocol\x12\x12\n\ntime_usecs\x18\x03 \x02(\x03\x12\x19\n\x11remote_cluster_id\x18\x04 \x02(\x03\x12%\n\x1dremote_cluster_incarnation_id\x18\x05 \x02(\x03\x12\x15\n\rtx_viewbox_id\x18\x06 \x01(\x03\x12\x1d\n\x15rx_viewbox_brick_size\x18\x07 \x01(\x05\x12\x1e\n\x16session_encryption_key\x18\x08 \x01(\x0c\x12\x1d\n\x15rx_megafile_supported\x18\n \x01(\x08\x12&\n\x1eview_user_quota_data_supported\x18\x0b \x01(\x08\x12&\n\x1e\x63ompression_enabled_DEPRECATED\x18\t \x01(\x08\x12\x1f\n\x17replicate_special_files\x18\x0c \x01(\x08\x12\x14\n\x0ctmp_dir_name\x18\r \x01(\t\x12%\n\x1dview_dir_quota_data_supported\x18\x0e \x01(\x08\x12$\n\x1c\x65nable_dir_sync_verification\x18\x0f \x01(\x08\x12\x30\n\x0c\x61ncestor_rid\x18\x10 \x01(\x0b\x32\x1a.cohesity.UniversalIdProto\x12\x37\n/run_divergence_searching_and_fixing_replication\x18\x11 \x01(\x08\x12.\n&is_app_view_replication_divergent_safe\x18\x12 \x01(\x08\x1a\xc9\x05\n\x0eProgressReport\x12\x32\n\x0ereplication_id\x18\x01 \x02(\x0b\x32\x1a.cohesity.UniversalIdProto\x12\x18\n\x10slave_session_id\x18\x02 \x01(\x03\x12\x1f\n\x17slave_logical_timestamp\x18\x03 \x01(\x03\x12\x1e\n\x16slave_state_checkpoint\x18\x04 \x01(\x0c\x12\"\n\x1ametadata_actions_completed\x18\n \x01(\x03\x12\x1e\n\x16total_metadata_actions\x18\x0b \x01(\x03\x12\x15\n\rpct_completed\x18\x05 \x01(\x05\x12!\n\x19logical_bytes_transferred\x18\x06 \x01(\x03\x12\"\n\x1aphysical_bytes_transferred\x18\x07 \x01(\x03\x12\x19\n\x11view_logical_size\x18\t \x01(\x03\x12+\n#estimated_logical_bytes_to_transfer\x18\x0c \x01(\x03\x12\"\n\x1a\x65stimated_changed_entities\x18\r \x01(\x03\x12%\n\x1dsynced_files_logical_size_sum\x18\x0e \x01(\x03\x12+\n#logical_bytes_transferred_object_ns\x18\x0f \x01(\x03\x12,\n$metadata_actions_completed_object_ns\x18\x10 \x01(\x03\x12\"\n\x1a\x64ir_sync_progress_detected\x18\x11 \x01(\x08\x12H\n\x11replication_stats\x18\x12 \x01(\x0b\x32-.cohesity.bridge.madrox.ReplicationStatistics\x12*\n\x05\x65rror\x18\x08 \x01(\x0b\x32\x1b.cohesity.bridge.ErrorProto\x1ao\n\x0b\x41ssignSlave\x12\x32\n\x0ereplication_id\x18\x01 \x02(\x0b\x32\x1a.cohesity.UniversalIdProto\x12\x18\n\x10slave_session_id\x18\x02 \x02(\x03\x12\x12\n\ntime_usecs\x18\x03 \x01(\x03\x1a\xe0\x01\n\x13\x43ompleteReplication\x12\x32\n\x0ereplication_id\x18\x01 \x02(\x0b\x32\x1a.cohesity.UniversalIdProto\x12\x12\n\ntime_usecs\x18\x02 \x02(\x03\x12*\n\x05\x65rror\x18\x03 \x01(\x0b\x32\x1b.cohesity.bridge.ErrorProto\x12%\n\x1dis_tracking_view_already_live\x18\x04 \x01(\x08\x12.\n&is_app_view_replication_divergent_safe\x18\x05 \x01(\x08\x1a\xfb\x01\n\x14\x41\x64\x64\x41ppHandlerContext\x12\x32\n\x0ereplication_id\x18\x01 \x02(\x0b\x32\x1a.cohesity.UniversalIdProto\x12u\n\x13\x61pp_handler_context\x18\x02 \x03(\x0b\x32X.cohesity.bridge.madrox.MasterWALRecordProto.AddAppHandlerContext.AppHandlerContextEntry\x1a\x38\n\x16\x41ppHandlerContextEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1aG\n\x0cMarkForPause\x12\'\n\x03rid\x18\x01 \x01(\x0b\x32\x1a.cohesity.UniversalIdProto\x12\x0e\n\x06reason\x18\x02 \x01(\t\x1a\x39\n\x0eMarkForUnpause\x12\'\n\x03rid\x18\x01 \x01(\x0b\x32\x1a.cohesity.UniversalIdProto')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'bridge.madrox.master_WAL_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_MASTERWALRECORDPROTO_ADDAPPHANDLERCONTEXT_APPHANDLERCONTEXTENTRY']._loaded_options = None
  _globals['_MASTERWALRECORDPROTO_ADDAPPHANDLERCONTEXT_APPHANDLERCONTEXTENTRY']._serialized_options = b'8\001'
  _globals['_MASTERWALRECORDPROTO']._serialized_start=194
  _globals['_MASTERWALRECORDPROTO']._serialized_end=4308
  _globals['_MASTERWALRECORDPROTO_MARKFORCANCELLATION']._serialized_start=1850
  _globals['_MASTERWALRECORDPROTO_MARKFORCANCELLATION']._serialized_end=1928
  _globals['_MASTERWALRECORDPROTO_PINUNPINANCESTORS']._serialized_start=1931
  _globals['_MASTERWALRECORDPROTO_PINUNPINANCESTORS']._serialized_end=2118
  _globals['_MASTERWALRECORDPROTO_HANDSHAKECOMPLETED']._serialized_start=2121
  _globals['_MASTERWALRECORDPROTO_HANDSHAKECOMPLETED']._serialized_end=2866
  _globals['_MASTERWALRECORDPROTO_PROGRESSREPORT']._serialized_start=2869
  _globals['_MASTERWALRECORDPROTO_PROGRESSREPORT']._serialized_end=3582
  _globals['_MASTERWALRECORDPROTO_ASSIGNSLAVE']._serialized_start=3584
  _globals['_MASTERWALRECORDPROTO_ASSIGNSLAVE']._serialized_end=3695
  _globals['_MASTERWALRECORDPROTO_COMPLETEREPLICATION']._serialized_start=3698
  _globals['_MASTERWALRECORDPROTO_COMPLETEREPLICATION']._serialized_end=3922
  _globals['_MASTERWALRECORDPROTO_ADDAPPHANDLERCONTEXT']._serialized_start=3925
  _globals['_MASTERWALRECORDPROTO_ADDAPPHANDLERCONTEXT']._serialized_end=4176
  _globals['_MASTERWALRECORDPROTO_ADDAPPHANDLERCONTEXT_APPHANDLERCONTEXTENTRY']._serialized_start=4120
  _globals['_MASTERWALRECORDPROTO_ADDAPPHANDLERCONTEXT_APPHANDLERCONTEXTENTRY']._serialized_end=4176
  _globals['_MASTERWALRECORDPROTO_MARKFORPAUSE']._serialized_start=4178
  _globals['_MASTERWALRECORDPROTO_MARKFORPAUSE']._serialized_end=4249
  _globals['_MASTERWALRECORDPROTO_MARKFORUNPAUSE']._serialized_start=4251
  _globals['_MASTERWALRECORDPROTO_MARKFORUNPAUSE']._serialized_end=4308
# @@protoc_insertion_point(module_scope)
