# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bridge/magneto/object_store/object_store_actions.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from bridge.magneto.base import magneto_actions_pb2 as bridge_dot_magneto_dot_base_dot_magneto__actions__pb2
from bridge.s3_portal.base import s3_metadata_pb2 as bridge_dot_s3__portal_dot_base_dot_s3__metadata__pb2
from bridge.snap_fs import entity_handle_pb2 as bridge_dot_snap__fs_dot_entity__handle__pb2
from configs import cluster_config_pb2 as configs_dot_cluster__config__pb2
from nexus.cloud.base import credentials_pb2 as nexus_dot_cloud_dot_base_dot_credentials__pb2
from magneto.directory_walker import directory_walker_pb2 as magneto_dot_directory__walker_dot_directory__walker__pb2
from magneto.object_walker import object_metadata_pb2 as magneto_dot_object__walker_dot_object__metadata__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6bridge/magneto/object_store/object_store_actions.proto\x12$cohesity.bridge.magneto.object_store\x1a)bridge/magneto/base/magneto_actions.proto\x1a\'bridge/s3_portal/base/s3_metadata.proto\x1a\"bridge/snap_fs/entity_handle.proto\x1a\x1c\x63onfigs/cluster_config.proto\x1a\"nexus/cloud/base/credentials.proto\x1a/magneto/directory_walker/directory_walker.proto\x1a+magneto/object_walker/object_metadata.proto\"\xb3\x0e\n\x14ObjectStoreActionArg\x12\x0f\n\x07task_id\x18\x01 \x01(\x03\x12\x17\n\x0bsub_task_id\x18\x02 \x01(\x03:\x02-1\x12G\n\x0cobject_store\x18\x03 \x01(\x0b\x32\x31.cohesity.bridge.magneto.object_store.ObjectStore\x12\x65\n\x0b\x61\x63tion_type\x18\r \x01(\x0e\x32P.cohesity.bridge.magneto.object_store.ObjectStoreActionArg.ObjectStoreActionType\x12T\n\x12prepare_backup_arg\x18\x04 \x01(\x0b\x32\x36.cohesity.bridge.magneto.object_store.PrepareBackupArgH\x00\x12\x41\n\x0f\x63\x61ncel_task_arg\x18\x05 \x01(\x0b\x32&.cohesity.bridge.magneto.CancelTaskArgH\x00\x12\x61\n\x19list_objects_metadata_arg\x18\x06 \x01(\x0b\x32<.cohesity.bridge.magneto.object_store.ListObjectsMetadataArgH\x00\x12[\n\x16\x62\x61\x63kup_object_area_arg\x18\x07 \x01(\x0b\x32\x39.cohesity.bridge.magneto.object_store.BackupObjectAreaArgH\x00\x12\x61\n\x19\x64\x65lete_object_version_arg\x18\x08 \x01(\x0b\x32<.cohesity.bridge.magneto.object_store.DeleteObjectVersionArgH\x00\x12T\n\x12\x63reate_objects_arg\x18\t \x01(\x0b\x32\x36.cohesity.bridge.magneto.object_store.CreateObjectsArgH\x00\x12i\n\x1d\x66inalize_cohesity_objects_arg\x18\n \x01(\x0b\x32@.cohesity.bridge.magneto.object_store.FinalizeCohesityObjectsArgH\x00\x12]\n\x17\x66inalize_s3_objects_arg\x18\x0b \x01(\x0b\x32:.cohesity.bridge.magneto.object_store.FinalizeS3ObjectsArgH\x00\x12\x64\n\x1b\x61\x62ort_s3_objects_upload_arg\x18\x0c \x01(\x0b\x32=.cohesity.bridge.magneto.object_store.AbortS3ObjectsUploadArgH\x00\x12^\n\x17restore_object_area_arg\x18\x0e \x01(\x0b\x32;.cohesity.bridge.magneto.object_store.RestoreObjectAreasArgH\x00\x12]\n\x17get_object_versions_arg\x18\x0f \x01(\x0b\x32:.cohesity.bridge.magneto.object_store.GetObjectVersionsArgH\x00\x12L\n\x0e\x65nd_backup_arg\x18\x10 \x01(\x0b\x32\x32.cohesity.bridge.magneto.object_store.EndBackupArgH\x00\"\xcf\x02\n\x15ObjectStoreActionType\x12\x12\n\x0ekPrepareBackup\x10\x01\x12\x0f\n\x0bkCancelTask\x10\x02\x12\x18\n\x14kListObjectsMetadata\x10\x03\x12\x15\n\x11kBackupObjectArea\x10\x04\x12\x18\n\x14kDeleteObjectVersion\x10\x05\x12\x12\n\x0ekCreateObjects\x10\x06\x12\x1c\n\x18kFinalizeCohesityObjects\x10\x07\x12\x16\n\x12kFinalizeS3Objects\x10\x08\x12\x19\n\x15kAbortS3ObjectsUpload\x10\t\x12\x0f\n\x0bkEndSubTask\x10\n\x12\x0e\n\nkEndBackup\x10\x0b\x12\x0f\n\x0bkEndRestore\x10\x0c\x12\x17\n\x13kRestoreObjectAreas\x10\r\x12\x16\n\x12kGetObjectVersions\x10\x0e\x32\x86\x01\n\x17object_store_action_arg\x12).cohesity.bridge.magneto.ExecuteActionArg\x18| \x01(\x0b\x32:.cohesity.bridge.magneto.object_store.ObjectStoreActionArgB\x17\n\x15ObjectStoreActionArgs\"\xe4\x01\n\x0bObjectStore\x12=\n\x04type\x18\x01 \x01(\x0e\x32/.cohesity.configs.ClusterConfigProto.Vault.Type\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0e\n\x06region\x18\x03 \x01(\t\x12(\n\x19object_level_acls_enabled\x18\x05 \x01(\x08:\x05\x66\x61lse\x12?\n\x0f\x61ws_credentials\x18\x04 \x01(\x0b\x32$.cohesity.nexus.cloud.AwsCredentialsH\x00\x42\r\n\x0b\x43redentials\"\xb3\x01\n\x10PrepareBackupArg\x12\x34\n\x04\x62\x61se\x18\x01 \x01(\x0b\x32&.cohesity.bridge.magneto.BackupBaseArg\x12\x1a\n\x12previous_view_name\x18\x02 \x01(\t\x12\x11\n\tview_name\x18\x03 \x01(\t\x12:\n\ts3_config\x18\x04 \x01(\x0b\x32\'.cohesity.bridge.s3.S3BucketConfigProto\"\x97\x01\n\x0c\x45ndBackupArg\x12\x34\n\x04\x62\x61se\x18\x01 \x01(\x0b\x32&.cohesity.bridge.magneto.BackupBaseArg\x12Q\n\x1c\x65ntities_in_config_to_delete\x18\x02 \x03(\x0b\x32+.cohesity.storage.dir_walker.EntityMetadata\"\xac\x01\n\x16ListObjectsMetadataArg\x12\x17\n\x0fstart_after_key\x18\x01 \x01(\t\x12\x0f\n\x07\x65nd_key\x18\x02 \x01(\t\x12\x1a\n\x12\x63ontinuation_token\x18\x03 \x01(\t\x12\x1f\n\x10include_versions\x18\x04 \x01(\x08:\x05\x66\x61lse\x12\x0e\n\x06prefix\x18\x05 \x01(\t\x12\x1b\n\x0cinclude_acls\x18\x06 \x01(\x08:\x05\x66\x61lse\"\xc5\x02\n\x13\x42\x61\x63kupObjectAreaArg\x12\x34\n\x04\x62\x61se\x18\x01 \x01(\x0b\x32&.cohesity.bridge.magneto.BackupBaseArg\x12\x66\n\x14object_area_info_vec\x18\x02 \x03(\x0b\x32H.cohesity.bridge.magneto.object_store.BackupObjectAreaArg.ObjectAreaInfo\x1a\x8f\x01\n\x0eObjectAreaInfo\x12\x45\n\x0bobject_area\x18\x01 \x01(\x0b\x32\x30.cohesity.bridge.magneto.object_store.ObjectArea\x12\x36\n\x02\x65h\x18\x02 \x01(\x0b\x32*.cohesity.bridge.snap_fs.EntityHandleProto\"-\n\nObjectInfo\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x12\n\nversion_id\x18\x02 \x01(\t\"\xc4\x01\n\nObjectArea\x12\x45\n\x0bobject_info\x18\x01 \x01(\x0b\x32\x30.cohesity.bridge.magneto.object_store.ObjectInfo\x12\x14\n\x0cstart_offset\x18\x02 \x01(\x03\x12\x0e\n\x06length\x18\x03 \x01(\r\x12I\n\x0fobject_metadata\x18\x04 \x01(\x0b\x32\x30.cohesity.storage.object_metadata.ObjectMetadata\"\xe5\x02\n\x10\x43reateObjectsArg\x12g\n\x16object_action_info_vec\x18\x01 \x03(\x0b\x32G.cohesity.bridge.magneto.object_store.CreateObjectsArg.ObjectActionInfo\x12\x1d\n\x15min_mega_file_size_mb\x18\x02 \x01(\x03\x12\x15\n\rsub_file_size\x18\x03 \x01(\x03\x1a\xb1\x01\n\x10ObjectActionInfo\x12I\n\x0fobject_metadata\x18\x01 \x01(\x0b\x32\x30.cohesity.storage.object_metadata.ObjectMetadata\x12R\n\robject_action\x18\x02 \x01(\x0e\x32\x32.cohesity.bridge.magneto.object_store.ObjectAction:\x07kCreate\"\xfa\x01\n\x1a\x46inalizeCohesityObjectsArg\x12x\n\x13\x66inalize_object_vec\x18\x01 \x03(\x0b\x32[.cohesity.bridge.magneto.object_store.FinalizeCohesityObjectsArg.FinalizeCohesityObjectInfo\x1a\x62\n\x1a\x46inalizeCohesityObjectInfo\x12\x36\n\x02\x65h\x18\x01 \x01(\x0b\x32*.cohesity.bridge.snap_fs.EntityHandleProto\x12\x0c\n\x04\x65tag\x18\x02 \x01(\t\"_\n\x16\x44\x65leteObjectVersionArg\x12\x45\n\x0bobject_info\x18\x01 \x01(\x0b\x32\x30.cohesity.bridge.magneto.object_store.ObjectInfo\"\x94\x03\n\x14\x46inalizeS3ObjectsArg\x12m\n\x14\x66inalize_objects_vec\x18\x01 \x03(\x0b\x32O.cohesity.bridge.magneto.object_store.FinalizeS3ObjectsArg.FinalizeS3ObjectInfo\x1a\x8c\x02\n\x14\x46inalizeS3ObjectInfo\x12\x45\n\x0bobject_info\x18\x01 \x01(\x0b\x32\x30.cohesity.bridge.magneto.object_store.ObjectInfo\x12\x11\n\tupload_id\x18\x02 \x01(\t\x12o\n\rpart_info_vec\x18\x03 \x03(\x0b\x32X.cohesity.bridge.magneto.object_store.FinalizeS3ObjectsArg.FinalizeS3ObjectInfo.PartInfo\x1a)\n\x08PartInfo\x12\x0f\n\x07part_id\x18\x01 \x01(\x05\x12\x0c\n\x04\x65tag\x18\x02 \x01(\t\"\xf8\x01\n\x17\x41\x62ortS3ObjectsUploadArg\x12o\n\x17objects_upload_info_vec\x18\x01 \x03(\x0b\x32N.cohesity.bridge.magneto.object_store.AbortS3ObjectsUploadArg.ObjectUploadInfo\x1al\n\x10ObjectUploadInfo\x12\x45\n\x0bobject_info\x18\x01 \x01(\x0b\x32\x30.cohesity.bridge.magneto.object_store.ObjectInfo\x12\x11\n\tupload_id\x18\x02 \x01(\t\"\xee\x02\n\x15RestoreObjectAreasArg\x12\x35\n\x04\x62\x61se\x18\x01 \x01(\x0b\x32\'.cohesity.bridge.magneto.RestoreBaseArg\x12h\n\x14object_area_info_vec\x18\x02 \x03(\x0b\x32J.cohesity.bridge.magneto.object_store.RestoreObjectAreasArg.ObjectAreaInfo\x1a\xb3\x01\n\x0eObjectAreaInfo\x12\x45\n\x0bobject_area\x18\x01 \x01(\x0b\x32\x30.cohesity.bridge.magneto.object_store.ObjectArea\x12\x11\n\tupload_id\x18\x02 \x01(\t\x12\x0f\n\x07part_id\x18\x03 \x01(\x05\x12\x36\n\x02\x65h\x18\x04 \x01(\x0b\x32*.cohesity.bridge.snap_fs.EntityHandleProto\".\n\x14GetObjectVersionsArg\x12\x16\n\x0eobject_key_vec\x18\x01 \x03(\t*(\n\x0cObjectAction\x12\x0b\n\x07kCreate\x10\x01\x12\x0b\n\x07kDelete\x10\x02')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'bridge.magneto.object_store.object_store_actions_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_OBJECTACTION']._serialized_start=5323
  _globals['_OBJECTACTION']._serialized_end=5363
  _globals['_OBJECTSTOREACTIONARG']._serialized_start=377
  _globals['_OBJECTSTOREACTIONARG']._serialized_end=2220
  _globals['_OBJECTSTOREACTIONARG_OBJECTSTOREACTIONTYPE']._serialized_start=1723
  _globals['_OBJECTSTOREACTIONARG_OBJECTSTOREACTIONTYPE']._serialized_end=2058
  _globals['_OBJECTSTORE']._serialized_start=2223
  _globals['_OBJECTSTORE']._serialized_end=2451
  _globals['_PREPAREBACKUPARG']._serialized_start=2454
  _globals['_PREPAREBACKUPARG']._serialized_end=2633
  _globals['_ENDBACKUPARG']._serialized_start=2636
  _globals['_ENDBACKUPARG']._serialized_end=2787
  _globals['_LISTOBJECTSMETADATAARG']._serialized_start=2790
  _globals['_LISTOBJECTSMETADATAARG']._serialized_end=2962
  _globals['_BACKUPOBJECTAREAARG']._serialized_start=2965
  _globals['_BACKUPOBJECTAREAARG']._serialized_end=3290
  _globals['_BACKUPOBJECTAREAARG_OBJECTAREAINFO']._serialized_start=3147
  _globals['_BACKUPOBJECTAREAARG_OBJECTAREAINFO']._serialized_end=3290
  _globals['_OBJECTINFO']._serialized_start=3292
  _globals['_OBJECTINFO']._serialized_end=3337
  _globals['_OBJECTAREA']._serialized_start=3340
  _globals['_OBJECTAREA']._serialized_end=3536
  _globals['_CREATEOBJECTSARG']._serialized_start=3539
  _globals['_CREATEOBJECTSARG']._serialized_end=3896
  _globals['_CREATEOBJECTSARG_OBJECTACTIONINFO']._serialized_start=3719
  _globals['_CREATEOBJECTSARG_OBJECTACTIONINFO']._serialized_end=3896
  _globals['_FINALIZECOHESITYOBJECTSARG']._serialized_start=3899
  _globals['_FINALIZECOHESITYOBJECTSARG']._serialized_end=4149
  _globals['_FINALIZECOHESITYOBJECTSARG_FINALIZECOHESITYOBJECTINFO']._serialized_start=4051
  _globals['_FINALIZECOHESITYOBJECTSARG_FINALIZECOHESITYOBJECTINFO']._serialized_end=4149
  _globals['_DELETEOBJECTVERSIONARG']._serialized_start=4151
  _globals['_DELETEOBJECTVERSIONARG']._serialized_end=4246
  _globals['_FINALIZES3OBJECTSARG']._serialized_start=4249
  _globals['_FINALIZES3OBJECTSARG']._serialized_end=4653
  _globals['_FINALIZES3OBJECTSARG_FINALIZES3OBJECTINFO']._serialized_start=4385
  _globals['_FINALIZES3OBJECTSARG_FINALIZES3OBJECTINFO']._serialized_end=4653
  _globals['_FINALIZES3OBJECTSARG_FINALIZES3OBJECTINFO_PARTINFO']._serialized_start=4612
  _globals['_FINALIZES3OBJECTSARG_FINALIZES3OBJECTINFO_PARTINFO']._serialized_end=4653
  _globals['_ABORTS3OBJECTSUPLOADARG']._serialized_start=4656
  _globals['_ABORTS3OBJECTSUPLOADARG']._serialized_end=4904
  _globals['_ABORTS3OBJECTSUPLOADARG_OBJECTUPLOADINFO']._serialized_start=4796
  _globals['_ABORTS3OBJECTSUPLOADARG_OBJECTUPLOADINFO']._serialized_end=4904
  _globals['_RESTOREOBJECTAREASARG']._serialized_start=4907
  _globals['_RESTOREOBJECTAREASARG']._serialized_end=5273
  _globals['_RESTOREOBJECTAREASARG_OBJECTAREAINFO']._serialized_start=5094
  _globals['_RESTOREOBJECTAREASARG_OBJECTAREAINFO']._serialized_end=5273
  _globals['_GETOBJECTVERSIONSARG']._serialized_start=5275
  _globals['_GETOBJECTVERSIONSARG']._serialized_end=5321
# @@protoc_insertion_point(module_scope)
