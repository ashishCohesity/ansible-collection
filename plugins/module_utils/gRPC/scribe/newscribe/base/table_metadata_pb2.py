# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: scribe/newscribe/base/table_metadata.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*scribe/newscribe/base/table_metadata.proto\x12\x0f\x63ohesity.scribe\"\x98\x0c\n\x12TableMetadataProto\x12\x39\n\x06tables\x18\x01 \x03(\x0b\x32).cohesity.scribe.TableMetadataProto.Table\x12;\n\x07tablets\x18\x02 \x03(\x0b\x32*.cohesity.scribe.TableMetadataProto.Tablet\x12\x12\n\x07next_id\x18\x03 \x02(\x05:\x01\x31\x12\x34\n(migration_trigger_table_metadata_version\x18\x05 \x01(\x03:\x02-1\x12[\n4scribe_tables_to_be_created_in_high_mem_usage_tablet\x18\x06 \x01(\t:\x1d\x63hunk_metadata,view_snap_tree\x12\x30\n!scribe_low_mem_usage_tablet_ready\x18\x07 \x01(\x08:\x05\x66\x61lse\x12.\n\"last_table_migration_completion_ts\x18\x08 \x01(\x03:\x02-1\x12*\n\x1bscribe_history_tablet_ready\x18\t \x01(\x08:\x05\x66\x61lse\x1a\xd8\x07\n\x05Table\x12\x10\n\x08table_id\x18\x01 \x02(\x05\x12\x12\n\ntable_name\x18\x02 \x02(\x0c\x12\x11\n\ttablet_id\x18\x03 \x01(\x05\x12\x1c\n\x10target_tablet_id\x18\x06 \x01(\x05:\x02-1\x12V\n\x15\x63ustom_hashing_scheme\x18\x07 \x01(\x0e\x32\x37.cohesity.scribe.TableMetadataProto.Table.HashingScheme\x12\x1c\n\rhistory_table\x18\x08 \x01(\x08:\x05\x66\x61lse\x12\x14\n\x0c\x62lock_reason\x18\t \x01(\t\x1a\xf6\x03\n\x18TableNameToHashingScheme\x12{\n\x15stats_timeseries_data\x18\x01 \x01(\x0e\x32\x37.cohesity.scribe.TableMetadataProto.Table.HashingScheme:#kStatsTimeseriesPrefixHashingScheme\x12s\n\x11stats_entity_meta\x18\x02 \x01(\x0e\x32\x37.cohesity.scribe.TableMetadataProto.Table.HashingScheme:\x1fkStatsEntityPrefixHashingScheme\x12u\n\x13stats_entity_schema\x18\x03 \x01(\x0e\x32\x37.cohesity.scribe.TableMetadataProto.Table.HashingScheme:\x1fkStatsSchemaPrefixHashingScheme\x12q\n\x11\x62ulk_write_test_0\x18\x04 \x01(\x0e\x32\x37.cohesity.scribe.TableMetadataProto.Table.HashingScheme:\x1dkTestTablePrefixHashingScheme\"\xe6\x01\n\rHashingScheme\x12\x19\n\x15kDefaultHashingScheme\x10\x00\x12\'\n#kStatsTimeseriesPrefixHashingScheme\x10\x01\x12#\n\x1fkStatsEntityPrefixHashingScheme\x10\x02\x12#\n\x1fkStatsSchemaPrefixHashingScheme\x10\x03\x12!\n\x1dkTestTablePrefixHashingScheme\x10\x04\x12$\n kHistoryTablePrefixHashingScheme\x10\x05J\x04\x08\x04\x10\x05J\x04\x08\x05\x10\x06\x1at\n\x06Tablet\x12\n\n\x02id\x18\x01 \x02(\x05\x12\x16\n\x0e\x65ncryption_key\x18\x02 \x01(\x0c\x12$\n\x15low_mem_usage_setting\x18\x03 \x01(\x08:\x05\x66\x61lse\x12 \n\x11store_row_history\x18\x04 \x01(\x08:\x05\x66\x61lseJ\x04\x08\x04\x10\x05')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'scribe.newscribe.base.table_metadata_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_TABLEMETADATAPROTO']._serialized_start=64
  _globals['_TABLEMETADATAPROTO']._serialized_end=1624
  _globals['_TABLEMETADATAPROTO_TABLE']._serialized_start=516
  _globals['_TABLEMETADATAPROTO_TABLE']._serialized_end=1500
  _globals['_TABLEMETADATAPROTO_TABLE_TABLENAMETOHASHINGSCHEME']._serialized_start=753
  _globals['_TABLEMETADATAPROTO_TABLE_TABLENAMETOHASHINGSCHEME']._serialized_end=1255
  _globals['_TABLEMETADATAPROTO_TABLE_HASHINGSCHEME']._serialized_start=1258
  _globals['_TABLEMETADATAPROTO_TABLE_HASHINGSCHEME']._serialized_end=1488
  _globals['_TABLEMETADATAPROTO_TABLET']._serialized_start=1502
  _globals['_TABLEMETADATAPROTO_TABLET']._serialized_end=1618
# @@protoc_insertion_point(module_scope)
