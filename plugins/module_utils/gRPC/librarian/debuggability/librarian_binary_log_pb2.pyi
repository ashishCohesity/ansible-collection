from bridge.base import error_pb2 as _error_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AzureWriteLogProto(_message.Message):
    __slots__ = ("op_type", "op_data")
    class OperationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kUnknown: _ClassVar[AzureWriteLogProto.OperationType]
        kAddToCache: _ClassVar[AzureWriteLogProto.OperationType]
        kAppendEntry: _ClassVar[AzureWriteLogProto.OperationType]
        kAppend: _ClassVar[AzureWriteLogProto.OperationType]
        kAppendExit: _ClassVar[AzureWriteLogProto.OperationType]
        kWriteEntry: _ClassVar[AzureWriteLogProto.OperationType]
        kWrite: _ClassVar[AzureWriteLogProto.OperationType]
        kWriteExit: _ClassVar[AzureWriteLogProto.OperationType]
        kFlush: _ClassVar[AzureWriteLogProto.OperationType]
        kClose: _ClassVar[AzureWriteLogProto.OperationType]
        kSync: _ClassVar[AzureWriteLogProto.OperationType]
        kFSync: _ClassVar[AzureWriteLogProto.OperationType]
        kFileSize: _ClassVar[AzureWriteLogProto.OperationType]
        kTruncateEntry: _ClassVar[AzureWriteLogProto.OperationType]
        kTruncate: _ClassVar[AzureWriteLogProto.OperationType]
        kTruncateExit: _ClassVar[AzureWriteLogProto.OperationType]
    kUnknown: AzureWriteLogProto.OperationType
    kAddToCache: AzureWriteLogProto.OperationType
    kAppendEntry: AzureWriteLogProto.OperationType
    kAppend: AzureWriteLogProto.OperationType
    kAppendExit: AzureWriteLogProto.OperationType
    kWriteEntry: AzureWriteLogProto.OperationType
    kWrite: AzureWriteLogProto.OperationType
    kWriteExit: AzureWriteLogProto.OperationType
    kFlush: AzureWriteLogProto.OperationType
    kClose: AzureWriteLogProto.OperationType
    kSync: AzureWriteLogProto.OperationType
    kFSync: AzureWriteLogProto.OperationType
    kFileSize: AzureWriteLogProto.OperationType
    kTruncateEntry: AzureWriteLogProto.OperationType
    kTruncate: AzureWriteLogProto.OperationType
    kTruncateExit: AzureWriteLogProto.OperationType
    class TruncateParams(_message.Message):
        __slots__ = ("new_size", "total_size")
        NEW_SIZE_FIELD_NUMBER: _ClassVar[int]
        TOTAL_SIZE_FIELD_NUMBER: _ClassVar[int]
        new_size: int
        total_size: int
        def __init__(self, new_size: _Optional[int] = ..., total_size: _Optional[int] = ...) -> None: ...
    class AddToCacheParams(_message.Message):
        __slots__ = ("offset", "size")
        OFFSET_FIELD_NUMBER: _ClassVar[int]
        SIZE_FIELD_NUMBER: _ClassVar[int]
        offset: int
        size: int
        def __init__(self, offset: _Optional[int] = ..., size: _Optional[int] = ...) -> None: ...
    class WriteParams(_message.Message):
        __slots__ = ("finalize",)
        FINALIZE_FIELD_NUMBER: _ClassVar[int]
        finalize: bool
        def __init__(self, finalize: bool = ...) -> None: ...
    class OperationData(_message.Message):
        __slots__ = ("truncate_params", "add_to_cache_params", "write_params")
        TRUNCATE_PARAMS_FIELD_NUMBER: _ClassVar[int]
        ADD_TO_CACHE_PARAMS_FIELD_NUMBER: _ClassVar[int]
        WRITE_PARAMS_FIELD_NUMBER: _ClassVar[int]
        truncate_params: AzureWriteLogProto.TruncateParams
        add_to_cache_params: AzureWriteLogProto.AddToCacheParams
        write_params: AzureWriteLogProto.WriteParams
        def __init__(self, truncate_params: _Optional[_Union[AzureWriteLogProto.TruncateParams, _Mapping]] = ..., add_to_cache_params: _Optional[_Union[AzureWriteLogProto.AddToCacheParams, _Mapping]] = ..., write_params: _Optional[_Union[AzureWriteLogProto.WriteParams, _Mapping]] = ...) -> None: ...
    OP_TYPE_FIELD_NUMBER: _ClassVar[int]
    OP_DATA_FIELD_NUMBER: _ClassVar[int]
    op_type: AzureWriteLogProto.OperationType
    op_data: AzureWriteLogProto.OperationData
    def __init__(self, op_type: _Optional[_Union[AzureWriteLogProto.OperationType, str]] = ..., op_data: _Optional[_Union[AzureWriteLogProto.OperationData, _Mapping]] = ...) -> None: ...

