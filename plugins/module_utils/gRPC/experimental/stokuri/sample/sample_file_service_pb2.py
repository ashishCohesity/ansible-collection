# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: experimental/stokuri/sample/sample_file_service.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from open_util.net import protorpc_pb2 as open__util_dot_net_dot_protorpc__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5experimental/stokuri/sample/sample_file_service.proto\x12$cohesity.experimental.stokuri.sample\x1a\x1copen_util/net/protorpc.proto\"+\n\tFileRange\x12\x0e\n\x06offset\x18\x01 \x01(\x03\x12\x0e\n\x06length\x18\x02 \x01(\x05\"\"\n\rCreateFileArg\x12\x11\n\tfile_name\x18\x01 \x01(\t\"r\n\x10\x43reateFileResult\x12^\n\x05\x65rror\x18\x01 \x01(\x0e\x32@.cohesity.experimental.stokuri.sample.SampleFileServiceErrorCode:\rkErrorSuccess\"f\n\x10ReadFileRangeArg\x12\x11\n\tfile_name\x18\x01 \x01(\t\x12?\n\x06\x65xtent\x18\x02 \x01(\x0b\x32/.cohesity.experimental.stokuri.sample.FileRange\"u\n\x13ReadFileRangeResult\x12^\n\x05\x65rror\x18\x02 \x01(\x0e\x32@.cohesity.experimental.stokuri.sample.SampleFileServiceErrorCode:\rkErrorSuccess\"g\n\x11WriteFileRangeArg\x12\x11\n\tfile_name\x18\x01 \x01(\t\x12?\n\x06\x65xtent\x18\x02 \x01(\x0b\x32/.cohesity.experimental.stokuri.sample.FileRange\"v\n\x14WriteFileRangeResult\x12^\n\x05\x65rror\x18\x02 \x01(\x0e\x32@.cohesity.experimental.stokuri.sample.SampleFileServiceErrorCode:\rkErrorSuccess\"/\n\x18SampleFileServicePingArg\x12\x13\n\x04name\x18\x01 \x01(\t:\x05Hello\"/\n\x1bSampleFileServicePingResult\x12\x10\n\x08greeting\x18\x01 \x01(\t*n\n\x1aSampleFileServiceErrorCode\x12\x11\n\rkErrorSuccess\x10\x00\x12\x16\n\x12kErrorFileNotFound\x10\x01\x12\x12\n\x0ekErrorInternal\x10\x02\x12\x11\n\rkErrorUnknown\x10\x03\x32\xbf\x04\n\x11SampleFileService\x12{\n\nCreateFile\x12\x33.cohesity.experimental.stokuri.sample.CreateFileArg\x1a\x36.cohesity.experimental.stokuri.sample.CreateFileResult\"\x00\x12\x84\x01\n\rReadFileRange\x12\x36.cohesity.experimental.stokuri.sample.ReadFileRangeArg\x1a\x39.cohesity.experimental.stokuri.sample.ReadFileRangeResult\"\x00\x12\x87\x01\n\x0eWriteFileRange\x12\x37.cohesity.experimental.stokuri.sample.WriteFileRangeArg\x1a:.cohesity.experimental.stokuri.sample.WriteFileRangeResult\"\x00\x12\x8b\x01\n\x04Ping\x12>.cohesity.experimental.stokuri.sample.SampleFileServicePingArg\x1a\x41.cohesity.experimental.stokuri.sample.SampleFileServicePingResult\"\x00\x1a\x0e\x80\xf1\x04\xc0\xcf$\x88\xf1\x04\x01\x90\xf1\x04\x02\x42\x03\x80\x01\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'experimental.stokuri.sample.sample_file_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\200\001\001'
  _globals['_SAMPLEFILESERVICE']._loaded_options = None
  _globals['_SAMPLEFILESERVICE']._serialized_options = b'\200\361\004\300\317$\210\361\004\001\220\361\004\002'
  _globals['_SAMPLEFILESERVICEERRORCODE']._serialized_start=868
  _globals['_SAMPLEFILESERVICEERRORCODE']._serialized_end=978
  _globals['_FILERANGE']._serialized_start=125
  _globals['_FILERANGE']._serialized_end=168
  _globals['_CREATEFILEARG']._serialized_start=170
  _globals['_CREATEFILEARG']._serialized_end=204
  _globals['_CREATEFILERESULT']._serialized_start=206
  _globals['_CREATEFILERESULT']._serialized_end=320
  _globals['_READFILERANGEARG']._serialized_start=322
  _globals['_READFILERANGEARG']._serialized_end=424
  _globals['_READFILERANGERESULT']._serialized_start=426
  _globals['_READFILERANGERESULT']._serialized_end=543
  _globals['_WRITEFILERANGEARG']._serialized_start=545
  _globals['_WRITEFILERANGEARG']._serialized_end=648
  _globals['_WRITEFILERANGERESULT']._serialized_start=650
  _globals['_WRITEFILERANGERESULT']._serialized_end=768
  _globals['_SAMPLEFILESERVICEPINGARG']._serialized_start=770
  _globals['_SAMPLEFILESERVICEPINGARG']._serialized_end=817
  _globals['_SAMPLEFILESERVICEPINGRESULT']._serialized_start=819
  _globals['_SAMPLEFILESERVICEPINGRESULT']._serialized_end=866
  _globals['_SAMPLEFILESERVICE']._serialized_start=981
  _globals['_SAMPLEFILESERVICE']._serialized_end=1556
# @@protoc_insertion_point(module_scope)
