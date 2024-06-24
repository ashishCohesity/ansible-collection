from bridge.audit_log import audit_log_pb2 as _audit_log_pb2
from bridge.snap_fs import snap_fs_metadata_pb2 as _snap_fs_metadata_pb2
from configs import cluster_config_pb2 as _cluster_config_pb2
from util.base import op_clock_pb2 as _op_clock_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SmbSessionMetadataProto(_message.Message):
    __slots__ = ("session_id", "state", "tree_connect_vec", "tree_id_generator", "user_id", "domain_id", "is_guest_session", "is_anonymous_session", "last_access_usecs", "opclock_vec", "security_context", "previous_session_ids", "dialect", "uid", "gid", "secondary_gid_map", "new_session_id", "token", "client_guid", "signing_key", "encryption_key", "decryption_key", "application_key", "enable_signature_for_responses", "verify_signature_for_requests", "client_ip", "server_ip", "primary_domain_id", "node_ip", "approx_disconnect_usecs", "create_timestamp_usecs", "is_unix_root_user", "is_local_authentication", "connection_keys", "tenant_id", "client_ip6_addr", "node_id", "is_token_sid_list_complete")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kSessionEstablished: _ClassVar[SmbSessionMetadataProto.State]
        kSessionNotAuthenticated: _ClassVar[SmbSessionMetadataProto.State]
        kSessionAuthenticated: _ClassVar[SmbSessionMetadataProto.State]
        kSessionTimeout: _ClassVar[SmbSessionMetadataProto.State]
        kSessionExpired: _ClassVar[SmbSessionMetadataProto.State]
        kSessionTakenOver: _ClassVar[SmbSessionMetadataProto.State]
    kSessionEstablished: SmbSessionMetadataProto.State
    kSessionNotAuthenticated: SmbSessionMetadataProto.State
    kSessionAuthenticated: SmbSessionMetadataProto.State
    kSessionTimeout: SmbSessionMetadataProto.State
    kSessionExpired: SmbSessionMetadataProto.State
    kSessionTakenOver: SmbSessionMetadataProto.State
    class Dialect(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kDialect202: _ClassVar[SmbSessionMetadataProto.Dialect]
        kDialect21: _ClassVar[SmbSessionMetadataProto.Dialect]
        kDialect30: _ClassVar[SmbSessionMetadataProto.Dialect]
    kDialect202: SmbSessionMetadataProto.Dialect
    kDialect21: SmbSessionMetadataProto.Dialect
    kDialect30: SmbSessionMetadataProto.Dialect
    class Privilege(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kPrivilegeBackup: _ClassVar[SmbSessionMetadataProto.Privilege]
        kPrivilegeRestore: _ClassVar[SmbSessionMetadataProto.Privilege]
        kPrivilegeTakeOwnership: _ClassVar[SmbSessionMetadataProto.Privilege]
        kPrivilegeSecurity: _ClassVar[SmbSessionMetadataProto.Privilege]
        kPrivilegeCreateSymlink: _ClassVar[SmbSessionMetadataProto.Privilege]
        kDataSecurity: _ClassVar[SmbSessionMetadataProto.Privilege]
    kPrivilegeBackup: SmbSessionMetadataProto.Privilege
    kPrivilegeRestore: SmbSessionMetadataProto.Privilege
    kPrivilegeTakeOwnership: SmbSessionMetadataProto.Privilege
    kPrivilegeSecurity: SmbSessionMetadataProto.Privilege
    kPrivilegeCreateSymlink: SmbSessionMetadataProto.Privilege
    kDataSecurity: SmbSessionMetadataProto.Privilege
    class TreeConnect(_message.Message):
        __slots__ = ("tree_id", "view_id", "root_inode_id", "root_entity_id", "view_box_id", "share_path", "alias_name", "alias_path_prefix", "read_only", "encryption_required", "is_internal", "capabilities")
        TREE_ID_FIELD_NUMBER: _ClassVar[int]
        VIEW_ID_FIELD_NUMBER: _ClassVar[int]
        ROOT_INODE_ID_FIELD_NUMBER: _ClassVar[int]
        ROOT_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
        VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
        SHARE_PATH_FIELD_NUMBER: _ClassVar[int]
        ALIAS_NAME_FIELD_NUMBER: _ClassVar[int]
        ALIAS_PATH_PREFIX_FIELD_NUMBER: _ClassVar[int]
        READ_ONLY_FIELD_NUMBER: _ClassVar[int]
        ENCRYPTION_REQUIRED_FIELD_NUMBER: _ClassVar[int]
        IS_INTERNAL_FIELD_NUMBER: _ClassVar[int]
        CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
        tree_id: int
        view_id: int
        root_inode_id: int
        root_entity_id: int
        view_box_id: int
        share_path: str
        alias_name: str
        alias_path_prefix: str
        read_only: bool
        encryption_required: bool
        is_internal: bool
        capabilities: int
        def __init__(self, tree_id: _Optional[int] = ..., view_id: _Optional[int] = ..., root_inode_id: _Optional[int] = ..., root_entity_id: _Optional[int] = ..., view_box_id: _Optional[int] = ..., share_path: _Optional[str] = ..., alias_name: _Optional[str] = ..., alias_path_prefix: _Optional[str] = ..., read_only: bool = ..., encryption_required: bool = ..., is_internal: bool = ..., capabilities: _Optional[int] = ...) -> None: ...
    class SecondaryGroupValue(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class SecondaryGidMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: SmbSessionMetadataProto.SecondaryGroupValue
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[SmbSessionMetadataProto.SecondaryGroupValue, _Mapping]] = ...) -> None: ...
    class Token(_message.Message):
        __slots__ = ("sids", "user_claims", "local_claims", "device_sids", "device_claims", "user_index", "owner_index", "primary_group", "default_dacl", "integrity_level_sid", "mandatory_policy", "smb_privileges")
        class SecurityClaim(_message.Message):
            __slots__ = ("name", "flags", "value_type", "values")
            NAME_FIELD_NUMBER: _ClassVar[int]
            FLAGS_FIELD_NUMBER: _ClassVar[int]
            VALUE_TYPE_FIELD_NUMBER: _ClassVar[int]
            VALUES_FIELD_NUMBER: _ClassVar[int]
            name: str
            flags: int
            value_type: int
            values: _containers.RepeatedScalarFieldContainer[str]
            def __init__(self, name: _Optional[str] = ..., flags: _Optional[int] = ..., value_type: _Optional[int] = ..., values: _Optional[_Iterable[str]] = ...) -> None: ...
        class LUID(_message.Message):
            __slots__ = ("low_part", "high_part")
            LOW_PART_FIELD_NUMBER: _ClassVar[int]
            HIGH_PART_FIELD_NUMBER: _ClassVar[int]
            low_part: int
            high_part: int
            def __init__(self, low_part: _Optional[int] = ..., high_part: _Optional[int] = ...) -> None: ...
        SIDS_FIELD_NUMBER: _ClassVar[int]
        USER_CLAIMS_FIELD_NUMBER: _ClassVar[int]
        LOCAL_CLAIMS_FIELD_NUMBER: _ClassVar[int]
        DEVICE_SIDS_FIELD_NUMBER: _ClassVar[int]
        DEVICE_CLAIMS_FIELD_NUMBER: _ClassVar[int]
        USER_INDEX_FIELD_NUMBER: _ClassVar[int]
        OWNER_INDEX_FIELD_NUMBER: _ClassVar[int]
        PRIMARY_GROUP_FIELD_NUMBER: _ClassVar[int]
        DEFAULT_DACL_FIELD_NUMBER: _ClassVar[int]
        INTEGRITY_LEVEL_SID_FIELD_NUMBER: _ClassVar[int]
        MANDATORY_POLICY_FIELD_NUMBER: _ClassVar[int]
        SMB_PRIVILEGES_FIELD_NUMBER: _ClassVar[int]
        sids: _containers.RepeatedCompositeFieldContainer[_cluster_config_pb2.ClusterConfigProto.SID]
        user_claims: _containers.RepeatedCompositeFieldContainer[SmbSessionMetadataProto.Token.SecurityClaim]
        local_claims: _containers.RepeatedCompositeFieldContainer[SmbSessionMetadataProto.Token.SecurityClaim]
        device_sids: _containers.RepeatedCompositeFieldContainer[_cluster_config_pb2.ClusterConfigProto.SID]
        device_claims: _containers.RepeatedCompositeFieldContainer[SmbSessionMetadataProto.Token.SecurityClaim]
        user_index: int
        owner_index: int
        primary_group: int
        default_dacl: _containers.RepeatedCompositeFieldContainer[_snap_fs_metadata_pb2.InodeMetadataProto.ExtendedAttributes.ACE]
        integrity_level_sid: _cluster_config_pb2.ClusterConfigProto.SID
        mandatory_policy: int
        smb_privileges: int
        def __init__(self, sids: _Optional[_Iterable[_Union[_cluster_config_pb2.ClusterConfigProto.SID, _Mapping]]] = ..., user_claims: _Optional[_Iterable[_Union[SmbSessionMetadataProto.Token.SecurityClaim, _Mapping]]] = ..., local_claims: _Optional[_Iterable[_Union[SmbSessionMetadataProto.Token.SecurityClaim, _Mapping]]] = ..., device_sids: _Optional[_Iterable[_Union[_cluster_config_pb2.ClusterConfigProto.SID, _Mapping]]] = ..., device_claims: _Optional[_Iterable[_Union[SmbSessionMetadataProto.Token.SecurityClaim, _Mapping]]] = ..., user_index: _Optional[int] = ..., owner_index: _Optional[int] = ..., primary_group: _Optional[int] = ..., default_dacl: _Optional[_Iterable[_Union[_snap_fs_metadata_pb2.InodeMetadataProto.ExtendedAttributes.ACE, _Mapping]]] = ..., integrity_level_sid: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.SID, _Mapping]] = ..., mandatory_policy: _Optional[int] = ..., smb_privileges: _Optional[int] = ...) -> None: ...
    class ConnectionKeys(_message.Message):
        __slots__ = ("session_key", "signing_key")
        SESSION_KEY_FIELD_NUMBER: _ClassVar[int]
        SIGNING_KEY_FIELD_NUMBER: _ClassVar[int]
        session_key: bytes
        signing_key: bytes
        def __init__(self, session_key: _Optional[bytes] = ..., signing_key: _Optional[bytes] = ...) -> None: ...
    class ConnectionKeysEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: SmbSessionMetadataProto.ConnectionKeys
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[SmbSessionMetadataProto.ConnectionKeys, _Mapping]] = ...) -> None: ...
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    TREE_CONNECT_VEC_FIELD_NUMBER: _ClassVar[int]
    TREE_ID_GENERATOR_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    IS_GUEST_SESSION_FIELD_NUMBER: _ClassVar[int]
    IS_ANONYMOUS_SESSION_FIELD_NUMBER: _ClassVar[int]
    LAST_ACCESS_USECS_FIELD_NUMBER: _ClassVar[int]
    OPCLOCK_VEC_FIELD_NUMBER: _ClassVar[int]
    SECURITY_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    PREVIOUS_SESSION_IDS_FIELD_NUMBER: _ClassVar[int]
    DIALECT_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    GID_FIELD_NUMBER: _ClassVar[int]
    SECONDARY_GID_MAP_FIELD_NUMBER: _ClassVar[int]
    NEW_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    CLIENT_GUID_FIELD_NUMBER: _ClassVar[int]
    SIGNING_KEY_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_KEY_FIELD_NUMBER: _ClassVar[int]
    DECRYPTION_KEY_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_KEY_FIELD_NUMBER: _ClassVar[int]
    ENABLE_SIGNATURE_FOR_RESPONSES_FIELD_NUMBER: _ClassVar[int]
    VERIFY_SIGNATURE_FOR_REQUESTS_FIELD_NUMBER: _ClassVar[int]
    CLIENT_IP_FIELD_NUMBER: _ClassVar[int]
    SERVER_IP_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    NODE_IP_FIELD_NUMBER: _ClassVar[int]
    APPROX_DISCONNECT_USECS_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
    IS_UNIX_ROOT_USER_FIELD_NUMBER: _ClassVar[int]
    IS_LOCAL_AUTHENTICATION_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_KEYS_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_IP6_ADDR_FIELD_NUMBER: _ClassVar[int]
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    IS_TOKEN_SID_LIST_COMPLETE_FIELD_NUMBER: _ClassVar[int]
    session_id: int
    state: SmbSessionMetadataProto.State
    tree_connect_vec: _containers.RepeatedCompositeFieldContainer[SmbSessionMetadataProto.TreeConnect]
    tree_id_generator: int
    user_id: str
    domain_id: str
    is_guest_session: bool
    is_anonymous_session: bool
    last_access_usecs: int
    opclock_vec: _containers.RepeatedCompositeFieldContainer[_op_clock_pb2.OpClock]
    security_context: bytes
    previous_session_ids: _containers.RepeatedScalarFieldContainer[int]
    dialect: SmbSessionMetadataProto.Dialect
    uid: int
    gid: int
    secondary_gid_map: _containers.MessageMap[int, SmbSessionMetadataProto.SecondaryGroupValue]
    new_session_id: int
    token: SmbSessionMetadataProto.Token
    client_guid: _cluster_config_pb2.ClusterConfigProto.SmbGUID
    signing_key: bytes
    encryption_key: bytes
    decryption_key: bytes
    application_key: bytes
    enable_signature_for_responses: bool
    verify_signature_for_requests: bool
    client_ip: str
    server_ip: str
    primary_domain_id: str
    node_ip: str
    approx_disconnect_usecs: int
    create_timestamp_usecs: int
    is_unix_root_user: bool
    is_local_authentication: bool
    connection_keys: _containers.MessageMap[int, SmbSessionMetadataProto.ConnectionKeys]
    tenant_id: str
    client_ip6_addr: str
    node_id: int
    is_token_sid_list_complete: bool
    def __init__(self, session_id: _Optional[int] = ..., state: _Optional[_Union[SmbSessionMetadataProto.State, str]] = ..., tree_connect_vec: _Optional[_Iterable[_Union[SmbSessionMetadataProto.TreeConnect, _Mapping]]] = ..., tree_id_generator: _Optional[int] = ..., user_id: _Optional[str] = ..., domain_id: _Optional[str] = ..., is_guest_session: bool = ..., is_anonymous_session: bool = ..., last_access_usecs: _Optional[int] = ..., opclock_vec: _Optional[_Iterable[_Union[_op_clock_pb2.OpClock, _Mapping]]] = ..., security_context: _Optional[bytes] = ..., previous_session_ids: _Optional[_Iterable[int]] = ..., dialect: _Optional[_Union[SmbSessionMetadataProto.Dialect, str]] = ..., uid: _Optional[int] = ..., gid: _Optional[int] = ..., secondary_gid_map: _Optional[_Mapping[int, SmbSessionMetadataProto.SecondaryGroupValue]] = ..., new_session_id: _Optional[int] = ..., token: _Optional[_Union[SmbSessionMetadataProto.Token, _Mapping]] = ..., client_guid: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.SmbGUID, _Mapping]] = ..., signing_key: _Optional[bytes] = ..., encryption_key: _Optional[bytes] = ..., decryption_key: _Optional[bytes] = ..., application_key: _Optional[bytes] = ..., enable_signature_for_responses: bool = ..., verify_signature_for_requests: bool = ..., client_ip: _Optional[str] = ..., server_ip: _Optional[str] = ..., primary_domain_id: _Optional[str] = ..., node_ip: _Optional[str] = ..., approx_disconnect_usecs: _Optional[int] = ..., create_timestamp_usecs: _Optional[int] = ..., is_unix_root_user: bool = ..., is_local_authentication: bool = ..., connection_keys: _Optional[_Mapping[int, SmbSessionMetadataProto.ConnectionKeys]] = ..., tenant_id: _Optional[str] = ..., client_ip6_addr: _Optional[str] = ..., node_id: _Optional[int] = ..., is_token_sid_list_complete: bool = ...) -> None: ...

