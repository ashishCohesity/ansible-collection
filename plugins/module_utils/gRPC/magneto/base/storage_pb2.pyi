from magneto.base import entity_pb2 as _entity_pb2
from magneto.base import enums_pb2 as _enums_pb2
from magneto.base import error_pb2 as _error_pb2
from magneto.base import magneto_pb2 as _magneto_pb2
from magneto.base import env_params_pb2 as _env_params_pb2
from magneto.base import nas_pb2 as _nas_pb2
from magneto.base import san_pb2 as _san_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf.internal import python_message as _python_message
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SanProtocol(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kUnknown: _ClassVar[SanProtocol]
    kPreferFc: _ClassVar[SanProtocol]
    kIscsiOnly: _ClassVar[SanProtocol]
kUnknown: SanProtocol
kPreferFc: SanProtocol
kIscsiOnly: SanProtocol

class StorageDeviceProto(_message.Message):
    __slots__ = ("type", "nas", "san_logical_unit", "vss_storage", "stored_entities_id_vec")
    Extensions: _python_message._ExtensionDict
    TYPE_FIELD_NUMBER: _ClassVar[int]
    NAS_FIELD_NUMBER: _ClassVar[int]
    SAN_LOGICAL_UNIT_FIELD_NUMBER: _ClassVar[int]
    VSS_STORAGE_FIELD_NUMBER: _ClassVar[int]
    STORED_ENTITIES_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    type: _enums_pb2.StorageProtocol.Type
    nas: _nas_pb2.NasPathProto
    san_logical_unit: _san_pb2.SanLogicalUnit
    vss_storage: VSSStorage
    stored_entities_id_vec: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, type: _Optional[_Union[_enums_pb2.StorageProtocol.Type, str]] = ..., nas: _Optional[_Union[_nas_pb2.NasPathProto, _Mapping]] = ..., san_logical_unit: _Optional[_Union[_san_pb2.SanLogicalUnit, _Mapping]] = ..., vss_storage: _Optional[_Union[VSSStorage, _Mapping]] = ..., stored_entities_id_vec: _Optional[_Iterable[int]] = ...) -> None: ...

class VSSStorage(_message.Message):
    __slots__ = ("host_entity",)
    HOST_ENTITY_FIELD_NUMBER: _ClassVar[int]
    host_entity: _entity_pb2.EntityProto
    def __init__(self, host_entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ...) -> None: ...

class StorageInfoProto(_message.Message):
    __slots__ = ("parent_source", "primary_device_vec")
    PARENT_SOURCE_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_DEVICE_VEC_FIELD_NUMBER: _ClassVar[int]
    parent_source: _entity_pb2.EntityProto
    primary_device_vec: _containers.RepeatedCompositeFieldContainer[StorageDeviceProto]
    def __init__(self, parent_source: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., primary_device_vec: _Optional[_Iterable[_Union[StorageDeviceProto, _Mapping]]] = ...) -> None: ...

class StorageSnapshotEligibilityStatusProto(_message.Message):
    __slots__ = ("type", "reason")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kEligible: _ClassVar[StorageSnapshotEligibilityStatusProto.Type]
        kUnknownStorageDevice: _ClassVar[StorageSnapshotEligibilityStatusProto.Type]
        kNoStorageDevice: _ClassVar[StorageSnapshotEligibilityStatusProto.Type]
        kSpansMultipleStorageDevices: _ClassVar[StorageSnapshotEligibilityStatusProto.Type]
        kFetchStorageInfoError: _ClassVar[StorageSnapshotEligibilityStatusProto.Type]
        kSpansMultipleParentStorageDevices: _ClassVar[StorageSnapshotEligibilityStatusProto.Type]
        kUseRctBackup: _ClassVar[StorageSnapshotEligibilityStatusProto.Type]
        kInvalidForStorageArraySnapshot: _ClassVar[StorageSnapshotEligibilityStatusProto.Type]
    kEligible: StorageSnapshotEligibilityStatusProto.Type
    kUnknownStorageDevice: StorageSnapshotEligibilityStatusProto.Type
    kNoStorageDevice: StorageSnapshotEligibilityStatusProto.Type
    kSpansMultipleStorageDevices: StorageSnapshotEligibilityStatusProto.Type
    kFetchStorageInfoError: StorageSnapshotEligibilityStatusProto.Type
    kSpansMultipleParentStorageDevices: StorageSnapshotEligibilityStatusProto.Type
    kUseRctBackup: StorageSnapshotEligibilityStatusProto.Type
    kInvalidForStorageArraySnapshot: StorageSnapshotEligibilityStatusProto.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    type: StorageSnapshotEligibilityStatusProto.Type
    reason: str
    def __init__(self, type: _Optional[_Union[StorageSnapshotEligibilityStatusProto.Type, str]] = ..., reason: _Optional[str] = ...) -> None: ...

