from helios.base import helios_cluster_base_pb2 as _helios_cluster_base_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CacheRequestArg(_message.Message):
    __slots__ = ("request_vec",)
    class CacheRequest(_message.Message):
        __slots__ = ("cluster_identifier",)
        CLUSTER_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
        cluster_identifier: _helios_cluster_base_pb2.ClusterIdentifier
        def __init__(self, cluster_identifier: _Optional[_Union[_helios_cluster_base_pb2.ClusterIdentifier, _Mapping]] = ...) -> None: ...
    REQUEST_VEC_FIELD_NUMBER: _ClassVar[int]
    request_vec: _containers.RepeatedCompositeFieldContainer[CacheRequestArg.CacheRequest]
    def __init__(self, request_vec: _Optional[_Iterable[_Union[CacheRequestArg.CacheRequest, _Mapping]]] = ...) -> None: ...

class CacheResponse(_message.Message):
    __slots__ = ("result_vec",)
    class CacheResult(_message.Message):
        __slots__ = ("cluster_identifier", "status", "output", "total_object_count")
        class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kSuccess: _ClassVar[CacheResponse.CacheResult.Status]
            kFailure: _ClassVar[CacheResponse.CacheResult.Status]
        kSuccess: CacheResponse.CacheResult.Status
        kFailure: CacheResponse.CacheResult.Status
        CLUSTER_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        OUTPUT_FIELD_NUMBER: _ClassVar[int]
        TOTAL_OBJECT_COUNT_FIELD_NUMBER: _ClassVar[int]
        cluster_identifier: _helios_cluster_base_pb2.ClusterIdentifier
        status: CacheResponse.CacheResult.Status
        output: str
        total_object_count: int
        def __init__(self, cluster_identifier: _Optional[_Union[_helios_cluster_base_pb2.ClusterIdentifier, _Mapping]] = ..., status: _Optional[_Union[CacheResponse.CacheResult.Status, str]] = ..., output: _Optional[str] = ..., total_object_count: _Optional[int] = ...) -> None: ...
    RESULT_VEC_FIELD_NUMBER: _ClassVar[int]
    result_vec: _containers.RepeatedCompositeFieldContainer[CacheResponse.CacheResult]
    def __init__(self, result_vec: _Optional[_Iterable[_Union[CacheResponse.CacheResult, _Mapping]]] = ...) -> None: ...

class McmEtlRestUrisProto(_message.Message):
    __slots__ = ("mcmetl_rest_port", "api_version", "cache_uri", "mcm_tag_updates_uri", "gc_tag_updates_uri")
    MCMETL_REST_PORT_FIELD_NUMBER: _ClassVar[int]
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    CACHE_URI_FIELD_NUMBER: _ClassVar[int]
    MCM_TAG_UPDATES_URI_FIELD_NUMBER: _ClassVar[int]
    GC_TAG_UPDATES_URI_FIELD_NUMBER: _ClassVar[int]
    mcmetl_rest_port: int
    api_version: str
    cache_uri: str
    mcm_tag_updates_uri: str
    gc_tag_updates_uri: str
    def __init__(self, mcmetl_rest_port: _Optional[int] = ..., api_version: _Optional[str] = ..., cache_uri: _Optional[str] = ..., mcm_tag_updates_uri: _Optional[str] = ..., gc_tag_updates_uri: _Optional[str] = ...) -> None: ...