class AzureRocksDBEnvLogProto(_message.Message):
    __slots__ = ("op_type", "op_data")
    class OperationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kUnknown: _ClassVar[AzureRocksDBEnvLogProto.OperationType]
        kWritableFile: _ClassVar[AzureRocksDBEnvLogProto.OperationType]
        kDeleteFile: _ClassVar[AzureRocksDBEnvLogProto.OperationType]
        kRenameFile: _ClassVar[AzureRocksDBEnvLogProto.OperationType]
        kCreateDir: _ClassVar[AzureRocksDBEnvLogProto.OperationType]
        kDeleteDir: _ClassVar[AzureRocksDBEnvLogProto.OperationType]
        kFileSize: _ClassVar[AzureRocksDBEnvLogProto.OperationType]
        kFileModificationTime: _ClassVar[AzureRocksDBEnvLogProto.OperationType]
        kWrite: _ClassVar[AzureRocksDBEnvLogProto.OperationType]
        kWriteRetry: _ClassVar[AzureRocksDBEnvLogProto.OperationType]
        kCreateObject: _ClassVar[AzureRocksDBEnvLogProto.OperationType]
        kReadEntry: _ClassVar[AzureRocksDBEnvLogProto.OperationType]
        kRead: _ClassVar[AzureRocksDBEnvLogProto.OperationType]
        kReadExit: _ClassVar[AzureRocksDBEnvLogProto.OperationType]
        kDownload: _ClassVar[AzureRocksDBEnvLogProto.OperationType]
        kGetObjectMetadata: _ClassVar[AzureRocksDBEnvLogProto.OperationType]
        kFinalizeObject: _ClassVar[AzureRocksDBEnvLogProto.OperationType]
        kFinalizeObjectAbort: _ClassVar[AzureRocksDBEnvLogProto.OperationType]
        kFinalizeObjectExit: _ClassVar[AzureRocksDBEnvLogProto.OperationType]
        kRefreshConnectionEntry: _ClassVar[AzureRocksDBEnvLogProto.OperationType]
        kRefreshConnectionExit: _ClassVar[AzureRocksDBEnvLogProto.OperationType]
        kFileExists: _ClassVar[AzureRocksDBEnvLogProto.OperationType]
        kListObjectsEntry: _ClassVar[AzureRocksDBEnvLogProto.OperationType]
        kListObjects: _ClassVar[AzureRocksDBEnvLogProto.OperationType]
        kListObjectsExit: _ClassVar[AzureRocksDBEnvLogProto.OperationType]
    kUnknown: AzureRocksDBEnvLogProto.OperationType
    kWritableFile: AzureRocksDBEnvLogProto.OperationType
    kDeleteFile: AzureRocksDBEnvLogProto.OperationType
    kRenameFile: AzureRocksDBEnvLogProto.OperationType
    kCreateDir: AzureRocksDBEnvLogProto.OperationType
    kDeleteDir: AzureRocksDBEnvLogProto.OperationType
    kFileSize: AzureRocksDBEnvLogProto.OperationType
    kFileModificationTime: AzureRocksDBEnvLogProto.OperationType
    kWrite: AzureRocksDBEnvLogProto.OperationType
    kWriteRetry: AzureRocksDBEnvLogProto.OperationType
    kCreateObject: AzureRocksDBEnvLogProto.OperationType
    kReadEntry: AzureRocksDBEnvLogProto.OperationType
    kRead: AzureRocksDBEnvLogProto.OperationType
    kReadExit: AzureRocksDBEnvLogProto.OperationType
    kDownload: AzureRocksDBEnvLogProto.OperationType
    kGetObjectMetadata: AzureRocksDBEnvLogProto.OperationType
    kFinalizeObject: AzureRocksDBEnvLogProto.OperationType
    kFinalizeObjectAbort: AzureRocksDBEnvLogProto.OperationType
    kFinalizeObjectExit: AzureRocksDBEnvLogProto.OperationType
    kRefreshConnectionEntry: AzureRocksDBEnvLogProto.OperationType
    kRefreshConnectionExit: AzureRocksDBEnvLogProto.OperationType
    kFileExists: AzureRocksDBEnvLogProto.OperationType
    kListObjectsEntry: AzureRocksDBEnvLogProto.OperationType
    kListObjects: AzureRocksDBEnvLogProto.OperationType
    kListObjectsExit: AzureRocksDBEnvLogProto.OperationType
    class FileSizeParams(_message.Message):
        __slots__ = ("size",)
        SIZE_FIELD_NUMBER: _ClassVar[int]
        size: int
        def __init__(self, size: _Optional[int] = ...) -> None: ...
    class FileModificationTimeParams(_message.Message):
        __slots__ = ("time",)
        TIME_FIELD_NUMBER: _ClassVar[int]
        time: int
        def __init__(self, time: _Optional[int] = ...) -> None: ...
    class FileWriteParams(_message.Message):
        __slots__ = ("offset", "part_num", "retry_count")
        OFFSET_FIELD_NUMBER: _ClassVar[int]
        PART_NUM_FIELD_NUMBER: _ClassVar[int]
        RETRY_COUNT_FIELD_NUMBER: _ClassVar[int]
        offset: int
        part_num: int
        retry_count: int
        def __init__(self, offset: _Optional[int] = ..., part_num: _Optional[int] = ..., retry_count: _Optional[int] = ...) -> None: ...
    class OperationData(_message.Message):
        __slots__ = ("file_size_params", "file_modification_params", "file_write_params")
        FILE_SIZE_PARAMS_FIELD_NUMBER: _ClassVar[int]
        FILE_MODIFICATION_PARAMS_FIELD_NUMBER: _ClassVar[int]
        FILE_WRITE_PARAMS_FIELD_NUMBER: _ClassVar[int]
        file_size_params: AzureRocksDBEnvLogProto.FileSizeParams
        file_modification_params: AzureRocksDBEnvLogProto.FileModificationTimeParams
        file_write_params: AzureRocksDBEnvLogProto.FileWriteParams
        def __init__(self, file_size_params: _Optional[_Union[AzureRocksDBEnvLogProto.FileSizeParams, _Mapping]] = ..., file_modification_params: _Optional[_Union[AzureRocksDBEnvLogProto.FileModificationTimeParams, _Mapping]] = ..., file_write_params: _Optional[_Union[AzureRocksDBEnvLogProto.FileWriteParams, _Mapping]] = ...) -> None: ...
    OP_TYPE_FIELD_NUMBER: _ClassVar[int]
    OP_DATA_FIELD_NUMBER: _ClassVar[int]
    op_type: AzureRocksDBEnvLogProto.OperationType
    op_data: AzureRocksDBEnvLogProto.OperationData
    def __init__(self, op_type: _Optional[_Union[AzureRocksDBEnvLogProto.OperationType, str]] = ..., op_data: _Optional[_Union[AzureRocksDBEnvLogProto.OperationData, _Mapping]] = ...) -> None: ...

