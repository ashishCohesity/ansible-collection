# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bridge/magneto/hyperv/hyperv_actions.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from bridge.magneto.base import magneto_actions_pb2 as bridge_dot_magneto_dot_base_dot_magneto__actions__pb2
from magneto.base.entities import hyperv_pb2 as magneto_dot_base_dot_entities_dot_hyperv__pb2
from magneto.connectors.hyperv import hyperv_pb2 as magneto_dot_connectors_dot_hyperv_dot_hyperv__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*bridge/magneto/hyperv/hyperv_actions.proto\x12\x1e\x63ohesity.bridge.magneto.hyperv\x1a)bridge/magneto/base/magneto_actions.proto\x1a\"magneto/base/entities/hyperv.proto\x1a&magneto/connectors/hyperv/hyperv.proto\"\xd6\x03\n\x11\x42\x61\x63kupHyperVVMArg\x12\x34\n\x04\x62\x61se\x18\x01 \x01(\x0b\x32&.cohesity.bridge.magneto.BackupBaseArg\x12\x44\n\x04type\x18\x02 \x01(\x0e\x32\x36.cohesity.bridge.magneto.hyperv.BackupHyperVVMArg.Type\x12\x34\n\x0broot_entity\x18\x03 \x01(\x0b\x32\x1f.cohesity.magneto.hyperv.Entity\x12\x32\n\tvm_entity\x18\x04 \x01(\x0b\x32\x1f.cohesity.magneto.hyperv.Entity\x12\x41\n\x10sparse_vm_config\x18\x05 \x01(\x0b\x32\'.cohesity.magneto.hyperv.SparseVMConfig\x12\x16\n\ncluster_id\x18\x06 \x01(\x03:\x02-1\x12\"\n\x16\x63luster_incarnation_id\x18\x07 \x01(\x03:\x02-1\"\\\n\x04Type\x12\x12\n\x0ekPrepareBackup\x10\x01\x12\x0f\n\x0bkSetupFiles\x10\x02\x12\x0f\n\x0bkBackupDisk\x10\x03\x12\x0e\n\nkCloseDisk\x10\x04\x12\x0e\n\nkEndBackup\x10\x05\"\xd3\x01\n\x13\x46\x65tchDiskMappingArg\x12\x16\n\x0ehead_filenames\x18\x01 \x03(\t\x12i\n\x14\x65ncoded_filepath_map\x18\x02 \x03(\x0b\x32K.cohesity.bridge.magneto.hyperv.FetchDiskMappingArg.EncodedFilepathMapEntry\x1a\x39\n\x17\x45ncodedFilepathMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x9e\x06\n\rRestoreVMsArg\x12@\n\x04type\x18\x01 \x01(\x0e\x32\x32.cohesity.bridge.magneto.hyperv.RestoreVMsArg.Type\x12U\n\x10vm_restore_infos\x18\x02 \x03(\x0b\x32;.cohesity.bridge.magneto.hyperv.RestoreVMsArg.VMRestoreInfo\x12\x13\n\x0bview_box_id\x18\x03 \x01(\x03\x12\x11\n\tview_name\x18\x04 \x01(\t\x12\x13\n\x0b\x63reate_view\x18\x05 \x01(\x08\x12\x1f\n\x10is_internal_view\x18\x07 \x01(\x08:\x05\x66\x61lse\x12\x13\n\x0bpath_prefix\x18\x08 \x01(\t\x12(\n\x1apreserve_original_dir_path\x18\n \x01(\x08:\x04true\x12&\n\x1eview_whitelist_ip_addr_str_vec\x18\t \x03(\t\x12S\n\x16\x66\x65tch_disk_mapping_arg\x18\x0b \x01(\x0b\x32\x33.cohesity.bridge.magneto.hyperv.FetchDiskMappingArg\x12\'\n\x18include_sparse_vm_config\x18\x0c \x01(\x08:\x05\x66\x61lse\x12-\n\x1euse_filenames_from_backup_view\x18\r \x01(\x08:\x05\x66\x61lse\x1a\xb0\x01\n\rVMRestoreInfo\x12\x11\n\tview_name\x18\x04 \x01(\t\x12\"\n\x1asnapshot_relative_dir_path\x18\x01 \x01(\t\x12\x32\n\tvm_entity\x18\x02 \x01(\x0b\x32\x1f.cohesity.magneto.hyperv.Entity\x12\x34\n\x0broot_entity\x18\x03 \x01(\x0b\x32\x1f.cohesity.magneto.hyperv.Entity\"O\n\x04Type\x12\r\n\tkCloneVMs\x10\x01\x12\x0e\n\nkDeleteVMs\x10\x02\x12\x15\n\x11kFetchDiskMapping\x10\x03\x12\x11\n\rkFetchVMsInfo\x10\x04\"\x8c\x03\n\x0fHyperVActionArg\x12\x0f\n\x07task_id\x18\x01 \x01(\x03\x12\x17\n\x0bsub_task_id\x18\x02 \x01(\x03:\x02-1\x12O\n\x14\x62\x61\x63kup_hyperv_vm_arg\x18\x03 \x01(\x0b\x32\x31.cohesity.bridge.magneto.hyperv.BackupHyperVVMArg\x12\x46\n\x0frestore_vms_arg\x18\x04 \x01(\x0b\x32-.cohesity.bridge.magneto.hyperv.RestoreVMsArg\x12?\n\x0f\x63\x61ncel_task_arg\x18\x05 \x01(\x0b\x32&.cohesity.bridge.magneto.CancelTaskArg2u\n\x11hyperv_action_arg\x12).cohesity.bridge.magneto.ExecuteActionArg\x18l \x01(\x0b\x32/.cohesity.bridge.magneto.hyperv.HyperVActionArg')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'bridge.magneto.hyperv.hyperv_actions_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_FETCHDISKMAPPINGARG_ENCODEDFILEPATHMAPENTRY']._loaded_options = None
  _globals['_FETCHDISKMAPPINGARG_ENCODEDFILEPATHMAPENTRY']._serialized_options = b'8\001'
  _globals['_BACKUPHYPERVVMARG']._serialized_start=198
  _globals['_BACKUPHYPERVVMARG']._serialized_end=668
  _globals['_BACKUPHYPERVVMARG_TYPE']._serialized_start=576
  _globals['_BACKUPHYPERVVMARG_TYPE']._serialized_end=668
  _globals['_FETCHDISKMAPPINGARG']._serialized_start=671
  _globals['_FETCHDISKMAPPINGARG']._serialized_end=882
  _globals['_FETCHDISKMAPPINGARG_ENCODEDFILEPATHMAPENTRY']._serialized_start=825
  _globals['_FETCHDISKMAPPINGARG_ENCODEDFILEPATHMAPENTRY']._serialized_end=882
  _globals['_RESTOREVMSARG']._serialized_start=885
  _globals['_RESTOREVMSARG']._serialized_end=1683
  _globals['_RESTOREVMSARG_VMRESTOREINFO']._serialized_start=1426
  _globals['_RESTOREVMSARG_VMRESTOREINFO']._serialized_end=1602
  _globals['_RESTOREVMSARG_TYPE']._serialized_start=1604
  _globals['_RESTOREVMSARG_TYPE']._serialized_end=1683
  _globals['_HYPERVACTIONARG']._serialized_start=1686
  _globals['_HYPERVACTIONARG']._serialized_end=2082
# @@protoc_insertion_point(module_scope)
