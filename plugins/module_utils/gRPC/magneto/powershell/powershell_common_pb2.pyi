from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PSInvocationInfo(_message.Message):
    __slots__ = ("ScriptLineNumber", "PSCommandPath")
    SCRIPTLINENUMBER_FIELD_NUMBER: _ClassVar[int]
    PSCOMMANDPATH_FIELD_NUMBER: _ClassVar[int]
    ScriptLineNumber: int
    PSCommandPath: str
    def __init__(self, ScriptLineNumber: _Optional[int] = ..., PSCommandPath: _Optional[str] = ...) -> None: ...

class PSCategoryInfo(_message.Message):
    __slots__ = ("Category", "Reason")
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    Category: int
    Reason: str
    def __init__(self, Category: _Optional[int] = ..., Reason: _Optional[str] = ...) -> None: ...

class PSException(_message.Message):
    __slots__ = ("Message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    Message: str
    def __init__(self, Message: _Optional[str] = ...) -> None: ...

class PSExceptionStack(_message.Message):
    __slots__ = ("Exception", "CategoryInfo", "InvocationInfo")
    EXCEPTION_FIELD_NUMBER: _ClassVar[int]
    CATEGORYINFO_FIELD_NUMBER: _ClassVar[int]
    INVOCATIONINFO_FIELD_NUMBER: _ClassVar[int]
    Exception: PSException
    CategoryInfo: PSCategoryInfo
    InvocationInfo: PSInvocationInfo
    def __init__(self, Exception: _Optional[_Union[PSException, _Mapping]] = ..., CategoryInfo: _Optional[_Union[PSCategoryInfo, _Mapping]] = ..., InvocationInfo: _Optional[_Union[PSInvocationInfo, _Mapping]] = ...) -> None: ...

class PSStringTuple(_message.Message):
    __slots__ = ("key_str", "value_str")
    KEY_STR_FIELD_NUMBER: _ClassVar[int]
    VALUE_STR_FIELD_NUMBER: _ClassVar[int]
    key_str: str
    value_str: str
    def __init__(self, key_str: _Optional[str] = ..., value_str: _Optional[str] = ...) -> None: ...

class PSGenericInputDataInternal(_message.Message):
    __slots__ = ("params_vec", "result_dir", "task_name", "task_id", "timeout_sec", "retry_onfailure_count", "exit_error")
    PARAMS_VEC_FIELD_NUMBER: _ClassVar[int]
    RESULT_DIR_FIELD_NUMBER: _ClassVar[int]
    TASK_NAME_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_SEC_FIELD_NUMBER: _ClassVar[int]
    RETRY_ONFAILURE_COUNT_FIELD_NUMBER: _ClassVar[int]
    EXIT_ERROR_FIELD_NUMBER: _ClassVar[int]
    params_vec: _containers.RepeatedCompositeFieldContainer[PSStringTuple]
    result_dir: str
    task_name: str
    task_id: int
    timeout_sec: int
    retry_onfailure_count: int
    exit_error: int
    def __init__(self, params_vec: _Optional[_Iterable[_Union[PSStringTuple, _Mapping]]] = ..., result_dir: _Optional[str] = ..., task_name: _Optional[str] = ..., task_id: _Optional[int] = ..., timeout_sec: _Optional[int] = ..., retry_onfailure_count: _Optional[int] = ..., exit_error: _Optional[int] = ...) -> None: ...
