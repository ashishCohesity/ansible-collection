# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: apollo/mr/algorithms/physical_storage_reporter/physical_storage_reporter.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from bridge.blob_store import blob_store_pb2 as bridge_dot_blob__store_dot_blob__store__pb2
from configs import cluster_config_pb2 as configs_dot_cluster__config__pb2
from bookkeeper.base import bookkeeper_pb2 as bookkeeper_dot_base_dot_bookkeeper__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nNapollo/mr/algorithms/physical_storage_reporter/physical_storage_reporter.proto\x12\x1d\x63ohesity.apollo.mr.algorithms\x1a\"bridge/blob_store/blob_store.proto\x1a\x1c\x63onfigs/cluster_config.proto\x1a bookkeeper/base/bookkeeper.proto\"\xc2\x07\n\'PhysicalStorageReporterContextDataProto\x12\x42\n\x14\x63luster_config_proto\x18\x01 \x01(\x0b\x32$.cohesity.configs.ClusterConfigProto\x12#\n\x17max_view_snaptree_level\x18\x02 \x01(\x05:\x02-1\x12#\n\x17max_blob_snaptree_level\x18\x03 \x01(\x05:\x02-1\x12\x17\n\x0fmax_group_depth\x18\x04 \x01(\x05\x12$\n\x15should_build_pipeline\x18\x06 \x01(\x08:\x05\x66\x61lse\x12\x14\n\x0cgroup_id_vec\x18\x07 \x03(\x03\x12?\n\x10group_config_vec\x18\x08 \x03(\x0b\x32%.cohesity.bookkeeper.GroupConfigProto\x12o\n\x0esd_spl_grp_map\x18\t \x03(\x0b\x32W.cohesity.apollo.mr.algorithms.PhysicalStorageReporterContextDataProto.SdSplGrpMapEntry\x12\x1f\n\x17relevant_nmspce_grp_idx\x18\n \x01(\x05\x12#\n\x1bnon_relevant_nmspce_grp_idx\x18\x0b \x01(\x05\x12\x1a\n\x12\x61ll_nmspce_grp_idx\x18\x0c \x01(\x05\x12.\n&pst_level0_reducer_num_shards_per_node\x18\r \x01(\x03\x12\x34\n,pst_minion_brick_reducer_num_shards_per_node\x18\x0e \x01(\x03\x12\x33\n+pst_minion_blob_reducer_num_shards_per_node\x18\x0f \x01(\x03\x1ah\n\x19StorageDomainSpecialGroup\x12\x19\n\x11storage_domain_id\x18\x01 \x01(\x03\x12\x1b\n\x13storage_domain_name\x18\x02 \x01(\t\x12\x13\n\x0b\x65ntity_name\x18\x03 \x01(\t\x1a\x94\x01\n\x10SdSplGrpMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12o\n\x05value\x18\x02 \x01(\x0b\x32`.cohesity.apollo.mr.algorithms.PhysicalStorageReporterContextDataProto.StorageDomainSpecialGroup:\x02\x38\x01J\x04\x08\x05\x10\x06\"\xf7\x01\n\x1fPhysicalStorageReporterKeyProto\x12\x0f\n\x07node_id\x18\x01 \x01(\x03\x12\x0e\n\x06offset\x18\x02 \x01(\x03\x12\x0e\n\x06id_vec\x18\x03 \x03(\x03\x12?\n\x10group_config_vec\x18\x04 \x03(\x0b\x32%.cohesity.bookkeeper.GroupConfigProto\x12\x0f\n\x07\x62lob_id\x18\x05 \x01(\x03\x12\x14\n\x0c\x62rick_number\x18\x06 \x01(\x03\x12\x15\n\rbrick_node_id\x18\x07 \x01(\x03\x12\x11\n\tindex_vec\x18\x08 \x03(\x05\x12\x11\n\tbucket_id\x18\t \x01(\x03\"\xe2\n\n!PhysicalStorageReporterValueProto\x12\x15\n\rchild_node_id\x18\x01 \x01(\x03\x12\x0e\n\x06offset\x18\x03 \x01(\x03\x12\x12\n\nbrick_size\x18\x04 \x01(\x03\x12\x15\n\rreserved_size\x18\x05 \x01(\x03\x12\x38\n\x0c\x63hunk_id_vec\x18\x06 \x03(\x0b\x32\".cohesity.bridge.blob.ChunkIdProto\x12\x1b\n\x13\x63hunk_logical_bytes\x18\x07 \x01(\x03\x12\x1b\n\x13\x63hunk_morphed_bytes\x18\x08 \x01(\x03\x12!\n\x19\x63hunk_morphed_bytes_cloud\x18\t \x01(\x03\x12\"\n\x1a\x63hunk_physical_bytes_cloud\x18\n \x01(\x03\x12\x1c\n\x14\x63hunk_physical_bytes\x18\x0b \x01(\x03\x12\x1b\n\x13\x62rick_bytes_logical\x18\r \x01(\x03\x12\x0e\n\x06id_vec\x18\x0e \x03(\x03\x12\x33\n\tobj_proto\x18\x0f \x01(\x0b\x32 .cohesity.bookkeeper.ObjectProto\x12\x18\n\x10root_snaptree_id\x18\x10 \x01(\x03\x12\x17\n\x0fnum_directories\x18\x11 \x01(\x03\x12\x19\n\x11num_regular_files\x18\x12 \x01(\x03\x12!\n\x19regular_files_usage_bytes\x18\x13 \x01(\x03\x12\x18\n\x10num_minion_files\x18\x14 \x01(\x03\x12 \n\x18minion_files_usage_bytes\x18\x15 \x01(\x03\x12\x16\n\x0enum_mega_files\x18\x16 \x01(\x03\x12\x1e\n\x16mega_files_usage_bytes\x18\x17 \x01(\x03\x12\x15\n\rstats_present\x18\x18 \x01(\x08\x12\x1a\n\x12scribe_row_version\x18\x19 \x01(\x03\x12?\n\x10group_config_vec\x18\x1a \x03(\x0b\x32%.cohesity.bookkeeper.GroupConfigProto\x12\x17\n\x0fis_unique_chunk\x18\x1b \x01(\x08\x12\x14\n\x0clogical_size\x18\x1c \x01(\x03\x12`\n\rblob_info_vec\x18\x1d \x03(\x0b\x32I.cohesity.apollo.mr.algorithms.PhysicalStorageReporterValueProto.BlobInfo\x12\x15\n\rrefd_by_inode\x18\x1e \x01(\x08\x12\x14\n\x0c\x62rick_number\x18\x1f \x01(\x03\x12\x15\n\rbrick_node_id\x18  \x01(\x03\x12\x15\n\rinode_node_id\x18! \x01(\x03\x12\"\n\x1aunique_chunk_logical_bytes\x18\" \x01(\x03\x12#\n\x1bunique_chunk_physical_bytes\x18# \x01(\x03\x12\"\n\x1aunique_chunk_morphed_bytes\x18$ \x01(\x03\x12)\n!unique_chunk_physical_bytes_cloud\x18% \x01(\x03\x12(\n unique_chunk_morphed_bytes_cloud\x18& \x01(\x03\x12\x11\n\tindex_vec\x18\' \x03(\x05\x12\x19\n\x11storage_domain_id\x18( \x01(\x03\x12\x11\n\tview_name\x18) \x01(\t\x12\x13\n\x0bis_internal\x18* \x01(\x08\x12\x1d\n\x15is_relevant_namespace\x18+ \x01(\x08\x1a.\n\x08\x42lobInfo\x12\x0f\n\x07\x62lob_id\x18\x01 \x01(\x03\x12\x11\n\tis_minion\x18\x02 \x01(\x08J\x04\x08\x02\x10\x03')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'apollo.mr.algorithms.physical_storage_reporter.physical_storage_reporter_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_PHYSICALSTORAGEREPORTERCONTEXTDATAPROTO_SDSPLGRPMAPENTRY']._loaded_options = None
  _globals['_PHYSICALSTORAGEREPORTERCONTEXTDATAPROTO_SDSPLGRPMAPENTRY']._serialized_options = b'8\001'
  _globals['_PHYSICALSTORAGEREPORTERCONTEXTDATAPROTO']._serialized_start=214
  _globals['_PHYSICALSTORAGEREPORTERCONTEXTDATAPROTO']._serialized_end=1176
  _globals['_PHYSICALSTORAGEREPORTERCONTEXTDATAPROTO_STORAGEDOMAINSPECIALGROUP']._serialized_start=915
  _globals['_PHYSICALSTORAGEREPORTERCONTEXTDATAPROTO_STORAGEDOMAINSPECIALGROUP']._serialized_end=1019
  _globals['_PHYSICALSTORAGEREPORTERCONTEXTDATAPROTO_SDSPLGRPMAPENTRY']._serialized_start=1022
  _globals['_PHYSICALSTORAGEREPORTERCONTEXTDATAPROTO_SDSPLGRPMAPENTRY']._serialized_end=1170
  _globals['_PHYSICALSTORAGEREPORTERKEYPROTO']._serialized_start=1179
  _globals['_PHYSICALSTORAGEREPORTERKEYPROTO']._serialized_end=1426
  _globals['_PHYSICALSTORAGEREPORTERVALUEPROTO']._serialized_start=1429
  _globals['_PHYSICALSTORAGEREPORTERVALUEPROTO']._serialized_end=2807
  _globals['_PHYSICALSTORAGEREPORTERVALUEPROTO_BLOBINFO']._serialized_start=2755
  _globals['_PHYSICALSTORAGEREPORTERVALUEPROTO_BLOBINFO']._serialized_end=2801
# @@protoc_insertion_point(module_scope)