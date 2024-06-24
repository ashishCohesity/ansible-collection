from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class AtomStatsConfigProto(_message.Message):
    __slots__ = ("entity_id_attr", "owner_id_attr", "source_id_attr", "env_name_attr", "node_id_attr", "cluster_id_attr", "cluster_incarnation_id_attr", "time_to_live_secs", "internal_stats_time_to_live_secs")
    class Metric(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kReceivedBytes: _ClassVar[AtomStatsConfigProto.Metric]
        kCachedBytes: _ClassVar[AtomStatsConfigProto.Metric]
        kDroppedBytes: _ClassVar[AtomStatsConfigProto.Metric]
        kPersistedBytes: _ClassVar[AtomStatsConfigProto.Metric]
        kReplicatedBytes: _ClassVar[AtomStatsConfigProto.Metric]
    kReceivedBytes: AtomStatsConfigProto.Metric
    kCachedBytes: AtomStatsConfigProto.Metric
    kDroppedBytes: AtomStatsConfigProto.Metric
    kPersistedBytes: AtomStatsConfigProto.Metric
    kReplicatedBytes: AtomStatsConfigProto.Metric
    class EntityOwnerStatsSchema(_message.Message):
        __slots__ = ("name", "version", "id_attr", "descriptive_name", "help_text", "is_internal")
        NAME_FIELD_NUMBER: _ClassVar[int]
        VERSION_FIELD_NUMBER: _ClassVar[int]
        ID_ATTR_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTIVE_NAME_FIELD_NUMBER: _ClassVar[int]
        HELP_TEXT_FIELD_NUMBER: _ClassVar[int]
        IS_INTERNAL_FIELD_NUMBER: _ClassVar[int]
        name: str
        version: int
        id_attr: str
        descriptive_name: str
        help_text: str
        is_internal: bool
        def __init__(self, name: _Optional[str] = ..., version: _Optional[int] = ..., id_attr: _Optional[str] = ..., descriptive_name: _Optional[str] = ..., help_text: _Optional[str] = ..., is_internal: bool = ...) -> None: ...
    class EntityNodeStatsSchema(_message.Message):
        __slots__ = ("name", "version", "id_attr", "descriptive_name", "help_text", "is_internal")
        NAME_FIELD_NUMBER: _ClassVar[int]
        VERSION_FIELD_NUMBER: _ClassVar[int]
        ID_ATTR_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTIVE_NAME_FIELD_NUMBER: _ClassVar[int]
        HELP_TEXT_FIELD_NUMBER: _ClassVar[int]
        IS_INTERNAL_FIELD_NUMBER: _ClassVar[int]
        name: str
        version: int
        id_attr: str
        descriptive_name: str
        help_text: str
        is_internal: bool
        def __init__(self, name: _Optional[str] = ..., version: _Optional[int] = ..., id_attr: _Optional[str] = ..., descriptive_name: _Optional[str] = ..., help_text: _Optional[str] = ..., is_internal: bool = ...) -> None: ...
    class EntityClusterStatsSchema(_message.Message):
        __slots__ = ("name", "version", "id_attr", "descriptive_name", "help_text", "is_internal")
        NAME_FIELD_NUMBER: _ClassVar[int]
        VERSION_FIELD_NUMBER: _ClassVar[int]
        ID_ATTR_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTIVE_NAME_FIELD_NUMBER: _ClassVar[int]
        HELP_TEXT_FIELD_NUMBER: _ClassVar[int]
        IS_INTERNAL_FIELD_NUMBER: _ClassVar[int]
        name: str
        version: int
        id_attr: str
        descriptive_name: str
        help_text: str
        is_internal: bool
        def __init__(self, name: _Optional[str] = ..., version: _Optional[int] = ..., id_attr: _Optional[str] = ..., descriptive_name: _Optional[str] = ..., help_text: _Optional[str] = ..., is_internal: bool = ...) -> None: ...
    class EntityTargetNodeStatsSchema(_message.Message):
        __slots__ = ("name", "version", "id_attr", "descriptive_name", "help_text", "is_internal")
        NAME_FIELD_NUMBER: _ClassVar[int]
        VERSION_FIELD_NUMBER: _ClassVar[int]
        ID_ATTR_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTIVE_NAME_FIELD_NUMBER: _ClassVar[int]
        HELP_TEXT_FIELD_NUMBER: _ClassVar[int]
        IS_INTERNAL_FIELD_NUMBER: _ClassVar[int]
        name: str
        version: int
        id_attr: str
        descriptive_name: str
        help_text: str
        is_internal: bool
        def __init__(self, name: _Optional[str] = ..., version: _Optional[int] = ..., id_attr: _Optional[str] = ..., descriptive_name: _Optional[str] = ..., help_text: _Optional[str] = ..., is_internal: bool = ...) -> None: ...
    class EntityOwnerTargetNodeStatsSchema(_message.Message):
        __slots__ = ("name", "version", "id_attr", "descriptive_name", "help_text", "is_internal")
        NAME_FIELD_NUMBER: _ClassVar[int]
        VERSION_FIELD_NUMBER: _ClassVar[int]
        ID_ATTR_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTIVE_NAME_FIELD_NUMBER: _ClassVar[int]
        HELP_TEXT_FIELD_NUMBER: _ClassVar[int]
        IS_INTERNAL_FIELD_NUMBER: _ClassVar[int]
        name: str
        version: int
        id_attr: str
        descriptive_name: str
        help_text: str
        is_internal: bool
        def __init__(self, name: _Optional[str] = ..., version: _Optional[int] = ..., id_attr: _Optional[str] = ..., descriptive_name: _Optional[str] = ..., help_text: _Optional[str] = ..., is_internal: bool = ...) -> None: ...
    class EntityOwnerTargetStatsSchema(_message.Message):
        __slots__ = ("name", "version", "id_attr", "descriptive_name", "help_text", "is_internal")
        NAME_FIELD_NUMBER: _ClassVar[int]
        VERSION_FIELD_NUMBER: _ClassVar[int]
        ID_ATTR_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTIVE_NAME_FIELD_NUMBER: _ClassVar[int]
        HELP_TEXT_FIELD_NUMBER: _ClassVar[int]
        IS_INTERNAL_FIELD_NUMBER: _ClassVar[int]
        name: str
        version: int
        id_attr: str
        descriptive_name: str
        help_text: str
        is_internal: bool
        def __init__(self, name: _Optional[str] = ..., version: _Optional[int] = ..., id_attr: _Optional[str] = ..., descriptive_name: _Optional[str] = ..., help_text: _Optional[str] = ..., is_internal: bool = ...) -> None: ...
    class EntityOwnerReplicationStatsSchema(_message.Message):
        __slots__ = ("name", "version", "id_attr", "descriptive_name", "help_text", "is_internal")
        NAME_FIELD_NUMBER: _ClassVar[int]
        VERSION_FIELD_NUMBER: _ClassVar[int]
        ID_ATTR_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTIVE_NAME_FIELD_NUMBER: _ClassVar[int]
        HELP_TEXT_FIELD_NUMBER: _ClassVar[int]
        IS_INTERNAL_FIELD_NUMBER: _ClassVar[int]
        name: str
        version: int
        id_attr: str
        descriptive_name: str
        help_text: str
        is_internal: bool
        def __init__(self, name: _Optional[str] = ..., version: _Optional[int] = ..., id_attr: _Optional[str] = ..., descriptive_name: _Optional[str] = ..., help_text: _Optional[str] = ..., is_internal: bool = ...) -> None: ...
    class NodeReplicationStatsSchema(_message.Message):
        __slots__ = ("name", "version", "id_attr", "descriptive_name", "help_text", "is_internal")
        NAME_FIELD_NUMBER: _ClassVar[int]
        VERSION_FIELD_NUMBER: _ClassVar[int]
        ID_ATTR_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTIVE_NAME_FIELD_NUMBER: _ClassVar[int]
        HELP_TEXT_FIELD_NUMBER: _ClassVar[int]
        IS_INTERNAL_FIELD_NUMBER: _ClassVar[int]
        name: str
        version: int
        id_attr: str
        descriptive_name: str
        help_text: str
        is_internal: bool
        def __init__(self, name: _Optional[str] = ..., version: _Optional[int] = ..., id_attr: _Optional[str] = ..., descriptive_name: _Optional[str] = ..., help_text: _Optional[str] = ..., is_internal: bool = ...) -> None: ...
    class ClusterReplicationStatsSchema(_message.Message):
        __slots__ = ("name", "version", "id_attr", "descriptive_name", "help_text", "is_internal")
        NAME_FIELD_NUMBER: _ClassVar[int]
        VERSION_FIELD_NUMBER: _ClassVar[int]
        ID_ATTR_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTIVE_NAME_FIELD_NUMBER: _ClassVar[int]
        HELP_TEXT_FIELD_NUMBER: _ClassVar[int]
        IS_INTERNAL_FIELD_NUMBER: _ClassVar[int]
        name: str
        version: int
        id_attr: str
        descriptive_name: str
        help_text: str
        is_internal: bool
        def __init__(self, name: _Optional[str] = ..., version: _Optional[int] = ..., id_attr: _Optional[str] = ..., descriptive_name: _Optional[str] = ..., help_text: _Optional[str] = ..., is_internal: bool = ...) -> None: ...
    class TargetNodeStatsSchema(_message.Message):
        __slots__ = ("name", "version", "id_attr", "descriptive_name", "help_text", "is_internal")
        NAME_FIELD_NUMBER: _ClassVar[int]
        VERSION_FIELD_NUMBER: _ClassVar[int]
        ID_ATTR_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTIVE_NAME_FIELD_NUMBER: _ClassVar[int]
        HELP_TEXT_FIELD_NUMBER: _ClassVar[int]
        IS_INTERNAL_FIELD_NUMBER: _ClassVar[int]
        name: str
        version: int
        id_attr: str
        descriptive_name: str
        help_text: str
        is_internal: bool
        def __init__(self, name: _Optional[str] = ..., version: _Optional[int] = ..., id_attr: _Optional[str] = ..., descriptive_name: _Optional[str] = ..., help_text: _Optional[str] = ..., is_internal: bool = ...) -> None: ...
    class TargetStatsSchema(_message.Message):
        __slots__ = ("name", "version", "id_attr", "descriptive_name", "help_text", "is_internal")
        NAME_FIELD_NUMBER: _ClassVar[int]
        VERSION_FIELD_NUMBER: _ClassVar[int]
        ID_ATTR_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTIVE_NAME_FIELD_NUMBER: _ClassVar[int]
        HELP_TEXT_FIELD_NUMBER: _ClassVar[int]
        IS_INTERNAL_FIELD_NUMBER: _ClassVar[int]
        name: str
        version: int
        id_attr: str
        descriptive_name: str
        help_text: str
        is_internal: bool
        def __init__(self, name: _Optional[str] = ..., version: _Optional[int] = ..., id_attr: _Optional[str] = ..., descriptive_name: _Optional[str] = ..., help_text: _Optional[str] = ..., is_internal: bool = ...) -> None: ...
    ENTITY_ID_ATTR_FIELD_NUMBER: _ClassVar[int]
    OWNER_ID_ATTR_FIELD_NUMBER: _ClassVar[int]
    SOURCE_ID_ATTR_FIELD_NUMBER: _ClassVar[int]
    ENV_NAME_ATTR_FIELD_NUMBER: _ClassVar[int]
    NODE_ID_ATTR_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_ATTR_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_INCARNATION_ID_ATTR_FIELD_NUMBER: _ClassVar[int]
    TIME_TO_LIVE_SECS_FIELD_NUMBER: _ClassVar[int]
    INTERNAL_STATS_TIME_TO_LIVE_SECS_FIELD_NUMBER: _ClassVar[int]
    entity_id_attr: str
    owner_id_attr: str
    source_id_attr: str
    env_name_attr: str
    node_id_attr: str
    cluster_id_attr: str
    cluster_incarnation_id_attr: str
    time_to_live_secs: int
    internal_stats_time_to_live_secs: int
    def __init__(self, entity_id_attr: _Optional[str] = ..., owner_id_attr: _Optional[str] = ..., source_id_attr: _Optional[str] = ..., env_name_attr: _Optional[str] = ..., node_id_attr: _Optional[str] = ..., cluster_id_attr: _Optional[str] = ..., cluster_incarnation_id_attr: _Optional[str] = ..., time_to_live_secs: _Optional[int] = ..., internal_stats_time_to_live_secs: _Optional[int] = ...) -> None: ...

class AtomResourceUsageStatsConfigProto(_message.Message):
    __slots__ = ("node_id_attr", "time_to_live_secs", "internal_stats_time_to_live_secs")
    class Metric(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kCpuUtilizationPct: _ClassVar[AtomResourceUsageStatsConfigProto.Metric]
        kMemoryUsageBytes: _ClassVar[AtomResourceUsageStatsConfigProto.Metric]
        kMemoryUsagePct: _ClassVar[AtomResourceUsageStatsConfigProto.Metric]
    kCpuUtilizationPct: AtomResourceUsageStatsConfigProto.Metric
    kMemoryUsageBytes: AtomResourceUsageStatsConfigProto.Metric
    kMemoryUsagePct: AtomResourceUsageStatsConfigProto.Metric
    class AtomNodeStatsSchema(_message.Message):
        __slots__ = ("name", "version", "id_attr", "descriptive_name", "help_text", "is_internal")
        NAME_FIELD_NUMBER: _ClassVar[int]
        VERSION_FIELD_NUMBER: _ClassVar[int]
        ID_ATTR_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTIVE_NAME_FIELD_NUMBER: _ClassVar[int]
        HELP_TEXT_FIELD_NUMBER: _ClassVar[int]
        IS_INTERNAL_FIELD_NUMBER: _ClassVar[int]
        name: str
        version: int
        id_attr: str
        descriptive_name: str
        help_text: str
        is_internal: bool
        def __init__(self, name: _Optional[str] = ..., version: _Optional[int] = ..., id_attr: _Optional[str] = ..., descriptive_name: _Optional[str] = ..., help_text: _Optional[str] = ..., is_internal: bool = ...) -> None: ...
    NODE_ID_ATTR_FIELD_NUMBER: _ClassVar[int]
    TIME_TO_LIVE_SECS_FIELD_NUMBER: _ClassVar[int]
    INTERNAL_STATS_TIME_TO_LIVE_SECS_FIELD_NUMBER: _ClassVar[int]
    node_id_attr: str
    time_to_live_secs: int
    internal_stats_time_to_live_secs: int
    def __init__(self, node_id_attr: _Optional[str] = ..., time_to_live_secs: _Optional[int] = ..., internal_stats_time_to_live_secs: _Optional[int] = ...) -> None: ...
