from configs import cluster_config_pb2 as _cluster_config_pb2
from bridge.vault.base import common_pb2 as _common_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UploadContext(_message.Message):
    __slots__ = ("upload_id", "part_vec", "object_finalized", "object_size_bytes", "part_size")
    class Part(_message.Message):
        __slots__ = ("part_num", "etag")
        PART_NUM_FIELD_NUMBER: _ClassVar[int]
        ETAG_FIELD_NUMBER: _ClassVar[int]
        part_num: int
        etag: str
        def __init__(self, part_num: _Optional[int] = ..., etag: _Optional[str] = ...) -> None: ...
    UPLOAD_ID_FIELD_NUMBER: _ClassVar[int]
    PART_VEC_FIELD_NUMBER: _ClassVar[int]
    OBJECT_FINALIZED_FIELD_NUMBER: _ClassVar[int]
    OBJECT_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    PART_SIZE_FIELD_NUMBER: _ClassVar[int]
    upload_id: str
    part_vec: _containers.RepeatedCompositeFieldContainer[UploadContext.Part]
    object_finalized: bool
    object_size_bytes: int
    part_size: int
    def __init__(self, upload_id: _Optional[str] = ..., part_vec: _Optional[_Iterable[_Union[UploadContext.Part, _Mapping]]] = ..., object_finalized: bool = ..., object_size_bytes: _Optional[int] = ..., part_size: _Optional[int] = ...) -> None: ...

class DownloadContext(_message.Message):
    __slots__ = ("restore_in_progress", "restore_finished", "expiry_time", "version_id")
    RESTORE_IN_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    RESTORE_FINISHED_FIELD_NUMBER: _ClassVar[int]
    EXPIRY_TIME_FIELD_NUMBER: _ClassVar[int]
    VERSION_ID_FIELD_NUMBER: _ClassVar[int]
    restore_in_progress: bool
    restore_finished: bool
    expiry_time: str
    version_id: str
    def __init__(self, restore_in_progress: bool = ..., restore_finished: bool = ..., expiry_time: _Optional[str] = ..., version_id: _Optional[str] = ...) -> None: ...

class LambdaConfig(_message.Message):
    __slots__ = ("version",)
    VERSION_FIELD_NUMBER: _ClassVar[int]
    version: int
    def __init__(self, version: _Optional[int] = ...) -> None: ...

class VaultObjectACLInfo(_message.Message):
    __slots__ = ("owner_id", "grants")
    class Grant(_message.Message):
        __slots__ = ("grantee", "permission", "grantee_type")
        GRANTEE_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_FIELD_NUMBER: _ClassVar[int]
        GRANTEE_TYPE_FIELD_NUMBER: _ClassVar[int]
        grantee: str
        permission: str
        grantee_type: str
        def __init__(self, grantee: _Optional[str] = ..., permission: _Optional[str] = ..., grantee_type: _Optional[str] = ...) -> None: ...
    OWNER_ID_FIELD_NUMBER: _ClassVar[int]
    GRANTS_FIELD_NUMBER: _ClassVar[int]
    owner_id: str
    grants: _containers.RepeatedCompositeFieldContainer[VaultObjectACLInfo.Grant]
    def __init__(self, owner_id: _Optional[str] = ..., grants: _Optional[_Iterable[_Union[VaultObjectACLInfo.Grant, _Mapping]]] = ...) -> None: ...

class CreateContext(_message.Message):
    __slots__ = ("tier_type", "grants")
    TIER_TYPE_FIELD_NUMBER: _ClassVar[int]
    GRANTS_FIELD_NUMBER: _ClassVar[int]
    tier_type: _cluster_config_pb2.ClusterConfigProto.Vault.CloudProperties.AmazonProperties.TierType
    grants: _containers.RepeatedCompositeFieldContainer[VaultObjectACLInfo.Grant]
    def __init__(self, tier_type: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.Vault.CloudProperties.AmazonProperties.TierType, str]] = ..., grants: _Optional[_Iterable[_Union[VaultObjectACLInfo.Grant, _Mapping]]] = ...) -> None: ...

class S3Cookie(_message.Message):
    __slots__ = ("monitoring_cookie", "cold_tier_cookie", "worm_cookie", "lifecycle_cookie")
    class LifeCyclePolicyCookie(_message.Message):
        __slots__ = ("object_name", "tier_type")
        OBJECT_NAME_FIELD_NUMBER: _ClassVar[int]
        TIER_TYPE_FIELD_NUMBER: _ClassVar[int]
        object_name: str
        tier_type: _cluster_config_pb2.ClusterConfigProto.Vault.CloudProperties.AmazonProperties.TierType
        def __init__(self, object_name: _Optional[str] = ..., tier_type: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.Vault.CloudProperties.AmazonProperties.TierType, str]] = ...) -> None: ...
    MONITORING_COOKIE_FIELD_NUMBER: _ClassVar[int]
    COLD_TIER_COOKIE_FIELD_NUMBER: _ClassVar[int]
    WORM_COOKIE_FIELD_NUMBER: _ClassVar[int]
    LIFECYCLE_COOKIE_FIELD_NUMBER: _ClassVar[int]
    monitoring_cookie: _common_pb2.MonitoringCookie
    cold_tier_cookie: _common_pb2.ColdTierCookie
    worm_cookie: _common_pb2.WormCookie
    lifecycle_cookie: S3Cookie.LifeCyclePolicyCookie
    def __init__(self, monitoring_cookie: _Optional[_Union[_common_pb2.MonitoringCookie, _Mapping]] = ..., cold_tier_cookie: _Optional[_Union[_common_pb2.ColdTierCookie, _Mapping]] = ..., worm_cookie: _Optional[_Union[_common_pb2.WormCookie, _Mapping]] = ..., lifecycle_cookie: _Optional[_Union[S3Cookie.LifeCyclePolicyCookie, _Mapping]] = ...) -> None: ...
