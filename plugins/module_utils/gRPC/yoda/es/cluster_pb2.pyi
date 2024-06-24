from yoda.es import jsonname_pb2 as _jsonname_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ClusterState(_message.Message):
    __slots__ = ("cluster_name", "version", "master_node", "nodes", "shard_state")
    class NodeDataMap(_message.Message):
        __slots__ = ("node_id", "node_data")
        NODE_ID_FIELD_NUMBER: _ClassVar[int]
        NODE_DATA_FIELD_NUMBER: _ClassVar[int]
        node_id: str
        node_data: NodeData
        def __init__(self, node_id: _Optional[str] = ..., node_data: _Optional[_Union[NodeData, _Mapping]] = ...) -> None: ...
    CLUSTER_NAME_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    MASTER_NODE_FIELD_NUMBER: _ClassVar[int]
    NODES_FIELD_NUMBER: _ClassVar[int]
    SHARD_STATE_FIELD_NUMBER: _ClassVar[int]
    cluster_name: str
    version: int
    master_node: str
    nodes: _containers.RepeatedCompositeFieldContainer[ClusterState.NodeDataMap]
    shard_state: _containers.RepeatedCompositeFieldContainer[ShardState]
    def __init__(self, cluster_name: _Optional[str] = ..., version: _Optional[int] = ..., master_node: _Optional[str] = ..., nodes: _Optional[_Iterable[_Union[ClusterState.NodeDataMap, _Mapping]]] = ..., shard_state: _Optional[_Iterable[_Union[ShardState, _Mapping]]] = ...) -> None: ...

class NodeData(_message.Message):
    __slots__ = ("name", "transport_address")
    NAME_FIELD_NUMBER: _ClassVar[int]
    TRANSPORT_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    name: str
    transport_address: str
    def __init__(self, name: _Optional[str] = ..., transport_address: _Optional[str] = ...) -> None: ...

class ShardState(_message.Message):
    __slots__ = ("state", "primary", "node_id", "relocating_node_id", "shard", "index_name")
    STATE_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_FIELD_NUMBER: _ClassVar[int]
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    RELOCATING_NODE_ID_FIELD_NUMBER: _ClassVar[int]
    SHARD_FIELD_NUMBER: _ClassVar[int]
    INDEX_NAME_FIELD_NUMBER: _ClassVar[int]
    state: str
    primary: bool
    node_id: str
    relocating_node_id: str
    shard: int
    index_name: str
    def __init__(self, state: _Optional[str] = ..., primary: bool = ..., node_id: _Optional[str] = ..., relocating_node_id: _Optional[str] = ..., shard: _Optional[int] = ..., index_name: _Optional[str] = ...) -> None: ...

class ClusterAllocation(_message.Message):
    __slots__ = ("commands",)
    COMMANDS_FIELD_NUMBER: _ClassVar[int]
    commands: _containers.RepeatedCompositeFieldContainer[ClusterAllocationCommand]
    def __init__(self, commands: _Optional[_Iterable[_Union[ClusterAllocationCommand, _Mapping]]] = ...) -> None: ...

class ClusterAllocationCommand(_message.Message):
    __slots__ = ("move", "allocate_replica", "cancel", "allocate_stale_primary", "allocate_empty_primary")
    MOVE_FIELD_NUMBER: _ClassVar[int]
    ALLOCATE_REPLICA_FIELD_NUMBER: _ClassVar[int]
    CANCEL_FIELD_NUMBER: _ClassVar[int]
    ALLOCATE_STALE_PRIMARY_FIELD_NUMBER: _ClassVar[int]
    ALLOCATE_EMPTY_PRIMARY_FIELD_NUMBER: _ClassVar[int]
    move: MoveCommand
    allocate_replica: AssignReplicaCommand
    cancel: CancelCommand
    allocate_stale_primary: AssignPrimaryCommand
    allocate_empty_primary: AssignPrimaryCommand
    def __init__(self, move: _Optional[_Union[MoveCommand, _Mapping]] = ..., allocate_replica: _Optional[_Union[AssignReplicaCommand, _Mapping]] = ..., cancel: _Optional[_Union[CancelCommand, _Mapping]] = ..., allocate_stale_primary: _Optional[_Union[AssignPrimaryCommand, _Mapping]] = ..., allocate_empty_primary: _Optional[_Union[AssignPrimaryCommand, _Mapping]] = ...) -> None: ...

