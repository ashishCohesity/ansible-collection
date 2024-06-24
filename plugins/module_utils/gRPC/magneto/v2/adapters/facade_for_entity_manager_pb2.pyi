from magneto.api import magneto_external_base_pb2 as _magneto_external_base_pb2
from magneto.base import enums_pb2 as _enums_pb2
from magneto.base.v2 import internal_entity_pb2 as _internal_entity_pb2
from magneto.v2.entity_manager import entity_external_pb2 as _entity_external_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import python_message as _python_message
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RegisterSourceArgInternal(_message.Message):
    __slots__ = ("register_source_arg", "connector_params_id", "internal_entity_proto", "existing_serialized_registered_entity_info")
    Extensions: _python_message._ExtensionDict
    REGISTER_SOURCE_ARG_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_PARAMS_ID_FIELD_NUMBER: _ClassVar[int]
    INTERNAL_ENTITY_PROTO_FIELD_NUMBER: _ClassVar[int]
    EXISTING_SERIALIZED_REGISTERED_ENTITY_INFO_FIELD_NUMBER: _ClassVar[int]
    register_source_arg: _entity_external_pb2.RegisterSourceArg
    connector_params_id: int
    internal_entity_proto: _internal_entity_pb2.InternalEntityProto
    existing_serialized_registered_entity_info: bytes
    def __init__(self, register_source_arg: _Optional[_Union[_entity_external_pb2.RegisterSourceArg, _Mapping]] = ..., connector_params_id: _Optional[int] = ..., internal_entity_proto: _Optional[_Union[_internal_entity_pb2.InternalEntityProto, _Mapping]] = ..., existing_serialized_registered_entity_info: _Optional[bytes] = ...) -> None: ...

class RegisterSourceInternalResult(_message.Message):
    __slots__ = ("base", "registered_source_primary_key", "serialized_magneto_v1_register_result", "serialized_registered_entity_info")
    Extensions: _python_message._ExtensionDict
    BASE_FIELD_NUMBER: _ClassVar[int]
    REGISTERED_SOURCE_PRIMARY_KEY_FIELD_NUMBER: _ClassVar[int]
    SERIALIZED_MAGNETO_V1_REGISTER_RESULT_FIELD_NUMBER: _ClassVar[int]
    SERIALIZED_REGISTERED_ENTITY_INFO_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ResultBase
    registered_source_primary_key: str
    serialized_magneto_v1_register_result: bytes
    serialized_registered_entity_info: bytes
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ResultBase, _Mapping]] = ..., registered_source_primary_key: _Optional[str] = ..., serialized_magneto_v1_register_result: _Optional[bytes] = ..., serialized_registered_entity_info: _Optional[bytes] = ...) -> None: ...

class UnregisterSourceArg(_message.Message):
    __slots__ = ("base", "registered_source_primary_key", "environment", "serialized_magneto_v1_unregister_arg", "serialized_registered_entity_info")
    BASE_FIELD_NUMBER: _ClassVar[int]
    REGISTERED_SOURCE_PRIMARY_KEY_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    SERIALIZED_MAGNETO_V1_UNREGISTER_ARG_FIELD_NUMBER: _ClassVar[int]
    SERIALIZED_REGISTERED_ENTITY_INFO_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ArgumentBase
    registered_source_primary_key: str
    environment: _enums_pb2.Environment.Type
    serialized_magneto_v1_unregister_arg: bytes
    serialized_registered_entity_info: bytes
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ArgumentBase, _Mapping]] = ..., registered_source_primary_key: _Optional[str] = ..., environment: _Optional[_Union[_enums_pb2.Environment.Type, str]] = ..., serialized_magneto_v1_unregister_arg: _Optional[bytes] = ..., serialized_registered_entity_info: _Optional[bytes] = ...) -> None: ...

class FetchEntityHierarchyDAGArg(_message.Message):
    __slots__ = ("base", "serialized_registered_entity_info", "entity_primary_key")
    BASE_FIELD_NUMBER: _ClassVar[int]
    SERIALIZED_REGISTERED_ENTITY_INFO_FIELD_NUMBER: _ClassVar[int]
    ENTITY_PRIMARY_KEY_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ArgumentBase
    serialized_registered_entity_info: bytes
    entity_primary_key: str
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ArgumentBase, _Mapping]] = ..., serialized_registered_entity_info: _Optional[bytes] = ..., entity_primary_key: _Optional[str] = ...) -> None: ...

class FetchEntityHierarchyDAGResult(_message.Message):
    __slots__ = ("base", "entity_hierarchy_dag", "pk_to_entity_map")
    class PkToEntityMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _internal_entity_pb2.InternalEntityProto
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_internal_entity_pb2.InternalEntityProto, _Mapping]] = ...) -> None: ...
    BASE_FIELD_NUMBER: _ClassVar[int]
    ENTITY_HIERARCHY_DAG_FIELD_NUMBER: _ClassVar[int]
    PK_TO_ENTITY_MAP_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ResultBase
    entity_hierarchy_dag: _entity_external_pb2.EntityHierarchyDAGProto
    pk_to_entity_map: _containers.MessageMap[str, _internal_entity_pb2.InternalEntityProto]
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ResultBase, _Mapping]] = ..., entity_hierarchy_dag: _Optional[_Union[_entity_external_pb2.EntityHierarchyDAGProto, _Mapping]] = ..., pk_to_entity_map: _Optional[_Mapping[str, _internal_entity_pb2.InternalEntityProto]] = ...) -> None: ...

class FetchInfoForEntitiesInternalArg(_message.Message):
    __slots__ = ("base", "entity_primary_key_vec", "serialized_registered_entity_info")
    BASE_FIELD_NUMBER: _ClassVar[int]
    ENTITY_PRIMARY_KEY_VEC_FIELD_NUMBER: _ClassVar[int]
    SERIALIZED_REGISTERED_ENTITY_INFO_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ArgumentBase
    entity_primary_key_vec: _containers.RepeatedScalarFieldContainer[str]
    serialized_registered_entity_info: bytes
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ArgumentBase, _Mapping]] = ..., entity_primary_key_vec: _Optional[_Iterable[str]] = ..., serialized_registered_entity_info: _Optional[bytes] = ...) -> None: ...

class FetchInfoForEntitiesInternalResult(_message.Message):
    __slots__ = ("base", "result_vec")
    class Result(_message.Message):
        __slots__ = ("entity_primary_key", "error", "entity_info")
        ENTITY_PRIMARY_KEY_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        ENTITY_INFO_FIELD_NUMBER: _ClassVar[int]
        entity_primary_key: str
        error: _magneto_external_base_pb2.ErrorProto
        entity_info: _internal_entity_pb2.InternalEntityProto
        def __init__(self, entity_primary_key: _Optional[str] = ..., error: _Optional[_Union[_magneto_external_base_pb2.ErrorProto, _Mapping]] = ..., entity_info: _Optional[_Union[_internal_entity_pb2.InternalEntityProto, _Mapping]] = ...) -> None: ...
    BASE_FIELD_NUMBER: _ClassVar[int]
    RESULT_VEC_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ResultBase
    result_vec: _containers.RepeatedCompositeFieldContainer[FetchInfoForEntitiesInternalResult.Result]
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ResultBase, _Mapping]] = ..., result_vec: _Optional[_Iterable[_Union[FetchInfoForEntitiesInternalResult.Result, _Mapping]]] = ...) -> None: ...
