from yoda.base import error_pb2 as _error_pb2
from yoda.audit import cluster_audit_document_pb2 as _cluster_audit_document_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetClusterAccessAuditReportArg(_message.Message):
    __slots__ = ("report_type", "start_time_secs", "end_time_secs", "user_name", "action", "entity_type", "entity_id", "page_size")
    class ReportType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kCustom: _ClassVar[GetClusterAccessAuditReportArg.ReportType]
    kCustom: GetClusterAccessAuditReportArg.ReportType
    REPORT_TYPE_FIELD_NUMBER: _ClassVar[int]
    START_TIME_SECS_FIELD_NUMBER: _ClassVar[int]
    END_TIME_SECS_FIELD_NUMBER: _ClassVar[int]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    ENTITY_TYPE_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    report_type: GetClusterAccessAuditReportArg.ReportType
    start_time_secs: int
    end_time_secs: int
    user_name: str
    action: str
    entity_type: str
    entity_id: int
    page_size: int
    def __init__(self, report_type: _Optional[_Union[GetClusterAccessAuditReportArg.ReportType, str]] = ..., start_time_secs: _Optional[int] = ..., end_time_secs: _Optional[int] = ..., user_name: _Optional[str] = ..., action: _Optional[str] = ..., entity_type: _Optional[str] = ..., entity_id: _Optional[int] = ..., page_size: _Optional[int] = ...) -> None: ...

class GetClusterAccessAuditReportResult(_message.Message):
    __slots__ = ("error", "access_docs")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ACCESS_DOCS_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    access_docs: _containers.RepeatedCompositeFieldContainer[_cluster_audit_document_pb2.ClusterAccessAuditDocument]
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., access_docs: _Optional[_Iterable[_Union[_cluster_audit_document_pb2.ClusterAccessAuditDocument, _Mapping]]] = ...) -> None: ...

class GetClusterNotificationAuditReportArg(_message.Message):
    __slots__ = ("start_time_secs", "end_time_secs", "category_type", "category_name", "severity", "page_size")
    START_TIME_SECS_FIELD_NUMBER: _ClassVar[int]
    END_TIME_SECS_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_TYPE_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_NAME_FIELD_NUMBER: _ClassVar[int]
    SEVERITY_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    start_time_secs: int
    end_time_secs: int
    category_type: str
    category_name: str
    severity: str
    page_size: int
    def __init__(self, start_time_secs: _Optional[int] = ..., end_time_secs: _Optional[int] = ..., category_type: _Optional[str] = ..., category_name: _Optional[str] = ..., severity: _Optional[str] = ..., page_size: _Optional[int] = ...) -> None: ...

class GetClusterNotificationAuditReportResult(_message.Message):
    __slots__ = ("error", "notification_docs")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    NOTIFICATION_DOCS_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    notification_docs: _containers.RepeatedCompositeFieldContainer[_cluster_audit_document_pb2.ClusterNotificationAuditDocument]
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., notification_docs: _Optional[_Iterable[_Union[_cluster_audit_document_pb2.ClusterNotificationAuditDocument, _Mapping]]] = ...) -> None: ...
