from scribe.base import scribe_pb2 as _scribe_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class WorkloadTrace(_message.Message):
    __slots__ = ("request_details", "row", "caller_details", "server_details")
    class RequestDetails(_message.Message):
        __slots__ = ("request_type", "reason", "timestamp_usecs")
        class RequestType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kWrite: _ClassVar[WorkloadTrace.RequestDetails.RequestType]
            kRead: _ClassVar[WorkloadTrace.RequestDetails.RequestType]
            kReadWithWrite: _ClassVar[WorkloadTrace.RequestDetails.RequestType]
            kDelete: _ClassVar[WorkloadTrace.RequestDetails.RequestType]
        kWrite: WorkloadTrace.RequestDetails.RequestType
        kRead: WorkloadTrace.RequestDetails.RequestType
        kReadWithWrite: WorkloadTrace.RequestDetails.RequestType
        kDelete: WorkloadTrace.RequestDetails.RequestType
        REQUEST_TYPE_FIELD_NUMBER: _ClassVar[int]
        REASON_FIELD_NUMBER: _ClassVar[int]
        TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
        request_type: WorkloadTrace.RequestDetails.RequestType
        reason: bytes
        timestamp_usecs: int
        def __init__(self, request_type: _Optional[_Union[WorkloadTrace.RequestDetails.RequestType, str]] = ..., reason: _Optional[bytes] = ..., timestamp_usecs: _Optional[int] = ...) -> None: ...
    class RowDetails(_message.Message):
        __slots__ = ("key", "table_id", "bucket_id", "version")
        KEY_FIELD_NUMBER: _ClassVar[int]
        TABLE_ID_FIELD_NUMBER: _ClassVar[int]
        BUCKET_ID_FIELD_NUMBER: _ClassVar[int]
        VERSION_FIELD_NUMBER: _ClassVar[int]
        key: _scribe_pb2.RowColumnKey
        table_id: int
        bucket_id: int
        version: int
        def __init__(self, key: _Optional[_Union[_scribe_pb2.RowColumnKey, _Mapping]] = ..., table_id: _Optional[int] = ..., bucket_id: _Optional[int] = ..., version: _Optional[int] = ...) -> None: ...
    class CallerDetails(_message.Message):
        __slots__ = ("constituent_id", "incarnation_id")
        CONSTITUENT_ID_FIELD_NUMBER: _ClassVar[int]
        INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
        constituent_id: int
        incarnation_id: int
        def __init__(self, constituent_id: _Optional[int] = ..., incarnation_id: _Optional[int] = ...) -> None: ...
    class ServerDetails(_message.Message):
        __slots__ = ("constituent_id", "session_id", "tablet_id")
        CONSTITUENT_ID_FIELD_NUMBER: _ClassVar[int]
        SESSION_ID_FIELD_NUMBER: _ClassVar[int]
        TABLET_ID_FIELD_NUMBER: _ClassVar[int]
        constituent_id: int
        session_id: int
        tablet_id: int
        def __init__(self, constituent_id: _Optional[int] = ..., session_id: _Optional[int] = ..., tablet_id: _Optional[int] = ...) -> None: ...
    REQUEST_DETAILS_FIELD_NUMBER: _ClassVar[int]
    ROW_FIELD_NUMBER: _ClassVar[int]
    CALLER_DETAILS_FIELD_NUMBER: _ClassVar[int]
    SERVER_DETAILS_FIELD_NUMBER: _ClassVar[int]
    request_details: WorkloadTrace.RequestDetails
    row: WorkloadTrace.RowDetails
    caller_details: WorkloadTrace.CallerDetails
    server_details: WorkloadTrace.ServerDetails
    def __init__(self, request_details: _Optional[_Union[WorkloadTrace.RequestDetails, _Mapping]] = ..., row: _Optional[_Union[WorkloadTrace.RowDetails, _Mapping]] = ..., caller_details: _Optional[_Union[WorkloadTrace.CallerDetails, _Mapping]] = ..., server_details: _Optional[_Union[WorkloadTrace.ServerDetails, _Mapping]] = ...) -> None: ...
