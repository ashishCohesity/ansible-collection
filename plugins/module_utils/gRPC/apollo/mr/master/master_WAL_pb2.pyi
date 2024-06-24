from apollo.mr.base import api_version_pb2 as _api_version_pb2
from apollo.mr.base import pipeline_pb2 as _pipeline_pb2
from apollo.mr.base import shard_pb2 as _shard_pb2
from apollo.mr.master import master_pb2 as _master_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class WALRecordProto(_message.Message):
    __slots__ = ("version", "software_version", "slave_vec", "job_vec", "shard_vec", "deleted_shard_checkpoint_vec", "job_history", "delete_job_run_history", "add_or_update_job_run_history", "delete_job", "add_or_update_job", "delete_slave", "add_slave", "delete_shard", "add_or_update_shard", "throttling_state")
    class ShardCheckpoint(_message.Message):
        __slots__ = ("shard_id", "checkpoint")
        SHARD_ID_FIELD_NUMBER: _ClassVar[int]
        CHECKPOINT_FIELD_NUMBER: _ClassVar[int]
        shard_id: _pipeline_pb2.IdProto
        checkpoint: _shard_pb2.ShardCheckpointProto
        def __init__(self, shard_id: _Optional[_Union[_pipeline_pb2.IdProto, _Mapping]] = ..., checkpoint: _Optional[_Union[_shard_pb2.ShardCheckpointProto, _Mapping]] = ...) -> None: ...
    class DeleteSlave(_message.Message):
        __slots__ = ("node_id",)
        NODE_ID_FIELD_NUMBER: _ClassVar[int]
        node_id: int
        def __init__(self, node_id: _Optional[int] = ...) -> None: ...
    class DeleteShard(_message.Message):
        __slots__ = ("id", "node_id", "checkpoint")
        ID_FIELD_NUMBER: _ClassVar[int]
        NODE_ID_FIELD_NUMBER: _ClassVar[int]
        CHECKPOINT_FIELD_NUMBER: _ClassVar[int]
        id: _pipeline_pb2.IdProto
        node_id: int
        checkpoint: _shard_pb2.ShardCheckpointProto
        def __init__(self, id: _Optional[_Union[_pipeline_pb2.IdProto, _Mapping]] = ..., node_id: _Optional[int] = ..., checkpoint: _Optional[_Union[_shard_pb2.ShardCheckpointProto, _Mapping]] = ...) -> None: ...
    VERSION_FIELD_NUMBER: _ClassVar[int]
    SOFTWARE_VERSION_FIELD_NUMBER: _ClassVar[int]
    SLAVE_VEC_FIELD_NUMBER: _ClassVar[int]
    JOB_VEC_FIELD_NUMBER: _ClassVar[int]
    SHARD_VEC_FIELD_NUMBER: _ClassVar[int]
    DELETED_SHARD_CHECKPOINT_VEC_FIELD_NUMBER: _ClassVar[int]
    JOB_HISTORY_FIELD_NUMBER: _ClassVar[int]
    DELETE_JOB_RUN_HISTORY_FIELD_NUMBER: _ClassVar[int]
    ADD_OR_UPDATE_JOB_RUN_HISTORY_FIELD_NUMBER: _ClassVar[int]
    DELETE_JOB_FIELD_NUMBER: _ClassVar[int]
    ADD_OR_UPDATE_JOB_FIELD_NUMBER: _ClassVar[int]
    DELETE_SLAVE_FIELD_NUMBER: _ClassVar[int]
    ADD_SLAVE_FIELD_NUMBER: _ClassVar[int]
    DELETE_SHARD_FIELD_NUMBER: _ClassVar[int]
    ADD_OR_UPDATE_SHARD_FIELD_NUMBER: _ClassVar[int]
    THROTTLING_STATE_FIELD_NUMBER: _ClassVar[int]
    version: _api_version_pb2.APIVersion
    software_version: str
    slave_vec: _containers.RepeatedCompositeFieldContainer[_shard_pb2.SlaveProto]
    job_vec: _containers.RepeatedCompositeFieldContainer[_master_pb2.JobProto]
    shard_vec: _containers.RepeatedCompositeFieldContainer[_shard_pb2.ShardProto]
    deleted_shard_checkpoint_vec: _containers.RepeatedCompositeFieldContainer[WALRecordProto.ShardCheckpoint]
    job_history: _master_pb2.JobHistoryProto
    delete_job_run_history: str
    add_or_update_job_run_history: _master_pb2.JobHistoryProto.RunHistory
    delete_job: _pipeline_pb2.IdProto
    add_or_update_job: _master_pb2.JobProto
    delete_slave: WALRecordProto.DeleteSlave
    add_slave: _shard_pb2.SlaveProto
    delete_shard: WALRecordProto.DeleteShard
    add_or_update_shard: _shard_pb2.ShardProto
    throttling_state: _master_pb2.ThrottlingState
    def __init__(self, version: _Optional[_Union[_api_version_pb2.APIVersion, _Mapping]] = ..., software_version: _Optional[str] = ..., slave_vec: _Optional[_Iterable[_Union[_shard_pb2.SlaveProto, _Mapping]]] = ..., job_vec: _Optional[_Iterable[_Union[_master_pb2.JobProto, _Mapping]]] = ..., shard_vec: _Optional[_Iterable[_Union[_shard_pb2.ShardProto, _Mapping]]] = ..., deleted_shard_checkpoint_vec: _Optional[_Iterable[_Union[WALRecordProto.ShardCheckpoint, _Mapping]]] = ..., job_history: _Optional[_Union[_master_pb2.JobHistoryProto, _Mapping]] = ..., delete_job_run_history: _Optional[str] = ..., add_or_update_job_run_history: _Optional[_Union[_master_pb2.JobHistoryProto.RunHistory, _Mapping]] = ..., delete_job: _Optional[_Union[_pipeline_pb2.IdProto, _Mapping]] = ..., add_or_update_job: _Optional[_Union[_master_pb2.JobProto, _Mapping]] = ..., delete_slave: _Optional[_Union[WALRecordProto.DeleteSlave, _Mapping]] = ..., add_slave: _Optional[_Union[_shard_pb2.SlaveProto, _Mapping]] = ..., delete_shard: _Optional[_Union[WALRecordProto.DeleteShard, _Mapping]] = ..., add_or_update_shard: _Optional[_Union[_shard_pb2.ShardProto, _Mapping]] = ..., throttling_state: _Optional[_Union[_master_pb2.ThrottlingState, _Mapping]] = ...) -> None: ...
