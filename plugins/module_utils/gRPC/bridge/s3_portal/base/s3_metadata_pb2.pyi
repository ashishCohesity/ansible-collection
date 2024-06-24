from bridge.s3_portal.keystone import keystone2_pb2 as _keystone2_pb2
from util.base import universal_id_pb2 as _universal_id_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ConditionOperator(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kStringEquals: _ClassVar[ConditionOperator]
    kStringNotEquals: _ClassVar[ConditionOperator]
    kStringEqualsIgnoreCase: _ClassVar[ConditionOperator]
    kStringNotEqualsIgnoreCase: _ClassVar[ConditionOperator]
    kStringLike: _ClassVar[ConditionOperator]
    kStringNotLike: _ClassVar[ConditionOperator]
    kNumericEquals: _ClassVar[ConditionOperator]
    kNumericNotEquals: _ClassVar[ConditionOperator]
    kNumericLessThan: _ClassVar[ConditionOperator]
    kNumericLessThanEquals: _ClassVar[ConditionOperator]
    kNumericGreaterThan: _ClassVar[ConditionOperator]
    kNumericGreaterThanEquals: _ClassVar[ConditionOperator]
    kDateEquals: _ClassVar[ConditionOperator]
    kDateNotEquals: _ClassVar[ConditionOperator]
    kDateLessThan: _ClassVar[ConditionOperator]
    kDateLessThanEquals: _ClassVar[ConditionOperator]
    kDateGreaterThan: _ClassVar[ConditionOperator]
    kDateGreaterThanEquals: _ClassVar[ConditionOperator]
    kBool: _ClassVar[ConditionOperator]
    kBinaryEquals: _ClassVar[ConditionOperator]
    kIpAddress: _ClassVar[ConditionOperator]
    kNotIpAddress: _ClassVar[ConditionOperator]
    kNull: _ClassVar[ConditionOperator]

class ProtocolType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kUnknown: _ClassVar[ProtocolType]
    kS3: _ClassVar[ProtocolType]
    kSwift: _ClassVar[ProtocolType]
kStringEquals: ConditionOperator
kStringNotEquals: ConditionOperator
kStringEqualsIgnoreCase: ConditionOperator
kStringNotEqualsIgnoreCase: ConditionOperator
kStringLike: ConditionOperator
kStringNotLike: ConditionOperator
kNumericEquals: ConditionOperator
kNumericNotEquals: ConditionOperator
kNumericLessThan: ConditionOperator
kNumericLessThanEquals: ConditionOperator
kNumericGreaterThan: ConditionOperator
kNumericGreaterThanEquals: ConditionOperator
kDateEquals: ConditionOperator
kDateNotEquals: ConditionOperator
kDateLessThan: ConditionOperator
kDateLessThanEquals: ConditionOperator
kDateGreaterThan: ConditionOperator
kDateGreaterThanEquals: ConditionOperator
kBool: ConditionOperator
kBinaryEquals: ConditionOperator
kIpAddress: ConditionOperator
kNotIpAddress: ConditionOperator
kNull: ConditionOperator
kUnknown: ProtocolType
kS3: ProtocolType
kSwift: ProtocolType

class ACLPermissionProto(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kRead: _ClassVar[ACLPermissionProto.Type]
        kWrite: _ClassVar[ACLPermissionProto.Type]
        kReadACP: _ClassVar[ACLPermissionProto.Type]
        kWriteACP: _ClassVar[ACLPermissionProto.Type]
        kFullControl: _ClassVar[ACLPermissionProto.Type]
    kRead: ACLPermissionProto.Type
    kWrite: ACLPermissionProto.Type
    kReadACP: ACLPermissionProto.Type
    kWriteACP: ACLPermissionProto.Type
    kFullControl: ACLPermissionProto.Type
    def __init__(self) -> None: ...

class BucketAccessPolicyPermissions(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kListBucket: _ClassVar[BucketAccessPolicyPermissions.Type]
        kListBucketVersions: _ClassVar[BucketAccessPolicyPermissions.Type]
        kListBucketMultipartUploads: _ClassVar[BucketAccessPolicyPermissions.Type]
        kGetBucketLocation: _ClassVar[BucketAccessPolicyPermissions.Type]
        kPutObject: _ClassVar[BucketAccessPolicyPermissions.Type]
        kDeleteObject: _ClassVar[BucketAccessPolicyPermissions.Type]
        kDeleteObjectVersion: _ClassVar[BucketAccessPolicyPermissions.Type]
        kGetBucketAcl: _ClassVar[BucketAccessPolicyPermissions.Type]
        kPutBucketAcl: _ClassVar[BucketAccessPolicyPermissions.Type]
        kBucketOwner: _ClassVar[BucketAccessPolicyPermissions.Type]
        kPutBucketObjectLockConfiguration: _ClassVar[BucketAccessPolicyPermissions.Type]
        kGetBucketObjectLockConfiguration: _ClassVar[BucketAccessPolicyPermissions.Type]
        kGetLifecycleConfiguration: _ClassVar[BucketAccessPolicyPermissions.Type]
        kPutLifecycleConfiguration: _ClassVar[BucketAccessPolicyPermissions.Type]
        kPutObjectRetention: _ClassVar[BucketAccessPolicyPermissions.Type]
        kGetObjectRetention: _ClassVar[BucketAccessPolicyPermissions.Type]
        kBypassGovernanceRetention: _ClassVar[BucketAccessPolicyPermissions.Type]
        kPutObjectLegalHold: _ClassVar[BucketAccessPolicyPermissions.Type]
        kGetObjectLegalHold: _ClassVar[BucketAccessPolicyPermissions.Type]
        kGetBucketPolicy: _ClassVar[BucketAccessPolicyPermissions.Type]
        kPutBucketPolicy: _ClassVar[BucketAccessPolicyPermissions.Type]
        kDeleteBucketPolicy: _ClassVar[BucketAccessPolicyPermissions.Type]
        kPutObjectTagging: _ClassVar[BucketAccessPolicyPermissions.Type]
        kPutObjectVersionTagging: _ClassVar[BucketAccessPolicyPermissions.Type]
        kGetObjectTagging: _ClassVar[BucketAccessPolicyPermissions.Type]
        kGetObjectVersionTagging: _ClassVar[BucketAccessPolicyPermissions.Type]
        kDeleteObjectTagging: _ClassVar[BucketAccessPolicyPermissions.Type]
        kDeleteObjectVersionTagging: _ClassVar[BucketAccessPolicyPermissions.Type]
        kGetBucketOwnershipControls: _ClassVar[BucketAccessPolicyPermissions.Type]
        kPutBucketOwnershipControls: _ClassVar[BucketAccessPolicyPermissions.Type]
        kGetBucketTagging: _ClassVar[BucketAccessPolicyPermissions.Type]
        kPutBucketTagging: _ClassVar[BucketAccessPolicyPermissions.Type]
    kListBucket: BucketAccessPolicyPermissions.Type
    kListBucketVersions: BucketAccessPolicyPermissions.Type
    kListBucketMultipartUploads: BucketAccessPolicyPermissions.Type
    kGetBucketLocation: BucketAccessPolicyPermissions.Type
    kPutObject: BucketAccessPolicyPermissions.Type
    kDeleteObject: BucketAccessPolicyPermissions.Type
    kDeleteObjectVersion: BucketAccessPolicyPermissions.Type
    kGetBucketAcl: BucketAccessPolicyPermissions.Type
    kPutBucketAcl: BucketAccessPolicyPermissions.Type
    kBucketOwner: BucketAccessPolicyPermissions.Type
    kPutBucketObjectLockConfiguration: BucketAccessPolicyPermissions.Type
    kGetBucketObjectLockConfiguration: BucketAccessPolicyPermissions.Type
    kGetLifecycleConfiguration: BucketAccessPolicyPermissions.Type
    kPutLifecycleConfiguration: BucketAccessPolicyPermissions.Type
    kPutObjectRetention: BucketAccessPolicyPermissions.Type
    kGetObjectRetention: BucketAccessPolicyPermissions.Type
    kBypassGovernanceRetention: BucketAccessPolicyPermissions.Type
    kPutObjectLegalHold: BucketAccessPolicyPermissions.Type
    kGetObjectLegalHold: BucketAccessPolicyPermissions.Type
    kGetBucketPolicy: BucketAccessPolicyPermissions.Type
    kPutBucketPolicy: BucketAccessPolicyPermissions.Type
    kDeleteBucketPolicy: BucketAccessPolicyPermissions.Type
    kPutObjectTagging: BucketAccessPolicyPermissions.Type
    kPutObjectVersionTagging: BucketAccessPolicyPermissions.Type
    kGetObjectTagging: BucketAccessPolicyPermissions.Type
    kGetObjectVersionTagging: BucketAccessPolicyPermissions.Type
    kDeleteObjectTagging: BucketAccessPolicyPermissions.Type
    kDeleteObjectVersionTagging: BucketAccessPolicyPermissions.Type
    kGetBucketOwnershipControls: BucketAccessPolicyPermissions.Type
    kPutBucketOwnershipControls: BucketAccessPolicyPermissions.Type
    kGetBucketTagging: BucketAccessPolicyPermissions.Type
    kPutBucketTagging: BucketAccessPolicyPermissions.Type
    def __init__(self) -> None: ...

class ObjectAccessPolicyPermissions(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kGetObject: _ClassVar[ObjectAccessPolicyPermissions.Type]
        kGetObjectVersion: _ClassVar[ObjectAccessPolicyPermissions.Type]
        kGetObjectTorrent: _ClassVar[ObjectAccessPolicyPermissions.Type]
        kGetObjectAcl: _ClassVar[ObjectAccessPolicyPermissions.Type]
        kGetObjectVersionAcl: _ClassVar[ObjectAccessPolicyPermissions.Type]
        kPutObjectAcl: _ClassVar[ObjectAccessPolicyPermissions.Type]
        kPutObjectVersionAcl: _ClassVar[ObjectAccessPolicyPermissions.Type]
        kBucketOwner: _ClassVar[ObjectAccessPolicyPermissions.Type]
        kPutObjectRetention: _ClassVar[ObjectAccessPolicyPermissions.Type]
        kGetObjectRetention: _ClassVar[ObjectAccessPolicyPermissions.Type]
        kBypassGovernanceRetention: _ClassVar[ObjectAccessPolicyPermissions.Type]
        kPutObjectLegalHold: _ClassVar[ObjectAccessPolicyPermissions.Type]
        kGetObjectLegalHold: _ClassVar[ObjectAccessPolicyPermissions.Type]
        kFullControlObject: _ClassVar[ObjectAccessPolicyPermissions.Type]
    kGetObject: ObjectAccessPolicyPermissions.Type
    kGetObjectVersion: ObjectAccessPolicyPermissions.Type
    kGetObjectTorrent: ObjectAccessPolicyPermissions.Type
    kGetObjectAcl: ObjectAccessPolicyPermissions.Type
    kGetObjectVersionAcl: ObjectAccessPolicyPermissions.Type
    kPutObjectAcl: ObjectAccessPolicyPermissions.Type
    kPutObjectVersionAcl: ObjectAccessPolicyPermissions.Type
    kBucketOwner: ObjectAccessPolicyPermissions.Type
    kPutObjectRetention: ObjectAccessPolicyPermissions.Type
    kGetObjectRetention: ObjectAccessPolicyPermissions.Type
    kBypassGovernanceRetention: ObjectAccessPolicyPermissions.Type
    kPutObjectLegalHold: ObjectAccessPolicyPermissions.Type
    kGetObjectLegalHold: ObjectAccessPolicyPermissions.Type
    kFullControlObject: ObjectAccessPolicyPermissions.Type
    def __init__(self) -> None: ...

class GroupProto(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kAuthenticatedUsersGroup: _ClassVar[GroupProto.Type]
        kAllUsersGroup: _ClassVar[GroupProto.Type]
        kLogDeliveryGroup: _ClassVar[GroupProto.Type]
        kCustomGroup: _ClassVar[GroupProto.Type]
        kInvalidGroup: _ClassVar[GroupProto.Type]
    kAuthenticatedUsersGroup: GroupProto.Type
    kAllUsersGroup: GroupProto.Type
    kLogDeliveryGroup: GroupProto.Type
    kCustomGroup: GroupProto.Type
    kInvalidGroup: GroupProto.Type
    def __init__(self) -> None: ...

class GranteeProto(_message.Message):
    __slots__ = ("type", "user_id", "email_address", "group")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kRegisteredUser: _ClassVar[GranteeProto.Type]
        kEmailUser: _ClassVar[GranteeProto.Type]
        kGroup: _ClassVar[GranteeProto.Type]
    kRegisteredUser: GranteeProto.Type
    kEmailUser: GranteeProto.Type
    kGroup: GranteeProto.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    EMAIL_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    GROUP_FIELD_NUMBER: _ClassVar[int]
    type: GranteeProto.Type
    user_id: str
    email_address: str
    group: GroupProto.Type
    def __init__(self, type: _Optional[_Union[GranteeProto.Type, str]] = ..., user_id: _Optional[str] = ..., email_address: _Optional[str] = ..., group: _Optional[_Union[GroupProto.Type, str]] = ...) -> None: ...

class KeystoneACLProto(_message.Message):
    __slots__ = ("read_grantees", "write_grantees")
    class Grantees(_message.Message):
        __slots__ = ("all_users", "project_id_vec", "user_id_vec", "project_users_map", "role_name_vec")
        class ProjectUsers(_message.Message):
            __slots__ = ("user_id_vec",)
            USER_ID_VEC_FIELD_NUMBER: _ClassVar[int]
            user_id_vec: _containers.RepeatedScalarFieldContainer[str]
            def __init__(self, user_id_vec: _Optional[_Iterable[str]] = ...) -> None: ...
        class ProjectUsersMapEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: KeystoneACLProto.Grantees.ProjectUsers
            def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[KeystoneACLProto.Grantees.ProjectUsers, _Mapping]] = ...) -> None: ...
        ALL_USERS_FIELD_NUMBER: _ClassVar[int]
        PROJECT_ID_VEC_FIELD_NUMBER: _ClassVar[int]
        USER_ID_VEC_FIELD_NUMBER: _ClassVar[int]
        PROJECT_USERS_MAP_FIELD_NUMBER: _ClassVar[int]
        ROLE_NAME_VEC_FIELD_NUMBER: _ClassVar[int]
        all_users: bool
        project_id_vec: _containers.RepeatedScalarFieldContainer[str]
        user_id_vec: _containers.RepeatedScalarFieldContainer[str]
        project_users_map: _containers.MessageMap[str, KeystoneACLProto.Grantees.ProjectUsers]
        role_name_vec: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, all_users: bool = ..., project_id_vec: _Optional[_Iterable[str]] = ..., user_id_vec: _Optional[_Iterable[str]] = ..., project_users_map: _Optional[_Mapping[str, KeystoneACLProto.Grantees.ProjectUsers]] = ..., role_name_vec: _Optional[_Iterable[str]] = ...) -> None: ...
    READ_GRANTEES_FIELD_NUMBER: _ClassVar[int]
    WRITE_GRANTEES_FIELD_NUMBER: _ClassVar[int]
    read_grantees: KeystoneACLProto.Grantees
    write_grantees: KeystoneACLProto.Grantees
    def __init__(self, read_grantees: _Optional[_Union[KeystoneACLProto.Grantees, _Mapping]] = ..., write_grantees: _Optional[_Union[KeystoneACLProto.Grantees, _Mapping]] = ...) -> None: ...

class CommonACLProto(_message.Message):
    __slots__ = ("read_grantees", "write_rlistings")
    class Grantees(_message.Message):
        __slots__ = ("all_users", "granted_referrer_vec", "denied_referrer_vec", "rlistings")
        ALL_USERS_FIELD_NUMBER: _ClassVar[int]
        GRANTED_REFERRER_VEC_FIELD_NUMBER: _ClassVar[int]
        DENIED_REFERRER_VEC_FIELD_NUMBER: _ClassVar[int]
        RLISTINGS_FIELD_NUMBER: _ClassVar[int]
        all_users: bool
        granted_referrer_vec: _containers.RepeatedScalarFieldContainer[str]
        denied_referrer_vec: _containers.RepeatedScalarFieldContainer[str]
        rlistings: bool
        def __init__(self, all_users: bool = ..., granted_referrer_vec: _Optional[_Iterable[str]] = ..., denied_referrer_vec: _Optional[_Iterable[str]] = ..., rlistings: bool = ...) -> None: ...
    READ_GRANTEES_FIELD_NUMBER: _ClassVar[int]
    WRITE_RLISTINGS_FIELD_NUMBER: _ClassVar[int]
    read_grantees: CommonACLProto.Grantees
    write_rlistings: bool
    def __init__(self, read_grantees: _Optional[_Union[CommonACLProto.Grantees, _Mapping]] = ..., write_rlistings: bool = ...) -> None: ...

class ACLProto(_message.Message):
    __slots__ = ("grant_vec", "swift_read_acl", "swift_write_acl", "keystone_acl", "common_acl")
    class Grant(_message.Message):
        __slots__ = ("grantee", "permission_vec")
        GRANTEE_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_VEC_FIELD_NUMBER: _ClassVar[int]
        grantee: GranteeProto
        permission_vec: _containers.RepeatedScalarFieldContainer[ACLPermissionProto.Type]
        def __init__(self, grantee: _Optional[_Union[GranteeProto, _Mapping]] = ..., permission_vec: _Optional[_Iterable[_Union[ACLPermissionProto.Type, str]]] = ...) -> None: ...
    GRANT_VEC_FIELD_NUMBER: _ClassVar[int]
    SWIFT_READ_ACL_FIELD_NUMBER: _ClassVar[int]
    SWIFT_WRITE_ACL_FIELD_NUMBER: _ClassVar[int]
    KEYSTONE_ACL_FIELD_NUMBER: _ClassVar[int]
    COMMON_ACL_FIELD_NUMBER: _ClassVar[int]
    grant_vec: _containers.RepeatedCompositeFieldContainer[ACLProto.Grant]
    swift_read_acl: str
    swift_write_acl: str
    keystone_acl: KeystoneACLProto
    common_acl: CommonACLProto
    def __init__(self, grant_vec: _Optional[_Iterable[_Union[ACLProto.Grant, _Mapping]]] = ..., swift_read_acl: _Optional[str] = ..., swift_write_acl: _Optional[str] = ..., keystone_acl: _Optional[_Union[KeystoneACLProto, _Mapping]] = ..., common_acl: _Optional[_Union[CommonACLProto, _Mapping]] = ...) -> None: ...

class Principal(_message.Message):
    __slots__ = ("wildcard_entry", "canonical_user_id_vec")
    WILDCARD_ENTRY_FIELD_NUMBER: _ClassVar[int]
    CANONICAL_USER_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    wildcard_entry: bool
    canonical_user_id_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, wildcard_entry: bool = ..., canonical_user_id_vec: _Optional[_Iterable[str]] = ...) -> None: ...

class ConditionKeyValues(_message.Message):
    __slots__ = ("value_vec",)
    VALUE_VEC_FIELD_NUMBER: _ClassVar[int]
    value_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, value_vec: _Optional[_Iterable[str]] = ...) -> None: ...

