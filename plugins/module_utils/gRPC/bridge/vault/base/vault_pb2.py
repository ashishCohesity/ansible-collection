# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bridge/vault/base/vault.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from bridge.vault.base import azure_pb2 as bridge_dot_vault_dot_base_dot_azure__pb2
from bridge.vault.base import glacier_pb2 as bridge_dot_vault_dot_base_dot_glacier__pb2
from bridge.vault.base import nas_pb2 as bridge_dot_vault_dot_base_dot_nas__pb2
from bridge.vault.base import nearline_pb2 as bridge_dot_vault_dot_base_dot_nearline__pb2
from bridge.vault.base import on_disk_vault_pb2 as bridge_dot_vault_dot_base_dot_on__disk__vault__pb2
from bridge.vault.base import qstar_pb2 as bridge_dot_vault_dot_base_dot_qstar__pb2
from bridge.vault.base import s3_pb2 as bridge_dot_vault_dot_base_dot_s3__pb2
from bridge.vault.base import worm_pb2 as bridge_dot_vault_dot_base_dot_worm__pb2
from configs import cluster_config_pb2 as configs_dot_cluster__config__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1d\x62ridge/vault/base/vault.proto\x12\x15\x63ohesity.bridge.vault\x1a\x1d\x62ridge/vault/base/azure.proto\x1a\x1f\x62ridge/vault/base/glacier.proto\x1a\x1b\x62ridge/vault/base/nas.proto\x1a bridge/vault/base/nearline.proto\x1a%bridge/vault/base/on_disk_vault.proto\x1a\x1d\x62ridge/vault/base/qstar.proto\x1a\x1a\x62ridge/vault/base/s3.proto\x1a\x1c\x62ridge/vault/base/worm.proto\x1a\x1c\x63onfigs/cluster_config.proto\"\xd9\x06\n\x11\x41\x64\x61pterAttributes\x12,\n\x15max_object_size_bytes\x18\x01 \x01(\x03:\r1099511627776\x12\x31\n\x1amax_object_part_size_bytes\x18\x02 \x01(\x03:\r1099511627776\x12\x1f\n\x14max_parts_per_object\x18\x03 \x01(\x05:\x01\x31\x12$\n\x16is_streaming_supported\x18\x04 \x01(\x08:\x04true\x12\x1a\n\x12\x66inalize_with_data\x18\x05 \x01(\x08\x12\"\n\x1aparallel_upload_per_object\x18\x06 \x01(\x08\x12.\n\x1d\x63loud_spill_upload_block_size\x18\x07 \x01(\x05:\x07\x31\x30\x34\x38\x35\x37\x36\x12#\n\x1bprepare_for_upload_required\x18\x08 \x01(\x08\x12(\n\x1aoverwriting_data_supported\x18\t \x01(\x08:\x04true\x12\"\n\x1ajournal_data_before_upload\x18\n \x01(\x08\x12/\n\'allow_finalizing_objects_multiple_times\x18\x0b \x01(\x08\x12\x30\n!supports_object_range_preparation\x18\x0c \x01(\x08:\x05\x66\x61lse\x12\'\n\x18supports_objects_caching\x18\r \x01(\x08:\x05\x66\x61lse\x12(\n\x19\x63url_throttling_supported\x18\x0e \x01(\x08:\x05\x66\x61lse\x12+\n\x1c\x63opy_object_ranges_supported\x18\x0f \x01(\x08:\x05\x66\x61lse\x12(\n\x19prefix_deletion_supported\x18\x10 \x01(\x08:\x05\x66\x61lse\x12&\n\x17get_data_lock_supported\x18\x11 \x01(\x08:\x05\x66\x61lse\x12!\n\x12versioning_enabled\x18\x12 \x01(\x08:\x05\x66\x61lse\x12\x30\n!validate_md5_checksum_for_uploads\x18\x13 \x01(\x08:\x05\x66\x61lse\x12/\n validate_object_ranges_supported\x18\x14 \x01(\x08:\x05\x66\x61lse\"\xee\x03\n\x1dVaultObjectCreateContextProto\x12H\n\x14\x61zure_create_context\x18\x01 \x01(\x0b\x32*.cohesity.bridge.vault.azure.CreateContext\x12\x42\n\x11s3_create_context\x18\x08 \x01(\x0b\x32\'.cohesity.bridge.vault.s3.CreateContext\x12\"\n\x1amax_object_part_size_bytes\x18\x02 \x01(\x03\x12\x1e\n\x0fis_object_empty\x18\x04 \x01(\x08:\x05\x66\x61lse\x12 \n\x11\x63ompute_part_size\x18\x05 \x01(\x08:\x05\x66\x61lse\x12\x1b\n\x13object_logical_size\x18\x06 \x01(\x03\x12,\n\x1e\x63\x61n_skip_empty_object_creation\x18\x07 \x01(\x08:\x04true\x12 \n\x18retention_timestamp_secs\x18\t \x01(\x03\x12\x41\n\x0eretention_mode\x18\n \x01(\x0e\x32).cohesity.bridge.vault.RetentionMode.Type\x12#\n\x14reuse_object_version\x18\x0b \x01(\x08:\x05\x66\x61lseJ\x04\x08\x03\x10\x04\"\xa0\x04\n\x17VaultUploadContextProto\x12N\n\x17nearline_upload_context\x18\x01 \x01(\x0b\x32-.cohesity.bridge.vault.nearline.UploadContext\x12L\n\x16glacier_upload_context\x18\x02 \x01(\x0b\x32,.cohesity.bridge.vault.glacier.UploadContext\x12\x42\n\x11s3_upload_context\x18\x03 \x01(\x0b\x32\'.cohesity.bridge.vault.s3.UploadContext\x12H\n\x14\x61zure_upload_context\x18\x04 \x01(\x0b\x32*.cohesity.bridge.vault.azure.UploadContext\x12H\n\x14qstar_upload_context\x18\x05 \x01(\x0b\x32*.cohesity.bridge.vault.qstar.UploadContext\x12\x44\n\x12nas_upload_context\x18\x06 \x01(\x0b\x32(.cohesity.bridge.vault.nas.UploadContext\x12\x13\n\x0bobject_name\x18\x07 \x01(\t\x12\x19\n\x11optimal_part_size\x18\x08 \x01(\x03\x12\x19\n\x11object_version_id\x18\t \x01(\t\"\xe8\x04\n\x19VaultDownloadContextProto\x12R\n\x19nearline_download_context\x18\x01 \x01(\x0b\x32/.cohesity.bridge.vault.nearline.DownloadContext\x12P\n\x18glacier_download_context\x18\x02 \x01(\x0b\x32..cohesity.bridge.vault.glacier.DownloadContext\x12L\n\x16\x61zure_download_context\x18\x03 \x01(\x0b\x32,.cohesity.bridge.vault.azure.DownloadContext\x12L\n\x16qstar_download_context\x18\x04 \x01(\x0b\x32,.cohesity.bridge.vault.qstar.DownloadContext\x12H\n\x14nas_download_context\x18\x05 \x01(\x0b\x32*.cohesity.bridge.vault.nas.DownloadContext\x12\x46\n\x13s3_download_context\x18\x06 \x01(\x0b\x32).cohesity.bridge.vault.s3.DownloadContext\x12\\\n\x1eon_disk_vault_download_context\x18\x07 \x01(\x0b\x32\x34.cohesity.bridge.vault.on_disk_vault.DownloadContext\x12\x19\n\x11object_version_id\x18\x08 \x01(\t\"\x9c\x03\n\x1cVaultListObjectsContextProto\x12J\n\x06params\x18\x01 \x01(\x0b\x32:.cohesity.bridge.vault.VaultListObjectsContextProto.Params\x12\x0e\n\x06\x63ookie\x18\x02 \x01(\t\x12W\n\x1cglacier_list_objects_context\x18\x03 \x01(\x0b\x32\x31.cohesity.bridge.vault.glacier.ListObjectsContext\x1a\xc6\x01\n\x06Params\x12\x0e\n\x06prefix\x18\x01 \x01(\t\x12\x0e\n\x06\x63ookie\x18\x02 \x01(\t\x12\x19\n\x0bmax_objects\x18\x03 \x01(\x05:\x04\x31\x30\x32\x34\x12\x18\n\x10start_time_usecs\x18\x04 \x01(\x03\x12\x16\n\x0e\x65nd_time_usecs\x18\x05 \x01(\x03\x12\"\n\x13is_prefix_directory\x18\x06 \x01(\x08:\x05\x66\x61lse\x12\x18\n\x10starts_after_key\x18\x07 \x01(\t\x12\x11\n\tdelimiter\x18\x08 \x01(\t\"E\n\rMediaInfoData\x12\x0f\n\x07\x62\x61rcode\x18\x01 \x01(\t\x12\x10\n\x08location\x18\x02 \x01(\t\x12\x11\n\tis_online\x18\x03 \x01(\x08\"m\n\x13ObjectFileBlockInfo\x12\x0e\n\x06offset\x18\x01 \x01(\x03\x12\x0c\n\x04size\x18\x02 \x01(\x03\x12\x38\n\nmedia_info\x18\x03 \x01(\x0b\x32$.cohesity.bridge.vault.MediaInfoData\"\xd5\x02\n\x0fVaultObjectInfo\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x0f\n\x04size\x18\x03 \x01(\x03:\x01\x30\x12\x15\n\rstorage_class\x18\x04 \x01(\t\x12\x1b\n\x0c\x61rchive_tier\x18\x05 \x01(\x08:\x05\x66\x61lse\x12\x44\n\x11s3_restore_status\x18\x06 \x01(\x0b\x32).cohesity.bridge.vault.s3.DownloadContext\x12Q\n\x0f\x63loud_tier_type\x18\x07 \x01(\x0b\x32\x38.cohesity.configs.ClusterConfigProto.Vault.CloudTierType\x12\x1f\n\x13last_modified_epoch\x18\x08 \x01(\x03:\x02-1\x12\x12\n\nversion_id\x18\t \x01(\t\x12\x0c\n\x04\x63tag\x18\n \x01(\t\"\x88\x01\n\x13LifecyclePolicyInfo\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x19\n\x11lifecycle_enabled\x18\x02 \x01(\x08\x12\x15\n\rdowntier_days\x18\x03 \x01(\x05\x12\x15\n\rdeletion_days\x18\x04 \x01(\x05\x12\x1a\n\x12\x65xpiration_enabled\x18\x05 \x01(\x08\"\x9f\x02\n\x0cVaultExtInfo\x12\x41\n\ncerts_data\x18\x01 \x01(\x0b\x32-.cohesity.bridge.vault.VaultExtInfo.CertsData\x12\x1d\n\x15private_endpoint_fqdn\x18\x0e \x01(\t\x12%\n\x1dprivate_endpoint_ipv4_address\x18\x0f \x01(\t\x1a\x85\x01\n\tCertsData\x12\x1b\n\x13\x63\x61_trusted_cert_pem\x18\x01 \x01(\x0c\x12\x17\n\x0f\x63lient_cert_pem\x18\x02 \x01(\t\x12#\n\x1b\x63lient_cert_private_key_pem\x18\x03 \x01(\t\x12\x1d\n\x15\x63reate_timestamp_usec\x18\x04 \x01(\x03\"\x84\x03\n\x0bVaultParams\x12H\n\x0erestore_params\x18\x01 \x01(\x0b\x32\x30.cohesity.bridge.vault.VaultParams.RestoreParams\x1a\xaa\x02\n\rRestoreParams\x12I\n\x07glacier\x18\x01 \x01(\x0b\x32\x38.cohesity.bridge.vault.VaultParams.RestoreParams.Glacier\x12\'\n\x18\x61llow_marked_for_removal\x18\x02 \x01(\x08:\x05\x66\x61lse\x1a\xa4\x01\n\x07Glacier\x12^\n\x0eretrieval_type\x18\x01 \x01(\x0e\x32\x46.cohesity.bridge.vault.VaultParams.RestoreParams.Glacier.RetrievalType\"9\n\rRetrievalType\x12\r\n\tkStandard\x10\x00\x12\t\n\x05kBulk\x10\x01\x12\x0e\n\nkExpedited\x10\x02\"\x87\x02\n\x17VaultUptierContextProto\x12\x44\n\x11s3_uptier_context\x18\x01 \x01(\x0b\x32).cohesity.bridge.vault.s3.DownloadContext\x12Z\n\x1con_disk_vault_uptier_context\x18\x02 \x01(\x0b\x32\x34.cohesity.bridge.vault.on_disk_vault.DownloadContext\x12J\n\x14\x61zure_uptier_context\x18\x03 \x01(\x0b\x32,.cohesity.bridge.vault.azure.DownloadContext\"\x99\x01\n\x12\x44\x61taLockPolicyInfo\x12\x18\n\x10\x64\x61talock_enabled\x18\x01 \x01(\x08\x12\x16\n\x0eretention_days\x18\x02 \x01(\x05\x12\x17\n\x0fretention_years\x18\x03 \x01(\x05\x12\x16\n\x0eretention_secs\x18\x04 \x01(\x05\x12 \n\x18\x62ucket_worm_lock_enabled\x18\x05 \x01(\x08')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'bridge.vault.base.vault_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_ADAPTERATTRIBUTES']._serialized_start=342
  _globals['_ADAPTERATTRIBUTES']._serialized_end=1199
  _globals['_VAULTOBJECTCREATECONTEXTPROTO']._serialized_start=1202
  _globals['_VAULTOBJECTCREATECONTEXTPROTO']._serialized_end=1696
  _globals['_VAULTUPLOADCONTEXTPROTO']._serialized_start=1699
  _globals['_VAULTUPLOADCONTEXTPROTO']._serialized_end=2243
  _globals['_VAULTDOWNLOADCONTEXTPROTO']._serialized_start=2246
  _globals['_VAULTDOWNLOADCONTEXTPROTO']._serialized_end=2862
  _globals['_VAULTLISTOBJECTSCONTEXTPROTO']._serialized_start=2865
  _globals['_VAULTLISTOBJECTSCONTEXTPROTO']._serialized_end=3277
  _globals['_VAULTLISTOBJECTSCONTEXTPROTO_PARAMS']._serialized_start=3079
  _globals['_VAULTLISTOBJECTSCONTEXTPROTO_PARAMS']._serialized_end=3277
  _globals['_MEDIAINFODATA']._serialized_start=3279
  _globals['_MEDIAINFODATA']._serialized_end=3348
  _globals['_OBJECTFILEBLOCKINFO']._serialized_start=3350
  _globals['_OBJECTFILEBLOCKINFO']._serialized_end=3459
  _globals['_VAULTOBJECTINFO']._serialized_start=3462
  _globals['_VAULTOBJECTINFO']._serialized_end=3803
  _globals['_LIFECYCLEPOLICYINFO']._serialized_start=3806
  _globals['_LIFECYCLEPOLICYINFO']._serialized_end=3942
  _globals['_VAULTEXTINFO']._serialized_start=3945
  _globals['_VAULTEXTINFO']._serialized_end=4232
  _globals['_VAULTEXTINFO_CERTSDATA']._serialized_start=4099
  _globals['_VAULTEXTINFO_CERTSDATA']._serialized_end=4232
  _globals['_VAULTPARAMS']._serialized_start=4235
  _globals['_VAULTPARAMS']._serialized_end=4623
  _globals['_VAULTPARAMS_RESTOREPARAMS']._serialized_start=4325
  _globals['_VAULTPARAMS_RESTOREPARAMS']._serialized_end=4623
  _globals['_VAULTPARAMS_RESTOREPARAMS_GLACIER']._serialized_start=4459
  _globals['_VAULTPARAMS_RESTOREPARAMS_GLACIER']._serialized_end=4623
  _globals['_VAULTPARAMS_RESTOREPARAMS_GLACIER_RETRIEVALTYPE']._serialized_start=4566
  _globals['_VAULTPARAMS_RESTOREPARAMS_GLACIER_RETRIEVALTYPE']._serialized_end=4623
  _globals['_VAULTUPTIERCONTEXTPROTO']._serialized_start=4626
  _globals['_VAULTUPTIERCONTEXTPROTO']._serialized_end=4889
  _globals['_DATALOCKPOLICYINFO']._serialized_start=4892
  _globals['_DATALOCKPOLICYINFO']._serialized_end=5045
# @@protoc_insertion_point(module_scope)