class EntityStorageMetadataProto(_message.Message):
    __slots__ = ()
    Extensions: _python_message._ExtensionDict
    def __init__(self) -> None: ...

class EntitiesStorageInfoProto(_message.Message):
    __slots__ = ("status", "entity_storage_info_vec")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kStarted: _ClassVar[EntitiesStorageInfoProto.Status]
        kStorageInfoFetched: _ClassVar[EntitiesStorageInfoProto.Status]
        kFinished: _ClassVar[EntitiesStorageInfoProto.Status]
    kStarted: EntitiesStorageInfoProto.Status
    kStorageInfoFetched: EntitiesStorageInfoProto.Status
    kFinished: EntitiesStorageInfoProto.Status
    class EntityStorageInfo(_message.Message):
        __slots__ = ("entity_id", "entity_storage_metadata", "eligibility_status", "storage_info_vec")
        ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
        ENTITY_STORAGE_METADATA_FIELD_NUMBER: _ClassVar[int]
        ELIGIBILITY_STATUS_FIELD_NUMBER: _ClassVar[int]
        STORAGE_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
        entity_id: int
        entity_storage_metadata: EntityStorageMetadataProto
        eligibility_status: StorageSnapshotEligibilityStatusProto
        storage_info_vec: _containers.RepeatedCompositeFieldContainer[StorageInfoProto]
        def __init__(self, entity_id: _Optional[int] = ..., entity_storage_metadata: _Optional[_Union[EntityStorageMetadataProto, _Mapping]] = ..., eligibility_status: _Optional[_Union[StorageSnapshotEligibilityStatusProto, _Mapping]] = ..., storage_info_vec: _Optional[_Iterable[_Union[StorageInfoProto, _Mapping]]] = ...) -> None: ...
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ENTITY_STORAGE_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    status: EntitiesStorageInfoProto.Status
    entity_storage_info_vec: _containers.RepeatedCompositeFieldContainer[EntitiesStorageInfoProto.EntityStorageInfo]
    def __init__(self, status: _Optional[_Union[EntitiesStorageInfoProto.Status, str]] = ..., entity_storage_info_vec: _Optional[_Iterable[_Union[EntitiesStorageInfoProto.EntityStorageInfo, _Mapping]]] = ...) -> None: ...

