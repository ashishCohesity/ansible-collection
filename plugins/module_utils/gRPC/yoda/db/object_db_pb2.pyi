from yoda.db import documents_pb2 as _documents_pb2
from yoda.base import reports_pb2 as _reports_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ObjectDbRow(_message.Message):
    __slots__ = ("document", "report")
    DOCUMENT_FIELD_NUMBER: _ClassVar[int]
    REPORT_FIELD_NUMBER: _ClassVar[int]
    document: _documents_pb2.ObjectSnapshotDocument
    report: _reports_pb2.YodaReport
    def __init__(self, document: _Optional[_Union[_documents_pb2.ObjectSnapshotDocument, _Mapping]] = ..., report: _Optional[_Union[_reports_pb2.YodaReport, _Mapping]] = ...) -> None: ...
