# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: experimental/surya/rpc/rpc_service.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from open_util.net import protorpc_pb2 as open__util_dot_net_dot_protorpc__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(experimental/surya/rpc/rpc_service.proto\x12\x16\x65xperimental.surya.rpc\x1a\x1copen_util/net/protorpc.proto\"!\n\rCreateFileArg\x12\x10\n\x08\x66ilename\x18\x01 \x01(\t\"A\n\x10ReadFileRangeArg\x12\x10\n\x08\x66ilename\x18\x01 \x01(\t\x12\x0e\n\x06offset\x18\x02 \x01(\r\x12\x0b\n\x03len\x18\x03 \x01(\r\"P\n\x11WriteFileRangeArg\x12\x10\n\x08\x66ilename\x18\x01 \x01(\t\x12\x0e\n\x06offset\x18\x02 \x01(\r\x12\x0b\n\x03len\x18\x03 \x01(\r\x12\x0c\n\x04\x64\x61ta\x18\x04 \x01(\t\"\x1f\n\x0c\x46ileResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\"\x1b\n\x08GreetArg\x12\x0f\n\x07message\x18\x01 \x01(\t\"\x1c\n\x0bGreetResult\x12\r\n\x05reply\x18\x01 \x01(\t2\xb9\x02\n\x0b\x46ileService\x12[\n\nCreateFile\x12%.experimental.surya.rpc.CreateFileArg\x1a$.experimental.surya.rpc.FileResponse\"\x00\x12\x61\n\rReadFileRange\x12(.experimental.surya.rpc.ReadFileRangeArg\x1a$.experimental.surya.rpc.FileResponse\"\x00\x12\x63\n\x0eWriteFileRange\x12).experimental.surya.rpc.WriteFileRangeArg\x1a$.experimental.surya.rpc.FileResponse\"\x00\x1a\x05\x80\xf1\x04\xe8\x07\x32o\n\x0cHelloService\x12P\n\x05Greet\x12 .experimental.surya.rpc.GreetArg\x1a#.experimental.surya.rpc.GreetResult\"\x00\x1a\r\x80\xf1\x04\xe8\x07\x88\xf1\x04\x01\x90\xf1\x04\x02\x42\x03\x80\x01\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'experimental.surya.rpc.rpc_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\200\001\001'
  _globals['_FILESERVICE']._loaded_options = None
  _globals['_FILESERVICE']._serialized_options = b'\200\361\004\350\007'
  _globals['_HELLOSERVICE']._loaded_options = None
  _globals['_HELLOSERVICE']._serialized_options = b'\200\361\004\350\007\210\361\004\001\220\361\004\002'
  _globals['_CREATEFILEARG']._serialized_start=98
  _globals['_CREATEFILEARG']._serialized_end=131
  _globals['_READFILERANGEARG']._serialized_start=133
  _globals['_READFILERANGEARG']._serialized_end=198
  _globals['_WRITEFILERANGEARG']._serialized_start=200
  _globals['_WRITEFILERANGEARG']._serialized_end=280
  _globals['_FILERESPONSE']._serialized_start=282
  _globals['_FILERESPONSE']._serialized_end=313
  _globals['_GREETARG']._serialized_start=315
  _globals['_GREETARG']._serialized_end=342
  _globals['_GREETRESULT']._serialized_start=344
  _globals['_GREETRESULT']._serialized_end=372
  _globals['_FILESERVICE']._serialized_start=375
  _globals['_FILESERVICE']._serialized_end=688
  _globals['_HELLOSERVICE']._serialized_start=690
  _globals['_HELLOSERVICE']._serialized_end=801
# @@protoc_insertion_point(module_scope)
