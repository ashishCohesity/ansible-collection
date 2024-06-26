# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bridge/cloud_chunk_repository/cloud_chunk_repository.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from configs import cluster_config_pb2 as configs_dot_cluster__config__pb2
from bridge.blob_store import blob_store_pb2 as bridge_dot_blob__store_dot_blob__store__pb2
from keychain.base import keychain_pb2 as keychain_dot_base_dot_keychain__pb2
from open_util.base import aes_encryptor_pb2 as open__util_dot_base_dot_aes__encryptor__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n:bridge/cloud_chunk_repository/cloud_chunk_repository.proto\x12&cohesity.bridge.cloud_chunk_repository\x1a\x1c\x63onfigs/cluster_config.proto\x1a\"bridge/blob_store/blob_store.proto\x1a\x1ckeychain/base/keychain.proto\x1a\"open_util/base/aes_encryptor.proto\"\xe7\x05\n\x1b\x43loudChunkFileMetadataProto\x12\x1b\n\x13\x64\x61ta_format_version\x18\x01 \x01(\x05\x12^\n\x11\x63ompression_level\x18\x02 \x01(\x0e\x32\x43.cohesity.configs.ClusterConfigProto.StoragePolicy.CompressionLevel\x12\x65\n\x0e\x63hunk_info_vec\x18\x03 \x03(\x0b\x32M.cohesity.bridge.cloud_chunk_repository.CloudChunkFileMetadataProto.ChunkInfo\x12p\n\x14\x63hunk_group_info_vec\x18\x04 \x03(\x0b\x32R.cohesity.bridge.cloud_chunk_repository.CloudChunkFileMetadataProto.ChunkGroupInfo\x12\x19\n\x11morphed_data_size\x18\x05 \x01(\x05\x12\x13\n\x0btouch_usecs\x18\x06 \x01(\x03\x12%\n\x19max_issued_local_chunk_id\x18\x07 \x01(\x03:\x02-1\x1a\x96\x01\n\tChunkInfo\x12\x39\n\x08\x63hunk_id\x18\x01 \x01(\x0b\x32\'.cohesity.bridge.blob.CloudChunkIdProto\x12N\n\x0c\x63hunk_column\x18\x02 \x01(\x0b\x32\x38.cohesity.bridge.blob.ChunkFileMetadataProto.ChunkColumn\x1a\x81\x01\n\x0e\x43hunkGroupInfo\x12\x15\n\rchunkgroup_id\x18\x01 \x01(\x05\x12X\n\x11\x63hunkgroup_column\x18\x02 \x01(\x0b\x32=.cohesity.bridge.blob.ChunkFileMetadataProto.ChunkGroupColumn\"\xac\x01\n%CloudChunkFileEncryptionMetadataProto\x12/\n\tedek_info\x18\x01 \x01(\x0b\x32\x1c.cohesity.keychain.EdekProto\x12\x1d\n\x15morphed_metadata_size\x18\x02 \x01(\x05\x12\x33\n\x0f\x65ncryption_mode\x18\x03 \x01(\x0e\x32\x1a.cohesity.AESEncryptorModeB,\n*com.cohesity.bridge.cloud_chunk_repository')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'bridge.cloud_chunk_repository.cloud_chunk_repository_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n*com.cohesity.bridge.cloud_chunk_repository'
  _globals['_CLOUDCHUNKFILEMETADATAPROTO']._serialized_start=235
  _globals['_CLOUDCHUNKFILEMETADATAPROTO']._serialized_end=978
  _globals['_CLOUDCHUNKFILEMETADATAPROTO_CHUNKINFO']._serialized_start=696
  _globals['_CLOUDCHUNKFILEMETADATAPROTO_CHUNKINFO']._serialized_end=846
  _globals['_CLOUDCHUNKFILEMETADATAPROTO_CHUNKGROUPINFO']._serialized_start=849
  _globals['_CLOUDCHUNKFILEMETADATAPROTO_CHUNKGROUPINFO']._serialized_end=978
  _globals['_CLOUDCHUNKFILEENCRYPTIONMETADATAPROTO']._serialized_start=981
  _globals['_CLOUDCHUNKFILEENCRYPTIONMETADATAPROTO']._serialized_end=1153
# @@protoc_insertion_point(module_scope)
