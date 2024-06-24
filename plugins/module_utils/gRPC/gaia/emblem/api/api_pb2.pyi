from gaia.dataplane.api import base_pb2 as _base_pb2
from gaia.emblem.base import error_pb2 as _error_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EmblemServiceInfo(_message.Message):
    __slots__ = ("host_address", "port", "authorization_header")
    HOST_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    AUTHORIZATION_HEADER_FIELD_NUMBER: _ClassVar[int]
    host_address: str
    port: int
    authorization_header: bytes
    def __init__(self, host_address: _Optional[str] = ..., port: _Optional[int] = ..., authorization_header: _Optional[bytes] = ...) -> None: ...

class VectorDBInfo(_message.Message):
    __slots__ = ("milvus_info", "pinecone_info")
    class MilvusInfo(_message.Message):
        __slots__ = ("host_address", "port", "username", "password")
        HOST_ADDRESS_FIELD_NUMBER: _ClassVar[int]
        PORT_FIELD_NUMBER: _ClassVar[int]
        USERNAME_FIELD_NUMBER: _ClassVar[int]
        PASSWORD_FIELD_NUMBER: _ClassVar[int]
        host_address: str
        port: int
        username: str
        password: str
        def __init__(self, host_address: _Optional[str] = ..., port: _Optional[int] = ..., username: _Optional[str] = ..., password: _Optional[str] = ...) -> None: ...
    class PineconeInfo(_message.Message):
        __slots__ = ("api_key",)
        API_KEY_FIELD_NUMBER: _ClassVar[int]
        api_key: bytes
        def __init__(self, api_key: _Optional[bytes] = ...) -> None: ...
    MILVUS_INFO_FIELD_NUMBER: _ClassVar[int]
    PINECONE_INFO_FIELD_NUMBER: _ClassVar[int]
    milvus_info: VectorDBInfo.MilvusInfo
    pinecone_info: VectorDBInfo.PineconeInfo
    def __init__(self, milvus_info: _Optional[_Union[VectorDBInfo.MilvusInfo, _Mapping]] = ..., pinecone_info: _Optional[_Union[VectorDBInfo.PineconeInfo, _Mapping]] = ...) -> None: ...

class CollectionIdentifier(_message.Message):
    __slots__ = ("name", "vector_db_info", "embeddings_model", "store_converted_documents")
    class EmbeddingsModel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kAllMiniLML6v2: _ClassVar[CollectionIdentifier.EmbeddingsModel]
    kAllMiniLML6v2: CollectionIdentifier.EmbeddingsModel
    NAME_FIELD_NUMBER: _ClassVar[int]
    VECTOR_DB_INFO_FIELD_NUMBER: _ClassVar[int]
    EMBEDDINGS_MODEL_FIELD_NUMBER: _ClassVar[int]
    STORE_CONVERTED_DOCUMENTS_FIELD_NUMBER: _ClassVar[int]
    name: str
    vector_db_info: VectorDBInfo
    embeddings_model: CollectionIdentifier.EmbeddingsModel
    store_converted_documents: bool
    def __init__(self, name: _Optional[str] = ..., vector_db_info: _Optional[_Union[VectorDBInfo, _Mapping]] = ..., embeddings_model: _Optional[_Union[CollectionIdentifier.EmbeddingsModel, str]] = ..., store_converted_documents: bool = ...) -> None: ...

class CreateCollectionArg(_message.Message):
    __slots__ = ("collection_id",)
    COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    collection_id: bytes
    def __init__(self, collection_id: _Optional[bytes] = ...) -> None: ...

class CreateCollectionResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteCollectionArg(_message.Message):
    __slots__ = ("collection_id",)
    COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    collection_id: bytes
    def __init__(self, collection_id: _Optional[bytes] = ...) -> None: ...

class DeleteCollectionResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class StartDocumentUploadArg(_message.Message):
    __slots__ = ("collection_id", "upload_specs")
    class UploadSpec(_message.Message):
        __slots__ = ("document_locator", "document_type", "total_length", "upload_length")
        DOCUMENT_LOCATOR_FIELD_NUMBER: _ClassVar[int]
        DOCUMENT_TYPE_FIELD_NUMBER: _ClassVar[int]
        TOTAL_LENGTH_FIELD_NUMBER: _ClassVar[int]
        UPLOAD_LENGTH_FIELD_NUMBER: _ClassVar[int]
        document_locator: bytes
        document_type: _base_pb2.DocumentType
        total_length: int
        upload_length: int
        def __init__(self, document_locator: _Optional[bytes] = ..., document_type: _Optional[_Union[_base_pb2.DocumentType, _Mapping]] = ..., total_length: _Optional[int] = ..., upload_length: _Optional[int] = ...) -> None: ...
    COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    UPLOAD_SPECS_FIELD_NUMBER: _ClassVar[int]
    collection_id: bytes
    upload_specs: _containers.RepeatedCompositeFieldContainer[StartDocumentUploadArg.UploadSpec]
    def __init__(self, collection_id: _Optional[bytes] = ..., upload_specs: _Optional[_Iterable[_Union[StartDocumentUploadArg.UploadSpec, _Mapping]]] = ...) -> None: ...

class StartDocumentUploadResult(_message.Message):
    __slots__ = ("upload_results",)
    class UploadResult(_message.Message):
        __slots__ = ("error_proto", "upload_handle")
        ERROR_PROTO_FIELD_NUMBER: _ClassVar[int]
        UPLOAD_HANDLE_FIELD_NUMBER: _ClassVar[int]
        error_proto: _error_pb2.ErrorProto
        upload_handle: bytes
        def __init__(self, error_proto: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., upload_handle: _Optional[bytes] = ...) -> None: ...
    UPLOAD_RESULTS_FIELD_NUMBER: _ClassVar[int]
    upload_results: _containers.RepeatedCompositeFieldContainer[StartDocumentUploadResult.UploadResult]
    def __init__(self, upload_results: _Optional[_Iterable[_Union[StartDocumentUploadResult.UploadResult, _Mapping]]] = ...) -> None: ...

class UploadHandleProto(_message.Message):
    __slots__ = ("document_directory_path",)
    DOCUMENT_DIRECTORY_PATH_FIELD_NUMBER: _ClassVar[int]
    document_directory_path: str
    def __init__(self, document_directory_path: _Optional[str] = ...) -> None: ...

class UploadDocumentPartsArg(_message.Message):
    __slots__ = ("upload_handle", "parts")
    class Part(_message.Message):
        __slots__ = ("offset", "content", "content_size")
        OFFSET_FIELD_NUMBER: _ClassVar[int]
        CONTENT_FIELD_NUMBER: _ClassVar[int]
        CONTENT_SIZE_FIELD_NUMBER: _ClassVar[int]
        offset: int
        content: bytes
        content_size: int
        def __init__(self, offset: _Optional[int] = ..., content: _Optional[bytes] = ..., content_size: _Optional[int] = ...) -> None: ...
    UPLOAD_HANDLE_FIELD_NUMBER: _ClassVar[int]
    PARTS_FIELD_NUMBER: _ClassVar[int]
    upload_handle: bytes
    parts: _containers.RepeatedCompositeFieldContainer[UploadDocumentPartsArg.Part]
    def __init__(self, upload_handle: _Optional[bytes] = ..., parts: _Optional[_Iterable[_Union[UploadDocumentPartsArg.Part, _Mapping]]] = ...) -> None: ...

class UploadDocumentPartsResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CreateEmbeddingsArg(_message.Message):
    __slots__ = ("document_batch", "upload_handles")
    class Document(_message.Message):
        __slots__ = ("document_locator", "document_type", "content", "content_size")
        DOCUMENT_LOCATOR_FIELD_NUMBER: _ClassVar[int]
        DOCUMENT_TYPE_FIELD_NUMBER: _ClassVar[int]
        CONTENT_FIELD_NUMBER: _ClassVar[int]
        CONTENT_SIZE_FIELD_NUMBER: _ClassVar[int]
        document_locator: bytes
        document_type: _base_pb2.DocumentType
        content: bytes
        content_size: int
        def __init__(self, document_locator: _Optional[bytes] = ..., document_type: _Optional[_Union[_base_pb2.DocumentType, _Mapping]] = ..., content: _Optional[bytes] = ..., content_size: _Optional[int] = ...) -> None: ...
    class DocumentBatch(_message.Message):
        __slots__ = ("collection_id", "documents")
        COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
        DOCUMENTS_FIELD_NUMBER: _ClassVar[int]
        collection_id: bytes
        documents: _containers.RepeatedCompositeFieldContainer[CreateEmbeddingsArg.Document]
        def __init__(self, collection_id: _Optional[bytes] = ..., documents: _Optional[_Iterable[_Union[CreateEmbeddingsArg.Document, _Mapping]]] = ...) -> None: ...
    DOCUMENT_BATCH_FIELD_NUMBER: _ClassVar[int]
    UPLOAD_HANDLES_FIELD_NUMBER: _ClassVar[int]
    document_batch: CreateEmbeddingsArg.DocumentBatch
    upload_handles: _containers.RepeatedScalarFieldContainer[bytes]
    def __init__(self, document_batch: _Optional[_Union[CreateEmbeddingsArg.DocumentBatch, _Mapping]] = ..., upload_handles: _Optional[_Iterable[bytes]] = ...) -> None: ...

class CreateEmbeddingsResult(_message.Message):
    __slots__ = ("results",)
    class EmbeddingsResult(_message.Message):
        __slots__ = ("error_proto", "num_indexed_chunks", "num_total_chunks", "num_indexed_bytes", "needed_conversion")
        ERROR_PROTO_FIELD_NUMBER: _ClassVar[int]
        NUM_INDEXED_CHUNKS_FIELD_NUMBER: _ClassVar[int]
        NUM_TOTAL_CHUNKS_FIELD_NUMBER: _ClassVar[int]
        NUM_INDEXED_BYTES_FIELD_NUMBER: _ClassVar[int]
        NEEDED_CONVERSION_FIELD_NUMBER: _ClassVar[int]
        error_proto: _error_pb2.ErrorProto
        num_indexed_chunks: int
        num_total_chunks: int
        num_indexed_bytes: int
        needed_conversion: bool
        def __init__(self, error_proto: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., num_indexed_chunks: _Optional[int] = ..., num_total_chunks: _Optional[int] = ..., num_indexed_bytes: _Optional[int] = ..., needed_conversion: bool = ...) -> None: ...
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[CreateEmbeddingsResult.EmbeddingsResult]
    def __init__(self, results: _Optional[_Iterable[_Union[CreateEmbeddingsResult.EmbeddingsResult, _Mapping]]] = ...) -> None: ...

class ConvertDocumentsArg(_message.Message):
    __slots__ = ("conversion_specs",)
    class ConversionSpec(_message.Message):
        __slots__ = ("document", "upload_handle", "offsets", "lengths")
        DOCUMENT_FIELD_NUMBER: _ClassVar[int]
        UPLOAD_HANDLE_FIELD_NUMBER: _ClassVar[int]
        OFFSETS_FIELD_NUMBER: _ClassVar[int]
        LENGTHS_FIELD_NUMBER: _ClassVar[int]
        document: CreateEmbeddingsArg.Document
        upload_handle: bytes
        offsets: _containers.RepeatedScalarFieldContainer[int]
        lengths: _containers.RepeatedScalarFieldContainer[int]
        def __init__(self, document: _Optional[_Union[CreateEmbeddingsArg.Document, _Mapping]] = ..., upload_handle: _Optional[bytes] = ..., offsets: _Optional[_Iterable[int]] = ..., lengths: _Optional[_Iterable[int]] = ...) -> None: ...
    CONVERSION_SPECS_FIELD_NUMBER: _ClassVar[int]
    conversion_specs: _containers.RepeatedCompositeFieldContainer[ConvertDocumentsArg.ConversionSpec]
    def __init__(self, conversion_specs: _Optional[_Iterable[_Union[ConvertDocumentsArg.ConversionSpec, _Mapping]]] = ...) -> None: ...

