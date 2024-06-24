from magneto.api import magneto_external_base_pb2 as _magneto_external_base_pb2
from magneto.api import permissions_external_pb2 as _permissions_external_pb2
from magneto.base import enums_pb2 as _enums_pb2
from magneto.base import magneto_pb2 as _magneto_pb2
from magneto.base import env_params_pb2 as _env_params_pb2
from util.base import universal_id_pb2 as _universal_id_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import python_message as _python_message
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class V1EntityInfoProto(_message.Message):
    __slots__ = ("entity_id", "parent_entity_id")
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    PARENT_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    entity_id: int
    parent_entity_id: int
    def __init__(self, entity_id: _Optional[int] = ..., parent_entity_id: _Optional[int] = ...) -> None: ...

class RegisterSourceArg(_message.Message):
    __slots__ = ("base", "environment", "encrypted_credentials", "serialized_magneto_v1_register_arg", "should_edit_source", "source_primary_key", "source_entity_id")
    Extensions: _python_message._ExtensionDict
    BASE_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTED_CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    SERIALIZED_MAGNETO_V1_REGISTER_ARG_FIELD_NUMBER: _ClassVar[int]
    SHOULD_EDIT_SOURCE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_PRIMARY_KEY_FIELD_NUMBER: _ClassVar[int]
    SOURCE_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ArgumentBase
    environment: _enums_pb2.Environment.Type
    encrypted_credentials: bytes
    serialized_magneto_v1_register_arg: bytes
    should_edit_source: bool
    source_primary_key: str
    source_entity_id: int
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ArgumentBase, _Mapping]] = ..., environment: _Optional[_Union[_enums_pb2.Environment.Type, str]] = ..., encrypted_credentials: _Optional[bytes] = ..., serialized_magneto_v1_register_arg: _Optional[bytes] = ..., should_edit_source: bool = ..., source_primary_key: _Optional[str] = ..., source_entity_id: _Optional[int] = ...) -> None: ...

class RegisterSourceResult(_message.Message):
    __slots__ = ("base", "registered_source_primary_key", "refresh_task_id", "serialized_magneto_v1_register_result", "v1_info")
    Extensions: _python_message._ExtensionDict
    BASE_FIELD_NUMBER: _ClassVar[int]
    REGISTERED_SOURCE_PRIMARY_KEY_FIELD_NUMBER: _ClassVar[int]
    REFRESH_TASK_ID_FIELD_NUMBER: _ClassVar[int]
    SERIALIZED_MAGNETO_V1_REGISTER_RESULT_FIELD_NUMBER: _ClassVar[int]
    V1_INFO_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ResultBase
    registered_source_primary_key: str
    refresh_task_id: bytes
    serialized_magneto_v1_register_result: bytes
    v1_info: V1EntityInfoProto
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ResultBase, _Mapping]] = ..., registered_source_primary_key: _Optional[str] = ..., refresh_task_id: _Optional[bytes] = ..., serialized_magneto_v1_register_result: _Optional[bytes] = ..., v1_info: _Optional[_Union[V1EntityInfoProto, _Mapping]] = ...) -> None: ...

class UnregisterSourceArg(_message.Message):
    __slots__ = ("base", "registered_source_primary_key", "environment", "registered_source_entity_id", "serialized_magneto_v1_unregister_arg")
    Extensions: _python_message._ExtensionDict
    BASE_FIELD_NUMBER: _ClassVar[int]
    REGISTERED_SOURCE_PRIMARY_KEY_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    REGISTERED_SOURCE_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    SERIALIZED_MAGNETO_V1_UNREGISTER_ARG_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ArgumentBase
    registered_source_primary_key: str
    environment: _enums_pb2.Environment.Type
    registered_source_entity_id: int
    serialized_magneto_v1_unregister_arg: bytes
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ArgumentBase, _Mapping]] = ..., registered_source_primary_key: _Optional[str] = ..., environment: _Optional[_Union[_enums_pb2.Environment.Type, str]] = ..., registered_source_entity_id: _Optional[int] = ..., serialized_magneto_v1_unregister_arg: _Optional[bytes] = ...) -> None: ...