class Condition(_message.Message):
    __slots__ = ("condition_key_values_map", "cond_operator", "for_any_value", "for_all_values", "if_exists")
    class ConditionKeyValuesMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: ConditionKeyValues
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[ConditionKeyValues, _Mapping]] = ...) -> None: ...
    CONDITION_KEY_VALUES_MAP_FIELD_NUMBER: _ClassVar[int]
    COND_OPERATOR_FIELD_NUMBER: _ClassVar[int]
    FOR_ANY_VALUE_FIELD_NUMBER: _ClassVar[int]
    FOR_ALL_VALUES_FIELD_NUMBER: _ClassVar[int]
    IF_EXISTS_FIELD_NUMBER: _ClassVar[int]
    condition_key_values_map: _containers.MessageMap[str, ConditionKeyValues]
    cond_operator: ConditionOperator
    for_any_value: bool
    for_all_values: bool
    if_exists: bool
    def __init__(self, condition_key_values_map: _Optional[_Mapping[str, ConditionKeyValues]] = ..., cond_operator: _Optional[_Union[ConditionOperator, str]] = ..., for_any_value: bool = ..., for_all_values: bool = ..., if_exists: bool = ...) -> None: ...

class Statement(_message.Message):
    __slots__ = ("sid", "is_allow", "principal", "negate_principal", "action_vec", "negate_action_vec", "resource_vec", "negate_resource_vec", "condition_vec")
    SID_FIELD_NUMBER: _ClassVar[int]
    IS_ALLOW_FIELD_NUMBER: _ClassVar[int]
    PRINCIPAL_FIELD_NUMBER: _ClassVar[int]
    NEGATE_PRINCIPAL_FIELD_NUMBER: _ClassVar[int]
    ACTION_VEC_FIELD_NUMBER: _ClassVar[int]
    NEGATE_ACTION_VEC_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_VEC_FIELD_NUMBER: _ClassVar[int]
    NEGATE_RESOURCE_VEC_FIELD_NUMBER: _ClassVar[int]
    CONDITION_VEC_FIELD_NUMBER: _ClassVar[int]
    sid: str
    is_allow: bool
    principal: Principal
    negate_principal: bool
    action_vec: _containers.RepeatedScalarFieldContainer[str]
    negate_action_vec: bool
    resource_vec: _containers.RepeatedScalarFieldContainer[str]
    negate_resource_vec: bool
    condition_vec: _containers.RepeatedCompositeFieldContainer[Condition]
    def __init__(self, sid: _Optional[str] = ..., is_allow: bool = ..., principal: _Optional[_Union[Principal, _Mapping]] = ..., negate_principal: bool = ..., action_vec: _Optional[_Iterable[str]] = ..., negate_action_vec: bool = ..., resource_vec: _Optional[_Iterable[str]] = ..., negate_resource_vec: bool = ..., condition_vec: _Optional[_Iterable[_Union[Condition, _Mapping]]] = ...) -> None: ...

