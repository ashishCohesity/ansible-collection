from configs import cluster_config_pb2 as _cluster_config_pb2
from util.base import universal_id_pb2 as _universal_id_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class IceboxArchiveRetirerContextDataProto(_message.Message):
    __slots__ = ("cluster_config_proto",)
    CLUSTER_CONFIG_PROTO_FIELD_NUMBER: _ClassVar[int]
    cluster_config_proto: _cluster_config_pb2.ClusterConfigProto
    def __init__(self, cluster_config_proto: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto, _Mapping]] = ...) -> None: ...

class IceboxArchiveRetirerMapKeyProto(_message.Message):
    __slots__ = ("archive_uid",)
    ARCHIVE_UID_FIELD_NUMBER: _ClassVar[int]
    archive_uid: _universal_id_pb2.UniversalIdProto
    def __init__(self, archive_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ...) -> None: ...

class IceboxArchiveRetirerMapValueProto(_message.Message):
    __slots__ = ("is_archive_retired", "num_chunk_expired", "num_chunk_alive", "num_chunk_with_op_in_progress", "num_chunk_without_access_timestamp")
    IS_ARCHIVE_RETIRED_FIELD_NUMBER: _ClassVar[int]
    NUM_CHUNK_EXPIRED_FIELD_NUMBER: _ClassVar[int]
    NUM_CHUNK_ALIVE_FIELD_NUMBER: _ClassVar[int]
    NUM_CHUNK_WITH_OP_IN_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    NUM_CHUNK_WITHOUT_ACCESS_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    is_archive_retired: bool
    num_chunk_expired: int
    num_chunk_alive: int
    num_chunk_with_op_in_progress: int
    num_chunk_without_access_timestamp: int
    def __init__(self, is_archive_retired: bool = ..., num_chunk_expired: _Optional[int] = ..., num_chunk_alive: _Optional[int] = ..., num_chunk_with_op_in_progress: _Optional[int] = ..., num_chunk_without_access_timestamp: _Optional[int] = ...) -> None: ...
