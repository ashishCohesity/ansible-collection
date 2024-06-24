# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bridge/iscsi_portal/scsi/logical_unit_metadata.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4bridge/iscsi_portal/scsi/logical_unit_metadata.proto\x12\x15\x63ohesity.bridge.iscsi\">\n\x0cScsiPeerInfo\x12\x16\n\x0e\x63onstituent_id\x18\x01 \x01(\x03\x12\x16\n\x0eincarnation_id\x18\x02 \x01(\x03\"\xe2\t\n\x18LogicalUnitMetadataProto\x12\x11\n\tfile_path\x18\x01 \x01(\t\x12\x65\n\x16persistent_reservation\x18\x03 \x01(\x0b\x32\x45.cohesity.bridge.iscsi.LogicalUnitMetadataProto.PersistentReservation\x12k\n\x17initiator_condition_map\x18\x04 \x03(\x0b\x32J.cohesity.bridge.iscsi.LogicalUnitMetadataProto.InitiatorConditionMapEntry\x1a\xb1\x04\n\x15PersistentReservation\x12\r\n\x05\x65poch\x18\x01 \x01(\x04\x12\"\n\x1apersist_through_power_lost\x18\x02 \x01(\x08\x12w\n\x12registered_key_map\x18\x03 \x03(\x0b\x32[.cohesity.bridge.iscsi.LogicalUnitMetadataProto.PersistentReservation.RegisteredKeyMapEntry\x12\x13\n\x0bis_reserved\x18\x04 \x01(\x08\x12\"\n\x1areserved_initiator_port_id\x18\x05 \x01(\x03\x12\x14\n\x0creserved_key\x18\x06 \x01(\x04\x12\x15\n\rreserved_type\x18\x07 \x01(\r\x1av\n\x0eReservationKey\x12\x0b\n\x03key\x18\x01 \x01(\x04\x12\x36\n\tpeer_info\x18\x02 \x01(\x0b\x32#.cohesity.bridge.iscsi.ScsiPeerInfo\x12\x1f\n\x17registration_time_usecs\x18\x03 \x01(\x03\x1a\x8d\x01\n\x15RegisteredKeyMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\x03\x12\x63\n\x05value\x18\x02 \x01(\x0b\x32T.cohesity.bridge.iscsi.LogicalUnitMetadataProto.PersistentReservation.ReservationKey:\x02\x38\x01\x1ag\n\x16UnitAttentionCondition\x12\x1d\n\x15\x61\x64\x64itional_sense_code\x18\x01 \x01(\r\x12\x11\n\tclear_aca\x18\x02 \x01(\x08\x12\x1b\n\x13\x63reation_time_usecs\x18\x03 \x01(\x03\x1a\xb5\x01\n\x1bInitiatorUnitAttentionState\x12\x36\n\tpeer_info\x18\x01 \x01(\x0b\x32#.cohesity.bridge.iscsi.ScsiPeerInfo\x12^\n\x0e\x63ondition_list\x18\x02 \x03(\x0b\x32\x46.cohesity.bridge.iscsi.LogicalUnitMetadataProto.UnitAttentionCondition\x1a\x89\x01\n\x1aInitiatorConditionMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\x03\x12Z\n\x05value\x18\x02 \x01(\x0b\x32K.cohesity.bridge.iscsi.LogicalUnitMetadataProto.InitiatorUnitAttentionState:\x02\x38\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'bridge.iscsi_portal.scsi.logical_unit_metadata_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_LOGICALUNITMETADATAPROTO_PERSISTENTRESERVATION_REGISTEREDKEYMAPENTRY']._loaded_options = None
  _globals['_LOGICALUNITMETADATAPROTO_PERSISTENTRESERVATION_REGISTEREDKEYMAPENTRY']._serialized_options = b'8\001'
  _globals['_LOGICALUNITMETADATAPROTO_INITIATORCONDITIONMAPENTRY']._loaded_options = None
  _globals['_LOGICALUNITMETADATAPROTO_INITIATORCONDITIONMAPENTRY']._serialized_options = b'8\001'
  _globals['_SCSIPEERINFO']._serialized_start=79
  _globals['_SCSIPEERINFO']._serialized_end=141
  _globals['_LOGICALUNITMETADATAPROTO']._serialized_start=144
  _globals['_LOGICALUNITMETADATAPROTO']._serialized_end=1394
  _globals['_LOGICALUNITMETADATAPROTO_PERSISTENTRESERVATION']._serialized_start=404
  _globals['_LOGICALUNITMETADATAPROTO_PERSISTENTRESERVATION']._serialized_end=965
  _globals['_LOGICALUNITMETADATAPROTO_PERSISTENTRESERVATION_RESERVATIONKEY']._serialized_start=703
  _globals['_LOGICALUNITMETADATAPROTO_PERSISTENTRESERVATION_RESERVATIONKEY']._serialized_end=821
  _globals['_LOGICALUNITMETADATAPROTO_PERSISTENTRESERVATION_REGISTEREDKEYMAPENTRY']._serialized_start=824
  _globals['_LOGICALUNITMETADATAPROTO_PERSISTENTRESERVATION_REGISTEREDKEYMAPENTRY']._serialized_end=965
  _globals['_LOGICALUNITMETADATAPROTO_UNITATTENTIONCONDITION']._serialized_start=967
  _globals['_LOGICALUNITMETADATAPROTO_UNITATTENTIONCONDITION']._serialized_end=1070
  _globals['_LOGICALUNITMETADATAPROTO_INITIATORUNITATTENTIONSTATE']._serialized_start=1073
  _globals['_LOGICALUNITMETADATAPROTO_INITIATORUNITATTENTIONSTATE']._serialized_end=1254
  _globals['_LOGICALUNITMETADATAPROTO_INITIATORCONDITIONMAPENTRY']._serialized_start=1257
  _globals['_LOGICALUNITMETADATAPROTO_INITIATORCONDITIONMAPENTRY']._serialized_end=1394
# @@protoc_insertion_point(module_scope)
