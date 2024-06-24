from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class InstanceIdentityDocumentInfo(_message.Message):
    __slots__ = ("devpay_product_codes", "marketplace_product_codes", "availability_zone", "private_ip", "version", "instance_id", "billing_products", "instance_type", "account_id", "image_id", "pending_time", "architecture", "kernel_id", "ramdisk_id", "region")
    DEVPAY_PRODUCT_CODES_FIELD_NUMBER: _ClassVar[int]
    MARKETPLACE_PRODUCT_CODES_FIELD_NUMBER: _ClassVar[int]
    AVAILABILITY_ZONE_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_IP_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    BILLING_PRODUCTS_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    IMAGE_ID_FIELD_NUMBER: _ClassVar[int]
    PENDING_TIME_FIELD_NUMBER: _ClassVar[int]
    ARCHITECTURE_FIELD_NUMBER: _ClassVar[int]
    KERNEL_ID_FIELD_NUMBER: _ClassVar[int]
    RAMDISK_ID_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    devpay_product_codes: _containers.RepeatedScalarFieldContainer[str]
    marketplace_product_codes: _containers.RepeatedScalarFieldContainer[str]
    availability_zone: str
    private_ip: str
    version: str
    instance_id: str
    billing_products: _containers.RepeatedScalarFieldContainer[str]
    instance_type: str
    account_id: str
    image_id: str
    pending_time: str
    architecture: str
    kernel_id: str
    ramdisk_id: str
    region: str
    def __init__(self, devpay_product_codes: _Optional[_Iterable[str]] = ..., marketplace_product_codes: _Optional[_Iterable[str]] = ..., availability_zone: _Optional[str] = ..., private_ip: _Optional[str] = ..., version: _Optional[str] = ..., instance_id: _Optional[str] = ..., billing_products: _Optional[_Iterable[str]] = ..., instance_type: _Optional[str] = ..., account_id: _Optional[str] = ..., image_id: _Optional[str] = ..., pending_time: _Optional[str] = ..., architecture: _Optional[str] = ..., kernel_id: _Optional[str] = ..., ramdisk_id: _Optional[str] = ..., region: _Optional[str] = ...) -> None: ...
