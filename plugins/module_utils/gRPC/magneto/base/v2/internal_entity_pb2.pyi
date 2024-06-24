from magneto.base import enums_pb2 as _enums_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import python_message as _python_message
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class InternalEntityProto(_message.Message):
    __slots__ = ("environment", "primary_key", "is_taskable", "searchable_attr_vec")
    Extensions: _python_message._ExtensionDict
    class SearchableAttr(_message.Message):
        __slots__ = ("key", "bytes_val", "int_val")
        KEY_FIELD_NUMBER: _ClassVar[int]
        BYTES_VAL_FIELD_NUMBER: _ClassVar[int]
        INT_VAL_FIELD_NUMBER: _ClassVar[int]
        key: str
        bytes_val: bytes
        int_val: int
        def __init__(self, key: _Optional[str] = ..., bytes_val: _Optional[bytes] = ..., int_val: _Optional[int] = ...) -> None: ...
    ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_KEY_FIELD_NUMBER: _ClassVar[int]
    IS_TASKABLE_FIELD_NUMBER: _ClassVar[int]
    SEARCHABLE_ATTR_VEC_FIELD_NUMBER: _ClassVar[int]
    environment: _enums_pb2.Environment.Type
    primary_key: str
    is_taskable: bool
    searchable_attr_vec: _containers.RepeatedCompositeFieldContainer[InternalEntityProto.SearchableAttr]
    def __init__(self, environment: _Optional[_Union[_enums_pb2.Environment.Type, str]] = ..., primary_key: _Optional[str] = ..., is_taskable: bool = ..., searchable_attr_vec: _Optional[_Iterable[_Union[InternalEntityProto.SearchableAttr, _Mapping]]] = ...) -> None: ...
