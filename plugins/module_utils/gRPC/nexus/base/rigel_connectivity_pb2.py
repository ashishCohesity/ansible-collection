# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: nexus/base/rigel_connectivity.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#nexus/base/rigel_connectivity.proto\x12\x13\x63ohesity.nexus.base\"\xf9\x08\n\x16RigelConnectivityProto\x12\'\n\x0bgandalf_key\x18\x01 \x01(\t:\x12rigel_connectivity\x12^\n\x17node_endpoint_state_vec\x18\x02 \x03(\x0b\x32=.cohesity.nexus.base.RigelConnectivityProto.NodeEndpointState\x1a\xd5\x07\n\x11NodeEndpointState\x12\x0f\n\x07node_id\x18\x01 \x01(\x03\x12w\n\x1d\x65ndpoint_connection_state_vec\x18\x02 \x03(\x0b\x32P.cohesity.nexus.base.RigelConnectivityProto.NodeEndpointState.EndpointConnStatus\x12q\n\x13GatewayReachability\x18\x03 \x01(\x0b\x32P.cohesity.nexus.base.RigelConnectivityProto.NodeEndpointState.EndpointConnStatusB\x02\x18\x01\x12s\n\x15\x44NSServerReachability\x18\x04 \x01(\x0b\x32P.cohesity.nexus.base.RigelConnectivityProto.NodeEndpointState.EndpointConnStatusB\x02\x18\x01\x12s\n\x15NTPServerReachability\x18\x05 \x01(\x0b\x32P.cohesity.nexus.base.RigelConnectivityProto.NodeEndpointState.EndpointConnStatusB\x02\x18\x01\x12\x18\n\x10\x63heck_time_usecs\x18\x06 \x01(\x03\x1a\xe2\x02\n\x12\x45ndpointConnStatus\x12\x15\n\rendpoint_name\x18\x01 \x01(\t\x12\x15\n\rendpoint_port\x18\x02 \x01(\t\x12v\n\x10\x63heck_result_vec\x18\x03 \x03(\x0b\x32\\.cohesity.nexus.base.RigelConnectivityProto.NodeEndpointState.EndpointConnStatus.CheckResult\x1a\xa5\x01\n\x0b\x43heckResult\x12\x12\n\ncheck_name\x18\x01 \x01(\t\x12k\n\x12\x63onnectivity_state\x18\x02 \x01(\x0e\x32O.cohesity.nexus.base.RigelConnectivityProto.NodeEndpointState.ConnectivityState\x12\x15\n\rerror_message\x18\x03 \x01(\t\"Z\n\x11\x43onnectivityState\x12\x11\n\rkStateUnknown\x10\x00\x12\x0c\n\x08kStateOk\x10\x01\x12\x0e\n\nkStateFail\x10\x02\x12\x14\n\x10kStateInProgress\x10\x03\x42\"Z nexus/base/rigel_connectivity.pb')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'nexus.base.rigel_connectivity_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z nexus/base/rigel_connectivity.pb'
  _globals['_RIGELCONNECTIVITYPROTO_NODEENDPOINTSTATE'].fields_by_name['GatewayReachability']._loaded_options = None
  _globals['_RIGELCONNECTIVITYPROTO_NODEENDPOINTSTATE'].fields_by_name['GatewayReachability']._serialized_options = b'\030\001'
  _globals['_RIGELCONNECTIVITYPROTO_NODEENDPOINTSTATE'].fields_by_name['DNSServerReachability']._loaded_options = None
  _globals['_RIGELCONNECTIVITYPROTO_NODEENDPOINTSTATE'].fields_by_name['DNSServerReachability']._serialized_options = b'\030\001'
  _globals['_RIGELCONNECTIVITYPROTO_NODEENDPOINTSTATE'].fields_by_name['NTPServerReachability']._loaded_options = None
  _globals['_RIGELCONNECTIVITYPROTO_NODEENDPOINTSTATE'].fields_by_name['NTPServerReachability']._serialized_options = b'\030\001'
  _globals['_RIGELCONNECTIVITYPROTO']._serialized_start=61
  _globals['_RIGELCONNECTIVITYPROTO']._serialized_end=1206
  _globals['_RIGELCONNECTIVITYPROTO_NODEENDPOINTSTATE']._serialized_start=225
  _globals['_RIGELCONNECTIVITYPROTO_NODEENDPOINTSTATE']._serialized_end=1206
  _globals['_RIGELCONNECTIVITYPROTO_NODEENDPOINTSTATE_ENDPOINTCONNSTATUS']._serialized_start=760
  _globals['_RIGELCONNECTIVITYPROTO_NODEENDPOINTSTATE_ENDPOINTCONNSTATUS']._serialized_end=1114
  _globals['_RIGELCONNECTIVITYPROTO_NODEENDPOINTSTATE_ENDPOINTCONNSTATUS_CHECKRESULT']._serialized_start=949
  _globals['_RIGELCONNECTIVITYPROTO_NODEENDPOINTSTATE_ENDPOINTCONNSTATUS_CHECKRESULT']._serialized_end=1114
  _globals['_RIGELCONNECTIVITYPROTO_NODEENDPOINTSTATE_CONNECTIVITYSTATE']._serialized_start=1116
  _globals['_RIGELCONNECTIVITYPROTO_NODEENDPOINTSTATE_CONNECTIVITYSTATE']._serialized_end=1206
# @@protoc_insertion_point(module_scope)