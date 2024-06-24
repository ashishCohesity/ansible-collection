from open_util.net import protorpc_pb2 as _protorpc_pb2
from yoda.base import yoda_pb2 as _yoda_pb2
from yoda.master.stub import yoda_rpc_args_pb2 as _yoda_rpc_args_pb2
from yoda.util import work_item_pb2 as _work_item_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SubmitWorkArg(_message.Message):
    __slots__ = ("target_constituent_id", "target_incarnation_id", "dispatcher_name", "work_item")
    TARGET_CONSTITUENT_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    DISPATCHER_NAME_FIELD_NUMBER: _ClassVar[int]
    WORK_ITEM_FIELD_NUMBER: _ClassVar[int]
    target_constituent_id: int
    target_incarnation_id: int
    dispatcher_name: str
    work_item: _work_item_pb2.WorkItem
    def __init__(self, target_constituent_id: _Optional[int] = ..., target_incarnation_id: _Optional[int] = ..., dispatcher_name: _Optional[str] = ..., work_item: _Optional[_Union[_work_item_pb2.WorkItem, _Mapping]] = ...) -> None: ...

class SubmitWorkResult(_message.Message):
    __slots__ = ("slave_constituent_id", "slave_incarnation_id")
    SLAVE_CONSTITUENT_ID_FIELD_NUMBER: _ClassVar[int]
    SLAVE_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    slave_constituent_id: int
    slave_incarnation_id: int
    def __init__(self, slave_constituent_id: _Optional[int] = ..., slave_incarnation_id: _Optional[int] = ...) -> None: ...

class ShutdownESArg(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ShutdownESResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class QueryRunningTasksArg(_message.Message):
    __slots__ = ("dispatcher_name",)
    DISPATCHER_NAME_FIELD_NUMBER: _ClassVar[int]
    dispatcher_name: str
    def __init__(self, dispatcher_name: _Optional[str] = ...) -> None: ...

class QueryRunningTasksResult(_message.Message):
    __slots__ = ("slave_session_id", "workid_vec")
    SLAVE_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    WORKID_VEC_FIELD_NUMBER: _ClassVar[int]
    slave_session_id: int
    workid_vec: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, slave_session_id: _Optional[int] = ..., workid_vec: _Optional[_Iterable[int]] = ...) -> None: ...

class PXGESDataMigrationArg(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PXGESDataMigrationResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
