# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: magneto/api/magneto_external_debug.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from magneto.api import enum_wrappers_pb2 as magneto_dot_api_dot_enum__wrappers__pb2
from magneto.api import enums_pb2 as magneto_dot_api_dot_enums__pb2
from magneto.api import magneto_external_base_pb2 as magneto_dot_api_dot_magneto__external__base__pb2
from util.base import universal_id_pb2 as util_dot_base_dot_universal__id__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(magneto/api/magneto_external_debug.proto\x12\x14\x63ohesity.magneto.api\x1a\x1fmagneto/api/enum_wrappers.proto\x1a\x17magneto/api/enums.proto\x1a\'magneto/api/magneto_external_base.proto\x1a\x1cutil/base/universal_id.proto\"\xeb\x01\n\x1aGetSnapshotLivenessInfoArg\x12\x30\n\x04\x62\x61se\x18\x01 \x01(\x0b\x32\".cohesity.magneto.api.ArgumentBase\x12+\n\x07job_uid\x18\x02 \x01(\x0b\x32\x1a.cohesity.UniversalIdProto\x12\x15\n\robject_id_vec\x18\x03 \x03(\x03\x12\x1c\n\x14run_start_time_usecs\x18\x05 \x01(\x03\x12\x39\n\rtime_interval\x18\x04 \x01(\x0b\x32\".cohesity.magneto.api.TimeInterval\"\x9d\x06\n\x1fObjectSnapshotLivenessInfoProto\x12\x31\n\x06object\x18\x01 \x01(\x0b\x32!.cohesity.magneto.api.ObjectProto\x12]\n\x11snapshot_info_vec\x18\x02 \x03(\x0b\x32\x42.cohesity.magneto.api.ObjectSnapshotLivenessInfoProto.SnapshotInfo\x1a\xe7\x04\n\x0cSnapshotInfo\x12\x13\n\x0bview_box_id\x18\x01 \x01(\x03\x12+\n\x07job_uid\x18\x02 \x01(\x0b\x32\x1a.cohesity.UniversalIdProto\x12\x1c\n\x14run_start_time_usecs\x18\x03 \x01(\x03\x12\x62\n\rcopy_info_vec\x18\x04 \x03(\x0b\x32K.cohesity.magneto.api.ObjectSnapshotLivenessInfoProto.SnapshotInfo.CopyInfo\x1a?\n\rLocalCopyInfo\x12\x11\n\tview_name\x18\x01 \x01(\t\x12\x1b\n\x13local_snapshot_path\x18\x02 \x01(\t\x1a\xd1\x02\n\x08\x43opyInfo\x12\x66\n\nlocal_copy\x18\x01 \x01(\x0b\x32P.cohesity.magneto.api.ObjectSnapshotLivenessInfoProto.SnapshotInfo.LocalCopyInfoH\x00\x12\x44\n\x0f\x61rchival_target\x18\x02 \x01(\x0b\x32).cohesity.magneto.api.ArchivalTargetProtoH\x00\x12#\n\x1bis_deleted_in_magneto_state\x18\x03 \x01(\x08\x12 \n\x18is_deleted_in_yoda_state\x18\x04 \x01(\x08\x12\x1d\n\x15is_deleted_on_snap_fs\x18\x05 \x01(\x08\x12\x1c\n\x14is_deleted_on_icebox\x18\x06 \x01(\x08\x42\x13\n\x11target_info_oneof\"t\n\'GetSnapshotLivenessInfoPaginationCookie\x12+\n\x07job_uid\x18\x01 \x01(\x0b\x32\x1a.cohesity.UniversalIdProto\x12\x1c\n\x14run_start_time_usecs\x18\x02 \x01(\x03\"\xa8\x02\n\x1dGetSnapshotLivenessInfoResult\x12.\n\x04\x62\x61se\x18\x01 \x01(\x0b\x32 .cohesity.magneto.api.ResultBase\x12Z\n\x0cliveness_map\x18\x02 \x03(\x0b\x32\x44.cohesity.magneto.api.GetSnapshotLivenessInfoResult.LivenessMapEntry\x12\x10\n\x08warnings\x18\x03 \x03(\t\x1ai\n\x10LivenessMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\x03\x12\x44\n\x05value\x18\x02 \x01(\x0b\x32\x35.cohesity.magneto.api.ObjectSnapshotLivenessInfoProto:\x02\x38\x01\"\xd7\x01\n\x1dGetBackupRunsInternalStateArg\x12\x30\n\x04\x62\x61se\x18\x01 \x01(\x0b\x32\".cohesity.magneto.api.ArgumentBase\x12+\n\x07job_uid\x18\x02 \x01(\x0b\x32\x1a.cohesity.UniversalIdProto\x12\x1c\n\x14run_start_time_usecs\x18\x03 \x01(\x03\x12\x39\n\rtime_interval\x18\x04 \x01(\x0b\x32\".cohesity.magneto.api.TimeInterval\"g\n BackupRunsInternalStateInfoProto\x12\x11\n\tis_gc_run\x18\x01 \x01(\x08\x12\x18\n\x10is_run_in_memory\x18\x02 \x01(\x08\x12\x16\n\x0escribe_key_vec\x18\x03 \x03(\t\"\xa4\x02\n GetBackupRunsInternalStateResult\x12.\n\x04\x62\x61se\x18\x01 \x01(\x0b\x32 .cohesity.magneto.api.ResultBase\x12\x62\n\x0f\x62\x61\x63kup_runs_map\x18\x02 \x03(\x0b\x32I.cohesity.magneto.api.GetBackupRunsInternalStateResult.BackupRunsMapEntry\x1al\n\x12\x42\x61\x63kupRunsMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\x03\x12\x45\n\x05value\x18\x02 \x01(\x0b\x32\x36.cohesity.magneto.api.BackupRunsInternalStateInfoProto:\x02\x38\x01\"\xd2\x05\n\x11\x45xportMetadataArg\x12\x30\n\x04\x62\x61se\x18\x01 \x01(\x0b\x32\".cohesity.magneto.api.ArgumentBase\x12S\n\x11metadata_selector\x18\x02 \x01(\x0b\x32\x38.cohesity.magneto.api.ExportMetadataArg.MetadataSelector\x12\x42\n\x08location\x18\x03 \x01(\x0b\x32\x30.cohesity.magneto.api.ExportMetadataArg.Location\x12\x43\n\x10\x64\x61ta_format_type\x18\x04 \x01(\x0e\x32).cohesity.magneto.api.DataFormatType.Type\x1a\xd2\x02\n\x10MetadataSelector\x12\x11\n\ttenant_id\x18\x01 \x01(\t\x12\x18\n\x10include_policies\x18\x02 \x01(\x08\x12 \n\x18include_job_descriptions\x18\x03 \x01(\x08\x12\x1d\n\x15include_restore_tasks\x18\x04 \x01(\x08\x12\x44\n\x14include_environments\x18\x05 \x03(\x0b\x32&.cohesity.magneto.api.EnvironmentProto\x12\x42\n\x0f\x65ntity_selector\x18\x06 \x01(\x0b\x32).cohesity.magneto.api.EntitySelectorProto\x12\x46\n\x0crun_selector\x18\x07 \x01(\x0b\x32\x30.cohesity.magneto.api.ProtectionRunSelectorProto\x1aX\n\x08Location\x12\x39\n\x04type\x18\x01 \x01(\x0e\x32+.cohesity.magneto.api.DataLocatorProto.Type\x12\x11\n\tview_name\x18\x02 \x01(\t\"c\n\x14\x45xportMetadataResult\x12.\n\x04\x62\x61se\x18\x01 \x01(\x0b\x32 .cohesity.magneto.api.ResultBase\x12\x1b\n\x13\x65xport_operation_id\x18\x02 \x01(\t\"m\n\x1cQueryExportMetadataStatusArg\x12\x30\n\x04\x62\x61se\x18\x01 \x01(\x0b\x32\".cohesity.magneto.api.ArgumentBase\x12\x1b\n\x13\x65xport_operation_id\x18\x02 \x01(\t\"\x87\x02\n\x1fQueryExportMetadataStatusResult\x12.\n\x04\x62\x61se\x18\x01 \x01(\x0b\x32 .cohesity.magneto.api.ResultBase\x12L\n\x06status\x18\x02 \x01(\x0e\x32<.cohesity.magneto.api.QueryExportMetadataStatusResult.Status\x12?\n\x0f\x65xport_location\x18\x03 \x01(\x0b\x32&.cohesity.magneto.api.DataLocatorProto\"%\n\x06Status\x12\x0c\n\x08kRunning\x10\x00\x12\r\n\tkFinished\x10\x01\"\x86\x01\n\x11ImportMetadataArg\x12\x30\n\x04\x62\x61se\x18\x01 \x01(\x0b\x32\".cohesity.magneto.api.ArgumentBase\x12?\n\x0fimport_location\x18\x02 \x01(\x0b\x32&.cohesity.magneto.api.DataLocatorProto\"c\n\x14ImportMetadataResult\x12.\n\x04\x62\x61se\x18\x01 \x01(\x0b\x32 .cohesity.magneto.api.ResultBase\x12\x1b\n\x13import_operation_id\x18\x02 \x01(\t\"m\n\x1cQueryImportMetadataStatusArg\x12\x30\n\x04\x62\x61se\x18\x01 \x01(\x0b\x32\".cohesity.magneto.api.ArgumentBase\x12\x1b\n\x13import_operation_id\x18\x02 \x01(\t\"\xc6\x01\n\x1fQueryImportMetadataStatusResult\x12.\n\x04\x62\x61se\x18\x01 \x01(\x0b\x32 .cohesity.magneto.api.ResultBase\x12L\n\x06status\x18\x02 \x01(\x0e\x32<.cohesity.magneto.api.QueryImportMetadataStatusResult.Status\"%\n\x06Status\x12\x0c\n\x08kRunning\x10\x00\x12\r\n\tkFinished\x10\x01\"s\n\"ValidateTenantMigrationMetadataArg\x12\x30\n\x04\x62\x61se\x18\x01 \x01(\x0b\x32\".cohesity.magneto.api.ArgumentBase\x12\x1b\n\x13import_operation_id\x18\x02 \x01(\t\"v\n%ValidateTenantMigrationMetadataResult\x12.\n\x04\x62\x61se\x18\x01 \x01(\x0b\x32 .cohesity.magneto.api.ResultBase\x12\x1d\n\x15validate_operation_id\x18\x02 \x01(\t\"z\n\'QueryTenantMigrationValidationStatusArg\x12\x30\n\x04\x62\x61se\x18\x01 \x01(\x0b\x32\".cohesity.magneto.api.ArgumentBase\x12\x1d\n\x15validate_operation_id\x18\x02 \x01(\t\"\x9d\x02\n*QueryTenantMigrationValidationStatusResult\x12.\n\x04\x62\x61se\x18\x01 \x01(\x0b\x32 .cohesity.magneto.api.ResultBase\x12W\n\x06status\x18\x02 \x01(\x0e\x32G.cohesity.magneto.api.QueryTenantMigrationValidationStatusResult.Status\x12?\n\x0freport_location\x18\x03 \x01(\x0b\x32&.cohesity.magneto.api.DataLocatorProto\"%\n\x06Status\x12\x0c\n\x08kRunning\x10\x00\x12\r\n\tkFinished\x10\x01\x42\x16Z\x14\x63ohesity/magneto/apib\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'magneto.api.magneto_external_debug_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\024cohesity/magneto/api'
  _globals['_GETSNAPSHOTLIVENESSINFORESULT_LIVENESSMAPENTRY']._loaded_options = None
  _globals['_GETSNAPSHOTLIVENESSINFORESULT_LIVENESSMAPENTRY']._serialized_options = b'8\001'
  _globals['_GETBACKUPRUNSINTERNALSTATERESULT_BACKUPRUNSMAPENTRY']._loaded_options = None
  _globals['_GETBACKUPRUNSINTERNALSTATERESULT_BACKUPRUNSMAPENTRY']._serialized_options = b'8\001'
  _globals['_GETSNAPSHOTLIVENESSINFOARG']._serialized_start=196
  _globals['_GETSNAPSHOTLIVENESSINFOARG']._serialized_end=431
  _globals['_OBJECTSNAPSHOTLIVENESSINFOPROTO']._serialized_start=434
  _globals['_OBJECTSNAPSHOTLIVENESSINFOPROTO']._serialized_end=1231
  _globals['_OBJECTSNAPSHOTLIVENESSINFOPROTO_SNAPSHOTINFO']._serialized_start=616
  _globals['_OBJECTSNAPSHOTLIVENESSINFOPROTO_SNAPSHOTINFO']._serialized_end=1231
  _globals['_OBJECTSNAPSHOTLIVENESSINFOPROTO_SNAPSHOTINFO_LOCALCOPYINFO']._serialized_start=828
  _globals['_OBJECTSNAPSHOTLIVENESSINFOPROTO_SNAPSHOTINFO_LOCALCOPYINFO']._serialized_end=891
  _globals['_OBJECTSNAPSHOTLIVENESSINFOPROTO_SNAPSHOTINFO_COPYINFO']._serialized_start=894
  _globals['_OBJECTSNAPSHOTLIVENESSINFOPROTO_SNAPSHOTINFO_COPYINFO']._serialized_end=1231
  _globals['_GETSNAPSHOTLIVENESSINFOPAGINATIONCOOKIE']._serialized_start=1233
  _globals['_GETSNAPSHOTLIVENESSINFOPAGINATIONCOOKIE']._serialized_end=1349
  _globals['_GETSNAPSHOTLIVENESSINFORESULT']._serialized_start=1352
  _globals['_GETSNAPSHOTLIVENESSINFORESULT']._serialized_end=1648
  _globals['_GETSNAPSHOTLIVENESSINFORESULT_LIVENESSMAPENTRY']._serialized_start=1543
  _globals['_GETSNAPSHOTLIVENESSINFORESULT_LIVENESSMAPENTRY']._serialized_end=1648
  _globals['_GETBACKUPRUNSINTERNALSTATEARG']._serialized_start=1651
  _globals['_GETBACKUPRUNSINTERNALSTATEARG']._serialized_end=1866
  _globals['_BACKUPRUNSINTERNALSTATEINFOPROTO']._serialized_start=1868
  _globals['_BACKUPRUNSINTERNALSTATEINFOPROTO']._serialized_end=1971
  _globals['_GETBACKUPRUNSINTERNALSTATERESULT']._serialized_start=1974
  _globals['_GETBACKUPRUNSINTERNALSTATERESULT']._serialized_end=2266
  _globals['_GETBACKUPRUNSINTERNALSTATERESULT_BACKUPRUNSMAPENTRY']._serialized_start=2158
  _globals['_GETBACKUPRUNSINTERNALSTATERESULT_BACKUPRUNSMAPENTRY']._serialized_end=2266
  _globals['_EXPORTMETADATAARG']._serialized_start=2269
  _globals['_EXPORTMETADATAARG']._serialized_end=2991
  _globals['_EXPORTMETADATAARG_METADATASELECTOR']._serialized_start=2563
  _globals['_EXPORTMETADATAARG_METADATASELECTOR']._serialized_end=2901
  _globals['_EXPORTMETADATAARG_LOCATION']._serialized_start=2903
  _globals['_EXPORTMETADATAARG_LOCATION']._serialized_end=2991
  _globals['_EXPORTMETADATARESULT']._serialized_start=2993
  _globals['_EXPORTMETADATARESULT']._serialized_end=3092
  _globals['_QUERYEXPORTMETADATASTATUSARG']._serialized_start=3094
  _globals['_QUERYEXPORTMETADATASTATUSARG']._serialized_end=3203
  _globals['_QUERYEXPORTMETADATASTATUSRESULT']._serialized_start=3206
  _globals['_QUERYEXPORTMETADATASTATUSRESULT']._serialized_end=3469
  _globals['_QUERYEXPORTMETADATASTATUSRESULT_STATUS']._serialized_start=3432
  _globals['_QUERYEXPORTMETADATASTATUSRESULT_STATUS']._serialized_end=3469
  _globals['_IMPORTMETADATAARG']._serialized_start=3472
  _globals['_IMPORTMETADATAARG']._serialized_end=3606
  _globals['_IMPORTMETADATARESULT']._serialized_start=3608
  _globals['_IMPORTMETADATARESULT']._serialized_end=3707
  _globals['_QUERYIMPORTMETADATASTATUSARG']._serialized_start=3709
  _globals['_QUERYIMPORTMETADATASTATUSARG']._serialized_end=3818
  _globals['_QUERYIMPORTMETADATASTATUSRESULT']._serialized_start=3821
  _globals['_QUERYIMPORTMETADATASTATUSRESULT']._serialized_end=4019
  _globals['_QUERYIMPORTMETADATASTATUSRESULT_STATUS']._serialized_start=3432
  _globals['_QUERYIMPORTMETADATASTATUSRESULT_STATUS']._serialized_end=3469
  _globals['_VALIDATETENANTMIGRATIONMETADATAARG']._serialized_start=4021
  _globals['_VALIDATETENANTMIGRATIONMETADATAARG']._serialized_end=4136
  _globals['_VALIDATETENANTMIGRATIONMETADATARESULT']._serialized_start=4138
  _globals['_VALIDATETENANTMIGRATIONMETADATARESULT']._serialized_end=4256
  _globals['_QUERYTENANTMIGRATIONVALIDATIONSTATUSARG']._serialized_start=4258
  _globals['_QUERYTENANTMIGRATIONVALIDATIONSTATUSARG']._serialized_end=4380
  _globals['_QUERYTENANTMIGRATIONVALIDATIONSTATUSRESULT']._serialized_start=4383
  _globals['_QUERYTENANTMIGRATIONVALIDATIONSTATUSRESULT']._serialized_end=4668
  _globals['_QUERYTENANTMIGRATIONVALIDATIONSTATUSRESULT_STATUS']._serialized_start=3432
  _globals['_QUERYTENANTMIGRATIONVALIDATIONSTATUSRESULT_STATUS']._serialized_end=3469
# @@protoc_insertion_point(module_scope)
