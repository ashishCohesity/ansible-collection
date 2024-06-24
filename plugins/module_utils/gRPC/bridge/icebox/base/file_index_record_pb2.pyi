from yoda.master.stub import yoda_rpc_args_pb2 as _yoda_rpc_args_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CrackedFileIndexRecordProto(_message.Message):
    __slots__ = ("version", "entity_id", "cfile_doc_vec", "cfile_doc_batch_metadata")
    VERSION_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    CFILE_DOC_VEC_FIELD_NUMBER: _ClassVar[int]
    CFILE_DOC_BATCH_METADATA_FIELD_NUMBER: _ClassVar[int]
    version: int
    entity_id: int
    cfile_doc_vec: _containers.RepeatedCompositeFieldContainer[_yoda_rpc_args_pb2.CrackedFileArchiveDoc]
    cfile_doc_batch_metadata: _yoda_rpc_args_pb2.CrackedFileArchiveDocBatchMetadata
    def __init__(self, version: _Optional[int] = ..., entity_id: _Optional[int] = ..., cfile_doc_vec: _Optional[_Iterable[_Union[_yoda_rpc_args_pb2.CrackedFileArchiveDoc, _Mapping]]] = ..., cfile_doc_batch_metadata: _Optional[_Union[_yoda_rpc_args_pb2.CrackedFileArchiveDocBatchMetadata, _Mapping]] = ...) -> None: ...
