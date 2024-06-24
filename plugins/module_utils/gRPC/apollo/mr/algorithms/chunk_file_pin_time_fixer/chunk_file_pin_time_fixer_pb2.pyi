from bridge.blob_store import blob_store_pb2 as _blob_store_pb2
from bridge.view_keeper import view_metadata_pb2 as _view_metadata_pb2
from configs import cluster_config_pb2 as _cluster_config_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ChunkFilePinTimeFixerContextDataProto(_message.Message):
    __slots__ = ("cluster_config_proto", "pinned_view_vec", "view_metadata_scan_successful")
    class PinnedViewEntry(_message.Message):
        __slots__ = ("view_id", "pin_config")
        VIEW_ID_FIELD_NUMBER: _ClassVar[int]
        PIN_CONFIG_FIELD_NUMBER: _ClassVar[int]
        view_id: int
        pin_config: _view_metadata_pb2.ViewIdMappingProto.PinConfig
        def __init__(self, view_id: _Optional[int] = ..., pin_config: _Optional[_Union[_view_metadata_pb2.ViewIdMappingProto.PinConfig, _Mapping]] = ...) -> None: ...
    CLUSTER_CONFIG_PROTO_FIELD_NUMBER: _ClassVar[int]
    PINNED_VIEW_VEC_FIELD_NUMBER: _ClassVar[int]
    VIEW_METADATA_SCAN_SUCCESSFUL_FIELD_NUMBER: _ClassVar[int]
    cluster_config_proto: _cluster_config_pb2.ClusterConfigProto
    pinned_view_vec: _containers.RepeatedCompositeFieldContainer[ChunkFilePinTimeFixerContextDataProto.PinnedViewEntry]
    view_metadata_scan_successful: bool
    def __init__(self, cluster_config_proto: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto, _Mapping]] = ..., pinned_view_vec: _Optional[_Iterable[_Union[ChunkFilePinTimeFixerContextDataProto.PinnedViewEntry, _Mapping]]] = ..., view_metadata_scan_successful: bool = ...) -> None: ...

class ChunkFileIdMapValueProto(_message.Message):
    __slots__ = ("max_pin_time_secs", "pinned_chunk_file_access_state_proto", "scribe_row_version", "replica_vec", "is_rf_chunk_file", "should_update_pin_time_secs")
    MAX_PIN_TIME_SECS_FIELD_NUMBER: _ClassVar[int]
    PINNED_CHUNK_FILE_ACCESS_STATE_PROTO_FIELD_NUMBER: _ClassVar[int]
    SCRIBE_ROW_VERSION_FIELD_NUMBER: _ClassVar[int]
    REPLICA_VEC_FIELD_NUMBER: _ClassVar[int]
    IS_RF_CHUNK_FILE_FIELD_NUMBER: _ClassVar[int]
    SHOULD_UPDATE_PIN_TIME_SECS_FIELD_NUMBER: _ClassVar[int]
    max_pin_time_secs: int
    pinned_chunk_file_access_state_proto: _blob_store_pb2.PinnedChunkFileAccessStateProto
    scribe_row_version: int
    replica_vec: _containers.RepeatedScalarFieldContainer[int]
    is_rf_chunk_file: bool
    should_update_pin_time_secs: bool
    def __init__(self, max_pin_time_secs: _Optional[int] = ..., pinned_chunk_file_access_state_proto: _Optional[_Union[_blob_store_pb2.PinnedChunkFileAccessStateProto, _Mapping]] = ..., scribe_row_version: _Optional[int] = ..., replica_vec: _Optional[_Iterable[int]] = ..., is_rf_chunk_file: bool = ..., should_update_pin_time_secs: bool = ...) -> None: ...

class DiskIdValueProto(_message.Message):
    __slots__ = ("chunk_file_id", "max_pin_time_secs", "pinned_chunk_file_access_state_proto", "scribe_row_version")
    CHUNK_FILE_ID_FIELD_NUMBER: _ClassVar[int]
    MAX_PIN_TIME_SECS_FIELD_NUMBER: _ClassVar[int]
    PINNED_CHUNK_FILE_ACCESS_STATE_PROTO_FIELD_NUMBER: _ClassVar[int]
    SCRIBE_ROW_VERSION_FIELD_NUMBER: _ClassVar[int]
    chunk_file_id: int
    max_pin_time_secs: int
    pinned_chunk_file_access_state_proto: _blob_store_pb2.PinnedChunkFileAccessStateProto
    scribe_row_version: int
    def __init__(self, chunk_file_id: _Optional[int] = ..., max_pin_time_secs: _Optional[int] = ..., pinned_chunk_file_access_state_proto: _Optional[_Union[_blob_store_pb2.PinnedChunkFileAccessStateProto, _Mapping]] = ..., scribe_row_version: _Optional[int] = ...) -> None: ...
