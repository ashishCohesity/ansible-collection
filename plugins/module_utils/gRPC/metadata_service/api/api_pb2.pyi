from metadata_service.base import error_pb2 as _error_pb2
from util.base import universal_id_pb2 as _universal_id_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf.internal import python_message as _python_message
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CRUDInfoProto(_message.Message):
    __slots__ = ("creation_time_usecs", "last_modification_time_usecs", "version")
    CREATION_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    LAST_MODIFICATION_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    creation_time_usecs: int
    last_modification_time_usecs: int
    version: int
    def __init__(self, creation_time_usecs: _Optional[int] = ..., last_modification_time_usecs: _Optional[int] = ..., version: _Optional[int] = ...) -> None: ...

class ArgumentBase(_message.Message):
    __slots__ = ("graph_name", "max_count", "pagination_cookie", "principal_name")
    GRAPH_NAME_FIELD_NUMBER: _ClassVar[int]
    MAX_COUNT_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_COOKIE_FIELD_NUMBER: _ClassVar[int]
    PRINCIPAL_NAME_FIELD_NUMBER: _ClassVar[int]
    graph_name: str
    max_count: int
    pagination_cookie: bytes
    principal_name: str
    def __init__(self, graph_name: _Optional[str] = ..., max_count: _Optional[int] = ..., pagination_cookie: _Optional[bytes] = ..., principal_name: _Optional[str] = ...) -> None: ...

class ResultBase(_message.Message):
    __slots__ = ("error", "pagination_cookie")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_COOKIE_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    pagination_cookie: bytes
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., pagination_cookie: _Optional[bytes] = ...) -> None: ...

class GraphLimitsProto(_message.Message):
    __slots__ = ("cumulative_node_inline_metadata_size_cap_bytes", "inline_attachment_size_cap_bytes", "cumulative_edge_metadata_size_cap_bytes", "open_transactions_buffer_size_bytes")
    CUMULATIVE_NODE_INLINE_METADATA_SIZE_CAP_BYTES_FIELD_NUMBER: _ClassVar[int]
    INLINE_ATTACHMENT_SIZE_CAP_BYTES_FIELD_NUMBER: _ClassVar[int]
    CUMULATIVE_EDGE_METADATA_SIZE_CAP_BYTES_FIELD_NUMBER: _ClassVar[int]
    OPEN_TRANSACTIONS_BUFFER_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    cumulative_node_inline_metadata_size_cap_bytes: int
    inline_attachment_size_cap_bytes: int
    cumulative_edge_metadata_size_cap_bytes: int
    open_transactions_buffer_size_bytes: int
    def __init__(self, cumulative_node_inline_metadata_size_cap_bytes: _Optional[int] = ..., inline_attachment_size_cap_bytes: _Optional[int] = ..., cumulative_edge_metadata_size_cap_bytes: _Optional[int] = ..., open_transactions_buffer_size_bytes: _Optional[int] = ...) -> None: ...

class GraphProto(_message.Message):
    __slots__ = ("name", "crud_info", "limits")
    NAME_FIELD_NUMBER: _ClassVar[int]
    CRUD_INFO_FIELD_NUMBER: _ClassVar[int]
    LIMITS_FIELD_NUMBER: _ClassVar[int]
    name: str
    crud_info: CRUDInfoProto
    limits: GraphLimitsProto
    def __init__(self, name: _Optional[str] = ..., crud_info: _Optional[_Union[CRUDInfoProto, _Mapping]] = ..., limits: _Optional[_Union[GraphLimitsProto, _Mapping]] = ...) -> None: ...

class CreateOrUpdateGraphArg(_message.Message):
    __slots__ = ("base", "crud_info", "config_json", "uid_generator_floor")
    BASE_FIELD_NUMBER: _ClassVar[int]
    CRUD_INFO_FIELD_NUMBER: _ClassVar[int]
    CONFIG_JSON_FIELD_NUMBER: _ClassVar[int]
    UID_GENERATOR_FLOOR_FIELD_NUMBER: _ClassVar[int]
    base: ArgumentBase
    crud_info: CRUDInfoProto
    config_json: str
    uid_generator_floor: int
    def __init__(self, base: _Optional[_Union[ArgumentBase, _Mapping]] = ..., crud_info: _Optional[_Union[CRUDInfoProto, _Mapping]] = ..., config_json: _Optional[str] = ..., uid_generator_floor: _Optional[int] = ...) -> None: ...

class CreateOrUpdateGraphResult(_message.Message):
    __slots__ = ("base", "graph")
    BASE_FIELD_NUMBER: _ClassVar[int]
    GRAPH_FIELD_NUMBER: _ClassVar[int]
    base: ResultBase
    graph: GraphProto
    def __init__(self, base: _Optional[_Union[ResultBase, _Mapping]] = ..., graph: _Optional[_Union[GraphProto, _Mapping]] = ...) -> None: ...

