# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: magneto/connectors/kvm/kvm_rest_api.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)magneto/connectors/kvm/kvm_rest_api.proto\x12\x19\x63ohesity.magneto.kvm.rest\"#\n\x0bTokenResult\x12\x14\n\x0c\x61\x63\x63\x65ss_token\x18\x01 \x01(\t\".\n\x0c\x45rrorContext\x12\x0e\n\x06reason\x18\x01 \x01(\t\x12\x0e\n\x06\x64\x65tail\x18\x02 \x01(\t\"#\n\x07\x43luster\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\"\xb0\x01\n\x06OSInfo\x12\x34\n\x04\x62oot\x18\x01 \x01(\x0b\x32&.cohesity.magneto.kvm.rest.OSInfo.Boot\x12\x0c\n\x04type\x18\x02 \x01(\t\x1a\x62\n\x04\x42oot\x12?\n\x07\x64\x65vices\x18\x01 \x01(\x0b\x32..cohesity.magneto.kvm.rest.OSInfo.Boot.Devices\x1a\x19\n\x07\x44\x65vices\x12\x0e\n\x06\x64\x65vice\x18\x01 \x03(\t\"\xee\t\n\x06VMInfo\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\n\n\x02id\x18\x03 \x01(\t\x12\x0e\n\x06status\x18\x04 \x01(\t\x12\x32\n\x03\x63pu\x18\x05 \x01(\x0b\x32%.cohesity.magneto.kvm.rest.VMInfo.CPU\x12\x0e\n\x06memory\x18\x06 \x01(\x03\x12-\n\x02os\x18\x07 \x01(\x0b\x32!.cohesity.magneto.kvm.rest.OSInfo\x12\x33\n\x07\x63luster\x18\x08 \x01(\x0b\x32\".cohesity.magneto.kvm.rest.Cluster\x12I\n\x0bvm_template\x18\t \x01(\x0b\x32*.cohesity.magneto.kvm.rest.VMInfo.TemplateR\x08template\x12\x34\n\x04host\x18\n \x01(\x0b\x32&.cohesity.magneto.kvm.rest.VMInfo.Host\x12\x38\n\x17\x63ustom_emulated_machine\x18\x0b \x01(\tR\x17\x63ustom_emulated_machine\x12\x0c\n\x04type\x18\x0c \x01(\t\x12\x0f\n\x07\x63omment\x18\r \x01(\t\x12T\n\rmemory_policy\x18\x0e \x01(\x0b\x32..cohesity.magneto.kvm.rest.VMInfo.MemoryPolicyR\rmemory_policy\x12`\n\x11high_availability\x18\x0f \x01(\x0b\x32\x32.cohesity.magneto.kvm.rest.VMInfo.HighAvailabilityR\x11high_availability\x12H\n\ttime_zone\x18\x10 \x01(\x0b\x32*.cohesity.magneto.kvm.rest.VMInfo.TimeZoneR\ttime_zone\x12H\n\x0einitialization\x18\x11 \x01(\x0b\x32\x30.cohesity.magneto.kvm.rest.VMInfo.Initialization\x12\x17\n\x0ftotal_disk_size\x18\x12 \x01(\x03\x1a\x84\x01\n\x03\x43PU\x12@\n\x08topology\x18\x01 \x01(\x0b\x32..cohesity.magneto.kvm.rest.VMInfo.CPU.Topology\x1a;\n\x08Topology\x12\x0f\n\x07sockets\x18\x01 \x01(\x05\x12\r\n\x05\x63ores\x18\x02 \x01(\x05\x12\x0f\n\x07threads\x18\x03 \x01(\x05\x1a\x18\n\x08Template\x12\x0c\n\x04name\x18\x01 \x01(\t\x1a\x12\n\x04Host\x12\n\n\x02id\x18\x01 \x01(\t\x1a/\n\x0cMemoryPolicy\x12\x12\n\nguaranteed\x18\x01 \x01(\x03\x12\x0b\n\x03max\x18\x02 \x01(\x03\x1a\x35\n\x10HighAvailability\x12\x0f\n\x07\x65nabled\x18\x01 \x01(\x08\x12\x10\n\x08priority\x18\x02 \x01(\x05\x1a\x18\n\x08TimeZone\x12\x0c\n\x04name\x18\x01 \x01(\t\x1a\x86\x01\n\x0eInitialization\x12U\n\rconfiguration\x18\x01 \x01(\x0b\x32>.cohesity.magneto.kvm.rest.VMInfo.Initialization.Configuration\x1a\x1d\n\rConfiguration\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\t\"\xbb\x01\n\nHostConfig\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x12\x0f\n\x07\x61\x64\x64ress\x18\x04 \x01(\t\x12\x33\n\x07\x63luster\x18\x03 \x01(\x0b\x32\".cohesity.magneto.kvm.rest.Cluster\x12\x36\n\x03spm\x18\x05 \x01(\x0b\x32).cohesity.magneto.kvm.rest.HostConfig.SPM\x1a\x15\n\x03SPM\x12\x0e\n\x06status\x18\x01 \x01(\t\"E\n\x0eHostListResult\x12\x33\n\x04host\x18\x01 \x03(\x0b\x32%.cohesity.magneto.kvm.rest.HostConfig\"\x18\n\nDataCenter\x12\n\n\x02id\x18\x01 \x01(\t\"=\n\x0cVMListResult\x12-\n\x02vm\x18\x01 \x03(\x0b\x32!.cohesity.magneto.kvm.rest.VMInfo\"z\n\rNetworkConfig\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12:\n\x0b\x64\x61ta_center\x18\x04 \x01(\x0b\x32%.cohesity.magneto.kvm.rest.DataCenter\"N\n\x11NetworkListResult\x12\x39\n\x07network\x18\x01 \x03(\x0b\x32(.cohesity.magneto.kvm.rest.NetworkConfig\"e\n\rClusterConfig\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x12:\n\x0b\x64\x61ta_center\x18\x03 \x01(\x0b\x32%.cohesity.magneto.kvm.rest.DataCenter\"N\n\x11\x43lusterListResult\x12\x39\n\x07\x63luster\x18\x01 \x03(\x0b\x32(.cohesity.magneto.kvm.rest.ClusterConfig\"#\n\x07MACPool\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\"J\n\x12MACPoolsListResult\x12\x34\n\x08mac_pool\x18\x01 \x03(\x0b\x32\".cohesity.magneto.kvm.rest.MACPool\"\xa0\x02\n\x13StorageDomainConfig\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x12\x0e\n\x06status\x18\x03 \x01(\t\x12S\n\x0c\x64\x61ta_centers\x18\x04 \x01(\x0b\x32=.cohesity.magneto.kvm.rest.StorageDomainConfig.DataCenterList\x1a\x89\x01\n\x0e\x44\x61taCenterList\x12]\n\x0b\x64\x61ta_center\x18\x01 \x03(\x0b\x32H.cohesity.magneto.kvm.rest.StorageDomainConfig.DataCenterList.DataCenter\x1a\x18\n\nDataCenter\x12\n\n\x02id\x18\x01 \x01(\t\"a\n\x17StorageDomainListResult\x12\x46\n\x0estorage_domain\x18\x01 \x03(\x0b\x32..cohesity.magneto.kvm.rest.StorageDomainConfig\",\n\x10\x44\x61taCenterConfig\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\"X\n\x14\x44\x61taCenterListResult\x12@\n\x0b\x64\x61ta_center\x18\x01 \x03(\x0b\x32+.cohesity.magneto.kvm.rest.DataCenterConfig\"\x7f\n\x0bVNicProfile\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12?\n\x07network\x18\x03 \x01(\x0b\x32..cohesity.magneto.kvm.rest.VNicProfile.Network\x1a\x15\n\x07Network\x12\n\n\x02id\x18\x01 \x01(\t\"]\n\x0fVNicProfileList\x12J\n\x0cvnic_profile\x18\x01 \x03(\x0b\x32&.cohesity.magneto.kvm.rest.VNicProfileR\x0cvnic_profile\"\x1d\n\x0cVMNicListArg\x12\r\n\x05vm_id\x18\x01 \x01(\t\"\x87\x05\n\x03Nic\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x12/\n\x03mac\x18\x03 \x01(\x0b\x32\".cohesity.magneto.kvm.rest.Nic.Mac\x12R\n\x10reported_devices\x18\x04 \x01(\x0b\x32&.cohesity.magneto.kvm.rest.Nic.DevicesR\x10reported_devices\x12J\n\x0cvnic_profile\x18\x05 \x01(\x0b\x32&.cohesity.magneto.kvm.rest.VNicProfileR\x0cvnic_profile\x12\x42\n\x07network\x18\x06 \x01(\x0b\x32(.cohesity.magneto.kvm.rest.NetworkConfigR\x07network\x1a\x16\n\x03Mac\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\x1a\xb8\x02\n\x07\x44\x65vices\x12W\n\x0freported_device\x18\x01 \x03(\x0b\x32-.cohesity.magneto.kvm.rest.Nic.Devices.DeviceR\x0freported_device\x1a\xd3\x01\n\x06\x44\x65vice\x12>\n\x03ips\x18\x01 \x01(\x0b\x32\x31.cohesity.magneto.kvm.rest.Nic.Devices.Device.IPs\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\n\n\x02id\x18\x03 \x01(\t\x1ao\n\x03IPs\x12@\n\x02ip\x18\x01 \x03(\x0b\x32\x34.cohesity.magneto.kvm.rest.Nic.Devices.Device.IPs.IP\x1a&\n\x02IP\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t\">\n\x0fVMNicListResult\x12+\n\x03nic\x18\x01 \x03(\x0b\x32\x1e.cohesity.magneto.kvm.rest.Nic\"\x1d\n\nHostNicArg\x12\x0f\n\x07host_id\x18\x01 \x01(\t\"\xe7\x01\n\rHostNicResult\x12\x42\n\x08host_nic\x18\x01 \x03(\x0b\x32\x30.cohesity.magneto.kvm.rest.HostNicResult.HostNic\x1a\x91\x01\n\x07HostNic\x12\x0c\n\x04name\x18\x01 \x01(\t\x12?\n\x02ip\x18\x02 \x01(\x0b\x32\x33.cohesity.magneto.kvm.rest.HostNicResult.HostNic.IP\x1a\x37\n\x02IP\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\x12\x0f\n\x07gateway\x18\x02 \x01(\t\x12\x0f\n\x07netmask\x18\x03 \x01(\t\"\xa7\x02\n\x0bOVirtConfig\x12H\n\x0cproduct_info\x18\x01 \x01(\x0b\x32\x32.cohesity.magneto.kvm.rest.OVirtConfig.ProductInfo\x1a\xcd\x01\n\x0bProductInfo\x12\x0c\n\x04name\x18\x01 \x01(\t\x12K\n\x07version\x18\x02 \x01(\x0b\x32:.cohesity.magneto.kvm.rest.OVirtConfig.ProductInfo.Version\x1a\x63\n\x07Version\x12\x1c\n\rmajor_version\x18\x01 \x01(\tR\x05major\x12\x1c\n\rminor_version\x18\x02 \x01(\tR\x05minor\x12\x1c\n\rbuild_version\x18\x03 \x01(\tR\x05\x62uild\"!\n\x0b\x44iskInfoArg\x12\x12\n\nurl_prefix\x18\x01 \x01(\t\"\xb0\x04\n\x08\x44iskInfo\x12$\n\x0b\x61\x63tual_size\x18\x01 \x01(\x03\x42\x02\x30\x02R\x0b\x61\x63tual_size\x12.\n\x10provisioned_size\x18\x02 \x01(\x03\x42\x02\x30\x02R\x10provisioned_size\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\n\n\x02id\x18\x04 \x01(\t\x12\x0e\n\x06\x66ormat\x18\x05 \x01(\t\x12\x1c\n\tread_only\x18\x06 \x01(\x08R\tread_only\x12\x11\n\tshareable\x18\x07 \x01(\x08\x12,\n\x11wipe_after_delete\x18\x08 \x01(\x08R\x11wipe_after_delete\x12\x0e\n\x06sparse\x18\t \x01(\x08\x12\x1a\n\x08image_id\x18\n \x01(\tR\x08image_id\x12\\\n\x0fstorage_domains\x18\x0b \x01(\x0b\x32\x32.cohesity.magneto.kvm.rest.DiskInfo.StorageDomainsR\x0fstorage_domains\x12\x13\n\x0b\x64\x65scription\x18\x0c \x01(\t\x1a\xa5\x01\n\x0eStorageDomains\x12h\n\x0estorage_domain\x18\x01 \x03(\x0b\x32@.cohesity.magneto.kvm.rest.DiskInfo.StorageDomains.StorageDomainR\x0estorage_domain\x1a)\n\rStorageDomain\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\"C\n\x0e\x44iskInfoResult\x12\x31\n\x04\x64isk\x18\x01 \x03(\x0b\x32#.cohesity.magneto.kvm.rest.DiskInfo\";\n\rWaitForJobArg\x12\x0e\n\x06job_id\x18\x01 \x01(\t\x12\x1a\n\x12wait_timeout_usecs\x18\x02 \x01(\x03\"C\n\x10WaitForJobResult\x12\x0e\n\x06status\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\n\n\x02id\x18\x03 \x01(\t\"h\n\x0cPollEventArg\x12\x16\n\x0e\x63orrelation_id\x18\x01 \x01(\t\x12\x14\n\x0csuccess_code\x18\x02 \x01(\x05\x12\x14\n\x0c\x66\x61ilure_code\x18\x03 \x01(\x05\x12\x14\n\x0ctimeout_secs\x18\x04 \x01(\x05\"\xa8\x01\n\x0fPollEventResult\x12?\n\x05\x65vent\x18\x01 \x03(\x0b\x32\x30.cohesity.magneto.kvm.rest.PollEventResult.Event\x1aT\n\x05\x45vent\x12\x16\n\x0e\x63orrelation_id\x18\x01 \x01(\t\x12\x10\n\x08severity\x18\x02 \x01(\t\x12\x0c\n\x04\x63ode\x18\x03 \x01(\x05\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\"a\n\x07JobInfo\x12\x0e\n\x06status\x18\x01 \x01(\t\x12\x33\n\x03job\x18\x02 \x01(\x0b\x32&.cohesity.magneto.kvm.rest.JobInfo.Job\x1a\x11\n\x03Job\x12\n\n\x02id\x18\x01 \x01(\t\"\x9f\x02\n\x12SnapshotInfoResult\x12\n\n\x02id\x18\x01 \x01(\t\x12@\n\x02vm\x18\x02 \x01(\x0b\x32\x34.cohesity.magneto.kvm.rest.SnapshotInfoResult.VMInfo\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x17\n\x0fsnapshot_status\x18\x04 \x01(\t\x12\x15\n\rsnapshot_type\x18\x05 \x01(\t\x1av\n\x06VMInfo\x12Q\n\x07\x63luster\x18\x01 \x01(\x0b\x32@.cohesity.magneto.kvm.rest.SnapshotInfoResult.VMInfo.ClusterInfo\x1a\x19\n\x0b\x43lusterInfo\x12\n\n\x02id\x18\x01 \x01(\t\" \n\x0fSnapshotListArg\x12\r\n\x05vm_id\x18\x01 \x01(\t\"U\n\x12SnapshotListResult\x12?\n\x08snapshot\x18\x01 \x03(\x0b\x32-.cohesity.magneto.kvm.rest.SnapshotInfoResult\"Z\n\x11\x43reateSnapshotArg\x12\x13\n\x0b\x64\x65scription\x18\x01 \x01(\t\x12\x30\n\x13persist_memorystate\x18\x02 \x01(\x08R\x13persist_memorystate\"7\n\x14\x43reateSnapshotResult\x12\n\n\x02id\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\"b\n\x0e\x43reateVMNicArg\x12\x14\n\x05vm_id\x18\x01 \x01(\tR\x05vm_id\x12:\n\x08nic_conf\x18\x02 \x01(\x0b\x32\x1e.cohesity.magneto.kvm.rest.NicR\x08nic_conf\"\x88\x01\n\x17\x43reateDiskAttachmentArg\x12\x14\n\x05vm_id\x18\x01 \x01(\tR\x05vm_id\x12W\n\x0f\x61ttachment_conf\x18\x02 \x01(\x0b\x32-.cohesity.magneto.kvm.rest.DiskAttachmentConfR\x0f\x61ttachment_conf\"\xaf\x01\n\x12\x44iskAttachmentConf\x12\x17\n\x08\x62ootable\x18\x01 \x01(\x08:\x05\x66\x61lse\x12\x14\n\x06\x61\x63tive\x18\x02 \x01(\x08:\x04true\x12\x19\n\tinterface\x18\x03 \x01(\t:\x06virtio\x12\x1c\n\tread_only\x18\x04 \x01(\x08R\tread_only\x12\x31\n\x04\x64isk\x18\x05 \x01(\x0b\x32#.cohesity.magneto.kvm.rest.DiskInfo\"\x0f\n\rPowerStateArg\"\x8d\x01\n\x10PowerStateResult\x12@\n\x05\x66\x61ult\x18\x01 \x01(\x0b\x32\x31.cohesity.magneto.kvm.rest.PowerStateResult.Fault\x12\x0e\n\x06status\x18\x02 \x01(\t\x1a\'\n\x05\x46\x61ult\x12\x0e\n\x06\x64\x65tail\x18\x01 \x01(\t\x12\x0e\n\x06reason\x18\x02 \x01(\t\"-\n\rVMDiskListArg\x12\r\n\x05vm_id\x18\x01 \x01(\t\x12\r\n\x05\x64\x63_id\x18\x02 \x01(\t\"\"\n\x11\x44iskAttachmentArg\x12\r\n\x05vm_id\x18\x01 \x01(\t\"^\n\x14\x44iskAttachmentResult\x12\x46\n\x0f\x64isk_attachment\x18\x01 \x03(\x0b\x32-.cohesity.magneto.kvm.rest.DiskAttachmentConf')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'magneto.connectors.kvm.kvm_rest_api_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_DISKINFO'].fields_by_name['actual_size']._loaded_options = None
  _globals['_DISKINFO'].fields_by_name['actual_size']._serialized_options = b'0\002'
  _globals['_DISKINFO'].fields_by_name['provisioned_size']._loaded_options = None
  _globals['_DISKINFO'].fields_by_name['provisioned_size']._serialized_options = b'0\002'
  _globals['_TOKENRESULT']._serialized_start=72
  _globals['_TOKENRESULT']._serialized_end=107
  _globals['_ERRORCONTEXT']._serialized_start=109
  _globals['_ERRORCONTEXT']._serialized_end=155
  _globals['_CLUSTER']._serialized_start=157
  _globals['_CLUSTER']._serialized_end=192
  _globals['_OSINFO']._serialized_start=195
  _globals['_OSINFO']._serialized_end=371
  _globals['_OSINFO_BOOT']._serialized_start=273
  _globals['_OSINFO_BOOT']._serialized_end=371
  _globals['_OSINFO_BOOT_DEVICES']._serialized_start=346
  _globals['_OSINFO_BOOT_DEVICES']._serialized_end=371
  _globals['_VMINFO']._serialized_start=374
  _globals['_VMINFO']._serialized_end=1636
  _globals['_VMINFO_CPU']._serialized_start=1191
  _globals['_VMINFO_CPU']._serialized_end=1323
  _globals['_VMINFO_CPU_TOPOLOGY']._serialized_start=1264
  _globals['_VMINFO_CPU_TOPOLOGY']._serialized_end=1323
  _globals['_VMINFO_TEMPLATE']._serialized_start=1325
  _globals['_VMINFO_TEMPLATE']._serialized_end=1349
  _globals['_VMINFO_HOST']._serialized_start=1351
  _globals['_VMINFO_HOST']._serialized_end=1369
  _globals['_VMINFO_MEMORYPOLICY']._serialized_start=1371
  _globals['_VMINFO_MEMORYPOLICY']._serialized_end=1418
  _globals['_VMINFO_HIGHAVAILABILITY']._serialized_start=1420
  _globals['_VMINFO_HIGHAVAILABILITY']._serialized_end=1473
  _globals['_VMINFO_TIMEZONE']._serialized_start=1475
  _globals['_VMINFO_TIMEZONE']._serialized_end=1499
  _globals['_VMINFO_INITIALIZATION']._serialized_start=1502
  _globals['_VMINFO_INITIALIZATION']._serialized_end=1636
  _globals['_VMINFO_INITIALIZATION_CONFIGURATION']._serialized_start=1607
  _globals['_VMINFO_INITIALIZATION_CONFIGURATION']._serialized_end=1636
  _globals['_HOSTCONFIG']._serialized_start=1639
  _globals['_HOSTCONFIG']._serialized_end=1826
  _globals['_HOSTCONFIG_SPM']._serialized_start=1805
  _globals['_HOSTCONFIG_SPM']._serialized_end=1826
  _globals['_HOSTLISTRESULT']._serialized_start=1828
  _globals['_HOSTLISTRESULT']._serialized_end=1897
  _globals['_DATACENTER']._serialized_start=1899
  _globals['_DATACENTER']._serialized_end=1923
  _globals['_VMLISTRESULT']._serialized_start=1925
  _globals['_VMLISTRESULT']._serialized_end=1986
  _globals['_NETWORKCONFIG']._serialized_start=1988
  _globals['_NETWORKCONFIG']._serialized_end=2110
  _globals['_NETWORKLISTRESULT']._serialized_start=2112
  _globals['_NETWORKLISTRESULT']._serialized_end=2190
  _globals['_CLUSTERCONFIG']._serialized_start=2192
  _globals['_CLUSTERCONFIG']._serialized_end=2293
  _globals['_CLUSTERLISTRESULT']._serialized_start=2295
  _globals['_CLUSTERLISTRESULT']._serialized_end=2373
  _globals['_MACPOOL']._serialized_start=2375
  _globals['_MACPOOL']._serialized_end=2410
  _globals['_MACPOOLSLISTRESULT']._serialized_start=2412
  _globals['_MACPOOLSLISTRESULT']._serialized_end=2486
  _globals['_STORAGEDOMAINCONFIG']._serialized_start=2489
  _globals['_STORAGEDOMAINCONFIG']._serialized_end=2777
  _globals['_STORAGEDOMAINCONFIG_DATACENTERLIST']._serialized_start=2640
  _globals['_STORAGEDOMAINCONFIG_DATACENTERLIST']._serialized_end=2777
  _globals['_STORAGEDOMAINCONFIG_DATACENTERLIST_DATACENTER']._serialized_start=1899
  _globals['_STORAGEDOMAINCONFIG_DATACENTERLIST_DATACENTER']._serialized_end=1923
  _globals['_STORAGEDOMAINLISTRESULT']._serialized_start=2779
  _globals['_STORAGEDOMAINLISTRESULT']._serialized_end=2876
  _globals['_DATACENTERCONFIG']._serialized_start=2878
  _globals['_DATACENTERCONFIG']._serialized_end=2922
  _globals['_DATACENTERLISTRESULT']._serialized_start=2924
  _globals['_DATACENTERLISTRESULT']._serialized_end=3012
  _globals['_VNICPROFILE']._serialized_start=3014
  _globals['_VNICPROFILE']._serialized_end=3141
  _globals['_VNICPROFILE_NETWORK']._serialized_start=3120
  _globals['_VNICPROFILE_NETWORK']._serialized_end=3141
  _globals['_VNICPROFILELIST']._serialized_start=3143
  _globals['_VNICPROFILELIST']._serialized_end=3236
  _globals['_VMNICLISTARG']._serialized_start=3238
  _globals['_VMNICLISTARG']._serialized_end=3267
  _globals['_NIC']._serialized_start=3270
  _globals['_NIC']._serialized_end=3917
  _globals['_NIC_MAC']._serialized_start=3580
  _globals['_NIC_MAC']._serialized_end=3602
  _globals['_NIC_DEVICES']._serialized_start=3605
  _globals['_NIC_DEVICES']._serialized_end=3917
  _globals['_NIC_DEVICES_DEVICE']._serialized_start=3706
  _globals['_NIC_DEVICES_DEVICE']._serialized_end=3917
  _globals['_NIC_DEVICES_DEVICE_IPS']._serialized_start=3806
  _globals['_NIC_DEVICES_DEVICE_IPS']._serialized_end=3917
  _globals['_NIC_DEVICES_DEVICE_IPS_IP']._serialized_start=3879
  _globals['_NIC_DEVICES_DEVICE_IPS_IP']._serialized_end=3917
  _globals['_VMNICLISTRESULT']._serialized_start=3919
  _globals['_VMNICLISTRESULT']._serialized_end=3981
  _globals['_HOSTNICARG']._serialized_start=3983
  _globals['_HOSTNICARG']._serialized_end=4012
  _globals['_HOSTNICRESULT']._serialized_start=4015
  _globals['_HOSTNICRESULT']._serialized_end=4246
  _globals['_HOSTNICRESULT_HOSTNIC']._serialized_start=4101
  _globals['_HOSTNICRESULT_HOSTNIC']._serialized_end=4246
  _globals['_HOSTNICRESULT_HOSTNIC_IP']._serialized_start=4191
  _globals['_HOSTNICRESULT_HOSTNIC_IP']._serialized_end=4246
  _globals['_OVIRTCONFIG']._serialized_start=4249
  _globals['_OVIRTCONFIG']._serialized_end=4544
  _globals['_OVIRTCONFIG_PRODUCTINFO']._serialized_start=4339
  _globals['_OVIRTCONFIG_PRODUCTINFO']._serialized_end=4544
  _globals['_OVIRTCONFIG_PRODUCTINFO_VERSION']._serialized_start=4445
  _globals['_OVIRTCONFIG_PRODUCTINFO_VERSION']._serialized_end=4544
  _globals['_DISKINFOARG']._serialized_start=4546
  _globals['_DISKINFOARG']._serialized_end=4579
  _globals['_DISKINFO']._serialized_start=4582
  _globals['_DISKINFO']._serialized_end=5142
  _globals['_DISKINFO_STORAGEDOMAINS']._serialized_start=4977
  _globals['_DISKINFO_STORAGEDOMAINS']._serialized_end=5142
  _globals['_DISKINFO_STORAGEDOMAINS_STORAGEDOMAIN']._serialized_start=5101
  _globals['_DISKINFO_STORAGEDOMAINS_STORAGEDOMAIN']._serialized_end=5142
  _globals['_DISKINFORESULT']._serialized_start=5144
  _globals['_DISKINFORESULT']._serialized_end=5211
  _globals['_WAITFORJOBARG']._serialized_start=5213
  _globals['_WAITFORJOBARG']._serialized_end=5272
  _globals['_WAITFORJOBRESULT']._serialized_start=5274
  _globals['_WAITFORJOBRESULT']._serialized_end=5341
  _globals['_POLLEVENTARG']._serialized_start=5343
  _globals['_POLLEVENTARG']._serialized_end=5447
  _globals['_POLLEVENTRESULT']._serialized_start=5450
  _globals['_POLLEVENTRESULT']._serialized_end=5618
  _globals['_POLLEVENTRESULT_EVENT']._serialized_start=5534
  _globals['_POLLEVENTRESULT_EVENT']._serialized_end=5618
  _globals['_JOBINFO']._serialized_start=5620
  _globals['_JOBINFO']._serialized_end=5717
  _globals['_JOBINFO_JOB']._serialized_start=5700
  _globals['_JOBINFO_JOB']._serialized_end=5717
  _globals['_SNAPSHOTINFORESULT']._serialized_start=5720
  _globals['_SNAPSHOTINFORESULT']._serialized_end=6007
  _globals['_SNAPSHOTINFORESULT_VMINFO']._serialized_start=5889
  _globals['_SNAPSHOTINFORESULT_VMINFO']._serialized_end=6007
  _globals['_SNAPSHOTINFORESULT_VMINFO_CLUSTERINFO']._serialized_start=5982
  _globals['_SNAPSHOTINFORESULT_VMINFO_CLUSTERINFO']._serialized_end=6007
  _globals['_SNAPSHOTLISTARG']._serialized_start=6009
  _globals['_SNAPSHOTLISTARG']._serialized_end=6041
  _globals['_SNAPSHOTLISTRESULT']._serialized_start=6043
  _globals['_SNAPSHOTLISTRESULT']._serialized_end=6128
  _globals['_CREATESNAPSHOTARG']._serialized_start=6130
  _globals['_CREATESNAPSHOTARG']._serialized_end=6220
  _globals['_CREATESNAPSHOTRESULT']._serialized_start=6222
  _globals['_CREATESNAPSHOTRESULT']._serialized_end=6277
  _globals['_CREATEVMNICARG']._serialized_start=6279
  _globals['_CREATEVMNICARG']._serialized_end=6377
  _globals['_CREATEDISKATTACHMENTARG']._serialized_start=6380
  _globals['_CREATEDISKATTACHMENTARG']._serialized_end=6516
  _globals['_DISKATTACHMENTCONF']._serialized_start=6519
  _globals['_DISKATTACHMENTCONF']._serialized_end=6694
  _globals['_POWERSTATEARG']._serialized_start=6696
  _globals['_POWERSTATEARG']._serialized_end=6711
  _globals['_POWERSTATERESULT']._serialized_start=6714
  _globals['_POWERSTATERESULT']._serialized_end=6855
  _globals['_POWERSTATERESULT_FAULT']._serialized_start=6816
  _globals['_POWERSTATERESULT_FAULT']._serialized_end=6855
  _globals['_VMDISKLISTARG']._serialized_start=6857
  _globals['_VMDISKLISTARG']._serialized_end=6902
  _globals['_DISKATTACHMENTARG']._serialized_start=6904
  _globals['_DISKATTACHMENTARG']._serialized_end=6938
  _globals['_DISKATTACHMENTRESULT']._serialized_start=6940
  _globals['_DISKATTACHMENTRESULT']._serialized_end=7034
# @@protoc_insertion_point(module_scope)