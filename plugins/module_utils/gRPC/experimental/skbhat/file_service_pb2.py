# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: experimental/skbhat/file_service.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from open_util.net import protorpc_pb2 as open__util_dot_net_dot_protorpc__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&experimental/skbhat/file_service.proto\x12\x1c\x63ohesity.experimental.skbhat\x1a\x1copen_util/net/protorpc.proto\"Y\n\x0b\x46ileRequest\x12\x11\n\tfile_name\x18\x01 \x01(\t\x12\x11\n\tfile_desc\x18\x03 \x01(\x03\x12\x14\n\x0cnum_bytes_rw\x18\x04 \x01(\x05\x12\x0e\n\x06offset\x18\x05 \x01(\x05\"Z\n\x0c\x46ileResponse\x12\x11\n\tfile_name\x18\x01 \x01(\t\x12\x11\n\tfile_desc\x18\x02 \x01(\x03\x12\x14\n\x0cnum_bytes_rw\x18\x05 \x01(\x03\x12\x0e\n\x06offset\x18\x06 \x01(\x05\x32\xce\x02\n\x0b\x46ileService\x12\x65\n\nCreateFile\x12).cohesity.experimental.skbhat.FileRequest\x1a*.cohesity.experimental.skbhat.FileResponse\"\x00\x12\x63\n\x08ReadFile\x12).cohesity.experimental.skbhat.FileRequest\x1a*.cohesity.experimental.skbhat.FileResponse\"\x00\x12\x64\n\tWriteFile\x12).cohesity.experimental.skbhat.FileRequest\x1a*.cohesity.experimental.skbhat.FileResponse\"\x00\x1a\r\x80\xf1\x04\xe8\x07\x88\xf1\x04\x01\x90\xf1\x04\x02\x42\x03\x80\x01\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'experimental.skbhat.file_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\200\001\001'
  _globals['_FILESERVICE']._loaded_options = None
  _globals['_FILESERVICE']._serialized_options = b'\200\361\004\350\007\210\361\004\001\220\361\004\002'
  _globals['_FILEREQUEST']._serialized_start=102
  _globals['_FILEREQUEST']._serialized_end=191
  _globals['_FILERESPONSE']._serialized_start=193
  _globals['_FILERESPONSE']._serialized_end=283
  _globals['_FILESERVICE']._serialized_start=286
  _globals['_FILESERVICE']._serialized_end=620
# @@protoc_insertion_point(module_scope)