class StorageDeviceSnapshotInfoProto(_message.Message):
    __slots__ = ("type", "error", "nas_snapshot", "san_snapshot")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    NAS_SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    SAN_SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    type: _enums_pb2.StorageProtocol.Type
    error: _error_pb2.ErrorProto
    nas_snapshot: _nas_pb2.NasPathSnapshotProto
    san_snapshot: _san_pb2.SanLogicalUnitSnapshot
    def __init__(self, type: _Optional[_Union[_enums_pb2.StorageProtocol.Type, str]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., nas_snapshot: _Optional[_Union[_nas_pb2.NasPathSnapshotProto, _Mapping]] = ..., san_snapshot: _Optional[_Union[_san_pb2.SanLogicalUnitSnapshot, _Mapping]] = ...) -> None: ...

class EntitySnapshotInfoProto(_message.Message):
    __slots__ = ("entity_id", "error", "snapshot_type", "snapshot_time_usecs", "group_snapshot_task_id")
    Extensions: _python_message._ExtensionDict
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_TYPE_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    GROUP_SNAPSHOT_TASK_ID_FIELD_NUMBER: _ClassVar[int]
    entity_id: int
    error: _error_pb2.ErrorProto
    snapshot_type: _magneto_pb2.ObjectSnapshotType
    snapshot_time_usecs: int
    group_snapshot_task_id: int
    def __init__(self, entity_id: _Optional[int] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., snapshot_type: _Optional[_Union[_magneto_pb2.ObjectSnapshotType, _Mapping]] = ..., snapshot_time_usecs: _Optional[int] = ..., group_snapshot_task_id: _Optional[int] = ...) -> None: ...

class EntitiesGroupSnapshotInfoProto(_message.Message):
    __slots__ = ("entity_snapshot_info_vec", "storage_device_snapshot_info_set", "last_error")
    Extensions: _python_message._ExtensionDict
    ENTITY_SNAPSHOT_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    STORAGE_DEVICE_SNAPSHOT_INFO_SET_FIELD_NUMBER: _ClassVar[int]
    LAST_ERROR_FIELD_NUMBER: _ClassVar[int]
    entity_snapshot_info_vec: _containers.RepeatedCompositeFieldContainer[EntitySnapshotInfoProto]
    storage_device_snapshot_info_set: _containers.RepeatedCompositeFieldContainer[StorageDeviceSnapshotInfoProto]
    last_error: _error_pb2.ErrorProto
    def __init__(self, entity_snapshot_info_vec: _Optional[_Iterable[_Union[EntitySnapshotInfoProto, _Mapping]]] = ..., storage_device_snapshot_info_set: _Optional[_Iterable[_Union[StorageDeviceSnapshotInfoProto, _Mapping]]] = ..., last_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class TeardownEntitySnapshotInfoProto(_message.Message):
    __slots__ = ("entity_id", "teardown_state_vec")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kStarted: _ClassVar[TeardownEntitySnapshotInfoProto.Status]
        kFinished: _ClassVar[TeardownEntitySnapshotInfoProto.Status]
    kStarted: TeardownEntitySnapshotInfoProto.Status
    kFinished: TeardownEntitySnapshotInfoProto.Status
    class TeardownAttemptState(_message.Message):
        __slots__ = ("status", "error")
        STATUS_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        status: TeardownEntitySnapshotInfoProto.Status
        error: _error_pb2.ErrorProto
        def __init__(self, status: _Optional[_Union[TeardownEntitySnapshotInfoProto.Status, str]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    TEARDOWN_STATE_VEC_FIELD_NUMBER: _ClassVar[int]
    entity_id: int
    teardown_state_vec: _containers.RepeatedCompositeFieldContainer[TeardownEntitySnapshotInfoProto.TeardownAttemptState]
    def __init__(self, entity_id: _Optional[int] = ..., teardown_state_vec: _Optional[_Iterable[_Union[TeardownEntitySnapshotInfoProto.TeardownAttemptState, _Mapping]]] = ...) -> None: ...

class TeardownGroupSnapshotInfoProto(_message.Message):
    __slots__ = ("teardown_entity_snapshot_info_vec", "teardown_primary_error", "delete_storage_snapshot_error", "storage_device_snapshot_info_vec")
    TEARDOWN_ENTITY_SNAPSHOT_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    TEARDOWN_PRIMARY_ERROR_FIELD_NUMBER: _ClassVar[int]
    DELETE_STORAGE_SNAPSHOT_ERROR_FIELD_NUMBER: _ClassVar[int]
    STORAGE_DEVICE_SNAPSHOT_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    teardown_entity_snapshot_info_vec: _containers.RepeatedCompositeFieldContainer[TeardownEntitySnapshotInfoProto]
    teardown_primary_error: _error_pb2.ErrorProto
    delete_storage_snapshot_error: _error_pb2.ErrorProto
    storage_device_snapshot_info_vec: _containers.RepeatedCompositeFieldContainer[StorageDeviceSnapshotInfoProto]
    def __init__(self, teardown_entity_snapshot_info_vec: _Optional[_Iterable[_Union[TeardownEntitySnapshotInfoProto, _Mapping]]] = ..., teardown_primary_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., delete_storage_snapshot_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., storage_device_snapshot_info_vec: _Optional[_Iterable[_Union[StorageDeviceSnapshotInfoProto, _Mapping]]] = ...) -> None: ...
