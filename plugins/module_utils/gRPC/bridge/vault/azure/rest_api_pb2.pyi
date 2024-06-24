from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetImmutabilityPolicyResponse(_message.Message):
    __slots__ = ("properties",)
    class Properties(_message.Message):
        __slots__ = ("immutability_period_since_creation_in_days", "allow_protected_append_writes", "state")
        IMMUTABILITY_PERIOD_SINCE_CREATION_IN_DAYS_FIELD_NUMBER: _ClassVar[int]
        ALLOW_PROTECTED_APPEND_WRITES_FIELD_NUMBER: _ClassVar[int]
        STATE_FIELD_NUMBER: _ClassVar[int]
        immutability_period_since_creation_in_days: int
        allow_protected_append_writes: bool
        state: str
        def __init__(self, immutability_period_since_creation_in_days: _Optional[int] = ..., allow_protected_append_writes: bool = ..., state: _Optional[str] = ...) -> None: ...
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    properties: GetImmutabilityPolicyResponse.Properties
    def __init__(self, properties: _Optional[_Union[GetImmutabilityPolicyResponse.Properties, _Mapping]] = ...) -> None: ...

class GetOAuth2AccessTokenResponse(_message.Message):
    __slots__ = ("token_type", "access_token", "expires_in")
    TOKEN_TYPE_FIELD_NUMBER: _ClassVar[int]
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_IN_FIELD_NUMBER: _ClassVar[int]
    token_type: str
    access_token: str
    expires_in: int
    def __init__(self, token_type: _Optional[str] = ..., access_token: _Optional[str] = ..., expires_in: _Optional[int] = ...) -> None: ...

