from magneto.base import magneto_pb2 as _magneto_pb2
from magneto.base import env_params_pb2 as _env_params_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf.internal import python_message as _python_message
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CloudEntityCommonInfo(_message.Message):
    __slots__ = ("name", "id", "failed_over", "physical_entity_id")
    NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    FAILED_OVER_FIELD_NUMBER: _ClassVar[int]
    PHYSICAL_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    id: str
    failed_over: bool
    physical_entity_id: int
    def __init__(self, name: _Optional[str] = ..., id: _Optional[str] = ..., failed_over: bool = ..., physical_entity_id: _Optional[int] = ...) -> None: ...

class CloneTaskVolumeBlobInfo(_message.Message):
    __slots__ = ("volume_guid", "resume_offset")
    VOLUME_GUID_FIELD_NUMBER: _ClassVar[int]
    RESUME_OFFSET_FIELD_NUMBER: _ClassVar[int]
    volume_guid: str
    resume_offset: int
    def __init__(self, volume_guid: _Optional[str] = ..., resume_offset: _Optional[int] = ...) -> None: ...

class VMConversionInfo(_message.Message):
    __slots__ = ("status", "blob_info_vec")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kStarted: _ClassVar[VMConversionInfo.Status]
        kOnPremDataCloned: _ClassVar[VMConversionInfo.Status]
        kVMConverted: _ClassVar[VMConversionInfo.Status]
        kFinished: _ClassVar[VMConversionInfo.Status]
    kStarted: VMConversionInfo.Status
    kOnPremDataCloned: VMConversionInfo.Status
    kVMConverted: VMConversionInfo.Status
    kFinished: VMConversionInfo.Status
    VM_CONVERSION_INFO_FIELD_NUMBER: _ClassVar[int]
    vm_conversion_info: _descriptor.FieldDescriptor
    STATUS_FIELD_NUMBER: _ClassVar[int]
    BLOB_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    status: VMConversionInfo.Status
    blob_info_vec: _containers.RepeatedCompositeFieldContainer[CloneTaskVolumeBlobInfo]
    def __init__(self, status: _Optional[_Union[VMConversionInfo.Status, str]] = ..., blob_info_vec: _Optional[_Iterable[_Union[CloneTaskVolumeBlobInfo, _Mapping]]] = ...) -> None: ...

class AwsVMConversionInfo(_message.Message):
    __slots__ = ("status",)
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kStarted: _ClassVar[AwsVMConversionInfo.Status]
        kClonedOnPremVMFiles: _ClassVar[AwsVMConversionInfo.Status]
        kClonedExportedOSDisk: _ClassVar[AwsVMConversionInfo.Status]
        kFinished: _ClassVar[AwsVMConversionInfo.Status]
    kStarted: AwsVMConversionInfo.Status
    kClonedOnPremVMFiles: AwsVMConversionInfo.Status
    kClonedExportedOSDisk: AwsVMConversionInfo.Status
    kFinished: AwsVMConversionInfo.Status
    AWS_VM_CONVERSION_INFO_FIELD_NUMBER: _ClassVar[int]
    aws_vm_conversion_info: _descriptor.FieldDescriptor
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: AwsVMConversionInfo.Status
    def __init__(self, status: _Optional[_Union[AwsVMConversionInfo.Status, str]] = ...) -> None: ...

class CohesityAgentInstallationStateProto(_message.Message):
    __slots__ = ("status", "tmp_folder_path")
    Extensions: _python_message._ExtensionDict
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kStarted: _ClassVar[CohesityAgentInstallationStateProto.Status]
        kPreDownloadStepsDone: _ClassVar[CohesityAgentInstallationStateProto.Status]
        kInstallerDownloaded: _ClassVar[CohesityAgentInstallationStateProto.Status]
        kAgentInstalled: _ClassVar[CohesityAgentInstallationStateProto.Status]
        kEnvironmentSpecificSetupDone: _ClassVar[CohesityAgentInstallationStateProto.Status]
    kStarted: CohesityAgentInstallationStateProto.Status
    kPreDownloadStepsDone: CohesityAgentInstallationStateProto.Status
    kInstallerDownloaded: CohesityAgentInstallationStateProto.Status
    kAgentInstalled: CohesityAgentInstallationStateProto.Status
    kEnvironmentSpecificSetupDone: CohesityAgentInstallationStateProto.Status
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TMP_FOLDER_PATH_FIELD_NUMBER: _ClassVar[int]
    status: CohesityAgentInstallationStateProto.Status
    tmp_folder_path: str
    def __init__(self, status: _Optional[_Union[CohesityAgentInstallationStateProto.Status, str]] = ..., tmp_folder_path: _Optional[str] = ...) -> None: ...
