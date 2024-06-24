from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf.internal import python_message as _python_message
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor
MORE_AUTHOR_FIELD_NUMBER: _ClassVar[int]
more_author: _descriptor.FieldDescriptor

class Book(_message.Message):
    __slots__ = ("title", "author", "length", "published", "content", "data", "publisher", "labels", "type")
    Extensions: _python_message._ExtensionDict
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        FICTION: _ClassVar[Book.Type]
        KIDS: _ClassVar[Book.Type]
        ACTION_AND_ADVENTURE: _ClassVar[Book.Type]
        arts_and_photography: _ClassVar[Book.Type]
        I18N_Tech: _ClassVar[Book.Type]
    FICTION: Book.Type
    KIDS: Book.Type
    ACTION_AND_ADVENTURE: Book.Type
    arts_and_photography: Book.Type
    I18N_Tech: Book.Type
    class Data(_message.Message):
        __slots__ = ("year", "copyright")
        YEAR_FIELD_NUMBER: _ClassVar[int]
        COPYRIGHT_FIELD_NUMBER: _ClassVar[int]
        year: int
        copyright: str
        def __init__(self, year: _Optional[int] = ..., copyright: _Optional[str] = ...) -> None: ...
    class Label(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    TITLE_FIELD_NUMBER: _ClassVar[int]
    AUTHOR_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    PUBLISHED_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    PUBLISHER_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    title: str
    author: Author
    length: int
    published: int
    content: bytes
    data: Book.Data
    publisher: Publisher
    labels: _containers.RepeatedCompositeFieldContainer[Book.Label]
    type: Book.Type
    def __init__(self, title: _Optional[str] = ..., author: _Optional[_Union[Author, _Mapping]] = ..., length: _Optional[int] = ..., published: _Optional[int] = ..., content: _Optional[bytes] = ..., data: _Optional[_Union[Book.Data, _Mapping]] = ..., publisher: _Optional[_Union[Publisher, _Mapping]] = ..., labels: _Optional[_Iterable[_Union[Book.Label, _Mapping]]] = ..., type: _Optional[_Union[Book.Type, str]] = ...) -> None: ...

class Publisher(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class Author(_message.Message):
    __slots__ = ("id", "name", "pseudonym", "alive", "friend")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PSEUDONYM_FIELD_NUMBER: _ClassVar[int]
    ALIVE_FIELD_NUMBER: _ClassVar[int]
    FRIEND_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    pseudonym: _containers.RepeatedScalarFieldContainer[str]
    alive: bool
    friend: _containers.RepeatedCompositeFieldContainer[Author]
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., pseudonym: _Optional[_Iterable[str]] = ..., alive: bool = ..., friend: _Optional[_Iterable[_Union[Author, _Mapping]]] = ...) -> None: ...

class BadAuthor(_message.Message):
    __slots__ = ("id", "name", "pseudonym", "alive")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PSEUDONYM_FIELD_NUMBER: _ClassVar[int]
    ALIVE_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: _containers.RepeatedScalarFieldContainer[int]
    pseudonym: str
    alive: _containers.RepeatedScalarFieldContainer[bool]
    def __init__(self, id: _Optional[str] = ..., name: _Optional[_Iterable[int]] = ..., pseudonym: _Optional[str] = ..., alive: _Optional[_Iterable[bool]] = ...) -> None: ...

class Primitive(_message.Message):
    __slots__ = ("fix32", "u32", "i32", "sf32", "s32", "fix64", "u64", "i64", "sf64", "s64", "str", "bytes", "float", "double", "bool", "rep_fix32", "rep_u32", "rep_i32", "rep_sf32", "rep_s32", "rep_fix64", "rep_u64", "rep_i64", "rep_sf64", "rep_s64", "rep_str", "rep_bytes", "rep_float", "rep_double", "rep_bool")
    FIX32_FIELD_NUMBER: _ClassVar[int]
    U32_FIELD_NUMBER: _ClassVar[int]
    I32_FIELD_NUMBER: _ClassVar[int]
    SF32_FIELD_NUMBER: _ClassVar[int]
    S32_FIELD_NUMBER: _ClassVar[int]
    FIX64_FIELD_NUMBER: _ClassVar[int]
    U64_FIELD_NUMBER: _ClassVar[int]
    I64_FIELD_NUMBER: _ClassVar[int]
    SF64_FIELD_NUMBER: _ClassVar[int]
    S64_FIELD_NUMBER: _ClassVar[int]
    STR_FIELD_NUMBER: _ClassVar[int]
    BYTES_FIELD_NUMBER: _ClassVar[int]
    FLOAT_FIELD_NUMBER: _ClassVar[int]
    DOUBLE_FIELD_NUMBER: _ClassVar[int]
    BOOL_FIELD_NUMBER: _ClassVar[int]
    REP_FIX32_FIELD_NUMBER: _ClassVar[int]
    REP_U32_FIELD_NUMBER: _ClassVar[int]
    REP_I32_FIELD_NUMBER: _ClassVar[int]
    REP_SF32_FIELD_NUMBER: _ClassVar[int]
    REP_S32_FIELD_NUMBER: _ClassVar[int]
    REP_FIX64_FIELD_NUMBER: _ClassVar[int]
    REP_U64_FIELD_NUMBER: _ClassVar[int]
    REP_I64_FIELD_NUMBER: _ClassVar[int]
    REP_SF64_FIELD_NUMBER: _ClassVar[int]
    REP_S64_FIELD_NUMBER: _ClassVar[int]
    REP_STR_FIELD_NUMBER: _ClassVar[int]
    REP_BYTES_FIELD_NUMBER: _ClassVar[int]
    REP_FLOAT_FIELD_NUMBER: _ClassVar[int]
    REP_DOUBLE_FIELD_NUMBER: _ClassVar[int]
    REP_BOOL_FIELD_NUMBER: _ClassVar[int]
    fix32: int
    u32: int
    i32: int
    sf32: int
    s32: int
    fix64: int
    u64: int
    i64: int
    sf64: int
    s64: int
    str: str
    bytes: bytes
    float: float
    double: float
    bool: bool
    rep_fix32: _containers.RepeatedScalarFieldContainer[int]
    rep_u32: _containers.RepeatedScalarFieldContainer[int]
    rep_i32: _containers.RepeatedScalarFieldContainer[int]
    rep_sf32: _containers.RepeatedScalarFieldContainer[int]
    rep_s32: _containers.RepeatedScalarFieldContainer[int]
    rep_fix64: _containers.RepeatedScalarFieldContainer[int]
    rep_u64: _containers.RepeatedScalarFieldContainer[int]
    rep_i64: _containers.RepeatedScalarFieldContainer[int]
    rep_sf64: _containers.RepeatedScalarFieldContainer[int]
    rep_s64: _containers.RepeatedScalarFieldContainer[int]
    rep_str: _containers.RepeatedScalarFieldContainer[str]
    rep_bytes: _containers.RepeatedScalarFieldContainer[bytes]
    rep_float: _containers.RepeatedScalarFieldContainer[float]
    rep_double: _containers.RepeatedScalarFieldContainer[float]
    rep_bool: _containers.RepeatedScalarFieldContainer[bool]
    def __init__(self, fix32: _Optional[int] = ..., u32: _Optional[int] = ..., i32: _Optional[int] = ..., sf32: _Optional[int] = ..., s32: _Optional[int] = ..., fix64: _Optional[int] = ..., u64: _Optional[int] = ..., i64: _Optional[int] = ..., sf64: _Optional[int] = ..., s64: _Optional[int] = ..., str: _Optional[str] = ..., bytes: _Optional[bytes] = ..., float: _Optional[float] = ..., double: _Optional[float] = ..., bool: bool = ..., rep_fix32: _Optional[_Iterable[int]] = ..., rep_u32: _Optional[_Iterable[int]] = ..., rep_i32: _Optional[_Iterable[int]] = ..., rep_sf32: _Optional[_Iterable[int]] = ..., rep_s32: _Optional[_Iterable[int]] = ..., rep_fix64: _Optional[_Iterable[int]] = ..., rep_u64: _Optional[_Iterable[int]] = ..., rep_i64: _Optional[_Iterable[int]] = ..., rep_sf64: _Optional[_Iterable[int]] = ..., rep_s64: _Optional[_Iterable[int]] = ..., rep_str: _Optional[_Iterable[str]] = ..., rep_bytes: _Optional[_Iterable[bytes]] = ..., rep_float: _Optional[_Iterable[float]] = ..., rep_double: _Optional[_Iterable[float]] = ..., rep_bool: _Optional[_Iterable[bool]] = ...) -> None: ...

class PackedPrimitive(_message.Message):
    __slots__ = ("rep_fix32", "rep_u32", "rep_i32", "rep_sf32", "rep_s32", "rep_fix64", "rep_u64", "rep_i64", "rep_sf64", "rep_s64", "rep_float", "rep_double", "rep_bool")
    REP_FIX32_FIELD_NUMBER: _ClassVar[int]
    REP_U32_FIELD_NUMBER: _ClassVar[int]
    REP_I32_FIELD_NUMBER: _ClassVar[int]
    REP_SF32_FIELD_NUMBER: _ClassVar[int]
    REP_S32_FIELD_NUMBER: _ClassVar[int]
    REP_FIX64_FIELD_NUMBER: _ClassVar[int]
    REP_U64_FIELD_NUMBER: _ClassVar[int]
    REP_I64_FIELD_NUMBER: _ClassVar[int]
    REP_SF64_FIELD_NUMBER: _ClassVar[int]
    REP_S64_FIELD_NUMBER: _ClassVar[int]
    REP_FLOAT_FIELD_NUMBER: _ClassVar[int]
    REP_DOUBLE_FIELD_NUMBER: _ClassVar[int]
    REP_BOOL_FIELD_NUMBER: _ClassVar[int]
    rep_fix32: _containers.RepeatedScalarFieldContainer[int]
    rep_u32: _containers.RepeatedScalarFieldContainer[int]
    rep_i32: _containers.RepeatedScalarFieldContainer[int]
    rep_sf32: _containers.RepeatedScalarFieldContainer[int]
    rep_s32: _containers.RepeatedScalarFieldContainer[int]
    rep_fix64: _containers.RepeatedScalarFieldContainer[int]
    rep_u64: _containers.RepeatedScalarFieldContainer[int]
    rep_i64: _containers.RepeatedScalarFieldContainer[int]
    rep_sf64: _containers.RepeatedScalarFieldContainer[int]
    rep_s64: _containers.RepeatedScalarFieldContainer[int]
    rep_float: _containers.RepeatedScalarFieldContainer[float]
    rep_double: _containers.RepeatedScalarFieldContainer[float]
    rep_bool: _containers.RepeatedScalarFieldContainer[bool]
    def __init__(self, rep_fix32: _Optional[_Iterable[int]] = ..., rep_u32: _Optional[_Iterable[int]] = ..., rep_i32: _Optional[_Iterable[int]] = ..., rep_sf32: _Optional[_Iterable[int]] = ..., rep_s32: _Optional[_Iterable[int]] = ..., rep_fix64: _Optional[_Iterable[int]] = ..., rep_u64: _Optional[_Iterable[int]] = ..., rep_i64: _Optional[_Iterable[int]] = ..., rep_sf64: _Optional[_Iterable[int]] = ..., rep_s64: _Optional[_Iterable[int]] = ..., rep_float: _Optional[_Iterable[float]] = ..., rep_double: _Optional[_Iterable[float]] = ..., rep_bool: _Optional[_Iterable[bool]] = ...) -> None: ...

class NestedBook(_message.Message):
    __slots__ = ("book",)
    ANOTHER_BOOK_FIELD_NUMBER: _ClassVar[int]
    another_book: _descriptor.FieldDescriptor
    BOOK_FIELD_NUMBER: _ClassVar[int]
    book: Book
    def __init__(self, book: _Optional[_Union[Book, _Mapping]] = ...) -> None: ...

class BadNestedBook(_message.Message):
    __slots__ = ("book",)
    BOOK_FIELD_NUMBER: _ClassVar[int]
    book: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, book: _Optional[_Iterable[int]] = ...) -> None: ...

