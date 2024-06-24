# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: magneto/v2/policy_manager/policy_external.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from magneto.api import magneto_external_base_pb2 as magneto_dot_api_dot_magneto__external__base__pb2
from magneto.base import error_pb2 as magneto_dot_base_dot_error__pb2
from magneto.base import policy_pb2 as magneto_dot_base_dot_policy__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/magneto/v2/policy_manager/policy_external.proto\x12\x1b\x63ohesity.magneto.api.policy\x1a\'magneto/api/magneto_external_base.proto\x1a\x18magneto/base/error.proto\x1a\x19magneto/base/policy.proto\"\x8a\x01\n\x19\x43reateOrUpdatePoliciesArg\x12\x30\n\x04\x62\x61se\x18\x01 \x01(\x0b\x32\".cohesity.magneto.api.ArgumentBase\x12;\n\npolicy_vec\x18\x02 \x03(\x0b\x32\'.cohesity.magneto.ProtectionPolicyProto\"\xf2\x01\n\x1c\x43reateOrUpdatePoliciesResult\x12.\n\x04\x62\x61se\x18\x01 \x01(\x0b\x32 .cohesity.magneto.api.ResultBase\x12T\n\nresult_vec\x18\x02 \x03(\x0b\x32@.cohesity.magneto.api.policy.CreateOrUpdatePoliciesResult.Result\x1aL\n\x06Result\x12\x11\n\tpolicy_id\x18\x01 \x01(\t\x12/\n\x05\x65rror\x18\x02 \x01(\x0b\x32 .cohesity.magneto.api.ErrorProto\"[\n\x10\x46\x65tchPoliciesArg\x12\x30\n\x04\x62\x61se\x18\x01 \x01(\x0b\x32\".cohesity.magneto.api.ArgumentBase\x12\x15\n\rpolicy_id_vec\x18\x02 \x03(\t\"\x86\x02\n\x13\x46\x65tchPoliciesResult\x12.\n\x04\x62\x61se\x18\x01 \x01(\x0b\x32 .cohesity.magneto.api.ResultBase\x12K\n\nresult_vec\x18\x02 \x03(\x0b\x32\x37.cohesity.magneto.api.policy.FetchPoliciesResult.Result\x1ar\n\x06Result\x12\x37\n\x06policy\x18\x01 \x01(\x0b\x32\'.cohesity.magneto.ProtectionPolicyProto\x12/\n\x05\x65rror\x18\x02 \x01(\x0b\x32 .cohesity.magneto.api.ErrorProtoB\x1dZ\x1b\x63ohesity/magneto/api/policy')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'magneto.v2.policy_manager.policy_external_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\033cohesity/magneto/api/policy'
  _globals['_CREATEORUPDATEPOLICIESARG']._serialized_start=175
  _globals['_CREATEORUPDATEPOLICIESARG']._serialized_end=313
  _globals['_CREATEORUPDATEPOLICIESRESULT']._serialized_start=316
  _globals['_CREATEORUPDATEPOLICIESRESULT']._serialized_end=558
  _globals['_CREATEORUPDATEPOLICIESRESULT_RESULT']._serialized_start=482
  _globals['_CREATEORUPDATEPOLICIESRESULT_RESULT']._serialized_end=558
  _globals['_FETCHPOLICIESARG']._serialized_start=560
  _globals['_FETCHPOLICIESARG']._serialized_end=651
  _globals['_FETCHPOLICIESRESULT']._serialized_start=654
  _globals['_FETCHPOLICIESRESULT']._serialized_end=916
  _globals['_FETCHPOLICIESRESULT_RESULT']._serialized_start=802
  _globals['_FETCHPOLICIESRESULT_RESULT']._serialized_end=916
# @@protoc_insertion_point(module_scope)
