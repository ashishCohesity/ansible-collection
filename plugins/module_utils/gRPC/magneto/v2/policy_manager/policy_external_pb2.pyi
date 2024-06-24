from magneto.api import magneto_external_base_pb2 as _magneto_external_base_pb2
from magneto.base import error_pb2 as _error_pb2
from magneto.base import policy_pb2 as _policy_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateOrUpdatePoliciesArg(_message.Message):
    __slots__ = ("base", "policy_vec")
    BASE_FIELD_NUMBER: _ClassVar[int]
    POLICY_VEC_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ArgumentBase
    policy_vec: _containers.RepeatedCompositeFieldContainer[_policy_pb2.ProtectionPolicyProto]
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ArgumentBase, _Mapping]] = ..., policy_vec: _Optional[_Iterable[_Union[_policy_pb2.ProtectionPolicyProto, _Mapping]]] = ...) -> None: ...

class CreateOrUpdatePoliciesResult(_message.Message):
    __slots__ = ("base", "result_vec")
    class Result(_message.Message):
        __slots__ = ("policy_id", "error")
        POLICY_ID_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        policy_id: str
        error: _magneto_external_base_pb2.ErrorProto
        def __init__(self, policy_id: _Optional[str] = ..., error: _Optional[_Union[_magneto_external_base_pb2.ErrorProto, _Mapping]] = ...) -> None: ...
    BASE_FIELD_NUMBER: _ClassVar[int]
    RESULT_VEC_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ResultBase
    result_vec: _containers.RepeatedCompositeFieldContainer[CreateOrUpdatePoliciesResult.Result]
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ResultBase, _Mapping]] = ..., result_vec: _Optional[_Iterable[_Union[CreateOrUpdatePoliciesResult.Result, _Mapping]]] = ...) -> None: ...

class FetchPoliciesArg(_message.Message):
    __slots__ = ("base", "policy_id_vec")
    BASE_FIELD_NUMBER: _ClassVar[int]
    POLICY_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ArgumentBase
    policy_id_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ArgumentBase, _Mapping]] = ..., policy_id_vec: _Optional[_Iterable[str]] = ...) -> None: ...

class FetchPoliciesResult(_message.Message):
    __slots__ = ("base", "result_vec")
    class Result(_message.Message):
        __slots__ = ("policy", "error")
        POLICY_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        policy: _policy_pb2.ProtectionPolicyProto
        error: _magneto_external_base_pb2.ErrorProto
        def __init__(self, policy: _Optional[_Union[_policy_pb2.ProtectionPolicyProto, _Mapping]] = ..., error: _Optional[_Union[_magneto_external_base_pb2.ErrorProto, _Mapping]] = ...) -> None: ...
    BASE_FIELD_NUMBER: _ClassVar[int]
    RESULT_VEC_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ResultBase
    result_vec: _containers.RepeatedCompositeFieldContainer[FetchPoliciesResult.Result]
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ResultBase, _Mapping]] = ..., result_vec: _Optional[_Iterable[_Union[FetchPoliciesResult.Result, _Mapping]]] = ...) -> None: ...
