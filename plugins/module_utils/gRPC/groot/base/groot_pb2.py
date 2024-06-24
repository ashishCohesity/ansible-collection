# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: groot/base/groot.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from groot.base import error_pb2 as groot_dot_base_dot_error__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16groot/base/groot.proto\x12\x13\x63ohesity.groot.base\x1a\x16groot/base/error.proto\"\xe0\x03\n\x0bServiceInfo\x12\x12\n\nservice_id\x18\x01 \x02(\x03\x12\x14\n\x0cservice_name\x18\x02 \x02(\t\x12\x0c\n\x04port\x18\x07 \x02(\x05\x12\x14\n\x0cnum_replicas\x18\x03 \x02(\x03\x12=\n\rcluster_state\x18\x04 \x02(\x0e\x32&.cohesity.groot.base.ServiceInfo.State\x12\x46\n\x10replica_info_vec\x18\x05 \x03(\x0b\x32,.cohesity.groot.base.ServiceInfo.ReplicaInfo\x12\x1a\n\x12has_master_replica\x18\x08 \x01(\x08\x12\x10\n\x08\x65poch_id\x18\x06 \x02(\x03\x12L\n\x16older_replica_info_vec\x18\t \x03(\x0b\x32,.cohesity.groot.base.ServiceInfo.ReplicaInfo\x1a[\n\x0bReplicaInfo\x12\x0f\n\x07node_id\x18\x01 \x02(\x03\x12\x0f\n\x07node_ip\x18\x02 \x01(\t\x12\x0f\n\x07\x64isk_id\x18\x03 \x01(\x03\x12\x19\n\x11is_master_replica\x18\x04 \x01(\x08\"#\n\x05State\x12\n\n\x06kReady\x10\x01\x12\x0e\n\nkMigrating\x10\x02\"Y\n\x12LookupMasterResult\x12)\n\x05\x65rror\x18\x01 \x01(\x0b\x32\x1a.cohesity.groot.ErrorProto\x12\n\n\x02ip\x18\x02 \x01(\t\x12\x0c\n\x04port\x18\x03 \x01(\x05\"\x8a\x02\n\x15GetDatabaseInfoResult\x12)\n\x05\x65rror\x18\x01 \x01(\x0b\x32\x1a.cohesity.groot.ErrorProto\x12R\n\x11\x64\x61tabase_info_vec\x18\x02 \x03(\x0b\x32\x37.cohesity.groot.base.GetDatabaseInfoResult.DatabaseInfo\x1ar\n\x0c\x44\x61tabaseInfo\x12\x0f\n\x07node_id\x18\x01 \x02(\x03\x12\x0f\n\x07node_ip\x18\x02 \x02(\t\x12\x0c\n\x04port\x18\x03 \x02(\x05\x12\x18\n\x10\x64\x65\x66\x61ult_username\x18\x04 \x01(\t\x12\x18\n\x10\x64\x65\x66\x61ult_password\x18\x05 \x01(\t\"I\n\x1cTriggerMagnetoFullsyncResult\x12)\n\x05\x65rror\x18\x01 \x01(\x0b\x32\x1a.cohesity.groot.ErrorProtoB\x15Z\x13groot/base/groot.pb')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'groot.base.groot_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\023groot/base/groot.pb'
  _globals['_SERVICEINFO']._serialized_start=72
  _globals['_SERVICEINFO']._serialized_end=552
  _globals['_SERVICEINFO_REPLICAINFO']._serialized_start=424
  _globals['_SERVICEINFO_REPLICAINFO']._serialized_end=515
  _globals['_SERVICEINFO_STATE']._serialized_start=517
  _globals['_SERVICEINFO_STATE']._serialized_end=552
  _globals['_LOOKUPMASTERRESULT']._serialized_start=554
  _globals['_LOOKUPMASTERRESULT']._serialized_end=643
  _globals['_GETDATABASEINFORESULT']._serialized_start=646
  _globals['_GETDATABASEINFORESULT']._serialized_end=912
  _globals['_GETDATABASEINFORESULT_DATABASEINFO']._serialized_start=798
  _globals['_GETDATABASEINFORESULT_DATABASEINFO']._serialized_end=912
  _globals['_TRIGGERMAGNETOFULLSYNCRESULT']._serialized_start=914
  _globals['_TRIGGERMAGNETOFULLSYNCRESULT']._serialized_end=987
# @@protoc_insertion_point(module_scope)
