# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: magneto/failover/stub/rpc_service.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from magneto.api import magneto_external_base_pb2 as magneto_dot_api_dot_magneto__external__base__pb2
from magneto.base import error_pb2 as magneto_dot_base_dot_error__pb2
from magneto.failover import failover_state_pb2 as magneto_dot_failover_dot_failover__state__pb2
from open_util.net import protorpc_pb2 as open__util_dot_net_dot_protorpc__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'magneto/failover/stub/rpc_service.proto\x12\x1e\x63ohesity.magneto.failover.stub\x1a\'magneto/api/magneto_external_base.proto\x1a\x18magneto/base/error.proto\x1a%magneto/failover/failover_state.proto\x1a\x1copen_util/net/protorpc.proto\"\xac\x03\n\x17\x46\x65tchFailoverCommandArg\x12\x15\n\rtx_cluster_id\x18\x01 \x01(\x03\x12!\n\x19tx_cluster_incarnation_id\x18\x02 \x01(\x03\x12\x1e\n\x16\x65xpected_rx_cluster_id\x18\x03 \x01(\x03\x12*\n\"expected_rx_cluster_incarnation_id\x18\x04 \x01(\x03\x12\x14\n\x0cis_forwarded\x18\x05 \x01(\x08\x12x\n\x1e\x66\x61ilover_replication_stats_vec\x18\x06 \x03(\x0b\x32P.cohesity.magneto.failover.stub.FetchFailoverCommandArg.FailoverReplicationStats\x1a{\n\x18\x46\x61iloverReplicationStats\x12\x14\n\x0c\x66\x61ilover_uid\x18\x01 \x01(\t\x12I\n\x15replication_stats_vec\x18\x02 \x03(\x0b\x32*.cohesity.magneto.api.ReplicationInfoProto\"\x9a\x01\n\x1a\x46\x65tchFailoverCommandResult\x12+\n\x05\x65rror\x18\x01 \x01(\x0b\x32\x1c.cohesity.magneto.ErrorProto\x12O\n\x18\x66\x61ilover_command_arg_vec\x18\x02 \x03(\x0b\x32-.cohesity.magneto.failover.FailoverCommandArg\"\xd9\x03\n!DeliverFailoverCommandResponseArg\x12\x15\n\rtx_cluster_id\x18\x01 \x01(\x03\x12!\n\x19tx_cluster_incarnation_id\x18\x02 \x01(\x03\x12\x1e\n\x16\x65xpected_rx_cluster_id\x18\x03 \x01(\x03\x12*\n\"expected_rx_cluster_incarnation_id\x18\x04 \x01(\x03\x12m\n\x1b\x66\x61ilover_command_result_vec\x18\x05 \x03(\x0b\x32H.cohesity.magneto.failover.stub.DeliverFailoverCommandResponseArg.Result\x12\x14\n\x0cis_forwarded\x18\x06 \x01(\x08\x1a\xa8\x01\n\x06Result\x12K\n\x14\x66\x61ilover_command_arg\x18\x01 \x01(\x0b\x32-.cohesity.magneto.failover.FailoverCommandArg\x12Q\n\x17\x66\x61ilover_command_result\x18\x02 \x01(\x0b\x32\x30.cohesity.magneto.failover.FailoverCommandResult\"S\n$DeliverFailoverCommandResponseResult\x12+\n\x05\x65rror\x18\x01 \x01(\x0b\x32\x1c.cohesity.magneto.ErrorProto2\xda\x02\n\nRpcService\x12\x8d\x01\n\x14\x46\x65tchFailoverCommand\x12\x37.cohesity.magneto.failover.stub.FetchFailoverCommandArg\x1a:.cohesity.magneto.failover.stub.FetchFailoverCommandResult\"\x00\x12\xab\x01\n\x1e\x44\x65liverFailoverCommandResponse\x12\x41.cohesity.magneto.failover.stub.DeliverFailoverCommandResponseArg\x1a\x44.cohesity.magneto.failover.stub.DeliverFailoverCommandResponseResult\"\x00\x1a\x0e\x80\xf1\x04\xc8\xdf\x02\x88\xf1\x04\x00\x90\xf1\x04\x00\x42\x03\x80\x01\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'magneto.failover.stub.rpc_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\200\001\001'
  _globals['_RPCSERVICE']._loaded_options = None
  _globals['_RPCSERVICE']._serialized_options = b'\200\361\004\310\337\002\210\361\004\000\220\361\004\000'
  _globals['_FETCHFAILOVERCOMMANDARG']._serialized_start=212
  _globals['_FETCHFAILOVERCOMMANDARG']._serialized_end=640
  _globals['_FETCHFAILOVERCOMMANDARG_FAILOVERREPLICATIONSTATS']._serialized_start=517
  _globals['_FETCHFAILOVERCOMMANDARG_FAILOVERREPLICATIONSTATS']._serialized_end=640
  _globals['_FETCHFAILOVERCOMMANDRESULT']._serialized_start=643
  _globals['_FETCHFAILOVERCOMMANDRESULT']._serialized_end=797
  _globals['_DELIVERFAILOVERCOMMANDRESPONSEARG']._serialized_start=800
  _globals['_DELIVERFAILOVERCOMMANDRESPONSEARG']._serialized_end=1273
  _globals['_DELIVERFAILOVERCOMMANDRESPONSEARG_RESULT']._serialized_start=1105
  _globals['_DELIVERFAILOVERCOMMANDRESPONSEARG_RESULT']._serialized_end=1273
  _globals['_DELIVERFAILOVERCOMMANDRESPONSERESULT']._serialized_start=1275
  _globals['_DELIVERFAILOVERCOMMANDRESPONSERESULT']._serialized_end=1358
  _globals['_RPCSERVICE']._serialized_start=1361
  _globals['_RPCSERVICE']._serialized_end=1707
# @@protoc_insertion_point(module_scope)
