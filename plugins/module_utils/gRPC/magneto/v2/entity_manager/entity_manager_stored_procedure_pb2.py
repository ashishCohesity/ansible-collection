# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: magneto/v2/entity_manager/entity_manager_stored_procedure.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from metadata_service.api import api_pb2 as metadata__service_dot_api_dot_api__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n?magneto/v2/entity_manager/entity_manager_stored_procedure.proto\x12/cohesity.magneto.entity.entity_manager_mds_proc\x1a\x1emetadata_service/api/api.proto\"\x98\x03\n\x18\x45ntityAccessProcArgProto\x12%\n\x1dregistered_source_primary_key\x18\x01 \x01(\t\x12s\n\x12permission_arg_vec\x18\x02 \x03(\x0b\x32W.cohesity.magneto.entity.entity_manager_mds_proc.EntityAccessProcArgProto.PermissionArg\x1a:\n\rPermissionArg\x12\x11\n\ttenant_id\x18\x01 \x01(\t\x12\x16\n\x0eserialized_SID\x18\x02 \x01(\t2\xa3\x01\n\x16\x65ntity_access_proc_arg\x12\x38.cohesity.metadata_service.api.ExecuteStoredProcedureArg\x18\x64 \x01(\x0b\x32I.cohesity.magneto.entity.entity_manager_mds_proc.EntityAccessProcArgProtoB1Z/cohesity/magneto/entity/entity_manager_mds_proc')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'magneto.v2.entity_manager.entity_manager_stored_procedure_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z/cohesity/magneto/entity/entity_manager_mds_proc'
  _globals['_ENTITYACCESSPROCARGPROTO']._serialized_start=149
  _globals['_ENTITYACCESSPROCARGPROTO']._serialized_end=557
  _globals['_ENTITYACCESSPROCARGPROTO_PERMISSIONARG']._serialized_start=333
  _globals['_ENTITYACCESSPROCARGPROTO_PERMISSIONARG']._serialized_end=391
# @@protoc_insertion_point(module_scope)
