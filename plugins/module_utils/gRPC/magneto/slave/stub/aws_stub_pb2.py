# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: magneto/slave/stub/aws_stub.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from bridge.vault.base import vault_pb2 as bridge_dot_vault_dot_base_dot_vault__pb2
from magneto.connectors.aws import aws_pb2 as magneto_dot_connectors_dot_aws_dot_aws__pb2
from magneto.slave.stub import stub_pb2 as magneto_dot_slave_dot_stub_dot_stub__pb2
from magneto.slave.stub import bridge_updates_pb2 as magneto_dot_slave_dot_stub_dot_bridge__updates__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!magneto/slave/stub/aws_stub.proto\x12\x1f\x63ohesity.magneto.slave.stub.aws\x1a\x1d\x62ridge/vault/base/vault.proto\x1a magneto/connectors/aws/aws.proto\x1a\x1dmagneto/slave/stub/stub.proto\x1a\'magneto/slave/stub/bridge_updates.proto\"Q\n\x15SetupVMFilesUpdateArg\x12\x38\n\x0f\x65\x62s_volumes_vec\x18\x01 \x03(\x0b\x32\x1f.cohesity.magneto.aws.EBSVolume\"\xa8\x01\n\x14\x45ndVMBackupUpdateArg\x12N\n!closed_ebs_volumes_vec_DEPRECATED\x18\x01 \x03(\x0b\x32\x1f.cohesity.magneto.aws.EBSVolumeB\x02\x18\x01\x12@\n\x17\x65rrored_ebs_volumes_vec\x18\x02 \x03(\x0b\x32\x1f.cohesity.magneto.aws.EBSVolume\"X\n\x15\x45ndVMRestoreUpdateArg\x12?\n\x16\x63losed_ebs_volumes_vec\x18\x01 \x03(\x0b\x32\x1f.cohesity.magneto.aws.EBSVolume\"\xe7\t\n\x12\x41WSActionUpdateArg\x12\x46\n\x04type\x18\x01 \x01(\x0e\x32\x38.cohesity.magneto.slave.stub.aws.AWSActionUpdateArg.Type\x12U\n\x1dvm_disk_s3_upload_context_vec\x18\x02 \x03(\x0b\x32..cohesity.bridge.vault.VaultUploadContextProto\x12Y\n\x19setup_vm_files_update_arg\x18\x04 \x01(\x0b\x32\x36.cohesity.magneto.slave.stub.aws.SetupVMFilesUpdateArg\x12P\n\x16\x62\x61\x63kup_disk_update_arg\x18\x05 \x01(\x0b\x32\x30.cohesity.magneto.slave.stub.BackupDiskUpdateArg\x12R\n\x17restore_disk_update_arg\x18\x08 \x01(\x0b\x32\x31.cohesity.magneto.slave.stub.RestoreDiskUpdateArg\x12W\n\x18\x65nd_vm_backup_update_arg\x18\x07 \x01(\x0b\x32\x35.cohesity.magneto.slave.stub.aws.EndVMBackupUpdateArg\x12Y\n\x19\x65nd_vm_restore_update_arg\x18\t \x01(\x0b\x32\x36.cohesity.magneto.slave.stub.aws.EndVMRestoreUpdateArg\x12\x31\n\tvm_config\x18\x06 \x01(\x0b\x32\x1e.cohesity.magneto.aws.VMConfig\"\xc6\x03\n\x04Type\x12\x1a\n\x16kCreateS3ObjectsUpdate\x10\x01\x12\x1b\n\x17kCreateEBSVolumesUpdate\x10\x02\x12\x17\n\x13kCopyDiskAreaUpdate\x10\x03\x12\x1c\n\x18kFinalizeS3ObjectsUpdate\x10\x04\x12\x15\n\x11kEndRestoreUpdate\x10\x05\x12\x1c\n\x18kDeleteAWSEntitiesUpdate\x10\x06\x12\x1e\n\x1akDownloadDiskPortionUpdate\x10\x07\x12\x16\n\x12kConvertDiskUpdate\x10\x08\x12\x19\n\x15kCopyVolumeDataUpdate\x10\t\x12\x1a\n\x16kPrepareVMBackupUpdate\x10\n\x12\x17\n\x13kSetupVMFilesUpdate\x10\x0b\x12\x17\n\x13kBackupVMDiskUpdate\x10\x0c\x12\x18\n\x14kRestoreVMDiskUpdate\x10\x10\x12\x15\n\x11kEndSubTaskUpdate\x10\r\x12\x16\n\x12kFetchVMInfoUpdate\x10\x0e\x12\x16\n\x12kEndVMBackupUpdate\x10\x0f\x12\x17\n\x13kEndVMRestoreUpdate\x10\x11\x32\x80\x01\n\x15\x61ws_action_update_arg\x12,.cohesity.magneto.slave.stub.ActionUpdateArg\x18p \x01(\x0b\x32\x33.cohesity.magneto.slave.stub.aws.AWSActionUpdateArg')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'magneto.slave.stub.aws_stub_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_ENDVMBACKUPUPDATEARG'].fields_by_name['closed_ebs_volumes_vec_DEPRECATED']._loaded_options = None
  _globals['_ENDVMBACKUPUPDATEARG'].fields_by_name['closed_ebs_volumes_vec_DEPRECATED']._serialized_options = b'\030\001'
  _globals['_SETUPVMFILESUPDATEARG']._serialized_start=207
  _globals['_SETUPVMFILESUPDATEARG']._serialized_end=288
  _globals['_ENDVMBACKUPUPDATEARG']._serialized_start=291
  _globals['_ENDVMBACKUPUPDATEARG']._serialized_end=459
  _globals['_ENDVMRESTOREUPDATEARG']._serialized_start=461
  _globals['_ENDVMRESTOREUPDATEARG']._serialized_end=549
  _globals['_AWSACTIONUPDATEARG']._serialized_start=552
  _globals['_AWSACTIONUPDATEARG']._serialized_end=1807
  _globals['_AWSACTIONUPDATEARG_TYPE']._serialized_start=1222
  _globals['_AWSACTIONUPDATEARG_TYPE']._serialized_end=1676
# @@protoc_insertion_point(module_scope)
