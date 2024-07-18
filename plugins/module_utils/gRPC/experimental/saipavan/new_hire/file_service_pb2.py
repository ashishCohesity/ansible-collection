# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: experimental/saipavan/new_hire/file_service.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from open_util.net import protorpc_pb2 as open__util_dot_net_dot_protorpc__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1experimental/saipavan/new_hire/file_service.proto\x12\'cohesity.experimental.saipavan.new_hire\x1a\x1copen_util/net/protorpc.proto\"&\n\x11\x43reateFileRequest\x12\x11\n\tfile_path\x18\x01 \x02(\t\"p\n\x12\x43reateFileResponse\x12G\n\x06status\x18\x01 \x02(\x0e\x32\x37.cohesity.experimental.saipavan.new_hire.ResponseStatus\x12\x11\n\terror_msg\x18\x02 \x01(\t\"5\n\x10WriteFileRequest\x12\x11\n\tfile_path\x18\x01 \x02(\t\x12\x0e\n\x06offset\x18\x02 \x02(\x05\"\x87\x01\n\x11WriteFileResponse\x12G\n\x06status\x18\x01 \x02(\x0e\x32\x37.cohesity.experimental.saipavan.new_hire.ResponseStatus\x12\x11\n\terror_msg\x18\x02 \x01(\t\x12\x16\n\x0ewrite_sequence\x18\x03 \x01(\x05\"D\n\x0fReadFileRequest\x12\x11\n\tfile_path\x18\x01 \x02(\t\x12\x0e\n\x06offset\x18\x02 \x02(\x05\x12\x0e\n\x06length\x18\x03 \x02(\x05\"n\n\x10ReadFileResponse\x12G\n\x06status\x18\x01 \x02(\x0e\x32\x37.cohesity.experimental.saipavan.new_hire.ResponseStatus\x12\x11\n\terror_msg\x18\x02 \x01(\t**\n\x0eResponseStatus\x12\x0b\n\x07SUCCESS\x10\x00\x12\x0b\n\x07\x46\x41ILURE\x10\x01\x32\xb1\x03\n\x0b\x46ileService\x12\x87\x01\n\nCreateFile\x12:.cohesity.experimental.saipavan.new_hire.CreateFileRequest\x1a;.cohesity.experimental.saipavan.new_hire.CreateFileResponse\"\x00\x12\x84\x01\n\tWriteFile\x12\x39.cohesity.experimental.saipavan.new_hire.WriteFileRequest\x1a:.cohesity.experimental.saipavan.new_hire.WriteFileResponse\"\x00\x12\x81\x01\n\x08ReadFile\x12\x38.cohesity.experimental.saipavan.new_hire.ReadFileRequest\x1a\x39.cohesity.experimental.saipavan.new_hire.ReadFileResponse\"\x00\x1a\r\x80\xf1\x04\xe8\x07\x88\xf1\x04\x01\x90\xf1\x04\x02\x42\x03\x80\x01\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'experimental.saipavan.new_hire.file_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\200\001\001'
  _globals['_FILESERVICE']._loaded_options = None
  _globals['_FILESERVICE']._serialized_options = b'\200\361\004\350\007\210\361\004\001\220\361\004\002'
  _globals['_RESPONSESTATUS']._serialized_start=653
  _globals['_RESPONSESTATUS']._serialized_end=695
  _globals['_CREATEFILEREQUEST']._serialized_start=124
  _globals['_CREATEFILEREQUEST']._serialized_end=162
  _globals['_CREATEFILERESPONSE']._serialized_start=164
  _globals['_CREATEFILERESPONSE']._serialized_end=276
  _globals['_WRITEFILEREQUEST']._serialized_start=278
  _globals['_WRITEFILEREQUEST']._serialized_end=331
  _globals['_WRITEFILERESPONSE']._serialized_start=334
  _globals['_WRITEFILERESPONSE']._serialized_end=469
  _globals['_READFILEREQUEST']._serialized_start=471
  _globals['_READFILEREQUEST']._serialized_end=539
  _globals['_READFILERESPONSE']._serialized_start=541
  _globals['_READFILERESPONSE']._serialized_end=651
  _globals['_FILESERVICE']._serialized_start=698
  _globals['_FILESERVICE']._serialized_end=1131
# @@protoc_insertion_point(module_scope)