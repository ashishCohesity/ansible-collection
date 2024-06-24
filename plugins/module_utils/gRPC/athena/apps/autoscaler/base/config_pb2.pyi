from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GcpConfigProto(_message.Message):
    __slots__ = ("project_id", "region", "zone")
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    ZONE_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    region: str
    zone: str
    def __init__(self, project_id: _Optional[str] = ..., region: _Optional[str] = ..., zone: _Optional[str] = ...) -> None: ...

class PolicyConfigProto(_message.Message):
    __slots__ = ("min_nodes_count", "min_hdd_count_per_node", "max_hdd_count_per_node", "usage_type", "scale_up_threshold", "scale_down_threshold")
    class UsageType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kClusterUsage: _ClassVar[PolicyConfigProto.UsageType]
        kNodeUsage: _ClassVar[PolicyConfigProto.UsageType]
        kDiskUsage: _ClassVar[PolicyConfigProto.UsageType]
    kClusterUsage: PolicyConfigProto.UsageType
    kNodeUsage: PolicyConfigProto.UsageType
    kDiskUsage: PolicyConfigProto.UsageType
    MIN_NODES_COUNT_FIELD_NUMBER: _ClassVar[int]
    MIN_HDD_COUNT_PER_NODE_FIELD_NUMBER: _ClassVar[int]
    MAX_HDD_COUNT_PER_NODE_FIELD_NUMBER: _ClassVar[int]
    USAGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    SCALE_UP_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    SCALE_DOWN_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    min_nodes_count: int
    min_hdd_count_per_node: int
    max_hdd_count_per_node: int
    usage_type: PolicyConfigProto.UsageType
    scale_up_threshold: float
    scale_down_threshold: float
    def __init__(self, min_nodes_count: _Optional[int] = ..., min_hdd_count_per_node: _Optional[int] = ..., max_hdd_count_per_node: _Optional[int] = ..., usage_type: _Optional[_Union[PolicyConfigProto.UsageType, str]] = ..., scale_up_threshold: _Optional[float] = ..., scale_down_threshold: _Optional[float] = ...) -> None: ...

class ConfigProto(_message.Message):
    __slots__ = ("gcp_config", "policy_config")
    GCP_CONFIG_FIELD_NUMBER: _ClassVar[int]
    POLICY_CONFIG_FIELD_NUMBER: _ClassVar[int]
    gcp_config: GcpConfigProto
    policy_config: PolicyConfigProto
    def __init__(self, gcp_config: _Optional[_Union[GcpConfigProto, _Mapping]] = ..., policy_config: _Optional[_Union[PolicyConfigProto, _Mapping]] = ...) -> None: ...
