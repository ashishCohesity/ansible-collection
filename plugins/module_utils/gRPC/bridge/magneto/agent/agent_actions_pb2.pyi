from bridge.magneto.base import magneto_actions_pb2 as _magneto_actions_pb2
from magneto.base import magneto_pb2 as _magneto_pb2
from magneto.base import env_params_pb2 as _env_params_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AgentInfo(_message.Message):
    __slots__ = ("connector_params", "api_version", "agent_incarnation_id")
    CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    AGENT_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    connector_params: _magneto_pb2.ConnectorParams
    api_version: int
    agent_incarnation_id: int
    def __init__(self, connector_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ..., api_version: _Optional[int] = ..., agent_incarnation_id: _Optional[int] = ...) -> None: ...

class FetchAndStoreDataAction(_message.Message):
    __slots__ = ("file_info_vec", "cluster_id", "cluster_incarnation_id")
    class FileInfo(_message.Message):
        __slots__ = ("snapfs_full_dir_path", "snapfs_file_name", "agent_data_id")
        SNAPFS_FULL_DIR_PATH_FIELD_NUMBER: _ClassVar[int]
        SNAPFS_FILE_NAME_FIELD_NUMBER: _ClassVar[int]
        AGENT_DATA_ID_FIELD_NUMBER: _ClassVar[int]
        snapfs_full_dir_path: str
        snapfs_file_name: str
        agent_data_id: bytes
        def __init__(self, snapfs_full_dir_path: _Optional[str] = ..., snapfs_file_name: _Optional[str] = ..., agent_data_id: _Optional[bytes] = ...) -> None: ...
    FILE_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    file_info_vec: _containers.RepeatedCompositeFieldContainer[FetchAndStoreDataAction.FileInfo]
    cluster_id: int
    cluster_incarnation_id: int
    def __init__(self, file_info_vec: _Optional[_Iterable[_Union[FetchAndStoreDataAction.FileInfo, _Mapping]]] = ..., cluster_id: _Optional[int] = ..., cluster_incarnation_id: _Optional[int] = ...) -> None: ...

class AgentActionArg(_message.Message):
    __slots__ = ("task_id", "agent_info", "fetch_and_store_data_action")
    AGENT_ACTION_ARG_FIELD_NUMBER: _ClassVar[int]
    agent_action_arg: _descriptor.FieldDescriptor
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    AGENT_INFO_FIELD_NUMBER: _ClassVar[int]
    FETCH_AND_STORE_DATA_ACTION_FIELD_NUMBER: _ClassVar[int]
    task_id: int
    agent_info: AgentInfo
    fetch_and_store_data_action: FetchAndStoreDataAction
    def __init__(self, task_id: _Optional[int] = ..., agent_info: _Optional[_Union[AgentInfo, _Mapping]] = ..., fetch_and_store_data_action: _Optional[_Union[FetchAndStoreDataAction, _Mapping]] = ...) -> None: ...
