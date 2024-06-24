from magneto.base import error_pb2 as _error_pb2
from magneto.connectors.file import file_pb2 as _file_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ExportPolicyInfo(_message.Message):
    __slots__ = ("policy_name", "export_rule_vec", "failed_export_rule_vec")
    class ExportRuleInfo(_message.Message):
        __slots__ = ("index", "client_match", "access_protocol_vec", "read_only_sf_vec", "read_write_sf_vec", "super_user_sf_vec", "access")
        class AccessProtocol(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kAny: _ClassVar[ExportPolicyInfo.ExportRuleInfo.AccessProtocol]
            kNfs: _ClassVar[ExportPolicyInfo.ExportRuleInfo.AccessProtocol]
            kNfs2: _ClassVar[ExportPolicyInfo.ExportRuleInfo.AccessProtocol]
            kNfs3: _ClassVar[ExportPolicyInfo.ExportRuleInfo.AccessProtocol]
            kNfs4: _ClassVar[ExportPolicyInfo.ExportRuleInfo.AccessProtocol]
            kCifs: _ClassVar[ExportPolicyInfo.ExportRuleInfo.AccessProtocol]
            kFlexcache: _ClassVar[ExportPolicyInfo.ExportRuleInfo.AccessProtocol]
        kAny: ExportPolicyInfo.ExportRuleInfo.AccessProtocol
        kNfs: ExportPolicyInfo.ExportRuleInfo.AccessProtocol
        kNfs2: ExportPolicyInfo.ExportRuleInfo.AccessProtocol
        kNfs3: ExportPolicyInfo.ExportRuleInfo.AccessProtocol
        kNfs4: ExportPolicyInfo.ExportRuleInfo.AccessProtocol
        kCifs: ExportPolicyInfo.ExportRuleInfo.AccessProtocol
        kFlexcache: ExportPolicyInfo.ExportRuleInfo.AccessProtocol
        class SecurityFlavor(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kSfAny: _ClassVar[ExportPolicyInfo.ExportRuleInfo.SecurityFlavor]
            kNone: _ClassVar[ExportPolicyInfo.ExportRuleInfo.SecurityFlavor]
            kNever: _ClassVar[ExportPolicyInfo.ExportRuleInfo.SecurityFlavor]
            kKrb5: _ClassVar[ExportPolicyInfo.ExportRuleInfo.SecurityFlavor]
            kKrb5i: _ClassVar[ExportPolicyInfo.ExportRuleInfo.SecurityFlavor]
            kKrb5p: _ClassVar[ExportPolicyInfo.ExportRuleInfo.SecurityFlavor]
            kNtlm: _ClassVar[ExportPolicyInfo.ExportRuleInfo.SecurityFlavor]
            kSys: _ClassVar[ExportPolicyInfo.ExportRuleInfo.SecurityFlavor]
        kSfAny: ExportPolicyInfo.ExportRuleInfo.SecurityFlavor
        kNone: ExportPolicyInfo.ExportRuleInfo.SecurityFlavor
        kNever: ExportPolicyInfo.ExportRuleInfo.SecurityFlavor
        kKrb5: ExportPolicyInfo.ExportRuleInfo.SecurityFlavor
        kKrb5i: ExportPolicyInfo.ExportRuleInfo.SecurityFlavor
        kKrb5p: ExportPolicyInfo.ExportRuleInfo.SecurityFlavor
        kNtlm: ExportPolicyInfo.ExportRuleInfo.SecurityFlavor
        kSys: ExportPolicyInfo.ExportRuleInfo.SecurityFlavor
        class AccessType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kRead: _ClassVar[ExportPolicyInfo.ExportRuleInfo.AccessType]
            kReadWrite: _ClassVar[ExportPolicyInfo.ExportRuleInfo.AccessType]
            kDenied: _ClassVar[ExportPolicyInfo.ExportRuleInfo.AccessType]
        kRead: ExportPolicyInfo.ExportRuleInfo.AccessType
        kReadWrite: ExportPolicyInfo.ExportRuleInfo.AccessType
        kDenied: ExportPolicyInfo.ExportRuleInfo.AccessType
        INDEX_FIELD_NUMBER: _ClassVar[int]
        CLIENT_MATCH_FIELD_NUMBER: _ClassVar[int]
        ACCESS_PROTOCOL_VEC_FIELD_NUMBER: _ClassVar[int]
        READ_ONLY_SF_VEC_FIELD_NUMBER: _ClassVar[int]
        READ_WRITE_SF_VEC_FIELD_NUMBER: _ClassVar[int]
        SUPER_USER_SF_VEC_FIELD_NUMBER: _ClassVar[int]
        ACCESS_FIELD_NUMBER: _ClassVar[int]
        index: int
        client_match: str
        access_protocol_vec: _containers.RepeatedScalarFieldContainer[ExportPolicyInfo.ExportRuleInfo.AccessProtocol]
        read_only_sf_vec: _containers.RepeatedScalarFieldContainer[ExportPolicyInfo.ExportRuleInfo.SecurityFlavor]
        read_write_sf_vec: _containers.RepeatedScalarFieldContainer[ExportPolicyInfo.ExportRuleInfo.SecurityFlavor]
        super_user_sf_vec: _containers.RepeatedScalarFieldContainer[ExportPolicyInfo.ExportRuleInfo.SecurityFlavor]
        access: ExportPolicyInfo.ExportRuleInfo.AccessType
        def __init__(self, index: _Optional[int] = ..., client_match: _Optional[str] = ..., access_protocol_vec: _Optional[_Iterable[_Union[ExportPolicyInfo.ExportRuleInfo.AccessProtocol, str]]] = ..., read_only_sf_vec: _Optional[_Iterable[_Union[ExportPolicyInfo.ExportRuleInfo.SecurityFlavor, str]]] = ..., read_write_sf_vec: _Optional[_Iterable[_Union[ExportPolicyInfo.ExportRuleInfo.SecurityFlavor, str]]] = ..., super_user_sf_vec: _Optional[_Iterable[_Union[ExportPolicyInfo.ExportRuleInfo.SecurityFlavor, str]]] = ..., access: _Optional[_Union[ExportPolicyInfo.ExportRuleInfo.AccessType, str]] = ...) -> None: ...
    class FailedExportRule(_message.Message):
        __slots__ = ("rule", "error")
        RULE_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        rule: ExportPolicyInfo.ExportRuleInfo
        error: _error_pb2.ErrorProto
        def __init__(self, rule: _Optional[_Union[ExportPolicyInfo.ExportRuleInfo, _Mapping]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...
    POLICY_NAME_FIELD_NUMBER: _ClassVar[int]
    EXPORT_RULE_VEC_FIELD_NUMBER: _ClassVar[int]
    FAILED_EXPORT_RULE_VEC_FIELD_NUMBER: _ClassVar[int]
    policy_name: str
    export_rule_vec: _containers.RepeatedCompositeFieldContainer[ExportPolicyInfo.ExportRuleInfo]
    failed_export_rule_vec: _containers.RepeatedCompositeFieldContainer[ExportPolicyInfo.FailedExportRule]
    def __init__(self, policy_name: _Optional[str] = ..., export_rule_vec: _Optional[_Iterable[_Union[ExportPolicyInfo.ExportRuleInfo, _Mapping]]] = ..., failed_export_rule_vec: _Optional[_Iterable[_Union[ExportPolicyInfo.FailedExportRule, _Mapping]]] = ...) -> None: ...

class SecuritySslInfo(_message.Message):
    __slots__ = ("server_authentication_enabled",)
    SERVER_AUTHENTICATION_ENABLED_FIELD_NUMBER: _ClassVar[int]
    server_authentication_enabled: bool
    def __init__(self, server_authentication_enabled: bool = ...) -> None: ...

class ChangeEntry(_message.Message):
    __slots__ = ("inode", "change_type", "is_creation_bit_set", "is_modify_bit_set")
    class ChangeType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kFileDeletion: _ClassVar[ChangeEntry.ChangeType]
        kFileCreation: _ClassVar[ChangeEntry.ChangeType]
        kInodeModification: _ClassVar[ChangeEntry.ChangeType]
    kFileDeletion: ChangeEntry.ChangeType
    kFileCreation: ChangeEntry.ChangeType
    kInodeModification: ChangeEntry.ChangeType
    NETAPP_ENTRY_FIELD_NUMBER: _ClassVar[int]
    netapp_entry: _descriptor.FieldDescriptor
    INODE_FIELD_NUMBER: _ClassVar[int]
    CHANGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    IS_CREATION_BIT_SET_FIELD_NUMBER: _ClassVar[int]
    IS_MODIFY_BIT_SET_FIELD_NUMBER: _ClassVar[int]
    inode: int
    change_type: ChangeEntry.ChangeType
    is_creation_bit_set: bool
    is_modify_bit_set: bool
    def __init__(self, inode: _Optional[int] = ..., change_type: _Optional[_Union[ChangeEntry.ChangeType, str]] = ..., is_creation_bit_set: bool = ..., is_modify_bit_set: bool = ...) -> None: ...

class SnapChangeInfoCache(_message.Message):
    __slots__ = ("deleted_inode_map", "total_create_events", "total_delete_events", "total_modify_events")
    class DeletedInodeMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: str
        def __init__(self, key: _Optional[int] = ..., value: _Optional[str] = ...) -> None: ...
    NETAPP_SNAP_CHANGE_INFO_CACHE_FIELD_NUMBER: _ClassVar[int]
    netapp_snap_change_info_cache: _descriptor.FieldDescriptor
    DELETED_INODE_MAP_FIELD_NUMBER: _ClassVar[int]
    TOTAL_CREATE_EVENTS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_DELETE_EVENTS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_MODIFY_EVENTS_FIELD_NUMBER: _ClassVar[int]
    deleted_inode_map: _containers.ScalarMap[int, str]
    total_create_events: int
    total_delete_events: int
    total_modify_events: int
    def __init__(self, deleted_inode_map: _Optional[_Mapping[int, str]] = ..., total_create_events: _Optional[int] = ..., total_delete_events: _Optional[int] = ..., total_modify_events: _Optional[int] = ...) -> None: ...

class SnapshotInfo(_message.Message):
    __slots__ = ("skip_adding_export_rule", "cohesity_export_rule_index", "export_policy_name", "changelist_state", "pagination_resume_token", "snapmirror_transfer_info", "snapmirror_objectstore_info", "snapshot_expiry_extension_error")
    class SnapdiffState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNotStarted: _ClassVar[SnapshotInfo.SnapdiffState]
        kCreateRequestSent: _ClassVar[SnapshotInfo.SnapdiffState]
        kCreated: _ClassVar[SnapshotInfo.SnapdiffState]
        kFullyIngested: _ClassVar[SnapshotInfo.SnapdiffState]
        kDeleted: _ClassVar[SnapshotInfo.SnapdiffState]
    kNotStarted: SnapshotInfo.SnapdiffState
    kCreateRequestSent: SnapshotInfo.SnapdiffState
    kCreated: SnapshotInfo.SnapdiffState
    kFullyIngested: SnapshotInfo.SnapdiffState
    kDeleted: SnapshotInfo.SnapdiffState
    class SnapmirrorTransferInfo(_message.Message):
        __slots__ = ("pre_transfer_exported_snapshot", "post_transfer_exported_snapshot", "transfer_uuid")
        PRE_TRANSFER_EXPORTED_SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
        POST_TRANSFER_EXPORTED_SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
        TRANSFER_UUID_FIELD_NUMBER: _ClassVar[int]
        pre_transfer_exported_snapshot: str
        post_transfer_exported_snapshot: str
        transfer_uuid: str
        def __init__(self, pre_transfer_exported_snapshot: _Optional[str] = ..., post_transfer_exported_snapshot: _Optional[str] = ..., transfer_uuid: _Optional[str] = ...) -> None: ...
    NETAPP_SNAPSHOT_INFO_FIELD_NUMBER: _ClassVar[int]
    netapp_snapshot_info: _descriptor.FieldDescriptor
    SKIP_ADDING_EXPORT_RULE_FIELD_NUMBER: _ClassVar[int]
    COHESITY_EXPORT_RULE_INDEX_FIELD_NUMBER: _ClassVar[int]
    EXPORT_POLICY_NAME_FIELD_NUMBER: _ClassVar[int]
    CHANGELIST_STATE_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_RESUME_TOKEN_FIELD_NUMBER: _ClassVar[int]
    SNAPMIRROR_TRANSFER_INFO_FIELD_NUMBER: _ClassVar[int]
    SNAPMIRROR_OBJECTSTORE_INFO_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_EXPIRY_EXTENSION_ERROR_FIELD_NUMBER: _ClassVar[int]
    skip_adding_export_rule: bool
    cohesity_export_rule_index: int
    export_policy_name: str
    changelist_state: SnapshotInfo.SnapdiffState
    pagination_resume_token: bytes
    snapmirror_transfer_info: SnapshotInfo.SnapmirrorTransferInfo
    snapmirror_objectstore_info: SnapmirrorObjectStoreInfo
    snapshot_expiry_extension_error: _error_pb2.ErrorProto
    def __init__(self, skip_adding_export_rule: bool = ..., cohesity_export_rule_index: _Optional[int] = ..., export_policy_name: _Optional[str] = ..., changelist_state: _Optional[_Union[SnapshotInfo.SnapdiffState, str]] = ..., pagination_resume_token: _Optional[bytes] = ..., snapmirror_transfer_info: _Optional[_Union[SnapshotInfo.SnapmirrorTransferInfo, _Mapping]] = ..., snapmirror_objectstore_info: _Optional[_Union[SnapmirrorObjectStoreInfo, _Mapping]] = ..., snapshot_expiry_extension_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class SnapmirrorObjectStoreInfo(_message.Message):
    __slots__ = ("objectstore_config_name", "destination_ep_uuid", "relationship_uuid", "view_name", "view_id", "object_store_config_uuid", "snapshot_uuid", "snapshot_instance_uuid", "data_transfer_start_time_usec")
    OBJECTSTORE_CONFIG_NAME_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_EP_UUID_FIELD_NUMBER: _ClassVar[int]
    RELATIONSHIP_UUID_FIELD_NUMBER: _ClassVar[int]
    VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    VIEW_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_STORE_CONFIG_UUID_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_UUID_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_INSTANCE_UUID_FIELD_NUMBER: _ClassVar[int]
    DATA_TRANSFER_START_TIME_USEC_FIELD_NUMBER: _ClassVar[int]
    objectstore_config_name: str
    destination_ep_uuid: str
    relationship_uuid: str
    view_name: str
    view_id: int
    object_store_config_uuid: str
    snapshot_uuid: str
    snapshot_instance_uuid: str
    data_transfer_start_time_usec: int
    def __init__(self, objectstore_config_name: _Optional[str] = ..., destination_ep_uuid: _Optional[str] = ..., relationship_uuid: _Optional[str] = ..., view_name: _Optional[str] = ..., view_id: _Optional[int] = ..., object_store_config_uuid: _Optional[str] = ..., snapshot_uuid: _Optional[str] = ..., snapshot_instance_uuid: _Optional[str] = ..., data_transfer_start_time_usec: _Optional[int] = ...) -> None: ...

class SnapmirrorTransferState(_message.Message):
    __slots__ = ()
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNotStarted: _ClassVar[SnapmirrorTransferState.State]
        kInProgress: _ClassVar[SnapmirrorTransferState.State]
        kFinished: _ClassVar[SnapmirrorTransferState.State]
        kAborted: _ClassVar[SnapmirrorTransferState.State]
        kErrored: _ClassVar[SnapmirrorTransferState.State]
    kNotStarted: SnapmirrorTransferState.State
    kInProgress: SnapmirrorTransferState.State
    kFinished: SnapmirrorTransferState.State
    kAborted: SnapmirrorTransferState.State
    kErrored: SnapmirrorTransferState.State
    def __init__(self) -> None: ...

class RestoreEnvironmentInfo(_message.Message):
    __slots__ = ("snapmirror_objectstore_info", "snapmirror_transfer_info", "snapmirror_restore_error")
    class SnapmirrorRestoreTransferInfo(_message.Message):
        __slots__ = ("transfer_uuid", "bytes_transferred", "transfer_job_uuid", "transfer_state", "transfer_error")
        TRANSFER_UUID_FIELD_NUMBER: _ClassVar[int]
        BYTES_TRANSFERRED_FIELD_NUMBER: _ClassVar[int]
        TRANSFER_JOB_UUID_FIELD_NUMBER: _ClassVar[int]
        TRANSFER_STATE_FIELD_NUMBER: _ClassVar[int]
        TRANSFER_ERROR_FIELD_NUMBER: _ClassVar[int]
        transfer_uuid: str
        bytes_transferred: int
        transfer_job_uuid: str
        transfer_state: SnapmirrorTransferState.State
        transfer_error: _error_pb2.ErrorProto
        def __init__(self, transfer_uuid: _Optional[str] = ..., bytes_transferred: _Optional[int] = ..., transfer_job_uuid: _Optional[str] = ..., transfer_state: _Optional[_Union[SnapmirrorTransferState.State, str]] = ..., transfer_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...
    RESTORE_ENV_INFO_FIELD_NUMBER: _ClassVar[int]
    restore_env_info: _descriptor.FieldDescriptor
    SNAPMIRROR_OBJECTSTORE_INFO_FIELD_NUMBER: _ClassVar[int]
    SNAPMIRROR_TRANSFER_INFO_FIELD_NUMBER: _ClassVar[int]
    SNAPMIRROR_RESTORE_ERROR_FIELD_NUMBER: _ClassVar[int]
    snapmirror_objectstore_info: SnapmirrorObjectStoreInfo
    snapmirror_transfer_info: RestoreEnvironmentInfo.SnapmirrorRestoreTransferInfo
    snapmirror_restore_error: _error_pb2.ErrorProto
    def __init__(self, snapmirror_objectstore_info: _Optional[_Union[SnapmirrorObjectStoreInfo, _Mapping]] = ..., snapmirror_transfer_info: _Optional[_Union[RestoreEnvironmentInfo.SnapmirrorRestoreTransferInfo, _Mapping]] = ..., snapmirror_restore_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...
