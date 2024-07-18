# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: magneto/agents/windows/stub/windows_apps_rpc.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from magneto.agents.windows.stub import windows_apps_param_pb2 as magneto_dot_agents_dot_windows_dot_stub_dot_windows__apps__param__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2magneto/agents/windows/stub/windows_apps_rpc.proto\x12$cohesity.magneto.agents.windows.stub\x1a\x34magneto/agents/windows/stub/windows_apps_param.proto2\xd7\x1d\n\x15WindowsAppsRpcService\x12\x96\x01\n\x13ReadBytesFromStream\x12<.cohesity.magneto.agents.windows.stub.ReadBytesFromStreamArg\x1a?.cohesity.magneto.agents.windows.stub.ReadBytesFromStreamResult\"\x00\x12\x93\x01\n\x12WriteBytesToStream\x12;.cohesity.magneto.agents.windows.stub.WriteBytesToStreamArg\x1a>.cohesity.magneto.agents.windows.stub.WriteBytesToStreamResult\"\x00\x12\x9c\x01\n\x15\x43ommitBytesFromStream\x12>.cohesity.magneto.agents.windows.stub.CommitBytesFromStreamArg\x1a\x41.cohesity.magneto.agents.windows.stub.CommitBytesFromStreamResult\"\x00\x12\x96\x01\n\x13\x43ommitBytesToStream\x12<.cohesity.magneto.agents.windows.stub.CommitBytesToStreamArg\x1a?.cohesity.magneto.agents.windows.stub.CommitBytesToStreamResult\"\x00\x12~\n\x0b\x43loseStream\x12\x34.cohesity.magneto.agents.windows.stub.CloseStreamArg\x1a\x37.cohesity.magneto.agents.windows.stub.CloseStreamResult\"\x00\x12\x84\x01\n\rUpdateJobInfo\x12\x36.cohesity.magneto.agents.windows.stub.UpdateJobInfoArg\x1a\x39.cohesity.magneto.agents.windows.stub.UpdateJobInfoResult\"\x00\x12\xa5\x01\n\x18VSSNotifyRestoreComplete\x12\x41.cohesity.magneto.agents.windows.stub.VSSNotifyRestoreCompleteArg\x1a\x44.cohesity.magneto.agents.windows.stub.VSSNotifyRestoreCompleteResult\"\x00\x12\x90\x01\n\x11\x44iscoverDatabases\x12:.cohesity.magneto.agents.windows.stub.DiscoverDatabasesArg\x1a=.cohesity.magneto.agents.windows.stub.DiscoverDatabasesResult\"\x00\x12\x9f\x01\n\x16QuerySQLBackupsetTable\x12?.cohesity.magneto.agents.windows.stub.QuerySQLBackupsetTableArg\x1a\x42.cohesity.magneto.agents.windows.stub.QuerySQLBackupsetTableResult\"\x00\x12\x99\x01\n\x14\x41\x62ortSQLVDIOperation\x12=.cohesity.magneto.agents.windows.stub.AbortSQLVDIOperationArg\x1a@.cohesity.magneto.agents.windows.stub.AbortSQLVDIOperationResult\"\x00\x12\x8d\x01\n\x10InitSQLLogBackup\x12\x39.cohesity.magneto.agents.windows.stub.InitSQLLogBackupArg\x1a<.cohesity.magneto.agents.windows.stub.InitSQLLogBackupResult\"\x00\x12\x8d\x01\n\x10InitSQLLogReplay\x12\x39.cohesity.magneto.agents.windows.stub.InitSQLLogReplayArg\x1a<.cohesity.magneto.agents.windows.stub.InitSQLLogReplayResult\"\x00\x12\xa5\x01\n\x18VSSGetSQLRestoreProgress\x12\x41.cohesity.magneto.agents.windows.stub.VSSGetSQLRestoreProgressArg\x1a\x44.cohesity.magneto.agents.windows.stub.VSSGetSQLRestoreProgressResult\"\x00\x12\x99\x01\n\x14\x45xecuteSQLStatements\x12=.cohesity.magneto.agents.windows.stub.ExecuteSQLStatementsArg\x1a@.cohesity.magneto.agents.windows.stub.ExecuteSQLStatementsResult\"\x00\x12\x93\x01\n\x12RevertAndAttachSQL\x12;.cohesity.magneto.agents.windows.stub.RevertAndAttachSQLArg\x1a>.cohesity.magneto.agents.windows.stub.RevertAndAttachSQLResult\"\x00\x12\x93\x01\n\x12\x44\x65tachSQLDatabases\x12;.cohesity.magneto.agents.windows.stub.DetachSQLDatabasesArg\x1a>.cohesity.magneto.agents.windows.stub.DetachSQLDatabasesResult\"\x00\x12\x99\x01\n\x14StartSQLNativeBackup\x12=.cohesity.magneto.agents.windows.stub.StartSQLNativeBackupArg\x1a@.cohesity.magneto.agents.windows.stub.StartSQLNativeBackupResult\"\x00\x12\x9c\x01\n\x15StartSQLNativeRestore\x12>.cohesity.magneto.agents.windows.stub.StartSQLNativeRestoreArg\x1a\x41.cohesity.magneto.agents.windows.stub.StartSQLNativeRestoreResult\"\x00\x12\xa2\x01\n\x17\x41\x62ortSQLNativeOperation\x12@.cohesity.magneto.agents.windows.stub.AbortSQLNativeOperationArg\x1a\x43.cohesity.magneto.agents.windows.stub.AbortSQLNativeOperationResult\"\x00\x12\xab\x01\n\x1aGetSQLNativeBackupProgress\x12\x43.cohesity.magneto.agents.windows.stub.GetSQLNativeBackupProgressArg\x1a\x46.cohesity.magneto.agents.windows.stub.GetSQLNativeBackupProgressResult\"\x00\x12\xae\x01\n\x1bGetSQLNativeRestoreProgress\x12\x44.cohesity.magneto.agents.windows.stub.GetSQLNativeRestoreProgressArg\x1aG.cohesity.magneto.agents.windows.stub.GetSQLNativeRestoreProgressResult\"\x00\x12\xa5\x01\n\x18\x43\x61ncelSQLNativeOperation\x12\x41.cohesity.magneto.agents.windows.stub.CancelSQLNativeOperationArg\x1a\x44.cohesity.magneto.agents.windows.stub.CancelSQLNativeOperationResult\"\x00\x12\xbd\x01\n NotifySQLNativeOperationComplete\x12I.cohesity.magneto.agents.windows.stub.NotifySQLNativeOperationCompleteArg\x1aL.cohesity.magneto.agents.windows.stub.NotifySQLNativeOperationCompleteResult\"\x00\x12\x9f\x01\n\x16GetSQLDatabaseFileInfo\x12?.cohesity.magneto.agents.windows.stub.GetSQLDatabaseFileInfoArg\x1a\x42.cohesity.magneto.agents.windows.stub.GetSQLDatabaseFileInfoResult\"\x00')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'magneto.agents.windows.stub.windows_apps_rpc_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_WINDOWSAPPSRPCSERVICE']._serialized_start=147
  _globals['_WINDOWSAPPSRPCSERVICE']._serialized_end=3946
# @@protoc_insertion_point(module_scope)