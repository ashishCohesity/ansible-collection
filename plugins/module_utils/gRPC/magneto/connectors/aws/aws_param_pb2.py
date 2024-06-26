# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: magneto/connectors/aws/aws_param.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from magneto.base.entities import s3_pb2 as magneto_dot_base_dot_entities_dot_s3__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&magneto/connectors/aws/aws_param.proto\x12\x14\x63ohesity.magneto.aws\x1a\x1emagneto/base/entities/s3.proto\"\xa1\x03\n\x12\x42lockDeviceMapping\x12\x13\n\x0b\x64\x65vice_name\x18\x01 \x01(\t\x12\x15\n\rebs_volume_id\x18\x02 \x01(\t\x12\x19\n\x11volume_size_bytes\x18\x03 \x01(\x03\x12\x13\n\x0bvolume_type\x18\x04 \x01(\t\x12\x1d\n\x15\x64\x65lete_on_termination\x18\x05 \x01(\x08\x12\x14\n\x0cis_encrypted\x18\x07 \x01(\x08\x12\x12\n\nkms_key_id\x18\x06 \x01(\t\x12\x13\n\x0bsnapshot_id\x18\x08 \x01(\t\x12\x17\n\x0fsrc_snapshot_id\x18\x0b \x01(\t\x12\x10\n\x08num_iops\x18\n \x01(\x05\x12\x1d\n\x0eis_marketplace\x18\t \x01(\x08:\x05\x66\x61lse\x12\x1b\n\x13\x63reation_time_msecs\x18\x0c \x01(\x03\x12\r\n\x05state\x18\r \x01(\t\x12\x32\n\x0fvolume_tags_vec\x18\x0e \x03(\x0b\x32\x19.cohesity.magneto.aws.Tag\x12\x13\n\x0bvolume_name\x18\x0f \x01(\t\x12\x12\n\nthroughput\x18\x10 \x01(\x05\".\n\x08\x42ootMode\"\"\n\x04Type\x12\x0f\n\x0bkLegacyBIOS\x10\x00\x12\t\n\x05kUEFI\x10\x01\"\xf2\x01\n\tVMInfoArg\x12\x13\n\x0bregion_name\x18\x01 \x01(\t\x12\x13\n\x0binstance_id\x18\x02 \x01(\t\x12/\n should_populate_marketplace_info\x18\x03 \x01(\x08:\x05\x66\x61lse\x12*\n\x1bshould_populate_kms_aliases\x18\x04 \x01(\x08:\x05\x66\x61lse\x12\x34\n\x11instance_tags_vec\x18\x05 \x03(\x0b\x32\x19.cohesity.magneto.aws.Tag\x12(\n\x19should_populate_boot_mode\x18\x06 \x01(\x08:\x05\x66\x61lse\"\x8b\x17\n\x0cVMInfoResult\x12\x13\n\x0bregion_name\x18\x01 \x01(\t\x12J\n\x18\x62lock_device_mapping_vec\x18\x02 \x03(\x0b\x32(.cohesity.magneto.aws.BlockDeviceMapping\x12\x13\n\x0binstance_id\x18\x13 \x01(\t\x12\x15\n\rinstance_type\x18\x03 \x01(\t\x12\x10\n\x08image_id\x18\x04 \x01(\t\x12\x11\n\tsubnet_id\x18\x05 \x01(\t\x12\x0e\n\x06vpc_id\x18\x06 \x01(\t\x12\x11\n\tkernel_id\x18\x15 \x01(\t\x12\x13\n\x0bram_disk_id\x18\x16 \x01(\t\x12\x19\n\x11public_ip_address\x18\x11 \x01(\t\x12\x1e\n\x12private_ip_address\x18\x12 \x01(\tB\x02\x18\x01\x12\x1a\n\x12security_group_ids\x18\x07 \x03(\t\x12\x15\n\rkey_pair_name\x18\x08 \x01(\t\x12J\n\x0fplacement_group\x18\t \x01(\x0b\x32\x31.cohesity.magneto.aws.VMInfoResult.PlacementGroup\x12\x18\n\x10is_ebs_optimized\x18\n \x01(\x08\x12\x18\n\x10is_ena_supported\x18\x17 \x01(\x08\x12R\n\x15network_interface_vec\x18\x0b \x03(\x0b\x32\x33.cohesity.magneto.aws.VMInfoResult.NetworkInterface\x12S\n\x15tag_specification_vec\x18\x0c \x03(\x0b\x32\x34.cohesity.magneto.aws.VMInfoResult.TagSpecifications\x12\x15\n\rinstance_name\x18\r \x01(\t\x12\x18\n\x10root_device_name\x18\x0e \x01(\t\x12\x14\n\x0c\x61rchitecture\x18\x0f \x01(\t\x12\x16\n\x0evirtualization\x18\x10 \x01(\t\x12\x10\n\x08platform\x18\x14 \x01(\t\x12\x16\n\x0eis_marketplace\x18\x18 \x01(\x08\x12\r\n\x05state\x18\x19 \x01(\t\x12\x19\n\x11\x61ttached_iam_role\x18\x1a \x01(\t\x12\x15\n\rsize_in_bytes\x18\x1b \x01(\x03\x12\x13\n\x0blaunch_time\x18\x1c \x01(\t\x12\x19\n\x11launch_time_msecs\x18\x1d \x01(\x03\x12S\n\x14iam_instance_profile\x18\x1e \x01(\x0b\x32\x35.cohesity.magneto.aws.VMInfoResult.IAMInstanceProfile\x12\x41\n\nmonitoring\x18\x1f \x01(\x0b\x32-.cohesity.magneto.aws.VMInfoResult.Monitoring\x12\x42\n\x0b\x63pu_options\x18  \x01(\x0b\x32-.cohesity.magneto.aws.VMInfoResult.CpuOptions\x12o\n\"capacity_reservation_specification\x18! \x01(\x0b\x32\x43.cohesity.magneto.aws.VMInfoResult.CapacityReservationSpecification\x12R\n\x13hibernation_options\x18\" \x01(\x0b\x32\x35.cohesity.magneto.aws.VMInfoResult.HibernationOptions\x12[\n\x1alicense_configurations_vec\x18# \x03(\x0b\x32\x37.cohesity.magneto.aws.VMInfoResult.LicenseConfiguration\x12L\n\x10metadata_options\x18$ \x01(\x0b\x32\x32.cohesity.magneto.aws.VMInfoResult.MetadataOptions\x12J\n\x0f\x65nclave_options\x18% \x01(\x0b\x32\x31.cohesity.magneto.aws.VMInfoResult.EnclaveOptions\x12\x36\n\tboot_mode\x18& \x01(\x0e\x32#.cohesity.magneto.aws.BootMode.Type\x12\x1c\n\x14private_ip_addresses\x18\' \x03(\t\x1a<\n\x0ePlacementGroup\x12\x0f\n\x07tenancy\x18\x01 \x01(\t\x12\x19\n\x11\x61vailability_zone\x18\x02 \x01(\t\x1a\xf2\x02\n\x10NetworkInterface\x12\x13\n\x0b\x64\x65scription\x18\x01 \x01(\t\x12\x17\n\x0c\x64\x65vice_index\x18\x02 \x01(\x05:\x01\x30\x12\x11\n\tsubnet_id\x18\x03 \x01(\t\x12\x1d\n\x12network_card_index\x18\x04 \x01(\x05:\x01\x30\x12\x1c\n\x14network_interface_id\x18\x05 \x01(\t\x12\x65\n\x16private_ip_address_vec\x18\x06 \x03(\x0b\x32\x45.cohesity.magneto.aws.VMInfoResult.NetworkInterface.InstanceIpAddress\x12\x18\n\x10ipv6_address_vec\x18\x07 \x03(\t\x12\x1d\n\x15security_group_id_vec\x18\x08 \x03(\t\x1a@\n\x11InstanceIpAddress\x12\x1a\n\x12private_ip_address\x18\x01 \x01(\t\x12\x0f\n\x07primary\x18\x02 \x01(\x08\x1a\xa5\x01\n\x11TagSpecifications\x12\x15\n\rresource_type\x18\x01 \x01(\t\x12R\n\x0ctag_info_vec\x18\x02 \x03(\x0b\x32<.cohesity.magneto.aws.VMInfoResult.TagSpecifications.TagInfo\x1a%\n\x07TagInfo\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\x1a-\n\x12IAMInstanceProfile\x12\x0b\n\x03\x61rn\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x1a\x1b\n\nMonitoring\x12\r\n\x05state\x18\x01 \x01(\t\x1a:\n\nCpuOptions\x12\x12\n\ncore_count\x18\x01 \x01(\x03\x12\x18\n\x10threads_per_core\x18\x02 \x01(\x03\x1a\xbf\x02\n CapacityReservationSpecification\x12\'\n\x1f\x63\x61pacity_reservation_preference\x18\x01 \x01(\t\x12\x82\x01\n\x1b\x63\x61pacity_reservation_target\x18\x02 \x01(\x0b\x32].cohesity.magneto.aws.VMInfoResult.CapacityReservationSpecification.CapacityReservationTarget\x1am\n\x19\x43\x61pacityReservationTarget\x12\x1f\n\x17\x63\x61pacity_reservation_id\x18\x01 \x01(\t\x12/\n\'capacity_reservation_resource_group_arn\x18\x02 \x01(\t\x1a+\n\x12HibernationOptions\x12\x15\n\ris_configured\x18\x01 \x01(\x08\x1a\x39\n\x14LicenseConfiguration\x12!\n\x19license_configuration_arn\x18\x01 \x01(\t\x1a\x62\n\x0fMetadataOptions\x12\x13\n\x0bhttp_tokens\x18\x01 \x01(\t\x12#\n\x1bhttp_put_response_hop_limit\x18\x02 \x01(\x03\x12\x15\n\rhttp_endpoint\x18\x03 \x01(\t\x1a!\n\x0e\x45nclaveOptions\x12\x0f\n\x07\x65nabled\x18\x01 \x01(\x08\"\xe6\x01\n\x13\x43reateVMSnapshotArg\x12\x13\n\x0bregion_name\x18\x01 \x01(\t\x12X\n\x10snapshot_arg_vec\x18\x02 \x03(\x0b\x32>.cohesity.magneto.aws.CreateVMSnapshotArg.EBSVolumeSnapshotArg\x1a`\n\x14\x45\x42SVolumeSnapshotArg\x12\n\n\x02id\x18\x01 \x01(\t\x12\x10\n\x08tag_uuid\x18\x02 \x01(\t\x12*\n\x07tag_vec\x18\x03 \x03(\x0b\x32\x19.cohesity.magneto.aws.Tag\"\xcb\x01\n\x16\x43reateVMSnapshotResult\x12\x61\n\x13snapshot_result_vec\x18\x01 \x03(\x0b\x32\x44.cohesity.magneto.aws.CreateVMSnapshotResult.EBSVolumeSnapshotResult\x1aN\n\x17\x45\x42SVolumeSnapshotResult\x12\n\n\x02id\x18\x01 \x01(\t\x12\x13\n\x0bsnapshot_id\x18\x02 \x01(\t\x12\x12\n\nsize_bytes\x18\x03 \x01(\x03\"q\n\x18\x46\x65tchEBSSnapshotsInfoArg\x12\x13\n\x0bregion_name\x18\x01 \x01(\t\x12\x17\n\x0fsnapshot_id_vec\x18\x02 \x03(\t\x12\x11\n\tvolume_id\x18\x03 \x01(\t\x12\x14\n\x0csnapshot_tag\x18\x04 \x01(\t\"\xf9\x03\n\x1b\x46\x65tchEBSSnapshotsInfoResult\x12Y\n\x11snapshot_info_vec\x18\x01 \x03(\x0b\x32>.cohesity.magneto.aws.FetchEBSSnapshotsInfoResult.SnapshotInfo\x1a\xfe\x02\n\x0cSnapshotInfo\x12\x13\n\x0bsnapshot_id\x18\x01 \x01(\t\x12\x11\n\tvolume_id\x18\x02 \x01(\t\x12\x17\n\x0fvolume_size_gib\x18\x03 \x01(\x05\x12\x14\n\x0cprogress_pct\x18\x04 \x01(\x05\x12[\n\x05state\x18\x05 \x01(\x0e\x32L.cohesity.magneto.aws.FetchEBSSnapshotsInfoResult.SnapshotInfo.SnapshotState\x12\x18\n\x10start_time_msecs\x18\x06 \x01(\x03\x12\x15\n\rstate_message\x18\x07 \x01(\t\x12\x34\n\x11snapshot_tags_vec\x18\x08 \x03(\x0b\x32\x19.cohesity.magneto.aws.Tag\"S\n\rSnapshotState\x12\x0c\n\x08kPending\x10\x01\x12\r\n\tkComplete\x10\x02\x12\n\n\x06kError\x10\x03\x12\x0b\n\x07kNotSet\x10\x04\x12\x0c\n\x08kUnknown\x10\x05\"=\n\nDiskFormat\"/\n\x04Type\x12\x08\n\x04kVHD\x10\x01\x12\t\n\x05kVMDK\x10\x02\x12\x08\n\x04kRAW\x10\x03\x12\x08\n\x04kOVA\x10\x04\"\xfc\x01\n\x11ImportSnapshotArg\x12\x13\n\x0bregion_name\x18\x01 \x02(\t\x12\x11\n\ts3_bucket\x18\x02 \x02(\t\x12\x0e\n\x06s3_key\x18\x03 \x02(\t\x12\x14\n\x0c\x63lient_token\x18\x04 \x01(\t\x12:\n\x0b\x64isk_format\x18\x05 \x02(\x0e\x32%.cohesity.magneto.aws.DiskFormat.Type\x12\x1d\n\x0eshould_encrypt\x18\x06 \x01(\x08:\x05\x66\x61lse\x12\x12\n\nkms_key_id\x18\x07 \x01(\t\x12*\n\x1busing_user_provided_kms_key\x18\x08 \x01(\x08:\x05\x66\x61lse\"7\n\x14ImportSnapshotResult\x12\x1f\n\x17import_snapshot_task_id\x18\x01 \x01(\t\"j\n\x1b\x43\x61ncelImportSnapshotTaskArg\x12\x13\n\x0bregion_name\x18\x01 \x02(\t\x12\x1f\n\x17import_snapshot_task_id\x18\x02 \x02(\t\x12\x15\n\rcancel_reason\x18\x03 \x01(\t\" \n\x1e\x43\x61ncelImportSnapshotTaskResult\"d\n\x18\x43\x61ncelImportImageTaskArg\x12\x13\n\x0bregion_name\x18\x01 \x02(\t\x12\x1c\n\x14import_image_task_id\x18\x02 \x02(\t\x12\x15\n\rcancel_reason\x18\x03 \x01(\t\"g\n\x18ImportSnapshotTaskStatus\"K\n\x04Type\x12\n\n\x06kError\x10\x01\x12\r\n\tkComplete\x10\x02\x12\x0b\n\x07kActive\x10\x03\x12\x0c\n\x08kDeleted\x10\x04\x12\r\n\tkDeleting\x10\x05\"y\n\x1d\x44\x65scribeImportSnapshotTaskArg\x12\x13\n\x0bregion_name\x18\x01 \x02(\t\x12\x1f\n\x17import_snapshot_task_id\x18\x02 \x02(\t\x12\"\n\x13wait_for_completion\x18\x03 \x01(\x08:\x05\x66\x61lse\"\xb8\x01\n DescribeImportSnapshotTaskResult\x12X\n\x1bimport_snapshot_task_status\x18\x01 \x01(\x0e\x32\x33.cohesity.magneto.aws.ImportSnapshotTaskStatus.Type\x12%\n\x1apercentage_task_completion\x18\x02 \x01(\x05:\x01\x30\x12\x13\n\x0bsnapshot_id\x18\x03 \x01(\t\"\xe1\x02\n\x18\x43reateAMIFromSnapshotArg\x12\x13\n\x0bregion_name\x18\x01 \x02(\t\x12\x10\n\x08\x61mi_name\x18\x02 \x02(\t\x12 \n\x13virtualization_type\x18\x03 \x01(\t:\x03hvm\x12\x1f\n\x11\x61rchitecture_type\x18\x04 \x01(\t:\x04i386\x12\x18\n\x10root_device_name\x18\x05 \x02(\t\x12\x11\n\tkernel_id\x18\x07 \x01(\t\x12\x13\n\x0bram_disk_id\x18\x08 \x01(\t\x12\x15\n\rena_supported\x18\t \x01(\x08\x12J\n\x18\x62lock_device_mapping_vec\x18\x06 \x03(\x0b\x32(.cohesity.magneto.aws.BlockDeviceMapping\x12\x36\n\tboot_mode\x18\n \x01(\x0e\x32#.cohesity.magneto.aws.BootMode.Type\"/\n\x1b\x43reateAMIFromSnapshotResult\x12\x10\n\x08image_id\x18\x01 \x01(\t\"=\n\x11\x44\x65leteSnapshotArg\x12\x13\n\x0bregion_name\x18\x01 \x02(\t\x12\x13\n\x0bsnapshot_id\x18\x02 \x02(\t\"\x16\n\x14\x44\x65leteSnapshotResult\"\xbf\x03\n\x13\x43reateVMInstanceArg\x12\x33\n\x07vm_info\x18\x01 \x01(\x0b\x32\".cohesity.magneto.aws.VMInfoResult\x12\x16\n\x08power_on\x18\x02 \x01(\x08:\x04true\x12#\n\x15wait_for_status_check\x18\x03 \x01(\x08:\x04true\x12\x1d\n\x0eset_private_ip\x18\x04 \x01(\x08:\x05\x66\x61lse\x12,\n\x1dreturn_early_in_pending_state\x18\x05 \x01(\x08:\x05\x66\x61lse\x12S\n\x0e\x64\x65vice_tag_map\x18\x06 \x03(\x0b\x32;.cohesity.magneto.aws.CreateVMInstanceArg.DeviceTagMapEntry\x1a/\n\x04Tags\x12\'\n\x04tags\x18\x01 \x03(\x0b\x32\x19.cohesity.magneto.aws.Tag\x1a\x63\n\x11\x44\x65viceTagMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12=\n\x05value\x18\x02 \x01(\x0b\x32..cohesity.magneto.aws.CreateVMInstanceArg.Tags:\x02\x38\x01\"\x96\x01\n\x16\x43reateVMInstanceResult\x12\x13\n\x0binstance_id\x18\x01 \x01(\t\x12\x19\n\x11public_ip_address\x18\x02 \x01(\t\x12\x1a\n\x12private_ip_address\x18\x03 \x01(\t\x12\x15\n\rinstance_type\x18\x04 \x01(\t\x12\x19\n\x11\x61vailability_zone\x18\x05 \x01(\t\"a\n\x10StartInstanceArg\x12\x13\n\x0binstance_id\x18\x01 \x01(\t\x12\x13\n\x0bregion_name\x18\x02 \x01(\t\x12#\n\x15wait_for_status_check\x18\x03 \x01(\x08:\x04true\"\xb5\x01\n\x14\x43reateEBSSnapshotArg\x12\x13\n\x0bregion_name\x18\x01 \x02(\t\x12\x11\n\tvolume_id\x18\x02 \x02(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x10\n\x08tag_uuid\x18\x04 \x01(\t\x12*\n\x07tag_vec\x18\x06 \x03(\x0b\x32\x19.cohesity.magneto.aws.Tag\x12\"\n\x13wait_for_completion\x18\x05 \x01(\x08:\x05\x66\x61lse\"a\n\x17\x43reateEBSSnapshotResult\x12\x13\n\x0bsnapshot_id\x18\x01 \x01(\t\x12\x17\n\x0fvolume_size_gib\x18\x02 \x01(\x05\x12\x18\n\x10time_taken_usecs\x18\x03 \x01(\x03\"\xff\x01\n\x0f\x43opySnapshotArg\x12\x0c\n\x04name\x18\x08 \x01(\t\x12\x1a\n\x12source_snapshot_id\x18\x01 \x01(\t\x12\x15\n\rsource_region\x18\x06 \x02(\t\x12\x13\n\x0b\x64\x65st_region\x18\x02 \x02(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x1d\n\x0eshould_encrypt\x18\x05 \x01(\x08:\x05\x66\x61lse\x12\x12\n\nkms_key_id\x18\x04 \x01(\t\x12*\n\x07tag_vec\x18\t \x03(\x0b\x32\x19.cohesity.magneto.aws.Tag\x12\"\n\x13wait_for_completion\x18\x07 \x01(\x08:\x05\x66\x61lse\")\n\x12\x43opySnapshotResult\x12\x13\n\x0bsnapshot_id\x18\x01 \x01(\t\"\xa2\x02\n\x12\x43reateEBSVolumeArg\x12\x13\n\x0bregion_name\x18\x01 \x02(\t\x12\x13\n\x0bsnapshot_id\x18\x02 \x01(\t\x12\x19\n\x11\x61vailability_zone\x18\x03 \x01(\t\x12\x17\n\x0f\x65\x62s_volume_type\x18\x05 \x01(\t\x12\x10\n\x08num_iops\x18\x06 \x01(\x05\x12\x17\n\x0fvolume_size_gib\x18\x07 \x01(\x05\x12\x1d\n\x0e\x65ncrypt_volume\x18\x08 \x01(\x08:\x05\x66\x61lse\x12\x12\n\nkms_key_id\x18\t \x01(\t\x12\x10\n\x08tag_uuid\x18\x04 \x01(\t\x12*\n\x07tag_vec\x18\n \x03(\x0b\x32\x19.cohesity.magneto.aws.Tag\x12\x12\n\nthroughput\x18\x0b \x01(\x05\"_\n\x15\x43reateEBSVolumeResult\x12\x11\n\tvolume_id\x18\x01 \x01(\t\x12\x18\n\x10volume_size_gibs\x18\x02 \x01(\x03\x12\x19\n\x11\x61vailability_zone\x18\x03 \x01(\t\"W\n\x15\x44\x65scribeEBSVolumesArg\x12\x13\n\x0bregion_name\x18\x01 \x02(\t\x12\x15\n\rvolume_id_vec\x18\x02 \x03(\t\x12\x12\n\nvolume_tag\x18\x03 \x01(\t\"f\n\x18\x44\x65scribeEBSVolumesResult\x12J\n\x18\x62lock_device_mapping_vec\x18\x01 \x03(\x0b\x32(.cohesity.magneto.aws.BlockDeviceMapping\"\x8c\x01\n\x12\x41ttachEBSVolumeArg\x12\x11\n\tvolume_id\x18\x01 \x02(\t\x12\x13\n\x0binstance_id\x18\x02 \x02(\t\x12\x13\n\x0b\x64\x65vice_name\x18\x03 \x02(\t\x12\x13\n\x0bregion_name\x18\x04 \x02(\t\x12$\n\x15\x64\x65lete_on_termination\x18\x05 \x01(\x08:\x05\x66\x61lse\"\x17\n\x15\x41ttachEBSVolumeResult\"<\n\x12\x44\x65leteEBSVolumeArg\x12\x13\n\x0bregion_name\x18\x01 \x02(\t\x12\x11\n\tvolume_id\x18\x02 \x02(\t\"\x17\n\x15\x44\x65leteEBSVolumeResult\"<\n\x12\x44\x65tachEBSVolumeArg\x12\x11\n\tvolume_id\x18\x01 \x02(\t\x12\x13\n\x0bregion_name\x18\x02 \x02(\t\"\x17\n\x15\x44\x65tachEBSVolumeResult\"8\n\x0eSubnetAddrMask\x12\x11\n\tsubnet_ip\x18\x01 \x01(\t\x12\x13\n\x0bsubnet_mask\x18\x02 \x01(\t\"\xc0\x01\n\x16\x43reateSecurityGroupArg\x12\x0e\n\x06vpc_id\x18\x01 \x02(\t\x12\x13\n\x0bregion_name\x18\x02 \x02(\t\x12\x1b\n\x13security_group_name\x18\x03 \x01(\t\x12\x1a\n\x12incoming_tcp_ports\x18\x04 \x03(\x05\x12H\n\x1a\x63luster_subnet_address_vec\x18\x05 \x03(\x0b\x32$.cohesity.magneto.aws.SubnetAddrMask\"6\n\x19\x43reateSecurityGroupResult\x12\x19\n\x11security_group_id\x18\x01 \x01(\t\"\\\n\x1cModifySnapshotPermissionsArg\x12\x13\n\x0bregion_name\x18\x01 \x02(\t\x12\x13\n\x0bsnapshot_id\x18\x02 \x02(\t\x12\x12\n\naccount_id\x18\x03 \x01(\t\"!\n\x1fModifySnapshotPermissionsResult\"\xd2\x01\n\x11SSMSendCommandArg\x12\x0e\n\x06region\x18\x01 \x01(\t\x12\x14\n\x0cinstance_ids\x18\x02 \x03(\t\x12\x15\n\rdocument_name\x18\x03 \x01(\t\x12\x45\n\nparameters\x18\x04 \x03(\x0b\x32\x31.cohesity.magneto.aws.SSMSendCommandArg.Parameter\x12\x0f\n\x07\x63omment\x18\x05 \x01(\t\x1a(\n\tParameter\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x0e\n\x06values\x18\x02 \x03(\t\"*\n\x14SSMSendCommandResult\x12\x12\n\ncommand_id\x18\x01 \x01(\t\"\x89\x01\n\x17SSMGetCommandOutcomeArg\x12\x0e\n\x06region\x18\x01 \x01(\t\x12\x12\n\ncommand_id\x18\x02 \x01(\t\x12\x13\n\x0binstance_id\x18\x03 \x01(\t\x12!\n\x12\x64ownload_log_files\x18\x04 \x01(\x08:\x05\x66\x61lse\x12\x12\n\nis_windows\x18\x05 \x01(\x08\"d\n\x1aSSMGetCommandOutcomeResult\x12\x16\n\x0e\x63ommand_status\x18\x01 \x01(\t\x12\x16\n\x0e\x63ommand_stdout\x18\x02 \x01(\t\x12\x16\n\x0e\x63ommand_stderr\x18\x03 \x01(\t\"\x89\x01\n\x1fModifyInstanceSecurityGroupsArg\x12\x19\n\x11security_group_id\x18\x01 \x01(\t\x12!\n\x19should_add_security_group\x18\x02 \x01(\x08\x12\x13\n\x0bregion_name\x18\x03 \x01(\t\x12\x13\n\x0binstance_id\x18\x04 \x01(\t\"$\n\"ModifyInstanceSecurityGroupsResult\"!\n\x03Tag\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"o\n\x13SetResourcesTagsArg\x12\x13\n\x0bregion_name\x18\x01 \x01(\t\x12\x17\n\x0fresource_id_vec\x18\x02 \x03(\t\x12*\n\x07tag_vec\x18\x03 \x03(\x0b\x32\x19.cohesity.magneto.aws.Tag\"\x18\n\x16SetResourcesTagsResult\"\xa2\x01\n\x15ListSnapshotBlocksArg\x12\x13\n\x0bregion_name\x18\x01 \x01(\t\x12\x13\n\x0bsnapshot_id\x18\x02 \x01(\t\x12\x18\n\x10\x62\x61se_snapshot_id\x18\x03 \x01(\t\x12\x13\n\x0bmax_results\x18\x04 \x01(\x03\x12\x12\n\nnext_token\x18\x05 \x01(\t\x12\x1c\n\x14starting_block_index\x18\x06 \x01(\x03\"]\n\x13GetSnapshotBlockArg\x12\x13\n\x0bregion_name\x18\x01 \x01(\t\x12\x13\n\x0bsnapshot_id\x18\x02 \x01(\t\x12\r\n\x05index\x18\x03 \x01(\x03\x12\r\n\x05token\x18\x04 \x01(\t\"\xef\x01\n\x10StartSnapshotArg\x12\x13\n\x0bregion_name\x18\x01 \x01(\t\x12\x16\n\x0evolume_size_gb\x18\x02 \x01(\x03\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x14\n\x0cis_encrypted\x18\x04 \x01(\x08\x12\x13\n\x0bkms_key_arn\x18\x05 \x01(\t\x12\x1a\n\x12parent_snapshot_id\x18\x06 \x01(\t\x12+\n\x08tags_vec\x18\x07 \x03(\x0b\x32\x19.cohesity.magneto.aws.Tag\x12\x14\n\x0c\x63lient_token\x18\x08 \x01(\t\x12\x0f\n\x07timeout\x18\t \x01(\x03\"\x97\x01\n\x13PutSnapshotBlockArg\x12\x13\n\x0bregion_name\x18\x01 \x01(\t\x12\x13\n\x0bsnapshot_id\x18\x02 \x01(\t\x12\x13\n\x0b\x62lock_index\x18\x03 \x01(\x03\x12\x10\n\x08\x63hecksum\x18\x04 \x01(\t\x12\x1a\n\x12\x63hecksum_algorithm\x18\x05 \x01(\t\x12\x13\n\x0b\x64\x61ta_length\x18\x06 \x01(\x03\"]\n\x13\x43ompleteSnapshotArg\x12\x13\n\x0bregion_name\x18\x01 \x01(\t\x12\x1c\n\x14\x63hanged_blocks_count\x18\x02 \x01(\x03\x12\x13\n\x0bsnapshot_id\x18\x03 \x01(\t\"4\n\x10InstanceTypeInfo\x12 \n\x18supported_boot_modes_vec\x18\x01 \x03(\t\"F\n\x18\x44\x65scribeInstanceTypesArg\x12\x13\n\x0bregion_name\x18\x01 \x01(\t\x12\x15\n\rinstance_type\x18\x02 \x01(\t\"a\n\x1b\x44\x65scribeInstanceTypesResult\x12\x42\n\x12instance_type_info\x18\x01 \x01(\x0b\x32&.cohesity.magneto.aws.InstanceTypeInfo\"t\n\x0cS3BucketInfo\x12\x31\n\x0c\x65ntity_proto\x18\x01 \x01(\x0b\x32\x1b.cohesity.magneto.s3.Entity\x12\x31\n\x0e\x62ucket_tag_vec\x18\x02 \x03(\x0b\x32\x19.cohesity.magneto.aws.Tag\"+\n\x14\x44\x65scribeS3BucketsArg\x12\x13\n\x0bregion_name\x18\x01 \x01(\t\"Y\n\x17\x44\x65scribeS3BucketsResult\x12>\n\x12s3_bucket_info_vec\x18\x01 \x03(\x0b\x32\".cohesity.magneto.aws.S3BucketInfoB%Z#magneto/connectors/aws/aws_param.pb')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'magneto.connectors.aws.aws_param_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z#magneto/connectors/aws/aws_param.pb'
  _globals['_VMINFORESULT'].fields_by_name['private_ip_address']._loaded_options = None
  _globals['_VMINFORESULT'].fields_by_name['private_ip_address']._serialized_options = b'\030\001'
  _globals['_CREATEVMINSTANCEARG_DEVICETAGMAPENTRY']._loaded_options = None
  _globals['_CREATEVMINSTANCEARG_DEVICETAGMAPENTRY']._serialized_options = b'8\001'
  _globals['_BLOCKDEVICEMAPPING']._serialized_start=97
  _globals['_BLOCKDEVICEMAPPING']._serialized_end=514
  _globals['_BOOTMODE']._serialized_start=516
  _globals['_BOOTMODE']._serialized_end=562
  _globals['_BOOTMODE_TYPE']._serialized_start=528
  _globals['_BOOTMODE_TYPE']._serialized_end=562
  _globals['_VMINFOARG']._serialized_start=565
  _globals['_VMINFOARG']._serialized_end=807
  _globals['_VMINFORESULT']._serialized_start=810
  _globals['_VMINFORESULT']._serialized_end=3765
  _globals['_VMINFORESULT_PLACEMENTGROUP']._serialized_start=2467
  _globals['_VMINFORESULT_PLACEMENTGROUP']._serialized_end=2527
  _globals['_VMINFORESULT_NETWORKINTERFACE']._serialized_start=2530
  _globals['_VMINFORESULT_NETWORKINTERFACE']._serialized_end=2900
  _globals['_VMINFORESULT_NETWORKINTERFACE_INSTANCEIPADDRESS']._serialized_start=2836
  _globals['_VMINFORESULT_NETWORKINTERFACE_INSTANCEIPADDRESS']._serialized_end=2900
  _globals['_VMINFORESULT_TAGSPECIFICATIONS']._serialized_start=2903
  _globals['_VMINFORESULT_TAGSPECIFICATIONS']._serialized_end=3068
  _globals['_VMINFORESULT_TAGSPECIFICATIONS_TAGINFO']._serialized_start=3031
  _globals['_VMINFORESULT_TAGSPECIFICATIONS_TAGINFO']._serialized_end=3068
  _globals['_VMINFORESULT_IAMINSTANCEPROFILE']._serialized_start=3070
  _globals['_VMINFORESULT_IAMINSTANCEPROFILE']._serialized_end=3115
  _globals['_VMINFORESULT_MONITORING']._serialized_start=3117
  _globals['_VMINFORESULT_MONITORING']._serialized_end=3144
  _globals['_VMINFORESULT_CPUOPTIONS']._serialized_start=3146
  _globals['_VMINFORESULT_CPUOPTIONS']._serialized_end=3204
  _globals['_VMINFORESULT_CAPACITYRESERVATIONSPECIFICATION']._serialized_start=3207
  _globals['_VMINFORESULT_CAPACITYRESERVATIONSPECIFICATION']._serialized_end=3526
  _globals['_VMINFORESULT_CAPACITYRESERVATIONSPECIFICATION_CAPACITYRESERVATIONTARGET']._serialized_start=3417
  _globals['_VMINFORESULT_CAPACITYRESERVATIONSPECIFICATION_CAPACITYRESERVATIONTARGET']._serialized_end=3526
  _globals['_VMINFORESULT_HIBERNATIONOPTIONS']._serialized_start=3528
  _globals['_VMINFORESULT_HIBERNATIONOPTIONS']._serialized_end=3571
  _globals['_VMINFORESULT_LICENSECONFIGURATION']._serialized_start=3573
  _globals['_VMINFORESULT_LICENSECONFIGURATION']._serialized_end=3630
  _globals['_VMINFORESULT_METADATAOPTIONS']._serialized_start=3632
  _globals['_VMINFORESULT_METADATAOPTIONS']._serialized_end=3730
  _globals['_VMINFORESULT_ENCLAVEOPTIONS']._serialized_start=3732
  _globals['_VMINFORESULT_ENCLAVEOPTIONS']._serialized_end=3765
  _globals['_CREATEVMSNAPSHOTARG']._serialized_start=3768
  _globals['_CREATEVMSNAPSHOTARG']._serialized_end=3998
  _globals['_CREATEVMSNAPSHOTARG_EBSVOLUMESNAPSHOTARG']._serialized_start=3902
  _globals['_CREATEVMSNAPSHOTARG_EBSVOLUMESNAPSHOTARG']._serialized_end=3998
  _globals['_CREATEVMSNAPSHOTRESULT']._serialized_start=4001
  _globals['_CREATEVMSNAPSHOTRESULT']._serialized_end=4204
  _globals['_CREATEVMSNAPSHOTRESULT_EBSVOLUMESNAPSHOTRESULT']._serialized_start=4126
  _globals['_CREATEVMSNAPSHOTRESULT_EBSVOLUMESNAPSHOTRESULT']._serialized_end=4204
  _globals['_FETCHEBSSNAPSHOTSINFOARG']._serialized_start=4206
  _globals['_FETCHEBSSNAPSHOTSINFOARG']._serialized_end=4319
  _globals['_FETCHEBSSNAPSHOTSINFORESULT']._serialized_start=4322
  _globals['_FETCHEBSSNAPSHOTSINFORESULT']._serialized_end=4827
  _globals['_FETCHEBSSNAPSHOTSINFORESULT_SNAPSHOTINFO']._serialized_start=4445
  _globals['_FETCHEBSSNAPSHOTSINFORESULT_SNAPSHOTINFO']._serialized_end=4827
  _globals['_FETCHEBSSNAPSHOTSINFORESULT_SNAPSHOTINFO_SNAPSHOTSTATE']._serialized_start=4744
  _globals['_FETCHEBSSNAPSHOTSINFORESULT_SNAPSHOTINFO_SNAPSHOTSTATE']._serialized_end=4827
  _globals['_DISKFORMAT']._serialized_start=4829
  _globals['_DISKFORMAT']._serialized_end=4890
  _globals['_DISKFORMAT_TYPE']._serialized_start=4843
  _globals['_DISKFORMAT_TYPE']._serialized_end=4890
  _globals['_IMPORTSNAPSHOTARG']._serialized_start=4893
  _globals['_IMPORTSNAPSHOTARG']._serialized_end=5145
  _globals['_IMPORTSNAPSHOTRESULT']._serialized_start=5147
  _globals['_IMPORTSNAPSHOTRESULT']._serialized_end=5202
  _globals['_CANCELIMPORTSNAPSHOTTASKARG']._serialized_start=5204
  _globals['_CANCELIMPORTSNAPSHOTTASKARG']._serialized_end=5310
  _globals['_CANCELIMPORTSNAPSHOTTASKRESULT']._serialized_start=5312
  _globals['_CANCELIMPORTSNAPSHOTTASKRESULT']._serialized_end=5344
  _globals['_CANCELIMPORTIMAGETASKARG']._serialized_start=5346
  _globals['_CANCELIMPORTIMAGETASKARG']._serialized_end=5446
  _globals['_IMPORTSNAPSHOTTASKSTATUS']._serialized_start=5448
  _globals['_IMPORTSNAPSHOTTASKSTATUS']._serialized_end=5551
  _globals['_IMPORTSNAPSHOTTASKSTATUS_TYPE']._serialized_start=5476
  _globals['_IMPORTSNAPSHOTTASKSTATUS_TYPE']._serialized_end=5551
  _globals['_DESCRIBEIMPORTSNAPSHOTTASKARG']._serialized_start=5553
  _globals['_DESCRIBEIMPORTSNAPSHOTTASKARG']._serialized_end=5674
  _globals['_DESCRIBEIMPORTSNAPSHOTTASKRESULT']._serialized_start=5677
  _globals['_DESCRIBEIMPORTSNAPSHOTTASKRESULT']._serialized_end=5861
  _globals['_CREATEAMIFROMSNAPSHOTARG']._serialized_start=5864
  _globals['_CREATEAMIFROMSNAPSHOTARG']._serialized_end=6217
  _globals['_CREATEAMIFROMSNAPSHOTRESULT']._serialized_start=6219
  _globals['_CREATEAMIFROMSNAPSHOTRESULT']._serialized_end=6266
  _globals['_DELETESNAPSHOTARG']._serialized_start=6268
  _globals['_DELETESNAPSHOTARG']._serialized_end=6329
  _globals['_DELETESNAPSHOTRESULT']._serialized_start=6331
  _globals['_DELETESNAPSHOTRESULT']._serialized_end=6353
  _globals['_CREATEVMINSTANCEARG']._serialized_start=6356
  _globals['_CREATEVMINSTANCEARG']._serialized_end=6803
  _globals['_CREATEVMINSTANCEARG_TAGS']._serialized_start=6655
  _globals['_CREATEVMINSTANCEARG_TAGS']._serialized_end=6702
  _globals['_CREATEVMINSTANCEARG_DEVICETAGMAPENTRY']._serialized_start=6704
  _globals['_CREATEVMINSTANCEARG_DEVICETAGMAPENTRY']._serialized_end=6803
  _globals['_CREATEVMINSTANCERESULT']._serialized_start=6806
  _globals['_CREATEVMINSTANCERESULT']._serialized_end=6956
  _globals['_STARTINSTANCEARG']._serialized_start=6958
  _globals['_STARTINSTANCEARG']._serialized_end=7055
  _globals['_CREATEEBSSNAPSHOTARG']._serialized_start=7058
  _globals['_CREATEEBSSNAPSHOTARG']._serialized_end=7239
  _globals['_CREATEEBSSNAPSHOTRESULT']._serialized_start=7241
  _globals['_CREATEEBSSNAPSHOTRESULT']._serialized_end=7338
  _globals['_COPYSNAPSHOTARG']._serialized_start=7341
  _globals['_COPYSNAPSHOTARG']._serialized_end=7596
  _globals['_COPYSNAPSHOTRESULT']._serialized_start=7598
  _globals['_COPYSNAPSHOTRESULT']._serialized_end=7639
  _globals['_CREATEEBSVOLUMEARG']._serialized_start=7642
  _globals['_CREATEEBSVOLUMEARG']._serialized_end=7932
  _globals['_CREATEEBSVOLUMERESULT']._serialized_start=7934
  _globals['_CREATEEBSVOLUMERESULT']._serialized_end=8029
  _globals['_DESCRIBEEBSVOLUMESARG']._serialized_start=8031
  _globals['_DESCRIBEEBSVOLUMESARG']._serialized_end=8118
  _globals['_DESCRIBEEBSVOLUMESRESULT']._serialized_start=8120
  _globals['_DESCRIBEEBSVOLUMESRESULT']._serialized_end=8222
  _globals['_ATTACHEBSVOLUMEARG']._serialized_start=8225
  _globals['_ATTACHEBSVOLUMEARG']._serialized_end=8365
  _globals['_ATTACHEBSVOLUMERESULT']._serialized_start=8367
  _globals['_ATTACHEBSVOLUMERESULT']._serialized_end=8390
  _globals['_DELETEEBSVOLUMEARG']._serialized_start=8392
  _globals['_DELETEEBSVOLUMEARG']._serialized_end=8452
  _globals['_DELETEEBSVOLUMERESULT']._serialized_start=8454
  _globals['_DELETEEBSVOLUMERESULT']._serialized_end=8477
  _globals['_DETACHEBSVOLUMEARG']._serialized_start=8479
  _globals['_DETACHEBSVOLUMEARG']._serialized_end=8539
  _globals['_DETACHEBSVOLUMERESULT']._serialized_start=8541
  _globals['_DETACHEBSVOLUMERESULT']._serialized_end=8564
  _globals['_SUBNETADDRMASK']._serialized_start=8566
  _globals['_SUBNETADDRMASK']._serialized_end=8622
  _globals['_CREATESECURITYGROUPARG']._serialized_start=8625
  _globals['_CREATESECURITYGROUPARG']._serialized_end=8817
  _globals['_CREATESECURITYGROUPRESULT']._serialized_start=8819
  _globals['_CREATESECURITYGROUPRESULT']._serialized_end=8873
  _globals['_MODIFYSNAPSHOTPERMISSIONSARG']._serialized_start=8875
  _globals['_MODIFYSNAPSHOTPERMISSIONSARG']._serialized_end=8967
  _globals['_MODIFYSNAPSHOTPERMISSIONSRESULT']._serialized_start=8969
  _globals['_MODIFYSNAPSHOTPERMISSIONSRESULT']._serialized_end=9002
  _globals['_SSMSENDCOMMANDARG']._serialized_start=9005
  _globals['_SSMSENDCOMMANDARG']._serialized_end=9215
  _globals['_SSMSENDCOMMANDARG_PARAMETER']._serialized_start=9175
  _globals['_SSMSENDCOMMANDARG_PARAMETER']._serialized_end=9215
  _globals['_SSMSENDCOMMANDRESULT']._serialized_start=9217
  _globals['_SSMSENDCOMMANDRESULT']._serialized_end=9259
  _globals['_SSMGETCOMMANDOUTCOMEARG']._serialized_start=9262
  _globals['_SSMGETCOMMANDOUTCOMEARG']._serialized_end=9399
  _globals['_SSMGETCOMMANDOUTCOMERESULT']._serialized_start=9401
  _globals['_SSMGETCOMMANDOUTCOMERESULT']._serialized_end=9501
  _globals['_MODIFYINSTANCESECURITYGROUPSARG']._serialized_start=9504
  _globals['_MODIFYINSTANCESECURITYGROUPSARG']._serialized_end=9641
  _globals['_MODIFYINSTANCESECURITYGROUPSRESULT']._serialized_start=9643
  _globals['_MODIFYINSTANCESECURITYGROUPSRESULT']._serialized_end=9679
  _globals['_TAG']._serialized_start=9681
  _globals['_TAG']._serialized_end=9714
  _globals['_SETRESOURCESTAGSARG']._serialized_start=9716
  _globals['_SETRESOURCESTAGSARG']._serialized_end=9827
  _globals['_SETRESOURCESTAGSRESULT']._serialized_start=9829
  _globals['_SETRESOURCESTAGSRESULT']._serialized_end=9853
  _globals['_LISTSNAPSHOTBLOCKSARG']._serialized_start=9856
  _globals['_LISTSNAPSHOTBLOCKSARG']._serialized_end=10018
  _globals['_GETSNAPSHOTBLOCKARG']._serialized_start=10020
  _globals['_GETSNAPSHOTBLOCKARG']._serialized_end=10113
  _globals['_STARTSNAPSHOTARG']._serialized_start=10116
  _globals['_STARTSNAPSHOTARG']._serialized_end=10355
  _globals['_PUTSNAPSHOTBLOCKARG']._serialized_start=10358
  _globals['_PUTSNAPSHOTBLOCKARG']._serialized_end=10509
  _globals['_COMPLETESNAPSHOTARG']._serialized_start=10511
  _globals['_COMPLETESNAPSHOTARG']._serialized_end=10604
  _globals['_INSTANCETYPEINFO']._serialized_start=10606
  _globals['_INSTANCETYPEINFO']._serialized_end=10658
  _globals['_DESCRIBEINSTANCETYPESARG']._serialized_start=10660
  _globals['_DESCRIBEINSTANCETYPESARG']._serialized_end=10730
  _globals['_DESCRIBEINSTANCETYPESRESULT']._serialized_start=10732
  _globals['_DESCRIBEINSTANCETYPESRESULT']._serialized_end=10829
  _globals['_S3BUCKETINFO']._serialized_start=10831
  _globals['_S3BUCKETINFO']._serialized_end=10947
  _globals['_DESCRIBES3BUCKETSARG']._serialized_start=10949
  _globals['_DESCRIBES3BUCKETSARG']._serialized_end=10992
  _globals['_DESCRIBES3BUCKETSRESULT']._serialized_start=10994
  _globals['_DESCRIBES3BUCKETSRESULT']._serialized_end=11083
# @@protoc_insertion_point(module_scope)