class BucketPolicy(_message.Message):
    __slots__ = ("version", "id", "statement_vec", "raw_policy_str")
    VERSION_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    STATEMENT_VEC_FIELD_NUMBER: _ClassVar[int]
    RAW_POLICY_STR_FIELD_NUMBER: _ClassVar[int]
    version: str
    id: str
    statement_vec: _containers.RepeatedCompositeFieldContainer[Statement]
    raw_policy_str: str
    def __init__(self, version: _Optional[str] = ..., id: _Optional[str] = ..., statement_vec: _Optional[_Iterable[_Union[Statement, _Mapping]]] = ..., raw_policy_str: _Optional[str] = ...) -> None: ...

class LifecycleRuleFilterTag(_message.Message):
    __slots__ = ("key", "value")
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    key: str
    value: str
    def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...

class LifecycleRuleFilterAnd(_message.Message):
    __slots__ = ("prefix", "tag_vec")
    PREFIX_FIELD_NUMBER: _ClassVar[int]
    TAG_VEC_FIELD_NUMBER: _ClassVar[int]
    prefix: str
    tag_vec: _containers.RepeatedCompositeFieldContainer[LifecycleRuleFilterTag]
    def __init__(self, prefix: _Optional[str] = ..., tag_vec: _Optional[_Iterable[_Union[LifecycleRuleFilterTag, _Mapping]]] = ...) -> None: ...

