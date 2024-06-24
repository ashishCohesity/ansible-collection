from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class BackupJobTaskStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kWaitingForSnapshot: _ClassVar[BackupJobTaskStatus]
    kReadyToSchedule: _ClassVar[BackupJobTaskStatus]
    kProgressMonitorCreated: _ClassVar[BackupJobTaskStatus]
    kAdmitted: _ClassVar[BackupJobTaskStatus]
    kFinishing: _ClassVar[BackupJobTaskStatus]
    kFinished: _ClassVar[BackupJobTaskStatus]
    kCancelled: _ClassVar[BackupJobTaskStatus]

class TaskStateInScribeSetting(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kDisabled: _ClassVar[TaskStateInScribeSetting]
    kEnabled: _ClassVar[TaskStateInScribeSetting]
    kUnsupportedInMasterOp: _ClassVar[TaskStateInScribeSetting]
    kDisabledDueToScribeRowConstraint: _ClassVar[TaskStateInScribeSetting]
kWaitingForSnapshot: BackupJobTaskStatus
kReadyToSchedule: BackupJobTaskStatus
kProgressMonitorCreated: BackupJobTaskStatus
kAdmitted: BackupJobTaskStatus
kFinishing: BackupJobTaskStatus
kFinished: BackupJobTaskStatus
kCancelled: BackupJobTaskStatus
kDisabled: TaskStateInScribeSetting
kEnabled: TaskStateInScribeSetting
kUnsupportedInMasterOp: TaskStateInScribeSetting
kDisabledDueToScribeRowConstraint: TaskStateInScribeSetting

class StorageSnapshotsTaskStatus(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kStarted: _ClassVar[StorageSnapshotsTaskStatus.Type]
        kPreProcessingDone: _ClassVar[StorageSnapshotsTaskStatus.Type]
        kAdmitted: _ClassVar[StorageSnapshotsTaskStatus.Type]
        kFetchedStorageInfo: _ClassVar[StorageSnapshotsTaskStatus.Type]
        kGroupsCreated: _ClassVar[StorageSnapshotsTaskStatus.Type]
        kGroupSnapshotTasksCreated: _ClassVar[StorageSnapshotsTaskStatus.Type]
        kFinished: _ClassVar[StorageSnapshotsTaskStatus.Type]
        kCancelled: _ClassVar[StorageSnapshotsTaskStatus.Type]
    kStarted: StorageSnapshotsTaskStatus.Type
    kPreProcessingDone: StorageSnapshotsTaskStatus.Type
    kAdmitted: StorageSnapshotsTaskStatus.Type
    kFetchedStorageInfo: StorageSnapshotsTaskStatus.Type
    kGroupsCreated: StorageSnapshotsTaskStatus.Type
    kGroupSnapshotTasksCreated: StorageSnapshotsTaskStatus.Type
    kFinished: StorageSnapshotsTaskStatus.Type
    kCancelled: StorageSnapshotsTaskStatus.Type
    def __init__(self) -> None: ...

class GroupSnapshotTaskStatus(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kStarted: _ClassVar[GroupSnapshotTaskStatus.Type]
        kPreProcessingDone: _ClassVar[GroupSnapshotTaskStatus.Type]
        kAdmitted: _ClassVar[GroupSnapshotTaskStatus.Type]
        kGroupSnapshotTaken: _ClassVar[GroupSnapshotTaskStatus.Type]
        kNotifiedBackupTasks: _ClassVar[GroupSnapshotTaskStatus.Type]
        kTeardownTaskCreated: _ClassVar[GroupSnapshotTaskStatus.Type]
        kFinished: _ClassVar[GroupSnapshotTaskStatus.Type]
        kCancelled: _ClassVar[GroupSnapshotTaskStatus.Type]
    kStarted: GroupSnapshotTaskStatus.Type
    kPreProcessingDone: GroupSnapshotTaskStatus.Type
    kAdmitted: GroupSnapshotTaskStatus.Type
    kGroupSnapshotTaken: GroupSnapshotTaskStatus.Type
    kNotifiedBackupTasks: GroupSnapshotTaskStatus.Type
    kTeardownTaskCreated: GroupSnapshotTaskStatus.Type
    kFinished: GroupSnapshotTaskStatus.Type
    kCancelled: GroupSnapshotTaskStatus.Type
    def __init__(self) -> None: ...

class TeardownGroupSnapshotTaskStatus(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kStarted: _ClassVar[TeardownGroupSnapshotTaskStatus.Type]
        kPreProcessingDone: _ClassVar[TeardownGroupSnapshotTaskStatus.Type]
        kAdmitted: _ClassVar[TeardownGroupSnapshotTaskStatus.Type]
        kSlaveTaskFinished: _ClassVar[TeardownGroupSnapshotTaskStatus.Type]
        kFinished: _ClassVar[TeardownGroupSnapshotTaskStatus.Type]
    kStarted: TeardownGroupSnapshotTaskStatus.Type
    kPreProcessingDone: TeardownGroupSnapshotTaskStatus.Type
    kAdmitted: TeardownGroupSnapshotTaskStatus.Type
    kSlaveTaskFinished: TeardownGroupSnapshotTaskStatus.Type
    kFinished: TeardownGroupSnapshotTaskStatus.Type
    def __init__(self) -> None: ...

class CancellationReason(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kUserInitiated: _ClassVar[CancellationReason.Type]
        kDeadlineExceeded: _ClassVar[CancellationReason.Type]
        kMissedAdmissionWindow: _ClassVar[CancellationReason.Type]
        kLateRetry: _ClassVar[CancellationReason.Type]
        kTimeoutExceeded: _ClassVar[CancellationReason.Type]
        kInMaintenanceMode: _ClassVar[CancellationReason.Type]
    kUserInitiated: CancellationReason.Type
    kDeadlineExceeded: CancellationReason.Type
    kMissedAdmissionWindow: CancellationReason.Type
    kLateRetry: CancellationReason.Type
    kTimeoutExceeded: CancellationReason.Type
    kInMaintenanceMode: CancellationReason.Type
    def __init__(self) -> None: ...

class PauseReason(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kUserInitiated: _ClassVar[PauseReason.Type]
        kBlackoutWindow: _ClassVar[PauseReason.Type]
    kUserInitiated: PauseReason.Type
    kBlackoutWindow: PauseReason.Type
    def __init__(self) -> None: ...

class ResumeReason(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kUserInitiated: _ClassVar[ResumeReason.Type]
        kBlackoutWindow: _ClassVar[ResumeReason.Type]
        kCancellationRequested: _ClassVar[ResumeReason.Type]
    kUserInitiated: ResumeReason.Type
    kBlackoutWindow: ResumeReason.Type
    kCancellationRequested: ResumeReason.Type
    def __init__(self) -> None: ...

class PauseStatus(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kRunning: _ClassVar[PauseStatus.Type]
        kPausing: _ClassVar[PauseStatus.Type]
        kPaused: _ClassVar[PauseStatus.Type]
        kResuming: _ClassVar[PauseStatus.Type]
    kRunning: PauseStatus.Type
    kPausing: PauseStatus.Type
    kPaused: PauseStatus.Type
    kResuming: PauseStatus.Type
    def __init__(self) -> None: ...

class BlackoutWindowAction(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNone: _ClassVar[BlackoutWindowAction.Type]
        kCancel: _ClassVar[BlackoutWindowAction.Type]
        kPause: _ClassVar[BlackoutWindowAction.Type]
    kNone: BlackoutWindowAction.Type
    kCancel: BlackoutWindowAction.Type
    kPause: BlackoutWindowAction.Type
    def __init__(self) -> None: ...

class RestoreTaskStatus(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kReadyToSchedule: _ClassVar[RestoreTaskStatus.Type]
        kProgressMonitorCreated: _ClassVar[RestoreTaskStatus.Type]
        kInternalViewCreated: _ClassVar[RestoreTaskStatus.Type]
        kRetrievedFromArchive: _ClassVar[RestoreTaskStatus.Type]
        kCDPViewHydrated: _ClassVar[RestoreTaskStatus.Type]
        kZipFileRequested: _ClassVar[RestoreTaskStatus.Type]
        kAdmitted: _ClassVar[RestoreTaskStatus.Type]
        kInProgress: _ClassVar[RestoreTaskStatus.Type]
        kOnHold: _ClassVar[RestoreTaskStatus.Type]
        kFinishingProgressMonitor: _ClassVar[RestoreTaskStatus.Type]
        kFinished: _ClassVar[RestoreTaskStatus.Type]
        kCancelled: _ClassVar[RestoreTaskStatus.Type]
        kCloneDestroyed: _ClassVar[RestoreTaskStatus.Type]
        kRestoreDone: _ClassVar[RestoreTaskStatus.Type]
        kFinalizing: _ClassVar[RestoreTaskStatus.Type]
    kReadyToSchedule: RestoreTaskStatus.Type
    kProgressMonitorCreated: RestoreTaskStatus.Type
    kInternalViewCreated: RestoreTaskStatus.Type
    kRetrievedFromArchive: RestoreTaskStatus.Type
    kCDPViewHydrated: RestoreTaskStatus.Type
    kZipFileRequested: RestoreTaskStatus.Type
    kAdmitted: RestoreTaskStatus.Type
    kInProgress: RestoreTaskStatus.Type
    kOnHold: RestoreTaskStatus.Type
    kFinishingProgressMonitor: RestoreTaskStatus.Type
    kFinished: RestoreTaskStatus.Type
    kCancelled: RestoreTaskStatus.Type
    kCloneDestroyed: RestoreTaskStatus.Type
    kRestoreDone: RestoreTaskStatus.Type
    kFinalizing: RestoreTaskStatus.Type
    def __init__(self) -> None: ...

class RefreshTaskStatus(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kReadyToSchedule: _ClassVar[RefreshTaskStatus.Type]
        kAdmitted: _ClassVar[RefreshTaskStatus.Type]
        kInProgress: _ClassVar[RefreshTaskStatus.Type]
        kProgressMonitorCreated: _ClassVar[RefreshTaskStatus.Type]
        kCloneDestroyed: _ClassVar[RefreshTaskStatus.Type]
        kFinishingProgressMonitor: _ClassVar[RefreshTaskStatus.Type]
        kCloneCreated: _ClassVar[RefreshTaskStatus.Type]
        kFinished: _ClassVar[RefreshTaskStatus.Type]
        kCancelled: _ClassVar[RefreshTaskStatus.Type]
    kReadyToSchedule: RefreshTaskStatus.Type
    kAdmitted: RefreshTaskStatus.Type
    kInProgress: RefreshTaskStatus.Type
    kProgressMonitorCreated: RefreshTaskStatus.Type
    kCloneDestroyed: RefreshTaskStatus.Type
    kFinishingProgressMonitor: RefreshTaskStatus.Type
    kCloneCreated: RefreshTaskStatus.Type
    kFinished: RefreshTaskStatus.Type
    kCancelled: RefreshTaskStatus.Type
    def __init__(self) -> None: ...

class RestoreJobStatus(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kStarted: _ClassVar[RestoreJobStatus.Type]
        kPreProcessingDone: _ClassVar[RestoreJobStatus.Type]
        kAdmitted: _ClassVar[RestoreJobStatus.Type]
        kRestoreTasksCreated: _ClassVar[RestoreJobStatus.Type]
        kFinished: _ClassVar[RestoreJobStatus.Type]
        kCancelled: _ClassVar[RestoreJobStatus.Type]
    kStarted: RestoreJobStatus.Type
    kPreProcessingDone: RestoreJobStatus.Type
    kAdmitted: RestoreJobStatus.Type
    kRestoreTasksCreated: RestoreJobStatus.Type
    kFinished: RestoreJobStatus.Type
    kCancelled: RestoreJobStatus.Type
    def __init__(self) -> None: ...

class DestroyClonedTaskStatus(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kReadyToSchedule: _ClassVar[DestroyClonedTaskStatus.Type]
        kAdmitted: _ClassVar[DestroyClonedTaskStatus.Type]
        kFinished: _ClassVar[DestroyClonedTaskStatus.Type]
    kReadyToSchedule: DestroyClonedTaskStatus.Type
    kAdmitted: DestroyClonedTaskStatus.Type
    kFinished: DestroyClonedTaskStatus.Type
    def __init__(self) -> None: ...

class DeactivateJobStatus(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kReadyToSchedule: _ClassVar[DeactivateJobStatus.Type]
        kAdmitted: _ClassVar[DeactivateJobStatus.Type]
        kFinished: _ClassVar[DeactivateJobStatus.Type]
    kReadyToSchedule: DeactivateJobStatus.Type
    kAdmitted: DeactivateJobStatus.Type
    kFinished: DeactivateJobStatus.Type
    def __init__(self) -> None: ...

class UpdateBackupRunTaskStatus(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kStarted: _ClassVar[UpdateBackupRunTaskStatus.Type]
        kFinished: _ClassVar[UpdateBackupRunTaskStatus.Type]
    kStarted: UpdateBackupRunTaskStatus.Type
    kFinished: UpdateBackupRunTaskStatus.Type
    def __init__(self) -> None: ...

class UpdateBackupObjectsTaskStatus(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kStarted: _ClassVar[UpdateBackupObjectsTaskStatus.Type]
        kCopyRunCreated: _ClassVar[UpdateBackupObjectsTaskStatus.Type]
        kIceboxUpdated: _ClassVar[UpdateBackupObjectsTaskStatus.Type]
        kFinished: _ClassVar[UpdateBackupObjectsTaskStatus.Type]
        kRemoteReplicaUpdated: _ClassVar[UpdateBackupObjectsTaskStatus.Type]
    kStarted: UpdateBackupObjectsTaskStatus.Type
    kCopyRunCreated: UpdateBackupObjectsTaskStatus.Type
    kIceboxUpdated: UpdateBackupObjectsTaskStatus.Type
    kFinished: UpdateBackupObjectsTaskStatus.Type
    kRemoteReplicaUpdated: UpdateBackupObjectsTaskStatus.Type
    def __init__(self) -> None: ...

class DeleteBackupJobPostProcessStatus(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kStarted: _ClassVar[DeleteBackupJobPostProcessStatus.Type]
        kFinished: _ClassVar[DeleteBackupJobPostProcessStatus.Type]
        kUDACleanupJob: _ClassVar[DeleteBackupJobPostProcessStatus.Type]
        kUDACleanupViews: _ClassVar[DeleteBackupJobPostProcessStatus.Type]
        kUDADeleteLogView: _ClassVar[DeleteBackupJobPostProcessStatus.Type]
        kUDADeleteDataView: _ClassVar[DeleteBackupJobPostProcessStatus.Type]
    kStarted: DeleteBackupJobPostProcessStatus.Type
    kFinished: DeleteBackupJobPostProcessStatus.Type
    kUDACleanupJob: DeleteBackupJobPostProcessStatus.Type
    kUDACleanupViews: DeleteBackupJobPostProcessStatus.Type
    kUDADeleteLogView: DeleteBackupJobPostProcessStatus.Type
    kUDADeleteDataView: DeleteBackupJobPostProcessStatus.Type
    def __init__(self) -> None: ...
