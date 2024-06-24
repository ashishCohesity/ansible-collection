from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SchemaMetricsProto(_message.Message):
    __slots__ = ("schema_name", "metric_name_vec")
    SCHEMA_NAME_FIELD_NUMBER: _ClassVar[int]
    METRIC_NAME_VEC_FIELD_NUMBER: _ClassVar[int]
    schema_name: str
    metric_name_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, schema_name: _Optional[str] = ..., metric_name_vec: _Optional[_Iterable[str]] = ...) -> None: ...

class SchemasProto(_message.Message):
    __slots__ = ("schema_vec",)
    SCHEMA_VEC_FIELD_NUMBER: _ClassVar[int]
    schema_vec: _containers.RepeatedCompositeFieldContainer[SchemaMetricsProto]
    def __init__(self, schema_vec: _Optional[_Iterable[_Union[SchemaMetricsProto, _Mapping]]] = ...) -> None: ...
