# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: qa/environment/base/environment.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from qa.environment.base import common_pb2 as qa_dot_environment_dot_base_dot_common__pb2
from qa.environment.base import cohesity_pb2 as qa_dot_environment_dot_base_dot_cohesity__pb2
from qa.environment.base import vmware_pb2 as qa_dot_environment_dot_base_dot_vmware__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%qa/environment/base/environment.proto\x12\x17\x63ohesity.qa.environment\x1a qa/environment/base/common.proto\x1a\"qa/environment/base/cohesity.proto\x1a qa/environment/base/vmware.proto\"\xbe\x03\n\x0fTestEnvironment\x12\x33\n\x08node_vec\x18\x01 \x03(\x0b\x32!.cohesity.qa.environment.NodeInfo\x12<\n\x0elogin_info_vec\x18\x02 \x03(\x0b\x32$.cohesity.qa.environment.Credentials\x12K\n\x14\x63ohesity_version_vec\x18\x03 \x03(\x0b\x32-.cohesity.qa.environment.CohesitySoftwareInfo\x12\x39\n\x0bvcenter_vec\x18\x04 \x03(\x0b\x32$.cohesity.qa.environment.VCenterInfo\x12?\n\x11vm_setup_info_vec\x18\x05 \x03(\x0b\x32$.cohesity.qa.environment.VMSetupInfo\x12\x34\n\x07ps_host\x18\x06 \x01(\x0b\x32#.cohesity.qa.environment.PSHostInfo\x12\x39\n\x0b\x63luster_vec\x18\x07 \x03(\x0b\x32$.cohesity.qa.environment.ClusterInfoB$Z\"qa/environment/base/environment.pb')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'qa.environment.base.environment_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\"qa/environment/base/environment.pb'
  _globals['_TESTENVIRONMENT']._serialized_start=171
  _globals['_TESTENVIRONMENT']._serialized_end=617
# @@protoc_insertion_point(module_scope)
