from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AccessTokenRequest(_message.Message):
    __slots__ = ("grant_type", "client_id", "client_secret")
    GRANT_TYPE_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_SECRET_FIELD_NUMBER: _ClassVar[int]
    grant_type: str
    client_id: str
    client_secret: str
    def __init__(self, grant_type: _Optional[str] = ..., client_id: _Optional[str] = ..., client_secret: _Optional[str] = ...) -> None: ...

class AccessTokenResponse(_message.Message):
    __slots__ = ("access_token", "token_type", "expires_in_secs")
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    TOKEN_TYPE_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_IN_SECS_FIELD_NUMBER: _ClassVar[int]
    access_token: str
    token_type: str
    expires_in_secs: int
    def __init__(self, access_token: _Optional[str] = ..., token_type: _Optional[str] = ..., expires_in_secs: _Optional[int] = ...) -> None: ...

class CreateSnapmirrorRelationshipRequest(_message.Message):
    __slots__ = ("src_endpoint", "dst_endpoint", "restore", "policy")
    SRC_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    DST_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    RESTORE_FIELD_NUMBER: _ClassVar[int]
    POLICY_FIELD_NUMBER: _ClassVar[int]
    src_endpoint: SnapmirrorEndpoint
    dst_endpoint: SnapmirrorEndpoint
    restore: bool
    policy: Policy
    def __init__(self, src_endpoint: _Optional[_Union[SnapmirrorEndpoint, _Mapping]] = ..., dst_endpoint: _Optional[_Union[SnapmirrorEndpoint, _Mapping]] = ..., restore: bool = ..., policy: _Optional[_Union[Policy, _Mapping]] = ...) -> None: ...

class CreateSnapmirrorRelationshipResponse(_message.Message):
    __slots__ = ("job",)
    JOB_FIELD_NUMBER: _ClassVar[int]
    job: JobLink
    def __init__(self, job: _Optional[_Union[JobLink, _Mapping]] = ...) -> None: ...

class SnapmirrorTransferInfoResponse(_message.Message):
    __slots__ = ("uuid", "snapshot", "state", "bytes_transferred", "relationship_info")
    class RelationshipInfo(_message.Message):
        __slots__ = ("uuid",)
        UUID_FIELD_NUMBER: _ClassVar[int]
        uuid: str
        def __init__(self, uuid: _Optional[str] = ...) -> None: ...
    UUID_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    BYTES_TRANSFERRED_FIELD_NUMBER: _ClassVar[int]
    RELATIONSHIP_INFO_FIELD_NUMBER: _ClassVar[int]
    uuid: str
    snapshot: str
    state: str
    bytes_transferred: int
    relationship_info: SnapmirrorTransferInfoResponse.RelationshipInfo
    def __init__(self, uuid: _Optional[str] = ..., snapshot: _Optional[str] = ..., state: _Optional[str] = ..., bytes_transferred: _Optional[int] = ..., relationship_info: _Optional[_Union[SnapmirrorTransferInfoResponse.RelationshipInfo, _Mapping]] = ...) -> None: ...

class AbortSnapmirrorTransferRequest(_message.Message):
    __slots__ = ("state",)
    STATE_FIELD_NUMBER: _ClassVar[int]
    state: str
    def __init__(self, state: _Optional[str] = ...) -> None: ...

