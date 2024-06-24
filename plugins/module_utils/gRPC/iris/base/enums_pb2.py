# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: iris/base/enums.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15iris/base/enums.proto\x12\x12\x63ohesity.iris.base*j\n\x12IrisVaultJobStatus\x12\x0f\n\x0bkJobRunning\x10\x01\x12\x11\n\rkJobSucceeded\x10\x02\x12\x0e\n\nkJobFailed\x10\x03\x12\x10\n\x0ckJobCanceled\x10\x04\x12\x0e\n\nkJobPaused\x10\x05*\xca \n\x10PrivilegeIdValue\x12\x12\n\x0ekPrincipalView\x10\x01\x12\x14\n\x10kPrincipalModify\x10\x02\x12\x0e\n\nkAppLaunch\x10\x03\x12\x13\n\x0fkAppsManagement\x10\x04\x12\x15\n\x11kOrganizationView\x10\x05\x12\x17\n\x13kOrganizationModify\x10\x06\x12\x1c\n\x18kOrganizationImpersonate\x10\x07\x12\x0e\n\nkCloneView\x10\x08\x12\x10\n\x0ckCloneModify\x10\t\x12\x10\n\x0ckClusterView\x10\n\x12\x12\n\x0ekClusterModify\x10\x0b\x12\x12\n\x0ekClusterCreate\x10\x0c\x12\x13\n\x0fkClusterSupport\x10\r\x12\x13\n\x0fkClusterUpgrade\x10\x0e\x12\x16\n\x12kClusterRemoteView\x10\x0f\x12\x18\n\x14kClusterRemoteModify\x10\x10\x12\x1e\n\x1akClusterExternalTargetView\x10\x11\x12 \n\x1ckClusterExternalTargetModify\x10\x12\x12\x11\n\rkClusterAudit\x10\x13\x12\x0e\n\nkAlertView\x10\x14\x12\x10\n\x0ckAlertModify\x10\x15\x12\r\n\tkVlanView\x10\x16\x12\x0f\n\x0bkVlanModify\x10\x17\x12\x17\n\x13kHybridExtenderView\x10\x18\x12\x1b\n\x17kHybridExtenderDownload\x10\x19\x12\x0f\n\x0bkAdLdapView\x10\x1a\x12\x11\n\rkAdLdapModify\x10\x1b\x12\x12\n\x0ekSchedulerView\x10\x1c\x12\x14\n\x10kSchedulerModify\x10\x1d\x12\x13\n\x0fkProtectionView\x10\x1e\x12\x15\n\x11kProtectionModify\x10\x1f\x12\x19\n\x15kProtectionJobOperate\x10 \x12\x1b\n\x17kProtectionSourceModify\x10!\x12\x19\n\x15kProtectionPolicyView\x10\"\x12\x1b\n\x17kProtectionPolicyModify\x10#\x12\x10\n\x0ckRestoreView\x10$\x12\x12\n\x0ekRestoreModify\x10%\x12\x14\n\x10kRestoreDownload\x10&\x12\x12\n\x0ekRemoteRestore\x10\'\x12\x10\n\x0ckStorageView\x10(\x12\x12\n\x0ekStorageModify\x10)\x12\x16\n\x12kStorageDomainView\x10*\x12\x18\n\x14kStorageDomainModify\x10+\x12\x12\n\x0ekAnalyticsView\x10,\x12\x14\n\x10kAnalyticsModify\x10-\x12\x10\n\x0ckReportsView\x10.\x12\x0e\n\nkMcmModify\x10/\x12\x11\n\rkDataSecurity\x10\x30\x12\x0e\n\nkSmbBackup\x10\x31\x12\x0f\n\x0bkSmbRestore\x10\x32\x12\x15\n\x11kSmbTakeOwnership\x10\x33\x12\x10\n\x0ckSmbAuditing\x10\x34\x12\x12\n\x0ekMcmUnregister\x10\x36\x12\x0f\n\x0bkMcmUpgrade\x10\x37\x12\x18\n\x14kMcmModifySuperAdmin\x10\x38\x12\x16\n\x12kMcmViewSuperAdmin\x10\x39\x12\x1b\n\x17kMcmModifyCohesityAdmin\x10:\x12\x19\n\x15kMcmViewCohesityAdmin\x10;\x12\x11\n\rkObjectSearch\x10<\x12#\n\x1fkFileDatalockExpiryTimeDecrease\x10=\x12\r\n\tkNodeView\x10>\x12\x14\n\x10kMcmObjectSearch\x10?\x12\x12\n\x0ekRunbookModify\x10@\x12\x11\n\rkKeystoneView\x10\x41\x12\x13\n\x0fkKeystoneModify\x10\x42\x12\x1e\n\x1akManageProtectionSourceAll\x10\x43\x12/\n+kManageProtectionSourceVmwareStandaloneHost\x10\x44\x12(\n$kManageProtectionSourceVmwareVcenter\x10\x45\x12/\n+kManageProtectionSourceVmwareVcloudDirector\x10\x46\x12,\n(kManageProtectionSourceHyperVScvmmServer\x10G\x12/\n+kManageProtectionSourceHyperVStandaloneHost\x10H\x12\x32\n.kManageProtectionSourceHyperVStandaloneCluster\x10I\x12\x35\n1kManageProtectionSourceAcropolisStandaloneCluster\x10J\x12<\n8kManageProtectionSourceAcropolisGenericStandaloneCluster\x10w\x12%\n!kManageProtectionSourceGcpIamUser\x10K\x12%\n!kManageProtectionSourceAwsIamUser\x10L\x12,\n(kManageProtectionSourceAzureSubscription\x10M\x12*\n&kManageProtectionSourceKvmOvirtManager\x10N\x12#\n\x1fkManageProtectionSourcePhysical\x10O\x12%\n!kManageProtectionSourceO365Domain\x10P\x12\x1e\n\x1akManageProtectionSourceSql\x10Q\x12!\n\x1dkManageProtectionSourceOracle\x10R\x12+\n\'kManageProtectionSourcePureStorageArray\x10S\x12-\n)kManageProtectionSourceNimbleStorageArray\x10T\x12*\n&kManageProtectionSourceHyperFlexServer\x10U\x12\x1d\n\x19kManageProtectionSourceAD\x10V\x12(\n$kManageProtectionSourceIsilonCluster\x10W\x12(\n$kManageProtectionSourceNetAppCluster\x10X\x12(\n$kManageProtectionSourceNetAppVServer\x10Y\x12)\n%kManageProtectionSourceGenericNasHost\x10Z\x12\x31\n-kManageProtectionSourceFlashbladeStorageArray\x10[\x12&\n\"kManageProtectionSourceGpfsCluster\x10\\\x12,\n(kManageProtectionSourceElastifileCluster\x10]\x12\x0c\n\x08kNisView\x10^\x12\x0e\n\nkNisModify\x10_\x12\x15\n\x11kMcmSimulatorView\x10`\x12\x17\n\x13kMcmSimulatorModify\x10\x61\x12#\n\x1fkManageProtectionSourceExchange\x10\x62\x12\'\n#kLinuxUserBashShellAccessDeprecated\x10\x63\x12\x18\n\x14kLinuxUserSudoAccess\x10\x64\x12$\n kManageProtectionSourceCassandra\x10\x65\x12\"\n\x1ekManageProtectionSourceMongoDB\x10\x66\x12$\n kManageProtectionSourceCouchbase\x10g\x12\x1f\n\x1bkManageProtectionSourceHdfs\x10h\x12 \n\x1ckManageProtectionSourceHbase\x10i\x12\x1f\n\x1bkManageProtectionSourceHive\x10j\x12%\n!kManageProtectionSourceKubernetes\x10k\x12\x1e\n\x1akManageBulkAgentInstallApp\x10l\x12\x17\n\x13kClusterMaintenance\x10m\x12\x12\n\x0ekAllowUiAccess\x10n\x12\x10\n\x0ckRunbookView\x10o\x12\x13\n\x0fkRunbookExecute\x10p\x12\x14\n\x10kBifrostVlanView\x10q\x12\x16\n\x12kBifrostVlanModify\x10r\x12\x11\n\rkApiKeyModify\x10s\x12\x0f\n\x0bkApiKeyView\x10t\x12\x11\n\rkKerberosView\x10u\x12\x13\n\x0fkKerberosModify\x10v\x12\r\n\tkTagsView\x10x\x12\x0f\n\x0bkTagsModify\x10y\x12\x0f\n\x0bkTagsManage\x10z\x12\x1e\n\x1akManageProtectionSourceUda\x10{\x12\x15\n\x11kAgentUpgradeView\x10|\x12\x17\n\x13kAgentUpgradeModify\x10}\x12\x11\n\rkManageS3Keys\x10~\x12\x14\n\x0fkMcmAccountView\x10\x82\x01\x12\x16\n\x11kMcmAccountModify\x10\x83\x01\x12\x1e\n\x19kProtectionDeleteSnapshot\x10\x84\x01\x12\x0f\n\nkMfaModify\x10\x85\x01\x12 \n\x1bkManageProtectionSourceSfdc\x10\x86\x01\x12\x18\n\x13kMcmRegionConfigure\x10\x87\x01\x12\x18\n\x13kManageSnapshotTags\x10\x88\x01\x12\x19\n\x14kRestoreSnapshotTags\x10\x89\x01\x12\x12\n\rkAuditLogView\x10\x8a\x01\x12\x14\n\x0fkAuditLogManage\x10\x8b\x01\x12\x19\n\x14kManageObservability\x10\x8c\x01\x12\x15\n\x10kGflagManagement\x10\x8d\x01\x12\x0f\n\nkDGaaSView\x10\x8e\x01\x12\x11\n\x0ckDGaaSModify\x10\x8f\x01\x12\x17\n\x12kRPaaSRegionModify\x10\x90\x01\x12\x0f\n\nkDRaaSView\x10\x91\x01\x12\x11\n\x0ckDRaaSModify\x10\x92\x01\x12\x14\n\x0fkHighClassified\x10\x93\x01\x12\x16\n\x11kBifrostRealmView\x10\x94\x01\x12\x18\n\x13kBifrostRealmModify\x10\x95\x01\x12\x19\n\x14kSecurityAdvisorView\x10\x96\x01\x12\x1b\n\x16kSecurityAdvisorModify\x10\x97\x01\x12\x1a\n\x15kSupportChannelModify\x10\x98\x01\x12\x15\n\x10kQuorumGroupView\x10\x99\x01\x12\x17\n\x12kQuorumGroupCreate\x10\x9a\x01\x12\x12\n\rkMcmModifyMfa\x10\x9b\x01\x12\x10\n\x0bkS3AbacView\x10\x9c\x01\x12\x12\n\rkS3AbacModify\x10\x9d\x01\x12\x0e\n\tkGaiaView\x10\xa7\x01\x12\x10\n\x0bkGaiaModify\x10\xa8\x01\"\x05\x08\x7f\x10\x81\x01*)\n\x0cMcmLoginType\x12\x0f\n\x0bkSalesforce\x10\x00\x12\x08\n\x04kSso\x10\x01*\xbf\x01\n\tRunStatus\x12\r\n\tkAccepted\x10\x00\x12\x0c\n\x08kRunning\x10\x01\x12\x0e\n\nkCanceling\x10\x02\x12\r\n\tkCanceled\x10\x03\x12\x0c\n\x08kSuccess\x10\x04\x12\x0c\n\x08kFailure\x10\x05\x12\x0c\n\x08kWarning\x10\x06\x12\x0b\n\x07kOnHold\x10\x07\x12\x0b\n\x07kMissed\x10\x08\x12\x0f\n\x0bkFinalizing\x10\t\x12\x13\n\x0fkWaitingToRetry\x10\n\x12\x0c\n\x08kSkipped\x10\x0b*a\n\x0eProtocolAccess\x12\x08\n\x04kAll\x10\x01\x12\x0c\n\x08kNFSOnly\x10\x02\x12\x0c\n\x08kSMBOnly\x10\x03\x12\x0b\n\x07kS3Only\x10\x04\x12\x0c\n\x08kUnknown\x10\x05\x12\x0e\n\nkSwiftOnly\x10\x06*%\n\x08TaskType\x12\r\n\tkRecovery\x10\x01\x12\n\n\x06kClone\x10\x02*S\n\x10\x43ompressionLevel\x12\x14\n\x10kCompressionNone\x10\x00\x12\x13\n\x0fkCompressionLow\x10\x01\x12\x14\n\x10kCompressionHigh\x10\x02*G\n\x12PasswordScoreProto\x12\t\n\x05kPoor\x10\x00\x12\t\n\x05kWeak\x10\x01\x12\x0b\n\x07kStrong\x10\x02\x12\x0e\n\nkExcellent\x10\x03*\xc6\x01\n\x08TileType\x12\x0f\n\x0bkHealthTile\x10\x01\x12\x10\n\x0ckJobRunsTile\x10\x02\x12\x13\n\x0fkRecoveriesTile\x10\x03\x12\x19\n\x15kProtectedObjectsTile\x10\x04\x12\x13\n\x0fkProtectionTile\x10\x05\x12\x12\n\x0ekAuditLogsTile\x10\x06\x12\r\n\tkIopsTile\x10\x07\x12\x13\n\x0fkThroughputTile\x10\x08\x12\x1a\n\x16kStorageEfficiencyTile\x10\t*T\n\x19UpdateProtectionJobAction\x12\n\n\x06kPause\x10\x01\x12\x0b\n\x07kResume\x10\x02\x12\r\n\tkActivate\x10\x03\x12\x0f\n\x0bkDeactivate\x10\x04*J\n\x0fRpoIntervalUnit\x12\x0b\n\x07kMinute\x10\x01\x12\t\n\x05kHour\x10\x02\x12\x08\n\x04kDay\x10\x03\x12\t\n\x05kWeek\x10\x04\x12\n\n\x06kMonth\x10\x05*6\n\x0b\x43lusterType\x12\r\n\tkPhysical\x10\x00\x12\x0c\n\x08kVirtual\x10\x01\x12\n\n\x06kCloud\x10\x02*\xb5\x04\n\x0cNexusOpError\x12\x0c\n\x08KNoError\x10\x00\x12\x1b\n\x17KSwPackageNotFoundError\x10\x01\x12\x19\n\x15KSwPackageExistsError\x10\x02\x12\x1a\n\x16KCurrNodeNotFoundError\x10\x03\x12\x17\n\x13KClusterExistsError\x10\x04\x12\x14\n\x10KNotClusterError\x10\x05\x12\x15\n\x11KNotFreeNodeError\x10\x06\x12\x19\n\x15KQueryParamParseError\x10\x07\x12\x14\n\x10KQueryParamEmpty\x10\x08\x12\x12\n\x0eKTimedoutError\x10\t\x12\x11\n\rKInvalidInput\x10\n\x12\x12\n\x0eKInternalError\x10\x0b\x12\x1a\n\x16KMethodNotAllowedError\x10\x0c\x12\x13\n\x0fKOpRunningError\x10\r\x12\x0f\n\x0bKRetryError\x10\x0e\x12\x15\n\x11KNodeNotReachable\x10\x0f\x12\x15\n\x11KNodeUnconfigured\x10\x10\x12\x13\n\x0fKNotImplemented\x10\x11\x12\x1b\n\x17KSwPackageNotCompatible\x10\x12\x12\x1a\n\x16KHardwareNotCompatible\x10\x13\x12\x1a\n\x16KFirmwareNotCompatible\x10\x14\x12\x19\n\x15KNodeHealthCheckError\x10\x15\x12\x1c\n\x18KNodeBeingAddedToCluster\x10\x16*!\n\x0c\x41uditLogType\x12\x11\n\rkNotification\x10\x00*{\n\x14NetworkInterfaceType\x12\x16\n\x12kPhysicalInterface\x10\x01\x12\x18\n\x14kBondMasterInterface\x10\x02\x12\x17\n\x13kBondSlaveInterface\x10\x03\x12\x18\n\x14kTaggedVlanInterface\x10\x04*}\n\x14InterfaceServiceType\x12\x17\n\x13kReplicationService\x10\x00\x12\x18\n\x14kRemoteTunnelService\x10\x01\x12\x17\n\x13kClusterDataService\x10\x02\x12\x19\n\x15kAvahiDiscoverService\x10\x03*1\n\x11InterfaceRoleType\x12\x0c\n\x08kPrimary\x10\x00\x12\x0e\n\nkSecondary\x10\x01*5\n\x12NetworkBondingMode\x12\x11\n\rkActiveBackup\x10\x01\x12\x0c\n\x08k802_3ad\x10\x04*;\n\x14\x43lusterServiceAction\x12\t\n\x05kStop\x10\x00\x12\n\n\x06kStart\x10\x01\x12\x0c\n\x08kRestart\x10\x02*W\n\x13\x43lusterServiceState\x12\x13\n\x0fkServiceStopped\x10\x00\x12\x13\n\x0fkServiceRunning\x10\x01\x12\x16\n\x12kServiceRestarting\x10\x02*\xee\t\n\x12\x43lusterServiceName\x12\x13\n\x0fkInvalidService\x10\x00\x12\x0b\n\x07kApollo\x10\x01\x12\x0b\n\x07kBridge\x10\x02\x12\n\n\x06kGenie\x10\x03\x12\x0f\n\x0bkGenieGofer\x10\x04\x12\x0c\n\x08kMagneto\x10\x05\x12\t\n\x05kIris\x10\x06\x12\x0e\n\nkIrisProxy\x10\x07\x12\x0e\n\nkNewScribe\x10\x08\x12\n\n\x06kStats\x10\t\x12\t\n\x05kYoda\x10\n\x12\x0b\n\x07kAlerts\x10\x0b\x12\r\n\tkKeychain\x10\x0c\x12\x0f\n\x0bkLogWatcher\x10\r\x12\x13\n\x0fkStatsCollector\x10\x0e\x12\x0c\n\x08kGandalf\x10\x0f\x12\n\n\x06kNexus\x10\x10\x12\x0f\n\x0bkNexusProxy\x10\x11\x12\x11\n\rkStorageProxy\x10\x12\x12\x0e\n\nkTricorder\x10\x13\x12\r\n\tkRtClient\x10\x14\x12\x0f\n\x0bkVaultProxy\x10\x15\x12\r\n\tkSmbProxy\x10\x16\x12\x10\n\x0ckBridgeProxy\x10\x17\x12\x0e\n\nkLibrarian\x10\x18\x12\n\n\x06kGroot\x10\x19\x12\x0f\n\x0bkEagleAgent\x10\x1a\x12\x0b\n\x07kAthena\x10\x1b\x12\x12\n\x0ekBifrostBroker\x10\x1c\x12\x0b\n\x07kElixir\x10\x1d\x12\x0c\n\x08kVulscan\x10\x1e\x12\r\n\tkPostgres\x10\x1f\x12\t\n\x05kAtom\x10 \x12\x0e\n\nkYodaAgent\x10!\x12\x0e\n\nkSmb2Proxy\x10\"\x12\x0e\n\nkThrottler\x10#\x12\n\n\x06kKafka\x10$\x12\r\n\tkEventing\x10%\x12\x11\n\rkAgentinstall\x10&\x12\x0b\n\x07kImanis\x10\'\x12\x0b\n\x07kElrond\x10(\x12\r\n\tkHeimdall\x10)\x12\x0c\n\x08kBifrost\x10*\x12\x0b\n\x07kIcebox\x10+\x12\x11\n\rkNodeExporter\x10,\x12\x0c\n\x08kCompass\x10-\x12\n\n\x06kPatch\x10.\x12\x0e\n\nkEtlServer\x10/\x12\r\n\tkUpgrader\x10\x30\x12\x10\n\x0ckTestservice\x10\x63\x12\x07\n\x03kOs\x10\x64\x12\n\n\x06kJanus\x10\x65\x12\n\n\x06kHcCli\x10\x66\x12\x08\n\x04kDlp\x10g\x12\x13\n\x0fkPushproxClient\x10h\x12\x0f\n\x0bkPushClient\x10i\x12\n\n\x06kAegis\x10j\x12\r\n\tkNfsProxy\x10k\x12\x18\n\x14kElixirWorkerservice\x10l\x12\r\n\tkArgusApp\x10m\x12\x14\n\x10kMetadataservice\x10n\x12\x10\n\x0ckSpireServer\x10o\x12\x0f\n\x0bkSpireAgent\x10p\x12\x14\n\x10kWorkqueueserver\x10q\x12\x12\n\x0ekElasticsearch\x10r\x12\x0e\n\nkLicensing\x10s\x12\t\n\x05kAxon\x10t\x12\x0b\n\x07kMagnus\x10u\x12\x0b\n\x07kOdsApp\x10v\x12\x17\n\x13kShelteredHarborApp\x10w\x12\x17\n\x13kShelteredHarborUda\x10x\x12\x0c\n\x08kCoredns\x10y\x12\x0f\n\x0bkCohesityCa\x10z\x12\x12\n\x0ekMetricsServer\x10{\x12\x12\n\x0ekInfraoperator\x10|\x12\x18\n\x14kMarketplaceoperator\x10}\x12\r\n\tkCohesion\x10~\x12\r\n\tkSpireApp\x10\x7f\x12\n\n\x05kGaia\x10\x80\x01*\x9d\x01\n\x0fViewStatsMetric\x12\x15\n\x11kSystemUsageBytes\x10\x01\x12\x17\n\x13kChunkBytesPhysical\x10\x02\x12\x14\n\x10kNumBytesWritten\x10\x03\x12\x11\n\rkNumBytesRead\x10\x04\x12\x17\n\x13kPeakReadThroughput\x10\x05\x12\x18\n\x14kPeakWriteThroughput\x10\x06*\x8b\x01\n\x12\x41uthenticationType\x12\x0e\n\nkAuthLocal\x10\x01\x12\x0b\n\x07kAuthAd\x10\x02\x12\x13\n\x0fkAuthSalesforce\x10\x03\x12\x0f\n\x0bkAuthGoogle\x10\x04\x12\x0c\n\x08kAuthSso\x10\x05\x12\x12\n\x0ekAuthMcmOnPrem\x10\x06\x12\x10\n\x0ckAuthService\x10\x07*j\n\x14PrincipalObjectClass\x12\n\n\x06kGroup\x10\x00\x12\t\n\x05kUser\x10\x01\x12\r\n\tkComputer\x10\x02\x12\x17\n\x13kWellKnownPrincipal\x10\x03\x12\x13\n\x0fkServiceAccount\x10\x04*(\n\x11QosPolicyPriority\x12\t\n\x05kHigh\x10\x01\x12\x08\n\x04kLow\x10\x02**\n\x07GroupBy\x12\x12\n\x0ekProtectionJob\x10\x01\x12\x0b\n\x07kTarget\x10\x02*m\n\x0c\x43onsumerType\x12\r\n\tkNoneType\x10\x01\x12\n\n\x06kViews\x10\x02\x12\x13\n\x0fkProtectionRuns\x10\x03\x12\x14\n\x10kReplicationRuns\x10\x04\x12\x17\n\x13kViewProtectionRuns\x10\x05*\xed\x04\n\x12ProtectionJobField\x12\x16\n\x12kProtectionJobName\x10\x01\x12\x1d\n\x19kProtectionJobDescription\x10\x02\x12\x19\n\x15kProtectionJobSources\x10\x03\x12\x1a\n\x16kProtectionJobSchedule\x10\x04\x12\x1e\n\x1akProtectionJobFullSchedule\x10\x05\x12\x1f\n\x1bkProtectionJobRetrySettings\x10\x06\x12!\n\x1dkProtectionJobRetentionPolicy\x10\x07\x12 \n\x1ckProtectionJobIndexingPolicy\x10\x08\x12 \n\x1ckProtectionJobAlertingPolicy\x10\t\x12\x1a\n\x16kProtectionJobPriority\x10\n\x12\x19\n\x15kProtectionJobQuiesce\x10\x0b\x12\x15\n\x11kProtectionJobSla\x10\x0c\x12\x1a\n\x16kProtectionJobPolicyId\x10\r\x12\x1a\n\x16kProtectionJobTimezone\x10\x0e\x12\"\n\x1ekProtectionJobFutureRunsPaused\x10\x0f\x12#\n\x1fkProtectionJobFutureRunsResumed\x10\x10\x12\x19\n\x15kSnapshotTargetPolicy\x10\x11\x12 \n\x1ckProtectionJobBlackoutWindow\x10\x12\x12\x15\n\x11kProtectionJobQOS\x10\x13\x12\x1e\n\x1akProtectionJobInvalidField\x10\x14*X\n\x10S3KeyMappingType\x12\x0b\n\x07kRandom\x10\x01\x12\n\n\x06kShort\x10\x02\x12\t\n\x05kLong\x10\x03\x12\x11\n\rkHierarchical\x10\x04\x12\r\n\tkObjectId\x10\x05*\xd6\x01\n\rNodeOperation\x12\x16\n\x12kNoActiveOperation\x10\x00\x12\x13\n\x0fkDestroyCluster\x10\x01\x12\x13\n\x0fkUpgradeCluster\x10\x02\x12\x13\n\x0fkRestartCluster\x10\x03\x12\x12\n\x0ekCreateCluster\x10\x04\x12\x12\n\x0ekExpandCluster\x10\x05\x12\x10\n\x0ckUpgradeNode\x10\x06\x12\x0f\n\x0bkRemoveNode\x10\x07\x12\r\n\tkAddDisks\x10\x08\x12\x14\n\x10kMarkDiskOffline\x10\t*[\n\x0cRemovalState\x12\x0e\n\nkNoRemoval\x10\x00\x12\x10\n\x0ckNodeRemoval\x10\x01\x12\x10\n\x0ckDiskRemoval\x10\x02\x12\x17\n\x13kNodeAndDiskRemoval\x10\x03*9\n\x13\x46\x61ultToleranceLevel\x12\t\n\x05kNode\x10\x00\x12\x0c\n\x08kChassis\x10\x01\x12\t\n\x05kRack\x10\x02*;\n\rNfsSquashType\x12\t\n\x05kNone\x10\x00\x12\x0f\n\x0bkRootSquash\x10\x01\x12\x0e\n\nkAllSquash\x10\x02*)\n\rMcmTenantType\x12\t\n\x05\x44maas\x10\x00\x12\x07\n\x03Mcm\x10\x03\"\x04\x08\x01\x10\x01*>\n\x13RecoveryProcessType\x12\x14\n\x10kInstantRecovery\x10\x00\x12\x11\n\rkCopyRecovery\x10\x01*l\n\rLockoutReason\x12\r\n\tNotLocked\x10\x00\x12\x17\n\x13\x46\x61iledLoginAttempts\x10\x01\x12\x11\n\rLockedByAdmin\x10\x02\x12\x0e\n\nInactivity\x10\x03\x12\x10\n\x0cOtherReasons\x10\x04*\"\n\x0bOtpCodeType\x12\x08\n\x04Totp\x10\x00\x12\t\n\x05\x45mail\x10\x01*@\n\x10\x43loudClusterSize\x12\t\n\x05Small\x10\x00\x12\n\n\x06Medium\x10\x01\x12\t\n\x05Large\x10\x02\x12\n\n\x06XLarge\x10\x03*V\n\x11MaintenanceStatus\x12\x14\n\x10UnderMaintenance\x10\x00\x12\x18\n\x14ScheduledMaintenance\x10\x01\x12\x11\n\rNotConfigured\x10\x02\x42\x14Z\x12iris/base/enums.pb')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'iris.base.enums_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\022iris/base/enums.pb'
  _globals['_IRISVAULTJOBSTATUS']._serialized_start=45
  _globals['_IRISVAULTJOBSTATUS']._serialized_end=151
  _globals['_PRIVILEGEIDVALUE']._serialized_start=154
  _globals['_PRIVILEGEIDVALUE']._serialized_end=4324
  _globals['_MCMLOGINTYPE']._serialized_start=4326
  _globals['_MCMLOGINTYPE']._serialized_end=4367
  _globals['_RUNSTATUS']._serialized_start=4370
  _globals['_RUNSTATUS']._serialized_end=4561
  _globals['_PROTOCOLACCESS']._serialized_start=4563
  _globals['_PROTOCOLACCESS']._serialized_end=4660
  _globals['_TASKTYPE']._serialized_start=4662
  _globals['_TASKTYPE']._serialized_end=4699
  _globals['_COMPRESSIONLEVEL']._serialized_start=4701
  _globals['_COMPRESSIONLEVEL']._serialized_end=4784
  _globals['_PASSWORDSCOREPROTO']._serialized_start=4786
  _globals['_PASSWORDSCOREPROTO']._serialized_end=4857
  _globals['_TILETYPE']._serialized_start=4860
  _globals['_TILETYPE']._serialized_end=5058
  _globals['_UPDATEPROTECTIONJOBACTION']._serialized_start=5060
  _globals['_UPDATEPROTECTIONJOBACTION']._serialized_end=5144
  _globals['_RPOINTERVALUNIT']._serialized_start=5146
  _globals['_RPOINTERVALUNIT']._serialized_end=5220
  _globals['_CLUSTERTYPE']._serialized_start=5222
  _globals['_CLUSTERTYPE']._serialized_end=5276
  _globals['_NEXUSOPERROR']._serialized_start=5279
  _globals['_NEXUSOPERROR']._serialized_end=5844
  _globals['_AUDITLOGTYPE']._serialized_start=5846
  _globals['_AUDITLOGTYPE']._serialized_end=5879
  _globals['_NETWORKINTERFACETYPE']._serialized_start=5881
  _globals['_NETWORKINTERFACETYPE']._serialized_end=6004
  _globals['_INTERFACESERVICETYPE']._serialized_start=6006
  _globals['_INTERFACESERVICETYPE']._serialized_end=6131
  _globals['_INTERFACEROLETYPE']._serialized_start=6133
  _globals['_INTERFACEROLETYPE']._serialized_end=6182
  _globals['_NETWORKBONDINGMODE']._serialized_start=6184
  _globals['_NETWORKBONDINGMODE']._serialized_end=6237
  _globals['_CLUSTERSERVICEACTION']._serialized_start=6239
  _globals['_CLUSTERSERVICEACTION']._serialized_end=6298
  _globals['_CLUSTERSERVICESTATE']._serialized_start=6300
  _globals['_CLUSTERSERVICESTATE']._serialized_end=6387
  _globals['_CLUSTERSERVICENAME']._serialized_start=6390
  _globals['_CLUSTERSERVICENAME']._serialized_end=7652
  _globals['_VIEWSTATSMETRIC']._serialized_start=7655
  _globals['_VIEWSTATSMETRIC']._serialized_end=7812
  _globals['_AUTHENTICATIONTYPE']._serialized_start=7815
  _globals['_AUTHENTICATIONTYPE']._serialized_end=7954
  _globals['_PRINCIPALOBJECTCLASS']._serialized_start=7956
  _globals['_PRINCIPALOBJECTCLASS']._serialized_end=8062
  _globals['_QOSPOLICYPRIORITY']._serialized_start=8064
  _globals['_QOSPOLICYPRIORITY']._serialized_end=8104
  _globals['_GROUPBY']._serialized_start=8106
  _globals['_GROUPBY']._serialized_end=8148
  _globals['_CONSUMERTYPE']._serialized_start=8150
  _globals['_CONSUMERTYPE']._serialized_end=8259
  _globals['_PROTECTIONJOBFIELD']._serialized_start=8262
  _globals['_PROTECTIONJOBFIELD']._serialized_end=8883
  _globals['_S3KEYMAPPINGTYPE']._serialized_start=8885
  _globals['_S3KEYMAPPINGTYPE']._serialized_end=8973
  _globals['_NODEOPERATION']._serialized_start=8976
  _globals['_NODEOPERATION']._serialized_end=9190
  _globals['_REMOVALSTATE']._serialized_start=9192
  _globals['_REMOVALSTATE']._serialized_end=9283
  _globals['_FAULTTOLERANCELEVEL']._serialized_start=9285
  _globals['_FAULTTOLERANCELEVEL']._serialized_end=9342
  _globals['_NFSSQUASHTYPE']._serialized_start=9344
  _globals['_NFSSQUASHTYPE']._serialized_end=9403
  _globals['_MCMTENANTTYPE']._serialized_start=9405
  _globals['_MCMTENANTTYPE']._serialized_end=9446
  _globals['_RECOVERYPROCESSTYPE']._serialized_start=9448
  _globals['_RECOVERYPROCESSTYPE']._serialized_end=9510
  _globals['_LOCKOUTREASON']._serialized_start=9512
  _globals['_LOCKOUTREASON']._serialized_end=9620
  _globals['_OTPCODETYPE']._serialized_start=9622
  _globals['_OTPCODETYPE']._serialized_end=9656
  _globals['_CLOUDCLUSTERSIZE']._serialized_start=9658
  _globals['_CLOUDCLUSTERSIZE']._serialized_end=9722
  _globals['_MAINTENANCESTATUS']._serialized_start=9724
  _globals['_MAINTENANCESTATUS']._serialized_end=9810
# @@protoc_insertion_point(module_scope)
