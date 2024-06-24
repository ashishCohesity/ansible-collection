from librarian.base import schema_pb2 as _schema_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class URIs(_message.Message):
    __slots__ = ("create_index_uri", "add_documents_uri", "get_documents_uri", "health_check_uri", "update_config_uri", "delete_index_uri", "delete_documents_uri", "update_index_uri", "get_stats_uri", "commit_changes_uri", "set_gflags_uri")
    CREATE_INDEX_URI_FIELD_NUMBER: _ClassVar[int]
    ADD_DOCUMENTS_URI_FIELD_NUMBER: _ClassVar[int]
    GET_DOCUMENTS_URI_FIELD_NUMBER: _ClassVar[int]
    HEALTH_CHECK_URI_FIELD_NUMBER: _ClassVar[int]
    UPDATE_CONFIG_URI_FIELD_NUMBER: _ClassVar[int]
    DELETE_INDEX_URI_FIELD_NUMBER: _ClassVar[int]
    DELETE_DOCUMENTS_URI_FIELD_NUMBER: _ClassVar[int]
    UPDATE_INDEX_URI_FIELD_NUMBER: _ClassVar[int]
    GET_STATS_URI_FIELD_NUMBER: _ClassVar[int]
    COMMIT_CHANGES_URI_FIELD_NUMBER: _ClassVar[int]
    SET_GFLAGS_URI_FIELD_NUMBER: _ClassVar[int]
    create_index_uri: str
    add_documents_uri: str
    get_documents_uri: str
    health_check_uri: str
    update_config_uri: str
    delete_index_uri: str
    delete_documents_uri: str
    update_index_uri: str
    get_stats_uri: str
    commit_changes_uri: str
    set_gflags_uri: str
    def __init__(self, create_index_uri: _Optional[str] = ..., add_documents_uri: _Optional[str] = ..., get_documents_uri: _Optional[str] = ..., health_check_uri: _Optional[str] = ..., update_config_uri: _Optional[str] = ..., delete_index_uri: _Optional[str] = ..., delete_documents_uri: _Optional[str] = ..., update_index_uri: _Optional[str] = ..., get_stats_uri: _Optional[str] = ..., commit_changes_uri: _Optional[str] = ..., set_gflags_uri: _Optional[str] = ...) -> None: ...

class HealthCheckResult(_message.Message):
    __slots__ = ("status",)
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNotReachable: _ClassVar[HealthCheckResult.Status]
        kConfigNotUpdated: _ClassVar[HealthCheckResult.Status]
        kReady: _ClassVar[HealthCheckResult.Status]
    kNotReachable: HealthCheckResult.Status
    kConfigNotUpdated: HealthCheckResult.Status
    kReady: HealthCheckResult.Status
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: HealthCheckResult.Status
    def __init__(self, status: _Optional[_Union[HealthCheckResult.Status, str]] = ...) -> None: ...

class UpdateConfigArg(_message.Message):
    __slots__ = ("indices_vec",)
    class BucketInfo(_message.Message):
        __slots__ = ("bucket_id", "data_directory_path", "remove_bucket", "disk_id")
        BUCKET_ID_FIELD_NUMBER: _ClassVar[int]
        DATA_DIRECTORY_PATH_FIELD_NUMBER: _ClassVar[int]
        REMOVE_BUCKET_FIELD_NUMBER: _ClassVar[int]
        DISK_ID_FIELD_NUMBER: _ClassVar[int]
        bucket_id: int
        data_directory_path: str
        remove_bucket: bool
        disk_id: int
        def __init__(self, bucket_id: _Optional[int] = ..., data_directory_path: _Optional[str] = ..., remove_bucket: bool = ..., disk_id: _Optional[int] = ...) -> None: ...
    class IndexInfo(_message.Message):
        __slots__ = ("name", "bucket_vec", "field_properties", "for_replication", "field_ids_fqn")
        class FieldPropertiesEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: _schema_pb2.IndexSchema.FieldMapping
            def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_schema_pb2.IndexSchema.FieldMapping, _Mapping]] = ...) -> None: ...
        class FieldIdsFqnEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: int
            value: str
            def __init__(self, key: _Optional[int] = ..., value: _Optional[str] = ...) -> None: ...
        NAME_FIELD_NUMBER: _ClassVar[int]
        BUCKET_VEC_FIELD_NUMBER: _ClassVar[int]
        FIELD_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
        FOR_REPLICATION_FIELD_NUMBER: _ClassVar[int]
        FIELD_IDS_FQN_FIELD_NUMBER: _ClassVar[int]
        name: str
        bucket_vec: _containers.RepeatedCompositeFieldContainer[UpdateConfigArg.BucketInfo]
        field_properties: _containers.MessageMap[str, _schema_pb2.IndexSchema.FieldMapping]
        for_replication: bool
        field_ids_fqn: _containers.ScalarMap[int, str]
        def __init__(self, name: _Optional[str] = ..., bucket_vec: _Optional[_Iterable[_Union[UpdateConfigArg.BucketInfo, _Mapping]]] = ..., field_properties: _Optional[_Mapping[str, _schema_pb2.IndexSchema.FieldMapping]] = ..., for_replication: bool = ..., field_ids_fqn: _Optional[_Mapping[int, str]] = ...) -> None: ...
    INDICES_VEC_FIELD_NUMBER: _ClassVar[int]
    indices_vec: _containers.RepeatedCompositeFieldContainer[UpdateConfigArg.IndexInfo]
    def __init__(self, indices_vec: _Optional[_Iterable[_Union[UpdateConfigArg.IndexInfo, _Mapping]]] = ...) -> None: ...

