from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class LibrarianMigrationStats(_message.Message):
    __slots__ = ("num_objects_to_migrate", "migration_started_usecs", "migration_finished_usecs", "migration_db_gc_completed", "migration_es_gc_completed")
    NUM_OBJECTS_TO_MIGRATE_FIELD_NUMBER: _ClassVar[int]
    MIGRATION_STARTED_USECS_FIELD_NUMBER: _ClassVar[int]
    MIGRATION_FINISHED_USECS_FIELD_NUMBER: _ClassVar[int]
    MIGRATION_DB_GC_COMPLETED_FIELD_NUMBER: _ClassVar[int]
    MIGRATION_ES_GC_COMPLETED_FIELD_NUMBER: _ClassVar[int]
    num_objects_to_migrate: int
    migration_started_usecs: int
    migration_finished_usecs: int
    migration_db_gc_completed: bool
    migration_es_gc_completed: bool
    def __init__(self, num_objects_to_migrate: _Optional[int] = ..., migration_started_usecs: _Optional[int] = ..., migration_finished_usecs: _Optional[int] = ..., migration_db_gc_completed: bool = ..., migration_es_gc_completed: bool = ...) -> None: ...
