from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class OrgInfo(_message.Message):
    __slots__ = ("org_id", "org_name", "organization_type", "concurrency")
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    ORG_NAME_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    CONCURRENCY_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    org_name: str
    organization_type: str
    concurrency: int
    def __init__(self, org_id: _Optional[str] = ..., org_name: _Optional[str] = ..., organization_type: _Optional[str] = ..., concurrency: _Optional[int] = ...) -> None: ...

class ObjectInfo(_message.Message):
    __slots__ = ("record_count", "object_type", "key_prefix", "field_info")
    class ObjectType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kStandard: _ClassVar[ObjectInfo.ObjectType]
        kCustom: _ClassVar[ObjectInfo.ObjectType]
    kStandard: ObjectInfo.ObjectType
    kCustom: ObjectInfo.ObjectType
    RECORD_COUNT_FIELD_NUMBER: _ClassVar[int]
    OBJECT_TYPE_FIELD_NUMBER: _ClassVar[int]
    KEY_PREFIX_FIELD_NUMBER: _ClassVar[int]
    FIELD_INFO_FIELD_NUMBER: _ClassVar[int]
    record_count: int
    object_type: ObjectInfo.ObjectType
    key_prefix: str
    field_info: _containers.RepeatedCompositeFieldContainer[FieldInfo]
    def __init__(self, record_count: _Optional[int] = ..., object_type: _Optional[_Union[ObjectInfo.ObjectType, str]] = ..., key_prefix: _Optional[str] = ..., field_info: _Optional[_Iterable[_Union[FieldInfo, _Mapping]]] = ...) -> None: ...

class FieldInfo(_message.Message):
    __slots__ = ("data_type", "field_type", "length", "precision", "scale", "name")
    class FieldType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kInvalid: _ClassVar[FieldInfo.FieldType]
        kStandard: _ClassVar[FieldInfo.FieldType]
        kCustom: _ClassVar[FieldInfo.FieldType]
    kInvalid: FieldInfo.FieldType
    kStandard: FieldInfo.FieldType
    kCustom: FieldInfo.FieldType
    DATA_TYPE_FIELD_NUMBER: _ClassVar[int]
    FIELD_TYPE_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    PRECISION_FIELD_NUMBER: _ClassVar[int]
    SCALE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    data_type: str
    field_type: FieldInfo.FieldType
    length: int
    precision: int
    scale: int
    name: str
    def __init__(self, data_type: _Optional[str] = ..., field_type: _Optional[_Union[FieldInfo.FieldType, str]] = ..., length: _Optional[int] = ..., precision: _Optional[int] = ..., scale: _Optional[int] = ..., name: _Optional[str] = ...) -> None: ...

class Entity(_message.Message):
    __slots__ = ("type", "name", "org_info", "object_info", "field_info", "user_license_info")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kOrg: _ClassVar[Entity.Type]
        kObject: _ClassVar[Entity.Type]
        kAppInstance: _ClassVar[Entity.Type]
        kField: _ClassVar[Entity.Type]
    kOrg: Entity.Type
    kObject: Entity.Type
    kAppInstance: Entity.Type
    kField: Entity.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ORG_INFO_FIELD_NUMBER: _ClassVar[int]
    OBJECT_INFO_FIELD_NUMBER: _ClassVar[int]
    FIELD_INFO_FIELD_NUMBER: _ClassVar[int]
    USER_LICENSE_INFO_FIELD_NUMBER: _ClassVar[int]
    type: Entity.Type
    name: str
    org_info: OrgInfo
    object_info: ObjectInfo
    field_info: FieldInfo
    user_license_info: UserLicenseInfo
    def __init__(self, type: _Optional[_Union[Entity.Type, str]] = ..., name: _Optional[str] = ..., org_info: _Optional[_Union[OrgInfo, _Mapping]] = ..., object_info: _Optional[_Union[ObjectInfo, _Mapping]] = ..., field_info: _Optional[_Union[FieldInfo, _Mapping]] = ..., user_license_info: _Optional[_Union[UserLicenseInfo, _Mapping]] = ...) -> None: ...

class UserLicenseInfo(_message.Message):
    __slots__ = ("total_sf_licenses", "num_used_sf_licenses", "last_updated_time")
    TOTAL_SF_LICENSES_FIELD_NUMBER: _ClassVar[int]
    NUM_USED_SF_LICENSES_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATED_TIME_FIELD_NUMBER: _ClassVar[int]
    total_sf_licenses: int
    num_used_sf_licenses: int
    last_updated_time: str
    def __init__(self, total_sf_licenses: _Optional[int] = ..., num_used_sf_licenses: _Optional[int] = ..., last_updated_time: _Optional[str] = ...) -> None: ...
