# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bridge/cloud_snaptree_repository/base/csr.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from bridge.cloud_snaptree_repository.stub import csr_pb2 as bridge_dot_cloud__snaptree__repository_dot_stub_dot_csr__pb2
from bridge.cloud_snaptree_repository.server import cloud_object_pb2 as bridge_dot_cloud__snaptree__repository_dot_server_dot_cloud__object__pb2
from bridge.vault.base import worm_pb2 as bridge_dot_vault_dot_base_dot_worm__pb2
from util.base import op_clock_pb2 as util_dot_base_dot_op__clock__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/bridge/cloud_snaptree_repository/base/csr.proto\x12\x18\x63ohesity.bridge.csr.base\x1a/bridge/cloud_snaptree_repository/stub/csr.proto\x1a:bridge/cloud_snaptree_repository/server/cloud_object.proto\x1a\x1c\x62ridge/vault/base/worm.proto\x1a\x18util/base/op_clock.proto\"\xb9\x01\n\x0eKeysStateProto\x12H\n\rkey_state_vec\x18\x01 \x03(\x0b\x32\x31.cohesity.bridge.csr.base.KeysStateProto.KeyState\x1a]\n\x08KeyState\x12\x41\n\x03key\x18\x01 \x01(\x0e\x32\x34.cohesity.bridge.csr.stub.FetchCloudObjectIdsArg.Key\x12\x0e\n\x06max_id\x18\x02 \x01(\x03\"\xed\n\n\x1e\x43loudObjectScribeMetadataProto\x12\x10\n\x08\x65poch_id\x18\x01 \x01(\x03\x12&\n\x0bopclock_vec\x18\r \x03(\x0b\x32\x11.cohesity.OpClock\x12\x1e\n\x16last_update_time_usecs\x18\n \x01(\x03\x12\x1c\n\x14\x63loud_object_version\x18\x02 \x01(\x03\x12S\n\x11\x63loud_object_type\x18\x03 \x01(\x0e\x32\x38.cohesity.bridge.csr.CloudObjectMetadataProto.ObjectType\x12\x0e\n\x06prefix\x18\t \x01(\t\x12X\n\x0bobject_info\x18\x04 \x01(\x0b\x32\x43.cohesity.bridge.csr.base.CloudObjectScribeMetadataProto.ObjectInfo\x12\x1b\n\x13intent_id_generator\x18\x05 \x01(\x03\x12 \n\x18update_intent_session_id\x18\x06 \x01(\x03\x12\\\n\rupdate_intent\x18\x07 \x01(\x0b\x32\x45.cohesity.bridge.csr.base.CloudObjectScribeMetadataProto.UpdateIntent\x12\x19\n\nis_deleted\x18\x0b \x01(\x08:\x05\x66\x61lse\x12\x19\n\x11num_deleted_nodes\x18\x0c \x01(\x05\x12,\n minimum_retention_timestamp_secs\x18\x0e \x01(\x03:\x02-1\x12\x41\n\x0eretention_mode\x18\x10 \x01(\x0e\x32).cohesity.bridge.vault.RetentionMode.Type\x12`\n!worm_retention_extendability_info\x18\x11 \x01(\x0b\x32\x35.cohesity.bridge.vault.WORMRetentionExtendabilityInfo\x12\x1b\n\x13versioned_object_id\x18\x0f \x01(\t\x1aN\n\nObjectInfo\x12\x15\n\rsegment_count\x18\x01 \x01(\x05\x12\x13\n\x0b\x65ntry_count\x18\x02 \x01(\x05\x12\x14\n\x0cmorphed_size\x18\x03 \x01(\x05\x1a\x80\x04\n\x0cUpdateIntent\x12\x11\n\tintent_id\x18\x01 \x01(\x03\x12\x1b\n\x13\x63reation_time_usecs\x18\x02 \x01(\x03\x12g\n\x0cwrite_object\x18\x03 \x01(\x0b\x32Q.cohesity.bridge.csr.base.CloudObjectScribeMetadataProto.UpdateIntent.WriteObject\x12i\n\rdelete_object\x18\x04 \x01(\x0b\x32R.cohesity.bridge.csr.base.CloudObjectScribeMetadataProto.UpdateIntent.DeleteObject\x1a\xdb\x01\n\x0bWriteObject\x12\x1c\n\x14\x63loud_object_written\x18\x01 \x01(\x08\x12\x10\n\x08\x65poch_id\x18\x03 \x01(\x03\x12X\n\x0bobject_info\x18\x02 \x01(\x0b\x32\x43.cohesity.bridge.csr.base.CloudObjectScribeMetadataProto.ObjectInfo\x12\x1c\n\rnodes_deleted\x18\x04 \x01(\x08:\x05\x66\x61lse\x12$\n\x15safe_to_delete_object\x18\x05 \x01(\x08:\x05\x66\x61lse\x1a\x0e\n\x0c\x44\x65leteObject\"A\n!CloudObjectScribeDeletedInfoProto\x12\x1c\n\x14\x64\x65leted_local_id_vec\x18\x01 \x03(\x03')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'bridge.cloud_snaptree_repository.base.csr_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_KEYSSTATEPROTO']._serialized_start=243
  _globals['_KEYSSTATEPROTO']._serialized_end=428
  _globals['_KEYSSTATEPROTO_KEYSTATE']._serialized_start=335
  _globals['_KEYSSTATEPROTO_KEYSTATE']._serialized_end=428
  _globals['_CLOUDOBJECTSCRIBEMETADATAPROTO']._serialized_start=431
  _globals['_CLOUDOBJECTSCRIBEMETADATAPROTO']._serialized_end=1820
  _globals['_CLOUDOBJECTSCRIBEMETADATAPROTO_OBJECTINFO']._serialized_start=1227
  _globals['_CLOUDOBJECTSCRIBEMETADATAPROTO_OBJECTINFO']._serialized_end=1305
  _globals['_CLOUDOBJECTSCRIBEMETADATAPROTO_UPDATEINTENT']._serialized_start=1308
  _globals['_CLOUDOBJECTSCRIBEMETADATAPROTO_UPDATEINTENT']._serialized_end=1820
  _globals['_CLOUDOBJECTSCRIBEMETADATAPROTO_UPDATEINTENT_WRITEOBJECT']._serialized_start=1585
  _globals['_CLOUDOBJECTSCRIBEMETADATAPROTO_UPDATEINTENT_WRITEOBJECT']._serialized_end=1804
  _globals['_CLOUDOBJECTSCRIBEMETADATAPROTO_UPDATEINTENT_DELETEOBJECT']._serialized_start=1806
  _globals['_CLOUDOBJECTSCRIBEMETADATAPROTO_UPDATEINTENT_DELETEOBJECT']._serialized_end=1820
  _globals['_CLOUDOBJECTSCRIBEDELETEDINFOPROTO']._serialized_start=1822
  _globals['_CLOUDOBJECTSCRIBEDELETEDINFOPROTO']._serialized_end=1887
# @@protoc_insertion_point(module_scope)
