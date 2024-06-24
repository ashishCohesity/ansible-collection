from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class MadroxStatsConfigProto(_message.Message):
    __slots__ = ("time_to_live_secs", "internal_stats_time_to_live_secs", "cluster_id_attr", "cluster_incarnation_id_attr")
    class Metric(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kTxLogicalBytes: _ClassVar[MadroxStatsConfigProto.Metric]
        kTxPhysicalBytes: _ClassVar[MadroxStatsConfigProto.Metric]
        kTxPhysicalBytesMorphed: _ClassVar[MadroxStatsConfigProto.Metric]
        kTxMetadataActions: _ClassVar[MadroxStatsConfigProto.Metric]
        kTxWanLatencyUsecs: _ClassVar[MadroxStatsConfigProto.Metric]
        kRxLogicalBytes: _ClassVar[MadroxStatsConfigProto.Metric]
        kRxPhysicalBytes: _ClassVar[MadroxStatsConfigProto.Metric]
        kTxRPCRoundTripLatencyUsecs: _ClassVar[MadroxStatsConfigProto.Metric]
        kTxFileSyncLogicalBytes: _ClassVar[MadroxStatsConfigProto.Metric]
        kTxDirSyncNewViewChildren: _ClassVar[MadroxStatsConfigProto.Metric]
    kTxLogicalBytes: MadroxStatsConfigProto.Metric
    kTxPhysicalBytes: MadroxStatsConfigProto.Metric
    kTxPhysicalBytesMorphed: MadroxStatsConfigProto.Metric
    kTxMetadataActions: MadroxStatsConfigProto.Metric
    kTxWanLatencyUsecs: MadroxStatsConfigProto.Metric
    kRxLogicalBytes: MadroxStatsConfigProto.Metric
    kRxPhysicalBytes: MadroxStatsConfigProto.Metric
    kTxRPCRoundTripLatencyUsecs: MadroxStatsConfigProto.Metric
    kTxFileSyncLogicalBytes: MadroxStatsConfigProto.Metric
    kTxDirSyncNewViewChildren: MadroxStatsConfigProto.Metric
    class JobTargetNodeStatsSchema(_message.Message):
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
    class JobTargetStatsSchema(_message.Message):
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
    class JobStatsSchema(_message.Message):
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
    class NodeStatsSchema(_message.Message):
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
    class ReplicationJobStatsSchema(_message.Message):
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
    TIME_TO_LIVE_SECS_FIELD_NUMBER: _ClassVar[int]
    INTERNAL_STATS_TIME_TO_LIVE_SECS_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_ATTR_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_INCARNATION_ID_ATTR_FIELD_NUMBER: _ClassVar[int]
    time_to_live_secs: int
    internal_stats_time_to_live_secs: int
    cluster_id_attr: str
    cluster_incarnation_id_attr: str
    def __init__(self, time_to_live_secs: _Optional[int] = ..., internal_stats_time_to_live_secs: _Optional[int] = ..., cluster_id_attr: _Optional[str] = ..., cluster_incarnation_id_attr: _Optional[str] = ...) -> None: ...
