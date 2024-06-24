from magneto.connectors.sql import sql_pb2 as _sql_pb2
from magneto.object_graph import backup_pb2 as _backup_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EntitySnapshotMetadataProto(_message.Message):
    __slots__ = ("db_snapshot_info", "clone_db_snapshot_info")
    class Snapshot(_message.Message):
        __slots__ = ("db_backup_info",)
        DB_BACKUP_INFO_FIELD_NUMBER: _ClassVar[int]
        db_backup_info: _sql_pb2.DatabaseBackupInfo
        def __init__(self, db_backup_info: _Optional[_Union[_sql_pb2.DatabaseBackupInfo, _Mapping]] = ...) -> None: ...
    class SnapshotOfClone(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    SQL_DB_SNAPSHOT_METADATA_FIELD_NUMBER: _ClassVar[int]
    sql_db_snapshot_metadata: _descriptor.FieldDescriptor
    DB_SNAPSHOT_INFO_FIELD_NUMBER: _ClassVar[int]
    CLONE_DB_SNAPSHOT_INFO_FIELD_NUMBER: _ClassVar[int]
    db_snapshot_info: EntitySnapshotMetadataProto.Snapshot
    clone_db_snapshot_info: EntitySnapshotMetadataProto.SnapshotOfClone
    def __init__(self, db_snapshot_info: _Optional[_Union[EntitySnapshotMetadataProto.Snapshot, _Mapping]] = ..., clone_db_snapshot_info: _Optional[_Union[EntitySnapshotMetadataProto.SnapshotOfClone, _Mapping]] = ...) -> None: ...
