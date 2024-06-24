from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StringArrayResponse(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, value: _Optional[_Iterable[str]] = ...) -> None: ...

class StringArrayRequest(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, value: _Optional[_Iterable[str]] = ...) -> None: ...

class EmptyRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetTagCategoryDetailsResponse(_message.Message):
    __slots__ = ("value",)
    class Value(_message.Message):
        __slots__ = ("id", "description", "name", "associable_types", "cardinality", "used_by")
        ID_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        ASSOCIABLE_TYPES_FIELD_NUMBER: _ClassVar[int]
        CARDINALITY_FIELD_NUMBER: _ClassVar[int]
        USED_BY_FIELD_NUMBER: _ClassVar[int]
        id: str
        description: str
        name: str
        associable_types: _containers.RepeatedScalarFieldContainer[str]
        cardinality: str
        used_by: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, id: _Optional[str] = ..., description: _Optional[str] = ..., name: _Optional[str] = ..., associable_types: _Optional[_Iterable[str]] = ..., cardinality: _Optional[str] = ..., used_by: _Optional[_Iterable[str]] = ...) -> None: ...
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: GetTagCategoryDetailsResponse.Value
    def __init__(self, value: _Optional[_Union[GetTagCategoryDetailsResponse.Value, _Mapping]] = ...) -> None: ...

class GetTagDetailsResponse(_message.Message):
    __slots__ = ("value",)
    class Value(_message.Message):
        __slots__ = ("id", "description", "name", "category_id", "used_by")
        ID_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        CATEGORY_ID_FIELD_NUMBER: _ClassVar[int]
        USED_BY_FIELD_NUMBER: _ClassVar[int]
        id: str
        description: str
        name: str
        category_id: str
        used_by: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, id: _Optional[str] = ..., description: _Optional[str] = ..., name: _Optional[str] = ..., category_id: _Optional[str] = ..., used_by: _Optional[_Iterable[str]] = ...) -> None: ...
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: GetTagDetailsResponse.Value
    def __init__(self, value: _Optional[_Union[GetTagDetailsResponse.Value, _Mapping]] = ...) -> None: ...

class ListAttachedObjectsResponse(_message.Message):
    __slots__ = ("value",)
    class Value(_message.Message):
        __slots__ = ("id", "type")
        ID_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        id: str
        type: str
        def __init__(self, id: _Optional[str] = ..., type: _Optional[str] = ...) -> None: ...
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: _containers.RepeatedCompositeFieldContainer[ListAttachedObjectsResponse.Value]
    def __init__(self, value: _Optional[_Iterable[_Union[ListAttachedObjectsResponse.Value, _Mapping]]] = ...) -> None: ...

class ListAttachedTagsRequest(_message.Message):
    __slots__ = ("object_id",)
    class Object_id(_message.Message):
        __slots__ = ("id", "type")
        ID_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        id: str
        type: str
        def __init__(self, id: _Optional[str] = ..., type: _Optional[str] = ...) -> None: ...
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    object_id: ListAttachedTagsRequest.Object_id
    def __init__(self, object_id: _Optional[_Union[ListAttachedTagsRequest.Object_id, _Mapping]] = ...) -> None: ...

class ListAttachedTagsOnObjectsRequest(_message.Message):
    __slots__ = ("object_ids",)
    class Object_id(_message.Message):
        __slots__ = ("id", "type")
        ID_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        id: str
        type: str
        def __init__(self, id: _Optional[str] = ..., type: _Optional[str] = ...) -> None: ...
    OBJECT_IDS_FIELD_NUMBER: _ClassVar[int]
    object_ids: _containers.RepeatedCompositeFieldContainer[ListAttachedTagsOnObjectsRequest.Object_id]
    def __init__(self, object_ids: _Optional[_Iterable[_Union[ListAttachedTagsOnObjectsRequest.Object_id, _Mapping]]] = ...) -> None: ...

