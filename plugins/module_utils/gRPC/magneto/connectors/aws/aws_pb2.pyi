from bridge.vault.base import vault_pb2 as _vault_pb2
from magneto.base import cloud_pb2 as _cloud_pb2
from magneto.base import policy_pb2 as _policy_pb2
from magneto.base import disk_pb2 as _disk_pb2
from magneto.base import error_pb2 as _error_pb2
from magneto.base import magneto_pb2 as _magneto_pb2
from magneto.base import env_params_pb2 as _env_params_pb2
from magneto.base import proxy_pb2 as _proxy_pb2
from magneto.base import sub_task_pb2 as _sub_task_pb2
from magneto.connectors.aws import aws_param_pb2 as _aws_param_pb2
from magneto.connectors.cloud import cloud_pb2 as _cloud_pb2_1
from magneto.connectors.file import file_pb2 as _file_pb2
from nexus.cloud.connectors.aws import rds_params_pb2 as _rds_params_pb2
from util import cbt_delta_pb2 as _cbt_delta_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ConvertVMDKToVHDxInfo(_message.Message):
    __slots__ = ("status", "name", "disk_area_start_offset")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kStarted: _ClassVar[ConvertVMDKToVHDxInfo.Status]
        kEmptyVHDxCreated: _ClassVar[ConvertVMDKToVHDxInfo.Status]
        kFinished: _ClassVar[ConvertVMDKToVHDxInfo.Status]
    kStarted: ConvertVMDKToVHDxInfo.Status
    kEmptyVHDxCreated: ConvertVMDKToVHDxInfo.Status
    kFinished: ConvertVMDKToVHDxInfo.Status
    STATUS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISK_AREA_START_OFFSET_FIELD_NUMBER: _ClassVar[int]
    status: ConvertVMDKToVHDxInfo.Status
    name: str
    disk_area_start_offset: int
    def __init__(self, status: _Optional[_Union[ConvertVMDKToVHDxInfo.Status, str]] = ..., name: _Optional[str] = ..., disk_area_start_offset: _Optional[int] = ...) -> None: ...