class LifecycleRuleFilter(_message.Message):
    __slots__ = ("prefix", "tag")
    PREFIX_FIELD_NUMBER: _ClassVar[int]
    TAG_FIELD_NUMBER: _ClassVar[int]
    AND_FIELD_NUMBER: _ClassVar[int]
    prefix: str
    tag: LifecycleRuleFilterTag
    def __init__(self, prefix: _Optional[str] = ..., tag: _Optional[_Union[LifecycleRuleFilterTag, _Mapping]] = ..., **kwargs) -> None: ...

class ExpirationAction(_message.Message):
    __slots__ = ("date_usecs", "days", "expired_object_delete_marker")
    DATE_USECS_FIELD_NUMBER: _ClassVar[int]
    DAYS_FIELD_NUMBER: _ClassVar[int]
    EXPIRED_OBJECT_DELETE_MARKER_FIELD_NUMBER: _ClassVar[int]
    date_usecs: int
    days: int
    expired_object_delete_marker: bool
    def __init__(self, date_usecs: _Optional[int] = ..., days: _Optional[int] = ..., expired_object_delete_marker: bool = ...) -> None: ...

class NoncurrentVersionExpirationAction(_message.Message):
    __slots__ = ("noncurrent_days",)
    NONCURRENT_DAYS_FIELD_NUMBER: _ClassVar[int]
    noncurrent_days: int
    def __init__(self, noncurrent_days: _Optional[int] = ...) -> None: ...

class AbortIncompleteMultipartUploadAction(_message.Message):
    __slots__ = ("days_after_initiation",)
    DAYS_AFTER_INITIATION_FIELD_NUMBER: _ClassVar[int]
    days_after_initiation: int
    def __init__(self, days_after_initiation: _Optional[int] = ...) -> None: ...

class LifecycleRule(_message.Message):
    __slots__ = ("id", "status", "prefix", "filter", "expiration", "noncurrent_version_expiration", "abort_incomplete_multipart_upload")
    ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    PREFIX_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    EXPIRATION_FIELD_NUMBER: _ClassVar[int]
    NONCURRENT_VERSION_EXPIRATION_FIELD_NUMBER: _ClassVar[int]
    ABORT_INCOMPLETE_MULTIPART_UPLOAD_FIELD_NUMBER: _ClassVar[int]
    id: str
    status: bool
    prefix: str
    filter: LifecycleRuleFilter
    expiration: ExpirationAction
    noncurrent_version_expiration: NoncurrentVersionExpirationAction
    abort_incomplete_multipart_upload: AbortIncompleteMultipartUploadAction
    def __init__(self, id: _Optional[str] = ..., status: bool = ..., prefix: _Optional[str] = ..., filter: _Optional[_Union[LifecycleRuleFilter, _Mapping]] = ..., expiration: _Optional[_Union[ExpirationAction, _Mapping]] = ..., noncurrent_version_expiration: _Optional[_Union[NoncurrentVersionExpirationAction, _Mapping]] = ..., abort_incomplete_multipart_upload: _Optional[_Union[AbortIncompleteMultipartUploadAction, _Mapping]] = ...) -> None: ...

class LifecycleConfigProto(_message.Message):
    __slots__ = ("version_id", "rules")
    VERSION_ID_FIELD_NUMBER: _ClassVar[int]
    RULES_FIELD_NUMBER: _ClassVar[int]
    version_id: int
    rules: _containers.RepeatedCompositeFieldContainer[LifecycleRule]
    def __init__(self, version_id: _Optional[int] = ..., rules: _Optional[_Iterable[_Union[LifecycleRule, _Mapping]]] = ...) -> None: ...

class OwnerInfo(_message.Message):
    __slots__ = ("user_id",)
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    def __init__(self, user_id: _Optional[str] = ...) -> None: ...

class SwiftContainerTaggingProto(_message.Message):
    __slots__ = ("project_tag", "acl_root_user")
    PROJECT_TAG_FIELD_NUMBER: _ClassVar[int]
    ACL_ROOT_USER_FIELD_NUMBER: _ClassVar[int]
    project_tag: _keystone2_pb2.Project
    acl_root_user: _keystone2_pb2.User
    def __init__(self, project_tag: _Optional[_Union[_keystone2_pb2.Project, _Mapping]] = ..., acl_root_user: _Optional[_Union[_keystone2_pb2.User, _Mapping]] = ...) -> None: ...

