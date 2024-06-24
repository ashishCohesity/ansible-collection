# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: magneto/connectors/outlook/outlook_external.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1magneto/connectors/outlook/outlook_external.proto\x12\x18\x63ohesity.magneto.outlook\"\x90\x01\n\x0e\x46olderRootType\"~\n\x04Type\x12\x12\n\x0ekMsgFolderRoot\x10\x01\x12\x19\n\x15kArchiveMsgFolderRoot\x10\x02\x12\x1f\n\x1bkRecoverableItemsFolderRoot\x10\x03\x12&\n\"kArchiveRecoverableItemsFolderRoot\x10\x04\"l\n\nFolderType\"^\n\x04Type\x12\x12\n\x0ekEmailMessages\x10\x01\x12\r\n\tkCalendar\x10\x02\x12\r\n\tkContacts\x10\x03\x12\x0b\n\x07kSearch\x10\x04\x12\n\n\x06kTasks\x10\x05\x12\x0b\n\x07kFolder\x10\x06\"\x9a\x02\n\x08ItemType\"\x8d\x02\n\x04Type\x12\x11\n\rkEmailMessage\x10\x01\x12\r\n\tkCalendar\x10\x02\x12\t\n\x05kTask\x10\x03\x12\x0c\n\x08kContact\x10\x04\x12\t\n\x05kItem\x10\x05\x12\x13\n\x0fkSharingMessage\x10\x06\x12\x13\n\x0fkMeetingMessage\x10\x07\x12\x13\n\x0fkMeetingRequest\x10\x08\x12\x14\n\x10kMeetingResponse\x10\t\x12\x18\n\x14kMeetingCancellation\x10\n\x12\r\n\tkPostItem\x10\x0b\x12\x0f\n\x0bkRoleMember\x10\x0c\x12\x0c\n\x08kNetwork\x10\r\x12\x0b\n\x07kPerson\x10\x0e\x12\x15\n\x11kDistributionList\x10\x0f\"+\n\x04User\x12\x15\n\remail_address\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\">\n\x0e\x41ttachmentType\",\n\x04Type\x12\t\n\x05kFile\x10\x01\x12\t\n\x05kItem\x10\x02\x12\x0e\n\nkReference\x10\x03\"\xa7\x01\n\nAttachment\x12\n\n\x02id\x18\x01 \x01(\t\x12;\n\x04type\x18\x02 \x01(\x0e\x32-.cohesity.magneto.outlook.AttachmentType.Type\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x14\n\x0c\x63ontent_type\x18\x04 \x01(\t\x12\x12\n\nsize_bytes\x18\x05 \x01(\x03\x12\x0e\n\x06inline\x18\x06 \x01(\x08*\x08\x08\x64\x10\x80\x80\x80\x80\x02\"\xfe\x0e\n\x0cItemMetaData\x12\n\n\x02id\x18\x01 \x01(\t\x12\x35\n\x04type\x18\x02 \x01(\x0e\x32\'.cohesity.magneto.outlook.ItemType.Type\x12\x18\n\x10parent_folder_id\x18\x03 \x01(\t\x12\x17\n\x0fhas_attachments\x18\x04 \x01(\x08\x12,\n\x04\x66rom\x18\x05 \x01(\x0b\x32\x1e.cohesity.magneto.outlook.User\x12\x38\n\x10to_recipient_vec\x18\x06 \x03(\x0b\x32\x1e.cohesity.magneto.outlook.User\x12\x38\n\x10\x63\x63_recipient_vec\x18\x07 \x03(\x0b\x32\x1e.cohesity.magneto.outlook.User\x12\x39\n\x11\x62\x63\x63_recipient_vec\x18\x08 \x03(\x0b\x32\x1e.cohesity.magneto.outlook.User\x12\x11\n\tsent_time\x18\t \x01(\x03\x12\x15\n\rreceived_time\x18\n \x01(\x03\x12<\n\x0e\x61ttachment_vec\x18\x0b \x03(\x0b\x32$.cohesity.magneto.outlook.Attachment\x12\x12\n\nchange_key\x18\x0c \x01(\t\x12\x0c\n\x04size\x18\r \x01(\x03\x12\x0f\n\x07subject\x18\x0e \x01(\t\x12\x12\n\nitem_class\x18\x0f \x01(\t\x12!\n\x19metadata_parent_folder_id\x18\x10 \x01(\t\x12\x15\n\rcreation_time\x18\x11 \x01(\x03\x12G\n\x0bsensitivity\x18\x12 \x01(\x0e\x32\x32.cohesity.magneto.outlook.ItemMetaData.Sensitivity\x12\x45\n\nimportance\x18\x13 \x01(\x0e\x32\x31.cohesity.magneto.outlook.ItemMetaData.Importance\x12\x1a\n\x12last_modified_name\x18\x14 \x01(\t\x12\x1a\n\x12last_modified_time\x18\x15 \x01(\x03\x12\x31\n\torganizer\x18\x16 \x01(\x0b\x32\x1e.cohesity.magneto.outlook.User\x12>\n\x16required_attendees_vec\x18\x17 \x03(\x0b\x32\x1e.cohesity.magneto.outlook.User\x12>\n\x16optional_attendees_vec\x18\x18 \x03(\x0b\x32\x1e.cohesity.magneto.outlook.User\x12\x14\n\x0cis_recurring\x18\x19 \x01(\x08\x12\x12\n\nstart_time\x18\x1a \x01(\x03\x12\x10\n\x08\x65nd_time\x18\x1b \x01(\x03\x12K\n\x10\x66irst_occurrence\x18\x1c \x01(\x0b\x32\x31.cohesity.magneto.outlook.ItemMetaData.Occurrence\x12J\n\x0flast_occurrence\x18\x1d \x01(\x0b\x32\x31.cohesity.magneto.outlook.ItemMetaData.Occurrence\x12T\n\x12recurrence_pattern\x18\x1e \x01(\x0e\x32\x38.cohesity.magneto.outlook.ItemMetaData.RecurrencePattern\x12\x12\n\nfirst_name\x18\x1f \x01(\t\x12\x13\n\x0bmiddle_name\x18  \x01(\t\x12\x11\n\tlast_name\x18! \x01(\t\x12\x10\n\x08\x62irthday\x18\" \x01(\x03\x12\x1b\n\x13\x65mail_addresses_vec\x18# \x03(\t\x12\r\n\x05owner\x18$ \x01(\t\x12\x10\n\x08\x64ue_date\x18% \x01(\x03\x12\x17\n\x0f\x63ompletion_date\x18& \x01(\x03\x12\x46\n\x0btask_status\x18\' \x01(\x0e\x32\x31.cohesity.magneto.outlook.ItemMetaData.TaskStatus\x12\x18\n\x10sha_256_checksum\x18( \x01(\t\x1a\x32\n\nOccurrence\x12\x12\n\nstart_time\x18\x01 \x01(\x03\x12\x10\n\x08\x65nd_time\x18\x02 \x01(\x03\"J\n\x0bSensitivity\x12\x0b\n\x07kNormal\x10\x01\x12\r\n\tkPersonal\x10\x02\x12\x0c\n\x08kPrivate\x10\x03\x12\x11\n\rkConfidential\x10\x04\"L\n\nImportance\x12\x12\n\x0ekLowImportance\x10\x01\x12\x15\n\x11kNormalImportance\x10\x02\x12\x13\n\x0fkHighImportance\x10\x03\"R\n\x11RecurrencePattern\x12\t\n\x05kNone\x10\x01\x12\x0b\n\x07kYearly\x10\x02\x12\x0c\n\x08kMonthly\x10\x03\x12\x0b\n\x07kWeekly\x10\x04\x12\n\n\x06kDaily\x10\x05\"c\n\nTaskStatus\x12\x0f\n\x0bkNotStarted\x10\x01\x12\x0f\n\x0bkInProgress\x10\x02\x12\x0e\n\nkCompleted\x10\x03\x12\x14\n\x10kWaitingOnOthers\x10\x04\x12\r\n\tkDeferred\x10\x05\"I\n\x0cPropertyType\"9\n\x04Type\x12\x0b\n\x07kBinary\x10\x00\x12\x0c\n\x08kBoolean\x10\x01\x12\x0b\n\x07kString\x10\x02\x12\t\n\x05kLong\x10\x03\">\n\x08\x46olderId\x12\n\n\x02id\x18\x01 \x01(\t\x12\x12\n\nchange_key\x18\x02 \x01(\t\x12\x12\n\nreplica_id\x18\x03 \x01(\t\"l\n\x10\x45xtendedFieldURI\x12\x14\n\x0cproperty_tag\x18\x01 \x01(\t\x12\x42\n\rproperty_type\x18\x02 \x01(\x0e\x32+.cohesity.magneto.outlook.PropertyType.Type\"\xb6\x01\n\x06UserId\x12\x0b\n\x03sid\x18\x01 \x01(\t\x12\x1c\n\x14primary_smtp_address\x18\x02 \x01(\t\x12\x14\n\x0c\x64isplay_name\x18\x03 \x01(\t\x12K\n\x12\x64istinguished_user\x18\x04 \x01(\x0e\x32/.cohesity.magneto.outlook.DistinguishedUserType\x12\x1e\n\x16\x65xternal_user_identity\x18\x05 \x01(\t\"\xb2\x04\n\nPermission\x12\x1f\n\x10\x63\x61n_create_items\x18\x01 \x01(\x08:\x05\x66\x61lse\x12%\n\x16\x63\x61n_create_sub_folders\x18\x02 \x01(\x08:\x05\x66\x61lse\x12\x1e\n\x0fis_folder_owner\x18\x03 \x01(\x08:\x05\x66\x61lse\x12 \n\x11is_folder_visible\x18\x04 \x01(\x08:\x05\x66\x61lse\x12 \n\x11is_folder_contact\x18\x05 \x01(\x08:\x05\x66\x61lse\x12O\n\nedit_items\x18\x06 \x01(\x0e\x32..cohesity.magneto.outlook.PermissionActionType:\x0bkActionNone\x12Q\n\x0c\x64\x65lete_items\x18\x07 \x01(\x0e\x32..cohesity.magneto.outlook.PermissionActionType:\x0bkActionNone\x12N\n\x10permission_level\x18\x08 \x01(\x0e\x32-.cohesity.magneto.outlook.PermissionLevelType:\x05kNone\x12Q\n\nread_items\x18\t \x01(\x0e\x32\x32.cohesity.magneto.outlook.PermissionReadAccessType:\tkReadNone\x12\x31\n\x07user_id\x18\n \x01(\x0b\x32 .cohesity.magneto.outlook.UserId\"c\n\rPermissionSet\x12\x39\n\x0bpermissions\x18\x01 \x03(\x0b\x32$.cohesity.magneto.outlook.Permission\x12\x17\n\x0funknown_entries\x18\x02 \x03(\t\"\xd1\x04\n\x11\x46olderContentInfo\x12\x14\n\x0c\x64isplay_name\x18\x01 \x01(\t\x12<\n\x10parent_folder_id\x18\x02 \x01(\x0b\x32\".cohesity.magneto.outlook.FolderId\x12\x13\n\x0btotal_count\x18\x03 \x01(\x05\x12\x14\n\x0cunread_count\x18\x04 \x01(\x05\x12\x1a\n\x12\x63hild_folder_count\x18\x05 \x01(\x05\x12?\n\x0epermission_set\x18\x06 \x01(\x0b\x32\'.cohesity.magneto.outlook.PermissionSet\x12\x35\n\tfolder_id\x18\x07 \x01(\x0b\x32\".cohesity.magneto.outlook.FolderId\x12\x14\n\x0c\x66older_class\x18\x08 \x01(\t\x12\x12\n\nsync_state\x18\t \x01(\t\x12[\n\x15\x65xtended_property_vec\x18\n \x03(\x0b\x32<.cohesity.magneto.outlook.FolderContentInfo.ExtendedProperty\x12\x37\n\x04type\x18\x0b \x01(\x0e\x32).cohesity.magneto.outlook.FolderType.Type\x1ai\n\x10\x45xtendedProperty\x12\x46\n\x12\x65xtended_field_uri\x18\x01 \x01(\x0b\x32*.cohesity.magneto.outlook.ExtendedFieldURI\x12\r\n\x05value\x18\x02 \x01(\t*=\n\x14PermissionActionType\x12\x0f\n\x0bkActionNone\x10\x00\x12\n\n\x06kOwned\x10\x01\x12\x08\n\x04kAll\x10\x02*\xb9\x01\n\x13PermissionLevelType\x12\t\n\x05kNone\x10\x00\x12\n\n\x06kOwner\x10\x01\x12\x15\n\x11kPublishingEditor\x10\x02\x12\x0b\n\x07kEditor\x10\x03\x12\x15\n\x11kPublishingAuthor\x10\x04\x12\x0b\n\x07kAuthor\x10\x05\x12\x15\n\x11kNoneditingAuthor\x10\x06\x12\r\n\tkReviewer\x10\x07\x12\x10\n\x0ckContributor\x10\x08\x12\x0b\n\x07kCustom\x10\t*;\n\x18PermissionReadAccessType\x12\r\n\tkReadNone\x10\x00\x12\x10\n\x0ckFullDetails\x10\x01*5\n\x15\x44istinguishedUserType\x12\x0c\n\x08kDefault\x10\x00\x12\x0e\n\nkAnonymous\x10\x01\x42\x30Z.magneto/connectors/outlook/outlook_external.pb')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'magneto.connectors.outlook.outlook_external_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z.magneto/connectors/outlook/outlook_external.pb'
  _globals['_PERMISSIONACTIONTYPE']._serialized_start=4517
  _globals['_PERMISSIONACTIONTYPE']._serialized_end=4578
  _globals['_PERMISSIONLEVELTYPE']._serialized_start=4581
  _globals['_PERMISSIONLEVELTYPE']._serialized_end=4766
  _globals['_PERMISSIONREADACCESSTYPE']._serialized_start=4768
  _globals['_PERMISSIONREADACCESSTYPE']._serialized_end=4827
  _globals['_DISTINGUISHEDUSERTYPE']._serialized_start=4829
  _globals['_DISTINGUISHEDUSERTYPE']._serialized_end=4882
  _globals['_FOLDERROOTTYPE']._serialized_start=80
  _globals['_FOLDERROOTTYPE']._serialized_end=224
  _globals['_FOLDERROOTTYPE_TYPE']._serialized_start=98
  _globals['_FOLDERROOTTYPE_TYPE']._serialized_end=224
  _globals['_FOLDERTYPE']._serialized_start=226
  _globals['_FOLDERTYPE']._serialized_end=334
  _globals['_FOLDERTYPE_TYPE']._serialized_start=240
  _globals['_FOLDERTYPE_TYPE']._serialized_end=334
  _globals['_ITEMTYPE']._serialized_start=337
  _globals['_ITEMTYPE']._serialized_end=619
  _globals['_ITEMTYPE_TYPE']._serialized_start=350
  _globals['_ITEMTYPE_TYPE']._serialized_end=619
  _globals['_USER']._serialized_start=621
  _globals['_USER']._serialized_end=664
  _globals['_ATTACHMENTTYPE']._serialized_start=666
  _globals['_ATTACHMENTTYPE']._serialized_end=728
  _globals['_ATTACHMENTTYPE_TYPE']._serialized_start=684
  _globals['_ATTACHMENTTYPE_TYPE']._serialized_end=728
  _globals['_ATTACHMENT']._serialized_start=731
  _globals['_ATTACHMENT']._serialized_end=898
  _globals['_ITEMMETADATA']._serialized_start=901
  _globals['_ITEMMETADATA']._serialized_end=2819
  _globals['_ITEMMETADATA_OCCURRENCE']._serialized_start=2430
  _globals['_ITEMMETADATA_OCCURRENCE']._serialized_end=2480
  _globals['_ITEMMETADATA_SENSITIVITY']._serialized_start=2482
  _globals['_ITEMMETADATA_SENSITIVITY']._serialized_end=2556
  _globals['_ITEMMETADATA_IMPORTANCE']._serialized_start=2558
  _globals['_ITEMMETADATA_IMPORTANCE']._serialized_end=2634
  _globals['_ITEMMETADATA_RECURRENCEPATTERN']._serialized_start=2636
  _globals['_ITEMMETADATA_RECURRENCEPATTERN']._serialized_end=2718
  _globals['_ITEMMETADATA_TASKSTATUS']._serialized_start=2720
  _globals['_ITEMMETADATA_TASKSTATUS']._serialized_end=2819
  _globals['_PROPERTYTYPE']._serialized_start=2821
  _globals['_PROPERTYTYPE']._serialized_end=2894
  _globals['_PROPERTYTYPE_TYPE']._serialized_start=2837
  _globals['_PROPERTYTYPE_TYPE']._serialized_end=2894
  _globals['_FOLDERID']._serialized_start=2896
  _globals['_FOLDERID']._serialized_end=2958
  _globals['_EXTENDEDFIELDURI']._serialized_start=2960
  _globals['_EXTENDEDFIELDURI']._serialized_end=3068
  _globals['_USERID']._serialized_start=3071
  _globals['_USERID']._serialized_end=3253
  _globals['_PERMISSION']._serialized_start=3256
  _globals['_PERMISSION']._serialized_end=3818
  _globals['_PERMISSIONSET']._serialized_start=3820
  _globals['_PERMISSIONSET']._serialized_end=3919
  _globals['_FOLDERCONTENTINFO']._serialized_start=3922
  _globals['_FOLDERCONTENTINFO']._serialized_end=4515
  _globals['_FOLDERCONTENTINFO_EXTENDEDPROPERTY']._serialized_start=4410
  _globals['_FOLDERCONTENTINFO_EXTENDEDPROPERTY']._serialized_end=4515
# @@protoc_insertion_point(module_scope)