class CloudDeployEntityInfo(_message.Message):
    __slots__ = ("vm_info", "common_info", "snapshot_info")
    class DiskInfo(_message.Message):
        __slots__ = ("vm_disk_relative_path", "is_boot_disk", "s3_object_name", "s3_object_size_bytes", "s3_object_upload_context", "import_image_task_id", "import_snapshot_task_id", "snapshot_id", "ebs_volume", "block_device_mapping", "use_proxy_vm", "lowest_unfinished_offset", "amis_snapshot_id", "use_ebs_write_api", "changed_blocks_count", "vmdk_to_vhdx_info")
        VM_DISK_RELATIVE_PATH_FIELD_NUMBER: _ClassVar[int]
        IS_BOOT_DISK_FIELD_NUMBER: _ClassVar[int]
        S3_OBJECT_NAME_FIELD_NUMBER: _ClassVar[int]
        S3_OBJECT_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
        S3_OBJECT_UPLOAD_CONTEXT_FIELD_NUMBER: _ClassVar[int]
        IMPORT_IMAGE_TASK_ID_FIELD_NUMBER: _ClassVar[int]
        IMPORT_SNAPSHOT_TASK_ID_FIELD_NUMBER: _ClassVar[int]
        SNAPSHOT_ID_FIELD_NUMBER: _ClassVar[int]
        EBS_VOLUME_FIELD_NUMBER: _ClassVar[int]
        BLOCK_DEVICE_MAPPING_FIELD_NUMBER: _ClassVar[int]
        USE_PROXY_VM_FIELD_NUMBER: _ClassVar[int]
        LOWEST_UNFINISHED_OFFSET_FIELD_NUMBER: _ClassVar[int]
        AMIS_SNAPSHOT_ID_FIELD_NUMBER: _ClassVar[int]
        USE_EBS_WRITE_API_FIELD_NUMBER: _ClassVar[int]
        CHANGED_BLOCKS_COUNT_FIELD_NUMBER: _ClassVar[int]
        VMDK_TO_VHDX_INFO_FIELD_NUMBER: _ClassVar[int]
        vm_disk_relative_path: str
        is_boot_disk: bool
        s3_object_name: str
        s3_object_size_bytes: int
        s3_object_upload_context: _vault_pb2.VaultUploadContextProto
        import_image_task_id: str
        import_snapshot_task_id: str
        snapshot_id: str
        ebs_volume: EBSVolume
        block_device_mapping: _aws_param_pb2.BlockDeviceMapping
        use_proxy_vm: bool
        lowest_unfinished_offset: int
        amis_snapshot_id: str
        use_ebs_write_api: bool
        changed_blocks_count: int
        vmdk_to_vhdx_info: ConvertVMDKToVHDxInfo
        def __init__(self, vm_disk_relative_path: _Optional[str] = ..., is_boot_disk: bool = ..., s3_object_name: _Optional[str] = ..., s3_object_size_bytes: _Optional[int] = ..., s3_object_upload_context: _Optional[_Union[_vault_pb2.VaultUploadContextProto, _Mapping]] = ..., import_image_task_id: _Optional[str] = ..., import_snapshot_task_id: _Optional[str] = ..., snapshot_id: _Optional[str] = ..., ebs_volume: _Optional[_Union[EBSVolume, _Mapping]] = ..., block_device_mapping: _Optional[_Union[_aws_param_pb2.BlockDeviceMapping, _Mapping]] = ..., use_proxy_vm: bool = ..., lowest_unfinished_offset: _Optional[int] = ..., amis_snapshot_id: _Optional[str] = ..., use_ebs_write_api: bool = ..., changed_blocks_count: _Optional[int] = ..., vmdk_to_vhdx_info: _Optional[_Union[ConvertVMDKToVHDxInfo, _Mapping]] = ...) -> None: ...
    class VMInfo(_message.Message):
        __slots__ = ("instance_id", "private_ip_address", "is_windows_vm", "disk_info_map", "aws_ami_id", "db_snapshot_info", "import_status", "converter_instance_id", "is_cohesity_imported_vm", "boot_mode", "attach_non_boot_disks", "aws_s3_object_name", "aws_s3_object_size", "aws_s3_object_vm_disk_relative_filepath", "aws_ebs_volume_names", "aws_ebs_volume_sizes", "aws_ebs_volume_vm_disk_relative_filepaths", "boot_disk_index", "boot_disk_s3_upload_context", "vm_config", "name")
        class ImportStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kStarted: _ClassVar[CloudDeployEntityInfo.VMInfo.ImportStatus]
            kPermitGranted: _ClassVar[CloudDeployEntityInfo.VMInfo.ImportStatus]
            kConverterVMCreated: _ClassVar[CloudDeployEntityInfo.VMInfo.ImportStatus]
            kEBSVolumeAttached: _ClassVar[CloudDeployEntityInfo.VMInfo.ImportStatus]
            kEBSVolumePrepared: _ClassVar[CloudDeployEntityInfo.VMInfo.ImportStatus]
            kEBSVolumeDetached: _ClassVar[CloudDeployEntityInfo.VMInfo.ImportStatus]
            kConverterVMTerminated: _ClassVar[CloudDeployEntityInfo.VMInfo.ImportStatus]
            kAMICreated: _ClassVar[CloudDeployEntityInfo.VMInfo.ImportStatus]
            kVerifyVMImportFinished: _ClassVar[CloudDeployEntityInfo.VMInfo.ImportStatus]
            kFinished: _ClassVar[CloudDeployEntityInfo.VMInfo.ImportStatus]
        kStarted: CloudDeployEntityInfo.VMInfo.ImportStatus
        kPermitGranted: CloudDeployEntityInfo.VMInfo.ImportStatus
        kConverterVMCreated: CloudDeployEntityInfo.VMInfo.ImportStatus
        kEBSVolumeAttached: CloudDeployEntityInfo.VMInfo.ImportStatus
        kEBSVolumePrepared: CloudDeployEntityInfo.VMInfo.ImportStatus
        kEBSVolumeDetached: CloudDeployEntityInfo.VMInfo.ImportStatus
        kConverterVMTerminated: CloudDeployEntityInfo.VMInfo.ImportStatus
        kAMICreated: CloudDeployEntityInfo.VMInfo.ImportStatus
        kVerifyVMImportFinished: CloudDeployEntityInfo.VMInfo.ImportStatus
        kFinished: CloudDeployEntityInfo.VMInfo.ImportStatus
        class DiskInfoMapEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: int
            value: CloudDeployEntityInfo.DiskInfo
            def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[CloudDeployEntityInfo.DiskInfo, _Mapping]] = ...) -> None: ...
        INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
        PRIVATE_IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
        IS_WINDOWS_VM_FIELD_NUMBER: _ClassVar[int]
        DISK_INFO_MAP_FIELD_NUMBER: _ClassVar[int]
        AWS_AMI_ID_FIELD_NUMBER: _ClassVar[int]
        DB_SNAPSHOT_INFO_FIELD_NUMBER: _ClassVar[int]
        IMPORT_STATUS_FIELD_NUMBER: _ClassVar[int]
        CONVERTER_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
        IS_COHESITY_IMPORTED_VM_FIELD_NUMBER: _ClassVar[int]
        BOOT_MODE_FIELD_NUMBER: _ClassVar[int]
        ATTACH_NON_BOOT_DISKS_FIELD_NUMBER: _ClassVar[int]
        AWS_S3_OBJECT_NAME_FIELD_NUMBER: _ClassVar[int]
        AWS_S3_OBJECT_SIZE_FIELD_NUMBER: _ClassVar[int]
        AWS_S3_OBJECT_VM_DISK_RELATIVE_FILEPATH_FIELD_NUMBER: _ClassVar[int]
        AWS_EBS_VOLUME_NAMES_FIELD_NUMBER: _ClassVar[int]
        AWS_EBS_VOLUME_SIZES_FIELD_NUMBER: _ClassVar[int]
        AWS_EBS_VOLUME_VM_DISK_RELATIVE_FILEPATHS_FIELD_NUMBER: _ClassVar[int]
        BOOT_DISK_INDEX_FIELD_NUMBER: _ClassVar[int]
        BOOT_DISK_S3_UPLOAD_CONTEXT_FIELD_NUMBER: _ClassVar[int]
        VM_CONFIG_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        instance_id: str
        private_ip_address: str
        is_windows_vm: bool
        disk_info_map: _containers.MessageMap[int, CloudDeployEntityInfo.DiskInfo]
        aws_ami_id: str
        db_snapshot_info: _rds_params_pb2.SnapshotInfo
        import_status: CloudDeployEntityInfo.VMInfo.ImportStatus
        converter_instance_id: str
        is_cohesity_imported_vm: bool
        boot_mode: _aws_param_pb2.BootMode.Type
        attach_non_boot_disks: bool
        aws_s3_object_name: str
        aws_s3_object_size: int
        aws_s3_object_vm_disk_relative_filepath: str
        aws_ebs_volume_names: _containers.RepeatedScalarFieldContainer[str]
        aws_ebs_volume_sizes: _containers.RepeatedScalarFieldContainer[int]
        aws_ebs_volume_vm_disk_relative_filepaths: _containers.RepeatedScalarFieldContainer[str]
        boot_disk_index: int
        boot_disk_s3_upload_context: _vault_pb2.VaultUploadContextProto
        vm_config: VMConfig
        name: str
        def __init__(self, instance_id: _Optional[str] = ..., private_ip_address: _Optional[str] = ..., is_windows_vm: bool = ..., disk_info_map: _Optional[_Mapping[int, CloudDeployEntityInfo.DiskInfo]] = ..., aws_ami_id: _Optional[str] = ..., db_snapshot_info: _Optional[_Union[_rds_params_pb2.SnapshotInfo, _Mapping]] = ..., import_status: _Optional[_Union[CloudDeployEntityInfo.VMInfo.ImportStatus, str]] = ..., converter_instance_id: _Optional[str] = ..., is_cohesity_imported_vm: bool = ..., boot_mode: _Optional[_Union[_aws_param_pb2.BootMode.Type, str]] = ..., attach_non_boot_disks: bool = ..., aws_s3_object_name: _Optional[str] = ..., aws_s3_object_size: _Optional[int] = ..., aws_s3_object_vm_disk_relative_filepath: _Optional[str] = ..., aws_ebs_volume_names: _Optional[_Iterable[str]] = ..., aws_ebs_volume_sizes: _Optional[_Iterable[int]] = ..., aws_ebs_volume_vm_disk_relative_filepaths: _Optional[_Iterable[str]] = ..., boot_disk_index: _Optional[int] = ..., boot_disk_s3_upload_context: _Optional[_Union[_vault_pb2.VaultUploadContextProto, _Mapping]] = ..., vm_config: _Optional[_Union[VMConfig, _Mapping]] = ..., name: _Optional[str] = ...) -> None: ...
    AWS_RESTORE_ENTITY_INFO_FIELD_NUMBER: _ClassVar[int]
    aws_restore_entity_info: _descriptor.FieldDescriptor
    AWS_CLOUD_DEPLOY_ENTITY_INFO_FIELD_NUMBER: _ClassVar[int]
    aws_cloud_deploy_entity_info: _descriptor.FieldDescriptor
    VM_INFO_FIELD_NUMBER: _ClassVar[int]
    COMMON_INFO_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_INFO_FIELD_NUMBER: _ClassVar[int]
    vm_info: CloudDeployEntityInfo.VMInfo
    common_info: _cloud_pb2_1.CloudEntityCommonInfo
    snapshot_info: _magneto_pb2.SnapshotInfoProto
    def __init__(self, vm_info: _Optional[_Union[CloudDeployEntityInfo.VMInfo, _Mapping]] = ..., common_info: _Optional[_Union[_cloud_pb2_1.CloudEntityCommonInfo, _Mapping]] = ..., snapshot_info: _Optional[_Union[_magneto_pb2.SnapshotInfoProto, _Mapping]] = ...) -> None: ...

