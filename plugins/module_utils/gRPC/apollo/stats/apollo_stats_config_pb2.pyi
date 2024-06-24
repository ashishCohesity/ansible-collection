from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ApolloStatsConfigProto(_message.Message):
    __slots__ = ("time_to_live_secs",)
    class DiskStats(_message.Message):
        __slots__ = ("schema_name", "schema_version", "id_attr", "descriptive_name", "help_text", "is_internal")
        class PerfMetric(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kNumBytesRead: _ClassVar[ApolloStatsConfigProto.DiskStats.PerfMetric]
            kNumBytesWritten: _ClassVar[ApolloStatsConfigProto.DiskStats.PerfMetric]
        kNumBytesRead: ApolloStatsConfigProto.DiskStats.PerfMetric
        kNumBytesWritten: ApolloStatsConfigProto.DiskStats.PerfMetric
        class UsageMetric(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kNumBytesUsed: _ClassVar[ApolloStatsConfigProto.DiskStats.UsageMetric]
            kNumChunkFilesOnBridge: _ClassVar[ApolloStatsConfigProto.DiskStats.UsageMetric]
        kNumBytesUsed: ApolloStatsConfigProto.DiskStats.UsageMetric
        kNumChunkFilesOnBridge: ApolloStatsConfigProto.DiskStats.UsageMetric
        SCHEMA_NAME_FIELD_NUMBER: _ClassVar[int]
        SCHEMA_VERSION_FIELD_NUMBER: _ClassVar[int]
        ID_ATTR_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTIVE_NAME_FIELD_NUMBER: _ClassVar[int]
        HELP_TEXT_FIELD_NUMBER: _ClassVar[int]
        IS_INTERNAL_FIELD_NUMBER: _ClassVar[int]
        schema_name: str
        schema_version: int
        id_attr: str
        descriptive_name: str
        help_text: str
        is_internal: bool
        def __init__(self, schema_name: _Optional[str] = ..., schema_version: _Optional[int] = ..., id_attr: _Optional[str] = ..., descriptive_name: _Optional[str] = ..., help_text: _Optional[str] = ..., is_internal: bool = ...) -> None: ...
    class MRDiskStats(_message.Message):
        __slots__ = ("schema_name", "schema_version", "id_attr", "descriptive_name", "help_text", "is_internal")
        class PerfMetric(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kMRNumBytesRead: _ClassVar[ApolloStatsConfigProto.MRDiskStats.PerfMetric]
            kMRNumBytesWritten: _ClassVar[ApolloStatsConfigProto.MRDiskStats.PerfMetric]
            kMRNumBytesDeleted: _ClassVar[ApolloStatsConfigProto.MRDiskStats.PerfMetric]
            kMRNumTrashSizeBytes: _ClassVar[ApolloStatsConfigProto.MRDiskStats.PerfMetric]
        kMRNumBytesRead: ApolloStatsConfigProto.MRDiskStats.PerfMetric
        kMRNumBytesWritten: ApolloStatsConfigProto.MRDiskStats.PerfMetric
        kMRNumBytesDeleted: ApolloStatsConfigProto.MRDiskStats.PerfMetric
        kMRNumTrashSizeBytes: ApolloStatsConfigProto.MRDiskStats.PerfMetric
        class UsageMetric(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kMRNumBytesUsed: _ClassVar[ApolloStatsConfigProto.MRDiskStats.UsageMetric]
        kMRNumBytesUsed: ApolloStatsConfigProto.MRDiskStats.UsageMetric
        SCHEMA_NAME_FIELD_NUMBER: _ClassVar[int]
        SCHEMA_VERSION_FIELD_NUMBER: _ClassVar[int]
        ID_ATTR_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTIVE_NAME_FIELD_NUMBER: _ClassVar[int]
        HELP_TEXT_FIELD_NUMBER: _ClassVar[int]
        IS_INTERNAL_FIELD_NUMBER: _ClassVar[int]
        schema_name: str
        schema_version: int
        id_attr: str
        descriptive_name: str
        help_text: str
        is_internal: bool
        def __init__(self, schema_name: _Optional[str] = ..., schema_version: _Optional[int] = ..., id_attr: _Optional[str] = ..., descriptive_name: _Optional[str] = ..., help_text: _Optional[str] = ..., is_internal: bool = ...) -> None: ...
    class MRAggregatedDiskStats(_message.Message):
        __slots__ = ("schema_name", "schema_version", "id_attr", "descriptive_name", "help_text", "is_internal")
        SCHEMA_NAME_FIELD_NUMBER: _ClassVar[int]
        SCHEMA_VERSION_FIELD_NUMBER: _ClassVar[int]
        ID_ATTR_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTIVE_NAME_FIELD_NUMBER: _ClassVar[int]
        HELP_TEXT_FIELD_NUMBER: _ClassVar[int]
        IS_INTERNAL_FIELD_NUMBER: _ClassVar[int]
        schema_name: str
        schema_version: int
        id_attr: str
        descriptive_name: str
        help_text: str
        is_internal: bool
        def __init__(self, schema_name: _Optional[str] = ..., schema_version: _Optional[int] = ..., id_attr: _Optional[str] = ..., descriptive_name: _Optional[str] = ..., help_text: _Optional[str] = ..., is_internal: bool = ...) -> None: ...
    class MRPipelineNodeStats(_message.Message):
        __slots__ = ("schema_name", "schema_version", "id_attr", "descriptive_name", "help_text", "is_internal")
        class PerfMetric(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kMRNumBytesRead: _ClassVar[ApolloStatsConfigProto.MRPipelineNodeStats.PerfMetric]
            kMRNumBytesWritten: _ClassVar[ApolloStatsConfigProto.MRPipelineNodeStats.PerfMetric]
            kMRPipelineReadIOPS: _ClassVar[ApolloStatsConfigProto.MRPipelineNodeStats.PerfMetric]
            kMRPipelineWriteIOPS: _ClassVar[ApolloStatsConfigProto.MRPipelineNodeStats.PerfMetric]
        kMRNumBytesRead: ApolloStatsConfigProto.MRPipelineNodeStats.PerfMetric
        kMRNumBytesWritten: ApolloStatsConfigProto.MRPipelineNodeStats.PerfMetric
        kMRPipelineReadIOPS: ApolloStatsConfigProto.MRPipelineNodeStats.PerfMetric
        kMRPipelineWriteIOPS: ApolloStatsConfigProto.MRPipelineNodeStats.PerfMetric
        SCHEMA_NAME_FIELD_NUMBER: _ClassVar[int]
        SCHEMA_VERSION_FIELD_NUMBER: _ClassVar[int]
        ID_ATTR_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTIVE_NAME_FIELD_NUMBER: _ClassVar[int]
        HELP_TEXT_FIELD_NUMBER: _ClassVar[int]
        IS_INTERNAL_FIELD_NUMBER: _ClassVar[int]
        schema_name: str
        schema_version: int
        id_attr: str
        descriptive_name: str
        help_text: str
        is_internal: bool
        def __init__(self, schema_name: _Optional[str] = ..., schema_version: _Optional[int] = ..., id_attr: _Optional[str] = ..., descriptive_name: _Optional[str] = ..., help_text: _Optional[str] = ..., is_internal: bool = ...) -> None: ...
    class MRPipelineDiskStats(_message.Message):
        __slots__ = ("schema_name", "schema_version", "id_attr", "descriptive_name", "help_text", "is_internal")
        SCHEMA_NAME_FIELD_NUMBER: _ClassVar[int]
        SCHEMA_VERSION_FIELD_NUMBER: _ClassVar[int]
        ID_ATTR_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTIVE_NAME_FIELD_NUMBER: _ClassVar[int]
        HELP_TEXT_FIELD_NUMBER: _ClassVar[int]
        IS_INTERNAL_FIELD_NUMBER: _ClassVar[int]
        schema_name: str
        schema_version: int
        id_attr: str
        descriptive_name: str
        help_text: str
        is_internal: bool
        def __init__(self, schema_name: _Optional[str] = ..., schema_version: _Optional[int] = ..., id_attr: _Optional[str] = ..., descriptive_name: _Optional[str] = ..., help_text: _Optional[str] = ..., is_internal: bool = ...) -> None: ...
    class MRFragmentDiskStats(_message.Message):
        __slots__ = ("schema_name", "schema_version", "id_attr", "descriptive_name", "help_text", "is_internal")
        class PerfMetric(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kMRNumBytesRead: _ClassVar[ApolloStatsConfigProto.MRFragmentDiskStats.PerfMetric]
            kMRNumBytesWritten: _ClassVar[ApolloStatsConfigProto.MRFragmentDiskStats.PerfMetric]
            kMRFragmentReadIOPS: _ClassVar[ApolloStatsConfigProto.MRFragmentDiskStats.PerfMetric]
            kMRFragmentWriteIOPS: _ClassVar[ApolloStatsConfigProto.MRFragmentDiskStats.PerfMetric]
        kMRNumBytesRead: ApolloStatsConfigProto.MRFragmentDiskStats.PerfMetric
        kMRNumBytesWritten: ApolloStatsConfigProto.MRFragmentDiskStats.PerfMetric
        kMRFragmentReadIOPS: ApolloStatsConfigProto.MRFragmentDiskStats.PerfMetric
        kMRFragmentWriteIOPS: ApolloStatsConfigProto.MRFragmentDiskStats.PerfMetric
        SCHEMA_NAME_FIELD_NUMBER: _ClassVar[int]
        SCHEMA_VERSION_FIELD_NUMBER: _ClassVar[int]
        ID_ATTR_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTIVE_NAME_FIELD_NUMBER: _ClassVar[int]
        HELP_TEXT_FIELD_NUMBER: _ClassVar[int]
        IS_INTERNAL_FIELD_NUMBER: _ClassVar[int]
        schema_name: str
        schema_version: int
        id_attr: str
        descriptive_name: str
        help_text: str
        is_internal: bool
        def __init__(self, schema_name: _Optional[str] = ..., schema_version: _Optional[int] = ..., id_attr: _Optional[str] = ..., descriptive_name: _Optional[str] = ..., help_text: _Optional[str] = ..., is_internal: bool = ...) -> None: ...
    class ScribeStats(_message.Message):
        __slots__ = ("schema_name", "schema_version", "id_attr", "descriptive_name", "help_text", "is_internal")
        class PerfMetric(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kNumRowsRead: _ClassVar[ApolloStatsConfigProto.ScribeStats.PerfMetric]
            kNumBytesRead: _ClassVar[ApolloStatsConfigProto.ScribeStats.PerfMetric]
            kNumRowsDeleted: _ClassVar[ApolloStatsConfigProto.ScribeStats.PerfMetric]
            kNumTablesScanned: _ClassVar[ApolloStatsConfigProto.ScribeStats.PerfMetric]
            kNumBucketsScanned: _ClassVar[ApolloStatsConfigProto.ScribeStats.PerfMetric]
        kNumRowsRead: ApolloStatsConfigProto.ScribeStats.PerfMetric
        kNumBytesRead: ApolloStatsConfigProto.ScribeStats.PerfMetric
        kNumRowsDeleted: ApolloStatsConfigProto.ScribeStats.PerfMetric
        kNumTablesScanned: ApolloStatsConfigProto.ScribeStats.PerfMetric
        kNumBucketsScanned: ApolloStatsConfigProto.ScribeStats.PerfMetric
        class UsageMetric(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kNumRowsSeen: _ClassVar[ApolloStatsConfigProto.ScribeStats.UsageMetric]
            kNumBytesSeen: _ClassVar[ApolloStatsConfigProto.ScribeStats.UsageMetric]
        kNumRowsSeen: ApolloStatsConfigProto.ScribeStats.UsageMetric
        kNumBytesSeen: ApolloStatsConfigProto.ScribeStats.UsageMetric
        SCHEMA_NAME_FIELD_NUMBER: _ClassVar[int]
        SCHEMA_VERSION_FIELD_NUMBER: _ClassVar[int]
        ID_ATTR_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTIVE_NAME_FIELD_NUMBER: _ClassVar[int]
        HELP_TEXT_FIELD_NUMBER: _ClassVar[int]
        IS_INTERNAL_FIELD_NUMBER: _ClassVar[int]
        schema_name: str
        schema_version: int
        id_attr: str
        descriptive_name: str
        help_text: str
        is_internal: bool
        def __init__(self, schema_name: _Optional[str] = ..., schema_version: _Optional[int] = ..., id_attr: _Optional[str] = ..., descriptive_name: _Optional[str] = ..., help_text: _Optional[str] = ..., is_internal: bool = ...) -> None: ...
    class AlgorithmStats(_message.Message):
        __slots__ = ("schema_name", "schema_version", "id_attr", "descriptive_name", "help_text", "is_internal", "default_entity_id")
        class PerfMetric(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kNumViewSnaptreeNodesDeleted: _ClassVar[ApolloStatsConfigProto.AlgorithmStats.PerfMetric]
            kNumBlobSnaptreeNodesDeleted: _ClassVar[ApolloStatsConfigProto.AlgorithmStats.PerfMetric]
            kNumBricksDeduped: _ClassVar[ApolloStatsConfigProto.AlgorithmStats.PerfMetric]
            kNumBricksDeleted: _ClassVar[ApolloStatsConfigProto.AlgorithmStats.PerfMetric]
            kNumChunksDeleted: _ClassVar[ApolloStatsConfigProto.AlgorithmStats.PerfMetric]
            kNumChunkFilesFixed: _ClassVar[ApolloStatsConfigProto.AlgorithmStats.PerfMetric]
            kNumChunkFilesDowntiered: _ClassVar[ApolloStatsConfigProto.AlgorithmStats.PerfMetric]
            kNumChunkFilesShuffled: _ClassVar[ApolloStatsConfigProto.AlgorithmStats.PerfMetric]
            kNumChunkFilesCompressed: _ClassVar[ApolloStatsConfigProto.AlgorithmStats.PerfMetric]
            kNumChunkFilesDefragged: _ClassVar[ApolloStatsConfigProto.AlgorithmStats.PerfMetric]
            kNumInodeIntentsFixed: _ClassVar[ApolloStatsConfigProto.AlgorithmStats.PerfMetric]
            kNumInodePhysSizeAdjusted: _ClassVar[ApolloStatsConfigProto.AlgorithmStats.PerfMetric]
            kNumViewMappingsFixed: _ClassVar[ApolloStatsConfigProto.AlgorithmStats.PerfMetric]
            kNumViewsDeleted: _ClassVar[ApolloStatsConfigProto.AlgorithmStats.PerfMetric]
            kNumViewBoxesDeleted: _ClassVar[ApolloStatsConfigProto.AlgorithmStats.PerfMetric]
            kNumNodeDeletedFromPartition: _ClassVar[ApolloStatsConfigProto.AlgorithmStats.PerfMetric]
            kNumNodeDeletedFromCluster: _ClassVar[ApolloStatsConfigProto.AlgorithmStats.PerfMetric]
            kNumDisksDeletedFromPartition: _ClassVar[ApolloStatsConfigProto.AlgorithmStats.PerfMetric]
            kNumDisksDeletedFromCluster: _ClassVar[ApolloStatsConfigProto.AlgorithmStats.PerfMetric]
            kNumClusterPartitionsDeleted: _ClassVar[ApolloStatsConfigProto.AlgorithmStats.PerfMetric]
            kNumLogicalUsageReported: _ClassVar[ApolloStatsConfigProto.AlgorithmStats.PerfMetric]
            kNumStatsEntitiesDeleted: _ClassVar[ApolloStatsConfigProto.AlgorithmStats.PerfMetric]
            kNumScribeRowsDeleted: _ClassVar[ApolloStatsConfigProto.AlgorithmStats.PerfMetric]
            kNumBridgeConstituentsDeletedFromOpclock: _ClassVar[ApolloStatsConfigProto.AlgorithmStats.PerfMetric]
            kNumExpiredSmbSessionsDeleted: _ClassVar[ApolloStatsConfigProto.AlgorithmStats.PerfMetric]
            kNumChunkFilesCloudSpilled: _ClassVar[ApolloStatsConfigProto.AlgorithmStats.PerfMetric]
            kNumViewBoxScribePhysicalUsageReported: _ClassVar[ApolloStatsConfigProto.AlgorithmStats.PerfMetric]
            kNumSmallFileBytesDeleted: _ClassVar[ApolloStatsConfigProto.AlgorithmStats.PerfMetric]
            kNumReferenceArchiveRetired: _ClassVar[ApolloStatsConfigProto.AlgorithmStats.PerfMetric]
            kNumChunkLocationEntriesFixed: _ClassVar[ApolloStatsConfigProto.AlgorithmStats.PerfMetric]
            kNumChunkLocationEntriesCleaned: _ClassVar[ApolloStatsConfigProto.AlgorithmStats.PerfMetric]
            kNumSnaptreeNodeLocationEntriesCleaned: _ClassVar[ApolloStatsConfigProto.AlgorithmStats.PerfMetric]
            kNumRestoredSnaptreeNodeLocationEntriesCleaned: _ClassVar[ApolloStatsConfigProto.AlgorithmStats.PerfMetric]
            kNumBrickUsageReported: _ClassVar[ApolloStatsConfigProto.AlgorithmStats.PerfMetric]
            kNumViewUsageFixed: _ClassVar[ApolloStatsConfigProto.AlgorithmStats.PerfMetric]
            kNumS3InodeIntentsFixed: _ClassVar[ApolloStatsConfigProto.AlgorithmStats.PerfMetric]
            kNumChunkFilesEncrypted: _ClassVar[ApolloStatsConfigProto.AlgorithmStats.PerfMetric]
            kNumChunkFilesErasureCoded: _ClassVar[ApolloStatsConfigProto.AlgorithmStats.PerfMetric]
            kNumUserUsageFixed: _ClassVar[ApolloStatsConfigProto.AlgorithmStats.PerfMetric]
            kNumUserUsageDeleted: _ClassVar[ApolloStatsConfigProto.AlgorithmStats.PerfMetric]
            kNumScribeRowsInserted: _ClassVar[ApolloStatsConfigProto.AlgorithmStats.PerfMetric]
            kNumMegachunkCreated: _ClassVar[ApolloStatsConfigProto.AlgorithmStats.PerfMetric]
            kNumExtentsDedupped: _ClassVar[ApolloStatsConfigProto.AlgorithmStats.PerfMetric]
            kNumDeleteScribeRangeIssued: _ClassVar[ApolloStatsConfigProto.AlgorithmStats.PerfMetric]
        kNumViewSnaptreeNodesDeleted: ApolloStatsConfigProto.AlgorithmStats.PerfMetric
        kNumBlobSnaptreeNodesDeleted: ApolloStatsConfigProto.AlgorithmStats.PerfMetric
        kNumBricksDeduped: ApolloStatsConfigProto.AlgorithmStats.PerfMetric
        kNumBricksDeleted: ApolloStatsConfigProto.AlgorithmStats.PerfMetric
        kNumChunksDeleted: ApolloStatsConfigProto.AlgorithmStats.PerfMetric
        kNumChunkFilesFixed: ApolloStatsConfigProto.AlgorithmStats.PerfMetric
        kNumChunkFilesDowntiered: ApolloStatsConfigProto.AlgorithmStats.PerfMetric
        kNumChunkFilesShuffled: ApolloStatsConfigProto.AlgorithmStats.PerfMetric
        kNumChunkFilesCompressed: ApolloStatsConfigProto.AlgorithmStats.PerfMetric
        kNumChunkFilesDefragged: ApolloStatsConfigProto.AlgorithmStats.PerfMetric
        kNumInodeIntentsFixed: ApolloStatsConfigProto.AlgorithmStats.PerfMetric
        kNumInodePhysSizeAdjusted: ApolloStatsConfigProto.AlgorithmStats.PerfMetric
        kNumViewMappingsFixed: ApolloStatsConfigProto.AlgorithmStats.PerfMetric
        kNumViewsDeleted: ApolloStatsConfigProto.AlgorithmStats.PerfMetric
        kNumViewBoxesDeleted: ApolloStatsConfigProto.AlgorithmStats.PerfMetric
        kNumNodeDeletedFromPartition: ApolloStatsConfigProto.AlgorithmStats.PerfMetric
        kNumNodeDeletedFromCluster: ApolloStatsConfigProto.AlgorithmStats.PerfMetric
        kNumDisksDeletedFromPartition: ApolloStatsConfigProto.AlgorithmStats.PerfMetric
        kNumDisksDeletedFromCluster: ApolloStatsConfigProto.AlgorithmStats.PerfMetric
        kNumClusterPartitionsDeleted: ApolloStatsConfigProto.AlgorithmStats.PerfMetric
        kNumLogicalUsageReported: ApolloStatsConfigProto.AlgorithmStats.PerfMetric
        kNumStatsEntitiesDeleted: ApolloStatsConfigProto.AlgorithmStats.PerfMetric
        kNumScribeRowsDeleted: ApolloStatsConfigProto.AlgorithmStats.PerfMetric
        kNumBridgeConstituentsDeletedFromOpclock: ApolloStatsConfigProto.AlgorithmStats.PerfMetric
        kNumExpiredSmbSessionsDeleted: ApolloStatsConfigProto.AlgorithmStats.PerfMetric
        kNumChunkFilesCloudSpilled: ApolloStatsConfigProto.AlgorithmStats.PerfMetric
        kNumViewBoxScribePhysicalUsageReported: ApolloStatsConfigProto.AlgorithmStats.PerfMetric
        kNumSmallFileBytesDeleted: ApolloStatsConfigProto.AlgorithmStats.PerfMetric
        kNumReferenceArchiveRetired: ApolloStatsConfigProto.AlgorithmStats.PerfMetric
        kNumChunkLocationEntriesFixed: ApolloStatsConfigProto.AlgorithmStats.PerfMetric
        kNumChunkLocationEntriesCleaned: ApolloStatsConfigProto.AlgorithmStats.PerfMetric
        kNumSnaptreeNodeLocationEntriesCleaned: ApolloStatsConfigProto.AlgorithmStats.PerfMetric
        kNumRestoredSnaptreeNodeLocationEntriesCleaned: ApolloStatsConfigProto.AlgorithmStats.PerfMetric
        kNumBrickUsageReported: ApolloStatsConfigProto.AlgorithmStats.PerfMetric
        kNumViewUsageFixed: ApolloStatsConfigProto.AlgorithmStats.PerfMetric
        kNumS3InodeIntentsFixed: ApolloStatsConfigProto.AlgorithmStats.PerfMetric
        kNumChunkFilesEncrypted: ApolloStatsConfigProto.AlgorithmStats.PerfMetric
        kNumChunkFilesErasureCoded: ApolloStatsConfigProto.AlgorithmStats.PerfMetric
        kNumUserUsageFixed: ApolloStatsConfigProto.AlgorithmStats.PerfMetric
        kNumUserUsageDeleted: ApolloStatsConfigProto.AlgorithmStats.PerfMetric
        kNumScribeRowsInserted: ApolloStatsConfigProto.AlgorithmStats.PerfMetric
        kNumMegachunkCreated: ApolloStatsConfigProto.AlgorithmStats.PerfMetric
        kNumExtentsDedupped: ApolloStatsConfigProto.AlgorithmStats.PerfMetric
        kNumDeleteScribeRangeIssued: ApolloStatsConfigProto.AlgorithmStats.PerfMetric
        SCHEMA_NAME_FIELD_NUMBER: _ClassVar[int]
        SCHEMA_VERSION_FIELD_NUMBER: _ClassVar[int]
        ID_ATTR_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTIVE_NAME_FIELD_NUMBER: _ClassVar[int]
        HELP_TEXT_FIELD_NUMBER: _ClassVar[int]
        IS_INTERNAL_FIELD_NUMBER: _ClassVar[int]
        DEFAULT_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
        schema_name: str
        schema_version: int
        id_attr: str
        descriptive_name: str
        help_text: str
        is_internal: bool
        default_entity_id: str
        def __init__(self, schema_name: _Optional[str] = ..., schema_version: _Optional[int] = ..., id_attr: _Optional[str] = ..., descriptive_name: _Optional[str] = ..., help_text: _Optional[str] = ..., is_internal: bool = ..., default_entity_id: _Optional[str] = ...) -> None: ...
    class ChunkFileStats(_message.Message):
        __slots__ = ("schema_name", "schema_version", "id_attr", "descriptive_name", "help_text", "is_internal")
        class UsageMetric(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kNumChunkFiles: _ClassVar[ApolloStatsConfigProto.ChunkFileStats.UsageMetric]
            kNumChunkFilesUnderReplicated: _ClassVar[ApolloStatsConfigProto.ChunkFileStats.UsageMetric]
            kNumChunkFilesOverReplicated: _ClassVar[ApolloStatsConfigProto.ChunkFileStats.UsageMetric]
            kNumChunkFilesReplicaUnreconciled: _ClassVar[ApolloStatsConfigProto.ChunkFileStats.UsageMetric]
            kNumChunkFilesNodeLevelReplicated: _ClassVar[ApolloStatsConfigProto.ChunkFileStats.UsageMetric]
            kNumChunkFilesChassisLevelReplicated: _ClassVar[ApolloStatsConfigProto.ChunkFileStats.UsageMetric]
            kNumChunkFilesRackLevelReplicated: _ClassVar[ApolloStatsConfigProto.ChunkFileStats.UsageMetric]
            kNumChunkFilesEncrypted: _ClassVar[ApolloStatsConfigProto.ChunkFileStats.UsageMetric]
            kNumChunkFilesCompressed: _ClassVar[ApolloStatsConfigProto.ChunkFileStats.UsageMetric]
            kNumChunkFilesCloud: _ClassVar[ApolloStatsConfigProto.ChunkFileStats.UsageMetric]
            kNumChunkFilesCloudEncrypted: _ClassVar[ApolloStatsConfigProto.ChunkFileStats.UsageMetric]
            kNumChunkFilesCloudCompressed: _ClassVar[ApolloStatsConfigProto.ChunkFileStats.UsageMetric]
            kNumChunkFilesWithoutAccessTime: _ClassVar[ApolloStatsConfigProto.ChunkFileStats.UsageMetric]
            kNumChunkFilesCloudWithoutAccessTime: _ClassVar[ApolloStatsConfigProto.ChunkFileStats.UsageMetric]
            kNumChunkFilesErasureCoded_2_1: _ClassVar[ApolloStatsConfigProto.ChunkFileStats.UsageMetric]
            kNumChunkFilesErasureCoded_2_2: _ClassVar[ApolloStatsConfigProto.ChunkFileStats.UsageMetric]
            kNumChunkFilesErasureCoded_3_1: _ClassVar[ApolloStatsConfigProto.ChunkFileStats.UsageMetric]
            kNumChunkFilesErasureCoded_3_2: _ClassVar[ApolloStatsConfigProto.ChunkFileStats.UsageMetric]
            kNumChunkFilesErasureCoded_4_1: _ClassVar[ApolloStatsConfigProto.ChunkFileStats.UsageMetric]
            kNumChunkFilesErasureCoded_4_2: _ClassVar[ApolloStatsConfigProto.ChunkFileStats.UsageMetric]
            kNumChunkFilesErasureCoded_5_1: _ClassVar[ApolloStatsConfigProto.ChunkFileStats.UsageMetric]
            kNumChunkFilesErasureCoded_5_2: _ClassVar[ApolloStatsConfigProto.ChunkFileStats.UsageMetric]
            kNumChunkFilesErasureCoded_N_K: _ClassVar[ApolloStatsConfigProto.ChunkFileStats.UsageMetric]
            kNumChunkFilesNDD: _ClassVar[ApolloStatsConfigProto.ChunkFileStats.UsageMetric]
            kNumChunkFiles_RF_N: _ClassVar[ApolloStatsConfigProto.ChunkFileStats.UsageMetric]
            kNumChunkFiles_RF_1: _ClassVar[ApolloStatsConfigProto.ChunkFileStats.UsageMetric]
            kNumChunkFiles_RF_2: _ClassVar[ApolloStatsConfigProto.ChunkFileStats.UsageMetric]
            kNumChunkFiles_RF_3: _ClassVar[ApolloStatsConfigProto.ChunkFileStats.UsageMetric]
            kNumChunkFiles_Lost: _ClassVar[ApolloStatsConfigProto.ChunkFileStats.UsageMetric]
            kNumChunkFiles_FT_0: _ClassVar[ApolloStatsConfigProto.ChunkFileStats.UsageMetric]
            kNumChunkFiles_FT_1: _ClassVar[ApolloStatsConfigProto.ChunkFileStats.UsageMetric]
            kNumChunkFiles_FT_N: _ClassVar[ApolloStatsConfigProto.ChunkFileStats.UsageMetric]
        kNumChunkFiles: ApolloStatsConfigProto.ChunkFileStats.UsageMetric
        kNumChunkFilesUnderReplicated: ApolloStatsConfigProto.ChunkFileStats.UsageMetric
        kNumChunkFilesOverReplicated: ApolloStatsConfigProto.ChunkFileStats.UsageMetric
        kNumChunkFilesReplicaUnreconciled: ApolloStatsConfigProto.ChunkFileStats.UsageMetric
        kNumChunkFilesNodeLevelReplicated: ApolloStatsConfigProto.ChunkFileStats.UsageMetric
        kNumChunkFilesChassisLevelReplicated: ApolloStatsConfigProto.ChunkFileStats.UsageMetric
        kNumChunkFilesRackLevelReplicated: ApolloStatsConfigProto.ChunkFileStats.UsageMetric
        kNumChunkFilesEncrypted: ApolloStatsConfigProto.ChunkFileStats.UsageMetric
        kNumChunkFilesCompressed: ApolloStatsConfigProto.ChunkFileStats.UsageMetric
        kNumChunkFilesCloud: ApolloStatsConfigProto.ChunkFileStats.UsageMetric
        kNumChunkFilesCloudEncrypted: ApolloStatsConfigProto.ChunkFileStats.UsageMetric
        kNumChunkFilesCloudCompressed: ApolloStatsConfigProto.ChunkFileStats.UsageMetric
        kNumChunkFilesWithoutAccessTime: ApolloStatsConfigProto.ChunkFileStats.UsageMetric
        kNumChunkFilesCloudWithoutAccessTime: ApolloStatsConfigProto.ChunkFileStats.UsageMetric
        kNumChunkFilesErasureCoded_2_1: ApolloStatsConfigProto.ChunkFileStats.UsageMetric
        kNumChunkFilesErasureCoded_2_2: ApolloStatsConfigProto.ChunkFileStats.UsageMetric
        kNumChunkFilesErasureCoded_3_1: ApolloStatsConfigProto.ChunkFileStats.UsageMetric
        kNumChunkFilesErasureCoded_3_2: ApolloStatsConfigProto.ChunkFileStats.UsageMetric
        kNumChunkFilesErasureCoded_4_1: ApolloStatsConfigProto.ChunkFileStats.UsageMetric
        kNumChunkFilesErasureCoded_4_2: ApolloStatsConfigProto.ChunkFileStats.UsageMetric
        kNumChunkFilesErasureCoded_5_1: ApolloStatsConfigProto.ChunkFileStats.UsageMetric
        kNumChunkFilesErasureCoded_5_2: ApolloStatsConfigProto.ChunkFileStats.UsageMetric
        kNumChunkFilesErasureCoded_N_K: ApolloStatsConfigProto.ChunkFileStats.UsageMetric
        kNumChunkFilesNDD: ApolloStatsConfigProto.ChunkFileStats.UsageMetric
        kNumChunkFiles_RF_N: ApolloStatsConfigProto.ChunkFileStats.UsageMetric
        kNumChunkFiles_RF_1: ApolloStatsConfigProto.ChunkFileStats.UsageMetric
        kNumChunkFiles_RF_2: ApolloStatsConfigProto.ChunkFileStats.UsageMetric
        kNumChunkFiles_RF_3: ApolloStatsConfigProto.ChunkFileStats.UsageMetric
        kNumChunkFiles_Lost: ApolloStatsConfigProto.ChunkFileStats.UsageMetric
        kNumChunkFiles_FT_0: ApolloStatsConfigProto.ChunkFileStats.UsageMetric
        kNumChunkFiles_FT_1: ApolloStatsConfigProto.ChunkFileStats.UsageMetric
        kNumChunkFiles_FT_N: ApolloStatsConfigProto.ChunkFileStats.UsageMetric
        SCHEMA_NAME_FIELD_NUMBER: _ClassVar[int]
        SCHEMA_VERSION_FIELD_NUMBER: _ClassVar[int]
        ID_ATTR_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTIVE_NAME_FIELD_NUMBER: _ClassVar[int]
        HELP_TEXT_FIELD_NUMBER: _ClassVar[int]
        IS_INTERNAL_FIELD_NUMBER: _ClassVar[int]
        schema_name: str
        schema_version: int
        id_attr: str
        descriptive_name: str
        help_text: str
        is_internal: bool
        def __init__(self, schema_name: _Optional[str] = ..., schema_version: _Optional[int] = ..., id_attr: _Optional[str] = ..., descriptive_name: _Optional[str] = ..., help_text: _Optional[str] = ..., is_internal: bool = ...) -> None: ...
    class NodeLevelStats(_message.Message):
        __slots__ = ("schema_name", "schema_version", "id_attr", "descriptive_name", "help_text", "is_internal")
        SCHEMA_NAME_FIELD_NUMBER: _ClassVar[int]
        SCHEMA_VERSION_FIELD_NUMBER: _ClassVar[int]
        ID_ATTR_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTIVE_NAME_FIELD_NUMBER: _ClassVar[int]
        HELP_TEXT_FIELD_NUMBER: _ClassVar[int]
        IS_INTERNAL_FIELD_NUMBER: _ClassVar[int]
        schema_name: str
        schema_version: int
        id_attr: str
        descriptive_name: str
        help_text: str
        is_internal: bool
        def __init__(self, schema_name: _Optional[str] = ..., schema_version: _Optional[int] = ..., id_attr: _Optional[str] = ..., descriptive_name: _Optional[str] = ..., help_text: _Optional[str] = ..., is_internal: bool = ...) -> None: ...
    class ClusterStats(_message.Message):
        __slots__ = ("schema_name", "schema_version", "id_attr", "descriptive_name", "help_text", "is_internal")
        SCHEMA_NAME_FIELD_NUMBER: _ClassVar[int]
        SCHEMA_VERSION_FIELD_NUMBER: _ClassVar[int]
        ID_ATTR_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTIVE_NAME_FIELD_NUMBER: _ClassVar[int]
        HELP_TEXT_FIELD_NUMBER: _ClassVar[int]
        IS_INTERNAL_FIELD_NUMBER: _ClassVar[int]
        schema_name: str
        schema_version: int
        id_attr: str
        descriptive_name: str
        help_text: str
        is_internal: bool
        def __init__(self, schema_name: _Optional[str] = ..., schema_version: _Optional[int] = ..., id_attr: _Optional[str] = ..., descriptive_name: _Optional[str] = ..., help_text: _Optional[str] = ..., is_internal: bool = ...) -> None: ...
    TIME_TO_LIVE_SECS_FIELD_NUMBER: _ClassVar[int]
    time_to_live_secs: int
    def __init__(self, time_to_live_secs: _Optional[int] = ...) -> None: ...

class ApolloInternalStatsProto(_message.Message):
    __slots__ = ()
    class JobStats(_message.Message):
        __slots__ = ()
        class UsageMetric(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kNumNodesRunning: _ClassVar[ApolloInternalStatsProto.JobStats.UsageMetric]
            kNumTasksRunning: _ClassVar[ApolloInternalStatsProto.JobStats.UsageMetric]
            kNumAlgosRunning: _ClassVar[ApolloInternalStatsProto.JobStats.UsageMetric]
            kJobStartTimeMSec: _ClassVar[ApolloInternalStatsProto.JobStats.UsageMetric]
            kJobEndTimeMSec: _ClassVar[ApolloInternalStatsProto.JobStats.UsageMetric]
        kNumNodesRunning: ApolloInternalStatsProto.JobStats.UsageMetric
        kNumTasksRunning: ApolloInternalStatsProto.JobStats.UsageMetric
        kNumAlgosRunning: ApolloInternalStatsProto.JobStats.UsageMetric
        kJobStartTimeMSec: ApolloInternalStatsProto.JobStats.UsageMetric
        kJobEndTimeMSec: ApolloInternalStatsProto.JobStats.UsageMetric
        def __init__(self) -> None: ...
    class MiscStats(_message.Message):
        __slots__ = ()
        class PerfMetric(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kNumTaskFailures: _ClassVar[ApolloInternalStatsProto.MiscStats.PerfMetric]
            kNumNodeFailures: _ClassVar[ApolloInternalStatsProto.MiscStats.PerfMetric]
            kNumJobFailures: _ClassVar[ApolloInternalStatsProto.MiscStats.PerfMetric]
        kNumTaskFailures: ApolloInternalStatsProto.MiscStats.PerfMetric
        kNumNodeFailures: ApolloInternalStatsProto.MiscStats.PerfMetric
        kNumJobFailures: ApolloInternalStatsProto.MiscStats.PerfMetric
        def __init__(self) -> None: ...
    class ActionStats(_message.Message):
        __slots__ = ()
        class PerfMetric(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kNumActionsRaised: _ClassVar[ApolloInternalStatsProto.ActionStats.PerfMetric]
            kNumActionsFromBridgeRaised: _ClassVar[ApolloInternalStatsProto.ActionStats.PerfMetric]
            kNumActionsExecuted: _ClassVar[ApolloInternalStatsProto.ActionStats.PerfMetric]
            kNumActionsRerouted: _ClassVar[ApolloInternalStatsProto.ActionStats.PerfMetric]
            kNumActionsDropped: _ClassVar[ApolloInternalStatsProto.ActionStats.PerfMetric]
            kNumActionsRejected: _ClassVar[ApolloInternalStatsProto.ActionStats.PerfMetric]
            kNumActionsRetried: _ClassVar[ApolloInternalStatsProto.ActionStats.PerfMetric]
        kNumActionsRaised: ApolloInternalStatsProto.ActionStats.PerfMetric
        kNumActionsFromBridgeRaised: ApolloInternalStatsProto.ActionStats.PerfMetric
        kNumActionsExecuted: ApolloInternalStatsProto.ActionStats.PerfMetric
        kNumActionsRerouted: ApolloInternalStatsProto.ActionStats.PerfMetric
        kNumActionsDropped: ApolloInternalStatsProto.ActionStats.PerfMetric
        kNumActionsRejected: ApolloInternalStatsProto.ActionStats.PerfMetric
        kNumActionsRetried: ApolloInternalStatsProto.ActionStats.PerfMetric
        def __init__(self) -> None: ...
    class MinionBlobStats(_message.Message):
        __slots__ = ()
        class UsageMetric(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kNumBytesUsed: _ClassVar[ApolloInternalStatsProto.MinionBlobStats.UsageMetric]
            kNumBytesUnreferenced: _ClassVar[ApolloInternalStatsProto.MinionBlobStats.UsageMetric]
            kMaxReservedByteOffset: _ClassVar[ApolloInternalStatsProto.MinionBlobStats.UsageMetric]
        kNumBytesUsed: ApolloInternalStatsProto.MinionBlobStats.UsageMetric
        kNumBytesUnreferenced: ApolloInternalStatsProto.MinionBlobStats.UsageMetric
        kMaxReservedByteOffset: ApolloInternalStatsProto.MinionBlobStats.UsageMetric
        def __init__(self) -> None: ...
    class IceboxArchiveStats(_message.Message):
        __slots__ = ()
        class UsageMetric(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kRetired: _ClassVar[ApolloInternalStatsProto.IceboxArchiveStats.UsageMetric]
            kPercentageReferenced: _ClassVar[ApolloInternalStatsProto.IceboxArchiveStats.UsageMetric]
            kNumChunksAlive: _ClassVar[ApolloInternalStatsProto.IceboxArchiveStats.UsageMetric]
            kTotalChunks: _ClassVar[ApolloInternalStatsProto.IceboxArchiveStats.UsageMetric]
        kRetired: ApolloInternalStatsProto.IceboxArchiveStats.UsageMetric
        kPercentageReferenced: ApolloInternalStatsProto.IceboxArchiveStats.UsageMetric
        kNumChunksAlive: ApolloInternalStatsProto.IceboxArchiveStats.UsageMetric
        kTotalChunks: ApolloInternalStatsProto.IceboxArchiveStats.UsageMetric
        def __init__(self) -> None: ...
    def __init__(self) -> None: ...
