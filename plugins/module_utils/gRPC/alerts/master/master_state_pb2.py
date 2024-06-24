# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: alerts/master/master_state.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from alerts.base import alert_pb2 as alerts_dot_base_dot_alert__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n alerts/master/master_state.proto\x12\x16\x63ohesity.alerts.master\x1a\x17\x61lerts/base/alert.proto\"\x81\x04\n\x0f\x41lertIndexProto\x12\x45\n\nindex_type\x18\x01 \x02(\x0e\x32\x31.cohesity.alerts.master.AlertIndexProto.IndexType\x12\x11\n\tindex_key\x18\x02 \x02(\t\x12\x34\n\ralert_id_list\x18\x03 \x03(\x0b\x32\x1d.cohesity.alerts.AlertIdProto\x12G\n\x0bupdate_type\x18\x04 \x01(\x0e\x32\x32.cohesity.alerts.master.AlertIndexProto.UpdateType\x12\x15\n\x06intent\x18\x05 \x01(\x08:\x05\x66\x61lse\"\xd8\x01\n\tIndexType\x12\x0e\n\nkAlertType\x10\x00\x12\x12\n\x0ekAlertCategory\x10\x01\x12\r\n\tkSeverity\x10\x02\x12\x0f\n\x0bkAlertState\x10\x03\x12\x0f\n\x0bkResolution\x10\x04\x12\r\n\tkProperty\x10\x05\x12\x08\n\x04kAll\x10\x06\x12\x0b\n\x07kIntent\x10\x07\x12\x0b\n\x07kHidden\x10\x08\x12\x0c\n\x08kSupport\x10\t\x12\r\n\tkTenantId\x10\n\x12\x13\n\x0fkLastOccurrence\x10\x0b\x12\x11\n\rkResolvedTime\x10\x0c\"#\n\nUpdateType\x12\x08\n\x04kAdd\x10\x00\x12\x0b\n\x07kRemove\x10\x01\"\xa1\x02\n\x14ResolutionIndexProto\x12V\n\x0fresolution_list\x18\x01 \x03(\x0b\x32=.cohesity.alerts.master.ResolutionIndexProto.ResolutionIdPair\x12G\n\x0bupdate_type\x18\x02 \x01(\x0e\x32\x32.cohesity.alerts.master.AlertIndexProto.UpdateType\x12\x15\n\x06intent\x18\x03 \x01(\x08:\x05\x66\x61lse\x1aQ\n\x10ResolutionIdPair\x12\x15\n\rresolution_id\x18\x01 \x02(\x03\x12&\n\x1eresolution_creation_time_usecs\x18\x02 \x02(\x03\"\x82\x03\n\x1a\x41lertByTimeStampIndexProto\x12\x45\n\nindex_type\x18\x01 \x02(\x0e\x32\x31.cohesity.alerts.master.AlertIndexProto.IndexType\x12\x61\n\x10ts_alert_id_list\x18\x02 \x03(\x0b\x32G.cohesity.alerts.master.AlertByTimeStampIndexProto.AlertByTimeStampPair\x12G\n\x0bupdate_type\x18\x03 \x01(\x0e\x32\x32.cohesity.alerts.master.AlertIndexProto.UpdateType\x12\x15\n\x06intent\x18\x04 \x01(\x08:\x05\x66\x61lse\x1aZ\n\x14\x41lertByTimeStampPair\x12\x11\n\ttimestamp\x18\x01 \x02(\x03\x12/\n\x08\x61lert_id\x18\x02 \x02(\x0b\x32\x1d.cohesity.alerts.AlertIdProto\"\xf9\x01\n\x18\x41lertCategoryUpdateProto\x12\x12\n\nalert_type\x18\x01 \x02(\x05\x12G\n\x0csrc_category\x18\x02 \x02(\x0e\x32\x31.cohesity.alerts.AlertMetadataProto.AlertCategory\x12J\n\x0ftarget_category\x18\x03 \x02(\x0e\x32\x31.cohesity.alerts.AlertMetadataProto.AlertCategory\x12\x18\n\x10\x65xpected_version\x18\x04 \x02(\x05\x12\x1a\n\x0bupdate_done\x18\x05 \x01(\x08:\x05\x66\x61lse\"\x8e\x03\n\x0eWALRecordProto\x12\x41\n\x10\x61lert_index_list\x18\x01 \x03(\x0b\x32\'.cohesity.alerts.master.AlertIndexProto\x12K\n\x15resolution_index_list\x18\x02 \x03(\x0b\x32,.cohesity.alerts.master.ResolutionIndexProto\x12T\n\x1a\x61lert_category_update_list\x18\x03 \x03(\x0b\x32\x30.cohesity.alerts.master.AlertCategoryUpdateProto\x12\x45\n\x14\x61lert_last_time_list\x18\x04 \x03(\x0b\x32\'.cohesity.alerts.master.AlertIndexProto\x12O\n\x13\x61lert_ts_index_list\x18\x05 \x03(\x0b\x32\x32.cohesity.alerts.master.AlertByTimeStampIndexProto')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'alerts.master.master_state_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_ALERTINDEXPROTO']._serialized_start=86
  _globals['_ALERTINDEXPROTO']._serialized_end=599
  _globals['_ALERTINDEXPROTO_INDEXTYPE']._serialized_start=346
  _globals['_ALERTINDEXPROTO_INDEXTYPE']._serialized_end=562
  _globals['_ALERTINDEXPROTO_UPDATETYPE']._serialized_start=564
  _globals['_ALERTINDEXPROTO_UPDATETYPE']._serialized_end=599
  _globals['_RESOLUTIONINDEXPROTO']._serialized_start=602
  _globals['_RESOLUTIONINDEXPROTO']._serialized_end=891
  _globals['_RESOLUTIONINDEXPROTO_RESOLUTIONIDPAIR']._serialized_start=810
  _globals['_RESOLUTIONINDEXPROTO_RESOLUTIONIDPAIR']._serialized_end=891
  _globals['_ALERTBYTIMESTAMPINDEXPROTO']._serialized_start=894
  _globals['_ALERTBYTIMESTAMPINDEXPROTO']._serialized_end=1280
  _globals['_ALERTBYTIMESTAMPINDEXPROTO_ALERTBYTIMESTAMPPAIR']._serialized_start=1190
  _globals['_ALERTBYTIMESTAMPINDEXPROTO_ALERTBYTIMESTAMPPAIR']._serialized_end=1280
  _globals['_ALERTCATEGORYUPDATEPROTO']._serialized_start=1283
  _globals['_ALERTCATEGORYUPDATEPROTO']._serialized_end=1532
  _globals['_WALRECORDPROTO']._serialized_start=1535
  _globals['_WALRECORDPROTO']._serialized_end=1933
# @@protoc_insertion_point(module_scope)
