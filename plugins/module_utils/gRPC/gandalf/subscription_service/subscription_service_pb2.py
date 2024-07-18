# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gandalf/subscription_service/subscription_service.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gandalf.base import error_pb2 as gandalf_dot_base_dot_error__pb2
from gandalf.server.stub import gandalf_pb2 as gandalf_dot_server_dot_stub_dot_gandalf__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n7gandalf/subscription_service/subscription_service.proto\x12%cohesity.gandalf.subscription_service\x1a\x18gandalf/base/error.proto\x1a!gandalf/server/stub/gandalf.proto\",\n\x0cWatchKeysArg\x12\x1c\n\x14\x61ll_keys_watched_vec\x18\x01 \x03(\t\"\xad\x01\n\x0fWatchKeysUpdate\x12_\n\x12key_value_info_vec\x18\x01 \x03(\x0b\x32\x43.cohesity.gandalf.subscription_service.WatchKeysUpdate.KeyValueInfo\x1a\x39\n\x0cKeyValueInfo\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x0b\n\x03val\x18\x02 \x01(\x0c\x12\x0f\n\x07version\x18\x03 \x01(\x03\"N\n\x13LookupKeyArgWrapper\x12\x37\n\x03\x61rg\x18\x01 \x01(\x0b\x32*.cohesity.gandalf.server.stub.LookupKeyArg\"\x8e\x01\n\x16LookupKeyResultWrapper\x12\x35\n\nerror_type\x18\x01 \x01(\x0e\x32!.cohesity.gandalf.ErrorProto.Type\x12=\n\x06result\x18\x02 \x01(\x0b\x32-.cohesity.gandalf.server.stub.LookupKeyResult\"m\n\x13UpdateKeyArgWrapper\x12\x37\n\x03\x61rg\x18\x01 \x01(\x0b\x32*.cohesity.gandalf.server.stub.UpdateKeyArg\x12\x1d\n\x15is_value_cas_fallback\x18\x02 \x01(\x08\"\x8e\x01\n\x16UpdateKeyResultWrapper\x12\x35\n\nerror_type\x18\x01 \x01(\x0e\x32!.cohesity.gandalf.ErrorProto.Type\x12=\n\x06result\x18\x02 \x01(\x0b\x32-.cohesity.gandalf.server.stub.UpdateKeyResult\"N\n\x13\x44\x65leteKeyArgWrapper\x12\x37\n\x03\x61rg\x18\x01 \x01(\x0b\x32*.cohesity.gandalf.server.stub.DeleteKeyArg\"\x8e\x01\n\x16\x44\x65leteKeyResultWrapper\x12\x35\n\nerror_type\x18\x01 \x01(\x0e\x32!.cohesity.gandalf.ErrorProto.Type\x12=\n\x06result\x18\x02 \x01(\x0b\x32-.cohesity.gandalf.server.stub.DeleteKeyResult\"Z\n\x19\x41tomicIncrementArgWrapper\x12=\n\x03\x61rg\x18\x01 \x01(\x0b\x32\x30.cohesity.gandalf.server.stub.AtomicIncrementArg\"c\n\x1c\x41tomicIncrementResultWrapper\x12\x43\n\x06result\x18\x02 \x01(\x0b\x32\x33.cohesity.gandalf.server.stub.AtomicIncrementResult\"\xff\x08\n\tSsMessage\x12\x43\n\x04type\x18\x01 \x01(\x0e\x32\x35.cohesity.gandalf.subscription_service.SsMessage.Type\x12\x12\n\nrequest_id\x18\x02 \x01(\x03\x12K\n\x0ewatch_keys_arg\x18\x03 \x01(\x0b\x32\x33.cohesity.gandalf.subscription_service.WatchKeysArg\x12Q\n\x11watch_keys_update\x18\x04 \x01(\x0b\x32\x36.cohesity.gandalf.subscription_service.WatchKeysUpdate\x12Z\n\x16wrapper_lookup_key_arg\x18\x05 \x01(\x0b\x32:.cohesity.gandalf.subscription_service.LookupKeyArgWrapper\x12`\n\x19wrapper_lookup_key_result\x18\x06 \x01(\x0b\x32=.cohesity.gandalf.subscription_service.LookupKeyResultWrapper\x12Z\n\x16wrapper_update_key_arg\x18\x07 \x01(\x0b\x32:.cohesity.gandalf.subscription_service.UpdateKeyArgWrapper\x12`\n\x19wrapper_update_key_result\x18\x08 \x01(\x0b\x32=.cohesity.gandalf.subscription_service.UpdateKeyResultWrapper\x12Z\n\x16wrapper_delete_key_arg\x18\t \x01(\x0b\x32:.cohesity.gandalf.subscription_service.DeleteKeyArgWrapper\x12`\n\x19wrapper_delete_key_result\x18\n \x01(\x0b\x32=.cohesity.gandalf.subscription_service.DeleteKeyResultWrapper\x12\x66\n\x1cwrapper_atomic_increment_arg\x18\x0b \x01(\x0b\x32@.cohesity.gandalf.subscription_service.AtomicIncrementArgWrapper\x12l\n\x1fwrapper_atomic_increment_result\x18\x0c \x01(\x0b\x32\x43.cohesity.gandalf.subscription_service.AtomicIncrementResultWrapper\"i\n\x04Type\x12\x0c\n\x08kUnknown\x10\x00\x12\r\n\tkWatchKey\x10\x01\x12\x0e\n\nkLookupKey\x10\x02\x12\x0e\n\nkUpdateKey\x10\x03\x12\x0e\n\nkDeleteKey\x10\x04\x12\x14\n\x10kAtomicIncrement\x10\x05\"A\n\tConstants\x1a\x34\n\x10GrpcMetadataKeys\x12 \n\rtenant_id_key\x18\x01 \x01(\t:\ttenant_id2\x8b\x01\n\x13SubscriptionService\x12t\n\x08SsStream\x12\x30.cohesity.gandalf.subscription_service.SsMessage\x1a\x30.cohesity.gandalf.subscription_service.SsMessage\"\x00(\x01\x30\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'gandalf.subscription_service.subscription_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_WATCHKEYSARG']._serialized_start=159
  _globals['_WATCHKEYSARG']._serialized_end=203
  _globals['_WATCHKEYSUPDATE']._serialized_start=206
  _globals['_WATCHKEYSUPDATE']._serialized_end=379
  _globals['_WATCHKEYSUPDATE_KEYVALUEINFO']._serialized_start=322
  _globals['_WATCHKEYSUPDATE_KEYVALUEINFO']._serialized_end=379
  _globals['_LOOKUPKEYARGWRAPPER']._serialized_start=381
  _globals['_LOOKUPKEYARGWRAPPER']._serialized_end=459
  _globals['_LOOKUPKEYRESULTWRAPPER']._serialized_start=462
  _globals['_LOOKUPKEYRESULTWRAPPER']._serialized_end=604
  _globals['_UPDATEKEYARGWRAPPER']._serialized_start=606
  _globals['_UPDATEKEYARGWRAPPER']._serialized_end=715
  _globals['_UPDATEKEYRESULTWRAPPER']._serialized_start=718
  _globals['_UPDATEKEYRESULTWRAPPER']._serialized_end=860
  _globals['_DELETEKEYARGWRAPPER']._serialized_start=862
  _globals['_DELETEKEYARGWRAPPER']._serialized_end=940
  _globals['_DELETEKEYRESULTWRAPPER']._serialized_start=943
  _globals['_DELETEKEYRESULTWRAPPER']._serialized_end=1085
  _globals['_ATOMICINCREMENTARGWRAPPER']._serialized_start=1087
  _globals['_ATOMICINCREMENTARGWRAPPER']._serialized_end=1177
  _globals['_ATOMICINCREMENTRESULTWRAPPER']._serialized_start=1179
  _globals['_ATOMICINCREMENTRESULTWRAPPER']._serialized_end=1278
  _globals['_SSMESSAGE']._serialized_start=1281
  _globals['_SSMESSAGE']._serialized_end=2432
  _globals['_SSMESSAGE_TYPE']._serialized_start=2327
  _globals['_SSMESSAGE_TYPE']._serialized_end=2432
  _globals['_CONSTANTS']._serialized_start=2434
  _globals['_CONSTANTS']._serialized_end=2499
  _globals['_CONSTANTS_GRPCMETADATAKEYS']._serialized_start=2447
  _globals['_CONSTANTS_GRPCMETADATAKEYS']._serialized_end=2499
  _globals['_SUBSCRIPTIONSERVICE']._serialized_start=2502
  _globals['_SUBSCRIPTIONSERVICE']._serialized_end=2641
# @@protoc_insertion_point(module_scope)