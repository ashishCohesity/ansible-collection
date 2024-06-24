from qa.regression.testcases.backup_tests.base import vm_backup_test_spec_pb2 as _vm_backup_test_spec_pb2
from qa.regression.testcases.restore.base import restore_files_test_spec_pb2 as _restore_files_test_spec_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class VmBackupSuiteInfo(_message.Message):
    __slots__ = ("vm_backup_test_data", "restore_files_test_data_vec")
    VM_BACKUP_TEST_DATA_FIELD_NUMBER: _ClassVar[int]
    RESTORE_FILES_TEST_DATA_VEC_FIELD_NUMBER: _ClassVar[int]
    vm_backup_test_data: _vm_backup_test_spec_pb2.VmBackupInfo
    restore_files_test_data_vec: _containers.RepeatedCompositeFieldContainer[_restore_files_test_spec_pb2.RestoreFilesTestInfo]
    def __init__(self, vm_backup_test_data: _Optional[_Union[_vm_backup_test_spec_pb2.VmBackupInfo, _Mapping]] = ..., restore_files_test_data_vec: _Optional[_Iterable[_Union[_restore_files_test_spec_pb2.RestoreFilesTestInfo, _Mapping]]] = ...) -> None: ...

class VmBackupSuiteInfoVec(_message.Message):
    __slots__ = ("vm_backup_suite_data_vec",)
    VM_BACKUP_SUITE_DATA_VEC_FIELD_NUMBER: _ClassVar[int]
    vm_backup_suite_data_vec: _containers.RepeatedCompositeFieldContainer[VmBackupSuiteInfo]
    def __init__(self, vm_backup_suite_data_vec: _Optional[_Iterable[_Union[VmBackupSuiteInfo, _Mapping]]] = ...) -> None: ...
