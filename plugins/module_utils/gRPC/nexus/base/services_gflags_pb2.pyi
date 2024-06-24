from configs import cluster_config_pb2 as _cluster_config_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ServicesGflagsProto(_message.Message):
    __slots__ = ("services_gflags_vec",)
    class ServiceProto(_message.Message):
        __slots__ = ("service_type", "gflags_vec")
        class ServiceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kApollo: _ClassVar[ServicesGflagsProto.ServiceProto.ServiceType]
            kBridge: _ClassVar[ServicesGflagsProto.ServiceProto.ServiceType]
            kGenie: _ClassVar[ServicesGflagsProto.ServiceProto.ServiceType]
            kGenieGofer: _ClassVar[ServicesGflagsProto.ServiceProto.ServiceType]
            kMagneto: _ClassVar[ServicesGflagsProto.ServiceProto.ServiceType]
            kIris: _ClassVar[ServicesGflagsProto.ServiceProto.ServiceType]
            kIrisProxy: _ClassVar[ServicesGflagsProto.ServiceProto.ServiceType]
            kScribe: _ClassVar[ServicesGflagsProto.ServiceProto.ServiceType]
            kStats: _ClassVar[ServicesGflagsProto.ServiceProto.ServiceType]
            kYoda: _ClassVar[ServicesGflagsProto.ServiceProto.ServiceType]
            kAlerts: _ClassVar[ServicesGflagsProto.ServiceProto.ServiceType]
            kKeychain: _ClassVar[ServicesGflagsProto.ServiceProto.ServiceType]
            kNewScribe: _ClassVar[ServicesGflagsProto.ServiceProto.ServiceType]
            kStorageProxy: _ClassVar[ServicesGflagsProto.ServiceProto.ServiceType]
            kRTClient: _ClassVar[ServicesGflagsProto.ServiceProto.ServiceType]
            kVaultProxy: _ClassVar[ServicesGflagsProto.ServiceProto.ServiceType]
            kGandalf: _ClassVar[ServicesGflagsProto.ServiceProto.ServiceType]
            kNexusProxy: _ClassVar[ServicesGflagsProto.ServiceProto.ServiceType]
            kTricorder: _ClassVar[ServicesGflagsProto.ServiceProto.ServiceType]
            kNexus: _ClassVar[ServicesGflagsProto.ServiceProto.ServiceType]
            kBridgeProxy: _ClassVar[ServicesGflagsProto.ServiceProto.ServiceType]
            kLibrarian: _ClassVar[ServicesGflagsProto.ServiceProto.ServiceType]
            kGroot: _ClassVar[ServicesGflagsProto.ServiceProto.ServiceType]
            kEagleAgent: _ClassVar[ServicesGflagsProto.ServiceProto.ServiceType]
            kAthena: _ClassVar[ServicesGflagsProto.ServiceProto.ServiceType]
            kBifrostBroker: _ClassVar[ServicesGflagsProto.ServiceProto.ServiceType]
            kLogwatcher: _ClassVar[ServicesGflagsProto.ServiceProto.ServiceType]
            kStatscollector: _ClassVar[ServicesGflagsProto.ServiceProto.ServiceType]
            kAtom: _ClassVar[ServicesGflagsProto.ServiceProto.ServiceType]
            kSmb2Proxy: _ClassVar[ServicesGflagsProto.ServiceProto.ServiceType]
            kThrottler: _ClassVar[ServicesGflagsProto.ServiceProto.ServiceType]
            kElrond: _ClassVar[ServicesGflagsProto.ServiceProto.ServiceType]
            kYodaAgent: _ClassVar[ServicesGflagsProto.ServiceProto.ServiceType]
            kHeimdall: _ClassVar[ServicesGflagsProto.ServiceProto.ServiceType]
            kBifrost: _ClassVar[ServicesGflagsProto.ServiceProto.ServiceType]
            kIcebox: _ClassVar[ServicesGflagsProto.ServiceProto.ServiceType]
            kCompass: _ClassVar[ServicesGflagsProto.ServiceProto.ServiceType]
            kPatch: _ClassVar[ServicesGflagsProto.ServiceProto.ServiceType]
            kAegis: _ClassVar[ServicesGflagsProto.ServiceProto.ServiceType]
            kEtlServer: _ClassVar[ServicesGflagsProto.ServiceProto.ServiceType]
            kNfsProxy: _ClassVar[ServicesGflagsProto.ServiceProto.ServiceType]
            kUpgrader: _ClassVar[ServicesGflagsProto.ServiceProto.ServiceType]
            kCohesityCa: _ClassVar[ServicesGflagsProto.ServiceProto.ServiceType]
            kCohesion: _ClassVar[ServicesGflagsProto.ServiceProto.ServiceType]
            kGaia: _ClassVar[ServicesGflagsProto.ServiceProto.ServiceType]
        kApollo: ServicesGflagsProto.ServiceProto.ServiceType
        kBridge: ServicesGflagsProto.ServiceProto.ServiceType
        kGenie: ServicesGflagsProto.ServiceProto.ServiceType
        kGenieGofer: ServicesGflagsProto.ServiceProto.ServiceType
        kMagneto: ServicesGflagsProto.ServiceProto.ServiceType
        kIris: ServicesGflagsProto.ServiceProto.ServiceType
        kIrisProxy: ServicesGflagsProto.ServiceProto.ServiceType
        kScribe: ServicesGflagsProto.ServiceProto.ServiceType
        kStats: ServicesGflagsProto.ServiceProto.ServiceType
        kYoda: ServicesGflagsProto.ServiceProto.ServiceType
        kAlerts: ServicesGflagsProto.ServiceProto.ServiceType
        kKeychain: ServicesGflagsProto.ServiceProto.ServiceType
        kNewScribe: ServicesGflagsProto.ServiceProto.ServiceType
        kStorageProxy: ServicesGflagsProto.ServiceProto.ServiceType
        kRTClient: ServicesGflagsProto.ServiceProto.ServiceType
        kVaultProxy: ServicesGflagsProto.ServiceProto.ServiceType
        kGandalf: ServicesGflagsProto.ServiceProto.ServiceType
        kNexusProxy: ServicesGflagsProto.ServiceProto.ServiceType
        kTricorder: ServicesGflagsProto.ServiceProto.ServiceType
        kNexus: ServicesGflagsProto.ServiceProto.ServiceType
        kBridgeProxy: ServicesGflagsProto.ServiceProto.ServiceType
        kLibrarian: ServicesGflagsProto.ServiceProto.ServiceType
        kGroot: ServicesGflagsProto.ServiceProto.ServiceType
        kEagleAgent: ServicesGflagsProto.ServiceProto.ServiceType
        kAthena: ServicesGflagsProto.ServiceProto.ServiceType
        kBifrostBroker: ServicesGflagsProto.ServiceProto.ServiceType
        kLogwatcher: ServicesGflagsProto.ServiceProto.ServiceType
        kStatscollector: ServicesGflagsProto.ServiceProto.ServiceType
        kAtom: ServicesGflagsProto.ServiceProto.ServiceType
        kSmb2Proxy: ServicesGflagsProto.ServiceProto.ServiceType
        kThrottler: ServicesGflagsProto.ServiceProto.ServiceType
        kElrond: ServicesGflagsProto.ServiceProto.ServiceType
        kYodaAgent: ServicesGflagsProto.ServiceProto.ServiceType
        kHeimdall: ServicesGflagsProto.ServiceProto.ServiceType
        kBifrost: ServicesGflagsProto.ServiceProto.ServiceType
        kIcebox: ServicesGflagsProto.ServiceProto.ServiceType
        kCompass: ServicesGflagsProto.ServiceProto.ServiceType
        kPatch: ServicesGflagsProto.ServiceProto.ServiceType
        kAegis: ServicesGflagsProto.ServiceProto.ServiceType
        kEtlServer: ServicesGflagsProto.ServiceProto.ServiceType
        kNfsProxy: ServicesGflagsProto.ServiceProto.ServiceType
        kUpgrader: ServicesGflagsProto.ServiceProto.ServiceType
        kCohesityCa: ServicesGflagsProto.ServiceProto.ServiceType
        kCohesion: ServicesGflagsProto.ServiceProto.ServiceType
        kGaia: ServicesGflagsProto.ServiceProto.ServiceType
        class Gflag(_message.Message):
            __slots__ = ("name", "value", "reason", "timestamp", "product_model", "for_parent_process")
            NAME_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            REASON_FIELD_NUMBER: _ClassVar[int]
            TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
            PRODUCT_MODEL_FIELD_NUMBER: _ClassVar[int]
            FOR_PARENT_PROCESS_FIELD_NUMBER: _ClassVar[int]
            name: str
            value: str
            reason: str
            timestamp: int
            product_model: _cluster_config_pb2.ClusterConfigProto.ProductModel
            for_parent_process: bool
            def __init__(self, name: _Optional[str] = ..., value: _Optional[str] = ..., reason: _Optional[str] = ..., timestamp: _Optional[int] = ..., product_model: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.ProductModel, str]] = ..., for_parent_process: bool = ...) -> None: ...
        SERVICE_TYPE_FIELD_NUMBER: _ClassVar[int]
        GFLAGS_VEC_FIELD_NUMBER: _ClassVar[int]
        service_type: ServicesGflagsProto.ServiceProto.ServiceType
        gflags_vec: _containers.RepeatedCompositeFieldContainer[ServicesGflagsProto.ServiceProto.Gflag]
        def __init__(self, service_type: _Optional[_Union[ServicesGflagsProto.ServiceProto.ServiceType, str]] = ..., gflags_vec: _Optional[_Iterable[_Union[ServicesGflagsProto.ServiceProto.Gflag, _Mapping]]] = ...) -> None: ...
    SERVICES_GFLAGS_VEC_FIELD_NUMBER: _ClassVar[int]
    services_gflags_vec: _containers.RepeatedCompositeFieldContainer[ServicesGflagsProto.ServiceProto]
    def __init__(self, services_gflags_vec: _Optional[_Iterable[_Union[ServicesGflagsProto.ServiceProto, _Mapping]]] = ...) -> None: ...
