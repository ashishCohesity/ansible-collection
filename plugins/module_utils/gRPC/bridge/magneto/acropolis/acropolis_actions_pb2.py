# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bridge/magneto/acropolis/acropolis_actions.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from bridge.magneto.base import magneto_actions_pb2 as bridge_dot_magneto_dot_base_dot_magneto__actions__pb2
from magneto.base.entities import acropolis_pb2 as magneto_dot_base_dot_entities_dot_acropolis__pb2
from magneto.base import entity_pb2 as magneto_dot_base_dot_entity__pb2
from magneto.base import enums_pb2 as magneto_dot_base_dot_enums__pb2
from magneto.base import san_pb2 as magneto_dot_base_dot_san__pb2
from magneto.connectors.acropolis import acropolis_pb2 as magneto_dot_connectors_dot_acropolis_dot_acropolis__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0bridge/magneto/acropolis/acropolis_actions.proto\x12!cohesity.bridge.magneto.acropolis\x1a)bridge/magneto/base/magneto_actions.proto\x1a%magneto/base/entities/acropolis.proto\x1a\x19magneto/base/entity.proto\x1a\x18magneto/base/enums.proto\x1a\x16magneto/base/san.proto\x1a,magneto/connectors/acropolis/acropolis.proto\"\xaf\x05\n\x14\x42\x61\x63kupAcropolisVMArg\x12\x34\n\x04\x62\x61se\x18\x01 \x01(\x0b\x32&.cohesity.bridge.magneto.BackupBaseArg\x12J\n\x04type\x18\x02 \x01(\x0e\x32<.cohesity.bridge.magneto.acropolis.BackupAcropolisVMArg.Type\x12\x37\n\x0broot_entity\x18\x03 \x01(\x0b\x32\".cohesity.magneto.acropolis.Entity\x12\x35\n\tvm_entity\x18\x04 \x01(\x0b\x32\".cohesity.magneto.acropolis.Entity\x12\x33\n\x0csan_port_vec\x18\x05 \x03(\x0b\x32\x1d.cohesity.magneto.san.SanPort\x12\x19\n\x11lun_serial_number\x18\x06 \x01(\t\x12\x37\n\tvm_config\x18\x07 \x01(\x0b\x32$.cohesity.magneto.acropolis.VMConfig\x12\x45\n\rowner_op_type\x18\x08 \x01(\x0e\x32\".cohesity.magneto.Environment.Type:\nkAcropolis\x12;\n\x14owner_op_root_entity\x18\t \x01(\x0b\x32\x1d.cohesity.magneto.EntityProto\x12\x39\n\x12owner_op_vm_entity\x18\n \x01(\x0b\x32\x1d.cohesity.magneto.EntityProto\"]\n\x04Type\x12\x12\n\x0ekPrepareBackup\x10\x01\x12\x0f\n\x0bkSetupFiles\x10\x02\x12\x0f\n\x0bkBackupDisk\x10\x03\x12\x0f\n\x0bkEndSubTask\x10\x04\x12\x0e\n\nkEndBackup\x10\x05\"\xfe\x05\n\x0cRestoreVMArg\x12\x35\n\x04\x62\x61se\x18\x01 \x01(\x0b\x32\'.cohesity.bridge.magneto.RestoreBaseArg\x12\x42\n\x04type\x18\x02 \x01(\x0e\x32\x34.cohesity.bridge.magneto.acropolis.RestoreVMArg.Type\x12Z\n\x0fvm_restore_info\x18\x03 \x01(\x0b\x32=.cohesity.bridge.magneto.acropolis.RestoreVMArg.VMRestoreInfoB\x02\x18\x01\x12\x13\n\x0bview_box_id\x18\x04 \x01(\x03\x12\x11\n\tview_name\x18\x05 \x01(\t\x12\x13\n\x0b\x63reate_view\x18\x06 \x01(\x08\x12\x1f\n\x10is_internal_view\x18\x07 \x01(\x08:\x05\x66\x61lse\x12\x33\n\x0csan_port_vec\x18\x08 \x03(\x0b\x32\x1d.cohesity.magneto.san.SanPort\x12\x19\n\x11lun_serial_number\x18\t \x01(\t\x12Z\n\x13vm_restore_info_vec\x18\n \x03(\x0b\x32=.cohesity.bridge.magneto.acropolis.RestoreVMArg.VMRestoreInfo\x1a\xb6\x01\n\rVMRestoreInfo\x12\x11\n\tview_name\x18\x01 \x01(\t\x12\"\n\x1asnapshot_relative_dir_path\x18\x02 \x01(\t\x12\x35\n\tvm_entity\x18\x03 \x01(\x0b\x32\".cohesity.magneto.acropolis.Entity\x12\x37\n\x0broot_entity\x18\x04 \x01(\x0b\x32\".cohesity.magneto.acropolis.Entity\"T\n\x04Type\x12\x11\n\rkCloneVMFiles\x10\x01\x12\x14\n\x10kRestoreDiskArea\x10\x02\x12\x0f\n\x0bkEndSubTask\x10\x03\x12\x12\n\x0ekDeleteVMFiles\x10\x04\"\xa2\x03\n\x12\x41\x63ropolisActionArg\x12\x0f\n\x07task_id\x18\x01 \x01(\x03\x12\x17\n\x0bsub_task_id\x18\x02 \x01(\x03:\x02-1\x12X\n\x17\x62\x61\x63kup_acropolis_vm_arg\x18\x03 \x01(\x0b\x32\x37.cohesity.bridge.magneto.acropolis.BackupAcropolisVMArg\x12G\n\x0erestore_vm_arg\x18\x04 \x01(\x0b\x32/.cohesity.bridge.magneto.acropolis.RestoreVMArg\x12?\n\x0f\x63\x61ncel_task_arg\x18\x05 \x01(\x0b\x32&.cohesity.bridge.magneto.CancelTaskArg2~\n\x14\x61\x63ropolis_action_arg\x12).cohesity.bridge.magneto.ExecuteActionArg\x18m \x01(\x0b\x32\x35.cohesity.bridge.magneto.acropolis.AcropolisActionArg')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'bridge.magneto.acropolis.acropolis_actions_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_RESTOREVMARG'].fields_by_name['vm_restore_info']._loaded_options = None
  _globals['_RESTOREVMARG'].fields_by_name['vm_restore_info']._serialized_options = b'\030\001'
  _globals['_BACKUPACROPOLISVMARG']._serialized_start=293
  _globals['_BACKUPACROPOLISVMARG']._serialized_end=980
  _globals['_BACKUPACROPOLISVMARG_TYPE']._serialized_start=887
  _globals['_BACKUPACROPOLISVMARG_TYPE']._serialized_end=980
  _globals['_RESTOREVMARG']._serialized_start=983
  _globals['_RESTOREVMARG']._serialized_end=1749
  _globals['_RESTOREVMARG_VMRESTOREINFO']._serialized_start=1481
  _globals['_RESTOREVMARG_VMRESTOREINFO']._serialized_end=1663
  _globals['_RESTOREVMARG_TYPE']._serialized_start=1665
  _globals['_RESTOREVMARG_TYPE']._serialized_end=1749
  _globals['_ACROPOLISACTIONARG']._serialized_start=1752
  _globals['_ACROPOLISACTIONARG']._serialized_end=2170
# @@protoc_insertion_point(module_scope)