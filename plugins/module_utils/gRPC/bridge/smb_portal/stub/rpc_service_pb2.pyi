from configs import cluster_config_pb2 as _cluster_config_pb2
from open_util.net import protorpc_pb2 as _protorpc_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ForwardArg(_message.Message):
    __slots__ = ("is_optional", "expected_ticket_sequencer_high", "expected_ticket_sequencer_low", "node_id", "view_id", "root_inode_id", "parent_entity_id", "entity_name", "entity_path", "client_ip", "persistent_id", "volatile_id")
    IS_OPTIONAL_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_TICKET_SEQUENCER_HIGH_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_TICKET_SEQUENCER_LOW_FIELD_NUMBER: _ClassVar[int]
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_ID_FIELD_NUMBER: _ClassVar[int]
    ROOT_INODE_ID_FIELD_NUMBER: _ClassVar[int]
    PARENT_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    ENTITY_NAME_FIELD_NUMBER: _ClassVar[int]
    ENTITY_PATH_FIELD_NUMBER: _ClassVar[int]
    CLIENT_IP_FIELD_NUMBER: _ClassVar[int]
    PERSISTENT_ID_FIELD_NUMBER: _ClassVar[int]
    VOLATILE_ID_FIELD_NUMBER: _ClassVar[int]
    is_optional: bool
    expected_ticket_sequencer_high: int
    expected_ticket_sequencer_low: int
    node_id: int
    view_id: int
    root_inode_id: int
    parent_entity_id: int
    entity_name: str
    entity_path: str
    client_ip: str
    persistent_id: int
    volatile_id: int
    def __init__(self, is_optional: bool = ..., expected_ticket_sequencer_high: _Optional[int] = ..., expected_ticket_sequencer_low: _Optional[int] = ..., node_id: _Optional[int] = ..., view_id: _Optional[int] = ..., root_inode_id: _Optional[int] = ..., parent_entity_id: _Optional[int] = ..., entity_name: _Optional[str] = ..., entity_path: _Optional[str] = ..., client_ip: _Optional[str] = ..., persistent_id: _Optional[int] = ..., volatile_id: _Optional[int] = ...) -> None: ...

class ForwardResult(_message.Message):
    __slots__ = ("persistent_id", "volatile_id", "entity_granted_access", "nt_status", "delete_on_close")
    PERSISTENT_ID_FIELD_NUMBER: _ClassVar[int]
    VOLATILE_ID_FIELD_NUMBER: _ClassVar[int]
    ENTITY_GRANTED_ACCESS_FIELD_NUMBER: _ClassVar[int]
    NT_STATUS_FIELD_NUMBER: _ClassVar[int]
    DELETE_ON_CLOSE_FIELD_NUMBER: _ClassVar[int]
    persistent_id: int
    volatile_id: int
    entity_granted_access: int
    nt_status: int
    delete_on_close: bool
    def __init__(self, persistent_id: _Optional[int] = ..., volatile_id: _Optional[int] = ..., entity_granted_access: _Optional[int] = ..., nt_status: _Optional[int] = ..., delete_on_close: bool = ...) -> None: ...

class OplockBreakArg(_message.Message):
    __slots__ = ("persistent_id", "volatile_id", "new_oplock_level", "new_lease_level")
    PERSISTENT_ID_FIELD_NUMBER: _ClassVar[int]
    VOLATILE_ID_FIELD_NUMBER: _ClassVar[int]
    NEW_OPLOCK_LEVEL_FIELD_NUMBER: _ClassVar[int]
    NEW_LEASE_LEVEL_FIELD_NUMBER: _ClassVar[int]
    persistent_id: int
    volatile_id: int
    new_oplock_level: int
    new_lease_level: int
    def __init__(self, persistent_id: _Optional[int] = ..., volatile_id: _Optional[int] = ..., new_oplock_level: _Optional[int] = ..., new_lease_level: _Optional[int] = ...) -> None: ...

class OplockBreakResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class LeaseBreakArg(_message.Message):
    __slots__ = ("view_id", "root_inode_id", "persistent_id", "parent_entity_id", "entity_name", "client_guid", "lease_key_low", "lease_key_high", "current_lease_state", "new_lease_state", "lease_epoch", "volatile_ids")
    VIEW_ID_FIELD_NUMBER: _ClassVar[int]
    ROOT_INODE_ID_FIELD_NUMBER: _ClassVar[int]
    PERSISTENT_ID_FIELD_NUMBER: _ClassVar[int]
    PARENT_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    ENTITY_NAME_FIELD_NUMBER: _ClassVar[int]
    CLIENT_GUID_FIELD_NUMBER: _ClassVar[int]
    LEASE_KEY_LOW_FIELD_NUMBER: _ClassVar[int]
    LEASE_KEY_HIGH_FIELD_NUMBER: _ClassVar[int]
    CURRENT_LEASE_STATE_FIELD_NUMBER: _ClassVar[int]
    NEW_LEASE_STATE_FIELD_NUMBER: _ClassVar[int]
    LEASE_EPOCH_FIELD_NUMBER: _ClassVar[int]
    VOLATILE_IDS_FIELD_NUMBER: _ClassVar[int]
    view_id: int
    root_inode_id: int
    persistent_id: int
    parent_entity_id: int
    entity_name: str
    client_guid: _cluster_config_pb2.ClusterConfigProto.SmbGUID
    lease_key_low: int
    lease_key_high: int
    current_lease_state: int
    new_lease_state: int
    lease_epoch: int
    volatile_ids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, view_id: _Optional[int] = ..., root_inode_id: _Optional[int] = ..., persistent_id: _Optional[int] = ..., parent_entity_id: _Optional[int] = ..., entity_name: _Optional[str] = ..., client_guid: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.SmbGUID, _Mapping]] = ..., lease_key_low: _Optional[int] = ..., lease_key_high: _Optional[int] = ..., current_lease_state: _Optional[int] = ..., new_lease_state: _Optional[int] = ..., lease_epoch: _Optional[int] = ..., volatile_ids: _Optional[_Iterable[int]] = ...) -> None: ...

class LeaseBreakResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListSmbSessionsArg(_message.Message):
    __slots__ = ("info_level", "client_tenant_id")
    class SessionInfoLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kInfoLevel0: _ClassVar[ListSmbSessionsArg.SessionInfoLevel]
        kInfoLevel1: _ClassVar[ListSmbSessionsArg.SessionInfoLevel]
        kInfoLevel2: _ClassVar[ListSmbSessionsArg.SessionInfoLevel]
    kInfoLevel0: ListSmbSessionsArg.SessionInfoLevel
    kInfoLevel1: ListSmbSessionsArg.SessionInfoLevel
    kInfoLevel2: ListSmbSessionsArg.SessionInfoLevel
    INFO_LEVEL_FIELD_NUMBER: _ClassVar[int]
    CLIENT_TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    info_level: ListSmbSessionsArg.SessionInfoLevel
    client_tenant_id: str
    def __init__(self, info_level: _Optional[_Union[ListSmbSessionsArg.SessionInfoLevel, str]] = ..., client_tenant_id: _Optional[str] = ...) -> None: ...

