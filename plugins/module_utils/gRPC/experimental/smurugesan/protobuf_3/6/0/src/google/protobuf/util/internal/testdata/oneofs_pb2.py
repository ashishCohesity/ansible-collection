# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: experimental/smurugesan/protobuf-3.6.0/src/google/protobuf/util/internal/testdata/oneofs.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n^experimental/smurugesan/protobuf-3.6.0/src/google/protobuf/util/internal/testdata/oneofs.proto\x12\x1egoogle.protobuf.testing.oneofs\x1a\x19google/protobuf/any.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xb7\x03\n\rOneOfsRequest\x12\r\n\x05value\x18\x01 \x01(\t\x12\x12\n\x08str_data\x18\x02 \x01(\tH\x00\x12\x12\n\x08int_data\x18\x03 \x01(\x05H\x00\x12<\n\x0cmessage_data\x18\x04 \x01(\x0b\x32$.google.protobuf.testing.oneofs.DataH\x00\x12=\n\tmore_data\x18\x05 \x01(\x0b\x32(.google.protobuf.testing.oneofs.MoreDataH\x00\x12.\n\x0bstruct_data\x18\x06 \x01(\x0b\x32\x17.google.protobuf.StructH\x00\x12,\n\nvalue_data\x18\x07 \x01(\x0b\x32\x16.google.protobuf.ValueH\x00\x12\x35\n\x0flist_value_data\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.ListValueH\x00\x12-\n\x07ts_data\x18\t \x01(\x0b\x32\x1a.google.protobuf.TimestampH\x00\x12&\n\x08\x61ny_data\x18\x13 \x01(\x0b\x32\x14.google.protobuf.AnyB\x06\n\x04\x64\x61ta\"\xd4\x01\n\x16RequestWithSimpleOneof\x12\r\n\x05value\x18\x01 \x01(\t\x12\x12\n\x08str_data\x18\x02 \x01(\tH\x00\x12\x12\n\x08int_data\x18\x03 \x01(\x05H\x00\x12<\n\x0cmessage_data\x18\x04 \x01(\x0b\x32$.google.protobuf.testing.oneofs.DataH\x00\x12=\n\tmore_data\x18\x05 \x01(\x0b\x32(.google.protobuf.testing.oneofs.MoreDataH\x00\x42\x06\n\x04\x64\x61ta\"\x1a\n\x04\x44\x61ta\x12\x12\n\ndata_value\x18\x01 \x01(\x05\"\x1d\n\x08MoreData\x12\x11\n\tstr_value\x18\x01 \x01(\t\"\x19\n\x08Response\x12\r\n\x05value\x18\x01 \x01(\tb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'experimental.smurugesan.protobuf_3.6.0.src.google.protobuf.util.internal.testdata.oneofs_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_ONEOFSREQUEST']._serialized_start=221
  _globals['_ONEOFSREQUEST']._serialized_end=660
  _globals['_REQUESTWITHSIMPLEONEOF']._serialized_start=663
  _globals['_REQUESTWITHSIMPLEONEOF']._serialized_end=875
  _globals['_DATA']._serialized_start=877
  _globals['_DATA']._serialized_end=903
  _globals['_MOREDATA']._serialized_start=905
  _globals['_MOREDATA']._serialized_end=934
  _globals['_RESPONSE']._serialized_start=936
  _globals['_RESPONSE']._serialized_end=961
# @@protoc_insertion_point(module_scope)
