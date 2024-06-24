from magneto.agents.windows.sql.base import sql_param_pb2 as _sql_param_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PingRequest(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class PingReply(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class Error(_message.Message):
    __slots__ = ("error_code", "error_msg")
    ERROR_CODE_FIELD_NUMBER: _ClassVar[int]
    ERROR_MSG_FIELD_NUMBER: _ClassVar[int]
    error_code: int
    error_msg: str
    def __init__(self, error_code: _Optional[int] = ..., error_msg: _Optional[str] = ...) -> None: ...

class ExecuteSQLStatementArg(_message.Message):
    __slots__ = ("query", "instance_name")
    QUERY_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_NAME_FIELD_NUMBER: _ClassVar[int]
    query: str
    instance_name: str
    def __init__(self, query: _Optional[str] = ..., instance_name: _Optional[str] = ...) -> None: ...

class ExecuteSQLStatementResponse(_message.Message):
    __slots__ = ("result", "err")
    RESULT_FIELD_NUMBER: _ClassVar[int]
    ERR_FIELD_NUMBER: _ClassVar[int]
    result: _sql_param_pb2.SQLResult
    err: Error
    def __init__(self, result: _Optional[_Union[_sql_param_pb2.SQLResult, _Mapping]] = ..., err: _Optional[_Union[Error, _Mapping]] = ...) -> None: ...

class GetInstanceNameToIdMapArg(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetInstanceNameToIdMapResponse(_message.Message):
    __slots__ = ("name_to_id", "err")
    class NameToIdEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAME_TO_ID_FIELD_NUMBER: _ClassVar[int]
    ERR_FIELD_NUMBER: _ClassVar[int]
    name_to_id: _containers.ScalarMap[str, str]
    err: Error
    def __init__(self, name_to_id: _Optional[_Mapping[str, str]] = ..., err: _Optional[_Union[Error, _Mapping]] = ...) -> None: ...

class GetInstanceIdArg(_message.Message):
    __slots__ = ("instance_name_string",)
    INSTANCE_NAME_STRING_FIELD_NUMBER: _ClassVar[int]
    instance_name_string: str
    def __init__(self, instance_name_string: _Optional[str] = ...) -> None: ...

class GetInstanceIdResponse(_message.Message):
    __slots__ = ("instance_id", "err")
    INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    ERR_FIELD_NUMBER: _ClassVar[int]
    instance_id: str
    err: Error
    def __init__(self, instance_id: _Optional[str] = ..., err: _Optional[_Union[Error, _Mapping]] = ...) -> None: ...

class IsInstanceOnlineArg(_message.Message):
    __slots__ = ("instance_name_string",)
    INSTANCE_NAME_STRING_FIELD_NUMBER: _ClassVar[int]
    instance_name_string: str
    def __init__(self, instance_name_string: _Optional[str] = ...) -> None: ...

class IsInstanceOnlineResponse(_message.Message):
    __slots__ = ("is_online", "err")
    IS_ONLINE_FIELD_NUMBER: _ClassVar[int]
    ERR_FIELD_NUMBER: _ClassVar[int]
    is_online: bool
    err: Error
    def __init__(self, is_online: bool = ..., err: _Optional[_Union[Error, _Mapping]] = ...) -> None: ...

class GetCommandArg(_message.Message):
    __slots__ = ("deviceset_id", "device_no", "data")
    DEVICESET_ID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_NO_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    deviceset_id: str
    device_no: int
    data: str
    def __init__(self, deviceset_id: _Optional[str] = ..., device_no: _Optional[int] = ..., data: _Optional[str] = ...) -> None: ...

class GetCommandResponse(_message.Message):
    __slots__ = ("error", "size", "position", "data", "commandcode")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    POSITION_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    COMMANDCODE_FIELD_NUMBER: _ClassVar[int]
    error: int
    size: int
    position: int
    data: str
    commandcode: int
    def __init__(self, error: _Optional[int] = ..., size: _Optional[int] = ..., position: _Optional[int] = ..., data: _Optional[str] = ..., commandcode: _Optional[int] = ...) -> None: ...

class CompleteCommandArg(_message.Message):
    __slots__ = ("deviceset_id", "device_no", "bytes_transferred", "position", "completion_code", "data")
    DEVICESET_ID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_NO_FIELD_NUMBER: _ClassVar[int]
    BYTES_TRANSFERRED_FIELD_NUMBER: _ClassVar[int]
    POSITION_FIELD_NUMBER: _ClassVar[int]
    COMPLETION_CODE_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    deviceset_id: str
    device_no: int
    bytes_transferred: int
    position: int
    completion_code: int
    data: str
    def __init__(self, deviceset_id: _Optional[str] = ..., device_no: _Optional[int] = ..., bytes_transferred: _Optional[int] = ..., position: _Optional[int] = ..., completion_code: _Optional[int] = ..., data: _Optional[str] = ...) -> None: ...

class CompleteCommandResponse(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: int
    def __init__(self, error: _Optional[int] = ...) -> None: ...

class CreateDeviceSetArg(_message.Message):
    __slots__ = ("deviceset_id", "instancename", "devicecount", "devicefeatures", "databasename")
    DEVICESET_ID_FIELD_NUMBER: _ClassVar[int]
    INSTANCENAME_FIELD_NUMBER: _ClassVar[int]
    DEVICECOUNT_FIELD_NUMBER: _ClassVar[int]
    DEVICEFEATURES_FIELD_NUMBER: _ClassVar[int]
    DATABASENAME_FIELD_NUMBER: _ClassVar[int]
    deviceset_id: str
    instancename: str
    devicecount: int
    devicefeatures: int
    databasename: str
    def __init__(self, deviceset_id: _Optional[str] = ..., instancename: _Optional[str] = ..., devicecount: _Optional[int] = ..., devicefeatures: _Optional[int] = ..., databasename: _Optional[str] = ...) -> None: ...

class CreateDeviceSetResponse(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: int
    def __init__(self, error: _Optional[int] = ...) -> None: ...

class ConfigureDeviceSetArg(_message.Message):
    __slots__ = ("deviceset_id",)
    DEVICESET_ID_FIELD_NUMBER: _ClassVar[int]
    deviceset_id: str
    def __init__(self, deviceset_id: _Optional[str] = ...) -> None: ...

class VDConfig(_message.Message):
    __slots__ = ("deviceCount", "features", "prefixZoneSize", "alignment", "softFileMarkBlockSize", "EOMWariningSize", "serverTimeout", "blocksize", "maxIODepth", "maxTransferSize", "bufferAreaSize")
    DEVICECOUNT_FIELD_NUMBER: _ClassVar[int]
    FEATURES_FIELD_NUMBER: _ClassVar[int]
    PREFIXZONESIZE_FIELD_NUMBER: _ClassVar[int]
    ALIGNMENT_FIELD_NUMBER: _ClassVar[int]
    SOFTFILEMARKBLOCKSIZE_FIELD_NUMBER: _ClassVar[int]
    EOMWARININGSIZE_FIELD_NUMBER: _ClassVar[int]
    SERVERTIMEOUT_FIELD_NUMBER: _ClassVar[int]
    BLOCKSIZE_FIELD_NUMBER: _ClassVar[int]
    MAXIODEPTH_FIELD_NUMBER: _ClassVar[int]
    MAXTRANSFERSIZE_FIELD_NUMBER: _ClassVar[int]
    BUFFERAREASIZE_FIELD_NUMBER: _ClassVar[int]
    deviceCount: int
    features: int
    prefixZoneSize: int
    alignment: int
    softFileMarkBlockSize: int
    EOMWariningSize: int
    serverTimeout: int
    blocksize: int
    maxIODepth: int
    maxTransferSize: int
    bufferAreaSize: int
    def __init__(self, deviceCount: _Optional[int] = ..., features: _Optional[int] = ..., prefixZoneSize: _Optional[int] = ..., alignment: _Optional[int] = ..., softFileMarkBlockSize: _Optional[int] = ..., EOMWariningSize: _Optional[int] = ..., serverTimeout: _Optional[int] = ..., blocksize: _Optional[int] = ..., maxIODepth: _Optional[int] = ..., maxTransferSize: _Optional[int] = ..., bufferAreaSize: _Optional[int] = ...) -> None: ...

class ConfigureDeviceSetResponse(_message.Message):
    __slots__ = ("error", "VDC_config")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    VDC_CONFIG_FIELD_NUMBER: _ClassVar[int]
    error: int
    VDC_config: VDConfig
    def __init__(self, error: _Optional[int] = ..., VDC_config: _Optional[_Union[VDConfig, _Mapping]] = ...) -> None: ...

class OpenDeviceArg(_message.Message):
    __slots__ = ("deviceset_id", "device_no")
    DEVICESET_ID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_NO_FIELD_NUMBER: _ClassVar[int]
    deviceset_id: str
    device_no: int
    def __init__(self, deviceset_id: _Optional[str] = ..., device_no: _Optional[int] = ...) -> None: ...

class OpenDeviceResponse(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: int
    def __init__(self, error: _Optional[int] = ...) -> None: ...

class CloseDeviceArg(_message.Message):
    __slots__ = ("deviceset_id", "issue_abort")
    DEVICESET_ID_FIELD_NUMBER: _ClassVar[int]
    ISSUE_ABORT_FIELD_NUMBER: _ClassVar[int]
    deviceset_id: str
    issue_abort: int
    def __init__(self, deviceset_id: _Optional[str] = ..., issue_abort: _Optional[int] = ...) -> None: ...

class CloseDeviceResponse(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: int
    def __init__(self, error: _Optional[int] = ...) -> None: ...

class GetProgressArg(_message.Message):
    __slots__ = ("backupid",)
    BACKUPID_FIELD_NUMBER: _ClassVar[int]
    backupid: str
    def __init__(self, backupid: _Optional[str] = ...) -> None: ...

class GetProgressResponse(_message.Message):
    __slots__ = ("percentage_completed", "error")
    PERCENTAGE_COMPLETED_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    percentage_completed: int
    error: int
    def __init__(self, percentage_completed: _Optional[int] = ..., error: _Optional[int] = ...) -> None: ...
