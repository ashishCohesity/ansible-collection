# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: helios/crms/api/v1/api.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from helios.crms.api.v1 import types_pb2 as helios_dot_crms_dot_api_dot_v1_dot_types__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1chelios/crms/api/v1/api.proto\x12\x07\x63rms.v1\x1a\x1ehelios/crms/api/v1/types.proto\"V\n\x12GetEntitlementsReq\x12\x12\n\naccount_id\x18\x01 \x01(\t\x12,\n\roffering_type\x18\x02 \x01(\x0e\x32\x15.crms.v1.OfferingType\"I\n\x13GetEntitlementsResp\x12\x32\n\x10\x65ntitlement_info\x18\x01 \x03(\x0b\x32\x18.crms.v1.EntitlementInfo\"\xcc\x03\n\x0f\x45ntitlementInfo\x12\n\n\x02id\x18\x01 \x01(\t\x12\x19\n\x11subscription_name\x18\x02 \x01(\t\x12\x10\n\x08quantity\x18\x03 \x01(\x03\x12\x1a\n\x12\x65ntitlement_source\x18\x04 \x01(\t\x12\x15\n\ris_free_trail\x18\x05 \x01(\x08\x12\x12\n\nstart_date\x18\x06 \x01(\t\x12\x10\n\x08\x65nd_date\x18\x07 \x01(\t\x12\x17\n\x0fhelios_end_date\x18\x08 \x01(\t\x12\x0e\n\x06status\x18\t \x01(\t\x12,\n\roffering_type\x18\n \x01(\x0e\x32\x15.crms.v1.OfferingType\x12\x0b\n\x03sku\x18\x0b \x01(\t\x12\x17\n\x0f\x61ws_customer_id\x18\x0c \x01(\t\x12\x16\n\x0e\x61ws_product_id\x18\r \x01(\t\x12\x32\n\x10\x65ntitlement_type\x18\x0e \x01(\x0e\x32\x18.crms.v1.EntitlementType\x12\x18\n\x10retention_period\x18\x0f \x01(\t\x12\x1a\n\x12metering_dimension\x18\x10 \x01(\t\x12\x11\n\tdataplane\x18\x11 \x01(\t\x12\x15\n\rstorage_class\x18\x12 \x01(\t2V\n\x04\x43RMS\x12N\n\x0fGetEntitlements\x12\x1b.crms.v1.GetEntitlementsReq\x1a\x1c.crms.v1.GetEntitlementsResp\"\x00\x42\x1dZ\x1b\x63ohesity/helios/crms/api/v1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'helios.crms.api.v1.api_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\033cohesity/helios/crms/api/v1'
  _globals['_GETENTITLEMENTSREQ']._serialized_start=73
  _globals['_GETENTITLEMENTSREQ']._serialized_end=159
  _globals['_GETENTITLEMENTSRESP']._serialized_start=161
  _globals['_GETENTITLEMENTSRESP']._serialized_end=234
  _globals['_ENTITLEMENTINFO']._serialized_start=237
  _globals['_ENTITLEMENTINFO']._serialized_end=697
  _globals['_CRMS']._serialized_start=699
  _globals['_CRMS']._serialized_end=785
# @@protoc_insertion_point(module_scope)
