from qa.perfHarness.base import error_pb2 as _error_pb2
from qa.perfHarness.base import harness_spec_pb2 as _harness_spec_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class VMInfo(_message.Message):
    __slots__ = ("moref_id", "name", "ip_addr", "os_type")
    MOREF_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    IP_ADDR_FIELD_NUMBER: _ClassVar[int]
    OS_TYPE_FIELD_NUMBER: _ClassVar[int]
    moref_id: str
    name: str
    ip_addr: str
    os_type: _harness_spec_pb2.OSType
    def __init__(self, moref_id: _Optional[str] = ..., name: _Optional[str] = ..., ip_addr: _Optional[str] = ..., os_type: _Optional[_Union[_harness_spec_pb2.OSType, str]] = ...) -> None: ...

class VMwareSetupState(_message.Message):
    __slots__ = ("error", "setup_start_time_usecs", "setup_end_time_usecs", "teardown_start_time_usecs", "teardown_end_time_usecs", "vm_info_vec", "state_cleaned_up")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    SETUP_START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    SETUP_END_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    TEARDOWN_START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    TEARDOWN_END_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    VM_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    STATE_CLEANED_UP_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    setup_start_time_usecs: int
    setup_end_time_usecs: int
    teardown_start_time_usecs: int
    teardown_end_time_usecs: int
    vm_info_vec: _containers.RepeatedCompositeFieldContainer[VMInfo]
    state_cleaned_up: bool
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., setup_start_time_usecs: _Optional[int] = ..., setup_end_time_usecs: _Optional[int] = ..., teardown_start_time_usecs: _Optional[int] = ..., teardown_end_time_usecs: _Optional[int] = ..., vm_info_vec: _Optional[_Iterable[_Union[VMInfo, _Mapping]]] = ..., state_cleaned_up: bool = ...) -> None: ...

class CohesitySetupState(_message.Message):
    __slots__ = ("error", "setup_start_time_usecs", "setup_end_time_usecs", "teardown_start_time_usecs", "teardown_end_time_usecs", "vcenter_entity_id", "viewbox_id_vec", "view_id_vec", "backup_job_id_vec", "state_cleaned_up")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    SETUP_START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    SETUP_END_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    TEARDOWN_START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    TEARDOWN_END_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    VCENTER_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    VIEWBOX_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    VIEW_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    BACKUP_JOB_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    STATE_CLEANED_UP_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    setup_start_time_usecs: int
    setup_end_time_usecs: int
    teardown_start_time_usecs: int
    teardown_end_time_usecs: int
    vcenter_entity_id: int
    viewbox_id_vec: _containers.RepeatedScalarFieldContainer[int]
    view_id_vec: _containers.RepeatedScalarFieldContainer[int]
    backup_job_id_vec: _containers.RepeatedScalarFieldContainer[int]
    state_cleaned_up: bool
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., setup_start_time_usecs: _Optional[int] = ..., setup_end_time_usecs: _Optional[int] = ..., teardown_start_time_usecs: _Optional[int] = ..., teardown_end_time_usecs: _Optional[int] = ..., vcenter_entity_id: _Optional[int] = ..., viewbox_id_vec: _Optional[_Iterable[int]] = ..., view_id_vec: _Optional[_Iterable[int]] = ..., backup_job_id_vec: _Optional[_Iterable[int]] = ..., state_cleaned_up: bool = ...) -> None: ...

class GuestManagerState(_message.Message):
    __slots__ = ("error", "prep_disk_start_time_usecs", "prep_disk_end_time_usecs", "guest_working_dir", "state", "workload_cleaned_up")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kManagerInitialized: _ClassVar[GuestManagerState.State]
        kDiskPrepped: _ClassVar[GuestManagerState.State]
        kWorkLoadRunning: _ClassVar[GuestManagerState.State]
        kWorkLoadStopped: _ClassVar[GuestManagerState.State]
    kManagerInitialized: GuestManagerState.State
    kDiskPrepped: GuestManagerState.State
    kWorkLoadRunning: GuestManagerState.State
    kWorkLoadStopped: GuestManagerState.State
    ERROR_FIELD_NUMBER: _ClassVar[int]
    PREP_DISK_START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    PREP_DISK_END_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    GUEST_WORKING_DIR_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    WORKLOAD_CLEANED_UP_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    prep_disk_start_time_usecs: int
    prep_disk_end_time_usecs: int
    guest_working_dir: str
    state: GuestManagerState.State
    workload_cleaned_up: bool
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., prep_disk_start_time_usecs: _Optional[int] = ..., prep_disk_end_time_usecs: _Optional[int] = ..., guest_working_dir: _Optional[str] = ..., state: _Optional[_Union[GuestManagerState.State, str]] = ..., workload_cleaned_up: bool = ...) -> None: ...

class HarnessState(_message.Message):
    __slots__ = ("creation_time_usecs", "error", "vmware_setup_state", "cohesity_setup_state", "guest_manager_state")
    CREATION_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    VMWARE_SETUP_STATE_FIELD_NUMBER: _ClassVar[int]
    COHESITY_SETUP_STATE_FIELD_NUMBER: _ClassVar[int]
    GUEST_MANAGER_STATE_FIELD_NUMBER: _ClassVar[int]
    creation_time_usecs: int
    error: _error_pb2.ErrorProto
    vmware_setup_state: VMwareSetupState
    cohesity_setup_state: CohesitySetupState
    guest_manager_state: GuestManagerState
    def __init__(self, creation_time_usecs: _Optional[int] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., vmware_setup_state: _Optional[_Union[VMwareSetupState, _Mapping]] = ..., cohesity_setup_state: _Optional[_Union[CohesitySetupState, _Mapping]] = ..., guest_manager_state: _Optional[_Union[GuestManagerState, _Mapping]] = ...) -> None: ...
