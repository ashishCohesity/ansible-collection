# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: magneto/connectors/hyperflex/rest_api.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+magneto/connectors/hyperflex/rest_api.proto\x12\x1a\x63ohesity.magneto.hyperflex\"/\n\tErrorInfo\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x11\n\tmessageId\x18\x02 \x01(\x05\"\x0e\n\x0c\x45mptyRequest\"*\n\x16GetUserContextResponse\x12\x10\n\x08username\x18\x01 \x01(\t\"g\n\x15GetServerInfoResponse\x12\x14\n\x0cinstanceUuid\x18\x01 \x01(\t\x12\x12\n\napiVersion\x18\x02 \x01(\t\x12\x16\n\x0eproductVersion\x18\x03 \x01(\t\x12\x0c\n\x04name\x18\x04 \x01(\t\"q\n\x15\x43reateSnapshotRequest\x12\x14\n\x0csnapshotName\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x15\n\x06memory\x18\x03 \x01(\x08:\x05\x66\x61lse\x12\x16\n\x07quiesce\x18\x04 \x01(\x08:\x05\x66\x61lse\",\n\x16\x43reateSnapshotResponse\x12\x12\n\nsnapshotId\x18\x01 \x01(\t\"p\n\x15\x44\x65leteSnapshotRequest\x12\x1d\n\x0eremoveChildren\x18\x01 \x01(\x08:\x05\x66\x61lse\x12\x1a\n\x0b\x63onsolidate\x18\x02 \x01(\x08:\x05\x66\x61lse\x12\x1c\n\x0eupdateSentinel\x18\x03 \x01(\x08:\x04true\"-\n\x16\x44\x65leteSnapshotResponse\x12\x13\n\x0bsnapshotIds\x18\x01 \x03(\t\"\xee\x01\n\x15GetDatastoresResponse\x12R\n\rdatastore_vec\x18\x01 \x03(\x0b\x32;.cohesity.magneto.hyperflex.GetDatastoresResponse.Datastore\x1a\x1c\n\rVirtDatastore\x12\x0b\n\x03mor\x18\x01 \x01(\t\x1a\x63\n\tDatastore\x12V\n\rvirtDatastore\x18\x01 \x01(\x0b\x32?.cohesity.magneto.hyperflex.GetDatastoresResponse.VirtDatastore')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'magneto.connectors.hyperflex.rest_api_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_ERRORINFO']._serialized_start=75
  _globals['_ERRORINFO']._serialized_end=122
  _globals['_EMPTYREQUEST']._serialized_start=124
  _globals['_EMPTYREQUEST']._serialized_end=138
  _globals['_GETUSERCONTEXTRESPONSE']._serialized_start=140
  _globals['_GETUSERCONTEXTRESPONSE']._serialized_end=182
  _globals['_GETSERVERINFORESPONSE']._serialized_start=184
  _globals['_GETSERVERINFORESPONSE']._serialized_end=287
  _globals['_CREATESNAPSHOTREQUEST']._serialized_start=289
  _globals['_CREATESNAPSHOTREQUEST']._serialized_end=402
  _globals['_CREATESNAPSHOTRESPONSE']._serialized_start=404
  _globals['_CREATESNAPSHOTRESPONSE']._serialized_end=448
  _globals['_DELETESNAPSHOTREQUEST']._serialized_start=450
  _globals['_DELETESNAPSHOTREQUEST']._serialized_end=562
  _globals['_DELETESNAPSHOTRESPONSE']._serialized_start=564
  _globals['_DELETESNAPSHOTRESPONSE']._serialized_end=609
  _globals['_GETDATASTORESRESPONSE']._serialized_start=612
  _globals['_GETDATASTORESRESPONSE']._serialized_end=850
  _globals['_GETDATASTORESRESPONSE_VIRTDATASTORE']._serialized_start=721
  _globals['_GETDATASTORESRESPONSE_VIRTDATASTORE']._serialized_end=749
  _globals['_GETDATASTORESRESPONSE_DATASTORE']._serialized_start=751
  _globals['_GETDATASTORESRESPONSE_DATASTORE']._serialized_end=850
# @@protoc_insertion_point(module_scope)
