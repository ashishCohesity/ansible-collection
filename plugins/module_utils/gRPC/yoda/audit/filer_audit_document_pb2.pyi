from yoda.es import jsonname_pb2 as _jsonname_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ErrorProto(_message.Message):
    __slots__ = ("type", "error_msg")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNoError: _ClassVar[ErrorProto.Type]
        kTimeout: _ClassVar[ErrorProto.Type]
        kInvalid: _ClassVar[ErrorProto.Type]
        kServiceUnavailable: _ClassVar[ErrorProto.Type]
        kAccessDenied: _ClassVar[ErrorProto.Type]
        kUnknownError: _ClassVar[ErrorProto.Type]
        kNotFound: _ClassVar[ErrorProto.Type]
        kMountFailure: _ClassVar[ErrorProto.Type]
        kIOError: _ClassVar[ErrorProto.Type]
    kNoError: ErrorProto.Type
    kTimeout: ErrorProto.Type
    kInvalid: ErrorProto.Type
    kServiceUnavailable: ErrorProto.Type
    kAccessDenied: ErrorProto.Type
    kUnknownError: ErrorProto.Type
    kNotFound: ErrorProto.Type
    kMountFailure: ErrorProto.Type
    kIOError: ErrorProto.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ERROR_MSG_FIELD_NUMBER: _ClassVar[int]
    type: ErrorProto.Type
    error_msg: str
    def __init__(self, type: _Optional[_Union[ErrorProto.Type, str]] = ..., error_msg: _Optional[str] = ...) -> None: ...

class FilerAuditDocument(_message.Message):
    __slots__ = ("timestamp_usecs", "view_id", "user_name", "user_group", "client_ip", "action_name", "status", "file_name", "error", "attribute_map")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kSuccess: _ClassVar[FilerAuditDocument.Status]
        kFailure: _ClassVar[FilerAuditDocument.Status]
    kSuccess: FilerAuditDocument.Status
    kFailure: FilerAuditDocument.Status
    class KeyValuePair(_message.Message):
        __slots__ = ("_key", "_value")
        _KEY_FIELD_NUMBER: _ClassVar[int]
        _VALUE_FIELD_NUMBER: _ClassVar[int]
        _key: str
        _value: str
        def __init__(self, _key: _Optional[str] = ..., _value: _Optional[str] = ...) -> None: ...
    TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
    VIEW_ID_FIELD_NUMBER: _ClassVar[int]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    USER_GROUP_FIELD_NUMBER: _ClassVar[int]
    CLIENT_IP_FIELD_NUMBER: _ClassVar[int]
    ACTION_NAME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTE_MAP_FIELD_NUMBER: _ClassVar[int]
    timestamp_usecs: int
    view_id: int
    user_name: bytes
    user_group: str
    client_ip: str
    action_name: str
    status: FilerAuditDocument.Status
    file_name: bytes
    error: ErrorProto
    attribute_map: _containers.RepeatedCompositeFieldContainer[FilerAuditDocument.KeyValuePair]
    def __init__(self, timestamp_usecs: _Optional[int] = ..., view_id: _Optional[int] = ..., user_name: _Optional[bytes] = ..., user_group: _Optional[str] = ..., client_ip: _Optional[str] = ..., action_name: _Optional[str] = ..., status: _Optional[_Union[FilerAuditDocument.Status, str]] = ..., file_name: _Optional[bytes] = ..., error: _Optional[_Union[ErrorProto, _Mapping]] = ..., attribute_map: _Optional[_Iterable[_Union[FilerAuditDocument.KeyValuePair, _Mapping]]] = ...) -> None: ...
