# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: experimental/dane.vandyck/nhce/service.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from open_util.net import protorpc_pb2 as open__util_dot_net_dot_protorpc__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,experimental/dane.vandyck/nhce/service.proto\x12\'cohesity.experimental.dane_vandyck.nhce\x1a\x1copen_util/net/protorpc.proto\";\n\x0cWriteRequest\x12\x0c\n\x04\x66ile\x18\x01 \x02(\t\x12\x0e\n\x06offset\x18\x02 \x02(\x03\x12\r\n\x05\x64\x65lay\x18\x03 \x01(\x03\"&\n\rWriteResponse\x12\x15\n\rbytes_written\x18\x01 \x01(\x03\"H\n\x0bReadRequest\x12\x0c\n\x04\x66ile\x18\x01 \x02(\t\x12\x0e\n\x06offset\x18\x02 \x02(\x03\x12\x0c\n\x04size\x18\x03 \x02(\x03\x12\r\n\x05\x64\x65lay\x18\x04 \x01(\x03\"\"\n\x0cReadResponse\x12\x12\n\nbytes_read\x18\x01 \x01(\x03\x32\x89\x02\n\x07Service\x12x\n\x05Write\x12\x35.cohesity.experimental.dane_vandyck.nhce.WriteRequest\x1a\x36.cohesity.experimental.dane_vandyck.nhce.WriteResponse\"\x00\x12u\n\x04Read\x12\x34.cohesity.experimental.dane_vandyck.nhce.ReadRequest\x1a\x35.cohesity.experimental.dane_vandyck.nhce.ReadResponse\"\x00\x1a\r\x80\xf1\x04\xe8\x07\x88\xf1\x04\x01\x90\xf1\x04\x02\x42\x03\x80\x01\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'experimental.dane.vandyck.nhce.service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\200\001\001'
  _globals['_SERVICE']._loaded_options = None
  _globals['_SERVICE']._serialized_options = b'\200\361\004\350\007\210\361\004\001\220\361\004\002'
  _globals['_WRITEREQUEST']._serialized_start=119
  _globals['_WRITEREQUEST']._serialized_end=178
  _globals['_WRITERESPONSE']._serialized_start=180
  _globals['_WRITERESPONSE']._serialized_end=218
  _globals['_READREQUEST']._serialized_start=220
  _globals['_READREQUEST']._serialized_end=292
  _globals['_READRESPONSE']._serialized_start=294
  _globals['_READRESPONSE']._serialized_end=328
  _globals['_SERVICE']._serialized_start=331
  _globals['_SERVICE']._serialized_end=596
# @@protoc_insertion_point(module_scope)
