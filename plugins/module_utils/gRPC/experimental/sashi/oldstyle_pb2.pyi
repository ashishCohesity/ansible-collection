from experimental.sashi import oldstyle_base_pb2 as _oldstyle_base_pb2
from experimental.sashi import newstyle_base_pb2 as _newstyle_base_pb2
from experimental.sashi import error_pb2 as _error_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class OldStyleProto(_message.Message):
    __slots__ = ("n", "o", "abcd")
    N_FIELD_NUMBER: _ClassVar[int]
    O_FIELD_NUMBER: _ClassVar[int]
    ABCD_FIELD_NUMBER: _ClassVar[int]
    n: _newstyle_base_pb2.NewStyleBaseProto
    o: _oldstyle_base_pb2.OldStyleBaseProto
    abcd: _error_pb2.Error
    def __init__(self, n: _Optional[_Union[_newstyle_base_pb2.NewStyleBaseProto, _Mapping]] = ..., o: _Optional[_Union[_oldstyle_base_pb2.OldStyleBaseProto, _Mapping]] = ..., abcd: _Optional[_Union[_error_pb2.Error, _Mapping]] = ...) -> None: ...