class ReplicationEntityInfo(_message.Message):
    __slots__ = ("type", "ebs_snapshot_id_map", "ami_id", "vm_config", "db_snapshot_arn", "db_snapshot_id", "cloud_replication_target")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kEBSSnapshot: _ClassVar[ReplicationEntityInfo.Type]
        kAMI: _ClassVar[ReplicationEntityInfo.Type]
        kRDSSnapshot: _ClassVar[ReplicationEntityInfo.Type]
    kEBSSnapshot: ReplicationEntityInfo.Type
    kAMI: ReplicationEntityInfo.Type
    kRDSSnapshot: ReplicationEntityInfo.Type
    class EbsSnapshotIdMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: str
        def __init__(self, key: _Optional[int] = ..., value: _Optional[str] = ...) -> None: ...
    AWS_REPLICATION_ENTITY_INFO_FIELD_NUMBER: _ClassVar[int]
    aws_replication_entity_info: _descriptor.FieldDescriptor
    TYPE_FIELD_NUMBER: _ClassVar[int]
    EBS_SNAPSHOT_ID_MAP_FIELD_NUMBER: _ClassVar[int]
    AMI_ID_FIELD_NUMBER: _ClassVar[int]
    VM_CONFIG_FIELD_NUMBER: _ClassVar[int]
    DB_SNAPSHOT_ARN_FIELD_NUMBER: _ClassVar[int]
    DB_SNAPSHOT_ID_FIELD_NUMBER: _ClassVar[int]
    CLOUD_REPLICATION_TARGET_FIELD_NUMBER: _ClassVar[int]
    type: ReplicationEntityInfo.Type
    ebs_snapshot_id_map: _containers.ScalarMap[int, str]
    ami_id: str
    vm_config: VMConfig
    db_snapshot_arn: str
    db_snapshot_id: str
    cloud_replication_target: _policy_pb2.CloudDeployTarget
    def __init__(self, type: _Optional[_Union[ReplicationEntityInfo.Type, str]] = ..., ebs_snapshot_id_map: _Optional[_Mapping[int, str]] = ..., ami_id: _Optional[str] = ..., vm_config: _Optional[_Union[VMConfig, _Mapping]] = ..., db_snapshot_arn: _Optional[str] = ..., db_snapshot_id: _Optional[str] = ..., cloud_replication_target: _Optional[_Union[_policy_pb2.CloudDeployTarget, _Mapping]] = ...) -> None: ...

