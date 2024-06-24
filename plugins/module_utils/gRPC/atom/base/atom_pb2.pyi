from atom.base import entity_pb2 as _entity_pb2
from atom.base import error_pb2 as _error_pb2
from atom.base import event_pb2 as _event_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AtomConfigProto(_message.Message):
    __slots__ = ("gandalf_master_key",)
    GANDALF_MASTER_KEY_FIELD_NUMBER: _ClassVar[int]
    gandalf_master_key: str
    def __init__(self, gandalf_master_key: _Optional[str] = ...) -> None: ...

class ConstituentLoadProto(_message.Message):
    __slots__ = ("incarnation_id", "is_live", "num_clients")
    INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    IS_LIVE_FIELD_NUMBER: _ClassVar[int]
    NUM_CLIENTS_FIELD_NUMBER: _ClassVar[int]
    incarnation_id: int
    is_live: bool
    num_clients: int
    def __init__(self, incarnation_id: _Optional[int] = ..., is_live: bool = ..., num_clients: _Optional[int] = ...) -> None: ...

class AllocatedNodeProto(_message.Message):
    __slots__ = ("entity_id", "constituent_id", "endpoint")
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    CONSTITUENT_ID_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    entity_id: _entity_pb2.EntityID
    constituent_id: int
    endpoint: str
    def __init__(self, entity_id: _Optional[_Union[_entity_pb2.EntityID, _Mapping]] = ..., constituent_id: _Optional[int] = ..., endpoint: _Optional[str] = ...) -> None: ...

class EntityMetadataProto(_message.Message):
    __slots__ = ("entity_id", "log_file_dir", "scribe_version", "vmware_vmsd_file_path", "replication_target_vec", "is_cdp_disabled", "is_journal_sharded")
    class ReplicationTargetInfo(_message.Message):
        __slots__ = ("cluster_id", "cluster_name", "log_file_dir", "remote_entity_id")
        CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
        CLUSTER_NAME_FIELD_NUMBER: _ClassVar[int]
        LOG_FILE_DIR_FIELD_NUMBER: _ClassVar[int]
        REMOTE_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
        cluster_id: int
        cluster_name: str
        log_file_dir: str
        remote_entity_id: _entity_pb2.EntityID
        def __init__(self, cluster_id: _Optional[int] = ..., cluster_name: _Optional[str] = ..., log_file_dir: _Optional[str] = ..., remote_entity_id: _Optional[_Union[_entity_pb2.EntityID, _Mapping]] = ...) -> None: ...
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    LOG_FILE_DIR_FIELD_NUMBER: _ClassVar[int]
    SCRIBE_VERSION_FIELD_NUMBER: _ClassVar[int]
    VMWARE_VMSD_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    REPLICATION_TARGET_VEC_FIELD_NUMBER: _ClassVar[int]
    IS_CDP_DISABLED_FIELD_NUMBER: _ClassVar[int]
    IS_JOURNAL_SHARDED_FIELD_NUMBER: _ClassVar[int]
    entity_id: _entity_pb2.EntityID
    log_file_dir: str
    scribe_version: int
    vmware_vmsd_file_path: str
    replication_target_vec: _containers.RepeatedCompositeFieldContainer[EntityMetadataProto.ReplicationTargetInfo]
    is_cdp_disabled: bool
    is_journal_sharded: bool
    def __init__(self, entity_id: _Optional[_Union[_entity_pb2.EntityID, _Mapping]] = ..., log_file_dir: _Optional[str] = ..., scribe_version: _Optional[int] = ..., vmware_vmsd_file_path: _Optional[str] = ..., replication_target_vec: _Optional[_Iterable[_Union[EntityMetadataProto.ReplicationTargetInfo, _Mapping]]] = ..., is_cdp_disabled: bool = ..., is_journal_sharded: bool = ...) -> None: ...

