from experimental.sashi import oldstyle_base_pb2 as _oldstyle_base_pb2
from experimental.sashi import newstyle_base_pb2 as _newstyle_base_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NewStyleProto(_message.Message):
    __slots__ = ("n", "o")
    N_FIELD_NUMBER: _ClassVar[int]
    O_FIELD_NUMBER: _ClassVar[int]
    n: _newstyle_base_pb2.NewStyleBaseProto
    o: _oldstyle_base_pb2.OldStyleBaseProto
    def __init__(self, n: _Optional[_Union[_newstyle_base_pb2.NewStyleBaseProto, _Mapping]] = ..., o: _Optional[_Union[_oldstyle_base_pb2.OldStyleBaseProto, _Mapping]] = ...) -> None: ...
