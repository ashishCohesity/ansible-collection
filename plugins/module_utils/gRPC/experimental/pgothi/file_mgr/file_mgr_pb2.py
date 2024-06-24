# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: experimental/pgothi/file_mgr/file_mgr.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from open_util.net import protorpc_pb2 as open__util_dot_net_dot_protorpc__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+experimental/pgothi/file_mgr/file_mgr.proto\x12$cohesity.experimental.pgothi.filemgr\x1a\x1copen_util/net/protorpc.proto\"+\n\tFileRange\x12\x0e\n\x06offset\x18\x01 \x01(\x03\x12\x0e\n\x06length\x18\x02 \x01(\x05\"f\n\nErrorProto\"X\n\x04\x43ode\x12\x11\n\rkErrorSuccess\x10\x00\x12\x16\n\x12kErrorFileNotFound\x10\x01\x12\x12\n\x0ekErrorInternal\x10\x02\x12\x11\n\rkErrorUnknown\x10\x03\"\"\n\rCreateFileArg\x12\x11\n\tfile_name\x18\x01 \x01(\t\"i\n\x12\x43reateFileResponse\x12S\n\x05\x65rror\x18\x01 \x01(\x0e\x32\x35.cohesity.experimental.pgothi.filemgr.ErrorProto.Code:\rkErrorSuccess\"f\n\x10ReadFileRangeArg\x12\x11\n\tfile_name\x18\x01 \x01(\t\x12?\n\x06\x65xtent\x18\x02 \x01(\x0b\x32/.cohesity.experimental.pgothi.filemgr.FileRange\"l\n\x15ReadFileRangeResponse\x12S\n\x05\x65rror\x18\x01 \x01(\x0e\x32\x35.cohesity.experimental.pgothi.filemgr.ErrorProto.Code:\rkErrorSuccess\"g\n\x11WriteFileRangeArg\x12\x11\n\tfile_name\x18\x01 \x01(\t\x12?\n\x06\x65xtent\x18\x02 \x01(\x0b\x32/.cohesity.experimental.pgothi.filemgr.FileRange\"m\n\x16WriteFileRangeResponse\x12S\n\x05\x65rror\x18\x01 \x01(\x0e\x32\x35.cohesity.experimental.pgothi.filemgr.ErrorProto.Code:\rkErrorSuccess\"$\n\x0e\x46ileMgrPingArg\x12\x12\n\x04name\x18\x01 \x01(\t:\x04Ping\"\'\n\x13\x46ileMgrPingResponse\x12\x10\n\x08greeting\x18\x01 \x01(\t2\xaf\x04\n\x0e\x46ileMgrService\x12}\n\nCreateFile\x12\x33.cohesity.experimental.pgothi.filemgr.CreateFileArg\x1a\x38.cohesity.experimental.pgothi.filemgr.CreateFileResponse\"\x00\x12\x86\x01\n\rReadFileRange\x12\x36.cohesity.experimental.pgothi.filemgr.ReadFileRangeArg\x1a;.cohesity.experimental.pgothi.filemgr.ReadFileRangeResponse\"\x00\x12\x89\x01\n\x0eWriteFileRange\x12\x37.cohesity.experimental.pgothi.filemgr.WriteFileRangeArg\x1a<.cohesity.experimental.pgothi.filemgr.WriteFileRangeResponse\"\x00\x12y\n\x04Ping\x12\x34.cohesity.experimental.pgothi.filemgr.FileMgrPingArg\x1a\x39.cohesity.experimental.pgothi.filemgr.FileMgrPingResponse\"\x00\x1a\x0e\x80\xf1\x04\xc0\xcf$\x88\xf1\x04\x01\x90\xf1\x04\x02\x42\x03\x80\x01\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'experimental.pgothi.file_mgr.file_mgr_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\200\001\001'
  _globals['_FILEMGRSERVICE']._loaded_options = None
  _globals['_FILEMGRSERVICE']._serialized_options = b'\200\361\004\300\317$\210\361\004\001\220\361\004\002'
  _globals['_FILERANGE']._serialized_start=115
  _globals['_FILERANGE']._serialized_end=158
  _globals['_ERRORPROTO']._serialized_start=160
  _globals['_ERRORPROTO']._serialized_end=262
  _globals['_ERRORPROTO_CODE']._serialized_start=174
  _globals['_ERRORPROTO_CODE']._serialized_end=262
  _globals['_CREATEFILEARG']._serialized_start=264
  _globals['_CREATEFILEARG']._serialized_end=298
  _globals['_CREATEFILERESPONSE']._serialized_start=300
  _globals['_CREATEFILERESPONSE']._serialized_end=405
  _globals['_READFILERANGEARG']._serialized_start=407
  _globals['_READFILERANGEARG']._serialized_end=509
  _globals['_READFILERANGERESPONSE']._serialized_start=511
  _globals['_READFILERANGERESPONSE']._serialized_end=619
  _globals['_WRITEFILERANGEARG']._serialized_start=621
  _globals['_WRITEFILERANGEARG']._serialized_end=724
  _globals['_WRITEFILERANGERESPONSE']._serialized_start=726
  _globals['_WRITEFILERANGERESPONSE']._serialized_end=835
  _globals['_FILEMGRPINGARG']._serialized_start=837
  _globals['_FILEMGRPINGARG']._serialized_end=873
  _globals['_FILEMGRPINGRESPONSE']._serialized_start=875
  _globals['_FILEMGRPINGRESPONSE']._serialized_end=914
  _globals['_FILEMGRSERVICE']._serialized_start=917
  _globals['_FILEMGRSERVICE']._serialized_end=1476
# @@protoc_insertion_point(module_scope)
