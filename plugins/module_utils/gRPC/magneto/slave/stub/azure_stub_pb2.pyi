from magneto.connectors.azure import azure_pb2 as _azure_pb2
from magneto.connectors.azure import azure_param_pb2 as _azure_param_pb2
from magneto.slave.stub import stub_pb2 as _stub_pb2
from magneto.slave.stub import bridge_updates_pb2 as _bridge_updates_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SetupVMFilesUpdateArg(_message.Message):
    __slots__ = ("virtual_disks_vec",)
    VIRTUAL_DISKS_VEC_FIELD_NUMBER: _ClassVar[int]
    virtual_disks_vec: _containers.RepeatedCompositeFieldContainer[_azure_pb2.VirtualDisk]
    def __init__(self, virtual_disks_vec: _Optional[_Iterable[_Union[_azure_pb2.VirtualDisk, _Mapping]]] = ...) -> None: ...

class QueryPageRangeUpdateArg(_message.Message):
    __slots__ = ("page_ranges_result",)
    PAGE_RANGES_RESULT_FIELD_NUMBER: _ClassVar[int]
    page_ranges_result: _azure_param_pb2.GetPageRangesResult
    def __init__(self, page_ranges_result: _Optional[_Union[_azure_param_pb2.GetPageRangesResult, _Mapping]] = ...) -> None: ...

class AzureActionUpdateArg(_message.Message):
    __slots__ = ("type", "setup_vm_files_update_arg", "backup_disk_update_arg", "vm_config", "query_page_range_update_arg")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kCreateBlobsUpdate: _ClassVar[AzureActionUpdateArg.Type]
        kCopyDiskAreaUpdate: _ClassVar[AzureActionUpdateArg.Type]
        kEndRestoreUpdate: _ClassVar[AzureActionUpdateArg.Type]
        kDeleteBlobsUpdate: _ClassVar[AzureActionUpdateArg.Type]
        kPrepareVMBackupUpdate: _ClassVar[AzureActionUpdateArg.Type]
        kSetupVMFilesUpdate: _ClassVar[AzureActionUpdateArg.Type]
        kBackupVMDiskUpdate: _ClassVar[AzureActionUpdateArg.Type]
        kEndSubTaskUpdate: _ClassVar[AzureActionUpdateArg.Type]
        kEndVMBackupUpdate: _ClassVar[AzureActionUpdateArg.Type]
        kFetchVMInfoUpdate: _ClassVar[AzureActionUpdateArg.Type]
        kQueryPageRangeUpdate: _ClassVar[AzureActionUpdateArg.Type]
    kCreateBlobsUpdate: AzureActionUpdateArg.Type
    kCopyDiskAreaUpdate: AzureActionUpdateArg.Type
    kEndRestoreUpdate: AzureActionUpdateArg.Type
    kDeleteBlobsUpdate: AzureActionUpdateArg.Type
    kPrepareVMBackupUpdate: AzureActionUpdateArg.Type
    kSetupVMFilesUpdate: AzureActionUpdateArg.Type
    kBackupVMDiskUpdate: AzureActionUpdateArg.Type
    kEndSubTaskUpdate: AzureActionUpdateArg.Type
    kEndVMBackupUpdate: AzureActionUpdateArg.Type
    kFetchVMInfoUpdate: AzureActionUpdateArg.Type
    kQueryPageRangeUpdate: AzureActionUpdateArg.Type
    AZURE_ACTION_UPDATE_ARG_FIELD_NUMBER: _ClassVar[int]
    azure_action_update_arg: _descriptor.FieldDescriptor
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SETUP_VM_FILES_UPDATE_ARG_FIELD_NUMBER: _ClassVar[int]
    BACKUP_DISK_UPDATE_ARG_FIELD_NUMBER: _ClassVar[int]
    VM_CONFIG_FIELD_NUMBER: _ClassVar[int]
    QUERY_PAGE_RANGE_UPDATE_ARG_FIELD_NUMBER: _ClassVar[int]
    type: AzureActionUpdateArg.Type
    setup_vm_files_update_arg: SetupVMFilesUpdateArg
    backup_disk_update_arg: _stub_pb2.BackupDiskUpdateArg
    vm_config: _azure_pb2.VMConfig
    query_page_range_update_arg: QueryPageRangeUpdateArg
    def __init__(self, type: _Optional[_Union[AzureActionUpdateArg.Type, str]] = ..., setup_vm_files_update_arg: _Optional[_Union[SetupVMFilesUpdateArg, _Mapping]] = ..., backup_disk_update_arg: _Optional[_Union[_stub_pb2.BackupDiskUpdateArg, _Mapping]] = ..., vm_config: _Optional[_Union[_azure_pb2.VMConfig, _Mapping]] = ..., query_page_range_update_arg: _Optional[_Union[QueryPageRangeUpdateArg, _Mapping]] = ...) -> None: ...
