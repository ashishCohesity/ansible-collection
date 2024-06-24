from configs import cluster_config_pb2 as _cluster_config_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PerfFactorsProto(_message.Message):
    __slots__ = ("model_factors_vec",)
    class ProductModelPerfFactor(_message.Message):
        __slots__ = ("product_model", "perf_factor")
        PRODUCT_MODEL_FIELD_NUMBER: _ClassVar[int]
        PERF_FACTOR_FIELD_NUMBER: _ClassVar[int]
        product_model: _cluster_config_pb2.ClusterConfigProto.ProductModel
        perf_factor: int
        def __init__(self, product_model: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.ProductModel, str]] = ..., perf_factor: _Optional[int] = ...) -> None: ...
    MODEL_FACTORS_VEC_FIELD_NUMBER: _ClassVar[int]
    model_factors_vec: _containers.RepeatedCompositeFieldContainer[PerfFactorsProto.ProductModelPerfFactor]
    def __init__(self, model_factors_vec: _Optional[_Iterable[_Union[PerfFactorsProto.ProductModelPerfFactor, _Mapping]]] = ...) -> None: ...
