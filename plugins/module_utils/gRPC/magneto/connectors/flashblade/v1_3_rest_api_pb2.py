# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: magneto/connectors/flashblade/v1_3_rest_api.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1magneto/connectors/flashblade/v1_3_rest_api.proto\x12 cohesity.magneto.flashblade.v1_3\"K\n\x0c\x45rrorContext\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x0f\n\x07\x63ontext\x18\x03 \x01(\t\x12\x0b\n\x03msg\x18\x04 \x01(\t\"\xaf\x01\n\x0f\x45rrorContextVec\x12L\n\rerror_ctx_vec\x18\x01 \x03(\x0b\x32..cohesity.magneto.flashblade.v1_3.ErrorContextR\x05\x65rror\x12N\n\x0e\x65rrors_ctx_vec\x18\x02 \x03(\x0b\x32..cohesity.magneto.flashblade.v1_3.ErrorContextR\x06\x65rrors\"F\n\x0ePaginationInfo\x12\x18\n\x10total_item_count\x18\x01 \x01(\x05\x12\x1a\n\x12\x63ontinuation_token\x18\x02 \x01(\t\"\x11\n\x0f\x41rraySpaceStats\"\x9d\x01\n\x14\x46ileSystemSpaceStats\x12\x35\n\x1dtotal_physical_usage_in_bytes\x18\x01 \x01(\x03R\x0etotal_physical\x12%\n\x15unique_usage_in_bytes\x18\x02 \x01(\x03R\x06unique\x12\'\n\x16logical_usage_in_bytes\x18\x03 \x01(\x03R\x07virtual\"7\n\x07NFSRule\x12\x0f\n\x07\x65nabled\x18\x01 \x01(\x08\x12\x1b\n\x0c\x65xport_rules\x18\x02 \x01(\tR\x05rules\",\n\x07SMBRule\x12\x0f\n\x07\x65nabled\x18\x01 \x01(\x08\x12\x10\n\x08\x61\x63l_mode\x18\x02 \x01(\t\"\x1b\n\x08HTTPRule\x12\x0f\n\x07\x65nabled\x18\x01 \x01(\x08\"D\n\x05\x41rray\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x12\x10\n\x08revision\x18\x03 \x01(\t\x12\x0f\n\x07version\x18\x04 \x01(\t\"8\n\x0f\x41\x63tiveDirectory\x12\x15\n\rcomputer_name\x18\x01 \x01(\t\x12\x0e\n\x06\x64omain\x18\x02 \x01(\t\"\xbc\x01\n\x17\x41\x63tiveDirectoryResponse\x12I\n\x0fpagination_info\x18\x01 \x01(\x0b\x32\x30.cohesity.magneto.flashblade.v1_3.PaginationInfo\x12V\n\x14\x61\x63tive_directory_vec\x18\x02 \x03(\x0b\x32\x31.cohesity.magneto.flashblade.v1_3.ActiveDirectoryR\x05items\"C\n\x10\x44irectoryService\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08services\x18\x02 \x03(\t\x12\x0f\n\x07\x65nabled\x18\x03 \x01(\x08\"\xc0\x01\n\x18\x44irectoryServiceResponse\x12I\n\x0fpagination_info\x18\x01 \x01(\x0b\x32\x30.cohesity.magneto.flashblade.v1_3.PaginationInfo\x12Y\n\x16\x64irectory_services_vec\x18\x02 \x03(\x0b\x32\x32.cohesity.magneto.flashblade.v1_3.DirectoryServiceR\x05items\"\xd2\x03\n\nFileSystem\x12\x0c\n\x04name\x18\x01 \x01(\t\x12(\n\x13\x63reation_time_msecs\x18\x02 \x01(\x03\x42\x02\x30\x02R\x07\x63reated\x12/\n\x16logical_capacity_bytes\x18\x03 \x01(\x03\x42\x02\x30\x02R\x0bprovisioned\x12\x38\n\x14snapshot_dir_enabled\x18\x04 \x01(\x08R\x1asnapshot_directory_enabled\x12\x11\n\tdestroyed\x18\x05 \x01(\x08\x12@\n\x08nfs_rule\x18\x06 \x01(\x0b\x32).cohesity.magneto.flashblade.v1_3.NFSRuleR\x03nfs\x12@\n\x08smb_rule\x18\x07 \x01(\x0b\x32).cohesity.magneto.flashblade.v1_3.SMBRuleR\x03smb\x12\x43\n\thttp_rule\x18\x08 \x01(\x0b\x32*.cohesity.magneto.flashblade.v1_3.HTTPRuleR\x04http\x12\x45\n\x05space\x18\t \x01(\x0b\x32\x36.cohesity.magneto.flashblade.v1_3.FileSystemSpaceStats\"\x0e\n\x0c\x45mptyRequest\")\n\x15\x43reateSessionResponse\x12\x10\n\x08username\x18\x01 \x01(\t\"+\n\x17ListAPIVersionsResponse\x12\x10\n\x08versions\x18\x01 \x03(\t\"U\n\x10GetArrayResponse\x12\x41\n\tarray_vec\x18\x01 \x03(\x0b\x32\'.cohesity.magneto.flashblade.v1_3.ArrayR\x05items\"\x84\x01\n\x10NetworkInterface\x12\x1b\n\nip_address\x18\x01 \x01(\tR\x07\x61\x64\x64ress\x12\x0f\n\x07\x65nabled\x18\x02 \x01(\x08\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x1d\n\x0bservice_vec\x18\x04 \x03(\tR\x08services\x12\x15\n\x07vlan_id\x18\x05 \x01(\x05R\x04vlan\"\xb0\x01\n\x13GetNetworksResponse\x12I\n\x0fpagination_info\x18\x01 \x01(\x0b\x32\x30.cohesity.magneto.flashblade.v1_3.PaginationInfo\x12N\n\x0bnetwork_vec\x18\x02 \x03(\x0b\x32\x32.cohesity.magneto.flashblade.v1_3.NetworkInterfaceR\x05items\"\xb1\x01\n\x16GetFileSystemsResponse\x12I\n\x0fpagination_info\x18\x01 \x01(\x0b\x32\x30.cohesity.magneto.flashblade.v1_3.PaginationInfo\x12L\n\x0f\x66ile_system_vec\x18\x02 \x03(\x0b\x32,.cohesity.magneto.flashblade.v1_3.FileSystemR\x05items\"\\\n\x18UpdateFileSystemsRequest\x12@\n\x08nfs_rule\x18\x01 \x01(\x0b\x32).cohesity.magneto.flashblade.v1_3.NFSRuleR\x03nfs\"i\n\x19UpdateFileSystemsResponse\x12L\n\x0f\x66ile_system_vec\x18\x01 \x03(\x0b\x32,.cohesity.magneto.flashblade.v1_3.FileSystemR\x05items\"\xcb\x01\n\x12\x46ileSystemSnapshot\x12(\n\x13\x63reation_time_msecs\x18\x01 \x01(\x03\x42\x02\x30\x02R\x07\x63reated\x12\x11\n\tdestroyed\x18\x02 \x01(\x08\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x0e\n\x06source\x18\x04 \x01(\t\x12\x0e\n\x06suffix\x18\x05 \x01(\t\x12\x18\n\x10source_destroyed\x18\x06 \x01(\x08\x12\x30\n\x14time_remaining_msecs\x18\x07 \x01(\x03\x42\x02\x30\x02R\x0etime_remaining\"\'\n\x15\x43reateSnapshotRequest\x12\x0e\n\x06suffix\x18\x01 \x01(\t\"w\n\x16\x43reateSnapshotResponse\x12]\n\x18\x66ile_system_snapshot_vec\x18\x01 \x03(\x0b\x32\x34.cohesity.magneto.flashblade.v1_3.FileSystemSnapshotR\x05items\"u\n\x14GetSnapshotsResponse\x12]\n\x18\x66ile_system_snapshot_vec\x18\x01 \x03(\x0b\x32\x34.cohesity.magneto.flashblade.v1_3.FileSystemSnapshotR\x05items\"*\n\x15UpdateSnapshotRequest\x12\x11\n\tdestroyed\x18\x01 \x01(\x08')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'magneto.connectors.flashblade.v1_3_rest_api_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_FILESYSTEM'].fields_by_name['creation_time_msecs']._loaded_options = None
  _globals['_FILESYSTEM'].fields_by_name['creation_time_msecs']._serialized_options = b'0\002'
  _globals['_FILESYSTEM'].fields_by_name['logical_capacity_bytes']._loaded_options = None
  _globals['_FILESYSTEM'].fields_by_name['logical_capacity_bytes']._serialized_options = b'0\002'
  _globals['_FILESYSTEMSNAPSHOT'].fields_by_name['creation_time_msecs']._loaded_options = None
  _globals['_FILESYSTEMSNAPSHOT'].fields_by_name['creation_time_msecs']._serialized_options = b'0\002'
  _globals['_FILESYSTEMSNAPSHOT'].fields_by_name['time_remaining_msecs']._loaded_options = None
  _globals['_FILESYSTEMSNAPSHOT'].fields_by_name['time_remaining_msecs']._serialized_options = b'0\002'
  _globals['_ERRORCONTEXT']._serialized_start=87
  _globals['_ERRORCONTEXT']._serialized_end=162
  _globals['_ERRORCONTEXTVEC']._serialized_start=165
  _globals['_ERRORCONTEXTVEC']._serialized_end=340
  _globals['_PAGINATIONINFO']._serialized_start=342
  _globals['_PAGINATIONINFO']._serialized_end=412
  _globals['_ARRAYSPACESTATS']._serialized_start=414
  _globals['_ARRAYSPACESTATS']._serialized_end=431
  _globals['_FILESYSTEMSPACESTATS']._serialized_start=434
  _globals['_FILESYSTEMSPACESTATS']._serialized_end=591
  _globals['_NFSRULE']._serialized_start=593
  _globals['_NFSRULE']._serialized_end=648
  _globals['_SMBRULE']._serialized_start=650
  _globals['_SMBRULE']._serialized_end=694
  _globals['_HTTPRULE']._serialized_start=696
  _globals['_HTTPRULE']._serialized_end=723
  _globals['_ARRAY']._serialized_start=725
  _globals['_ARRAY']._serialized_end=793
  _globals['_ACTIVEDIRECTORY']._serialized_start=795
  _globals['_ACTIVEDIRECTORY']._serialized_end=851
  _globals['_ACTIVEDIRECTORYRESPONSE']._serialized_start=854
  _globals['_ACTIVEDIRECTORYRESPONSE']._serialized_end=1042
  _globals['_DIRECTORYSERVICE']._serialized_start=1044
  _globals['_DIRECTORYSERVICE']._serialized_end=1111
  _globals['_DIRECTORYSERVICERESPONSE']._serialized_start=1114
  _globals['_DIRECTORYSERVICERESPONSE']._serialized_end=1306
  _globals['_FILESYSTEM']._serialized_start=1309
  _globals['_FILESYSTEM']._serialized_end=1775
  _globals['_EMPTYREQUEST']._serialized_start=1777
  _globals['_EMPTYREQUEST']._serialized_end=1791
  _globals['_CREATESESSIONRESPONSE']._serialized_start=1793
  _globals['_CREATESESSIONRESPONSE']._serialized_end=1834
  _globals['_LISTAPIVERSIONSRESPONSE']._serialized_start=1836
  _globals['_LISTAPIVERSIONSRESPONSE']._serialized_end=1879
  _globals['_GETARRAYRESPONSE']._serialized_start=1881
  _globals['_GETARRAYRESPONSE']._serialized_end=1966
  _globals['_NETWORKINTERFACE']._serialized_start=1969
  _globals['_NETWORKINTERFACE']._serialized_end=2101
  _globals['_GETNETWORKSRESPONSE']._serialized_start=2104
  _globals['_GETNETWORKSRESPONSE']._serialized_end=2280
  _globals['_GETFILESYSTEMSRESPONSE']._serialized_start=2283
  _globals['_GETFILESYSTEMSRESPONSE']._serialized_end=2460
  _globals['_UPDATEFILESYSTEMSREQUEST']._serialized_start=2462
  _globals['_UPDATEFILESYSTEMSREQUEST']._serialized_end=2554
  _globals['_UPDATEFILESYSTEMSRESPONSE']._serialized_start=2556
  _globals['_UPDATEFILESYSTEMSRESPONSE']._serialized_end=2661
  _globals['_FILESYSTEMSNAPSHOT']._serialized_start=2664
  _globals['_FILESYSTEMSNAPSHOT']._serialized_end=2867
  _globals['_CREATESNAPSHOTREQUEST']._serialized_start=2869
  _globals['_CREATESNAPSHOTREQUEST']._serialized_end=2908
  _globals['_CREATESNAPSHOTRESPONSE']._serialized_start=2910
  _globals['_CREATESNAPSHOTRESPONSE']._serialized_end=3029
  _globals['_GETSNAPSHOTSRESPONSE']._serialized_start=3031
  _globals['_GETSNAPSHOTSRESPONSE']._serialized_end=3148
  _globals['_UPDATESNAPSHOTREQUEST']._serialized_start=3150
  _globals['_UPDATESNAPSHOTREQUEST']._serialized_end=3192
# @@protoc_insertion_point(module_scope)
