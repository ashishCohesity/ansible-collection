# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bridge/blob_store/tools/full_cfm.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from bridge.blob_store import blob_store_pb2 as bridge_dot_blob__store_dot_blob__store__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&bridge/blob_store/tools/full_cfm.proto\x12\x14\x63ohesity.bridge.blob\x1a\"bridge/blob_store/blob_store.proto\"\x90\x04\n\x07\x46ullCFM\x12P\n\rmaster_column\x18\x01 \x01(\x0b\x32\x39.cohesity.bridge.blob.ChunkFileMetadataProto.MasterColumn\x12:\n\tchunk_vec\x18\x02 \x03(\x0b\x32\'.cohesity.bridge.blob.FullCFM.ChunkInfo\x12\x45\n\x0f\x63hunk_group_vec\x18\x03 \x03(\x0b\x32,.cohesity.bridge.blob.FullCFM.ChunkGroupInfo\x12\x16\n\x0escribe_version\x18\x04 \x01(\x03\x1a\x91\x01\n\tChunkInfo\x12\x34\n\x08\x63hunk_id\x18\x01 \x01(\x0b\x32\".cohesity.bridge.blob.ChunkIdProto\x12N\n\x0c\x63hunk_column\x18\x02 \x01(\x0b\x32\x38.cohesity.bridge.blob.ChunkFileMetadataProto.ChunkColumn\x1a\x83\x01\n\x0e\x43hunkGroupInfo\x12\x16\n\x0e\x63hunk_group_id\x18\x01 \x01(\x05\x12Y\n\x12\x63hunk_group_column\x18\x02 \x01(\x0b\x32=.cohesity.bridge.blob.ChunkFileMetadataProto.ChunkGroupColumn')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'bridge.blob_store.tools.full_cfm_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_FULLCFM']._serialized_start=101
  _globals['_FULLCFM']._serialized_end=629
  _globals['_FULLCFM_CHUNKINFO']._serialized_start=350
  _globals['_FULLCFM_CHUNKINFO']._serialized_end=495
  _globals['_FULLCFM_CHUNKGROUPINFO']._serialized_start=498
  _globals['_FULLCFM_CHUNKGROUPINFO']._serialized_end=629
# @@protoc_insertion_point(module_scope)
