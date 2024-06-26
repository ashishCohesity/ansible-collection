# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: heimdall/master/adapters/azure/azure.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from heimdall.master.base import master_pb2 as heimdall_dot_master_dot_base_dot_master__pb2
from heimdall.master.stub import rpc_service_pb2 as heimdall_dot_master_dot_stub_dot_rpc__service__pb2
from nexus.cloud.connectors.azure import rest_api_pb2 as nexus_dot_cloud_dot_connectors_dot_azure_dot_rest__api__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*heimdall/master/adapters/azure/azure.proto\x12\x1e\x63ohesity.heimdall.master.azure\x1a!heimdall/master/base/master.proto\x1a&heimdall/master/stub/rpc_service.proto\x1a+nexus/cloud/connectors/azure/rest_api.proto\"\xf3\x05\n\x14\x41zureAcquireDisksArg\x12\x11\n\tdisk_name\x18\x01 \x01(\t\x12\x17\n\x0fsubscription_id\x18\x02 \x01(\t\x12\x1b\n\x13resource_group_name\x18\x03 \x01(\t\x12\x12\n\nsize_bytes\x18\x04 \x01(\x03\x12\x1b\n\x13logical_sector_size\x18\x05 \x01(\x05\x12\x0e\n\x06region\x18\x06 \x01(\t\x12L\n\x04tags\x18\x07 \x03(\x0b\x32>.cohesity.heimdall.master.azure.AzureAcquireDisksArg.TagsEntry\x12K\n\x08sku_name\x18\x08 \x01(\x0e\x32+.cohesity.heimdall.master.azure.DiskSkuName:\x0ckPremium_LRS\x12G\n\x08sku_tier\x18\t \x01(\x0e\x32+.cohesity.heimdall.master.azure.DiskSkuTier:\x08kPremium\x12\r\n\x05vm_id\x18\n \x01(\t\x12:\n\x02\x66s\x18\x0b \x01(\x0e\x32(.cohesity.heimdall.master.FileSystemType:\x04kXFS\x12N\n\x0epartition_type\x18\x0c \x01(\x0e\x32+.cohesity.heimdall.master.DiskPartitionType:\tkStandard\x12\x1a\n\x0fnumber_of_disks\x18\r \x01(\x05:\x01\x31\x1a+\n\tTagsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x32\x88\x01\n\x17\x61zure_acquire_disks_arg\x12\x31.cohesity.heimdall.master.stub.AcquireResourceArg\x18g \x01(\x0b\x32\x34.cohesity.heimdall.master.azure.AzureAcquireDisksArg\"\x80\x05\n\x0e\x41zureDisksInfo\x12\x0e\n\x06region\x18\x01 \x01(\t\x12\x46\n\x04tags\x18\x02 \x03(\x0b\x32\x38.cohesity.heimdall.master.azure.AzureDisksInfo.TagsEntry\x12\x17\n\x0fsubscription_id\x18\x03 \x01(\t\x12\x1b\n\x13resource_group_name\x18\x04 \x01(\t\x12\r\n\x05vm_id\x18\x05 \x01(\t\x12\x13\n\x0bmount_point\x18\x06 \x01(\t\x12K\n\x08sku_name\x18\x07 \x01(\x0e\x32+.cohesity.heimdall.master.azure.DiskSkuName:\x0ckPremium_LRS\x12G\n\x08sku_tier\x18\x08 \x01(\x0e\x32+.cohesity.heimdall.master.azure.DiskSkuTier:\x08kPremium\x12:\n\x02\x66s\x18\t \x01(\x0e\x32(.cohesity.heimdall.master.FileSystemType:\x04kXFS\x12N\n\x0epartition_type\x18\n \x01(\x0e\x32+.cohesity.heimdall.master.DiskPartitionType:\tkStandard\x1a+\n\tTagsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x32m\n\x10\x61zure_disks_info\x12#.cohesity.heimdall.master.DisksInfo\x18\x65 \x01(\x0b\x32..cohesity.heimdall.master.azure.AzureDisksInfo\"\xcd\x02\n\x17\x41zureAcquireDisksResult\x12W\n\rdisk_info_vec\x18\x01 \x03(\x0b\x32@.cohesity.heimdall.master.azure.AzureAcquireDisksResult.DiskInfo\x12\x13\n\x0bmount_point\x18\x02 \x01(\t\x1a\x30\n\x08\x44iskInfo\x12\x0f\n\x07\x64isk_id\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65vice_name\x18\x02 \x01(\t2\x91\x01\n\x1a\x61zure_acquire_disks_result\x12\x34.cohesity.heimdall.master.stub.AcquireResourceResult\x18g \x01(\x0b\x32\x37.cohesity.heimdall.master.azure.AzureAcquireDisksResult\"\xbb\x03\n\x19\x41zureAcquireDiskAccessArg\x12\x0e\n\x06region\x18\x01 \x01(\t\x12\x0e\n\x06vpn_id\x18\x02 \x01(\t\x12\x0e\n\x06subnet\x18\x03 \x01(\t\x12Q\n\x04tags\x18\x04 \x03(\x0b\x32\x43.cohesity.heimdall.master.azure.AzureAcquireDiskAccessArg.TagsEntry\x12\x1b\n\x13resource_group_name\x18\x05 \x01(\t\x12\"\n\x14\x61\x64\x64_dns_to_etc_hosts\x18\x06 \x01(\x08:\x04true\x12\x17\n\x0fsubscription_id\x18\x07 \x01(\t\x1a+\n\tTagsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x32\x93\x01\n\x1d\x61zure_acquire_disk_access_arg\x12\x31.cohesity.heimdall.master.stub.AcquireResourceArg\x18\x65 \x01(\x0b\x32\x39.cohesity.heimdall.master.azure.AzureAcquireDiskAccessArg\"\xb7\x03\n\x13\x41zureDiskAccessInfo\x12\x0e\n\x06region\x18\x01 \x01(\t\x12\x0e\n\x06vpn_id\x18\x02 \x01(\t\x12\x0e\n\x06subnet\x18\x03 \x01(\t\x12K\n\x04tags\x18\x04 \x03(\x0b\x32=.cohesity.heimdall.master.azure.AzureDiskAccessInfo.TagsEntry\x12\x1b\n\x13resource_group_name\x18\x05 \x01(\t\x12\"\n\x14\x61\x64\x64_dns_to_etc_hosts\x18\x06 \x01(\x08:\x04true\x12\x17\n\x0fsubscription_id\x18\x07 \x01(\t\x12\x1d\n\x15subnet_resource_group\x18\x08 \x01(\t\x1a+\n\tTagsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x32}\n\x16\x61zure_disk_access_info\x12(.cohesity.heimdall.master.DiskAccessInfo\x18\x65 \x01(\x0b\x32\x33.cohesity.heimdall.master.azure.AzureDiskAccessInfo\"\xb8\x02\n\x1c\x41zureAcquireDiskAccessResult\x12\x16\n\x0e\x64isk_access_id\x18\x01 \x01(\t\x12\x1b\n\x13private_endpoint_id\x18\x02 \x01(\t\x12\x1d\n\x15private_endpoint_fqdn\x18\x03 \x01(\t\x12%\n\x1dprivate_endpoint_ipv4_address\x18\x04 \x01(\t2\x9c\x01\n azure_acquire_disk_access_result\x12\x34.cohesity.heimdall.master.stub.AcquireResourceResult\x18\x65 \x01(\x0b\x32<.cohesity.heimdall.master.azure.AzureAcquireDiskAccessResult*6\n\x0b\x44iskSkuTier\x12\x0c\n\x08kPremium\x10\x01\x12\r\n\tkStandard\x10\x02\x12\n\n\x06kUltra\x10\x03*\x97\x01\n\x0b\x44iskSkuName\x12\x10\n\x0ckPremium_LRS\x10\x01\x12\x12\n\x0ekPremiumV2_LRS\x10\x02\x12\x10\n\x0ckPremium_ZRS\x10\x03\x12\x14\n\x10kStandardSSD_LRS\x10\x04\x12\x14\n\x10kStandardSSD_ZRS\x10\x05\x12\x11\n\rkStandard_LRS\x10\x06\x12\x11\n\rkUltraSSD_LRS\x10\x07')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'heimdall.master.adapters.azure.azure_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_AZUREACQUIREDISKSARG_TAGSENTRY']._loaded_options = None
  _globals['_AZUREACQUIREDISKSARG_TAGSENTRY']._serialized_options = b'8\001'
  _globals['_AZUREDISKSINFO_TAGSENTRY']._loaded_options = None
  _globals['_AZUREDISKSINFO_TAGSENTRY']._serialized_options = b'8\001'
  _globals['_AZUREACQUIREDISKACCESSARG_TAGSENTRY']._loaded_options = None
  _globals['_AZUREACQUIREDISKACCESSARG_TAGSENTRY']._serialized_options = b'8\001'
  _globals['_AZUREDISKACCESSINFO_TAGSENTRY']._loaded_options = None
  _globals['_AZUREDISKACCESSINFO_TAGSENTRY']._serialized_options = b'8\001'
  _globals['_DISKSKUTIER']._serialized_start=3138
  _globals['_DISKSKUTIER']._serialized_end=3192
  _globals['_DISKSKUNAME']._serialized_start=3195
  _globals['_DISKSKUNAME']._serialized_end=3346
  _globals['_AZUREACQUIREDISKSARG']._serialized_start=199
  _globals['_AZUREACQUIREDISKSARG']._serialized_end=954
  _globals['_AZUREACQUIREDISKSARG_TAGSENTRY']._serialized_start=772
  _globals['_AZUREACQUIREDISKSARG_TAGSENTRY']._serialized_end=815
  _globals['_AZUREDISKSINFO']._serialized_start=957
  _globals['_AZUREDISKSINFO']._serialized_end=1597
  _globals['_AZUREDISKSINFO_TAGSENTRY']._serialized_start=772
  _globals['_AZUREDISKSINFO_TAGSENTRY']._serialized_end=815
  _globals['_AZUREACQUIREDISKSRESULT']._serialized_start=1600
  _globals['_AZUREACQUIREDISKSRESULT']._serialized_end=1933
  _globals['_AZUREACQUIREDISKSRESULT_DISKINFO']._serialized_start=1737
  _globals['_AZUREACQUIREDISKSRESULT_DISKINFO']._serialized_end=1785
  _globals['_AZUREACQUIREDISKACCESSARG']._serialized_start=1936
  _globals['_AZUREACQUIREDISKACCESSARG']._serialized_end=2379
  _globals['_AZUREACQUIREDISKACCESSARG_TAGSENTRY']._serialized_start=772
  _globals['_AZUREACQUIREDISKACCESSARG_TAGSENTRY']._serialized_end=815
  _globals['_AZUREDISKACCESSINFO']._serialized_start=2382
  _globals['_AZUREDISKACCESSINFO']._serialized_end=2821
  _globals['_AZUREDISKACCESSINFO_TAGSENTRY']._serialized_start=772
  _globals['_AZUREDISKACCESSINFO_TAGSENTRY']._serialized_end=815
  _globals['_AZUREACQUIREDISKACCESSRESULT']._serialized_start=2824
  _globals['_AZUREACQUIREDISKACCESSRESULT']._serialized_end=3136
# @@protoc_insertion_point(module_scope)
