from magneto.base import magneto_pb2 as _magneto_pb2
from magneto.base import env_params_pb2 as _env_params_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateSessionArg(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CreateSessionResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class QueryEntityHierarchyArg(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class QueryEntityHierarchyResult(_message.Message):
    __slots__ = ("entity_hierarchy",)
    ENTITY_HIERARCHY_FIELD_NUMBER: _ClassVar[int]
    entity_hierarchy: _magneto_pb2.EntityHierarchyProto
    def __init__(self, entity_hierarchy: _Optional[_Union[_magneto_pb2.EntityHierarchyProto, _Mapping]] = ...) -> None: ...

class GetSnapshotArg(_message.Message):
    __slots__ = ("container_id", "snapshot_name")
    CONTAINER_ID_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_NAME_FIELD_NUMBER: _ClassVar[int]
    container_id: int
    snapshot_name: str
    def __init__(self, container_id: _Optional[int] = ..., snapshot_name: _Optional[str] = ...) -> None: ...

class CreateSnapshotArg(_message.Message):
    __slots__ = ("name", "data_container_id")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DATA_CONTAINER_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    data_container_id: int
    def __init__(self, name: _Optional[str] = ..., data_container_id: _Optional[int] = ...) -> None: ...

class DeleteSnapshotArg(_message.Message):
    __slots__ = ("snapshot_id",)
    SNAPSHOT_ID_FIELD_NUMBER: _ClassVar[int]
    snapshot_id: int
    def __init__(self, snapshot_id: _Optional[int] = ...) -> None: ...

class DeleteSnapshotResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetShareArg(_message.Message):
    __slots__ = ("share_mount_path",)
    SHARE_MOUNT_PATH_FIELD_NUMBER: _ClassVar[int]
    share_mount_path: str
    def __init__(self, share_mount_path: _Optional[str] = ...) -> None: ...

class GetShareResult(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class CreateShareArg(_message.Message):
    __slots__ = ("snapshot_id", "name", "path")
    SNAPSHOT_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    snapshot_id: int
    name: str
    path: str
    def __init__(self, snapshot_id: _Optional[int] = ..., name: _Optional[str] = ..., path: _Optional[str] = ...) -> None: ...

class CreateShareResult(_message.Message):
    __slots__ = ("id", "mount_path")
    ID_FIELD_NUMBER: _ClassVar[int]
    MOUNT_PATH_FIELD_NUMBER: _ClassVar[int]
    id: int
    mount_path: str
    def __init__(self, id: _Optional[int] = ..., mount_path: _Optional[str] = ...) -> None: ...

class DeleteShareArg(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class DeleteShareResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class FetchCloudIPArg(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class FetchCloudIPResult(_message.Message):
    __slots__ = ("ip_addr",)
    IP_ADDR_FIELD_NUMBER: _ClassVar[int]
    ip_addr: str
    def __init__(self, ip_addr: _Optional[str] = ...) -> None: ...

class FetchEnodeIPsArg(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class FetchEnodeIPsResult(_message.Message):
    __slots__ = ("ip_addrs",)
    IP_ADDRS_FIELD_NUMBER: _ClassVar[int]
    ip_addrs: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, ip_addrs: _Optional[_Iterable[str]] = ...) -> None: ...

class GetJobInfoArg(_message.Message):
    __slots__ = ("job_id",)
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    job_id: int
    def __init__(self, job_id: _Optional[int] = ...) -> None: ...

class GetJobInfoResult(_message.Message):
    __slots__ = ("status", "last_error")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    LAST_ERROR_FIELD_NUMBER: _ClassVar[int]
    status: str
    last_error: str
    def __init__(self, status: _Optional[str] = ..., last_error: _Optional[str] = ...) -> None: ...
