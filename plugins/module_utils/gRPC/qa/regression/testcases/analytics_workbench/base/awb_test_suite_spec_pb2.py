# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: qa/regression/testcases/analytics_workbench/base/awb_test_suite_spec.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from qa.regression.testcases.backup_tests.base import vm_backup_test_spec_pb2 as qa_dot_regression_dot_testcases_dot_backup__tests_dot_base_dot_vm__backup__test__spec__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nJqa/regression/testcases/analytics_workbench/base/awb_test_suite_spec.proto\x12\x15\x63ohesity.qa.awb_suite\x1a\x43qa/regression/testcases/backup_tests/base/vm_backup_test_spec.proto\"@\n\x18\x46ileLastModifiedTestInfo\x12\x12\n\nstart_time\x18\x01 \x02(\x03\x12\x10\n\x08\x65nd_time\x18\x02 \x02(\x03\"\xa9\x02\n\x16\x46ilesOnServersTestInfo\x12\x11\n\tjob_names\x18\x01 \x03(\t\x12\x12\n\nview_boxes\x18\x02 \x03(\t\x12\x0f\n\x07servers\x18\x03 \x03(\t\x12\x12\n\nfile_types\x18\x04 \x03(\t\x12\x0c\n\x04path\x18\x05 \x01(\t\x12\x17\n\x0flatest_snapshot\x18\x06 \x02(\x08\x12U\n\x1c\x66ile_last_modified_test_data\x18\x07 \x01(\x0b\x32/.cohesity.qa.awb_suite.FileLastModifiedTestInfo\x12\x45\n\x13vm_backup_test_data\x18\x08 \x01(\x0b\x32(.cohesity.qa.vm_backup_test.VmBackupInfo\"\xc1\x01\n\x13\x46ilesOnViewTestInfo\x12\x10\n\x08view_box\x18\x01 \x02(\t\x12\x0c\n\x04view\x18\x02 \x02(\t\x12\x12\n\nfile_types\x18\x03 \x03(\t\x12\x0c\n\x04path\x18\x04 \x01(\t\x12U\n\x1c\x66ile_last_modified_test_data\x18\x05 \x01(\x0b\x32/.cohesity.qa.awb_suite.FileLastModifiedTestInfo\x12\x11\n\tfile_urls\x18\x06 \x03(\t\"\x8e\x02\n\x15PatternFinderTestInfo\x12\x0e\n\x06on_nfs\x18\x01 \x02(\x08\x12Q\n\x1a\x66iles_on_servers_test_data\x18\x02 \x01(\x0b\x32-.cohesity.qa.awb_suite.FilesOnServersTestInfo\x12K\n\x17\x66iles_on_view_test_data\x18\x03 \x01(\x0b\x32*.cohesity.qa.awb_suite.FilesOnViewTestInfo\x12\x16\n\x0esearch_pattern\x18\x04 \x02(\t\x12\x18\n\x10results_location\x18\x05 \x02(\t\x12\x13\n\x0bjob_timeout\x18\x06 \x02(\x05\"\xe4\x02\n\x17VideoCompressorTestInfo\x12\x10\n\x08view_box\x18\x01 \x02(\t\x12\x0c\n\x04view\x18\x02 \x02(\t\x12\x11\n\textension\x18\x03 \x02(\t\x12\x13\n\x0bvideo_codec\x18\x04 \x02(\t\x12\x13\n\x0b\x61udio_codec\x18\x05 \x02(\t\x12\x12\n\nresolution\x18\x06 \x01(\t\x12\x18\n\x10output_extension\x18\x07 \x02(\t\x12\x12\n\nfile_types\x18\x08 \x03(\t\x12\x0c\n\x04path\x18\t \x01(\t\x12U\n\x1c\x66ile_last_modified_test_data\x18\n \x01(\x0b\x32/.cohesity.qa.awb_suite.FileLastModifiedTestInfo\x12\x18\n\x10results_location\x18\x0b \x02(\t\x12\x13\n\x0bjob_timeout\x18\x0c \x02(\x05\x12\x16\n\x0evideo_file_url\x18\r \x02(\t\"\xba\x01\n\x0c\x41wbTestInfos\x12R\n\x1cpattern_finder_test_data_vec\x18\x01 \x03(\x0b\x32,.cohesity.qa.awb_suite.PatternFinderTestInfo\x12V\n\x1evideo_compressor_test_data_vec\x18\x02 \x03(\x0b\x32..cohesity.qa.awb_suite.VideoCompressorTestInfoBIZGqa/regression/testcases/analytics_workbench/base/awb_test_suite_spec.pb')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'qa.regression.testcases.analytics_workbench.base.awb_test_suite_spec_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'ZGqa/regression/testcases/analytics_workbench/base/awb_test_suite_spec.pb'
  _globals['_FILELASTMODIFIEDTESTINFO']._serialized_start=170
  _globals['_FILELASTMODIFIEDTESTINFO']._serialized_end=234
  _globals['_FILESONSERVERSTESTINFO']._serialized_start=237
  _globals['_FILESONSERVERSTESTINFO']._serialized_end=534
  _globals['_FILESONVIEWTESTINFO']._serialized_start=537
  _globals['_FILESONVIEWTESTINFO']._serialized_end=730
  _globals['_PATTERNFINDERTESTINFO']._serialized_start=733
  _globals['_PATTERNFINDERTESTINFO']._serialized_end=1003
  _globals['_VIDEOCOMPRESSORTESTINFO']._serialized_start=1006
  _globals['_VIDEOCOMPRESSORTESTINFO']._serialized_end=1362
  _globals['_AWBTESTINFOS']._serialized_start=1365
  _globals['_AWBTESTINFOS']._serialized_end=1551
# @@protoc_insertion_point(module_scope)
