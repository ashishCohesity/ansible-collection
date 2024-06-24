from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ErrorInfo(_message.Message):
    __slots__ = ("message", "messageId")
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    MESSAGEID_FIELD_NUMBER: _ClassVar[int]
    message: str
    messageId: int
    def __init__(self, message: _Optional[str] = ..., messageId: _Optional[int] = ...) -> None: ...

class EmptyRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetUserContextResponse(_message.Message):
    __slots__ = ("username",)
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    username: str
    def __init__(self, username: _Optional[str] = ...) -> None: ...

class GetServerInfoResponse(_message.Message):
    __slots__ = ("instanceUuid", "apiVersion", "productVersion", "name")
    INSTANCEUUID_FIELD_NUMBER: _ClassVar[int]
    APIVERSION_FIELD_NUMBER: _ClassVar[int]
    PRODUCTVERSION_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    instanceUuid: str
    apiVersion: str
    productVersion: str
    name: str
    def __init__(self, instanceUuid: _Optional[str] = ..., apiVersion: _Optional[str] = ..., productVersion: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class CreateSnapshotRequest(_message.Message):
    __slots__ = ("snapshotName", "description", "memory", "quiesce")
    SNAPSHOTNAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    MEMORY_FIELD_NUMBER: _ClassVar[int]
    QUIESCE_FIELD_NUMBER: _ClassVar[int]
    snapshotName: str
    description: str
    memory: bool
    quiesce: bool
    def __init__(self, snapshotName: _Optional[str] = ..., description: _Optional[str] = ..., memory: bool = ..., quiesce: bool = ...) -> None: ...

class CreateSnapshotResponse(_message.Message):
    __slots__ = ("snapshotId",)
    SNAPSHOTID_FIELD_NUMBER: _ClassVar[int]
    snapshotId: str
    def __init__(self, snapshotId: _Optional[str] = ...) -> None: ...

class DeleteSnapshotRequest(_message.Message):
    __slots__ = ("removeChildren", "consolidate", "updateSentinel")
    REMOVECHILDREN_FIELD_NUMBER: _ClassVar[int]
    CONSOLIDATE_FIELD_NUMBER: _ClassVar[int]
    UPDATESENTINEL_FIELD_NUMBER: _ClassVar[int]
    removeChildren: bool
    consolidate: bool
    updateSentinel: bool
    def __init__(self, removeChildren: bool = ..., consolidate: bool = ..., updateSentinel: bool = ...) -> None: ...

class DeleteSnapshotResponse(_message.Message):
    __slots__ = ("snapshotIds",)
    SNAPSHOTIDS_FIELD_NUMBER: _ClassVar[int]
    snapshotIds: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, snapshotIds: _Optional[_Iterable[str]] = ...) -> None: ...

class GetDatastoresResponse(_message.Message):
    __slots__ = ("datastore_vec",)
    class VirtDatastore(_message.Message):
        __slots__ = ("mor",)
        MOR_FIELD_NUMBER: _ClassVar[int]
        mor: str
        def __init__(self, mor: _Optional[str] = ...) -> None: ...
    class Datastore(_message.Message):
        __slots__ = ("virtDatastore",)
        VIRTDATASTORE_FIELD_NUMBER: _ClassVar[int]
        virtDatastore: GetDatastoresResponse.VirtDatastore
        def __init__(self, virtDatastore: _Optional[_Union[GetDatastoresResponse.VirtDatastore, _Mapping]] = ...) -> None: ...
    DATASTORE_VEC_FIELD_NUMBER: _ClassVar[int]
    datastore_vec: _containers.RepeatedCompositeFieldContainer[GetDatastoresResponse.Datastore]
    def __init__(self, datastore_vec: _Optional[_Iterable[_Union[GetDatastoresResponse.Datastore, _Mapping]]] = ...) -> None: ...
