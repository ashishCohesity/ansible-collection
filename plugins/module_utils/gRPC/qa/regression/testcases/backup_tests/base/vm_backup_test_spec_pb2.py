# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: qa/regression/testcases/backup_tests/base/vm_backup_test_spec.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nCqa/regression/testcases/backup_tests/base/vm_backup_test_spec.proto\x12\x1a\x63ohesity.qa.vm_backup_test\"G\n\x13VcenterBackupSource\x12\x0c\n\x04host\x18\x01 \x02(\t\x12\x10\n\x08username\x18\x02 \x02(\t\x12\x10\n\x08password\x18\x03 \x02(\t\"\xf3\x01\n\x0cVmBackupInfo\x12\x10\n\x08job_name\x18\x01 \x02(\t\x12\x15\n\rview_box_name\x18\x02 \x02(\t\x12I\n\x10vc_backup_source\x18\x03 \x02(\x0b\x32/.cohesity.qa.vm_backup_test.VcenterBackupSource\x12\x11\n\tvm_morefs\x18\x04 \x03(\t\x12/\n\rjob_policy_id\x18\x05 \x02(\t:\x18TEMPLATE_COHESITY_SILVER\x12\x16\n\x08indexing\x18\x06 \x02(\x08:\x04true\x12\x13\n\x0bjob_timeout\x18\x07 \x02(\x05\x42\x42Z@qa/regression/testcases/backup_tests/base/vm_backup_test_spec.pb')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'qa.regression.testcases.backup_tests.base.vm_backup_test_spec_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z@qa/regression/testcases/backup_tests/base/vm_backup_test_spec.pb'
  _globals['_VCENTERBACKUPSOURCE']._serialized_start=99
  _globals['_VCENTERBACKUPSOURCE']._serialized_end=170
  _globals['_VMBACKUPINFO']._serialized_start=173
  _globals['_VMBACKUPINFO']._serialized_end=416
# @@protoc_insertion_point(module_scope)