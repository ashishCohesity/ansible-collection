from magneto.api import magneto_external_base_pb2 as _magneto_external_base_pb2
from util.base import universal_id_pb2 as _universal_id_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MagnetoObjectType(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kBackupJob: _ClassVar[MagnetoObjectType.Type]
        kProtectionPolicy: _ClassVar[MagnetoObjectType.Type]
        kEntity: _ClassVar[MagnetoObjectType.Type]
        kBackupRun: _ClassVar[MagnetoObjectType.Type]
        kCopyRun: _ClassVar[MagnetoObjectType.Type]
        kRestoreTask: _ClassVar[MagnetoObjectType.Type]
        kObjectBackup: _ClassVar[MagnetoObjectType.Type]
        kObjectSnapshot: _ClassVar[MagnetoObjectType.Type]
        kObjectSnapshotCopy: _ClassVar[MagnetoObjectType.Type]
    kBackupJob: MagnetoObjectType.Type
    kProtectionPolicy: MagnetoObjectType.Type
    kEntity: MagnetoObjectType.Type
    kBackupRun: MagnetoObjectType.Type
    kCopyRun: MagnetoObjectType.Type
    kRestoreTask: MagnetoObjectType.Type
    kObjectBackup: MagnetoObjectType.Type
    kObjectSnapshot: MagnetoObjectType.Type
    kObjectSnapshotCopy: MagnetoObjectType.Type
    def __init__(self) -> None: ...

class MagnetoObjectId(_message.Message):
    __slots__ = ("backup_job_id", "protection_policy_id", "entity_id", "backup_run_id", "copy_run_id", "restore_task_id", "object_backup_id", "object_snapshot_id", "object_copy_snapshot_id")
    class BackupJobId(_message.Message):
        __slots__ = ("job_uid",)
        JOB_UID_FIELD_NUMBER: _ClassVar[int]
        job_uid: _universal_id_pb2.UniversalIdProto
        def __init__(self, job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ...) -> None: ...
    class ProtectionPolicyId(_message.Message):
        __slots__ = ("id",)
        ID_FIELD_NUMBER: _ClassVar[int]
        id: str
        def __init__(self, id: _Optional[str] = ...) -> None: ...
    class EntityId(_message.Message):
        __slots__ = ("id", "is_replica")
        ID_FIELD_NUMBER: _ClassVar[int]
        IS_REPLICA_FIELD_NUMBER: _ClassVar[int]
        id: int
        is_replica: bool
        def __init__(self, id: _Optional[int] = ..., is_replica: bool = ...) -> None: ...
    class BackupRunId(_message.Message):
        __slots__ = ("job_uid", "run_start_time_usecs")
        JOB_UID_FIELD_NUMBER: _ClassVar[int]
        RUN_START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
        job_uid: _universal_id_pb2.UniversalIdProto
        run_start_time_usecs: int
        def __init__(self, job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., run_start_time_usecs: _Optional[int] = ...) -> None: ...
    class CopyRunId(_message.Message):
        __slots__ = ("job_uid", "run_start_time_usecs", "start_time_usecs")
        JOB_UID_FIELD_NUMBER: _ClassVar[int]
        RUN_START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
        START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
        job_uid: _universal_id_pb2.UniversalIdProto
        run_start_time_usecs: int
        start_time_usecs: int
        def __init__(self, job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., run_start_time_usecs: _Optional[int] = ..., start_time_usecs: _Optional[int] = ...) -> None: ...
    class ObjectBackupId(_message.Message):
        __slots__ = ("entity_id", "backup_spec_uid", "action_key")
        ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
        BACKUP_SPEC_UID_FIELD_NUMBER: _ClassVar[int]
        ACTION_KEY_FIELD_NUMBER: _ClassVar[int]
        entity_id: MagnetoObjectId.EntityId
        backup_spec_uid: _universal_id_pb2.UniversalIdProto
        action_key: _magneto_external_base_pb2.ObjectActionKey
        def __init__(self, entity_id: _Optional[_Union[MagnetoObjectId.EntityId, _Mapping]] = ..., backup_spec_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., action_key: _Optional[_Union[_magneto_external_base_pb2.ObjectActionKey, _Mapping]] = ...) -> None: ...
    class ObjectSnapshotId(_message.Message):
        __slots__ = ("object_backup_id", "snapshot_start_time_usecs")
        OBJECT_BACKUP_ID_FIELD_NUMBER: _ClassVar[int]
        SNAPSHOT_START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
        object_backup_id: MagnetoObjectId.ObjectBackupId
        snapshot_start_time_usecs: int
        def __init__(self, object_backup_id: _Optional[_Union[MagnetoObjectId.ObjectBackupId, _Mapping]] = ..., snapshot_start_time_usecs: _Optional[int] = ...) -> None: ...
    class ObjectCopySnapshotId(_message.Message):
        __slots__ = ("object_snapshot_id", "copy_start_time_usecs")
        OBJECT_SNAPSHOT_ID_FIELD_NUMBER: _ClassVar[int]
        COPY_START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
        object_snapshot_id: MagnetoObjectId.ObjectSnapshotId
        copy_start_time_usecs: int
        def __init__(self, object_snapshot_id: _Optional[_Union[MagnetoObjectId.ObjectSnapshotId, _Mapping]] = ..., copy_start_time_usecs: _Optional[int] = ...) -> None: ...
    class RestoreTaskId(_message.Message):
        __slots__ = ("task_id",)
        TASK_ID_FIELD_NUMBER: _ClassVar[int]
        task_id: int
        def __init__(self, task_id: _Optional[int] = ...) -> None: ...
    BACKUP_JOB_ID_FIELD_NUMBER: _ClassVar[int]
    PROTECTION_POLICY_ID_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    BACKUP_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    COPY_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    RESTORE_TASK_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_BACKUP_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_SNAPSHOT_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_COPY_SNAPSHOT_ID_FIELD_NUMBER: _ClassVar[int]
    backup_job_id: MagnetoObjectId.BackupJobId
    protection_policy_id: MagnetoObjectId.ProtectionPolicyId
    entity_id: MagnetoObjectId.EntityId
    backup_run_id: MagnetoObjectId.BackupRunId
    copy_run_id: MagnetoObjectId.CopyRunId
    restore_task_id: MagnetoObjectId.RestoreTaskId
    object_backup_id: MagnetoObjectId.ObjectBackupId
    object_snapshot_id: MagnetoObjectId.ObjectSnapshotId
    object_copy_snapshot_id: MagnetoObjectId.ObjectCopySnapshotId
    def __init__(self, backup_job_id: _Optional[_Union[MagnetoObjectId.BackupJobId, _Mapping]] = ..., protection_policy_id: _Optional[_Union[MagnetoObjectId.ProtectionPolicyId, _Mapping]] = ..., entity_id: _Optional[_Union[MagnetoObjectId.EntityId, _Mapping]] = ..., backup_run_id: _Optional[_Union[MagnetoObjectId.BackupRunId, _Mapping]] = ..., copy_run_id: _Optional[_Union[MagnetoObjectId.CopyRunId, _Mapping]] = ..., restore_task_id: _Optional[_Union[MagnetoObjectId.RestoreTaskId, _Mapping]] = ..., object_backup_id: _Optional[_Union[MagnetoObjectId.ObjectBackupId, _Mapping]] = ..., object_snapshot_id: _Optional[_Union[MagnetoObjectId.ObjectSnapshotId, _Mapping]] = ..., object_copy_snapshot_id: _Optional[_Union[MagnetoObjectId.ObjectCopySnapshotId, _Mapping]] = ...) -> None: ...

class MagnetoChangedObjectProto(_message.Message):
    __slots__ = ("change_id", "object_vec", "change_publish_time_usecs")
    class ChangedObject(_message.Message):
        __slots__ = ("type", "object_id")
        TYPE_FIELD_NUMBER: _ClassVar[int]
        OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
        type: MagnetoObjectType.Type
        object_id: MagnetoObjectId
        def __init__(self, type: _Optional[_Union[MagnetoObjectType.Type, str]] = ..., object_id: _Optional[_Union[MagnetoObjectId, _Mapping]] = ...) -> None: ...
    CHANGE_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_VEC_FIELD_NUMBER: _ClassVar[int]
    CHANGE_PUBLISH_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    change_id: int
    object_vec: _containers.RepeatedCompositeFieldContainer[MagnetoChangedObjectProto.ChangedObject]
    change_publish_time_usecs: int
    def __init__(self, change_id: _Optional[int] = ..., object_vec: _Optional[_Iterable[_Union[MagnetoChangedObjectProto.ChangedObject, _Mapping]]] = ..., change_publish_time_usecs: _Optional[int] = ...) -> None: ...
