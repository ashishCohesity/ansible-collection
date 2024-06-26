# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bridge/s3_portal/grpc_stub/s3_grpc_service.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from bridge.snap_fs import entity_handle_pb2 as bridge_dot_snap__fs_dot_entity__handle__pb2
from bridge.s3_portal.base import s3_error_pb2 as bridge_dot_s3__portal_dot_base_dot_s3__error__pb2
from magneto.object_walker import object_metadata_pb2 as magneto_dot_object__walker_dot_object__metadata__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0bridge/s3_portal/grpc_stub/s3_grpc_service.proto\x12\x1e\x63ohesity.bridge.s3_portal.stub\x1a\"bridge/snap_fs/entity_handle.proto\x1a$bridge/s3_portal/base/s3_error.proto\x1a+magneto/object_walker/object_metadata.proto\"\xa8\x01\n\x0f\x43reateObjectArg\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x13\n\x0b\x62ucket_name\x18\x02 \x01(\t\x12\x14\n\x0cis_mega_file\x18\x03 \x01(\x08\x12\x46\n\x0cobj_metadata\x18\x04 \x01(\x0b\x32\x30.cohesity.storage.object_metadata.ObjectMetadata\x12\x15\n\rsub_file_size\x18\x05 \x01(\x03\"\x84\x01\n\x12\x43reateObjectResult\x12=\n\tobject_eh\x18\x01 \x01(\x0b\x32*.cohesity.bridge.snap_fs.EntityHandleProto\x12/\n\x05\x65rror\x18\x02 \x01(\x0b\x32 .cohesity.bridge.s3.S3ErrorProto\"`\n\x11\x46inalizeObjectArg\x12=\n\tobject_eh\x18\x01 \x01(\x0b\x32*.cohesity.bridge.snap_fs.EntityHandleProto\x12\x0c\n\x04\x65tag\x18\x02 \x01(\t\"G\n\x14\x46inalizeObjectResult\x12/\n\x05\x65rror\x18\x01 \x01(\x0b\x32 .cohesity.bridge.s3.S3ErrorProto\"8\n\x14GetObjectVersionsArg\x12\x13\n\x0b\x62ucket_name\x18\x01 \x01(\t\x12\x0b\n\x03key\x18\x02 \x01(\t\"\xc1\x02\n\x17GetObjectVersionsResult\x12/\n\x05\x65rror\x18\x01 \x01(\x0b\x32 .cohesity.bridge.s3.S3ErrorProto\x12h\n\x0e\x65ntity_handles\x18\x02 \x03(\x0b\x32P.cohesity.bridge.s3_portal.stub.GetObjectVersionsResult.EntityHandleVersionTuple\x1a\x8a\x01\n\x18\x45ntityHandleVersionTuple\x12\x12\n\nversion_id\x18\x01 \x01(\x05\x12=\n\tobject_eh\x18\x02 \x01(\x0b\x32*.cohesity.bridge.snap_fs.EntityHandleProto\x12\x1b\n\x13\x65xternal_version_id\x18\x03 \x01(\t\"W\n\x16\x44\x65leteObjectVersionArg\x12\x13\n\x0b\x62ucket_name\x18\x01 \x01(\t\x12\x0b\n\x03key\x18\x02 \x01(\t\x12\x1b\n\x13\x65xternal_version_id\x18\x03 \x01(\t\"L\n\x19\x44\x65leteObjectVersionResult\x12/\n\x05\x65rror\x18\x01 \x01(\x0b\x32 .cohesity.bridge.s3.S3ErrorProto2\x9d\x04\n\x13S3PrivateRpcService\x12u\n\x0c\x43reateObject\x12/.cohesity.bridge.s3_portal.stub.CreateObjectArg\x1a\x32.cohesity.bridge.s3_portal.stub.CreateObjectResult\"\x00\x12{\n\x0e\x46inalizeObject\x12\x31.cohesity.bridge.s3_portal.stub.FinalizeObjectArg\x1a\x34.cohesity.bridge.s3_portal.stub.FinalizeObjectResult\"\x00\x12\x84\x01\n\x11GetObjectVersions\x12\x34.cohesity.bridge.s3_portal.stub.GetObjectVersionsArg\x1a\x37.cohesity.bridge.s3_portal.stub.GetObjectVersionsResult\"\x00\x12\x8a\x01\n\x13\x44\x65leteObjectVersion\x12\x36.cohesity.bridge.s3_portal.stub.DeleteObjectVersionArg\x1a\x39.cohesity.bridge.s3_portal.stub.DeleteObjectVersionResult\"\x00\x42\x03\x80\x01\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'bridge.s3_portal.grpc_stub.s3_grpc_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\200\001\000'
  _globals['_CREATEOBJECTARG']._serialized_start=204
  _globals['_CREATEOBJECTARG']._serialized_end=372
  _globals['_CREATEOBJECTRESULT']._serialized_start=375
  _globals['_CREATEOBJECTRESULT']._serialized_end=507
  _globals['_FINALIZEOBJECTARG']._serialized_start=509
  _globals['_FINALIZEOBJECTARG']._serialized_end=605
  _globals['_FINALIZEOBJECTRESULT']._serialized_start=607
  _globals['_FINALIZEOBJECTRESULT']._serialized_end=678
  _globals['_GETOBJECTVERSIONSARG']._serialized_start=680
  _globals['_GETOBJECTVERSIONSARG']._serialized_end=736
  _globals['_GETOBJECTVERSIONSRESULT']._serialized_start=739
  _globals['_GETOBJECTVERSIONSRESULT']._serialized_end=1060
  _globals['_GETOBJECTVERSIONSRESULT_ENTITYHANDLEVERSIONTUPLE']._serialized_start=922
  _globals['_GETOBJECTVERSIONSRESULT_ENTITYHANDLEVERSIONTUPLE']._serialized_end=1060
  _globals['_DELETEOBJECTVERSIONARG']._serialized_start=1062
  _globals['_DELETEOBJECTVERSIONARG']._serialized_end=1149
  _globals['_DELETEOBJECTVERSIONRESULT']._serialized_start=1151
  _globals['_DELETEOBJECTVERSIONRESULT']._serialized_end=1227
  _globals['_S3PRIVATERPCSERVICE']._serialized_start=1230
  _globals['_S3PRIVATERPCSERVICE']._serialized_end=1771
# @@protoc_insertion_point(module_scope)