class SpanFsDataLocatorProto(_message.Message):
    __slots__ = ("view_name", "storage_domain_id", "path_vec")
    class Path(_message.Message):
        __slots__ = ("namespace_root_name", "path", "files_size_bytes", "sha1_checksum")
        NAMESPACE_ROOT_NAME_FIELD_NUMBER: _ClassVar[int]
        PATH_FIELD_NUMBER: _ClassVar[int]
        FILES_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
        SHA1_CHECKSUM_FIELD_NUMBER: _ClassVar[int]
        namespace_root_name: str
        path: str
        files_size_bytes: int
        sha1_checksum: bytes
        def __init__(self, namespace_root_name: _Optional[str] = ..., path: _Optional[str] = ..., files_size_bytes: _Optional[int] = ..., sha1_checksum: _Optional[bytes] = ...) -> None: ...
    VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    STORAGE_DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    PATH_VEC_FIELD_NUMBER: _ClassVar[int]
    view_name: str
    storage_domain_id: int
    path_vec: _containers.RepeatedCompositeFieldContainer[SpanFsDataLocatorProto.Path]
    def __init__(self, view_name: _Optional[str] = ..., storage_domain_id: _Optional[int] = ..., path_vec: _Optional[_Iterable[_Union[SpanFsDataLocatorProto.Path, _Mapping]]] = ...) -> None: ...

class DataLocatorProto(_message.Message):
    __slots__ = ("data_locator_type", "spanfs_data_locator")
    class LocatorType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kSpanFs: _ClassVar[DataLocatorProto.LocatorType]
        kS3: _ClassVar[DataLocatorProto.LocatorType]
    kSpanFs: DataLocatorProto.LocatorType
    kS3: DataLocatorProto.LocatorType
    DATA_LOCATOR_TYPE_FIELD_NUMBER: _ClassVar[int]
    SPANFS_DATA_LOCATOR_FIELD_NUMBER: _ClassVar[int]
    data_locator_type: DataLocatorProto.LocatorType
    spanfs_data_locator: SpanFsDataLocatorProto
    def __init__(self, data_locator_type: _Optional[_Union[DataLocatorProto.LocatorType, str]] = ..., spanfs_data_locator: _Optional[_Union[SpanFsDataLocatorProto, _Mapping]] = ...) -> None: ...

class AttachmentProto(_message.Message):
    __slots__ = ("inline_attachment", "external_attachment")
    INLINE_ATTACHMENT_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_ATTACHMENT_FIELD_NUMBER: _ClassVar[int]
    inline_attachment: bytes
    external_attachment: DataLocatorProto
    def __init__(self, inline_attachment: _Optional[bytes] = ..., external_attachment: _Optional[_Union[DataLocatorProto, _Mapping]] = ...) -> None: ...

class NodeProto(_message.Message):
    __slots__ = ("node_uid", "crud_info", "node_type", "label_vec", "int_attrs_map", "str_attrs_map", "attachment_map", "node_data", "avoid_auto_garbage_collect")
    class IntAttrsMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    class StrAttrsMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class AttachmentMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: AttachmentProto
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[AttachmentProto, _Mapping]] = ...) -> None: ...
    NODE_UID_FIELD_NUMBER: _ClassVar[int]
    CRUD_INFO_FIELD_NUMBER: _ClassVar[int]
    NODE_TYPE_FIELD_NUMBER: _ClassVar[int]
    LABEL_VEC_FIELD_NUMBER: _ClassVar[int]
    INT_ATTRS_MAP_FIELD_NUMBER: _ClassVar[int]
    STR_ATTRS_MAP_FIELD_NUMBER: _ClassVar[int]
    ATTACHMENT_MAP_FIELD_NUMBER: _ClassVar[int]
    NODE_DATA_FIELD_NUMBER: _ClassVar[int]
    AVOID_AUTO_GARBAGE_COLLECT_FIELD_NUMBER: _ClassVar[int]
    node_uid: _universal_id_pb2.UniversalIdProto
    crud_info: CRUDInfoProto
    node_type: str
    label_vec: _containers.RepeatedScalarFieldContainer[str]
    int_attrs_map: _containers.ScalarMap[str, int]
    str_attrs_map: _containers.ScalarMap[str, str]
    attachment_map: _containers.MessageMap[str, AttachmentProto]
    node_data: DataLocatorProto
    avoid_auto_garbage_collect: bool
    def __init__(self, node_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., crud_info: _Optional[_Union[CRUDInfoProto, _Mapping]] = ..., node_type: _Optional[str] = ..., label_vec: _Optional[_Iterable[str]] = ..., int_attrs_map: _Optional[_Mapping[str, int]] = ..., str_attrs_map: _Optional[_Mapping[str, str]] = ..., attachment_map: _Optional[_Mapping[str, AttachmentProto]] = ..., node_data: _Optional[_Union[DataLocatorProto, _Mapping]] = ..., avoid_auto_garbage_collect: bool = ...) -> None: ...

class EdgeIdentifierProto(_message.Message):
    __slots__ = ("from_node_uid", "to_node_uid", "edge_type")
    FROM_NODE_UID_FIELD_NUMBER: _ClassVar[int]
    TO_NODE_UID_FIELD_NUMBER: _ClassVar[int]
    EDGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    from_node_uid: _universal_id_pb2.UniversalIdProto
    to_node_uid: _universal_id_pb2.UniversalIdProto
    edge_type: str
    def __init__(self, from_node_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., to_node_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., edge_type: _Optional[str] = ...) -> None: ...

class EdgeProto(_message.Message):
    __slots__ = ("edge_id", "crud_info", "int_attrs_map", "str_attrs_map")
    class IntAttrsMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    class StrAttrsMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    EDGE_ID_FIELD_NUMBER: _ClassVar[int]
    CRUD_INFO_FIELD_NUMBER: _ClassVar[int]
    INT_ATTRS_MAP_FIELD_NUMBER: _ClassVar[int]
    STR_ATTRS_MAP_FIELD_NUMBER: _ClassVar[int]
    edge_id: EdgeIdentifierProto
    crud_info: CRUDInfoProto
    int_attrs_map: _containers.ScalarMap[str, int]
    str_attrs_map: _containers.ScalarMap[str, str]
    def __init__(self, edge_id: _Optional[_Union[EdgeIdentifierProto, _Mapping]] = ..., crud_info: _Optional[_Union[CRUDInfoProto, _Mapping]] = ..., int_attrs_map: _Optional[_Mapping[str, int]] = ..., str_attrs_map: _Optional[_Mapping[str, str]] = ...) -> None: ...