class GetDataEventsArg(_message.Message):
    __slots__ = ("entity_id", "entity_id_vec", "for_master", "is_journal_sharded")
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    FOR_MASTER_FIELD_NUMBER: _ClassVar[int]
    IS_JOURNAL_SHARDED_FIELD_NUMBER: _ClassVar[int]
    entity_id: _entity_pb2.EntityID
    entity_id_vec: _containers.RepeatedCompositeFieldContainer[_entity_pb2.EntityID]
    for_master: bool
    is_journal_sharded: bool
    def __init__(self, entity_id: _Optional[_Union[_entity_pb2.EntityID, _Mapping]] = ..., entity_id_vec: _Optional[_Iterable[_Union[_entity_pb2.EntityID, _Mapping]]] = ..., for_master: bool = ..., is_journal_sharded: bool = ...) -> None: ...

class GetDataEventsResult(_message.Message):
    __slots__ = ("error", "entity_data_events_vec")
    class EntityDataEvents(_message.Message):
        __slots__ = ("error", "entity_id", "data_event_vec")
        ERROR_FIELD_NUMBER: _ClassVar[int]
        ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
        DATA_EVENT_VEC_FIELD_NUMBER: _ClassVar[int]
        error: _error_pb2.ErrorProto
        entity_id: _entity_pb2.EntityID
        data_event_vec: _containers.RepeatedCompositeFieldContainer[_event_pb2.DataEvent]
        def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., entity_id: _Optional[_Union[_entity_pb2.EntityID, _Mapping]] = ..., data_event_vec: _Optional[_Iterable[_Union[_event_pb2.DataEvent, _Mapping]]] = ...) -> None: ...
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ENTITY_DATA_EVENTS_VEC_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    entity_data_events_vec: _containers.RepeatedCompositeFieldContainer[GetDataEventsResult.EntityDataEvents]
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., entity_data_events_vec: _Optional[_Iterable[_Union[GetDataEventsResult.EntityDataEvents, _Mapping]]] = ...) -> None: ...

class ClearDataEventsArg(_message.Message):
    __slots__ = ("latest_consumed_sequencer_info_vec", "for_master")
    class EntitySequencerInfo(_message.Message):
        __slots__ = ("entity_id", "sequencer", "is_journal_sharded", "clear_all")
        ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
        SEQUENCER_FIELD_NUMBER: _ClassVar[int]
        IS_JOURNAL_SHARDED_FIELD_NUMBER: _ClassVar[int]
        CLEAR_ALL_FIELD_NUMBER: _ClassVar[int]
        entity_id: _entity_pb2.EntityID
        sequencer: _event_pb2.Sequencer
        is_journal_sharded: bool
        clear_all: bool
        def __init__(self, entity_id: _Optional[_Union[_entity_pb2.EntityID, _Mapping]] = ..., sequencer: _Optional[_Union[_event_pb2.Sequencer, _Mapping]] = ..., is_journal_sharded: bool = ..., clear_all: bool = ...) -> None: ...
    LATEST_CONSUMED_SEQUENCER_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    FOR_MASTER_FIELD_NUMBER: _ClassVar[int]
    latest_consumed_sequencer_info_vec: _containers.RepeatedCompositeFieldContainer[ClearDataEventsArg.EntitySequencerInfo]
    for_master: bool
    def __init__(self, latest_consumed_sequencer_info_vec: _Optional[_Iterable[_Union[ClearDataEventsArg.EntitySequencerInfo, _Mapping]]] = ..., for_master: bool = ...) -> None: ...

class ClearDataEventsResult(_message.Message):
    __slots__ = ("error", "entity_result_vec")
    class ClearDataEventsEntityResult(_message.Message):
        __slots__ = ("error", "entity_id")
        ERROR_FIELD_NUMBER: _ClassVar[int]
        ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
        error: _error_pb2.ErrorProto
        entity_id: _entity_pb2.EntityID
        def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., entity_id: _Optional[_Union[_entity_pb2.EntityID, _Mapping]] = ...) -> None: ...
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ENTITY_RESULT_VEC_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    entity_result_vec: _containers.RepeatedCompositeFieldContainer[ClearDataEventsResult.ClearDataEventsEntityResult]
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., entity_result_vec: _Optional[_Iterable[_Union[ClearDataEventsResult.ClearDataEventsEntityResult, _Mapping]]] = ...) -> None: ...

class UpdateEntityMetadataArg(_message.Message):
    __slots__ = ("entity_metadata",)
    ENTITY_METADATA_FIELD_NUMBER: _ClassVar[int]
    entity_metadata: EntityMetadataProto
    def __init__(self, entity_metadata: _Optional[_Union[EntityMetadataProto, _Mapping]] = ...) -> None: ...

class UpdateEntityMetadataResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class AddDataEventsArg(_message.Message):
    __slots__ = ("entity_data_event_vec", "is_gap_filler", "for_master")
    class AddDataEventsEntity(_message.Message):
        __slots__ = ("entity_id", "data_event_vec", "is_journal_sharded")
        ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
        DATA_EVENT_VEC_FIELD_NUMBER: _ClassVar[int]
        IS_JOURNAL_SHARDED_FIELD_NUMBER: _ClassVar[int]
        entity_id: _entity_pb2.EntityID
        data_event_vec: _containers.RepeatedCompositeFieldContainer[_event_pb2.DataEvent]
        is_journal_sharded: bool
        def __init__(self, entity_id: _Optional[_Union[_entity_pb2.EntityID, _Mapping]] = ..., data_event_vec: _Optional[_Iterable[_Union[_event_pb2.DataEvent, _Mapping]]] = ..., is_journal_sharded: bool = ...) -> None: ...
    ENTITY_DATA_EVENT_VEC_FIELD_NUMBER: _ClassVar[int]
    IS_GAP_FILLER_FIELD_NUMBER: _ClassVar[int]
    FOR_MASTER_FIELD_NUMBER: _ClassVar[int]
    entity_data_event_vec: _containers.RepeatedCompositeFieldContainer[AddDataEventsArg.AddDataEventsEntity]
    is_gap_filler: bool
    for_master: bool
    def __init__(self, entity_data_event_vec: _Optional[_Iterable[_Union[AddDataEventsArg.AddDataEventsEntity, _Mapping]]] = ..., is_gap_filler: bool = ..., for_master: bool = ...) -> None: ...

class AddDataEventsResult(_message.Message):
    __slots__ = ("error", "entity_result_vec")
    class AddDataEventsEntityResult(_message.Message):
        __slots__ = ("error", "entity_id")
        ERROR_FIELD_NUMBER: _ClassVar[int]
        ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
        error: _error_pb2.ErrorProto
        entity_id: _entity_pb2.EntityID
        def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., entity_id: _Optional[_Union[_entity_pb2.EntityID, _Mapping]] = ...) -> None: ...
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ENTITY_RESULT_VEC_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    entity_result_vec: _containers.RepeatedCompositeFieldContainer[AddDataEventsResult.AddDataEventsEntityResult]
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., entity_result_vec: _Optional[_Iterable[_Union[AddDataEventsResult.AddDataEventsEntityResult, _Mapping]]] = ...) -> None: ...

class NodeInfoProto(_message.Message):
    __slots__ = ("node_constituent_id", "rpc_endpoint")
    NODE_CONSTITUENT_ID_FIELD_NUMBER: _ClassVar[int]
    RPC_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    node_constituent_id: int
    rpc_endpoint: str
    def __init__(self, node_constituent_id: _Optional[int] = ..., rpc_endpoint: _Optional[str] = ...) -> None: ...

class RegisterEntityArg(_message.Message):
    __slots__ = ("entity_id", "entity_metadata")
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    ENTITY_METADATA_FIELD_NUMBER: _ClassVar[int]
    entity_id: _entity_pb2.EntityID
    entity_metadata: EntityMetadataProto
    def __init__(self, entity_id: _Optional[_Union[_entity_pb2.EntityID, _Mapping]] = ..., entity_metadata: _Optional[_Union[EntityMetadataProto, _Mapping]] = ...) -> None: ...

class RegisterEntityResult(_message.Message):
    __slots__ = ("error", "entity_id", "node_info")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    NODE_INFO_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    entity_id: _entity_pb2.EntityID
    node_info: NodeInfoProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., entity_id: _Optional[_Union[_entity_pb2.EntityID, _Mapping]] = ..., node_info: _Optional[_Union[NodeInfoProto, _Mapping]] = ...) -> None: ...

class GetEntityManagerNodeArg(_message.Message):
    __slots__ = ("entity_id",)
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    entity_id: _entity_pb2.EntityID
    def __init__(self, entity_id: _Optional[_Union[_entity_pb2.EntityID, _Mapping]] = ...) -> None: ...