class CloudTarget(_message.Message):
    __slots__ = ("name", "provider_type", "container", "server", "port", "is_ssl_enabled", "snapmirror_use", "owner", "access_key", "secret_password", "svm_name", "is_certificate_validation_enabled", "uuid", "link", "ipspace")
    NAME_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_TYPE_FIELD_NUMBER: _ClassVar[int]
    CONTAINER_FIELD_NUMBER: _ClassVar[int]
    SERVER_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    IS_SSL_ENABLED_FIELD_NUMBER: _ClassVar[int]
    SNAPMIRROR_USE_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    ACCESS_KEY_FIELD_NUMBER: _ClassVar[int]
    SECRET_PASSWORD_FIELD_NUMBER: _ClassVar[int]
    SVM_NAME_FIELD_NUMBER: _ClassVar[int]
    IS_CERTIFICATE_VALIDATION_ENABLED_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    LINK_FIELD_NUMBER: _ClassVar[int]
    IPSPACE_FIELD_NUMBER: _ClassVar[int]
    name: str
    provider_type: str
    container: str
    server: str
    port: int
    is_ssl_enabled: bool
    snapmirror_use: str
    owner: str
    access_key: str
    secret_password: str
    svm_name: str
    is_certificate_validation_enabled: bool
    uuid: str
    link: SelfLink
    ipspace: str
    def __init__(self, name: _Optional[str] = ..., provider_type: _Optional[str] = ..., container: _Optional[str] = ..., server: _Optional[str] = ..., port: _Optional[int] = ..., is_ssl_enabled: bool = ..., snapmirror_use: _Optional[str] = ..., owner: _Optional[str] = ..., access_key: _Optional[str] = ..., secret_password: _Optional[str] = ..., svm_name: _Optional[str] = ..., is_certificate_validation_enabled: bool = ..., uuid: _Optional[str] = ..., link: _Optional[_Union[SelfLink, _Mapping]] = ..., ipspace: _Optional[str] = ...) -> None: ...

class ObjectStoreConfigCreateResponse(_message.Message):
    __slots__ = ("job",)
    JOB_FIELD_NUMBER: _ClassVar[int]
    job: JobLink
    def __init__(self, job: _Optional[_Union[JobLink, _Mapping]] = ...) -> None: ...

class ObjectStoreConfigGetRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ObjectStoreConfigGetResponse(_message.Message):
    __slots__ = ("num_records", "records", "link")
    NUM_RECORDS_FIELD_NUMBER: _ClassVar[int]
    RECORDS_FIELD_NUMBER: _ClassVar[int]
    LINK_FIELD_NUMBER: _ClassVar[int]
    num_records: int
    records: _containers.RepeatedCompositeFieldContainer[CloudTarget]
    link: SelfLink
    def __init__(self, num_records: _Optional[int] = ..., records: _Optional[_Iterable[_Union[CloudTarget, _Mapping]]] = ..., link: _Optional[_Union[SelfLink, _Mapping]] = ...) -> None: ...

class ObjectStoreConfigDeleteRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ObjectStoreConfigDeleteResponse(_message.Message):
    __slots__ = ("num_records", "jobs", "link")
    NUM_RECORDS_FIELD_NUMBER: _ClassVar[int]
    JOBS_FIELD_NUMBER: _ClassVar[int]
    LINK_FIELD_NUMBER: _ClassVar[int]
    num_records: int
    jobs: _containers.RepeatedCompositeFieldContainer[CloudTarget]
    link: SelfLink
    def __init__(self, num_records: _Optional[int] = ..., jobs: _Optional[_Iterable[_Union[CloudTarget, _Mapping]]] = ..., link: _Optional[_Union[SelfLink, _Mapping]] = ...) -> None: ...

class ObjectStoreConfigModifyRequest(_message.Message):
    __slots__ = ("secret_password",)
    SECRET_PASSWORD_FIELD_NUMBER: _ClassVar[int]
    secret_password: str
    def __init__(self, secret_password: _Optional[str] = ...) -> None: ...

class ObjectStoreConfigModifyResponse(_message.Message):
    __slots__ = ("job",)
    JOB_FIELD_NUMBER: _ClassVar[int]
    job: JobLink
    def __init__(self, job: _Optional[_Union[JobLink, _Mapping]] = ...) -> None: ...

