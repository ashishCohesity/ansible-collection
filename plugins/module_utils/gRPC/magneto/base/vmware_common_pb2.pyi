from magneto.base import entity_pb2 as _entity_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RestoreVMwareVMParams(_message.Message):
    __slots__ = ("target_vm_folder", "target_datastore_folder", "copy_recovery", "preserve_tags_during_clone", "resource_pool_entity", "datastore_entity_vec", "preserve_custom_attributes_during_clone", "storage_profile_name", "storage_profile_vcd_uuid", "org_vdc_network_name", "org_vdc_network_vcd_uuid", "catalog_uuid", "overwrite_existing_vm", "power_off_and_rename_existing_vm", "attempt_differential_restore", "is_on_prem_deploy", "allow_nbdssl_transport_fallback", "disk_provision_type")
    class DiskProvisionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kBackedUpDiskType: _ClassVar[RestoreVMwareVMParams.DiskProvisionType]
        kThickProvisionLazyZeroed: _ClassVar[RestoreVMwareVMParams.DiskProvisionType]
        kThickProvisionEagerlyZeroed: _ClassVar[RestoreVMwareVMParams.DiskProvisionType]
        kThinProvision: _ClassVar[RestoreVMwareVMParams.DiskProvisionType]
    kBackedUpDiskType: RestoreVMwareVMParams.DiskProvisionType
    kThickProvisionLazyZeroed: RestoreVMwareVMParams.DiskProvisionType
    kThickProvisionEagerlyZeroed: RestoreVMwareVMParams.DiskProvisionType
    kThinProvision: RestoreVMwareVMParams.DiskProvisionType
    TARGET_VM_FOLDER_FIELD_NUMBER: _ClassVar[int]
    TARGET_DATASTORE_FOLDER_FIELD_NUMBER: _ClassVar[int]
    COPY_RECOVERY_FIELD_NUMBER: _ClassVar[int]
    PRESERVE_TAGS_DURING_CLONE_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_POOL_ENTITY_FIELD_NUMBER: _ClassVar[int]
    DATASTORE_ENTITY_VEC_FIELD_NUMBER: _ClassVar[int]
    PRESERVE_CUSTOM_ATTRIBUTES_DURING_CLONE_FIELD_NUMBER: _ClassVar[int]
    STORAGE_PROFILE_NAME_FIELD_NUMBER: _ClassVar[int]
    STORAGE_PROFILE_VCD_UUID_FIELD_NUMBER: _ClassVar[int]
    ORG_VDC_NETWORK_NAME_FIELD_NUMBER: _ClassVar[int]
    ORG_VDC_NETWORK_VCD_UUID_FIELD_NUMBER: _ClassVar[int]
    CATALOG_UUID_FIELD_NUMBER: _ClassVar[int]
    OVERWRITE_EXISTING_VM_FIELD_NUMBER: _ClassVar[int]
    POWER_OFF_AND_RENAME_EXISTING_VM_FIELD_NUMBER: _ClassVar[int]
    ATTEMPT_DIFFERENTIAL_RESTORE_FIELD_NUMBER: _ClassVar[int]
    IS_ON_PREM_DEPLOY_FIELD_NUMBER: _ClassVar[int]
    ALLOW_NBDSSL_TRANSPORT_FALLBACK_FIELD_NUMBER: _ClassVar[int]
    DISK_PROVISION_TYPE_FIELD_NUMBER: _ClassVar[int]
    target_vm_folder: _entity_pb2.EntityProto
    target_datastore_folder: _entity_pb2.EntityProto
    copy_recovery: bool
    preserve_tags_during_clone: bool
    resource_pool_entity: _entity_pb2.EntityProto
    datastore_entity_vec: _containers.RepeatedCompositeFieldContainer[_entity_pb2.EntityProto]
    preserve_custom_attributes_during_clone: bool
    storage_profile_name: str
    storage_profile_vcd_uuid: str
    org_vdc_network_name: str
    org_vdc_network_vcd_uuid: str
    catalog_uuid: str
    overwrite_existing_vm: bool
    power_off_and_rename_existing_vm: bool
    attempt_differential_restore: bool
    is_on_prem_deploy: bool
    allow_nbdssl_transport_fallback: bool
    disk_provision_type: RestoreVMwareVMParams.DiskProvisionType
    def __init__(self, target_vm_folder: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., target_datastore_folder: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., copy_recovery: bool = ..., preserve_tags_during_clone: bool = ..., resource_pool_entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., datastore_entity_vec: _Optional[_Iterable[_Union[_entity_pb2.EntityProto, _Mapping]]] = ..., preserve_custom_attributes_during_clone: bool = ..., storage_profile_name: _Optional[str] = ..., storage_profile_vcd_uuid: _Optional[str] = ..., org_vdc_network_name: _Optional[str] = ..., org_vdc_network_vcd_uuid: _Optional[str] = ..., catalog_uuid: _Optional[str] = ..., overwrite_existing_vm: bool = ..., power_off_and_rename_existing_vm: bool = ..., attempt_differential_restore: bool = ..., is_on_prem_deploy: bool = ..., allow_nbdssl_transport_fallback: bool = ..., disk_provision_type: _Optional[_Union[RestoreVMwareVMParams.DiskProvisionType, str]] = ...) -> None: ...
