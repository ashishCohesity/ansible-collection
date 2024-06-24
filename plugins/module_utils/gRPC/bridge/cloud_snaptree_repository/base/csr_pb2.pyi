from bridge.cloud_snaptree_repository.stub import csr_pb2 as _csr_pb2
from bridge.cloud_snaptree_repository.server import cloud_object_pb2 as _cloud_object_pb2
from bridge.vault.base import worm_pb2 as _worm_pb2
from util.base import op_clock_pb2 as _op_clock_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class KeysStateProto(_message.Message):
    __slots__ = ("key_state_vec",)
    class KeyState(_message.Message):
        __slots__ = ("key", "max_id")
        KEY_FIELD_NUMBER: _ClassVar[int]
        MAX_ID_FIELD_NUMBER: _ClassVar[int]
        key: _csr_pb2.FetchCloudObjectIdsArg.Key
        max_id: int
        def __init__(self, key: _Optional[_Union[_csr_pb2.FetchCloudObjectIdsArg.Key, str]] = ..., max_id: _Optional[int] = ...) -> None: ...
    KEY_STATE_VEC_FIELD_NUMBER: _ClassVar[int]
    key_state_vec: _containers.RepeatedCompositeFieldContainer[KeysStateProto.KeyState]
    def __init__(self, key_state_vec: _Optional[_Iterable[_Union[KeysStateProto.KeyState, _Mapping]]] = ...) -> None: ...

