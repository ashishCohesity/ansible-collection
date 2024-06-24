from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EntityAttributesNamesProto(_message.Message):
    __slots__ = ("is_taskable", "is_registered_source", "registered_source_primary_key", "last_refresh_start_time", "last_refresh_error", "num_protected_children", "total_protected_bytes_logical", "num_unprotected_children", "total_unprotected_bytes_logical", "checksum", "detached_from_eh", "logical_size_in_bytes")
    IS_TASKABLE_FIELD_NUMBER: _ClassVar[int]
    IS_REGISTERED_SOURCE_FIELD_NUMBER: _ClassVar[int]
    REGISTERED_SOURCE_PRIMARY_KEY_FIELD_NUMBER: _ClassVar[int]
    LAST_REFRESH_START_TIME_FIELD_NUMBER: _ClassVar[int]
    LAST_REFRESH_ERROR_FIELD_NUMBER: _ClassVar[int]
    NUM_PROTECTED_CHILDREN_FIELD_NUMBER: _ClassVar[int]
    TOTAL_PROTECTED_BYTES_LOGICAL_FIELD_NUMBER: _ClassVar[int]
    NUM_UNPROTECTED_CHILDREN_FIELD_NUMBER: _ClassVar[int]
    TOTAL_UNPROTECTED_BYTES_LOGICAL_FIELD_NUMBER: _ClassVar[int]
    CHECKSUM_FIELD_NUMBER: _ClassVar[int]
    DETACHED_FROM_EH_FIELD_NUMBER: _ClassVar[int]
    LOGICAL_SIZE_IN_BYTES_FIELD_NUMBER: _ClassVar[int]
    is_taskable: str
    is_registered_source: str
    registered_source_primary_key: str
    last_refresh_start_time: str
    last_refresh_error: str
    num_protected_children: str
    total_protected_bytes_logical: str
    num_unprotected_children: str
    total_unprotected_bytes_logical: str
    checksum: str
    detached_from_eh: str
    logical_size_in_bytes: str
    def __init__(self, is_taskable: _Optional[str] = ..., is_registered_source: _Optional[str] = ..., registered_source_primary_key: _Optional[str] = ..., last_refresh_start_time: _Optional[str] = ..., last_refresh_error: _Optional[str] = ..., num_protected_children: _Optional[str] = ..., total_protected_bytes_logical: _Optional[str] = ..., num_unprotected_children: _Optional[str] = ..., total_unprotected_bytes_logical: _Optional[str] = ..., checksum: _Optional[str] = ..., detached_from_eh: _Optional[str] = ..., logical_size_in_bytes: _Optional[str] = ...) -> None: ...

class EntityAttachmentNamesProto(_message.Message):
    __slots__ = ("registration_info", "registered_entity_info", "aggregated_info")
    REGISTRATION_INFO_FIELD_NUMBER: _ClassVar[int]
    REGISTERED_ENTITY_INFO_FIELD_NUMBER: _ClassVar[int]
    AGGREGATED_INFO_FIELD_NUMBER: _ClassVar[int]
    registration_info: str
    registered_entity_info: str
    aggregated_info: str
    def __init__(self, registration_info: _Optional[str] = ..., registered_entity_info: _Optional[str] = ..., aggregated_info: _Optional[str] = ...) -> None: ...

class AggregatedEntityInfoProto(_message.Message):
    __slots__ = ("aggregated_counters_vec",)
    class Counters(_message.Message):
        __slots__ = ("count", "bytes")
        COUNT_FIELD_NUMBER: _ClassVar[int]
        BYTES_FIELD_NUMBER: _ClassVar[int]
        count: int
        bytes: int
        def __init__(self, count: _Optional[int] = ..., bytes: _Optional[int] = ...) -> None: ...
    class AggregatedCounters(_message.Message):
        __slots__ = ("environment_type_str", "protected", "unprotected")
        ENVIRONMENT_TYPE_STR_FIELD_NUMBER: _ClassVar[int]
        PROTECTED_FIELD_NUMBER: _ClassVar[int]
        UNPROTECTED_FIELD_NUMBER: _ClassVar[int]
        environment_type_str: str
        protected: AggregatedEntityInfoProto.Counters
        unprotected: AggregatedEntityInfoProto.Counters
        def __init__(self, environment_type_str: _Optional[str] = ..., protected: _Optional[_Union[AggregatedEntityInfoProto.Counters, _Mapping]] = ..., unprotected: _Optional[_Union[AggregatedEntityInfoProto.Counters, _Mapping]] = ...) -> None: ...
    AGGREGATED_COUNTERS_VEC_FIELD_NUMBER: _ClassVar[int]
    aggregated_counters_vec: _containers.RepeatedCompositeFieldContainer[AggregatedEntityInfoProto.AggregatedCounters]
    def __init__(self, aggregated_counters_vec: _Optional[_Iterable[_Union[AggregatedEntityInfoProto.AggregatedCounters, _Mapping]]] = ...) -> None: ...

class PrincipalAttributeNamesProto(_message.Message):
    __slots__ = ("tenant_id", "serialized_sid")
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    SERIALIZED_SID_FIELD_NUMBER: _ClassVar[int]
    tenant_id: str
    serialized_sid: str
    def __init__(self, tenant_id: _Optional[str] = ..., serialized_sid: _Optional[str] = ...) -> None: ...
