# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bridge/snap_fs/dedup_range.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from bridge.base import cloud_pb2 as bridge_dot_base_dot_cloud__pb2
from bridge.blob_store import blob_store_pb2 as bridge_dot_blob__store_dot_blob__store__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n bridge/snap_fs/dedup_range.proto\x12\x17\x63ohesity.bridge.snap_fs\x1a\x17\x62ridge/base/cloud.proto\x1a\"bridge/blob_store/blob_store.proto\"\xe5\x02\n\tRangeInfo\x12\x0e\n\x06offset\x18\x01 \x02(\x03\x12\x18\n\tchunk_len\x18\x02 \x01(\x03:\x05\x31\x36\x33\x38\x34\x12\x0c\n\x04sha1\x18\x03 \x01(\x0c\x12\x0f\n\x07is_zero\x18\x04 \x01(\x08\x12\x10\n\x08has_data\x18\x05 \x01(\x08\x12\x14\n\x0c\x63hunk_offset\x18\x06 \x01(\x05\x12\x11\n\trange_len\x18\x07 \x01(\x05\x12\x1c\n\x0eis_dedup_chunk\x18\x08 \x01(\x08:\x04true\x12O\n\x18\x63loud_chunk_location_vec\x18\x0b \x03(\x0b\x32-.cohesity.bridge.blob.CloudChunkLocationProto\x12 \n\x18skip_cloud_chunk_mapping\x18\n \x01(\x08\x12\x18\n\x10\x62rick_level_sha1\x18\x0c \x01(\x0c\x12)\n!skip_unnecessary_metadata_lookups\x18\r \x01(\x08\"\xe8\x01\n\x12\x43loudChunkFileInfo\x12<\n\x0f\x63loud_object_id\x18\x01 \x01(\x0b\x32#.cohesity.bridge.CloudObjectIdProto\x12\x13\n\x07version\x18\x02 \x01(\x03:\x02-1\x12\x13\n\x0b\x63hunk_count\x18\x03 \x01(\x03\x12\x19\n\x11morphed_data_size\x18\x04 \x01(\x03\x12\x1f\n\x17\x62ypass_write_permission\x18\x05 \x01(\x08\x12.\n\tlease_vec\x18\x06 \x03(\x0b\x32\x1b.cohesity.bridge.LeaseProto\"\x93\x01\n\nDedupRange\x12\x35\n\trange_vec\x18\x01 \x03(\x0b\x32\".cohesity.bridge.snap_fs.RangeInfo\x12N\n\x19\x63loud_chunk_file_info_vec\x18\x02 \x03(\x0b\x32+.cohesity.bridge.snap_fs.CloudChunkFileInfoB.\n\x1b\x63om.cohesity.bridge.snap_fsB\x0f\x44\x65\x64upRangeProto')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'bridge.snap_fs.dedup_range_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033com.cohesity.bridge.snap_fsB\017DedupRangeProto'
  _globals['_RANGEINFO']._serialized_start=123
  _globals['_RANGEINFO']._serialized_end=480
  _globals['_CLOUDCHUNKFILEINFO']._serialized_start=483
  _globals['_CLOUDCHUNKFILEINFO']._serialized_end=715
  _globals['_DEDUPRANGE']._serialized_start=718
  _globals['_DEDUPRANGE']._serialized_end=865
# @@protoc_insertion_point(module_scope)
