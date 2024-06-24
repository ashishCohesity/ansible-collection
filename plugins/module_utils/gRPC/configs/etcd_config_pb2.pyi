from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EtcdConfig(_message.Message):
    __slots__ = ("version", "cluster_state", "initial_cluster_token", "cluster_size", "members", "events", "member_blacklist", "current_etcd_version", "target_etcd_version", "create_timestamp", "update_timestamp", "last_update_node_id", "last_update_operation_id")
    class ClusterState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NEW: _ClassVar[EtcdConfig.ClusterState]
        EXISTING: _ClassVar[EtcdConfig.ClusterState]
        UPGRADING: _ClassVar[EtcdConfig.ClusterState]
    NEW: EtcdConfig.ClusterState
    EXISTING: EtcdConfig.ClusterState
    UPGRADING: EtcdConfig.ClusterState
    class Member(_message.Message):
        __slots__ = ("name", "node_id", "peer_urls", "client_urls", "state", "current_version")
        class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            JOINING: _ClassVar[EtcdConfig.Member.State]
            ACTIVE: _ClassVar[EtcdConfig.Member.State]
            LEAVING: _ClassVar[EtcdConfig.Member.State]
            ADDRESS_UPDATING: _ClassVar[EtcdConfig.Member.State]
            UPGRADING: _ClassVar[EtcdConfig.Member.State]
        JOINING: EtcdConfig.Member.State
        ACTIVE: EtcdConfig.Member.State
        LEAVING: EtcdConfig.Member.State
        ADDRESS_UPDATING: EtcdConfig.Member.State
        UPGRADING: EtcdConfig.Member.State
        NAME_FIELD_NUMBER: _ClassVar[int]
        NODE_ID_FIELD_NUMBER: _ClassVar[int]
        PEER_URLS_FIELD_NUMBER: _ClassVar[int]
        CLIENT_URLS_FIELD_NUMBER: _ClassVar[int]
        STATE_FIELD_NUMBER: _ClassVar[int]
        CURRENT_VERSION_FIELD_NUMBER: _ClassVar[int]
        name: str
        node_id: int
        peer_urls: _containers.RepeatedScalarFieldContainer[str]
        client_urls: _containers.RepeatedScalarFieldContainer[str]
        state: EtcdConfig.Member.State
        current_version: str
        def __init__(self, name: _Optional[str] = ..., node_id: _Optional[int] = ..., peer_urls: _Optional[_Iterable[str]] = ..., client_urls: _Optional[_Iterable[str]] = ..., state: _Optional[_Union[EtcdConfig.Member.State, str]] = ..., current_version: _Optional[str] = ...) -> None: ...
    class Event(_message.Message):
        __slots__ = ("type", "timestamp", "resource_id", "node_id", "description")
        class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            UNKNOWN: _ClassVar[EtcdConfig.Event.Type]
            MEMBER_ADDING: _ClassVar[EtcdConfig.Event.Type]
            MEMBER_ADDED: _ClassVar[EtcdConfig.Event.Type]
            MEMBER_REMOVING: _ClassVar[EtcdConfig.Event.Type]
            MEMBER_REMOVED: _ClassVar[EtcdConfig.Event.Type]
            MEMBER_ADDRESS_UPDATING: _ClassVar[EtcdConfig.Event.Type]
            MEMBER_ADDRESS_UPDATED: _ClassVar[EtcdConfig.Event.Type]
            MEMBER_UPGRADING: _ClassVar[EtcdConfig.Event.Type]
            MEMBER_UPGRADED: _ClassVar[EtcdConfig.Event.Type]
            CLUSTER_CREATION_INITIATED: _ClassVar[EtcdConfig.Event.Type]
            CLUSTER_CREATION_COMPLETED: _ClassVar[EtcdConfig.Event.Type]
            CLUSTER_RECONSTRUCT_INITIATED: _ClassVar[EtcdConfig.Event.Type]
            CLUSTER_RECONSTRUCT_COMPLETED: _ClassVar[EtcdConfig.Event.Type]
            CLUSTER_REINITIALIZE_INITIATED: _ClassVar[EtcdConfig.Event.Type]
            CLUSTER_REINITIALIZE_COMPLETED: _ClassVar[EtcdConfig.Event.Type]
            CLUSTER_UPGRADE_INITIATED: _ClassVar[EtcdConfig.Event.Type]
            CLUSTER_UPGRADE_COMPLETED: _ClassVar[EtcdConfig.Event.Type]
        UNKNOWN: EtcdConfig.Event.Type
        MEMBER_ADDING: EtcdConfig.Event.Type
        MEMBER_ADDED: EtcdConfig.Event.Type
        MEMBER_REMOVING: EtcdConfig.Event.Type
        MEMBER_REMOVED: EtcdConfig.Event.Type
        MEMBER_ADDRESS_UPDATING: EtcdConfig.Event.Type
        MEMBER_ADDRESS_UPDATED: EtcdConfig.Event.Type
        MEMBER_UPGRADING: EtcdConfig.Event.Type
        MEMBER_UPGRADED: EtcdConfig.Event.Type
        CLUSTER_CREATION_INITIATED: EtcdConfig.Event.Type
        CLUSTER_CREATION_COMPLETED: EtcdConfig.Event.Type
        CLUSTER_RECONSTRUCT_INITIATED: EtcdConfig.Event.Type
        CLUSTER_RECONSTRUCT_COMPLETED: EtcdConfig.Event.Type
        CLUSTER_REINITIALIZE_INITIATED: EtcdConfig.Event.Type
        CLUSTER_REINITIALIZE_COMPLETED: EtcdConfig.Event.Type
        CLUSTER_UPGRADE_INITIATED: EtcdConfig.Event.Type
        CLUSTER_UPGRADE_COMPLETED: EtcdConfig.Event.Type
        TYPE_FIELD_NUMBER: _ClassVar[int]
        TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
        RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
        NODE_ID_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        type: EtcdConfig.Event.Type
        timestamp: str
        resource_id: str
        node_id: int
        description: str
        def __init__(self, type: _Optional[_Union[EtcdConfig.Event.Type, str]] = ..., timestamp: _Optional[str] = ..., resource_id: _Optional[str] = ..., node_id: _Optional[int] = ..., description: _Optional[str] = ...) -> None: ...
    VERSION_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_STATE_FIELD_NUMBER: _ClassVar[int]
    INITIAL_CLUSTER_TOKEN_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_SIZE_FIELD_NUMBER: _ClassVar[int]
    MEMBERS_FIELD_NUMBER: _ClassVar[int]
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    MEMBER_BLACKLIST_FIELD_NUMBER: _ClassVar[int]
    CURRENT_ETCD_VERSION_FIELD_NUMBER: _ClassVar[int]
    TARGET_ETCD_VERSION_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATE_NODE_ID_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATE_OPERATION_ID_FIELD_NUMBER: _ClassVar[int]
    version: int
    cluster_state: EtcdConfig.ClusterState
    initial_cluster_token: str
    cluster_size: int
    members: _containers.RepeatedCompositeFieldContainer[EtcdConfig.Member]
    events: _containers.RepeatedCompositeFieldContainer[EtcdConfig.Event]
    member_blacklist: _containers.RepeatedScalarFieldContainer[int]
    current_etcd_version: str
    target_etcd_version: str
    create_timestamp: str
    update_timestamp: str
    last_update_node_id: int
    last_update_operation_id: str
    def __init__(self, version: _Optional[int] = ..., cluster_state: _Optional[_Union[EtcdConfig.ClusterState, str]] = ..., initial_cluster_token: _Optional[str] = ..., cluster_size: _Optional[int] = ..., members: _Optional[_Iterable[_Union[EtcdConfig.Member, _Mapping]]] = ..., events: _Optional[_Iterable[_Union[EtcdConfig.Event, _Mapping]]] = ..., member_blacklist: _Optional[_Iterable[int]] = ..., current_etcd_version: _Optional[str] = ..., target_etcd_version: _Optional[str] = ..., create_timestamp: _Optional[str] = ..., update_timestamp: _Optional[str] = ..., last_update_node_id: _Optional[int] = ..., last_update_operation_id: _Optional[str] = ...) -> None: ...
