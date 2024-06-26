# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: magneto/connectors/acropolis/v2_rest_api.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.magneto/connectors/acropolis/v2_rest_api.proto\x12\x1d\x63ohesity.magneto.acropolis.v2\"\xab\x01\n\tErrorInfo\x12\x46\n\nerror_code\x18\x01 \x01(\x0b\x32\x32.cohesity.magneto.acropolis.v2.ErrorInfo.ErrorCode\x12\x18\n\x10\x64\x65tailed_message\x18\x02 \x01(\t\x12\x0f\n\x07message\x18\x03 \x01(\t\x1a+\n\tErrorCode\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x10\n\x08help_url\x18\x02 \x01(\t\":\n\x14\x43reateSessionRequest\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\"K\n\x15\x43reateSessionResponse\x12\x18\n\x10timeout_absolute\x18\x01 \x01(\x05\x12\x18\n\x10timeout_inactive\x18\x02 \x01(\x05\"\x9e\x01\n\x0cListMetadata\x12\x16\n\x0etotal_entities\x18\x01 \x01(\x05\x12\r\n\x05\x63ount\x18\x02 \x01(\x05\x12\x1c\n\x14grand_total_entities\x18\x03 \x01(\x05\x12\x13\n\x0bnext_cursor\x18\x04 \x01(\t\x12\x0c\n\x04page\x18\x05 \x01(\x05\x12\x11\n\tend_index\x18\x06 \x01(\x05\x12\x13\n\x0bstart_index\x18\x07 \x01(\x05\"\x86\x03\n\x04Task\x12\x14\n\x0c\x64isplay_name\x18\x01 \x01(\t\x12\x17\n\x0fprogress_status\x18\x02 \x01(\t\x12\x18\n\x10start_time_usecs\x18\x03 \x01(\x03\x12\x14\n\x0c\x63luster_uuid\x18\x05 \x01(\t\x12\x0c\n\x04uuid\x18\x06 \x01(\t\x12\x43\n\x0b\x65ntity_list\x18\x07 \x03(\x0b\x32..cohesity.magneto.acropolis.v2.Task.TaskEntity\x12G\n\rmeta_response\x18\x08 \x01(\x0b\x32\x30.cohesity.magneto.acropolis.v2.Task.MetaResponse\x1aI\n\nTaskEntity\x12\x11\n\tentity_id\x18\x01 \x01(\t\x12\x13\n\x0b\x65ntity_name\x18\x02 \x01(\t\x12\x13\n\x0b\x65ntity_type\x18\x03 \x01(\t\x1a\x38\n\x0cMetaResponse\x12\x12\n\nerror_code\x18\x01 \x01(\x05\x12\x14\n\x0c\x65rror_detail\x18\x02 \x01(\t\"c\n\x0bTaskPollArg\x12(\n\x0f\x63ompleted_tasks\x18\x01 \x03(\tR\x0f\x63ompleted_tasks\x12*\n\x10timeout_interval\x18\x02 \x01(\x05R\x10timeout_interval\"f\n\x0eTaskPollResult\x12\x11\n\ttimed_out\x18\x01 \x01(\x08\x12\x41\n\x14\x63ompleted_tasks_info\x18\x02 \x03(\x0b\x32#.cohesity.magneto.acropolis.v2.Task\"\xf4\x01\n\x05VMNic\x12\"\n\x0cnetwork_uuid\x18\x01 \x01(\tR\x0cnetwork_uuid\x12 \n\x0bmac_address\x18\x02 \x01(\tR\x0bmac_address\x12\x1e\n\nrequest_ip\x18\x03 \x01(\x08R\nrequest_ip\x12\x32\n\x14requested_ip_address\x18\x04 \x01(\tR\x14requested_ip_address\x12\r\n\x05model\x18\x05 \x01(\t\x12\x1e\n\nip_address\x18\x06 \x01(\tR\nip_address\x12\"\n\x0cis_connected\x18\x07 \x01(\x08R\x0cis_connected\"\xa5\x02\n\x0b\x44iskAddress\x12$\n\rndfs_filepath\x18\x01 \x01(\tR\rndfs_filepath\x12 \n\x0bvmdisk_uuid\x18\x02 \x01(\tR\x0bvmdisk_uuid\x12,\n\x11volume_group_uuid\x18\x03 \x01(\tR\x11volume_group_uuid\x12\"\n\x0c\x64\x65vice_index\x18\x04 \x01(\x05R\x0c\x64\x65vice_index\x12\x1e\n\ndisk_label\x18\x05 \x01(\tR\ndisk_label\x12\x1e\n\ndevice_bus\x18\x06 \x01(\tR\ndevice_bus\x12 \n\x0b\x64\x65vice_uuid\x18\x07 \x01(\tR\x0b\x64\x65vice_uuid\x12\x1a\n\x08is_cdrom\x18\x08 \x01(\x08R\x08is_cdrom\"\xfb\x04\n\x04\x44isk\x12N\n\x0c\x64isk_address\x18\x01 \x01(\x0b\x32*.cohesity.magneto.acropolis.v2.DiskAddressR\x0c\x64isk_address\x12P\n\rvm_disk_clone\x18\x02 \x01(\x0b\x32*.cohesity.magneto.acropolis.v2.VMDiskCloneR\rvm_disk_clone\x12S\n\x0evm_disk_create\x18\x03 \x01(\x0b\x32+.cohesity.magneto.acropolis.v2.VMDiskCreateR\x0evm_disk_create\x12\x1a\n\x08is_cdrom\x18\x04 \x01(\x08R\x08is_cdrom\x12\x30\n\x13is_scsi_passthrough\x18\x05 \x01(\x08R\x13is_scsi_passthrough\x12\x1a\n\x08is_empty\x18\x06 \x01(\x08R\x08is_empty\x12\x0c\n\x04size\x18\x07 \x01(\x03\x12\x1e\n\x16storage_container_uuid\x18\x08 \x01(\t\x12\x1e\n\x16storage_container_name\x18\t \x01(\t\x12.\n\x12\x66lash_mode_enabled\x18\n \x01(\x08R\x12\x66lash_mode_enabled\x12(\n\x0f\x64\x61tasource_uuid\x18\x0b \x01(\tR\x0f\x64\x61tasource_uuid\x12j\n\x16vm_disk_clone_external\x18\x0c \x01(\x0b\x32\x32.cohesity.magneto.acropolis.v2.VMDiskCloneExternalR\x16vm_disk_clone_external\":\n\x08\x41\x66\x66inity\x12\x0e\n\x06policy\x18\x01 \x01(\t\x12\x1e\n\nhost_uuids\x18\x02 \x03(\tR\nhost_uuids\"\xc6\x0e\n\x08VMConfig\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04uuid\x18\x02 \x01(\t\x12.\n\x12num_cores_per_vcpu\x18\x03 \x01(\x05R\x12num_cores_per_vcpu\x12\x1c\n\tnum_vcpus\x18\x04 \x01(\x05R\tnum_vcpus\x12\x1c\n\tmemory_mb\x18\x05 \x01(\x05R\tmemory_mb\x12\x34\n\x15memory_reservation_mb\x18\x06 \x01(\x05R\x15memory_reservation_mb\x12>\n\x07vm_nics\x18\x07 \x03(\x0b\x32$.cohesity.magneto.acropolis.v2.VMNicR\x07vm_nics\x12G\n\x0cvm_disk_info\x18\x08 \x03(\x0b\x32#.cohesity.magneto.acropolis.v2.DiskR\x0cvm_disk_info\x12\x10\n\x08timezone\x18\t \x01(\t\x12M\n\x07vm_gpus\x18\n \x03(\x0b\x32\x33.cohesity.magneto.acropolis.v2.VMConfig.VMGpuConfigR\x07vm_gpus\x12 \n\x0bpower_state\x18\x0b \x01(\tR\x0bpower_state\x12\x30\n\x13vcpu_reservation_hz\x18\r \x01(\x03R\x13vcpu_reservation_hz\x12.\n\x12\x61llow_live_migrate\x18\x0e \x01(\x08R\x12\x61llow_live_migrate\x12@\n\x04\x62oot\x18\x0f \x01(\x0b\x32\x32.cohesity.magneto.acropolis.v2.VMConfig.BootConfig\x12Y\n\x0bvm_features\x18\x10 \x01(\x0b\x32\x37.cohesity.magneto.acropolis.v2.VMConfig.vm_feature_listR\x0bvm_features\x12\x1c\n\thost_uuid\x18\x11 \x01(\tR\thost_uuid\x12\x39\n\x08\x61\x66\x66inity\x18\x12 \x01(\x0b\x32\'.cohesity.magneto.acropolis.v2.Affinity\x12$\n\rgpus_assigned\x18\x13 \x01(\x08R\rgpus_assigned\x12 \n\x0b\x64\x65scription\x18\x14 \x01(\tR\x0b\x64\x65scription\x1a\x8d\x05\n\x0bVMGpuConfig\x12\x16\n\x06in_use\x18\x01 \x01(\x08R\x06in_use\x12 \n\x0b\x64\x65vice_name\x18\x02 \x01(\tR\x0b\x64\x65vice_name\x12\x1c\n\tdevice_id\x18\x03 \x01(\x05R\tdevice_id\x12\x1e\n\nassignable\x18\x04 \x01(\x08R\nassignable\x12\x1a\n\x08\x66raction\x18\x05 \x01(\x05R\x08\x66raction\x12\x38\n\x17\x66rame_buffer_size_bytes\x18\x06 \x01(\x03R\x17\x66rame_buffer_size_bytes\x12\x1a\n\x08gpu_mode\x18\x07 \x01(\tR\x08gpu_mode\x12 \n\x0bgpu_profile\x18\x08 \x01(\tR\x0bgpu_profile\x12\x1a\n\x08gpu_type\x18\t \x01(\tR\x08gpu_type\x12\x1e\n\ngpu_vendor\x18\n \x01(\tR\ngpu_vendor\x12\x32\n\x14guest_driver_version\x18\x0b \x01(\tR\x14guest_driver_version\x12\x32\n\x14max_instances_per_vm\x18\x0c \x01(\x05R\x14max_instances_per_vm\x12&\n\x0emax_resolution\x18\r \x01(\tR\x0emax_resolution\x12<\n\x19num_virtual_display_heads\x18\x0e \x01(\x05R\x19num_virtual_display_heads\x12\x1c\n\tnuma_node\x18\x0f \x01(\x05R\tnuma_node\x12\x12\n\x04sbdf\x18\x10 \x01(\tR\x04sbdf\x12\x1a\n\x08licenses\x18\x11 \x03(\tR\x08licenses\x12\x1a\n\x08vm_uuids\x18\x12 \x03(\tR\x08vm_uuids\x1a\xf0\x01\n\nBootConfig\x12*\n\x10\x62oot_device_type\x18\x01 \x01(\tR\x10\x62oot_device_type\x12\x1a\n\x08mac_addr\x18\x02 \x01(\tR\x08mac_addr\x12N\n\x0c\x64isk_address\x18\x03 \x01(\x0b\x32*.cohesity.magneto.acropolis.v2.DiskAddressR\x0c\x64isk_address\x12\x1c\n\tuefi_boot\x18\x04 \x01(\x08R\tuefi_boot\x12,\n\x11\x62oot_device_order\x18\x05 \x03(\tR\x11\x62oot_device_order\x1aM\n\x0fvm_feature_list\x12\x1a\n\x08\x61gent_vm\x18\x01 \x01(\x08R\x08\x41GENT_VM\x12\x1e\n\nflash_mode\x18\x02 \x01(\x08R\nFLASH_MODE\"\xb6\x0e\n\x0e\x43reateVMConfig\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04uuid\x18\x02 \x01(\t\x12.\n\x12num_cores_per_vcpu\x18\x03 \x01(\x05R\x12num_cores_per_vcpu\x12\x1c\n\tnum_vcpus\x18\x04 \x01(\x05R\tnum_vcpus\x12\x1c\n\tmemory_mb\x18\x05 \x01(\x05R\tmemory_mb\x12\x34\n\x15memory_reservation_mb\x18\x06 \x01(\x05R\x15memory_reservation_mb\x12>\n\x07vm_nics\x18\x07 \x03(\x0b\x32$.cohesity.magneto.acropolis.v2.VMNicR\x07vm_nics\x12?\n\x08vm_disks\x18\x08 \x03(\x0b\x32#.cohesity.magneto.acropolis.v2.DiskR\x08vm_disks\x12\x10\n\x08timezone\x18\t \x01(\t\x12S\n\x07vm_gpus\x18\n \x03(\x0b\x32\x39.cohesity.magneto.acropolis.v2.CreateVMConfig.VMGpuConfigR\x07vm_gpus\x12 \n\x0bpower_state\x18\x0b \x01(\tR\x0bpower_state\x12\x30\n\x13vcpu_reservation_hz\x18\r \x01(\x03R\x13vcpu_reservation_hz\x12.\n\x12\x61llow_live_migrate\x18\x0e \x01(\x08R\x12\x61llow_live_migrate\x12\x46\n\x04\x62oot\x18\x0f \x01(\x0b\x32\x38.cohesity.magneto.acropolis.v2.CreateVMConfig.BootConfig\x12_\n\x0bvm_features\x18\x10 \x01(\x0b\x32=.cohesity.magneto.acropolis.v2.CreateVMConfig.vm_feature_listR\x0bvm_features\x12\x1c\n\thost_uuid\x18\x11 \x01(\tR\thost_uuid\x12\x39\n\x08\x61\x66\x66inity\x18\x12 \x01(\x0b\x32\'.cohesity.magneto.acropolis.v2.Affinity\x12$\n\rgpus_assigned\x18\x13 \x01(\x08R\rgpus_assigned\x12 \n\x0b\x64\x65scription\x18\x14 \x01(\tR\x0b\x64\x65scription\x1a\x8d\x05\n\x0bVMGpuConfig\x12\x16\n\x06in_use\x18\x01 \x01(\x08R\x06in_use\x12 \n\x0b\x64\x65vice_name\x18\x02 \x01(\tR\x0b\x64\x65vice_name\x12\x1c\n\tdevice_id\x18\x03 \x01(\x05R\tdevice_id\x12\x1e\n\nassignable\x18\x04 \x01(\x08R\nassignable\x12\x1a\n\x08\x66raction\x18\x05 \x01(\x05R\x08\x66raction\x12\x38\n\x17\x66rame_buffer_size_bytes\x18\x06 \x01(\x03R\x17\x66rame_buffer_size_bytes\x12\x1a\n\x08gpu_mode\x18\x07 \x01(\tR\x08gpu_mode\x12 \n\x0bgpu_profile\x18\x08 \x01(\tR\x0bgpu_profile\x12\x1a\n\x08gpu_type\x18\t \x01(\tR\x08gpu_type\x12\x1e\n\ngpu_vendor\x18\n \x01(\tR\ngpu_vendor\x12\x32\n\x14guest_driver_version\x18\x0b \x01(\tR\x14guest_driver_version\x12\x32\n\x14max_instances_per_vm\x18\x0c \x01(\x05R\x14max_instances_per_vm\x12&\n\x0emax_resolution\x18\r \x01(\tR\x0emax_resolution\x12<\n\x19num_virtual_display_heads\x18\x0e \x01(\x05R\x19num_virtual_display_heads\x12\x1c\n\tnuma_node\x18\x0f \x01(\x05R\tnuma_node\x12\x12\n\x04sbdf\x18\x10 \x01(\tR\x04sbdf\x12\x1a\n\x08licenses\x18\x11 \x03(\tR\x08licenses\x12\x1a\n\x08vm_uuids\x18\x12 \x03(\tR\x08vm_uuids\x1a\xf0\x01\n\nBootConfig\x12*\n\x10\x62oot_device_type\x18\x01 \x01(\tR\x10\x62oot_device_type\x12\x1a\n\x08mac_addr\x18\x02 \x01(\tR\x08mac_addr\x12N\n\x0c\x64isk_address\x18\x03 \x01(\x0b\x32*.cohesity.magneto.acropolis.v2.DiskAddressR\x0c\x64isk_address\x12\x1c\n\tuefi_boot\x18\x04 \x01(\x08R\tuefi_boot\x12,\n\x11\x62oot_device_order\x18\x05 \x03(\tR\x11\x62oot_device_order\x1a-\n\x0fvm_feature_list\x12\x1a\n\x08\x61gent_vm\x18\x01 \x01(\x08R\x08\x41GENT_VM\"#\n\x0e\x43reateVMResult\x12\x11\n\ttask_uuid\x18\x01 \x01(\t\"\xc6\x01\n\x0cVMListResult\x12\x39\n\x08\x65ntities\x18\x01 \x03(\x0b\x32\'.cohesity.magneto.acropolis.v2.VMConfig\x12=\n\x08metadata\x18\x02 \x01(\x0b\x32+.cohesity.magneto.acropolis.v2.ListMetadata\x12<\n\nerror_info\x18\x03 \x01(\x0b\x32(.cohesity.magneto.acropolis.v2.ErrorInfo\"^\n\x0cVMDiskCreate\x12\x36\n\x16storage_container_uuid\x18\x01 \x01(\tR\x16storage_container_uuid\x12\x16\n\x04size\x18\x02 \x01(\x03\x42\x02\x30\x02R\x04size\"\xbd\x01\n\x0bVMDiskClone\x12\x36\n\x16storage_container_uuid\x18\x01 \x01(\tR\x16storage_container_uuid\x12&\n\x0cminimum_size\x18\x02 \x01(\x03\x42\x02\x30\x02R\x0cminimum_size\x12N\n\x0c\x64isk_address\x18\x03 \x01(\x0b\x32*.cohesity.magneto.acropolis.v2.DiskAddressR\x0c\x64isk_address\"{\n\x13VMDiskCloneExternal\x12,\n\x11\x65xternal_disk_url\x18\x01 \x01(\tR\x11\x65xternal_disk_url\x12\x36\n\x16storage_container_uuid\x18\x02 \x01(\tR\x16storage_container_uuid\"\xf0\x01\n\x0eVolumeDiskSpec\x12,\n\x11volume_group_uuid\x18\x01 \x01(\tR\x11volume_group_uuid\x12Q\n\rcreate_config\x18\x02 \x01(\x0b\x32+.cohesity.magneto.acropolis.v2.VMDiskCreateR\rcreate_config\x12N\n\x0c\x63lone_config\x18\x03 \x01(\x0b\x32*.cohesity.magneto.acropolis.v2.VMDiskCloneR\x0c\x63lone_config\x12\r\n\x05index\x18\x04 \x01(\x05\"5\n\x0bIscsiClient\x12&\n\x0e\x63lient_address\x18\x02 \x01(\tR\x0e\x63lient_address\"\xbd\x02\n\x14\x43reateVolumeGroupArg\x12\x0c\n\x04uuid\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x14\n\x0ciscsi_target\x18\x03 \x01(\t\x12\x30\n\x13iscsi_target_prefix\x18\x04 \x01(\tR\x13iscsi_target_prefix\x12K\n\tdisk_list\x18\x05 \x03(\x0b\x32-.cohesity.magneto.acropolis.v2.VolumeDiskSpecR\tdisk_list\x12V\n\x10\x61ttached_clients\x18\x06 \x03(\x0b\x32*.cohesity.magneto.acropolis.v2.IscsiClientR\x10\x61ttached_clients\x12\x1c\n\tis_shared\x18\x07 \x01(\x08R\tis_shared\",\n\x17\x43reateVolumeGroupResult\x12\x11\n\ttask_uuid\x18\x01 \x01(\t\",\n\x17\x44\x65leteVolumeGroupResult\x12\x11\n\ttask_uuid\x18\x01 \x01(\t\"4\n\nScsiClient\x12&\n\x0e\x63lient_address\x18\x01 \x01(\tR\x0e\x63lient_address\"\xcb\x01\n\x14UpdateVolumeGroupArg\x12U\n\x10\x61ttached_clients\x18\x02 \x03(\x0b\x32).cohesity.magneto.acropolis.v2.ScsiClientR\x10\x61ttached_clients\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x30\n\x13iscsi_target_prefix\x18\x04 \x01(\tR\x13iscsi_target_prefix\x12\x1c\n\tis_shared\x18\x05 \x01(\x08R\tis_shared\"d\n\x13\x43loseVolumeGroupArg\x12M\n\x0ciscsi_client\x18\x01 \x01(\x0b\x32).cohesity.magneto.acropolis.v2.ScsiClientR\x0ciscsi_client\"\'\n\x16\x43loseVolumeGroupResult\x12\r\n\x05value\x18\x01 \x01(\x08\"\xc7\x03\n\x15VolumeGroupInfoResult\x12\x0c\n\x04uuid\x18\x01 \x01(\t\x12\x12\n\nis_deleted\x18\x02 \x01(\x08\x12X\n\x0f\x61ttachment_list\x18\x03 \x03(\x0b\x32?.cohesity.magneto.acropolis.v2.VolumeGroupInfoResult.Initiators\x12\x14\n\x0ciscsi_target\x18\x04 \x01(\t\x12\x0c\n\x04name\x18\x05 \x01(\t\x12V\n\tdisk_list\x18\x06 \x03(\x0b\x32\x43.cohesity.magneto.acropolis.v2.VolumeGroupInfoResult.VolumeDiskList\x1aH\n\nInitiators\x12\x1c\n\x14initiator_ip_address\x18\x01 \x01(\t\x12\x1c\n\x14iscsi_initiator_name\x18\x02 \x01(\t\x1al\n\x0eVolumeDiskList\x12\r\n\x05index\x18\x01 \x01(\x05\x12\x1e\n\x16storage_container_uuid\x18\x02 \x01(\t\x12\x13\n\x0bvmdisk_uuid\x18\x03 \x01(\t\x12\x16\n\x0evmdisk_size_mb\x18\x04 \x01(\x03\"\xf9\x01\n\rClusterConfig\x12\x14\n\x0cmulticluster\x18\x01 \x01(\x08\x12\x14\n\x0c\x63luster_uuid\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x30\n(cluster_external_data_services_ipaddress\x18\x04 \x01(\t\x12\x0f\n\x07version\x18\x05 \x01(\t\x12\x18\n\x10hypervisor_types\x18\x06 \x03(\t\x12Q\n\x12management_servers\x18\x07 \x03(\x0b\x32\x35.cohesity.magneto.acropolis.v2.ManagementServerConfig\"p\n\x16ManagementServerConfig\x12\x1e\n\nip_address\x18\x01 \x01(\tR\nip_address\x12\x36\n\x16management_server_type\x18\x02 \x01(\tR\x16management_server_type\"\x81\x01\n\tContainer\x12\x1e\n\x16storage_container_uuid\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x14\n\x0cmax_capacity\x18\x03 \x01(\x03\x12\x1a\n\x12marked_for_removal\x18\x04 \x01(\x08\x12\x14\n\x0c\x63luster_uuid\x18\x05 \x01(\t\"\xce\x01\n\x13\x43ontainerListResult\x12:\n\x08\x65ntities\x18\x01 \x03(\x0b\x32(.cohesity.magneto.acropolis.v2.Container\x12=\n\x08metadata\x18\x02 \x01(\x0b\x32+.cohesity.magneto.acropolis.v2.ListMetadata\x12<\n\nerror_info\x18\x03 \x01(\x0b\x32(.cohesity.magneto.acropolis.v2.ErrorInfo\"<\n\x08IPConfig\x12\x17\n\x0fnetwork_address\x18\x01 \x01(\t\x12\x17\n\x0f\x64\x65\x66\x61ult_gateway\x18\x02 \x01(\t\"a\n\x07Network\x12\x0c\n\x04uuid\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12:\n\tip_config\x18\x03 \x01(\x0b\x32\'.cohesity.magneto.acropolis.v2.IPConfig\"\xca\x01\n\x11NetworkListResult\x12\x38\n\x08\x65ntities\x18\x01 \x03(\x0b\x32&.cohesity.magneto.acropolis.v2.Network\x12=\n\x08metadata\x18\x02 \x01(\x0b\x32+.cohesity.magneto.acropolis.v2.ListMetadata\x12<\n\nerror_info\x18\x03 \x01(\x0b\x32(.cohesity.magneto.acropolis.v2.ErrorInfo\"\x84\x01\n\x04Host\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04uuid\x18\x02 \x01(\t\x12 \n\x18memory_capacity_in_bytes\x18\x03 \x01(\x03\x12>\n\x1a\x63ontroller_vm_backplane_ip\x18\x04 \x01(\tR\x1a\x63ontroller_vm_backplane_ip\"\xc4\x01\n\x0eHostListResult\x12\x35\n\x08\x65ntities\x18\x01 \x03(\x0b\x32#.cohesity.magneto.acropolis.v2.Host\x12=\n\x08metadata\x18\x02 \x01(\x0b\x32+.cohesity.magneto.acropolis.v2.ListMetadata\x12<\n\nerror_info\x18\x03 \x01(\x0b\x32(.cohesity.magneto.acropolis.v2.ErrorInfo\"6\n\x12SetVMPowerStateArg\x12\x0c\n\x04uuid\x18\x01 \x01(\t\x12\x12\n\ntransition\x18\x02 \x01(\t\"*\n\x15SetVMPowerStateResult\x12\x11\n\ttask_uuid\x18\x01 \x01(\t')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'magneto.connectors.acropolis.v2_rest_api_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_VMDISKCREATE'].fields_by_name['size']._loaded_options = None
  _globals['_VMDISKCREATE'].fields_by_name['size']._serialized_options = b'0\002'
  _globals['_VMDISKCLONE'].fields_by_name['minimum_size']._loaded_options = None
  _globals['_VMDISKCLONE'].fields_by_name['minimum_size']._serialized_options = b'0\002'
  _globals['_ERRORINFO']._serialized_start=82
  _globals['_ERRORINFO']._serialized_end=253
  _globals['_ERRORINFO_ERRORCODE']._serialized_start=210
  _globals['_ERRORINFO_ERRORCODE']._serialized_end=253
  _globals['_CREATESESSIONREQUEST']._serialized_start=255
  _globals['_CREATESESSIONREQUEST']._serialized_end=313
  _globals['_CREATESESSIONRESPONSE']._serialized_start=315
  _globals['_CREATESESSIONRESPONSE']._serialized_end=390
  _globals['_LISTMETADATA']._serialized_start=393
  _globals['_LISTMETADATA']._serialized_end=551
  _globals['_TASK']._serialized_start=554
  _globals['_TASK']._serialized_end=944
  _globals['_TASK_TASKENTITY']._serialized_start=813
  _globals['_TASK_TASKENTITY']._serialized_end=886
  _globals['_TASK_METARESPONSE']._serialized_start=888
  _globals['_TASK_METARESPONSE']._serialized_end=944
  _globals['_TASKPOLLARG']._serialized_start=946
  _globals['_TASKPOLLARG']._serialized_end=1045
  _globals['_TASKPOLLRESULT']._serialized_start=1047
  _globals['_TASKPOLLRESULT']._serialized_end=1149
  _globals['_VMNIC']._serialized_start=1152
  _globals['_VMNIC']._serialized_end=1396
  _globals['_DISKADDRESS']._serialized_start=1399
  _globals['_DISKADDRESS']._serialized_end=1692
  _globals['_DISK']._serialized_start=1695
  _globals['_DISK']._serialized_end=2330
  _globals['_AFFINITY']._serialized_start=2332
  _globals['_AFFINITY']._serialized_end=2390
  _globals['_VMCONFIG']._serialized_start=2393
  _globals['_VMCONFIG']._serialized_end=4255
  _globals['_VMCONFIG_VMGPUCONFIG']._serialized_start=3280
  _globals['_VMCONFIG_VMGPUCONFIG']._serialized_end=3933
  _globals['_VMCONFIG_BOOTCONFIG']._serialized_start=3936
  _globals['_VMCONFIG_BOOTCONFIG']._serialized_end=4176
  _globals['_VMCONFIG_VM_FEATURE_LIST']._serialized_start=4178
  _globals['_VMCONFIG_VM_FEATURE_LIST']._serialized_end=4255
  _globals['_CREATEVMCONFIG']._serialized_start=4258
  _globals['_CREATEVMCONFIG']._serialized_end=6104
  _globals['_CREATEVMCONFIG_VMGPUCONFIG']._serialized_start=3280
  _globals['_CREATEVMCONFIG_VMGPUCONFIG']._serialized_end=3933
  _globals['_CREATEVMCONFIG_BOOTCONFIG']._serialized_start=3936
  _globals['_CREATEVMCONFIG_BOOTCONFIG']._serialized_end=4176
  _globals['_CREATEVMCONFIG_VM_FEATURE_LIST']._serialized_start=4178
  _globals['_CREATEVMCONFIG_VM_FEATURE_LIST']._serialized_end=4223
  _globals['_CREATEVMRESULT']._serialized_start=6106
  _globals['_CREATEVMRESULT']._serialized_end=6141
  _globals['_VMLISTRESULT']._serialized_start=6144
  _globals['_VMLISTRESULT']._serialized_end=6342
  _globals['_VMDISKCREATE']._serialized_start=6344
  _globals['_VMDISKCREATE']._serialized_end=6438
  _globals['_VMDISKCLONE']._serialized_start=6441
  _globals['_VMDISKCLONE']._serialized_end=6630
  _globals['_VMDISKCLONEEXTERNAL']._serialized_start=6632
  _globals['_VMDISKCLONEEXTERNAL']._serialized_end=6755
  _globals['_VOLUMEDISKSPEC']._serialized_start=6758
  _globals['_VOLUMEDISKSPEC']._serialized_end=6998
  _globals['_ISCSICLIENT']._serialized_start=7000
  _globals['_ISCSICLIENT']._serialized_end=7053
  _globals['_CREATEVOLUMEGROUPARG']._serialized_start=7056
  _globals['_CREATEVOLUMEGROUPARG']._serialized_end=7373
  _globals['_CREATEVOLUMEGROUPRESULT']._serialized_start=7375
  _globals['_CREATEVOLUMEGROUPRESULT']._serialized_end=7419
  _globals['_DELETEVOLUMEGROUPRESULT']._serialized_start=7421
  _globals['_DELETEVOLUMEGROUPRESULT']._serialized_end=7465
  _globals['_SCSICLIENT']._serialized_start=7467
  _globals['_SCSICLIENT']._serialized_end=7519
  _globals['_UPDATEVOLUMEGROUPARG']._serialized_start=7522
  _globals['_UPDATEVOLUMEGROUPARG']._serialized_end=7725
  _globals['_CLOSEVOLUMEGROUPARG']._serialized_start=7727
  _globals['_CLOSEVOLUMEGROUPARG']._serialized_end=7827
  _globals['_CLOSEVOLUMEGROUPRESULT']._serialized_start=7829
  _globals['_CLOSEVOLUMEGROUPRESULT']._serialized_end=7868
  _globals['_VOLUMEGROUPINFORESULT']._serialized_start=7871
  _globals['_VOLUMEGROUPINFORESULT']._serialized_end=8326
  _globals['_VOLUMEGROUPINFORESULT_INITIATORS']._serialized_start=8144
  _globals['_VOLUMEGROUPINFORESULT_INITIATORS']._serialized_end=8216
  _globals['_VOLUMEGROUPINFORESULT_VOLUMEDISKLIST']._serialized_start=8218
  _globals['_VOLUMEGROUPINFORESULT_VOLUMEDISKLIST']._serialized_end=8326
  _globals['_CLUSTERCONFIG']._serialized_start=8329
  _globals['_CLUSTERCONFIG']._serialized_end=8578
  _globals['_MANAGEMENTSERVERCONFIG']._serialized_start=8580
  _globals['_MANAGEMENTSERVERCONFIG']._serialized_end=8692
  _globals['_CONTAINER']._serialized_start=8695
  _globals['_CONTAINER']._serialized_end=8824
  _globals['_CONTAINERLISTRESULT']._serialized_start=8827
  _globals['_CONTAINERLISTRESULT']._serialized_end=9033
  _globals['_IPCONFIG']._serialized_start=9035
  _globals['_IPCONFIG']._serialized_end=9095
  _globals['_NETWORK']._serialized_start=9097
  _globals['_NETWORK']._serialized_end=9194
  _globals['_NETWORKLISTRESULT']._serialized_start=9197
  _globals['_NETWORKLISTRESULT']._serialized_end=9399
  _globals['_HOST']._serialized_start=9402
  _globals['_HOST']._serialized_end=9534
  _globals['_HOSTLISTRESULT']._serialized_start=9537
  _globals['_HOSTLISTRESULT']._serialized_end=9733
  _globals['_SETVMPOWERSTATEARG']._serialized_start=9735
  _globals['_SETVMPOWERSTATEARG']._serialized_end=9789
  _globals['_SETVMPOWERSTATERESULT']._serialized_start=9791
  _globals['_SETVMPOWERSTATERESULT']._serialized_end=9833
# @@protoc_insertion_point(module_scope)