class ObjectOwnerShipProto(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kBucketOwnerPreferred: _ClassVar[ObjectOwnerShipProto.Type]
        kObjectWriter: _ClassVar[ObjectOwnerShipProto.Type]
        kBucketOwnerEnforced: _ClassVar[ObjectOwnerShipProto.Type]
    kBucketOwnerPreferred: ObjectOwnerShipProto.Type
    kObjectWriter: ObjectOwnerShipProto.Type
    kBucketOwnerEnforced: ObjectOwnerShipProto.Type
    def __init__(self) -> None: ...

class OwnershipControlsRule(_message.Message):
    __slots__ = ("object_ownership",)
    OBJECT_OWNERSHIP_FIELD_NUMBER: _ClassVar[int]
    object_ownership: ObjectOwnerShipProto.Type
    def __init__(self, object_ownership: _Optional[_Union[ObjectOwnerShipProto.Type, str]] = ...) -> None: ...

class BucketOwnershipControls(_message.Message):
    __slots__ = ("rule",)
    RULE_FIELD_NUMBER: _ClassVar[int]
    rule: OwnershipControlsRule
    def __init__(self, rule: _Optional[_Union[OwnershipControlsRule, _Mapping]] = ...) -> None: ...

class S3BucketConfigProto(_message.Message):
    __slots__ = ("versioning_state", "owner_info", "acl", "lifecycle_config", "tag_map", "protocol_type", "swift_container_tag", "init_cluster_id", "init_cluster_incarnation_id", "bucket_policy", "enable_obj_store_access", "ownership_controls", "object_tags_added", "prefix_to_child_bucket_map", "prefix_delimiter", "efficient_mpu_enabled", "max_subfiles_per_mpu", "abac_enabled")
    class VersioningState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kUnVersioned: _ClassVar[S3BucketConfigProto.VersioningState]
        kVersioningEnabled: _ClassVar[S3BucketConfigProto.VersioningState]
        kVersioningSuspended: _ClassVar[S3BucketConfigProto.VersioningState]
    kUnVersioned: S3BucketConfigProto.VersioningState
    kVersioningEnabled: S3BucketConfigProto.VersioningState
    kVersioningSuspended: S3BucketConfigProto.VersioningState
    class TagMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class PrefixToChildBucketMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    VERSIONING_STATE_FIELD_NUMBER: _ClassVar[int]
    OWNER_INFO_FIELD_NUMBER: _ClassVar[int]
    ACL_FIELD_NUMBER: _ClassVar[int]
    LIFECYCLE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    TAG_MAP_FIELD_NUMBER: _ClassVar[int]
    PROTOCOL_TYPE_FIELD_NUMBER: _ClassVar[int]
    SWIFT_CONTAINER_TAG_FIELD_NUMBER: _ClassVar[int]
    INIT_CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    INIT_CLUSTER_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    BUCKET_POLICY_FIELD_NUMBER: _ClassVar[int]
    ENABLE_OBJ_STORE_ACCESS_FIELD_NUMBER: _ClassVar[int]
    OWNERSHIP_CONTROLS_FIELD_NUMBER: _ClassVar[int]
    OBJECT_TAGS_ADDED_FIELD_NUMBER: _ClassVar[int]
    PREFIX_TO_CHILD_BUCKET_MAP_FIELD_NUMBER: _ClassVar[int]
    PREFIX_DELIMITER_FIELD_NUMBER: _ClassVar[int]
    EFFICIENT_MPU_ENABLED_FIELD_NUMBER: _ClassVar[int]
    MAX_SUBFILES_PER_MPU_FIELD_NUMBER: _ClassVar[int]
    ABAC_ENABLED_FIELD_NUMBER: _ClassVar[int]
    versioning_state: S3BucketConfigProto.VersioningState
    owner_info: OwnerInfo
    acl: ACLProto
    lifecycle_config: LifecycleConfigProto
    tag_map: _containers.ScalarMap[str, str]
    protocol_type: ProtocolType
    swift_container_tag: SwiftContainerTaggingProto
    init_cluster_id: int
    init_cluster_incarnation_id: int
    bucket_policy: BucketPolicy
    enable_obj_store_access: bool
    ownership_controls: BucketOwnershipControls
    object_tags_added: bool
    prefix_to_child_bucket_map: _containers.ScalarMap[str, str]
    prefix_delimiter: str
    efficient_mpu_enabled: bool
    max_subfiles_per_mpu: int
    abac_enabled: bool
    def __init__(self, versioning_state: _Optional[_Union[S3BucketConfigProto.VersioningState, str]] = ..., owner_info: _Optional[_Union[OwnerInfo, _Mapping]] = ..., acl: _Optional[_Union[ACLProto, _Mapping]] = ..., lifecycle_config: _Optional[_Union[LifecycleConfigProto, _Mapping]] = ..., tag_map: _Optional[_Mapping[str, str]] = ..., protocol_type: _Optional[_Union[ProtocolType, str]] = ..., swift_container_tag: _Optional[_Union[SwiftContainerTaggingProto, _Mapping]] = ..., init_cluster_id: _Optional[int] = ..., init_cluster_incarnation_id: _Optional[int] = ..., bucket_policy: _Optional[_Union[BucketPolicy, _Mapping]] = ..., enable_obj_store_access: bool = ..., ownership_controls: _Optional[_Union[BucketOwnershipControls, _Mapping]] = ..., object_tags_added: bool = ..., prefix_to_child_bucket_map: _Optional[_Mapping[str, str]] = ..., prefix_delimiter: _Optional[str] = ..., efficient_mpu_enabled: bool = ..., max_subfiles_per_mpu: _Optional[int] = ..., abac_enabled: bool = ...) -> None: ...

class S3KeyMappingConfigProto(_message.Message):
    __slots__ = ("segment_length", "max_segments", "object_snap_tree_enabled")
    SEGMENT_LENGTH_FIELD_NUMBER: _ClassVar[int]
    MAX_SEGMENTS_FIELD_NUMBER: _ClassVar[int]
    OBJECT_SNAP_TREE_ENABLED_FIELD_NUMBER: _ClassVar[int]
    segment_length: int
    max_segments: int
    object_snap_tree_enabled: bool
    def __init__(self, segment_length: _Optional[int] = ..., max_segments: _Optional[int] = ..., object_snap_tree_enabled: bool = ...) -> None: ...

class ObjectFileMetadataProto(_message.Message):
    __slots__ = ("version_id", "owner_info", "acl", "user_defined_metadata_map", "is_null_version", "delete_marker", "etag", "obj_name_with_trailing_slash", "tag_set", "mpu_metadata", "content_type")
    class UserDefinedMetadataMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class TagSetEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class MPUMetadataProto(_message.Message):
        __slots__ = ("subfile_info", "part_entry_vec", "object_size", "cleanup_invalid_parts_data")
        class RLEPartEntry(_message.Message):
            __slots__ = ("number", "size", "count")
            NUMBER_FIELD_NUMBER: _ClassVar[int]
            SIZE_FIELD_NUMBER: _ClassVar[int]
            COUNT_FIELD_NUMBER: _ClassVar[int]
            number: int
            size: int
            count: int
            def __init__(self, number: _Optional[int] = ..., size: _Optional[int] = ..., count: _Optional[int] = ...) -> None: ...
        SUBFILE_INFO_FIELD_NUMBER: _ClassVar[int]
        PART_ENTRY_VEC_FIELD_NUMBER: _ClassVar[int]
        OBJECT_SIZE_FIELD_NUMBER: _ClassVar[int]
        CLEANUP_INVALID_PARTS_DATA_FIELD_NUMBER: _ClassVar[int]
        subfile_info: MPUSubfileInfo
        part_entry_vec: _containers.RepeatedCompositeFieldContainer[ObjectFileMetadataProto.MPUMetadataProto.RLEPartEntry]
        object_size: int
        cleanup_invalid_parts_data: CleanupInvalidPartsData
        def __init__(self, subfile_info: _Optional[_Union[MPUSubfileInfo, _Mapping]] = ..., part_entry_vec: _Optional[_Iterable[_Union[ObjectFileMetadataProto.MPUMetadataProto.RLEPartEntry, _Mapping]]] = ..., object_size: _Optional[int] = ..., cleanup_invalid_parts_data: _Optional[_Union[CleanupInvalidPartsData, _Mapping]] = ...) -> None: ...
    VERSION_ID_FIELD_NUMBER: _ClassVar[int]
    OWNER_INFO_FIELD_NUMBER: _ClassVar[int]
    ACL_FIELD_NUMBER: _ClassVar[int]
    USER_DEFINED_METADATA_MAP_FIELD_NUMBER: _ClassVar[int]
    IS_NULL_VERSION_FIELD_NUMBER: _ClassVar[int]
    DELETE_MARKER_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    OBJ_NAME_WITH_TRAILING_SLASH_FIELD_NUMBER: _ClassVar[int]
    TAG_SET_FIELD_NUMBER: _ClassVar[int]
    MPU_METADATA_FIELD_NUMBER: _ClassVar[int]
    CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    version_id: int
    owner_info: OwnerInfo
    acl: ACLProto
    user_defined_metadata_map: _containers.ScalarMap[str, str]
    is_null_version: bool
    delete_marker: bool
    etag: str
    obj_name_with_trailing_slash: bool
    tag_set: _containers.ScalarMap[str, str]
    mpu_metadata: ObjectFileMetadataProto.MPUMetadataProto
    content_type: str
    def __init__(self, version_id: _Optional[int] = ..., owner_info: _Optional[_Union[OwnerInfo, _Mapping]] = ..., acl: _Optional[_Union[ACLProto, _Mapping]] = ..., user_defined_metadata_map: _Optional[_Mapping[str, str]] = ..., is_null_version: bool = ..., delete_marker: bool = ..., etag: _Optional[str] = ..., obj_name_with_trailing_slash: bool = ..., tag_set: _Optional[_Mapping[str, str]] = ..., mpu_metadata: _Optional[_Union[ObjectFileMetadataProto.MPUMetadataProto, _Mapping]] = ..., content_type: _Optional[str] = ...) -> None: ...

class ObjectDirMetadataProto(_message.Message):
    __slots__ = ("null_version_id", "finalizing_version_id_hint", "finalized_version_vec", "creation_timestamp_vec", "external_object_name", "delete_marker_flag_vec", "object_id", "finalizing_upload_id")
    NULL_VERSION_ID_FIELD_NUMBER: _ClassVar[int]
    FINALIZING_VERSION_ID_HINT_FIELD_NUMBER: _ClassVar[int]
    FINALIZED_VERSION_VEC_FIELD_NUMBER: _ClassVar[int]
    CREATION_TIMESTAMP_VEC_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_OBJECT_NAME_FIELD_NUMBER: _ClassVar[int]
    DELETE_MARKER_FLAG_VEC_FIELD_NUMBER: _ClassVar[int]
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    FINALIZING_UPLOAD_ID_FIELD_NUMBER: _ClassVar[int]
    null_version_id: int
    finalizing_version_id_hint: int
    finalized_version_vec: _containers.RepeatedScalarFieldContainer[int]
    creation_timestamp_vec: _containers.RepeatedScalarFieldContainer[int]
    external_object_name: str
    delete_marker_flag_vec: _containers.RepeatedScalarFieldContainer[bool]
    object_id: _universal_id_pb2.UniversalIdProto
    finalizing_upload_id: int
    def __init__(self, null_version_id: _Optional[int] = ..., finalizing_version_id_hint: _Optional[int] = ..., finalized_version_vec: _Optional[_Iterable[int]] = ..., creation_timestamp_vec: _Optional[_Iterable[int]] = ..., external_object_name: _Optional[str] = ..., delete_marker_flag_vec: _Optional[_Iterable[bool]] = ..., object_id: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., finalizing_upload_id: _Optional[int] = ...) -> None: ...

class EmptyObjectMetadata(_message.Message):
    __slots__ = ("owner_info",)
    OWNER_INFO_FIELD_NUMBER: _ClassVar[int]
    owner_info: OwnerInfo
    def __init__(self, owner_info: _Optional[_Union[OwnerInfo, _Mapping]] = ...) -> None: ...

class MPUSubfileInfo(_message.Message):
    __slots__ = ("max_part_size_mb", "max_parts_per_subfile", "max_subfiles")
    MAX_PART_SIZE_MB_FIELD_NUMBER: _ClassVar[int]
    MAX_PARTS_PER_SUBFILE_FIELD_NUMBER: _ClassVar[int]
    MAX_SUBFILES_FIELD_NUMBER: _ClassVar[int]
    max_part_size_mb: int
    max_parts_per_subfile: int
    max_subfiles: int
    def __init__(self, max_part_size_mb: _Optional[int] = ..., max_parts_per_subfile: _Optional[int] = ..., max_subfiles: _Optional[int] = ...) -> None: ...

class MultiPartUploadMetadataProto(_message.Message):
    __slots__ = ("owner_info", "acl", "user_defined_metadata_map", "object_lock_headers_map", "tag_set", "subfile_info", "content_type")
    class UserDefinedMetadataMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class ObjectLockHeadersMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class TagSetEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    OWNER_INFO_FIELD_NUMBER: _ClassVar[int]
    ACL_FIELD_NUMBER: _ClassVar[int]
    USER_DEFINED_METADATA_MAP_FIELD_NUMBER: _ClassVar[int]
    OBJECT_LOCK_HEADERS_MAP_FIELD_NUMBER: _ClassVar[int]
    TAG_SET_FIELD_NUMBER: _ClassVar[int]
    SUBFILE_INFO_FIELD_NUMBER: _ClassVar[int]
    CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    owner_info: OwnerInfo
    acl: ACLProto
    user_defined_metadata_map: _containers.ScalarMap[str, str]
    object_lock_headers_map: _containers.ScalarMap[str, str]
    tag_set: _containers.ScalarMap[str, str]
    subfile_info: MPUSubfileInfo
    content_type: str
    def __init__(self, owner_info: _Optional[_Union[OwnerInfo, _Mapping]] = ..., acl: _Optional[_Union[ACLProto, _Mapping]] = ..., user_defined_metadata_map: _Optional[_Mapping[str, str]] = ..., object_lock_headers_map: _Optional[_Mapping[str, str]] = ..., tag_set: _Optional[_Mapping[str, str]] = ..., subfile_info: _Optional[_Union[MPUSubfileInfo, _Mapping]] = ..., content_type: _Optional[str] = ...) -> None: ...

class InvalidPartBytesRange(_message.Message):
    __slots__ = ("offset", "length")
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    offset: int
    length: int
    def __init__(self, offset: _Optional[int] = ..., length: _Optional[int] = ...) -> None: ...

class CleanupInvalidPartsData(_message.Message):
    __slots__ = ("part_2_invalid_bytes_map",)
    class Part2InvalidBytesMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: InvalidPartBytesRange
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[InvalidPartBytesRange, _Mapping]] = ...) -> None: ...
    PART_2_INVALID_BYTES_MAP_FIELD_NUMBER: _ClassVar[int]
    part_2_invalid_bytes_map: _containers.MessageMap[int, InvalidPartBytesRange]
    def __init__(self, part_2_invalid_bytes_map: _Optional[_Mapping[int, InvalidPartBytesRange]] = ...) -> None: ...

