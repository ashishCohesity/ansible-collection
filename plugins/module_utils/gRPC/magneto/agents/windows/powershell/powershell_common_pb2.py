# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: magneto/agents/windows/powershell/powershell_common.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n9magneto/agents/windows/powershell/powershell_common.proto\x12*cohesity.magneto.agents.windows.powershell\"C\n\x10PSInvocationInfo\x12\x18\n\x10ScriptLineNumber\x18\x01 \x01(\r\x12\x15\n\rPSCommandPath\x18\x02 \x01(\t\"2\n\x0ePSCategoryInfo\x12\x10\n\x08\x43\x61tegory\x18\x01 \x01(\r\x12\x0e\n\x06Reason\x18\x02 \x01(\t\"\x1e\n\x0bPSException\x12\x0f\n\x07Message\x18\x01 \x01(\t\"\x86\x02\n\x10PSExceptionStack\x12J\n\tException\x18\x01 \x01(\x0b\x32\x37.cohesity.magneto.agents.windows.powershell.PSException\x12P\n\x0c\x43\x61tegoryInfo\x18\x02 \x01(\x0b\x32:.cohesity.magneto.agents.windows.powershell.PSCategoryInfo\x12T\n\x0eInvocationInfo\x18\x03 \x01(\x0b\x32<.cohesity.magneto.agents.windows.powershell.PSInvocationInfo\"3\n\rPSStringTuple\x12\x0f\n\x07key_str\x18\x01 \x02(\t\x12\x11\n\tvalue_str\x18\x02 \x01(\t\"\xf2\x01\n\x1aPSGenericInputDataInternal\x12M\n\nparams_vec\x18\x01 \x03(\x0b\x32\x39.cohesity.magneto.agents.windows.powershell.PSStringTuple\x12\x12\n\nresult_dir\x18\x02 \x02(\t\x12\x11\n\ttask_name\x18\x03 \x01(\t\x12\x12\n\x07task_id\x18\x04 \x01(\x03:\x01\x31\x12\x17\n\x0btimeout_sec\x18\x05 \x01(\x05:\x02-1\x12\x1d\n\x15retry_onfailure_count\x18\x06 \x01(\r\x12\x12\n\nexit_error\x18\x07 \x01(\x05')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'magneto.agents.windows.powershell.powershell_common_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_PSINVOCATIONINFO']._serialized_start=105
  _globals['_PSINVOCATIONINFO']._serialized_end=172
  _globals['_PSCATEGORYINFO']._serialized_start=174
  _globals['_PSCATEGORYINFO']._serialized_end=224
  _globals['_PSEXCEPTION']._serialized_start=226
  _globals['_PSEXCEPTION']._serialized_end=256
  _globals['_PSEXCEPTIONSTACK']._serialized_start=259
  _globals['_PSEXCEPTIONSTACK']._serialized_end=521
  _globals['_PSSTRINGTUPLE']._serialized_start=523
  _globals['_PSSTRINGTUPLE']._serialized_end=574
  _globals['_PSGENERICINPUTDATAINTERNAL']._serialized_start=577
  _globals['_PSGENERICINPUTDATAINTERNAL']._serialized_end=819
# @@protoc_insertion_point(module_scope)
