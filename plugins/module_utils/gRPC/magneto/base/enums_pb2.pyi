from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class Environment(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kVMware: _ClassVar[Environment.Type]
        kHyperV: _ClassVar[Environment.Type]
        kSQL: _ClassVar[Environment.Type]
        kView: _ClassVar[Environment.Type]
        kPuppeteer: _ClassVar[Environment.Type]
        kPhysical: _ClassVar[Environment.Type]
        kPure: _ClassVar[Environment.Type]
        kAzure: _ClassVar[Environment.Type]
        kNetapp: _ClassVar[Environment.Type]
        kAgent: _ClassVar[Environment.Type]
        kGenericNas: _ClassVar[Environment.Type]
        kAcropolis: _ClassVar[Environment.Type]
        kPhysicalFiles: _ClassVar[Environment.Type]
        kIsilon: _ClassVar[Environment.Type]
        kKVM: _ClassVar[Environment.Type]
        kAWS: _ClassVar[Environment.Type]
        kExchange: _ClassVar[Environment.Type]
        kHyperVVSS: _ClassVar[Environment.Type]
        kOracle: _ClassVar[Environment.Type]
        kGCP: _ClassVar[Environment.Type]
        kFlashBlade: _ClassVar[Environment.Type]
        kAWSNative: _ClassVar[Environment.Type]
        kVCD: _ClassVar[Environment.Type]
        kO365: _ClassVar[Environment.Type]
        kO365Outlook: _ClassVar[Environment.Type]
        kHyperFlex: _ClassVar[Environment.Type]
        kGCPNative: _ClassVar[Environment.Type]
        kAzureNative: _ClassVar[Environment.Type]
        kAzureSnapshotManager: _ClassVar[Environment.Type]
        kAD: _ClassVar[Environment.Type]
        kAWSSnapshotManager: _ClassVar[Environment.Type]
        kGPFS: _ClassVar[Environment.Type]
        kRDSSnapshotManager: _ClassVar[Environment.Type]
        kAuroraSnapshotManager: _ClassVar[Environment.Type]
        kKubernetes: _ClassVar[Environment.Type]
        kNimble: _ClassVar[Environment.Type]
        kElastifile: _ClassVar[Environment.Type]
        kCassandra: _ClassVar[Environment.Type]
        kMongoDB: _ClassVar[Environment.Type]
        kHBase: _ClassVar[Environment.Type]
        kHive: _ClassVar[Environment.Type]
        kHdfs: _ClassVar[Environment.Type]
        kCouchbase: _ClassVar[Environment.Type]
        kO365PublicFolders: _ClassVar[Environment.Type]
        kUDA: _ClassVar[Environment.Type]
        kO365Teams: _ClassVar[Environment.Type]
        kO365Group: _ClassVar[Environment.Type]
        kO365Exchange: _ClassVar[Environment.Type]
        kO365OneDrive: _ClassVar[Environment.Type]
        kO365Sharepoint: _ClassVar[Environment.Type]
        kSfdc: _ClassVar[Environment.Type]
        kAwsS3: _ClassVar[Environment.Type]
        kAwsRDSOracleRMANBackup: _ClassVar[Environment.Type]
        kAwsRDSPostgresBackup: _ClassVar[Environment.Type]
        kAzureSQL: _ClassVar[Environment.Type]
        kIbmFlashSystem: _ClassVar[Environment.Type]
    kVMware: Environment.Type
    kHyperV: Environment.Type
    kSQL: Environment.Type
    kView: Environment.Type
    kPuppeteer: Environment.Type
    kPhysical: Environment.Type
    kPure: Environment.Type
    kAzure: Environment.Type
    kNetapp: Environment.Type
    kAgent: Environment.Type
    kGenericNas: Environment.Type
    kAcropolis: Environment.Type
    kPhysicalFiles: Environment.Type
    kIsilon: Environment.Type
    kKVM: Environment.Type
    kAWS: Environment.Type
    kExchange: Environment.Type
    kHyperVVSS: Environment.Type
    kOracle: Environment.Type
    kGCP: Environment.Type
    kFlashBlade: Environment.Type
    kAWSNative: Environment.Type
    kVCD: Environment.Type
    kO365: Environment.Type
    kO365Outlook: Environment.Type
    kHyperFlex: Environment.Type
    kGCPNative: Environment.Type
    kAzureNative: Environment.Type
    kAzureSnapshotManager: Environment.Type
    kAD: Environment.Type
    kAWSSnapshotManager: Environment.Type
    kGPFS: Environment.Type
    kRDSSnapshotManager: Environment.Type
    kAuroraSnapshotManager: Environment.Type
    kKubernetes: Environment.Type
    kNimble: Environment.Type
    kElastifile: Environment.Type
    kCassandra: Environment.Type
    kMongoDB: Environment.Type
    kHBase: Environment.Type
    kHive: Environment.Type
    kHdfs: Environment.Type
    kCouchbase: Environment.Type
    kO365PublicFolders: Environment.Type
    kUDA: Environment.Type
    kO365Teams: Environment.Type
    kO365Group: Environment.Type
    kO365Exchange: Environment.Type
    kO365OneDrive: Environment.Type
    kO365Sharepoint: Environment.Type
    kSfdc: Environment.Type
    kAwsS3: Environment.Type
    kAwsRDSOracleRMANBackup: Environment.Type
    kAwsRDSPostgresBackup: Environment.Type
    kAzureSQL: Environment.Type
    kIbmFlashSystem: Environment.Type
    def __init__(self) -> None: ...

class HostEnv(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kLinux: _ClassVar[HostEnv.Type]
        kWindows: _ClassVar[HostEnv.Type]
        kOther: _ClassVar[HostEnv.Type]
        kAix: _ClassVar[HostEnv.Type]
        kSolaris: _ClassVar[HostEnv.Type]
        kSapHana: _ClassVar[HostEnv.Type]
        kSapOracle: _ClassVar[HostEnv.Type]
        kCockroachDB: _ClassVar[HostEnv.Type]
        kMySQL: _ClassVar[HostEnv.Type]
        kSapSybase: _ClassVar[HostEnv.Type]
        kSapMaxDB: _ClassVar[HostEnv.Type]
        kSapSybaseIQ: _ClassVar[HostEnv.Type]
        kDB2: _ClassVar[HostEnv.Type]
        kSapASE: _ClassVar[HostEnv.Type]
        kMariaDB: _ClassVar[HostEnv.Type]
        kPostgreSQL: _ClassVar[HostEnv.Type]
        kHPUX: _ClassVar[HostEnv.Type]
        kVOS: _ClassVar[HostEnv.Type]
    kLinux: HostEnv.Type
    kWindows: HostEnv.Type
    kOther: HostEnv.Type
    kAix: HostEnv.Type
    kSolaris: HostEnv.Type
    kSapHana: HostEnv.Type
    kSapOracle: HostEnv.Type
    kCockroachDB: HostEnv.Type
    kMySQL: HostEnv.Type
    kSapSybase: HostEnv.Type
    kSapMaxDB: HostEnv.Type
    kSapSybaseIQ: HostEnv.Type
    kDB2: HostEnv.Type
    kSapASE: HostEnv.Type
    kMariaDB: HostEnv.Type
    kPostgreSQL: HostEnv.Type
    kHPUX: HostEnv.Type
    kVOS: HostEnv.Type
    def __init__(self) -> None: ...

class Day(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kSunday: _ClassVar[Day.Type]
        kMonday: _ClassVar[Day.Type]
        kTuesday: _ClassVar[Day.Type]
        kWednesday: _ClassVar[Day.Type]
        kThursday: _ClassVar[Day.Type]
        kFriday: _ClassVar[Day.Type]
        kSaturday: _ClassVar[Day.Type]
    kSunday: Day.Type
    kMonday: Day.Type
    kTuesday: Day.Type
    kWednesday: Day.Type
    kThursday: Day.Type
    kFriday: Day.Type
    kSaturday: Day.Type
    def __init__(self) -> None: ...

class BackupQoSPrincipal(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kBackupHDD: _ClassVar[BackupQoSPrincipal.Type]
        kBackupSSD: _ClassVar[BackupQoSPrincipal.Type]
        kTestAndDevHigh: _ClassVar[BackupQoSPrincipal.Type]
        kBackupAll: _ClassVar[BackupQoSPrincipal.Type]
    kBackupHDD: BackupQoSPrincipal.Type
    kBackupSSD: BackupQoSPrincipal.Type
    kTestAndDevHigh: BackupQoSPrincipal.Type
    kBackupAll: BackupQoSPrincipal.Type
    def __init__(self) -> None: ...

class ScheduledBackupType(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kRegular: _ClassVar[ScheduledBackupType.Type]
        kFull: _ClassVar[ScheduledBackupType.Type]
        kLog: _ClassVar[ScheduledBackupType.Type]
        kSystem: _ClassVar[ScheduledBackupType.Type]
        kRefresh: _ClassVar[ScheduledBackupType.Type]
        kHydrateCDP: _ClassVar[ScheduledBackupType.Type]
        kStorageArraySnapshot: _ClassVar[ScheduledBackupType.Type]
    kRegular: ScheduledBackupType.Type
    kFull: ScheduledBackupType.Type
    kLog: ScheduledBackupType.Type
    kSystem: ScheduledBackupType.Type
    kRefresh: ScheduledBackupType.Type
    kHydrateCDP: ScheduledBackupType.Type
    kStorageArraySnapshot: ScheduledBackupType.Type
    def __init__(self) -> None: ...

class ExternalSnapshotDeletionType(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kDeleteNow: _ClassVar[ExternalSnapshotDeletionType.Type]
        kDeleteBasedOnPolicy: _ClassVar[ExternalSnapshotDeletionType.Type]
    kDeleteNow: ExternalSnapshotDeletionType.Type
    kDeleteBasedOnPolicy: ExternalSnapshotDeletionType.Type
    def __init__(self) -> None: ...

class VerificationStatus(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kPending: _ClassVar[VerificationStatus.Type]
        kScheduled: _ClassVar[VerificationStatus.Type]
        kFinished: _ClassVar[VerificationStatus.Type]
        kRefreshInProgress: _ClassVar[VerificationStatus.Type]
    kPending: VerificationStatus.Type
    kScheduled: VerificationStatus.Type
    kFinished: VerificationStatus.Type
    kRefreshInProgress: VerificationStatus.Type
    def __init__(self) -> None: ...

class ConversionStatus(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kPending: _ClassVar[ConversionStatus.Type]
        kScheduled: _ClassVar[ConversionStatus.Type]
        kFinished: _ClassVar[ConversionStatus.Type]
    kPending: ConversionStatus.Type
    kScheduled: ConversionStatus.Type
    kFinished: ConversionStatus.Type
    def __init__(self) -> None: ...

class ConversionCleanupStatus(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kPending: _ClassVar[ConversionCleanupStatus.Type]
        kFinished: _ClassVar[ConversionCleanupStatus.Type]
    kPending: ConversionCleanupStatus.Type
    kFinished: ConversionCleanupStatus.Type
    def __init__(self) -> None: ...

class StorageProtocol(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNas: _ClassVar[StorageProtocol.Type]
        kSan: _ClassVar[StorageProtocol.Type]
        kVSS: _ClassVar[StorageProtocol.Type]
    kNas: StorageProtocol.Type
    kSan: StorageProtocol.Type
    kVSS: StorageProtocol.Type
    def __init__(self) -> None: ...

class NasProtocol(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNoProtocol: _ClassVar[NasProtocol.Type]
        kNfs3: _ClassVar[NasProtocol.Type]
        kNfs4: _ClassVar[NasProtocol.Type]
        kNfs4_1: _ClassVar[NasProtocol.Type]
        kCifs1: _ClassVar[NasProtocol.Type]
        kCifs2: _ClassVar[NasProtocol.Type]
        kCifs3: _ClassVar[NasProtocol.Type]
    kNoProtocol: NasProtocol.Type
    kNfs3: NasProtocol.Type
    kNfs4: NasProtocol.Type
    kNfs4_1: NasProtocol.Type
    kCifs1: NasProtocol.Type
    kCifs2: NasProtocol.Type
    kCifs3: NasProtocol.Type
    def __init__(self) -> None: ...

class PublicTaskStatus(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kAccepted: _ClassVar[PublicTaskStatus.Type]
        kRunning: _ClassVar[PublicTaskStatus.Type]
        kOnHold: _ClassVar[PublicTaskStatus.Type]
        kCanceling: _ClassVar[PublicTaskStatus.Type]
        kCanceled: _ClassVar[PublicTaskStatus.Type]
        kSuccess: _ClassVar[PublicTaskStatus.Type]
        kWarning: _ClassVar[PublicTaskStatus.Type]
        kFailure: _ClassVar[PublicTaskStatus.Type]
        kMissed: _ClassVar[PublicTaskStatus.Type]
        kPausing: _ClassVar[PublicTaskStatus.Type]
        kPaused: _ClassVar[PublicTaskStatus.Type]
        kResuming: _ClassVar[PublicTaskStatus.Type]
        kWaiting: _ClassVar[PublicTaskStatus.Type]
        kFinalizing: _ClassVar[PublicTaskStatus.Type]
        kWaitingToRetry: _ClassVar[PublicTaskStatus.Type]
        kSkipped: _ClassVar[PublicTaskStatus.Type]
    kAccepted: PublicTaskStatus.Type
    kRunning: PublicTaskStatus.Type
    kOnHold: PublicTaskStatus.Type
    kCanceling: PublicTaskStatus.Type
    kCanceled: PublicTaskStatus.Type
    kSuccess: PublicTaskStatus.Type
    kWarning: PublicTaskStatus.Type
    kFailure: PublicTaskStatus.Type
    kMissed: PublicTaskStatus.Type
    kPausing: PublicTaskStatus.Type
    kPaused: PublicTaskStatus.Type
    kResuming: PublicTaskStatus.Type
    kWaiting: PublicTaskStatus.Type
    kFinalizing: PublicTaskStatus.Type
    kWaitingToRetry: PublicTaskStatus.Type
    kSkipped: PublicTaskStatus.Type
    def __init__(self) -> None: ...

class TargetType(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kBridge: _ClassVar[TargetType.Type]
        kBridgeProxy: _ClassVar[TargetType.Type]
    kBridge: TargetType.Type
    kBridgeProxy: TargetType.Type
    def __init__(self) -> None: ...

class JobPauseReason(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kTenantDeactivation: _ClassVar[JobPauseReason.Type]
    kTenantDeactivation: JobPauseReason.Type
    def __init__(self) -> None: ...

class AttributeType(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kUnknown: _ClassVar[AttributeType.Type]
        kDepartment: _ClassVar[AttributeType.Type]
        kCity: _ClassVar[AttributeType.Type]
        kCountry: _ClassVar[AttributeType.Type]
        kDesignation: _ClassVar[AttributeType.Type]
        kDisplayNamePrefixAlphabet: _ClassVar[AttributeType.Type]
        kMailboxType: _ClassVar[AttributeType.Type]
        kCustom: _ClassVar[AttributeType.Type]
        kDataLocationCode: _ClassVar[AttributeType.Type]
    kUnknown: AttributeType.Type
    kDepartment: AttributeType.Type
    kCity: AttributeType.Type
    kCountry: AttributeType.Type
    kDesignation: AttributeType.Type
    kDisplayNamePrefixAlphabet: AttributeType.Type
    kMailboxType: AttributeType.Type
    kCustom: AttributeType.Type
    kDataLocationCode: AttributeType.Type
    def __init__(self) -> None: ...
