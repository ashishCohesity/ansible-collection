# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: util/qos/test/disk_selector_hetrogenous_cluster_test.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n:util/qos/test/disk_selector_hetrogenous_cluster_test.proto\x12\x0c\x63ohesity.qos\"\xfd\x03\n#DiskSelectorHetrogenousClusterProto\x12h\n\x0btest_config\x18\x01 \x02(\x0b\x32S.cohesity.qos.DiskSelectorHetrogenousClusterProto.DiskSelectorHetrogenousTestConfig\x12^\n\x07\x63luster\x18\x02 \x03(\x0b\x32M.cohesity.qos.DiskSelectorHetrogenousClusterProto.DiskSelectorHetrogenousNode\x1a\xc7\x01\n!DiskSelectorHetrogenousTestConfig\x12\x16\n\x0etest_iteration\x18\x01 \x01(\x05\x12\x1b\n\x13iteration_to_report\x18\x02 \x01(\x05\x12\x18\n\x10\x64\x61ta_size_per_io\x18\x03 \x01(\t\x12\x1a\n\x12num_disk_to_return\x18\x04 \x01(\x05\x12\x1b\n\x13max_replica_failure\x18\x05 \x01(\x05\x12\x1a\n\x12max_entity_failure\x18\x06 \x01(\x05\x1a\x42\n\x1b\x44iskSelectorHetrogenousNode\x12\x10\n\x08num_disk\x18\x01 \x01(\x03\x12\x11\n\tdisk_size\x18\x02 \x01(\t')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'util.qos.test.disk_selector_hetrogenous_cluster_test_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_DISKSELECTORHETROGENOUSCLUSTERPROTO']._serialized_start=77
  _globals['_DISKSELECTORHETROGENOUSCLUSTERPROTO']._serialized_end=586
  _globals['_DISKSELECTORHETROGENOUSCLUSTERPROTO_DISKSELECTORHETROGENOUSTESTCONFIG']._serialized_start=319
  _globals['_DISKSELECTORHETROGENOUSCLUSTERPROTO_DISKSELECTORHETROGENOUSTESTCONFIG']._serialized_end=518
  _globals['_DISKSELECTORHETROGENOUSCLUSTERPROTO_DISKSELECTORHETROGENOUSNODE']._serialized_start=520
  _globals['_DISKSELECTORHETROGENOUSCLUSTERPROTO_DISKSELECTORHETROGENOUSNODE']._serialized_end=586
# @@protoc_insertion_point(module_scope)