class SnapmirrorRelationshipResponse(_message.Message):
    __slots__ = ("state", "is_relationship_healthy", "dst_endpoint", "uuid", "exported_snapshot", "restore", "unhealthy_relationship_reason", "transfer", "src_endpoint")
    class UnhealthyRelationshipReason(_message.Message):
        __slots__ = ("code", "msg")
        CODE_FIELD_NUMBER: _ClassVar[int]
        MSG_FIELD_NUMBER: _ClassVar[int]
        code: str
        msg: str
        def __init__(self, code: _Optional[str] = ..., msg: _Optional[str] = ...) -> None: ...
    STATE_FIELD_NUMBER: _ClassVar[int]
    IS_RELATIONSHIP_HEALTHY_FIELD_NUMBER: _ClassVar[int]
    DST_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    EXPORTED_SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    RESTORE_FIELD_NUMBER: _ClassVar[int]
    UNHEALTHY_RELATIONSHIP_REASON_FIELD_NUMBER: _ClassVar[int]
    TRANSFER_FIELD_NUMBER: _ClassVar[int]
    SRC_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    state: str
    is_relationship_healthy: bool
    dst_endpoint: SnapmirrorEndpoint
    uuid: str
    exported_snapshot: str
    restore: bool
    unhealthy_relationship_reason: _containers.RepeatedCompositeFieldContainer[SnapmirrorRelationshipResponse.UnhealthyRelationshipReason]
    transfer: Transfer
    src_endpoint: SnapmirrorEndpoint
    def __init__(self, state: _Optional[str] = ..., is_relationship_healthy: bool = ..., dst_endpoint: _Optional[_Union[SnapmirrorEndpoint, _Mapping]] = ..., uuid: _Optional[str] = ..., exported_snapshot: _Optional[str] = ..., restore: bool = ..., unhealthy_relationship_reason: _Optional[_Iterable[_Union[SnapmirrorRelationshipResponse.UnhealthyRelationshipReason, _Mapping]]] = ..., transfer: _Optional[_Union[Transfer, _Mapping]] = ..., src_endpoint: _Optional[_Union[SnapmirrorEndpoint, _Mapping]] = ...) -> None: ...

class UpdateSnapmirrorRelationshipRequest(_message.Message):
    __slots__ = ("state",)
    STATE_FIELD_NUMBER: _ClassVar[int]
    state: str
    def __init__(self, state: _Optional[str] = ...) -> None: ...

class UpdateSnapmirrorRelationshipResponse(_message.Message):
    __slots__ = ("job",)
    JOB_FIELD_NUMBER: _ClassVar[int]
    job: JobLink
    def __init__(self, job: _Optional[_Union[JobLink, _Mapping]] = ...) -> None: ...

class FilteredSnapmirrorRelationshipResponse(_message.Message):
    __slots__ = ("num_records", "record_vec")
    NUM_RECORDS_FIELD_NUMBER: _ClassVar[int]
    RECORD_VEC_FIELD_NUMBER: _ClassVar[int]
    num_records: int
    record_vec: _containers.RepeatedCompositeFieldContainer[SnapmirrorRelationshipResponse]
    def __init__(self, num_records: _Optional[int] = ..., record_vec: _Optional[_Iterable[_Union[SnapmirrorRelationshipResponse, _Mapping]]] = ...) -> None: ...

class DeleteSnapmirrorRelationshipResponse(_message.Message):
    __slots__ = ("job",)
    JOB_FIELD_NUMBER: _ClassVar[int]
    job: JobLink
    def __init__(self, job: _Optional[_Union[JobLink, _Mapping]] = ...) -> None: ...

class UpdateSnapmirrorTransferRequest(_message.Message):
    __slots__ = ("source_snapshot", "files_vec")
    SOURCE_SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    FILES_VEC_FIELD_NUMBER: _ClassVar[int]
    source_snapshot: str
    files_vec: _containers.RepeatedCompositeFieldContainer[File]
    def __init__(self, source_snapshot: _Optional[str] = ..., files_vec: _Optional[_Iterable[_Union[File, _Mapping]]] = ...) -> None: ...

class UpdateSnapmirrorTransferResponse(_message.Message):
    __slots__ = ("job",)
    JOB_FIELD_NUMBER: _ClassVar[int]
    job: JobLink
    def __init__(self, job: _Optional[_Union[JobLink, _Mapping]] = ...) -> None: ...

class FilteredSnapmirrorTransferResponse(_message.Message):
    __slots__ = ("num_records", "transfer_info")
    NUM_RECORDS_FIELD_NUMBER: _ClassVar[int]
    TRANSFER_INFO_FIELD_NUMBER: _ClassVar[int]
    num_records: int
    transfer_info: _containers.RepeatedCompositeFieldContainer[SnapmirrorTransferInfoResponse]
    def __init__(self, num_records: _Optional[int] = ..., transfer_info: _Optional[_Iterable[_Union[SnapmirrorTransferInfoResponse, _Mapping]]] = ...) -> None: ...

