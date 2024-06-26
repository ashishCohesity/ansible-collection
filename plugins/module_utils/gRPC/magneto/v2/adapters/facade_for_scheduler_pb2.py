# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: magneto/v2/adapters/facade_for_scheduler.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from magneto.api import magneto_external_base_pb2 as magneto_dot_api_dot_magneto__external__base__pb2
from magneto.base import error_pb2 as magneto_dot_base_dot_error__pb2
from util.base import universal_id_pb2 as util_dot_base_dot_universal__id__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.magneto/v2/adapters/facade_for_scheduler.proto\x12\x1e\x63ohesity.magneto.adapter.sched\x1a\'magneto/api/magneto_external_base.proto\x1a\x18magneto/base/error.proto\x1a\x1cutil/base/universal_id.proto\"\x8d\x01\n\x1b\x45numerateObjectsToBackupArg\x12\x30\n\x04\x62\x61se\x18\x01 \x01(\x0b\x32\".cohesity.magneto.api.ArgumentBase\x12<\n\x18protected_source_uid_vec\x18\x02 \x03(\x0b\x32\x1a.cohesity.UniversalIdProto\"\xd1\x02\n\x1e\x45numerateObjectsToBackupResult\x12.\n\x04\x62\x61se\x18\x01 \x01(\x0b\x32 .cohesity.magneto.api.ResultBase\x12Y\n\nresult_vec\x18\x02 \x03(\x0b\x32\x45.cohesity.magneto.adapter.sched.EnumerateObjectsToBackupResult.Result\x1a\xa3\x01\n\x06Result\x12\x38\n\x14protected_source_uid\x18\x01 \x01(\x0b\x32\x1a.cohesity.UniversalIdProto\x12+\n\x05\x65rror\x18\x02 \x01(\x0b\x32\x1c.cohesity.magneto.ErrorProto\x12\x32\n\x0eobject_uid_vec\x18\x03 \x03(\x0b\x32\x1a.cohesity.UniversalIdProto\"\xcd\x02\n\x16\x43onstructBackupPlanArg\x12\x30\n\x04\x62\x61se\x18\x01 \x01(\x0b\x32\".cohesity.magneto.api.ArgumentBase\x12+\n\x07run_uid\x18\x02 \x01(\x0b\x32\x1a.cohesity.UniversalIdProto\x12\x64\n\x14protected_source_vec\x18\x03 \x03(\x0b\x32\x46.cohesity.magneto.adapter.sched.ConstructBackupPlanArg.ProtectedSource\x1an\n\x0fProtectedSource\x12\'\n\x03uid\x18\x01 \x01(\x0b\x32\x1a.cohesity.UniversalIdProto\x12\x32\n\x0eobject_uid_vec\x18\x02 \x03(\x0b\x32\x1a.cohesity.UniversalIdProto\"\xca\x02\n\x12\x42\x61\x63kupTaskDagProto\x12I\n\x08node_vec\x18\x01 \x03(\x0b\x32\x37.cohesity.magneto.adapter.sched.BackupTaskDagProto.Node\x12R\n\rroot_node_vec\x18\x02 \x03(\x0b\x32;.cohesity.magneto.adapter.sched.BackupTaskDagProto.RootNode\x1ap\n\x04Node\x12\x1b\n\x13serialized_task_arg\x18\x01 \x01(\x0c\x12\x32\n\x0eobject_uid_vec\x18\x02 \x03(\x0b\x32\x1a.cohesity.UniversalIdProto\x12\x17\n\x0f\x63hild_index_vec\x18\x03 \x03(\x05\x1a#\n\x08RootNode\x12\x17\n\x0froot_node_index\x18\x01 \x01(\x05\"\x8a\x03\n\x19\x43onstructBackupPlanResult\x12.\n\x04\x62\x61se\x18\x01 \x01(\x0b\x32 .cohesity.magneto.api.ResultBase\x12\x13\n\x0bin_progress\x18\x02 \x01(\x08\x12T\n\nresult_vec\x18\x03 \x03(\x0b\x32@.cohesity.magneto.adapter.sched.ConstructBackupPlanResult.Result\x1a\xd1\x01\n\x06Result\x12+\n\x07run_uid\x18\x01 \x01(\x0b\x32\x1a.cohesity.UniversalIdProto\x12\'\n\x03uid\x18\x02 \x01(\x0b\x32\x1a.cohesity.UniversalIdProto\x12+\n\x05\x65rror\x18\x03 \x01(\x0b\x32\x1c.cohesity.magneto.ErrorProto\x12\x44\n\x08task_dag\x18\x04 \x01(\x0b\x32\x32.cohesity.magneto.adapter.sched.BackupTaskDagProto')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'magneto.v2.adapters.facade_for_scheduler_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_ENUMERATEOBJECTSTOBACKUPARG']._serialized_start=180
  _globals['_ENUMERATEOBJECTSTOBACKUPARG']._serialized_end=321
  _globals['_ENUMERATEOBJECTSTOBACKUPRESULT']._serialized_start=324
  _globals['_ENUMERATEOBJECTSTOBACKUPRESULT']._serialized_end=661
  _globals['_ENUMERATEOBJECTSTOBACKUPRESULT_RESULT']._serialized_start=498
  _globals['_ENUMERATEOBJECTSTOBACKUPRESULT_RESULT']._serialized_end=661
  _globals['_CONSTRUCTBACKUPPLANARG']._serialized_start=664
  _globals['_CONSTRUCTBACKUPPLANARG']._serialized_end=997
  _globals['_CONSTRUCTBACKUPPLANARG_PROTECTEDSOURCE']._serialized_start=887
  _globals['_CONSTRUCTBACKUPPLANARG_PROTECTEDSOURCE']._serialized_end=997
  _globals['_BACKUPTASKDAGPROTO']._serialized_start=1000
  _globals['_BACKUPTASKDAGPROTO']._serialized_end=1330
  _globals['_BACKUPTASKDAGPROTO_NODE']._serialized_start=1181
  _globals['_BACKUPTASKDAGPROTO_NODE']._serialized_end=1293
  _globals['_BACKUPTASKDAGPROTO_ROOTNODE']._serialized_start=1295
  _globals['_BACKUPTASKDAGPROTO_ROOTNODE']._serialized_end=1330
  _globals['_CONSTRUCTBACKUPPLANRESULT']._serialized_start=1333
  _globals['_CONSTRUCTBACKUPPLANRESULT']._serialized_end=1727
  _globals['_CONSTRUCTBACKUPPLANRESULT_RESULT']._serialized_start=1518
  _globals['_CONSTRUCTBACKUPPLANRESULT_RESULT']._serialized_end=1727
# @@protoc_insertion_point(module_scope)
