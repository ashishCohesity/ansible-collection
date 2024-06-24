from bridge.magneto.base import magneto_actions_pb2 as _magneto_actions_pb2
from bridge.vault.base import vault_pb2 as _vault_pb2
from configs import cluster_config_pb2 as _cluster_config_pb2
from magneto.base import disk_pb2 as _disk_pb2
from magneto.base.entities import aws_pb2 as _aws_pb2
from magneto.base.entities import vmware_pb2 as _vmware_pb2
from magneto.base import entity_pb2 as _entity_pb2
from magneto.connectors.aws import aws_pb2 as _aws_pb2_1
from nexus.cloud.base import credentials_pb2 as _credentials_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BackupAWSVMArg(_message.Message):
    __slots__ = ("base", "type", "root_entity", "vm_entity", "vm_config", "exported_root_volume", "exported_disk_file_name", "use_diff_api")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kPrepareBackup: _ClassVar[BackupAWSVMArg.Type]
        kSetupFiles: _ClassVar[BackupAWSVMArg.Type]
        kBackupDisk: _ClassVar[BackupAWSVMArg.Type]
        kEndSubTask: _ClassVar[BackupAWSVMArg.Type]
        kEndBackup: _ClassVar[BackupAWSVMArg.Type]
    kPrepareBackup: BackupAWSVMArg.Type
    kSetupFiles: BackupAWSVMArg.Type
    kBackupDisk: BackupAWSVMArg.Type
    kEndSubTask: BackupAWSVMArg.Type
    kEndBackup: BackupAWSVMArg.Type
    BASE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ROOT_ENTITY_FIELD_NUMBER: _ClassVar[int]
    VM_ENTITY_FIELD_NUMBER: _ClassVar[int]
    VM_CONFIG_FIELD_NUMBER: _ClassVar[int]
    EXPORTED_ROOT_VOLUME_FIELD_NUMBER: _ClassVar[int]
    EXPORTED_DISK_FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    USE_DIFF_API_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_actions_pb2.BackupBaseArg
    type: BackupAWSVMArg.Type
    root_entity: _aws_pb2.Entity
    vm_entity: _aws_pb2.Entity
    vm_config: _aws_pb2_1.VMConfig
    exported_root_volume: bool
    exported_disk_file_name: str
    use_diff_api: bool
    def __init__(self, base: _Optional[_Union[_magneto_actions_pb2.BackupBaseArg, _Mapping]] = ..., type: _Optional[_Union[BackupAWSVMArg.Type, str]] = ..., root_entity: _Optional[_Union[_aws_pb2.Entity, _Mapping]] = ..., vm_entity: _Optional[_Union[_aws_pb2.Entity, _Mapping]] = ..., vm_config: _Optional[_Union[_aws_pb2_1.VMConfig, _Mapping]] = ..., exported_root_volume: bool = ..., exported_disk_file_name: _Optional[str] = ..., use_diff_api: bool = ...) -> None: ...

