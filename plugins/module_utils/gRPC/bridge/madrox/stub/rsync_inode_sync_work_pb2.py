# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bridge/madrox/stub/rsync_inode_sync_work.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from bridge.base import error_pb2 as bridge_dot_base_dot_error__pb2
from bridge.madrox import rsync_snap_tree_diff_pb2 as bridge_dot_madrox_dot_rsync__snap__tree__diff__pb2
from bridge.snap_fs import dedup_range_pb2 as bridge_dot_snap__fs_dot_dedup__range__pb2
from bridge.snap_fs import snap_fs_metadata_pb2 as bridge_dot_snap__fs_dot_snap__fs__metadata__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.bridge/madrox/stub/rsync_inode_sync_work.proto\x12\x16\x63ohesity.bridge.madrox\x1a\x17\x62ridge/base/error.proto\x1a(bridge/madrox/rsync_snap_tree_diff.proto\x1a bridge/snap_fs/dedup_range.proto\x1a%bridge/snap_fs/snap_fs_metadata.proto\"\xda\x01\n\x1aRsyncFileDataSyncWorkProto\x12\x1b\n\x13namespace_root_name\x18\x01 \x02(\t\x12\x15\n\rfile_dst_path\x18\x02 \x02(\x0c\x12\x1a\n\x12is_non_dedup_write\x18\x03 \x01(\x08\x12\x38\n\x0b\x64\x65\x64up_range\x18\x04 \x01(\x0b\x32#.cohesity.bridge.snap_fs.DedupRange\x12\x15\n\rpayload_bytes\x18\x05 \x01(\x05\x12\x1b\n\x13\x66orwarding_disabled\x18\x06 \x01(\x08\"\xa5\x01\n\x1fRsyncFileDataMissingRangesProto\x12P\n\trange_vec\x18\x01 \x03(\x0b\x32=.cohesity.bridge.madrox.RsyncFileDataMissingRangesProto.Range\x1a\x30\n\x05Range\x12\x13\n\x0b\x66ile_offset\x18\x01 \x02(\x03\x12\x12\n\nsize_bytes\x18\x02 \x02(\x03\"\xc6\x03\n\x1fRsyncApplyEntityActionWorkProto\x12\x1b\n\x13namespace_root_name\x18\x01 \x02(\t\x12\x61\n\x10\x61pply_action_vec\x18\x02 \x03(\x0b\x32G.cohesity.bridge.madrox.RsyncApplyEntityActionWorkProto.ApplyActionInfo\x12\x17\n\x0fis_roll_forward\x18\x03 \x01(\x08\x12%\n\x1d\x65xpected_final_entries_in_dir\x18\x04 \x01(\x05\x1a\xe2\x01\n\x0f\x41pplyActionInfo\x12>\n\toperation\x18\x01 \x01(\x0e\x32+.cohesity.bridge.madrox.RsyncOperation.Type\x12\x10\n\x08src_path\x18\x02 \x01(\x0c\x12\x13\n\x0btarget_path\x18\x03 \x01(\x0c\x12I\n\x14target_path_metadata\x18\x04 \x01(\x0b\x32+.cohesity.bridge.snap_fs.InodeMetadataProto\x12\x1d\n\x15is_missing_inode_work\x18\x05 \x01(\x08\"~\n\x1bRsyncVerifyDirSyncWorkProto\x12\x1b\n\x13root_namespace_name\x18\x01 \x01(\t\x12\x14\n\x0ctmp_dir_name\x18\x02 \x01(\t\x12\x16\n\x0e\x64irectory_path\x18\x03 \x01(\x0c\x12\x14\n\x0cnum_children\x18\x04 \x01(\x05\"y\n\x1dRsyncVerifyDirSyncResultProto\x12*\n\x05\x65rror\x18\x01 \x01(\x0b\x32\x1b.cohesity.bridge.ErrorProto\x12\x14\n\x0cnum_children\x18\x02 \x01(\x05\x12\x16\n\x0e\x63hild_name_vec\x18\x03 \x03(\x0c\"\xca\x01\n!RsyncFindMissingEntitiesWorkProto\x12\x61\n\x0f\x66ind_action_vec\x18\x01 \x03(\x0b\x32H.cohesity.bridge.madrox.RsyncFindMissingEntitiesWorkProto.FindActionInfo\x12\x1b\n\x13root_namespace_name\x18\x02 \x01(\t\x1a%\n\x0e\x46indActionInfo\x12\x13\n\x0b\x65ntity_path\x18\x01 \x01(\x0c\"q\n\"RsyncFindMissingEntitiesWorkResult\x12*\n\x05\x65rror\x18\x01 \x01(\x0b\x32\x1b.cohesity.bridge.ErrorProto\x12\x1f\n\x17missing_entity_name_vec\x18\x02 \x03(\x0c')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'bridge.madrox.stub.rsync_inode_sync_work_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_RSYNCFILEDATASYNCWORKPROTO']._serialized_start=215
  _globals['_RSYNCFILEDATASYNCWORKPROTO']._serialized_end=433
  _globals['_RSYNCFILEDATAMISSINGRANGESPROTO']._serialized_start=436
  _globals['_RSYNCFILEDATAMISSINGRANGESPROTO']._serialized_end=601
  _globals['_RSYNCFILEDATAMISSINGRANGESPROTO_RANGE']._serialized_start=553
  _globals['_RSYNCFILEDATAMISSINGRANGESPROTO_RANGE']._serialized_end=601
  _globals['_RSYNCAPPLYENTITYACTIONWORKPROTO']._serialized_start=604
  _globals['_RSYNCAPPLYENTITYACTIONWORKPROTO']._serialized_end=1058
  _globals['_RSYNCAPPLYENTITYACTIONWORKPROTO_APPLYACTIONINFO']._serialized_start=832
  _globals['_RSYNCAPPLYENTITYACTIONWORKPROTO_APPLYACTIONINFO']._serialized_end=1058
  _globals['_RSYNCVERIFYDIRSYNCWORKPROTO']._serialized_start=1060
  _globals['_RSYNCVERIFYDIRSYNCWORKPROTO']._serialized_end=1186
  _globals['_RSYNCVERIFYDIRSYNCRESULTPROTO']._serialized_start=1188
  _globals['_RSYNCVERIFYDIRSYNCRESULTPROTO']._serialized_end=1309
  _globals['_RSYNCFINDMISSINGENTITIESWORKPROTO']._serialized_start=1312
  _globals['_RSYNCFINDMISSINGENTITIESWORKPROTO']._serialized_end=1514
  _globals['_RSYNCFINDMISSINGENTITIESWORKPROTO_FINDACTIONINFO']._serialized_start=1477
  _globals['_RSYNCFINDMISSINGENTITIESWORKPROTO_FINDACTIONINFO']._serialized_end=1514
  _globals['_RSYNCFINDMISSINGENTITIESWORKRESULT']._serialized_start=1516
  _globals['_RSYNCFINDMISSINGENTITIESWORKRESULT']._serialized_end=1629
# @@protoc_insertion_point(module_scope)