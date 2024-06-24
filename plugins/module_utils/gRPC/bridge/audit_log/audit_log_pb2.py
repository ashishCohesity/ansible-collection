# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bridge/audit_log/audit_log.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from bridge.s3_portal.base import s3_enums_pb2 as bridge_dot_s3__portal_dot_base_dot_s3__enums__pb2
from bridge.s3_portal.base import s3_error_pb2 as bridge_dot_s3__portal_dot_base_dot_s3__error__pb2
from bridge.snap_fs import entity_handle_pb2 as bridge_dot_snap__fs_dot_entity__handle__pb2
from bridge.snap_fs import snap_fs_metadata_pb2 as bridge_dot_snap__fs_dot_snap__fs__metadata__pb2
from configs import cluster_config_pb2 as configs_dot_cluster__config__pb2
from yoda.es import jsonname_pb2 as yoda_dot_es_dot_jsonname__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n bridge/audit_log/audit_log.proto\x12\x19\x63ohesity.bridge.audit_log\x1a$bridge/s3_portal/base/s3_enums.proto\x1a$bridge/s3_portal/base/s3_error.proto\x1a\"bridge/snap_fs/entity_handle.proto\x1a%bridge/snap_fs/snap_fs_metadata.proto\x1a\x1c\x63onfigs/cluster_config.proto\x1a\x16yoda/es/jsonname.proto\"\xbb\x01\n\x0cUserIdentity\x12\x11\n\tuser_name\x18\x01 \x01(\t\x12\x13\n\x0b\x64omain_name\x18\x02 \x01(\t\x12\x18\n\x10is_guest_session\x18\x03 \x01(\x08\x12\x1c\n\x14is_anonymous_session\x18\x04 \x01(\x08\x12\x0f\n\x07user_id\x18\x05 \x01(\r\x12:\n\x08user_sid\x18\x06 \x01(\x0b\x32(.cohesity.configs.ClusterConfigProto.SID\"5\n\rAuditRecordId\x12\x12\n\nsession_id\x18\x01 \x01(\x03\x12\x10\n\x08local_id\x18\x02 \x01(\x03\"\x93\x02\n\x0e\x46ileAttributes\x12\x0c\n\x04mode\x18\x01 \x01(\r\x12\x0f\n\x07user_id\x18\x02 \x01(\r\x12\x10\n\x08group_id\x18\x03 \x01(\r\x12\x12\n\nsize_bytes\x18\x04 \x01(\x03\x12\x13\n\x0bmtime_usecs\x18\x05 \x01(\x03\x12[\n\x13\x65xtended_attributes\x18\x06 \x01(\x0b\x32>.cohesity.bridge.snap_fs.InodeMetadataProto.ExtendedAttributes\x12\x18\n\x10\x66ile_access_mask\x18\x07 \x01(\r\x12\x1b\n\x13\x63reation_time_usecs\x18\x08 \x01(\x03\x12\x13\n\x0b\x61time_usecs\x18\t \x01(\x03\"B\n\nS3Response\x12\x0c\n\x04\x65tag\x18\x01 \x01(\t\x12\x11\n\tupload_id\x18\x02 \x01(\x03\x12\x13\n\x0bpart_number\x18\x03 \x01(\x03\"\xef\r\n\x0b\x41uditRecord\x12\x34\n\x02id\x18\x01 \x01(\x0b\x32(.cohesity.bridge.audit_log.AuditRecordId\x12\x17\n\x0ftimestamp_usecs\x18\x02 \x01(\x03\x12\x41\n\rentity_handle\x18\x03 \x01(\x0b\x32*.cohesity.bridge.snap_fs.EntityHandleProto\x12\x11\n\tview_name\x18\x04 \x01(\t\x12\x17\n\x0fview_alias_name\x18\x15 \x01(\t\x12>\n\ruser_identity\x18\x05 \x01(\x0b\x32\'.cohesity.bridge.audit_log.UserIdentity\x12\x11\n\tclient_ip\x18\x06 \x01(\t\x12\x41\n\x08protocol\x18\x07 \x01(\x0e\x32/.cohesity.bridge.audit_log.AuditRecord.Protocol\x12H\n\x0crequest_type\x18\x08 \x01(\x0e\x32\x32.cohesity.bridge.audit_log.AuditRecord.RequestType\x12\x1b\n\x13mnt_response_status\x18\t \x01(\x03\x12\x1b\n\x13nfs_response_status\x18\n \x01(\x03\x12\x1b\n\x13smb_response_status\x18\x0b \x01(\r\x12\x1e\n\x16\x62ridge_response_status\x18\x1a \x01(\r\x12\x0c\n\x04path\x18\x0c \x01(\t\x12\x42\n\tfile_type\x18\r \x01(\x0e\x32/.cohesity.bridge.audit_log.AuditRecord.FileType\x12<\n\tfile_attr\x18\x0e \x01(\x0b\x32).cohesity.bridge.audit_log.FileAttributes\x12\x41\n\x0eprev_file_attr\x18\x14 \x01(\x0b\x32).cohesity.bridge.audit_log.FileAttributes\x12\x11\n\tdest_path\x18\x0f \x01(\t\x12\x46\n\x12\x64\x65st_entity_handle\x18\x10 \x01(\x0b\x32*.cohesity.bridge.snap_fs.EntityHandleProto\x12\x17\n\x0f\x64\x65lete_on_close\x18\x11 \x01(\x08\x12\x39\n\x0fs3_request_type\x18\x12 \x01(\x0e\x32 .cohesity.bridge.s3.Request.Type\x12\x41\n\x12s3_response_status\x18\x13 \x01(\x0e\x32%.cohesity.bridge.s3.S3ErrorProto.Code\x12O\n\x1bsource_parent_entity_handle\x18\x16 \x01(\x0b\x32*.cohesity.bridge.snap_fs.EntityHandleProto\x12:\n\x0bs3_response\x18\x17 \x01(\x0b\x32%.cohesity.bridge.audit_log.S3Response\x12)\n\x1bshould_publish_audit_record\x18\x18 \x01(\x08:\x04true\x12,\n\x1dshould_log_filer_event_record\x18\x19 \x01(\x08:\x05\x66\x61lse\x12\x13\n\x0blcm_rule_id\x18\x1d \x01(\t\x12J\n\x14\x64\x64w_portal_audit_log\x18\x1e \x01(\x0b\x32,.cohesity.bridge.audit_log.DdwPortalAuditLog\"Q\n\x08Protocol\x12\x08\n\x04kSMB\x10\x00\x12\t\n\x05kNFS3\x10\x01\x12\x07\n\x03kS3\x10\x02\x12\n\n\x06kSwift\x10\x03\x12\x0b\n\x07kSnapFS\x10\x04\x12\x0e\n\nkDdwPortal\x10\x05\"\xeb\x01\n\x0bRequestType\x12\n\n\x06kLogOn\x10\x00\x12\x0b\n\x07kLogOff\x10\x01\x12\n\n\x06kMount\x10\x02\x12\t\n\x05kOpen\x10\x03\x12\x0b\n\x07kCreate\x10\x04\x12\n\n\x06kClose\x10\x05\x12\x0b\n\x07kDelete\x10\x06\x12\x0b\n\x07kRename\x10\x07\x12\x12\n\x0ekSetAttributes\x10\x08\x12\x0b\n\x07kCommit\x10\t\x12\x0b\n\x07kUmount\x10\n\x12\x15\n\x11kQuarantineThreat\x10\x0b\x12\x17\n\x13kUnquarantineThreat\x10\x0c\x12\x10\n\x0ckResetThreat\x10\r\x12\t\n\x05kRead\x10\x0e\"~\n\x08\x46ileType\x12\t\n\x05kFile\x10\x01\x12\x0e\n\nkDirectory\x10\x02\x12\x10\n\x0ckBlockDevice\x10\x03\x12\x14\n\x10kCharacterDevice\x10\x04\x12\x0c\n\x08kSymLink\x10\x05\x12\t\n\x05kLink\x10\x06\x12\x0b\n\x07kSocket\x10\x07\x12\t\n\x05kPipe\x10\x08\"\xd3\x0f\n\x14\x46ormattedAuditRecord\x12 \n\ttimestamp\x18\x01 \x01(\tB\r\x92\xb5\x18\tTimestamp\x12\x1f\n\trecord_id\x18\x02 \x01(\tB\x0c\x92\xb5\x18\x08RecordID\x12\x1e\n\x08protocol\x18\x03 \x01(\tB\x0c\x92\xb5\x18\x08Protocol\x12\x1f\n\tclient_ip\x18\x04 \x01(\tB\x0c\x92\xb5\x18\x08\x43lientIP\x12\x1f\n\tuser_name\x18\x05 \x01(\tB\x0c\x92\xb5\x18\x08UserName\x12\x1b\n\x07user_id\x18\x06 \x01(\x05\x42\n\x92\xb5\x18\x06UserID\x12#\n\x0b\x64omain_name\x18\x07 \x01(\tB\x0e\x92\xb5\x18\nDomainName\x12\x1d\n\x08user_sid\x18\x08 \x01(\tB\x0b\x92\xb5\x18\x07UserSID\x12\x1f\n\tview_name\x18\t \x01(\tB\x0c\x92\xb5\x18\x08ViewName\x12*\n\x0fview_alias_name\x18\x1e \x01(\tB\x11\x92\xb5\x18\rViewAliasName\x12\x16\n\x04\x66sid\x18\x1c \x01(\x03\x42\x08\x92\xb5\x18\x04\x46sid\x12%\n\x0crequest_type\x18\n \x01(\tB\x0f\x92\xb5\x18\x0bRequestType\x12\x1a\n\x06result\x18\x0b \x01(\tB\n\x92\xb5\x18\x06Result\x12#\n\x0b\x65ntity_type\x18\x0c \x01(\tB\x0e\x92\xb5\x18\nEntityType\x12#\n\x0b\x65ntity_path\x18\r \x01(\tB\x0e\x92\xb5\x18\nEntityPath\x12%\n\x0c\x65ntity_inode\x18\x0e \x01(\x03\x42\x0f\x92\xb5\x18\x0b\x45ntityInode\x12#\n\x0b\x65ntity_mode\x18\x0f \x01(\rB\x0e\x92\xb5\x18\nEntityMode\x12(\n\x0e\x65ntity_user_id\x18\x10 \x01(\rB\x10\x92\xb5\x18\x0c\x45ntityUserID\x12*\n\x0f\x65ntity_group_id\x18\x11 \x01(\rB\x11\x92\xb5\x18\rEntityGroupID\x12:\n\x17\x65ntity_modify_timestamp\x18\x12 \x01(\tB\x19\x92\xb5\x18\x15\x45ntityModifyTimestamp\x12\x30\n\x12\x65ntity_access_mask\x18\x13 \x01(\rB\x14\x92\xb5\x18\x10\x45ntityAccessMask\x12:\n\x17\x64\x65stination_entity_path\x18\x14 \x01(\tB\x19\x92\xb5\x18\x15\x44\x65stinationEntityPath\x12<\n\x18\x64\x65stination_entity_inode\x18\x15 \x01(\x03\x42\x1a\x92\xb5\x18\x16\x44\x65stinationEntityInode\x12*\n\x0f\x64\x65lete_on_close\x18\x16 \x01(\x08\x42\x11\x92\xb5\x18\rDeleteOnClose\x12\x38\n\x18smb2_security_descriptor\x18\x17 \x01(\tB\x16\x92\xb5\x18\x12SecurityDescriptor\x12o\n\x13security_descriptor\x18  \x01(\x0b\x32:.cohesity.bridge.audit_log.FormattedSmb2SecurityDescriptorB\x16\x92\xb5\x18\x12SecurityDescriptor\x12\x41\n\x1dprev_smb2_security_descriptor\x18\x1b \x01(\tB\x1a\x92\xb5\x18\x16PrevSecurityDescriptor\x12x\n\x18prev_security_descriptor\x18! \x01(\x0b\x32:.cohesity.bridge.audit_log.FormattedSmb2SecurityDescriptorB\x1a\x92\xb5\x18\x16PrevSecurityDescriptor\x12,\n\x10prev_entity_mode\x18\x18 \x01(\rB\x12\x92\xb5\x18\x0ePrevEntityMode\x12\x31\n\x13prev_entity_user_id\x18\x19 \x01(\x05\x42\x14\x92\xb5\x18\x10PrevEntityUserID\x12\x33\n\x14prev_entity_group_id\x18\x1a \x01(\x05\x42\x15\x92\xb5\x18\x11PrevEntityGroupID\x12,\n\x10inode_size_bytes\x18\x1d \x01(\x03\x42\x12\x92\xb5\x18\x0eInodeSizeBytes\x12?\n\x1asource_parent_entity_inode\x18\x1f \x01(\x03\x42\x1b\x92\xb5\x18\x17SourceParentEntityInode\x12\x16\n\x04\x65tag\x18\" \x01(\tB\x08\x92\xb5\x18\x04\x45Tag\x12\x1f\n\tupload_id\x18# \x01(\x03\x42\x0c\x92\xb5\x18\x08UploadId\x12#\n\x0bpart_number\x18$ \x01(\x03\x42\x0e\x92\xb5\x18\nPartNumber\x12j\n\x14\x64\x64w_portal_audit_log\x18) \x01(\x0b\x32\x35.cohesity.bridge.audit_log.FormattedDdwPortalAuditLogB\x15\x92\xb5\x18\x11\x44\x64wPortalAuditLog\x12&\n\rlcm_rule_name\x18* \x01(\tB\x0f\x92\xb5\x18\x0bLCMRuleName\x12>\n\x19\x65ntity_creation_timestamp\x18+ \x01(\tB\x1b\x92\xb5\x18\x17\x45ntityCreationTimestamp\x12:\n\x17\x65ntity_access_timestamp\x18, \x01(\tB\x19\x92\xb5\x18\x15\x45ntityAccessTimestampJ\x04\x08%\x10&J\x04\x08&\x10\'R\x0cs3_audit_logR\x18s3_audit_log_copy_source\"\x89\x01\n\x0c\x46ormattedACE\x12\x1d\n\x08\x61\x63\x65_type\x18\x01 \x02(\x05\x42\x0b\x92\xb5\x18\x07\x41\x63\x65Type\x12\x1f\n\tace_flags\x18\x02 \x02(\x05\x42\x0c\x92\xb5\x18\x08\x41\x63\x65\x46lags\x12#\n\x0b\x61\x63\x63\x65ss_mask\x18\x03 \x02(\rB\x0e\x92\xb5\x18\nAccessMask\x12\x14\n\x03sid\x18\x04 \x02(\tB\x07\x92\xb5\x18\x03Sid\"\xc4\x01\n\x1f\x46ormattedSmb2SecurityDescriptor\x12\x1c\n\x07\x63ontrol\x18\x01 \x02(\rB\x0b\x92\xb5\x18\x07\x43ontrol\x12\x1f\n\towner_sid\x18\x02 \x01(\tB\x0c\x92\xb5\x18\x08OwnerSid\x12\x1f\n\tgroup_sid\x18\x03 \x01(\tB\x0c\x92\xb5\x18\x08GroupSid\x12\x41\n\x05\x64\x61\x63ls\x18\x04 \x03(\x0b\x32\'.cohesity.bridge.audit_log.FormattedACEB\t\x92\xb5\x18\x05\x44\x61\x63ls\"\xef\x02\n\x11\x44\x64wPortalAuditLog\x12\x11\n\tfile_name\x18\x01 \x01(\t\x12\x12\n\nstart_time\x18\x02 \x01(\x03\x12\x10\n\x08\x65nd_time\x18\x03 \x01(\x03\x12\x11\n\tfile_size\x18\x04 \x01(\x03\x12\x11\n\tread_size\x18\x05 \x01(\x03\x12\x43\n\x06status\x18\x06 \x01(\x0e\x32\x33.cohesity.bridge.audit_log.DdwPortalAuditLog.Status\x12L\n\x0bsource_type\x18\x07 \x01(\x0e\x32\x37.cohesity.bridge.audit_log.DdwPortalAuditLog.SourceType\x12\x0b\n\x03tag\x18\x08 \x01(\t\"5\n\x06Status\x12\x0f\n\x0bkInProgress\x10\x00\x12\x0c\n\x08kSuccess\x10\x01\x12\x0c\n\x08kFailure\x10\x02\"$\n\nSourceType\x12\x0c\n\x08kGeneral\x10\x00\x12\x08\n\x04kSBT\x10\x01\"\x98\x02\n\x1a\x46ormattedDdwPortalAuditLog\x12\x1f\n\tfile_name\x18\x01 \x01(\tB\x0c\x92\xb5\x18\x08\x46ileName\x12!\n\nstart_time\x18\x02 \x01(\x03\x42\r\x92\xb5\x18\tStartTime\x12\x1d\n\x08\x65nd_time\x18\x03 \x01(\x03\x42\x0b\x92\xb5\x18\x07\x45ndTime\x12\x1f\n\tfile_size\x18\x04 \x01(\x03\x42\x0c\x92\xb5\x18\x08\x46ileSize\x12\x1f\n\tread_size\x18\x05 \x01(\x03\x42\x0c\x92\xb5\x18\x08ReadSize\x12\x1a\n\x06status\x18\x06 \x01(\tB\n\x92\xb5\x18\x06Status\x12#\n\x0bsource_type\x18\x07 \x01(\tB\x0e\x92\xb5\x18\nSourceType\x12\x14\n\x03tag\x18\x08 \x01(\tB\x07\x92\xb5\x18\x03TagB\x1fZ\x1d\x62ridge/audit_log/audit_log.pb')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'bridge.audit_log.audit_log_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\035bridge/audit_log/audit_log.pb'
  _globals['_FORMATTEDAUDITRECORD'].fields_by_name['timestamp']._loaded_options = None
  _globals['_FORMATTEDAUDITRECORD'].fields_by_name['timestamp']._serialized_options = b'\222\265\030\tTimestamp'
  _globals['_FORMATTEDAUDITRECORD'].fields_by_name['record_id']._loaded_options = None
  _globals['_FORMATTEDAUDITRECORD'].fields_by_name['record_id']._serialized_options = b'\222\265\030\010RecordID'
  _globals['_FORMATTEDAUDITRECORD'].fields_by_name['protocol']._loaded_options = None
  _globals['_FORMATTEDAUDITRECORD'].fields_by_name['protocol']._serialized_options = b'\222\265\030\010Protocol'
  _globals['_FORMATTEDAUDITRECORD'].fields_by_name['client_ip']._loaded_options = None
  _globals['_FORMATTEDAUDITRECORD'].fields_by_name['client_ip']._serialized_options = b'\222\265\030\010ClientIP'
  _globals['_FORMATTEDAUDITRECORD'].fields_by_name['user_name']._loaded_options = None
  _globals['_FORMATTEDAUDITRECORD'].fields_by_name['user_name']._serialized_options = b'\222\265\030\010UserName'
  _globals['_FORMATTEDAUDITRECORD'].fields_by_name['user_id']._loaded_options = None
  _globals['_FORMATTEDAUDITRECORD'].fields_by_name['user_id']._serialized_options = b'\222\265\030\006UserID'
  _globals['_FORMATTEDAUDITRECORD'].fields_by_name['domain_name']._loaded_options = None
  _globals['_FORMATTEDAUDITRECORD'].fields_by_name['domain_name']._serialized_options = b'\222\265\030\nDomainName'
  _globals['_FORMATTEDAUDITRECORD'].fields_by_name['user_sid']._loaded_options = None
  _globals['_FORMATTEDAUDITRECORD'].fields_by_name['user_sid']._serialized_options = b'\222\265\030\007UserSID'
  _globals['_FORMATTEDAUDITRECORD'].fields_by_name['view_name']._loaded_options = None
  _globals['_FORMATTEDAUDITRECORD'].fields_by_name['view_name']._serialized_options = b'\222\265\030\010ViewName'
  _globals['_FORMATTEDAUDITRECORD'].fields_by_name['view_alias_name']._loaded_options = None
  _globals['_FORMATTEDAUDITRECORD'].fields_by_name['view_alias_name']._serialized_options = b'\222\265\030\rViewAliasName'
  _globals['_FORMATTEDAUDITRECORD'].fields_by_name['fsid']._loaded_options = None
  _globals['_FORMATTEDAUDITRECORD'].fields_by_name['fsid']._serialized_options = b'\222\265\030\004Fsid'
  _globals['_FORMATTEDAUDITRECORD'].fields_by_name['request_type']._loaded_options = None
  _globals['_FORMATTEDAUDITRECORD'].fields_by_name['request_type']._serialized_options = b'\222\265\030\013RequestType'
  _globals['_FORMATTEDAUDITRECORD'].fields_by_name['result']._loaded_options = None
  _globals['_FORMATTEDAUDITRECORD'].fields_by_name['result']._serialized_options = b'\222\265\030\006Result'
  _globals['_FORMATTEDAUDITRECORD'].fields_by_name['entity_type']._loaded_options = None
  _globals['_FORMATTEDAUDITRECORD'].fields_by_name['entity_type']._serialized_options = b'\222\265\030\nEntityType'
  _globals['_FORMATTEDAUDITRECORD'].fields_by_name['entity_path']._loaded_options = None
  _globals['_FORMATTEDAUDITRECORD'].fields_by_name['entity_path']._serialized_options = b'\222\265\030\nEntityPath'
  _globals['_FORMATTEDAUDITRECORD'].fields_by_name['entity_inode']._loaded_options = None
  _globals['_FORMATTEDAUDITRECORD'].fields_by_name['entity_inode']._serialized_options = b'\222\265\030\013EntityInode'
  _globals['_FORMATTEDAUDITRECORD'].fields_by_name['entity_mode']._loaded_options = None
  _globals['_FORMATTEDAUDITRECORD'].fields_by_name['entity_mode']._serialized_options = b'\222\265\030\nEntityMode'
  _globals['_FORMATTEDAUDITRECORD'].fields_by_name['entity_user_id']._loaded_options = None
  _globals['_FORMATTEDAUDITRECORD'].fields_by_name['entity_user_id']._serialized_options = b'\222\265\030\014EntityUserID'
  _globals['_FORMATTEDAUDITRECORD'].fields_by_name['entity_group_id']._loaded_options = None
  _globals['_FORMATTEDAUDITRECORD'].fields_by_name['entity_group_id']._serialized_options = b'\222\265\030\rEntityGroupID'
  _globals['_FORMATTEDAUDITRECORD'].fields_by_name['entity_modify_timestamp']._loaded_options = None
  _globals['_FORMATTEDAUDITRECORD'].fields_by_name['entity_modify_timestamp']._serialized_options = b'\222\265\030\025EntityModifyTimestamp'
  _globals['_FORMATTEDAUDITRECORD'].fields_by_name['entity_access_mask']._loaded_options = None
  _globals['_FORMATTEDAUDITRECORD'].fields_by_name['entity_access_mask']._serialized_options = b'\222\265\030\020EntityAccessMask'
  _globals['_FORMATTEDAUDITRECORD'].fields_by_name['destination_entity_path']._loaded_options = None
  _globals['_FORMATTEDAUDITRECORD'].fields_by_name['destination_entity_path']._serialized_options = b'\222\265\030\025DestinationEntityPath'
  _globals['_FORMATTEDAUDITRECORD'].fields_by_name['destination_entity_inode']._loaded_options = None
  _globals['_FORMATTEDAUDITRECORD'].fields_by_name['destination_entity_inode']._serialized_options = b'\222\265\030\026DestinationEntityInode'
  _globals['_FORMATTEDAUDITRECORD'].fields_by_name['delete_on_close']._loaded_options = None
  _globals['_FORMATTEDAUDITRECORD'].fields_by_name['delete_on_close']._serialized_options = b'\222\265\030\rDeleteOnClose'
  _globals['_FORMATTEDAUDITRECORD'].fields_by_name['smb2_security_descriptor']._loaded_options = None
  _globals['_FORMATTEDAUDITRECORD'].fields_by_name['smb2_security_descriptor']._serialized_options = b'\222\265\030\022SecurityDescriptor'
  _globals['_FORMATTEDAUDITRECORD'].fields_by_name['security_descriptor']._loaded_options = None
  _globals['_FORMATTEDAUDITRECORD'].fields_by_name['security_descriptor']._serialized_options = b'\222\265\030\022SecurityDescriptor'
  _globals['_FORMATTEDAUDITRECORD'].fields_by_name['prev_smb2_security_descriptor']._loaded_options = None
  _globals['_FORMATTEDAUDITRECORD'].fields_by_name['prev_smb2_security_descriptor']._serialized_options = b'\222\265\030\026PrevSecurityDescriptor'
  _globals['_FORMATTEDAUDITRECORD'].fields_by_name['prev_security_descriptor']._loaded_options = None
  _globals['_FORMATTEDAUDITRECORD'].fields_by_name['prev_security_descriptor']._serialized_options = b'\222\265\030\026PrevSecurityDescriptor'
  _globals['_FORMATTEDAUDITRECORD'].fields_by_name['prev_entity_mode']._loaded_options = None
  _globals['_FORMATTEDAUDITRECORD'].fields_by_name['prev_entity_mode']._serialized_options = b'\222\265\030\016PrevEntityMode'
  _globals['_FORMATTEDAUDITRECORD'].fields_by_name['prev_entity_user_id']._loaded_options = None
  _globals['_FORMATTEDAUDITRECORD'].fields_by_name['prev_entity_user_id']._serialized_options = b'\222\265\030\020PrevEntityUserID'
  _globals['_FORMATTEDAUDITRECORD'].fields_by_name['prev_entity_group_id']._loaded_options = None
  _globals['_FORMATTEDAUDITRECORD'].fields_by_name['prev_entity_group_id']._serialized_options = b'\222\265\030\021PrevEntityGroupID'
  _globals['_FORMATTEDAUDITRECORD'].fields_by_name['inode_size_bytes']._loaded_options = None
  _globals['_FORMATTEDAUDITRECORD'].fields_by_name['inode_size_bytes']._serialized_options = b'\222\265\030\016InodeSizeBytes'
  _globals['_FORMATTEDAUDITRECORD'].fields_by_name['source_parent_entity_inode']._loaded_options = None
  _globals['_FORMATTEDAUDITRECORD'].fields_by_name['source_parent_entity_inode']._serialized_options = b'\222\265\030\027SourceParentEntityInode'
  _globals['_FORMATTEDAUDITRECORD'].fields_by_name['etag']._loaded_options = None
  _globals['_FORMATTEDAUDITRECORD'].fields_by_name['etag']._serialized_options = b'\222\265\030\004ETag'
  _globals['_FORMATTEDAUDITRECORD'].fields_by_name['upload_id']._loaded_options = None
  _globals['_FORMATTEDAUDITRECORD'].fields_by_name['upload_id']._serialized_options = b'\222\265\030\010UploadId'
  _globals['_FORMATTEDAUDITRECORD'].fields_by_name['part_number']._loaded_options = None
  _globals['_FORMATTEDAUDITRECORD'].fields_by_name['part_number']._serialized_options = b'\222\265\030\nPartNumber'
  _globals['_FORMATTEDAUDITRECORD'].fields_by_name['ddw_portal_audit_log']._loaded_options = None
  _globals['_FORMATTEDAUDITRECORD'].fields_by_name['ddw_portal_audit_log']._serialized_options = b'\222\265\030\021DdwPortalAuditLog'
  _globals['_FORMATTEDAUDITRECORD'].fields_by_name['lcm_rule_name']._loaded_options = None
  _globals['_FORMATTEDAUDITRECORD'].fields_by_name['lcm_rule_name']._serialized_options = b'\222\265\030\013LCMRuleName'
  _globals['_FORMATTEDAUDITRECORD'].fields_by_name['entity_creation_timestamp']._loaded_options = None
  _globals['_FORMATTEDAUDITRECORD'].fields_by_name['entity_creation_timestamp']._serialized_options = b'\222\265\030\027EntityCreationTimestamp'
  _globals['_FORMATTEDAUDITRECORD'].fields_by_name['entity_access_timestamp']._loaded_options = None
  _globals['_FORMATTEDAUDITRECORD'].fields_by_name['entity_access_timestamp']._serialized_options = b'\222\265\030\025EntityAccessTimestamp'
  _globals['_FORMATTEDACE'].fields_by_name['ace_type']._loaded_options = None
  _globals['_FORMATTEDACE'].fields_by_name['ace_type']._serialized_options = b'\222\265\030\007AceType'
  _globals['_FORMATTEDACE'].fields_by_name['ace_flags']._loaded_options = None
  _globals['_FORMATTEDACE'].fields_by_name['ace_flags']._serialized_options = b'\222\265\030\010AceFlags'
  _globals['_FORMATTEDACE'].fields_by_name['access_mask']._loaded_options = None
  _globals['_FORMATTEDACE'].fields_by_name['access_mask']._serialized_options = b'\222\265\030\nAccessMask'
  _globals['_FORMATTEDACE'].fields_by_name['sid']._loaded_options = None
  _globals['_FORMATTEDACE'].fields_by_name['sid']._serialized_options = b'\222\265\030\003Sid'
  _globals['_FORMATTEDSMB2SECURITYDESCRIPTOR'].fields_by_name['control']._loaded_options = None
  _globals['_FORMATTEDSMB2SECURITYDESCRIPTOR'].fields_by_name['control']._serialized_options = b'\222\265\030\007Control'
  _globals['_FORMATTEDSMB2SECURITYDESCRIPTOR'].fields_by_name['owner_sid']._loaded_options = None
  _globals['_FORMATTEDSMB2SECURITYDESCRIPTOR'].fields_by_name['owner_sid']._serialized_options = b'\222\265\030\010OwnerSid'
  _globals['_FORMATTEDSMB2SECURITYDESCRIPTOR'].fields_by_name['group_sid']._loaded_options = None
  _globals['_FORMATTEDSMB2SECURITYDESCRIPTOR'].fields_by_name['group_sid']._serialized_options = b'\222\265\030\010GroupSid'
  _globals['_FORMATTEDSMB2SECURITYDESCRIPTOR'].fields_by_name['dacls']._loaded_options = None
  _globals['_FORMATTEDSMB2SECURITYDESCRIPTOR'].fields_by_name['dacls']._serialized_options = b'\222\265\030\005Dacls'
  _globals['_FORMATTEDDDWPORTALAUDITLOG'].fields_by_name['file_name']._loaded_options = None
  _globals['_FORMATTEDDDWPORTALAUDITLOG'].fields_by_name['file_name']._serialized_options = b'\222\265\030\010FileName'
  _globals['_FORMATTEDDDWPORTALAUDITLOG'].fields_by_name['start_time']._loaded_options = None
  _globals['_FORMATTEDDDWPORTALAUDITLOG'].fields_by_name['start_time']._serialized_options = b'\222\265\030\tStartTime'
  _globals['_FORMATTEDDDWPORTALAUDITLOG'].fields_by_name['end_time']._loaded_options = None
  _globals['_FORMATTEDDDWPORTALAUDITLOG'].fields_by_name['end_time']._serialized_options = b'\222\265\030\007EndTime'
  _globals['_FORMATTEDDDWPORTALAUDITLOG'].fields_by_name['file_size']._loaded_options = None
  _globals['_FORMATTEDDDWPORTALAUDITLOG'].fields_by_name['file_size']._serialized_options = b'\222\265\030\010FileSize'
  _globals['_FORMATTEDDDWPORTALAUDITLOG'].fields_by_name['read_size']._loaded_options = None
  _globals['_FORMATTEDDDWPORTALAUDITLOG'].fields_by_name['read_size']._serialized_options = b'\222\265\030\010ReadSize'
  _globals['_FORMATTEDDDWPORTALAUDITLOG'].fields_by_name['status']._loaded_options = None
  _globals['_FORMATTEDDDWPORTALAUDITLOG'].fields_by_name['status']._serialized_options = b'\222\265\030\006Status'
  _globals['_FORMATTEDDDWPORTALAUDITLOG'].fields_by_name['source_type']._loaded_options = None
  _globals['_FORMATTEDDDWPORTALAUDITLOG'].fields_by_name['source_type']._serialized_options = b'\222\265\030\nSourceType'
  _globals['_FORMATTEDDDWPORTALAUDITLOG'].fields_by_name['tag']._loaded_options = None
  _globals['_FORMATTEDDDWPORTALAUDITLOG'].fields_by_name['tag']._serialized_options = b'\222\265\030\003Tag'
  _globals['_USERIDENTITY']._serialized_start=269
  _globals['_USERIDENTITY']._serialized_end=456
  _globals['_AUDITRECORDID']._serialized_start=458
  _globals['_AUDITRECORDID']._serialized_end=511
  _globals['_FILEATTRIBUTES']._serialized_start=514
  _globals['_FILEATTRIBUTES']._serialized_end=789
  _globals['_S3RESPONSE']._serialized_start=791
  _globals['_S3RESPONSE']._serialized_end=857
  _globals['_AUDITRECORD']._serialized_start=860
  _globals['_AUDITRECORD']._serialized_end=2635
  _globals['_AUDITRECORD_PROTOCOL']._serialized_start=2188
  _globals['_AUDITRECORD_PROTOCOL']._serialized_end=2269
  _globals['_AUDITRECORD_REQUESTTYPE']._serialized_start=2272
  _globals['_AUDITRECORD_REQUESTTYPE']._serialized_end=2507
  _globals['_AUDITRECORD_FILETYPE']._serialized_start=2509
  _globals['_AUDITRECORD_FILETYPE']._serialized_end=2635
  _globals['_FORMATTEDAUDITRECORD']._serialized_start=2638
  _globals['_FORMATTEDAUDITRECORD']._serialized_end=4641
  _globals['_FORMATTEDACE']._serialized_start=4644
  _globals['_FORMATTEDACE']._serialized_end=4781
  _globals['_FORMATTEDSMB2SECURITYDESCRIPTOR']._serialized_start=4784
  _globals['_FORMATTEDSMB2SECURITYDESCRIPTOR']._serialized_end=4980
  _globals['_DDWPORTALAUDITLOG']._serialized_start=4983
  _globals['_DDWPORTALAUDITLOG']._serialized_end=5350
  _globals['_DDWPORTALAUDITLOG_STATUS']._serialized_start=5259
  _globals['_DDWPORTALAUDITLOG_STATUS']._serialized_end=5312
  _globals['_DDWPORTALAUDITLOG_SOURCETYPE']._serialized_start=5314
  _globals['_DDWPORTALAUDITLOG_SOURCETYPE']._serialized_end=5350
  _globals['_FORMATTEDDDWPORTALAUDITLOG']._serialized_start=5353
  _globals['_FORMATTEDDDWPORTALAUDITLOG']._serialized_end=5633
# @@protoc_insertion_point(module_scope)
