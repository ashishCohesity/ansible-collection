from groot.server.master import wal_entry_pb2 as _wal_entry_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class WALEntry(_message.Message):
    __slots__ = ("task", "disk_id")
    class ServiceInfo(_message.Message):
        __slots__ = ("service_id", "epoch_id")
        SERVICE_ID_FIELD_NUMBER: _ClassVar[int]
        EPOCH_ID_FIELD_NUMBER: _ClassVar[int]
        service_id: int
        epoch_id: int
        def __init__(self, service_id: _Optional[int] = ..., epoch_id: _Optional[int] = ...) -> None: ...
    TASK_FIELD_NUMBER: _ClassVar[int]
    DISK_ID_FIELD_NUMBER: _ClassVar[int]
    task: _wal_entry_pb2.MigrationTask
    disk_id: int
    def __init__(self, task: _Optional[_Union[_wal_entry_pb2.MigrationTask, _Mapping]] = ..., disk_id: _Optional[int] = ...) -> None: ...
