# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bridge/s3_portal/base/swift.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!bridge/s3_portal/base/swift.proto\x12\x18\x63ohesity.bridge.s3.swift\":\n\x0fSwiftAccountKey\x12\x11\n\ttenant_id\x18\x01 \x01(\t\x12\x14\n\x0c\x61\x63\x63ount_name\x18\x02 \x01(\t\"\xb2\x01\n\x11SwiftAccountValue\x12R\n\x0cmetadata_map\x18\x01 \x03(\x0b\x32<.cohesity.bridge.s3.swift.SwiftAccountValue.MetadataMapEntry\x12\x15\n\rcreation_time\x18\x02 \x01(\x03\x1a\x32\n\x10MetadataMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"[\n\x13SwiftContainerUsage\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x14\n\x05\x63ount\x18\x02 \x01(\x01R\x05\x63ount\x12\x1a\n\x0busage_bytes\x18\x03 \x01(\x01R\x05\x62ytes\"_\n\x1bSwiftGetAccountResponseBody\x12@\n\tcontainer\x18\x01 \x03(\x0b\x32-.cohesity.bridge.s3.swift.SwiftContainerUsage\"\xbe\x01\n\x16SwiftListObjectsEntity\x12\x1a\n\x0busage_bytes\x18\x01 \x01(\x01R\x05\x62ytes\x12$\n\rlast_modified\x18\x02 \x01(\tR\rlast_modified\x12\x12\n\x04hash\x18\x03 \x01(\tR\x04hash\x12\x12\n\x04name\x18\x04 \x01(\tR\x04name\x12\"\n\x0c\x63ontent_type\x18\x05 \x01(\tR\x0c\x63ontent_type\x12\x16\n\x06subdir\x18\x06 \x01(\tR\x06subdir\"s\n\x1dSwiftGetContainerResponseBody\x12R\n\x0blist_result\x18\x01 \x03(\x0b\x32\x30.cohesity.bridge.s3.swift.SwiftListObjectsEntityR\x0blist_result')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'bridge.s3_portal.base.swift_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_SWIFTACCOUNTVALUE_METADATAMAPENTRY']._loaded_options = None
  _globals['_SWIFTACCOUNTVALUE_METADATAMAPENTRY']._serialized_options = b'8\001'
  _globals['_SWIFTACCOUNTKEY']._serialized_start=63
  _globals['_SWIFTACCOUNTKEY']._serialized_end=121
  _globals['_SWIFTACCOUNTVALUE']._serialized_start=124
  _globals['_SWIFTACCOUNTVALUE']._serialized_end=302
  _globals['_SWIFTACCOUNTVALUE_METADATAMAPENTRY']._serialized_start=252
  _globals['_SWIFTACCOUNTVALUE_METADATAMAPENTRY']._serialized_end=302
  _globals['_SWIFTCONTAINERUSAGE']._serialized_start=304
  _globals['_SWIFTCONTAINERUSAGE']._serialized_end=395
  _globals['_SWIFTGETACCOUNTRESPONSEBODY']._serialized_start=397
  _globals['_SWIFTGETACCOUNTRESPONSEBODY']._serialized_end=492
  _globals['_SWIFTLISTOBJECTSENTITY']._serialized_start=495
  _globals['_SWIFTLISTOBJECTSENTITY']._serialized_end=685
  _globals['_SWIFTGETCONTAINERRESPONSEBODY']._serialized_start=687
  _globals['_SWIFTGETCONTAINERRESPONSEBODY']._serialized_end=802
# @@protoc_insertion_point(module_scope)