class UnregisterSourceResult(_message.Message):
    __slots__ = ("base", "serialized_magneto_v1_unregister_result")
    Extensions: _python_message._ExtensionDict
    BASE_FIELD_NUMBER: _ClassVar[int]
    SERIALIZED_MAGNETO_V1_UNREGISTER_RESULT_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ResultBase
    serialized_magneto_v1_unregister_result: bytes
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ResultBase, _Mapping]] = ..., serialized_magneto_v1_unregister_result: _Optional[bytes] = ...) -> None: ...

class UpdateEntityArg(_message.Message):
    __slots__ = ("base", "primary_key", "should_return_entity_proto", "entity_id", "serialized_magneto_v1_update_arg")
    Extensions: _python_message._ExtensionDict
    BASE_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_KEY_FIELD_NUMBER: _ClassVar[int]
    SHOULD_RETURN_ENTITY_PROTO_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    SERIALIZED_MAGNETO_V1_UPDATE_ARG_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ArgumentBase
    primary_key: str
    should_return_entity_proto: bool
    entity_id: int
    serialized_magneto_v1_update_arg: bytes
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ArgumentBase, _Mapping]] = ..., primary_key: _Optional[str] = ..., should_return_entity_proto: bool = ..., entity_id: _Optional[int] = ..., serialized_magneto_v1_update_arg: _Optional[bytes] = ...) -> None: ...

class UpdateEntityResult(_message.Message):
    __slots__ = ("base", "serialized_magneto_v1_update_result")
    Extensions: _python_message._ExtensionDict
    BASE_FIELD_NUMBER: _ClassVar[int]
    SERIALIZED_MAGNETO_V1_UPDATE_RESULT_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ResultBase
    serialized_magneto_v1_update_result: bytes
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ResultBase, _Mapping]] = ..., serialized_magneto_v1_update_result: _Optional[bytes] = ...) -> None: ...

class StartSourceRefreshArg(_message.Message):
    __slots__ = ("base", "environment", "source_primary_key", "source_entity_id", "refresh_task_id", "should_force_refresh")
    BASE_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    SOURCE_PRIMARY_KEY_FIELD_NUMBER: _ClassVar[int]
    SOURCE_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    REFRESH_TASK_ID_FIELD_NUMBER: _ClassVar[int]
    SHOULD_FORCE_REFRESH_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ArgumentBase
    environment: _enums_pb2.Environment.Type
    source_primary_key: str
    source_entity_id: int
    refresh_task_id: bytes
    should_force_refresh: bool
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ArgumentBase, _Mapping]] = ..., environment: _Optional[_Union[_enums_pb2.Environment.Type, str]] = ..., source_primary_key: _Optional[str] = ..., source_entity_id: _Optional[int] = ..., refresh_task_id: _Optional[bytes] = ..., should_force_refresh: bool = ...) -> None: ...

class StartSourceRefreshResult(_message.Message):
    __slots__ = ("base", "refresh_task_id", "refresh_status")
    Extensions: _python_message._ExtensionDict
    BASE_FIELD_NUMBER: _ClassVar[int]
    REFRESH_TASK_ID_FIELD_NUMBER: _ClassVar[int]
    REFRESH_STATUS_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ResultBase
    refresh_task_id: bytes
    refresh_status: _enums_pb2.PublicTaskStatus.Type
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ResultBase, _Mapping]] = ..., refresh_task_id: _Optional[bytes] = ..., refresh_status: _Optional[_Union[_enums_pb2.PublicTaskStatus.Type, str]] = ...) -> None: ...

