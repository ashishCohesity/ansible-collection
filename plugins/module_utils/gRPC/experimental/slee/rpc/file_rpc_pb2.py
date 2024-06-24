# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: experimental/slee/rpc/file_rpc.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from open_util.net import protorpc_pb2 as open__util_dot_net_dot_protorpc__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$experimental/slee/rpc/file_rpc.proto\x12\x1e\x63ohesity.experimental.slee.rpc\x1a\x1copen_util/net/protorpc.proto\"#\n\x0fSayHelloPayload\x12\x10\n\x08question\x18\x01 \x02(\t\" \n\x0eSayHelloResult\x12\x0e\n\x06\x61nswer\x18\x01 \x02(\t\"O\n\x11\x43reateFilePayload\x12\x11\n\tfile_path\x18\x01 \x02(\t\x12\x12\n\nsize_bytes\x18\x02 \x02(\x04\x12\x13\n\x0binit_string\x18\x03 \x01(\t\":\n\x10\x43reateFileResult\x12\x0e\n\x06status\x18\x01 \x02(\x05\x12\x16\n\x0ereturn_message\x18\x02 \x01(\t\"R\n\x14ReadFileRangePayload\x12\x11\n\tfile_path\x18\x01 \x02(\t\x12\x14\n\x0coffset_bytes\x18\x02 \x02(\x04\x12\x11\n\tlen_bytes\x18\x03 \x02(\x04\"P\n\x13ReadFileRangeResult\x12\x0e\n\x06status\x18\x01 \x02(\x05\x12\x11\n\tdata_read\x18\x02 \x02(\t\x12\x16\n\x0ereturn_message\x18\x03 \x01(\t\"Y\n\x15WriteFileRangePayload\x12\x11\n\tfile_path\x18\x01 \x02(\t\x12\x14\n\x0coffset_bytes\x18\x02 \x02(\x04\x12\x17\n\x0f\x64\x61ta_2b_written\x18\x03 \x02(\t\">\n\x14WriteFileRangeResult\x12\x0e\n\x06status\x18\x01 \x02(\x05\x12\x16\n\x0ereturn_message\x18\x02 \x01(\t2\x83\x04\n\x11RemoteFileService\x12j\n\x05Greet\x12/.cohesity.experimental.slee.rpc.SayHelloPayload\x1a..cohesity.experimental.slee.rpc.SayHelloResult\"\x00\x12s\n\nCreateFile\x12\x31.cohesity.experimental.slee.rpc.CreateFilePayload\x1a\x30.cohesity.experimental.slee.rpc.CreateFileResult\"\x00\x12|\n\rReadFileRange\x12\x34.cohesity.experimental.slee.rpc.ReadFileRangePayload\x1a\x33.cohesity.experimental.slee.rpc.ReadFileRangeResult\"\x00\x12\x7f\n\x0eWriteFileRange\x12\x35.cohesity.experimental.slee.rpc.WriteFileRangePayload\x1a\x34.cohesity.experimental.slee.rpc.WriteFileRangeResult\"\x00\x1a\x0e\x80\xf1\x04\xc0\xcf$\x88\xf1\x04\x01\x90\xf1\x04\x02\x42\x03\x80\x01\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'experimental.slee.rpc.file_rpc_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\200\001\001'
  _globals['_REMOTEFILESERVICE']._loaded_options = None
  _globals['_REMOTEFILESERVICE']._serialized_options = b'\200\361\004\300\317$\210\361\004\001\220\361\004\002'
  _globals['_SAYHELLOPAYLOAD']._serialized_start=102
  _globals['_SAYHELLOPAYLOAD']._serialized_end=137
  _globals['_SAYHELLORESULT']._serialized_start=139
  _globals['_SAYHELLORESULT']._serialized_end=171
  _globals['_CREATEFILEPAYLOAD']._serialized_start=173
  _globals['_CREATEFILEPAYLOAD']._serialized_end=252
  _globals['_CREATEFILERESULT']._serialized_start=254
  _globals['_CREATEFILERESULT']._serialized_end=312
  _globals['_READFILERANGEPAYLOAD']._serialized_start=314
  _globals['_READFILERANGEPAYLOAD']._serialized_end=396
  _globals['_READFILERANGERESULT']._serialized_start=398
  _globals['_READFILERANGERESULT']._serialized_end=478
  _globals['_WRITEFILERANGEPAYLOAD']._serialized_start=480
  _globals['_WRITEFILERANGEPAYLOAD']._serialized_end=569
  _globals['_WRITEFILERANGERESULT']._serialized_start=571
  _globals['_WRITEFILERANGERESULT']._serialized_end=633
  _globals['_REMOTEFILESERVICE']._serialized_start=636
  _globals['_REMOTEFILESERVICE']._serialized_end=1151
# @@protoc_insertion_point(module_scope)
