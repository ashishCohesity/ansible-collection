from nexus.sheltered_harbor.roles.common.proto import grpc_pb2 as _grpc_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class InstitutionIdType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    INVALID: _ClassVar[InstitutionIdType]
    TYPE1: _ClassVar[InstitutionIdType]
    TYPE2: _ClassVar[InstitutionIdType]
    TYPE3: _ClassVar[InstitutionIdType]
    TYPE4: _ClassVar[InstitutionIdType]
    TYPE5: _ClassVar[InstitutionIdType]
INVALID: InstitutionIdType
TYPE1: InstitutionIdType
TYPE2: InstitutionIdType
TYPE3: InstitutionIdType
TYPE4: InstitutionIdType
TYPE5: InstitutionIdType

class FinancialEntity(_message.Message):
    __slots__ = ("institution_id", "institution_id_type", "name", "registration_id")
    INSTITUTION_ID_FIELD_NUMBER: _ClassVar[int]
    INSTITUTION_ID_TYPE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    REGISTRATION_ID_FIELD_NUMBER: _ClassVar[int]
    institution_id: str
    institution_id_type: InstitutionIdType
    name: str
    registration_id: str
    def __init__(self, institution_id: _Optional[str] = ..., institution_id_type: _Optional[_Union[InstitutionIdType, str]] = ..., name: _Optional[str] = ..., registration_id: _Optional[str] = ...) -> None: ...

class FinancialEntitiesReq(_message.Message):
    __slots__ = ("list_parameters", "filters")
    class Filters(_message.Message):
        __slots__ = ("institution_id_types",)
        INSTITUTION_ID_TYPES_FIELD_NUMBER: _ClassVar[int]
        institution_id_types: _containers.RepeatedScalarFieldContainer[InstitutionIdType]
        def __init__(self, institution_id_types: _Optional[_Iterable[_Union[InstitutionIdType, str]]] = ...) -> None: ...
    LIST_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    list_parameters: _grpc_pb2.ListParameters
    filters: FinancialEntitiesReq.Filters
    def __init__(self, list_parameters: _Optional[_Union[_grpc_pb2.ListParameters, _Mapping]] = ..., filters: _Optional[_Union[FinancialEntitiesReq.Filters, _Mapping]] = ...) -> None: ...

class DataVaultingArchivePrepareReq(_message.Message):
    __slots__ = ("institution_id", "business_date")
    INSTITUTION_ID_FIELD_NUMBER: _ClassVar[int]
    BUSINESS_DATE_FIELD_NUMBER: _ClassVar[int]
    institution_id: str
    business_date: str
    def __init__(self, institution_id: _Optional[str] = ..., business_date: _Optional[str] = ...) -> None: ...

class DataVaultingArchivePrepareReply(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _grpc_pb2.CommonError
    def __init__(self, error: _Optional[_Union[_grpc_pb2.CommonError, _Mapping]] = ...) -> None: ...

class DataVaultingArchivePrepareStatusReq(_message.Message):
    __slots__ = ("institution_id", "business_date")
    INSTITUTION_ID_FIELD_NUMBER: _ClassVar[int]
    BUSINESS_DATE_FIELD_NUMBER: _ClassVar[int]
    institution_id: str
    business_date: str
    def __init__(self, institution_id: _Optional[str] = ..., business_date: _Optional[str] = ...) -> None: ...

class DataVaultingArchivePrepareStatusReply(_message.Message):
    __slots__ = ("error", "state", "status")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    error: _grpc_pb2.CommonError
    state: _grpc_pb2.OperationState
    status: str
    def __init__(self, error: _Optional[_Union[_grpc_pb2.CommonError, _Mapping]] = ..., state: _Optional[_Union[_grpc_pb2.OperationState, str]] = ..., status: _Optional[str] = ...) -> None: ...

class DataVaultingArchivePrepareCancelReq(_message.Message):
    __slots__ = ("institution_id", "business_date")
    INSTITUTION_ID_FIELD_NUMBER: _ClassVar[int]
    BUSINESS_DATE_FIELD_NUMBER: _ClassVar[int]
    institution_id: str
    business_date: str
    def __init__(self, institution_id: _Optional[str] = ..., business_date: _Optional[str] = ...) -> None: ...

class DataVaultingArchivePrepareCancelReply(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _grpc_pb2.CommonError
    def __init__(self, error: _Optional[_Union[_grpc_pb2.CommonError, _Mapping]] = ...) -> None: ...

class DataVaultingTransferUpdateReq(_message.Message):
    __slots__ = ("archive_id", "state", "status", "error")
    ARCHIVE_ID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    archive_id: str
    state: _grpc_pb2.OperationState
    status: str
    error: _grpc_pb2.CommonError
    def __init__(self, archive_id: _Optional[str] = ..., state: _Optional[_Union[_grpc_pb2.OperationState, str]] = ..., status: _Optional[str] = ..., error: _Optional[_Union[_grpc_pb2.CommonError, _Mapping]] = ...) -> None: ...

class DataVaultingTransferUpdateReply(_message.Message):
    __slots__ = ("error", "canceled")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    CANCELED_FIELD_NUMBER: _ClassVar[int]
    error: _grpc_pb2.CommonError
    canceled: bool
    def __init__(self, error: _Optional[_Union[_grpc_pb2.CommonError, _Mapping]] = ..., canceled: bool = ...) -> None: ...
