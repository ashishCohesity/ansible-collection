from magneto.api.common import base_pb2 as _base_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AWSSnapshotManagerEnvBackupParams(_message.Message):
    __slots__ = ("volume_exclusion_params", "indexing_policy", "should_create_ami", "ami_creation_frequency", "create_ami_for_run")
    VOLUME_EXCLUSION_PARAMS_FIELD_NUMBER: _ClassVar[int]
    INDEXING_POLICY_FIELD_NUMBER: _ClassVar[int]
    SHOULD_CREATE_AMI_FIELD_NUMBER: _ClassVar[int]
    AMI_CREATION_FREQUENCY_FIELD_NUMBER: _ClassVar[int]
    CREATE_AMI_FOR_RUN_FIELD_NUMBER: _ClassVar[int]
    volume_exclusion_params: EBSVolumeExclusionParams
    indexing_policy: _base_pb2.IndexingPolicyProto
    should_create_ami: bool
    ami_creation_frequency: int
    create_ami_for_run: bool
    def __init__(self, volume_exclusion_params: _Optional[_Union[EBSVolumeExclusionParams, _Mapping]] = ..., indexing_policy: _Optional[_Union[_base_pb2.IndexingPolicyProto, _Mapping]] = ..., should_create_ami: bool = ..., ami_creation_frequency: _Optional[int] = ..., create_ami_for_run: bool = ...) -> None: ...

class AWSNativeEnvBackupParams(_message.Message):
    __slots__ = ("volume_exclusion_params", "indexing_policy")
    VOLUME_EXCLUSION_PARAMS_FIELD_NUMBER: _ClassVar[int]
    INDEXING_POLICY_FIELD_NUMBER: _ClassVar[int]
    volume_exclusion_params: EBSVolumeExclusionParams
    indexing_policy: _base_pb2.IndexingPolicyProto
    def __init__(self, volume_exclusion_params: _Optional[_Union[EBSVolumeExclusionParams, _Mapping]] = ..., indexing_policy: _Optional[_Union[_base_pb2.IndexingPolicyProto, _Mapping]] = ...) -> None: ...

class AWSRDSSnapshotManagerEnvBackupParams(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AWSAuroraSnapshotManagerEnvBackupParams(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AwsRDSPostgresEnvBackupParams(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class EC2ObjectParamsProto(_message.Message):
    __slots__ = ("volume_exclusion_params",)
    VOLUME_EXCLUSION_PARAMS_FIELD_NUMBER: _ClassVar[int]
    volume_exclusion_params: EBSVolumeExclusionParams
    def __init__(self, volume_exclusion_params: _Optional[_Union[EBSVolumeExclusionParams, _Mapping]] = ...) -> None: ...

class EBSVolumeExclusionParams(_message.Message):
    __slots__ = ("volume_id_vec", "max_volume_size_bytes", "volume_type_vec", "device_name_vec")
    VOLUME_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    MAX_VOLUME_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    VOLUME_TYPE_VEC_FIELD_NUMBER: _ClassVar[int]
    DEVICE_NAME_VEC_FIELD_NUMBER: _ClassVar[int]
    volume_id_vec: _containers.RepeatedScalarFieldContainer[str]
    max_volume_size_bytes: int
    volume_type_vec: _containers.RepeatedScalarFieldContainer[str]
    device_name_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, volume_id_vec: _Optional[_Iterable[str]] = ..., max_volume_size_bytes: _Optional[int] = ..., volume_type_vec: _Optional[_Iterable[str]] = ..., device_name_vec: _Optional[_Iterable[str]] = ...) -> None: ...
