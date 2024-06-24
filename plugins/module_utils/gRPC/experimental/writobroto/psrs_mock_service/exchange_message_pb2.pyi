from open_util.net import protorpc_pb2 as _protorpc_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RangeProto(_message.Message):
    __slots__ = ("begin", "end")
    BEGIN_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    begin: int
    end: int
    def __init__(self, begin: _Optional[int] = ..., end: _Optional[int] = ...) -> None: ...

class RegisterDomainResponseProto(_message.Message):
    __slots__ = ("mailbox_range",)
    MAILBOX_RANGE_FIELD_NUMBER: _ClassVar[int]
    mailbox_range: _containers.RepeatedCompositeFieldContainer[RangeProto]
    def __init__(self, mailbox_range: _Optional[_Iterable[_Union[RangeProto, _Mapping]]] = ...) -> None: ...

class GetFolderHierarchyResponseProto(_message.Message):
    __slots__ = ("created", "deleted", "updated")
    CREATED_FIELD_NUMBER: _ClassVar[int]
    DELETED_FIELD_NUMBER: _ClassVar[int]
    UPDATED_FIELD_NUMBER: _ClassVar[int]
    created: _containers.RepeatedCompositeFieldContainer[RangeProto]
    deleted: _containers.RepeatedCompositeFieldContainer[RangeProto]
    updated: _containers.RepeatedCompositeFieldContainer[RangeProto]
    def __init__(self, created: _Optional[_Iterable[_Union[RangeProto, _Mapping]]] = ..., deleted: _Optional[_Iterable[_Union[RangeProto, _Mapping]]] = ..., updated: _Optional[_Iterable[_Union[RangeProto, _Mapping]]] = ...) -> None: ...

class GetFolderChangesResponseProto(_message.Message):
    __slots__ = ("created", "deleted", "updated")
    CREATED_FIELD_NUMBER: _ClassVar[int]
    DELETED_FIELD_NUMBER: _ClassVar[int]
    UPDATED_FIELD_NUMBER: _ClassVar[int]
    created: _containers.RepeatedCompositeFieldContainer[RangeProto]
    deleted: _containers.RepeatedCompositeFieldContainer[RangeProto]
    updated: _containers.RepeatedCompositeFieldContainer[RangeProto]
    def __init__(self, created: _Optional[_Iterable[_Union[RangeProto, _Mapping]]] = ..., deleted: _Optional[_Iterable[_Union[RangeProto, _Mapping]]] = ..., updated: _Optional[_Iterable[_Union[RangeProto, _Mapping]]] = ...) -> None: ...
