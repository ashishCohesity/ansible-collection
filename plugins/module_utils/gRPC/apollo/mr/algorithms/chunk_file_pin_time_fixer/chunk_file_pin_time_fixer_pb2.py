# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: apollo/mr/algorithms/chunk_file_pin_time_fixer/chunk_file_pin_time_fixer.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from bridge.blob_store import blob_store_pb2 as bridge_dot_blob__store_dot_blob__store__pb2
from bridge.view_keeper import view_metadata_pb2 as bridge_dot_view__keeper_dot_view__metadata__pb2
from configs import cluster_config_pb2 as configs_dot_cluster__config__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nNapollo/mr/algorithms/chunk_file_pin_time_fixer/chunk_file_pin_time_fixer.proto\x12\x1d\x63ohesity.apollo.mr.algorithms\x1a\"bridge/blob_store/blob_store.proto\x1a&bridge/view_keeper/view_metadata.proto\x1a\x1c\x63onfigs/cluster_config.proto\"\xf3\x02\n%ChunkFilePinTimeFixerContextDataProto\x12\x42\n\x14\x63luster_config_proto\x18\x01 \x01(\x0b\x32$.cohesity.configs.ClusterConfigProto\x12m\n\x0fpinned_view_vec\x18\x02 \x03(\x0b\x32T.cohesity.apollo.mr.algorithms.ChunkFilePinTimeFixerContextDataProto.PinnedViewEntry\x12%\n\x1dview_metadata_scan_successful\x18\x04 \x01(\x08\x1aj\n\x0fPinnedViewEntry\x12\x0f\n\x07view_id\x18\x01 \x01(\x03\x12\x46\n\npin_config\x18\x02 \x01(\x0b\x32\x32.cohesity.bridge.view.ViewIdMappingProto.PinConfigJ\x04\x08\x03\x10\x04\"\x90\x02\n\x18\x43hunkFileIdMapValueProto\x12\x19\n\x11max_pin_time_secs\x18\x01 \x01(\x03\x12\x63\n$pinned_chunk_file_access_state_proto\x18\x02 \x01(\x0b\x32\x35.cohesity.bridge.blob.PinnedChunkFileAccessStateProto\x12\x1a\n\x12scribe_row_version\x18\x04 \x01(\x03\x12\x13\n\x0breplica_vec\x18\x05 \x03(\x03\x12\x18\n\x10is_rf_chunk_file\x18\x06 \x01(\x08\x12#\n\x1bshould_update_pin_time_secs\x18\x07 \x01(\x08J\x04\x08\x03\x10\x04\"\xc5\x01\n\x10\x44iskIdValueProto\x12\x15\n\rchunk_file_id\x18\x01 \x01(\x03\x12\x19\n\x11max_pin_time_secs\x18\x02 \x01(\x03\x12\x63\n$pinned_chunk_file_access_state_proto\x18\x03 \x01(\x0b\x32\x35.cohesity.bridge.blob.PinnedChunkFileAccessStateProto\x12\x1a\n\x12scribe_row_version\x18\x04 \x01(\x03')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'apollo.mr.algorithms.chunk_file_pin_time_fixer.chunk_file_pin_time_fixer_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_CHUNKFILEPINTIMEFIXERCONTEXTDATAPROTO']._serialized_start=220
  _globals['_CHUNKFILEPINTIMEFIXERCONTEXTDATAPROTO']._serialized_end=591
  _globals['_CHUNKFILEPINTIMEFIXERCONTEXTDATAPROTO_PINNEDVIEWENTRY']._serialized_start=479
  _globals['_CHUNKFILEPINTIMEFIXERCONTEXTDATAPROTO_PINNEDVIEWENTRY']._serialized_end=585
  _globals['_CHUNKFILEIDMAPVALUEPROTO']._serialized_start=594
  _globals['_CHUNKFILEIDMAPVALUEPROTO']._serialized_end=866
  _globals['_DISKIDVALUEPROTO']._serialized_start=869
  _globals['_DISKIDVALUEPROTO']._serialized_end=1066
# @@protoc_insertion_point(module_scope)
