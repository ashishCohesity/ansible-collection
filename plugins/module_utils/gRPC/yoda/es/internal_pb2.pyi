from yoda.es import jsonname_pb2 as _jsonname_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AddMeta(_message.Message):
    __slots__ = ("_type", "_id")
    _TYPE_FIELD_NUMBER: _ClassVar[int]
    _ID_FIELD_NUMBER: _ClassVar[int]
    _type: str
    _id: str
    def __init__(self, _type: _Optional[str] = ..., _id: _Optional[str] = ...) -> None: ...

class DeleteMeta(_message.Message):
    __slots__ = ("_type", "_id")
    _TYPE_FIELD_NUMBER: _ClassVar[int]
    _ID_FIELD_NUMBER: _ClassVar[int]
    _type: str
    _id: str
    def __init__(self, _type: _Optional[str] = ..., _id: _Optional[str] = ...) -> None: ...

class BulkOp(_message.Message):
    __slots__ = ("index", "create", "delete")
    INDEX_FIELD_NUMBER: _ClassVar[int]
    CREATE_FIELD_NUMBER: _ClassVar[int]
    DELETE_FIELD_NUMBER: _ClassVar[int]
    index: AddMeta
    create: AddMeta
    delete: DeleteMeta
    def __init__(self, index: _Optional[_Union[AddMeta, _Mapping]] = ..., create: _Optional[_Union[AddMeta, _Mapping]] = ..., delete: _Optional[_Union[DeleteMeta, _Mapping]] = ...) -> None: ...