class RestoreVMsArg(_message.Message):
    __slots__ = ("base", "type", "vm_restore_infos", "view_box_id", "destination_view_name", "s3_bucket", "credentials", "aws_region", "disk_info", "use_ebs_write_api")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kRestoreDisk: _ClassVar[RestoreVMsArg.Type]
        kCreateS3Objects: _ClassVar[RestoreVMsArg.Type]
        kCreateEBSVolumes: _ClassVar[RestoreVMsArg.Type]
        kCopyDiskArea: _ClassVar[RestoreVMsArg.Type]
        kFinalizeS3Objects: _ClassVar[RestoreVMsArg.Type]
        kEndRestore: _ClassVar[RestoreVMsArg.Type]
        kDeleteAWSEntities: _ClassVar[RestoreVMsArg.Type]
        kFetchVMsInfo: _ClassVar[RestoreVMsArg.Type]
        kEndSubTask: _ClassVar[RestoreVMsArg.Type]
    kRestoreDisk: RestoreVMsArg.Type
    kCreateS3Objects: RestoreVMsArg.Type
    kCreateEBSVolumes: RestoreVMsArg.Type
    kCopyDiskArea: RestoreVMsArg.Type
    kFinalizeS3Objects: RestoreVMsArg.Type
    kEndRestore: RestoreVMsArg.Type
    kDeleteAWSEntities: RestoreVMsArg.Type
    kFetchVMsInfo: RestoreVMsArg.Type
    kEndSubTask: RestoreVMsArg.Type
    class VMRestoreInfo(_message.Message):
        __slots__ = ("vm_entity", "entity", "aws_entity_infos", "snapshot_relative_dir_path")
        class AWSEntityInfo(_message.Message):
            __slots__ = ("name", "vm_disk_relative_filepath", "size", "disk_info", "area", "vm_disk_s3_upload_context", "part_num", "is_s3_object")
            NAME_FIELD_NUMBER: _ClassVar[int]
            VM_DISK_RELATIVE_FILEPATH_FIELD_NUMBER: _ClassVar[int]
            SIZE_FIELD_NUMBER: _ClassVar[int]
            DISK_INFO_FIELD_NUMBER: _ClassVar[int]
            AREA_FIELD_NUMBER: _ClassVar[int]
            VM_DISK_S3_UPLOAD_CONTEXT_FIELD_NUMBER: _ClassVar[int]
            PART_NUM_FIELD_NUMBER: _ClassVar[int]
            IS_S3_OBJECT_FIELD_NUMBER: _ClassVar[int]
            name: str
            vm_disk_relative_filepath: str
            size: int
            disk_info: _aws_pb2_1.CloudDeployEntityInfo.DiskInfo
            area: _disk_pb2.DiskAreaProto
            vm_disk_s3_upload_context: _vault_pb2.VaultUploadContextProto
            part_num: int
            is_s3_object: bool
            def __init__(self, name: _Optional[str] = ..., vm_disk_relative_filepath: _Optional[str] = ..., size: _Optional[int] = ..., disk_info: _Optional[_Union[_aws_pb2_1.CloudDeployEntityInfo.DiskInfo, _Mapping]] = ..., area: _Optional[_Union[_disk_pb2.DiskAreaProto, _Mapping]] = ..., vm_disk_s3_upload_context: _Optional[_Union[_vault_pb2.VaultUploadContextProto, _Mapping]] = ..., part_num: _Optional[int] = ..., is_s3_object: bool = ...) -> None: ...
        VM_ENTITY_FIELD_NUMBER: _ClassVar[int]
        ENTITY_FIELD_NUMBER: _ClassVar[int]
        AWS_ENTITY_INFOS_FIELD_NUMBER: _ClassVar[int]
        SNAPSHOT_RELATIVE_DIR_PATH_FIELD_NUMBER: _ClassVar[int]
        vm_entity: _vmware_pb2.Entity
        entity: _entity_pb2.EntityProto
        aws_entity_infos: _containers.RepeatedCompositeFieldContainer[RestoreVMsArg.VMRestoreInfo.AWSEntityInfo]
        snapshot_relative_dir_path: str
        def __init__(self, vm_entity: _Optional[_Union[_vmware_pb2.Entity, _Mapping]] = ..., entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., aws_entity_infos: _Optional[_Iterable[_Union[RestoreVMsArg.VMRestoreInfo.AWSEntityInfo, _Mapping]]] = ..., snapshot_relative_dir_path: _Optional[str] = ...) -> None: ...
    BASE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    VM_RESTORE_INFOS_FIELD_NUMBER: _ClassVar[int]
    VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    S3_BUCKET_FIELD_NUMBER: _ClassVar[int]
    CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    AWS_REGION_FIELD_NUMBER: _ClassVar[int]
    DISK_INFO_FIELD_NUMBER: _ClassVar[int]
    USE_EBS_WRITE_API_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_actions_pb2.RestoreBaseArg
    type: RestoreVMsArg.Type
    vm_restore_infos: _containers.RepeatedCompositeFieldContainer[RestoreVMsArg.VMRestoreInfo]
    view_box_id: int
    destination_view_name: str
    s3_bucket: str
    credentials: _credentials_pb2.AwsCredentials
    aws_region: str
    disk_info: _aws_pb2_1.CloudDeployEntityInfo.DiskInfo
    use_ebs_write_api: bool
    def __init__(self, base: _Optional[_Union[_magneto_actions_pb2.RestoreBaseArg, _Mapping]] = ..., type: _Optional[_Union[RestoreVMsArg.Type, str]] = ..., vm_restore_infos: _Optional[_Iterable[_Union[RestoreVMsArg.VMRestoreInfo, _Mapping]]] = ..., view_box_id: _Optional[int] = ..., destination_view_name: _Optional[str] = ..., s3_bucket: _Optional[str] = ..., credentials: _Optional[_Union[_credentials_pb2.AwsCredentials, _Mapping]] = ..., aws_region: _Optional[str] = ..., disk_info: _Optional[_Union[_aws_pb2_1.CloudDeployEntityInfo.DiskInfo, _Mapping]] = ..., use_ebs_write_api: bool = ...) -> None: ...

