# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: helios/base/helios_audit_settings.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'helios/base/helios_audit_settings.proto\x12\x18\x63ohesity.helios.auditlog\"C\n\x19HeliosAuditLogUserSetting\x12\x10\n\x08user_sid\x18\x01 \x01(\t\x12\x14\n\x0cread_logging\x18\x02 \x01(\x08\"D\n\x19HeliosAuditLogRoleSetting\x12\x11\n\trole_name\x18\x01 \x01(\t\x12\x14\n\x0cread_logging\x18\x02 \x01(\x08\"\x83\x02\n\x1bHeliosAuditLogSettingsProto\x12J\n\ruser_settings\x18\x01 \x03(\x0b\x32\x33.cohesity.helios.auditlog.HeliosAuditLogUserSetting\x12\x14\n\x0cread_logging\x18\x02 \x01(\x08\x12J\n\rrole_settings\x18\x03 \x03(\x0b\x32\x33.cohesity.helios.auditlog.HeliosAuditLogRoleSetting\x12\"\n\x15retention_period_days\x18\x04 \x01(\x05:\x03\x31\x38\x30\x12\x12\n\naccount_id\x18\x05 \x01(\tB\x1aZ\x18\x63ohesity/helios/auditlog')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'helios.base.helios_audit_settings_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\030cohesity/helios/auditlog'
  _globals['_HELIOSAUDITLOGUSERSETTING']._serialized_start=69
  _globals['_HELIOSAUDITLOGUSERSETTING']._serialized_end=136
  _globals['_HELIOSAUDITLOGROLESETTING']._serialized_start=138
  _globals['_HELIOSAUDITLOGROLESETTING']._serialized_end=206
  _globals['_HELIOSAUDITLOGSETTINGSPROTO']._serialized_start=209
  _globals['_HELIOSAUDITLOGSETTINGSPROTO']._serialized_end=468
# @@protoc_insertion_point(module_scope)
