from metadata_service.api import api_pb2 as _api_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EntityAccessProcArgProto(_message.Message):
    __slots__ = ("registered_source_primary_key", "permission_arg_vec")
    class PermissionArg(_message.Message):
        __slots__ = ("tenant_id", "serialized_SID")
        TENANT_ID_FIELD_NUMBER: _ClassVar[int]
        SERIALIZED_SID_FIELD_NUMBER: _ClassVar[int]
        tenant_id: str
        serialized_SID: str
        def __init__(self, tenant_id: _Optional[str] = ..., serialized_SID: _Optional[str] = ...) -> None: ...
    ENTITY_ACCESS_PROC_ARG_FIELD_NUMBER: _ClassVar[int]
    entity_access_proc_arg: _descriptor.FieldDescriptor
    REGISTERED_SOURCE_PRIMARY_KEY_FIELD_NUMBER: _ClassVar[int]
    PERMISSION_ARG_VEC_FIELD_NUMBER: _ClassVar[int]
    registered_source_primary_key: str
    permission_arg_vec: _containers.RepeatedCompositeFieldContainer[EntityAccessProcArgProto.PermissionArg]
    def __init__(self, registered_source_primary_key: _Optional[str] = ..., permission_arg_vec: _Optional[_Iterable[_Union[EntityAccessProcArgProto.PermissionArg, _Mapping]]] = ...) -> None: ...
