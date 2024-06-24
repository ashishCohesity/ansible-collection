from open_util.net import protorpc_pb2 as _protorpc_pb2
from yoda.audit import cluster_audit_report_pb2 as _cluster_audit_report_pb2
from yoda.base import error_pb2 as _error_pb2
from yoda.base import reports_pb2 as _reports_pb2
from yoda.base import yoda_pb2 as _yoda_pb2
from yoda.master.stub import yoda_rpc_args_pb2 as _yoda_rpc_args_pb2
from google.protobuf.internal import python_message as _python_message
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UpdateSlaveTaskArg(_message.Message):
    __slots__ = ("task_id", "constituent_id", "incarnation_id", "error", "report")
    Extensions: _python_message._ExtensionDict
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    CONSTITUENT_ID_FIELD_NUMBER: _ClassVar[int]
    INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    REPORT_FIELD_NUMBER: _ClassVar[int]
    task_id: int
    constituent_id: int
    incarnation_id: int
    error: _error_pb2.ErrorProto
    report: _reports_pb2.YodaReport
    def __init__(self, task_id: _Optional[int] = ..., constituent_id: _Optional[int] = ..., incarnation_id: _Optional[int] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., report: _Optional[_Union[_reports_pb2.YodaReport, _Mapping]] = ...) -> None: ...

class UpdateSlaveTaskResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UpdateLibrarianMigrationWorkArg(_message.Message):
    __slots__ = ("task_id", "constituent_id", "incarnation_id", "error")
    Extensions: _python_message._ExtensionDict
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    CONSTITUENT_ID_FIELD_NUMBER: _ClassVar[int]
    INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    task_id: int
    constituent_id: int
    incarnation_id: int
    error: _error_pb2.ErrorProto
    def __init__(self, task_id: _Optional[int] = ..., constituent_id: _Optional[int] = ..., incarnation_id: _Optional[int] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class UpdateLibrarianMigrationWorkResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UpdateSlaveAuditTaskArg(_message.Message):
    __slots__ = ("task_id", "constituent_id", "incarnation_id", "error")
    Extensions: _python_message._ExtensionDict
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    CONSTITUENT_ID_FIELD_NUMBER: _ClassVar[int]
    INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    task_id: int
    constituent_id: int
    incarnation_id: int
    error: _error_pb2.ErrorProto
    def __init__(self, task_id: _Optional[int] = ..., constituent_id: _Optional[int] = ..., incarnation_id: _Optional[int] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class UpdateSlaveAuditTaskResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