class ConvertDocumentsResult(_message.Message):
    __slots__ = ("conversion_results",)
    class ConversionResult(_message.Message):
        __slots__ = ("error_proto", "document_ranges")
        class ConvertedDocumentRange(_message.Message):
            __slots__ = ("content", "content_size")
            CONTENT_FIELD_NUMBER: _ClassVar[int]
            CONTENT_SIZE_FIELD_NUMBER: _ClassVar[int]
            content: bytes
            content_size: int
            def __init__(self, content: _Optional[bytes] = ..., content_size: _Optional[int] = ...) -> None: ...
        ERROR_PROTO_FIELD_NUMBER: _ClassVar[int]
        DOCUMENT_RANGES_FIELD_NUMBER: _ClassVar[int]
        error_proto: _error_pb2.ErrorProto
        document_ranges: _containers.RepeatedCompositeFieldContainer[ConvertDocumentsResult.ConversionResult.ConvertedDocumentRange]
        def __init__(self, error_proto: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., document_ranges: _Optional[_Iterable[_Union[ConvertDocumentsResult.ConversionResult.ConvertedDocumentRange, _Mapping]]] = ...) -> None: ...
    CONVERSION_RESULTS_FIELD_NUMBER: _ClassVar[int]
    conversion_results: _containers.RepeatedCompositeFieldContainer[ConvertDocumentsResult.ConversionResult]
    def __init__(self, conversion_results: _Optional[_Iterable[_Union[ConvertDocumentsResult.ConversionResult, _Mapping]]] = ...) -> None: ...

class GetSimilarDocumentPartsArg(_message.Message):
    __slots__ = ("collection_ids", "query", "top_k")
    COLLECTION_IDS_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    TOP_K_FIELD_NUMBER: _ClassVar[int]
    collection_ids: _containers.RepeatedScalarFieldContainer[bytes]
    query: str
    top_k: int
    def __init__(self, collection_ids: _Optional[_Iterable[bytes]] = ..., query: _Optional[str] = ..., top_k: _Optional[int] = ...) -> None: ...

class DocumentParts(_message.Message):
    __slots__ = ("document_locator", "parts")
    class Part(_message.Message):
        __slots__ = ("offset", "length", "needed_conversion", "text", "score")
        class MatchScore(_message.Message):
            __slots__ = ("cosine_similarity", "bm25_score")
            COSINE_SIMILARITY_FIELD_NUMBER: _ClassVar[int]
            BM25_SCORE_FIELD_NUMBER: _ClassVar[int]
            cosine_similarity: float
            bm25_score: float
            def __init__(self, cosine_similarity: _Optional[float] = ..., bm25_score: _Optional[float] = ...) -> None: ...
        OFFSET_FIELD_NUMBER: _ClassVar[int]
        LENGTH_FIELD_NUMBER: _ClassVar[int]
        NEEDED_CONVERSION_FIELD_NUMBER: _ClassVar[int]
        TEXT_FIELD_NUMBER: _ClassVar[int]
        SCORE_FIELD_NUMBER: _ClassVar[int]
        offset: int
        length: int
        needed_conversion: bool
        text: str
        score: DocumentParts.Part.MatchScore
        def __init__(self, offset: _Optional[int] = ..., length: _Optional[int] = ..., needed_conversion: bool = ..., text: _Optional[str] = ..., score: _Optional[_Union[DocumentParts.Part.MatchScore, _Mapping]] = ...) -> None: ...
    DOCUMENT_LOCATOR_FIELD_NUMBER: _ClassVar[int]
    PARTS_FIELD_NUMBER: _ClassVar[int]
    document_locator: bytes
    parts: _containers.RepeatedCompositeFieldContainer[DocumentParts.Part]
    def __init__(self, document_locator: _Optional[bytes] = ..., parts: _Optional[_Iterable[_Union[DocumentParts.Part, _Mapping]]] = ...) -> None: ...

class GetSimilarDocumentPartsResult(_message.Message):
    __slots__ = ("document_parts_vec",)
    DOCUMENT_PARTS_VEC_FIELD_NUMBER: _ClassVar[int]
    document_parts_vec: _containers.RepeatedCompositeFieldContainer[DocumentParts]
    def __init__(self, document_parts_vec: _Optional[_Iterable[_Union[DocumentParts, _Mapping]]] = ...) -> None: ...
