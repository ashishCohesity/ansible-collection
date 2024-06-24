from bridge.vault.base import vault_pb2 as _vault_pb2
from magneto.connectors.aws import aws_pb2 as _aws_pb2
from magneto.slave.stub import stub_pb2 as _stub_pb2
from magneto.slave.stub import bridge_updates_pb2 as _bridge_updates_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SetupVMFilesUpdateArg(_message.Message):
    __slots__ = ("ebs_volumes_vec",)
    EBS_VOLUMES_VEC_FIELD_NUMBER: _ClassVar[int]
    ebs_volumes_vec: _containers.RepeatedCompositeFieldContainer[_aws_pb2.EBSVolume]
    def __init__(self, ebs_volumes_vec: _Optional[_Iterable[_Union[_aws_pb2.EBSVolume, _Mapping]]] = ...) -> None: ...

class EndVMBackupUpdateArg(_message.Message):
    __slots__ = ("closed_ebs_volumes_vec_DEPRECATED", "errored_ebs_volumes_vec")
    CLOSED_EBS_VOLUMES_VEC_DEPRECATED_FIELD_NUMBER: _ClassVar[int]
    ERRORED_EBS_VOLUMES_VEC_FIELD_NUMBER: _ClassVar[int]
    closed_ebs_volumes_vec_DEPRECATED: _containers.RepeatedCompositeFieldContainer[_aws_pb2.EBSVolume]
    errored_ebs_volumes_vec: _containers.RepeatedCompositeFieldContainer[_aws_pb2.EBSVolume]
    def __init__(self, closed_ebs_volumes_vec_DEPRECATED: _Optional[_Iterable[_Union[_aws_pb2.EBSVolume, _Mapping]]] = ..., errored_ebs_volumes_vec: _Optional[_Iterable[_Union[_aws_pb2.EBSVolume, _Mapping]]] = ...) -> None: ...

class EndVMRestoreUpdateArg(_message.Message):
    __slots__ = ("closed_ebs_volumes_vec",)
    CLOSED_EBS_VOLUMES_VEC_FIELD_NUMBER: _ClassVar[int]
    closed_ebs_volumes_vec: _containers.RepeatedCompositeFieldContainer[_aws_pb2.EBSVolume]
    def __init__(self, closed_ebs_volumes_vec: _Optional[_Iterable[_Union[_aws_pb2.EBSVolume, _Mapping]]] = ...) -> None: ...