class ListSmbSessionsResult(_message.Message):
    __slots__ = ("session_vec",)
    class SmbSession(_message.Message):
        __slots__ = ("session_id", "client_computer_name", "user_name", "num_opens", "uptime", "idle_time", "client_type", "is_guest_session", "is_encrypted")
        SESSION_ID_FIELD_NUMBER: _ClassVar[int]
        CLIENT_COMPUTER_NAME_FIELD_NUMBER: _ClassVar[int]
        USER_NAME_FIELD_NUMBER: _ClassVar[int]
        NUM_OPENS_FIELD_NUMBER: _ClassVar[int]
        UPTIME_FIELD_NUMBER: _ClassVar[int]
        IDLE_TIME_FIELD_NUMBER: _ClassVar[int]
        CLIENT_TYPE_FIELD_NUMBER: _ClassVar[int]
        IS_GUEST_SESSION_FIELD_NUMBER: _ClassVar[int]
        IS_ENCRYPTED_FIELD_NUMBER: _ClassVar[int]
        session_id: int
        client_computer_name: str
        user_name: str
        num_opens: int
        uptime: int
        idle_time: int
        client_type: str
        is_guest_session: bool
        is_encrypted: bool
        def __init__(self, session_id: _Optional[int] = ..., client_computer_name: _Optional[str] = ..., user_name: _Optional[str] = ..., num_opens: _Optional[int] = ..., uptime: _Optional[int] = ..., idle_time: _Optional[int] = ..., client_type: _Optional[str] = ..., is_guest_session: bool = ..., is_encrypted: bool = ...) -> None: ...
    SESSION_VEC_FIELD_NUMBER: _ClassVar[int]
    session_vec: _containers.RepeatedCompositeFieldContainer[ListSmbSessionsResult.SmbSession]
    def __init__(self, session_vec: _Optional[_Iterable[_Union[ListSmbSessionsResult.SmbSession, _Mapping]]] = ...) -> None: ...

class ListSmbFileOpensArg(_message.Message):
    __slots__ = ("info_level", "user_name", "base_path", "tenant_id")
    class OpenFileInfoLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kInfoLevel2: _ClassVar[ListSmbFileOpensArg.OpenFileInfoLevel]
        kInfoLevel3: _ClassVar[ListSmbFileOpensArg.OpenFileInfoLevel]
    kInfoLevel2: ListSmbFileOpensArg.OpenFileInfoLevel
    kInfoLevel3: ListSmbFileOpensArg.OpenFileInfoLevel
    INFO_LEVEL_FIELD_NUMBER: _ClassVar[int]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    BASE_PATH_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    info_level: ListSmbFileOpensArg.OpenFileInfoLevel
    user_name: str
    base_path: str
    tenant_id: str
    def __init__(self, info_level: _Optional[_Union[ListSmbFileOpensArg.OpenFileInfoLevel, str]] = ..., user_name: _Optional[str] = ..., base_path: _Optional[str] = ..., tenant_id: _Optional[str] = ...) -> None: ...

class ListSmbFileOpensResult(_message.Message):
    __slots__ = ("file_opens_vec",)
    class FileOpen(_message.Message):
        __slots__ = ("volatile_id", "session_id", "tree_id", "view_id", "root_inode_id", "parent_entity_id", "entity_name", "granted_access", "user_name", "num_locks", "file_path", "global_file_id", "persistent_id")
        VOLATILE_ID_FIELD_NUMBER: _ClassVar[int]
        SESSION_ID_FIELD_NUMBER: _ClassVar[int]
        TREE_ID_FIELD_NUMBER: _ClassVar[int]
        VIEW_ID_FIELD_NUMBER: _ClassVar[int]
        ROOT_INODE_ID_FIELD_NUMBER: _ClassVar[int]
        PARENT_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
        ENTITY_NAME_FIELD_NUMBER: _ClassVar[int]
        GRANTED_ACCESS_FIELD_NUMBER: _ClassVar[int]
        USER_NAME_FIELD_NUMBER: _ClassVar[int]
        NUM_LOCKS_FIELD_NUMBER: _ClassVar[int]
        FILE_PATH_FIELD_NUMBER: _ClassVar[int]
        GLOBAL_FILE_ID_FIELD_NUMBER: _ClassVar[int]
        PERSISTENT_ID_FIELD_NUMBER: _ClassVar[int]
        volatile_id: int
        session_id: int
        tree_id: int
        view_id: int
        root_inode_id: int
        parent_entity_id: int
        entity_name: str
        granted_access: int
        user_name: str
        num_locks: int
        file_path: str
        global_file_id: int
        persistent_id: int
        def __init__(self, volatile_id: _Optional[int] = ..., session_id: _Optional[int] = ..., tree_id: _Optional[int] = ..., view_id: _Optional[int] = ..., root_inode_id: _Optional[int] = ..., parent_entity_id: _Optional[int] = ..., entity_name: _Optional[str] = ..., granted_access: _Optional[int] = ..., user_name: _Optional[str] = ..., num_locks: _Optional[int] = ..., file_path: _Optional[str] = ..., global_file_id: _Optional[int] = ..., persistent_id: _Optional[int] = ...) -> None: ...
    FILE_OPENS_VEC_FIELD_NUMBER: _ClassVar[int]
    file_opens_vec: _containers.RepeatedCompositeFieldContainer[ListSmbFileOpensResult.FileOpen]
    def __init__(self, file_opens_vec: _Optional[_Iterable[_Union[ListSmbFileOpensResult.FileOpen, _Mapping]]] = ...) -> None: ...