class GetStatsArg(_message.Message):
    __slots__ = ("index_name_vec",)
    INDEX_NAME_VEC_FIELD_NUMBER: _ClassVar[int]
    index_name_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, index_name_vec: _Optional[_Iterable[str]] = ...) -> None: ...

class GetStatsResult(_message.Message):
    __slots__ = ("lucene_index_stats",)
    class BucketStats(_message.Message):
        __slots__ = ("bucket_id", "stats", "disk_id")
        class StatsEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: str
            def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
        BUCKET_ID_FIELD_NUMBER: _ClassVar[int]
        STATS_FIELD_NUMBER: _ClassVar[int]
        DISK_ID_FIELD_NUMBER: _ClassVar[int]
        bucket_id: str
        stats: _containers.ScalarMap[str, str]
        disk_id: str
        def __init__(self, bucket_id: _Optional[str] = ..., stats: _Optional[_Mapping[str, str]] = ..., disk_id: _Optional[str] = ...) -> None: ...
    class IndexStats(_message.Message):
        __slots__ = ("per_bucket_stats", "per_replica_bucket_stats")
        PER_BUCKET_STATS_FIELD_NUMBER: _ClassVar[int]
        PER_REPLICA_BUCKET_STATS_FIELD_NUMBER: _ClassVar[int]
        per_bucket_stats: _containers.RepeatedCompositeFieldContainer[GetStatsResult.BucketStats]
        per_replica_bucket_stats: _containers.RepeatedCompositeFieldContainer[GetStatsResult.BucketStats]
        def __init__(self, per_bucket_stats: _Optional[_Iterable[_Union[GetStatsResult.BucketStats, _Mapping]]] = ..., per_replica_bucket_stats: _Optional[_Iterable[_Union[GetStatsResult.BucketStats, _Mapping]]] = ...) -> None: ...
    class LuceneIndexStatsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: GetStatsResult.IndexStats
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[GetStatsResult.IndexStats, _Mapping]] = ...) -> None: ...
    LUCENE_INDEX_STATS_FIELD_NUMBER: _ClassVar[int]
    lucene_index_stats: _containers.MessageMap[str, GetStatsResult.IndexStats]
    def __init__(self, lucene_index_stats: _Optional[_Mapping[str, GetStatsResult.IndexStats]] = ...) -> None: ...

class CommitChangesArg(_message.Message):
    __slots__ = ("index_name", "bucket_id", "index_incarnation_id", "bucket_incarnation_id", "for_replication", "disk_id")
    INDEX_NAME_FIELD_NUMBER: _ClassVar[int]
    BUCKET_ID_FIELD_NUMBER: _ClassVar[int]
    INDEX_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    BUCKET_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    FOR_REPLICATION_FIELD_NUMBER: _ClassVar[int]
    DISK_ID_FIELD_NUMBER: _ClassVar[int]
    index_name: str
    bucket_id: int
    index_incarnation_id: int
    bucket_incarnation_id: int
    for_replication: bool
    disk_id: int
    def __init__(self, index_name: _Optional[str] = ..., bucket_id: _Optional[int] = ..., index_incarnation_id: _Optional[int] = ..., bucket_incarnation_id: _Optional[int] = ..., for_replication: bool = ..., disk_id: _Optional[int] = ...) -> None: ...

class SetGflagsArg(_message.Message):
    __slots__ = ("gflags_vec",)
    class Flag(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    GFLAGS_VEC_FIELD_NUMBER: _ClassVar[int]
    gflags_vec: _containers.RepeatedCompositeFieldContainer[SetGflagsArg.Flag]
    def __init__(self, gflags_vec: _Optional[_Iterable[_Union[SetGflagsArg.Flag, _Mapping]]] = ...) -> None: ...
