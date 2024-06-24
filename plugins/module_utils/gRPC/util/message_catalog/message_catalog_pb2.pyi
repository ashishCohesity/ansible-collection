from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MessageArgument(_message.Message):
    __slots__ = ("arg_name", "arg_value")
    ARG_NAME_FIELD_NUMBER: _ClassVar[int]
    ARG_VALUE_FIELD_NUMBER: _ClassVar[int]
    arg_name: str
    arg_value: str
    def __init__(self, arg_name: _Optional[str] = ..., arg_value: _Optional[str] = ...) -> None: ...

class MessageProto(_message.Message):
    __slots__ = ("message_guid", "message_args_vec", "short_message_string")
    MESSAGE_GUID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_ARGS_VEC_FIELD_NUMBER: _ClassVar[int]
    SHORT_MESSAGE_STRING_FIELD_NUMBER: _ClassVar[int]
    message_guid: str
    message_args_vec: _containers.RepeatedCompositeFieldContainer[MessageArgument]
    short_message_string: str
    def __init__(self, message_guid: _Optional[str] = ..., message_args_vec: _Optional[_Iterable[_Union[MessageArgument, _Mapping]]] = ..., short_message_string: _Optional[str] = ...) -> None: ...