class ListObjectstoreEndpointSnapshotsResponse(_message.Message):
    __slots__ = ("num_snapshots", "snapshot_vec")
    NUM_SNAPSHOTS_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_VEC_FIELD_NUMBER: _ClassVar[int]
    num_snapshots: int
    snapshot_vec: _containers.RepeatedCompositeFieldContainer[Snapshot]
    def __init__(self, num_snapshots: _Optional[int] = ..., snapshot_vec: _Optional[_Iterable[_Union[Snapshot, _Mapping]]] = ...) -> None: ...

class DeleteSnapshotResponse(_message.Message):
    __slots__ = ("job",)
    JOB_FIELD_NUMBER: _ClassVar[int]
    job: JobLink
    def __init__(self, job: _Optional[_Union[JobLink, _Mapping]] = ...) -> None: ...

class DeleteObjectStoreEndpointResponse(_message.Message):
    __slots__ = ("job",)
    JOB_FIELD_NUMBER: _ClassVar[int]
    job: JobLink
    def __init__(self, job: _Optional[_Union[JobLink, _Mapping]] = ...) -> None: ...

class SnapDiffSessionRequest(_message.Message):
    __slots__ = ("application", "base_snapshot", "diff_snapshot", "restart_cookie", "report_file_attributes", "checkpoint_enabled", "file_access_protocol", "max_diffs")
    APPLICATION_FIELD_NUMBER: _ClassVar[int]
    BASE_SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    DIFF_SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    RESTART_COOKIE_FIELD_NUMBER: _ClassVar[int]
    REPORT_FILE_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    CHECKPOINT_ENABLED_FIELD_NUMBER: _ClassVar[int]
    FILE_ACCESS_PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    MAX_DIFFS_FIELD_NUMBER: _ClassVar[int]
    application: Application
    base_snapshot: Snapshot
    diff_snapshot: Snapshot
    restart_cookie: str
    report_file_attributes: bool
    checkpoint_enabled: bool
    file_access_protocol: str
    max_diffs: int
    def __init__(self, application: _Optional[_Union[Application, _Mapping]] = ..., base_snapshot: _Optional[_Union[Snapshot, _Mapping]] = ..., diff_snapshot: _Optional[_Union[Snapshot, _Mapping]] = ..., restart_cookie: _Optional[str] = ..., report_file_attributes: bool = ..., checkpoint_enabled: bool = ..., file_access_protocol: _Optional[str] = ..., max_diffs: _Optional[int] = ...) -> None: ...

class SnapDiffSessionResponse(_message.Message):
    __slots__ = ("num_records", "records")
    class Record(_message.Message):
        __slots__ = ("uuid", "handle", "base_snapshot", "diff_snapshot", "checkpoint_enabled", "file_access_protocol", "max_diffs")
        UUID_FIELD_NUMBER: _ClassVar[int]
        HANDLE_FIELD_NUMBER: _ClassVar[int]
        BASE_SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
        DIFF_SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
        CHECKPOINT_ENABLED_FIELD_NUMBER: _ClassVar[int]
        FILE_ACCESS_PROTOCOL_FIELD_NUMBER: _ClassVar[int]
        MAX_DIFFS_FIELD_NUMBER: _ClassVar[int]
        uuid: str
        handle: str
        base_snapshot: Snapshot
        diff_snapshot: Snapshot
        checkpoint_enabled: bool
        file_access_protocol: str
        max_diffs: int
        def __init__(self, uuid: _Optional[str] = ..., handle: _Optional[str] = ..., base_snapshot: _Optional[_Union[Snapshot, _Mapping]] = ..., diff_snapshot: _Optional[_Union[Snapshot, _Mapping]] = ..., checkpoint_enabled: bool = ..., file_access_protocol: _Optional[str] = ..., max_diffs: _Optional[int] = ...) -> None: ...
    NUM_RECORDS_FIELD_NUMBER: _ClassVar[int]
    RECORDS_FIELD_NUMBER: _ClassVar[int]
    num_records: int
    records: _containers.RepeatedCompositeFieldContainer[SnapDiffSessionResponse.Record]
    def __init__(self, num_records: _Optional[int] = ..., records: _Optional[_Iterable[_Union[SnapDiffSessionResponse.Record, _Mapping]]] = ...) -> None: ...

