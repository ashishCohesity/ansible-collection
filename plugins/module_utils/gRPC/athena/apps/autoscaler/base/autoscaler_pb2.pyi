from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DbEntryProto(_message.Message):
    __slots__ = ("id", "action_proto", "cluster_info", "cluster_stats", "start_time_msecs", "end_time_msecs", "retry_attempt")
    ID_FIELD_NUMBER: _ClassVar[int]
    ACTION_PROTO_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_INFO_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_STATS_FIELD_NUMBER: _ClassVar[int]
    START_TIME_MSECS_FIELD_NUMBER: _ClassVar[int]
    END_TIME_MSECS_FIELD_NUMBER: _ClassVar[int]
    RETRY_ATTEMPT_FIELD_NUMBER: _ClassVar[int]
    id: int
    action_proto: ActionProto
    cluster_info: ClusterInfoProto
    cluster_stats: ProcessClusterStatsArg
    start_time_msecs: int
    end_time_msecs: int
    retry_attempt: int
    def __init__(self, id: _Optional[int] = ..., action_proto: _Optional[_Union[ActionProto, _Mapping]] = ..., cluster_info: _Optional[_Union[ClusterInfoProto, _Mapping]] = ..., cluster_stats: _Optional[_Union[ProcessClusterStatsArg, _Mapping]] = ..., start_time_msecs: _Optional[int] = ..., end_time_msecs: _Optional[int] = ..., retry_attempt: _Optional[int] = ...) -> None: ...

class ActionProto(_message.Message):
    __slots__ = ("action", "add_disk_action", "add_node_action", "remove_disk_action", "remove_node_action", "state")
    class ActionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kAddDisk: _ClassVar[ActionProto.ActionType]
        kAddNode: _ClassVar[ActionProto.ActionType]
        kRemoveDisk: _ClassVar[ActionProto.ActionType]
        kRemoveNode: _ClassVar[ActionProto.ActionType]
    kAddDisk: ActionProto.ActionType
    kAddNode: ActionProto.ActionType
    kRemoveDisk: ActionProto.ActionType
    kRemoveNode: ActionProto.ActionType
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kInProgress: _ClassVar[ActionProto.State]
        kFailed: _ClassVar[ActionProto.State]
        kFinished: _ClassVar[ActionProto.State]
    kInProgress: ActionProto.State
    kFailed: ActionProto.State
    kFinished: ActionProto.State
    ACTION_FIELD_NUMBER: _ClassVar[int]
    ADD_DISK_ACTION_FIELD_NUMBER: _ClassVar[int]
    ADD_NODE_ACTION_FIELD_NUMBER: _ClassVar[int]
    REMOVE_DISK_ACTION_FIELD_NUMBER: _ClassVar[int]
    REMOVE_NODE_ACTION_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    action: ActionProto.ActionType
    add_disk_action: AddDiskAction
    add_node_action: AddNodeAction
    remove_disk_action: RemoveDiskAction
    remove_node_action: RemoveNodeAction
    state: ActionProto.State
    def __init__(self, action: _Optional[_Union[ActionProto.ActionType, str]] = ..., add_disk_action: _Optional[_Union[AddDiskAction, _Mapping]] = ..., add_node_action: _Optional[_Union[AddNodeAction, _Mapping]] = ..., remove_disk_action: _Optional[_Union[RemoveDiskAction, _Mapping]] = ..., remove_node_action: _Optional[_Union[RemoveNodeAction, _Mapping]] = ..., state: _Optional[_Union[ActionProto.State, str]] = ...) -> None: ...

class AddDiskAction(_message.Message):
    __slots__ = ("disk_type", "disk_info_vec")
    class AddDiskInfo(_message.Message):
        __slots__ = ("disk_name", "node_id")
        DISK_NAME_FIELD_NUMBER: _ClassVar[int]
        NODE_ID_FIELD_NUMBER: _ClassVar[int]
        disk_name: str
        node_id: int
        def __init__(self, disk_name: _Optional[str] = ..., node_id: _Optional[int] = ...) -> None: ...
    DISK_TYPE_FIELD_NUMBER: _ClassVar[int]
    DISK_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    disk_type: str
    disk_info_vec: _containers.RepeatedCompositeFieldContainer[AddDiskAction.AddDiskInfo]
    def __init__(self, disk_type: _Optional[str] = ..., disk_info_vec: _Optional[_Iterable[_Union[AddDiskAction.AddDiskInfo, _Mapping]]] = ...) -> None: ...

class AddNodeAction(_message.Message):
    __slots__ = ("vm_name",)
    VM_NAME_FIELD_NUMBER: _ClassVar[int]
    vm_name: str
    def __init__(self, vm_name: _Optional[str] = ...) -> None: ...

