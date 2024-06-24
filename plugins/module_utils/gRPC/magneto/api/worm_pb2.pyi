from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class WormRetentionProto(_message.Message):
    __slots__ = ("policy_type", "retention_secs", "version", "enable_worm_on_external_target")
    class WormPolicyType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNone: _ClassVar[WormRetentionProto.WormPolicyType]
        kCompliance: _ClassVar[WormRetentionProto.WormPolicyType]
        kAdministrative: _ClassVar[WormRetentionProto.WormPolicyType]
    kNone: WormRetentionProto.WormPolicyType
    kCompliance: WormRetentionProto.WormPolicyType
    kAdministrative: WormRetentionProto.WormPolicyType
    POLICY_TYPE_FIELD_NUMBER: _ClassVar[int]
    RETENTION_SECS_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    ENABLE_WORM_ON_EXTERNAL_TARGET_FIELD_NUMBER: _ClassVar[int]
    policy_type: WormRetentionProto.WormPolicyType
    retention_secs: int
    version: int
    enable_worm_on_external_target: bool
    def __init__(self, policy_type: _Optional[_Union[WormRetentionProto.WormPolicyType, str]] = ..., retention_secs: _Optional[int] = ..., version: _Optional[int] = ..., enable_worm_on_external_target: bool = ...) -> None: ...

class ArchiveWORMProperties(_message.Message):
    __slots__ = ("is_archive_worm_compliant", "archive_worm_non_compliance_reason", "worm_expiry_time_usecs", "external_target_data_lock_retention_secs", "policy_type")
    IS_ARCHIVE_WORM_COMPLIANT_FIELD_NUMBER: _ClassVar[int]
    ARCHIVE_WORM_NON_COMPLIANCE_REASON_FIELD_NUMBER: _ClassVar[int]
    WORM_EXPIRY_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_TARGET_DATA_LOCK_RETENTION_SECS_FIELD_NUMBER: _ClassVar[int]
    POLICY_TYPE_FIELD_NUMBER: _ClassVar[int]
    is_archive_worm_compliant: bool
    archive_worm_non_compliance_reason: str
    worm_expiry_time_usecs: int
    external_target_data_lock_retention_secs: int
    policy_type: WormRetentionProto.WormPolicyType
    def __init__(self, is_archive_worm_compliant: bool = ..., archive_worm_non_compliance_reason: _Optional[str] = ..., worm_expiry_time_usecs: _Optional[int] = ..., external_target_data_lock_retention_secs: _Optional[int] = ..., policy_type: _Optional[_Union[WormRetentionProto.WormPolicyType, str]] = ...) -> None: ...

class DataLockConstraintsProto(_message.Message):
    __slots__ = ("policy_type", "data_lock_expiry_usecs", "enable_worm_on_external_target")
    POLICY_TYPE_FIELD_NUMBER: _ClassVar[int]
    DATA_LOCK_EXPIRY_USECS_FIELD_NUMBER: _ClassVar[int]
    ENABLE_WORM_ON_EXTERNAL_TARGET_FIELD_NUMBER: _ClassVar[int]
    policy_type: WormRetentionProto.WormPolicyType
    data_lock_expiry_usecs: int
    enable_worm_on_external_target: bool
    def __init__(self, policy_type: _Optional[_Union[WormRetentionProto.WormPolicyType, str]] = ..., data_lock_expiry_usecs: _Optional[int] = ..., enable_worm_on_external_target: bool = ...) -> None: ...