class TransactionContextProto(_message.Message):
    __slots__ = ("gandalf_session_id", "liveness_namespace", "id_str")
    GANDALF_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    LIVENESS_NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    ID_STR_FIELD_NUMBER: _ClassVar[int]
    gandalf_session_id: int
    liveness_namespace: str
    id_str: str
    def __init__(self, gandalf_session_id: _Optional[int] = ..., liveness_namespace: _Optional[str] = ..., id_str: _Optional[str] = ...) -> None: ...

class CreateTransactionContextArg(_message.Message):
    __slots__ = ("base", "transaction_context", "create_attachment_dir")
    BASE_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    CREATE_ATTACHMENT_DIR_FIELD_NUMBER: _ClassVar[int]
    base: ArgumentBase
    transaction_context: TransactionContextProto
    create_attachment_dir: bool
    def __init__(self, base: _Optional[_Union[ArgumentBase, _Mapping]] = ..., transaction_context: _Optional[_Union[TransactionContextProto, _Mapping]] = ..., create_attachment_dir: bool = ...) -> None: ...

class CreateTransactionContextResult(_message.Message):
    __slots__ = ("base", "external_attachment_dir")
    BASE_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_ATTACHMENT_DIR_FIELD_NUMBER: _ClassVar[int]
    base: ResultBase
    external_attachment_dir: DataLocatorProto
    def __init__(self, base: _Optional[_Union[ResultBase, _Mapping]] = ..., external_attachment_dir: _Optional[_Union[DataLocatorProto, _Mapping]] = ...) -> None: ...

class CommitTransactionArg(_message.Message):
    __slots__ = ("transaction_ctx", "abort", "expected_max_sequence_number")
    TRANSACTION_CTX_FIELD_NUMBER: _ClassVar[int]
    ABORT_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_MAX_SEQUENCE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    transaction_ctx: TransactionContextProto
    abort: bool
    expected_max_sequence_number: int
    def __init__(self, transaction_ctx: _Optional[_Union[TransactionContextProto, _Mapping]] = ..., abort: bool = ..., expected_max_sequence_number: _Optional[int] = ...) -> None: ...

class CommitTransactionResult(_message.Message):
    __slots__ = ("base",)
    BASE_FIELD_NUMBER: _ClassVar[int]
    base: ResultBase
    def __init__(self, base: _Optional[_Union[ResultBase, _Mapping]] = ...) -> None: ...

class ReserveUniversalIdsArg(_message.Message):
    __slots__ = ("base", "transaction_context", "num_uids", "cluster_id", "cluster_incarnation_id")
    BASE_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    NUM_UIDS_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    base: ArgumentBase
    transaction_context: TransactionContextProto
    num_uids: int
    cluster_id: int
    cluster_incarnation_id: int
    def __init__(self, base: _Optional[_Union[ArgumentBase, _Mapping]] = ..., transaction_context: _Optional[_Union[TransactionContextProto, _Mapping]] = ..., num_uids: _Optional[int] = ..., cluster_id: _Optional[int] = ..., cluster_incarnation_id: _Optional[int] = ...) -> None: ...

class ReserveUniversalIdsResult(_message.Message):
    __slots__ = ("base", "starting_object_id")
    BASE_FIELD_NUMBER: _ClassVar[int]
    STARTING_OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    base: ResultBase
    starting_object_id: int
    def __init__(self, base: _Optional[_Union[ResultBase, _Mapping]] = ..., starting_object_id: _Optional[int] = ...) -> None: ...

