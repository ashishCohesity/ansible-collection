from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class WireFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UNSPECIFIED: _ClassVar[WireFormat]
    PROTOBUF: _ClassVar[WireFormat]
    JSON: _ClassVar[WireFormat]
UNSPECIFIED: WireFormat
PROTOBUF: WireFormat
JSON: WireFormat

class ConformanceRequest(_message.Message):
    __slots__ = ("protobuf_payload", "json_payload", "requested_output_format", "message_type")
    PROTOBUF_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    JSON_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_OUTPUT_FORMAT_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    protobuf_payload: bytes
    json_payload: str
    requested_output_format: WireFormat
    message_type: str
    def __init__(self, protobuf_payload: _Optional[bytes] = ..., json_payload: _Optional[str] = ..., requested_output_format: _Optional[_Union[WireFormat, str]] = ..., message_type: _Optional[str] = ...) -> None: ...

class ConformanceResponse(_message.Message):
    __slots__ = ("parse_error", "serialize_error", "runtime_error", "protobuf_payload", "json_payload", "skipped")
    PARSE_ERROR_FIELD_NUMBER: _ClassVar[int]
    SERIALIZE_ERROR_FIELD_NUMBER: _ClassVar[int]
    RUNTIME_ERROR_FIELD_NUMBER: _ClassVar[int]
    PROTOBUF_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    JSON_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    SKIPPED_FIELD_NUMBER: _ClassVar[int]
    parse_error: str
    serialize_error: str
    runtime_error: str
    protobuf_payload: bytes
    json_payload: str
    skipped: str
    def __init__(self, parse_error: _Optional[str] = ..., serialize_error: _Optional[str] = ..., runtime_error: _Optional[str] = ..., protobuf_payload: _Optional[bytes] = ..., json_payload: _Optional[str] = ..., skipped: _Optional[str] = ...) -> None: ...
