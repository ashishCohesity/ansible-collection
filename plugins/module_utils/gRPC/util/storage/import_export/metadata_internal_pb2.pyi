from util.storage import error_pb2 as _error_pb2
from util.storage.import_export import api_pb2 as _api_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ExportIdentifier(_message.Message):
    __slots__ = ("service_identifier", "export_usec", "export_sequence_number", "export_id")
    SERVICE_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    EXPORT_USEC_FIELD_NUMBER: _ClassVar[int]
    EXPORT_SEQUENCE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    EXPORT_ID_FIELD_NUMBER: _ClassVar[int]
    service_identifier: str
    export_usec: int
    export_sequence_number: int
    export_id: str
    def __init__(self, service_identifier: _Optional[str] = ..., export_usec: _Optional[int] = ..., export_sequence_number: _Optional[int] = ..., export_id: _Optional[str] = ...) -> None: ...

class ImportExportMetadata(_message.Message):
    __slots__ = ("export_identifier", "num_data_files", "export_status", "error", "marked_for_gc")
    EXPORT_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    NUM_DATA_FILES_FIELD_NUMBER: _ClassVar[int]
    EXPORT_STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    MARKED_FOR_GC_FIELD_NUMBER: _ClassVar[int]
    export_identifier: ExportIdentifier
    num_data_files: int
    export_status: _api_pb2.ExportStatus
    error: _error_pb2.ErrorProto
    marked_for_gc: bool
    def __init__(self, export_identifier: _Optional[_Union[ExportIdentifier, _Mapping]] = ..., num_data_files: _Optional[int] = ..., export_status: _Optional[_Union[_api_pb2.ExportStatus, str]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., marked_for_gc: bool = ...) -> None: ...

class Cookie(_message.Message):
    __slots__ = ("import_export_id", "last_data_file", "last_sequence_number")
    IMPORT_EXPORT_ID_FIELD_NUMBER: _ClassVar[int]
    LAST_DATA_FILE_FIELD_NUMBER: _ClassVar[int]
    LAST_SEQUENCE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    import_export_id: str
    last_data_file: str
    last_sequence_number: int
    def __init__(self, import_export_id: _Optional[str] = ..., last_data_file: _Optional[str] = ..., last_sequence_number: _Optional[int] = ...) -> None: ...
