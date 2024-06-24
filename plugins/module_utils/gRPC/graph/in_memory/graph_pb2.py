# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: graph/in_memory/graph.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from util.base import universal_id_pb2 as util_dot_base_dot_universal__id__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1bgraph/in_memory/graph.proto\x12\x18\x63ohesity.graph.in_memory\x1a\x1cutil/base/universal_id.proto\"S\n\x0e\x41ttributeProto\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x11\n\x07str_val\x18\x02 \x01(\x0cH\x00\x12\x11\n\x07int_val\x18\x03 \x01(\x03H\x00\x42\r\n\x0bvalue_oneof\"\xe7\x01\n\tEdgeProto\x12\'\n\x03uid\x18\x01 \x01(\x0b\x32\x1a.cohesity.UniversalIdProto\x12\x31\n\rfrom_node_uid\x18\x02 \x01(\x0b\x32\x1a.cohesity.UniversalIdProto\x12/\n\x0bto_node_uid\x18\x03 \x01(\x0b\x32\x1a.cohesity.UniversalIdProto\x12\x0c\n\x04type\x18\x04 \x01(\t\x12?\n\rattribute_vec\x18\x05 \x03(\x0b\x32(.cohesity.graph.in_memory.AttributeProto\"\x9d\x01\n\tNodeProto\x12\'\n\x03uid\x18\x01 \x01(\x0b\x32\x1a.cohesity.UniversalIdProto\x12?\n\rattribute_vec\x18\x03 \x03(\x0b\x32(.cohesity.graph.in_memory.AttributeProto\x12\x11\n\tlabel_vec\x18\x04 \x03(\t\x12\x13\n\x0bopaque_data\x18\x02 \x01(\x0c\"J\n\nIndexProto\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05label\x18\x02 \x01(\t\x12\x1f\n\x17node_attribute_name_vec\x18\x03 \x03(\t\"\xe8\x01\n\x14GraphCheckpointProto\x12\x12\n\ngraph_name\x18\x01 \x01(\t\x12\x35\n\x08node_vec\x18\x02 \x03(\x0b\x32#.cohesity.graph.in_memory.NodeProto\x12\x35\n\x08\x65\x64ge_vec\x18\x03 \x03(\x0b\x32#.cohesity.graph.in_memory.EdgeProto\x12\x15\n\rnext_local_id\x18\x04 \x01(\x03\x12\x37\n\tindex_vec\x18\x05 \x03(\x0b\x32$.cohesity.graph.in_memory.IndexProto\"\xff\x01\n\x17\x42\x61tchUpdaterActionProto\x12<\n\x0f\x61\x64\x64_update_node\x18\x06 \x01(\x0b\x32#.cohesity.graph.in_memory.NodeProto\x12\x33\n\x0f\x64\x65lete_node_uid\x18\x07 \x01(\x0b\x32\x1a.cohesity.UniversalIdProto\x12<\n\x0f\x61\x64\x64_update_edge\x18\x08 \x01(\x0b\x32#.cohesity.graph.in_memory.EdgeProto\x12\x33\n\x0f\x64\x65lete_edge_uid\x18\t \x01(\x0b\x32\x1a.cohesity.UniversalIdProto\"\x8a\x05\n\x0eWALRecordProto\x12\x0f\n\x07version\x18\x01 \x01(\x03\x12\x44\n\x0cgraph_db_vec\x18\x02 \x03(\x0b\x32..cohesity.graph.in_memory.GraphCheckpointProto\x12\x12\n\ngraph_name\x18\x03 \x01(\t\x12J\n\x0c\x63reate_graph\x18\x04 \x01(\x0b\x32\x34.cohesity.graph.in_memory.WALRecordProto.CreateGraph\x12\x14\n\x0c\x64\x65lete_graph\x18\x05 \x01(\x08\x12<\n\x0f\x61\x64\x64_update_node\x18\x06 \x01(\x0b\x32#.cohesity.graph.in_memory.NodeProto\x12\x33\n\x0f\x64\x65lete_node_uid\x18\x07 \x01(\x0b\x32\x1a.cohesity.UniversalIdProto\x12<\n\x0f\x61\x64\x64_update_edge\x18\x08 \x01(\x0b\x32#.cohesity.graph.in_memory.EdgeProto\x12\x33\n\x0f\x64\x65lete_edge_uid\x18\t \x01(\x0b\x32\x1a.cohesity.UniversalIdProto\x12\x19\n\x11num_uids_reserved\x18\n \x01(\x05\x12:\n\x0c\x63reate_index\x18\x0b \x01(\x0b\x32$.cohesity.graph.in_memory.IndexProto\x12\x12\n\ndrop_index\x18\x0c \x01(\t\x12K\n\x10\x62\x61tch_update_vec\x18\r \x03(\x0b\x32\x31.cohesity.graph.in_memory.BatchUpdaterActionProto\x1a\r\n\x0b\x43reateGraph')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'graph.in_memory.graph_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_ATTRIBUTEPROTO']._serialized_start=87
  _globals['_ATTRIBUTEPROTO']._serialized_end=170
  _globals['_EDGEPROTO']._serialized_start=173
  _globals['_EDGEPROTO']._serialized_end=404
  _globals['_NODEPROTO']._serialized_start=407
  _globals['_NODEPROTO']._serialized_end=564
  _globals['_INDEXPROTO']._serialized_start=566
  _globals['_INDEXPROTO']._serialized_end=640
  _globals['_GRAPHCHECKPOINTPROTO']._serialized_start=643
  _globals['_GRAPHCHECKPOINTPROTO']._serialized_end=875
  _globals['_BATCHUPDATERACTIONPROTO']._serialized_start=878
  _globals['_BATCHUPDATERACTIONPROTO']._serialized_end=1133
  _globals['_WALRECORDPROTO']._serialized_start=1136
  _globals['_WALRECORDPROTO']._serialized_end=1786
  _globals['_WALRECORDPROTO_CREATEGRAPH']._serialized_start=1773
  _globals['_WALRECORDPROTO_CREATEGRAPH']._serialized_end=1786
# @@protoc_insertion_point(module_scope)
