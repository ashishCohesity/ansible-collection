from bridge.base import error_pb2 as _error_pb2
from magneto.slave.stub import bridge_updates_pb2 as _bridge_updates_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FetchAndStoreDataActionUpdateArg(_message.Message):
    __slots__ = ("file_update_arg_vec",)
    class FileUpdateArg(_message.Message):
        __slots__ = ("agent_data_id", "size_bytes", "error")
        AGENT_DATA_ID_FIELD_NUMBER: _ClassVar[int]
        SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        agent_data_id: bytes
        size_bytes: int
        error: _error_pb2.ErrorProto
        def __init__(self, agent_data_id: _Optional[bytes] = ..., size_bytes: _Optional[int] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...
    FILE_UPDATE_ARG_VEC_FIELD_NUMBER: _ClassVar[int]
    file_update_arg_vec: _containers.RepeatedCompositeFieldContainer[FetchAndStoreDataActionUpdateArg.FileUpdateArg]
    def __init__(self, file_update_arg_vec: _Optional[_Iterable[_Union[FetchAndStoreDataActionUpdateArg.FileUpdateArg, _Mapping]]] = ...) -> None: ...

class AgentActionUpdateArg(_message.Message):
    __slots__ = ("fetch_and_store_data_action_update_arg",)
    AGENT_ACTION_UPDATE_ARG_FIELD_NUMBER: _ClassVar[int]
    agent_action_update_arg: _descriptor.FieldDescriptor
    FETCH_AND_STORE_DATA_ACTION_UPDATE_ARG_FIELD_NUMBER: _ClassVar[int]
    fetch_and_store_data_action_update_arg: FetchAndStoreDataActionUpdateArg
    def __init__(self, fetch_and_store_data_action_update_arg: _Optional[_Union[FetchAndStoreDataActionUpdateArg, _Mapping]] = ...) -> None: ...