class CloudObjectScribeMetadataProto(_message.Message):
    __slots__ = ("epoch_id", "opclock_vec", "last_update_time_usecs", "cloud_object_version", "cloud_object_type", "prefix", "object_info", "intent_id_generator", "update_intent_session_id", "update_intent", "is_deleted", "num_deleted_nodes", "minimum_retention_timestamp_secs", "retention_mode", "worm_retention_extendability_info", "versioned_object_id")
    class ObjectInfo(_message.Message):
        __slots__ = ("segment_count", "entry_count", "morphed_size")
        SEGMENT_COUNT_FIELD_NUMBER: _ClassVar[int]
        ENTRY_COUNT_FIELD_NUMBER: _ClassVar[int]
        MORPHED_SIZE_FIELD_NUMBER: _ClassVar[int]
        segment_count: int
        entry_count: int
        morphed_size: int
        def __init__(self, segment_count: _Optional[int] = ..., entry_count: _Optional[int] = ..., morphed_size: _Optional[int] = ...) -> None: ...
    class UpdateIntent(_message.Message):
        __slots__ = ("intent_id", "creation_time_usecs", "write_object", "delete_object")
        class WriteObject(_message.Message):
            __slots__ = ("cloud_object_written", "epoch_id", "object_info", "nodes_deleted", "safe_to_delete_object")
            CLOUD_OBJECT_WRITTEN_FIELD_NUMBER: _ClassVar[int]
            EPOCH_ID_FIELD_NUMBER: _ClassVar[int]
            OBJECT_INFO_FIELD_NUMBER: _ClassVar[int]
            NODES_DELETED_FIELD_NUMBER: _ClassVar[int]
            SAFE_TO_DELETE_OBJECT_FIELD_NUMBER: _ClassVar[int]
            cloud_object_written: bool
            epoch_id: int
            object_info: CloudObjectScribeMetadataProto.ObjectInfo
            nodes_deleted: bool
            safe_to_delete_object: bool
            def __init__(self, cloud_object_written: bool = ..., epoch_id: _Optional[int] = ..., object_info: _Optional[_Union[CloudObjectScribeMetadataProto.ObjectInfo, _Mapping]] = ..., nodes_deleted: bool = ..., safe_to_delete_object: bool = ...) -> None: ...
        class DeleteObject(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        INTENT_ID_FIELD_NUMBER: _ClassVar[int]
        CREATION_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
        WRITE_OBJECT_FIELD_NUMBER: _ClassVar[int]
        DELETE_OBJECT_FIELD_NUMBER: _ClassVar[int]
        intent_id: int
        creation_time_usecs: int
        write_object: CloudObjectScribeMetadataProto.UpdateIntent.WriteObject
        delete_object: CloudObjectScribeMetadataProto.UpdateIntent.DeleteObject
        def __init__(self, intent_id: _Optional[int] = ..., creation_time_usecs: _Optional[int] = ..., write_object: _Optional[_Union[CloudObjectScribeMetadataProto.UpdateIntent.WriteObject, _Mapping]] = ..., delete_object: _Optional[_Union[CloudObjectScribeMetadataProto.UpdateIntent.DeleteObject, _Mapping]] = ...) -> None: ...
    EPOCH_ID_FIELD_NUMBER: _ClassVar[int]
    OPCLOCK_VEC_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATE_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    CLOUD_OBJECT_VERSION_FIELD_NUMBER: _ClassVar[int]
    CLOUD_OBJECT_TYPE_FIELD_NUMBER: _ClassVar[int]
    PREFIX_FIELD_NUMBER: _ClassVar[int]
    OBJECT_INFO_FIELD_NUMBER: _ClassVar[int]
    INTENT_ID_GENERATOR_FIELD_NUMBER: _ClassVar[int]
    UPDATE_INTENT_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    UPDATE_INTENT_FIELD_NUMBER: _ClassVar[int]
    IS_DELETED_FIELD_NUMBER: _ClassVar[int]
    NUM_DELETED_NODES_FIELD_NUMBER: _ClassVar[int]
    MINIMUM_RETENTION_TIMESTAMP_SECS_FIELD_NUMBER: _ClassVar[int]
    RETENTION_MODE_FIELD_NUMBER: _ClassVar[int]
    WORM_RETENTION_EXTENDABILITY_INFO_FIELD_NUMBER: _ClassVar[int]
    VERSIONED_OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    epoch_id: int
    opclock_vec: _containers.RepeatedCompositeFieldContainer[_op_clock_pb2.OpClock]
    last_update_time_usecs: int
    cloud_object_version: int
    cloud_object_type: _cloud_object_pb2.CloudObjectMetadataProto.ObjectType
    prefix: str
    object_info: CloudObjectScribeMetadataProto.ObjectInfo
    intent_id_generator: int
    update_intent_session_id: int
    update_intent: CloudObjectScribeMetadataProto.UpdateIntent
    is_deleted: bool
    num_deleted_nodes: int
    minimum_retention_timestamp_secs: int
    retention_mode: _worm_pb2.RetentionMode.Type
    worm_retention_extendability_info: _worm_pb2.WORMRetentionExtendabilityInfo
    versioned_object_id: str
    def __init__(self, epoch_id: _Optional[int] = ..., opclock_vec: _Optional[_Iterable[_Union[_op_clock_pb2.OpClock, _Mapping]]] = ..., last_update_time_usecs: _Optional[int] = ..., cloud_object_version: _Optional[int] = ..., cloud_object_type: _Optional[_Union[_cloud_object_pb2.CloudObjectMetadataProto.ObjectType, str]] = ..., prefix: _Optional[str] = ..., object_info: _Optional[_Union[CloudObjectScribeMetadataProto.ObjectInfo, _Mapping]] = ..., intent_id_generator: _Optional[int] = ..., update_intent_session_id: _Optional[int] = ..., update_intent: _Optional[_Union[CloudObjectScribeMetadataProto.UpdateIntent, _Mapping]] = ..., is_deleted: bool = ..., num_deleted_nodes: _Optional[int] = ..., minimum_retention_timestamp_secs: _Optional[int] = ..., retention_mode: _Optional[_Union[_worm_pb2.RetentionMode.Type, str]] = ..., worm_retention_extendability_info: _Optional[_Union[_worm_pb2.WORMRetentionExtendabilityInfo, _Mapping]] = ..., versioned_object_id: _Optional[str] = ...) -> None: ...

class CloudObjectScribeDeletedInfoProto(_message.Message):
    __slots__ = ("deleted_local_id_vec",)
    DELETED_LOCAL_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    deleted_local_id_vec: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, deleted_local_id_vec: _Optional[_Iterable[int]] = ...) -> None: ...
