from magneto.base import error_pb2 as _error_pb2
from magneto.master.base import enums_pb2 as _enums_pb2
from util.base import universal_id_pb2 as _universal_id_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import python_message as _python_message
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EntityBackupSpec(_message.Message):
    __slots__ = ("source_node_uid", "backup_task_uid")
    SOURCE_NODE_UID_FIELD_NUMBER: _ClassVar[int]
    BACKUP_TASK_UID_FIELD_NUMBER: _ClassVar[int]
    source_node_uid: _universal_id_pb2.UniversalIdProto
    backup_task_uid: _universal_id_pb2.UniversalIdProto
    def __init__(self, source_node_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., backup_task_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ...) -> None: ...

class EntitySnapshotMetadataProto(_message.Message):
    __slots__ = ("expiration_timestamp_usecs", "extended_expiration_timestamp_usecs", "user_label", "source_entity_uid")
    Extensions: _python_message._ExtensionDict
    EXPIRATION_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
    EXTENDED_EXPIRATION_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
    USER_LABEL_FIELD_NUMBER: _ClassVar[int]
    SOURCE_ENTITY_UID_FIELD_NUMBER: _ClassVar[int]
    expiration_timestamp_usecs: int
    extended_expiration_timestamp_usecs: int
    user_label: str
    source_entity_uid: _universal_id_pb2.UniversalIdProto
    def __init__(self, expiration_timestamp_usecs: _Optional[int] = ..., extended_expiration_timestamp_usecs: _Optional[int] = ..., user_label: _Optional[str] = ..., source_entity_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ...) -> None: ...

class TransientEntityBackupStateProto(_message.Message):
    __slots__ = ("cancellation_reason", "previous_snapshot_info", "current_snapshot_info")
    CANCELLATION_REASON_FIELD_NUMBER: _ClassVar[int]
    PREVIOUS_SNAPSHOT_INFO_FIELD_NUMBER: _ClassVar[int]
    CURRENT_SNAPSHOT_INFO_FIELD_NUMBER: _ClassVar[int]
    cancellation_reason: _enums_pb2.CancellationReason.Type
    previous_snapshot_info: EntitySnapshotMetadataProto
    current_snapshot_info: EntitySnapshotMetadataProto
    def __init__(self, cancellation_reason: _Optional[_Union[_enums_pb2.CancellationReason.Type, str]] = ..., previous_snapshot_info: _Optional[_Union[EntitySnapshotMetadataProto, _Mapping]] = ..., current_snapshot_info: _Optional[_Union[EntitySnapshotMetadataProto, _Mapping]] = ...) -> None: ...

class EntityBackupStatus(_message.Message):
    __slots__ = ("start_time_usecs", "end_time_usecs", "transient_info")
    START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    END_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    TRANSIENT_INFO_FIELD_NUMBER: _ClassVar[int]
    start_time_usecs: int
    end_time_usecs: int
    transient_info: TransientEntityBackupStateProto
    def __init__(self, start_time_usecs: _Optional[int] = ..., end_time_usecs: _Optional[int] = ..., transient_info: _Optional[_Union[TransientEntityBackupStateProto, _Mapping]] = ...) -> None: ...

class EntityBackupResult(_message.Message):
    __slots__ = ("error", "warnings", "user_message", "snapshot_node_uid")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    USER_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_NODE_UID_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    warnings: _containers.RepeatedCompositeFieldContainer[_error_pb2.ErrorProto]
    user_message: str
    snapshot_node_uid: _universal_id_pb2.UniversalIdProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., warnings: _Optional[_Iterable[_Union[_error_pb2.ErrorProto, _Mapping]]] = ..., user_message: _Optional[str] = ..., snapshot_node_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ...) -> None: ...

class EntityBackupTaskStateProto(_message.Message):
    __slots__ = ("spec", "status", "result")
    SPEC_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    spec: EntityBackupSpec
    status: EntityBackupStatus
    result: EntityBackupResult
    def __init__(self, spec: _Optional[_Union[EntityBackupSpec, _Mapping]] = ..., status: _Optional[_Union[EntityBackupStatus, _Mapping]] = ..., result: _Optional[_Union[EntityBackupResult, _Mapping]] = ...) -> None: ...
