# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: magneto/directory_walker/stats_store_interface.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from magneto.directory_walker import directory_walker_pb2 as magneto_dot_directory__walker_dot_directory__walker__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4magneto/directory_walker/stats_store_interface.proto\x12\x1b\x63ohesity.storage.dir_walker\x1a/magneto/directory_walker/directory_walker.proto\"L\n\x0e\x46ileTypeBucket\x12\x15\n\rfile_type_tag\x18\x01 \x01(\t\x12#\n\x1b\x66ile_type_bucket_extensions\x18\x02 \x03(\t\"W\n\x0e\x46ileSizeBucket\x12\x15\n\rfile_size_tag\x18\x01 \x01(\t\x12\x17\n\x0f\x66ile_size_start\x18\x02 \x01(\x04\x12\x15\n\rfile_size_end\x18\x03 \x01(\x04\"_\n\x10\x41\x63\x63\x65ssTimeBucket\x12\x17\n\x0f\x61\x63\x63\x65ss_time_tag\x18\x01 \x01(\t\x12\x19\n\x11\x61\x63\x63\x65ss_time_start\x18\x02 \x01(\x04\x12\x17\n\x0f\x61\x63\x63\x65ss_time_end\x18\x03 \x01(\x04\"S\n\rModTimeBucket\x12\x14\n\x0cmod_time_tag\x18\x01 \x01(\t\x12\x16\n\x0emod_time_start\x18\x02 \x01(\x04\x12\x14\n\x0cmod_time_end\x18\x03 \x01(\x04\"\xa5\x01\n\rProtoCubeCell\x12\x15\n\rfile_type_tag\x18\x01 \x01(\t\x12\x15\n\rfile_size_tag\x18\x02 \x01(\t\x12\x17\n\x0f\x61\x63\x63\x65ss_time_tag\x18\x03 \x01(\t\x12\x14\n\x0cmod_time_tag\x18\x07 \x01(\t\x12\x12\n\nfile_count\x18\x04 \x01(\x04\x12\x12\n\ntotal_size\x18\x05 \x01(\x04\x12\x0f\n\x07\x63\x65ll_id\x18\x06 \x01(\x04\"\xcd\x02\n\x13ProtoCubeAttributes\x12\x14\n\x0c\x64imension_nr\x18\x01 \x01(\x03\x12\x46\n\x11\x66ile_type_buckets\x18\x05 \x03(\x0b\x32+.cohesity.storage.dir_walker.FileTypeBucket\x12\x46\n\x11\x66ile_size_buckets\x18\x06 \x03(\x0b\x32+.cohesity.storage.dir_walker.FileSizeBucket\x12J\n\x13\x61\x63\x63\x65ss_time_buckets\x18\x07 \x03(\x0b\x32-.cohesity.storage.dir_walker.AccessTimeBucket\x12\x44\n\x10mod_time_buckets\x18\x08 \x03(\x0b\x32*.cohesity.storage.dir_walker.ModTimeBucket\"\xa4\x01\n\x12\x45ntitySamplingRule\x12K\n\x0b\x65ntity_type\x18\x01 \x01(\x0e\x32\x36.cohesity.storage.dir_walker.EntityMetadata.EntityType\x12\x41\n\x06metric\x18\x02 \x03(\x0e\x32\x31.cohesity.storage.dir_walker.ProtoCube.MetricType\"Z\n\x10\x45ntityStatPolicy\x12\x46\n\rpolicy_record\x18\x01 \x03(\x0b\x32/.cohesity.storage.dir_walker.EntitySamplingRule\"\xbd\x02\n\tProtoCube\x12\x43\n\tcube_attr\x18\x01 \x01(\x0b\x32\x30.cohesity.storage.dir_walker.ProtoCubeAttributes\x12\x18\n\x0c\x63\x65llIndexMap\x18\x02 \x03(\x03\x42\x02\x10\x01\x12\x16\n\x0e\x61\x63tive_cell_nr\x18\x03 \x01(\x03\x12=\n\tdata_cell\x18\x04 \x03(\x0b\x32*.cohesity.storage.dir_walker.ProtoCubeCell\x12=\n\x06policy\x18\x05 \x01(\x0b\x32-.cohesity.storage.dir_walker.EntityStatPolicy\";\n\nMetricType\x12\x0e\n\nkFileCount\x10\x01\x12\r\n\tkDirCount\x10\x02\x12\x0e\n\nkTotalSize\x10\x03\x42\x1fZ\x1dutil/storage/directory_walker')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'magneto.directory_walker.stats_store_interface_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\035util/storage/directory_walker'
  _globals['_PROTOCUBE'].fields_by_name['cellIndexMap']._loaded_options = None
  _globals['_PROTOCUBE'].fields_by_name['cellIndexMap']._serialized_options = b'\020\001'
  _globals['_FILETYPEBUCKET']._serialized_start=134
  _globals['_FILETYPEBUCKET']._serialized_end=210
  _globals['_FILESIZEBUCKET']._serialized_start=212
  _globals['_FILESIZEBUCKET']._serialized_end=299
  _globals['_ACCESSTIMEBUCKET']._serialized_start=301
  _globals['_ACCESSTIMEBUCKET']._serialized_end=396
  _globals['_MODTIMEBUCKET']._serialized_start=398
  _globals['_MODTIMEBUCKET']._serialized_end=481
  _globals['_PROTOCUBECELL']._serialized_start=484
  _globals['_PROTOCUBECELL']._serialized_end=649
  _globals['_PROTOCUBEATTRIBUTES']._serialized_start=652
  _globals['_PROTOCUBEATTRIBUTES']._serialized_end=985
  _globals['_ENTITYSAMPLINGRULE']._serialized_start=988
  _globals['_ENTITYSAMPLINGRULE']._serialized_end=1152
  _globals['_ENTITYSTATPOLICY']._serialized_start=1154
  _globals['_ENTITYSTATPOLICY']._serialized_end=1244
  _globals['_PROTOCUBE']._serialized_start=1247
  _globals['_PROTOCUBE']._serialized_end=1564
  _globals['_PROTOCUBE_METRICTYPE']._serialized_start=1505
  _globals['_PROTOCUBE_METRICTYPE']._serialized_end=1564
# @@protoc_insertion_point(module_scope)
