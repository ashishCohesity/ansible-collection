from google.protobuf import descriptor_pb2 as _descriptor_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor
HTTP_STATUS_CODE_OPTION_FIELD_NUMBER: _ClassVar[int]
http_status_code_option: _descriptor.FieldDescriptor

class S3ErrorProto(_message.Message):
    __slots__ = ("code", "message", "resource")
    class Code(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNoError: _ClassVar[S3ErrorProto.Code]
        kAccessDenied: _ClassVar[S3ErrorProto.Code]
        kAccountProblem: _ClassVar[S3ErrorProto.Code]
        kAmbiguousGrantByEmailAddress: _ClassVar[S3ErrorProto.Code]
        kBadDigest: _ClassVar[S3ErrorProto.Code]
        kBucketAlreadyExists: _ClassVar[S3ErrorProto.Code]
        kBucketAlreadyOwnedByYou: _ClassVar[S3ErrorProto.Code]
        kBucketNotEmpty: _ClassVar[S3ErrorProto.Code]
        kCredentialsNotSupported: _ClassVar[S3ErrorProto.Code]
        kCrossLocationLoggingProhibited: _ClassVar[S3ErrorProto.Code]
        kEntityTooSmall: _ClassVar[S3ErrorProto.Code]
        kEntityTooLarge: _ClassVar[S3ErrorProto.Code]
        kExpiredToken: _ClassVar[S3ErrorProto.Code]
        kIllegalVersioningConfigurationException: _ClassVar[S3ErrorProto.Code]
        kIncompleteBody: _ClassVar[S3ErrorProto.Code]
        kIncorrectNumberOfFilesInPostRequest: _ClassVar[S3ErrorProto.Code]
        kInlineDataTooLarge: _ClassVar[S3ErrorProto.Code]
        kInternalError: _ClassVar[S3ErrorProto.Code]
        kInvalidAccessKeyId: _ClassVar[S3ErrorProto.Code]
        kInvalidArgument: _ClassVar[S3ErrorProto.Code]
        kInvalidBucketName: _ClassVar[S3ErrorProto.Code]
        kInvalidBucketState: _ClassVar[S3ErrorProto.Code]
        kInvalidDigest: _ClassVar[S3ErrorProto.Code]
        kInvalidEncryptionAlgorithmError: _ClassVar[S3ErrorProto.Code]
        kInvalidObjectState: _ClassVar[S3ErrorProto.Code]
        kInvalidPart: _ClassVar[S3ErrorProto.Code]
        kInvalidPartOrder: _ClassVar[S3ErrorProto.Code]
        kInvalidPolicyDocument: _ClassVar[S3ErrorProto.Code]
        kInvalidRange: _ClassVar[S3ErrorProto.Code]
        kInvalidRequest: _ClassVar[S3ErrorProto.Code]
        kInvalidSecurity: _ClassVar[S3ErrorProto.Code]
        kInvalidURI: _ClassVar[S3ErrorProto.Code]
        kKeyTooLong: _ClassVar[S3ErrorProto.Code]
        kMalformedACLError: _ClassVar[S3ErrorProto.Code]
        kMalformedXML: _ClassVar[S3ErrorProto.Code]
        kMaxMessageLengthExceeded: _ClassVar[S3ErrorProto.Code]
        kMetadataTooLarge: _ClassVar[S3ErrorProto.Code]
        kMethodNotAllowed: _ClassVar[S3ErrorProto.Code]
        kMissingContentLength: _ClassVar[S3ErrorProto.Code]
        kMissingRequestBodyError: _ClassVar[S3ErrorProto.Code]
        kNoSuchBucket: _ClassVar[S3ErrorProto.Code]
        kNoSuchKey: _ClassVar[S3ErrorProto.Code]
        kNoSuchLifecycleConfiguration: _ClassVar[S3ErrorProto.Code]
        kNoSuchUpload: _ClassVar[S3ErrorProto.Code]
        kNoSuchVersion: _ClassVar[S3ErrorProto.Code]
        kNotImplemented: _ClassVar[S3ErrorProto.Code]
        kNoSuchBucketPolicy: _ClassVar[S3ErrorProto.Code]
        kOperationAborted: _ClassVar[S3ErrorProto.Code]
        kPreconditionFailed: _ClassVar[S3ErrorProto.Code]
        kSignatureDoesNotMatch: _ClassVar[S3ErrorProto.Code]
        kTooManyRequests: _ClassVar[S3ErrorProto.Code]
        kServiceUnavailable: _ClassVar[S3ErrorProto.Code]
        kTooManyBuckets: _ClassVar[S3ErrorProto.Code]
        kUnexpectedContent: _ClassVar[S3ErrorProto.Code]
        kUnAuthorized: _ClassVar[S3ErrorProto.Code]
        kRequestTimeout: _ClassVar[S3ErrorProto.Code]
        kGatewayTimeout: _ClassVar[S3ErrorProto.Code]
        kInsufficientStorage: _ClassVar[S3ErrorProto.Code]
        kUnmodified: _ClassVar[S3ErrorProto.Code]
        kUnresolvableGrantByEmailAddress: _ClassVar[S3ErrorProto.Code]
        kRequestTimeTooSkewed: _ClassVar[S3ErrorProto.Code]
        kInvalidObjectName: _ClassVar[S3ErrorProto.Code]
        kEmptyMetadataKeyName: _ClassVar[S3ErrorProto.Code]
        kInvalidUtf8String: _ClassVar[S3ErrorProto.Code]
        kRetry: _ClassVar[S3ErrorProto.Code]
        kInvalidChunkBody: _ClassVar[S3ErrorProto.Code]
        kInvalidInternalState: _ClassVar[S3ErrorProto.Code]
        kInvalidToken: _ClassVar[S3ErrorProto.Code]
        kContainerAlreadyExists: _ClassVar[S3ErrorProto.Code]
        kSwiftBadDigest: _ClassVar[S3ErrorProto.Code]
        kObjectLockConfigurationNotFoundError: _ClassVar[S3ErrorProto.Code]
        kNoSuchObjectLockConfiguration: _ClassVar[S3ErrorProto.Code]
        kMalformedPolicy: _ClassVar[S3ErrorProto.Code]
        kBadRequest: _ClassVar[S3ErrorProto.Code]
        kInvalidTag: _ClassVar[S3ErrorProto.Code]
        kOwnershipControlsNotFoundError: _ClassVar[S3ErrorProto.Code]
        kAccessControlListNotSupported: _ClassVar[S3ErrorProto.Code]
        kInvalidBucketAclWithObjectOwnership: _ClassVar[S3ErrorProto.Code]
    kNoError: S3ErrorProto.Code
    kAccessDenied: S3ErrorProto.Code
    kAccountProblem: S3ErrorProto.Code
    kAmbiguousGrantByEmailAddress: S3ErrorProto.Code
    kBadDigest: S3ErrorProto.Code
    kBucketAlreadyExists: S3ErrorProto.Code
    kBucketAlreadyOwnedByYou: S3ErrorProto.Code
    kBucketNotEmpty: S3ErrorProto.Code
    kCredentialsNotSupported: S3ErrorProto.Code
    kCrossLocationLoggingProhibited: S3ErrorProto.Code
    kEntityTooSmall: S3ErrorProto.Code
    kEntityTooLarge: S3ErrorProto.Code
    kExpiredToken: S3ErrorProto.Code
    kIllegalVersioningConfigurationException: S3ErrorProto.Code
    kIncompleteBody: S3ErrorProto.Code
    kIncorrectNumberOfFilesInPostRequest: S3ErrorProto.Code
    kInlineDataTooLarge: S3ErrorProto.Code
    kInternalError: S3ErrorProto.Code
    kInvalidAccessKeyId: S3ErrorProto.Code
    kInvalidArgument: S3ErrorProto.Code
    kInvalidBucketName: S3ErrorProto.Code
    kInvalidBucketState: S3ErrorProto.Code
    kInvalidDigest: S3ErrorProto.Code
    kInvalidEncryptionAlgorithmError: S3ErrorProto.Code
    kInvalidObjectState: S3ErrorProto.Code
    kInvalidPart: S3ErrorProto.Code
    kInvalidPartOrder: S3ErrorProto.Code
    kInvalidPolicyDocument: S3ErrorProto.Code
    kInvalidRange: S3ErrorProto.Code
    kInvalidRequest: S3ErrorProto.Code
    kInvalidSecurity: S3ErrorProto.Code
    kInvalidURI: S3ErrorProto.Code
    kKeyTooLong: S3ErrorProto.Code
    kMalformedACLError: S3ErrorProto.Code
    kMalformedXML: S3ErrorProto.Code
    kMaxMessageLengthExceeded: S3ErrorProto.Code
    kMetadataTooLarge: S3ErrorProto.Code
    kMethodNotAllowed: S3ErrorProto.Code
    kMissingContentLength: S3ErrorProto.Code
    kMissingRequestBodyError: S3ErrorProto.Code
    kNoSuchBucket: S3ErrorProto.Code
    kNoSuchKey: S3ErrorProto.Code
    kNoSuchLifecycleConfiguration: S3ErrorProto.Code
    kNoSuchUpload: S3ErrorProto.Code
    kNoSuchVersion: S3ErrorProto.Code
    kNotImplemented: S3ErrorProto.Code
    kNoSuchBucketPolicy: S3ErrorProto.Code
    kOperationAborted: S3ErrorProto.Code
    kPreconditionFailed: S3ErrorProto.Code
    kSignatureDoesNotMatch: S3ErrorProto.Code
    kTooManyRequests: S3ErrorProto.Code
    kServiceUnavailable: S3ErrorProto.Code
    kTooManyBuckets: S3ErrorProto.Code
    kUnexpectedContent: S3ErrorProto.Code
    kUnAuthorized: S3ErrorProto.Code
    kRequestTimeout: S3ErrorProto.Code
    kGatewayTimeout: S3ErrorProto.Code
    kInsufficientStorage: S3ErrorProto.Code
    kUnmodified: S3ErrorProto.Code
    kUnresolvableGrantByEmailAddress: S3ErrorProto.Code
    kRequestTimeTooSkewed: S3ErrorProto.Code
    kInvalidObjectName: S3ErrorProto.Code
    kEmptyMetadataKeyName: S3ErrorProto.Code
    kInvalidUtf8String: S3ErrorProto.Code
    kRetry: S3ErrorProto.Code
    kInvalidChunkBody: S3ErrorProto.Code
    kInvalidInternalState: S3ErrorProto.Code
    kInvalidToken: S3ErrorProto.Code
    kContainerAlreadyExists: S3ErrorProto.Code
    kSwiftBadDigest: S3ErrorProto.Code
    kObjectLockConfigurationNotFoundError: S3ErrorProto.Code
    kNoSuchObjectLockConfiguration: S3ErrorProto.Code
    kMalformedPolicy: S3ErrorProto.Code
    kBadRequest: S3ErrorProto.Code
    kInvalidTag: S3ErrorProto.Code
    kOwnershipControlsNotFoundError: S3ErrorProto.Code
    kAccessControlListNotSupported: S3ErrorProto.Code
    kInvalidBucketAclWithObjectOwnership: S3ErrorProto.Code
    CODE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    code: S3ErrorProto.Code
    message: str
    resource: str
    def __init__(self, code: _Optional[_Union[S3ErrorProto.Code, str]] = ..., message: _Optional[str] = ..., resource: _Optional[str] = ...) -> None: ...
