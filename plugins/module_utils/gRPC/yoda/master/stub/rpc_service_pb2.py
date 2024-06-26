# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yoda/master/stub/rpc_service.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from open_util.net import protorpc_pb2 as open__util_dot_net_dot_protorpc__pb2
from yoda.audit import cluster_audit_report_pb2 as yoda_dot_audit_dot_cluster__audit__report__pb2
from yoda.base import error_pb2 as yoda_dot_base_dot_error__pb2
from yoda.base import reports_pb2 as yoda_dot_base_dot_reports__pb2
from yoda.base import yoda_pb2 as yoda_dot_base_dot_yoda__pb2
from yoda.master.stub import yoda_rpc_args_pb2 as yoda_dot_master_dot_stub_dot_yoda__rpc__args__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\"yoda/master/stub/rpc_service.proto\x12\x19\x63ohesity.yoda.master.stub\x1a\x1copen_util/net/protorpc.proto\x1a%yoda/audit/cluster_audit_report.proto\x1a\x15yoda/base/error.proto\x1a\x17yoda/base/reports.proto\x1a\x14yoda/base/yoda.proto\x1a$yoda/master/stub/yoda_rpc_args.proto\"\xb4\x01\n\x12UpdateSlaveTaskArg\x12\x0f\n\x07task_id\x18\x01 \x02(\x03\x12\x16\n\x0e\x63onstituent_id\x18\x02 \x01(\x03\x12\x16\n\x0eincarnation_id\x18\x03 \x01(\x03\x12(\n\x05\x65rror\x18\x04 \x01(\x0b\x32\x19.cohesity.yoda.ErrorProto\x12)\n\x06report\x18\x05 \x01(\x0b\x32\x19.cohesity.yoda.YodaReport*\x08\x08\x64\x10\x80\x80\x80\x80\x02\"\x17\n\x15UpdateSlaveTaskResult\"\x96\x01\n\x1fUpdateLibrarianMigrationWorkArg\x12\x0f\n\x07task_id\x18\x01 \x02(\x03\x12\x16\n\x0e\x63onstituent_id\x18\x02 \x01(\x03\x12\x16\n\x0eincarnation_id\x18\x03 \x01(\x03\x12(\n\x05\x65rror\x18\x04 \x01(\x0b\x32\x19.cohesity.yoda.ErrorProto*\x08\x08\x64\x10\x80\x80\x80\x80\x02\"$\n\"UpdateLibrarianMigrationWorkResult\"\x8e\x01\n\x17UpdateSlaveAuditTaskArg\x12\x0f\n\x07task_id\x18\x01 \x02(\x03\x12\x16\n\x0e\x63onstituent_id\x18\x02 \x01(\x03\x12\x16\n\x0eincarnation_id\x18\x03 \x01(\x03\x12(\n\x05\x65rror\x18\x04 \x01(\x0b\x32\x19.cohesity.yoda.ErrorProto*\x08\x08\x64\x10\x80\x80\x80\x80\x02\"\x1c\n\x1aUpdateSlaveAuditTaskResult2\xdf\x1e\n\nRpcService\x12Z\n\x0b\x41\x64\x64Snapshot\x12\".cohesity.yoda.base.AddSnapshotArg\x1a%.cohesity.yoda.base.AddSnapshotResult\"\x00\x12{\n\x16UpdateSnapshotReplicas\x12-.cohesity.yoda.base.UpdateSnapshotReplicasArg\x1a\x30.cohesity.yoda.base.UpdateSnapshotReplicasResult\"\x00\x12\x98\x01\n\x1bGetMissingMigratedSnapshots\x12\x39.cohesity.yoda.master.stub.GetMissingMigratedSnapshotsArg\x1a<.cohesity.yoda.master.stub.GetMissingMigratedSnapshotsResult\"\x00\x12\x63\n\x0eRemoveSnapshot\x12%.cohesity.yoda.base.RemoveSnapshotArg\x1a(.cohesity.yoda.base.RemoveSnapshotResult\"\x00\x12~\n\x17RemoveVersionsFromIndex\x12..cohesity.yoda.base.RemoveVersionsFromIndexArg\x1a\x31.cohesity.yoda.base.RemoveVersionsFromIndexResult\"\x00\x12]\n\x0cRemoveObject\x12#.cohesity.yoda.base.RemoveObjectArg\x1a&.cohesity.yoda.base.RemoveObjectResult\"\x00\x12`\n\x0fGetVMVolumeInfo\x12#.cohesity.yoda.base.VMVolumeInfoArg\x1a&.cohesity.yoda.base.VMVolumeInfoResult\"\x00\x12\x84\x01\n\x19GetCrackedFileRestoreInfo\x12\x30.cohesity.yoda.base.GetCrackedFileRestoreInfoArg\x1a\x33.cohesity.yoda.base.GetCrackedFileRestoreInfoResult\"\x00\x12N\n\x07ReadDir\x12\x1e.cohesity.yoda.base.ReadDirArg\x1a!.cohesity.yoda.base.ReadDirResult\"\x00\x12Q\n\x08\x46ileStat\x12\x1f.cohesity.yoda.base.FileStatArg\x1a\".cohesity.yoda.base.FileStatResult\"\x00\x12\x8c\x01\n\x17PrepareCrackedFileIndex\x12\x35.cohesity.yoda.master.stub.PrepareCrackedFileIndexArg\x1a\x38.cohesity.yoda.master.stub.PrepareCrackedFileIndexResult\"\x00\x12\x80\x01\n\x13GetCrackedFileIndex\x12\x31.cohesity.yoda.master.stub.GetCrackedFileIndexArg\x1a\x34.cohesity.yoda.master.stub.GetCrackedFileIndexResult\"\x00\x12\x8c\x01\n\x17ReleaseCrackedFileIndex\x12\x35.cohesity.yoda.master.stub.ReleaseCrackedFileIndexArg\x1a\x38.cohesity.yoda.master.stub.ReleaseCrackedFileIndexResult\"\x00\x12\x95\x01\n\x1aPreparePutCrackedFileIndex\x12\x38.cohesity.yoda.master.stub.PreparePutCrackedFileIndexArg\x1a;.cohesity.yoda.master.stub.PreparePutCrackedFileIndexResult\"\x00\x12\x80\x01\n\x13PutCrackedFileIndex\x12\x31.cohesity.yoda.master.stub.PutCrackedFileIndexArg\x1a\x34.cohesity.yoda.master.stub.PutCrackedFileIndexResult\"\x00\x12\x95\x01\n\x1aReleasePutCrackedFileIndex\x12\x38.cohesity.yoda.master.stub.ReleasePutCrackedFileIndexArg\x1a;.cohesity.yoda.master.stub.ReleasePutCrackedFileIndexResult\"\x00\x12z\n\x15UpdateSlaveTaskStatus\x12-.cohesity.yoda.master.stub.UpdateSlaveTaskArg\x1a\x30.cohesity.yoda.master.stub.UpdateSlaveTaskResult\"\x00\x12\xa1\x01\n\"UpdateLibrarianMigrationWorkStatus\x12:.cohesity.yoda.master.stub.UpdateLibrarianMigrationWorkArg\x1a=.cohesity.yoda.master.stub.UpdateLibrarianMigrationWorkResult\"\x00\x12\x89\x01\n\x1aUpdateSlaveAuditTaskStatus\x12\x32.cohesity.yoda.master.stub.UpdateSlaveAuditTaskArg\x1a\x35.cohesity.yoda.master.stub.UpdateSlaveAuditTaskResult\"\x00\x12Q\n\nPingMaster\x12\x1f.cohesity.yoda.base.PingRequest\x1a .cohesity.yoda.base.PingResponse\"\x00\x12\x8c\x01\n\x1bGetClusterAccessAuditReport\x12\x33.cohesity.yoda.audit.GetClusterAccessAuditReportArg\x1a\x36.cohesity.yoda.audit.GetClusterAccessAuditReportResult\"\x00\x12\x9e\x01\n!GetClusterNotificationAuditReport\x12\x39.cohesity.yoda.audit.GetClusterNotificationAuditReportArg\x1a<.cohesity.yoda.audit.GetClusterNotificationAuditReportResult\"\x00\x12\x8d\x01\n\x1cGetCrackedFileIndexingStatus\x12\x33.cohesity.yoda.base.GetCrackedFileIndexingStatusArg\x1a\x36.cohesity.yoda.base.GetCrackedFileIndexingStatusResult\"\x00\x12i\n\x10\x45xtractFileRange\x12\'.cohesity.yoda.base.ExtractFileRangeArg\x1a*.cohesity.yoda.base.ExtractFileRangeResult\"\x00\x12\x81\x01\n\x18PrepareBulkFilesDownload\x12/.cohesity.yoda.base.PrepareBulkFilesDownloadArg\x1a\x32.cohesity.yoda.base.PrepareBulkFilesDownloadResult\"\x00\x12~\n\x17\x43\x61ncelBulkFilesDownload\x12..cohesity.yoda.base.CancelBulkFilesDownloadArg\x1a\x31.cohesity.yoda.base.CancelBulkFilesDownloadResult\"\x00\x12{\n\x16GetRecursiveFolderSize\x12-.cohesity.yoda.base.GetRecursiveFolderSizeArg\x1a\x30.cohesity.yoda.base.GetRecursiveFolderSizeResult\"\x00\x12T\n\tApplyTags\x12 .cohesity.yoda.base.ApplyTagsArg\x1a#.cohesity.yoda.base.ApplyTagsResult\"\x00\x12W\n\nRemoveTags\x12!.cohesity.yoda.base.RemoveTagsArg\x1a$.cohesity.yoda.base.RemoveTagsResult\"\x00\x12T\n\tCreateTag\x12 .cohesity.yoda.base.CreateTagArg\x1a#.cohesity.yoda.base.CreateTagResult\"\x00\x12T\n\tUpdateTag\x12 .cohesity.yoda.base.UpdateTagArg\x1a#.cohesity.yoda.base.UpdateTagResult\"\x00\x12T\n\tDeleteTag\x12 .cohesity.yoda.base.DeleteTagArg\x1a#.cohesity.yoda.base.DeleteTagResult\"\x00\x12N\n\x07GetTags\x12\x1e.cohesity.yoda.base.GetTagsArg\x1a!.cohesity.yoda.base.GetTagsResult\"\x00\x1a\r\x80\xf1\x04\x88\'\x88\xf1\x04\x01\x90\xf1\x04\x02\x42\x03\x80\x01\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yoda.master.stub.rpc_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\200\001\001'
  _globals['_RPCSERVICE']._loaded_options = None
  _globals['_RPCSERVICE']._serialized_options = b'\200\361\004\210\'\210\361\004\001\220\361\004\002'
  _globals['_UPDATESLAVETASKARG']._serialized_start=243
  _globals['_UPDATESLAVETASKARG']._serialized_end=423
  _globals['_UPDATESLAVETASKRESULT']._serialized_start=425
  _globals['_UPDATESLAVETASKRESULT']._serialized_end=448
  _globals['_UPDATELIBRARIANMIGRATIONWORKARG']._serialized_start=451
  _globals['_UPDATELIBRARIANMIGRATIONWORKARG']._serialized_end=601
  _globals['_UPDATELIBRARIANMIGRATIONWORKRESULT']._serialized_start=603
  _globals['_UPDATELIBRARIANMIGRATIONWORKRESULT']._serialized_end=639
  _globals['_UPDATESLAVEAUDITTASKARG']._serialized_start=642
  _globals['_UPDATESLAVEAUDITTASKARG']._serialized_end=784
  _globals['_UPDATESLAVEAUDITTASKRESULT']._serialized_start=786
  _globals['_UPDATESLAVEAUDITTASKRESULT']._serialized_end=814
  _globals['_RPCSERVICE']._serialized_start=817
  _globals['_RPCSERVICE']._serialized_end=4752
# @@protoc_insertion_point(module_scope)