class ListAttachedTagsOnObjectsResponse(_message.Message):
    __slots__ = ("value",)
    class Object_id(_message.Message):
        __slots__ = ("id", "type")
        ID_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        id: str
        type: str
        def __init__(self, id: _Optional[str] = ..., type: _Optional[str] = ...) -> None: ...
    class Value(_message.Message):
        __slots__ = ("object_id", "tag_ids")
        OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
        TAG_IDS_FIELD_NUMBER: _ClassVar[int]
        object_id: ListAttachedTagsOnObjectsResponse.Object_id
        tag_ids: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, object_id: _Optional[_Union[ListAttachedTagsOnObjectsResponse.Object_id, _Mapping]] = ..., tag_ids: _Optional[_Iterable[str]] = ...) -> None: ...
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: _containers.RepeatedCompositeFieldContainer[ListAttachedTagsOnObjectsResponse.Value]
    def __init__(self, value: _Optional[_Iterable[_Union[ListAttachedTagsOnObjectsResponse.Value, _Mapping]]] = ...) -> None: ...

class ApplyTagstoObjectRequest(_message.Message):
    __slots__ = ("object_id", "tag_ids")
    class Object_id(_message.Message):
        __slots__ = ("id", "type")
        ID_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        id: str
        type: str
        def __init__(self, id: _Optional[str] = ..., type: _Optional[str] = ...) -> None: ...
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    TAG_IDS_FIELD_NUMBER: _ClassVar[int]
    object_id: ApplyTagstoObjectRequest.Object_id
    tag_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, object_id: _Optional[_Union[ApplyTagstoObjectRequest.Object_id, _Mapping]] = ..., tag_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class ApplyTagstoObjectResponse(_message.Message):
    __slots__ = ("value",)
    class Value(_message.Message):
        __slots__ = ("error_messages", "success")
        class Error_messages(_message.Message):
            __slots__ = ("args", "default_message", "id")
            ARGS_FIELD_NUMBER: _ClassVar[int]
            DEFAULT_MESSAGE_FIELD_NUMBER: _ClassVar[int]
            ID_FIELD_NUMBER: _ClassVar[int]
            args: _containers.RepeatedScalarFieldContainer[str]
            default_message: str
            id: str
            def __init__(self, args: _Optional[_Iterable[str]] = ..., default_message: _Optional[str] = ..., id: _Optional[str] = ...) -> None: ...
        ERROR_MESSAGES_FIELD_NUMBER: _ClassVar[int]
        SUCCESS_FIELD_NUMBER: _ClassVar[int]
        error_messages: _containers.RepeatedCompositeFieldContainer[ApplyTagstoObjectResponse.Value.Error_messages]
        success: bool
        def __init__(self, error_messages: _Optional[_Iterable[_Union[ApplyTagstoObjectResponse.Value.Error_messages, _Mapping]]] = ..., success: bool = ...) -> None: ...
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: ApplyTagstoObjectResponse.Value
    def __init__(self, value: _Optional[_Union[ApplyTagstoObjectResponse.Value, _Mapping]] = ...) -> None: ...

