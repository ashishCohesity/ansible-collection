# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: open_util/base/aes_encryptor.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\"open_util/base/aes_encryptor.proto\x12\x08\x63ohesity\"~\n\rEncryptHeader\x12\n\n\x02iv\x18\x01 \x02(\x0c\x12\x1b\n\x13morphed_data_length\x18\x02 \x01(\x07\x12\x0b\n\x03key\x18\x03 \x01(\x0c\x12\x0f\n\x07version\x18\x04 \x01(\x05\x12\x19\n\rencrypted_len\x18\x05 \x01(\x07\x42\x02\x18\x01\x12\x0b\n\x03tag\x18\x06 \x01(\x0c*&\n\x10\x41\x45SEncryptorMode\x12\x08\n\x04kCBC\x10\x00\x12\x08\n\x04kGCM\x10\x01\x42 \n\x1b\x63om.cohesity.open_util.base\x80\x01\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'open_util.base.aes_encryptor_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033com.cohesity.open_util.base\200\001\001'
  _globals['_ENCRYPTHEADER'].fields_by_name['encrypted_len']._loaded_options = None
  _globals['_ENCRYPTHEADER'].fields_by_name['encrypted_len']._serialized_options = b'\030\001'
  _globals['_AESENCRYPTORMODE']._serialized_start=176
  _globals['_AESENCRYPTORMODE']._serialized_end=214
  _globals['_ENCRYPTHEADER']._serialized_start=48
  _globals['_ENCRYPTHEADER']._serialized_end=174
# @@protoc_insertion_point(module_scope)