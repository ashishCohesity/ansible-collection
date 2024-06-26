# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: magneto/base/entities/gpfs.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from magneto.base import enums_pb2 as magneto_dot_base_dot_enums__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n magneto/base/entities/gpfs.proto\x12\x15\x63ohesity.magneto.gpfs\x1a\x18magneto/base/enums.proto\"\xee\x02\n\x0b\x43lusterInfo\x12\n\n\x02id\x18\x01 \x01(\x04\x12\x16\n\x0eprimary_server\x18\x02 \x01(\t\x12\x15\n\rces_addresses\x18\x03 \x03(\t\x12\x42\n\rnode_info_vec\x18\x04 \x03(\x0b\x32+.cohesity.magneto.gpfs.ClusterInfo.NodeInfo\x12-\n\x1fuse_path_entity_hash_comparator\x18\x05 \x01(\x08:\x04true\x1a\xb0\x01\n\x08NodeInfo\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\nip_address\x18\x02 \x01(\t\x12Y\n\x12operational_status\x18\x03 \x01(\x0e\x32=.cohesity.magneto.gpfs.ClusterInfo.NodeInfo.OperationalStatus\"\'\n\x11OperationalStatus\x12\x07\n\x03kUp\x10\x00\x12\t\n\x05kDown\x10\x01\"V\n\x0e\x46ilesystemInfo\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04path\x18\x02 \x01(\t\x12\x16\n\x0e\x63\x61pacity_bytes\x18\x03 \x01(\x04\x12\x12\n\nused_bytes\x18\x04 \x01(\x04\"\x97\x02\n\x0b\x46ilesetInfo\x12\x0e\n\x02id\x18\x01 \x01(\x04\x42\x02\x18\x01\x12\x0c\n\x04path\x18\x02 \x01(\t\x12\x17\n\x0f\x66ilesystem_name\x18\x03 \x01(\t\x12\x42\n\x16supported_protocol_vec\x18\x04 \x03(\x0e\x32\".cohesity.magneto.NasProtocol.Type\x12$\n\x16is_independent_fileset\x18\x05 \x01(\x08:\x04true\x12\x0c\n\x04\x66sid\x18\x06 \x01(\t\x12*\n\x1buse_fsid_as_hash_comparator\x18\x07 \x01(\x08:\x05\x66\x61lse\x12-\n\x1fuse_path_entity_hash_comparator\x18\x08 \x01(\x08:\x04true\"}\n\x13\x46ilesetSnapshotInfo\x12\x0f\n\x07snap_id\x18\x01 \x01(\x04\x12\x15\n\rsnapshot_name\x18\x02 \x01(\t\x12\x17\n\x0f\x66ilesystem_name\x18\x03 \x01(\t\x12\x14\n\x0c\x66ileset_name\x18\x04 \x01(\t\x12\x0f\n\x07\x63reated\x18\x05 \x01(\t\"\xb1\x02\n\x06\x45ntity\x12\x30\n\x04type\x18\x01 \x01(\x0e\x32\".cohesity.magneto.gpfs.Entity.Type\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x38\n\x0c\x63luster_info\x18\x03 \x01(\x0b\x32\".cohesity.magneto.gpfs.ClusterInfo\x12>\n\x0f\x66ilesystem_info\x18\x04 \x01(\x0b\x32%.cohesity.magneto.gpfs.FilesystemInfo\x12\x38\n\x0c\x66ileset_info\x18\x05 \x01(\x0b\x32\".cohesity.magneto.gpfs.FilesetInfo\"3\n\x04Type\x12\x0c\n\x08kCluster\x10\x00\x12\x0f\n\x0bkFilesystem\x10\x01\x12\x0c\n\x08kFileset\x10\x02')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'magneto.base.entities.gpfs_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_FILESETINFO'].fields_by_name['id']._loaded_options = None
  _globals['_FILESETINFO'].fields_by_name['id']._serialized_options = b'\030\001'
  _globals['_CLUSTERINFO']._serialized_start=86
  _globals['_CLUSTERINFO']._serialized_end=452
  _globals['_CLUSTERINFO_NODEINFO']._serialized_start=276
  _globals['_CLUSTERINFO_NODEINFO']._serialized_end=452
  _globals['_CLUSTERINFO_NODEINFO_OPERATIONALSTATUS']._serialized_start=413
  _globals['_CLUSTERINFO_NODEINFO_OPERATIONALSTATUS']._serialized_end=452
  _globals['_FILESYSTEMINFO']._serialized_start=454
  _globals['_FILESYSTEMINFO']._serialized_end=540
  _globals['_FILESETINFO']._serialized_start=543
  _globals['_FILESETINFO']._serialized_end=822
  _globals['_FILESETSNAPSHOTINFO']._serialized_start=824
  _globals['_FILESETSNAPSHOTINFO']._serialized_end=949
  _globals['_ENTITY']._serialized_start=952
  _globals['_ENTITY']._serialized_end=1257
  _globals['_ENTITY_TYPE']._serialized_start=1206
  _globals['_ENTITY_TYPE']._serialized_end=1257
# @@protoc_insertion_point(module_scope)