class UpdateNodeProto(_message.Message):
    __slots__ = ("node_uid", "crud_info", "node_type", "add_label_vec", "remove_label_vec", "add_or_update_int_attrs_map", "add_or_update_str_attrs_map", "remove_attr_key_vec", "add_or_update_attachments_map", "remove_attachment_key_vec", "avoid_auto_garbage_collect")
    class AddOrUpdateIntAttrsMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    class AddOrUpdateStrAttrsMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class AddOrUpdateAttachmentsMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: AttachmentProto
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[AttachmentProto, _Mapping]] = ...) -> None: ...
    NODE_UID_FIELD_NUMBER: _ClassVar[int]
    CRUD_INFO_FIELD_NUMBER: _ClassVar[int]
    NODE_TYPE_FIELD_NUMBER: _ClassVar[int]
    ADD_LABEL_VEC_FIELD_NUMBER: _ClassVar[int]
    REMOVE_LABEL_VEC_FIELD_NUMBER: _ClassVar[int]
    ADD_OR_UPDATE_INT_ATTRS_MAP_FIELD_NUMBER: _ClassVar[int]
    ADD_OR_UPDATE_STR_ATTRS_MAP_FIELD_NUMBER: _ClassVar[int]
    REMOVE_ATTR_KEY_VEC_FIELD_NUMBER: _ClassVar[int]
    ADD_OR_UPDATE_ATTACHMENTS_MAP_FIELD_NUMBER: _ClassVar[int]
    REMOVE_ATTACHMENT_KEY_VEC_FIELD_NUMBER: _ClassVar[int]
    AVOID_AUTO_GARBAGE_COLLECT_FIELD_NUMBER: _ClassVar[int]
    node_uid: _universal_id_pb2.UniversalIdProto
    crud_info: CRUDInfoProto
    node_type: str
    add_label_vec: _containers.RepeatedScalarFieldContainer[str]
    remove_label_vec: _containers.RepeatedScalarFieldContainer[str]
    add_or_update_int_attrs_map: _containers.ScalarMap[str, int]
    add_or_update_str_attrs_map: _containers.ScalarMap[str, str]
    remove_attr_key_vec: _containers.RepeatedScalarFieldContainer[str]
    add_or_update_attachments_map: _containers.MessageMap[str, AttachmentProto]
    remove_attachment_key_vec: _containers.RepeatedScalarFieldContainer[str]
    avoid_auto_garbage_collect: bool
    def __init__(self, node_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., crud_info: _Optional[_Union[CRUDInfoProto, _Mapping]] = ..., node_type: _Optional[str] = ..., add_label_vec: _Optional[_Iterable[str]] = ..., remove_label_vec: _Optional[_Iterable[str]] = ..., add_or_update_int_attrs_map: _Optional[_Mapping[str, int]] = ..., add_or_update_str_attrs_map: _Optional[_Mapping[str, str]] = ..., remove_attr_key_vec: _Optional[_Iterable[str]] = ..., add_or_update_attachments_map: _Optional[_Mapping[str, AttachmentProto]] = ..., remove_attachment_key_vec: _Optional[_Iterable[str]] = ..., avoid_auto_garbage_collect: bool = ...) -> None: ...

class AddEdgeProto(_message.Message):
    __slots__ = ("edge", "expected_from_node_version", "expected_to_node_version", "from_node_type", "to_node_type")
    EDGE_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_FROM_NODE_VERSION_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_TO_NODE_VERSION_FIELD_NUMBER: _ClassVar[int]
    FROM_NODE_TYPE_FIELD_NUMBER: _ClassVar[int]
    TO_NODE_TYPE_FIELD_NUMBER: _ClassVar[int]
    edge: EdgeProto
    expected_from_node_version: int
    expected_to_node_version: int
    from_node_type: str
    to_node_type: str
    def __init__(self, edge: _Optional[_Union[EdgeProto, _Mapping]] = ..., expected_from_node_version: _Optional[int] = ..., expected_to_node_version: _Optional[int] = ..., from_node_type: _Optional[str] = ..., to_node_type: _Optional[str] = ...) -> None: ...

class AddNodeProto(_message.Message):
    __slots__ = ("node", "primary_key_attr_name_vec")
    NODE_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_KEY_ATTR_NAME_VEC_FIELD_NUMBER: _ClassVar[int]
    node: NodeProto
    primary_key_attr_name_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, node: _Optional[_Union[NodeProto, _Mapping]] = ..., primary_key_attr_name_vec: _Optional[_Iterable[str]] = ...) -> None: ...

class UpdateEdgeProto(_message.Message):
    __slots__ = ("edge_id", "crud_info", "add_or_update_int_attrs_map", "add_or_update_str_attrs_map", "remove_attr_key_vec", "expected_from_node_version", "expected_to_node_version", "from_node_type", "to_node_type")
    class AddOrUpdateIntAttrsMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    class AddOrUpdateStrAttrsMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    EDGE_ID_FIELD_NUMBER: _ClassVar[int]
    CRUD_INFO_FIELD_NUMBER: _ClassVar[int]
    ADD_OR_UPDATE_INT_ATTRS_MAP_FIELD_NUMBER: _ClassVar[int]
    ADD_OR_UPDATE_STR_ATTRS_MAP_FIELD_NUMBER: _ClassVar[int]
    REMOVE_ATTR_KEY_VEC_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_FROM_NODE_VERSION_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_TO_NODE_VERSION_FIELD_NUMBER: _ClassVar[int]
    FROM_NODE_TYPE_FIELD_NUMBER: _ClassVar[int]
    TO_NODE_TYPE_FIELD_NUMBER: _ClassVar[int]
    edge_id: EdgeIdentifierProto
    crud_info: CRUDInfoProto
    add_or_update_int_attrs_map: _containers.ScalarMap[str, int]
    add_or_update_str_attrs_map: _containers.ScalarMap[str, str]
    remove_attr_key_vec: _containers.RepeatedScalarFieldContainer[str]
    expected_from_node_version: int
    expected_to_node_version: int
    from_node_type: str
    to_node_type: str
    def __init__(self, edge_id: _Optional[_Union[EdgeIdentifierProto, _Mapping]] = ..., crud_info: _Optional[_Union[CRUDInfoProto, _Mapping]] = ..., add_or_update_int_attrs_map: _Optional[_Mapping[str, int]] = ..., add_or_update_str_attrs_map: _Optional[_Mapping[str, str]] = ..., remove_attr_key_vec: _Optional[_Iterable[str]] = ..., expected_from_node_version: _Optional[int] = ..., expected_to_node_version: _Optional[int] = ..., from_node_type: _Optional[str] = ..., to_node_type: _Optional[str] = ...) -> None: ...

