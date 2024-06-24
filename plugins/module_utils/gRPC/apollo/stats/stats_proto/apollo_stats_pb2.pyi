from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ViewBoxStatsProto(_message.Message):
    __slots__ = ("view_box_map",)
    class ViewBox(_message.Message):
        __slots__ = ("action_metrics", "chunk_file_metrics")
        class ActionMetricsEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: int
            value: int
            def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
        class ChunkFileMetricsEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: int
            value: int
            def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
        ACTION_METRICS_FIELD_NUMBER: _ClassVar[int]
        CHUNK_FILE_METRICS_FIELD_NUMBER: _ClassVar[int]
        action_metrics: _containers.ScalarMap[int, int]
        chunk_file_metrics: _containers.ScalarMap[int, int]
        def __init__(self, action_metrics: _Optional[_Mapping[int, int]] = ..., chunk_file_metrics: _Optional[_Mapping[int, int]] = ...) -> None: ...
    class ViewBoxMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: ViewBoxStatsProto.ViewBox
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[ViewBoxStatsProto.ViewBox, _Mapping]] = ...) -> None: ...
    VIEW_BOX_MAP_FIELD_NUMBER: _ClassVar[int]
    view_box_map: _containers.MessageMap[int, ViewBoxStatsProto.ViewBox]
    def __init__(self, view_box_map: _Optional[_Mapping[int, ViewBoxStatsProto.ViewBox]] = ...) -> None: ...

class JobInfoProto(_message.Message):
    __slots__ = ("job_info_map",)
    class JobInfo(_message.Message):
        __slots__ = ("algo_names", "num_actions_raised", "job_start_time", "job_end_time")
        ALGO_NAMES_FIELD_NUMBER: _ClassVar[int]
        NUM_ACTIONS_RAISED_FIELD_NUMBER: _ClassVar[int]
        JOB_START_TIME_FIELD_NUMBER: _ClassVar[int]
        JOB_END_TIME_FIELD_NUMBER: _ClassVar[int]
        algo_names: _containers.RepeatedScalarFieldContainer[bytes]
        num_actions_raised: int
        job_start_time: int
        job_end_time: int
        def __init__(self, algo_names: _Optional[_Iterable[bytes]] = ..., num_actions_raised: _Optional[int] = ..., job_start_time: _Optional[int] = ..., job_end_time: _Optional[int] = ...) -> None: ...
    class JobInfoMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: JobInfoProto.JobInfo
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[JobInfoProto.JobInfo, _Mapping]] = ...) -> None: ...
    JOB_INFO_MAP_FIELD_NUMBER: _ClassVar[int]
    job_info_map: _containers.MessageMap[str, JobInfoProto.JobInfo]
    def __init__(self, job_info_map: _Optional[_Mapping[str, JobInfoProto.JobInfo]] = ...) -> None: ...

class NodeInfoProto(_message.Message):
    __slots__ = ("node_info_map",)
    class NodeInfo(_message.Message):
        __slots__ = ("is_master",)
        IS_MASTER_FIELD_NUMBER: _ClassVar[int]
        is_master: bool
        def __init__(self, is_master: bool = ...) -> None: ...
    class NodeInfoMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: NodeInfoProto.NodeInfo
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[NodeInfoProto.NodeInfo, _Mapping]] = ...) -> None: ...
    NODE_INFO_MAP_FIELD_NUMBER: _ClassVar[int]
    node_info_map: _containers.MessageMap[str, NodeInfoProto.NodeInfo]
    def __init__(self, node_info_map: _Optional[_Mapping[str, NodeInfoProto.NodeInfo]] = ...) -> None: ...
