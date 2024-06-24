from magneto.agents.base import agent_pb2 as _agent_pb2
from magneto.base.entities import vmware_common_pb2 as _vmware_common_pb2
from magneto.base import error_pb2 as _error_pb2
from magneto.base import magneto_pb2 as _magneto_pb2
from magneto.base import env_params_pb2 as _env_params_pb2
from magneto.base import storage_pb2 as _storage_pb2
from yoda.base import volume_info_pb2 as _volume_info_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SetupRestoreDiskTaskInfo(_message.Message):
    __slots__ = ("setup_state", "setup_error", "teardown_state", "teardown_error", "relative_restore_path_vec", "encoded_disk_path_vec", "datastore_info", "attached_disk_map", "existing_volume_info_vec", "attached_volume_info_vec", "volume_file_info_vec", "mount_volume_info_vec", "snapshot_files_cloned", "disk_to_controller_key_map", "new_to_old_disk_uuid_map", "disk_uuid_to_provisioning_info_map", "disk_unique_id_vec", "cloned_storage_snapshot_info_vec", "curr_snapshot_idx", "restore_path_to_disk_uuid_map")
    class SetupState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kCloneVMFiles: _ClassVar[SetupRestoreDiskTaskInfo.SetupState]
        kMountDatastore: _ClassVar[SetupRestoreDiskTaskInfo.SetupState]
        kAttachVMDKs: _ClassVar[SetupRestoreDiskTaskInfo.SetupState]
        kBringDisksOnline: _ClassVar[SetupRestoreDiskTaskInfo.SetupState]
        kSetupFinished: _ClassVar[SetupRestoreDiskTaskInfo.SetupState]
        kSetupCancelled: _ClassVar[SetupRestoreDiskTaskInfo.SetupState]
    kCloneVMFiles: SetupRestoreDiskTaskInfo.SetupState
    kMountDatastore: SetupRestoreDiskTaskInfo.SetupState
    kAttachVMDKs: SetupRestoreDiskTaskInfo.SetupState
    kBringDisksOnline: SetupRestoreDiskTaskInfo.SetupState
    kSetupFinished: SetupRestoreDiskTaskInfo.SetupState
    kSetupCancelled: SetupRestoreDiskTaskInfo.SetupState
    class TeardownState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kDetachDisks: _ClassVar[SetupRestoreDiskTaskInfo.TeardownState]
        kUnmountDatastore: _ClassVar[SetupRestoreDiskTaskInfo.TeardownState]
        kDeleteView: _ClassVar[SetupRestoreDiskTaskInfo.TeardownState]
        kTeardownFinished: _ClassVar[SetupRestoreDiskTaskInfo.TeardownState]
    kDetachDisks: SetupRestoreDiskTaskInfo.TeardownState
    kUnmountDatastore: SetupRestoreDiskTaskInfo.TeardownState
    kDeleteView: SetupRestoreDiskTaskInfo.TeardownState
    kTeardownFinished: SetupRestoreDiskTaskInfo.TeardownState
    class DatastoreInfo(_message.Message):
        __slots__ = ("moref", "host_moref", "datastore_system_moref", "name", "remote_host", "remote_path", "datacenter_moref", "datacenter_name")
        MOREF_FIELD_NUMBER: _ClassVar[int]
        HOST_MOREF_FIELD_NUMBER: _ClassVar[int]
        DATASTORE_SYSTEM_MOREF_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        REMOTE_HOST_FIELD_NUMBER: _ClassVar[int]
        REMOTE_PATH_FIELD_NUMBER: _ClassVar[int]
        DATACENTER_MOREF_FIELD_NUMBER: _ClassVar[int]
        DATACENTER_NAME_FIELD_NUMBER: _ClassVar[int]
        moref: _vmware_common_pb2.MORef
        host_moref: _vmware_common_pb2.MORef
        datastore_system_moref: _vmware_common_pb2.MORef
        name: str
        remote_host: str
        remote_path: str
        datacenter_moref: _vmware_common_pb2.MORef
        datacenter_name: str
        def __init__(self, moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ..., host_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ..., datastore_system_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ..., name: _Optional[str] = ..., remote_host: _Optional[str] = ..., remote_path: _Optional[str] = ..., datacenter_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ..., datacenter_name: _Optional[str] = ...) -> None: ...
    class AttachedDiskInfo(_message.Message):
        __slots__ = ("key", "unit_number", "controller_key", "disk_id")
        KEY_FIELD_NUMBER: _ClassVar[int]
        UNIT_NUMBER_FIELD_NUMBER: _ClassVar[int]
        CONTROLLER_KEY_FIELD_NUMBER: _ClassVar[int]
        DISK_ID_FIELD_NUMBER: _ClassVar[int]
        key: int
        unit_number: int
        controller_key: int
        disk_id: str
        def __init__(self, key: _Optional[int] = ..., unit_number: _Optional[int] = ..., controller_key: _Optional[int] = ..., disk_id: _Optional[str] = ...) -> None: ...
    class AttachedDiskMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: SetupRestoreDiskTaskInfo.AttachedDiskInfo
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[SetupRestoreDiskTaskInfo.AttachedDiskInfo, _Mapping]] = ...) -> None: ...
    class DiskToControllerKeyMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    class NewToOldDiskUuidMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class DiskProvisioningInfo(_message.Message):
        __slots__ = ("disk_type", "is_thin_provisioned", "thick_eager_scrub_provision")
        DISK_TYPE_FIELD_NUMBER: _ClassVar[int]
        IS_THIN_PROVISIONED_FIELD_NUMBER: _ClassVar[int]
        THICK_EAGER_SCRUB_PROVISION_FIELD_NUMBER: _ClassVar[int]
        disk_type: int
        is_thin_provisioned: bool
        thick_eager_scrub_provision: bool
        def __init__(self, disk_type: _Optional[int] = ..., is_thin_provisioned: bool = ..., thick_eager_scrub_provision: bool = ...) -> None: ...
    class DiskUuidToProvisioningInfoMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: SetupRestoreDiskTaskInfo.DiskProvisioningInfo
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[SetupRestoreDiskTaskInfo.DiskProvisioningInfo, _Mapping]] = ...) -> None: ...
    class ClonedStorageSnapshotInfo(_message.Message):
        __slots__ = ("storage_device_snapshot_info", "mounted_datastore", "record_volume_for_gc", "snapshot_time_usecs", "src_datastore_name")
        STORAGE_DEVICE_SNAPSHOT_INFO_FIELD_NUMBER: _ClassVar[int]
        MOUNTED_DATASTORE_FIELD_NUMBER: _ClassVar[int]
        RECORD_VOLUME_FOR_GC_FIELD_NUMBER: _ClassVar[int]
        SNAPSHOT_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
        SRC_DATASTORE_NAME_FIELD_NUMBER: _ClassVar[int]
        storage_device_snapshot_info: _storage_pb2.StorageDeviceSnapshotInfoProto
        mounted_datastore: SetupRestoreDiskTaskInfo.DatastoreInfo
        record_volume_for_gc: bool
        snapshot_time_usecs: int
        src_datastore_name: str
        def __init__(self, storage_device_snapshot_info: _Optional[_Union[_storage_pb2.StorageDeviceSnapshotInfoProto, _Mapping]] = ..., mounted_datastore: _Optional[_Union[SetupRestoreDiskTaskInfo.DatastoreInfo, _Mapping]] = ..., record_volume_for_gc: bool = ..., snapshot_time_usecs: _Optional[int] = ..., src_datastore_name: _Optional[str] = ...) -> None: ...
    class RestorePathToDiskUuidMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    VMWARE_SETUP_RESTORE_DISK_TASK_INFO_FIELD_NUMBER: _ClassVar[int]
    vmware_setup_restore_disk_task_info: _descriptor.FieldDescriptor
    SETUP_STATE_FIELD_NUMBER: _ClassVar[int]
    SETUP_ERROR_FIELD_NUMBER: _ClassVar[int]
    TEARDOWN_STATE_FIELD_NUMBER: _ClassVar[int]
    TEARDOWN_ERROR_FIELD_NUMBER: _ClassVar[int]
    RELATIVE_RESTORE_PATH_VEC_FIELD_NUMBER: _ClassVar[int]
    ENCODED_DISK_PATH_VEC_FIELD_NUMBER: _ClassVar[int]
    DATASTORE_INFO_FIELD_NUMBER: _ClassVar[int]
    ATTACHED_DISK_MAP_FIELD_NUMBER: _ClassVar[int]
    EXISTING_VOLUME_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    ATTACHED_VOLUME_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    VOLUME_FILE_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    MOUNT_VOLUME_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_FILES_CLONED_FIELD_NUMBER: _ClassVar[int]
    DISK_TO_CONTROLLER_KEY_MAP_FIELD_NUMBER: _ClassVar[int]
    NEW_TO_OLD_DISK_UUID_MAP_FIELD_NUMBER: _ClassVar[int]
    DISK_UUID_TO_PROVISIONING_INFO_MAP_FIELD_NUMBER: _ClassVar[int]
    DISK_UNIQUE_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    CLONED_STORAGE_SNAPSHOT_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    CURR_SNAPSHOT_IDX_FIELD_NUMBER: _ClassVar[int]
    RESTORE_PATH_TO_DISK_UUID_MAP_FIELD_NUMBER: _ClassVar[int]
    setup_state: SetupRestoreDiskTaskInfo.SetupState
    setup_error: _error_pb2.ErrorProto
    teardown_state: SetupRestoreDiskTaskInfo.TeardownState
    teardown_error: _error_pb2.ErrorProto
    relative_restore_path_vec: _containers.RepeatedScalarFieldContainer[str]
    encoded_disk_path_vec: _containers.RepeatedScalarFieldContainer[str]
    datastore_info: SetupRestoreDiskTaskInfo.DatastoreInfo
    attached_disk_map: _containers.MessageMap[str, SetupRestoreDiskTaskInfo.AttachedDiskInfo]
    existing_volume_info_vec: _containers.RepeatedCompositeFieldContainer[_agent_pb2.VolumeInfoProto]
    attached_volume_info_vec: _containers.RepeatedCompositeFieldContainer[_agent_pb2.VolumeInfoProto]
    volume_file_info_vec: _containers.RepeatedCompositeFieldContainer[_volume_info_pb2.VolumeInfo]
    mount_volume_info_vec: _containers.RepeatedCompositeFieldContainer[_agent_pb2.MountVolumeInfo]
    snapshot_files_cloned: bool
    disk_to_controller_key_map: _containers.ScalarMap[str, int]
    new_to_old_disk_uuid_map: _containers.ScalarMap[str, str]
    disk_uuid_to_provisioning_info_map: _containers.MessageMap[str, SetupRestoreDiskTaskInfo.DiskProvisioningInfo]
    disk_unique_id_vec: _containers.RepeatedScalarFieldContainer[str]
    cloned_storage_snapshot_info_vec: _containers.RepeatedCompositeFieldContainer[SetupRestoreDiskTaskInfo.ClonedStorageSnapshotInfo]
    curr_snapshot_idx: int
    restore_path_to_disk_uuid_map: _containers.ScalarMap[str, str]
    def __init__(self, setup_state: _Optional[_Union[SetupRestoreDiskTaskInfo.SetupState, str]] = ..., setup_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., teardown_state: _Optional[_Union[SetupRestoreDiskTaskInfo.TeardownState, str]] = ..., teardown_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., relative_restore_path_vec: _Optional[_Iterable[str]] = ..., encoded_disk_path_vec: _Optional[_Iterable[str]] = ..., datastore_info: _Optional[_Union[SetupRestoreDiskTaskInfo.DatastoreInfo, _Mapping]] = ..., attached_disk_map: _Optional[_Mapping[str, SetupRestoreDiskTaskInfo.AttachedDiskInfo]] = ..., existing_volume_info_vec: _Optional[_Iterable[_Union[_agent_pb2.VolumeInfoProto, _Mapping]]] = ..., attached_volume_info_vec: _Optional[_Iterable[_Union[_agent_pb2.VolumeInfoProto, _Mapping]]] = ..., volume_file_info_vec: _Optional[_Iterable[_Union[_volume_info_pb2.VolumeInfo, _Mapping]]] = ..., mount_volume_info_vec: _Optional[_Iterable[_Union[_agent_pb2.MountVolumeInfo, _Mapping]]] = ..., snapshot_files_cloned: bool = ..., disk_to_controller_key_map: _Optional[_Mapping[str, int]] = ..., new_to_old_disk_uuid_map: _Optional[_Mapping[str, str]] = ..., disk_uuid_to_provisioning_info_map: _Optional[_Mapping[str, SetupRestoreDiskTaskInfo.DiskProvisioningInfo]] = ..., disk_unique_id_vec: _Optional[_Iterable[str]] = ..., cloned_storage_snapshot_info_vec: _Optional[_Iterable[_Union[SetupRestoreDiskTaskInfo.ClonedStorageSnapshotInfo, _Mapping]]] = ..., curr_snapshot_idx: _Optional[int] = ..., restore_path_to_disk_uuid_map: _Optional[_Mapping[str, str]] = ...) -> None: ...
