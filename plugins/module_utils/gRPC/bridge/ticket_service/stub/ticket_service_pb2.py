# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bridge/ticket_service/stub/ticket_service.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from open_util.net import protorpc_pb2 as open__util_dot_net_dot_protorpc__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/bridge/ticket_service/stub/ticket_service.proto\x12\x1b\x63ohesity.bridge.ticket.stub\x1a\x1copen_util/net/protorpc.proto\"\xf2\x02\n\nAcquireArg\x12\x11\n\tdomain_id\x18\x01 \x02(\x03\x12\x11\n\tentity_id\x18\x02 \x02(\x03\x12\x1a\n\x0cis_exclusive\x18\x03 \x01(\x08:\x04true\x12\x13\n\x0b\x63\x61n_forward\x18\x04 \x01(\x08\x12\x1a\n\x0erecall_if_idle\x18\x07 \x01(\x08\x42\x02\x18\x01\x12\x18\n\x10slave_session_id\x18\x05 \x02(\x03\x12 \n\x18slave_has_pinned_tickets\x18\x06 \x01(\x08\x12\x15\n\racquire_token\x18\x08 \x01(\x03\x12\x32\n$need_remote_session_id_if_not_pinned\x18\t \x01(\x08:\x04true\x12*\n\x1e\x65xpected_ticket_sequencer_high\x18\x0b \x01(\x03:\x02-1\x12)\n\x1d\x65xpected_ticket_sequencer_low\x18\x0c \x01(\x03:\x02-1\x12\x13\n\x0brpc_version\x18\n \x01(\x03\"\xe0\x01\n\rAcquireResult\x12\x14\n\x0cis_exclusive\x18\x01 \x01(\x03\x12\x1f\n\x17remote_slave_session_id\x18\x02 \x01(\x03\x12\x1d\n\x15ticket_sequencer_high\x18\x03 \x01(\x03\x12\x1c\n\x14ticket_sequencer_low\x18\x04 \x01(\x03\x12\x32\n*last_exclusive_holder_death_relative_usecs\x18\x05 \x01(\x03\x12\'\n\x1flast_slave_death_relative_usecs\x18\x06 \x01(\x03\"J\n\x07IdleArg\x12\x11\n\tdomain_id\x18\x01 \x02(\x03\x12\x12\n\nentity_vec\x18\x02 \x03(\x03\x12\x18\n\x10slave_session_id\x18\x03 \x02(\x03\"\x0c\n\nIdleResult\"\xbd\x01\n\tRecallArg\x12\x11\n\tdomain_id\x18\x01 \x02(\x03\x12\x11\n\tentity_id\x18\x02 \x02(\x03\x12\x16\n\x0erecall_if_idle\x18\x03 \x01(\x08\x12\x1d\n\x15recall_exclusive_only\x18\x04 \x01(\x08\x12\x18\n\x10master_sequencer\x18\x05 \x02(\x03\x12\x15\n\racquire_token\x18\x06 \x01(\x03\x12\"\n\x1ainitiator_slave_session_id\x18\x07 \x01(\x03\"D\n\x0cRecallResult\x12\x1a\n\x0crecalled_all\x18\x01 \x01(\x08:\x04true\x12\x18\n\x10slave_session_id\x18\x02 \x02(\x03\"`\n\tGetAllArg\x12\x11\n\tdomain_id\x18\x01 \x02(\x03\x12\x18\n\x10master_sequencer\x18\x02 \x02(\x03\x12\x11\n\tmaster_ip\x18\x03 \x02(\t\x12\x13\n\x0bmaster_port\x18\x04 \x02(\x05\"\xcf\x01\n\x0cGetAllResult\x12\x18\n\x10slave_session_id\x18\x01 \x02(\x03\x12\x12\n\nentity_vec\x18\x02 \x03(\x03\x12\x18\n\x10is_exclusive_vec\x18\x03 \x03(\x08\x12!\n\x19ticket_sequencer_high_vec\x18\x04 \x03(\x03\x12 \n\x18ticket_sequencer_low_vec\x18\x05 \x03(\x03\x12\x32\n*last_exclusive_holder_death_relative_usecs\x18\x06 \x03(\x03\"R\n\x14GetOwnerSessionIdArg\x12\x11\n\tdomain_id\x18\x01 \x02(\x03\x12\x11\n\tentity_id\x18\x02 \x02(\x03\x12\x14\n\x0cis_exclusive\x18\x03 \x01(\x08\"3\n\x17GetOwnerSessionIdResult\x12\x18\n\x10slave_session_id\x18\x01 \x02(\x03\x32\x94\x04\n\nRpcService\x12`\n\x07\x41\x63quire\x12\'.cohesity.bridge.ticket.stub.AcquireArg\x1a*.cohesity.bridge.ticket.stub.AcquireResult\"\x00\x12W\n\x04Idle\x12$.cohesity.bridge.ticket.stub.IdleArg\x1a\'.cohesity.bridge.ticket.stub.IdleResult\"\x00\x12]\n\x06Recall\x12&.cohesity.bridge.ticket.stub.RecallArg\x1a).cohesity.bridge.ticket.stub.RecallResult\"\x00\x12]\n\x06GetAll\x12&.cohesity.bridge.ticket.stub.GetAllArg\x1a).cohesity.bridge.ticket.stub.GetAllResult\"\x00\x12~\n\x11GetOwnerSessionId\x12\x31.cohesity.bridge.ticket.stub.GetOwnerSessionIdArg\x1a\x34.cohesity.bridge.ticket.stub.GetOwnerSessionIdResult\"\x00\x1a\r\x80\xf1\x04\xa0\x1f\x88\xf1\x04\x01\x90\xf1\x04\x02\x42\x03\x80\x01\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'bridge.ticket_service.stub.ticket_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\200\001\001'
  _globals['_ACQUIREARG'].fields_by_name['recall_if_idle']._loaded_options = None
  _globals['_ACQUIREARG'].fields_by_name['recall_if_idle']._serialized_options = b'\030\001'
  _globals['_RPCSERVICE']._loaded_options = None
  _globals['_RPCSERVICE']._serialized_options = b'\200\361\004\240\037\210\361\004\001\220\361\004\002'
  _globals['_ACQUIREARG']._serialized_start=111
  _globals['_ACQUIREARG']._serialized_end=481
  _globals['_ACQUIRERESULT']._serialized_start=484
  _globals['_ACQUIRERESULT']._serialized_end=708
  _globals['_IDLEARG']._serialized_start=710
  _globals['_IDLEARG']._serialized_end=784
  _globals['_IDLERESULT']._serialized_start=786
  _globals['_IDLERESULT']._serialized_end=798
  _globals['_RECALLARG']._serialized_start=801
  _globals['_RECALLARG']._serialized_end=990
  _globals['_RECALLRESULT']._serialized_start=992
  _globals['_RECALLRESULT']._serialized_end=1060
  _globals['_GETALLARG']._serialized_start=1062
  _globals['_GETALLARG']._serialized_end=1158
  _globals['_GETALLRESULT']._serialized_start=1161
  _globals['_GETALLRESULT']._serialized_end=1368
  _globals['_GETOWNERSESSIONIDARG']._serialized_start=1370
  _globals['_GETOWNERSESSIONIDARG']._serialized_end=1452
  _globals['_GETOWNERSESSIONIDRESULT']._serialized_start=1454
  _globals['_GETOWNERSESSIONIDRESULT']._serialized_end=1505
  _globals['_RPCSERVICE']._serialized_start=1508
  _globals['_RPCSERVICE']._serialized_end=2040
# @@protoc_insertion_point(module_scope)