class ExternalEntityProto(_message.Message):
    __slots__ = ("environment", "primary_key", "serialized_magneto_v1_entity_hierarchy_proto", "v1_info", "aggregated_protected_info_vec", "aggregated_unprotected_info_vec")
    Extensions: _python_message._ExtensionDict
    ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_KEY_FIELD_NUMBER: _ClassVar[int]
    SERIALIZED_MAGNETO_V1_ENTITY_HIERARCHY_PROTO_FIELD_NUMBER: _ClassVar[int]
    V1_INFO_FIELD_NUMBER: _ClassVar[int]
    AGGREGATED_PROTECTED_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    AGGREGATED_UNPROTECTED_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    environment: _enums_pb2.Environment.Type
    primary_key: str
    serialized_magneto_v1_entity_hierarchy_proto: bytes
    v1_info: V1EntityInfoProto
    aggregated_protected_info_vec: _containers.RepeatedCompositeFieldContainer[_magneto_pb2.EntityHierarchyProto.AggregatedEntityInfo]
    aggregated_unprotected_info_vec: _containers.RepeatedCompositeFieldContainer[_magneto_pb2.EntityHierarchyProto.AggregatedEntityInfo]
    def __init__(self, environment: _Optional[_Union[_enums_pb2.Environment.Type, str]] = ..., primary_key: _Optional[str] = ..., serialized_magneto_v1_entity_hierarchy_proto: _Optional[bytes] = ..., v1_info: _Optional[_Union[V1EntityInfoProto, _Mapping]] = ..., aggregated_protected_info_vec: _Optional[_Iterable[_Union[_magneto_pb2.EntityHierarchyProto.AggregatedEntityInfo, _Mapping]]] = ..., aggregated_unprotected_info_vec: _Optional[_Iterable[_Union[_magneto_pb2.EntityHierarchyProto.AggregatedEntityInfo, _Mapping]]] = ...) -> None: ...

class GetHierarchyArg(_message.Message):
    __slots__ = ("base", "entity_primary_key", "entity_id", "type_vec", "num_levels")
    BASE_FIELD_NUMBER: _ClassVar[int]
    ENTITY_PRIMARY_KEY_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_VEC_FIELD_NUMBER: _ClassVar[int]
    NUM_LEVELS_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ArgumentBase
    entity_primary_key: str
    entity_id: int
    type_vec: _containers.RepeatedScalarFieldContainer[_enums_pb2.Environment.Type]
    num_levels: int
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ArgumentBase, _Mapping]] = ..., entity_primary_key: _Optional[str] = ..., entity_id: _Optional[int] = ..., type_vec: _Optional[_Iterable[_Union[_enums_pb2.Environment.Type, str]]] = ..., num_levels: _Optional[int] = ...) -> None: ...

class EntityHierarchyDAGProto(_message.Message):
    __slots__ = ("root_node_index", "dag_node_vec")
    class Node(_message.Message):
        __slots__ = ("uid", "entity_info", "dst_node_index_vec")
        UID_FIELD_NUMBER: _ClassVar[int]
        ENTITY_INFO_FIELD_NUMBER: _ClassVar[int]
        DST_NODE_INDEX_VEC_FIELD_NUMBER: _ClassVar[int]
        uid: _universal_id_pb2.UniversalIdProto
        entity_info: ExternalEntityProto
        dst_node_index_vec: _containers.RepeatedScalarFieldContainer[int]
        def __init__(self, uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., entity_info: _Optional[_Union[ExternalEntityProto, _Mapping]] = ..., dst_node_index_vec: _Optional[_Iterable[int]] = ...) -> None: ...
    ROOT_NODE_INDEX_FIELD_NUMBER: _ClassVar[int]
    DAG_NODE_VEC_FIELD_NUMBER: _ClassVar[int]
    root_node_index: int
    dag_node_vec: _containers.RepeatedCompositeFieldContainer[EntityHierarchyDAGProto.Node]
    def __init__(self, root_node_index: _Optional[int] = ..., dag_node_vec: _Optional[_Iterable[_Union[EntityHierarchyDAGProto.Node, _Mapping]]] = ...) -> None: ...

class GetHierarchyResult(_message.Message):
    __slots__ = ("base", "entity_hierarchy_dag")
    BASE_FIELD_NUMBER: _ClassVar[int]
    ENTITY_HIERARCHY_DAG_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ResultBase
    entity_hierarchy_dag: _containers.RepeatedCompositeFieldContainer[EntityHierarchyDAGProto]
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ResultBase, _Mapping]] = ..., entity_hierarchy_dag: _Optional[_Iterable[_Union[EntityHierarchyDAGProto, _Mapping]]] = ...) -> None: ...

