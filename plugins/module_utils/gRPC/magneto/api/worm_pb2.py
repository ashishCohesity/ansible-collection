# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: magneto/api/worm.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16magneto/api/worm.proto\x12\x14\x63ohesity.magneto.api\"\xfd\x01\n\x12WormRetentionProto\x12S\n\x0bpolicy_type\x18\x01 \x01(\x0e\x32\x37.cohesity.magneto.api.WormRetentionProto.WormPolicyType:\x05kNone\x12\x16\n\x0eretention_secs\x18\x02 \x01(\x03\x12\x0f\n\x07version\x18\x03 \x01(\x05\x12&\n\x1e\x65nable_worm_on_external_target\x18\x04 \x01(\x08\"A\n\x0eWormPolicyType\x12\t\n\x05kNone\x10\x00\x12\x0f\n\x0bkCompliance\x10\x01\x12\x13\n\x0fkAdministrative\x10\x02\"\x86\x02\n\x15\x41rchiveWORMProperties\x12!\n\x19is_archive_worm_compliant\x18\x01 \x01(\x08\x12*\n\"archive_worm_non_compliance_reason\x18\x02 \x01(\t\x12\x1e\n\x16worm_expiry_time_usecs\x18\x03 \x01(\x03\x12\x30\n(external_target_data_lock_retention_secs\x18\x04 \x01(\x03\x12L\n\x0bpolicy_type\x18\x05 \x01(\x0e\x32\x37.cohesity.magneto.api.WormRetentionProto.WormPolicyType\"\xb0\x01\n\x18\x44\x61taLockConstraintsProto\x12L\n\x0bpolicy_type\x18\x01 \x01(\x0e\x32\x37.cohesity.magneto.api.WormRetentionProto.WormPolicyType\x12\x1e\n\x16\x64\x61ta_lock_expiry_usecs\x18\x02 \x01(\x03\x12&\n\x1e\x65nable_worm_on_external_target\x18\x03 \x01(\x08\x42\x16Z\x14\x63ohesity/magneto/api')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'magneto.api.worm_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\024cohesity/magneto/api'
  _globals['_WORMRETENTIONPROTO']._serialized_start=49
  _globals['_WORMRETENTIONPROTO']._serialized_end=302
  _globals['_WORMRETENTIONPROTO_WORMPOLICYTYPE']._serialized_start=237
  _globals['_WORMRETENTIONPROTO_WORMPOLICYTYPE']._serialized_end=302
  _globals['_ARCHIVEWORMPROPERTIES']._serialized_start=305
  _globals['_ARCHIVEWORMPROPERTIES']._serialized_end=567
  _globals['_DATALOCKCONSTRAINTSPROTO']._serialized_start=570
  _globals['_DATALOCKCONSTRAINTSPROTO']._serialized_end=746
# @@protoc_insertion_point(module_scope)