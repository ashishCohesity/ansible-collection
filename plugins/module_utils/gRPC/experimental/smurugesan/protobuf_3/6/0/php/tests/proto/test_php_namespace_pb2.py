# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: experimental/smurugesan/protobuf-3.6.0/php/tests/proto/test_php_namespace.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nOexperimental/smurugesan/protobuf-3.6.0/php/tests/proto/test_php_namespace.proto\x12\x03\x66oo\"\xa5\x03\n\rTestNamespace\x12\t\n\x01\x61\x18\x01 \x01(\x05\x12\x38\n\x0enested_message\x18\x02 \x01(\x0b\x32 .foo.TestNamespace.NestedMessage\x12\x32\n\x0bnested_enum\x18\x03 \x01(\x0e\x32\x1d.foo.TestNamespace.NestedEnum\x12/\n\rreserved_name\x18\x04 \x01(\x0b\x32\x18.foo.TestNamespace.Empty\x1a\x1a\n\rNestedMessage\x12\t\n\x01\x61\x18\x01 \x01(\x05\x1a\xb5\x01\n\x05\x45mpty\x12>\n\x0enested_message\x18\x01 \x01(\x0b\x32&.foo.TestNamespace.Empty.NestedMessage\x12\x38\n\x0bnested_enum\x18\x02 \x01(\x0e\x32#.foo.TestNamespace.Empty.NestedEnum\x1a\x1a\n\rNestedMessage\x12\t\n\x01\x61\x18\x01 \x01(\x05\"\x16\n\nNestedEnum\x12\x08\n\x04ZERO\x10\x00\"\x16\n\nNestedEnum\x12\x08\n\x04ZERO\x10\x00\x42\x1f\xca\x02\x08Php\\Test\xe2\x02\x11Metadata\\Php\\Testb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'experimental.smurugesan.protobuf_3.6.0.php.tests.proto.test_php_namespace_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\312\002\010Php\\Test\342\002\021Metadata\\Php\\Test'
  _globals['_TESTNAMESPACE']._serialized_start=89
  _globals['_TESTNAMESPACE']._serialized_end=510
  _globals['_TESTNAMESPACE_NESTEDMESSAGE']._serialized_start=276
  _globals['_TESTNAMESPACE_NESTEDMESSAGE']._serialized_end=302
  _globals['_TESTNAMESPACE_EMPTY']._serialized_start=305
  _globals['_TESTNAMESPACE_EMPTY']._serialized_end=486
  _globals['_TESTNAMESPACE_EMPTY_NESTEDMESSAGE']._serialized_start=276
  _globals['_TESTNAMESPACE_EMPTY_NESTEDMESSAGE']._serialized_end=302
  _globals['_TESTNAMESPACE_EMPTY_NESTEDENUM']._serialized_start=464
  _globals['_TESTNAMESPACE_EMPTY_NESTEDENUM']._serialized_end=486
  _globals['_TESTNAMESPACE_NESTEDENUM']._serialized_start=464
  _globals['_TESTNAMESPACE_NESTEDENUM']._serialized_end=486
# @@protoc_insertion_point(module_scope)
