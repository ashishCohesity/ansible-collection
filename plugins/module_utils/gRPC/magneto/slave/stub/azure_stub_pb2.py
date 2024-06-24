# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: magneto/slave/stub/azure_stub.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from magneto.connectors.azure import azure_pb2 as magneto_dot_connectors_dot_azure_dot_azure__pb2
from magneto.connectors.azure import azure_param_pb2 as magneto_dot_connectors_dot_azure_dot_azure__param__pb2
from magneto.slave.stub import stub_pb2 as magneto_dot_slave_dot_stub_dot_stub__pb2
from magneto.slave.stub import bridge_updates_pb2 as magneto_dot_slave_dot_stub_dot_bridge__updates__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#magneto/slave/stub/azure_stub.proto\x12!cohesity.magneto.slave.stub.azure\x1a$magneto/connectors/azure/azure.proto\x1a*magneto/connectors/azure/azure_param.proto\x1a\x1dmagneto/slave/stub/stub.proto\x1a\'magneto/slave/stub/bridge_updates.proto\"W\n\x15SetupVMFilesUpdateArg\x12>\n\x11virtual_disks_vec\x18\x01 \x03(\x0b\x32#.cohesity.magneto.azure.VirtualDisk\"b\n\x17QueryPageRangeUpdateArg\x12G\n\x12page_ranges_result\x18\x01 \x01(\x0b\x32+.cohesity.magneto.azure.GetPageRangesResult\"\xe3\x06\n\x14\x41zureActionUpdateArg\x12J\n\x04type\x18\x01 \x01(\x0e\x32<.cohesity.magneto.slave.stub.azure.AzureActionUpdateArg.Type\x12[\n\x19setup_vm_files_update_arg\x18\x02 \x01(\x0b\x32\x38.cohesity.magneto.slave.stub.azure.SetupVMFilesUpdateArg\x12P\n\x16\x62\x61\x63kup_disk_update_arg\x18\x03 \x01(\x0b\x32\x30.cohesity.magneto.slave.stub.BackupDiskUpdateArg\x12\x33\n\tvm_config\x18\x04 \x01(\x0b\x32 .cohesity.magneto.azure.VMConfig\x12_\n\x1bquery_page_range_update_arg\x18\x06 \x01(\x0b\x32:.cohesity.magneto.slave.stub.azure.QueryPageRangeUpdateArg\"\x96\x02\n\x04Type\x12\x16\n\x12kCreateBlobsUpdate\x10\x01\x12\x17\n\x13kCopyDiskAreaUpdate\x10\x02\x12\x15\n\x11kEndRestoreUpdate\x10\x03\x12\x16\n\x12kDeleteBlobsUpdate\x10\x04\x12\x1a\n\x16kPrepareVMBackupUpdate\x10\x05\x12\x17\n\x13kSetupVMFilesUpdate\x10\x06\x12\x17\n\x13kBackupVMDiskUpdate\x10\x07\x12\x15\n\x11kEndSubTaskUpdate\x10\x08\x12\x16\n\x12kEndVMBackupUpdate\x10\t\x12\x16\n\x12kFetchVMInfoUpdate\x10\n\x12\x19\n\x15kQueryPageRangeUpdate\x10\x0b\x32\x86\x01\n\x17\x61zure_action_update_arg\x12,.cohesity.magneto.slave.stub.ActionUpdateArg\x18i \x01(\x0b\x32\x37.cohesity.magneto.slave.stub.azure.AzureActionUpdateArgJ\x04\x08\x05\x10\x06R\x12page_ranges_result')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'magneto.slave.stub.azure_stub_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_SETUPVMFILESUPDATEARG']._serialized_start=228
  _globals['_SETUPVMFILESUPDATEARG']._serialized_end=315
  _globals['_QUERYPAGERANGEUPDATEARG']._serialized_start=317
  _globals['_QUERYPAGERANGEUPDATEARG']._serialized_end=415
  _globals['_AZUREACTIONUPDATEARG']._serialized_start=418
  _globals['_AZUREACTIONUPDATEARG']._serialized_end=1285
  _globals['_AZUREACTIONUPDATEARG_TYPE']._serialized_start=844
  _globals['_AZUREACTIONUPDATEARG_TYPE']._serialized_end=1122
# @@protoc_insertion_point(module_scope)