class DetachTagsFromObjectRequest(_message.Message):
    __slots__ = ("object_id", "tag_ids")
    class Object_id(_message.Message):
        __slots__ = ("id", "type")
        ID_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        id: str
        type: str
        def __init__(self, id: _Optional[str] = ..., type: _Optional[str] = ...) -> None: ...
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    TAG_IDS_FIELD_NUMBER: _ClassVar[int]
    object_id: DetachTagsFromObjectRequest.Object_id
    tag_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, object_id: _Optional[_Union[DetachTagsFromObjectRequest.Object_id, _Mapping]] = ..., tag_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class DetachTagsFromObjectResponse(_message.Message):
    __slots__ = ("value",)
    class Value(_message.Message):
        __slots__ = ("error_messages", "success")
        class Error_messages(_message.Message):
            __slots__ = ("args", "default_message", "id")
            ARGS_FIELD_NUMBER: _ClassVar[int]
            DEFAULT_MESSAGE_FIELD_NUMBER: _ClassVar[int]
            ID_FIELD_NUMBER: _ClassVar[int]
            args: _containers.RepeatedScalarFieldContainer[str]
            default_message: str
            id: str
            def __init__(self, args: _Optional[_Iterable[str]] = ..., default_message: _Optional[str] = ..., id: _Optional[str] = ...) -> None: ...
        ERROR_MESSAGES_FIELD_NUMBER: _ClassVar[int]
        SUCCESS_FIELD_NUMBER: _ClassVar[int]
        error_messages: _containers.RepeatedCompositeFieldContainer[DetachTagsFromObjectResponse.Value.Error_messages]
        success: bool
        def __init__(self, error_messages: _Optional[_Iterable[_Union[DetachTagsFromObjectResponse.Value.Error_messages, _Mapping]]] = ..., success: bool = ...) -> None: ...
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: DetachTagsFromObjectResponse.Value
    def __init__(self, value: _Optional[_Union[DetachTagsFromObjectResponse.Value, _Mapping]] = ...) -> None: ...

class ObjectId(_message.Message):
    __slots__ = ("id", "type")
    ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    id: str
    type: str
    def __init__(self, id: _Optional[str] = ..., type: _Optional[str] = ...) -> None: ...

class ErrorMessage(_message.Message):
    __slots__ = ("args", "default_message", "id")
    ARGS_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    args: _containers.RepeatedScalarFieldContainer[str]
    default_message: str
    id: str
    def __init__(self, args: _Optional[_Iterable[str]] = ..., default_message: _Optional[str] = ..., id: _Optional[str] = ...) -> None: ...

class ListTagCategoriesIdResponseV1(_message.Message):
    __slots__ = ("tag_category_id_vec",)
    TAG_CATEGORY_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    tag_category_id_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, tag_category_id_vec: _Optional[_Iterable[str]] = ...) -> None: ...

class GetTagCategoryDetailsResponseV1(_message.Message):
    __slots__ = ("id", "description", "name", "associable_types", "cardinality", "used_by")
    ID_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ASSOCIABLE_TYPES_FIELD_NUMBER: _ClassVar[int]
    CARDINALITY_FIELD_NUMBER: _ClassVar[int]
    USED_BY_FIELD_NUMBER: _ClassVar[int]
    id: str
    description: str
    name: str
    associable_types: _containers.RepeatedScalarFieldContainer[str]
    cardinality: str
    used_by: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, id: _Optional[str] = ..., description: _Optional[str] = ..., name: _Optional[str] = ..., associable_types: _Optional[_Iterable[str]] = ..., cardinality: _Optional[str] = ..., used_by: _Optional[_Iterable[str]] = ...) -> None: ...

class ListTagsForCategoryRequestV1(_message.Message):
    __slots__ = ("category_id",)
    CATEGORY_ID_FIELD_NUMBER: _ClassVar[int]
    category_id: str
    def __init__(self, category_id: _Optional[str] = ...) -> None: ...

class ListTagsForCategoryResponseV1(_message.Message):
    __slots__ = ("tag_id_vec",)
    TAG_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    tag_id_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, tag_id_vec: _Optional[_Iterable[str]] = ...) -> None: ...

class GetTagDetailsResponseV1(_message.Message):
    __slots__ = ("id", "description", "name", "category_id", "used_by")
    ID_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_ID_FIELD_NUMBER: _ClassVar[int]
    USED_BY_FIELD_NUMBER: _ClassVar[int]
    id: str
    description: str
    name: str
    category_id: str
    used_by: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, id: _Optional[str] = ..., description: _Optional[str] = ..., name: _Optional[str] = ..., category_id: _Optional[str] = ..., used_by: _Optional[_Iterable[str]] = ...) -> None: ...