class ReplicationInfo(_message.Message):
    __slots__ = ("status", "error", "take_account_permit")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kStarted: _ClassVar[ReplicationInfo.Status]
        kPermitGranted: _ClassVar[ReplicationInfo.Status]
        kCloned: _ClassVar[ReplicationInfo.Status]
        kVMInfoFetched: _ClassVar[ReplicationInfo.Status]
        kSnapshotsCopied: _ClassVar[ReplicationInfo.Status]
        kFinished: _ClassVar[ReplicationInfo.Status]
    kStarted: ReplicationInfo.Status
    kPermitGranted: ReplicationInfo.Status
    kCloned: ReplicationInfo.Status
    kVMInfoFetched: ReplicationInfo.Status
    kSnapshotsCopied: ReplicationInfo.Status
    kFinished: ReplicationInfo.Status
    AWS_REPLICATION_INFO_FIELD_NUMBER: _ClassVar[int]
    aws_replication_info: _descriptor.FieldDescriptor
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    TAKE_ACCOUNT_PERMIT_FIELD_NUMBER: _ClassVar[int]
    status: ReplicationInfo.Status
    error: _error_pb2.ErrorProto
    take_account_permit: bool
    def __init__(self, status: _Optional[_Union[ReplicationInfo.Status, str]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., take_account_permit: bool = ...) -> None: ...

class CloudDeployInfo(_message.Message):
    __slots__ = ("status", "error", "view_deletion_error", "to_recover_vm_idx", "to_recover_disk_idx", "to_recover_disk_lowest_offset", "s3_bucket_name", "sub_tasks_vec", "total_bytes_to_write_to_source", "take_iam_permit", "take_account_permit", "prev_highest_sub_task_id", "take_proxy_permit_on_dummy_entity", "is_using_new_aws_convert_and_deploy", "use_cohesity_aws_import_export", "verify_vm_import", "cohesity_aws_import_error", "enable_start_snapshot_in_sub_task")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kStarted: _ClassVar[CloudDeployInfo.Status]
        kProgressMonitorsCreated: _ClassVar[CloudDeployInfo.Status]
        kPermitGranted: _ClassVar[CloudDeployInfo.Status]
        kVHDxCreated: _ClassVar[CloudDeployInfo.Status]
        kCloned: _ClassVar[CloudDeployInfo.Status]
        kVMInfoFetched: _ClassVar[CloudDeployInfo.Status]
        kConflictChecked: _ClassVar[CloudDeployInfo.Status]
        kS3BucketCreated: _ClassVar[CloudDeployInfo.Status]
        kVMImportRoleCreated: _ClassVar[CloudDeployInfo.Status]
        kS3ObjectsCreated: _ClassVar[CloudDeployInfo.Status]
        kEBSVolumesAttached: _ClassVar[CloudDeployInfo.Status]
        kVMFilesCopied: _ClassVar[CloudDeployInfo.Status]
        kSubTasksCreated: _ClassVar[CloudDeployInfo.Status]
        kSubTasksFinished: _ClassVar[CloudDeployInfo.Status]
        kS3ObjectsFinalized: _ClassVar[CloudDeployInfo.Status]
        kFullUploadSubTasksFinished: _ClassVar[CloudDeployInfo.Status]
        kDiffUploadSubTasksFinished: _ClassVar[CloudDeployInfo.Status]
        kBridgeStateCleared: _ClassVar[CloudDeployInfo.Status]
        kSnapshotsCreated: _ClassVar[CloudDeployInfo.Status]
        kVMsImported: _ClassVar[CloudDeployInfo.Status]
        kVMCreated: _ClassVar[CloudDeployInfo.Status]
        kFinished: _ClassVar[CloudDeployInfo.Status]
    kStarted: CloudDeployInfo.Status
    kProgressMonitorsCreated: CloudDeployInfo.Status
    kPermitGranted: CloudDeployInfo.Status
    kVHDxCreated: CloudDeployInfo.Status
    kCloned: CloudDeployInfo.Status
    kVMInfoFetched: CloudDeployInfo.Status
    kConflictChecked: CloudDeployInfo.Status
    kS3BucketCreated: CloudDeployInfo.Status
    kVMImportRoleCreated: CloudDeployInfo.Status
    kS3ObjectsCreated: CloudDeployInfo.Status
    kEBSVolumesAttached: CloudDeployInfo.Status
    kVMFilesCopied: CloudDeployInfo.Status
    kSubTasksCreated: CloudDeployInfo.Status
    kSubTasksFinished: CloudDeployInfo.Status
    kS3ObjectsFinalized: CloudDeployInfo.Status
    kFullUploadSubTasksFinished: CloudDeployInfo.Status
    kDiffUploadSubTasksFinished: CloudDeployInfo.Status
    kBridgeStateCleared: CloudDeployInfo.Status
    kSnapshotsCreated: CloudDeployInfo.Status
    kVMsImported: CloudDeployInfo.Status
    kVMCreated: CloudDeployInfo.Status
    kFinished: CloudDeployInfo.Status
    AWS_RESTORE_INFO_FIELD_NUMBER: _ClassVar[int]
    aws_restore_info: _descriptor.FieldDescriptor
    AWS_CLOUD_DEPLOY_INFO_FIELD_NUMBER: _ClassVar[int]
    aws_cloud_deploy_info: _descriptor.FieldDescriptor
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    VIEW_DELETION_ERROR_FIELD_NUMBER: _ClassVar[int]
    TO_RECOVER_VM_IDX_FIELD_NUMBER: _ClassVar[int]
    TO_RECOVER_DISK_IDX_FIELD_NUMBER: _ClassVar[int]
    TO_RECOVER_DISK_LOWEST_OFFSET_FIELD_NUMBER: _ClassVar[int]
    S3_BUCKET_NAME_FIELD_NUMBER: _ClassVar[int]
    SUB_TASKS_VEC_FIELD_NUMBER: _ClassVar[int]
    TOTAL_BYTES_TO_WRITE_TO_SOURCE_FIELD_NUMBER: _ClassVar[int]
    TAKE_IAM_PERMIT_FIELD_NUMBER: _ClassVar[int]
    TAKE_ACCOUNT_PERMIT_FIELD_NUMBER: _ClassVar[int]
    PREV_HIGHEST_SUB_TASK_ID_FIELD_NUMBER: _ClassVar[int]
    TAKE_PROXY_PERMIT_ON_DUMMY_ENTITY_FIELD_NUMBER: _ClassVar[int]
    IS_USING_NEW_AWS_CONVERT_AND_DEPLOY_FIELD_NUMBER: _ClassVar[int]
    USE_COHESITY_AWS_IMPORT_EXPORT_FIELD_NUMBER: _ClassVar[int]
    VERIFY_VM_IMPORT_FIELD_NUMBER: _ClassVar[int]
    COHESITY_AWS_IMPORT_ERROR_FIELD_NUMBER: _ClassVar[int]
    ENABLE_START_SNAPSHOT_IN_SUB_TASK_FIELD_NUMBER: _ClassVar[int]
    status: CloudDeployInfo.Status
    error: _error_pb2.ErrorProto
    view_deletion_error: _error_pb2.ErrorProto
    to_recover_vm_idx: int
    to_recover_disk_idx: int
    to_recover_disk_lowest_offset: int
    s3_bucket_name: str
    sub_tasks_vec: _containers.RepeatedCompositeFieldContainer[_sub_task_pb2.SubTaskInfo]
    total_bytes_to_write_to_source: int
    take_iam_permit: bool
    take_account_permit: bool
    prev_highest_sub_task_id: int
    take_proxy_permit_on_dummy_entity: bool
    is_using_new_aws_convert_and_deploy: bool
    use_cohesity_aws_import_export: bool
    verify_vm_import: bool
    cohesity_aws_import_error: _error_pb2.ErrorProto
    enable_start_snapshot_in_sub_task: bool
    def __init__(self, status: _Optional[_Union[CloudDeployInfo.Status, str]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., view_deletion_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., to_recover_vm_idx: _Optional[int] = ..., to_recover_disk_idx: _Optional[int] = ..., to_recover_disk_lowest_offset: _Optional[int] = ..., s3_bucket_name: _Optional[str] = ..., sub_tasks_vec: _Optional[_Iterable[_Union[_sub_task_pb2.SubTaskInfo, _Mapping]]] = ..., total_bytes_to_write_to_source: _Optional[int] = ..., take_iam_permit: bool = ..., take_account_permit: bool = ..., prev_highest_sub_task_id: _Optional[int] = ..., take_proxy_permit_on_dummy_entity: bool = ..., is_using_new_aws_convert_and_deploy: bool = ..., use_cohesity_aws_import_export: bool = ..., verify_vm_import: bool = ..., cohesity_aws_import_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., enable_start_snapshot_in_sub_task: bool = ...) -> None: ...

class ClonedEntityInfo(_message.Message):
    __slots__ = ("vm_info",)
    class VMInfo(_message.Message):
        __slots__ = ("s3_bucket_name", "s3_object_vec", "ebs_volume_vec", "ami_id", "instance_id", "snapshot_id_vec")
        S3_BUCKET_NAME_FIELD_NUMBER: _ClassVar[int]
        S3_OBJECT_VEC_FIELD_NUMBER: _ClassVar[int]
        EBS_VOLUME_VEC_FIELD_NUMBER: _ClassVar[int]
        AMI_ID_FIELD_NUMBER: _ClassVar[int]
        INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
        SNAPSHOT_ID_VEC_FIELD_NUMBER: _ClassVar[int]
        s3_bucket_name: str
        s3_object_vec: _containers.RepeatedScalarFieldContainer[str]
        ebs_volume_vec: _containers.RepeatedScalarFieldContainer[str]
        ami_id: str
        instance_id: str
        snapshot_id_vec: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, s3_bucket_name: _Optional[str] = ..., s3_object_vec: _Optional[_Iterable[str]] = ..., ebs_volume_vec: _Optional[_Iterable[str]] = ..., ami_id: _Optional[str] = ..., instance_id: _Optional[str] = ..., snapshot_id_vec: _Optional[_Iterable[str]] = ...) -> None: ...
    AWS_CLONED_ENTITY_INFO_FIELD_NUMBER: _ClassVar[int]
    aws_cloned_entity_info: _descriptor.FieldDescriptor
    VM_INFO_FIELD_NUMBER: _ClassVar[int]
    vm_info: ClonedEntityInfo.VMInfo
    def __init__(self, vm_info: _Optional[_Union[ClonedEntityInfo.VMInfo, _Mapping]] = ...) -> None: ...

class SystemSubTaskInfo(_message.Message):
    __slots__ = ("status", "error", "create_image_state", "launch_instance_state", "create_bucket_state", "export_instance_state", "download_disk_state", "convert_disk_state", "copy_volume_data_state", "dr_to_cloud_vm_info", "is_incremental")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kStarted: _ClassVar[SystemSubTaskInfo.Status]
        kCreateImage: _ClassVar[SystemSubTaskInfo.Status]
        kLaunchInstance: _ClassVar[SystemSubTaskInfo.Status]
        kCreateBucket: _ClassVar[SystemSubTaskInfo.Status]
        kExportInstance: _ClassVar[SystemSubTaskInfo.Status]
        kWaitForExportInstance: _ClassVar[SystemSubTaskInfo.Status]
        kDownloadDisk: _ClassVar[SystemSubTaskInfo.Status]
        kConvertDisk: _ClassVar[SystemSubTaskInfo.Status]
        kCloneRootDisk: _ClassVar[SystemSubTaskInfo.Status]
        kFinished: _ClassVar[SystemSubTaskInfo.Status]
    kStarted: SystemSubTaskInfo.Status
    kCreateImage: SystemSubTaskInfo.Status
    kLaunchInstance: SystemSubTaskInfo.Status
    kCreateBucket: SystemSubTaskInfo.Status
    kExportInstance: SystemSubTaskInfo.Status
    kWaitForExportInstance: SystemSubTaskInfo.Status
    kDownloadDisk: SystemSubTaskInfo.Status
    kConvertDisk: SystemSubTaskInfo.Status
    kCloneRootDisk: SystemSubTaskInfo.Status
    kFinished: SystemSubTaskInfo.Status
    class CreateImageState(_message.Message):
        __slots__ = ("image_name", "image_id")
        IMAGE_NAME_FIELD_NUMBER: _ClassVar[int]
        IMAGE_ID_FIELD_NUMBER: _ClassVar[int]
        image_name: str
        image_id: str
        def __init__(self, image_name: _Optional[str] = ..., image_id: _Optional[str] = ...) -> None: ...
    class LaunchInstanceState(_message.Message):
        __slots__ = ("vm_name", "instance_id")
        VM_NAME_FIELD_NUMBER: _ClassVar[int]
        INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
        vm_name: str
        instance_id: str
        def __init__(self, vm_name: _Optional[str] = ..., instance_id: _Optional[str] = ...) -> None: ...
    class CreateBucketState(_message.Message):
        __slots__ = ("disk_s3_bucket_name",)
        DISK_S3_BUCKET_NAME_FIELD_NUMBER: _ClassVar[int]
        disk_s3_bucket_name: str
        def __init__(self, disk_s3_bucket_name: _Optional[str] = ...) -> None: ...
    class ExportInstanceState(_message.Message):
        __slots__ = ("disk_s3_prefix", "disk_s3_key", "disk_size_bytes", "export_task_id")
        DISK_S3_PREFIX_FIELD_NUMBER: _ClassVar[int]
        DISK_S3_KEY_FIELD_NUMBER: _ClassVar[int]
        DISK_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
        EXPORT_TASK_ID_FIELD_NUMBER: _ClassVar[int]
        disk_s3_prefix: str
        disk_s3_key: str
        disk_size_bytes: int
        export_task_id: str
        def __init__(self, disk_s3_prefix: _Optional[str] = ..., disk_s3_key: _Optional[str] = ..., disk_size_bytes: _Optional[int] = ..., export_task_id: _Optional[str] = ...) -> None: ...
    class DownloadDiskState(_message.Message):
        __slots__ = ("disk_rel_file_path", "next_offset")
        DISK_REL_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
        NEXT_OFFSET_FIELD_NUMBER: _ClassVar[int]
        disk_rel_file_path: str
        next_offset: int
        def __init__(self, disk_rel_file_path: _Optional[str] = ..., next_offset: _Optional[int] = ...) -> None: ...
    class ConvertDiskState(_message.Message):
        __slots__ = ("converted_disk_rel_file_path",)
        CONVERTED_DISK_REL_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
        converted_disk_rel_file_path: str
        def __init__(self, converted_disk_rel_file_path: _Optional[str] = ...) -> None: ...
    class CopyVolumeDataState(_message.Message):
        __slots__ = ("virtual_disk_rel_file_path",)
        VIRTUAL_DISK_REL_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
        virtual_disk_rel_file_path: str
        def __init__(self, virtual_disk_rel_file_path: _Optional[str] = ...) -> None: ...
    SYSTEM_SUB_TASK_INFO_FIELD_NUMBER: _ClassVar[int]
    system_sub_task_info: _descriptor.FieldDescriptor
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    CREATE_IMAGE_STATE_FIELD_NUMBER: _ClassVar[int]
    LAUNCH_INSTANCE_STATE_FIELD_NUMBER: _ClassVar[int]
    CREATE_BUCKET_STATE_FIELD_NUMBER: _ClassVar[int]
    EXPORT_INSTANCE_STATE_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_DISK_STATE_FIELD_NUMBER: _ClassVar[int]
    CONVERT_DISK_STATE_FIELD_NUMBER: _ClassVar[int]
    COPY_VOLUME_DATA_STATE_FIELD_NUMBER: _ClassVar[int]
    DR_TO_CLOUD_VM_INFO_FIELD_NUMBER: _ClassVar[int]
    IS_INCREMENTAL_FIELD_NUMBER: _ClassVar[int]
    status: SystemSubTaskInfo.Status
    error: _error_pb2.ErrorProto
    create_image_state: SystemSubTaskInfo.CreateImageState
    launch_instance_state: SystemSubTaskInfo.LaunchInstanceState
    create_bucket_state: SystemSubTaskInfo.CreateBucketState
    export_instance_state: SystemSubTaskInfo.ExportInstanceState
    download_disk_state: SystemSubTaskInfo.DownloadDiskState
    convert_disk_state: SystemSubTaskInfo.ConvertDiskState
    copy_volume_data_state: SystemSubTaskInfo.CopyVolumeDataState
    dr_to_cloud_vm_info: _cloud_pb2.DRToCloudVMInfo
    is_incremental: bool
    def __init__(self, status: _Optional[_Union[SystemSubTaskInfo.Status, str]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., create_image_state: _Optional[_Union[SystemSubTaskInfo.CreateImageState, _Mapping]] = ..., launch_instance_state: _Optional[_Union[SystemSubTaskInfo.LaunchInstanceState, _Mapping]] = ..., create_bucket_state: _Optional[_Union[SystemSubTaskInfo.CreateBucketState, _Mapping]] = ..., export_instance_state: _Optional[_Union[SystemSubTaskInfo.ExportInstanceState, _Mapping]] = ..., download_disk_state: _Optional[_Union[SystemSubTaskInfo.DownloadDiskState, _Mapping]] = ..., convert_disk_state: _Optional[_Union[SystemSubTaskInfo.ConvertDiskState, _Mapping]] = ..., copy_volume_data_state: _Optional[_Union[SystemSubTaskInfo.CopyVolumeDataState, _Mapping]] = ..., dr_to_cloud_vm_info: _Optional[_Union[_cloud_pb2.DRToCloudVMInfo, _Mapping]] = ..., is_incremental: bool = ...) -> None: ...

class EBSVolume(_message.Message):
    __slots__ = ("key", "block_device_mapping", "snapshot_id", "snapshot_creation_time_usecs", "snapshot_volume_info", "status", "skip_close_disk", "delta_type", "last_position_backed_up", "total_bytes_read_from_source", "encoded_filename", "error", "exported_root_volume", "exported_disk_file_name", "skip_download")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kStarted: _ClassVar[EBSVolume.Status]
        kSnapshotCreated: _ClassVar[EBSVolume.Status]
        kSnapshotFinished: _ClassVar[EBSVolume.Status]
        kSnapshotAttached: _ClassVar[EBSVolume.Status]
        kSubTasksFinished: _ClassVar[EBSVolume.Status]
        kSnapshotDetached: _ClassVar[EBSVolume.Status]
        kVolumeDeleted: _ClassVar[EBSVolume.Status]
        kSnapshotDeleted: _ClassVar[EBSVolume.Status]
    kStarted: EBSVolume.Status
    kSnapshotCreated: EBSVolume.Status
    kSnapshotFinished: EBSVolume.Status
    kSnapshotAttached: EBSVolume.Status
    kSubTasksFinished: EBSVolume.Status
    kSnapshotDetached: EBSVolume.Status
    kVolumeDeleted: EBSVolume.Status
    kSnapshotDeleted: EBSVolume.Status
    class SnapshotVolumeInfo(_message.Message):
        __slots__ = ("snapshot_ebs_volume_id", "proxy_info", "snapshot_id")
        SNAPSHOT_EBS_VOLUME_ID_FIELD_NUMBER: _ClassVar[int]
        PROXY_INFO_FIELD_NUMBER: _ClassVar[int]
        SNAPSHOT_ID_FIELD_NUMBER: _ClassVar[int]
        snapshot_ebs_volume_id: str
        proxy_info: _proxy_pb2.ProxyInfo
        snapshot_id: str
        def __init__(self, snapshot_ebs_volume_id: _Optional[str] = ..., proxy_info: _Optional[_Union[_proxy_pb2.ProxyInfo, _Mapping]] = ..., snapshot_id: _Optional[str] = ...) -> None: ...
    AWS_EBS_VOLUME_FIELD_NUMBER: _ClassVar[int]
    aws_ebs_volume: _descriptor.FieldDescriptor
    KEY_FIELD_NUMBER: _ClassVar[int]
    BLOCK_DEVICE_MAPPING_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_ID_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_CREATION_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_VOLUME_INFO_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SKIP_CLOSE_DISK_FIELD_NUMBER: _ClassVar[int]
    DELTA_TYPE_FIELD_NUMBER: _ClassVar[int]
    LAST_POSITION_BACKED_UP_FIELD_NUMBER: _ClassVar[int]
    TOTAL_BYTES_READ_FROM_SOURCE_FIELD_NUMBER: _ClassVar[int]
    ENCODED_FILENAME_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    EXPORTED_ROOT_VOLUME_FIELD_NUMBER: _ClassVar[int]
    EXPORTED_DISK_FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    SKIP_DOWNLOAD_FIELD_NUMBER: _ClassVar[int]
    key: int
    block_device_mapping: _aws_param_pb2.BlockDeviceMapping
    snapshot_id: str
    snapshot_creation_time_usecs: int
    snapshot_volume_info: EBSVolume.SnapshotVolumeInfo
    status: EBSVolume.Status
    skip_close_disk: bool
    delta_type: _cbt_delta_pb2.CBTDeltaType.Type
    last_position_backed_up: int
    total_bytes_read_from_source: int
    encoded_filename: str
    error: _error_pb2.ErrorProto
    exported_root_volume: bool
    exported_disk_file_name: str
    skip_download: bool
    def __init__(self, key: _Optional[int] = ..., block_device_mapping: _Optional[_Union[_aws_param_pb2.BlockDeviceMapping, _Mapping]] = ..., snapshot_id: _Optional[str] = ..., snapshot_creation_time_usecs: _Optional[int] = ..., snapshot_volume_info: _Optional[_Union[EBSVolume.SnapshotVolumeInfo, _Mapping]] = ..., status: _Optional[_Union[EBSVolume.Status, str]] = ..., skip_close_disk: bool = ..., delta_type: _Optional[_Union[_cbt_delta_pb2.CBTDeltaType.Type, str]] = ..., last_position_backed_up: _Optional[int] = ..., total_bytes_read_from_source: _Optional[int] = ..., encoded_filename: _Optional[str] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., exported_root_volume: bool = ..., exported_disk_file_name: _Optional[str] = ..., skip_download: bool = ...) -> None: ...

class VMConfig(_message.Message):
    __slots__ = ("vm_info", "ebs_volumes_vec", "db_info", "db_snapshot_info", "cluster_db_snapshot_info")
    VM_INFO_FIELD_NUMBER: _ClassVar[int]
    EBS_VOLUMES_VEC_FIELD_NUMBER: _ClassVar[int]
    DB_INFO_FIELD_NUMBER: _ClassVar[int]
    DB_SNAPSHOT_INFO_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_DB_SNAPSHOT_INFO_FIELD_NUMBER: _ClassVar[int]
    vm_info: _aws_param_pb2.VMInfoResult
    ebs_volumes_vec: _containers.RepeatedCompositeFieldContainer[EBSVolume]
    db_info: _rds_params_pb2.DBInfo
    db_snapshot_info: _rds_params_pb2.SnapshotInfo
    cluster_db_snapshot_info: _rds_params_pb2.ClusterSnapshotInfo
    def __init__(self, vm_info: _Optional[_Union[_aws_param_pb2.VMInfoResult, _Mapping]] = ..., ebs_volumes_vec: _Optional[_Iterable[_Union[EBSVolume, _Mapping]]] = ..., db_info: _Optional[_Union[_rds_params_pb2.DBInfo, _Mapping]] = ..., db_snapshot_info: _Optional[_Union[_rds_params_pb2.SnapshotInfo, _Mapping]] = ..., cluster_db_snapshot_info: _Optional[_Union[_rds_params_pb2.ClusterSnapshotInfo, _Mapping]] = ...) -> None: ...

class SnapshotBlockInfo(_message.Message):
    __slots__ = ("delta_info", "snapshot_block_size", "next_token", "number_of_blocks", "volume_size_bytes")
    DELTA_INFO_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_BLOCK_SIZE_FIELD_NUMBER: _ClassVar[int]
    NEXT_TOKEN_FIELD_NUMBER: _ClassVar[int]
    NUMBER_OF_BLOCKS_FIELD_NUMBER: _ClassVar[int]
    VOLUME_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    delta_info: _cbt_delta_pb2.CBTDeltaInfo
    snapshot_block_size: int
    next_token: str
    number_of_blocks: int
    volume_size_bytes: int
    def __init__(self, delta_info: _Optional[_Union[_cbt_delta_pb2.CBTDeltaInfo, _Mapping]] = ..., snapshot_block_size: _Optional[int] = ..., next_token: _Optional[str] = ..., number_of_blocks: _Optional[int] = ..., volume_size_bytes: _Optional[int] = ...) -> None: ...

class SnapshotInfo(_message.Message):
    __slots__ = ("job_instance_id", "attempt_num", "server_vm_info", "take_iam_permit", "take_account_permit", "take_separate_sub_task_permit", "status", "ebs_volumes_vec", "snapshot_blocks_info_vec", "sub_tasks_vec", "error", "snapshot_deletion_error", "quiesced", "sub_file_size_mb", "aws_ami_id", "release_master_source_backup_entity_lock", "use_ebs_diff_api", "export_status", "converter_instance_id", "export_ebs_volume_disk_key", "original_root_volume_id")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kStarted: _ClassVar[SnapshotInfo.Status]
        kVMInfoFetched: _ClassVar[SnapshotInfo.Status]
        kCreateSnapshotInitialized: _ClassVar[SnapshotInfo.Status]
        kSubTasksCreated: _ClassVar[SnapshotInfo.Status]
        kSetupFilesFinished: _ClassVar[SnapshotInfo.Status]
        kSnapshotComplete: _ClassVar[SnapshotInfo.Status]
        kVMExported: _ClassVar[SnapshotInfo.Status]
        kDeltaBlocksFetched: _ClassVar[SnapshotInfo.Status]
        kSubTasksFinished: _ClassVar[SnapshotInfo.Status]
        kEndBackupFinished: _ClassVar[SnapshotInfo.Status]
    kStarted: SnapshotInfo.Status
    kVMInfoFetched: SnapshotInfo.Status
    kCreateSnapshotInitialized: SnapshotInfo.Status
    kSubTasksCreated: SnapshotInfo.Status
    kSetupFilesFinished: SnapshotInfo.Status
    kSnapshotComplete: SnapshotInfo.Status
    kVMExported: SnapshotInfo.Status
    kDeltaBlocksFetched: SnapshotInfo.Status
    kSubTasksFinished: SnapshotInfo.Status
    kEndBackupFinished: SnapshotInfo.Status
    class ExportStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kExportTaskStarted: _ClassVar[SnapshotInfo.ExportStatus]
        kPermitGranted: _ClassVar[SnapshotInfo.ExportStatus]
        kConverterVMCreated: _ClassVar[SnapshotInfo.ExportStatus]
        kEBSVolumeAttached: _ClassVar[SnapshotInfo.ExportStatus]
        kEBSVolumePrepared: _ClassVar[SnapshotInfo.ExportStatus]
        kEBSVolumeDetached: _ClassVar[SnapshotInfo.ExportStatus]
        kConverterVMTerminated: _ClassVar[SnapshotInfo.ExportStatus]
        kExportTaskFinished: _ClassVar[SnapshotInfo.ExportStatus]
    kExportTaskStarted: SnapshotInfo.ExportStatus
    kPermitGranted: SnapshotInfo.ExportStatus
    kConverterVMCreated: SnapshotInfo.ExportStatus
    kEBSVolumeAttached: SnapshotInfo.ExportStatus
    kEBSVolumePrepared: SnapshotInfo.ExportStatus
    kEBSVolumeDetached: SnapshotInfo.ExportStatus
    kConverterVMTerminated: SnapshotInfo.ExportStatus
    kExportTaskFinished: SnapshotInfo.ExportStatus
    AWS_SNAPSHOT_INFO_FIELD_NUMBER: _ClassVar[int]
    aws_snapshot_info: _descriptor.FieldDescriptor
    JOB_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    ATTEMPT_NUM_FIELD_NUMBER: _ClassVar[int]
    SERVER_VM_INFO_FIELD_NUMBER: _ClassVar[int]
    TAKE_IAM_PERMIT_FIELD_NUMBER: _ClassVar[int]
    TAKE_ACCOUNT_PERMIT_FIELD_NUMBER: _ClassVar[int]
    TAKE_SEPARATE_SUB_TASK_PERMIT_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    EBS_VOLUMES_VEC_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_BLOCKS_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    SUB_TASKS_VEC_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_DELETION_ERROR_FIELD_NUMBER: _ClassVar[int]
    QUIESCED_FIELD_NUMBER: _ClassVar[int]
    SUB_FILE_SIZE_MB_FIELD_NUMBER: _ClassVar[int]
    AWS_AMI_ID_FIELD_NUMBER: _ClassVar[int]
    RELEASE_MASTER_SOURCE_BACKUP_ENTITY_LOCK_FIELD_NUMBER: _ClassVar[int]
    USE_EBS_DIFF_API_FIELD_NUMBER: _ClassVar[int]
    EXPORT_STATUS_FIELD_NUMBER: _ClassVar[int]
    CONVERTER_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    EXPORT_EBS_VOLUME_DISK_KEY_FIELD_NUMBER: _ClassVar[int]
    ORIGINAL_ROOT_VOLUME_ID_FIELD_NUMBER: _ClassVar[int]
    job_instance_id: int
    attempt_num: int
    server_vm_info: _aws_param_pb2.VMInfoResult
    take_iam_permit: bool
    take_account_permit: bool
    take_separate_sub_task_permit: bool
    status: SnapshotInfo.Status
    ebs_volumes_vec: _containers.RepeatedCompositeFieldContainer[EBSVolume]
    snapshot_blocks_info_vec: _containers.RepeatedCompositeFieldContainer[SnapshotBlockInfo]
    sub_tasks_vec: _containers.RepeatedCompositeFieldContainer[_sub_task_pb2.SubTaskInfo]
    error: _error_pb2.ErrorProto
    snapshot_deletion_error: _containers.RepeatedCompositeFieldContainer[_error_pb2.ErrorProto]
    quiesced: bool
    sub_file_size_mb: int
    aws_ami_id: str
    release_master_source_backup_entity_lock: bool
    use_ebs_diff_api: bool
    export_status: SnapshotInfo.ExportStatus
    converter_instance_id: str
    export_ebs_volume_disk_key: int
    original_root_volume_id: str
    def __init__(self, job_instance_id: _Optional[int] = ..., attempt_num: _Optional[int] = ..., server_vm_info: _Optional[_Union[_aws_param_pb2.VMInfoResult, _Mapping]] = ..., take_iam_permit: bool = ..., take_account_permit: bool = ..., take_separate_sub_task_permit: bool = ..., status: _Optional[_Union[SnapshotInfo.Status, str]] = ..., ebs_volumes_vec: _Optional[_Iterable[_Union[EBSVolume, _Mapping]]] = ..., snapshot_blocks_info_vec: _Optional[_Iterable[_Union[SnapshotBlockInfo, _Mapping]]] = ..., sub_tasks_vec: _Optional[_Iterable[_Union[_sub_task_pb2.SubTaskInfo, _Mapping]]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., snapshot_deletion_error: _Optional[_Iterable[_Union[_error_pb2.ErrorProto, _Mapping]]] = ..., quiesced: bool = ..., sub_file_size_mb: _Optional[int] = ..., aws_ami_id: _Optional[str] = ..., release_master_source_backup_entity_lock: bool = ..., use_ebs_diff_api: bool = ..., export_status: _Optional[_Union[SnapshotInfo.ExportStatus, str]] = ..., converter_instance_id: _Optional[str] = ..., export_ebs_volume_disk_key: _Optional[int] = ..., original_root_volume_id: _Optional[str] = ...) -> None: ...

class RDSSnapshotInfo(_message.Message):
    __slots__ = ("job_instance_id", "attempt_num", "server_db_info", "status", "db_snapshot_info", "error", "snapshot_deletion_error", "take_account_permit", "cluster_db_snapshot_info")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kStarted: _ClassVar[RDSSnapshotInfo.Status]
        kDBInfoFetched: _ClassVar[RDSSnapshotInfo.Status]
        kSnapshotCreated: _ClassVar[RDSSnapshotInfo.Status]
        kSetupFilesFinished: _ClassVar[RDSSnapshotInfo.Status]
        kSnapshotComplete: _ClassVar[RDSSnapshotInfo.Status]
        kEndBackupFinished: _ClassVar[RDSSnapshotInfo.Status]
    kStarted: RDSSnapshotInfo.Status
    kDBInfoFetched: RDSSnapshotInfo.Status
    kSnapshotCreated: RDSSnapshotInfo.Status
    kSetupFilesFinished: RDSSnapshotInfo.Status
    kSnapshotComplete: RDSSnapshotInfo.Status
    kEndBackupFinished: RDSSnapshotInfo.Status
    RDS_SNAPSHOT_INFO_FIELD_NUMBER: _ClassVar[int]
    rds_snapshot_info: _descriptor.FieldDescriptor
    JOB_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    ATTEMPT_NUM_FIELD_NUMBER: _ClassVar[int]
    SERVER_DB_INFO_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    DB_SNAPSHOT_INFO_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_DELETION_ERROR_FIELD_NUMBER: _ClassVar[int]
    TAKE_ACCOUNT_PERMIT_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_DB_SNAPSHOT_INFO_FIELD_NUMBER: _ClassVar[int]
    job_instance_id: int
    attempt_num: int
    server_db_info: _rds_params_pb2.DBInfo
    status: RDSSnapshotInfo.Status
    db_snapshot_info: _rds_params_pb2.SnapshotInfo
    error: _error_pb2.ErrorProto
    snapshot_deletion_error: _containers.RepeatedCompositeFieldContainer[_error_pb2.ErrorProto]
    take_account_permit: bool
    cluster_db_snapshot_info: _rds_params_pb2.ClusterSnapshotInfo
    def __init__(self, job_instance_id: _Optional[int] = ..., attempt_num: _Optional[int] = ..., server_db_info: _Optional[_Union[_rds_params_pb2.DBInfo, _Mapping]] = ..., status: _Optional[_Union[RDSSnapshotInfo.Status, str]] = ..., db_snapshot_info: _Optional[_Union[_rds_params_pb2.SnapshotInfo, _Mapping]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., snapshot_deletion_error: _Optional[_Iterable[_Union[_error_pb2.ErrorProto, _Mapping]]] = ..., take_account_permit: bool = ..., cluster_db_snapshot_info: _Optional[_Union[_rds_params_pb2.ClusterSnapshotInfo, _Mapping]] = ...) -> None: ...

class RestoreEnvironmentInfo(_message.Message):
    __slots__ = ("vm_info", "cohesity_agent_installation_state_proto", "status", "should_uninstall_agent")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kVMInfoFetched: _ClassVar[RestoreEnvironmentInfo.Status]
        kCohesityAgentInstalled: _ClassVar[RestoreEnvironmentInfo.Status]
    kVMInfoFetched: RestoreEnvironmentInfo.Status
    kCohesityAgentInstalled: RestoreEnvironmentInfo.Status
    RESTORE_ENV_INFO_FIELD_NUMBER: _ClassVar[int]
    restore_env_info: _descriptor.FieldDescriptor
    VM_INFO_FIELD_NUMBER: _ClassVar[int]
    COHESITY_AGENT_INSTALLATION_STATE_PROTO_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SHOULD_UNINSTALL_AGENT_FIELD_NUMBER: _ClassVar[int]
    vm_info: _aws_param_pb2.VMInfoResult
    cohesity_agent_installation_state_proto: _cloud_pb2_1.CohesityAgentInstallationStateProto
    status: RestoreEnvironmentInfo.Status
    should_uninstall_agent: bool
    def __init__(self, vm_info: _Optional[_Union[_aws_param_pb2.VMInfoResult, _Mapping]] = ..., cohesity_agent_installation_state_proto: _Optional[_Union[_cloud_pb2_1.CohesityAgentInstallationStateProto, _Mapping]] = ..., status: _Optional[_Union[RestoreEnvironmentInfo.Status, str]] = ..., should_uninstall_agent: bool = ...) -> None: ...

class CohesityAgentInstallationEnvironmentInfo(_message.Message):
    __slots__ = ("security_group_id",)
    INSTALLATION_ENV_INFO_FIELD_NUMBER: _ClassVar[int]
    installation_env_info: _descriptor.FieldDescriptor
    SECURITY_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    security_group_id: str
    def __init__(self, security_group_id: _Optional[str] = ...) -> None: ...

class AwsSubTaskInfo(_message.Message):
    __slots__ = ("total_blocks_copied",)
    AWS_SUB_TASK_INFO_FIELD_NUMBER: _ClassVar[int]
    aws_sub_task_info: _descriptor.FieldDescriptor
    TOTAL_BLOCKS_COPIED_FIELD_NUMBER: _ClassVar[int]
    total_blocks_copied: int
    def __init__(self, total_blocks_copied: _Optional[int] = ...) -> None: ...