class PartMetadataProto(_message.Message):
    __slots__ = ("etag", "part_mapping")
    class PartMappingProto(_message.Message):
        __slots__ = ("subfile_name", "part_info_map")
        class PartInfo(_message.Message):
            __slots__ = ("uniquifier", "part_size", "finalized_part_info", "invalid_bytes_range")
            class FinalizedPartInfo(_message.Message):
                __slots__ = ("etag", "mtime_usecs")
                ETAG_FIELD_NUMBER: _ClassVar[int]
                MTIME_USECS_FIELD_NUMBER: _ClassVar[int]
                etag: str
                mtime_usecs: int
                def __init__(self, etag: _Optional[str] = ..., mtime_usecs: _Optional[int] = ...) -> None: ...
            UNIQUIFIER_FIELD_NUMBER: _ClassVar[int]
            PART_SIZE_FIELD_NUMBER: _ClassVar[int]
            FINALIZED_PART_INFO_FIELD_NUMBER: _ClassVar[int]
            INVALID_BYTES_RANGE_FIELD_NUMBER: _ClassVar[int]
            uniquifier: int
            part_size: int
            finalized_part_info: PartMetadataProto.PartMappingProto.PartInfo.FinalizedPartInfo
            invalid_bytes_range: InvalidPartBytesRange
            def __init__(self, uniquifier: _Optional[int] = ..., part_size: _Optional[int] = ..., finalized_part_info: _Optional[_Union[PartMetadataProto.PartMappingProto.PartInfo.FinalizedPartInfo, _Mapping]] = ..., invalid_bytes_range: _Optional[_Union[InvalidPartBytesRange, _Mapping]] = ...) -> None: ...
        class PartInfoMapEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: int
            value: PartMetadataProto.PartMappingProto.PartInfo
            def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[PartMetadataProto.PartMappingProto.PartInfo, _Mapping]] = ...) -> None: ...
        SUBFILE_NAME_FIELD_NUMBER: _ClassVar[int]
        PART_INFO_MAP_FIELD_NUMBER: _ClassVar[int]
        subfile_name: str
        part_info_map: _containers.MessageMap[int, PartMetadataProto.PartMappingProto.PartInfo]
        def __init__(self, subfile_name: _Optional[str] = ..., part_info_map: _Optional[_Mapping[int, PartMetadataProto.PartMappingProto.PartInfo]] = ...) -> None: ...
    ETAG_FIELD_NUMBER: _ClassVar[int]
    PART_MAPPING_FIELD_NUMBER: _ClassVar[int]
    etag: str
    part_mapping: PartMetadataProto.PartMappingProto
    def __init__(self, etag: _Optional[str] = ..., part_mapping: _Optional[_Union[PartMetadataProto.PartMappingProto, _Mapping]] = ...) -> None: ...