class FetchJobDetailsRequest(_message.Message):
    __slots__ = ("uuid",)
    UUID_FIELD_NUMBER: _ClassVar[int]
    uuid: str
    def __init__(self, uuid: _Optional[str] = ...) -> None: ...

class FetchJobDetailsResponse(_message.Message):
    __slots__ = ("link", "uuid", "state", "msg", "code", "description")
    LINK_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    MSG_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    link: SelfLink
    uuid: str
    state: str
    msg: str
    code: int
    description: str
    def __init__(self, link: _Optional[_Union[SelfLink, _Mapping]] = ..., uuid: _Optional[str] = ..., state: _Optional[str] = ..., msg: _Optional[str] = ..., code: _Optional[int] = ..., description: _Optional[str] = ...) -> None: ...

class SnapmirrorCreatePolicyRequest(_message.Message):
    __slots__ = ("name", "svm_name", "retention", "create_snapshot_on_source")
    NAME_FIELD_NUMBER: _ClassVar[int]
    SVM_NAME_FIELD_NUMBER: _ClassVar[int]
    RETENTION_FIELD_NUMBER: _ClassVar[int]
    CREATE_SNAPSHOT_ON_SOURCE_FIELD_NUMBER: _ClassVar[int]
    name: str
    svm_name: str
    retention: _containers.RepeatedCompositeFieldContainer[SnapmirrorRetention]
    create_snapshot_on_source: bool
    def __init__(self, name: _Optional[str] = ..., svm_name: _Optional[str] = ..., retention: _Optional[_Iterable[_Union[SnapmirrorRetention, _Mapping]]] = ..., create_snapshot_on_source: bool = ...) -> None: ...

class SnapmirrorPolicyUpdateRequest(_message.Message):
    __slots__ = ("uuid", "retention")
    UUID_FIELD_NUMBER: _ClassVar[int]
    RETENTION_FIELD_NUMBER: _ClassVar[int]
    uuid: str
    retention: _containers.RepeatedCompositeFieldContainer[SnapmirrorRetention]
    def __init__(self, uuid: _Optional[str] = ..., retention: _Optional[_Iterable[_Union[SnapmirrorRetention, _Mapping]]] = ...) -> None: ...

class SnapmirrorPolicyResponse(_message.Message):
    __slots__ = ("job",)
    JOB_FIELD_NUMBER: _ClassVar[int]
    job: JobLink
    def __init__(self, job: _Optional[_Union[JobLink, _Mapping]] = ...) -> None: ...

class SnapmirrorPolicyShowResponse(_message.Message):
    __slots__ = ("uuid", "name", "type", "retention")
    UUID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    RETENTION_FIELD_NUMBER: _ClassVar[int]
    uuid: str
    name: str
    type: str
    retention: _containers.RepeatedCompositeFieldContainer[SnapmirrorRetention]
    def __init__(self, uuid: _Optional[str] = ..., name: _Optional[str] = ..., type: _Optional[str] = ..., retention: _Optional[_Iterable[_Union[SnapmirrorRetention, _Mapping]]] = ...) -> None: ...

class SnapmirrorPolicyNameShowResponse(_message.Message):
    __slots__ = ("num_records",)
    NUM_RECORDS_FIELD_NUMBER: _ClassVar[int]
    num_records: int
    def __init__(self, num_records: _Optional[int] = ...) -> None: ...

class FetchSnapshotInstanceDetailsResponse(_message.Message):
    __slots__ = ("num_snapshots", "snapshot_vec")
    class SnapshotInstanceDetails(_message.Message):
        __slots__ = ("instance_uuid",)
        INSTANCE_UUID_FIELD_NUMBER: _ClassVar[int]
        instance_uuid: str
        def __init__(self, instance_uuid: _Optional[str] = ...) -> None: ...
    NUM_SNAPSHOTS_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_VEC_FIELD_NUMBER: _ClassVar[int]
    num_snapshots: int
    snapshot_vec: _containers.RepeatedCompositeFieldContainer[FetchSnapshotInstanceDetailsResponse.SnapshotInstanceDetails]
    def __init__(self, num_snapshots: _Optional[int] = ..., snapshot_vec: _Optional[_Iterable[_Union[FetchSnapshotInstanceDetailsResponse.SnapshotInstanceDetails, _Mapping]]] = ...) -> None: ...

