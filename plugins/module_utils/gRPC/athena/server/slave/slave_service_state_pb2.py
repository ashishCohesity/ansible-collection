# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: athena/server/slave/slave_service_state.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-athena/server/slave/slave_service_state.proto\x12\x0f\x63ohesity.athena\"\xe7\x03\n\x16SlaveServiceStateProto\x12H\n\x0bservice_vec\x18\x01 \x03(\x0b\x32\x33.cohesity.athena.SlaveServiceStateProto.ServiceInfo\x1a\x8e\x01\n\x0bServiceInfo\x12\x41\n\x04name\x18\x01 \x01(\x0e\x32\x33.cohesity.athena.SlaveServiceStateProto.ServiceName\x12\x0f\n\x07\x61rg_vec\x18\x02 \x03(\t\x12\x13\n\x0b\x66ingerprint\x18\x03 \x01(\t\x12\x16\n\x0eincarnation_id\x18\x04 \x01(\x03\"\xf1\x01\n\x0bServiceName\x12\x0b\n\x07unknown\x10\x00\x12\n\n\x06\x64ocker\x10\x01\x12\r\n\tkubeSlave\x10\x02\x12\x0b\n\x07kubelet\x10\x03\x12\x0f\n\x0b\x61thenaProxy\x10\x04\x12\x06\n\x02vm\x10\x05\x12\r\n\tkubeProxy\x10\x06\x12\x0c\n\x08\x66lanneld\x10\x07\x12\x12\n\x0e\x61thenaWatchdog\x10\x08\x12\r\n\tyodaAgent\x10\t\x12\r\n\tflanneld2\x10\n\x12\n\n\x06multus\x10\x0b\x12\x19\n\x15\x64ocker_registry_local\x10\x0c\x12\x0e\n\ncontainerd\x10\r\x12\x0e\n\nathenaCert\x10\x0e\x42,Z*athena/server/slave/slave_service_state.pb')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'athena.server.slave.slave_service_state_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z*athena/server/slave/slave_service_state.pb'
  _globals['_SLAVESERVICESTATEPROTO']._serialized_start=67
  _globals['_SLAVESERVICESTATEPROTO']._serialized_end=554
  _globals['_SLAVESERVICESTATEPROTO_SERVICEINFO']._serialized_start=168
  _globals['_SLAVESERVICESTATEPROTO_SERVICEINFO']._serialized_end=310
  _globals['_SLAVESERVICESTATEPROTO_SERVICENAME']._serialized_start=313
  _globals['_SLAVESERVICESTATEPROTO_SERVICENAME']._serialized_end=554
# @@protoc_insertion_point(module_scope)