class MoveCommand(_message.Message):
    __slots__ = ("index", "shard", "from_node", "to_node")
    INDEX_FIELD_NUMBER: _ClassVar[int]
    SHARD_FIELD_NUMBER: _ClassVar[int]
    FROM_NODE_FIELD_NUMBER: _ClassVar[int]
    TO_NODE_FIELD_NUMBER: _ClassVar[int]
    index: str
    shard: int
    from_node: str
    to_node: str
    def __init__(self, index: _Optional[str] = ..., shard: _Optional[int] = ..., from_node: _Optional[str] = ..., to_node: _Optional[str] = ...) -> None: ...

class CancelCommand(_message.Message):
    __slots__ = ("index", "shard", "node", "allow_primary")
    INDEX_FIELD_NUMBER: _ClassVar[int]
    SHARD_FIELD_NUMBER: _ClassVar[int]
    NODE_FIELD_NUMBER: _ClassVar[int]
    ALLOW_PRIMARY_FIELD_NUMBER: _ClassVar[int]
    index: str
    shard: int
    node: str
    allow_primary: bool
    def __init__(self, index: _Optional[str] = ..., shard: _Optional[int] = ..., node: _Optional[str] = ..., allow_primary: bool = ...) -> None: ...

class AssignReplicaCommand(_message.Message):
    __slots__ = ("index", "shard", "node")
    INDEX_FIELD_NUMBER: _ClassVar[int]
    SHARD_FIELD_NUMBER: _ClassVar[int]
    NODE_FIELD_NUMBER: _ClassVar[int]
    index: str
    shard: int
    node: str
    def __init__(self, index: _Optional[str] = ..., shard: _Optional[int] = ..., node: _Optional[str] = ...) -> None: ...

class AssignPrimaryCommand(_message.Message):
    __slots__ = ("index", "shard", "node", "accept_data_loss")
    INDEX_FIELD_NUMBER: _ClassVar[int]
    SHARD_FIELD_NUMBER: _ClassVar[int]
    NODE_FIELD_NUMBER: _ClassVar[int]
    ACCEPT_DATA_LOSS_FIELD_NUMBER: _ClassVar[int]
    index: str
    shard: int
    node: str
    accept_data_loss: bool
    def __init__(self, index: _Optional[str] = ..., shard: _Optional[int] = ..., node: _Optional[str] = ..., accept_data_loss: bool = ...) -> None: ...

class ClusterHealth(_message.Message):
    __slots__ = ("cluster_name", "status", "timed_out", "number_of_nodes", "number_of_data_nodes", "active_primary_shards", "active_shards", "relocating_shards", "initializing_shards", "unassigned_shards")
    CLUSTER_NAME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TIMED_OUT_FIELD_NUMBER: _ClassVar[int]
    NUMBER_OF_NODES_FIELD_NUMBER: _ClassVar[int]
    NUMBER_OF_DATA_NODES_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_PRIMARY_SHARDS_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_SHARDS_FIELD_NUMBER: _ClassVar[int]
    RELOCATING_SHARDS_FIELD_NUMBER: _ClassVar[int]
    INITIALIZING_SHARDS_FIELD_NUMBER: _ClassVar[int]
    UNASSIGNED_SHARDS_FIELD_NUMBER: _ClassVar[int]
    cluster_name: str
    status: str
    timed_out: bool
    number_of_nodes: int
    number_of_data_nodes: int
    active_primary_shards: int
    active_shards: int
    relocating_shards: int
    initializing_shards: int
    unassigned_shards: int
    def __init__(self, cluster_name: _Optional[str] = ..., status: _Optional[str] = ..., timed_out: bool = ..., number_of_nodes: _Optional[int] = ..., number_of_data_nodes: _Optional[int] = ..., active_primary_shards: _Optional[int] = ..., active_shards: _Optional[int] = ..., relocating_shards: _Optional[int] = ..., initializing_shards: _Optional[int] = ..., unassigned_shards: _Optional[int] = ...) -> None: ...
