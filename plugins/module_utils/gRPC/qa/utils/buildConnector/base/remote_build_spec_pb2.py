# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: qa/utils/buildConnector/base/remote_build_spec.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4qa/utils/buildConnector/base/remote_build_spec.proto\x12\x1b\x63ohesity.qa.build_connector\"M\n\x11ServerCredentials\x12\x1a\n\x08username\x18\x01 \x02(\t:\x08\x63ohesity\x12\x1c\n\x08password\x18\x02 \x02(\t:\nFr8shst8rt\"o\n\x16ServerConnectionParams\x12\x10\n\x08\x65ndpoint\x18\x01 \x02(\t\x12\x43\n\x0bserver_cred\x18\x02 \x02(\x0b\x32..cohesity.qa.build_connector.ServerCredentials\"j\n\x0b\x42uildServer\x12\x43\n\x06server\x18\x01 \x02(\x0b\x32\x33.cohesity.qa.build_connector.ServerConnectionParams\x12\x16\n\x0eworkspace_path\x18\x02 \x02(\t\"_\n\x12RemoteBuildServers\x12I\n\x17remote_build_server_vec\x18\x01 \x03(\x0b\x32(.cohesity.qa.build_connector.BuildServer\"C\n\x0bNVParamType\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\r\n\x05value\x18\x02 \x02(\t\x12\x17\n\x0fprefix_abs_path\x18\x03 \x02(\x08\"\x1f\n\x0fSingleParamType\x12\x0c\n\x04name\x18\x01 \x02(\t\"\x99\x01\n\nBuildParam\x12?\n\x07s_param\x18\x01 \x01(\x0b\x32,.cohesity.qa.build_connector.SingleParamTypeH\x00\x12<\n\x08nv_param\x18\x02 \x01(\x0b\x32(.cohesity.qa.build_connector.NVParamTypeH\x00\x42\x0c\n\nparam_type\"\x8d\x01\n\x0b\x42uildParams\x12:\n\tbld_param\x18\x01 \x03(\x0b\x32\'.cohesity.qa.build_connector.BuildParam\x12\x13\n\x0bscript_path\x18\x02 \x02(\t\x12\x0f\n\x07timeout\x18\x03 \x02(\x05\x12\x1c\n\noutput_dir\x18\x04 \x02(\t:\x08\x61rtifactB3Z1qa/utils/buildConnector/base/remote_build_spec.pb')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'qa.utils.buildConnector.base.remote_build_spec_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z1qa/utils/buildConnector/base/remote_build_spec.pb'
  _globals['_SERVERCREDENTIALS']._serialized_start=85
  _globals['_SERVERCREDENTIALS']._serialized_end=162
  _globals['_SERVERCONNECTIONPARAMS']._serialized_start=164
  _globals['_SERVERCONNECTIONPARAMS']._serialized_end=275
  _globals['_BUILDSERVER']._serialized_start=277
  _globals['_BUILDSERVER']._serialized_end=383
  _globals['_REMOTEBUILDSERVERS']._serialized_start=385
  _globals['_REMOTEBUILDSERVERS']._serialized_end=480
  _globals['_NVPARAMTYPE']._serialized_start=482
  _globals['_NVPARAMTYPE']._serialized_end=549
  _globals['_SINGLEPARAMTYPE']._serialized_start=551
  _globals['_SINGLEPARAMTYPE']._serialized_end=582
  _globals['_BUILDPARAM']._serialized_start=585
  _globals['_BUILDPARAM']._serialized_end=738
  _globals['_BUILDPARAMS']._serialized_start=741
  _globals['_BUILDPARAMS']._serialized_end=882
# @@protoc_insertion_point(module_scope)
