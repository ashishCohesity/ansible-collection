from util.base import universal_id_pb2 as _universal_id_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AttributeProto(_message.Message):
    __slots__ = ("name", "str_val", "int_val")
    NAME_FIELD_NUMBER: _ClassVar[int]
    STR_VAL_FIELD_NUMBER: _ClassVar[int]
    INT_VAL_FIELD_NUMBER: _ClassVar[int]
    name: str
    str_val: bytes
    int_val: int
    def __init__(self, name: _Optional[str] = ..., str_val: _Optional[bytes] = ..., int_val: _Optional[int] = ...) -> None: ...

class EdgeProto(_message.Message):
    __slots__ = ("uid", "from_node_uid", "to_node_uid", "type", "attribute_vec")
    UID_FIELD_NUMBER: _ClassVar[int]
    FROM_NODE_UID_FIELD_NUMBER: _ClassVar[int]
    TO_NODE_UID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTE_VEC_FIELD_NUMBER: _ClassVar[int]
    uid: _universal_id_pb2.UniversalIdProto
    from_node_uid: _universal_id_pb2.UniversalIdProto
    to_node_uid: _universal_id_pb2.UniversalIdProto
    type: str
    attribute_vec: _containers.RepeatedCompositeFieldContainer[AttributeProto]
    def __init__(self, uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., from_node_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., to_node_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., type: _Optional[str] = ..., attribute_vec: _Optional[_Iterable[_Union[AttributeProto, _Mapping]]] = ...) -> None: ...

class NodeProto(_message.Message):
    __slots__ = ("uid", "attribute_vec", "label_vec", "opaque_data")
    UID_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTE_VEC_FIELD_NUMBER: _ClassVar[int]
    LABEL_VEC_FIELD_NUMBER: _ClassVar[int]
    OPAQUE_DATA_FIELD_NUMBER: _ClassVar[int]
    uid: _universal_id_pb2.UniversalIdProto
    attribute_vec: _containers.RepeatedCompositeFieldContainer[AttributeProto]
    label_vec: _containers.RepeatedScalarFieldContainer[str]
    opaque_data: bytes
    def __init__(self, uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., attribute_vec: _Optional[_Iterable[_Union[AttributeProto, _Mapping]]] = ..., label_vec: _Optional[_Iterable[str]] = ..., opaque_data: _Optional[bytes] = ...) -> None: ...

class IndexProto(_message.Message):
    __slots__ = ("name", "label", "node_attribute_name_vec")
    NAME_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    NODE_ATTRIBUTE_NAME_VEC_FIELD_NUMBER: _ClassVar[int]
    name: str
    label: str
    node_attribute_name_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, name: _Optional[str] = ..., label: _Optional[str] = ..., node_attribute_name_vec: _Optional[_Iterable[str]] = ...) -> None: ...

class GraphCheckpointProto(_message.Message):
    __slots__ = ("graph_name", "node_vec", "edge_vec", "next_local_id", "index_vec")
    GRAPH_NAME_FIELD_NUMBER: _ClassVar[int]
    NODE_VEC_FIELD_NUMBER: _ClassVar[int]
    EDGE_VEC_FIELD_NUMBER: _ClassVar[int]
    NEXT_LOCAL_ID_FIELD_NUMBER: _ClassVar[int]
    INDEX_VEC_FIELD_NUMBER: _ClassVar[int]
    graph_name: str
    node_vec: _containers.RepeatedCompositeFieldContainer[NodeProto]
    edge_vec: _containers.RepeatedCompositeFieldContainer[EdgeProto]
    next_local_id: int
    index_vec: _containers.RepeatedCompositeFieldContainer[IndexProto]
    def __init__(self, graph_name: _Optional[str] = ..., node_vec: _Optional[_Iterable[_Union[NodeProto, _Mapping]]] = ..., edge_vec: _Optional[_Iterable[_Union[EdgeProto, _Mapping]]] = ..., next_local_id: _Optional[int] = ..., index_vec: _Optional[_Iterable[_Union[IndexProto, _Mapping]]] = ...) -> None: ...

