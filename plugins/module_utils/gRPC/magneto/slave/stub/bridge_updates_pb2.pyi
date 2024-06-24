from bridge.base import error_pb2 as _error_pb2
from magneto.base import api_version_pb2 as _api_version_pb2
from magneto.base import enums_pb2 as _enums_pb2
from util.base import op_clock_pb2 as _op_clock_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import python_message as _python_message
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ActionUpdateArg(_message.Message):
    __slots__ = ("api_version", "slave_op_clock", "type", "task_id", "sub_task_id", "error", "fetch_files_update_arg")
    Extensions: _python_message._ExtensionDict
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    SLAVE_OP_CLOCK_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    SUB_TASK_ID_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    FETCH_FILES_UPDATE_ARG_FIELD_NUMBER: _ClassVar[int]
    api_version: _api_version_pb2.APIVersion
    slave_op_clock: _op_clock_pb2.OpClock
    type: _enums_pb2.Environment.Type
    task_id: int
    sub_task_id: int
    error: _error_pb2.ErrorProto
    fetch_files_update_arg: FetchFilesUpdateArg
    def __init__(self, api_version: _Optional[_Union[_api_version_pb2.APIVersion, _Mapping]] = ..., slave_op_clock: _Optional[_Union[_op_clock_pb2.OpClock, _Mapping]] = ..., type: _Optional[_Union[_enums_pb2.Environment.Type, str]] = ..., task_id: _Optional[int] = ..., sub_task_id: _Optional[int] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., fetch_files_update_arg: _Optional[_Union[FetchFilesUpdateArg, _Mapping]] = ...) -> None: ...

class ActionUpdateResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class FetchFilesUpdateArg(_message.Message):
    __slots__ = ("dir_vec",)
    class Dir(_message.Message):
        __slots__ = ("full_dir_path", "file_vec", "error")
        class File(_message.Message):
            __slots__ = ("file_name", "data", "error")
            FILE_NAME_FIELD_NUMBER: _ClassVar[int]
            DATA_FIELD_NUMBER: _ClassVar[int]
            ERROR_FIELD_NUMBER: _ClassVar[int]
            file_name: str
            data: bytes
            error: _error_pb2.ErrorProto
            def __init__(self, file_name: _Optional[str] = ..., data: _Optional[bytes] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...
        FULL_DIR_PATH_FIELD_NUMBER: _ClassVar[int]
        FILE_VEC_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        full_dir_path: str
        file_vec: _containers.RepeatedCompositeFieldContainer[FetchFilesUpdateArg.Dir.File]
        error: _error_pb2.ErrorProto
        def __init__(self, full_dir_path: _Optional[str] = ..., file_vec: _Optional[_Iterable[_Union[FetchFilesUpdateArg.Dir.File, _Mapping]]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...
    DIR_VEC_FIELD_NUMBER: _ClassVar[int]
    dir_vec: _containers.RepeatedCompositeFieldContainer[FetchFilesUpdateArg.Dir]
    def __init__(self, dir_vec: _Optional[_Iterable[_Union[FetchFilesUpdateArg.Dir, _Mapping]]] = ...) -> None: ...
