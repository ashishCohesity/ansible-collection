from helios.crms.api.v1 import types_pb2 as _types_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetEntitlementsReq(_message.Message):
    __slots__ = ("account_id", "offering_type")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    OFFERING_TYPE_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    offering_type: _types_pb2.OfferingType
    def __init__(self, account_id: _Optional[str] = ..., offering_type: _Optional[_Union[_types_pb2.OfferingType, str]] = ...) -> None: ...

class GetEntitlementsResp(_message.Message):
    __slots__ = ("entitlement_info",)
    ENTITLEMENT_INFO_FIELD_NUMBER: _ClassVar[int]
    entitlement_info: _containers.RepeatedCompositeFieldContainer[EntitlementInfo]
    def __init__(self, entitlement_info: _Optional[_Iterable[_Union[EntitlementInfo, _Mapping]]] = ...) -> None: ...

class EntitlementInfo(_message.Message):
    __slots__ = ("id", "subscription_name", "quantity", "entitlement_source", "is_free_trail", "start_date", "end_date", "helios_end_date", "status", "offering_type", "sku", "aws_customer_id", "aws_product_id", "entitlement_type", "retention_period", "metering_dimension", "dataplane", "storage_class")
    ID_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTION_NAME_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    ENTITLEMENT_SOURCE_FIELD_NUMBER: _ClassVar[int]
    IS_FREE_TRAIL_FIELD_NUMBER: _ClassVar[int]
    START_DATE_FIELD_NUMBER: _ClassVar[int]
    END_DATE_FIELD_NUMBER: _ClassVar[int]
    HELIOS_END_DATE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    OFFERING_TYPE_FIELD_NUMBER: _ClassVar[int]
    SKU_FIELD_NUMBER: _ClassVar[int]
    AWS_CUSTOMER_ID_FIELD_NUMBER: _ClassVar[int]
    AWS_PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    ENTITLEMENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    RETENTION_PERIOD_FIELD_NUMBER: _ClassVar[int]
    METERING_DIMENSION_FIELD_NUMBER: _ClassVar[int]
    DATAPLANE_FIELD_NUMBER: _ClassVar[int]
    STORAGE_CLASS_FIELD_NUMBER: _ClassVar[int]
    id: str
    subscription_name: str
    quantity: int
    entitlement_source: str
    is_free_trail: bool
    start_date: str
    end_date: str
    helios_end_date: str
    status: str
    offering_type: _types_pb2.OfferingType
    sku: str
    aws_customer_id: str
    aws_product_id: str
    entitlement_type: _types_pb2.EntitlementType
    retention_period: str
    metering_dimension: str
    dataplane: str
    storage_class: str
    def __init__(self, id: _Optional[str] = ..., subscription_name: _Optional[str] = ..., quantity: _Optional[int] = ..., entitlement_source: _Optional[str] = ..., is_free_trail: bool = ..., start_date: _Optional[str] = ..., end_date: _Optional[str] = ..., helios_end_date: _Optional[str] = ..., status: _Optional[str] = ..., offering_type: _Optional[_Union[_types_pb2.OfferingType, str]] = ..., sku: _Optional[str] = ..., aws_customer_id: _Optional[str] = ..., aws_product_id: _Optional[str] = ..., entitlement_type: _Optional[_Union[_types_pb2.EntitlementType, str]] = ..., retention_period: _Optional[str] = ..., metering_dimension: _Optional[str] = ..., dataplane: _Optional[str] = ..., storage_class: _Optional[str] = ...) -> None: ...
