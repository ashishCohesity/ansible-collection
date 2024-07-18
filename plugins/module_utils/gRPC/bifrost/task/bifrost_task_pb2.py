# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bifrost/task/bifrost_task.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from bifrost.base import error_pb2 as bifrost_dot_base_dot_error__pb2
from bifrost.stub import bridge_auth_params_pb2 as bifrost_dot_stub_dot_bridge__auth__params__pb2
from bifrost.stub import magneto_connector_params_pb2 as bifrost_dot_stub_dot_magneto__connector__params__pb2
from magneto.base import api_version_pb2 as magneto_dot_base_dot_api__version__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1f\x62ifrost/task/bifrost_task.proto\x12\x15\x63ohesity.bifrost.task\x1a\x18\x62ifrost/base/error.proto\x1a%bifrost/stub/bridge_auth_params.proto\x1a+bifrost/stub/magneto_connector_params.proto\x1a\x1emagneto/base/api_version.proto\"\xc4\x01\n\x16\x42ifrostScheduleTaskArg\x12M\n\x0bsource_type\x18\x01 \x01(\x0e\x32\x38.cohesity.bifrost.task.BifrostScheduleTaskArg.SourceType\x12!\n\x15source_constituent_id\x18\x02 \x01(\x03:\x02-1\x12\x0f\n\x07task_id\x18\x03 \x01(\x03\"\'\n\nSourceType\x12\x0c\n\x08kMagneto\x10\x01\x12\x0b\n\x07kBridge\x10\x02\"8\n\x19\x42ifrostScheduleTaskResult\x12\x1b\n\x0f\x62ifrost_task_id\x18\x01 \x01(\x03\x42\x02\x18\x01\"\xce\x02\n\x14UpdateBifrostTaskArg\x12\x31\n\x0b\x61pi_version\x18\x01 \x01(\x0b\x32\x1c.cohesity.magneto.APIVersion\x12\x11\n\ttenant_id\x18\x02 \x01(\t\x12\x1e\n\x16\x62ifrost_constituent_id\x18\x03 \x01(\x03\x12\x1a\n\x12\x62ifrost_session_id\x18\x04 \x01(\x03\x12\x0f\n\x07task_id\x18\x05 \x01(\x03\x12W\n\x18magneto_connector_result\x18\x06 \x01(\x0b\x32\x35.cohesity.bifrost.stub.magneto.MagnetoConnectorResult\x12J\n\x12\x62ridge_auth_result\x18\x07 \x01(\x0b\x32..cohesity.bifrost.stub.bridge.BridgeAuthResult\"F\n\x17UpdateBifrostTaskResult\x12+\n\x05\x65rror\x18\x01 \x01(\x0b\x32\x1c.cohesity.bifrost.ErrorProto')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'bifrost.task.bifrost_task_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_BIFROSTSCHEDULETASKRESULT'].fields_by_name['bifrost_task_id']._loaded_options = None
  _globals['_BIFROSTSCHEDULETASKRESULT'].fields_by_name['bifrost_task_id']._serialized_options = b'\030\001'
  _globals['_BIFROSTSCHEDULETASKARG']._serialized_start=201
  _globals['_BIFROSTSCHEDULETASKARG']._serialized_end=397
  _globals['_BIFROSTSCHEDULETASKARG_SOURCETYPE']._serialized_start=358
  _globals['_BIFROSTSCHEDULETASKARG_SOURCETYPE']._serialized_end=397
  _globals['_BIFROSTSCHEDULETASKRESULT']._serialized_start=399
  _globals['_BIFROSTSCHEDULETASKRESULT']._serialized_end=455
  _globals['_UPDATEBIFROSTTASKARG']._serialized_start=458
  _globals['_UPDATEBIFROSTTASKARG']._serialized_end=792
  _globals['_UPDATEBIFROSTTASKRESULT']._serialized_start=794
  _globals['_UPDATEBIFROSTTASKRESULT']._serialized_end=864
# @@protoc_insertion_point(module_scope)