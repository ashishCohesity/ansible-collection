from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class Request(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kUnKnown: _ClassVar[Request.Type]
        kS3GetBuckets: _ClassVar[Request.Type]
        kS3GetBucketACL: _ClassVar[Request.Type]
        kS3UpdateBucketACL: _ClassVar[Request.Type]
        kS3MultipleDeleteObjects: _ClassVar[Request.Type]
        kS3GetBucketTagging: _ClassVar[Request.Type]
        kS3UpdateBucketTagging: _ClassVar[Request.Type]
        kS3DeleteBucketTagging: _ClassVar[Request.Type]
        kS3ListObjectVersions: _ClassVar[Request.Type]
        kS3GetBucketVersioning: _ClassVar[Request.Type]
        kS3UpdateBucketVersioning: _ClassVar[Request.Type]
        kS3ListMultiPartUploads: _ClassVar[Request.Type]
        kS3ListObjects: _ClassVar[Request.Type]
        kS3HeadBucket: _ClassVar[Request.Type]
        kS3CreateBucket: _ClassVar[Request.Type]
        kS3DeleteBucket: _ClassVar[Request.Type]
        kS3GetBucketLocation: _ClassVar[Request.Type]
        kS3GetObjectLockConfiguration: _ClassVar[Request.Type]
        kS3UpdateObjectLockConfiguration: _ClassVar[Request.Type]
        kS3GetBucketLifecycleConfiguration: _ClassVar[Request.Type]
        kS3UpdateBucketLifecycleConfiguration: _ClassVar[Request.Type]
        kS3DeleteBucketLifecycleConfiguration: _ClassVar[Request.Type]
        kS3GetBucketPolicy: _ClassVar[Request.Type]
        kS3UpdateBucketPolicy: _ClassVar[Request.Type]
        kS3DeleteBucketPolicy: _ClassVar[Request.Type]
        kS3GetBucketOwnershipControls: _ClassVar[Request.Type]
        kS3UpdateBucketOwnershipControls: _ClassVar[Request.Type]
        kS3DeleteBucketOwnershipControls: _ClassVar[Request.Type]
        kS3InitMultiPartUpload: _ClassVar[Request.Type]
        kS3ListObjectParts: _ClassVar[Request.Type]
        kS3UploadObjectPart: _ClassVar[Request.Type]
        kS3CompleteMultiPartUpload: _ClassVar[Request.Type]
        kS3AbortMultiPartUpload: _ClassVar[Request.Type]
        kS3GetObject: _ClassVar[Request.Type]
        kS3GetObjectMetadata: _ClassVar[Request.Type]
        kS3CreateObject: _ClassVar[Request.Type]
        kS3DeleteObject: _ClassVar[Request.Type]
        kS3GetObjectACL: _ClassVar[Request.Type]
        kS3UpdateObjectACL: _ClassVar[Request.Type]
        kS3CopyObject: _ClassVar[Request.Type]
        kS3GetObjectRetention: _ClassVar[Request.Type]
        kS3UpdateObjectRetention: _ClassVar[Request.Type]
        kS3GetObjectLegalHold: _ClassVar[Request.Type]
        kS3UpdateObjectLegalHold: _ClassVar[Request.Type]
        kS3GetObjectTagging: _ClassVar[Request.Type]
        kS3UpdateObjectTagging: _ClassVar[Request.Type]
        kS3DeleteObjectTagging: _ClassVar[Request.Type]
        kS3UploadPartCopy: _ClassVar[Request.Type]
        kSwiftGetServiceInfo: _ClassVar[Request.Type]
        kSwiftGetAccount: _ClassVar[Request.Type]
        kSwiftGetAccountMetadata: _ClassVar[Request.Type]
        kSwiftUpdateAccountMetadata: _ClassVar[Request.Type]
        kSwiftGetContainer: _ClassVar[Request.Type]
        kSwiftCreateContainer: _ClassVar[Request.Type]
        kSwiftUpdateContainerMetadata: _ClassVar[Request.Type]
        kSwiftGetContainerMetadata: _ClassVar[Request.Type]
        kSwiftDeleteContainer: _ClassVar[Request.Type]
        kSwiftGetObject: _ClassVar[Request.Type]
        kSwiftCreateObject: _ClassVar[Request.Type]
        kSwiftCopyObject: _ClassVar[Request.Type]
        kSwiftDeleteObject: _ClassVar[Request.Type]
        kSwiftGetObjectMetadata: _ClassVar[Request.Type]
        kSwiftUpdateObjectMetadata: _ClassVar[Request.Type]
        kSwiftGetEndpoints: _ClassVar[Request.Type]
    kUnKnown: Request.Type
    kS3GetBuckets: Request.Type
    kS3GetBucketACL: Request.Type
    kS3UpdateBucketACL: Request.Type
    kS3MultipleDeleteObjects: Request.Type
    kS3GetBucketTagging: Request.Type
    kS3UpdateBucketTagging: Request.Type
    kS3DeleteBucketTagging: Request.Type
    kS3ListObjectVersions: Request.Type
    kS3GetBucketVersioning: Request.Type
    kS3UpdateBucketVersioning: Request.Type
    kS3ListMultiPartUploads: Request.Type
    kS3ListObjects: Request.Type
    kS3HeadBucket: Request.Type
    kS3CreateBucket: Request.Type
    kS3DeleteBucket: Request.Type
    kS3GetBucketLocation: Request.Type
    kS3GetObjectLockConfiguration: Request.Type
    kS3UpdateObjectLockConfiguration: Request.Type
    kS3GetBucketLifecycleConfiguration: Request.Type
    kS3UpdateBucketLifecycleConfiguration: Request.Type
    kS3DeleteBucketLifecycleConfiguration: Request.Type
    kS3GetBucketPolicy: Request.Type
    kS3UpdateBucketPolicy: Request.Type
    kS3DeleteBucketPolicy: Request.Type
    kS3GetBucketOwnershipControls: Request.Type
    kS3UpdateBucketOwnershipControls: Request.Type
    kS3DeleteBucketOwnershipControls: Request.Type
    kS3InitMultiPartUpload: Request.Type
    kS3ListObjectParts: Request.Type
    kS3UploadObjectPart: Request.Type
    kS3CompleteMultiPartUpload: Request.Type
    kS3AbortMultiPartUpload: Request.Type
    kS3GetObject: Request.Type
    kS3GetObjectMetadata: Request.Type
    kS3CreateObject: Request.Type
    kS3DeleteObject: Request.Type
    kS3GetObjectACL: Request.Type
    kS3UpdateObjectACL: Request.Type
    kS3CopyObject: Request.Type
    kS3GetObjectRetention: Request.Type
    kS3UpdateObjectRetention: Request.Type
    kS3GetObjectLegalHold: Request.Type
    kS3UpdateObjectLegalHold: Request.Type
    kS3GetObjectTagging: Request.Type
    kS3UpdateObjectTagging: Request.Type
    kS3DeleteObjectTagging: Request.Type
    kS3UploadPartCopy: Request.Type
    kSwiftGetServiceInfo: Request.Type
    kSwiftGetAccount: Request.Type
    kSwiftGetAccountMetadata: Request.Type
    kSwiftUpdateAccountMetadata: Request.Type
    kSwiftGetContainer: Request.Type
    kSwiftCreateContainer: Request.Type
    kSwiftUpdateContainerMetadata: Request.Type
    kSwiftGetContainerMetadata: Request.Type
    kSwiftDeleteContainer: Request.Type
    kSwiftGetObject: Request.Type
    kSwiftCreateObject: Request.Type
    kSwiftCopyObject: Request.Type
    kSwiftDeleteObject: Request.Type
    kSwiftGetObjectMetadata: Request.Type
    kSwiftUpdateObjectMetadata: Request.Type
    kSwiftGetEndpoints: Request.Type
    def __init__(self) -> None: ...

class BucketSubresource(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNoSubresource: _ClassVar[BucketSubresource.Type]
        kAccelerate: _ClassVar[BucketSubresource.Type]
        kAcl: _ClassVar[BucketSubresource.Type]
        kCors: _ClassVar[BucketSubresource.Type]
        kDelete: _ClassVar[BucketSubresource.Type]
        kLifecycle: _ClassVar[BucketSubresource.Type]
        kLocation: _ClassVar[BucketSubresource.Type]
        kLogging: _ClassVar[BucketSubresource.Type]
        kPolicy: _ClassVar[BucketSubresource.Type]
        kReplication: _ClassVar[BucketSubresource.Type]
        kRequestPayment: _ClassVar[BucketSubresource.Type]
        kTagging: _ClassVar[BucketSubresource.Type]
        kVersions: _ClassVar[BucketSubresource.Type]
        kVersioning: _ClassVar[BucketSubresource.Type]
        kWebsite: _ClassVar[BucketSubresource.Type]
        kUploads: _ClassVar[BucketSubresource.Type]
        kObjectLock: _ClassVar[BucketSubresource.Type]
        kOwnershipControls: _ClassVar[BucketSubresource.Type]
    kNoSubresource: BucketSubresource.Type
    kAccelerate: BucketSubresource.Type
    kAcl: BucketSubresource.Type
    kCors: BucketSubresource.Type
    kDelete: BucketSubresource.Type
    kLifecycle: BucketSubresource.Type
    kLocation: BucketSubresource.Type
    kLogging: BucketSubresource.Type
    kPolicy: BucketSubresource.Type
    kReplication: BucketSubresource.Type
    kRequestPayment: BucketSubresource.Type
    kTagging: BucketSubresource.Type
    kVersions: BucketSubresource.Type
    kVersioning: BucketSubresource.Type
    kWebsite: BucketSubresource.Type
    kUploads: BucketSubresource.Type
    kObjectLock: BucketSubresource.Type
    kOwnershipControls: BucketSubresource.Type
    def __init__(self) -> None: ...

class ObjectSubresource(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNoSubresource: _ClassVar[ObjectSubresource.Type]
        kAcl: _ClassVar[ObjectSubresource.Type]
        kTorrent: _ClassVar[ObjectSubresource.Type]
        kRestore: _ClassVar[ObjectSubresource.Type]
        kUploads: _ClassVar[ObjectSubresource.Type]
        kUploadId: _ClassVar[ObjectSubresource.Type]
        kRetention: _ClassVar[ObjectSubresource.Type]
        kLegalHold: _ClassVar[ObjectSubresource.Type]
        kTagging: _ClassVar[ObjectSubresource.Type]
    kNoSubresource: ObjectSubresource.Type
    kAcl: ObjectSubresource.Type
    kTorrent: ObjectSubresource.Type
    kRestore: ObjectSubresource.Type
    kUploads: ObjectSubresource.Type
    kUploadId: ObjectSubresource.Type
    kRetention: ObjectSubresource.Type
    kLegalHold: ObjectSubresource.Type
    kTagging: ObjectSubresource.Type
    def __init__(self) -> None: ...
