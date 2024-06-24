from magneto.api.common import base_pb2 as _base_pb2
from magneto.api.common import filters_pb2 as _filters_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class S3BackupJobParams(_message.Message):
    __slots__ = ("storage_classes", "skip_files_on_error", "indexing_policy", "backup_object_acls")
    class StorageClass(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kS3Standard: _ClassVar[S3BackupJobParams.StorageClass]
        kS3IntelligentTiering: _ClassVar[S3BackupJobParams.StorageClass]
        kS3StandardIA: _ClassVar[S3BackupJobParams.StorageClass]
        kS3OneZoneIA: _ClassVar[S3BackupJobParams.StorageClass]
    kS3Standard: S3BackupJobParams.StorageClass
    kS3IntelligentTiering: S3BackupJobParams.StorageClass
    kS3StandardIA: S3BackupJobParams.StorageClass
    kS3OneZoneIA: S3BackupJobParams.StorageClass
    STORAGE_CLASSES_FIELD_NUMBER: _ClassVar[int]
    SKIP_FILES_ON_ERROR_FIELD_NUMBER: _ClassVar[int]
    INDEXING_POLICY_FIELD_NUMBER: _ClassVar[int]
    BACKUP_OBJECT_ACLS_FIELD_NUMBER: _ClassVar[int]
    storage_classes: _containers.RepeatedScalarFieldContainer[S3BackupJobParams.StorageClass]
    skip_files_on_error: bool
    indexing_policy: _base_pb2.IndexingPolicyProto
    backup_object_acls: bool
    def __init__(self, storage_classes: _Optional[_Iterable[_Union[S3BackupJobParams.StorageClass, str]]] = ..., skip_files_on_error: bool = ..., indexing_policy: _Optional[_Union[_base_pb2.IndexingPolicyProto, _Mapping]] = ..., backup_object_acls: bool = ...) -> None: ...

class S3BucketParamsProto(_message.Message):
    __slots__ = ("filtering_policies",)
    FILTERING_POLICIES_FIELD_NUMBER: _ClassVar[int]
    filtering_policies: _containers.RepeatedCompositeFieldContainer[_filters_pb2.FilteringPolicyProto]
    def __init__(self, filtering_policies: _Optional[_Iterable[_Union[_filters_pb2.FilteringPolicyProto, _Mapping]]] = ...) -> None: ...