class DeleteEdgeProto(_message.Message):
    __slots__ = ("edge_id", "crud_info", "expected_from_node_version", "expected_to_node_version", "from_node_type", "to_node_type")
    EDGE_ID_FIELD_NUMBER: _ClassVar[int]
    CRUD_INFO_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_FROM_NODE_VERSION_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_TO_NODE_VERSION_FIELD_NUMBER: _ClassVar[int]
    FROM_NODE_TYPE_FIELD_NUMBER: _ClassVar[int]
    TO_NODE_TYPE_FIELD_NUMBER: _ClassVar[int]
    edge_id: EdgeIdentifierProto
    crud_info: CRUDInfoProto
    expected_from_node_version: int
    expected_to_node_version: int
    from_node_type: str
    to_node_type: str
    def __init__(self, edge_id: _Optional[_Union[EdgeIdentifierProto, _Mapping]] = ..., crud_info: _Optional[_Union[CRUDInfoProto, _Mapping]] = ..., expected_from_node_version: _Optional[int] = ..., expected_to_node_version: _Optional[int] = ..., from_node_type: _Optional[str] = ..., to_node_type: _Optional[str] = ...) -> None: ...

class AddBatchToTransactionArg(_message.Message):
    __slots__ = ("base", "transaction_context", "sequence_number", "add_node_vec", "add_edge_vec", "update_node_vec", "update_edge_vec", "delete_edge_vec")
    BASE_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    SEQUENCE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    ADD_NODE_VEC_FIELD_NUMBER: _ClassVar[int]
    ADD_EDGE_VEC_FIELD_NUMBER: _ClassVar[int]
    UPDATE_NODE_VEC_FIELD_NUMBER: _ClassVar[int]
    UPDATE_EDGE_VEC_FIELD_NUMBER: _ClassVar[int]
    DELETE_EDGE_VEC_FIELD_NUMBER: _ClassVar[int]
    base: ArgumentBase
    transaction_context: TransactionContextProto
    sequence_number: int
    add_node_vec: _containers.RepeatedCompositeFieldContainer[AddNodeProto]
    add_edge_vec: _containers.RepeatedCompositeFieldContainer[AddEdgeProto]
    update_node_vec: _containers.RepeatedCompositeFieldContainer[UpdateNodeProto]
    update_edge_vec: _containers.RepeatedCompositeFieldContainer[UpdateEdgeProto]
    delete_edge_vec: _containers.RepeatedCompositeFieldContainer[DeleteEdgeProto]
    def __init__(self, base: _Optional[_Union[ArgumentBase, _Mapping]] = ..., transaction_context: _Optional[_Union[TransactionContextProto, _Mapping]] = ..., sequence_number: _Optional[int] = ..., add_node_vec: _Optional[_Iterable[_Union[AddNodeProto, _Mapping]]] = ..., add_edge_vec: _Optional[_Iterable[_Union[AddEdgeProto, _Mapping]]] = ..., update_node_vec: _Optional[_Iterable[_Union[UpdateNodeProto, _Mapping]]] = ..., update_edge_vec: _Optional[_Iterable[_Union[UpdateEdgeProto, _Mapping]]] = ..., delete_edge_vec: _Optional[_Iterable[_Union[DeleteEdgeProto, _Mapping]]] = ...) -> None: ...

class AddBatchToTransactionResult(_message.Message):
    __slots__ = ("base",)
    BASE_FIELD_NUMBER: _ClassVar[int]
    base: ResultBase
    def __init__(self, base: _Optional[_Union[ResultBase, _Mapping]] = ...) -> None: ...

class FilterProto(_message.Message):
    __slots__ = ("match_type_vec", "match_label_vec", "match_attr_vec")
    class ValueList(_message.Message):
        __slots__ = ("str_val_list", "int_val_list")
        STR_VAL_LIST_FIELD_NUMBER: _ClassVar[int]
        INT_VAL_LIST_FIELD_NUMBER: _ClassVar[int]
        str_val_list: _containers.RepeatedScalarFieldContainer[str]
        int_val_list: _containers.RepeatedScalarFieldContainer[int]
        def __init__(self, str_val_list: _Optional[_Iterable[str]] = ..., int_val_list: _Optional[_Iterable[int]] = ...) -> None: ...
    class IntValueRange(_message.Message):
        __slots__ = ("lower_bound", "upper_bound")
        LOWER_BOUND_FIELD_NUMBER: _ClassVar[int]
        UPPER_BOUND_FIELD_NUMBER: _ClassVar[int]
        lower_bound: int
        upper_bound: int
        def __init__(self, lower_bound: _Optional[int] = ..., upper_bound: _Optional[int] = ...) -> None: ...
    class MatchAttr(_message.Message):
        __slots__ = ("match_type", "attr_name", "attr_value_list", "attr_value_range")
        MATCH_TYPE_FIELD_NUMBER: _ClassVar[int]
        ATTR_NAME_FIELD_NUMBER: _ClassVar[int]
        ATTR_VALUE_LIST_FIELD_NUMBER: _ClassVar[int]
        ATTR_VALUE_RANGE_FIELD_NUMBER: _ClassVar[int]
        match_type: str
        attr_name: str
        attr_value_list: FilterProto.ValueList
        attr_value_range: FilterProto.IntValueRange
        def __init__(self, match_type: _Optional[str] = ..., attr_name: _Optional[str] = ..., attr_value_list: _Optional[_Union[FilterProto.ValueList, _Mapping]] = ..., attr_value_range: _Optional[_Union[FilterProto.IntValueRange, _Mapping]] = ...) -> None: ...
    MATCH_TYPE_VEC_FIELD_NUMBER: _ClassVar[int]
    MATCH_LABEL_VEC_FIELD_NUMBER: _ClassVar[int]
    MATCH_ATTR_VEC_FIELD_NUMBER: _ClassVar[int]
    match_type_vec: _containers.RepeatedScalarFieldContainer[str]
    match_label_vec: _containers.RepeatedScalarFieldContainer[str]
    match_attr_vec: _containers.RepeatedCompositeFieldContainer[FilterProto.MatchAttr]
    def __init__(self, match_type_vec: _Optional[_Iterable[str]] = ..., match_label_vec: _Optional[_Iterable[str]] = ..., match_attr_vec: _Optional[_Iterable[_Union[FilterProto.MatchAttr, _Mapping]]] = ...) -> None: ...

