from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DomainAssignmentProto(_message.Message):
    __slots__ = ("gandalf_key", "assignment_vec")
    class Assignment(_message.Message):
        __slots__ = ("constituent_id", "domain_vec")
        CONSTITUENT_ID_FIELD_NUMBER: _ClassVar[int]
        DOMAIN_VEC_FIELD_NUMBER: _ClassVar[int]
        constituent_id: int
        domain_vec: _containers.RepeatedScalarFieldContainer[int]
        def __init__(self, constituent_id: _Optional[int] = ..., domain_vec: _Optional[_Iterable[int]] = ...) -> None: ...
    GANDALF_KEY_FIELD_NUMBER: _ClassVar[int]
    ASSIGNMENT_VEC_FIELD_NUMBER: _ClassVar[int]
    gandalf_key: str
    assignment_vec: _containers.RepeatedCompositeFieldContainer[DomainAssignmentProto.Assignment]
    def __init__(self, gandalf_key: _Optional[str] = ..., assignment_vec: _Optional[_Iterable[_Union[DomainAssignmentProto.Assignment, _Mapping]]] = ...) -> None: ...
