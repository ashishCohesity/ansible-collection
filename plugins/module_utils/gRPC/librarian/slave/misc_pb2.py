# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: librarian/slave/misc.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1alibrarian/slave/misc.proto\x12\x18\x63ohesity.librarian.slave\"P\n\x0bPruneKeyArg\x12\x13\n\x0bnum_buckets\x18\x01 \x01(\x03\x12\x19\n\x11sharding_function\x18\x02 \x01(\t\x12\x11\n\tbucket_id\x18\x03 \x01(\x03\"\x92\x02\n\x0fPruneKeysCookie\x12\x11\n\tbucket_id\x18\x01 \x01(\x03\x12\x0e\n\x06\x63ookie\x18\x02 \x01(\x0c\x12@\n\x06status\x18\x03 \x01(\x0e\x32\x30.cohesity.librarian.slave.PruneKeysCookie.Status\x12\x18\n\x10time_taken_usecs\x18\x04 \x01(\x03\x12\x18\n\x10num_docs_scanned\x18\x05 \x01(\x03\x12\x18\n\x10num_docs_deleted\x18\x06 \x01(\x03\x12\x18\n\x10start_time_usecs\x18\x07 \x01(\x03\"2\n\x06Status\x12\x0f\n\x0bkNotStarted\x10\x00\x12\x0c\n\x08kStarted\x10\x01\x12\t\n\x05kDone\x10\x02\"\x99\x03\n\x11ShuffleKeysCookie\x12\x11\n\tbucket_id\x18\x01 \x01(\x03\x12\x42\n\x06status\x18\x02 \x01(\x0e\x32\x32.cohesity.librarian.slave.ShuffleKeysCookie.Status\x12\x17\n\x0fstart_time_secs\x18\x03 \x01(\x03\x12\x17\n\x0ftime_taken_secs\x18\x04 \x01(\x03\x12V\n\x11keys_copied_stats\x18\x05 \x03(\x0b\x32;.cohesity.librarian.slave.ShuffleKeysCookie.KeysCopiedStats\x12\x0b\n\x03key\x18\x06 \x01(\t\x12\x18\n\x10num_docs_scanned\x18\x07 \x01(\x03\x1aH\n\x0fKeysCopiedStats\x12\x11\n\tbucket_id\x18\x01 \x01(\x03\x12\x0f\n\x07\x64isk_id\x18\x02 \x01(\x03\x12\x11\n\tdoc_count\x18\x03 \x01(\x03\"2\n\x06Status\x12\x0f\n\x0bkNotStarted\x10\x00\x12\x0c\n\x08kStarted\x10\x01\x12\t\n\x05kDone\x10\x02')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'librarian.slave.misc_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_PRUNEKEYARG']._serialized_start=56
  _globals['_PRUNEKEYARG']._serialized_end=136
  _globals['_PRUNEKEYSCOOKIE']._serialized_start=139
  _globals['_PRUNEKEYSCOOKIE']._serialized_end=413
  _globals['_PRUNEKEYSCOOKIE_STATUS']._serialized_start=363
  _globals['_PRUNEKEYSCOOKIE_STATUS']._serialized_end=413
  _globals['_SHUFFLEKEYSCOOKIE']._serialized_start=416
  _globals['_SHUFFLEKEYSCOOKIE']._serialized_end=825
  _globals['_SHUFFLEKEYSCOOKIE_KEYSCOPIEDSTATS']._serialized_start=701
  _globals['_SHUFFLEKEYSCOOKIE_KEYSCOPIEDSTATS']._serialized_end=773
  _globals['_SHUFFLEKEYSCOOKIE_STATUS']._serialized_start=363
  _globals['_SHUFFLEKEYSCOOKIE_STATUS']._serialized_end=413
# @@protoc_insertion_point(module_scope)
