# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: open_util/net/protorpc.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2
from open_util.base import compression_types_pb2 as open__util_dot_base_dot_compression__types__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1copen_util/net/protorpc.proto\x12\x0c\x63ohesity.net\x1a google/protobuf/descriptor.proto\x1a&open_util/base/compression_types.proto\"d\n\nProtoRpcId\x12\x16\n\x0eincarnation_id\x18\x01 \x02(\x03\x12\x12\n\nrequest_id\x18\x02 \x02(\x03\x12\x12\n\ncluster_id\x18\x03 \x01(\x03\x12\x16\n\x0e\x63onstituent_id\x18\x04 \x01(\x03\"#\n\x06IpInfo\x12\n\n\x02ip\x18\x01 \x02(\t\x12\r\n\x05\x65poch\x18\x02 \x02(\x03\"Z\n\x14SlicedEncryptionInfo\x12\x16\n\x0esliced_enc_ver\x18\x01 \x02(\x05\x12\x16\n\x0enum_enc_slices\x18\x02 \x02(\x05\x12\x12\n\nslice_size\x18\x03 \x02(\x03\"y\n\x10ProtoRpcChecksum\x12\x31\n\x04type\x18\x01 \x01(\x0e\x32#.cohesity.net.ProtoRpcChecksum.Type\x12\x10\n\x08\x63hecksum\x18\x02 \x01(\x0c\" \n\x04Type\x12\x0c\n\x08kUnknown\x10\x00\x12\n\n\x06kCRC32\x10\x01\"\x8a\x04\n\x15ProtoRpcRequestHeader\x12\x14\n\x0cservice_name\x18\x01 \x02(\t\x12\x13\n\x0bmethod_name\x18\x02 \x02(\t\x12-\n\x0bprotorpc_id\x18\x03 \x02(\x0b\x32\x18.cohesity.net.ProtoRpcId\x12\x1e\n\x16\x63lient_send_time_usecs\x18\x04 \x02(\x03\x12\x15\n\rtimeout_msecs\x18\x05 \x01(\x05\x12\x16\n\x0e\x61rg_proto_size\x18\x06 \x02(\x05\x12\x18\n\x10\x61rg_payload_size\x18\x07 \x01(\x05\x12 \n\x18notification_listen_port\x18\x08 \x01(\x05\x12\x32\n\'min_progress_notification_interval_secs\x18\t \x01(\x05:\x01\x35\x12\x39\n\x10\x63ompression_type\x18\n \x01(\x0e\x32\x1f.cohesity.CompressionProto.Type\x12\x1e\n\x16\x65ncryption_key_locator\x18\x0b \x01(\x0c\x12,\n\x0esender_ip_info\x18\x0c \x01(\x0b\x32\x14.cohesity.net.IpInfo\x12\x12\n\nauth_token\x18\r \x01(\x0c\x12;\n\x0fsliced_enc_info\x18\x0e \x01(\x0b\x32\".cohesity.net.SlicedEncryptionInfo\"\xc3\x01\n\x0eProtoRpcStatus\"k\n\x04Type\x12\x0c\n\x08kNoError\x10\x00\x12\x0c\n\x08kTimeout\x10\x01\x12\x13\n\x0fkTransportError\x10\x02\x12\x11\n\rkServiceError\x10\x03\x12\x10\n\x0ckMethodError\x10\x04\x12\r\n\tkAppError\x10\x05\"D\n\x11MethodErrorReason\x12\x13\n\x0fkMethodNotFound\x10\x00\x12\x1a\n\x16kEncryptionKeyNotFound\x10\x01\"\xac\x03\n\x16ProtoRpcResponseHeader\x12;\n\x06status\x18\x01 \x01(\x0e\x32!.cohesity.net.ProtoRpcStatus.Type:\x08kNoError\x12-\n\x0bprotorpc_id\x18\x02 \x01(\x0b\x32\x18.cohesity.net.ProtoRpcId\x12\x14\n\x0c\x65rror_detail\x18\x03 \x01(\t\x12\x11\n\tapp_error\x18\x04 \x01(\x05\x12\x19\n\x11result_proto_size\x18\x05 \x01(\x05\x12\x1b\n\x13result_payload_size\x18\x06 \x01(\x05\x12K\n\x13method_error_reason\x18\x07 \x01(\x0e\x32..cohesity.net.ProtoRpcStatus.MethodErrorReason\x12\x1b\n\x13\x61pp_exec_time_usecs\x18\x08 \x01(\x03\x12\x1e\n\x16server_recv_time_usecs\x18\t \x01(\x03\x12;\n\x0fsliced_enc_info\x18\n \x01(\x0b\x32\".cohesity.net.SlicedEncryptionInfo\"x\n\x17ProtoRpcBinaryLogHeader\x12\x1f\n\x17peer_transport_endpoint\x18\x01 \x01(\t\x12 \n\x18local_transport_endpoint\x18\x02 \x01(\t\x12\x1a\n\x12server_sequence_id\x18\x03 \x01(\x03\"\xf8\x01\n\x0fProtoRpcApiList\x12\x38\n\x08port_vec\x18\x03 \x03(\x0b\x32&.cohesity.net.ProtoRpcApiList.PortInfo\x1aN\n\x07SvcInfo\x12\x15\n\rsvc_full_name\x18\x01 \x02(\t\x12\x17\n\x0fmethod_name_vec\x18\x02 \x03(\t\x12\x13\n\x0b\x61ll_methods\x18\x03 \x01(\x08\x1a[\n\x08PortInfo\x12\x17\n\x0bserver_port\x18\x01 \x02(\x05:\x02-1\x12\x36\n\x07svc_vec\x18\x02 \x03(\x0b\x32%.cohesity.net.ProtoRpcApiList.SvcInfo:?\n\x15\x64\x65\x66\x61ult_timeout_msecs\x12\x1f.google.protobuf.ServiceOptions\x18\x90N \x01(\x05:M\n#default_timeout_exponential_backoff\x12\x1f.google.protobuf.ServiceOptions\x18\x91N \x01(\x08:E\n\x1b\x64\x65\x66\x61ult_timeout_max_retries\x12\x1f.google.protobuf.ServiceOptions\x18\x92N \x01(\x05:X\n.default_enable_retry_on_connection_termination\x12\x1f.google.protobuf.ServiceOptions\x18\x93N \x01(\x08:c\n\x18\x64\x65\x66\x61ult_compression_type\x12\x1f.google.protobuf.ServiceOptions\x18\x94N \x01(\x0e\x32\x1f.cohesity.CompressionProto.Type:7\n\rtimeout_msecs\x12\x1e.google.protobuf.MethodOptions\x18\xa0\x9c\x01 \x01(\x05:E\n\x1btimeout_exponential_backoff\x12\x1e.google.protobuf.MethodOptions\x18\xa1\x9c\x01 \x01(\x08:=\n\x13timeout_max_retries\x12\x1e.google.protobuf.MethodOptions\x18\xa2\x9c\x01 \x01(\x05:P\n&enable_retry_on_connection_termination\x12\x1e.google.protobuf.MethodOptions\x18\xa3\x9c\x01 \x01(\x08:[\n\x10\x63ompression_type\x12\x1e.google.protobuf.MethodOptions\x18\xa4\x9c\x01 \x01(\x0e\x32\x1f.cohesity.CompressionProto.TypeB1\n\x10\x63om.cohesity.netB\rProtoRpcProtoH\x01Z\x0c\x63ohesity/net')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'open_util.net.protorpc_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\020com.cohesity.netB\rProtoRpcProtoH\001Z\014cohesity/net'
  _globals['_PROTORPCID']._serialized_start=120
  _globals['_PROTORPCID']._serialized_end=220
  _globals['_IPINFO']._serialized_start=222
  _globals['_IPINFO']._serialized_end=257
  _globals['_SLICEDENCRYPTIONINFO']._serialized_start=259
  _globals['_SLICEDENCRYPTIONINFO']._serialized_end=349
  _globals['_PROTORPCCHECKSUM']._serialized_start=351
  _globals['_PROTORPCCHECKSUM']._serialized_end=472
  _globals['_PROTORPCCHECKSUM_TYPE']._serialized_start=440
  _globals['_PROTORPCCHECKSUM_TYPE']._serialized_end=472
  _globals['_PROTORPCREQUESTHEADER']._serialized_start=475
  _globals['_PROTORPCREQUESTHEADER']._serialized_end=997
  _globals['_PROTORPCSTATUS']._serialized_start=1000
  _globals['_PROTORPCSTATUS']._serialized_end=1195
  _globals['_PROTORPCSTATUS_TYPE']._serialized_start=1018
  _globals['_PROTORPCSTATUS_TYPE']._serialized_end=1125
  _globals['_PROTORPCSTATUS_METHODERRORREASON']._serialized_start=1127
  _globals['_PROTORPCSTATUS_METHODERRORREASON']._serialized_end=1195
  _globals['_PROTORPCRESPONSEHEADER']._serialized_start=1198
  _globals['_PROTORPCRESPONSEHEADER']._serialized_end=1626
  _globals['_PROTORPCBINARYLOGHEADER']._serialized_start=1628
  _globals['_PROTORPCBINARYLOGHEADER']._serialized_end=1748
  _globals['_PROTORPCAPILIST']._serialized_start=1751
  _globals['_PROTORPCAPILIST']._serialized_end=1999
  _globals['_PROTORPCAPILIST_SVCINFO']._serialized_start=1828
  _globals['_PROTORPCAPILIST_SVCINFO']._serialized_end=1906
  _globals['_PROTORPCAPILIST_PORTINFO']._serialized_start=1908
  _globals['_PROTORPCAPILIST_PORTINFO']._serialized_end=1999
# @@protoc_insertion_point(module_scope)
