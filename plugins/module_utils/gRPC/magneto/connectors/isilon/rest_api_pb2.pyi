from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateSessionRequest(_message.Message):
    __slots__ = ("username", "password", "services")
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    SERVICES_FIELD_NUMBER: _ClassVar[int]
    username: str
    password: str
    services: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, username: _Optional[str] = ..., password: _Optional[str] = ..., services: _Optional[_Iterable[str]] = ...) -> None: ...

class CreateSessionResponse(_message.Message):
    __slots__ = ("timeout_absolute", "timeout_inactive", "services")
    TIMEOUT_ABSOLUTE_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_INACTIVE_FIELD_NUMBER: _ClassVar[int]
    SERVICES_FIELD_NUMBER: _ClassVar[int]
    timeout_absolute: int
    timeout_inactive: int
    services: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, timeout_absolute: _Optional[int] = ..., timeout_inactive: _Optional[int] = ..., services: _Optional[_Iterable[str]] = ...) -> None: ...

class GetSnapshotResponse(_message.Message):
    __slots__ = ("snapshots",)
    SNAPSHOTS_FIELD_NUMBER: _ClassVar[int]
    snapshots: _containers.RepeatedCompositeFieldContainer[CreateSnapshotResponse]
    def __init__(self, snapshots: _Optional[_Iterable[_Union[CreateSnapshotResponse, _Mapping]]] = ...) -> None: ...

class CreateSnapshotRequest(_message.Message):
    __slots__ = ("path", "name", "alias", "expires")
    PATH_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ALIAS_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_FIELD_NUMBER: _ClassVar[int]
    path: str
    name: str
    alias: str
    expires: int
    def __init__(self, path: _Optional[str] = ..., name: _Optional[str] = ..., alias: _Optional[str] = ..., expires: _Optional[int] = ...) -> None: ...

class CreateSnapshotResponse(_message.Message):
    __slots__ = ("name", "created", "expires", "state", "path", "id", "size")
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATED_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    name: str
    created: int
    expires: int
    state: str
    path: str
    id: int
    size: int
    def __init__(self, name: _Optional[str] = ..., created: _Optional[int] = ..., expires: _Optional[int] = ..., state: _Optional[str] = ..., path: _Optional[str] = ..., id: _Optional[int] = ..., size: _Optional[int] = ...) -> None: ...

class ClusterConfigResponse(_message.Message):
    __slots__ = ("name", "description", "guid", "version")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    GUID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    guid: str
    version: str
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., guid: _Optional[str] = ..., version: _Optional[str] = ...) -> None: ...

class ZonesResponse(_message.Message):
    __slots__ = ("zones",)
    class Zone(_message.Message):
        __slots__ = ("id", "zone_id", "name", "path", "groupnet")
        ID_FIELD_NUMBER: _ClassVar[int]
        ZONE_ID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        PATH_FIELD_NUMBER: _ClassVar[int]
        GROUPNET_FIELD_NUMBER: _ClassVar[int]
        id: str
        zone_id: int
        name: str
        path: str
        groupnet: str
        def __init__(self, id: _Optional[str] = ..., zone_id: _Optional[int] = ..., name: _Optional[str] = ..., path: _Optional[str] = ..., groupnet: _Optional[str] = ...) -> None: ...
    ZONES_FIELD_NUMBER: _ClassVar[int]
    zones: _containers.RepeatedCompositeFieldContainer[ZonesResponse.Zone]
    def __init__(self, zones: _Optional[_Iterable[_Union[ZonesResponse.Zone, _Mapping]]] = ...) -> None: ...

