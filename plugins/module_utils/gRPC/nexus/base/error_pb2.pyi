from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ErrorProto(_message.Message):
    __slots__ = ("type", "error_detail")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNoError: _ClassVar[ErrorProto.Type]
        kRetry: _ClassVar[ErrorProto.Type]
        kTimeout: _ClassVar[ErrorProto.Type]
        kNotCluster: _ClassVar[ErrorProto.Type]
        kGandalfError: _ClassVar[ErrorProto.Type]
        kInvalidVersion: _ClassVar[ErrorProto.Type]
        kStaleVersion: _ClassVar[ErrorProto.Type]
        kNonExistentKey: _ClassVar[ErrorProto.Type]
        kConfigWatchCancel: _ClassVar[ErrorProto.Type]
        kProtoParseError: _ClassVar[ErrorProto.Type]
        kNexusProxyNotInit: _ClassVar[ErrorProto.Type]
        kAvahiPublishError: _ClassVar[ErrorProto.Type]
        kCancel: _ClassVar[ErrorProto.Type]
        kInvalidRequest: _ClassVar[ErrorProto.Type]
        kNtpInitError: _ClassVar[ErrorProto.Type]
        kScribeError: _ClassVar[ErrorProto.Type]
        kPermissionDenied: _ClassVar[ErrorProto.Type]
        kNonExistent: _ClassVar[ErrorProto.Type]
        kTransportError: _ClassVar[ErrorProto.Type]
        kResumeIncomplete: _ClassVar[ErrorProto.Type]
        kAlreadyExists: _ClassVar[ErrorProto.Type]
        kCloudInternalError: _ClassVar[ErrorProto.Type]
        kCloudClusterCreateError: _ClassVar[ErrorProto.Type]
        kCloudResourceLimitExceeded: _ClassVar[ErrorProto.Type]
        kInvalidState: _ClassVar[ErrorProto.Type]
        kCloudResourceUnsupported: _ClassVar[ErrorProto.Type]
        kConfigWatchLimitExceeded: _ClassVar[ErrorProto.Type]
        kCloudNetworkConnectionError: _ClassVar[ErrorProto.Type]
        kDSHMNotInit: _ClassVar[ErrorProto.Type]
        kNotMaster: _ClassVar[ErrorProto.Type]
        kInTransientState: _ClassVar[ErrorProto.Type]
        kNameAlreadyExists: _ClassVar[ErrorProto.Type]
        kInvalidInput: _ClassVar[ErrorProto.Type]
        kOldVersion: _ClassVar[ErrorProto.Type]
        kNotTransientState: _ClassVar[ErrorProto.Type]
        kNoStableState: _ClassVar[ErrorProto.Type]
        kIDAlreadyExists: _ClassVar[ErrorProto.Type]
        kServiceNotEnabled: _ClassVar[ErrorProto.Type]
        kNotSupported: _ClassVar[ErrorProto.Type]
        kVolumeAttachmentFailed: _ClassVar[ErrorProto.Type]
        kKeychainError: _ClassVar[ErrorProto.Type]
        kSSLCertificateError: _ClassVar[ErrorProto.Type]
        kParseError: _ClassVar[ErrorProto.Type]
        kUnknownError: _ClassVar[ErrorProto.Type]
        kUDAConfigError: _ClassVar[ErrorProto.Type]
        kGCPSubnetIPExhausted: _ClassVar[ErrorProto.Type]
        kResourceCountLimitExceeded: _ClassVar[ErrorProto.Type]
        kSnapshotError: _ClassVar[ErrorProto.Type]
        kErrorCount: _ClassVar[ErrorProto.Type]
        kScriptError: _ClassVar[ErrorProto.Type]
    kNoError: ErrorProto.Type
    kRetry: ErrorProto.Type
    kTimeout: ErrorProto.Type
    kNotCluster: ErrorProto.Type
    kGandalfError: ErrorProto.Type
    kInvalidVersion: ErrorProto.Type
    kStaleVersion: ErrorProto.Type
    kNonExistentKey: ErrorProto.Type
    kConfigWatchCancel: ErrorProto.Type
    kProtoParseError: ErrorProto.Type
    kNexusProxyNotInit: ErrorProto.Type
    kAvahiPublishError: ErrorProto.Type
    kCancel: ErrorProto.Type
    kInvalidRequest: ErrorProto.Type
    kNtpInitError: ErrorProto.Type
    kScribeError: ErrorProto.Type
    kPermissionDenied: ErrorProto.Type
    kNonExistent: ErrorProto.Type
    kTransportError: ErrorProto.Type
    kResumeIncomplete: ErrorProto.Type
    kAlreadyExists: ErrorProto.Type
    kCloudInternalError: ErrorProto.Type
    kCloudClusterCreateError: ErrorProto.Type
    kCloudResourceLimitExceeded: ErrorProto.Type
    kInvalidState: ErrorProto.Type
    kCloudResourceUnsupported: ErrorProto.Type
    kConfigWatchLimitExceeded: ErrorProto.Type
    kCloudNetworkConnectionError: ErrorProto.Type
    kDSHMNotInit: ErrorProto.Type
    kNotMaster: ErrorProto.Type
    kInTransientState: ErrorProto.Type
    kNameAlreadyExists: ErrorProto.Type
    kInvalidInput: ErrorProto.Type
    kOldVersion: ErrorProto.Type
    kNotTransientState: ErrorProto.Type
    kNoStableState: ErrorProto.Type
    kIDAlreadyExists: ErrorProto.Type
    kServiceNotEnabled: ErrorProto.Type
    kNotSupported: ErrorProto.Type
    kVolumeAttachmentFailed: ErrorProto.Type
    kKeychainError: ErrorProto.Type
    kSSLCertificateError: ErrorProto.Type
    kParseError: ErrorProto.Type
    kUnknownError: ErrorProto.Type
    kUDAConfigError: ErrorProto.Type
    kGCPSubnetIPExhausted: ErrorProto.Type
    kResourceCountLimitExceeded: ErrorProto.Type
    kSnapshotError: ErrorProto.Type
    kErrorCount: ErrorProto.Type
    kScriptError: ErrorProto.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ERROR_DETAIL_FIELD_NUMBER: _ClassVar[int]
    type: ErrorProto.Type
    error_detail: str
    def __init__(self, type: _Optional[_Union[ErrorProto.Type, str]] = ..., error_detail: _Optional[str] = ...) -> None: ...
