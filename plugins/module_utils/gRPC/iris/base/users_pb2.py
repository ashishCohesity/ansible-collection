# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: iris/base/users.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15iris/base/users.proto\x12\rcohesity.iris\"\xde\x16\n\nUsersProto\x12\x30\n\x08user_vec\x18\x01 \x03(\x0b\x32\x1e.cohesity.iris.UsersProto.User\x12\x12\n\x07version\x18\x02 \x01(\x05:\x01\x31\x12\x32\n\tgroup_vec\x18\x03 \x03(\x0b\x32\x1f.cohesity.iris.UsersProto.Group\x12\x37\n\x0f\x63ustom_role_vec\x18\x04 \x03(\x0b\x32\x1e.cohesity.iris.UsersProto.Role\x12\x13\n\x08last_rid\x18\x05 \x01(\r:\x01\x31\x12\x37\n\x0fseeded_role_vec\x18\x06 \x03(\x0b\x32\x1e.cohesity.iris.UsersProto.Role\x12\x37\n\rsession_table\x18\x07 \x03(\x0b\x32 .cohesity.iris.SessionTableEntry\x12*\n\"allow_ui_access_privilege_upgraded\x18\x08 \x01(\x08\x12)\n!smb_backup_operator_role_upgraded\x18\t \x01(\x08\x1a\x84\x0f\n\x04User\x12\x10\n\x08username\x18\x01 \x02(\t\x12\x10\n\x08password\x18\x02 \x01(\x0c\x12\x15\n\rraw_smb_token\x18\x18 \x01(\x0c\x12\x1f\n\x17ntlm_encrypted_password\x18\x14 \x01(\x0c\x12\x15\n\x06\x64omain\x18\x03 \x02(\t:\x05LOCAL\x12\x15\n\remail_address\x18\x04 \x01(\t\x12\x12\n\nfirst_name\x18\x05 \x01(\t\x12\x11\n\tlast_name\x18\x06 \x01(\t\x12R\n\x16s3_portal_account_info\x18\x0e \x01(\x0b\x32\x32.cohesity.iris.UsersProto.User.S3PortalAccountInfo\x12\x1a\n\x12\x63reated_time_msecs\x18\x08 \x02(\x03\x12\x1f\n\x17last_updated_time_msecs\x18\t \x01(\x03\x12\x19\n\x11\x65xpired_time_msec\x18\x15 \x01(\x03\x12\x1c\n\x14\x65\x66\x66\x65\x63tive_time_msecs\x18\n \x01(\x03\x12\x13\n\x0b\x64\x65scription\x18\x0b \x01(\t\x12\x10\n\x08role_vec\x18\x0f \x03(\t\x12\x0b\n\x03sid\x18\x10 \x01(\t\x12\x19\n\x11primary_group_sid\x18\x16 \x01(\t\x12\x12\n\nrestricted\x18\x11 \x01(\x08\x12\x11\n\ttenant_id\x18\x12 \x01(\t\x12\x45\n\x17salesforce_account_info\x18\x13 \x01(\x0b\x32$.cohesity.iris.SalesforceAccountInfo\x12=\n\x13google_account_info\x18\x17 \x01(\x0b\x32 .cohesity.iris.GoogleAccountInfo\x12$\n\x15\x66orce_password_change\x18\x19 \x01(\x08:\x05\x66\x61lse\x12<\n\ruser_api_keys\x18\x1a \x03(\x0b\x32%.cohesity.iris.UsersProto.User.ApiKey\x12$\n\x1clast_password_set_time_msecs\x18\x1b \x01(\x03\x12\x1a\n\x12previous_passwords\x18\x1c \x03(\x0c\x12\x1e\n\x16invalid_login_attempts\x18\x1d \x01(\x05\x12 \n\x18invalid_login_time_msecs\x18\x1e \x01(\x03\x12\x19\n\x11is_account_locked\x18\x1f \x01(\x08\x12\"\n\x13is_account_disabled\x18  \x01(\x08:\x05\x66\x61lse\x12(\n last_successful_login_time_msecs\x18! \x01(\x03\x12\x38\n\x08mfa_info\x18# \x01(\x0b\x32&.cohesity.iris.UsersProto.User.MfaInfo\x12\x18\n\x10\x61llow_dso_modify\x18$ \x01(\x08\x12!\n\x12is_ui_support_user\x18% \x01(\x08:\x05\x66\x61lse\x12>\n\rrole_type_vec\x18\x07 \x03(\x0e\x32#.cohesity.iris.UsersProto.User.RoleB\x02\x18\x01\x12\x1f\n\x13language_preference\x18\x0c \x01(\tB\x02\x18\x01\x12\x14\n\x08timezone\x18\r \x01(\tB\x02\x18\x01\x1a\x62\n\x13S3PortalAccountInfo\x12\x19\n\x11\x63\x61nonical_user_id\x18\x01 \x01(\t\x12\x15\n\raccess_key_id\x18\x02 \x01(\x0c\x12\x19\n\x11secret_access_key\x18\x03 \x01(\x0c\x1a\x89\x02\n\x06\x41piKey\x12\n\n\x02id\x18\x01 \x02(\t\x12\x12\n\nhashed_key\x18\x02 \x02(\t\x12\x0c\n\x04name\x18\x03 \x02(\t\x12\x1a\n\x12\x63reated_time_msecs\x18\x04 \x01(\x03\x12\x18\n\x10\x63reated_user_sid\x18\x05 \x01(\t\x12\x18\n\x10\x63reated_username\x18\x06 \x01(\t\x12\x16\n\x0eowner_user_sid\x18\x07 \x01(\t\x12\x16\n\x0eowner_username\x18\x08 \x01(\t\x12\x1d\n\x15\x65xpiration_time_msecs\x18\t \x01(\x03\x12\x1f\n\x17last_rotated_time_msecs\x18\n \x01(\x03\x12\x11\n\tis_active\x18\x0b \x01(\x08\x1ag\n\x07TotpKey\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x12\x12\n\nsecret_key\x18\x03 \x01(\x0c\x12\x0b\n\x03uri\x18\x04 \x01(\x0c\x12!\n\x12is_totp_setup_done\x18\x05 \x01(\x08:\x05\x66\x61lse\x1a\xab\x01\n\x07MfaInfo\x12&\n\x17is_user_exempt_from_mfa\x18\x01 \x01(\x08:\x05\x66\x61lse\x12\x39\n\ttotp_keys\x18\x02 \x03(\x0b\x32&.cohesity.iris.UsersProto.User.TotpKey\x12\x1a\n\x12num_wrong_attempts\x18\x03 \x01(\x05\x12!\n\x19invalid_verify_time_msecs\x18\x04 \x01(\x03\"?\n\x04Role\x12\x11\n\rkClusterAdmin\x10\x01\x12\x10\n\x0ckClusterUser\x10\x02\x12\x12\n\x0ekClusterViewer\x10\x03\x1a\xa4\x03\n\x05Group\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x10\n\x08role_vec\x18\x02 \x03(\t\x12\x10\n\x08user_vec\x18\x03 \x03(\t\x12\x15\n\x06\x64omain\x18\x04 \x02(\t:\x05LOCAL\x12\x1a\n\x12\x63reated_time_msecs\x18\x05 \x01(\x03\x12\x1f\n\x17last_updated_time_msecs\x18\x06 \x01(\x03\x12\x13\n\x0b\x64\x65scription\x18\x07 \x01(\t\x12\x0b\n\x03sid\x18\x08 \x01(\t\x12\x12\n\nrestricted\x18\t \x01(\x08\x12\x11\n\ttenant_id\x18\n \x01(\t\x12\x15\n\rtenant_id_vec\x18\r \x03(\t\x12\x1d\n\x15is_smb_principal_only\x18\x0b \x01(\x08\x12G\n\x11smb_principal_vec\x18\x0c \x03(\x0b\x32,.cohesity.iris.UsersProto.Group.SmbPrincipal\x1aM\n\x0cSmbPrincipal\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06\x64omain\x18\x02 \x01(\t\x12\x0b\n\x03sid\x18\x03 \x01(\t\x12\x12\n\x04type\x18\x04 \x01(\t:\x04User\x1a\x90\x01\n\x04Role\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x15\n\rprivilege_vec\x18\x02 \x03(\t\x12\x1a\n\x12\x63reated_time_msecs\x18\x03 \x02(\x03\x12\x1f\n\x17last_updated_time_msecs\x18\x04 \x01(\x03\x12\x13\n\x0b\x64\x65scription\x18\x05 \x01(\t\x12\x11\n\ttenant_id\x18\x06 \x01(\t\"<\n\x15SalesforceAccountInfo\x12\x12\n\naccount_id\x18\x01 \x01(\t\x12\x0f\n\x07user_id\x18\x02 \x01(\t\"8\n\x11GoogleAccountInfo\x12\x12\n\naccount_id\x18\x01 \x01(\t\x12\x0f\n\x07user_id\x18\x02 \x01(\t\"V\n\x11SessionTableEntry\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x0e\n\x06\x64omain\x18\x02 \x01(\t\x12\x12\n\nexpiryTime\x18\x03 \x01(\x03\x12\x0b\n\x03sid\x18\x04 \x01(\t\"Y\n\tLoginTime\x12\x0b\n\x03sid\x18\x01 \x01(\t\x12\x1d\n\x15last_login_time_msecs\x18\x02 \x01(\x03\x12 \n\x18\x63urrent_login_time_msecs\x18\x03 \x01(\x03\"\x97\x02\n\rEmailOtpProto\x12<\n\remail_otp_vec\x18\x01 \x03(\x0b\x32%.cohesity.iris.EmailOtpProto.EmailOtp\x1a\xc7\x01\n\x08\x45mailOtp\x12\x0b\n\x03sid\x18\x01 \x01(\t\x12\x10\n\x08otp_code\x18\x02 \x01(\t\x12\x1b\n\x13\x63reation_time_msecs\x18\x03 \x01(\x03\x12&\n\x17is_email_otp_setup_done\x18\x04 \x01(\x08:\x05\x66\x61lse\x12\x1a\n\x12num_wrong_attempts\x18\x05 \x01(\x05\x12\x18\n\x10num_regeneration\x18\x06 \x01(\x05\x12!\n\x19invalid_verify_time_msecs\x18\x07 \x01(\x03\x42\x14Z\x12iris/base/users.pb')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'iris.base.users_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\022iris/base/users.pb'
  _globals['_USERSPROTO_USER'].fields_by_name['role_type_vec']._loaded_options = None
  _globals['_USERSPROTO_USER'].fields_by_name['role_type_vec']._serialized_options = b'\030\001'
  _globals['_USERSPROTO_USER'].fields_by_name['language_preference']._loaded_options = None
  _globals['_USERSPROTO_USER'].fields_by_name['language_preference']._serialized_options = b'\030\001'
  _globals['_USERSPROTO_USER'].fields_by_name['timezone']._loaded_options = None
  _globals['_USERSPROTO_USER'].fields_by_name['timezone']._serialized_options = b'\030\001'
  _globals['_USERSPROTO']._serialized_start=41
  _globals['_USERSPROTO']._serialized_end=2951
  _globals['_USERSPROTO_USER']._serialized_start=457
  _globals['_USERSPROTO_USER']._serialized_end=2381
  _globals['_USERSPROTO_USER_S3PORTALACCOUNTINFO']._serialized_start=1671
  _globals['_USERSPROTO_USER_S3PORTALACCOUNTINFO']._serialized_end=1769
  _globals['_USERSPROTO_USER_APIKEY']._serialized_start=1772
  _globals['_USERSPROTO_USER_APIKEY']._serialized_end=2037
  _globals['_USERSPROTO_USER_TOTPKEY']._serialized_start=2039
  _globals['_USERSPROTO_USER_TOTPKEY']._serialized_end=2142
  _globals['_USERSPROTO_USER_MFAINFO']._serialized_start=2145
  _globals['_USERSPROTO_USER_MFAINFO']._serialized_end=2316
  _globals['_USERSPROTO_USER_ROLE']._serialized_start=2318
  _globals['_USERSPROTO_USER_ROLE']._serialized_end=2381
  _globals['_USERSPROTO_GROUP']._serialized_start=2384
  _globals['_USERSPROTO_GROUP']._serialized_end=2804
  _globals['_USERSPROTO_GROUP_SMBPRINCIPAL']._serialized_start=2727
  _globals['_USERSPROTO_GROUP_SMBPRINCIPAL']._serialized_end=2804
  _globals['_USERSPROTO_ROLE']._serialized_start=2807
  _globals['_USERSPROTO_ROLE']._serialized_end=2951
  _globals['_SALESFORCEACCOUNTINFO']._serialized_start=2953
  _globals['_SALESFORCEACCOUNTINFO']._serialized_end=3013
  _globals['_GOOGLEACCOUNTINFO']._serialized_start=3015
  _globals['_GOOGLEACCOUNTINFO']._serialized_end=3071
  _globals['_SESSIONTABLEENTRY']._serialized_start=3073
  _globals['_SESSIONTABLEENTRY']._serialized_end=3159
  _globals['_LOGINTIME']._serialized_start=3161
  _globals['_LOGINTIME']._serialized_end=3250
  _globals['_EMAILOTPPROTO']._serialized_start=3253
  _globals['_EMAILOTPPROTO']._serialized_end=3532
  _globals['_EMAILOTPPROTO_EMAILOTP']._serialized_start=3333
  _globals['_EMAILOTPPROTO_EMAILOTP']._serialized_end=3532
# @@protoc_insertion_point(module_scope)