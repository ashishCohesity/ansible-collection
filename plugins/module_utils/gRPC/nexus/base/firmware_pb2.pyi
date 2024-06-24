from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class BIOSProto(_message.Message):
    __slots__ = ("model", "type", "primary", "secondary", "op_code", "boot_code", "sdr", "me", "vendor", "release_date", "bios_revision", "firmware_revision")
    MODEL_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_FIELD_NUMBER: _ClassVar[int]
    SECONDARY_FIELD_NUMBER: _ClassVar[int]
    OP_CODE_FIELD_NUMBER: _ClassVar[int]
    BOOT_CODE_FIELD_NUMBER: _ClassVar[int]
    SDR_FIELD_NUMBER: _ClassVar[int]
    ME_FIELD_NUMBER: _ClassVar[int]
    VENDOR_FIELD_NUMBER: _ClassVar[int]
    RELEASE_DATE_FIELD_NUMBER: _ClassVar[int]
    BIOS_REVISION_FIELD_NUMBER: _ClassVar[int]
    FIRMWARE_REVISION_FIELD_NUMBER: _ClassVar[int]
    model: str
    type: str
    primary: str
    secondary: str
    op_code: str
    boot_code: str
    sdr: str
    me: str
    vendor: str
    release_date: str
    bios_revision: str
    firmware_revision: str
    def __init__(self, model: _Optional[str] = ..., type: _Optional[str] = ..., primary: _Optional[str] = ..., secondary: _Optional[str] = ..., op_code: _Optional[str] = ..., boot_code: _Optional[str] = ..., sdr: _Optional[str] = ..., me: _Optional[str] = ..., vendor: _Optional[str] = ..., release_date: _Optional[str] = ..., bios_revision: _Optional[str] = ..., firmware_revision: _Optional[str] = ...) -> None: ...

class Disk(_message.Message):
    __slots__ = ("model", "type", "name", "vendor", "serial", "firmware")
    MODEL_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    VENDOR_FIELD_NUMBER: _ClassVar[int]
    SERIAL_FIELD_NUMBER: _ClassVar[int]
    FIRMWARE_FIELD_NUMBER: _ClassVar[int]
    model: str
    type: str
    name: str
    vendor: str
    serial: str
    firmware: str
    def __init__(self, model: _Optional[str] = ..., type: _Optional[str] = ..., name: _Optional[str] = ..., vendor: _Optional[str] = ..., serial: _Optional[str] = ..., firmware: _Optional[str] = ...) -> None: ...

class NIC(_message.Message):
    __slots__ = ("model", "type", "name", "vendor", "serial", "firmware")
    MODEL_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    VENDOR_FIELD_NUMBER: _ClassVar[int]
    SERIAL_FIELD_NUMBER: _ClassVar[int]
    FIRMWARE_FIELD_NUMBER: _ClassVar[int]
    model: str
    type: str
    name: str
    vendor: str
    serial: str
    firmware: str
    def __init__(self, model: _Optional[str] = ..., type: _Optional[str] = ..., name: _Optional[str] = ..., vendor: _Optional[str] = ..., serial: _Optional[str] = ..., firmware: _Optional[str] = ...) -> None: ...

class RAID(_message.Message):
    __slots__ = ("model", "type", "serial", "fw_build", "bios", "firmware")
    MODEL_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SERIAL_FIELD_NUMBER: _ClassVar[int]
    FW_BUILD_FIELD_NUMBER: _ClassVar[int]
    BIOS_FIELD_NUMBER: _ClassVar[int]
    FIRMWARE_FIELD_NUMBER: _ClassVar[int]
    model: str
    type: str
    serial: str
    fw_build: str
    bios: str
    firmware: str
    def __init__(self, model: _Optional[str] = ..., type: _Optional[str] = ..., serial: _Optional[str] = ..., fw_build: _Optional[str] = ..., bios: _Optional[str] = ..., firmware: _Optional[str] = ...) -> None: ...
