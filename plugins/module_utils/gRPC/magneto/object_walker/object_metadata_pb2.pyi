from util.storage import error_pb2 as _error_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ObjectMetadata(_message.Message):
    __slots__ = ("prefix", "key", "error", "version_id", "last_modified_msecs", "ctag", "owner", "size_bytes", "serialized_metadata", "permissions", "storage_class")
    class ACLInfo(_message.Message):
        __slots__ = ("permission", "grantee", "grantee_type")
        PERMISSION_FIELD_NUMBER: _ClassVar[int]
        GRANTEE_FIELD_NUMBER: _ClassVar[int]
        GRANTEE_TYPE_FIELD_NUMBER: _ClassVar[int]
        permission: str
        grantee: str
        grantee_type: str
        def __init__(self, permission: _Optional[str] = ..., grantee: _Optional[str] = ..., grantee_type: _Optional[str] = ...) -> None: ...
    PREFIX_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    VERSION_ID_FIELD_NUMBER: _ClassVar[int]
    LAST_MODIFIED_MSECS_FIELD_NUMBER: _ClassVar[int]
    CTAG_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    SERIALIZED_METADATA_FIELD_NUMBER: _ClassVar[int]
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    STORAGE_CLASS_FIELD_NUMBER: _ClassVar[int]
    prefix: str
    key: str
    error: _error_pb2.ErrorProto
    version_id: str
    last_modified_msecs: int
    ctag: str
    owner: str
    size_bytes: int
    serialized_metadata: bytes
    permissions: _containers.RepeatedCompositeFieldContainer[ObjectMetadata.ACLInfo]
    storage_class: str
    def __init__(self, prefix: _Optional[str] = ..., key: _Optional[str] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., version_id: _Optional[str] = ..., last_modified_msecs: _Optional[int] = ..., ctag: _Optional[str] = ..., owner: _Optional[str] = ..., size_bytes: _Optional[int] = ..., serialized_metadata: _Optional[bytes] = ..., permissions: _Optional[_Iterable[_Union[ObjectMetadata.ACLInfo, _Mapping]]] = ..., storage_class: _Optional[str] = ...) -> None: ...
