from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AxonConfig(_message.Message):
    __slots__ = ("num_nodes", "ip_addresses", "node_ids", "ovn_nb_port", "ovn_sb_port", "ovn_nb_raft_port", "ovn_sb_raft_port", "blacklist", "tunnel_intf_grp_id", "tunnel_vlan_id", "use_custom_interface_for_tunnel", "default_external_intf_grp_id", "default_external_vlan_id", "use_custom_interface_for_default_external_access", "ovn_nb_raft_cluster_id", "ovn_sb_raft_cluster_id", "gandalf_key", "master_node_id", "create_timestamp", "update_timestamp", "last_update_node_id", "last_update_operation_id", "members_status", "events", "reconstruct_resources", "northbound_status", "southbound_status")
    class Member(_message.Message):
        __slots__ = ("node_id", "ip_address", "nb_server_id", "sb_server_id", "state", "nb_cluster_id", "sb_cluster_id")
        class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            JOINING: _ClassVar[AxonConfig.Member.State]
            ACTIVE: _ClassVar[AxonConfig.Member.State]
            LEAVING: _ClassVar[AxonConfig.Member.State]
            ADDRESS_UPDATING: _ClassVar[AxonConfig.Member.State]
        JOINING: AxonConfig.Member.State
        ACTIVE: AxonConfig.Member.State
        LEAVING: AxonConfig.Member.State
        ADDRESS_UPDATING: AxonConfig.Member.State
        NODE_ID_FIELD_NUMBER: _ClassVar[int]
        IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
        NB_SERVER_ID_FIELD_NUMBER: _ClassVar[int]
        SB_SERVER_ID_FIELD_NUMBER: _ClassVar[int]
        STATE_FIELD_NUMBER: _ClassVar[int]
        NB_CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
        SB_CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
        node_id: int
        ip_address: str
        nb_server_id: str
        sb_server_id: str
        state: AxonConfig.Member.State
        nb_cluster_id: str
        sb_cluster_id: str
        def __init__(self, node_id: _Optional[int] = ..., ip_address: _Optional[str] = ..., nb_server_id: _Optional[str] = ..., sb_server_id: _Optional[str] = ..., state: _Optional[_Union[AxonConfig.Member.State, str]] = ..., nb_cluster_id: _Optional[str] = ..., sb_cluster_id: _Optional[str] = ...) -> None: ...
    class MembersStatusEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: AxonConfig.Member
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[AxonConfig.Member, _Mapping]] = ...) -> None: ...
    class Event(_message.Message):
        __slots__ = ("type", "timestamp", "resource_id", "ip_address", "node_id", "description")
        class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            UNKNOWN: _ClassVar[AxonConfig.Event.Type]
            MEMBER_ADDING: _ClassVar[AxonConfig.Event.Type]
            MEMBER_ADDED: _ClassVar[AxonConfig.Event.Type]
            MEMBER_REMOVING: _ClassVar[AxonConfig.Event.Type]
            MEMBER_REMOVED: _ClassVar[AxonConfig.Event.Type]
            MEMBER_ADDRESS_UPDATING: _ClassVar[AxonConfig.Event.Type]
            MEMBER_ADDRESS_UPDATED: _ClassVar[AxonConfig.Event.Type]
            MEMBER_STALE_CLUSTER_ID_CLEANUP: _ClassVar[AxonConfig.Event.Type]
            MEMBER_NB_SERVER_ID_UPDATED: _ClassVar[AxonConfig.Event.Type]
            MEMBER_SB_SERVER_ID_UPDATED: _ClassVar[AxonConfig.Event.Type]
            MEMBER_NB_CLUSTER_ID_UPDATED: _ClassVar[AxonConfig.Event.Type]
            MEMBER_SB_CLUSTER_ID_UPDATED: _ClassVar[AxonConfig.Event.Type]
            MEMBER_STALE_NB_CLUSTER_ID_CLEANUP: _ClassVar[AxonConfig.Event.Type]
            MEMBER_STALE_SB_CLUSTER_ID_CLEANUP: _ClassVar[AxonConfig.Event.Type]
            CLUSTER_CREATE_INITIATED: _ClassVar[AxonConfig.Event.Type]
            CLUSTER_CREATE_COMPLETED: _ClassVar[AxonConfig.Event.Type]
            CLUSTER_NB_CLUSTER_ID_UPDATED: _ClassVar[AxonConfig.Event.Type]
            CLUSTER_SB_CLUSTER_ID_UPDATED: _ClassVar[AxonConfig.Event.Type]
            CLUSTER_RECONSTRUCT_INITIATED: _ClassVar[AxonConfig.Event.Type]
            CLUSTER_RECONSTRUCT_COMPLETED: _ClassVar[AxonConfig.Event.Type]
            SB_RECONSTRUCT_INITIATED: _ClassVar[AxonConfig.Event.Type]
            CONFIG_MASTER_SYNC: _ClassVar[AxonConfig.Event.Type]
            CONFIG_NODE_SYNC: _ClassVar[AxonConfig.Event.Type]
            USER_MANUAL_UPDATE: _ClassVar[AxonConfig.Event.Type]
        UNKNOWN: AxonConfig.Event.Type
        MEMBER_ADDING: AxonConfig.Event.Type
        MEMBER_ADDED: AxonConfig.Event.Type
        MEMBER_REMOVING: AxonConfig.Event.Type
        MEMBER_REMOVED: AxonConfig.Event.Type
        MEMBER_ADDRESS_UPDATING: AxonConfig.Event.Type
        MEMBER_ADDRESS_UPDATED: AxonConfig.Event.Type
        MEMBER_STALE_CLUSTER_ID_CLEANUP: AxonConfig.Event.Type
        MEMBER_NB_SERVER_ID_UPDATED: AxonConfig.Event.Type
        MEMBER_SB_SERVER_ID_UPDATED: AxonConfig.Event.Type
        MEMBER_NB_CLUSTER_ID_UPDATED: AxonConfig.Event.Type
        MEMBER_SB_CLUSTER_ID_UPDATED: AxonConfig.Event.Type
        MEMBER_STALE_NB_CLUSTER_ID_CLEANUP: AxonConfig.Event.Type
        MEMBER_STALE_SB_CLUSTER_ID_CLEANUP: AxonConfig.Event.Type
        CLUSTER_CREATE_INITIATED: AxonConfig.Event.Type
        CLUSTER_CREATE_COMPLETED: AxonConfig.Event.Type
        CLUSTER_NB_CLUSTER_ID_UPDATED: AxonConfig.Event.Type
        CLUSTER_SB_CLUSTER_ID_UPDATED: AxonConfig.Event.Type
        CLUSTER_RECONSTRUCT_INITIATED: AxonConfig.Event.Type
        CLUSTER_RECONSTRUCT_COMPLETED: AxonConfig.Event.Type
        SB_RECONSTRUCT_INITIATED: AxonConfig.Event.Type
        CONFIG_MASTER_SYNC: AxonConfig.Event.Type
        CONFIG_NODE_SYNC: AxonConfig.Event.Type
        USER_MANUAL_UPDATE: AxonConfig.Event.Type
        TYPE_FIELD_NUMBER: _ClassVar[int]
        TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
        RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
        IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
        NODE_ID_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        type: AxonConfig.Event.Type
        timestamp: str
        resource_id: str
        ip_address: str
        node_id: int
        description: str
        def __init__(self, type: _Optional[_Union[AxonConfig.Event.Type, str]] = ..., timestamp: _Optional[str] = ..., resource_id: _Optional[str] = ..., ip_address: _Optional[str] = ..., node_id: _Optional[int] = ..., description: _Optional[str] = ...) -> None: ...
    class RaftClusterStatus(_message.Message):
        __slots__ = ("id", "incarnation", "create_timestamp")
        ID_FIELD_NUMBER: _ClassVar[int]
        INCARNATION_FIELD_NUMBER: _ClassVar[int]
        CREATE_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
        id: str
        incarnation: int
        create_timestamp: str
        def __init__(self, id: _Optional[str] = ..., incarnation: _Optional[int] = ..., create_timestamp: _Optional[str] = ...) -> None: ...
    NUM_NODES_FIELD_NUMBER: _ClassVar[int]
    IP_ADDRESSES_FIELD_NUMBER: _ClassVar[int]
    NODE_IDS_FIELD_NUMBER: _ClassVar[int]
    OVN_NB_PORT_FIELD_NUMBER: _ClassVar[int]
    OVN_SB_PORT_FIELD_NUMBER: _ClassVar[int]
    OVN_NB_RAFT_PORT_FIELD_NUMBER: _ClassVar[int]
    OVN_SB_RAFT_PORT_FIELD_NUMBER: _ClassVar[int]
    BLACKLIST_FIELD_NUMBER: _ClassVar[int]
    TUNNEL_INTF_GRP_ID_FIELD_NUMBER: _ClassVar[int]
    TUNNEL_VLAN_ID_FIELD_NUMBER: _ClassVar[int]
    USE_CUSTOM_INTERFACE_FOR_TUNNEL_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_EXTERNAL_INTF_GRP_ID_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_EXTERNAL_VLAN_ID_FIELD_NUMBER: _ClassVar[int]
    USE_CUSTOM_INTERFACE_FOR_DEFAULT_EXTERNAL_ACCESS_FIELD_NUMBER: _ClassVar[int]
    OVN_NB_RAFT_CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    OVN_SB_RAFT_CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    GANDALF_KEY_FIELD_NUMBER: _ClassVar[int]
    MASTER_NODE_ID_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATE_NODE_ID_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATE_OPERATION_ID_FIELD_NUMBER: _ClassVar[int]
    MEMBERS_STATUS_FIELD_NUMBER: _ClassVar[int]
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    RECONSTRUCT_RESOURCES_FIELD_NUMBER: _ClassVar[int]
    NORTHBOUND_STATUS_FIELD_NUMBER: _ClassVar[int]
    SOUTHBOUND_STATUS_FIELD_NUMBER: _ClassVar[int]
    num_nodes: int
    ip_addresses: _containers.RepeatedScalarFieldContainer[str]
    node_ids: _containers.RepeatedScalarFieldContainer[int]
    ovn_nb_port: int
    ovn_sb_port: int
    ovn_nb_raft_port: int
    ovn_sb_raft_port: int
    blacklist: _containers.RepeatedScalarFieldContainer[str]
    tunnel_intf_grp_id: int
    tunnel_vlan_id: int
    use_custom_interface_for_tunnel: bool
    default_external_intf_grp_id: int
    default_external_vlan_id: int
    use_custom_interface_for_default_external_access: bool
    ovn_nb_raft_cluster_id: str
    ovn_sb_raft_cluster_id: str
    gandalf_key: str
    master_node_id: int
    create_timestamp: str
    update_timestamp: str
    last_update_node_id: int
    last_update_operation_id: str
    members_status: _containers.MessageMap[int, AxonConfig.Member]
    events: _containers.RepeatedCompositeFieldContainer[AxonConfig.Event]
    reconstruct_resources: bool
    northbound_status: AxonConfig.RaftClusterStatus
    southbound_status: AxonConfig.RaftClusterStatus
    def __init__(self, num_nodes: _Optional[int] = ..., ip_addresses: _Optional[_Iterable[str]] = ..., node_ids: _Optional[_Iterable[int]] = ..., ovn_nb_port: _Optional[int] = ..., ovn_sb_port: _Optional[int] = ..., ovn_nb_raft_port: _Optional[int] = ..., ovn_sb_raft_port: _Optional[int] = ..., blacklist: _Optional[_Iterable[str]] = ..., tunnel_intf_grp_id: _Optional[int] = ..., tunnel_vlan_id: _Optional[int] = ..., use_custom_interface_for_tunnel: bool = ..., default_external_intf_grp_id: _Optional[int] = ..., default_external_vlan_id: _Optional[int] = ..., use_custom_interface_for_default_external_access: bool = ..., ovn_nb_raft_cluster_id: _Optional[str] = ..., ovn_sb_raft_cluster_id: _Optional[str] = ..., gandalf_key: _Optional[str] = ..., master_node_id: _Optional[int] = ..., create_timestamp: _Optional[str] = ..., update_timestamp: _Optional[str] = ..., last_update_node_id: _Optional[int] = ..., last_update_operation_id: _Optional[str] = ..., members_status: _Optional[_Mapping[int, AxonConfig.Member]] = ..., events: _Optional[_Iterable[_Union[AxonConfig.Event, _Mapping]]] = ..., reconstruct_resources: bool = ..., northbound_status: _Optional[_Union[AxonConfig.RaftClusterStatus, _Mapping]] = ..., southbound_status: _Optional[_Union[AxonConfig.RaftClusterStatus, _Mapping]] = ...) -> None: ...
