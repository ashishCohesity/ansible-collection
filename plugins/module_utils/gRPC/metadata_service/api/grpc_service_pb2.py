# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: metadata_service/api/grpc_service.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from metadata_service.api import api_pb2 as metadata__service_dot_api_dot_api__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'metadata_service/api/grpc_service.proto\x12\x1d\x63ohesity.metadata_service.api\x1a\x1emetadata_service/api/api.proto2\xb7\t\n\x0bGRpcService\x12\x88\x01\n\x13\x43reateOrUpdateGraph\x12\x35.cohesity.metadata_service.api.CreateOrUpdateGraphArg\x1a\x38.cohesity.metadata_service.api.CreateOrUpdateGraphResult\"\x00\x12\x97\x01\n\x18\x43reateTransactionContext\x12:.cohesity.metadata_service.api.CreateTransactionContextArg\x1a=.cohesity.metadata_service.api.CreateTransactionContextResult\"\x00\x12\x82\x01\n\x11\x43ommitTransaction\x12\x33.cohesity.metadata_service.api.CommitTransactionArg\x1a\x36.cohesity.metadata_service.api.CommitTransactionResult\"\x00\x12\x88\x01\n\x13ReserveUniversalIds\x12\x35.cohesity.metadata_service.api.ReserveUniversalIdsArg\x1a\x38.cohesity.metadata_service.api.ReserveUniversalIdsResult\"\x00\x12\x8e\x01\n\x15\x41\x64\x64\x42\x61tchToTransaction\x12\x37.cohesity.metadata_service.api.AddBatchToTransactionArg\x1a:.cohesity.metadata_service.api.AddBatchToTransactionResult\"\x00\x12p\n\x0bLookupNodes\x12-.cohesity.metadata_service.api.LookupNodesArg\x1a\x30.cohesity.metadata_service.api.LookupNodesResult\"\x00\x12\x94\x01\n\x17TraverseNeighborsOfNode\x12\x39.cohesity.metadata_service.api.TraverseNeighborsOfNodeArg\x1a<.cohesity.metadata_service.api.TraverseNeighborsOfNodeResult\"\x00\x12g\n\x08\x46\x65tchDag\x12*.cohesity.metadata_service.api.FetchDagArg\x1a-.cohesity.metadata_service.api.FetchDagResult\"\x00\x12p\n\x0bTraverseDag\x12-.cohesity.metadata_service.api.TraverseDagArg\x1a\x30.cohesity.metadata_service.api.TraverseDagResult\"\x00\x42\"Z\x1d\x63ohesity/metadata_service/api\x80\x01\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'metadata_service.api.grpc_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\035cohesity/metadata_service/api\200\001\000'
  _globals['_GRPCSERVICE']._serialized_start=107
  _globals['_GRPCSERVICE']._serialized_end=1314
# @@protoc_insertion_point(module_scope)