class AzureRocksDBLogProto(_message.Message):
    __slots__ = ("component", "error")
    class Component(_message.Message):
        __slots__ = ("env_log", "write_log")
        ENV_LOG_FIELD_NUMBER: _ClassVar[int]
        WRITE_LOG_FIELD_NUMBER: _ClassVar[int]
        env_log: AzureRocksDBEnvLogProto
        write_log: AzureWriteLogProto
        def __init__(self, env_log: _Optional[_Union[AzureRocksDBEnvLogProto, _Mapping]] = ..., write_log: _Optional[_Union[AzureWriteLogProto, _Mapping]] = ...) -> None: ...
    COMPONENT_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    component: AzureRocksDBLogProto.Component
    error: _error_pb2.ErrorProto
    def __init__(self, component: _Optional[_Union[AzureRocksDBLogProto.Component, _Mapping]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class RocksDBLogProto(_message.Message):
    __slots__ = ("object_name", "platform_log", "message")
    class PlatformLog(_message.Message):
        __slots__ = ("azure_log",)
        AZURE_LOG_FIELD_NUMBER: _ClassVar[int]
        azure_log: AzureRocksDBLogProto
        def __init__(self, azure_log: _Optional[_Union[AzureRocksDBLogProto, _Mapping]] = ...) -> None: ...
    OBJECT_NAME_FIELD_NUMBER: _ClassVar[int]
    PLATFORM_LOG_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    object_name: str
    platform_log: RocksDBLogProto.PlatformLog
    message: str
    def __init__(self, object_name: _Optional[str] = ..., platform_log: _Optional[_Union[RocksDBLogProto.PlatformLog, _Mapping]] = ..., message: _Optional[str] = ...) -> None: ...

class LibrarianLogProto(_message.Message):
    __slots__ = ("component_log",)
    class LibrarianComponentLog(_message.Message):
        __slots__ = ("rocks_db_log",)
        ROCKS_DB_LOG_FIELD_NUMBER: _ClassVar[int]
        rocks_db_log: RocksDBLogProto
        def __init__(self, rocks_db_log: _Optional[_Union[RocksDBLogProto, _Mapping]] = ...) -> None: ...
    COMPONENT_LOG_FIELD_NUMBER: _ClassVar[int]
    component_log: LibrarianLogProto.LibrarianComponentLog
    def __init__(self, component_log: _Optional[_Union[LibrarianLogProto.LibrarianComponentLog, _Mapping]] = ...) -> None: ...
