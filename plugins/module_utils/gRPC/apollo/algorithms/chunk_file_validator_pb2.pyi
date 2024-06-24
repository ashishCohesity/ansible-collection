from configs import cluster_config_pb2 as _cluster_config_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ChunkFileValidatorContextDataProto(_message.Message):
    __slots__ = ("cluster_config_proto",)
    CLUSTER_CONFIG_PROTO_FIELD_NUMBER: _ClassVar[int]
    cluster_config_proto: _cluster_config_pb2.ClusterConfigProto
    def __init__(self, cluster_config_proto: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto, _Mapping]] = ...) -> None: ...

class ChunkFileValidatorMapKeyProto(_message.Message):
    __slots__ = ("disk_id", "chunk_file_id")
    DISK_ID_FIELD_NUMBER: _ClassVar[int]
    CHUNK_FILE_ID_FIELD_NUMBER: _ClassVar[int]
    disk_id: int
    chunk_file_id: int
    def __init__(self, disk_id: _Optional[int] = ..., chunk_file_id: _Optional[int] = ...) -> None: ...

class ChunkFileValidatorMapValueProto(_message.Message):
    __slots__ = ("in_scribe", "on_disk", "owner_blob_id", "view_box_id", "is_empty_chunk_file")
    IN_SCRIBE_FIELD_NUMBER: _ClassVar[int]
    ON_DISK_FIELD_NUMBER: _ClassVar[int]
    OWNER_BLOB_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
    IS_EMPTY_CHUNK_FILE_FIELD_NUMBER: _ClassVar[int]
    in_scribe: bool
    on_disk: bool
    owner_blob_id: int
    view_box_id: int
    is_empty_chunk_file: bool
    def __init__(self, in_scribe: bool = ..., on_disk: bool = ..., owner_blob_id: _Optional[int] = ..., view_box_id: _Optional[int] = ..., is_empty_chunk_file: bool = ...) -> None: ...

class ChunkFileValidatorDiskIdScannedProto(_message.Message):
    __slots__ = ("scanned_disk_id",)
    SCANNED_DISK_ID_FIELD_NUMBER: _ClassVar[int]
    scanned_disk_id: int
    def __init__(self, scanned_disk_id: _Optional[int] = ...) -> None: ...
