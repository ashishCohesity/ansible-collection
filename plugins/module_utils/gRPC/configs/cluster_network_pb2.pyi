from configs import node_network_pb2 as _node_network_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ClusterNetworkProto(_message.Message):
    __slots__ = ("cluster_network_config_gandalf_key", "node_group_vec", "node_network_vec", "sysctl_settings")
    class sysctl_setting(_message.Message):
        __slots__ = ("conf_key", "value")
        CONF_KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        conf_key: str
        value: str
        def __init__(self, conf_key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class sysctl_setting_conf(_message.Message):
        __slots__ = ("sysctl_setting_vec", "version")
        SYSCTL_SETTING_VEC_FIELD_NUMBER: _ClassVar[int]
        VERSION_FIELD_NUMBER: _ClassVar[int]
        sysctl_setting_vec: _containers.RepeatedCompositeFieldContainer[ClusterNetworkProto.sysctl_setting]
        version: int
        def __init__(self, sysctl_setting_vec: _Optional[_Iterable[_Union[ClusterNetworkProto.sysctl_setting, _Mapping]]] = ..., version: _Optional[int] = ...) -> None: ...
    CLUSTER_NETWORK_CONFIG_GANDALF_KEY_FIELD_NUMBER: _ClassVar[int]
    NODE_GROUP_VEC_FIELD_NUMBER: _ClassVar[int]
    NODE_NETWORK_VEC_FIELD_NUMBER: _ClassVar[int]
    SYSCTL_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    cluster_network_config_gandalf_key: str
    node_group_vec: _containers.RepeatedCompositeFieldContainer[_node_network_pb2.NodeGroup]
    node_network_vec: _containers.RepeatedCompositeFieldContainer[_node_network_pb2.NodeNetworkProto]
    sysctl_settings: ClusterNetworkProto.sysctl_setting_conf
    def __init__(self, cluster_network_config_gandalf_key: _Optional[str] = ..., node_group_vec: _Optional[_Iterable[_Union[_node_network_pb2.NodeGroup, _Mapping]]] = ..., node_network_vec: _Optional[_Iterable[_Union[_node_network_pb2.NodeNetworkProto, _Mapping]]] = ..., sysctl_settings: _Optional[_Union[ClusterNetworkProto.sysctl_setting_conf, _Mapping]] = ...) -> None: ...
