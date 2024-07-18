# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bridge/chunk_repository/chunk_file_state.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from bridge.chunk_repository import disk_logger_pb2 as bridge_dot_chunk__repository_dot_disk__logger__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.bridge/chunk_repository/chunk_file_state.proto\x12\x1a\x63ohesity.bridge.chunk_repo\x1a)bridge/chunk_repository/disk_logger.proto\"\x8a\x06\n\x13\x43hunkFileStateProto\x12\x13\n\x07version\x18\x01 \x01(\x03:\x02-1\x12&\n\x1ahighest_intent_id_detected\x18\x02 \x01(\x03:\x02-1\x12\x1c\n\x10physical_version\x18\x03 \x01(\x03:\x02-1\x12\x1c\n\x14max_chunk_file_bytes\x18\x04 \x01(\x05\x12\x1d\n\x15used_chunk_file_bytes\x18\x05 \x01(\x05\x12\x15\n\rstripe_column\x18\x06 \x01(\x05\x12$\n\x1cnext_available_chunkgroup_id\x18\x07 \x01(\x05\x12\x12\n\nis_corrupt\x18\x08 \x01(\x08\x12Y\n\x11update_intent_vec\x18\t \x03(\x0b\x32>.cohesity.bridge.chunk_repo.DiskLoggerRecordProto.UpdateIntent\x12$\n\x18last_finalized_intent_id\x18\n \x01(\x03:\x02-1\x12\"\n\x16last_aborted_intent_id\x18\x0b \x01(\x03:\x02-1\x12\"\n\x1alast_read_access_time_secs\x18\x0c \x01(\x03\x12#\n\x1blast_write_access_time_secs\x18\r \x01(\x03\x12v\n\x11\x63hunk_stripe_type\x18\x0e \x01(\x0e\x32Q.cohesity.bridge.chunk_repo.DiskLoggerRecordProto.ChunkFileChange.ChunkStripeType:\x08kUnknown\x12\x19\n\x11max_pin_secs_hint\x18\x0f \x01(\x03\x12\x13\n\x0bview_box_id\x18\x10 \x01(\x03\x12t\n\x15\x63orruption_error_info\x18\x11 \x01(\x0b\x32U.cohesity.bridge.chunk_repo.DiskLoggerRecordProto.ChunkFileChange.CorruptionErrorInfo')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'bridge.chunk_repository.chunk_file_state_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_CHUNKFILESTATEPROTO']._serialized_start=122
  _globals['_CHUNKFILESTATEPROTO']._serialized_end=900
# @@protoc_insertion_point(module_scope)