class TraverseNeighborsFilterProto(_message.Message):
    __slots__ = ("edge_filter", "neighbor_node_filter_vec", "fetch_neighbor_node_info", "order_by_attr_key", "order_ascending", "attr_key_vec")
    class EdgeFilter(_message.Message):
        __slots__ = ("incoming", "outgoing", "filter_vec")
        INCOMING_FIELD_NUMBER: _ClassVar[int]
        OUTGOING_FIELD_NUMBER: _ClassVar[int]
        FILTER_VEC_FIELD_NUMBER: _ClassVar[int]
        incoming: bool
        outgoing: bool
        filter_vec: _containers.RepeatedCompositeFieldContainer[FilterProto]
        def __init__(self, incoming: bool = ..., outgoing: bool = ..., filter_vec: _Optional[_Iterable[_Union[FilterProto, _Mapping]]] = ...) -> None: ...
    EDGE_FILTER_FIELD_NUMBER: _ClassVar[int]
    NEIGHBOR_NODE_FILTER_VEC_FIELD_NUMBER: _ClassVar[int]
    FETCH_NEIGHBOR_NODE_INFO_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_ATTR_KEY_FIELD_NUMBER: _ClassVar[int]
    ORDER_ASCENDING_FIELD_NUMBER: _ClassVar[int]
    ATTR_KEY_VEC_FIELD_NUMBER: _ClassVar[int]
    edge_filter: TraverseNeighborsFilterProto.EdgeFilter
    neighbor_node_filter_vec: _containers.RepeatedCompositeFieldContainer[FilterProto]
    fetch_neighbor_node_info: bool
    order_by_attr_key: str
    order_ascending: bool
    attr_key_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, edge_filter: _Optional[_Union[TraverseNeighborsFilterProto.EdgeFilter, _Mapping]] = ..., neighbor_node_filter_vec: _Optional[_Iterable[_Union[FilterProto, _Mapping]]] = ..., fetch_neighbor_node_info: bool = ..., order_by_attr_key: _Optional[str] = ..., order_ascending: bool = ..., attr_key_vec: _Optional[_Iterable[str]] = ...) -> None: ...

class NeighborNodeEdgePairProto(_message.Message):
    __slots__ = ("neighbor_node_uid", "neighbor_node", "edge")
    NEIGHBOR_NODE_UID_FIELD_NUMBER: _ClassVar[int]
    NEIGHBOR_NODE_FIELD_NUMBER: _ClassVar[int]
    EDGE_FIELD_NUMBER: _ClassVar[int]
    neighbor_node_uid: _universal_id_pb2.UniversalIdProto
    neighbor_node: NodeProto
    edge: EdgeProto
    def __init__(self, neighbor_node_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., neighbor_node: _Optional[_Union[NodeProto, _Mapping]] = ..., edge: _Optional[_Union[EdgeProto, _Mapping]] = ...) -> None: ...

class LookupNodesArg(_message.Message):
    __slots__ = ("base", "transaction_context", "node_vec", "filter_vec", "fetch_node_info", "num_neighbors_to_fetch", "neighbor_traversal_filter")
    class NodeArg(_message.Message):
        __slots__ = ("node_type", "uid")
        NODE_TYPE_FIELD_NUMBER: _ClassVar[int]
        UID_FIELD_NUMBER: _ClassVar[int]
        node_type: str
        uid: _universal_id_pb2.UniversalIdProto
        def __init__(self, node_type: _Optional[str] = ..., uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ...) -> None: ...
    BASE_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    NODE_VEC_FIELD_NUMBER: _ClassVar[int]
    FILTER_VEC_FIELD_NUMBER: _ClassVar[int]
    FETCH_NODE_INFO_FIELD_NUMBER: _ClassVar[int]
    NUM_NEIGHBORS_TO_FETCH_FIELD_NUMBER: _ClassVar[int]
    NEIGHBOR_TRAVERSAL_FILTER_FIELD_NUMBER: _ClassVar[int]
    base: ArgumentBase
    transaction_context: TransactionContextProto
    node_vec: _containers.RepeatedCompositeFieldContainer[LookupNodesArg.NodeArg]
    filter_vec: _containers.RepeatedCompositeFieldContainer[FilterProto]
    fetch_node_info: bool
    num_neighbors_to_fetch: int
    neighbor_traversal_filter: TraverseNeighborsFilterProto
    def __init__(self, base: _Optional[_Union[ArgumentBase, _Mapping]] = ..., transaction_context: _Optional[_Union[TransactionContextProto, _Mapping]] = ..., node_vec: _Optional[_Iterable[_Union[LookupNodesArg.NodeArg, _Mapping]]] = ..., filter_vec: _Optional[_Iterable[_Union[FilterProto, _Mapping]]] = ..., fetch_node_info: bool = ..., num_neighbors_to_fetch: _Optional[int] = ..., neighbor_traversal_filter: _Optional[_Union[TraverseNeighborsFilterProto, _Mapping]] = ...) -> None: ...