class GetEntityManagerNodeResult(_message.Message):
    __slots__ = ("error", "entity_id", "node_info")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    NODE_INFO_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    entity_id: _entity_pb2.EntityID
    node_info: NodeInfoProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., entity_id: _Optional[_Union[_entity_pb2.EntityID, _Mapping]] = ..., node_info: _Optional[_Union[NodeInfoProto, _Mapping]] = ...) -> None: ...

class GetRegisteredEntitiesArg(_message.Message):
    __slots__ = ("node_info_vec",)
    NODE_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    node_info_vec: _containers.RepeatedCompositeFieldContainer[NodeInfoProto]
    def __init__(self, node_info_vec: _Optional[_Iterable[_Union[NodeInfoProto, _Mapping]]] = ...) -> None: ...

class GetRegisteredEntitiesResult(_message.Message):
    __slots__ = ("error", "node_entities_vec")
    class RegisteredEntitiesPerNodeResult(_message.Message):
        __slots__ = ("node_info", "entity_vec")
        NODE_INFO_FIELD_NUMBER: _ClassVar[int]
        ENTITY_VEC_FIELD_NUMBER: _ClassVar[int]
        node_info: NodeInfoProto
        entity_vec: _containers.RepeatedCompositeFieldContainer[_entity_pb2.EntityID]
        def __init__(self, node_info: _Optional[_Union[NodeInfoProto, _Mapping]] = ..., entity_vec: _Optional[_Iterable[_Union[_entity_pb2.EntityID, _Mapping]]] = ...) -> None: ...
    ERROR_FIELD_NUMBER: _ClassVar[int]
    NODE_ENTITIES_VEC_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    node_entities_vec: _containers.RepeatedCompositeFieldContainer[GetRegisteredEntitiesResult.RegisteredEntitiesPerNodeResult]
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., node_entities_vec: _Optional[_Iterable[_Union[GetRegisteredEntitiesResult.RegisteredEntitiesPerNodeResult, _Mapping]]] = ...) -> None: ...

class UnregisterEntityArg(_message.Message):
    __slots__ = ("entity_id",)
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    entity_id: _entity_pb2.EntityID
    def __init__(self, entity_id: _Optional[_Union[_entity_pb2.EntityID, _Mapping]] = ...) -> None: ...

class UnregisterEntityResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class AddOrRemoveRegisteredEntityArg(_message.Message):
    __slots__ = ("entity_id", "remove_entity")
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    REMOVE_ENTITY_FIELD_NUMBER: _ClassVar[int]
    entity_id: _entity_pb2.EntityID
    remove_entity: bool
    def __init__(self, entity_id: _Optional[_Union[_entity_pb2.EntityID, _Mapping]] = ..., remove_entity: bool = ...) -> None: ...

class AddOrRemoveRegisteredEntityResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class EpochProto(_message.Message):
    __slots__ = ("epoch_id", "scribe_version")
    EPOCH_ID_FIELD_NUMBER: _ClassVar[int]
    SCRIBE_VERSION_FIELD_NUMBER: _ClassVar[int]
    epoch_id: int
    scribe_version: int
    def __init__(self, epoch_id: _Optional[int] = ..., scribe_version: _Optional[int] = ...) -> None: ...

class SwitchEpochArg(_message.Message):
    __slots__ = ("entity_id", "curr_epoch")
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    CURR_EPOCH_FIELD_NUMBER: _ClassVar[int]
    entity_id: _entity_pb2.EntityID
    curr_epoch: EpochProto
    def __init__(self, entity_id: _Optional[_Union[_entity_pb2.EntityID, _Mapping]] = ..., curr_epoch: _Optional[_Union[EpochProto, _Mapping]] = ...) -> None: ...

class SwitchEpochResult(_message.Message):
    __slots__ = ("error", "entity_id", "epoch")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    EPOCH_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    entity_id: _entity_pb2.EntityID
    epoch: EpochProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., entity_id: _Optional[_Union[_entity_pb2.EntityID, _Mapping]] = ..., epoch: _Optional[_Union[EpochProto, _Mapping]] = ...) -> None: ...
