from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FindingsProto(_message.Message):
    __slots__ = ("id", "quote", "info_type", "likelihood", "location", "resource_name", "info_type_name", "container_name")
    ID_FIELD_NUMBER: _ClassVar[int]
    QUOTE_FIELD_NUMBER: _ClassVar[int]
    INFO_TYPE_FIELD_NUMBER: _ClassVar[int]
    LIKELIHOOD_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    INFO_TYPE_NAME_FIELD_NUMBER: _ClassVar[int]
    CONTAINER_NAME_FIELD_NUMBER: _ClassVar[int]
    id: int
    quote: str
    info_type: InfoTypeProto
    likelihood: str
    location: LocationProto
    resource_name: str
    info_type_name: str
    container_name: str
    def __init__(self, id: _Optional[int] = ..., quote: _Optional[str] = ..., info_type: _Optional[_Union[InfoTypeProto, _Mapping]] = ..., likelihood: _Optional[str] = ..., location: _Optional[_Union[LocationProto, _Mapping]] = ..., resource_name: _Optional[str] = ..., info_type_name: _Optional[str] = ..., container_name: _Optional[str] = ...) -> None: ...

class InfoTypeProto(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class LocationProto(_message.Message):
    __slots__ = ("content_locations",)
    CONTENT_LOCATIONS_FIELD_NUMBER: _ClassVar[int]
    content_locations: _containers.RepeatedCompositeFieldContainer[ContentLocationProto]
    def __init__(self, content_locations: _Optional[_Iterable[_Union[ContentLocationProto, _Mapping]]] = ...) -> None: ...

class ContentLocationProto(_message.Message):
    __slots__ = ("container_name",)
    CONTAINER_NAME_FIELD_NUMBER: _ClassVar[int]
    container_name: str
    def __init__(self, container_name: _Optional[str] = ...) -> None: ...
