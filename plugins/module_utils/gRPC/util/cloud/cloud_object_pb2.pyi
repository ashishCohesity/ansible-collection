from keychain.base import keychain_pb2 as _keychain_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CloudObject(_message.Message):
    __slots__ = ("edek_info", "data")
    EDEK_INFO_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    edek_info: _keychain_pb2.EdekProto
    data: bytes
    def __init__(self, edek_info: _Optional[_Union[_keychain_pb2.EdekProto, _Mapping]] = ..., data: _Optional[bytes] = ...) -> None: ...
