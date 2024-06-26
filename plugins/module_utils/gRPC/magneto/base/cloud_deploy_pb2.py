# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: magneto/base/cloud_deploy.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from magneto.base import entity_pb2 as magneto_dot_base_dot_entity__pb2
from magneto.base.entities import aws_pb2 as magneto_dot_base_dot_entities_dot_aws__pb2
from magneto.base import env_params_pb2 as magneto_dot_base_dot_env__params__pb2

from magneto.base.env_params_pb2 import *

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1fmagneto/base/cloud_deploy.proto\x12\x10\x63ohesity.magneto\x1a\x19magneto/base/entity.proto\x1a\x1fmagneto/base/entities/aws.proto\x1a\x1dmagneto/base/env_params.proto\"\xf3\x01\n\x16\x41zureManagedDiskParams\x12J\n\x10os_disk_sku_type\x18\x01 \x01(\x0e\x32\x30.cohesity.magneto.AzureManagedDiskParams.SKUType\x12M\n\x13\x64\x61ta_disks_sku_type\x18\x02 \x01(\x0e\x32\x30.cohesity.magneto.AzureManagedDiskParams.SKUType\">\n\x07SKUType\x12\x0f\n\x0bkPremiumSSD\x10\x01\x12\x10\n\x0ckStandardSSD\x10\x02\x12\x10\n\x0ckStandardHDD\x10\x03\"\xb3\t\n\x16\x44\x65ployVMsToAzureParams\x12\x33\n\x0csubscription\x18\x14 \x01(\x0b\x32\x1d.cohesity.magneto.EntityProto\x12-\n\x06region\x18\x15 \x01(\x0b\x32\x1d.cohesity.magneto.EntityProto\x12\x35\n\x0eresource_group\x18\x02 \x01(\x0b\x32\x1d.cohesity.magneto.EntityProto\x12\x36\n\x0f\x63ompute_options\x18\x03 \x01(\x0b\x32\x1d.cohesity.magneto.EntityProto\x12=\n\x16storage_resource_group\x18\n \x01(\x0b\x32\x1d.cohesity.magneto.EntityProto\x12\x36\n\x0fstorage_account\x18\x04 \x01(\x0b\x32\x1d.cohesity.magneto.EntityProto\x12\x38\n\x11storage_container\x18\x05 \x01(\x0b\x32\x1d.cohesity.magneto.EntityProto\x12\x32\n\x0bstorage_key\x18\x06 \x01(\x0b\x32\x1d.cohesity.magneto.EntityProto\x12=\n\x16network_security_group\x18\x0c \x01(\x0b\x32\x1d.cohesity.magneto.EntityProto\x12=\n\x16network_resource_group\x18\t \x01(\x0b\x32\x1d.cohesity.magneto.EntityProto\x12\x36\n\x0fvirtual_network\x18\x07 \x01(\x0b\x32\x1d.cohesity.magneto.EntityProto\x12-\n\x06subnet\x18\x08 \x01(\x0b\x32\x1d.cohesity.magneto.EntityProto\x12K\n\x19\x61zure_managed_disk_params\x18\x0b \x01(\x0b\x32(.cohesity.magneto.AzureManagedDiskParams\x12=\n\x16temp_vm_resource_group\x18\r \x01(\x0b\x32\x1d.cohesity.magneto.EntityProto\x12>\n\x17temp_vm_storage_account\x18\x0e \x01(\x0b\x32\x1d.cohesity.magneto.EntityProto\x12@\n\x19temp_vm_storage_container\x18\x0f \x01(\x0b\x32\x1d.cohesity.magneto.EntityProto\x12>\n\x17temp_vm_virtual_network\x18\x10 \x01(\x0b\x32\x1d.cohesity.magneto.EntityProto\x12\x35\n\x0etemp_vm_subnet\x18\x11 \x01(\x0b\x32\x1d.cohesity.magneto.EntityProto\x12\x37\n\x10\x61vailability_set\x18\x12 \x01(\x0b\x32\x1d.cohesity.magneto.EntityProto\x12>\n\x12\x64\x61ta_transfer_info\x18\x13 \x01(\x0b\x32\".cohesity.magneto.DataTransferInfo\"\xae\x04\n\x1c\x44\x65ployDBInstancesToRDSParams\x12\x16\n\x0e\x64\x62_instance_id\x18\x01 \x01(\t\x12\x38\n\x11\x61vailability_zone\x18\x02 \x01(\x0b\x32\x1d.cohesity.magneto.EntityProto\x12\x39\n\x12\x64\x62_parameter_group\x18\x03 \x01(\x0b\x32\x1d.cohesity.magneto.EntityProto\x12\x36\n\x0f\x64\x62_option_group\x18\x04 \x01(\x0b\x32\x1d.cohesity.magneto.EntityProto\x12\x1b\n\x13multi_az_deployment\x18\x05 \x01(\x08\x12\x0f\n\x07\x64\x62_port\x18\x06 \x01(\x05\x12\"\n\x1a\x61uto_minor_version_upgrade\x18\x07 \x01(\x08\x12\x1e\n\x16\x63opy_tags_to_snapshots\x18\x08 \x01(\x08\x12\x1d\n\x15iam_db_authentication\x18\t \x01(\x08\x12\x1c\n\x14public_accessibility\x18\n \x01(\x08\x12\x65\n\x14point_in_time_params\x18\x0b \x01(\x0b\x32G.cohesity.magneto.DeployDBInstancesToRDSParams.PointInTimeRestoreParams\x1a\x33\n\x18PointInTimeRestoreParams\x12\x17\n\x0ftimestamp_msecs\x18\x01 \x01(\x03\"\xb8\x05\n\x14\x44\x65ployVMsToAWSParams\x12-\n\x06region\x18\x01 \x01(\x0b\x32\x1d.cohesity.magneto.EntityProto\x12\x34\n\rinstance_type\x18\x02 \x01(\x0b\x32\x1d.cohesity.magneto.EntityProto\x12*\n\x03vpc\x18\x03 \x01(\x0b\x32\x1d.cohesity.magneto.EntityProto\x12-\n\x06subnet\x18\x04 \x01(\x0b\x32\x1d.cohesity.magneto.EntityProto\x12>\n\x17network_security_groups\x18\x05 \x03(\x0b\x32\x1d.cohesity.magneto.EntityProto\x12\x34\n\rkey_pair_name\x18\x06 \x01(\x0b\x32\x1d.cohesity.magneto.EntityProto\x12\x42\n\nrds_params\x18\x07 \x01(\x0b\x32..cohesity.magneto.DeployDBInstancesToRDSParams\x12\x45\n\raurora_params\x18\n \x01(\x0b\x32..cohesity.magneto.DeployDBInstancesToRDSParams\x12\x33\n\x0cproxy_vm_vpc\x18\x08 \x01(\x0b\x32\x1d.cohesity.magneto.EntityProto\x12\x36\n\x0fproxy_vm_subnet\x18\t \x01(\x0b\x32\x1d.cohesity.magneto.EntityProto\x12\x33\n\x0e\x63ustom_tag_vec\x18\x0b \x03(\x0b\x32\x1b.cohesity.magneto.CustomTag\x12=\n\x11\x65ncryption_params\x18\x0c \x01(\x0b\x32\".cohesity.magneto.EncryptionParams\"\'\n\tCustomTag\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"\xd4\x01\n\x14\x44\x65ployVMsToGCPParams\x12\x31\n\nproject_id\x18\x01 \x01(\x0b\x32\x1d.cohesity.magneto.EntityProto\x12-\n\x06region\x18\x02 \x01(\x0b\x32\x1d.cohesity.magneto.EntityProto\x12+\n\x04zone\x18\x03 \x01(\x0b\x32\x1d.cohesity.magneto.EntityProto\x12-\n\x06subnet\x18\x04 \x01(\x0b\x32\x1d.cohesity.magneto.EntityProto\"N\n\x1dReplicateSnapshotsToAWSParams\x12-\n\x06region\x18\x01 \x01(\x0b\x32\x1d.cohesity.magneto.EntityProto\"\x89\x02\n\x1fReplicateSnapshotsToAzureParams\x12=\n\x16storage_resource_group\x18\x01 \x01(\x0b\x32\x1d.cohesity.magneto.EntityProto\x12\x36\n\x0fstorage_account\x18\x02 \x01(\x0b\x32\x1d.cohesity.magneto.EntityProto\x12\x38\n\x11storage_container\x18\x03 \x01(\x0b\x32\x1d.cohesity.magneto.EntityProto\x12\x35\n\x0eresource_group\x18\x04 \x01(\x0b\x32\x1d.cohesity.magneto.EntityProto\"S\n\x11\x44\x65ployFleetParams\x12>\n\x10\x61ws_fleet_params\x18\x01 \x01(\x0b\x32$.cohesity.magneto.aws.AWSFleetParams\"\xf8\x03\n\x16\x44\x65ployVMsToCloudParams\x12L\n\x1a\x64\x65ploy_vms_to_azure_params\x18\x01 \x01(\x0b\x32(.cohesity.magneto.DeployVMsToAzureParams\x12H\n\x18\x64\x65ploy_vms_to_aws_params\x18\x02 \x01(\x0b\x32&.cohesity.magneto.DeployVMsToAWSParams\x12H\n\x18\x64\x65ploy_vms_to_gcp_params\x18\x03 \x01(\x0b\x32&.cohesity.magneto.DeployVMsToGCPParams\x12Z\n!replicate_snapshots_to_aws_params\x18\x04 \x01(\x0b\x32/.cohesity.magneto.ReplicateSnapshotsToAWSParams\x12^\n#replicate_snapshots_to_azure_params\x18\x05 \x01(\x0b\x32\x31.cohesity.magneto.ReplicateSnapshotsToAzureParams\x12@\n\x13\x64\x65ploy_fleet_params\x18\x06 \x01(\x0b\x32#.cohesity.magneto.DeployFleetParams\"\x8b\x01\n\x10\x45ncryptionParams\x12\x16\n\x0eshould_encrypt\x18\x01 \x01(\x08\x12\x30\n\x07kms_key\x18\x02 \x01(\x0b\x32\x1d.cohesity.magneto.EntityProtoH\x00\x12\x1c\n\x12\x63ustom_kms_key_arn\x18\x03 \x01(\tH\x00\x42\x0f\n\rkms_key_oneofP\x02')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'magneto.base.cloud_deploy_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_AZUREMANAGEDDISKPARAMS']._serialized_start=145
  _globals['_AZUREMANAGEDDISKPARAMS']._serialized_end=388
  _globals['_AZUREMANAGEDDISKPARAMS_SKUTYPE']._serialized_start=326
  _globals['_AZUREMANAGEDDISKPARAMS_SKUTYPE']._serialized_end=388
  _globals['_DEPLOYVMSTOAZUREPARAMS']._serialized_start=391
  _globals['_DEPLOYVMSTOAZUREPARAMS']._serialized_end=1594
  _globals['_DEPLOYDBINSTANCESTORDSPARAMS']._serialized_start=1597
  _globals['_DEPLOYDBINSTANCESTORDSPARAMS']._serialized_end=2155
  _globals['_DEPLOYDBINSTANCESTORDSPARAMS_POINTINTIMERESTOREPARAMS']._serialized_start=2104
  _globals['_DEPLOYDBINSTANCESTORDSPARAMS_POINTINTIMERESTOREPARAMS']._serialized_end=2155
  _globals['_DEPLOYVMSTOAWSPARAMS']._serialized_start=2158
  _globals['_DEPLOYVMSTOAWSPARAMS']._serialized_end=2854
  _globals['_CUSTOMTAG']._serialized_start=2856
  _globals['_CUSTOMTAG']._serialized_end=2895
  _globals['_DEPLOYVMSTOGCPPARAMS']._serialized_start=2898
  _globals['_DEPLOYVMSTOGCPPARAMS']._serialized_end=3110
  _globals['_REPLICATESNAPSHOTSTOAWSPARAMS']._serialized_start=3112
  _globals['_REPLICATESNAPSHOTSTOAWSPARAMS']._serialized_end=3190
  _globals['_REPLICATESNAPSHOTSTOAZUREPARAMS']._serialized_start=3193
  _globals['_REPLICATESNAPSHOTSTOAZUREPARAMS']._serialized_end=3458
  _globals['_DEPLOYFLEETPARAMS']._serialized_start=3460
  _globals['_DEPLOYFLEETPARAMS']._serialized_end=3543
  _globals['_DEPLOYVMSTOCLOUDPARAMS']._serialized_start=3546
  _globals['_DEPLOYVMSTOCLOUDPARAMS']._serialized_end=4050
  _globals['_ENCRYPTIONPARAMS']._serialized_start=4053
  _globals['_ENCRYPTIONPARAMS']._serialized_end=4192
# @@protoc_insertion_point(module_scope)
