# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: configs/rigel_transient_config.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$configs/rigel_transient_config.proto\x12\x10\x63ohesity.configs\"\x90\x01\n\x15RigelConnectionStatus\x12\x14\n\x0cis_connected\x18\x01 \x01(\x08\x12&\n\x1elast_connected_timestamp_msecs\x18\x02 \x01(\x03\x12\x19\n\x11\x65rror_message_str\x18\x03 \x01(\t\x12\x1e\n\x16\x62ifrost_consitutent_id\x18\x04 \x01(\x03\"\x94\x02\n\tRigelNode\x12\x12\n\nrigel_guid\x18\x01 \x01(\x03\x12O\n\x1e\x63ontrolplane_connection_status\x18\x02 \x01(\x0b\x32\'.cohesity.configs.RigelConnectionStatus\x12P\n\x1b\x64\x61taplane_connection_status\x18\x03 \x01(\x0b\x32\'.cohesity.configs.RigelConnectionStatusB\x02\x18\x01\x12P\n\x1f\x64\x61taplane_connection_status_vec\x18\x04 \x03(\x0b\x32\'.cohesity.configs.RigelConnectionStatus\"K\n\x14RigelTransientConfig\x12\x33\n\x0erigel_node_vec\x18\x01 \x03(\x0b\x32\x1b.cohesity.configs.RigelNodeB9\n\x14\x63om.cohesity.configsZ!configs/rigel_transient_config.pb')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'configs.rigel_transient_config_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\024com.cohesity.configsZ!configs/rigel_transient_config.pb'
  _globals['_RIGELNODE'].fields_by_name['dataplane_connection_status']._loaded_options = None
  _globals['_RIGELNODE'].fields_by_name['dataplane_connection_status']._serialized_options = b'\030\001'
  _globals['_RIGELCONNECTIONSTATUS']._serialized_start=59
  _globals['_RIGELCONNECTIONSTATUS']._serialized_end=203
  _globals['_RIGELNODE']._serialized_start=206
  _globals['_RIGELNODE']._serialized_end=482
  _globals['_RIGELTRANSIENTCONFIG']._serialized_start=484
  _globals['_RIGELTRANSIENTCONFIG']._serialized_end=559
# @@protoc_insertion_point(module_scope)
