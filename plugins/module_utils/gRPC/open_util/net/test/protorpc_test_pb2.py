# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: open_util/net/test/protorpc_test.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from open_util.net import protorpc_pb2 as open__util_dot_net_dot_protorpc__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&open_util/net/test/protorpc_test.proto\x12\x08xx.yy.zz\x1a\x1copen_util/net/protorpc.proto\"\xc9\x01\n\x08Proc1Arg\x12\x0b\n\x03val\x18\x01 \x02(\x05\x12\x0c\n\x04\x64\x61ta\x18\x02 \x02(\t\x12\x10\n\x08\x64\x65lay_ms\x18\x03 \x01(\x05\x12\x16\n\x0esend_app_error\x18\x04 \x01(\x05\x12\x1d\n\x15send_app_error_detail\x18\x05 \x01(\t\x12\x1e\n\x16include_app_error_data\x18\x06 \x01(\x08\x12\x17\n\x0flocal_transport\x18\x07 \x01(\x08\x12 \n\x18include_client_cert_info\x18\x08 \x01(\x08\"B\n\x0bProc1Result\x12\x0b\n\x03val\x18\x01 \x02(\x05\x12\x0c\n\x04\x64\x61ta\x18\x02 \x02(\t\x12\x18\n\x10\x63lient_cert_info\x18\x03 \x01(\t\"5\n\x08Proc2Arg\x12\x10\n\x08\x64\x65lay_ms\x18\x01 \x02(\x05\x12\x17\n\x0flocal_transport\x18\x02 \x01(\x08\" \n\x0bProc2Result\x12\x11\n\tdelay_str\x18\x01 \x02(\t\"\xd9\x02\n\x08Proc3Arg\x12\x11\n\tterminate\x18\x01 \x01(\x08\x12\x17\n\x0flocal_transport\x18\x02 \x01(\x08\x12\x38\n\x10repeated_msg_vec\x18\x03 \x03(\x0b\x32\x1e.xx.yy.zz.Proc3Arg.RepeatedMsg\x12\x18\n\x10payload_checksum\x18\x04 \x01(\r\x1a\xcc\x01\n\x0bRepeatedMsg\x12-\n\x02id\x18\x01 \x01(\x0b\x32!.xx.yy.zz.Proc3Arg.RepeatedMsg.Id\x12\x31\n\x04\x64\x61ta\x18\x02 \x01(\x0b\x32#.xx.yy.zz.Proc3Arg.RepeatedMsg.Data\x1a$\n\x02Id\x12\x0e\n\x06id_int\x18\x01 \x01(\x03\x12\x0e\n\x06id_str\x18\x02 \x01(\x0c\x1a\x35\n\x04\x44\x61ta\x12-\n\x02id\x18\x01 \x01(\x0b\x32!.xx.yy.zz.Proc3Arg.RepeatedMsg.Id\"^\n\x0bProc3Result\x12\x11\n\tterminate\x18\x01 \x02(\x08\x12\x18\n\x10payload_checksum\x18\x02 \x01(\r\x12\"\n\x1a\x63hecksum_enabled_gflag_set\x18\x05 \x01(\x08*i\n\nErrorProto\x12\x0c\n\x08kNoError\x10\x00\x12\n\n\x06kRetry\x10\x01\x12\x0c\n\x08kTimeout\x10\x02\x12\x13\n\x0fkTransportError\x10\x03\x12\x0e\n\nkAppError1\x10\x04\x12\x0e\n\nkAppError2\x10\x05\x32\xdb\x01\n\x0cProtoRpcSvc1\x12\x34\n\x05Proc1\x12\x12.xx.yy.zz.Proc1Arg\x1a\x15.xx.yy.zz.Proc1Result\"\x00\x12\x38\n\x05Proc2\x12\x12.xx.yy.zz.Proc2Arg\x1a\x15.xx.yy.zz.Proc2Result\"\x04\xa0\xe2\t\x01\x12P\n!ServerDoesntPopulateRequiredField\x12\x12.xx.yy.zz.Proc1Arg\x1a\x15.xx.yy.zz.Proc1Result\"\x00\x1a\t\x80\xf1\x04\xd0\x0f\x90\xf1\x04\x01\x32\x42\n\x0cProtoRpcSvc2\x12\x32\n\x05Proc3\x12\x12.xx.yy.zz.Proc3Arg\x1a\x15.xx.yy.zz.Proc3ResultB0\n\x15\x63om.cohesity.net.testB\x11ProtoRpcTestProto\x80\x01\x01\x88\x01\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'open_util.net.test.protorpc_test_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\025com.cohesity.net.testB\021ProtoRpcTestProto\200\001\001\210\001\001'
  _globals['_PROTORPCSVC1']._loaded_options = None
  _globals['_PROTORPCSVC1']._serialized_options = b'\200\361\004\320\017\220\361\004\001'
  _globals['_PROTORPCSVC1'].methods_by_name['Proc2']._loaded_options = None
  _globals['_PROTORPCSVC1'].methods_by_name['Proc2']._serialized_options = b'\240\342\t\001'
  _globals['_ERRORPROTO']._serialized_start=887
  _globals['_ERRORPROTO']._serialized_end=992
  _globals['_PROC1ARG']._serialized_start=83
  _globals['_PROC1ARG']._serialized_end=284
  _globals['_PROC1RESULT']._serialized_start=286
  _globals['_PROC1RESULT']._serialized_end=352
  _globals['_PROC2ARG']._serialized_start=354
  _globals['_PROC2ARG']._serialized_end=407
  _globals['_PROC2RESULT']._serialized_start=409
  _globals['_PROC2RESULT']._serialized_end=441
  _globals['_PROC3ARG']._serialized_start=444
  _globals['_PROC3ARG']._serialized_end=789
  _globals['_PROC3ARG_REPEATEDMSG']._serialized_start=585
  _globals['_PROC3ARG_REPEATEDMSG']._serialized_end=789
  _globals['_PROC3ARG_REPEATEDMSG_ID']._serialized_start=698
  _globals['_PROC3ARG_REPEATEDMSG_ID']._serialized_end=734
  _globals['_PROC3ARG_REPEATEDMSG_DATA']._serialized_start=736
  _globals['_PROC3ARG_REPEATEDMSG_DATA']._serialized_end=789
  _globals['_PROC3RESULT']._serialized_start=791
  _globals['_PROC3RESULT']._serialized_end=885
  _globals['_PROTORPCSVC1']._serialized_start=995
  _globals['_PROTORPCSVC1']._serialized_end=1214
  _globals['_PROTORPCSVC2']._serialized_start=1216
  _globals['_PROTORPCSVC2']._serialized_end=1282
# @@protoc_insertion_point(module_scope)