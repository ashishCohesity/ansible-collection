from magneto.base import san_pb2 as _san_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf.internal import python_message as _python_message
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Entity(_message.Message):
    __slots__ = ("type", "name", "id_version", "array_id", "array_revision", "array_version", "array_port_vec", "volume_creation_time", "volume_serial", "volume_size", "volume_total_space_used", "volume_source", "base_volume_id", "volume_iqn", "volume_group_id", "volume_group_uid", "storage_pool_id", "storage_pool_status", "availability_group_id")
    Extensions: _python_message._ExtensionDict
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kStorageArray: _ClassVar[Entity.Type]
        kVolume: _ClassVar[Entity.Type]
        kPureVolumeGroup: _ClassVar[Entity.Type]
        kPureProtectionGroup: _ClassVar[Entity.Type]
        kVolumeGroup: _ClassVar[Entity.Type]
        kStoragePool: _ClassVar[Entity.Type]
        kAvailabilityGroup: _ClassVar[Entity.Type]
        kDummyResource: _ClassVar[Entity.Type]
    kStorageArray: Entity.Type
    kVolume: Entity.Type
    kPureVolumeGroup: Entity.Type
    kPureProtectionGroup: Entity.Type
    kVolumeGroup: Entity.Type
    kStoragePool: Entity.Type
    kAvailabilityGroup: Entity.Type
    kDummyResource: Entity.Type
    class IdentifierVersion(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNone: _ClassVar[Entity.IdentifierVersion]
        kNumericIdentifier: _ClassVar[Entity.IdentifierVersion]
        kUniqueIdentifier: _ClassVar[Entity.IdentifierVersion]
    kNone: Entity.IdentifierVersion
    kNumericIdentifier: Entity.IdentifierVersion
    kUniqueIdentifier: Entity.IdentifierVersion
    class StoragePoolStatus(_message.Message):
        __slots__ = ()
        class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kUnknown: _ClassVar[Entity.StoragePoolStatus.Type]
            kOnline: _ClassVar[Entity.StoragePoolStatus.Type]
            kOffline: _ClassVar[Entity.StoragePoolStatus.Type]
        kUnknown: Entity.StoragePoolStatus.Type
        kOnline: Entity.StoragePoolStatus.Type
        kOffline: Entity.StoragePoolStatus.Type
        def __init__(self) -> None: ...
    TYPE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ID_VERSION_FIELD_NUMBER: _ClassVar[int]
    ARRAY_ID_FIELD_NUMBER: _ClassVar[int]
    ARRAY_REVISION_FIELD_NUMBER: _ClassVar[int]
    ARRAY_VERSION_FIELD_NUMBER: _ClassVar[int]
    ARRAY_PORT_VEC_FIELD_NUMBER: _ClassVar[int]
    VOLUME_CREATION_TIME_FIELD_NUMBER: _ClassVar[int]
    VOLUME_SERIAL_FIELD_NUMBER: _ClassVar[int]
    VOLUME_SIZE_FIELD_NUMBER: _ClassVar[int]
    VOLUME_TOTAL_SPACE_USED_FIELD_NUMBER: _ClassVar[int]
    VOLUME_SOURCE_FIELD_NUMBER: _ClassVar[int]
    BASE_VOLUME_ID_FIELD_NUMBER: _ClassVar[int]
    VOLUME_IQN_FIELD_NUMBER: _ClassVar[int]
    VOLUME_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    VOLUME_GROUP_UID_FIELD_NUMBER: _ClassVar[int]
    STORAGE_POOL_ID_FIELD_NUMBER: _ClassVar[int]
    STORAGE_POOL_STATUS_FIELD_NUMBER: _ClassVar[int]
    AVAILABILITY_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    type: Entity.Type
    name: str
    id_version: Entity.IdentifierVersion
    array_id: str
    array_revision: str
    array_version: str
    array_port_vec: _containers.RepeatedCompositeFieldContainer[_san_pb2.SanPort]
    volume_creation_time: str
    volume_serial: str
    volume_size: int
    volume_total_space_used: int
    volume_source: str
    base_volume_id: str
    volume_iqn: str
    volume_group_id: str
    volume_group_uid: str
    storage_pool_id: str
    storage_pool_status: Entity.StoragePoolStatus.Type
    availability_group_id: str
    def __init__(self, type: _Optional[_Union[Entity.Type, str]] = ..., name: _Optional[str] = ..., id_version: _Optional[_Union[Entity.IdentifierVersion, str]] = ..., array_id: _Optional[str] = ..., array_revision: _Optional[str] = ..., array_version: _Optional[str] = ..., array_port_vec: _Optional[_Iterable[_Union[_san_pb2.SanPort, _Mapping]]] = ..., volume_creation_time: _Optional[str] = ..., volume_serial: _Optional[str] = ..., volume_size: _Optional[int] = ..., volume_total_space_used: _Optional[int] = ..., volume_source: _Optional[str] = ..., base_volume_id: _Optional[str] = ..., volume_iqn: _Optional[str] = ..., volume_group_id: _Optional[str] = ..., volume_group_uid: _Optional[str] = ..., storage_pool_id: _Optional[str] = ..., storage_pool_status: _Optional[_Union[Entity.StoragePoolStatus.Type, str]] = ..., availability_group_id: _Optional[str] = ...) -> None: ...
