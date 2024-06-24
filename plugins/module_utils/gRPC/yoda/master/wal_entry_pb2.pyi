from yoda.base import reports_pb2 as _reports_pb2
from yoda.master import librarian_migration_pb2 as _librarian_migration_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TaskDetails(_message.Message):
    __slots__ = ("task_id", "pending_sub_task_id_vec", "report", "completed")
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    PENDING_SUB_TASK_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    REPORT_FIELD_NUMBER: _ClassVar[int]
    COMPLETED_FIELD_NUMBER: _ClassVar[int]
    task_id: int
    pending_sub_task_id_vec: _containers.RepeatedScalarFieldContainer[int]
    report: _reports_pb2.YodaReport
    completed: bool
    def __init__(self, task_id: _Optional[int] = ..., pending_sub_task_id_vec: _Optional[_Iterable[int]] = ..., report: _Optional[_Union[_reports_pb2.YodaReport, _Mapping]] = ..., completed: bool = ...) -> None: ...

class WalRecord(_message.Message):
    __slots__ = ("librarian_migration_stats", "task_vec")
    LIBRARIAN_MIGRATION_STATS_FIELD_NUMBER: _ClassVar[int]
    TASK_VEC_FIELD_NUMBER: _ClassVar[int]
    librarian_migration_stats: _librarian_migration_pb2.LibrarianMigrationStats
    task_vec: _containers.RepeatedCompositeFieldContainer[TaskDetails]
    def __init__(self, librarian_migration_stats: _Optional[_Union[_librarian_migration_pb2.LibrarianMigrationStats, _Mapping]] = ..., task_vec: _Optional[_Iterable[_Union[TaskDetails, _Mapping]]] = ...) -> None: ...
