from bifrost.base import error_pb2 as _error_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ListFilesArg(_message.Message):
    __slots__ = ("list_dir_path", "include_regex", "exclude_regex", "should_set_create_time")
    LIST_DIR_PATH_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_REGEX_FIELD_NUMBER: _ClassVar[int]
    EXCLUDE_REGEX_FIELD_NUMBER: _ClassVar[int]
    SHOULD_SET_CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    list_dir_path: str
    include_regex: str
    exclude_regex: str
    should_set_create_time: bool
    def __init__(self, list_dir_path: _Optional[str] = ..., include_regex: _Optional[str] = ..., exclude_regex: _Optional[str] = ..., should_set_create_time: bool = ...) -> None: ...

class ListFilesResult(_message.Message):
    __slots__ = ("file_vec",)
    class File(_message.Message):
        __slots__ = ("original_file_name", "original_size", "original_mtime_usecs", "create_time_usecs")
        ORIGINAL_FILE_NAME_FIELD_NUMBER: _ClassVar[int]
        ORIGINAL_SIZE_FIELD_NUMBER: _ClassVar[int]
        ORIGINAL_MTIME_USECS_FIELD_NUMBER: _ClassVar[int]
        CREATE_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
        original_file_name: bytes
        original_size: int
        original_mtime_usecs: int
        create_time_usecs: int
        def __init__(self, original_file_name: _Optional[bytes] = ..., original_size: _Optional[int] = ..., original_mtime_usecs: _Optional[int] = ..., create_time_usecs: _Optional[int] = ...) -> None: ...
    FILE_VEC_FIELD_NUMBER: _ClassVar[int]
    file_vec: _containers.RepeatedCompositeFieldContainer[ListFilesResult.File]
    def __init__(self, file_vec: _Optional[_Iterable[_Union[ListFilesResult.File, _Mapping]]] = ...) -> None: ...

class FetchFileArg(_message.Message):
    __slots__ = ("file_name", "offset_bytes", "limit_size_bytes", "compress_data")
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    OFFSET_BYTES_FIELD_NUMBER: _ClassVar[int]
    LIMIT_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    COMPRESS_DATA_FIELD_NUMBER: _ClassVar[int]
    file_name: bytes
    offset_bytes: int
    limit_size_bytes: int
    compress_data: bool
    def __init__(self, file_name: _Optional[bytes] = ..., offset_bytes: _Optional[int] = ..., limit_size_bytes: _Optional[int] = ..., compress_data: bool = ...) -> None: ...

class FetchFileResult(_message.Message):
    __slots__ = ("original_file_name", "data")
    ORIGINAL_FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    original_file_name: bytes
    data: bytes
    def __init__(self, original_file_name: _Optional[bytes] = ..., data: _Optional[bytes] = ...) -> None: ...

class BifrostDebugArg(_message.Message):
    __slots__ = ("type", "list_files_arg", "fetch_file_arg")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kListFiles: _ClassVar[BifrostDebugArg.Type]
        kFetchFile: _ClassVar[BifrostDebugArg.Type]
    kListFiles: BifrostDebugArg.Type
    kFetchFile: BifrostDebugArg.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    LIST_FILES_ARG_FIELD_NUMBER: _ClassVar[int]
    FETCH_FILE_ARG_FIELD_NUMBER: _ClassVar[int]
    type: BifrostDebugArg.Type
    list_files_arg: ListFilesArg
    fetch_file_arg: FetchFileArg
    def __init__(self, type: _Optional[_Union[BifrostDebugArg.Type, str]] = ..., list_files_arg: _Optional[_Union[ListFilesArg, _Mapping]] = ..., fetch_file_arg: _Optional[_Union[FetchFileArg, _Mapping]] = ...) -> None: ...

class BifrostDebugResult(_message.Message):
    __slots__ = ("error", "list_files_result", "fetch_file_result")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    LIST_FILES_RESULT_FIELD_NUMBER: _ClassVar[int]
    FETCH_FILE_RESULT_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    list_files_result: ListFilesResult
    fetch_file_result: FetchFileResult
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., list_files_result: _Optional[_Union[ListFilesResult, _Mapping]] = ..., fetch_file_result: _Optional[_Union[FetchFileResult, _Mapping]] = ...) -> None: ...