class HRef(_message.Message):
    __slots__ = ("href",)
    HREF_FIELD_NUMBER: _ClassVar[int]
    href: str
    def __init__(self, href: _Optional[str] = ...) -> None: ...

class SelfLink(_message.Message):
    __slots__ = ("self",)
    SELF_FIELD_NUMBER: _ClassVar[int]
    self: HRef
    def __init__(self, self_: _Optional[_Union[HRef, _Mapping]] = ...) -> None: ...

class JobLink(_message.Message):
    __slots__ = ("link", "uuid")
    LINK_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    link: SelfLink
    uuid: str
    def __init__(self, link: _Optional[_Union[SelfLink, _Mapping]] = ..., uuid: _Optional[str] = ...) -> None: ...

class SnapmirrorEndpoint(_message.Message):
    __slots__ = ("path", "uuid")
    PATH_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    path: str
    uuid: str
    def __init__(self, path: _Optional[str] = ..., uuid: _Optional[str] = ...) -> None: ...

class Policy(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class Transfer(_message.Message):
    __slots__ = ("bytes_transferred", "state", "uuid")
    BYTES_TRANSFERRED_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    bytes_transferred: int
    state: str
    uuid: str
    def __init__(self, bytes_transferred: _Optional[int] = ..., state: _Optional[str] = ..., uuid: _Optional[str] = ...) -> None: ...

class Application(_message.Message):
    __slots__ = ("name", "type")
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    name: str
    type: str
    def __init__(self, name: _Optional[str] = ..., type: _Optional[str] = ...) -> None: ...

class Snapshot(_message.Message):
    __slots__ = ("name", "uuid")
    NAME_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    name: str
    uuid: str
    def __init__(self, name: _Optional[str] = ..., uuid: _Optional[str] = ...) -> None: ...

class SnapmirrorRetention(_message.Message):
    __slots__ = ("label", "count")
    LABEL_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    label: str
    count: int
    def __init__(self, label: _Optional[str] = ..., count: _Optional[int] = ...) -> None: ...

class File(_message.Message):
    __slots__ = ("destination_path", "source_path")
    DESTINATION_PATH_FIELD_NUMBER: _ClassVar[int]
    SOURCE_PATH_FIELD_NUMBER: _ClassVar[int]
    destination_path: str
    source_path: str
    def __init__(self, destination_path: _Optional[str] = ..., source_path: _Optional[str] = ...) -> None: ...

class ErrorContext(_message.Message):
    __slots__ = ("error",)
    class Error(_message.Message):
        __slots__ = ("argument_vec", "code", "msg", "target")
        class Argument(_message.Message):
            __slots__ = ("code", "msg")
            CODE_FIELD_NUMBER: _ClassVar[int]
            MSG_FIELD_NUMBER: _ClassVar[int]
            code: str
            msg: str
            def __init__(self, code: _Optional[str] = ..., msg: _Optional[str] = ...) -> None: ...
        ARGUMENT_VEC_FIELD_NUMBER: _ClassVar[int]
        CODE_FIELD_NUMBER: _ClassVar[int]
        MSG_FIELD_NUMBER: _ClassVar[int]
        TARGET_FIELD_NUMBER: _ClassVar[int]
        argument_vec: _containers.RepeatedCompositeFieldContainer[ErrorContext.Error.Argument]
        code: str
        msg: str
        target: str
        def __init__(self, argument_vec: _Optional[_Iterable[_Union[ErrorContext.Error.Argument, _Mapping]]] = ..., code: _Optional[str] = ..., msg: _Optional[str] = ..., target: _Optional[str] = ...) -> None: ...
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: ErrorContext.Error
    def __init__(self, error: _Optional[_Union[ErrorContext.Error, _Mapping]] = ...) -> None: ...

class FileSystemRequest(_message.Message):
    __slots__ = ("type", "permissions")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    type: str
    permissions: str
    def __init__(self, type: _Optional[str] = ..., permissions: _Optional[str] = ...) -> None: ...

class EmptyResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
