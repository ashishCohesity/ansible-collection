from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Sale(_message.Message):
    __slots__ = ("sale_amount", "currency")
    SALE_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    sale_amount: int
    currency: str
    def __init__(self, sale_amount: _Optional[int] = ..., currency: _Optional[str] = ...) -> None: ...

class SalesAnalyticsPipelineData(_message.Message):
    __slots__ = ("currency_converters",)
    class CurrencyConverter(_message.Message):
        __slots__ = ("currency", "conversion_factor")
        CURRENCY_FIELD_NUMBER: _ClassVar[int]
        CONVERSION_FACTOR_FIELD_NUMBER: _ClassVar[int]
        currency: str
        conversion_factor: float
        def __init__(self, currency: _Optional[str] = ..., conversion_factor: _Optional[float] = ...) -> None: ...
    CURRENCY_CONVERTERS_FIELD_NUMBER: _ClassVar[int]
    currency_converters: _containers.RepeatedCompositeFieldContainer[SalesAnalyticsPipelineData.CurrencyConverter]
    def __init__(self, currency_converters: _Optional[_Iterable[_Union[SalesAnalyticsPipelineData.CurrencyConverter, _Mapping]]] = ...) -> None: ...
