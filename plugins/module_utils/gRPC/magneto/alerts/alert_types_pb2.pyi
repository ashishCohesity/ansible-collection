from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AlertTypeProto(_message.Message):
    __slots__ = ("id",)
    class Id(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kBackupJobSuccess: _ClassVar[AlertTypeProto.Id]
        kBackupJobFail: _ClassVar[AlertTypeProto.Id]
        kBackupJobSlaViolated: _ClassVar[AlertTypeProto.Id]
        kBackupJobWarning: _ClassVar[AlertTypeProto.Id]
        kBackupJobCancelledBlackoutWindow: _ClassVar[AlertTypeProto.Id]
        kBackupObjectFail: _ClassVar[AlertTypeProto.Id]
        kBackupObjectSlaViolated: _ClassVar[AlertTypeProto.Id]
        kBackupObjectCancelledBlackoutWindow: _ClassVar[AlertTypeProto.Id]
        kPolicyConversion: _ClassVar[AlertTypeProto.Id]
        kArchivalJobBacklog: _ClassVar[AlertTypeProto.Id]
        kReplicationJobBacklog: _ClassVar[AlertTypeProto.Id]
        kProtectionGroupProgressingSlowly: _ClassVar[AlertTypeProto.Id]
        kReplicationTaskFailure: _ClassVar[AlertTypeProto.Id]
        kCDPDisabled: _ClassVar[AlertTypeProto.Id]
        kVMMigration: _ClassVar[AlertTypeProto.Id]
        kObjectBackupFailed: _ClassVar[AlertTypeProto.Id]
        kObjectBackupSlaViolated: _ClassVar[AlertTypeProto.Id]
        kProtectionPolicyDeleted: _ClassVar[AlertTypeProto.Id]
        kProtectionGroupDeleted: _ClassVar[AlertTypeProto.Id]
        kPolicyDatalockChanged: _ClassVar[AlertTypeProto.Id]
        kPolicyDatalockDurationChanged: _ClassVar[AlertTypeProto.Id]
        kProtectionPolicyModified: _ClassVar[AlertTypeProto.Id]
        kProtectionGroupModified: _ClassVar[AlertTypeProto.Id]
        kProtectionRunModified: _ClassVar[AlertTypeProto.Id]
        kSourceConnectivityFailure: _ClassVar[AlertTypeProto.Id]
        kCDPAlert: _ClassVar[AlertTypeProto.Id]
        kDeferSchedule: _ClassVar[AlertTypeProto.Id]
        kObjectDeletionRejected: _ClassVar[AlertTypeProto.Id]
        kAzureCEHostCachingEnabled: _ClassVar[AlertTypeProto.Id]
        kOracleMountFailure: _ClassVar[AlertTypeProto.Id]
        kProtectionServiceNotInitialized: _ClassVar[AlertTypeProto.Id]
        kNasSourceSnapshotDeletionFailed: _ClassVar[AlertTypeProto.Id]
        kIsilonChangelistCleanupFailed: _ClassVar[AlertTypeProto.Id]
        kOracleRestoreChainBreak: _ClassVar[AlertTypeProto.Id]
        kRestoreTaskFailed: _ClassVar[AlertTypeProto.Id]
        kRestoreTaskWarning: _ClassVar[AlertTypeProto.Id]
        kUnabletoReachYoda: _ClassVar[AlertTypeProto.Id]
        kUpcomingExpiryWithFailedCopies: _ClassVar[AlertTypeProto.Id]
        kOracleUnresponsiveProgressQuery: _ClassVar[AlertTypeProto.Id]
        kUpdateSecurityAuthConfigFailed: _ClassVar[AlertTypeProto.Id]
        kAgentCertIsAboutToExpire: _ClassVar[AlertTypeProto.Id]
    kBackupJobSuccess: AlertTypeProto.Id
    kBackupJobFail: AlertTypeProto.Id
    kBackupJobSlaViolated: AlertTypeProto.Id
    kBackupJobWarning: AlertTypeProto.Id
    kBackupJobCancelledBlackoutWindow: AlertTypeProto.Id
    kBackupObjectFail: AlertTypeProto.Id
    kBackupObjectSlaViolated: AlertTypeProto.Id
    kBackupObjectCancelledBlackoutWindow: AlertTypeProto.Id
    kPolicyConversion: AlertTypeProto.Id
    kArchivalJobBacklog: AlertTypeProto.Id
    kReplicationJobBacklog: AlertTypeProto.Id
    kProtectionGroupProgressingSlowly: AlertTypeProto.Id
    kReplicationTaskFailure: AlertTypeProto.Id
    kCDPDisabled: AlertTypeProto.Id
    kVMMigration: AlertTypeProto.Id
    kObjectBackupFailed: AlertTypeProto.Id
    kObjectBackupSlaViolated: AlertTypeProto.Id
    kProtectionPolicyDeleted: AlertTypeProto.Id
    kProtectionGroupDeleted: AlertTypeProto.Id
    kPolicyDatalockChanged: AlertTypeProto.Id
    kPolicyDatalockDurationChanged: AlertTypeProto.Id
    kProtectionPolicyModified: AlertTypeProto.Id
    kProtectionGroupModified: AlertTypeProto.Id
    kProtectionRunModified: AlertTypeProto.Id
    kSourceConnectivityFailure: AlertTypeProto.Id
    kCDPAlert: AlertTypeProto.Id
    kDeferSchedule: AlertTypeProto.Id
    kObjectDeletionRejected: AlertTypeProto.Id
    kAzureCEHostCachingEnabled: AlertTypeProto.Id
    kOracleMountFailure: AlertTypeProto.Id
    kProtectionServiceNotInitialized: AlertTypeProto.Id
    kNasSourceSnapshotDeletionFailed: AlertTypeProto.Id
    kIsilonChangelistCleanupFailed: AlertTypeProto.Id
    kOracleRestoreChainBreak: AlertTypeProto.Id
    kRestoreTaskFailed: AlertTypeProto.Id
    kRestoreTaskWarning: AlertTypeProto.Id
    kUnabletoReachYoda: AlertTypeProto.Id
    kUpcomingExpiryWithFailedCopies: AlertTypeProto.Id
    kOracleUnresponsiveProgressQuery: AlertTypeProto.Id
    kUpdateSecurityAuthConfigFailed: AlertTypeProto.Id
    kAgentCertIsAboutToExpire: AlertTypeProto.Id
    ID_FIELD_NUMBER: _ClassVar[int]
    id: AlertTypeProto.Id
    def __init__(self, id: _Optional[_Union[AlertTypeProto.Id, str]] = ...) -> None: ...
