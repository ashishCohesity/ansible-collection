from magneto.base import error_pb2 as _error_pb2
from google.protobuf.internal import python_message as _python_message
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PreSnapshotResultProto(_message.Message):
    __slots__ = ("status",)
    Extensions: _python_message._ExtensionDict
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: _error_pb2.ErrorProto
    def __init__(self, status: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class SnapshotResultProto(_message.Message):
    __slots__ = ("status",)
    Extensions: _python_message._ExtensionDict
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: _error_pb2.ErrorProto
    def __init__(self, status: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class PostSnapshotResultProto(_message.Message):
    __slots__ = ("status",)
    Extensions: _python_message._ExtensionDict
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: _error_pb2.ErrorProto
    def __init__(self, status: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class SnapshotContextProto(_message.Message):
    __slots__ = ()
    Extensions: _python_message._ExtensionDict
    def __init__(self) -> None: ...

class DatabaseMetadataProto(_message.Message):
    __slots__ = ("status",)
    Extensions: _python_message._ExtensionDict
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: _error_pb2.ErrorProto
    def __init__(self, status: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...
