from yoda.master.stub import yoda_rpc_args_pb2 as _yoda_rpc_args_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ClusterIdentifier(_message.Message):
    __slots__ = ("cluster_id", "cluster_incarnation_id", "sf_account_id")
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    SF_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    cluster_id: int
    cluster_incarnation_id: int
    sf_account_id: str
    def __init__(self, cluster_id: _Optional[int] = ..., cluster_incarnation_id: _Optional[int] = ..., sf_account_id: _Optional[str] = ...) -> None: ...

class SnapshotDiffTriggerRequest(_message.Message):
    __slots__ = ("cluster_identifier", "prepareCrackedFileIndexArg")
    CLUSTER_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    PREPARECRACKEDFILEINDEXARG_FIELD_NUMBER: _ClassVar[int]
    cluster_identifier: ClusterIdentifier
    prepareCrackedFileIndexArg: _yoda_rpc_args_pb2.PrepareCrackedFileIndexArg
    def __init__(self, cluster_identifier: _Optional[_Union[ClusterIdentifier, _Mapping]] = ..., prepareCrackedFileIndexArg: _Optional[_Union[_yoda_rpc_args_pb2.PrepareCrackedFileIndexArg, _Mapping]] = ...) -> None: ...

class SnapshotDiffStatusRequest(_message.Message):
    __slots__ = ("cluster_identifier", "key")
    CLUSTER_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    cluster_identifier: ClusterIdentifier
    key: str
    def __init__(self, cluster_identifier: _Optional[_Union[ClusterIdentifier, _Mapping]] = ..., key: _Optional[str] = ...) -> None: ...

class PranaRestUrisProto(_message.Message):
    __slots__ = ("api_version", "snapshot_diff_trigger_uri", "snapshot_diff_status_uri", "connection_status_uri", "helios_collector_state_uri", "helios_collector_state_reset_uri")
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_DIFF_TRIGGER_URI_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_DIFF_STATUS_URI_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_STATUS_URI_FIELD_NUMBER: _ClassVar[int]
    HELIOS_COLLECTOR_STATE_URI_FIELD_NUMBER: _ClassVar[int]
    HELIOS_COLLECTOR_STATE_RESET_URI_FIELD_NUMBER: _ClassVar[int]
    api_version: str
    snapshot_diff_trigger_uri: str
    snapshot_diff_status_uri: str
    connection_status_uri: str
    helios_collector_state_uri: str
    helios_collector_state_reset_uri: str
    def __init__(self, api_version: _Optional[str] = ..., snapshot_diff_trigger_uri: _Optional[str] = ..., snapshot_diff_status_uri: _Optional[str] = ..., connection_status_uri: _Optional[str] = ..., helios_collector_state_uri: _Optional[str] = ..., helios_collector_state_reset_uri: _Optional[str] = ...) -> None: ...
