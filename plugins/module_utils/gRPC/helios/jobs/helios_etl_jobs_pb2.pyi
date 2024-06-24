from nexus.eagle_agent.base import pipe_data_pb2 as _pipe_data_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HeliosEtlJobs(_message.Message):
    __slots__ = ("job_type", "job_object", "cluster_identifier", "timestamp_ms", "sf_account_name")
    class JobType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        Unknown: _ClassVar[HeliosEtlJobs.JobType]
        Geolocation: _ClassVar[HeliosEtlJobs.JobType]
        MagnetoObjectAnalysis: _ClassVar[HeliosEtlJobs.JobType]
    Unknown: HeliosEtlJobs.JobType
    Geolocation: HeliosEtlJobs.JobType
    MagnetoObjectAnalysis: HeliosEtlJobs.JobType
    class JobObject(_message.Message):
        __slots__ = ("geolocation_object", "magneto_object")
        class GeolocationObject(_message.Message):
            __slots__ = ("ip_address", "force_refresh", "is_claimed")
            IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
            FORCE_REFRESH_FIELD_NUMBER: _ClassVar[int]
            IS_CLAIMED_FIELD_NUMBER: _ClassVar[int]
            ip_address: str
            force_refresh: bool
            is_claimed: bool
            def __init__(self, ip_address: _Optional[str] = ..., force_refresh: bool = ..., is_claimed: bool = ...) -> None: ...
        class MagnetoObjectAnalysisJobObject(_message.Message):
            __slots__ = ("object_type", "cluster_id", "disk_location", "checksum")
            OBJECT_TYPE_FIELD_NUMBER: _ClassVar[int]
            CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
            DISK_LOCATION_FIELD_NUMBER: _ClassVar[int]
            CHECKSUM_FIELD_NUMBER: _ClassVar[int]
            object_type: str
            cluster_id: int
            disk_location: str
            checksum: str
            def __init__(self, object_type: _Optional[str] = ..., cluster_id: _Optional[int] = ..., disk_location: _Optional[str] = ..., checksum: _Optional[str] = ...) -> None: ...
        GEOLOCATION_OBJECT_FIELD_NUMBER: _ClassVar[int]
        MAGNETO_OBJECT_FIELD_NUMBER: _ClassVar[int]
        geolocation_object: HeliosEtlJobs.JobObject.GeolocationObject
        magneto_object: HeliosEtlJobs.JobObject.MagnetoObjectAnalysisJobObject
        def __init__(self, geolocation_object: _Optional[_Union[HeliosEtlJobs.JobObject.GeolocationObject, _Mapping]] = ..., magneto_object: _Optional[_Union[HeliosEtlJobs.JobObject.MagnetoObjectAnalysisJobObject, _Mapping]] = ...) -> None: ...
    JOB_TYPE_FIELD_NUMBER: _ClassVar[int]
    JOB_OBJECT_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_MS_FIELD_NUMBER: _ClassVar[int]
    SF_ACCOUNT_NAME_FIELD_NUMBER: _ClassVar[int]
    job_type: HeliosEtlJobs.JobType
    job_object: HeliosEtlJobs.JobObject
    cluster_identifier: _pipe_data_pb2.ClusterIdentifier
    timestamp_ms: int
    sf_account_name: str
    def __init__(self, job_type: _Optional[_Union[HeliosEtlJobs.JobType, str]] = ..., job_object: _Optional[_Union[HeliosEtlJobs.JobObject, _Mapping]] = ..., cluster_identifier: _Optional[_Union[_pipe_data_pb2.ClusterIdentifier, _Mapping]] = ..., timestamp_ms: _Optional[int] = ..., sf_account_name: _Optional[str] = ...) -> None: ...
