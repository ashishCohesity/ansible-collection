# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gandalf/server/paxos/base/paxos.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from open_util.net import protorpc_pb2 as open__util_dot_net_dot_protorpc__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%gandalf/server/paxos/base/paxos.proto\x12\x1d\x63ohesity.gandalf.server_paxos\x1a\x1copen_util/net/protorpc.proto\"\x9a\x03\n\x0fPaxosErrorProto\"\x86\x03\n\x04Type\x12\x0c\n\x08kNoError\x10\x00\x12\x13\n\x0fkTransportError\x10\x01\x12\x11\n\rkUnresolvable\x10\x02\x12\x0c\n\x08kTimeout\x10\x03\x12\n\n\x06kRetry\x10\x04\x12\x14\n\x10kIncorrectNodeId\x10\x05\x12\x16\n\x12kProposerNotInView\x10\x06\x12\x1a\n\x16kInstanceAlreadyChosen\x10\x07\x12\x1d\n\x19kPreviousInstanceUnchosen\x10\x08\x12\x18\n\x14kLeasedToAnotherNode\x10\t\x12\x0e\n\nkPreempted\x10\n\x12\x14\n\x10kNoAcceptedValue\x10\x0b\x12\x1a\n\x16kAcceptedValueMismatch\x10\x0c\x12\x19\n\x15kCannotGarbageCollect\x10\r\x12\x17\n\x13kNoValueForInstance\x10\x0e\x12\x16\n\x12kClusterIdMismatch\x10\x0f\x12\x17\n\x13kEncryptionRequired\x10\x11\"\x04\x08\x10\x10\x10\"\x9b\x02\n\x0eViewDescriptor\x12\x10\n\x08node_ids\x18\x01 \x03(\x03\x12\x18\n\x10target_view_size\x18\x02 \x02(\x03\x12\x19\n\rspare_node_id\x18\x03 \x01(\x03:\x02-1\x12X\n\x0enode_endpoints\x18\x04 \x03(\x0b\x32@.cohesity.gandalf.server_paxos.ViewDescriptor.NodeEndpointsEntry\x12\x15\n\rsupports_grpc\x18\x05 \x01(\x08\x12\x1b\n\x13paxos_supports_grpc\x18\x06 \x01(\x08\x1a\x34\n\x12NodeEndpointsEntry\x12\x0b\n\x03key\x18\x01 \x01(\x03\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xb3\x04\n\x10PaxosValueHeader\x12M\n\nvalue_type\x18\x01 \x02(\x0e\x32\x39.cohesity.gandalf.server_paxos.PaxosValueHeader.ValueType\x12Z\n\x11\x63lient_value_type\x18\x02 \x01(\x0e\x32?.cohesity.gandalf.server_paxos.PaxosValueHeader.ClientValueType\x12%\n\x19start_checkpoint_instance\x18\x03 \x01(\x03:\x02-1\x12\x1d\n\x11gc_until_instance\x18\x04 \x01(\x03:\x02-1\"t\n\tValueType\x12\x10\n\x0ckUnknownType\x10\x00\x12\x11\n\rkBecomeMaster\x10\x01\x12\x11\n\rkLeaseRenewal\x10\x02\x12\t\n\x05kView\x10\x03\x12\x10\n\x0ckClientValue\x10\x04\x12\x12\n\x0ekNumValueTypes\x10\x05\"\xb7\x01\n\x0f\x43lientValueType\x12\x1b\n\x17kUnknownClientValueType\x10\x00\x12\x13\n\x0fkBulkDataRecord\x10\x01\x12\x1a\n\x16kStartCheckpointRecord\x10\x02\x12\x1d\n\x19kFinalizeCheckpointRecord\x10\x03\x12\x1d\n\x19kGarbageCollectionRequest\x10\x04\x12\x18\n\x14kNumClientValueTypes\x10\x05\"6\n\nProposalId\x12\x14\n\tlocal_num\x18\x02 \x02(\x03:\x01\x30\x12\x12\n\x07node_id\x18\x03 \x02(\x03:\x01\x30\"\xaf\x01\n\rInstanceRange\x12\x1f\n\x13min_chosen_instance\x18\x01 \x02(\x03:\x02-1\x12\x1f\n\x13max_chosen_instance\x18\x02 \x02(\x03:\x02-1\x12\x1d\n\x11unchosen_instance\x18\x03 \x01(\x03:\x02-1\x12\x1f\n\x13\x66inalize_checkpoint\x18\x04 \x01(\x03:\x02-1\x12\x1c\n\x10start_checkpoint\x18\x05 \x01(\x03:\x02-1\"\x9b\x01\n\rAcceptorState\x12\x44\n\x11promised_proposal\x18\x01 \x02(\x0b\x32).cohesity.gandalf.server_paxos.ProposalId\x12\x44\n\x0einstance_range\x18\x02 \x02(\x0b\x32,.cohesity.gandalf.server_paxos.InstanceRange\"\xfe\x01\n\nPrepareArg\x12\x16\n\x0esender_node_id\x18\x01 \x02(\x03\x12\x19\n\x11sender_cluster_id\x18\x06 \x01(\x03\x12\x18\n\x10receiver_node_id\x18\x02 \x02(\x03\x12>\n\x0bproposal_id\x18\x03 \x02(\x0b\x32).cohesity.gandalf.server_paxos.ProposalId\x12\x14\n\x0cinstance_num\x18\x04 \x02(\x03\x12M\n\x17proposer_instance_range\x18\x05 \x02(\x0b\x32,.cohesity.gandalf.server_paxos.InstanceRange\"\xa1\x01\n\rPrepareResult\x12\x44\n\x0e\x61\x63\x63\x65ptor_state\x18\x01 \x02(\x0b\x32,.cohesity.gandalf.server_paxos.AcceptorState\x12J\n\x17\x61\x63\x63\x65pted_value_proposal\x18\x04 \x01(\x0b\x32).cohesity.gandalf.server_paxos.ProposalId\"\xfd\x01\n\tAcceptArg\x12\x16\n\x0esender_node_id\x18\x01 \x02(\x03\x12\x19\n\x11sender_cluster_id\x18\x06 \x01(\x03\x12\x18\n\x10receiver_node_id\x18\x02 \x02(\x03\x12>\n\x0bproposal_id\x18\x03 \x02(\x0b\x32).cohesity.gandalf.server_paxos.ProposalId\x12M\n\x17proposer_instance_range\x18\x04 \x02(\x0b\x32,.cohesity.gandalf.server_paxos.InstanceRange\x12\x14\n\x0cinstance_num\x18\x05 \x02(\x03\"T\n\x0c\x41\x63\x63\x65ptResult\x12\x44\n\x0e\x61\x63\x63\x65ptor_state\x18\x01 \x02(\x0b\x32,.cohesity.gandalf.server_paxos.AcceptorState\"\x9e\x02\n\rMarkChosenArg\x12\x16\n\x0esender_node_id\x18\x01 \x02(\x03\x12\x19\n\x11sender_cluster_id\x18\x07 \x01(\x03\x12\x18\n\x10receiver_node_id\x18\x02 \x02(\x03\x12>\n\x0bproposal_id\x18\x03 \x02(\x0b\x32).cohesity.gandalf.server_paxos.ProposalId\x12\x14\n\x0cinstance_num\x18\x04 \x02(\x03\x12M\n\x17proposer_instance_range\x18\x05 \x02(\x0b\x32,.cohesity.gandalf.server_paxos.InstanceRange\x12\x1b\n\x13value_sha1_checksum\x18\x06 \x02(\x0c\"X\n\x10MarkChosenResult\x12\x44\n\x0e\x61\x63\x63\x65ptor_state\x18\x01 \x02(\x0b\x32,.cohesity.gandalf.server_paxos.AcceptorState\"z\n\x15PullChosenInstanceArg\x12\x16\n\x0esender_node_id\x18\x01 \x02(\x03\x12\x19\n\x11sender_cluster_id\x18\x04 \x01(\x03\x12\x18\n\x10receiver_node_id\x18\x02 \x02(\x03\x12\x14\n\x0cmin_instance\x18\x03 \x02(\x03\"D\n\x18PullChosenInstanceResult\x12\x11\n\tinstances\x18\x01 \x03(\x03\x12\x15\n\rpayload_sizes\x18\x02 \x03(\x03\"{\n\x11GarbageCollectArg\x12\x16\n\x0esender_node_id\x18\x01 \x02(\x03\x12\x19\n\x11sender_cluster_id\x18\x04 \x01(\x03\x12\x18\n\x10receiver_node_id\x18\x02 \x02(\x03\x12\x19\n\x11gc_until_instance\x18\x03 \x02(\x03\"\x16\n\x14GarbageCollectResult2\xd8\x04\n\x0fPaxosRpcService\x12\x64\n\x07Prepare\x12).cohesity.gandalf.server_paxos.PrepareArg\x1a,.cohesity.gandalf.server_paxos.PrepareResult\"\x00\x12\x61\n\x06\x41\x63\x63\x65pt\x12(.cohesity.gandalf.server_paxos.AcceptArg\x1a+.cohesity.gandalf.server_paxos.AcceptResult\"\x00\x12m\n\nMarkChosen\x12,.cohesity.gandalf.server_paxos.MarkChosenArg\x1a/.cohesity.gandalf.server_paxos.MarkChosenResult\"\x00\x12\x8a\x01\n\x12PullChosenInstance\x12\x34.cohesity.gandalf.server_paxos.PullChosenInstanceArg\x1a\x37.cohesity.gandalf.server_paxos.PullChosenInstanceResult\"\x05\x80\xe2\t\xb8\x17\x12y\n\x0eGarbageCollect\x12\x30.cohesity.gandalf.server_paxos.GarbageCollectArg\x1a\x33.cohesity.gandalf.server_paxos.GarbageCollectResult\"\x00\x1a\x05\x80\xf1\x04\x88\'B\x03\x80\x01\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'gandalf.server.paxos.base.paxos_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\200\001\001'
  _globals['_VIEWDESCRIPTOR_NODEENDPOINTSENTRY']._loaded_options = None
  _globals['_VIEWDESCRIPTOR_NODEENDPOINTSENTRY']._serialized_options = b'8\001'
  _globals['_PAXOSRPCSERVICE']._loaded_options = None
  _globals['_PAXOSRPCSERVICE']._serialized_options = b'\200\361\004\210\''
  _globals['_PAXOSRPCSERVICE'].methods_by_name['PullChosenInstance']._loaded_options = None
  _globals['_PAXOSRPCSERVICE'].methods_by_name['PullChosenInstance']._serialized_options = b'\200\342\t\270\027'
  _globals['_PAXOSERRORPROTO']._serialized_start=103
  _globals['_PAXOSERRORPROTO']._serialized_end=513
  _globals['_PAXOSERRORPROTO_TYPE']._serialized_start=123
  _globals['_PAXOSERRORPROTO_TYPE']._serialized_end=513
  _globals['_VIEWDESCRIPTOR']._serialized_start=516
  _globals['_VIEWDESCRIPTOR']._serialized_end=799
  _globals['_VIEWDESCRIPTOR_NODEENDPOINTSENTRY']._serialized_start=747
  _globals['_VIEWDESCRIPTOR_NODEENDPOINTSENTRY']._serialized_end=799
  _globals['_PAXOSVALUEHEADER']._serialized_start=802
  _globals['_PAXOSVALUEHEADER']._serialized_end=1365
  _globals['_PAXOSVALUEHEADER_VALUETYPE']._serialized_start=1063
  _globals['_PAXOSVALUEHEADER_VALUETYPE']._serialized_end=1179
  _globals['_PAXOSVALUEHEADER_CLIENTVALUETYPE']._serialized_start=1182
  _globals['_PAXOSVALUEHEADER_CLIENTVALUETYPE']._serialized_end=1365
  _globals['_PROPOSALID']._serialized_start=1367
  _globals['_PROPOSALID']._serialized_end=1421
  _globals['_INSTANCERANGE']._serialized_start=1424
  _globals['_INSTANCERANGE']._serialized_end=1599
  _globals['_ACCEPTORSTATE']._serialized_start=1602
  _globals['_ACCEPTORSTATE']._serialized_end=1757
  _globals['_PREPAREARG']._serialized_start=1760
  _globals['_PREPAREARG']._serialized_end=2014
  _globals['_PREPARERESULT']._serialized_start=2017
  _globals['_PREPARERESULT']._serialized_end=2178
  _globals['_ACCEPTARG']._serialized_start=2181
  _globals['_ACCEPTARG']._serialized_end=2434
  _globals['_ACCEPTRESULT']._serialized_start=2436
  _globals['_ACCEPTRESULT']._serialized_end=2520
  _globals['_MARKCHOSENARG']._serialized_start=2523
  _globals['_MARKCHOSENARG']._serialized_end=2809
  _globals['_MARKCHOSENRESULT']._serialized_start=2811
  _globals['_MARKCHOSENRESULT']._serialized_end=2899
  _globals['_PULLCHOSENINSTANCEARG']._serialized_start=2901
  _globals['_PULLCHOSENINSTANCEARG']._serialized_end=3023
  _globals['_PULLCHOSENINSTANCERESULT']._serialized_start=3025
  _globals['_PULLCHOSENINSTANCERESULT']._serialized_end=3093
  _globals['_GARBAGECOLLECTARG']._serialized_start=3095
  _globals['_GARBAGECOLLECTARG']._serialized_end=3218
  _globals['_GARBAGECOLLECTRESULT']._serialized_start=3220
  _globals['_GARBAGECOLLECTRESULT']._serialized_end=3242
  _globals['_PAXOSRPCSERVICE']._serialized_start=3245
  _globals['_PAXOSRPCSERVICE']._serialized_end=3845
# @@protoc_insertion_point(module_scope)