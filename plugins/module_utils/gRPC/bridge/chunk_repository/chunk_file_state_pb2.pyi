from bridge.chunk_repository import disk_logger_pb2 as _disk_logger_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ChunkFileStateProto(_message.Message):
    __slots__ = ("version", "highest_intent_id_detected", "physical_version", "max_chunk_file_bytes", "used_chunk_file_bytes", "stripe_column", "next_available_chunkgroup_id", "is_corrupt", "update_intent_vec", "last_finalized_intent_id", "last_aborted_intent_id", "last_read_access_time_secs", "last_write_access_time_secs", "chunk_stripe_type", "max_pin_secs_hint", "view_box_id", "corruption_error_info")
    VERSION_FIELD_NUMBER: _ClassVar[int]
    HIGHEST_INTENT_ID_DETECTED_FIELD_NUMBER: _ClassVar[int]
    PHYSICAL_VERSION_FIELD_NUMBER: _ClassVar[int]
    MAX_CHUNK_FILE_BYTES_FIELD_NUMBER: _ClassVar[int]
    USED_CHUNK_FILE_BYTES_FIELD_NUMBER: _ClassVar[int]
    STRIPE_COLUMN_FIELD_NUMBER: _ClassVar[int]
    NEXT_AVAILABLE_CHUNKGROUP_ID_FIELD_NUMBER: _ClassVar[int]
    IS_CORRUPT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_INTENT_VEC_FIELD_NUMBER: _ClassVar[int]
    LAST_FINALIZED_INTENT_ID_FIELD_NUMBER: _ClassVar[int]
    LAST_ABORTED_INTENT_ID_FIELD_NUMBER: _ClassVar[int]
    LAST_READ_ACCESS_TIME_SECS_FIELD_NUMBER: _ClassVar[int]
    LAST_WRITE_ACCESS_TIME_SECS_FIELD_NUMBER: _ClassVar[int]
    CHUNK_STRIPE_TYPE_FIELD_NUMBER: _ClassVar[int]
    MAX_PIN_SECS_HINT_FIELD_NUMBER: _ClassVar[int]
    VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
    CORRUPTION_ERROR_INFO_FIELD_NUMBER: _ClassVar[int]
    version: int
    highest_intent_id_detected: int
    physical_version: int
    max_chunk_file_bytes: int
    used_chunk_file_bytes: int
    stripe_column: int
    next_available_chunkgroup_id: int
    is_corrupt: bool
    update_intent_vec: _containers.RepeatedCompositeFieldContainer[_disk_logger_pb2.DiskLoggerRecordProto.UpdateIntent]
    last_finalized_intent_id: int
    last_aborted_intent_id: int
    last_read_access_time_secs: int
    last_write_access_time_secs: int
    chunk_stripe_type: _disk_logger_pb2.DiskLoggerRecordProto.ChunkFileChange.ChunkStripeType
    max_pin_secs_hint: int
    view_box_id: int
    corruption_error_info: _disk_logger_pb2.DiskLoggerRecordProto.ChunkFileChange.CorruptionErrorInfo
    def __init__(self, version: _Optional[int] = ..., highest_intent_id_detected: _Optional[int] = ..., physical_version: _Optional[int] = ..., max_chunk_file_bytes: _Optional[int] = ..., used_chunk_file_bytes: _Optional[int] = ..., stripe_column: _Optional[int] = ..., next_available_chunkgroup_id: _Optional[int] = ..., is_corrupt: bool = ..., update_intent_vec: _Optional[_Iterable[_Union[_disk_logger_pb2.DiskLoggerRecordProto.UpdateIntent, _Mapping]]] = ..., last_finalized_intent_id: _Optional[int] = ..., last_aborted_intent_id: _Optional[int] = ..., last_read_access_time_secs: _Optional[int] = ..., last_write_access_time_secs: _Optional[int] = ..., chunk_stripe_type: _Optional[_Union[_disk_logger_pb2.DiskLoggerRecordProto.ChunkFileChange.ChunkStripeType, str]] = ..., max_pin_secs_hint: _Optional[int] = ..., view_box_id: _Optional[int] = ..., corruption_error_info: _Optional[_Union[_disk_logger_pb2.DiskLoggerRecordProto.ChunkFileChange.CorruptionErrorInfo, _Mapping]] = ...) -> None: ...