class GetManagementPoliciesResponse(_message.Message):
    __slots__ = ("properties",)
    class Properties(_message.Message):
        __slots__ = ("policy", "last_modified_time")
        class Policy(_message.Message):
            __slots__ = ("rules",)
            class Rule(_message.Message):
                __slots__ = ("enabled", "name", "type", "definition")
                class Definition(_message.Message):
                    __slots__ = ("actions", "filters")
                    class Actions(_message.Message):
                        __slots__ = ("base_blob", "snapshot", "version")
                        class DateAfterModification(_message.Message):
                            __slots__ = ("days_after_creation_greater_than", "days_after_last_access_time_greater_than", "days_after_last_tier_change_greater_than", "days_after_modification_greater_than")
                            DAYS_AFTER_CREATION_GREATER_THAN_FIELD_NUMBER: _ClassVar[int]
                            DAYS_AFTER_LAST_ACCESS_TIME_GREATER_THAN_FIELD_NUMBER: _ClassVar[int]
                            DAYS_AFTER_LAST_TIER_CHANGE_GREATER_THAN_FIELD_NUMBER: _ClassVar[int]
                            DAYS_AFTER_MODIFICATION_GREATER_THAN_FIELD_NUMBER: _ClassVar[int]
                            days_after_creation_greater_than: int
                            days_after_last_access_time_greater_than: int
                            days_after_last_tier_change_greater_than: int
                            days_after_modification_greater_than: int
                            def __init__(self, days_after_creation_greater_than: _Optional[int] = ..., days_after_last_access_time_greater_than: _Optional[int] = ..., days_after_last_tier_change_greater_than: _Optional[int] = ..., days_after_modification_greater_than: _Optional[int] = ...) -> None: ...
                        class BaseBlobActions(_message.Message):
                            __slots__ = ("delete", "enable_auto_tier_to_hot_from_cool", "tier_to_archive", "tier_to_cool")
                            DELETE_FIELD_NUMBER: _ClassVar[int]
                            ENABLE_AUTO_TIER_TO_HOT_FROM_COOL_FIELD_NUMBER: _ClassVar[int]
                            TIER_TO_ARCHIVE_FIELD_NUMBER: _ClassVar[int]
                            TIER_TO_COOL_FIELD_NUMBER: _ClassVar[int]
                            delete: GetManagementPoliciesResponse.Properties.Policy.Rule.Definition.Actions.DateAfterModification
                            enable_auto_tier_to_hot_from_cool: bool
                            tier_to_archive: GetManagementPoliciesResponse.Properties.Policy.Rule.Definition.Actions.DateAfterModification
                            tier_to_cool: GetManagementPoliciesResponse.Properties.Policy.Rule.Definition.Actions.DateAfterModification
                            def __init__(self, delete: _Optional[_Union[GetManagementPoliciesResponse.Properties.Policy.Rule.Definition.Actions.DateAfterModification, _Mapping]] = ..., enable_auto_tier_to_hot_from_cool: bool = ..., tier_to_archive: _Optional[_Union[GetManagementPoliciesResponse.Properties.Policy.Rule.Definition.Actions.DateAfterModification, _Mapping]] = ..., tier_to_cool: _Optional[_Union[GetManagementPoliciesResponse.Properties.Policy.Rule.Definition.Actions.DateAfterModification, _Mapping]] = ...) -> None: ...
                        class SnapshotActions(_message.Message):
                            __slots__ = ("delete", "tier_to_archive", "tier_to_cool")
                            DELETE_FIELD_NUMBER: _ClassVar[int]
                            TIER_TO_ARCHIVE_FIELD_NUMBER: _ClassVar[int]
                            TIER_TO_COOL_FIELD_NUMBER: _ClassVar[int]
                            delete: GetManagementPoliciesResponse.Properties.Policy.Rule.Definition.Actions.DateAfterModification
                            tier_to_archive: GetManagementPoliciesResponse.Properties.Policy.Rule.Definition.Actions.DateAfterModification
                            tier_to_cool: GetManagementPoliciesResponse.Properties.Policy.Rule.Definition.Actions.DateAfterModification
                            def __init__(self, delete: _Optional[_Union[GetManagementPoliciesResponse.Properties.Policy.Rule.Definition.Actions.DateAfterModification, _Mapping]] = ..., tier_to_archive: _Optional[_Union[GetManagementPoliciesResponse.Properties.Policy.Rule.Definition.Actions.DateAfterModification, _Mapping]] = ..., tier_to_cool: _Optional[_Union[GetManagementPoliciesResponse.Properties.Policy.Rule.Definition.Actions.DateAfterModification, _Mapping]] = ...) -> None: ...
                        class VersionActions(_message.Message):
                            __slots__ = ("delete", "tier_to_archive", "tier_to_cool")
                            DELETE_FIELD_NUMBER: _ClassVar[int]
                            TIER_TO_ARCHIVE_FIELD_NUMBER: _ClassVar[int]
                            TIER_TO_COOL_FIELD_NUMBER: _ClassVar[int]
                            delete: GetManagementPoliciesResponse.Properties.Policy.Rule.Definition.Actions.DateAfterModification
                            tier_to_archive: GetManagementPoliciesResponse.Properties.Policy.Rule.Definition.Actions.DateAfterModification
                            tier_to_cool: GetManagementPoliciesResponse.Properties.Policy.Rule.Definition.Actions.DateAfterModification
                            def __init__(self, delete: _Optional[_Union[GetManagementPoliciesResponse.Properties.Policy.Rule.Definition.Actions.DateAfterModification, _Mapping]] = ..., tier_to_archive: _Optional[_Union[GetManagementPoliciesResponse.Properties.Policy.Rule.Definition.Actions.DateAfterModification, _Mapping]] = ..., tier_to_cool: _Optional[_Union[GetManagementPoliciesResponse.Properties.Policy.Rule.Definition.Actions.DateAfterModification, _Mapping]] = ...) -> None: ...
                        BASE_BLOB_FIELD_NUMBER: _ClassVar[int]
                        SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
                        VERSION_FIELD_NUMBER: _ClassVar[int]
                        base_blob: GetManagementPoliciesResponse.Properties.Policy.Rule.Definition.Actions.BaseBlobActions
                        snapshot: GetManagementPoliciesResponse.Properties.Policy.Rule.Definition.Actions.SnapshotActions
                        version: GetManagementPoliciesResponse.Properties.Policy.Rule.Definition.Actions.VersionActions
                        def __init__(self, base_blob: _Optional[_Union[GetManagementPoliciesResponse.Properties.Policy.Rule.Definition.Actions.BaseBlobActions, _Mapping]] = ..., snapshot: _Optional[_Union[GetManagementPoliciesResponse.Properties.Policy.Rule.Definition.Actions.SnapshotActions, _Mapping]] = ..., version: _Optional[_Union[GetManagementPoliciesResponse.Properties.Policy.Rule.Definition.Actions.VersionActions, _Mapping]] = ...) -> None: ...
                    class Filters(_message.Message):
                        __slots__ = ("blob_types", "prefix_match")
                        BLOB_TYPES_FIELD_NUMBER: _ClassVar[int]
                        PREFIX_MATCH_FIELD_NUMBER: _ClassVar[int]
                        blob_types: _containers.RepeatedScalarFieldContainer[str]
                        prefix_match: _containers.RepeatedScalarFieldContainer[str]
                        def __init__(self, blob_types: _Optional[_Iterable[str]] = ..., prefix_match: _Optional[_Iterable[str]] = ...) -> None: ...
                    ACTIONS_FIELD_NUMBER: _ClassVar[int]
                    FILTERS_FIELD_NUMBER: _ClassVar[int]
                    actions: GetManagementPoliciesResponse.Properties.Policy.Rule.Definition.Actions
                    filters: GetManagementPoliciesResponse.Properties.Policy.Rule.Definition.Filters
                    def __init__(self, actions: _Optional[_Union[GetManagementPoliciesResponse.Properties.Policy.Rule.Definition.Actions, _Mapping]] = ..., filters: _Optional[_Union[GetManagementPoliciesResponse.Properties.Policy.Rule.Definition.Filters, _Mapping]] = ...) -> None: ...
                ENABLED_FIELD_NUMBER: _ClassVar[int]
                NAME_FIELD_NUMBER: _ClassVar[int]
                TYPE_FIELD_NUMBER: _ClassVar[int]
                DEFINITION_FIELD_NUMBER: _ClassVar[int]
                enabled: bool
                name: str
                type: str
                definition: GetManagementPoliciesResponse.Properties.Policy.Rule.Definition
                def __init__(self, enabled: bool = ..., name: _Optional[str] = ..., type: _Optional[str] = ..., definition: _Optional[_Union[GetManagementPoliciesResponse.Properties.Policy.Rule.Definition, _Mapping]] = ...) -> None: ...
            RULES_FIELD_NUMBER: _ClassVar[int]
            rules: _containers.RepeatedCompositeFieldContainer[GetManagementPoliciesResponse.Properties.Policy.Rule]
            def __init__(self, rules: _Optional[_Iterable[_Union[GetManagementPoliciesResponse.Properties.Policy.Rule, _Mapping]]] = ...) -> None: ...
        POLICY_FIELD_NUMBER: _ClassVar[int]
        LAST_MODIFIED_TIME_FIELD_NUMBER: _ClassVar[int]
        policy: GetManagementPoliciesResponse.Properties.Policy
        last_modified_time: str
        def __init__(self, policy: _Optional[_Union[GetManagementPoliciesResponse.Properties.Policy, _Mapping]] = ..., last_modified_time: _Optional[str] = ...) -> None: ...
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    properties: GetManagementPoliciesResponse.Properties
    def __init__(self, properties: _Optional[_Union[GetManagementPoliciesResponse.Properties, _Mapping]] = ...) -> None: ...
