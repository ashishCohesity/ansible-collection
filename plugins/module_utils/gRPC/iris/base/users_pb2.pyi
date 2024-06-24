from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UsersProto(_message.Message):
    __slots__ = ("user_vec", "version", "group_vec", "custom_role_vec", "last_rid", "seeded_role_vec", "session_table", "allow_ui_access_privilege_upgraded", "smb_backup_operator_role_upgraded")
    class User(_message.Message):
        __slots__ = ("username", "password", "raw_smb_token", "ntlm_encrypted_password", "domain", "email_address", "first_name", "last_name", "s3_portal_account_info", "created_time_msecs", "last_updated_time_msecs", "expired_time_msec", "effective_time_msecs", "description", "role_vec", "sid", "primary_group_sid", "restricted", "tenant_id", "salesforce_account_info", "google_account_info", "force_password_change", "user_api_keys", "last_password_set_time_msecs", "previous_passwords", "invalid_login_attempts", "invalid_login_time_msecs", "is_account_locked", "is_account_disabled", "last_successful_login_time_msecs", "mfa_info", "allow_dso_modify", "is_ui_support_user", "role_type_vec", "language_preference", "timezone")
        class Role(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kClusterAdmin: _ClassVar[UsersProto.User.Role]
            kClusterUser: _ClassVar[UsersProto.User.Role]
            kClusterViewer: _ClassVar[UsersProto.User.Role]
        kClusterAdmin: UsersProto.User.Role
        kClusterUser: UsersProto.User.Role
        kClusterViewer: UsersProto.User.Role
        class S3PortalAccountInfo(_message.Message):
            __slots__ = ("canonical_user_id", "access_key_id", "secret_access_key")
            CANONICAL_USER_ID_FIELD_NUMBER: _ClassVar[int]
            ACCESS_KEY_ID_FIELD_NUMBER: _ClassVar[int]
            SECRET_ACCESS_KEY_FIELD_NUMBER: _ClassVar[int]
            canonical_user_id: str
            access_key_id: bytes
            secret_access_key: bytes
            def __init__(self, canonical_user_id: _Optional[str] = ..., access_key_id: _Optional[bytes] = ..., secret_access_key: _Optional[bytes] = ...) -> None: ...
        class ApiKey(_message.Message):
            __slots__ = ("id", "hashed_key", "name", "created_time_msecs", "created_user_sid", "created_username", "owner_user_sid", "owner_username", "expiration_time_msecs", "last_rotated_time_msecs", "is_active")
            ID_FIELD_NUMBER: _ClassVar[int]
            HASHED_KEY_FIELD_NUMBER: _ClassVar[int]
            NAME_FIELD_NUMBER: _ClassVar[int]
            CREATED_TIME_MSECS_FIELD_NUMBER: _ClassVar[int]
            CREATED_USER_SID_FIELD_NUMBER: _ClassVar[int]
            CREATED_USERNAME_FIELD_NUMBER: _ClassVar[int]
            OWNER_USER_SID_FIELD_NUMBER: _ClassVar[int]
            OWNER_USERNAME_FIELD_NUMBER: _ClassVar[int]
            EXPIRATION_TIME_MSECS_FIELD_NUMBER: _ClassVar[int]
            LAST_ROTATED_TIME_MSECS_FIELD_NUMBER: _ClassVar[int]
            IS_ACTIVE_FIELD_NUMBER: _ClassVar[int]
            id: str
            hashed_key: str
            name: str
            created_time_msecs: int
            created_user_sid: str
            created_username: str
            owner_user_sid: str
            owner_username: str
            expiration_time_msecs: int
            last_rotated_time_msecs: int
            is_active: bool
            def __init__(self, id: _Optional[str] = ..., hashed_key: _Optional[str] = ..., name: _Optional[str] = ..., created_time_msecs: _Optional[int] = ..., created_user_sid: _Optional[str] = ..., created_username: _Optional[str] = ..., owner_user_sid: _Optional[str] = ..., owner_username: _Optional[str] = ..., expiration_time_msecs: _Optional[int] = ..., last_rotated_time_msecs: _Optional[int] = ..., is_active: bool = ...) -> None: ...
        class TotpKey(_message.Message):
            __slots__ = ("name", "id", "secret_key", "uri", "is_totp_setup_done")
            NAME_FIELD_NUMBER: _ClassVar[int]
            ID_FIELD_NUMBER: _ClassVar[int]
            SECRET_KEY_FIELD_NUMBER: _ClassVar[int]
            URI_FIELD_NUMBER: _ClassVar[int]
            IS_TOTP_SETUP_DONE_FIELD_NUMBER: _ClassVar[int]
            name: str
            id: str
            secret_key: bytes
            uri: bytes
            is_totp_setup_done: bool
            def __init__(self, name: _Optional[str] = ..., id: _Optional[str] = ..., secret_key: _Optional[bytes] = ..., uri: _Optional[bytes] = ..., is_totp_setup_done: bool = ...) -> None: ...
        class MfaInfo(_message.Message):
            __slots__ = ("is_user_exempt_from_mfa", "totp_keys", "num_wrong_attempts", "invalid_verify_time_msecs")
            IS_USER_EXEMPT_FROM_MFA_FIELD_NUMBER: _ClassVar[int]
            TOTP_KEYS_FIELD_NUMBER: _ClassVar[int]
            NUM_WRONG_ATTEMPTS_FIELD_NUMBER: _ClassVar[int]
            INVALID_VERIFY_TIME_MSECS_FIELD_NUMBER: _ClassVar[int]
            is_user_exempt_from_mfa: bool
            totp_keys: _containers.RepeatedCompositeFieldContainer[UsersProto.User.TotpKey]
            num_wrong_attempts: int
            invalid_verify_time_msecs: int
            def __init__(self, is_user_exempt_from_mfa: bool = ..., totp_keys: _Optional[_Iterable[_Union[UsersProto.User.TotpKey, _Mapping]]] = ..., num_wrong_attempts: _Optional[int] = ..., invalid_verify_time_msecs: _Optional[int] = ...) -> None: ...
        USERNAME_FIELD_NUMBER: _ClassVar[int]
        PASSWORD_FIELD_NUMBER: _ClassVar[int]
        RAW_SMB_TOKEN_FIELD_NUMBER: _ClassVar[int]
        NTLM_ENCRYPTED_PASSWORD_FIELD_NUMBER: _ClassVar[int]
        DOMAIN_FIELD_NUMBER: _ClassVar[int]
        EMAIL_ADDRESS_FIELD_NUMBER: _ClassVar[int]
        FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
        LAST_NAME_FIELD_NUMBER: _ClassVar[int]
        S3_PORTAL_ACCOUNT_INFO_FIELD_NUMBER: _ClassVar[int]
        CREATED_TIME_MSECS_FIELD_NUMBER: _ClassVar[int]
        LAST_UPDATED_TIME_MSECS_FIELD_NUMBER: _ClassVar[int]
        EXPIRED_TIME_MSEC_FIELD_NUMBER: _ClassVar[int]
        EFFECTIVE_TIME_MSECS_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        ROLE_VEC_FIELD_NUMBER: _ClassVar[int]
        SID_FIELD_NUMBER: _ClassVar[int]
        PRIMARY_GROUP_SID_FIELD_NUMBER: _ClassVar[int]
        RESTRICTED_FIELD_NUMBER: _ClassVar[int]
        TENANT_ID_FIELD_NUMBER: _ClassVar[int]
        SALESFORCE_ACCOUNT_INFO_FIELD_NUMBER: _ClassVar[int]
        GOOGLE_ACCOUNT_INFO_FIELD_NUMBER: _ClassVar[int]
        FORCE_PASSWORD_CHANGE_FIELD_NUMBER: _ClassVar[int]
        USER_API_KEYS_FIELD_NUMBER: _ClassVar[int]
        LAST_PASSWORD_SET_TIME_MSECS_FIELD_NUMBER: _ClassVar[int]
        PREVIOUS_PASSWORDS_FIELD_NUMBER: _ClassVar[int]
        INVALID_LOGIN_ATTEMPTS_FIELD_NUMBER: _ClassVar[int]
        INVALID_LOGIN_TIME_MSECS_FIELD_NUMBER: _ClassVar[int]
        IS_ACCOUNT_LOCKED_FIELD_NUMBER: _ClassVar[int]
        IS_ACCOUNT_DISABLED_FIELD_NUMBER: _ClassVar[int]
        LAST_SUCCESSFUL_LOGIN_TIME_MSECS_FIELD_NUMBER: _ClassVar[int]
        MFA_INFO_FIELD_NUMBER: _ClassVar[int]
        ALLOW_DSO_MODIFY_FIELD_NUMBER: _ClassVar[int]
        IS_UI_SUPPORT_USER_FIELD_NUMBER: _ClassVar[int]
        ROLE_TYPE_VEC_FIELD_NUMBER: _ClassVar[int]
        LANGUAGE_PREFERENCE_FIELD_NUMBER: _ClassVar[int]
        TIMEZONE_FIELD_NUMBER: _ClassVar[int]
        username: str
        password: bytes
        raw_smb_token: bytes
        ntlm_encrypted_password: bytes
        domain: str
        email_address: str
        first_name: str
        last_name: str
        s3_portal_account_info: UsersProto.User.S3PortalAccountInfo
        created_time_msecs: int
        last_updated_time_msecs: int
        expired_time_msec: int
        effective_time_msecs: int
        description: str
        role_vec: _containers.RepeatedScalarFieldContainer[str]
        sid: str
        primary_group_sid: str
        restricted: bool
        tenant_id: str
        salesforce_account_info: SalesforceAccountInfo
        google_account_info: GoogleAccountInfo
        force_password_change: bool
        user_api_keys: _containers.RepeatedCompositeFieldContainer[UsersProto.User.ApiKey]
        last_password_set_time_msecs: int
        previous_passwords: _containers.RepeatedScalarFieldContainer[bytes]
        invalid_login_attempts: int
        invalid_login_time_msecs: int
        is_account_locked: bool
        is_account_disabled: bool
        last_successful_login_time_msecs: int
        mfa_info: UsersProto.User.MfaInfo
        allow_dso_modify: bool
        is_ui_support_user: bool
        role_type_vec: _containers.RepeatedScalarFieldContainer[UsersProto.User.Role]
        language_preference: str
        timezone: str
        def __init__(self, username: _Optional[str] = ..., password: _Optional[bytes] = ..., raw_smb_token: _Optional[bytes] = ..., ntlm_encrypted_password: _Optional[bytes] = ..., domain: _Optional[str] = ..., email_address: _Optional[str] = ..., first_name: _Optional[str] = ..., last_name: _Optional[str] = ..., s3_portal_account_info: _Optional[_Union[UsersProto.User.S3PortalAccountInfo, _Mapping]] = ..., created_time_msecs: _Optional[int] = ..., last_updated_time_msecs: _Optional[int] = ..., expired_time_msec: _Optional[int] = ..., effective_time_msecs: _Optional[int] = ..., description: _Optional[str] = ..., role_vec: _Optional[_Iterable[str]] = ..., sid: _Optional[str] = ..., primary_group_sid: _Optional[str] = ..., restricted: bool = ..., tenant_id: _Optional[str] = ..., salesforce_account_info: _Optional[_Union[SalesforceAccountInfo, _Mapping]] = ..., google_account_info: _Optional[_Union[GoogleAccountInfo, _Mapping]] = ..., force_password_change: bool = ..., user_api_keys: _Optional[_Iterable[_Union[UsersProto.User.ApiKey, _Mapping]]] = ..., last_password_set_time_msecs: _Optional[int] = ..., previous_passwords: _Optional[_Iterable[bytes]] = ..., invalid_login_attempts: _Optional[int] = ..., invalid_login_time_msecs: _Optional[int] = ..., is_account_locked: bool = ..., is_account_disabled: bool = ..., last_successful_login_time_msecs: _Optional[int] = ..., mfa_info: _Optional[_Union[UsersProto.User.MfaInfo, _Mapping]] = ..., allow_dso_modify: bool = ..., is_ui_support_user: bool = ..., role_type_vec: _Optional[_Iterable[_Union[UsersProto.User.Role, str]]] = ..., language_preference: _Optional[str] = ..., timezone: _Optional[str] = ...) -> None: ...
    class Group(_message.Message):
        __slots__ = ("name", "role_vec", "user_vec", "domain", "created_time_msecs", "last_updated_time_msecs", "description", "sid", "restricted", "tenant_id", "tenant_id_vec", "is_smb_principal_only", "smb_principal_vec")
        class SmbPrincipal(_message.Message):
            __slots__ = ("name", "domain", "sid", "type")
            NAME_FIELD_NUMBER: _ClassVar[int]
            DOMAIN_FIELD_NUMBER: _ClassVar[int]
            SID_FIELD_NUMBER: _ClassVar[int]
            TYPE_FIELD_NUMBER: _ClassVar[int]
            name: str
            domain: str
            sid: str
            type: str
            def __init__(self, name: _Optional[str] = ..., domain: _Optional[str] = ..., sid: _Optional[str] = ..., type: _Optional[str] = ...) -> None: ...
        NAME_FIELD_NUMBER: _ClassVar[int]
        ROLE_VEC_FIELD_NUMBER: _ClassVar[int]
        USER_VEC_FIELD_NUMBER: _ClassVar[int]
        DOMAIN_FIELD_NUMBER: _ClassVar[int]
        CREATED_TIME_MSECS_FIELD_NUMBER: _ClassVar[int]
        LAST_UPDATED_TIME_MSECS_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        SID_FIELD_NUMBER: _ClassVar[int]
        RESTRICTED_FIELD_NUMBER: _ClassVar[int]
        TENANT_ID_FIELD_NUMBER: _ClassVar[int]
        TENANT_ID_VEC_FIELD_NUMBER: _ClassVar[int]
        IS_SMB_PRINCIPAL_ONLY_FIELD_NUMBER: _ClassVar[int]
        SMB_PRINCIPAL_VEC_FIELD_NUMBER: _ClassVar[int]
        name: str
        role_vec: _containers.RepeatedScalarFieldContainer[str]
        user_vec: _containers.RepeatedScalarFieldContainer[str]
        domain: str
        created_time_msecs: int
        last_updated_time_msecs: int
        description: str
        sid: str
        restricted: bool
        tenant_id: str
        tenant_id_vec: _containers.RepeatedScalarFieldContainer[str]
        is_smb_principal_only: bool
        smb_principal_vec: _containers.RepeatedCompositeFieldContainer[UsersProto.Group.SmbPrincipal]
        def __init__(self, name: _Optional[str] = ..., role_vec: _Optional[_Iterable[str]] = ..., user_vec: _Optional[_Iterable[str]] = ..., domain: _Optional[str] = ..., created_time_msecs: _Optional[int] = ..., last_updated_time_msecs: _Optional[int] = ..., description: _Optional[str] = ..., sid: _Optional[str] = ..., restricted: bool = ..., tenant_id: _Optional[str] = ..., tenant_id_vec: _Optional[_Iterable[str]] = ..., is_smb_principal_only: bool = ..., smb_principal_vec: _Optional[_Iterable[_Union[UsersProto.Group.SmbPrincipal, _Mapping]]] = ...) -> None: ...
    class Role(_message.Message):
        __slots__ = ("name", "privilege_vec", "created_time_msecs", "last_updated_time_msecs", "description", "tenant_id")
        NAME_FIELD_NUMBER: _ClassVar[int]
        PRIVILEGE_VEC_FIELD_NUMBER: _ClassVar[int]
        CREATED_TIME_MSECS_FIELD_NUMBER: _ClassVar[int]
        LAST_UPDATED_TIME_MSECS_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        TENANT_ID_FIELD_NUMBER: _ClassVar[int]
        name: str
        privilege_vec: _containers.RepeatedScalarFieldContainer[str]
        created_time_msecs: int
        last_updated_time_msecs: int
        description: str
        tenant_id: str
        def __init__(self, name: _Optional[str] = ..., privilege_vec: _Optional[_Iterable[str]] = ..., created_time_msecs: _Optional[int] = ..., last_updated_time_msecs: _Optional[int] = ..., description: _Optional[str] = ..., tenant_id: _Optional[str] = ...) -> None: ...
    USER_VEC_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    GROUP_VEC_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_ROLE_VEC_FIELD_NUMBER: _ClassVar[int]
    LAST_RID_FIELD_NUMBER: _ClassVar[int]
    SEEDED_ROLE_VEC_FIELD_NUMBER: _ClassVar[int]
    SESSION_TABLE_FIELD_NUMBER: _ClassVar[int]
    ALLOW_UI_ACCESS_PRIVILEGE_UPGRADED_FIELD_NUMBER: _ClassVar[int]
    SMB_BACKUP_OPERATOR_ROLE_UPGRADED_FIELD_NUMBER: _ClassVar[int]
    user_vec: _containers.RepeatedCompositeFieldContainer[UsersProto.User]
    version: int
    group_vec: _containers.RepeatedCompositeFieldContainer[UsersProto.Group]
    custom_role_vec: _containers.RepeatedCompositeFieldContainer[UsersProto.Role]
    last_rid: int
    seeded_role_vec: _containers.RepeatedCompositeFieldContainer[UsersProto.Role]
    session_table: _containers.RepeatedCompositeFieldContainer[SessionTableEntry]
    allow_ui_access_privilege_upgraded: bool
    smb_backup_operator_role_upgraded: bool
    def __init__(self, user_vec: _Optional[_Iterable[_Union[UsersProto.User, _Mapping]]] = ..., version: _Optional[int] = ..., group_vec: _Optional[_Iterable[_Union[UsersProto.Group, _Mapping]]] = ..., custom_role_vec: _Optional[_Iterable[_Union[UsersProto.Role, _Mapping]]] = ..., last_rid: _Optional[int] = ..., seeded_role_vec: _Optional[_Iterable[_Union[UsersProto.Role, _Mapping]]] = ..., session_table: _Optional[_Iterable[_Union[SessionTableEntry, _Mapping]]] = ..., allow_ui_access_privilege_upgraded: bool = ..., smb_backup_operator_role_upgraded: bool = ...) -> None: ...

class SalesforceAccountInfo(_message.Message):
    __slots__ = ("account_id", "user_id")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    user_id: str
    def __init__(self, account_id: _Optional[str] = ..., user_id: _Optional[str] = ...) -> None: ...

class GoogleAccountInfo(_message.Message):
    __slots__ = ("account_id", "user_id")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    user_id: str
    def __init__(self, account_id: _Optional[str] = ..., user_id: _Optional[str] = ...) -> None: ...

class SessionTableEntry(_message.Message):
    __slots__ = ("username", "domain", "expiryTime", "sid")
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    EXPIRYTIME_FIELD_NUMBER: _ClassVar[int]
    SID_FIELD_NUMBER: _ClassVar[int]
    username: str
    domain: str
    expiryTime: int
    sid: str
    def __init__(self, username: _Optional[str] = ..., domain: _Optional[str] = ..., expiryTime: _Optional[int] = ..., sid: _Optional[str] = ...) -> None: ...

class LoginTime(_message.Message):
    __slots__ = ("sid", "last_login_time_msecs", "current_login_time_msecs")
    SID_FIELD_NUMBER: _ClassVar[int]
    LAST_LOGIN_TIME_MSECS_FIELD_NUMBER: _ClassVar[int]
    CURRENT_LOGIN_TIME_MSECS_FIELD_NUMBER: _ClassVar[int]
    sid: str
    last_login_time_msecs: int
    current_login_time_msecs: int
    def __init__(self, sid: _Optional[str] = ..., last_login_time_msecs: _Optional[int] = ..., current_login_time_msecs: _Optional[int] = ...) -> None: ...

class EmailOtpProto(_message.Message):
    __slots__ = ("email_otp_vec",)
    class EmailOtp(_message.Message):
        __slots__ = ("sid", "otp_code", "creation_time_msecs", "is_email_otp_setup_done", "num_wrong_attempts", "num_regeneration", "invalid_verify_time_msecs")
        SID_FIELD_NUMBER: _ClassVar[int]
        OTP_CODE_FIELD_NUMBER: _ClassVar[int]
        CREATION_TIME_MSECS_FIELD_NUMBER: _ClassVar[int]
        IS_EMAIL_OTP_SETUP_DONE_FIELD_NUMBER: _ClassVar[int]
        NUM_WRONG_ATTEMPTS_FIELD_NUMBER: _ClassVar[int]
        NUM_REGENERATION_FIELD_NUMBER: _ClassVar[int]
        INVALID_VERIFY_TIME_MSECS_FIELD_NUMBER: _ClassVar[int]
        sid: str
        otp_code: str
        creation_time_msecs: int
        is_email_otp_setup_done: bool
        num_wrong_attempts: int
        num_regeneration: int
        invalid_verify_time_msecs: int
        def __init__(self, sid: _Optional[str] = ..., otp_code: _Optional[str] = ..., creation_time_msecs: _Optional[int] = ..., is_email_otp_setup_done: bool = ..., num_wrong_attempts: _Optional[int] = ..., num_regeneration: _Optional[int] = ..., invalid_verify_time_msecs: _Optional[int] = ...) -> None: ...
    EMAIL_OTP_VEC_FIELD_NUMBER: _ClassVar[int]
    email_otp_vec: _containers.RepeatedCompositeFieldContainer[EmailOtpProto.EmailOtp]
    def __init__(self, email_otp_vec: _Optional[_Iterable[_Union[EmailOtpProto.EmailOtp, _Mapping]]] = ...) -> None: ...