class AWSActionUpdateArg(_message.Message):
    __slots__ = ("type", "vm_disk_s3_upload_context_vec", "setup_vm_files_update_arg", "backup_disk_update_arg", "restore_disk_update_arg", "end_vm_backup_update_arg", "end_vm_restore_update_arg", "vm_config")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kCreateS3ObjectsUpdate: _ClassVar[AWSActionUpdateArg.Type]
        kCreateEBSVolumesUpdate: _ClassVar[AWSActionUpdateArg.Type]
        kCopyDiskAreaUpdate: _ClassVar[AWSActionUpdateArg.Type]
        kFinalizeS3ObjectsUpdate: _ClassVar[AWSActionUpdateArg.Type]
        kEndRestoreUpdate: _ClassVar[AWSActionUpdateArg.Type]
        kDeleteAWSEntitiesUpdate: _ClassVar[AWSActionUpdateArg.Type]
        kDownloadDiskPortionUpdate: _ClassVar[AWSActionUpdateArg.Type]
        kConvertDiskUpdate: _ClassVar[AWSActionUpdateArg.Type]
        kCopyVolumeDataUpdate: _ClassVar[AWSActionUpdateArg.Type]
        kPrepareVMBackupUpdate: _ClassVar[AWSActionUpdateArg.Type]
        kSetupVMFilesUpdate: _ClassVar[AWSActionUpdateArg.Type]
        kBackupVMDiskUpdate: _ClassVar[AWSActionUpdateArg.Type]
        kRestoreVMDiskUpdate: _ClassVar[AWSActionUpdateArg.Type]
        kEndSubTaskUpdate: _ClassVar[AWSActionUpdateArg.Type]
        kFetchVMInfoUpdate: _ClassVar[AWSActionUpdateArg.Type]
        kEndVMBackupUpdate: _ClassVar[AWSActionUpdateArg.Type]
        kEndVMRestoreUpdate: _ClassVar[AWSActionUpdateArg.Type]
    kCreateS3ObjectsUpdate: AWSActionUpdateArg.Type
    kCreateEBSVolumesUpdate: AWSActionUpdateArg.Type
    kCopyDiskAreaUpdate: AWSActionUpdateArg.Type
    kFinalizeS3ObjectsUpdate: AWSActionUpdateArg.Type
    kEndRestoreUpdate: AWSActionUpdateArg.Type
    kDeleteAWSEntitiesUpdate: AWSActionUpdateArg.Type
    kDownloadDiskPortionUpdate: AWSActionUpdateArg.Type
    kConvertDiskUpdate: AWSActionUpdateArg.Type
    kCopyVolumeDataUpdate: AWSActionUpdateArg.Type
    kPrepareVMBackupUpdate: AWSActionUpdateArg.Type
    kSetupVMFilesUpdate: AWSActionUpdateArg.Type
    kBackupVMDiskUpdate: AWSActionUpdateArg.Type
    kRestoreVMDiskUpdate: AWSActionUpdateArg.Type
    kEndSubTaskUpdate: AWSActionUpdateArg.Type
    kFetchVMInfoUpdate: AWSActionUpdateArg.Type
    kEndVMBackupUpdate: AWSActionUpdateArg.Type
    kEndVMRestoreUpdate: AWSActionUpdateArg.Type
    AWS_ACTION_UPDATE_ARG_FIELD_NUMBER: _ClassVar[int]
    aws_action_update_arg: _descriptor.FieldDescriptor
    TYPE_FIELD_NUMBER: _ClassVar[int]
    VM_DISK_S3_UPLOAD_CONTEXT_VEC_FIELD_NUMBER: _ClassVar[int]
    SETUP_VM_FILES_UPDATE_ARG_FIELD_NUMBER: _ClassVar[int]
    BACKUP_DISK_UPDATE_ARG_FIELD_NUMBER: _ClassVar[int]
    RESTORE_DISK_UPDATE_ARG_FIELD_NUMBER: _ClassVar[int]
    END_VM_BACKUP_UPDATE_ARG_FIELD_NUMBER: _ClassVar[int]
    END_VM_RESTORE_UPDATE_ARG_FIELD_NUMBER: _ClassVar[int]
    VM_CONFIG_FIELD_NUMBER: _ClassVar[int]
    type: AWSActionUpdateArg.Type
    vm_disk_s3_upload_context_vec: _containers.RepeatedCompositeFieldContainer[_vault_pb2.VaultUploadContextProto]
    setup_vm_files_update_arg: SetupVMFilesUpdateArg
    backup_disk_update_arg: _stub_pb2.BackupDiskUpdateArg
    restore_disk_update_arg: _stub_pb2.RestoreDiskUpdateArg
    end_vm_backup_update_arg: EndVMBackupUpdateArg
    end_vm_restore_update_arg: EndVMRestoreUpdateArg
    vm_config: _aws_pb2.VMConfig
    def __init__(self, type: _Optional[_Union[AWSActionUpdateArg.Type, str]] = ..., vm_disk_s3_upload_context_vec: _Optional[_Iterable[_Union[_vault_pb2.VaultUploadContextProto, _Mapping]]] = ..., setup_vm_files_update_arg: _Optional[_Union[SetupVMFilesUpdateArg, _Mapping]] = ..., backup_disk_update_arg: _Optional[_Union[_stub_pb2.BackupDiskUpdateArg, _Mapping]] = ..., restore_disk_update_arg: _Optional[_Union[_stub_pb2.RestoreDiskUpdateArg, _Mapping]] = ..., end_vm_backup_update_arg: _Optional[_Union[EndVMBackupUpdateArg, _Mapping]] = ..., end_vm_restore_update_arg: _Optional[_Union[EndVMRestoreUpdateArg, _Mapping]] = ..., vm_config: _Optional[_Union[_aws_pb2.VMConfig, _Mapping]] = ...) -> None: ...
