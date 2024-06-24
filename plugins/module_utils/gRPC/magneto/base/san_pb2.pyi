from magneto.base import disk_pb2 as _disk_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf.internal import python_message as _python_message
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SanPort(_message.Message):
    __slots__ = ("iqn", "ip_addr", "port", "group_target_enabled", "wwn", "tag")
    IQN_FIELD_NUMBER: _ClassVar[int]
    IP_ADDR_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    GROUP_TARGET_ENABLED_FIELD_NUMBER: _ClassVar[int]
    WWN_FIELD_NUMBER: _ClassVar[int]
    TAG_FIELD_NUMBER: _ClassVar[int]
    iqn: str
    ip_addr: str
    port: int
    group_target_enabled: bool
    wwn: str
    tag: str
    def __init__(self, iqn: _Optional[str] = ..., ip_addr: _Optional[str] = ..., port: _Optional[int] = ..., group_target_enabled: bool = ..., wwn: _Optional[str] = ..., tag: _Optional[str] = ...) -> None: ...

class SanLogicalUnit(_message.Message):
    __slots__ = ("protocol", "name", "lun", "serial_number", "size", "total_bytes_read_from_source", "san_port_vec", "sub_file_size_mb", "source_volume_entity_id")
    Extensions: _python_message._ExtensionDict
    class ProtocolType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ISCSI: _ClassVar[SanLogicalUnit.ProtocolType]
        FC: _ClassVar[SanLogicalUnit.ProtocolType]
    ISCSI: SanLogicalUnit.ProtocolType
    FC: SanLogicalUnit.ProtocolType
    SAN_LOGICAL_UNIT_FIELD_NUMBER: _ClassVar[int]
    san_logical_unit: _descriptor.FieldDescriptor
    PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    LUN_FIELD_NUMBER: _ClassVar[int]
    SERIAL_NUMBER_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_BYTES_READ_FROM_SOURCE_FIELD_NUMBER: _ClassVar[int]
    SAN_PORT_VEC_FIELD_NUMBER: _ClassVar[int]
    SUB_FILE_SIZE_MB_FIELD_NUMBER: _ClassVar[int]
    SOURCE_VOLUME_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    protocol: SanLogicalUnit.ProtocolType
    name: str
    lun: int
    serial_number: str
    size: int
    total_bytes_read_from_source: int
    san_port_vec: _containers.RepeatedCompositeFieldContainer[SanPort]
    sub_file_size_mb: int
    source_volume_entity_id: int
    def __init__(self, protocol: _Optional[_Union[SanLogicalUnit.ProtocolType, str]] = ..., name: _Optional[str] = ..., lun: _Optional[int] = ..., serial_number: _Optional[str] = ..., size: _Optional[int] = ..., total_bytes_read_from_source: _Optional[int] = ..., san_port_vec: _Optional[_Iterable[_Union[SanPort, _Mapping]]] = ..., sub_file_size_mb: _Optional[int] = ..., source_volume_entity_id: _Optional[int] = ...) -> None: ...

class SanLogicalUnitSnapshot(_message.Message):
    __slots__ = ("san_logical_unit",)
    SAN_LOGICAL_UNIT_FIELD_NUMBER: _ClassVar[int]
    san_logical_unit: SanLogicalUnit
    def __init__(self, san_logical_unit: _Optional[_Union[SanLogicalUnit, _Mapping]] = ...) -> None: ...

class SanGroupUnit(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class AvailabilityGroup(_message.Message):
    __slots__ = ("name", "id")
    NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    id: str
    def __init__(self, name: _Optional[str] = ..., id: _Optional[str] = ...) -> None: ...
