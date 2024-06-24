from bridge.base import cloud_pb2 as _cloud_pb2
from bridge.base import request_context_pb2 as _request_context_pb2
from bridge.blob_store import blob_store_pb2 as _blob_store_pb2
from open_util.net import protorpc_pb2 as _protorpc_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ReadChunksArg(_message.Message):
    __slots__ = ("cloud_object_id", "cloud_chunk_file_version", "cloud_chunk_file_metadata_size", "cloud_chunk_id_vec", "request_context", "read_from_uptiered_copy")
    CLOUD_OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    CLOUD_CHUNK_FILE_VERSION_FIELD_NUMBER: _ClassVar[int]
    CLOUD_CHUNK_FILE_METADATA_SIZE_FIELD_NUMBER: _ClassVar[int]
    CLOUD_CHUNK_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    REQUEST_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    READ_FROM_UPTIERED_COPY_FIELD_NUMBER: _ClassVar[int]
    cloud_object_id: _cloud_pb2.CloudObjectIdProto
    cloud_chunk_file_version: int
    cloud_chunk_file_metadata_size: int
    cloud_chunk_id_vec: _containers.RepeatedCompositeFieldContainer[_blob_store_pb2.CloudChunkIdProto]
    request_context: _request_context_pb2.RequestContextProto
    read_from_uptiered_copy: bool
    def __init__(self, cloud_object_id: _Optional[_Union[_cloud_pb2.CloudObjectIdProto, _Mapping]] = ..., cloud_chunk_file_version: _Optional[int] = ..., cloud_chunk_file_metadata_size: _Optional[int] = ..., cloud_chunk_id_vec: _Optional[_Iterable[_Union[_blob_store_pb2.CloudChunkIdProto, _Mapping]]] = ..., request_context: _Optional[_Union[_request_context_pb2.RequestContextProto, _Mapping]] = ..., read_from_uptiered_copy: bool = ...) -> None: ...

class ReadChunksResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
