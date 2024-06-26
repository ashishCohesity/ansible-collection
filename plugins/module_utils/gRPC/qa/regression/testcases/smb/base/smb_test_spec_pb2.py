# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: qa/regression/testcases/smb/base/smb_test_spec.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4qa/regression/testcases/smb/base/smb_test_spec.proto\x12\x14\x63ohesity.qa.smb_test\"\xf0\x02\n\tTestSetup\x12\x15\n\rscripts_share\x18\x01 \x02(\t\x12\x13\n\x0bscripts_dir\x18\x02 \x01(\t\x12\x13\n\x0bmount_drive\x18\x03 \x01(\t\x12\x1a\n\x12script_backup_4vip\x18\x04 \x01(\t\x12\x1c\n\x14script_invoke_backup\x18\x05 \x01(\t\x12\x17\n\x0frestore_default\x18\x06 \x01(\t\x12\x14\n\x0ctshark_drive\x18\x07 \x01(\t\x12\x1d\n\x15script_purge_kerberos\x18\x08 \x01(\t\x12\x1e\n\x16script_create_database\x18\t \x01(\t\x12\x19\n\x11\x64\x62_load_data_file\x18\n \x01(\t\x12\x15\n\rdb_size_in_gb\x18\x0b \x01(\t\x12\x19\n\x11\x64\x62_name_to_create\x18\x0c \x01(\t\x12\x17\n\x0f\x64\x62_restore_path\x18\r \x01(\t\x12\x14\n\x0crestore_move\x18\x0e \x01(\t\"8\n\x12WindowsCredentials\x12\x10\n\x08username\x18\x01 \x02(\t\x12\x10\n\x08password\x18\x02 \x02(\t\"\x98\x01\n\x07SqlInfo\x12\x10\n\x08username\x18\x01 \x02(\t\x12\x10\n\x08password\x18\x02 \x02(\t\x12\x13\n\x0bmount_drive\x18\x03 \x02(\t\x12\x14\n\x0csql_instance\x18\x04 \x02(\t\x12\x14\n\x0csql_small_db\x18\x05 \x01(\t\x12\x14\n\x0csql_large_db\x18\x06 \x01(\t\x12\x12\n\nsql_mid_db\x18\x07 \x01(\t\"T\n\x10LogCollectorInfo\x12\x14\n\x0ctarget_share\x18\x01 \x01(\t\x12\x13\n\x0bmount_drive\x18\x02 \x01(\t\x12\x15\n\rsql_logs_path\x18\x03 \x01(\t\"\x92\x01\n\x07SmbHost\x12\x39\n\thost_type\x18\x01 \x02(\x0e\x32&.cohesity.qa.smb_test.SmbHost.HostType\x12\x11\n\thost_name\x18\x02 \x02(\t\x12\x0f\n\x07host_ip\x18\x03 \x02(\t\"(\n\x08HostType\x12\r\n\tWIN2012R2\x10\x00\x12\r\n\tWIN2008R2\x10\x01\"\xb6\x02\n\x0eSmbTestServers\x12\x33\n\ntest_setup\x18\x01 \x01(\x0b\x32\x1f.cohesity.qa.smb_test.TestSetup\x12\x45\n\x13windows_credentials\x18\x02 \x02(\x0b\x32(.cohesity.qa.smb_test.WindowsCredentials\x12/\n\x08sql_info\x18\x03 \x02(\x0b\x32\x1d.cohesity.qa.smb_test.SqlInfo\x12\x42\n\x12log_collector_info\x18\x04 \x01(\x0b\x32&.cohesity.qa.smb_test.LogCollectorInfo\x12\x33\n\x0csmb_host_vec\x18\x05 \x03(\x0b\x32\x1d.cohesity.qa.smb_test.SmbHostB3Z1qa/regression/testcases/smb/base/smb_test_spec.pb')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'qa.regression.testcases.smb.base.smb_test_spec_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z1qa/regression/testcases/smb/base/smb_test_spec.pb'
  _globals['_TESTSETUP']._serialized_start=79
  _globals['_TESTSETUP']._serialized_end=447
  _globals['_WINDOWSCREDENTIALS']._serialized_start=449
  _globals['_WINDOWSCREDENTIALS']._serialized_end=505
  _globals['_SQLINFO']._serialized_start=508
  _globals['_SQLINFO']._serialized_end=660
  _globals['_LOGCOLLECTORINFO']._serialized_start=662
  _globals['_LOGCOLLECTORINFO']._serialized_end=746
  _globals['_SMBHOST']._serialized_start=749
  _globals['_SMBHOST']._serialized_end=895
  _globals['_SMBHOST_HOSTTYPE']._serialized_start=855
  _globals['_SMBHOST_HOSTTYPE']._serialized_end=895
  _globals['_SMBTESTSERVERS']._serialized_start=898
  _globals['_SMBTESTSERVERS']._serialized_end=1208
# @@protoc_insertion_point(module_scope)