class ListTreeConnectsArg(_message.Message):
    __slots__ = ("info_level", "share_name", "client_tenant_id")
    class InfoLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kInfoLevel0: _ClassVar[ListTreeConnectsArg.InfoLevel]
        kInfoLevel1: _ClassVar[ListTreeConnectsArg.InfoLevel]
    kInfoLevel0: ListTreeConnectsArg.InfoLevel
    kInfoLevel1: ListTreeConnectsArg.InfoLevel
    INFO_LEVEL_FIELD_NUMBER: _ClassVar[int]
    SHARE_NAME_FIELD_NUMBER: _ClassVar[int]
    CLIENT_TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    info_level: ListTreeConnectsArg.InfoLevel
    share_name: str
    client_tenant_id: str
    def __init__(self, info_level: _Optional[_Union[ListTreeConnectsArg.InfoLevel, str]] = ..., share_name: _Optional[str] = ..., client_tenant_id: _Optional[str] = ...) -> None: ...

class ListTreeConnectsResult(_message.Message):
    __slots__ = ("connection_vec",)
    class TreeConnect(_message.Message):
        __slots__ = ("tree_id", "num_opens", "num_users", "uptime", "user_name", "client_name")
        TREE_ID_FIELD_NUMBER: _ClassVar[int]
        NUM_OPENS_FIELD_NUMBER: _ClassVar[int]
        NUM_USERS_FIELD_NUMBER: _ClassVar[int]
        UPTIME_FIELD_NUMBER: _ClassVar[int]
        USER_NAME_FIELD_NUMBER: _ClassVar[int]
        CLIENT_NAME_FIELD_NUMBER: _ClassVar[int]
        tree_id: int
        num_opens: int
        num_users: int
        uptime: int
        user_name: str
        client_name: str
        def __init__(self, tree_id: _Optional[int] = ..., num_opens: _Optional[int] = ..., num_users: _Optional[int] = ..., uptime: _Optional[int] = ..., user_name: _Optional[str] = ..., client_name: _Optional[str] = ...) -> None: ...
    CONNECTION_VEC_FIELD_NUMBER: _ClassVar[int]
    connection_vec: _containers.RepeatedCompositeFieldContainer[ListTreeConnectsResult.TreeConnect]
    def __init__(self, connection_vec: _Optional[_Iterable[_Union[ListTreeConnectsResult.TreeConnect, _Mapping]]] = ...) -> None: ...

class HasOpenFileHandlesArg(_message.Message):
    __slots__ = ("dir_path",)
    DIR_PATH_FIELD_NUMBER: _ClassVar[int]
    dir_path: str
    def __init__(self, dir_path: _Optional[str] = ...) -> None: ...

class HasOpenFileHandlesResult(_message.Message):
    __slots__ = ("has_open_files",)
    HAS_OPEN_FILES_FIELD_NUMBER: _ClassVar[int]
    has_open_files: bool
    def __init__(self, has_open_files: bool = ...) -> None: ...
