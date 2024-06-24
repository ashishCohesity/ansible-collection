from magneto.base.entities import elastifile_pb2 as _elastifile_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetContainersResponse(_message.Message):
    __slots__ = ("data_containers",)
    class ContainerInfo(_message.Message):
        __slots__ = ("id", "name", "uuid", "used_capacity", "created_at", "nfs_interface", "smb_interface")
        class UsedCapacity(_message.Message):
            __slots__ = ("bytes",)
            BYTES_FIELD_NUMBER: _ClassVar[int]
            bytes: int
            def __init__(self, bytes: _Optional[int] = ...) -> None: ...
        ID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        UUID_FIELD_NUMBER: _ClassVar[int]
        USED_CAPACITY_FIELD_NUMBER: _ClassVar[int]
        CREATED_AT_FIELD_NUMBER: _ClassVar[int]
        NFS_INTERFACE_FIELD_NUMBER: _ClassVar[int]
        SMB_INTERFACE_FIELD_NUMBER: _ClassVar[int]
        id: int
        name: str
        uuid: str
        used_capacity: GetContainersResponse.ContainerInfo.UsedCapacity
        created_at: str
        nfs_interface: bool
        smb_interface: bool
        def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., uuid: _Optional[str] = ..., used_capacity: _Optional[_Union[GetContainersResponse.ContainerInfo.UsedCapacity, _Mapping]] = ..., created_at: _Optional[str] = ..., nfs_interface: bool = ..., smb_interface: bool = ...) -> None: ...
    DATA_CONTAINERS_FIELD_NUMBER: _ClassVar[int]
    data_containers: _containers.RepeatedCompositeFieldContainer[GetContainersResponse.ContainerInfo]
    def __init__(self, data_containers: _Optional[_Iterable[_Union[GetContainersResponse.ContainerInfo, _Mapping]]] = ...) -> None: ...

class CreateSessionRequest(_message.Message):
    __slots__ = ("user",)
    class UserInfo(_message.Message):
        __slots__ = ("login", "password")
        LOGIN_FIELD_NUMBER: _ClassVar[int]
        PASSWORD_FIELD_NUMBER: _ClassVar[int]
        login: str
        password: str
        def __init__(self, login: _Optional[str] = ..., password: _Optional[str] = ...) -> None: ...
    USER_FIELD_NUMBER: _ClassVar[int]
    user: CreateSessionRequest.UserInfo
    def __init__(self, user: _Optional[_Union[CreateSessionRequest.UserInfo, _Mapping]] = ...) -> None: ...

class CreateSessionResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetSnapshotResponse(_message.Message):
    __slots__ = ("snapshots",)
    SNAPSHOTS_FIELD_NUMBER: _ClassVar[int]
    snapshots: _containers.RepeatedCompositeFieldContainer[_elastifile_pb2.ElastifileSnapshotInfo]
    def __init__(self, snapshots: _Optional[_Iterable[_Union[_elastifile_pb2.ElastifileSnapshotInfo, _Mapping]]] = ...) -> None: ...

class CreateSnapshotRequest(_message.Message):
    __slots__ = ("snapshot",)
    class SnapshotInfo(_message.Message):
        __slots__ = ("name", "data_container_id")
        NAME_FIELD_NUMBER: _ClassVar[int]
        DATA_CONTAINER_ID_FIELD_NUMBER: _ClassVar[int]
        name: str
        data_container_id: int
        def __init__(self, name: _Optional[str] = ..., data_container_id: _Optional[int] = ...) -> None: ...
    SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    snapshot: CreateSnapshotRequest.SnapshotInfo
    def __init__(self, snapshot: _Optional[_Union[CreateSnapshotRequest.SnapshotInfo, _Mapping]] = ...) -> None: ...

class DeleteSnapshotResponse(_message.Message):
    __slots__ = ("job_details",)
    class JobDetails(_message.Message):
        __slots__ = ("job_id",)
        JOB_ID_FIELD_NUMBER: _ClassVar[int]
        job_id: int
        def __init__(self, job_id: _Optional[int] = ...) -> None: ...
    JOB_DETAILS_FIELD_NUMBER: _ClassVar[int]
    job_details: _containers.RepeatedCompositeFieldContainer[DeleteSnapshotResponse.JobDetails]
    def __init__(self, job_details: _Optional[_Iterable[_Union[DeleteSnapshotResponse.JobDetails, _Mapping]]] = ...) -> None: ...

class GetShareResponse(_message.Message):
    __slots__ = ("shares",)
    SHARES_FIELD_NUMBER: _ClassVar[int]
    shares: _containers.RepeatedCompositeFieldContainer[ShareResponse]
    def __init__(self, shares: _Optional[_Iterable[_Union[ShareResponse, _Mapping]]] = ...) -> None: ...

class ShareResponse(_message.Message):
    __slots__ = ("id", "uuid", "mount_path")
    ID_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    MOUNT_PATH_FIELD_NUMBER: _ClassVar[int]
    id: int
    uuid: str
    mount_path: str
    def __init__(self, id: _Optional[int] = ..., uuid: _Optional[str] = ..., mount_path: _Optional[str] = ...) -> None: ...

class CreateShareRequest(_message.Message):
    __slots__ = ("snapshot_id", "name", "path", "user_mapping")
    SNAPSHOT_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    USER_MAPPING_FIELD_NUMBER: _ClassVar[int]
    snapshot_id: int
    name: str
    path: str
    user_mapping: str
    def __init__(self, snapshot_id: _Optional[int] = ..., name: _Optional[str] = ..., path: _Optional[str] = ..., user_mapping: _Optional[str] = ...) -> None: ...

class DeleteShareResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class FetchCloudIPResponse(_message.Message):
    __slots__ = ("load_balancer_vip",)
    LOAD_BALANCER_VIP_FIELD_NUMBER: _ClassVar[int]
    load_balancer_vip: str
    def __init__(self, load_balancer_vip: _Optional[str] = ...) -> None: ...

class FetchEnodeIPsResponse(_message.Message):
    __slots__ = ("enodes",)
    class EnodeInfo(_message.Message):
        __slots__ = ("id", "name", "data_ip")
        ID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        DATA_IP_FIELD_NUMBER: _ClassVar[int]
        id: int
        name: str
        data_ip: str
        def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., data_ip: _Optional[str] = ...) -> None: ...
    ENODES_FIELD_NUMBER: _ClassVar[int]
    enodes: _containers.RepeatedCompositeFieldContainer[FetchEnodeIPsResponse.EnodeInfo]
    def __init__(self, enodes: _Optional[_Iterable[_Union[FetchEnodeIPsResponse.EnodeInfo, _Mapping]]] = ...) -> None: ...

class GetJobInfoResponse(_message.Message):
    __slots__ = ("status", "last_error")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    LAST_ERROR_FIELD_NUMBER: _ClassVar[int]
    status: str
    last_error: str
    def __init__(self, status: _Optional[str] = ..., last_error: _Optional[str] = ...) -> None: ...

class ErrorContext(_message.Message):
    __slots__ = ("type", "msg")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    MSG_FIELD_NUMBER: _ClassVar[int]
    type: str
    msg: str
    def __init__(self, type: _Optional[str] = ..., msg: _Optional[str] = ...) -> None: ...
