# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bridge/ticket_service/domain_assignment.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-bridge/ticket_service/domain_assignment.proto\x12\x16\x63ohesity.bridge.ticket\"\xcf\x01\n\x15\x44omainAssignmentProto\x12*\n\x0bgandalf_key\x18\x01 \x01(\t:\x15ts_domain_assignments\x12P\n\x0e\x61ssignment_vec\x18\x02 \x03(\x0b\x32\x38.cohesity.bridge.ticket.DomainAssignmentProto.Assignment\x1a\x38\n\nAssignment\x12\x16\n\x0e\x63onstituent_id\x18\x01 \x02(\x03\x12\x12\n\ndomain_vec\x18\x02 \x03(\x03')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'bridge.ticket_service.domain_assignment_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_DOMAINASSIGNMENTPROTO']._serialized_start=74
  _globals['_DOMAINASSIGNMENTPROTO']._serialized_end=281
  _globals['_DOMAINASSIGNMENTPROTO_ASSIGNMENT']._serialized_start=225
  _globals['_DOMAINASSIGNMENTPROTO_ASSIGNMENT']._serialized_end=281
# @@protoc_insertion_point(module_scope)
