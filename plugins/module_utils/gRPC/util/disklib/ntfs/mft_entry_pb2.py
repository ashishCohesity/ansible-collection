# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: util/disklib/ntfs/mft_entry.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!util/disklib/ntfs/mft_entry.proto\x12\x15\x63ohesity.disklib.ntfs\"\xa1\x03\n\rMFTEntryProto\x12\x15\n\rmft_reference\x18\x01 \x01(\x06\x12\x15\n\x07is_file\x18\x02 \x01(\x08:\x04true\x12\x41\n\nfile_names\x18\x03 \x03(\x0b\x32-.cohesity.disklib.ntfs.MFTEntryProto.FileName\x12\x12\n\nsize_bytes\x18\x04 \x01(\x03\x12\x13\n\x0bmtime_usecs\x18\x05 \x01(\x06\x12\x17\n\x0fphysical_offset\x18\x06 \x01(\x03\x1a\x97\x01\n\x08\x46ileName\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x1c\n\x14parent_mft_reference\x18\x02 \x01(\x06\x12J\n\x0e\x66ile_namespace\x18\x03 \x01(\x0e\x32\x32.cohesity.disklib.ntfs.MFTEntryProto.NTFSNamespace\x12\x13\n\x0bparent_path\x18\x04 \x01(\t\"C\n\rNTFSNamespace\x12\n\n\x06kPosix\x10\x00\x12\n\n\x06kWin32\x10\x01\x12\x08\n\x04kDOS\x10\x02\x12\x10\n\x0ckWin32AndDOS\x10\x03')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'util.disklib.ntfs.mft_entry_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_MFTENTRYPROTO']._serialized_start=61
  _globals['_MFTENTRYPROTO']._serialized_end=478
  _globals['_MFTENTRYPROTO_FILENAME']._serialized_start=258
  _globals['_MFTENTRYPROTO_FILENAME']._serialized_end=409
  _globals['_MFTENTRYPROTO_NTFSNAMESPACE']._serialized_start=411
  _globals['_MFTENTRYPROTO_NTFSNAMESPACE']._serialized_end=478
# @@protoc_insertion_point(module_scope)
