from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class IrisVaultJobStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kJobRunning: _ClassVar[IrisVaultJobStatus]
    kJobSucceeded: _ClassVar[IrisVaultJobStatus]
    kJobFailed: _ClassVar[IrisVaultJobStatus]
    kJobCanceled: _ClassVar[IrisVaultJobStatus]
    kJobPaused: _ClassVar[IrisVaultJobStatus]

class PrivilegeIdValue(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kPrincipalView: _ClassVar[PrivilegeIdValue]
    kPrincipalModify: _ClassVar[PrivilegeIdValue]
    kAppLaunch: _ClassVar[PrivilegeIdValue]
    kAppsManagement: _ClassVar[PrivilegeIdValue]
    kOrganizationView: _ClassVar[PrivilegeIdValue]
    kOrganizationModify: _ClassVar[PrivilegeIdValue]
    kOrganizationImpersonate: _ClassVar[PrivilegeIdValue]
    kCloneView: _ClassVar[PrivilegeIdValue]
    kCloneModify: _ClassVar[PrivilegeIdValue]
    kClusterView: _ClassVar[PrivilegeIdValue]
    kClusterModify: _ClassVar[PrivilegeIdValue]
    kClusterCreate: _ClassVar[PrivilegeIdValue]
    kClusterSupport: _ClassVar[PrivilegeIdValue]
    kClusterUpgrade: _ClassVar[PrivilegeIdValue]
    kClusterRemoteView: _ClassVar[PrivilegeIdValue]
    kClusterRemoteModify: _ClassVar[PrivilegeIdValue]
    kClusterExternalTargetView: _ClassVar[PrivilegeIdValue]
    kClusterExternalTargetModify: _ClassVar[PrivilegeIdValue]
    kClusterAudit: _ClassVar[PrivilegeIdValue]
    kAlertView: _ClassVar[PrivilegeIdValue]
    kAlertModify: _ClassVar[PrivilegeIdValue]
    kVlanView: _ClassVar[PrivilegeIdValue]
    kVlanModify: _ClassVar[PrivilegeIdValue]
    kHybridExtenderView: _ClassVar[PrivilegeIdValue]
    kHybridExtenderDownload: _ClassVar[PrivilegeIdValue]
    kAdLdapView: _ClassVar[PrivilegeIdValue]
    kAdLdapModify: _ClassVar[PrivilegeIdValue]
    kSchedulerView: _ClassVar[PrivilegeIdValue]
    kSchedulerModify: _ClassVar[PrivilegeIdValue]
    kProtectionView: _ClassVar[PrivilegeIdValue]
    kProtectionModify: _ClassVar[PrivilegeIdValue]
    kProtectionJobOperate: _ClassVar[PrivilegeIdValue]
    kProtectionSourceModify: _ClassVar[PrivilegeIdValue]
    kProtectionPolicyView: _ClassVar[PrivilegeIdValue]
    kProtectionPolicyModify: _ClassVar[PrivilegeIdValue]
    kRestoreView: _ClassVar[PrivilegeIdValue]
    kRestoreModify: _ClassVar[PrivilegeIdValue]
    kRestoreDownload: _ClassVar[PrivilegeIdValue]
    kRemoteRestore: _ClassVar[PrivilegeIdValue]
    kStorageView: _ClassVar[PrivilegeIdValue]
    kStorageModify: _ClassVar[PrivilegeIdValue]
    kStorageDomainView: _ClassVar[PrivilegeIdValue]
    kStorageDomainModify: _ClassVar[PrivilegeIdValue]
    kAnalyticsView: _ClassVar[PrivilegeIdValue]
    kAnalyticsModify: _ClassVar[PrivilegeIdValue]
    kReportsView: _ClassVar[PrivilegeIdValue]
    kMcmModify: _ClassVar[PrivilegeIdValue]
    kDataSecurity: _ClassVar[PrivilegeIdValue]
    kSmbBackup: _ClassVar[PrivilegeIdValue]
    kSmbRestore: _ClassVar[PrivilegeIdValue]
    kSmbTakeOwnership: _ClassVar[PrivilegeIdValue]
    kSmbAuditing: _ClassVar[PrivilegeIdValue]
    kMcmUnregister: _ClassVar[PrivilegeIdValue]
    kMcmUpgrade: _ClassVar[PrivilegeIdValue]
    kMcmModifySuperAdmin: _ClassVar[PrivilegeIdValue]
    kMcmViewSuperAdmin: _ClassVar[PrivilegeIdValue]
    kMcmModifyCohesityAdmin: _ClassVar[PrivilegeIdValue]
    kMcmViewCohesityAdmin: _ClassVar[PrivilegeIdValue]
    kObjectSearch: _ClassVar[PrivilegeIdValue]
    kFileDatalockExpiryTimeDecrease: _ClassVar[PrivilegeIdValue]
    kNodeView: _ClassVar[PrivilegeIdValue]
    kMcmObjectSearch: _ClassVar[PrivilegeIdValue]
    kRunbookModify: _ClassVar[PrivilegeIdValue]
    kKeystoneView: _ClassVar[PrivilegeIdValue]
    kKeystoneModify: _ClassVar[PrivilegeIdValue]
    kManageProtectionSourceAll: _ClassVar[PrivilegeIdValue]
    kManageProtectionSourceVmwareStandaloneHost: _ClassVar[PrivilegeIdValue]
    kManageProtectionSourceVmwareVcenter: _ClassVar[PrivilegeIdValue]
    kManageProtectionSourceVmwareVcloudDirector: _ClassVar[PrivilegeIdValue]
    kManageProtectionSourceHyperVScvmmServer: _ClassVar[PrivilegeIdValue]
    kManageProtectionSourceHyperVStandaloneHost: _ClassVar[PrivilegeIdValue]
    kManageProtectionSourceHyperVStandaloneCluster: _ClassVar[PrivilegeIdValue]
    kManageProtectionSourceAcropolisStandaloneCluster: _ClassVar[PrivilegeIdValue]
    kManageProtectionSourceAcropolisGenericStandaloneCluster: _ClassVar[PrivilegeIdValue]
    kManageProtectionSourceGcpIamUser: _ClassVar[PrivilegeIdValue]
    kManageProtectionSourceAwsIamUser: _ClassVar[PrivilegeIdValue]
    kManageProtectionSourceAzureSubscription: _ClassVar[PrivilegeIdValue]
    kManageProtectionSourceKvmOvirtManager: _ClassVar[PrivilegeIdValue]
    kManageProtectionSourcePhysical: _ClassVar[PrivilegeIdValue]
    kManageProtectionSourceO365Domain: _ClassVar[PrivilegeIdValue]
    kManageProtectionSourceSql: _ClassVar[PrivilegeIdValue]
    kManageProtectionSourceOracle: _ClassVar[PrivilegeIdValue]
    kManageProtectionSourcePureStorageArray: _ClassVar[PrivilegeIdValue]
    kManageProtectionSourceNimbleStorageArray: _ClassVar[PrivilegeIdValue]
    kManageProtectionSourceHyperFlexServer: _ClassVar[PrivilegeIdValue]
    kManageProtectionSourceAD: _ClassVar[PrivilegeIdValue]
    kManageProtectionSourceIsilonCluster: _ClassVar[PrivilegeIdValue]
    kManageProtectionSourceNetAppCluster: _ClassVar[PrivilegeIdValue]
    kManageProtectionSourceNetAppVServer: _ClassVar[PrivilegeIdValue]
    kManageProtectionSourceGenericNasHost: _ClassVar[PrivilegeIdValue]
    kManageProtectionSourceFlashbladeStorageArray: _ClassVar[PrivilegeIdValue]
    kManageProtectionSourceGpfsCluster: _ClassVar[PrivilegeIdValue]
    kManageProtectionSourceElastifileCluster: _ClassVar[PrivilegeIdValue]
    kNisView: _ClassVar[PrivilegeIdValue]
    kNisModify: _ClassVar[PrivilegeIdValue]
    kMcmSimulatorView: _ClassVar[PrivilegeIdValue]
    kMcmSimulatorModify: _ClassVar[PrivilegeIdValue]
    kManageProtectionSourceExchange: _ClassVar[PrivilegeIdValue]
    kLinuxUserBashShellAccessDeprecated: _ClassVar[PrivilegeIdValue]
    kLinuxUserSudoAccess: _ClassVar[PrivilegeIdValue]
    kManageProtectionSourceCassandra: _ClassVar[PrivilegeIdValue]
    kManageProtectionSourceMongoDB: _ClassVar[PrivilegeIdValue]
    kManageProtectionSourceCouchbase: _ClassVar[PrivilegeIdValue]
    kManageProtectionSourceHdfs: _ClassVar[PrivilegeIdValue]
    kManageProtectionSourceHbase: _ClassVar[PrivilegeIdValue]
    kManageProtectionSourceHive: _ClassVar[PrivilegeIdValue]
    kManageProtectionSourceKubernetes: _ClassVar[PrivilegeIdValue]
    kManageBulkAgentInstallApp: _ClassVar[PrivilegeIdValue]
    kClusterMaintenance: _ClassVar[PrivilegeIdValue]
    kAllowUiAccess: _ClassVar[PrivilegeIdValue]
    kRunbookView: _ClassVar[PrivilegeIdValue]
    kRunbookExecute: _ClassVar[PrivilegeIdValue]
    kBifrostVlanView: _ClassVar[PrivilegeIdValue]
    kBifrostVlanModify: _ClassVar[PrivilegeIdValue]
    kApiKeyModify: _ClassVar[PrivilegeIdValue]
    kApiKeyView: _ClassVar[PrivilegeIdValue]
    kKerberosView: _ClassVar[PrivilegeIdValue]
    kKerberosModify: _ClassVar[PrivilegeIdValue]
    kTagsView: _ClassVar[PrivilegeIdValue]
    kTagsModify: _ClassVar[PrivilegeIdValue]
    kTagsManage: _ClassVar[PrivilegeIdValue]
    kManageProtectionSourceUda: _ClassVar[PrivilegeIdValue]
    kAgentUpgradeView: _ClassVar[PrivilegeIdValue]
    kAgentUpgradeModify: _ClassVar[PrivilegeIdValue]
    kManageS3Keys: _ClassVar[PrivilegeIdValue]
    kMcmAccountView: _ClassVar[PrivilegeIdValue]
    kMcmAccountModify: _ClassVar[PrivilegeIdValue]
    kProtectionDeleteSnapshot: _ClassVar[PrivilegeIdValue]
    kMfaModify: _ClassVar[PrivilegeIdValue]
    kManageProtectionSourceSfdc: _ClassVar[PrivilegeIdValue]
    kMcmRegionConfigure: _ClassVar[PrivilegeIdValue]
    kManageSnapshotTags: _ClassVar[PrivilegeIdValue]
    kRestoreSnapshotTags: _ClassVar[PrivilegeIdValue]
    kAuditLogView: _ClassVar[PrivilegeIdValue]
    kAuditLogManage: _ClassVar[PrivilegeIdValue]
    kManageObservability: _ClassVar[PrivilegeIdValue]
    kGflagManagement: _ClassVar[PrivilegeIdValue]
    kDGaaSView: _ClassVar[PrivilegeIdValue]
    kDGaaSModify: _ClassVar[PrivilegeIdValue]
    kRPaaSRegionModify: _ClassVar[PrivilegeIdValue]
    kDRaaSView: _ClassVar[PrivilegeIdValue]
    kDRaaSModify: _ClassVar[PrivilegeIdValue]
    kHighClassified: _ClassVar[PrivilegeIdValue]
    kBifrostRealmView: _ClassVar[PrivilegeIdValue]
    kBifrostRealmModify: _ClassVar[PrivilegeIdValue]
    kSecurityAdvisorView: _ClassVar[PrivilegeIdValue]
    kSecurityAdvisorModify: _ClassVar[PrivilegeIdValue]
    kSupportChannelModify: _ClassVar[PrivilegeIdValue]
    kQuorumGroupView: _ClassVar[PrivilegeIdValue]
    kQuorumGroupCreate: _ClassVar[PrivilegeIdValue]
    kMcmModifyMfa: _ClassVar[PrivilegeIdValue]
    kS3AbacView: _ClassVar[PrivilegeIdValue]
    kS3AbacModify: _ClassVar[PrivilegeIdValue]
    kGaiaView: _ClassVar[PrivilegeIdValue]
    kGaiaModify: _ClassVar[PrivilegeIdValue]

class McmLoginType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kSalesforce: _ClassVar[McmLoginType]
    kSso: _ClassVar[McmLoginType]

class RunStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kAccepted: _ClassVar[RunStatus]
    kRunning: _ClassVar[RunStatus]
    kCanceling: _ClassVar[RunStatus]
    kCanceled: _ClassVar[RunStatus]
    kSuccess: _ClassVar[RunStatus]
    kFailure: _ClassVar[RunStatus]
    kWarning: _ClassVar[RunStatus]
    kOnHold: _ClassVar[RunStatus]
    kMissed: _ClassVar[RunStatus]
    kFinalizing: _ClassVar[RunStatus]
    kWaitingToRetry: _ClassVar[RunStatus]
    kSkipped: _ClassVar[RunStatus]

class ProtocolAccess(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kAll: _ClassVar[ProtocolAccess]
    kNFSOnly: _ClassVar[ProtocolAccess]
    kSMBOnly: _ClassVar[ProtocolAccess]
    kS3Only: _ClassVar[ProtocolAccess]
    kUnknown: _ClassVar[ProtocolAccess]
    kSwiftOnly: _ClassVar[ProtocolAccess]

class TaskType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kRecovery: _ClassVar[TaskType]
    kClone: _ClassVar[TaskType]

class CompressionLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kCompressionNone: _ClassVar[CompressionLevel]
    kCompressionLow: _ClassVar[CompressionLevel]
    kCompressionHigh: _ClassVar[CompressionLevel]

class PasswordScoreProto(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kPoor: _ClassVar[PasswordScoreProto]
    kWeak: _ClassVar[PasswordScoreProto]
    kStrong: _ClassVar[PasswordScoreProto]
    kExcellent: _ClassVar[PasswordScoreProto]

class TileType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kHealthTile: _ClassVar[TileType]
    kJobRunsTile: _ClassVar[TileType]
    kRecoveriesTile: _ClassVar[TileType]
    kProtectedObjectsTile: _ClassVar[TileType]
    kProtectionTile: _ClassVar[TileType]
    kAuditLogsTile: _ClassVar[TileType]
    kIopsTile: _ClassVar[TileType]
    kThroughputTile: _ClassVar[TileType]
    kStorageEfficiencyTile: _ClassVar[TileType]

class UpdateProtectionJobAction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kPause: _ClassVar[UpdateProtectionJobAction]
    kResume: _ClassVar[UpdateProtectionJobAction]
    kActivate: _ClassVar[UpdateProtectionJobAction]
    kDeactivate: _ClassVar[UpdateProtectionJobAction]

class RpoIntervalUnit(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kMinute: _ClassVar[RpoIntervalUnit]
    kHour: _ClassVar[RpoIntervalUnit]
    kDay: _ClassVar[RpoIntervalUnit]
    kWeek: _ClassVar[RpoIntervalUnit]
    kMonth: _ClassVar[RpoIntervalUnit]

class ClusterType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kPhysical: _ClassVar[ClusterType]
    kVirtual: _ClassVar[ClusterType]
    kCloud: _ClassVar[ClusterType]

class NexusOpError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    KNoError: _ClassVar[NexusOpError]
    KSwPackageNotFoundError: _ClassVar[NexusOpError]
    KSwPackageExistsError: _ClassVar[NexusOpError]
    KCurrNodeNotFoundError: _ClassVar[NexusOpError]
    KClusterExistsError: _ClassVar[NexusOpError]
    KNotClusterError: _ClassVar[NexusOpError]
    KNotFreeNodeError: _ClassVar[NexusOpError]
    KQueryParamParseError: _ClassVar[NexusOpError]
    KQueryParamEmpty: _ClassVar[NexusOpError]
    KTimedoutError: _ClassVar[NexusOpError]
    KInvalidInput: _ClassVar[NexusOpError]
    KInternalError: _ClassVar[NexusOpError]
    KMethodNotAllowedError: _ClassVar[NexusOpError]
    KOpRunningError: _ClassVar[NexusOpError]
    KRetryError: _ClassVar[NexusOpError]
    KNodeNotReachable: _ClassVar[NexusOpError]
    KNodeUnconfigured: _ClassVar[NexusOpError]
    KNotImplemented: _ClassVar[NexusOpError]
    KSwPackageNotCompatible: _ClassVar[NexusOpError]
    KHardwareNotCompatible: _ClassVar[NexusOpError]
    KFirmwareNotCompatible: _ClassVar[NexusOpError]
    KNodeHealthCheckError: _ClassVar[NexusOpError]
    KNodeBeingAddedToCluster: _ClassVar[NexusOpError]

class AuditLogType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kNotification: _ClassVar[AuditLogType]

class NetworkInterfaceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kPhysicalInterface: _ClassVar[NetworkInterfaceType]
    kBondMasterInterface: _ClassVar[NetworkInterfaceType]
    kBondSlaveInterface: _ClassVar[NetworkInterfaceType]
    kTaggedVlanInterface: _ClassVar[NetworkInterfaceType]

class InterfaceServiceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kReplicationService: _ClassVar[InterfaceServiceType]
    kRemoteTunnelService: _ClassVar[InterfaceServiceType]
    kClusterDataService: _ClassVar[InterfaceServiceType]
    kAvahiDiscoverService: _ClassVar[InterfaceServiceType]

class InterfaceRoleType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kPrimary: _ClassVar[InterfaceRoleType]
    kSecondary: _ClassVar[InterfaceRoleType]

class NetworkBondingMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kActiveBackup: _ClassVar[NetworkBondingMode]
    k802_3ad: _ClassVar[NetworkBondingMode]

class ClusterServiceAction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kStop: _ClassVar[ClusterServiceAction]
    kStart: _ClassVar[ClusterServiceAction]
    kRestart: _ClassVar[ClusterServiceAction]

class ClusterServiceState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kServiceStopped: _ClassVar[ClusterServiceState]
    kServiceRunning: _ClassVar[ClusterServiceState]
    kServiceRestarting: _ClassVar[ClusterServiceState]

class ClusterServiceName(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kInvalidService: _ClassVar[ClusterServiceName]
    kApollo: _ClassVar[ClusterServiceName]
    kBridge: _ClassVar[ClusterServiceName]
    kGenie: _ClassVar[ClusterServiceName]
    kGenieGofer: _ClassVar[ClusterServiceName]
    kMagneto: _ClassVar[ClusterServiceName]
    kIris: _ClassVar[ClusterServiceName]
    kIrisProxy: _ClassVar[ClusterServiceName]
    kNewScribe: _ClassVar[ClusterServiceName]
    kStats: _ClassVar[ClusterServiceName]
    kYoda: _ClassVar[ClusterServiceName]
    kAlerts: _ClassVar[ClusterServiceName]
    kKeychain: _ClassVar[ClusterServiceName]
    kLogWatcher: _ClassVar[ClusterServiceName]
    kStatsCollector: _ClassVar[ClusterServiceName]
    kGandalf: _ClassVar[ClusterServiceName]
    kNexus: _ClassVar[ClusterServiceName]
    kNexusProxy: _ClassVar[ClusterServiceName]
    kStorageProxy: _ClassVar[ClusterServiceName]
    kTricorder: _ClassVar[ClusterServiceName]
    kRtClient: _ClassVar[ClusterServiceName]
    kVaultProxy: _ClassVar[ClusterServiceName]
    kSmbProxy: _ClassVar[ClusterServiceName]
    kBridgeProxy: _ClassVar[ClusterServiceName]
    kLibrarian: _ClassVar[ClusterServiceName]
    kGroot: _ClassVar[ClusterServiceName]
    kEagleAgent: _ClassVar[ClusterServiceName]
    kAthena: _ClassVar[ClusterServiceName]
    kBifrostBroker: _ClassVar[ClusterServiceName]
    kElixir: _ClassVar[ClusterServiceName]
    kVulscan: _ClassVar[ClusterServiceName]
    kPostgres: _ClassVar[ClusterServiceName]
    kAtom: _ClassVar[ClusterServiceName]
    kYodaAgent: _ClassVar[ClusterServiceName]
    kSmb2Proxy: _ClassVar[ClusterServiceName]
    kThrottler: _ClassVar[ClusterServiceName]
    kKafka: _ClassVar[ClusterServiceName]
    kEventing: _ClassVar[ClusterServiceName]
    kAgentinstall: _ClassVar[ClusterServiceName]
    kImanis: _ClassVar[ClusterServiceName]
    kElrond: _ClassVar[ClusterServiceName]
    kHeimdall: _ClassVar[ClusterServiceName]
    kBifrost: _ClassVar[ClusterServiceName]
    kIcebox: _ClassVar[ClusterServiceName]
    kNodeExporter: _ClassVar[ClusterServiceName]
    kCompass: _ClassVar[ClusterServiceName]
    kPatch: _ClassVar[ClusterServiceName]
    kEtlServer: _ClassVar[ClusterServiceName]
    kUpgrader: _ClassVar[ClusterServiceName]
    kTestservice: _ClassVar[ClusterServiceName]
    kOs: _ClassVar[ClusterServiceName]
    kJanus: _ClassVar[ClusterServiceName]
    kHcCli: _ClassVar[ClusterServiceName]
    kDlp: _ClassVar[ClusterServiceName]
    kPushproxClient: _ClassVar[ClusterServiceName]
    kPushClient: _ClassVar[ClusterServiceName]
    kAegis: _ClassVar[ClusterServiceName]
    kNfsProxy: _ClassVar[ClusterServiceName]
    kElixirWorkerservice: _ClassVar[ClusterServiceName]
    kArgusApp: _ClassVar[ClusterServiceName]
    kMetadataservice: _ClassVar[ClusterServiceName]
    kSpireServer: _ClassVar[ClusterServiceName]
    kSpireAgent: _ClassVar[ClusterServiceName]
    kWorkqueueserver: _ClassVar[ClusterServiceName]
    kElasticsearch: _ClassVar[ClusterServiceName]
    kLicensing: _ClassVar[ClusterServiceName]
    kAxon: _ClassVar[ClusterServiceName]
    kMagnus: _ClassVar[ClusterServiceName]
    kOdsApp: _ClassVar[ClusterServiceName]
    kShelteredHarborApp: _ClassVar[ClusterServiceName]
    kShelteredHarborUda: _ClassVar[ClusterServiceName]
    kCoredns: _ClassVar[ClusterServiceName]
    kCohesityCa: _ClassVar[ClusterServiceName]
    kMetricsServer: _ClassVar[ClusterServiceName]
    kInfraoperator: _ClassVar[ClusterServiceName]
    kMarketplaceoperator: _ClassVar[ClusterServiceName]
    kCohesion: _ClassVar[ClusterServiceName]
    kSpireApp: _ClassVar[ClusterServiceName]
    kGaia: _ClassVar[ClusterServiceName]

class ViewStatsMetric(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kSystemUsageBytes: _ClassVar[ViewStatsMetric]
    kChunkBytesPhysical: _ClassVar[ViewStatsMetric]
    kNumBytesWritten: _ClassVar[ViewStatsMetric]
    kNumBytesRead: _ClassVar[ViewStatsMetric]
    kPeakReadThroughput: _ClassVar[ViewStatsMetric]
    kPeakWriteThroughput: _ClassVar[ViewStatsMetric]

class AuthenticationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kAuthLocal: _ClassVar[AuthenticationType]
    kAuthAd: _ClassVar[AuthenticationType]
    kAuthSalesforce: _ClassVar[AuthenticationType]
    kAuthGoogle: _ClassVar[AuthenticationType]
    kAuthSso: _ClassVar[AuthenticationType]
    kAuthMcmOnPrem: _ClassVar[AuthenticationType]
    kAuthService: _ClassVar[AuthenticationType]

class PrincipalObjectClass(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kGroup: _ClassVar[PrincipalObjectClass]
    kUser: _ClassVar[PrincipalObjectClass]
    kComputer: _ClassVar[PrincipalObjectClass]
    kWellKnownPrincipal: _ClassVar[PrincipalObjectClass]
    kServiceAccount: _ClassVar[PrincipalObjectClass]

class QosPolicyPriority(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kHigh: _ClassVar[QosPolicyPriority]
    kLow: _ClassVar[QosPolicyPriority]

class GroupBy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kProtectionJob: _ClassVar[GroupBy]
    kTarget: _ClassVar[GroupBy]

class ConsumerType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kNoneType: _ClassVar[ConsumerType]
    kViews: _ClassVar[ConsumerType]
    kProtectionRuns: _ClassVar[ConsumerType]
    kReplicationRuns: _ClassVar[ConsumerType]
    kViewProtectionRuns: _ClassVar[ConsumerType]

class ProtectionJobField(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kProtectionJobName: _ClassVar[ProtectionJobField]
    kProtectionJobDescription: _ClassVar[ProtectionJobField]
    kProtectionJobSources: _ClassVar[ProtectionJobField]
    kProtectionJobSchedule: _ClassVar[ProtectionJobField]
    kProtectionJobFullSchedule: _ClassVar[ProtectionJobField]
    kProtectionJobRetrySettings: _ClassVar[ProtectionJobField]
    kProtectionJobRetentionPolicy: _ClassVar[ProtectionJobField]
    kProtectionJobIndexingPolicy: _ClassVar[ProtectionJobField]
    kProtectionJobAlertingPolicy: _ClassVar[ProtectionJobField]
    kProtectionJobPriority: _ClassVar[ProtectionJobField]
    kProtectionJobQuiesce: _ClassVar[ProtectionJobField]
    kProtectionJobSla: _ClassVar[ProtectionJobField]
    kProtectionJobPolicyId: _ClassVar[ProtectionJobField]
    kProtectionJobTimezone: _ClassVar[ProtectionJobField]
    kProtectionJobFutureRunsPaused: _ClassVar[ProtectionJobField]
    kProtectionJobFutureRunsResumed: _ClassVar[ProtectionJobField]
    kSnapshotTargetPolicy: _ClassVar[ProtectionJobField]
    kProtectionJobBlackoutWindow: _ClassVar[ProtectionJobField]
    kProtectionJobQOS: _ClassVar[ProtectionJobField]
    kProtectionJobInvalidField: _ClassVar[ProtectionJobField]

class S3KeyMappingType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kRandom: _ClassVar[S3KeyMappingType]
    kShort: _ClassVar[S3KeyMappingType]
    kLong: _ClassVar[S3KeyMappingType]
    kHierarchical: _ClassVar[S3KeyMappingType]
    kObjectId: _ClassVar[S3KeyMappingType]

class NodeOperation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kNoActiveOperation: _ClassVar[NodeOperation]
    kDestroyCluster: _ClassVar[NodeOperation]
    kUpgradeCluster: _ClassVar[NodeOperation]
    kRestartCluster: _ClassVar[NodeOperation]
    kCreateCluster: _ClassVar[NodeOperation]
    kExpandCluster: _ClassVar[NodeOperation]
    kUpgradeNode: _ClassVar[NodeOperation]
    kRemoveNode: _ClassVar[NodeOperation]
    kAddDisks: _ClassVar[NodeOperation]
    kMarkDiskOffline: _ClassVar[NodeOperation]

class RemovalState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kNoRemoval: _ClassVar[RemovalState]
    kNodeRemoval: _ClassVar[RemovalState]
    kDiskRemoval: _ClassVar[RemovalState]
    kNodeAndDiskRemoval: _ClassVar[RemovalState]

class FaultToleranceLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kNode: _ClassVar[FaultToleranceLevel]
    kChassis: _ClassVar[FaultToleranceLevel]
    kRack: _ClassVar[FaultToleranceLevel]

class NfsSquashType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kNone: _ClassVar[NfsSquashType]
    kRootSquash: _ClassVar[NfsSquashType]
    kAllSquash: _ClassVar[NfsSquashType]

class McmTenantType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    Dmaas: _ClassVar[McmTenantType]
    Mcm: _ClassVar[McmTenantType]

class RecoveryProcessType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kInstantRecovery: _ClassVar[RecoveryProcessType]
    kCopyRecovery: _ClassVar[RecoveryProcessType]

class LockoutReason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NotLocked: _ClassVar[LockoutReason]
    FailedLoginAttempts: _ClassVar[LockoutReason]
    LockedByAdmin: _ClassVar[LockoutReason]
    Inactivity: _ClassVar[LockoutReason]
    OtherReasons: _ClassVar[LockoutReason]

class OtpCodeType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    Totp: _ClassVar[OtpCodeType]
    Email: _ClassVar[OtpCodeType]

class CloudClusterSize(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    Small: _ClassVar[CloudClusterSize]
    Medium: _ClassVar[CloudClusterSize]
    Large: _ClassVar[CloudClusterSize]
    XLarge: _ClassVar[CloudClusterSize]

class MaintenanceStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UnderMaintenance: _ClassVar[MaintenanceStatus]
    ScheduledMaintenance: _ClassVar[MaintenanceStatus]
    NotConfigured: _ClassVar[MaintenanceStatus]
kJobRunning: IrisVaultJobStatus
kJobSucceeded: IrisVaultJobStatus
kJobFailed: IrisVaultJobStatus
kJobCanceled: IrisVaultJobStatus
kJobPaused: IrisVaultJobStatus
kPrincipalView: PrivilegeIdValue
kPrincipalModify: PrivilegeIdValue
kAppLaunch: PrivilegeIdValue
kAppsManagement: PrivilegeIdValue
kOrganizationView: PrivilegeIdValue
kOrganizationModify: PrivilegeIdValue
kOrganizationImpersonate: PrivilegeIdValue
kCloneView: PrivilegeIdValue
kCloneModify: PrivilegeIdValue
kClusterView: PrivilegeIdValue
kClusterModify: PrivilegeIdValue
kClusterCreate: PrivilegeIdValue
kClusterSupport: PrivilegeIdValue
kClusterUpgrade: PrivilegeIdValue
kClusterRemoteView: PrivilegeIdValue
kClusterRemoteModify: PrivilegeIdValue
kClusterExternalTargetView: PrivilegeIdValue
kClusterExternalTargetModify: PrivilegeIdValue
kClusterAudit: PrivilegeIdValue
kAlertView: PrivilegeIdValue
kAlertModify: PrivilegeIdValue
kVlanView: PrivilegeIdValue
kVlanModify: PrivilegeIdValue
kHybridExtenderView: PrivilegeIdValue
kHybridExtenderDownload: PrivilegeIdValue
kAdLdapView: PrivilegeIdValue
kAdLdapModify: PrivilegeIdValue
kSchedulerView: PrivilegeIdValue
kSchedulerModify: PrivilegeIdValue
kProtectionView: PrivilegeIdValue
kProtectionModify: PrivilegeIdValue
kProtectionJobOperate: PrivilegeIdValue
kProtectionSourceModify: PrivilegeIdValue
kProtectionPolicyView: PrivilegeIdValue
kProtectionPolicyModify: PrivilegeIdValue
kRestoreView: PrivilegeIdValue
kRestoreModify: PrivilegeIdValue
kRestoreDownload: PrivilegeIdValue
kRemoteRestore: PrivilegeIdValue
kStorageView: PrivilegeIdValue
kStorageModify: PrivilegeIdValue
kStorageDomainView: PrivilegeIdValue
kStorageDomainModify: PrivilegeIdValue
kAnalyticsView: PrivilegeIdValue
kAnalyticsModify: PrivilegeIdValue
kReportsView: PrivilegeIdValue
kMcmModify: PrivilegeIdValue
kDataSecurity: PrivilegeIdValue
kSmbBackup: PrivilegeIdValue
kSmbRestore: PrivilegeIdValue
kSmbTakeOwnership: PrivilegeIdValue
kSmbAuditing: PrivilegeIdValue
kMcmUnregister: PrivilegeIdValue
kMcmUpgrade: PrivilegeIdValue
kMcmModifySuperAdmin: PrivilegeIdValue
kMcmViewSuperAdmin: PrivilegeIdValue
kMcmModifyCohesityAdmin: PrivilegeIdValue
kMcmViewCohesityAdmin: PrivilegeIdValue
kObjectSearch: PrivilegeIdValue
kFileDatalockExpiryTimeDecrease: PrivilegeIdValue
kNodeView: PrivilegeIdValue
kMcmObjectSearch: PrivilegeIdValue
kRunbookModify: PrivilegeIdValue
kKeystoneView: PrivilegeIdValue
kKeystoneModify: PrivilegeIdValue
kManageProtectionSourceAll: PrivilegeIdValue
kManageProtectionSourceVmwareStandaloneHost: PrivilegeIdValue
kManageProtectionSourceVmwareVcenter: PrivilegeIdValue
kManageProtectionSourceVmwareVcloudDirector: PrivilegeIdValue
kManageProtectionSourceHyperVScvmmServer: PrivilegeIdValue
kManageProtectionSourceHyperVStandaloneHost: PrivilegeIdValue
kManageProtectionSourceHyperVStandaloneCluster: PrivilegeIdValue
kManageProtectionSourceAcropolisStandaloneCluster: PrivilegeIdValue
kManageProtectionSourceAcropolisGenericStandaloneCluster: PrivilegeIdValue
kManageProtectionSourceGcpIamUser: PrivilegeIdValue
kManageProtectionSourceAwsIamUser: PrivilegeIdValue
kManageProtectionSourceAzureSubscription: PrivilegeIdValue
kManageProtectionSourceKvmOvirtManager: PrivilegeIdValue
kManageProtectionSourcePhysical: PrivilegeIdValue
kManageProtectionSourceO365Domain: PrivilegeIdValue
kManageProtectionSourceSql: PrivilegeIdValue
kManageProtectionSourceOracle: PrivilegeIdValue
kManageProtectionSourcePureStorageArray: PrivilegeIdValue
kManageProtectionSourceNimbleStorageArray: PrivilegeIdValue
kManageProtectionSourceHyperFlexServer: PrivilegeIdValue
kManageProtectionSourceAD: PrivilegeIdValue
kManageProtectionSourceIsilonCluster: PrivilegeIdValue
kManageProtectionSourceNetAppCluster: PrivilegeIdValue
kManageProtectionSourceNetAppVServer: PrivilegeIdValue
kManageProtectionSourceGenericNasHost: PrivilegeIdValue
kManageProtectionSourceFlashbladeStorageArray: PrivilegeIdValue
kManageProtectionSourceGpfsCluster: PrivilegeIdValue
kManageProtectionSourceElastifileCluster: PrivilegeIdValue
kNisView: PrivilegeIdValue
kNisModify: PrivilegeIdValue
kMcmSimulatorView: PrivilegeIdValue
kMcmSimulatorModify: PrivilegeIdValue
kManageProtectionSourceExchange: PrivilegeIdValue
kLinuxUserBashShellAccessDeprecated: PrivilegeIdValue
kLinuxUserSudoAccess: PrivilegeIdValue
kManageProtectionSourceCassandra: PrivilegeIdValue
kManageProtectionSourceMongoDB: PrivilegeIdValue
kManageProtectionSourceCouchbase: PrivilegeIdValue
kManageProtectionSourceHdfs: PrivilegeIdValue
kManageProtectionSourceHbase: PrivilegeIdValue
kManageProtectionSourceHive: PrivilegeIdValue
kManageProtectionSourceKubernetes: PrivilegeIdValue
kManageBulkAgentInstallApp: PrivilegeIdValue
kClusterMaintenance: PrivilegeIdValue
kAllowUiAccess: PrivilegeIdValue
kRunbookView: PrivilegeIdValue
kRunbookExecute: PrivilegeIdValue
kBifrostVlanView: PrivilegeIdValue
kBifrostVlanModify: PrivilegeIdValue
kApiKeyModify: PrivilegeIdValue
kApiKeyView: PrivilegeIdValue
kKerberosView: PrivilegeIdValue
kKerberosModify: PrivilegeIdValue
kTagsView: PrivilegeIdValue
kTagsModify: PrivilegeIdValue
kTagsManage: PrivilegeIdValue
kManageProtectionSourceUda: PrivilegeIdValue
kAgentUpgradeView: PrivilegeIdValue
kAgentUpgradeModify: PrivilegeIdValue
kManageS3Keys: PrivilegeIdValue
kMcmAccountView: PrivilegeIdValue
kMcmAccountModify: PrivilegeIdValue
kProtectionDeleteSnapshot: PrivilegeIdValue
kMfaModify: PrivilegeIdValue
kManageProtectionSourceSfdc: PrivilegeIdValue
kMcmRegionConfigure: PrivilegeIdValue
kManageSnapshotTags: PrivilegeIdValue
kRestoreSnapshotTags: PrivilegeIdValue
kAuditLogView: PrivilegeIdValue
kAuditLogManage: PrivilegeIdValue
kManageObservability: PrivilegeIdValue
kGflagManagement: PrivilegeIdValue
kDGaaSView: PrivilegeIdValue
kDGaaSModify: PrivilegeIdValue
kRPaaSRegionModify: PrivilegeIdValue
kDRaaSView: PrivilegeIdValue
kDRaaSModify: PrivilegeIdValue
kHighClassified: PrivilegeIdValue
kBifrostRealmView: PrivilegeIdValue
kBifrostRealmModify: PrivilegeIdValue
kSecurityAdvisorView: PrivilegeIdValue
kSecurityAdvisorModify: PrivilegeIdValue
kSupportChannelModify: PrivilegeIdValue
kQuorumGroupView: PrivilegeIdValue
kQuorumGroupCreate: PrivilegeIdValue
kMcmModifyMfa: PrivilegeIdValue
kS3AbacView: PrivilegeIdValue
kS3AbacModify: PrivilegeIdValue
kGaiaView: PrivilegeIdValue
kGaiaModify: PrivilegeIdValue
kSalesforce: McmLoginType
kSso: McmLoginType
kAccepted: RunStatus
kRunning: RunStatus
kCanceling: RunStatus
kCanceled: RunStatus
kSuccess: RunStatus
kFailure: RunStatus
kWarning: RunStatus
kOnHold: RunStatus
kMissed: RunStatus
kFinalizing: RunStatus
kWaitingToRetry: RunStatus
kSkipped: RunStatus
kAll: ProtocolAccess
kNFSOnly: ProtocolAccess
kSMBOnly: ProtocolAccess
kS3Only: ProtocolAccess
kUnknown: ProtocolAccess
kSwiftOnly: ProtocolAccess
kRecovery: TaskType
kClone: TaskType
kCompressionNone: CompressionLevel
kCompressionLow: CompressionLevel
kCompressionHigh: CompressionLevel
kPoor: PasswordScoreProto
kWeak: PasswordScoreProto
kStrong: PasswordScoreProto
kExcellent: PasswordScoreProto
kHealthTile: TileType
kJobRunsTile: TileType
kRecoveriesTile: TileType
kProtectedObjectsTile: TileType
kProtectionTile: TileType
kAuditLogsTile: TileType
kIopsTile: TileType
kThroughputTile: TileType
kStorageEfficiencyTile: TileType
kPause: UpdateProtectionJobAction
kResume: UpdateProtectionJobAction
kActivate: UpdateProtectionJobAction
kDeactivate: UpdateProtectionJobAction
kMinute: RpoIntervalUnit
kHour: RpoIntervalUnit
kDay: RpoIntervalUnit
kWeek: RpoIntervalUnit
kMonth: RpoIntervalUnit
kPhysical: ClusterType
kVirtual: ClusterType
kCloud: ClusterType
KNoError: NexusOpError
KSwPackageNotFoundError: NexusOpError
KSwPackageExistsError: NexusOpError
KCurrNodeNotFoundError: NexusOpError
KClusterExistsError: NexusOpError
KNotClusterError: NexusOpError
KNotFreeNodeError: NexusOpError
KQueryParamParseError: NexusOpError
KQueryParamEmpty: NexusOpError
KTimedoutError: NexusOpError
KInvalidInput: NexusOpError
KInternalError: NexusOpError
KMethodNotAllowedError: NexusOpError
KOpRunningError: NexusOpError
KRetryError: NexusOpError
KNodeNotReachable: NexusOpError
KNodeUnconfigured: NexusOpError
KNotImplemented: NexusOpError
KSwPackageNotCompatible: NexusOpError
KHardwareNotCompatible: NexusOpError
KFirmwareNotCompatible: NexusOpError
KNodeHealthCheckError: NexusOpError
KNodeBeingAddedToCluster: NexusOpError
kNotification: AuditLogType
kPhysicalInterface: NetworkInterfaceType
kBondMasterInterface: NetworkInterfaceType
kBondSlaveInterface: NetworkInterfaceType
kTaggedVlanInterface: NetworkInterfaceType
kReplicationService: InterfaceServiceType
kRemoteTunnelService: InterfaceServiceType
kClusterDataService: InterfaceServiceType
kAvahiDiscoverService: InterfaceServiceType
kPrimary: InterfaceRoleType
kSecondary: InterfaceRoleType
kActiveBackup: NetworkBondingMode
k802_3ad: NetworkBondingMode
kStop: ClusterServiceAction
kStart: ClusterServiceAction
kRestart: ClusterServiceAction
kServiceStopped: ClusterServiceState
kServiceRunning: ClusterServiceState
kServiceRestarting: ClusterServiceState
kInvalidService: ClusterServiceName
kApollo: ClusterServiceName
kBridge: ClusterServiceName
kGenie: ClusterServiceName
kGenieGofer: ClusterServiceName
kMagneto: ClusterServiceName
kIris: ClusterServiceName
kIrisProxy: ClusterServiceName
kNewScribe: ClusterServiceName
kStats: ClusterServiceName
kYoda: ClusterServiceName
kAlerts: ClusterServiceName
kKeychain: ClusterServiceName
kLogWatcher: ClusterServiceName
kStatsCollector: ClusterServiceName
kGandalf: ClusterServiceName
kNexus: ClusterServiceName
kNexusProxy: ClusterServiceName
kStorageProxy: ClusterServiceName
kTricorder: ClusterServiceName
kRtClient: ClusterServiceName
kVaultProxy: ClusterServiceName
kSmbProxy: ClusterServiceName
kBridgeProxy: ClusterServiceName
kLibrarian: ClusterServiceName
kGroot: ClusterServiceName
kEagleAgent: ClusterServiceName
kAthena: ClusterServiceName
kBifrostBroker: ClusterServiceName
kElixir: ClusterServiceName
kVulscan: ClusterServiceName
kPostgres: ClusterServiceName
kAtom: ClusterServiceName
kYodaAgent: ClusterServiceName
kSmb2Proxy: ClusterServiceName
kThrottler: ClusterServiceName
kKafka: ClusterServiceName
kEventing: ClusterServiceName
kAgentinstall: ClusterServiceName
kImanis: ClusterServiceName
kElrond: ClusterServiceName
kHeimdall: ClusterServiceName
kBifrost: ClusterServiceName
kIcebox: ClusterServiceName
kNodeExporter: ClusterServiceName
kCompass: ClusterServiceName
kPatch: ClusterServiceName
kEtlServer: ClusterServiceName
kUpgrader: ClusterServiceName
kTestservice: ClusterServiceName
kOs: ClusterServiceName
kJanus: ClusterServiceName
kHcCli: ClusterServiceName
kDlp: ClusterServiceName
kPushproxClient: ClusterServiceName
kPushClient: ClusterServiceName
kAegis: ClusterServiceName
kNfsProxy: ClusterServiceName
kElixirWorkerservice: ClusterServiceName
kArgusApp: ClusterServiceName
kMetadataservice: ClusterServiceName
kSpireServer: ClusterServiceName
kSpireAgent: ClusterServiceName
kWorkqueueserver: ClusterServiceName
kElasticsearch: ClusterServiceName
kLicensing: ClusterServiceName
kAxon: ClusterServiceName
kMagnus: ClusterServiceName
kOdsApp: ClusterServiceName
kShelteredHarborApp: ClusterServiceName
kShelteredHarborUda: ClusterServiceName
kCoredns: ClusterServiceName
kCohesityCa: ClusterServiceName
kMetricsServer: ClusterServiceName
kInfraoperator: ClusterServiceName
kMarketplaceoperator: ClusterServiceName
kCohesion: ClusterServiceName
kSpireApp: ClusterServiceName
kGaia: ClusterServiceName
kSystemUsageBytes: ViewStatsMetric
kChunkBytesPhysical: ViewStatsMetric
kNumBytesWritten: ViewStatsMetric
kNumBytesRead: ViewStatsMetric
kPeakReadThroughput: ViewStatsMetric
kPeakWriteThroughput: ViewStatsMetric
kAuthLocal: AuthenticationType
kAuthAd: AuthenticationType
kAuthSalesforce: AuthenticationType
kAuthGoogle: AuthenticationType
kAuthSso: AuthenticationType
kAuthMcmOnPrem: AuthenticationType
kAuthService: AuthenticationType
kGroup: PrincipalObjectClass
kUser: PrincipalObjectClass
kComputer: PrincipalObjectClass
kWellKnownPrincipal: PrincipalObjectClass
kServiceAccount: PrincipalObjectClass
kHigh: QosPolicyPriority
kLow: QosPolicyPriority
kProtectionJob: GroupBy
kTarget: GroupBy
kNoneType: ConsumerType
kViews: ConsumerType
kProtectionRuns: ConsumerType
kReplicationRuns: ConsumerType
kViewProtectionRuns: ConsumerType
kProtectionJobName: ProtectionJobField
kProtectionJobDescription: ProtectionJobField
kProtectionJobSources: ProtectionJobField
kProtectionJobSchedule: ProtectionJobField
kProtectionJobFullSchedule: ProtectionJobField
kProtectionJobRetrySettings: ProtectionJobField
kProtectionJobRetentionPolicy: ProtectionJobField
kProtectionJobIndexingPolicy: ProtectionJobField
kProtectionJobAlertingPolicy: ProtectionJobField
kProtectionJobPriority: ProtectionJobField
kProtectionJobQuiesce: ProtectionJobField
kProtectionJobSla: ProtectionJobField
kProtectionJobPolicyId: ProtectionJobField
kProtectionJobTimezone: ProtectionJobField
kProtectionJobFutureRunsPaused: ProtectionJobField
kProtectionJobFutureRunsResumed: ProtectionJobField
kSnapshotTargetPolicy: ProtectionJobField
kProtectionJobBlackoutWindow: ProtectionJobField
kProtectionJobQOS: ProtectionJobField
kProtectionJobInvalidField: ProtectionJobField
kRandom: S3KeyMappingType
kShort: S3KeyMappingType
kLong: S3KeyMappingType
kHierarchical: S3KeyMappingType
kObjectId: S3KeyMappingType
kNoActiveOperation: NodeOperation
kDestroyCluster: NodeOperation
kUpgradeCluster: NodeOperation
kRestartCluster: NodeOperation
kCreateCluster: NodeOperation
kExpandCluster: NodeOperation
kUpgradeNode: NodeOperation
kRemoveNode: NodeOperation
kAddDisks: NodeOperation
kMarkDiskOffline: NodeOperation
kNoRemoval: RemovalState
kNodeRemoval: RemovalState
kDiskRemoval: RemovalState
kNodeAndDiskRemoval: RemovalState
kNode: FaultToleranceLevel
kChassis: FaultToleranceLevel
kRack: FaultToleranceLevel
kNone: NfsSquashType
kRootSquash: NfsSquashType
kAllSquash: NfsSquashType
Dmaas: McmTenantType
Mcm: McmTenantType
kInstantRecovery: RecoveryProcessType
kCopyRecovery: RecoveryProcessType
NotLocked: LockoutReason
FailedLoginAttempts: LockoutReason
LockedByAdmin: LockoutReason
Inactivity: LockoutReason
OtherReasons: LockoutReason
Totp: OtpCodeType
Email: OtpCodeType
Small: CloudClusterSize
Medium: CloudClusterSize
Large: CloudClusterSize
XLarge: CloudClusterSize
UnderMaintenance: MaintenanceStatus
ScheduledMaintenance: MaintenanceStatus
NotConfigured: MaintenanceStatus
