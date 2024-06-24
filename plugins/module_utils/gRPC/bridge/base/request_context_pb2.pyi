from configs import cluster_config_pb2 as _cluster_config_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class WorkloadType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kUnknown: _ClassVar[WorkloadType]
    kBackup: _ClassVar[WorkloadType]
    kArchive: _ClassVar[WorkloadType]
    kRestore: _ClassVar[WorkloadType]
    kReplication: _ClassVar[WorkloadType]
    kSmartFiles: _ClassVar[WorkloadType]
    kIndexing: _ClassVar[WorkloadType]
    kApps: _ClassVar[WorkloadType]
    kBackground: _ClassVar[WorkloadType]
    kOther: _ClassVar[WorkloadType]
    kHealer: _ClassVar[WorkloadType]
kUnknown: WorkloadType
kBackup: WorkloadType
kArchive: WorkloadType
kRestore: WorkloadType
kReplication: WorkloadType
kSmartFiles: WorkloadType
kIndexing: WorkloadType
kApps: WorkloadType
kBackground: WorkloadType
kOther: WorkloadType
kHealer: WorkloadType

class WorkloadTag(_message.Message):
    __slots__ = ("tag", "emit_node_level_stats")
    TAG_FIELD_NUMBER: _ClassVar[int]
    EMIT_NODE_LEVEL_STATS_FIELD_NUMBER: _ClassVar[int]
    tag: str
    emit_node_level_stats: bool
    def __init__(self, tag: _Optional[str] = ..., emit_node_level_stats: bool = ...) -> None: ...

class RequestContextProto(_message.Message):
    __slots__ = ("ip", "ip_epoch", "request_id", "client_ip", "portal_type", "qos_context", "qos_principal", "request_trace_id_high", "request_trace_id_low", "is_magneto_request", "view_pin_secs", "chunk_file_max_pin_secs", "should_retain_trace", "workload_attrs", "is_preemptable", "workload_type")
    class WorkloadAttributes(_message.Message):
        __slots__ = ("tags_vec", "union_with_view_tags")
        TAGS_VEC_FIELD_NUMBER: _ClassVar[int]
        UNION_WITH_VIEW_TAGS_FIELD_NUMBER: _ClassVar[int]
        tags_vec: _containers.RepeatedCompositeFieldContainer[WorkloadTag]
        union_with_view_tags: bool
        def __init__(self, tags_vec: _Optional[_Iterable[_Union[WorkloadTag, _Mapping]]] = ..., union_with_view_tags: bool = ...) -> None: ...
    IP_FIELD_NUMBER: _ClassVar[int]
    IP_EPOCH_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_IP_FIELD_NUMBER: _ClassVar[int]
    PORTAL_TYPE_FIELD_NUMBER: _ClassVar[int]
    QOS_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    QOS_PRINCIPAL_FIELD_NUMBER: _ClassVar[int]
    REQUEST_TRACE_ID_HIGH_FIELD_NUMBER: _ClassVar[int]
    REQUEST_TRACE_ID_LOW_FIELD_NUMBER: _ClassVar[int]
    IS_MAGNETO_REQUEST_FIELD_NUMBER: _ClassVar[int]
    VIEW_PIN_SECS_FIELD_NUMBER: _ClassVar[int]
    CHUNK_FILE_MAX_PIN_SECS_FIELD_NUMBER: _ClassVar[int]
    SHOULD_RETAIN_TRACE_FIELD_NUMBER: _ClassVar[int]
    WORKLOAD_ATTRS_FIELD_NUMBER: _ClassVar[int]
    IS_PREEMPTABLE_FIELD_NUMBER: _ClassVar[int]
    WORKLOAD_TYPE_FIELD_NUMBER: _ClassVar[int]
    ip: str
    ip_epoch: int
    request_id: int
    client_ip: str
    portal_type: int
    qos_context: _cluster_config_pb2.ClusterConfigProto.QoSMapping.QoSContext
    qos_principal: _cluster_config_pb2.ClusterConfigProto.QoSPrincipal
    request_trace_id_high: int
    request_trace_id_low: int
    is_magneto_request: bool
    view_pin_secs: int
    chunk_file_max_pin_secs: int
    should_retain_trace: bool
    workload_attrs: RequestContextProto.WorkloadAttributes
    is_preemptable: bool
    workload_type: WorkloadType
    def __init__(self, ip: _Optional[str] = ..., ip_epoch: _Optional[int] = ..., request_id: _Optional[int] = ..., client_ip: _Optional[str] = ..., portal_type: _Optional[int] = ..., qos_context: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.QoSMapping.QoSContext, _Mapping]] = ..., qos_principal: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.QoSPrincipal, _Mapping]] = ..., request_trace_id_high: _Optional[int] = ..., request_trace_id_low: _Optional[int] = ..., is_magneto_request: bool = ..., view_pin_secs: _Optional[int] = ..., chunk_file_max_pin_secs: _Optional[int] = ..., should_retain_trace: bool = ..., workload_attrs: _Optional[_Union[RequestContextProto.WorkloadAttributes, _Mapping]] = ..., is_preemptable: bool = ..., workload_type: _Optional[_Union[WorkloadType, str]] = ...) -> None: ...