class DownloadDiskArg(_message.Message):
    __slots__ = ("s3_bucket", "s3_object_name", "object_area_info", "credentials", "aws_region", "view_box_id", "target_view_name", "target_file_rel_path")
    S3_BUCKET_FIELD_NUMBER: _ClassVar[int]
    S3_OBJECT_NAME_FIELD_NUMBER: _ClassVar[int]
    OBJECT_AREA_INFO_FIELD_NUMBER: _ClassVar[int]
    CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    AWS_REGION_FIELD_NUMBER: _ClassVar[int]
    VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    TARGET_FILE_REL_PATH_FIELD_NUMBER: _ClassVar[int]
    s3_bucket: str
    s3_object_name: str
    object_area_info: _disk_pb2.DiskAreaProto
    credentials: _credentials_pb2.AwsCredentials
    aws_region: str
    view_box_id: int
    target_view_name: str
    target_file_rel_path: str
    def __init__(self, s3_bucket: _Optional[str] = ..., s3_object_name: _Optional[str] = ..., object_area_info: _Optional[_Union[_disk_pb2.DiskAreaProto, _Mapping]] = ..., credentials: _Optional[_Union[_credentials_pb2.AwsCredentials, _Mapping]] = ..., aws_region: _Optional[str] = ..., view_box_id: _Optional[int] = ..., target_view_name: _Optional[str] = ..., target_file_rel_path: _Optional[str] = ...) -> None: ...

class CopyVolumeArg(_message.Message):
    __slots__ = ("view_box_id", "view_name", "src_file_rel_path", "target_file_rel_path", "object_area_info")
    VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    SRC_FILE_REL_PATH_FIELD_NUMBER: _ClassVar[int]
    TARGET_FILE_REL_PATH_FIELD_NUMBER: _ClassVar[int]
    OBJECT_AREA_INFO_FIELD_NUMBER: _ClassVar[int]
    view_box_id: int
    view_name: str
    src_file_rel_path: str
    target_file_rel_path: str
    object_area_info: _disk_pb2.DiskAreaProto
    def __init__(self, view_box_id: _Optional[int] = ..., view_name: _Optional[str] = ..., src_file_rel_path: _Optional[str] = ..., target_file_rel_path: _Optional[str] = ..., object_area_info: _Optional[_Union[_disk_pb2.DiskAreaProto, _Mapping]] = ...) -> None: ...

class AWSActionArg(_message.Message):
    __slots__ = ("task_id", "sub_task_id", "backup_vm_arg", "restore_vms_arg", "cancel_task_arg", "download_disk_arg", "copy_volume_arg", "vault_type")
    AWS_ACTION_ARG_FIELD_NUMBER: _ClassVar[int]
    aws_action_arg: _descriptor.FieldDescriptor
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    SUB_TASK_ID_FIELD_NUMBER: _ClassVar[int]
    BACKUP_VM_ARG_FIELD_NUMBER: _ClassVar[int]
    RESTORE_VMS_ARG_FIELD_NUMBER: _ClassVar[int]
    CANCEL_TASK_ARG_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_DISK_ARG_FIELD_NUMBER: _ClassVar[int]
    COPY_VOLUME_ARG_FIELD_NUMBER: _ClassVar[int]
    VAULT_TYPE_FIELD_NUMBER: _ClassVar[int]
    task_id: int
    sub_task_id: int
    backup_vm_arg: BackupAWSVMArg
    restore_vms_arg: RestoreVMsArg
    cancel_task_arg: _magneto_actions_pb2.CancelTaskArg
    download_disk_arg: DownloadDiskArg
    copy_volume_arg: CopyVolumeArg
    vault_type: _cluster_config_pb2.ClusterConfigProto.Vault.Type
    def __init__(self, task_id: _Optional[int] = ..., sub_task_id: _Optional[int] = ..., backup_vm_arg: _Optional[_Union[BackupAWSVMArg, _Mapping]] = ..., restore_vms_arg: _Optional[_Union[RestoreVMsArg, _Mapping]] = ..., cancel_task_arg: _Optional[_Union[_magneto_actions_pb2.CancelTaskArg, _Mapping]] = ..., download_disk_arg: _Optional[_Union[DownloadDiskArg, _Mapping]] = ..., copy_volume_arg: _Optional[_Union[CopyVolumeArg, _Mapping]] = ..., vault_type: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.Vault.Type, str]] = ...) -> None: ...