class SmbEntityIdProto(_message.Message):
    __slots__ = ("view_id", "parent_entity_id", "root_inode_id", "entity_name")
    VIEW_ID_FIELD_NUMBER: _ClassVar[int]
    PARENT_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    ROOT_INODE_ID_FIELD_NUMBER: _ClassVar[int]
    ENTITY_NAME_FIELD_NUMBER: _ClassVar[int]
    view_id: int
    parent_entity_id: int
    root_inode_id: int
    entity_name: str
    def __init__(self, view_id: _Optional[int] = ..., parent_entity_id: _Optional[int] = ..., root_inode_id: _Optional[int] = ..., entity_name: _Optional[str] = ...) -> None: ...

class SmbEntityMetadataProto(_message.Message):
    __slots__ = ("entity_id", "delete_on_close", "read_opens", "write_opens", "delete_opens", "read_disabled_opens", "write_disabled_opens", "delete_disabled_opens", "active_opens", "opclock_vec", "locks", "oplocks", "audit_record_id", "path", "delete_pending")
    class ReadOpensEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: bool
        def __init__(self, key: _Optional[int] = ..., value: bool = ...) -> None: ...
    class WriteOpensEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: bool
        def __init__(self, key: _Optional[int] = ..., value: bool = ...) -> None: ...
    class DeleteOpensEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: bool
        def __init__(self, key: _Optional[int] = ..., value: bool = ...) -> None: ...
    class ReadDisabledOpensEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: bool
        def __init__(self, key: _Optional[int] = ..., value: bool = ...) -> None: ...
    class WriteDisabledOpensEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: bool
        def __init__(self, key: _Optional[int] = ..., value: bool = ...) -> None: ...
    class DeleteDisabledOpensEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: bool
        def __init__(self, key: _Optional[int] = ..., value: bool = ...) -> None: ...
    class SmbEntityOpenState(_message.Message):
        __slots__ = ("session_id", "last_update_usecs", "timeout_msecs", "access", "sharing", "durable_guid", "node_id", "is_persistent", "app_instance", "client_guid", "create_doc_option", "node_incarnation_id", "create_action")
        class AppInstance(_message.Message):
            __slots__ = ("id", "version")
            class Version(_message.Message):
                __slots__ = ("low", "high")
                LOW_FIELD_NUMBER: _ClassVar[int]
                HIGH_FIELD_NUMBER: _ClassVar[int]
                low: int
                high: int
                def __init__(self, low: _Optional[int] = ..., high: _Optional[int] = ...) -> None: ...
            ID_FIELD_NUMBER: _ClassVar[int]
            VERSION_FIELD_NUMBER: _ClassVar[int]
            id: bytes
            version: SmbEntityMetadataProto.SmbEntityOpenState.AppInstance.Version
            def __init__(self, id: _Optional[bytes] = ..., version: _Optional[_Union[SmbEntityMetadataProto.SmbEntityOpenState.AppInstance.Version, _Mapping]] = ...) -> None: ...
        SESSION_ID_FIELD_NUMBER: _ClassVar[int]
        LAST_UPDATE_USECS_FIELD_NUMBER: _ClassVar[int]
        TIMEOUT_MSECS_FIELD_NUMBER: _ClassVar[int]
        ACCESS_FIELD_NUMBER: _ClassVar[int]
        SHARING_FIELD_NUMBER: _ClassVar[int]
        DURABLE_GUID_FIELD_NUMBER: _ClassVar[int]
        NODE_ID_FIELD_NUMBER: _ClassVar[int]
        IS_PERSISTENT_FIELD_NUMBER: _ClassVar[int]
        APP_INSTANCE_FIELD_NUMBER: _ClassVar[int]
        CLIENT_GUID_FIELD_NUMBER: _ClassVar[int]
        CREATE_DOC_OPTION_FIELD_NUMBER: _ClassVar[int]
        NODE_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
        CREATE_ACTION_FIELD_NUMBER: _ClassVar[int]
        session_id: int
        last_update_usecs: int
        timeout_msecs: int
        access: int
        sharing: int
        durable_guid: _cluster_config_pb2.ClusterConfigProto.SmbGUID
        node_id: int
        is_persistent: bool
        app_instance: SmbEntityMetadataProto.SmbEntityOpenState.AppInstance
        client_guid: _cluster_config_pb2.ClusterConfigProto.SmbGUID
        create_doc_option: bool
        node_incarnation_id: int
        create_action: int
        def __init__(self, session_id: _Optional[int] = ..., last_update_usecs: _Optional[int] = ..., timeout_msecs: _Optional[int] = ..., access: _Optional[int] = ..., sharing: _Optional[int] = ..., durable_guid: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.SmbGUID, _Mapping]] = ..., node_id: _Optional[int] = ..., is_persistent: bool = ..., app_instance: _Optional[_Union[SmbEntityMetadataProto.SmbEntityOpenState.AppInstance, _Mapping]] = ..., client_guid: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.SmbGUID, _Mapping]] = ..., create_doc_option: bool = ..., node_incarnation_id: _Optional[int] = ..., create_action: _Optional[int] = ...) -> None: ...
    class ActiveOpensEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: SmbEntityMetadataProto.SmbEntityOpenState
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[SmbEntityMetadataProto.SmbEntityOpenState, _Mapping]] = ...) -> None: ...
    class SmbEntityLockState(_message.Message):
        __slots__ = ("lock_ranges", "lock_sequence_vec")
        class LockRange(_message.Message):
            __slots__ = ("offset", "length", "is_exclusive")
            OFFSET_FIELD_NUMBER: _ClassVar[int]
            LENGTH_FIELD_NUMBER: _ClassVar[int]
            IS_EXCLUSIVE_FIELD_NUMBER: _ClassVar[int]
            offset: int
            length: int
            is_exclusive: bool
            def __init__(self, offset: _Optional[int] = ..., length: _Optional[int] = ..., is_exclusive: bool = ...) -> None: ...
        LOCK_RANGES_FIELD_NUMBER: _ClassVar[int]
        LOCK_SEQUENCE_VEC_FIELD_NUMBER: _ClassVar[int]
        lock_ranges: _containers.RepeatedCompositeFieldContainer[SmbEntityMetadataProto.SmbEntityLockState.LockRange]
        lock_sequence_vec: _containers.RepeatedScalarFieldContainer[int]
        def __init__(self, lock_ranges: _Optional[_Iterable[_Union[SmbEntityMetadataProto.SmbEntityLockState.LockRange, _Mapping]]] = ..., lock_sequence_vec: _Optional[_Iterable[int]] = ...) -> None: ...
    class LocksEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: SmbEntityMetadataProto.SmbEntityLockState
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[SmbEntityMetadataProto.SmbEntityLockState, _Mapping]] = ...) -> None: ...
    class SmbEntityOpLockState(_message.Message):
        __slots__ = ("oplock_type", "lease_type", "lease_flags", "lease_key", "parent_lease_key", "lease_epoch", "is_breaking", "lease_breaking_to")
        class LeaseKey(_message.Message):
            __slots__ = ("low_part", "high_part")
            LOW_PART_FIELD_NUMBER: _ClassVar[int]
            HIGH_PART_FIELD_NUMBER: _ClassVar[int]
            low_part: int
            high_part: int
            def __init__(self, low_part: _Optional[int] = ..., high_part: _Optional[int] = ...) -> None: ...
        OPLOCK_TYPE_FIELD_NUMBER: _ClassVar[int]
        LEASE_TYPE_FIELD_NUMBER: _ClassVar[int]
        LEASE_FLAGS_FIELD_NUMBER: _ClassVar[int]
        LEASE_KEY_FIELD_NUMBER: _ClassVar[int]
        PARENT_LEASE_KEY_FIELD_NUMBER: _ClassVar[int]
        LEASE_EPOCH_FIELD_NUMBER: _ClassVar[int]
        IS_BREAKING_FIELD_NUMBER: _ClassVar[int]
        LEASE_BREAKING_TO_FIELD_NUMBER: _ClassVar[int]
        oplock_type: int
        lease_type: int
        lease_flags: int
        lease_key: SmbEntityMetadataProto.SmbEntityOpLockState.LeaseKey
        parent_lease_key: SmbEntityMetadataProto.SmbEntityOpLockState.LeaseKey
        lease_epoch: int
        is_breaking: bool
        lease_breaking_to: int
        def __init__(self, oplock_type: _Optional[int] = ..., lease_type: _Optional[int] = ..., lease_flags: _Optional[int] = ..., lease_key: _Optional[_Union[SmbEntityMetadataProto.SmbEntityOpLockState.LeaseKey, _Mapping]] = ..., parent_lease_key: _Optional[_Union[SmbEntityMetadataProto.SmbEntityOpLockState.LeaseKey, _Mapping]] = ..., lease_epoch: _Optional[int] = ..., is_breaking: bool = ..., lease_breaking_to: _Optional[int] = ...) -> None: ...
    class OplocksEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: SmbEntityMetadataProto.SmbEntityOpLockState
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[SmbEntityMetadataProto.SmbEntityOpLockState, _Mapping]] = ...) -> None: ...
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    DELETE_ON_CLOSE_FIELD_NUMBER: _ClassVar[int]
    READ_OPENS_FIELD_NUMBER: _ClassVar[int]
    WRITE_OPENS_FIELD_NUMBER: _ClassVar[int]
    DELETE_OPENS_FIELD_NUMBER: _ClassVar[int]
    READ_DISABLED_OPENS_FIELD_NUMBER: _ClassVar[int]
    WRITE_DISABLED_OPENS_FIELD_NUMBER: _ClassVar[int]
    DELETE_DISABLED_OPENS_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_OPENS_FIELD_NUMBER: _ClassVar[int]
    OPCLOCK_VEC_FIELD_NUMBER: _ClassVar[int]
    LOCKS_FIELD_NUMBER: _ClassVar[int]
    OPLOCKS_FIELD_NUMBER: _ClassVar[int]
    AUDIT_RECORD_ID_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    DELETE_PENDING_FIELD_NUMBER: _ClassVar[int]
    entity_id: int
    delete_on_close: bool
    read_opens: _containers.ScalarMap[int, bool]
    write_opens: _containers.ScalarMap[int, bool]
    delete_opens: _containers.ScalarMap[int, bool]
    read_disabled_opens: _containers.ScalarMap[int, bool]
    write_disabled_opens: _containers.ScalarMap[int, bool]
    delete_disabled_opens: _containers.ScalarMap[int, bool]
    active_opens: _containers.MessageMap[int, SmbEntityMetadataProto.SmbEntityOpenState]
    opclock_vec: _containers.RepeatedCompositeFieldContainer[_op_clock_pb2.OpClock]
    locks: _containers.MessageMap[int, SmbEntityMetadataProto.SmbEntityLockState]
    oplocks: _containers.MessageMap[int, SmbEntityMetadataProto.SmbEntityOpLockState]
    audit_record_id: _audit_log_pb2.AuditRecordId
    path: str
    delete_pending: bool
    def __init__(self, entity_id: _Optional[int] = ..., delete_on_close: bool = ..., read_opens: _Optional[_Mapping[int, bool]] = ..., write_opens: _Optional[_Mapping[int, bool]] = ..., delete_opens: _Optional[_Mapping[int, bool]] = ..., read_disabled_opens: _Optional[_Mapping[int, bool]] = ..., write_disabled_opens: _Optional[_Mapping[int, bool]] = ..., delete_disabled_opens: _Optional[_Mapping[int, bool]] = ..., active_opens: _Optional[_Mapping[int, SmbEntityMetadataProto.SmbEntityOpenState]] = ..., opclock_vec: _Optional[_Iterable[_Union[_op_clock_pb2.OpClock, _Mapping]]] = ..., locks: _Optional[_Mapping[int, SmbEntityMetadataProto.SmbEntityLockState]] = ..., oplocks: _Optional[_Mapping[int, SmbEntityMetadataProto.SmbEntityOpLockState]] = ..., audit_record_id: _Optional[_Union[_audit_log_pb2.AuditRecordId, _Mapping]] = ..., path: _Optional[str] = ..., delete_pending: bool = ...) -> None: ...
