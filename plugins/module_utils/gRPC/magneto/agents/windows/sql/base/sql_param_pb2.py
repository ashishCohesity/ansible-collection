# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: magneto/agents/windows/sql/base/sql_param.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/magneto/agents/windows/sql/base/sql_param.proto\x12#cohesity.magneto.agents.windows.sql\"5\n\x13SQLColumnAttributes\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x04type\x18\x02 \x01(\x05:\x02-1\"\xdc\x01\n\x07SQLCell\x12?\n\x04type\x18\x01 \x01(\x0e\x32\x31.cohesity.magneto.agents.windows.sql.SQLCell.Type\x12\x16\n\x0eis_null_valued\x18\x02 \x01(\x08\x12\x14\n\x0cstring_value\x18\x03 \x01(\x0c\x12\x15\n\rinteger_value\x18\x04 \x01(\x03\x12\x18\n\x10u16_string_value\x18\x05 \x01(\x0c\"1\n\x04Type\x12\x0b\n\x07kString\x10\x01\x12\x0c\n\x08kInteger\x10\x02\x12\x0e\n\nkTimestamp\x10\x03\"H\n\x06SQLRow\x12>\n\x08\x63\x65ll_vec\x18\x01 \x03(\x0b\x32,.cohesity.magneto.agents.windows.sql.SQLCell\"\xa2\x01\n\tSQLResult\x12W\n\x15\x63olumn_attributes_vec\x18\x01 \x03(\x0b\x32\x38.cohesity.magneto.agents.windows.sql.SQLColumnAttributes\x12<\n\x07row_vec\x18\x02 \x03(\x0b\x32+.cohesity.magneto.agents.windows.sql.SQLRow\":\n\x12\x45xecuteSQLQueryArg\x12\x15\n\rinstance_name\x18\x01 \x01(\x0c\x12\r\n\x05query\x18\x02 \x01(\x0c\"\xb6\x01\n\x13\x45xecuteSQLActionArg\x12G\n\x0b\x61\x63tion_type\x18\x01 \x01(\x0e\x32\x32.cohesity.magneto.agents.windows.sql.SQLActionType\x12V\n\x15\x65xecute_sql_query_arg\x18\x02 \x01(\x0b\x32\x37.cohesity.magneto.agents.windows.sql.ExecuteSQLQueryArg\"[\n\x15\x45xecuteSQLQueryResult\x12\x42\n\nsql_result\x18\x01 \x01(\x0b\x32..cohesity.magneto.agents.windows.sql.SQLResult\"\xbf\x01\n\x16\x45xecuteSQLActionResult\x12G\n\x0b\x61\x63tion_type\x18\x01 \x01(\x0e\x32\x32.cohesity.magneto.agents.windows.sql.SQLActionType\x12\\\n\x18\x65xecute_sql_query_result\x18\x02 \x01(\x0b\x32:.cohesity.magneto.agents.windows.sql.ExecuteSQLQueryResult*%\n\rSQLActionType\x12\x14\n\x10kExecuteSQLQuery\x10\x01\x42)Z\'magneto/agents/windows/sql/base/stub.pb')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'magneto.agents.windows.sql.base.sql_param_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\'magneto/agents/windows/sql/base/stub.pb'
  _globals['_SQLACTIONTYPE']._serialized_start=1137
  _globals['_SQLACTIONTYPE']._serialized_end=1174
  _globals['_SQLCOLUMNATTRIBUTES']._serialized_start=88
  _globals['_SQLCOLUMNATTRIBUTES']._serialized_end=141
  _globals['_SQLCELL']._serialized_start=144
  _globals['_SQLCELL']._serialized_end=364
  _globals['_SQLCELL_TYPE']._serialized_start=315
  _globals['_SQLCELL_TYPE']._serialized_end=364
  _globals['_SQLROW']._serialized_start=366
  _globals['_SQLROW']._serialized_end=438
  _globals['_SQLRESULT']._serialized_start=441
  _globals['_SQLRESULT']._serialized_end=603
  _globals['_EXECUTESQLQUERYARG']._serialized_start=605
  _globals['_EXECUTESQLQUERYARG']._serialized_end=663
  _globals['_EXECUTESQLACTIONARG']._serialized_start=666
  _globals['_EXECUTESQLACTIONARG']._serialized_end=848
  _globals['_EXECUTESQLQUERYRESULT']._serialized_start=850
  _globals['_EXECUTESQLQUERYRESULT']._serialized_end=941
  _globals['_EXECUTESQLACTIONRESULT']._serialized_start=944
  _globals['_EXECUTESQLACTIONRESULT']._serialized_end=1135
# @@protoc_insertion_point(module_scope)
