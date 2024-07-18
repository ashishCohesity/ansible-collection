# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bridge/madrox/stub/rsync_custom_snap_tree_work.proto
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
from bridge.snap_tree import snap_tree_pb2 as bridge_dot_snap__tree_dot_snap__tree__pb2
from bridge.s3_portal.base import s3_metadata_pb2 as bridge_dot_s3__portal_dot_base_dot_s3__metadata__pb2
from bridge.view_keeper import view_metadata_pb2 as bridge_dot_view__keeper_dot_view__metadata__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4bridge/madrox/stub/rsync_custom_snap_tree_work.proto\x12\x16\x63ohesity.bridge.madrox\x1a\x17\x62ridge/base/error.proto\x1a(bridge/madrox/rsync_snap_tree_diff.proto\x1a bridge/snap_tree/snap_tree.proto\x1a\'bridge/s3_portal/base/s3_metadata.proto\x1a&bridge/view_keeper/view_metadata.proto\"\xa6\x03\n\x1cRsyncCustomSnapTreeWorkProto\x12\x35\n\ttree_info\x18\x01 \x01(\x0b\x32\".cohesity.bridge.view.SnapTreeInfo\x12]\n\x08work_vec\x18\x02 \x03(\x0b\x32K.cohesity.bridge.madrox.RsyncCustomSnapTreeWorkProto.CustomSnapTreeWorkUnit\x1a\xef\x01\n\x16\x43ustomSnapTreeWorkUnit\x12;\n\x03key\x18\x01 \x01(\x0b\x32..cohesity.bridge.madrox.CustomSnapTreeKeyProto\x12G\n\toperation\x18\x02 \x01(\x0e\x32\x34.cohesity.bridge.snap_tree.SnapTreeKeyOperation.Type\x12O\n\x17s3object_tree_val_proto\x18\x03 \x01(\x0b\x32..cohesity.bridge.s3.S3ObjectSnapTreeValueProto\"L\n\x1eRsyncCustomSnapTreeResultProto\x12*\n\x05\x65rror\x18\x01 \x01(\x0b\x32\x1b.cohesity.bridge.ErrorProto')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'bridge.madrox.stub.rsync_custom_snap_tree_work_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_RSYNCCUSTOMSNAPTREEWORKPROTO']._serialized_start=263
  _globals['_RSYNCCUSTOMSNAPTREEWORKPROTO']._serialized_end=685
  _globals['_RSYNCCUSTOMSNAPTREEWORKPROTO_CUSTOMSNAPTREEWORKUNIT']._serialized_start=446
  _globals['_RSYNCCUSTOMSNAPTREEWORKPROTO_CUSTOMSNAPTREEWORKUNIT']._serialized_end=685
  _globals['_RSYNCCUSTOMSNAPTREERESULTPROTO']._serialized_start=687
  _globals['_RSYNCCUSTOMSNAPTREERESULTPROTO']._serialized_end=763
# @@protoc_insertion_point(module_scope)