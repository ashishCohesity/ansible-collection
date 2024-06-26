# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: experimental/zhuhua/rpc/simple_service.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from open_util.net import protorpc_pb2 as open__util_dot_net_dot_protorpc__pb2
from util.base import op_clock_pb2 as util_dot_base_dot_op__clock__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,experimental/zhuhua/rpc/simple_service.proto\x12 cohesity.experimental.zhuhua.rpc\x1a\x1copen_util/net/protorpc.proto\x1a\x18util/base/op_clock.proto\"\xe2\x01\n\nErrorProto\x12\x46\n\x08\x65rr_code\x18\x01 \x01(\x0e\x32\x34.cohesity.experimental.zhuhua.rpc.ErrorProto.ErrCode\x12\x12\n\nerr_detail\x18\x02 \x01(\t\"x\n\x07\x45rrCode\x12\x0c\n\x08kNoError\x10\x00\x12\x14\n\x10kInvalidFileName\x10\x01\x12\x14\n\x10kNonExistantFile\x10\x02\x12\x0c\n\x08kIOError\x10\x03\x12\x14\n\x10kInvalidArgument\x10\x04\x12\x0f\n\x0bkEOFReached\x10\x05\"!\n\rCreateFileArg\x12\x10\n\x08\x66ilename\x18\x01 \x01(\t\"d\n\x10\x43reateFileResult\x12\x0f\n\x07\x63reated\x18\x01 \x01(\x08\x12?\n\terr_proto\x18\x02 \x01(\x0b\x32,.cohesity.experimental.zhuhua.rpc.ErrorProto\"j\n\x10ReadFileRangeArg\x12\x10\n\x08\x66ilename\x18\x01 \x01(\t\x12\x0e\n\x06offset\x18\x02 \x01(\x03\x12\x0e\n\x06length\x18\x03 \x01(\x03\x12\x11\n\tbufoffset\x18\x04 \x01(\x03\x12\x11\n\tbufmaxlen\x18\x05 \x01(\x03\"h\n\x13ReadFileRangeResult\x12\x10\n\x08numbytes\x18\x01 \x01(\x03\x12?\n\terr_proto\x18\x02 \x01(\x0b\x32,.cohesity.experimental.zhuhua.rpc.ErrorProto\"X\n\x11WriteFileRangeArg\x12\x10\n\x08\x66ilename\x18\x01 \x01(\t\x12\x0e\n\x06offset\x18\x02 \x01(\x03\x12\x0e\n\x06length\x18\x03 \x01(\x03\x12\x11\n\tbufoffset\x18\x04 \x01(\x03\"i\n\x14WriteFileRangeResult\x12\x10\n\x08numbytes\x18\x01 \x01(\x03\x12?\n\terr_proto\x18\x02 \x01(\x0b\x32,.cohesity.experimental.zhuhua.rpc.ErrorProto2\x92\x03\n\rSimpleService\x12s\n\nCreateFile\x12/.cohesity.experimental.zhuhua.rpc.CreateFileArg\x1a\x32.cohesity.experimental.zhuhua.rpc.CreateFileResult\"\x00\x12\x7f\n\x0eWriteFileRange\x12\x33.cohesity.experimental.zhuhua.rpc.WriteFileRangeArg\x1a\x36.cohesity.experimental.zhuhua.rpc.WriteFileRangeResult\"\x00\x12|\n\rReadFileRange\x12\x32.cohesity.experimental.zhuhua.rpc.ReadFileRangeArg\x1a\x35.cohesity.experimental.zhuhua.rpc.ReadFileRangeResult\"\x00\x1a\r\x80\xf1\x04\xa0\x1f\x88\xf1\x04\x01\x90\xf1\x04\x05\x42\x03\x80\x01\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'experimental.zhuhua.rpc.simple_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\200\001\001'
  _globals['_SIMPLESERVICE']._loaded_options = None
  _globals['_SIMPLESERVICE']._serialized_options = b'\200\361\004\240\037\210\361\004\001\220\361\004\005'
  _globals['_ERRORPROTO']._serialized_start=139
  _globals['_ERRORPROTO']._serialized_end=365
  _globals['_ERRORPROTO_ERRCODE']._serialized_start=245
  _globals['_ERRORPROTO_ERRCODE']._serialized_end=365
  _globals['_CREATEFILEARG']._serialized_start=367
  _globals['_CREATEFILEARG']._serialized_end=400
  _globals['_CREATEFILERESULT']._serialized_start=402
  _globals['_CREATEFILERESULT']._serialized_end=502
  _globals['_READFILERANGEARG']._serialized_start=504
  _globals['_READFILERANGEARG']._serialized_end=610
  _globals['_READFILERANGERESULT']._serialized_start=612
  _globals['_READFILERANGERESULT']._serialized_end=716
  _globals['_WRITEFILERANGEARG']._serialized_start=718
  _globals['_WRITEFILERANGEARG']._serialized_end=806
  _globals['_WRITEFILERANGERESULT']._serialized_start=808
  _globals['_WRITEFILERANGERESULT']._serialized_end=913
  _globals['_SIMPLESERVICE']._serialized_start=916
  _globals['_SIMPLESERVICE']._serialized_end=1318
# @@protoc_insertion_point(module_scope)
