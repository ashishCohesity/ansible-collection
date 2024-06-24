# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: nexus/eagle_agent/base/helios_event.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from alerts.base import alert_pb2 as alerts_dot_base_dot_alert__pb2
from alerts.master.stub import master_service_pb2 as alerts_dot_master_dot_stub_dot_master__service__pb2
from nexus.eagle_agent.base import helios_cluster_base_pb2 as nexus_dot_eagle__agent_dot_base_dot_helios__cluster__base__pb2
try:
  helios_dot_base_dot_helios__cluster__base__pb2 = nexus_dot_eagle__agent_dot_base_dot_helios__cluster__base__pb2.helios_dot_base_dot_helios__cluster__base__pb2
except AttributeError:
  helios_dot_base_dot_helios__cluster__base__pb2 = nexus_dot_eagle__agent_dot_base_dot_helios__cluster__base__pb2.helios.base.helios_cluster_base_pb2
from nexus.base import services_gflags_pb2 as nexus_dot_base_dot_services__gflags__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)nexus/eagle_agent/base/helios_event.proto\x12\x15\x63ohesity.helios.event\x1a\x17\x61lerts/base/alert.proto\x1a\'alerts/master/stub/master_service.proto\x1a\x30nexus/eagle_agent/base/helios_cluster_base.proto\x1a nexus/base/services_gflags.proto\"\xcd\x07\n\x05\x45vent\x12\x12\n\nevent_uuid\x18\x01 \x01(\t\x12\x43\n\x12\x63luster_identifier\x18\x02 \x01(\x0b\x32\'.cohesity.helios.base.ClusterIdentifier\x12\x34\n\x04type\x18\x03 \x01(\x0e\x32&.cohesity.helios.event.Event.EventType\x12\x12\n\nevent_name\x18\x04 \x01(\t\x12:\n\x06source\x18\x05 \x01(\x0e\x32*.cohesity.helios.event.Event.EventHostType\x12\"\n\x1aoccurrence_timestamp_usecs\x18\x06 \x01(\x03\x12\x1b\n\x13processed_timestamp\x18\x07 \x01(\t\x12\x17\n\x0fvisible_to_user\x18\x08 \x01(\x08\x12M\n\x0e\x61lert_instance\x18\t \x01(\x0b\x32\x35.cohesity.alerts.master.QueryAlertsResult.AlertDetail\x12<\n\x08\x63\x61tegory\x18\n \x01(\x0e\x32*.cohesity.helios.event.Event.EventCategory\x12;\n\x0b\x61lert_state\x18\x0b \x01(\x0e\x32&.cohesity.alerts.AlertProto.AlertState\x12=\n\tprocessor\x18\x10 \x01(\x0e\x32*.cohesity.helios.event.Event.EventHostType\x12\x17\n\x0f\x61\x64\x64itional_data\x18\x11 \x01(\x0c\x12S\n\x0egflag_instance\x18\x12 \x01(\x0b\x32;.cohesity.nexus.base.ServicesGflagsProto.ServiceProto.Gflag\x12:\n\rerror_details\x18\x13 \x01(\x0b\x32#.cohesity.helios.event.ErrorDetails\x12\x11\n\tnode_info\x18\x14 \x01(\t\x12\x14\n\x0c\x63luster_name\x18\x15 \x01(\t\"`\n\tEventType\x12\n\n\x06kAlert\x10\x00\x12\x11\n\rkNotification\x10\x01\x12\x1b\n\x17kClusterSoftwareUpgrade\x10\x02\x12\x0b\n\x07kGflags\x10\x03\x12\n\n\x06kError\x10\x04\"*\n\rEventHostType\x12\x0c\n\x08kCluster\x10\x00\x12\x0b\n\x07kHelios\x10\x01\"!\n\rEventCategory\x12\x10\n\x0ckSystemEvent\x10\x00\"q\n\x0c\x45rrorDetails\x12\x14\n\x0cservice_name\x18\x01 \x01(\t\x12\x0f\n\x07op_name\x18\x02 \x01(\t\x12\x13\n\x0bobject_name\x18\x03 \x01(\t\x12\x0e\n\x06object\x18\x04 \x01(\x0c\x12\x15\n\rerror_message\x18\x05 \x01(\t\"\x0c\n\nAuditLogId\"\x90\x01\n\x0f\x41uditSourceInfo\x12\x43\n\x12\x63luster_identifier\x18\x01 \x01(\x0b\x32\'.cohesity.helios.base.ClusterIdentifier\x12\x11\n\tuser_name\x18\x02 \x01(\t\x12\x0f\n\x07user_id\x18\x03 \x01(\r\x12\x14\n\x0cservice_name\x18\x04 \x01(\t\"\xbf\x04\n\rAuditLogProto\x12\x37\n\x0c\x61udit_log_id\x18\x01 \x01(\x0b\x32!.cohesity.helios.event.AuditLogId\x12\x41\n\x11\x61udit_source_info\x18\x02 \x01(\x0b\x32&.cohesity.helios.event.AuditSourceInfo\x12\x17\n\x0ftimestamp_usecs\x18\x03 \x01(\x03\x12\x42\n\naudit_type\x18\x04 \x01(\x0e\x32..cohesity.helios.event.AuditLogProto.AuditType\x12H\n\rresource_type\x18\x05 \x01(\x0e\x32\x31.cohesity.helios.event.AuditLogProto.ResourceType\x12\x17\n\x0f\x65ntity_type_vec\x18\x06 \x03(\t\x12\x1a\n\x12\x61\x64\x64itional_details\x18\x07 \x01(\t\"\x97\x01\n\tAuditType\x12\x0c\n\x08kCreated\x10\x01\x12\x0c\n\x08kDeleted\x10\x02\x12\x0c\n\x08kUpdated\x10\x03\x12\x0f\n\x0bkUnregister\x10\x04\x12\x0c\n\x08kUpgrade\x10\x05\x12\x0c\n\x08kTimeout\x10\x06\x12\x19\n\x15kClusterAuditDocument\x10\x07\x12\x18\n\x14kHeliosAuditDocument\x10\x08\"<\n\x0cResourceType\x12\r\n\tkGrpcConn\x10\x01\x12\x0f\n\x0bkGrpcPBConn\x10\x02\x12\x0c\n\x08kCluster\x10\x03\x42(Z&nexus/eagle_agent/base/helios_event.pb')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'nexus.eagle_agent.base.helios_event_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z&nexus/eagle_agent/base/helios_event.pb'
  _globals['_EVENT']._serialized_start=219
  _globals['_EVENT']._serialized_end=1192
  _globals['_EVENT_EVENTTYPE']._serialized_start=1017
  _globals['_EVENT_EVENTTYPE']._serialized_end=1113
  _globals['_EVENT_EVENTHOSTTYPE']._serialized_start=1115
  _globals['_EVENT_EVENTHOSTTYPE']._serialized_end=1157
  _globals['_EVENT_EVENTCATEGORY']._serialized_start=1159
  _globals['_EVENT_EVENTCATEGORY']._serialized_end=1192
  _globals['_ERRORDETAILS']._serialized_start=1194
  _globals['_ERRORDETAILS']._serialized_end=1307
  _globals['_AUDITLOGID']._serialized_start=1309
  _globals['_AUDITLOGID']._serialized_end=1321
  _globals['_AUDITSOURCEINFO']._serialized_start=1324
  _globals['_AUDITSOURCEINFO']._serialized_end=1468
  _globals['_AUDITLOGPROTO']._serialized_start=1471
  _globals['_AUDITLOGPROTO']._serialized_end=2046
  _globals['_AUDITLOGPROTO_AUDITTYPE']._serialized_start=1833
  _globals['_AUDITLOGPROTO_AUDITTYPE']._serialized_end=1984
  _globals['_AUDITLOGPROTO_RESOURCETYPE']._serialized_start=1986
  _globals['_AUDITLOGPROTO_RESOURCETYPE']._serialized_end=2046
# @@protoc_insertion_point(module_scope)
