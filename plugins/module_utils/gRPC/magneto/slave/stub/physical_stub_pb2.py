# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: magneto/slave/stub/physical_stub.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from magneto.base.entities import physical_pb2 as magneto_dot_base_dot_entities_dot_physical__pb2
from magneto.base import physical_pb2 as magneto_dot_base_dot_physical__pb2
from magneto.slave.stub import stub_pb2 as magneto_dot_slave_dot_stub_dot_stub__pb2
from magneto.slave.stub import bridge_updates_pb2 as magneto_dot_slave_dot_stub_dot_bridge__updates__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&magneto/slave/stub/physical_stub.proto\x12$cohesity.magneto.slave.stub.physical\x1a$magneto/base/entities/physical.proto\x1a\x1bmagneto/base/physical.proto\x1a\x1dmagneto/slave/stub/stub.proto\x1a\'magneto/slave/stub/bridge_updates.proto\"o\n\x16PrepareBackupUpdateArg\x12\x15\n\troot_path\x18\x01 \x01(\tB\x02\x18\x01\x12!\n\x15relative_snapshot_dir\x18\x02 \x01(\tB\x02\x18\x01\x12\x1b\n\x13\x61ncillary_view_name\x18\x03 \x01(\t\"\xbc\x01\n\x13SetupFilesUpdateArg\x12=\n\rvirtual_disks\x18\x01 \x03(\x0b\x32&.cohesity.magneto.physical.VirtualDisk\x12,\n$virtual_disk_filepaths_to_be_deleted\x18\x02 \x03(\t\x12\x15\n\troot_path\x18\x03 \x01(\tB\x02\x18\x01\x12!\n\x15relative_snapshot_dir\x18\x04 \x01(\tB\x02\x18\x01\"\x9b\x02\n\x13\x43loneHostsUpdateArg\x12Z\n\x0c\x63loned_hosts\x18\x01 \x03(\x0b\x32\x44.cohesity.magneto.slave.stub.physical.CloneHostsUpdateArg.ClonedHost\x1a\xa7\x01\n\nClonedHost\x12\x31\n\x06\x65ntity\x18\x01 \x01(\x0b\x32!.cohesity.magneto.physical.Entity\x12G\n\x12sparse_host_config\x18\x02 \x01(\x0b\x32+.cohesity.magneto.physical.SparseHostConfig\x12\x1d\n\x15relative_cloned_paths\x18\x03 \x03(\t\"\xec\x06\n\x0f\x41\x63tionUpdateArg\x12H\n\x04type\x18\x01 \x01(\x0e\x32:.cohesity.magneto.slave.stub.physical.ActionUpdateArg.Type\x12_\n\x19prepare_backup_update_arg\x18\x05 \x01(\x0b\x32<.cohesity.magneto.slave.stub.physical.PrepareBackupUpdateArg\x12P\n\x16\x62\x61\x63kup_disk_update_arg\x18\x02 \x01(\x0b\x32\x30.cohesity.magneto.slave.stub.BackupDiskUpdateArg\x12Y\n\x16setup_files_update_arg\x18\x03 \x01(\x0b\x32\x39.cohesity.magneto.slave.stub.physical.SetupFilesUpdateArg\x12Y\n\x16\x63lone_hosts_update_arg\x18\x04 \x01(\x0b\x32\x39.cohesity.magneto.slave.stub.physical.CloneHostsUpdateArg\x12R\n\x17restore_disk_update_arg\x18\x06 \x01(\x0b\x32\x31.cohesity.magneto.slave.stub.RestoreDiskUpdateArg\"\xc7\x01\n\x04Type\x12\x18\n\x14kPrepareBackupUpdate\x10\x01\x12\x15\n\x11kSetupFilesUpdate\x10\x02\x12\x15\n\x11kBackupDiskUpdate\x10\x03\x12\x14\n\x10kCloseDiskUpdate\x10\x04\x12\x14\n\x10kEndBackupUpdate\x10\x05\x12\x15\n\x11kCloneHostsUpdate\x10\x06\x12\x1c\n\x18kDeleteClonedHostsUpdate\x10\x07\x12\x16\n\x12kRestoreDiskUpdate\x10\x08\x32\x87\x01\n\x1aphysical_action_update_arg\x12,.cohesity.magneto.slave.stub.ActionUpdateArg\x18g \x01(\x0b\x32\x35.cohesity.magneto.slave.stub.physical.ActionUpdateArg')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'magneto.slave.stub.physical_stub_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_PREPAREBACKUPUPDATEARG'].fields_by_name['root_path']._loaded_options = None
  _globals['_PREPAREBACKUPUPDATEARG'].fields_by_name['root_path']._serialized_options = b'\030\001'
  _globals['_PREPAREBACKUPUPDATEARG'].fields_by_name['relative_snapshot_dir']._loaded_options = None
  _globals['_PREPAREBACKUPUPDATEARG'].fields_by_name['relative_snapshot_dir']._serialized_options = b'\030\001'
  _globals['_SETUPFILESUPDATEARG'].fields_by_name['root_path']._loaded_options = None
  _globals['_SETUPFILESUPDATEARG'].fields_by_name['root_path']._serialized_options = b'\030\001'
  _globals['_SETUPFILESUPDATEARG'].fields_by_name['relative_snapshot_dir']._loaded_options = None
  _globals['_SETUPFILESUPDATEARG'].fields_by_name['relative_snapshot_dir']._serialized_options = b'\030\001'
  _globals['_PREPAREBACKUPUPDATEARG']._serialized_start=219
  _globals['_PREPAREBACKUPUPDATEARG']._serialized_end=330
  _globals['_SETUPFILESUPDATEARG']._serialized_start=333
  _globals['_SETUPFILESUPDATEARG']._serialized_end=521
  _globals['_CLONEHOSTSUPDATEARG']._serialized_start=524
  _globals['_CLONEHOSTSUPDATEARG']._serialized_end=807
  _globals['_CLONEHOSTSUPDATEARG_CLONEDHOST']._serialized_start=640
  _globals['_CLONEHOSTSUPDATEARG_CLONEDHOST']._serialized_end=807
  _globals['_ACTIONUPDATEARG']._serialized_start=810
  _globals['_ACTIONUPDATEARG']._serialized_end=1686
  _globals['_ACTIONUPDATEARG_TYPE']._serialized_start=1349
  _globals['_ACTIONUPDATEARG_TYPE']._serialized_end=1548
# @@protoc_insertion_point(module_scope)