# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bridge/nfs_portal/nfs41.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from bridge.snap_fs import entity_handle_pb2 as bridge_dot_snap__fs_dot_entity__handle__pb2
from util.base import op_clock_pb2 as util_dot_base_dot_op__clock__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1d\x62ridge/nfs_portal/nfs41.proto\x12\x16\x63ohesity.bridge.nfs.v4\x1a\"bridge/snap_fs/entity_handle.proto\x1a\x18util/base/op_clock.proto\"\\\n\x08TableKey\x12\x17\n\x0f\x63lient_owner_id\x18\x01 \x01(\x0c\x12\x11\n\tclient_id\x18\x02 \x01(\x03\x12\x12\n\nsession_id\x18\x03 \x01(\x03\x12\x10\n\x08state_id\x18\x04 \x01(\x03\"\xc4\x0c\n\nTableValue\x12]\n\x17\x63lient_owner_id_mapping\x18\x01 \x03(\x0b\x32<.cohesity.bridge.nfs.v4.TableValue.ClientOwnerIdMappingEntry\x12R\n\x11server_ip_mapping\x18\x05 \x03(\x0b\x32\x37.cohesity.bridge.nfs.v4.TableValue.ServerIpMappingEntry\x12M\n\x11\x63lient_id_mapping\x18\x02 \x01(\x0b\x32\x32.cohesity.bridge.nfs.v4.TableValue.ClientIdMapping\x12O\n\x12session_id_mapping\x18\x03 \x01(\x0b\x32\x33.cohesity.bridge.nfs.v4.TableValue.SessionIdMapping\x12K\n\x10state_id_mapping\x18\x04 \x01(\x0b\x32\x31.cohesity.bridge.nfs.v4.TableValue.StateIdMapping\x1a;\n\x19\x43lientOwnerIdMappingEntry\x12\x0b\n\x03key\x18\x01 \x01(\x03\x12\r\n\x05value\x18\x02 \x01(\x04:\x02\x38\x01\x1a\x36\n\x14ServerIpMappingEntry\x12\x0b\n\x03key\x18\x01 \x01(\x03\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\x8a\x04\n\x0f\x43lientIdMapping\x12\x17\n\x0f\x63lient_owner_id\x18\x01 \x02(\x0c\x12\x10\n\x08verifier\x18\x02 \x02(\x04\x12\x11\n\tserver_ip\x18\x08 \x01(\t\x12\x18\n\x10\x65xpiration_usecs\x18\x03 \x01(\x03\x12\x16\n\x0esession_id_vec\x18\x04 \x03(\x03\x12\x14\n\x0cstate_id_vec\x18\x07 \x03(\x03\x12V\n\rupdate_intent\x18\x05 \x01(\x0b\x32?.cohesity.bridge.nfs.v4.TableValue.ClientIdMapping.UpdateIntent\x12\x66\n\x12\x63s_reply_cache_vec\x18\x06 \x03(\x0b\x32J.cohesity.bridge.nfs.v4.TableValue.ClientIdMapping.CreateSessionReplyCache\x1au\n\x0cUpdateIntent\x12\"\n\x07opclock\x18\x01 \x01(\x0b\x32\x11.cohesity.OpClock\x12\x13\n\x0bis_creation\x18\x02 \x01(\x08\x12\x16\n\x0esession_id_vec\x18\x03 \x03(\x03\x12\x14\n\x0cstate_id_vec\x18\x04 \x03(\x03\x1a:\n\x17\x43reateSessionReplyCache\x12\x12\n\nsession_id\x18\x01 \x02(\x03\x12\x0b\n\x03seq\x18\x02 \x02(\x04\x1a\x34\n\x10SessionIdMapping\x12\x11\n\tclient_id\x18\x01 \x02(\x03\x12\r\n\x05\x66lags\x18\x02 \x01(\r\x1a\xdd\x03\n\x0eStateIdMapping\x12\x11\n\tclient_id\x18\x01 \x02(\x03\x12\x12\n\nsession_id\x18\x02 \x02(\x03\x12\x41\n\rentity_handle\x18\x03 \x02(\x0b\x32*.cohesity.bridge.snap_fs.EntityHandleProto\x12\x0e\n\x03seq\x18\x04 \x01(\r:\x01\x31\x12S\n\x0copen_details\x18\x05 \x01(\x0b\x32=.cohesity.bridge.nfs.v4.TableValue.StateIdMapping.OpenDetails\x12S\n\x0clock_details\x18\x06 \x01(\x0b\x32=.cohesity.bridge.nfs.v4.TableValue.StateIdMapping.LockDetails\x1ap\n\x0bOpenDetails\x12\x0f\n\x07open_id\x18\x01 \x02(\x03\x12\x0e\n\x06\x61\x63\x63\x65ss\x18\x02 \x01(\r\x12\x14\n\x0cshare_access\x18\x03 \x01(\r\x12\x12\n\nshare_deny\x18\x04 \x01(\r\x12\x16\n\x0elock_state_ids\x18\x05 \x03(\x03\x1a\x35\n\x0bLockDetails\x12\x15\n\ropen_state_id\x18\x01 \x02(\x03\x12\x0f\n\x07open_id\x18\x02 \x02(\x03')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'bridge.nfs_portal.nfs41_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_TABLEVALUE_CLIENTOWNERIDMAPPINGENTRY']._loaded_options = None
  _globals['_TABLEVALUE_CLIENTOWNERIDMAPPINGENTRY']._serialized_options = b'8\001'
  _globals['_TABLEVALUE_SERVERIPMAPPINGENTRY']._loaded_options = None
  _globals['_TABLEVALUE_SERVERIPMAPPINGENTRY']._serialized_options = b'8\001'
  _globals['_TABLEKEY']._serialized_start=119
  _globals['_TABLEKEY']._serialized_end=211
  _globals['_TABLEVALUE']._serialized_start=214
  _globals['_TABLEVALUE']._serialized_end=1818
  _globals['_TABLEVALUE_CLIENTOWNERIDMAPPINGENTRY']._serialized_start=644
  _globals['_TABLEVALUE_CLIENTOWNERIDMAPPINGENTRY']._serialized_end=703
  _globals['_TABLEVALUE_SERVERIPMAPPINGENTRY']._serialized_start=705
  _globals['_TABLEVALUE_SERVERIPMAPPINGENTRY']._serialized_end=759
  _globals['_TABLEVALUE_CLIENTIDMAPPING']._serialized_start=762
  _globals['_TABLEVALUE_CLIENTIDMAPPING']._serialized_end=1284
  _globals['_TABLEVALUE_CLIENTIDMAPPING_UPDATEINTENT']._serialized_start=1107
  _globals['_TABLEVALUE_CLIENTIDMAPPING_UPDATEINTENT']._serialized_end=1224
  _globals['_TABLEVALUE_CLIENTIDMAPPING_CREATESESSIONREPLYCACHE']._serialized_start=1226
  _globals['_TABLEVALUE_CLIENTIDMAPPING_CREATESESSIONREPLYCACHE']._serialized_end=1284
  _globals['_TABLEVALUE_SESSIONIDMAPPING']._serialized_start=1286
  _globals['_TABLEVALUE_SESSIONIDMAPPING']._serialized_end=1338
  _globals['_TABLEVALUE_STATEIDMAPPING']._serialized_start=1341
  _globals['_TABLEVALUE_STATEIDMAPPING']._serialized_end=1818
  _globals['_TABLEVALUE_STATEIDMAPPING_OPENDETAILS']._serialized_start=1651
  _globals['_TABLEVALUE_STATEIDMAPPING_OPENDETAILS']._serialized_end=1763
  _globals['_TABLEVALUE_STATEIDMAPPING_LOCKDETAILS']._serialized_start=1765
  _globals['_TABLEVALUE_STATEIDMAPPING_LOCKDETAILS']._serialized_end=1818
# @@protoc_insertion_point(module_scope)