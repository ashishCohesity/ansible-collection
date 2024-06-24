from configs import cluster_config_pb2 as _cluster_config_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PlatformGflagsProtoWrapper(_message.Message):
    __slots__ = ("service_defaults_vec",)
    class ServiceDefaultsProto(_message.Message):
        __slots__ = ("service_name", "platform_gflags_vec")
        class PlatformGflags(_message.Message):
            __slots__ = ("models", "gflags_vec")
            class Gflag(_message.Message):
                __slots__ = ("name", "value", "expected_value_before_apply", "for_parent_process")
                NAME_FIELD_NUMBER: _ClassVar[int]
                VALUE_FIELD_NUMBER: _ClassVar[int]
                EXPECTED_VALUE_BEFORE_APPLY_FIELD_NUMBER: _ClassVar[int]
                FOR_PARENT_PROCESS_FIELD_NUMBER: _ClassVar[int]
                name: str
                value: str
                expected_value_before_apply: str
                for_parent_process: bool
                def __init__(self, name: _Optional[str] = ..., value: _Optional[str] = ..., expected_value_before_apply: _Optional[str] = ..., for_parent_process: bool = ...) -> None: ...
            MODELS_FIELD_NUMBER: _ClassVar[int]
            GFLAGS_VEC_FIELD_NUMBER: _ClassVar[int]
            models: _containers.RepeatedScalarFieldContainer[_cluster_config_pb2.ClusterConfigProto.ProductModel]
            gflags_vec: _containers.RepeatedCompositeFieldContainer[PlatformGflagsProtoWrapper.ServiceDefaultsProto.PlatformGflags.Gflag]
            def __init__(self, models: _Optional[_Iterable[_Union[_cluster_config_pb2.ClusterConfigProto.ProductModel, str]]] = ..., gflags_vec: _Optional[_Iterable[_Union[PlatformGflagsProtoWrapper.ServiceDefaultsProto.PlatformGflags.Gflag, _Mapping]]] = ...) -> None: ...
        SERVICE_NAME_FIELD_NUMBER: _ClassVar[int]
        PLATFORM_GFLAGS_VEC_FIELD_NUMBER: _ClassVar[int]
        service_name: _cluster_config_pb2.ClusterConfigProto.Bulletin.ServiceName
        platform_gflags_vec: _containers.RepeatedCompositeFieldContainer[PlatformGflagsProtoWrapper.ServiceDefaultsProto.PlatformGflags]
        def __init__(self, service_name: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.Bulletin.ServiceName, str]] = ..., platform_gflags_vec: _Optional[_Iterable[_Union[PlatformGflagsProtoWrapper.ServiceDefaultsProto.PlatformGflags, _Mapping]]] = ...) -> None: ...
    SERVICE_DEFAULTS_VEC_FIELD_NUMBER: _ClassVar[int]
    service_defaults_vec: _containers.RepeatedCompositeFieldContainer[PlatformGflagsProtoWrapper.ServiceDefaultsProto]
    def __init__(self, service_defaults_vec: _Optional[_Iterable[_Union[PlatformGflagsProtoWrapper.ServiceDefaultsProto, _Mapping]]] = ...) -> None: ...
