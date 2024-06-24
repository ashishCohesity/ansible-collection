from configs import cluster_config_pb2 as _cluster_config_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class QuotaUID(_message.Message):
    __slots__ = ("uid", "sid")
    UID_FIELD_NUMBER: _ClassVar[int]
    SID_FIELD_NUMBER: _ClassVar[int]
    uid: int
    sid: _cluster_config_pb2.ClusterConfigProto.SID
    def __init__(self, uid: _Optional[int] = ..., sid: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.SID, _Mapping]] = ...) -> None: ...

class QuotaSnapTreeValueProto(_message.Message):
    __slots__ = ("user_quota_policy",)
    USER_QUOTA_POLICY_FIELD_NUMBER: _ClassVar[int]
    user_quota_policy: _cluster_config_pb2.ClusterConfigProto.QuotaPolicy
    def __init__(self, user_quota_policy: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.QuotaPolicy, _Mapping]] = ...) -> None: ...

class UsageQuotaSnapTreeValueProto(_message.Message):
    __slots__ = ("logical_usage_bytes",)
    LOGICAL_USAGE_BYTES_FIELD_NUMBER: _ClassVar[int]
    logical_usage_bytes: int
    def __init__(self, logical_usage_bytes: _Optional[int] = ...) -> None: ...

class QuotaBackupManifestProto(_message.Message):
    __slots__ = ("user_quota_enabled", "default_policy", "num_override_batches", "total_num_overrides")
    USER_QUOTA_ENABLED_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_POLICY_FIELD_NUMBER: _ClassVar[int]
    NUM_OVERRIDE_BATCHES_FIELD_NUMBER: _ClassVar[int]
    TOTAL_NUM_OVERRIDES_FIELD_NUMBER: _ClassVar[int]
    user_quota_enabled: bool
    default_policy: _cluster_config_pb2.ClusterConfigProto.QuotaPolicy
    num_override_batches: int
    total_num_overrides: int
    def __init__(self, user_quota_enabled: bool = ..., default_policy: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.QuotaPolicy, _Mapping]] = ..., num_override_batches: _Optional[int] = ..., total_num_overrides: _Optional[int] = ...) -> None: ...

class DirQuotaSnapTreeValueProto(_message.Message):
    __slots__ = ("dir_quota_policy", "dir_path", "logical_usage_bytes", "dir_walk_pending", "is_tombstone")
    DIR_QUOTA_POLICY_FIELD_NUMBER: _ClassVar[int]
    DIR_PATH_FIELD_NUMBER: _ClassVar[int]
    LOGICAL_USAGE_BYTES_FIELD_NUMBER: _ClassVar[int]
    DIR_WALK_PENDING_FIELD_NUMBER: _ClassVar[int]
    IS_TOMBSTONE_FIELD_NUMBER: _ClassVar[int]
    dir_quota_policy: _cluster_config_pb2.ClusterConfigProto.QuotaPolicy
    dir_path: str
    logical_usage_bytes: int
    dir_walk_pending: bool
    is_tombstone: bool
    def __init__(self, dir_quota_policy: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.QuotaPolicy, _Mapping]] = ..., dir_path: _Optional[str] = ..., logical_usage_bytes: _Optional[int] = ..., dir_walk_pending: bool = ..., is_tombstone: bool = ...) -> None: ...

class DirQuotaBackupManifestProto(_message.Message):
    __slots__ = ("dir_quota_enabled", "num_dir_quota_batches", "total_num_dir_quotas")
    DIR_QUOTA_ENABLED_FIELD_NUMBER: _ClassVar[int]
    NUM_DIR_QUOTA_BATCHES_FIELD_NUMBER: _ClassVar[int]
    TOTAL_NUM_DIR_QUOTAS_FIELD_NUMBER: _ClassVar[int]
    dir_quota_enabled: bool
    num_dir_quota_batches: int
    total_num_dir_quotas: int
    def __init__(self, dir_quota_enabled: bool = ..., num_dir_quota_batches: _Optional[int] = ..., total_num_dir_quotas: _Optional[int] = ...) -> None: ...