class ListAttachedObjectsResponseV1(_message.Message):
    __slots__ = ("attached_objects_vec",)
    ATTACHED_OBJECTS_VEC_FIELD_NUMBER: _ClassVar[int]
    attached_objects_vec: _containers.RepeatedCompositeFieldContainer[ObjectId]
    def __init__(self, attached_objects_vec: _Optional[_Iterable[_Union[ObjectId, _Mapping]]] = ...) -> None: ...

class ListAttachedTagsRequestV1(_message.Message):
    __slots__ = ("object_id",)
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    object_id: ObjectId
    def __init__(self, object_id: _Optional[_Union[ObjectId, _Mapping]] = ...) -> None: ...

class ListAttachedTagsResponseV1(_message.Message):
    __slots__ = ("attached_tags_vec",)
    ATTACHED_TAGS_VEC_FIELD_NUMBER: _ClassVar[int]
    attached_tags_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, attached_tags_vec: _Optional[_Iterable[str]] = ...) -> None: ...

class ListAttachedTagsOnObjectsRequestV1(_message.Message):
    __slots__ = ("object_ids",)
    OBJECT_IDS_FIELD_NUMBER: _ClassVar[int]
    object_ids: _containers.RepeatedCompositeFieldContainer[ObjectId]
    def __init__(self, object_ids: _Optional[_Iterable[_Union[ObjectId, _Mapping]]] = ...) -> None: ...

class ListAttachedTagsOnObjectsResponseV1(_message.Message):
    __slots__ = ("list_attached_tags_on_objects",)
    class ListAttachedTagsOnObjects(_message.Message):
        __slots__ = ("object_id", "tag_ids")
        OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
        TAG_IDS_FIELD_NUMBER: _ClassVar[int]
        object_id: ObjectId
        tag_ids: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, object_id: _Optional[_Union[ObjectId, _Mapping]] = ..., tag_ids: _Optional[_Iterable[str]] = ...) -> None: ...
    LIST_ATTACHED_TAGS_ON_OBJECTS_FIELD_NUMBER: _ClassVar[int]
    list_attached_tags_on_objects: _containers.RepeatedCompositeFieldContainer[ListAttachedTagsOnObjectsResponseV1.ListAttachedTagsOnObjects]
    def __init__(self, list_attached_tags_on_objects: _Optional[_Iterable[_Union[ListAttachedTagsOnObjectsResponseV1.ListAttachedTagsOnObjects, _Mapping]]] = ...) -> None: ...

class ApplyTagsToObjectRequestV1(_message.Message):
    __slots__ = ("object_id", "tag_ids")
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    TAG_IDS_FIELD_NUMBER: _ClassVar[int]
    object_id: ObjectId
    tag_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, object_id: _Optional[_Union[ObjectId, _Mapping]] = ..., tag_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class ApplyTagsToObjectResponseV1(_message.Message):
    __slots__ = ("error_messages", "success")
    ERROR_MESSAGES_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    error_messages: _containers.RepeatedCompositeFieldContainer[ErrorMessage]
    success: bool
    def __init__(self, error_messages: _Optional[_Iterable[_Union[ErrorMessage, _Mapping]]] = ..., success: bool = ...) -> None: ...

class DetachTagsFromObjectRequestV1(_message.Message):
    __slots__ = ("object_id", "tag_ids")
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    TAG_IDS_FIELD_NUMBER: _ClassVar[int]
    object_id: ObjectId
    tag_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, object_id: _Optional[_Union[ObjectId, _Mapping]] = ..., tag_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class DetachTagsFromObjectResponseV1(_message.Message):
    __slots__ = ("error_messages", "success")
    ERROR_MESSAGES_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    error_messages: _containers.RepeatedCompositeFieldContainer[ErrorMessage]
    success: bool
    def __init__(self, error_messages: _Optional[_Iterable[_Union[ErrorMessage, _Mapping]]] = ..., success: bool = ...) -> None: ...