class SmbSharesResponse(_message.Message):
    __slots__ = ("shares",)
    class SmbShare(_message.Message):
        __slots__ = ("path", "id", "zid", "description", "name")
        PATH_FIELD_NUMBER: _ClassVar[int]
        ID_FIELD_NUMBER: _ClassVar[int]
        ZID_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        path: str
        id: str
        zid: int
        description: str
        name: str
        def __init__(self, path: _Optional[str] = ..., id: _Optional[str] = ..., zid: _Optional[int] = ..., description: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...
    SHARES_FIELD_NUMBER: _ClassVar[int]
    shares: _containers.RepeatedCompositeFieldContainer[SmbSharesResponse.SmbShare]
    def __init__(self, shares: _Optional[_Iterable[_Union[SmbSharesResponse.SmbShare, _Mapping]]] = ...) -> None: ...

class NfsExportsResponse(_message.Message):
    __slots__ = ("exports",)
    class NfsExport(_message.Message):
        __slots__ = ("id", "paths", "zone", "description", "root_clients", "read_only_clients", "read_write_clients", "allow_mounting_subdirs")
        ID_FIELD_NUMBER: _ClassVar[int]
        PATHS_FIELD_NUMBER: _ClassVar[int]
        ZONE_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        ROOT_CLIENTS_FIELD_NUMBER: _ClassVar[int]
        READ_ONLY_CLIENTS_FIELD_NUMBER: _ClassVar[int]
        READ_WRITE_CLIENTS_FIELD_NUMBER: _ClassVar[int]
        ALLOW_MOUNTING_SUBDIRS_FIELD_NUMBER: _ClassVar[int]
        id: int
        paths: _containers.RepeatedScalarFieldContainer[str]
        zone: str
        description: str
        root_clients: _containers.RepeatedScalarFieldContainer[str]
        read_only_clients: _containers.RepeatedScalarFieldContainer[str]
        read_write_clients: _containers.RepeatedScalarFieldContainer[str]
        allow_mounting_subdirs: bool
        def __init__(self, id: _Optional[int] = ..., paths: _Optional[_Iterable[str]] = ..., zone: _Optional[str] = ..., description: _Optional[str] = ..., root_clients: _Optional[_Iterable[str]] = ..., read_only_clients: _Optional[_Iterable[str]] = ..., read_write_clients: _Optional[_Iterable[str]] = ..., allow_mounting_subdirs: bool = ...) -> None: ...
    EXPORTS_FIELD_NUMBER: _ClassVar[int]
    exports: _containers.RepeatedCompositeFieldContainer[NfsExportsResponse.NfsExport]
    def __init__(self, exports: _Optional[_Iterable[_Union[NfsExportsResponse.NfsExport, _Mapping]]] = ...) -> None: ...

class CreateJobRequest(_message.Message):
    __slots__ = ("type", "changelistcreate_params")
    class ChangelistRequest(_message.Message):
        __slots__ = ("newer_snapid", "older_snapid")
        NEWER_SNAPID_FIELD_NUMBER: _ClassVar[int]
        OLDER_SNAPID_FIELD_NUMBER: _ClassVar[int]
        newer_snapid: int
        older_snapid: int
        def __init__(self, newer_snapid: _Optional[int] = ..., older_snapid: _Optional[int] = ...) -> None: ...
    TYPE_FIELD_NUMBER: _ClassVar[int]
    CHANGELISTCREATE_PARAMS_FIELD_NUMBER: _ClassVar[int]
    type: str
    changelistcreate_params: CreateJobRequest.ChangelistRequest
    def __init__(self, type: _Optional[str] = ..., changelistcreate_params: _Optional[_Union[CreateJobRequest.ChangelistRequest, _Mapping]] = ...) -> None: ...

class CreateJobResponse(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class GetJobInfoRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class GetJobInfoResponse(_message.Message):
    __slots__ = ("jobs",)
    class JobInfo(_message.Message):
        __slots__ = ("id", "type", "description", "create_time_secs", "start_time_secs", "end_time_secs", "state", "progress")
        ID_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        CREATE_TIME_SECS_FIELD_NUMBER: _ClassVar[int]
        START_TIME_SECS_FIELD_NUMBER: _ClassVar[int]
        END_TIME_SECS_FIELD_NUMBER: _ClassVar[int]
        STATE_FIELD_NUMBER: _ClassVar[int]
        PROGRESS_FIELD_NUMBER: _ClassVar[int]
        id: int
        type: str
        description: str
        create_time_secs: int
        start_time_secs: int
        end_time_secs: int
        state: str
        progress: str
        def __init__(self, id: _Optional[int] = ..., type: _Optional[str] = ..., description: _Optional[str] = ..., create_time_secs: _Optional[int] = ..., start_time_secs: _Optional[int] = ..., end_time_secs: _Optional[int] = ..., state: _Optional[str] = ..., progress: _Optional[str] = ...) -> None: ...
    JOBS_FIELD_NUMBER: _ClassVar[int]
    jobs: _containers.RepeatedCompositeFieldContainer[GetJobInfoResponse.JobInfo]
    def __init__(self, jobs: _Optional[_Iterable[_Union[GetJobInfoResponse.JobInfo, _Mapping]]] = ...) -> None: ...

class CancelJobRequest(_message.Message):
    __slots__ = ("state",)
    STATE_FIELD_NUMBER: _ClassVar[int]
    state: str
    def __init__(self, state: _Optional[str] = ...) -> None: ...

class CancelJobResponse(_message.Message):
    __slots__ = ("errors",)
    class error(_message.Message):
        __slots__ = ("code", "message")
        CODE_FIELD_NUMBER: _ClassVar[int]
        MESSAGE_FIELD_NUMBER: _ClassVar[int]
        code: str
        message: str
        def __init__(self, code: _Optional[str] = ..., message: _Optional[str] = ...) -> None: ...
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    errors: _containers.RepeatedCompositeFieldContainer[CancelJobResponse.error]
    def __init__(self, errors: _Optional[_Iterable[_Union[CancelJobResponse.error, _Mapping]]] = ...) -> None: ...

class GetInfoOrDeleteChangelistRequest(_message.Message):
    __slots__ = ("older_snapid", "newer_snapid")
    OLDER_SNAPID_FIELD_NUMBER: _ClassVar[int]
    NEWER_SNAPID_FIELD_NUMBER: _ClassVar[int]
    older_snapid: int
    newer_snapid: int
    def __init__(self, older_snapid: _Optional[int] = ..., newer_snapid: _Optional[int] = ...) -> None: ...

class GetChangelistInfoResponse(_message.Message):
    __slots__ = ("num_entries",)
    NUM_ENTRIES_FIELD_NUMBER: _ClassVar[int]
    num_entries: int
    def __init__(self, num_entries: _Optional[int] = ...) -> None: ...

class GetChangelistRequest(_message.Message):
    __slots__ = ("older_snapid", "newer_snapid", "resume")
    OLDER_SNAPID_FIELD_NUMBER: _ClassVar[int]
    NEWER_SNAPID_FIELD_NUMBER: _ClassVar[int]
    RESUME_FIELD_NUMBER: _ClassVar[int]
    older_snapid: int
    newer_snapid: int
    resume: str
    def __init__(self, older_snapid: _Optional[int] = ..., newer_snapid: _Optional[int] = ..., resume: _Optional[str] = ...) -> None: ...

class GetChangelistResponse(_message.Message):
    __slots__ = ("entries", "resume", "size")
    class ChangeEntry(_message.Message):
        __slots__ = ("path", "id")
        PATH_FIELD_NUMBER: _ClassVar[int]
        ID_FIELD_NUMBER: _ClassVar[int]
        path: str
        id: int
        def __init__(self, path: _Optional[str] = ..., id: _Optional[int] = ...) -> None: ...
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    RESUME_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    entries: _containers.RepeatedCompositeFieldContainer[GetChangelistResponse.ChangeEntry]
    resume: str
    size: int
    def __init__(self, entries: _Optional[_Iterable[_Union[GetChangelistResponse.ChangeEntry, _Mapping]]] = ..., resume: _Optional[str] = ..., size: _Optional[int] = ...) -> None: ...

class NetworkInterfacesResponse(_message.Message):
    __slots__ = ("interfaces",)
    class NetworkInterface(_message.Message):
        __slots__ = ("id", "ip_addrs", "status", "lnn", "name", "owners")
        class Owner(_message.Message):
            __slots__ = ("groupnet",)
            GROUPNET_FIELD_NUMBER: _ClassVar[int]
            groupnet: str
            def __init__(self, groupnet: _Optional[str] = ...) -> None: ...
        ID_FIELD_NUMBER: _ClassVar[int]
        IP_ADDRS_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        LNN_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        OWNERS_FIELD_NUMBER: _ClassVar[int]
        id: str
        ip_addrs: _containers.RepeatedScalarFieldContainer[str]
        status: str
        lnn: int
        name: str
        owners: _containers.RepeatedCompositeFieldContainer[NetworkInterfacesResponse.NetworkInterface.Owner]
        def __init__(self, id: _Optional[str] = ..., ip_addrs: _Optional[_Iterable[str]] = ..., status: _Optional[str] = ..., lnn: _Optional[int] = ..., name: _Optional[str] = ..., owners: _Optional[_Iterable[_Union[NetworkInterfacesResponse.NetworkInterface.Owner, _Mapping]]] = ...) -> None: ...
    INTERFACES_FIELD_NUMBER: _ClassVar[int]
    interfaces: _containers.RepeatedCompositeFieldContainer[NetworkInterfacesResponse.NetworkInterface]
    def __init__(self, interfaces: _Optional[_Iterable[_Union[NetworkInterfacesResponse.NetworkInterface, _Mapping]]] = ...) -> None: ...

class NetworkPoolsResponse(_message.Message):
    __slots__ = ("pools",)
    class Pool(_message.Message):
        __slots__ = ("access_zone", "address_type", "alloc_method", "groupnet", "interfaces", "id", "name", "ranges", "sc_dns_zone", "subnet")
        class Interface(_message.Message):
            __slots__ = ("id", "lnn")
            ID_FIELD_NUMBER: _ClassVar[int]
            LNN_FIELD_NUMBER: _ClassVar[int]
            id: str
            lnn: int
            def __init__(self, id: _Optional[str] = ..., lnn: _Optional[int] = ...) -> None: ...
        class Range(_message.Message):
            __slots__ = ("high", "low")
            HIGH_FIELD_NUMBER: _ClassVar[int]
            LOW_FIELD_NUMBER: _ClassVar[int]
            high: str
            low: str
            def __init__(self, high: _Optional[str] = ..., low: _Optional[str] = ...) -> None: ...
        ACCESS_ZONE_FIELD_NUMBER: _ClassVar[int]
        ADDRESS_TYPE_FIELD_NUMBER: _ClassVar[int]
        ALLOC_METHOD_FIELD_NUMBER: _ClassVar[int]
        GROUPNET_FIELD_NUMBER: _ClassVar[int]
        INTERFACES_FIELD_NUMBER: _ClassVar[int]
        ID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        RANGES_FIELD_NUMBER: _ClassVar[int]
        SC_DNS_ZONE_FIELD_NUMBER: _ClassVar[int]
        SUBNET_FIELD_NUMBER: _ClassVar[int]
        access_zone: str
        address_type: str
        alloc_method: str
        groupnet: str
        interfaces: _containers.RepeatedCompositeFieldContainer[NetworkPoolsResponse.Pool.Interface]
        id: str
        name: str
        ranges: _containers.RepeatedCompositeFieldContainer[NetworkPoolsResponse.Pool.Range]
        sc_dns_zone: str
        subnet: str
        def __init__(self, access_zone: _Optional[str] = ..., address_type: _Optional[str] = ..., alloc_method: _Optional[str] = ..., groupnet: _Optional[str] = ..., interfaces: _Optional[_Iterable[_Union[NetworkPoolsResponse.Pool.Interface, _Mapping]]] = ..., id: _Optional[str] = ..., name: _Optional[str] = ..., ranges: _Optional[_Iterable[_Union[NetworkPoolsResponse.Pool.Range, _Mapping]]] = ..., sc_dns_zone: _Optional[str] = ..., subnet: _Optional[str] = ...) -> None: ...
    POOLS_FIELD_NUMBER: _ClassVar[int]
    pools: _containers.RepeatedCompositeFieldContainer[NetworkPoolsResponse.Pool]
    def __init__(self, pools: _Optional[_Iterable[_Union[NetworkPoolsResponse.Pool, _Mapping]]] = ...) -> None: ...

class NfsExportsRequest(_message.Message):
    __slots__ = ("allow_mounting_subdirs", "root_clients", "read_only_clients", "read_write_clients")
    ALLOW_MOUNTING_SUBDIRS_FIELD_NUMBER: _ClassVar[int]
    ROOT_CLIENTS_FIELD_NUMBER: _ClassVar[int]
    READ_ONLY_CLIENTS_FIELD_NUMBER: _ClassVar[int]
    READ_WRITE_CLIENTS_FIELD_NUMBER: _ClassVar[int]
    allow_mounting_subdirs: bool
    root_clients: _containers.RepeatedScalarFieldContainer[str]
    read_only_clients: _containers.RepeatedScalarFieldContainer[str]
    read_write_clients: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, allow_mounting_subdirs: bool = ..., root_clients: _Optional[_Iterable[str]] = ..., read_only_clients: _Optional[_Iterable[str]] = ..., read_write_clients: _Optional[_Iterable[str]] = ...) -> None: ...

class ClusterVersionResponse(_message.Message):
    __slots__ = ("latest",)
    LATEST_FIELD_NUMBER: _ClassVar[int]
    latest: str
    def __init__(self, latest: _Optional[str] = ...) -> None: ...

class GetRoleInfoRequest(_message.Message):
    __slots__ = ("resume",)
    RESUME_FIELD_NUMBER: _ClassVar[int]
    resume: str
    def __init__(self, resume: _Optional[str] = ...) -> None: ...

class GetRoleInfoResponse(_message.Message):
    __slots__ = ("roles", "resume", "size")
    class RoleEntry(_message.Message):
        __slots__ = ("id", "name", "members", "privileges")
        class MemberInfo(_message.Message):
            __slots__ = ("id", "name", "type")
            ID_FIELD_NUMBER: _ClassVar[int]
            NAME_FIELD_NUMBER: _ClassVar[int]
            TYPE_FIELD_NUMBER: _ClassVar[int]
            id: str
            name: str
            type: str
            def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., type: _Optional[str] = ...) -> None: ...
        class PrivilegeInfo(_message.Message):
            __slots__ = ("id", "name", "read_only")
            ID_FIELD_NUMBER: _ClassVar[int]
            NAME_FIELD_NUMBER: _ClassVar[int]
            READ_ONLY_FIELD_NUMBER: _ClassVar[int]
            id: str
            name: str
            read_only: bool
            def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., read_only: bool = ...) -> None: ...
        ID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        MEMBERS_FIELD_NUMBER: _ClassVar[int]
        PRIVILEGES_FIELD_NUMBER: _ClassVar[int]
        id: str
        name: str
        members: _containers.RepeatedCompositeFieldContainer[GetRoleInfoResponse.RoleEntry.MemberInfo]
        privileges: _containers.RepeatedCompositeFieldContainer[GetRoleInfoResponse.RoleEntry.PrivilegeInfo]
        def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., members: _Optional[_Iterable[_Union[GetRoleInfoResponse.RoleEntry.MemberInfo, _Mapping]]] = ..., privileges: _Optional[_Iterable[_Union[GetRoleInfoResponse.RoleEntry.PrivilegeInfo, _Mapping]]] = ...) -> None: ...
    ROLES_FIELD_NUMBER: _ClassVar[int]
    RESUME_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    roles: _containers.RepeatedCompositeFieldContainer[GetRoleInfoResponse.RoleEntry]
    resume: str
    size: int
    def __init__(self, roles: _Optional[_Iterable[_Union[GetRoleInfoResponse.RoleEntry, _Mapping]]] = ..., resume: _Optional[str] = ..., size: _Optional[int] = ...) -> None: ...