class BatchUpdaterActionProto(_message.Message):
    __slots__ = ("add_update_node", "delete_node_uid", "add_update_edge", "delete_edge_uid")
    ADD_UPDATE_NODE_FIELD_NUMBER: _ClassVar[int]
    DELETE_NODE_UID_FIELD_NUMBER: _ClassVar[int]
    ADD_UPDATE_EDGE_FIELD_NUMBER: _ClassVar[int]
    DELETE_EDGE_UID_FIELD_NUMBER: _ClassVar[int]
    add_update_node: NodeProto
    delete_node_uid: _universal_id_pb2.UniversalIdProto
    add_update_edge: EdgeProto
    delete_edge_uid: _universal_id_pb2.UniversalIdProto
    def __init__(self, add_update_node: _Optional[_Union[NodeProto, _Mapping]] = ..., delete_node_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., add_update_edge: _Optional[_Union[EdgeProto, _Mapping]] = ..., delete_edge_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ...) -> None: ...

class WALRecordProto(_message.Message):
    __slots__ = ("version", "graph_db_vec", "graph_name", "create_graph", "delete_graph", "add_update_node", "delete_node_uid", "add_update_edge", "delete_edge_uid", "num_uids_reserved", "create_index", "drop_index", "batch_update_vec")
    class CreateGraph(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    VERSION_FIELD_NUMBER: _ClassVar[int]
    GRAPH_DB_VEC_FIELD_NUMBER: _ClassVar[int]
    GRAPH_NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_GRAPH_FIELD_NUMBER: _ClassVar[int]
    DELETE_GRAPH_FIELD_NUMBER: _ClassVar[int]
    ADD_UPDATE_NODE_FIELD_NUMBER: _ClassVar[int]
    DELETE_NODE_UID_FIELD_NUMBER: _ClassVar[int]
    ADD_UPDATE_EDGE_FIELD_NUMBER: _ClassVar[int]
    DELETE_EDGE_UID_FIELD_NUMBER: _ClassVar[int]
    NUM_UIDS_RESERVED_FIELD_NUMBER: _ClassVar[int]
    CREATE_INDEX_FIELD_NUMBER: _ClassVar[int]
    DROP_INDEX_FIELD_NUMBER: _ClassVar[int]
    BATCH_UPDATE_VEC_FIELD_NUMBER: _ClassVar[int]
    version: int
    graph_db_vec: _containers.RepeatedCompositeFieldContainer[GraphCheckpointProto]
    graph_name: str
    create_graph: WALRecordProto.CreateGraph
    delete_graph: bool
    add_update_node: NodeProto
    delete_node_uid: _universal_id_pb2.UniversalIdProto
    add_update_edge: EdgeProto
    delete_edge_uid: _universal_id_pb2.UniversalIdProto
    num_uids_reserved: int
    create_index: IndexProto
    drop_index: str
    batch_update_vec: _containers.RepeatedCompositeFieldContainer[BatchUpdaterActionProto]
    def __init__(self, version: _Optional[int] = ..., graph_db_vec: _Optional[_Iterable[_Union[GraphCheckpointProto, _Mapping]]] = ..., graph_name: _Optional[str] = ..., create_graph: _Optional[_Union[WALRecordProto.CreateGraph, _Mapping]] = ..., delete_graph: bool = ..., add_update_node: _Optional[_Union[NodeProto, _Mapping]] = ..., delete_node_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., add_update_edge: _Optional[_Union[EdgeProto, _Mapping]] = ..., delete_edge_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., num_uids_reserved: _Optional[int] = ..., create_index: _Optional[_Union[IndexProto, _Mapping]] = ..., drop_index: _Optional[str] = ..., batch_update_vec: _Optional[_Iterable[_Union[BatchUpdaterActionProto, _Mapping]]] = ...) -> None: ...
