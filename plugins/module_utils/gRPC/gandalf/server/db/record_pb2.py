# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gandalf/server/db/record.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gandalf.base import common_pb2 as gandalf_dot_base_dot_common__pb2
from gandalf.server.stub import gandalf_pb2 as gandalf_dot_server_dot_stub_dot_gandalf__pb2
from util.base import op_clock_pb2 as util_dot_base_dot_op__clock__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1egandalf/server/db/record.proto\x12\x17\x63ohesity.gandalf.server\x1a\x19gandalf/base/common.proto\x1a!gandalf/server/stub/gandalf.proto\x1a\x18util/base/op_clock.proto\"\x8a\x06\n\x07\x44\x62Value\x12>\n\x0esession_record\x18\x01 \x01(\x0b\x32&.cohesity.gandalf.server.SessionRecord\x12\x38\n\x0block_record\x18\x02 \x01(\x0b\x32#.cohesity.gandalf.server.LockRecord\x12\x36\n\nkey_record\x18\x03 \x01(\x0b\x32\".cohesity.gandalf.server.KeyRecord\x12\x43\n\x11name_space_record\x18\x04 \x01(\x0b\x32(.cohesity.gandalf.server.NamespaceRecord\x12?\n\x0fop_clock_record\x18\x05 \x01(\x0b\x32&.cohesity.gandalf.server.OpClockRecord\x12U\n\x1a\x61\x63tive_notification_record\x18\t \x01(\x0b\x32\x31.cohesity.gandalf.server.ActiveNotificationRecord\x12\x1c\n\x14session_id_generator\x18\x06 \x01(\x03\x12 \n\x18incarnation_id_generator\x18\x07 \x01(\x03\x12#\n\x1bnewlock_sequencer_generator\x18\x08 \x01(\x03\x12/\n\'active_notification_record_id_generator\x18\n \x01(\x03\x12\x45\n\x12\x64\x61ta_format_record\x18\x0b \x01(\x0b\x32).cohesity.gandalf.server.DataFormatRecord\x12I\n\x18\x63onstituent_stats_record\x18\x0c \x01(\x0b\x32\'.cohesity.gandalf.ConstituentStatsProto\x12H\n\x1cop_clock_bucket_cache_record\x18\r \x01(\x0b\x32\".cohesity.OpClockVectorCacheBucket\"\xb2\x07\n\rSessionRecord\x12\x12\n\nsession_id\x18\x01 \x02(\x03\x12\x1c\n\x14\x65xpiration_time_msec\x18\x02 \x02(\x03\x12\"\n\x17highest_notification_id\x18\x03 \x02(\x03:\x01\x30\x12\x31\n&highest_notification_id_sent_to_client\x18\x0b \x01(\x03:\x01\x30\x12\x65\n\'legacy_unacked_notifications_DEPRECATED\x18\x04 \x03(\x0b\x32\x30.cohesity.gandalf.server.stub.ClientNotificationB\x02\x18\x01\x12\x62\n\x1funacked_queued_notification_vec\x18\n \x03(\x0b\x32\x39.cohesity.gandalf.server.SessionRecord.QueuedNotification\x12K\n\tresources\x18\x05 \x03(\x0b\x32\x38.cohesity.gandalf.server.SessionRecord.RegisteredRequest\x12\x13\n\x0b\x63lient_name\x18\x06 \x01(\t\x12\x19\n\x11\x63lient_ip_address\x18\x07 \x01(\t\x12\x1b\n\x13\x63lient_healthz_port\x18\x08 \x01(\x05\x12\x1b\n\x13\x63reation_time_msecs\x18\t \x01(\x03\x12$\n\x1c\x63lient_session_timeout_msecs\x18\x0c \x01(\x03\x12\x11\n\ttenant_id\x18\r \x01(\t\x1ai\n\x12QueuedNotification\x12%\n\x1d\x61\x63tive_notification_record_id\x18\x01 \x02(\x03\x12\x18\n\x10session_local_id\x18\x02 \x02(\x03\x12\x12\n\nrequest_id\x18\x03 \x02(\x03\x1a\xf1\x01\n\x11RegisteredRequest\x12K\n\x04type\x18\x01 \x02(\x0e\x32=.cohesity.gandalf.server.SessionRecord.RegisteredRequest.Type\x12\x13\n\x0b\x65ntity_name\x18\x02 \x02(\t\x12\x12\n\nrequest_id\x18\x03 \x02(\x03\"f\n\x04Type\x12\r\n\tkKeyWatch\x10\x00\x12\x0e\n\nkLockWatch\x10\x01\x12\x10\n\x0ckLockRequest\x10\x02\x12\x12\n\x0ekLivenessWatch\x10\x03\x12\x19\n\x15kLivenessRegistration\x10\x04\"\xb6\x04\n\nLockRecord\x12\x11\n\tlock_name\x18\x01 \x02(\t\x12\x15\n\tsequencer\x18\x02 \x02(\x03:\x02-1\x12\x45\n\nrequesters\x18\x08 \x03(\x0b\x32\x31.cohesity.gandalf.server.LockRecord.LockRequester\x12=\n\x08watchers\x18\x07 \x03(\x0b\x32+.cohesity.gandalf.server.LockRecord.Watcher\x12\x12\n\npersistent\x18\t \x01(\x08\x1a\xb0\x02\n\rLockRequester\x12\x12\n\nsession_id\x18\x01 \x02(\x03\x12\x12\n\nrequest_id\x18\x02 \x02(\x03\x12\x16\n\x0e\x63onstituent_id\x18\x03 \x02(\x03\x12\x14\n\x0cis_exclusive\x18\x04 \x02(\x08\x12\x10\n\x08is_force\x18\x05 \x02(\x08\x12\x0c\n\x04\x64\x61ta\x18\x06 \x01(\x0c\x12\x0f\n\x07is_held\x18\x07 \x02(\x08\x12\x12\n\npersistent\x18\x08 \x01(\x08\x12\x0f\n\x07node_id\x18\t \x01(\x03\x12\x11\n\tcan_crash\x18\n \x01(\x08\x12\x42\n\rpriority_type\x18\x0b \x01(\x0e\x32+.cohesity.gandalf.LockPriority.PriorityType\x12\x1c\n\x14\x61void_holder_of_lock\x18\x0c \x01(\t\x1a\x31\n\x07Watcher\x12\x12\n\nsession_id\x18\x01 \x02(\x03\x12\x12\n\nrequest_id\x18\x02 \x02(\x03\"\xb3\x01\n\tKeyRecord\x12\x0b\n\x03key\x18\x01 \x02(\t\x12\x13\n\x07version\x18\x02 \x02(\x03:\x02-1\x12\r\n\x05value\x18\x03 \x01(\x0c\x12?\n\x08watchers\x18\x06 \x03(\x0b\x32-.cohesity.gandalf.server.KeyRecord.KeyWatcher\x1a\x34\n\nKeyWatcher\x12\x12\n\nsession_id\x18\x01 \x02(\x03\x12\x12\n\nrequest_id\x18\x02 \x02(\x03\"\xd2\x03\n\x0fNamespaceRecord\x12\x12\n\nname_space\x18\x01 \x02(\t\x12U\n\x17registered_constituents\x18\x02 \x03(\x0b\x32\x34.cohesity.gandalf.server.NamespaceRecord.Constituent\x12K\n\x08watchers\x18\x03 \x03(\x0b\x32\x39.cohesity.gandalf.server.NamespaceRecord.NamespaceWatcher\x12-\n%num_recently_seen_unique_constituents\x18\x04 \x01(\x03\x1a\x9b\x01\n\x0b\x43onstituent\x12\x16\n\x0e\x63onstituent_id\x18\x01 \x02(\x03\x12\x12\n\nsession_id\x18\x02 \x02(\x03\x12\x0c\n\x04\x64\x61ta\x18\x03 \x01(\x0c\x12)\n\x1dprior_registration_session_id\x18\x04 \x01(\x03:\x02-1\x12\'\n\x19persist_constituent_stats\x18\x05 \x01(\x08:\x04true\x1a:\n\x10NamespaceWatcher\x12\x12\n\nsession_id\x18\x01 \x02(\x03\x12\x12\n\nrequest_id\x18\x02 \x02(\x03\"5\n\rOpClockRecord\x12$\n\top_clocks\x18\x01 \x03(\x0b\x32\x11.cohesity.OpClock\"\x88\x01\n\x18\x41\x63tiveNotificationRecord\x12\n\n\x02id\x18\x01 \x02(\x03\x12M\n\x13\x63lient_notification\x18\x02 \x02(\x0b\x32\x30.cohesity.gandalf.server.stub.ClientNotification\x12\x11\n\tref_count\x18\x03 \x02(\x05\"X\n\x10\x44\x61taFormatRecord\x12$\n\x1cuse_refcounted_notifications\x18\x01 \x01(\x08\x12\x1e\n\x16\x65nable_opclock_caching\x18\x02 \x01(\x08\"x\n\x10GandalfWALRecord\x12\x14\n\x0cupdated_keys\x18\x01 \x03(\t\x12\x38\n\x0eupdated_values\x18\x02 \x03(\x0b\x32 .cohesity.gandalf.server.DbValue\x12\x14\n\x0c\x64\x65leted_keys\x18\x03 \x03(\tB\x03\x80\x01\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'gandalf.server.db.record_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\200\001\001'
  _globals['_SESSIONRECORD'].fields_by_name['legacy_unacked_notifications_DEPRECATED']._loaded_options = None
  _globals['_SESSIONRECORD'].fields_by_name['legacy_unacked_notifications_DEPRECATED']._serialized_options = b'\030\001'
  _globals['_DBVALUE']._serialized_start=148
  _globals['_DBVALUE']._serialized_end=926
  _globals['_SESSIONRECORD']._serialized_start=929
  _globals['_SESSIONRECORD']._serialized_end=1875
  _globals['_SESSIONRECORD_QUEUEDNOTIFICATION']._serialized_start=1526
  _globals['_SESSIONRECORD_QUEUEDNOTIFICATION']._serialized_end=1631
  _globals['_SESSIONRECORD_REGISTEREDREQUEST']._serialized_start=1634
  _globals['_SESSIONRECORD_REGISTEREDREQUEST']._serialized_end=1875
  _globals['_SESSIONRECORD_REGISTEREDREQUEST_TYPE']._serialized_start=1773
  _globals['_SESSIONRECORD_REGISTEREDREQUEST_TYPE']._serialized_end=1875
  _globals['_LOCKRECORD']._serialized_start=1878
  _globals['_LOCKRECORD']._serialized_end=2444
  _globals['_LOCKRECORD_LOCKREQUESTER']._serialized_start=2089
  _globals['_LOCKRECORD_LOCKREQUESTER']._serialized_end=2393
  _globals['_LOCKRECORD_WATCHER']._serialized_start=2395
  _globals['_LOCKRECORD_WATCHER']._serialized_end=2444
  _globals['_KEYRECORD']._serialized_start=2447
  _globals['_KEYRECORD']._serialized_end=2626
  _globals['_KEYRECORD_KEYWATCHER']._serialized_start=2574
  _globals['_KEYRECORD_KEYWATCHER']._serialized_end=2626
  _globals['_NAMESPACERECORD']._serialized_start=2629
  _globals['_NAMESPACERECORD']._serialized_end=3095
  _globals['_NAMESPACERECORD_CONSTITUENT']._serialized_start=2880
  _globals['_NAMESPACERECORD_CONSTITUENT']._serialized_end=3035
  _globals['_NAMESPACERECORD_NAMESPACEWATCHER']._serialized_start=3037
  _globals['_NAMESPACERECORD_NAMESPACEWATCHER']._serialized_end=3095
  _globals['_OPCLOCKRECORD']._serialized_start=3097
  _globals['_OPCLOCKRECORD']._serialized_end=3150
  _globals['_ACTIVENOTIFICATIONRECORD']._serialized_start=3153
  _globals['_ACTIVENOTIFICATIONRECORD']._serialized_end=3289
  _globals['_DATAFORMATRECORD']._serialized_start=3291
  _globals['_DATAFORMATRECORD']._serialized_end=3379
  _globals['_GANDALFWALRECORD']._serialized_start=3381
  _globals['_GANDALFWALRECORD']._serialized_end=3501
# @@protoc_insertion_point(module_scope)
