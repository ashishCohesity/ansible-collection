from open_util.net import protorpc_pb2 as _protorpc_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ReturnCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SUCCESS: _ClassVar[ReturnCode]
    ERROR: _ClassVar[ReturnCode]
SUCCESS: ReturnCode
ERROR: ReturnCode

class Data(_message.Message):
    __slots__ = ("length", "buffer")
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    BUFFER_FIELD_NUMBER: _ClassVar[int]
    length: int
    buffer: str
    def __init__(self, length: _Optional[int] = ..., buffer: _Optional[str] = ...) -> None: ...

class CreateRequest(_message.Message):
    __slots__ = ("fname",)
    FNAME_FIELD_NUMBER: _ClassVar[int]
    fname: str
    def __init__(self, fname: _Optional[str] = ...) -> None: ...

class CreateResult(_message.Message):
    __slots__ = ("code",)
    CODE_FIELD_NUMBER: _ClassVar[int]
    code: ReturnCode
    def __init__(self, code: _Optional[_Union[ReturnCode, str]] = ...) -> None: ...

class ReadRequest(_message.Message):
    __slots__ = ("fname", "offset", "length")
    FNAME_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    fname: str
    offset: int
    length: int
    def __init__(self, fname: _Optional[str] = ..., offset: _Optional[int] = ..., length: _Optional[int] = ...) -> None: ...

class ReadResult(_message.Message):
    __slots__ = ("code", "data")
    CODE_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    code: ReturnCode
    data: Data
    def __init__(self, code: _Optional[_Union[ReturnCode, str]] = ..., data: _Optional[_Union[Data, _Mapping]] = ...) -> None: ...

class WriteRequest(_message.Message):
    __slots__ = ("fname", "offset", "data")
    FNAME_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    fname: str
    offset: int
    data: Data
    def __init__(self, fname: _Optional[str] = ..., offset: _Optional[int] = ..., data: _Optional[_Union[Data, _Mapping]] = ...) -> None: ...

class WriteResult(_message.Message):
    __slots__ = ("code",)
    CODE_FIELD_NUMBER: _ClassVar[int]
    code: ReturnCode
    def __init__(self, code: _Optional[_Union[ReturnCode, str]] = ...) -> None: ...
