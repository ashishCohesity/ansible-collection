from google.protobuf import descriptor_pb2 as _descriptor_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Version(_message.Message):
    __slots__ = ("major", "minor", "patch", "suffix")
    MAJOR_FIELD_NUMBER: _ClassVar[int]
    MINOR_FIELD_NUMBER: _ClassVar[int]
    PATCH_FIELD_NUMBER: _ClassVar[int]
    SUFFIX_FIELD_NUMBER: _ClassVar[int]
    major: int
    minor: int
    patch: int
    suffix: str
    def __init__(self, major: _Optional[int] = ..., minor: _Optional[int] = ..., patch: _Optional[int] = ..., suffix: _Optional[str] = ...) -> None: ...

class CodeGeneratorRequest(_message.Message):
    __slots__ = ("file_to_generate", "parameter", "proto_file", "compiler_version")
    FILE_TO_GENERATE_FIELD_NUMBER: _ClassVar[int]
    PARAMETER_FIELD_NUMBER: _ClassVar[int]
    PROTO_FILE_FIELD_NUMBER: _ClassVar[int]
    COMPILER_VERSION_FIELD_NUMBER: _ClassVar[int]
    file_to_generate: _containers.RepeatedScalarFieldContainer[str]
    parameter: str
    proto_file: _containers.RepeatedCompositeFieldContainer[_descriptor_pb2.FileDescriptorProto]
    compiler_version: Version
    def __init__(self, file_to_generate: _Optional[_Iterable[str]] = ..., parameter: _Optional[str] = ..., proto_file: _Optional[_Iterable[_Union[_descriptor_pb2.FileDescriptorProto, _Mapping]]] = ..., compiler_version: _Optional[_Union[Version, _Mapping]] = ...) -> None: ...

class CodeGeneratorResponse(_message.Message):
    __slots__ = ("error", "file")
    class File(_message.Message):
        __slots__ = ("name", "insertion_point", "content")
        NAME_FIELD_NUMBER: _ClassVar[int]
        INSERTION_POINT_FIELD_NUMBER: _ClassVar[int]
        CONTENT_FIELD_NUMBER: _ClassVar[int]
        name: str
        insertion_point: str
        content: str
        def __init__(self, name: _Optional[str] = ..., insertion_point: _Optional[str] = ..., content: _Optional[str] = ...) -> None: ...
    ERROR_FIELD_NUMBER: _ClassVar[int]
    FILE_FIELD_NUMBER: _ClassVar[int]
    error: str
    file: _containers.RepeatedCompositeFieldContainer[CodeGeneratorResponse.File]
    def __init__(self, error: _Optional[str] = ..., file: _Optional[_Iterable[_Union[CodeGeneratorResponse.File, _Mapping]]] = ...) -> None: ...