class RemoveDiskAction(_message.Message):
    __slots__ = ("disk_info_vec",)
    class RemoveDiskInfo(_message.Message):
        __slots__ = ("disk_name", "node_id")
        DISK_NAME_FIELD_NUMBER: _ClassVar[int]
        NODE_ID_FIELD_NUMBER: _ClassVar[int]
        disk_name: str
        node_id: int
        def __init__(self, disk_name: _Optional[str] = ..., node_id: _Optional[int] = ...) -> None: ...
    DISK_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    disk_info_vec: _containers.RepeatedCompositeFieldContainer[RemoveDiskAction.RemoveDiskInfo]
    def __init__(self, disk_info_vec: _Optional[_Iterable[_Union[RemoveDiskAction.RemoveDiskInfo, _Mapping]]] = ...) -> None: ...

class RemoveNodeAction(_message.Message):
    __slots__ = ("vm_name",)
    VM_NAME_FIELD_NUMBER: _ClassVar[int]
    vm_name: str
    def __init__(self, vm_name: _Optional[str] = ...) -> None: ...

class ProcessClusterStatsArg(_message.Message):
    __slots__ = ("cluster_usage", "node_info_vec")
    class NodeInfo(_message.Message):
        __slots__ = ("node_id", "node_usage", "disk_info_vec")
        class DiskInfo(_message.Message):
            __slots__ = ("disk_id", "disk_usage")
            DISK_ID_FIELD_NUMBER: _ClassVar[int]
            DISK_USAGE_FIELD_NUMBER: _ClassVar[int]
            disk_id: int
            disk_usage: float
            def __init__(self, disk_id: _Optional[int] = ..., disk_usage: _Optional[float] = ...) -> None: ...
        NODE_ID_FIELD_NUMBER: _ClassVar[int]
        NODE_USAGE_FIELD_NUMBER: _ClassVar[int]
        DISK_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
        node_id: int
        node_usage: float
        disk_info_vec: _containers.RepeatedCompositeFieldContainer[ProcessClusterStatsArg.NodeInfo.DiskInfo]
        def __init__(self, node_id: _Optional[int] = ..., node_usage: _Optional[float] = ..., disk_info_vec: _Optional[_Iterable[_Union[ProcessClusterStatsArg.NodeInfo.DiskInfo, _Mapping]]] = ...) -> None: ...
    CLUSTER_USAGE_FIELD_NUMBER: _ClassVar[int]
    NODE_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    cluster_usage: float
    node_info_vec: _containers.RepeatedCompositeFieldContainer[ProcessClusterStatsArg.NodeInfo]
    def __init__(self, cluster_usage: _Optional[float] = ..., node_info_vec: _Optional[_Iterable[_Union[ProcessClusterStatsArg.NodeInfo, _Mapping]]] = ...) -> None: ...

class ProcessClusterStatsResult(_message.Message):
    __slots__ = ("action",)
    ACTION_FIELD_NUMBER: _ClassVar[int]
    action: ActionProto
    def __init__(self, action: _Optional[_Union[ActionProto, _Mapping]] = ...) -> None: ...

class DiskInfoProto(_message.Message):
    __slots__ = ("disk_id", "disk_name")
    DISK_ID_FIELD_NUMBER: _ClassVar[int]
    DISK_NAME_FIELD_NUMBER: _ClassVar[int]
    disk_id: int
    disk_name: str
    def __init__(self, disk_id: _Optional[int] = ..., disk_name: _Optional[str] = ...) -> None: ...

class NodeInfoProto(_message.Message):
    __slots__ = ("node_id", "vm_name", "node_ip", "disk_info_vec")
    class DiskInfoVecEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: DiskInfoProto
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[DiskInfoProto, _Mapping]] = ...) -> None: ...
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    VM_NAME_FIELD_NUMBER: _ClassVar[int]
    NODE_IP_FIELD_NUMBER: _ClassVar[int]
    DISK_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    node_id: int
    vm_name: str
    node_ip: str
    disk_info_vec: _containers.MessageMap[int, DiskInfoProto]
    def __init__(self, node_id: _Optional[int] = ..., vm_name: _Optional[str] = ..., node_ip: _Optional[str] = ..., disk_info_vec: _Optional[_Mapping[int, DiskInfoProto]] = ...) -> None: ...

class ClusterInfoProto(_message.Message):
    __slots__ = ("cluster_id", "incarnation_id", "node_info_map", "gcp_info")
    class NodeInfoMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: NodeInfoProto
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[NodeInfoProto, _Mapping]] = ...) -> None: ...
    class GcpInfo(_message.Message):
        __slots__ = ("vm_model",)
        VM_MODEL_FIELD_NUMBER: _ClassVar[int]
        vm_model: str
        def __init__(self, vm_model: _Optional[str] = ...) -> None: ...
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    NODE_INFO_MAP_FIELD_NUMBER: _ClassVar[int]
    GCP_INFO_FIELD_NUMBER: _ClassVar[int]
    cluster_id: int
    incarnation_id: int
    node_info_map: _containers.MessageMap[int, NodeInfoProto]
    gcp_info: ClusterInfoProto.GcpInfo
    def __init__(self, cluster_id: _Optional[int] = ..., incarnation_id: _Optional[int] = ..., node_info_map: _Optional[_Mapping[int, NodeInfoProto]] = ..., gcp_info: _Optional[_Union[ClusterInfoProto.GcpInfo, _Mapping]] = ...) -> None: ...
