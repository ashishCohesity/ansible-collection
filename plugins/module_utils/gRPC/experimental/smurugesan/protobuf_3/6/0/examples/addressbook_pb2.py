# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: experimental/smurugesan/protobuf-3.6.0/examples/addressbook.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nAexperimental/smurugesan/protobuf-3.6.0/examples/addressbook.proto\x12\x08tutorial\x1a\x1fgoogle/protobuf/timestamp.proto\"\x87\x02\n\x06Person\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\x05\x12\r\n\x05\x65mail\x18\x03 \x01(\t\x12,\n\x06phones\x18\x04 \x03(\x0b\x32\x1c.tutorial.Person.PhoneNumber\x12\x30\n\x0clast_updated\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x1aG\n\x0bPhoneNumber\x12\x0e\n\x06number\x18\x01 \x01(\t\x12(\n\x04type\x18\x02 \x01(\x0e\x32\x1a.tutorial.Person.PhoneType\"+\n\tPhoneType\x12\n\n\x06MOBILE\x10\x00\x12\x08\n\x04HOME\x10\x01\x12\x08\n\x04WORK\x10\x02\"/\n\x0b\x41\x64\x64ressBook\x12 \n\x06people\x18\x01 \x03(\x0b\x32\x10.tutorial.PersonBP\n\x14\x63om.example.tutorialB\x11\x41\x64\x64ressBookProtos\xaa\x02$Google.Protobuf.Examples.AddressBookb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'experimental.smurugesan.protobuf_3.6.0.examples.addressbook_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\024com.example.tutorialB\021AddressBookProtos\252\002$Google.Protobuf.Examples.AddressBook'
  _globals['_PERSON']._serialized_start=113
  _globals['_PERSON']._serialized_end=376
  _globals['_PERSON_PHONENUMBER']._serialized_start=260
  _globals['_PERSON_PHONENUMBER']._serialized_end=331
  _globals['_PERSON_PHONETYPE']._serialized_start=333
  _globals['_PERSON_PHONETYPE']._serialized_end=376
  _globals['_ADDRESSBOOK']._serialized_start=378
  _globals['_ADDRESSBOOK']._serialized_end=425
# @@protoc_insertion_point(module_scope)
