# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gaia/dataplane/api/base.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1dgaia/dataplane/api/base.proto\x12\x1b\x63ohesity.gaia.dataplane.api\"\xc2\x03\n\x06Object\x12\x12\n\naccount_id\x18\x01 \x01(\x0c\x12\x11\n\ttenant_id\x18\x02 \x01(\x0c\x12<\n\x04type\x18\x03 \x01(\x0e\x32..cohesity.gaia.dataplane.api.Object.ObjectType\x12\n\n\x02id\x18\x04 \x01(\x0c\x12\x0c\n\x04name\x18\x05 \x01(\t\x12\x43\n\tsnapshots\x18\x06 \x03(\x0b\x32\x30.cohesity.gaia.dataplane.api.Object.SnapshotInfo\x12I\n\x14\x62\x61se_snapshot_handle\x18\x07 \x01(\x0b\x32+.cohesity.gaia.dataplane.api.SnapshotHandle\x1a\x62\n\x0cSnapshotInfo\x12\x44\n\x0fsnapshot_handle\x18\x01 \x01(\x0b\x32+.cohesity.gaia.dataplane.api.SnapshotHandle\x12\x0c\n\x04tags\x18\x02 \x03(\t\"E\n\nObjectType\x12\x0c\n\x08kMailbox\x10\x00\x12\r\n\tkOneDrive\x10\x01\x12\x07\n\x03kVM\x10\x02\x12\x11\n\rkCohesityView\x10\x03\"F\n\x0eSnapshotHandle\x12\x16\n\x0emagneto_job_id\x18\x01 \x01(\x03\x12\x1c\n\x14run_start_time_usecs\x18\x02 \x01(\x03\"+\n\x0fSubObjectHandle\x12\n\n\x02id\x18\x01 \x01(\x0c\x12\x0c\n\x04name\x18\x02 \x01(\t\"\xf1\x01\n\x0c\x44ocumentType\x12<\n\x04type\x18\x01 \x01(\x0e\x32..cohesity.gaia.dataplane.api.DocumentType.Type\x12\x0c\n\x04name\x18\x02 \x01(\t\"\x94\x01\n\x04Type\x12\x0c\n\x08kUnknown\x10\x00\x12\r\n\tkTextFile\x10\x01\x12\x08\n\x04kPDF\x10\x02\x12\x08\n\x04kDoc\x10\x03\x12\t\n\x05kDocx\x10\x04\x12\x08\n\x04kPpt\x10\x05\x12\t\n\x05kPptx\x10\x06\x12\x08\n\x04kXls\x10\x07\x12\t\n\x05kXlsx\x10\x08\x12\x08\n\x04kRtf\x10\t\x12\x08\n\x04kOdf\x10\n\x12\x12\n\x0ekO365EmailBlob\x10\x0b\"\x88\x02\n\x0f\x44ocumentLocator\x12\x11\n\tobject_id\x18\x01 \x01(\x0c\x12\x43\n\x0bobject_type\x18\x02 \x01(\x0e\x32..cohesity.gaia.dataplane.api.Object.ObjectType\x12\x44\n\x0fsnapshot_handle\x18\x03 \x01(\x0b\x32+.cohesity.gaia.dataplane.api.SnapshotHandle\x12G\n\x11sub_object_handle\x18\x04 \x01(\x0b\x32,.cohesity.gaia.dataplane.api.SubObjectHandle\x12\x0e\n\x06\x64oc_id\x18\x05 \x01(\x0c\x42\x1dZ\x1b\x63ohesity/gaia/dataplane/apib\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'gaia.dataplane.api.base_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\033cohesity/gaia/dataplane/api'
  _globals['_OBJECT']._serialized_start=63
  _globals['_OBJECT']._serialized_end=513
  _globals['_OBJECT_SNAPSHOTINFO']._serialized_start=344
  _globals['_OBJECT_SNAPSHOTINFO']._serialized_end=442
  _globals['_OBJECT_OBJECTTYPE']._serialized_start=444
  _globals['_OBJECT_OBJECTTYPE']._serialized_end=513
  _globals['_SNAPSHOTHANDLE']._serialized_start=515
  _globals['_SNAPSHOTHANDLE']._serialized_end=585
  _globals['_SUBOBJECTHANDLE']._serialized_start=587
  _globals['_SUBOBJECTHANDLE']._serialized_end=630
  _globals['_DOCUMENTTYPE']._serialized_start=633
  _globals['_DOCUMENTTYPE']._serialized_end=874
  _globals['_DOCUMENTTYPE_TYPE']._serialized_start=726
  _globals['_DOCUMENTTYPE_TYPE']._serialized_end=874
  _globals['_DOCUMENTLOCATOR']._serialized_start=877
  _globals['_DOCUMENTLOCATOR']._serialized_end=1141
# @@protoc_insertion_point(module_scope)