class ErrorContext(_message.Message):
    __slots__ = ("errors",)
    class ErrorInfo(_message.Message):
        __slots__ = ("code", "field", "msg")
        CODE_FIELD_NUMBER: _ClassVar[int]
        FIELD_FIELD_NUMBER: _ClassVar[int]
        MSG_FIELD_NUMBER: _ClassVar[int]
        code: str
        field: str
        msg: str
        def __init__(self, code: _Optional[str] = ..., field: _Optional[str] = ..., msg: _Optional[str] = ...) -> None: ...
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    errors: _containers.RepeatedCompositeFieldContainer[ErrorContext.ErrorInfo]
    def __init__(self, errors: _Optional[_Iterable[_Union[ErrorContext.ErrorInfo, _Mapping]]] = ...) -> None: ...

class AdsResponse(_message.Message):
    __slots__ = ("ads",)
    class Ads(_message.Message):
        __slots__ = ("hostname", "primary_domain")
        HOSTNAME_FIELD_NUMBER: _ClassVar[int]
        PRIMARY_DOMAIN_FIELD_NUMBER: _ClassVar[int]
        hostname: str
        primary_domain: str
        def __init__(self, hostname: _Optional[str] = ..., primary_domain: _Optional[str] = ...) -> None: ...
    ADS_FIELD_NUMBER: _ClassVar[int]
    ads: _containers.RepeatedCompositeFieldContainer[AdsResponse.Ads]
    def __init__(self, ads: _Optional[_Iterable[_Union[AdsResponse.Ads, _Mapping]]] = ...) -> None: ...