class IntentProto(_message.Message):
    __slots__ = ("intent_id_high", "intent_id_low", "fix_intent_deadline_usecs", "is_for_lifecycle", "create_path", "delete_path", "init_object_creation", "finalize_object_creation", "delete_object", "clone_version_file_2_fs", "init_multi_part_upload", "create_part", "complete_multi_part_upload", "delete_multi_part_upload")
    class CreateDeletePath(_message.Message):
        __slots__ = ("base_path", "relative_path", "relative_path_component_idx")
        BASE_PATH_FIELD_NUMBER: _ClassVar[int]
        RELATIVE_PATH_FIELD_NUMBER: _ClassVar[int]
        RELATIVE_PATH_COMPONENT_IDX_FIELD_NUMBER: _ClassVar[int]
        base_path: str
        relative_path: bytes
        relative_path_component_idx: int
        def __init__(self, base_path: _Optional[str] = ..., relative_path: _Optional[bytes] = ..., relative_path_component_idx: _Optional[int] = ...) -> None: ...
    class InitObjectCreation(_message.Message):
        __slots__ = ("object_name", "object_lock_headers_map", "external_object_name", "tag_set", "object_id")
        class ObjectLockHeadersMapEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: str
            def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
        class TagSetEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: str
            def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
        OBJECT_NAME_FIELD_NUMBER: _ClassVar[int]
        OBJECT_LOCK_HEADERS_MAP_FIELD_NUMBER: _ClassVar[int]
        EXTERNAL_OBJECT_NAME_FIELD_NUMBER: _ClassVar[int]
        TAG_SET_FIELD_NUMBER: _ClassVar[int]
        OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
        object_name: str
        object_lock_headers_map: _containers.ScalarMap[str, str]
        external_object_name: str
        tag_set: _containers.ScalarMap[str, str]
        object_id: _universal_id_pb2.UniversalIdProto
        def __init__(self, object_name: _Optional[str] = ..., object_lock_headers_map: _Optional[_Mapping[str, str]] = ..., external_object_name: _Optional[str] = ..., tag_set: _Optional[_Mapping[str, str]] = ..., object_id: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ...) -> None: ...
    class FinalizeObjectCreation(_message.Message):
        __slots__ = ("object_name", "version_id_to_delete", "object_lock_headers_map", "external_object_name", "tag_set", "part_2_invalid_bytes_map")
        class ObjectLockHeadersMapEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: str
            def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
        class TagSetEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: str
            def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
        class Part2InvalidBytesMapEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: int
            value: InvalidPartBytesRange
            def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[InvalidPartBytesRange, _Mapping]] = ...) -> None: ...
        OBJECT_NAME_FIELD_NUMBER: _ClassVar[int]
        VERSION_ID_TO_DELETE_FIELD_NUMBER: _ClassVar[int]
        OBJECT_LOCK_HEADERS_MAP_FIELD_NUMBER: _ClassVar[int]
        EXTERNAL_OBJECT_NAME_FIELD_NUMBER: _ClassVar[int]
        TAG_SET_FIELD_NUMBER: _ClassVar[int]
        PART_2_INVALID_BYTES_MAP_FIELD_NUMBER: _ClassVar[int]
        object_name: str
        version_id_to_delete: int
        object_lock_headers_map: _containers.ScalarMap[str, str]
        external_object_name: str
        tag_set: _containers.ScalarMap[str, str]
        part_2_invalid_bytes_map: _containers.MessageMap[int, InvalidPartBytesRange]
        def __init__(self, object_name: _Optional[str] = ..., version_id_to_delete: _Optional[int] = ..., object_lock_headers_map: _Optional[_Mapping[str, str]] = ..., external_object_name: _Optional[str] = ..., tag_set: _Optional[_Mapping[str, str]] = ..., part_2_invalid_bytes_map: _Optional[_Mapping[int, InvalidPartBytesRange]] = ...) -> None: ...
    class DeleteObject(_message.Message):
        __slots__ = ("object_name", "version_id", "is_current_version", "new_current_version_id", "bypass_governance_retention", "external_object_name", "object_id")
        OBJECT_NAME_FIELD_NUMBER: _ClassVar[int]
        VERSION_ID_FIELD_NUMBER: _ClassVar[int]
        IS_CURRENT_VERSION_FIELD_NUMBER: _ClassVar[int]
        NEW_CURRENT_VERSION_ID_FIELD_NUMBER: _ClassVar[int]
        BYPASS_GOVERNANCE_RETENTION_FIELD_NUMBER: _ClassVar[int]
        EXTERNAL_OBJECT_NAME_FIELD_NUMBER: _ClassVar[int]
        OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
        object_name: str
        version_id: int
        is_current_version: bool
        new_current_version_id: int
        bypass_governance_retention: bool
        external_object_name: str
        object_id: _universal_id_pb2.UniversalIdProto
        def __init__(self, object_name: _Optional[str] = ..., version_id: _Optional[int] = ..., is_current_version: bool = ..., new_current_version_id: _Optional[int] = ..., bypass_governance_retention: bool = ..., external_object_name: _Optional[str] = ..., object_id: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ...) -> None: ...
    class CloneVersionFile2Fs(_message.Message):
        __slots__ = ("object_name",)
        OBJECT_NAME_FIELD_NUMBER: _ClassVar[int]
        object_name: str
        def __init__(self, object_name: _Optional[str] = ...) -> None: ...
    class InitMultiPartUpload(_message.Message):
        __slots__ = ("object_name", "upload_id", "object_lock_headers_map", "tag_set", "external_object_name")
        class ObjectLockHeadersMapEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: str
            def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
        class TagSetEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: str
            def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
        OBJECT_NAME_FIELD_NUMBER: _ClassVar[int]
        UPLOAD_ID_FIELD_NUMBER: _ClassVar[int]
        OBJECT_LOCK_HEADERS_MAP_FIELD_NUMBER: _ClassVar[int]
        TAG_SET_FIELD_NUMBER: _ClassVar[int]
        EXTERNAL_OBJECT_NAME_FIELD_NUMBER: _ClassVar[int]
        object_name: str
        upload_id: int
        object_lock_headers_map: _containers.ScalarMap[str, str]
        tag_set: _containers.ScalarMap[str, str]
        external_object_name: str
        def __init__(self, object_name: _Optional[str] = ..., upload_id: _Optional[int] = ..., object_lock_headers_map: _Optional[_Mapping[str, str]] = ..., tag_set: _Optional[_Mapping[str, str]] = ..., external_object_name: _Optional[str] = ...) -> None: ...
    class CreatePart(_message.Message):
        __slots__ = ("object_name", "upload_id", "part_number")
        OBJECT_NAME_FIELD_NUMBER: _ClassVar[int]
        UPLOAD_ID_FIELD_NUMBER: _ClassVar[int]
        PART_NUMBER_FIELD_NUMBER: _ClassVar[int]
        object_name: str
        upload_id: int
        part_number: int
        def __init__(self, object_name: _Optional[str] = ..., upload_id: _Optional[int] = ..., part_number: _Optional[int] = ...) -> None: ...
    class CompleteMultiPartUpload(_message.Message):
        __slots__ = ("object_name", "upload_id", "ordered_part_info_vec", "object_etag", "object_lock_headers_map", "external_object_name", "tag_set", "part_2_invalid_bytes_map")
        class PartInfo(_message.Message):
            __slots__ = ("part_number", "inode_id", "part_logical_size")
            PART_NUMBER_FIELD_NUMBER: _ClassVar[int]
            INODE_ID_FIELD_NUMBER: _ClassVar[int]
            PART_LOGICAL_SIZE_FIELD_NUMBER: _ClassVar[int]
            part_number: int
            inode_id: int
            part_logical_size: int
            def __init__(self, part_number: _Optional[int] = ..., inode_id: _Optional[int] = ..., part_logical_size: _Optional[int] = ...) -> None: ...
        class ObjectLockHeadersMapEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: str
            def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
        class TagSetEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: str
            def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
        class Part2InvalidBytesMapEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: int
            value: InvalidPartBytesRange
            def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[InvalidPartBytesRange, _Mapping]] = ...) -> None: ...
        OBJECT_NAME_FIELD_NUMBER: _ClassVar[int]
        UPLOAD_ID_FIELD_NUMBER: _ClassVar[int]
        ORDERED_PART_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
        OBJECT_ETAG_FIELD_NUMBER: _ClassVar[int]
        OBJECT_LOCK_HEADERS_MAP_FIELD_NUMBER: _ClassVar[int]
        EXTERNAL_OBJECT_NAME_FIELD_NUMBER: _ClassVar[int]
        TAG_SET_FIELD_NUMBER: _ClassVar[int]
        PART_2_INVALID_BYTES_MAP_FIELD_NUMBER: _ClassVar[int]
        object_name: str
        upload_id: int
        ordered_part_info_vec: _containers.RepeatedCompositeFieldContainer[IntentProto.CompleteMultiPartUpload.PartInfo]
        object_etag: str
        object_lock_headers_map: _containers.ScalarMap[str, str]
        external_object_name: str
        tag_set: _containers.ScalarMap[str, str]
        part_2_invalid_bytes_map: _containers.MessageMap[int, InvalidPartBytesRange]
        def __init__(self, object_name: _Optional[str] = ..., upload_id: _Optional[int] = ..., ordered_part_info_vec: _Optional[_Iterable[_Union[IntentProto.CompleteMultiPartUpload.PartInfo, _Mapping]]] = ..., object_etag: _Optional[str] = ..., object_lock_headers_map: _Optional[_Mapping[str, str]] = ..., external_object_name: _Optional[str] = ..., tag_set: _Optional[_Mapping[str, str]] = ..., part_2_invalid_bytes_map: _Optional[_Mapping[int, InvalidPartBytesRange]] = ...) -> None: ...
    class DeleteMultiPartUpload(_message.Message):
        __slots__ = ("object_name", "upload_id", "finalized_file_object_id", "finalized_file_version_id")
        OBJECT_NAME_FIELD_NUMBER: _ClassVar[int]
        UPLOAD_ID_FIELD_NUMBER: _ClassVar[int]
        FINALIZED_FILE_OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
        FINALIZED_FILE_VERSION_ID_FIELD_NUMBER: _ClassVar[int]
        object_name: str
        upload_id: int
        finalized_file_object_id: _universal_id_pb2.UniversalIdProto
        finalized_file_version_id: int
        def __init__(self, object_name: _Optional[str] = ..., upload_id: _Optional[int] = ..., finalized_file_object_id: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., finalized_file_version_id: _Optional[int] = ...) -> None: ...
    INTENT_ID_HIGH_FIELD_NUMBER: _ClassVar[int]
    INTENT_ID_LOW_FIELD_NUMBER: _ClassVar[int]
    FIX_INTENT_DEADLINE_USECS_FIELD_NUMBER: _ClassVar[int]
    IS_FOR_LIFECYCLE_FIELD_NUMBER: _ClassVar[int]
    CREATE_PATH_FIELD_NUMBER: _ClassVar[int]
    DELETE_PATH_FIELD_NUMBER: _ClassVar[int]
    INIT_OBJECT_CREATION_FIELD_NUMBER: _ClassVar[int]
    FINALIZE_OBJECT_CREATION_FIELD_NUMBER: _ClassVar[int]
    DELETE_OBJECT_FIELD_NUMBER: _ClassVar[int]
    CLONE_VERSION_FILE_2_FS_FIELD_NUMBER: _ClassVar[int]
    INIT_MULTI_PART_UPLOAD_FIELD_NUMBER: _ClassVar[int]
    CREATE_PART_FIELD_NUMBER: _ClassVar[int]
    COMPLETE_MULTI_PART_UPLOAD_FIELD_NUMBER: _ClassVar[int]
    DELETE_MULTI_PART_UPLOAD_FIELD_NUMBER: _ClassVar[int]
    intent_id_high: int
    intent_id_low: int
    fix_intent_deadline_usecs: int
    is_for_lifecycle: bool
    create_path: IntentProto.CreateDeletePath
    delete_path: IntentProto.CreateDeletePath
    init_object_creation: IntentProto.InitObjectCreation
    finalize_object_creation: IntentProto.FinalizeObjectCreation
    delete_object: IntentProto.DeleteObject
    clone_version_file_2_fs: IntentProto.CloneVersionFile2Fs
    init_multi_part_upload: IntentProto.InitMultiPartUpload
    create_part: IntentProto.CreatePart
    complete_multi_part_upload: IntentProto.CompleteMultiPartUpload
    delete_multi_part_upload: IntentProto.DeleteMultiPartUpload
    def __init__(self, intent_id_high: _Optional[int] = ..., intent_id_low: _Optional[int] = ..., fix_intent_deadline_usecs: _Optional[int] = ..., is_for_lifecycle: bool = ..., create_path: _Optional[_Union[IntentProto.CreateDeletePath, _Mapping]] = ..., delete_path: _Optional[_Union[IntentProto.CreateDeletePath, _Mapping]] = ..., init_object_creation: _Optional[_Union[IntentProto.InitObjectCreation, _Mapping]] = ..., finalize_object_creation: _Optional[_Union[IntentProto.FinalizeObjectCreation, _Mapping]] = ..., delete_object: _Optional[_Union[IntentProto.DeleteObject, _Mapping]] = ..., clone_version_file_2_fs: _Optional[_Union[IntentProto.CloneVersionFile2Fs, _Mapping]] = ..., init_multi_part_upload: _Optional[_Union[IntentProto.InitMultiPartUpload, _Mapping]] = ..., create_part: _Optional[_Union[IntentProto.CreatePart, _Mapping]] = ..., complete_multi_part_upload: _Optional[_Union[IntentProto.CompleteMultiPartUpload, _Mapping]] = ..., delete_multi_part_upload: _Optional[_Union[IntentProto.DeleteMultiPartUpload, _Mapping]] = ...) -> None: ...

class S3ObjectSnapTreeValueProto(_message.Message):
    __slots__ = ("object_id", "intent", "cluster_id", "cluster_incarnation_id", "object_leaf_dir_inode_id")
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    INTENT_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_LEAF_DIR_INODE_ID_FIELD_NUMBER: _ClassVar[int]
    object_id: int
    intent: IntentProto
    cluster_id: int
    cluster_incarnation_id: int
    object_leaf_dir_inode_id: int
    def __init__(self, object_id: _Optional[int] = ..., intent: _Optional[_Union[IntentProto, _Mapping]] = ..., cluster_id: _Optional[int] = ..., cluster_incarnation_id: _Optional[int] = ..., object_leaf_dir_inode_id: _Optional[int] = ...) -> None: ...
