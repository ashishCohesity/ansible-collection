from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class O365ErrorProto(_message.Message):
    __slots__ = ("error_type", "error_message")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNoError: _ClassVar[O365ErrorProto.Type]
        kEmptySoapResponse: _ClassVar[O365ErrorProto.Type]
        kMailboxNotFound: _ClassVar[O365ErrorProto.Type]
        kInvalidSyncStateError: _ClassVar[O365ErrorProto.Type]
        kAutomaticFullBackupFailure: _ClassVar[O365ErrorProto.Type]
        kOneDriveResyncRequired: _ClassVar[O365ErrorProto.Type]
        kFolderIdMalformed: _ClassVar[O365ErrorProto.Type]
        kFolderAlreadyExists: _ClassVar[O365ErrorProto.Type]
        kSiteDriveBackupFailure: _ClassVar[O365ErrorProto.Type]
        kRangeNotSatisfiable: _ClassVar[O365ErrorProto.Type]
        kContentMailboxInfoMissing: _ClassVar[O365ErrorProto.Type]
        kFolderExpansionError: _ClassVar[O365ErrorProto.Type]
        kFetchContentError: _ClassVar[O365ErrorProto.Type]
        kSyncInfoMissing: _ClassVar[O365ErrorProto.Type]
        kPrivateChannelSiteBackupFailure: _ClassVar[O365ErrorProto.Type]
        kDeltaLinkExpired: _ClassVar[O365ErrorProto.Type]
        kGenericEwsErrorResponse: _ClassVar[O365ErrorProto.Type]
        kSiteDriveDataUnclean: _ClassVar[O365ErrorProto.Type]
        kUserOneDriveNotProvisioned: _ClassVar[O365ErrorProto.Type]
        kEmptyFileContent: _ClassVar[O365ErrorProto.Type]
        kFailedToAddSiteAdmin: _ClassVar[O365ErrorProto.Type]
        kFailedToAddSPListItemComment: _ClassVar[O365ErrorProto.Type]
        kFailedToAddSPListItemPermission: _ClassVar[O365ErrorProto.Type]
        kFailedToAddSPListItemAttachment: _ClassVar[O365ErrorProto.Type]
        kDriveQuotaExhausted: _ClassVar[O365ErrorProto.Type]
    kNoError: O365ErrorProto.Type
    kEmptySoapResponse: O365ErrorProto.Type
    kMailboxNotFound: O365ErrorProto.Type
    kInvalidSyncStateError: O365ErrorProto.Type
    kAutomaticFullBackupFailure: O365ErrorProto.Type
    kOneDriveResyncRequired: O365ErrorProto.Type
    kFolderIdMalformed: O365ErrorProto.Type
    kFolderAlreadyExists: O365ErrorProto.Type
    kSiteDriveBackupFailure: O365ErrorProto.Type
    kRangeNotSatisfiable: O365ErrorProto.Type
    kContentMailboxInfoMissing: O365ErrorProto.Type
    kFolderExpansionError: O365ErrorProto.Type
    kFetchContentError: O365ErrorProto.Type
    kSyncInfoMissing: O365ErrorProto.Type
    kPrivateChannelSiteBackupFailure: O365ErrorProto.Type
    kDeltaLinkExpired: O365ErrorProto.Type
    kGenericEwsErrorResponse: O365ErrorProto.Type
    kSiteDriveDataUnclean: O365ErrorProto.Type
    kUserOneDriveNotProvisioned: O365ErrorProto.Type
    kEmptyFileContent: O365ErrorProto.Type
    kFailedToAddSiteAdmin: O365ErrorProto.Type
    kFailedToAddSPListItemComment: O365ErrorProto.Type
    kFailedToAddSPListItemPermission: O365ErrorProto.Type
    kFailedToAddSPListItemAttachment: O365ErrorProto.Type
    kDriveQuotaExhausted: O365ErrorProto.Type
    ERROR_TYPE_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    error_type: O365ErrorProto.Type
    error_message: str
    def __init__(self, error_type: _Optional[_Union[O365ErrorProto.Type, str]] = ..., error_message: _Optional[str] = ...) -> None: ...
