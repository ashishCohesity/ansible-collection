# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: magneto/slave/stub/san_stub.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from magneto.base import disk_pb2 as magneto_dot_base_dot_disk__pb2
from magneto.slave.stub import stub_pb2 as magneto_dot_slave_dot_stub_dot_stub__pb2
from magneto.slave.stub import bridge_updates_pb2 as magneto_dot_slave_dot_stub_dot_bridge__updates__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!magneto/slave/stub/san_stub.proto\x12\x1f\x63ohesity.magneto.slave.stub.san\x1a\x17magneto/base/disk.proto\x1a\x1dmagneto/slave/stub/stub.proto\x1a\'magneto/slave/stub/bridge_updates.proto\"O\n\x13SetupFilesUpdateArg\x12\x15\n\troot_path\x18\x01 \x01(\tB\x02\x18\x01\x12!\n\x15relative_snapshot_dir\x18\x02 \x01(\tB\x02\x18\x01\"\x80\x01\n\x16\x46\x65tchDiskInfoUpdateArg\x12)\n\x04\x64isk\x18\x01 \x01(\x0b\x32\x1b.cohesity.magneto.DiskProto\x12;\n\x0e\x64isk_area_list\x18\x02 \x01(\x0b\x32#.cohesity.magneto.DiskAreaListProto\"\xa8\x06\n\x12SanActionUpdateArg\x12\x46\n\x04type\x18\x01 \x01(\x0e\x32\x38.cohesity.magneto.slave.stub.san.SanActionUpdateArg.Type\x12T\n\x16setup_files_update_arg\x18\x02 \x01(\x0b\x32\x34.cohesity.magneto.slave.stub.san.SetupFilesUpdateArg\x12U\n\x1b\x62\x61\x63kup_disk_area_update_arg\x18\x03 \x01(\x0b\x32\x30.cohesity.magneto.slave.stub.BackupDiskUpdateArg\x12W\n\x1crestore_disk_area_update_arg\x18\x04 \x01(\x0b\x32\x31.cohesity.magneto.slave.stub.RestoreDiskUpdateArg\x12[\n\x1a\x66\x65tch_disk_info_update_arg\x18\x05 \x01(\x0b\x32\x37.cohesity.magneto.slave.stub.san.FetchDiskInfoUpdateArg\"\xe3\x01\n\x04Type\x12\x18\n\x14kPrepareBackupUpdate\x10\x01\x12\x15\n\x11kSetupFilesUpdate\x10\x02\x12\x19\n\x15kBackupDiskAreaUpdate\x10\x03\x12\x15\n\x11kEndSubTaskUpdate\x10\x04\x12\x14\n\x10kEndBackupUpdate\x10\x05\x12\x15\n\x11kCloneFilesUpdate\x10\x06\x12\x18\n\x14kFetchDiskInfoUpdate\x10\x07\x12\x1a\n\x16kRestoreDiskAreaUpdate\x10\x08\x12\x15\n\x11kEndRestoreUpdate\x10\t2\x80\x01\n\x15san_action_update_arg\x12,.cohesity.magneto.slave.stub.ActionUpdateArg\x18h \x01(\x0b\x32\x33.cohesity.magneto.slave.stub.san.SanActionUpdateArg')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'magneto.slave.stub.san_stub_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_SETUPFILESUPDATEARG'].fields_by_name['root_path']._loaded_options = None
  _globals['_SETUPFILESUPDATEARG'].fields_by_name['root_path']._serialized_options = b'\030\001'
  _globals['_SETUPFILESUPDATEARG'].fields_by_name['relative_snapshot_dir']._loaded_options = None
  _globals['_SETUPFILESUPDATEARG'].fields_by_name['relative_snapshot_dir']._serialized_options = b'\030\001'
  _globals['_SETUPFILESUPDATEARG']._serialized_start=167
  _globals['_SETUPFILESUPDATEARG']._serialized_end=246
  _globals['_FETCHDISKINFOUPDATEARG']._serialized_start=249
  _globals['_FETCHDISKINFOUPDATEARG']._serialized_end=377
  _globals['_SANACTIONUPDATEARG']._serialized_start=380
  _globals['_SANACTIONUPDATEARG']._serialized_end=1188
  _globals['_SANACTIONUPDATEARG_TYPE']._serialized_start=830
  _globals['_SANACTIONUPDATEARG_TYPE']._serialized_end=1057
# @@protoc_insertion_point(module_scope)