class FetchInfoForEntitiesArg(_message.Message):
    __slots__ = ("base", "entity_primary_key_vec", "entity_id_vec", "match_registered_source_primary_key", "only_in_hierarchy", "verbosity")
    Extensions: _python_message._ExtensionDict
    BASE_FIELD_NUMBER: _ClassVar[int]
    ENTITY_PRIMARY_KEY_VEC_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    MATCH_REGISTERED_SOURCE_PRIMARY_KEY_FIELD_NUMBER: _ClassVar[int]
    ONLY_IN_HIERARCHY_FIELD_NUMBER: _ClassVar[int]
    VERBOSITY_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ArgumentBase
    entity_primary_key_vec: _containers.RepeatedScalarFieldContainer[str]
    entity_id_vec: _containers.RepeatedScalarFieldContainer[int]
    match_registered_source_primary_key: str
    only_in_hierarchy: bool
    verbosity: int
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ArgumentBase, _Mapping]] = ..., entity_primary_key_vec: _Optional[_Iterable[str]] = ..., entity_id_vec: _Optional[_Iterable[int]] = ..., match_registered_source_primary_key: _Optional[str] = ..., only_in_hierarchy: bool = ..., verbosity: _Optional[int] = ...) -> None: ...

class FetchInfoForEntitiesResult(_message.Message):
    __slots__ = ("base", "result_vec")
    class Result(_message.Message):
        __slots__ = ("entity_primary_key", "entity_id", "error", "entity_info")
        ENTITY_PRIMARY_KEY_FIELD_NUMBER: _ClassVar[int]
        ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        ENTITY_INFO_FIELD_NUMBER: _ClassVar[int]
        entity_primary_key: str
        entity_id: int
        error: _magneto_external_base_pb2.ErrorProto
        entity_info: ExternalEntityProto
        def __init__(self, entity_primary_key: _Optional[str] = ..., entity_id: _Optional[int] = ..., error: _Optional[_Union[_magneto_external_base_pb2.ErrorProto, _Mapping]] = ..., entity_info: _Optional[_Union[ExternalEntityProto, _Mapping]] = ...) -> None: ...
    BASE_FIELD_NUMBER: _ClassVar[int]
    RESULT_VEC_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ResultBase
    result_vec: _containers.RepeatedCompositeFieldContainer[FetchInfoForEntitiesResult.Result]
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ResultBase, _Mapping]] = ..., result_vec: _Optional[_Iterable[_Union[FetchInfoForEntitiesResult.Result, _Mapping]]] = ...) -> None: ...

class UpdatePermissionsForEntityArg(_message.Message):
    __slots__ = ("base", "entity_permission_info_vec")
    class EntityPermissionInfo(_message.Message):
        __slots__ = ("primary_key", "entity_id", "permission_info")
        PRIMARY_KEY_FIELD_NUMBER: _ClassVar[int]
        ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_INFO_FIELD_NUMBER: _ClassVar[int]
        primary_key: str
        entity_id: int
        permission_info: _permissions_external_pb2.EntityPermissionInfoProto
        def __init__(self, primary_key: _Optional[str] = ..., entity_id: _Optional[int] = ..., permission_info: _Optional[_Union[_permissions_external_pb2.EntityPermissionInfoProto, _Mapping]] = ...) -> None: ...
    BASE_FIELD_NUMBER: _ClassVar[int]
    ENTITY_PERMISSION_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ArgumentBase
    entity_permission_info_vec: _containers.RepeatedCompositeFieldContainer[UpdatePermissionsForEntityArg.EntityPermissionInfo]
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ArgumentBase, _Mapping]] = ..., entity_permission_info_vec: _Optional[_Iterable[_Union[UpdatePermissionsForEntityArg.EntityPermissionInfo, _Mapping]]] = ...) -> None: ...

class UpdatePermissionsForEntityResult(_message.Message):
    __slots__ = ("base", "result_vec")
    class Result(_message.Message):
        __slots__ = ("primary_key", "entity_id", "error")
        PRIMARY_KEY_FIELD_NUMBER: _ClassVar[int]
        ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        primary_key: str
        entity_id: int
        error: _magneto_external_base_pb2.ErrorProto
        def __init__(self, primary_key: _Optional[str] = ..., entity_id: _Optional[int] = ..., error: _Optional[_Union[_magneto_external_base_pb2.ErrorProto, _Mapping]] = ...) -> None: ...
    BASE_FIELD_NUMBER: _ClassVar[int]
    RESULT_VEC_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ResultBase
    result_vec: _containers.RepeatedCompositeFieldContainer[UpdatePermissionsForEntityResult.Result]
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ResultBase, _Mapping]] = ..., result_vec: _Optional[_Iterable[_Union[UpdatePermissionsForEntityResult.Result, _Mapping]]] = ...) -> None: ...