class LookupNodesResult(_message.Message):
    __slots__ = ("base", "result_vec")
    class Result(_message.Message):
        __slots__ = ("node_uid", "error", "node", "neighbor_node_edge_pair_vec", "total_neighbor_count")
        NODE_UID_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        NODE_FIELD_NUMBER: _ClassVar[int]
        NEIGHBOR_NODE_EDGE_PAIR_VEC_FIELD_NUMBER: _ClassVar[int]
        TOTAL_NEIGHBOR_COUNT_FIELD_NUMBER: _ClassVar[int]
        node_uid: _universal_id_pb2.UniversalIdProto
        error: _error_pb2.ErrorProto
        node: NodeProto
        neighbor_node_edge_pair_vec: _containers.RepeatedCompositeFieldContainer[NeighborNodeEdgePairProto]
        total_neighbor_count: int
        def __init__(self, node_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., node: _Optional[_Union[NodeProto, _Mapping]] = ..., neighbor_node_edge_pair_vec: _Optional[_Iterable[_Union[NeighborNodeEdgePairProto, _Mapping]]] = ..., total_neighbor_count: _Optional[int] = ...) -> None: ...
    BASE_FIELD_NUMBER: _ClassVar[int]
    RESULT_VEC_FIELD_NUMBER: _ClassVar[int]
    base: ResultBase
    result_vec: _containers.RepeatedCompositeFieldContainer[LookupNodesResult.Result]
    def __init__(self, base: _Optional[_Union[ResultBase, _Mapping]] = ..., result_vec: _Optional[_Iterable[_Union[LookupNodesResult.Result, _Mapping]]] = ...) -> None: ...

class TraverseNeighborsOfNodeArg(_message.Message):
    __slots__ = ("base", "transaction_context", "node_uid", "node_type", "neighbor_traversal_filter", "count_only")
    BASE_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    NODE_UID_FIELD_NUMBER: _ClassVar[int]
    NODE_TYPE_FIELD_NUMBER: _ClassVar[int]
    NEIGHBOR_TRAVERSAL_FILTER_FIELD_NUMBER: _ClassVar[int]
    COUNT_ONLY_FIELD_NUMBER: _ClassVar[int]
    base: ArgumentBase
    transaction_context: TransactionContextProto
    node_uid: _universal_id_pb2.UniversalIdProto
    node_type: str
    neighbor_traversal_filter: TraverseNeighborsFilterProto
    count_only: bool
    def __init__(self, base: _Optional[_Union[ArgumentBase, _Mapping]] = ..., transaction_context: _Optional[_Union[TransactionContextProto, _Mapping]] = ..., node_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., node_type: _Optional[str] = ..., neighbor_traversal_filter: _Optional[_Union[TraverseNeighborsFilterProto, _Mapping]] = ..., count_only: bool = ...) -> None: ...

class TraverseNeighborsOfNodeResult(_message.Message):
    __slots__ = ("base", "num_matching_neighbors", "neighbor_node_edge_pair_vec")
    BASE_FIELD_NUMBER: _ClassVar[int]
    NUM_MATCHING_NEIGHBORS_FIELD_NUMBER: _ClassVar[int]
    NEIGHBOR_NODE_EDGE_PAIR_VEC_FIELD_NUMBER: _ClassVar[int]
    base: ResultBase
    num_matching_neighbors: int
    neighbor_node_edge_pair_vec: _containers.RepeatedCompositeFieldContainer[NeighborNodeEdgePairProto]
    def __init__(self, base: _Optional[_Union[ResultBase, _Mapping]] = ..., num_matching_neighbors: _Optional[int] = ..., neighbor_node_edge_pair_vec: _Optional[_Iterable[_Union[NeighborNodeEdgePairProto, _Mapping]]] = ...) -> None: ...

class FetchDagArg(_message.Message):
    __slots__ = ("base", "transaction_context", "node_type", "root_node_uid", "edge_type", "label_vec", "attr_key_vec", "num_levels")
    BASE_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    NODE_TYPE_FIELD_NUMBER: _ClassVar[int]
    ROOT_NODE_UID_FIELD_NUMBER: _ClassVar[int]
    EDGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    LABEL_VEC_FIELD_NUMBER: _ClassVar[int]
    ATTR_KEY_VEC_FIELD_NUMBER: _ClassVar[int]
    NUM_LEVELS_FIELD_NUMBER: _ClassVar[int]
    base: ArgumentBase
    transaction_context: TransactionContextProto
    node_type: str
    root_node_uid: _universal_id_pb2.UniversalIdProto
    edge_type: str
    label_vec: _containers.RepeatedScalarFieldContainer[str]
    attr_key_vec: _containers.RepeatedScalarFieldContainer[str]
    num_levels: int
    def __init__(self, base: _Optional[_Union[ArgumentBase, _Mapping]] = ..., transaction_context: _Optional[_Union[TransactionContextProto, _Mapping]] = ..., node_type: _Optional[str] = ..., root_node_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., edge_type: _Optional[str] = ..., label_vec: _Optional[_Iterable[str]] = ..., attr_key_vec: _Optional[_Iterable[str]] = ..., num_levels: _Optional[int] = ...) -> None: ...

