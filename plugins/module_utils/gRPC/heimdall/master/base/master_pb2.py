# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: heimdall/master/base/master.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from heimdall.base import error_pb2 as heimdall_dot_base_dot_error__pb2
from heimdall.master.stub import rpc_service_pb2 as heimdall_dot_master_dot_stub_dot_rpc__service__pb2
from magneto.base import magneto_pb2 as magneto_dot_base_dot_magneto__pb2
try:
  magneto_dot_base_dot_env__params__pb2 = magneto_dot_base_dot_magneto__pb2.magneto_dot_base_dot_env__params__pb2
except AttributeError:
  magneto_dot_base_dot_env__params__pb2 = magneto_dot_base_dot_magneto__pb2.magneto.base.env_params_pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!heimdall/master/base/master.proto\x12\x18\x63ohesity.heimdall.master\x1a\x19heimdall/base/error.proto\x1a&heimdall/master/stub/rpc_service.proto\x1a\x1amagneto/base/magneto.proto\"\xdf\x07\n\tFleetInfo\x12\x12\n\nip_address\x18\x02 \x01(\t\x12:\n\x06status\x18\x05 \x01(\x0e\x32*.cohesity.heimdall.master.FleetInfo.Status\x12L\n\ragents_health\x18\x0c \x03(\x0b\x32\x35.cohesity.heimdall.master.FleetInfo.AgentsHealthEntry\x12\x43\n\x07os_type\x18\r \x01(\x0e\x32*.cohesity.heimdall.master.stub.FleetOSType:\x06kLinux\x12\x0e\n\x02id\x18\x01 \x01(\tB\x02\x18\x01\x12\x43\n\x0b\x65nvironment\x18\x03 \x01(\x0e\x32*.cohesity.heimdall.master.stub.EnvironmentB\x02\x18\x01\x12\x1c\n\x10source_entity_id\x18\x04 \x01(\x03\x42\x02\x18\x01\x12L\n\x0brequest_map\x18\x06 \x03(\x0b\x32\x33.cohesity.heimdall.master.FleetInfo.RequestMapEntryB\x02\x18\x01\x12\x30\n\x05\x65rror\x18\x07 \x01(\x0b\x32\x1d.cohesity.heimdall.ErrorProtoB\x02\x18\x01\x12\x10\n\x04name\x18\x08 \x01(\tB\x02\x18\x01\x12\x46\n\rworkflow_type\x18\t \x01(\x0e\x32+.cohesity.heimdall.master.stub.WorkflowTypeB\x02\x18\x01\x12\x1c\n\x10\x63reate_time_secs\x18\n \x01(\x03\x42\x02\x18\x01\x12\"\n\x16last_release_time_secs\x18\x0b \x01(\x03\x42\x02\x18\x01\x1aR\n\x11\x41gentsHealthEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12,\n\x05value\x18\x02 \x01(\x0b\x32\x1d.cohesity.heimdall.ErrorProto:\x02\x38\x01\x1aT\n\x0fRequestMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x30\n\x05value\x18\x02 \x01(\x0b\x32!.cohesity.heimdall.master.Request:\x02\x38\x01\"\xab\x01\n\x06Status\x12\x17\n\x13kLaunchIntentLogged\x10\x01\x12\r\n\tkLaunched\x10\x02\x12\x19\n\x15kAddedToClusterConfig\x10\x06\x12\x12\n\x0ekAgentsStarted\x10\x03\x12\x1d\n\x19kRemovedFromClusterConfig\x10\x07\x12\x1a\n\x16kTerminationInProgress\x10\x05\x12\x0f\n\x0bkTerminated\x10\x04*\x08\x08\x64\x10\x80\x80\x80\x80\x02\"\xe6\x07\n\x0cResourceInfo\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12?\n\x0b\x65nvironment\x18\x03 \x01(\x0e\x32*.cohesity.heimdall.master.stub.Environment\x12\x18\n\x10source_entity_id\x18\x04 \x01(\x03\x12=\n\x06status\x18\x05 \x01(\x0e\x32-.cohesity.heimdall.master.ResourceInfo.Status\x12K\n\x0brequest_map\x18\x06 \x03(\x0b\x32\x36.cohesity.heimdall.master.ResourceInfo.RequestMapEntry\x12,\n\x05\x65rror\x18\x07 \x01(\x0b\x32\x1d.cohesity.heimdall.ErrorProto\x12\x42\n\rworkflow_type\x18\x08 \x01(\x0e\x32+.cohesity.heimdall.master.stub.WorkflowType\x12\x42\n\rresource_type\x18\t \x01(\x0e\x32+.cohesity.heimdall.master.stub.ResourceType\x12\x18\n\x10\x63reate_time_secs\x18\n \x01(\x03\x12\x1e\n\x16last_release_time_secs\x18\x0b \x01(\x03\x12<\n\nrigel_info\x18\x0f \x01(\x0b\x32(.cohesity.heimdall.master.stub.RigelInfo\x12\x39\n\nfleet_info\x18\x0c \x01(\x0b\x32#.cohesity.heimdall.master.FleetInfoH\x00\x12\x44\n\x10\x64isk_access_info\x18\r \x01(\x0b\x32(.cohesity.heimdall.master.DiskAccessInfoH\x00\x12\x39\n\ndisks_info\x18\x0e \x01(\x0b\x32#.cohesity.heimdall.master.DisksInfoH\x00\x1aT\n\x0fRequestMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x30\n\x05value\x18\x02 \x01(\x0b\x32!.cohesity.heimdall.master.Request:\x02\x38\x01\"}\n\x06Status\x12\x17\n\x13kCreateIntentLogged\x10\x01\x12\x0c\n\x08kCreated\x10\x02\x12\x17\n\x13kDeletionInProgress\x10\x03\x12\x0c\n\x08kDeleted\x10\x04\x12\x16\n\x12kReleaseInProgress\x10\x05\x12\r\n\tkReleased\x10\x06\x42\x16\n\x14ResourceDetailedInfo\"\xc2\x01\n\x0e\x44iskAccessInfo\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x16\n\x0e\x64isk_access_id\x18\x02 \x01(\t\x12\x1d\n\x15private_endpoint_name\x18\x03 \x01(\t\x12\x1b\n\x13private_endpoint_id\x18\x04 \x01(\t\x12\x1d\n\x15private_endpoint_fqdn\x18\x05 \x01(\t\x12%\n\x1dprivate_endpoint_ipv4_address\x18\x06 \x01(\t*\x08\x08\x64\x10\x80\x80\x80\x80\x02\"\xb7\x03\n\tDisksInfo\x12\x1a\n\x0fnumber_of_disks\x18\x01 \x01(\x05:\x01\x31\x12\x12\n\nsize_bytes\x18\x02 \x01(\x03\x12:\n\x06status\x18\x03 \x01(\x0e\x32*.cohesity.heimdall.master.DisksInfo.Status\x12\x43\n\rdisk_info_vec\x18\x04 \x03(\x0b\x32,.cohesity.heimdall.master.DisksInfo.DiskInfo\x12!\n\x12is_resize_required\x18\x05 \x01(\x08:\x05\x66\x61lse\x12\x1f\n\x17last_modified_time_secs\x18\x06 \x01(\x03\x1a=\n\x08\x44iskInfo\x12\x0f\n\x07\x64isk_id\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65vice_name\x18\x02 \x01(\t\x12\x0b\n\x03lun\x18\x03 \x01(\x05\"l\n\x06Status\x12\x17\n\x13kLaunchIntentLogged\x10\x01\x12\r\n\tkLaunched\x10\x02\x12\x0c\n\x08kResized\x10\x03\x12\r\n\tkAttached\x10\x04\x12\x0c\n\x08kMounted\x10\x05\x12\x0f\n\x0bkReadyToUse\x10\x06*\x08\x08\x64\x10\x80\x80\x80\x80\x02\"\x9a\x02\n\x07Request\x12\n\n\x02id\x18\x01 \x01(\t\x12\x42\n\rworkflow_type\x18\x02 \x01(\x0e\x32+.cohesity.heimdall.master.stub.WorkflowType\x12\x1e\n\x16\x61\x63quire_timestamp_secs\x18\x03 \x01(\x03\x12L\n\x17requested_resource_type\x18\x04 \x01(\x0e\x32+.cohesity.heimdall.master.stub.ResourceType\x12Q\n\x17requested_resources_map\x18\x05 \x01(\x0b\x32\x30.cohesity.heimdall.master.stub.ResourceWeightMap\"\x1e\n\x0cListOfString\x12\x0e\n\x06values\x18\x01 \x03(\t\"`\n\x17HeimdallConnectorParams\x12;\n\x10\x63onnector_params\x18\x01 \x01(\x0b\x32!.cohesity.magneto.ConnectorParams*\x08\x08\x64\x10\x80\x80\x80\x80\x02\"\x8c\x01\n\nOSToAMIMap\x12K\n\ros_to_ami_map\x18\x01 \x03(\x0b\x32\x34.cohesity.heimdall.master.OSToAMIMap.OsToAmiMapEntry\x1a\x31\n\x0fOsToAmiMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xf5\x01\n\x0eHeimdallConfig\x12\\\n\x13workflow_weight_map\x18\x01 \x03(\x0b\x32?.cohesity.heimdall.master.HeimdallConfig.WorkflowWeightMapEntry\x12\x19\n\x11resource_name_vec\x18\x02 \x03(\t\x1aj\n\x16WorkflowWeightMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12?\n\x05value\x18\x02 \x01(\x0b\x32\x30.cohesity.heimdall.master.stub.ResourceWeightMap:\x02\x38\x01\"\xbd\x01\n\x0c\x43loudzMapKey\x12\x18\n\x10source_entity_id\x18\x01 \x01(\x03\x12\x0e\n\x06region\x18\x02 \x01(\t\x12?\n\x0b\x65nvironment\x18\x03 \x01(\x0e\x32*.cohesity.heimdall.master.stub.Environment\x12\x42\n\rworkflow_type\x18\x04 \x01(\x0e\x32+.cohesity.heimdall.master.stub.WorkflowType*B\n\nFleetAgent\x12\x0e\n\nkYodaAgent\x10\x01\x12\x11\n\rkStorageProxy\x10\x02\x12\x11\n\rkWindowsAgent\x10\x03*+\n\x11\x46leetResourceType\x12\x0c\n\x08kNetwork\x10\x01\x12\x08\n\x04kCPU\x10\x02*\x8c\x01\n\nUpdateType\x12\x17\n\x13kLaunchIntentLogged\x10\x01\x12\x14\n\x10kResourceCreated\x10\x02\x12\x14\n\x10kResourceDeleted\x10\x03\x12\x14\n\x10kRequestAssigned\x10\x04\x12\x14\n\x10kRequestReleased\x10\x05\x12\r\n\tkNewError\x10\x06*,\n\x11\x44iskPartitionType\x12\r\n\tkStandard\x10\x01\x12\x08\n\x04kLVM\x10\x02*%\n\x0e\x46ileSystemType\x12\t\n\x05kEXT4\x10\x01\x12\x08\n\x04kXFS\x10\x02')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'heimdall.master.base.master_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_FLEETINFO_AGENTSHEALTHENTRY']._loaded_options = None
  _globals['_FLEETINFO_AGENTSHEALTHENTRY']._serialized_options = b'8\001'
  _globals['_FLEETINFO_REQUESTMAPENTRY']._loaded_options = None
  _globals['_FLEETINFO_REQUESTMAPENTRY']._serialized_options = b'8\001'
  _globals['_FLEETINFO'].fields_by_name['id']._loaded_options = None
  _globals['_FLEETINFO'].fields_by_name['id']._serialized_options = b'\030\001'
  _globals['_FLEETINFO'].fields_by_name['environment']._loaded_options = None
  _globals['_FLEETINFO'].fields_by_name['environment']._serialized_options = b'\030\001'
  _globals['_FLEETINFO'].fields_by_name['source_entity_id']._loaded_options = None
  _globals['_FLEETINFO'].fields_by_name['source_entity_id']._serialized_options = b'\030\001'
  _globals['_FLEETINFO'].fields_by_name['request_map']._loaded_options = None
  _globals['_FLEETINFO'].fields_by_name['request_map']._serialized_options = b'\030\001'
  _globals['_FLEETINFO'].fields_by_name['error']._loaded_options = None
  _globals['_FLEETINFO'].fields_by_name['error']._serialized_options = b'\030\001'
  _globals['_FLEETINFO'].fields_by_name['name']._loaded_options = None
  _globals['_FLEETINFO'].fields_by_name['name']._serialized_options = b'\030\001'
  _globals['_FLEETINFO'].fields_by_name['workflow_type']._loaded_options = None
  _globals['_FLEETINFO'].fields_by_name['workflow_type']._serialized_options = b'\030\001'
  _globals['_FLEETINFO'].fields_by_name['create_time_secs']._loaded_options = None
  _globals['_FLEETINFO'].fields_by_name['create_time_secs']._serialized_options = b'\030\001'
  _globals['_FLEETINFO'].fields_by_name['last_release_time_secs']._loaded_options = None
  _globals['_FLEETINFO'].fields_by_name['last_release_time_secs']._serialized_options = b'\030\001'
  _globals['_RESOURCEINFO_REQUESTMAPENTRY']._loaded_options = None
  _globals['_RESOURCEINFO_REQUESTMAPENTRY']._serialized_options = b'8\001'
  _globals['_OSTOAMIMAP_OSTOAMIMAPENTRY']._loaded_options = None
  _globals['_OSTOAMIMAP_OSTOAMIMAPENTRY']._serialized_options = b'8\001'
  _globals['_HEIMDALLCONFIG_WORKFLOWWEIGHTMAPENTRY']._loaded_options = None
  _globals['_HEIMDALLCONFIG_WORKFLOWWEIGHTMAPENTRY']._serialized_options = b'8\001'
  _globals['_FLEETAGENT']._serialized_start=3790
  _globals['_FLEETAGENT']._serialized_end=3856
  _globals['_FLEETRESOURCETYPE']._serialized_start=3858
  _globals['_FLEETRESOURCETYPE']._serialized_end=3901
  _globals['_UPDATETYPE']._serialized_start=3904
  _globals['_UPDATETYPE']._serialized_end=4044
  _globals['_DISKPARTITIONTYPE']._serialized_start=4046
  _globals['_DISKPARTITIONTYPE']._serialized_end=4090
  _globals['_FILESYSTEMTYPE']._serialized_start=4092
  _globals['_FILESYSTEMTYPE']._serialized_end=4129
  _globals['_FLEETINFO']._serialized_start=159
  _globals['_FLEETINFO']._serialized_end=1150
  _globals['_FLEETINFO_AGENTSHEALTHENTRY']._serialized_start=798
  _globals['_FLEETINFO_AGENTSHEALTHENTRY']._serialized_end=880
  _globals['_FLEETINFO_REQUESTMAPENTRY']._serialized_start=882
  _globals['_FLEETINFO_REQUESTMAPENTRY']._serialized_end=966
  _globals['_FLEETINFO_STATUS']._serialized_start=969
  _globals['_FLEETINFO_STATUS']._serialized_end=1140
  _globals['_RESOURCEINFO']._serialized_start=1153
  _globals['_RESOURCEINFO']._serialized_end=2151
  _globals['_RESOURCEINFO_REQUESTMAPENTRY']._serialized_start=882
  _globals['_RESOURCEINFO_REQUESTMAPENTRY']._serialized_end=966
  _globals['_RESOURCEINFO_STATUS']._serialized_start=2002
  _globals['_RESOURCEINFO_STATUS']._serialized_end=2127
  _globals['_DISKACCESSINFO']._serialized_start=2154
  _globals['_DISKACCESSINFO']._serialized_end=2348
  _globals['_DISKSINFO']._serialized_start=2351
  _globals['_DISKSINFO']._serialized_end=2790
  _globals['_DISKSINFO_DISKINFO']._serialized_start=2609
  _globals['_DISKSINFO_DISKINFO']._serialized_end=2670
  _globals['_DISKSINFO_STATUS']._serialized_start=2672
  _globals['_DISKSINFO_STATUS']._serialized_end=2780
  _globals['_REQUEST']._serialized_start=2793
  _globals['_REQUEST']._serialized_end=3075
  _globals['_LISTOFSTRING']._serialized_start=3077
  _globals['_LISTOFSTRING']._serialized_end=3107
  _globals['_HEIMDALLCONNECTORPARAMS']._serialized_start=3109
  _globals['_HEIMDALLCONNECTORPARAMS']._serialized_end=3205
  _globals['_OSTOAMIMAP']._serialized_start=3208
  _globals['_OSTOAMIMAP']._serialized_end=3348
  _globals['_OSTOAMIMAP_OSTOAMIMAPENTRY']._serialized_start=3299
  _globals['_OSTOAMIMAP_OSTOAMIMAPENTRY']._serialized_end=3348
  _globals['_HEIMDALLCONFIG']._serialized_start=3351
  _globals['_HEIMDALLCONFIG']._serialized_end=3596
  _globals['_HEIMDALLCONFIG_WORKFLOWWEIGHTMAPENTRY']._serialized_start=3490
  _globals['_HEIMDALLCONFIG_WORKFLOWWEIGHTMAPENTRY']._serialized_end=3596
  _globals['_CLOUDZMAPKEY']._serialized_start=3599
  _globals['_CLOUDZMAPKEY']._serialized_end=3788
# @@protoc_insertion_point(module_scope)