class Cyclic(_message.Message):
    __slots__ = ("m_int", "m_str", "m_book", "m_author", "m_cyclic")
    M_INT_FIELD_NUMBER: _ClassVar[int]
    M_STR_FIELD_NUMBER: _ClassVar[int]
    M_BOOK_FIELD_NUMBER: _ClassVar[int]
    M_AUTHOR_FIELD_NUMBER: _ClassVar[int]
    M_CYCLIC_FIELD_NUMBER: _ClassVar[int]
    m_int: int
    m_str: str
    m_book: Book
    m_author: _containers.RepeatedCompositeFieldContainer[Author]
    m_cyclic: Cyclic
    def __init__(self, m_int: _Optional[int] = ..., m_str: _Optional[str] = ..., m_book: _Optional[_Union[Book, _Mapping]] = ..., m_author: _Optional[_Iterable[_Union[Author, _Mapping]]] = ..., m_cyclic: _Optional[_Union[Cyclic, _Mapping]] = ...) -> None: ...

class TestJsonName1(_message.Message):
    __slots__ = ("one_value",)
    ONE_VALUE_FIELD_NUMBER: _ClassVar[int]
    one_value: int
    def __init__(self, one_value: _Optional[int] = ...) -> None: ...

class TestJsonName2(_message.Message):
    __slots__ = ("another_value",)
    ANOTHER_VALUE_FIELD_NUMBER: _ClassVar[int]
    another_value: int
    def __init__(self, another_value: _Optional[int] = ...) -> None: ...