class FetchDagResult(_message.Message):
    __slots__ = ("base", "root_node_index", "dag_node_vec")
    class DagEdge(_message.Message):
        __slots__ = ("edge_version", "dest_node_index")
        EDGE_VERSION_FIELD_NUMBER: _ClassVar[int]
        DEST_NODE_INDEX_FIELD_NUMBER: _ClassVar[int]
        edge_version: int
        dest_node_index: int
        def __init__(self, edge_version: _Optional[int] = ..., dest_node_index: _Optional[int] = ...) -> None: ...
    class DagNode(_message.Message):
        __slots__ = ("node", "dag_edge_vec")
        NODE_FIELD_NUMBER: _ClassVar[int]
        DAG_EDGE_VEC_FIELD_NUMBER: _ClassVar[int]
        node: NodeProto
        dag_edge_vec: _containers.RepeatedCompositeFieldContainer[FetchDagResult.DagEdge]
        def __init__(self, node: _Optional[_Union[NodeProto, _Mapping]] = ..., dag_edge_vec: _Optional[_Iterable[_Union[FetchDagResult.DagEdge, _Mapping]]] = ...) -> None: ...
    BASE_FIELD_NUMBER: _ClassVar[int]
    ROOT_NODE_INDEX_FIELD_NUMBER: _ClassVar[int]
    DAG_NODE_VEC_FIELD_NUMBER: _ClassVar[int]
    base: ResultBase
    root_node_index: int
    dag_node_vec: _containers.RepeatedCompositeFieldContainer[FetchDagResult.DagNode]
    def __init__(self, base: _Optional[_Union[ResultBase, _Mapping]] = ..., root_node_index: _Optional[int] = ..., dag_node_vec: _Optional[_Iterable[_Union[FetchDagResult.DagNode, _Mapping]]] = ...) -> None: ...

class TraverseDagArg(_message.Message):
    __slots__ = ("base", "transaction_context", "node_type", "root_node_uid", "num_levels", "traverse_type", "neighbor_node_filter", "root_component_only")
    class TraverseType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNone: _ClassVar[TraverseDagArg.TraverseType]
        kBFS: _ClassVar[TraverseDagArg.TraverseType]
    kNone: TraverseDagArg.TraverseType
    kBFS: TraverseDagArg.TraverseType
    BASE_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    NODE_TYPE_FIELD_NUMBER: _ClassVar[int]
    ROOT_NODE_UID_FIELD_NUMBER: _ClassVar[int]
    NUM_LEVELS_FIELD_NUMBER: _ClassVar[int]
    TRAVERSE_TYPE_FIELD_NUMBER: _ClassVar[int]
    NEIGHBOR_NODE_FILTER_FIELD_NUMBER: _ClassVar[int]
    ROOT_COMPONENT_ONLY_FIELD_NUMBER: _ClassVar[int]
    base: ArgumentBase
    transaction_context: TransactionContextProto
    node_type: str
    root_node_uid: _universal_id_pb2.UniversalIdProto
    num_levels: int
    traverse_type: TraverseDagArg.TraverseType
    neighbor_node_filter: TraverseNeighborsFilterProto
    root_component_only: bool
    def __init__(self, base: _Optional[_Union[ArgumentBase, _Mapping]] = ..., transaction_context: _Optional[_Union[TransactionContextProto, _Mapping]] = ..., node_type: _Optional[str] = ..., root_node_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., num_levels: _Optional[int] = ..., traverse_type: _Optional[_Union[TraverseDagArg.TraverseType, str]] = ..., neighbor_node_filter: _Optional[_Union[TraverseNeighborsFilterProto, _Mapping]] = ..., root_component_only: bool = ...) -> None: ...

class TraverseDagResult(_message.Message):
    __slots__ = ("base", "node_vec")
    BASE_FIELD_NUMBER: _ClassVar[int]
    NODE_VEC_FIELD_NUMBER: _ClassVar[int]
    base: ResultBase
    node_vec: _containers.RepeatedCompositeFieldContainer[NodeProto]
    def __init__(self, base: _Optional[_Union[ResultBase, _Mapping]] = ..., node_vec: _Optional[_Iterable[_Union[NodeProto, _Mapping]]] = ...) -> None: ...

class ConstantsProto(_message.Message):
    __slots__ = ("reserved_chars",)
    RESERVED_CHARS_FIELD_NUMBER: _ClassVar[int]
    reserved_chars: str
    def __init__(self, reserved_chars: _Optional[str] = ...) -> None: ...

class ExecuteStoredProcedureArg(_message.Message):
    __slots__ = ("base", "transaction_context", "stored_procedure_exec_relative_path")
    Extensions: _python_message._ExtensionDict
    BASE_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    STORED_PROCEDURE_EXEC_RELATIVE_PATH_FIELD_NUMBER: _ClassVar[int]
    base: ArgumentBase
    transaction_context: TransactionContextProto
    stored_procedure_exec_relative_path: str
    def __init__(self, base: _Optional[_Union[ArgumentBase, _Mapping]] = ..., transaction_context: _Optional[_Union[TransactionContextProto, _Mapping]] = ..., stored_procedure_exec_relative_path: _Optional[str] = ...) -> None: ...

class ExecuteStoredProcedureResult(_message.Message):
    __slots__ = ("base", "fetchdag_result")
    BASE_FIELD_NUMBER: _ClassVar[int]
    FETCHDAG_RESULT_FIELD_NUMBER: _ClassVar[int]
    base: ResultBase
    fetchdag_result: FetchDagResult
    def __init__(self, base: _Optional[_Union[ResultBase, _Mapping]] = ..., fetchdag_result: _Optional[_Union[FetchDagResult, _Mapping]] = ...) -> None: ...
