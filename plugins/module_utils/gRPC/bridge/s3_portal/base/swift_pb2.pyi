from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SwiftAccountKey(_message.Message):
    __slots__ = ("tenant_id", "account_name")
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_NAME_FIELD_NUMBER: _ClassVar[int]
    tenant_id: str
    account_name: str
    def __init__(self, tenant_id: _Optional[str] = ..., account_name: _Optional[str] = ...) -> None: ...

class SwiftAccountValue(_message.Message):
    __slots__ = ("metadata_map", "creation_time")
    class MetadataMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    METADATA_MAP_FIELD_NUMBER: _ClassVar[int]
    CREATION_TIME_FIELD_NUMBER: _ClassVar[int]
    metadata_map: _containers.ScalarMap[str, str]
    creation_time: int
    def __init__(self, metadata_map: _Optional[_Mapping[str, str]] = ..., creation_time: _Optional[int] = ...) -> None: ...

class SwiftContainerUsage(_message.Message):
    __slots__ = ("name", "count", "usage_bytes")
    NAME_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    USAGE_BYTES_FIELD_NUMBER: _ClassVar[int]
    name: str
    count: float
    usage_bytes: float
    def __init__(self, name: _Optional[str] = ..., count: _Optional[float] = ..., usage_bytes: _Optional[float] = ...) -> None: ...

class SwiftGetAccountResponseBody(_message.Message):
    __slots__ = ("container",)
    CONTAINER_FIELD_NUMBER: _ClassVar[int]
    container: _containers.RepeatedCompositeFieldContainer[SwiftContainerUsage]
    def __init__(self, container: _Optional[_Iterable[_Union[SwiftContainerUsage, _Mapping]]] = ...) -> None: ...

class SwiftListObjectsEntity(_message.Message):
    __slots__ = ("usage_bytes", "last_modified", "hash", "name", "content_type", "subdir")
    USAGE_BYTES_FIELD_NUMBER: _ClassVar[int]
    LAST_MODIFIED_FIELD_NUMBER: _ClassVar[int]
    HASH_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    SUBDIR_FIELD_NUMBER: _ClassVar[int]
    usage_bytes: float
    last_modified: str
    hash: str
    name: str
    content_type: str
    subdir: str
    def __init__(self, usage_bytes: _Optional[float] = ..., last_modified: _Optional[str] = ..., hash: _Optional[str] = ..., name: _Optional[str] = ..., content_type: _Optional[str] = ..., subdir: _Optional[str] = ...) -> None: ...

class SwiftGetContainerResponseBody(_message.Message):
    __slots__ = ("list_result",)
    LIST_RESULT_FIELD_NUMBER: _ClassVar[int]
    list_result: _containers.RepeatedCompositeFieldContainer[SwiftListObjectsEntity]
    def __init__(self, list_result: _Optional[_Iterable[_Union[SwiftListObjectsEntity, _Mapping]]] = ...) -> None: ...
