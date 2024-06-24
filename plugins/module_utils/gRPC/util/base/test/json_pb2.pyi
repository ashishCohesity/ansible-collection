from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class JsonMessage(_message.Message):
    __slots__ = ("id_int64_as_string", "id_int64_as_numeric", "id_int32_as_numeric", "name_long", "percent_vec", "sub_message", "rep_sub_message", "unused_field")
    class SubJsonMessage(_message.Message):
        __slots__ = ("sub_id", "sub_name")
        SUB_ID_FIELD_NUMBER: _ClassVar[int]
        SUB_NAME_FIELD_NUMBER: _ClassVar[int]
        sub_id: int
        sub_name: str
        def __init__(self, sub_id: _Optional[int] = ..., sub_name: _Optional[str] = ...) -> None: ...
    ID_INT64_AS_STRING_FIELD_NUMBER: _ClassVar[int]
    ID_INT64_AS_NUMERIC_FIELD_NUMBER: _ClassVar[int]
    ID_INT32_AS_NUMERIC_FIELD_NUMBER: _ClassVar[int]
    NAME_LONG_FIELD_NUMBER: _ClassVar[int]
    PERCENT_VEC_FIELD_NUMBER: _ClassVar[int]
    SUB_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    REP_SUB_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    UNUSED_FIELD_FIELD_NUMBER: _ClassVar[int]
    id_int64_as_string: int
    id_int64_as_numeric: int
    id_int32_as_numeric: int
    name_long: str
    percent_vec: _containers.RepeatedScalarFieldContainer[float]
    sub_message: JsonMessage.SubJsonMessage
    rep_sub_message: _containers.RepeatedCompositeFieldContainer[JsonMessage.SubJsonMessage]
    unused_field: str
    def __init__(self, id_int64_as_string: _Optional[int] = ..., id_int64_as_numeric: _Optional[int] = ..., id_int32_as_numeric: _Optional[int] = ..., name_long: _Optional[str] = ..., percent_vec: _Optional[_Iterable[float]] = ..., sub_message: _Optional[_Union[JsonMessage.SubJsonMessage, _Mapping]] = ..., rep_sub_message: _Optional[_Iterable[_Union[JsonMessage.SubJsonMessage, _Mapping]]] = ..., unused_field: _Optional[str] = ...) -> None: ...

class JsonMessageList(_message.Message):
    __slots__ = ("json_message_vec",)
    JSON_MESSAGE_VEC_FIELD_NUMBER: _ClassVar[int]
    json_message_vec: _containers.RepeatedCompositeFieldContainer[JsonMessage]
    def __init__(self, json_message_vec: _Optional[_Iterable[_Union[JsonMessage, _Mapping]]] = ...) -> None: ...

class JsonObjectId(_message.Message):
    __slots__ = ("id", "type")
    ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    id: str
    type: str
    def __init__(self, id: _Optional[str] = ..., type: _Optional[str] = ...) -> None: ...

class JsonListMessageResponse(_message.Message):
    __slots__ = ("json_object_list",)
    class JsonObjectList(_message.Message):
        __slots__ = ("object_id", "tag_ids")
        OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
        TAG_IDS_FIELD_NUMBER: _ClassVar[int]
        object_id: JsonObjectId
        tag_ids: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, object_id: _Optional[_Union[JsonObjectId, _Mapping]] = ..., tag_ids: _Optional[_Iterable[str]] = ...) -> None: ...
    JSON_OBJECT_LIST_FIELD_NUMBER: _ClassVar[int]
    json_object_list: _containers.RepeatedCompositeFieldContainer[JsonListMessageResponse.JsonObjectList]
    def __init__(self, json_object_list: _Optional[_Iterable[_Union[JsonListMessageResponse.JsonObjectList, _Mapping]]] = ...) -> None: ...

class JsonStringList(_message.Message):
    __slots__ = ("json_string_vec",)
    JSON_STRING_VEC_FIELD_NUMBER: _ClassVar[int]
    json_string_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, json_string_vec: _Optional[_Iterable[str]] = ...) -> None: ...

class JsonListObject(_message.Message):
    __slots__ = ("json_string_message_list",)
    class JsonStringMessageList(_message.Message):
        __slots__ = ("object_id", "string_vec")
        OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
        STRING_VEC_FIELD_NUMBER: _ClassVar[int]
        object_id: _containers.RepeatedCompositeFieldContainer[JsonObjectId]
        string_vec: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, object_id: _Optional[_Iterable[_Union[JsonObjectId, _Mapping]]] = ..., string_vec: _Optional[_Iterable[str]] = ...) -> None: ...
    JSON_STRING_MESSAGE_LIST_FIELD_NUMBER: _ClassVar[int]
    json_string_message_list: _containers.RepeatedCompositeFieldContainer[JsonListObject.JsonStringMessageList]
    def __init__(self, json_string_message_list: _Optional[_Iterable[_Union[JsonListObject.JsonStringMessageList, _Mapping]]] = ...) -> None: ...
