# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: experimental/abhijeet/rpc/file_service.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from open_util.net import protorpc_pb2 as open__util_dot_net_dot_protorpc__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,experimental/abhijeet/rpc/file_service.proto\x12\"cohesity.experimental.abhijeet.rpc\x1a\x1copen_util/net/protorpc.proto\">\n\x11\x46ileCreateRequest\x12\x11\n\tfile_name\x18\x01 \x01(\t\x12\x16\n\x0e\x66ile_extension\x18\x02 \x01(\t\"\"\n\x10\x46ileCreateResult\x12\x0e\n\x06status\x18\x01 \x01(\x08\"c\n\x10\x46ileWriteRequest\x12\x11\n\tfile_name\x18\x01 \x01(\t\x12\x11\n\x06offset\x18\x02 \x01(\x03:\x01\x30\x12\x15\n\rdata_to_write\x18\x03 \x01(\x0c\x12\x12\n\nwrite_mode\x18\x04 \x01(\t\"!\n\x0f\x46ileWriteResult\x12\x0e\n\x06status\x18\x01 \x01(\x08\"G\n\x0f\x46ileReadRequest\x12\x11\n\tfile_name\x18\x01 \x01(\t\x12\x11\n\x06offset\x18\x02 \x01(\x03:\x01\x30\x12\x0e\n\x06length\x18\x03 \x01(\x03\".\n\x0e\x46ileReadResult\x12\x0e\n\x06status\x18\x01 \x01(\x08\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\x32\x94\x03\n\x0b\x46ileService\x12{\n\nCreateFile\x12\x35.cohesity.experimental.abhijeet.rpc.FileCreateRequest\x1a\x34.cohesity.experimental.abhijeet.rpc.FileCreateResult\"\x00\x12}\n\x0eWriteFileRange\x12\x34.cohesity.experimental.abhijeet.rpc.FileWriteRequest\x1a\x33.cohesity.experimental.abhijeet.rpc.FileWriteResult\"\x00\x12z\n\rReadFileRange\x12\x33.cohesity.experimental.abhijeet.rpc.FileReadRequest\x1a\x32.cohesity.experimental.abhijeet.rpc.FileReadResult\"\x00\x1a\r\x80\xf1\x04\xe8\x07\x88\xf1\x04\x01\x90\xf1\x04\x02\x42\x03\x80\x01\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'experimental.abhijeet.rpc.file_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\200\001\001'
  _globals['_FILESERVICE']._loaded_options = None
  _globals['_FILESERVICE']._serialized_options = b'\200\361\004\350\007\210\361\004\001\220\361\004\002'
  _globals['_FILECREATEREQUEST']._serialized_start=114
  _globals['_FILECREATEREQUEST']._serialized_end=176
  _globals['_FILECREATERESULT']._serialized_start=178
  _globals['_FILECREATERESULT']._serialized_end=212
  _globals['_FILEWRITEREQUEST']._serialized_start=214
  _globals['_FILEWRITEREQUEST']._serialized_end=313
  _globals['_FILEWRITERESULT']._serialized_start=315
  _globals['_FILEWRITERESULT']._serialized_end=348
  _globals['_FILEREADREQUEST']._serialized_start=350
  _globals['_FILEREADREQUEST']._serialized_end=421
  _globals['_FILEREADRESULT']._serialized_start=423
  _globals['_FILEREADRESULT']._serialized_end=469
  _globals['_FILESERVICE']._serialized_start=472
  _globals['_FILESERVICE']._serialized_end=876
# @@protoc_insertion_point(module_scope)
